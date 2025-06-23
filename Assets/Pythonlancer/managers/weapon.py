from managers.tools.helpers import ManagerHelper
from managers.tools import query as Q

from world.equipment import Equipment
from world.gun import *
from world import launcher

from fx.weapon import WeaponFX


class NotExistLauncherException(Exception):
    pass


class WeaponManager:

    def __init__(self, lancer_core):
        self.core = lancer_core
        self.ids = self.core.ids.weapon

        self.weapon_factions = [i.WEAPON_FACTION for i in FactionGun.subclasses]
        self.launcher_types = [
            launcher.MainMissile,
            launcher.FastMissile,
            launcher.MainSuperMissile,
            launcher.ShieldMissile,
            launcher.CruiseDisruptor,
            launcher.Torpedo,
            launcher.CivMine,
            launcher.ProfMine,
            launcher.MilMine,
        ]

        self.guns_list = []
        self.single_guns_db = {}
        self.generic_guns_db = {i: {} for i in self.weapon_factions}

        self.generic_launchers_db = {}
        self.launchers_list = []

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

        for faction in ALL_FACTIONS:
            self.generic_launchers_db[faction] = {}

            for launcher in self.launcher_types:
                self.generic_launchers_db[faction][launcher.WEAPON_CODE] = {}

                for equipment_class in launcher.CLASSES_KEYS:
                    the_launcher = launcher(self.ids, faction, equipment_class)
                    self.generic_launchers_db[faction][launcher.WEAPON_CODE][equipment_class] = the_launcher
                    self.launchers_list.append(the_launcher)

    def get_guns_by_query(self, gun_query: Q.Gun):
        guns = []
        for the_class in gun_query.eq_classes:
            guns.append(
                self.get_gun_raw(gun_query.gun, the_class)
            )
        return guns

    def get_generic_guns_by_query(self, weapon_faction, gun_query: Q.GenericGun):
        guns = []
        if weapon_faction not in self.weapon_factions:
            raise Exception('weapon factions is not exist when try to get generic gun')

        for the_class in gun_query.eq_classes:
            guns.append(
                self.get_generic_gun(weapon_faction, gun_query.generic_kind, the_class)
            )
        return guns

    def get_generic_launchers_by_query(self, weapon_faction, launcher_query: Q.GenericLauncher):
        launchers = []
        if weapon_faction not in self.weapon_factions:
            raise Exception('weapon factions is not exist when try to get generic gun')

        for the_class in launcher_query.eq_classes:
            try:
                launchers.append(
                    self.get_generic_launcher(weapon_faction, launcher_query.launcher_kind, the_class)
                )
            except NotExistLauncherException:
                pass
        return launchers

    def get_gun_raw(self, gun_nickname, equipment_class):
        return self.single_guns_db[gun_nickname][equipment_class]

    def get_gun(self, gun, equipment_class):
        return self.single_guns_db[gun.BASE_NICKNAME][equipment_class]

    def get_generic_gun(self, weapon_faction, generic_kind, equipment_class):
        return self.generic_guns_db[weapon_faction][generic_kind][equipment_class]

    def get_generic_launcher(self, launcher_faction, launcher_kind, equipment_class):
        kind_launcher = self.generic_launchers_db[launcher_faction][launcher_kind]
        try:
            return kind_launcher[equipment_class]
        except KeyError:
            raise NotExistLauncherException('Such class is not exist for launcher')

    def get_weapon_equip(self):
        return ManagerHelper.extract_equips(self.guns_list, self.launchers_list)

    def get_weapon_good(self):
        return ManagerHelper.extract_goods(self.guns_list, self.launchers_list)

    def get_lootprops(self):
        return ManagerHelper.extract_lootprops(self.guns_list, self.launchers_list)

    def get_demo_marketdata(self):
        return ManagerHelper.extract_marketdata(self.guns_list, self.launchers_list)

    def get_ammo_items(self):
        return self.launchers_list
