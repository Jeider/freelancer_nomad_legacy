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
from templates.solar import hackable
from templates.nebula import rh_mnh_blue_nebula
from templates.nebula import exclusion

from templates.dockable import astbase
from templates.dockable import trading_outposts
from templates.dockable import station_debris
from templates.dockable import junker


class MunchMember(object):
    INDEX = 1
    ABSTRACT = False
    FACTION = faction.RH_GRP

    INTERIOR_BG1 = interior.INTERIOR_RH_MUNCHEN


class MunchRawText(MunchMember, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = rh_mnh
space_color = 5, 8, 10
local_faction = li_p_grp
space_farclip = 100000

[TexturePanels]
file = universe\heavens\shapes.ini

[Music]
space = music_omega_space
danger = music_omega_danger
battle = music_omega_battle

[Dust]
spacedust = Dust

[Ambient]
color = 15, 17, 20

[Background]
nebulae = solar\\stars_mod\\rh_mnh_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_rh_mnh_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
;property_flags = 512 ;lava - MILITARY
property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = rh_mnh_system_light
pos = -31, 0, -48
color = 250, 221, 124
range = 60000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION'''


class MunchBlueNebula(zones.NebulaZone):
    SPACEDUST = Dust.RADIOACTIVE_BLUE
    SPACEDUST_MAXPARTICLES = 50
    MUSIC = Ambience.BADLANDS
    INTERFERENCE = 0.5

    PROPERTY_FLAGS = 32768
    PROPERTY_FOG_COLOR = '5, 10, 50'


BLUE_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.LINES_EXCLUSION,
    'shell_scalar': 1,
    'max_alpha': 0.3,
    'exclusion_tint': '255, 255, 255',
    'fog_far': 5000,
}


BLUE_ALT_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.VORTEX_EXCLUSION,
    'shell_scalar': 1,
    'max_alpha': 0.3,
    'exclusion_tint': '255, 255, 255',
    'fog_far': 5000,
}


class MunchLargeNebula(MunchMember, MunchBlueNebula):
    INDEX = 1
    FILE_NAME = 'gen_rh_mnh_blue_nebula1'
    CONTENT_TEMPLATE = rh_mnh_blue_nebula.MunchenLargeBlueNebulaTemplate


class MunchSmallNebula(MunchMember, MunchBlueNebula):
    INDEX = 2
    FILE_NAME = 'gen_rh_mnh_blue_nebula2'
    CONTENT_TEMPLATE = rh_mnh_blue_nebula.MunchenLargeBlueNebulaTemplate


class MunchSun(MunchMember, main_objects.Sun):
    STAR = 'med_yellow_sun'
    LOADOUT = 'small_yellow_sun_fx'
    ATMOSHPERE_RANGE = 12000


class MunchBaseMinesZone(zones.AsteroidZone):
    ASTEROID_DEFINITION_CLASS = asteroid_definition.SpaceMines
    SPACEDUST = Dust.DEBRIS
    SPACEDUST_MAXPARTICLES = 100
    MUSIC = Ambience.MINE_AST
    INTERFERENCE = 0.1
    DRAG_MODIFIER = 1.5
    PROPERTY_FLAGS = 4128


class MunchBattleMinesZone1(MunchMember, MunchBaseMinesZone):
    ALIAS = 'mines'
    INDEX = 1


class MunchBattleMinesZone2(MunchMember, MunchBaseMinesZone):
    ALIAS = 'mines'
    INDEX = 2


class MunchBattleMinesZone3(MunchMember, MunchBaseMinesZone):
    ALIAS = 'mines'
    INDEX = 3


class MunchBattleMinesZone4(MunchMember, MunchBaseMinesZone):
    ALIAS = 'mines'
    INDEX = 4


class MunchBattleMinesZone5(MunchMember, MunchBaseMinesZone):
    ALIAS = 'mines'
    INDEX = 5


class MunchAsteroids1(MunchMember, zones.AsteroidZone):
    ALIAS = 'ast'
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = asteroid_definition.BadlansDynasteroids


class MunchBaseRheinlandHackableBattleship(main_objects.HackableBattleship):
    ALIAS = 'mines'
    HACKABLE_SOLAR_CLASS = hackable.HackableRheinlandBattleship
    INTERIOR_CLASS = interior.EquipDeckInterior
    AST_EXCLUSION_ZONE_SIZE = 600


class MunchBaseRheinlandLockedBattleship(main_objects.LockedBattleship):
    ALIAS = 'mines'
    ARCHETYPE = 'suprise_rh_battleship'
    INTERIOR_CLASS = interior.EquipDeckInterior
    AST_EXCLUSION_ZONE_SIZE = 600


class MunchBaseKusariHackableBattleship(main_objects.HackableBattleship):
    ALIAS = 'mines'
    HACKABLE_SOLAR_CLASS = hackable.HackableKusariBattleship
    INTERIOR_CLASS = interior.EquipDeckInterior
    AST_EXCLUSION_ZONE_SIZE = 600
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_KU


class MunchBaseKusariLockedBattleship(main_objects.LockedBattleship):
    ALIAS = 'mines'
    ARCHETYPE = 'suprise_ku_battleship'
    INTERIOR_CLASS = interior.EquipDeckInterior
    AST_EXCLUSION_ZONE_SIZE = 600
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_KU


class MunchBattleRuins1(MunchMember, MunchBaseRheinlandLockedBattleship):
    ALIAS = 'mines'
    INDEX = 1
    BASE_INDEX = 61

    ASTEROID_ZONES = [
        MunchBattleMinesZone1,
    ]


class MunchBattleRuins2(MunchMember, MunchBaseKusariLockedBattleship):
    ALIAS = 'mines'
    INDEX = 2
    BASE_INDEX = 62

    ASTEROID_ZONES = [
        MunchBattleMinesZone2,
    ]


class MunchBattleRuins3(MunchMember, MunchBaseRheinlandLockedBattleship):
    ALIAS = 'mines'
    INDEX = 3
    BASE_INDEX = 63

    ASTEROID_ZONES = [
        MunchBattleMinesZone3,
    ]


class MunchBattleRuins4(MunchMember, MunchBaseKusariLockedBattleship):
    ALIAS = 'mines'
    INDEX = 4
    BASE_INDEX = 64

    ASTEROID_ZONES = [
        MunchBattleMinesZone4,
    ]


class MunchBattleRuins5(MunchMember, MunchBaseRheinlandLockedBattleship):
    ALIAS = 'mines'
    INDEX = 5
    BASE_INDEX = 65

    ASTEROID_ZONES = [
        MunchBattleMinesZone5,
    ]


class MunchRheinlandSupriseRewards(MunchMember, mineable.DefaultSupriseRewardsGroup):
    NAME = 'rh_mnh_rheinland_suprise'
    SOLAR = suprise.RheinlandMainFighter
    REWARD_ITEM = None
    ULTRA_REWARD_BASES = [
        MunchBattleRuins1,
        # MunchBattleRuins2,
        MunchBattleRuins3,
        # MunchBattleRuins4,
        MunchBattleRuins5,
    ]


class MunchKusariSupriseRewards(MunchMember, mineable.DefaultSupriseRewardsGroup):
    NAME = 'rh_mnh_kusari_suprise'
    SOLAR = suprise.KusariMainFighter
    REWARD_ITEM = None
    ULTRA_REWARD_BASES = [
        # MunchBattleRuins1,
        MunchBattleRuins2,
        # MunchBattleRuins3,
        MunchBattleRuins4,
        # MunchBattleRuins5,
    ]


class MunchSolarSupriseField(mineable.DefaultField):
    BOX_SIZE = 400
    DENSITY_MULTIPLER = 4
    DRIFT_X = 0.5
    DRIFT_Y = 0.5
    DRIFT_Z = 0.5
    EMPTY_CHANCE = 0.2


class MunchBaseKusariSupriseField(mineable.SupriseRewardField):
    ALIAS = 'mines'
    FIELD_CLASS = MunchSolarSupriseField
    REWARDS_GROUP_CLASS = MunchKusariSupriseRewards
    ULTRA_REWARD = True


class MunchBaseRheinlandSupriseField(mineable.SupriseRewardField):
    ALIAS = 'mines'
    FIELD_CLASS = MunchSolarSupriseField
    REWARDS_GROUP_CLASS = MunchRheinlandSupriseRewards
    ULTRA_REWARD = True


class MunchSupriseRewardField1(MunchMember, MunchBaseRheinlandSupriseField):
    INDEX = 1
    ULTRA_BASE = MunchBattleRuins1


class MunchSupriseRewardField2(MunchMember, MunchBaseKusariSupriseField):
    INDEX = 2
    ULTRA_BASE = MunchBattleRuins2


class MunchSupriseRewardField3(MunchMember, MunchBaseRheinlandSupriseField):
    INDEX = 3
    ULTRA_BASE = MunchBattleRuins3


class MunchSupriseRewardField4(MunchMember, MunchBaseKusariSupriseField):
    INDEX = 4
    ULTRA_BASE = MunchBattleRuins4


class MunchSupriseRewardField5(MunchMember, MunchBaseRheinlandSupriseField):
    INDEX = 5
    ULTRA_BASE = MunchBattleRuins5


class MunchBizmarkJumpgate(MunchMember, main_objects.Jumpgate):
    INDEX = 1
    REL = RIGHT


class MunchHonshuJumpgate(MunchMember, main_objects.Jumpgate):
    INDEX = 2
    REL = LEFT


class MunchKoengisbergJumpgate(MunchMember, main_objects.Jumpgate):
    INDEX = 3
    REL = TOP
    LOCKED_DOCK = True


class MunchDockring(MunchMember, main_objects.Dockring):
    BASE_INDEX = 1
    REL = BOTTOM
    AUDIO_PREFIX = SpaceVoice.RH_PLANET
    INTERIOR_CLASS = interior.CustomFullSingleRoomInterior
    DEALERS = dealers.RheinlandPlanetDealers


class MunchTrading(MunchMember, main_objects.TradingBase):
    BASE_INDEX = 2
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = trading_outposts.LibertyTradingOutpost
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.RheinlandCivilianDealers


class MunchCivilianStationRuins(MunchMember, main_objects.NotDockableObject):
    ALIAS = 'ruins'
    INDEX = 1
    REL = TOP
    REL_DRIFT = 3000

    SPACE_OBJECT_TEMPLATE = station_debris.MunchenCivilianStationDebris

    # ASTEROID_ZONES = [
    #     Om15GasPocketsZone1,
    # ]


class MunchCivilianStationDropPoint1(MunchMember, main_objects.HackableStation):
    ALIAS = 'ruins_dock'
    INDEX = 1
    BASE_INDEX = 51
    RELATED_OBJECT = MunchCivilianStationRuins
    RELATED_OBJECT_INDEX = 0
    HACKABLE_SOLAR_CLASS = hackable.HackableOutpost
    INTERIOR_CLASS = interior.EquipDeckInterior


class MunchCivilianStationDropPoint2(MunchMember, main_objects.HackableStation):
    ALIAS = 'ruins_dock'
    INDEX = 2
    BASE_INDEX = 52
    RELATED_OBJECT = MunchCivilianStationRuins
    RELATED_OBJECT_INDEX = 1
    HACKABLE_SOLAR_CLASS = hackable.HackableOutpost
    INTERIOR_CLASS = interior.EquipDeckInterior


class MunchBattleStationRuins(MunchMember, main_objects.NotDockableObject):
    ALIAS = 'ruins'
    INDEX = 2
    REL = TOP

    SPACE_OBJECT_TEMPLATE = station_debris.MunchenBattleStationDebris


class MunchOutcastBase(MunchMember, main_objects.PirateBase):
    BASE_INDEX = 3
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = astbase.MunchenAsteroidBase
    FACTION = faction.PI_GRP  # TEMP

    DEFENCE_LEVEL = None

    AUDIO_PREFIX = SpaceVoice.OUTPOST
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.RheinlandPirateDealers

    ASTEROID_ZONES = [
        MunchAsteroids1
    ]
    AST_EXCLUSION_ZONE_SIZE = 2500

    EXCLUSION_PARAMS = BLUE_EXCLUSION_PARAMS
    NEBULA_ZONES = [
        MunchLargeNebula
    ]
    NEBULA_EXCLUSION_ZONE_SIZE = 2000


class MunchJunkersBase(MunchMember, main_objects.PirateBase):
    INDEX = 2
    BASE_INDEX = 4
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = junker.OmegaSmelter
    FACTION = faction.JUNK_GRP

    DEFENCE_LEVEL = None

    AUDIO_PREFIX = SpaceVoice.OUTPOST
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.RheinlandPirateDealers

    EXCLUSION_PARAMS = BLUE_ALT_EXCLUSION_PARAMS
    NEBULA_ZONES = [
        MunchSmallNebula
    ]
    NEBULA_EXCLUSION_ZONE_SIZE = 2000


class MunchPlanet1(MunchMember, main_objects.Planet):
    ARCHETYPE = 'planet_watblucld_3000'
    SPHERE_RADIUS = 3000
    RELATED_DOCK_RING = MunchDockring


class MunchPlanet2(MunchMember, main_objects.Planet):
    INDEX = 2
    ARCHETYPE = 'planet_moonblu_1000'
    SPHERE_RADIUS = 1000
    PLANET_CIRCLE = False


class MunchPlanet3(MunchMember, main_objects.Planet):
    INDEX = 3
    ARCHETYPE = 'planet_rckmnt_4000'
    SPHERE_RADIUS = 4000


class MunchCivRuinsConn1(MunchMember, main_objects.TradeConnection):
    OBJ_FROM = MunchCivilianStationRuins
    OBJ_TO = MunchBizmarkJumpgate
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        MunchOutcastBase,
    ]


class MunchCivRuinsConn2(MunchMember, main_objects.TradeConnection):
    OBJ_FROM = MunchCivilianStationRuins
    OBJ_TO = MunchDockring
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        MunchOutcastBase,
    ]


class MunchTradingConn1(MunchMember, main_objects.TradeConnection):
    OBJ_FROM = MunchTrading
    OBJ_TO = MunchDockring
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        MunchJunkersBase,
    ]


class MunchTradingConn2(MunchMember, main_objects.TradeConnection):
    OBJ_FROM = MunchTrading
    OBJ_TO = MunchHonshuJumpgate
    OBJ_FROM_TLR_FORCE_OFFSET = (-27000, 0, 22000)
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        MunchJunkersBase,
    ]


class MunchCivRuinsBrokenConn1(MunchMember, main_objects.BrokenTradeConnection):
    OBJ_FROM = MunchCivilianStationRuins
    OBJ_TO = MunchKoengisbergJumpgate
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'E'
    TLR_OUTER_ZONE = False


class MunchBattleStationRuinsBrokenConn1(MunchMember, main_objects.BrokenTradeConnection):
    OBJ_FROM = MunchBattleStationRuins
    OBJ_TO = MunchTrading
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'F'
    TLR_OUTER_ZONE = False


class MunchBattleStationRuinsBrokenConn2(MunchMember, main_objects.BrokenTradeConnection):
    OBJ_FROM = MunchBattleStationRuins
    OBJ_TO = MunchKoengisbergJumpgate
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'G'
    TLR_OUTER_ZONE = False
