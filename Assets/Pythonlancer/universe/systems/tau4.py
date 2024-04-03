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
from templates.solar import hackable
from templates.solar import debris_box
from templates.solar import suprise
from templates.nebula import tau4_nebula
from templates.nebula import exclusion

from templates.dockable import astbase
from templates.dockable import shipyards
from templates.dockable import trade_storages
from templates.dockable import prisons
from templates.dockable import police
from templates.dockable import columbia_production
from templates.dockable import pirate
from templates.dockable import junker
from templates.dockable import station_debris


class Tau4Member(object):
    INDEX = 1
    ABSTRACT = False
    FACTION = faction.KU_GRP

    INTERIOR_BG1 = interior.INTERIOR_TAU4


class Tau4StaticText(Tau4Member, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = tau4
space_color = 50, 35, 20
local_faction = ku_grp
space_farclip = 50000

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Dust]
spacedust = Dust

[Music]
space = music_tau_space
danger = music_tau_danger
battle = music_tau_battle

[Ambient]
color = 40, 27, 12

[Background]
nebulae = solar\\stars_mod\\tau4_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_tau4_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
;property_flags = 512 ;lava - MILITARY
property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = tau4_system_light
pos = 0, 2, 0
color = 255, 200, 200
range = 150000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION
'''


class Tau4AsteroidDefinition1(asteroid_definition.TekagiAsteroidDefinition):
    BELT = True
    BILLBOARDS = True
    DYNAST = True
    LOOT = False  # TEMP


class Tau4AsteroidZone1(Tau4Member, zones.AsteroidZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = Tau4AsteroidDefinition1


class Tau4AbandonedAstBase1(Tau4Member, main_objects.AbandonedAsteroid):
    ALIAS = 'ast'
    INDEX = 1
    BASE_INDEX = 51
    ROTATE_RANDOM = True
    ARCHETYPE = 'miningbase_mineableA'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        Tau4AsteroidZone1,
    ]
    AST_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.ASTEROID,
        'spacedust_maxparticles': 200,
    }


class Tau4AsteroidReward(Tau4Member, mineable.AsteroidRewardsGroupUltra):
    NAME = 'tau4_unlock'
    SOLAR = asteroid.AsteroidTekagi
    REWARD_ITEM = 'comm_roid_uranium'
    ULTRA_REWARD_BASES = [
        Tau4AbandonedAstBase1,
    ]


class Tau4MineableField(mineable.MineableAsteroidField):
    BOX_SIZE = 1400
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.3
    DRIFT_Y = 0
    DRIFT_Z = 0.3


class Tau4BaseAsteroidRewardField(mineable.AsteroidRewardField):
    ALIAS = 'ast'
    FIELD_CLASS = Tau4MineableField
    REWARDS_GROUP_CLASS = Tau4AsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class Tau4RewardAsteroids1(Tau4Member, Tau4BaseAsteroidRewardField):
    INDEX = 1
    ULTRA_BASE = Tau4AbandonedAstBase1


class Tau4Sun(Tau4Member, main_objects.Sun):
    STAR = 'Bw10_Sun'
    LOADOUT = 'small_blue_sun_fx'


class Tau4BaseWhiteNebula(zones.NebulaZone):
    MUSIC = Ambience.NEBULA_BARRIER
    INTERFERENCE = 0.5

    PROPERTY_FLAGS = 32768
    PROPERTY_FOG_COLOR = '150, 100, 20'


class Tau4SouthWestNebula(Tau4Member, Tau4BaseWhiteNebula):
    INDEX = 1
    CONTENT_TEMPLATE = tau4_nebula.Tau4WhiteNebulaTemplate


class Tau4XenosNorthNebula(Tau4Member, Tau4BaseWhiteNebula):
    INDEX = 2
    CONTENT_TEMPLATE = tau4_nebula.Tau4WhiteNebulaTemplate


class Tau4CorsairJumpNebula(Tau4Member, Tau4BaseWhiteNebula):
    INDEX = 3
    CONTENT_TEMPLATE = tau4_nebula.Tau4WhiteNebulaTemplate


WHITE_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.GENERIC_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '95, 73, 67',
    'fog_far': 5000,
}


class Tau4BasePrisonLiner(main_objects.LockedBattleship):
    ALIAS = 'prison_liner'
    ROTATE_RANDOM = True
    ARCHETYPE = 'suprise_prison_liner'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True
    AST_EXCLUSION_ZONE_SIZE = 600

    NEBULA_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.RADIOACTIVE_RED,
        'spacedust_maxparticles': 200,
    }


class Tau4BaseMinesZone(zones.AsteroidZone):
    ASTEROID_DEFINITION_CLASS = asteroid_definition.SpaceMines
    ALIAS = 'prison_liner'
    SPACEDUST = Dust.DEBRIS
    SPACEDUST_MAXPARTICLES = 100
    MUSIC = Ambience.MINE_AST
    INTERFERENCE = 0.1
    DRAG_MODIFIER = 1.5
    PROPERTY_FLAGS = 4128


class Tau4SolarMinesZone1(Tau4Member, Tau4BaseMinesZone):
    INDEX = 1


class Tau4SolarMinesZone2(Tau4Member, Tau4BaseMinesZone):
    INDEX = 2


class Tau4PrisonLiner1(Tau4Member, Tau4BasePrisonLiner):
    INDEX = 1
    BASE_INDEX = 52
    ASTEROID_ZONES = [
        Tau4SolarMinesZone1,
    ]


class Tau4PrisonLiner2(Tau4Member, Tau4BasePrisonLiner):
    INDEX = 2
    BASE_INDEX = 53
    ASTEROID_ZONES = [
        Tau4SolarMinesZone2,
    ]


class Tau4LinerSupriseRewards(Tau4Member, mineable.DefaultSupriseRewardsGroup):
    NAME = 'tau4_prison_liner_suprise'
    SOLAR = suprise.KusariAllFighter
    REWARD_ITEM = None
    ULTRA_REWARD_BASES = [
        Tau4PrisonLiner1,
        Tau4PrisonLiner2,
    ]


class Tau4SolarSupriseField(mineable.DefaultField):
    BOX_SIZE = 400
    DENSITY_MULTIPLER = 4
    DRIFT_X = 0.5
    DRIFT_Y = 0.5
    DRIFT_Z = 0.5
    EMPTY_CHANCE = 0.2


class Tau4BaseSolarSupriseRewardField(mineable.SupriseRewardField):
    ALIAS = 'prison_liner'
    FIELD_CLASS = Tau4SolarSupriseField
    REWARDS_GROUP_CLASS = Tau4LinerSupriseRewards
    ULTRA_REWARD = True


class Tau4SolarSupriseRewardField1(Tau4Member, Tau4BaseSolarSupriseRewardField):
    INDEX = 1
    ULTRA_BASE = Tau4PrisonLiner1


class Tau4SolarSupriseRewardField2(Tau4Member, Tau4BaseSolarSupriseRewardField):
    INDEX = 2
    ULTRA_BASE = Tau4PrisonLiner2


class Tau4KyushuJumpgate(Tau4Member, main_objects.Jumpgate):
    INDEX = 1
    REL = LEFT


class Tau4HokkaidoJumpgate(Tau4Member, main_objects.Jumpgate):
    INDEX = 2
    REL = RIGHT


class Tau4Station(Tau4Member, main_objects.Station):
    BASE_INDEX = 1
    REL = TOP
    SPACE_OBJECT_TEMPLATE = columbia_production.ColumbiaSmallProduction
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.KusariCivilianDealers


class Tau4Freeport(Tau4Member, main_objects.Freeport):
    BASE_INDEX = 2
    REL = BOTTOM
    REL_APPEND = 2500
    SPACE_OBJECT_TEMPLATE = trade_storages.LibertyLongStorage
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.KusariCivilianDealers


class Tau4Battleship(Tau4Member, main_objects.KusariBattleship):
    BASE_INDEX = 3
    REL = BOTTOM
    REL_APPEND = 2500
    INTERIOR_CLASS = interior.BattleshipInterior
    DEALERS = dealers.KusariMilitaryDealers


class Tau4Planet1(Tau4Member, main_objects.Planet):
    ARCHETYPE = 'planet_desorcld_3000'
    SPHERE_RADIUS = 3000


class Tau4Planet2(Tau4Member, main_objects.Planet):
    INDEX = 2
    ARCHETYPE = 'planet_icemntcld_4000'
    SPHERE_RADIUS = 4000


class Tau4Planet3(Tau4Member, main_objects.Planet):
    INDEX = 3
    ARCHETYPE = 'planet_icewatcld_3000'
    SPHERE_RADIUS = 3000



class Tau4SouthPirates(Tau4Member, main_objects.PirateBase):
    INDEX = 1
    BASE_INDEX = 4
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = pirate.PirateBaseBizmark
    FACTION = faction.CO_GRP

    DEFENCE_LEVEL = None

    AUDIO_PREFIX = SpaceVoice.OUTPOST
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.KusariPirateDealers

    NEBULA_ZONES = [
        Tau4SouthWestNebula
    ]
    EXCLUSION_PARAMS = WHITE_EXCLUSION_PARAMS
    NEBULA_EXCLUSION_ZONE_SIZE = 2000


class Tau4Xenos(Tau4Member, main_objects.PirateBase):
    INDEX = 2
    BASE_INDEX = 5
    REL = TOP
    SPACE_OBJECT_TEMPLATE = pirate.PirateBaseCalifornia
    FACTION = faction.CO_GRP

    DEFENCE_LEVEL = None

    AUDIO_PREFIX = SpaceVoice.OUTPOST
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.KusariPirateDealers

    NEBULA_ZONES = [
        Tau4XenosNorthNebula
    ]
    EXCLUSION_PARAMS = WHITE_EXCLUSION_PARAMS


class Tau4BattleshipRuins1(Tau4Member, main_objects.HackableBattleship):
    ALIAS = 'bship_ruins'
    INDEX = 1
    BASE_INDEX = 61
    REL = BOTTOM
    HACKABLE_SOLAR_CLASS = hackable.HackableKusariBattleship
    INTERIOR_CLASS = interior.EquipDeckInterior


class Tau4LuxuryRuins1(Tau4Member, main_objects.HackableBattleship):
    ALIAS = 'luxury'
    INDEX = 1
    BASE_INDEX = 62
    REL = TOP
    HACKABLE_SOLAR_CLASS = hackable.HackableLuxuryLiner
    INTERIOR_CLASS = interior.EquipDeckInterior


class Tau4StationConn1(Tau4Member, main_objects.TradeConnection):
    OBJ_FROM = Tau4KyushuJumpgate
    OBJ_TO = Tau4Station
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        Tau4SouthPirates
    ]


class Tau4StationConn2(Tau4Member, main_objects.TradeConnection):
    OBJ_FROM = Tau4Station
    OBJ_TO = Tau4Freeport
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        Tau4SouthPirates
    ]


class Tau4BattleshipConn1(Tau4Member, main_objects.TradeConnection):
    OBJ_FROM = Tau4Freeport
    OBJ_TO = Tau4Battleship
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        Tau4SouthPirates
    ]


class Tau4BattleshipConn2(Tau4Member, main_objects.TradeConnection):
    OBJ_FROM = Tau4Battleship
    OBJ_TO = Tau4HokkaidoJumpgate
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        Tau4Xenos
    ]


class Tau4SpragueConn1(Tau4Member, main_objects.AbandonedBuoyTradeConnection):
    OBJ_FROM = Tau4Station
    OBJ_TO = Tau4LuxuryRuins1
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'E'
    ATTACKED_BY = [
        Tau4Xenos
    ]


class Tau4BattleshipRuinsConn1(Tau4Member, main_objects.AbandonedBuoyTradeConnection):
    OBJ_FROM = Tau4BattleshipRuins1
    OBJ_TO = Tau4Freeport
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'E'
