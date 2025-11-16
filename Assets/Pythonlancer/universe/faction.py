from fx.contrail import Contrail
from fx.light import Light

from world import gun
from world.equipment import MainMiscEquip as misc
from world import bodyparts
from world import ship

from text.strings import MultiString as MS


class Faction:
    INTERCEPTOR1 = None
    INTERCEPTOR2 = None
    ELITE1 = None
    ELITE2 = None
    ELITE3 = None
    RU_NAME = None

    MANAGED = True
    CODE = None
    ALT_CODE = None
    MSG_CODE = None

    COSTUME = None
    GUEST_APPEARANCE = None

    STORY_ONLY = False

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    def __str__(self):
        return self.CODE

    @classmethod
    def get_code(cls):
        return cls.ALT_CODE if cls.ALT_CODE else cls.CODE

    @classmethod
    def get_costume(cls):
        return cls.COSTUME

    @classmethod
    def get_guest(cls):
        return cls.GUEST_APPEARANCE

    def get_ru_name(self):
        return self.RU_NAME

    def get_msg_code(self):
        return self.MSG_CODE if self.MSG_CODE else self.get_code()

    def get_msg_id_prefix(self):
        return f'gcs_refer_faction_{self.get_msg_code()}_short'


class LawfulFaction:
    LEGALITY = 'lawful'


class UnlawfulFaction:
    LEGALITY = 'unlawful'


class RheinlandFleet:
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


class LibertyFleet:
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


class BretoniaFleet:
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


class KusariFleet:
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


class BorderWorldFleet:
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


class CorsairFleet:
    ELITE1 = ship.Bloodhound
    ELITE2 = ship.Wolfhound

    SHIPS = [
        ELITE1, ELITE2
    ]


class OrderFleet:
    ELITE1 = ship.Anubis

    SHIPS = [
        ELITE1
    ]


class OutcastFleet:
    INTERCEPTOR1 = ship.Startracker
    ELITE1 = ship.Starblazer

    SHIPS = [
        INTERCEPTOR1,
        ELITE1,
    ]


class BaseRheinland:
    SHIELD_WEAPON = gun.RheinlandShieldgun
    CONTRAIL = Contrail.CONTRAIL_RH
    LIGHT = Light.SMALL_YELLOW
    COSTUME = bodyparts.RHEINLAND


class BaseLiberty:
    SHIELD_WEAPON = gun.LibertyShieldgun
    CONTRAIL = Contrail.CONTRAIL_LI
    LIGHT = Light.SMALL_BLUE
    COSTUME = bodyparts.LIBERTY


class BaseBretonia:
    SHIELD_WEAPON = gun.BretoniaShieldgun
    CONTRAIL = Contrail.CONTRAIL_BR
    LIGHT = Light.SMALL_BLUE
    COSTUME = bodyparts.BRETONIA


class BaseKusari:
    SHIELD_WEAPON = gun.KusariShieldgun
    CONTRAIL = Contrail.CONTRAIL_KU
    LIGHT = Light.SMALL_ORANGE
    COSTUME = bodyparts.KUSARI


class BaseBorderWorld:
    SHIELD_WEAPON = gun.BorderWorldCorsairgun
    CONTRAIL = Contrail.CONTRAIL_CO
    LIGHT = Light.SMALL_PURPLE
    COSTUME = bodyparts.BORDER_WORLD


class RheinlandMainEquip:
    AFTERBURN = misc.RH_MAIN
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_MAIN
    POWER = misc.RH_MAIN
    SHIELD = misc.RH_MAIN


class RheinlandCivEquip:
    AFTERBURN = misc.RH_CIV
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_CIV
    POWER = misc.RH_CIV
    SHIELD = misc.RH_CIV


class RheinlandPirateEquip:
    AFTERBURN = misc.RH_PIRATE
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.RH_PIRATE
    POWER = misc.RH_PIRATE
    SHIELD = misc.RH_PIRATE


class LibertyMainEquip:
    AFTERBURN = misc.LI_MAIN
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.LI_MAIN
    POWER = misc.LI_MAIN
    SHIELD = misc.LI_MAIN


class LibertyCivEquip:
    AFTERBURN = misc.LI_CIV
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.LI_CIV
    POWER = misc.LI_CIV
    SHIELD = misc.LI_CIV


class LibertyPirateEquip:
    AFTERBURN = misc.LI_PIRATE
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.LI_PIRATE
    POWER = misc.LI_PIRATE
    SHIELD = misc.LI_PIRATE


