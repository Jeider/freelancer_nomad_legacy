from managers.tools.helpers import ManagerHelper
from managers.tools import query as Q

from world.equipment import Equipment, MainMiscEquip
from world.power import Power
from world.engine import Engine
from world.shield import Shield, ShieldNPC
from world.thruster import Thruster
from world.armor import ArmorNPC
from world import ship


class NPCArmorManager:

    def __init__(self, lancer_core):
        self.core = lancer_core

        self.ship_types = [
            ship.BaseInterceptorShip,
            ship.BaseFighterShip,
            ship.BaseFreighterShip,
        ]

        self.npc_armors_db = {}
        self.npc_armors_list = []

        self.load_game_data()

    def load_game_data(self):
        for ship_type in self.ship_types:
            self.npc_armors_db[ship_type.SHIP_TYPE] = {}
            for base_item_class, base_item_armor in ship_type.HIT_PTS_PER_CLASS.items():
                self.npc_armors_db[ship_type.SHIP_TYPE][base_item_class] = {}
                for scaled_item_class, scaled_item_armor in ship_type.HIT_PTS_PER_CLASS.items():
                    armor_scale = ((scaled_item_armor * 100) / base_item_armor) / 100
                    npc_armor = ArmorNPC(ship_type.SHIP_TYPE, base_item_class, scaled_item_class, armor_scale)
                    self.npc_armors_db[ship_type.SHIP_TYPE][base_item_class][scaled_item_class] = npc_armor
                    self.npc_armors_list.append(npc_armor)

    def get_npc_armor(self, ship, armor_index):
        return self.npc_armors_db[ship.SHIP_TYPE][ship.SHIP_CLASS][armor_index]

    def get_select_equip(self):
        return ManagerHelper.extract_equips(self.npc_armors_list)
