import random

from templates.space_object_template import SpaceObjectTemplate
from universe.content.system_object import SystemObject
from universe.content.loadout import DynamicAttachedCargoLoadout

from text.dividers import DIVIDER


MINING_REWARD_LOW = 1
MINING_REWARD_MEDIUM = 2
MINING_REWARD_HUGE = 3
MINING_REWARD_ULTRA = 4


class Mineable(SystemObject):
    ABSTRACT = True


class FieldBox(object):
    def __init__(self, field, left_x, top_z, box_size):
        self.field = field
        self.left_x = left_x
        self.top_z = top_z
        self.box_size = box_size
        self.is_empty = False
        self.contained_object = None

    def mark_as_empty(self):
        self.is_empty = True

    def set_contained_object(self, contained_object)
        self.contained_object = contained_object

    def get_position(self):
        center_append = self.box_size * 0.5

        drift_x = int(center_append * self.field.DRIFT_X)
        drift_y = int(self.box_size * self.field.DRIFT_Y)
        drift_z = int(center_append * self.field.DRIFT_Z)

        center_x = self.left_x + center_append + random.randint(-abs(drift_x), drift_x)
        center_y = 0 + center_append + random.randint(-abs(drift_y), drift_y)
        center_z = self.top_z + center_append + random.randint(-abs(drift_z), drift_z)

        return (center_x, center_y, center_z)

    def get_rotate(self):
        return (
            random.randint(self.field.ROTATE_MIN, self.field.ROTATE_MAX),
            random.randint(self.field.ROTATE_MIN, self.field.ROTATE_MAX),
            random.randint(self.field.ROTATE_MIN, self.field.ROTATE_MAX),
        )


class Field(object):
    BOX_SIZE = 300
    DENSITY_MULTIPLER = 1
    DRIFT_X = 0.1
    DRIFT_Y = 0.1
    DRIFT_Z = 0.1
    ROTATE_MIN = -180
    ROTATE_MAX = 180
    EMPTY_CHANCE = 0

    def __init__(self):
        self.boxes = []
        self.build_field()
        self.mark_empty()

    def build_field(self):
        max_box_size = self.DENSITY_MULTIPLER * self.BOX_SIZE
        init_point = -abs(max_box_size)

        left_x = init_point
        top_z = init_point

        while True:
            self.boxes.append(FieldBox(self, left_x, top_z, self.BOX_SIZE))

            top_z += self.BOX_SIZE
            if top_z >= max_box_size:
                top_z = init_point
                left_x += self.BOX_SIZE

            if left_x >= max_box_size:
                break

    def get_boxes(self):
        return self.boxes

    def mark_empty(self):
        if self.EMPTY_CHANCE == 0:
            return

        empty_count = len(self.boxes) * self.EMPTY_CHANCE
        empty_boxes = random.choice(empty_count, k=empty_count)
        for box in empty_boxes:
            box.mark_empty()


class DefaultField(Field):
    BOX_SIZE = 1000
    DENSITY_MULTIPLER = 5
    DRIFT_X = 0.7
    DRIFT_Y = 0.8
    DRIFT_Z = 0.7
    ROTATE_MIN = -180
    ROTATE_MAX = 180
    EMPTY_CHANCE = 0


