import random

from templates.space_object_template import SpaceObjectTemplate
from universe.content.system_object import SystemObject
from universe.content.loadout import DynamicAttachedCargoLoadout, DynamicInternalCargoLoadout, SingleInternalCargoLoadout

from text.dividers import DIVIDER


MINING_REWARD_LOW = 'low'
MINING_REWARD_MEDIUM = 'medium'
MINING_REWARD_HIGH = 'high'
MINING_REWARD_ULTRA = 'ultra'
MINING_REWARD_ULTRA_ADDITIONAL = 'ultra_additional'


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

        y_size = self.field.BOX_Y_SIZE_OVERRIDE if self.field.BOX_Y_SIZE_OVERRIDE > 0 else self.box_size

        self.drift_x = int(self.center_append * self.field.DRIFT_X)
        self.drift_y = int(y_size * self.field.DRIFT_Y)
        self.drift_z = int(self.center_append * self.field.DRIFT_Z)

    def mark_as_empty(self):
        self.is_empty = True

    def set_reward_type(self, reward_type):
        self.reward_type = reward_type

    def get_reward_type(self):
        return self.reward_type

    def get_position(self, x_adjust=0, y_adjust=0, z_adjust=0):
        center_x = self.left_x + self.center_append + random.randint(-abs(self.drift_x), self.drift_x)
        center_y = 0 + random.randint(-abs(self.drift_y), self.drift_y)
        center_z = self.top_z + self.center_append + random.randint(-abs(self.drift_z), self.drift_z)

        return (center_x + x_adjust, center_y + y_adjust, center_z + z_adjust)

    def get_rotate(self):
        return (
            random.randint(self.field.ROTATE_MIN, self.field.ROTATE_MAX),
            random.randint(self.field.ROTATE_MIN, self.field.ROTATE_MAX),
            random.randint(self.field.ROTATE_MIN, self.field.ROTATE_MAX),
        )


class Field(object):
    ABSTRACT = True

    BOX_SIZE = 300
    BOX_Y_SIZE_OVERRIDE = 0
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

        empty_count = int(len(self.boxes) * self.EMPTY_CHANCE)
        empty_boxes = random.choices(self.boxes, k=empty_count)
        for box in empty_boxes:
            box.mark_as_empty()


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
    ABSTRACT = True

    REWARD_TYPE = None
    MIN = 1
    MAX = 2
    LOADOUTS_COUNT = 1


class AsteroidRewardPropsLow(RewardProps):
    REWARD_TYPE = MINING_REWARD_LOW
    MIN = 1
    MAX = 2
    LOADOUTS_COUNT = 5


class AsteroidRewardPropsMedium(RewardProps):
    REWARD_TYPE = MINING_REWARD_MEDIUM
    MIN = 2
    MAX = 4
    LOADOUTS_COUNT = 5


class AsteroidRewardPropsHigh(RewardProps):
    REWARD_TYPE = MINING_REWARD_HIGH
    MIN = 4
    MAX = 8
    LOADOUTS_COUNT = 5


class AsteroidRewardPropsUltra(RewardProps):
    REWARD_TYPE = MINING_REWARD_ULTRA
    MIN = 8
    MAX = 10
    LOADOUTS_COUNT = 1


class DebrisBoxRewardPropsLow(RewardProps):
    REWARD_TYPE = MINING_REWARD_LOW
    MIN = 1
    MAX = 3
    LOADOUTS_COUNT = 10


class DebrisBoxRewardPropsMedium(RewardProps):
    REWARD_TYPE = MINING_REWARD_MEDIUM
    MIN = 5
    MAX = 10
    LOADOUTS_COUNT = 10


class DebrisBoxRewardPropsHigh(RewardProps):
    REWARD_TYPE = MINING_REWARD_HIGH
    MIN = 10
    MAX = 20
    LOADOUTS_COUNT = 10


class DebrisBoxRewardPropsUltra(RewardProps):
    REWARD_TYPE = MINING_REWARD_ULTRA
    LOADOUTS_COUNT = 1


