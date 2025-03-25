from fx.space import Dust
from fx.sound import Ambience

from managers.tools import query as Q
from world.names import *
from universe.content import meta

from universe.content.member import Member
from universe.content.system_object import TOP, BOTTOM, LEFT, RIGHT
from universe.content import main_objects
from universe.content import zones
from universe.content import asteroid_definition
from universe.content import interior
from universe.content import dealers
from universe.audio.space_voice import SpaceVoice
from universe.content import faction
from universe.content import mineable
from templates.solar import asteroid
from templates.solar import hackable
from templates.solar import debris_box
from templates.nebula import ku_hkd_nebula
from templates.nebula import exclusion

from templates.dockable import pirate
from templates.dockable import trade_storages
from templates.dockable import kyushu_megashipyard
from templates.dockable import police
from templates.dockable import alg
from templates.dockable import junker
from templates.dockable import gmg_hq


class HokkMember(Member):
    FACTION = faction.KU_GRP
    INTERIOR_BG1 = interior.INTERIOR_KU_HOKKAIDO


class HokkStaticText(HokkMember, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = ku_hkd
space_color = 13, 10, 6
local_faction = ku_grp
space_farclip = 50000

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Dust]
spacedust = Dust

[Music]
space = music_ku_space
danger = music_ku_danger
battle = music_ku_battle

[Ambient]
; color = 100, 100, 100
color = 12, 10, 6


