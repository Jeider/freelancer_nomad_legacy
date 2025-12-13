from fx.contrail import Contrail
from fx.light import Light

from world import gun
from world.equipment import MainMiscEquip as misc
from world import bodyparts
from world import ship

from world.names import DEFAULT_COMMS, RH_COMMS, LI_COMMS, BR_COMMS, KU_COMMS, GLOBAL_COMMS

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


OTHER_DEFAULTS = '''
rep = 0, ku_p_grp
rep = 0, gd_bh_grp
rep = 0, gd_z_grp
rep = 0, co_rs_grp
rep = 0, br_p_grp
rep = 0, fc_or_grp
rep = 0, co_shi_grp
rep = 0, fc_ln_grp
rep = 0, li_n_grp
rep = 0, fc_f_grp
rep = 0, fc_h_grp
rep = 0, fc_q_grp
rep = 0, co_ss_grp
rep = 0, co_khc_grp
rep = 0, fc_m_grp
rep = 0, fc_lh_grp
rep = 0, co_vr_grp
rep = 0, fc_c_grp
rep = 0, rh_m_grp
rep = 0, co_be_grp
rep = 0, co_alg_grp
rep = 0, fc_lr_grp
rep = 0, fc_fa_grp
rep = 0, co_hsp_grp
rep = 0, rh_n_grp
rep = 0, co_me_grp
rep = 0, li_p_grp
rep = 0, br_m_grp
rep = 0, co_ic_grp
rep = 0, fc_x_grp
rep = 0, fc_gc_grp
rep = 0, fc_lwb_grp
rep = 0, ku_n_grp
rep = 0, fc_ou_grp
rep = 0, fc_bd_grp
rep = 0, fc_b_grp
rep = 0, br_n_grp
rep = 0, fc_rn_grp
rep = 0, co_nws_grp
rep = 0, fc_u_grp
rep = 0, co_os_grp
rep = 0, co_kt_grp
rep = 0, gd_im_grp
rep = 0, co_ni_grp
rep = 0, rh_p_grp
rep = 0, fc_g_grp
rep = 0, co_ti_grp
rep = 0, fc_kn_grp
rep = 0, fc_ouk_grp
rep = 0, fc_rh_grp
rep = 0, fc_j_grp
rep = 0, gd_gm_grp
rep = 0, li_lsf_grp
'''

LIFTER = 'rc_grp_lifter'

RU_VOICES_LEGAL = '''
voice = pilot01
voice = pilot02
voice = pilot03
voice = pilot04
voice = pilot05
'''

RU_VOICES_PIRATE = '''
voice = pilot06
voice = pilot07
voice = pilot08
voice = pilot09
'''

EN_VOICES_LEGAL = '''
voice = pilot_f_mil_m01_new
voice = pilot_f_mil_m02_new
voice = pilot_f_leg_f01_new
'''

EN_VOICES_PIRATE = '''
voice = pilot_f_ill_m01_new
voice = pilot_f_ill_m02_new
voice = pilot_f_leg_f01_new
'''

SCAN_CARGO = '''
scan_for_cargo = commodity_alien_artifacts, 1
scan_for_cargo = commodity_cardamine, 2
scan_announce = false
scan_chance = 0.300000
'''

FORMATIONS = '''
formation = fighters, fighter_basic
formation = freighters, freighter_rheinland
formation = freighters2, freighter2_rheinland
formation = transports, transport_rheinland
formation = transports2, transport2_rheinland
formation = gunboats, armored_basic
'''

RANKS_LIBERTY = '''
firstname_male = 226608, 226741
firstname_female = 226808, 226952
lastname = 227008, 227307
rank_desig = 197008, 197009, 197010, 3, 4
formation_desig = 197808, 197820
large_ship_desig = 196977
large_ship_names = 202608, 202647
'''

RANKS_BRETONIA = '''
firstname_male = 227308, 227410
firstname_female = 227508, 227575
lastname = 227708, 228007
rank_desig = 197011, 197012, 197013, 8, 10
formation_desig = 197808, 197820
large_ship_desig = 196978
large_ship_names = 202708, 202747
'''

RANKS_KUSARI = '''
firstname_male = 228708, 228807
firstname_female = 228808, 228890
lastname = 228908, 229207
rank_desig = 197017, 197018, 197019, 9, 11
formation_desig = 197829, 197836
large_ship_desig = 196980
large_ship_names = 202808, 202847
'''

RANKS_RHEINLAND = '''
firstname_male = 228008, 228207
firstname_female = 228208, 228407
lastname = 228408, 228663
rank_desig = 197023, 197024, 197025, 12, 13
formation_desig = 197808, 197820
large_ship_desig = 196982
large_ship_names = 202908, 202947
'''

RANKS_HISPANIA = '''
firstname_male = 229208, 229248
firstname_female = 229308, 229340
lastname = 229408, 229459
rank_desig = 197080, 197081, 197082, 10, 15
formation_desig = 197808, 197820
'''

RANKS_UNKNOWN = '''
firstname_male = 229609, 229609
lastname = 229608, 229608
rank_desig = 197140, 197140, 197140, 10, 15
formation_desig = 197808, 197820
'''

COMM_LIBERTY = '''
space_costume = li_captain_head, li_male_elite_body, {helmet1}
space_costume = li_rockford_head, li_male_elite_body, {helmet2}
space_costume = li_sales_head_hat, li_male_elite_body, {helmet1}
space_costume = ge_male4_head, li_male_elite_body, {helmet2}
space_costume = pl_male2_head, li_male_elite_body, {helmet1}
space_costume = ge_male3_head, li_male_elite_body, {helmet2}
space_costume = li_newscaster_head_gen_hat, li_female_elite_body, {helmet1}_female
space_costume = li_newscaster_head_gen_hat, li_female_elite_body, {helmet2}_female
space_costume = br_newscaster_head_gen_hat, li_female_elite_body, {helmet1}_female
space_costume = br_newscaster_head_gen_hat, li_female_elite_body, {helmet2}_female
space_costume = pl_female2_head, li_female_elite_body, {helmet1}_female
space_costume = pl_female2_head, li_female_elite_body, {helmet2}_female
'''

COMM_BRETONIA = '''
space_costume = br_bartender_head, br_male_elite_body, {helmet1}
space_costume = br_quigly_head, br_male_elite_body, {helmet2}
space_costume = br_sales_head_hat, br_male_elite_body, {helmet1}
space_costume = ge_male1_head, br_male_elite_body, {helmet2}
space_costume = pl_male5_head, br_male_elite_body, {helmet1}
space_costume = sc_scientist2_head_hat, br_male_elite_body, {helmet2}
space_costume = br_newscaster_head_gen_hat, br_female_elite_body, {helmet1}_female
space_costume = br_newscaster_head_gen_hat, br_female_elite_body, {helmet2}_female
space_costume = rh_newscaster_head_gen_hat, br_female_elite_body, {helmet1}_female
space_costume = rh_newscaster_head_gen_hat, br_female_elite_body, {helmet2}_female
space_costume = pl_female2_head, br_female_elite_body, {helmet1}_female
space_costume = pl_female2_head, br_female_elite_body, {helmet2}_female
'''

COMM_KUSARI = '''
space_costume = ku_bartender_head_hat, ku_male_elite_body, {helmet1}
space_costume = ku_captain_head, ku_male_elite_body, {helmet2}
space_costume = ku_bartender_head_hat, ku_male_elite_body, {helmet1}
space_costume = ku_captain_head, ku_male_elite_body, {helmet2}
space_costume = ku_bartender_head_hat, ku_male_elite_body, {helmet1}
space_costume = ku_captain_head, ku_male_elite_body, {helmet2}
space_costume = ku_newscaster_head_gen, ku_female_elite_body, {helmet1}_female
space_costume = ku_newscaster_head_gen, ku_female_elite_body, {helmet2}_female
space_costume = ku_newscaster_head_gen, ku_female_elite_body, {helmet1}_female
space_costume = ku_newscaster_head_gen, ku_female_elite_body, {helmet2}_female
space_costume = ku_newscaster_head_gen, ku_female_elite_body, {helmet1}_female
space_costume = ku_newscaster_head_gen, ku_female_elite_body, {helmet2}_female
'''

COMM_RHEINLAND = '''
space_costume = rh_bartender_head, rh_male_elite_body, {helmet1}
space_costume = rh_captain_head, rh_male_elite_body, {helmet2}
space_costume = rh_sales_head, rh_male_elite_body, {helmet1}
space_costume = rh_wilham_head, rh_male_elite_body, {helmet2}
space_costume = ge_male6_head, rh_male_elite_body, {helmet1}
space_costume = sc_scientist1_head_hat, rh_male_elite_body, {helmet2}
space_costume = li_newscaster_head_gen_hat, rh_female_elite_body, {helmet1}_female
space_costume = li_newscaster_head_gen_hat, rh_female_elite_body, {helmet2}_female
space_costume = br_newscaster_head_gen_hat, rh_female_elite_body, {helmet1}_female
space_costume = br_newscaster_head_gen_hat, rh_female_elite_body, {helmet2}_female
space_costume = rh_newscaster_head_gen_hat, rh_female_elite_body, {helmet1}_female
space_costume = rh_newscaster_head_gen_hat, rh_female_elite_body, {helmet2}_female
'''

COMM_HISPANIA = '''
space_costume = pi_pirate1_head, pi_pirate3_body, {helmet1}
space_costume = pi_pirate2_head, pi_pirate3_body, {helmet2}
space_costume = pi_pirate4_head, pi_pirate3_body, {helmet1}
space_costume = sh_male4_head, pi_pirate3_body, {helmet2}
space_costume = ge_male4_head, pi_pirate3_body, {helmet1}
space_costume = ge_male1_head, pi_pirate3_body, {helmet2}
space_costume = li_newscaster_head_gen_hat, sh_female1_body, {helmet1}_female
space_costume = li_newscaster_head_gen_hat, sh_female1_body, {helmet2}_female
space_costume = rh_newscaster_head_gen_hat, sh_female1_body, {helmet1}_female
space_costume = rh_newscaster_head_gen_hat, sh_female1_body, {helmet2}_female
space_costume = pl_female2_head, sh_female1_body, {helmet1}_female
space_costume = pl_female2_head, sh_female1_body, {helmet2}_female
'''

COMM_JOURNEYMAN = '''
space_costume = pl_male2_head, sh_male2_body, {helmet1}
space_costume = pl_male3_head_hat, sh_male2_body, {helmet2}
space_costume = pl_male6_head, sh_male2_body, {helmet1}
space_costume = pl_male8_head_hat, sh_male2_body, {helmet2}
space_costume = ge_male6_head, sh_male2_body, {helmet1}
space_costume = sc_scientist2_head_hat, sh_male2_body, {helmet2}
space_costume = li_newscaster_head_gen_hat, pl_female2_journeyman_body, {helmet1}_female
space_costume = li_newscaster_head_gen_hat, pl_female2_journeyman_body, {helmet2}_female
space_costume = rh_newscaster_head_gen_hat, pl_female2_journeyman_body, {helmet1}_female
space_costume = rh_newscaster_head_gen_hat, pl_female2_journeyman_body, {helmet2}_female
space_costume = pl_female2_head, pl_female2_journeyman_body, {helmet1}_female
space_costume = pl_female2_head, pl_female2_journeyman_body, {helmet2}_female
'''

