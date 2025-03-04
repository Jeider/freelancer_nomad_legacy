from managers.tools.helpers import ManagerHelper

from text.strings import StringCompiler

from world.equipment import Equipment
from world.gun import Gun

from fx.weapon import WeaponFX


class WeaponManager:

    def __init__(self, lancer_core):
        self.core = lancer_core
        self.ids = self.core.ids.equip

        self.guns_db = {}
        self.guns_list = []

        self.load_game_data()

    def load_game_data(self):
        for gun in Gun.subclasses:
            self.guns_db[gun.BASE_NICKNAME] = {}

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
                self.guns_db[gun.BASE_NICKNAME][equipment_class] = the_gun
                self.guns_list.append(the_gun)

    def get_gun(self, gun, equipment_class):
        return self.guns_db[gun.BASE_NICKNAME][equipment_class]

    def get_weapon_equip(self):
        return ManagerHelper.extract_equips(self.guns_list)

    def get_weapon_good(self):
        return ManagerHelper.extract_goods(self.guns_list)

    def get_lootprops(self):
        return ManagerHelper.extract_lootprops(self.guns_list)

    def get_demo_marketdata(self):
        return ManagerHelper.extract_marketdata(self.guns_list)
