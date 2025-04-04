from random import randint

from audio.sound import Sound

from story.math import euler_to_quat
from universe.content.system_object import Marker
from universe.content.main_objects import Battleship, JumpableObject

from text.dividers import SINGLE_DIVIDER, DIVIDER


DEFAULT_AFFILIATION = 'fc_uk_grp'

OBJ_TYPE_TEMPLATE = 'type = rep_inst, {system}, {string_id}, {string_id}, {pos_x}, {pos_y}, {pos_z}, {target_nickname}'
NAVMARKER_TYPE_TEMPLATE = 'type = navmarker, {system}, {string_id}, {string_id}, {pos_x}, {pos_y}, {pos_z}'
ETHER_COMM_TEMPLATE = 'Act_EtherComm = {voice_root}, {string_id}, Player, {line}, -1, {comm_appearance}'

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
TRIGGER = '[Trigger]'

GOTO = 'goto'
GOTO_CRUISE = 'goto_cruise'
GOTO_NO_CRUISE = 'goto_no_cruise'

GOTO_MODES = (GOTO, GOTO_CRUISE, GOTO_NO_CRUISE)

DRY_RUN = 'Cnd_True = no_params'
NO_OL = 'no_ol'
SHAPE_SPHERE = 'SPHERE'


def ini_boolean(boolval):
    return 'true' if boolval else 'false'


class Nag:
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
        return self.get_leaving_nag(nag_name, target, FAIL_DOCK_BATTLESHIP, self.DOCK_RANGE)

    def jump(self, nag_name, target):
        """for template"""
        return self.get_leaving_nag(nag_name, target, FAIL_JUMPGATE, self.JUMP_RANGE)

    def combat(self, nag_name, target):
        """for template"""
        return self.get_leaving_nag(nag_name, target, FAIL_LEAVE_COMBAT, self.COMBAT_RANGE, nag_always=False)


class Target:
    def get_nn_type(self, string_id):
        raise NotImplementedError

    def get_position(self):
        raise NotImplementedError

    def get_rotate(self):
        raise NotImplementedError

    def get_size(self):
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

    @property
    def size(self):
        return self.get_size()

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

    def inside_pos(self, range, obj='Player'):
        return f'Cnd_DistVec = inside, {obj}, {self.pos}, {range}'

    def outside_pos(self, range, obj='Player'):
        return f'Cnd_DistVec = outside, {obj}, {self.pos}, {range}'

    def inside_sphere(self, obj='Player'):
        return f'Cnd_DistVec = inside, {obj}, {self.pos}, {self.size[0]}'

    def outside_sphere(self, obj='Player'):
        return f'Cnd_DistVec = outside, {obj}, {self.pos}, {self.size[0]}'

    def inside_obj(self, range, obj='Player'):
        raise NotImplementedError

    def outside_obj(self, range, obj='Player'):
        raise NotImplementedError


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

    def get_size(self):
        return self.marker.get_size()

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


class DefinedStaticMixin:

    def get_name(self):
        raise NotImplementedError

    @property
    def name(self):
        """for template"""
        return self.get_name()

    def cond_destroyed(self):
        return f'Cnd_Destroyed = {self.name}'

    def destroy(self, mode=EXPLODE):
        return f'Act_Destroy = {self.name}, {mode}'

    def hide(self):
        return self.destroy(mode=SILENT)

    def fuse(self, fuse_name):
        return f'Act_LightFuse = {self.name}, {fuse_name}'

    def inside_obj(self, range, obj='Player'):
        return f'Cnd_DistShip = inside, {obj}, {self.name}, {range}'

    def outside_obj(self, range, obj='Player'):
        return f'Cnd_DistShip = outside, {obj}, {self.name}, {range}'

    def mark(self):
        return f'Act_MarkObj = {self.name}, 1'

    def unmark(self):
        return f'Act_MarkObj = {self.name}, 0'

    def invulnerable(self, godmode=True, damage_from_player=None, alive_percent=None):
        params = [ini_boolean(godmode)]
        if damage_from_player is not None:
            params.append(ini_boolean(damage_from_player))

            if alive_percent is not None:
                params.append(alive_percent)

        params_string = ", ".join(map(str, params))

        return f"Act_Invulnerable = {self.get_name()}, {params_string}"


