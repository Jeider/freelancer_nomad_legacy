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





class Sigma8Member(object):
    INDEX = 1
    FACTION = faction.RH_GRP
    ABSTRACT = False


class Sigma8StaticText(Sigma8Member, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = sig8
space_color = 2, 10, 5
local_faction = rh_grp
space_farclip = 60000

[archetype]
ship = rh_fighter
ship = rh_elite
ship = rh_freighter
ship = rh_cruiser
ship = rh_gunboat
ship = rh_battleship
ship = bw_fighter
ship = bw_elite
ship = bw_elite2
ship = pi_fighter
ship = pi_elite
ship = ge_transport
ship = ge_armored

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Music]
space = music_sigma_space
danger = music_sigma_danger
battle = music_sigma_battle

[Ambient]
color = 2, 10, 5

[Dust]
spacedust = Dust

[Background]
nebulae = solar\\stars_mod\\sig8_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_sig8_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
;property_flags = 512 ;lava - MILITARY
property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = sig8_System_Light
pos = 0, 0, 0
color = 194, 213, 254
range = 200000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION

[LightSource]
nickname = sig8_green_Light
pos = 100000, 0, 0
color = 24, 34, 25
range = 100000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION

'''


class Sig8Sun(Sigma8Member, main_objects.Sun):
    STAR = 'med_blue_sun'
    LOADOUT = 'med_blue_sun_fx'


class Sig8BerlinJumpgate(Sigma8Member, main_objects.Jumpgate):
    INDEX = 1
    REL = TOP


class Sig8BizmarkJumpgate(Sigma8Member, main_objects.Jumpgate):
    INDEX = 2
    REL = BOTTOM
