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
from universe import faction
from universe.content import mineable
from universe.content import population
from templates.nebula import sig22_nebula
from templates.nebula import exclusion

from templates.solar import hackable
from templates.solar import asteroid
from templates.dockable import pirate
from templates.dockable import station_debris
from templates.dockable import constanta

from text.content import dockable_info
from text.strings import MultiString as MS


class Sig22Member(Member):
    FACTION = faction.LibertyMain
    WEAPON_FACTION = WEAPON_LI
    EQUIP_FACTION = EQUIP_LI


class Sig22Liberty(object):
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_LI
    FACTION = faction.LibertyMain
    WEAPON_FACTION = WEAPON_LI
    EQUIP_FACTION = EQUIP_LI


class Sig22Bretonia(object):
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_BR
    POPULATION_KIND = population.POP_SECOND
    FACTION = faction.BretoniaMain
    WEAPON_FACTION = WEAPON_BR
    EQUIP_FACTION = EQUIP_BR


class Sig22StaticText(Sig22Member, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = sig22
space_color = 2, 2, 2
local_faction = li_grp
space_farclip = 60000

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Dust]
spacedust = Dust

[Music]
space = music_sigma_space
danger = music_sigma_danger
battle = music_sigma_battle

[Ambient]
color = 30, 55, 55

