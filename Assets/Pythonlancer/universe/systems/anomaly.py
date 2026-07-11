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


class AnomalyMember(Member):
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


class AnomalyTredelaneRing1(AnomalyMember, main_objects.VirtualDepot):
    ALIAS = 'ring'
    INDEX = 1
    REL = LEFT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class AnomalyTredelaneRing2(AnomalyMember, main_objects.VirtualDepot):
    ALIAS = 'ring'
    INDEX = 2
    REL = RIGHT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class AnomalyTredelaneRing3(AnomalyMember, main_objects.VirtualDepot):
    ALIAS = 'ring'
    INDEX = 3
    REL = LEFT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class AnomalyTredelaneRing4(AnomalyMember, main_objects.VirtualDepot):
    ALIAS = 'ring'
    INDEX = 4
    REL = RIGHT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class AnomalyTredelaneRing5(AnomalyMember, main_objects.VirtualDepot):
    ALIAS = 'ring'
    INDEX = 5
    REL = RIGHT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class AnomalyTredelaneRing6(AnomalyMember, main_objects.VirtualDepot):
    ALIAS = 'ring'
    INDEX = 6
    REL = RIGHT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class AnomalyTredelaneRing7(AnomalyMember, main_objects.VirtualDepot):
    ALIAS = 'ring'
    INDEX = 7
    REL = RIGHT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class AnomalyTredelaneRing8(AnomalyMember, main_objects.VirtualDepot):
    ALIAS = 'ring'
    INDEX = 8
    REL = RIGHT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class AnomalyTredelaneRing9(AnomalyMember, main_objects.VirtualDepot):
    ALIAS = 'ring'
    INDEX = 9
    REL = RIGHT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class AnomalyTredelaneRing10(AnomalyMember, main_objects.VirtualDepot):
    ALIAS = 'ring'
    INDEX = 10
    REL = RIGHT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class AnomalyTredelaneRing11(AnomalyMember, main_objects.VirtualDepot):
    ALIAS = 'ring'
    INDEX = 11
    REL = RIGHT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class AnomalyTredelaneRing12(AnomalyMember, main_objects.VirtualDepot):
    ALIAS = 'ring'
    INDEX = 12
    REL = RIGHT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class AnomalyTredelaneRing13(AnomalyMember, main_objects.VirtualDepot):
    ALIAS = 'ring'
    INDEX = 13
    REL = RIGHT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class AnomalyTredelaneRing14(AnomalyMember, main_objects.VirtualDepot):
    ALIAS = 'ring'
    INDEX = 14
    REL = RIGHT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class AnomalyTunnel1(AnomalyMember, main_objects.AnomalyTradeConnection):
    OBJ_FROM = AnomalyTredelaneRing1
    OBJ_TO = AnomalyTredelaneRing2
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'A'
    TLR_DISTANCE = 15000
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class AnomalyTunnel2(AnomalyMember, main_objects.AnomalyTradeConnection):
    OBJ_FROM = AnomalyTredelaneRing3
    OBJ_TO = AnomalyTredelaneRing4
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'B'
    TLR_DISTANCE = 15000
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class AnomalyTunnel3(AnomalyMember, main_objects.AnomalyTradeConnection):
    OBJ_FROM = AnomalyTredelaneRing5
    OBJ_TO = AnomalyTredelaneRing6
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'C'
    TLR_DISTANCE = 20000
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class AnomalyTunnel4(AnomalyMember, main_objects.AnomalyTradeConnection):
    OBJ_FROM = AnomalyTredelaneRing7
    OBJ_TO = AnomalyTredelaneRing8
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'D'
    TLR_DISTANCE = 25000
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class AnomalyTunnel5(AnomalyMember, main_objects.AnomalyTradeConnection):
    OBJ_FROM = AnomalyTredelaneRing9
    OBJ_TO = AnomalyTredelaneRing10
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'E'
    TLR_DISTANCE = 25000
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class AnomalyTunnel6(AnomalyMember, main_objects.AnomalyTradeConnection):
    OBJ_FROM = AnomalyTredelaneRing11
    OBJ_TO = AnomalyTredelaneRing12
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'F'
    TLR_DISTANCE = 100000
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class AnomalyTunnel7(AnomalyMember, main_objects.AnomalyTradeConnection):
    OBJ_FROM = AnomalyTredelaneRing13
    OBJ_TO = AnomalyTredelaneRing14
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'G'
    TLR_DISTANCE = 150000
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True

