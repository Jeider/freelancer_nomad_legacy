from fx.space import Dust
from fx.sound import Ambience

from universe.content.system_object import TOP, BOTTOM, LEFT, RIGHT
from universe.content import main_objects
from universe.content.zones import TemplatedNebulaZone, AsteroidZone
from universe.content.asteroid_definition import AsteroidDefinition
from universe.content import interior
from universe.content import dealers
from universe.content.space_voice import SpaceVoice
from universe.content import faction

from templates.dockable.gas_miner import BretoniaPirateGasMiner, RheinlandCivilianGasMiner, RheinlandPirateGasMiner, CadizGasMiner
from templates.dockable.trade_storages import HonshuStorage

from universe.content.mineable import DefaultGasCrystalRewardsGroup, DefaultField, GasCrystalRewardField, ComplexGasCrystalRewardField
from templates.nebula.exclusion import CROW_EXCLUSION, BARRIER_EXCLUSION, BARRIER_EXCLUSION_SMALL
from templates.nebula.sig13_blue_nebula import Sig13BlueNebulaTemplate
from templates.solar.gas_crystal import SimpleCrystalAsteroid, ComplexCrystalAsteroid





class Sigma13Member(object):
    INDEX = 1
    FACTION = faction.RH_GRP
    ABSTRACT = False


class Sig13Rheinland(object):
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_RH


class Sig13Liberty(object):
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_LI


class Sigma13StaticText(Sigma13Member, main_objects.RawText):
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

[EncounterParameters]
nickname = rh_grp_main_defend
filename = missions\\npc\\rh\\rh_grp_main_defend.ini

[EncounterParameters]
nickname = rh_grp_main_scout
filename = missions\\npc\\rh\\rh_grp_main_scout.ini

[EncounterParameters]
nickname = rh_grp_main_gunboat
filename = missions\\npc\\rh\\rh_grp_main_gunboat.ini

[EncounterParameters]
nickname = bh_grp_rh_scout
filename = missions\\npc\\rh\\bh_grp_rh_scout.ini

[EncounterParameters]
nickname = li_grp_main_defend
filename = missions\\npc\\li\\li_grp_main_defend.ini

[EncounterParameters]
nickname = li_grp_main_scout
filename = missions\\npc\\li\\li_grp_main_scout.ini

[EncounterParameters]
nickname = bh_grp_li_scout
filename = missions\\npc\\li\\bh_grp_li_scout.ini

[EncounterParameters]
nickname = pi_grp_rh_assault
filename = missions\\npc\\pi\\pi_grp_rh_assault.ini

[EncounterParameters]
nickname = pi_grp_li_assault
filename = missions\\npc\\pi\\pi_grp_li_assault.ini

[EncounterParameters]
nickname = li_grp_main_trade
filename = missions\\npc\\li\\li_grp_main_trade.ini

[EncounterParameters]
nickname = rh_grp_main_trade
filename = missions\\npc\\rh\\rh_grp_main_trade.ini

[EncounterParameters]
nickname = tr_grp_rh_transport
filename = missions\\npc\\rh\\tr_grp_rh_transport.ini

[EncounterParameters]
nickname = tr_grp_li_large_train
filename = missions\\npc\\li\\tr_grp_li_large_train.ini

[EncounterParameters]
nickname = li_grp_main_trade_tlr
filename = missions\\npc\\li\\li_grp_main_trade_tlr.ini

[EncounterParameters]
nickname = rh_grp_main_trade_tlr
filename = missions\\npc\\rh\\rh_grp_main_trade_tlr.ini

[EncounterParameters]
nickname = tr_grp_rh_transport_tlr
filename = missions\\npc\\rh\\tr_grp_rh_transport_tlr.ini

[EncounterParameters]
nickname = tr_grp_li_large_train_tlr
filename = missions\\npc\\li\\tr_grp_li_large_train_tlr.ini

[EncounterParameters]
nickname = rh_grp_main_patrol
filename = missions\\npc\\rh\\rh_grp_main_patrol.ini

[EncounterParameters]
nickname = li_grp_main_patrol
filename = missions\\npc\\li\\li_grp_main_patrol.ini

[EncounterParameters]
nickname = rh_junkers
filename = missions\\npc\\rh\\rh_junkers.ini

