from fx.space import Dust, JumpholeEffect
from fx.sound import Ambience
import fx.neuralnet as nn

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
from templates.solar import debris_box
from templates.nebula import rh_biz_nebula
from templates.nebula import exclusion

from templates.dockable import pirate
from templates.dockable import astbase
from templates.dockable import constanta
from templates.dockable import shipyards
from templates.dockable import alg
from templates.dockable import research
from templates.dockable import rheinland_military


class BizmarkMember(Member):
    FACTION = faction.RheinlandMain
    WEAPON_FACTION = WEAPON_RH
    EQUIP_FACTION = EQUIP_RH


class BizmarkStaticText(BizmarkMember, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = rh_biz
space_color = 10, 6, 0
local_faction = rh_grp
space_farclip = 75000

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Dust]
spacedust = Dust

[Music]
space = music_rh_space
danger = music_rh_danger
battle = music_rh_battle

[Ambient]
color = 10, 6, 0

[LightSource]
nickname = Bizmark_Sys_Light
pos = 0, 0, 0
color = 200, 200, 255
range = 200000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION

[zone]
nickname = zone_rh_biz_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
property_flags = 512 ;lava - MILITARY
;property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[Background]
complex_stars = solar\\stars_mod\\new_generic.cmp
nebulae = solar\\stars_mod\\rh_biz_nebula.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp
'''


class BizmarkAsteroidDefinition(asteroid_definition.Omega15NiobiumAsteroidDefinition):
    ABSTRACT = True
    NAME = None
    DYNAST = True
    BELT = True
    BILLBOARDS = True
    LOOT = False  # TEMP


class BizmarkAsteroidZone1(BizmarkMember, zones.AsteroidZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = BizmarkAsteroidDefinition


class BizmarkAsteroidZone2(BizmarkMember, zones.AsteroidZone):
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = BizmarkAsteroidDefinition


class BizmarkDebrisZone1(BizmarkMember, zones.DebrisZone):
    INDEX = 1
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class BizmarkDebrisZone2(BizmarkMember, zones.DebrisZone):
    INDEX = 2
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class BizmarkDebrisZone3(BizmarkMember, zones.DebrisZone):
    INDEX = 3
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class BizmarkDebrisZone4(BizmarkMember, zones.DebrisZone):
    INDEX = 4
    ASTEROID_DEFINITION_CLASS = asteroid_definition.DebrisDefinition


class BizmarkTopLeftNebula(BizmarkMember, zones.NebulaZone):
    INDEX = 1
    CONTENT_TEMPLATE = rh_biz_nebula.BizmarkBrownNebulaTemplate
    SPACEDUST = Dust.ATTRACT
    SPACEDUST_MAXPARTICLES = 40
    MUSIC = Ambience.NEBULA_DMATTER


class BizmarkTopRightNebula(BizmarkMember, zones.NebulaZone):
    INDEX = 2
    CONTENT_TEMPLATE = rh_biz_nebula.BizmarkBrownNebulaTemplate
    SPACEDUST = Dust.ATTRACT
    SPACEDUST_MAXPARTICLES = 40
    MUSIC = Ambience.NEBULA_DMATTER


class Bizmark8Sun(BizmarkMember, main_objects.Sun):
    STAR = 'Ku01_sun'
    LOADOUT = 'large_blue_sun_fx'


class BizmarkSigma8Jumpgate(BizmarkMember, main_objects.Jumpgate):
    INDEX = 1
    REL = TOP
    TARGET_SYSTEM_NAME = 'sig8'


class BizmarkMunchenJumpgate(BizmarkMember, main_objects.Jumpgate):
    INDEX = 2
    REL = LEFT
    TARGET_SYSTEM_NAME = 'rh_mnh'


class BizmarkOmega15Jumpgate(BizmarkMember, main_objects.Jumpgate):
    INDEX = 3
    REL = BOTTOM
    TARGET_SYSTEM_NAME = 'om15'


BROWN_EXCLUSION_PARAMS = {
    'zone_shell': exclusion.EDGE_EXCLUSION,
    'shell_scalar': 1.1,
    'max_alpha': 0.5,
    'exclusion_tint': '150, 80, 40',
    'fog_far': 5000,
}


class BizmarkSigma8Jumphole(BizmarkMember, main_objects.Jumphole):
    REL = TOP

    TARGET_SYSTEM_NAME = 'sig8'

    LOADOUT = JumpholeEffect.LIGHT

    NEBULA_EXCLUSION_ZONE_SIZE = 2500
    EXCLUSION_PARAMS = BROWN_EXCLUSION_PARAMS
    NEBULA_ZONES = [BizmarkTopLeftNebula]


class BizmarkDockRing(BizmarkMember, main_objects.LargePlanetDockring):
    BASE_INDEX = 1
    REL = RIGHT
    AUDIO_PREFIX = SpaceVoice.RH_PLANET
    INTERIOR_CLASS = interior.CustomFullSplitRoomInterior
    DEALERS = dealers.RheinlandPlanetDealers
    SHIP_SET = markets.ShipSet('ge_fighter2', 'ge_fighter3', 'bw_freighter')
    RU_NAME = 'Планета Бисмарк'

    BASE_PROPS = meta.LargePlanet(
        objectives=[
            meta.ProduceBest(LUXURY_DIAMONDS),
            meta.ProduceBest(SMELTER_PARTS),
            meta.ProduceCheap(OPTICAL_CHIPS),
            meta.ProduceCheap(RESEARCH_EQUIP),
            meta.ProduceNormal(SOLAR_PLANT_PARTS),
            meta.ProduceBad(DEFENCE_SYSTEMS),
        ]
    )


class BizmarkTrading(BizmarkMember, main_objects.TradingBase):
    BASE_INDEX = 2
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = shipyards.HeavyBarrelShipyard

    AUDIO_PREFIX = SpaceVoice.OUTPOST
    INTERIOR_CLASS = interior.OutpostShipdealerInterior
    DEALERS = dealers.RheinlandCivilianDealers
    SHIP_SET = markets.ShipSet('rh_freighter')
    RU_NAME = 'Станция Бремен'

    BASE_PROPS = meta.LargeTradingBase(
        objectives=[
            meta.HaveGreenhouse(),
        ]
    )


class BizmarkBattleship(BizmarkMember, main_objects.RheinlandBattleship):
    BASE_INDEX = 3
    REL = LEFT

    AUDIO_PREFIX = SpaceVoice.BATTLESHIP
    INTERIOR_CLASS = interior.BattleshipInterior
    INTERIOR_EXTRA_ROOMS = ['''
