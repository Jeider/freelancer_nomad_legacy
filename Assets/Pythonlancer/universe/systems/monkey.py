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
from templates.solar import suprise
from universe import faction
from universe.content import mineable
from templates.solar import asteroid
from templates.nebula import co_och_nebula
from templates.nebula import exclusion
from templates.dockable import cloakgen

from templates.solar import dyson_rubic

from text.strings import MultiString as MS


class MonkeyMember(Member):
    FACTION = faction.Corsairs
    INTERIOR_BG1 = interior.INTERIOR_CO_OCHO_RIOS
    INTERIOR_BG2 = interior.INTERIOR_STARS
    WEAPON_FACTION = WEAPON_BW
    EQUIP_FACTION = EQUIP_BW
    AST_TYPE = 'ku_tgk'
#
#
# class Virt1NomadGate(Virt1Member, main_objects.Jumpgate):
#     ALIAS = 'jg'
#     INDEX = 1
#     ARCHETYPE = 'virt_gate'
#
#     TARGET_SYSTEM_NAME = 'co_och'
#     ROTATE_BY_TEMPLATE = True
#
#     JUMP_OUT_POINT = 'entry1'


class MonkeyDoor1(MonkeyMember, main_objects.VirtualDepot):
    ALIAS = 'door'
    INDEX = 1
    REL = LEFT
    RU_NAME = MS('Дверь', "Door")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class MonkeyDoor2(MonkeyMember, main_objects.VirtualDepot):
    ALIAS = 'door'
    INDEX = 2
    REL = RIGHT
    RU_NAME = MS('Дверь', "Door")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class MonkeyDoor3(MonkeyMember, main_objects.VirtualDepot):
    ALIAS = 'door'
    INDEX = 3
    REL = LEFT
    RU_NAME = MS('Дверь', "Door")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class MonkeyDoor4(MonkeyMember, main_objects.VirtualDepot):
    ALIAS = 'door'
    INDEX = 4
    REL = RIGHT
    RU_NAME = MS('Дверь', "Door")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class MonkeyTunnel1(MonkeyMember, main_objects.BrokenTradeConnection):
    OBJ_FROM = MonkeyDoor1
    OBJ_TO = MonkeyDoor2
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'A'
    TLR_DISTANCE = 2000
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class MonkeyTunnel2(MonkeyMember, main_objects.BrokenTradeConnection):
    OBJ_FROM = MonkeyDoor3
    OBJ_TO = MonkeyDoor4
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'B'
    TLR_DISTANCE = 2000
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class MunchenRoboSupriseRewards(MonkeyMember, mineable.DefaultSupriseRewardsGroup):
    NAME = 'monkey_top_ships'
    SOLAR = suprise.BretoniaMiscFighterEdge
    REWARD_ITEM = None
    ULTRA_REWARD_BASES = [
        # StutSolarPlant1,
        # StutSolarPlant2,
        # StutSolarPlant3,
        # StutSolarPlant4,
        # StutSolarPlant5,
    ]


class MonkeySolarSupriseField(mineable.DefaultField):
    BOX_SIZE = 200
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.7
    DRIFT_Y = 0.5
    DRIFT_Z = 0.7
    EMPTY_CHANCE = 0.1

#
# class MonkeyRoboSubpriseRewardField(MonkeyMember, mineable.SupriseRewardField):
#     ALIAS = 'suprise'
#     INDEX = 1
#     FIELD_CLASS = MonkeySolarSupriseField
#     REWARDS_GROUP_CLASS = MunchenRoboSupriseRewards
#     ULTRA_REWARD = False

#
# class StutSolarSupriseRewardField1(StutMember, StutBaseSolarSupriseRewardField):
#     INDEX = 1
#     # ULTRA_BASE = StutSolarPlant1




class MnkPortal(MonkeyMember, main_objects.NotDockableObject):
    ALIAS = 'station'
    INDEX = 1
    BASE_INDEX = 2
    REL = LEFT
    SPACE_OBJECT_TEMPLATE = cloakgen.Cloakgen
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.BretoniaPirateDealers
    CALC_STORE = False
    HAVE_CHARACTERS = False


    AST_EXCLUSION_ZONE_SIZE = 4000
    ASTEROID_ZONES = [
        # CurAsteroidZone4,
    ]

    RU_NAME = MS('Портал', 'Portal')