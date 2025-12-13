from tools.data_folder import DataFolder

from managers.tools.helpers import ManagerHelper

from world.commodity import Commodity

from text.dividers import SINGLE_DIVIDER, DIVIDER

COMM_PER_FACTION_TEMPLATE = 'hardcoded_inis/static_content/commodities_per_faction.ini'


class UniverseCommodity:
    def __init__(self, commodity):
        self.commodity = commodity
        self.base_commodity_db = {}
        self.base_commodity_list = []
        self.comm_producers = []
        self.consumer_per_price = {}
        self.consumers_list = []
        self.producers_scanned = False
        self.consumers_scanned = False

    def add_base_commodity(self, base_commodity):
        self.base_commodity_db[base_commodity.get_base_name()] = base_commodity
        self.base_commodity_list.append(base_commodity)

    def get_comm_name(self):
        return self.commodity.ALIAS

    def scan_producers(self):
        for base_commodity in self.base_commodity_list:
            if base_commodity.is_produce():
                self.comm_producers.append(base_commodity)

        self.producers_scanned = True

    def get_producers(self):
        if not self.producers_scanned:
            raise Exception(f'commodity {self.get_comm_name()} is not scanned for producers')

        return self.comm_producers

    def scan_consumers(self):
        for base_commodity in self.base_commodity_list:
            if base_commodity.is_consume():
                self.consumer_per_price[base_commodity.get_purchase_price()] = base_commodity

        self.consumer_per_price = dict(sorted(self.consumer_per_price.items()))
        self.consumers_list = list(self.consumer_per_price.items())
        self.consumers_scanned = True

    def get_best_consumer(self):
        if not self.consumers_scanned:
            raise Exception(f'commodity {self.get_comm_name()} is not scanned for consumers')

        return self.consumers_list[-1][1]


class StoreManager:
    def __init__(self, lancer_core):
        self.core = lancer_core
        self.ids = self.core.ids.commodity

        self.comms_db = {}
        self.comms_list = []
        self.universe_comms_db = {}
        self.universe_comms_list: list[UniverseCommodity] = []

        self.init_commoditites()

        self.sync_data()

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

    def get_commodities(self):
        return self.comms_list

    def compile_producers(self):
        for u_comm in self.universe_comms_list:
            u_comm.scan_producers()

    def compile_consumers(self):
        for u_comm in self.universe_comms_list:
            u_comm.scan_consumers()

    def get_comm_equip(self):
        return ManagerHelper.extract_equips(self.comms_list)

    def get_comm_good(self):
        return ManagerHelper.extract_goods(self.comms_list)

    def get_comms_per_factions(self):
        results = []
        for faction in self.core.factions.get_all():
            if not faction.is_listed():
                continue
            comms = []
            for comm in faction.get_commodities():
                comms.append(
                    f'MarketGood = {self.get_by_name(comm).get_nickname()}, 0, 0'
                )
            results.append(
                f'''[FactionGood]
faction = {faction.get_code()}
{SINGLE_DIVIDER.join(comms)}
'''
            )
        return DIVIDER.join(results)

    def get_comm_per_faction_content(self):
        context = {
            'generated': self.get_comms_per_factions(),
        }
        return self.core.tpl_manager.get_result(COMM_PER_FACTION_TEMPLATE, context)

    def sync_data(self):
        if not self.core.write:
            return

        data_folder = DataFolder(build_to_folder=self.core.build_folder)

        data_folder.sync_equip_hardcoded('commodities_per_faction', self.get_comm_per_faction_content())
