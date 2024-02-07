import random

from templates.space_object_template import SpaceObjectTemplate
from universe.content.system_object import SystemObject
from universe.content.loadout import DynamicAttachedCargoLoadout

from text.dividers import DIVIDER


MINING_REWARD_LOW = 'low'
MINING_REWARD_MEDIUM = 'medium'
MINING_REWARD_HIGH = 'high'
MINING_REWARD_ULTRA = 'ultra'


class Mineable(SystemObject):
    ABSTRACT = True


class FieldBox(object):
    def __init__(self, field, left_x, top_z, box_size):
        self.field = field
        self.left_x = left_x
        self.top_z = top_z
        self.box_size = box_size
        self.is_empty = False
        self.reward_type = None

        self.center_append = self.box_size * 0.5

        self.drift_x = int(self.center_append * self.field.DRIFT_X)
        self.drift_y = int(self.box_size * self.field.DRIFT_Y)
        self.drift_z = int(self.center_append * self.field.DRIFT_Z)

    def mark_as_empty(self):
        self.is_empty = True

    def set_reward_type(self, reward_type):
        self.reward_type = reward_type

    def get_reward_type(self):
        return self.reward_type

    def get_position(self):

        center_x = self.left_x + self.center_append + random.randint(-abs(self.drift_x), self.drift_x)
        center_y = 0 + self.center_append + random.randint(-abs(self.drift_y), self.drift_y)
        center_z = self.top_z + self.center_append + random.randint(-abs(self.drift_z), self.drift_z)

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

    def get_not_empty_boxes(self):
        return [box for box in self.boxes if not box.is_empty]

    def get_boxes_without_reward(self):
        return [box for box in self.boxes if not box.is_empty and not box.reward_type]

    def mark_empty(self):
        if self.EMPTY_CHANCE == 0:
            return

        empty_count = len(self.boxes) * self.EMPTY_CHANCE
        empty_boxes = random.choice(empty_count, k=empty_count)
        for box in empty_boxes:
            box.mark_empty()


class DefaultField(Field):
    BOX_SIZE = 1000
    DENSITY_MULTIPLER = 3
    DRIFT_X = 0.7
    DRIFT_Y = 0.8
    DRIFT_Z = 0.7
    ROTATE_MIN = -180
    ROTATE_MAX = 180
    EMPTY_CHANCE = 0



class RewardProps(object):
    REWARD_TYPE = None
    MIN = 1
    MAX = 2
    LOADOUTS_COUNT = 5


class RewardPropsLow(object):
    REWARD_TYPE = MINING_REWARD_LOW
    MIN = 1
    MAX = 3
    LOADOUTS_COUNT = 5
    REWARD_ITEM = 'comm_roid_niobium'


class RewardPropsMedium(object):
    REWARD_TYPE = MINING_REWARD_MEDIUM
    MIN = 5
    MAX = 10
    LOADOUTS_COUNT = 5
    REWARD_ITEM = 'comm_roid_niobium'


class RewardPropsHigh(object):
    REWARD_TYPE = MINING_REWARD_HIGH
    MIN = 10
    MAX = 20
    LOADOUTS_COUNT = 5
    REWARD_ITEM = 'comm_roid_niobium'


class RewardPropsUltra(object):
    REWARD_TYPE = MINING_REWARD_ULTRA
    MIN = 10
    MAX = 25
    LOADOUTS_COUNT = 1
    REWARD_ITEM = 'comm_roid_niobium'
    ULTRA_REWARD_ITEM = 'rh_lightgun01'


