from fx.space import Dust
from fx.sound import Ambience

from universe.content.system_object import TOP, BOTTOM, LEFT, RIGHT
from universe.content.main_objects import RawText, SunSmall, Jumpgate, Station, Freeport, RheinlandBattleship, PirateBase, TradeConnection
from universe.content.zones import AsteroidZone
from universe.content.asteroid_definition import Omega15AsteroidDefinition, DebrisDefinition
from universe.content import interior
from universe.content import dealers
from universe.content.space_voice import SpaceVoice
from universe.content import faction


from templates.dockable.gas_miner import BretoniaPirateGasMiner, RheinlandCivilianGasMiner, RheinlandPirateGasMiner, CadizGasMiner

from templates.dockable.prisons import AlaskaPrison


from universe.content.mineable import DefaultAsteroidRewardsGroup, DefaultDebrisBoxRewardsGroup, DefaultField, AsteroidRewardField, DebrisBoxRewardField, AsteroidRewardsGroupMedium, DefaultDebrisBoxRewardsGroupUltra

from templates.solar.asteroid import AsteroidOmega15
from templates.solar.debris_box import DebrisBox


class Sigma13Member(object):
    INDEX = 1
    FACTION = faction.RH_GRP
    ABSTRACT = False


class Sigma13StaticText(Sigma13Member, RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = sig13
space_color = 0, 0, 0
local_faction = rh_grp

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Dust]
spacedust = Dust

[Music]
space = music_sigma_space
danger = music_sigma_danger
battle = music_sigma_battle

[Ambient]
color = 20, 20, 40

[Background]
basic_stars = solar\\stars_mod\\new_generic.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_sig13_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
property_flags = 2048

[LightSource]
nickname = sig13_system_light
pos = -31, 0, -48
color = 120, 250, 255
range = 60000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION

[Nebula]
file = solar\\nebula_mod\\sig13_blue_nebula.ini
zone = Zone_sig13_blue_nebula

[zone]
nickname = Zone_sig13_blue_nebula
ids_name = 203659
pos = 0, 0, 0
shape = SPHERE
size = 500000
property_flags = 32768
property_fog_color = 0, 50, 80
visit = 32
ids_info = 065577
sort = 99
interference = 0.300000
Music = zone_nebula_crow

[EncounterParameters]
nickname = rh_grp_main_defend
filename = missions\\npc\\rh\\rh_grp_main_defend.ini

[EncounterParameters]
nickname = rh_grp_main_scout
filename = missions\\npc\\rh\\rh_grp_main_scout.ini

[EncounterParameters]
nickname = bh_grp_rh_scout
filename = missions\\npc\\rh\\bh_grp_rh_scout.ini

[EncounterParameters]
nickname = li_grp_main_defend
filename = missions\\npc\\li\\li_grp_main_defend.ini

[EncounterParameters]
nickname = li_grp_main_scout
filename = missions\\npc\\li\\li_grp_main_scout.ini

[EncounterParameters]
nickname = bh_grp_li_scout
filename = missions\\npc\\li\\bh_grp_li_scout.ini

[EncounterParameters]
nickname = pi_grp_rh_assault
filename = missions\\npc\\pi\\pi_grp_rh_assault.ini

[EncounterParameters]
nickname = pi_grp_li_assault
filename = missions\\npc\\pi\\pi_grp_li_assault.ini

[EncounterParameters]
nickname = li_grp_main_trade
filename = missions\\npc\\li\\li_grp_main_trade.ini

[EncounterParameters]
nickname = rh_grp_main_trade
filename = missions\\npc\\rh\\rh_grp_main_trade.ini

[EncounterParameters]
nickname = tr_grp_rh_transport
filename = missions\\npc\\rh\\tr_grp_rh_transport.ini

[EncounterParameters]
nickname = tr_grp_li_large_train
filename = missions\\npc\\li\\tr_grp_li_large_train.ini

[EncounterParameters]
nickname = li_grp_main_trade_tlr
filename = missions\\npc\\li\\li_grp_main_trade_tlr.ini

[EncounterParameters]
nickname = rh_grp_main_trade_tlr
filename = missions\\npc\\rh\\rh_grp_main_trade_tlr.ini