[EncounterParameters]
nickname = rh_pirates_patrol
filename = missions\\npc\\pi\\pi_grp_rh_patrol.ini

[EncounterParameters]
nickname = li_pirates_patrol
filename = missions\\npc\\pi\\pi_grp_li_patrol.ini

[EncounterParameters]
nickname = bh_grp_rh_patrol
filename = missions\\npc\\rh\\bh_grp_rh_patrol.ini

[EncounterParameters]
nickname = bh_grp_li_patrol
filename = missions\\npc\\li\\bh_grp_li_patrol.ini

[EncounterParameters]
nickname = co_grp_main_patrol
filename = missions\\npc\\co\\co_grp_main_patrol.ini

[EncounterParameters]
nickname = patrol_tlr
filename = missions\\NPC\\patrol_tlr.ini

[EncounterParameters]
nickname = patrol_police
filename = missions\\NPC\\patrol_police.ini

[EncounterParameters]
nickname = bh_grp_rh_trade
filename = missions\\npc\\rh\\bh_grp_rh_trade.ini

[EncounterParameters]
nickname = bh_grp_rh_trade_tlr
filename = missions\\npc\\rh\\bh_grp_rh_trade_tlr.ini

'''

CROW_EXCLUSION_PARAMS = {
    'zone_shell': CROW_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '255, 255, 200',
    'fog_far': 5000,
}


BARRIER_EXCLUSION_PARAMS = {
    'zone_shell': BARRIER_EXCLUSION,
    'shell_scalar': 1,
    'max_alpha': 0.3,
    'exclusion_tint': '0, 125, 255',
    'fog_far': 5000,
}




class Sig13Nebula(Sigma13Member, TemplatedNebulaZone):
    INDEX = 1
    FILE_NAME = 'gen_seg13_blue_nebula'
    SPACEDUST = Dust.ATTRACT
    SPACEDUST_MAXPARTICLES = 50
    MUSIC = Ambience.NEBULA_CROW
    CONTENT_TEMPLATE = Sig13BlueNebulaTemplate
    INTERFERENCE = 0.5

    PROPERTY_FLAGS = 32768
    PROPERTY_FOG_COLOR = '0.000000, 100.000000, 160.000000'


class Sig13Sun(Sigma13Member, main_objects.SunSmall):
    STAR = 'med_blue_sun'


class Sig13ForbesJumpgate(Sigma13Member, main_objects.Jumpgate):
    INDEX = 1
    REL = TOP


class Sig13CaliforniaJumpgate(Sigma13Member, main_objects.Jumpgate):
    INDEX = 2
    REL = LEFT


class Sig13BerlinJumpgate(Sigma13Member, main_objects.Jumpgate):
    INDEX = 3
    REL = BOTTOM


class Sig13LibertyStation(Sigma13Member, Sig13Liberty, main_objects.Station):
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
    EXCLUSION_PARAMS = BARRIER_EXCLUSION_PARAMS
    NEBULA_ZONES = [Sig13Nebula]
    INTERIOR_BG1 = interior.INTERIOR_BG_CROW

    FACTION = faction.LI_GRP


class Sig13RheinlandStation(Sigma13Member, Sig13Rheinland, main_objects.Station):
    INDEX = 2
    BASE_INDEX = 1
    REL = RIGHT
    REL_APPEND = 1500
    SPACE_OBJECT_TEMPLATE = RheinlandCivilianGasMiner
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.RheinlandCivilianDealers
    FACTION = faction.RH_GRP

    NEBULA_EXCLUSION_ZONE_SIZE = 3000
    EXCLUSION_PARAMS = BARRIER_EXCLUSION_PARAMS
    NEBULA_ZONES = [Sig13Nebula]
    INTERIOR_BG1 = interior.INTERIOR_BG_CROW


class Sig13Battleship(Sigma13Member, Sig13Rheinland, main_objects.RheinlandBattleship):
    BASE_INDEX = 4
    REL = RIGHT
    REL_APPEND = 1000
    REL_DRIFT = 1500
    INTERIOR_CLASS = interior.BattleshipInterior
    DEALERS = dealers.RheinlandMilitaryDealers
    FACTION = faction.RH_GRP

    NEBULA_EXCLUSION_ZONE_SIZE = 2000
    EXCLUSION_PARAMS = CROW_EXCLUSION_PARAMS
    NEBULA_ZONES = [Sig13Nebula]
    INTERIOR_BG1 = interior.INTERIOR_BG_CROW


class Sig13Freeport(Sigma13Member, Sig13Liberty, main_objects.Freeport):
    BASE_INDEX = 5
    REL = LEFT
    REL_APPEND = 1000
    SPACE_OBJECT_TEMPLATE = HonshuStorage
    INTERIOR_CLASS = interior.BattleshipInterior
    DEALERS = dealers.RheinlandMilitaryDealers
    FACTION = faction.LI_GRP
    ROTATE_RANDOM = True

    NEBULA_EXCLUSION_ZONE_SIZE = 2000
    EXCLUSION_PARAMS = BARRIER_EXCLUSION_PARAMS
    NEBULA_ZONES = [Sig13Nebula]
    INTERIOR_BG1 = interior.INTERIOR_BG_CROW


class Sig13PirateTopRight(Sigma13Member, Sig13Liberty, main_objects.PirateBase):
    BASE_INDEX = 6
    INDEX = 1
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = CadizGasMiner
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.LibertyPirateDealers
    FACTION = faction.LX_GRP
    DEFENCE_LEVEL = None

    NEBULA_EXCLUSION_ZONE_SIZE = 2000
    EXCLUSION_PARAMS = CROW_EXCLUSION_PARAMS
    NEBULA_ZONES = [Sig13Nebula]
    INTERIOR_BG1 = interior.INTERIOR_BG_CROW


class Sig13PirateTopLeft(Sigma13Member, Sig13Liberty, main_objects.PirateBase):
    BASE_INDEX = 7
    INDEX = 2
    REL = TOP
    SPACE_OBJECT_TEMPLATE = RheinlandPirateGasMiner
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.LibertyPirateDealers
    FACTION = faction.LX_GRP
    DEFENCE_LEVEL = None

    NEBULA_EXCLUSION_ZONE_SIZE = 2000
    EXCLUSION_PARAMS = CROW_EXCLUSION_PARAMS
    NEBULA_ZONES = [Sig13Nebula]
    INTERIOR_BG1 = interior.INTERIOR_BG_CROW


class Sig13PirateBottom(Sigma13Member, Sig13Rheinland, main_objects.PirateBase):
    BASE_INDEX = 8
    INDEX = 3
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = BretoniaPirateGasMiner
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.RheinlandPirateDealers
    FACTION = faction.RX_GRP
    DEFENCE_LEVEL = None

    NEBULA_EXCLUSION_ZONE_SIZE = 2000
    EXCLUSION_PARAMS = CROW_EXCLUSION_PARAMS
    NEBULA_ZONES = [Sig13Nebula]
    INTERIOR_BG1 = interior.INTERIOR_BG_CROW


class Sig13ConnRheinlandGas1(Sigma13Member, main_objects.TradeConnection):
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


class Sig13ConnRheinlandGas2(Sigma13Member, main_objects.TradeConnection):
    OBJ_FROM = Sig13RheinlandStation
    OBJ_TO = Sig13BerlinJumpgate
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        Sig13PirateBottom,
    ]


class Sig13ConnLibertyGas1(Sigma13Member, main_objects.TradeConnection):
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


class Sig13ConnLibertyGas2(Sigma13Member, main_objects.TradeConnection):
    OBJ_FROM = Sig13LibertyStation
    OBJ_TO = Sig13ForbesJumpgate
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        Sig13PirateTopLeft,
    ]


class Sig13ConnBattleship1(Sigma13Member, main_objects.TradeConnection):
    OBJ_FROM = Sig13Battleship
    OBJ_TO = Sig13BerlinJumpgate
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        # BerlinPiratesTop
    ]


class Sig13ConnBattleship2(Sigma13Member, main_objects.TradeConnection):
    OBJ_FROM = Sig13Battleship
    OBJ_TO = Sig13Freeport
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'F'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        Sig13PirateTopRight,
    ]


class Sig13ConnFreeport1(Sigma13Member, main_objects.TradeConnection):
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


class Sig13BaseAbandonedMiner(main_objects.AbandonedAsteroid):
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

class Sigma13GasPockets(AsteroidDefinition):
    FIELD = True
    CUBE = True
    FIELD_TEMPLATE = FIELD_TEMPLATE
    CUBE_TEMPLATE = CUBE_TEMPLATE


class Sigma13GasPockets1(Sigma13GasPockets):
    ABSTRACT = False
    NAME = 'sig13_gas_pocket1'


class Sigma13GasPockets2(Sigma13GasPockets):
    ABSTRACT = False
    NAME = 'sig13_gas_pocket2'


class Sigma13GasPockets3(Sigma13GasPockets):
    ABSTRACT = False
    NAME = 'sig13_gas_pocket3'


class Sigma13GasPocketsZone1(Sigma13Member, AsteroidZone):
    ALIAS = 'bigcryst'
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = Sigma13GasPockets1
    SPACEDUST = Dust.OXYGEN
    SPACEDUST_MAXPARTICLES = 200


class Sigma13GasPocketsZone2(Sigma13Member, AsteroidZone):
    ALIAS = 'bigcryst'
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = Sigma13GasPockets2
    SPACEDUST = Dust.OXYGEN
    SPACEDUST_MAXPARTICLES = 200


class Sigma13GasPocketsZone3(Sigma13Member, AsteroidZone):
    ALIAS = 'bigcryst'
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = Sigma13GasPockets3
    SPACEDUST = Dust.OXYGEN
    SPACEDUST_MAXPARTICLES = 200


class Sig13GasMiner1(Sigma13Member, Sig13BaseRheinlandGasMiner):
    INDEX = 1
    BASE_INDEX = 51


class Sig13GasMiner2(Sigma13Member, Sig13BaseRheinlandGasMiner):
    INDEX = 2
    BASE_INDEX = 52


class Sig13GasMiner3(Sigma13Member, Sig13BaseLibertyGasMiner):
    INDEX = 3
    BASE_INDEX = 53


class Sig13GasMiner4(Sigma13Member, Sig13BaseRheinlandGasMiner):
    INDEX = 4
    BASE_INDEX = 54


class Sig13GasMiner5(Sigma13Member, Sig13BaseRheinlandGasMiner):
    INDEX = 5
    BASE_INDEX = 55


class Sig13GasMiner6(Sigma13Member, Sig13BaseRheinlandGasMiner):
    INDEX = 6
    BASE_INDEX = 56


class Sig13GasMiner7(Sigma13Member, Sig13BaseLibertyGasMiner):
    INDEX = 7
    BASE_INDEX = 57


class Sig13GasMiner8(Sigma13Member, Sig13BaseLibertyGasMiner):
    INDEX = 8
    BASE_INDEX = 58


class Sig13GasMiner9(Sigma13Member, Sig13BaseLibertyGasMiner):
    INDEX = 9
    BASE_INDEX = 59


class Sig13SimpleCrystalRewards(Sigma13Member, DefaultGasCrystalRewardsGroup):
    NAME = 'sig13_gascryst_simple1'
    SOLAR = SimpleCrystalAsteroid
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

class Sig13SimpleCrystalField(DefaultField):
    BOX_SIZE = 1000
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.4
    DRIFT_Y = 0.4
    DRIFT_Z = 0.4
    EMPTY_CHANCE = 0.3


class Sig13BaseSimpleGasCrystalField(GasCrystalRewardField):
    FIELD_NAME = None
    FIELD_CLASS = Sig13SimpleCrystalField
    REWARDS_GROUP_CLASS = Sig13SimpleCrystalRewards
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class Sig13SimpleGasCrystalField1(Sigma13Member, Sig13BaseSimpleGasCrystalField):
    FIELD_NAME = 'sig13_simple_field1'
    INDEX = 1
    ULTRA_BASE = Sig13GasMiner1


class Sig13SimpleGasCrystalField2(Sigma13Member, Sig13BaseSimpleGasCrystalField):
    FIELD_NAME = 'sig13_simple_field2'
    INDEX = 2
    ULTRA_BASE = Sig13GasMiner2


class Sig13SimpleGasCrystalField3(Sigma13Member, Sig13BaseSimpleGasCrystalField):
    FIELD_NAME = 'sig13_simple_field3'
    INDEX = 3
    ULTRA_BASE = Sig13GasMiner3


class Sig13SimpleGasCrystalField4(Sigma13Member, Sig13BaseSimpleGasCrystalField):
    FIELD_NAME = 'sig13_simple_field4'
    INDEX = 4
    ULTRA_BASE = Sig13GasMiner4


class Sig13SimpleGasCrystalField5(Sigma13Member, Sig13BaseSimpleGasCrystalField):
    FIELD_NAME = 'sig13_simple_field5'
    INDEX = 5
    ULTRA_BASE = Sig13GasMiner5


class Sig13SimpleGasCrystalField6(Sigma13Member, Sig13BaseSimpleGasCrystalField):
    FIELD_NAME = 'sig13_simple_field6'
    INDEX = 6
    ULTRA_BASE = Sig13GasMiner6


class Sig13SimpleGasCrystalField7(Sigma13Member, Sig13BaseSimpleGasCrystalField):
    FIELD_NAME = 'sig13_simple_field7'
    INDEX = 7
    ULTRA_BASE = Sig13GasMiner7


class Sig13SimpleGasCrystalField8(Sigma13Member, Sig13BaseSimpleGasCrystalField):
    FIELD_NAME = 'sig13_simple_field8'
    INDEX = 8
    ULTRA_BASE = Sig13GasMiner8


class Sig13SimpleGasCrystalField9(Sigma13Member, Sig13BaseSimpleGasCrystalField):
    FIELD_NAME = 'sig13_simple_field9'
    INDEX = 9
    ULTRA_BASE = Sig13GasMiner9


class Sig13AbandonedMiner1(Sigma13Member, Sig13Rheinland, Sig13BaseAbandonedMiner):
    INDEX = 1
    BASE_INDEX = 60
    ASTEROID_ZONES = [
        Sigma13GasPocketsZone1
    ]


class Sig13AbandonedMiner2(Sigma13Member, Sig13Rheinland, Sig13BaseAbandonedMiner):
    INDEX = 2
    BASE_INDEX = 61
    ASTEROID_ZONES = [
        Sigma13GasPocketsZone2
    ]


class Sig13AbandonedMiner3(Sigma13Member, Sig13Liberty, Sig13BaseAbandonedMiner):
    INDEX = 3
    BASE_INDEX = 62
    ASTEROID_ZONES = [
        Sigma13GasPocketsZone3
    ]


class Sig13ComplexCrystalRewards(Sigma13Member, DefaultGasCrystalRewardsGroup):
    NAME = 'sig13_gascryst_complex1'
    SOLAR = ComplexCrystalAsteroid
    REWARD_ITEM = 'comm_gas_balloons'
    ULTRA_REWARD_BASES = [
        Sig13AbandonedMiner1,
        Sig13AbandonedMiner2,
        Sig13AbandonedMiner3,
    ]


class Sig13ComplexCrystalField(DefaultField):
    BOX_SIZE = 1400
    DENSITY_MULTIPLER = 1
    DRIFT_X = 0.3
    DRIFT_Y = 0.5
    DRIFT_Z = 0.3


class Sig13BaseComplexGasCrystalField(ComplexGasCrystalRewardField):
    FIELD_NAME = None
    FIELD_CLASS = Sig13ComplexCrystalField
    REWARDS_GROUP_CLASS = Sig13ComplexCrystalRewards
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class ComplexGasCrystalField1(Sigma13Member, Sig13BaseComplexGasCrystalField):
    FIELD_NAME = 'sig13_complex_field1'
    INDEX = 1
    ULTRA_BASE = Sig13AbandonedMiner1


class ComplexGasCrystalField2(Sigma13Member, Sig13BaseComplexGasCrystalField):
    FIELD_NAME = 'sig13_complex_field2'
    INDEX = 2
    ULTRA_BASE = Sig13AbandonedMiner2


class ComplexGasCrystalField3(Sigma13Member, Sig13BaseComplexGasCrystalField):
    FIELD_NAME = 'sig13_complex_field3'
    INDEX = 3
    ULTRA_BASE = Sig13AbandonedMiner3
