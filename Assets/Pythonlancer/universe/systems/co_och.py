from fx.space import Dust, JumpholeEffect
from fx.sound import Ambience
from universe.audio.space_voice import SpaceVoice, SpaceCostume

from managers.tools import query as Q
from world.names import *
from universe.content import meta

from universe import markets

from universe.content.member import Member
from universe.content.system_object import LEFT, RIGHT, TOP
from universe.content import main_objects
from universe.content import zones
from universe.content import interior
from universe.content import dealers
from universe.content import asteroid_definition
from universe import faction
from universe.content import mineable
from templates.solar import asteroid
from templates.nebula import co_och_nebula
from templates.nebula import exclusion
from templates.dockable import corsair_dreadnought

from templates.solar import dyson_rubic

from text.strings import MultiString as MS


class OchoMember(Member):
    FACTION = faction.Corsairs
    INTERIOR_BG1 = interior.INTERIOR_CO_OCHO_RIOS
    INTERIOR_BG2 = interior.INTERIOR_STARS
    WEAPON_FACTION = WEAPON_BW
    EQUIP_FACTION = EQUIP_BW
    AST_TYPE = 'ku_tgk'


class OchoStaticText(OchoMember, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = co_och
space_color = 0, 0, 0
local_faction = co_grp
space_farclip = 50000

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Dust]
spacedust = Dust

[Music]
space = music_omicron_space
danger = music_omicron_danger
battle = music_omicron_battle

[Ambient]
color = 25, 35, 25

