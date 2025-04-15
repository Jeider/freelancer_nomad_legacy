import random

from universe import sirius as S
from universe.systems import ku_tgk, sig42
from story.ingame import ingame_mission
from story.math import euler_to_quat
from story import actors

from story.ingame import names as N
from story.ingame import objectives as O
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

BDR_NAMES = [
    'Коссак',
    'Сарацин',
    'Мохок',
    'Маори',
    'Нубиен',
    'Викинг',
    'Монтроз',
    'Маккей',
    'Хэвок',
    'Онслоу',
    'Джервис',
]


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
                Solar(self, S.sig42, sol, ru_name='Объект'),
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
            the_cap = Capital(cap, ru_name=N.BR_DESTROYER, **bdr_torpedo)
            caps.append(the_cap)
            torp_caps.append(the_cap)

        self.add_capital_group('BDR_TORP', torp_caps)

        return caps

    def get_real_objects(self):
        return {
            'ku_tgk_tlr_1': Conn(self, ku_tgk.TekagiFreeportConn2, ku_tgk.TekagiLargeStation),
            'ku_tgk_tlr_2': Conn(self, ku_tgk.TekagiFreeportConn1, ku_tgk.TekagiFreeport),
            'to_sig42': Obj(self, ku_tgk.TekagiSiriusJumphole),
        }

    def get_nn_objectives(self):
        return [
            NNObj(self, O.LAUNCH, name='launch'),

            NNObj(self, O.TLR, target='om7_tlr_1'),
            NNObj(self, 'Сядьте на Харадзюку', target='harajuku'),

            NNObj(self, O.CHASE_ROCKFORD, name='rockford_chase1', target='rockford_chase1'),
            NNObj(self, O.CHASE_ROCKFORD, name='rockford_chase2', target='rockford_chase2'),
            NNObj(self, O.CHASE_ROCKFORD, name='rockford_chase3', target='rockford_chase3'),
            NNObj(self, O.CHASE_ROCKFORD, name='rockford_chase4', target='rockford_chase4'),
        ]

    def get_ships(self):
        return [
            Ship(
                self,
                'kim',
                jumper=True,
                hero=True,
                actor=actors.Kim,
                labels=[
                    'friend',
                    'order',
                ],
                npc=NPC(
                    faction=faction.OrderMain,
                    ship=ship.Dragon,
                    level=NPC.D10,
                    equip_map=EqMap(base_level=6),
                )
            ),
            Ship(
                self,
                'kim',
                jumper=True,
                hero=True,
                actor=actors.Kim,
                labels=[
                    'friend',
                    'order',
                ],
                npc=NPC(
                    faction=faction.OrderMain,
                    ship=ship.Dragon,
                    level=NPC.D10,
                    equip_map=EqMap(base_level=6),
                )
            ),
        ]
