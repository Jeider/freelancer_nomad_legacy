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
from universe.content import mineable
from universe.content import population

from templates.nebula import exclusion
from templates.nebula import tau23_nebula
from templates.solar import gas_crystal

from templates.dockable import gas_miner
from templates.dockable import trade_storages

from text.strings import MultiString as MS


class Tau23Member(Member):
    FACTION = faction.BretoniaMain
    INTERIOR_BG1 = interior.INTERIOR_BG_BARRIER_CLOUD
    WEAPON_FACTION = WEAPON_BR
    EQUIP_FACTION = EQUIP_BR


class Tau23Bretonia(object):
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_BR
    FACTION = faction.BretoniaMain
    WEAPON_FACTION = WEAPON_BR
    EQUIP_FACTION = EQUIP_BR


class Tau23Kusari(object):
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_KU
    POPULATION_KIND = population.POP_SECOND
    FACTION = faction.KusariMain
    WEAPON_FACTION = WEAPON_KU
    EQUIP_FACTION = EQUIP_KU


class Tau23StaticText(Tau23Member, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = tau23
space_color = 0, 0, 0
local_faction = br_grp

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Dust]
spacedust = Dust

[Music]
space = music_tau_space
danger = music_tau_danger
battle = music_tau_battle

[Ambient]
color = 0, 0, 0

