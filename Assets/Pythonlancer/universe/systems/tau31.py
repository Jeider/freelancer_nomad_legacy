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
from templates.nebula import tau31_nebula
from templates.nebula import exclusion
from templates.solar import gas_crystal
from templates.solar import hackable

from templates.dockable import gas_miner
from templates.dockable import bounty_hunter
from templates.dockable import upsilon_gasinside


class Tau31Member(Member):
    FACTION = faction.LibertyMain
    INTERIOR_BG1 = interior.INTERIOR_BG_EDGE
    WEAPON_FACTION = WEAPON_LI
    EQUIP_FACTION = EQUIP_LI


class Tau31StaticText(Tau31Member, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = tau31
space_color = 0, 0, 0
local_faction = li_grp

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Music]
space = music_tau_space
danger = music_tau_danger
battle = music_tau_battle

[Ambient]
color = 0, 0, 0

[Dust]
spacedust = Dust

[LightSource]
nickname = tau31_system_light
pos = -31, 0, -48
color = 110, 255, 255
range = 80000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION

[zone]
nickname = zone_tau31_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
;property_flags = 512 ;lava - MILITARY
;property_flags = 256 ;ice - TRADING
property_flags = 2048 ;crystal - GASMINING
'''


class Tau31Nebula(Tau31Member, zones.NebulaZone):
    INDEX = 1
    SPACEDUST = Dust.ATTRACT_GREEN
    SPACEDUST_MAXPARTICLES = 50
    MUSIC = Ambience.NEBULA_EDGE
    CONTENT_TEMPLATE = tau31_nebula.Tau31MainNebulaTemplate
    INTERFERENCE = 0.5


EDGE_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.EDGE_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '110, 130, 110',
    'fog_far': 5000,
}

EDGE_EXCLUSION_PARAMS_NEAR = {
    'zone_shell': exclusion.EDGE_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '110, 130, 110',
    'fog_far': 2500,
}


class Tau31Sun(Tau31Member, main_objects.SunSmall):
    STAR = 'med_white_sun'


class Tau31ManhattanJumpgate(Tau31Member, main_objects.Jumpgate):
    INDEX = 1
    REL = RIGHT
    TARGET_SYSTEM_NAME = 'li_mnh'


class Tau31Tau37Jumpgate(Tau31Member, main_objects.Jumpgate):
    INDEX = 2
    REL = LEFT
    TARGET_SYSTEM_NAME = 'tau37'


class Tau31ColumbiaJumpgate(Tau31Member, main_objects.Jumpgate):
    INDEX = 3
    REL = BOTTOM
    TARGET_SYSTEM_NAME = 'li_col'


class Tau31Station(Tau31Member, main_objects.GasMiningStation):
    INDEX = 1
    BASE_INDEX = 1
    REL = TOP
    REL_DRIFT = 0
    REL_APPEND = 2000
    ARCHETYPE = 'smallstation1_old'
    LOADOUT = 'smallstation_li'
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.LibertyCivilianDealers

    NEBULA_EXCLUSION_ZONE_SIZE = 5000
    EXCLUSION_PARAMS = EDGE_EXCLUSION_PARAMS
    NEBULA_ZONES = [Tau31Nebula]


class Tau31Battleship(Tau31Member, main_objects.LibertyBattleship):
    BASE_INDEX = 2
    REL = RIGHT
    REL_APPEND = 1000
    REL_DRIFT = 500
    INTERIOR_CLASS = interior.BattleshipInterior
    DEALERS = dealers.LibertyMilitaryDealers

    NEBULA_EXCLUSION_ZONE_SIZE = 3000
    EXCLUSION_PARAMS = EDGE_EXCLUSION_PARAMS
    NEBULA_ZONES = [Tau31Nebula]


class Tau31Trading(Tau31Member, main_objects.TradingBase):
    BASE_INDEX = 3
    REL = TOP
    REL_APPEND = 1000
    REL_DRIFT = 1500
    SPACE_OBJECT_TEMPLATE = bounty_hunter.TauFreeport
    INTERIOR_CLASS = interior.BattleshipInterior
    DEALERS = dealers.LibertyCivilianDealers

    NEBULA_EXCLUSION_ZONE_SIZE = 2500
    EXCLUSION_PARAMS = EDGE_EXCLUSION_PARAMS
    NEBULA_ZONES = [Tau31Nebula]


class Tau31BottomPirates(Tau31Member, main_objects.PirateGasMiner):
    BASE_INDEX = 4
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = gas_miner.BretoniaPirateGasMiner
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.LibertyPirateDealers
    DEFENCE_LEVEL = None
    FACTION = faction.LibertyPirate

    NEBULA_EXCLUSION_ZONE_SIZE = 2000
    EXCLUSION_PARAMS = EDGE_EXCLUSION_PARAMS
    NEBULA_ZONES = [Tau31Nebula]


class Tau31TopPirates(Tau31Member, main_objects.PirateGasMiner):
    INDEX = 2
    BASE_INDEX = 5
    REL = TOP
    SPACE_OBJECT_TEMPLATE = gas_miner.RheinlandPirateGasMiner
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.LibertyPirateDealers
    DEFENCE_LEVEL = None
    FACTION = faction.LibertyPirate

    NEBULA_EXCLUSION_ZONE_SIZE = 2000
    EXCLUSION_PARAMS = EDGE_EXCLUSION_PARAMS
    NEBULA_ZONES = [Tau31Nebula]


class Tau31StationConn1(Tau31Member, main_objects.TradeConnection):
    OBJ_FROM = Tau31Station
    OBJ_TO = Tau31ManhattanJumpgate
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        Tau31TopPirates,
    ]


class Tau31StationConn2(Tau31Member, main_objects.TradeConnection):
    OBJ_FROM = Tau31Station
    OBJ_TO = Tau31Battleship
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        Tau31BottomPirates,
    ]


class Tau31StationConn3(Tau31Member, main_objects.TradeConnection):
    OBJ_FROM = Tau31Station
    OBJ_TO = Tau31Trading
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        Tau31TopPirates,
    ]


class Tau31TradingConn1(Tau31Member, main_objects.TradeConnection):
    OBJ_FROM = Tau31Trading
    OBJ_TO = Tau31Tau37Jumpgate
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        Tau31TopPirates,
    ]


class Tau31BattleshipConn1(Tau31Member, main_objects.TradeConnection):
    OBJ_FROM = Tau31Battleship
    OBJ_TO = Tau31ColumbiaJumpgate
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'F'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        Tau31BottomPirates,
    ]


class Tau31BaseLibertyGasMiner(main_objects.GasMinerOld):
    ALIAS = 'cryst'
    ROTATE_RANDOM = True
    ARCHETYPE = 'gas_miner_old'
    LOADOUT = 'gas_miner_old_li'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    NEBULA_EXCLUSION_ZONE_SIZE = 3000
    EXCLUSION_PARAMS = EDGE_EXCLUSION_PARAMS
    NEBULA_ZONES = [Tau31Nebula]
    NEBULA_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.ICE,
        'spacedust_maxparticles': 200,
    }


class Tau31BaseAbandonedMiner(main_objects.AbandonedAsteroidIce):
    ALIAS = 'bigcryst'
    ROTATE_RANDOM = True
    ARCHETYPE = 'miningbase_ice_block'
    # LOADOUT = 'miningbase_ice_block_pi_01'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    NEBULA_EXCLUSION_ZONE_SIZE = 8500
    AST_EXCLUSION_ZONE_SIZE = 2000
    EXCLUSION_PARAMS = EDGE_EXCLUSION_PARAMS
    NEBULA_ZONES = [Tau31Nebula]
    AST_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.ICE,
        'spacedust_maxparticles': 200,
    }


FIELD_TEMPLATE = '''
cube_size = 400
fill_dist = 1500
diffuse_color = 100, 200, 100
ambient_color = 150, 200, 150
ambient_increase = 20, 255, 20
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


