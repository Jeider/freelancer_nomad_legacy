# from universe.base import br_wrw_01_Base, br_wrw_02_Base, br_wrw_03_Base, br_wrw_04_Base
from universe.content.system_object import TOP, BOTTOM, LEFT, RIGHT
from universe.content.main_objects import TradeConnection, Jumpgate, Dockring, Station, TradeStation, PirateBase, Sattelite
from universe.content.mineable import RewardsGroup, RewardAsteroidField
from templates.solar.asteroid import AsteroidOmega15
from templates.dockable.pirate import PirateBaseBizmark


class WarwickSysObject(object):
    FACTION = 'br_grp'


class WarwickJumpgateLeft(Jumpgate, WarwickSysObject):
    POS = (-60000, 0, -15000)
    REL = LEFT


class WarwickJumpgateRight(Jumpgate, WarwickSysObject):
    POS = (55000, 0, -35000)
    REL = LEFT


class WarwickJumpgateBottom(Jumpgate, WarwickSysObject):
    POS = (-27000, 0, 45000)
    REL = LEFT


class WarwickDock(Dockring, WarwickSysObject):
    POS = (-25000, 0, -25000)
    REL = TOP


class WarwickProdStation(Station, WarwickSysObject):
    POS = (25000, 0, -25000)
    REL = TOP


class WarwickTradingOutpost(TradeStation, WarwickSysObject):
    POS = (-20000, 0, 10000)
    REL = LEFT


class WarwickIrelandBase(PirateBase, WarwickSysObject):
    POS = (-45000, 0, 20000)
    REL = LEFT
    # SPACE_OBJECT_TEMPLATE = PirateBaseBizmark
    # SPACE_OBJECT_NAME = 'br_wrw_10'


class WarwickPirateBase(PirateBase, WarwickSysObject):
    POS = (50000, 0, -5000)
    REL = RIGHT


class WarwickConnection1(TradeConnection, WarwickSysObject):
    OBJ_FROM = WarwickJumpgateLeft
    OBJ_TO = WarwickDock
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        WarwickIrelandBase
    ]


class WarwickConnection2(TradeConnection, WarwickSysObject):
    OBJ_FROM = WarwickDock
    OBJ_TO = WarwickTradingOutpost
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        WarwickIrelandBase
    ]


class WarwickConnection3(TradeConnection, WarwickSysObject):
    OBJ_FROM = WarwickDock
    OBJ_TO = WarwickProdStation
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'C'


class WarwickConnection4(TradeConnection, WarwickSysObject):
    OBJ_FROM = WarwickProdStation
    OBJ_TO = WarwickJumpgateRight
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        WarwickPirateBase
    ]


class WarwickConnection5(TradeConnection, WarwickSysObject):
    OBJ_FROM = WarwickTradingOutpost
    OBJ_TO = WarwickJumpgateBottom
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        WarwickIrelandBase
    ]


class Omega15NiobiumAsteroid(RewardsGroup):
    NAME = 'om15_niobium'
    ASTEROID_SOLAR = AsteroidOmega15


class AsteroidFieldOne(RewardAsteroidField, WarwickSysObject):
    POS = (5000, 0, 20000)
    FIELD_NAME = 'om15_field1'
    REWARDS_GROUP_CLASS = Omega15NiobiumAsteroid
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True

    # MINING_ULTRA_REWARD = 'rh_lightgun01'
    # 

