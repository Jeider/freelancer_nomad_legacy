from world.equipment import Equipment, MainMiscEquip
from world.power import Power
from world.engine import Engine
from world.shield import Shield, ShieldNPC
from world.thruster import Thruster
from world.weapon import WeaponFactory


class MiscEquipManager(object):

    def __init__(self):
        self.engines_db = {}
        self.powerplants_db = {}
        self.shields_db = {}
        self.npc_shields_db = {}
        self.thrusters_db = {}

        self.load_game_data()

    def load_game_data(self):
        # shipclass-based equipment
        for shipclass in Equipment.SHIPCLASSES:
            self.engines_db[shipclass] = {}
            self.powerplants_db[shipclass] = {}
            self.shields_db[shipclass] = {}
            self.npc_shields_db[shipclass] = {}

            for equip_type in MainMiscEquip.ALL_EQUIP_TYPES:

                self.engines_db[shipclass][equip_type] = {}
                self.powerplants_db[shipclass][equip_type] = {}
                self.shields_db[shipclass][equip_type] = {}
                self.npc_shields_db[shipclass][equip_type] = {}

                for equipment_class in Equipment.BASE_CLASSES:
                    self.engines_db[shipclass][equip_type][equipment_class] = Engine(equip_type, shipclass, equipment_class, 500, 200)
                    self.powerplants_db[shipclass][equip_type][equipment_class] = Power(equip_type, shipclass, equipment_class, 500, 200)
                    self.shields_db[shipclass][equip_type][equipment_class] = Shield(equip_type, shipclass, equipment_class, 500, 200)
                    self.npc_shields_db[shipclass][equip_type][equipment_class] = ShieldNPC(equip_type, shipclass, equipment_class, 500, 200)

        # generic equipment
        for equip_type in MainMiscEquip.ALL_EQUIP_TYPES:
            self.thrusters_db[equip_type] = {}

            for equipment_class in Equipment.BASE_CLASSES:
                self.thrusters_db[equip_type][equipment_class] = Thruster(equip_type, equipment_class, 500, 200)

    def get_engine(self, shipclass, equip_type, equipment_class):
        return self.engines_db[shipclass][equip_type][equipment_class]

    def get_powerplant(self, shipclass, equip_type, equipment_class):
        return self.powerplants_db[shipclass][equip_type][equipment_class]

    def get_shield(self, shipclass, equip_type, equipment_class):
        return self.shields_db[shipclass][equip_type][equipment_class]

    def get_npc_shield(self, shipclass, equip_type, equipment_class):
        return self.npc_shields_db[shipclass][equip_type][equipment_class]

    def get_thruster(self, equip_type, equipment_class):
        return self.thrusters_db[equip_type][equipment_class]

