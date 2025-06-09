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


class SphereMember(Member):
    FACTION = faction.ASF


class SphereOneMissouri(SphereMember, main_objects.LibertyBattleship):
    ALIAS = 'dread_arrive'
    INDEX = 1
    BASE_INDEX = 1
    REL = TOP
    INTERIOR_CLASS = interior.BattleshipInterior
    INTERIOR_EXTRA_ROOMS = [r'''
[Room]
nickname = Deck2
file = Universe\SPECIAL\SPHERE\ROOM\dread_mnh_deck.ini

[Room]
nickname = Deck3
file = Universe\SPECIAL\SPHERE\ROOM\dread_mnh_deck.ini
    ''']
    DEALERS = dealers.LibertyMilitaryDealers
    STORY = True
    CALC_STORE = False
    FACTION = faction.LibertyMain
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_LI
    WEAPON_FACTION = WEAPON_LI
    EQUIP_FACTION = EQUIP_LI
    # ASF set?
    SHIP_SET = markets.ShipSet('bh_elite')
    OFFER_MISSIONS = False


class SphereOneMissouriTorp(SphereMember, main_objects.LibertyBattleship):
    ALIAS = 'dread_defend'
    INDEX = 1
    BASE_INDEX = 2
    REL = TOP
    INTERIOR_CLASS = interior.BattleshipInterior
    INTERIOR_EXTRA_ROOMS = [r'''
[Room]
nickname = Deck2
file = Universe\SPECIAL\SPHERE\ROOM\dread_mnh_deck.ini

[Room]
nickname = Deck3
file = Universe\SPECIAL\SPHERE\ROOM\dread_mnh_deck.ini
    ''']
    DEALERS = dealers.LibertyMilitaryDealers
    STORY = True
    CALC_STORE = False
    FACTION = faction.LibertyMain
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_LI
    WEAPON_FACTION = WEAPON_LI
    EQUIP_FACTION = EQUIP_LI
    # ASF set?
    SHIP_SET = markets.ShipSet('bh_elite')


class SphereOneLab(SphereMember, main_objects.Station):
    ALIAS = 'sphere_laboratory0'
    INDEX = 1
    BASE_INDEX = 99
    REL = TOP
    INTERIOR_CLASS = interior.StoryDummyInterior
    STORY = True
    CALC_STORE = False
    FACTION = faction.LibertyMain
    IS_BASE = False


class SphereOneDepotOne(SphereMember, main_objects.Station):
    ALIAS = 'sphere_depot_0'
    INDEX = 1
    BASE_INDEX = 91
    REL = TOP
    INTERIOR_CLASS = interior.StoryDummyInterior
    STORY = True
    CALC_STORE = False
    FACTION = faction.LibertyMain
    IS_BASE = False


class SphereOneDepotTwo(SphereMember, main_objects.Station):
    ALIAS = 'sphere_depot_0'
    INDEX = 2
    BASE_INDEX = 92
    REL = TOP
    INTERIOR_CLASS = interior.StoryDummyInterior
    STORY = True
    CALC_STORE = False
    FACTION = faction.LibertyMain
    IS_BASE = False
