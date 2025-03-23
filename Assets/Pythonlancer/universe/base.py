import operator

from world.names import DEFAULT, BASIC, ROID, ALLOY, PRODUCT, LUXURY, CONTRABAND

from universe.markets import Market, MarketCommodity

from universe.content import meta
from universe.content.main_objects import Jumpgate, DockableObject

from text.dividers import SINGLE_DIVIDER


class BaseEdge:
    def __init__(self, graph, root_object, depth=0):
        self.graph = graph
        self.root_object = root_object
        self.edges = []
        self.depth = depth

    def add_edge(self, edge):
        self.edges.append(edge)

    def find_edges(self, depth):
        self.find_trade_edges(self.root_object, depth)

        if issubclass(self.root_object.__class__, Jumpgate):
            self.find_target_jumpgate(depth)

        return self.edges

    def find_trade_edges(self, root_object, depth):
        if not root_object.connections:
            raise Exception(f'{root_object} have no connections')
        for the_conn in root_object.connections:
            for destination in the_conn.get_edge_objects():
                if destination != self.root_object and destination not in self.graph.used_objects:
                    new_edge = BaseEdge(self.graph, destination, depth=depth)
                    self.add_edge(new_edge)
                    self.graph.add_used_object(destination, depth)

    def find_target_jumpgate(self, depth):
        target_jumpgate = self.root_object.get_target_jumpgate()
        if target_jumpgate.system not in self.graph.loaded_systems and target_jumpgate.system.SCAN_JUMP:
            new_edge = BaseEdge(self.graph, target_jumpgate, depth=depth)
            self.add_edge(new_edge)
            self.graph.add_used_object(target_jumpgate, depth)
            self.graph.add_loaded_system(target_jumpgate.system)

    def __str__(self):
        return f'Edge {self.root_object.get_full_alias()} in {self.root_object.system.NAME}'


class BaseGraph:
    def __init__(self, root_object, resell_range=0):
        self.resell_range = resell_range
        self.resellers = []
        self.root_object = root_object
        self.root_edge = BaseEdge(self, self.root_object, depth=0)
        self.used_objects = []
        self.loaded_systems = [root_object.system]
        self.depths_db = {}
        self.depth = 0
        self.load_relations()
        if self.depth == 0:
            raise Exception(f'{self.root_object} have no connections')

    def add_used_object(self, dockable_object, depth):
        self.used_objects.append(dockable_object)

        if issubclass(dockable_object.__class__, DockableObject):
            self.depths_db[dockable_object.get_base_nickname()] = depth
            if depth < self.resell_range and dockable_object.have_trader():
                self.resellers.append(dockable_object)

    def add_loaded_system(self, system):
        self.loaded_systems.append(system)

    def get_depth_by_base_name(self, base_name):
        return self.depths_db[base_name]

    def load_relations(self, max_depth=2000):
        edges = [self.root_edge]
        self.depth = 0
        while True:
            new_edges = []
            for edge in edges:
                new_edges.extend(edge.find_edges(depth=self.depth))

            if len(new_edges) == 0:
                break

            self.depth += 1
            if self.depth > max_depth:
                break

            edges = new_edges


