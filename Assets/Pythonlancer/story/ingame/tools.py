from random import randint

from story.math import euler_to_quat
from universe.content.system_object import Marker
from universe.content.main_objects import Battleship, JumpableObject

from text.dividers import SINGLE_DIVIDER, DIVIDER


OBJ_TYPE_TEMPLATE = 'type = rep_inst, {system}, {string_id}, {string_id}, {pos_x}, {pos_y}, {pos_z}, {target_nickname}'
NAVMARKER_TYPE_TEMPLATE = 'type = navmarker, {system}, {string_id}, {string_id}, {pos_x}, {pos_y}, {pos_z}'

FAIL_TLR = 90000  # вы не активировали торговый путь
FAIL_TARGET = 90001  # точка назначения
FAIL_LEAVE_COMBAT = 90002  # Вы покинули место сражения
FAIL_JUMPGATE = 90003  # Вы не активировали гиперврата
FAIL_DOCK_BASE = 90004  # Вы не провели стыковку с базой
FAIL_DOCK_BATTLESHIP = 90005  # Вы не провели стыковку с линкором
FAIL_LEAVE_BASE = 90006  # Вы покинули базу

LOCK_MANEUVERS = 'Act_LockManeuvers = true'
UNLOCK_MANEUVERS = 'Act_LockManeuvers = false'
CLEAR_OBJECTIVES = 'Act_SetNNObj = null, OBJECTIVE_HISTORY'

PLAYER = 'Player'

EXPLODE = 'EXPLODE'
SILENT = 'SILENT'
DESTROY_MODES = (EXPLODE, SILENT)

GOTO = 'goto'
GOTO_CRUISE = 'goto_cruise'
GOTO_NO_CRUISE = 'goto_no_cruise'

