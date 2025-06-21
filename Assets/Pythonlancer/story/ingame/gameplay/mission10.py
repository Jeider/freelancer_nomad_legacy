import random

from universe import sirius as S
from story.ingame import ingame_mission
from story.math import euler_to_quat
from story import actors

from story.ingame import objectives as O
from story.ingame.tools import (
    Point, Obj, Conn, NNObj, Ship, Solar, DockableBattleshipSolar, Capital, Patrol, Direct, DRY_RUN, Trigger,
    SaveState, MultiLine
)
from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT

from world.npc import NPC, EqMap
from world import ship
from universe import faction

from text.dividers import SINGLE_DIVIDER, DIVIDER

NPCSHIPS = '''

[NPCShipArch]
nickname = ms10_armored
loadout = m12_armored
level = d10
ship_archetype = ge_armored
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER, d5

'''


class Stealth:

    MAIN = 'STEALTH_init'
    SAFE_ENABLE = 'STEALTH_safe_enable'
    SAFE_STOP = 'STEALTH_safe_turn_off'
    DANGER_ENABLE = 'STEALTH_danger_enable'
    DANGER_STOP = 'STEALTH_danger_turn_off'
    SAFE_EXIT = 'STEALTH_safe_exit'
    DANGER_EXIT = 'STEALTH_danger_exit'
    SAFE_EXIT_ZONE = 'STEALTH_{0}_safe_exit'
    DANGER_EXIT_ZONE = 'STEALTH_{0}_danger_exit'
    PATROLLER_CHECK = 'STEALTH_patroller{0}_near'
    PATROLLER_NAME = 'patroller{0}'
    PATROL_NEAR_DISTANCE = 2000
    FAIL_BY_PATROL = 'STEALTH_fail_by_patrol'
    FAIL_BY_TIMEOUT = 'STEALTH_fail_by_timeout'
    TIMEOUT_ACTION = 'STEALTH_timeout'
    TIMEOUT_SECONDS = 10
    SYSTEM_NAME = S.xen.NAME

    SAFE_ZONES = [
        'Zone_xenos_MAIN_nebula',
        'Zone_xenos_sphere01',
        'Zone_xenos_sphere02',
        'Zone_xenos_sphere03',
        'Zone_xenos_sphere04',
        'Zone_xenos_sphere05',
        'Zone_xenos_sphere06',
        'Zone_xenos_sphere07',
        'Zone_xenos_start_sphere',
    ]
    INIT_SAFE_ZONE = 'Zone_xenos_start_sphere'
    PATROLLERS_COUNT = 12

    def __init__(self, direct, trigger):
        self.direct: Direct = direct
        self.trigger: Trigger = trigger

    def turn(self):
        return f'Act_ActTrig = {self.MAIN}'

    def deactivate(self):
        return SINGLE_DIVIDER.join([
            self.deactivate_safe_exit_zones(),
            self.deactivate_danger_exit_zones(),
            self.deactivate_patroller_checks(),
            self.disable_static_actions(),
        ])

    def activate_safe_exit_zones(self):
        content = [self.trigger.turn(self.SAFE_EXIT_ZONE.format(t)) for t in self.SAFE_ZONES]
        return SINGLE_DIVIDER.join(content)

    def deactivate_safe_exit_zones(self):
        content = [self.trigger.off(self.SAFE_EXIT_ZONE.format(t)) for t in self.SAFE_ZONES]
        return SINGLE_DIVIDER.join(content)

    def activate_danger_exit_zones(self):
        content = [self.trigger.turn(self.DANGER_EXIT_ZONE.format(t)) for t in self.SAFE_ZONES]
        return SINGLE_DIVIDER.join(content)

    def deactivate_danger_exit_zones(self):
        content = [self.trigger.off(self.DANGER_EXIT_ZONE.format(t)) for t in self.SAFE_ZONES]
        return SINGLE_DIVIDER.join(content)

    def activate_patroller_checks(self):
        return SINGLE_DIVIDER.join([
            self.trigger.turn(self.PATROLLER_CHECK.format(i)) for i in range(1, self.PATROLLERS_COUNT+1)
        ])

    def deactivate_patroller_checks(self):
        return SINGLE_DIVIDER.join([
            self.trigger.off(self.PATROLLER_CHECK.format(i)) for i in range(1, self.PATROLLERS_COUNT+1)
        ])

    def get_safe_exit_zones(self):
        content = []
        for zone in self.SAFE_ZONES:
            trig = self.SAFE_EXIT_ZONE.format(zone)

            content += [
                self.trigger.new(trig),
                self.direct.outside_sphere(self.SYSTEM_NAME, zone),
                self.trigger.turn(self.SAFE_EXIT),
                'Act_EtherComm = nnvoice, 1, Player, mod_xenos_exit_gas, -1, , robot_body_E',
                ''
            ]

        return SINGLE_DIVIDER.join(content)

    def get_danger_exit_zones(self):
        content = []
        for zone in self.SAFE_ZONES:
            trig = self.DANGER_EXIT_ZONE.format(zone)

            content += [
                self.trigger.new(trig),
                self.direct.inside_sphere(self.SYSTEM_NAME, zone),
                self.trigger.turn(self.DANGER_EXIT),
                self.trigger.turn(self.DANGER_STOP),
                self.trigger.off(self.TIMEOUT_ACTION),
                self.trigger.turn(self.SAFE_EXIT_ZONE.format(zone)),
                'Act_EtherComm = nnvoice, 1, Player, mod_xenos_enter_gas, -1, , robot_body_E',
                ''
            ]

        return SINGLE_DIVIDER.join(content)

    def get_patroller_failed_zones(self):
        content = []
        for i in range(1, self.PATROLLERS_COUNT+1):
            trig = self.PATROLLER_CHECK.format(i)
            patroller = self.PATROLLER_NAME.format(i)

            content += [
                self.trigger.new(trig),
                f'Cnd_DistShip = inside, Player, {patroller}, {self.PATROL_NEAR_DISTANCE}',
                self.trigger.turn(self.FAIL_BY_PATROL),
                ''
            ]

        return SINGLE_DIVIDER.join(content)

    def get_patroller_checks(self):
        return SINGLE_DIVIDER.join([
            self.trigger.turn(self.PATROLLER_CHECK.format(i)) for i in range(1, self.PATROLLERS_COUNT+1)
        ])

    def define(self):
        content = [
            self.trigger.new(self.MAIN, dry=True),
            self.trigger.turn(
                self.SAFE_EXIT_ZONE.format(self.INIT_SAFE_ZONE),
            ),
            '',

            self.trigger.new(self.FAIL_BY_PATROL, dry=True),
            # 'Act_ChangeState = FAIL',
            'Act_EtherComm = nnvoice, 1, Player, mod_xenos_fail_patrol, -1, , robot_body_E',
            '',

            self.trigger.new(self.FAIL_BY_TIMEOUT, dry=True),
            # 'Act_ChangeState = FAIL',
            'Act_EtherComm = nnvoice, 1, Player, mod_xenos_fail_timeout, -1, , robot_body_E',
            '',

            self.trigger.new(self.TIMEOUT_ACTION),
            f'Cnd_Timer = {self.TIMEOUT_SECONDS}',
            self.trigger.turn(self.FAIL_BY_TIMEOUT),

            self.trigger.new(self.SAFE_ENABLE, dry=True),
            # self.activate_safe_exit_zones(),
            '',

            self.trigger.new(self.SAFE_STOP, dry=True),
            self.deactivate_safe_exit_zones(),
            '',

            self.trigger.new(self.DANGER_ENABLE, dry=True),
            self.trigger.turn(self.TIMEOUT_ACTION),
            self.activate_patroller_checks(),
            self.activate_danger_exit_zones(),
            '',

            self.trigger.new(self.DANGER_STOP, dry=True),
            self.deactivate_patroller_checks(),
            self.deactivate_danger_exit_zones(),
            '',

            self.trigger.new(self.SAFE_EXIT, dry=True),
            self.trigger.turn(self.SAFE_STOP),
            self.trigger.turn(self.DANGER_ENABLE),
            '',

            self.trigger.new(self.DANGER_EXIT, dry=True),
            self.trigger.turn(self.DANGER_STOP),
            self.trigger.turn(self.SAFE_ENABLE),
            '',
            ';;MRK1',
            self.get_safe_exit_zones(),
            ';;MRK2',
            self.get_danger_exit_zones(),
            ';;MRK3',
            self.get_patroller_failed_zones(),
        ]
        return SINGLE_DIVIDER.join(content)

    def disable_static_actions(self):
        return SINGLE_DIVIDER.join([
            self.trigger.off(self.MAIN),
            self.trigger.off(self.SAFE_EXIT_ZONE.format(self.INIT_SAFE_ZONE),),
            self.trigger.off(self.FAIL_BY_PATROL),
            self.trigger.off(self.FAIL_BY_TIMEOUT),
            self.trigger.new(self.TIMEOUT_ACTION),
            self.trigger.off(self.SAFE_ENABLE),
            self.trigger.off(self.SAFE_STOP),
            self.trigger.off(self.DANGER_ENABLE),
            self.trigger.off(self.DANGER_STOP),
            self.trigger.off(self.SAFE_EXIT),
            self.trigger.off(self.DANGER_EXIT),
        ])


