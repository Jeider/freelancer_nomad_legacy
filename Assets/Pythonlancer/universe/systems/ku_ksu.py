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
from templates.solar import asteroid
from templates.solar import debris_box


from templates.dockable import pirate
from templates.dockable import police
from templates.dockable import trade_storages
from templates.dockable import columbia_production
from templates.dockable import astbase
from templates.dockable import shipyards
from templates.dockable import alg
from templates.dockable import research
from templates.dockable import odissey


class KyushuMember(object):
    INDEX = 1
    ABSTRACT = False
    FACTION = faction.KU_GRP

    INTERIOR_BG1 = interior.INTERIOR_KU_KYUSHU


class KyushuStaticText(KyushuMember, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = ku_ksu
space_color = 20, 35, 50 ;;;50, 35, 20 ;;;;45, 45, 55
local_faction = ku_grp
space_farclip = 70000

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Dust]
spacedust = Dust

[Music]
space = music_ku_space
danger = music_ku_danger
battle = music_ku_battle

[Ambient]
color = 45, 45, 55

[Background]
nebulae = solar\\stars_mod\\ku_ksu_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_ku_ksu_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
property_flags = 512 ;lava - MILITARY
;property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = ku_ksu_system_light
pos = 0, 0, 0
color = 153, 200, 253
range = 150000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION
'''


class KyushuDebrisZone1(KyushuMember, zones.DebrisZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class KyushuDebrisZone2(KyushuMember, zones.DebrisZone):
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class KyushuDebrisZone3(KyushuMember, zones.DebrisZone):
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class KyushuDebrisZone4(KyushuMember, zones.DebrisZone):
    INDEX = 4
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition



class KyushuBaseDebrisManufactoring(main_objects.DebrisManufactoring):
    ALIAS = 'deb'
    ROTATE_RANDOM = True
    ARCHETYPE = 'mplatform'
    LOADOUT = 'mplatform_ku_debris'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    AST_EXCLUSION_ZONE_SIZE = 2000
    AST_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.RADIOACTIVE_RED,
        'spacedust_maxparticles': 200,
    }


class KyushuDebrisFactory1(KyushuMember, KyushuBaseDebrisManufactoring):
    INDEX = 1
    BASE_INDEX = 51
    ASTEROID_ZONES = [
        KyushuDebrisZone1,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500


class KyushuDebrisFactory2(KyushuMember, KyushuBaseDebrisManufactoring):
    INDEX = 2
    BASE_INDEX = 52
    ASTEROID_ZONES = [
        KyushuDebrisZone2,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500


class KyushuDebrisFactory3(KyushuMember, KyushuBaseDebrisManufactoring):
    INDEX = 3
    BASE_INDEX = 53
    ASTEROID_ZONES = [
        KyushuDebrisZone3,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500


class KyushuDebrisBoxReward(KyushuMember, mineable.DefaultDebrisBoxRewardsGroup):
    NAME = 'ku_ksu_debrisbox'
    SOLAR = debris_box.DebrisBox
    REWARD_ITEM = 'comm_scrap_metal'
    ULTRA_REWARD_BASES = [
        KyushuDebrisFactory1,
        KyushuDebrisFactory2,
        KyushuDebrisFactory3,
    ]


class KyushuBaseDebrisBoxRewardField(mineable.DebrisBoxRewardField):
    FIELD_CLASS = mineable.MineableDebrixBoxField
    REWARDS_GROUP_CLASS = KyushuDebrisBoxReward
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class KyushuDebrisBoxField1(KyushuMember, KyushuBaseDebrisBoxRewardField):
    INDEX = 1
    ULTRA_BASE = KyushuDebrisFactory1


class KyushuDebrisBoxField2(KyushuMember, KyushuBaseDebrisBoxRewardField):
    INDEX = 2
    ULTRA_BASE = KyushuDebrisFactory2


class KyushuDebrisBoxField3(KyushuMember, KyushuBaseDebrisBoxRewardField):
    INDEX = 3
    ULTRA_BASE = KyushuDebrisFactory3


class KyushuAsteroidDefinition1(asteroid_definition.Tau37AsteroidDefinition):
    BELT = True
    BILLBOARDS = True
    DYNAST = True
    LOOT = False  # TEMP


class KyushuAsteroidZone1(KyushuMember, zones.AsteroidZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = KyushuAsteroidDefinition1


class KyushuAsteroidZone2(KyushuMember, zones.AsteroidZone):
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = KyushuAsteroidDefinition1


class KyushuAsteroidZone3(KyushuMember, zones.AsteroidZone):
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = KyushuAsteroidDefinition1


class KyushuBaseAbandonedAst(main_objects.AbandonedAsteroid):
    ALIAS = 'ast'
    ROTATE_RANDOM = True
    ARCHETYPE = 'miningbase_mineableA'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    AST_EXCLUSION_ZONE_SIZE = 2500
    AST_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.ICE,
        'spacedust_maxparticles': 200,
    }


class KyushuAbandonedAstBase1(KyushuMember, KyushuBaseAbandonedAst):
    INDEX = 1
    BASE_INDEX = 61

    ASTEROID_ZONES = [
        KyushuAsteroidZone1,
    ]


class KyushuAbandonedAstBase2(KyushuMember, KyushuBaseAbandonedAst):
    INDEX = 2
    BASE_INDEX = 62

    ASTEROID_ZONES = [
        KyushuAsteroidZone2,
    ]


class KyushuUnlockAsteroidReward(KyushuMember, mineable.AsteroidRewardsGroupUltra):
    NAME = 'ku_ksu_unlock'
    SOLAR = asteroid.AsteroidTau37
    REWARD_ITEM = 'comm_roid_uranium'
    ULTRA_REWARD_BASES = [
        KyushuAbandonedAstBase1,
        KyushuAbandonedAstBase2,
    ]


class KyushuBackgroundAsteroidReward(KyushuMember, mineable.AsteroidRewardsGroupUltra):
    NAME = 'ku_ksu_background'
    SOLAR = asteroid.AsteroidTau37
    REWARD_ITEM = 'comm_roid_uranium'


class KyushuMineableField(mineable.MineableAsteroidField):
    BOX_SIZE = 1400
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.3
    DRIFT_Y = 0
    DRIFT_Z = 0.3


class KyushuUnlockAsteroidRewardField(mineable.AsteroidRewardField):
    ALIAS = 'ast'
    FIELD_CLASS = KyushuMineableField
    REWARDS_GROUP_CLASS = KyushuUnlockAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class KyushuBackgroundAsteroidRewardField(mineable.AsteroidRewardField):
    ALIAS = 'ast'
    FIELD_CLASS = KyushuMineableField
    REWARDS_GROUP_CLASS = KyushuBackgroundAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25
    ULTRA_REWARD = False


class KyushuRewardAsteroids1(KyushuMember, KyushuUnlockAsteroidRewardField):
    INDEX = 1
    ULTRA_BASE = KyushuAbandonedAstBase1


class KyushuRewardAsteroids2(KyushuMember, KyushuUnlockAsteroidRewardField):
    INDEX = 2
    ULTRA_BASE = KyushuAbandonedAstBase2


class KyushuRewardAsteroids3(KyushuMember, KyushuBackgroundAsteroidRewardField):
    INDEX = 3


class KyushuSun1(KyushuMember, main_objects.Sun):
    STAR = 'ku03_Sun1'
    LOADOUT = 'med_blue_sun_fx'


class KyushuSun2(KyushuMember, main_objects.Sun):
    INDEX = 2
    STAR = 'ku03_Sun1'
    LOADOUT = 'med_blue_sun_fx'


class KyushuTau4Jumpgate(KyushuMember, main_objects.Jumpgate):
    INDEX = 1
    REL = LEFT


class KyushuTau23Jumpgate(KyushuMember, main_objects.Jumpgate):
    INDEX = 2
    REL = RIGHT


class KyushuDockring(KyushuMember, main_objects.Dockring):
    BASE_INDEX = 1
    REL = RIGHT
    AUDIO_PREFIX = SpaceVoice.KU_PLANET
    INTERIOR_CLASS = interior.CustomFullSplitRoomInterior
    DEALERS = dealers.KusariPlanetDealers


class KyushuMiningDockring(KyushuMember, main_objects.Dockring):
    INDEX = 2
    BASE_INDEX = 2
    REL = TOP
    AUDIO_PREFIX = SpaceVoice.KU_PLANET
    INTERIOR_CLASS = interior.CustomFullSplitRoomInterior
    DEALERS = dealers.KusariPlanetDealers


class KyushuMegastation(KyushuMember, main_objects.Station):
    BASE_INDEX = 3
    REL = RIGHT
    REL_DRIFT = 1000
    SPACE_OBJECT_TEMPLATE = odissey.Odissey
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.KusariCivilianDealers


class KyushuShipyard(KyushuMember, main_objects.Shipyard):
    BASE_INDEX = 4
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = shipyards.HeavyBarrelShipyard
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.KusariCivilianDealers


class KyushuTrading(KyushuMember, main_objects.TradingBase):
    BASE_INDEX = 5
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = trade_storages.HokkaidoStorage
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.KusariCivilianDealers


class KyushuResearch(KyushuMember, main_objects.Station):
    ALIAS = 'research'
    BASE_INDEX = 6
    REL = LEFT
    SPACE_OBJECT_TEMPLATE = research.KyushuResearch
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.KusariCivilianDealers


class KyushuPolice(KyushuMember, main_objects.Outpost):
    ALIAS = 'police'
    BASE_INDEX = 7
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = police.BerlinPoliceOutpost
    INTERIOR_CLASS = interior.OutpostShipdealerInterior
    AUDIO_PREFIX = SpaceVoice.BORDER_STATION
    DEALERS = dealers.KusariMilitaryDealers


class KyushuLiner(KyushuMember, main_objects.LuxuryLiner):
    ALIAS = 'liner'
    BASE_INDEX = 8
    REL = LEFT
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.KusariCivilianDealers


class KyushuPlanet1(KyushuMember, main_objects.Planet):
    ARCHETYPE = 'planet_watblusmlcld_3000'
    SPHERE_RADIUS = 3000
    RELATED_DOCK_RING = KyushuDockring


class KyushuPlanet2(KyushuMember, main_objects.Planet):
    INDEX = 2
    ARCHETYPE = 'planet_desored_3000'
    SPHERE_RADIUS = 3000
    RELATED_DOCK_RING = KyushuMiningDockring


class KyushuPlanet3(KyushuMember, main_objects.Planet):
    INDEX = 3
    ARCHETYPE = 'planet_ice_blue_3000'
    SPHERE_RADIUS = 3000


class KyushuNorthAsteroidPirates(KyushuMember, main_objects.PirateBase):
    BASE_INDEX = 9
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = astbase.KyushuAsteroidBase
    FACTION = faction.KX_GRP

    DEFENCE_LEVEL = None

    INTERIOR_BG1 = interior.INTERIOR_BG_WALKER

    AUDIO_PREFIX = SpaceVoice.OUTPOST
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.KusariPirateDealers

    ASTEROID_ZONES = [
        KyushuAsteroidZone3,
    ]


class KyushuJunkers(KyushuMember, main_objects.PirateBase):
    INDEX = 2
    BASE_INDEX = 10
    REL = TOP
    SPACE_OBJECT_TEMPLATE = pirate.PirateBaseForbes
    FACTION = faction.JUNK_GRP

    DEFENCE_LEVEL = None

    AUDIO_PREFIX = SpaceVoice.OUTPOST
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.KusariPirateDealers

    ASTEROID_ZONES = [
        KyushuDebrisZone4,
    ]


class KyushuPoliceConn1(KyushuMember, main_objects.TradeConnection):
    OBJ_FROM = KyushuTau23Jumpgate
    OBJ_TO = KyushuPolice
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        KyushuNorthAsteroidPirates
    ]


class KyushuPoliceConn2(KyushuMember, main_objects.TradeConnection):
    OBJ_FROM = KyushuMegastation
    OBJ_TO = KyushuPolice
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        KyushuNorthAsteroidPirates
    ]


class KyushuPoliceConn3(KyushuMember, main_objects.TradeConnection):
    OBJ_FROM = KyushuPolice
    OBJ_TO = KyushuMiningDockring
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        KyushuNorthAsteroidPirates
    ]


class KyushuOdisseyConn1(KyushuMember, main_objects.TradeConnection):
    OBJ_FROM = KyushuMegastation
    OBJ_TO = KyushuResearch
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        KyushuNorthAsteroidPirates
    ]


class KyushuTradingConn1(KyushuMember, main_objects.TradeConnection):
    OBJ_FROM = KyushuResearch
    OBJ_TO = KyushuTrading
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        KyushuJunkers
    ]


class KyushuTradingConn2(KyushuMember, main_objects.TradeConnection):
    OBJ_FROM = KyushuTrading
    OBJ_TO = KyushuTau4Jumpgate
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        KyushuJunkers
    ]


class KyushuTradingConn3(KyushuMember, main_objects.TradeConnection):
    OBJ_FROM = KyushuTrading
    OBJ_TO = KyushuShipyard
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'F'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        KyushuJunkers
    ]


class KyushuMainPlanetConn1(KyushuMember, main_objects.TradeConnection):
    OBJ_FROM = KyushuShipyard
    OBJ_TO = KyushuDockring
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'G'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        KyushuJunkers
    ]


class KyushuMainPlanetConn2(KyushuMember, main_objects.TradeConnection):
    OBJ_FROM = KyushuDockring
    OBJ_TO = KyushuMiningDockring
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'H'
    HUNTER_DEFENCE_REL = LEFT


class KyushuLinerConn1(KyushuMember, main_objects.BuoyTradeConnection):
    OBJ_FROM = KyushuResearch
    OBJ_TO = KyushuLiner
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'I'


class KyushuLinerConn2(KyushuMember, main_objects.BuoyTradeConnection):
    OBJ_FROM = KyushuLiner
    OBJ_TO = KyushuPolice
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'J'
