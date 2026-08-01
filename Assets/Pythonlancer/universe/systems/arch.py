from fx.space import Dust, JumpholeEffect
from fx.sound import Ambience
from universe.audio.space_voice import SpaceVoice, SpaceCostume

from managers.tools import query as Q
from world.names import *
from universe.content import meta
import fx.neuralnet as nn

from world.npc import NPC, EqMap
from world import ship

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
from universe.content import encounter
from templates.solar import asteroid
from templates.nebula import co_och_nebula
from templates.nebula import exclusion
from templates.dockable import corsair_dreadnought

from templates.solar import dyson_rubic

from text.strings import MultiString as MS


class ArchMember(Member):
    FACTION = faction.Corsairs
    INTERIOR_BG1 = interior.INTERIOR_CO_OCHO_RIOS
    INTERIOR_BG2 = interior.INTERIOR_STARS
    WEAPON_FACTION = WEAPON_BW
    EQUIP_FACTION = EQUIP_BW
    AST_TYPE = 'ku_tgk'


class ArchStaticText(ArchMember, main_objects.RawText):
    SPACE_CONTENT = '''
[SystemInfo]
space_color = 0, 0, 0
local_faction = fc_n_grp

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Music]
space = music_beta_exploration_08
danger = music_beta_danger_08
battle = music_beta_battle_08

[Dust]
spacedust = Dust

[Ambient]
color = 30, 30, 30

[Background]
basic_stars = solar\\stars_mod\\new_generic.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
nebulae = solar\\stars_mod\\arch_nebula.cmp

[LightSource]
nickname = arch_system_light
pos = 0, 0, 0
color = 225, 255, 243
range = 70000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION


[Object]
nickname = arch_02
ids_name = 196765
pos = 47988, 1000, 20578
rotate = 0, -71, 2
archetype = space_arch
ids_info = 65879
base = Ku07_02_Base
dock_with = Ku07_02_Base
visit = 0
behavior = NOTHING

[Object]
nickname = arch_02_Asteroid
ids_name = 196765
pos = 47988, 1000, 20578
rotate = 0, -71, 2
archetype = space_arch_asteroid2
ids_info = 65879
visit = 128
behavior = NOTHING
parent = arch_02

[Object]
nickname = arch_space_arch_chunk1a_1
pos = 46645, 0, 11560
rotate = 0, -70, 0
archetype = space_arch_chunk1a

[Object]
nickname = arch_space_arch_chunk1b_1
pos = 40552, 1200, 6758
rotate = 0, -60, 0
archetype = space_arch_chunk1b

[Object]
nickname = arch_space_arch_chunk2a_1
pos = 38163, 1000, 2818
rotate = 20, -20, 0
archetype = space_arch_chunk2a

[Object]
nickname = arch_space_arch_chunk2b_1
pos = 43067, -300, 15756
rotate = -110, -49, 102
archetype = space_arch_chunk2b

[Object]
nickname = arch_space_arch_chunk3a_1
pos = 49265, 1000, 5147
rotate = 30, 60, 0
archetype = space_arch_chunk3a

[Object]
nickname = arch_space_arch_chunk3b_1
pos = 45084, 1000, 2233
rotate = 0, -20, 0
archetype = space_arch_chunk3b

[Object]
nickname = arch_space_arch_chunk3c_1
pos = 45852, 1000, 9329
archetype = space_arch_chunk3c

[Object]
nickname = arch_space_arch_chunk3d_1
pos = 46382, 1000, 7292
rotate = 0, -20, 0
archetype = space_arch_chunk3d

[Object]
nickname = arch_space_arch_chunk3e_1
pos = 40401, 1000, 12303
rotate = 115, -20, 0
archetype = space_arch_chunk3e
'''


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


class ArchBaseEdgeNebula(zones.NebulaZone):
    MUSIC = Ambience.ASTEROID_NOMAD
    INTERFERENCE = 0.5

    SPACEDUST = Dust.ATTRACT_GREEN
    SPACEDUST_MAXPARTICLES = 100

    PROPERTY_FLAGS = 32768
    PROPERTY_FOG_COLOR = '150, 100, 20'