class Solar(DefinedStaticMixin, Point):

    def __init__(self, *args, ru_name, labels=None, base=None, **kwargs):
        self.ru_name = ru_name
        self.base = base
        self.labels = labels if labels else []
        super().__init__(*args, **kwargs)
        self.ids_name = self.mission.ids.new_name(self.ru_name)

    def get_name(self):
        return self.alias

    @property
    def string_id(self):
        return self.ids_name.id

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

    def spawn(self):
        return f'Act_SpawnSolar = {self.get_name()}'

    def define(self, archetype, loadout=None, faction=None, label=None):
        solar = [
            '[MsnSolar]',
            f'nickname = {self.name}',
            f'position = {self.pos}',
            f'orientation = {self.orient}',
            f'archetype = {archetype}',
            f'faction = {faction}' if faction else f'faction = {DEFAULT_AFFILIATION}',
            f'string_id = {self.ids_name.id}',
            'radius = 0',
        ]
        if self.base:
            solar.append(f'base = {self.base}')
            solar.append(f'system = {self.system.NAME}')
        if loadout:
            solar.append(f'loadout = {loadout}')
        if label:
            solar.append(f'label = {label}')
        for root_label in self.labels:
            solar.append(f'label = {root_label}')

        return SINGLE_DIVIDER.join(solar)


class StaticJumpgate(Solar):

    def open_access(self):
        return f'Act_PlayerCanDock = false, {self.get_name()}'

    def turn_nag(self, nag_name, towards=False):
        return self.mission.nag.jump(nag_name, self)


class DockableSolar(Solar):

    def open_access(self):
        return f'Act_PlayerCanDock = false, {self.get_name()}'

    def turn_nag(self, nag_name, towards=False):
        return self.mission.nag.dock_base(nag_name, self)


class DockableBattleshipSolar(Solar):

    def open_access(self):
        return f'Act_PlayerCanDock = false, {self.get_name()}'

    def turn_nag(self, nag_name, towards=False):
        return self.mission.nag.dock_battleship(nag_name, self)


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
            return self.mission.nag.dock_battleship(nag_name, self)
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


class RelPos:
    def __init__(self, deg, target_name, radius):
        self.deg = deg
        self.target_name = target_name
        self.radius = radius

    def get_ini(self):
        return f'{self.deg}, {self.target_name}, {self.radius}'


