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

'''

class Misson11(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m11/m11.ini'
    FOLDER = 'M11'
    FILE = 'm11'
    SCRIPT_INDEX = 9
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
        # sig42_solars = [
        #     'com_sat',
        #     'com_sat_shield',
        #     'check1',
        # ]
        # for sol in sig42_solars:
        #     defined_points.append(
        #         Solar(self, S.sig42, sol),
        #     )

        return defined_points

    def get_capital_ships(self):
        hq_rcr = {
            'npc_ship_arch': 'ms11_rh_cruiser',
            'faction': 'rh_grp',
            'labels': ['enemy', 'rh_cruiser', 'rheinland', 'hq_attack'],
        }
        hq_kd = {
            'npc_ship_arch': 'ms11_ku_destroyer',
            'faction': 'or_grp',
            'labels': ['friend', 'ku_destroyer', 'ku', 'order'],
        }

        vien_rcr = {
            'npc_ship_arch': 'ms11_rh_cruiser',
            'faction': 'rh_grp',
            'labels': ['enemy', 'rh_cruiser', 'rheinland', 'vienna_defend'],
        }

        caps = []
        hq_rcrs = []
        hq_kds = []
        vien_rcrs = []

        hq_caps = 4
        vien_caps = 4

        for index in range(1, hq_caps+1):
            cap = f'hq_rcr{index}'
            the_cap = Capital(cap, ids_name=1, **hq_rcr)
            caps.append(the_cap)
            hq_rcrs.append(the_cap)

        self.add_capital_group('HQ_RCR', hq_rcrs)

        for index in range(1, hq_caps+1):
            cap = f'hq_kd{index}'
            the_cap = Capital(cap, ids_name=1, **hq_kd)
            caps.append(the_cap)
            hq_kds.append(the_cap)

        self.add_capital_group('HQ_KD', hq_kds)

        for index in range(1, vien_caps+1):
            cap = f'vien_rcr{index}'
            the_cap = Capital(cap, ids_name=1, **hq_rcr)
            caps.append(the_cap)
            vien_rcrs.append(the_cap)

        self.add_capital_group('VIEN_RCR', vien_rcrs)

        return caps

    def get_nn_objectives(self):
        return []

    def get_ships(self):
        return [
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
        ]
