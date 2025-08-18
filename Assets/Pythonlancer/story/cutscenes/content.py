from story import math


ENTITY_TEMPLATE_FOLDER = 'cutscenes/entity/'
EVENT_TEMPLATE_FOLDER = 'cutscenes/event/'

OFFSCREEN = 'offscreen'

TARGET_ROOT = 'ROOT'
TARGET_PART = 'PART'
TARGET_HARDPOINT = 'HARDPOINT'

TARGET_TYPES = [TARGET_ROOT, TARGET_PART, TARGET_HARDPOINT]

LIT_DYNAMIC = 'LIT_DYNAMIC'
LIT_AMBIENT = 'LIT_AMBIENT'

L_DIRECT = 'L_DIRECT'
L_POINT = 'L_POINT'
L_SPOT = 'L_SPOT'
LIGHT_TYPES = [L_DIRECT, L_POINT, L_SPOT]

BODY_HEAD = 'Body_Head'
EYE_IK = 'Eye IK Left'

MAIN = 'main'
BG = 'bg'
DEFAULT_GROUP = 'default_group'
BG_GROUP = 'bg_group'

IDLE = 'idle'

MALE_ANIMS = {
    IDLE: 'Sc_MLBODY_STND_IDLE_000LV_xa_04',
}

FEMALE_ANIMS = {
    IDLE: 'Sc_FMBODY_STND_IDLE_000LV_xa_05',
}

X_AXIS = 'X_AXIS'
Y_AXIS = 'Y_AXIS'
Z_AXIS = 'Z_AXIS'

NEG_X_AXIS = 'NEG_X_AXIS'
NEG_Y_AXIS = 'NEG_Y_AXIS'
NEG_Z_AXIS = 'NEG_Z_AXIS'

HEAD_SIT_FEMALE = 1.25  # 1.1 ??
HEAD_SIT_MALE = 1.25
HEAD_STAND_FEMALE = 1.55
HEAD_STAND_MALE = 1.65

SOURCE_BLENDER = 'blender'
SOURCE_PYTHONLANCER = 'pythonlancer'


class Point:
    # WARNING! temporary only for positions!!
    def __init__(self, name, position, source, rotate=None):  # , orientation, rotate
        self.name = name
        self.source = source
        if self.source == SOURCE_BLENDER:
            self.position = [position[0], position[2], -position[1]]
        else:
            self.position = position
        # self.orientation = [orientation[3], orientation[0], orientation[1], -orientation[2]]  # quaternion
        # deg_euler = math.radians_to_degrees(*rotate)
        # self.rotate = [deg_euler[0], deg_euler[1], deg_euler[2]]
        # if len(self.orientation) != 4:
        #     raise Exception(f'Point {name} have wrong quaternion for orientation')
        self.rotate = rotate if rotate else [0, 0, 0]


    @property
    def pos(self):
        return '{0:.2f}, {1:.2f}, {2:.2f}'.format(*self.position)

    @property
    def orient(self):
        raise NotImplementedError
        # return '{0:.2f}, {1:.2f}, {2:.2f}, {3:.2f}'.format(*math.euler_to_quat(*self.rotate))

    @property
    def matrix(self):
        mx = math.euler_to_matrix(*self.rotate)
        return '''
            {{ {0:.7f},{1:.7f},{2:.7f} }},
            {{ {3:.7f},{4:.7f},{5:.7f} }},
            {{ {6:.7f},{7:.7f},{8:.7f} }}
        '''.format(
            mx[0][0], mx[0][1], mx[0][2],
            mx[1][0], mx[1][1], mx[1][2],
            mx[2][0], mx[2][1], mx[2][2],
        )


class Group:
    def __init__(self, root, name, group_type=DEFAULT_GROUP, time=0):
        self.root = root
        self.name = name
        self.time = time
        self.group_type = group_type

    def add_event(self, event, time_append=0, time_delay=0):
        time = self.time + time_delay
        self.root.add_event(time, event)
        self.time += time_append

    def get_time(self):
        return self.time

    def get_name(self):
        return self.name

    def append_time(self, time):
        self.time += time

    def is_default(self):
        return self.group_type == DEFAULT_GROUP

    def get_type(self):
        return self.group_type


