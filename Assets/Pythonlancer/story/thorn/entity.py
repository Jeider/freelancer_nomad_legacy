from story.math import euler_to_quat, euler_to_matrix

ENTITY_NAME = 'name'
TYPE = 'type'
TEMPLATE_NAME = 'template_name'
LT_GRP = 'lt_grp'
SRT_GRP = 'srt_grp'
USR_FLG = 'usr_flg'
FLAGS = 'flags'
LIT_DYNAMIC = 'LIT_DYNAMIC'
LIT_AMBIENT = 'LIT_AMBIENT'
SPATIAL_PROPS = 'spatialprops'
POS = 'pos'
ORIENT = 'orient'

THORN_DIVIDER = ',\r\n'


def param(key, value):
    return f'{key} = {value}'


class Entity(object):
    INITIAL_POS = [0, 0, 0]
    FLAGS = []

    def __init__(self, name):
        self.name = name
        self.root_data = {
            LT_GRP: 0,
            SRT_GRP: 0,
            USR_FLG: 0,
        }
        self.position = self.INITIAL_POS
        self.rotate = (0, 0, 0)
        self.flags = self.FLAGS

    def get_position_as_thorn(self):
        return '({0}, {1}, {2})'.format(*self.position)

    def get_rotate(self):
        return self.rotate

    def get_orient_quat(self):
        return '{0:.2f}, {1:.2f}, {2:.2f}, {3:.2f}'.format(*euler_to_quat(*self.get_rotate()))

    def get_orient_matrix(self):
        matrix = euler_to_matrix(*self.get_rotate())
        items = [f'[{line[0]:.2f}, {line[1]:.2f}, {line[2]:.2f}]' for line in matrix]
        return f'[{",".join(items)}]'

    def get_extra_items(self):
        return []

    def get_thorn(self):
        thorn = list()
        thorn.append(param(ENTITY_NAME, self.name))
        for key, val in self.root_data.items():
            thorn.append(param(key, val))
        thorn.append(param(POS, self.get_position_as_thorn()))
        thorn.append(param(ORIENT, self.get_orient_matrix()))


class Marker(Entity):
    pass


class CharacterEntity(Entity):
    FLOOR_HEIGHT = 0
    ACTOR = ''

    def get_extra_items(self):
        return [
            f'compoundprops = {{floor_height = {self.FLOOR_HEIGHT}}}',
            f'userprops = {{Actor = "{self.ACTOR}", category = "Character"}}',
        ]


class Character(object):
    LOOK_HEAD_MARKER = None
    LOOK_EYE_MARKER = None
    LOOK_HEAD_SMOOTH = True
    LOOK_EYE_SMOOTH = True

    def start_ik(self, duration):
        pass

    def look_head(self, point, switch_time=1):
        pass

    def look_eye(self, point, switch_time=1):
        pass
