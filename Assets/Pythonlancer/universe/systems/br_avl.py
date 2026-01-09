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
from templates.solar import suprise


from templates.dockable import pirate
from templates.dockable import junker
from templates.dockable import avalon_megabase
from templates.dockable import trade_storages
from templates.dockable import police
from templates.dockable import shipyards
from templates.dockable import prisons

from story.ingame.names import PRINCE_OF_WALES, MSG_PRINCE_OF_WALES
from text.strings import MultiString as MS


class AvalMember(Member):
    FACTION = faction.BretoniaMain
    WEAPON_FACTION = WEAPON_BR
    EQUIP_FACTION = EQUIP_BR
    INTERIOR_BG1 = interior.INTERIOR_BR_AVALON


class AvalStaticText(AvalMember, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = br_avl
space_color = 5, 5, 15
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
color = 10, 10, 25

[Background]
nebulae = solar\\stars_mod\\br_avl_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_br_avl_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
property_flags = 512 ;lava - MILITARY
;property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = Br_avl_system_light
pos = 0, 0, 0
color = 253, 230, 180
range = 120000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION
'''


class AvalSun(AvalMember, main_objects.Sun):
    STAR = 'br01_sun'
    LOADOUT = 'med_yellow_sun_fx'


class AvalDebrisZone1(AvalMember, zones.DebrisZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class AvalDebrisZone2(AvalMember, zones.DebrisZone):
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class AvalDebrisZone3(AvalMember, zones.DebrisZone):
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class AvalBaseDebrisManufactoring(main_objects.DebrisManufactoring):
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


class AvalDebrisFactory1(AvalMember, AvalBaseDebrisManufactoring):
    INDEX = 1
    BASE_INDEX = 51
    ASTEROID_ZONES = [
        AvalDebrisZone2,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500
    RU_NAME = MS('Плавильня Стокпорт', "Stockport Smelter")
    MISC_EQUIP_TYPE = BR_MAIN
    EQUIP_SET = markets.EquipSet(
        Q.Thruster(BR_CIV, eq_classes=markets.SECRET2),
        Q.Power(BR_MAIN, eq_classes=markets.SECRET3),
    )


class AvalDebrisFactory2(AvalMember, AvalBaseDebrisManufactoring):
    INDEX = 2
    BASE_INDEX = 52
    ASTEROID_ZONES = [
        AvalDebrisZone3,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500
    RU_NAME = MS('Плавильня Олдем', "Oldham Smelter")
    MISC_EQUIP_TYPE = BR_MAIN
    EQUIP_SET = markets.EquipSet(
        Q.Thruster(BR_CIV, eq_classes=markets.SECRET3),
        Q.Power(BR_PIRATE, eq_classes=markets.SECRET2),
    )


class AvalDebrisBoxReward(AvalMember, mineable.DefaultDebrisBoxRewardsGroup):
    NAME = 'br_avl_debrisbox'
    SOLAR = debris_box.DebrisBox
    REWARD_ITEM = 'comm_scrap_metal'
    ULTRA_REWARD_BASES = [
        AvalDebrisFactory1,
        AvalDebrisFactory2,
    ]


class AvalBaseDebrisBoxRewardField(mineable.DebrisBoxRewardField):
    FIELD_CLASS = mineable.MineableDebrixBoxField
    REWARDS_GROUP_CLASS = AvalDebrisBoxReward
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class AvalDebrisBoxField1(AvalMember, AvalBaseDebrisBoxRewardField):
    INDEX = 1
    ULTRA_BASE = AvalDebrisFactory1


class AvalDebrisBoxField2(AvalMember, AvalBaseDebrisBoxRewardField):
    INDEX = 2
    ULTRA_BASE = AvalDebrisFactory2


class AvalBaseSolarPlant(main_objects.SolarPlant):
    ALIAS = 'solar'
    ROTATE_RANDOM = True
    ARCHETYPE = 'solar_plant_old'
    LOADOUT = 'solar_plant_br'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True
    AST_EXCLUSION_ZONE_SIZE = 600

    NEBULA_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.RADIOACTIVE_RED,
        'spacedust_maxparticles': 200,
    }


class AvalBaseMinesZone(zones.AsteroidZone):
    ASTEROID_DEFINITION_CLASS = asteroid_definition.SpaceMines
    SPACEDUST = Dust.DEBRIS
    SPACEDUST_MAXPARTICLES = 100
    MUSIC = Ambience.MINE_AST
    INTERFERENCE = 0.1
    DRAG_MODIFIER = 1.5
    PROPERTY_FLAGS = 4128


class AvalSolarMinesZone1(AvalMember, AvalBaseMinesZone):
    ALIAS = 'solar'
    INDEX = 1


class AvalSolarMinesZone2(AvalMember, AvalBaseMinesZone):
    ALIAS = 'solar'
    INDEX = 2


class AvalSolarMinesZone3(AvalMember, AvalBaseMinesZone):
    ALIAS = 'solar'
    INDEX = 3


class AvalSolarMinesZone4(AvalMember, AvalBaseMinesZone):
    ALIAS = 'solar'
    INDEX = 4


class AvalSolarMinesZone5(AvalMember, AvalBaseMinesZone):
    ALIAS = 'solar'
    INDEX = 5


class AvalSolarPlant1(AvalMember, AvalBaseSolarPlant):
    INDEX = 1
    BASE_INDEX = 61
    ASTEROID_ZONES = [
        AvalSolarMinesZone1,
    ]
    RU_NAME = MS('Солн.генератор Тидворт', 'Solar Plant Titword')
    MISC_EQUIP_TYPE = BR_PIRATE
    EQUIP_SET = markets.EquipSet(
        Q.Power(BR_CIV, eq_classes=markets.SECRET3),
        Q.Shield(BR_PIRATE, eq_classes=markets.SECRET2),
    )


class AvalSolarPlant2(AvalMember, AvalBaseSolarPlant):
    INDEX = 2
    BASE_INDEX = 62
    ASTEROID_ZONES = [
        AvalSolarMinesZone2,
    ]
    RU_NAME = MS('Солн.генератор Льюис', "Solar Plant Lewes")
    MISC_EQUIP_TYPE = BR_PIRATE
    EQUIP_SET = markets.EquipSet(
        Q.Power(BR_CIV, eq_classes=markets.SECRET2),
        Q.Shield(BR_PIRATE, eq_classes=markets.SECRET3),
    )


class AvalSolarPlant3(AvalMember, AvalBaseSolarPlant):
    INDEX = 3
    BASE_INDEX = 63
    ASTEROID_ZONES = [
        AvalSolarMinesZone3,
    ]
    RU_NAME = MS('Солн.генератор Харлоу', 'Solar Plant Harlow')
    MISC_EQUIP_TYPE = BR_PIRATE
    EQUIP_SET = markets.EquipSet(
        Q.Power(BR_PIRATE, eq_classes=markets.SECRET2),
        Q.Shield(BR_PIRATE, eq_classes=markets.SECRET2),
    )


class AvalSolarPlant4(AvalMember, AvalBaseSolarPlant):
    INDEX = 4
    BASE_INDEX = 64
    ASTEROID_ZONES = [
        AvalSolarMinesZone4,
    ]
    RU_NAME = MS('Солн.генератор Челси', "Solar Plant Chelsey")
    MISC_EQUIP_TYPE = BR_PIRATE
    EQUIP_SET = markets.EquipSet(
        Q.Power(BR_CIV, eq_classes=markets.SECRET2),
        Q.Shield(BR_MAIN, eq_classes=markets.SECRET2),
    )


class AvalSolarPlant5(AvalMember, AvalBaseSolarPlant):
    INDEX = 5
    BASE_INDEX = 65
    ASTEROID_ZONES = [
        AvalSolarMinesZone5,
    ]
    RU_NAME = MS('Солн.генератор Вейбридж', "Solar Plant Weybridge")
    MISC_EQUIP_TYPE = BR_PIRATE
    EQUIP_SET = markets.EquipSet(
        Q.Power(BR_CIV, eq_classes=markets.SECRET3),
        Q.Shield(BR_PIRATE, eq_classes=markets.SECRET2),
    )


class AvalSolarSupriseRewards(AvalMember, mineable.DefaultSupriseRewardsGroup):
    NAME = 'br_avl_solar_suprise'
    SOLAR = suprise.BretoniaMiscFighter
    REWARD_ITEM = None
    ULTRA_REWARD_BASES = [
        AvalSolarPlant1,
        AvalSolarPlant2,
        AvalSolarPlant3,
        AvalSolarPlant4,
        AvalSolarPlant5,
    ]


class AvalSolarSupriseField(mineable.DefaultField):
    BOX_SIZE = 400
    DENSITY_MULTIPLER = 4
    DRIFT_X = 0.5
    DRIFT_Y = 0.5
    DRIFT_Z = 0.5
    EMPTY_CHANCE = 0.2


class AvalBaseSolarSupriseRewardField(mineable.SupriseRewardField):
    ALIAS = 'solar'
    FIELD_CLASS = AvalSolarSupriseField
    REWARDS_GROUP_CLASS = AvalSolarSupriseRewards
    ULTRA_REWARD = True


class AvalSolarSupriseRewardField1(AvalMember, AvalBaseSolarSupriseRewardField):
    INDEX = 1
    ULTRA_BASE = AvalSolarPlant1


class AvalSolarSupriseRewardField2(AvalMember, AvalBaseSolarSupriseRewardField):
    INDEX = 2
    ULTRA_BASE = AvalSolarPlant2


class AvalSolarSupriseRewardField3(AvalMember, AvalBaseSolarSupriseRewardField):
    INDEX = 3
    ULTRA_BASE = AvalSolarPlant3


class AvalSolarSupriseRewardField4(AvalMember, AvalBaseSolarSupriseRewardField):
    INDEX = 4
    ULTRA_BASE = AvalSolarPlant4


class AvalSolarSupriseRewardField5(AvalMember, AvalBaseSolarSupriseRewardField):
    INDEX = 5
    ULTRA_BASE = AvalSolarPlant5


class AvalAsteroidDefinition1(asteroid_definition.CuracaoPlumbumAsteroidDefinition):
    BELT = True
    BILLBOARDS = True
    DYNAST = True


class AvalAsteroidZone1(AvalMember, zones.AsteroidZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = AvalAsteroidDefinition1


class AvalAsteroidZone2(AvalMember, zones.AsteroidZone):
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = AvalAsteroidDefinition1


class AvalAsteroidZone3(AvalMember, zones.AsteroidZone):
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = AvalAsteroidDefinition1


class AvalBaseAbandonedAst(main_objects.AbandonedAsteroid):
    ALIAS = 'ast'
    ROTATE_RANDOM = True
    ARCHETYPE = 'co_cur_base_medium01'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    AST_EXCLUSION_ZONE_SIZE = 2500
    AST_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.ICE,
        'spacedust_maxparticles': 200,
    }


class AvalAbandonedAstBase1(AvalMember, AvalBaseAbandonedAst):
    INDEX = 1
    BASE_INDEX = 58

    ASTEROID_ZONES = [
        AvalAsteroidZone1,
    ]
    RU_NAME = MS('База Илинг', "Ealing Base")
    MISC_EQUIP_TYPE = BR_PIRATE
    WEAPON_FACTION = WEAPON_BR
    EQUIP_SET = markets.EquipSet(
        Q.Gun('br_xenosgun', eq_classes=markets.SECRET2),
        Q.Engine(None, eq_classes=markets.SECRET2),
    )


class AvalAbandonedAstBase2(AvalMember, AvalBaseAbandonedAst):
    INDEX = 2
    BASE_INDEX = 59
    ARCHETYPE = 'co_cur_base_medium02'

    ASTEROID_ZONES = [
        AvalAsteroidZone2,
    ]
    RU_NAME = MS('База Вулидж', "Woolwich Base")
    MISC_EQUIP_TYPE = BR_PIRATE
    WEAPON_FACTION = WEAPON_BR
    EQUIP_SET = markets.EquipSet(
        Q.Gun('br_iragun', eq_classes=markets.SECRET2),
        Q.Engine(None, eq_classes=markets.SECRET1),
    )


class AvalUnlockAsteroidReward(AvalMember, mineable.AsteroidRewardsGroupUltra):
    NAME = 'br_avl_unlock'
    SOLAR = asteroid.AsteroidCuracao
    REWARD_ITEM = roid(PLUMBUM)
    ULTRA_REWARD_BASES = [
        AvalAbandonedAstBase1,
        AvalAbandonedAstBase2,
    ]


class AvalBackgroundAsteroidReward(AvalMember, mineable.AsteroidRewardsGroupUltra):
    NAME = 'br_avl_background'
    SOLAR = asteroid.AsteroidCuracao
    REWARD_ITEM = roid(PLUMBUM)


class AvalMineableField(mineable.MineableAsteroidField):
    BOX_SIZE = 1400
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.3
    DRIFT_Y = 0
    DRIFT_Z = 0.3


class AvalUnlockAsteroidRewardField(mineable.AsteroidRewardField):
    ALIAS = 'ast'
    FIELD_CLASS = AvalMineableField
    REWARDS_GROUP_CLASS = AvalUnlockAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class AvalBackgroundAsteroidRewardField(mineable.AsteroidStaticField):
    ALIAS = 'ast'
    FIELD_CLASS = AvalMineableField
    REWARDS_GROUP_CLASS = AvalBackgroundAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25
    ULTRA_REWARD = False


class AvalRewardAsteroids1(AvalMember, AvalUnlockAsteroidRewardField):
    INDEX = 1
    ULTRA_BASE = AvalAbandonedAstBase1


class AvalRewardAsteroids2(AvalMember, AvalUnlockAsteroidRewardField):
    INDEX = 2
    ULTRA_BASE = AvalAbandonedAstBase2


class AvalRewardAsteroids3(AvalMember, AvalBackgroundAsteroidRewardField):
    INDEX = 3


class AvalTau29Jumpgate(AvalMember, main_objects.Jumpgate):
    INDEX = 1
    REL = RIGHT
    TARGET_SYSTEM_NAME = 'tau29'


class AvalTau23Jumpgate(AvalMember, main_objects.Jumpgate):
    INDEX = 2
    REL = BOTTOM
    TARGET_SYSTEM_NAME = 'tau23'


class AvalDockring(AvalMember, main_objects.LargePlanetDockring):
    BASE_INDEX = 1
    REL = LEFT
    INTERIOR_CLASS = interior.CustomFullSplitRoomInterior
    DEALERS = dealers.BretoniaPlanetDealers
    SHIP_SET = markets.ShipSet('co_fighter', 'co_elite', 'br_freighter')
    RU_NAME = MS('Планета Авалон', "Planet Avalon")

    BASE_PROPS = meta.LargePlanet(
        objectives=[
            meta.ProduceBest(AMMUNITION),
            meta.ProduceBest(DEFENCE_SYSTEMS),
            meta.ProduceCheap(MOX_FUEL),
            meta.ProduceNormal(ELECTRONICS),
            meta.ProduceNormal(RESEARCH_EQUIP),
            meta.ProduceBad(LUXURY_DIAMONDS),
            meta.ProduceBad(LUXURY_GOODS),
        ]
    )


class AvalShipyard(AvalMember, main_objects.Shipyard):
    INDEX = 1
    BASE_INDEX = 2
    REL = BOTTOM
    RU_NAME = MS('Верфь Саутг+емптон', 'Southampton Shipyard')

    SPACE_OBJECT_TEMPLATE = shipyards.HeavyBarrelShipyard

    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.BretoniaCivilianDealers


class AvalPolice(AvalMember, main_objects.Outpost):
    ALIAS = 'police'
    INDEX = 1
    BASE_INDEX = 3
    REL = BOTTOM
    RU_NAME = MS('Аванпост Манч+естер', "Outpost Manchester")

    SPACE_OBJECT_TEMPLATE = police.BerlinPoliceOutpost

    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.BretoniaMilitaryDealers


class AvalTrading(AvalMember, main_objects.TradingBase):
    INDEX = 1
    BASE_INDEX = 4
    REL = RIGHT
    RU_NAME = MS('Торговая станция Б+ирмингем', "Trading station Birmingham")

    SPACE_OBJECT_TEMPLATE = trade_storages.TekagiStorage

    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.BretoniaCivilianDealers


class AvalMilitary(AvalMember, main_objects.Station):
    INDEX = 1
    BASE_INDEX = 5
    REL = TOP
    RU_NAME = MS('Станция Лондон', "London Station")

    SPACE_OBJECT_TEMPLATE = avalon_megabase.AvalonMegabase

    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.BretoniaMilitaryDealers

    BASE_PROPS = meta.MediumStation(
        objectives=[
            meta.SupportBattleships(),
        ]
    )


class AvalPrison(AvalMember, main_objects.Prison):
    INDEX = 1
    BASE_INDEX = 6
    REL = TOP
    RU_NAME = MS('Тюрьма Г+олспи', "Golspie Prison")

    SPACE_OBJECT_TEMPLATE = prisons.AvalonPrison

    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.BretoniaMilitaryDealers


class AvalJunkers(AvalMember, main_objects.JunkerBase):
    INDEX = 1
    BASE_INDEX = 7
    ALIAS = 'pirate'
    REL = LEFT
    SPACE_OBJECT_TEMPLATE = junker.ForbesJunker
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.BretoniaPirateDealers
    FACTION = faction.Xenos
    AST_EXCLUSION_ZONE_SIZE = 2500
    ASTEROID_ZONES = [
        AvalDebrisZone3
    ]
    RU_NAME = MS('База К+ардиган', "Cardigan Base")


class AvalPirates(AvalMember, main_objects.PirateStation):
    INDEX = 2
    BASE_INDEX = 8
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = pirate.PirateBaseCalifornia
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.BretoniaPirateDealers
    FACTION = faction.BretoniaPirate
    AST_EXCLUSION_ZONE_SIZE = 2500
    ASTEROID_ZONES = [
        AvalAsteroidZone3
    ]
    RU_NAME = MS('База Л+онстон', 'Launceston Base')


class AvalPlanet1(AvalMember, main_objects.Planet):
    INDEX = 1
    ARCHETYPE = 'planet_earthgrncld_4000'
    SPHERE_RADIUS = 4000
    RELATED_DOCK_RING = AvalDockring


class AvalPlanet2(AvalMember, main_objects.Planet):
    INDEX = 2
    ARCHETYPE = 'planet_gasorgcld_5000'
    SPHERE_RADIUS = 5000
    RU_NAME = MS('Планета Эксмор', 'Planet Exmore')


class AvalPlanet3(AvalMember, main_objects.Planet):
    INDEX = 3
    ARCHETYPE = 'planet_moonblu_2500'
    SPHERE_RADIUS = 2500
    RU_NAME = MS('Планета Уотфорд', "Planet Watford")


class AvalPlanet4(AvalMember, main_objects.Planet):
    INDEX = 4
    ARCHETYPE = 'planet_desored_3000'
    SPHERE_RADIUS = 3000
    RU_NAME = MS('Планета Кроли', 'Planet Crawley')


class AvalPoliceConn1(AvalMember, main_objects.TradeConnection):
    OBJ_FROM = AvalDockring
    OBJ_TO = AvalPolice
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        AvalPirates,
    ]


class AvalPoliceConn2(AvalMember, main_objects.TradeConnection):
    OBJ_FROM = AvalPolice
    OBJ_TO = AvalTau23Jumpgate
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        AvalPirates,
    ]


class AvalPoliceConn3(AvalMember, main_objects.TradeConnection):
    OBJ_FROM = AvalPolice
    OBJ_TO = AvalShipyard
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'C'


class AvalPrisonConn1(AvalMember, main_objects.TradeConnection):
    OBJ_FROM = AvalPrison
    OBJ_TO = AvalDockring
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'D'


class AvalPrisonConn2(AvalMember, main_objects.TradeConnection):
    OBJ_FROM = AvalPrison
    OBJ_TO = AvalMilitary
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'E'

    OBJ_FROM_TLR_FORCE_OFFSET = (-21500, 0, -59000)


class AvalDockringConn1(AvalMember, main_objects.TradeConnection):
    OBJ_FROM = AvalDockring
    OBJ_TO = AvalMilitary
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'F'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        AvalJunkers,
    ]


class AvalTradingConn1(AvalMember, main_objects.TradeConnection):
    OBJ_FROM = AvalMilitary
    OBJ_TO = AvalTrading
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'I'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        AvalJunkers,
    ]


class AvalTradingConn2(AvalMember, main_objects.TradeConnection):
    OBJ_FROM = AvalTrading
    OBJ_TO = AvalTau29Jumpgate
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'G'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        AvalJunkers,
    ]


class AvalTradingConn3(AvalMember, main_objects.TradeConnection):
    OBJ_FROM = AvalTrading
    OBJ_TO = AvalShipyard
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'H'


class AvalStoryBattleship(AvalMember, main_objects.BretoniaBattleship):
    ALIAS = 'm7_bship'
    INDEX = 1
    BASE_INDEX = 99
    REL = LEFT
    INTERIOR_CLASS = interior.BattleshipInterior
    DEALERS = dealers.BretoniaMilitaryDealers
    STORY = True
    CALC_STORE = False
    FORCE_CONNECTIONS = [
        AvalPolice,  # TODO: haven't real economics connection
    ]
    SHIP_SET = markets.ShipSet('co_elite_darcy')
    RU_NAME = PRINCE_OF_WALES
    MSG_PREFIX = MSG_PRINCE_OF_WALES


class AvalStoryBattleshipTwo(AvalMember, main_objects.BretoniaBattleship):
    ALIAS = 'm8_bship'
    INDEX = 1
    BASE_INDEX = 98
    REL = LEFT
    INTERIOR_CLASS = interior.BattleshipInterior
    DEALERS = dealers.BretoniaMilitaryDealers
    STORY = True
    CALC_STORE = False
    IS_BASE = False
    AUTOSAVE_FORBIDDEN = True
    RU_NAME = PRINCE_OF_WALES
    MSG_PREFIX = MSG_PRINCE_OF_WALES
