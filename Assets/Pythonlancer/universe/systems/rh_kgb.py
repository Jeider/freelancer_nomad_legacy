from fx.space import Dust, JumpholeEffect
from fx.sound import Ambience

from universe.content.member import Member
from universe.content.system_object import LEFT, RIGHT
from universe.content import main_objects
from universe.content import zones
from universe import faction
from templates.nebula import rh_biz_nebula
from templates.nebula import rh_mnh_blue_nebula
from templates.nebula import exclusion

from text.strings import MultiString as MS


class KgbMember(Member):
    FACTION = faction.RheinlandPirate


class KgbRawText(KgbMember, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = rh_kgb
space_color = 0, 0, 0
space_farclip = 55000

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Music]
space = music_iw_space
danger = music_iw_danger
battle = music_iw_battle

[Dust]
spacedust = Dust

[Ambient]
color = 15, 15, 15

[Background]
nebulae = solar\\stars_mod\\rh_kgb_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[LightSource]
nickname = rh_kgb_system_light
pos = 0, 0, 0
color = 255, 150, 50
range = 200000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION

[LightSource]
nickname = rh_kgb_sirius_A_light
pos = -800000, 0, -30000
color = 120, 170, 255
range = 850000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION

'''


class KgbBrownNebula(KgbMember, zones.NebulaZone):
    INDEX = 1
    SPACEDUST = Dust.ATTRACT
    SPACEDUST_MAXPARTICLES = 40
    MUSIC = Ambience.NEBULA_DMATTER
    #CONTENT_TEMPLATE = sig8_nebula.Sig8BrownNebulaTemplate
    CONTENT_TEMPLATE = rh_biz_nebula.BizmarkBrownNebulaTemplate

    PROPERTY_FLAGS = 32768
    PROPERTY_FOG_COLOR = '100, 80, 10'


class KgbBlueNebula(KgbMember, zones.NebulaZone):
    INDEX = 2
    SPACEDUST = Dust.ATTRACT
    SPACEDUST_MAXPARTICLES = 40
    MUSIC = Ambience.NEBULA_DMATTER
    CONTENT_TEMPLATE = rh_mnh_blue_nebula.MunchenLargeBlueNebulaTemplate

    PROPERTY_FLAGS = 32768
    PROPERTY_FOG_COLOR = '100, 80, 10'


BROWN_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.EDGE_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '100, 80, 10',
    'fog_far': 5000,
}


BLUE_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.VORTEX_EXCLUSION,
    'shell_scalar': 1,
    'max_alpha': 0.3,
    'exclusion_tint': '255, 255, 255',
    'fog_far': 5000,
}


class KgbSun(KgbMember, main_objects.Sun):
    STAR = 'med_orange_sun'
    LOADOUT = 'small_yellow_sun_fx'
    ATMOSHPERE_RANGE = 12000


class KgbPlanet1(KgbMember, main_objects.Planet):
    ARCHETYPE = 'planet_gasicecld_10000'
    SPHERE_RADIUS = 10000
    PLANET_CIRCLE = False
    RU_NAME = MS('Планета Пиллау', 'Planet Pillau')


class KgbPlanet2(KgbMember, main_objects.Planet):
    INDEX = 2
    ARCHETYPE = 'planet_moonblu_2000'
    SPHERE_RADIUS = 2000
    RU_NAME = MS('Планета Нойхаузен', 'Planet Neuhausen')


class KgbPlanet3(KgbMember, main_objects.Planet):
    INDEX = 3
    ARCHETYPE = 'planet_earthsnwcld_4000'
    SPHERE_RADIUS = 4000
    PLANET_CIRCLE = False
    RU_NAME = MS('Планета Эрзгеб', 'Planet Erzgebirge')


class KgbPlanet4(KgbMember, main_objects.Planet):
    INDEX = 4
    ARCHETYPE = 'planet_rckdes_3000'
    SPHERE_RADIUS = 3000
    PLANET_CIRCLE = False
    RU_NAME = MS('Планета Битенен', 'Planet Bitenen')


class KgbPlanet5(KgbMember, main_objects.Planet):
    INDEX = 5
    ARCHETYPE = 'planet_desorcld_3000'
    SPHERE_RADIUS = 3000
    RU_NAME = MS('Планета Кранц', 'Planet Krantz')


class KgbSig8Jumphole(KgbMember, main_objects.Jumphole):
    INDEX = 1
    REL = RIGHT

    TARGET_SYSTEM_NAME = 'sig8'

    LOADOUT = JumpholeEffect.GREEN

    NEBULA_EXCLUSION_ZONE_SIZE = 2500
    EXCLUSION_PARAMS = BROWN_EXCLUSION_PARAMS
    NEBULA_ZONES = [KgbBrownNebula]


class KgbMunchenJumpgate(KgbMember, main_objects.JumpgateAlt):
    INDEX = 1
    REL = LEFT

    FACTION = faction.RheinlandMain

    TARGET_SYSTEM_NAME = 'rh_mnh'

    NEBULA_EXCLUSION_ZONE_SIZE = 2500
    EXCLUSION_PARAMS = BLUE_EXCLUSION_PARAMS
    NEBULA_ZONES = [KgbBlueNebula]
