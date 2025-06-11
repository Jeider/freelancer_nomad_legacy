import random

from universe import sirius as S
from universe.systems import br_avl
from story.ingame import ingame_mission
from story.math import euler_to_quat
from story import actors
from text.dividers import SINGLE_DIVIDER, DIVIDER

from story.ingame import names as N
from story.ingame import objectives as O
from story.ingame.tools import (
    Point, Obj, Conn, NNObj, Ship, Solar, Capital, SaveState, DockableBattleshipSolar, StaticJumpgate,
    MultiText, TextDialog, Direct, Trigger, DRY_RUN, DIALOG_YES_NO
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
    STATIC_NPCSHIPS = NPCSHIPS
    SCRIPT_INDEX = 8
    DIRECT_SYSTEMS = [S.br_avl, S.m8_tau44, S.m8_lair_enter, S.m8_lair_core, S.m8_lair_escape]

    def get_save_states(self):
        return [
            SaveState(self, 'li_enter', 'Патруль Либерти'),
        ]

    def get_dialogs(self):
        return [
            TextDialog(
                self, 'mount', 'Установка устройства невидимости',
                ru_content=MultiText([
                    'Хетчер выдала вам устройство невидимости. Вы должны установить его на место вашей контрмеры',

                    'Если вы вылетите без установленного устройства невидимости, то миссия будет проиграна.',
                ]),
            ),
        ]
    def get_real_objects(self):
        return {
            'vendor_planet': Obj(self, br_avl.AvalDockring),
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
            NNObj(self, O.GOTO, target='explore_area_waypoint6', reach_range=1000),

            NNObj(self, 'Уничтожьте вражеские истребители', name='destroy_entry_liberty'),

            NNObj(self, O.GOTO, target='enter_the_lair_wp1'),
            NNObj(self, O.GOTO, target='enter_the_lair_wp2'),

            NNObj(self, 'Уничтожьте перегородку шлюза', name='dock_wales', target='locked_door', nag=False),

            NNObj(self, 'Вступите в битву', name='enter_battle'),
            NNObj(self, 'Уничтожьте энергетические стойки', name='destroy_columns'),

            NNObj(self, O.GOTO, target='leave_lair_zone'),

        ]

    def get_static_points(self):
        defined_points = []

        main_group = [
            DockableBattleshipSolar(
                self, S.br_avl, 'price_wales_avalon', faction='br_grp',
                archetype='b_battleship', loadout='br_battleship_station',
                ru_name='Линкор Принц Уэльский', base='tau44_99_base'
            ),
            DockableBattleshipSolar(
                self, S.m8_tau44, 'price_wales_start', faction='br_grp',
                archetype='b_battleship', loadout='br_battleship_station',
                ru_name='Линкор Принц Уэльский', base='tau44_99_base'
            ),
            DockableBattleshipSolar(
                self, S.m8_tau44, 'price_wales_battle', faction='br_grp',
                archetype='b_battleship_fuseable', loadout='br_battleship_station',
                ru_name='Линкор Принц Уэльский', base='tau44_99_base',
                labels=['bretonia'],
            ),
            Solar(
                self, S.m8_lair_enter, 'locked_door', archetype='space_door_lock_destroyable',
                ru_name='Перегородка шлюза'
            ),
        ]
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
            # '04_road_to_station',
        ]

        tau44_core_points = [
            # '04_road_to_station',
        ]

        tau44_escape_points = [
            # '04_road_to_station',
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

        return defined_points

    def get_capital_ships(self):
        core_cruiser = {
            'npc_ship_arch': 'ms8_core_cruiser',
            'faction': 'fc_uk_grp',
            'labels': ['li_core'],
            'ru_name': N.LI_CRUISER,
        }
        li_cruiser = {
            'npc_ship_arch': 'ms8_li_cruiser',
            'faction': 'fc_uk_grp',
            'labels': ['li_core'],
            'ru_name': N.LI_CRUISER,
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
        outer_caps_count = 3

        for index in range(1, outer_caps_count+1):
            cap = f'li_cruiser{index}'
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
                labels=[
                    'li_enter',
                ],
                system_class=S.m8_tau44,
                slide_x=100,
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.Defender,
                    level=NPC.D10,
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
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.Defender,
                    level=NPC.D12,
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
                )
            ),

        ]
