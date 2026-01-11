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
from templates.nebula import sig17_nebula
from templates.nebula import exclusion

from templates.dockable import astbase
from templates.dockable import cambridge_research
from templates.dockable import police
from templates.dockable import pirate
from templates.dockable import station_debris

from text.content import dockable_info

from text.strings import MultiString as MS


class Sig17Member(Member):
    FACTION = faction.LibertyMain
    INTERIOR_BG1 = interior.INTERIOR_SIGMA17
    WEAPON_FACTION = WEAPON_LI
    EQUIP_FACTION = EQUIP_LI


class Sig17StaticText(Sig17Member, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = sig17
space_color = 0, 0, 0
local_faction = li_grp
space_farclip = 50000

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Dust]
spacedust = Dust

[Music]
space = music_sigma_space
danger = music_sigma_danger
battle = music_sigma_battle

[Ambient]
color = 0, 0, 0

[Background]
nebulae = solar\\stars_mod\\sig17_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_sig17_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
;property_flags = 512 ;lava - MILITARY
property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = sig17_system_light
pos = -31, 0, -48
color = 220, 251, 255
range = 80000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION
color_curve = sigma17_color, 50.0
'''


class Sig17Sun1(Sig17Member, main_objects.Sun):
    STAR = 'edge_sun'
    LOADOUT = 'med_green_sun_fx'

    ATMOSHPERE_RANGE = 6000
    DRAG_ZONE_SIZE = 5800
    DEATH_ZONE_SIZE = 4000


class Sig17Sun2(Sig17Member, main_objects.Sun):
    INDEX = 2
    STAR = 'Bw06_sun2'
    LOADOUT = 'small_green_sun_fx'

    ATMOSHPERE_RANGE = 6000
    DRAG_ZONE_SIZE = 5800
    DEATH_ZONE_SIZE = 4000


class Sig17Sun3(Sig17Member, main_objects.Sun):
    INDEX = 3
    STAR = 'Bw06_sun3'
    LOADOUT = 'small_blue_sun_fx'

    ATMOSHPERE_RANGE = 6000
    DRAG_ZONE_SIZE = 6500
    DEATH_ZONE_SIZE = 4000


class Sig17BaseEdgeNebula(zones.NebulaZone):
    MUSIC = Ambience.NEBULA_EDGE
    INTERFERENCE = 0.5

    SPACEDUST = Dust.ATTRACT_GREEN
    SPACEDUST_MAXPARTICLES = 100

    PROPERTY_FLAGS = 32768
    PROPERTY_FOG_COLOR = '150, 100, 20'


class Sig17BaseCrowNebula(zones.NebulaZone):
    MUSIC = Ambience.NEBULA_CROW
    INTERFERENCE = 0.5

    SPACEDUST = Dust.ATTRACT
    SPACEDUST_MAXPARTICLES = 100

    PROPERTY_FLAGS = 32768
    PROPERTY_FOG_COLOR = '150, 100, 20'


class Sig17EastNorthNebula(Sig17Member, Sig17BaseEdgeNebula):
    INDEX = 1
    CONTENT_TEMPLATE = sig17_nebula.Sig17EdgeNebulaTemplate


class Sig17EastSouthNebula(Sig17Member, Sig17BaseEdgeNebula):
    INDEX = 2
    CONTENT_TEMPLATE = sig17_nebula.Sig17EdgeNebulaTemplate


class Sig17WestNebula(Sig17Member, Sig17BaseEdgeNebula):
    INDEX = 3
    CONTENT_TEMPLATE = sig17_nebula.Sig17CrowNebulaTemplate


EDGE_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.EDGE_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '200, 200, 200',
    'fog_far': 5000,
}


CROW_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.CROW_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '255, 255, 255',
    'fog_far': 5000,
}


class Sig17AsteroidDefinition1(asteroid_definition.Omega15NiobiumAsteroidDefinition):
    BELT = True
    BILLBOARDS = True
    DYNAST = True


class Sig17AsteroidZone1(Sig17Member, zones.AsteroidZone):
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = Sig17AsteroidDefinition1


class Sig17AbandonedAstBase1(Sig17Member, main_objects.AbandonedAsteroid):
    ALIAS = 'ast'
    INDEX = 3
    BASE_INDEX = 51
    ROTATE_RANDOM = True
    ARCHETYPE = 'om15_base_medium01'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True
    RU_NAME = MS('База Солт-Лейк-Сити', "Salt-Lake-City Base")

    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        Sig17AsteroidZone1,
    ]
    AST_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.ASTEROID,
        'spacedust_maxparticles': 200,
    }
    MISC_EQUIP_TYPE = LI_PIRATE
    WEAPON_FACTION = WEAPON_LI
    EQUIP_SET = markets.EquipSet(
        Q.Gun('li_starlinegun', eq_classes=markets.SECRET2),
        Q.Engine(None, eq_classes=markets.SECRET2),
    )


class Sig17AsteroidReward(Sig17Member, mineable.AsteroidRewardsGroupUltra):
    NAME = 'sig17_unlock'
    SOLAR = asteroid.AsteroidOmega15
    REWARD_ITEM = roid(NIOBIUM)
    ULTRA_REWARD_BASES = [
        Sig17AbandonedAstBase1,
    ]


class Sig17AstMineableField(mineable.MineableAsteroidField):
    BOX_SIZE = 1400
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.3
    DRIFT_Y = 0
    DRIFT_Z = 0.3


class Sig17BaseAsteroidRewardField(mineable.AsteroidRewardField):
    ALIAS = 'ast'
    FIELD_CLASS = Sig17AstMineableField
    REWARDS_GROUP_CLASS = Sig17AsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class Sig17RewardAsteroids1(Sig17Member, Sig17BaseAsteroidRewardField):
    INDEX = 3
    ULTRA_BASE = Sig17AbandonedAstBase1


class Sig17BaseNomadAstZone(zones.AsteroidZone):
    ASTEROID_DEFINITION_CLASS = asteroid_definition.NomadDynasteroids
    ALIAS = 'ast'
    MUSIC = Ambience.ASTEROID_NOMAD


class Sig17EastNorthNomadAstZone(Sig17Member, Sig17BaseNomadAstZone):
    INDEX = 1


class Sig17EastSouthNomadAstZone(Sig17Member, Sig17BaseNomadAstZone):
    INDEX = 2


class Sig17BaseDreadRuins(main_objects.LockedBattleship):
    ALIAS = 'battleship_ruins'
    ROTATE_RANDOM = True
    ARCHETYPE = 'suprise_li_dreadnought'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True
    AST_EXCLUSION_ZONE_SIZE = 600

    NEBULA_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.RADIOACTIVE_RED,
        'spacedust_maxparticles': 200,
    }


class Sig17BaseMinesZone(zones.AsteroidZone):
    ASTEROID_DEFINITION_CLASS = asteroid_definition.SpaceMines
    ALIAS = 'battleship_ruins'
    SPACEDUST = Dust.DEBRIS
    SPACEDUST_MAXPARTICLES = 100
    MUSIC = Ambience.MINE_AST
    INTERFERENCE = 0.1
    DRAG_MODIFIER = 1.5
    PROPERTY_FLAGS = 4128


class Sig17DreadMinesZone1(Sig17Member, Sig17BaseMinesZone):
    INDEX = 1


class Sig17DreadMinesZone2(Sig17Member, Sig17BaseMinesZone):
    INDEX = 2


class Sig17DreadRuins1(Sig17Member, Sig17BaseDreadRuins):
    INDEX = 1
    BASE_INDEX = 52
    ASTEROID_ZONES = [
        Sig17DreadMinesZone1,
    ]
    RU_NAME = MS('Линкор Невада', 'Battleship Nevada')


class Sig17DreadRuins2(Sig17Member, Sig17BaseDreadRuins):
    INDEX = 2
    BASE_INDEX = 53
    ASTEROID_ZONES = [
        Sig17DreadMinesZone2,
    ]
    RU_NAME = MS('Линкор Калифорния', 'Battleship California')


class Sig17DreadSupriseRewards(Sig17Member, mineable.DefaultSupriseRewardsGroup):
    NAME = 'sig17_dread_ruins_suprise'
    SOLAR = suprise.LibertyMiscFighter
    REWARD_ITEM = None
    ULTRA_REWARD_BASES = [
        Sig17DreadRuins1,
        Sig17DreadRuins2,
    ]


class Sig17DreadRuinsSupriseField(mineable.DefaultField):
    BOX_SIZE = 400
    DENSITY_MULTIPLER = 4
    DRIFT_X = 0.5
    DRIFT_Y = 0.5
    DRIFT_Z = 0.5
    EMPTY_CHANCE = 0.2


class Sig17BaseSolarSupriseRewardField(mineable.SupriseRewardField):
    ALIAS = 'battleship_ruins'
    FIELD_CLASS = Sig17DreadRuinsSupriseField
    REWARDS_GROUP_CLASS = Sig17DreadSupriseRewards
    ULTRA_REWARD = True


class Sig17SolarSupriseRewardField1(Sig17Member, Sig17BaseSolarSupriseRewardField):
    INDEX = 1
    ULTRA_BASE = Sig17DreadRuins1


class Sig17SolarSupriseRewardField2(Sig17Member, Sig17BaseSolarSupriseRewardField):
    INDEX = 2
    ULTRA_BASE = Sig17DreadRuins2


class Sig17NewYorkJumpgate(Sig17Member, main_objects.Jumpgate):
    INDEX = 1
    REL = TOP
    TARGET_SYSTEM_NAME = 'li_mnh'


class Sig17ForbesJumpgate(Sig17Member, main_objects.Jumpgate):
    INDEX = 2
    REL = BOTTOM
    TARGET_SYSTEM_NAME = 'li_for'


class Sig17Freeport(Sig17Member, main_objects.Freeport):
    BASE_INDEX = 1
    REL = LEFT
    SPACE_OBJECT_TEMPLATE = cambridge_research.CambridgeResearchAlternative
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.LibertyCivilianDealers

    RU_NAME = MS('Фрипорт 8', "Freeport 8")


class Sig17Battleship(Sig17Member, main_objects.LibertyBattleship):
    BASE_INDEX = 2
    REL = LEFT
    INTERIOR_CLASS = interior.BattleshipInterior
    DEALERS = dealers.LibertyMilitaryDealers
    SHIP_SET = markets.ShipSet('li_elite2')

    RU_NAME = MS('Линкор Грифон', 'Battleship Griffin')


class Sig17Police(Sig17Member, main_objects.Outpost):
    ALIAS = 'police'
    BASE_INDEX = 3
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = police.PoliceOutpostLiberty
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.LibertyMilitaryDealers

    RU_NAME = MS('Аванпост Геттисберг', "Outpost Gettysburg")


class Sig17Liner(Sig17Member, main_objects.LuxuryLiner):
    ALIAS = 'luxury'
    BASE_INDEX = 4
    REL = BOTTOM
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.LibertyCivilianDealers

    RU_NAME = MS('Круизный лайнер Фл+остон', "Cruise Line Fhloston")


class Sig17FreeportSevenRuins(Sig17Member, main_objects.StationRuins):
    ALIAS = 'ruins'
    INDEX = 1
    REL = RIGHT

    SPACE_OBJECT_TEMPLATE = station_debris.Freeport7Debris

    RU_NAME = MS('Фрипорт 7', 'Freeport 7')
    RU_FIRST_DESCRIPTION = dockable_info.sig17_fp7


class Sig17FreeportSevenRuins1(Sig17Member, main_objects.HackableStation):
    ALIAS = 'ruins_dock'
    INDEX = 1
    BASE_INDEX = 61
    RELATED_OBJECT = Sig17FreeportSevenRuins
    RELATED_OBJECT_INDEX = 0
    HACKABLE_SOLAR_CLASS = hackable.HackableFreeport7Dock
    INTERIOR_CLASS = interior.EquipDeckInterior

    RU_NAME = MS('Стыковочный узел 1 Фрипорта 7', 'Freeport 7 Docking Point 1')
    MISC_EQUIP_TYPE = LI_CIV
    WEAPON_FACTION = WEAPON_LI
    EQUIP_SET = markets.EquipSet(
        Q.Gun('li_shieldgun', eq_classes=markets.SECRET2),
        Q.Shield(LI_CIV, eq_classes=markets.SECRET3),
    )


class Sig17FreeportSevenRuin2(Sig17Member, main_objects.HackableStation):
    ALIAS = 'ruins_dock'
    INDEX = 2
    BASE_INDEX = 62
    RELATED_OBJECT = Sig17FreeportSevenRuins
    RELATED_OBJECT_INDEX = 1
    HACKABLE_SOLAR_CLASS = hackable.HackableFreeport7DockRot180
    INTERIOR_CLASS = interior.EquipDeckInterior

    RU_NAME = MS('Стыковочный узел 2 Фрипорта 7','Freeport 7 Docking Point 2')
    MISC_EQUIP_TYPE = LI_CIV
    WEAPON_FACTION = WEAPON_LI
    EQUIP_SET = markets.EquipSet(
        Q.GenericLauncher(CD_MISSILE, eq_classes=markets.MISSILE),
        Q.Shield(LI_PIRATE, eq_classes=markets.SECRET3),
    )


class Sig17EdgeNebulaPirates(Sig17Member, main_objects.PirateAsteroid):
    INDEX = 1
    BASE_INDEX = 5
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = astbase.NomadAsteroidBase
    FACTION = faction.Corsairs

    RU_NAME = MS('Форт Ред-Ривер', 'Fort Red-River')

    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.LibertyPirateDealers

    NEBULA_ZONES = [
        Sig17EastNorthNebula
    ]
    EXCLUSION_PARAMS = EDGE_EXCLUSION_PARAMS
    NEBULA_EXCLUSION_ZONE_SIZE = 2000

    ASTEROID_ZONES = [
        Sig17EastNorthNomadAstZone
    ]
    AST_EXCLUSION_ZONE_SIZE = 2500


class Sig17CrowNebulaPirates(Sig17Member, main_objects.PirateStation):
    INDEX = 2
    BASE_INDEX = 6
    REL = LEFT
    SPACE_OBJECT_TEMPLATE = pirate.LibertyRombicPirateBase
    FACTION = faction.LibertyRogues

    RU_NAME = MS('База М+оркрофт', 'Morecroft Base')

    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.LibertyPirateDealers

    NEBULA_ZONES = [
        Sig17WestNebula
    ]
    EXCLUSION_PARAMS = CROW_EXCLUSION_PARAMS
    NEBULA_EXCLUSION_ZONE_SIZE = 2000


class Sig17LuxuryRuins1(Sig17Member, main_objects.HackableLuxury):
    ALIAS = 'liner_ruins'
    INDEX = 1
    BASE_INDEX = 63
    REL = RIGHT
    HACKABLE_SOLAR_CLASS = hackable.HackableLuxuryLiner
    INTERIOR_CLASS = interior.EquipDeckInterior

    RU_NAME = MS('Круизный лайнер Атлантика', 'Cruise Line Atlantic')
    MISC_EQUIP_TYPE = LI_CIV
    WEAPON_FACTION = WEAPON_LI
    EQUIP_SET = markets.EquipSet(
        Q.Gun('li_civgun', eq_classes=markets.SECRET3),
        Q.Engine(LI_PIRATE, eq_classes=markets.SECRET3),
    )


class Sig17Planet1(Sig17Member, main_objects.Planet):
    ARCHETYPE = 'planet_gasblucld_5000'
    SPHERE_RADIUS = 5000
    RU_NAME = MS('Планета Чикасо', 'Planet Chickasaw')


class Sig17Planet2(Sig17Member, main_objects.Planet):
    INDEX = 2
    ARCHETYPE = 'planet_icemntcld_4000'
    SPHERE_RADIUS = 4000
    RU_NAME = MS('Планета Маскоджи', 'Planet Muskogee')


class Sig17FreeportConn1(Sig17Member, main_objects.TradeConnection):
    OBJ_FROM = Sig17NewYorkJumpgate
    OBJ_TO = Sig17Freeport
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        Sig17EdgeNebulaPirates
    ]


class Sig17FreeportConn2(Sig17Member, main_objects.TradeConnection):
    OBJ_FROM = Sig17Freeport
    OBJ_TO = Sig17Battleship
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        Sig17CrowNebulaPirates
    ]

    OBJ_TO_TLR_FORCE_OFFSET = (-15420, 0, 25038)


class Sig17FreeportConn3(Sig17Member, main_objects.TradeConnection):
    OBJ_FROM = Sig17Freeport
    OBJ_TO = Sig17Police
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        Sig17CrowNebulaPirates
    ]


class Sig17BattleshipConn1(Sig17Member, main_objects.TradeConnection):
    OBJ_FROM = Sig17Battleship
    OBJ_TO = Sig17ForbesJumpgate
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        Sig17CrowNebulaPirates
    ]

    OBJ_FROM_TLR_FORCE_OFFSET = (-16826, 0, 29264)


class Sig17LinerConn1(Sig17Member, main_objects.BuoyTradeConnection):
    OBJ_FROM = Sig17Freeport
    OBJ_TO = Sig17Liner
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'E'

    OBJ_FROM_TLR_FORCE_OFFSET = (-12000, 0, -19000)


class Sig17LinerConn2(Sig17Member, main_objects.BuoyTradeConnection):
    OBJ_FROM = Sig17Liner
    OBJ_TO = Sig17Police
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'F'


class Sig17BrokenLinerConn1(Sig17Member, main_objects.AbandonedBuoyTradeConnection):
    OBJ_FROM = Sig17Battleship
    OBJ_TO = Sig17LuxuryRuins1
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'G'

    OBJ_FROM_TLR_FORCE_OFFSET = (-11000, 0, 28000)


class Sig17FreeportSevenConn1(Sig17Member, main_objects.BrokenTradeConnection):
    OBJ_FROM = Sig17NewYorkJumpgate
    OBJ_TO = Sig17FreeportSevenRuins
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'H'


class Sig17FreeportSevenConn2(Sig17Member, main_objects.BrokenTradeConnection):
    OBJ_FROM = Sig17FreeportSevenRuins
    OBJ_TO = Sig17Police
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'I'