[Background]
nebulae = solar\\stars_mod\\sig22_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_sig22_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
;property_flags = 512 ;lava - MILITARY
property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = sig22_system_light
pos = -31, 0, -48
color = 200, 200, 200
range = 60000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION
'''


class Sig22Sun1(Sig22Member, main_objects.Sun):
    STAR = 'med_white_sun'
    LOADOUT = 'med_blue_sun_fx'


class Sig22BaseBlueNebula(zones.NebulaZone):
    SPACEDUST = Dust.ATTRACT
    SPACEDUST_MAXPARTICLES = 40
    MUSIC = Ambience.NEBULA_DMATTER
    INTERFERENCE = 0.5
    LOAD_FOG = False


class Sig22WestNebula(Sig22Member, Sig22BaseBlueNebula):
    INDEX = 1
    CONTENT_TEMPLATE = sig22_nebula.Sig22BlueNebulaTemplate


class Sig22BottomNebula(Sig22Member, Sig22BaseBlueNebula):
    INDEX = 2
    CONTENT_TEMPLATE = sig22_nebula.Sig22BlueNebulaTemplate


BLUE_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.GENERIC_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '60, 60, 90',
    'fog_far': 5000,
}


class Sig22AsteroidDefinition1(asteroid_definition.Tau37UraniumAsteroidDefinition):
    BELT = True
    BILLBOARDS = True
    DYNAST = True


class Sig22BaseAsteroidZone(zones.AsteroidZone):
    ASTEROID_DEFINITION_CLASS = Sig22AsteroidDefinition1


class Sig22AsteroidZone1(Sig22Member, Sig22BaseAsteroidZone):
    INDEX = 1


class Sig22AsteroidZone2(Sig22Member, Sig22BaseAsteroidZone):
    INDEX = 2


class Sig22AsteroidZone3(Sig22Member, Sig22BaseAsteroidZone):
    INDEX = 3


class Sig22AsteroidZone4(Sig22Member, Sig22BaseAsteroidZone):
    INDEX = 4


class Sig22AsteroidZone5(Sig22Member, Sig22BaseAsteroidZone):
    INDEX = 5


class Sig22AsteroidZone6(Sig22Member, Sig22BaseAsteroidZone):
    INDEX = 6


class Sig22AsteroidZone7(Sig22Member, Sig22BaseAsteroidZone):
    INDEX = 7


class Sig22OldOutpostRuins(Sig22Member, Sig22Liberty, main_objects.StationRuins):
    ALIAS = 'ruins'
    INDEX = 1
    REL = RIGHT
    RU_NAME = MS('Фрипорт 4', 'Freeport 4')
    RU_FIRST_DESCRIPTION = dockable_info.sig22_ruins

    SPACE_OBJECT_TEMPLATE = station_debris.Freeport7DebrisAlternative

    ASTEROID_ZONES = [
        Sig22AsteroidZone1,
    ]


class Sig22OldOutpostRuinsSuprisePoint(Sig22Member, Sig22Liberty, main_objects.HackableStation):
    ALIAS = 'ruins_dock'
    INDEX = 1
    BASE_INDEX = 61
    RELATED_OBJECT = Sig22OldOutpostRuins
    HACKABLE_SOLAR_CLASS = hackable.HackableFreeport7Dock
    INTERIOR_CLASS = interior.EquipDeckInterior
    RU_NAME = MS('Стыковочный узел фрипорта 4', 'Freeport 4 Docking Point')
    MISC_EQUIP_TYPE = LI_CIV
    WEAPON_FACTION = WEAPON_LI
    EQUIP_SET = markets.EquipSet(
        Q.GenericLauncher(CD_MISSILE, eq_classes=markets.MISSILE),
        Q.Shield(LI_CIV, eq_classes=markets.SECRET3),
    )


class Sig22BattleshipRuins1(Sig22Member, Sig22Liberty, main_objects.HackableBattleship):
    ALIAS = 'ast'
    INDEX = 2
    BASE_INDEX = 62
    HACKABLE_SOLAR_CLASS = hackable.HackableLibertyDreadnought
    INTERIOR_CLASS = interior.EquipDeckInterior
    RU_NAME = MS('Линкор Пенсильвания', "Battleship Pennsylvania")

    ASTEROID_ZONES = [
        Sig22AsteroidZone2,
    ]
    MISC_EQUIP_TYPE = LI_PIRATE
    WEAPON_FACTION = WEAPON_LI
    EQUIP_SET = markets.EquipSet(
        Q.Gun('li_lightgun', eq_classes=markets.SECRET3),
        Q.PlayerArmor(None, eq_classes=markets.SECRET3),
    )


class Sig22BattleshipRuins2(Sig22Bretonia, Sig22Member, main_objects.HackableBattleship):
    ALIAS = 'ast'
    INDEX = 3
    BASE_INDEX = 63
    HACKABLE_SOLAR_CLASS = hackable.HackableBretoniaBattleship
    INTERIOR_CLASS = interior.EquipDeckInterior
    RU_NAME = MS('Линкор Левиафан', 'Battleship Leviathan')

    ASTEROID_ZONES = [
        Sig22AsteroidZone2,
    ]
    MISC_EQUIP_TYPE = BR_PIRATE
    WEAPON_FACTION = WEAPON_BR
    EQUIP_SET = markets.EquipSet(
        Q.GenericLauncher(MAIN_MISSILE, eq_classes=markets.MISSILE),
        Q.PlayerArmor(None, eq_classes=markets.SECRET3),
    )


class Sig22BattleshipRuins3(Sig22Bretonia, Sig22Member, main_objects.HackableBattleship):
    ALIAS = 'ast'
    INDEX = 4
    BASE_INDEX = 64
    HACKABLE_SOLAR_CLASS = hackable.HackableBretoniaBattleship
    INTERIOR_CLASS = interior.EquipDeckInterior
    RU_NAME = MS('Линкор Худ', "Battleship Hood")

    ASTEROID_ZONES = [
        Sig22AsteroidZone2,
    ]
    MISC_EQUIP_TYPE = BR_PIRATE
    WEAPON_FACTION = WEAPON_BR
    EQUIP_SET = markets.EquipSet(
        Q.Gun('br_shieldgun', eq_classes=markets.SECRET2),
        Q.PlayerArmor(None, eq_classes=markets.SECRET2),
    )


class Sig22BaseAbandonedAst(main_objects.AbandonedAsteroid):
    ALIAS = 'ast'
    ROTATE_RANDOM = True
    ARCHETYPE = 'tau37_base_medium02'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    AST_EXCLUSION_ZONE_SIZE = 2500
    AST_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.ICE,
        'spacedust_maxparticles': 200,
    }


class Sig22AbandonedAstBase1(Sig22Member, Sig22BaseAbandonedAst):
    INDEX = 5
    BASE_INDEX = 65
    RU_NAME = MS('База Хило', 'Hilo Base')

    ASTEROID_ZONES = [
        Sig22AsteroidZone5,
    ]
    MISC_EQUIP_TYPE = BR_PIRATE
    WEAPON_FACTION = WEAPON_BR
    EQUIP_SET = markets.EquipSet(
        Q.Gun('br_iragun', eq_classes=markets.SECRET2),
        Q.Engine(None, eq_classes=markets.SECRET2),
    )


class Sig22AbandonedAstBase2(Sig22Member, Sig22BaseAbandonedAst):
    INDEX = 6
    BASE_INDEX = 66
    RU_NAME = MS('База Алоха', "Aloha Base")

    ARCHETYPE = 'tau37_base_medium01'

    ASTEROID_ZONES = [
        Sig22AsteroidZone6,
    ]
    MISC_EQUIP_TYPE = LI_PIRATE
    WEAPON_FACTION = WEAPON_LI
    EQUIP_SET = markets.EquipSet(
        Q.Gun('li_roguegun', eq_classes=markets.SECRET2),
        Q.Engine(None, eq_classes=markets.SECRET3),
    )


class Sig22AbandonedAstBase3(Sig22Member, Sig22BaseAbandonedAst):
    INDEX = 7
    BASE_INDEX = 67
    RU_NAME = MS('База Оаху', "O'ahu Base")

    ARCHETYPE = 'tau37_base_medium03'

    ASTEROID_ZONES = [
        Sig22AsteroidZone7,
    ]
    MISC_EQUIP_TYPE = LI_PIRATE
    WEAPON_FACTION = WEAPON_LI
    EQUIP_SET = markets.EquipSet(
        Q.Gun('li_pirategun', eq_classes=markets.SECRET2),
        Q.Engine(None, eq_classes=markets.SECRET2),
    )


class Sig22UnlockAsteroidReward(Sig22Member, mineable.AsteroidRewardsGroupUltra):
    NAME = 'sig22_unlock'
    SOLAR = asteroid.AsteroidTau37
    REWARD_ITEM = roid(URANIUM)
    ULTRA_REWARD_BASES = [
        Sig22AbandonedAstBase1,
        Sig22AbandonedAstBase2,
        Sig22AbandonedAstBase3,
    ]


class Sig22BackgroundAsteroidReward(Sig22Member, mineable.AsteroidRewardsGroupUltra):
    NAME = 'sig22_background'
    SOLAR = asteroid.AsteroidTau37
    REWARD_ITEM = roid(URANIUM)


class Sig22MineableField(mineable.MineableAsteroidField):
    BOX_SIZE = 1400
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.3
    DRIFT_Y = 0
    DRIFT_Z = 0.3


class Sig22UnlockAsteroidRewardField(mineable.AsteroidRewardField):
    ALIAS = 'ast'
    FIELD_CLASS = Sig22MineableField
    REWARDS_GROUP_CLASS = Sig22UnlockAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class Sig22BackgroundAsteroidRewardField(mineable.AsteroidStaticField):
    ALIAS = 'ast'
    FIELD_CLASS = Sig22MineableField
    REWARDS_GROUP_CLASS = Sig22BackgroundAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25
    ULTRA_REWARD = False


class Sig22RewardAsteroids2(Sig22Member, Sig22BackgroundAsteroidRewardField):
    INDEX = 2


class Sig22RewardAsteroids3(Sig22Member, Sig22BackgroundAsteroidRewardField):
    INDEX = 3


class Sig22RewardAsteroids4(Sig22Member, Sig22BackgroundAsteroidRewardField):
    INDEX = 4


class Sig22RewardAsteroids5(Sig22Member, Sig22UnlockAsteroidRewardField):
    INDEX = 5
    ULTRA_BASE = Sig22AbandonedAstBase1


class Sig22RewardAsteroids6(Sig22Member, Sig22UnlockAsteroidRewardField):
    INDEX = 6
    ULTRA_BASE = Sig22AbandonedAstBase2


class Sig22RewardAsteroids7(Sig22Member, Sig22UnlockAsteroidRewardField):
    INDEX = 7
    ULTRA_BASE = Sig22AbandonedAstBase3


class Sig22WarwickJumpgate(Sig22Member, main_objects.Jumpgate):
    INDEX = 1
    REL = LEFT
    TARGET_SYSTEM_NAME = 'br_wrw'


class Sig22CaliforniaJumpgate(Sig22Member, main_objects.Jumpgate):
    INDEX = 2
    REL = RIGHT
    TARGET_SYSTEM_NAME = 'li_cal'


class Sig22ColumbiaJumpgate(Sig22Member, main_objects.Jumpgate):
    INDEX = 3
    REL = TOP
    TARGET_SYSTEM_NAME = 'li_col'


class Sig22Dockring(Sig22Bretonia, Sig22Member, main_objects.WaterPlanetDockring):
    BASE_INDEX = 1
    REL = BOTTOM
    INTERIOR_CLASS = interior.CustomFullSingleRoomInterior
    DEALERS = dealers.BretoniaCivilianDealers
    SHIP_SET = markets.ShipSet('bh_elite')
    RU_NAME = MS('Планета Гонолулу', 'Planet Honolulu')


class Sig22Station(Sig22Member, Sig22Liberty, main_objects.TradingBase):
    ALIAS = 'station'
    BASE_INDEX = 2
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = constanta.ConstantaAlternative
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.LibertyCivilianDealers
    RU_NAME = MS('Станция Констанца', 'Constanța Station')

    BASE_PROPS = meta.TradingBase(
        objectives=[
            meta.HaveGreenhouse(),
        ]
    )


class Sig22Battleship(Sig22Member, main_objects.LibertyBattleship):
    BASE_INDEX = 3
    REL = RIGHT
    REL_APPEND = 2500
    INTERIOR_CLASS = interior.BattleshipInterior
    DEALERS = dealers.LibertyMilitaryDealers
    SHIP_SET = markets.ShipSet('li_fighter')
    RU_NAME = MS('Линкор Аризона', 'Battlship Arizona')


class Sig22Planet1(Sig22Member, main_objects.Planet):
    ARCHETYPE = 'planet_watblucld_3000'
    SPHERE_RADIUS = 3000
    RELATED_DOCK_RING = Sig22Dockring


class Sig22Planet2(Sig22Member, main_objects.Planet):
    INDEX = 2
    ARCHETYPE = 'planet_desorcld_3000'
    SPHERE_RADIUS = 3000
    RU_NAME = MS('Планета Сопдет', 'Planet Sopdet')


class Sig22SouthPirates(Sig22Member, Sig22Liberty, main_objects.PirateStation):
    INDEX = 1
    BASE_INDEX = 4
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = pirate.PirateBaseBizmark
    FACTION = faction.LaneHackers

    RU_NAME = MS('База Алькатрас', "Alcatraz Base")

    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.LibertyPirateDealers

    NEBULA_ZONES = [
        Sig22BottomNebula
    ]
    EXCLUSION_PARAMS = BLUE_EXCLUSION_PARAMS
    NEBULA_EXCLUSION_ZONE_SIZE = 2000


class Sig22NorthPirates(Sig22Bretonia, Sig22Member, main_objects.PirateStation):
    INDEX = 2
    BASE_INDEX = 5
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = pirate.PirateBaseStuttgart
    FACTION = faction.Ireland
    RU_NAME = MS('База Лим+ерик', "Limerick Base")

    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.BretoniaPirateDealers

    NEBULA_ZONES = [
        Sig22WestNebula
    ]
    EXCLUSION_PARAMS = BLUE_EXCLUSION_PARAMS
    NEBULA_EXCLUSION_ZONE_SIZE = 2000


class Sig22BattleshipConn1(Sig22Member, Sig22Liberty, main_objects.TradeConnection):
    OBJ_FROM = Sig22ColumbiaJumpgate
    OBJ_TO = Sig22Battleship
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        Sig22NorthPirates
    ]


class Sig22BattleshipConn2(Sig22Member, Sig22Liberty, main_objects.TradeConnection):
    OBJ_FROM = Sig22Battleship
    OBJ_TO = Sig22Station
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        Sig22SouthPirates
    ]


class Sig22PlanetConn1(Sig22Bretonia, Sig22Member, main_objects.TradeConnection):
    OBJ_FROM = Sig22WarwickJumpgate
    OBJ_TO = Sig22Dockring
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        Sig22NorthPirates
    ]


class Sig22PlanetConn2(Sig22Member, Sig22Liberty, main_objects.TradeConnection):
    OBJ_FROM = Sig22Dockring
    OBJ_TO = Sig22Station
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        Sig22SouthPirates
    ]


class Sig22StationConn2(Sig22Member, Sig22Liberty, main_objects.TradeConnection):
    OBJ_FROM = Sig22Station
    OBJ_TO = Sig22CaliforniaJumpgate
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        Sig22SouthPirates
    ]


class Sig22RuinsConn1(Sig22Member, main_objects.BrokenTradeConnection):
    OBJ_FROM = Sig22OldOutpostRuins
    OBJ_TO = Sig22WarwickJumpgate
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'F'


class Sig22RuinsConn2(Sig22Member, main_objects.BrokenTradeConnection):
    OBJ_FROM = Sig22OldOutpostRuins
    OBJ_TO = Sig22ColumbiaJumpgate
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'G'

