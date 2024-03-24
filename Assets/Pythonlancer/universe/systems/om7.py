from fx.space import Dust
from fx.sound import Ambience

from universe.content.system_object import TOP, BOTTOM, LEFT, RIGHT
from universe.content import main_objects
from universe.content import zones
from universe.content import asteroid_definition
from universe.content import interior
from universe.content import dealers
from universe.content.space_voice import SpaceVoice
from universe.content import faction
from universe.content import mineable
from universe.content import population
from templates.solar import suprise

from templates.nebula import exclusion
from templates.nebula import om7_nebula
from templates.solar import gas_crystal
from templates.solar import hackable

from templates.dockable import pirate
from templates.dockable import gas_miner
from templates.dockable import trade_storages
from templates.dockable import kusari_palace
from templates.dockable import station_debris
from templates.dockable import shipyards
from templates.dockable import alg
from templates.dockable import research
from templates.dockable import rheinland_military


class Om7Member(object):
    INDEX = 1
    ABSTRACT = False
    FACTION = faction.KU_GRP

    INTERIOR_BG1 = interior.INTERIOR_BG_WALKER


class Om7Kusari(object):
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_KU
    FACTION = faction.KU_GRP


class Om7Rheinland(object):
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_RH
    POPULATION_KIND = population.POP_SECOND
    FACTION = faction.RH_GRP


class Om7StaticText(Om7Member, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = om7
space_color = 0,0,0
local_faction = ku_grp

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Dust]
spacedust = Dust

[Music]
space = music_omega_space
danger = music_omega_danger
battle = music_omega_battle

[Ambient]
color = 0,0,0

[Background]
complex_stars = solar\stars_mod\new_generic.cmp
basic_stars = solar\stars_mod\new_generic.cmp

