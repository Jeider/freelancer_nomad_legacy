from world.commodity import Commodity, DefaultCommodity, BasicCommodity, Roid, Alloy, Product
from world.names import *


class UniverseCommodity:
    def __init__(self, commodity):
        self.commodity = commodity
        self.base_commodity_db = {}
        self.base_commodity_list = []
        self.comm_producers = []
        self.scanned = False

    def add_base_commodity(self, base_commodity):
        self.base_commodity_db[base_commodity.get_base_name()] = base_commodity
        self.base_commodity_list.append(base_commodity)

    def get_comm_name(self):
        return self.commodity.ALIAS

    def scan_bases(self):
        for base_commodity in self.base_commodity_list:
            if base_commodity.is_produce():
                self.comm_producers.append(base_commodity)

        self.scanned = True

    def get_producers(self):
        if not self.scanned:
            raise Exception(f'commodity {self.get_comm_name()} is not scanned')

        return self.comm_producers


class StoreManager:
    def __init__(self, lancer_core):
        self.core = lancer_core
        self.ids = self.core.ids.equip

        self.comms_db = {}
        self.comms_list = []
        self.universe_comms_db = {}
        self.universe_comms_list = []

        self.init_commoditites()

    def init_commoditites(self):
        for commodity in Commodity.subclasses:
            if not commodity.BASE_COMMODITY:
                continue

            comm = commodity(ids=self.ids)
            universe_comm = UniverseCommodity(comm)

            self.comms_db[comm.ALIAS] = comm
            self.comms_list.append(comm)

            self.universe_comms_db[comm.ALIAS] = universe_comm
            self.universe_comms_list.append(universe_comm)

    def get_by_name(self, name):
        return self.comms_db[name]

    def get_universe_commodities(self):
        return self.universe_comms_list

    def compile_commodities(self):
        for u_comm in self.universe_comms_list:
            u_comm.scan_bases()
