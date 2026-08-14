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


class HbrMainMember(Member):
    FACTION = faction.Corsairs
    INTERIOR_BG1 = interior.INTERIOR_CO_OCHO_RIOS
    INTERIOR_BG2 = interior.INTERIOR_STARS
    WEAPON_FACTION = WEAPON_BW
    EQUIP_FACTION = EQUIP_BW
    AST_TYPE = 'ku_tgk'


class ArchStaticText(HbrMainMember, main_objects.RawText):
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
nebulae = solar\\stars_mod\\ku_hkd_nebula.cmp


[LightSource]
nickname = br_hbr_system_light
pos = 0, 0, 0
color = 236, 241, 255
range = 150000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION


'''



class HbrSun(HbrMainMember, main_objects.Sun):
    STAR = 'Li02_Sun'
    LOADOUT = 'large_blue_sun_fx'


class HbrDeathZone(HbrMainMember, main_objects.DangeonMainDeathZone):
    pass


class HbrMainHelp1(HbrMainMember, main_objects.HelpPlayback):
    INDEX = 1
    SOUND = 'nn_hbr2_help1'


class HbrMainHelp2(HbrMainMember, main_objects.HelpPlayback):
    INDEX = 2
    SOUND = 'nn_hbr2_help2'


class HbrMainHelp3(HbrMainMember, main_objects.HelpPlayback):
    INDEX = 3
    SOUND = 'nn_hbr2_help3'


class HbrMainHelp4(HbrMainMember, main_objects.HelpPlayback):
    INDEX = 4
    SOUND = 'nn_hbr2_help4'


class HbrMainMegaCannon(HbrMainMember, main_objects.Station):
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

    FACTION = faction.ASF
    # FORCE_SPACE_FACTION = faction.ASFMegaCannonExit

    EQUIP_SET = markets.EquipSet(
        Q.Gun('bw_corsairgun', eq_classes=markets.SECRET3),
    )


class HbrMainEnterGate(HbrMainMember, main_objects.JumpgateAlt):
    ALIAS = 'jg'
    INDEX = 2
    ROTATE_BY_TEMPLATE = True
    TARGET_SYSTEM_NAME = 'heavy_barrel1'


class HbrMainGunDefence(HbrMainMember, main_objects.CustomerEncounterZone):
    INDEX = 9
    FACTION = faction.ASF
    DENSITY = 10
    REPOP_TIME = 15
    RELIEF_TIME = 35
    ENCOUNTERS = [
        encounter.EncounterEntry(
            ships=[
                encounter.NpcShipEncounter(
                    'asf_defence',
                    npc=NPC(
                        faction=faction.LibertyMain,
                        ship=ship.DefenderJuni,
                        level=NPC.D5,
                        equip_map=EqMap(base_level=5),
                    ),
                    count=2
                ),
                encounter.NpcShipEncounter(
                    'asf_defence2',
                    npc=NPC(
                        faction=faction.LibertyMain,
                        ship=ship.Patriot,
                        level=NPC.D5,
                        equip_map=EqMap(base_level=5),
                    ),
                    count=2
                ),
            ],
            chance=1,
        )
    ]


class HbrMainGunNomadFighter(HbrMainMember, main_objects.CustomerEncounterZone):
    INDEX = 8
    FACTION = faction.Nomad
    DENSITY = 10
    REPOP_TIME = 10
    RELIEF_TIME = 10
    ENCOUNTERS = [
        encounter.EncounterEntry(
            ships=[
                encounter.NpcShipEncounter(
                    'nomad_gun_assault',
                    static_npc_shiparch='demo_no_fighter',
                    count=4
                )
            ],
            chance=0.75,
        ),
        encounter.EncounterEntry(
            ships=[
                encounter.NpcShipEncounter(
                    'nomad_gun_assault_leader',
                    static_npc_shiparch='demo_no_elite',
                    count=1
                ),
                encounter.NpcShipEncounter(
                    'nomad_gun_assault_support',
                    static_npc_shiparch='demo_no_fighter',
                    count=4
                )
            ],
            chance=0.25,
        ),
    ]


class HbrNomadFighterBaseUnlockers(HbrMainMember, main_objects.CustomerEncounterZone):
    INDEX = 7
    FACTION = faction.NomadMegaCannon
    DENSITY = 10
    REPOP_TIME = 10
    RELIEF_TIME = 10
    ENCOUNTERS = [
        encounter.EncounterEntry(
            ships=[
                encounter.NpcShipEncounter(
                    'nomad_gun_assault_alt',
                    static_npc_shiparch='demo_no_fighter',
                    count=4
                )
            ],
            chance=0.75,
        ),
    ]


class HbrMainDangeonTradelane4(HbrMainMember, main_objects.DangeonTradelane):
    INDEX = 7
    TARGET_INDEX = 8
    RU_NAME = MS('Далее', 'Next')
    RU_NAME_TARGET = MS('Пред', 'Prev')
    LOCKED_DOCK = True
    MAKE_KEYS = True
    ALLOW_UNLOCK_FIRST_GATE = True
    ALLOW_UNLOCK_SECOND_GATE = False
    KEY_COLLECT_FX = 'fx_snd_nn_hbr_planet_loot'


class HbrMainArrows(HbrMainMember, main_objects.MultipleStaticObjects):
    ALIAS = 'arrow'
    START_INDEX = 7
    MAX_OBJECTS = 15


class HbrMainPlanetExplodeReward(HbrMainMember, main_objects.AutoStaticObject):
    ALIAS = 'reward'
    INDEX = 1
    TEMPLATE_LOADOUT = False
    AUTO_KEY_LOADOUT_FOR_BASE = HbrMainDangeonTradelane4






class HbrMainRewardBase(HbrMainMember, main_objects.Station):
    ALIAS = 'base'
    INDEX = 3
    BASE_INDEX = 2
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
file = Universe\\GENERATED_ROOMS\\playback_hbr_finish.ini
    ''']
    INTERIOR_CUSTOM_START_ROOM = 'Playback'
    INTERIOR_EXTRA_ROOM_FILES = [
        interior.InteriorRoom(
            name='playback_hbr_finish',
            subfolder=interior.ROOM_FOLDER_PLAYBACK,
            template='li_col_bar',
            context={
                'script_folder': 'generated',
                'script_file': 'm24_reward',
            }
        )
    ]


