from fx.contrail import Contrail
from fx.light import Light

from world import gun
from world.equipment import MainMiscEquip as misc
from world.npc import NPC
from world import ship


class Faction(object):
    INTERCEPTOR1 = None
    INTERCEPTOR2 = None
    ELITE1 = None
    ELITE2 = None
    ELITE3 = None

    STORY_ONLY = False

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)


class LawfulFaction(object):
    LEGALITY = 'lawful'


class UnlawfulFaction(object):
    LEGALITY = 'unlawful'


class RheinlandFleet(object):
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


class BretoniaFleet(object):
    INTERCEPTOR1 = ship.Legionnaire
    INTERCEPTOR2 = ship.Cavalier
    ELITE1 = ship.Centurion
    ELITE2 = ship.Titan
    ELITE3 = ship.Crusader

    SHIPS = [
        INTERCEPTOR1, INTERCEPTOR2,
        ELITE1, ELITE2,
        ELITE3
    ]


class KusariFleet(object):
    INTERCEPTOR1 = ship.Hawk
    INTERCEPTOR2 = ship.Drake
    ELITE1 = ship.Falcon
    ELITE2 = ship.Eagle
    ELITE3 = ship.Dragon

    SHIPS = [
        INTERCEPTOR1, INTERCEPTOR2,
        ELITE1, ELITE2,
        ELITE3
    ]


class BorderWorldFleet(object):
    INTERCEPTOR1 = ship.Starflier
    INTERCEPTOR2 = ship.Startracker
    ELITE1 = ship.Bloodhound
    ELITE2 = ship.Starblazer
    ELITE3 = ship.Wolfhound

    SHIPS = [
        INTERCEPTOR1, INTERCEPTOR2,
        ELITE1, ELITE2,
        ELITE3
    ]


class CorsairFleet(object):
    ELITE1 = ship.Bloodhound
    ELITE2 = ship.Wolfhound

    SHIPS = [
        ELITE1, ELITE2
    ]


class OrderFleet(object):
    ELITE1 = ship.Anubis

    SHIPS = [
        ELITE1
    ]


class OutcastFleet(object):
    INTERCEPTOR1 = ship.Startracker
    ELITE1 = ship.Starblazer

    SHIPS = [
        INTERCEPTOR1,
        ELITE1,
    ]


class BaseRheinland(object):
    SHIELD_WEAPON = gun.RheinlandShieldgun
    CONTRAIL = Contrail.CONTRAIL_RH
    LIGHT = Light.SMALL_YELLOW


class BaseLiberty(object):
    SHIELD_WEAPON = gun.LibertyShieldgun
    CONTRAIL = Contrail.CONTRAIL_LI
    LIGHT = Light.SMALL_BLUE


class BaseBretonia(object):
    SHIELD_WEAPON = gun.BretoniaShieldgun
    CONTRAIL = Contrail.CONTRAIL_BR
    LIGHT = Light.SMALL_BLUE


class BaseKusari(object):
    SHIELD_WEAPON = gun.KusariShieldgun
    CONTRAIL = Contrail.CONTRAIL_KU
    LIGHT = Light.SMALL_ORANGE


class BaseBorderWorld(object):
    SHIELD_WEAPON = gun.BorderWorldCorsairgun
    CONTRAIL = Contrail.CONTRAIL_CO
    LIGHT = Light.SMALL_PURPLE


class RheinlandMainEquip(object):
    AFTERBURN = misc.RH_MAIN
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_MAIN
    POWER = misc.RH_MAIN
    SHIELD = misc.RH_MAIN


class RheinlandCivEquip(object):
    AFTERBURN = misc.RH_CIV
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_CIV
    POWER = misc.RH_CIV
    SHIELD = misc.RH_CIV


class RheinlandPirateEquip(object):
    AFTERBURN = misc.RH_PIRATE
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_PIRATE
    POWER = misc.RH_PIRATE
    SHIELD = misc.RH_PIRATE


class LibertyMainEquip(object):
    AFTERBURN = misc.LI_MAIN
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.LI_MAIN
    POWER = misc.LI_MAIN
    SHIELD = misc.LI_MAIN


class LibertyCivEquip(object):
    AFTERBURN = misc.LI_CIV
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.LI_CIV
    POWER = misc.LI_CIV
    SHIELD = misc.LI_CIV