class Ship(Target):
    def __init__(self, mission, name, count=1, hero=False, npc=None, actor=None,
                 affiliation=None, jumper=False, labels=None,
                 rel_pos=None, relative_pos=False, relative_target='Player', relative_range=1000,
                 radius=None, system_class=None, base_name=None, unique_npc_entry=False,
                 slide_x=0, slide_y=0, slide_z=0):
        self.mission = mission
        self.ids = self.mission.ids
        self.system = (
            self.mission.get_system(system_class.NAME)
            if system_class
            else None
        )
        self.name = name
        self.count = count
        self.hero = hero
        self.npc = npc
        self.jumper = jumper
        self.affiliation = affiliation or DEFAULT_AFFILIATION
        self.rel_pos = rel_pos
        self.relative_pos = relative_pos
        self.relative_target = relative_target
        self.relative_range = relative_range
        self.rel_deg = self.get_init_rel_deg()
        self.radius = radius
        self.actor = actor
        self.labels = labels if labels is not None else []
        self.base_name = base_name
        self.unique_npc_entry = unique_npc_entry
        if self.npc:
            self.npc.set_name(self.get_npc_shiparch_name())
        self.slide_x = slide_x
        self.slide_y = slide_y
        self.slide_z = slide_z
        self.respawn_defined = False

    def get_name(self):
        return self.name

    def member(self, index=1):
        """for template"""
        if self.count > 1:
            return self.get_multiple_member_name(index)
        return self.get_single_member_name()

    def member_obj(self, index=1):
        """for template"""
        return ShipMember(self, index)

    @property
    def leader(self):
        """for template"""
        return self.member(1)

    @property
    def the(self):
        """for template"""
        return self.member(1)

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
            if self.actor.RU_NAME:
                ids_name = self.ids.new_name(self.actor.RU_NAME)
                items.append(f'individual_name = {ids_name.id}')
            if self.actor.COMM_APPEARANCE:
                items.append(f'space_costume = {self.actor.COMM_APPEARANCE}')
            if self.actor.SPACE_VOICE:
                items.append(f'voice = {self.actor.SPACE_VOICE}')
        else:
            if self.base_name:
                try:
                    ids_name = self.ids.new_name(f'{self.base_name} {index}')
                    items.append(f'individual_name = {ids_name.id}')
                except IndexError:
                    pass

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
        if not self.actor or not self.actor.RU_NAME:
            if not self.base_name:
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

    def spawn(self, objlist=NO_OL, pos=None):
        if self.relative_pos:
            raise Exception('Ship %s is configured as relative-pos' % self.name)
        if self.count > 1:
            raise Exception('Ship %s is not single' % self.name)

        spawn = f'Act_SpawnShip = {self.get_single_member_name()}, {objlist}'
        if pos:
            spawn = ', '.join([spawn, pos])

        items = [spawn]
        if self.hero:
            items.append(self.invulnerable())
            items.append(self.mark_all())

        return SINGLE_DIVIDER.join(items)

    def spawn_member(self, member_index=1, objlist=NO_OL):
        return f'Act_SpawnShip = {self.get_multiple_member_name(member_index)}, {objlist}'

    def spawn_all(self):
        """Just spawn all ships, defined in relative pos mode"""
        if not self.relative_pos:
            raise Exception('Ship %s is not configured as relative-pos' % self.name)
        actions = []
        for index in range(1, self.count+1):
            actions.append(f'Act_SpawnShip = {self.get_multiple_member_name(index)}')
        return SINGLE_DIVIDER.join(actions)

    def spawn_all_with_pos_orient(self, objlist=NO_OL):
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

    def spawn_all_slide(self, objlist=NO_OL):
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

    def destroy_member(self, member_index, destroy_mode):
        if destroy_mode not in DESTROY_MODES:
            raise Exception('Unknown destroy kind %s' % destroy_mode)
        return f'Act_Destroy = {self.get_member_name(member_index)}, {destroy_mode}'

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

    def invulnerable(self, godmode=True, damage_from_player=None, alive_percent=None, exclude=None):
        members = []
        exclude = exclude or []
        params = [ini_boolean(godmode)]
        if damage_from_player is not None:
            params.append(ini_boolean(damage_from_player))

            if alive_percent is not None:
                params.append(alive_percent)

        params_string = ", ".join(map(str, params))

        for index in range(1, self.count+1):
            if index in exclude:
                continue
            members.append(f'Act_Invulnerable = {self.get_member_name(index)}, {params_string}')

        return SINGLE_DIVIDER.join(members)

    def define_respawn(self, trigger_setrep, objlist=NO_OL):
        self.respawn_defined = True

        if self.system is None:
            raise Exception('System is not defined for ship %s' % self.name)
        if self.slide_x == 0 and self.slide_y == 0 and self.slide_z == 0:
            raise Exception('At least one slide param must be defined for ship %s' % self.name)

        marker = Marker(self.system, self.name)
        pos = list(marker.get_position())
        orient = euler_to_quat(*marker.get_rotate())

        actions = []
        for index in range(1, self.count+1):
            member = self.get_member_name(index)
            spawn_params = [
                self.get_multiple_member_name(index),
                objlist,
                *pos,
                *orient
            ]
            actions.extend([
                '[Trigger]',
                f'nickname = member_respawn_{member}',
                f'Cnd_Destroyed = {member}',
                f'Act_SpawnShip = {", ".join(map(str, spawn_params))}',
                f'Act_ActTrig = {trigger_setrep}',
                'repeatable = true',
            ])

            pos[0] += self.slide_x
            pos[1] += self.slide_y
            pos[2] += self.slide_z

        return SINGLE_DIVIDER.join(actions)

    def turn_respawn_on(self):
        if not self.respawn_defined:
            raise Exception('respawn triggers not defined in mission')

        actions = []
        for index in range(1, self.count+1):
            actions.append(f'Act_ActTrig = member_respawn_{self.get_member_name(index)}')

        return SINGLE_DIVIDER.join(actions)

    def turn_respawn_off(self):
        if not self.respawn_defined:
            raise Exception('respawn triggers not defined in mission')

        actions = []
        for index in range(1, self.count+1):
            actions.append(f'Act_DeActTrig = member_respawn_{self.get_member_name(index)}')

        return SINGLE_DIVIDER.join(actions)