[zone]
nickname = zone_om7_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
;property_flags = 512 ;lava - MILITARY
;property_flags = 256 ;ice - TRADING
property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = om7_system_light
pos = -1, 0, -1
color = 255, 200, 125
range = 80000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION
'''


class Om7Nebula(Om7Member, zones.NebulaZone):
    INDEX = 1
    MUSIC = Ambience.NEBULA_WALKER
    CONTENT_TEMPLATE = om7_nebula.Om7MainNebulaTemplate
    INTERFERENCE = 0.5


WALKER_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.WALKER_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '120, 125, 130',
    'fog_far': 5000,
}


class Om7Sun(Om7Member, main_objects.SunSmall):
    STAR = 'med_white_sun'


class Om7HokkaidoJumpgate(Om7Member, main_objects.Jumpgate):
    INDEX = 1
    REL = LEFT


class Om7StuttgartJumpgate(Om7Member, main_objects.Jumpgate):
    INDEX = 2
    REL = RIGHT


class Om7KusariStation(Om7Member, Om7Kusari, main_objects.Station):
    INDEX = 1
    BASE_INDEX = 1
    REL = TOP
    REL_DRIFT = 0
    REL_APPEND = 2000
    ARCHETYPE = 'smallstation1_old'
    LOADOUT = 'smallstation_ku'
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.KusariCivilianDealers

    NEBULA_EXCLUSION_ZONE_SIZE = 5000
    EXCLUSION_PARAMS = WALKER_EXCLUSION_PARAMS
    NEBULA_ZONES = [Om7Nebula]

    FACTION = faction.KU_GRP


class Om7RheinlandStation(Om7Member, Om7Rheinland, main_objects.Station):
    INDEX = 2
    BASE_INDEX = 2
    REL = TOP
    REL_DRIFT = 0
    REL_APPEND = 2000
    ARCHETYPE = 'smallstation1_old'
    LOADOUT = 'smallstation_rh'
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.RheinlandCivilianDealers

    NEBULA_EXCLUSION_ZONE_SIZE = 5000
    EXCLUSION_PARAMS = WALKER_EXCLUSION_PARAMS
    NEBULA_ZONES = [Om7Nebula]

    FACTION = faction.RH_GRP


class Om7Battleship(Om7Member, Om7Rheinland, main_objects.RheinlandBattleship):
    BASE_INDEX = 3
    REL = LEFT
    REL_APPEND = 1000
    REL_DRIFT = 500
    INTERIOR_CLASS = interior.BattleshipInterior
    DEALERS = dealers.RheinlandMilitaryDealers
    FACTION = faction.RH_GRP

    NEBULA_EXCLUSION_ZONE_SIZE = 3000
    EXCLUSION_PARAMS = WALKER_EXCLUSION_PARAMS
    NEBULA_ZONES = [Om7Nebula]


class Om7Freeport(Om7Member, Om7Kusari, main_objects.Freeport):
    BASE_INDEX = 4
    REL = TOP
    REL_APPEND = 2000
    SPACE_OBJECT_TEMPLATE = trade_storages.HonshuStorage
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.KusariCivilianDealers

    NEBULA_EXCLUSION_ZONE_SIZE = 3500
    EXCLUSION_PARAMS = WALKER_EXCLUSION_PARAMS
    NEBULA_ZONES = [Om7Nebula]

    FACTION = faction.KU_GRP


class Om7PirateLargeAsteroid(Om7Member, Om7Kusari, main_objects.PirateBase):
    BASE_INDEX = 5
    INDEX = 1
    REL = BOTTOM
    REL_APPEND = 4000
    SPACE_OBJECT_TEMPLATE = kusari_palace.KusariPalace
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.KusariPirateDealers
    FACTION = faction.KX_GRP
    DEFENCE_LEVEL = None

    NEBULA_EXCLUSION_ZONE_SIZE = 5000
    EXCLUSION_PARAMS = WALKER_EXCLUSION_PARAMS
    NEBULA_ZONES = [Om7Nebula]


class Om7RightPirates(Om7Member, Om7Rheinland, main_objects.PirateBase):
    BASE_INDEX = 6
    INDEX = 2
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = gas_miner.RheinlandPirateGasMiner
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.RheinlandPirateDealers
    FACTION = faction.RX_GRP
    DEFENCE_LEVEL = None

    NEBULA_EXCLUSION_ZONE_SIZE = 2000
    EXCLUSION_PARAMS = WALKER_EXCLUSION_PARAMS
    NEBULA_ZONES = [Om7Nebula]


class Om7LostRheinlandRuins(Om7Member, Om7Rheinland, main_objects.NotDockableObject):
    ALIAS = 'ruins'
    INDEX = 1
    REL = RIGHT

    REL_APPEND = 1500

    SPACE_OBJECT_TEMPLATE = station_debris.StuttgartDestroyedOutpost

    NEBULA_EXCLUSION_ZONE_SIZE = 2000
    EXCLUSION_PARAMS = WALKER_EXCLUSION_PARAMS
    NEBULA_ZONES = [Om7Nebula]


class Om7LostRheinlandRuinsSuprisePoint(Om7Member, Om7Rheinland, main_objects.HackableStation):
    ALIAS = 'ruins_dock'
    INDEX = 1
    BASE_INDEX = 71
    RELATED_OBJECT = Om7LostRheinlandRuins
    HACKABLE_SOLAR_CLASS = hackable.HackableOutpostRot90
    INTERIOR_CLASS = interior.EquipDeckInterior


class Om7KusariStationConn1(Om7Member, main_objects.TradeConnection):
    OBJ_FROM = Om7KusariStation
    OBJ_TO = Om7HokkaidoJumpgate
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        Om7PirateLargeAsteroid
    ]


class Om7KusariStationConn2(Om7Member, main_objects.TradeConnection):
    OBJ_FROM = Om7KusariStation
    OBJ_TO = Om7Freeport
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        Om7PirateLargeAsteroid
    ]


class Om7RheinlandStationConn1(Om7Member, Om7Rheinland, main_objects.TradeConnection):
    OBJ_FROM = Om7RheinlandStation
    OBJ_TO = Om7Freeport
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        Om7RightPirates
    ]


class Om7RheinlandStationConn2(Om7Member, Om7Rheinland, main_objects.TradeConnection):
    OBJ_FROM = Om7RheinlandStation
    OBJ_TO = Om7StuttgartJumpgate
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        Om7RightPirates
    ]


class Om7RheinlandStationConn3(Om7Member, Om7Rheinland, main_objects.TradeConnection):
    OBJ_FROM = Om7RheinlandStation
    OBJ_TO = Om7Battleship
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        Om7RightPirates
    ]


class Om7PalaceConn1(Om7Member, main_objects.BrokenTradeConnection):
    OBJ_FROM = Om7PirateLargeAsteroid
    OBJ_TO = Om7HokkaidoJumpgate
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'F'
    OBJ_TO_TLR_FORCE_OFFSET = (-47000, 0, -17000)


class Om7PalaceConn2(Om7Member, main_objects.BrokenTradeConnection):
    OBJ_FROM = Om7PirateLargeAsteroid
    OBJ_TO = Om7Freeport
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'G'
    OBJ_TO_TLR_FORCE_OFFSET = (-6000, 0, -16000)


class Om7PalaceConn3(Om7Member, main_objects.BrokenTradeConnection):
    OBJ_FROM = Om7PirateLargeAsteroid
    OBJ_TO = Om7LostRheinlandRuins
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'H'


class Om7RheinlandRuinsConn1(Om7Member, main_objects.BrokenTradeConnection):
    OBJ_FROM = Om7LostRheinlandRuins
    OBJ_TO = Om7Battleship
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'I'

    OBJ_TO_TLR_FORCE_OFFSET = (8000, 0, 24000)


class Om7BaseKusariGasMiner(Om7Kusari, main_objects.GasMinerOld):
    ALIAS = 'cryst'
    ROTATE_RANDOM = True
    ARCHETYPE = 'gas_miner_old'
    LOADOUT = 'gas_miner_old_ku'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    NEBULA_EXCLUSION_ZONE_SIZE = 3000
    EXCLUSION_PARAMS = WALKER_EXCLUSION_PARAMS
    NEBULA_ZONES = [Om7Nebula]
    NEBULA_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.ICE,
        'spacedust_maxparticles': 200,
    }


class Om7BaseRheinlandGasMiner(Om7Rheinland, main_objects.GasMinerOld):
    ALIAS = 'cryst'
    ROTATE_RANDOM = True
    ARCHETYPE = 'gas_miner_old'
    LOADOUT = 'gas_miner_old_rh'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    NEBULA_EXCLUSION_ZONE_SIZE = 3000
    EXCLUSION_PARAMS = WALKER_EXCLUSION_PARAMS
    NEBULA_ZONES = [Om7Nebula]
    INTERIOR_BG1 = interior.INTERIOR_BG_CROW
    NEBULA_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.ICE,
        'spacedust_maxparticles': 200,
    }


class Om7BaseAbandonedMiner(main_objects.AbandonedAsteroid):
    ALIAS = 'bigcryst'
    ROTATE_RANDOM = True
    ARCHETYPE = 'miningbase_ice_block'
    # LOADOUT = 'miningbase_ice_block_pi_01'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    NEBULA_EXCLUSION_ZONE_SIZE = 8500
    AST_EXCLUSION_ZONE_SIZE = 2000
    EXCLUSION_PARAMS = WALKER_EXCLUSION_PARAMS
    NEBULA_ZONES = [Om7Nebula]
    INTERIOR_BG1 = interior.INTERIOR_BG_CROW
    AST_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.ICE,
        'spacedust_maxparticles': 200,
    }


FIELD_TEMPLATE = '''
cube_size = 400
fill_dist = 1500
diffuse_color = 255, 140, 30
ambient_color = 40, 20, 0
ambient_increase = 60, 30, 10
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

