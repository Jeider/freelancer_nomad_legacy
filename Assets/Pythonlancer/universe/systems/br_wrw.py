# from universe.base import br_wrw_01_Base, br_wrw_02_Base, br_wrw_03_Base, br_wrw_04_Base
from universe.object import TradeConnection, TradelaneAssault, HuntersDefence, Jumpgate, Dockring, Station, TradeStation, PirateBase, TOP, BOTTOM, LEFT, RIGHT


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


class WarwickConnection2(TradeConnection, WarwickSysObject):
    OBJ_FROM = WarwickDock
    OBJ_TO = WarwickTradingOutpost
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = LEFT


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


class WarwickConnection5(TradeConnection, WarwickSysObject):
    OBJ_FROM = WarwickTradingOutpost
    OBJ_TO = WarwickJumpgateBottom
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = LEFT


class WarwickPirateTradeAttack1(TradelaneAssault, WarwickSysObject):
    LAUNCH_BASE = WarwickIrelandBase
    ATTACKED_ROUTE = WarwickConnection1


class WarwickPirateTradeAttack2(TradelaneAssault, WarwickSysObject):
    LAUNCH_BASE = WarwickIrelandBase
    ATTACKED_ROUTE = WarwickConnection2


class WarwickPirateTradeAttack3(TradelaneAssault, WarwickSysObject):
    LAUNCH_BASE = WarwickIrelandBase
    ATTACKED_ROUTE = WarwickConnection5


class WarwickHuntersDefence1(HuntersDefence, WarwickSysObject):
    DEFENCED_ROUTE = WarwickConnection1
    REL = BOTTOM


class WarwickHuntersDefence2(HuntersDefence, WarwickSysObject):
    DEFENCED_ROUTE = WarwickConnection2
    REL = LEFT


class WarwickHuntersDefence3(HuntersDefence, WarwickSysObject):
    DEFENCED_ROUTE = WarwickConnection4
    REL = BOTTOM


class WarwickHuntersDefence4(HuntersDefence, WarwickSysObject):
    DEFENCED_ROUTE = WarwickConnection4
    REL = LEFT
