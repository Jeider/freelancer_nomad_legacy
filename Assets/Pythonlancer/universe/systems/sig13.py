from fx.space import Dust
from fx.sound import Ambience

from managers.tools import query as Q
from world.names import *
from universe.content import meta

from universe import markets

from universe.content.member import Member
from universe.content.system_object import TOP, BOTTOM, LEFT, RIGHT
from universe.content import main_objects
from universe.content import zones
from universe.content import asteroid_definition
from universe.content import interior
from universe.content import dealers
from universe import faction
from universe.content import population
from universe.content import mineable

from templates.dockable import gas_miner
from templates.dockable import trade_storages

from templates.nebula import exclusion
from templates.nebula import sig13_blue_nebula
from templates.solar import gas_crystal


class Sig13Member(Member):
    FACTION = faction.RheinlandMain
    WEAPON_FACTION = WEAPON_RH
    EQUIP_FACTION = EQUIP_RH


class Sig13Rheinland(object):
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_RH
    FACTION = faction.RheinlandMain
    WEAPON_FACTION = WEAPON_RH
    EQUIP_FACTION = EQUIP_RH


class Sig13Liberty(object):
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_LI
    POPULATION_KIND = population.POP_SECOND
    FACTION = faction.LibertyMain
    WEAPON_FACTION = WEAPON_LI
    EQUIP_FACTION = EQUIP_LI


class Sig13StaticText(Sig13Member, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = sig13
space_color = 0, 0, 0
local_faction = rh_grp

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Dust]
spacedust = Dust

[Music]
space = music_sigma_space
danger = music_sigma_danger
battle = music_sigma_battle

[Ambient]
color = 20, 20, 40

[Background]
basic_stars = solar\\stars_mod\\new_generic.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_sig13_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
property_flags = 2048

[LightSource]
nickname = sig13_system_light
pos = -31, 0, -48
color = 120, 250, 255
range = 60000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION

