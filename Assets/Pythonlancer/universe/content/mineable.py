import random

from templates.space_object_template import SpaceObjectTemplate
from universe.content.system_object import SystemObject
from universe.content.loadout import DynamicAttachedCargoLoadout, DynamicInternalCargoLoadout, SingleInternalCargoLoadout, SingleAttachedItemLoadout

from text.dividers import SINGLE_DIVIDER, DIVIDER


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
            0 if self.field.ROT_X_ZERO else random.randint(self.field.ROTATE_X_MIN, self.field.ROTATE_X_MAX),
            0 if self.field.ROT_Y_ZERO else random.randint(self.field.ROTATE_Y_MIN, self.field.ROTATE_Y_MAX),
            0 if self.field.ROT_Z_ZERO else random.randint(self.field.ROTATE_Z_MIN, self.field.ROTATE_Z_MAX),
        )


class Field(object):
    ABSTRACT = True

    BOX_SIZE = 300
    BOX_Y_SIZE_OVERRIDE = 0
    DENSITY_MULTIPLER = 1
    DRIFT_X = 0.1
    DRIFT_Y = 0.1
    DRIFT_Z = 0.1
    ROTATE_X_MIN = -180
    ROTATE_X_MAX = 180
    ROTATE_Y_MIN = -180
    ROTATE_Y_MAX = 180
    ROTATE_Z_MIN = -180
    ROTATE_Z_MAX = 180
    EMPTY_CHANCE = 0
    ROT_X_ZERO = False
    ROT_Y_ZERO = False
    ROT_Z_ZERO = False

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
    EMPTY_CHANCE = 0


class BackgroundAsteroidsField(DefaultField):
    BOX_SIZE = 2500
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.3
    DRIFT_Y = 0
    DRIFT_Z = 0.3


class MineableAsteroidField(DefaultField):
    BOX_SIZE = 1500
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.3
    DRIFT_Y = 0
    DRIFT_Z = 0.3


class MineableDebrixBoxField(DefaultField):
    BOX_SIZE = 1200
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.2
    DRIFT_Y = 0
    DRIFT_Z = 0.2


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
    MAX = 2
    LOADOUTS_COUNT = 5


class DebrisBoxRewardPropsMedium(RewardProps):
    REWARD_TYPE = MINING_REWARD_MEDIUM
    MIN = 3
    MAX = 4
    LOADOUTS_COUNT = 5


class DebrisBoxRewardPropsHigh(RewardProps):
    REWARD_TYPE = MINING_REWARD_HIGH
    MIN = 5
    MAX = 7
    LOADOUTS_COUNT = 5


class DebrisBoxRewardPropsUltra(RewardProps):
    REWARD_TYPE = MINING_REWARD_ULTRA
    LOADOUTS_COUNT = 1


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

    ULTRA_REWARD_BASES = []

    NAME = 'any'
    LOADOUT_NICKNAME_TEMPLATE = '{name}_{reward_type}_loadout_{index}'

    def __init__(self, system):
        self.system = system

        self.solar = self.SOLAR()

        self.loadouts_list = []
        self.loadouts_db = {}

        self.ultra_loadouts_db = {}

        self.fill_loadouts()

    def fill_loadouts(self):
        raise NotImplementedError

    def get_loadouts(self):
        return self.loadouts_list

    def get_loadout_by_reward_type(self, reward_type, ultra_base_instance):
        try:
            if reward_type == MINING_REWARD_ULTRA:
                return self.ultra_loadouts_db[ultra_base_instance.get_base_nickname()]
            else:
                return random.choice(self.loadouts_db[reward_type])
        except KeyError as e:
            pass
            # raise Exception('reward_type %s isnt defined for reward group %s' % (reward_type, self.__class__.__name__))

    def get_loadout_name_by_reward_type(self, reward_type, ultra_base_instance):
        loadout = self.get_loadout_by_reward_type(reward_type, ultra_base_instance)
        if loadout:
            return loadout.get_loadout_nickname()

        if reward_type == MINING_REWARD_ULTRA:
            raise Exception(f'Error! Ultra reward loadout not found for {self}')
        return None

    def get_multiple_loadouts_by_reward_type(self, reward_type, count, ultra_base_instance):
        try:
            if reward_type == MINING_REWARD_ULTRA:
                additional_items_count = count - 1
                ultra_items = random.choices(self.loadouts_db[MINING_REWARD_ULTRA_ADDITIONAL], k=additional_items_count)
                ultra_items.append(self.ultra_loadouts_db[ultra_base_instance.get_base_nickname()])
                random.shuffle(ultra_items)
                return ultra_items
            else:
                return random.choices(self.loadouts_db[reward_type], k=count)
        except KeyError as e:
            raise Exception('reward_type %s isnt defined for reward group %s' % reward_type, self.__name__)

    def get_loadout_names_by_reward_type(self, reward_type, count, ultra_base_instance=None):
        return [loadout.get_loadout_nickname() for loadout in self.get_multiple_loadouts_by_reward_type(reward_type, count, ultra_base_instance)]


