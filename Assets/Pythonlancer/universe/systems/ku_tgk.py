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
from templates.solar import asteroid as asteroid_solar
from templates.solar import debris_box


from templates.dockable import pirate
from templates.dockable import astbase
from templates.dockable import trade_storages
from templates.dockable import columbia_production
from templates.dockable import constanta
from templates.dockable import shipyards
from templates.dockable import alg
from templates.dockable import research
from templates.dockable import rheinland_military


class TekagiMember(object):
    INDEX = 1
    ABSTRACT = False
    FACTION = faction.BR_GRP

#
# class BizmarkBaseAsteroidDefinition(asteroid_definition.Omega15NiobiumAsteroidDefinition):
#     ABSTRACT = True
#     NAME = None
#     DYNAST = True
#     BELT = True
#     BILLBOARDS = True
#     LOOT = False  # TEMP
#
#
# class BizmarkAsteroidDefinition1(BizmarkBaseAsteroidDefinition):
#     ABSTRACT = False
#     NAME = 'rh_biz_pirate_astfield1'
#
#
# class BizmarkAsteroidZone1(BizmarkMember, zones.AsteroidZone):
#     INDEX = 1
#     ASTEROID_DEFINITION_CLASS = BizmarkAsteroidDefinition1