[Background]
nebulae = solar\\stars_mod\\white_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_tau23_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
;property_flags = 512 ;lava - MILITARY
;property_flags = 256 ;ice - TRADING
property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = Light_System_tau23
pos = 0, 0, 0
color = 225, 255, 225
range = 100000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION
'''


class Tau23Nebula(Tau23Member, zones.NebulaZone):
    INDEX = 1
    MUSIC = Ambience.NEBULA_BARRIER
    CONTENT_TEMPLATE = tau23_nebula.Tau23MainNebulaTemplate
    INTERFERENCE = 0.5


BARRIER_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.ICE_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '120, 125, 130',
    'fog_far': 5000,
}


class Tau23Sun(Tau23Member, main_objects.SunSmall):
    STAR = 'ku03_Sun2'


class Tau23AvalonJumpgate(Tau23Member, main_objects.Jumpgate):
    INDEX = 1
    REL = TOP
    TARGET_SYSTEM_NAME = 'br_avl'


class Tau23KyushuJumpgate(Tau23Member, main_objects.Jumpgate):
    INDEX = 2
    REL = BOTTOM
    TARGET_SYSTEM_NAME = 'ku_ksu'


class Tau23BretoniaStation(Tau23Member, Tau23Bretonia, main_objects.GasMiningStation):
    INDEX = 1
    BASE_INDEX = 1
    REL = LEFT
    REL_APPEND = 2000
    SPACE_OBJECT_TEMPLATE = gas_miner.BretoniaCivilianGasMiner
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.BretoniaCivilianDealers
    RU_NAME = MS('Станция +Эдинбург', 'Station Edinburgh')

    NEBULA_EXCLUSION_ZONE_SIZE = 5000
    EXCLUSION_PARAMS = BARRIER_EXCLUSION_PARAMS
    NEBULA_ZONES = [Tau23Nebula]

    BASE_PROPS = meta.GasMiningStation(
        objectives=[
            meta.HaveGreenhouse(),
            meta.HaveReactor(),
        ]
    )


class Tau23KusariStation(Tau23Kusari, Tau23Member, main_objects.GasMiningStation):
    INDEX = 2
    BASE_INDEX = 2
    REL = LEFT
    REL_DRIFT = 0
    REL_APPEND = 2000
    ARCHETYPE = 'smallstation1_old'
    LOADOUT = 'smallstation_ku'
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.KusariCivilianDealers
    RU_NAME = MS('Станция Сибуя', "Shibuya Base")

    NEBULA_EXCLUSION_ZONE_SIZE = 5000
    EXCLUSION_PARAMS = BARRIER_EXCLUSION_PARAMS
    NEBULA_ZONES = [Tau23Nebula]


class Tau23BretoniaBattleship(Tau23Member, Tau23Bretonia, main_objects.BretoniaBattleship):
    INDEX = 1
    BASE_INDEX = 3
    REL = RIGHT
    REL_APPEND = 1000
    REL_DRIFT = 500
    INTERIOR_CLASS = interior.BattleshipInterior
    DEALERS = dealers.BretoniaMilitaryDealers
    SHIP_SET = markets.ShipSet('br_elite')
    RU_NAME = MS('Линкор Авангард', 'Battleship Vanguard')

    NEBULA_EXCLUSION_ZONE_SIZE = 2000
    EXCLUSION_PARAMS = BARRIER_EXCLUSION_PARAMS
    NEBULA_ZONES = [Tau23Nebula]


class Tau23KusariBattleship(Tau23Kusari, Tau23Member, main_objects.KusariBattleship):
    INDEX = 2
    BASE_INDEX = 4
    REL = LEFT
    REL_APPEND = 1000
    REL_DRIFT = 500
    INTERIOR_CLASS = interior.BattleshipInterior
    DEALERS = dealers.KusariMilitaryDealers
    SHIP_SET = markets.ShipSet('ku_fighter')
    RU_NAME = MS('Линкор Кирисима', 'Battleship Kirishima')

    NEBULA_EXCLUSION_ZONE_SIZE = 2000
    EXCLUSION_PARAMS = BARRIER_EXCLUSION_PARAMS
    NEBULA_ZONES = [Tau23Nebula]


class Tau23Freeport(Tau23Member, Tau23Bretonia, main_objects.Freeport):
    INDEX = 1
    BASE_INDEX = 5
    REL = RIGHT
    REL_APPEND = 2000
    SPACE_OBJECT_TEMPLATE = trade_storages.ManhattanStorage
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.BretoniaCivilianDealers
    RU_NAME = MS('Фрипорт Кельтик', 'Freeport Celtic')

    NEBULA_EXCLUSION_ZONE_SIZE = 3500
    EXCLUSION_PARAMS = BARRIER_EXCLUSION_PARAMS
    NEBULA_ZONES = [Tau23Nebula]


class Tau23TopRightPirates(Tau23Member, Tau23Bretonia, main_objects.PirateGasMiner):
    INDEX = 1
    BASE_INDEX = 6
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = gas_miner.RheinlandPirateGasMiner
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.BretoniaPirateDealers
    FACTION = faction.Xenos
    DEFENCE_LEVEL = None
    RU_NAME = MS('База Брест', "Brest Base")

    NEBULA_EXCLUSION_ZONE_SIZE = 2000
    EXCLUSION_PARAMS = BARRIER_EXCLUSION_PARAMS
    NEBULA_ZONES = [Tau23Nebula]


class Tau23BottomLeftPirates(Tau23Kusari, Tau23Member, main_objects.PirateGasMiner):
    INDEX = 2
    BASE_INDEX = 7
    REL = LEFT
    SPACE_OBJECT_TEMPLATE = gas_miner.BretoniaPirateGasMiner
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.KusariPirateDealers
    FACTION = faction.FarmerAlliance
    DEFENCE_LEVEL = None
    RU_NAME = MS('База Кога', 'Koga Base')

    NEBULA_EXCLUSION_ZONE_SIZE = 2000
    EXCLUSION_PARAMS = BARRIER_EXCLUSION_PARAMS
    NEBULA_ZONES = [Tau23Nebula]


class Tau23BretoniaStationConn1(Tau23Member, Tau23Bretonia, main_objects.TradeConnection):
    OBJ_FROM = Tau23BretoniaStation
    OBJ_TO = Tau23AvalonJumpgate
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        Tau23TopRightPirates
    ]


class Tau23BretoniaStationConn2(Tau23Member, Tau23Bretonia, main_objects.TradeConnection):
    OBJ_FROM = Tau23BretoniaStation
    OBJ_TO = Tau23Freeport
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        Tau23TopRightPirates
    ]


class Tau23BretoniaBattleshipConn1(Tau23Member, Tau23Bretonia, main_objects.TradeConnection):
    OBJ_FROM = Tau23BretoniaBattleship
    OBJ_TO = Tau23Freeport
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        Tau23TopRightPirates
    ]


class Tau23KusariStationConn1(Tau23Kusari, Tau23Member, main_objects.TradeConnection):
    OBJ_FROM = Tau23KusariStation
    OBJ_TO = Tau23Freeport
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        Tau23BottomLeftPirates
    ]


class Tau23KusariStationConn2(Tau23Kusari, Tau23Member, main_objects.TradeConnection):
    OBJ_FROM = Tau23KusariStation
    OBJ_TO = Tau23KyushuJumpgate
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        Tau23BottomLeftPirates
    ]


class Tau23KusariStationConn3(Tau23Kusari, Tau23Member, main_objects.TradeConnection):
    OBJ_FROM = Tau23KusariStation
    OBJ_TO = Tau23KusariBattleship
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'F'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        Tau23BottomLeftPirates
    ]


class Tau23BaseBretoniaGasMiner(Tau23Bretonia, main_objects.GasMinerOld):
    ALIAS = 'cryst'
    ROTATE_RANDOM = True
    ARCHETYPE = 'gas_miner_old'
    LOADOUT = 'gas_miner_old_br'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    NEBULA_EXCLUSION_ZONE_SIZE = 3000
    EXCLUSION_PARAMS = BARRIER_EXCLUSION_PARAMS
    NEBULA_ZONES = [Tau23Nebula]
    NEBULA_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.ICE,
        'spacedust_maxparticles': 200,
    }


class Tau23BaseKusariGasMiner(main_objects.GasMinerOld):
    ALIAS = 'cryst'
    ROTATE_RANDOM = True
    ARCHETYPE = 'gas_miner_old'
    LOADOUT = 'gas_miner_old_ku'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    NEBULA_EXCLUSION_ZONE_SIZE = 3000
    EXCLUSION_PARAMS = BARRIER_EXCLUSION_PARAMS
    NEBULA_ZONES = [Tau23Nebula]
    NEBULA_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.ICE,
        'spacedust_maxparticles': 200,
    }


class Tau23BaseAbandonedMiner(main_objects.AbandonedAsteroidIce):
    ALIAS = 'bigcryst'
    ROTATE_RANDOM = True
    ARCHETYPE = 'miningbase_ice_block'
    # LOADOUT = 'miningbase_ice_block_pi_01'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    NEBULA_EXCLUSION_ZONE_SIZE = 8500
    AST_EXCLUSION_ZONE_SIZE = 2000
    EXCLUSION_PARAMS = BARRIER_EXCLUSION_PARAMS
    NEBULA_ZONES = [Tau23Nebula]
    NEBULA_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.ICE,
        'spacedust_maxparticles': 200,
    }


FIELD_TEMPLATE = '''
cube_size = 400
fill_dist = 1500
diffuse_color = 125, 125, 125
ambient_color = 100, 100, 100
ambient_increase = 50, 50, 50
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


