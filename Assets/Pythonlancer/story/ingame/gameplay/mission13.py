import random

from universe import sirius as S
from story.ingame import ingame_mission
from story.math import euler_to_quat
from story import actors

from story.ingame.tools import Point, Obj, Conn, NNObj, Ship, Solar, Capital, SaveState
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

[NPCShipArch]
nickname = ms13_li_dread
loadout = li_dreadnought_03
level = d10
ship_archetype = li_dreadnought
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER, d5

[NPCShipArch]
nickname = beast_fire_shiparch
loadout = beast_fire_ship
level = d10
ship_archetype = beast_ultra_fire_ship
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER, d5



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
            'krieg1',
            'sph02_door02',
            'sph02_door02_open',
            'sph02_to_inside',
            'inside_to_sph02',
            'sph02_door03',
            'sph02_door03_open',
            'sph02_door03_close',
        ]

        sphere_gens = [
            'sph2_core_F01',
            'sph2_core_F02',
            'sph2_core_F03',
            'sph2_core_F04',
            'sph2_core_F05',
            'sph2_core_F06',
            'sph2_core_F07',
            'sph2_core_F08',
            'sph2_core_G01',
            'sph2_core_G02',
            'sph2_core_G03',
            'sph2_core_G04',
            'sph2_core_G05',
            'sph2_core_G06',
            'sph2_core_G07',
            'sph2_core_G08',
        ]

        krieg_gens = [
            'krieg_gen1',
            'krieg_gen2',
            'krieg_gen3',
            'krieg_gen4',
            'krieg_gen5',
            'krieg_gen6',
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

        for s_gen in sphere_gens:
            defined_points.append(
                Solar(self, S.sphere2, s_gen, ru_name='Генератор',
                      archetype='sphere_generator', loadout='sphere_generator_laser'),
            )

        for kr_gen in krieg_gens:
            defined_points.append(
                Solar(self, S.sphere2, kr_gen, ru_name='Генератор',
                      archetype='beast_generator'),
            )

        for sol, ru_name in inside_solars:
            defined_points.append(
                Solar(self, S.sphere2_inside, sol, ru_name=ru_name),
            )

        defined_points.extend([
            Solar(self, S.sphere2, 'krieg_sleep', ru_name='Крыг', loadout='beast_sleep', archetype='beast_1500'),
            Solar(self, S.sphere2, 'krieg_opens', ru_name='Крыг', loadout='beast_arrive', archetype='beast_1500'),
            Solar(self, S.sphere2, 'krieg_opens_force', ru_name='Крыг',
                  loadout='beast_force_open', archetype='beast_1500',
                  pilot='pilot_solar_hardest', labels=['the_krieg']),
            Solar(self, S.sphere2, 'hit_fx', ru_name='Удар!', loadout='beast_hit', archetype='hidden_connect',
                  labels=['the_krieg']),
        ])



        return defined_points

    def get_capital_ships(self):
        li_dread = {
            'npc_ship_arch': 'ms13_li_dread',
            'faction': 'asf_grp',
            'labels': ['friend', 'asf_a', 'asf'],
        }
        beast_fire = {
            'npc_ship_arch': 'beast_fire_shiparch',
        }

        caps = [
            Capital(self, 'li_dread', ru_name='Линкор Миссури', **li_dread),
            Capital(self, 'krieg_fire', ru_name='Выстрел', radius=0, **beast_fire),
        ]

        return caps

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
