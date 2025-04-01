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
from templates.dockable import terraforming
from templates.dockable import valensia


class OrdHQMember(Member):
    FACTION = faction.LibertyMain


class OrdHQRawText(OrdHQMember, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = or_hq
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
pos = 0, 0, 0
color = 135, 180, 255
range = 200000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION


'''

class OrdHQSun(OrdHQMember, main_objects.Sun):
    STAR = 'med_white_sun'
    LOADOUT = 'med_blue_sun_fx'
    ATMOSHPERE_RANGE = 12000


class OrdHQPlanet1(OrdHQMember, main_objects.Planet):
    ARCHETYPE = 'planet_earthgrnice_9000'
    SPHERE_RADIUS = 9000
    PLANET_CIRCLE = False
    SPIN = 0


class OrdHQTerraform1(OrdHQMember, main_objects.NotDockableObject):
    ALIAS = 'terra'
    INDEX = 1
    REL = RIGHT

    SPACE_OBJECT_TEMPLATE = terraforming.TerraformingTwo


class OrdHQTerraform2(OrdHQMember, main_objects.NotDockableObject):
    ALIAS = 'terra'
    INDEX = 2
    REL = RIGHT

    SPACE_OBJECT_TEMPLATE = terraforming.TerraformingTwo


class OrdHQTerraform3(OrdHQMember, main_objects.NotDockableObject):
    ALIAS = 'terra'
    INDEX = 3
    REL = RIGHT

    SPACE_OBJECT_TEMPLATE = terraforming.TerraformingTwo


class OrdHQTerraformFX1(OrdHQMember, main_objects.NotDockableObject):
    ALIAS = 'terrafx'
    INDEX = 1
    REL = RIGHT

    ARCHETYPE = 'hidden_connect'
    LOADOUT = 'terraform_effect2_terra'


class OrdHQTerraformFX2(OrdHQMember, main_objects.NotDockableObject):
    ALIAS = 'terrafx'
    INDEX = 2
    REL = RIGHT

    ARCHETYPE = 'hidden_connect'
    LOADOUT = 'terraform_effect2_terra'


class OrdHQTerraformFX3(OrdHQMember, main_objects.NotDockableObject):
    ALIAS = 'terrafx'
    INDEX = 3
    REL = RIGHT

    ARCHETYPE = 'hidden_connect'
    LOADOUT = 'terraform_effect2_terra'


class OrdHQLargeStation(OrdHQMember, main_objects.NotDockableObject):
    ALIAS = 'station'
    INDEX = 1
    REL = RIGHT

    SPACE_OBJECT_TEMPLATE = valensia.ValensiaOutsideTwo