class BretoniaMainEquip:
    AFTERBURN = misc.BR_MAIN
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.BR_MAIN
    POWER = misc.BR_MAIN
    SHIELD = misc.BR_MAIN


class BretoniaCivEquip:
    AFTERBURN = misc.BR_CIV
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.BR_CIV
    POWER = misc.BR_CIV
    SHIELD = misc.BR_CIV


class BretoniaPirateEquip:
    AFTERBURN = misc.BR_PIRATE
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.BR_PIRATE
    POWER = misc.BR_PIRATE
    SHIELD = misc.BR_PIRATE


class KusariMainEquip:
    AFTERBURN = misc.KU_MAIN
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.KU_MAIN
    POWER = misc.KU_MAIN
    SHIELD = misc.KU_MAIN


class KusariCivEquip:
    AFTERBURN = misc.KU_CIV
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.KU_CIV
    POWER = misc.KU_CIV
    SHIELD = misc.KU_CIV


class KusariPirateEquip:
    AFTERBURN = misc.KU_PIRATE
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.KU_PIRATE
    POWER = misc.KU_PIRATE
    SHIELD = misc.KU_PIRATE


class BorderWorldOrderEquip:
    AFTERBURN = misc.CO_ORDER
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.CO_ORDER
    POWER = misc.CO_ORDER
    SHIELD = misc.CO_ORDER


class BorderWorldOutcastsEquip:
    AFTERBURN = misc.CO_OUTCAST
    TORPEDO = None
    CM = None
    MINE = None
    ENGINE = misc.CO_OUTCAST
    POWER = misc.CO_OUTCAST
    SHIELD = misc.CO_OUTCAST


class BorderWorldCorsairEquip:
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
    GUEST_APPEARANCE = bodyparts.TRADER
    RU_NAME = MS('Р+эйнланд', "Rheinland")


class RheinlandCivilians(LawfulFaction, RheinlandFleet, BaseRheinland, RheinlandCivEquip, Faction):
    CODE = 'rc_grp'
    WEAPON = gun.RheinlandCivgun
    GUEST_APPEARANCE = bodyparts.PEASANT
    RU_NAME = MS('Д+ауманн', "Daumann")


class RheinlandTraders(RheinlandCivilians):
    CODE = 'tr_grp_rh'
    RU_NAME = MS('Интерсп+эйс', "Interspace")


class RheinlandHunters(LawfulFaction, RheinlandFleet, BaseRheinland, RheinlandCivEquip, Faction):
    CODE = 'bh_grp_rh'
    WEAPON = gun.RheinlandHuntergun
    AFTERBURN = misc.RH_MAIN
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Асгард', "PMC Asgaard")


class WorkaroundHunter(RheinlandHunters):
    CODE = 'bh_grp'
    WEAPON = gun.RheinlandHuntergun
    AFTERBURN = misc.RH_MAIN
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    MANAGED = False


class RheinlandPirate(UnlawfulFaction, RheinlandFleet, BaseRheinland, RheinlandPirateEquip, Faction):
    CODE = 'pi_grp_rh'
    WEAPON = gun.RheinlandPirategun
    GUEST_APPEARANCE = bodyparts.PIRATE
    RU_NAME = MS('Бундсчух', "Bundschuh")


class WorkaroundPirate(RheinlandHunters):
    CODE = 'pi_grp'
    WEAPON = gun.RheinlandHuntergun
    AFTERBURN = misc.RH_MAIN
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    MANAGED = False


class Hessians(UnlawfulFaction, RheinlandFleet, BaseRheinland, RheinlandPirateEquip, Faction):
    CODE = 'rx_grp'
    WEAPON = gun.RheinlandHessiangun
    GUEST_APPEARANCE = bodyparts.PIRATE
    RU_NAME = MS('Г+ессенцы', "Hessians")


class Junkers(UnlawfulFaction, RheinlandFleet, BaseRheinland, RheinlandPirateEquip, Faction):
    CODE = 'junk_grp'
    WEAPON = gun.RheinlandJunkergun
    GUEST_APPEARANCE = bodyparts.PEASANT
    RU_NAME = MS('Мусорщики', "Junkers")


# Liberty


class LibertyMain(LawfulFaction, LibertyFleet, BaseLiberty, LibertyMainEquip, Faction):
    CODE = 'li_grp'
    WEAPON = gun.LibertyLightgun
    GUEST_APPEARANCE = bodyparts.TRADER
    RU_NAME = MS('Л+иберти', "Liberty")