### EVENTS


class Event:
    TEMPLATE = None

    def __init__(self, root, group=MAIN, time_append=0, time_delay=0):
        self.root = root
        self.group = self.root.get_group(group)
        self.group.add_event(self, time_append, time_delay)

    def get_params(self):
        raise NotImplementedError

    def get_template(self):
        if not self.TEMPLATE:
            raise Exception(f'Event item {self} have no template')
        return EVENT_TEMPLATE_FOLDER + f'{self.TEMPLATE}.lua'

    def get_thorn(self, time):
        params = self.get_params()
        params['time'] = time
        return self.root.tpl_manager.get_result(self.get_template(), params)


class LookAtEvent(Event):
    TEMPLATE = 'look_at'

    def __init__(self, point, focus, duration, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.point = point
        self.focus = focus
        self.duration = duration

    def get_params(self):
        return {
            'point': self.point,
            'focus': self.focus,
            'duration': self.duration,
        }


class SetCameraEvent(Event):
    TEMPLATE = 'set_camera'

    def __init__(self, camera_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.camera_name = camera_name

    def get_params(self):
        return {
            'name': self.camera_name,
        }


class SoundEvent(Event):
    TEMPLATE = 'sound'

    def __init__(self, sound_name, duration=20, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sound_name = sound_name
        self.duration = duration

    def get_params(self):
        return {
            'sound': self.sound_name,
            'duration': self.duration,
        }


class MoveEvent(Event):
    TEMPLATE = 'move_linear'
    ADJUST_POS = 'pos = {0, 0, 0}'
    ADJUST_ORIENT = 'q_orient = {1, 0, 0, 0}'
    ADJUST_ORIENT_TEMPLATE = 'q_orient = {{ {quat} }}'

    def __init__(self, object_name, target_name, duration, smooth=True,
                 adjust_pos=True, adjust_orient=True,
                 rotate_y=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.object_name = object_name
        self.target_name = target_name
        self.duration = duration
        self.smooth = smooth
        self.adjust_orient = adjust_orient
        self.adjust_pos = adjust_pos
        self.rotate = (0, rotate_y, 0)

    def set_duration(self, duration):
        self.duration = duration

    def get_move_rules(self):
        rules = []
        if self.adjust_pos:
            rules.append(self.ADJUST_POS)

        if self.adjust_orient:
            rules.append(
                self.ADJUST_ORIENT_TEMPLATE.format(
                    quat='{0:.2f}, {1:.2f}, {2:.2f}, {3:.2f}'.format(*math.euler_to_quat(*self.rotate)))
            )
        if len(rules) == 0:
            raise Exception(f'MoveEvent for {self.object_name} have no move rules: it should adjust pos or/and orient')

        return ', '.join(rules)

    def get_params(self):
        return {
            'object_name': self.object_name,
            'target_name': self.target_name,
            'duration': self.duration,
            'smooth': self.smooth,
            'move_rules': self.get_move_rules(),
        }


class MoveFastEvent(MoveEvent):
    """shortcut with zero duration"""
    def __init__(self, *args, **kwargs):
        kwargs['smooth'] = False
        kwargs['duration'] = 0
        kwargs['adjust_pos'] = True
        super().__init__(*args, **kwargs)


class MoveOffscreenEvent(MoveEvent):
    """shortcut for offscreen"""
    def __init__(self, *args, **kwargs):
        kwargs['smooth'] = False
        kwargs['duration'] = 0
        kwargs['target_name'] = OFFSCREEN
        kwargs['adjust_pos'] = True
        super().__init__(*args, **kwargs)


class RotateAxisEvent(Event):
    TEMPLATE = 'rotate_axis'
    AXIS = 'Y_AXIS'

    def __init__(self, object_name, angle, duration, smooth=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.object_name = object_name
        self.angle = angle
        self.duration = duration
        self.smooth = smooth

    def get_params(self):
        return {
            'object_name': self.object_name,
            'angle': self.angle,
            'duration': self.duration,
            'smooth': self.smooth,
            'axis': self.AXIS,
        }


class IkEvent(Event):
    TEMPLATE = 'ik'

    def __init__(self, char_name, target_name, duration, end_effector, transition_duration=1,
                 target_part='', up=NEG_Y_AXIS, front=Z_AXIS, target_type=TARGET_ROOT, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.char_name = char_name
        self.target_name = target_name
        self.duration = duration
        self.end_effector = end_effector
        self.transition_duration = transition_duration
        self.target_part = target_part
        self.target_type = target_type
        self.up = up
        self.front = front

        if self.target_type not in TARGET_TYPES:
            raise Exception(f'IK for {self.char_name} has invalid target_type')

        if self.target_type != TARGET_ROOT and self.target_part == '':
            raise Exception(f'IK for {self.char_name} requires defined target_part')

    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        self.duration = duration

    def get_params(self):
        return {
            'char_name': self.char_name,
            'target_name': self.target_name,
            'duration': self.duration,
            'transition_duration': self.transition_duration,
            'end_effector': self.end_effector,
            'target_part': self.target_part,
            'target_type': self.target_type,
            'up': self.up,
            'front': self.front,
        }


class NeckIkEvent(IkEvent):
    """shortcut for generic neck ik"""
    def __init__(self, *args, **kwargs):
        kwargs['end_effector'] = BODY_HEAD
        super().__init__(*args, **kwargs)


class Char2CharNeckIkEvent(NeckIkEvent):
    """shortcut for simple next char neck ik"""
    def __init__(self, *args, **kwargs):
        kwargs['target_part'] = BODY_HEAD
        kwargs['target_type'] = TARGET_PART
        super().__init__(*args, **kwargs)


class EyeIkEvent(IkEvent):
    """shortcut for generic neck ik"""
    def __init__(self, *args, **kwargs):
        kwargs['end_effector'] = EYE_IK
        super().__init__(*args, **kwargs)


class FloorHeightEvent(Event):
    TEMPLATE = 'floor_height'

    def __init__(self, char_name, floor_height, duration=0.001, smooth=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.char_name = char_name
        self.floor_height = floor_height
        self.duration = duration
        self.smooth = smooth

    def make_immediately(self):
        self.duration = 0
        self.smooth = False

    def get_params(self):
        return {
            'char': self.char_name,
            'floor_height': self.floor_height,
            'duration': self.duration,
            'smooth': self.smooth,
        }


class MotionEvent(Event):
    TEMPLATE = 'motion'

    def __init__(self, object_name, anim, duration, time_scale=1, start_time=0,
                 loop=False, trans_time=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.object_name = object_name
        self.anim = anim
        self.duration = duration
        self.time_scale = time_scale
        self.start_time = start_time
        self.loop = loop
        self.trans_time = trans_time

    def get_params(self):
        return {
            'object_name': self.object_name,
            'anim': self.anim,
            'duration': self.duration,
            'time_scale': self.time_scale,
            'start_time': self.start_time,
            'loop': self.loop,
            'trans_time': self.trans_time,
        }


class AnimEvent(Event):
    TEMPLATE = 'anim'

    def __init__(self, object_name, anim, duration, time_scale=1, start_time=0,
                 loop=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.object_name = object_name
        self.anim = anim
        self.duration = duration
        self.time_scale = time_scale
        self.start_time = start_time
        self.loop = loop

    def get_params(self):
        return {
            'object_name': self.object_name,
            'anim': self.anim,
            'duration': self.duration,
            'time_scale': self.time_scale,
            'start_time': self.start_time,
            'loop': self.loop,
        }


class FacialEvent(Event):
    TEMPLATE = 'facial'

    def __init__(self, object_name, motion, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.object_name = object_name
        self.motion = motion

    def get_params(self):
        return {
            'object_name': self.object_name,
            'motion': self.motion,
        }


class LightAnimEvent(Event):
    TEMPLATE = 'light_anim'

    def __init__(self, object_name, duration, smooth=False,
                 diffuse=None, ambient=None, on=None, lt_range=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.object_name = object_name
        self.duration = duration
        self.smooth = smooth
        self.diffuse = diffuse
        self.ambient = ambient
        self.on = on
        self.lt_range = lt_range

    def get_actions(self):
        actions = []

        if self.diffuse is not None:
            if len(self.diffuse) != 3:
                raise Exception(f'Light anim for {self.object_name} have wrong diffuse')

            actions.append(f' diffuse = {{ {self.diffuse[0]}, {self.diffuse[1]}, {self.diffuse[2]} }}')

        if self.ambient is not None:
            if len(self.ambient) != 3:
                raise Exception(f'Light anim for {self.object_name} have wrong ambient')

            actions.append(f' ambient = {{ {self.ambient[0]}, {self.ambient[1]}, {self.ambient[2]} }}')

        if self.on is not None:
            actions.append(f'on = {"Y" if self.on else "N"}')

        if self.lt_range is not None:
            actions.append(f'range = {self.lt_range}')

        if len(actions) == 0:
            raise Exception(f'Light anim for {self.object_name} has no any action')

        return ', '.join(actions)

    def get_params(self):
        return {
            'name': self.object_name,
            'duration': self.duration,
            'smooth': self.smooth,
            'light_changes': self.get_actions(),
        }


class StartAlchemyEvent(Event):
    TEMPLATE = 'start_alchemy'

    def __init__(self, object_name, duration, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.object_name = object_name
        self.duration = duration

    def get_params(self):
        return {
            'name': self.object_name,
            'duration': self.duration,
        }


class ConnectHardpointEvent(Event):
    TEMPLATE = 'connect_hardpoint'

    def __init__(self, target_name, parent_name, duration,
                 target_hardpoint, parent_hardpoint, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_name = target_name
        self.parent_name = parent_name
        self.duration = duration
        self.target_hardpoint = target_hardpoint
        self.parent_hardpoint = parent_hardpoint

    def get_params(self):
        return {
            'target_name': self.target_name,
            'parent_name': self.parent_name,
            'duration': self.duration,
            'target_hardpoint': self.target_hardpoint,
            'parent_hardpoint': self.parent_hardpoint,
        }

    def set_duration(self, duration):
        self.duration = duration


class AttachEvent(Event):
    TEMPLATE = 'attach'

    def __init__(self, target_name, parent_name, duration,
                 target_part, target_type, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_name = target_name
        self.parent_name = parent_name
        self.duration = duration
        self.target_part = target_part
        self.target_type = target_type

        if self.target_type not in TARGET_TYPES:
            raise Exception(f'Attach event for {self.parent_name} has invalid target_type')

        if self.target_type != TARGET_ROOT and self.target_part == '':
            raise Exception(f'Attach event for {self.parent_name} requires defined target_part')

    def get_params(self):
        return {
            'target_name': self.target_name,
            'parent_name': self.parent_name,
            'duration': self.duration,
            'target_part': self.target_part,
            'target_type': self.target_type,
        }

    def set_duration(self, duration):
        self.duration = duration


class StartSoundEvent(Event):
    TEMPLATE = 'start_sound'

    def __init__(self, sound_name, duration, loop=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sound_name = sound_name
        self.duration = duration
        self.loop = loop

    def get_params(self):
        return {
            'sound': self.sound_name,
            'duration': self.duration,
            'loop': self.loop,
        }

    def set_duration(self, duration):
        self.duration = duration


class AudioAnimEvent(Event):
    TEMPLATE = 'audio_anim'

    def __init__(self, sound_name, duration, attenuation, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sound_name = sound_name
        self.duration = duration
        self.attenuation = attenuation

    def get_params(self):
        return {
            'sound': self.sound_name,
            'duration': self.duration,
            'attenuation': self.attenuation,
        }


### ENTITIES


class Entity:
    TEMPLATE_ROOT = ENTITY_TEMPLATE_FOLDER
    TEMPLATE = None

    def __init__(self, root, name):
        self.root = root
        self.name = name
        self.root.add_entity(self)

    def get_params(self):
        raise NotImplementedError

    def get_template(self):
        if not self.TEMPLATE:
            raise Exception(f'Entity item {self} have no template')
        return ENTITY_TEMPLATE_FOLDER + f'{self.TEMPLATE}.lua'

    def get_thorn(self):
        return self.root.tpl_manager.get_result(self.get_template(), self.get_params())


class Marker(Entity):
    TEMPLATE = 'marker'

    def __init__(self, point_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.point_name = point_name
        self.point = self.root.get_point(self.point_name)

    def get_params(self):
        return {
            'name': self.name,
            'point': self.point,
        }


class Compound(Entity):
    FORCE_POS = None
    FORCE_MATRIX = None

    def __init__(self, light_group, init_point, rotate_y=0,
                 use_ambient=False, matrix_scale=1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.light_group = light_group
        self.init_point = init_point
        self.point = self.root.get_point(self.init_point)
        self.rotate_y = rotate_y
        self.use_ambient = use_ambient
        self.matrix_scale = matrix_scale

    def get_init_matrix(self):
        if self.FORCE_MATRIX:
            mx = self.FORCE_MATRIX
        else:
            rotate = (
                [0, self.rotate_y, 0]
                if self.rotate_y != 0
                else self.point.rotate
            )
            mx = math.euler_to_matrix(*rotate)

        return '''
            {{ {0:.7f},{1:.7f},{2:.7f} }}, 
            {{ {3:.7f},{4:.7f},{5:.7f} }},
            {{ {6:.7f},{7:.7f},{8:.7f} }}
        '''.format(
            mx[0][0]*self.matrix_scale, mx[0][1]*self.matrix_scale, mx[0][2]*self.matrix_scale,
            mx[1][0]*self.matrix_scale, mx[1][1]*self.matrix_scale, mx[1][2]*self.matrix_scale,
            mx[2][0]*self.matrix_scale, mx[2][1]*self.matrix_scale, mx[2][2]*self.matrix_scale,
        )

    def get_flags(self):
        flags = [LIT_DYNAMIC]
        if self.use_ambient:
            flags.append(LIT_AMBIENT)
        return ' + '.join(flags)

    def get_compound_template_name(self):
        raise NotImplementedError

    def get_params(self):
        return {
            'name': self.name,
            'template_name': self.get_compound_template_name(),
            'light_group': self.light_group,
            'init_pos': '{0}, {1}, {2}'.format(*self.FORCE_POS) if self.FORCE_POS else self.point.pos,
            'init_matrix': self.get_init_matrix(),
            'light_flags': self.get_flags(),
        }

    def anim(self, group, anim, duration=10, **kwargs):
        return MotionEvent(root=self.root, group=group,
                           object_name=self.name, anim=anim,
                           duration=duration,
                           **kwargs)


class Prop(Compound):
    COMPOUND_TEMPLATE_NAME = None
    TEMPLATE = 'prop'

    def get_compound_template_name(self):
        return self.COMPOUND_TEMPLATE_NAME


class Glass(Prop):
    COMPOUND_TEMPLATE_NAME = 'glass'


class BottleWine(Prop):
    COMPOUND_TEMPLATE_NAME = 'bottle_wine_3'


class Character(Compound):
    TEMPLATE = 'character'

    def __init__(self, actor, floor_height=0, extra_ik_markers=None,
                 ik_start_point=None, *args, **kwargs):
        self.actor = actor
        name = f'Char_{self.actor.NAME}'
        super().__init__(name=name, *args, **kwargs)
        self.floor_height = floor_height
        self.animations = FEMALE_ANIMS if self.actor.is_female() else MALE_ANIMS
        self.head_ik_name = self.get_ik_marker('head')
        self.eye_ik_name = self.get_ik_marker('eye')
        self.ik_start_point = ik_start_point
        self.extra_ik_markers = extra_ik_markers if extra_ik_markers else []
        self.init_char_points()

    def get_ik_marker(self, ik_name):
        return f'char_ik_{self.name}_{ik_name}_ik'

    def init_char_points(self):
        ik_position = [0, 0, 0]
        if self.ik_start_point:
            raise NotImplementedError
            # ik_position = self.root.get_point(self.ik_start_point).position

        temp_ik_point_name = f'ikpoint_{self.name}'
        self.root.add_point(
            name=temp_ik_point_name,
            position=ik_position,
            source=SOURCE_PYTHONLANCER,
        )

        Marker(
            root=self.root,
            name=self.head_ik_name,
            point_name=temp_ik_point_name
        )

        Marker(
            root=self.root,
            name=self.eye_ik_name,
            point_name=temp_ik_point_name
        )

        for ik_name in self.extra_ik_markers:
            Marker(
                root=self.root,
                name=self.get_ik_marker(ik_name),
                point_name=temp_ik_point_name
            )


    def move_head_ik(self, group, target_name, immediately=False, **kwargs):
        event_class = MoveFastEvent if immediately else MoveEvent
        event_class(root=self.root, group=group,
                    object_name=self.head_ik_name, target_name=target_name,
                    **kwargs)

    def move_eye_ik(self, group, target_name, immediately=False, **kwargs):
        event_class = MoveFastEvent if immediately else MoveEvent
        event_class(root=self.root, group=group,
                   object_name=self.eye_ik_name, target_name=target_name,
                   **kwargs)

    def move_ik(self, group, ik_marker, target_name, immediately=False, **kwargs):
        event_class = MoveFastEvent if immediately else MoveEvent
        event_class(root=self.root, group=group,
                   object_name=self.get_ik_marker(ik_marker), target_name=target_name,
                   **kwargs)

    def start_head_ik(self, group, **kwargs):
        return NeckIkEvent(root=self.root, group=group, char_name=self.name,
                           target_name=self.head_ik_name,
                           **kwargs)

    def start_eye_ik(self, group, **kwargs):
        return EyeIkEvent(root=self.root, group=group, char_name=self.name,
                          target_name=self.eye_ik_name,
                          **kwargs)

    def start_ik(self, group, ik_marker, **kwargs):
        return IkEvent(root=self.root, group=group, char_name=self.name,
                       target_name=self.get_ik_marker(ik_marker),
                       **kwargs)


    def get_char_marker(self, point_name, y_offset):
        original_pos = self.root.get_point(point_name).position
        marker_name = f'charpoint_{point_name}'
        temp_point_name = f'init_{marker_name}'
        self.root.add_point(
            name=temp_point_name,
            position=[original_pos[0], y_offset, original_pos[2]],
            source=SOURCE_PYTHONLANCER,
        )
        Marker(
            root=self.root,
            name=marker_name,
            point_name=temp_point_name
        )
        return marker_name

    def get_stand_marker(self, point_name, floor_height=0):
        y_offset = HEAD_STAND_FEMALE if self.actor.is_female() else HEAD_STAND_MALE
        return self.get_char_marker(point_name, y_offset+floor_height)

    def get_sit_marker(self, point_name, floor_height=0):
        y_offset = HEAD_SIT_FEMALE if self.actor.is_female() else HEAD_SIT_MALE
        return self.get_char_marker(point_name, y_offset+floor_height)

    def get_compound_template_name(self):
        return self.actor.CUTSCENE_APPEARANCE

    def get_params(self):
        params = super().get_params()
        params['actor'] = self.actor.get_game_actor()
        params['floor_height'] = self.floor_height
        return params

    def motion(self, group, anim, duration=10, repeat=1, **kwargs):
        if self.actor.is_male() and 'fmbody' in anim.lower():
            raise Exception(f'{anim} has wrong gender for {self.name}')
        if self.actor.is_female() and 'mlbody' in anim.lower():
            raise Exception(f'{anim} has wrong gender for {self.name}')

        if repeat > 1 and kwargs.get('loop'):
            raise Exception('cannot repeat loop motion event')

        for i in range(1, repeat+1):
            MotionEvent(root=self.root, group=group,
                        object_name=self.name, anim=anim,
                        duration=duration,
                        **kwargs)

    def idle(self, group, duration=10, **kwargs):
        animation = self.animations[IDLE]
        MotionEvent(root=self.root, group=group,
                    object_name=self.name, anim=animation,
                    duration=duration,
                    **kwargs)

    def facial(self, group, index, append=True, extra_delay=0.3):
        sound = self.root.lookup_single_sound(index)
        if self.actor != sound.line.actor:
            raise Exception(f'Sound {index} is belong to actor {sound.line.actor}. Cannot run by {self.actor}')

        meta = self.root.lookup_sound_meta(sound)
        if len(meta) == 0:
            raise Exception(f'Empty meta for sound {index} !')

        lip_group = f'motion_{index}'
        self.root.clone_group(lip_group, original=group)

        for lip in meta:
            FacialEvent(root=self.root, group=lip_group,
                        object_name=self.name, motion=lip.get_props(),
                        time_delay=lip.get_delay())

        SoundEvent(root=self.root, group=group, sound_name=sound.get_nickname(),
                   time_append=sound.get_duration()+extra_delay if append else 0)


class Camera(Marker):
    def set(self, group, **kwargs):
        SetCameraEvent(root=self.root, group=group, camera_name=self.name, **kwargs)


class StaticCamera(Camera):
    TEMPLATE = 'camera'

    def __init__(self, fov, *args, **kwargs):
        super().__init__(point_name=kwargs['name'], *args, **kwargs)
        self.fov = fov

    def get_params(self):
        return {
            'name': self.name,
            'point': self.point,
            'fov': self.fov,
        }


class LookAtCamera(Camera):
    TEMPLATE = 'camera'

    def __init__(self, fov, look_duration=1000, *args, **kwargs):
        super().__init__(point_name=kwargs['name'], *args, **kwargs)
        self.fov = fov
        self.focus_name = f'{self.name}_focus'
        self.focus = self.root.get_automarker(self.focus_name)
        self.look_at = LookAtEvent(
            root=self.root, group=BG,
            point=self.point, focus=self.focus,
            duration=look_duration,
        )

    def get_params(self):
        return {
            'name': self.name,
            'point': self.point,
            'fov': self.fov,
        }

    def move_cam(self, group, index, duration, time_delay=0, time_append=0, smooth=True):
        target = f'{self.name}{index}'
        target_obj = self.root.get_automarker(target)
        return MoveEvent(root=self.root, group=group,
                         object_name=self.name, target_name=target_obj.name,
                         duration=duration, smooth=smooth,
                         time_delay=time_delay, time_append=time_append)

    def move_focus(self, group, index, duration, time_delay=0, time_append=0, smooth=True):
        target = f'{self.focus_name}{index}'
        target_obj = self.root.get_automarker(target)
        return MoveEvent(root=self.root, group=group,
                         object_name=self.focus.name, target_name=target_obj.name,
                         duration=duration, smooth=smooth,
                         time_delay=time_delay, time_append=time_append)


class Sound(Entity):
    TEMPLATE = 'sound'

    def __init__(self, sound, attenuation, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sound = sound
        self.attenuation = attenuation

    def get_params(self):
        return {
            'name': self.name,
            'sound': self.sound,
            'attenuation': self.attenuation,
        }

    def start(self, group, duration, loop=False, **kwargs):
        return StartSoundEvent(root=self.root, group=group, sound_name=self.name,
                               duration=duration, loop=loop, **kwargs)

    def change_attenuation(self, group, duration, attenuation, **kwargs):
        AudioAnimEvent(root=self.root, group=group, sound_name=self.name,
                       duration=duration, attenuation=attenuation, **kwargs)


class Music(Sound):
    pass


class Light(Entity):
    TEMPLATE = 'light'

    def __init__(self, light_group, diffuse, ambient, direction, point_name=None,
                 light_type=L_DIRECT, on=True, range=2000, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.point_name = point_name if point_name else self.root.DEFAULT_POINT_NAME
        self.point = self.root.get_point(self.point_name)
        self.light_group = light_group
        self.diffuse = diffuse
        self.ambient = ambient
        self.direction = direction
        self.light_type = light_type
        self.on = on
        self.range = range
        if self.light_type not in LIGHT_TYPES:
            raise Exception(f'Light {self.name} has invalid type {self.light_type}')
        if len(self.diffuse) != 3:
            raise Exception(f'Diffuse of light {self.name} should have 3 points')
        if len(self.ambient) != 3:
            raise Exception(f'Ambient of light {self.name} should have 3 points')
        if len(self.direction) != 3:
            raise Exception(f'Direction of light {self.name} should have 3 points')

    def get_light_name(self):
        return f'LIGHT_{self.name}'

    def get_index(self):
        return self.light_group

    def get_params(self):
        return {
            'name': self.get_light_name(),
            'point': self.point,
            'light_group': self.light_group,
            'light_type': self.light_type,
            'on': self.on,
            'range': self.range,
            'diffuse': ', '.join([str(i) for i in self.diffuse]),
            'ambient': ', '.join([str(i) for i in self.ambient]),
            'direction': ', '.join([str(i) for i in self.direction]),
        }

    def turn_on(self, group, **kwargs):
        LightAnimEvent(root=self.root, group=group, object_name=self.get_light_name(), on=True, duration=0, smooth=False, **kwargs)

    def turn_off(self, group, **kwargs):
        LightAnimEvent(root=self.root, group=group, object_name=self.get_light_name(), on=False, duration=0, smooth=False, **kwargs)

    def set_diffuse(self, group, diffuse, duration, smooth=False, **kwargs):
        LightAnimEvent(root=self.root, group=group, object_name=self.get_light_name(), diffuse=diffuse,
                       duration=duration, smooth=smooth, **kwargs)

    def set_ambient(self, group, ambient, duration, smooth=False, **kwargs):
        LightAnimEvent(root=self.root, group=group, object_name=self.get_light_name(), ambient=ambient,
                       duration=duration, smooth=smooth, **kwargs)

    def set_range(self, group, range, duration, smooth=False, **kwargs):
        LightAnimEvent(root=self.root, group=group, object_name=self.get_light_name(), lt_range=range,
                       duration=duration, smooth=smooth, **kwargs)

    def animate_diffuse(self, group, sequence_name, start_diffuse, end_diffuse,
                        duration, start_gap, end_gap, repeat, smooth=False):
        event_group = f'ambient_anim_{sequence_name}'
        self.root.clone_group(event_group, original=group)
        first = True
        for i in range(1, repeat+1):
            gap = start_gap if first else end_gap
            self.set_diffuse(group=event_group, diffuse=end_diffuse if first else start_diffuse,
                             duration=duration, smooth=smooth, time_append=duration+gap)
            first = not first

    # possible not working???
    def animate_ambient(self, group, sequence_name, start_ambient, end_ambient,
                        duration, gap, repeat, smooth=False):
        event_group = f'ambient_anim_{sequence_name}'
        self.root.clone_group(event_group, original=group)
        first = True
        for i in range(1, repeat+1):
            self.set_ambient(group=event_group, ambient=end_ambient if first else start_ambient,
                             duration=duration, smooth=smooth, time_append=duration+gap)
            first = not first

    def animate_range(self, group, sequence_name, start_range, end_range,
                        duration, gap, repeat, smooth=False):
        event_group = f'range_anim_{sequence_name}'
        self.root.clone_group(event_group, original=group)
        first = True
        for i in range(1, repeat+1):
            self.set_range(group=event_group, range=end_range if first else start_range,
                           duration=duration, smooth=smooth, time_append=duration+gap)
            first = not first


class Alchemy(Entity):
    TEMPLATE = 'alchemy'

    def __init__(self, particles, point_name=None, sparam=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.point_name = point_name if point_name else self.root.DEFAULT_POINT_NAME
        self.point = self.root.get_point(self.point_name)
        self.particles = particles
        self.sparam = sparam

    def get_params(self):
        return {
            'name': self.name,
            'particles': self.particles,
            'point': self.point,
            'sparam': self.sparam,
        }

    def start(self, group, duration, **kwargs):
        StartAlchemyEvent(root=self.root, group=group, object_name=self.name, duration=duration, **kwargs)
