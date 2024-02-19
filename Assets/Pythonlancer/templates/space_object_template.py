from text.dividers import SINGLE_DIVIDER

POS = 'pos'
NICKNAME = 'nickname'


class SpaceObjectTemplate(object):
    TEMPLATE = None
    SPACE_OBJECT_NAME = None

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    def __init__(self, template=None, space_object_name=None):
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
        def prepare_pos(pos_val):
            if pos_val % 1 == 0:
                return int(pos_val)
            else:
                return pos_val

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