class Om7GasPockets(asteroid_definition.AsteroidDefinition):
    FIELD = True
    CUBE = True
    FIELD_TEMPLATE = FIELD_TEMPLATE
    CUBE_TEMPLATE = CUBE_TEMPLATE


class Om7GasPocketsZone1(Om7Member, zones.AsteroidZone):
    ALIAS = 'bigcryst'
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = Om7GasPockets
    SPACEDUST = Dust.OXYGEN
    SPACEDUST_MAXPARTICLES = 200


class Om7GasPocketsZone2(Om7Member, zones.AsteroidZone):
    ALIAS = 'bigcryst'
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = Om7GasPockets
    SPACEDUST = Dust.OXYGEN
    SPACEDUST_MAXPARTICLES = 200


class Om7GasPocketsZone3(Om7Member, zones.AsteroidZone):
    ALIAS = 'bigcryst'
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = Om7GasPockets
    SPACEDUST = Dust.OXYGEN
    SPACEDUST_MAXPARTICLES = 200


class Om7GasMiner1(Om7Member, Om7BaseKusariGasMiner):
    INDEX = 1
    BASE_INDEX = 51


class Om7GasMiner2(Om7Member, Om7BaseKusariGasMiner):
    INDEX = 2
    BASE_INDEX = 52


