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
from templates.solar import debris_box
from templates.nebula import li_mnh_nebula
from templates.nebula import exclusion

from templates.dockable import sphere_megabase
from templates.dockable import trade_storages
from templates.dockable import prisons
from templates.dockable import police
from templates.dockable import liberty_military
from templates.dockable import manhattan_megabase
from templates.dockable import forbes_megafactory
from templates.dockable import junker
from templates.dockable import pirate


class ManhMember(Member):
    FACTION = faction.LibertyMain
    WEAPON_FACTION = WEAPON_LI
    EQUIP_FACTION = EQUIP_LI


class ManhStaticText(ManhMember, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = li_mnh
space_color = 5, 15, 25
local_faction = li_grp
space_farclip = 70000

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Dust]
spacedust = Dust

[Music]
space = music_li_space
danger = music_li_danger
battle = music_li_battle

[Ambient]
; color = 150, 150, 150
color = 5, 15, 25  ;;prod
;color = 14, 16, 30

[Background]
nebulae = solar\\stars_mod\\li_mnh_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_li_mnh_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
property_flags = 512 ;lava - MILITARY
;property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = System_LIGHT_li_mnh
pos = 642, 0, 198
color = 255, 255, 255
range = 120000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION
'''


class ManhSun(ManhMember, main_objects.Sun):
    STAR = 'med_white_sun'
    LOADOUT = 'med_blue_sun_fx'



class ManhBaseBlueNebula(zones.NebulaZone):
    SPACEDUST = Dust.ATTRACT
    SPACEDUST_MAXPARTICLES = 40
    MUSIC = Ambience.NEBULA_CROW
    INTERFERENCE = 0.5

    PROPERTY_FLAGS = 32768
    PROPERTY_FOG_COLOR = '150, 100, 20'


class ManhLargeNebula(ManhMember, ManhBaseBlueNebula):
    INDEX = 1
    CONTENT_TEMPLATE = li_mnh_nebula.ManhattanNebulaTemplate


class ManhPirateNebula(ManhMember, ManhBaseBlueNebula):
    INDEX = 2
    CONTENT_TEMPLATE = li_mnh_nebula.ManhattanNebulaTemplate


CROW_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.CROW_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '100, 255, 155',
    'fog_far': 5000,
}


class ManhDebrisZone1(ManhMember, zones.DebrisZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class ManhDebrisZone2(ManhMember, zones.DebrisZone):
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class ManhDebrisZone3(ManhMember, zones.DebrisZone):
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class ManhDebrisZone4(ManhMember, zones.DebrisZone):
    INDEX = 4
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class ManhDebrisZone5(ManhMember, zones.DebrisZone):
    INDEX = 5
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class ManhBaseDebrisManufactoring(main_objects.DebrisManufactoring):
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


class ManhDebrisFactory1(ManhMember, ManhBaseDebrisManufactoring):
    INDEX = 1
    BASE_INDEX = 51
    ASTEROID_ZONES = [
        ManhDebrisZone1,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500


class ManhDebrisFactory2(ManhMember, ManhBaseDebrisManufactoring):
    INDEX = 2
    BASE_INDEX = 52
    ASTEROID_ZONES = [
        ManhDebrisZone2,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500


class ManhDebrisFactory3(ManhMember, ManhBaseDebrisManufactoring):
    INDEX = 3
    BASE_INDEX = 53
    ASTEROID_ZONES = [
        ManhDebrisZone3,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500


class ManhDebrisFactory4(ManhMember, ManhBaseDebrisManufactoring):
    INDEX = 4
    BASE_INDEX = 54
    ASTEROID_ZONES = [
        ManhDebrisZone4,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500


class ManhDebrisBoxReward(ManhMember, mineable.DefaultDebrisBoxRewardsGroup):
    NAME = 'li_mnh_debrisbox'
    SOLAR = debris_box.DebrisBox
    REWARD_ITEM = 'comm_scrap_metal'
    ULTRA_REWARD_BASES = [
        ManhDebrisFactory1,
        ManhDebrisFactory2,
        ManhDebrisFactory3,
        ManhDebrisFactory4,
    ]


class ManhBaseDebrisBoxRewardField(mineable.DebrisBoxRewardField):
    FIELD_CLASS = mineable.MineableDebrixBoxField
    REWARDS_GROUP_CLASS = ManhDebrisBoxReward
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class ManhDebrisBoxField1(ManhMember, ManhBaseDebrisBoxRewardField):
    INDEX = 1
    ULTRA_BASE = ManhDebrisFactory1


class ManhDebrisBoxField2(ManhMember, ManhBaseDebrisBoxRewardField):
    INDEX = 2
    ULTRA_BASE = ManhDebrisFactory2


class ManhDebrisBoxField3(ManhMember, ManhBaseDebrisBoxRewardField):
    INDEX = 3
    ULTRA_BASE = ManhDebrisFactory3


class ManhDebrisBoxField4(ManhMember, ManhBaseDebrisBoxRewardField):
    INDEX = 4
    ULTRA_BASE = ManhDebrisFactory4


class ManhSig17Jumpgate(ManhMember, main_objects.Jumpgate):
    INDEX = 1
    REL = BOTTOM
    TARGET_SYSTEM_NAME = 'sig17'


class ManhTau31Jumpgate(ManhMember, main_objects.Jumpgate):
    INDEX = 2
    REL = LEFT
    TARGET_SYSTEM_NAME = 'tau31'


class ManhDockring(ManhMember, main_objects.LargePlanetDockring):
    BASE_INDEX = 1
    REL = TOP
    AUDIO_PREFIX = SpaceVoice.LI_PLANET
    INTERIOR_CLASS = interior.CustomFullSplitRoomInterior
    DEALERS = dealers.LibertyPlanetDealers
    SHIP_SET = markets.ShipSet('li_fighter', 'ge_fighter3', 'li_freighter')

    BASE_PROPS = meta.ManhattanSuperPlanet(
        objectives=[
            meta.ProduceBest(LUXURY_GOODS),
            meta.ProduceCheap(ENGINE_PARTS),
            meta.ProduceCheap(MINING_EQUIPMENT),
            meta.ProduceNormal(LUXURY_GOLD),
            meta.ProduceBad(OPTICAL_CHIPS),
        ]
    )


class ManhMiningDockring(ManhMember, main_objects.MiningPlanetDockring):
    INDEX = 2
    BASE_INDEX = 2
    REL = RIGHT
    AUDIO_PREFIX = SpaceVoice.LI_PLANET
    INTERIOR_CLASS = interior.CustomFullSplitRoomInterior
    DEALERS = dealers.LibertyPlanetDealers
    SHIP_SET = markets.ShipSet('ge_csv')

    BASE_PROPS = meta.MiningPlanet(
        objectives=[
            meta.ProduceBest(NICOLLUM),
            meta.ProduceNormal(BERILIUM),
        ]
    )


class ManhShipyard(ManhMember, main_objects.Shipyard):
    BASE_INDEX = 3
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = manhattan_megabase.ManhattanMegabase
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.LibertyCivilianDealers

    BASE_PROPS = meta.Megabase(
        objectives=[
            meta.ProduceCheap(STATION_PANELS),
            meta.ProduceCheap(AMMUNITION),
            meta.HaveReactor(),
            meta.HaveGreenhouse(),
            meta.SupportBattleships(),
        ]
    )


class ManhProduction(ManhMember, main_objects.Station):
    BASE_INDEX = 4
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = forbes_megafactory.ForbesManufactoring
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.LibertyCivilianDealers


class ManhMilitary(ManhMember, main_objects.Station):
    ALIAS = 'military'
    BASE_INDEX = 5
    REL = LEFT
    SPACE_OBJECT_TEMPLATE = liberty_military.LibertyMilitary
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.LibertyMilitaryDealers


class ManhTrading(ManhMember, main_objects.TradingBase):
    BASE_INDEX = 6
    REL = LEFT
    SPACE_OBJECT_TEMPLATE = trade_storages.ManhattanStorage
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.LibertyCivilianDealers


class ManhPolice(ManhMember, main_objects.Outpost):
    ALIAS = 'police'
    BASE_INDEX = 7
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = police.PoliceOutpostLiberty
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.LibertyMilitaryDealers


class ManhRefinery(ManhMember, main_objects.Refinery):
    BASE_INDEX = 8
    REL = TOP
    SPACE_OBJECT_TEMPLATE = sphere_megabase.SphereRefinery
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.LibertyCivilianDealers

    BASE_PROPS = meta.Refinery(
        objectives=[
            meta.ProduceBad(ALLOY_RADIATION),
            meta.ProduceBad(ALLOY_CONDUCTOR),
            meta.ProduceBad(ALLOY_TEMPERATURE),
        ]
    )


class ManhPrison(ManhMember, main_objects.Prison):
    BASE_INDEX = 9
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = prisons.AlaskaPrison
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.LibertyMilitaryDealers

    NEBULA_ZONES = [
        ManhLargeNebula
    ]
    EXCLUSION_PARAMS = CROW_EXCLUSION_PARAMS


class ManhPlanet1(ManhMember, main_objects.Planet):
    ARCHETYPE = 'planet_earthgrncld_4000'
    SPHERE_RADIUS = 4000
    RELATED_DOCK_RING = ManhDockring


class ManhPlanet2(ManhMember, main_objects.Planet):
    INDEX = 2
    ARCHETYPE = 'planet_desored_3000'
    SPHERE_RADIUS = 3000
    RELATED_DOCK_RING = ManhMiningDockring


class ManhPlanet3(ManhMember, main_objects.Planet):
    INDEX = 3
    ARCHETYPE = 'planet_gaspurcld_3000'
    SPHERE_RADIUS = 3000
    RING = True
    RING_ZONE_ALIAS = 'ring'
    RING_ZONE_INDEX = 1
    RING_FILE_NAME = 'li_mmh'


class ManhPlanet4(ManhMember, main_objects.Planet):
    INDEX = 4
    ARCHETYPE = 'planet_crater_2000'
    SPHERE_RADIUS = 2000


class ManhJunkers(ManhMember, main_objects.JunkerBase):
    INDEX = 2
    BASE_INDEX = 10
    ALIAS = 'pirate'
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = junker.BerlinJunker
    FACTION = faction.LibertyPirate

    DEFENCE_LEVEL = None

    AUDIO_PREFIX = SpaceVoice.OUTPOST
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.LibertyPirateDealers

    ASTEROID_ZONES = [
        ManhDebrisZone5
    ]
    AST_EXCLUSION_ZONE_SIZE = 3000


class ManhNebulaPirates(ManhMember, main_objects.PirateStation):
    INDEX = 1
    BASE_INDEX = 11
    REL = TOP
    SPACE_OBJECT_TEMPLATE = pirate.ManhattanPirateBase
    FACTION = faction.LibertyPirate

    DEFENCE_LEVEL = None

    AUDIO_PREFIX = SpaceVoice.OUTPOST
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.LibertyPirateDealers

    NEBULA_ZONES = [
        ManhPirateNebula
    ]
    EXCLUSION_PARAMS = CROW_EXCLUSION_PARAMS


class ManhPoliceConn1(ManhMember, main_objects.TradeConnection):
    OBJ_FROM = ManhTau31Jumpgate
    OBJ_TO = ManhPolice
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        ManhNebulaPirates,
    ]


class ManhPoliceConn2(ManhMember, main_objects.TradeConnection):
    OBJ_FROM = ManhPolice
    OBJ_TO = ManhDockring
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'Z'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        ManhNebulaPirates,
    ]


class ManhProductionConn1(ManhMember, main_objects.TradeConnection):
    OBJ_FROM = ManhDockring
    OBJ_TO = ManhProduction
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = BOTTOM


class ManhProductionConn2(ManhMember, main_objects.TradeConnection):
    OBJ_FROM = ManhProduction
    OBJ_TO = ManhMiningDockring
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        ManhJunkers
    ]


class ManhProductionConn3(ManhMember, main_objects.TradeConnection):
    OBJ_FROM = ManhRefinery
    OBJ_TO = ManhProduction
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        ManhJunkers
    ]


class ManhProductionConn4(ManhMember, main_objects.TradeConnection):
    OBJ_FROM = ManhProduction
    OBJ_TO = ManhShipyard
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        ManhJunkers
    ]


class ManhTradingConn1(ManhMember, main_objects.TradeConnection):
    OBJ_FROM = ManhMilitary
    OBJ_TO = ManhTrading
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'F'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        ManhNebulaPirates
    ]


class ManhTradingConn2(ManhMember, main_objects.TradeConnection):
    OBJ_FROM = ManhTrading
    OBJ_TO = ManhShipyard
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'G'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        ManhNebulaPirates
    ]


class ManhTradingConn3(ManhMember, main_objects.TradeConnection):
    OBJ_FROM = ManhDockring
    OBJ_TO = ManhTrading
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'H'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        ManhNebulaPirates
    ]


class ManhTradingConn4(ManhMember, main_objects.TradeConnection):
    OBJ_FROM = ManhTrading
    OBJ_TO = ManhPrison
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'I'


class ManhShipyardConn1(ManhMember, main_objects.TradeConnection):
    OBJ_FROM = ManhShipyard
    OBJ_TO = ManhSig17Jumpgate
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'J'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        ManhJunkers
    ]
