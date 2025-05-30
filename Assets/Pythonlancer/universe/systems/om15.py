from fx.space import Dust
from fx.sound import Ambience

from managers.tools import query as Q
from world.names import *
from universe.content import meta

from universe import markets

from universe.content.member import Member
from universe.content.system_object import TOP, BOTTOM, LEFT, RIGHT
from universe.content import main_objects
from universe.content import zones
from universe.content import asteroid_definition
from universe.content import interior
from universe.content import dealers
from universe.audio.space_voice import SpaceVoice
from universe import faction
from universe.content import mineable
from templates.solar import asteroid as asteroid_solar
from templates.solar import hackable
from templates.nebula import om15_orange_nebula
from templates.nebula import exclusion

from templates.dockable import junker
from templates.dockable import trade_storages
from templates.dockable import rheinland_military
from templates.dockable import roid_mining
from templates.dockable import station_debris


class Omega15Member(Member):
    FACTION = faction.RheinlandMain
    INTERIOR_BG1 = interior.INTERIOR_BG_WALKER
    WEAPON_FACTION = WEAPON_RH
    EQUIP_FACTION = EQUIP_RH


class Om15RawText(Omega15Member, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = om15
space_color = 30, 15, 5
local_faction = rh_grp
space_farclip = 50000

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Dust]
spacedust = Dust

[Music]
space = music_omega_space
danger = music_omega_danger
battle = music_omega_battle

[Ambient]
color = 60, 30, 10