class Om7GasMiner3(Om7Member, Om7BaseKusariGasMiner):
    INDEX = 3
    BASE_INDEX = 53


class Om7GasMiner4(Om7Member, Om7BaseKusariGasMiner):
    INDEX = 4
    BASE_INDEX = 54


class Om7GasMiner5(Om7Member, Om7BaseRheinlandGasMiner):
    INDEX = 5
    BASE_INDEX = 55


class Om7GasMiner6(Om7Member, Om7BaseRheinlandGasMiner):
    INDEX = 6
    BASE_INDEX = 56


class Om7GasMiner7(Om7Member, Om7BaseRheinlandGasMiner):
    INDEX = 7
    BASE_INDEX = 57


class Om7GasMiner8(Om7Member, Om7BaseRheinlandGasMiner):
    INDEX = 8
    BASE_INDEX = 58


class Om7GasMiner9(Om7Member, Om7BaseRheinlandGasMiner):
    INDEX = 9
    BASE_INDEX = 59


class Om7SimpleCrystalRewards(Om7Member, mineable.DefaultGasCrystalRewardsGroup):
    NAME = 'Om7_gascryst_simple1'
    SOLAR = gas_crystal.SimpleCrystalAsteroid
    REWARD_ITEM = 'comm_gas_balloons'
    ULTRA_REWARD_BASES = [
        Om7GasMiner1,
        Om7GasMiner2,
        Om7GasMiner3,
        Om7GasMiner4,
        Om7GasMiner5,
        Om7GasMiner6,
        Om7GasMiner7,
        Om7GasMiner8,
        Om7GasMiner9,
    ]


class Om7SimpleCrystalField(mineable.DefaultField):
    BOX_SIZE = 1000
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.4
    DRIFT_Y = 0.4
    DRIFT_Z = 0.4
    EMPTY_CHANCE = 0.3


class Om7BaseSimpleGasCrystalField(mineable.GasCrystalRewardField):
    FIELD_CLASS = Om7SimpleCrystalField
    REWARDS_GROUP_CLASS = Om7SimpleCrystalRewards
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class Om7SimpleGasCrystalField1(Om7Member, Om7BaseSimpleGasCrystalField):
    INDEX = 1
    ULTRA_BASE = Om7GasMiner1


class Om7SimpleGasCrystalField2(Om7Member, Om7BaseSimpleGasCrystalField):
    INDEX = 2
    ULTRA_BASE = Om7GasMiner2


class Om7SimpleGasCrystalField3(Om7Member, Om7BaseSimpleGasCrystalField):
    INDEX = 3
    ULTRA_BASE = Om7GasMiner3


