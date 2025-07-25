from world.ship import Ship
from world.capital import Capital
from templates.hardcoded_inis.ships import ShiparchTemplate
from text.dividers import DIVIDER

from tools.data_folder import DataFolder

SHIPARCH_TEMPLATE = 'hardcoded_inis/static_content/shiparch.ini'
FUSE_GEN_CAPITAL = 'fuse_gen_capital'


class ShiparchManager:
    def __init__(self, lancer_core):
        self.core = lancer_core
        self.misc_equip = self.core.misc_equip
        self.ids = self.core.ids.ship

        self.params = {}
        self.ships = []
        self.ships_db = {}
        self.capitals = []
        self.capitals_db = {}

        self.shiparch_context = {}
        shiparch_loaded = False

        for ship in Ship.subclasses:
            instance = ship(self.ids)
            self.shiparch_context[ship.TEMPLATE_CODE] = instance
            self.ships.append(instance)
            self.ships_db[instance.ARCHETYPE] = instance

        for capital in Capital.subclasses:
            instance = capital(self.ids)
            self.shiparch_context[capital.TEMPLATE_CODE] = instance
            self.capitals.append(instance)
            self.capitals_db[instance.ARCHETYPE] = instance

        self.sync_data()

    def get_ship_by_class(self, ship_class):
        return self.ships_db[ship_class.ARCHETYPE]

    def get_ship_by_archetype(self, archetype):
        return self.ships_db[archetype]

    def validate_shiparch(self):
        for ship in self.ships:
            if not ship.is_used():
                raise Exception(f'ship {ship} is not used')

    def get_shiparch_content(self):
        shiparch = self.core.tpl_manager.get_result(SHIPARCH_TEMPLATE, self.shiparch_context)
        self.validate_shiparch()
        self.shiparch_loaded = True
        return shiparch

    def get_ship_goods(self):
        data = []

        for ship in self.ships:
            shipclass = ship.EQUIPMENT_SHIPCLASS
            equip_type = ship.PACKAGE_EQUIPMENT_TYPE
            equipment_class = ship.get_package_equipment_class()

            engine = self.misc_equip.get_engine(shipclass, equip_type, equipment_class).get_nickname()
            power = self.misc_equip.get_powerplant(shipclass, equip_type, equipment_class).get_nickname()
            shield = self.misc_equip.get_shield(shipclass, equip_type, equipment_class).get_nickname()

            data.append(ship.get_hull())
            data.append(ship.get_package(shield, engine, power, ship.PACKAGE_LIGHT))

        return DIVIDER.join(data)

    def get_fuses(self):
        fuses = []
        for capital in self.capitals:
            fuses.append(capital.get_part_fuses_definitions())
        return DIVIDER.join(fuses)

    def sync_data(self):
        if not self.core.write:
            return
        DataFolder.sync_shiparch(self.get_shiparch_content())
        DataFolder.sync_fuse(FUSE_GEN_CAPITAL, self.get_fuses())
