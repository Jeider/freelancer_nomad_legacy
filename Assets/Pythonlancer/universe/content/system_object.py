from text.dividers import SINGLE_DIVIDER, DIVIDER
from random import randint

TOP = 'top'
BOTTOM = 'bottom'
LEFT = 'left'
RIGHT = 'right'

DIRECTIONS = (TOP, BOTTOM, LEFT, RIGHT)
POS_Y_FORCE_VALUE = 0

MIN_REL_APPEND = 500

POS_KEY = 'pos'
ROT_KEY = 'rotate'
SIZE_KEY = 'size'

FULL_ALIAS_TEMPLATE = '{alias}{index}'

RAND_ROTATE_MIN = -360
RAND_ROTATE_MAX = 360


def get_reversed_direction(direction):
    if direction == TOP:
        return BOTTOM

    if direction == BOTTOM:
        return TOP

    if direction == LEFT:
        return RIGHT

    if direction == RIGHT:
        return LEFT

    raise Exception('unknown direction %s' % direction)


class SystemObject(object):
    ABSTRACT = True

    POS = None
    REL = None

    ALIAS = None
    INDEX = 1

    IDS_NAME = 1  # TEMPORARY
    IDS_INFO = 1  # TEMPORARY

    REL_APPEND = 3000  # distance between object and tradelane
    REL_DRIFT = 0  # move initial pos for tradelane start point

    ROTATE_RANDOM = False

    FACTION = None

    LAWFUL_POPULATION_CLASS = None
    UNLAWFUL_POPULATION_CLASS = None

    @classmethod
    def is_abstract(cls):
        return cls.ABSTRACT

    @classmethod
    def get_rel(cls):
        if not cls.REL:
            raise Exception('REL is required')

        if cls.REL not in DIRECTIONS:
            raise Exception('REL %s is not correct direction' % cls.REL)

        return cls.REL

    @classmethod
    def get_rel_drift(cls):
        return cls.REL_DRIFT

    @classmethod
    def get_rel_append(cls):
        if cls.REL_APPEND < MIN_REL_APPEND:
            raise Exception('Too small REL_APPEND')
        return cls.REL_APPEND

    def get_tradelane_props(self, tradelane_side, extra_drift=0, extra_drift_alt_axis=0, force_offset=None):
        if force_offset is not None:
            return force_offset[0], POS_Y_FORCE_VALUE, force_offset[2], self.IDS_NAME

        tradelane_side = get_reversed_direction(tradelane_side)

        pos_x, _, pos_z = self.get_position()

        rel_append = self.get_rel_append()
        rel_drift = self.get_rel_drift()
        rel = self.get_rel()

        if rel_drift > 0:
            if rel == LEFT:
                pos_x += rel_drift + extra_drift
            if rel == RIGHT:
                pos_x -= rel_drift + extra_drift
            if rel == TOP:
                pos_z += rel_drift + extra_drift
            if rel == BOTTOM:
                pos_z -= rel_drift + extra_drift

        if extra_drift != 0:
            if rel == LEFT:
                pos_x += extra_drift
            if rel == RIGHT:
                pos_x += extra_drift
            if rel == TOP:
                pos_z += extra_drift
            if rel == BOTTOM:
                pos_z += extra_drift

        if extra_drift_alt_axis != 0:
            if rel == LEFT:
                pos_z += extra_drift_alt_axis
            if rel == RIGHT:
                pos_z += extra_drift_alt_axis
            if rel == TOP:
                pos_x += extra_drift_alt_axis
            if rel == BOTTOM:
                pos_x += extra_drift_alt_axis

        if tradelane_side == LEFT:
            pos_x -= rel_append
        if tradelane_side == RIGHT:
            pos_x += rel_append
        if tradelane_side == TOP:
            pos_z -= rel_append
        if tradelane_side == BOTTOM:
            pos_z += rel_append

        return pos_x, POS_Y_FORCE_VALUE, pos_z, self.IDS_NAME

    def __init__(self, system, *args, **kwargs):
        self.system = system
        self.init_args = args
        self.init_kwargs = kwargs
        self.force_rotate_value = randint(RAND_ROTATE_MIN, RAND_ROTATE_MAX) if self.ROTATE_RANDOM else None

    def get_system_content(self):
        raise NotImplementedError()

    @classmethod
    def get_alias(cls):
        if cls.ALIAS is None:
            raise Exception('unknown alias')
        return cls.ALIAS

    @classmethod
    def get_full_alias(cls):
        return FULL_ALIAS_TEMPLATE.format(
            alias=cls.get_alias(),
            index=cls.INDEX,
        )
    def get_position(self):
        return self.system.template.get_item_pos(self.get_full_alias())

    def get_rotate(self):
        if self.force_rotate_value:
            return (0, self.force_rotate_value, 0)
        return self.system.template.get_item_rotate(self.get_full_alias())

    def get_shape(self):
        return self.system.template.get_item_shape(self.get_full_alias())

    def get_size(self):
        return self.system.template.get_item_size(self.get_full_alias())

    def get_faction(self):
        return self.FACTION

    def get_lawful_population_class(self):
        if self.LAWFUL_POPULATION_CLASS:
            return self.LAWFUL_POPULATION_CLASS
        elif self.system.LAWFUL_POPULATION_CLASS:
            return self.system.LAWFUL_POPULATION_CLASS
        raise Exception('lawful population class isnt defined for %s' % self.__class__.__name__)

    def get_unlawful_population_class(self):
        if self.UNLAWFUL_POPULATION_CLASS:
            return self.UNLAWFUL_POPULATION_CLASS
        elif self.system.UNLAWFUL_POPULATION_CLASS:
            return self.system.UNLAWFUL_POPULATION_CLASS
        raise Exception('unlawful population class isnt defined for %s' % self.__class__.__name__)


class DynamicSystemObject(SystemObject):
    ABSTRACT = True

    def __init__(self, system, space_nickname, alias, index, *args, **kwargs):
        self.space_nickname = space_nickname
        self.alias = alias
        self.index = index
        super().__init__(system, *args, **kwargs)

    @classmethod
    def get_alias(cls):
        raise Exception('can not access static alias of dynamic object')

    @classmethod
    def get_full_alias(cls):
        raise Exception('can not access static alias of dynamic object')

    def get_dynamic_alias(self):
        if self.alias is None:
            raise Exception('unknown alias')
        return self.alias

    def get_full_dynamic_alias(self):
        return FULL_ALIAS_TEMPLATE.format(
            alias=self.get_dynamic_alias(),
            index=self.index,
        )

    def get_position(self):
        return self.system.template.get_item_pos(self.get_full_dynamic_alias())

    def get_rotate(self):
        return self.system.template.get_item_rotate(self.get_full_dynamic_alias())

    def get_shape(self):
        shape = self.system.template.get_item_shape(self.get_full_dynamic_alias())
        if shape.upper() == 'SPHERE':
            raise Exception('SPHERE shapes not supported at this moment')
        return shape

    def get_size(self):
        return self.system.template.get_item_size(self.get_full_dynamic_alias())