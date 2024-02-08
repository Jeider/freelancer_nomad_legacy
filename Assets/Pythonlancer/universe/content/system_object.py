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

    IDS_NAME = 1  # TEMPORARY

    REL_APPEND = 3000  # distance between object and tradelane
    REL_DRIFT = 0  # move initial pos for tradelane start point


    @classmethod
    def get_position(cls):
        if not cls.POS:
            raise Exception('POS is not defined')

        try:
            if not isinstance(cls.POS[0], int) or not isinstance(cls.POS[1], int) or not isinstance(cls.POS[2], int):
                raise Exception('POS must containt only integers')
        except IndexError:
            raise Exception('Not enough items in POS')

        return cls.POS

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

    @classmethod
    def get_tradelane_props(cls, tradelane_side):
        tradelane_side = get_reversed_direction(tradelane_side)

        pos_x, _, pos_z = cls.get_position()

        rel_append = cls.get_rel_append()
        rel_drift = cls.get_rel_drift()
        rel = cls.get_rel()

        if rel_drift > 0:
            if rel == LEFT:
                pos_x += rel_drift
            if rel == RIGHT:
                pos_x -= rel_drift
            if rel == TOP:
                pos_z += rel_drift
            if rel == BOTTOM:
                pos_z -= rel_drift

        if tradelane_side == LEFT:
            pos_x -= rel_append
        if tradelane_side == RIGHT:
            pos_x += rel_append
        if tradelane_side == TOP:
            pos_z -= rel_append
        if tradelane_side == BOTTOM:
            pos_z += rel_append

        return pos_x, POS_Y_FORCE_VALUE, pos_z, cls.IDS_NAME

    def __init__(self, system):
        self.system = system

    def get_system_content(self):
        raise NotImplementedError()
