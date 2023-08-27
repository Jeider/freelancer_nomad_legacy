from universe.base import Base, EQUIP_CLASSES_PER_LEVEL
from universe.markets import EquipDealer, ShipDealer

from world.equipment import Equipment

from text.dividers import SINGLE_DIVIDER, DIVIDER


class UniverseManager(object):

    def __init__(self, misc_equip, weapons, shiparch):
        self.misc_equip = misc_equip
        self.weapons = weapons
        self.shiparch = shiparch

        self.bases = []
        self.equip_dealers_list = []
        self.ship_dealers_list = []

        self.load_bases()

    def load_bases(self):
        for base_class in Base.subclasses:
            base = base_class()
            self.bases.append(base)

            if base.LEVEL:
                equip_items = self.load_base_equip_items(base)
                dealer = EquipDealer(base.NAME, equip_items)
                self.equip_dealers_list.append(dealer)

            if len(base.SHIPS) > 0:
                dealer = ShipDealer(base.NAME, [self.shiparch.get_ship_by_archetype(ship.ARCHETYPE) for ship in base.SHIPS])
                self.ship_dealers_list.append(dealer)


    def load_base_equip_items(self, base):
        items = []
        if base.GUN:
            equip_classes = base.get_gun_classes()
            for equip_class in equip_classes:
                items.append(self.weapons.get_gun(base.GUN, equip_class))

        if base.ENGINE:
            equip_classes = base.get_engine_classes()
            for equip_class in equip_classes:
                for shipclass in Equipment.SHIPCLASSES:
                    items.append(self.misc_equip.get_engine(shipclass, base.ENGINE, equip_class))

        if base.POWER:
            equip_classes = base.get_power_classes()
            for equip_class in equip_classes:
                for shipclass in Equipment.SHIPCLASSES:
                    items.append(self.misc_equip.get_powerplant(shipclass, base.POWER, equip_class))

        if base.SHIELD:
            equip_classes = base.get_shield_classes()
            for equip_class in equip_classes:
                for shipclass in Equipment.SHIPCLASSES:
                    items.append(self.misc_equip.get_shield(shipclass, base.SHIELD, equip_class))

        if base.THRUSTER:
            equip_classes = base.get_thruster_classes()
            for equip_class in equip_classes:
                items.append(self.misc_equip.get_thruster(base.THRUSTER, equip_class))

        return items

    def get_market_equip(self):
        data = ''

        for dealer in self.equip_dealers_list:
            data += dealer.get_market_content() + DIVIDER

        return data

    def get_market_ships(self):
        data = ''

        for dealer in self.ship_dealers_list:
            data += dealer.get_market_content() + DIVIDER

        return data
