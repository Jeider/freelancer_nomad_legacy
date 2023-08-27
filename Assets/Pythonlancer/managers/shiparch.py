from world.ship import Ship
from templates.shiparch import ShiparchTemplate
from text.dividers import SINGLE_DIVIDER, DIVIDER


class ShiparchManager(object):

    def __init__(self, misc_equip):
        self.misc_equip = misc_equip

        self.params = {}
        self.ships = []

        for ship in Ship.subclasses:
            instance = ship()
            self.params.update(instance.get_shiparch_params())
            self.ships.append(instance)

    def get_file_content(self):
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
            data += ship.get_package(engine, power, shield, ship.PACKAGE_LIGHT) + DIVIDER

        return data