class Misson10(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m10/m10.ini'
    FOLDER = 'M10'
    FILE = 'm10'
    START_SAVE_ID = 33000
    START_SAVE_RU_NAME = 'Система ксеносов. Линкор Мусаси'
    SCRIPT_INDEX = 10
    DIRECT_SYSTEMS = [S.xen]
    STATIC_NPCSHIPS = NPCSHIPS
    RTC = ['briefieng']
    INIT_OFFER = MultiLine(
        'ЗАДАЧА:',
        'Вызволить заключенных из тюрьмы на базе ксеносов',
        '',
        'СЛОЖНОСТЬ:',
        'Высокая.',
        '',
        'Награда:',
        'Освобождение Аларика, выполнение договора',
    ).get_content()

    def get_save_states(self):
        return [
            SaveState(self, 'inside_nebula', 'Ксеносы. Внутри главной туманности'),
            SaveState(self, 'near_base', 'Ксеносы. Рядом с базой'),
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.patrol = Patrol(direct=self.direct, trigger=self.trigger)
        self.stealth = Stealth(direct=self.direct, trigger=self.trigger)

    def get_initial_context(self) -> dict:
        context = super().get_initial_context()
        context['patrol'] = self.patrol
        context['stealth'] = self.stealth
        return context

    def get_ingame_thorns(self):
        return [
            IngameThorn(
                self,
                system_class=S.xen,
                template=GENERIC_TWO_POINT,
                name='m10_hacking',
                points={
                    'camera': 'cam_isnide',
                    'marker': 'xenos_control01',
                },
                duration=120,
            ),
        ]

    def get_static_points(self):
        defined_points = []

        xen_points = [
            'first_puff',
            'last_puff',
            'point_control',
            'prepare_point',
            'assault_target',
            'escape_point1',
            'escape_point2',
            'xenos_leave_musashi',
        ]
        for p in xen_points:
            defined_points.append(
                Point(self, S.xen, p)
            )

        defined_points.extend([
            Solar(self, S.xen, 'xenos_control01_door', ru_name='Дверь', archetype='space_door_lock2_destroyable'),
            Solar(self, S.xen, 'xenos_control_hack_layer_valid', ru_name='Взлом', archetype='m10_hacker_01_valid'),
            Solar(self, S.xen, 'xenos_control_hack_layer_3', ru_name='Взлом', archetype='m10_hacker_01_layer_03'),
            Solar(self, S.xen, 'xenos_control_hack_layer_2', ru_name='Взлом', archetype='m10_hacker_01_layer_02'),
            Solar(self, S.xen, 'xenos_control_hack_layer_1', ru_name='Взлом', archetype='m10_hacker_01_layer_01'),

            Solar(self, S.xen, 'xenos_launch_musashi', ru_name='Линкор Мусаси', base='xen_99_base',
                  archetype='k_battleship'),
            DockableBattleshipSolar(self, S.xen, 'xenos_leave_musashi', ru_name='Линкор Мусаси', base='xen_98_base',
                  archetype='k_battleship'),
        ])

        wplatforms_count = 6
        wplatforms = [f'xen_platform_{i:02d}' for i in range(1, wplatforms_count+1)]
        for sol in wplatforms:
            defined_points.append(
                Solar(self, S.xen, sol, ru_name='Орудийная платформа', labels=['enemy', 'wplatforms'],
                      archetype='wplatform_ms10', loadout='ms10_the_platform'),
            )

        return defined_points

    def get_nn_objectives(self):
        return [
            NNObj(self, O.LAUNCH, name='launch'),

            NNObj(self, O.GOTO, name='first_puff', target='first_puff', nag=False),
            NNObj(self, 'Доберитесь большого облака, минуя патрули',
                  name='last_puff', target='last_puff', nag=False),
            NNObj(self, O.GOTO, name='point_control', target='point_control'),

            NNObj(self, 'Уничтожьте дверь', name='destroy_door', target='xenos_control01_door'),
            NNObj(self, 'Взломайте панель управления', name='hack_the_system'),

            NNObj(self, 'Доберитесь до места встречи с Дерси и звеном Локи',
                  name='prepare_point', target='prepare_point'),
            NNObj(self, 'Направляйтесь к базе Ксеносов',
                  name='assault_target', target='assault_target'),

            NNObj(self, 'Уничтожьте орудийные платформы', name='destroy_wplatforms'),

            NNObj(self, 'Обеспечьте стыковку транспорта', name='defend_armored'),
            NNObj(self, 'Ожидайте транспорт', name='wait_for_armored'),
            NNObj(self, 'Обеспечьте защиту транспорта, пока он покидает зону битвы',
                  name='wait_for_armored_left_out'),

            NNObj(self, O.GOTO, name='escape_point1', target='escape_point1'),
            NNObj(self, O.GOTO, name='escape_point2', target='escape_point2'),
            NNObj(self, 'Сядьте на линкор Мусаси', name='dock_musashi', target='xenos_leave_musashi'),
        ]

    def get_ships(self):
        xen_npc_params = {
            'faction': faction.Ireland,
            'ship': ship.Centurion,
            'level': NPC.D10,
            'equip_map': EqMap(base_level=5),
        }
        wingman_npc_params = {
            'faction': faction.KusariMain,
            'ship': ship.Dragon,
            'level': NPC.D10,
            'equip_map': EqMap(base_level=6),
        }
        escort_npc_params = {
            'faction': faction.KusariMain,
            'ship': ship.Dragon,
            'level': NPC.D10,
            'equip_map': EqMap(base_level=6),
        }

        return [
            # TODO: make Xenos
            Ship(
                self,
                'patroller',
                count=12,
                affiliation=faction.Ireland.CODE,
                system_class=S.xen,
                labels=[
                    'patroller',
                    'xenos',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.Ireland,
                    ship=ship.Centurion,
                    level=NPC.D10,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'base_launch',
                count=3,
                affiliation=faction.Ireland.CODE,
                system_class=S.xen,
                arrival_obj='xen_01',
                labels=[
                    'xenos',
                    'enemy',
                ],
                npc=NPC(**xen_npc_params),
            ),
            Ship(
                self,
                'base_launch2',
                count=3,
                affiliation=faction.Ireland.CODE,
                system_class=S.xen,
                arrival_obj='xen_01',
                labels=[
                    'xenos',
                    'enemy',
                ],
                npc=NPC(**xen_npc_params),
            ),
            Ship(
                self,
                'xen_f1',
                count=3,
                affiliation=faction.Ireland.CODE,
                system_class=S.xen,
                slide_x=100,
                slide_z=-100,
                labels=[
                    'xenos',
                    'enemy',
                ],
                npc=NPC(**xen_npc_params),
            ),
            Ship(
                self,
                'xen_f2',
                count=3,
                affiliation=faction.Ireland.CODE,
                system_class=S.xen,
                slide_x=100,
                slide_z=100,
                labels=[
                    'xenos',
                    'enemy',
                ],
                npc=NPC(**xen_npc_params),
            ),
            Ship(
                self,
                'xen_f3',
                count=3,
                affiliation=faction.Ireland.CODE,
                system_class=S.xen,
                slide_x=-100,
                slide_z=-100,
                labels=[
                    'xenos',
                    'enemy',
                ],
                npc=NPC(**xen_npc_params),
            ),
            Ship(
                self,
                'xen_f4',
                count=3,
                affiliation=faction.Ireland.CODE,
                system_class=S.xen,
                slide_x=-100,
                slide_z=100,
                labels=[
                    'xenos',
                    'enemy',
                ],
                npc=NPC(**xen_npc_params),
            ),
            Ship(
                self,
                'darcy',
                hero=True,
                actor=actors.Darcy,
                labels=[
                    'asf',
                    'friend',
                    'trent_wing',
                ],
                npc=NPC(
                    faction=faction.BretoniaMain,
                    ship=ship.Crusader,
                    level=NPC.D19,
                    equip_map=EqMap(base_level=6),
                )
            ),
            Ship(
                self,
                'wingman',
                count=4,
                system_class=S.om7,
                labels=[
                    'friend',
                    'order',
                    'trent_wing'
                ],
                unique_npc_entry=True,
                base_name='Локи',
                npc=NPC(
                    faction=faction.KusariMain,
                    ship=ship.Falcon,
                    level=NPC.D6,
                    equip_map=EqMap(base_level=6),
                )
            ),
            Ship(
                self,
                'armor_helper',
                count=6,
                system_class=S.om7,
                labels=[
                    'friend',
                    'order',
                    'armor_wing'
                ],
                unique_npc_entry=True,
                base_name='Один',
                npc=NPC(
                    faction=faction.OrderMain,
                    ship=ship.Eagle,
                    level=NPC.D10,
                    equip_map=EqMap(base_level=5),
                )
            ),
        ]

    def get_capital_ships(self):
        armored_ship = {
            'npc_ship_arch': 'ms10_armored',
            'faction': 'fc_uk_grp',
            'labels': ['friend'],
        }
        armored_ship_out = {
            'npc_ship_arch': 'ms10_armored',
            'faction': 'fc_uk_grp',
            'labels': ['friend'],
            'arrival_obj': 'xen_01',
        }

        caps = [
            Capital(self, 'armored', ru_name='Бронированный транспорт', **armored_ship),
            Capital(self, 'armored_out', ru_name='Бронированный транспорт', **armored_ship_out),
        ]

        return caps
