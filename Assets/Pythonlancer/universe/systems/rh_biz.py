from fx.space import Dust
from fx.sound import Ambience

from universe.content.system_object import TOP, BOTTOM, LEFT, RIGHT
from universe.content import main_objects
from universe.content import zones
from universe.content import asteroid_definition
from universe.content import interior
from universe.content import dealers
from universe.content.space_voice import SpaceVoice
from universe.content import faction
from universe.content import mineable
from templates.solar import asteroid as asteroid_solar
from templates.solar import debris_box
from templates.nebula import rh_biz_nebula

from templates.dockable import pirate
from templates.dockable import astbase
from templates.dockable import constanta
from templates.dockable import shipyards
from templates.dockable import alg
from templates.dockable import research
from templates.dockable import rheinland_military


class BizmarkMember(object):
    INDEX = 1
    ABSTRACT = False
    FACTION = faction.RH_GRP


class BizmarkStaticText(BizmarkMember, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = rh_biz
space_color = 10, 6, 0
local_faction = rh_grp
space_farclip = 75000

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Dust]
spacedust = Dust

[Music]
space = music_rh_space
danger = music_rh_danger
battle = music_rh_battle

[Ambient]
color = 10, 6, 0

[LightSource]
nickname = Bizmark_Sys_Light
pos = 0, 0, 0
color = 200, 200, 255
range = 200000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION

[zone]
nickname = zone_rh_biz_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
property_flags = 512 ;lava - MILITARY
;property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[Background]
complex_stars = solar\\stars_mod\\new_generic.cmp
nebulae = solar\\stars_mod\\rh_biz_nebula.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