class ShipMember:
    def __init__(self, ship, member_index):
        self.ship: Ship = ship
        self.member_index: int = member_index

    @property
    def name(self):
        """for template"""
        return self.ship.member(index=self.member_index)

    def hide(self):
        return self.ship.destroy_member(member_index=self.member_index, destroy_mode=SILENT)

    def spawn(self, ol=NO_OL):
        return self.ship.spawn_member(member_index=self.member_index, objlist=ol)


class NNObj:
    TITLE = '[NNObjective]'
    NICKNAME_TEMPLATE = 'nickname = {nickname}'
    STATE = 'state = HIDDEN'

    def __init__(self, mission, ru_action, name=None, target=None, towards=False, nag=True, force_jumpgate=False):
        self.mission = mission
        self.ids_name = self.mission.ids.new_name(ru_action)
        self.target = target
        self.target_point = self.get_target_point()
        self.name = f'nn_{name}' if name else self.generate_name()
        self.towards = towards
        self.nag = nag
        self.force_jumpgate = force_jumpgate

    def get_string_id(self):
        return self.ids_name.id

    def get_simple_type(self):
        return f'type = ids, {self.get_string_id()}'

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
            return self.target_point.get_nn_type(self.get_string_id())
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
            str(self.get_string_id()),
            str(self.get_string_id()),
            self.target_point.name,
            self.target_point.system.NAME,
        ]
        params_line = ", ".join(path_params)
        return f'Act_NNPath = {params_line}'


class Script:
    def __init__(self, msn_script):
        self.msn_script = msn_script
        self.used_lines = []

    def get_ether_comm(self, sound):
        self.used_lines.append(
            sound.line.index
        )
        return ETHER_COMM_TEMPLATE.format(
            voice_root=self.msn_script.get_voice_root_for_sound(sound),
            string_id=1,
            line=sound.get_nickname(),
            comm_appearance=sound.line.actor.get_comm_appearance(),
        )

    def lookup_single_sound(self, index) -> Sound:
        for sound in self.msn_script.space.get_sounds():
            if sound.line.index == index:
                return sound

        raise Exception(f'MSN {self.msn_script.MISSION_INDEX}. Comm with index {index} not found')

    def line(self, index: int):
        sound = self.lookup_single_sound(index)
        return self.get_ether_comm(sound)

    def dialog(self, start: int, end: int):
        comms = []
        for sound in self.msn_script.space.get_sounds():
            if sound.line.index >= start and sound.line.index <= end:
                comms.append(self.get_ether_comm(sound))

        if len(comms) == 0:
            raise Exception(f'MSN {self.msn_script.MISSION_INDEX}. Dialog from {start} to {end} is not found in script')

        return SINGLE_DIVIDER.join(comms)

    def ends(self, index, check=True):
        if check and index not in self.used_lines:
            raise Exception(f'MSN {self.msn_script.MISSION_INDEX}. Line {index} isnt used and cant be CommCompleted')
        sound = self.lookup_single_sound(index)
        return f'Cnd_CommComplete = {sound.get_nickname()}'


