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
from templates.nebula import rh_biz_nebula
from templates.nebula import rh_mnh_blue_nebula
from templates.nebula import exclusion
from templates.dockable import upsilon_gasinside
from templates.dockable import valensia


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


class OchoOmegaStorage(OchoMember, main_objects.SmugglerStoragePoint):
    INDEX = 1


class OchoMainAsteroidDefinition(asteroid_definition.TekagiAsteroidDefinition):
    BELT = True
    BILLBOARDS = True
    DYNAST = True
    LOOT = False  # TEMP
    BELT_HEIGHT = 8000


class OchoAsteroidZone1(OchoMember, zones.AsteroidZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = OchoMainAsteroidDefinition


class BaseOchoAst1Static(main_objects.AutoStaticObject):
    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        OchoAsteroidZone1,
    ]
    AST_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.ASTEROID,
        'spacedust_maxparticles': 200,
    }


class OchoStaticAst1(OchoMember, BaseOchoAst1Static):
    INDEX = 1


class OchoStaticAst2(OchoMember, BaseOchoAst1Static):
    INDEX = 2


class OchoStaticAst3(OchoMember, BaseOchoAst1Static):
    INDEX = 3


class OchoStaticAst4(OchoMember, BaseOchoAst1Static):
    INDEX = 4


class OchoMainAsteroidBase(OchoMember, main_objects.PirateAsteroid):
    ALIAS = 'astbase'
    INDEX = 1
    BASE_INDEX = 1
    ARCHETYPE = 'co_base_rock_large02'
    LOADOUT = 'co_base_rock_large01_pi_01'
    INTERIOR_CLASS = interior.CustomFullSplitRoomInterior
    DEFENCE_LEVEL = None
    RU_NAME = 'База Очо-Риос'
    SHIP_SET = markets.ShipSet('co_fighter')
    CALC_STORE = False

    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        OchoAsteroidZone1,
    ]
    AST_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.ASTEROID,
        'spacedust_maxparticles': 200,
    }
    EQUIP_SET = markets.EquipSet(
        Q.Gun('bw_corsairgun', eq_classes=markets.SECRET3),
    )


class OchoMetro1(OchoMember, main_objects.MetroMiningOne):
    INDEX = 1


class OchoMetro2(OchoMember, main_objects.MetroMiningTwo):
    INDEX = 2


class OchNomadCore(main_objects.Sattelite):
    ALIAS = 'no_core1'
    ARCHETYPE = 'domkavash_generator'
    OFFSET = [240, -315, 70]
    ROTATE = [0, -61, 0]


class OchoStatic5(OchoMember, main_objects.AutoStaticObject):
    INDEX = 5
    SATTELITES = [OchNomadCore]