[EncounterParameters]
nickname = tr_grp_rh_transport_tlr
filename = missions\\npc\\rh\\tr_grp_rh_transport_tlr.ini

[EncounterParameters]
nickname = tr_grp_li_large_train_tlr
filename = missions\\npc\\li\\tr_grp_li_large_train_tlr.ini

[EncounterParameters]
nickname = rh_grp_main_patrol
filename = missions\\npc\\rh\\rh_grp_main_patrol.ini

[EncounterParameters]
nickname = li_grp_main_patrol
filename = missions\\npc\\li\\li_grp_main_patrol.ini

[EncounterParameters]
nickname = rh_junkers
filename = missions\\npc\\rh\\rh_junkers.ini

[EncounterParameters]
nickname = rh_pirates_patrol
filename = missions\\npc\\pi\\pi_grp_rh_patrol.ini

[EncounterParameters]
nickname = li_pirates_patrol
filename = missions\\npc\\pi\\pi_grp_li_patrol.ini

[EncounterParameters]
nickname = bh_grp_rh_patrol
filename = missions\\npc\\rh\\bh_grp_rh_patrol.ini

[EncounterParameters]
nickname = bh_grp_li_patrol
filename = missions\\npc\\li\\bh_grp_li_patrol.ini

[EncounterParameters]
nickname = co_grp_main_patrol
filename = missions\\npc\\co\\co_grp_main_patrol.ini

[EncounterParameters]
nickname = patrol_tlr
filename = missions\\NPC\\patrol_tlr.ini

[EncounterParameters]
nickname = patrol_police
filename = missions\\NPC\\patrol_police.ini

'''




class Sig13Sun(Sigma13Member, SunSmall):
    STAR = 'med_blue_sun'


class Sig13ForbesJumpgate(Sigma13Member, Jumpgate):
    INDEX = 1
    REL = TOP


class Sig13CaliforniaJumpgate(Sigma13Member, Jumpgate):
    INDEX = 2
    REL = LEFT


class Sig13BerlinJumpgate(Sigma13Member, Jumpgate):
    INDEX = 3
    REL = BOTTOM


class Sig13LibertyStation(Sigma13Member, Station):
    INDEX = 1
    BASE_INDEX = 2
    REL = RIGHT
    ARCHETYPE = 'smallstation1_old'
    LOADOUT = 'smallstation_li'
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.LibertyCivilianDealers


class Sig13RheinlandStation(Sigma13Member, Station):
    INDEX = 2
    BASE_INDEX = 1
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = RheinlandCivilianGasMiner
    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.RheinlandCivilianDealers


class Sig13Battleship(Sigma13Member, RheinlandBattleship):
    BASE_INDEX = 4
    REL = RIGHT
    INTERIOR_CLASS = interior.BattleshipInterior
    DEALERS = dealers.RheinlandMilitaryDealers


class Sig13Freeport(Sigma13Member, Freeport):
    BASE_INDEX = 5
    REL = LEFT
    ARCHETYPE = 'outpost'
    LOADOUT = 'li_big_outpost'
    INTERIOR_CLASS = interior.BattleshipInterior
    DEALERS = dealers.RheinlandMilitaryDealers
    ROTATE_RANDOM = True


class Sig13PirateTopRight(Sigma13Member, PirateBase):
    BASE_INDEX = 6
    INDEX = 1
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = CadizGasMiner
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.LibertyPirateDealers
    FACTION = faction.LX_GRP
    DEFENCE_LEVEL = None


class Sig13PirateTopLeft(Sigma13Member, PirateBase):
    BASE_INDEX = 7
    INDEX = 2
    REL = TOP
    SPACE_OBJECT_TEMPLATE = RheinlandPirateGasMiner
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.LibertyPirateDealers
    FACTION = faction.LX_GRP
    DEFENCE_LEVEL = None


class Sig13PirateBottom(Sigma13Member, PirateBase):
    BASE_INDEX = 8
    INDEX = 3
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = BretoniaPirateGasMiner
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.RheinlandPirateDealers
    FACTION = faction.RX_GRP
    DEFENCE_LEVEL = None
