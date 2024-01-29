from templates.space_objects.pirate import PirateBaseBizmark, PirateBaseHokkaido
from templates.space_objects.tekagi_megabase import TekagiMegabase
from templates.space_objects.nomad_babylon import Babylon
from templates.space_objects.nomad_asf_hq import AsfHQ
from templates.space_objects.prisons import AvalonPrison, HonshuPrison
from templates.space_objects.shipyards import CambridgeShipyard, HokkaidoShipyard
from templates.space_objects.trade_storages import HokkaidoStorage, HonshuStorage
from templates.space_objects.cloakgen import Cloakgen
from templates.space_objects.avalon_megabase import AvalonMegabase
from templates.space_objects.cambridge_research import CambridgeResearch
from templates.space_objects.olaf import Olaf
from templates.space_objects.megacannon import MegaCannon
from templates.space_objects.gmg_hq import GmgHQAlive, GmgHQDestroyed
from templates.space_objects.alg import AlgBaseHokkaido
from templates.space_objects.junker import HonshuJunker
from templates.space_objects.honshu_military import HonshuMilitary
from templates.space_objects.kyushu_megashipyard import KyushuMegashipyard
from templates.space_objects.research import KyushuResearch
from templates.space_objects.asteroid import KyushuAsteroidBase


base = KyushuAsteroidBase()

instance = base.get_instance(new_space_object_name=None, move_to=(-70000, -20000, 20000))

print(instance)
