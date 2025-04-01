from fx.space import Dust, JumpholeEffect
from fx.sound import Ambience

from universe.content.member import Member
from universe.content.system_object import LEFT, RIGHT
from universe.content import main_objects
from universe.content import zones
from universe import faction
from templates.nebula import rh_biz_nebula
from templates.nebula import rh_mnh_blue_nebula
from templates.nebula import exclusion
from templates.dockable import terraforming
from templates.dockable import valensia


class OrdHQMember(Member):
    FACTION = faction.LibertyMain

