from managers.tools.mixins import StringsMixin
from managers.tools.helpers import extract_equips, extract_goods, extract_lootprops

from text.strings import StringCompiler
from text.dividers import SINGLE_DIVIDER, DIVIDER

from world.equipment import Equipment
from world.gun import Gun


class WeaponManager(StringsMixin):

    def __init__(self, last_string_id, last_infocard_id):
        self.guns_db = {}
        self.guns_list = []

        self.last_string_id = last_string_id
        self.last_infocard_id = last_infocard_id

        self.load_game_data()

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
        return extract_equips(self.guns_list)

    def get_weapon_good(self):
        return extract_goods(self.guns_list)

    def get_lootprops(self):
        return extract_lootprops(self.guns_list)

    def get_ru_names(self):
        items = {gun.ids_name: gun.get_ru_name() for gun in self.guns_list}
        return StringCompiler.compile_names(items)

    def get_demo_marketdata(self):
        return SINGLE_DIVIDER.join([gun.get_marketdata() for gun in self.guns_list])
