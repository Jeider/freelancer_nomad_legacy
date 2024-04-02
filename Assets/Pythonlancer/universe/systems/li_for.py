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
from templates.solar import asteroid
from templates.solar import hackable
from templates.solar import debris_box
from templates.nebula import li_for_nebula
from templates.nebula import exclusion

from templates.dockable import astbase
from templates.dockable import shipyards
from templates.dockable import research
from templates.dockable import forbes_megafactory
from templates.dockable import police
from templates.dockable import alg
from templates.dockable import junker
from templates.dockable import station_debris


class ForbesMember(object):
    INDEX = 1
    ABSTRACT = False
    FACTION = faction.LI_GRP

    INTERIOR_BG1 = interior.INTERIOR_LI_FORBES


class ForbesStaticText(ForbesMember, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = li_for
space_color = 0, 10, 8
local_faction = li_grp
space_farclip = 200000

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Music]
space = music_li_space
danger = music_li_danger
battle = music_li_battle

[Dust]
spacedust = Dust

[Ambient]
color = 6, 20, 16

[Background]
nebulae = solar\\stars_mod\\li_for_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_li_for_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
property_flags = 512 ;lava - MILITARY
;property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = li_for_system_light
pos = 0, 0, 0
color = 255, 255, 255
;color = 253, 180, 70
range = 90000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION

'''


class ForbesBaseGreenNebula(zones.NebulaZone):
    SPACEDUST = Dust.ATTRACT_GREEN
    SPACEDUST_MAXPARTICLES = 40
    MUSIC = Ambience.NEBULA_WALKER
    CONTENT_TEMPLATE = li_for_nebula.ForbesGreenNebula
    INTERFERENCE = 0.5

    PROPERTY_FLAGS = 32768
    PROPERTY_FOG_COLOR = '150, 100, 20'


class ForbesSouthWestNebula(ForbesMember, ForbesBaseGreenNebula):
    INDEX = 1


FORBES_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.EDGE_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '200, 200, 255',
    'fog_far': 5000,
}


class ForbesDebrisZone1(ForbesMember, zones.DebrisZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class ForbesDebrisZone2(ForbesMember, zones.DebrisZone):
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class ForbesDebrisZone3(ForbesMember, zones.DebrisZone):
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class ForbesDebrisZone4(ForbesMember, zones.DebrisZone):
    INDEX = 4
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class ForbesDebrisZone5(ForbesMember, zones.DebrisZone):
    INDEX = 5
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class ForbesDebrisZone6(ForbesMember, zones.DebrisZone):
    INDEX = 6
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class ForbesBaseDebrisManufactoring(main_objects.DebrisManufactoring):
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


class ForbesDebrisFactory1(ForbesMember, ForbesBaseDebrisManufactoring):
    INDEX = 1
    BASE_INDEX = 51
    ASTEROID_ZONES = [
        ForbesDebrisZone1,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500


class ForbesDebrisFactory2(ForbesMember, ForbesBaseDebrisManufactoring):
    INDEX = 2
    BASE_INDEX = 52
    ASTEROID_ZONES = [
        ForbesDebrisZone2,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500


class ForbesDebrisFactory3(ForbesMember, ForbesBaseDebrisManufactoring):
    INDEX = 3
    BASE_INDEX = 53
    ASTEROID_ZONES = [
        ForbesDebrisZone3,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500


class ForbesDebrisFactory4(ForbesMember, ForbesBaseDebrisManufactoring):
    INDEX = 4
    BASE_INDEX = 54
    ASTEROID_ZONES = [
        ForbesDebrisZone4,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500


class ForbesDebrisBoxReward(ForbesMember, mineable.DefaultDebrisBoxRewardsGroup):
    NAME = 'li_for_debrisbox'
    SOLAR = debris_box.DebrisBox
    REWARD_ITEM = 'comm_scrap_metal'
    ULTRA_REWARD_BASES = [
        ForbesDebrisFactory1,
        ForbesDebrisFactory2,
        ForbesDebrisFactory3,
        ForbesDebrisFactory4,
    ]


class ForbesBaseDebrisBoxRewardField(mineable.DebrisBoxRewardField):
    FIELD_CLASS = mineable.MineableDebrixBoxField
    REWARDS_GROUP_CLASS = ForbesDebrisBoxReward
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class ForbesDebrisBoxField1(ForbesMember, ForbesBaseDebrisBoxRewardField):
    INDEX = 1
    ULTRA_BASE = ForbesDebrisFactory1


class ForbesDebrisBoxField2(ForbesMember, ForbesBaseDebrisBoxRewardField):
    INDEX = 2
    ULTRA_BASE = ForbesDebrisFactory2


class ForbesDebrisBoxField3(ForbesMember, ForbesBaseDebrisBoxRewardField):
    INDEX = 3
    ULTRA_BASE = ForbesDebrisFactory3


class ForbesDebrisBoxField4(ForbesMember, ForbesBaseDebrisBoxRewardField):
    INDEX = 4
    ULTRA_BASE = ForbesDebrisFactory4


class ForbesAsteroidDefinition1(asteroid_definition.CaliforniaAsteroidDefinition):
    BELT = True
    BILLBOARDS = True
    DYNAST = True
    LOOT = False  # TEMP


class ForbesAsteroidZone1(ForbesMember, zones.AsteroidZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = ForbesAsteroidDefinition1


class ForbesAsteroidReward(ForbesMember, mineable.AsteroidRewardsGroupHigh):
    NAME = 'li_for_norewardast'
    SOLAR = asteroid.AsteroidCalifornia
    REWARD_ITEM = 'comm_roid_uranium'


class ForbesMineableField(mineable.MineableAsteroidField):
    BOX_SIZE = 1400
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.3
    DRIFT_Y = 0
    DRIFT_Z = 0.3


class ForbesBaseAsteroidRewardField(mineable.AsteroidRewardField):
    ALIAS = 'ast'
    FIELD_CLASS = ForbesMineableField
    REWARDS_GROUP_CLASS = ForbesAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25
    ULTRA_REWARD = False


class ForbesRewardAsteroids1(ForbesMember, ForbesBaseAsteroidRewardField):
    INDEX = 1


class ForbesSun(ForbesMember, main_objects.Sun):
    STAR = 'med_yellow_sun'
    LOADOUT = 'med_yellow_sun_fx'


class ForbesSigma13Jumpgate(ForbesMember, main_objects.Jumpgate):
    INDEX = 1
    REL = BOTTOM


class ForbesSigma17Jumpgate(ForbesMember, main_objects.Jumpgate):
    INDEX = 2
    REL = TOP


class ForbesDockring(ForbesMember, main_objects.Dockring):
    BASE_INDEX = 1
    REL = RIGHT
    AUDIO_PREFIX = SpaceVoice.LI_PLANET
    INTERIOR_CLASS = interior.CustomFullSplitRoomInterior
    DEALERS = dealers.LibertyPlanetDealers


class ForbesShipyard(ForbesMember, main_objects.Shipyard):
    BASE_INDEX = 2
    REL = RIGHT
    REL_DRIFT = 200
    REL_APPEND = 1000
    SPACE_OBJECT_TEMPLATE = shipyards.ForbesShipyard
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.LibertyCivilianDealers

    NEBULA_ZONES = [
        ForbesBaseGreenNebula
    ]
    EXCLUSION_PARAMS = FORBES_EXCLUSION_PARAMS


class ForbesRefinery(ForbesMember, main_objects.Refinery):
    BASE_INDEX = 3
    REL = TOP
    SPACE_OBJECT_TEMPLATE = alg.AlgBaseHokkaido
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.LibertyCivilianDealers
    FACTION = faction.LC_GRP


class ForbesPolice(ForbesMember, main_objects.Outpost):
    ALIAS = 'police'
    BASE_INDEX = 4
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = police.PoliceOutpostLiberty
    INTERIOR_CLASS = interior.OutpostShipdealerInterior
    AUDIO_PREFIX = SpaceVoice.BORDER_STATION
    DEALERS = dealers.LibertyMilitaryDealers


class ForbesLargeStation(ForbesMember, main_objects.Station):
    BASE_INDEX = 5
    REL = BOTTOM
    REL_APPEND = 2500
    SPACE_OBJECT_TEMPLATE = forbes_megafactory.ForbesMegafactory
    AUDIO_PREFIX = SpaceVoice.STATION
    INTERIOR_CLASS = interior.StationShipdealerInterior
    DEALERS = dealers.LibertyCivilianDealers


class ForbesResearch(ForbesMember, main_objects.Station):
    ALIAS = 'research'
    BASE_INDEX = 6
    REL = LEFT

    SPACE_OBJECT_TEMPLATE = research.ForbesResearch

    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.LibertyCivilianDealers


class ForbesPlanet1(ForbesMember, main_objects.Planet):
    ARCHETYPE = 'planet_earthsnwcld_2500'
    SPHERE_RADIUS = 2500
    RELATED_DOCK_RING = ForbesDockring


class ForbesPlanet2(ForbesMember, main_objects.Planet):
    INDEX = 2
    ARCHETYPE = 'planet_crater_2000'
    SPHERE_RADIUS = 2000


class ForbesOldOutpostRuins(ForbesMember, main_objects.NotDockableObject):
    ALIAS = 'ruins'
    INDEX = 1
    REL = LEFT

    SPACE_OBJECT_TEMPLATE = station_debris.ColumbiaDebris
    ASTEROID_ZONES = [
        ForbesDebrisZone5,
    ]


class ForbesOldOutpostRuinsSuprisePoint1(ForbesMember, main_objects.HackableStation):
    ALIAS = 'ruins_dock'
    INDEX = 1
    BASE_INDEX = 71
    RELATED_OBJECT = ForbesOldOutpostRuins
    RELATED_OBJECT_INDEX = 0
    HACKABLE_SOLAR_CLASS = hackable.HackableOutpost
    INTERIOR_CLASS = interior.EquipDeckInterior


class ForbesAsteroidPirates(ForbesMember, main_objects.PirateBase):
    BASE_INDEX = 7
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = astbase.BerlinAsteroidBase
    FACTION = faction.LX_GRP

    DEFENCE_LEVEL = None

    AUDIO_PREFIX = SpaceVoice.OUTPOST
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.LibertyPirateDealers

    ASTEROID_ZONES = [
        ForbesAsteroidZone1
    ]
    AST_EXCLUSION_ZONE_SIZE = 3000


class ForbesJunkers(ForbesMember, main_objects.PirateBase):
    ALIAS = 'junker'
    BASE_INDEX = 8
    REL = TOP
    SPACE_OBJECT_TEMPLATE = junker.BerlinJunker
    FACTION = faction.JUNK_GRP

    DEFENCE_LEVEL = None

    AUDIO_PREFIX = SpaceVoice.OUTPOST
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.LibertyPirateDealers

    ASTEROID_ZONES = [
        ForbesDebrisZone6,
    ]


class ForbesPlanetConn1(ForbesMember, main_objects.TradeConnection):
    OBJ_FROM = ForbesSigma17Jumpgate
    OBJ_TO = ForbesDockring
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        ForbesAsteroidPirates
    ]


class ForbesPlanetConn2(ForbesMember, main_objects.TradeConnection):
    OBJ_FROM = ForbesDockring
    OBJ_TO = ForbesShipyard
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        ForbesAsteroidPirates
    ]


class ForbesPlanetConn3(ForbesMember, main_objects.TradeConnection):
    OBJ_FROM = ForbesLargeStation
    OBJ_TO = ForbesDockring
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        ForbesJunkers
    ]


class ForbesPoliceConn1(ForbesMember, main_objects.TradeConnection):
    OBJ_FROM = ForbesResearch
    OBJ_TO = ForbesPolice
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        ForbesJunkers
    ]


class ForbesPoliceConn2(ForbesMember, main_objects.TradeConnection):
    OBJ_FROM = ForbesPolice
    OBJ_TO = ForbesShipyard
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        ForbesAsteroidPirates
    ]


class ForbesPoliceConn3(ForbesMember, main_objects.TradeConnection):
    OBJ_FROM = ForbesPolice
    OBJ_TO = ForbesSigma13Jumpgate
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'F'


class ForbesStationConn1(ForbesMember, main_objects.TradeConnection):
    OBJ_FROM = ForbesRefinery
    OBJ_TO = ForbesLargeStation
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'G'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        ForbesJunkers
    ]


class ForbesStationConn2(ForbesMember, main_objects.TradeConnection):
    OBJ_FROM = ForbesLargeStation
    OBJ_TO = ForbesResearch
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'H'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        ForbesJunkers
    ]


class ForbesBrokenRuinsConn1(ForbesMember, main_objects.BrokenTradeConnection):
    OBJ_FROM = ForbesOldOutpostRuins
    OBJ_TO = ForbesSigma17Jumpgate
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'I'


class ForbesBrokenRuinsConn2(ForbesMember, main_objects.BrokenTradeConnection):
    OBJ_FROM = ForbesOldOutpostRuins
    OBJ_TO = ForbesLargeStation
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'J'
