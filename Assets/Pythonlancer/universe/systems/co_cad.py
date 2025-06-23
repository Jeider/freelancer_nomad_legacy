from fx.space import Dust, JumpholeEffect
from fx.sound import Ambience
from universe.audio.space_voice import SpaceVoice, SpaceCostume

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


class CadizMember(Member):
    FACTION = faction.Ireland
    INTERIOR_BG1 = interior.INTERIOR_CO_CADIZ
    INTERIOR_BG2 = interior.INTERIOR_STARS


class CadizOrderBattleship(CadizMember, main_objects.Battleship):
    ALIAS = 'order_battleship'
    INDEX = 1
    BASE_INDEX = 99
    REL = TOP
    INTERIOR_CLASS = interior.BattleshipNoshipInterior
    DEALERS = dealers.LibertyMilitaryDealers
    STORY = True
    CALC_STORE = False
    FACTION = faction.LibertyMain
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_LI
    IS_BASE = False
    RU_NAME = 'Линкор Навухудоносор'


class CadizDockring(CadizMember, main_objects.Dockring):
    ALIAS = 'co_cad_01'
    INDEX = 1
    BASE_INDEX = 1
    REL = TOP
    AUDIO_PREFIX = SpaceVoice.CO_PLANET
    INTERIOR_CLASS = interior.StoryDummyEquipShipInterior
    DEALERS = dealers.LibertyPirateDealers
    WEAPON_FACTION = WEAPON_BW
    EQUIP_FACTION = EQUIP_BW
    MISC_EQUIP_GEN_TYPE = GEN_PIRATE
    STORY = True
    CALC_STORE = False
    FACTION = faction.Corsairs
    RU_NAME = 'Планета Кадиз'
    EQUIP_SET = markets.CorsairSet
    SHIP_SET = markets.ShipSet('pi_elite')


class CadizFreeport(CadizMember, main_objects.Dockring):
    ALIAS = 'co_cad_03'
    INDEX = 1
    BASE_INDEX = 3
    REL = TOP
    AUDIO_PREFIX = SpaceVoice.FREEPORT
    INTERIOR_CLASS = interior.StoryDummyEquipInterior
    DEALERS = dealers.LibertyPirateDealers
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_LI
    WEAPON_FACTION = WEAPON_BW
    EQUIP_FACTION = EQUIP_BW
    MISC_EQUIP_GEN_TYPE = GEN_CIV
    STORY = True
    CALC_STORE = False
    FACTION = faction.Corsairs
    RU_NAME = 'Фрипорт Тринидад'
    EQUIP_SET = markets.CorsairCivSet
