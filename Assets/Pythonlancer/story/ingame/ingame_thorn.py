GENERIC_TWO_POINT = 'cam_generic_two_point'
GENERIC_TWO_POINT_MOVE = 'cam_generic_two_point_move'
GENERIC_TWO_POINT_MOVE2 = 'cam_generic_two_point_move2'
GENERIC_MOUNTED_ROTATABLE = 'cam_mounted_rotatable'
DEFAULT_TARGET = 'Player'
TEMPLATES_SUBFOLDER = 'ingame_thorn'
DEFAULT_DURATION = 30


class IngameThorn(object):

    def __init__(self, mission, system_class, template, name, points=None,
                 params=None, target=DEFAULT_TARGET, duration=None):
        self.mission = mission
        self.system_class = system_class
        self.template = template
        self.name = name
        self.points = points if points else {}
        self.params = params if params else {}
        self.target = target
        self.duration = duration

    def get_duration(self):
        if self.duration:
            return self.duration
        return DEFAULT_DURATION

    def get_template(self):
        return f'{TEMPLATES_SUBFOLDER}/{self.template}.lua'

    def get_name(self):
        return self.name

    def get_context(self):
        context = {
            'name': self.get_name(),
            'duration': self.get_duration(),
        }
        for key, point in self.points.items():
            context[key] = self.mission.get_system_obj_pos(self.system_class, point)

        for key, param in self.params.items():
            context[key] = param

        return context

    def get_filename(self):
        return f'MISSIONS\GENERATED_THORN\\{self.get_name()}.thn'

    def call(self):
        return f'Act_CallThorn = {self.get_filename()}, {self.target}'
