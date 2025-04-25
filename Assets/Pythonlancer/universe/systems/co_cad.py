from fx.space import Dust, JumpholeEffect
from fx.sound import Ambience

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


class CadizMember(Member):
    FACTION = faction.Ireland


class CadizOrderBattleship(CadizMember, main_objects.Battleship):
    ALIAS = 'order_battleship'
    INDEX = 1
    BASE_INDEX = 99
    REL = TOP
    INTERIOR_CLASS = interior.BattleshipInterior
    DEALERS = dealers.LibertyMilitaryDealers
    STORY = True
    CALC_STORE = False
    FACTION = faction.LibertyMain
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_LI
