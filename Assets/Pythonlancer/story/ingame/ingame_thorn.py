GENERIC_TWO_POINT = 'cam_generic_two_point'
DEFAULT_TARGET = 'Player'
TEMPLATES_SUBFOLDER = 'ingame_thorn'


class IngameThorn(object):

    def __init__(self, mission, system_class, template, name, points, target=DEFAULT_TARGET):
        self.mission = mission
        self.system_class = system_class
        self.template = template
        self.name = name
        self.points = points
        self.target = target

    def get_template(self):
        return f'{TEMPLATES_SUBFOLDER}/{self.template}.lua'

    def get_name(self):
        return self.name

    def get_context(self):
        context = {}
        for key, point in self.points.items():
            context[key] = self.mission.get_system_obj_pos(self.system_class, point)

        return context

    def get_filename(self):
        return f'MISSIONS\GENERATED_THORN\\{self.get_name()}.thn'

    def call(self):
        return f'Act_CallThorn = {self.get_filename()}, {self.target}'