class HbrMainReferenceBase(HbrMainMember, main_objects.DockableReference):
    ALIAS = 'base'
    INDEX = 2
    REFERENCED_DOCKABLE = HbrMainRewardBase
    ARCHETYPE = 'depot'
    RU_NAME = MS('База Очо-Р+иос', "Ocho-Rios Base")

    FORCE_SPACE_FACTION = faction.ASFMegaCannonExit


class HbrMainRoadPoint1(HbrMainMember, main_objects.NavBuoy):
    ALIAS = 'road'
    INDEX = 13


class HbrMainRoadPoint2(HbrMainMember, main_objects.NavBuoy):
    ALIAS = 'road'
    INDEX = 14


class HbrMainRoadPoint3(HbrMainMember, main_objects.NavBuoy):
    ALIAS = 'road'
    INDEX = 15


class HbrMainRoadPoint4(HbrMainMember, main_objects.NavBuoy):
    ALIAS = 'road'
    INDEX = 16


class HbrMainHelpway1(HbrMainMember, main_objects.ParticleTradeConnection):
    OBJ_FROM = HbrMainRoadPoint1
    OBJ_TO = HbrMainRoadPoint2
    TRADELANE_LETTER = 'X'


class HbrMainHelpway2(HbrMainMember, main_objects.ParticleTradeConnection):
    OBJ_FROM = HbrMainRoadPoint3
    OBJ_TO = HbrMainRoadPoint4
    TRADELANE_LETTER = 'Y'