class ASF(LibertyMain):
    CODE = 'asf_grp'
    WEAPON = gun.LibertyLightgun
    GUEST_APPEARANCE = bodyparts.MILITARY
    RU_NAME = MS('Эс-Бэ-А', "ASF")


class LibertyCivilians(LawfulFaction, LibertyFleet, BaseLiberty, LibertyCivEquip, Faction):
    CODE = 'lc_grp'
    WEAPON = gun.LibertyCivgun
    GUEST_APPEARANCE = bodyparts.PEASANT
    RU_NAME = MS('Дип Спэйс', "Deep Space Engineering")


class LibertyTraders(LibertyCivilians):
    CODE = 'tr_grp_li'
    RU_NAME = MS('Адж+ейра', "Ageira")


class LibertyHunters(LawfulFaction, LibertyFleet, BaseLiberty, LibertyCivEquip, Faction):
    CODE = 'bh_grp_li'
    WEAPON = gun.LibertyHuntergun
    AFTERBURN = misc.LI_MAIN
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Щит', "PMC Shield")


class LibertyPirate(UnlawfulFaction, LibertyFleet, BaseLiberty, LibertyPirateEquip, Faction):
    CODE = 'pi_grp_li'
    WEAPON = gun.LibertyPirategun
    GUEST_APPEARANCE = bodyparts.PIRATE
    RU_NAME = MS('Д+икси', "Dixie")


class LibertyRogues(UnlawfulFaction, LibertyFleet, BaseLiberty, LibertyPirateEquip, Faction):
    CODE = 'lx_grp'
    WEAPON = gun.LibertyRoguegun
    GUEST_APPEARANCE = bodyparts.PIRATE
    RU_NAME = MS('Разбойники Л+иберти', "Liberty Rogues")


class Starline(UnlawfulFaction, LibertyFleet, BaseLiberty, LibertyPirateEquip, Faction):
    CODE = 'sl_grp'
    WEAPON = gun.LibertyStarlinegun
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Старл+айн', "Starline")


class LaneHackers(UnlawfulFaction, LibertyFleet, BaseLiberty, LibertyPirateEquip, Faction):
    CODE = 'hack_grp'
    WEAPON = gun.LibertyStarlinegun
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Хакеры', "Lane Hackers")


# Bretonia


class BretoniaMain(LawfulFaction, BretoniaFleet, BaseBretonia, BretoniaMainEquip, Faction):
    CODE = 'br_grp'
    WEAPON = gun.BretoniaLightgun
    GUEST_APPEARANCE = bodyparts.TRADER
    RU_NAME = MS('Брет+ония', "Bretonia")


class BretoniaCivilians(LawfulFaction, BretoniaFleet, BaseBretonia, BretoniaCivEquip, Faction):
    CODE = 'bc_grp'
    WEAPON = gun.BretoniaCivgun
    GUEST_APPEARANCE = bodyparts.PEASANT
    RU_NAME = MS('Би-Эм-Эм', "BMM")


class BretoniaTraders(BretoniaCivilians):
    CODE = 'tr_grp_br'
    RU_NAME = MS('Б+овекс', "Bowex")


class BretoniaHunters(LawfulFaction, BretoniaFleet, BaseBretonia, BretoniaCivEquip, Faction):
    CODE = 'bh_grp_br'
    WEAPON = gun.BretoniaHuntergun
    AFTERBURN = misc.BR_MAIN
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Р+оял-Форс', "PMC Roal Force")


class BretoniaPirate(UnlawfulFaction, BretoniaFleet, BaseBretonia, BretoniaPirateEquip, Faction):
    CODE = 'pi_grp_br'
    WEAPON = gun.BretoniaPirategun
    GUEST_APPEARANCE = bodyparts.PIRATE
    RU_NAME = MS('Гайане', "Gaians")


class Ireland(UnlawfulFaction, BretoniaFleet, BaseBretonia, BretoniaPirateEquip, Faction):
    CODE = 'bx_grp'
    WEAPON = gun.BretoniaIragun
    GUEST_APPEARANCE = bodyparts.PIRATE
    RU_NAME = MS('И-Эр-А', "IRA")


