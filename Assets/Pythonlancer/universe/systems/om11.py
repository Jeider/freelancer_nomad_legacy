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


class Om11StaticTunnels1(Om11Member, main_objects.BackgroundComplexObject):
    ALIAS = 'tunnel'
    INDEX = 1
    WORKSPACE_TEMPLATE_NAME = 'om13ast'
    ROTATE = -20


class Om11StaticTunnels2(Om11Member, main_objects.BackgroundComplexObject):
    ALIAS = 'tunnel'
    INDEX = 2
    WORKSPACE_TEMPLATE_NAME = 'om13ast'
    ROTATE = 160