[Background]
nebulae = solar\\stars_mod\\co_och_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_co_och_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
property_flags = 512 ;lava - MILITARY
;property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = co_Ocho_Rios_system_light
pos = 0, 0, 0
color = 153, 200, 253
range = 120000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION
'''


class OchoSun(OchoMember, main_objects.Sun):
    STAR = 'Ku03_sun2'
    LOADOUT = 'small_blue_sun_fx'


class OchBaseEdgeNebula(zones.NebulaZone):
    MUSIC = Ambience.ASTEROID_NOMAD
    INTERFERENCE = 0.5

    SPACEDUST = Dust.ATTRACT_GREEN
    SPACEDUST_MAXPARTICLES = 100

    PROPERTY_FLAGS = 32768
    PROPERTY_FOG_COLOR = '150, 100, 20'


class OchBaseWalkerNebula(zones.NebulaZone):
    MUSIC = Ambience.ASTEROID_NOMAD
    INTERFERENCE = 0.5

    SPACEDUST = Dust.ATTRACT_GREEN
    SPACEDUST_MAXPARTICLES = 100

    PROPERTY_FLAGS = 32768
    PROPERTY_FOG_COLOR = '150, 100, 20'


EDGE_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.LINES_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '50, 150, 50',
    'fog_far': 5000,
}


EDGE_EXCLUSION_PARAMS2 = {
    'zone_shell': exclusion.VORTEX_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '150, 180, 160',
    'fog_far': 2500,
}


WALKER_EXCLUSION_PARAMS = {
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '200, 200, 200',
    'fog_far': 5000,
}


class OchNomadNebula(OchoMember, OchBaseEdgeNebula):
    INDEX = 1
    CONTENT_TEMPLATE = co_och_nebula.OchEdgeNebulaTemplate


class OchWalkerNebula(OchoMember, OchBaseEdgeNebula):
    INDEX = 2
    CONTENT_TEMPLATE = co_och_nebula.OchWalkerNebulaTemplate

#
# class OchoOmegaStorage(OchoMember, main_objects.SmugglerStoragePoint):
#     INDEX = 1


class OchoLargeAsteroidDefinition(asteroid_definition.TekagiAsteroidDefinition):
    BELT = True
    BILLBOARDS = True
    DYNAST = True
    LOOT = False  # TEMP
    BELT_HEIGHT = 8000


class OchoSmallAsteroidDefinition(asteroid_definition.TekagiAsteroidDefinition):
    BELT = True
    BILLBOARDS = True
    DYNAST = True
    LOOT = False  # TEMP


class OchoNomadAsteroidDefinition(asteroid_definition.NomadDynasteroids):
    pass


class OchoAsteroidZone1(OchoMember, zones.AsteroidZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = OchoLargeAsteroidDefinition
    MUSIC = Ambience.AST_ROCK

    SPACEDUST = Dust.ASTEROID
    SPACEDUST_MAXPARTICLES = 200


class OchoAsteroidZone2(OchoMember, zones.AsteroidZone):
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = OchoLargeAsteroidDefinition
    MUSIC = Ambience.AST_ROCK

    SPACEDUST = Dust.ASTEROID
    SPACEDUST_MAXPARTICLES = 200


class OchoAsteroidZone3(OchoMember, zones.AsteroidZone):
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = OchoNomadAsteroidDefinition


class OchoAsteroidZone4(OchoMember, zones.AsteroidZone):
    INDEX = 4
    ASTEROID_DEFINITION_CLASS = OchoSmallAsteroidDefinition
    MUSIC = Ambience.AST_ROCK

    SPACEDUST = Dust.ASTEROID
    SPACEDUST_MAXPARTICLES = 200


class BaseOchoAst1Static(main_objects.AutoStaticObject):
    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        OchoAsteroidZone1,
    ]


class BaseOchoAst2Static(main_objects.AutoStaticObject):
    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        OchoAsteroidZone2,
    ]


class OchoStaticAst1(OchoMember, BaseOchoAst1Static):
    INDEX = 1


class OchoStaticAst2(OchoMember, BaseOchoAst1Static):
    INDEX = 2


class OchoStaticAst3(OchoMember, BaseOchoAst1Static):
    INDEX = 3


class OchSuprise1(main_objects.SupriseSattelite):
    ALIAS = 'suprise1'
    ARCHETYPE = 'suprise_pi_freighter'
    OFFSET = [-350, -150, 200]
    ROTATE_RANDOM = True
    ORIENT_TOGETHER = True


class OchSuprise2(main_objects.SupriseSattelite):
    ALIAS = 'suprise2'
    ARCHETYPE = 'suprise_bw_elite2'
    OFFSET = [-150, -250, 100]
    ROTATE_RANDOM = True
    ORIENT_TOGETHER = True


class OchoStaticAst4(OchoMember, BaseOchoAst2Static):
    INDEX = 4
    SATTELITES = [OchSuprise1, OchSuprise2]


class OchoStaticAst5(OchoMember, BaseOchoAst2Static):
    INDEX = 5


class OchoStaticAst6(OchoMember, BaseOchoAst2Static):
    INDEX = 6


class OchWalkerSuprise1(main_objects.SupriseSattelite):
    ALIAS = 'suprise_wlk1'
    ARCHETYPE = 'suprise_ku_freighter'
    OFFSET = [255, -205, 150]
    ROTATE_RANDOM = True
    ORIENT_TOGETHER = True


class OchoStaticAst8(OchoMember, main_objects.AutoStaticObject):
    INDEX = 8
    SATTELITES = [OchWalkerSuprise1]

    NEBULA_ZONES = [
        OchWalkerNebula
    ]
    EXCLUSION_PARAMS = WALKER_EXCLUSION_PARAMS
    NEBULA_EXCLUSION_ZONE_SIZE = 5000


class OchSuprise3(main_objects.SupriseSattelite):
    ALIAS = 'suprise3'
    ARCHETYPE = 'suprise_bw_freighter'
    OFFSET = [115, -55, 210]
    ROTATE_RANDOM = True
    ORIENT_TOGETHER = True


class OchSuprise4(main_objects.SupriseSattelite):
    ALIAS = 'suprise4'
    ARCHETYPE = 'suprise_pi_elite'
    OFFSET = [-250, 310, 100]
    ROTATE_RANDOM = True
    ORIENT_TOGETHER = True


class OchSuprise5(main_objects.SupriseSattelite):
    ALIAS = 'suprise5'
    ARCHETYPE = 'suprise_bw_fighter'
    OFFSET = [-450, 150, -200]
    ROTATE_RANDOM = True
    ORIENT_TOGETHER = True


class OchoStaticAst7(OchoMember, BaseOchoAst1Static):
    INDEX = 7
    SATTELITES = [OchSuprise3, OchSuprise4, OchSuprise5]

    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        OchoAsteroidZone2,
    ]


class OchoLargeAsteroidBase(OchoMember, main_objects.PirateAsteroid):
    ALIAS = 'astbase'
    INDEX = 1
    BASE_INDEX = 1
    ARCHETYPE = 'co_base_rock_large02'
    LOADOUT = 'co_base_rock_large01_pi_01'
    INTERIOR_CLASS = interior.CustomFullSplitRoomInterior
    DEFENCE_LEVEL = None
    RU_NAME = MS('База Очо-Р+иос', "Ocho-Rios Base")
    SHIP_SET = markets.ShipSet('co_fighter')
    CALC_STORE = False
    HAVE_CHARACTERS = False
    DEALERS = dealers.RheinlandPirateDealers

    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        OchoAsteroidZone1,
    ]
    EQUIP_SET = markets.EquipSet(
        Q.Gun('bw_corsairgun', eq_classes=markets.SECRET3),
    )


class OchoLargeDread(OchoMember, main_objects.Station):
    ALIAS = 'dread'
    BASE_INDEX = 2
    REL = LEFT
    SPACE_OBJECT_TEMPLATE = corsair_dreadnought.CorsairDreadnoughtAlive
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.RheinlandPirateDealers
    CALC_STORE = False
    HAVE_CHARACTERS = False

    AST_EXCLUSION_ZONE_SIZE = 4000
    ASTEROID_ZONES = [
        OchoAsteroidZone4,
    ]

    RU_NAME = MS('Линкор Конкорд', 'Battleship Concord')


class OchoMetro1(OchoMember, main_objects.MetroMiningOne):
    INDEX = 1

    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        OchoAsteroidZone2,
    ]


class OchoMetro2(OchoMember, main_objects.MetroMiningTwo):
    INDEX = 2

    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        OchoAsteroidZone2,
    ]


class OchoMetro3(OchoMember, main_objects.MetroMiningOne):
    INDEX = 3

    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        OchoAsteroidZone2,
    ]


class OchoMetro4(OchoMember, main_objects.MetroMiningTwo):
    INDEX = 4

    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        OchoAsteroidZone2,
    ]


class OchNomadObelisk(main_objects.Sattelite):
    ALIAS = 'no_core1'
    ARCHETYPE = 'domkavash_generator'
    OFFSET = [240, -315, 70]
    ROTATE = [0, -61, 0]


class OchoNomadStaticAst(OchoMember, main_objects.AutoStaticObject):
    INDEX = 9
    SATTELITES = [OchNomadObelisk]

    AST_EXCLUSION_ZONE_SIZE = 4000
    ASTEROID_ZONES = [
        OchoAsteroidZone3,
    ]
    AST_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.ORGANISM,
        'spacedust_maxparticles': 200,
        'music': Ambience.NOMAD
    }

    NEBULA_ZONES = [
        OchNomadNebula
    ]
    EXCLUSION_PARAMS = EDGE_EXCLUSION_PARAMS
    NEBULA_EXCLUSION_ZONE_SIZE = 5000


class OchoResearchBase1(OchoMember, main_objects.AbandonedAsteroid):
    ALIAS = 'scient'
    INDEX = 1
    BASE_INDEX = 51
    ROTATE_RANDOM = True
    ARCHETYPE = 'miningbase_nomad'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    RU_NAME = MS('База Магеллан', "Magellan Base")

    INTERIOR_BG1 = interior.INTERIOR_BG_EDGE
    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        OchoAsteroidZone3,
    ]
    AST_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.ASTEROID,
        'spacedust_maxparticles': 200,
    }

    NEBULA_ZONES = [
        OchNomadNebula
    ]
    EXCLUSION_PARAMS = EDGE_EXCLUSION_PARAMS

    MISC_EQUIP_TYPE = RH_PIRATE
    WEAPON_FACTION = WEAPON_RH
    EQUIP_SET = markets.EquipSet(
        Q.Gun('rh_junkergun', eq_classes=markets.SECRET2),
        Q.Engine(None, eq_classes=markets.SECRET2),
    )


class OchoResearchBase2(OchoMember, main_objects.AbandonedAsteroid):
    ALIAS = 'scient'
    INDEX = 2
    BASE_INDEX = 52
    ROTATE_RANDOM = True
    ARCHETYPE = 'miningbase_nomad'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    RU_NAME = MS('База Олдрин', "Aldrin Base")

    INTERIOR_BG1 = interior.INTERIOR_BG_EDGE
    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        OchoAsteroidZone3,
    ]
    AST_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.ASTEROID,
        'spacedust_maxparticles': 200,
    }

    NEBULA_ZONES = [
        OchNomadNebula
    ]
    EXCLUSION_PARAMS = EDGE_EXCLUSION_PARAMS

    MISC_EQUIP_TYPE = RH_PIRATE
    WEAPON_FACTION = WEAPON_RH
    EQUIP_SET = markets.EquipSet(
        Q.Gun('rh_junkergun', eq_classes=markets.SECRET2),
        Q.Engine(None, eq_classes=markets.SECRET2),
    )


class OchoNomadAsteroidReward(OchoMember, mineable.AsteroidRewardsGroupUltra):
    NAME = 'ocho_rios_nomad'
    SOLAR = asteroid.AsteroidNomadGreen
    REWARD_ITEM = 'comm_roid_niobium'
    ULTRA_REWARD_BASES = [
        OchoResearchBase1,
        OchoResearchBase2,
    ]


class OchoResearchAsteroids1(OchoMember, mineable.AsteroidRewardField):
    ALIAS = 'scient'
    INDEX = 1
    FIELD_CLASS = mineable.MineableAsteroidField
    REWARDS_GROUP_CLASS = OchoNomadAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True
    ULTRA_BASE = OchoResearchBase1


class OchoResearchAsteroids2(OchoMember, mineable.AsteroidRewardField):
    ALIAS = 'scient'
    INDEX = 2
    FIELD_CLASS = mineable.MineableAsteroidField
    REWARDS_GROUP_CLASS = OchoNomadAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True
    ULTRA_BASE = OchoResearchBase2



NO_FIELD_TEMPLATE = '''
cube_size = 400
fill_dist = 1500
diffuse_color = 100, 150, 255
ambient_color = 100, 200, 255
ambient_increase = 20, 30, 255
empty_cube_frequency = 0.000000
max_alpha = 0.400000
'''

NO_CUBE_TEMPLATE = '''
asteroid = mine_oxygen, 0.800000, -0.500000, -0.200000, 15, 90, 120, mine
asteroid = mine_oxygen, -0.300000, 0.600000, 0.800000, 85, 0, 185, mine
asteroid = mine_oxygen, 0.400000, -0.700000, -0.200000, 15, 90, 120, mine
asteroid = mine_oxygen, -0.300000, -0.300000, 0.800000, 85, 0, 185, mine
asteroid = mine_oxygen, -0.700000, 0.400000, -0.400000, 75, 30, 70, mine
'''

TRN_FIELD_TEMPLATE = '''
cube_size = 1000 ;single version
;cube_size = 3300 ;multiple version
fill_dist = 2000 
empty_cube_frequency = 0.000000
'''

TRN_CUBE_TEMPLATE = '''
asteroid = mod_red_biglair02, -0.80, -0.75, -0.70, 27, 154, 293
asteroid = mod_red_biglair01, -0.65, -0.60, -0.55, 312, 89, 175
asteroid = mod_red_biglair02, -0.50, -0.45, -0.40, 84, 231, 46
asteroid = mod_red_biglair01, -0.35, -0.30, -0.25, 198, 347, 268
asteroid = mod_red_biglair02, -0.20, -0.15, -0.10, 43, 112, 359
asteroid = mod_red_biglair01, -0.05, 0.00, 0.05, 271, 56, 134
asteroid = mod_red_biglair02, 0.10, 0.15, 0.20, 156, 298, 77
asteroid = mod_red_biglair01, 0.25, 0.30, 0.35, 335, 183, 212
asteroid = mod_red_biglair02, 0.40, 0.45, 0.50, 68, 45, 341
asteroid = mod_red_biglair01, 0.55, 0.60, 0.65, 247, 364, 108
asteroid = mod_red_biglair02, 0.70, 0.75, 0.80, 139, 73, 286
asteroid = mod_red_biglair01, -0.78, -0.38, 0.02, 32, 259, 165
asteroid = mod_red_biglair02, 0.42, 0.72, -0.48, 295, 141, 48
asteroid = mod_red_biglair01, -0.22, 0.58, -0.72, 113, 316, 227
asteroid = mod_red_biglair02, 0.68, -0.28, 0.28, 186, 65, 302
asteroid = mod_red_biglair01, -0.52, -0.72, 0.62, 51, 278, 89
asteroid = mod_red_biglair02, 0.32, 0.82, -0.18, 344, 129, 14
asteroid = mod_red_biglair01, -0.62, 0.22, -0.32, 221, 96, 357
asteroid = mod_red_biglair02, 0.78, -0.62, -0.12, 79, 210, 146
asteroid = mod_red_biglair01, -0.12, -0.52, 0.78, 163, 305, 233
asteroid = mod_red_biglair02, 0.23, -0.77, 0.43, 288, 53, 71
asteroid = mod_red_biglair01, -0.43, 0.73, -0.23, 107, 387, 198
asteroid = mod_red_biglair02, 0.53, 0.13, -0.83, 254, 172, 49
asteroid = mod_red_biglair01, -0.73, -0.13, 0.63, 41, 249, 310
asteroid = mod_red_biglair02, 0.13, -0.63, -0.33, 315, 104, 135
asteroid = mod_red_biglair01, -0.83, 0.43, 0.73, 177, 338, 266
asteroid = mod_red_biglair02, 0.63, 0.83, -0.53, 62, 187, 59
asteroid = mod_red_biglair01, -0.33, -0.83, 0.13, 228, 42, 324
asteroid = mod_red_biglair02, 0.83, -0.33, -0.63, 93, 263, 181
asteroid = mod_red_biglair01, -0.53, 0.63, 0.33, 355, 116, 42