class Trigger:
    ALLOWED_VIBES = [
        'REP_HOSTILE_MAXIMUM',
        'REP_HOSTILE_THRESHOLD',
        'REP_NEUTRAL',
        'REP_FRIEND_THRESHOLD',
        'REP_FRIEND_MAXIMUM',
    ]

    def new(self, name, dry=False):
        content = [
            TRIGGER,
            f'nickname = {name}',
        ]
        if dry:
            content.append(DRY_RUN)
        return SINGLE_DIVIDER.join(content)

    def next(self, next_name):
        return SINGLE_DIVIDER.join([
            f'Act_ActTrig = {next_name}',
            '',
            TRIGGER,
            f'nickname = {next_name}',
        ])

    def turn(self, trigger):
        return f'Act_ActTrig = {trigger}'

    def off(self, trigger):
        return f'Act_DeActTrig = {trigger}'

    def delay(self, next_name, delay: float):
        return SINGLE_DIVIDER.join([
            f'Act_ActTrig = delay_{next_name}',
            '',
            TRIGGER,
            f'nickname = delay_{next_name}',
            f'Cnd_Timer = {delay}',
            self.turn(next_name),
        ])

    def delay_direct(self, next_name, delay: float):
        return SINGLE_DIVIDER.join([
            f'Act_ActTrig = delay_{next_name}',
            '',
            TRIGGER,
            f'nickname = delay_{next_name}',
            f'Cnd_Timer = {delay}',
        ])

    def vibe_label_ship(self, vibe, label, ship='Player'):
        if vibe not in self.ALLOWED_VIBES:
            raise Exception('unknown vibe %s' % vibe)

        return SINGLE_DIVIDER.join([
            f'Act_SetVibeLblToShip = {label}, {ship}, {vibe}',
            f'Act_SetVibeShipToLbl = {ship}, {label}, {vibe}'
        ])

    def vibe_label(self, vibe, label1, label2):
        if vibe not in self.ALLOWED_VIBES:
            raise Exception('unknown vibe %s' % vibe)

        return SINGLE_DIVIDER.join([
            f'Act_SetVibeLbl = {label1}, {label2}, {vibe}',
            f'Act_SetVibeLbl = {label2}, {label1}, {vibe}'
        ])

    def vibe_ship(self, vibe, ship1, ship2='Player', single=False):
        if vibe not in self.ALLOWED_VIBES:
            raise Exception('unknown vibe %s' % vibe)
        actions = [
            f'Act_SetVibe = {ship1}, {ship2}, {vibe}',
        ]
        if not single:
            actions.append(
                f'Act_SetVibe = {ship2}, {ship1}, {vibe}'
            )

        return SINGLE_DIVIDER.join(actions)


class Capital(DefinedStaticMixin):

    def __init__(self, mission, alias, npc_ship_arch, ru_name, faction=None, labels=None):
        self.mission = mission
        self.alias = alias
        self.npc_ship_arch = npc_ship_arch
        self.ru_name = ru_name
        self.ids_name = self.mission.ids.new_name(self.ru_name)
        self.faction = faction or DEFAULT_AFFILIATION
        self.labels = labels or []

    def get_name(self):
        return self.alias

    def get_definition(self):
        ship = [
            '[NPC]',
            f'nickname = npc_{self.name}',
            f'affiliation = {self.faction}',
            f'npc_ship_arch = {self.npc_ship_arch}',
            f'individual_name = {self.ids_name.id}'
        ]

        ship.extend([
            '',
            '[MsnShip]',
            f'nickname = {self.name}',
            f'NPC = npc_{self.name}',
        ])
        for label in self.labels:
            ship.append(f'label = {label}')
        return SINGLE_DIVIDER.join(ship)


class Cond:

    def destroyed(self, name, count=None, kind=None):
        params = [name]
        if count:
            params.append(str(count))
        if kind:
            params.append(kind)
        return f'Cnd_Destroyed = {", ".join(params)}'