class ArchNebula1(ArchMember, ArchBaseEdgeNebula):
    INDEX = 1
    CONTENT_TEMPLATE = co_och_nebula.OchEdgeNebulaTemplate


class ArchSun(ArchMember, main_objects.Sun):
    STAR = 'Ku07_Sun'
    # LOADOUT = 'small_blue_sun_fx'


class ArchDeathZone(ArchMember, main_objects.DangeonDeathZone):
    pass


class ArchDangeonTradelane1(ArchMember, main_objects.DangeonTradelane):
    INDEX = 1
    TARGET_INDEX = 2
    RU_NAME = MS('Далее', 'Next')
    RU_NAME_TARGET = MS('Пред', 'Prev')


class ArchDangeonTradelane2(ArchMember, main_objects.DangeonTradelane):
    INDEX = 3
    TARGET_INDEX = 4
    RU_NAME = MS('Далее', 'Next')
    RU_NAME_TARGET = MS('Пред', 'Prev')


class ArchDangeonTradelane3(ArchMember, main_objects.DangeonTradelane):
    INDEX = 5
    TARGET_INDEX = 6
    RU_NAME = MS('Далее', 'Next')
    RU_NAME_TARGET = MS('Пред', 'Prev')


class ArchRoadPoint1(ArchMember, main_objects.VirtualDepot):
    ALIAS = 'road'
    INDEX = 1
    REL = LEFT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class ArchRoadPoint2(ArchMember, main_objects.VirtualDepot):
    ALIAS = 'road'
    INDEX = 2
    REL = RIGHT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class ArchRoadPoint3(ArchMember, main_objects.VirtualDepot):
    ALIAS = 'road'
    INDEX = 3
    REL = LEFT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class ArchRoadPoint4(ArchMember, main_objects.VirtualDepot):
    ALIAS = 'road'
    INDEX = 4
    REL = RIGHT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class ArchHelpway1(ArchMember, main_objects.ParticleTradeConnection):
    OBJ_FROM = ArchRoadPoint1
    OBJ_TO = ArchRoadPoint2
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'A'
    TLR_DISTANCE = 800
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class ArchHelpway2(ArchMember, main_objects.ParticleTradeConnection):
    OBJ_FROM = ArchRoadPoint3
    OBJ_TO = ArchRoadPoint4
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'B'
    TLR_DISTANCE = 800
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class ArchArrows(ArchMember, main_objects.MultipleStaticObjects):
    ALIAS = 'arrow'
    MAX_OBJECTS = 10


class ArchDemoBase(ArchMember, main_objects.Station):
    ALIAS = 'temp'
    INDEX = 1
    BASE_INDEX = 1
    ARCHETYPE = 'co_base_rock_large02'
    LOADOUT = 'co_base_rock_large01_pi_01'
    INTERIOR_CLASS = interior.CustomFullSplitRoomInterior
    DEFENCE_LEVEL = None
    RANDOM_ROBOT = True
    OFFICIAL_BARTENDER = False
    RU_NAME = MS('База Очо-Р+иос', "Ocho-Rios Base")
    SHIP_SET = markets.ShipSet('co_fighter')
    CALC_STORE = False
    HAVE_CHARACTERS = False
    DEALERS = dealers.RheinlandPirateDealers
    LOCKED_DOCK = True
    KEY_COLLECT_FX = nn.FX_GOT_KEY_STATION

    EQUIP_SET = markets.EquipSet(
        Q.Gun('bw_corsairgun', eq_classes=markets.SECRET3),
    )

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


class ArchRubicNomadAst(asteroid_definition.AsteroidDefinition):
    FIELD = True
    CUBE = True
    FIELD_TEMPLATE = TRN_FIELD_TEMPLATE
    CUBE_TEMPLATE = TRN_CUBE_TEMPLATE


class ArchRubicAstZone1(ArchMember, zones.AsteroidZone):
    ALIAS = 'rubic'
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = ArchRubicNomadAst
    SPACEDUST = Dust.ATTRACT_PURPLE
    SPACEDUST_MAXPARTICLES = 200
    DRAG_MODIFIER = 1.3
    INTERFERENCE = 0.5


