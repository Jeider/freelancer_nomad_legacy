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
from templates.nebula import li_cal_nebula
from templates.nebula import exclusion
from templates.dockable import arch

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
space = music_omicron_space
danger = music_omicron_danger
battle = music_omicron_battle

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



'''


EDGE_EXCLUSION_PARAMS2 = {
    'zone_shell': exclusion.VORTEX_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '150, 180, 160',
    'fog_far': 2500,
}

CROW_EXCLUSION_PARAMS2 = {
    'zone_shell': exclusion.VORTEX_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '150, 160, 180',
    'fog_far': 2500,
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


class ArchNebula2(ArchMember, ArchBaseEdgeNebula):
    INDEX = 2
    CONTENT_TEMPLATE = co_och_nebula.OchEdgeNebulaTemplate


class ArchNebula3(ArchMember, ArchBaseEdgeNebula):
    INDEX = 3
    CONTENT_TEMPLATE = co_och_nebula.OchEdgeNebulaTemplate


class ArchSun(ArchMember, main_objects.Sun):
    STAR = 'Ku07_Sun'
    # LOADOUT = 'small_blue_sun_fx'


class ArchDeathZone(ArchMember, main_objects.DangeonDeathZone):
    pass


class ArchDangeonTradelane4(ArchMember, main_objects.DangeonTradelane):
    INDEX = 7
    TARGET_INDEX = 8
    RU_NAME = MS('Далее', 'Next')
    RU_NAME_TARGET = MS('Пред', 'Prev')
    LOCKED_DOCK = True
    MAKE_KEYS = False
    ALLOW_UNLOCK_FIRST_GATE = True
    ALLOW_UNLOCK_SECOND_GATE = True


class ArchDangeonTradelane1(ArchMember, main_objects.DangeonTradelane):
    INDEX = 1
    TARGET_INDEX = 2
    RU_NAME = MS('Далее', 'Next')
    RU_NAME_TARGET = MS('Пред', 'Prev')
    LOCKED_DOCK = True
    ALLOW_UNLOCK_SECOND_GATE = False


class ArchDangeonTradelane2(ArchMember, main_objects.DangeonTradelane):
    INDEX = 3
    TARGET_INDEX = 4
    RU_NAME = MS('Далее', 'Next')
    RU_NAME_TARGET = MS('Пред', 'Prev')
    LOCKED_DOCK = True
    ALLOW_UNLOCK_SECOND_GATE = False


class ArchDangeonTradelane3(ArchMember, main_objects.DangeonTradelane):
    INDEX = 5
    TARGET_INDEX = 6
    RU_NAME = MS('Далее', 'Next')
    RU_NAME_TARGET = MS('Пред', 'Prev')
    LOCKED_DOCK = True
    ALLOW_UNLOCK_SECOND_GATE = False
    UNLOCK_ANOTHER_DANGEON_TLR = ArchDangeonTradelane4


class ArchRoadPoint1(ArchMember, main_objects.NavBuoy):
    ALIAS = 'road'
    INDEX = 1


class ArchRoadPoint2(ArchMember, main_objects.NavBuoy):
    ALIAS = 'road'
    INDEX = 2


class ArchRoadPoint3(ArchMember, main_objects.NavBuoy):
    ALIAS = 'road'
    INDEX = 3


class ArchRoadPoint4(ArchMember, main_objects.NavBuoy):
    ALIAS = 'road'
    INDEX = 4


class ArchRoadPoint5(ArchMember, main_objects.NavBuoy):
    ALIAS = 'road'
    INDEX = 5


class ArchRoadPoint6(ArchMember, main_objects.NavBuoy):
    ALIAS = 'road'
    INDEX = 6


class ArchRoadPoint7(ArchMember, main_objects.NavBuoy):
    ALIAS = 'road'
    INDEX = 7


class ArchRoadPoint8(ArchMember, main_objects.NavBuoy):
    ALIAS = 'road'
    INDEX = 8


class ArchRoadPoint9(ArchMember, main_objects.NavBuoy):
    ALIAS = 'road'
    INDEX = 9


class ArchRoadPoint10(ArchMember, main_objects.NavBuoy):
    ALIAS = 'road'
    INDEX = 10


class ArchRoadPoint11(ArchMember, main_objects.NavBuoy):
    ALIAS = 'road'
    INDEX = 11


class ArchRoadPoint12(ArchMember, main_objects.NavBuoy):
    ALIAS = 'road'
    INDEX = 12


class ArchHelpway1(ArchMember, main_objects.ParticleTradeConnection):
    OBJ_FROM = ArchRoadPoint1
    OBJ_TO = ArchRoadPoint2
    TRADELANE_LETTER = 'A'


class ArchHelpway2(ArchMember, main_objects.ParticleTradeConnection):
    OBJ_FROM = ArchRoadPoint3
    OBJ_TO = ArchRoadPoint4
    TRADELANE_LETTER = 'B'


class ArchHelpway3(ArchMember, main_objects.ParticleTradeConnection):
    OBJ_FROM = ArchRoadPoint5
    OBJ_TO = ArchRoadPoint6
    TRADELANE_LETTER = 'C'


class ArchHelpway4(ArchMember, main_objects.ParticleTradeConnection):
    OBJ_FROM = ArchRoadPoint7
    OBJ_TO = ArchRoadPoint8
    TRADELANE_LETTER = 'D'


class ArchHelpway5(ArchMember, main_objects.ParticleTradeConnection):
    OBJ_FROM = ArchRoadPoint9
    OBJ_TO = ArchRoadPoint10
    TRADELANE_LETTER = 'E'


class ArchHelpway6(ArchMember, main_objects.ParticleTradeConnection):
    OBJ_FROM = ArchRoadPoint11
    OBJ_TO = ArchRoadPoint12
    TRADELANE_LETTER = 'F'


class ArchArrows(ArchMember, main_objects.MultipleStaticObjects):
    ALIAS = 'arrow'
    MAX_OBJECTS = 10


class ArchHelp1(ArchMember, main_objects.HelpPlayback):
    INDEX = 1
    SOUND = 'dangeon_rules'


class ArchHelp2(ArchMember, main_objects.HelpPlayback):
    INDEX = 2
    SOUND = 'dyson_rubic'


class ArchHelp3(ArchMember, main_objects.HelpPlayback):
    INDEX = 3
    SOUND = 'dangeon_forward'


class ArchHelp4(ArchMember, main_objects.HelpPlayback):
    INDEX = 4
    SOUND = 'dangeon_final_exit'


class ArchHelp5(ArchMember, main_objects.HelpPlayback):
    INDEX = 5
    SOUND = 'arch_step2'


class ArchHelp6(ArchMember, main_objects.HelpPlayback):
    INDEX = 6
    SOUND = 'battleship_shield_lock'


class ArchDemoBase(ArchMember, main_objects.Station):
    ALIAS = 'base'
    INDEX = 1
    BASE_INDEX = 1
    SPACE_OBJECT_TEMPLATE = arch.SpaceArch
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


class ArchPowerGen1(ArchMember, main_objects.AutoStaticObject):
    ALIAS = 'gen'
    INDEX = 1
    TEMPLATE_LOADOUT = False

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


class ArchPowerGen2(ArchMember, main_objects.AutoStaticObject):
    ALIAS = 'gen'
    INDEX = 2
    TEMPLATE_LOADOUT = False

    ASTEROID_ZONES = [
        ArchRubicAstZone2,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500

    NEBULA_ZONES = [
        ArchNebula2
    ]
    EXCLUSION_PARAMS = EDGE_EXCLUSION_PARAMS2
    NEBULA_EXCLUSION_ZONE_SIZE = 3000
    NEBULA_EXCLUSION_EDGE_FRACTION = 0.4


class ArchPowerGen3(ArchMember, main_objects.AutoStaticObject):
    ALIAS = 'gen'
    INDEX = 3
    TEMPLATE_LOADOUT = False

    ASTEROID_ZONES = [
        ArchRubicAstZone3,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500

    NEBULA_ZONES = [
        ArchNebula3
    ]
    EXCLUSION_PARAMS = EDGE_EXCLUSION_PARAMS2
    NEBULA_EXCLUSION_ZONE_SIZE = 3000
    NEBULA_EXCLUSION_EDGE_FRACTION = 0.4


class ArchDysonRubicNomadGateRewards(ArchMember, mineable.DefaultDysonRubicRewardGroup):
    NAME = 'arch_rubic'
    SOLAR = dyson_rubic.DysonRubic
    REWARD_ITEM = None
    ULTRA_REWARD_BASES = [
        ArchDangeonTradelane1,
        ArchDangeonTradelane2,
        ArchDangeonTradelane3,
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

    ULTRA_BASE = ArchDangeonTradelane1


class ArchDysonRubicField2(ArchMember, mineable.DysonRubicRewardField):
    FIELD_CLASS = ArchDysonRubicFieldProps
    REWARDS_GROUP_CLASS = ArchDysonRubicNomadGateRewards
    MEDIUM_REWARD_CHANCE = 0
    HIGH_REWARD_CHANCE = 0
    ULTRA_REWARD = True
    GLYPH = dyson_rubic.GLYPH4

    INDEX = 2

    ULTRA_BASE = ArchDangeonTradelane2


class ArchDysonRubicField3(ArchMember, mineable.DysonRubicRewardField):
    FIELD_CLASS = ArchDysonRubicFieldProps
    REWARDS_GROUP_CLASS = ArchDysonRubicNomadGateRewards
    MEDIUM_REWARD_CHANCE = 0
    HIGH_REWARD_CHANCE = 0
    ULTRA_REWARD = True
    GLYPH = dyson_rubic.GLYPH6

    INDEX = 3

    ULTRA_BASE = ArchDangeonTradelane3
#
#
# class ArchEnc1(ArchMember, main_objects.CustomerEncounterZone):
#     INDEX = 1
#     FACTION = faction.Nomad
#     DENSITY = 10
#     REPOP_TIME = 10
#     RELIEF_TIME = 25
#     SHIPS = [
#         encounter.NpcShipEncounter(
#             'zone1a',
#             npc=NPC(
#                 faction=faction.Outcasts,
#                 ship=ship.NomadStiletto,
#                 level=NPC.D1,
#                 equip_map=EqMap(base_level=1),
#             ),
#             count=1
#         ),
#         encounter.NpcShipEncounter(
#             'zone1b',
#             npc=NPC(
#                 faction=faction.Outcasts,
#                 ship=ship.NomadDagger,
#                 level=NPC.D1,
#                 equip_map=EqMap(base_level=1),
#             ),
#             count=2
#         ),
#     ]


class ArchEnc2(ArchMember, main_objects.CustomerEncounterZone):
    INDEX = 2
    FACTION = faction.Nomad
    DENSITY = 10
    REPOP_TIME = 10
    RELIEF_TIME = 25
    SHIPS = [
        encounter.NpcShipEncounter(
            'zone2b',
            npc=NPC(
                faction=faction.Outcasts,
                ship=ship.NomadCenturion,
                level=NPC.D1,
                equip_map=EqMap(base_level=1),
            ),
            count=1
        ),
        encounter.NpcShipEncounter(
            'zone2c',
            npc=NPC(
                faction=faction.Outcasts,
                ship=ship.NomadLegionnaire,
                level=NPC.D1,
                equip_map=EqMap(base_level=1),
            ),
            count=2
        ),
    ]




class ArchEnc3(ArchMember, main_objects.CustomerEncounterZone):
    INDEX = 3
    FACTION = faction.Nomad
    DENSITY = 10
    REPOP_TIME = 10
    RELIEF_TIME = 25
    SHIPS = [
        encounter.NpcShipEncounter(
            'zone3a',
            npc=NPC(
                faction=faction.Outcasts,
                ship=ship.NomadTitan,
                level=NPC.D1,
                equip_map=EqMap(base_level=1),
            ),
            count=1
        ),
        encounter.NpcShipEncounter(
            'zone3b',
            npc=NPC(
                faction=faction.Outcasts,
                ship=ship.NomadCenturion,
                level=NPC.D1,
                equip_map=EqMap(base_level=1),
            ),
            count=1
        ),
        encounter.NpcShipEncounter(
            'zone3c',
            npc=NPC(
                faction=faction.Outcasts,
                ship=ship.NomadLegionnaire,
                level=NPC.D1,
                equip_map=EqMap(base_level=1),
            ),
            count=1
        ),
    ]




class ArchEnc4(ArchMember, main_objects.CustomerEncounterZone):
    INDEX = 4
    FACTION = faction.Nomad
    DENSITY = 10
    REPOP_TIME = 10
    RELIEF_TIME = 25
    SHIPS = [
        encounter.NpcShipEncounter(
            'zon42a',
            npc=NPC(
                faction=faction.Outcasts,
                ship=ship.NomadCrusader,
                level=NPC.D1,
                equip_map=EqMap(base_level=1),
            ),
            count=1
        ),
        encounter.NpcShipEncounter(
            'zone4b',
            npc=NPC(
                faction=faction.Outcasts,
                ship=ship.NomadCavalier,
                level=NPC.D1,
                equip_map=EqMap(base_level=1),
            ),
            count=1
        ),
        encounter.NpcShipEncounter(
            'zone4c',
            npc=NPC(
                faction=faction.Outcasts,
                ship=ship.NomadTitan,
                level=NPC.D1,
                equip_map=EqMap(base_level=1),
            ),
            count=1
        ),
    ]


class ArchEnterGate(ArchMember, main_objects.AutoStaticObject):
    ALIAS = 'jg'
    INDEX = 1
    TEMPLATE_LOADOUT = False


class ArchExitGate(ArchMember, main_objects.AutoStaticObject):
    ALIAS = 'jg'
    INDEX = 2
    TEMPLATE_LOADOUT = False


class ArchShield1(ArchMember, main_objects.AutoStaticObject):
    ALIAS = 'shield'
    INDEX = 1
    TEMPLATE_LOADOUT = False


class ArchBattleship1(ArchMember, main_objects.AutoStaticObject):
    ALIAS = 'bship'
    INDEX = 1
    TEMPLATE_LOADOUT = False