class Direct:
    def __init__(self, mission, systems):
        self.mission = mission
        self.systems = systems
        self.sys_map = {sys.NAME: sys for sys in systems}
        self.trigger = Trigger()
        self.trigger_groups = {}
        self.save_states: dict = {state.get_code(): state for state in self.mission.get_save_states()}

    def save(self, code):
        state = self.save_states.get(code)
        if not state:
            raise Exception(f'unknown save state {code}')
        trigger = f'save_state_{code}'
        content = [
            f'Act_Save = {trigger}, {state.get_id()}',
            '',
            '[Trigger]',
            f'nickname = {trigger}',
            'Cnd_SpaceEnter = no_params',
            'Act_RevertCam = no_params',
            f'Act_ActTrig = init_the_{trigger}',
            '',
            '[Trigger]',
            f'nickname = init_the_{trigger}',
            'Cnd_Timer = 0.3',
        ]
        return SINGLE_DIVIDER.join(content)

    def add_trigger_to_group(self, group, trigger_name):
        if group not in self.trigger_groups:
            self.trigger_groups[group] = []

        self.trigger_groups[group].append(trigger_name)

    def get_point(self, system_name, alias):
        return Point(self.mission, self.sys_map[system_name], alias)

    def pos(self, system_name, alias):
        return self.get_point(system_name, alias).pos

    def orient(self, system_name, alias):
        return self.get_point(system_name, alias).orient

    def pos_orient(self, system_name, alias):
        return self.get_point(system_name, alias).pos_orient

    def inside_pos(self, system_name, alias, range, obj='Player'):
        return self.get_point(system_name, alias).inside_pos(range, obj)

    def outside_pos(self, system_name, alias, range, obj='Player'):
        return self.get_point(system_name, alias).outside_pos(range, obj)

    def inside_sphere(self, system_name, alias, obj='Player'):
        return self.get_point(system_name, alias).inside_sphere(obj)

    def outside_sphere(self, system_name, alias, obj='Player'):
        return self.get_point(system_name, alias).outside_sphere(obj)

    def next_cond_inside_pos(self, system_name, alias, range, obj='Player', group=None):
        trigger_name = f'near_{alias}'
        if group is not None:
            self.add_trigger_to_group(group, trigger_name)
        return SINGLE_DIVIDER.join([
            self.trigger.next(trigger_name),
            self.get_point(system_name, alias).inside_pos(range, obj)
        ])

    def ol_goto(self, system_name, alias, ol_name, goto, near: int = 100, avoidance: bool | None=None):
        point = self.get_point(system_name, alias)
        objlist = [
            '[ObjList]',
            f'nickname = {ol_name}',
        ]
        if avoidance:
            objlist.append(f'avoidance = {ini_boolean(avoidance)}')
        objlist.append(point.goto_vec(goto, near))
        return SINGLE_DIVIDER.join(objlist)

    def spawn_capital(self, system_name, capital: Capital, point=None, ol=None,
                      invulnerable=True, damage_from_player=True):
        point = self.get_point(system_name, point if point else capital.name)
        actions = [
            f'Act_SpawnShip = {capital.name}, {ol or "no_ol"}, {point.pos_orient}'
        ]
        if invulnerable:
            actions.append(capital.invulnerable(damage_from_player=damage_from_player))
        return SINGLE_DIVIDER.join(actions)

    def spawn_capital_group(self, system_name, group_name, ol=None,
                            invulnerable=True, damage_from_player=True):
        group = self.mission.get_capital_group(group_name)
        actions = []
        for cap in group:
            actions.append(self.spawn_capital(system_name, cap, point=None, ol=ol,
                                              invulnerable=invulnerable,
                                              damage_from_player=damage_from_player))
        return SINGLE_DIVIDER.join(actions)

    def fuse_capital_group(self, group_name, fuse):
        group = self.mission.get_capital_group(group_name)
        actions = []
        for cap in group:
            actions.append(cap.fuse(fuse))
        return SINGLE_DIVIDER.join(actions)

    def hide_capital_group(self, group_name):
        group = self.mission.get_capital_group(group_name)
        actions = []
        for cap in group:
            actions.append(cap.hide())
        return SINGLE_DIVIDER.join(actions)

    def invulnerable_capital_group(self, group_name, godmode, damage_from_player):
        group = self.mission.get_capital_group(group_name)
        actions = []
        for cap in group:
            actions.append(cap.invulnerable(godmode=godmode, damage_from_player=damage_from_player))
        return SINGLE_DIVIDER.join(actions)

    def mark_capital_group(self, group_name):
        group = self.mission.get_capital_group(group_name)
        actions = []
        for cap in group:
            actions.append(cap.mark())
        return SINGLE_DIVIDER.join(actions)

    def spawn_ship(self, system_name, alias, ship: Ship, ol=NO_OL):
        point = self.get_point(system_name, alias)
        return ship.spawn(ol, pos=point.pos_orient)

    def spawn_ship_member(self, system_name, alias, ship_member: ShipMember, ol=NO_OL):
        point = self.get_point(system_name, alias)
        return f'{ship_member.spawn(ol)}, {point.pos_orient}'

    def deactivate_trigger_group(self, group):
        if group not in self.trigger_groups:
            raise Exception(f'no trigger group {group}')

        return SINGLE_DIVIDER.join(
            [ f'Act_DeActTrig = {trig}' for trig in self.trigger_groups[group]]
        )

    def new_string_id(self, ru_name):
        return self.mission.ids.new_name(ru_name).id