COMM_PEASANT = '''
space_costume = pl_male3_head_hat, pl_male1_peasant_body, {helmet1}
space_costume = pl_male5_head, pl_male1_peasant_body, {helmet2}
space_costume = pl_male8_head_hat, pl_male1_peasant_body, {helmet1}
space_costume = ge_male3_head, pl_male1_peasant_body, {helmet2}
space_costume = ge_male6_head, pl_male1_peasant_body, {helmet1}
space_costume = sc_scientist2_head_hat, pl_male1_peasant_body, {helmet2}
space_costume = li_newscaster_head_gen_hat, pl_female1_journeyman_body, {helmet1}_female
space_costume = li_newscaster_head_gen_hat, pl_female1_journeyman_body, {helmet2}_female
space_costume = rh_newscaster_head_gen_hat, pl_female1_journeyman_body, {helmet1}_female
space_costume = rh_newscaster_head_gen_hat, pl_female1_journeyman_body, {helmet2}_female
space_costume = pl_female2_head, pl_female1_journeyman_body, {helmet1}_female
space_costume = pl_female2_head, pl_female1_journeyman_body, {helmet2}_female
'''

COMM_ORDER = '''
space_costume = pi_pirate1_head, pi_orillion_body, {helmet1}
space_costume = pi_pirate4_head, pi_orillion_body, {helmet2}
space_costume = sh_male4_head, pi_orillion_body, {helmet1}
space_costume = ge_male2_head, pi_orillion_body, {helmet2}
space_costume = ge_male4_head, pi_orillion_body, {helmet1}
space_costume = ge_male1_head, pi_orillion_body, {helmet2}
space_costume = li_newscaster_head_gen_hat, pl_female2_journeyman_body, {helmet1}_female
space_costume = li_newscaster_head_gen_hat, pl_female2_journeyman_body, {helmet2}_female
space_costume = rh_newscaster_head_gen_hat, pl_female2_journeyman_body, {helmet1}_female
space_costume = rh_newscaster_head_gen_hat, pl_female2_journeyman_body, {helmet2}_female
space_costume = pl_female2_head, pl_female2_journeyman_body, {helmet1}_female
space_costume = pl_female2_head, pl_female2_journeyman_body, {helmet2}_female
'''


class LoadedRelation:
    def __init__(self, faction, init_reputation=NEUTRAL):
        self.faction = faction
        self.reputation: float = init_reputation
        self.empathy: float = NEUTRAL

    def get_reputation(self):
        return self.reputation

    def get_empathy(self):
        return self.empathy

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
    FREIGHTER = None
    RU_NAME = None
    RU_NAME_FULL = None
    FORCE_IDS_NAME = None
    FORCE_IDS_SHORT_NAME = None
    FORCE_IDS_INFO = None
    DEFAULT_REPUTATION = NEUTRAL
    SCANNING_CARGO = False
    IS_PIRATE = False
    IS_MILITARY = False
    IS_CIVILIAN = False
    RANDOM_MISSIONS = True

    COMMODITY = DEFAULT_COMMS

    MANAGED = True
    LISTED = True
    CODE = None
    MSG_CODE = None
    KIND = None

    COSTUME = None
    GUEST_APPEARANCE = None
    ABSTRACT = False
    MC_COSTUME = 'mc_generic'
    RANKS = RANKS_UNKNOWN
    HELMET1 = None
    HELMET2 = None
    COMM_TEMPLATE = None
    LEGALITY = 'lawful'
    EXTRA_NPC_SHIPS = []
    JUMP_PREFERENCE = None
    PLURALITY = None
    HAVE_FACTION_PROPS = True

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    def __str__(self):
        return self.CODE

    def __init__(self, russian, ids):
        self.russian = russian
        self.ids = ids
        self.relations = {}

        if not self.FORCE_IDS_NAME:
            self.ids_full_name = self.ids.factions_main.new_name(
                self.get_ru_name_full_clean()
            )
            # misc
            self.ids_offer1 = self.ids.factions_offer1.new_name(
                self.get_ru_name_full_clean()
            )
            self.ids_offer2 = self.ids.factions_offer2.new_name(
                self.get_ru_name_full_clean()
            )
            self.ids_offer3 = self.ids.factions_offer3.new_name(
                self.get_ru_name_full_clean()
            )
            self.ids_offer4 = self.ids.factions_offer4.new_name(
                self.get_ru_name_full_clean()
            )

        if not self.FORCE_IDS_SHORT_NAME:
            self.ids_short_name = self.ids.factions_shorts.new_name(
                self.get_ru_name_clean()
            )

        if not self.FORCE_IDS_INFO:
            self.ids_info = self.ids.factions_desc.new_info(
                self.get_ru_info()
            )
        self.npc_ships = []
        if len(self.EXTRA_NPC_SHIPS):
            self.npc_ships += self.EXTRA_NPC_SHIPS

    def get_commodities(self):
        return self.COMMODITY

    def add_npc_ship(self, npc_ship):
        self.npc_ships.append(npc_ship)

    def get_ru_name_clean(self):
        return MS(
            self.RU_NAME.get_ru().replace('+', ''),
            self.RU_NAME.get_en().replace('+', '')
        )

    def get_ru_name_full_clean(self):
        return MS(
            self.RU_NAME_FULL.get_ru().replace('+', ''),
            self.RU_NAME_FULL.get_en().replace('+', '')
        )

    def get_offer1_name(self):
        return self.get_ru_name_clean()

    def get_offer2_name(self):
        return self.get_ru_name_clean()

    def get_offer3_name(self):
        return self.get_ru_name_clean()

    def get_offer4_name(self):
        return self.get_ru_name_clean()

    def get_ru_info(self):
        return MS('', '')

    def is_managed(self):
        return self.MANAGED

    def is_listed(self):
        return self.LISTED

    def has_military_mission(self):
        return self.RANDOM_MISSIONS and self.IS_MILITARY and self.MANAGED

    def has_civilian_mission(self):
        return self.RANDOM_MISSIONS and self.IS_CIVILIAN and self.MANAGED

    def has_pirate_mission(self):
        return self.RANDOM_MISSIONS and self.IS_PIRATE and self.MANAGED

    def get_ships(self):
        ships = []
        if self.INTERCEPTOR:
            ships.append(self.INTERCEPTOR)
        if self.ELITE:
            ships.append(self.ELITE)
        if self.FREIGHTER:
            ships.append(self.FREIGHTER)
        return ships

    def init_relations(self, rel_faction):
        self.relations[rel_faction.CODE] = LoadedRelation(
            rel_faction,
            init_reputation=FRIEND_MAX if rel_faction.CODE == self.CODE else self.DEFAULT_REPUTATION
        )

    def change_reputation(self, rel_faction, reputation):
        self.relations[rel_faction.CODE].set_reputation(reputation)

    def change_empathy(self, rel_faction, empathy):
        self.relations[rel_faction.CODE].set_empathy(empathy)

    @classmethod
    def get_code(cls):
        return cls.CODE

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

    def get_relations_data(self):
        result = []
        for faction_code, rel in self.relations.items():
            result.append(
                f'rep = {rel.get_reputation()}, {faction_code}'
            )
        return SINGLE_DIVIDER.join(result)

    def get_initial_world_content(self):
        return f'''[Group]
nickname = {self.get_code()}
ids_name = {self.FORCE_IDS_NAME if self.FORCE_IDS_NAME else self.ids_full_name.id}
ids_info = {self.FORCE_IDS_INFO if self.FORCE_IDS_INFO else self.ids_info.id}
ids_short_name = {self.FORCE_IDS_SHORT_NAME if self.FORCE_IDS_SHORT_NAME else self.ids_short_name.id}
{self.get_relations_data()}

'''

    def get_empathy_data(self):
        result = []
        for faction_code, rel in self.relations.items():
            result.append(
                f'empathy_rate = {faction_code}, {rel.get_empathy()}'
            )
        return SINGLE_DIVIDER.join(result)

    def get_empathy_content(self):
        return f'''[RepChangeEffects]
group = {self.get_code()}
event = object_destruction, -0.030000
event = random_mission_success, 0.130700
event = random_mission_failure, -0.045000
event = random_mission_abortion, -0.067500
{self.get_empathy_data()}
'''

    def get_empty_rep(self, hate=False):
        return f'rep = {ENEMY_MED if hate else NEUTRAL}, {self.get_code()}'

    def get_plurality(self):
        if self.PLURALITY:
            return self.PLURALITY
        return 'plural' if self.IS_PIRATE else 'singular'

    def get_jump_preference(self):
        if self.JUMP_PREFERENCE:
            return self.JUMP_PREFERENCE
        return 'jumphole' if self.IS_PIRATE else 'jumpgate'

    def get_faction_prop(self):
        if not self.HAVE_FACTION_PROPS:
            return ''
        items = [
            '[FactionProps]',
            f'affiliation = {self.get_code()}',
            f'legality = {self.LEGALITY}',
            f'nickname_plurality = {self.get_plurality()}',
            f'msg_id_prefix = {self.msg}',
            f'jump_preference = {self.get_jump_preference()}',
        ]
        for ship in self.npc_ships:
            items.append(f'npc_ship = {ship}')

        if self.IS_PIRATE:
            if self.russian:
                items.append(RU_VOICES_PIRATE)
            else:
                items.append(EN_VOICES_PIRATE)
        else:
            if self.russian:
                items.append(RU_VOICES_LEGAL)
            else:
                items.append(EN_VOICES_LEGAL)

        items.append(f'mc_costume = {self.MC_COSTUME}')

        if self.COMM_TEMPLATE and self.HELMET1 and self.HELMET2:
            items.append(
                self.COMM_TEMPLATE.format(helmet1=self.HELMET1, helmet2=self.HELMET2)
            )

        items.append(self.RANKS)

        if self.SCANNING_CARGO:
            items.append(SCAN_CARGO)

        items.append(FORMATIONS)

        return SINGLE_DIVIDER.join(items)


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
    RANKS = RANKS_RHEINLAND
    MC_COSTUME = 'mc_rheinland'
    COMM_TEMPLATE = COMM_RHEINLAND
    HELMET1 = bodyparts.COMM_RH_REICHMAN
    HELMET2 = bodyparts.COMM_RH_WILHAM


class BaseLiberty:
    SHIELD_WEAPON = gun.LibertyShieldgun
    CONTRAIL = Contrail.CONTRAIL_LI
    LIGHT = Light.SMALL_BLUE
    COSTUME = bodyparts.LIBERTY
    RANKS = RANKS_LIBERTY
    MC_COSTUME = 'mc_liberty'
    COMM_TEMPLATE = COMM_LIBERTY
    HELMET1 = bodyparts.COMM_LI_HATCHER
    HELMET2 = bodyparts.COMM_GE_GENERIC2


class BaseBretonia:
    SHIELD_WEAPON = gun.BretoniaShieldgun
    CONTRAIL = Contrail.CONTRAIL_BR
    LIGHT = Light.SMALL_BLUE
    COSTUME = bodyparts.BRETONIA
    RANKS = RANKS_RHEINLAND
    MC_COSTUME = 'mc_bretonia'
    COMM_TEMPLATE = COMM_BRETONIA
    HELMET1 = bodyparts.COMM_BR_BRIGHTON
    HELMET2 = bodyparts.COMM_BR_KAITLYN


