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
from templates.dockable import upsilon_gasinside
from templates.dockable import valensia


class ViennaMember(Member):
    FACTION = faction.RheinlandMain


class ViennaRawText(ViennaMember, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = rh_vien
space_color = 10, 10, 10
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
color = 55, 55, 55

[Background]
nebulae = solar\\stars_mod\\ku_hkd_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[LightSource]
nickname = or_hq_system_light
pos = 50000, 50000, 0
color = 135, 180, 255
range = 200000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION


'''


class ViennaThe(ViennaMember, main_objects.NotDockableObject):
    ALIAS = 'station'
    INDEX = 1
    REL = RIGHT

    SPACE_OBJECT_TEMPLATE = upsilon_gasinside.Vienna
