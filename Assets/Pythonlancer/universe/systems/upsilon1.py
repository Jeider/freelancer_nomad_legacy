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
from templates.dockable import nomad_babylon


class Up1Member(Member):
    FACTION = faction.Corsairs
    INTERIOR_BG1 = interior.INTERIOR_BG_BARRIER_CLOUD
    WEAPON_FACTION = WEAPON_BW
    EQUIP_FACTION = EQUIP_BW
    AST_TYPE = 'ku_tgk'


class Up1StaticText(Up1Member, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = co_mad
space_color = 5, 5, 5
local_faction = co_grp
space_farclip = 80000
'''


class Upsilon1MadJumpgate(Up1Member, main_objects.Jumpgate):
    INDEX = 1
    REL = RIGHT
    TARGET_SYSTEM_NAME = 'co_mad'
    ROTATE_BY_TEMPLATE = True

