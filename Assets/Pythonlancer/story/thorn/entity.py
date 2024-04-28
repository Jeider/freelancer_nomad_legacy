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
        self.orientation = [[1, 0, 0], [0, 1, 0], [0, 0, 0]]
        self.flags = self.FLAGS

    def get_position_as_thorn(self):
        return '({0}, {1}, {2})'.format(*self.position)

    def get_orientation_as_thorn(self):
        pass

    def get_extra_items(self):
        return []

    def get_thorn(self):
        thorn = list()
        thorn.append(param(ENTITY_NAME, self.name))
        for key, val in self.root_data.items():
            thorn.append(param(key, val))
        thorn.append(param(POS, self.get_position_as_thorn()))
        thorn.append(param(ORIENT, self.get_orientation_as_thorn()))


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
    pass
