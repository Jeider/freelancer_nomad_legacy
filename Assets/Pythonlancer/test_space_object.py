import sys
import pathlib
from text.dividers import DIVIDER
from templates.space_object_template import SpaceObjectTemplate

# XLARGE

from templates.combined.tekagi_megabase import TekagiMegabase
from templates.combined.kusari_palace import KusariPalace
from templates.combined.nomad_asf_hq import AsfHQ




# from templates.combined.nomad_babylon import Babylon
# from templates.combined.sphere_megabase import SphereMegabase, SphereMegabaseShort

# from templates.combined.upsilon_gasinside import UpsilonMegabase, UpsilonLostResearch
# from templates.combined.ulster_megabase import UlsterMegabase




# from templates.combined.stuttgart_megabase import StuttgartMegabase

# from templates.combined.megacannon import MegaCannon
# from templates.combined.odissey import Odissey
# from templates.combined.potsdam import Potsdam
# from templates.combined.manhattan_megabase import ManhattanMegabase

# from templates.combined.gavana import Gavana
# from templates.combined.valensia import ValensiaOutside
# from templates.combined.terraforming import Terraforming

# LARGE

# from templates.combined.cloakgen import Cloakgen
# from templates.combined.avalon_megabase import AvalonMegabase
# from templates.combined.cambridge_research import CambridgeResearch
# from templates.combined.olaf import Olaf
# from templates.combined.honshu_military import HonshuMilitary
# from templates.combined.kyushu_megashipyard import KyushuMegashipyard
# from templates.combined.constanta import Constanta
# from templates.combined.rheinland_military import RheinlandMilitary
# from templates.combined.tortuga import Tortuga
# from templates.combined.corsair_dreadnought import CorsairDreadnoughtDestroyed, CorsairDreadnoughtAlive
# from templates.combined.forbes_megafactory import ForbesMegafactory
# from templates.combined.columbia_production import ColumbiaProduction
# from templates.combined.liberty_military import LibertyMilitary
# from templates.combined.california_tradestation import CaliforniaTradestation

# DEFAULT

# from templates.combined.station_debris import TekagiDebris, MunchenBattleStationDebris, MunchenCivilianStationDebris, OmegaDanzigDebris, StuttgartDestroyedOutpost, ForbesDebris, ColumbiaDebris, CaliforniaDebris
# from templates.combined.edge_world import BlackHoleResearch, BlackHoleOutpost, BlackHoleDestroyedStation, ShinobiAbandonedResearch, OchoRiosResearch, MadridProduction, CadizFreeport, NeutronResearch

# from templates.combined.bounty_hunter import PortRoyal, ChurchAlive, ChurchDestroyed
# from templates.combined.gmg_hq import GmgHQAlive, GmgHQDestroyed
# from templates.combined.alg import AlgBaseHokkaido, AlgBaseBerlin



# from templates.combined.prisons import AvalonPrison, HonshuPrison, BerlinPrison, AlaskaPrison, ColumbiaPrison
# from templates.combined.shipyards import CambridgeShipyard, HokkaidoShipyard, StuttgartShipyard, ForbesShipyard, UlsterShipyardDestroyed, UlsterShipyardAlive, HeavyBarrelShipyard

# from templates.combined.roid_mining import BretoniaRoidMining, RheinlandRoidMining, LibertyRoidMining, UpsilonRoidMining
# from templates.combined.gas_miner import BretoniaPirateGasMiner, BretoniaCivilianGasMiner, RheinlandCivilianGasMiner, RheinlandPirateGasMiner, CadizGasMiner
# from templates.combined.research import KyushuResearch, SiriusResearch, RheinlandResearch, ForbesResearch




# from templates.combined.pirate import PirateBaseBizmark, PirateBaseHokkaido, LibertyRombicPirateBase, PirateBaseStuttgart, PirateBaseCambridge, ManhattanPirateBase, PirateBaseForbes, PirateBaseColumbia, PirateBaseCalifornia
# from templates.combined.asteroid import KyushuAsteroidBase, NomadAsteroidBase, MunchenAsteroidBase, BizmarkAsteroidBase, BerlinAsteroidBase, ManhattanAsteroidBase, CaliforniaAsteroidBase
# from templates.combined.junker import HonshuJunker, SigmaEightJunker, StuttgartJunker, BerlinJunker, OmegaSmelter, ForbesJunker

# from templates.combined.trading_outposts import LibertyTradingOutpost, RheinlandTradingOutpost
# from templates.combined.police import PoliceOutpostBretonia, SigmaEightPoliceOutpost, StuttgartPoliceOutpost, BerlinPoliceOutpost, OmicronPoliceOutpost, PoliceOutpostLiberty
# from templates.combined.trade_storages import HokkaidoStorage, HonshuStorage, TekagiStorage, LibertyLongStorage, RheinlandOmegaStorage, ManhattanStorage




# base = KyushuMegashipyard().get_instance(new_space_object_name=None, move_to=(30000, 8000, 25000))

# print(base)


# sys.exit()



output = []
pos_x = 0
pos_y = 0
# append = 5000  # XLARGE
# append = 3500  # LARGE
append = 2500  # DEFAULT
max_y = 10000

offset = 0
limit = 1000


# index = 1
# demo_file_name = 'demo1.ini'
# append = 1500


# index = 100
# demo_file_name = 'demo2.ini'
# append = 2500


# index = 200
# demo_file_name = 'demo3.ini'
# append = 2500


# index = 300
# demo_file_name = 'demo4.ini'
# append = 3500
# max_y = 13000


# index = 400
# demo_file_name = 'demo5.ini'
# append = 5000


# index = 500
# demo_file_name = 'demo6.ini'
# append = 6000
# max_y = 15000


index = 600
demo_file_name = 'demo7.ini'
append = 6000
max_y = 15000




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

DEMO_CONTENT = '''[SystemInfo]
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
pos = -50000, 30000, -50000
color = 255, 255, 255
range = 150000
type = DIRECTIONAL
atten_curve = DYNAMIC_DIRECTION

'''

final_out = DEMO_CONTENT + DIVIDER.join(output)

demo_file_path = pathlib.Path().resolve().parent.parent / 'DATA' / 'UNIVERSE' / 'SPECIAL' / 'DEMO' / demo_file_name
demo_file_path.write_text(final_out, encoding='utf-8')


