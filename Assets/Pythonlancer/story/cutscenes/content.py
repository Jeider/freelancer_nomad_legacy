from story import math


ENTITY_TEMPLATE_FOLDER = 'cutscenes/entity/'
EVENT_TEMPLATE_FOLDER = 'cutscenes/event/'

MAIN = 'main'
BG = 'bg'

IDLE = 'idle'

MALE_ANIMS = {
    IDLE: 'Sc_MLBODY_STND_IDLE_000LV_xa_04',
}

FEMALE_ANIMS = {
    IDLE: 'Sc_FMBODY_STND_IDLE_000LV_xa_05',
}


class Point:
    def __init__(self, name, position, orientation, rotate):
        self.name = name
        self.position = [position[0], position[2], -position[1]]
        self.orientation = [orientation[3], orientation[0], orientation[1], -orientation[2]]  # quaternion
        deg_euler = math.radians_to_degrees(*rotate)
        self.rotate = [deg_euler[0], deg_euler[1], deg_euler[2]]
        if len(self.orientation) != 4:
            raise Exception(f'Point {name} have wrong quaternion for orientation')

    @property
    def pos(self):
        return '{0:.2f}, {1:.2f}, {2:.2f}'.format(*self.position)

    @property
    def orient(self):
        return '{0:.2f}, {1:.2f}, {2:.2f}, {3:.2f}'.format(*math.euler_to_quat(*self.rotate))

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
    def __init__(self, root, time=0):
        self.root = root
        self.time = time

    def add_event(self, event, time_append=0, time_delay=0):
        time = self.time + time_delay
        self.root.add_event(time, event)
        self.time += time_append

    def get_time(self):
        return self.time


class Event:
    TEMPLATE = None

    def __init__(self, root, group=MAIN, time_append=0, time_delay=0):
        self.root = root
        self.time = 0
        self.group = self.root.get_group(group)
        self.group.add_event(self, time_append, time_delay)

    def set_time(self, time):
        self.time = time

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

    def __init__(self, object_name, target_name, duration, smooth=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.object_name = object_name
        self.target_name = target_name
        self.duration = duration
        self.smooth = smooth

    def get_params(self):
        return {
            'object_name': self.object_name,
            'target_name': self.target_name,
            'duration': self.duration,
            'smooth': self.smooth,
        }


class MotionEvent(Event):
    TEMPLATE = 'motion'

    def __init__(self, object_name, anim, duration, time_scale=1, start_time=0, loop=False, *args, **kwargs):
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


class Character(Entity):
    TEMPLATE = 'character'

    def __init__(self, actor, light_group, init_point, rotate=0, *args, **kwargs):
        self.actor = actor
        name = f'Char_{self.actor.NAME}'
        super().__init__(name=name, *args, **kwargs)
        self.light_group = light_group
        self.init_point = init_point
        self.init_pos = self.root.get_point(self.init_point).pos
        self.rotate = rotate
        self.animations = FEMALE_ANIMS if self.actor.is_female() else MALE_ANIMS

    def get_init_matrix(self):
        mx = math.euler_to_matrix(0, self.rotate, 0)
        return '''
            {{ {0:.7f},{1:.7f},{2:.7f} }}, 
            {{ {3:.7f},{4:.7f},{5:.7f} }},
            {{ {6:.7f},{7:.7f},{8:.7f} }}
        '''.format(
            mx[0][0], mx[0][1], mx[0][2],
            mx[1][0], mx[1][1], mx[1][2],
            mx[2][0], mx[2][1], mx[2][2],
        )

    def get_params(self):
        return {
            'name': self.name,
            'template_name': self.actor.CUTSCENE_APPEARANCE,
            'actor': self.actor.get_game_actor(),
            'light_group': self.light_group,
            'init_pos': self.init_pos,
            'init_matrix': self.get_init_matrix(),
        }

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
                        time_delay=lip.get_delay(), time_append=lip.get_delay())

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
        MoveEvent(root=self.root, group=group,
                  object_name=self.name, target_name=target_obj.name,
                  duration=duration, smooth=smooth,
                  time_delay=time_delay, time_append=time_append)

    def move_focus(self, group, index, duration, time_delay=0, time_append=0, smooth=True):
        target = f'{self.focus_name}{index}'
        target_obj = self.root.get_automarker(target)
        MoveEvent(root=self.root, group=group,
                  object_name=self.focus.name, target_name=target_obj.name,
                  duration=duration, smooth=smooth,
                  time_delay=time_delay, time_append=time_append)