class ArchRubicAstZone2(ArchMember, zones.AsteroidZone):
    ALIAS = 'rubic'
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = ArchRubicNomadAst
    SPACEDUST = Dust.ATTRACT_PURPLE
    SPACEDUST_MAXPARTICLES = 200
    DRAG_MODIFIER = 1.3
    INTERFERENCE = 0.5


class ArchRubicAstZone3(ArchMember, zones.AsteroidZone):
    ALIAS = 'rubic'
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = ArchRubicNomadAst
    SPACEDUST = Dust.ATTRACT_PURPLE
    SPACEDUST_MAXPARTICLES = 200
    DRAG_MODIFIER = 1.3
    INTERFERENCE = 0.5


class ArchNomadGateHelper1(ArchMember, main_objects.NotAppearableObject):
    ALIAS = 'virt'
    INDEX = 1

    ASTEROID_ZONES = [
        ArchRubicAstZone1,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500

    NEBULA_ZONES = [
        ArchNebula1
    ]
    EXCLUSION_PARAMS = EDGE_EXCLUSION_PARAMS2
    NEBULA_EXCLUSION_ZONE_SIZE = 3000
    NEBULA_EXCLUSION_EDGE_FRACTION = 0.4


class ArchNomadGateHelper2(ArchMember, main_objects.NotAppearableObject):
    ALIAS = 'virt'
    INDEX = 2

    ASTEROID_ZONES = [
        ArchRubicAstZone2,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500


class ArchNomadGateHelper3(ArchMember, main_objects.NotAppearableObject):
    ALIAS = 'virt'
    INDEX = 3

    ASTEROID_ZONES = [
        ArchRubicAstZone3,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500


class ArchDysonRubicNomadGateRewards(ArchMember, mineable.DefaultDysonRubicRewardGroup):
    NAME = 'arch_rubic'
    SOLAR = dyson_rubic.DysonRubic
    REWARD_ITEM = None
    ULTRA_REWARD_BASES = [
        ArchDemoBase,
    ]


class ArchDysonRubicFieldProps(mineable.DefaultField):
    BOX_SIZE = 2000
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


class ArchDysonRubicField1(ArchMember, mineable.DysonRubicRewardField):
    FIELD_CLASS = ArchDysonRubicFieldProps
    REWARDS_GROUP_CLASS = ArchDysonRubicNomadGateRewards
    MEDIUM_REWARD_CHANCE = 0
    HIGH_REWARD_CHANCE = 0
    ULTRA_REWARD = True
    GLYPH = dyson_rubic.GLYPH2

    INDEX = 1

    ULTRA_BASE = ArchDemoBase


class ArchDysonRubicField2(ArchMember, mineable.DysonRubicRewardField):
    FIELD_CLASS = ArchDysonRubicFieldProps
    REWARDS_GROUP_CLASS = ArchDysonRubicNomadGateRewards
    MEDIUM_REWARD_CHANCE = 0
    HIGH_REWARD_CHANCE = 0
    ULTRA_REWARD = True
    GLYPH = dyson_rubic.GLYPH4

    INDEX = 2

    ULTRA_BASE = ArchDemoBase


class ArchDysonRubicField3(ArchMember, mineable.DysonRubicRewardField):
    FIELD_CLASS = ArchDysonRubicFieldProps
    REWARDS_GROUP_CLASS = ArchDysonRubicNomadGateRewards
    MEDIUM_REWARD_CHANCE = 0
    HIGH_REWARD_CHANCE = 0
    ULTRA_REWARD = True
    GLYPH = dyson_rubic.GLYPH6

    INDEX = 3

    ULTRA_BASE = ArchDemoBase


class ArchEnc1(ArchMember, main_objects.CustomerEncounterZone):
    INDEX = 1
    SHIPS = [
        encounter.NpcShipEncounter(
            'main_outcast',
            npc=NPC(
                faction=faction.Outcasts,
                ship=ship.Dagger,
                level=NPC.D2,
                equip_map=EqMap(base_level=2),
            ),
            count=1
        ),
        encounter.NpcShipEncounter(
            'second_outcast',
            npc=NPC(
                faction=faction.Outcasts,
                ship=ship.Sabre,
                level=NPC.D5,
                equip_map=EqMap(base_level=5),
            ),
            count=3
        )
    ]
