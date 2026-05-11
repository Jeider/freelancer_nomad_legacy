from fx.space import Dust, JumpholeEffect
from fx.sound import Ambience
from universe.audio.space_voice import SpaceVoice, SpaceCostume

from managers.tools import query as Q
from world.names import *
from universe.content import meta

from universe import markets

from universe.content.member import Member
from universe.content.system_object import LEFT, RIGHT, TOP
from universe.content import main_objects
from universe.content import zones
from universe.content import interior
from universe.content import dealers
from universe.content import asteroid_definition
from universe import faction
from universe.content import mineable
from templates.solar import asteroid
from templates.nebula import co_och_nebula
from templates.nebula import exclusion
from templates.dockable import terraforming
from templates.solar import suprise


from text.strings import MultiString as MS


class CurMember(Member):
    FACTION = faction.Corsairs
    INTERIOR_BG1 = interior.INTERIOR_CO_CURACAO
    INTERIOR_BG2 = interior.INTERIOR_STARS
    WEAPON_FACTION = WEAPON_BW
    EQUIP_FACTION = EQUIP_BW
    AST_TYPE = 'co_cur'


class CurStaticText(CurMember, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = co_cur
space_color = 10, 15, 35
local_faction = co_grp
space_farclip = 70000

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Dust]
spacedust = Dust

[Music]
space = music_iw_space
danger = music_iw_danger
battle = music_iw_battle

[Ambient]
color = 10, 15, 35

[Background]
nebulae = solar\\stars_mod\\co_cur_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[LightSource]
nickname = co_cur_system_light
pos = -31, 0, -48
color = 110, 255, 255
range = 80000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION

[zone]
nickname = zone_co_cur_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
property_flags = 512 ;lava - MILITARY
;property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING
'''


class CurSun(CurMember, main_objects.Sun):
    STAR = 'sm_white_sun'
    LOADOUT = 'med_blue_sun_fx'


class CurTerrPlanet(CurMember, main_objects.Planet):
    INDEX = 1
    ARCHETYPE = 'planet_desormed_4000'
    SPHERE_RADIUS = 4000
    RU_NAME = MS('Планета Кюросао', 'Planet Curacao')


class CurTerraformer(CurMember, main_objects.Station):
    ALIAS = 'station'
    INDEX = 1
    BASE_INDEX = 2
    REL = LEFT
    SPACE_OBJECT_TEMPLATE = terraforming.TerraformingRotate
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.BretoniaPirateDealers
    CALC_STORE = False
    HAVE_CHARACTERS = False

    AST_EXCLUSION_ZONE_SIZE = 4000
    ASTEROID_ZONES = [
        # CurAsteroidZone4,
    ]

    RU_NAME = MS('Станция Антилия', 'Station Antillia')


class CurTrack(CurMember, main_objects.BackgroundComplexObject):
    ALIAS = 'track'
    INDEX = 1
    ROTATE = 180

    WORKSPACE_TEMPLATE_NAME = 'br05_track'
    # ARCHETYPE_CHANGE_FROM = 'om15'  # it's initially om15 asteroid kind





class CurLargeAsteroidDefinition(asteroid_definition.CuracaoAsteroidDefinition):
    BELT = True
    BILLBOARDS = True
    DYNAST = True
    LOOT = False  # TEMP
    BELT_HEIGHT = 8000


class CurSmallAsteroidDefinition(asteroid_definition.CuracaoAsteroidDefinition):
    BELT = True
    BILLBOARDS = True
    DYNAST = True
    LOOT = False  # TEMP


class CurAsteroidZone1(CurMember, zones.AsteroidZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = CurLargeAsteroidDefinition
    MUSIC = Ambience.AST_ROCK

    SPACEDUST = Dust.ASTEROID
    SPACEDUST_MAXPARTICLES = 200


class CurAsteroidZone2(CurMember, zones.AsteroidZone):
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = CurLargeAsteroidDefinition
    MUSIC = Ambience.AST_ROCK

    SPACEDUST = Dust.ASTEROID
    SPACEDUST_MAXPARTICLES = 200


class CurAsteroidZone3(CurMember, zones.AsteroidZone):
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = CurSmallAsteroidDefinition
    MUSIC = Ambience.AST_ROCK

    SPACEDUST = Dust.ASTEROID
    SPACEDUST_MAXPARTICLES = 200


class CurAsteroidZone4(CurMember, zones.AsteroidZone):
    INDEX = 4
    ASTEROID_DEFINITION_CLASS = CurSmallAsteroidDefinition
    MUSIC = Ambience.AST_ROCK

    SPACEDUST = Dust.ASTEROID
    SPACEDUST_MAXPARTICLES = 200


class CurAsteroidZone5(CurMember, zones.AsteroidZone):
    INDEX = 5
    ASTEROID_DEFINITION_CLASS = CurSmallAsteroidDefinition
    MUSIC = Ambience.AST_ROCK

    SPACEDUST = Dust.ASTEROID
    SPACEDUST_MAXPARTICLES = 200


class CurAsteroidZone6(CurMember, zones.AsteroidZone):
    INDEX = 6
    ASTEROID_DEFINITION_CLASS = CurSmallAsteroidDefinition
    MUSIC = Ambience.AST_ROCK

    SPACEDUST = Dust.ASTEROID
    SPACEDUST_MAXPARTICLES = 200


class BaseCurAst1Static(main_objects.AutoStaticObject):
    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        CurAsteroidZone1,
    ]


class BaseCurAst2Static(main_objects.AutoStaticObject):
    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        CurAsteroidZone2,
    ]


class CurStaticAst1(CurMember, BaseCurAst1Static):
    INDEX = 1


class CurStaticAst2(CurMember, BaseCurAst1Static):
    INDEX = 2


class CurStaticAst3(CurMember, BaseCurAst1Static):
    INDEX = 3


class OchSuprise1(main_objects.SupriseSattelite):
    ALIAS = 'suprise1'
    ARCHETYPE = 'suprise_pi_freighter'
    OFFSET = [-350, -150, 200]
    ROTATE_RANDOM = True
    ORIENT_TOGETHER = True


class OchSuprise2(main_objects.SupriseSattelite):
    ALIAS = 'suprise2'
    ARCHETYPE = 'suprise_bw_elite2'
    OFFSET = [-150, -250, 100]
    ROTATE_RANDOM = True
    ORIENT_TOGETHER = True


class CurStaticAst4(CurMember, BaseCurAst2Static):
    INDEX = 4
    SATTELITES = [OchSuprise1, OchSuprise2]


class CurStaticAst5(CurMember, BaseCurAst2Static):
    INDEX = 5


class CurStaticAst6(CurMember, BaseCurAst2Static):
    INDEX = 6


class OchSuprise3(main_objects.SupriseSattelite):
    ALIAS = 'suprise3'
    ARCHETYPE = 'suprise_bw_freighter'
    OFFSET = [115, -55, 210]
    ROTATE_RANDOM = True
    ORIENT_TOGETHER = True


class OchSuprise4(main_objects.SupriseSattelite):
    ALIAS = 'suprise4'
    ARCHETYPE = 'suprise_pi_elite'
    OFFSET = [-250, 310, 100]
    ROTATE_RANDOM = True
    ORIENT_TOGETHER = True


class OchSuprise5(main_objects.SupriseSattelite):
    ALIAS = 'suprise5'
    ARCHETYPE = 'suprise_bw_fighter'
    OFFSET = [-450, 150, -200]
    ROTATE_RANDOM = True
    ORIENT_TOGETHER = True


class CurStaticAst7(CurMember, BaseCurAst1Static):
    INDEX = 7
    SATTELITES = [OchSuprise3, OchSuprise4, OchSuprise5]

    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        CurAsteroidZone2,
    ]


class CurLargeAsteroidBase(CurMember, main_objects.PirateAsteroid):
    ALIAS = 'astbase'
    INDEX = 1
    BASE_INDEX = 1
    ARCHETYPE = 'co_cur_base_large01'
    LOADOUT = 'co_base_rock_large01_pi_01'
    INTERIOR_CLASS = interior.CustomFullSplitRoomInterior
    DEFENCE_LEVEL = None
    RU_NAME = MS('База Лион', "Lion Base")
    SHIP_SET = markets.ShipSet('co_fighter')
    CALC_STORE = False
    HAVE_CHARACTERS = False
    DEALERS = dealers.BretoniaPirateDealers

    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        CurAsteroidZone1,
    ]
    EQUIP_SET = markets.EquipSet(
        Q.Gun('bw_corsairgun', eq_classes=markets.SECRET3),
    )


class CurMetro1(CurMember, main_objects.MetroMiningOne):
    INDEX = 1

    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        CurAsteroidZone2,
    ]


class CurMetro2(CurMember, main_objects.MetroMiningTwo):
    INDEX = 2

    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        CurAsteroidZone2,
    ]


class CurMetro3(CurMember, main_objects.MetroMiningOne):
    INDEX = 3

    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        CurAsteroidZone2,
    ]


class CurMetro4(CurMember, main_objects.MetroMiningTwo):
    INDEX = 4

    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        CurAsteroidZone2,
    ]


class CurBaseSolarPlant(main_objects.SolarPlant):
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


class CurBaseMinesZone(zones.AsteroidZone):
    ASTEROID_DEFINITION_CLASS = asteroid_definition.SpaceMines
    SPACEDUST = Dust.DEBRIS
    SPACEDUST_MAXPARTICLES = 100
    MUSIC = Ambience.MINE_AST
    INTERFERENCE = 0.1
    DRAG_MODIFIER = 1.5
    PROPERTY_FLAGS = 4128


class CurSolarMinesZone1(CurMember, CurBaseMinesZone):
    ALIAS = 'solar'
    INDEX = 1


class CurSolarMinesZone2(CurMember, CurBaseMinesZone):
    ALIAS = 'solar'
    INDEX = 2


class CurSolarPlant1(CurMember, CurBaseSolarPlant):
    INDEX = 1
    BASE_INDEX = 61
    ASTEROID_ZONES = [
        CurSolarMinesZone1,
    ]
    RU_NAME = MS('Солн.генератор Барбадос', 'Solar Plant Barbados')
    MISC_EQUIP_TYPE = BR_PIRATE
    EQUIP_SET = markets.EquipSet(
        Q.Power(BR_CIV, eq_classes=markets.SECRET3),
        Q.Shield(BR_PIRATE, eq_classes=markets.SECRET2),
    )


class CurSolarPlant2(CurMember, CurBaseSolarPlant):
    INDEX = 2
    BASE_INDEX = 62
    ASTEROID_ZONES = [
        CurSolarMinesZone2,
    ]
    RU_NAME = MS('Солн.генератор Аруба', "Solar Plant Aruba")
    MISC_EQUIP_TYPE = BR_PIRATE
    EQUIP_SET = markets.EquipSet(
        Q.Power(BR_CIV, eq_classes=markets.SECRET2),
        Q.Shield(BR_PIRATE, eq_classes=markets.SECRET3),
    )


class CurSolarSupriseRewards(CurMember, mineable.DefaultSupriseRewardsGroup):
    NAME = 'co_cur_solar_suprise'
    SOLAR = suprise.BretoniaMiscFighterEdge
    REWARD_ITEM = None
    ULTRA_REWARD_BASES = [
        CurSolarPlant1,
        CurSolarPlant2,
    ]


class CurSolarSupriseField(mineable.DefaultField):
    BOX_SIZE = 400
    DENSITY_MULTIPLER = 4
    DRIFT_X = 0.5
    DRIFT_Y = 0.5
    DRIFT_Z = 0.5
    EMPTY_CHANCE = 0.2


class CurBaseSolarSupriseRewardField(mineable.SupriseRewardField):
    ALIAS = 'solar'
    FIELD_CLASS = CurSolarSupriseField
    REWARDS_GROUP_CLASS = CurSolarSupriseRewards
    ULTRA_REWARD = True


class CurSolarSupriseRewardField1(CurMember, CurBaseSolarSupriseRewardField):
    INDEX = 1
    ULTRA_BASE = CurSolarPlant1


class CurSolarSupriseRewardField2(CurMember, CurBaseSolarSupriseRewardField):
    INDEX = 2
    ULTRA_BASE = CurSolarPlant2


class CurPirates(CurMember, main_objects.PirateStation):
    INDEX = 1
    BASE_INDEX = 3
    REL = RIGHT
    ARCHETYPE = 'co_cur_base_medium03'
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.BretoniaMilitaryDealers
    FACTION = faction.BretoniaHunters
    AST_EXCLUSION_ZONE_SIZE = 2500
    ASTEROID_ZONES = [
        CurAsteroidZone4
    ]
    RU_NAME = MS('База Тортола', 'Tortola Base')

    CALC_STORE = False
    HAVE_CHARACTERS = False





class CurAbandonedAstBase1(CurMember, main_objects.AbandonedAsteroid):
    ALIAS = 'ast'
    INDEX = 6
    BASE_INDEX = 51
    ROTATE_RANDOM = True
    ARCHETYPE = 'co_cur_base_medium01'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    RU_NAME = MS('База Верджин-Горда', "Virgin Gorda Base")

    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        CurAsteroidZone6,
    ]
    AST_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.ASTEROID,
        'spacedust_maxparticles': 200,
    }
    MISC_EQUIP_TYPE = RH_PIRATE
    WEAPON_FACTION = WEAPON_RH
    EQUIP_SET = markets.EquipSet(
        Q.Gun('rh_junkergun', eq_classes=markets.SECRET2),
        Q.Engine(None, eq_classes=markets.SECRET2),
    )


class CurPirateAsteroidReward(CurMember, mineable.AsteroidRewardsGroupUltra):
    NAME = 'rh_biz_rock'
    SOLAR = asteroid.AsteroidCuracao
    REWARD_ITEM = roid(BERILIUM)
    ULTRA_REWARD_BASES = [
        CurAbandonedAstBase1,
    ]


class CurPirateAsteroids(CurMember, mineable.AsteroidStaticField):
    INDEX = 4
    FIELD_CLASS = mineable.BackgroundAsteroidsField
    REWARDS_GROUP_CLASS = CurPirateAsteroidReward


class CurAbandonedAsteroids1(CurMember, mineable.AsteroidRewardField):
    INDEX = 6
    FIELD_CLASS = mineable.MineableAsteroidField
    REWARDS_GROUP_CLASS = CurPirateAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True
    ULTRA_BASE = CurAbandonedAstBase1