class LibertyPirateEquip(object):
    AFTERBURN = misc.LI_PIRATE
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.LI_PIRATE
    POWER = misc.LI_PIRATE
    SHIELD = misc.LI_PIRATE


class BretoniaMainEquip(object):
    AFTERBURN = misc.BR_MAIN
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.BR_MAIN
    POWER = misc.BR_MAIN
    SHIELD = misc.BR_MAIN


class BretoniaCivEquip(object):
    AFTERBURN = misc.BR_CIV
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.BR_CIV
    POWER = misc.BR_CIV
    SHIELD = misc.BR_CIV


class BretoniaPirateEquip(object):
    AFTERBURN = misc.BR_PIRATE
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.BR_PIRATE
    POWER = misc.BR_PIRATE
    SHIELD = misc.BR_PIRATE


class KusariMainEquip(object):
    AFTERBURN = misc.KU_MAIN
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.KU_MAIN
    POWER = misc.KU_MAIN
    SHIELD = misc.KU_MAIN


class KusariCivEquip(object):
    AFTERBURN = misc.KU_CIV
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.KU_CIV
    POWER = misc.KU_CIV
    SHIELD = misc.KU_CIV


class KusariPirateEquip(object):
    AFTERBURN = misc.KU_PIRATE
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.KU_PIRATE
    POWER = misc.KU_PIRATE
    SHIELD = misc.KU_PIRATE


class BorderWorldOrderEquip(object):
    AFTERBURN = misc.CO_ORDER
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.CO_ORDER
    POWER = misc.CO_ORDER
    SHIELD = misc.CO_ORDER


class BorderWorldOutcastsEquip(object):
    AFTERBURN = misc.CO_OUTCAST
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.CO_OUTCAST
    POWER = misc.CO_OUTCAST
    SHIELD = misc.CO_OUTCAST


class BorderWorldCorsairEquip(object):
    AFTERBURN = misc.CO_CORSAIR
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.CO_CORSAIR
    POWER = misc.CO_CORSAIR
    SHIELD = misc.CO_CORSAIR


# Rheinland


class RheinlandMain(LawfulFaction, RheinlandFleet, BaseRheinland, RheinlandMainEquip, Faction):
    CODE = 'rh_grp'
    WEAPON = gun.RheinlandLightgun


class RheinlandCivilians(LawfulFaction, RheinlandFleet, BaseRheinland, RheinlandCivEquip, Faction):
    CODE = 'rc_grp'
    WEAPON = gun.RheinlandCivgun


class RheinlandHunters(LawfulFaction, RheinlandFleet, BaseRheinland, RheinlandCivEquip, Faction):
    CODE = 'bh_grp_rh'
    WEAPON = gun.RheinlandHuntergun
    AFTERBURN = misc.RH_MAIN


class RheinlandPirate(UnlawfulFaction, RheinlandFleet, BaseRheinland, RheinlandPirateEquip, Faction):
    CODE = 'pi_grp_rh'
    WEAPON = gun.RheinlandPirategun


class Hessians(UnlawfulFaction, RheinlandFleet, BaseRheinland, RheinlandPirateEquip, Faction):
    CODE = 'rx_grp'
    WEAPON = gun.RheinlandHessiangun


class Junkers(UnlawfulFaction, RheinlandFleet, BaseRheinland, RheinlandPirateEquip, Faction):
    CODE = 'junk_grp'
    WEAPON = gun.RheinlandJunkergun


# Liberty


class LibertyMain(LawfulFaction, LibertyFleet, BaseLiberty, LibertyMainEquip, Faction):
    CODE = 'li_grp'
    WEAPON = gun.LibertyLightgun


class ASF(LibertyMain):
    CODE = 'asf_grp'
    WEAPON = gun.LibertyLightgun


class LibertyCivilians(LawfulFaction, LibertyFleet, BaseLiberty, LibertyCivEquip, Faction):
    CODE = 'lc_grp'
    WEAPON = gun.LibertyCivgun


class LibertyHunters(LawfulFaction, LibertyFleet, BaseLiberty, LibertyCivEquip, Faction):
    CODE = 'bh_grp_li'
    WEAPON = gun.LibertyHuntergun
    AFTERBURN = misc.LI_MAIN


class LibertyPirate(UnlawfulFaction, LibertyFleet, BaseLiberty, LibertyPirateEquip, Faction):
    CODE = 'pi_grp_li'
    WEAPON = gun.LibertyPirategun


