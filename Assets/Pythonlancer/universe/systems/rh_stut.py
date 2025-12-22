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

from text.strings import MultiString as MS


class StutMember(Member):
    FACTION = faction.RheinlandMain
    INTERIOR_BG1 = interior.INTERIOR_RH_STUTTGART
    WEAPON_FACTION = WEAPON_RH
    EQUIP_FACTION = EQUIP_RH


class StutRawText(StutMember, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = rh_stut
space_color = 10, 10, 0
local_faction = rh_grp
space_farclip = 75000

[TexturePanels]
file = universe\\heavens\\shapes.ini

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


class StutDebrisZone1(StutMember, zones.DebrisZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class StutDebrisZone2(StutMember, zones.DebrisZone):
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class StutDebrisZone3(StutMember, zones.DebrisZone):
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


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
    RU_NAME = MS('Плавильня Гейдельберг', "Heidelberg Smelter")
    MISC_EQUIP_TYPE = RH_MAIN
    EQUIP_SET = markets.EquipSet(
        Q.Thruster(RH_PIRATE, eq_classes=markets.SECRET3),
        Q.Power(RH_PIRATE, eq_classes=markets.SECRET2),
    )


class StutDebrisFactory2(StutMember, StutBaseDebrisManufactoring):
    INDEX = 3
    BASE_INDEX = 52
    ASTEROID_ZONES = [
        StutDebrisZone3,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500
    RU_NAME = MS('Плавильня Неандерталь', 'Neanderthal Smelter')
    MISC_EQUIP_TYPE = RH_MAIN
    EQUIP_SET = markets.EquipSet(
        Q.Thruster(RH_CIV, eq_classes=markets.SECRET2),
        Q.Power(RH_MAIN, eq_classes=markets.SECRET3),
    )


class StutDebrisBoxReward(StutMember, mineable.DefaultDebrisBoxRewardsGroup):
    NAME = 'rh_stut_debrisbox'
    SOLAR = debris_box.DebrisBox
    REWARD_ITEM = 'comm_scrap_metal'
    ULTRA_REWARD_BASES = [
        StutDebrisFactory1,
        StutDebrisFactory2,
    ]


class StutBaseDebrisBoxRewardField(mineable.DebrisBoxRewardField):
    FIELD_CLASS = mineable.MineableDebrixBoxField
    REWARDS_GROUP_CLASS = StutDebrisBoxReward
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class StutDebrisBoxField1(StutMember, StutBaseDebrisBoxRewardField):
    INDEX = 2
    ULTRA_BASE = StutDebrisFactory1


class StutDebrisBoxField2(StutMember, StutBaseDebrisBoxRewardField):
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


class StutBaseMinesZone(zones.AsteroidZone):
    ASTEROID_DEFINITION_CLASS = asteroid_definition.SpaceMines
    SPACEDUST = Dust.DEBRIS
    SPACEDUST_MAXPARTICLES = 100
    MUSIC = Ambience.MINE_AST
    INTERFERENCE = 0.1
    DRAG_MODIFIER = 1.5
    PROPERTY_FLAGS = 4128


class StutSolarMinesZone1(StutMember, StutBaseMinesZone):
    ALIAS = 'solar'
    INDEX = 1


class StutSolarMinesZone2(StutMember, StutBaseMinesZone):
    ALIAS = 'solar'
    INDEX = 2


class StutSolarMinesZone3(StutMember, StutBaseMinesZone):
    ALIAS = 'solar'
    INDEX = 3


class StutSolarMinesZone4(StutMember, StutBaseMinesZone):
    ALIAS = 'solar'
    INDEX = 4


class StutSolarMinesZone5(StutMember, StutBaseMinesZone):
    ALIAS = 'solar'
    INDEX = 5


class StutSolarPlant1(StutMember, StutBaseSolarPlant):
    INDEX = 1
    BASE_INDEX = 61
    ASTEROID_ZONES = [
        StutSolarMinesZone1,
    ]
    RU_NAME = MS('Солн.генератор Тюбинген', 'Solar Planet Tübingen ')
    MISC_EQUIP_TYPE = RH_PIRATE
    EQUIP_SET = markets.EquipSet(
        Q.Power(RH_CIV, eq_classes=markets.SECRET3),
        Q.Shield(RH_PIRATE, eq_classes=markets.SECRET2),
    )


class StutSolarPlant2(StutMember, StutBaseSolarPlant):
    INDEX = 2
    BASE_INDEX = 62
    ASTEROID_ZONES = [
        StutSolarMinesZone2,
    ]
    RU_NAME = MS('Солн.генератор Хейльбронн', 'Solar Planet Heilbronn')
    MISC_EQUIP_TYPE = RH_PIRATE
    EQUIP_SET = markets.EquipSet(
        Q.Power(RH_CIV, eq_classes=markets.SECRET2),
        Q.Shield(RH_PIRATE, eq_classes=markets.SECRET3),
    )


class StutSolarPlant3(StutMember, StutBaseSolarPlant):
    INDEX = 3
    BASE_INDEX = 63
    ASTEROID_ZONES = [
        StutSolarMinesZone3,
    ]
    RU_NAME = MS('Солн.генератор Кобленц', 'Solar Plant Koblenz')
    MISC_EQUIP_TYPE = RH_PIRATE
    EQUIP_SET = markets.EquipSet(
        Q.Power(RH_PIRATE, eq_classes=markets.SECRET2),
        Q.Shield(RH_PIRATE, eq_classes=markets.SECRET2),
    )


class StutSolarPlant4(StutMember, StutBaseSolarPlant):
    INDEX = 4
    BASE_INDEX = 64
    ASTEROID_ZONES = [
        StutSolarMinesZone4,
    ]
    RU_NAME = MS('Солн.генератор Хамм', 'Solar Plant Hamm')
    MISC_EQUIP_TYPE = RH_PIRATE
    EQUIP_SET = markets.EquipSet(
        Q.Power(RH_CIV, eq_classes=markets.SECRET2),
        Q.Shield(RH_MAIN, eq_classes=markets.SECRET2),
    )


class StutSolarPlant5(StutMember, StutBaseSolarPlant):
    INDEX = 5
    BASE_INDEX = 65
    ASTEROID_ZONES = [
        StutSolarMinesZone5,
    ]
    RU_NAME = MS('Солн.генератор Кассель', "Solar Planet Kassel")
    MISC_EQUIP_TYPE = RH_PIRATE
    EQUIP_SET = markets.EquipSet(
        Q.Power(RH_CIV, eq_classes=markets.SECRET3),
        Q.Shield(RH_PIRATE, eq_classes=markets.SECRET2),
    )


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
    FIELD_CLASS = StutSolarSupriseField
    REWARDS_GROUP_CLASS = StutSolarSupriseRewards
    ULTRA_REWARD = True


class StutSolarSupriseRewardField1(StutMember, StutBaseSolarSupriseRewardField):
    INDEX = 1
    ULTRA_BASE = StutSolarPlant1


class StutSolarSupriseRewardField2(StutMember, StutBaseSolarSupriseRewardField):
    INDEX = 2
    ULTRA_BASE = StutSolarPlant2


class StutSolarSupriseRewardField3(StutMember, StutBaseSolarSupriseRewardField):
    INDEX = 3
    ULTRA_BASE = StutSolarPlant3


class StutSolarSupriseRewardField4(StutMember, StutBaseSolarSupriseRewardField):
    INDEX = 4
    ULTRA_BASE = StutSolarPlant4


class StutSolarSupriseRewardField5(StutMember, StutBaseSolarSupriseRewardField):
    INDEX = 5
    ULTRA_BASE = StutSolarPlant5


class StutSun(StutMember, main_objects.Sun):
    STAR = 'med_orange_sun'
    LOADOUT = 'large_yellow_sun_fx'
    ATMOSHPERE_RANGE = 12000


class StutOmega15Jumpgate(StutMember, main_objects.Jumpgate):
    INDEX = 1
    REL = RIGHT
    TARGET_SYSTEM_NAME = 'om15'


class StutOmega7Jumpgate(StutMember, main_objects.Jumpgate):
    INDEX = 2
    REL = LEFT
    TARGET_SYSTEM_NAME = 'om7'


class StutDockring(StutMember, main_objects.LargePlanetDockring):
    BASE_INDEX = 1
    REL = TOP
    INTERIOR_CLASS = interior.CustomFullSingleRoomInterior
    DEALERS = dealers.RheinlandPlanetDealers
    SHIP_SET = markets.ShipSet('ge_fighter2', 'bw_elite2', 'rh_freighter')
    RU_NAME = MS('Планета Шт+утгарт', "Planet Stuttgart")

    BASE_PROPS = meta.LargePlanet(
        objectives=[
            meta.ProduceBest(ROID_MINER_PARTS),
            meta.ProduceCheap(PROD_MACHINES),
            meta.ProduceNormal(JUMPGATE_PARTS),
            meta.ProduceNormal(POLYMERS),
        ]
    )


class StutPoliceOutpost(StutMember, main_objects.Outpost):
    BASE_INDEX = 2
    REL = TOP
    SPACE_OBJECT_TEMPLATE = police.StuttgartPoliceOutpost
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.RheinlandMilitaryDealers
    RU_NAME = MS('Аванпост Цюрих', 'Outpost Zürich')


class StutShipyard(StutMember, main_objects.Shipyard):
    BASE_INDEX = 3
    REL = LEFT
    SPACE_OBJECT_TEMPLATE = shipyards.StuttgartShipyard
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.RheinlandMilitaryDealers
    RU_NAME = MS('Верфь Росток', 'Rostock Shipyard')


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
    RU_NAME = MS('Станция Мангейм', 'Mannheim Station')

    BASE_PROPS = meta.LargePlanet(
        objectives=[
            meta.ProduceBest(STATION_PANELS),
            meta.ProduceBest(ALLOY_HEAVY),
            meta.ProduceBad(ALLOY_CONDUCTOR),
            meta.ProduceBad(ENGINE_PARTS),
            meta.SupportBattleships(),
        ]
    )


class StutTraders(StutMember, main_objects.TradingBase):
    BASE_INDEX = 5
    REL = TOP
    SPACE_OBJECT_TEMPLATE = bounty_hunter.ChurchAlive
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.RheinlandCivilianDealers
    RU_NAME = MS('Торговая база Франкфурт', 'Trading base Frankfurt')


class StutLuxuryDockring(StutMember, main_objects.ResortPlanetDockring):
    INDEX = 2
    BASE_INDEX = 6
    REL = TOP
    INTERIOR_CLASS = interior.CustomFullSingleRoomInterior
    DEALERS = dealers.RheinlandPlanetDealers
    SHIP_SET = markets.ShipSet('bw_fighter')
    RU_NAME = MS('Планета Баден-Баден', 'Planet Baden-Baden')


class StutNebulaPirates(StutMember, main_objects.PirateStation):
    BASE_INDEX = 7
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = pirate.PirateBaseStuttgart
    FACTION = faction.Hessians

    RU_NAME = MS('База Фрайбург', 'Freiburg Base')

    INTERIOR_BG1 = interior.INTERIOR_BG_WALKER

    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.RheinlandPirateDealers


class StutJunkers(StutMember, main_objects.JunkerBase):
    INDEX = 2
    BASE_INDEX = 8
    ALIAS = 'pirate'
    REL = TOP
    SPACE_OBJECT_TEMPLATE = junker.StuttgartJunker
    FACTION = faction.Junkers

    RU_NAME = MS('База Висбаден', "Wiesbaden Base")

    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.RheinlandPirateDealers

    ASTEROID_ZONES = [
        StutDebrisZone1,
    ]


class StutPlanet1(StutMember, main_objects.Planet):
    ARCHETYPE = 'planet_earthgrnice_3000'
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
    RU_NAME = MS('Планета Вюртемберг', "Planet Württemberg")


class StutPoliceConn1(StutMember, main_objects.TradeConnection):
    OBJ_FROM = StutPoliceOutpost
    OBJ_TO = StutOmega7Jumpgate
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
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