class BaseKusari:
    SHIELD_WEAPON = gun.KusariShieldgun
    CONTRAIL = Contrail.CONTRAIL_KU
    LIGHT = Light.SMALL_ORANGE
    COSTUME = bodyparts.KUSARI
    RANKS = RANKS_KUSARI
    MC_COSTUME = 'mc_kusari'
    COMM_TEMPLATE = COMM_KUSARI
    HELMET1 = bodyparts.COMM_KU_KYM
    HELMET2 = bodyparts.COMM_PL_PLAYER


class BaseBorderWorld:
    SHIELD_WEAPON = gun.BorderWorldCorsairgun
    CONTRAIL = Contrail.CONTRAIL_CO
    LIGHT = Light.SMALL_PURPLE
    COSTUME = bodyparts.BORDER_WORLD
    RANKS = RANKS_HISPANIA
    MC_COSTUME = 'mc_corsair'
    COMM_TEMPLATE = COMM_HISPANIA
    HELMET1 = bodyparts.COMM_BR_DARCY
    HELMET2 = bodyparts.COMM_PI_PIRATE


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
    RU_NAME_FULL = MS('Рейнландская империя', "Rheinland Empire")
    SCANNING_CARGO = True
    EXTRA_NPC_SHIPS = [
        'rh_grp_main_cruiser', 'rh_grp_main_gunboat'
    ]
    IS_MILITARY = True
    COMMODITY = RH_COMMS

#
# class RheinlandMilitary(RheinlandMain):
#     CODE = 'rm_grp'
#     MANAGED = False
#     RANDOM_MISSIONS = False


class RheinlandCivilians(LawfulFaction, RheinlandMainFleet, BaseRheinland, RheinlandCivEquip, Faction):
    CODE = 'rc_grp'
    WEAPON = gun.RheinlandCivgun
    GUEST_APPEARANCE = bodyparts.PEASANT
    RU_NAME = MS('Д+ауманн', "Daumann")
    RU_NAME_FULL = MS('Промышленность Дауманн', "Daumann Heavy Construction")
    MC_COSTUME = 'mc_siemens'
    COMM_TEMPLATE = COMM_PEASANT
    EXTRA_NPC_SHIPS = [LIFTER]
    IS_CIVILIAN = True
    COMMODITY = RH_COMMS


class RheinlandTraders(LawfulFaction, CivilianFleet, BaseRheinland, RheinlandCivEquip, Faction):
    CODE = 'tr_grp_rh'
    WEAPON = gun.RheinlandCivgun
    GUEST_APPEARANCE = bodyparts.PEASANT
    RU_NAME = MS('Интерсп+эйс', "Interspace")
    RU_NAME_FULL = MS('Коммерция Интерспейс', "Interspace commerce")
    MC_COSTUME = 'mc_siemens'
    COMM_TEMPLATE = COMM_PEASANT
    IS_CIVILIAN = True
    EXTRA_NPC_SHIPS = ['rh_grp_ge_transport_main_01']
    COMMODITY = GLOBAL_COMMS


class RheinlandHunters(LawfulFaction, RheinlandSecondFleet, BaseRheinland, RheinlandCivEquip, Faction):
    CODE = 'bh_grp_rh'
    WEAPON = gun.RheinlandHuntergun
    AFTERBURN = misc.RH_MAIN
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Асгард', "Asgard")
    RU_NAME_FULL = MS('ЧВК Асгард', "PMC Asgard")
    MC_COSTUME = 'mc_hessian'
    SCANNING_CARGO = True
    COMM_TEMPLATE = COMM_JOURNEYMAN
    HELMET1 = bodyparts.COMM_RH_ELITE
    HELMET2 = bodyparts.COMM_RH_GUARD
    IS_CIVILIAN = True
    RANDOM_MISSIONS = False
    EXTRA_NPC_SHIPS = ['rh_grp_ge_armored_main_01']


class RheinlandPirate(UnlawfulFaction, RheinlandSecondFleet, BaseRheinland, RheinlandPirateEquip, Faction):
    CODE = 'pi_grp_rh'
    WEAPON = gun.RheinlandPirategun
    GUEST_APPEARANCE = bodyparts.PIRATE
    RU_NAME = MS('Бундсчух', "Bundschuh")
    RU_NAME_FULL = MS('Бундсчух', "Bundschuh")
    MC_COSTUME = 'mc_hessian'
    IS_PIRATE = True
    COMM_TEMPLATE = COMM_HISPANIA
    HELMET1 = bodyparts.COMM_BR_DARCY
    HELMET2 = bodyparts.COMM_PI_PIRATE
    RANDOM_MISSIONS = False


class Hessians(UnlawfulFaction, RheinlandSecondFleet, BaseRheinland, RheinlandPirateEquip, Faction):
    CODE = 'rx_grp'
    WEAPON = gun.RheinlandHessiangun
    GUEST_APPEARANCE = bodyparts.PIRATE
    RU_NAME = MS('Г+ессенцы', "Hessians")
    RU_NAME_FULL = MS('Г+ессенцы', "Hessians")
    MC_COSTUME = 'mc_hessian'
    IS_PIRATE = True
    COMM_TEMPLATE = COMM_HISPANIA
    HELMET1 = bodyparts.COMM_BR_DARCY
    HELMET2 = bodyparts.COMM_PI_PIRATE


class Junkers(UnlawfulFaction, CivilianFleet, BaseRheinland, RheinlandPirateEquip, Faction):
    CODE = 'junk_grp'
    WEAPON = gun.RheinlandJunkergun
    GUEST_APPEARANCE = bodyparts.PEASANT
    RU_NAME = MS('Мусорщики', "Junkers")
    RU_NAME_FULL = MS('Мусорщики', "Junkers")
    MC_COSTUME = 'mc_hessian'
    IS_PIRATE = True
    COMM_TEMPLATE = COMM_HISPANIA
    HELMET1 = bodyparts.COMM_BR_DARCY
    HELMET2 = bodyparts.COMM_PI_PIRATE
    RANDOM_MISSIONS = False


# Liberty


class LibertyMain(LawfulFaction, LibertyMainFleet, BaseLiberty, LibertyMainEquip, Faction):
    CODE = 'li_grp'
    WEAPON = gun.LibertyLightgun
    GUEST_APPEARANCE = bodyparts.TRADER
    RU_NAME = MS('Л+иберти', "Liberty")
    RU_NAME_FULL = MS('Республика Либерти', "Liberty Republic")
    SCANNING_CARGO = True
    EXTRA_NPC_SHIPS = [
        'li_grp_main_cruiser',
    ]
    IS_MILITARY = True
    COMMODITY = LI_COMMS

#
# class LibertyMilitary(LibertyMain):
#     CODE = 'lm_grp'
#     MANAGED = False
#     RANDOM_MISSIONS = False


class ASF(LibertyMain):
    CODE = 'asf_grp'
    WEAPON = gun.LibertyLightgun
    GUEST_APPEARANCE = bodyparts.MILITARY
    # RU_NAME = MS('Эс-Бэ-А', "Ai-eS-eF")  # For voice!
    RU_NAME = MS('СБА', "ASF")
    RU_NAME_FULL = MS('Служба безопасности Альянса', "Alliance Security Force")
    MANAGED = False
    RANDOM_MISSIONS = False


class LibertyCivilians(LawfulFaction, LibertyMainFleet, BaseLiberty, LibertyCivEquip, Faction):
    CODE = 'lc_grp'
    WEAPON = gun.LibertyCivgun
    GUEST_APPEARANCE = bodyparts.PEASANT
    RU_NAME = MS('Дип Спэйс', "Deep Space")
    RU_NAME_FULL = MS('Дип Спэйс Инжиниринг', "Deep Space Engineering")
    MC_COSTUME = 'mc_deepspace'
    COMM_TEMPLATE = COMM_PEASANT
    EXTRA_NPC_SHIPS = [LIFTER]
    IS_CIVILIAN = True
    COMMODITY = LI_COMMS


class LibertyTraders(LawfulFaction, CivilianFleet, BaseLiberty, LibertyCivEquip, Faction):
    CODE = 'tr_grp_li'
    WEAPON = gun.LibertyCivgun
    GUEST_APPEARANCE = bodyparts.PEASANT
    RU_NAME = MS('Адж+ейра', "Ageira")
    RU_NAME_FULL = MS('Адж+ейра Технолоджис', "Ageira Technologies")
    MC_COSTUME = 'mc_deepspace'
    COMM_TEMPLATE = COMM_PEASANT
    IS_CIVILIAN = True
    EXTRA_NPC_SHIPS = ['li_grp_ge_large_train_main_01']
    IS_GLOBAL_TRADER = True
    COMMODITY = GLOBAL_COMMS


class LibertyHunters(LawfulFaction, LibertySecondFleet, BaseLiberty, LibertyCivEquip, Faction):
    CODE = 'bh_grp_li'
    WEAPON = gun.LibertyHuntergun
    AFTERBURN = misc.LI_MAIN
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Щит', "Shield")
    RU_NAME_FULL = MS('ЧВК Щит', "PMC Shield")
    MC_COSTUME = 'mc_rebel'
    SCANNING_CARGO = True
    COMM_TEMPLATE = COMM_JOURNEYMAN
    HELMET1 = bodyparts.COMM_LI_ELITE
    HELMET2 = bodyparts.COMM_LI_GUARD
    IS_CIVILIAN = True
    RANDOM_MISSIONS = False
    EXTRA_NPC_SHIPS = ['li_grp_ge_armored_main_01']


class LibertyPirate(UnlawfulFaction, LibertySecondFleet, BaseLiberty, LibertyPirateEquip, Faction):
    CODE = 'pi_grp_li'
    WEAPON = gun.LibertyPirategun
    GUEST_APPEARANCE = bodyparts.PIRATE
    RU_NAME = MS('Д+икси', "Dixie")
    RU_NAME_FULL = MS('Конфедеративные мятежники', "Confederate rebels")
    MC_COSTUME = 'mc_rebel'
    IS_PIRATE = True
    COMM_TEMPLATE = COMM_HISPANIA
    HELMET1 = bodyparts.COMM_BR_DARCY
    HELMET2 = bodyparts.COMM_PI_PIRATE


class LibertyRogues(UnlawfulFaction, LibertySecondFleet, BaseLiberty, LibertyPirateEquip, Faction):
    CODE = 'lx_grp'
    WEAPON = gun.LibertyRoguegun
    GUEST_APPEARANCE = bodyparts.PIRATE
    RU_NAME = MS('Разбойники Л+иберти', "Liberty Rogues")
    RU_NAME_FULL = MS('Разбойники Л+иберти', "Liberty Rogues")
    MC_COSTUME = 'mc_rebel'
    IS_PIRATE = True
    COMM_TEMPLATE = COMM_HISPANIA
    HELMET1 = bodyparts.COMM_BR_DARCY
    HELMET2 = bodyparts.COMM_PI_PIRATE


class Starline(UnlawfulFaction, LibertyMainFleet, BaseLiberty, LibertyPirateEquip, Faction):
    CODE = 'sl_grp'
    WEAPON = gun.LibertyStarlinegun
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Старл+айн', "Starline")
    RU_NAME_FULL = MS('Банда Старлайна', "Starline's Band")
    MC_COSTUME = 'mc_rebel'
    IS_PIRATE = True
    COMM_TEMPLATE = COMM_JOURNEYMAN
    HELMET1 = bodyparts.COMM_LI_ELITE
    HELMET2 = bodyparts.COMM_LI_GUARD
    RANDOM_MISSIONS = False


