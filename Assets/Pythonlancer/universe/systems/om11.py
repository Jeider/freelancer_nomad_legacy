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


class Om11Member(Member):
    FACTION = faction.Corsairs
    INTERIOR_BG1 = interior.INTERIOR_OMEGA11
    INTERIOR_BG2 = interior.INTERIOR_STARS
    WEAPON_FACTION = WEAPON_BW
    EQUIP_FACTION = EQUIP_BW
    AST_TYPE = 'li_cal'


class Om11StaticText(Om11Member, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = om11
space_color = 10, 8, 0
local_faction = ku_grp
space_farclip = 60000

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Dust]
spacedust = Dust

[Music]
space = music_omega_space
danger = music_omega_danger
battle = music_omega_battle

[Ambient]
color = 25, 20, 5

[Background]
nebulae = solar\\stars_mod\\om11_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_om11_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
;property_flags = 512 ;lava - MILITARY
;property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = om11_system_light
pos = 0, 0, 0
color = 255, 150, 40
range = 80000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION
'''


class Om11Sun(Om11Member, main_objects.Sun):
    STAR = 'red_giant_sun'
    LOADOUT = 'large_red_sun_fx'
    ATMOSHPERE_RANGE = 20000
    DEATH_ZONE_SIZE = 12000
    DRAG_ZONE_SIZE = 17000


class Om11StaticTunnels1(Om11Member, main_objects.BackgroundTunnelOmega13):
    INDEX = 1
    WORKSPACE_TEMPLATE_NAME = 'om13ast'
    ROTATE = 0
    ARCHETYPE_CHANGE_TO = 'tau37'


class Om11StaticTunnels2(Om11Member, main_objects.BackgroundTunnelOmega13):
    INDEX = 2
    WORKSPACE_TEMPLATE_NAME = 'om13ast'
    ROTATE = 160
    ARCHETYPE_CHANGE_TO = 'tau37'


class Om11LargeAsteroidDefinition(asteroid_definition.Tau37LargeAsteroids):
    ABSTRACT = False
    NAME = 'om11_large_ast'
    EXCLUSION_SIZE_OVERRIDE = 2000


class Om11DynAsteroidDefinition(asteroid_definition.Tau37AsteroidDefinition):
    ABSTRACT = False
    NAME = 'om11_dyn_ast'
    DYNAST = True
    BELT = True
    BILLBOARDS = True
    LOOT = False  # TEMP
    EXCLUSION_SIZE_OVERRIDE = 3500


class Om11AsteroidLargeZone1(Om11Member, zones.AsteroidZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = Om11LargeAsteroidDefinition
    MUSIC = Ambience.AST_ROCK

    SPACEDUST = Dust.ASTEROID
    SPACEDUST_MAXPARTICLES = 200


class Om11AsteroidDynZone1(Om11Member, zones.AsteroidZone):
    ALIAS = 'astdyn'
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = Om11DynAsteroidDefinition


class Om11BigCorsairAsteroidBase(Om11Member, main_objects.PirateAsteroid):
    ALIAS = 'astbase'
    INDEX = 1
    BASE_INDEX = 1
    ARCHETYPE = 'tau37_base_large01'
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
        Om11AsteroidDynZone1,
        Om11AsteroidLargeZone1,
    ]
    EQUIP_SET = markets.EquipSet(
        Q.Gun('bw_corsairgun', eq_classes=markets.SECRET3),
    )
