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
from templates.nebula import co_och_nebula
from templates.nebula import exclusion
from templates.dockable import corsair_dreadnought


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
space_farclip = 150000

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
    'exclusion_tint': '50, 200, 50',
    'fog_far': 5000,
}


WALKER_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.WALKER_EXCLUSION,
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


class OchoStaticAst7(OchoMember, BaseOchoAst2Static):
    INDEX = 7


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
    RU_NAME = 'База Кадиз'
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

    RU_NAME = 'Линкор Конкорд'


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
        OchBaseEdgeNebula
    ]
    EXCLUSION_PARAMS = EDGE_EXCLUSION_PARAMS
    NEBULA_EXCLUSION_ZONE_SIZE = 5000
