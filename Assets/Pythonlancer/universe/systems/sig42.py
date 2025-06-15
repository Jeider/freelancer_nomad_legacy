from managers.tools import query as Q
from world.names import *
from universe.content import meta

from universe import markets

from fx.space import Dust, JumpholeEffect
from fx.sound import Ambience

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
from universe.content import population

from templates.nebula import invisible_nebula
from templates.solar import asteroid
from templates.solar import hackable

from templates.dockable import research
from templates.dockable import odissey
from templates.dockable import pirate


class Sig42Member(Member):
    FACTION = faction.BretoniaMain

    INTERIOR_BG1 = interior.INTERIOR_SIRIUS


class Sig42Bretonia(object):
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_BR
    FACTION = faction.BretoniaMain
    WEAPON_FACTION = WEAPON_BR
    EQUIP_FACTION = EQUIP_BR


class Sig42Kusari(object):
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_KU
    POPULATION_KIND = population.POP_SECOND
    FACTION = faction.KusariMain
    WEAPON_FACTION = WEAPON_KU
    EQUIP_FACTION = EQUIP_KU


class Sig42StaticText(Sig42Member, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = sig42
space_color = 0, 0, 0
local_faction = br_grp
space_farclip = 10000000

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Dust]
spacedust = Dust

[Music]
space = music_sigma_space
danger = music_sigma_danger
battle = music_sigma_battle

[Ambient]
color = 15, 15, 25

[Background]
nebulae = solar\\stars_mod\\sirius_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_sig42_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000

[LightSource]
nickname = sig42_sirius_A_light
pos = -150000, 0, 0
color = 120, 170, 255
range = 800000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION

[LightSource]
nickname = sig42_sirius_B_light
pos = 60000, -10000, 0
color = 225, 225, 255
range = 100000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION
'''


class Sig42Sun1(Sig42Member, main_objects.Sun):
    STAR = 'sirius_A'
    LOADOUT = 'sirius_A_sun_fx'

    ATMOSHPERE_RANGE = 50000
    DRAG_ZONE_SIZE = 50000
    DEATH_ZONE_SIZE = 40000


class Sig42Sun2(Sig42Member, main_objects.Sun):
    INDEX = 2
    STAR = 'med_blue_sun'
    LOADOUT = 'med_blue_sun_fx'

    ATMOSHPERE_RANGE = 10000
    DRAG_ZONE_SIZE = 9500
    DEATH_ZONE_SIZE = 4000


class Sig42WarwickJumpgate(Sig42Member, main_objects.Jumpgate):
    INDEX = 1
    REL = TOP
    TARGET_SYSTEM_NAME = 'br_wrw'


class Sig42HonshuJumpgate(Sig42Member, main_objects.Jumpgate):
    INDEX = 2
    REL = BOTTOM
    TARGET_SYSTEM_NAME = 'ku_hns'


class Sig42AsteroidDefinition1(asteroid_definition.CuracaoAsteroidDefinition):
    BELT = True
    BILLBOARDS = True
    DYNAST = True
    LOOT = False  # TEMP


class Sig42AsteroidZone1(Sig42Member, zones.AsteroidZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = Sig42AsteroidDefinition1


class Sig42AsteroidZone2(Sig42Member, zones.AsteroidZone):
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = Sig42AsteroidDefinition1


class Sig42AsteroidZone3(Sig42Member, zones.AsteroidZone):
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = Sig42AsteroidDefinition1


class Sig42AsteroidReward(Sig42Member, mineable.AsteroidRewardsGroupUltra):
    NAME = 'sig42_bg_ast'
    SOLAR = asteroid.AsteroidCuracao
    REWARD_ITEM = 'comm_roid_uranium'


class Sig42AstMineableField(mineable.MineableAsteroidField):
    BOX_SIZE = 1400
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.3
    DRIFT_Y = 0
    DRIFT_Z = 0.3


class Sig42BaseAsteroidRewardField(mineable.AsteroidRewardField):
    ALIAS = 'ast'
    FIELD_CLASS = Sig42AstMineableField
    REWARDS_GROUP_CLASS = Sig42AsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25
    ULTRA_REWARD = False


class Sig42RewardAsteroids1(Sig42Member, Sig42BaseAsteroidRewardField):
    INDEX = 1


class Sig42RewardAsteroids2(Sig42Member, Sig42BaseAsteroidRewardField):
    INDEX = 2


class Sig42BaseBretoniaSolarPlant(Sig42Bretonia, main_objects.HackableSolarPlant):
    ALIAS = 'solar'
    LOADOUT = 'solar_plant_br'
    HACKABLE_SOLAR_CLASS = hackable.HackableSolarPlantRot90
    INTERIOR_CLASS = interior.EquipDeckInterior


class Sig42BaseKusariSolarPlant(Sig42Kusari, main_objects.HackableSolarPlant):
    ALIAS = 'solar'
    LOADOUT = 'solar_plant_ku'
    HACKABLE_SOLAR_CLASS = hackable.HackableSolarPlantRot90
    INTERIOR_CLASS = interior.EquipDeckInterior


class Sig42SolarPlant1(Sig42Member, Sig42BaseBretoniaSolarPlant):
    INDEX = 1
    BASE_INDEX = 61
    REL = LEFT


class Sig42SolarPlant2(Sig42Member, Sig42BaseBretoniaSolarPlant):
    INDEX = 2
    BASE_INDEX = 62
    REL = LEFT


class Sig42SolarPlant3(Sig42Member, Sig42BaseKusariSolarPlant):
    INDEX = 3
    BASE_INDEX = 63
    REL = LEFT


class Sig42SolarPlant4(Sig42Member, Sig42BaseBretoniaSolarPlant):
    INDEX = 4
    BASE_INDEX = 64
    REL = RIGHT


class Sig42SolarPlant5(Sig42Member, Sig42BaseKusariSolarPlant):
    INDEX = 5
    BASE_INDEX = 65
    REL = RIGHT


class Sig42Dockring(Sig42Member, Sig42Bretonia, main_objects.MiningPlanetDockring):
    BASE_INDEX = 1
    REL = BOTTOM
    AUDIO_PREFIX = SpaceVoice.BR_PLANET
    INTERIOR_CLASS = interior.CustomFullSplitRoomInteriorSecond
    DEALERS = dealers.BretoniaCivilianDealers
    SHIP_SET = markets.ShipSet('br_fighter')

    BASE_PROPS = meta.MiningPlanet(
        objectives=[
            meta.ProduceBad(URANIUM),
            meta.ProduceBad(NICOLLUM),
        ]
    )


class Sig42BretoniaStation(Sig42Member, Sig42Bretonia, main_objects.TradelaneSupportStation):
    INDEX = 1
    BASE_INDEX = 2
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = odissey.OdisseySimple
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.BretoniaCivilianDealers

    BASE_PROPS = meta.TradelaneSupportStation(
        objectives=[
            meta.HaveGreenhouse(),
        ]
    )


class Sig42KusariStation(Sig42Member, Sig42Kusari, main_objects.ResearchStation):
    INDEX = 2
    BASE_INDEX = 3
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = research.SiriusResearch
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.KusariCivilianDealers

    BASE_PROPS = meta.Research(
        objectives=[
            meta.HaveGreenhouse(),
            meta.HaveSolarPanels(),
        ]
    )


class Sig42Liner(Sig42Member, Sig42Bretonia, main_objects.LuxuryLiner):
    ALIAS = 'luxury'
    BASE_INDEX = 4
    REL = LEFT
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.BretoniaCivilianDealers


class Sig42VirtualDepot(Sig42Member, Sig42Bretonia, main_objects.VirtualDepot):
    REL = RIGHT


class Sig42TopPirates(Sig42Member, Sig42Bretonia, main_objects.PirateStation):
    INDEX = 1
    BASE_INDEX = 5
    REL = TOP
    SPACE_OBJECT_TEMPLATE = pirate.LibertyRombicPirateBase
    FACTION = faction.BretoniaPirate

    DEFENCE_LEVEL = None

    AUDIO_PREFIX = SpaceVoice.OUTPOST
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.BretoniaPirateDealers

    ASTEROID_ZONES = [
        Sig42AsteroidZone1
    ]
    AST_EXCLUSION_ZONE_SIZE = 2500


class Sig42BottomPirates(Sig42Member, Sig42Kusari, main_objects.PirateStation):
    INDEX = 2
    BASE_INDEX = 6
    REL = TOP
    SPACE_OBJECT_TEMPLATE = pirate.PirateBaseHokkaido
    FACTION = faction.KusariPirate

    DEFENCE_LEVEL = None

    AUDIO_PREFIX = SpaceVoice.OUTPOST
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.KusariPirateDealers

    ASTEROID_ZONES = [
        Sig42AsteroidZone2
    ]
    AST_EXCLUSION_ZONE_SIZE = 2500


class Sig42Planet1(Sig42Member, main_objects.Planet):
    ARCHETYPE = 'planet_desorcld_3000'
    SPHERE_RADIUS = 3000
    RELATED_DOCK_RING = Sig42Dockring


class Sig42BretoniaStationConn1(Sig42Member, Sig42Bretonia, main_objects.TradeConnection):
    OBJ_FROM = Sig42WarwickJumpgate
    OBJ_TO = Sig42BretoniaStation
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        Sig42TopPirates
    ]


class Sig42BretoniaStationConn2(Sig42Member, Sig42Bretonia, main_objects.TradeConnection):
    OBJ_FROM = Sig42BretoniaStation
    OBJ_TO = Sig42VirtualDepot
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'B'


class Sig42BretoniaStationConn3(Sig42Member, Sig42Bretonia, main_objects.TradeConnection):
    OBJ_FROM = Sig42Liner
    OBJ_TO = Sig42BretoniaStation
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        Sig42TopPirates
    ]


class Sig42KusariStationConn1(Sig42Member, Sig42Kusari, main_objects.TradeConnection):
    OBJ_FROM = Sig42VirtualDepot
    OBJ_TO = Sig42KusariStation
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        Sig42BottomPirates
    ]


class Sig42KusariStationConn2(Sig42Member, Sig42Kusari, main_objects.TradeConnection):
    OBJ_FROM = Sig42KusariStation
    OBJ_TO = Sig42HonshuJumpgate
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        Sig42BottomPirates
    ]


class Sig42KusariStationConn3(Sig42Member, Sig42Kusari, main_objects.TradeConnection):
    OBJ_FROM = Sig42Dockring
    OBJ_TO = Sig42KusariStation
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'F'


class Sig42LinerConn1(Sig42Member, Sig42Bretonia, main_objects.TradeConnection):
    OBJ_FROM = Sig42Liner
    OBJ_TO = Sig42Dockring
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'G'


class Sig42SolarBuoyConn1(Sig42Member, main_objects.AbandonedBuoyTradeConnection):
    OBJ_FROM = Sig42SolarPlant1
    OBJ_TO = Sig42Liner
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'H'

    OBJ_TO_TLR_FORCE_OFFSET = (-42000, 0, -11000)


class Sig42SolarBuoyConn2(Sig42Member, main_objects.AbandonedBuoyTradeConnection):
    OBJ_FROM = Sig42SolarPlant3
    OBJ_TO = Sig42Dockring
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'I'

    OBJ_FROM_TLR_FORCE_OFFSET = (-43000.0, 0.0, 20000.0)


class Sig42SolarBuoyConn3(Sig42Member, main_objects.AbandonedBuoyTradeConnection):
    OBJ_FROM = Sig42VirtualDepot
    OBJ_TO = Sig42SolarPlant4
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'J'


class Sig42InvisibleOrderNebula(Sig42Member, zones.NebulaZone):
    ALIAS = 'invisible'
    INDEX = 1
    CONTENT_TEMPLATE = invisible_nebula.SiriusInvisibleNebula
    SPACEDUST = Dust.RADIOACTIVE_BLUE
    SPACEDUST_MAXPARTICLES = 120
    MUSIC = Ambience.NEBULA_DMATTER


class Sig42InvisibleAsfNebula(Sig42Member, zones.NebulaZone):
    ALIAS = 'invisible'
    INDEX = 2
    CONTENT_TEMPLATE = invisible_nebula.SiriusInvisibleNebula
    SPACEDUST = Dust.RADIOACTIVE_BLUE
    SPACEDUST_MAXPARTICLES = 120
    MUSIC = Ambience.NEBULA_DMATTER


class Sig42OrderJumpgate(Sig42Member, main_objects.JumpgateAlt):
    INDEX = 9
    REL = RIGHT

    FACTION = faction.BretoniaMain
    DEFENCE_LEVEL = None

    TARGET_SYSTEM_NAME = 'or_hq'
    FORCE_INSPACE_NAME = 'jg_sirius_to_or_hq'
    FORCE_TARGET_NAME = 'jg_or_hq_to_sirius'
    LOCKED_DOCK = True


class Sig42AsfJumpgate(Sig42Member, main_objects.JumpgateAlt):
    INDEX = 8
    REL = LEFT

    FACTION = faction.BretoniaMain
    DEFENCE_LEVEL = None

    TARGET_SYSTEM_NAME = 'asf_hq'
    FORCE_INSPACE_NAME = 'jg_sirius_to_asf_hq'
    FORCE_TARGET_NAME = 'jg_asf_hq_to_sirius'
    LOCKED_DOCK = True


class Sig42TekagiJumphole(Sig42Member, main_objects.Jumphole):
    REL = TOP

    TARGET_SYSTEM_NAME = 'ku_tgk'
    LOCKED_DOCK = True

    LOADOUT = JumpholeEffect.LIGHT


class AfterLairOsiris(Sig42Member, main_objects.LibertyBattleship):
    ALIAS = 'lair_osiris'
    INDEX = 1
    BASE_INDEX = 99
    REL = TOP
    INTERIOR_CLASS = interior.OsirisInterior
    DEALERS = dealers.LibertyMilitaryDealers
    STORY = True
    CALC_STORE = False
    IS_BASE = False
    AUTOSAVE_FORBIDDEN = True
    FACTION = faction.LibertyMain
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_LI
    WEAPON_FACTION = WEAPON_LI
    EQUIP_FACTION = EQUIP_LI
    # ASF set?
    SHIP_SET = markets.ShipSet('li_elite')

