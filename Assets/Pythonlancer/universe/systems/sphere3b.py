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


class Sphere3BMember(Member):
    FACTION = faction.Corsairs
    INTERIOR_BG1 = interior.INTERIOR_CO_OCHO_RIOS
    INTERIOR_BG2 = interior.INTERIOR_STARS
    WEAPON_FACTION = WEAPON_BW
    EQUIP_FACTION = EQUIP_BW
    AST_TYPE = 'ku_tgk'


# class Virt1NomadGate(Virt1Member, main_objects.Jumpgate):
#     ALIAS = 'jg'
#     INDEX = 1
#     ARCHETYPE = 'virt_gate'
#
#     TARGET_SYSTEM_NAME = 'co_och'
#     ROTATE_BY_TEMPLATE = True
#
#     JUMP_OUT_POINT = 'entry1'


class Sphere3BTredelaneRing1(Sphere3BMember, main_objects.VirtualDepot):
    ALIAS = 'ring'
    INDEX = 1
    REL = LEFT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True


class Sphere3BTredelaneRing2(Sphere3BMember, main_objects.VirtualDepot):
    ALIAS = 'ring'
    INDEX = 2
    REL = RIGHT
    RU_NAME = MS('Точка', "Point")
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True

class Sphere3BTunnel1(Sphere3BMember, main_objects.DysonAnomalyTradeConnection):
    OBJ_FROM = Sphere3BTredelaneRing1
    OBJ_TO = Sphere3BTredelaneRing2
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'A'
    TLR_DISTANCE = 10000
    REL_DRIFT = 0
    REL_APPEND = 0
    MIN_REL_IGNORE = True
