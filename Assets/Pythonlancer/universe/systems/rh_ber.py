from fx.space import Dust
from fx.sound import Ambience

from universe.content.system_object import TOP, BOTTOM, LEFT, RIGHT
from universe.content.main_objects import RawText, Sun, Planet, Jumpgate, Dockring, Shipyard, Station, Outpost, Prison, Refinery, TradingBase, JunkerBase, PirateBase, Sattelite, TradeConnection
from universe.content.zones import AsteroidZone, DebrisZone, NebulaZone
from universe.content import interior

from templates.dockable.pirate import PirateBaseBizmark
from templates.dockable.potsdam import Potsdam
from templates.dockable.prisons import BerlinPrison
from templates.dockable.shipyards import CambridgeShipyard
from templates.dockable.alg import AlgBaseHokkaido
from templates.dockable.asteroid import BerlinAsteroidBase
from templates.dockable.junker import BerlinJunker
from templates.dockable.police import BerlinPoliceOutpost
from templates.dockable.trade_storages import TekagiStorage

from universe.content.mineable import DefaultAsteroidRewardsGroup, DefaultDebrisBoxRewardsGroup, DefaultField, AsteroidRewardField, DebrisBoxRewardField, AsteroidRewardsGroupMedium, DefaultDebrisBoxRewardsGroupUltra

from templates.solar.asteroid import AsteroidOmega15
from templates.solar.debris_box import DebrisBox

from universe.content.asteroid_definition import Omega15AsteroidDefinition




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


# BerlinMember ? 
class BerlinSysObject(object):
    INDEX = 1
    FACTION = 'rh_grp'
    ABSTRACT = False


class BerlinPirateAsteroidReward(BerlinSysObject, AsteroidRewardsGroupMedium):
    NAME = 'rh_ber_rock'
    SOLAR = AsteroidOmega15
    REWARD_ITEM = 'comm_roid_niobium'


class BerlinDebrisBoxReward(BerlinSysObject, DefaultDebrisBoxRewardsGroup):
    NAME = 'rh_ber_debrisbox'
    SOLAR = DebrisBox
    REWARD_ITEM = 'comm_scrap_metal'
    ULTRA_REWARD_ITEM = 'rh_shieldgun09'


class BerlinAstField(DefaultField):
    BOX_SIZE = 3000
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.3
    DRIFT_Y = 0
    DRIFT_Z = 0.3


class BerlinDebrisField(DefaultField):
    BOX_SIZE = 1200
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.2
    DRIFT_Y = 0.1
    DRIFT_Z = 0.2


class BerlinPirateAsteroids(BerlinSysObject, AsteroidRewardField):
    INDEX = 1
    FIELD_CLASS = BerlinAstField
    REWARDS_GROUP_CLASS = BerlinPirateAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25


# class BerlinDebrisBoxMediumField(BerlinSysObject, DebrisBoxRewardField):
#     INDEX = 1
#     FIELD_CLASS = WarwickField2
#     REWARDS_GROUP_CLASS = BerlinDebrisBoxReward
#     MEDIUM_REWARD_CHANCE = 0.5
#     HIGH_REWARD_CHANCE = 0.25
#     ULTRA_REWARD = False


# class BerlinDebrisBoxHighField1(BerlinSysObject, DebrisBoxRewardField):
#     INDEX = 1
#     FIELD_CLASS = BerlinDebrisField
#     REWARDS_GROUP_CLASS = BerlinDebrisBoxReward
#     MEDIUM_REWARD_CHANCE = 0.5
#     HIGH_REWARD_CHANCE = 0.25
#     ULTRA_REWARD = False

class BerlinDebrisBoxHighField2(BerlinSysObject, DebrisBoxRewardField):
    INDEX = 2
    FIELD_CLASS = BerlinDebrisField
    REWARDS_GROUP_CLASS = BerlinDebrisBoxReward
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = False


class BerlinDebrisBoxHighField3(BerlinSysObject, DebrisBoxRewardField):
    INDEX = 3
    FIELD_CLASS = BerlinDebrisField
    REWARDS_GROUP_CLASS = BerlinDebrisBoxReward
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = False


class BerlinDebrisBoxHighField4(BerlinSysObject, DebrisBoxRewardField):
    INDEX = 4
    FIELD_CLASS = BerlinDebrisField
    REWARDS_GROUP_CLASS = BerlinDebrisBoxReward
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = False


class BerlinPirateAsteroidDefinition(Omega15AsteroidDefinition):
    ABSTRACT = False
    NAME = 'rh_ber_pirate_astfield'
    DYNAST = True
    BELT = False
    BILLBOARDS = False
    LOOT = False  # TEMP