class RewardsGroup(object):
    REWARD_PROPS = [
        RewardPropsLow,
        RewardPropsMedium,
        RewardPropsHigh,
    ]
    ULTRA_REWARD_PROP = RewardPropsUltra
    ASTEROID_SOLAR = None

    NAME = 'any'
    LOADOUT_NICKNAME_TEMPLATE = '{name}_{reward_type}_loadout_{index}'

    def __init__(self):
        self.asteroid_solar = self.ASTEROID_SOLAR()

        self.loadouts_list = []
        self.loadouts_db = {}

        self.loadout_ultra_reward = None

        self.fill_loadouts()

    def fill_loadouts(self):
        hardpoints = self.asteroid_solar.get_hardpoints()
        init_items = self.asteroid_solar.get_init_loadout_items()

        for reward_prop in self.REWARD_PROPS:
            self.loadouts_db[reward_prop.REWARD_TYPE] = []
            for i in range(1, reward_prop.LOADOUTS_COUNT + 1):
                nickname = self.LOADOUT_NICKNAME_TEMPLATE.format(
                    name=self.NAME,
                    reward_type=reward_prop.REWARD_TYPE,
                    index=i
                )
                loadout = DynamicAttachedCargoLoadout(
                    loadout_nickname=nickname,
                    cargo_item=reward_prop.REWARD_ITEM,
                    hardpoints=hardpoints,
                    min=reward_prop.MIN,
                    max=reward_prop.MAX,
                    init_items=init_items,
                ).get_loadout()
                self.loadouts_list.append(loadout)
                self.loadouts_db[reward_prop.REWARD_TYPE].append(loadout)

        if self.ULTRA_REWARD_PROP:
            if self.ULTRA_REWARD_PROP.ULTRA_REWARD_ITEM is None:
                raise Exception('Ultra reward item is mandatory for ultra reward prop')

            ultra_hardpoint = random.choice(hardpoints)
            no_ultra_hardpoints = [item for item in hardpoints if item != ultra_hardpoint]

            nickname = self.LOADOUT_NICKNAME_TEMPLATE.format(
                name=self.NAME,
                reward_type='ultra',
                index=1
            )
            self.loadout_ultra_reward = DynamicAttachedCargoLoadout(
                loadout_nickname=nickname,
                cargo_item=self.ULTRA_REWARD_PROP.REWARD_ITEM,
                hardpoints=no_ultra_hardpoints,
                min=self.ULTRA_REWARD_PROP.MIN,
                max=self.ULTRA_REWARD_PROP.MAX,
                init_items=init_items,
            ).get_loadout()
            self.loadout_ultra_reward.add_cargo(
                self.ULTRA_REWARD_PROP.ULTRA_REWARD_ITEM,
                1,
                ultra_hardpoint
            )
            self.loadouts_list.append(self.loadout_ultra_reward)

    def get_loadouts(self):
        return self.loadouts_list

    def get_archetype_by_reward_type(self, reward_type):
        if reward_type == MINING_REWARD_LOW: 
            return self.asteroid_solar.DEFAULT_ARCHETYPE
        if reward_type == MINING_REWARD_MEDIUM:
            return self.asteroid_solar.ARCHETYPE_REWARD_MEDIUM
        if reward_type == MINING_REWARD_HIGH:
            return self.asteroid_solar.ARCHETYPE_REWARD_HIGH
        if reward_type == MINING_REWARD_ULTRA:
            return self.asteroid_solar.ARCHETYPE_REWARD_ULTRA

        raise Exception('unknown reward_type %s' % reward_type)

    def get_loadout_by_reward_type(self, reward_type):
        try:
            if reward_type == MINING_REWARD_ULTRA:
                return self.loadout_ultra_reward
            else:
                return random.choice(self.loadouts_db[reward_type])
        except IndexError as e:
            raise Exception('reward_type %s isnt defined for this reward group' % reward_type)

    def get_loadout_name_by_reward_type(self, reward_type):
        return self.get_loadout_by_reward_type(reward_type).get_loadout_nickname()


class RewardAsteroidField(Mineable):
    ABSTRACT = False
    FIELD_CLASS = DefaultField
    REWARDS_GROUP_CLASS = None
    FIELD_NAME = None

    MEDIUM_REWARD_CHANCE = 0
    HIGH_REWARD_CHANCE = 0
    ULTRA_REWARD = False

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

        self.mark_rewards()

        self.rewards_group = self.system.get_rewards_group_by_class(self.REWARDS_GROUP_CLASS)
        self.dummy_system_object_string = self.generate_asteroids()

    def mark_rewards(self):
        available_boxes = self.field.get_boxes_without_reward()
        box_count = len(available_boxes)
        indexes = list(range(0, box_count))

        ultra_index = None
        high_indexes = []
        medium_indexes = []

        if self.ULTRA_REWARD:
            ultra_index = random.choice(indexes)
            indexes.remove(ultra_index)

        if self.HIGH_REWARD_CHANCE > 0:
            high_count = box_count * self.HIGH_REWARD_CHANCE
            high_indexes = set(random.choices(indexes, k=int(high_count)))

            for index in high_indexes:
                indexes.remove(index)

        if self.MEDIUM_REWARD_CHANCE > 0:
            medium_count = box_count * self.MEDIUM_REWARD_CHANCE
            medium_indexes = set(random.choices(indexes, k=int(medium_count)))
            for index in medium_indexes:
                indexes.remove(index)

        for index, box in enumerate(available_boxes):
            if ultra_index and index == ultra_index:
                box.set_reward_type(MINING_REWARD_ULTRA)
            elif index in high_indexes:
                box.set_reward_type(MINING_REWARD_HIGH)
            elif index in medium_indexes:
                box.set_reward_type(MINING_REWARD_MEDIUM)


    def generate_asteroids(self):
        items = []
        index = 1

        for box in self.field.get_boxes():
            if box.is_empty:
                continue

            box_reward_type = box.get_reward_type()
            reward_type = box_reward_type if box_reward_type else MINING_REWARD_LOW


            items.append(
                self.SYSTEM_OBJECT_TEMPLATE.format(
                    nickname=self.create_nickname(index),
                    pos='{}, {}, {}'.format(*box.get_position()),
                    rotate='{}, {}, {}'.format(*box.get_rotate()),
                    archetype=self.rewards_group.get_archetype_by_reward_type(reward_type),
                    loadout=self.rewards_group.get_loadout_name_by_reward_type(reward_type)
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

        return real_object.get_instance(new_space_object_name=self.FIELD_NAME, move_to=self.POS)


# class MediumRewardField(RewardAsteroidField):
#     MEDIUM_REWARD_CHANCE = 0.4
#     HUGE_REWARD_CHANCE = 0