class LaneHackers(UnlawfulFaction, RheinlandSecondFleet, BaseLiberty, LibertyPirateEquip, Faction):
    CODE = 'hack_grp'
    WEAPON = gun.LibertyStarlinegun
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Хакеры', "Hackers")
    RU_NAME_FULL = MS('Путевые хакеры', "Lane Hackers")
    MC_COSTUME = 'mc_rebel'
    IS_PIRATE = True
    COMM_TEMPLATE = COMM_HISPANIA
    HELMET1 = bodyparts.COMM_BR_DARCY
    HELMET2 = bodyparts.COMM_PI_PIRATE
    RANDOM_MISSIONS = False


# Bretonia


class BretoniaMain(LawfulFaction, BretoniaMainFleet, BaseBretonia, BretoniaMainEquip, Faction):
    CODE = 'br_grp'
    WEAPON = gun.BretoniaLightgun
    GUEST_APPEARANCE = bodyparts.TRADER
    RU_NAME = MS('Брет+ония', "Bretonia")
    RU_NAME_FULL = MS('Королевство Брет+ония', "Bretonia Kingdom")
    EXTRA_NPC_SHIPS = [
        'br_grp_main_destroyer', 'br_grp_main_gunboat'
    ]
    IS_MILITARY = True
    COMMODITY = BR_COMMS

#
# class BretoniaMilitary(BretoniaMain):
#     CODE = 'bm_grp'
#     MANAGED = False
#     RANDOM_MISSIONS = False


class BretoniaCivilians(LawfulFaction, BretoniaMainFleet, BaseBretonia, BretoniaCivEquip, Faction):
    CODE = 'bc_grp'
    WEAPON = gun.BretoniaCivgun
    GUEST_APPEARANCE = bodyparts.PEASANT
    # RU_NAME = MS('Би-Эм-Эм', "BMM")
    RU_NAME = MS('БММ', "BMM")
    RU_NAME_FULL = MS('Королевское предприятие БММ', "Royal Enterprise BMM")
    MC_COSTUME = 'mc_aegis'
    COMM_TEMPLATE = COMM_PEASANT
    EXTRA_NPC_SHIPS = [LIFTER]
    IS_CIVILIAN = True
    COMMODITY = BR_COMMS


class BretoniaTraders(LawfulFaction, CivilianFleet, BaseBretonia, BretoniaCivEquip, Faction):
    CODE = 'tr_grp_br'
    WEAPON = gun.BretoniaCivgun
    GUEST_APPEARANCE = bodyparts.PEASANT
    RU_NAME = MS('Б+овекс', "Bowex")
    RU_NAME_FULL = MS('Пограничные перевозки Бовекс', "Border World Exports")
    MC_COSTUME = 'mc_aegis'
    COMM_TEMPLATE = COMM_PEASANT
    IS_CIVILIAN = True
    EXTRA_NPC_SHIPS = ['br_grp_ge_transport_main_01']
    COMMODITY = GLOBAL_COMMS


class BretoniaHunters(LawfulFaction, BretoniaSecondFleet, BaseBretonia, BretoniaCivEquip, Faction):
    CODE = 'bh_grp_br'
    WEAPON = gun.BretoniaHuntergun
    AFTERBURN = misc.BR_MAIN
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    # RU_NAME = MS('Р+оял-Форс', "Roal Force")
    RU_NAME = MS('Роял-Форс', "Roal Force")
    RU_NAME_FULL = MS('ЧВК Роял-Форс', "PMC Roal Force")
    MC_COSTUME = 'mc_energon'
    SCANNING_CARGO = True
    COMM_TEMPLATE = COMM_JOURNEYMAN
    HELMET1 = bodyparts.COMM_BR_GUARD
    HELMET2 = bodyparts.COMM_BR_ELITE
    IS_CIVILIAN = True
    RANDOM_MISSIONS = False
    EXTRA_NPC_SHIPS = ['br_grp_ge_armored_main_01']


class BretoniaPirate(UnlawfulFaction, CivilianFleet, BaseBretonia, BretoniaPirateEquip, Faction):
    CODE = 'pi_grp_br'
    WEAPON = gun.BretoniaPirategun
    GUEST_APPEARANCE = bodyparts.PIRATE
    RU_NAME = MS('Гайане', "Gaians")
    RU_NAME_FULL = MS('Гайане', "Gaians")
    MC_COSTUME = 'mc_energon'
    IS_PIRATE = True
    COMM_TEMPLATE = COMM_HISPANIA
    HELMET1 = bodyparts.COMM_BR_DARCY
    HELMET2 = bodyparts.COMM_PI_PIRATE


class Ireland(UnlawfulFaction, BretoniaSecondFleet, BaseBretonia, BretoniaPirateEquip, Faction):
    CODE = 'bx_grp'
    WEAPON = gun.BretoniaIragun
    GUEST_APPEARANCE = bodyparts.PIRATE
    RU_NAME = MS('ИРА', "IRA")
    RU_NAME_FULL = MS('Ирландская республиканская армия', "Ireland Republican Army")
    MC_COSTUME = 'mc_energon'
    IS_PIRATE = True
    COMM_TEMPLATE = COMM_JOURNEYMAN
    HELMET1 = bodyparts.COMM_BR_ELITE
    HELMET2 = bodyparts.COMM_BR_GUARD


class Xenos(UnlawfulFaction, BretoniaSecondFleet, BaseBretonia, BretoniaPirateEquip, Faction):
    CODE = 'xenos_grp'
    WEAPON = gun.BretoniaXenosgun
    GUEST_APPEARANCE = bodyparts.PEASANT
    RU_NAME = MS('Кс+еносы', "Xenos")
    RU_NAME_FULL = MS('Кс+еносы', "Xenos")
    MC_COSTUME = 'mc_energon'
    IS_PIRATE = True
    COMM_TEMPLATE = COMM_HISPANIA
    HELMET1 = bodyparts.COMM_BR_DARCY
    HELMET2 = bodyparts.COMM_PI_PIRATE
    # RANDOM_MISSIONS = False


# Kusari


class KusariMain(LawfulFaction, KusariMainFleet, BaseKusari, KusariMainEquip, Faction):
    CODE = 'ku_grp'
    WEAPON = gun.KusariLightgun
    GUEST_APPEARANCE = bodyparts.TRADER
    RU_NAME = MS('Кус+ари', "Kusari")
    RU_NAME_FULL = MS('Сёгунат Кус+ари', "Kusari Shogunate")
    SCANNING_CARGO = True
    EXTRA_NPC_SHIPS = [
        'ku_grp_main_destroyer', 'ku_grp_main_gunboat'
    ]
    IS_MILITARY = True
    COMMODITY = KU_COMMS

#
# class KusariMilitary(KusariMain):
#     CODE = 'km_grp'
#     MANAGED = False
#     RANDOM_MISSIONS = False


class KusariCivilians(LawfulFaction, KusariMainFleet, BaseKusari, KusariCivEquip, Faction):
    CODE = 'kc_grp'
    WEAPON = gun.KusariCivgun
    GUEST_APPEARANCE = bodyparts.PEASANT
    RU_NAME = MS('Киш+иро', "Kishiro")
    RU_NAME_FULL = MS('Киш+иро Технолоджис', "Kishiro Technologies")
    MC_COSTUME = 'mc_gasmining'
    COMM_TEMPLATE = COMM_PEASANT
    EXTRA_NPC_SHIPS = [LIFTER]
    IS_CIVILIAN = True
    COMMODITY = KU_COMMS


class KusariTraders(LawfulFaction, CivilianFleet, BaseKusari, KusariCivEquip, Faction):
    CODE = 'tr_grp_ku'
    WEAPON = gun.KusariCivgun
    GUEST_APPEARANCE = bodyparts.PEASANT
    RU_NAME = MS('Сам+ура', "Samura")
    RU_NAME_FULL = MS('Промышленность Сам+ура', "Samura Industries")
    MC_COSTUME = 'mc_gasmining'
    COMM_TEMPLATE = COMM_PEASANT
    IS_CIVILIAN = True
    EXTRA_NPC_SHIPS = ['ku_grp_ge_large_train_main_01']
    COMMODITY = GLOBAL_COMMS


class KusariHunters(LawfulFaction, KusariSecondFleet, BaseKusari, KusariCivEquip, Faction):
    CODE = 'bh_grp_ku'
    WEAPON = gun.KusariHuntergun
    AFTERBURN = misc.KU_MAIN
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Чёрный Дракон', "Black Dragon")
    RU_NAME_FULL = MS('ЧВК Чёрный Дракон', "PMC Black Dragon")
    MC_COSTUME = 'mc_shinobi'
    SCANNING_CARGO = True
    COMM_TEMPLATE = COMM_JOURNEYMAN
    HELMET1 = bodyparts.COMM_KU_ELITE
    HELMET2 = bodyparts.COMM_KU_GUARD
    IS_CIVILIAN = True
    RANDOM_MISSIONS = False
    EXTRA_NPC_SHIPS = ['ku_grp_ge_armored_main_01']


class KusariPirate(UnlawfulFaction, KusariSecondFleet, BaseKusari, KusariPirateEquip, Faction):
    CODE = 'pi_grp_ku'
    WEAPON = gun.KusariPirategun
    GUEST_APPEARANCE = bodyparts.PIRATE
    RU_NAME = MS('Золот+ые Хризант+емы', "Golden Chrystantems")
    RU_NAME_FULL = MS('Золот+ые Хризант+емы', "Golden Chrystantems")
    MC_COSTUME = 'mc_shinobi'
    IS_PIRATE = True
    COMM_TEMPLATE = COMM_HISPANIA
    HELMET1 = bodyparts.COMM_BR_DARCY
    HELMET2 = bodyparts.COMM_PI_PIRATE


class Shinobi(UnlawfulFaction, KusariMainFleet, BaseKusari, KusariPirateEquip, Faction):
    CODE = 'kx_grp'
    WEAPON = gun.KusariShinobigun
    GUEST_APPEARANCE = bodyparts.PIRATE
    RU_NAME = MS('Клан Шин+оби', "Shinobi Clan")
    RU_NAME_FULL = MS('Клан Шин+оби', "Shinobi Clan")
    MC_COSTUME = 'mc_shinobi'
    IS_PIRATE = True
    COMM_TEMPLATE = COMM_JOURNEYMAN
    HELMET1 = bodyparts.COMM_BR_DARCY
    HELMET2 = bodyparts.COMM_PI_PIRATE


class FarmerAlliance(UnlawfulFaction, KusariSecondFleet, BaseKusari, KusariPirateEquip, Faction):
    CODE = 'farm_grp'
    WEAPON = gun.KusariDragongun
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Фермеры', "Farmers")
    RU_NAME_FULL = MS('Альянс фермеров', "Farmer Alliance")
    MC_COSTUME = 'mc_shinobi'
    IS_PIRATE = True
    COMM_TEMPLATE = COMM_JOURNEYMAN
    HELMET1 = bodyparts.COMM_BR_DARCY
    HELMET2 = bodyparts.COMM_PI_PIRATE


# Border World


