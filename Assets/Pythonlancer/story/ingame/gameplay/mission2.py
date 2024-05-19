import random

from universe import sirius as S
from universe.systems import rh_biz, om15
from story.ingame import ingame_mission
from story.math import euler_to_quat
from story import actors

from story.ingame.tools import Point, Obj, Conn, NNObj, Ship
from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT

from world.npc import NPC, EqMap
from world import ship
from universe import faction

from text.dividers import SINGLE_DIVIDER

REAL_AST_REWARD_NAME_FORMAT = 'om15_field_miner6_reward_field_asteroid_{index}'
ALT_AST_REWARD_NAME_FORMAT = 'om15_demo_alt_ast_reward_{index}'
REAL_REWARD_ASTEROIDS_COUNT = 16
LOW_REAL_AST_ARCHETYPE = 'om15_mineast_super_lowdamage'
VALID_AST_LOADOUT = 'm2_low_real_om15_xast_ultra'
INVALID_AST_LOADOUT = 'm2_low_real_om15_xast_empty'


class Om15DemoAstField(object):
    POSITIONS = [
        (17066, -200, 13143),
        (17113, -200, 14405),
        (17239, -200, 15752),
        (17048, -200, 16885),
        (18227, -200, 13334),
        (18432, -200, 14341),
        (18269, -200, 15634),
        (18470, -200, 16782),
        (19672, -200, 13110),
        (19521, -200, 14455),
        (19544, -200, 15460),
        (19604, -200, 16735),
        (20897, -200, 13324),
        (20962, -200, 14322),
        (20697, -200, 15688),
        (20654, -200, 16971),
    ]

    SOLAR_TEMPLATE = '''[MsnSolar]
nickname = {nickname}
string_id = 1
faction = fc_uk_grp
system = om15
position = {pos}
orientation = {orient}
archetype = {archetype}
loadout = {loadout}
label = ast_bg_demo
radius = 0
'''

    def get_msn_solars(self):
        ast_count = len(self.POSITIONS)
        valid_index = random.randint(1, ast_count)
        space_content = []

        for index, pos in enumerate(self.POSITIONS, start=1):
            rotate = (
                random.randint(0, 360),
                random.randint(0, 360),
                random.randint(0, 360)
            )
            space_content.append(
                self.SOLAR_TEMPLATE.format(
                    nickname=ALT_AST_REWARD_NAME_FORMAT.format(index=index),
                    pos='{0}, {1}, {2}'.format(*pos),
                    orient='{0:.2f}, {1:.2f}, {2:.2f}, {3:.2f}'.format(*euler_to_quat(*rotate)),
                    archetype=LOW_REAL_AST_ARCHETYPE,
                    loadout=VALID_AST_LOADOUT if index == valid_index else INVALID_AST_LOADOUT,
                )
            )
        return SINGLE_DIVIDER.join(space_content)

    def get_new_ast_names(self):
        names = []
        for i in range(1, len(self.POSITIONS)+1):
            names.append(ALT_AST_REWARD_NAME_FORMAT.format(index=i))
        return names

    def get_old_ast_names(self):
        names = []
        for i in range(1, REAL_REWARD_ASTEROIDS_COUNT+1):
            names.append(REAL_AST_REWARD_NAME_FORMAT.format(index=i))
        return names

    def spawn_new_ast(self):
        actions = []
        for name in self.get_new_ast_names():
            actions.append(f'Act_SpawnSolar = {name}')
        return SINGLE_DIVIDER.join(actions)

    def remove_new_ast(self):
        actions = []
        for name in self.get_new_ast_names():
            actions.append(f'Act_Destroy = {name}, SILENT')
        return SINGLE_DIVIDER.join(actions)

    def remove_originals(self):
        actions = []
        for name in self.get_old_ast_names():
            actions.append(f'Act_Destroy = {name}, SILENT')
        return SINGLE_DIVIDER.join(actions)


