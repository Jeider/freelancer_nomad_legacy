from fx.space import Dust, JumpholeEffect
from fx.sound import Ambience

from world.names import *
from universe import markets

from universe.content.member import Member
from universe.content.system_object import LEFT, RIGHT
from universe.content import main_objects
from universe.content import zones
from universe.content import interior
from universe.content import dealers
from universe import faction
from templates.nebula import rh_biz_nebula
from templates.nebula import rh_mnh_blue_nebula
from templates.nebula import exclusion
from templates.dockable import terraforming
from templates.dockable import valensia

from story.ingame.names import MUSASHI


class OrdHQMember(Member):
    FACTION = faction.KusariMain
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_KU
    WEAPON_FACTION = WEAPON_BW
    EQUIP_FACTION = EQUIP_BW


class OrdHQStoryBattleship(OrdHQMember, main_objects.KusariBattleship):
    ALIAS = 'ord_hq_musashi'
    INDEX = 1
    BASE_INDEX = 99
    REL = LEFT
    INTERIOR_CLASS = interior.BattleshipInterior
    DEALERS = dealers.KusariMilitaryDealers
    STORY = True
    CALC_STORE = False
    EQUIP_SET = markets.MusashiSecondSet
    SHIP_SET = markets.ShipSet('ku_elite')
    RU_NAME = MUSASHI
