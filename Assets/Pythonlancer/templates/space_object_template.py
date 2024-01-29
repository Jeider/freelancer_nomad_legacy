from text.dividers import SINGLE_DIVIDER

POS = 'pos'


class SpaceObjectTemplate(object):
    TEMPLATE = None
    SPACE_OBJECT_NAME = None

    def __init__(self):
        if not self.TEMPLATE:
            raise Exception('TEMPLATE not defined')

        if not self.SPACE_OBJECT_NAME:
            raise Exception('SPACE_OBJECT_NAME not defined')

        self.instance = self.TEMPLATE

    def get_instance(self, new_space_object_name=None, move_to=None):
        replaces = []

        if new_space_object_name:
            replaces.append(tuple((self.SPACE_OBJECT_NAME, new_space_object_name)))

        if len(replaces):
            self.apply_replaces(replaces)

        if move_to:
            self.move_position(move_to)

        return self.instance

    def apply_replaces(self, replaces):
        for replace_from, replace_to in replaces:
            self.instance = self.instance.replace(replace_from, replace_to)

    def move_position(self, move_to):
        def prepare_pos(pos_val):
            if pos_val % 1 == 0:
                return int(pos_val)
            else:
                return pos_val

        try:
            move_x = int(move_to[0])
            move_y = int(move_to[1])
            move_z = int(move_to[2])
        except IndexError:
            raise Exception('Invalid move_to format')
        except ValueError:
            raise Exception('move_to must contain integers')

        lines = []
        for line in self.instance.splitlines():
            if line.startswith(POS):
                pos_split = line.split('=')[1].strip().split(',')
                pos_x = float(pos_split[0]) + move_x
                pos_y = float(pos_split[1]) + move_y
                pos_z = float(pos_split[2]) + move_z
                lines.append('{0} = {1}, {2}, {3}'.format(
                    POS,
                    prepare_pos(pos_x),
                    prepare_pos(pos_y),
                    prepare_pos(pos_z),
                ))

            else:
                lines.append(line)

        self.instance = SINGLE_DIVIDER.join(lines)