class Misson02(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m02/m02.ini'
    FOLDER = 'M02'
    FILE = 'm02'

    def get_ingame_thorns(self):
        return [
            IngameThorn(
                self,
                system_class=S.rh_biz,
                template=GENERIC_TWO_POINT,
                name='m02_battleship_launch',
                points={
                    'camera': 'm2_cam1',
                    'marker': 'm2_cam_marker1',
                },
                duration=6,
            ),

            IngameThorn(
                self,
                system_class=S.om15,
                template=GENERIC_TWO_POINT,
                name='m02_demo_ast01',
                points={
                    'camera': 'ast_cam1',
                    'marker': 'demo_ast1',
                },
                duration=200,
            ),

            IngameThorn(
                self,
                system_class=S.om15,
                template=GENERIC_TWO_POINT,
                name='m02_demo_ast02',
                points={
                    'camera': 'ast_cam2',
                    'marker': 'demo_ast2',
                },
                duration=200,
            ),
        ]

    def get_real_objects(self):
        return {
            'biz_tlr_1': Conn(self, rh_biz.BizmarkConnBattleship1, rh_biz.BizmarkBattleship),
            'biz_tlr_2': Conn(self, rh_biz.BizmarkConnBattleship1, rh_biz.BizmarkOmega15Jumpgate),
            'biz_to_om15': Obj(self, rh_biz.BizmarkOmega15Jumpgate),

            'om15_tlr_1': Conn(self, om15.Om15PoliceConn1, om15.Om15BizmarkJumpgate),
            'om15_tlr_2': Conn(self, om15.Om15PoliceConn1, om15.Om15Outpost),

            'om15_virtual_depot': Obj(self, om15.Om15VirtualDepot),
            'om15_jacobo_miner': Obj(self, om15.Om15RoidMiner6),

            'om15_to_biz': Obj(self, rh_biz.BizmarkOmega15Jumpgate),
            'battleship': Obj(self, rh_biz.BizmarkBattleship),
        }

    def get_static_points(self):
        return [
            Point(self, S.rh_biz, 'wilham_init'),

            Point(self, S.om15, 'demo_ast1'),
            Point(self, S.om15, 'demo_ast2'),

            Point(self, S.om15, 'jacobo_init'),
            Point(self, S.om15, 'jacobo_scan_save'),
            Point(self, S.om15, 'player_scan_save'),

            Point(self, S.om15, 'waypoint1'),
            Point(self, S.om15, 'waypoint2'),

            Point(self, S.om15, 'ship1'),
            Point(self, S.om15, 'ship2'),
            Point(self, S.om15, 'shipa1'),
            Point(self, S.om15, 'shipa2'),
            Point(self, S.om15, 'shipa3'),

            Point(self, S.om15, 'depot_waypoint1'),
            Point(self, S.om15, 'base1'),

            Point(self, S.om15, 'punisher_init'),
            Point(self, S.om15, 'wilham_back_init'),
            Point(self, S.om15, 'player_back_save'),

            Point(self, S.om15, 'shipd1'),
            Point(self, S.om15, 'shipd2'),

            Point(self, S.om15, 'shipdf1a'),
            Point(self, S.om15, 'shipdf1b'),
            Point(self, S.om15, 'shipdf1c'),

            Point(self, S.om15, 'shipdf2a'),
            Point(self, S.om15, 'shipdf2b'),
            Point(self, S.om15, 'shipdf2c'),

            Point(self, S.om15, 'base1'),
            Point(self, S.om15, 'platform1'),
            Point(self, S.om15, 'platform2'),

            Point(self, S.om15, 'shipbfr1'),
            Point(self, S.om15, 'shipb1'),
            Point(self, S.om15, 'shipb1'),
            Point(self, S.om15, 'shipb2'),
            Point(self, S.om15, 'shipb3'),
            Point(self, S.om15, 'shipb4'),
            Point(self, S.om15, 'shipb5'),
            Point(self, S.om15, 'shipb6'),

            Point(self, S.om15, 'player_base_save'),
            Point(self, S.om15, 'wilham_base'),
            Point(self, S.om15, 'punishers_base'),
            Point(self, S.om15, 'catching'),
        ]

    def get_ships(self):
        return [
            Ship(
                self,
                'jacobo',
                npc=NPC(
                    faction=faction.Outcasts,
                    ship=ship.Stiletto,
                    level=NPC.D2,
                    equip_map=EqMap(base_level=2),
                )
            ),
            Ship(
                self,
                'wilham',
                jumper=True,
                actor=actors.Wilham,
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D2,
                    equip_map=EqMap(base_level=2),
                )
            ),
            Ship(
                self,
                'punisher',
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D2,
                    equip_map=EqMap(base_level=2),
                )
            ),
            Ship(
                self,
                'junker_fighter',
                count=5,
                affiliation=faction.Junkers.CODE,
                npc=NPC(
                    faction=faction.Junkers,
                    ship=ship.Dagger,
                    level=NPC.D2,
                    equip_map=EqMap(base_level=2),
                )
            ),
            Ship(
                self,
                'junker_elite',
                count=5,
                affiliation=faction.Junkers.CODE,
                npc=NPC(
                    faction=faction.Junkers,
                    ship=ship.Dagger,
                    level=NPC.D1,
                    equip_map=EqMap(base_level=1),
                )
            ),
            Ship(
                self,
                'junker_csv',
                affiliation=faction.Junkers.CODE,
                npc=NPC(
                    faction=faction.Junkers,
                    ship=ship.CSV,
                    level=NPC.D1,
                    equip_map=EqMap(base_level=1),
                )
            ),
            Ship(
                self,
                'depot_fighter',
                count=10,
                affiliation=faction.Corsairs.CODE,
                npc=NPC(
                    faction=faction.Corsairs,
                    ship=ship.Bloodhound,
                    level=NPC.D1,
                    equip_map=EqMap(base_level=1),
                )
            ),
            Ship(
                self,
                'base_fighter',
                count=10,
                affiliation=faction.Corsairs.CODE,
                npc=NPC(
                    faction=faction.Corsairs,
                    ship=ship.Bloodhound,
                    level=NPC.D1,
                    equip_map=EqMap(base_level=1),
                )
            ),
            Ship(
                self,
                'base_fighter_improved',
                count=5,
                affiliation=faction.Corsairs.CODE,
                npc=NPC(
                    faction=faction.Corsairs,
                    ship=ship.Bloodhound,
                    level=NPC.D2,
                    equip_map=EqMap(base_level=2),
                )
            ),
        ]

    '''


[NPC]
nickname = npc_co_fighter
affiliation = co_grp
npc_ship_arch = co_fighter_m2

[NPC]
nickname = npc_co_freighter
affiliation = co_grp
npc_ship_arch = co_freighter_m2

[NPC]
nickname = npc_co_fighter_improved
affiliation = co_grp
npc_ship_arch = co_fighter_m2_improved


[MsnShip]
nickname = depot_freighter1
NPC = npc_co_freighter
label = corsairs
label = depot_freighters
random_name = true
    '''
    def get_initial_context(self) -> dict:
        context = super().get_initial_context()
        context['demo_astfield'] = Om15DemoAstField()
        return context

    def get_nn_objectives(self):
        return [
            NNObj(self, 92003, name='meet_vendor', target='battleship'),

            NNObj(self, 92023, name='launch'),

            NNObj(self, 92005, target='biz_tlr_1'),
            NNObj(self, 92006, target='biz_to_om15'),
            NNObj(self, 92007, target='om15_tlr_1'),
            NNObj(self, 92008, target='om15_jacobo_miner'),
            NNObj(self, 92010, name='scan_wp1', target='waypoint1'),
            NNObj(self, 92010, name='scan_wp2', target='waypoint2'),

            NNObj(self, 92011, name='scan_objects'),
            NNObj(self, 92012, name='destroy_junkers'),
            NNObj(self, 92009, name='drop_objects'),
            NNObj(self, 92013, name='get_objects'),

            NNObj(self, 92013, target='om15_tlr_2'),

            NNObj(self, 92024, name='wait_for_transfer_data'),
            NNObj(self, 92015, name='find_corsair_depot', target='depot_waypoint1'),
            NNObj(self, 92016, name='find_corsair_base', target='base1'),

            NNObj(self, 92017, name='destroy_platforms'),
            NNObj(self, 92018, name='destroy_corsairs'),

            NNObj(self, 92019, name='om15_to_biz_fly', target='om15_to_biz', towards=True),
            NNObj(self, 92019, target='om15_to_biz'),
            NNObj(self, 92005, target='biz_tlr_2'),
            NNObj(self, 92022, target='battleship'),
        ]



