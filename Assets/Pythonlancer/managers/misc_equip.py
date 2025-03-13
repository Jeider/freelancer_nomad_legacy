from managers.tools.helpers import ManagerHelper
from managers.tools import query as Q

from world.equipment import Equipment, MainMiscEquip
from world.power import Power
from world.engine import Engine
from world.shield import Shield, ShieldNPC
from world.thruster import Thruster
from world.armor import ArmorNPC
from world.ship import Ship


class MiscEquipManager:

    def __init__(self, lancer_core):
        self.core = lancer_core

        self.ids = self.core.ids.equip

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
                    equip_props = {
                        'ids': self.ids, 'equip_type': equip_type,
                        'ship_class': shipclass, 'equipment_class': equipment_class
                    }
                    engine = Engine(**equip_props)
                    self.engines_db[shipclass][equip_type][equipment_class] = engine
                    self.engines_list.append(engine)

                    powerplant = Power(**equip_props)
                    self.powerplants_db[shipclass][equip_type][equipment_class] = powerplant
                    self.powerplants_list.append(powerplant)

                    shield = Shield(**equip_props)
                    self.shields_db[shipclass][equip_type][equipment_class] = shield
                    self.shields_list.append(shield)

                    shield_npc = ShieldNPC(**equip_props)
                    self.npc_shields_db[shipclass][equip_type][equipment_class] = shield_npc
                    self.npc_shields_list.append(shield_npc)

        # generic equipment
        for equip_type in MainMiscEquip.ALL_EQUIP_TYPES:
            self.thrusters_db[equip_type] = {}

            for equipment_class in Equipment.BASE_CLASSES:
                thruster = Thruster(self.ids, equip_type, equipment_class)
                self.thrusters_db[equip_type][equipment_class] = thruster
                self.thrusters_list.append(thruster)

        # NPC shiparch features

        for armor_index, armor_scale in Ship.ARMOR_INDICES.items():
            npc_armor = ArmorNPC(armor_index, armor_scale)
            self.npc_armors_db[armor_index] = npc_armor
            self.npc_armors_list.append(npc_armor)

    def get_shipclass_item_by_query(self, query: Q.MiscEquip, func: str):
        items = []
        action = getattr(self, func)
        for the_class in query.eq_classes:
            for shipclass in Equipment.SHIPCLASSES:
                items.append(
                    action(
                        shipclass=shipclass,
                        equip_type=query.eq_type,
                        equipment_class=the_class,
                    )
                )
        return items

    def get_single_item_by_query(self, query: Q.MiscEquip, func: str):
        items = []
        action = getattr(self, func)
        for the_class in query.eq_classes:
            items.append(
                action(
                    equip_type=query.eq_type,
                    equipment_class=the_class,
                )
            )
        return items

    def get_engine_by_query(self, query: Q.Engine):
        return self.get_shipclass_item_by_query(query, 'get_engine')

    def get_power_by_query(self, query: Q.Power):
        return self.get_shipclass_item_by_query(query, 'get_powerplant')

    def get_shield_by_query(self, query: Q.Shield):
        return self.get_shipclass_item_by_query(query, 'get_shield')

    def get_thruster_by_query(self, query: Q.Thruster):
        return self.get_single_item_by_query(query, 'get_thruster')

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
        return ManagerHelper.extract_equips(self.engines_list)

    def get_engine_good(self):
        return ManagerHelper.extract_goods(self.engines_list)

    def get_powerplant_equip(self):
        return ManagerHelper.extract_equips(self.powerplants_list)

    def get_powerplant_good(self):
        return ManagerHelper.extract_goods(self.powerplants_list)

    def get_st_equip(self):
        return ManagerHelper.extract_equips(self.shields_list, self.npc_shields_list, self.thrusters_list)

    def get_st_good(self):
        return ManagerHelper.extract_goods(self.shields_list, self.npc_shields_list, self.thrusters_list)

    def get_select_equip(self):
        return ManagerHelper.extract_equips(self.npc_armors_list)

    def get_lootprops(self):
        return ManagerHelper.extract_lootprops(
            self.engines_list,
            self.powerplants_list,
            self.shields_list,
            self.thrusters_list
        )

    def get_demo_marketdata(self):
        return ManagerHelper.extract_marketdata(
            self.engines_list,
            self.powerplants_list,
            self.shields_list,
            self.thrusters_list
        )