[Background]
nebulae = solar\\stars_mod\\ku_hkd_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_ku_hkd_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
property_flags = 512 ;lava - MILITARY
;property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = ku_hkd_system_light
pos = -31, 0, -48
color = 150, 170, 255
range = 200000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION
'''


class HokkBaseOrangeNebula(zones.NebulaZone):
    SPACEDUST = Dust.ATTRACT_ORANGE
    SPACEDUST_MAXPARTICLES = 40
    MUSIC = Ambience.NEBULA_WALKER
    CONTENT_TEMPLATE = ku_hkd_nebula.KuHkdOrangeNebulaTemplate
    INTERFERENCE = 0.5

    PROPERTY_FLAGS = 32768
    PROPERTY_FOG_COLOR = '150, 100, 20'


class HokkBaseBarrierNebula(zones.NebulaZone):
    SPACEDUST = Dust.ATTRACT_ORANGE
    SPACEDUST_MAXPARTICLES = 40
    MUSIC = Ambience.NEBULA_BARRIER
    CONTENT_TEMPLATE = ku_hkd_nebula.HokkaidoBarrierNebulaTemplate
    INTERFERENCE = 0.5

    PROPERTY_FLAGS = 32768
    PROPERTY_FOG_COLOR = '150, 100, 20'


class HokkSouthWestNebula(HokkMember, HokkBaseBarrierNebula):
    INDEX = 1


class HokkSouthEastNebula(HokkMember, HokkBaseOrangeNebula):
    INDEX = 2


WALKER_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.WALKER_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '255, 255, 255',
    'fog_far': 5000,
}


BARRIER_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.ICE_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '255, 180, 120',
    'fog_far': 5000,
}


class HokkDebrisZone1(HokkMember, zones.DebrisZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class HokkDebrisZone2(HokkMember, zones.DebrisZone):
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class HokkDebrisZone3(HokkMember, zones.DebrisZone):
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class HokkDebrisZone4(HokkMember, zones.DebrisZone):
    INDEX = 4
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class HokkDebrisZone5(HokkMember, zones.DebrisZone):
    INDEX = 5
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class HokkDebrisZone6(HokkMember, zones.DebrisZone):
    INDEX = 6
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class HokkBaseDebrisManufactoring(main_objects.DebrisManufactoring):
    ALIAS = 'deb'
    ROTATE_RANDOM = True
    ARCHETYPE = 'mplatform'
    LOADOUT = 'mplatform_ku_debris'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    AST_EXCLUSION_ZONE_SIZE = 2000
    AST_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.RADIOACTIVE_RED,
        'spacedust_maxparticles': 200,
    }


class HokkDebrisFactory1(HokkMember, HokkBaseDebrisManufactoring):
    INDEX = 1
    BASE_INDEX = 51
    ASTEROID_ZONES = [
        HokkDebrisZone1,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500


class HokkDebrisFactory2(HokkMember, HokkBaseDebrisManufactoring):
    INDEX = 2
    BASE_INDEX = 52
    ASTEROID_ZONES = [
        HokkDebrisZone2,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500


class HokkDebrisFactory3(HokkMember, HokkBaseDebrisManufactoring):
    INDEX = 3
    BASE_INDEX = 53
    ASTEROID_ZONES = [
        HokkDebrisZone3,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500


class HokkDebrisFactory4(HokkMember, HokkBaseDebrisManufactoring):
    INDEX = 4
    BASE_INDEX = 54
    ASTEROID_ZONES = [
        HokkDebrisZone4,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500


class HokkDebrisBoxReward(HokkMember, mineable.DefaultDebrisBoxRewardsGroup):
    NAME = 'ku_hkd_debrisbox'
    SOLAR = debris_box.DebrisBox
    REWARD_ITEM = 'comm_scrap_metal'
    ULTRA_REWARD_BASES = [
        HokkDebrisFactory1,
        HokkDebrisFactory2,
        HokkDebrisFactory3,
        HokkDebrisFactory4,
    ]


class HokkBaseDebrisBoxRewardField(mineable.DebrisBoxRewardField):
    FIELD_CLASS = mineable.MineableDebrixBoxField
    REWARDS_GROUP_CLASS = HokkDebrisBoxReward
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class HokkDebrisBoxField1(HokkMember, HokkBaseDebrisBoxRewardField):
    INDEX = 1
    ULTRA_BASE = HokkDebrisFactory1


class HokkDebrisBoxField2(HokkMember, HokkBaseDebrisBoxRewardField):
    INDEX = 2
    ULTRA_BASE = HokkDebrisFactory2


class HokkDebrisBoxField3(HokkMember, HokkBaseDebrisBoxRewardField):
    INDEX = 3
    ULTRA_BASE = HokkDebrisFactory3


class HokkDebrisBoxField4(HokkMember, HokkBaseDebrisBoxRewardField):
    INDEX = 4
    ULTRA_BASE = HokkDebrisFactory4


class HokkAsteroidDefinition1(asteroid_definition.TekagiAsteroidDefinition):
    BELT = False
    BILLBOARDS = False
    DYNAST = True
    LOOT = False  # TEMP


class HokkAsteroidZone1(HokkMember, zones.AsteroidZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = HokkAsteroidDefinition1


class HokkAbandonedAstBase1(HokkMember, main_objects.AbandonedAsteroid):
    ALIAS = 'ast'
    INDEX = 1
    BASE_INDEX = 61
    ROTATE_RANDOM = True
    ARCHETYPE = 'miningbase_mineableA'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        HokkAsteroidZone1,
    ]
    AST_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.ASTEROID,
        'spacedust_maxparticles': 200,
    }
    NEBULA_ZONES = [
        HokkBaseBarrierNebula
    ]
    EXCLUSION_PARAMS = BARRIER_EXCLUSION_PARAMS


class HokkAsteroidReward(HokkMember, mineable.AsteroidRewardsGroupUltra):
    NAME = 'ku_hkd_unlock'
    SOLAR = asteroid.AsteroidTekagi
    REWARD_ITEM = 'comm_roid_uranium'
    ULTRA_REWARD_BASES = [
        HokkAbandonedAstBase1,
    ]


class HokkMineableField(mineable.MineableAsteroidField):
    BOX_SIZE = 1400
    DENSITY_MULTIPLER = 2
    DRIFT_X = 0.3
    DRIFT_Y = 0
    DRIFT_Z = 0.3


class HokkBaseAsteroidRewardField(mineable.AsteroidRewardField):
    ALIAS = 'ast'
    FIELD_CLASS = HokkMineableField
    REWARDS_GROUP_CLASS = HokkAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class HokkRewardAsteroids1(HokkMember, HokkBaseAsteroidRewardField):
    INDEX = 1
    ULTRA_BASE = HokkAbandonedAstBase1


class HokkSun(HokkMember, main_objects.Sun):
    STAR = 'Ku01_Sun'
    LOADOUT = 'small_blue_sun_fx'


class HokkTau4Jumpgate(HokkMember, main_objects.Jumpgate):
    INDEX = 1
    REL = LEFT
    TARGET_SYSTEM_NAME = 'tau4'


class HokkOmega3Jumpgate(HokkMember, main_objects.Jumpgate):
    INDEX = 2
    REL = RIGHT
    TARGET_SYSTEM_NAME = 'ku_tgk'


class HokkOmega7Jumpgate(HokkMember, main_objects.Jumpgate):
    INDEX = 3
    REL = BOTTOM
    TARGET_SYSTEM_NAME = 'om7'


class HokkDockring(HokkMember, main_objects.LargePlanetDockring):
    BASE_INDEX = 1
    REL = TOP
    AUDIO_PREFIX = SpaceVoice.KU_PLANET
    INTERIOR_CLASS = interior.CustomFullSplitRoomInterior
    DEALERS = dealers.KusariPlanetDealers

    BASE_PROPS = meta.LargePlanet(
        objectives=[
            meta.ProduceBest(LUXURY_GOLD),
            meta.ProduceBest(OPTICAL_CHIPS),
            meta.ProduceCheap(JUMPGATE_PARTS),
            meta.ProduceCheap(GREENHOUSE_PARTS),
            meta.ProduceNormal(SMELTER_PARTS),
            meta.ProduceBad(AMMUNITION),
        ]
    )


class HokkMegaShipyard(HokkMember, main_objects.Shipyard):
    BASE_INDEX = 2
    REL = RIGHT
    REL_DRIFT = 1000
    SPACE_OBJECT_TEMPLATE = kyushu_megashipyard.KyushuMegashipyard
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.KusariCivilianDealers

    BASE_PROPS = meta.Shipyard(
        objectives=[
            meta.SupportBattleships(),
            meta.ConsumeHeavyMunitions(),
        ]
    )


class HokkRefinery(HokkMember, main_objects.Refinery):
    BASE_INDEX = 3
    REL = TOP
    SPACE_OBJECT_TEMPLATE = alg.AlgBaseHokkaido
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.KusariCivilianDealers
    FACTION = faction.KC_GRP

    BASE_PROPS = meta.Refinery(
        objectives=[
            meta.ProduceBest(ALLOY_CONDUCTOR),
            meta.ProduceBad(ALLOY_RADIATION),
        ]
    )


class HokkPolice(HokkMember, main_objects.Outpost):
    ALIAS = 'police'
    BASE_INDEX = 4
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = police.SigmaEightPoliceOutpost
    INTERIOR_CLASS = interior.OutpostShipdealerInterior
    AUDIO_PREFIX = SpaceVoice.BORDER_STATION
    DEALERS = dealers.KusariMilitaryDealers


class HokkStation(HokkMember, main_objects.TradelaneSupportStation):
    BASE_INDEX = 5
    REL = BOTTOM

    ARCHETYPE = 'largestation1_old'
    LOADOUT = 'largestation_ku'

    AUDIO_PREFIX = SpaceVoice.STATION
    INTERIOR_CLASS = interior.StationShipdealerInterior
    DEALERS = dealers.KusariCivilianDealers


class HokkTrading(HokkMember, main_objects.TradingBase):
    BASE_INDEX = 6
    REL = LEFT

    SPACE_OBJECT_TEMPLATE = trade_storages.ManhattanStorage

    INTERIOR_CLASS = interior.OutpostInterior
    DEALERS = dealers.KusariCivilianDealers


class HokkPlanet1(HokkMember, main_objects.Planet):
    ARCHETYPE = 'planet_watdrkcld_4000'
    SPHERE_RADIUS = 4000
    RELATED_DOCK_RING = HokkDockring


class HokkPlanet2(HokkMember, main_objects.Planet):
    INDEX = 2
    ARCHETYPE = 'planet_gasyelcld_3000'
    SPHERE_RADIUS = 3000


class HokkPlanet3(HokkMember, main_objects.Planet):
    INDEX = 3
    ARCHETYPE = 'planet_icemoon_2500'
    SPHERE_RADIUS = 2500


class HokkOldReserachRuins(HokkMember, main_objects.StationRuins):
    ALIAS = 'ruins'
    INDEX = 1
    REL = LEFT

    SPACE_OBJECT_TEMPLATE = gmg_hq.GmgHQDestroyed
    ASTEROID_ZONES = [
        HokkDebrisZone6,
    ]


class HokkOldReserachRuinsSuprisePoint1(HokkMember, main_objects.HackableStation):
    ALIAS = 'ruins_dock'
    INDEX = 1
    BASE_INDEX = 71
    RELATED_OBJECT = HokkOldReserachRuins
    RELATED_OBJECT_INDEX = 0
    HACKABLE_SOLAR_CLASS = hackable.HackableOutpostRot90
    INTERIOR_CLASS = interior.EquipDeckInterior


class HokkOldReserachRuinsSuprisePoint2(HokkMember, main_objects.HackableStation):
    ALIAS = 'ruins_dock'
    INDEX = 2
    BASE_INDEX = 72
    RELATED_OBJECT = HokkOldReserachRuins
    RELATED_OBJECT_INDEX = 1
    HACKABLE_SOLAR_CLASS = hackable.HackableOutpostRot90
    INTERIOR_CLASS = interior.EquipDeckInterior


class HokkNebulaPirates(HokkMember, main_objects.PirateStation):
    BASE_INDEX = 7
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = pirate.PirateBaseCalifornia
    FACTION = faction.KX_GRP

    DEFENCE_LEVEL = None

    INTERIOR_BG1 = interior.INTERIOR_BG_WALKER

    AUDIO_PREFIX = SpaceVoice.OUTPOST
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.KusariPirateDealers


class HokkJunkers(HokkMember, main_objects.JunkerBase):
    ALIAS = 'junker'
    BASE_INDEX = 8
    REL = TOP
    SPACE_OBJECT_TEMPLATE = junker.BerlinJunker
    FACTION = faction.JUNK_GRP

    DEFENCE_LEVEL = None

    AUDIO_PREFIX = SpaceVoice.OUTPOST
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.KusariPirateDealers

    ASTEROID_ZONES = [
        HokkDebrisZone5,
    ]


class HokkTradingConn1(HokkMember, main_objects.TradeConnection):
    OBJ_FROM = HokkTau4Jumpgate
    OBJ_TO = HokkTrading
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = BOTTOM


class HokkTradingConn2(HokkMember, main_objects.TradeConnection):
    OBJ_FROM = HokkTrading
    OBJ_TO = HokkDockring
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'B'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        HokkNebulaPirates
    ]


class HokkTradingConn3(HokkMember, main_objects.TradeConnection):
    OBJ_FROM = HokkStation
    OBJ_TO = HokkTrading
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        HokkNebulaPirates
    ]


class HokkRefineryConn1(HokkMember, main_objects.TradeConnection):
    OBJ_FROM = HokkDockring
    OBJ_TO = HokkRefinery
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        HokkJunkers
    ]


class HokkRefineryConn2(HokkMember, main_objects.TradeConnection):
    OBJ_FROM = HokkRefinery
    OBJ_TO = HokkMegaShipyard
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        HokkJunkers
    ]

    OBJ_FROM_TLR_FORCE_OFFSET = (24000, 0, -38000)


class HokkRefineryConn3(HokkMember, main_objects.TradeConnection):
    OBJ_FROM = HokkOmega3Jumpgate
    OBJ_TO = HokkRefinery
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        HokkJunkers
    ]


class HokkPoliceConn1(HokkMember, main_objects.TradeConnection):
    OBJ_FROM = HokkMegaShipyard
    OBJ_TO = HokkPolice
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'F'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        HokkJunkers
    ]


class HokkPoliceConn2(HokkMember, main_objects.TradeConnection):
    OBJ_FROM = HokkPolice
    OBJ_TO = HokkOmega7Jumpgate
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'G'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        HokkNebulaPirates
    ]


class HokkPoliceConn3(HokkMember, main_objects.TradeConnection):
    OBJ_FROM = HokkStation
    OBJ_TO = HokkPolice
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'H'
    HUNTER_DEFENCE_REL = BOTTOM
    ATTACKED_BY = [
        HokkNebulaPirates
    ]


class HokkRuinsConn1(HokkMember, main_objects.BrokenTradeConnection):
    OBJ_FROM = HokkRefinery
    OBJ_TO = HokkOldReserachRuins
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'I'

    OBJ_FROM_TLR_FORCE_OFFSET = (22000, 0, -35000)


class HokkRuinsConn2(HokkMember, main_objects.BrokenTradeConnection):
    OBJ_FROM = HokkOldReserachRuins
    OBJ_TO = HokkPolice
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'J'


class HokkRuinsConn3(HokkMember, main_objects.BrokenTradeConnection):
    OBJ_FROM = HokkOldReserachRuins
    OBJ_TO = HokkMegaShipyard
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'K'
