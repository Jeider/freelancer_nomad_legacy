import random

from universe import sirius as S
from universe.systems import rh_biz, om15
from story.ingame import ingame_mission
from story.math import euler_to_quat
from story import actors

from story.ingame import objectives as O
from story.ingame.tools import (Point, Obj, Conn, NNObj, Ship, TextDialog, MultiText, MultiLine,
                                DIALOG_YES_NO, SaveState)
from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT

from world.npc import NPC, EqMap
from world import ship
from universe import faction

from text.dividers import SINGLE_DIVIDER
from text.strings import MultiString as MS

REAL_AST_REWARD_NAME_FORMAT = 'om15_field_miner6_reward_field_asteroid_{index}'
ALT_AST_REWARD_NAME_FORMAT = 'om15_demo_alt_ast_reward_{index}'
REAL_REWARD_ASTEROIDS_COUNT = 16
LOW_REAL_AST_ARCHETYPE = 'om15_mineast_super_lowdamage'
LOW_REAL_AST_ARCHETYPE_ULTRA = 'om15_mineast_super_lowdamage_ultra'
VALID_AST_LOADOUT = 'm2_low_real_om15_xast_ultra'
INVALID_AST_LOADOUT = 'm2_low_real_om15_xast_empty'

NPCSHIPS = '''
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
nickname = ms2_csv_cinema
loadout = ms2_csv_01_cinema
level = d5
ship_archetype = ge_csv
pilot = mod_fighter_version_a
state_graph = FIGHTER
npc_class = unlawful, FIGHTER

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

'''


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
        valid_indexes = [3, 8, 14]
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
                    archetype=LOW_REAL_AST_ARCHETYPE_ULTRA if index in valid_indexes else LOW_REAL_AST_ARCHETYPE,
                    loadout=VALID_AST_LOADOUT if index in valid_indexes else INVALID_AST_LOADOUT,
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
    START_SAVE_ID = 32200
    START_SAVE_RU_NAME = MS('Бисмарк. Линкор Шарнхорст', 'Bismarck, Battleship Scharnhorst')
    STATIC_NPCSHIPS = NPCSHIPS
    SCRIPT_INDEX = 2
    INIT_OFFER = MultiLine(
        ru_lines=[
            'ЗАДАЧА:',
            'Найти разрушенный корабль, добыть полезную информацию из него и доставить Вильгельму.',
            '',
            'СЛОЖНОСТЬ:',
            'Низкая.',
            '',
            'Награда:',
            '5 000 кредитов.',
        ],
        en_lines=[
            'OBJECTIVE:',
            'Find ship wreck, extract important information from this ship and give it back to Wilhelm.',
            '',
            'DIFFICULTY:',
            'Low.',
            '',
            'REWARD:',
            '5 000 credits.',
        ]
    ).get_content()

    def get_dialogs(self):
        return [
            TextDialog(
                self, 'vendor', 'Вильгельм',
                ru_content=MultiText([
                    'Доброго времени суток, герр Трент, меня зовут Вильгельм и я представляю вооруженные силы Рейнланда. '
                    'Нас впечатлили ваши достижения на территории Рейнланда за столь короткий срок, и мы хотели бы '
                    'предложить вам работу по вашему профилю. Хочу сразу предупредить, что работа сопряжена с некоторой '
                    'степенью секретности. Если вас заинтересовало предложение - мы могли бы лично встретиться '
                    'на линкоре Шарнхорст в системе Бисмарк',
                ],
                [
                    'Greetings, herr Trent, My name is Wilhelm and I am an officer of Rheinland military force. '
                    'We are impressed by your achievements in the Rhineland in such a short period of time and '
                    'would like to offer you a position in your field.',
                    'I would like to warn you right away that this work involves a certain degree of secrecy. ',
                    'If you are interested in the proposal, we could meet in person on the battleship '
                    'Scharnhorst in the Bismarck system.',
                ])
            ),
            TextDialog(
                self, 'mining', 'Майнинг астероидов',
                ru_content=MultiText(
                    [
                        'Чтобы получить доступ к рудокопу, вы должны добыть ключ в одном из астероидов.',

                        'Хотите запустить обучение?',
                    ],
                    [
                        'In order to get access to roid miner you must extra key from on of near asteroids.',

                        'Do you want to run tutorial?',
                    ]
                ),
                dialog_type=DIALOG_YES_NO,
            ),
        ]

    def get_save_states(self):
        return [
            SaveState(self, 'junker_battle', MS('Омега-15, Мусорщики', 'Omega-15, Junkers')),
            SaveState(self, 'meet_punishers', MS('Омега-15, Встреча с Карателями', 'Omega-15, Meeting with Punishers')),
            SaveState(self, 'base_assault', MS('Омега-15, штурм базы Корсаров', 'Omega-15, Assault on Corsairs\' base')),
        ]

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

            'om15_to_biz': Obj(self, om15.Om15BizmarkJumpgate),
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
            # Point(self, S.om15, 'shipb1'),
            # Point(self, S.om15, 'shipb1'),
            # Point(self, S.om15, 'shipb2'),
            # Point(self, S.om15, 'shipb3'),
            # Point(self, S.om15, 'shipb4'),
            # Point(self, S.om15, 'shipb5'),
            # Point(self, S.om15, 'shipb6'),

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
                labels=[
                    'outcast',
                    'friend',
                ],
                hero=True,
                actor=actors.Jacobo,
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
                hero=True,
                actor=actors.Wilham,
                labels=[
                    'rheinland',
                    'friend',
                ],
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
                count=5,
                labels=[
                    'punisher',
                    'punishers',
                    'rheinland',
                ],
                unique_npc_entry=True,
                base_name=MS('Каратель', 'Punisher'),
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
                labels=['junker'],
                relative_pos=True,
                relative_range=1000,
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
                count=3,
                affiliation=faction.Junkers.CODE,
                labels=['junker'],
                relative_pos=True,
                relative_range=1500,
                npc=NPC(
                    faction=faction.Junkers,
                    ship=ship.Stiletto,
                    level=NPC.D2,
                    equip_map=EqMap(base_level=2),
                )
            ),
            Ship(
                self,
                'junker_csv',
                affiliation=faction.Junkers.CODE,
                labels=['junker'],
                count=2,
                relative_pos=True,
                relative_range=1600,
                npc=NPC(
                    faction=faction.Junkers,
                    ship=ship.CSV,
                    level=NPC.D2,
                    equip_map=EqMap(base_level=2),
                )
            ),
            Ship(
                self,
                'depot_fighter',
                count=6,
                affiliation=faction.Corsairs.CODE,
                system_class=S.om15,
                labels=[
                    'depot_fighters',
                    'corsairs',
                    'ships',
                ],
                npc=NPC(
                    faction=faction.Corsairs,
                    ship=ship.Bloodhound,
                    level=NPC.D3,
                    equip_map=EqMap(base_level=2),
                )
            ),
            Ship(
                self,
                'depot_freighter',
                count=2,
                affiliation=faction.Corsairs.CODE,
                labels=[
                    'depot_freighters',
                    'corsairs',
                    'ships',
                ],
                npc=NPC(
                    faction=faction.Corsairs,
                    ship=ship.Mule,
                    level=NPC.D2,
                    equip_map=EqMap(base_level=1),
                )
            ),
            Ship(
                self,
                'base_fighter',
                count=6,
                affiliation=faction.Corsairs.CODE,
                system_class=S.om15,
                labels=[
                    'base_fighters',
                    'corsairs',
                    'ships',
                ],
                npc=NPC(
                    faction=faction.Corsairs,
                    ship=ship.Bloodhound,
                    level=NPC.D2,
                    equip_map=EqMap(base_level=2),
                )
            ),
            Ship(
                self,
                'base_reinforcement',
                count=3,
                relative_pos=True,
                relative_range=2000,
                affiliation=faction.Corsairs.CODE,
                labels=[
                    'base_fighters',
                    'corsairs',
                    'ships',
                ],
                npc=NPC(
                    faction=faction.Corsairs,
                    ship=ship.Bloodhound,
                    level=NPC.D3,
                    equip_map=EqMap(base_level=2),
                )
            ),
            Ship(
                self,
                'base_reinforcement_second',
                count=3,
                relative_pos=True,
                relative_range=2000,
                affiliation=faction.Corsairs.CODE,
                labels=[
                    'base_fighters',
                    'corsairs',
                    'ships',
                ],
                npc=NPC(
                    faction=faction.Corsairs,
                    ship=ship.Bloodhound,
                    level=NPC.D3,
                    equip_map=EqMap(base_level=2),
                )
            ),
        ]

    def get_initial_context(self) -> dict:
        context = super().get_initial_context()
        context['demo_astfield'] = Om15DemoAstField()
        return context

    def get_nn_objectives(self):
        return [
            NNObj(self, MS('Найдитель Вильгельма в баре линкора Шарнхорст',
                           'Find Wilhelm in bar at Battleship Scharnhorst'), name='meet_vendor', target='battleship'),

            NNObj(self, O.LAUNCH, name='launch'),

            NNObj(self, O.TLR, target='biz_tlr_1'),
            NNObj(self, O.JUMPGATE, target='biz_to_om15'),
            NNObj(self, O.TLR, target='om15_tlr_1'),
            NNObj(self, MS('Получите доступ и сядьте на добывающее судно Матильда',
                           'Get access and dock with roid miner Matilda'), target='om15_jacobo_miner'),
            NNObj(self, O.GOTO, name='scan_wp1', target='waypoint1'),
            NNObj(self, O.GOTO, name='scan_wp2', target='waypoint2'),

            NNObj(self, MS('Просканируйте объекты', 'Scan marked objects'), name='scan_objects'),
            NNObj(self, MS('Уничтожьте мусорщиков', 'Destroy junkers'), name='destroy_junkers'),
            NNObj(self, MS('Выбейте чёрный ящик', 'Exract the black box by your guns'), name='drop_objects'),
            NNObj(self, MS('Подберите черный ящик', 'Tractor the black box'), name='get_objects'),

            NNObj(self, O.TLR, target='om15_tlr_2'),

            NNObj(self, MS('Ожидайте обработки информации из чёрного ящика',
                           'Wait for processing data from the black box'), name='wait_for_transfer_data'),
            NNObj(self, O.GOTO, name='find_corsair_depot', target='depot_waypoint1'),
            NNObj(self, O.GOTO, name='find_corsair_base', target='base1'),

            NNObj(self, O.DESTROY_WP, name='destroy_platforms'),
            NNObj(self, O.DESTROY_CORSAIRS, name='destroy_corsairs'),

            NNObj(self, O.GOTO_JUMPGATE, name='om15_to_biz_fly', target='om15_to_biz', towards=True),
            NNObj(self, O.JUMPGATE, target='om15_to_biz'),
            NNObj(self, O.TLR, target='biz_tlr_2'),
            NNObj(self, O.DOCK_BATTLESHIP, target='battleship'),
        ]



