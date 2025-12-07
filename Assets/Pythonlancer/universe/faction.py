from fx.contrail import Contrail
from fx.light import Light

from world import gun
from world.equipment import MainMiscEquip as misc
from world import bodyparts
from world import ship

from text.strings import MultiString as MS
from text.dividers import SINGLE_DIVIDER


# 047050 - Navy (short)

# 196846 - Liberty Navy (Main!)

# 328680 - Liberty Navy
# 328780 - the Liberty Navy
# 328880 - Liberty Navy
# 328980 - The Liberty Navy


ENEMY_MAX = -0.91
ENEMY_MED = -0.65
ENEMY_MIN = -0.3
NEUTRAL = 0
FRIEND_MIN = 0.3
FRIEND_MED = 0.65
FRIEND_MAX = 0.91
MAXIMUM = 0.9


HATE1 = -0.025
HATE2 = -0.05
HATE3 = -0.1
HATE4 = -0.25
HATE5 = -0.3
HATE6 = -0.35
HATE7 = -0.4
HATE8 = -0.45
HATE9 = -0.5

LIKE1 = 0.025
LIKE2 = 0.05
LIKE3 = 0.1
LIKE4 = 0.25
LIKE5 = 0.3
LIKE6 = 0.35
LIKE7 = 0.4
LIKE8 = 0.45
LIKE9 = 0.5


class LoadedRelation:
    def __init__(self, faction):
        self.faction = faction
        self.reputation: float = NEUTRAL
        self.empathy: float = NEUTRAL

    def set_reputation(self, reputation):
        if self.reputation == 0:
            self.reputation = reputation
        elif self.reputation > 0:
            if reputation > self.reputation:
                self.reputation = reputation
        else:
            if reputation < self.reputation:
                self.reputation = reputation

    def set_empathy(self, empathy):
        if self.empathy == 0:
            self.empathy = empathy
        elif self.empathy > 0:
            if empathy > self.empathy:
                self.empathy = empathy
        else:
            if empathy < self.empathy:
                self.empathy = empathy


class Faction:
    INTERCEPTOR = None
    ELITE = None
    FRIEGHTER = None
    RU_NAME = None

    MANAGED = True
    CODE = None
    ALT_CODE = None
    MSG_CODE = None
    KIND = None

    COSTUME = None
    GUEST_APPEARANCE = None

    STORY_ONLY = False

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    def __str__(self):
        return self.CODE

    def __init__(self):
        self.relations = {}

    def is_managed(self):
        return self.MANAGED

    def get_ships(self):
        ships = []
        if self.INTERCEPTOR:
            ships.append(self.INTERCEPTOR)
        if self.ELITE:
            ships.append(self.ELITE)
        if self.FRIEGHTER:
            ships.append(self.FRIEGHTER)
        return ships

    def init_relations(self, rel_faction):
        self.relations[rel_faction.CODE] = LoadedRelation(rel_faction)

    def change_reputation(self, rel_faction, reputation):
        self.relations[rel_faction.CODE].set_reputation(reputation)

    def change_empathy(self, rel_faction, empathy):
        self.relations[rel_faction.CODE].set_empathy(empathy)

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

    def get_msg_id_prefix_main(self):
        return f'gcs_refer_faction_{self.get_msg_code()}'

    @property
    def msg(self):
        return self.get_msg_id_prefix_main()


class LawfulFaction:
    LEGALITY = 'lawful'


class UnlawfulFaction:
    LEGALITY = 'unlawful'


class CivilianFleet:
    INTERCEPTOR = ship.Banshee
    ELITE = ship.Valkyrie
    # use transport as frieghter


class RheinlandMainFleet:
    INTERCEPTOR = ship.Banshee
    ELITE = ship.Valkyrie
    FREIGHTER = ship.Humpback


class RheinlandSecondFleet:
    INTERCEPTOR = ship.Dagger
    ELITE = ship.Stiletto


class LibertyMainFleet:
    INTERCEPTOR = ship.Patriot
    ELITE = ship.Defender
    FREIGHTER = ship.Rhino


class LibertySecondFleet:
    INTERCEPTOR = ship.Piranha
    ELITE = ship.Barracuda


class BretoniaMainFleet:
    INTERCEPTOR = ship.Cavalier
    ELITE = ship.Crusader
    FREIGHTER = ship.Clydesdale


class BretoniaSecondFleet:
    INTERCEPTOR = ship.Legionnaire
    ELITE = ship.Centurion


class KusariMainFleet:
    INTERCEPTOR = ship.Drake
    ELITE = ship.Dragon
    FREIGHTER = ship.Dron


class KusariSecondFleet:
    INTERCEPTOR = ship.Hawk
    ELITE = ship.Falcon


class BorderWorldFleet:
    INTERCEPTOR = ship.Bloodhound
    ELITE = ship.Wolfhound
    FREIGHTER = ship.Mule


class CorsairFleet:
    INTERCEPTOR = ship.Bloodhound
    ELITE = ship.Wolfhound
    FREIGHTER = ship.Mule


class OrderFleet:
    ELITE = ship.Anubis


class OutcastFleet:
    INTERCEPTOR = ship.Startracker
    ELITE = ship.Starblazer
    FREIGHTER = ship.Dromader


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


class RheinlandMain(LawfulFaction, RheinlandMainFleet, BaseRheinland, RheinlandMainEquip, Faction):
    CODE = 'rh_grp'
    WEAPON = gun.RheinlandLightgun
    GUEST_APPEARANCE = bodyparts.TRADER
    RU_NAME = MS('Р+эйнланд', "Rheinland")


class RheinlandMilitary(RheinlandMain):
    CODE = 'rm_grp'
    MANAGED = False


class RheinlandCivilians(LawfulFaction, RheinlandMainFleet, BaseRheinland, RheinlandCivEquip, Faction):
    CODE = 'rc_grp'
    WEAPON = gun.RheinlandCivgun
    GUEST_APPEARANCE = bodyparts.PEASANT
    RU_NAME = MS('Д+ауманн', "Daumann")


class RheinlandTraders(LawfulFaction, CivilianFleet, BaseRheinland, RheinlandCivEquip, Faction):
    CODE = 'tr_grp_rh'
    WEAPON = gun.RheinlandCivgun
    GUEST_APPEARANCE = bodyparts.PEASANT
    RU_NAME = MS('Интерсп+эйс', "Interspace")


class RheinlandHunters(LawfulFaction, RheinlandSecondFleet, BaseRheinland, RheinlandCivEquip, Faction):
    CODE = 'bh_grp_rh'
    WEAPON = gun.RheinlandHuntergun
    AFTERBURN = misc.RH_MAIN
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Асгард', "Asgard")


class RheinlandPirate(UnlawfulFaction, RheinlandSecondFleet, BaseRheinland, RheinlandPirateEquip, Faction):
    CODE = 'pi_grp_rh'
    WEAPON = gun.RheinlandPirategun
    GUEST_APPEARANCE = bodyparts.PIRATE
    RU_NAME = MS('Бундсчух', "Bundschuh")
    PIRATE = True


class Hessians(UnlawfulFaction, RheinlandSecondFleet, BaseRheinland, RheinlandPirateEquip, Faction):
    CODE = 'rx_grp'
    WEAPON = gun.RheinlandHessiangun
    GUEST_APPEARANCE = bodyparts.PIRATE
    RU_NAME = MS('Г+ессенцы', "Hessians")
    PIRATE = True


class Junkers(UnlawfulFaction, CivilianFleet, BaseRheinland, RheinlandPirateEquip, Faction):
    CODE = 'junk_grp'
    WEAPON = gun.RheinlandJunkergun
    GUEST_APPEARANCE = bodyparts.PEASANT
    RU_NAME = MS('Мусорщики', "Junkers")
    PIRATE = True


# Liberty


class LibertyMain(LawfulFaction, LibertyMainFleet, BaseLiberty, LibertyMainEquip, Faction):
    CODE = 'li_grp'
    WEAPON = gun.LibertyLightgun
    GUEST_APPEARANCE = bodyparts.TRADER
    RU_NAME = MS('Л+иберти', "Liberty")


class LibertyMilitary(LibertyMain):
    CODE = 'lm_grp'
    MANAGED = False


class ASF(LibertyMain):
    CODE = 'asf_grp'
    WEAPON = gun.LibertyLightgun
    GUEST_APPEARANCE = bodyparts.MILITARY
    RU_NAME = MS('Эс-Бэ-А', "Ai-eS-eF")
    MANAGED = False


