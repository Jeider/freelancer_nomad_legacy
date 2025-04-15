import random

from universe import sirius as S
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
nickname = ms13_no_fighter
loadout = ms6_no_fighter
level = d13
ship_archetype = no_fighter
pilot = mod_fighter_version_a
state_graph = FIGHTER
npc_class = lawful, FIGHTER

'''


class Misson13(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m13/m13.ini'
    FOLDER = 'M13'
    FILE = 'm13'
    SCRIPT_INDEX = 13
    DIRECT_SYSTEMS = [S.sphere2, S.sphere2_inside, S.beast01]
    STATIC_NPCSHIPS = NPCSHIPS

    def get_static_points(self):
        sphere_points = [
            # 'base1',
            # 'gen1',
            # 'gen2',
        ]

        sphere_solars = [
            'gen1',
            'gen2',
            'gen3',
            'lazer1',
            'core1',
            'core2',
            'core3',
            'core4',
            'core5',
            'core6',
            'arm1',
            'arm2',
            'arm3',
            'arm4',
            'arm5',
            'arm6',
            'arm7',
            'arm8',
            'core_fx',
            'krieg1',
            'sph02_door02',
            'sph02_door02_open',
            'sph02_to_inside',
            'inside_to_sph02',
            'sph02_door03',
            'sph02_door03_open',
            'sph02_door03_close',
        ]

        inside_solars = [
            ('sph02_ins_airlock_exit', 'выход'),
        ]

        defined_points = []
        for p in sphere_points:
            defined_points.append(
                Point(self, S.sphere2, p)
            )

        for sol in sphere_solars:
            defined_points.append(
                Solar(self, S.sphere2, sol, ru_name='test'),
            )

        for sol, ru_name in inside_solars:
            defined_points.append(
                Solar(self, S.sphere2_inside, sol, ru_name=ru_name),
            )

        return defined_points

    def get_ships(self):
        return [
            Ship(
                self,
                'no_chamber',
                count=10,
                affiliation=faction.OrderMain.CODE,
                system_class=S.beast01,
                slide_z=50,
                radius=0,
                labels=[
                    'enemy',
                ],
                static_npc_shiparch='ms13_no_fighter'
            )
        ]
