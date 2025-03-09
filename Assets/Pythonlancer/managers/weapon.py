from managers.tools.helpers import ManagerHelper

from text.strings import StringCompiler

from world.equipment import Equipment
from world.gun import *

from fx.weapon import WeaponFX


def validate_eq(value):
    if type(value) is not list:
        raise Exception('Eq classes should be list')


class GunQuery:
    def __init__(self, gun, eq_classes):
        self.gun = gun
        self.eq_classes = validate_eq(eq_classes)


class GenericGunQuery:
    def __init__(self, generic_kind, eq_classes):
        self.generic_kind = generic_kind
        self.eq_classes = validate_eq(eq_classes)


class WeaponManager:

    def __init__(self, lancer_core):
        self.core = lancer_core
        self.ids = self.core.ids.equip

        self.guns_list = []
        self.single_guns_db = {}
        self.generic_guns_db = {i.WEAPON_FACTION: {} for i in FactionGun.subclasses}

        self.load_game_data()

    def load_game_data(self):
        for gun in Gun.subclasses:
            self.single_guns_db[gun.BASE_NICKNAME] = {}

            for equipment_class in Equipment.BASE_CLASSES:
                the_gun = gun(
                    self.ids,
                    equipment_class=equipment_class, faction=gun.WEAPON_FACTION,
                    weapon_fx=WeaponFX(
                        equip_class=equipment_class,
                        faction=gun.FX_FACTION,
                        fx_appearance=gun.FX_APPEARANCE
                    )
                )
                self.single_guns_db[gun.BASE_NICKNAME][equipment_class] = the_gun
                self.guns_list.append(the_gun)

            if gun.is_generic():
                self.generic_guns_db[gun.WEAPON_FACTION][gun.GENERIC_KIND] = self.single_guns_db[gun.BASE_NICKNAME]

    def get_guns_by_query(self, gun_query: GunQuery):
        guns = []
        for the_class in gun_query.eq_classes:
            guns.append(
                self.get_gun(gun_query.gun, the_class)
            )
        return guns

    def get_generic_guns_by_query(self, weapon_faction, gun_query: GenericGunQuery):
        guns = []
        for the_class in gun_query.eq_classes:
            guns.append(
                self.get_generic_gun(weapon_faction, gun_query.generic_kind, the_class)
            )
        return guns

    def get_gun(self, gun, equipment_class):
        return self.single_guns_db[gun.BASE_NICKNAME][equipment_class]

    def get_generic_gun(self, weapon_faction, generic_kind, equipment_class):
        return self.generic_guns_db[weapon_faction][generic_kind][equipment_class]

    def get_weapon_equip(self):
        return ManagerHelper.extract_equips(self.guns_list)

    def get_weapon_good(self):
        return ManagerHelper.extract_goods(self.guns_list)

    def get_lootprops(self):
        return ManagerHelper.extract_lootprops(self.guns_list)

    def get_demo_marketdata(self):
        return ManagerHelper.extract_marketdata(self.guns_list)
