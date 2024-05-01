from story.math import euler_to_quat
from universe.content.system_object import Marker
from universe.content.main_objects import Battleship, JumpableObject

from text.dividers import SINGLE_DIVIDER


OBJ_TYPE_TEMPLATE = 'type = rep_inst, {system}, {string_id}, {string_id}, {pos_x}, {pos_y}, {pos_z}, {target_nickname}'

FAIL_TLR = 90000  # вы не активировали торговый путь
FAIL_TARGET = 90001  # точка назначения
FAIL_LEAVE_COMBAT = 90002  # Вы покинули место сражения
FAIL_JUMPGATE = 90003  # Вы не активировали гиперврата
FAIL_DOCK_BASE = 90004  # Вы не провели стыковку с базой
FAIL_DOCK_BATTLESHIP = 90005  # Вы не провели стыковку с линкором
FAIL_LEAVE_BASE = 90006  # Вы покинули базу

LOCK_MANEUVERS = 'Act_LockManeuvers = true'
UNLOCK_MANEUVERS = 'Act_LockManeuvers = false'


class Nag(object):
    NAG_OFF = 'Act_NagOff = {nag_name}'
    NAG_OBJ_TOWARDS = 'Act_NagDistTowards = OBJ, {nag_name}, nag_voice, {obj_name}, {fail_id}, {range}, NAG_ALWAYS'
    NAG_OBJ_LEAVING = 'Act_NagDistLeaving = {nag_name}, nag_voice, {obj_name}, {fail_id}, {range}'
    NAG_ALWAYS = 'NAG_ALWAYS'
    TOWARDS_RANGE = 4000
    TLR_RANGE = 100
    JUMP_RANGE = 1000
    COMBAT_RANGE = 6000
    DOCK_RANGE = 4000

    'Act_NagDistLeaving = FirstTradelaneNag, nag_voice, SIG13_F_Trade_Lane_Ring_L1_04, 090000, 100, NAG_ALWAYS'
    'Act_NagDistLeaving = NagJumpBer, nag_voice, sig13_to_ber, 090003, 1, 1000, NAG_ALWAYS'
    'Act_NagDistLeaving = BlockpostBattleNag, nag_voice, MSN01_alaric, 090002, 6000, NAG_ALWAYS'
    'Act_NagDistLeaving = DockBerlinNag, nag_voice, Rh_Ber_01_Docking_Ring, 090004, 4000, NAG_ALWAYS'

    def __init__(self):
        self.last_nag_name = None

    @property
    def nag_voice(self):
        return 'Act_SpawnShip = nag_voice'

    def nag_off(self):
        if self.last_nag_name is not None:
            nag_off = self.NAG_OFF.format(nag_name=self.last_nag_name)
            self.last_nag_name = None
            return nag_off
        return ''

    def get_towards_nag(self, nag_name, target):
        items = []
        if self.last_nag_name:
            items.append(self.nag_off())

        self.last_nag_name = nag_name
        towards = self.NAG_OBJ_TOWARDS.format(
            nag_name=nag_name,
            obj_name=target,
            fail_id=FAIL_TARGET,
            range=self.TOWARDS_RANGE,
        )
        items.append(
            towards
        )
        return SINGLE_DIVIDER.join(items)

    def towards(self, nag_name, target):
        """for template"""
        return self.get_towards_nag(nag_name, target)

    def get_leaving_nag(self, nag_name, target, fail_id, range, nag_always=True):
        items = []
        if self.last_nag_name:
            items.append(self.nag_off())

        self.last_nag_name = nag_name
        leaving = self.NAG_OBJ_LEAVING.format(
            nag_name=nag_name,
            obj_name=target.get_name(),
            fail_id=fail_id,
            range=range,
        )
        if nag_always:
            leaving += f', {self.NAG_ALWAYS}'

        items.append(
            leaving
        )
        return SINGLE_DIVIDER.join(items)

    def tlr(self, nag_name, target):
        """for template"""
        return self.get_leaving_nag(nag_name, target, FAIL_TLR, self.TLR_RANGE)

    def obj(self, nag_name, target):
        """for template"""
        return self.get_leaving_nag(nag_name, target, FAIL_DOCK_BASE, self.DOCK_RANGE)

    def dock_battleship(self, nag_name, target):
        """for template"""
        return self.get_leaving_nag(nag_name, target, FAIL_DOCK_BATTLESHIP
                                    , self.DOCK_RANGE)

    def jump(self, nag_name, target):
        """for template"""
        return self.get_leaving_nag(nag_name, target, FAIL_JUMPGATE, self.JUMP_RANGE)

    def combat(self, nag_name, target):
        """for template"""
        return self.get_leaving_nag(nag_name, target, FAIL_LEAVE_COMBAT, self.COMBAT_RANGE, nag_always=False)


class Target(object):
    def get_nn_type(self, string_id):
        raise NotImplementedError

    def get_position(self):
        raise NotImplementedError

    def get_rotate(self):
        raise NotImplementedError

    def pos(self):
        """for template"""
        return '{0:.2f}, {1:.2f}, {2:.2f}'.format(*self.get_position())

    def orient(self):
        """for template"""
        return '{0:.2f}, {1:.2f}, {2:.2f}, {3:.2f}'.format(*euler_to_quat(*self.get_rotate()))

    def pos_orient(self):
        """for template"""
        return f'{self.pos()}, {self.orient()}'

    def get_name(self):
        raise NotImplementedError

    def open_access(self):
        return False

    def turn_nag(self, nag_name):
        return False


