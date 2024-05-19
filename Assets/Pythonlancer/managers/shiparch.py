from world.ship import Ship
from templates.hardcoded_inis.ships import ShiparchTemplate
from text.dividers import DIVIDER
from text.infocards import InfocardBuilder, INFO_SHIP_ABOUT, INFO_SHIP_TABLE, INFO_SHIP_KEYS, INFO_SHIP_VALUES
from text.strings import StringCompiler

from tools.data_folder import DataFolder


class ShiparchManager(object):

    def __init__(self, lancer_core):
        self.core = lancer_core
        self.misc_equip = self.core.misc_equip

        self.params = {}
        self.ships = []
        self.ships_db = {}

        for ship in Ship.subclasses:
            instance = ship(
                self.get_next_string_id(),
                self.get_next_infocard_id(),
                self.get_next_infocard_id(),
                self.get_next_infocard_id(),
                self.get_next_infocard_id(),
            )
            self.params.update(instance.get_shiparch_params())
            self.ships.append(instance)
            self.ships_db[instance.ARCHETYPE] = instance

        self.sync_data()

    def get_next_string_id(self):
        return self.core.get_next_ship_string_id()

    def get_next_infocard_id(self):
        return self.core.get_next_ship_infocard_id()

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

    def get_ship_ru_names(self):
        items = {}

        for ship in self.ships:
            items[ship.ids_name] = ship.get_ru_name()

        return StringCompiler.compile_names(items)

    def get_ship_ru_infocards(self):
        infocards = {}

        for ship in self.ships:
            ship_stats = ship.get_infocard_values()
            infocards[ship.ids_info] = InfocardBuilder.build_infocard(INFO_SHIP_TABLE, ship_stats)
            infocards[ship.ids_info1] = InfocardBuilder.build_infocard(INFO_SHIP_ABOUT, {})
            infocards[ship.ids_info2] = InfocardBuilder.build_infocard(INFO_SHIP_KEYS, {})
            infocards[ship.ids_info3] = InfocardBuilder.build_infocard(INFO_SHIP_VALUES, ship_stats)

        return StringCompiler.compile_infocards(infocards)

    def sync_data(self):
        DataFolder.sync_shiparch(self.get_shiparch_content())
