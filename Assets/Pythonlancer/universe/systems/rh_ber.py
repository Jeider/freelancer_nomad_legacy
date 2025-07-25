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
from universe.content import interior
from universe.content import dealers
from universe.content import asteroid_definition
from universe.audio.space_voice import SpaceVoice
from universe import faction

from templates.nebula import rh_ber_nebula
from templates.dockable import pirate
from templates.dockable import potsdam
from templates.dockable import prisons
from templates.dockable import shipyards
from templates.dockable import stuttgart_megabase
from templates.dockable import astbase
from templates.dockable import junker
from templates.dockable import police
from templates.dockable import trade_storages

from universe.content import mineable

from templates.solar import asteroid
from templates.solar import debris_box


class BerlinMember(Member):
    FACTION = faction.RheinlandMain
    WEAPON_FACTION = WEAPON_RH
    EQUIP_FACTION = EQUIP_RH


class BerlinStaticText(BerlinMember, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = rh_ber
space_color = 3, 7, 12
local_faction = rh_grp
space_farclip = 75000

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Music]
space = music_rh_space
danger = music_rh_danger
battle = music_rh_battle

[Ambient]
color = 3, 5, 8

[Dust]
spacedust = Dust

[Background]
nebulae = solar\\stars_mod\\rh_ber_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_rh_ber_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
property_flags = 512 ;lava - MILITARY
;property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = Rh_Ber_System_Light
pos = 0, 0, 0
color = 150, 190, 255
range = 150000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION

'''


class BerlinPirateAsteroidReward(BerlinMember, mineable.AsteroidRewardsGroupMedium):
    NAME = 'rh_ber_rock'
    SOLAR = asteroid.AsteroidOmega15
    REWARD_ITEM = 'comm_roid_niobium'


class BerlinAstField(mineable.DefaultField):
    BOX_SIZE = 3000
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.3
    DRIFT_Y = 0
    DRIFT_Z = 0.3


class BerlinDebrisField(mineable.DefaultField):
    BOX_SIZE = 1200
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.2
    DRIFT_Y = 0.1
    DRIFT_Z = 0.2


class BerlinPirateAsteroids(BerlinMember, mineable.AsteroidRewardField):
    INDEX = 1
    FIELD_CLASS = BerlinAstField
    REWARDS_GROUP_CLASS = BerlinPirateAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25


class BerlinPirateAsteroidDefinition(asteroid_definition.Omega15AsteroidDefinition):
    ABSTRACT = False
    NAME = 'rh_ber_pirate_astfield'
    DYNAST = True
    BELT = False
    BILLBOARDS = False
    LOOT = False  # TEMP


class BerlinAsteroidZone1(BerlinMember, zones.AsteroidZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = BerlinPirateAsteroidDefinition


class BerlinDebrisZone1(BerlinMember, zones.DebrisZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class BerlinDebrisZone2(BerlinMember, zones.DebrisZone):
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class BerlinDebrisZone3(BerlinMember, zones.DebrisZone):
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class BerlinDebrisZone4(BerlinMember, zones.DebrisZone):
    INDEX = 4
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class BerlinDebrisZone5(BerlinMember, zones.DebrisZone):
    INDEX = 5
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class BerlinBaseDebrisManufactoring(main_objects.DebrisManufactoring):
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


class BerlinDebrisFactory1(BerlinMember, BerlinBaseDebrisManufactoring):
    INDEX = 2
    BASE_INDEX = 51
    ASTEROID_ZONES = [
        BerlinDebrisZone2,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500
    RU_NAME = 'Плавильня Путлиц'
    MISC_EQUIP_TYPE = RH_MAIN
    EQUIP_SET = markets.EquipSet(
        Q.Thruster(RH_CIV, eq_classes=markets.SECRET3),
        Q.Power(RH_PIRATE, eq_classes=markets.SECRET2),
    )


class BerlinDebrisFactory2(BerlinMember, BerlinBaseDebrisManufactoring):
    INDEX = 3
    BASE_INDEX = 52
    ASTEROID_ZONES = [
        BerlinDebrisZone3,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500
    RU_NAME = 'Плавильня Рёбель'
    MISC_EQUIP_TYPE = RH_MAIN
    EQUIP_SET = markets.EquipSet(
        Q.Thruster(RH_CIV, eq_classes=markets.SECRET2),
        Q.Power(RH_MAIN, eq_classes=markets.SECRET3),
    )


class BerlinDebrisFactory3(BerlinMember, BerlinBaseDebrisManufactoring):
    INDEX = 4
    BASE_INDEX = 53
    ASTEROID_ZONES = [
        BerlinDebrisZone4,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500
    RU_NAME = 'Плавильня Лёц'
    MISC_EQUIP_TYPE = RH_MAIN
    EQUIP_SET = markets.EquipSet(
        Q.Thruster(RH_PIRATE, eq_classes=markets.SECRET2),
        Q.Power(RH_MAIN, eq_classes=markets.SECRET2),
    )


class BerlinDebrisBoxReward(BerlinMember, mineable.DefaultDebrisBoxRewardsGroup):
    NAME = 'rh_ber_debrisbox'
    SOLAR = debris_box.DebrisBox
    REWARD_ITEM = 'comm_scrap_metal'
    ULTRA_REWARD_BASES = [
        BerlinDebrisFactory1,
        BerlinDebrisFactory2,
        BerlinDebrisFactory3,
    ]


class BerlinBaseDebrisBoxRewardField(mineable.DebrisBoxRewardField):
    FIELD_CLASS = mineable.MineableDebrixBoxField
    REWARDS_GROUP_CLASS = BerlinDebrisBoxReward
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class BerlinDebrisBoxField1(BerlinMember, BerlinBaseDebrisBoxRewardField):
    INDEX = 2
    ULTRA_BASE = BerlinDebrisFactory1


class BerlinDebrisBoxField2(BerlinMember, BerlinBaseDebrisBoxRewardField):
    INDEX = 3
    ULTRA_BASE = BerlinDebrisFactory2


class BerlinDebrisBoxField3(BerlinMember, BerlinBaseDebrisBoxRewardField):
    INDEX = 4
    ULTRA_BASE = BerlinDebrisFactory3


class BerlinTopNebula(BerlinMember, zones.NebulaZone):
    INDEX = 1
    CONTENT_TEMPLATE = rh_ber_nebula.BerlinBlueNebulaTemplate
    SPACEDUST = Dust.ATTRACT
    SPACEDUST_MAXPARTICLES = 50
    MUSIC = Ambience.AST_ROCK


class BerlinSun(BerlinMember, main_objects.Sun):
    STAR = 'Rh04_Sun'
    LOADOUT = 'med_blue_sun_fx'


class BerlinSigma13Jumpgate(BerlinMember, main_objects.Jumpgate):
    INDEX = 1
    REL = TOP
    TARGET_SYSTEM_NAME = 'sig13'


class BerlinSigma8Jumpgate(BerlinMember, main_objects.Jumpgate):
    INDEX = 2
    REL = BOTTOM
    TARGET_SYSTEM_NAME = 'sig8'


class BerlinDockring(BerlinMember, main_objects.LargePlanetDockring):
    BASE_INDEX = 1
    REL = RIGHT
    AUDIO_PREFIX = SpaceVoice.RH_PLANET
    INTERIOR_CLASS = interior.CustomFullSplitRoomInterior
    DEALERS = dealers.RheinlandPlanetDealers
    SHIP_SET = markets.ShipSet('rh_fighter', 'bw_elite', 'ge_csv')
    RU_NAME = 'Планета Берлин'

    BASE_PROPS = meta.LargePlanet(
        objectives=[
            meta.ProduceBest(DIAMONDS),
            meta.ProduceCheap(MOX_FUEL),
            meta.ProduceCheap(ROID_MINER_PARTS),
            meta.ProduceNormal(SMELTER_PARTS),
            meta.ProduceNormal(ENGINE_PARTS),
            meta.ProduceBad(GAS_MINER_PARTS),
            meta.ProduceBad(ELECTRONICS),
        ]
    )


class BerlinPrison(BerlinMember, main_objects.Prison):
    BASE_INDEX = 2
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = prisons.BerlinPrison
    INTERIOR_CLASS = interior.StationBshbarInterior
    DEALERS = dealers.RheinlandMilitaryDealers
    RU_NAME = 'Тюрьма Шверин'


class BerlinMegaStation(BerlinMember, main_objects.Station):
    BASE_INDEX = 4
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = potsdam.Potsdam
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.RheinlandCivilianDealers
    RU_NAME = 'Станция Потсдам'

    BASE_PROPS = meta.Megabase(
        objectives=[
            meta.ProduceBest(PROD_MACHINES),
            meta.ProduceNormal(TLR_PARTS),
            meta.ProduceBad(AMMUNITION),

            meta.HaveGreenhouse(),
            meta.HaveSolarPanels(),
            meta.SupportBattleships(),
        ]
    )


class BerlinOutpost(BerlinMember, main_objects.Outpost):
    BASE_INDEX = 6
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = police.BerlinPoliceOutpost
    INTERIOR_CLASS = interior.OutpostInterior
    AUDIO_PREFIX = SpaceVoice.BORDER_STATION
    DEALERS = dealers.RheinlandMilitaryDealers
    RU_NAME = 'Аванпост Бранденбург'


class BerlinShipyard(BerlinMember, main_objects.Shipyard):
    BASE_INDEX = 3
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = shipyards.CambridgeShipyard
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.RheinlandMilitaryDealers
    RU_NAME = 'Верфь Гамбург'


class BerlinTrading(BerlinMember, main_objects.TradingBase):
    BASE_INDEX = 9
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = trade_storages.TekagiStorage
    INTERIOR_CLASS = interior.BattleshipNoshipInterior
    DEALERS = dealers.RheinlandCivilianDealers
    FACTION = faction.RheinlandCivilians
    RU_NAME = 'Торговая база Бонн'


class BerlinRefinery(BerlinMember, main_objects.Refinery):
    BASE_INDEX = 7
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = stuttgart_megabase.MannhaimShortGasless
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.RheinlandCivilianDealers
    FACTION = faction.RheinlandCivilians
    RU_NAME = 'Станция Дрезден'

    BASE_PROPS = meta.Refinery(
        objectives=[
            meta.ProduceBad(ALLOY_HEAVY),
            meta.ProduceBad(ALLOY_TEMPERATURE),
        ]
    )


class BerlinJunkers(BerlinMember, main_objects.JunkerBase):
    BASE_INDEX = 8
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = junker.BerlinJunker
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.RheinlandPirateDealers
    FACTION = faction.Junkers
    ASTEROID_ZONES = [
        BerlinDebrisZone1
    ]
    DEFENCE_LEVEL = None

    RU_NAME = 'База Линц'


class BerlinPiratesTop(BerlinMember, main_objects.PirateAsteroid):
    BASE_INDEX = 5
    INDEX = 1
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = astbase.BerlinAsteroidBase
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.RheinlandPirateDealers
    FACTION = faction.RheinlandPirate
    AST_EXCLUSION_ZONE_SIZE = 2500
    ASTEROID_ZONES = [
        BerlinAsteroidZone1
    ]
    DEFENCE_LEVEL = None
    RU_NAME = 'База Ульм'


class BerlinPiratesBottom(BerlinMember, main_objects.PirateStation):
    BASE_INDEX = 10
    INDEX = 2
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = pirate.PirateBaseBizmark
    INTERIOR_CLASS = interior.PirateStationInterior
    DEALERS = dealers.RheinlandPirateDealers
    FACTION = faction.RheinlandPirate
    ASTEROID_ZONES = [
        BerlinDebrisZone5
    ]
    DEFENCE_LEVEL = None
    RU_NAME = 'База Вюрцбург'


class BerlinPlanet1(BerlinMember, main_objects.Planet):
    ARCHETYPE = 'planet_earthind_4000'
    SPHERE_RADIUS = 4000
    RELATED_DOCK_RING = BerlinDockring


class BerlinPlanet2(BerlinMember, main_objects.Planet):
    INDEX = 2
    ARCHETYPE = 'planet_icewatind_3000'
    PLANET_CIRCLE = False
    SPHERE_RADIUS = 3000
    RING = True
    RING_ZONE_ALIAS = 'ring'
    RING_ZONE_INDEX = 1
    RING_FILE_NAME = 'berlin'
    RU_NAME = 'Планета Линден'


class BerlinPlanet3(BerlinMember, main_objects.Planet):
    INDEX = 3
    ARCHETYPE = 'planet_ice_purple_1500'
    SPHERE_RADIUS = 1500
    RU_NAME = 'Планета Швабия'


class BerlinPlanet4(BerlinMember, main_objects.Planet):
    INDEX = 4
    ARCHETYPE = 'planet_gasgrncld_2500'
    SPHERE_RADIUS = 2500
    RU_NAME = 'Планета Фридрих'


class BerConnOutpost1(BerlinMember, main_objects.TradeConnection):
    OBJ_FROM = BerlinOutpost
    OBJ_TO = BerlinSigma13Jumpgate
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        BerlinPiratesTop
    ]
    OBJ_FROM_TLR_FORCE_OFFSET = (11400, 0, -31300)


class BerConnOutpost2(BerlinMember, main_objects.TradeConnection):
    OBJ_FROM = BerlinOutpost
    OBJ_TO = BerlinShipyard
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        BerlinPiratesTop
    ]


class BerConnOutpost3(BerlinMember, main_objects.TradeConnection):
    OBJ_FROM = BerlinOutpost
    OBJ_TO = BerlinDockring
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = BOTTOM


class BerConnShipPris(BerlinMember, main_objects.TradeConnection):
    OBJ_FROM = BerlinShipyard
    OBJ_TO = BerlinPrison
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        BerlinPiratesTop
    ]


class BerConnTrading1(BerlinMember, main_objects.TradeConnection):
    OBJ_FROM = BerlinTrading
    OBJ_TO = BerlinPrison
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        BerlinPiratesBottom
    ]


class BerConnTrading2(BerlinMember, main_objects.TradeConnection):
    OBJ_FROM = BerlinTrading
    OBJ_TO = BerlinSigma8Jumpgate
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'F'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        BerlinPiratesBottom
    ]


class BerConnTrading3(BerlinMember, main_objects.TradeConnection):
    OBJ_FROM = BerlinTrading
    OBJ_TO = BerlinMegaStation
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'G'
    HUNTER_DEFENCE_REL = BOTTOM


class BerConnStation1(BerlinMember, main_objects.TradeConnection):
    OBJ_FROM = BerlinMegaStation
    OBJ_TO = BerlinDockring
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'H'
    ATTACKED_BY = [
        BerlinJunkers
    ]


class BerConnStation2(BerlinMember, main_objects.TradeConnection):
    OBJ_FROM = BerlinMegaStation
    OBJ_TO = BerlinRefinery
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'I'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        BerlinJunkers
    ]
    OBJ_FROM_EXTRA_DRIFT = 5000