[Background]
nebulae = solar\\stars_mod\\om15_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_om15_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
;property_flags = 512 ;lava - MILITARY
property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = om15_System_Light
pos = 0, 0, 0
color = 255, 120, 50
range = 80000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION
'''


class Om15WalkerNebula(zones.NebulaZone):
    SPACEDUST = Dust.ATTRACT_ORANGE
    SPACEDUST_MAXPARTICLES = 40
    MUSIC = Ambience.NEBULA_WALKER
    INTERFERENCE = 0.5

    PROPERTY_FLAGS = 32768
    PROPERTY_FOG_COLOR = '150, 90, 20'


class Om15LargeNebula(Omega15Member, Om15WalkerNebula):
    INDEX = 1
    FILE_NAME = 'gen_om15_orange_nebula1'
    CONTENT_TEMPLATE = om15_orange_nebula.Omega15LargeNebulaTemplate


class Om15JunkerNebula(Omega15Member, Om15WalkerNebula):
    INDEX = 2
    FILE_NAME = 'gen_om15_orange_nebula2'
    CONTENT_TEMPLATE = om15_orange_nebula.Omega15SmallNebulaTemplate


class Om15RuinsNebula(Omega15Member, Om15WalkerNebula):
    INDEX = 3
    FILE_NAME = 'gen_om15_orange_nebula3'
    CONTENT_TEMPLATE = om15_orange_nebula.Omega15DangerNebulaTemplate


class Om15StoryNebula(Omega15Member, Om15WalkerNebula):
    ALIAS = 'story_neb'
    INDEX = 1
    FILE_NAME = 'gen_om15_orange_nebula4'
    CONTENT_TEMPLATE = om15_orange_nebula.Omega15NorthStoryNebulaTemplate
    MUSIC = Ambience.NEBULA_WALKER


WALKER_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.WALKER_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '255, 255, 255',
    'fog_far': 5000,
}


WALKER_DARK_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.WALKER_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '200, 160, 70',
    'fog_far': 5000,
}


class Om15AsteroidDefinition1(asteroid_definition.Omega15NiobiumAsteroidDefinition):
    ABSTRACT = False
    NAME = 'om15_main_astfield'
    DYNAST = True
    BELT = False
    BILLBOARDS = False
    LOOT = False # TEMP


class Om15AsteroidZone1(Omega15Member, zones.AsteroidZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = Om15AsteroidDefinition1
    SPACEDUST = Dust.LAVA
    SPACEDUST_MAXPARTICLES = 125
    MUSIC = Ambience.AST_LAVA


class Om15BaseRoidMiner(main_objects.RoidMiner):
    ALIAS = 'miner'
    ROTATE_RANDOM = True
    ARCHETYPE = 'Roid_Miner2'
    LOADOUT = 'roid_miner_om15'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    CARGO_PODS_LOADOUT = 'roid_miner_om15_cargo'

    AST_EXCLUSION_ZONE_SIZE = 2500
    ASTEROID_ZONES = [Om15AsteroidZone1]
    NEBULA_EXCLUSION_ZONE_SIZE = 3000
    EXCLUSION_PARAMS = WALKER_EXCLUSION_PARAMS
    NEBULA_ZONES = [Om15LargeNebula]
    NEBULA_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.LAVA,
        'spacedust_maxparticles': 200,
    }


class Om15RoidMiner1(Omega15Member, Om15BaseRoidMiner):
    INDEX = 1
    BASE_INDEX = 61


class Om15RoidMiner2(Omega15Member, Om15BaseRoidMiner):
    INDEX = 2
    BASE_INDEX = 62


class Om15RoidMiner3(Omega15Member, Om15BaseRoidMiner):
    INDEX = 3
    BASE_INDEX = 63


class Om15RoidMiner4(Omega15Member, Om15BaseRoidMiner):
    INDEX = 4
    BASE_INDEX = 64


class Om15RoidMiner5(Omega15Member, Om15BaseRoidMiner):
    INDEX = 5
    BASE_INDEX = 65


class Om15RoidMiner6(Omega15Member, Om15BaseRoidMiner):
    INDEX = 6
    BASE_INDEX = 66


class Om15RoidMiner7(Omega15Member, Om15BaseRoidMiner):
    INDEX = 7
    BASE_INDEX = 67


class Om15NiobiumAsteroidReward(Omega15Member, mineable.AsteroidRewardsGroupUltra):
    NAME = 'om15_niobium'
    SOLAR = asteroid_solar.AsteroidOmega15
    REWARD_ITEM = 'comm_roid_niobium'
    ULTRA_REWARD_BASES = [
        Om15RoidMiner1,
        Om15RoidMiner2,
        Om15RoidMiner3,
        Om15RoidMiner4,
        Om15RoidMiner5,
        Om15RoidMiner6,
        Om15RoidMiner7,
    ]


class Om15MineableField(mineable.MineableAsteroidField):
    BOX_SIZE = 1200
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.3
    DRIFT_Y = 0
    DRIFT_Z = 0.3


class Omega15BaseAsteroidRewardField(mineable.AsteroidRewardField):
    ALIAS = 'miner'
    FIELD_CLASS = Om15MineableField
    REWARDS_GROUP_CLASS = Om15NiobiumAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class Omega15RoidMinerAsteroids1(Omega15Member, Omega15BaseAsteroidRewardField):
    INDEX = 1
    ULTRA_BASE = Om15RoidMiner1


class Omega15RoidMinerAsteroids2(Omega15Member, Omega15BaseAsteroidRewardField):
    INDEX = 2
    ULTRA_BASE = Om15RoidMiner2


class Omega15RoidMinerAsteroids3(Omega15Member, Omega15BaseAsteroidRewardField):
    INDEX = 3
    ULTRA_BASE = Om15RoidMiner3


class Omega15RoidMinerAsteroids4(Omega15Member, Omega15BaseAsteroidRewardField):
    INDEX = 4
    ULTRA_BASE = Om15RoidMiner4


class Omega15RoidMinerAsteroids5(Omega15Member, Omega15BaseAsteroidRewardField):
    INDEX = 5
    ULTRA_BASE = Om15RoidMiner5


class Omega15RoidMinerAsteroids6(Omega15Member, Omega15BaseAsteroidRewardField):
    INDEX = 6
    ULTRA_BASE = Om15RoidMiner6


class Omega15RoidMinerAsteroids7(Omega15Member, Omega15BaseAsteroidRewardField):
    INDEX = 7
    ULTRA_BASE = Om15RoidMiner7


FIELD_TEMPLATE = '''
cube_size = 400
fill_dist = 1500
diffuse_color = 255, 140, 30
ambient_color = 40, 20, 0
ambient_increase = 60, 30, 10
empty_cube_frequency = 0.0
max_alpha = 0.300000
'''


CUBE_TEMPLATE = '''
xaxis_rotation = 8, 40, 90, 158
yaxis_rotation = 5, 45, 100, 135
zaxis_rotation = 355, 45, 78, 145
asteroid = mine_oxygen, 0.800000, -0.500000, -0.200000, 15, 90, 120, mine
asteroid = mine_oxygen, -0.300000, 0.600000, 0.800000, 85, 0, 185, mine
asteroid = mine_oxygen, 0.400000, -0.700000, -0.200000, 15, 90, 120, mine
asteroid = mine_oxygen, -0.300000, -0.300000, 0.800000, 85, 0, 185, mine
asteroid = mine_oxygen, -0.700000, 0.400000, -0.400000, 75, 30, 70, mine
'''


class Om15GasPockets(asteroid_definition.AsteroidDefinition):
    FIELD = True
    CUBE = True
    FIELD_TEMPLATE = FIELD_TEMPLATE
    CUBE_TEMPLATE = CUBE_TEMPLATE


class Om15GasPocketsZone1(Omega15Member, zones.AsteroidZone):
    ALIAS = 'pocket'
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = Om15GasPockets
    SPACEDUST = Dust.RADIOACTIVE_RED
    SPACEDUST_MAXPARTICLES = 200


class Om15Sun(Omega15Member, main_objects.SunSmall):
    STAR = 'Rh05_Sun'
    LOADOUT = 'med_yellow_sun_fx'
    ATMOSHPERE_RANGE = 11000

    LLIGHT_CLOUD = True
    LLIGHT_CLOUD_NAME = 'om15_light_cloud'
    LLIGHT_CLOUD_RANGE = 600000


class Om15BizmarkJumpgate(Omega15Member, main_objects.Jumpgate):
    INDEX = 1
    REL = RIGHT
    TARGET_SYSTEM_NAME = 'rh_biz'


class Om15StutJumpgate(Omega15Member, main_objects.Jumpgate):
    INDEX = 2
    REL = LEFT
    TARGET_SYSTEM_NAME = 'rh_stut'


class Om15MiningStation(Omega15Member, main_objects.RoidMinerStation):
    BASE_INDEX = 1
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = roid_mining.RheinlandRoidMining
    INTERIOR_CLASS = interior.OutpostShipdealerInterior
    DEALERS = dealers.RheinlandCivilianDealers
    SHIP_SET = markets.ShipSet('ge_csv')

    BASE_PROPS = meta.RoidMiningStation(
        objectives=[
            meta.ProduceBest(NIOBIUM),
        ],
    )


class Om15Outpost(Omega15Member, main_objects.Outpost):
    BASE_INDEX = 2
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = rheinland_military.KelnShort
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.RheinlandMilitaryDealers

    ASTEROID_ZONES = [Om15AsteroidZone1]
    AST_EXCLUSION_ZONE_SIZE = 4000

    NEBULA_EXCLUSION_ZONE_SIZE = 4000
    EXCLUSION_PARAMS = WALKER_EXCLUSION_PARAMS
    NEBULA_ZONES = [Om15LargeNebula]


class Om15Freeport(Omega15Member, main_objects.Freeport):
    BASE_INDEX = 3
    REL = TOP
    SPACE_OBJECT_TEMPLATE = trade_storages.RheinlandOmegaStorage
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.RheinlandMilitaryDealers


class Om15Junkers(Omega15Member, main_objects.JunkerBase):
    ALIAS = 'junker'
    BASE_INDEX = 4
    REL = TOP
    SPACE_OBJECT_TEMPLATE = junker.OmegaSmelter
    FACTION = faction.Junkers

    DEFENCE_LEVEL = None

    AUDIO_PREFIX = SpaceVoice.OUTPOST
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.RheinlandPirateDealers

    NEBULA_EXCLUSION_ZONE_SIZE = 2000
    EXCLUSION_PARAMS = WALKER_EXCLUSION_PARAMS
    NEBULA_ZONES = [
        Om15JunkerNebula,
    ]


class Om15AbandonedStation(Omega15Member, main_objects.StationRuins):
    ALIAS = 'ruins'
    INDEX = 1
    REL = RIGHT

    SPACE_OBJECT_TEMPLATE = station_debris.OmegaDanzigDebris

    ASTEROID_ZONES = [
        Om15GasPocketsZone1,
    ]
    AST_EXCLUSION_ZONE_SIZE = 4000

    NEBULA_EXCLUSION_ZONE_SIZE = 2000
    EXCLUSION_PARAMS = WALKER_EXCLUSION_PARAMS
    NEBULA_ZONES = [
        Om15RuinsNebula,
    ]


class Om15AbandonedStationDropPoint1(Omega15Member, main_objects.HackableStation):
    ALIAS = 'ruins_dock'
    INDEX = 1
    BASE_INDEX = 51
    RELATED_OBJECT = Om15AbandonedStation
    RELATED_OBJECT_INDEX = 0
    HACKABLE_SOLAR_CLASS = hackable.HackableOutpost
    INTERIOR_CLASS = interior.EquipDeckInterior


class Om15AbandonedStationDropPoint2(Omega15Member, main_objects.HackableStation):
    ALIAS = 'ruins_dock'
    INDEX = 2
    BASE_INDEX = 52
    RELATED_OBJECT = Om15AbandonedStation
    RELATED_OBJECT_INDEX = 1
    HACKABLE_SOLAR_CLASS = hackable.HackableOutpost
    INTERIOR_CLASS = interior.EquipDeckInterior


class Om15Planet1(Omega15Member, main_objects.Planet):
    INDEX = 1
    ARCHETYPE = 'planet_moonred_3000'
    SPHERE_RADIUS = 3000


class Om15Planet2(Omega15Member, main_objects.Planet):
    INDEX = 2
    ARCHETYPE = 'planet_gasyelcld_3000'
    SPHERE_RADIUS = 3000


class Om15VirtualDepot(Omega15Member, main_objects.VirtualDepot):
    REL = TOP


class Om15PoliceConn1(Omega15Member, main_objects.TradeConnection):
    OBJ_FROM = Om15Outpost
    OBJ_TO = Om15BizmarkJumpgate
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = LEFT


class Om15PoliceConn2(Omega15Member, main_objects.TradeConnection):
    OBJ_FROM = Om15Outpost
    OBJ_TO = Om15MiningStation
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        Om15Junkers,
    ]


class Om15FreeportConn1(Omega15Member, main_objects.TradeConnection):
    OBJ_FROM = Om15Freeport
    OBJ_TO = Om15MiningStation
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        Om15Junkers,
    ]


class Om15FreeportConn2(Omega15Member, main_objects.TradeConnection):
    OBJ_FROM = Om15Freeport
    OBJ_TO = Om15StutJumpgate
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        Om15Junkers,
    ]


class Om15VirtualConn1(Omega15Member, main_objects.BrokenTradeConnection):
    OBJ_FROM = Om15VirtualDepot
    OBJ_TO = Om15Freeport
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        Om15Junkers,
    ]


class Om15VirtualConn2(Omega15Member, main_objects.BrokenTradeConnection):
    OBJ_FROM = Om15VirtualDepot
    OBJ_TO = Om15BizmarkJumpgate
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'F'
    HUNTER_DEFENCE_REL = TOP


class Om15StoryCorsairBase(Omega15Member, main_objects.VirtualDepot):
    ALIAS = 'story_excl'
    INDEX = 1

    EXCLUSION_PARAMS = WALKER_EXCLUSION_PARAMS
    NEBULA_EXCLUSION_ZONE_SIZE = 6000
    NEBULA_ZONES = [
        Om15StoryNebula
    ]


class Om15StoryCorsairDepot(Omega15Member, main_objects.VirtualDepot):
    ALIAS = 'story_excl'
    INDEX = 2

    EXCLUSION_PARAMS = WALKER_EXCLUSION_PARAMS
    NEBULA_EXCLUSION_ZONE_SIZE = 3000
    NEBULA_ZONES = [
        Om15StoryNebula
    ]