class Patrol:

    def __init__(self, direct, trigger):
        self.direct: Direct = direct
        self.trigger: Trigger = trigger
        self.line_patrols = {}

    def get_line_patrol_trigger_name(self, patroller):
        return f'line_patrol_of_{patroller}'

    def define_line_patrol(self, system_name,
                           patroller: ShipMember,
                           init_point: str,
                           target_point: str,
                           restart_point: str,
                           target_range:int = 500,
                           near_range: int = 100,
                           mode: str = GOTO_CRUISE):
        patroller_name = patroller.name
        main_patrol_name = self.get_line_patrol_trigger_name(patroller_name)
        objlist_name = f'ol_{patroller_name}_to_the_end'

        if patroller_name in self.line_patrols.keys():
            raise Exception(f'Patrol {patroller_name} is already defined')

        content = [
            self.direct.ol_goto(system_name, target_point, objlist_name, mode, near=near_range),
            '',
            self.trigger.new(main_patrol_name),
            DRY_RUN,
            self.direct.spawn_ship_member(
                system_name,
                alias=init_point,
                ship_member=patroller,
                ol=objlist_name,
            ),
            self.trigger.next(f'{main_patrol_name}_goto'),
            self.direct.inside_pos(system_name, target_point, range=target_range, obj=patroller_name),
            f'Act_GiveObjList = {patroller_name}, force_stop',
            self.trigger.delay_direct(f'{main_patrol_name}_done', 1),

            f'Act_RelocateShip = {patroller_name}, {self.direct.pos_orient(system_name, restart_point)}',
            self.trigger.delay_direct(f'{main_patrol_name}_restart', 1),
            f'Act_GiveObjList = {patroller_name}, {objlist_name}',
        ]

        self.line_patrols[main_patrol_name] = patroller

        return SINGLE_DIVIDER.join(content)

    def start_line_patrol(self, patroller: ShipMember):
        main_patrol_name = self.get_line_patrol_trigger_name(patroller.name)

        if main_patrol_name not in self.line_patrols.keys():
            raise Exception(f'Patrol {main_patrol_name} is not defined')

        return f'Act_ActTrig = {main_patrol_name}'

    def stop_line_patrol(self, patroller: ShipMember):
        main_patrol_name = self.get_line_patrol_trigger_name(patroller.name)

        if main_patrol_name not in self.line_patrols.keys():
            raise Exception(f'Patrol {main_patrol_name} is not defined')

        triggers = [
            main_patrol_name,
            f'{main_patrol_name}_goto',
            f'{main_patrol_name}_done',
            f'{main_patrol_name}_restart',
        ]
        deactivators = SINGLE_DIVIDER.join([f'Act_DeActTrig = {t}' for t in triggers])
        hide_ship = patroller.hide()

        return SINGLE_DIVIDER.join([deactivators, hide_ship])

    def stop_all_line_patrols(self):
        actions = []
        for patroller in self.line_patrols.values():
            actions.append(
                self.stop_line_patrol(patroller=patroller)
            )
        return SINGLE_DIVIDER.join(actions)


class Rtc:
    def __init__(self, mission):
        self.mission = mission
        self.rtc = self.mission.RTC

    def add(self, rtc):
        if rtc not in self.rtc:
            raise Exception(f'Mission {self.mission.FILE} have no rtc {rtc}')

        return f'Act_AddRTC = missions\\{self.mission.FOLDER}\\{rtc}.ini'

    def remove(self, rtc):
        if rtc not in self.rtc:
            raise Exception(f'Mission {self.mission.FILE} have no rtc {rtc}')

        return f'Act_RemoveRTC = missions\\{self.mission.FOLDER}\\{rtc}.ini'

    def done(self, rtc):
        if rtc not in self.rtc:
            raise Exception(f'Mission {self.mission.FILE} have no rtc {rtc}')

        return f'Cnd_RTCDone = missions\\{self.mission.FOLDER}\\{rtc}.ini'


class Offer:
    def __init__(self, mission):
        self.mission = mission

    def init(self):
        return SINGLE_DIVIDER.join([
            f'Act_SetTitle = {self.mission.get_init_title()}',
            f'Act_SetOffer = {self.mission.get_init_offer()}',
        ])

    def accept(self):
        return SINGLE_DIVIDER.join([
            f'Act_SetTitle = {self.mission.get_accept_title()}',
            f'Act_SetOffer = {self.mission.get_accept_offer()}',
        ])


class SaveState:

    def __init__(self, mission, code, ru_name):
        self.mission = mission
        self.code = code
        self.ru_name = ru_name
        self.ids_name = self.mission.ids.new_name(self.ru_name)

    def get_code(self):
        return self.code

    def get_id(self):
        return self.ids_name.id
