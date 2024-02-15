from universe.content.system_object import TOP, BOTTOM, LEFT, RIGHT
from universe.content.main_objects import Sun, Jumpgate, Dockring, Shipyard, Station, Outpost, Prison, Refinery, TradingBase, JunkerBase, PirateBase, Sattelite, TradeConnection

from templates.dockable.pirate import PirateBaseBizmark
from templates.dockable.potsdam import Potsdam
from templates.dockable.prisons import BerlinPrison
from templates.dockable.shipyards import CambridgeShipyard
from templates.dockable.alg import AlgBaseHokkaido
from templates.dockable.asteroid import BerlinAsteroidBase
from templates.dockable.junker import BerlinJunker
from templates.dockable.police import BerlinPoliceOutpost
from templates.dockable.trade_storages import TekagiStorage



# DEFAULT

# from templates.dockable.station_debris import TekagiDebris, MunchenBattleStationDebris, MunchenCivilianStationDebris, OmegaDanzigDebris, StuttgartDestroyedOutpost, ForbesDebris, ColumbiaDebris, CaliforniaDebris
# from templates.dockable.edge_world import BlackHoleResearch, BlackHoleOutpost, BlackHoleDestroyedStation, ShinobiAbandonedResearch, OchoRiosResearch, MadridProduction, CadizFreeport, NeutronResearch

# from templates.dockable.bounty_hunter import PortRoyal, ChurchAlive, ChurchDestroyed
# from templates.dockable.gmg_hq import GmgHQAlive, GmgHQDestroyed
# from templates.dockable.alg import AlgBaseHokkaido, AlgBaseBerlin



# from templates.dockable.prisons import AvalonPrison, HonshuPrison, BerlinPrison, AlaskaPrison, ColumbiaPrison
# from templates.dockable.shipyards import CambridgeShipyard, HokkaidoShipyard, StuttgartShipyard, ForbesShipyard, UlsterShipyardDestroyed, UlsterShipyardAlive, HeavyBarrelShipyard

# from templates.dockable.roid_mining import BretoniaRoidMining, RheinlandRoidMining, LibertyRoidMining, UpsilonRoidMining
# from templates.dockable.gas_miner import BretoniaPirateGasMiner, BretoniaCivilianGasMiner, RheinlandCivilianGasMiner, RheinlandPirateGasMiner, CadizGasMiner
# from templates.dockable.research import KyushuResearch, SiriusResearch, RheinlandResearch, ForbesResearch




# from templates.dockable.pirate import PirateBaseBizmark, PirateBaseHokkaido, LibertyRombicPirateBase, PirateBaseStuttgart, PirateBaseCambridge, ManhattanPirateBase, PirateBaseForbes, PirateBaseColumbia, PirateBaseCalifornia
# from templates.dockable.asteroid import KyushuAsteroidBase, NomadAsteroidBase, MunchenAsteroidBase, BizmarkAsteroidBase, BerlinAsteroidBase, ManhattanAsteroidBase, CaliforniaAsteroidBase
# from templates.dockable.junker import HonshuJunker, SigmaEightJunker, StuttgartJunker, BerlinJunker, OmegaSmelter, ForbesJunker

# from templates.dockable.trading_outposts import LibertyTradingOutpost, RheinlandTradingOutpost
# from templates.dockable.police import PoliceOutpostBretonia, SigmaEightPoliceOutpost, StuttgartPoliceOutpost, BerlinPoliceOutpost, OmicronPoliceOutpost, PoliceOutpostLiberty
# from templates.dockable.trade_storages import HokkaidoStorage, HonshuStorage, TekagiStorage, LibertyLongStorage, RheinlandOmegaStorage, ManhattanStorage



class BerlinSysObject(object):
    INDEX = 1
    FACTION = 'rh_grp'
    ABSTRACT = False



class BerlinSun(BerlinSysObject, Sun):
    STAR = 'Rh04_Sun'
    LOADOUT = 'med_blue_sun_fx'


class BerlinJumpgateTop(BerlinSysObject, Jumpgate):
    INDEX = 1
    REL = TOP


class BerlinJumpgateBottom(BerlinSysObject, Jumpgate):
    INDEX = 2
    REL = LEFT


class BerlinDockring(BerlinSysObject, Dockring):
    BASE_INDEX = 1
    REL = RIGHT


class BerlinPrison(BerlinSysObject, Prison):
    BASE_INDEX = 2
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = BerlinPrison


class BerlinMegaStation(BerlinSysObject, Station):
    BASE_INDEX = 4
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = Potsdam


