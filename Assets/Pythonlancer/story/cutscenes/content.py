from story import math


ENTITY_TEMPLATE_FOLDER = 'cutscenes/entity/'


class Point:
    def __init__(self, name, position, orientation):
        self.name = name
        self.position = position
        self.orientation = orientation  # quaternion
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
        return math.quat_to_matrix(self.orientation)


class Entity:
    TEMPLATE = None

    def __init__(self, root):
        self.root = root

    def get_params(self):
        raise NotImplementedError

    def get_template(self):
        if not self.TEMPLATE:
            raise Exception(f'Entity {self} have no template')
        return ENTITY_TEMPLATE_FOLDER + f'{self.TEMPLATE}.lua'

    def get_thorn(self):
        return self.root.tpl_manager.get_result(self.get_template(), self.get_params())


class Marker(Entity):
    TEMPLATE = 'marker'

    def __init__(self, root, name, point):
        super().__init__(root)
        self.name = name
        self.point = point

    def get_params(self):
        return {
            'name': self.name,
            'point': self.point,
        }
