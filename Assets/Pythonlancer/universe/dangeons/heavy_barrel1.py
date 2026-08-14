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


class HbrRtcMember(Member):
    FACTION = faction.Corsairs
    INTERIOR_BG1 = interior.INTERIOR_CO_OCHO_RIOS
    INTERIOR_BG2 = interior.INTERIOR_STARS
    WEAPON_FACTION = WEAPON_BW
    EQUIP_FACTION = EQUIP_BW
    AST_TYPE = 'ku_tgk'


class HbrRtcStaticContent(HbrRtcMember, main_objects.RawText):
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
color = 25, 25, 25

[Background]
basic_stars = solar\\stars_mod\\new_generic.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
nebulae = solar\\stars_mod\\ku_hns_nebula.cmp


[LightSource]
nickname = br_hbr_system_light
pos = 0, 0, 0
color = 236, 241, 255
range = 150000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION


'''


class HbrRtcDeathZone(HbrRtcMember, main_objects.DangeonRtcDeathZone):
    pass


class HbrRtcRealBase(HbrRtcMember, main_objects.Station):
    ALIAS = 'base'
    INDEX = 2
    BASE_INDEX = 1
    ARCHETYPE = 'depot'
    INTERIOR_CLASS = interior.OutpostInterior
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_KU
    DEFENCE_LEVEL = None
    SPACE_VOICE = None
    ALLOW_SPACE_COSTUME = False
    OFFICIAL_BARTENDER = False
    RU_NAME = MS('База Очо-Р+иос', "Ocho-Rios Base")
    CALC_STORE = False
    HAVE_CHARACTERS = False
    DEALERS = dealers.RheinlandPirateDealers
    LOCKED_DOCK = True
    KEY_COLLECT_FX = nn.FX_GOT_KEY_STATION

    EQUIP_SET = markets.EquipSet(
        Q.Gun('bw_corsairgun', eq_classes=markets.SECRET3),
    )
    INTERIOR_EXTRA_ROOMS = ['''
[Room]
nickname = Playback
file = Universe\\GENERATED_ROOMS\\playback_hbr_start.ini
    ''']
    INTERIOR_CUSTOM_START_ROOM = 'Playback'
    INTERIOR_EXTRA_ROOM_FILES = [
        interior.InteriorRoom(
            name='playback_hbr_start',
            subfolder=interior.ROOM_FOLDER_PLAYBACK,
            template='rh_ber_bar',
            context={
                'script_folder': 'generated',
                'script_file': 'm26_berlin',
            }
        )
    ]


class HbrRtcReferenceBase(HbrRtcMember, main_objects.DockableReference):
    ALIAS = 'base'
    INDEX = 1
    REFERENCED_DOCKABLE = HbrRtcRealBase
    ARCHETYPE = 'depot'
    RU_NAME = MS('База Очо-Р+иос', "Ocho-Rios Base")


class HbrRtcRoadPoint1(HbrRtcMember, main_objects.NavBuoy):
    ALIAS = 'road'
    INDEX = 1


class HbrRtcRoadPoint2(HbrRtcMember, main_objects.NavBuoy):
    ALIAS = 'road'
    INDEX = 2


class HbrRtcRoadPoint3(HbrRtcMember, main_objects.NavBuoy):
    ALIAS = 'road'
    INDEX = 3


class HbrRtcRoadPoint4(HbrRtcMember, main_objects.NavBuoy):
    ALIAS = 'road'
    INDEX = 4


class HbrRtcHelpway1(HbrRtcMember, main_objects.ParticleTradeConnection):
    OBJ_FROM = HbrRtcRoadPoint1
    OBJ_TO = HbrRtcRoadPoint2
    TRADELANE_LETTER = 'A'


class HbrRtcHelpway2(HbrRtcMember, main_objects.ParticleTradeConnection):
    OBJ_FROM = HbrRtcRoadPoint3
    OBJ_TO = HbrRtcRoadPoint4
    TRADELANE_LETTER = 'B'


class HbrRtcArrows(HbrRtcMember, main_objects.MultipleStaticObjects):
    ALIAS = 'arrow'
    START_INDEX = 1
    MAX_OBJECTS = 6


class HbrRtcHelp1(HbrRtcMember, main_objects.HelpPlayback):
    INDEX = 1
    SOUND = 'nn_hbr1_help1'


class HbrRtcHelp2(HbrRtcMember, main_objects.HelpPlayback):
    INDEX = 2
    SOUND = 'nn_hbr1_help2'


class HbrRtcHelp3(HbrRtcMember, main_objects.HelpPlayback):
    INDEX = 3
    SOUND = 'nn_hbr1_help3'


class HbrRtcHelp4(HbrRtcMember, main_objects.HelpPlayback):
    INDEX = 4
    SOUND = 'nn_hbr1_help4'


class HbrRtcEnterGate(HbrRtcMember, main_objects.AutoStaticObject):
    ALIAS = 'jg'
    INDEX = 1
    TEMPLATE_LOADOUT = False


class HbrRtcExitGate(HbrRtcMember, main_objects.JumpgateAlt):
    ALIAS = 'jg'
    INDEX = 2
    ROTATE_BY_TEMPLATE = True
    TARGET_SYSTEM_NAME = 'heavy_barrel2'