class MultipointRewardsGroup(RewardsGroup):
    def fill_loadouts(self):
        hardpoints = self.solar.get_hardpoints()
        init_items = self.solar.get_init_loadout_items()
        init_items_ultra = self.solar.get_init_loadout_items_ultra()

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

            for base in self.ULTRA_REWARD_BASES:
                base_instance = self.system.get_static_by_class(base)
                if not base_instance.LOCKED_DOCK:
                    raise Exception('this base is not locked')

                ultra_hardpoint = random.choice(hardpoints)
                no_ultra_hardpoints = [item for item in hardpoints if item != ultra_hardpoint]

                base_nickname = base_instance.get_base_nickname()
                base_key = base_instance.get_key_name()

                nickname = self.LOADOUT_NICKNAME_TEMPLATE.format(
                    name=self.NAME,
                    reward_type=base_nickname,
                    index=1
                )
                loadout_ultra_reward = DynamicAttachedCargoLoadout(
                    loadout_nickname=nickname,
                    cargo_item=self.REWARD_ITEM,
                    hardpoints=no_ultra_hardpoints,
                    min=self.ULTRA_REWARD_PROP.MIN,
                    max=self.ULTRA_REWARD_PROP.MAX,
                    init_items=init_items_ultra,
                ).get_loadout()
                loadout_ultra_reward.add_cargo(
                    base_key,
                    1,
                    ultra_hardpoint
                )
                self.loadouts_list.append(loadout_ultra_reward)
                self.ultra_loadouts_db[base_nickname] = loadout_ultra_reward


class SinglepointRewardsGroup(RewardsGroup):
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
            for base in self.ULTRA_REWARD_BASES:
                base_instance = self.system.get_static_by_class(base)
                if not base_instance.LOCKED_DOCK:
                    raise Exception('this base is not locked')

                base_nickname = base_instance.get_base_nickname()
                base_key = base_instance.get_key_name()

                nickname = self.LOADOUT_NICKNAME_TEMPLATE.format(
                    name=self.NAME,
                    reward_type=base_nickname,
                    index=1
                )

                drop_hardpoint = self.solar.get_drop_hardpoint()
                if drop_hardpoint:
                    loadout_ultra_reward = SingleAttachedItemLoadout(
                        loadout_nickname=nickname,
                        equip_item=base_key,
                        hardpoint=drop_hardpoint,
                        init_items=init_items,
                    ).get_loadout()
                else:
                    loadout_ultra_reward = SingleInternalCargoLoadout(
                        loadout_nickname=nickname,
                        cargo_item=base_key,
                        init_items=init_items,
                    ).get_loadout()
                self.loadouts_list.append(loadout_ultra_reward)
                self.ultra_loadouts_db[base_nickname] = loadout_ultra_reward


class DefaultAsteroidRewardsGroup(MultipointRewardsGroup):
    REWARD_PROPS = [
        AsteroidRewardPropsLow,
        AsteroidRewardPropsMedium,
        AsteroidRewardPropsHigh,
    ]
    ULTRA_REWARD_PROP = AsteroidRewardPropsUltra


class DefaultDebrisBoxRewardsGroup(MultipointRewardsGroup):
    REWARD_PROPS = [
        DebrisBoxRewardPropsLow,
        DebrisBoxRewardPropsMedium,
        DebrisBoxRewardPropsHigh,
    ]
    ULTRA_REWARD_PROP = DebrisBoxRewardPropsUltra


class DefaultGasCrystalRewardsGroup(SinglepointRewardsGroup):
    REWARD_PROPS = [
        GasCrystalRewardPropsLow,
        GasCrystalRewardPropsMedium,
        GasCrystalRewardPropsHigh,
        GasCrystalRewardPropsUltraAdditional,
    ]
    ULTRA_REWARD_PROP = GasCrystalRewardPropsUltra


class DefaultSupriseRewardsGroup(SinglepointRewardsGroup):
    REWARD_PROPS = []
    ULTRA_REWARD_PROP = SupriseRewardPropsUltra


class AsteroidRewardsGroupLow(MultipointRewardsGroup):
    REWARD_PROPS = [
        AsteroidRewardPropsLow,
    ]


class AsteroidRewardsGroupMedium(MultipointRewardsGroup):
    REWARD_PROPS = [
        AsteroidRewardPropsLow,
        AsteroidRewardPropsMedium,
    ]


class AsteroidRewardsGroupHigh(MultipointRewardsGroup):
    REWARD_PROPS = [
        AsteroidRewardPropsLow,
        AsteroidRewardPropsMedium,
        AsteroidRewardPropsHigh,
    ]


class AsteroidRewardsGroupUltra(MultipointRewardsGroup):
    REWARD_PROPS = [
        AsteroidRewardPropsLow,
        AsteroidRewardPropsMedium,
        AsteroidRewardPropsHigh,
    ]
    ULTRA_REWARD_PROP = AsteroidRewardPropsUltra


class DefaultDebrisBoxRewardsGroupLow(SinglepointRewardsGroup):
    REWARD_PROPS = [
        DebrisBoxRewardPropsLow,
    ]