class BerlinOutpost(BerlinSysObject, Outpost):
    BASE_INDEX = 6
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = BerlinPoliceOutpost


class BerlinShipyard(BerlinSysObject, Shipyard):
    BASE_INDEX = 3
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = CambridgeShipyard


class BerlinTrading(BerlinSysObject, TradingBase):
    BASE_INDEX = 9
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = TekagiStorage


class BerlinRefinery(BerlinSysObject, Refinery):
    BASE_INDEX = 7
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = AlgBaseHokkaido


class BerlinJunkers(BerlinSysObject, JunkerBase):
    BASE_INDEX = 8
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = BerlinJunker


class BerlinPiratesTop(BerlinSysObject, PirateBase):
    BASE_INDEX = 5
    INDEX = 1
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = BerlinAsteroidBase


class BerlinPiratesBottom(BerlinSysObject, PirateBase):
    BASE_INDEX = 11
    INDEX = 2
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = PirateBaseBizmark


class BerConnOutpost1(BerlinSysObject, TradeConnection):
    OBJ_FROM = BerlinOutpost
    OBJ_TO = BerlinJumpgateTop
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        BerlinPiratesTop
    ]


class BerConnOutpost2(BerlinSysObject, TradeConnection):
    OBJ_FROM = BerlinOutpost
    OBJ_TO = BerlinShipyard
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        BerlinPiratesTop
    ]


class BerConnOutpost3(BerlinSysObject, TradeConnection):
    OBJ_FROM = BerlinOutpost
    OBJ_TO = BerlinDockring
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = BOTTOM


class BerConnShipPris(BerlinSysObject, TradeConnection):
    OBJ_FROM = BerlinShipyard
    OBJ_TO = BerlinPrison
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        BerlinPiratesTop
    ]


class BerConnTrading1(BerlinSysObject, TradeConnection):
    OBJ_FROM = BerlinTrading
    OBJ_TO = BerlinPrison
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        BerlinPiratesBottom
    ]


class BerConnTrading2(BerlinSysObject, TradeConnection):
    OBJ_FROM = BerlinTrading
    OBJ_TO = BerlinJumpgateBottom
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'F'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        BerlinPiratesBottom
    ]


class BerConnTrading3(BerlinSysObject, TradeConnection):
    OBJ_FROM = BerlinTrading
    OBJ_TO = BerlinMegaStation
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'G'
    HUNTER_DEFENCE_REL = BOTTOM


class BerConnStation1(BerlinSysObject, TradeConnection):
    OBJ_FROM = BerlinMegaStation
    OBJ_TO = BerlinDockring
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'H'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        BerlinJunkers
    ]


class BerConnStation2(BerlinSysObject, TradeConnection):
    OBJ_FROM = BerlinMegaStation
    OBJ_TO = BerlinRefinery
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'I'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        BerlinJunkers
    ]
    OBJ_FROM_EXTRA_DRIFT = 5000



# class WarwickConnection2(WarwickSysObject, TradeConnection):
#     OBJ_FROM = WarwickDock
#     OBJ_TO = WarwickTradingOutpost
#     SIDE_FROM = TOP
#     SIDE_TO = BOTTOM
#     TRADELANE_LETTER = 'B'
#     HUNTER_DEFENCE_REL = LEFT
#     ATTACKED_BY = [
#         WarwickIrelandBase
#     ]


# class WarwickConnection3(WarwickSysObject, TradeConnection):
#     OBJ_FROM = WarwickDock
#     OBJ_TO = WarwickProdStation
#     SIDE_FROM = LEFT
#     SIDE_TO = RIGHT
#     TRADELANE_LETTER = 'C'


# class WarwickConnection4(WarwickSysObject, TradeConnection):
#     OBJ_FROM = WarwickProdStation
#     OBJ_TO = WarwickJumpgateRight
#     SIDE_FROM = LEFT
#     SIDE_TO = RIGHT
#     TRADELANE_LETTER = 'D'
#     HUNTER_DEFENCE_REL = BOTTOM
#     ATTACKED_BY = [
#         WarwickPirateBase
#     ]


# class WarwickConnection5(WarwickSysObject, TradeConnection):
#     OBJ_FROM = WarwickTradingOutpost
#     OBJ_TO = WarwickJumpgateBottom
#     SIDE_FROM = TOP
#     SIDE_TO = BOTTOM
#     TRADELANE_LETTER = 'E'
#     HUNTER_DEFENCE_REL = LEFT
#     ATTACKED_BY = [
#         WarwickIrelandBase
#     ]