class DebrisBoxRewardPropsUltraAdditional(RewardProps):
    REWARD_TYPE = MINING_REWARD_ULTRA_ADDITIONAL
    MIN = 10
    MAX = 25
    LOADOUTS_COUNT = 10


class GasCrystalRewardPropsLow(RewardProps):
    REWARD_TYPE = MINING_REWARD_LOW
    MIN = 1
    MAX = 3
    LOADOUTS_COUNT = 10


class GasCrystalRewardPropsMedium(RewardProps):
    REWARD_TYPE = MINING_REWARD_MEDIUM
    MIN = 5
    MAX = 10
    LOADOUTS_COUNT = 10


class GasCrystalRewardPropsHigh(RewardProps):
    REWARD_TYPE = MINING_REWARD_HIGH
    MIN = 10
    MAX = 20
    LOADOUTS_COUNT = 10


class GasCrystalRewardPropsUltra(RewardProps):
    REWARD_TYPE = MINING_REWARD_ULTRA
    LOADOUTS_COUNT = 1


class GasCrystalRewardPropsUltraAdditional(RewardProps):
    REWARD_TYPE = MINING_REWARD_ULTRA_ADDITIONAL
    MIN = 10
    MAX = 25
    LOADOUTS_COUNT = 10


class SupriseRewardPropsLow(RewardProps):
    REWARD_TYPE = MINING_REWARD_LOW
    MIN = 1
    MAX = 3
    LOADOUTS_COUNT = 5


class SupriseRewardPropsUltra(RewardProps):
    REWARD_TYPE = MINING_REWARD_ULTRA
    LOADOUTS_COUNT = 1


class RewardsGroup(object):
    ABSTRACT = True

    REWARD_PROPS = []
    ULTRA_REWARD_PROP = None
    SOLAR = None

    REWARD_ITEM = None
    ULTRA_REWARD_ITEM = None

    NAME = 'any'
    LOADOUT_NICKNAME_TEMPLATE = '{name}_{reward_type}_loadout_{index}'

    def __init__(self):
        self.solar = self.SOLAR()

        self.loadouts_list = []
        self.loadouts_db = {}

        self.loadout_ultra_reward = None

        self.fill_loadouts()

    def fill_loadouts(self):
        raise NotImplementedError

    def get_loadouts(self):
        return self.loadouts_list

    def get_loadout_by_reward_type(self, reward_type):
        try:
            if reward_type == MINING_REWARD_ULTRA:
                return self.loadout_ultra_reward
            else:
                return random.choice(self.loadouts_db[reward_type])
        except KeyError as e:
            raise Exception('reward_type %s isnt defined for reward group %s' % (reward_type, self.__class__.__name__))

    def get_loadout_name_by_reward_type(self, reward_type):
        return self.get_loadout_by_reward_type(reward_type).get_loadout_nickname()

    def get_multiple_loadouts_by_reward_type(self, reward_type, count):
        try:
            if reward_type == MINING_REWARD_ULTRA:
                additional_items_count = count - 1
                ultra_items = random.choices(self.loadouts_db[MINING_REWARD_ULTRA_ADDITIONAL], k=count)
                ultra_items.append(self.loadout_ultra_reward)
                random.shuffle(ultra_items)
                return ultra_items
            else:
                return random.choices(self.loadouts_db[reward_type], k=count)
        except KeyError as e:
            raise Exception('reward_type %s isnt defined for reward group %s' % reward_type, self.__name__)

    def get_loadout_names_by_reward_type(self, reward_type, count):
        return [loadout.get_loadout_nickname() for loadout in self.get_multiple_loadouts_by_reward_type(reward_type, count)]


