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

from templates.solar import hackable
from templates.solar import asteroid as asteroid_solar
from templates.dockable import pirate
from templates.dockable import asteroid as asteroid_base
from templates.dockable import trade_storages
from templates.dockable import columbia_production
from templates.dockable import constanta
from templates.dockable import station_debris
from templates.dockable import junker
from templates.dockable import police
from templates.dockable import trade_storages


class Sigma8Member(object):
    INDEX = 1
    FACTION = faction.RH_GRP
    ABSTRACT = False

    INTERIOR_BG1 = interior.INTERIOR_SIG8


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


[EncounterParameters]
nickname = rh_grp_main_defend
filename = missions\\npc\\rh\\rh_grp_main_defend.ini

[EncounterParameters]
nickname = rh_grp_main_scout
filename = missions\\npc\\rh\\rh_grp_main_scout.ini

[EncounterParameters]
nickname = rh_grp_main_gunboat
filename = missions\\npc\\rh\\rh_grp_main_gunboat.ini

[EncounterParameters]
nickname = rh_grp_main_elite2
filename = missions\\npc\\rh\\rh_grp_main_elite2.ini

[EncounterParameters]
nickname = rh_grp_main_trade
filename = missions\\npc\\rh\\rh_grp_main_trade.ini

[EncounterParameters]
nickname = bh_grp_rh_trade
filename = missions\\npc\\rh\\bh_grp_rh_trade.ini

[EncounterParameters]
nickname = bh_grp_rh_scout
filename = missions\\npc\\rh\\bh_grp_rh_scout.ini

[EncounterParameters]
nickname = tr_grp_rh_transport
filename = missions\\npc\\rh\\tr_grp_rh_transport.ini

[EncounterParameters]
nickname = co_grp_main_defend
filename = missions\\npc\\co\\co_grp_main_defend.ini

[EncounterParameters]
nickname = co_grp_main_assault
filename = missions\\npc\\co\\co_grp_main_assault.ini

[EncounterParameters]
nickname = rx_grp_main_defend
filename = missions\\npc\\pi\\rx_grp_main_defend.ini

[EncounterParameters]
nickname = pi_grp_rh_assault
filename = missions\\npc\\pi\\pi_grp_rh_assault.ini

[EncounterParameters]
nickname = area_xscout
filename = missions\\NPC\\area_rebels.ini

[EncounterParameters]
nickname = rh_grp_main_trade_tlr
filename = missions\\npc\\rh\\rh_grp_main_trade_tlr.ini

[EncounterParameters]
nickname = tr_grp_rh_transport_tlr
filename = missions\\npc\\rh\\tr_grp_rh_transport_tlr.ini

[EncounterParameters]
nickname = bh_grp_rh_trade_tlr
filename = missions\\npc\\rh\\bh_grp_rh_trade_tlr.ini

[EncounterParameters]
nickname = rh_pirates_patrol
filename = missions\\npc\\pi\\pi_grp_rh_patrol.ini

[EncounterParameters]
nickname = rh_grp_main_patrol
filename = missions\\npc\\rh\\rh_grp_main_patrol.ini

[EncounterParameters]
nickname = rx_grp_main_patrol
filename = missions\\npc\\pi\\rx_grp_main_patrol.ini

[EncounterParameters]
nickname = patrol_tlr
filename = missions\\NPC\\patrol_tlr.ini

[EncounterParameters]
nickname = patrol_police
filename = missions\\NPC\\patrol_police.ini

[EncounterParameters]
nickname = bh_grp_rh_patrol
filename = missions\\npc\\rh\\bh_grp_rh_patrol.ini

[EncounterParameters]
nickname = rx_grp_patrol_trade
filename = missions\\NPC\\PI\\rx_grp_patrol_trade.ini

[EncounterParameters]
nickname = rh_junkers
filename = missions\\npc\\rh\\rh_junkers.ini

[EncounterParameters]
nickname = co_grp_main_patrol
filename = missions\\npc\\co\\co_grp_main_patrol.ini

