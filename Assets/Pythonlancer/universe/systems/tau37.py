from fx.space import Dust
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
from templates.nebula import tau37_nebula
from templates.nebula import exclusion

from templates.dockable import astbase
from templates.dockable import trade_storages
from templates.dockable import roid_mining
from templates.dockable import station_debris


class Tau37Member(Member):
    FACTION = faction.BretoniaMain
    INTERIOR_BG1 = interior.INTERIOR_BG_WHITE
    WEAPON_FACTION = WEAPON_BR
    EQUIP_FACTION = EQUIP_BR


class Tau37StaticText(Tau37Member, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = tau37
space_color = 10, 40, 80
local_faction = br_grp
space_farclip = 60000

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Dust]
spacedust = Dust

[Music]
space = music_tau_space
danger = music_tau_danger
battle = music_tau_battle

[Ambient]
color = 80, 100, 140

[Background]
nebulae = solar\\stars_mod\\white_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_tau37_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
;property_flags = 512 ;lava - MILITARY
property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = tau37_primary_orange_light
pos = 1723, 30000, -1378
color = 255, 160, 50
range = 150000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION

[LightSource]
nickname = tau37_secondary_blue_light
pos = 0, 0, 0
color = 20, 35, 50
range = 40000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION
'''


class Tau37Sun1(Tau37Member, main_objects.Sun):
    STAR = 'proto_sun1'
    LOADOUT = 'small_blue_sun_fx'
    RING = True
    RING_ZONE_ALIAS = 'ring'
    RING_ZONE_INDEX = 1
    RING_FILE_NAME = 'tau37_ice'
    ATMOSHPERE_RANGE = 4000
    DEATH_ZONE_SIZE = 3000


class Tau37Sun2(Tau37Member, main_objects.Sun):
    INDEX = 2
    STAR = 'med_yellow_sun'
    LOADOUT = 'small_yellow_sun_fx'
    RING = True
    RING_ZONE_ALIAS = 'ring'
    RING_ZONE_INDEX = 2
    RING_FILE_NAME = 'tau37_rock'
    ATMOSHPERE_RANGE = 4000
    DEATH_ZONE_SIZE = 3000


class Tau37Nebula(zones.NebulaZone):
    CONTENT_TEMPLATE = tau37_nebula.Tau37WhiteNebulaTemplate
    SPACEDUST = Dust.ASTEROID
    SPACEDUST_MAXPARTICLES = 60
    MUSIC = Ambience.NEBULA_BARRIER


class Tau37TopNebula(Tau37Member, Tau37Nebula):
    INDEX = 1


class Tau37WestNebula(Tau37Member, Tau37Nebula):
    INDEX = 2


class Tau37EastNebula(Tau37Member, Tau37Nebula):
    INDEX = 3


BARRIER_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.ICE_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '200, 200, 180',
    'fog_far': 5000,
}


class Tau37AsteroidDefinition1(asteroid_definition.Tau37AsteroidDefinition):
    BELT = False
    BILLBOARDS = False
    DYNAST = True
    LOOT = True
    LOOT_COMMODITY = 'comm_roid_uranium'


class Tau37AsteroidZone(zones.AsteroidZone):
    ASTEROID_DEFINITION_CLASS = Tau37AsteroidDefinition1


class Tau37AsteroidZone1(Tau37Member, Tau37AsteroidZone):
    INDEX = 1


class Tau37AsteroidZone2(Tau37Member, Tau37AsteroidZone):
    INDEX = 2


class Tau37AsteroidZone3(Tau37Member, Tau37AsteroidZone):
    INDEX = 3


class Tau37BaseRoidMiner(main_objects.RoidMiner):
    ALIAS = 'miner'
    ROTATE_RANDOM = True
    ARCHETYPE = 'Roid_Miner2'
    LOADOUT = 'roid_miner_tau37'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    ASTEROID_ARCHETYPE = 'tau37_mining_asteroid'
    CARGO_PODS_LOADOUT = 'roid_miner_tau37_cargo'

    AST_EXCLUSION_ZONE_SIZE = 3000
    EXCLUSION_PARAMS = BARRIER_EXCLUSION_PARAMS


class Tau37RoidMiner1(Tau37Member, Tau37BaseRoidMiner):
    INDEX = 1
    BASE_INDEX = 61
    ASTEROID_ZONES = [Tau37AsteroidZone1]
    NEBULA_ZONES = [Tau37TopNebula]


class Tau37RoidMiner2(Tau37Member, Tau37BaseRoidMiner):
    INDEX = 2
    BASE_INDEX = 62
    ASTEROID_ZONES = [Tau37AsteroidZone1]
    NEBULA_ZONES = [Tau37TopNebula]


class Tau37RoidMiner3(Tau37Member, Tau37BaseRoidMiner):
    INDEX = 3
    BASE_INDEX = 63
    ASTEROID_ZONES = [Tau37AsteroidZone1]
    NEBULA_ZONES = [Tau37TopNebula]


class Tau37RoidMiner4(Tau37Member, Tau37BaseRoidMiner):
    INDEX = 4
    BASE_INDEX = 64
    ASTEROID_ZONES = [Tau37AsteroidZone1]
    NEBULA_ZONES = [Tau37TopNebula]


class Tau37RoidMiner5(Tau37Member, Tau37BaseRoidMiner):
    INDEX = 5
    BASE_INDEX = 65
    ASTEROID_ZONES = [Tau37AsteroidZone3]
    NEBULA_ZONES = [Tau37EastNebula]


class Tau37RoidMiner6(Tau37Member, Tau37BaseRoidMiner):
    INDEX = 6
    BASE_INDEX = 66
    ASTEROID_ZONES = [Tau37AsteroidZone3]
    NEBULA_ZONES = [Tau37EastNebula]


class Tau37RoidMiner7(Tau37Member, Tau37BaseRoidMiner):
    INDEX = 7
    BASE_INDEX = 67
    ASTEROID_ZONES = [Tau37AsteroidZone3]
    NEBULA_ZONES = [Tau37EastNebula]


class Tau37UraniumAsteroidReward(Tau37Member, mineable.AsteroidRewardsGroupUltra):
    NAME = 'tau37_gold'
    SOLAR = asteroid_solar.AsteroidTau37
    REWARD_ITEM = 'comm_roid_uranium'
    ULTRA_REWARD_BASES = [
        Tau37RoidMiner1,
        Tau37RoidMiner2,
        Tau37RoidMiner3,
        Tau37RoidMiner4,
        Tau37RoidMiner5,
        Tau37RoidMiner6,
        Tau37RoidMiner7,
    ]


class Tau37MineableField(mineable.MineableAsteroidField):
    BOX_SIZE = 1200
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.3
    DRIFT_Y = 0
    DRIFT_Z = 0.3


class Tau37BaseAsteroidRewardField(mineable.AsteroidRewardField):
    ALIAS = 'miner'
    FIELD_CLASS = Tau37MineableField
    REWARDS_GROUP_CLASS = Tau37UraniumAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class Tau37RoidMinerAsteroids1(Tau37Member, Tau37BaseAsteroidRewardField):
    INDEX = 1
    ULTRA_BASE = Tau37RoidMiner1


class Tau37RoidMinerAsteroids2(Tau37Member, Tau37BaseAsteroidRewardField):
    INDEX = 2
    ULTRA_BASE = Tau37RoidMiner2


class Tau37RoidMinerAsteroids3(Tau37Member, Tau37BaseAsteroidRewardField):
    INDEX = 3
    ULTRA_BASE = Tau37RoidMiner3


class Tau37RoidMinerAsteroids4(Tau37Member, Tau37BaseAsteroidRewardField):
    INDEX = 4
    ULTRA_BASE = Tau37RoidMiner4


class Tau37RoidMinerAsteroids5(Tau37Member, Tau37BaseAsteroidRewardField):
    INDEX = 5
    ULTRA_BASE = Tau37RoidMiner5


class Tau37RoidMinerAsteroids6(Tau37Member, Tau37BaseAsteroidRewardField):
    INDEX = 6
    ULTRA_BASE = Tau37RoidMiner6


class Tau37RoidMinerAsteroids7(Tau37Member, Tau37BaseAsteroidRewardField):
    INDEX = 7
    ULTRA_BASE = Tau37RoidMiner7


class Tau37Tau31Jumpgate(Tau37Member, main_objects.Jumpgate):
    INDEX = 1
    REL = RIGHT
    TARGET_SYSTEM_NAME = 'tau31'


class Tau37CambridgeJumpgate(Tau37Member, main_objects.Jumpgate):
    INDEX = 2
    REL = BOTTOM
    TARGET_SYSTEM_NAME = 'br_cam'


class Tau37VirtualPoint1(Tau37Member, main_objects.VirtualDepot):
    REL = TOP


class Tau37VirtualPoint2(Tau37Member, main_objects.VirtualDepot):
    INDEX = 2
    REL = BOTTOM


class Tau37MiningStation(Tau37Member, main_objects.RoidMinerStation):
    BASE_INDEX = 1
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = roid_mining.BretoniaRoidMining
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.BretoniaCivilianDealers

    BASE_PROPS = meta.RoidMiningStation(
        objectives=[
            meta.ProduceBest(URANIUM),
            meta.HaveSolarPanels(),
        ]
    )


class Tau37Freeport(Tau37Member, main_objects.Freeport):
    BASE_INDEX = 2
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = trade_storages.RheinlandOmegaStorage
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.BretoniaCivilianDealers


class Tau37Battleship(Tau37Member, main_objects.BretoniaBattleship):
    BASE_INDEX = 3
    REL = LEFT
    INTERIOR_CLASS = interior.BattleshipInterior
    DEALERS = dealers.BretoniaMilitaryDealers


class Tau37CorsairBase(Tau37Member, main_objects.PirateAsteroid):
    ALIAS = 'corsair'
    BASE_INDEX = 4
    REL = LEFT
    SPACE_OBJECT_TEMPLATE = astbase.CaliforniaAsteroidBase
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.BretoniaPirateDealers

    FACTION = faction.Corsairs
    DEFENCE_LEVEL = None

    ASTEROID_ZONES = [
        Tau37AsteroidZone2,
    ]
    EXCLUSION_PARAMS = BARRIER_EXCLUSION_PARAMS
    NEBULA_ZONES = [Tau37WestNebula]


class Tau37DeepNebulaRuins(Tau37Member, main_objects.StationRuins):
    ALIAS = 'ruins'
    INDEX = 1
    REL = RIGHT

    SPACE_OBJECT_TEMPLATE = station_debris.SigmaEightFreeport

    ASTEROID_ZONES = [
        Tau37AsteroidZone2,
    ]
    EXCLUSION_PARAMS = BARRIER_EXCLUSION_PARAMS
    NEBULA_ZONES = [Tau37WestNebula]
    NEBULA_EXCLUSION_ZONE_SIZE = 2000
    AST_EXCLUSION_ZONE_SIZE = 2500


class Tau37DeepNebulaRuinsSuprisePoint(Tau37Member, main_objects.HackableStation):
    ALIAS = 'ruins_dock'
    INDEX = 1
    BASE_INDEX = 51
    RELATED_OBJECT = Tau37DeepNebulaRuins
    HACKABLE_SOLAR_CLASS = hackable.HackableOutpost
    INTERIOR_CLASS = interior.EquipDeckInterior


class Tau37MiningStationConn1(Tau37Member, main_objects.TradeConnection):
    OBJ_FROM = Tau37MiningStation
    OBJ_TO = Tau37Tau31Jumpgate
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = TOP


class Tau37MiningStationConn2(Tau37Member, main_objects.TradeConnection):
    OBJ_FROM = Tau37MiningStation
    OBJ_TO = Tau37VirtualPoint1
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        Tau37CorsairBase
    ]


class Tau37MiningStationConn3(Tau37Member, main_objects.TradeConnection):
    OBJ_FROM = Tau37MiningStation
    OBJ_TO = Tau37Freeport
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = LEFT


class Tau37FreeportConn1(Tau37Member, main_objects.TradeConnection):
    OBJ_FROM = Tau37Freeport
    OBJ_TO = Tau37CambridgeJumpgate
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        Tau37CorsairBase
    ]


class Tau37FreeportConn2(Tau37Member, main_objects.TradeConnection):
    OBJ_FROM = Tau37Freeport
    OBJ_TO = Tau37VirtualPoint2
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'E'


class Tau37BattleshipConn1(Tau37Member, main_objects.BuoyTradeConnection):
    OBJ_FROM = Tau37Battleship
    OBJ_TO = Tau37Freeport
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'F'


class Tau37BattleshipConn2(Tau37Member, main_objects.BuoyTradeConnection):
    OBJ_FROM = Tau37Battleship
    OBJ_TO = Tau37CambridgeJumpgate
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'G'


class Tau37Planet1(Tau37Member, main_objects.Planet):
    INDEX = 1
    ARCHETYPE = 'planet_gasicecld_4000'
    SPHERE_RADIUS = 4000