class Tau23GasPockets(asteroid_definition.AsteroidDefinition):
    FIELD = True
    CUBE = True
    FIELD_TEMPLATE = FIELD_TEMPLATE
    CUBE_TEMPLATE = CUBE_TEMPLATE


class Tau23GasPocketsZone1(Tau23Member, zones.AsteroidZone):
    ALIAS = 'bigcryst'
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = Tau23GasPockets
    SPACEDUST = Dust.OXYGEN
    SPACEDUST_MAXPARTICLES = 200


class Tau23GasPocketsZone2(Tau23Member, zones.AsteroidZone):
    ALIAS = 'bigcryst'
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = Tau23GasPockets
    SPACEDUST = Dust.OXYGEN
    SPACEDUST_MAXPARTICLES = 200


class Tau23GasPocketsZone3(Tau23Member, zones.AsteroidZone):
    ALIAS = 'bigcryst'
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = Tau23GasPockets
    SPACEDUST = Dust.OXYGEN
    SPACEDUST_MAXPARTICLES = 200


class Tau23GasMiner1(Tau23Member, Tau23BaseBretoniaGasMiner):
    INDEX = 1
    BASE_INDEX = 51
    RU_NAME = MS('Газодобытчик Эссингтон', 'Gas Miner Essington')
    EQUIP_SET = markets.EquipSet(
        Q.SingleLauncher(CM, eq_classes=markets.CM2),
        Q.Thruster(BR_MAIN, eq_classes=markets.SECRET3),
    )