'''

CROW_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.CROW_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '255, 255, 200',
    'fog_far': 5000,
}


GENERIC_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.GENERIC_EXCLUSION,
    'shell_scalar': 1,
    'max_alpha': 0.6,
    'exclusion_tint': '20, 150, 255',
    'fog_far': 5000,
}


ICE_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.ICE_EXCLUSION,
    'shell_scalar': 1,
    'max_alpha': 0.8,
    'exclusion_tint': '20, 180, 255',
    'fog_far': 5000,
}


class Sig13Nebula(Sig13Member, zones.NebulaZone):
    INDEX = 1
    SPACEDUST = Dust.ATTRACT
    SPACEDUST_MAXPARTICLES = 50
    MUSIC = Ambience.NEBULA_CROW
    CONTENT_TEMPLATE = sig13_blue_nebula.Sig13BlueNebulaTemplate
    INTERFERENCE = 0.5

    PROPERTY_FLAGS = 32768
    PROPERTY_FOG_COLOR = '0.000000, 100.000000, 160.000000'


class Sig13Sun(Sig13Member, main_objects.SunSmall):
    STAR = 'med_blue_sun'


class Sig13ForbesJumpgate(Sig13Member, main_objects.Jumpgate):
    INDEX = 1
    REL = TOP
    TARGET_SYSTEM_NAME = 'li_for'


class Sig13CaliforniaJumpgate(Sig13Member, main_objects.Jumpgate):
    INDEX = 2
    REL = LEFT
    TARGET_SYSTEM_NAME = 'li_cal'


class Sig13BerlinJumpgate(Sig13Member, main_objects.Jumpgate):
    INDEX = 3
    REL = BOTTOM
    TARGET_SYSTEM_NAME = 'rh_ber'


class Sig13LibertyStation(Sig13Liberty, Sig13Member, main_objects.GasMiningStation):
    INDEX = 1
    BASE_INDEX = 2
    REL = RIGHT
    REL_DRIFT = 0
    REL_APPEND = 1000
    ARCHETYPE = 'smallstation1_old'
    LOADOUT = 'smallstation_li'
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.LibertyCivilianDealers

    NEBULA_EXCLUSION_ZONE_SIZE = 5000
    EXCLUSION_PARAMS = GENERIC_EXCLUSION_PARAMS
    NEBULA_ZONES = [Sig13Nebula]
    INTERIOR_BG1 = interior.INTERIOR_BG_CROW


class Sig13RheinlandStation(Sig13Member, Sig13Rheinland, main_objects.GasMiningStation):
    INDEX = 2
    BASE_INDEX = 1
    REL = RIGHT
    REL_APPEND = 1500
    SPACE_OBJECT_TEMPLATE = gas_miner.RheinlandCivilianGasMiner
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.RheinlandCivilianDealers

    NEBULA_EXCLUSION_ZONE_SIZE = 3000
    EXCLUSION_PARAMS = GENERIC_EXCLUSION_PARAMS
    NEBULA_ZONES = [Sig13Nebula]
    INTERIOR_BG1 = interior.INTERIOR_BG_CROW


class Sig13Battleship(Sig13Member, Sig13Rheinland, main_objects.RheinlandBattleship):
    BASE_INDEX = 4
    REL = RIGHT
    REL_APPEND = 1000
    REL_DRIFT = 1500
    INTERIOR_CLASS = interior.BattleshipInterior
    DEALERS = dealers.RheinlandMilitaryDealers
    SHIP_SET = markets.ShipSet('rh_elite')

    NEBULA_EXCLUSION_ZONE_SIZE = 2000
    EXCLUSION_PARAMS = CROW_EXCLUSION_PARAMS
    NEBULA_ZONES = [Sig13Nebula]
    INTERIOR_BG1 = interior.INTERIOR_BG_CROW


class Sig13Freeport(Sig13Liberty, Sig13Member, main_objects.Freeport):
    BASE_INDEX = 5
    REL = LEFT
    REL_APPEND = 1000
    SPACE_OBJECT_TEMPLATE = trade_storages.HonshuStorage
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.RheinlandCivilianDealers
    ROTATE_RANDOM = True

    NEBULA_EXCLUSION_ZONE_SIZE = 2000
    EXCLUSION_PARAMS = GENERIC_EXCLUSION_PARAMS
    NEBULA_ZONES = [Sig13Nebula]
    INTERIOR_BG1 = interior.INTERIOR_BG_CROW


class Sig13PirateTopRight(Sig13Liberty, Sig13Member, main_objects.PirateGasMiner):
    BASE_INDEX = 6
    INDEX = 1
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = gas_miner.CadizGasMiner
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.LibertyPirateDealers
    FACTION = faction.LibertyPirate
    DEFENCE_LEVEL = None

    NEBULA_EXCLUSION_ZONE_SIZE = 2000
    EXCLUSION_PARAMS = CROW_EXCLUSION_PARAMS
    NEBULA_ZONES = [Sig13Nebula]
    INTERIOR_BG1 = interior.INTERIOR_BG_CROW


class Sig13PirateTopLeft(Sig13Liberty, Sig13Member, main_objects.PirateGasMiner):
    BASE_INDEX = 7
    INDEX = 2
    REL = TOP
    SPACE_OBJECT_TEMPLATE = gas_miner.RheinlandPirateGasMiner
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.LibertyPirateDealers
    FACTION = faction.LibertyPirate
    DEFENCE_LEVEL = None

    NEBULA_EXCLUSION_ZONE_SIZE = 2000
    EXCLUSION_PARAMS = CROW_EXCLUSION_PARAMS
    NEBULA_ZONES = [Sig13Nebula]
    INTERIOR_BG1 = interior.INTERIOR_BG_CROW


class Sig13PirateBottom(Sig13Member, Sig13Rheinland, main_objects.PirateGasMiner):
    BASE_INDEX = 8
    INDEX = 3
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = gas_miner.BretoniaPirateGasMiner
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.RheinlandPirateDealers
    FACTION = faction.RheinlandPirate
    DEFENCE_LEVEL = None

    NEBULA_EXCLUSION_ZONE_SIZE = 2000
    EXCLUSION_PARAMS = CROW_EXCLUSION_PARAMS
    NEBULA_ZONES = [Sig13Nebula]
    INTERIOR_BG1 = interior.INTERIOR_BG_CROW


class Sig13ConnRheinlandGas1(Sig13Member, main_objects.TradeConnection):
    OBJ_FROM = Sig13RheinlandStation
    OBJ_TO = Sig13CaliforniaJumpgate
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        Sig13PirateBottom,
    ]
    REL_APPEND = 0
    REL_DRIFT = 5000

    OBJ_FROM_EXTRA_DRIFT = -1000
    # OBJ_FROM_EXTRA_DRIFT_ALT_AXIS = 3000
    # OBJ_TO_EXTRA_DRIFT = 1000
    # OBJ_TO_EXTRA_DRIFT_ALT_AXIS = -2000


class Sig13ConnRheinlandGas2(Sig13Member, main_objects.TradeConnection):
    OBJ_FROM = Sig13RheinlandStation
    OBJ_TO = Sig13BerlinJumpgate
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        Sig13PirateBottom,
    ]


class Sig13ConnLibertyGas1(Sig13Liberty, Sig13Member, main_objects.TradeConnection):
    OBJ_FROM = Sig13LibertyStation
    OBJ_TO = Sig13CaliforniaJumpgate
    SIDE_FROM = TOP
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        Sig13PirateTopLeft,
    ]

    OBJ_FROM_EXTRA_DRIFT = -3000
    OBJ_FROM_EXTRA_DRIFT_ALT_AXIS = -2000
    OBJ_TO_EXTRA_DRIFT = 1000
    OBJ_TO_EXTRA_DRIFT_ALT_AXIS = -2000


class Sig13ConnLibertyGas2(Sig13Liberty, Sig13Member, main_objects.TradeConnection):
    OBJ_FROM = Sig13LibertyStation
    OBJ_TO = Sig13ForbesJumpgate
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        Sig13PirateTopLeft,
    ]


class Sig13ConnBattleship1(Sig13Member, main_objects.TradeConnection):
    OBJ_FROM = Sig13Battleship
    OBJ_TO = Sig13BerlinJumpgate
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        # BerlinPiratesTop
    ]


class Sig13ConnBattleship2(Sig13Member, main_objects.TradeConnection):
    OBJ_FROM = Sig13Battleship
    OBJ_TO = Sig13Freeport
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'F'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        Sig13PirateTopRight,
    ]


class Sig13ConnFreeport1(Sig13Liberty, Sig13Member, main_objects.TradeConnection):
    OBJ_FROM = Sig13Freeport
    OBJ_TO = Sig13ForbesJumpgate
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'G'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        Sig13PirateTopRight,
    ]


class Sig13BaseLibertyGasMiner(Sig13Liberty, main_objects.GasMinerOld):
    ALIAS = 'cryst'
    ROTATE_RANDOM = True
    ARCHETYPE = 'gas_miner_old'
    LOADOUT = 'gas_miner_old_li'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    NEBULA_EXCLUSION_ZONE_SIZE = 3000
    EXCLUSION_PARAMS = CROW_EXCLUSION_PARAMS
    NEBULA_ZONES = [Sig13Nebula]
    INTERIOR_BG1 = interior.INTERIOR_BG_CROW
    NEBULA_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.ICE,
        'spacedust_maxparticles': 200,
    }


class Sig13BaseRheinlandGasMiner(Sig13Rheinland, main_objects.GasMinerOld):
    ALIAS = 'cryst'
    ROTATE_RANDOM = True
    ARCHETYPE = 'gas_miner_old'
    LOADOUT = 'gas_miner_old_rh'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    NEBULA_EXCLUSION_ZONE_SIZE = 3000
    EXCLUSION_PARAMS = CROW_EXCLUSION_PARAMS
    NEBULA_ZONES = [Sig13Nebula]
    INTERIOR_BG1 = interior.INTERIOR_BG_CROW
    NEBULA_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.ICE,
        'spacedust_maxparticles': 200,
    }


class Sig13BaseAbandonedMiner(main_objects.AbandonedAsteroidIce):
    ALIAS = 'bigcryst'
    ROTATE_RANDOM = True
    ARCHETYPE = 'miningbase_ice_block'
    # LOADOUT = 'miningbase_ice_block_pi_01'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    NEBULA_EXCLUSION_ZONE_SIZE = 8500
    AST_EXCLUSION_ZONE_SIZE = 2000
    EXCLUSION_PARAMS = CROW_EXCLUSION_PARAMS
    NEBULA_ZONES = [Sig13Nebula]
    INTERIOR_BG1 = interior.INTERIOR_BG_CROW
    AST_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.ICE,
        'spacedust_maxparticles': 200,
    }


FIELD_TEMPLATE = '''
cube_size = 400
fill_dist = 1500
diffuse_color = 100, 150, 255
ambient_color = 100, 200, 255
ambient_increase = 20, 30, 255
empty_cube_frequency = 0.000000
max_alpha = 0.400000
'''

CUBE_TEMPLATE = '''
asteroid = mine_oxygen, 0.800000, -0.500000, -0.200000, 15, 90, 120, mine
asteroid = mine_oxygen, -0.300000, 0.600000, 0.800000, 85, 0, 185, mine
asteroid = mine_oxygen, 0.400000, -0.700000, -0.200000, 15, 90, 120, mine
asteroid = mine_oxygen, -0.300000, -0.300000, 0.800000, 85, 0, 185, mine
asteroid = mine_oxygen, -0.700000, 0.400000, -0.400000, 75, 30, 70, mine
'''


class Sig13GasPockets(asteroid_definition.AsteroidDefinition):
    FIELD = True
    CUBE = True
    FIELD_TEMPLATE = FIELD_TEMPLATE
    CUBE_TEMPLATE = CUBE_TEMPLATE


class Sig13GasPocketsZone1(Sig13Member, zones.AsteroidZone):
    ALIAS = 'bigcryst'
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = Sig13GasPockets
    SPACEDUST = Dust.OXYGEN
    SPACEDUST_MAXPARTICLES = 200


class Sig13GasPocketsZone2(Sig13Member, zones.AsteroidZone):
    ALIAS = 'bigcryst'
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = Sig13GasPockets
    SPACEDUST = Dust.OXYGEN
    SPACEDUST_MAXPARTICLES = 200


class Sig13GasPocketsZone3(Sig13Member, zones.AsteroidZone):
    ALIAS = 'bigcryst'
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = Sig13GasPockets
    SPACEDUST = Dust.OXYGEN
    SPACEDUST_MAXPARTICLES = 200


class Sig13GasMiner1(Sig13Member, Sig13BaseRheinlandGasMiner):
    INDEX = 1
    BASE_INDEX = 51


class Sig13GasMiner2(Sig13Member, Sig13BaseRheinlandGasMiner):
    INDEX = 2
    BASE_INDEX = 52


class Sig13GasMiner3(Sig13Member, Sig13BaseLibertyGasMiner):
    INDEX = 3
    BASE_INDEX = 53


class Sig13GasMiner4(Sig13Member, Sig13BaseRheinlandGasMiner):
    INDEX = 4
    BASE_INDEX = 54


class Sig13GasMiner5(Sig13Member, Sig13BaseRheinlandGasMiner):
    INDEX = 5
    BASE_INDEX = 55


class Sig13GasMiner6(Sig13Member, Sig13BaseRheinlandGasMiner):
    INDEX = 6
    BASE_INDEX = 56


class Sig13GasMiner7(Sig13Member, Sig13BaseLibertyGasMiner):
    INDEX = 7
    BASE_INDEX = 57


class Sig13GasMiner8(Sig13Member, Sig13BaseLibertyGasMiner):
    INDEX = 8
    BASE_INDEX = 58


class Sig13GasMiner9(Sig13Member, Sig13BaseLibertyGasMiner):
    INDEX = 9
    BASE_INDEX = 59


class Sig13SimpleCrystalRewards(Sig13Member, mineable.DefaultGasCrystalRewardsGroup):
    NAME = 'sig13_gascryst_simple1'
    SOLAR = gas_crystal.SimpleCrystalAsteroid
    REWARD_ITEM = 'comm_gas_balloons'
    ULTRA_REWARD_BASES = [
        Sig13GasMiner1,
        Sig13GasMiner2,
        Sig13GasMiner3,
        Sig13GasMiner4,
        Sig13GasMiner5,
        Sig13GasMiner6,
        Sig13GasMiner7,
        Sig13GasMiner8,
        Sig13GasMiner9,
    ]


class Sig13SimpleCrystalField(mineable.DefaultField):
    BOX_SIZE = 1000
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.4
    DRIFT_Y = 0.4
    DRIFT_Z = 0.4
    EMPTY_CHANCE = 0.3


class Sig13BaseSimpleGasCrystalField(mineable.GasCrystalRewardField):
    FIELD_CLASS = Sig13SimpleCrystalField
    REWARDS_GROUP_CLASS = Sig13SimpleCrystalRewards
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class Sig13SimpleGasCrystalField1(Sig13Member, Sig13BaseSimpleGasCrystalField):
    INDEX = 1
    ULTRA_BASE = Sig13GasMiner1


class Sig13SimpleGasCrystalField2(Sig13Member, Sig13BaseSimpleGasCrystalField):
    INDEX = 2
    ULTRA_BASE = Sig13GasMiner2


class Sig13SimpleGasCrystalField3(Sig13Member, Sig13BaseSimpleGasCrystalField):
    INDEX = 3
    ULTRA_BASE = Sig13GasMiner3


class Sig13SimpleGasCrystalField4(Sig13Member, Sig13BaseSimpleGasCrystalField):
    INDEX = 4
    ULTRA_BASE = Sig13GasMiner4


class Sig13SimpleGasCrystalField5(Sig13Member, Sig13BaseSimpleGasCrystalField):
    INDEX = 5
    ULTRA_BASE = Sig13GasMiner5


class Sig13SimpleGasCrystalField6(Sig13Member, Sig13BaseSimpleGasCrystalField):
    INDEX = 6
    ULTRA_BASE = Sig13GasMiner6


class Sig13SimpleGasCrystalField7(Sig13Member, Sig13BaseSimpleGasCrystalField):
    INDEX = 7
    ULTRA_BASE = Sig13GasMiner7


class Sig13SimpleGasCrystalField8(Sig13Member, Sig13BaseSimpleGasCrystalField):
    INDEX = 8
    ULTRA_BASE = Sig13GasMiner8


class Sig13SimpleGasCrystalField9(Sig13Member, Sig13BaseSimpleGasCrystalField):
    INDEX = 9
    ULTRA_BASE = Sig13GasMiner9


class Sig13AbandonedMiner1(Sig13Member, Sig13Rheinland, Sig13BaseAbandonedMiner):
    INDEX = 1
    BASE_INDEX = 60
    ASTEROID_ZONES = [
        Sig13GasPocketsZone1
    ]


class Sig13AbandonedMiner2(Sig13Member, Sig13Rheinland, Sig13BaseAbandonedMiner):
    INDEX = 2
    BASE_INDEX = 61
    ASTEROID_ZONES = [
        Sig13GasPocketsZone2
    ]


class Sig13AbandonedMiner3(Sig13Liberty, Sig13Member, Sig13BaseAbandonedMiner):
    INDEX = 3
    BASE_INDEX = 62
    ASTEROID_ZONES = [
        Sig13GasPocketsZone3
    ]


class Sig13ComplexCrystalRewards(Sig13Member, mineable.DefaultGasCrystalRewardsGroup):
    NAME = 'sig13_gascryst_complex1'
    SOLAR = gas_crystal.ComplexCrystalAsteroid
    REWARD_ITEM = 'comm_gas_balloons'
    ULTRA_REWARD_BASES = [
        Sig13AbandonedMiner1,
        Sig13AbandonedMiner2,
        Sig13AbandonedMiner3,
    ]


class Sig13ComplexCrystalField(mineable.DefaultField):
    BOX_SIZE = 1400
    DENSITY_MULTIPLER = 1
    DRIFT_X = 0.3
    DRIFT_Y = 0.5
    DRIFT_Z = 0.3


class Sig13BaseComplexGasCrystalField(mineable.ComplexGasCrystalRewardField):
    FIELD_CLASS = Sig13ComplexCrystalField
    REWARDS_GROUP_CLASS = Sig13ComplexCrystalRewards
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class ComplexGasCrystalField1(Sig13Member, Sig13BaseComplexGasCrystalField):
    INDEX = 1
    ULTRA_BASE = Sig13AbandonedMiner1


class ComplexGasCrystalField2(Sig13Member, Sig13BaseComplexGasCrystalField):
    INDEX = 2
    ULTRA_BASE = Sig13AbandonedMiner2


class ComplexGasCrystalField3(Sig13Member, Sig13BaseComplexGasCrystalField):
    INDEX = 3
    ULTRA_BASE = Sig13AbandonedMiner3
