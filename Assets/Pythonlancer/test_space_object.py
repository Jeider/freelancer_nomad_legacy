from templates.space_object_template import SpaceObjectTemplate

# XLARGE

# from templates.space_objects.tekagi_megabase import TekagiMegabase
# from templates.space_objects.nomad_babylon import Babylon
# from templates.space_objects.nomad_asf_hq import AsfHQ
# from templates.space_objects.megacannon import MegaCannon
# from templates.space_objects.kusari_palace import KusariPalace
# from templates.space_objects.odissey import Odissey
# from templates.space_objects.potsdam import Potsdam
# from templates.space_objects.manhattan_megabase import ManhattanMegabase
# from templates.space_objects.valensia import ValensiaOutside
# from templates.space_objects.terraforming import Terraforming
# from templates.space_objects.gavana import Gavana
# from templates.space_objects.ulster_megabase import UlsterMegabase
# from templates.space_objects.sphere_megabase import SphereMegabase, SphereMegabaseShort

# LARGE

# from templates.space_objects.cloakgen import Cloakgen
# from templates.space_objects.avalon_megabase import AvalonMegabase
# from templates.space_objects.cambridge_research import CambridgeResearch
# from templates.space_objects.olaf import Olaf
# from templates.space_objects.honshu_military import HonshuMilitary
# from templates.space_objects.kyushu_megashipyard import KyushuMegashipyard
# from templates.space_objects.constanta import Constanta
# from templates.space_objects.stuttgart_megabase import StuttgartMegabase
# from templates.space_objects.rheinland_military import RheinlandMilitary
# from templates.space_objects.tortuga import Tortuga
# from templates.space_objects.corsair_dreadnought import CorsairDreadnoughtDestroyed, CorsairDreadnoughtAlive
# from templates.space_objects.forbes_megafactory import ForbesMegafactory
# from templates.space_objects.columbia_production import ColumbiaProduction
# from templates.space_objects.liberty_military import LibertyMilitary
# from templates.space_objects.california_tradestation import CaliforniaTradestation

# DEFAULT

# from templates.space_objects.edge_world import BlackHoleResearch, BlackHoleOutpost, BlackHoleDestroyedStation, ShinobiAbandonedResearch, OchoRiosResearch, MadridProduction, CadizFreeport
# from templates.space_objects.bounty_hunter import PortRoyal, ChurchAlive, ChurchDestroyed
# from templates.space_objects.gmg_hq import GmgHQAlive, GmgHQDestroyed
# from templates.space_objects.alg import AlgBaseHokkaido, AlgBaseBerlin
# from templates.space_objects.pirate import PirateBaseBizmark, PirateBaseHokkaido, LibertyRombicPirateBase, PirateBaseStuttgart, PirateBaseCambridge, ManhattanPirateBase, PirateBaseForbes, PirateBaseColumbia, PirateBaseCalifornia
# from templates.space_objects.prisons import AvalonPrison, HonshuPrison, BerlinPrison, AlaskaPrison, ColumbiaPrison
# from templates.space_objects.shipyards import CambridgeShipyard, HokkaidoShipyard, StuttgartShipyard, ForbesShipyard, UlsterShipyardDestroyed, UlsterShipyardAlive, HeavyBarrelShipyard
# from templates.space_objects.trade_storages import HokkaidoStorage, HonshuStorage, TekagiStorage, LibertyLongStorage, RheinlandOmegaStorage, ManhattanStorage
# from templates.space_objects.junker import HonshuJunker, SigmaEightJunker, StuttgartJunker, BerlinJunker, OmegaSmelter, ForbesJunker
# from templates.space_objects.roid_mining import BretoniaRoidMining, RheinlandRoidMining, LibertyRoidMining
# from templates.space_objects.research import KyushuResearch, SiriusResearch, RheinlandResearch, ForbesResearch
# from templates.space_objects.asteroid import KyushuAsteroidBase, NomadAsteroidBase, MunchenAsteroidBase, BizmarkAsteroidBase, BerlinAsteroidBase, ManhattanAsteroidBase, CaliforniaAsteroidBase
# from templates.space_objects.gas_miner import BretoniaPirateGasMiner, BretoniaCivilianGasMiner, RheinlandCivilianGasMiner, RheinlandPirateGasMiner, CadizGasMiner
# from templates.space_objects.trading_outposts import LibertyTradingOutpost, RheinlandTradingOutpost
# from templates.space_objects.police import PoliceOutpostBretonia, SigmaEightPoliceOutpost, StuttgartPoliceOutpost, BerlinPoliceOutpost, OmicronPoliceOutpost, PoliceOutpostLiberty
from templates.space_objects.station_debris import TekagiDebris, MunchenBattleStationDebris, MunchenCivilianStationDebris, OmegaDanzigDebris, StuttgartDestroyedOutpost, ForbesDebris, ColumbiaDebris, CaliforniaDebris

from text.dividers import DIVIDER


output = []
pos_x = 0
pos_y = 0
append = 2500
max_y = 20000

offset = 0
limit = 1000

index = 1
for base in SpaceObjectTemplate.subclasses:
    name = 'test_base_{index:02}'.format(index=index)
    # print((pos_x, 0, pos_y))
    output.append(
        base().get_instance(new_space_object_name=name, move_to=(pos_x, 0, pos_y))
    )

    pos_y += append
    if pos_y > max_y:
        pos_y = 0
        pos_x += append

    index += 1
    if index > limit:
        break

DEMO_CONTENT = '''
[SystemInfo]
name = demo_sys
space_color = 20, 20, 20
local_faction = br_grp
space_farclip = 4000000

[TexturePanels]
file = universe\\heavens\\shapes.ini

[Dust]
spacedust = Dust

[Music]
space = music_omicron_space
danger = music_omicron_danger
battle = music_omicron_battle

[Ambient]
color = 100, 100, 100

[Background]
complex_stars = solar\\stars_mod\\new_generic.cmp
basic_stars = solar\\stars_mod\\new_generic.cmp

[Object]
nickname = demo_jumpgate_fix
pos = 0, -50000, 0
rotate = 0, 0, 0
archetype = jumpgate

[LightSource]
nickname = Xdemo_system_light
pos = 50000, 50000, 50000
color = 255, 255, 255
range = 150000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION
'''

print(DEMO_CONTENT + DIVIDER.join(output))
