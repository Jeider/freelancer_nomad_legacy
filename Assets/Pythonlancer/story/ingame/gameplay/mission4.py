import random

from universe import sirius as S
from universe.systems import rh_mnh, rh_biz, sig8, li_for
from story.ingame import ingame_mission
from story.math import euler_to_quat
from story import actors

from story.ingame.tools import Point, Obj, Conn, NNObj, Ship, Solar
from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT

from world.npc import NPC, EqMap
from world import ship
from universe import faction

NPCSHIPS = '''

[NPCShipArch]
nickname = ms4_rh_battleship_ship
loadout = rh_battleship_01
level = d10
ship_archetype = rh_battleship_ms4
pilot = cruiser_default_lowgun
state_graph = CRUISER
npc_class = lawful, CRUISER

[NPCShipArch]
nickname = ms4_rh_cruiser_ship
loadout = rh_grp_cruiser
level = d10
ship_archetype = rh_cruiser
pilot = cruiser_default_lowgun
state_graph = CRUISER
npc_class = lawful, CRUISER

[NPCShipArch]
nickname = ms4_rh_gunboat_ship
loadout = rh_grp_gunboat_no_torpedoes
level = d10
ship_archetype = rh_gunboat
pilot = cruiser_default_lowgun
state_graph = CRUISER
npc_class = lawful, CRUISER, d22
'''



class Misson03(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m04/m04.ini'
    FOLDER = 'M04'
    FILE = 'm04'
    STATIC_NPCSHIPS = NPCSHIPS

    def get_real_objects(self):
        return {
            'vendor_planet': Obj(self, rh_mnh.MunchDockring),
            'mnh_tlr_1': Conn(self, rh_mnh.MunchCivRuinsConn1, rh_mnh.MunchDockring),
            'mnh_tlr_2': Conn(self, rh_mnh.MunchCivRuinsConn2, rh_mnh.MunchCivilianStationRuins),
            'mnh_to_biz': Obj(self, rh_mnh.MunchBizmarkJumpgate),




        }