class Tau23GasMiner2(Tau23Member, Tau23BaseBretoniaGasMiner):
    INDEX = 2
    BASE_INDEX = 52
    RU_NAME = MS('Газодобытчик Косфорд', 'Gas Miner Cosford')
    EQUIP_SET = markets.EquipSet(
        Q.SingleLauncher(CM, eq_classes=markets.CM2),
        Q.Thruster(BR_PIRATE, eq_classes=markets.SECRET3),
    )


class Tau23GasMiner3(Tau23Member, Tau23BaseBretoniaGasMiner):
    INDEX = 3
    BASE_INDEX = 53
    RU_NAME = MS('Газодобытчик Дорридж', 'Gas Miner Dorridge')
    EQUIP_SET = markets.EquipSet(
        Q.SingleLauncher(CM, eq_classes=markets.CM2),
        Q.Thruster(BR_MAIN, eq_classes=markets.SECRET2),
    )


class Tau23GasMiner4(Tau23Member, Tau23BaseBretoniaGasMiner):
    INDEX = 4
    BASE_INDEX = 54
    RU_NAME = MS('Газодобытчик Ширли', 'Gas Miner Shirley')
    EQUIP_SET = markets.EquipSet(
        Q.SingleLauncher(CM, eq_classes=markets.CM3),
        Q.Thruster(BR_PIRATE, eq_classes=markets.SECRET2),
    )


class Tau23GasMiner5(Tau23Member, Tau23BaseBretoniaGasMiner):
    INDEX = 5
    BASE_INDEX = 55
    RU_NAME = MS('Газодобытчик Одлем', 'Gas Miner Alderley Edge')
    EQUIP_SET = markets.EquipSet(
        Q.SingleLauncher(CM, eq_classes=markets.CM2),
        Q.Thruster(BR_MAIN, eq_classes=markets.SECRET2),
    )


class Tau23GasMiner6(Tau23Kusari, Tau23Member, Tau23BaseKusariGasMiner):
    INDEX = 6
    BASE_INDEX = 56
    RU_NAME = MS('Газодобытчик Карацу', "Gas Miner Karatsu")
    EQUIP_SET = markets.EquipSet(
        Q.SingleLauncher(CM, eq_classes=markets.CM3),
        Q.Thruster(KU_MAIN, eq_classes=markets.SECRET2),
    )


class Tau23GasMiner7(Tau23Kusari, Tau23Member, Tau23BaseKusariGasMiner):
    INDEX = 7
    BASE_INDEX = 57
    RU_NAME = MS('Газодобытчик Уресино', "Gas Miner Ureshino")
    EQUIP_SET = markets.EquipSet(
        Q.SingleLauncher(CM, eq_classes=markets.CM2),
        Q.Thruster(KU_MAIN, eq_classes=markets.SECRET3),
    )


