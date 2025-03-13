from universe.content.main_objects import Jumpgate


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
        if issubclass(self.root_object.__class__, Jumpgate) and self.jumper is True:
            return self.find_target_jumpgate(depth)

        return self.find_trade_edges(self.root_object, depth)

    def find_trade_edges(self, root_object, depth):
        for the_conn in root_object.connections:
            for destination in the_conn.get_destination_objects():
                if destination != self.root_object and destination not in self.graph.used_objects:
                    new_edge = BaseEdge(self.graph, destination, depth=depth)
                    self.add_edge(new_edge)
                    self.graph.add_used_object(destination, depth)
        return self.edges

    def find_target_jumpgate(self, depth):
        target_jumpgate = self.root_object.get_target_jumpgate()
        new_edge = BaseEdge(self.graph, target_jumpgate, jumper=False, depth=depth)
        self.add_edge(new_edge)
        self.graph.add_used_object(target_jumpgate, depth)
        return self.edges

    def __str__(self):
        return f'Edge {self.root_object.get_full_alias()} in {self.root_object.system.NAME}'


class BaseGraph:
    def __init__(self, root_object):
        self.root_object = root_object
        self.root_edge = BaseEdge(self, self.root_object, depth=0)
        self.used_objects = []
        self.depths_db = {}
        self.load_relations()

    def add_used_object(self, edge, depth):
        self.used_objects.append(edge)
        self.depths_db[edge.root_object.get_base_nickname()] = depth

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
        self.graph = None

        self.base_commodities_db = {}

        self.load_empty_stores()

        if self.props:
            self.parse_objectives()

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

    def parse_objectives(self):
        print(self.props.__class__.__name__)
        for objective in self.props.get_objectives():

            for store_change in objective.get_store_changes():
                base_commodity = self.base_commodities_db[store_change.get_comm_name()]
                base_commodity.add_to_stock(store_change.get_comm_change())


POP_XLARGE_PLANET = 10
POP_LARGE_PLANET = 9
POP_MINING_PLANET = 8
POP_ULTRA_MEGABASE = 7
POP_MEGABASE = 6
POP_MEDIUM_BASE = 5
POP_SMALL_BASE = 4
POP_XSMALL_BASE = 3


class BaseProps:
    DEFAULT_POPULATION = None

    def __init__(self, *args):
        self.objectives = args

    def get_objectives(self):
        return self.objectives


class DefaultBaseProps(BaseProps):
    DEFAULT_POPULATION = POP_XSMALL_BASE


class LargePlanet(BaseProps):
    DEFAULT_POPULATION = POP_LARGE_PLANET


class LargeTradingBase(BaseProps):
    pass


class SmallTradingBase(LargeTradingBase):
    pass


class Megabase(BaseProps):
    DEFAULT_POPULATION = POP_MEGABASE


class MediumStation(BaseProps):
    DEFAULT_POPULATION = POP_MEDIUM_BASE


class BaseCommodity:

    def __init__(self, base, commodity, stock=0):
        self.base = base
        self.commodity = commodity
        self.stock = stock

    def get_name(self):
        return self.base.get_name()

    def add_to_stock(self, value):
        self.stock += value


STOCK_MAXIMAL = 700
STOCK_XLARGE = 600
STOCK_LARGE = 500
STOCK_MEDIUM = 400
STOCK_SMALL = 300
STOCK_XSMALL = 200
STOCK_MINIMAL = 100

CONSUME_MAXIMAL = 700
CONSUME_XLARGE = 600
CONSUME_LARGE = 500
CONSUME_MEDIUM = 400
CONSUME_SMALL = 300
CONSUME_XSMALL = 200
CONSUME_MINIMAL = 100


class CommodityAction:

    def __init__(self, comm_name, value, consume=False):
        self.comm_name = comm_name
        self.value = value
        self.consume = consume

    def get_comm_name(self):
        return self.comm_name

    def get_comm_change(self):
        return -self.value if self.consume else self.value


class BaseObjective:

    def __init__(self, comm_name, level: int):
        self.comm_name = comm_name
        self.level = level

    def get_store_changes(self):
        return self.get_main_actions() + self.get_side_effects()

    def get_main_actions(self):
        return []

    def get_side_effects(self):
        return []


class MineRoid(BaseObjective):

    def get_main_actions(self):
        return [
            CommodityAction(self.comm_name, self.level),
        ]


class ConsumeRoid(BaseObjective):

    def get_store_changes(self):
        return [
            CommodityAction(self.comm_name, -self.level),
        ]
