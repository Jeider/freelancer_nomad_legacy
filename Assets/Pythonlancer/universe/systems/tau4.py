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
from templates.solar import suprise
from templates.nebula import tau4_nebula
from templates.nebula import exclusion

from templates.dockable import trade_storages
from templates.dockable import ulster_megabase
from templates.dockable import pirate

from text.strings import MultiString as MS


class Tau4Member(Member):
    FACTION = faction.KusariMain
    INTERIOR_BG1 = interior.INTERIOR_TAU4
    WEAPON_FACTION = WEAPON_KU
    EQUIP_FACTION = EQUIP_KU


class Tau4StaticText(Tau4Member, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = tau4
space_color = 50, 35, 20
local_faction = ku_grp
space_farclip = 50000

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Dust]
spacedust = Dust

[Music]
space = music_tau_space
danger = music_tau_danger
battle = music_tau_battle

[Ambient]
color = 40, 27, 12

[Background]
nebulae = solar\\stars_mod\\tau4_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_tau4_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
;property_flags = 512 ;lava - MILITARY
property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = tau4_system_light
pos = 0, 2, 0
color = 255, 200, 200
range = 150000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION
'''


class Tau4AsteroidDefinition1(asteroid_definition.TekagiAsteroidDefinition):
    BELT = True
    BILLBOARDS = True
    DYNAST = True
    LOOT = False  # TEMP


class Tau4AsteroidZone1(Tau4Member, zones.AsteroidZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = Tau4AsteroidDefinition1


class Tau4AbandonedAstBase1(Tau4Member, main_objects.AbandonedAsteroid):
    ALIAS = 'ast'
    INDEX = 1
    BASE_INDEX = 51
    ROTATE_RANDOM = True
    ARCHETYPE = 'miningbase_mineableA'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True
    RU_NAME = MS('База Мацуяма', "Matsuyama Base")

    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        Tau4AsteroidZone1,
    ]
    AST_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.ASTEROID,
        'spacedust_maxparticles': 200,
    }
    MISC_EQUIP_TYPE = KU_PIRATE
    WEAPON_FACTION = WEAPON_KU
    EQUIP_SET = markets.EquipSet(
        Q.Gun('ku_pirategun', eq_classes=markets.SECRET3),
        Q.Engine(None, eq_classes=markets.SECRET2),
    )


class Tau4AsteroidReward(Tau4Member, mineable.AsteroidRewardsGroupUltra):
    NAME = 'tau4_unlock'
    SOLAR = asteroid.AsteroidTekagi
    REWARD_ITEM = 'comm_roid_uranium'
    ULTRA_REWARD_BASES = [
        Tau4AbandonedAstBase1,
    ]


class Tau4MineableField(mineable.MineableAsteroidField):
    BOX_SIZE = 1400
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.3
    DRIFT_Y = 0
    DRIFT_Z = 0.3


class Tau4BaseAsteroidRewardField(mineable.AsteroidRewardField):
    ALIAS = 'ast'
    FIELD_CLASS = Tau4MineableField
    REWARDS_GROUP_CLASS = Tau4AsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class Tau4RewardAsteroids1(Tau4Member, Tau4BaseAsteroidRewardField):
    INDEX = 1
    ULTRA_BASE = Tau4AbandonedAstBase1


class Tau4Sun(Tau4Member, main_objects.Sun):
    STAR = 'Bw10_Sun'
    LOADOUT = 'small_blue_sun_fx'


class Tau4BaseWhiteNebula(zones.NebulaZone):
    MUSIC = Ambience.NEBULA_BARRIER
    INTERFERENCE = 0.5

    PROPERTY_FLAGS = 32768
    PROPERTY_FOG_COLOR = '150, 100, 20'


class Tau4SouthWestNebula(Tau4Member, Tau4BaseWhiteNebula):
    INDEX = 1
    CONTENT_TEMPLATE = tau4_nebula.Tau4WhiteNebulaTemplate


class Tau4XenosNorthNebula(Tau4Member, Tau4BaseWhiteNebula):
    INDEX = 2
    CONTENT_TEMPLATE = tau4_nebula.Tau4WhiteNebulaTemplate


class Tau4CorsairJumpNebula(Tau4Member, Tau4BaseWhiteNebula):
    INDEX = 3
    CONTENT_TEMPLATE = tau4_nebula.Tau4WhiteNebulaTemplate


WHITE_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.GENERIC_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '95, 73, 67',
    'fog_far': 5000,
}


class Tau4BasePrisonLiner(main_objects.LockedLuxury):
    ALIAS = 'prison_liner'
    ROTATE_RANDOM = True
    ARCHETYPE = 'suprise_prison_liner'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True
    AST_EXCLUSION_ZONE_SIZE = 600

    NEBULA_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.RADIOACTIVE_RED,
        'spacedust_maxparticles': 200,
    }


class Tau4BaseMinesZone(zones.AsteroidZone):
    ASTEROID_DEFINITION_CLASS = asteroid_definition.SpaceMines
    ALIAS = 'prison_liner'
    SPACEDUST = Dust.DEBRIS
    SPACEDUST_MAXPARTICLES = 100
    MUSIC = Ambience.MINE_AST
    INTERFERENCE = 0.1
    DRAG_MODIFIER = 1.5
    PROPERTY_FLAGS = 4128


class Tau4PrisonLinerMinesZone1(Tau4Member, Tau4BaseMinesZone):
    INDEX = 1


class Tau4PrisonLinerMinesZone2(Tau4Member, Tau4BaseMinesZone):
    INDEX = 2


class Tau4PrisonLiner1(Tau4Member, Tau4BasePrisonLiner):
    INDEX = 1
    BASE_INDEX = 52
    ASTEROID_ZONES = [
        Tau4PrisonLinerMinesZone1,
    ]
    RU_NAME = MS('Тюремный лайнер Такасэбунэ', 'Prison Liner Takasebune')
    MISC_EQUIP_TYPE = KU_PIRATE
    WEAPON_FACTION = WEAPON_KU
    EQUIP_SET = markets.EquipSet(
        Q.GenericLauncher(FAST_MISSILE, eq_classes=markets.MISSILE),
        Q.PlayerArmor(None, eq_classes=markets.SECRET3),
    )


class Tau4PrisonLiner2(Tau4Member, Tau4BasePrisonLiner):
    INDEX = 2
    BASE_INDEX = 53
    ASTEROID_ZONES = [
        Tau4PrisonLinerMinesZone2,
    ]
    RU_NAME = MS('Тюремный лайнер Сюинсэн', 'Prison Liner Shuinsen')
    MISC_EQUIP_TYPE = KU_PIRATE
    WEAPON_FACTION = WEAPON_KU
    EQUIP_SET = markets.EquipSet(
        Q.Gun('ku_huntergun', eq_classes=markets.SECRET3),
        Q.PlayerArmor(None, eq_classes=markets.SECRET2),
    )


class Tau4LinerSupriseRewards(Tau4Member, mineable.DefaultSupriseRewardsGroup):
    NAME = 'tau4_prison_liner_suprise'
    SOLAR = suprise.KusariAllFighter
    REWARD_ITEM = None
    ULTRA_REWARD_BASES = [
        Tau4PrisonLiner1,
        Tau4PrisonLiner2,
    ]


class Tau4PrisonLinerSupriseField(mineable.DefaultField):
    BOX_SIZE = 400
    DENSITY_MULTIPLER = 4
    DRIFT_X = 0.5
    DRIFT_Y = 0.5
    DRIFT_Z = 0.5
    EMPTY_CHANCE = 0.2


class Tau4BaseLinerSupriseRewardField(mineable.SupriseRewardField):
    ALIAS = 'prison_liner'
    FIELD_CLASS = Tau4PrisonLinerSupriseField
    REWARDS_GROUP_CLASS = Tau4LinerSupriseRewards
    ULTRA_REWARD = True


class Tau4LinerSupriseRewardField1(Tau4Member, Tau4BaseLinerSupriseRewardField):
    INDEX = 1
    ULTRA_BASE = Tau4PrisonLiner1


class Tau4LinerSupriseRewardField2(Tau4Member, Tau4BaseLinerSupriseRewardField):
    INDEX = 2
    ULTRA_BASE = Tau4PrisonLiner2


class Tau4KyushuJumpgate(Tau4Member, main_objects.Jumpgate):
    INDEX = 1
    REL = LEFT
    TARGET_SYSTEM_NAME = 'ku_ksu'


class Tau4HokkaidoJumpgate(Tau4Member, main_objects.Jumpgate):
    INDEX = 2
    REL = RIGHT
    TARGET_SYSTEM_NAME = 'ku_hkd'


class Tau4Station(Tau4Member, main_objects.TradelaneSupportStation):
    BASE_INDEX = 1
    REL = TOP
    SPACE_OBJECT_TEMPLATE = ulster_megabase.UlsterShortBase
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.KusariCivilianDealers
    RU_NAME = MS('Станция +Осака', 'Osaka Station')

    BASE_PROPS = meta.TradelaneSupportStation(
        objectives=[
            meta.HaveGreenhouse(),
        ]
    )


class Tau4Freeport(Tau4Member, main_objects.Freeport):
    BASE_INDEX = 2
    REL = BOTTOM
    REL_APPEND = 2500
    SPACE_OBJECT_TEMPLATE = trade_storages.LibertyLongStorage
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.KusariCivilianDealers
    RU_NAME = MS('Фрипорт Окинава', 'Freeport Okinawa')


class Tau4Battleship(Tau4Member, main_objects.KusariBattleship):
    BASE_INDEX = 3
    REL = BOTTOM
    REL_APPEND = 2500
    INTERIOR_CLASS = interior.BattleshipInterior
    DEALERS = dealers.KusariMilitaryDealers
    SHIP_SET = markets.ShipSet('ku_elite')
    RU_NAME = MS('Линкор Ямасиро', "Battleship Yamashiro")


class Tau4Planet1(Tau4Member, main_objects.Planet):
    ARCHETYPE = 'planet_desorcld_3000'
    SPHERE_RADIUS = 3000
    RU_NAME = MS('Планета Сайтама', 'Planet Saitama')


class Tau4Planet2(Tau4Member, main_objects.Planet):
    INDEX = 2
    ARCHETYPE = 'planet_icemntcld_4000'
    SPHERE_RADIUS = 4000
    RU_NAME = MS('Планета Гумма', 'Planet Gumma')


class Tau4Planet3(Tau4Member, main_objects.Planet):
    INDEX = 3
    ARCHETYPE = 'planet_icewatcld_3000'
    SPHERE_RADIUS = 3000
    RU_NAME = MS('Планета Хёгу', 'Planet Hyogu')


class Tau4SouthPirates(Tau4Member, main_objects.PirateStation):
    INDEX = 1
    BASE_INDEX = 4
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = pirate.PirateBaseBizmark
    FACTION = faction.Corsairs

    DEFENCE_LEVEL = None
    RU_NAME = MS('База Муцуэ', "Mutsue Base")

    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.KusariPirateDealers

    NEBULA_ZONES = [
        Tau4SouthWestNebula
    ]
    EXCLUSION_PARAMS = WHITE_EXCLUSION_PARAMS
    NEBULA_EXCLUSION_ZONE_SIZE = 2000


class Tau4Xenos(Tau4Member, main_objects.PirateStation):
    INDEX = 2
    BASE_INDEX = 5
    REL = TOP
    SPACE_OBJECT_TEMPLATE = pirate.PirateBaseCalifornia
    FACTION = faction.Xenos
    RU_NAME = MS('База Сингапур', 'Singapore Base')

    DEFENCE_LEVEL = None

    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.KusariPirateDealers

    NEBULA_ZONES = [
        Tau4XenosNorthNebula
    ]
    EXCLUSION_PARAMS = WHITE_EXCLUSION_PARAMS


class Tau4BattleshipRuins1(Tau4Member, main_objects.HackableBattleship):
    ALIAS = 'bship_ruins'
    INDEX = 1
    BASE_INDEX = 61
    REL = BOTTOM
    HACKABLE_SOLAR_CLASS = hackable.HackableKusariBattleship
    INTERIOR_CLASS = interior.EquipDeckInterior
    RU_NAME = MS('Линкор Ямато', "Battleship Yamato")

    MISC_EQUIP_TYPE = KU_PIRATE
    WEAPON_FACTION = WEAPON_KU
    EQUIP_SET = markets.EquipSet(
        Q.GenericLauncher(FAST_MISSILE, eq_classes=markets.MISSILE),
        Q.PlayerArmor(None, eq_classes=markets.SECRET1),
    )


class Tau4LuxuryRuins1(Tau4Member, main_objects.HackableLuxury):
    ALIAS = 'luxury'
    INDEX = 1
    BASE_INDEX = 62
    REL = TOP
    HACKABLE_SOLAR_CLASS = hackable.HackableLuxuryLiner
    INTERIOR_CLASS = interior.EquipDeckInterior
    RU_NAME = MS('Круизный лайнер Филиппины', 'Cruise Liner Philippines')

    MISC_EQUIP_TYPE = KU_PIRATE
    WEAPON_FACTION = WEAPON_KU
    EQUIP_SET = markets.EquipSet(
        Q.Gun('ku_civgun', eq_classes=markets.SECRET3),
        Q.Engine(None, eq_classes=markets.SECRET3),
    )


class Tau4StationConn1(Tau4Member, main_objects.TradeConnection):
    OBJ_FROM = Tau4KyushuJumpgate
    OBJ_TO = Tau4Station
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        Tau4SouthPirates
    ]


class Tau4StationConn2(Tau4Member, main_objects.TradeConnection):
    OBJ_FROM = Tau4Station
    OBJ_TO = Tau4Freeport
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        Tau4SouthPirates
    ]


class Tau4BattleshipConn1(Tau4Member, main_objects.TradeConnection):
    OBJ_FROM = Tau4Freeport
    OBJ_TO = Tau4Battleship
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        Tau4SouthPirates
    ]


class Tau4BattleshipConn2(Tau4Member, main_objects.TradeConnection):
    OBJ_FROM = Tau4Battleship
    OBJ_TO = Tau4HokkaidoJumpgate
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        Tau4Xenos
    ]


class Tau4SpragueConn1(Tau4Member, main_objects.AbandonedBuoyTradeConnection):
    OBJ_FROM = Tau4Station
    OBJ_TO = Tau4LuxuryRuins1
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'E'
    ATTACKED_BY = [
        Tau4Xenos
    ]


class Tau4BattleshipRuinsConn1(Tau4Member, main_objects.AbandonedBuoyTradeConnection):
    OBJ_FROM = Tau4BattleshipRuins1
    OBJ_TO = Tau4Freeport
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'F'