class LibertyCivilians(LawfulFaction, LibertyMainFleet, BaseLiberty, LibertyCivEquip, Faction):
    CODE = 'lc_grp'
    WEAPON = gun.LibertyCivgun
    GUEST_APPEARANCE = bodyparts.PEASANT
    RU_NAME = MS('Дип Спэйс', "Deep Space")


class LibertyTraders(LawfulFaction, CivilianFleet, BaseLiberty, LibertyCivEquip, Faction):
    CODE = 'tr_grp_li'
    WEAPON = gun.LibertyCivgun
    GUEST_APPEARANCE = bodyparts.PEASANT
    RU_NAME = MS('Адж+ейра', "Ageira")


class LibertyHunters(LawfulFaction, LibertySecondFleet, BaseLiberty, LibertyCivEquip, Faction):
    CODE = 'bh_grp_li'
    WEAPON = gun.LibertyHuntergun
    AFTERBURN = misc.LI_MAIN
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Щит', "Shield")


class LibertyPirate(UnlawfulFaction, LibertySecondFleet, BaseLiberty, LibertyPirateEquip, Faction):
    CODE = 'pi_grp_li'
    WEAPON = gun.LibertyPirategun
    GUEST_APPEARANCE = bodyparts.PIRATE
    RU_NAME = MS('Д+икси', "Dixie")


class LibertyRogues(UnlawfulFaction, LibertySecondFleet, BaseLiberty, LibertyPirateEquip, Faction):
    CODE = 'lx_grp'
    WEAPON = gun.LibertyRoguegun
    GUEST_APPEARANCE = bodyparts.PIRATE
    RU_NAME = MS('Разбойники Л+иберти', "Liberty Rogues")


class Starline(UnlawfulFaction, LibertyMainFleet, BaseLiberty, LibertyPirateEquip, Faction):
    CODE = 'sl_grp'
    WEAPON = gun.LibertyStarlinegun
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Старл+айн', "Starline")


class LaneHackers(UnlawfulFaction, RheinlandSecondFleet, BaseLiberty, LibertyPirateEquip, Faction):
    CODE = 'hack_grp'
    WEAPON = gun.LibertyStarlinegun
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Хакеры', "Hackers")


# Bretonia


class BretoniaMain(LawfulFaction, BretoniaMainFleet, BaseBretonia, BretoniaMainEquip, Faction):
    CODE = 'br_grp'
    WEAPON = gun.BretoniaLightgun
    GUEST_APPEARANCE = bodyparts.TRADER
    RU_NAME = MS('Брет+ония', "Bretonia")


class BretoniaMilitary(BretoniaMain):
    CODE = 'bm_grp'
    MANAGED = False


class BretoniaCivilians(LawfulFaction, BretoniaMainFleet, BaseBretonia, BretoniaCivEquip, Faction):
    CODE = 'bc_grp'
    WEAPON = gun.BretoniaCivgun
    GUEST_APPEARANCE = bodyparts.PEASANT
    RU_NAME = MS('Би-Эм-Эм', "BMM")


class BretoniaTraders(LawfulFaction, CivilianFleet, BaseBretonia, BretoniaCivEquip, Faction):
    CODE = 'tr_grp_br'
    WEAPON = gun.BretoniaCivgun
    GUEST_APPEARANCE = bodyparts.PEASANT
    RU_NAME = MS('Б+овекс', "Bowex")


class BretoniaHunters(LawfulFaction, BretoniaSecondFleet, BaseBretonia, BretoniaCivEquip, Faction):
    CODE = 'bh_grp_br'
    WEAPON = gun.BretoniaHuntergun
    AFTERBURN = misc.BR_MAIN
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Р+оял-Форс', "Roal Force")


class BretoniaPirate(UnlawfulFaction, CivilianFleet, BaseBretonia, BretoniaPirateEquip, Faction):
    CODE = 'pi_grp_br'
    WEAPON = gun.BretoniaPirategun
    GUEST_APPEARANCE = bodyparts.PIRATE
    RU_NAME = MS('Гайане', "Gaians")


class Ireland(UnlawfulFaction, BretoniaSecondFleet, BaseBretonia, BretoniaPirateEquip, Faction):
    CODE = 'bx_grp'
    WEAPON = gun.BretoniaIragun
    GUEST_APPEARANCE = bodyparts.PIRATE
    RU_NAME = MS('И-Эр-А', "I-eR-A")


class Xenos(UnlawfulFaction, BretoniaSecondFleet, BaseBretonia, BretoniaPirateEquip, Faction):
    CODE = 'xenos_grp'
    WEAPON = gun.BretoniaXenosgun
    GUEST_APPEARANCE = bodyparts.PEASANT
    RU_NAME = MS('Кс+еносы', "Xenos")


# Kusari


class KusariMain(LawfulFaction, KusariMainFleet, BaseKusari, KusariMainEquip, Faction):
    CODE = 'ku_grp'
    WEAPON = gun.KusariLightgun
    GUEST_APPEARANCE = bodyparts.TRADER
    RU_NAME = MS('Кус+ари', "Kusari")


class KusariMilitary(KusariMain):
    CODE = 'km_grp'
    MANAGED = False


class KusariCivilians(LawfulFaction, KusariMainFleet, BaseKusari, KusariCivEquip, Faction):
    CODE = 'kc_grp'
    WEAPON = gun.KusariCivgun
    GUEST_APPEARANCE = bodyparts.PEASANT
    RU_NAME = MS('Киш+иро', "Kishiro")


class KusariTraders(LawfulFaction, CivilianFleet, BaseKusari, KusariCivEquip, Faction):
    CODE = 'tr_grp_ku'
    WEAPON = gun.KusariCivgun
    GUEST_APPEARANCE = bodyparts.PEASANT
    RU_NAME = MS('Сам+ура', "Samura")


class KusariHunters(LawfulFaction, KusariSecondFleet, BaseKusari, KusariCivEquip, Faction):
    CODE = 'bh_grp_ku'
    WEAPON = gun.KusariHuntergun
    AFTERBURN = misc.KU_MAIN
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Чёрный Дракон', "Black Dragon")


class KusariPirate(UnlawfulFaction, KusariSecondFleet, BaseKusari, KusariPirateEquip, Faction):
    CODE = 'pi_grp_ku'
    WEAPON = gun.KusariPirategun
    GUEST_APPEARANCE = bodyparts.PIRATE
    RU_NAME = MS('Золот+ые Хризант+емы', "Golden Chrystantems")


class Shinobi(UnlawfulFaction, KusariMainFleet, BaseKusari, KusariPirateEquip, Faction):
    CODE = 'kx_grp'
    WEAPON = gun.KusariShinobigun
    GUEST_APPEARANCE = bodyparts.PIRATE
    RU_NAME = MS('Клан Шин+оби', "Shinobi Clan")


class FarmerAlliance(UnlawfulFaction, KusariSecondFleet, BaseKusari, KusariPirateEquip, Faction):
    CODE = 'farm_grp'
    WEAPON = gun.KusariDragongun
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Фермеры', "Farmers")


# Border World


class OrderMain(LawfulFaction, OrderFleet, BaseBorderWorld, BorderWorldOrderEquip, Faction):
    CODE = 'or_grp'
    WEAPON = gun.OrderLightgun
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Орден', "The Order")


class OrderMilitary(OrderMain):
    CODE = 'om_grp'
    MANAGED = False


class Corsairs(UnlawfulFaction, CorsairFleet, BaseBorderWorld, BorderWorldCorsairEquip, Faction):
    CODE = 'co_grp'
    WEAPON = gun.BorderWorldCorsairgun
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Корс+ары', "Corsairs")


class CorsairMilitary(Corsairs):
    CODE = 'cm_grp'
    MANAGED = False


class BorderWorldHunters(UnlawfulFaction, CorsairFleet, BaseBorderWorld, BorderWorldCorsairEquip, Faction):
    CODE = 'bh_grp_bw'
    MSG_CODE = 'co_grp'
    WEAPON = gun.BorderWorldCorsairgun
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Приватиры', "Privateers")


class Outcasts(LawfulFaction, RheinlandSecondFleet, BaseBorderWorld, BorderWorldOutcastsEquip, Faction):
    CODE = 'out_grp'
    WEAPON = gun.BorderWorldOutcastgun
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Изг+ои', "Outcasts")


class BorderWorldPirate(UnlawfulFaction, RheinlandSecondFleet, BaseBorderWorld, BorderWorldCorsairEquip, Faction):
    CODE = 'pi_grp_bw'
    WEAPON = gun.BorderWorldPirategun
    GUEST_APPEARANCE = bodyparts.PIRATE
    RU_NAME = MS('Пилигр+имы', "Pilgrims")