class RewardAsteroid(object):
    REWARD_TYPE = None
    MAIN_REWARD_ITEM = None
    ULTRA_REWARD_ITEM = None
    LOADOUTS_COUNT = 5
    REWARD_MIN = 1
    REWARD_MAX = 2
    NAME = 'test'
    LOADOUT_NICKNAME_TEMPLATE = '{name}_loadout_{index}'


    def __init__(self, reward_asteroid_field, asteroid_solar, reward_type):
        self.reward_asteroid_field = reward_asteroid_field
        self.asteroid_solar = asteroid_solar

        if self.MAIN_REWARD_ITEM is None:
            raise Exception('MAIN_REWARD_ITEM is mandatory')

        if self.REWARD_TYPE == MINING_REWARD_ULTRA and ULTRA_REWARD_ITEM is None:
            raise Exception('ULTRA_REWARD_ITEM is mandatory for ultra reward')

        self.loadouts = []

        self.fill_loadouts()

        self.loadout_index = 0

    def fill_loadouts(self):
        for i in range(1, self.LOADOUTS_COUNT + 1):
            nickname = self.LOADOUT_NICKNAME_TEMPLATE.format(name=self.NAME, index=i)
            DynamicAttachedCargoLoadout(
                loadout_nickname=name,
                cargo_item=self.MAIN_REWARD_ITEM,
                hardpoints=self.asteroid_solar.get_hardpoints(),
                min=self.REWARD_MIN,
                max=self.REWARD_MAX,
            )

    def get_next_loadout(self):
        pass


class Omega15LowRewardNiobiumAsteroid(RewardAsteroid):
    REWARD_TYPE = MINING_REWARD_LOW
    MAIN_REWARD_ITEM = 'comm_roid_niobium'
    NAME = 'omega15_low_reward'


class Omega15MediumRewardNiobiumAsteroid(RewardAsteroid):
    REWARD_TYPE = MINING_REWARD_MEDIUM
    MAIN_REWARD_ITEM = 'comm_roid_niobium'
    NAME = 'omega15_medium_reward'


class Omega15HighRewardNiobiumAsteroid(RewardAsteroid):
    REWARD_TYPE = MINING_REWARD_HIGH
    MAIN_REWARD_ITEM = 'comm_roid_niobium'
    NAME = 'omega15_high_reward'


class RewardAsteroidField(Mineable):
    ABSTRACT = False
    FIELD_CLASS = DefaultField
    BASE_REWARD_TYPE = MINING_REWARD_LOW
    EXTRA_REWARD_TYPE = MINING_REWARD_MEDIUM
    EXTRA_REWARD_CHANCE = 0
    REWARD_MIN = 1
    ULTRA_REWARD_ITEM = None

    BASE_REWARD_ASTEROID = Omega15LowRewardNiobiumAsteroid

    ASTEROID_SOLAR = None
    FIELD_NAME = None

    LOADOUT = 'om15_mineast_super'
    # RENEWABLE = True

    SYSTEM_OBJECT_TEMPLATE = '''[Object]
nickname = {nickname}
pos = {pos}
rotate = {rotate}
archetype = {archetype}
loadout = {loadout}'''

    DUMMY_NAME = 'xast_dummy'

    NICKNAME_TEMPLATE = '{dummy_name}_asteroid_{index}'

    def __init__(self, system):
        self.system = system
        self.field = self.FIELD_CLASS()
        self.dummy_system_object_string = self.generate_asteroids()
        self.asteroid_solar = self.ASTEROID_SOLAR()

    def generate_asteroids(self):
        items = []
        index = 1

        for box in self.field.get_boxes():
            if box.is_empty:
                continue

            items.append(
                self.SYSTEM_OBJECT_TEMPLATE.format(
                    nickname=self.create_nickname(index),
                    pos='{}, {}, {}'.format(*box.get_position()),
                    rotate='{}, {}, {}'.format(*box.get_rotate()),
                    archetype=self.ARCHETYPE,
                    loadout=self.LOADOUT
                )
            )
            index += 1

        return DIVIDER.join(items)

    def create_nickname(self, index):
        return self.NICKNAME_TEMPLATE.format(dummy_name=self.DUMMY_NAME, index=index)

    def get_system_content(self):
        real_object = SpaceObjectTemplate(
            template=self.dummy_system_object_string,
            space_object_name=self.DUMMY_NAME,
        )

        return real_object.get_instance(new_space_object_name=self.FIELD_NAMEs, move_to=self.POS)


# class MediumRewardField(RewardAsteroidField):
#     MEDIUM_REWARD_CHANCE = 0.4
#     HUGE_REWARD_CHANCE = 0