'''




class Sig8BaseAsteroidDefinition(asteroid_definition.Omega15NiobiumAsteroidDefinition):
    ABSTRACT = True
    NAME = None
    DYNAST = True
    BELT = True
    BILLBOARDS = True
    LOOT = False  # TEMP


class Sig8AsteroidDefinition1(Sig8BaseAsteroidDefinition):
    ABSTRACT = False
    NAME = 'sig8_astfield1'


class Sig8AsteroidDefinition2(Sig8BaseAsteroidDefinition):
    ABSTRACT = False
    NAME = 'sig8_astfield2'


class Sig8AsteroidDefinition3(Sig8BaseAsteroidDefinition):
    ABSTRACT = False
    NAME = 'sig8_astfield3'


class Sig8AsteroidDefinition4(Sig8BaseAsteroidDefinition):
    ABSTRACT = False
    NAME = 'sig8_astfield4'


class Sig8BaseVanillaAstZone(zones.AsteroidZone):
    SPACEDUST = Dust.ASTEROID
    SPACEDUST_MAXPARTICLES = 100
    MUSIC = Ambience.AST_ROCK


class Sig8AsteroidZone1(Sigma8Member, Sig8BaseVanillaAstZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = Sig8AsteroidDefinition1


class Sig8AsteroidZone2(Sigma8Member, Sig8BaseVanillaAstZone):
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = Sig8AsteroidDefinition2


class Sig8AsteroidZone3(Sigma8Member, Sig8BaseVanillaAstZone):
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = Sig8AsteroidDefinition3


class Sig8AsteroidZone4(Sigma8Member, Sig8BaseVanillaAstZone):
    INDEX = 4
    ASTEROID_DEFINITION_CLASS = Sig8AsteroidDefinition4


class Sig8Sun(Sigma8Member, main_objects.Sun):
    STAR = 'med_blue_sun'
    LOADOUT = 'med_blue_sun_fx'


class Sig8BerlinJumpgate(Sigma8Member, main_objects.Jumpgate):
    INDEX = 1
    REL = TOP


class Sig8BizmarkJumpgate(Sigma8Member, main_objects.Jumpgate):
    INDEX = 2
    REL = BOTTOM


class Sig8Station(Sigma8Member, main_objects.Station):
    INDEX = 1
    BASE_INDEX = 1
    REL = LEFT

    ARCHETYPE = 'largestation1_old'
    LOADOUT = 'largestation_rh'

    AUDIO_PREFIX = SpaceVoice.STATION
    INTERIOR_CLASS = interior.StationShipdealerInterior
    DEALERS = dealers.RheinlandCivilianDealers


class Sig8Freeport(Sigma8Member, main_objects.Freeport):
    INDEX = 1
    BASE_INDEX = 2
    REL = LEFT

    SPACE_OBJECT_TEMPLATE = trade_storages.HonshuStorage

    AUDIO_PREFIX = SpaceVoice.FREEPORT
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.RheinlandCivilianDealers


class Sig8BorderStation(Sigma8Member, main_objects.Outpost):
    INDEX = 1
    BASE_INDEX = 3
    REL = RIGHT

    SPACE_OBJECT_TEMPLATE = police.SigmaEightPoliceOutpost

    AUDIO_PREFIX = SpaceVoice.BORDER_STATION
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.RheinlandMilitaryDealers


class Sig8Junkers(Sigma8Member, main_objects.JunkerBase):
    INDEX = 1
    BASE_INDEX = 4
    REL = RIGHT

    SPACE_OBJECT_TEMPLATE = junker.SigmaEightJunker

    FACTION = faction.JUNK_GRP
    DEFENCE_LEVEL = None

    AUDIO_PREFIX = SpaceVoice.STATION
    INTERIOR_CLASS = interior.PirateStationInterior
    DEALERS = dealers.RheinlandCivilianDealers


class Sig8Pirate(Sigma8Member, main_objects.PirateBase):
    INDEX = 1
    BASE_INDEX = 5
    REL = RIGHT

    SPACE_OBJECT_TEMPLATE = pirate.ManhattanPirateBase

    FACTION = faction.RX_GRP
    DEFENCE_LEVEL = None

    AUDIO_PREFIX = SpaceVoice.STATION
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.RheinlandCivilianDealers


class Sigma8Planet1(Sigma8Member, main_objects.Planet):
    INDEX = 1
    ARCHETYPE = 'planet_gaspurcld_5000'
    SPHERE_RADIUS = 5000
    RING = True
    RING_ZONE_ALIAS = 'ring'
    RING_ZONE_INDEX = 1
    RING_FILE_NAME = 'sig8'


class Sigma8Planet2(Sigma8Member, main_objects.Planet):
    INDEX = 2
    ARCHETYPE = 'planet_icemntcld_2500'
    SPHERE_RADIUS = 2500


class Sigma8Planet3(Sigma8Member, main_objects.Planet):
    INDEX = 3
    ARCHETYPE = 'planet_crater_1500'
    SPHERE_RADIUS = 1500


class Sig8OldFreeportRuins(Sigma8Member, main_objects.NotDockableObject):
    ALIAS = 'ruins'
    INDEX = 1
    REL = RIGHT

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


class Sig8BattleshipRuins1(Sigma8Member, main_objects.HackableBattleship):
    ALIAS = 'ast'
    INDEX = 2
    BASE_INDEX = 61
    HACKABLE_SOLAR_CLASS = hackable.HackableRheinlandBattleship
    INTERIOR_CLASS = interior.EquipDeckInterior

    ASTEROID_ZONES = [
        Sig8AsteroidZone2,
    ]


class Sig8BattleshipRuins2(Sigma8Member, main_objects.HackableBattleship):
    ALIAS = 'ast'
    INDEX = 3
    BASE_INDEX = 62
    HACKABLE_SOLAR_CLASS = hackable.HackableRheinlandBattleship
    INTERIOR_CLASS = interior.EquipDeckInterior

    ASTEROID_ZONES = [
        Sig8AsteroidZone3,
    ]


class Sig8BattleshipRuins3(Sigma8Member, main_objects.HackableBattleship):
    ALIAS = 'ast'
    INDEX = 4
    BASE_INDEX = 63
    HACKABLE_SOLAR_CLASS = hackable.HackableRheinlandBattleship
    INTERIOR_CLASS = interior.EquipDeckInterior

    ASTEROID_ZONES = [
        Sig8AsteroidZone4,
    ]


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


class Sig8GreenNebula1(Sigma8Member, zones.NebulaZone):
    INDEX = 1
    FILE_NAME = 'sig8_green_nebula'
    SPACEDUST = Dust.ATTRACT_GREEN
    SPACEDUST_MAXPARTICLES = 40
    MUSIC = Ambience.BADLANDS


class Sig8GreenNebula2(Sigma8Member, zones.NebulaZone):
    INDEX = 2
    FILE_NAME = 'sig8_green_nebula'
    SPACEDUST = Dust.ATTRACT_GREEN
    SPACEDUST_MAXPARTICLES = 40
    MUSIC = Ambience.BADLANDS


class Sig8BrownNebula1(Sigma8Member, zones.NebulaZone):
    INDEX = 3
    FILE_NAME = 'sig8_brown_nebula'
    SPACEDUST = Dust.ATTRACT
    SPACEDUST_MAXPARTICLES = 40
    MUSIC = Ambience.NEBULA_DMATTER


class Sig8BrownNebula2(Sigma8Member, zones.NebulaZone):
    INDEX = 4
    FILE_NAME = 'sig8_brown_nebula'
    SPACEDUST = Dust.ATTRACT
    SPACEDUST_MAXPARTICLES = 40
    MUSIC = Ambience.NEBULA_DMATTER


class Sigma8EastAsteroidReward(Sigma8Member, mineable.AsteroidRewardsGroupMedium):
    NAME = 'sig8_east_ast'
    SOLAR = asteroid_solar.AsteroidOmega15
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