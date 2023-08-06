from text.strings import StringCompiler

from world.equipment import Equipment, MainMiscEquip
from world.power import Power
from world.engine import Engine
from world.shield import Shield, ShieldNPC
from world.thruster import Thruster
from world.armor import ArmorNPC
from world.ship import Ship

SINGLE_DIVIDER = "\n"
DIVIDER = "\n\n"


class MiscEquipManager(object):

    def __init__(self, last_string_id):
        self.engines_db = {}
        self.engines_list = []
        self.powerplants_db = {}
        self.powerplants_list = []
        self.shields_db = {}
        self.shields_list = []
        self.npc_shields_db = {}
        self.npc_shields_list = []
        self.thrusters_db = {}
        self.thrusters_list = []
        self.npc_armors_db = {}
        self.npc_armors_list = []

        self.last_string_id = last_string_id

        self.load_game_data()

    def get_next_string_id(self):
        self.last_string_id += 1
        return self.last_string_id

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
                    engine = Engine(equip_type, shipclass, equipment_class, self.get_next_string_id(), 1)
                    self.engines_db[shipclass][equip_type][equipment_class] = engine
                    self.engines_list.append(engine)

                    powerplant = Power(equip_type, shipclass, equipment_class, self.get_next_string_id(), 1)
                    self.powerplants_db[shipclass][equip_type][equipment_class] = powerplant
                    self.powerplants_list.append(powerplant)

                    shield_name_id = self.get_next_string_id()

                    shield = Shield(equip_type, shipclass, equipment_class, shield_name_id, 1)
                    self.shields_db[shipclass][equip_type][equipment_class] = shield
                    self.shields_list.append(shield)

                    shield_npc = ShieldNPC(equip_type, shipclass, equipment_class, shield_name_id, 1)
                    self.npc_shields_db[shipclass][equip_type][equipment_class] = shield_npc
                    self.npc_shields_list.append(shield_npc)

        # generic equipment
        for equip_type in MainMiscEquip.ALL_EQUIP_TYPES:
            self.thrusters_db[equip_type] = {}

            for equipment_class in Equipment.BASE_CLASSES:
                thruster = Thruster(equip_type, equipment_class, self.get_next_string_id(), 1)
                self.thrusters_db[equip_type][equipment_class] = thruster
                self.thrusters_list.append(thruster)

        # NPC shiparch features

        for armor_index, armor_scale in Ship.ARMOR_INDICES.items():
            npc_armor = ArmorNPC(armor_index, armor_scale)
            self.npc_armors_db[armor_index] = npc_armor
            self.npc_armors_list.append(npc_armor)

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

    def get_npc_armor(self, armor_index):
        return self.npc_armors_db[armor_index]

    def get_engine_equip(self):
        data = ''

        for engine in self.engines_list:
            data += engine.get_equip() + DIVIDER

        return data

    def get_engine_good(self):
        data = ''

        for engine in self.engines_list:
            data += engine.get_good() + DIVIDER

        return data

    def get_powerplant_equip(self):
        data = ''

        for powerplant in self.powerplants_list:
            data += powerplant.get_equip() + DIVIDER

        return data

    def get_powerplant_good(self):
        data = ''

        for powerplant in self.powerplants_list:
            data += powerplant.get_good() + DIVIDER

        return data

    def get_st_equip(self):
        data = ''

        for shield in self.shields_list:
            data += shield.get_equip() + DIVIDER

        for shield in self.npc_shields_list:
            data += shield.get_equip() + DIVIDER

        for thruster in self.thrusters_list:
            data += thruster.get_equip() + DIVIDER

        return data

    def get_st_good(self):
        data = ''

        for shield in self.shields_list:
            data += shield.get_good() + DIVIDER

        for shield in self.npc_shields_list:
            data += shield.get_good() + DIVIDER

        for thruster in self.thrusters_list:
            data += thruster.get_good() + DIVIDER

        return data

    def get_select_equip(self):
        data = ''

        for armor in self.npc_armors_list:
            data += armor.get_equip() + DIVIDER

        return data

    def get_lootprops(self):
        data = ''

        for engine in self.engines_list:
            data += engine.get_lootprops() + DIVIDER

        for powerplant in self.powerplants_list:
            data += powerplant.get_lootprops() + DIVIDER

        for shield in self.shields_list:
            data += shield.get_lootprops() + DIVIDER

        for shield in self.npc_shields_list:
            data += shield.get_lootprops() + DIVIDER

        for thruster in self.thrusters_list:
            data += thruster.get_lootprops() + DIVIDER

        return data

    def get_ru_names(self):
        items = {}

        for engine in self.engines_list:
            items[engine.ids_name] = engine.get_ru_name()

        for powerplant in self.powerplants_list:
            items[powerplant.ids_name] = powerplant.get_ru_name()

        for shield in self.shields_list:
            items[shield.ids_name] = shield.get_ru_name()

        for thruster in self.thrusters_list:
            items[thruster.ids_name] = thruster.get_ru_name()

        return StringCompiler.compile_names(items)

    def get_demo_marketdata(self):
        data = ''

        for engine in self.engines_list:
            data += engine.get_marketdata() + SINGLE_DIVIDER

        data += SINGLE_DIVIDER

        for powerplant in self.powerplants_list:
            data += powerplant.get_marketdata() + SINGLE_DIVIDER

        data += SINGLE_DIVIDER

        for shield in self.shields_list:
            data += shield.get_marketdata() + SINGLE_DIVIDER

        data += SINGLE_DIVIDER

        for thruster in self.thrusters_list:
            data += thruster.get_marketdata() + SINGLE_DIVIDER

        data += SINGLE_DIVIDER

        return data