class Om7SimpleGasCrystalField4(Om7Member, Om7BaseSimpleGasCrystalField):
    INDEX = 4
    ULTRA_BASE = Om7GasMiner4


class Om7SimpleGasCrystalField5(Om7Member, Om7BaseSimpleGasCrystalField):
    INDEX = 5
    ULTRA_BASE = Om7GasMiner5


class Om7SimpleGasCrystalField6(Om7Member, Om7BaseSimpleGasCrystalField):
    INDEX = 6
    ULTRA_BASE = Om7GasMiner6


class Om7SimpleGasCrystalField7(Om7Member, Om7BaseSimpleGasCrystalField):
    INDEX = 7
    ULTRA_BASE = Om7GasMiner7


class Om7SimpleGasCrystalField8(Om7Member, Om7BaseSimpleGasCrystalField):
    INDEX = 8
    ULTRA_BASE = Om7GasMiner8


class Om7SimpleGasCrystalField9(Om7Member, Om7BaseSimpleGasCrystalField):
    INDEX = 9
    ULTRA_BASE = Om7GasMiner9


class Om7AbandonedMiner1(Om7Member, Om7Rheinland, Om7BaseAbandonedMiner):
    INDEX = 1
    BASE_INDEX = 61
    ASTEROID_ZONES = [
        Om7GasPocketsZone1
    ]


class Om7AbandonedMiner2(Om7Member, Om7Kusari, Om7BaseAbandonedMiner):
    INDEX = 2
    BASE_INDEX = 62
    ASTEROID_ZONES = [
        Om7GasPocketsZone2
    ]


class Om7AbandonedMiner3(Om7Member, Om7Kusari, Om7BaseAbandonedMiner):
    INDEX = 3
    BASE_INDEX = 63
    ASTEROID_ZONES = [
        Om7GasPocketsZone3
    ]


class Om7ComplexCrystalRewards(Om7Member, mineable.DefaultGasCrystalRewardsGroup):
    NAME = 'Om7_gascryst_complex1'
    SOLAR = gas_crystal.ComplexCrystalAsteroid
    REWARD_ITEM = 'comm_gas_balloons'
    ULTRA_REWARD_BASES = [
        Om7AbandonedMiner1,
        Om7AbandonedMiner2,
        Om7AbandonedMiner3,
    ]


class Om7ComplexCrystalField(mineable.DefaultField):
    BOX_SIZE = 1400
    DENSITY_MULTIPLER = 1
    DRIFT_X = 0.3
    DRIFT_Y = 0.5
    DRIFT_Z = 0.3


class Om7BaseComplexGasCrystalField(mineable.ComplexGasCrystalRewardField):
    FIELD_CLASS = Om7ComplexCrystalField
    REWARDS_GROUP_CLASS = Om7ComplexCrystalRewards
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class ComplexGasCrystalField1(Om7Member, Om7BaseComplexGasCrystalField):
    INDEX = 1
    ULTRA_BASE = Om7AbandonedMiner1


class ComplexGasCrystalField2(Om7Member, Om7BaseComplexGasCrystalField):
    INDEX = 2
    ULTRA_BASE = Om7AbandonedMiner2


class ComplexGasCrystalField3(Om7Member, Om7BaseComplexGasCrystalField):
    INDEX = 3
    ULTRA_BASE = Om7AbandonedMiner3


class Om7BaseRheinlandLockedBattleship(main_objects.LockedBattleship):
    ALIAS = 'pocket'
    ARCHETYPE = 'suprise_rh_battleship'
    INTERIOR_CLASS = interior.EquipDeckInterior
    AST_EXCLUSION_ZONE_SIZE = 600


class Om7BaseKusariLockedBattleship(main_objects.LockedBattleship):
    ALIAS = 'pocket'
    ARCHETYPE = 'suprise_ku_battleship'
    INTERIOR_CLASS = interior.EquipDeckInterior
    AST_EXCLUSION_ZONE_SIZE = 600
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_KU


