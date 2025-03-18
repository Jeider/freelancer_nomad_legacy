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
from universe.content import faction
from universe.content import mineable
from templates.solar import hackable
from templates.solar import asteroid as asteroid_solar
from templates.nebula import tau29_nebula
from templates.nebula import exclusion
from templates.solar import gas_crystal

from templates.dockable import police
from templates.dockable import astbase
from templates.dockable import trade_storages
from templates.dockable import olaf
from templates.dockable import avalon_megabase
from templates.dockable import station_debris


class Tau29Member(Member):
    FACTION = faction.BR_GRP
    INTERIOR_BG1 = interior.INTERIOR_TAU29


class Tau37StaticText(Tau29Member, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = tau29
space_color = 60, 60, 90
local_faction = br_grp
space_farclip = 100000

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Dust]
spacedust = Dust

[Music]
space = music_tau_space
danger = music_tau_danger
battle = music_tau_battle

[Ambient]
color = 40, 40, 60

[Background]
nebulae = solar\\stars_mod\\tau29_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_tau29_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
;property_flags = 512 ;lava - MILITARY
property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = tau29_System_Light
pos = 0, 0, 0
color = 150, 190, 255
range = 150000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION
'''


class Tau29Sun(Tau29Member, main_objects.Sun):
    STAR = 'Rh04_Sun'
    LOADOUT = 'small_blue_sun_fx'


RING_DYNAST_TEMPLATE = '''
[DynamicAsteroids]
asteroid = ast_tau29_normal_a
count = 50
placement_radius = 300.000000
placement_offset = 150.000000
max_velocity = 0.01
max_angular_velocity = 0.01
color_shift = 0.6, 0.8, 1

[DynamicAsteroids]
asteroid = ast_tau29_normal_b
count = 50
placement_radius = 300.000000
placement_offset = 150.000000
max_velocity = 0.01
max_angular_velocity = 0.01
color_shift = 0.6, 0.8, 1

[DynamicAsteroids]
asteroid = ast_tau29_normal_c
count = 50
placement_radius = 300.000000
placement_offset = 150.000000
max_velocity = 0.01
max_angular_velocity = 0.01
color_shift = 0.6, 0.8, 1