class HardpointRewardsGroup(RewardsGroup):
    def fill_loadouts(self):
        hardpoints = self.solar.get_hardpoints()
        init_items = self.solar.get_init_loadout_items()

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
                    cargo_item=self.REWARD_ITEM,
                    hardpoints=hardpoints,
                    min=reward_prop.MIN,
                    max=reward_prop.MAX,
                    init_items=init_items,
                ).get_loadout()
                self.loadouts_list.append(loadout)
                self.loadouts_db[reward_prop.REWARD_TYPE].append(loadout)

        if self.ULTRA_REWARD_PROP:
            if self.ULTRA_REWARD_ITEM is None:
                raise Exception('Ultra reward item is mandatory for ultra reward prop')

            ultra_hardpoint = random.choice(hardpoints)
            no_ultra_hardpoints = [item for item in hardpoints if item != ultra_hardpoint]

            nickname = self.LOADOUT_NICKNAME_TEMPLATE.format(
                name=self.NAME,
                reward_type=MINING_REWARD_ULTRA,
                index=1
            )
            self.loadout_ultra_reward = DynamicAttachedCargoLoadout(
                loadout_nickname=nickname,
                cargo_item=self.REWARD_ITEM,
                hardpoints=no_ultra_hardpoints,
                min=self.ULTRA_REWARD_PROP.MIN,
                max=self.ULTRA_REWARD_PROP.MAX,
                init_items=init_items,
            ).get_loadout()
            self.loadout_ultra_reward.add_cargo(
                self.ULTRA_REWARD_ITEM,
                1,
                ultra_hardpoint
            )
            self.loadouts_list.append(self.loadout_ultra_reward)


class InternalRewardsGroup(RewardsGroup):

    def fill_loadouts(self):
        init_items = self.solar.get_init_loadout_items()

        for reward_prop in self.REWARD_PROPS:
            self.loadouts_db[reward_prop.REWARD_TYPE] = []
            for i in range(1, reward_prop.LOADOUTS_COUNT + 1):
                nickname = self.LOADOUT_NICKNAME_TEMPLATE.format(
                    name=self.NAME,
                    reward_type=reward_prop.REWARD_TYPE,
                    index=i
                )
                loadout = DynamicInternalCargoLoadout(
                    loadout_nickname=nickname,
                    cargo_item=self.REWARD_ITEM,
                    min=reward_prop.MIN,
                    max=reward_prop.MAX,
                    init_items=init_items,
                ).get_loadout()
                self.loadouts_list.append(loadout)
                self.loadouts_db[reward_prop.REWARD_TYPE].append(loadout)

        if self.ULTRA_REWARD_PROP:
            if self.ULTRA_REWARD_ITEM is None:
                raise Exception('Ultra reward item is mandatory for ultra reward prop')

            nickname = self.LOADOUT_NICKNAME_TEMPLATE.format(
                name=self.NAME,
                reward_type=MINING_REWARD_ULTRA,
                index=1
            )
            self.loadout_ultra_reward = SingleInternalCargoLoadout(
                loadout_nickname=nickname,
                cargo_item=self.ULTRA_REWARD_ITEM,
                init_items=init_items,
            ).get_loadout()
            self.loadouts_list.append(self.loadout_ultra_reward)


class DefaultAsteroidRewardsGroup(HardpointRewardsGroup):
    REWARD_PROPS = [
        AsteroidRewardPropsLow,
        AsteroidRewardPropsMedium,
        AsteroidRewardPropsHigh,
    ]
    ULTRA_REWARD_PROP = AsteroidRewardPropsUltra


class DefaultDebrisBoxRewardsGroup(InternalRewardsGroup):
    REWARD_PROPS = [
        DebrisBoxRewardPropsLow,
        DebrisBoxRewardPropsMedium,
        DebrisBoxRewardPropsHigh,
        DebrisBoxRewardPropsUltraAdditional,
    ]
    ULTRA_REWARD_PROP = DebrisBoxRewardPropsUltra


class DefaultGasCrystalRewardsGroup(InternalRewardsGroup):
    REWARD_PROPS = [
        GasCrystalRewardPropsLow,
        GasCrystalRewardPropsMedium,
        GasCrystalRewardPropsHigh,
        GasCrystalRewardPropsUltraAdditional,
    ]
    ULTRA_REWARD_PROP = GasCrystalRewardPropsUltra


