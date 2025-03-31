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
from universe.audio.space_voice import SpaceVoice
from universe import faction
from universe.content import mineable
from templates.solar import asteroid as asteroid_solar
from templates.solar import hackable
from templates.nebula import li_cal_nebula
from templates.nebula import exclusion

from templates.dockable import pirate
from templates.dockable import astbase
from templates.dockable import station_debris
from templates.dockable import manhattan_megabase
from templates.dockable import california_tradestation
from templates.dockable import roid_mining


class CalMember(Member):
    FACTION = faction.LibertyMain
    INTERIOR_BG1 = interior.INTERIOR_BG_CROW


class CalStaticText(CalMember, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = li_cal
;space_color = 10, 50, 60
space_color = 10, 50, 60
local_faction = li_grp
space_farclip = 50000

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Dust]
spacedust = Dust

[Music]
space = music_li_space
danger = music_li_danger
battle = music_li_battle

[Ambient]
;color = 5, 25, 30
color = 30, 80, 100

[Background]
nebulae = solar\\stars_mod\\li_cal_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_li_cal_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
property_flags = 512 ;lava - MILITARY
;property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = Li_Cal_system_light
pos = -31, 0, -48
color = 236, 241, 255
range = 100000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION
'''


class CalSun(CalMember, main_objects.Sun):
    STAR = 'Li02_Sun'
    LOADOUT = 'small_blue_sun_fx'
    ATMOSHPERE_RANGE = 12000
    DEATH_ZONE_SIZE = 10000

    LLIGHT_CLOUD = True
    LLIGHT_CLOUD_NAME = 'li_cal_light_cloud'
    LLIGHT_CLOUD_RANGE = 600000


class CalLargeNebula(zones.NebulaZone):
    CONTENT_TEMPLATE = li_cal_nebula.LiCalLargeNebulaTemplate
    SPACEDUST = Dust.ASTEROID
    SPACEDUST_MAXPARTICLES = 60
    MUSIC = Ambience.AST_ROCK


class CalSmallNebula(zones.NebulaZone):
    CONTENT_TEMPLATE = li_cal_nebula.LiCalSmallNebulaTemplate
    SPACEDUST = Dust.ASTEROID
    SPACEDUST_MAXPARTICLES = 60
    MUSIC = Ambience.AST_ROCK


class CalNebula1(CalMember, CalLargeNebula):
    INDEX = 1


class CalNebula2(CalMember, CalLargeNebula):
    INDEX = 2


class CalNebula3(CalMember, CalSmallNebula):
    INDEX = 3


class CalNebula4(CalMember, CalSmallNebula):
    INDEX = 4


class CalNebula5(CalMember, zones.NebulaZone):
    INDEX = 5
    CONTENT_TEMPLATE = li_cal_nebula.LiCalDangerNebulaTemplate
    SPACEDUST = Dust.RADIOACTIVE_BLUE
    SPACEDUST_MAXPARTICLES = 60
    MUSIC = Ambience.NEBULA_CROW


CROW_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.CROW_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '255, 255, 200',
    'fog_far': 5000,
}


class CalAsteroidDefinition1(asteroid_definition.CaliforniaAsteroidDefinition):
    BELT = False
    BILLBOARDS = False
    DYNAST = True
    LOOT = True
    LOOT_COMMODITY = 'comm_roid_berilium'


class CalAsteroidZone(zones.AsteroidZone):
    ASTEROID_DEFINITION_CLASS = CalAsteroidDefinition1


class CalAsteroidZone1(CalMember, CalAsteroidZone):
    INDEX = 1


class CalAsteroidZone2(CalMember, CalAsteroidZone):
    INDEX = 2


class CalAsteroidZone3(CalMember, CalAsteroidZone):
    INDEX = 3


class CalBaseRoidMiner(main_objects.RoidMiner):
    ALIAS = 'miner'
    ROTATE_RANDOM = True
    ARCHETYPE = 'Roid_Miner2'
    LOADOUT = 'roid_miner_li_cal'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    CARGO_PODS_LOADOUT = 'roid_miner_li_cal_cargo'
    ASTEROID_ARCHETYPE = 'li_cal_mining_asteroid'

    AST_EXCLUSION_ZONE_SIZE = 3000
    EXCLUSION_PARAMS = CROW_EXCLUSION_PARAMS


class CalNebula1RoidMiner(CalBaseRoidMiner):
    ASTEROID_ZONES = [CalAsteroidZone1]
    NEBULA_ZONES = [CalNebula1]


class CalNebula2RoidMiner(CalBaseRoidMiner):
    ASTEROID_ZONES = [CalAsteroidZone2]
    NEBULA_ZONES = [CalNebula2]


class CalRoidMiner1(CalMember, CalNebula1RoidMiner):
    INDEX = 1
    BASE_INDEX = 61


class CalRoidMiner2(CalMember, CalNebula1RoidMiner):
    INDEX = 2
    BASE_INDEX = 62


class CalRoidMiner3(CalMember, CalNebula1RoidMiner):
    INDEX = 3
    BASE_INDEX = 63


class CalRoidMiner4(CalMember, CalNebula1RoidMiner):
    INDEX = 4
    BASE_INDEX = 64


class CalRoidMiner5(CalMember, CalNebula1RoidMiner):
    INDEX = 5
    BASE_INDEX = 65


class CalRoidMiner6(CalMember, CalNebula2RoidMiner):
    INDEX = 6
    BASE_INDEX = 66


class CalRoidMiner7(CalMember, CalNebula2RoidMiner):
    INDEX = 7
    BASE_INDEX = 67


class CalRoidMiner8(CalMember, CalNebula2RoidMiner):
    INDEX = 8
    BASE_INDEX = 68


class CalRoidMiner9(CalMember, CalNebula2RoidMiner):
    INDEX = 9
    BASE_INDEX = 69


class CalBerliliumAsteroidReward(CalMember, mineable.AsteroidRewardsGroupUltra):
    NAME = 'li_cal_berilium'
    SOLAR = asteroid_solar.AsteroidCalifornia
    REWARD_ITEM = 'comm_roid_berilium'
    ULTRA_REWARD_BASES = [
        CalRoidMiner1,
        CalRoidMiner2,
        CalRoidMiner3,
        CalRoidMiner4,
        CalRoidMiner5,
        CalRoidMiner6,
        CalRoidMiner7,
        CalRoidMiner8,
        CalRoidMiner9,
    ]


class CalMineableField(mineable.MineableAsteroidField):
    BOX_SIZE = 1200
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.3
    DRIFT_Y = 0
    DRIFT_Z = 0.3


class CalBaseAsteroidRewardField(mineable.AsteroidRewardField):
    ALIAS = 'miner'
    FIELD_CLASS = CalMineableField
    REWARDS_GROUP_CLASS = CalBerliliumAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class CalRoidMinerAsteroids1(CalMember, CalBaseAsteroidRewardField):
    INDEX = 1
    ULTRA_BASE = CalRoidMiner1


class CalRoidMinerAsteroids2(CalMember, CalBaseAsteroidRewardField):
    INDEX = 2
    ULTRA_BASE = CalRoidMiner2


class CalRoidMinerAsteroids3(CalMember, CalBaseAsteroidRewardField):
    INDEX = 3
    ULTRA_BASE = CalRoidMiner3


class CalRoidMinerAsteroids4(CalMember, CalBaseAsteroidRewardField):
    INDEX = 4
    ULTRA_BASE = CalRoidMiner4


class CalRoidMinerAsteroids5(CalMember, CalBaseAsteroidRewardField):
    INDEX = 5
    ULTRA_BASE = CalRoidMiner5


class CalRoidMinerAsteroids6(CalMember, CalBaseAsteroidRewardField):
    INDEX = 6
    ULTRA_BASE = CalRoidMiner6


class CalRoidMinerAsteroids7(CalMember, CalBaseAsteroidRewardField):
    INDEX = 7
    ULTRA_BASE = CalRoidMiner7


class CalRoidMinerAsteroids8(CalMember, CalBaseAsteroidRewardField):
    INDEX = 8
    ULTRA_BASE = CalRoidMiner8


class CalRoidMinerAsteroids9(CalMember, CalBaseAsteroidRewardField):
    INDEX = 9
    ULTRA_BASE = CalRoidMiner9


class CalSig13Jumpgate(CalMember, main_objects.Jumpgate):
    INDEX = 1
    REL = RIGHT
    TARGET_SYSTEM_NAME = 'sig13'


class CalSig22Jumpgate(CalMember, main_objects.Jumpgate):
    INDEX = 2
    REL = LEFT
    TARGET_SYSTEM_NAME = 'sig22'


class CalVirtualPoint1(CalMember, main_objects.VirtualDepot):
    REL = TOP
    REL_APPEND = 1000


class CalDockring(CalMember, main_objects.LargePlanetDockring):
    BASE_INDEX = 1
    REL = TOP
    AUDIO_PREFIX = SpaceVoice.LI_PLANET
    INTERIOR_CLASS = interior.CustomFullSplitRoomInterior
    DEALERS = dealers.LibertyPlanetDealers

    BASE_PROPS = meta.LargePlanet(
        objectives=[
            meta.ProduceBest(POLYMERS),
            meta.ProduceCheap(GREENHOUSE_PARTS),
            meta.ProduceNormal(LUXURY_FOOD),
            meta.ProduceNormal(WATER_EXTRA),
        ]
    )


class CalMiningStation(CalMember, main_objects.RoidMinerStation):
    BASE_INDEX = 2
    REL = LEFT
    SPACE_OBJECT_TEMPLATE = roid_mining.LibertyRoidMining
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.LibertyCivilianDealers

    BASE_PROPS = meta.RoidMiningStation(
        objectives=[
            meta.ProduceBest(BERILIUM),
        ]
    )


class CalPolice(CalMember, main_objects.Outpost):
    ALIAS = 'police'
    BASE_INDEX = 3
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = manhattan_megabase.ManhattanMegabaseOutpost
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.LibertyMilitaryDealers

    ASTEROID_ZONES = [CalAsteroidZone2]
    NEBULA_ZONES = [CalNebula2]
    EXCLUSION_PARAMS = CROW_EXCLUSION_PARAMS
    REL_APPEND = 2000


class CalBattleship(CalMember, main_objects.LibertyBattleship):
    BASE_INDEX = 4
    REL = RIGHT
    INTERIOR_CLASS = interior.BattleshipInterior
    DEALERS = dealers.LibertyMilitaryDealers


class CalTrading(CalMember, main_objects.TradingBase):
    BASE_INDEX = 5
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = california_tradestation.CaliforniaTradestation
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.LibertyCivilianDealers

    BASE_PROPS = meta.LargeTradingBase()


class CalPirate1(CalMember, main_objects.PirateAsteroid):
    BASE_INDEX = 6
    REL = LEFT
    SPACE_OBJECT_TEMPLATE = astbase.CaliforniaAsteroidBase
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.LibertyPirateDealers

    FACTION = faction.LibertyPirate
    DEFENCE_LEVEL = None

    ASTEROID_ZONES = [
        CalAsteroidZone3,
    ]
    EXCLUSION_PARAMS = CROW_EXCLUSION_PARAMS
    NEBULA_ZONES = [CalNebula3]


class CalPirate2(CalMember, main_objects.PirateStation):
    INDEX = 2
    BASE_INDEX = 7
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = pirate.PirateBaseCalifornia
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.LibertyPirateDealers

    FACTION = faction.LibertyPirate
    DEFENCE_LEVEL = None

    EXCLUSION_PARAMS = CROW_EXCLUSION_PARAMS
    NEBULA_ZONES = [CalNebula4]


FIELD_TEMPLATE = '''
cube_size = 400
fill_dist = 1500
diffuse_color = 100, 150, 255
ambient_color = 100, 200, 255
ambient_increase = 20, 30, 255
empty_cube_frequency = 0.0
max_alpha = 0.300000
'''


CUBE_TEMPLATE = '''
xaxis_rotation = 8, 40, 90, 158
yaxis_rotation = 5, 45, 100, 135
zaxis_rotation = 355, 45, 78, 145
asteroid = mine_oxygen, 0.800000, -0.500000, -0.200000, 15, 90, 120, mine
asteroid = mine_oxygen, -0.300000, 0.600000, 0.800000, 85, 0, 185, mine
asteroid = mine_oxygen, 0.400000, -0.700000, -0.200000, 15, 90, 120, mine
asteroid = mine_oxygen, -0.300000, -0.300000, 0.800000, 85, 0, 185, mine
asteroid = mine_oxygen, -0.700000, 0.400000, -0.400000, 75, 30, 70, mine
'''


class CalGasPockets(asteroid_definition.AsteroidDefinition):
    FIELD = True
    CUBE = True
    FIELD_TEMPLATE = FIELD_TEMPLATE
    CUBE_TEMPLATE = CUBE_TEMPLATE


class CalGasPocketsZone1(CalMember, zones.AsteroidZone):
    ALIAS = 'pocket'
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = CalGasPockets
    SPACEDUST = Dust.RADIOACTIVE_BLUE
    SPACEDUST_MAXPARTICLES = 200


class CalAbandonedStation(CalMember, main_objects.StationRuins):
    ALIAS = 'ruins'
    INDEX = 1
    REL = RIGHT

    SPACE_OBJECT_TEMPLATE = station_debris.CaliforniaDebris

    ASTEROID_ZONES = [
        CalGasPocketsZone1,
    ]
    AST_EXCLUSION_ZONE_SIZE = 4000

    NEBULA_EXCLUSION_ZONE_SIZE = 2000
    EXCLUSION_PARAMS = CROW_EXCLUSION_PARAMS
    NEBULA_ZONES = [
        CalNebula5,
    ]


class CalAbandonedStationDropPoint1(CalMember, main_objects.HackableStation):
    ALIAS = 'ruins_dock'
    INDEX = 1
    BASE_INDEX = 51
    RELATED_OBJECT = CalAbandonedStation
    RELATED_OBJECT_INDEX = 0
    HACKABLE_SOLAR_CLASS = hackable.HackableOutpost
    INTERIOR_CLASS = interior.EquipDeckInterior


class CalAbandonedStationDropPoint2(CalMember, main_objects.HackableStation):
    ALIAS = 'ruins_dock'
    INDEX = 2
    BASE_INDEX = 52
    RELATED_OBJECT = CalAbandonedStation
    RELATED_OBJECT_INDEX = 1
    HACKABLE_SOLAR_CLASS = hackable.HackableOutpostRot90
    INTERIOR_CLASS = interior.EquipDeckInterior


class CalMiningStationConn1(CalMember, main_objects.TradeConnection):
    OBJ_FROM = CalMiningStation
    OBJ_TO = CalSig22Jumpgate
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        CalPirate1
    ]


class CalMiningStationConn2(CalMember, main_objects.TradeConnection):
    OBJ_FROM = CalMiningStation
    OBJ_TO = CalDockring
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        CalPirate1
    ]


class CalMiningStationConn3(CalMember, main_objects.TradeConnection):
    OBJ_FROM = CalMiningStation
    OBJ_TO = CalPolice
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = LEFT


class CalPoliceConn1(CalMember, main_objects.TradeConnection):
    OBJ_FROM = CalPolice
    OBJ_TO = CalVirtualPoint1
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        CalPirate2
    ]


class CalTradingConn1(CalMember, main_objects.TradeConnection):
    OBJ_FROM = CalTrading
    OBJ_TO = CalDockring
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        CalPirate2
    ]


class CalTradingConn2(CalMember, main_objects.TradeConnection):
    OBJ_FROM = CalTrading
    OBJ_TO = CalBattleship
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'F'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        CalPirate2
    ]


class CalBattleshipConn1(CalMember, main_objects.TradeConnection):
    OBJ_FROM = CalBattleship
    OBJ_TO = CalVirtualPoint1
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = LEFT


class CalBattleshipConn2(CalMember, main_objects.TradeConnection):
    OBJ_FROM = CalBattleship
    OBJ_TO = CalSig13Jumpgate
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'F'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        CalPirate2
    ]


class CalPlanet1(CalMember, main_objects.Planet):
    ARCHETYPE = 'planet_earth_3000'
    SPHERE_RADIUS = 3000
    RELATED_DOCK_RING = CalDockring


class CalPlanet2(CalMember, main_objects.Planet):
    INDEX = 2
    ARCHETYPE = 'planet_ice_blue_1000'
    PLANET_CIRCLE = False
    SPHERE_RADIUS = 1000
