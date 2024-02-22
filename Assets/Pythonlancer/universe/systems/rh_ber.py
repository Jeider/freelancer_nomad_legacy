from fx.space import Dust
from fx.sound import Ambience

from universe.content.system_object import TOP, BOTTOM, LEFT, RIGHT
from universe.content.main_objects import RawText, Sun, Planet, Jumpgate, Dockring, Shipyard, Station, Outpost, Prison, Refinery, TradingBase, JunkerBase, PirateBase, Sattelite, TradeConnection
from universe.content.zones import AsteroidZone, DebrisZone, NebulaZone
from universe.content import interior
from universe.content import dealers
from universe.content.asteroid_definition import Omega15AsteroidDefinition, DebrisDefinition
from universe.content.space_voice import SpaceVoice
from universe.content import faction

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


class BerlinMember(object):
    INDEX = 1
    FACTION = faction.RH_GRP
    ABSTRACT = False


class BerlinStaticText(BerlinMember, RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = rh_ber
space_color = 3, 7, 12
local_faction = rh_grp
space_farclip = 75000

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
atten_curve = DYNAMIC_DIRECTION



[EncounterParameters]
nickname = rh_grp_main_defend
filename = missions\\npc\\rh\\rh_grp_main_defend.ini

[EncounterParameters]
nickname = rh_grp_main_scout
filename = missions\\npc\\rh\\rh_grp_main_scout.ini

[EncounterParameters]
nickname = rh_grp_main_cruiser
filename = missions\\npc\\rh\\rh_grp_main_cruiser.ini

[EncounterParameters]
nickname = rh_grp_main_gunboat
filename = missions\\npc\\rh\\rh_grp_main_gunboat.ini

[EncounterParameters]
nickname = rh_grp_main_elite2
filename = missions\\npc\\rh\\rh_grp_main_elite2.ini

[EncounterParameters]
nickname = bh_grp_rh_scout
filename = missions\\npc\\rh\\bh_grp_rh_scout.ini

[EncounterParameters]
nickname = rh_grp_main_trade
filename = missions\\npc\\rh\\rh_grp_main_trade.ini

[EncounterParameters]
nickname = tr_grp_rh_transport
filename = missions\\npc\\rh\\tr_grp_rh_transport.ini

[EncounterParameters]
nickname = bh_grp_rh_trade
filename = missions\\npc\\rh\\bh_grp_rh_trade.ini

[EncounterParameters]
nickname = rh_grp_main_trade_tlr
filename = missions\\npc\\rh\\rh_grp_main_trade_tlr.ini

[EncounterParameters]
nickname = tr_grp_rh_transport_tlr
filename = missions\\npc\\rh\\tr_grp_rh_transport_tlr.ini

[EncounterParameters]
nickname = bh_grp_rh_trade_tlr
filename = missions\\npc\\rh\\bh_grp_rh_trade_tlr.ini

[EncounterParameters]
nickname = rh_pirates_patrol
filename = missions\\npc\\pi\\pi_grp_rh_patrol.ini

[EncounterParameters]
nickname = rh_grp_main_patrol
filename = missions\\npc\\rh\\rh_grp_main_patrol.ini

[EncounterParameters]
nickname = rh_junkers
filename = missions\\npc\\rh\\rh_junkers.ini

[EncounterParameters]
nickname = bh_grp_rh_patrol
filename = missions\\npc\\rh\\bh_grp_rh_patrol.ini

[EncounterParameters]
nickname = patrol_police
filename = missions\\NPC\\patrol_police.ini

[EncounterParameters]
nickname = patrol_tlr
filename = missions\\NPC\\patrol_tlr.ini

[EncounterParameters]
nickname = patrol_alg
filename = missions\\NPC\\RH\\rh_alg.ini

[EncounterParameters]
nickname = area_xscout
filename = missions\\NPC\\area_rebels.ini

[EncounterParameters]
nickname = corp_lifter
filename = missions\\npc\\lifter.ini

[EncounterParameters]
nickname = corp_repair
filename = missions\\npc\\repair.ini

'''



class BerlinPirateAsteroidReward(BerlinMember, AsteroidRewardsGroupMedium):
    NAME = 'rh_ber_rock'
    SOLAR = AsteroidOmega15
    REWARD_ITEM = 'comm_roid_niobium'


class BerlinDebrisBoxReward(BerlinMember, DefaultDebrisBoxRewardsGroup):
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


class BerlinPirateAsteroids(BerlinMember, AsteroidRewardField):
    INDEX = 1
    FIELD_CLASS = BerlinAstField
    REWARDS_GROUP_CLASS = BerlinPirateAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25


# class BerlinDebrisBoxMediumField(BerlinMember, DebrisBoxRewardField):
#     INDEX = 1
#     FIELD_CLASS = WarwickField2
#     REWARDS_GROUP_CLASS = BerlinDebrisBoxReward
#     MEDIUM_REWARD_CHANCE = 0.5
#     HIGH_REWARD_CHANCE = 0.25
#     ULTRA_REWARD = False


# class BerlinDebrisBoxHighField1(BerlinMember, DebrisBoxRewardField):
#     INDEX = 1
#     FIELD_CLASS = BerlinDebrisField
#     REWARDS_GROUP_CLASS = BerlinDebrisBoxReward
#     MEDIUM_REWARD_CHANCE = 0.5
#     HIGH_REWARD_CHANCE = 0.25
#     ULTRA_REWARD = False

class BerlinDebrisBoxHighField2(BerlinMember, DebrisBoxRewardField):
    INDEX = 2
    FIELD_CLASS = BerlinDebrisField
    REWARDS_GROUP_CLASS = BerlinDebrisBoxReward
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = False


class BerlinDebrisBoxHighField3(BerlinMember, DebrisBoxRewardField):
    INDEX = 3
    FIELD_CLASS = BerlinDebrisField
    REWARDS_GROUP_CLASS = BerlinDebrisBoxReward
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = False


class BerlinDebrisBoxHighField4(BerlinMember, DebrisBoxRewardField):
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


class BerlinDebrisZone1Definition(DebrisDefinition):
    ABSTRACT = False
    NAME = 'rh_ber_debris_field1'


class BerlinDebrisZone2Definition(DebrisDefinition):
    ABSTRACT = False
    NAME = 'rh_ber_debris_field2'


class BerlinDebrisZone3Definition(DebrisDefinition):
    ABSTRACT = False
    NAME = 'rh_ber_debris_field3'


class BerlinDebrisZone4Definition(DebrisDefinition):
    ABSTRACT = False
    NAME = 'rh_ber_debris_field4'


class BerlinDebrisZone5Definition(DebrisDefinition):
    ABSTRACT = False
    NAME = 'rh_ber_debris_field5'


class BerlinAsteroidZone1(BerlinMember, AsteroidZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = BerlinPirateAsteroidDefinition


class BerlinDebrisZone1(BerlinMember, DebrisZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = BerlinDebrisZone1Definition


class BerlinDebrisZone2(BerlinMember, DebrisZone):
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = BerlinDebrisZone2Definition


class BerlinDebrisZone3(BerlinMember, DebrisZone):
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = BerlinDebrisZone3Definition


class BerlinDebrisZone4(BerlinMember, DebrisZone):
    INDEX = 4
    ASTEROID_DEFINITION_CLASS = BerlinDebrisZone4Definition


class BerlinDebrisZone5(BerlinMember, DebrisZone):
    INDEX = 5
    ASTEROID_DEFINITION_CLASS = BerlinDebrisZone5Definition


class BerlinTopNebula(BerlinMember, NebulaZone):
    INDEX = 1
    FILE_NAME = 'rh_ber_blue_nebula'
    SPACEDUST = Dust.ATTRACT
    SPACEDUST_MAXPARTICLES = 50
    MUSIC = Ambience.AST_ROCK


# class BerlinDebrisBoxUltraField(BerlinMember, DebrisBoxRewardField):
#     INDEX = 1
#     FIELD_CLASS = WarwickField2
#     REWARDS_GROUP_CLASS = DebrisBoxCheck
#     MEDIUM_REWARD_CHANCE = 0.5
#     HIGH_REWARD_CHANCE = 0.25
#     ULTRA_REWARD = True



class BerlinSun(BerlinMember, Sun):
    STAR = 'Rh04_Sun'
    LOADOUT = 'med_blue_sun_fx'


class BerlinJumpgateTop(BerlinMember, Jumpgate):
    INDEX = 1
    REL = TOP


class BerlinJumpgateBottom(BerlinMember, Jumpgate):
    INDEX = 2
    REL = BOTTOM


class BerlinDockring(BerlinMember, Dockring):
    BASE_INDEX = 1
    REL = RIGHT
    AUDIO_PREFIX = SpaceVoice.RH_PLANET
    INTERIOR_CLASS = interior.CustomFullSplitRoomInterior
    DEALERS = dealers.RheinlandPlanetDealers


class BerlinPrison(BerlinMember, Prison):
    BASE_INDEX = 2
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = BerlinPrison
    INTERIOR_CLASS = interior.StationBshbarInterior
    DEALERS = dealers.RheinlandMilitaryDealers


class BerlinMegaStation(BerlinMember, Station):
    BASE_INDEX = 4
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = Potsdam
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.RheinlandCivilianDealers


class BerlinOutpost(BerlinMember, Outpost):
    BASE_INDEX = 6
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = BerlinPoliceOutpost
    INTERIOR_CLASS = interior.OutpostShipdealerInterior
    AUDIO_PREFIX = SpaceVoice.BORDER_STATION
    DEALERS = dealers.RheinlandMilitaryDealers


class BerlinShipyard(BerlinMember, Shipyard):
    BASE_INDEX = 3
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = CambridgeShipyard
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.RheinlandMilitaryDealers


class BerlinTrading(BerlinMember, TradingBase):
    BASE_INDEX = 9
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = TekagiStorage
    INTERIOR_CLASS = interior.BattleshipNoshipInterior
    DEALERS = dealers.RheinlandCivilianDealers
    FACTION = faction.TR_GRP


class BerlinRefinery(BerlinMember, Refinery):
    BASE_INDEX = 7
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = AlgBaseHokkaido
    INTERIOR_CLASS = interior.BattleshipInterior
    DEALERS = dealers.RheinlandCivilianDealers
    FACTION = faction.RC_GRP


class BerlinJunkers(BerlinMember, JunkerBase):
    BASE_INDEX = 8
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = BerlinJunker
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.RheinlandPirateDealers
    FACTION = faction.JUNK_GRP
    ASTEROID_ZONES = [
        BerlinDebrisZone1
    ]
    DEFENCE_LEVEL = None


class BerlinPiratesTop(BerlinMember, PirateBase):
    BASE_INDEX = 5
    INDEX = 1
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = BerlinAsteroidBase
    INTERIOR_CLASS = interior.PirateOutpostShipdealerInterior
    DEALERS = dealers.RheinlandPirateDealers
    FACTION = faction.RX_GRP
    AST_EXCLUSION_ZONE_SIZE = 2500
    ASTEROID_ZONES = [
        BerlinAsteroidZone1
    ]
    DEFENCE_LEVEL = None


class BerlinPiratesBottom(BerlinMember, PirateBase):
    BASE_INDEX = 10
    INDEX = 2
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = PirateBaseBizmark
    INTERIOR_CLASS = interior.PirateStationShipdealerInterior
    DEALERS = dealers.RheinlandPirateDealers
    FACTION = faction.RX_GRP
    ASTEROID_ZONES = [
        BerlinDebrisZone5
    ]
    DEFENCE_LEVEL = None


class BerlinPlanet1(BerlinMember, Planet):
    ARCHETYPE = 'planet_desormed_4000'
    SPHERE_RADIUS = 4000
    RELATED_DOCK_RING = BerlinDockring


class BerlinPlanet2(BerlinMember, Planet):
    INDEX = 2
    ARCHETYPE = 'planet_icewatind_3000'
    PLANET_CIRCLE = False
    SPHERE_RADIUS = 3000
    RING = True
    RING_ZONE_ALIAS = 'ring'
    RING_ZONE_INDEX = 1
    RING_FILE_NAME = 'berlin'


class BerlinPlanet3(BerlinMember, Planet):
    INDEX = 3
    ARCHETYPE = 'planet_ice_purple_1500'
    SPHERE_RADIUS = 1500


class BerlinPlanet4(BerlinMember, Planet):
    INDEX = 4
    ARCHETYPE = 'planet_gasgrncld_2500'
    SPHERE_RADIUS = 2500


class BerConnOutpost1(BerlinMember, TradeConnection):
    OBJ_FROM = BerlinOutpost
    OBJ_TO = BerlinJumpgateTop
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        BerlinPiratesTop
    ]


class BerConnOutpost2(BerlinMember, TradeConnection):
    OBJ_FROM = BerlinOutpost
    OBJ_TO = BerlinShipyard
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        BerlinPiratesTop
    ]


class BerConnOutpost3(BerlinMember, TradeConnection):
    OBJ_FROM = BerlinOutpost
    OBJ_TO = BerlinDockring
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = BOTTOM


class BerConnShipPris(BerlinMember, TradeConnection):
    OBJ_FROM = BerlinShipyard
    OBJ_TO = BerlinPrison
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        BerlinPiratesTop
    ]


class BerConnTrading1(BerlinMember, TradeConnection):
    OBJ_FROM = BerlinTrading
    OBJ_TO = BerlinPrison
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        BerlinPiratesBottom
    ]


class BerConnTrading2(BerlinMember, TradeConnection):
    OBJ_FROM = BerlinTrading
    OBJ_TO = BerlinJumpgateBottom
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'F'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        BerlinPiratesBottom
    ]


class BerConnTrading3(BerlinMember, TradeConnection):
    OBJ_FROM = BerlinTrading
    OBJ_TO = BerlinMegaStation
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'G'
    HUNTER_DEFENCE_REL = BOTTOM


class BerConnStation1(BerlinMember, TradeConnection):
    OBJ_FROM = BerlinMegaStation
    OBJ_TO = BerlinDockring
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'H'
    ATTACKED_BY = [
        BerlinJunkers
    ]


class BerConnStation2(BerlinMember, TradeConnection):
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
