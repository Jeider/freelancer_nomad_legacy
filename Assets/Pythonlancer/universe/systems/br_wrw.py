from fx.space import Dust

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

from templates.dockable import astbase
from templates.dockable import junker
from templates.dockable import ulster_megabase
from templates.dockable import police
from templates.dockable import shipyards
from templates.dockable import alg

from text.strings import MultiString as MS


class WarwickMember(Member):
    FACTION = faction.BretoniaMain
    WEAPON_FACTION = WEAPON_BR
    EQUIP_FACTION = EQUIP_BR


class WarwickStaticText(WarwickMember, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = br_wrw
space_color = 25, 20, 5
;space_color = 60, 60, 60
local_faction = br_grp
space_farclip = 1000000

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Music]
space = music_br_space
danger = music_br_danger
battle = music_br_battle

[Dust]
spacedust = Dust

[Ambient]
color = 25, 20, 5
;color = 60, 60, 60

[Background]
nebulae = solar\\stars_mod\\br_wrw_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_br_wrw_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
property_flags = 512 ;lava - MILITARY
;property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = Br_wrw_system_light
pos = 0, 0, 0
color = 220, 160, 80
range = 150000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION
'''


class WarwickPirateAsteroidReward(WarwickMember, mineable.AsteroidRewardsGroupMedium):
    NAME = 'br_wrw_rock'
    SOLAR = asteroid.AsteroidTau37
    REWARD_ITEM = 'comm_roid_niobium'


class WarwickAstField(mineable.DefaultField):
    BOX_SIZE = 1500
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.3
    DRIFT_Y = 0.05
    DRIFT_Z = 0.3


class WarwickDebrisField(mineable.DefaultField):
    BOX_SIZE = 1200
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.2
    DRIFT_Y = 0.1
    DRIFT_Z = 0.2


class WarwickPirateAsteroids(WarwickMember, mineable.AsteroidRewardField):
    INDEX = 1
    FIELD_CLASS = WarwickAstField
    REWARDS_GROUP_CLASS = WarwickPirateAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25


class WarwickPirateAsteroidDefinition(asteroid_definition.Tau37AsteroidDefinition):
    ABSTRACT = False
    DYNAST = True
    BELT = True
    BILLBOARDS = False
    LOOT = False  # TEMP


class WarwickAsteroidZone1(WarwickMember, zones.AsteroidZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = WarwickPirateAsteroidDefinition


class WarwickAsteroidZone2(WarwickMember, zones.AsteroidZone):
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = WarwickPirateAsteroidDefinition


class WarwickDebrisZone1(WarwickMember, zones.DebrisZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class WarwickDebrisZone2(WarwickMember, zones.DebrisZone):
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class WarwickDebrisZone3(WarwickMember, zones.DebrisZone):
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class WarwickDebrisZone4(WarwickMember, zones.DebrisZone):
    INDEX = 4
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class WarwickDebrisZone5(WarwickMember, zones.DebrisZone):
    INDEX = 5
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class WarwickBaseDebrisManufactoring(main_objects.DebrisManufactoring):
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


class WarwickDebrisFactory1(WarwickMember, WarwickBaseDebrisManufactoring):
    INDEX = 1
    BASE_INDEX = 51
    ASTEROID_ZONES = [
        WarwickDebrisZone1,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500
    RU_NAME = MS('Плавильня Ротбери', "Rothbury Smelter")
    MISC_EQUIP_TYPE = BR_MAIN
    EQUIP_SET = markets.EquipSet(
        Q.Thruster(BR_CIV, eq_classes=markets.SECRET2),
        Q.Power(BR_PIRATE, eq_classes=markets.SECRET3),
    )


class WarwickDebrisFactory2(WarwickMember, WarwickBaseDebrisManufactoring):
    INDEX = 2
    BASE_INDEX = 52
    ASTEROID_ZONES = [
        WarwickDebrisZone2,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500
    RU_NAME = MS('Плавильня Тиркс', "Tirks Smelter")
    MISC_EQUIP_TYPE = BR_MAIN
    EQUIP_SET = markets.EquipSet(
        Q.Thruster(BR_PIRATE, eq_classes=markets.SECRET2),
        Q.Power(BR_MAIN, eq_classes=markets.SECRET2),
    )


class WarwickDebrisFactory3(WarwickMember, WarwickBaseDebrisManufactoring):
    INDEX = 3
    BASE_INDEX = 53
    ASTEROID_ZONES = [
        WarwickDebrisZone3,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500
    RU_NAME = MS('Плавильня Галифакс', "Halafacs Smelter")
    MISC_EQUIP_TYPE = BR_MAIN
    EQUIP_SET = markets.EquipSet(
        Q.Thruster(BR_PIRATE, eq_classes=markets.SECRET3),
        Q.Power(BR_PIRATE, eq_classes=markets.SECRET2),
    )


class WarwickDebrisFactory4(WarwickMember, WarwickBaseDebrisManufactoring):
    INDEX = 4
    BASE_INDEX = 54
    ASTEROID_ZONES = [
        WarwickDebrisZone4,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500
    RU_NAME = MS('Плавильня Блекпул', "Blackpool Smelter")
    MISC_EQUIP_TYPE = BR_MAIN
    EQUIP_SET = markets.EquipSet(
        Q.Thruster(BR_CIV, eq_classes=markets.SECRET2),
        Q.Power(BR_MAIN, eq_classes=markets.SECRET3),
    )


class WarwickDebrisBoxReward(WarwickMember, mineable.DefaultDebrisBoxRewardsGroup):
    NAME = 'br_wrw_debrisbox'
    SOLAR = debris_box.DebrisBox
    REWARD_ITEM = 'comm_scrap_metal'
    ULTRA_REWARD_BASES = [
        WarwickDebrisFactory1,
        WarwickDebrisFactory2,
        WarwickDebrisFactory3,
        WarwickDebrisFactory4,
    ]


class WarwickBaseDebrisBoxRewardField(mineable.DebrisBoxRewardField):
    FIELD_CLASS = mineable.MineableDebrixBoxField
    REWARDS_GROUP_CLASS = WarwickDebrisBoxReward
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class WarwickDebrisBoxField1(WarwickMember, WarwickBaseDebrisBoxRewardField):
    INDEX = 1
    ULTRA_BASE = WarwickDebrisFactory1


class WarwickDebrisBoxField2(WarwickMember, WarwickBaseDebrisBoxRewardField):
    INDEX = 2
    ULTRA_BASE = WarwickDebrisFactory2


class WarwickDebrisBoxField3(WarwickMember, WarwickBaseDebrisBoxRewardField):
    INDEX = 3
    ULTRA_BASE = WarwickDebrisFactory3


class WarwickDebrisBoxField4(WarwickMember, WarwickBaseDebrisBoxRewardField):
    INDEX = 4
    ULTRA_BASE = WarwickDebrisFactory4


class WarwickSun(WarwickMember, main_objects.Sun):
    STAR = 'Br04_Sun'
    LOADOUT = 'large_yellow_sun_fx'


class WarwickTau29Jumpgate(WarwickMember, main_objects.Jumpgate):
    INDEX = 1
    REL = LEFT
    TARGET_SYSTEM_NAME = 'tau29'


class WarwickSig22Jumpgate(WarwickMember, main_objects.Jumpgate):
    INDEX = 2
    REL = RIGHT
    TARGET_SYSTEM_NAME = 'sig22'


class WarwickSiriusJumpgate(WarwickMember, main_objects.Jumpgate):
    INDEX = 3
    REL = BOTTOM
    TARGET_SYSTEM_NAME = 'sig42'


class WarwickDockring(WarwickMember, main_objects.LargePlanetDockring):
    BASE_INDEX = 1
    REL = TOP
    INTERIOR_CLASS = interior.CustomFullSplitRoomInterior
    DEALERS = dealers.BretoniaPlanetDealers
    SHIP_SET = markets.ShipSet('co_fighter', 'co_elite2', 'ge_csv')
    RU_NAME = MS('Планета Уорик', 'Warwick Planet')

    BASE_PROPS = meta.LargePlanet(
        objectives=[
            meta.ProduceBest(REACTORS),
            meta.ProduceBest(PLUMBUM),
            meta.ProduceCheap(MOX_FUEL),
            meta.ProduceCheap(AMMUNITION),
            meta.ProduceNormal(MINING_EQUIPMENT),
            meta.ProduceNormal(GAS_MINER_PARTS),
            meta.ProduceBad(SMELTER_PARTS),
            meta.ProduceBad(ROID_MINER_PARTS),
        ]
    )


class WarwickLargeStation(WarwickMember, main_objects.LargeStation):
    BASE_INDEX = 2
    REL = TOP
    REL_DRIFT = 800
    SPACE_OBJECT_TEMPLATE = ulster_megabase.UlsterMegabase
    INTERIOR_CLASS = interior.StationShipdealerInterior
    DEALERS = dealers.BretoniaCivilianDealers
    SHIP_SET = markets.ShipSet('br_freighter')
    RU_NAME = MS('Станция Лидс', "Station Leeds")

    BASE_PROPS = meta.Megabase(
        objectives=[
            meta.ProduceBest(GREENHOUSE_PARTS),
            meta.ProduceBest(TERRAFORM_MINERALS),
            meta.ProduceCheap(SHIP_HULL_PANELS),
            meta.ProduceCheap(ENGINE_PARTS),

            meta.HaveGreenhouse(),
            meta.HaveSolarPanels(),
            meta.HaveReactor(),
        ]
    )


class WarwickRefinery(WarwickMember, main_objects.Refinery):
    BASE_INDEX = 3
    REL = LEFT
    SPACE_OBJECT_TEMPLATE = alg.AlgBaseBerlin
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.BretoniaCivilianDealers
    FACTION = faction.BretoniaCivilians
    RU_NAME = MS('Станция Глазго', "Glasgow Station")

    BASE_PROPS = meta.Refinery(
        objectives=[
            meta.ProduceNormal(ALLOY_RADIATION),
            meta.ProduceBad(ALLOY_HEAVY),
            meta.ProduceBad(ALLOY_TEMPERATURE),
        ]
    )


class WarwickOutpost(WarwickMember, main_objects.Outpost):
    BASE_INDEX = 4
    REL = LEFT
    SPACE_OBJECT_TEMPLATE = police.PoliceOutpostBretonia
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.BretoniaMilitaryDealers
    RU_NAME = MS('Аванпост Ливерпуль', "Outpost Liverpool")


class WarwickShipyard(WarwickMember, main_objects.Shipyard):
    BASE_INDEX = 5
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = shipyards.UlsterShipyardAlive
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.BretoniaCivilianDealers
    RU_NAME = MS('Верфь Бристоль', "Bristol Shipyard")


class WarwickPiratesTop(WarwickMember, main_objects.PirateAsteroid):
    BASE_INDEX = 6
    INDEX = 1
    REL = TOP
    SPACE_OBJECT_TEMPLATE = astbase.BerlinAsteroidBase
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.BretoniaPirateDealers
    FACTION = faction.BretoniaPirate
    AST_EXCLUSION_ZONE_SIZE = 2500
    ASTEROID_ZONES = [
        WarwickAsteroidZone1
    ]
    DEFENCE_LEVEL = None
    RU_NAME = MS('База Г+олуэй', "Galway Base")


class WarwickJunkers(WarwickMember, main_objects.JunkerBase):
    BASE_INDEX = 8
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = junker.StuttgartJunker
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.BretoniaPirateDealers
    FACTION = faction.BretoniaPirate
    ASTEROID_ZONES = [
        WarwickDebrisZone5
    ]
    DEFENCE_LEVEL = None
    RU_NAME = MS('База Д+углас', 'Duglas Base')


class WarwickPlanet1(WarwickMember, main_objects.Planet):
    ARCHETYPE = 'planet_earthcity_4000'
    SPHERE_RADIUS = 4000
    RELATED_DOCK_RING = WarwickDockring


class WarwickPlanet2(WarwickMember, main_objects.Planet):
    INDEX = 2
    ARCHETYPE = 'planet_desorgrck_3000'
    SPHERE_RADIUS = 3000
    RU_NAME = MS('Планета Готфелл', "Gotwell base")


class WarwickPlanet3(WarwickMember, main_objects.Planet):
    INDEX = 3
    ARCHETYPE = 'planet_moonblu_2500'
    SPHERE_RADIUS = 2500
    RU_NAME = MS('Планета Слейт Айлендс', "Planet Slate Islands")


class WarwickPoliceConn1(WarwickMember, main_objects.TradeConnection):
    OBJ_FROM = WarwickOutpost
    OBJ_TO = WarwickSiriusJumpgate
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        WarwickJunkers
    ]


class WarwickPoliceConn2(WarwickMember, main_objects.TradeConnection):
    OBJ_FROM = WarwickOutpost
    OBJ_TO = WarwickShipyard
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        WarwickJunkers
    ]


class WarwickPoliceConn3(WarwickMember, main_objects.TradeConnection):
    OBJ_FROM = WarwickOutpost
    OBJ_TO = WarwickRefinery
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        WarwickJunkers
    ]


class WarwickPlanetConn1(WarwickMember, main_objects.TradeConnection):
    OBJ_FROM = WarwickDockring
    OBJ_TO = WarwickTau29Jumpgate
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = BOTTOM


class WarwickPlanetConn2(WarwickMember, main_objects.TradeConnection):
    OBJ_FROM = WarwickDockring
    OBJ_TO = WarwickLargeStation
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        WarwickPiratesTop
    ]


class WarwickPlanetConn3(WarwickMember, main_objects.TradeConnection):
    OBJ_FROM = WarwickDockring
    OBJ_TO = WarwickRefinery
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'F'


class WarwickShipyardConn1(WarwickMember, main_objects.TradeConnection):
    OBJ_FROM = WarwickShipyard
    OBJ_TO = WarwickRefinery
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'G'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        WarwickJunkers
    ]
    OBJ_FROM_TLR_FORCE_OFFSET = (14000, 0, 23500)


class WarwickShipyardConn2(WarwickMember, main_objects.TradeConnection):
    OBJ_FROM = WarwickShipyard
    OBJ_TO = WarwickLargeStation
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'H'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        WarwickPiratesTop
    ]


class WarwickLargeStationConn1(WarwickMember, main_objects.TradeConnection):
    OBJ_FROM = WarwickLargeStation
    OBJ_TO = WarwickSig22Jumpgate
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'I'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        WarwickPiratesTop
    ]