'''


class BizmarkAsteroidDefinition(asteroid_definition.Omega15NiobiumAsteroidDefinition):
    ABSTRACT = True
    NAME = None
    DYNAST = True
    BELT = True
    BILLBOARDS = True
    LOOT = False  # TEMP


class BizmarkAsteroidZone1(BizmarkMember, zones.AsteroidZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = BizmarkAsteroidDefinition


class BizmarkAsteroidZone2(BizmarkMember, zones.AsteroidZone):
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = BizmarkAsteroidDefinition


class BizmarkDebrisZone1(BizmarkMember, zones.DebrisZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class BizmarkDebrisZone2(BizmarkMember, zones.DebrisZone):
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class BizmarkDebrisZone3(BizmarkMember, zones.DebrisZone):
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class BizmarkDebrisZone4(BizmarkMember, zones.DebrisZone):
    INDEX = 4
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class BizmarkTopLeftNebula(BizmarkMember, zones.NebulaZone):
    INDEX = 1
    CONTENT_TEMPLATE = rh_biz_nebula.BizmarkBrownNebulaTemplate
    SPACEDUST = Dust.ATTRACT
    SPACEDUST_MAXPARTICLES = 40
    MUSIC = Ambience.NEBULA_DMATTER


class BizmarkTopRightNebula(BizmarkMember, zones.NebulaZone):
    INDEX = 2
    CONTENT_TEMPLATE = rh_biz_nebula.BizmarkBrownNebulaTemplate
    SPACEDUST = Dust.ATTRACT
    SPACEDUST_MAXPARTICLES = 40
    MUSIC = Ambience.NEBULA_DMATTER


class Bizmark8Sun(BizmarkMember, main_objects.Sun):
    STAR = 'Ku01_sun'
    LOADOUT = 'large_blue_sun_fx'


class BizmarkSigma8Jumpgate(BizmarkMember, main_objects.Jumpgate):
    INDEX = 1
    REL = TOP


class BizmarkMunchenJumpgate(BizmarkMember, main_objects.Jumpgate):
    INDEX = 2
    REL = LEFT


class BizmarkOmega15Jumpgate(BizmarkMember, main_objects.Jumpgate):
    INDEX = 3
    REL = BOTTOM


class BizmarkDockRing(BizmarkMember, main_objects.Dockring):
    BASE_INDEX = 1
    REL = RIGHT
    AUDIO_PREFIX = SpaceVoice.RH_PLANET
    INTERIOR_CLASS = interior.CustomFullSplitRoomInterior
    DEALERS = dealers.RheinlandPlanetDealers


class BizmarkTrading(BizmarkMember, main_objects.TradingBase):
    BASE_INDEX = 2
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = shipyards.HeavyBarrelShipyard

    AUDIO_PREFIX = SpaceVoice.OUTPOST
    INTERIOR_CLASS = interior.OutpostShipdealerInterior
    DEALERS = dealers.RheinlandCivilianDealers


class BizmarkBattleship(BizmarkMember, main_objects.RheinlandBattleship):
    BASE_INDEX = 3
    REL = LEFT

    AUDIO_PREFIX = SpaceVoice.BATTLESHIP
    INTERIOR_CLASS = interior.BattleshipInterior
    DEALERS = dealers.RheinlandMilitaryDealers


class BizmarkResearch(BizmarkMember, main_objects.Station):
    ALIAS = 'research'
    INDEX = 1
    BASE_INDEX = 4
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = research.RheinlandResearch

    AUDIO_PREFIX = SpaceVoice.STATION
    INTERIOR_CLASS = interior.StationBshbarInterior
    DEALERS = dealers.RheinlandCivilianDealers


class BizmarkMilitary(BizmarkMember, main_objects.Station):
    ALIAS = 'military'
    BASE_INDEX = 5
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = rheinland_military.RheinlandMilitary

    LOCKED_DOCK = True

    AUDIO_PREFIX = SpaceVoice.STATION
    INTERIOR_CLASS = interior.StationShipdealerInterior
    DEALERS = dealers.RheinlandMilitaryDealers


class BizmarkShipyard(BizmarkMember, main_objects.Shipyard):
    BASE_INDEX = 6
    REL = TOP
    REL_DRIFT = 1000
    SPACE_OBJECT_TEMPLATE = constanta.Constanta

    AUDIO_PREFIX = SpaceVoice.SHIPYARD
    INTERIOR_CLASS = interior.StationShipdealerInterior
    DEALERS = dealers.RheinlandCivilianDealers


class BizmarkRefinery(BizmarkMember, main_objects.Refinery):
    BASE_INDEX = 7
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = alg.AlgBaseBerlin

    AUDIO_PREFIX = SpaceVoice.FACTORY
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.RheinlandCivilianDealers

    ASTEROID_ZONES = [
        BizmarkDebrisZone4,
    ]


class BizmarkTopPirate(BizmarkMember, main_objects.PirateBase):
    BASE_INDEX = 8
    INDEX = 1
    REL = TOP
    SPACE_OBJECT_TEMPLATE = pirate.PirateBaseCalifornia
    FACTION = faction.PI_GRP

    DEFENCE_LEVEL = None

    AUDIO_PREFIX = SpaceVoice.OUTPOST
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.RheinlandPirateDealers


class BizmarkRightPirate(BizmarkMember, main_objects.PirateBase):
    BASE_INDEX = 9
    INDEX = 2
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = astbase.BizmarkAsteroidBase
    FACTION = faction.RX_GRP

    DEFENCE_LEVEL = None

    AUDIO_PREFIX = SpaceVoice.OUTPOST
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.RheinlandPirateDealers
    ASTEROID_ZONES = [
        BizmarkAsteroidZone1,
    ]


class BizmarkBaseDebrisManufactoring(main_objects.DebrisManufactoring):
    ALIAS = 'deb'
    ROTATE_RANDOM = True
    ARCHETYPE = 'mplatform'
    LOADOUT = 'mplatform_rh_debris'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    INTERIOR_BG1 = interior.INTERIOR_RH_BIZMARK
    AST_EXCLUSION_ZONE_SIZE = 2000
    AST_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.RADIOACTIVE_RED,
        'spacedust_maxparticles': 200,
    }


class BizmarkAbandonedAstBase1(BizmarkMember, main_objects.AbandonedAsteroid):
    ALIAS = 'ast'
    INDEX = 2
    BASE_INDEX = 61
    ROTATE_RANDOM = True
    ARCHETYPE = 'miningbase_mineableA'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    INTERIOR_BG1 = interior.INTERIOR_RH_BIZMARK
    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        BizmarkAsteroidZone2,
    ]
    AST_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.ASTEROID,
        'spacedust_maxparticles': 200,
    }


class BizmarkDebrisFactory1(BizmarkMember, BizmarkBaseDebrisManufactoring):
    INDEX = 1
    BASE_INDEX = 51
    ASTEROID_ZONES = [
        BizmarkDebrisZone1,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500


class BizmarkDebrisFactory2(BizmarkMember, BizmarkBaseDebrisManufactoring):
    INDEX = 2
    BASE_INDEX = 52
    ASTEROID_ZONES = [
        BizmarkDebrisZone2,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500


class BizmarkDebrisFactory3(BizmarkMember, BizmarkBaseDebrisManufactoring):
    INDEX = 3
    BASE_INDEX = 53
    ASTEROID_ZONES = [
        BizmarkDebrisZone3,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500


class BizmarkPirateAsteroidReward(BizmarkMember, mineable.AsteroidRewardsGroupUltra):
    NAME = 'rh_biz_rock'
    SOLAR = asteroid_solar.AsteroidOmega15
    REWARD_ITEM = 'comm_roid_niobium'
    ULTRA_REWARD_BASES = [
        BizmarkAbandonedAstBase1,
    ]


class BizmarkDebrisBoxReward(BizmarkMember, mineable.DefaultDebrisBoxRewardsGroup):
    NAME = 'rh_biz_debrisbox'
    SOLAR = debris_box.DebrisBox
    REWARD_ITEM = 'comm_scrap_metal'
    ULTRA_REWARD_BASES = [
        BizmarkDebrisFactory1,
        BizmarkDebrisFactory2,
        BizmarkDebrisFactory3,
    ]


class BizmarkPirateAsteroids(BizmarkMember, mineable.AsteroidRewardField):
    INDEX = 1
    FIELD_CLASS = mineable.BackgroundAsteroidsField
    REWARDS_GROUP_CLASS = BizmarkPirateAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25


class BizmarkAbandonedAsteroids1(BizmarkMember, mineable.AsteroidRewardField):
    INDEX = 2
    FIELD_CLASS = mineable.MineableAsteroidField
    REWARDS_GROUP_CLASS = BizmarkPirateAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True
    ULTRA_BASE = BizmarkAbandonedAstBase1


class BizmarkBaseDebrisBoxRewardField(mineable.DebrisBoxRewardField):
    FIELD_NAME = None
    FIELD_CLASS = mineable.MineableDebrixBoxField
    REWARDS_GROUP_CLASS = BizmarkDebrisBoxReward
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class BizmarkDebrisBoxField1(BizmarkMember, BizmarkBaseDebrisBoxRewardField):
    FIELD_NAME = 'rh_biz_debris1'
    INDEX = 1
    ULTRA_BASE = BizmarkDebrisFactory1


class BizmarkDebrisBoxField2(BizmarkMember, BizmarkBaseDebrisBoxRewardField):
    FIELD_NAME = 'rh_biz_debris2'
    INDEX = 2
    ULTRA_BASE = BizmarkDebrisFactory2


class BizmarkDebrisBoxField3(BizmarkMember, BizmarkBaseDebrisBoxRewardField):
    FIELD_NAME = 'rh_biz_debris3'
    INDEX = 3
    ULTRA_BASE = BizmarkDebrisFactory3


class BizmarkPlanet1(BizmarkMember, main_objects.Planet):
    ARCHETYPE = 'planet_earthsnwcld_3000'
    SPHERE_RADIUS = 3000
    RELATED_DOCK_RING = BizmarkDockRing


class BizmarkPlanet2(BizmarkMember, main_objects.Planet):
    INDEX = 2
    ARCHETYPE = 'planet_desored_2000'
    SPHERE_RADIUS = 2000


class BizmarkPlanet3(BizmarkMember, main_objects.Planet):
    INDEX = 3
    ARCHETYPE = 'planet_ice_purple_5000'
    SPHERE_RADIUS = 5000


class BizmarkPlanet4(BizmarkMember, main_objects.Planet):
    INDEX = 4
    ARCHETYPE = 'planet_gasgrncld_3000'
    SPHERE_RADIUS = 3000
    RING = True
    RING_ZONE_ALIAS = 'ring'
    RING_ZONE_INDEX = 1
    RING_FILE_NAME = 'bizmark'


class BizmarkConnPlanet1(BizmarkMember, main_objects.TradeConnection):
    OBJ_FROM = BizmarkDockRing
    OBJ_TO = BizmarkSigma8Jumpgate
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        BizmarkRightPirate,
    ]


class BizmarkConnPlanet2(BizmarkMember, main_objects.TradeConnection):
    OBJ_FROM = BizmarkDockRing
    OBJ_TO = BizmarkTrading
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'B'


class BizmarkConnPlanet3(BizmarkMember, main_objects.TradeConnection):
    OBJ_FROM = BizmarkDockRing
    OBJ_TO = BizmarkBattleship
    OBJ_FROM_TLR_FORCE_OFFSET = (38000, 0, -7000)
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        BizmarkRightPirate,
    ]


class BizmarkConnPlanet4(BizmarkMember, main_objects.TradeConnection):
    OBJ_FROM = BizmarkDockRing
    OBJ_TO = BizmarkResearch
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        BizmarkRightPirate,
    ]


class BizmarkConnTrading1(BizmarkMember, main_objects.TradeConnection):
    OBJ_FROM = BizmarkTrading
    OBJ_TO = BizmarkMunchenJumpgate
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        BizmarkTopPirate,
    ]


class BizmarkConnBattleship1(BizmarkMember, main_objects.TradeConnection):
    OBJ_FROM = BizmarkBattleship
    OBJ_TO = BizmarkOmega15Jumpgate
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'F'
    HUNTER_DEFENCE_REL = RIGHT


class BizmarkConnBattleship2(BizmarkMember, main_objects.TradeConnection):
    OBJ_FROM = BizmarkBattleship
    OBJ_TO = BizmarkResearch
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'G'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        BizmarkRightPirate,
    ]


class BizmarkConnShipyard1(BizmarkMember, main_objects.TradeConnection):
    OBJ_FROM = BizmarkShipyard
    OBJ_TO = BizmarkMunchenJumpgate
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'H'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        BizmarkTopPirate,
    ]


class BizmarkConnShipyard2(BizmarkMember, main_objects.TradeConnection):
    OBJ_FROM = BizmarkShipyard
    OBJ_TO = BizmarkRefinery
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'I'
    HUNTER_DEFENCE_REL = LEFT


class BizmarkConnShipyard3(BizmarkMember, main_objects.TradeConnection):
    OBJ_FROM = BizmarkShipyard
    OBJ_TO = BizmarkBattleship
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'J'
