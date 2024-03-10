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
from templates.solar import asteroid as asteroid_solar
from templates.solar import debris_box

from templates.dockable import pirate
from templates.dockable import asteroid as asteroid_base
from templates.dockable import trade_storages
from templates.dockable import columbia_production
from templates.dockable import constanta
from templates.dockable import shipyards
from templates.dockable import alg
from templates.dockable import research
from templates.dockable import rheinland_military


class StutMember(object):d
    INDEX = 1
    ABSTRACT = False
    FACTION = faction.RH_GRP


class StutRawText(StutMember, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = rh_stut
space_color = 10, 10, 0
local_faction = rh_grp
space_farclip = 75000

[TexturePanels]
file = universe\heavens\shapes.ini

[Music]
space = music_rh_space
danger = music_rh_danger
battle = music_rh_battle

[Dust]
spacedust = Dust

[Ambient]
color = 20, 10, 5

[Background]
nebulae = solar\stars_mod\rh_stut_nebula.cmp
complex_stars = solar\stars_mod\new_generic.cmp
basic_stars = solar\stars_mod\new_generic.cmp

[zone]
nickname = zone_rh_stut_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
property_flags = 512 ;lava - MILITARY
;property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = rh_stut_System_Light
pos = 0, 0, 0
color = 252, 153, 53
; color = 255, 255, 255
range = 120000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION'''


class StutSun(StutMember, main_objects.Sun):
    STAR = 'med_orange_sun'
    LOADOUT = 'large_yellow_sun_fx'
    ATMOSHPERE_RANGE = 12000
