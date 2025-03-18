import operator

from universe.content import meta
from universe.content.main_objects import Jumpgate, DockableObject

from text.dividers import SINGLE_DIVIDER


class BaseEdge:
    def __init__(self, graph, root_object, jumper=True, depth=0):
        self.graph = graph
        self.root_object = root_object
        self.edges = []
        self.jumper = jumper
        self.depth = depth

    def add_edge(self, edge):
        self.edges.append(edge)

    def find_edges(self, depth):
        self.find_trade_edges(self.root_object, depth)

        if issubclass(self.root_object.__class__, Jumpgate):
            self.find_target_jumpgate(depth)

        return self.edges

    def find_trade_edges(self, root_object, depth):
        for the_conn in root_object.connections:
            for destination in the_conn.get_destination_objects():
                if destination != self.root_object and destination not in self.graph.used_objects:
                    new_edge = BaseEdge(self.graph, destination, depth=depth)
                    self.add_edge(new_edge)
                    self.graph.add_used_object(destination, depth)

    def find_target_jumpgate(self, depth):
        target_jumpgate = self.root_object.get_target_jumpgate()
        if target_jumpgate.system not in self.graph.loaded_systems:
            new_edge = BaseEdge(self.graph, target_jumpgate, jumper=False, depth=depth)
            self.add_edge(new_edge)
            self.graph.add_used_object(target_jumpgate, depth)
            self.graph.add_loaded_system(target_jumpgate.system)

    def __str__(self):
        return f'Edge {self.root_object.get_full_alias()} in {self.root_object.system.NAME}'


class BaseGraph:
    def __init__(self, root_object):
        self.root_object = root_object
        self.root_edge = BaseEdge(self, self.root_object, depth=0)
        self.used_objects = []
        self.loaded_systems = [root_object.system]
        self.depths_db = {}
        self.load_relations()

    def add_used_object(self, dockable_object, depth):
        self.used_objects.append(dockable_object)

        if issubclass(dockable_object.__class__, DockableObject):
            self.depths_db[dockable_object.get_base_nickname()] = depth

    def add_loaded_system(self, system):
        self.loaded_systems.append(system)

    def get_depth_by_base_name(self, base_name):
        return self.depths_db[base_name]

    def load_relations(self, max_depth=2000):
        edges = [self.root_edge]
        depth = 0
        while True:
            new_edges = []
            for edge in edges:
                new_edges.extend(edge.find_edges(depth=depth))

            if len(new_edges) == 0:
                break

            depth += 1
            if depth > max_depth:
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
        return BaseGraph(root_object=self.system_object)

    def load_empty_stores(self):
        for u_comm in self.core.store.get_universe_commodities():
            base_commodity = BaseCommodity(self, u_comm)
            self.base_commodities_db[u_comm.get_comm_name()] = base_commodity
            u_comm.add_base_commodity(base_commodity)

    def add_action(self, action):
        comm_name = action.get_comm_name()
        base_commodity = self.base_commodities_db[comm_name]
        base_commodity.change_state(action.get_comm_change())

        if comm_name in meta.PRODUCT_RELATIONS:
            for consume in meta.PRODUCT_RELATIONS[comm_name]:
                consume_commodity = self.base_commodities_db[comm_name]
                consume_commodity.change_state(meta.CONSUME)

    def parse_prop_actions(self):
        for objective in self.props.get_objectives():

            for action in objective.get_actions():
                self.add_action(action)

        for action in self.props.get_raw_actions():
            self.add_action(action)

    def compile_base(self):
        # print('SCAN BASE')
        # print(f'BASE: {self.get_name()}')
        self.load_graph()
        self.load_commodities()

    def get_debug_table(self):
        print(self.get_name())
        return (f'[{self.get_name()}]\n'
                f'{self.get_debug_commodities()}')

    def get_debug_commodities(self):
        items = []
        for base_comm in self.base_commodities_db.values():
            if base_comm.state_changed():
                items.append(base_comm.get_debug_info())

        return SINGLE_DIVIDER.join(items)

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
                    failed = 1
                    print(f'BASE: {self.get_name()}')
                    print(f'COMM: {base_comm.get_comm_name()}')
                    print(f'Graph not contain base {producer.get_base_name()}')
                    # debug_graph = self.get_base_graph()
                    # raise Exception(f'Graph not contain base {producer.get_base_name()}')

            if failed == 1:
                continue

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

            # print('1')





# sorted_by_second = sorted(data, key=lambda tup: tup[1])

class BaseCommodity:

    def __init__(self, base, universe_commodity):
        self.base = base
        self.universe_commodity = universe_commodity
        self.consume = False
        self.resell = False
        self.produce = 0
        self.purchase_price = 0

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

    def get_debug_info(self):
        if self.is_produce():
            return f'{self.get_comm_name()} = {self.get_produce_price()} (produce)'

        info = (
            'resell'
            if self.resell
            else 'consume'
        )

        return f'{self.get_comm_name()} = {self.get_purchase_price()} ({info})'