class Tau23GasMiner8(Tau23Kusari, Tau23Member, Tau23BaseKusariGasMiner):
    INDEX = 8
    BASE_INDEX = 58
    RU_NAME = MS('Газодобытчик Тамана', 'Gas Miner Tamana')
    EQUIP_SET = markets.EquipSet(
        Q.SingleLauncher(CM, eq_classes=markets.CM3),
        Q.Thruster(KU_PIRATE, eq_classes=markets.SECRET2),
    )


class Tau23GasMiner9(Tau23Kusari, Tau23Member, Tau23BaseKusariGasMiner):
    INDEX = 9
    BASE_INDEX = 59
    RU_NAME = MS('Газодобытчик Такета', "Gas Miner Taketa")
    EQUIP_SET = markets.EquipSet(
        Q.SingleLauncher(CM, eq_classes=markets.CM2),
        Q.Thruster(KU_PIRATE, eq_classes=markets.SECRET3),
    )


class Tau23GasMiner10(Tau23Kusari, Tau23Member, Tau23BaseKusariGasMiner):
    INDEX = 10
    BASE_INDEX = 60
    RU_NAME = MS('Газодобытчик Ямага', "Gas Miner Yamaga")
    EQUIP_SET = markets.EquipSet(
        Q.SingleLauncher(CM, eq_classes=markets.CM3),
        Q.Thruster(KU_MAIN, eq_classes=markets.SECRET2),
    )


class Tau23SimpleCrystalRewards(Tau23Member, mineable.DefaultGasCrystalRewardsGroup):
    NAME = 'Tau23_gascryst_simple1'
    SOLAR = gas_crystal.SimpleCrystalAsteroid
    REWARD_ITEM = 'comm_gas_balloons'
    ULTRA_REWARD_BASES = [
        Tau23GasMiner1,
        Tau23GasMiner2,
        Tau23GasMiner3,
        Tau23GasMiner4,
        Tau23GasMiner5,
        Tau23GasMiner6,
        Tau23GasMiner7,
        Tau23GasMiner8,
        Tau23GasMiner9,
        Tau23GasMiner10,
    ]


class Tau23SimpleCrystalField(mineable.DefaultField):
    BOX_SIZE = 1000
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.4
    DRIFT_Y = 0.4
    DRIFT_Z = 0.4
    EMPTY_CHANCE = 0.3


class Tau23BaseSimpleGasCrystalField(mineable.GasCrystalRewardField):
    FIELD_CLASS = Tau23SimpleCrystalField
    REWARDS_GROUP_CLASS = Tau23SimpleCrystalRewards
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class Tau23SimpleGasCrystalField1(Tau23Member, Tau23BaseSimpleGasCrystalField):
    INDEX = 1
    ULTRA_BASE = Tau23GasMiner1


class Tau23SimpleGasCrystalField2(Tau23Member, Tau23BaseSimpleGasCrystalField):
    INDEX = 2
    ULTRA_BASE = Tau23GasMiner2


class Tau23SimpleGasCrystalField3(Tau23Member, Tau23BaseSimpleGasCrystalField):
    INDEX = 3
    ULTRA_BASE = Tau23GasMiner3


class Tau23SimpleGasCrystalField4(Tau23Member, Tau23BaseSimpleGasCrystalField):
    INDEX = 4
    ULTRA_BASE = Tau23GasMiner4


class Tau23SimpleGasCrystalField5(Tau23Member, Tau23BaseSimpleGasCrystalField):
    INDEX = 5
    ULTRA_BASE = Tau23GasMiner5


class Tau23SimpleGasCrystalField6(Tau23Member, Tau23BaseSimpleGasCrystalField):
    INDEX = 6
    ULTRA_BASE = Tau23GasMiner6


class Tau23SimpleGasCrystalField7(Tau23Member, Tau23BaseSimpleGasCrystalField):
    INDEX = 7
    ULTRA_BASE = Tau23GasMiner7