class BerlinAsteroidZone1(BerlinSysObject, AsteroidZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = BerlinPirateAsteroidDefinition


class BerlinDebrisZone1(BerlinSysObject, DebrisZone):
    INDEX = 1


class BerlinDebrisZone2(BerlinSysObject, DebrisZone):
    INDEX = 2


class BerlinDebrisZone3(BerlinSysObject, DebrisZone):
    INDEX = 3


class BerlinDebrisZone4(BerlinSysObject, DebrisZone):
    INDEX = 4


class BerlinDebrisZone5(BerlinSysObject, DebrisZone):
    INDEX = 5


class BerlinTopNebula(BerlinSysObject, NebulaZone):
    INDEX = 1
    FILE_NAME = 'rh_ber_blue_nebula'
    SPACEDUST = Dust.ATTRACT
    SPACEDUST_MAXPARTICLES = 50
    MUSIC = Ambience.AST_ROCK


# class BerlinDebrisBoxUltraField(BerlinSysObject, DebrisBoxRewardField):
#     INDEX = 1
#     FIELD_CLASS = WarwickField2
#     REWARDS_GROUP_CLASS = DebrisBoxCheck
#     MEDIUM_REWARD_CHANCE = 0.5
#     HIGH_REWARD_CHANCE = 0.25
#     ULTRA_REWARD = True


class BerlinStaticText(BerlinSysObject, RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = rh_ber
space_color = 3, 7, 12
local_faction = rh_grp
space_farclip = 50000

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Music]
space = music_rh_space
danger = music_rh_danger
battle = music_rh_battle

[Ambient]
color = 3, 5, 8

[Dust]
spacedust = Dust

[Background]
nebulae = solar\\stars_mod\\rh_ber_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_rh_ber_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
property_flags = 512 ;lava - MILITARY
;property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = Rh_Ber_System_Light
pos = 0, 0, 0
color = 150, 190, 255
range = 150000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION'''


class BerlinSun(BerlinSysObject, Sun):
    STAR = 'Rh04_Sun'
    LOADOUT = 'med_blue_sun_fx'


class BerlinJumpgateTop(BerlinSysObject, Jumpgate):
    INDEX = 1
    REL = TOP


class BerlinJumpgateBottom(BerlinSysObject, Jumpgate):
    INDEX = 2
    REL = BOTTOM


class BerlinDockring(BerlinSysObject, Dockring):
    BASE_INDEX = 1
    REL = RIGHT


class BerlinPrison(BerlinSysObject, Prison):
    BASE_INDEX = 2
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = BerlinPrison
    INTERIOR_CLASS = interior.StationBshbarInterior


class BerlinMegaStation(BerlinSysObject, Station):
    BASE_INDEX = 4
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = Potsdam
    INTERIOR_CLASS = interior.StationInterior


class BerlinOutpost(BerlinSysObject, Outpost):
    BASE_INDEX = 6
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = BerlinPoliceOutpost
    INTERIOR_CLASS = interior.OutpostShipdealerInterior


class BerlinShipyard(BerlinSysObject, Shipyard):
    BASE_INDEX = 3
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = CambridgeShipyard
    INTERIOR_CLASS = interior.OutpostInterior


class BerlinTrading(BerlinSysObject, TradingBase):
    BASE_INDEX = 9
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = TekagiStorage
    INTERIOR_CLASS = interior.BattleshipNoshipInterior


class BerlinRefinery(BerlinSysObject, Refinery):
    BASE_INDEX = 7
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = AlgBaseHokkaido
    INTERIOR_CLASS = interior.BattleshipInterior


class BerlinJunkers(BerlinSysObject, JunkerBase):
    BASE_INDEX = 8
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = BerlinJunker
    INTERIOR_CLASS = interior.PirateOutpostInterior
    ASTEROID_ZONES = [
        # BerlinDebrisZone1
    ]


class BerlinPiratesTop(BerlinSysObject, PirateBase):
    BASE_INDEX = 5
    INDEX = 1
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = BerlinAsteroidBase
    INTERIOR_CLASS = interior.PirateOutpostShipdealerInterior
    AST_EXCLUSION_ZONE_SIZE = 2000
    ASTEROID_ZONES = [
        BerlinAsteroidZone1
    ]


class BerlinPiratesBottom(BerlinSysObject, PirateBase):
    BASE_INDEX = 10
    INDEX = 2
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = PirateBaseBizmark
    INTERIOR_CLASS = interior.PirateStationShipdealerInterior


class BerlinPlanet1(BerlinSysObject, Planet):
    ARCHETYPE = 'planet_desormed_4000'
    SPHERE_RADIUS = 4000
    RELATED_DOCK_RING = BerlinDockring


class BerlinPlanet2(BerlinSysObject, Planet):
    INDEX = 2
    ARCHETYPE = 'planet_icewatind_3000'
    PLANET_CIRCLE = False
    SPHERE_RADIUS = 3000
    RING = True
    RING_ZONE_ALIAS = 'ring'
    RING_ZONE_INDEX = 1
    RING_FILE_NAME = 'berlin'


class BerlinPlanet3(BerlinSysObject, Planet):
    INDEX = 3
    ARCHETYPE = 'planet_ice_purple_1500'
    SPHERE_RADIUS = 1500


class BerlinPlanet4(BerlinSysObject, Planet):
    INDEX = 4
    ARCHETYPE = 'planet_gasgrncld_2500'
    SPHERE_RADIUS = 2500


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
