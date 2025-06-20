from world.names import *
from universe.content.member import Member
from universe.content.system_object import LEFT, RIGHT, TOP
from universe.content import main_objects
from universe.content import zones
from universe.content import interior
from universe.content import dealers
from universe import faction

from universe import markets


class Omega13AltMember(Member):
    FACTION = faction.Corsairs


class BlackholeOsiris(Omega13AltMember, main_objects.LibertyBattleship):
    ALIAS = 'osiris_bh'
    INDEX = 1
    BASE_INDEX = 99
    REL = TOP
    INTERIOR_CLASS = interior.OsirisInterior
    DEALERS = dealers.LibertyMilitaryDealers
    STORY = True
    CALC_STORE = False
    FACTION = faction.LibertyMain
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_LI
    WEAPON_FACTION = WEAPON_LI
    EQUIP_FACTION = EQUIP_LI
    EQUIP_SET = markets.OsirisSet
    # ASF set?
    SHIP_SET = markets.ShipSet('bh_elite2')
    RU_NAME = 'Линкор Осирис'
