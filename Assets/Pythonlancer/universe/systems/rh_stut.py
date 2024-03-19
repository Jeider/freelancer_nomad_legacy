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
from templates.solar import suprise
from templates.solar import debris_box
from templates.nebula.rh_stut_orange_nebula import RhStutOrangeNebulaTemplate
from templates.nebula import exclusion

from templates.dockable import pirate
from templates.dockable import junker
from templates.dockable import shipyards
from templates.dockable import police
from templates.dockable import stuttgart_megabase
from templates.dockable import bounty_hunter


class StutMember(object):
    INDEX = 1
    ABSTRACT = False
    FACTION = faction.RH_GRP

    INTERIOR_BG1 = interior.INTERIOR_RH_STUTTGART


class StutRawText(StutMember, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = rh_stut
space_color = 10, 10, 0
local_faction = rh_grp
space_farclip = 75000

[TexturePanels]
file = universe\heavens\shapes.ini

[Music]
space = music_rh_space
danger = music_rh_danger
battle = music_rh_battle

[Dust]
spacedust = Dust

[Ambient]
color = 20, 10, 5

[Background]
nebulae = solar\\stars_mod\\rh_stut_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_rh_stut_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
property_flags = 512 ;lava - MILITARY
;property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = rh_stut_System_Light
pos = 0, 0, 0
color = 252, 153, 53
; color = 255, 255, 255
range = 120000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION'''


class StutOrangeNebula1(StutMember, zones.NebulaZone):
    INDEX = 1
    FILE_NAME = 'gen_rh_stut_orange_nebula'
    SPACEDUST = Dust.ATTRACT_ORANGE
    SPACEDUST_MAXPARTICLES = 40
    MUSIC = Ambience.NEBULA_WALKER
    CONTENT_TEMPLATE = RhStutOrangeNebulaTemplate
    INTERFERENCE = 0.5

    PROPERTY_FLAGS = 32768
    PROPERTY_FOG_COLOR = '150, 100, 20'


WALKER_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.WALKER_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '255, 255, 255',
    'fog_far': 5000,
}


class StutDebrisZoneDefinition1(asteroid_definition.DebrisDefinition):
    ABSTRACT = False
    NAME = 'rh_stut_debris_field1'


class StutDebrisZoneDefinition2(asteroid_definition.DebrisDefinition):
    ABSTRACT = False
    NAME = 'rh_stut_debris_field2'


class StutDebrisZoneDefinition3(asteroid_definition.DebrisDefinition):
    ABSTRACT = False
    NAME = 'rh_stut_debris_field3'


class StutDebrisZone1(StutMember, zones.DebrisZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = StutDebrisZoneDefinition1


class StutDebrisZone2(StutMember, zones.DebrisZone):
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = StutDebrisZoneDefinition2


class StutDebrisZone3(StutMember, zones.DebrisZone):
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = StutDebrisZoneDefinition3



class StutBaseDebrisManufactoring(main_objects.DebrisManufactoring):
    ALIAS = 'deb'
    ROTATE_RANDOM = True
    ARCHETYPE = 'mplatform'
    LOADOUT = 'mplatform_rh_debris'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    AST_EXCLUSION_ZONE_SIZE = 2000
    AST_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.RADIOACTIVE_RED,
        'spacedust_maxparticles': 200,
    }


class StutDebrisFactory1(StutMember, StutBaseDebrisManufactoring):
    INDEX = 2
    BASE_INDEX = 51
    ASTEROID_ZONES = [
        StutDebrisZone2,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500


class StutDebrisFactory2(StutMember, StutBaseDebrisManufactoring):
    INDEX = 3
    BASE_INDEX = 52
    ASTEROID_ZONES = [
        StutDebrisZone3,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500


class StutDebrisBoxReward(StutMember, mineable.DefaultDebrisBoxRewardsGroup):
    NAME = 'rh_biz_debrisbox'
    SOLAR = debris_box.DebrisBox
    REWARD_ITEM = 'comm_scrap_metal'
    ULTRA_REWARD_BASES = [
        StutDebrisFactory1,
        StutDebrisFactory2,
    ]

class StutBaseDebrisBoxRewardField(mineable.DebrisBoxRewardField):
    FIELD_NAME = None
    FIELD_CLASS = mineable.MineableDebrixBoxField
    REWARDS_GROUP_CLASS = StutDebrisBoxReward
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class StutDebrisBoxField1(StutMember, StutBaseDebrisBoxRewardField):
    FIELD_NAME = 'rh_stut_debris1'
    INDEX = 2
    ULTRA_BASE = StutDebrisFactory1


class StutDebrisBoxField2(StutMember, StutBaseDebrisBoxRewardField):
    FIELD_NAME = 'rh_stut_debris2'
    INDEX = 3
    ULTRA_BASE = StutDebrisFactory2




class StutBaseSolarPlant(main_objects.SolarPlant):
    ALIAS = 'solar'
    ROTATE_RANDOM = True
    ARCHETYPE = 'solar_plant_old'
    LOADOUT = 'solar_plant_rh'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True
    AST_EXCLUSION_ZONE_SIZE = 600

    NEBULA_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.RADIOACTIVE_RED,
        'spacedust_maxparticles': 200,
    }


FIELD_TEMPLATE = '''
cube_size = 500
fill_dist = 1500
diffuse_color = 200, 200, 200
ambient_color = 110, 110, 110
ambient_increase = 80, 80, 80
empty_cube_frequency = 0.0
'''

CUBE_TEMPLATE = '''
asteroid = mine_spike_minedout, 0.200000, 0.800000, 0.300000, 45, 20, 0, mine
asteroid = mine_spike_minedout, 0.600000, 0.200000, -0.200000, 35, 10, 20, mine
asteroid = mine_spike_minedout, 0.400000, -0.700000, -0.200000, 15, 90, 120, mine
asteroid = mine_spike_minedout, -0.200000, -0.100000, -0.600000, 105, 160, 25, mine
asteroid = mine_spike_minedout, 0.500000, -0.200000, -0.600000, 75, 30, 70, mine
asteroid = mine_spike_minedout, -0.700000, 0.400000, -0.400000, 75, 30, 70, mine
asteroid = mine_spike_minedout, -0.200000, 0.600000, 0.600000, 105, 160, 25, mine
asteroid = mine_spike_minedout, -0.500000, -0.200000, 0.600000, 75, 30, 70, mine
'''

BILLBOARD_TEMPLATE = '''
[AsteroidBillboards]
count = 600
start_dist = 2500
fade_dist_percent = 0.900000
shape = spike_mine_tri_minedout
size = 300, 300
'''


class StutSolarMines(asteroid_definition.AsteroidDefinition):
    FIELD = True
    CUBE = True
    BILLBOARDS = True
    FIELD_TEMPLATE = FIELD_TEMPLATE
    CUBE_TEMPLATE = CUBE_TEMPLATE
    BILLBOARD_TEMPLATE = BILLBOARD_TEMPLATE
    SHAPES = [
        asteroid_definition.SHAPES_MINES,
    ]


class StutSolarMines1(StutSolarMines):
    ABSTRACT = False
    NAME = 'rh_stut_solar_mines1'


class StutSolarMines2(StutSolarMines):
    ABSTRACT = False
    NAME = 'rh_stut_solar_mines2'


class StutSolarMines3(StutSolarMines):
    ABSTRACT = False
    NAME = 'rh_stut_solar_mines3'


class StutSolarMines4(StutSolarMines):
    ABSTRACT = False
    NAME = 'rh_stut_solar_mines4'


class StutSolarMines5(StutSolarMines):
    ABSTRACT = False
    NAME = 'rh_stut_solar_mines5'


class StutBaseMinesZone(zones.AsteroidZone):
    SPACEDUST = Dust.DEBRIS
    SPACEDUST_MAXPARTICLES = 100
    MUSIC = Ambience.MINE_AST
    INTERFERENCE = 0.1
    DRAG_MODIFIER = 1.5
    PROPERTY_FLAGS = 4128


class StutSolarMinesZone1(StutMember, StutBaseMinesZone):
    ALIAS = 'solar'
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = StutSolarMines1


class StutSolarMinesZone2(StutMember, StutBaseMinesZone):
    ALIAS = 'solar'
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = StutSolarMines2


class StutSolarMinesZone3(StutMember, StutBaseMinesZone):
    ALIAS = 'solar'
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = StutSolarMines3


class StutSolarMinesZone4(StutMember, StutBaseMinesZone):
    ALIAS = 'solar'
    INDEX = 4
    ASTEROID_DEFINITION_CLASS = StutSolarMines4


class StutSolarMinesZone5(StutMember, StutBaseMinesZone):
    ALIAS = 'solar'
    INDEX = 5
    ASTEROID_DEFINITION_CLASS = StutSolarMines5


class StutSolarPlant1(StutMember, StutBaseSolarPlant):
    INDEX = 1
    BASE_INDEX = 61
    ASTEROID_ZONES = [
        StutSolarMinesZone1,
    ]


class StutSolarPlant2(StutMember, StutBaseSolarPlant):
    INDEX = 2
    BASE_INDEX = 62
    ASTEROID_ZONES = [
        StutSolarMinesZone2,
    ]


class StutSolarPlant3(StutMember, StutBaseSolarPlant):
    INDEX = 3
    BASE_INDEX = 63
    ASTEROID_ZONES = [
        StutSolarMinesZone3,
    ]


class StutSolarPlant4(StutMember, StutBaseSolarPlant):
    INDEX = 4
    BASE_INDEX = 64
    ASTEROID_ZONES = [
        StutSolarMinesZone4,
    ]


class StutSolarPlant5(StutMember, StutBaseSolarPlant):
    INDEX = 5
    BASE_INDEX = 65
    ASTEROID_ZONES = [
        StutSolarMinesZone5,
    ]


class StutSolarSupriseRewards(StutMember, mineable.DefaultSupriseRewardsGroup):
    NAME = 'rh_stut_solar_suprise'
    SOLAR = suprise.RheinlandMiscFighter
    REWARD_ITEM = None
    ULTRA_REWARD_BASES = [
        StutSolarPlant1,
        StutSolarPlant2,
        StutSolarPlant3,
        StutSolarPlant4,
        StutSolarPlant5,
    ]


class StutSolarSupriseField(mineable.DefaultField):
    BOX_SIZE = 400
    DENSITY_MULTIPLER = 4
    DRIFT_X = 0.5
    DRIFT_Y = 0.5
    DRIFT_Z = 0.5
    EMPTY_CHANCE = 0.2


class StutBaseSolarSupriseRewardField(mineable.SupriseRewardField):
    ALIAS = 'solar'
    FIELD_NAME = None
    FIELD_CLASS = StutSolarSupriseField
    REWARDS_GROUP_CLASS = StutSolarSupriseRewards
    ULTRA_REWARD = True


class StutSolarSupriseRewardField1(StutMember, StutBaseSolarSupriseRewardField):
    FIELD_NAME = 'rh_stut_suprise_field1'
    INDEX = 1
    ULTRA_BASE = StutSolarPlant1


class StutSolarSupriseRewardField2(StutMember, StutBaseSolarSupriseRewardField):
    FIELD_NAME = 'rh_stut_suprise_field2'
    INDEX = 2
    ULTRA_BASE = StutSolarPlant2


class StutSolarSupriseRewardField3(StutMember, StutBaseSolarSupriseRewardField):
    FIELD_NAME = 'rh_stut_suprise_field3'
    INDEX = 3
    ULTRA_BASE = StutSolarPlant3


class StutSolarSupriseRewardField4(StutMember, StutBaseSolarSupriseRewardField):
    FIELD_NAME = 'rh_stut_suprise_field4'
    INDEX = 4
    ULTRA_BASE = StutSolarPlant4


class StutSolarSupriseRewardField5(StutMember, StutBaseSolarSupriseRewardField):
    FIELD_NAME = 'rh_stut_suprise_field5'
    INDEX = 5
    ULTRA_BASE = StutSolarPlant5


class StutSun(StutMember, main_objects.Sun):
    STAR = 'med_orange_sun'
    LOADOUT = 'large_yellow_sun_fx'
    ATMOSHPERE_RANGE = 12000


class StutOmega15Jumpgate(StutMember, main_objects.Jumpgate):
    INDEX = 1
    REL = RIGHT


class StutOmega7Jumpgate(StutMember, main_objects.Jumpgate):
    INDEX = 2
    REL = LEFT


class StutDockring(StutMember, main_objects.Dockring):
    BASE_INDEX = 1
    REL = TOP
    AUDIO_PREFIX = SpaceVoice.RH_PLANET
    INTERIOR_CLASS = interior.CustomFullSplitRoomInterior
    DEALERS = dealers.RheinlandPlanetDealers


class StutPoliceOutpost(StutMember, main_objects.Outpost):
    BASE_INDEX = 2
    REL = TOP
    SPACE_OBJECT_TEMPLATE = police.StuttgartPoliceOutpost
    INTERIOR_CLASS = interior.OutpostShipdealerInterior
    AUDIO_PREFIX = SpaceVoice.BORDER_STATION
    DEALERS = dealers.RheinlandMilitaryDealers


class StutShipyard(StutMember, main_objects.Shipyard):
    BASE_INDEX = 3
    REL = LEFT
    SPACE_OBJECT_TEMPLATE = shipyards.StuttgartShipyard
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.RheinlandMilitaryDealers


class StutMegabase(StutMember, main_objects.Station):
    BASE_INDEX = 4
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = stuttgart_megabase.StuttgartMegabase
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.RheinlandCivilianDealers

    INTERIOR_BG1 = interior.INTERIOR_BG_WALKER

    NEBULA_EXCLUSION_ZONE_SIZE = 3500
    EXCLUSION_PARAMS = WALKER_EXCLUSION_PARAMS
    NEBULA_ZONES = [StutOrangeNebula1]


class StutTraders(StutMember, main_objects.TradingBase):
    BASE_INDEX = 5
    REL = TOP
    SPACE_OBJECT_TEMPLATE = bounty_hunter.ChurchAlive
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.RheinlandCivilianDealers


class StutLuxuryDockring(StutMember, main_objects.Dockring):
    INDEX = 2
    BASE_INDEX = 6
    REL = TOP
    AUDIO_PREFIX = SpaceVoice.RH_PLANET
    INTERIOR_CLASS = interior.CustomFullSingleRoomInterior
    DEALERS = dealers.RheinlandPlanetDealers


class StutNebulaPirates(StutMember, main_objects.PirateBase):
    BASE_INDEX = 7
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = pirate.PirateBaseStuttgart
    FACTION = faction.RX_GRP

    DEFENCE_LEVEL = None

    INTERIOR_BG1 = interior.INTERIOR_BG_WALKER

    AUDIO_PREFIX = SpaceVoice.OUTPOST
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.RheinlandPirateDealers


class StutJunkers(StutMember, main_objects.PirateBase):
    INDEX = 2
    BASE_INDEX = 8
    REL = TOP
    SPACE_OBJECT_TEMPLATE = junker.StuttgartJunker
    FACTION = faction.JUNK_GRP

    DEFENCE_LEVEL = None

    AUDIO_PREFIX = SpaceVoice.OUTPOST
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.RheinlandPirateDealers

    ASTEROID_ZONES = [
        StutDebrisZone1,
    ]


class StutPlanet1(StutMember, main_objects.Planet):
    ARCHETYPE = 'planet_earthcity_3000'
    SPHERE_RADIUS = 3000
    RELATED_DOCK_RING = StutDockring


class StutPlanet2(StutMember, main_objects.Planet):
    INDEX = 2
    ARCHETYPE = 'planet_watblucld_2000'
    SPHERE_RADIUS = 2000
    RELATED_DOCK_RING = StutLuxuryDockring


class StutPlanet3(StutMember, main_objects.Planet):
    INDEX = 3
    ARCHETYPE = 'planet_ice_grey_2000'
    SPHERE_RADIUS = 2000


class StutPoliceConn1(StutMember, main_objects.TradeConnection):
    OBJ_FROM = StutPoliceOutpost
    OBJ_TO = StutOmega7Jumpgate
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        StutJunkers,
    ]


class StutPoliceConn2(StutMember, main_objects.TradeConnection):
    OBJ_FROM = StutPoliceOutpost
    OBJ_TO = StutShipyard
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'B'


class StutPoliceConn3(StutMember, main_objects.TradeConnection):
    OBJ_FROM = StutPoliceOutpost
    OBJ_TO = StutDockring
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        StutJunkers,
    ]


class StutTradingConn1(StutMember, main_objects.TradeConnection):
    OBJ_FROM = StutTraders
    OBJ_TO = StutDockring
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        StutNebulaPirates,
    ]
    OBJ_TO_TLR_FORCE_OFFSET = (23000, 0, -38000)


class StutTradingConn2(StutMember, main_objects.TradeConnection):
    OBJ_FROM = StutTraders
    OBJ_TO = StutOmega15Jumpgate
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        StutNebulaPirates,
    ]


class StutTradingConn3(StutMember, main_objects.TradeConnection):
    OBJ_FROM = StutTraders
    OBJ_TO = StutMegabase
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'F'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        StutNebulaPirates,
    ]


class StutProductionConn1(StutMember, main_objects.TradeConnection):
    OBJ_FROM = StutShipyard
    OBJ_TO = StutMegabase
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'G'
    HUNTER_DEFENCE_REL = BOTTOM




class StutLuxuryConn1(StutMember, main_objects.TradeConnection):
    OBJ_FROM = StutDockring
    OBJ_TO = StutLuxuryDockring
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'H'
    HUNTER_DEFENCE_REL = LEFT

    OBJ_FROM_TLR_FORCE_OFFSET = (25000, 0, -42000)