'''

RING_BILLBOARDS_TEMPLATE = '''
[AsteroidBillboards]
count = 2000
start_dist = 1000
fade_dist_percent = 0.98
shape = tau29_billboards
color_shift = 0.6, 0.8, 1
;ambient_intensity = 5	
size = 30, 60
'''


class Tau29RingAsteroidsDefinition(asteroid_definition.AsteroidDefinition):
    SHAPES = [
        asteroid_definition.SHAPES_TAU29
    ]
    DYNAST = True
    BILLBOARDS = True
    DYNAST_TEMPLATE = RING_DYNAST_TEMPLATE
    BILLBOARD_TEMPLATE = RING_BILLBOARDS_TEMPLATE
    EXCLUDE_BILLBOARDS = False


class Tau29RingAsteroidsField(Tau29Member, zones.AsteroidZone):
    ALIAS = 'astring'
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = Tau29RingAsteroidsDefinition


class Tau29Planet1(Tau29Member, main_objects.Planet):
    INDEX = 1
    ARCHETYPE = 'planet_gasblucld_5000'
    SPHERE_RADIUS = 5000

    RING = True
    RING_ZONE_ALIAS = 'ring'
    RING_ZONE_INDEX = 1
    RING_FILE_NAME = 'tau29_ice'

    ASTEROID_ZONES = [Tau29RingAsteroidsField]
    AST_EXCLUSION_ZONE_SIZE = 6000


class Tau29Planet2(Tau29Member, main_objects.Planet):
    INDEX = 2
    ARCHETYPE = 'planet_rckdes_3000'
    SPHERE_RADIUS = 3000

    RING = True
    RING_ZONE_ALIAS = 'ring'
    RING_ZONE_INDEX = 2
    RING_FILE_NAME = 'tau29_rock'


class Tau29Nebula(Tau29Member, zones.NebulaZone):
    CONTENT_TEMPLATE = tau29_nebula.Tau29MainNebulaTemplate
    # SPACEDUST = Dust.ICE
    # SPACEDUST_MAXPARTICLES = 50
    MUSIC = Ambience.NEBULA_BARRIER


class Tau29NebulaGasMinerMissionMarker(Tau29Member, zones.PropertyZone):
    ALIAS = 'neb'
    INDEX = 1
    PROPERTY_FLAGS = 2048


BARRIER_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.ICE_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '120, 180, 200',
    'fog_far': 5000,
}


class Tau29AsteroidDefinition1(asteroid_definition.Tau37AsteroidDefinition):
    BELT = True
    BILLBOARDS = True
    DYNAST = True
    LOOT = False


class Tau29AsteroidZone(zones.AsteroidZone):
    ASTEROID_DEFINITION_CLASS = Tau29AsteroidDefinition1


class Tau29AsteroidZone1(Tau29Member, Tau29AsteroidZone):
    INDEX = 1

#
# class Tau29AsteroidZone2(Tau29Member, Tau29AsteroidZone):
#     INDEX = 2


class Tau29AsteroidZone3(Tau29Member, Tau29AsteroidZone):
    INDEX = 3


class Tau29AsteroidZone4(Tau29Member, Tau29AsteroidZone):
    INDEX = 4


class Tau29AsteroidZone5(Tau29Member, Tau29AsteroidZone):
    INDEX = 5


class Tau29BaseGasMiner(main_objects.GasMinerOld):
    ALIAS = 'cryst'
    ROTATE_RANDOM = True
    ARCHETYPE = 'gas_miner_old'
    LOADOUT = 'gas_miner_old_br'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    NEBULA_EXCLUSION_ZONE_SIZE = 3200
    EXCLUSION_PARAMS = BARRIER_EXCLUSION_PARAMS
    NEBULA_ZONES = [Tau29Nebula]
    NEBULA_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.ICE,
        'spacedust_maxparticles': 200,
    }


class Tau29GasMiner1(Tau29Member, Tau29BaseGasMiner):
    INDEX = 1
    BASE_INDEX = 51


class Tau29GasMiner2(Tau29Member, Tau29BaseGasMiner):
    INDEX = 2
    BASE_INDEX = 52


class Tau29GasMiner3(Tau29Member, Tau29BaseGasMiner):
    INDEX = 3
    BASE_INDEX = 53


class Tau29SimpleCrystalRewards(Tau29Member, mineable.DefaultGasCrystalRewardsGroup):
    NAME = 'sig13_gascryst_simple1'
    SOLAR = gas_crystal.SimpleCrystalAsteroid
    REWARD_ITEM = 'comm_gas_balloons'
    ULTRA_REWARD_BASES = [
        Tau29GasMiner1,
        Tau29GasMiner2,
        Tau29GasMiner3,
    ]

class Tau29SimpleCrystalField(mineable.DefaultField):
    BOX_SIZE = 1000
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.4
    DRIFT_Y = 0.4
    DRIFT_Z = 0.4
    EMPTY_CHANCE = 0.3


class Tau29BaseSimpleGasCrystalField(mineable.GasCrystalRewardField):
    FIELD_CLASS = Tau29SimpleCrystalField
    REWARDS_GROUP_CLASS = Tau29SimpleCrystalRewards
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class Tau29SimpleGasCrystalField1(Tau29Member, Tau29BaseSimpleGasCrystalField):
    INDEX = 1
    ULTRA_BASE = Tau29GasMiner1


class Tau29SimpleGasCrystalField2(Tau29Member, Tau29BaseSimpleGasCrystalField):
    INDEX = 2
    ULTRA_BASE = Tau29GasMiner2


class Tau29SimpleGasCrystalField3(Tau29Member, Tau29BaseSimpleGasCrystalField):
    INDEX = 3
    ULTRA_BASE = Tau29GasMiner3


class Tau29RingRuins(Tau29Member, main_objects.NotDockableObject):
    ALIAS = 'ruins'
    INDEX = 1
    REL = RIGHT

    SPACE_OBJECT_TEMPLATE = station_debris.ForbesDebris

    ASTEROID_ZONES = [
        Tau29RingAsteroidsField
    ]
    AST_EXCLUSION_ZONE_SIZE = 800


class Tau29RingRuinsSuprisePoint(Tau29Member, main_objects.HackableStation):
    ALIAS = 'ruins_dock'
    INDEX = 1
    BASE_INDEX = 61
    RELATED_OBJECT = Tau29RingRuins
    HACKABLE_SOLAR_CLASS = hackable.HackableOutpost
    INTERIOR_CLASS = interior.EquipDeckInterior


class Tau29CambridgeJumpgate(Tau29Member, main_objects.Jumpgate):
    INDEX = 1
    REL = TOP
    TARGET_SYSTEM_NAME = 'br_cam'


class Tau29AvalonJumpgate(Tau29Member, main_objects.Jumpgate):
    INDEX = 2
    REL = LEFT
    TARGET_SYSTEM_NAME = 'br_avl'


class Tau29WarwickJumpgate(Tau29Member, main_objects.Jumpgate):
    INDEX = 3
    REL = RIGHT
    TARGET_SYSTEM_NAME = 'br_wrw'


class Tau29VirtualPoint1(Tau29Member, main_objects.VirtualDepot):
    REL = TOP


class Tau29LargeStation(Tau29Member, main_objects.GasMiningStation):
    BASE_INDEX = 1
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = olaf.Olaf
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.BretoniaCivilianDealers

    REL_APPEND = 2000

    EXCLUSION_PARAMS = BARRIER_EXCLUSION_PARAMS
    NEBULA_ZONES = [Tau29Nebula]
    AST_EXCLUSION_ZONE_SIZE = 6000

    BASE_PROPS = meta.GasMiningStation(
        objectives=[
            meta.HaveSolarPanels(),
        ]
    )


class Tau29Trading(Tau29Member, main_objects.TradingBase):
    BASE_INDEX = 2
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = avalon_megabase.AvalonMegabaseShort
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.BretoniaCivilianDealers


class Tau29Police(Tau29Member, main_objects.Outpost):
    ALIAS = 'police'
    BASE_INDEX = 3
    REL = TOP
    SPACE_OBJECT_TEMPLATE = police.PoliceOutpostLiberty
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.BretoniaMilitaryDealers


class Tau29BottomPirates(Tau29Member, main_objects.PirateAsteroid):
    BASE_INDEX = 4
    REL = LEFT
    SPACE_OBJECT_TEMPLATE = astbase.BizmarkAsteroidBase
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.BretoniaPirateDealers

    FACTION = faction.BX_GRP
    DEFENCE_LEVEL = None

    ASTEROID_ZONES = [
        Tau29AsteroidZone3,
    ]


class Tau29TopPirates(Tau29Member, main_objects.PirateAsteroid):
    INDEX = 2
    BASE_INDEX = 5
    REL = LEFT
    SPACE_OBJECT_TEMPLATE = astbase.BerlinAsteroidBase
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.BretoniaPirateDealers

    FACTION = faction.BX_GRP
    DEFENCE_LEVEL = None
    #
    # ASTEROID_ZONES = [
    #     Tau29AsteroidZone5,
    # ]


class Tau29AbandonedAstBase1(Tau29Member, main_objects.AbandonedAsteroid):
    ALIAS = 'ast'
    INDEX = 4
    BASE_INDEX = 62
    ROTATE_RANDOM = True
    ARCHETYPE = 'miningbase_mineableA'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        Tau29AsteroidZone4,
    ]
    AST_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.ASTEROID,
        'spacedust_maxparticles': 200,
    }


class Tau29AbandonedAstBase2(Tau29Member, main_objects.AbandonedAsteroid):
    ALIAS = 'ast'
    INDEX = 1
    BASE_INDEX = 63
    ROTATE_RANDOM = True
    ARCHETYPE = 'miningbase_mineableA'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        Tau29AsteroidZone4,
    ]
    AST_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.ASTEROID,
        'spacedust_maxparticles': 200,
    }


class Tau29AsteroidReward(Tau29Member, mineable.AsteroidRewardsGroupUltra):
    NAME = 'tau29_unlock'
    SOLAR = asteroid_solar.AsteroidTau37
    REWARD_ITEM = 'comm_roid_uranium'
    ULTRA_REWARD_BASES = [
        Tau29AbandonedAstBase1,
        Tau29AbandonedAstBase2,
    ]


class Tau29AsteroidNoReward(Tau29Member, mineable.AsteroidRewardsGroupUltra):
    NAME = 'tau29_any'
    SOLAR = asteroid_solar.AsteroidTau37
    REWARD_ITEM = 'comm_roid_uranium'


class Tau29MineableField(mineable.MineableAsteroidField):
    BOX_SIZE = 1400
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.3
    DRIFT_Y = 0
    DRIFT_Z = 0.3


class Tau29BaseAsteroidRewardField(mineable.AsteroidRewardField):
    ALIAS = 'ast'
    FIELD_CLASS = Tau29MineableField
    REWARDS_GROUP_CLASS = Tau29AsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class Tau29BaseAsteroidNoRewardField(mineable.AsteroidRewardField):
    ALIAS = 'ast'
    FIELD_CLASS = Tau29MineableField
    REWARDS_GROUP_CLASS = Tau29AsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25
    ULTRA_REWARD = False


class Tau29RewardAsteroids1(Tau29Member, Tau29BaseAsteroidRewardField):
    INDEX = 1
    ULTRA_BASE = Tau29AbandonedAstBase2

#
# class Tau29RewardAsteroids2(Tau29Member, Tau29BaseAsteroidRewardField):
#     INDEX = 2


class Tau29RewardAsteroids3(Tau29Member, Tau29BaseAsteroidNoRewardField):
    INDEX = 3


class Tau29RewardAsteroids4(Tau29Member, Tau29BaseAsteroidRewardField):
    INDEX = 4
    ULTRA_BASE = Tau29AbandonedAstBase1


class Tau29RewardAsteroids5(Tau29Member, Tau29BaseAsteroidNoRewardField):
    INDEX = 5


class Tau29LargeStationConn1(Tau29Member, main_objects.TradeConnection):
    OBJ_FROM = Tau29LargeStation
    OBJ_TO = Tau29CambridgeJumpgate
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        Tau29TopPirates
    ]


class Tau29LargeStationConn2(Tau29Member, main_objects.TradeConnection):
    OBJ_FROM = Tau29LargeStation
    OBJ_TO = Tau29WarwickJumpgate
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'B'


class Tau29LargeStationConn3(Tau29Member, main_objects.TradeConnection):
    OBJ_FROM = Tau29LargeStation
    OBJ_TO = Tau29Trading
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        Tau29TopPirates
    ]


class Tau29PoliceConn1(Tau29Member, main_objects.TradeConnection):
    OBJ_FROM = Tau29Police
    OBJ_TO = Tau29Trading
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        Tau29BottomPirates
    ]


class Tau29PoliceConn2(Tau29Member, main_objects.TradeConnection):
    OBJ_FROM = Tau29Police
    OBJ_TO = Tau29AvalonJumpgate
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        Tau29BottomPirates
    ]


class Tau29PoliceBuoyConn1(Tau29Member, main_objects.AbandonedBuoyTradeConnection):
    OBJ_FROM = Tau29Police
    OBJ_TO = Tau29VirtualPoint1
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'F'


class Tau29TradingBrokenConn1(Tau29Member, main_objects.BrokenTradeConnection):
    OBJ_FROM = Tau29Trading
    OBJ_TO = Tau29WarwickJumpgate
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'G'
    OBJ_TO_TLR_FORCE_OFFSET = (57000, 0, 7000)
