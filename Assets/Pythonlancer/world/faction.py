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


class LawfulFaction(Faction):
    LEGALITY = 'lawful'


class UnlawfulFaction(Faction):
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


class BaseRheinland(object):
    SHIELD_WEAPON = RheinlandShieldgun
    CONTRAIL = Contrail.CONTRAIL_RH
    LIGHT = Light.SMALL_YELLOW


class RheinlandMain(LawfulFaction, RhenlandFleet, BaseRheinland):
    CODE = 'rh_grp'

    WEAPON = RheinlandLightgun
    AFTERBURN = misc.RH_MAIN
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_MAIN
    POWER = misc.RH_MAIN
    SHIELD = misc.RH_MAIN


class RheinlandCivilians(LawfulFaction, RhenlandFleet, BaseRheinland):
    CODE = 'rc_grp'

    WEAPON = RheinlandCivgun
    AFTERBURN = misc.RH_CIV
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_CIV
    POWER = misc.RH_CIV
    SHIELD = misc.RH_CIV


class RheinlandHunters(LawfulFaction, RhenlandFleet, BaseRheinland):
    CODE = 'bh_grp_rh'

    WEAPON = RheinlandHuntergun
    AFTERBURN = misc.RH_MAIN
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_CIV
    POWER = misc.RH_CIV
    SHIELD = misc.RH_CIV


class RheinlandPirate(UnlawfulFaction, RhenlandFleet, BaseRheinland):
    CODE = 'pi_grp_rh'

    WEAPON = RheinlandPirategun
    AFTERBURN = misc.RH_PIRATE
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_PIRATE
    POWER = misc.RH_PIRATE
    SHIELD = misc.RH_PIRATE


class Hessians(UnlawfulFaction, RhenlandFleet, BaseRheinland):
    CODE = 'rx_grp'

    WEAPON = RheinlandHessiangun
    AFTERBURN = misc.RH_PIRATE
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_PIRATE
    POWER = misc.RH_PIRATE
    SHIELD = misc.RH_PIRATE


class Junkers(UnlawfulFaction, RhenlandFleet, BaseRheinland):
    CODE = 'junk_grp'

    WEAPON = RheinlandJunkergun
    AFTERBURN = misc.RH_PIRATE
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_PIRATE
    POWER = misc.RH_PIRATE
    SHIELD = misc.RH_PIRATE