class LibertyRogues(UnlawfulFaction, LibertyFleet, BaseLiberty, LibertyPirateEquip, Faction):
    CODE = 'lx_grp'
    WEAPON = gun.LibertyRoguegun


class Starline(UnlawfulFaction, LibertyFleet, BaseLiberty, LibertyPirateEquip, Faction):
    CODE = 'sl_grp'
    WEAPON = gun.LibertyStarlinegun


# Bretonia


class BretoniaMain(LawfulFaction, BretoniaFleet, BaseBretonia, BretoniaMainEquip, Faction):
    CODE = 'br_grp'
    WEAPON = gun.BretoniaLightgun


class BretoniaCivilians(LawfulFaction, BretoniaFleet, BaseBretonia, BretoniaCivEquip, Faction):
    CODE = 'bc_grp'
    WEAPON = gun.BretoniaCivgun


class BretoniaHunters(LawfulFaction, BretoniaFleet, BaseBretonia, BretoniaCivEquip, Faction):
    CODE = 'bh_grp_br'
    WEAPON = gun.BretoniaHuntergun
    AFTERBURN = misc.BR_MAIN


class BretoniaPirate(UnlawfulFaction, BretoniaFleet, BaseBretonia, BretoniaPirateEquip, Faction):
    CODE = 'pi_grp_br'
    WEAPON = gun.BretoniaPirategun


class Ireland(UnlawfulFaction, BretoniaFleet, BaseBretonia, BretoniaPirateEquip, Faction):
    CODE = 'bx_grp'
    WEAPON = gun.BretoniaIragun


class Xenos(UnlawfulFaction, BretoniaFleet, BaseBretonia, BretoniaPirateEquip, Faction):
    CODE = 'xs_grp'
    WEAPON = gun.BretoniaXenosgun


# Kusari


class KusariMain(LawfulFaction, KusariFleet, BaseKusari, KusariMainEquip, Faction):
    CODE = 'ku_grp'
    WEAPON = gun.KusariLightgun


class KusariCivilians(LawfulFaction, KusariFleet, BaseKusari, KusariCivEquip, Faction):
    CODE = 'kc_grp'
    WEAPON = gun.KusariCivgun


class KusariHunters(LawfulFaction, KusariFleet, BaseKusari, KusariCivEquip, Faction):
    CODE = 'bh_grp_ku'
    WEAPON = gun.KusariHuntergun
    AFTERBURN = misc.KU_MAIN


class KusariPirate(UnlawfulFaction, KusariFleet, BaseKusari, KusariPirateEquip, Faction):
    CODE = 'pi_grp_ku'
    WEAPON = gun.KusariPirategun


class Shinobi(UnlawfulFaction, KusariFleet, BaseKusari, KusariPirateEquip, Faction):
    CODE = 'kx_grp'
    WEAPON = gun.KusariShinobigun


class BloodDragons(UnlawfulFaction, KusariFleet, BaseKusari, KusariPirateEquip, Faction):
    CODE = 'bd_grp'
    WEAPON = gun.KusariDragongun


# Border World


class OrderMain(LawfulFaction, OrderFleet, BaseBorderWorld, BorderWorldOrderEquip, Faction):
    CODE = 'or_grp'
    WEAPON = gun.OrderLightgun


class Corsairs(LawfulFaction, CorsairFleet, BaseBorderWorld, BorderWorldCorsairEquip, Faction):
    CODE = 'co_grp'
    WEAPON = gun.BorderWorldCorsairgun


class Outcasts(LawfulFaction, BorderWorldFleet, BaseBorderWorld, BorderWorldOutcastsEquip, Faction):
    CODE = 'edv_grp'
    WEAPON = gun.BorderWorldOutcastgun


class BorderWorldPirate(UnlawfulFaction, BorderWorldFleet, BaseBorderWorld, BorderWorldCorsairEquip, Faction):
    CODE = 'pi_grp_bw'
    WEAPON = gun.BorderWorldPirategun


class DeidrichPeople(UnlawfulFaction, RheinlandFleet, BaseRheinland, RheinlandMainEquip, Faction):
    CODE = 'fc_b_grp'
    WEAPON = gun.RheinlandLightgun
    STORY_ONLY = True


class AlaricLike(LawfulFaction, LibertyFleet, BaseLiberty, LibertyMainEquip, Faction):
    CODE = 'li_al'
    WEAPON = gun.LibertyHuntergun
    AFTERBURN = misc.LI_MAIN
    STORY_ONLY = True
