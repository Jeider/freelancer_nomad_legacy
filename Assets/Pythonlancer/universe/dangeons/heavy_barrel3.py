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
from templates.dockable import megacannon

from templates.solar import dyson_rubic

from text.strings import MultiString as MS


class HbrMember(Member):
    FACTION = faction.Corsairs
    INTERIOR_BG1 = interior.INTERIOR_CO_OCHO_RIOS
    INTERIOR_BG2 = interior.INTERIOR_STARS
    WEAPON_FACTION = WEAPON_BW
    EQUIP_FACTION = EQUIP_BW
    AST_TYPE = 'ku_tgk'


class ArchStaticText(HbrMember, main_objects.RawText):
    SPACE_CONTENT = '''
[SystemInfo]
space_color = 0, 0, 0
local_faction = fc_n_grp
space_farclip = 50000

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Music]
space = music_tau_space
danger = music_tau_danger
battle = music_tau_battle

[Dust]
spacedust = Dust

[Ambient]
color = 5, 5, 5

[Background]
basic_stars = solar\\stars_mod\\new_generic.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
nebulae = solar\\stars_mod\\\br_wrw_nebula2.cmp


[LightSource]
nickname = br_hbr_system_light
pos = 0, 0, 0
color = 236, 241, 255
range = 150000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION


'''



class HbrSun(HbrMember, main_objects.Sun):
    STAR = 'Li02_Sun'
    LOADOUT = 'large_blue_sun_fx'


class HbrDeathZone(HbrMember, main_objects.DangeonMainDeathZone):
    pass


class HbrDemoBase(HbrMember, main_objects.Station):
    ALIAS = 'base'
    INDEX = 1
    BASE_INDEX = 1
    SPACE_OBJECT_TEMPLATE = megacannon.HeavyBarrelWithPlanet
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
