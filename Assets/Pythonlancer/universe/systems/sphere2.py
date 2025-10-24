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

from story.ingame.names import OSIRIS


class Sphere2Member(Member):
    FACTION = faction.ASF


class SphereTwoOsiris(Sphere2Member, main_objects.LibertyBattleship):
    ALIAS = 'osiris_arrive'
    INDEX = 1
    BASE_INDEX = 99
    REL = TOP
    INTERIOR_CLASS = interior.OsirisInterior
    INTERIOR_EXTRA_ROOMS = ['''
;mission 02 special room
[Room]
nickname = Deck2
file = Universe\\SPECIAL\\SPHERE2\\Room\\osiris_deck2.ini
    ''']
    DEALERS = dealers.LibertyMilitaryDealers
    STORY = True
    CALC_STORE = False
    FACTION = faction.LibertyMain
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_LI
    WEAPON_FACTION = WEAPON_LI
    EQUIP_FACTION = EQUIP_LI
    # ASF set?
    EQUIP_SET = markets.OsirisSet
    SHIP_SET = markets.ShipSet('bh_elite2')
    RU_NAME = OSIRIS