class DefaultSupriseRewardsGroup(InternalRewardsGroup):
    REWARD_PROPS = [
        GasCrystalRewardPropsLow,
    ]
    ULTRA_REWARD_PROP = GasCrystalRewardPropsUltra


class AsteroidRewardsGroupLow(HardpointRewardsGroup):
    REWARD_PROPS = [
        AsteroidRewardPropsLow,
    ]


class AsteroidRewardsGroupMedium(HardpointRewardsGroup):
    REWARD_PROPS = [
        AsteroidRewardPropsLow,
        AsteroidRewardPropsMedium,
    ]


class AsteroidRewardsGroupHigh(HardpointRewardsGroup):
    REWARD_PROPS = [
        AsteroidRewardPropsLow,
        AsteroidRewardPropsMedium,
        AsteroidRewardPropsHigh,
    ]


class AsteroidRewardsGroupUltra(HardpointRewardsGroup):
    REWARD_PROPS = [
        AsteroidRewardPropsLow,
        AsteroidRewardPropsMedium,
        AsteroidRewardPropsHigh,
    ]
    ULTRA_REWARD_PROP = AsteroidRewardPropsUltra


class DefaultDebrisBoxRewardsGroupLow(InternalRewardsGroup):
    REWARD_PROPS = [
        DebrisBoxRewardPropsLow,
    ]


class DefaultDebrisBoxRewardsGroupMedium(InternalRewardsGroup):
    REWARD_PROPS = [
        DebrisBoxRewardPropsLow,
        DebrisBoxRewardPropsMedium,
    ]


class DefaultDebrisBoxRewardsGroupHigh(InternalRewardsGroup):
    REWARD_PROPS = [
        DebrisBoxRewardPropsLow,
        DebrisBoxRewardPropsMedium,
        DebrisBoxRewardPropsHigh,
    ]


class DefaultDebrisBoxRewardsGroupUltra(InternalRewardsGroup):
    REWARD_PROPS = [
        DebrisBoxRewardPropsLow,
        DebrisBoxRewardPropsMedium,
        DebrisBoxRewardPropsHigh,
        DebrisBoxRewardPropsUltraAdditional,
    ]
    ULTRA_REWARD_PROP = DebrisBoxRewardPropsUltra


class RewardField(Mineable):
    FIELD_CLASS = None
    REWARDS_GROUP_CLASS = None
    FIELD_NAME = None

    MEDIUM_REWARD_CHANCE = 0
    HIGH_REWARD_CHANCE = 0
    ULTRA_REWARD = False

    DUMMY_NAME = 'reward_item_dummy'

    NICKNAME_TEMPLATE = '{dummy_name}_{solar_alias}_{index}'

    def __init__(self, system):
        self.system = system
        self.field = self.FIELD_CLASS()

        self.mark_rewards()

        self.rewards_group = self.system.get_rewards_group_by_class(self.REWARDS_GROUP_CLASS)
        self.dummy_system_object_string = self.generate_box_content()

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

    def generate_box_content(self):
        items = []

        for index, box in enumerate(self.field.get_boxes(), start=1):
            if box.is_empty:
                continue

            box_reward_type = box.get_reward_type()
            reward_type = box_reward_type if box_reward_type else MINING_REWARD_LOW

            items.append(
                self.generate_box_content_item(box, reward_type, index)
            )

        return DIVIDER.join(items)

    def generate_box_content_item(self):
        raise NotImplementedError

    def create_nickname(self, index):
        return self.NICKNAME_TEMPLATE.format(dummy_name=self.DUMMY_NAME, solar_alias=self.rewards_group.solar.ALIAS, index=index)

    def get_reward_field_name(self):
        if self.FIELD_NAME:
            return self.FIELD_NAME
        else:
            return '{system_name}_field_{alias}_test'.format(system_name=self.system.NAME, alias=self.get_full_alias())

    def get_system_content(self):
        real_object = SpaceObjectTemplate(
            template=self.dummy_system_object_string,
            space_object_name=self.DUMMY_NAME,
        )

        return real_object.get_instance(new_space_object_name=self.get_reward_field_name(), move_to=self.get_position())


