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
from universe.audio.space_voice import SpaceVoice
from universe import faction
from universe.content import mineable
from templates.solar import debris_box
from templates.solar import suprise
from templates.nebula import ku_hns_nebula
from templates.nebula import exclusion

from templates.dockable import shipyards
from templates.dockable import prisons
from templates.dockable import police
from templates.dockable import honshu_military
from templates.dockable import junker
from templates.dockable import cambridge_research


class HonsMember(Member):
    FACTION = faction.KusariMain
    INTERIOR_BG1 = interior.INTERIOR_KU_HONSHU
    WEAPON_FACTION = WEAPON_KU
    EQUIP_FACTION = EQUIP_KU


class HonsStaticText(HonsMember, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = ku_hns
space_color = 10, 10, 25
local_faction = ku_grp
space_farclip = 60000

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Dust]
spacedust = Dust

[Music]
space = music_ku_space
danger = music_ku_danger
battle = music_ku_battle

[Ambient]
color = 5, 15, 15

[Background]
nebulae = solar\\stars_mod\\ku_hns_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_ku_hns_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
property_flags = 512 ;lava - MILITARY
;property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = ku_hns_system_light
pos = -31, 0, -48
color = 190, 210, 255
range = 120000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION
'''


class HonsSun(HonsMember, main_objects.Sun):
    STAR = 'Ku04_Sun'
    LOADOUT = 'large_blue_sun_fx'


class HonsBaseBlueNebula(zones.NebulaZone):
    SPACEDUST = Dust.ATTRACT
    SPACEDUST_MAXPARTICLES = 40
    MUSIC = Ambience.NEBULA_DMATTER
    INTERFERENCE = 0.5

    PROPERTY_FLAGS = 32768
    PROPERTY_FOG_COLOR = '150, 100, 20'


class HonsSouthNebula(HonsMember, HonsBaseBlueNebula):
    INDEX = 1
    CONTENT_TEMPLATE = ku_hns_nebula.HonshuLargeBlueNebulaTemplate


BLUE_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.GENERIC_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '60, 60, 90',
    'fog_far': 5000,
}


class HonsDebrisZone1(HonsMember, zones.DebrisZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class HonsDebrisZone2(HonsMember, zones.DebrisZone):
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class HonsDebrisZone3(HonsMember, zones.DebrisZone):
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class HonsDebrisZone4(HonsMember, zones.DebrisZone):
    INDEX = 4
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class HonsBaseDebrisManufactoring(main_objects.DebrisManufactoring):
    ALIAS = 'deb'
    ROTATE_RANDOM = True
    ARCHETYPE = 'mplatform'
    LOADOUT = 'mplatform_ku_debris'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    AST_EXCLUSION_ZONE_SIZE = 2000
    AST_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.RADIOACTIVE_RED,
        'spacedust_maxparticles': 200,
    }


class HonsDebrisFactory1(HonsMember, HonsBaseDebrisManufactoring):
    INDEX = 1
    BASE_INDEX = 51
    ASTEROID_ZONES = [
        HonsDebrisZone1,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500


class HonsDebrisFactory2(HonsMember, HonsBaseDebrisManufactoring):
    INDEX = 2
    BASE_INDEX = 52
    ASTEROID_ZONES = [
        HonsDebrisZone2,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500


class HonsDebrisFactory3(HonsMember, HonsBaseDebrisManufactoring):
    INDEX = 3
    BASE_INDEX = 53
    ASTEROID_ZONES = [
        HonsDebrisZone3,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500


class HonsDebrisBoxReward(HonsMember, mineable.DefaultDebrisBoxRewardsGroup):
    NAME = 'ku_hns_debrisbox'
    SOLAR = debris_box.DebrisBox
    REWARD_ITEM = 'comm_scrap_metal'
    ULTRA_REWARD_BASES = [
        HonsDebrisFactory1,
        HonsDebrisFactory2,
        HonsDebrisFactory3,
    ]


class HonsBaseDebrisBoxRewardField(mineable.DebrisBoxRewardField):
    FIELD_CLASS = mineable.MineableDebrixBoxField
    REWARDS_GROUP_CLASS = HonsDebrisBoxReward
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class HonsDebrisBoxField1(HonsMember, HonsBaseDebrisBoxRewardField):
    INDEX = 1
    ULTRA_BASE = HonsDebrisFactory1


class HonsDebrisBoxField2(HonsMember, HonsBaseDebrisBoxRewardField):
    INDEX = 2
    ULTRA_BASE = HonsDebrisFactory2


class HonsDebrisBoxField3(HonsMember, HonsBaseDebrisBoxRewardField):
    INDEX = 3
    ULTRA_BASE = HonsDebrisFactory3


class HonsBaseSolarPlant(main_objects.SolarPlant):
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


class HonsBaseMinesZone(zones.AsteroidZone):
    ASTEROID_DEFINITION_CLASS = asteroid_definition.SpaceMines
    SPACEDUST = Dust.DEBRIS
    SPACEDUST_MAXPARTICLES = 100
    MUSIC = Ambience.MINE_AST
    INTERFERENCE = 0.1
    DRAG_MODIFIER = 1.5
    PROPERTY_FLAGS = 4128


class HonsSolarMinesZone1(HonsMember, HonsBaseMinesZone):
    ALIAS = 'solar'
    INDEX = 1


class HonsSolarMinesZone2(HonsMember, HonsBaseMinesZone):
    ALIAS = 'solar'
    INDEX = 2


class HonsSolarMinesZone3(HonsMember, HonsBaseMinesZone):
    ALIAS = 'solar'
    INDEX = 3


class HonsSolarMinesZone4(HonsMember, HonsBaseMinesZone):
    ALIAS = 'solar'
    INDEX = 4


class HonsSolarMinesZone5(HonsMember, HonsBaseMinesZone):
    ALIAS = 'solar'
    INDEX = 5


class HonsSolarPlant1(HonsMember, HonsBaseSolarPlant):
    INDEX = 1
    BASE_INDEX = 61
    ASTEROID_ZONES = [
        HonsSolarMinesZone1,
    ]


class HonsSolarPlant2(HonsMember, HonsBaseSolarPlant):
    INDEX = 2
    BASE_INDEX = 62
    ASTEROID_ZONES = [
        HonsSolarMinesZone2,
    ]


class HonsSolarPlant3(HonsMember, HonsBaseSolarPlant):
    INDEX = 3
    BASE_INDEX = 63
    ASTEROID_ZONES = [
        HonsSolarMinesZone3,
    ]


class HonsSolarPlant4(HonsMember, HonsBaseSolarPlant):
    INDEX = 4
    BASE_INDEX = 64
    ASTEROID_ZONES = [
        HonsSolarMinesZone4,
    ]


class HonsSolarPlant5(HonsMember, HonsBaseSolarPlant):
    INDEX = 5
    BASE_INDEX = 65
    ASTEROID_ZONES = [
        HonsSolarMinesZone5,
    ]


class HonsSolarSupriseRewards(HonsMember, mineable.DefaultSupriseRewardsGroup):
    NAME = 'ku_hns_solar_suprise'
    SOLAR = suprise.KusariMiscFighter
    REWARD_ITEM = None
    ULTRA_REWARD_BASES = [
        HonsSolarPlant1,
        HonsSolarPlant2,
        HonsSolarPlant3,
        HonsSolarPlant4,
        HonsSolarPlant5,
    ]


class HonsSolarSupriseField(mineable.DefaultField):
    BOX_SIZE = 400
    DENSITY_MULTIPLER = 4
    DRIFT_X = 0.5
    DRIFT_Y = 0.5
    DRIFT_Z = 0.5
    EMPTY_CHANCE = 0.2


class HonsBaseSolarSupriseRewardField(mineable.SupriseRewardField):
    ALIAS = 'solar'
    FIELD_CLASS = HonsSolarSupriseField
    REWARDS_GROUP_CLASS = HonsSolarSupriseRewards
    ULTRA_REWARD = True


class HonsSolarSupriseRewardField1(HonsMember, HonsBaseSolarSupriseRewardField):
    INDEX = 1
    ULTRA_BASE = HonsSolarPlant1


class HonsSolarSupriseRewardField2(HonsMember, HonsBaseSolarSupriseRewardField):
    INDEX = 2
    ULTRA_BASE = HonsSolarPlant2


class HonsSolarSupriseRewardField3(HonsMember, HonsBaseSolarSupriseRewardField):
    INDEX = 3
    ULTRA_BASE = HonsSolarPlant3


class HonsSolarSupriseRewardField4(HonsMember, HonsBaseSolarSupriseRewardField):
    INDEX = 4
    ULTRA_BASE = HonsSolarPlant4


class HonsSolarSupriseRewardField5(HonsMember, HonsBaseSolarSupriseRewardField):
    INDEX = 5
    ULTRA_BASE = HonsSolarPlant5


class HonsTekagiJumpgate(HonsMember, main_objects.Jumpgate):
    INDEX = 1
    REL = BOTTOM
    TARGET_SYSTEM_NAME = 'ku_tgk'


class HonsSiriusJumpgate(HonsMember, main_objects.Jumpgate):
    INDEX = 2
    REL = TOP
    TARGET_SYSTEM_NAME = 'sig42'


class HonsMunchenJumpgate(HonsMember, main_objects.Jumpgate):
    INDEX = 3
    REL = RIGHT
    TARGET_SYSTEM_NAME = 'rh_mnh'


class HonsDockring(HonsMember, main_objects.LargePlanetDockring):
    BASE_INDEX = 1
    REL = LEFT
    AUDIO_PREFIX = SpaceVoice.KU_PLANET
    INTERIOR_CLASS = interior.CustomFullSplitRoomInterior
    DEALERS = dealers.KusariPlanetDealers

    BASE_PROPS = meta.LargePlanet(
        objectives=[
            meta.ProduceBest(SOLAR_PLANT_PARTS),
            meta.ProduceBest(RESEARCH_EQUIP),
            meta.ProduceNormal(ROID_MINER_PARTS),
            meta.ProduceNormal(ENGINE_PARTS),
            meta.ProduceBad(MINING_EQUIPMENT),
        ]
    )


class HonsMilitary(HonsMember, main_objects.Station):
    BASE_INDEX = 2
    REL = BOTTOM
    REL_DRIFT = 500
    SPACE_OBJECT_TEMPLATE = honshu_military.HonshuMilitary
    INTERIOR_CLASS = interior.StationShipdealerInterior
    DEALERS = dealers.KusariMilitaryDealers

    BASE_PROPS = meta.MediumStation(
        objectives=[
            meta.SupportBattleships(),
            meta.ConsumeHeavyMunitions(),
        ]
    )


class HonsShipyard(HonsMember, main_objects.Shipyard):
    BASE_INDEX = 3
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = shipyards.HokkaidoShipyard
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.KusariCivilianDealers


class HonsPrison(HonsMember, main_objects.Prison):
    BASE_INDEX = 4
    REL = LEFT
    SPACE_OBJECT_TEMPLATE = prisons.HonshuPrison
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.KusariMilitaryDealers


class HonsPolice(HonsMember, main_objects.Outpost):
    ALIAS = 'police'
    BASE_INDEX = 5
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = police.StuttgartPoliceOutpost
    INTERIOR_CLASS = interior.OutpostShipdealerInterior
    AUDIO_PREFIX = SpaceVoice.BORDER_STATION
    DEALERS = dealers.KusariMilitaryDealers


class HonsTrading(HonsMember, main_objects.TradingBase):
    BASE_INDEX = 6
    REL = BOTTOM
    REL_APPEND = 2500
    SPACE_OBJECT_TEMPLATE = cambridge_research.CambridgeResearchAlternative
    INTERIOR_CLASS = interior.StationShipdealerInterior
    DEALERS = dealers.KusariCivilianDealers

    BASE_PROPS = meta.TradingBase(
        objectives=[
            meta.HaveGreenhouse(),
        ]
    )


class HonsPlanet1(HonsMember, main_objects.Planet):
    ARCHETYPE = 'planet_watbluislcld_4000'
    SPHERE_RADIUS = 4000
    RELATED_DOCK_RING = HonsDockring


class HonsPlanet2(HonsMember, main_objects.Planet):
    INDEX = 2
    ARCHETYPE = 'planet_desorcld_3000'
    SPHERE_RADIUS = 3000


class HonsPlanet3(HonsMember, main_objects.Planet):
    INDEX = 3
    ARCHETYPE = 'planet_gasblucld_5000'
    SPHERE_RADIUS = 5000


class HonsPlanet4(HonsMember, main_objects.Planet):
    INDEX = 4
    ARCHETYPE = 'planet_gasgrncld_3000'
    SPHERE_RADIUS = 3000


class HonsNebulaPirates(HonsMember, main_objects.PirateStation):
    INDEX = 1
    BASE_INDEX = 7
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = junker.HonshuJunker
    FACTION = faction.KusariPirate

    DEFENCE_LEVEL = None

    AUDIO_PREFIX = SpaceVoice.OUTPOST
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.KusariPirateDealers

    NEBULA_ZONES = [
        HonsSouthNebula
    ]
    EXCLUSION_PARAMS = BLUE_EXCLUSION_PARAMS
    NEBULA_EXCLUSION_ZONE_SIZE = 2000


class HonsJunkers(HonsMember, main_objects.JunkerBase):
    INDEX = 2
    BASE_INDEX = 8
    ALIAS = 'pirate'
    REL = TOP
    SPACE_OBJECT_TEMPLATE = junker.StuttgartJunker
    FACTION = faction.KusariPirate

    DEFENCE_LEVEL = None

    AUDIO_PREFIX = SpaceVoice.OUTPOST
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.KusariPirateDealers

    ASTEROID_ZONES = [
        HonsDebrisZone4
    ]
    AST_EXCLUSION_ZONE_SIZE = 2500


class HonsTradingConn1(HonsMember, main_objects.TradeConnection):
    OBJ_FROM = HonsSiriusJumpgate
    OBJ_TO = HonsTrading
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        HonsJunkers
    ]


class HonsTradingConn2(HonsMember, main_objects.TradeConnection):
    OBJ_FROM = HonsDockring
    OBJ_TO = HonsTrading
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        HonsJunkers
    ]


class HonsTradingConn3(HonsMember, main_objects.TradeConnection):
    OBJ_FROM = HonsTrading
    OBJ_TO = HonsPolice
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        HonsJunkers
    ]


class HonsPrisonConn1(HonsMember, main_objects.TradeConnection):
    OBJ_FROM = HonsDockring
    OBJ_TO = HonsPrison
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = LEFT


class HonsPrisonConn2(HonsMember, main_objects.TradeConnection):
    OBJ_FROM = HonsPrison
    OBJ_TO = HonsTekagiJumpgate
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        HonsNebulaPirates
    ]


class HonsPrisonConn3(HonsMember, main_objects.TradeConnection):
    OBJ_FROM = HonsPrison
    OBJ_TO = HonsShipyard
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'F'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        HonsNebulaPirates
    ]


class HonsShipyardConn1(HonsMember, main_objects.TradeConnection):
    OBJ_FROM = HonsPolice
    OBJ_TO = HonsShipyard
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'G'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        HonsNebulaPirates
    ]


class HonsShipyardConn2(HonsMember, main_objects.TradeConnection):
    OBJ_FROM = HonsShipyard
    OBJ_TO = HonsMilitary
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'H'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        HonsNebulaPirates
    ]


class HonsPoliceConn1(HonsMember, main_objects.TradeConnection):
    OBJ_FROM = HonsPolice
    OBJ_TO = HonsMunchenJumpgate
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'I'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        HonsJunkers
    ]