class Tau31GasPockets(asteroid_definition.AsteroidDefinition):
    FIELD = True
    CUBE = True
    FIELD_TEMPLATE = FIELD_TEMPLATE
    CUBE_TEMPLATE = CUBE_TEMPLATE


class Tau31GasPocketsZone1(Tau31Member, zones.AsteroidZone):
    ALIAS = 'bigcryst'
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = Tau31GasPockets
    SPACEDUST = Dust.OXYGEN
    SPACEDUST_MAXPARTICLES = 200


class Tau31GasPocketsZone2(Tau31Member, zones.AsteroidZone):
    ALIAS = 'bigcryst'
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = Tau31GasPockets
    SPACEDUST = Dust.OXYGEN
    SPACEDUST_MAXPARTICLES = 200


class Tau31GasPocketsSpecialZone1(Tau31Member, zones.AsteroidZone):
    ALIAS = 'pocket'
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = Tau31GasPockets
    SPACEDUST = Dust.ORGANISM
    SPACEDUST_MAXPARTICLES = 200


class Tau31GasMiner1(Tau31Member, Tau31BaseLibertyGasMiner):
    INDEX = 1
    BASE_INDEX = 51


class Tau31GasMiner2(Tau31Member, Tau31BaseLibertyGasMiner):
    INDEX = 2
    BASE_INDEX = 52


class Tau31GasMiner3(Tau31Member, Tau31BaseLibertyGasMiner):
    INDEX = 3
    BASE_INDEX = 53


class Tau31GasMiner4(Tau31Member, Tau31BaseLibertyGasMiner):
    INDEX = 4
    BASE_INDEX = 54


class Tau31GasMiner5(Tau31Member, Tau31BaseLibertyGasMiner):
    INDEX = 5
    BASE_INDEX = 55


