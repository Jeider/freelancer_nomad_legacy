from fx.space import Dust
from fx.sound import Ambience

from universe.content.system_object import TOP, BOTTOM, LEFT, RIGHT
from universe.content import main_objects
from universe.content import zones
from universe.content import interior
from universe.content import dealers
from universe.content import asteroid_definition
from universe.content.space_voice import SpaceVoice
from universe.content import faction

from templates.dockable import pirate
from templates.dockable import potsdam
from templates.dockable import prisons
from templates.dockable import shipyards
from templates.dockable import alg
from templates.dockable import astbase
from templates.dockable import junker
from templates.dockable import police
from templates.dockable import trade_storages

from universe.content import mineable

from templates.solar.asteroid import AsteroidOmega15
from templates.solar.debris_box import DebrisBox


class BerlinMember(object):
    INDEX = 1
    FACTION = faction.RH_GRP
    ABSTRACT = False


class BerlinStaticText(BerlinMember, main_objects.RawText):
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

'''


class BerlinPirateAsteroidReward(BerlinMember, mineable.AsteroidRewardsGroupMedium):
    NAME = 'rh_ber_rock'
    SOLAR = AsteroidOmega15
    REWARD_ITEM = 'comm_roid_niobium'


class BerlinDebrisBoxReward(BerlinMember, mineable.DefaultDebrisBoxRewardsGroup):
    NAME = 'rh_ber_debrisbox'
    SOLAR = DebrisBox
    REWARD_ITEM = 'comm_scrap_metal'
    ULTRA_REWARD_ITEM = 'rh_shieldgun09'


class BerlinAstField(mineable.DefaultField):
    BOX_SIZE = 3000
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.3
    DRIFT_Y = 0
    DRIFT_Z = 0.3


class BerlinDebrisField(mineable.DefaultField):
    BOX_SIZE = 1200
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.2
    DRIFT_Y = 0.1
    DRIFT_Z = 0.2


class BerlinPirateAsteroids(BerlinMember, mineable.AsteroidRewardField):
    INDEX = 1
    FIELD_CLASS = BerlinAstField
    REWARDS_GROUP_CLASS = BerlinPirateAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25


class BerlinDebrisBoxHighField2(BerlinMember, mineable.DebrisBoxRewardField):
    INDEX = 2
    FIELD_CLASS = BerlinDebrisField
    REWARDS_GROUP_CLASS = BerlinDebrisBoxReward
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = False


class BerlinDebrisBoxHighField3(BerlinMember, mineable.DebrisBoxRewardField):
    INDEX = 3
    FIELD_CLASS = BerlinDebrisField
    REWARDS_GROUP_CLASS = BerlinDebrisBoxReward
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = False


class BerlinDebrisBoxHighField4(BerlinMember, mineable.DebrisBoxRewardField):
    INDEX = 4
    FIELD_CLASS = BerlinDebrisField
    REWARDS_GROUP_CLASS = BerlinDebrisBoxReward
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = False


class BerlinPirateAsteroidDefinition(asteroid_definition.Omega15AsteroidDefinition):
    ABSTRACT = False
    NAME = 'rh_ber_pirate_astfield'
    DYNAST = True
    BELT = False
    BILLBOARDS = False
    LOOT = False  # TEMP


class BerlinDebrisZone1Definition(asteroid_definition.DebrisDefinition):
    ABSTRACT = False
    NAME = 'rh_ber_debris_field1'


class BerlinDebrisZone2Definition(asteroid_definition.DebrisDefinition):
    ABSTRACT = False
    NAME = 'rh_ber_debris_field2'


class BerlinDebrisZone3Definition(asteroid_definition.DebrisDefinition):
    ABSTRACT = False
    NAME = 'rh_ber_debris_field3'


class BerlinDebrisZone4Definition(asteroid_definition.DebrisDefinition):
    ABSTRACT = False
    NAME = 'rh_ber_debris_field4'


class BerlinDebrisZone5Definition(asteroid_definition.DebrisDefinition):
    ABSTRACT = False
    NAME = 'rh_ber_debris_field5'


class BerlinAsteroidZone1(BerlinMember, zones.AsteroidZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = BerlinPirateAsteroidDefinition


class BerlinDebrisZone1(BerlinMember, zones.DebrisZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = BerlinDebrisZone1Definition


class BerlinDebrisZone2(BerlinMember, zones.DebrisZone):
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = BerlinDebrisZone2Definition


class BerlinDebrisZone3(BerlinMember, zones.DebrisZone):
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = BerlinDebrisZone3Definition


class BerlinDebrisZone4(BerlinMember, zones.DebrisZone):
    INDEX = 4
    ASTEROID_DEFINITION_CLASS = BerlinDebrisZone4Definition


class BerlinDebrisZone5(BerlinMember, zones.DebrisZone):
    INDEX = 5
    ASTEROID_DEFINITION_CLASS = BerlinDebrisZone5Definition


class BerlinTopNebula(BerlinMember, zones.NebulaZone):
    INDEX = 1
    FILE_NAME = 'rh_ber_blue_nebula'
    SPACEDUST = Dust.ATTRACT
    SPACEDUST_MAXPARTICLES = 50
    MUSIC = Ambience.AST_ROCK


class BerlinSun(BerlinMember, main_objects.Sun):
    STAR = 'Rh04_Sun'
    LOADOUT = 'med_blue_sun_fx'


class BerlinJumpgateTop(BerlinMember, main_objects.Jumpgate):
    INDEX = 1
    REL = TOP


class BerlinJumpgateBottom(BerlinMember, main_objects.Jumpgate):
    INDEX = 2
    REL = BOTTOM


class BerlinDockring(BerlinMember, main_objects.Dockring):
    BASE_INDEX = 1
    REL = RIGHT
    AUDIO_PREFIX = SpaceVoice.RH_PLANET
    INTERIOR_CLASS = interior.CustomFullSplitRoomInterior
    DEALERS = dealers.RheinlandPlanetDealers


class BerlinPrison(BerlinMember, main_objects.Prison):
    BASE_INDEX = 2
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = prisons.BerlinPrison
    INTERIOR_CLASS = interior.StationBshbarInterior
    DEALERS = dealers.RheinlandMilitaryDealers


class BerlinMegaStation(BerlinMember, main_objects.Station):
    BASE_INDEX = 4
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = potsdam.Potsdam
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.RheinlandCivilianDealers


class BerlinOutpost(BerlinMember, main_objects.Outpost):
    BASE_INDEX = 6
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = police.BerlinPoliceOutpost
    INTERIOR_CLASS = interior.OutpostShipdealerInterior
    AUDIO_PREFIX = SpaceVoice.BORDER_STATION
    DEALERS = dealers.RheinlandMilitaryDealers


class BerlinShipyard(BerlinMember, main_objects.Shipyard):
    BASE_INDEX = 3
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = shipyards.CambridgeShipyard
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.RheinlandMilitaryDealers


class BerlinTrading(BerlinMember, main_objects.TradingBase):
    BASE_INDEX = 9
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = trade_storages.TekagiStorage
    INTERIOR_CLASS = interior.BattleshipNoshipInterior
    DEALERS = dealers.RheinlandCivilianDealers
    FACTION = faction.TR_GRP


class BerlinRefinery(BerlinMember, main_objects.Refinery):
    BASE_INDEX = 7
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = alg.AlgBaseHokkaido
    INTERIOR_CLASS = interior.BattleshipInterior
    DEALERS = dealers.RheinlandCivilianDealers
    FACTION = faction.RC_GRP


class BerlinJunkers(BerlinMember, main_objects.JunkerBase):
    BASE_INDEX = 8
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = junker.BerlinJunker
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.RheinlandPirateDealers
    FACTION = faction.JUNK_GRP
    ASTEROID_ZONES = [
        BerlinDebrisZone1
    ]
    DEFENCE_LEVEL = None


class BerlinPiratesTop(BerlinMember, main_objects.PirateBase):
    BASE_INDEX = 5
    INDEX = 1
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = astbase.BerlinAsteroidBase
    INTERIOR_CLASS = interior.PirateOutpostShipdealerInterior
    DEALERS = dealers.RheinlandPirateDealers
    FACTION = faction.RX_GRP
    AST_EXCLUSION_ZONE_SIZE = 2500
    ASTEROID_ZONES = [
        BerlinAsteroidZone1
    ]
    DEFENCE_LEVEL = None


class BerlinPiratesBottom(BerlinMember, main_objects.PirateBase):
    BASE_INDEX = 10
    INDEX = 2
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = pirate.PirateBaseBizmark
    INTERIOR_CLASS = interior.PirateStationShipdealerInterior
    DEALERS = dealers.RheinlandPirateDealers
    FACTION = faction.RX_GRP
    ASTEROID_ZONES = [
        BerlinDebrisZone5
    ]
    DEFENCE_LEVEL = None


class BerlinPlanet1(BerlinMember, main_objects.Planet):
    ARCHETYPE = 'planet_desormed_4000'
    SPHERE_RADIUS = 4000
    RELATED_DOCK_RING = BerlinDockring


class BerlinPlanet2(BerlinMember, main_objects.Planet):
    INDEX = 2
    ARCHETYPE = 'planet_icewatind_3000'
    PLANET_CIRCLE = False
    SPHERE_RADIUS = 3000
    RING = True
    RING_ZONE_ALIAS = 'ring'
    RING_ZONE_INDEX = 1
    RING_FILE_NAME = 'berlin'


class BerlinPlanet3(BerlinMember, main_objects.Planet):
    INDEX = 3
    ARCHETYPE = 'planet_ice_purple_1500'
    SPHERE_RADIUS = 1500


class BerlinPlanet4(BerlinMember, main_objects.Planet):
    INDEX = 4
    ARCHETYPE = 'planet_gasgrncld_2500'
    SPHERE_RADIUS = 2500


class BerConnOutpost1(BerlinMember, main_objects.TradeConnection):
    OBJ_FROM = BerlinOutpost
    OBJ_TO = BerlinJumpgateTop
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        BerlinPiratesTop
    ]


class BerConnOutpost2(BerlinMember, main_objects.TradeConnection):
    OBJ_FROM = BerlinOutpost
    OBJ_TO = BerlinShipyard
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        BerlinPiratesTop
    ]


class BerConnOutpost3(BerlinMember, main_objects.TradeConnection):
    OBJ_FROM = BerlinOutpost
    OBJ_TO = BerlinDockring
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = BOTTOM


class BerConnShipPris(BerlinMember, main_objects.TradeConnection):
    OBJ_FROM = BerlinShipyard
    OBJ_TO = BerlinPrison
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        BerlinPiratesTop
    ]


class BerConnTrading1(BerlinMember, main_objects.TradeConnection):
    OBJ_FROM = BerlinTrading
    OBJ_TO = BerlinPrison
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        BerlinPiratesBottom
    ]


class BerConnTrading2(BerlinMember, main_objects.TradeConnection):
    OBJ_FROM = BerlinTrading
    OBJ_TO = BerlinJumpgateBottom
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'F'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        BerlinPiratesBottom
    ]


class BerConnTrading3(BerlinMember, main_objects.TradeConnection):
    OBJ_FROM = BerlinTrading
    OBJ_TO = BerlinMegaStation
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'G'
    HUNTER_DEFENCE_REL = BOTTOM


class BerConnStation1(BerlinMember, main_objects.TradeConnection):
    OBJ_FROM = BerlinMegaStation
    OBJ_TO = BerlinDockring
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'H'
    ATTACKED_BY = [
        BerlinJunkers
    ]


class BerConnStation2(BerlinMember, main_objects.TradeConnection):
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