class DefaultDebrisBoxRewardsGroupMedium(SinglepointRewardsGroup):
    REWARD_PROPS = [
        DebrisBoxRewardPropsLow,
        DebrisBoxRewardPropsMedium,
    ]


class DefaultDebrisBoxRewardsGroupHigh(SinglepointRewardsGroup):
    REWARD_PROPS = [
        DebrisBoxRewardPropsLow,
        DebrisBoxRewardPropsMedium,
        DebrisBoxRewardPropsHigh,
    ]


class DefaultDebrisBoxRewardsGroupUltra(SinglepointRewardsGroup):
    REWARD_PROPS = [
        DebrisBoxRewardPropsLow,
        DebrisBoxRewardPropsMedium,
        DebrisBoxRewardPropsHigh,
    ]
    ULTRA_REWARD_PROP = DebrisBoxRewardPropsUltra


class RewardField(Mineable):
    FIELD_CLASS = None
    REWARDS_GROUP_CLASS = None

    MEDIUM_REWARD_CHANCE = 0
    HIGH_REWARD_CHANCE = 0
    ULTRA_REWARD = False
    ULTRA_BASE = None

    HAS_REWARDS = True

    DUMMY_NAME = 'reward_item_dummy'

    NICKNAME_TEMPLATE = '{dummy_name}_{solar_alias}_{index}'

    def __init__(self, system):
        self.system = system

        self.ultra_base_instance = None
        if self.ULTRA_REWARD is True:
            if not self.ULTRA_BASE:
                raise Exception('RewardField have not attached base to unlock %s' % self.__class__.__name__)
            self.ultra_base_instance = self.system.get_static_by_class(self.ULTRA_BASE)

        self.field = self.FIELD_CLASS()

        if self.HAS_REWARDS:
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
            if ultra_index is not None and index == ultra_index:
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

    def generate_box_content_item(self, box, reward_type, index):
        raise NotImplementedError

    def get_solar_alias(self):
        return self.rewards_group.solar.ALIAS

    def create_nickname(self, index):
        return self.NICKNAME_TEMPLATE.format(dummy_name=self.DUMMY_NAME, solar_alias=self.get_solar_alias(), index=index)

    def get_reward_field_name(self):
        if hasattr(self, 'FIELD_NAME'):
            raise Exception('FIELD_NAME is obsolete for %s' % self.__class__.__name__)
        return '{system_name}_field_{alias}_reward_field'.format(system_name=self.system.NAME, alias=self.get_full_alias())

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
loadout = {loadout}
visit = 128'''

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
            loadout=self.rewards_group.get_loadout_name_by_reward_type(reward_type, self.ultra_base_instance)
        )


class DebrisBoxRewardField(AsteroidRewardField):
    ALIAS = 'deb'


class GasCrystalRewardField(RewardField):
    ALIAS = 'cryst'

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

        loadouts = self.rewards_group.get_loadout_names_by_reward_type(reward_type, len(gas_positions), self.ultra_base_instance)

        nickname = self.create_nickname(index)
        box_pos = box.get_position()

        asteroid = self.rewards_group.solar.get_asteroid(nickname, box_pos, asteroid_archetype)

        gas_items = []
        for index, gas_pos in enumerate(gas_positions):
            gas_items.append(
                self.rewards_group.solar.get_inner_gas_item(nickname, box_pos, gas_pos, loadouts[index], index+1)
            )

        return DIVIDER.join([asteroid] + gas_items)


class ComplexGasCrystalRewardField(GasCrystalRewardField):
    ALIAS = 'bigcryst'


class SupriseRewardField(RewardField):
    ALIAS = 'suprise'

    SYSTEM_OBJECT_TEMPLATE = '''[Object]
nickname = {nickname}
pos = {pos}
rotate = {rotate}
archetype = {archetype}'''

    def get_archetype(self):
        return self.rewards_group.solar.get_default_archetype()

    def generate_box_content_item(self, box, reward_type, index):
        sys_object = self.SYSTEM_OBJECT_TEMPLATE.format(
            nickname=self.create_nickname(index),
            pos='{}, {}, {}'.format(*box.get_position()),
            rotate='{}, {}, {}'.format(*box.get_rotate()),
            archetype=self.get_archetype(),
        )
        loadout = self.rewards_group.get_loadout_name_by_reward_type(reward_type, self.ultra_base_instance)
        if loadout:
            sys_object += SINGLE_DIVIDER + f'loadout = {loadout}'
        return sys_object


class StaticObjectField(SupriseRewardField):
    STATIC_ARCHETYPES = []
    HAS_REWARDS = False

    def get_solar_alias(self):
        return 'static'

    def get_archetype(self):
        return random.choice(self.STATIC_ARCHETYPES)

    def generate_box_content_item(self, box, reward_type, index):
        sys_object = self.SYSTEM_OBJECT_TEMPLATE.format(
            nickname=self.create_nickname(index),
            pos='{}, {}, {}'.format(*box.get_position()),
            rotate='{}, {}, {}'.format(*box.get_rotate()),
            archetype=self.get_archetype(),
        )
        return sys_object
