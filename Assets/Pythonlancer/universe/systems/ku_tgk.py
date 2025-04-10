from fx.space import Dust, JumpholeEffect
from fx.sound import Ambience

from managers.tools import query as Q
from world.names import *
from universe.content import meta

from universe.content.member import Member
from universe.content.system_object import TOP, BOTTOM, LEFT, RIGHT
from universe.content import main_objects
from universe.content import zones
from universe.content import asteroid_definition
from universe.content import interior
from universe.content import dealers
from universe import faction
from universe.content import mineable
from templates.solar import hackable
from templates.solar import asteroid as asteroid_solar

from templates.dockable import astbase
from templates.dockable import trade_storages
from templates.dockable import tekagi_megabase
from templates.dockable import roid_mining
from templates.dockable import station_debris


class TekagiMember(Member):
    FACTION = faction.KusariMain
    INTERIOR_BG1 = interior.INTERIOR_KU_TAKAGI


class TekagiStaticText(TekagiMember, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = ku_tgk
space_color = 0, 0, 0
local_faction = ku_grp
space_farclip = 70000

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Dust]
spacedust = Dust

[Music]
space = music_ku_space
danger = music_ku_danger
battle = music_ku_battle

[Ambient]
color = 12, 10, 10

[Background]
nebulae = solar\\stars_mod\\ku_tgk_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_ku_tgk_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
;property_flags = 512 ;lava - MILITARY
property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = TGK_system_light
pos = 0, 0, 0
color = 255, 245, 225
range = 90000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION
'''


class TekagiSun(TekagiMember, main_objects.Sun):
    STAR = 'ku07_Sun'
    LOADOUT = 'small_yellow_sun_fx'


class TekagiAsteroidDefinition1(asteroid_definition.TekagiAsteroidDefinition):
    BELT = True
    BILLBOARDS = True
    DYNAST = True
    LOOT = True
    BELT_HEIGHT = 8000
    LOOT_COMMODITY = 'comm_roid_gold'


class TekagiAsteroidZone(zones.AsteroidZone):
    ASTEROID_DEFINITION_CLASS = TekagiAsteroidDefinition1
    SPACEDUST = Dust.ASTEROID
    SPACEDUST_MAXPARTICLES = 100
    MUSIC = Ambience.AST_ROCK


class TekagiAsteroidZone1(TekagiMember, TekagiAsteroidZone):
    INDEX = 1


class TekagiAsteroidZone2(TekagiMember, TekagiAsteroidZone):
    INDEX = 2


class TekagiAsteroidZone3(TekagiMember, TekagiAsteroidZone):
    INDEX = 3


class TekagiAsteroidZone4(TekagiMember, TekagiAsteroidZone):
    INDEX = 4


class TekagiAsteroidZone5(TekagiMember, TekagiAsteroidZone):
    INDEX = 5


class TekagiAsteroidZone6(TekagiMember, TekagiAsteroidZone):
    INDEX = 6


class TekagiAsteroidZone7(TekagiMember, TekagiAsteroidZone):
    INDEX = 7


class TekagiAsteroidZone8(TekagiMember, TekagiAsteroidZone):
    INDEX = 8


class TekagiAsteroidZone9(TekagiMember, TekagiAsteroidZone):
    INDEX = 9


class TekagiAsteroidZone10(TekagiMember, TekagiAsteroidZone):
    INDEX = 10


class TekagiAsteroidZone11(TekagiMember, TekagiAsteroidZone):
    INDEX = 11


class TekagiAsteroidZone12(TekagiMember, TekagiAsteroidZone):
    INDEX = 12


class TekagiAsteroidZone13(TekagiMember, TekagiAsteroidZone):
    INDEX = 13


class TekagiBaseRoidMiner(main_objects.RoidMiner):
    ALIAS = 'miner'
    ROTATE_RANDOM = True
    ARCHETYPE = 'Roid_Miner2'
    LOADOUT = 'roid_miner_ku_tgk'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    ASTEROID_ARCHETYPE = 'ku_tgk_mining_asteroid'
    CARGO_PODS_LOADOUT = 'roid_miner_ku_tgk_cargo'

    AST_EXCLUSION_ZONE_SIZE = 3000


class TekagiRoidMiner1(TekagiMember, TekagiBaseRoidMiner):
    INDEX = 1
    BASE_INDEX = 61
    ASTEROID_ZONES = [TekagiAsteroidZone2]


class TekagiRoidMiner2(TekagiMember, TekagiBaseRoidMiner):
    INDEX = 2
    BASE_INDEX = 62
    ASTEROID_ZONES = [TekagiAsteroidZone3]


class TekagiRoidMiner3(TekagiMember, TekagiBaseRoidMiner):
    INDEX = 3
    BASE_INDEX = 63
    ASTEROID_ZONES = [TekagiAsteroidZone1]


class TekagiRoidMiner4(TekagiMember, TekagiBaseRoidMiner):
    INDEX = 4
    BASE_INDEX = 64
    ASTEROID_ZONES = [TekagiAsteroidZone1]


class TekagiRoidMiner5(TekagiMember, TekagiBaseRoidMiner):
    INDEX = 5
    BASE_INDEX = 65
    ASTEROID_ZONES = [TekagiAsteroidZone4]


class TekagiRoidMiner6(TekagiMember, TekagiBaseRoidMiner):
    INDEX = 6
    BASE_INDEX = 66
    ASTEROID_ZONES = [TekagiAsteroidZone2]


class TekagiRoidMiner7(TekagiMember, TekagiBaseRoidMiner):
    INDEX = 7
    BASE_INDEX = 67
    ASTEROID_ZONES = [TekagiAsteroidZone5]


class TekagiRoidMiner8(TekagiMember, TekagiBaseRoidMiner):
    INDEX = 8
    BASE_INDEX = 68
    ASTEROID_ZONES = [TekagiAsteroidZone9]


class TekagiRoidMiner9(TekagiMember, TekagiBaseRoidMiner):
    INDEX = 9
    BASE_INDEX = 69
    ASTEROID_ZONES = [TekagiAsteroidZone8]


class TekagiRoidMiner10(TekagiMember, TekagiBaseRoidMiner):
    INDEX = 10
    BASE_INDEX = 70
    ASTEROID_ZONES = [TekagiAsteroidZone8]


class TekagiGoldAsteroidReward(TekagiMember, mineable.AsteroidRewardsGroupUltra):
    NAME = 'ku_tgk_gold'
    SOLAR = asteroid_solar.AsteroidTekagi
    REWARD_ITEM = 'comm_roid_gold'
    ULTRA_REWARD_BASES = [
        TekagiRoidMiner1,
        TekagiRoidMiner2,
        TekagiRoidMiner3,
        TekagiRoidMiner4,
        TekagiRoidMiner5,
        TekagiRoidMiner6,
        TekagiRoidMiner7,
        TekagiRoidMiner8,
        TekagiRoidMiner9,
        TekagiRoidMiner10,
    ]


class TekagiMineableField(mineable.MineableAsteroidField):
    BOX_SIZE = 1500
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.3
    DRIFT_Y = 0
    DRIFT_Z = 0.3


class TekagiBaseAsteroidRewardField(mineable.AsteroidRewardField):
    ALIAS = 'miner'
    FIELD_CLASS = TekagiMineableField
    REWARDS_GROUP_CLASS = TekagiGoldAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class TekagiRoidMinerAsteroids1(TekagiMember, TekagiBaseAsteroidRewardField):
    INDEX = 1
    ULTRA_BASE = TekagiRoidMiner1


class TekagiRoidMinerAsteroids2(TekagiMember, TekagiBaseAsteroidRewardField):
    INDEX = 2
    ULTRA_BASE = TekagiRoidMiner2


class TekagiRoidMinerAsteroids3(TekagiMember, TekagiBaseAsteroidRewardField):
    INDEX = 3
    ULTRA_BASE = TekagiRoidMiner3


class TekagiRoidMinerAsteroids4(TekagiMember, TekagiBaseAsteroidRewardField):
    INDEX = 4
    ULTRA_BASE = TekagiRoidMiner4


class TekagiRoidMinerAsteroids5(TekagiMember, TekagiBaseAsteroidRewardField):
    INDEX = 5
    ULTRA_BASE = TekagiRoidMiner5


class TekagiRoidMinerAsteroids6(TekagiMember, TekagiBaseAsteroidRewardField):
    INDEX = 6
    ULTRA_BASE = TekagiRoidMiner6


class TekagiRoidMinerAsteroids7(TekagiMember, TekagiBaseAsteroidRewardField):
    INDEX = 7
    ULTRA_BASE = TekagiRoidMiner7


class TekagiRoidMinerAsteroids8(TekagiMember, TekagiBaseAsteroidRewardField):
    INDEX = 8
    ULTRA_BASE = TekagiRoidMiner8


class TekagiRoidMinerAsteroids9(TekagiMember, TekagiBaseAsteroidRewardField):
    INDEX = 9
    ULTRA_BASE = TekagiRoidMiner9

class TekagiRoidMinerAsteroids10(TekagiMember, TekagiBaseAsteroidRewardField):
    INDEX = 10
    ULTRA_BASE = TekagiRoidMiner10


class TekagiHonshuJumpgate(TekagiMember, main_objects.Jumpgate):
    INDEX = 1
    REL = RIGHT
    TARGET_SYSTEM_NAME = 'ku_hns'


class TekagiHokkaidoJumpgate(TekagiMember, main_objects.Jumpgate):
    INDEX = 2
    REL = LEFT
    TARGET_SYSTEM_NAME = 'ku_hkd'


class TekagiLargeStation(TekagiMember, main_objects.Station):
    BASE_INDEX = 1
    REL = TOP
    SPACE_OBJECT_TEMPLATE = tekagi_megabase.TekagiMegabase
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.KusariCivilianDealers

    REL_APPEND = 4000

    BASE_PROPS = meta.MegaTradingbase(
        objectives=[
            meta.ProduceBest(ELECTRONICS),
            meta.ProduceBad(TLR_PARTS),
            meta.ProduceBad(JUMPGATE_PARTS),
        ]
    )


class TekagiMiningStation(TekagiMember, main_objects.RoidMinerStation):
    INDEX = 2
    BASE_INDEX = 2
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = roid_mining.UpsilonRoidMining
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.KusariCivilianDealers

    BASE_PROPS = meta.RoidMiningStation(
        objectives=[
            meta.ProduceBest(GOLD),
        ]
    )


class TekagiFreeport(TekagiMember, main_objects.Freeport):
    INDEX = 1
    BASE_INDEX = 3
    REL = TOP
    SPACE_OBJECT_TEMPLATE = trade_storages.TekagiStorage
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.KusariCivilianDealers


class TekagiWestPirates(TekagiMember, main_objects.PirateAsteroid):
    INDEX = 1
    BASE_INDEX = 4
    REL = LEFT
    SPACE_OBJECT_TEMPLATE = astbase.BerlinAsteroidBase
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.KusariPirateDealers

    FACTION = faction.KusariPirate
    DEFENCE_LEVEL = None


class TekagiEastPirates(TekagiMember, main_objects.PirateAsteroid):
    INDEX = 2
    BASE_INDEX = 5
    REL = LEFT
    SPACE_OBJECT_TEMPLATE = astbase.CaliforniaAsteroidBase
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.KusariPirateDealers

    FACTION = faction.KusariPirate
    DEFENCE_LEVEL = None


class TekagiRuins(TekagiMember, main_objects.StationRuins):
    ALIAS = 'ruins'
    INDEX = 1
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = station_debris.TekagiDebris
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.KusariPirateDealers
    REL_APPEND = 6000


class TekagiRuinsDropPoint1(TekagiMember, main_objects.HackableStation):
    ALIAS = 'ruins_dock'
    INDEX = 1
    BASE_INDEX = 51
    RELATED_OBJECT = TekagiRuins
    RELATED_OBJECT_INDEX = 0
    HACKABLE_SOLAR_CLASS = hackable.HackableOutpostRot90
    INTERIOR_CLASS = interior.EquipDeckInterior


class TekagiRuinsDropPoint2(TekagiMember, main_objects.HackableStation):
    ALIAS = 'ruins_dock'
    INDEX = 2
    BASE_INDEX = 52
    RELATED_OBJECT = TekagiRuins
    RELATED_OBJECT_INDEX = 1
    HACKABLE_SOLAR_CLASS = hackable.HackableOutpostRot90
    INTERIOR_CLASS = interior.EquipDeckInterior


class TekagiVirtualDepot(TekagiMember, main_objects.VirtualDepot):
    REL = TOP


class TekagiFreeportConn1(TekagiMember, main_objects.TradeConnection):
    OBJ_FROM = TekagiFreeport
    OBJ_TO = TekagiHonshuJumpgate
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        TekagiEastPirates
    ]


class TekagiFreeportConn2(TekagiMember, main_objects.TradeConnection):
    OBJ_FROM = TekagiFreeport
    OBJ_TO = TekagiLargeStation
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        TekagiEastPirates
    ]


class TekagiMiningStationConn1(TekagiMember, main_objects.TradeConnection):
    OBJ_FROM = TekagiMiningStation
    OBJ_TO = TekagiLargeStation
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        TekagiWestPirates
    ]


class TekagiMiningStationConn2(TekagiMember, main_objects.TradeConnection):
    OBJ_FROM = TekagiMiningStation
    OBJ_TO = TekagiHokkaidoJumpgate
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        TekagiWestPirates
    ]


class TekagiLargeStationVirtualConn1(TekagiMember, main_objects.TradeConnection):
    OBJ_FROM = TekagiLargeStation
    OBJ_TO = TekagiVirtualDepot
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = BOTTOM


class TekagiMiningStationBrokenConn1(TekagiMember, main_objects.BrokenTradeConnection):
    OBJ_FROM = TekagiMiningStation
    OBJ_TO = TekagiRuins
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'F'


class TekagiSiriusJumphole(TekagiMember, main_objects.Jumphole):
    REL = TOP

    TARGET_SYSTEM_NAME = 'sig42'
    LOCKED_DOCK = True

    LOADOUT = JumpholeEffect.LIGHT