class Tau31SimpleCrystalRewards(Tau31Member, mineable.DefaultGasCrystalRewardsGroup):
    NAME = 'Tau31_gascryst_simple1'
    SOLAR = gas_crystal.SimpleCrystalAsteroid
    REWARD_ITEM = 'comm_gas_balloons'
    ULTRA_REWARD_BASES = [
        Tau31GasMiner1,
        Tau31GasMiner2,
        Tau31GasMiner3,
        Tau31GasMiner4,
        Tau31GasMiner5,
    ]


class Tau31SimpleCrystalField(mineable.DefaultField):
    BOX_SIZE = 1000
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.4
    DRIFT_Y = 0.4
    DRIFT_Z = 0.4
    EMPTY_CHANCE = 0.3


class Tau31BaseSimpleGasCrystalField(mineable.GasCrystalRewardField):
    FIELD_CLASS = Tau31SimpleCrystalField
    REWARDS_GROUP_CLASS = Tau31SimpleCrystalRewards
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class Tau31SimpleGasCrystalField1(Tau31Member, Tau31BaseSimpleGasCrystalField):
    INDEX = 1
    ULTRA_BASE = Tau31GasMiner1


class Tau31SimpleGasCrystalField2(Tau31Member, Tau31BaseSimpleGasCrystalField):
    INDEX = 2
    ULTRA_BASE = Tau31GasMiner2


class Tau31SimpleGasCrystalField3(Tau31Member, Tau31BaseSimpleGasCrystalField):
    INDEX = 3
    ULTRA_BASE = Tau31GasMiner3


class Tau31SimpleGasCrystalField4(Tau31Member, Tau31BaseSimpleGasCrystalField):
    INDEX = 4
    ULTRA_BASE = Tau31GasMiner4


class Tau31SimpleGasCrystalField5(Tau31Member, Tau31BaseSimpleGasCrystalField):
    INDEX = 5
    ULTRA_BASE = Tau31GasMiner5


class Tau31AbandonedMiner1(Tau31Member, Tau31BaseAbandonedMiner):
    INDEX = 1
    BASE_INDEX = 60
    ASTEROID_ZONES = [
        Tau31GasPocketsZone1
    ]


class Tau31AbandonedMiner2(Tau31Member, Tau31BaseAbandonedMiner):
    INDEX = 2
    BASE_INDEX = 61
    ASTEROID_ZONES = [
        Tau31GasPocketsZone2
    ]


class Tau31ComplexCrystalRewards(Tau31Member, mineable.DefaultGasCrystalRewardsGroup):
    NAME = 'Tau31_gascryst_complex1'
    SOLAR = gas_crystal.ComplexCrystalAsteroid
    REWARD_ITEM = 'comm_gas_balloons'
    ULTRA_REWARD_BASES = [
        Tau31AbandonedMiner1,
        Tau31AbandonedMiner2,
    ]


class Tau31ComplexCrystalField(mineable.DefaultField):
    BOX_SIZE = 1400
    DENSITY_MULTIPLER = 1
    DRIFT_X = 0.3
    DRIFT_Y = 0.5
    DRIFT_Z = 0.3


class Tau31BaseComplexGasCrystalField(mineable.ComplexGasCrystalRewardField):
    FIELD_CLASS = Tau31ComplexCrystalField
    REWARDS_GROUP_CLASS = Tau31ComplexCrystalRewards
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class ComplexGasCrystalField1(Tau31Member, Tau31BaseComplexGasCrystalField):
    INDEX = 1
    ULTRA_BASE = Tau31AbandonedMiner1


class ComplexGasCrystalField2(Tau31Member, Tau31BaseComplexGasCrystalField):
    INDEX = 2
    ULTRA_BASE = Tau31AbandonedMiner2


class Tau31OldResearchRuins(Tau31Member, main_objects.StationRuins):
    ALIAS = 'ruins'
    INDEX = 1
    REL = RIGHT

    SPACE_OBJECT_TEMPLATE = upsilon_gasinside.UpsilonLostResearch

    ASTEROID_ZONES = [
        Tau31GasPocketsSpecialZone1,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500

    NEBULA_EXCLUSION_ZONE_SIZE = 2500
    EXCLUSION_PARAMS = EDGE_EXCLUSION_PARAMS_NEAR
    NEBULA_ZONES = [Tau31Nebula]


class Tau31OldResearchRuinsSuprisePoint1(Tau31Member, main_objects.HackableStation):
    ALIAS = 'ruins_dock'
    INDEX = 1
    BASE_INDEX = 71
    RELATED_OBJECT = Tau31OldResearchRuins
    RELATED_OBJECT_INDEX = 0
    HACKABLE_SOLAR_CLASS = hackable.HackablePrisonRot180
    INTERIOR_CLASS = interior.EquipDeckInterior


class Tau31OldResearchRuinsSuprisePoint2(Tau31Member, main_objects.HackableStation):
    ALIAS = 'ruins_dock'
    INDEX = 2
    BASE_INDEX = 72
    RELATED_OBJECT = Tau31OldResearchRuins
    RELATED_OBJECT_INDEX = 1
    HACKABLE_SOLAR_CLASS = hackable.HackablePrison
    INTERIOR_CLASS = interior.EquipDeckInterior
