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
from universe.audio.space_voice import SpaceVoice
from universe import faction
from universe.content import mineable
from templates.solar import asteroid
from templates.solar import debris_box
from templates.solar import hackable
from templates.nebula import br_cam_nebula
from templates.nebula import exclusion

from templates.dockable import pirate
from templates.dockable import junker
from templates.dockable import columbia_production
from templates.dockable import trade_storages
from templates.dockable import police
from templates.dockable import shipyards
from templates.dockable import cambridge_research
from templates.dockable import station_debris


class CamMember(Member):
    FACTION = faction.BretoniaMain
    WEAPON_FACTION = WEAPON_BR
    EQUIP_FACTION = EQUIP_BR


class CamStaticText(CamMember, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = br_cam
space_color = 0, 0, 0 ;3, 5, 8
local_faction = br_grp
space_farclip = 100000

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Music]
space = music_br_space
danger = music_br_danger
battle = music_br_battle

[Dust]
spacedust = Dust

[Ambient]
color = 10, 18, 20

[Background]
nebulae = solar\\stars_mod\\br_cam_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_br_cam_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
property_flags = 512 ;lava - MILITARY
;property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = br_cam_system_light
pos = 0, 0, 0
color = 255, 255, 255
range = 150000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION
'''


CROW_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.CROW_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '240, 240, 160',
    'fog_far': 5000,
}


class CamTopNebula(CamMember, zones.NebulaZone):
    INDEX = 1
    MUSIC = Ambience.NEBULA_BARRIER
    CONTENT_TEMPLATE = br_cam_nebula.CambridgeNebulaTemplate

    PROPERTY_FLAGS = 32768
    PROPERTY_FOG_COLOR = '0, 255, 0'


class CamBottomNebula(CamMember, zones.NebulaZone):
    INDEX = 2
    MUSIC = Ambience.NEBULA_BARRIER
    CONTENT_TEMPLATE = br_cam_nebula.CambridgeNebulaTemplate

    PROPERTY_FLAGS = 32768
    PROPERTY_FOG_COLOR = '0, 255, 0'


class CamAsteroidDefinition(asteroid_definition.Tau37AsteroidDefinition):
    DYNAST = True
    BELT = True
    BILLBOARDS = True
    LOOT = False  # TEMP


class CamBaseVanillaAstZone(zones.AsteroidZone):
    SPACEDUST = Dust.ASTEROID
    SPACEDUST_MAXPARTICLES = 100
    MUSIC = Ambience.AST_ROCK
    ASTEROID_DEFINITION_CLASS = CamAsteroidDefinition


class CamAsteroidZone1(CamMember, CamBaseVanillaAstZone):
    INDEX = 1


class CamAsteroidZone2(CamMember, CamBaseVanillaAstZone):
    INDEX = 2


class CamAsteroidZone3(CamMember, CamBaseVanillaAstZone):
    INDEX = 3


class CamAsteroidZone4(CamMember, CamBaseVanillaAstZone):
    INDEX = 4


class CamEastAsteroidReward(CamMember, mineable.AsteroidRewardsGroupMedium):
    NAME = 'Cam_east_ast'
    SOLAR = asteroid.AsteroidOmega15
    REWARD_ITEM = 'comm_roid_niobium'


class CamLargeAsteroids2(CamMember, mineable.AsteroidRewardField):
    INDEX = 2
    FIELD_CLASS = mineable.BackgroundAsteroidsField
    REWARDS_GROUP_CLASS = CamEastAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25


class CamLargeAsteroids3(CamMember, mineable.AsteroidRewardField):
    INDEX = 3
    FIELD_CLASS = mineable.BackgroundAsteroidsField
    REWARDS_GROUP_CLASS = CamEastAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25


class CamLargeAsteroids4(CamMember, mineable.AsteroidRewardField):
    INDEX = 4
    FIELD_CLASS = mineable.BackgroundAsteroidsField
    REWARDS_GROUP_CLASS = CamEastAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25


class CamSun(CamMember, main_objects.Sun):
    STAR = 'med_white_sun'
    LOADOUT = 'med_blue_sun_fx'


class CamTau37Jumpgate(CamMember, main_objects.Jumpgate):
    INDEX = 1
    REL = TOP
    TARGET_SYSTEM_NAME = 'tau37'


class CamTau29Jumpgate(CamMember, main_objects.Jumpgate):
    INDEX = 2
    REL = BOTTOM
    TARGET_SYSTEM_NAME = 'tau29'


class CamDebrisField(mineable.DefaultField):
    BOX_SIZE = 1200
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.2
    DRIFT_Y = 0.1
    DRIFT_Z = 0.2


class CamDebrisZone1(CamMember, zones.DebrisZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class CamDebrisZone2(CamMember, zones.DebrisZone):
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class CamDebrisZone3(CamMember, zones.DebrisZone):
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class CamDebrisZone4(CamMember, zones.DebrisZone):
    INDEX = 4
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class CamBaseDebrisManufactoring(main_objects.DebrisManufactoring):
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


class CamDebrisFactory1(CamMember, CamBaseDebrisManufactoring):
    INDEX = 1
    BASE_INDEX = 51
    ASTEROID_ZONES = [
        CamDebrisZone1,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500
    RU_NAME = 'Плавильня Ботри'


class CamDebrisFactory2(CamMember, CamBaseDebrisManufactoring):
    INDEX = 2
    BASE_INDEX = 52
    ASTEROID_ZONES = [
        CamDebrisZone2,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500
    RU_NAME = 'Плавильня Кеттон'


class CamDebrisFactory3(CamMember, CamBaseDebrisManufactoring):
    INDEX = 3
    BASE_INDEX = 53
    ASTEROID_ZONES = [
        CamDebrisZone3,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500
    RU_NAME = 'Плавильня Анкастер'


class CamDebrisBoxReward(CamMember, mineable.DefaultDebrisBoxRewardsGroup):
    NAME = 'br_cam_debrisbox'
    SOLAR = debris_box.DebrisBox
    REWARD_ITEM = 'comm_scrap_metal'
    ULTRA_REWARD_BASES = [
        CamDebrisFactory1,
        CamDebrisFactory2,
        CamDebrisFactory3,
    ]


class CamBaseDebrisBoxRewardField(mineable.DebrisBoxRewardField):
    FIELD_CLASS = mineable.MineableDebrixBoxField
    REWARDS_GROUP_CLASS = CamDebrisBoxReward
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class CamDebrisBoxField1(CamMember, CamBaseDebrisBoxRewardField):
    INDEX = 1
    ULTRA_BASE = CamDebrisFactory1


class CamDebrisBoxField2(CamMember, CamBaseDebrisBoxRewardField):
    INDEX = 2
    ULTRA_BASE = CamDebrisFactory2


class CamDebrisBoxField3(CamMember, CamBaseDebrisBoxRewardField):
    INDEX = 3
    ULTRA_BASE = CamDebrisFactory3


class CamBattleshipRuins1(CamMember, main_objects.HackableBattleship):
    ALIAS = 'ast'
    INDEX = 2
    BASE_INDEX = 65
    HACKABLE_SOLAR_CLASS = hackable.HackableBretoniaBattleship
    INTERIOR_CLASS = interior.EquipDeckInterior

    ASTEROID_ZONES = [
        CamAsteroidZone2,
    ]
    RU_NAME = 'Линкор Титаник'


class CamBattleshipRuins2(CamMember, main_objects.HackableBattleship):
    ALIAS = 'ast'
    INDEX = 3
    BASE_INDEX = 66
    HACKABLE_SOLAR_CLASS = hackable.HackableBretoniaBattleship
    INTERIOR_CLASS = interior.EquipDeckInterior

    ASTEROID_ZONES = [
        CamAsteroidZone2,
    ]
    RU_NAME = 'Линкор Бриттаник'


class CamBattleshipRuins3(CamMember, main_objects.HackableBattleship):
    ALIAS = 'ast'
    INDEX = 4
    BASE_INDEX = 67
    HACKABLE_SOLAR_CLASS = hackable.HackableBretoniaBattleship
    INTERIOR_CLASS = interior.EquipDeckInterior

    ASTEROID_ZONES = [
        CamAsteroidZone2,
    ]
    RU_NAME = 'Линкор Олимпик'


class CamOldOutpostRuins(CamMember, main_objects.StationRuins):
    ALIAS = 'ruins'
    INDEX = 1
    REL = RIGHT

    RU_NAME = 'Аванпост Мерсия'

    SPACE_OBJECT_TEMPLATE = station_debris.StuttgartDestroyedOutpost

    ASTEROID_ZONES = [
        CamAsteroidZone1,
    ]


class CamOldOutpostRuinsSuprisePoint(CamMember, main_objects.HackableStation):
    ALIAS = 'ruins_dock'
    INDEX = 1
    BASE_INDEX = 61
    RELATED_OBJECT = CamOldOutpostRuins
    HACKABLE_SOLAR_CLASS = hackable.HackableOutpost
    INTERIOR_CLASS = interior.EquipDeckInterior

    RU_NAME = 'Стыковочный узел Мерсии'


class CamDockring(CamMember, main_objects.LargePlanetDockring):
    BASE_INDEX = 1
    REL = BOTTOM
    AUDIO_PREFIX = SpaceVoice.BR_PLANET
    INTERIOR_CLASS = interior.CustomFullSplitRoomInterior
    DEALERS = dealers.BretoniaPlanetDealers
    SHIP_SET = markets.ShipSet('br_fighter', 'ge_fighter3', 'bw_freighter')
    RU_NAME = 'Планета Кембридж'

    BASE_PROPS = meta.LargePlanet(
        objectives=[
            meta.ProduceBest(LUXURY_FOOD),
            meta.ProduceBest(MOX_FUEL),
            meta.ProduceCheap(POLYMERS),
            meta.ProduceNormal(SOLAR_PLANT_PARTS),
            meta.ProduceNormal(OPTICAL_CHIPS),
            meta.ProduceBad(PROD_MACHINES),
            meta.ProduceBad(WATER_EXTRA),
        ]
    )


class CamStation(CamMember, main_objects.TradelaneSupportStation):
    INDEX = 1
    BASE_INDEX = 2
    REL = LEFT

    ARCHETYPE = 'largestation1_old'
    LOADOUT = 'largestation_br'

    AUDIO_PREFIX = SpaceVoice.STATION
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.BretoniaCivilianDealers

    RU_NAME = 'Станция Шеффилд'


class CamTrading(CamMember, main_objects.TradingBase):
    INDEX = 1
    BASE_INDEX = 3
    REL = LEFT

    SPACE_OBJECT_TEMPLATE = trade_storages.TekagiStorage

    AUDIO_PREFIX = SpaceVoice.OUTPOST
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.BretoniaCivilianDealers

    RU_NAME = 'Станция Челтнем'


class CamShipyard(CamMember, main_objects.Shipyard):
    INDEX = 1
    BASE_INDEX = 4
    REL = TOP

    SPACE_OBJECT_TEMPLATE = shipyards.CambridgeShipyard

    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.BretoniaCivilianDealers

    RU_NAME = 'Верфь Кардифф'


class CamPolice(CamMember, main_objects.Outpost):
    ALIAS = 'police'
    INDEX = 1
    BASE_INDEX = 5
    REL = TOP

    SPACE_OBJECT_TEMPLATE = police.PoliceOutpostBretonia

    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.BretoniaMilitaryDealers

    RU_NAME = 'Аванпост Блекпул'


class CamRefinery(CamMember, main_objects.Refinery):
    INDEX = 1
    BASE_INDEX = 6
    REL = LEFT

    RU_NAME = 'Станция Дерби'

    SPACE_OBJECT_TEMPLATE = columbia_production.ColumbiaSmallProduction

    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.BretoniaCivilianDealers

    BASE_PROPS = meta.Refinery(
        objectives=[
            meta.ProduceBest(ALLOY_RADIATION),
            meta.ProduceBad(ALLOY_TEMPERATURE),
        ]
    )


class CamResearch(CamMember, main_objects.ResearchStation):
    ALIAS = 'research'
    INDEX = 1
    BASE_INDEX = 7
    REL = LEFT
    RU_NAME = 'Станция Гринвич'

    SPACE_OBJECT_TEMPLATE = cambridge_research.CambridgeResearch

    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.BretoniaCivilianDealers

    BASE_PROPS = meta.Research(
        objectives=[
            meta.HaveSolarPanels(),
            meta.HaveGreenhouse(),
        ]
    )


class CamJunkers(CamMember, main_objects.JunkerBase):
    INDEX = 1
    BASE_INDEX = 8
    ALIAS = 'pirate'
    REL = LEFT
    SPACE_OBJECT_TEMPLATE = junker.HonshuJunker
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.BretoniaPirateDealers
    FACTION = faction.BretoniaPirate
    AST_EXCLUSION_ZONE_SIZE = 2500
    ASTEROID_ZONES = [
        CamDebrisZone4
    ]
    DEFENCE_LEVEL = None

    RU_NAME = 'База Спалдинг'


class CamPirates(CamMember, main_objects.PirateStation):
    INDEX = 2
    BASE_INDEX = 9
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = pirate.PirateBaseStuttgart
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.BretoniaPirateDealers
    FACTION = faction.BretoniaPirate
    NEBULA_EXCLUSION_ZONE_SIZE = 2000
    NEBULA_ZONES = [
        CamBottomNebula
    ]
    EXCLUSION_PARAMS = CROW_EXCLUSION_PARAMS
    DEFENCE_LEVEL = None

    RU_NAME = 'База Корк'


class CamPlanet1(CamMember, main_objects.Planet):
    INDEX = 1
    ARCHETYPE = 'planet_earth_3000'
    SPHERE_RADIUS = 3000
    RELATED_DOCK_RING = CamDockring


class CamPlanet2(CamMember, main_objects.Planet):
    INDEX = 2
    ARCHETYPE = 'planet_desorgrck_3000'
    SPHERE_RADIUS = 3000
    RU_NAME = 'Планета Саффолк'


class CamPlanet3(CamMember, main_objects.Planet):
    INDEX = 3
    ARCHETYPE = 'planet_ice_blue_3000'
    SPHERE_RADIUS = 3000
    RU_NAME = 'Планета Тетфорд'


class CamPlanet4(CamMember, main_objects.Planet):
    INDEX = 4
    ARCHETYPE = 'planet_gasgrncld_3000'
    SPHERE_RADIUS = 3000
    RU_NAME = 'Планета Манея'


class CamPlanetConn1(CamMember, main_objects.TradeConnection):
    OBJ_FROM = CamRefinery
    OBJ_TO = CamDockring
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        CamJunkers,
    ]


class CamPlanetConn2(CamMember, main_objects.TradeConnection):
    OBJ_FROM = CamDockring
    OBJ_TO = CamStation
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        CamPirates,
    ]


class CamPlanetConn3(CamMember, main_objects.TradeConnection):
    OBJ_FROM = CamTrading
    OBJ_TO = CamDockring
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        CamJunkers,
    ]


class CamShipyardConn1(CamMember, main_objects.TradeConnection):
    OBJ_FROM = CamTau37Jumpgate
    OBJ_TO = CamShipyard
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        CamJunkers,
    ]


class CamShipyardConn2(CamMember, main_objects.TradeConnection):
    OBJ_FROM = CamShipyard
    OBJ_TO = CamTrading
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        CamJunkers,
    ]


class CamShipyardConn3(CamMember, main_objects.TradeConnection):
    OBJ_FROM = CamResearch
    OBJ_TO = CamShipyard
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'F'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        CamJunkers,
    ]


class CamShipyardConn4(CamMember, main_objects.TradeConnection):
    OBJ_FROM = CamShipyard
    OBJ_TO = CamPolice
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'G'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        CamPirates,
    ]


class CamStationConn1(CamMember, main_objects.TradeConnection):
    OBJ_FROM = CamStation
    OBJ_TO = CamTau29Jumpgate
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'H'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        CamPirates,
    ]


class CamBrokenConn1(CamMember, main_objects.BrokenTradeConnection):
    OBJ_FROM = CamPolice
    OBJ_TO = CamOldOutpostRuins
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'I'
    ATTACKED_BY = [
        CamPirates,
    ]


class CamBrokenConn2(CamMember, main_objects.BrokenTradeConnection):
    OBJ_FROM = CamPolice
    OBJ_TO = CamOldOutpostRuins
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'J'
    ATTACKED_BY = [
        CamPirates,
    ]


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


class CamGasPockets(asteroid_definition.AsteroidDefinition):
    FIELD = True
    CUBE = True
    FIELD_TEMPLATE = FIELD_TEMPLATE
    CUBE_TEMPLATE = CUBE_TEMPLATE


class CamGasPocketsZone1(CamMember, zones.AsteroidZone):
    ALIAS = 'pocket'
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = CamGasPockets
    SPACEDUST = Dust.RADIOACTIVE_RED
    SPACEDUST_MAXPARTICLES = 200


class CamAbandonedStation(CamMember, main_objects.StationRuins):
    ALIAS = 'ruins'
    INDEX = 2
    REL = RIGHT

    SPACE_OBJECT_TEMPLATE = station_debris.OmegaDanzigDebrisAlternative

    ASTEROID_ZONES = [
        CamGasPocketsZone1,
    ]
    AST_EXCLUSION_ZONE_SIZE = 4000

    NEBULA_EXCLUSION_ZONE_SIZE = 2000
    EXCLUSION_PARAMS = CROW_EXCLUSION_PARAMS
    NEBULA_ZONES = [
        CamTopNebula,
    ]

    RU_NAME = 'Станция Оксфорд'


class CamAbandonedStationSuprisePoint1(CamMember, main_objects.HackableStation):
    ALIAS = 'ruins_dock'
    INDEX = 3
    BASE_INDEX = 71
    RELATED_OBJECT = CamAbandonedStation
    RELATED_OBJECT_INDEX = 0
    HACKABLE_SOLAR_CLASS = hackable.HackableOutpost
    INTERIOR_CLASS = interior.EquipDeckInterior

    RU_NAME = 'Исследовательский блок 1 Оксфорда'


class CamAbandonedStationSuprisePoint2(CamMember, main_objects.HackableStation):
    ALIAS = 'ruins_dock'
    INDEX = 4
    BASE_INDEX = 72
    RELATED_OBJECT = CamAbandonedStation
    RELATED_OBJECT_INDEX = 1
    HACKABLE_SOLAR_CLASS = hackable.HackableOutpost
    INTERIOR_CLASS = interior.EquipDeckInterior

    RU_NAME = 'Исследовательский блок 2 Оксфорда'
