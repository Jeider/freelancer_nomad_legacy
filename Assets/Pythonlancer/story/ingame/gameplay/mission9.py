import random

from universe import sirius as S
from story.ingame import ingame_mission
from story.math import euler_to_quat
from story import actors

from story.ingame.tools import Point, Obj, Conn, NNObj, Ship, Solar, Capital
from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT

from world.npc import NPC, EqMap
from world import ship
from universe import faction

NPCSHIPS = '''

[NPCShipArch]
nickname = ms9_br_destroyer_torpedo
loadout = m09_br_torp_destroyer
level = d10
ship_archetype = br_destroyer
pilot = cruiser_antisolar
state_graph = CRUISER
npc_class = lawful, CRUISER, d5

'''

class Misson09(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m09/m09.ini'
    FOLDER = 'M09'
    FILE = 'm09'
    SCRIPT_INDEX = 9
    DIRECT_SYSTEMS = [S.sig42]
    STATIC_NPCSHIPS = NPCSHIPS

    def get_static_points(self):
        defined_points = []

        # SIRIUS

        sig42_points = [

        ]
        for p in sig42_points:
            defined_points.append(
                Point(self, S.sig42, p)
            )

        sig42_solars = [
            'com_sat',
            'com_sat_shield',
            'check1',
        ]
        for sol in sig42_solars:
            defined_points.append(
                Solar(self, S.sig42, sol),
            )

        return defined_points

    def get_capital_ships(self):
        bdr_torpedo = {
            'npc_ship_arch': 'ms9_br_destroyer_torpedo',
            'faction': 'asf_grp',
            'labels': ['enemy', 'br_destroyer', 'torpedo_attack'],
        }

        caps = []
        torp_caps = []

        torp_caps_len = 12

        for index in range(1, torp_caps_len+1):
            cap = f'bdr{index:02d}'
            the_cap = Capital(cap, ids_name=1, **bdr_torpedo)
            caps.append(the_cap)
            torp_caps.append(the_cap)

        self.add_capital_group('BDR_TORP', torp_caps)

        return caps

    def get_nn_objectives(self):
        return []

    def get_ships(self):
        return []
