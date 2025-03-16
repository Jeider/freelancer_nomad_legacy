from universe.content.main_objects import Jumpgate, DockableObject


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

    def add_used_object(self, dockable_object, depth):
        self.used_objects.append(dockable_object)

        if issubclass(dockable_object.__class__, DockableObject):
            self.depths_db[dockable_object.get_base_nickname()] = depth

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
        for objective in self.props.get_objectives():

            for store_change in objective.get_store_changes():
                base_commodity = self.base_commodities_db[store_change.get_comm_name()]
                base_commodity.add_to_stock(store_change.get_comm_change())


class BaseCommodity:

    def __init__(self, base, commodity, stock=0):
        self.base = base
        self.commodity = commodity
        self.stock = stock

    def get_name(self):
        return self.base.get_name()

    def add_to_stock(self, value):
        self.stock += value


