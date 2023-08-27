from text.strings import StringCompiler
from text.dividers import SINGLE_DIVIDER, DIVIDER

from world.equipment import Equipment
from world.gun import Gun


class WeaponManager(object):

    def __init__(self, initial_id):
        self.guns_db = {}
        self.guns_list = []

        self.last_string_id = initial_id

        self.load_game_data()

    def get_next_string_id(self):
        self.last_string_id += 1
        return self.last_string_id

    def load_game_data(self):
        for gun in Gun.subclasses:
            self.guns_db[gun.BASE_NICKNAME] = {}

            for equipment_class in Equipment.BASE_CLASSES:
                the_gun = gun(
                    equipment_class=equipment_class, faction=Equipment.FACTION_RH, 
                    ids_name=self.get_next_string_id(), ids_info=1
                )
                self.guns_db[gun.BASE_NICKNAME][equipment_class] = the_gun
                self.guns_list.append(the_gun)

    def get_gun(self, gun, equipment_class):
        return self.guns_db[gun.BASE_NICKNAME][equipment_class]

    def get_weapon_equip(self):
        data = ''

        for gun in self.guns_list:
            data += gun.get_equip() + DIVIDER

        return data

    def get_weapon_good(self):
        data = ''

        for gun in self.guns_list:
            data += gun.get_good() + DIVIDER

        return data

    def get_lootprops(self):
        data = ''

        for gun in self.guns_list:
            data += gun.get_lootprops() + DIVIDER

        return data

    def get_ru_names(self):
        items = {}

        for gun in self.guns_list:
            items[gun.ids_name] = gun.get_ru_name()

        return StringCompiler.compile_names(items)

    def get_weapon_equip(self):
        data = ''

        for gun in self.guns_list:
            data += gun.get_equip() + DIVIDER

        return data

    def get_demo_marketdata(self):
        data = ''

        for gun in self.guns_list:
            data += gun.get_marketdata() + SINGLE_DIVIDER

        data += SINGLE_DIVIDER

        return data
