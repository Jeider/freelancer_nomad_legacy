from fx.space import Dust, JumpholeEffect
from fx.sound import Ambience

from world.names import *
from universe import markets

from universe.content.member import Member
from universe.content.system_object import LEFT, RIGHT, TOP
from universe.content import main_objects
from universe.content import zones
from universe.content import interior
from universe.content import dealers
from universe import faction
from templates.nebula import rh_biz_nebula
from templates.nebula import rh_mnh_blue_nebula
from templates.nebula import exclusion
from templates.dockable import upsilon_gasinside
from templates.dockable import valensia

from story.ingame.names import PRINCE_OF_WALES, MSG_PRINCE_OF_WALES


class Tau44Member(Member):
    FACTION = faction.ASF


class Tau44PrinceWales(Tau44Member, main_objects.BretoniaBattleship):
    ALIAS = 'wales_arrive'
    INDEX = 1
    BASE_INDEX = 99
    REL = TOP
    INTERIOR_CLASS = interior.BattleshipInterior
    DEALERS = dealers.BretoniaMilitaryDealers
    STORY = True
    CALC_STORE = False
    FACTION = faction.BretoniaMain
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_BR
    WEAPON_FACTION = WEAPON_BR
    EQUIP_FACTION = EQUIP_BR
    # ASF set?
    SHIP_SET = markets.ShipSet('br_elite')
    OFFER_MISSIONS = False
    RU_NAME = PRINCE_OF_WALES
    MSG_PREFIX = MSG_PRINCE_OF_WALES
