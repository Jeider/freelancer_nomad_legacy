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


class XenMember(Member):
    FACTION = faction.Ireland
    WEAPON_FACTION = WEAPON_BW
    EQUIP_FACTION = EQUIP_BW


class XenosKusariBattleship(XenMember, main_objects.KusariBattleship):
    ALIAS = 'start_musashi'
    INDEX = 1
    BASE_INDEX = 99
    REL = TOP
    INTERIOR_CLASS = interior.BattleshipInterior
    DEALERS = dealers.KusariMilitaryDealers
    STORY = True
    CALC_STORE = False
    FACTION = faction.KusariMain
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_KU
    EQUIP_SET = markets.OrderSet
    SHIP_SET = markets.ShipSet('ku_elite')
    RU_NAME = 'Линкор Мусаси'


class XenosKusariBattleshipTwo(XenMember, main_objects.KusariBattleship):
    ALIAS = 'leave_musashi'
    INDEX = 1
    BASE_INDEX = 98
    REL = TOP
    INTERIOR_CLASS = interior.BattleshipInterior
    DEALERS = dealers.KusariMilitaryDealers
    STORY = True
    CALC_STORE = False
    FACTION = faction.KusariMain
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_KU
    IS_BASE = False
    AUTOSAVE_FORBIDDEN = True
    RU_NAME = 'Линкор Мусаси'