'''
[NPCShipArch]
nickname = ms2_wilham
loadout = ms2_wilham_01
level = d10
ship_archetype = rh_elite
pilot = mod_fighter_version_a
state_graph = FIGHTER
npc_class = lawful, FIGHTER

[NPCShipArch]
nickname = ms2_junker_fighter
loadout = ms2_junker_fighter
level = d5
ship_archetype = bw_fighter
pilot = mod_fighter_version_a
state_graph = FIGHTER
npc_class = unlawful, FIGHTER

[NPCShipArch]
nickname = ms2_junker_elite
loadout = ms2_junker_elite
level = d5
ship_archetype = bw_elite
pilot = mod_fighter_version_a_lowgun
state_graph = FIGHTER
npc_class = unlawful, FIGHTER

[NPCShipArch]
nickname = ms2_csv
loadout = ms2_csv_01
level = d5
ship_archetype = ge_csv
pilot = mod_fighter_version_a
state_graph = FIGHTER
npc_class = unlawful, FIGHTER

[NPCShipArch]
nickname = ms2_csv_cinema
loadout = ms2_csv_01_cinema
level = d5
ship_archetype = ge_csv
pilot = mod_fighter_version_a
state_graph = FIGHTER
npc_class = unlawful, FIGHTER



;PUNISHERS
[NPCShipArch]
nickname = ms2_punisher_a
loadout = ms2_punisher_01
level = d10
ship_archetype = rh_elite
pilot = mod_fighter_version_a_lowgun
state_graph = FIGHTER
npc_class = lawful, FIGHTER

[NPCShipArch]
nickname = ms2_punisher_b
loadout = ms2_punisher_02
level = d10
ship_archetype = rh_elite
pilot = mod_fighter_version_a_lowgun
state_graph = FIGHTER
npc_class = lawful, FIGHTER


;v2 arch


[NPCShipArch]
nickname = ms2_jacobo
loadout = ms2_jacobo_01
level = d3
ship_archetype = bw_elite
pilot = mod_fighter_version_a
state_graph = FIGHTER
npc_class = lawful, FIGHTER

[NPCShipArch]
nickname = ms2_suprise_ship
loadout = ms2_top_secret
level = d1
ship_archetype = suprise_rh_elite_ms2
pilot = pilot_null
state_graph = FIGHTER
npc_class = lawful, FIGHTER

[NPCShipArch]
nickname = ms2_suprise_ship_freighter
level = d1
ship_archetype = rh_freighter
pilot = pilot_null
state_graph = FIGHTER
npc_class = lawful, FIGHTER





;CORSAIRS
[NPCShipArch]
nickname = co_fighter_m2
loadout = lod_m2_co_fighter
level = d3
ship_archetype = pi_fighter
pilot = mod_fighter_version_a
state_graph = FIGHTER
npc_class = unlawful, FIGHTER, m2_reinforce

[NPCShipArch]
nickname = co_fighter_m2_improved
loadout = lod_m2_co_fighter_improved
level = d4
ship_archetype = pi_fighter
pilot = mod_fighter_version_a
state_graph = FIGHTER
npc_class = unlawful, FIGHTER, m2_reinforce

[NPCShipArch]
nickname = co_freighter_m2
loadout = lod_ms2_co_freighter
level = d4
ship_archetype = pi_freighter
pilot = mod_fighter_version_a
state_graph = FIGHTER
npc_class = unlawful, FREIGHTER
'''