;mission 02 special room
[Room]
nickname = Deck2
file = Universe\\SYSTEMS_MOD\\RH_BIZMARK\\Room\\rh_biz_03_deck2.ini
    ''']
    DEALERS = dealers.RheinlandMilitaryDealers
    SHIP_SET = markets.ShipSet('bw_fighter')
    RU_NAME = 'Линкор Шарнхорст'


class BizmarkResearch(BizmarkMember, main_objects.ResearchStation):
    ALIAS = 'research'
    INDEX = 1
    BASE_INDEX = 4
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = research.RheinlandResearch
    RU_NAME = 'Исследовательская станция Мюнстер'

    AUDIO_PREFIX = SpaceVoice.STATION
    INTERIOR_CLASS = interior.StationBshbarInterior
    DEALERS = dealers.RheinlandCivilianDealers

    BASE_PROPS = meta.Research()


class BizmarkMilitary(BizmarkMember, main_objects.Station):
    ALIAS = 'military'
    BASE_INDEX = 5
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = rheinland_military.RheinlandMilitary

    RU_NAME = 'Станция Кёльн'

    LOCKED_DOCK = True
    KEY_COLLECT_FX = nn.FX_GOT_KEY_STATION

    AUDIO_PREFIX = SpaceVoice.STATION
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.RheinlandMilitaryDealers

    BASE_PROPS = meta.MediumStation(
        objectives=[
            meta.SupportBattleships(),
            meta.ConsumeHeavyMunitions(),
        ]
    )
    CALC_STORE = False


class BizmarkShipyard(BizmarkMember, main_objects.Shipyard):
    BASE_INDEX = 6
    REL = TOP
    REL_DRIFT = 1000
    SPACE_OBJECT_TEMPLATE = constanta.Constanta
    RU_NAME = 'Верфь Киль'

    AUDIO_PREFIX = SpaceVoice.SHIPYARD
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.RheinlandCivilianDealers


class BizmarkRefinery(BizmarkMember, main_objects.Refinery):
    BASE_INDEX = 7
    REL = BOTTOM
    SPACE_OBJECT_TEMPLATE = alg.AlgBaseBerlin
    RU_NAME = 'Станция Дортмунд'

    AUDIO_PREFIX = SpaceVoice.FACTORY
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.RheinlandCivilianDealers

    ASTEROID_ZONES = [
        BizmarkDebrisZone4,
    ]


class BizmarkTopPirate(BizmarkMember, main_objects.PirateStation):
    BASE_INDEX = 8
    INDEX = 1
    REL = TOP
    SPACE_OBJECT_TEMPLATE = pirate.PirateBaseCalifornia
    FACTION = faction.RheinlandPirate

    DEFENCE_LEVEL = None
    RU_NAME = 'База Майнц'

    AUDIO_PREFIX = SpaceVoice.OUTPOST
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.RheinlandPirateDealers


class BizmarkRightPirate(BizmarkMember, main_objects.PirateAsteroid):
    BASE_INDEX = 9
    INDEX = 2
    REL = RIGHT
    SPACE_OBJECT_TEMPLATE = astbase.BizmarkAsteroidBase
    FACTION = faction.RheinlandPirate

    DEFENCE_LEVEL = None
    RU_NAME = 'База Саарбрюкен'

    AUDIO_PREFIX = SpaceVoice.OUTPOST
    INTERIOR_CLASS = interior.PirateOutpostInterior
    DEALERS = dealers.RheinlandPirateDealers
    ASTEROID_ZONES = [
        BizmarkAsteroidZone1,
    ]


class BizmarkBaseDebrisManufactoring(main_objects.DebrisManufactoring):
    ALIAS = 'deb'
    ROTATE_RANDOM = True
    ARCHETYPE = 'mplatform'
    LOADOUT = 'mplatform_rh_debris'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    INTERIOR_BG1 = interior.INTERIOR_RH_BIZMARK
    AST_EXCLUSION_ZONE_SIZE = 2000
    AST_EXCLUSION_ZONE_PARAMS = {
        'spacedust': Dust.RADIOACTIVE_RED,
        'spacedust_maxparticles': 200,
    }


class BizmarkAbandonedAstBase1(BizmarkMember, main_objects.AbandonedAsteroid):
    ALIAS = 'ast'
    INDEX = 2
    BASE_INDEX = 61
    ROTATE_RANDOM = True
    ARCHETYPE = 'miningbase_mineableA'
    INTERIOR_CLASS = interior.EquipDeckInterior
    DEFENCE_LEVEL = None
    LOCKED_DOCK = True

    RU_NAME = 'База Эссен'

    INTERIOR_BG1 = interior.INTERIOR_RH_BIZMARK
    AST_EXCLUSION_ZONE_SIZE = 3500
    ASTEROID_ZONES = [
        BizmarkAsteroidZone2,
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


class BizmarkDebrisFactory1(BizmarkMember, BizmarkBaseDebrisManufactoring):
    INDEX = 1
    BASE_INDEX = 51
    ASTEROID_ZONES = [
        BizmarkDebrisZone1,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500
    RU_NAME = 'База Вадерн'
    MISC_EQUIP_TYPE = RH_MAIN
    EQUIP_SET = markets.EquipSet(
        Q.Thruster(RH_CIV, eq_classes=markets.SECRET3),
        Q.Power(RH_PIRATE, eq_classes=markets.SECRET2),
    )


class BizmarkDebrisFactory2(BizmarkMember, BizmarkBaseDebrisManufactoring):
    INDEX = 2
    BASE_INDEX = 52
    ASTEROID_ZONES = [
        BizmarkDebrisZone2,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500
    RU_NAME = 'База Марпингер'
    MISC_EQUIP_TYPE = RH_MAIN
    EQUIP_SET = markets.EquipSet(
        Q.Thruster(RH_CIV, eq_classes=markets.SECRET2),
        Q.Power(RH_PIRATE, eq_classes=markets.SECRET3),
    )


class BizmarkDebrisFactory3(BizmarkMember, BizmarkBaseDebrisManufactoring):
    INDEX = 3
    BASE_INDEX = 53
    ASTEROID_ZONES = [
        BizmarkDebrisZone3,
    ]
    AST_EXCLUSION_ZONE_SIZE = 3500
    RU_NAME = 'База Герсхайм'
    MISC_EQUIP_TYPE = RH_MAIN
    EQUIP_SET = markets.EquipSet(
        Q.Thruster(RH_PIRATE, eq_classes=markets.SECRET2),
        Q.Power(RH_MAIN, eq_classes=markets.SECRET2),
    )


class BizmarkPirateAsteroidReward(BizmarkMember, mineable.AsteroidRewardsGroupUltra):
    NAME = 'rh_biz_rock'
    SOLAR = asteroid.AsteroidOmega15
    REWARD_ITEM = 'comm_roid_niobium'
    ULTRA_REWARD_BASES = [
        BizmarkAbandonedAstBase1,
    ]


class BizmarkDebrisBoxReward(BizmarkMember, mineable.DefaultDebrisBoxRewardsGroup):
    NAME = 'rh_biz_debrisbox'
    SOLAR = debris_box.DebrisBox
    REWARD_ITEM = 'comm_scrap_metal'
    ULTRA_REWARD_BASES = [
        BizmarkDebrisFactory1,
        BizmarkDebrisFactory2,
        BizmarkDebrisFactory3,
    ]


class BizmarkPirateAsteroids(BizmarkMember, mineable.AsteroidRewardField):
    INDEX = 1
    FIELD_CLASS = mineable.BackgroundAsteroidsField
    REWARDS_GROUP_CLASS = BizmarkPirateAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25


class BizmarkAbandonedAsteroids1(BizmarkMember, mineable.AsteroidRewardField):
    INDEX = 2
    FIELD_CLASS = mineable.MineableAsteroidField
    REWARDS_GROUP_CLASS = BizmarkPirateAsteroidReward
    MEDIUM_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True
    ULTRA_BASE = BizmarkAbandonedAstBase1


class BizmarkBaseDebrisBoxRewardField(mineable.DebrisBoxRewardField):
    FIELD_CLASS = mineable.MineableDebrixBoxField
    REWARDS_GROUP_CLASS = BizmarkDebrisBoxReward
    MEDIUM_REWARD_CHANCE = 0.5
    HIGH_REWARD_CHANCE = 0.25
    ULTRA_REWARD = True


class BizmarkDebrisBoxField1(BizmarkMember, BizmarkBaseDebrisBoxRewardField):
    INDEX = 1
    ULTRA_BASE = BizmarkDebrisFactory1


class BizmarkDebrisBoxField2(BizmarkMember, BizmarkBaseDebrisBoxRewardField):
    INDEX = 2
    ULTRA_BASE = BizmarkDebrisFactory2


class BizmarkDebrisBoxField3(BizmarkMember, BizmarkBaseDebrisBoxRewardField):
    INDEX = 3
    ULTRA_BASE = BizmarkDebrisFactory3


class BizmarkPlanet1(BizmarkMember, main_objects.Planet):
    ARCHETYPE = 'planet_earthsnwcld_3000'
    SPHERE_RADIUS = 3000
    RELATED_DOCK_RING = BizmarkDockRing


class BizmarkPlanet2(BizmarkMember, main_objects.Planet):
    INDEX = 2
    ARCHETYPE = 'planet_desored_2000'
    SPHERE_RADIUS = 2000
    RU_NAME = 'Планета Саксония'


class BizmarkPlanet3(BizmarkMember, main_objects.Planet):
    INDEX = 3
    ARCHETYPE = 'planet_ice_purple_5000'
    SPHERE_RADIUS = 5000
    RU_NAME = 'Планета Померания'


class BizmarkPlanet4(BizmarkMember, main_objects.Planet):
    INDEX = 4
    ARCHETYPE = 'planet_gasgrncld_3000'
    SPHERE_RADIUS = 3000
    RING = True
    RING_ZONE_ALIAS = 'ring'
    RING_ZONE_INDEX = 1
    RING_FILE_NAME = 'bizmark'
    RU_NAME = 'Планета Лейденшафт'


class BizmarkConnPlanet1(BizmarkMember, main_objects.TradeConnection):
    OBJ_FROM = BizmarkDockRing
    OBJ_TO = BizmarkSigma8Jumpgate
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'A'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        BizmarkRightPirate,
    ]


class BizmarkConnPlanet2(BizmarkMember, main_objects.TradeConnection):
    OBJ_FROM = BizmarkDockRing
    OBJ_TO = BizmarkTrading
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'B'


class BizmarkConnPlanet3(BizmarkMember, main_objects.TradeConnection):
    OBJ_FROM = BizmarkDockRing
    OBJ_TO = BizmarkBattleship
    OBJ_FROM_TLR_FORCE_OFFSET = (38000, 0, -7000)
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'C'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        BizmarkRightPirate,
    ]


class BizmarkConnPlanet4(BizmarkMember, main_objects.TradeConnection):
    OBJ_FROM = BizmarkDockRing
    OBJ_TO = BizmarkResearch
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'D'
    HUNTER_DEFENCE_REL = RIGHT
    ATTACKED_BY = [
        BizmarkRightPirate,
    ]


class BizmarkConnTrading1(BizmarkMember, main_objects.TradeConnection):
    OBJ_FROM = BizmarkTrading
    OBJ_TO = BizmarkMunchenJumpgate
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'E'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        BizmarkTopPirate,
    ]


class BizmarkConnBattleship1(BizmarkMember, main_objects.TradeConnection):
    OBJ_FROM = BizmarkBattleship
    OBJ_TO = BizmarkOmega15Jumpgate
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'F'
    HUNTER_DEFENCE_REL = RIGHT


class BizmarkConnBattleship2(BizmarkMember, main_objects.TradeConnection):
    OBJ_FROM = BizmarkBattleship
    OBJ_TO = BizmarkResearch
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'G'
    HUNTER_DEFENCE_REL = TOP
    ATTACKED_BY = [
        BizmarkRightPirate,
    ]


class BizmarkConnShipyard1(BizmarkMember, main_objects.TradeConnection):
    OBJ_FROM = BizmarkShipyard
    OBJ_TO = BizmarkMunchenJumpgate
    SIDE_FROM = BOTTOM
    SIDE_TO = TOP
    TRADELANE_LETTER = 'H'
    HUNTER_DEFENCE_REL = LEFT
    ATTACKED_BY = [
        BizmarkTopPirate,
    ]


class BizmarkConnShipyard2(BizmarkMember, main_objects.TradeConnection):
    OBJ_FROM = BizmarkShipyard
    OBJ_TO = BizmarkRefinery
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'I'
    HUNTER_DEFENCE_REL = LEFT


class BizmarkConnShipyard3(BizmarkMember, main_objects.TradeConnection):
    OBJ_FROM = BizmarkShipyard
    OBJ_TO = BizmarkBattleship
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'J'
