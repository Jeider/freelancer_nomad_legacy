from fx.space import Dust, JumpholeEffect
from fx.sound import Ambience
from universe.audio.space_voice import SpaceVoice, SpaceCostume

from managers.tools import query as Q
from world.names import *
from universe.content import meta

from universe import markets

from universe.content.member import Member
from universe.content.system_object import LEFT, RIGHT, TOP, BOTTOM
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
from templates.dockable import nomad_babylon
from templates.dockable import edge_world

from text.strings import MultiString as MS


class MadMember(Member):
    FACTION = faction.Corsairs
    INTERIOR_BG1 = interior.INTERIOR_CO_MADRID
    INTERIOR_BG2 = interior.INTERIOR_STARS
    WEAPON_FACTION = WEAPON_BW
    EQUIP_FACTION = EQUIP_BW
    AST_TYPE = 'li_cal'
    REL_APPEND = 4000


class MadStaticText(MadMember, main_objects.RawText):
    SPACE_CONTENT = '''[SystemInfo]
name = co_mad
space_color = 5, 5, 5
local_faction = co_grp
space_farclip = 80000

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Dust]
spacedust = Dust

[Music]
space = music_omega_space
danger = music_omega_danger
battle = music_omega_battle

[Ambient]
color = 10, 25, 40

[Background]
nebulae = solar\\stars_mod\\co_mad_nebula.cmp
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[zone]
nickname = zone_co_mad_system_status
pos = 0, 0, 0
shape = SPHERE
size = 100000
property_flags = 512 ;lava - MILITARY
;property_flags = 256 ;ice - TRADING
;property_flags = 2048 ;crystal - GASMINING

[LightSource]
nickname = Co_Mad_System_Light
pos = 0, 0, 0
color = 232, 80, 0
range = 100000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION
'''


class MadSun(MadMember, main_objects.Sun):
    STAR = 'sm_red_sun'
    LOADOUT = 'big_red_sun_fx'


class MadLargeStation(MadMember, main_objects.Station):
    ALIAS = 'station'
    INDEX = 1
    BASE_INDEX = 2
    REL = LEFT
    SPACE_OBJECT_TEMPLATE = nomad_babylon.BabylonShippingDock
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.KusariPirateDealers
    CALC_STORE = False
    HAVE_CHARACTERS = False
    EQUIP_SET = markets.StationSet
    BASE_PROPS = meta.PirateStation()
    DEFENCE_LEVEL = None

    RU_NAME = MS('Станция Валенсия', "Valensia Station")


class MadRingStation(MadMember, main_objects.Station):
    ALIAS = 'station'
    INDEX = 2
    BASE_INDEX = 3
    REL = TOP
    SPACE_OBJECT_TEMPLATE = edge_world.MadridProduction
    INTERIOR_CLASS = interior.StationInterior
    DEALERS = dealers.KusariPirateDealers
    CALC_STORE = False
    HAVE_CHARACTERS = False
    EQUIP_SET = markets.StationSet
    BASE_PROPS = meta.PirateStation()
    DEFENCE_LEVEL = None

    RU_NAME = MS('Станция Морелия', "Morelia Station")


class MadDockring(MadMember, main_objects.LargePlanetDockring):
    BASE_INDEX = 1
    REL = BOTTOM
    AUDIO_PREFIX = SpaceVoice.CO_PLANET
    INTERIOR_CLASS = interior.CustomFullSplitRoomInterior
    DEALERS = dealers.KusariPirateDealers
    SHIP_SET = markets.ShipSet('pi_fighter')
    RU_NAME = MS('Планета Мадрид', 'Planet Madrid')
    EQUIP_SET = markets.StationSet
    BASE_PROPS = meta.PirateStation()
    CALC_STORE = False
    HAVE_CHARACTERS = False
    DEFENCE_LEVEL = None

    # BASE_PROPS = meta.LargePlanet(
    #     objectives=[
    #         meta.ProduceBest(LUXURY_FOOD),
    #         meta.ProduceBest(MOX_FUEL),
    #         meta.ProduceCheap(POLYMERS),
    #         meta.ProduceNormal(SOLAR_PLANT_PARTS),
    #         meta.ProduceNormal(OPTICAL_CHIPS),
    #         meta.ProduceBad(PROD_MACHINES),
    #         meta.ProduceBad(WATER_EXTRA),
    #     ]
    # )



