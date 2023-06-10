from fx.contrail import Contrail
from fx.light import Light

from world.gun import Gun
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


class RheinlandMain(LawfulFaction, RhenlandFleet):
    CODE = 'rh_grp'

    WEAPON = Gun.RH_LIGHTGUN
    SHIELD_WEAPON = Gun.RH_SHIELDGUN
    AFTERBURN = misc.RH_MAIN
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_MAIN
    POWER = misc.RH_MAIN
    SHIELD = misc.RH_MAIN
    CONTRAIL = Contrail.CONTRAIL_RH

    LIGHT = Light.SMALL_YELLOW


class RheinlandCivilians(LawfulFaction, RhenlandFleet):
    CODE = 'rc_grp'

    WEAPON = Gun.RH_CIVGUN
    SHIELD_WEAPON = Gun.RH_SHIELDGUN
    AFTERBURN = misc.RH_CIV
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_CIV
    POWER = misc.RH_CIV
    SHIELD = misc.RH_CIV
    CONTRAIL = Contrail.CONTRAIL_RH

    LIGHT = Light.SMALL_YELLOW


class RheinlandHunters(LawfulFaction, RhenlandFleet):
    CODE = 'bh_grp_rh'

    WEAPON = Gun.RH_HUNTERGUN
    SHIELD_WEAPON = Gun.RH_SHIELDGUN
    AFTERBURN = misc.RH_MAIN
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_CIV
    POWER = misc.RH_CIV
    SHIELD = misc.RH_CIV
    CONTRAIL = Contrail.CONTRAIL_RH

    LIGHT = Light.SMALL_YELLOW


class RheinlandPirate(UnlawfulFaction, RhenlandFleet):
    CODE = 'pi_grp_rh'

    WEAPON = Gun.RH_PIRATEGUN
    SHIELD_WEAPON = Gun.RH_SHIELDGUN
    AFTERBURN = misc.RH_PIRATE
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_PIRATE
    POWER = misc.RH_PIRATE
    SHIELD = misc.RH_PIRATE
    CONTRAIL = Contrail.CONTRAIL_RH

    LIGHT = Light.SMALL_YELLOW


class Hessians(UnlawfulFaction, RhenlandFleet):
    CODE = 'rx_grp'

    WEAPON = Gun.RH_HESSIANGUN
    SHIELD_WEAPON = Gun.RH_SHIELDGUN
    AFTERBURN = misc.RH_PIRATE
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_PIRATE
    POWER = misc.RH_PIRATE
    SHIELD = misc.RH_PIRATE
    CONTRAIL = Contrail.CONTRAIL_RH

    LIGHT = Light.SMALL_YELLOW


class Junkers(UnlawfulFaction, RhenlandFleet):
    CODE = 'junk_grp'

    WEAPON = Gun.RH_JUNKERGUN
    SHIELD_WEAPON = Gun.RH_SHIELDGUN
    AFTERBURN = misc.RH_PIRATE
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_PIRATE
    POWER = misc.RH_PIRATE
    SHIELD = misc.RH_PIRATE
    CONTRAIL = Contrail.CONTRAIL_RH

    LIGHT = Light.SMALL_YELLOW