class AsteroidRewardField(RewardField):
    ALIAS = 'ast'

    SYSTEM_OBJECT_TEMPLATE = '''[Object]
nickname = {nickname}
pos = {pos}
rotate = {rotate}
archetype = {archetype}
loadout = {loadout}'''

    def get_archetype_by_reward_type(self, reward_type):
        if reward_type == MINING_REWARD_LOW: 
            return self.rewards_group.solar.get_default_archetype()
        if reward_type == MINING_REWARD_MEDIUM:
            return self.rewards_group.solar.get_medium_reward_archetype()
        if reward_type == MINING_REWARD_HIGH:
            return self.rewards_group.solar.get_high_reward_archetype()
        if reward_type == MINING_REWARD_ULTRA:
            return self.rewards_group.solar.get_ultra_reward_archetype()

        raise Exception('unknown reward_type %s' % reward_type)

    def generate_box_content_item(self, box, reward_type, index):
        return self.SYSTEM_OBJECT_TEMPLATE.format(
            nickname=self.create_nickname(index),
            pos='{}, {}, {}'.format(*box.get_position()),
            rotate='{}, {}, {}'.format(*box.get_rotate()),
            archetype=self.get_archetype_by_reward_type(reward_type),
            loadout=self.rewards_group.get_loadout_name_by_reward_type(reward_type)
        )


class DebrisBoxRewardField(RewardField):
    ALIAS = 'deb'

    SYSTEM_OBJECT_TEMPLATE = '''[Object]
nickname = {nickname}_box01
pos = {pos_1}
rotate = 0, 0, 0
archetype = {archetype}
loadout = {loadout_1}

[Object]
nickname = {nickname}_box02
pos = {pos_2}
rotate = 0, 90, 0
archetype = {archetype}
loadout = {loadout_2}

[Object]
nickname = {nickname}_box03
pos = {pos_3}
rotate = 0, 180, 0
archetype = {archetype}
loadout = {loadout_3}

[Object]
nickname = {nickname}_box04
pos = {pos_4}
rotate = 0, -90, 0
archetype = {archetype}
loadout = {loadout_4}

[Object]
nickname = {nickname}_box05
pos = {pos_5}
rotate = 180, -90, 0
archetype = {archetype}
loadout = {loadout_5}

[Object]
nickname = {nickname}_box06
pos = {pos_6}
rotate = 180, 0, 0
archetype = {archetype}
loadout = {loadout_6}

[Object]
nickname = {nickname}_box07
pos = {pos_7}
rotate = 180, 90, 0
archetype = {archetype}
loadout = {loadout_7}

[Object]
nickname = {nickname}_box08
pos = {pos_8}
rotate = 180, 180, 0
archetype = {archetype}
loadout = {loadout_8}'''

    POSITIONS = [
        (0, 0, 0),
        (0, 0, -5),
        (-5, 0, -5),
        (-5, 0, 0),
        (0, -0.5, 0),
        (0, -0.5, -5),
        (-5, -0.5, -5),
        (-5, -0.5, 0),
    ]

    # POSITIONS = [
    #     (0, 0, 0),
    #     (0, 0, -4.8),
    #     (-4.8, 0, -4.8),
    #     (-4.8, 0, 0),
    #     (0, -0.1, 0),
    #     (0, -0.1, -4.8),
    #     (-4.8, -0.1, -4.8),
    #     (-4.8, -0.1, 0),
    # ]


    ITEMS_COUNT = 8

    POS_KEY_TEMPLATE = 'pos_{i}'
    LOADOUT_KEY_TEMPLATE = 'loadout_{i}'

    def get_archetype_by_reward_type(self, reward_type):
        if reward_type == MINING_REWARD_LOW: 
            return self.rewards_group.solar.get_default_archetype()
        if reward_type == MINING_REWARD_MEDIUM:
            return self.rewards_group.solar.get_medium_reward_archetype()
        if reward_type == MINING_REWARD_HIGH:
            return self.rewards_group.solar.get_high_reward_archetype()
        if reward_type == MINING_REWARD_ULTRA:
            return self.rewards_group.solar.get_ultra_reward_archetype()

        raise Exception('unknown reward_type %s' % reward_type)

    def generate_box_content_item(self, box, reward_type, index):
        archetype = self.get_archetype_by_reward_type(reward_type)
        loadouts = self.rewards_group.get_loadout_names_by_reward_type(reward_type, self.ITEMS_COUNT)

        template_params = {
            'nickname': self.create_nickname(index),
            'archetype': archetype,
        }

        box_pos = box.get_position()

        for i in range(1, self.ITEMS_COUNT + 1):
            item_key = i-1
            i_pos_x, i_pos_y, i_pos_z = self.POSITIONS[item_key]
            pos_x = box_pos[0] + i_pos_x
            pos_y = box_pos[1] + i_pos_y
            pos_z = box_pos[2] + i_pos_z
            template_params[self.POS_KEY_TEMPLATE.format(i=i)] = '{}, {}, {}'.format(pos_x, pos_y, pos_z)
            template_params[self.LOADOUT_KEY_TEMPLATE.format(i=i)] = loadouts[item_key]

        return self.SYSTEM_OBJECT_TEMPLATE.format(**template_params)