class Point(Target):
    def __init__(self, mission, system_class, alias):
        self.mission = mission
        self.system = self.mission.get_system(system_class.NAME)
        self.alias = alias
        self.marker = Marker(self.system, alias=self.alias)

    def get_position(self):
        return self.marker.get_position()

    def get_rotate(self):
        return self.marker.get_rotate()

    def get_name(self):
        raise Exception('still not implemented. should create nagvec')


class Obj(Target):

    def __init__(self, mission, instance_class):
        self.mission = mission
        self.instance_class = instance_class
        self.system = self.mission.get_system(instance_class.SYSTEM_NAME)
        self.instance = self.system.get_static_by_class(self.instance_class)

    def get_nn_type(self, string_id):
        position = self.instance.get_position()
        return OBJ_TYPE_TEMPLATE.format(
            system=self.system.NAME,
            string_id=string_id,
            pos_x=position[0],
            pos_y=position[1],
            pos_z=position[2],
            target_nickname=self.get_name(),
        )

    def get_name(self):
        return self.instance.get_inspace_nickname()

    def open_access(self):
        return f'Act_PlayerCanDock = false, {self.get_name()}'

    def turn_nag(self, nag_name):
        if issubclass(self.instance_class, Battleship):
            return self.mission.nag.tlr(nag_name, self)
        elif issubclass(self.instance_class, JumpableObject):
            return self.mission.nag.jump(nag_name, self)

        return self.mission.nag.dock(nag_name, self)


class Conn(Target):
    def __init__(self, mission, connection_class, start_point_class):
        self.mission = mission
        self.connection_class = connection_class
        self.start_point_class = start_point_class

        self.system = self.mission.get_system(connection_class.SYSTEM_NAME)
        self.connection_instance = self.system.get_trade_connection_by_class(self.connection_class)

        self.forward = False
        if self.start_point_class == connection_class.OBJ_FROM:
            print('fwd')
            self.forward = True
        elif self.start_point_class != connection_class.OBJ_TO:
            raise Exception('Conn %s have instance not from connection' % connection_class.__name__)

    def get_first_ring(self):
        return self.connection_instance.tradelanes[0 if self.forward else -1]

    def get_first_ring_name(self):
        return self.get_first_ring().get_ring_nickname()

    def get_last_ring_name(self):
        return self.connection_instance.tradelanes[-1 if self.forward else 0].get_ring_nickname()

    def get_first_two_rings_names(self):
        rings = (
            self.connection_instance.tradelanes[0:2]
            if self.forward else
            list(reversed(self.connection_instance.tradelanes[-2:]))
        )
        return ', '.join([ring.get_ring_nickname() for ring in rings])

    def get_position(self):
        return self.get_first_ring().get_tradelane_pos()

    def get_rotate(self):
        return self.get_first_ring().get_tradelane_rotate()

    def start_ring(self):
        """for template"""
        return self.get_first_ring_name()

    def last_ring(self):
        """for template"""
        return self.get_last_ring_name()

    def first_rings(self):
        """for template"""
        return self.get_first_two_rings_names()

    def get_nn_type(self, string_id):
        position = self.get_position()
        return OBJ_TYPE_TEMPLATE.format(
            system=self.system.NAME,
            string_id=string_id,
            pos_x=position[0],
            pos_y=position[1],
            pos_z=position[2],
            target_nickname=self.get_name(),
        )

    def get_name(self):
        return self.get_first_ring_name()

    def open_access(self):
        return f'Act_PlayerCanTradelane = false, {self.first_rings()}'

    def turn_nag(self, nag_name):
        return self.mission.nag.tlr(nag_name, self)

    @property
    def enter(self):
        actions = [
            f'Cnd_TLEntered = Player, {self.first_rings()}',
            LOCK_MANEUVERS,
            self.mission.nag.nag_off(),
        ]
        return SINGLE_DIVIDER.join(actions)

    @property
    def exit(self):
        actions = [
            f'Cnd_TLExited = Player, {self.last_ring()}',
            UNLOCK_MANEUVERS,
            'Act_PlayerCanTradelane = false',
        ]
        return SINGLE_DIVIDER.join(actions)


class Ship(Target):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class NNObj(object):
    TITLE = '[NNObjective]'
    NICKNAME_TEMPLATE = 'nickname = {nickname}'
    STATE = 'state = HIDDEN'

    def __init__(self, mission, string_id=None, name=None, target=None):
        self.mission = mission
        self.string_id = string_id if string_id else self.get_string_id()
        self.target = target
        self.target_point = self.get_target_point()
        self.name = f'nn_{name}' if name else self.generate_name()

    def get_string_id(self):
        raise NotImplementedError

    def get_simple_type(self):
        return f'type = ids, {self.string_id}'

    def generate_name(self):
        if not self.target_point:
            raise Exception('target is required')
        return f'nn_{self.target}'

    def get_name(self):
        return self.name

    def get_target_point(self):
        if self.target:
            return self.mission.get_point(self.target)

    def get_type_definition(self):
        if self.target_point:
            return self.target_point.get_nn_type(self.string_id)
        return self.get_simple_type()

    def get_definition(self):
        items = [
            self.TITLE,
            self.NICKNAME_TEMPLATE.format(nickname=self.get_name()),
            self.STATE,
            self.get_type_definition(),
        ]
        return SINGLE_DIVIDER.join(items)

    def set(self):
        """for template"""
        actions = [
            f'Act_SetNNObj = {self.get_name()}'
        ]
        if self.target:
            open_access = self.target_point.open_access()
            if open_access is not False:
                actions.append(open_access)

            turn_nag = self.target_point.turn_nag(self.get_name())
            if turn_nag is not False:
                actions.append(turn_nag)

        return SINGLE_DIVIDER.join(actions)


