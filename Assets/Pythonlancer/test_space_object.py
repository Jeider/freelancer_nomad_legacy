
from templates.space_objects.tekagi_megabase import TekagiMegabase
from templates.space_objects.nomad_babylon import Babylon
from templates.space_objects.nomad_asf_hq import AsfHQ
from templates.space_objects.cloakgen import Cloakgen
from templates.space_objects.avalon_megabase import AvalonMegabase
from templates.space_objects.cambridge_research import CambridgeResearch
from templates.space_objects.olaf import Olaf
from templates.space_objects.megacannon import MegaCannon
from templates.space_objects.honshu_military import HonshuMilitary
from templates.space_objects.kyushu_megashipyard import KyushuMegashipyard
from templates.space_objects.kusari_palace import KusariPalace
from templates.space_objects.odissey import Odissey
from templates.space_objects.constanta import Constanta
from templates.space_objects.stuttgart_megabase import StuttgartMegabase
from templates.space_objects.rheinland_military import RheinlandMilitary
from templates.space_objects.potsdam import Potsdam
from templates.space_objects.tortuga import Tortuga
from templates.space_objects.corsair_dreadnought import CorsairDreadnoughtDestroyed, CorsairDreadnoughtAlive
from templates.space_objects.manhattan_megabase import ManhattanMegabase
from templates.space_objects.forbes_megafactory import ForbesMegafactory

from templates.space_objects.edge_world import BlackHoleResearch, BlackHoleOutpost, BlackHoleDestroyedStation, ShinobiAbandonedResearch
from templates.space_objects.bounty_hunter import PortRoyal, ChurchAlive, ChurchDestroyed
from templates.space_objects.gmg_hq import GmgHQAlive, GmgHQDestroyed
from templates.space_objects.alg import AlgBaseHokkaido, AlgBaseBerlin
from templates.space_objects.pirate import PirateBaseBizmark, PirateBaseHokkaido, LibertyRombicPirateBase, PirateBaseStuttgart, PirateBaseCambridge, ManhattanPirateBase, PirateBaseForbes
from templates.space_objects.prisons import AvalonPrison, HonshuPrison, BerlinPrison, AlaskaPrison
from templates.space_objects.shipyards import CambridgeShipyard, HokkaidoShipyard, StuttgartShipyard, ForbesShipyard
from templates.space_objects.trade_storages import HokkaidoStorage, HonshuStorage, TekagiStorage, LibertyLongStorage, RheinlandOmegaStorage, ManhattanStorage
from templates.space_objects.junker import HonshuJunker, SigmaEightJunker, StuttgartJunker, BerlinJunker, OmegaSmelter
from templates.space_objects.roid_mining import BretoniaRoidMining, RheinlandRoidMining
from templates.space_objects.research import KyushuResearch, SiriusResearch, RheinlandResearch
from templates.space_objects.asteroid import KyushuAsteroidBase, NomadAsteroidBase, MunchenAsteroidBase, BizmarkAsteroidBase, BerlinAsteroidBase, ManhattanAsteroidBase
from templates.space_objects.gas_miner import BretoniaPirateGasMiner, BretoniaCivilianGasMiner, RheinlandCivilianGasMiner, RheinlandPirateGasMiner
from templates.space_objects.trading_outposts import LibertyTradingOutpost, RheinlandTradingOutpost
from templates.space_objects.police import PoliceOutpostBretonia, SigmaEightPoliceOutpost, StuttgartPoliceOutpost, BerlinPoliceOutpost, OmicronPoliceOutpost
from templates.space_objects.station_debris import TekagiDebris, MunchenBattleStationDebris, MunchenCivilianStationDebris, OmegaDanzigDebris, StuttgartDestroyedOutpost


base = PirateBaseForbes()

instance = base.get_instance(new_space_object_name=None, move_to=(40000, 0, -10000))

print(instance)
