import random

from universe import sirius as S
from universe.systems import br_avl, sig42
from story.ingame import ingame_mission
from story.math import euler_to_quat
from story import actors
from text.dividers import SINGLE_DIVIDER, DIVIDER

from story.ingame import names as N
from story.ingame import objectives as O
from story.ingame.tools import (
    Point, Obj, Conn, NNObj, Ship, Solar, Capital, SaveState, DockableBattleshipSolar, StaticJumpgate,
    MultiText, MultiLine, TextDialog, Direct, Trigger, DRY_RUN, DIALOG_YES_NO
)
from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT, GENERIC_MOUNTED_ROTATABLE

from world.npc import NPC, EqMap
from world import ship
from universe import faction

NPCSHIPS = '''

[NPCShipArch]
nickname = ms8_core_cruiser
loadout = li_grp_cruiser_nospeed
level = d19
ship_archetype = li_cruiser
pilot = cruiser_basecrusher
state_graph = CRUISER
npc_class = lawful, class_cruiser

[NPCShipArch]
nickname = ms8_li_cruiser
loadout = li_grp_cruiser
level = d19
ship_archetype = li_cruiser
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, class_cruiser

'''


class Misson08(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m08/m08.ini'
    FOLDER = 'M08'
    FILE = 'm08'
    START_SAVE_ID = 32800
    START_SAVE_RU_NAME = 'Планета Авалон'
    STATIC_NPCSHIPS = NPCSHIPS
    SCRIPT_INDEX = 8
    DIRECT_SYSTEMS = [S.br_avl, S.m8_tau44, S.m8_lair_enter, S.m8_lair_core, S.m8_lair_escape, S.m8_asf_hq, S.sig42]
    RTC = ['queen_rtc']
    INIT_OFFER = MultiLine(
        'ЗАДАЧА:',
        'Изучить обстановку в аванпосте ИРА, находящейся в зоне контроля СБА',
        '',
        'СЛОЖНОСТЬ:',
        'Высокая.',
        '',
        'Награда:',
        '50 000 кредитов',
    ).get_content()

    def get_save_states(self):
        return [
            SaveState(self, 'li_enter', 'Патруль Либерти'),
        ]

    def get_dialogs(self):
        return [
            TextDialog(
                self, 'launch', 'Линкор уже на месте',
                ru_content=MultiText([
                    'Линкор уже прибыл на место задания. Вы можете подготовить свой корабль и вылетать по готовности.',
                ]),
            ),
            TextDialog(
                self, 'columns', 'Энергетические колонны',
                ru_content=MultiText([
                    'Атакуйте энергетические колонны. Они расположены по экватору логова Кочевников.',
                ]),
            ),
            TextDialog(
                self, 'complete', 'Миссия завершена',
                ru_content=MultiText([
                    'Артефакт успешно передан на научную станцию. Миссия закончена. Ожидайте сообщений от Хетчер.',
                ]),
            ),
        ]

    def get_real_objects(self):
        return {
            'vendor_planet': Obj(self, br_avl.AvalDockring),
            'final_planet': Obj(self, sig42.Sig42Dockring),
        }

    def get_nn_objectives(self):
        return [
            NNObj(self, 'Встретьтесь с Дерси в баре планеты Авалон', name='meet_vendor', target='vendor_planet'),
            NNObj(self, O.LAUNCH, name='launch'),

            NNObj(self, 'Сядьте на линкор Принц Уэльский', name='dock_wales', target='price_wales_avalon'),

            NNObj(self, 'Подготовьтесь к миссии и вылетайте', name='prepare_and_launch'),
            NNObj(self, 'Исследуйте локацию', name='explore_area'),

            NNObj(self, O.GOTO, target='explore_area_waypoint1', reach_range=1000),
            NNObj(self, O.GOTO, target='explore_area_waypoint2', reach_range=1000),
            NNObj(self, O.GOTO, target='explore_area_waypoint3', reach_range=1000),
            NNObj(self, O.GOTO, target='explore_area_waypoint4', reach_range=600),
            NNObj(self, O.GOTO, target='explore_area_waypoint5', reach_range=1000),
            NNObj(self, O.GOTO, target='explore_area_waypoint6', reach_range=1500),

            NNObj(self, 'Уничтожьте вражеские истребители', name='destroy_entry_liberty'),

            NNObj(self, O.GOTO, target='enter_the_lair_wp1'),
            NNObj(self, O.GOTO, target='enter_the_lair_wp2'),

            NNObj(self, O.GOTO, target='enter_wp1', reach_range=200),
            NNObj(self, O.GOTO, target='enter_wp2', reach_range=200),
            NNObj(self, O.GOTO, target='enter_wp3', reach_range=200),
            NNObj(self, O.GOTO, target='enter_wp4', reach_range=200),
            NNObj(self, O.GOTO, target='enter_wp5', reach_range=200),
            NNObj(self, O.GOTO, target='enter_wp6', reach_range=200),
            NNObj(self, O.GOTO, target='enter_wp7', reach_range=200),
            NNObj(self, O.GOTO, target='enter_wp8', reach_range=200),
            NNObj(self, O.GOTO, target='enter_wp9', reach_range=200),

            NNObj(self, 'Уничтожьте перегородку шлюза', name='destroy_door', target='locked_door', nag=False),

            NNObj(self, O.GOTO, target='core_wp1', reach_range=200),
            NNObj(self, O.GOTO, target='core_wp2', reach_range=200),
            NNObj(self, O.GOTO, target='core_wp3', reach_range=200),
            NNObj(self, O.GOTO, target='core_escape_wp1', reach_range=200),
            NNObj(self, O.GOTO, target='core_escape_wp2', reach_range=200),

            NNObj(self, O.GOTO, target='escape_start1', reach_range=300),
            NNObj(self, O.GOTO, target='escape_start2', reach_range=300),
            NNObj(self, O.GOTO, target='escape_start3', reach_range=300),
            NNObj(self, O.GOTO, target='escape_start4', reach_range=300),
            NNObj(self, O.GOTO, target='escape_start5', reach_range=300),
            NNObj(self, O.GOTO, target='escape_start6', reach_range=300),
            NNObj(self, O.GOTO, target='escape_start7', reach_range=300),
            NNObj(self, O.GOTO, target='escape_start8', reach_range=300),

            NNObj(self, O.GOTO, target='escape_left_door', reach_range=300),
            NNObj(self, 'Пролетите туннель', name='escape_left_tunnel'),

            NNObj(self, O.GOTO, target='escape_middle1', reach_range=300),
            NNObj(self, O.GOTO, target='escape_middle2', reach_range=300),
            NNObj(self, O.GOTO, target='escape_middle3', reach_range=300),
            NNObj(self, O.GOTO, target='escape_middle4', reach_range=300),
            NNObj(self, O.GOTO, target='escape_middle5', reach_range=300),
            NNObj(self, O.GOTO, target='escape_end1', reach_range=300),
            NNObj(self, O.GOTO, target='escape_end2', reach_range=300),
            NNObj(self, O.GOTO, target='escape_end3', reach_range=300),
            NNObj(self, O.GOTO, target='escape_end4', reach_range=300),
            NNObj(self, O.GOTO, target='escape_end5', reach_range=300),
            NNObj(self, O.GOTO, target='escape_end6', reach_range=300),
            NNObj(self, O.GOTO, target='escape_end7', reach_range=300),

            NNObj(self, 'Вступите в битву', name='enter_battle'),
            NNObj(self, 'Уничтожьте энергетические стойки', name='destroy_columns'),

            NNObj(self, O.GOTO, target='leave_lair_zone'),

            NNObj(self, 'Следуйте за Хетчер', name='follow_hatcher'),
            NNObj(self, O.GOTO, name='goto_final_planet', target='final_planet', towards=True),
            NNObj(self, 'Сядьте на планету Спрага', name='dock_final_planet', target='final_planet'),
        ]

    def get_static_points(self):
        defined_points = []

        main_group = [
            DockableBattleshipSolar(
                self, S.br_avl, 'price_wales_avalon', faction='br_grp',
                archetype='b_battleship', loadout='br_battleship_station',
                ru_name='Линкор Принц Уэльский', base='br_avl_98_base'
            ),
            DockableBattleshipSolar(
                self, S.m8_tau44, 'price_wales_start', faction='br_grp',
                archetype='b_battleship', loadout='br_battleship_station',
                ru_name='Линкор Принц Уэльский', base='m8_tau44_99_base'
            ),
            Solar(
                self, S.m8_tau44, 'price_wales_battle', faction='br_grp',
                archetype='b_battleship_fuseable', loadout='br_battleship_station',
                ru_name='Линкор Принц Уэльский',
                labels=['bretonia'],
            ),
            Solar(
                self, S.m8_lair_enter, 'locked_door', archetype='space_door_lock_destroyable',
                ru_name='Перегородка шлюза'
            ),
        ]
        detonators = 12
        for i in range(1, detonators+1):
            main_group.append(
                Solar(
                    self, S.m8_tau44, f'kernel_launcher{i:02d}', archetype='kernel_launcher',
                    ru_name='Детонатор', loadout='lair_kernel_launcher'
                ),
            )

        defined_points.extend(main_group)
        self.add_solar_group('SOLAR_MAIN', main_group)

        tau44_points = [
            'explore_area_waypoint1',
            'explore_area_waypoint2',
            'explore_area_waypoint3',
            'explore_area_waypoint4',
            'explore_area_waypoint5',
            'explore_area_waypoint6',
            'enter_the_lair_wp1',
            'enter_the_lair_wp2',
            'leave_lair_zone',
        ]

        tau44_entry_points = [
            'enter_wp1',
            'enter_wp2',
            'enter_wp3',
            'enter_wp4',
            'enter_wp5',
            'enter_wp6',
            'enter_wp7',
            'enter_wp8',
            'enter_wp9',
        ]

        tau44_core_points = [
            'core_wp1',
            'core_wp2',
            'core_wp3',
            'core_escape_wp1',
            'core_escape_wp2',
        ]

        tau44_escape_points = [
            'escape_start1',
            'escape_start2',
            'escape_start3',
            'escape_start4',
            'escape_start5',
            'escape_start6',
            'escape_start7',
            'escape_start8',

            'escape_left_door',

            'escape_middle1',
            'escape_middle2',
            'escape_middle3',
            'escape_middle4',
            'escape_middle5',

            'escape_end1',
            'escape_end2',
            'escape_end3',
            'escape_end4',
            'escape_end5',
            'escape_end6',
            'escape_end7',
        ]

        for p in tau44_points:
            defined_points.append(
                Point(self, S.m8_tau44, p)
            )

        for p in tau44_entry_points:
            defined_points.append(
                Point(self, S.m8_lair_enter, p)
            )

        for p in tau44_core_points:
            defined_points.append(
                Point(self, S.m8_lair_core, p)
            )

        for p in tau44_escape_points:
            defined_points.append(
                Point(self, S.m8_lair_escape, p)
            )

        columns = [
            'outer_column01',
            'outer_column02',
            'outer_column03',
            'outer_column04',
            'outer_column05',
            'outer_column06',
            'outer_column07',
            'outer_column08',
        ]

        cols = []
        for column in columns:
            cols.append(
                Solar(self, S.m8_tau44, column, ru_name='Энергопоток',
                      archetype='lair_energy_column', labels=['outer_energy_column'])
            )

        defined_points.extend(cols)
        self.add_solar_group('COLUMNS', cols)

        fort_arch = {'archetype': 'rmbase_shipyard', 'loadout': 'rmbase_shipyard_m13'}

        hq_group = [
            Solar(self, S.m8_asf_hq, 'fort_bush',  ru_name='Форт Буш', **fort_arch),
            Solar(self, S.m8_asf_hq, 'fort1',  ru_name='Форт Джефферсон', **fort_arch),
            Solar(self, S.m8_asf_hq, 'fort2',  ru_name='Форт Аламо', **fort_arch),
            Solar(self, S.m8_asf_hq, 'fort3',  ru_name='Форт Стармер', **fort_arch),
            Solar(self, S.m8_asf_hq, 'fort4',  ru_name='Форт Росс', **fort_arch),
            Solar(self, S.m8_asf_hq, 'fort5',  ru_name='Форт Нокс', **fort_arch),
            DockableBattleshipSolar(
                self, S.m8_asf_hq, 'osiris1', faction='asf_grp',
                archetype='o_osiris', loadout='li_battleship_02',
                ru_name='Линкор Осирис', base='sig42_99_base',
                labels=['friend', 'asf', 'osiris']),
            Solar(
                self, S.m8_asf_hq, 'dread1', faction='asf_grp',
                archetype='l_dreadnought', loadout='li_dreadnought_03',
                ru_name='Линкор Миссисипи',
                labels=['friend', 'asf', 'osiris']),
            DockableBattleshipSolar(
                self, S.sig42, 'lair_osiris1', faction='asf_grp',
                archetype='o_osiris', loadout='li_battleship_02',
                ru_name='Линкор Осирис', base='sig42_99_base',
                labels=['friend', 'asf', 'osiris']),
        ]
        defined_points.extend(hq_group)
        self.add_solar_group('ASF_HQ', hq_group)

        return defined_points

    def get_capital_ships(self):
        core_cruiser = {
            'npc_ship_arch': 'ms8_core_cruiser',
            'faction': 'fc_uk_grp',
            'labels': ['li_core'],
            'ru_name': N.LI_CRUISER,
            'radius': 0,
        }
        li_cruiser = {
            'npc_ship_arch': 'ms8_li_cruiser',
            'faction': 'fc_uk_grp',
            'labels': ['liberty'],
            'ru_name': N.LI_CRUISER,
            'radius': 0,
        }

        caps = []

        core_caps = []
        core_caps_count = 3

        for index in range(1, core_caps_count+1):
            cap = f'core_cruiser{index}'
            the_cap = Capital(self, cap, **core_cruiser)
            caps.append(the_cap)
            core_caps.append(the_cap)

        self.add_capital_group('CORE_CAP', core_caps)

        outer_caps = []
        outer_caps_count = 2

        for index in range(1, outer_caps_count+1):
            cap = f'out_cruiser{index}'
            the_cap = Capital(self, cap, **li_cruiser)
            caps.append(the_cap)
            outer_caps.append(the_cap)

        self.add_capital_group('OUTER_CAP', outer_caps)

        return caps

    def get_ships(self):
        return [
            Ship(
                self,
                'darcy',
                hero=True,
                actor=actors.Darcy,
                labels=[
                    'friend',
                ],
                radius=0,
                npc=NPC(
                    faction=faction.BretoniaMain,
                    ship=ship.Cavalier,
                    level=NPC.D12,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'hatcher',
                hero=True,
                jumper=True,
                actor=actors.Hatcher,
                labels=[
                    'friend',
                ],
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.DefenderJuni,
                    level=NPC.D12,
                    equip_map=EqMap(base_level=5),
                    animated_wings=True,
                )
            ),
            Ship(
                self,
                'enter_fighter',
                count=5,
                # count=2,
                labels=[
                    'li_enter',
                ],
                system_class=S.m8_tau44,
                slide_x=-100,
                radius=0,
                affiliation=faction.LibertyMain.CODE,
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.Defender,
                    level=NPC.D8,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'core_fighter',
                count=12,
                labels=[
                    'li_core',
                ],
                radius=0,
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.Defender,
                    level=NPC.D12,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'br_fighterA',
                count=5,
                labels=[
                    'bretonia',
                    'friend',
                ],
                system_class=S.m8_tau44,
                slide_x=100,
                radius=0,
                affiliation=faction.BretoniaMain.CODE,
                npc=NPC(
                    faction=faction.BretoniaMain,
                    ship=ship.Cavalier,
                    level=NPC.D10,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'br_fighterB',
                count=5,
                labels=[
                    'bretonia',
                    'friend',
                ],
                system_class=S.m8_tau44,
                slide_x=100,
                radius=0,
                affiliation=faction.BretoniaMain.CODE,
                npc=NPC(
                    faction=faction.BretoniaMain,
                    ship=ship.Cavalier,
                    level=NPC.D10,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'li_fighterA',
                count=4,
                labels=[
                    'liberty',
                ],
                system_class=S.m8_tau44,
                slide_x=-100,
                radius=0,
                affiliation=faction.LibertyMain.CODE,
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.Defender,
                    level=NPC.D8,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'li_fighterB',
                count=4,
                labels=[
                    'liberty',
                ],
                system_class=S.m8_tau44,
                slide_x=-100,
                radius=0,
                affiliation=faction.LibertyMain.CODE,
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.Defender,
                    level=NPC.D8,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'li_fighterC',
                count=4,
                labels=[
                    'liberty',
                ],
                system_class=S.m8_tau44,
                slide_z=-100,
                radius=0,
                affiliation=faction.LibertyMain.CODE,
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.Patriot,
                    level=NPC.D8,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'li_fighterD',
                count=4,
                labels=[
                    'liberty',
                ],
                system_class=S.m8_tau44,
                slide_z=-100,
                radius=0,
                affiliation=faction.LibertyMain.CODE,
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.Patriot,
                    level=NPC.D8,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'asf',
                count=12,
                labels=[
                    'asf',
                ],
                affiliation=faction.ASF.CODE,
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.Defender,
                    level=NPC.D12,
                    equip_map=EqMap(base_level=5),
                    extra_equip=[
                        'equip = cloak_fast, HpCloak01, 1',
                    ],
                )
            ),

        ]
