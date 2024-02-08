# from universe.base import br_wrw_01_Base, br_wrw_02_Base, br_wrw_03_Base, br_wrw_04_Base
from universe.content.system_object import TOP, BOTTOM, LEFT, RIGHT
from universe.content.main_objects import TradeConnection, Jumpgate, Dockring, Station, TradeStation, PirateBase, Sattelite
from universe.content.mineable import DefaultAsteroidRewardsGroup, DefaultDebrisBoxRewardsGroup, DefaultField, AsteroidRewardField, DebrisBoxRewardField
from templates.solar.asteroid import AsteroidOmega15
from templates.solar.debris_box import DebrisBox
from templates.dockable.pirate import PirateBaseBizmark


class WarwickSysObject(object):
    FACTION = 'br_grp'
    ABSTRACT = False


class WarwickJumpgateLeft(WarwickSysObject, Jumpgate):
    POS = (-60000, 0, -15000)
    REL = LEFT


class WarwickJumpgateRight(WarwickSysObject, Jumpgate):
    POS = (55000, 0, -35000)
    REL = LEFT


class WarwickJumpgateBottom(WarwickSysObject, Jumpgate):
    POS = (-27000, 0, 45000)
    REL = LEFT


class WarwickDock(WarwickSysObject, Dockring):
    POS = (-25000, 0, -25000)
    REL = TOP


class WarwickProdStation(WarwickSysObject, Station):
    POS = (25000, 0, -25000)
    REL = TOP


class WarwickTradingOutpost(WarwickSysObject, TradeStation):
    POS = (-20000, 0, 10000)
    REL = LEFT


class WarwickIrelandBase(WarwickSysObject, PirateBase):
    POS = (-45000, 0, 20000)
    REL = LEFT
    # SPACE_OBJECT_TEMPLATE = PirateBaseBizmark
    # SPACE_OBJECT_NAME = 'br_wrw_10'


class WarwickPirateBase(WarwickSysObject, PirateBase):
    POS = (50000, 0, -5000)
    REL = RIGHT


class WarwickConnection1(WarwickSysObject, TradeConnection):
    OBJ_FROM = WarwickJumpgateLeft
    OBJ_TO = WarwickDock
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        WarwickIrelandBase
    ]


class WarwickConnection2(WarwickSysObject, TradeConnection):
    OBJ_FROM = WarwickDock
    OBJ_TO = WarwickTradingOutpost
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        WarwickIrelandBase
    ]


class WarwickConnection3(WarwickSysObject, TradeConnection):
    OBJ_FROM = WarwickDock
    OBJ_TO = WarwickProdStation
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'C'


class WarwickConnection4(WarwickSysObject, TradeConnection):
    OBJ_FROM = WarwickProdStation
    OBJ_TO = WarwickJumpgateRight
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        WarwickPirateBase
    ]


class WarwickConnection5(WarwickSysObject, TradeConnection):
    OBJ_FROM = WarwickTradingOutpost
    OBJ_TO = WarwickJumpgateBottom
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        WarwickIrelandBase
    ]


class Omega15NiobiumAsteroid(WarwickSysObject, DefaultAsteroidRewardsGroup):
    NAME = 'om15_niobium'
    SOLAR = AsteroidOmega15
    REWARD_ITEM = 'comm_roid_niobium'
    ULTRA_REWARD_ITEM = 'rh_lightgun01'


class DebrisBoxCheckField(WarwickSysObject, DefaultDebrisBoxRewardsGroup):
    NAME = 'debris_box_check'
    SOLAR = DebrisBox
    REWARD_ITEM = 'comm_scrap_metal'
    ULTRA_REWARD_ITEM = 'rh_shieldgun09'


class WarwickField1(DefaultField):
    BOX_SIZE = 1000
    DENSITY_MULTIPLER = 3


class WarwickField2(DefaultField):
    BOX_SIZE = 500
    DENSITY_MULTIPLER = 3
    DRIFT_X = 0.3
    DRIFT_Y = 0.2
    DRIFT_Z = 0.3
    ROTATE_MIN = 0
    ROTATE_MAX = 0
    EMPTY_CHANCE = 0


# class AsteroidFieldOne(WarwickSysObject, AsteroidRewardField):
#     POS = (5000, 0, 20000)
#     FIELD_NAME = 'om15_field1'
#     FIELD_CLASS = WarwickField1
#     REWARDS_GROUP_CLASS = Omega15NiobiumAsteroid
#     MEDIUM_REWARD_CHANCE = 0.5
#     HIGH_REWARD_CHANCE = 0.25
#     ULTRA_REWARD = True


class DebrisBoxSuperField(WarwickSysObject, DebrisBoxRewardField):
    POS = (20000, 0, 10000)
    FIELD_NAME = 'om15_field2'
    FIELD_CLASS = WarwickField2
    REWARDS_GROUP_CLASS = DebrisBoxCheckField
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True





    # MINING_ULTRA_REWARD = 'rh_lightgun01'
    # 

