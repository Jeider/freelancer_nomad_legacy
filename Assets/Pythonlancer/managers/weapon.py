from managers.tools.helpers import ManagerHelper

from text.strings import StringCompiler

from world.equipment import Equipment
from world.gun import Gun

from fx.weapon import WeaponFX


class WeaponManager(object):

    def __init__(self, lancer_core):
        self.core = lancer_core

        self.guns_db = {}
        self.guns_list = []

        self.load_game_data()

    def get_next_string_id(self):
        return self.core.get_next_equip_string_id()

    def get_next_infocard_id(self):
        return self.core.get_next_equip_infocard_id()

    def load_game_data(self):
        for gun in Gun.subclasses:
            self.guns_db[gun.BASE_NICKNAME] = {}

            for equipment_class in Equipment.BASE_CLASSES:
                the_gun = gun(
                    equipment_class=equipment_class, faction=gun.WEAPON_FACTION, 
                    ids_name=self.get_next_string_id(), ids_info=self.get_next_infocard_id(),
                    weapon_fx=WeaponFX(equip_class=equipment_class, faction=gun.FX_FACTION, fx_appearance=gun.FX_APPEARANCE)
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

    def get_ru_names(self):
        items = ManagerHelper.extract_ru_names(self.guns_list)
        return StringCompiler.compile_names(items)

    def get_ru_infocards(self):
        infocards = ManagerHelper.extract_ru_infocards(self.guns_list)
        return StringCompiler.compile_infocards(infocards)

    def get_demo_marketdata(self):
        return ManagerHelper.extract_marketdata(self.guns_list)
