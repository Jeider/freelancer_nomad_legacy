import random

from universe import sirius as S
from story.ingame import ingame_mission
from story.math import euler_to_quat
from story import actors

from story.ingame import names as N
from story.ingame.tools import Point, Obj, Conn, NNObj, Ship, Solar, Capital
from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT

from world.npc import NPC, EqMap
from world import ship
from universe import faction

NPCSHIPS = '''

[NPCShipArch]
nickname = ms11_ku_destroyer
loadout = ku_grp_destroyer
level = d5
ship_archetype = ku_destroyer
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER

[NPCShipArch]
nickname = ms11_rh_cruiser
loadout = rh_grp_cruiser
level = d5
ship_archetype = rh_cruiser
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER

[NPCShipArch]
nickname = ms11_rh_battleship
loadout = rh_battleship_01
level = d5
ship_archetype = rh_battleship
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER

[NPCShipArch]
nickname = ms11_ku_battleship
loadout = ku_grp_battleship
level = d10
ship_archetype = ku_battleship
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER, d5

'''

class Misson11(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m11/m11.ini'
    FOLDER = 'M11'
    FILE = 'm11'
    SCRIPT_INDEX = 11
    DIRECT_SYSTEMS = [S.or_hq, S.rh_vien]
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

        boxes = 16
        vienn_solars = [f'BOX{i:02d}' for i in range(1, boxes+1)]
        for sol in vienn_solars:
            defined_points.append(
                Solar(self, S.rh_vien, sol, ru_name='Исследовательский контейнер'),
            )

        return defined_points

    def get_capital_ships(self):
        hq_rcr = {
            'npc_ship_arch': 'ms11_rh_cruiser',
            'faction': 'rh_grp',
            'labels': ['enemy', 'rh_cruiser', 'rheinland', 'hq_attack'],
            'ru_name': N.RH_CRUISER,
        }
        hq_kd = {
            'npc_ship_arch': 'ms11_ku_destroyer',
            'faction': 'or_grp',
            'labels': ['friend', 'ku_destroyer', 'ku', 'order'],
            'ru_name': N.KU_DESTROYER,
        }

        vien_rcr = {
            'npc_ship_arch': 'ms11_rh_cruiser',
            'faction': 'rh_grp',
            'labels': ['enemy', 'rh_cruiser', 'rheinland', 'vienna_defend'],
            'ru_name': N.RH_CRUISER,
        }

        vien_rbs = {
            'npc_ship_arch': 'ms11_rh_battleship',
            'faction': 'rh_grp',
            'labels': ['enemy', 'rh_battleship', 'rheinland', 'vienna_defend'],
        }
        vien_kd = {
            'npc_ship_arch': 'ms11_ku_destroyer',
            'faction': 'or_grp',
            'labels': ['friend', 'ku_destroyer', 'ku', 'order', 'vienna_assault'],
            'ru_name': N.KU_DESTROYER,
        }
        vien_kbs = {
            'npc_ship_arch': 'ms11_ku_battleship',
            'faction': 'rh_grp',
            'labels': ['enemy', 'ku_battleship', 'ku', 'order', 'vienna_assault'],
        }

        caps = []
        hq_rcrs = []
        hq_kds = []
        vien_rcrs = []
        vien_rbss = []
        vien_kds = []
        vien_kbss = []

        hq_caps = 4
        vien_rcrs_count = 3
        vien_rbs_count = 1
        vien_ku_caps = 2
        vien_kbs_count = 1

        for index in range(1, hq_caps+1):
            cap = f'hq_rcr{index}'
            the_cap = Capital(self, cap, **hq_rcr)
            caps.append(the_cap)
            hq_rcrs.append(the_cap)

        self.add_capital_group('HQ_RCR', hq_rcrs)

        for index in range(1, hq_caps+1):
            cap = f'hq_kd{index}'
            the_cap = Capital(self, cap, **hq_kd)
            caps.append(the_cap)
            hq_kds.append(the_cap)

        self.add_capital_group('HQ_KD', hq_kds)

        for index in range(1, vien_rcrs_count+1):
            cap = f'vien_rcr{index}'
            the_cap = Capital(self, cap, **vien_rcr)
            caps.append(the_cap)
            vien_rcrs.append(the_cap)

        self.add_capital_group('VIEN_RCR', vien_rcrs)

        for index in range(1, vien_rbs_count+1):
            cap = f'vien_bs{index}'
            the_cap = Capital(self, cap, ru_name='Линкор Тирпиц', **vien_rbs)
            caps.append(the_cap)
            vien_rbss.append(the_cap)

        self.add_capital_group('VIEN_RBS', vien_rbss)

        for index in range(1, vien_ku_caps+1):
            cap = f'vien_kd{index}'
            the_cap = Capital(self, cap, **vien_kd)
            caps.append(the_cap)
            vien_kds.append(the_cap)

        self.add_capital_group('VIEN_KD', vien_kds)

        for index in range(1, vien_kbs_count+1):
            cap = f'vien_kbs{index}'
            the_cap = Capital(self, cap, ru_name='Линкор Мусаси', **vien_kbs)
            caps.append(the_cap)
            vien_kbss.append(the_cap)

        self.add_capital_group('VIEN_KBS', vien_kbss)

        return caps

    def get_nn_objectives(self):
        return []

    def get_ships(self):
        return [
            # HQ
            Ship(
                self,
                'hq_ku1',
                count=4,
                affiliation=faction.OrderMain.CODE,
                system_class=S.or_hq,
                slide_x=50,
                slide_z=50,
                labels=[
                    'hq_defence',
                    'order',
                    'friend',
                ],
                npc=NPC(
                    faction=faction.KusariMain,
                    ship=ship.Dragon,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'hq_ku2',
                count=4,
                affiliation=faction.OrderMain.CODE,
                system_class=S.or_hq,
                slide_x=-50,
                slide_z=50,
                labels=[
                    'hq_defence',
                    'order',
                    'friend',
                ],
                npc=NPC(
                    faction=faction.KusariMain,
                    ship=ship.Dragon,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'hq_rh1',
                count=5,
                affiliation=faction.RheinlandMain.CODE,
                system_class=S.or_hq,
                slide_z=50,
                labels=[
                    'hq_attack',
                    'rheinland',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'hq_rh2',
                count=5,
                affiliation=faction.RheinlandMain.CODE,
                system_class=S.or_hq,
                slide_z=50,
                labels=[
                    'hq_attack',
                    'rheinland',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),
            # VIEN
            Ship(
                self,
                'vien_kf1',
                count=3,
                affiliation=faction.OrderMain.CODE,
                system_class=S.rh_vien,
                slide_x=50,
                slide_z=50,
                labels=[
                    'vien_assault',
                    'order',
                    'friend',
                ],
                npc=NPC(
                    faction=faction.KusariMain,
                    ship=ship.Dragon,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'vien_kf2',
                count=3,
                affiliation=faction.OrderMain.CODE,
                system_class=S.rh_vien,
                slide_x=50,
                slide_z=50,
                labels=[
                    'vien_assault',
                    'order',
                    'friend',
                ],
                npc=NPC(
                    faction=faction.KusariMain,
                    ship=ship.Dragon,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'vien_rf1',
                count=4,
                affiliation=faction.RheinlandMain.CODE,
                system_class=S.rh_vien,
                slide_z=50,
                labels=[
                    'vien_defence',
                    'rheinland',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'vien_rf2',
                count=4,
                affiliation=faction.RheinlandMain.CODE,
                system_class=S.rh_vien,
                slide_z=50,
                labels=[
                    'vien_defence',
                    'rheinland',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),
        ]
