from fx.contrail import Contrail
from fx.light import Light

from world.gun import *
from world.equipment import MainMiscEquip as misc
from world.npc import NPC
from world import ship


class Faction(object):
    INTERCEPTOR1 = None
    INTERCEPTOR2 = None
    ELITE1 = None
    ELITE2 = None
    ELITE3 = None

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)


class LawfulFaction(object):
    LEGALITY = 'lawful'


class UnlawfulFaction(object):
    LEGALITY = 'unlawful'


class RhenlandFleet(object):
    INTERCEPTOR1 = ship.Dagger
    INTERCEPTOR2 = ship.Banshee
    ELITE1 = ship.Stiletto
    ELITE2 = ship.Sabre
    ELITE3 = ship.Valkyrie

    SHIPS = [
        INTERCEPTOR1, INTERCEPTOR2,
        ELITE1, ELITE2,
        ELITE3
    ]


class LibertyFleet(object):
    INTERCEPTOR1 = ship.Piranha
    INTERCEPTOR2 = ship.Patriot
    ELITE1 = ship.Barracuda
    ELITE2 = ship.Hammerhead
    ELITE3 = ship.Defender

    SHIPS = [
        INTERCEPTOR1, INTERCEPTOR2,
        ELITE1, ELITE2,
        ELITE3
    ]


class CorsairFleet(object):
    INTERCEPTOR1 = ship.Bloodhound
    ELITE1 = ship.Wolfhound

    SHIPS = [
        INTERCEPTOR1, ELITE1
    ]


class BaseRheinland(object):
    SHIELD_WEAPON = RheinlandShieldgun
    CONTRAIL = Contrail.CONTRAIL_RH
    LIGHT = Light.SMALL_YELLOW


class BaseLiberty(object):
    SHIELD_WEAPON = RheinlandShieldgun
    CONTRAIL = Contrail.CONTRAIL_LI
    LIGHT = Light.SMALL_BLUE


class BaseCorsair(object):
    SHIELD_WEAPON = RheinlandShieldgun
    CONTRAIL = Contrail.CONTRAIL_CO
    LIGHT = Light.SMALL_PURPLE


class RheinlandMain(LawfulFaction, RhenlandFleet, BaseRheinland, Faction):
    CODE = 'rh_grp'

    WEAPON = RheinlandLightgun
    AFTERBURN = misc.RH_MAIN
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_MAIN
    POWER = misc.RH_MAIN
    SHIELD = misc.RH_MAIN


class RheinlandCivilians(LawfulFaction, RhenlandFleet, BaseRheinland, Faction):
    CODE = 'rc_grp'

    WEAPON = RheinlandCivgun
    AFTERBURN = misc.RH_CIV
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_CIV
    POWER = misc.RH_CIV
    SHIELD = misc.RH_CIV


class RheinlandHunters(LawfulFaction, RhenlandFleet, BaseRheinland, Faction):
    CODE = 'bh_grp_rh'

    WEAPON = RheinlandHuntergun
    AFTERBURN = misc.RH_MAIN
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_CIV
    POWER = misc.RH_CIV
    SHIELD = misc.RH_CIV


class RheinlandPirate(UnlawfulFaction, RhenlandFleet, BaseRheinland, Faction):
    CODE = 'pi_grp_rh'

    WEAPON = RheinlandPirategun
    AFTERBURN = misc.RH_PIRATE
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_PIRATE
    POWER = misc.RH_PIRATE
    SHIELD = misc.RH_PIRATE


class Hessians(UnlawfulFaction, RhenlandFleet, BaseRheinland, Faction):
    CODE = 'rx_grp'

    WEAPON = RheinlandHessiangun
    AFTERBURN = misc.RH_PIRATE
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_PIRATE
    POWER = misc.RH_PIRATE
    SHIELD = misc.RH_PIRATE


class Junkers(UnlawfulFaction, RhenlandFleet, BaseRheinland, Faction):
    CODE = 'junk_grp'

    WEAPON = RheinlandJunkergun
    AFTERBURN = misc.RH_PIRATE
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_PIRATE
    POWER = misc.RH_PIRATE
    SHIELD = misc.RH_PIRATE



# temp
class LibertyMain(LawfulFaction, LibertyFleet, BaseLiberty, Faction):
    CODE = 'li_grp'

    WEAPON = RheinlandLightgun
    AFTERBURN = misc.LI_MAIN
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.LI_MAIN
    POWER = misc.LI_MAIN
    SHIELD = misc.LI_MAIN



# temp
class Corsairs(UnlawfulFaction, CorsairFleet, BaseCorsair, Faction):
    CODE = 'co_grp'

    WEAPON = RheinlandLightgun
    AFTERBURN = misc.CO_CORSAIR
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.CO_CORSAIR
    POWER = misc.CO_CORSAIR
    SHIELD = misc.CO_CORSAIR
