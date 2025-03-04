import random

from universe import sirius as S
from story.ingame import ingame_mission
from story.math import euler_to_quat
from story import actors

from story.ingame import objectives as O
from story.ingame.tools import Point, Obj, Conn, NNObj, Ship, Solar, Capital, Patrol, Direct, DRY_RUN, Trigger
from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT

from world.npc import NPC, EqMap
from world import ship
from universe import faction

from text.dividers import SINGLE_DIVIDER, DIVIDER

NPCSHIPS = '''

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


class Misson10(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m10/m10.ini'
    FOLDER = 'M10'
    FILE = 'm10'
    SCRIPT_INDEX = 10
    DIRECT_SYSTEMS = [S.xen]
    STATIC_NPCSHIPS = NPCSHIPS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.patrol = Patrol(direct=self.direct, trigger=self.trigger)
        self.stealth = Stealth(direct=self.direct, trigger=self.trigger)

    def get_initial_context(self) -> dict:
        context = super().get_initial_context()
        context['patrol'] = self.patrol
        context['stealth'] = self.stealth
        return context

    def get_static_points(self):
        defined_points = []

        # SIRIUS

        xen_points = [
            'first_puff',
            'last_puff',

        ]
        for p in xen_points:
            defined_points.append(
                Point(self, S.xen, p)
            )

        return defined_points

    def get_nn_objectives(self):
        return [
            NNObj(self, O.GOTO, name='first_puff', target='first_puff'),
            NNObj(self, 'Доберитесь большого облака, минуя патрули', name='last_puff', target='last_puff'),
        ]

    def get_ships(self):
        return [
            # HQ
            Ship(
                self,
                'patroller',
                count=12,
                affiliation=faction.OrderMain.CODE,
                system_class=S.or_hq,  # TODO: make Xenos
                labels=[
                    'patroller',
                    'xenos',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.BretoniaPirate,
                    ship=ship.Stiletto,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),
        ]