class OrderMain(LawfulFaction, OrderFleet, BaseBorderWorld, BorderWorldOrderEquip, Faction):
    CODE = 'or_grp'
    WEAPON = gun.OrderLightgun
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Орден', "The Order")
    RU_NAME_FULL = MS('Орден', "The Order")
    MC_COSTUME = 'mc_generic'
    COMM_TEMPLATE = COMM_ORDER
    HELMET1 = bodyparts.COMM_RH_ALARIC
    HELMET2 = bodyparts.COMM_BR_ELITE
    IS_MILITARY = True
    RANDOM_MISSIONS = False

#
# class OrderMilitary(OrderMain):
#     CODE = 'om_grp'
#     MANAGED = False
#     RANDOM_MISSIONS = False


class Corsairs(UnlawfulFaction, CorsairFleet, BaseBorderWorld, BorderWorldCorsairEquip, Faction):
    CODE = 'co_grp'
    WEAPON = gun.BorderWorldCorsairgun
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Корс+ары', "Corsairs")
    RU_NAME_FULL = MS('Корс+ары', "Corsairs")
    IS_PIRATE = True
    COMM_TEMPLATE = COMM_HISPANIA
    # IS_MILITARY = True

#
# class CorsairMilitary(Corsairs):
#     CODE = 'cm_grp'
#     MANAGED = False
#     RANDOM_MISSIONS = False

#
# class BorderWorldHunters(UnlawfulFaction, CorsairFleet, BaseBorderWorld, BorderWorldCorsairEquip, Faction):
#     CODE = 'bh_bw_grp'
#     WEAPON = gun.BorderWorldCorsairgun
#     GUEST_APPEARANCE = bodyparts.JOURNEYMAN
#     RU_NAME = MS('Приватиры', "Privateers")
#     RU_NAME_FULL = MS('Приватиры', "Privateers")
#     IS_PIRATE = True
#     COMM_TEMPLATE = COMM_JOURNEYMAN
#     RANDOM_MISSIONS = False


class Outcasts(LawfulFaction, RheinlandSecondFleet, BaseBorderWorld, BorderWorldOutcastsEquip, Faction):
    CODE = 'out_grp'
    WEAPON = gun.BorderWorldOutcastgun
    GUEST_APPEARANCE = bodyparts.JOURNEYMAN
    RU_NAME = MS('Изг+ои', "Outcasts")
    RU_NAME_FULL = MS('Изг+ои', "Outcasts")
    IS_PIRATE = True
    COMM_TEMPLATE = COMM_JOURNEYMAN
    # RANDOM_MISSIONS = False


class BorderWorldPirate(UnlawfulFaction, RheinlandSecondFleet, BaseBorderWorld, BorderWorldCorsairEquip, Faction):
    CODE = 'cx_grp'
    WEAPON = gun.BorderWorldPirategun
    GUEST_APPEARANCE = bodyparts.PIRATE
    RU_NAME = MS('Пилигр+имы', "Pilgrims")
    RU_NAME_FULL = MS('Пилигр+имы', "Pilgrims")
    IS_PIRATE = True
    RANDOM_MISSIONS = False

#
# class BorderWorldTraders(UnlawfulFaction, CorsairFleet, BaseBorderWorld, BorderWorldCorsairEquip, Faction):
#     CODE = 'tr_grp_bw'
#     WEAPON = gun.BorderWorldPirategun
#     GUEST_APPEARANCE = bodyparts.PIRATE
#     RU_NAME = MS('Меркадо', "Mercado")
#     RU_NAME_FULL = MS('Меркадо', "Mercado")
#     IS_PIRATE = True
#     COMM_TEMPLATE = COMM_PEASANT
#     RANDOM_MISSIONS = False


class DeidrichPeople(UnlawfulFaction, BaseRheinland, RheinlandMainEquip, Faction):
    CODE = 'dtr_grp'
    WEAPON = gun.RheinlandLightgun
    MANAGED = False
    RU_NAME = MS('Люди Дитриха', "Deidrich's people")
    RU_NAME_FULL = MS('Люди Дитриха', "Deidrich's people")
    RANDOM_MISSIONS = False

#
# class Workaround1(UnlawfulFaction, BaseRheinland, RheinlandMainEquip, Faction):
#     CODE = 'bh_grp'
#     WEAPON = gun.RheinlandLightgun
#     MANAGED = False
#     RU_NAME = MS('Люди Дитриха', "Deidrich's people")
#     RU_NAME_FULL = MS('Люди Дитриха', "Deidrich's people")
#     RANDOM_MISSIONS = False
#
#
# class Workaround2(UnlawfulFaction, BaseRheinland, RheinlandMainEquip, Faction):
#     CODE = 'pi_grp'
#     WEAPON = gun.RheinlandLightgun
#     MANAGED = False
#     RU_NAME = MS('Люди Дитриха', "Deidrich's people")
#     RU_NAME_FULL = MS('Люди Дитриха', "Deidrich's people")
#     RANDOM_MISSIONS = False
#
#
# class Workaround3(UnlawfulFaction, BaseRheinland, RheinlandMainEquip, Faction):
#     CODE = 'tr_grp'
#     WEAPON = gun.RheinlandLightgun
#     MANAGED = False
#     RU_NAME = MS('Люди Дитриха', "Deidrich's people")
#     RU_NAME_FULL = MS('Люди Дитриха', "Deidrich's people")
#     RANDOM_MISSIONS = False
#
#
# class OdjaPeople(UnlawfulFaction, BaseKusari, KusariMainEquip, Faction):
#     CODE = 'odja_grp'
#     WEAPON = gun.RheinlandLightgun
#     MANAGED = False
#     RU_NAME = MS('Клан Одзя', "Clan Odja")
#     RU_NAME_FULL = MS('Клан Одзя', "Clan Odja")
#     RANDOM_MISSIONS = False
#
#
# class Hispaniola(UnlawfulFaction, BaseBretonia, BretoniaMainEquip, Faction):
#     CODE = 'hsp_grp'
#     WEAPON = gun.RheinlandLightgun
#     MANAGED = False
#     RU_NAME = MS('Экипаж Испаньолы', "Hispaniola crew")
#     RU_NAME_FULL = MS('Экипаж Испаньолы', "Hispaniola crew")
#     RANDOM_MISSIONS = False
#
#
# class RheinlandSmuggler(RheinlandPirate):
#     CODE = 'smg_rh_grp'
#     MANAGED = False
#     RU_NAME = MS('', "")
#     RU_NAME_FULL = MS('', "")
#     RANDOM_MISSIONS = False

#
# class LibertySmuggler(LibertyPirate):
#     CODE = 'smg_li_grp'
#     MANAGED = False
#     RU_NAME = MS('', "")
#     RU_NAME_FULL = MS('', "")
#     RANDOM_MISSIONS = False
#
#
# class BretoniaSmuggler(BretoniaPirate):
#     CODE = 'smg_br_grp'
#     MANAGED = False
#     RU_NAME = MS('', "")
#     RU_NAME_FULL = MS('', "")
#     RANDOM_MISSIONS = False
#
#
# class KusariSmuggler(KusariPirate):
#     CODE = 'smg_ku_grp'
#     MANAGED = False
#     RU_NAME = MS('', "")
#     RU_NAME_FULL = MS('', "")
#     RANDOM_MISSIONS = False
#
#
# class BorderWorldSmuggler(BorderWorldPirate):
#     CODE = 'smg_bw_grp'
#     MANAGED = False
#     RU_NAME = MS('', "")
#     RU_NAME_FULL = MS('', "")
#     RANDOM_MISSIONS = False


class Unknown(Faction):
    CODE = 'fc_uk_grp'
    MANAGED = False
    JUMP_PREFERENCE = 'all'
    PLURALITY = 'singular'
    HAVE_FACTION_PROPS = False
    LISTED = False
    FORCE_IDS_NAME = 1
    FORCE_IDS_SHORT_NAME = 1
    FORCE_IDS_INFO = 1
    RANDOM_MISSIONS = False


class AlaricLike(LawfulFaction, BaseLiberty, LibertyMainEquip, Faction):
    CODE = 'li_al'
    WEAPON = gun.LibertyHuntergun
    AFTERBURN = misc.LI_MAIN
    MANAGED = False
    ABSTRACT = True
    FORCE_IDS_NAME = 1
    FORCE_IDS_SHORT_NAME = 1
    FORCE_IDS_INFO = 1
    RANDOM_MISSIONS = False
    HAVE_FACTION_PROPS = False


class Nomad(Faction):
    CODE = 'fc_n_grp'
    MANAGED = False
    DEFAULT_REPUTATION = FRIEND_MED
    RU_NAME = MS('Номады', "Nomads")
    RU_NAME_FULL = MS('Номады', "Nomads")
    LISTED = False
    FORCE_IDS_NAME = 1
    FORCE_IDS_SHORT_NAME = 1
    FORCE_IDS_INFO = 1
    RANDOM_MISSIONS = False
    HAVE_FACTION_PROPS = False


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
            return self.empathy - (self.empathy*2)
        else:
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
    # Relation(BorderWorldHunters, NEUTRAL),

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

    # Relation(Nomad, ENEMY_MED),
    Relation(DeidrichPeople, NEUTRAL),
    # Relation(OdjaPeople, NEUTRAL),
    # Relation(Hispaniola, NEUTRAL),
    #
    # Relation(RheinlandSmuggler, ENEMY_MED),
    # Relation(LibertySmuggler, ENEMY_MED),
    # Relation(BretoniaSmuggler, ENEMY_MED),
    # Relation(KusariSmuggler, ENEMY_MED),
    # Relation(BorderWorldSmuggler, ENEMY_MED),
]