class Om7BaseBattlePockets(zones.AsteroidZone):
    ALIAS = 'pocket'
    ASTEROID_DEFINITION_CLASS = Om7GasPockets
    SPACEDUST = Dust.RADIOACTIVE_RED
    SPACEDUST_MAXPARTICLES = 200


class Om7BattlePocketsZone1(Om7Member, Om7BaseBattlePockets):
    INDEX = 1


class Om7BattlePocketsZone2(Om7Member, Om7BaseBattlePockets):
    INDEX = 2


class Om7BattlePocketsZone3(Om7Member, Om7BaseBattlePockets):
    INDEX = 3


class Om7BattlePocketsZone4(Om7Member, Om7BaseBattlePockets):
    INDEX = 4


class Om7BattleRuins1(Om7Member, Om7BaseKusariLockedBattleship):
    INDEX = 1
    BASE_INDEX = 72

    ASTEROID_ZONES = [
        Om7BattlePocketsZone1,
    ]


class Om7BattleRuins2(Om7Member, Om7BaseKusariLockedBattleship):
    INDEX = 2
    BASE_INDEX = 73

    ASTEROID_ZONES = [
        Om7BattlePocketsZone2,
    ]


class Om7BattleRuins3(Om7Member, Om7BaseKusariLockedBattleship):
    INDEX = 3
    BASE_INDEX = 74

    ASTEROID_ZONES = [
        Om7BattlePocketsZone3,
    ]


class Om7BattleRuins4(Om7Member, Om7BaseRheinlandLockedBattleship):
    INDEX = 4
    BASE_INDEX = 75

    ASTEROID_ZONES = [
        Om7BattlePocketsZone4,
    ]


class Om7KusariSupriseRewards(Om7Member, mineable.DefaultSupriseRewardsGroup):
    NAME = 'om7_kusari_suprise'
    SOLAR = suprise.KusariMainFighter
    REWARD_ITEM = None
    ULTRA_REWARD_BASES = [
        Om7BattleRuins1,
        Om7BattleRuins2,
        Om7BattleRuins3,
    ]


class Om7RheinlandSupriseRewards(Om7Member, mineable.DefaultSupriseRewardsGroup):
    NAME = 'om7_rheinland_suprise'
    SOLAR = suprise.RheinlandMainFighter
    REWARD_ITEM = None
    ULTRA_REWARD_BASES = [
        Om7BattleRuins4,
    ]


class Om7BattleSupriseField(mineable.DefaultField):
    BOX_SIZE = 400
    DENSITY_MULTIPLER = 4
    DRIFT_X = 0.5
    DRIFT_Y = 0.5
    DRIFT_Z = 0.5
    EMPTY_CHANCE = 0.2


class Om7BaseKusariSupriseField(mineable.SupriseRewardField):
    ALIAS = 'pocket'
    FIELD_CLASS = Om7BattleSupriseField
    REWARDS_GROUP_CLASS = Om7KusariSupriseRewards
    ULTRA_REWARD = True


class Om7BaseRheinlandSupriseField(mineable.SupriseRewardField):
    ALIAS = 'pocket'
    FIELD_CLASS = Om7BattleSupriseField
    REWARDS_GROUP_CLASS = Om7RheinlandSupriseRewards
    ULTRA_REWARD = True


class Om7SupriseRewardField1(Om7Member, Om7BaseKusariSupriseField):
    INDEX = 1
    ULTRA_BASE = Om7BattleRuins1


class Om7SupriseRewardField2(Om7Member, Om7BaseKusariSupriseField):
    INDEX = 2
    ULTRA_BASE = Om7BattleRuins2


class Om7SupriseRewardField3(Om7Member, Om7BaseKusariSupriseField):
    INDEX = 3
    ULTRA_BASE = Om7BattleRuins3


class Om7SupriseRewardField4(Om7Member, Om7BaseRheinlandSupriseField):
    INDEX = 4
    ULTRA_BASE = Om7BattleRuins4
