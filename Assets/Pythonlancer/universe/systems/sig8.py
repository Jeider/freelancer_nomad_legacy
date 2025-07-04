from fx.space import Dust, JumpholeEffect
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
from templates.nebula import sig8_nebula
from templates.nebula import exclusion

from templates.solar import hackable
from templates.solar import asteroid
from templates.dockable import pirate
from templates.dockable import station_debris
from templates.dockable import junker
from templates.dockable import police
from templates.dockable import trade_storages


class Sigma8Member(Member):
    FACTION = faction.RheinlandMain
    INTERIOR_BG1 = interior.INTERIOR_SIGMA8
    WEAPON_FACTION = WEAPON_RH
    EQUIP_FACTION = EQUIP_RH


class Sigma8StaticText(Sigma8Member, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = sig8
space_color = 2, 10, 5
local_faction = rh_grp
space_farclip = 60000

[archetype]
ship = rh_fighter
ship = rh_elite
ship = rh_freighter
ship = rh_cruiser
ship = rh_gunboat
ship = rh_battleship
ship = bw_fighter
ship = bw_elite
ship = bw_elite2
ship = pi_fighter
ship = pi_elite
ship = ge_transport
ship = ge_armored

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Music]
space = music_sigma_space
danger = music_sigma_danger
battle = music_sigma_battle

[Ambient]
color = 2, 10, 5

[Dust]
spacedust = Dust

[Background]
nebulae = solar\\stars_mod\\sig8_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_sig8_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
;property_flags = 512 ;lava - MILITARY
property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = sig8_System_Light
pos = 0, 0, 0
color = 194, 213, 254
range = 200000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION

