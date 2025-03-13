from world.commodity import Commodity, DefaultCommodity, BasicCommodity, Roid, Alloy, Product
from world.names import *


class UniverseCommodity:
    def __init__(self, commodity):
        self.commodity = commodity
        self.base_commodity_db = {}
        self.base_commodity_list = []

    def add_base_commodity(self, base_commodity):
        self.base_commodity_db[base_commodity.get_name()] = base_commodity
        self.base_commodity_list.append(base_commodity)

    def get_comm_name(self):
        return self.commodity.ALIAS


class StoreManager:
    def __init__(self, lancer_core):
        self.core = lancer_core
        self.ids = self.core.ids.equip

        self.comms_db = {}
        self.comms_list = []
        self.universe_comms_db = {}
        self.universe_comms_list = []

        self.universe_basics = []
        self.universe_defaults = []
        self.universe_roids = []
        self.universe_alloys = []
        self.universe_products = []

        self.init_commoditites()

    def init_commoditites(self):
        for commodity in Commodity.subclasses:
            comm = commodity(ids=self.ids)
            universe_comm = UniverseCommodity(comm)

            self.comms_db[comm.ALIAS] = comm
            self.comms_list.append(comm)

            self.universe_comms_db[comm.ALIAS] = universe_comm
            self.universe_comms_list.append(universe_comm)

            the_class = commodity.__class__

            if issubclass(the_class, DefaultCommodity):
                self.universe_defaults.append(comm)

            elif issubclass(the_class, BasicCommodity):
                self.universe_basics.append(comm)

            elif issubclass(the_class, Roid):
                self.universe_roids.append(comm)

            elif issubclass(the_class, Alloy):
                self.universe_alloys.append(comm)

            elif issubclass(the_class, Product):
                self.universe_products.append(comm)

    def get_by_name(self, name):
        return self.comms_db[name]

    def get_universe_commodities(self):
        return self.universe_comms_list
