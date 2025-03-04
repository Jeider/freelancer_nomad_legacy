from world.ship import Ship
from templates.hardcoded_inis.ships import ShiparchTemplate
from text.dividers import DIVIDER

from tools.data_folder import DataFolder


class ShiparchManager:
    def __init__(self, lancer_core):
        self.core = lancer_core
        self.misc_equip = self.core.misc_equip
        self.ids = self.core.ids.ship

        self.params = {}
        self.ships = []
        self.ships_db = {}

        for ship in Ship.subclasses:
            instance = ship(self.ids)
            self.params.update(instance.get_shiparch_params())
            self.ships.append(instance)
            self.ships_db[instance.ARCHETYPE] = instance

        self.sync_data()

    def get_ship_by_class(self, ship_class):
        return self.ships_db[ship_class.ARCHETYPE]

    def get_ship_by_archetype(self, archetype):
        return self.ships_db[archetype]

    def get_shiparch_content(self):
        return ShiparchTemplate().format(self.params)

    def get_ship_goods(self):
        data = ''

        for ship in self.ships:
            shipclass = ship.EQUIPMENT_SHIPCLASS
            equip_type = ship.PACKAGE_EQUIPMENT_TYPE
            equipment_class = ship.get_package_equipment_class()

            engine = self.misc_equip.get_engine(shipclass, equip_type, equipment_class).get_nickname()
            power = self.misc_equip.get_powerplant(shipclass, equip_type, equipment_class).get_nickname()
            shield = self.misc_equip.get_shield(shipclass, equip_type, equipment_class).get_nickname()

            data += ship.get_hull() + DIVIDER
            data += ship.get_package(shield, engine, power, ship.PACKAGE_LIGHT) + DIVIDER

        return data

    def sync_data(self):
        if not self.core.write:
            return
        DataFolder.sync_shiparch(self.get_shiparch_content())