class BorderWorldTraders(UnlawfulFaction, CorsairFleet, BaseBorderWorld, BorderWorldCorsairEquip, Faction):
    CODE = 'tr_grp_bw'
    WEAPON = gun.BorderWorldPirategun
    GUEST_APPEARANCE = bodyparts.PIRATE
    RU_NAME = MS('Меркадо', "Mercado")


class DeidrichPeople(UnlawfulFaction, BaseRheinland, RheinlandMainEquip, Faction):
    CODE = 'dtr_grp'
    WEAPON = gun.RheinlandLightgun
    MANAGED = False


class OdjaPeople(UnlawfulFaction, BaseKusari, KusariMainEquip, Faction):
    CODE = 'odja_grp'
    WEAPON = gun.RheinlandLightgun
    MANAGED = False


class Hispaniola(UnlawfulFaction, BaseKusari, KusariMainEquip, Faction):
    CODE = 'hsp_grp'
    WEAPON = gun.RheinlandLightgun
    MANAGED = False


class AlaricLike(LawfulFaction, BaseLiberty, LibertyMainEquip, Faction):
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


class Relation:
    def __init__(self, faction, reputation: float = NEUTRAL, empathy: float = NEUTRAL):
        self.faction = faction
        self.reputation = reputation
        self.empathy = empathy

    def get_faction(self):
        return self.faction

    def get_reputation(self):
        return self.reputation

    def get_empathy(self):
        return self.empathy

    def get_reputation_inverse(self):
        if self.reputation == 0:
            return 0

        if self.reputation > 0:
            return self.reputation - (self.reputation*2)
        else:
            return self.reputation + (abs(self.reputation)*2)

    def get_empathy_inverse(self):
        if self.empathy == 0:
            return 0

        if self.empathy > 0:
            print(self.empathy - (self.empathy*2))
            return self.empathy - (self.empathy*2)
        else:
            print(self.empathy + (abs(self.empathy)*2))
            return self.empathy + (abs(self.empathy)*2)


class FactionRelation:
    def __init__(self, faction, relations):
        self.faction = faction
        self.relations = relations


PLAYER_RELATIONS = [
    Relation(RheinlandMain, NEUTRAL),
    Relation(LibertyMain, NEUTRAL),
    Relation(BretoniaMain, NEUTRAL),
    Relation(KusariMain, NEUTRAL),

    Relation(RheinlandHunters, NEUTRAL),
    Relation(LibertyHunters, NEUTRAL),
    Relation(BretoniaHunters, NEUTRAL),
    Relation(KusariHunters, NEUTRAL),
    Relation(BorderWorldHunters, NEUTRAL),

    Relation(RheinlandCivilians, NEUTRAL),
    Relation(LibertyCivilians, NEUTRAL),
    Relation(BretoniaCivilians, NEUTRAL),
    Relation(KusariCivilians, NEUTRAL),

    Relation(RheinlandTraders, NEUTRAL),
    Relation(LibertyTraders, NEUTRAL),
    Relation(BretoniaTraders, NEUTRAL),
    Relation(KusariTraders, NEUTRAL),

    Relation(RheinlandPirate, ENEMY_MED),
    Relation(LibertyPirate, ENEMY_MED),
    Relation(BretoniaPirate, ENEMY_MED),
    Relation(KusariPirate, ENEMY_MED),
    Relation(BorderWorldPirate, ENEMY_MED),

    Relation(OrderMain, NEUTRAL),
    Relation(ASF, NEUTRAL),
    Relation(Corsairs, ENEMY_MED),
    Relation(Outcasts, NEUTRAL),

    Relation(Hessians, ENEMY_MED),
    Relation(Junkers, ENEMY_MED),
    Relation(LibertyRogues, ENEMY_MED),
    Relation(Starline, ENEMY_MED),
    Relation(LaneHackers, ENEMY_MED),
    Relation(Xenos, ENEMY_MED),
    Relation(Ireland, ENEMY_MED),
    Relation(Shinobi, ENEMY_MED),
    Relation(FarmerAlliance, ENEMY_MED),

    Relation(Nomad, ENEMY_MAX),
    Relation(DeidrichPeople, ENEMY_MAX),
    Relation(OdjaPeople, NEUTRAL),
    Relation(Hispaniola, NEUTRAL),
]


class PlayerFaction:

    @classmethod
    def get_init_factions(cls):
        result = []
        for rel in PLAYER_RELATIONS:
            result.append(
                f'house = {rel.reputation}, {rel.faction1.CODE}'
            )
        return SINGLE_DIVIDER.join(result)


