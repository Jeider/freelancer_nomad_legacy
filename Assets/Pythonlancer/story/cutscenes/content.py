from story import math


ENTITY_TEMPLATE_FOLDER = 'cutscenes/entity/'
EVENT_TEMPLATE_FOLDER = 'cutscenes/event/'

MAIN = 'main'
BG = 'bg'


class Point:
    def __init__(self, name, position, orientation):
        self.name = name
        self.position = [position[0], position[2], -position[1]]
        self.orientation = [orientation[3], orientation[0], orientation[2], -orientation[1]]  # quaternion
        if len(self.orientation) != 4:
            raise Exception(f'Point {name} have wrong quaternion for orientation')

    @property
    def pos(self):
        return '{0:.2f}, {1:.2f}, {2:.2f}'.format(*self.position)

    @property
    def orient(self):
        return '{0:.2f}, {1:.2f}, {2:.2f}, {3:.2f}'.format(*self.orientation)

    @property
    def matrix(self):
        mx = math.quat_to_matrix(self.orientation)
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
        self.time += time_delay
        self.root.add_event(self.time, event)
        self.time += time_append + time_delay


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


class Entity:
    TEMPLATE_ROOT = ENTITY_TEMPLATE_FOLDER
    TEMPLATE = None

    def __init__(self, root):
        self.root = root

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

    def __init__(self, root, name, point_name):
        super().__init__(root)
        self.name = name
        self.point_name = point_name
        self.point = self.root.get_point(self.point_name)

    def get_params(self):
        return {
            'name': self.name,
            'point': self.point,
        }


class StaticCamera(Marker):
    TEMPLATE = 'camera'

    def __init__(self, root, name, fov):
        super().__init__(root, name, name)
        self.fov = fov

    def get_params(self):
        return {
            'name': self.name,
            'point': self.point,
            'fov': self.fov,
        }


class LookAtCamera(Marker):
    TEMPLATE = 'camera'

    def __init__(self, root, name, fov, look_duration=1000):
        super().__init__(root, name, name)
        self.fov = fov
        self.focus = self.root.get_automarker(f'{name}_focus')
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