class Xenos(UnlawfulFaction, BretoniaFleet, BaseBretonia, BretoniaPirateEquip, Faction):
    CODE = 'xenos_grp'
    WEAPON = gun.BretoniaXenosgun
    GUEST_APPEARANCE = bodyparts.PEASANT
    RU_NAME = MS('Кс+еносы', "Xenos")


# Kusari


class KusariMain(LawfulFaction, KusariFleet, BaseKusari, KusariMainEquip, Faction):
    CODE = 'ku_grp'
    WEAPON = gun.KusariLightgun
    GUEST_APPEARANCE = bodyparts.TRADER
    RU_NAME = MS('Кус+ари', "Kusari")


class KusariCivilians(LawfulFaction, KusariFleet, BaseKusari, KusariCivEquip, Faction):
    CODE = 'kc_grp'
    WEAPON = gun.KusariCivgun
    GUEST_APPEARANCE = bodyparts.PEASANT
    RU_NAME = MS('Киш+иро', "Kishiro")


class KusariTraders(KusariCivilians):
    CODE = 'tr_grp_ku'
    RU_NAME = MS('Сам+ура', "Samura")


class KusariHunters(LawfulFaction, KusariFleet, BaseKusari, KusariCivEquip, Faction):
    CODE = 'bh_grp_ku'
    WEAPON = gun.KusariHuntergun
    AFTERBURN = misc.KU_MAIN
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Чёрный Дракон', "PMC Black Dragon")


class KusariPirate(UnlawfulFaction, KusariFleet, BaseKusari, KusariPirateEquip, Faction):
    CODE = 'pi_grp_ku'
    WEAPON = gun.KusariPirategun
    GUEST_APPEARANCE = bodyparts.PIRATE
    RU_NAME = MS('Золот+ые Хризант+емы', "Golden Chrystantems")


class Shinobi(UnlawfulFaction, KusariFleet, BaseKusari, KusariPirateEquip, Faction):
    CODE = 'kx_grp'
    WEAPON = gun.KusariShinobigun
    GUEST_APPEARANCE = bodyparts.PIRATE
    RU_NAME = MS('Клан Шин+оби', "Shinobi Clan")


class FarmerAlliance(UnlawfulFaction, KusariFleet, BaseKusari, KusariPirateEquip, Faction):
    CODE = 'farm_grp'
    WEAPON = gun.KusariDragongun
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Фермеры', "Farmer Alliance")


# Border World


class OrderMain(LawfulFaction, OrderFleet, BaseBorderWorld, BorderWorldOrderEquip, Faction):
    CODE = 'or_grp'
    WEAPON = gun.OrderLightgun
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Орден', "The Order")


class Corsairs(LawfulFaction, CorsairFleet, BaseBorderWorld, BorderWorldCorsairEquip, Faction):
    CODE = 'co_grp'
    WEAPON = gun.BorderWorldCorsairgun
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Корс+ары', "Corsairs")


class Outcasts(LawfulFaction, BorderWorldFleet, BaseBorderWorld, BorderWorldOutcastsEquip, Faction):
    CODE = 'edv_grp'
    MSG_CODE = 'out_grp'
    WEAPON = gun.BorderWorldOutcastgun
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Изг+ои', "Outcasts")


class BorderWorldPirate(UnlawfulFaction, BorderWorldFleet, BaseBorderWorld, BorderWorldCorsairEquip, Faction):
    CODE = 'pi_grp_bw'
    WEAPON = gun.BorderWorldPirategun
    GUEST_APPEARANCE = bodyparts.PIRATE
    RU_NAME = MS('Пилигр+имы', "Pilgrims")


class BoderWorldTraders(BorderWorldPirate):
    CODE = 'tr_grp_bw'
    RU_NAME = MS('Меркадо', "Mercado")


class DeidrichPeople(UnlawfulFaction, RheinlandFleet, BaseRheinland, RheinlandMainEquip, Faction):
    CODE = 'fc_b_grp'
    WEAPON = gun.RheinlandLightgun
    STORY_ONLY = True
    MANAGED = False


class AlaricLike(LawfulFaction, LibertyFleet, BaseLiberty, LibertyMainEquip, Faction):
    CODE = 'li_al'
    WEAPON = gun.LibertyHuntergun
    AFTERBURN = misc.LI_MAIN
    STORY_ONLY = True
    MANAGED = False


class Nomad(Faction):
    CODE = 'fc_n_grp'
    STORY_ONLY = True
    MANAGED = False


class Unknown(Faction):
    CODE = 'fc_uk_grp'
    STORY_ONLY = True
    MANAGED = False
