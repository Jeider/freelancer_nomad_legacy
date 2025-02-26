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

'''

class Misson10(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m10/m10.ini'
    FOLDER = 'M10'
    FILE = 'm10'
    SCRIPT_INDEX = 10
    DIRECT_SYSTEMS = [S.xen]
    STATIC_NPCSHIPS = NPCSHIPS

    def get_static_points(self):
        defined_points = []

        # SIRIUS
        #
        # sig42_points = [
        #
        # ]
        # for p in sig42_points:
        #     defined_points.append(
        #         Point(self, S.sig42, p)
        #     )
        #

        return defined_points

    def get_nn_objectives(self):
        return []

    def get_ships(self):
        return [
            # HQ
            Ship(
                self,
                'patroller',
                count=20,
                affiliation=faction.OrderMain.CODE,
                system_class=S.or_hq,
                labels=[
                    'patroller',
                    'xenos',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.BretoniaPirate,  # xenos in future
                    ship=ship.Stiletto,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),
        ]
