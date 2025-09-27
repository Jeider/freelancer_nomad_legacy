from story.math import euler_to_matrix, relocate_point, rotate_point
from text.dividers import SINGLE_DIVIDER

POS = 'pos'
ROTATE = 'rotate'
NICKNAME = 'nickname'
ARCHETYPE = 'archetype'

ARCHETYPE_MAP = {
    'space_girder': 'attached_girder_rot',
    'space_girdera': 'attached_girder_a',
    'space_girderc': 'rmbase_attached_girder_c',
    'space_industrial02a': 'attached_industrial02a_root',
    'space_industrial02d': 'attached_industrial02d',
    'space_panel': 'attached_solarpnl',
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
    'om15_xxxlarge_door': 'attached_om15_xxxlarge_door',
    'om15_xxxlarge_tunnel01': 'attached_om15_xxxlarge_tunnel01',
    'om15_xxxlarge_tunnel02': 'attached_om15_xxxlarge_tunnel02',
    'om15_xxxlarge_tunnel03': 'attached_om15_xxxlarge_tunnel03',
    'om15_xxxlarge_tunnel04': 'attached_om15_xxxlarge_tunnel04',
    'om15_xxxlarge_tunnel05': 'attached_om15_xxxlarge_tunnel05',
    'om15_xxxlarge_wall': 'attached_om15_xxxlarge_wall',
    'large_ring': 'attached_small_station_ring_alt',
    'space_large_arch': 'attached_space_large_arch',
    'space_large_arch_part': 'attached_space_large_arch_part',
    'space_short_large_arch': 'attached_space_short_large_arch',
    'space_long_large_arch': 'attached_space_long_large_arch',
    'shipyard': 'attached_shipyard_a_root',
    'space_small_control_block': 'rmbase_attached_small_control_block',
    'space_tankl4': 'attached_tankl4_root',
    'space_tube_fix': 'attached_space_tube_fix',
    'space_cloakgen_laser': 'attached_space_cloakgen_laser',
}



FORCE_IGNORED_ARCHETYPES = [
    'orderbase_jumphole',
    'terraforming_core',
    'sw_center_250',
    'space_tube_hidden_connect',
    'hidden_connect',
]


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

    def get_instance(self, dock_props='', root_props='', new_space_object_name=None, move_to=None, rotate_core=0,
                     archetype_changes=None):
        replaces = []

        if new_space_object_name:
            replaces.append(tuple((self.space_object_name, new_space_object_name)))

        if len(replaces):
            self.apply_replaces(replaces)

        self.apply_props(dock_props, root_props)

        if move_to or rotate_core:
            self.relocate(move_to=move_to, rotate_core=rotate_core, archetype_changes=archetype_changes)

        return self.instance

    def apply_replaces(self, replaces):
        for replace_from, replace_to in replaces:
            self.instance = self.instance.replace(replace_from, replace_to)

    def apply_props(self, dock_props, root_props):
        self.instance = self.instance.format(dock_props=dock_props, root_props=root_props)

    def relocate(self, move_to=None, rotate_core=0, archetype_changes=None):
        archetype_changes = archetype_changes if archetype_changes is not None else []
        if not move_to:
            move_to = [0, 0, 0]

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
                    pos_x = float(pos_split[0])
                    pos_y = float(pos_split[1])
                    pos_z = float(pos_split[2])
                except ValueError as e:
                    raise Exception('Could not convert pos. Last nickname: {nick}. Reason: {ex}'.format(nick=self.last_nickname, ex=e))

                if rotate_core != 0:
                    pos_x, pos_y, pos_z = relocate_point(
                        point=[pos_x, pos_y, pos_z],
                        rotate_y=rotate_core
                    )

                lines.append('{0} = {1:.5f}, {2:.5f}, {3:.5f}'.format(
                    POS,
                    prepare_pos(pos_x + move_x),
                    prepare_pos(pos_y + move_y),
                    prepare_pos(pos_z + move_z),
                ))

            elif line.startswith(ROTATE):
                if rotate_core != 0:
                    rotate_split = line.split('=')[1].strip().split(',')
                    try:
                        rotate_x = float(rotate_split[0])
                        rotate_y = float(rotate_split[1])
                        rotate_z = float(rotate_split[2])
                    except ValueError as e:
                        raise Exception('Could not convert rotate. Last nickname: {nick}. Reason: {ex}'.format(
                            nick=self.last_nickname, ex=e))

                    rotate_y -= rotate_core

                    lines.append('{0} = {1:.7f}, {2:.7f}, {3:.7f}'.format(
                        ROTATE,
                        prepare_pos(rotate_x),
                        prepare_pos(rotate_y),
                        prepare_pos(rotate_z),
                    ))
                else:
                    lines.append(line)

            elif line.startswith(ARCHETYPE):
                archetype = line
                for change1, change2 in archetype_changes:
                    archetype = archetype.replace(change1, change2)
                lines.append(archetype)

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

    def get_segments_as_loadout(self, warning=False):
        allowed_archetypes = ARCHETYPE_MAP.keys()
        records = []
        for segment in self.segments:
            if segment.archetype in FORCE_IGNORED_ARCHETYPES:
                continue
            if segment.archetype not in allowed_archetypes:
                if not warning:
                    continue
                else:
                    raise Exception(f'archetype {segment.archetype} is not allowed')

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
parent = {self.space_object_name}
'''
            )
        return SINGLE_DIVIDER.join(records)


    @classmethod
    def get_locked_object_offset(cls, index=0):
        if not cls.LOCKED_OBJECT_OFFSETS:
            raise Exception('Locked object offset isnt defined for %s' % cls.__class__.__name__)
        return cls.LOCKED_OBJECT_OFFSETS[index]