[LightSource]
nickname = sig8_green_Light
pos = 100000, 0, 0
color = 24, 34, 25
range = 100000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION
'''


BROWN_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.EDGE_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '100, 80, 10',
    'fog_far': 5000,
}


EDGE_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.EDGE_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '200, 255, 200',
    'fog_far': 5000,
}


class Sig8GreenNebula1(Sigma8Member, zones.NebulaZone):
    INDEX = 1
    SPACEDUST = Dust.ATTRACT_GREEN
    SPACEDUST_MAXPARTICLES = 40
    MUSIC = Ambience.NEBULA_EDGE
    CONTENT_TEMPLATE = sig8_nebula.Sig8LargeEdgeNebulaTemplate

    PROPERTY_FLAGS = 32768
    PROPERTY_FOG_COLOR = '0, 255, 0'


class Sig8GreenNebula2(Sigma8Member, zones.NebulaZone):
    INDEX = 2
    SPACEDUST = Dust.ATTRACT_GREEN
    SPACEDUST_MAXPARTICLES = 40
    MUSIC = Ambience.NEBULA_EDGE
    CONTENT_TEMPLATE = sig8_nebula.Sig8LargeEdgeNebulaTemplate

    PROPERTY_FLAGS = 32768
    PROPERTY_FOG_COLOR = '0, 255, 0'

#
# class Sig8BrownNebula1(Sigma8Member, zones.NebulaZone):
#     INDEX = 3
#     SPACEDUST = Dust.ATTRACT
#     SPACEDUST_MAXPARTICLES = 40
#     MUSIC = Ambience.NEBULA_DMATTER
#     CONTENT_TEMPLATE = sig8_nebula.Sig8BrownNebulaTemplate
#
#     PROPERTY_FLAGS = 32768
#     PROPERTY_FOG_COLOR = '100, 80, 10'


class Sig8BrownNebula2(Sigma8Member, zones.NebulaZone):
    INDEX = 4
    SPACEDUST = Dust.ATTRACT
    SPACEDUST_MAXPARTICLES = 40
    MUSIC = Ambience.NEBULA_DMATTER
    CONTENT_TEMPLATE = sig8_nebula.Sig8BrownNebulaTemplate

    PROPERTY_FLAGS = 32768
    PROPERTY_FOG_COLOR = '100, 80, 10'


class Sig8AsteroidDefinition(asteroid_definition.Omega15NiobiumAsteroidDefinition):
    DYNAST = True
    BELT = True
    BILLBOARDS = True
    LOOT = False  # TEMP


class Sig8BaseVanillaAstZone(zones.AsteroidZone):
    SPACEDUST = Dust.ASTEROID
    SPACEDUST_MAXPARTICLES = 100
    MUSIC = Ambience.AST_ROCK
    ASTEROID_DEFINITION_CLASS = Sig8AsteroidDefinition


class Sig8AsteroidZone1(Sigma8Member, Sig8BaseVanillaAstZone):
    INDEX = 1


class Sig8AsteroidZone2(Sigma8Member, Sig8BaseVanillaAstZone):
    INDEX = 2


class Sig8AsteroidZone3(Sigma8Member, Sig8BaseVanillaAstZone):
    INDEX = 3


class Sig8AsteroidZone4(Sigma8Member, Sig8BaseVanillaAstZone):
    INDEX = 4


class Sig8AsteroidZone5(Sigma8Member, Sig8BaseVanillaAstZone):
    INDEX = 5


class Sigma8EastAsteroidReward(Sigma8Member, mineable.AsteroidRewardsGroupMedium):
    NAME = 'sig8_east_ast'
    SOLAR = asteroid.AsteroidOmega15
    REWARD_ITEM = 'comm_roid_niobium'


class Sigma8LargeAsteroids1(Sigma8Member, mineable.AsteroidRewardField):
    INDEX = 1
    FIELD_CLASS = mineable.BackgroundAsteroidsField
    REWARDS_GROUP_CLASS = Sigma8EastAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25


class Sigma8LargeAsteroids2(Sigma8Member, mineable.AsteroidRewardField):
    INDEX = 2
    FIELD_CLASS = mineable.BackgroundAsteroidsField
    REWARDS_GROUP_CLASS = Sigma8EastAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25


class Sigma8LargeAsteroids3(Sigma8Member, mineable.AsteroidRewardField):
    INDEX = 3
    FIELD_CLASS = mineable.BackgroundAsteroidsField
    REWARDS_GROUP_CLASS = Sigma8EastAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25


class Sigma8LargeAsteroids4(Sigma8Member, mineable.AsteroidRewardField):
    INDEX = 4
    FIELD_CLASS = mineable.BackgroundAsteroidsField
    REWARDS_GROUP_CLASS = Sigma8EastAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25


class Sig8Sun(Sigma8Member, main_objects.Sun):
    STAR = 'med_blue_sun'
    LOADOUT = 'med_blue_sun_fx'


class Sig8BerlinJumpgate(Sigma8Member, main_objects.Jumpgate):
    INDEX = 1
    REL = TOP
    TARGET_SYSTEM_NAME = 'rh_ber'


class Sig8BizmarkJumpgate(Sigma8Member, main_objects.Jumpgate):
    INDEX = 2
    REL = BOTTOM
    TARGET_SYSTEM_NAME = 'rh_biz'


class Sig8Station(Sigma8Member, main_objects.TradelaneSupportStation):
    INDEX = 1
    BASE_INDEX = 1
    REL = LEFT

    ARCHETYPE = 'largestation1_old'
    LOADOUT = 'largestation_rh'

    AUDIO_PREFIX = SpaceVoice.STATION
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.RheinlandCivilianDealers

    RU_NAME = 'Станция Штарке'


class Sig8Freeport(Sigma8Member, main_objects.Freeport):
    INDEX = 1
    BASE_INDEX = 2
    REL = LEFT

    SPACE_OBJECT_TEMPLATE = trade_storages.HonshuStorage

    AUDIO_PREFIX = SpaceVoice.FREEPORT
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.RheinlandCivilianDealers

    RU_NAME = 'Фрипорт Гослар'


class Sig8BorderStation(Sigma8Member, main_objects.Outpost):
    INDEX = 1
    BASE_INDEX = 3
    REL = RIGHT

    SPACE_OBJECT_TEMPLATE = police.SigmaEightPoliceOutpost

    AUDIO_PREFIX = SpaceVoice.BORDER_STATION
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.RheinlandMilitaryDealers

    RU_NAME = 'Аванпост Аугсбург'


class Sig8Junkers(Sigma8Member, main_objects.JunkerBase):
    INDEX = 1
    BASE_INDEX = 4
    REL = RIGHT

    SPACE_OBJECT_TEMPLATE = junker.SigmaEightJunker

    FACTION = faction.Junkers
    DEFENCE_LEVEL = None
    RU_NAME = 'Склад Зуль'

    AUDIO_PREFIX = SpaceVoice.STATION
    INTERIOR_CLASS = interior.PirateStationInterior
    DEALERS = dealers.RheinlandCivilianDealers

    NEBULA_EXCLUSION_ZONE_SIZE = 2500
    EXCLUSION_PARAMS = EDGE_EXCLUSION_PARAMS
    NEBULA_ZONES = [Sig8GreenNebula2]


class Sig8Pirate(Sigma8Member, main_objects.PirateStation):
    INDEX = 1
    BASE_INDEX = 5
    REL = RIGHT

    SPACE_OBJECT_TEMPLATE = pirate.ManhattanPirateBase

    FACTION = faction.WorkaroundPirate
    DEFENCE_LEVEL = None
    RU_NAME = 'База Вернигороде'

    AUDIO_PREFIX = SpaceVoice.STATION
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.RheinlandPirateDealers

    NEBULA_EXCLUSION_ZONE_SIZE = 3500
    EXCLUSION_PARAMS = EDGE_EXCLUSION_PARAMS
    NEBULA_ZONES = [Sig8GreenNebula1]


class Sig8BizmarkJumphole(Sigma8Member, main_objects.Jumphole):
    REL = LEFT
    INDEX = 2

    TARGET_SYSTEM_NAME = 'rh_biz'

    LOADOUT = JumpholeEffect.LIGHT

    NEBULA_EXCLUSION_ZONE_SIZE = 2500
    EXCLUSION_PARAMS = BROWN_EXCLUSION_PARAMS
    # NEBULA_ZONES = [Sig8BrownNebula1]
    ASTEROID_ZONES = [Sig8AsteroidZone5]


class Sig8KoenigsbergJumphole(Sigma8Member, main_objects.Jumphole):
    INDEX = 1
    REL = TOP

    TARGET_SYSTEM_NAME = 'rh_kgb'

    LOADOUT = JumpholeEffect.GREEN

    NEBULA_EXCLUSION_ZONE_SIZE = 2500
    EXCLUSION_PARAMS = BROWN_EXCLUSION_PARAMS
    NEBULA_ZONES = [Sig8BrownNebula2]


class Sig8TemporaryOmicronJumppoint(Sigma8Member, main_objects.VirtualDepot):
    INDEX = 3
    REL = TOP

    NEBULA_EXCLUSION_ZONE_SIZE = 2500
    EXCLUSION_PARAMS = EDGE_EXCLUSION_PARAMS
    NEBULA_ZONES = [Sig8GreenNebula2]

    RU_NAME = 'Временная гипердыра в Малый Омикрон'


class Sig8ForbesJumphole(Sigma8Member, main_objects.Jumphole):
    INDEX = 4
    REL = RIGHT

    TARGET_SYSTEM_NAME = 'li_for'

    LOADOUT = JumpholeEffect.GREEN

    NEBULA_EXCLUSION_ZONE_SIZE = 2500
    EXCLUSION_PARAMS = EDGE_EXCLUSION_PARAMS
    NEBULA_ZONES = [Sig8GreenNebula2]


class Sigma8Planet1(Sigma8Member, main_objects.Planet):
    INDEX = 1
    ARCHETYPE = 'planet_gaspurcld_5000'
    SPHERE_RADIUS = 5000
    RING = True
    RING_ZONE_ALIAS = 'ring'
    RING_ZONE_INDEX = 1
    RING_FILE_NAME = 'sig8'
    RU_NAME = 'Планета Трир'


class Sigma8Planet2(Sigma8Member, main_objects.Planet):
    INDEX = 2
    ARCHETYPE = 'planet_icemntcld_2500'
    SPHERE_RADIUS = 2500
    RU_NAME = 'Планета Прюм'


class Sigma8Planet3(Sigma8Member, main_objects.Planet):
    INDEX = 3
    ARCHETYPE = 'planet_crater_1500'
    SPHERE_RADIUS = 1500
    RU_NAME = 'Планета Крёф'


class Sig8OldFreeportRuins(Sigma8Member, main_objects.StationRuins):
    ALIAS = 'ruins'
    INDEX = 1
    REL = RIGHT

    RU_NAME = 'База Монако'

    SPACE_OBJECT_TEMPLATE = station_debris.SigmaEightFreeport

    ASTEROID_ZONES = [
        Sig8AsteroidZone1,
    ]


class Sig8OldFreeportRuinsSuprisePoint(Sigma8Member, main_objects.HackableStation):
    ALIAS = 'ruins_dock'
    INDEX = 1
    BASE_INDEX = 51
    RELATED_OBJECT = Sig8OldFreeportRuins
    HACKABLE_SOLAR_CLASS = hackable.HackableOutpost
    INTERIOR_CLASS = interior.EquipDeckInterior

    RU_NAME = 'Стыковочный узел Монако'
    MISC_EQUIP_TYPE = RH_CIV
    WEAPON_FACTION = WEAPON_RH
    EQUIP_SET = markets.EquipSet(
        Q.GenericLauncher(MAIN_SUPER_MISSILE, eq_classes=markets.MISSILE),
        Q.Shield(RH_PIRATE, eq_classes=markets.SECRET2),
    )


class Sig8BattleshipRuins1(Sigma8Member, main_objects.HackableBattleship):
    ALIAS = 'ast'
    INDEX = 2
    BASE_INDEX = 61
    HACKABLE_SOLAR_CLASS = hackable.HackableRheinlandBattleship
    INTERIOR_CLASS = interior.EquipDeckInterior
    RU_NAME = 'Линкор Принц Ойген'

    ASTEROID_ZONES = [
        Sig8AsteroidZone2,
    ]

    MISC_EQUIP_TYPE = RH_PIRATE
    WEAPON_FACTION = WEAPON_RH
    EQUIP_SET = markets.EquipSet(
        Q.GenericLauncher(MAIN_MISSILE, eq_classes=markets.MISSILE),
        Q.PlayerArmor(None, eq_classes=markets.SECRET2),
    )


class Sig8BattleshipRuins2(Sigma8Member, main_objects.HackableBattleship):
    ALIAS = 'ast'
    INDEX = 3
    BASE_INDEX = 62
    HACKABLE_SOLAR_CLASS = hackable.HackableRheinlandBattleship
    INTERIOR_CLASS = interior.EquipDeckInterior
    RU_NAME = 'Линкор Адмирал Хиппер'

    ASTEROID_ZONES = [
        Sig8AsteroidZone3,
    ]

    MISC_EQUIP_TYPE = RH_PIRATE
    WEAPON_FACTION = WEAPON_RH
    EQUIP_SET = markets.EquipSet(
        Q.Gun('rh_lightgun', eq_classes=markets.SECRET3),
        Q.PlayerArmor(None, eq_classes=markets.SECRET3),
    )


class Sig8BattleshipRuins3(Sigma8Member, main_objects.HackableBattleship):
    ALIAS = 'ast'
    INDEX = 4
    BASE_INDEX = 63
    HACKABLE_SOLAR_CLASS = hackable.HackableRheinlandBattleship
    INTERIOR_CLASS = interior.EquipDeckInterior
    RU_NAME = 'Линкор Лютцов'

    ASTEROID_ZONES = [
        Sig8AsteroidZone4,
    ]

    MISC_EQUIP_TYPE = RH_PIRATE
    WEAPON_FACTION = WEAPON_RH
    EQUIP_SET = markets.EquipSet(
        Q.GenericLauncher(TORPEDO_MISSILE, eq_classes=markets.MISSILE),
        Q.PlayerArmor(None, eq_classes=markets.SECRET2),
    )


class Sig8StarkeConn1(Sigma8Member, main_objects.TradeConnection):
    OBJ_FROM = Sig8Station
    OBJ_TO = Sig8BerlinJumpgate
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        Sig8Pirate,
    ]


class Sig8StarkeConn2(Sigma8Member, main_objects.TradeConnection):
    OBJ_FROM = Sig8Station
    OBJ_TO = Sig8Freeport
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        Sig8Pirate,
    ]


class Sig8PoliceConn1(Sigma8Member, main_objects.TradeConnection):
    OBJ_FROM = Sig8BorderStation
    OBJ_TO = Sig8Freeport
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        Sig8Junkers,
    ]


class Sig8PoliceConn2(Sigma8Member, main_objects.TradeConnection):
    OBJ_FROM = Sig8BorderStation
    OBJ_TO = Sig8BizmarkJumpgate
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        Sig8Junkers,
    ]


class Sig8BrokenConn1(Sigma8Member, main_objects.BrokenTradeConnection):
    OBJ_FROM = Sig8OldFreeportRuins
    OBJ_TO = Sig8BorderStation
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'X'
    ATTACKED_BY = [
        Sig8Junkers,
    ]