class MadHunterAstBase(MadMember, main_objects.PirateAsteroid):
    ALIAS = 'astbase'
    INDEX = 1
    BASE_INDEX = 4
    ARCHETYPE = 'li_cal_base_large01'
    LOADOUT = 'co_base_rock_large01_pi_01'
    INTERIOR_CLASS = interior.CustomFullSplitRoomInterior
    DEFENCE_LEVEL = None
    RU_NAME = MS('База Крит', "Crete Base")
    SHIP_SET = markets.ShipSet('co_fighter')
    CALC_STORE = False
    HAVE_CHARACTERS = False
    DEALERS = dealers.KusariPirateDealers
    FACTION = faction.WorkaroundHunter

    # AST_EXCLUSION_ZONE_SIZE = 3500
    # ASTEROID_ZONES = [
    #     Om11AsteroidDynZone1,
    #     Om11AsteroidLargeZone1,
    # ]
    EQUIP_SET = markets.EquipSet(
        Q.Gun('bw_corsairgun', eq_classes=markets.SECRET3),
    )


class MadPlanet1(MadMember, main_objects.Planet):
    INDEX = 1
    ARCHETYPE = 'planet_rckbrn_3000'
    SPHERE_RADIUS = 3000
    RELATED_DOCK_RING = MadDockring


class MadPlanet2(MadMember, main_objects.Planet):
    INDEX = 2
    ARCHETYPE = 'planet_ice_blue_800'
    SPHERE_RADIUS = 800
    PLANET_CIRCLE = False
    RU_NAME = MS('Планета Менорка', 'Planet Menorka')


class MadPlanet3(MadMember, main_objects.Planet):
    INDEX = 3
    ARCHETYPE = 'planet_rckdes_3000'
    SPHERE_RADIUS = 3000
    RU_NAME = MS('Планета Альхесирас', "Planet Algeciras")


class MadPlanet4(MadMember, main_objects.Planet):
    INDEX = 4
    ARCHETYPE = 'planet_gasorgcld_5000'
    SPHERE_RADIUS = 5000
    RING = True
    RING_ZONE_ALIAS = 'ring'
    RING_ZONE_INDEX = 1
    RING_FILE_NAME = 'lava_beta'
    RU_NAME = MS('Планета Кордова', "Planet Cordoba")


class MadUpsilonMajorJumpgate(MadMember, main_objects.Jumpgate):
    INDEX = 1
    REL = LEFT
    TARGET_SYSTEM_NAME = 'upsilon1'


class MadOmega11Jumpgate(MadMember, main_objects.Jumpgate):
    INDEX = 2
    REL = RIGHT
    TARGET_SYSTEM_NAME = 'om11'


class MadStationConn1(MadMember, main_objects.LargeTradeConnection):
    OBJ_FROM = MadUpsilonMajorJumpgate
    OBJ_TO = MadLargeStation
    SIDE_FROM = LEFT
    SIDE_TO = RIGHT
    TRADELANE_LETTER = 'A'
    # HUNTER_DEFENCE_REL = TOP


class MadStationConn2(MadMember, main_objects.LargeTradeConnection):
    OBJ_FROM = MadRingStation
    OBJ_TO = MadLargeStation
    SIDE_FROM = TOP
    SIDE_TO = BOTTOM
    TRADELANE_LETTER = 'B'
    # HUNTER_DEFENCE_REL = RIGHT
    # ATTACKED_BY = [
    #     MadHunterAstBase,
    # ]


class MadStationConn3(MadMember, main_objects.LargeTradeConnection):
    OBJ_FROM = MadDockring
    OBJ_TO = MadLargeStation
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'C'
    # HUNTER_DEFENCE_REL = TOP


class MadPlanetConn1(MadMember, main_objects.LargeTradeConnection):
    OBJ_FROM = MadOmega11Jumpgate
    OBJ_TO = MadDockring
    SIDE_FROM = RIGHT
    SIDE_TO = LEFT
    TRADELANE_LETTER = 'D'
    # HUNTER_DEFENCE_REL = TOP
    # ATTACKED_BY = [
    #     MadHunterAstBase,
    # ]