class Base:

    def __init__(self, core, system, system_object):
        self.core = core
        self.system = system
        self.system_object = system_object
        # self.props = self.system_object.BASE_PROPS if self.system_object.BASE_PROPS else DefaultBaseProps()
        self.props = self.system_object.BASE_PROPS

        if not self.props:
            raise Exception('Base props is not defined for base %s' % self.system_object.get_base_nickname())

        self.graph: BaseGraph | None = None

        self.base_commodities_db = {}

        self.load_empty_stores()

        if self.props:
            self.parse_prop_actions()

    def get_name(self):
        return self.system_object.get_base_nickname()

    def load_graph(self):
        self.graph = self.get_base_graph()

    def get_base_graph(self):
        return BaseGraph(root_object=self.system_object, resell_range=self.props.RESELL_GOODS_DEPTH_RANGE)

    def load_empty_stores(self):
        for u_comm in self.core.store.get_universe_commodities():
            base_commodity = BaseCommodity(self, u_comm)
            self.base_commodities_db[u_comm.get_comm_name()] = base_commodity
            u_comm.add_base_commodity(base_commodity)

    def add_action(self, action):
        comm_name = action.get_comm_name()
        base_commodity = self.base_commodities_db[comm_name]
        base_commodity.change_state(action.get_comm_change())

        if comm_name in meta.CONSUMES_PER_PRODUCE and base_commodity.is_produce():
            for consume in meta.CONSUMES_PER_PRODUCE[comm_name]:
                consume_commodity = self.base_commodities_db[consume]
                consume_commodity.change_state(meta.CONSUME)

    def parse_prop_actions(self):
        for objective in self.props.get_objectives():

            for action in objective.get_actions():
                self.add_action(action)

        for action in self.props.get_raw_actions():
            self.add_action(action)

    def load_resell_commodities(self, resell_commodities):
        for r_comm in resell_commodities:
            base_commodity = self.base_commodities_db[r_comm]
            base_commodity.change_state(meta.RESELL)

    def compile_base(self):
        # print('SCAN BASE')
        # print(f'BASE: {self.get_name()}')
        self.load_graph()
        self.load_resell_data()
        self.load_commodities()

    def get_commodity_market(self):
        return Market(
            base_nickname=self.get_name(),
            items=self.base_commodities_db.values(),
        )

    def get_debug_table(self):
        return (f'[{self.get_name()}]\n'
                f'{self.get_debug_commodities()}')

    def get_debug_commodities(self):
        items = []
        for base_comm in self.base_commodities_db.values():
            if base_comm.state_changed():
                items.append(base_comm.get_debug_info())

        return SINGLE_DIVIDER.join(items)

    def get_products(self):
        products = []
        for base_comm in self.base_commodities_db.values():
            if base_comm.is_produce():
                products.append(base_comm)
        return products

    def load_resell_data(self):
        resell_commodities = set()
        # if len(self.graph.resellers):
        #     print(f'BASE RESSELLER: {self.get_name()}')
        for reseller in self.graph.resellers:
            reseller_base = self.system.universe_manager.get_base_by_name(reseller.get_base_nickname())
            # print(reseller_base.system_object)
            for product in reseller_base.get_products():
                for kind in self.props.RESELL_TYPES:
                    if any((
                            kind == DEFAULT and product.commodity.IS_DEFAULT,
                            kind == BASIC and product.commodity.IS_BASIC,
                            kind == ROID and product.commodity.IS_ROID,
                            kind == ALLOY and product.commodity.IS_ALLOY,
                            kind == PRODUCT and product.commodity.IS_DEFAULT,
                            kind == LUXURY and product.commodity.IS_LUXURY,
                            kind == CONTRABAND and product.commodity.IS_CONTRABAND,
                            )):
                        resell_commodities.add(product.get_comm_name())
                        continue

        self.load_resell_commodities(resell_commodities)

    def load_commodities(self):
        if not self.graph:
            raise Exception('graph is required')

        for base_comm in self.base_commodities_db.values():
            if not base_comm.is_consume():
                continue

            failed = 0

            # print(f'COMM: {base_comm.get_comm_name()}')

            producers = base_comm.universe_commodity.get_producers()
            if not len(producers):
                raise Exception(f'no producers for commodity {base_comm.get_comm_name()}')

            depth_map = []
            for producer in producers:
                try:
                    depth = self.graph.get_depth_by_base_name(producer.get_base_name())
                    depth_map.append((depth, producer))
                except KeyError:
                    # failed = 1
                    # print(f'BASE: {self.get_name()}')
                    # print(f'COMM: {base_comm.get_comm_name()}')
                    # print(f'Graph not contain base {producer.get_base_name()}')
                    raise Exception(f'Graph not contain base {producer.get_base_name()}')
            #
            # if failed == 1:
            #     continue

            cheapest_producers_price = []
            min_depth = (min(depth_map, key=operator.itemgetter(0)))[0]
            for depth, producer in depth_map:
                if depth == min_depth:
                    cheapest_producers_price.append(producer.get_produce_price())

            produce_price = (
                min(cheapest_producers_price)
                if len(cheapest_producers_price) > 0
                else cheapest_producers_price[0]
            )

            purchase_price = base_comm.universe_commodity.commodity.get_consume_price(
                produce_price=produce_price,
                depth=min_depth,
            )

            base_comm.set_purchase_price(purchase_price)


class BaseCommodity(MarketCommodity):

    def __init__(self, base, universe_commodity):
        self.base = base
        self.universe_commodity = universe_commodity
        self.consume = False
        self.resell = False
        self.produce = 0
        self.purchase_price = 0

    @property
    def commodity(self):
        return self.universe_commodity.commodity

    def get_nickname(self):
        return self.commodity.get_nickname()

    def get_price(self):
        if self.is_consume():
            purchase_price = self.get_purchase_price()
            if purchase_price == 0:
                raise Exception(f'No purchase price for commodity {self.get_comm_name()} on {self.get_base_name()}')
            return purchase_price
        elif self.is_produce():
            return self.get_produce_price()

        return self.commodity.get_default_price()

    def get_price_percent(self):
        price_pct = ((self.get_price() * 100) / self.commodity.get_default_price()) / 100
        return f'{price_pct}'  # ;;; {self.get_price()} -- ({self.get_debug_mark()})'

    def get_base_name(self):
        return self.base.get_name()

    def get_comm_name(self):
        return self.universe_commodity.get_comm_name()

    def state_changed(self):
        return self.is_consume() or self.is_produce()

    def set_purchase_price(self, price):
        self.purchase_price = price

    def get_purchase_price(self):
        return self.purchase_price

    def is_produce(self):
        return self.produce > 0

    def is_consume(self):
        return self.consume or self.resell

    def in_stock(self):
        return self.resell or self.produce > 0

    def is_best_price(self):
        return meta.PRODUCE_CHEAP < self.produce

    def is_cheap_price(self):
        return meta.PRODUCE_NORMAL < self.produce <= meta.PRODUCE_CHEAP

    def is_normal_price(self):
        return meta.PRODUCE_BAD < self.produce <= meta.PRODUCE_NORMAL

    def is_bad_price(self):
        return 0 < self.produce <= meta.PRODUCE_BAD

    def get_produce_price(self):
        if self.is_best_price():
            return self.universe_commodity.commodity.get_best_price()
        if self.is_cheap_price():
            return self.universe_commodity.commodity.get_cheap_price()
        if self.is_normal_price():
            return self.universe_commodity.commodity.get_normal_price()
        if self.is_bad_price():
            return self.universe_commodity.commodity.get_bad_price()

        raise Exception('unknown produce state')

    def change_state(self, state):
        if state == meta.RESELL:
            self.resell = True
        elif state == meta.CONSUME:
            self.consume = True
        elif state > 0:
            self.produce += state
        else:
            raise Exception('Unknown state %d' % state)

    def get_debug_mark(self):
        if self.is_produce():
            return 'produce'

        if self.resell:
            return 'resell'

        if self.consume:
            return 'consume'

        return 'default'

    def get_debug_info(self):
        return f'{self.get_comm_name()} = {self.get_purchase_price()} ({self.get_debug_mark()})'