class GasCrystalRewardField(RewardField):
    ALIAS = 'crystal'

    def get_asteroid_archetype_by_reward_type(self, reward_type):
        if reward_type == MINING_REWARD_LOW: 
            return self.rewards_group.solar.get_default_archetype()
        if reward_type == MINING_REWARD_MEDIUM:
            return self.rewards_group.solar.get_medium_reward_archetype()
        if reward_type == MINING_REWARD_HIGH:
            return self.rewards_group.solar.get_high_reward_archetype()
        if reward_type == MINING_REWARD_ULTRA:
            return self.rewards_group.solar.get_ultra_reward_archetype()

        raise Exception('unknown reward_type %s' % reward_type)

    def generate_box_content_item(self, box, reward_type, index):
        self.rewards_group.solar.change_template()
        asteroid_archetype = self.get_asteroid_archetype_by_reward_type(reward_type)
        gas_positions = self.rewards_group.solar.get_gas_positions()
        loadouts = self.rewards_group.get_loadout_names_by_reward_type(reward_type, len(gas_positions))

        nickname = self.create_nickname(index)
        box_pos = box.get_position()


        asteroid = self.rewards_group.solar.get_asteroid(nickname, box_pos, asteroid_archetype)

        gas_items = []
        for index, gas_pos in enumerate(gas_positions):
            gas_items.append(
                self.rewards_group.solar.get_inner_gas_item(nickname, box_pos, gas_pos, loadouts[index], index+1)
            )

        return DIVIDER.join([asteroid] + gas_items)


class SupriseRewardField(RewardField):
    ALIAS = 'suprise'

    SYSTEM_OBJECT_TEMPLATE = '''[Object]
nickname = {nickname}
pos = {pos}
rotate = {rotate}
archetype = {archetype}
loadout = {loadout}'''

    def get_archetype(self):
        return self.rewards_group.solar.get_default_archetype()

    def generate_box_content_item(self, box, reward_type, index):
        return self.SYSTEM_OBJECT_TEMPLATE.format(
            nickname=self.create_nickname(index),
            pos='{}, {}, {}'.format(*box.get_position()),
            rotate='{}, {}, {}'.format(*box.get_rotate()),
            archetype=self.get_archetype(),
            loadout=self.rewards_group.get_loadout_name_by_reward_type(reward_type)
        )