class Tau23SimpleGasCrystalField8(Tau23Member, Tau23BaseSimpleGasCrystalField):
    INDEX = 8
    ULTRA_BASE = Tau23GasMiner8


class Tau23SimpleGasCrystalField9(Tau23Member, Tau23BaseSimpleGasCrystalField):
    INDEX = 9
    ULTRA_BASE = Tau23GasMiner9


class Tau23SimpleGasCrystalField10(Tau23Member, Tau23BaseSimpleGasCrystalField):
    INDEX = 10
    ULTRA_BASE = Tau23GasMiner10


class Tau23AbandonedMiner1(Tau23Member, Tau23Bretonia, Tau23BaseAbandonedMiner):
    INDEX = 1
    BASE_INDEX = 61
    ASTEROID_ZONES = [
        Tau23GasPocketsZone1
    ]
    RU_NAME = MS('База Кайкос', 'Caicos Base')
    MISC_EQUIP_TYPE = BR_MAIN
    EQUIP_SET = markets.EquipSet(
        Q.Gun('br_heavygun', eq_classes=markets.SECRET2),
        Q.Engine(BR_MAIN, eq_classes=markets.SECRET2),
    )


class Tau23AbandonedMiner2(Tau23Member, Tau23Bretonia, Tau23BaseAbandonedMiner):
    INDEX = 2
    BASE_INDEX = 62
    ASTEROID_ZONES = [
        Tau23GasPocketsZone2
    ]
    RU_NAME = MS('База Теркс', 'Turks Base')
    MISC_EQUIP_TYPE = BR_MAIN
    EQUIP_SET = markets.EquipSet(
        Q.Gun('br_lightgun', eq_classes=markets.SECRET2),
        Q.Engine(BR_MAIN, eq_classes=markets.SECRET2),
    )


class Tau23AbandonedMiner3(Tau23Kusari, Tau23Member, Tau23BaseAbandonedMiner):
    INDEX = 3
    BASE_INDEX = 63
    ASTEROID_ZONES = [
        Tau23GasPocketsZone3
    ]
    RU_NAME = MS('База Наха', "Naha Base")
    MISC_EQUIP_TYPE = KU_MAIN
    EQUIP_SET = markets.EquipSet(
        Q.Gun('ku_heavygun', eq_classes=markets.SECRET2),
        Q.Engine(KU_MAIN, eq_classes=markets.SECRET2),
    )


class Tau23ComplexCrystalRewards(Tau23Member, mineable.DefaultGasCrystalRewardsGroup):
    NAME = 'Tau23_gascryst_complex1'
    SOLAR = gas_crystal.ComplexCrystalAsteroid
    REWARD_ITEM = 'comm_gas_balloons'
    ULTRA_REWARD_BASES = [
        Tau23AbandonedMiner1,
        Tau23AbandonedMiner2,
        Tau23AbandonedMiner3,
    ]


class Tau23ComplexCrystalField(mineable.DefaultField):
    BOX_SIZE = 1400
    DENSITY_MULTIPLER = 1
    DRIFT_X = 0.3
    DRIFT_Y = 0.5
    DRIFT_Z = 0.3


class Tau23BaseComplexGasCrystalField(mineable.ComplexGasCrystalRewardField):
    FIELD_CLASS = Tau23ComplexCrystalField
    REWARDS_GROUP_CLASS = Tau23ComplexCrystalRewards
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class ComplexGasCrystalField1(Tau23Member, Tau23BaseComplexGasCrystalField):
    INDEX = 1
    ULTRA_BASE = Tau23AbandonedMiner1


class ComplexGasCrystalField2(Tau23Member, Tau23BaseComplexGasCrystalField):
    INDEX = 2
    ULTRA_BASE = Tau23AbandonedMiner2


class ComplexGasCrystalField3(Tau23Member, Tau23BaseComplexGasCrystalField):
    INDEX = 3
    ULTRA_BASE = Tau23AbandonedMiner3