RELATIONS = [
    FactionRelation(
        RheinlandMain,
        [
            Relation(RheinlandMain, FRIEND_MAX),
            Relation(LibertyMain, FRIEND_MAX),
            Relation(BretoniaMain, FRIEND_MAX),
            Relation(KusariMain, FRIEND_MAX),

            Relation(RheinlandHunters, NEUTRAL, LIKE2),
            Relation(LibertyHunters, NEUTRAL, LIKE1),
            Relation(BretoniaHunters, NEUTRAL, LIKE1),
            Relation(KusariHunters, NEUTRAL, LIKE1),
            Relation(BorderWorldHunters, NEUTRAL, LIKE1),

            Relation(RheinlandCivilians, FRIEND_MAX, LIKE4),
            Relation(LibertyCivilians, FRIEND_MAX, LIKE2),
            Relation(BretoniaCivilians, FRIEND_MAX, LIKE2),
            Relation(KusariCivilians, FRIEND_MAX, LIKE2),

            Relation(RheinlandTraders, FRIEND_MAX, LIKE3),
            Relation(LibertyTraders, FRIEND_MAX, LIKE2),
            Relation(BretoniaTraders, FRIEND_MAX, LIKE2),
            Relation(KusariTraders, FRIEND_MAX, LIKE2),
            Relation(BorderWorldTraders, NEUTRAL, LIKE2),

            Relation(RheinlandPirate, ENEMY_MAX, HATE5),
            Relation(LibertyPirate, ENEMY_MAX, HATE3),
            Relation(BretoniaPirate, ENEMY_MAX, HATE2),
            Relation(KusariPirate, ENEMY_MAX, HATE3),
            Relation(BorderWorldPirate, ENEMY_MAX, HATE1),

            Relation(Corsairs, ENEMY_MED, HATE6),
            Relation(Outcasts, NEUTRAL),

            Relation(Hessians, ENEMY_MED, HATE8),
            Relation(Junkers, ENEMY_MIN, HATE3),
            Relation(LibertyRogues, ENEMY_MED, HATE7),
            Relation(Starline, ENEMY_MED, HATE3),
            Relation(LaneHackers, ENEMY_MED, HATE6),
            Relation(Xenos, ENEMY_MED, HATE7),
            Relation(Ireland, ENEMY_MED, HATE3),
            Relation(Shinobi, ENEMY_MED, HATE5),
            Relation(FarmerAlliance, ENEMY_MED, HATE5),

            Relation(Nomad, ENEMY_MAX),
        ]
    ),

    FactionRelation(
        LibertyMain,
        [
            Relation(RheinlandMain, FRIEND_MAX),
            Relation(LibertyMain, FRIEND_MAX),
            Relation(BretoniaMain, FRIEND_MAX),
            Relation(KusariMain, FRIEND_MAX),

            Relation(RheinlandHunters, NEUTRAL, LIKE1),
            Relation(LibertyHunters, NEUTRAL, LIKE2),
            Relation(BretoniaHunters, NEUTRAL, LIKE1),
            Relation(KusariHunters, NEUTRAL, LIKE1),
            Relation(BorderWorldHunters, NEUTRAL, LIKE1),

            Relation(RheinlandCivilians, FRIEND_MAX, LIKE2),
            Relation(LibertyCivilians, FRIEND_MAX, LIKE4),
            Relation(BretoniaCivilians, FRIEND_MAX, LIKE2),
            Relation(KusariCivilians, FRIEND_MAX, LIKE2),

            Relation(RheinlandTraders, FRIEND_MAX, LIKE2),
            Relation(LibertyTraders, FRIEND_MAX, LIKE3),
            Relation(BretoniaTraders, FRIEND_MAX, LIKE2),
            Relation(KusariTraders, FRIEND_MAX, LIKE2),
            Relation(BorderWorldTraders, NEUTRAL, LIKE2),

            Relation(RheinlandPirate, ENEMY_MAX, HATE3),
            Relation(LibertyPirate, ENEMY_MAX, HATE5),
            Relation(BretoniaPirate, ENEMY_MAX, HATE3),
            Relation(KusariPirate, ENEMY_MAX, HATE2),
            Relation(BorderWorldPirate, ENEMY_MAX, HATE1),

            Relation(Corsairs, ENEMY_MED, HATE6),
            Relation(Outcasts, NEUTRAL),

            Relation(Hessians, ENEMY_MED, HATE3),
            Relation(Junkers, ENEMY_MIN, HATE2),
            Relation(LibertyRogues, ENEMY_MED, HATE7),
            Relation(Starline, ENEMY_MED, HATE2),
            Relation(LaneHackers, ENEMY_MED, HATE8),
            Relation(Xenos, ENEMY_MED, HATE7),
            Relation(Ireland, ENEMY_MED, HATE4),
            Relation(Shinobi, ENEMY_MED, HATE2),
            Relation(FarmerAlliance, ENEMY_MED, HATE1),

            Relation(Nomad, ENEMY_MAX),
        ]
    ),

    FactionRelation(
        BretoniaMain,
        [
            Relation(RheinlandMain, FRIEND_MAX),
            Relation(LibertyMain, FRIEND_MAX),
            Relation(BretoniaMain, FRIEND_MAX),
            Relation(KusariMain, FRIEND_MAX),

            Relation(RheinlandHunters, NEUTRAL, LIKE1),
            Relation(LibertyHunters, NEUTRAL, LIKE1),
            Relation(BretoniaHunters, NEUTRAL, LIKE2),
            Relation(KusariHunters, NEUTRAL, LIKE1),
            Relation(BorderWorldHunters, NEUTRAL, LIKE1),

            Relation(RheinlandCivilians, FRIEND_MAX, LIKE2),
            Relation(LibertyCivilians, FRIEND_MAX, LIKE2),
            Relation(BretoniaCivilians, FRIEND_MAX, LIKE2),
            Relation(KusariCivilians, FRIEND_MAX, LIKE2),

            Relation(RheinlandTraders, FRIEND_MAX, LIKE2),
            Relation(LibertyTraders, FRIEND_MAX, LIKE3),
            Relation(BretoniaTraders, FRIEND_MAX, LIKE2),
            Relation(KusariTraders, FRIEND_MAX, LIKE2),
            Relation(BorderWorldTraders, NEUTRAL, LIKE2),

            Relation(RheinlandPirate, ENEMY_MAX, HATE3),
            Relation(LibertyPirate, ENEMY_MAX, HATE5),
            Relation(BretoniaPirate, ENEMY_MAX, HATE3),
            Relation(KusariPirate, ENEMY_MAX, HATE2),
            Relation(BorderWorldPirate, ENEMY_MAX, HATE1),

            Relation(Corsairs, ENEMY_MED, HATE6),
            Relation(Outcasts, NEUTRAL),

            Relation(Hessians, ENEMY_MED, HATE3),
            Relation(Junkers, ENEMY_MIN, HATE2),
            Relation(LibertyRogues, ENEMY_MED, HATE7),
            Relation(Starline, ENEMY_MED, HATE2),
            Relation(LaneHackers, ENEMY_MED, HATE8),
            Relation(Xenos, ENEMY_MED, HATE7),
            Relation(Ireland, ENEMY_MED, HATE4),
            Relation(Shinobi, ENEMY_MED, HATE2),
            Relation(FarmerAlliance, ENEMY_MED, HATE1),

            Relation(Nomad, ENEMY_MAX),
        ]
    ),

    FactionRelation(
        KusariMain,
        [
            Relation(RheinlandMain, FRIEND_MAX),
            Relation(LibertyMain, FRIEND_MAX),
            Relation(BretoniaMain, FRIEND_MAX),
            Relation(KusariMain, FRIEND_MAX),

            Relation(RheinlandHunters, NEUTRAL, LIKE1),
            Relation(LibertyHunters, NEUTRAL, LIKE1),
            Relation(BretoniaHunters, NEUTRAL, LIKE1),
            Relation(KusariHunters, NEUTRAL, LIKE2),
            Relation(BorderWorldHunters, NEUTRAL, LIKE1),

            Relation(RheinlandCivilians, FRIEND_MAX, LIKE2),
            Relation(LibertyCivilians, FRIEND_MAX, LIKE2),
            Relation(BretoniaCivilians, FRIEND_MAX, LIKE2),
            Relation(KusariCivilians, FRIEND_MAX, LIKE4),

            Relation(RheinlandTraders, FRIEND_MAX, LIKE2),
            Relation(LibertyTraders, FRIEND_MAX, LIKE2),
            Relation(BretoniaTraders, FRIEND_MAX, LIKE2),
            Relation(KusariTraders, FRIEND_MAX, LIKE3),
            Relation(BorderWorldTraders, NEUTRAL, LIKE2),

            Relation(RheinlandPirate, ENEMY_MAX, HATE3),
            Relation(LibertyPirate, ENEMY_MAX, HATE2),
            Relation(BretoniaPirate, ENEMY_MAX, HATE3),
            Relation(KusariPirate, ENEMY_MAX, HATE5),
            Relation(BorderWorldPirate, ENEMY_MAX, HATE2),

            Relation(Corsairs, ENEMY_MED, HATE6),
            Relation(Outcasts, NEUTRAL),

            Relation(Hessians, ENEMY_MED, HATE5),
            Relation(Junkers, ENEMY_MIN, HATE2),
            Relation(LibertyRogues, ENEMY_MED, HATE1),
            Relation(Starline, ENEMY_MED, HATE1),
            Relation(LaneHackers, ENEMY_MED, HATE4),
            Relation(Xenos, ENEMY_MED, HATE8),
            Relation(Ireland, ENEMY_MED, HATE5),
            Relation(Shinobi, ENEMY_MED, HATE7),
            Relation(FarmerAlliance, ENEMY_MED, HATE9),

            Relation(Nomad, ENEMY_MAX),
        ]
    ),

    ### HUNTERS

    FactionRelation(
        RheinlandHunters,
        [
            Relation(RheinlandMain, NEUTRAL, LIKE1),
            Relation(LibertyMain, NEUTRAL, LIKE1),
            Relation(BretoniaMain, NEUTRAL, LIKE1),
            Relation(KusariMain, NEUTRAL, LIKE1),

            Relation(RheinlandHunters, NEUTRAL, LIKE2),
            Relation(LibertyHunters, NEUTRAL, LIKE2),
            Relation(BretoniaHunters, NEUTRAL, LIKE2),
            Relation(KusariHunters, NEUTRAL, LIKE2),
            Relation(BorderWorldHunters, NEUTRAL, LIKE1),

            Relation(RheinlandCivilians, FRIEND_MAX),
            Relation(LibertyCivilians, FRIEND_MAX),
            Relation(BretoniaCivilians, FRIEND_MAX),
            Relation(KusariCivilians, FRIEND_MAX),

            Relation(RheinlandTraders, FRIEND_MAX),
            Relation(LibertyTraders, FRIEND_MAX),
            Relation(BretoniaTraders, FRIEND_MAX),
            Relation(KusariTraders, FRIEND_MAX),
            Relation(BorderWorldTraders, NEUTRAL),

            Relation(RheinlandPirate, ENEMY_MAX),
            Relation(LibertyPirate, ENEMY_MAX),
            Relation(BretoniaPirate, ENEMY_MAX),
            Relation(KusariPirate, ENEMY_MAX),
            Relation(BorderWorldPirate, ENEMY_MAX),

            Relation(Corsairs, ENEMY_MED, HATE5),
            Relation(Outcasts, ENEMY_MED, HATE2),

            Relation(Hessians, ENEMY_MED, HATE4),
            Relation(Junkers, ENEMY_MIN, HATE2),
            Relation(LibertyRogues, ENEMY_MED, HATE4),
            Relation(Starline, ENEMY_MED, HATE4),
            Relation(LaneHackers, ENEMY_MED, HATE4),
            Relation(Xenos, ENEMY_MED, HATE6),
            Relation(Ireland, ENEMY_MED, HATE4),
            Relation(Shinobi, ENEMY_MED, HATE4),
            Relation(FarmerAlliance, ENEMY_MED, HATE4),

            Relation(Nomad, ENEMY_MAX),
        ]
    ),

    FactionRelation(
        LibertyHunters,
        [
            Relation(RheinlandMain, NEUTRAL, LIKE1),
            Relation(LibertyMain, NEUTRAL, LIKE1),
            Relation(BretoniaMain, NEUTRAL, LIKE1),
            Relation(KusariMain, NEUTRAL, LIKE1),

            Relation(RheinlandHunters, NEUTRAL, LIKE2),
            Relation(LibertyHunters, NEUTRAL, LIKE2),
            Relation(BretoniaHunters, NEUTRAL, LIKE2),
            Relation(KusariHunters, NEUTRAL, LIKE2),
            Relation(BorderWorldHunters, NEUTRAL, LIKE1),

            Relation(RheinlandCivilians, FRIEND_MAX),
            Relation(LibertyCivilians, FRIEND_MAX),
            Relation(BretoniaCivilians, FRIEND_MAX),
            Relation(KusariCivilians, FRIEND_MAX),

            Relation(RheinlandTraders, FRIEND_MAX),
            Relation(LibertyTraders, FRIEND_MAX),
            Relation(BretoniaTraders, FRIEND_MAX),
            Relation(KusariTraders, FRIEND_MAX),
            Relation(BorderWorldTraders, NEUTRAL),

            Relation(RheinlandPirate, ENEMY_MAX),
            Relation(LibertyPirate, ENEMY_MAX),
            Relation(BretoniaPirate, ENEMY_MAX),
            Relation(KusariPirate, ENEMY_MAX),
            Relation(BorderWorldPirate, ENEMY_MAX),

            Relation(Corsairs, ENEMY_MED, HATE5),
            Relation(Outcasts, ENEMY_MED, HATE2),

            Relation(Hessians, ENEMY_MED, HATE4),
            Relation(Junkers, ENEMY_MIN, HATE2),
            Relation(LibertyRogues, ENEMY_MED, HATE4),
            Relation(Starline, ENEMY_MED, HATE4),
            Relation(LaneHackers, ENEMY_MED, HATE4),
            Relation(Xenos, ENEMY_MED, HATE6),
            Relation(Ireland, ENEMY_MED, HATE4),
            Relation(Shinobi, ENEMY_MED, HATE4),
            Relation(FarmerAlliance, ENEMY_MED, HATE4),

            Relation(Nomad, ENEMY_MAX),
        ]
    ),

    FactionRelation(
        BretoniaHunters,
        [
            Relation(RheinlandMain, NEUTRAL, LIKE1),
            Relation(LibertyMain, NEUTRAL, LIKE1),
            Relation(BretoniaMain, NEUTRAL, LIKE1),
            Relation(KusariMain, NEUTRAL, LIKE1),

            Relation(RheinlandHunters, NEUTRAL, LIKE2),
            Relation(LibertyHunters, NEUTRAL, LIKE2),
            Relation(BretoniaHunters, NEUTRAL, LIKE2),
            Relation(KusariHunters, NEUTRAL, LIKE2),
            Relation(BorderWorldHunters, NEUTRAL, LIKE1),

            Relation(RheinlandCivilians, FRIEND_MAX),
            Relation(LibertyCivilians, FRIEND_MAX),
            Relation(BretoniaCivilians, FRIEND_MAX),
            Relation(KusariCivilians, FRIEND_MAX),

            Relation(RheinlandTraders, FRIEND_MAX),
            Relation(LibertyTraders, FRIEND_MAX),
            Relation(BretoniaTraders, FRIEND_MAX),
            Relation(KusariTraders, FRIEND_MAX),
            Relation(BorderWorldTraders, NEUTRAL),

            Relation(RheinlandPirate, ENEMY_MAX),
            Relation(LibertyPirate, ENEMY_MAX),
            Relation(BretoniaPirate, ENEMY_MAX),
            Relation(KusariPirate, ENEMY_MAX),
            Relation(BorderWorldPirate, ENEMY_MAX),

            Relation(Corsairs, ENEMY_MED, HATE5),
            Relation(Outcasts, ENEMY_MED, HATE2),

            Relation(Hessians, ENEMY_MED, HATE4),
            Relation(Junkers, ENEMY_MIN, HATE2),
            Relation(LibertyRogues, ENEMY_MED, HATE4),
            Relation(Starline, ENEMY_MED, HATE4),
            Relation(LaneHackers, ENEMY_MED, HATE4),
            Relation(Xenos, ENEMY_MED, HATE6),
            Relation(Ireland, ENEMY_MED, HATE4),
            Relation(Shinobi, ENEMY_MED, HATE4),
            Relation(FarmerAlliance, ENEMY_MED, HATE4),

            Relation(Nomad, ENEMY_MAX),
        ]
    ),

    FactionRelation(
        KusariHunters,
        [
            Relation(RheinlandMain, NEUTRAL, LIKE1),
            Relation(LibertyMain, NEUTRAL, LIKE1),
            Relation(BretoniaMain, NEUTRAL, LIKE1),
            Relation(KusariMain, NEUTRAL, LIKE1),

            Relation(RheinlandHunters, NEUTRAL, LIKE2),
            Relation(LibertyHunters, NEUTRAL, LIKE2),
            Relation(BretoniaHunters, NEUTRAL, LIKE2),
            Relation(KusariHunters, NEUTRAL, LIKE2),

            Relation(RheinlandCivilians, FRIEND_MAX),
            Relation(LibertyCivilians, FRIEND_MAX),
            Relation(BretoniaCivilians, FRIEND_MAX),
            Relation(KusariCivilians, FRIEND_MAX),

            Relation(RheinlandTraders, FRIEND_MAX),
            Relation(LibertyTraders, FRIEND_MAX),
            Relation(BretoniaTraders, FRIEND_MAX),
            Relation(KusariTraders, FRIEND_MAX),
            Relation(BorderWorldTraders, NEUTRAL),

            Relation(RheinlandPirate, ENEMY_MAX),
            Relation(LibertyPirate, ENEMY_MAX),
            Relation(BretoniaPirate, ENEMY_MAX),
            Relation(KusariPirate, ENEMY_MAX),
            Relation(BorderWorldPirate, ENEMY_MAX),

            Relation(Corsairs, ENEMY_MED, HATE5),
            Relation(Outcasts, ENEMY_MED, HATE2),

            Relation(Hessians, ENEMY_MED, HATE4),
            Relation(Junkers, ENEMY_MIN, HATE2),
            Relation(LibertyRogues, ENEMY_MED, HATE4),
            Relation(Starline, ENEMY_MED, HATE4),
            Relation(LaneHackers, ENEMY_MED, HATE4),
            Relation(Xenos, ENEMY_MED, HATE6),
            Relation(Ireland, ENEMY_MED, HATE4),
            Relation(Shinobi, ENEMY_MED, HATE4),
            Relation(FarmerAlliance, ENEMY_MED, HATE4),

            Relation(Nomad, ENEMY_MAX),
        ]
    ),

    FactionRelation(
        BorderWorldHunters,
        [
            Relation(RheinlandMain, NEUTRAL, LIKE1),
            Relation(LibertyMain, NEUTRAL, LIKE1),
            Relation(BretoniaMain, NEUTRAL, LIKE1),
            Relation(KusariMain, NEUTRAL, LIKE1),

            Relation(RheinlandHunters, NEUTRAL, LIKE2),
            Relation(LibertyHunters, NEUTRAL, LIKE2),
            Relation(BretoniaHunters, NEUTRAL, LIKE2),
            Relation(KusariHunters, NEUTRAL, LIKE2),

            Relation(RheinlandCivilians, FRIEND_MAX),
            Relation(LibertyCivilians, FRIEND_MAX),
            Relation(BretoniaCivilians, FRIEND_MAX),
            Relation(KusariCivilians, FRIEND_MAX),

            Relation(RheinlandTraders, FRIEND_MAX),
            Relation(LibertyTraders, FRIEND_MAX),
            Relation(BretoniaTraders, FRIEND_MAX),
            Relation(KusariTraders, FRIEND_MAX),
            Relation(BorderWorldTraders, NEUTRAL),

            Relation(RheinlandPirate, ENEMY_MAX),
            Relation(LibertyPirate, ENEMY_MAX),
            Relation(BretoniaPirate, ENEMY_MAX),
            Relation(KusariPirate, ENEMY_MAX),
            Relation(BorderWorldPirate, ENEMY_MAX),

            Relation(Corsairs, ENEMY_MED, HATE5),
            Relation(Outcasts, ENEMY_MED, HATE2),

            Relation(Hessians, ENEMY_MED, HATE4),
            Relation(Junkers, ENEMY_MIN, HATE2),
            Relation(LibertyRogues, ENEMY_MED, HATE4),
            Relation(Starline, ENEMY_MED, HATE4),
            Relation(LaneHackers, ENEMY_MED, HATE4),
            Relation(Xenos, ENEMY_MED, HATE6),
            Relation(Ireland, ENEMY_MED, HATE4),
            Relation(Shinobi, ENEMY_MED, HATE4),
            Relation(FarmerAlliance, ENEMY_MED, HATE4),

            Relation(Nomad, ENEMY_MAX),
        ]
    ),

    ### CIVILIANS

    FactionRelation(
        RheinlandCivilians,
        [
            Relation(RheinlandMain, FRIEND_MAX),
            Relation(LibertyMain, FRIEND_MAX),
            Relation(BretoniaMain, FRIEND_MAX),
            Relation(KusariMain, FRIEND_MAX),

            Relation(RheinlandHunters, NEUTRAL, LIKE2),
            Relation(LibertyHunters, NEUTRAL, LIKE1),
            Relation(BretoniaHunters, NEUTRAL, LIKE1),
            Relation(KusariHunters, NEUTRAL, LIKE1),

            Relation(RheinlandCivilians, FRIEND_MAX, LIKE4),
            Relation(LibertyCivilians, FRIEND_MAX, LIKE2),
            Relation(BretoniaCivilians, FRIEND_MAX, LIKE2),
            Relation(KusariCivilians, FRIEND_MAX, LIKE2),

            Relation(RheinlandTraders, FRIEND_MAX, LIKE3),
            Relation(LibertyTraders, FRIEND_MAX, LIKE2),
            Relation(BretoniaTraders, FRIEND_MAX, LIKE2),
            Relation(KusariTraders, FRIEND_MAX, LIKE2),
            Relation(BorderWorldTraders, NEUTRAL, LIKE2),

            Relation(RheinlandPirate, ENEMY_MAX, HATE5),
            Relation(LibertyPirate, ENEMY_MAX, HATE3),
            Relation(BretoniaPirate, ENEMY_MAX, HATE2),
            Relation(KusariPirate, ENEMY_MAX, HATE3),
            Relation(BorderWorldPirate, ENEMY_MAX, HATE1),

            Relation(Corsairs, ENEMY_MED, HATE3),
            Relation(Outcasts, NEUTRAL),

            Relation(Hessians, ENEMY_MED, HATE8),
            Relation(Junkers, ENEMY_MIN, HATE3),
            Relation(LibertyRogues, ENEMY_MED, HATE7),
            Relation(Starline, ENEMY_MED, HATE3),
            Relation(LaneHackers, ENEMY_MED, HATE6),
            Relation(Xenos, ENEMY_MED, HATE7),
            Relation(Ireland, ENEMY_MED, HATE3),
            Relation(Shinobi, ENEMY_MED, HATE5),
            Relation(FarmerAlliance, ENEMY_MED, HATE5),

            Relation(Nomad, ENEMY_MAX),
            Relation(DeidrichPeople, ENEMY_MAX),
        ]
    ),

    FactionRelation(
        LibertyCivilians,
        [
            Relation(RheinlandMain, FRIEND_MAX),
            Relation(LibertyMain, FRIEND_MAX),
            Relation(BretoniaMain, FRIEND_MAX),
            Relation(KusariMain, FRIEND_MAX),

            Relation(RheinlandHunters, NEUTRAL, LIKE1),
            Relation(LibertyHunters, NEUTRAL, LIKE2),
            Relation(BretoniaHunters, NEUTRAL, LIKE1),
            Relation(KusariHunters, NEUTRAL, LIKE1),

            Relation(RheinlandCivilians, FRIEND_MAX, LIKE2),
            Relation(LibertyCivilians, FRIEND_MAX, LIKE4),
            Relation(BretoniaCivilians, FRIEND_MAX, LIKE2),
            Relation(KusariCivilians, FRIEND_MAX, LIKE2),

            Relation(RheinlandTraders, FRIEND_MAX, LIKE2),
            Relation(LibertyTraders, FRIEND_MAX, LIKE3),
            Relation(BretoniaTraders, FRIEND_MAX, LIKE2),
            Relation(KusariTraders, FRIEND_MAX, LIKE2),
            Relation(BorderWorldTraders, NEUTRAL, LIKE2),

            Relation(RheinlandPirate, ENEMY_MAX, HATE3),
            Relation(LibertyPirate, ENEMY_MAX, HATE5),
            Relation(BretoniaPirate, ENEMY_MAX, HATE3),
            Relation(KusariPirate, ENEMY_MAX, HATE2),
            Relation(BorderWorldPirate, ENEMY_MAX, HATE1),

            Relation(Corsairs, ENEMY_MED, HATE3),
            Relation(Outcasts, NEUTRAL),

            Relation(Hessians, ENEMY_MED, HATE3),
            Relation(Junkers, ENEMY_MIN, HATE2),
            Relation(LibertyRogues, ENEMY_MED, HATE7),
            Relation(Starline, ENEMY_MED, HATE2),
            Relation(LaneHackers, ENEMY_MED, HATE8),
            Relation(Xenos, ENEMY_MED, HATE7),
            Relation(Ireland, ENEMY_MED, HATE4),
            Relation(Shinobi, ENEMY_MED, HATE2),
            Relation(FarmerAlliance, ENEMY_MED, HATE1),

            Relation(Nomad, ENEMY_MAX),
        ]
    ),

    FactionRelation(
        BretoniaCivilians,
        [
            Relation(RheinlandMain, FRIEND_MAX),
            Relation(LibertyMain, FRIEND_MAX),
            Relation(BretoniaMain, FRIEND_MAX),
            Relation(KusariMain, FRIEND_MAX),

            Relation(RheinlandHunters, NEUTRAL, LIKE1),
            Relation(LibertyHunters, NEUTRAL, LIKE1),
            Relation(BretoniaHunters, NEUTRAL, LIKE2),
            Relation(KusariHunters, NEUTRAL, LIKE1),

            Relation(RheinlandCivilians, FRIEND_MAX, LIKE2),
            Relation(LibertyCivilians, FRIEND_MAX, LIKE2),
            Relation(BretoniaCivilians, FRIEND_MAX, LIKE2),
            Relation(KusariCivilians, FRIEND_MAX, LIKE2),

            Relation(RheinlandTraders, FRIEND_MAX, LIKE2),
            Relation(LibertyTraders, FRIEND_MAX, LIKE3),
            Relation(BretoniaTraders, FRIEND_MAX, LIKE2),
            Relation(KusariTraders, FRIEND_MAX, LIKE2),
            Relation(BorderWorldTraders, NEUTRAL, LIKE2),

            Relation(RheinlandPirate, ENEMY_MAX, HATE3),
            Relation(LibertyPirate, ENEMY_MAX, HATE5),
            Relation(BretoniaPirate, ENEMY_MAX, HATE3),
            Relation(KusariPirate, ENEMY_MAX, HATE2),
            Relation(BorderWorldPirate, ENEMY_MAX, HATE1),

            Relation(Corsairs, ENEMY_MED, HATE3),
            Relation(Outcasts, NEUTRAL),

            Relation(Hessians, ENEMY_MED, HATE3),
            Relation(Junkers, ENEMY_MIN, HATE2),
            Relation(LibertyRogues, ENEMY_MED, HATE7),
            Relation(Starline, ENEMY_MED, HATE2),
            Relation(LaneHackers, ENEMY_MED, HATE8),
            Relation(Xenos, ENEMY_MED, HATE7),
            Relation(Ireland, ENEMY_MED, HATE4),
            Relation(Shinobi, ENEMY_MED, HATE2),
            Relation(FarmerAlliance, ENEMY_MED, HATE1),

            Relation(Nomad, ENEMY_MAX),
        ]
    ),

    FactionRelation(
        KusariCivilians,
        [
            Relation(RheinlandMain, FRIEND_MAX),
            Relation(LibertyMain, FRIEND_MAX),
            Relation(BretoniaMain, FRIEND_MAX),
            Relation(KusariMain, FRIEND_MAX),

            Relation(RheinlandHunters, NEUTRAL, LIKE1),
            Relation(LibertyHunters, NEUTRAL, LIKE1),
            Relation(BretoniaHunters, NEUTRAL, LIKE1),
            Relation(KusariHunters, NEUTRAL, LIKE2),

            Relation(RheinlandCivilians, FRIEND_MAX, LIKE2),
            Relation(LibertyCivilians, FRIEND_MAX, LIKE2),
            Relation(BretoniaCivilians, FRIEND_MAX, LIKE2),
            Relation(KusariCivilians, FRIEND_MAX, LIKE4),

            Relation(RheinlandTraders, FRIEND_MAX, LIKE2),
            Relation(LibertyTraders, FRIEND_MAX, LIKE2),
            Relation(BretoniaTraders, FRIEND_MAX, LIKE2),
            Relation(KusariTraders, FRIEND_MAX, LIKE3),
            Relation(BorderWorldTraders, NEUTRAL, LIKE2),

            Relation(RheinlandPirate, ENEMY_MAX, HATE3),
            Relation(LibertyPirate, ENEMY_MAX, HATE2),
            Relation(BretoniaPirate, ENEMY_MAX, HATE3),
            Relation(KusariPirate, ENEMY_MAX, HATE5),
            Relation(BorderWorldPirate, ENEMY_MAX, HATE2),

            Relation(Corsairs, ENEMY_MED, HATE3),
            Relation(Outcasts, NEUTRAL),

            Relation(Hessians, ENEMY_MED, HATE5),
            Relation(Junkers, ENEMY_MIN, HATE2),
            Relation(LibertyRogues, ENEMY_MED, HATE1),
            Relation(Starline, ENEMY_MED, HATE1),
            Relation(LaneHackers, ENEMY_MED, HATE4),
            Relation(Xenos, ENEMY_MED, HATE8),
            Relation(Ireland, ENEMY_MED, HATE5),
            Relation(Shinobi, ENEMY_MED, HATE7),
            Relation(FarmerAlliance, ENEMY_MED, HATE9),

            Relation(Nomad, ENEMY_MAX),
        ]
    ),

    ### TRADERS

    FactionRelation(
        RheinlandTraders,
        [
            Relation(RheinlandMain, FRIEND_MAX),
            Relation(LibertyMain, FRIEND_MAX),
            Relation(BretoniaMain, FRIEND_MAX),
            Relation(KusariMain, FRIEND_MAX),

            Relation(RheinlandHunters, NEUTRAL, LIKE2),
            Relation(LibertyHunters, NEUTRAL, LIKE1),
            Relation(BretoniaHunters, NEUTRAL, LIKE1),
            Relation(KusariHunters, NEUTRAL, LIKE1),

            Relation(RheinlandCivilians, FRIEND_MAX, LIKE4),
            Relation(LibertyCivilians, FRIEND_MAX, LIKE2),
            Relation(BretoniaCivilians, FRIEND_MAX, LIKE2),
            Relation(KusariCivilians, FRIEND_MAX, LIKE2),

            Relation(RheinlandTraders, FRIEND_MAX, LIKE3),
            Relation(LibertyTraders, FRIEND_MAX, LIKE2),
            Relation(BretoniaTraders, FRIEND_MAX, LIKE2),
            Relation(KusariTraders, FRIEND_MAX, LIKE2),
            Relation(BorderWorldTraders, NEUTRAL, LIKE2),

            Relation(RheinlandPirate, ENEMY_MAX, HATE5),
            Relation(LibertyPirate, ENEMY_MAX, HATE3),
            Relation(BretoniaPirate, ENEMY_MAX, HATE2),
            Relation(KusariPirate, ENEMY_MAX, HATE3),
            Relation(BorderWorldPirate, ENEMY_MAX, HATE1),

            Relation(Corsairs, ENEMY_MED, HATE3),
            Relation(Outcasts, NEUTRAL),

            Relation(Hessians, ENEMY_MED, HATE8),
            Relation(Junkers, ENEMY_MIN, HATE3),
            Relation(LibertyRogues, ENEMY_MED, HATE7),
            Relation(Starline, ENEMY_MED, HATE3),
            Relation(LaneHackers, ENEMY_MED, HATE6),
            Relation(Xenos, ENEMY_MED, HATE7),
            Relation(Ireland, ENEMY_MED, HATE3),
            Relation(Shinobi, ENEMY_MED, HATE5),
            Relation(FarmerAlliance, ENEMY_MED, HATE5),

            Relation(Nomad, ENEMY_MAX),
            Relation(DeidrichPeople, ENEMY_MAX),
        ]
    ),

    FactionRelation(
        LibertyTraders,
        [
            Relation(RheinlandMain, FRIEND_MAX),
            Relation(LibertyMain, FRIEND_MAX),
            Relation(BretoniaMain, FRIEND_MAX),
            Relation(KusariMain, FRIEND_MAX),

            Relation(RheinlandHunters, NEUTRAL, LIKE1),
            Relation(LibertyHunters, NEUTRAL, LIKE2),
            Relation(BretoniaHunters, NEUTRAL, LIKE1),
            Relation(KusariHunters, NEUTRAL, LIKE1),

            Relation(RheinlandCivilians, FRIEND_MAX, LIKE2),
            Relation(LibertyCivilians, FRIEND_MAX, LIKE4),
            Relation(BretoniaCivilians, FRIEND_MAX, LIKE2),
            Relation(KusariCivilians, FRIEND_MAX, LIKE2),

            Relation(RheinlandTraders, FRIEND_MAX, LIKE2),
            Relation(LibertyTraders, FRIEND_MAX, LIKE3),
            Relation(BretoniaTraders, FRIEND_MAX, LIKE2),
            Relation(KusariTraders, FRIEND_MAX, LIKE2),
            Relation(BorderWorldTraders, NEUTRAL, LIKE2),

            Relation(RheinlandPirate, ENEMY_MAX, HATE3),
            Relation(LibertyPirate, ENEMY_MAX, HATE5),
            Relation(BretoniaPirate, ENEMY_MAX, HATE3),
            Relation(KusariPirate, ENEMY_MAX, HATE2),
            Relation(BorderWorldPirate, ENEMY_MAX, HATE1),

            Relation(Corsairs, ENEMY_MED, HATE3),
            Relation(Outcasts, NEUTRAL),

            Relation(Hessians, ENEMY_MED, HATE3),
            Relation(Junkers, ENEMY_MIN, HATE2),
            Relation(LibertyRogues, ENEMY_MED, HATE7),
            Relation(Starline, ENEMY_MED, HATE2),
            Relation(LaneHackers, ENEMY_MED, HATE8),
            Relation(Xenos, ENEMY_MED, HATE7),
            Relation(Ireland, ENEMY_MED, HATE4),
            Relation(Shinobi, ENEMY_MED, HATE2),
            Relation(FarmerAlliance, ENEMY_MED, HATE1),

            Relation(Nomad, ENEMY_MAX),
        ]
    ),

    FactionRelation(
        BretoniaTraders,
        [
            Relation(RheinlandMain, FRIEND_MAX),
            Relation(LibertyMain, FRIEND_MAX),
            Relation(BretoniaMain, FRIEND_MAX),
            Relation(KusariMain, FRIEND_MAX),

            Relation(RheinlandHunters, NEUTRAL, LIKE1),
            Relation(LibertyHunters, NEUTRAL, LIKE1),
            Relation(BretoniaHunters, NEUTRAL, LIKE2),
            Relation(KusariHunters, NEUTRAL, LIKE1),

            Relation(RheinlandCivilians, FRIEND_MAX, LIKE2),
            Relation(LibertyCivilians, FRIEND_MAX, LIKE2),
            Relation(BretoniaCivilians, FRIEND_MAX, LIKE2),
            Relation(KusariCivilians, FRIEND_MAX, LIKE2),

            Relation(RheinlandTraders, FRIEND_MAX, LIKE2),
            Relation(LibertyTraders, FRIEND_MAX, LIKE3),
            Relation(BretoniaTraders, FRIEND_MAX, LIKE2),
            Relation(KusariTraders, FRIEND_MAX, LIKE2),
            Relation(BorderWorldTraders, NEUTRAL, LIKE2),

            Relation(RheinlandPirate, ENEMY_MAX, HATE3),
            Relation(LibertyPirate, ENEMY_MAX, HATE5),
            Relation(BretoniaPirate, ENEMY_MAX, HATE3),
            Relation(KusariPirate, ENEMY_MAX, HATE2),
            Relation(BorderWorldPirate, ENEMY_MAX, HATE1),

            Relation(Corsairs, ENEMY_MED, HATE3),
            Relation(Outcasts, NEUTRAL),

            Relation(Hessians, ENEMY_MED, HATE3),
            Relation(Junkers, ENEMY_MIN, HATE2),
            Relation(LibertyRogues, ENEMY_MED, HATE7),
            Relation(Starline, ENEMY_MED, HATE2),
            Relation(LaneHackers, ENEMY_MED, HATE8),
            Relation(Xenos, ENEMY_MED, HATE7),
            Relation(Ireland, ENEMY_MED, HATE4),
            Relation(Shinobi, ENEMY_MED, HATE2),
            Relation(FarmerAlliance, ENEMY_MED, HATE1),

            Relation(Nomad, ENEMY_MAX),
        ]
    ),

    FactionRelation(
        KusariTraders,
        [
            Relation(RheinlandMain, FRIEND_MAX),
            Relation(LibertyMain, FRIEND_MAX),
            Relation(BretoniaMain, FRIEND_MAX),
            Relation(KusariMain, FRIEND_MAX),

            Relation(RheinlandHunters, NEUTRAL, LIKE1),
            Relation(LibertyHunters, NEUTRAL, LIKE1),
            Relation(BretoniaHunters, NEUTRAL, LIKE1),
            Relation(KusariHunters, NEUTRAL, LIKE2),

            Relation(RheinlandCivilians, FRIEND_MAX, LIKE2),
            Relation(LibertyCivilians, FRIEND_MAX, LIKE2),
            Relation(BretoniaCivilians, FRIEND_MAX, LIKE2),
            Relation(KusariCivilians, FRIEND_MAX, LIKE4),

            Relation(RheinlandTraders, FRIEND_MAX, LIKE2),
            Relation(LibertyTraders, FRIEND_MAX, LIKE2),
            Relation(BretoniaTraders, FRIEND_MAX, LIKE2),
            Relation(KusariTraders, FRIEND_MAX, LIKE3),
            Relation(BorderWorldTraders, NEUTRAL, LIKE2),

            Relation(RheinlandPirate, ENEMY_MAX, HATE3),
            Relation(LibertyPirate, ENEMY_MAX, HATE2),
            Relation(BretoniaPirate, ENEMY_MAX, HATE3),
            Relation(KusariPirate, ENEMY_MAX, HATE5),
            Relation(BorderWorldPirate, ENEMY_MAX, HATE2),

            Relation(Corsairs, ENEMY_MED, HATE3),
            Relation(Outcasts, NEUTRAL),

            Relation(Hessians, ENEMY_MED, HATE5),
            Relation(Junkers, ENEMY_MIN, HATE2),
            Relation(LibertyRogues, ENEMY_MED, HATE1),
            Relation(Starline, ENEMY_MED, HATE1),
            Relation(LaneHackers, ENEMY_MED, HATE4),
            Relation(Xenos, ENEMY_MED, HATE8),
            Relation(Ireland, ENEMY_MED, HATE5),
            Relation(Shinobi, ENEMY_MED, HATE7),
            Relation(FarmerAlliance, ENEMY_MED, HATE9),

            Relation(Nomad, ENEMY_MAX),
        ]
    ),

    FactionRelation(
        BorderWorldTraders,
        [
            Relation(RheinlandMain, FRIEND_MAX),
            Relation(LibertyMain, FRIEND_MAX),
            Relation(BretoniaMain, FRIEND_MAX),
            Relation(KusariMain, FRIEND_MAX),

            Relation(RheinlandHunters, NEUTRAL, LIKE1),
            Relation(LibertyHunters, NEUTRAL, LIKE1),
            Relation(BretoniaHunters, NEUTRAL, LIKE1),
            Relation(KusariHunters, NEUTRAL, LIKE2),

            Relation(RheinlandCivilians, FRIEND_MAX, LIKE2),
            Relation(LibertyCivilians, FRIEND_MAX, LIKE2),
            Relation(BretoniaCivilians, FRIEND_MAX, LIKE2),
            Relation(KusariCivilians, FRIEND_MAX, LIKE4),

            Relation(RheinlandTraders, FRIEND_MAX, LIKE2),
            Relation(LibertyTraders, FRIEND_MAX, LIKE2),
            Relation(BretoniaTraders, FRIEND_MAX, LIKE2),
            Relation(KusariTraders, FRIEND_MAX, LIKE3),
            Relation(BorderWorldTraders, NEUTRAL, LIKE2),

            Relation(RheinlandPirate, ENEMY_MAX, HATE3),
            Relation(LibertyPirate, ENEMY_MAX, HATE2),
            Relation(BretoniaPirate, ENEMY_MAX, HATE3),
            Relation(KusariPirate, ENEMY_MAX, HATE5),
            Relation(BorderWorldPirate, ENEMY_MAX, HATE2),

            Relation(Corsairs, NEUTRAL),
            Relation(Outcasts, NEUTRAL),

            Relation(Hessians, ENEMY_MED, HATE5),
            Relation(Junkers, ENEMY_MIN, HATE2),
            Relation(LibertyRogues, ENEMY_MED, HATE1),
            Relation(Starline, ENEMY_MED, HATE1),
            Relation(LaneHackers, ENEMY_MED, HATE4),
            Relation(Xenos, ENEMY_MED, HATE8),
            Relation(Ireland, ENEMY_MED, HATE5),
            Relation(Shinobi, ENEMY_MED, HATE7),
            Relation(FarmerAlliance, ENEMY_MED, HATE9),

            Relation(Nomad, ENEMY_MAX),
        ]
    ),

    ###
    #
    # FactionRelation(
    #     Rheinland,
    #     [
    #         Relation(RheinlandMain, FRIEND_MAX),
    #         Relation(LibertyMain, FRIEND_MAX),
    #         Relation(BretoniaMain, FRIEND_MAX),
    #         Relation(KusariMain, FRIEND_MAX),
    #
    #         Relation(RheinlandHunters, NEUTRAL),
    #         Relation(LibertyHunters, NEUTRAL),
    #         Relation(BretoniaHunters, NEUTRAL),
    #         Relation(KusariHunters, NEUTRAL),
    #
    #         Relation(RheinlandCivilians, FRIEND_MAX),
    #         Relation(LibertyCivilians, FRIEND_MAX),
    #         Relation(BretoniaCivilians, FRIEND_MAX),
    #         Relation(KusariCivilians, FRIEND_MAX),
    #
    #         Relation(RheinlandTraders, FRIEND_MAX),
    #         Relation(LibertyTraders, FRIEND_MAX),
    #         Relation(BretoniaTraders, FRIEND_MAX),
    #         Relation(KusariTraders, FRIEND_MAX),
    #         Relation(BorderWorldTraders, NEUTRAL),
    #
    #         Relation(RheinlandPirate, ENEMY_MAX),
    #         Relation(LibertyPirate, ENEMY_MAX),
    #         Relation(BretoniaPirate, ENEMY_MAX),
    #         Relation(KusariPirate, ENEMY_MAX),
    #         Relation(BorderWorldPirate, ENEMY_MAX),
    #
    #         Relation(Corsairs, NEUTRAL),
    #         Relation(Outcasts, NEUTRAL),
    #
    #         Relation(Hessians, ENEMY_MED),
    #         Relation(Junkers, ENEMY_MIN),
    #         Relation(LibertyRogues, ENEMY_MED),
    #         Relation(Starline, ENEMY_MED),
    #         Relation(LaneHackers, ENEMY_MED),
    #         Relation(Xenos, ENEMY_MED),
    #         Relation(Ireland, ENEMY_MED),
    #         Relation(Shinobi, ENEMY_MED),
    #         Relation(FarmerAlliance, ENEMY_MED),
    #
    #         Relation(Nomad, ENEMY_MAX),
    #         Relation(DeidrichPeople, ENEMY_MAX),
    #     ]
    # ),

]
#
# FactionRelation(
#     LibertyMain,
#     [
#         Relation(RheinlandMain, FRIEND_MAX),
#         Relation(LibertyMain, FRIEND_MAX),
#         Relation(BretoniaMain, FRIEND_MAX),
#         Relation(KusariMain, FRIEND_MAX),
#
#         Relation(RheinlandHunters, NEUTRAL),
#         Relation(LibertyHunters, NEUTRAL),
#         Relation(BretoniaHunters, NEUTRAL),
#         Relation(KusariHunters, NEUTRAL),
#
#         Relation(RheinlandCivilians, FRIEND_MAX),
#         Relation(LibertyCivilians, FRIEND_MAX),
#         Relation(BretoniaCivilians, FRIEND_MAX),
#         Relation(KusariCivilians, FRIEND_MAX),
#
#         Relation(RheinlandTraders, FRIEND_MAX),
#         Relation(LibertyTraders, FRIEND_MAX),
#         Relation(BretoniaTraders, FRIEND_MAX),
#         Relation(KusariTraders, FRIEND_MAX),
#         Relation(BorderWorldTraders, NEUTRAL),
#
#         Relation(RheinlandPirate, ENEMY_MAX),
#         Relation(LibertyPirate, ENEMY_MAX),
#         Relation(BretoniaPirate, ENEMY_MAX),
#         Relation(KusariPirate, ENEMY_MAX),
#         Relation(BorderWorldPirate, ENEMY_MAX),
#
#         Relation(Corsairs, NEUTRAL),
#         Relation(Outcasts, NEUTRAL),
#
#         Relation(Hessians, ENEMY_MED),
#         Relation(Junkers, ENEMY_MIN),
#         Relation(LibertyRogues, ENEMY_MED),
#         Relation(Starline, ENEMY_MED),
#         Relation(LaneHackers, ENEMY_MED),
#         Relation(Xenos, ENEMY_MED),
#         Relation(Ireland, ENEMY_MED),
#         Relation(Shinobi, ENEMY_MED),
#         Relation(FarmerAlliance, ENEMY_MED),
#
#         Relation(Nomad, ENEMY_MAX),
#         Relation(DeidrichPeople, ENEMY_MAX),
#     ]
# ),