GOTO_MODES = (GOTO, GOTO_CRUISE, GOTO_NO_CRUISE)


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

    def __init__(self):
        self.last_nag_name = None

    @property
    def nag_voice(self):
        actions = [
            'Act_Destroy = nag_voice, SILENT',
            'Act_SpawnShip = nag_voice'
        ]
        return SINGLE_DIVIDER.join(actions)

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
            obj_name=target.get_name(),
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

    def get_leaving_nag(self, nag_name, target, fail_id, nag_range, nag_always=True):
        items = []
        if self.last_nag_name:
            items.append(self.nag_off())

        self.last_nag_name = nag_name
        leaving = self.NAG_OBJ_LEAVING.format(
            nag_name=nag_name,
            obj_name=target.get_name(),
            fail_id=fail_id,
            range=nag_range,
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

    def dock_base(self, nag_name, target):
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
        print(self)
        raise NotImplementedError

    def get_rotate(self):
        raise NotImplementedError

    @staticmethod
    def get_rotate_random():
        return (
            randint(0, 360),
            randint(0, 360),
            randint(0, 360)
        )

    @property
    def pos(self):
        """for template"""
        return '{0:.2f}, {1:.2f}, {2:.2f}'.format(*self.get_position())

    @property
    def orient(self):
        """for template"""
        return '{0:.2f}, {1:.2f}, {2:.2f}, {3:.2f}'.format(*euler_to_quat(*self.get_rotate()))

    @property
    def orient_random(self):
        """for template"""
        return '{0:.2f}, {1:.2f}, {2:.2f}, {3:.2f}'.format(*euler_to_quat(*self.get_rotate_random()))

    @property
    def pos_orient(self):
        """for template"""
        return f'{self.pos}, {self.orient}'

    def get_name(self):
        raise NotImplementedError

    def open_access(self):
        return False

    def turn_nag(self, nag_name, towards=False):
        return False

    def goto_vec(self, mode=GOTO, near=100):
        if mode not in GOTO_MODES:
            raise Exception('Unknown goto mode %s in point' % mode)
        pos = self.get_position()
        return f'GotoVec = {mode}, {pos[0]}, {pos[1]}, {pos[2]}, {near}, true'

    def goto_obj(self, mode=GOTO, near=100):
        if mode not in GOTO_MODES:
            raise Exception('Unknown goto mode %s in point' % mode)

        return f'GotoShip = {mode}, {self.get_name()}, {near}, true'


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

    def get_nn_type(self, string_id):
        position = self.get_position()
        return NAVMARKER_TYPE_TEMPLATE.format(
            system=self.system.NAME,
            string_id=string_id,
            pos_x=position[0],
            pos_y=position[1],
            pos_z=position[2],
        )


class Solar(Target):

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
        return self.alias

    def get_nn_type(self, string_id):
        position = self.marker.get_position()
        return OBJ_TYPE_TEMPLATE.format(
            system=self.system.NAME,
            string_id=string_id,
            pos_x=position[0],
            pos_y=position[1],
            pos_z=position[2],
            target_nickname=self.get_name(),
        )

    @property
    def name(self):
        """for template"""
        return self.get_name()


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

    def get_position(self):
        return self.instance.get_position()

    def get_rotate(self):
        return self.instance.get_rotate()

    def get_name(self):
        return self.instance.get_inspace_nickname()

    def open_access(self):
        return f'Act_PlayerCanDock = false, {self.get_name()}'

    def turn_nag(self, nag_name, towards=False):
        if towards:
            return self.mission.nag.towards(nag_name, self)

        if issubclass(self.instance_class, Battleship):
            return self.mission.nag.tlr(nag_name, self)
        elif issubclass(self.instance_class, JumpableObject):
            return self.mission.nag.jump(nag_name, self)

        return self.mission.nag.dock_base(nag_name, self)

    @property
    def name(self):
        """for template"""
        return self.get_name()

    @property
    def base(self):
        """for template"""
        return self.instance.get_base_nickname()

    @property
    def make_neutral(self):
        return f'Act_SetRep = Player, {self.instance.FACTION}, 0'


class Conn(Target):
    def __init__(self, mission, connection_class, start_point_class):
        self.mission = mission
        self.connection_class = connection_class
        self.start_point_class = start_point_class

        self.system = self.mission.get_system(connection_class.SYSTEM_NAME)
        self.connection_instance = self.system.get_trade_connection_by_class(self.connection_class)

        self.forward = False
        if self.start_point_class == connection_class.OBJ_FROM:
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

    @property
    def start_ring(self):
        """for template"""
        return self.get_first_ring_name()

    @property
    def last_ring(self):
        """for template"""
        return self.get_last_ring_name()

    @property
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
        return f'Act_PlayerCanTradelane = false, {self.first_rings}'

    def turn_nag(self, nag_name, towards=False):
        return self.mission.nag.tlr(nag_name, self)

    def enter_target(self, target=None):
        target_name = 'Player'
        if target:
            target_name = target.get_name()

        actions = [
            f'Cnd_TLEntered = {target_name}, {self.first_rings}',
            LOCK_MANEUVERS,
            self.mission.nag.nag_off(),
            CLEAR_OBJECTIVES,
        ]
        return SINGLE_DIVIDER.join(actions)

    @property
    def enter(self):
        return self.enter_target()

    def exit_target(self, target=None):
        target_name = 'Player'
        if target:
            target_name = target.get_name()

        actions = [
            f'Cnd_TLExited = {target_name}, {self.last_ring}',
        ]
        if target is None:
            actions.extend([
                UNLOCK_MANEUVERS,
                'Act_PlayerCanTradelane = false',
            ])
        return SINGLE_DIVIDER.join(actions)

    @property
    def exit(self):
        return self.exit_target()


class RelPos(object):
    def __init__(self, deg, target_name, radius):
        self.deg = deg
        self.target_name = target_name
        self.radius = radius

    def get_ini(self):
        return f'{self.deg}, {self.target_name}, {self.radius}'



class Ship(Target):
    DEFAULT_AFFILIATION = 'fc_uk_grp'

    def __init__(self, mission, name, count=1, npc=None, actor=None,
                 affiliation=None, jumper=False, labels=None,
                 rel_pos=None, relative_pos=False, relative_target='Player', relative_range=1000,
                 radius=None, system_class=None, name_ids=None, unique_npc_entry=False,
                 slide_x=0, slide_y=0, slide_z=0):
        self.mission = mission
        self.system = (
            self.mission.get_system(system_class.NAME)
            if system_class
            else None
        )
        self.name = name
        self.count = count
        self.npc = npc
        self.jumper = jumper
        self.affiliation = affiliation or self.DEFAULT_AFFILIATION
        self.rel_pos = rel_pos
        self.relative_pos = relative_pos
        self.relative_target = relative_target
        self.relative_range = relative_range
        self.rel_deg = self.get_init_rel_deg()
        self.radius = radius
        self.actor = actor
        self.labels = labels if labels is not None else []
        self.name_ids = name_ids if name_ids is not None else []
        self.unique_npc_entry = unique_npc_entry
        if self.npc:
            self.npc.set_name(self.get_npc_shiparch_name())
        self.slide_x = slide_x
        self.slide_y = slide_y
        self.slide_z = slide_z

    def get_name(self):
        return self.name

    def member(self, index=1):
        """for template"""
        if self.count > 1:
            return self.get_multiple_member_name(index)
        return self.get_single_member_name()

    def is_single(self):
        return self.count == 1

    def is_multiple(self):
        return self.count > 1

    def get_single_member_name(self):
        return f'{self.name}'

    def get_multiple_member_name(self, index):
        return f'{self.name}{index}'

    def get_member_name(self, index=1):
        if self.is_single():
            return self.get_single_member_name()
        else:
            return self.get_multiple_member_name(index)

    def get_mission_npc_name(self, index=1):
        if not self.unique_npc_entry:
            return f'npc_{self.name}'

        return f'npc_{self.name}_{index}'

    def get_npc_shiparch_name(self):
        return f'{self.mission.FILE}_{self.name}'

    def get_mission_npc(self, index=1):
        items = [
            '[NPC]',
            f'nickname = {self.get_mission_npc_name(index)}',
            f'npc_ship_arch = {self.get_npc_shiparch_name()}',
            f'affiliation = {self.affiliation}',
        ]
        if self.actor:
            if self.actor.NAME_ID:
                items.append(f'individual_name = {self.actor.NAME_ID}')
            if self.actor.COMM_APPEARANCE:
                items.append(f'space_costume = {self.actor.COMM_APPEARANCE}')
            if self.actor.SPACE_VOICE:
                items.append(f'voice = {self.actor.SPACE_VOICE}')
        else:
            if self.name_ids:
                items.append(f'individual_name = {self.name_ids[index-1]}')

        return SINGLE_DIVIDER.join(items)

    def get_mission_npcs(self):
        if not self.unique_npc_entry:
            return self.get_mission_npc()

        entries = []
        for index in range(1, self.count+1):
            entries.append(self.get_mission_npc(index))

        return DIVIDER.join(entries)

    def get_mission_ship(self, index=1):
        items = [
            '[MsnShip]',
            f'nickname = {self.member(index)}',
            f'NPC = {self.get_mission_npc_name(index)}',
        ]
        if self.jumper:
            items.append('jumper = true')
        if not self.actor or not self.actor.NAME_ID:
            if not self.name_ids:
                items.append('random_name = true')
        if self.rel_pos:
            items.append(f'rel_pos = {self.rel_pos.get_ini()}')
        if self.relative_pos:
            items.append(f'rel_pos = {self.get_next_deg(index)}, {self.relative_target}, {self.relative_range}')
        if self.radius:
            items.append(f'radius = {self.radius}')
        for label in self.labels:
            items.append(f'label = {label}')
        return SINGLE_DIVIDER.join(items)

    def get_init_rel_deg(self):
        return randint(0, 360)

    def get_rel_deg_step(self):
        return 360 / self.count

    def get_next_deg(self, index):
        if index != 1:
            self.rel_deg += self.get_rel_deg_step()
            if self.rel_deg > 360:
                self.rel_deg -= 360
        return int(self.rel_deg)

    def get_mission_ships(self):
        msn_ships = []
        for member_index in range(1, self.count+1):
            msn_ships.append(
                self.get_mission_ship(member_index)
            )
        return DIVIDER.join(msn_ships)

    def spawn(self, objlist='no_ol'):
        if self.relative_pos:
            raise Exception('Ship %s is configured as relative-pos' % self.name)
        if self.count > 1:
            raise Exception('Ship %s is not single' % self.name)
        return f'Act_SpawnShip = {self.get_single_member_name()}, {objlist}'

    def spawn_all(self):
        """Just spawn all ships, defined in relative pos mode"""
        if not self.relative_pos:
            raise Exception('Ship %s is not configured as relative-pos' % self.name)
        actions = []
        for index in range(1, self.count+1):
            actions.append(f'Act_SpawnShip = {self.get_multiple_member_name(index)}')
        return SINGLE_DIVIDER.join(actions)

    def spawn_all_with_pos_orient(self, objlist='no_ol'):
        """Spawn all ships by points in system. Points must be defined in system like NAME1, etc"""
        if self.system is None:
            raise Exception('System is not defined for ship %s' % self.name)
        actions = []
        for index in range(1, self.count+1):
            name = self.get_multiple_member_name(index)
            marker = Marker(self.system, name)
            pos_orient = '{0:.2f}, {1:.2f}, {2:.2f}, {3:.2f}, {4:.2f}, {5:.2f}, {6:.2f}'.format(
                *marker.get_position(),
                *euler_to_quat(*marker.get_rotate())
            )
            actions.append(f'Act_SpawnShip = {name}, {objlist}, {pos_orient}')

        return SINGLE_DIVIDER.join(actions)

    def spawn_all_slide(self, objlist='no_ol'):
        """Spawn all ships with slide. Like formation. Point with SHIP NAME is MANDATORY in System"""
        if self.system is None:
            raise Exception('System is not defined for ship %s' % self.name)
        if self.slide_x == 0 and self.slide_y == 0 and self.slide_z == 0:
            raise Exception('At least one slide param must be defined for ship %s' % self.name)
        marker = Marker(self.system, self.name)
        pos = list(marker.get_position())
        orient = euler_to_quat(*marker.get_rotate())
        actions = []
        for index in range(1, self.count+1):
            params = [
                self.get_multiple_member_name(index),
                objlist,
                *pos,
                *orient
            ]
            actions.append(f'Act_SpawnShip = {", ".join(map(str, params))}')

            pos[0] += self.slide_x
            pos[1] += self.slide_y
            pos[2] += self.slide_z

        return SINGLE_DIVIDER.join(actions)

    def mark_all(self, exclude=None):
        actions = []
        exclude = exclude or []
        for index in range(1, self.count+1):
            if index in exclude:
                continue
            actions.append(f'Act_MarkObj = {self.get_member_name(index)}, 1')
        return SINGLE_DIVIDER.join(actions)

    def unmark_all(self, exclude=None):
        actions = []
        exclude = exclude or []
        for index in range(1, self.count+1):
            if index in exclude:
                continue
            actions.append(f'Act_MarkObj = {self.get_member_name(index)}, 0')
        return SINGLE_DIVIDER.join(actions)

    def destroy_all(self, destroy_mode, exclude=None):
        if destroy_mode not in DESTROY_MODES:
            raise Exception('Unknown destroy kind %s' % destroy_mode)
        actions = []
        exclude = exclude or []
        for index in range(1, self.count+1):
            if index in exclude:
                continue
            actions.append(f'Act_Destroy = {self.get_member_name(index)}, {destroy_mode}')
        return SINGLE_DIVIDER.join(actions)

    def hide_all(self, exclude=None):
        return self.destroy_all(SILENT, exclude)

    def explode_all(self, exclude=None):
        return self.destroy_all(EXPLODE, exclude)

    def member_list(self, separator=', ', exclude=None):
        members = []
        exclude = exclude or []
        for index in range(1, self.count+1):
            if index in exclude:
                continue
            members.append(self.get_member_name(index))

        return separator.join(members)

    def formation_members(self, exclude=None):
        members = []
        exclude = exclude or []
        for index in range(1, self.count+1):
            if index in exclude:
                continue
            members.append(f'ship = {self.get_member_name(index)}')

        return SINGLE_DIVIDER.join(members)

    def give_objlist_all(self, objlist, exclude=None):
        members = []
        exclude = exclude or []
        for index in range(1, self.count+1):
            if index in exclude:
                continue
            members.append(f'Act_GiveObjList = {self.get_member_name(index)}, {objlist}')

        return SINGLE_DIVIDER.join(members)

    def invulnerable(self, godmode, damage_from_player=None, alive_percent=None, exclude=None):
        members = []
        exclude = exclude or []
        params = [
            'true' if godmode else 'false',
        ]
        if damage_from_player is not None:
            params.append('true' if damage_from_player else 'false',)

            if alive_percent is not None:
                params.append(alive_percent)

        params_string = ", ".join(map(str, params))

        for index in range(1, self.count+1):
            if index in exclude:
                continue
            members.append(f'Act_Invulnerable = {self.get_member_name(index)}, {params_string}')

        return SINGLE_DIVIDER.join(members)


class NNObj(object):
    TITLE = '[NNObjective]'
    NICKNAME_TEMPLATE = 'nickname = {nickname}'
    STATE = 'state = HIDDEN'

    def __init__(self, mission, string_id=None, name=None, target=None, towards=False, nag=True):
        self.mission = mission
        self.string_id = string_id if string_id else self.get_string_id()
        self.target = target
        self.target_point = self.get_target_point()
        self.name = f'nn_{name}' if name else self.generate_name()
        self.towards = towards
        self.nag = nag

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
            if open_access is not False and not self.towards:
                actions.append(open_access)

            if self.nag:
                turn_nag = self.target_point.turn_nag(self.get_name(), towards=self.towards)
                if turn_nag is not False:
                    actions.append(turn_nag)

        return SINGLE_DIVIDER.join(actions)

    def set_as_path(self):
        if not self.target or self.target_point.__class__ != Obj:
            raise Exception('Cant use path for nn without Obj target for %s' % self.name)
        path_params = [
            str(self.string_id),
            str(self.string_id),
            self.target_point.name,
            self.target_point.system.NAME,
        ]
        params_line = ", ".join(path_params)
        return f'Act_NNPath = {params_line}'