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
from templates.solar import hackable
from templates.solar import debris_box
from templates.solar import suprise
from templates.nebula import li_col_nebula
from templates.nebula import exclusion

from templates.dockable import astbase
from templates.dockable import shipyards
from templates.dockable import prisons
from templates.dockable import police
from templates.dockable import columbia_production
from templates.dockable import columbia_new_hope
from templates.dockable import junker
from templates.dockable import station_debris


class ColMember(Member):
    FACTION = faction.LibertyMain
    INTERIOR_BG1 = interior.INTERIOR_LI_COLUMBIA
    WEAPON_FACTION = WEAPON_LI
    EQUIP_FACTION = EQUIP_LI


class ColStaticText(ColMember, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = li_col
space_color = 25, 5, 20
local_faction = li_grp
space_farclip = 200000

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Dust]
spacedust = Dust

[Music]
space = music_li_space
danger = music_li_danger
battle = music_li_battle

[Ambient]
color = 20, 3, 16

[Background]
nebulae = solar\\stars_mod\\li_col_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_li_col_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
property_flags = 512 ;lava - MILITARY
;property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = li_col_system_light
pos = 0, 0, 0
color = 213, 233, 255
range = 100000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION
'''


class ColSun(ColMember, main_objects.Sun):
    STAR = 'lg_white_sun'
    LOADOUT = 'large_blue_sun_fx'



class ColBaseBlueNebula(zones.NebulaZone):
    SPACEDUST = Dust.ATTRACT
    SPACEDUST_MAXPARTICLES = 40
    MUSIC = Ambience.NEBULA_CROW
    INTERFERENCE = 0.5

    PROPERTY_FLAGS = 32768
    PROPERTY_FOG_COLOR = '150, 100, 20'


class ColLargeWestNebula(ColMember, ColBaseBlueNebula):
    INDEX = 1
    CONTENT_TEMPLATE = li_col_nebula.ColumbiaMainNebulaTemplate


class ColNorthNebula(ColMember, ColBaseBlueNebula):
    INDEX = 2
    CONTENT_TEMPLATE = li_col_nebula.ColumbiaSmallNebulaTemplate


CROW_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.CROW_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '255, 100, 235',
    'fog_far': 5000,
}


class ColDebrisZone1(ColMember, zones.DebrisZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class ColDebrisZone2(ColMember, zones.DebrisZone):
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class ColDebrisZone3(ColMember, zones.DebrisZone):
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class ColBaseDebrisManufactoring(main_objects.DebrisManufactoring):
    ALIAS = 'deb'
    ROTATE_RANDOM = True
    ARCHETYPE = 'mplatform'
    LOADOUT = 'mplatform_li_debris'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    AST_EXCLUSION_ZONE_SIZE = 2000
    AST_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.RADIOACTIVE_RED,
        'spacedust_maxparticles': 200,
    }


class ColDebrisFactory1(ColMember, ColBaseDebrisManufactoring):
    INDEX = 1
    BASE_INDEX = 51
    ASTEROID_ZONES = [
        ColDebrisZone1,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500
    RU_NAME = 'Плавильня Команчи'
    MISC_EQUIP_TYPE = LI_MAIN
    EQUIP_SET = markets.EquipSet(
        Q.Thruster(LI_PIRATE, eq_classes=markets.SECRET3),
        Q.Power(LI_PIRATE, eq_classes=markets.SECRET2),
    )


class ColDebrisFactory2(ColMember, ColBaseDebrisManufactoring):
    INDEX = 2
    BASE_INDEX = 52
    ASTEROID_ZONES = [
        ColDebrisZone2,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500
    RU_NAME = 'Плавильня Гейтсвилл'
    MISC_EQUIP_TYPE = LI_MAIN
    EQUIP_SET = markets.EquipSet(
        Q.Thruster(LI_CIV, eq_classes=markets.SECRET2),
        Q.Power(LI_MAIN, eq_classes=markets.SECRET3),
    )


class ColDebrisFactory3(ColMember, ColBaseDebrisManufactoring):
    INDEX = 3
    BASE_INDEX = 53
    ASTEROID_ZONES = [
        ColDebrisZone3,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500
    RU_NAME = 'Плавильня Олни'
    MISC_EQUIP_TYPE = LI_MAIN
    EQUIP_SET = markets.EquipSet(
        Q.Thruster(LI_CIV, eq_classes=markets.SECRET3),
        Q.Power(LI_PIRATE, eq_classes=markets.SECRET2),
    )


class ColDebrisBoxReward(ColMember, mineable.DefaultDebrisBoxRewardsGroup):
    NAME = 'li_col_debrisbox'
    SOLAR = debris_box.DebrisBox
    REWARD_ITEM = 'comm_scrap_metal'
    ULTRA_REWARD_BASES = [
        ColDebrisFactory1,
        ColDebrisFactory2,
        ColDebrisFactory3,
    ]


class ColBaseDebrisBoxRewardField(mineable.DebrisBoxRewardField):
    FIELD_CLASS = mineable.MineableDebrixBoxField
    REWARDS_GROUP_CLASS = ColDebrisBoxReward
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class ColDebrisBoxField1(ColMember, ColBaseDebrisBoxRewardField):
    INDEX = 1
    ULTRA_BASE = ColDebrisFactory1


class ColDebrisBoxField2(ColMember, ColBaseDebrisBoxRewardField):
    INDEX = 2
    ULTRA_BASE = ColDebrisFactory2


class ColDebrisBoxField3(ColMember, ColBaseDebrisBoxRewardField):
    INDEX = 3
    ULTRA_BASE = ColDebrisFactory3


class ColSpaceAsteroidDefinition(asteroid_definition.CaliforniaAsteroidDefinition):
    BELT = True
    BILLBOARDS = True
    DYNAST = True
    LOOT = False  # TEMP


class ColNebulaAsteroidDefinition(asteroid_definition.CaliforniaAsteroidDefinition):
    BELT = False
    BILLBOARDS = False
    DYNAST = True
    LOOT = False  # TEMP


class ColAsteroidZone1(ColMember, zones.AsteroidZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = ColSpaceAsteroidDefinition


class ColAsteroidZone2(ColMember, zones.AsteroidZone):
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = ColSpaceAsteroidDefinition


class ColAsteroidZone3(ColMember, zones.AsteroidZone):
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = ColNebulaAsteroidDefinition


class ColAbandonedAstBase1(ColMember, main_objects.AbandonedAsteroid):
    ALIAS = 'ast'
    INDEX = 1
    BASE_INDEX = 55
    ROTATE_RANDOM = True
    ARCHETYPE = 'miningbase_mineableA'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True
    RU_NAME = 'База Сансарк'

    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        ColAsteroidZone1,
    ]
    AST_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.ASTEROID,
        'spacedust_maxparticles': 200,
    }
    MISC_EQUIP_TYPE = LI_PIRATE
    WEAPON_FACTION = WEAPON_LI
    EQUIP_SET = markets.EquipSet(
        Q.Gun('li_roguegun', eq_classes=markets.SECRET3),
        Q.Engine(None, eq_classes=markets.SECRET3),
    )


class ColBackgroundAsteroidReward(ColMember, mineable.AsteroidRewardsGroupHigh):
    NAME = 'li_col_rewardast'
    SOLAR = asteroid.AsteroidCalifornia
    REWARD_ITEM = 'comm_roid_uranium'


class ColUnlockerAsteroidReward(ColMember, mineable.AsteroidRewardsGroupHigh):
    NAME = 'li_for_norewardast'
    SOLAR = asteroid.AsteroidCalifornia
    REWARD_ITEM = 'comm_roid_uranium'
    ULTRA_REWARD_BASES = [
        ColAbandonedAstBase1,
    ]


class ColMineableField(mineable.MineableAsteroidField):
    BOX_SIZE = 1400
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.3
    DRIFT_Y = 0
    DRIFT_Z = 0.3


class ColBackgroundAsteroidRewardField(mineable.AsteroidRewardField):
    ALIAS = 'ast'
    FIELD_CLASS = ColMineableField
    REWARDS_GROUP_CLASS = ColBackgroundAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25
    ULTRA_REWARD = False


class ColUnlockerAsteroidRewardField(mineable.AsteroidRewardField):
    ALIAS = 'ast'
    FIELD_CLASS = ColMineableField
    REWARDS_GROUP_CLASS = ColUnlockerAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class ColRewardAsteroids1(ColMember, ColUnlockerAsteroidRewardField):
    INDEX = 1
    ULTRA_BASE = ColAbandonedAstBase1


class ColRewardAsteroids2(ColMember, ColBackgroundAsteroidRewardField):
    INDEX = 2


class ColRewardAsteroids3(ColMember, ColBackgroundAsteroidRewardField):
    INDEX = 3


class ColBaseSolarPlant(main_objects.SolarPlant):
    ALIAS = 'solar'
    ROTATE_RANDOM = True
    ARCHETYPE = 'solar_plant_old'
    LOADOUT = 'solar_plant_li'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True
    AST_EXCLUSION_ZONE_SIZE = 600

    NEBULA_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.RADIOACTIVE_RED,
        'spacedust_maxparticles': 200,
    }


class ColBaseMinesZone(zones.AsteroidZone):
    ASTEROID_DEFINITION_CLASS = asteroid_definition.SpaceMines
    SPACEDUST = Dust.DEBRIS
    SPACEDUST_MAXPARTICLES = 100
    MUSIC = Ambience.MINE_AST
    INTERFERENCE = 0.1
    DRAG_MODIFIER = 1.5
    PROPERTY_FLAGS = 4128


class ColSolarMinesZone1(ColMember, ColBaseMinesZone):
    ALIAS = 'solar'
    INDEX = 1


class ColSolarMinesZone2(ColMember, ColBaseMinesZone):
    ALIAS = 'solar'
    INDEX = 2


class ColSolarMinesZone3(ColMember, ColBaseMinesZone):
    ALIAS = 'solar'
    INDEX = 3


class ColSolarMinesZone4(ColMember, ColBaseMinesZone):
    ALIAS = 'solar'
    INDEX = 4


class ColSolarMinesZone5(ColMember, ColBaseMinesZone):
    ALIAS = 'solar'
    INDEX = 5


class ColSolarPlant1(ColMember, ColBaseSolarPlant):
    INDEX = 1
    BASE_INDEX = 61
    ASTEROID_ZONES = [
        ColSolarMinesZone1,
    ]
    RU_NAME = 'Солн.генератор Ламеса'


class ColSolarPlant2(ColMember, ColBaseSolarPlant):
    INDEX = 2
    BASE_INDEX = 62
    ASTEROID_ZONES = [
        ColSolarMinesZone2,
    ]
    RU_NAME = 'Солн.генератор Монаханс'


class ColSolarPlant3(ColMember, ColBaseSolarPlant):
    INDEX = 3
    BASE_INDEX = 63
    ASTEROID_ZONES = [
        ColSolarMinesZone3,
    ]
    RU_NAME = 'Солн.генератор Андрус'


class ColSolarPlant4(ColMember, ColBaseSolarPlant):
    INDEX = 4
    BASE_INDEX = 64
    ASTEROID_ZONES = [
        ColSolarMinesZone4,
    ]
    RU_NAME = 'Солн.генератор Ранкин'


class ColSolarPlant5(ColMember, ColBaseSolarPlant):
    INDEX = 5
    BASE_INDEX = 65
    ASTEROID_ZONES = [
        ColSolarMinesZone5,
    ]
    RU_NAME = 'Солн.генератор Шеффилд'


class ColSolarSupriseRewards(ColMember, mineable.DefaultSupriseRewardsGroup):
    NAME = 'li_col_solar_suprise'
    SOLAR = suprise.LibertyMiscFighter
    REWARD_ITEM = None
    ULTRA_REWARD_BASES = [
        ColSolarPlant1,
        ColSolarPlant2,
        ColSolarPlant3,
        ColSolarPlant4,
        ColSolarPlant5,
    ]


class ColSolarSupriseField(mineable.DefaultField):
    BOX_SIZE = 400
    DENSITY_MULTIPLER = 4
    DRIFT_X = 0.5
    DRIFT_Y = 0.5
    DRIFT_Z = 0.5
    EMPTY_CHANCE = 0.2


class ColBaseSolarSupriseRewardField(mineable.SupriseRewardField):
    ALIAS = 'solar'
    FIELD_CLASS = ColSolarSupriseField
    REWARDS_GROUP_CLASS = ColSolarSupriseRewards
    ULTRA_REWARD = True


class ColSolarSupriseRewardField1(ColMember, ColBaseSolarSupriseRewardField):
    INDEX = 1
    ULTRA_BASE = ColSolarPlant1


class ColSolarSupriseRewardField2(ColMember, ColBaseSolarSupriseRewardField):
    INDEX = 2
    ULTRA_BASE = ColSolarPlant2


class ColSolarSupriseRewardField3(ColMember, ColBaseSolarSupriseRewardField):
    INDEX = 3
    ULTRA_BASE = ColSolarPlant3


class ColSolarSupriseRewardField4(ColMember, ColBaseSolarSupriseRewardField):
    INDEX = 4
    ULTRA_BASE = ColSolarPlant4


class ColSolarSupriseRewardField5(ColMember, ColBaseSolarSupriseRewardField):
    INDEX = 5
    ULTRA_BASE = ColSolarPlant5


class ColSig22Jumpgate(ColMember, main_objects.Jumpgate):
    INDEX = 1
    REL = BOTTOM
    TARGET_SYSTEM_NAME = 'sig22'


class ColTau31Jumpgate(ColMember, main_objects.Jumpgate):
    INDEX = 2
    REL = TOP
    TARGET_SYSTEM_NAME = 'tau31'


class ColDockring(ColMember, main_objects.LargePlanetDockring):
    BASE_INDEX = 1
    REL = BOTTOM
    AUDIO_PREFIX = SpaceVoice.LI_PLANET
    INTERIOR_CLASS = interior.CustomFullSplitRoomInterior
    DEALERS = dealers.LibertyPlanetDealers
    SHIP_SET = markets.ShipSet('bh_fighter', 'bh_elite2', 'bw_freighter')
    RU_NAME = 'Планета Колумбия'

    BASE_PROPS = meta.LargePlanet(
        objectives=[
            meta.ProduceBest(JUMPGATE_PARTS),
            meta.ProduceBest(MINING_EQUIPMENT),
            meta.ProduceCheap(MOX_FUEL),
            meta.ProduceNormal(PROD_MACHINES),
            meta.ProduceNormal(SMELTER_PARTS),
        ]
    )


class ColMiningDockring(ColMember, main_objects.MiningPlanetDockring):
    INDEX = 2
    BASE_INDEX = 2
    REL = LEFT
    AUDIO_PREFIX = SpaceVoice.LI_PLANET
    INTERIOR_CLASS = interior.CustomFullSingleRoomInterior
    DEALERS = dealers.LibertyPlanetDealers
    SHIP_SET = markets.ShipSet('ge_fighter3')
    RU_NAME = 'Планета Хьюстон'

    BASE_PROPS = meta.MiningPlanet(
        objectives=[
            meta.ProduceNormal(DIAMONDS),
            meta.ProduceBad(NIOBIUM),
            meta.ProduceBad(GOLD),
        ]
    )


class ColShipyard(ColMember, main_objects.Shipyard):
    BASE_INDEX = 3
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = shipyards.StuttgartShipyard
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.LibertyCivilianDealers
    RU_NAME = 'Верфь Портленд'


class ColPrison(ColMember, main_objects.Prison):
    BASE_INDEX = 4
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = prisons.ColumbiaPrison
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.LibertyMilitaryDealers
    RU_NAME = 'Тюрьма Бомонт'


class ColPolice(ColMember, main_objects.Outpost):
    ALIAS = 'police'
    BASE_INDEX = 5
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = police.PoliceOutpostLiberty
    INTERIOR_CLASS = interior.OutpostInterior
    AUDIO_PREFIX = SpaceVoice.BORDER_STATION
    DEALERS = dealers.LibertyMilitaryDealers
    RU_NAME = 'Аванпост Новый Орлеан'


class ColProduction(ColMember, main_objects.Refinery):
    ALIAS = 'station'
    BASE_INDEX = 6
    REL = BOTTOM
    REL_APPEND = 2500
    SPACE_OBJECT_TEMPLATE = columbia_production.ColumbiaProduction
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.LibertyCivilianDealers

    EXCLUSION_PARAMS = CROW_EXCLUSION_PARAMS
    NEBULA_ZONES = [ColLargeWestNebula]
    NEBULA_EXCLUSION_ZONE_SIZE = 4000

    RU_NAME = 'Станция Даллас'

    BASE_PROPS = meta.Refinery(
        objectives=[
            meta.ProduceBest(ALLOY_TEMPERATURE),
            meta.ProduceBad(ALLOY_HEAVY),
            meta.ProduceBad(ALLOY_CONDUCTOR),
            meta.ProduceBad(ALLOY_RADIATION),
        ]
    )


class ColTrading(ColMember, main_objects.TradingBase):
    BASE_INDEX = 7
    REL = BOTTOM
    REL_APPEND = 2500
    SPACE_OBJECT_TEMPLATE = columbia_new_hope.ColumbiaNewHope
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.LibertyCivilianDealers
    RU_NAME = 'Торговая база Сиетл'


class ColPlanet1(ColMember, main_objects.Planet):
    ARCHETYPE = 'planet_earthind_4000'
    SPHERE_RADIUS = 4000
    RELATED_DOCK_RING = ColDockring


class ColPlanet2(ColMember, main_objects.Planet):
    INDEX = 2
    ARCHETYPE = 'planet_icemntcld_2500'
    SPHERE_RADIUS = 2500
    RELATED_DOCK_RING = ColMiningDockring

#
# class ColPlanet3(ColMember, main_objects.Planet):
#     INDEX = 3
#     ARCHETYPE = 'planet_gasgrncld_3000'
#     SPHERE_RADIUS = 3000


class ColPlanet4(ColMember, main_objects.Planet):
    INDEX = 4
    ARCHETYPE = 'planet_ice_blue_3000'
    SPHERE_RADIUS = 3000
    RU_NAME = 'Планета Аризона'


class ColOldTradingBaseRuins(ColMember, main_objects.StationRuins):
    ALIAS = 'ruins'
    INDEX = 1
    REL = LEFT

    RU_NAME = 'Фрипорт 1'

    SPACE_OBJECT_TEMPLATE = station_debris.ColumbiaDebris
    ASTEROID_ZONES = [
        ColAsteroidZone3,
    ]

    EXCLUSION_PARAMS = CROW_EXCLUSION_PARAMS
    NEBULA_ZONES = [ColLargeWestNebula]
    NEBULA_EXCLUSION_ZONE_SIZE = 3000


class ColOldTradingBaseRuinsSuprisePoint1(ColMember, main_objects.HackableStation):
    ALIAS = 'ruins_dock'
    INDEX = 1
    BASE_INDEX = 71
    RELATED_OBJECT = ColOldTradingBaseRuins
    RELATED_OBJECT_INDEX = 0
    HACKABLE_SOLAR_CLASS = hackable.HackableOutpost
    INTERIOR_CLASS = interior.EquipDeckInterior

    RU_NAME = 'Стыковочный узел 1 фрипорта 1'
    MISC_EQUIP_TYPE = LI_MAIN
    WEAPON_FACTION = WEAPON_LI
    EQUIP_SET = markets.EquipSet(
        Q.GenericLauncher(FAST_MISSILE, eq_classes=markets.MISSILE),
        Q.Engine(LI_MAIN, eq_classes=markets.SECRET2),
    )


class ColOldTradingBaseRuinsSuprisePoint2(ColMember, main_objects.HackableStation):
    ALIAS = 'ruins_dock'
    INDEX = 2
    BASE_INDEX = 72
    RELATED_OBJECT = ColOldTradingBaseRuins
    RELATED_OBJECT_INDEX = 1
    HACKABLE_SOLAR_CLASS = hackable.HackableOutpost
    INTERIOR_CLASS = interior.EquipDeckInterior

    RU_NAME = 'Стыковочный узел 2 фрипорта 1'
    MISC_EQUIP_TYPE = LI_MAIN
    WEAPON_FACTION = WEAPON_LI
    EQUIP_SET = markets.EquipSet(
        Q.GenericLauncher(TORPEDO_MISSILE, eq_classes=markets.MISSILE),
        Q.Engine(LI_MAIN, eq_classes=markets.SECRET3),
    )


class ColAsteroidPirates(ColMember, main_objects.PirateAsteroid):
    INDEX = 2
    BASE_INDEX = 8
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = astbase.BerlinAsteroidBase
    FACTION = faction.LibertyPirate

    DEFENCE_LEVEL = None
    RU_NAME = 'База Вестпорт'

    AUDIO_PREFIX = SpaceVoice.OUTPOST
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.LibertyPirateDealers

    ASTEROID_ZONES = [
        ColAsteroidZone2
    ]
    AST_EXCLUSION_ZONE_SIZE = 3000


class ColNebulaPirates(ColMember, main_objects.PirateStation):
    INDEX = 1
    BASE_INDEX = 9
    REL = TOP
    SPACE_OBJECT_TEMPLATE = junker.BerlinJunker
    FACTION = faction.LibertyPirate
    RU_NAME = 'База Пальмито'

    DEFENCE_LEVEL = None

    AUDIO_PREFIX = SpaceVoice.OUTPOST
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.LibertyPirateDealers

    NEBULA_ZONES = [
        ColNorthNebula
    ]
    EXCLUSION_PARAMS = CROW_EXCLUSION_PARAMS


class ColShipyardConn1(ColMember, main_objects.TradeConnection):
    OBJ_FROM = ColTau31Jumpgate
    OBJ_TO = ColShipyard
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        ColNebulaPirates
    ]


class ColShipyardConn2(ColMember, main_objects.TradeConnection):
    OBJ_FROM = ColShipyard
    OBJ_TO = ColPrison
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        ColNebulaPirates
    ]


class ColShipyardConn3(ColMember, main_objects.TradeConnection):
    OBJ_FROM = ColTrading
    OBJ_TO = ColShipyard
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        ColNebulaPirates
    ]


class ColTradingConn1(ColMember, main_objects.TradeConnection):
    OBJ_FROM = ColMiningDockring
    OBJ_TO = ColTrading
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        ColNebulaPirates
    ]


class ColTradingConn2(ColMember, main_objects.TradeConnection):
    OBJ_FROM = ColTrading
    OBJ_TO = ColProduction
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        ColAsteroidPirates
    ]


class ColMainPlanetConn1(ColMember, main_objects.TradeConnection):
    OBJ_FROM = ColPrison
    OBJ_TO = ColDockring
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'F'


class ColMainPlanetConn2(ColMember, main_objects.TradeConnection):
    OBJ_FROM = ColPolice
    OBJ_TO = ColDockring
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'G'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        ColAsteroidPirates
    ]


class ColPoliceConn1(ColMember, main_objects.TradeConnection):
    OBJ_FROM = ColProduction
    OBJ_TO = ColPolice
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'H'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        ColNebulaPirates
    ]


class ColPoliceConn2(ColMember, main_objects.TradeConnection):
    OBJ_FROM = ColPolice
    OBJ_TO = ColSig22Jumpgate
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'K'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        ColAsteroidPirates
    ]


class ColRuinsConn1(ColMember, main_objects.BrokenTradeConnection):
    OBJ_FROM = ColMiningDockring
    OBJ_TO = ColOldTradingBaseRuins
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'I'


class ColRuinsConn2(ColMember, main_objects.BrokenTradeConnection):
    OBJ_FROM = ColOldTradingBaseRuins
    OBJ_TO = ColProduction
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'J'
    OBJ_TO_TLR_FORCE_OFFSET = (-53000, 0, 17500)