'''


class OchoRubicNomadAst(asteroid_definition.AsteroidDefinition):
    FIELD = True
    CUBE = True
    FIELD_TEMPLATE = TRN_FIELD_TEMPLATE
    CUBE_TEMPLATE = TRN_CUBE_TEMPLATE


class OchoRubicAstZone1(OchoMember, zones.AsteroidZone):
    ALIAS = 'rubic'
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = OchoRubicNomadAst
    SPACEDUST = Dust.ATTRACT_PURPLE
    SPACEDUST_MAXPARTICLES = 200
    DRAG_MODIFIER = 1.3
    INTERFERENCE = 0.5


class OchoNomadGate(OchoMember, main_objects.Jumpgate):
    ALIAS = 'jg'
    INDEX = 3
    ARCHETYPE = 'nomad_gate'

    TARGET_SYSTEM_NAME = 'virt1'
    ROTATE_BY_TEMPLATE = True

    ASTEROID_ZONES = [
        OchoAsteroidZone3,
    ]
    AST_EXCLUSION_ZONE_SIZE = 8000

    NEBULA_ZONES = [
        OchNomadNebula
    ]
    EXCLUSION_PARAMS = EDGE_EXCLUSION_PARAMS2
    NEBULA_EXCLUSION_ZONE_SIZE = 3000
    NEBULA_EXCLUSION_EDGE_FRACTION = 0.4


class OchoNomadGateHelper(OchoMember, main_objects.NotAppearableObject):
    ALIAS = 'virt'
    INDEX = 1

    ASTEROID_ZONES = [
        OchoRubicAstZone1,
    ]
    AST_EXCLUSION_ZONE_SIZE = 2500


class OchoDysonRubicNomadGateRewards(OchoMember, mineable.DefaultDysonRubicRewardGroup):
    NAME = 'och_rubic'
    SOLAR = dyson_rubic.DysonRubic
    REWARD_ITEM = None
    ULTRA_REWARD_BASES = [
        OchoResearchAsteroids1,
    ]


class OchoDysonRubicFieldProps(mineable.DefaultField):
    BOX_SIZE = 1500
    DENSITY_MULTIPLER = 1
    DRIFT_X = 0.11
    DRIFT_Y = 0.025
    DRIFT_Z = 0.11
    ROTATE_X_MIN = 0
    ROTATE_X_MAX = 0
    ROTATE_Y_MIN = -180
    ROTATE_Y_MAX = 180
    ROTATE_Z_MIN = 0
    ROTATE_Z_MAX = 0


class OchoDysonRubicField(OchoMember, mineable.DysonRubicRewardField):
    FIELD_CLASS = OchoDysonRubicFieldProps
    REWARDS_GROUP_CLASS = OchoDysonRubicNomadGateRewards
    MEDIUM_REWARD_CHANCE = 0
    HIGH_REWARD_CHANCE = 0
    ULTRA_REWARD = True
    GLYPH = dyson_rubic.GLYPH3

    INDEX = 1
    ULTRA_BASE = OchoResearchAsteroids1