RELATIONS = [
    FactionRelation(
        RheinlandMain,
        [
            Relation(RheinlandMain, FRIEND_MED),
            Relation(LibertyMain, FRIEND_MED),
            Relation(BretoniaMain, FRIEND_MED),
            Relation(KusariMain, FRIEND_MED),

            Relation(RheinlandHunters, NEUTRAL, LIKE2),
            Relation(LibertyHunters, NEUTRAL, LIKE1),
            Relation(BretoniaHunters, NEUTRAL, LIKE1),
            Relation(KusariHunters, NEUTRAL, LIKE1),
            # Relation(BorderWorldHunters, NEUTRAL, LIKE1),

            Relation(RheinlandCivilians, FRIEND_MED, LIKE4),
            Relation(LibertyCivilians, FRIEND_MED, LIKE2),
            Relation(BretoniaCivilians, FRIEND_MED, LIKE2),
            Relation(KusariCivilians, FRIEND_MED, LIKE2),

            Relation(RheinlandTraders, FRIEND_MED, LIKE3),
            Relation(LibertyTraders, FRIEND_MED, LIKE2),
            Relation(BretoniaTraders, FRIEND_MED, LIKE2),
            Relation(KusariTraders, FRIEND_MED, LIKE2),
            # Relation(BorderWorldTraders, NEUTRAL, LIKE2),

            Relation(RheinlandPirate, ENEMY_MED, HATE5),
            Relation(LibertyPirate, ENEMY_MED, HATE3),
            Relation(BretoniaPirate, ENEMY_MED, HATE2),
            Relation(KusariPirate, FRIEND_MED, HATE3),
            # Relation(BorderWorldPirate, FRIEND_MED, HATE1),

            Relation(Corsairs, ENEMY_MED, HATE6),
            Relation(Outcasts, NEUTRAL),

            Relation(Hessians, ENEMY_MED, HATE8),
            # Relation(Junkers, ENEMY_MIN, HATE3),
            Relation(LibertyRogues, ENEMY_MED, HATE7),
            # Relation(Starline, ENEMY_MED, HATE3),
            Relation(LaneHackers, ENEMY_MED, HATE6),
            # Relation(Xenos, ENEMY_MED, HATE7),
            # Relation(Ireland, ENEMY_MED, HATE3),
            Relation(Shinobi, ENEMY_MED, HATE5),
            Relation(FarmerAlliance, ENEMY_MED, HATE5),

            Relation(Nomad, FRIEND_MED),
        ]
    ),

    FactionRelation(
        LibertyMain,
        [
            Relation(RheinlandMain, FRIEND_MED),
            Relation(LibertyMain, FRIEND_MED),
            Relation(BretoniaMain, FRIEND_MED),
            Relation(KusariMain, FRIEND_MED),

            Relation(RheinlandHunters, NEUTRAL, LIKE1),
            Relation(LibertyHunters, NEUTRAL, LIKE2),
            Relation(BretoniaHunters, NEUTRAL, LIKE1),
            Relation(KusariHunters, NEUTRAL, LIKE1),
            # Relation(BorderWorldHunters, NEUTRAL, LIKE1),

            Relation(RheinlandCivilians, FRIEND_MED, LIKE2),
            Relation(LibertyCivilians, FRIEND_MED, LIKE4),
            Relation(BretoniaCivilians, FRIEND_MED, LIKE2),
            Relation(KusariCivilians, FRIEND_MED, LIKE2),

            Relation(RheinlandTraders, FRIEND_MED, LIKE2),
            Relation(LibertyTraders, FRIEND_MED, LIKE3),
            Relation(BretoniaTraders, FRIEND_MED, LIKE2),
            Relation(KusariTraders, FRIEND_MED, LIKE2),
            # Relation(BorderWorldTraders, NEUTRAL, LIKE2),

            Relation(RheinlandPirate, ENEMY_MED, HATE3),
            Relation(LibertyPirate, ENEMY_MED, HATE5),
            Relation(BretoniaPirate, ENEMY_MED, HATE3),
            Relation(KusariPirate, ENEMY_MED, HATE2),
            Relation(BorderWorldPirate, ENEMY_MED, HATE1),

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

            Relation(Nomad, FRIEND_MED),
        ]
    ),

    FactionRelation(
        BretoniaMain,
        [
            Relation(RheinlandMain, FRIEND_MED),
            Relation(LibertyMain, FRIEND_MED),
            Relation(BretoniaMain, FRIEND_MED),
            Relation(KusariMain, FRIEND_MED),

            Relation(RheinlandHunters, NEUTRAL, LIKE1),
            Relation(LibertyHunters, NEUTRAL, LIKE1),
            Relation(BretoniaHunters, NEUTRAL, LIKE2),
            Relation(KusariHunters, NEUTRAL, LIKE1),
            # Relation(BorderWorldHunters, NEUTRAL, LIKE1),

            Relation(RheinlandCivilians, FRIEND_MED, LIKE2),
            Relation(LibertyCivilians, FRIEND_MED, LIKE2),
            Relation(BretoniaCivilians, FRIEND_MED, LIKE2),
            Relation(KusariCivilians, FRIEND_MED, LIKE2),

            Relation(RheinlandTraders, FRIEND_MED, LIKE2),
            Relation(LibertyTraders, FRIEND_MED, LIKE3),
            Relation(BretoniaTraders, FRIEND_MED, LIKE2),
            Relation(KusariTraders, FRIEND_MED, LIKE2),
            # Relation(BorderWorldTraders, NEUTRAL, LIKE2),

            Relation(RheinlandPirate, ENEMY_MED, HATE3),
            Relation(LibertyPirate, ENEMY_MED, HATE5),
            Relation(BretoniaPirate, ENEMY_MED, HATE3),
            Relation(KusariPirate, ENEMY_MED, HATE2),
            Relation(BorderWorldPirate, ENEMY_MED, HATE1),

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

            Relation(Nomad, FRIEND_MED),
        ]
    ),

    FactionRelation(
        KusariMain,
        [
            Relation(RheinlandMain, FRIEND_MED),
            Relation(LibertyMain, FRIEND_MED),
            Relation(BretoniaMain, FRIEND_MED),
            Relation(KusariMain, FRIEND_MED),

            Relation(RheinlandHunters, NEUTRAL, LIKE1),
            Relation(LibertyHunters, NEUTRAL, LIKE1),
            Relation(BretoniaHunters, NEUTRAL, LIKE1),
            Relation(KusariHunters, NEUTRAL, LIKE2),
            # Relation(BorderWorldHunters, NEUTRAL, LIKE1),

            Relation(RheinlandCivilians, FRIEND_MED, LIKE2),
            Relation(LibertyCivilians, FRIEND_MED, LIKE2),
            Relation(BretoniaCivilians, FRIEND_MED, LIKE2),
            Relation(KusariCivilians, FRIEND_MED, LIKE4),

            Relation(RheinlandTraders, FRIEND_MED, LIKE2),
            Relation(LibertyTraders, FRIEND_MED, LIKE2),
            Relation(BretoniaTraders, FRIEND_MED, LIKE2),
            Relation(KusariTraders, FRIEND_MED, LIKE3),
            # Relation(BorderWorldTraders, NEUTRAL, LIKE2),

            Relation(RheinlandPirate, ENEMY_MED, HATE3),
            Relation(LibertyPirate, ENEMY_MED, HATE2),
            Relation(BretoniaPirate, ENEMY_MED, HATE3),
            Relation(KusariPirate, ENEMY_MED, HATE5),
            Relation(BorderWorldPirate, ENEMY_MED, HATE2),

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

            Relation(Nomad, FRIEND_MED),
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
            # Relation(BorderWorldHunters, NEUTRAL, LIKE1),

            Relation(RheinlandCivilians, FRIEND_MED),
            Relation(LibertyCivilians, FRIEND_MED),
            Relation(BretoniaCivilians, FRIEND_MED),
            Relation(KusariCivilians, FRIEND_MED),

            Relation(RheinlandTraders, FRIEND_MED),
            Relation(LibertyTraders, FRIEND_MED),
            Relation(BretoniaTraders, FRIEND_MED),
            Relation(KusariTraders, FRIEND_MED),
            # Relation(BorderWorldTraders, NEUTRAL),

            Relation(RheinlandPirate, ENEMY_MED, HATE5),
            Relation(LibertyPirate, ENEMY_MED, HATE4),
            Relation(BretoniaPirate, ENEMY_MED, HATE2),
            Relation(KusariPirate, ENEMY_MED, HATE4),
            Relation(BorderWorldPirate, ENEMY_MED, HATE2),

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

            Relation(Nomad, FRIEND_MED),
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
            # Relation(BorderWorldHunters, NEUTRAL, LIKE1),

            Relation(RheinlandCivilians, FRIEND_MED),
            Relation(LibertyCivilians, FRIEND_MED),
            Relation(BretoniaCivilians, FRIEND_MED),
            Relation(KusariCivilians, FRIEND_MED),

            Relation(RheinlandTraders, FRIEND_MED),
            Relation(LibertyTraders, FRIEND_MED),
            Relation(BretoniaTraders, FRIEND_MED),
            Relation(KusariTraders, FRIEND_MED),
            # Relation(BorderWorldTraders, NEUTRAL),

            Relation(RheinlandPirate, ENEMY_MED, HATE3),
            Relation(LibertyPirate, ENEMY_MED, HATE4),
            Relation(BretoniaPirate, ENEMY_MED, HATE3),
            Relation(KusariPirate, ENEMY_MED, HATE2),
            Relation(BorderWorldPirate, ENEMY_MED, HATE2),

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

            Relation(Nomad, FRIEND_MED),
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
            # Relation(BorderWorldHunters, NEUTRAL, LIKE1),

            Relation(RheinlandCivilians, FRIEND_MED),
            Relation(LibertyCivilians, FRIEND_MED),
            Relation(BretoniaCivilians, FRIEND_MED),
            Relation(KusariCivilians, FRIEND_MED),

            Relation(RheinlandTraders, FRIEND_MED),
            Relation(LibertyTraders, FRIEND_MED),
            Relation(BretoniaTraders, FRIEND_MED),
            Relation(KusariTraders, FRIEND_MED),
            # Relation(BorderWorldTraders, NEUTRAL),

            Relation(RheinlandPirate, ENEMY_MED, HATE2),
            Relation(LibertyPirate, ENEMY_MED, HATE3),
            Relation(BretoniaPirate, ENEMY_MED, HATE5),
            Relation(KusariPirate, ENEMY_MED, HATE3),
            Relation(BorderWorldPirate, ENEMY_MED, HATE2),

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

            Relation(Nomad, FRIEND_MED),
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

            Relation(RheinlandCivilians, FRIEND_MED),
            Relation(LibertyCivilians, FRIEND_MED),
            Relation(BretoniaCivilians, FRIEND_MED),
            Relation(KusariCivilians, FRIEND_MED),

            Relation(RheinlandTraders, FRIEND_MED),
            Relation(LibertyTraders, FRIEND_MED),
            Relation(BretoniaTraders, FRIEND_MED),
            Relation(KusariTraders, FRIEND_MED),
            # Relation(BorderWorldTraders, NEUTRAL),

            Relation(RheinlandPirate, ENEMY_MED, HATE3),
            Relation(LibertyPirate, ENEMY_MED, HATE2),
            Relation(BretoniaPirate, ENEMY_MED, HATE3),
            Relation(KusariPirate, ENEMY_MED, HATE5),
            Relation(BorderWorldPirate, ENEMY_MED, HATE2),

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

            Relation(Nomad, FRIEND_MED),
        ]
    ),
    #
    # FactionRelation(
    #     BorderWorldHunters,
    #     [
    #         Relation(RheinlandMain, NEUTRAL, LIKE1),
    #         Relation(LibertyMain, NEUTRAL, LIKE1),
    #         Relation(BretoniaMain, NEUTRAL, LIKE1),
    #         Relation(KusariMain, NEUTRAL, LIKE1),
    #
    #         Relation(RheinlandHunters, NEUTRAL, LIKE2),
    #         Relation(LibertyHunters, NEUTRAL, LIKE2),
    #         Relation(BretoniaHunters, NEUTRAL, LIKE2),
    #         Relation(KusariHunters, NEUTRAL, LIKE2),
    #
    #         Relation(RheinlandCivilians, FRIEND_MED),
    #         Relation(LibertyCivilians, FRIEND_MED),
    #         Relation(BretoniaCivilians, FRIEND_MED),
    #         Relation(KusariCivilians, FRIEND_MED),
    #
    #         Relation(RheinlandTraders, FRIEND_MED),
    #         Relation(LibertyTraders, FRIEND_MED),
    #         Relation(BretoniaTraders, FRIEND_MED),
    #         Relation(KusariTraders, FRIEND_MED),
    #         Relation(BorderWorldTraders, NEUTRAL),
    #
    #         Relation(RheinlandPirate, FRIEND_MED),
    #         Relation(LibertyPirate, FRIEND_MED),
    #         Relation(BretoniaPirate, FRIEND_MED),
    #         Relation(KusariPirate, FRIEND_MED),
    #         Relation(BorderWorldPirate, FRIEND_MED),
    #
    #         Relation(Corsairs, ENEMY_MED, HATE5),
    #         Relation(Outcasts, ENEMY_MED, HATE2),
    #
    #         Relation(Hessians, ENEMY_MED, HATE4),
    #         Relation(Junkers, ENEMY_MIN, HATE2),
    #         Relation(LibertyRogues, ENEMY_MED, HATE4),
    #         Relation(Starline, ENEMY_MED, HATE4),
    #         Relation(LaneHackers, ENEMY_MED, HATE4),
    #         Relation(Xenos, ENEMY_MED, HATE6),
    #         Relation(Ireland, ENEMY_MED, HATE4),
    #         Relation(Shinobi, ENEMY_MED, HATE4),
    #         Relation(FarmerAlliance, ENEMY_MED, HATE4),
    #
    #         Relation(Nomad, FRIEND_MED),
    #     ]
    # ),

    ### CIVILIANS

    FactionRelation(
        RheinlandCivilians,
        [
            Relation(RheinlandMain, FRIEND_MED),
            Relation(LibertyMain, FRIEND_MED),
            Relation(BretoniaMain, FRIEND_MED),
            Relation(KusariMain, FRIEND_MED),

            Relation(RheinlandHunters, NEUTRAL, LIKE2),
            Relation(LibertyHunters, NEUTRAL, LIKE1),
            Relation(BretoniaHunters, NEUTRAL, LIKE1),
            Relation(KusariHunters, NEUTRAL, LIKE1),

            Relation(RheinlandCivilians, FRIEND_MED, LIKE4),
            Relation(LibertyCivilians, FRIEND_MED, LIKE2),
            Relation(BretoniaCivilians, FRIEND_MED, LIKE2),
            Relation(KusariCivilians, FRIEND_MED, LIKE2),

            Relation(RheinlandTraders, FRIEND_MED, LIKE3),
            Relation(LibertyTraders, FRIEND_MED, LIKE2),
            Relation(BretoniaTraders, FRIEND_MED, LIKE2),
            Relation(KusariTraders, FRIEND_MED, LIKE2),
            # Relation(BorderWorldTraders, NEUTRAL, LIKE2),

            Relation(RheinlandPirate, FRIEND_MED, HATE5),
            Relation(LibertyPirate, FRIEND_MED, HATE3),
            Relation(BretoniaPirate, FRIEND_MED, HATE2),
            Relation(KusariPirate, FRIEND_MED, HATE3),
            Relation(BorderWorldPirate, FRIEND_MED, HATE1),

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

            Relation(Nomad, FRIEND_MED),
            Relation(DeidrichPeople, FRIEND_MED),
        ]
    ),

    FactionRelation(
        LibertyCivilians,
        [
            Relation(RheinlandMain, FRIEND_MED),
            Relation(LibertyMain, FRIEND_MED),
            Relation(BretoniaMain, FRIEND_MED),
            Relation(KusariMain, FRIEND_MED),

            Relation(RheinlandHunters, NEUTRAL, LIKE1),
            Relation(LibertyHunters, NEUTRAL, LIKE2),
            Relation(BretoniaHunters, NEUTRAL, LIKE1),
            Relation(KusariHunters, NEUTRAL, LIKE1),

            Relation(RheinlandCivilians, FRIEND_MED, LIKE2),
            Relation(LibertyCivilians, FRIEND_MED, LIKE4),
            Relation(BretoniaCivilians, FRIEND_MED, LIKE2),
            Relation(KusariCivilians, FRIEND_MED, LIKE2),

            Relation(RheinlandTraders, FRIEND_MED, LIKE2),
            Relation(LibertyTraders, FRIEND_MED, LIKE3),
            Relation(BretoniaTraders, FRIEND_MED, LIKE2),
            Relation(KusariTraders, FRIEND_MED, LIKE2),
            # Relation(BorderWorldTraders, NEUTRAL, LIKE2),

            Relation(RheinlandPirate, FRIEND_MED, HATE3),
            Relation(LibertyPirate, FRIEND_MED, HATE5),
            Relation(BretoniaPirate, FRIEND_MED, HATE3),
            Relation(KusariPirate, FRIEND_MED, HATE2),
            Relation(BorderWorldPirate, FRIEND_MED, HATE1),

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

            Relation(Nomad, FRIEND_MED),
        ]
    ),

    FactionRelation(
        BretoniaCivilians,
        [
            Relation(RheinlandMain, FRIEND_MED),
            Relation(LibertyMain, FRIEND_MED),
            Relation(BretoniaMain, FRIEND_MED),
            Relation(KusariMain, FRIEND_MED),

            Relation(RheinlandHunters, NEUTRAL, LIKE1),
            Relation(LibertyHunters, NEUTRAL, LIKE1),
            Relation(BretoniaHunters, NEUTRAL, LIKE2),
            Relation(KusariHunters, NEUTRAL, LIKE1),

            Relation(RheinlandCivilians, FRIEND_MED, LIKE2),
            Relation(LibertyCivilians, FRIEND_MED, LIKE2),
            Relation(BretoniaCivilians, FRIEND_MED, LIKE2),
            Relation(KusariCivilians, FRIEND_MED, LIKE2),

            Relation(RheinlandTraders, FRIEND_MED, LIKE2),
            Relation(LibertyTraders, FRIEND_MED, LIKE3),
            Relation(BretoniaTraders, FRIEND_MED, LIKE2),
            Relation(KusariTraders, FRIEND_MED, LIKE2),
            # Relation(BorderWorldTraders, NEUTRAL, LIKE2),

            Relation(RheinlandPirate, FRIEND_MED, HATE3),
            Relation(LibertyPirate, FRIEND_MED, HATE5),
            Relation(BretoniaPirate, FRIEND_MED, HATE3),
            Relation(KusariPirate, FRIEND_MED, HATE2),
            Relation(BorderWorldPirate, FRIEND_MED, HATE1),

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

            Relation(Nomad, FRIEND_MED),
        ]
    ),

    FactionRelation(
        KusariCivilians,
        [
            Relation(RheinlandMain, FRIEND_MED),
            Relation(LibertyMain, FRIEND_MED),
            Relation(BretoniaMain, FRIEND_MED),
            Relation(KusariMain, FRIEND_MED),

            Relation(RheinlandHunters, NEUTRAL, LIKE1),
            Relation(LibertyHunters, NEUTRAL, LIKE1),
            Relation(BretoniaHunters, NEUTRAL, LIKE1),
            Relation(KusariHunters, NEUTRAL, LIKE2),

            Relation(RheinlandCivilians, FRIEND_MED, LIKE2),
            Relation(LibertyCivilians, FRIEND_MED, LIKE2),
            Relation(BretoniaCivilians, FRIEND_MED, LIKE2),
            Relation(KusariCivilians, FRIEND_MED, LIKE4),

            Relation(RheinlandTraders, FRIEND_MED, LIKE2),
            Relation(LibertyTraders, FRIEND_MED, LIKE2),
            Relation(BretoniaTraders, FRIEND_MED, LIKE2),
            Relation(KusariTraders, FRIEND_MED, LIKE3),
            # Relation(BorderWorldTraders, NEUTRAL, LIKE2),

            Relation(RheinlandPirate, FRIEND_MED, HATE3),
            Relation(LibertyPirate, FRIEND_MED, HATE2),
            Relation(BretoniaPirate, FRIEND_MED, HATE3),
            Relation(KusariPirate, FRIEND_MED, HATE5),
            Relation(BorderWorldPirate, FRIEND_MED, HATE2),

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

            Relation(Nomad, FRIEND_MED),
        ]
    ),

    ### TRADERS

    FactionRelation(
        RheinlandTraders,
        [
            Relation(RheinlandMain, FRIEND_MED),
            Relation(LibertyMain, FRIEND_MED),
            Relation(BretoniaMain, FRIEND_MED),
            Relation(KusariMain, FRIEND_MED),

            Relation(RheinlandHunters, NEUTRAL, LIKE2),
            Relation(LibertyHunters, NEUTRAL, LIKE1),
            Relation(BretoniaHunters, NEUTRAL, LIKE1),
            Relation(KusariHunters, NEUTRAL, LIKE1),

            Relation(RheinlandCivilians, FRIEND_MED, LIKE4),
            Relation(LibertyCivilians, FRIEND_MED, LIKE2),
            Relation(BretoniaCivilians, FRIEND_MED, LIKE2),
            Relation(KusariCivilians, FRIEND_MED, LIKE2),

            Relation(RheinlandTraders, FRIEND_MED, LIKE3),
            Relation(LibertyTraders, FRIEND_MED, LIKE2),
            Relation(BretoniaTraders, FRIEND_MED, LIKE2),
            Relation(KusariTraders, FRIEND_MED, LIKE2),
            # Relation(BorderWorldTraders, NEUTRAL, LIKE2),

            Relation(RheinlandPirate, FRIEND_MED, HATE5),
            Relation(LibertyPirate, FRIEND_MED, HATE3),
            Relation(BretoniaPirate, FRIEND_MED, HATE2),
            Relation(KusariPirate, FRIEND_MED, HATE3),
            Relation(BorderWorldPirate, FRIEND_MED, HATE1),

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

            Relation(Nomad, FRIEND_MED),
            Relation(DeidrichPeople, FRIEND_MED),
        ]
    ),

    FactionRelation(
        LibertyTraders,
        [
            Relation(RheinlandMain, FRIEND_MED),
            Relation(LibertyMain, FRIEND_MED),
            Relation(BretoniaMain, FRIEND_MED),
            Relation(KusariMain, FRIEND_MED),

            Relation(RheinlandHunters, NEUTRAL, LIKE1),
            Relation(LibertyHunters, NEUTRAL, LIKE2),
            Relation(BretoniaHunters, NEUTRAL, LIKE1),
            Relation(KusariHunters, NEUTRAL, LIKE1),

            Relation(RheinlandCivilians, FRIEND_MED, LIKE2),
            Relation(LibertyCivilians, FRIEND_MED, LIKE4),
            Relation(BretoniaCivilians, FRIEND_MED, LIKE2),
            Relation(KusariCivilians, FRIEND_MED, LIKE2),

            Relation(RheinlandTraders, FRIEND_MED, LIKE2),
            Relation(LibertyTraders, FRIEND_MED, LIKE3),
            Relation(BretoniaTraders, FRIEND_MED, LIKE2),
            Relation(KusariTraders, FRIEND_MED, LIKE2),
            # Relation(BorderWorldTraders, NEUTRAL, LIKE2),

            Relation(RheinlandPirate, FRIEND_MED, HATE3),
            Relation(LibertyPirate, FRIEND_MED, HATE5),
            Relation(BretoniaPirate, FRIEND_MED, HATE3),
            Relation(KusariPirate, FRIEND_MED, HATE2),
            Relation(BorderWorldPirate, FRIEND_MED, HATE1),

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

            Relation(Nomad, FRIEND_MED),
        ]
    ),

    FactionRelation(
        BretoniaTraders,
        [
            Relation(RheinlandMain, FRIEND_MED),
            Relation(LibertyMain, FRIEND_MED),
            Relation(BretoniaMain, FRIEND_MED),
            Relation(KusariMain, FRIEND_MED),

            Relation(RheinlandHunters, NEUTRAL, LIKE1),
            Relation(LibertyHunters, NEUTRAL, LIKE1),
            Relation(BretoniaHunters, NEUTRAL, LIKE2),
            Relation(KusariHunters, NEUTRAL, LIKE1),

            Relation(RheinlandCivilians, FRIEND_MED, LIKE2),
            Relation(LibertyCivilians, FRIEND_MED, LIKE2),
            Relation(BretoniaCivilians, FRIEND_MED, LIKE2),
            Relation(KusariCivilians, FRIEND_MED, LIKE2),

            Relation(RheinlandTraders, FRIEND_MED, LIKE2),
            Relation(LibertyTraders, FRIEND_MED, LIKE3),
            Relation(BretoniaTraders, FRIEND_MED, LIKE2),
            Relation(KusariTraders, FRIEND_MED, LIKE2),
            # Relation(BorderWorldTraders, NEUTRAL, LIKE2),

            Relation(RheinlandPirate, FRIEND_MED, HATE3),
            Relation(LibertyPirate, FRIEND_MED, HATE5),
            Relation(BretoniaPirate, FRIEND_MED, HATE3),
            Relation(KusariPirate, FRIEND_MED, HATE2),
            Relation(BorderWorldPirate, FRIEND_MED, HATE1),

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

            Relation(Nomad, FRIEND_MED),
        ]
    ),

    FactionRelation(
        KusariTraders,
        [
            Relation(RheinlandMain, FRIEND_MED),
            Relation(LibertyMain, FRIEND_MED),
            Relation(BretoniaMain, FRIEND_MED),
            Relation(KusariMain, FRIEND_MED),

            Relation(RheinlandHunters, NEUTRAL, LIKE1),
            Relation(LibertyHunters, NEUTRAL, LIKE1),
            Relation(BretoniaHunters, NEUTRAL, LIKE1),
            Relation(KusariHunters, NEUTRAL, LIKE2),

            Relation(RheinlandCivilians, FRIEND_MED, LIKE2),
            Relation(LibertyCivilians, FRIEND_MED, LIKE2),
            Relation(BretoniaCivilians, FRIEND_MED, LIKE2),
            Relation(KusariCivilians, FRIEND_MED, LIKE4),

            Relation(RheinlandTraders, FRIEND_MED, LIKE2),
            Relation(LibertyTraders, FRIEND_MED, LIKE2),
            Relation(BretoniaTraders, FRIEND_MED, LIKE2),
            Relation(KusariTraders, FRIEND_MED, LIKE3),
            # Relation(BorderWorldTraders, NEUTRAL, LIKE2),

            Relation(RheinlandPirate, FRIEND_MED, HATE3),
            Relation(LibertyPirate, FRIEND_MED, HATE2),
            Relation(BretoniaPirate, FRIEND_MED, HATE3),
            Relation(KusariPirate, FRIEND_MED, HATE5),
            Relation(BorderWorldPirate, FRIEND_MED, HATE2),

            Relation(Corsairs, ENEMY_MED, HATE3),
            Relation(Outcasts, NEUTRAL),

            Relation(Hessians, ENEMY_MED, HATE5),
            # Relation(Junkers, ENEMY_MIN, HATE2),
            Relation(LibertyRogues, ENEMY_MED, HATE1),
            Relation(Starline, ENEMY_MED, HATE1),
            Relation(LaneHackers, ENEMY_MED, HATE4),
            Relation(Xenos, ENEMY_MED, HATE8),
            Relation(Ireland, ENEMY_MED, HATE5),
            Relation(Shinobi, ENEMY_MED, HATE7),
            Relation(FarmerAlliance, ENEMY_MED, HATE9),

            Relation(Nomad, FRIEND_MED),
        ]
    ),
    #
    # FactionRelation(
    #     BorderWorldTraders,
    #     [
    #         Relation(RheinlandMain, FRIEND_MED),
    #         Relation(LibertyMain, FRIEND_MED),
    #         Relation(BretoniaMain, FRIEND_MED),
    #         Relation(KusariMain, FRIEND_MED),
    #
    #         Relation(RheinlandHunters, NEUTRAL, LIKE1),
    #         Relation(LibertyHunters, NEUTRAL, LIKE1),
    #         Relation(BretoniaHunters, NEUTRAL, LIKE1),
    #         Relation(KusariHunters, NEUTRAL, LIKE2),
    #
    #         Relation(RheinlandCivilians, NEUTRAL, LIKE2),
    #         Relation(LibertyCivilians, NEUTRAL, LIKE2),
    #         Relation(BretoniaCivilians, NEUTRAL, LIKE2),
    #         Relation(KusariCivilians, NEUTRAL, LIKE4),
    #
    #         Relation(RheinlandTraders, FRIEND_MED, LIKE2),
    #         Relation(LibertyTraders, FRIEND_MED, LIKE2),
    #         Relation(BretoniaTraders, FRIEND_MED, LIKE2),
    #         Relation(KusariTraders, FRIEND_MED, LIKE3),
    #         Relation(BorderWorldTraders, NEUTRAL, LIKE2),
    #
    #         Relation(RheinlandPirate, FRIEND_MED, HATE3),
    #         Relation(LibertyPirate, FRIEND_MED, HATE2),
    #         Relation(BretoniaPirate, FRIEND_MED, HATE3),
    #         Relation(KusariPirate, FRIEND_MED, HATE5),
    #         Relation(BorderWorldPirate, FRIEND_MED, HATE2),
    #
    #         Relation(Corsairs, NEUTRAL),
    #         Relation(Outcasts, NEUTRAL),
    #
    #         Relation(Hessians, ENEMY_MED, HATE5),
    #         Relation(Junkers, ENEMY_MIN, HATE2),
    #         Relation(LibertyRogues, ENEMY_MED, HATE1),
    #         Relation(Starline, ENEMY_MED, HATE1),
    #         Relation(LaneHackers, ENEMY_MED, HATE4),
    #         Relation(Xenos, ENEMY_MED, HATE8),
    #         Relation(Ireland, ENEMY_MED, HATE5),
    #         Relation(Shinobi, ENEMY_MED, HATE7),
    #         Relation(FarmerAlliance, ENEMY_MED, HATE9),
    #
    #         Relation(Nomad, FRIEND_MED),
    #     ]
    # ),

    FactionRelation(
        Nomad,
        [
            Relation(RheinlandMain, FRIEND_MED),
            Relation(LibertyMain, FRIEND_MED),
            Relation(BretoniaMain, FRIEND_MED),
            Relation(KusariMain, FRIEND_MED),

            Relation(RheinlandHunters, FRIEND_MED),
            Relation(LibertyHunters, FRIEND_MED),
            Relation(BretoniaHunters, FRIEND_MED),
            Relation(KusariHunters, FRIEND_MED),

            Relation(RheinlandCivilians, FRIEND_MED),
            Relation(LibertyCivilians, FRIEND_MED),
            Relation(BretoniaCivilians, FRIEND_MED),
            Relation(KusariCivilians, FRIEND_MED),

            Relation(RheinlandTraders, FRIEND_MED),
            Relation(LibertyTraders, FRIEND_MED),
            Relation(BretoniaTraders, FRIEND_MED),
            Relation(KusariTraders, FRIEND_MED),
            # Relation(BorderWorldTraders, FRIEND_MED),

            Relation(RheinlandPirate, FRIEND_MED),
            Relation(LibertyPirate, FRIEND_MED),
            Relation(BretoniaPirate, FRIEND_MED),
            Relation(KusariPirate, FRIEND_MED),
            Relation(BorderWorldPirate, FRIEND_MED),

            Relation(Corsairs, FRIEND_MED),
            Relation(Outcasts, FRIEND_MED),
            Relation(OrderMain, FRIEND_MED),
            Relation(ASF, FRIEND_MED),

            Relation(Corsairs, FRIEND_MED),
            Relation(Outcasts, FRIEND_MED),
            Relation(OrderMain, FRIEND_MED),
            Relation(ASF, FRIEND_MED),

            Relation(Unknown, FRIEND_MED),
            # Relation(RheinlandSmuggler, FRIEND_MED),
            # Relation(LibertySmuggler, FRIEND_MED),
            # Relation(BretoniaSmuggler, FRIEND_MED),
            # Relation(KusariSmuggler, FRIEND_MED),
            # Relation(BorderWorldSmuggler, FRIEND_MED),

            Relation(Hessians, FRIEND_MED),
            Relation(Junkers, FRIEND_MED),
            Relation(LibertyRogues, FRIEND_MED),
            Relation(Starline, FRIEND_MED),
            Relation(LaneHackers, FRIEND_MED),
            Relation(Xenos, FRIEND_MED),
            Relation(Ireland, FRIEND_MED),
            Relation(Shinobi, FRIEND_MED),
            Relation(FarmerAlliance, FRIEND_MED),
        ]
    ),

    FactionRelation(
        Corsairs,
        [
            Relation(Outcasts, ENEMY_MED, HATE1),

            Relation(RheinlandHunters, FRIEND_MED),
            Relation(LibertyHunters, FRIEND_MED),
            Relation(BretoniaHunters, FRIEND_MED),
            Relation(KusariHunters, FRIEND_MED),
            # Relation(BorderWorldHunters, FRIEND_MED),

            Relation(Hessians, FRIEND_MED, HATE3),
            Relation(Junkers, NEUTRAL),
            Relation(LibertyRogues, NEUTRAL),
            Relation(Starline, FRIEND_MED, HATE2),
            Relation(LaneHackers, ENEMY_MIN),
            Relation(Xenos, FRIEND_MED, HATE5),
            Relation(Ireland, ENEMY_MIN),
            Relation(Shinobi, FRIEND_MED, HATE3),
            Relation(FarmerAlliance, ENEMY_MIN),
        ]
    ),

    FactionRelation(
        Outcasts,
        [
            Relation(RheinlandHunters, FRIEND_MED),
            Relation(LibertyHunters, FRIEND_MED),
            Relation(BretoniaHunters, FRIEND_MED),
            Relation(KusariHunters, FRIEND_MED),
            # Relation(BorderWorldHunters, FRIEND_MED),

            Relation(Hessians, NEUTRAL),
            Relation(Junkers, NEUTRAL),
            Relation(LibertyRogues, NEUTRAL),
            Relation(Starline, FRIEND_MED, HATE6),
            Relation(LaneHackers, ENEMY_MIN),
            Relation(Xenos, FRIEND_MED, HATE3),
            Relation(Ireland, ENEMY_MIN),
            Relation(Shinobi, FRIEND_MED, HATE1),
            Relation(FarmerAlliance, ENEMY_MIN),
        ]
    ),

    FactionRelation(
        Outcasts,
        [
            Relation(RheinlandHunters, FRIEND_MED),
            Relation(LibertyHunters, FRIEND_MED),
            Relation(BretoniaHunters, FRIEND_MED),
            Relation(KusariHunters, FRIEND_MED),
            # Relation(BorderWorldHunters, FRIEND_MED),

            Relation(Hessians, NEUTRAL),
            Relation(Junkers, NEUTRAL),
            Relation(LibertyRogues, NEUTRAL),
            Relation(Starline, FRIEND_MED, HATE6),
            Relation(LaneHackers, ENEMY_MIN),
            Relation(Xenos, FRIEND_MED, HATE3),
            Relation(Ireland, ENEMY_MIN),
            Relation(Shinobi, FRIEND_MED, HATE1),
            Relation(FarmerAlliance, ENEMY_MIN),
        ]
    ),


]
