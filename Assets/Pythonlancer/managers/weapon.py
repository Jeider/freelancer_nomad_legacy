from world.equipment import Equipment
from world.gun import Gun


class WeaponManager(object):

    def __init__(self):
        self.guns_db = {}

        self.load_game_data()

    def load_game_data(self):
        for gun in Gun.RH_GUNS:
            self.guns_db[gun['base_nickname']] = {}

            for equipment_class in Equipment.BASE_CLASSES:
                self.guns_db[gun['base_nickname']][equipment_class] = Gun(equipment_class=equipment_class, faction=Equipment.FACTION_RH, **gun)

    def get_gun(self, gun_base_nickname, equipment_class):
        return self.guns_db[gun_base_nickname][equipment_class]
