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
from universe.content import mineable
from templates.solar import asteroid
from templates.nebula import co_och_nebula
from templates.nebula import exclusion
from templates.dockable import corsair_dreadnought

from templates.solar import dyson_rubic

from text.strings import MultiString as MS


class LairEnterMember(Member):
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
