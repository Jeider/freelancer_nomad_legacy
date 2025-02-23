from story.math import euler_to_quat, euler_to_matrix
from text.dividers import SINGLE_DIVIDER

POS = 'pos'
ROTATE = 'rotate'
NICKNAME = 'nickname'
ARCHETYPE = 'archetype'

ARCHETYPE_MAP = {
    'space_girder': 'attached_girder_rot',
    'space_girdera': 'attached_girder_a',
    'space_industrial02a': 'attached_industrial02a_root',
    'space_domea': 'attached_dome_a',
    'space_industrial01a': 'attached_ind01_a_root',
    'space_industriala': 'attached_ind_a_rot',
    'space_short_tube': 'attached_short_tube',
    'space_airlock_dummy': 'attached_airlock_dummy',
    'space_habitat_tall': 'attached_habitat_tall_gen',
    'space_habitat_wide': 'attached_habitat_wide_gen',
    'space_small_control_tower': 'attached_small_control_tower',
    'space_medium_control_tower': 'attached_medium_control_tower',
    'space_control_tower': 'attached_large_control_tower',
}

def prepare_pos(pos_val):
    if pos_val % 1 == 0:
        return int(pos_val)
    else:
        return pos_val


class StationSegment():

    def __init__(self, nickname):
        self.nickname = nickname.strip()
        self.pos = (0, 0, 0)
        self.rotate = (0, 0, 0)
        self.archetype = None

    def set_pos(self, pos_string):
        pos_list = pos_string.strip().split(',')
        try:
            self.pos = (
                prepare_pos(float(pos_list[0])),
                prepare_pos(float(pos_list[1])),
                prepare_pos(float(pos_list[2]))
            )
        except (ValueError, TypeError):
            raise Exception(f'Could not parse pos for {self.nickname}')

    def set_rotate(self, rotate_string):
        rotate_list = rotate_string.strip().split(',')
        try:
            self.rotate = (
                prepare_pos(float(rotate_list[0])),
                prepare_pos(float(rotate_list[1])),
                prepare_pos(float(rotate_list[2]))
            )
        except ValueError:
            raise Exception(f'Could not parse rotate for {self.nickname}')

    def set_archetype(self, archetype):
        self.archetype = archetype.strip()

    def get_pos(self):
        return f'{self.pos[0]}, {self.pos[1]}, {self.pos[2]}'

    def get_rotate(self):
        return f'{self.rotate[0]}, {self.rotate[1]}, {self.rotate[2]}'

    def get_orient_matrix(self):
        matrix = euler_to_matrix(*self.rotate)
        items = matrix[0] + matrix[1] + matrix[2]
        return ",".join([str(item) for item in items])


class SpaceObjectTemplate(object):
    TEMPLATE = None
    SPACE_OBJECT_NAME = None
    LOCKED_OBJECT_OFFSETS = None

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    def __init__(self, template=None, space_object_name=None):
        self.segments = []
        self.template = template if template else self.TEMPLATE
        if not self.template:
            raise Exception('TEMPLATE not defined')

        self.space_object_name = space_object_name if space_object_name else self.SPACE_OBJECT_NAME
        if not self.space_object_name:
            raise Exception('SPACE_OBJECT_NAME not defined')

        self.instance = self.template
        self.last_nickname = ''

    def get_instance(self, dock_props='', root_props='', new_space_object_name=None, move_to=None):
        replaces = []

        if new_space_object_name:
            replaces.append(tuple((self.space_object_name, new_space_object_name)))

        if len(replaces):
            self.apply_replaces(replaces)

        self.apply_props(dock_props, root_props)

        if move_to:
            self.move_position(move_to)

        return self.instance


    def apply_replaces(self, replaces):
        for replace_from, replace_to in replaces:
            self.instance = self.instance.replace(replace_from, replace_to)

    def apply_props(self, dock_props, root_props):
        self.instance = self.instance.format(dock_props=dock_props, root_props=root_props)

    def move_position(self, move_to):

        try:
            move_x = float(move_to[0])
            move_y = float(move_to[1])
            move_z = float(move_to[2])
        except IndexError:
            raise Exception('Invalid move_to format')
        except ValueError:
            raise Exception('move_to must contain integers')

        lines = []
        for line in self.instance.splitlines():
            if line.startswith(POS):
                pos_split = line.split('=')[1].strip().split(',')
                try:
                    pos_x = float(pos_split[0]) + move_x
                    pos_y = float(pos_split[1]) + move_y
                    pos_z = float(pos_split[2]) + move_z
                except ValueError as e:
                    raise Exception('Could not convert value. Last nickname: {nick}. Reason: {ex}'.format(nick=self.last_nickname, ex=e))
                lines.append('{0} = {1}, {2}, {3}'.format(
                    POS,
                    prepare_pos(pos_x),
                    prepare_pos(pos_y),
                    prepare_pos(pos_z),
                ))

            else:
                if line.startswith(NICKNAME):
                    self.last_nickname = line
                lines.append(line)

        self.instance = SINGLE_DIVIDER.join(lines)

    def parse_segments(self):
        this_segment = None

        for line in self.instance.splitlines():
            line_split = line.split('=')

            if line.startswith(NICKNAME):
                this_segment = StationSegment(line_split[1])
                self.segments.append(this_segment)

            elif line.startswith(POS):
                this_segment.set_pos(line_split[1])

            elif line.startswith(ROTATE):
                this_segment.set_rotate(line_split[1])

            elif line.startswith(ARCHETYPE):
                this_segment.set_archetype(line_split[1])

    def get_segments_as_hardpoints_xml(self):
        hps = []
        for segment in self.segments:
            hps.append(f'''
                <Hp_{segment.nickname}>
                   <Orientation type="Matrix">{segment.get_orient_matrix()}</Orientation>
                   <Position type="Vector">{segment.get_pos()}</Position>
                </Hp_{segment.nickname}>
            ''')

        return SINGLE_DIVIDER.join(hps)

    def get_segments_as_loadout(self):
        allowed_archetypes = ARCHETYPE_MAP.keys()
        records = []
        for segment in self.segments:
            if segment.archetype not in allowed_archetypes:
                continue

            records.append(
                f'equip = {ARCHETYPE_MAP[segment.archetype]}, Hp_{segment.nickname}'
            )
        return SINGLE_DIVIDER.join(records)

    def get_instance_from_segments(self):
        hardpoint_archetypes = ARCHETYPE_MAP.keys()
        records = []
        for segment in self.segments:
            if segment.archetype in hardpoint_archetypes:
                continue

            records.append(
                f'''[Object]
nickname = {segment.nickname}
pos = {segment.get_pos()}
rotate = {segment.get_rotate()}
archetype = {segment.archetype}
parent = up2_01
'''
            )
        return SINGLE_DIVIDER.join(records)


    @classmethod
    def get_locked_object_offset(cls, index=0):
        if not cls.LOCKED_OBJECT_OFFSETS:
            raise Exception('Locked object offset isnt defined for %s' % cls.__class__.__name__)
        return cls.LOCKED_OBJECT_OFFSETS[index]
