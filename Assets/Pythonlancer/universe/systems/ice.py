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
from templates.dockable import scient

from templates.solar import dyson_rubic

from text.strings import MultiString as MS


class IceMember(Member):
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


class IceTredelaneRing1(IceMember, main_objects.VirtualDepot):
    ALIAS = 'ring'
    INDEX = 1
    REL = LEFT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class IceTredelaneRing2(IceMember, main_objects.VirtualDepot):
    ALIAS = 'ring'
    INDEX = 2
    REL = RIGHT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class IceTredelaneRing3(IceMember, main_objects.VirtualDepot):
    ALIAS = 'ring'
    INDEX = 3
    REL = LEFT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class IceTredelaneRing4(IceMember, main_objects.VirtualDepot):
    ALIAS = 'ring'
    INDEX = 4
    REL = RIGHT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class IceTredelaneRing5(IceMember, main_objects.VirtualDepot):
    ALIAS = 'ring'
    INDEX = 5
    REL = RIGHT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class IceTredelaneRing6(IceMember, main_objects.VirtualDepot):
    ALIAS = 'ring'
    INDEX = 6
    REL = RIGHT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class IceTredelaneRing7(IceMember, main_objects.VirtualDepot):
    ALIAS = 'ring'
    INDEX = 7
    REL = RIGHT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class IceTredelaneRing12(IceMember, main_objects.VirtualDepot):
    ALIAS = 'ring'
    INDEX = 12
    REL = RIGHT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class IceTredelaneRing13(IceMember, main_objects.VirtualDepot):
    ALIAS = 'ring'
    INDEX = 13
    REL = RIGHT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class IceTredelaneRing8(IceMember, main_objects.VirtualDepot):
    ALIAS = 'ring'
    INDEX = 8
    REL = RIGHT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class IceTredelaneRing9(IceMember, main_objects.VirtualDepot):
    ALIAS = 'ring'
    INDEX = 9
    REL = RIGHT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class IceTredelaneRing10(IceMember, main_objects.VirtualDepot):
    ALIAS = 'ring'
    INDEX = 10
    REL = RIGHT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class IceTredelaneBuoy1(IceMember, main_objects.VirtualDepot):
    ALIAS = 'buoy'
    INDEX = 1
    REL = RIGHT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class IceTredelaneBuoy2(IceMember, main_objects.VirtualDepot):
    ALIAS = 'buoy'
    INDEX = 2
    REL = RIGHT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True



class IceTunnel1(IceMember, main_objects.AnomalyTradeConnection):
    OBJ_FROM = IceTredelaneRing1
    OBJ_TO = IceTredelaneRing2
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'A'
    TLR_DISTANCE = 10000
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class IceTunnel2(IceMember, main_objects.AnomalyTradeConnection):
    OBJ_FROM = IceTredelaneRing3
    OBJ_TO = IceTredelaneRing4
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'B'
    TLR_DISTANCE = 10000
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class IceTunnel3(IceMember, main_objects.AnomalyTradeConnection):
    OBJ_FROM = IceTredelaneRing5
    OBJ_TO = IceTredelaneRing6
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'C'
    TLR_DISTANCE = 10000
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class IceTunnel4(IceMember, main_objects.AnomalyTradeConnection):
    OBJ_FROM = IceTredelaneRing7
    OBJ_TO = IceTredelaneRing8
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'D'
    TLR_DISTANCE = 10000
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class IceTunnel5(IceMember, main_objects.AnomalyTradeConnection):
    OBJ_FROM = IceTredelaneRing9
    OBJ_TO = IceTredelaneRing10
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'E'
    TLR_DISTANCE = 7000
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class IceTunnel6(IceMember, main_objects.AnomalyTradeConnection):
    OBJ_FROM = IceTredelaneRing12
    OBJ_TO = IceTredelaneRing13
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'F'
    TLR_DISTANCE = 25000
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class IceTunnel7(IceMember, main_objects.AnomalyBuoyTradeConnection):
    OBJ_FROM = IceTredelaneBuoy1
    OBJ_TO = IceTredelaneBuoy2
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'G'
    TLR_DISTANCE = 5000
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True
    POLICE_PATROL = False






class BaseIceBase(main_objects.NotDockableObject):
    ALIAS = 'station'
    INDEX = 1
    BASE_INDEX = 1
    REL = LEFT
    SPACE_OBJECT_TEMPLATE = scient.Willard
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.BretoniaPirateDealers
    CALC_STORE = False
    HAVE_CHARACTERS = False

    AST_EXCLUSION_ZONE_SIZE = 4000
    ASTEROID_ZONES = [
        # CurAsteroidZone4,
    ]

    RU_NAME = MS('Иссл база', 'Research Base')


class IceBase1(IceMember, BaseIceBase):
    INDEX = 1


class IceBase2(IceMember, BaseIceBase):
    INDEX = 2


class IceBase3(IceMember, BaseIceBase):
    INDEX = 3


class IceBase4(IceMember, BaseIceBase):
    INDEX = 4
