from world.equipment import MainMiscEquip as misc
from world.weapon import WeaponFactory as wp
from world.npc import NPC
from world import ship


class Faction(object):
    INTERCEPTOR1 = None
    INTERCEPTOR2 = None
    ELITE1 = None
    ELITE2 = None
    ELITE3 = None

    @staticmethod
    def get_interceptor_by_level(level):




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
        RhenlandFleet.INTERCEPTOR1, RhenlandFleet.INTERCEPTOR2,
        RhenlandFleet.ELITE1, RhenlandFleet.ELITE2,
        RhenlandFleet.ELITE3
    ]





class RheinlandMain(LawfulFaction, RhenlandFleet):
    CODE = 'rh_grp'

    WEAPON = wp.RH_LIGHTGUN
    SHIELD_WEAPON = wp.RH_SHIELDGUN
    AFTERBURN = misc.RH_MAIN
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_MAIN
    POWER = misc.RH_MAIN
    SHIELD = misc.RH_MAIN

    LIGHT = 'SlowSmallYellow'


class RheinlandCivilians(LawfulFaction, RhenlandFleet):
    CODE = 'rc_grp'

    WEAPON = wp.RH_CIVGUN
    SHIELD_WEAPON = wp.RH_SHIELDGUN
    AFTERBURN = misc.RH_CIV
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_CIV
    POWER = misc.RH_CIV
    SHIELD = misc.RH_CIV

    LIGHT = 'SlowSmallYellow'


class RheinlandHunters(LawfulFaction, RhenlandFleet):
    CODE = 'bh_grp_rh'

    WEAPON = wp.RH_HUNTERGUN
    SHIELD_WEAPON = wp.RH_SHIELDGUN
    AFTERBURN = misc.RH_MAIN
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_CIV
    POWER = misc.RH_CIV
    SHIELD = misc.RH_CIV

    LIGHT = 'SlowSmallYellow'


class RheinlandPirate(UnlawfulFaction, RhenlandFleet):
    CODE = 'pi_grp_rh'

    WEAPON = wp.RH_PIRATEGUN
    SHIELD_WEAPON = wp.RH_SHIELDGUN
    AFTERBURN = misc.RH_PIRATE
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_PIRATE
    POWER = misc.RH_PIRATE
    SHIELD = misc.RH_PIRATE

    LIGHT = 'SlowSmallYellow'


class Hessians(UnlawfulFaction, RhenlandFleet):
    CODE = 'rx_grp'

    WEAPON = wp.RH_HESSIANGUN
    SHIELD_WEAPON = wp.RH_SHIELDGUN
    AFTERBURN = misc.RH_PIRATE
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_PIRATE
    POWER = misc.RH_PIRATE
    SHIELD = misc.RH_PIRATE

    LIGHT = 'SlowSmallYellow'


class Junkers(UnlawfulFaction, RhenlandFleet):
    CODE = 'junk_grp'

    WEAPON = wp.RH_JUNKERGUN
    SHIELD_WEAPON = wp.RH_SHIELDGUN
    AFTERBURN = misc.RH_PIRATE
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_PIRATE
    POWER = misc.RH_PIRATE
    SHIELD = misc.RH_PIRATE

    LIGHT = 'SlowSmallYellow'
