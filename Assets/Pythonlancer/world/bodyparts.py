from random import choice, shuffle, randint

GUARD = 1
ELITE = 2
TRADER = 3
PEASANT = 4
JOURNEYMAN = 5
BARTENDER = 6
FAT = 7
GENERAL = 8
SCIENT = 9
PIRATE = 10
ORDER = 11
PLAYER = 12
ROBOT = 13
HERO = 14
SALES = 15
MILITARY = 16
CAPTAIN = 17
GENERIC = 18
MONKEY = 19

RHEINLAND = 1
LIBERTY = 2
BRETONIA = 3
KUSARI = 4
BORDER_WORLD = 5


BENCHMARK_MALE_HAND_RIGHT = 'benchmark_male_hand_right'
BENCHMARK_MALE_HAND_LEFT = 'benchmark_male_hand_left'
MALE_HAND_RIGHT_BLACK = 'male_hand_right_black'
MALE_HAND_LEFT_BLACK = 'male_hand_left_black'
ROBOT_HAND_RIGHT = 'robot_hand_right'
ROBOT_HAND_LEFT = 'robot_hand_left'
ROBOT_HAND_RIGHTB = 'robot_hand_rightb'
ROBOT_HAND_LEFTB = 'robot_hand_leftb'

BENCHMARK_FEMALE_HAND_RIGHT = 'benchmark_female_hand_right'
BENCHMARK_FEMALE_HAND_LEFT = 'benchmark_female_hand_left'
FEMALE_HAND_RIGHT_BLACK = 'female_hand_right_black'
FEMALE_HAND_LEFT_BLACK = 'female_hand_left_black'

MALE_WHITE_HANDS = [BENCHMARK_MALE_HAND_LEFT, BENCHMARK_MALE_HAND_RIGHT]
MALE_BLACK_HANDS = [MALE_HAND_LEFT_BLACK, MALE_HAND_RIGHT_BLACK]
FEMALE_WHITE_HANDS = [BENCHMARK_FEMALE_HAND_LEFT, BENCHMARK_FEMALE_HAND_RIGHT]
FEMALE_BLACK_HANDS = [FEMALE_HAND_LEFT_BLACK, FEMALE_HAND_RIGHT_BLACK]
ROBO_HANDS = [ROBOT_HAND_LEFT, ROBOT_HAND_RIGHT]
ROBO_HANDS_B = [ROBOT_HAND_LEFTB, ROBOT_HAND_RIGHTB]

PROP_NEURALNET_A = 'prop_neuralnet_a'
PROP_NEURALNET_A_COMBO = 'prop_neuralnet_a_combo'
PROP_NEURALNET_A_RIGHT = 'prop_neuralnet_a_right'
PROP_NEURALNET_B = 'prop_neuralnet_b'
PROP_NEURALNET_B_COMBO = 'prop_neuralnet_b_combo'
PROP_NEURALNET_B_RIGHT = 'prop_neuralnet_b_right'
PROP_NEURALNET_C = 'prop_neuralnet_c'
PROP_NEURALNET_C_COMBO = 'prop_neuralnet_c_combo'
PROP_NEURALNET_C_RIGHT = 'prop_neuralnet_c_right'
PROP_NEURALNET_D = 'prop_neuralnet_d'
PROP_NEURALNET_D_COMBO = 'prop_neuralnet_d_combo'
PROP_NEURALNET_D_RIGHT = 'prop_neuralnet_d_right'
PROP_NEURALNET_F_UP = 'prop_neuralnet_f_up'
PROP_NEURALNET_F_UP_RIGHT = 'prop_neuralnet_f_up_right'
PROP_NEURALNET_E_COMBO = 'prop_neuralnet_e_combo'
PROP_NEURALNET_E_RIGHT = 'prop_neuralnet_e_right'
PROP_NEURALNET_E = 'prop_neuralnet_e'
PROP_NEURALNET_F_RIGHT = 'prop_neuralnet_f_right'
PROP_NEURALNET_F = 'prop_neuralnet_f'

NN_A = [
    PROP_NEURALNET_A,
    PROP_NEURALNET_A_COMBO,
    PROP_NEURALNET_A_RIGHT,
]
NN_B = [
    PROP_NEURALNET_B,
    PROP_NEURALNET_B_COMBO,
    PROP_NEURALNET_B_RIGHT,
]
NN_C = [
    PROP_NEURALNET_C,
    PROP_NEURALNET_C_COMBO,
    PROP_NEURALNET_C_RIGHT,
]
NN_D = [
    PROP_NEURALNET_D,
    PROP_NEURALNET_D_COMBO,
    PROP_NEURALNET_D_RIGHT,
]
NN_E = [
    PROP_NEURALNET_E,
    PROP_NEURALNET_E_COMBO,
    PROP_NEURALNET_E_RIGHT,
]
NN_F = [
    PROP_NEURALNET_F,
    PROP_NEURALNET_F_RIGHT,
    PROP_NEURALNET_F_UP,
    PROP_NEURALNET_F_UP_RIGHT,
]

TRADER_NN = NN_A + NN_E
PEASANT_NN = NN_B + NN_C + NN_D + NN_F

PROP_SHADES_01 = 'prop_shades_01'
PROP_SHADES_02 = 'prop_shades_02'
PROP_SHADES_03 = 'prop_shades_03'
PROP_SHADES_04 = 'prop_shades_04'
PROP_SHADES_05 = 'prop_shades_05'
PROP_SHADES_01_FEM = 'prop_shades_01_fem'
PROP_SHADES_02_FEM = 'prop_shades_02_fem'
PROP_SHADES_03_FEM = 'prop_shades_03_fem'
PROP_SHADES_04_FEM = 'prop_shades_04_fem'
PROP_SHADES_05_FEM = 'prop_shades_05_fem'

MALE_SHADES = [PROP_SHADES_01, PROP_SHADES_02, PROP_SHADES_03, PROP_SHADES_04, PROP_SHADES_05]
FEMALE_SHADES = [PROP_SHADES_01_FEM, PROP_SHADES_02_FEM, PROP_SHADES_03_FEM, PROP_SHADES_04_FEM, PROP_SHADES_05_FEM]

PROP_MASK_OUTCAST = 'prop_mask_outcast'
PROP_MASK_OUTCAST_FEM = 'prop_mask_outcast_fem'
PROP_HAT_FEMALE_BR_ELITE = 'prop_hat_female_br_elite'
PROP_HAT_FEMALE_BR_ELITE_VISOR = 'prop_hat_female_br_elite_visor'
PROP_HAT_FEMALE_BR_GRD = 'prop_hat_female_br_grd'
PROP_HAT_FEMALE_BR_GRD_VISOR = 'prop_hat_female_br_grd_visor'
PROP_HAT_FEMALE_CAP_A = 'prop_hat_female_cap_a'
PROP_HAT_FEMALE_KU_ELITE = 'prop_hat_female_ku_elite'
PROP_HAT_FEMALE_KU_ELITE_VISOR = 'prop_hat_female_ku_elite_visor'
PROP_HAT_FEMALE_LI_ELITE = 'prop_hat_female_li_elite'
PROP_HAT_FEMALE_LI_ELITE_VISOR = 'prop_hat_female_li_elite_visor'
PROP_HAT_FEMALE_LI_GRD = 'prop_hat_female_li_grd'
PROP_HAT_FEMALE_LI_GRD_VISOR = 'prop_hat_female_li_grd_visor'
PROP_HAT_FEMALE_MINER = 'prop_hat_female_miner'
PROP_HAT_FEMALE_MINER_VISOR = 'prop_hat_female_miner_visor'
PROP_HAT_FEMALE_PIRATE_A = 'prop_hat_female_pirate_a'
PROP_HAT_FEMALE_PIRATE_B = 'prop_hat_female_pirate_b'
PROP_HAT_FEMALE_PIRATE_B_VISOR = 'prop_hat_female_pirate_b_visor'
PROP_HAT_FEMALE_POLICE = 'prop_hat_female_police'
PROP_HAT_FEMALE_POLICE_VISOR = 'prop_hat_female_police_visor'
PROP_HAT_FEMALE_RH_ELITE = 'prop_hat_female_rh_elite'
PROP_HAT_FEMALE_RH_ELITE_VISOR = 'prop_hat_female_rh_elite_visor'
PROP_HAT_MALE_BR_ELITE = 'prop_hat_male_br_elite'
PROP_HAT_MALE_BR_ELITE_VISOR = 'prop_hat_male_br_elite_visor'
PROP_HAT_MALE_BR_GRD = 'prop_hat_male_br_grd'
PROP_HAT_MALE_BR_GRD_VISOR = 'prop_hat_male_br_grd_visor'
PROP_HAT_MALE_CAP_A = 'prop_hat_male_cap_a'
PROP_HAT_MALE_KU_ELITE = 'prop_hat_male_ku_elite'
PROP_HAT_MALE_KU_ELITE_VISOR = 'prop_hat_male_ku_elite_visor'
PROP_HAT_MALE_LI_ELITE = 'prop_hat_male_li_elite'
PROP_HAT_MALE_LI_ELITE_VISOR = 'prop_hat_male_li_elite_visor'
PROP_HAT_MALE_LI_GRD = 'prop_hat_male_li_grd'
PROP_HAT_MALE_LI_GRD_VISOR = 'prop_hat_male_li_grd_visor'
PROP_HAT_MALE_MINER = 'prop_hat_male_miner'
PROP_HAT_MALE_MINER_VISOR = 'prop_hat_male_miner_visor'
PROP_HAT_MALE_PIRATE_A = 'prop_hat_male_pirate_a'
PROP_HAT_MALE_PIRATE_B = 'prop_hat_male_pirate_b'
PROP_HAT_MALE_PIRATE_B_VISOR = 'prop_hat_male_pirate_b_visor'
PROP_HAT_MALE_POLICE = 'prop_hat_male_police'
PROP_HAT_MALE_POLICE_VISOR = 'prop_hat_male_police_visor'
PROP_HAT_MALE_RH_ELITE = 'prop_hat_male_rh_elite'
PROP_HAT_MALE_RH_ELITE_VISOR = 'prop_hat_male_rh_elite_visor'
PROP_HAT_FEMALE_KU_GRD = 'prop_hat_female_ku_grd'
PROP_HAT_FEMALE_KU_GRD_VISOR = 'prop_hat_female_ku_grd_visor'
PROP_HAT_FEMALE_RH_GRD = 'prop_hat_female_rh_grd'
PROP_HAT_FEMALE_RH_GRD_VISOR = 'prop_hat_female_rh_grd_visor'
PROP_HAT_MALE_KU_GRD = 'prop_hat_male_ku_grd'
PROP_HAT_MALE_KU_GRD_VISOR = 'prop_hat_male_ku_grd_visor'
PROP_HAT_MALE_RH_GRD = 'prop_hat_male_rh_grd'
PROP_HAT_MALE_RH_GRD_VISOR = 'prop_hat_male_rh_grd_visor'
COMM_BR_BRIGHTON = 'comm_br_brighton'
COMM_BR_BRIGHTON_FEMALE = 'comm_br_brighton_female'
COMM_BR_DARCY = 'comm_br_darcy'
COMM_BR_DARCY_FEMALE = 'comm_br_darcy_female'
COMM_BR_KAITLYN = 'comm_br_kaitlyn'
COMM_BR_KAITLYN_FEMALE = 'comm_br_kaitlyn_female'
COMM_GE_GENERIC1 = 'comm_ge_generic1'
COMM_GE_GENERIC1_FEMALE = 'comm_ge_generic1_female'
COMM_GE_GENERIC2 = 'comm_ge_generic2'
COMM_GE_GENERIC2_FEMALE = 'comm_ge_generic2_female'
COMM_KU_KYM = 'comm_ku_kym'
COMM_KU_KYM_FEMALE = 'comm_ku_kym_female'
COMM_LI_HATCHER = 'comm_li_hatcher'
COMM_LI_HATCHER_FEMALE = 'comm_li_hatcher_female'
COMM_PI_PIRATE = 'comm_pi_pirate'
COMM_PI_PIRATE_FEMALE = 'comm_pi_pirate_female'
COMM_PL_PLAYER = 'comm_pl_player'
COMM_PL_PLAYER_FEMALE = 'comm_pl_player_female'
COMM_RH_ALARIC = 'comm_rh_alaric'
COMM_RH_ALARIC_FEMALE = 'comm_rh_alaric_female'
COMM_RH_REICHMAN = 'comm_rh_reichman'
COMM_RH_REICHMAN_FEMALE = 'comm_rh_reichman_female'
COMM_RH_WILHAM = 'comm_rh_wilham'
COMM_RH_WILHAM_FEMALE = 'comm_rh_wilham_female'
COMM_BR_ELITE = 'comm_br_elite'
COMM_RH_ELITE = 'comm_rh_elite'
COMM_LI_ELITE = 'comm_li_elite'
COMM_KU_ELITE = 'comm_ku_elite'
COMM_BR_ELITE_FEMALE = 'comm_br_elite_female'
COMM_RH_ELITE_FEMALE = 'comm_rh_elite_female'
COMM_LI_ELITE_FEMALE = 'comm_li_elite_female'
COMM_KU_ELITE_FEMALE = 'comm_ku_elite_female'
COMM_BR_GUARD = 'comm_br_guard'
COMM_RH_GUARD = 'comm_rh_guard'
COMM_LI_GUARD = 'comm_li_guard'
COMM_KU_GUARD = 'comm_ku_guard'
COMM_BR_GUARD_FEMALE = 'comm_br_guard_female'
COMM_RH_GUARD_FEMALE = 'comm_rh_guard_female'
COMM_LI_GUARD_FEMALE = 'comm_li_guard_female'
COMM_KU_GUARD_FEMALE = 'comm_ku_guard_female'
NEW_FEM_GLASSES = 'new_fem_glasses'


def load_items_by_usage(items):
    result = {}
    for item in items:
        usage = item.get_usage()
        if usage not in result:
            result[usage] = [item]
        else:
            result[usage].append(item)
    return result


def get_male_shades():
    if randint(0, 3) == 1:
        return choice(MALE_SHADES)


def get_female_shades():
    if randint(0, 3) == 1:
        return choice(FEMALE_SHADES)


def get_trader_nn():
    if randint(0, 1) == 1:
        return choice(TRADER_NN)


def get_peasant_nn():
    if randint(0, 2) == 1:
        return choice(PEASANT_NN)


class Body:

    def get_name(self):
        raise NotImplementedError

    def get_usage(self):
        raise NotImplementedError


class MaleBody:

    def __init__(self, name, usage):
        self.name = name
        self.usage = usage

    def get_name(self):
        return self.name

    def get_usage(self):
        return self.usage


class FemaleBody:

    def __init__(self, name, usage, bust=False, white_important=False):
        self.name = name
        self.usage = usage
        self.bust = bust
        self.white_important = white_important

    def get_name(self):
        return self.name

    def get_usage(self):
        return self.usage

    def have_bust(self):
        return self.bust

    def white_is_important(self):
        return self.white_important


class PartsStore:
    MALE_HATS = {}
    FEMALE_HATS = {}
    MALE = []
    FEMALE = []

    def __init__(self):
        self.male_per_type = load_items_by_usage(self.MALE)
        self.female_per_type = load_items_by_usage(self.FEMALE)

    def get_male(self, *usages):
        bodies = []
        for usage in usages:
            bodies.extend(self.male_per_type[usage])
        return choice(bodies)

    def get_female(self, *usages, bust=False, white_important=False):
        choosed_bodies = []
        for usage in usages:
            for body in self.female_per_type[usage]:
                if white_important and body.is_black():
                    continue

                if bust:
                    if body.have_bust():
                        choosed_bodies.append(body)
                else:
                    if not body.have_bust():
                        choosed_bodies.append(body)

        if len(choosed_bodies) == 0:
            raise Exception('no body for query')

        return choice(choosed_bodies)

    def get_male_hat(self, usage, hat_mandatory=False):
        use_hat = randint(0, 1) == 1
        if hat_mandatory or use_hat:
            return choice(self.MALE_HATS[usage])

    def get_female_hat(self, usage, hat_mandatory=False):
        use_hat = randint(0, 1) == 1
        if hat_mandatory or use_hat:
            return choice(self.FEMALE_HATS[usage])


class LibertyBodyStore(PartsStore):
    MALE_HATS = {
        MILITARY: [
            PROP_HAT_MALE_LI_ELITE,
            PROP_HAT_MALE_LI_ELITE_VISOR,
        ]
    }
    FEMALE_HATS = {
        MILITARY: [
            PROP_HAT_FEMALE_LI_ELITE,
            PROP_HAT_FEMALE_LI_ELITE_VISOR,
        ]
    }
    MALE = [
        MaleBody('li_bartender_body', BARTENDER),
        MaleBody('li_commtrader_body', TRADER),
        MaleBody('li_male_guard_body', GUARD),
        MaleBody('li_male_elite_body', ELITE),
        MaleBody('li_manhattan_bartender_body', FAT),
        MaleBody('li_scrote_body', GENERAL),
        MaleBody('li_shipdealer_body', TRADER),
        MaleBody('li_tilton_body_alt', GENERAL),
        MaleBody('li_rockford_body', TRADER),
    ]
    FEMALE = [
        FemaleBody('li_female_elite_body', ELITE),
        FemaleBody('li_female_guard_body', GUARD),
        FemaleBody('li_hatcher_body', GENERAL),
        FemaleBody('br_karina_body', TRADER),
    ]


class BretoniaBodyStore(PartsStore):
    MALE_HATS = {
        MILITARY: [
            PROP_HAT_MALE_BR_ELITE,
            PROP_HAT_MALE_BR_ELITE_VISOR,
            PROP_HAT_MALE_BR_GRD,
            PROP_HAT_MALE_BR_GRD_VISOR,
        ]
    }
    FEMALE_HATS = {
        MILITARY: [
            PROP_HAT_FEMALE_BR_ELITE,
            PROP_HAT_FEMALE_BR_ELITE_VISOR,
            PROP_HAT_FEMALE_BR_GRD,
            PROP_HAT_FEMALE_BR_GRD_VISOR,
        ]
    }
    MALE = [
        MaleBody('br_bartender_body', BARTENDER),
        MaleBody('br_brighton_body', GENERAL),
        MaleBody('br_commtrader_body', TRADER),
        MaleBody('br_male_elite_body', ELITE),
        MaleBody('br_male_guard_body', GUARD),
        MaleBody('br_quigly_body', TRADER),
        MaleBody('br_shipdealer_body', TRADER),
        MaleBody('br_tobias_body', FAT),
        MaleBody('li_rockford_body', TRADER),
    ]
    FEMALE = [
        FemaleBody('br_darcy_body', GENERAL),
        FemaleBody('br_female_elite_body', ELITE),
        FemaleBody('br_female_guard_body', GUARD),
        FemaleBody('br_kaitlyn_body', TRADER),
        FemaleBody('br_karina_body', TRADER),
    ]


class KusariBodyStore(PartsStore):
    MALE_HATS = {
        MILITARY: [
            PROP_HAT_MALE_KU_ELITE,
            PROP_HAT_MALE_KU_ELITE_VISOR,
            PROP_HAT_MALE_KU_GRD,
            PROP_HAT_MALE_KU_GRD_VISOR,
        ]
    }
    FEMALE_HATS = {
        MILITARY: [
            PROP_HAT_FEMALE_KU_ELITE,
            PROP_HAT_FEMALE_KU_ELITE_VISOR,
            PROP_HAT_FEMALE_KU_GRD,
            PROP_HAT_FEMALE_KU_GRD_VISOR,
        ]
    }
    MALE = [
        MaleBody('ku_bartender_body', BARTENDER),
        MaleBody('ku_commtrader_body', TRADER),
        MaleBody('ku_edo_body', FAT),
        MaleBody('ku_male_elite_body', ELITE),
        MaleBody('ku_male_guard_body', GUARD),
        MaleBody('ku_shipdealer_body', TRADER),
        MaleBody('li_rockford_body', TRADER),
    ]
    FEMALE = [
        FemaleBody('ku_kym_body', TRADER, bust=True, white_important=True),
        FemaleBody('ku_kym_body_gen', TRADER, white_important=True),
        FemaleBody('ku_kym_body_bust', TRADER, bust=True),
        FemaleBody('ku_female_elite_body', ELITE),
        FemaleBody('ku_female_guard_body', GUARD),
        FemaleBody('br_karina_body', TRADER),
    ]


class RheinlandBodyStore(PartsStore):
    MALE_HATS = {
        MILITARY: [
            PROP_HAT_MALE_RH_ELITE,
            PROP_HAT_MALE_RH_ELITE_VISOR,
        ]
    }
    FEMALE_HATS = {
        MILITARY: [
            PROP_HAT_FEMALE_RH_ELITE,
            PROP_HAT_FEMALE_RH_ELITE_VISOR,
        ]
    }
    MALE = [
        MaleBody('rh_bartender_body', BARTENDER),
        MaleBody('rh_commtrader_body', TRADER),
        MaleBody('rh_deidrich_body', GENERAL),
        MaleBody('rh_male_elite_body', ELITE),
        MaleBody('rh_male_guard_body', GUARD),
        MaleBody('rh_reichman_body', GENERAL),
        MaleBody('rh_shipdealer_body', TRADER),
        MaleBody('rh_wilham_body', GENERAL),
        MaleBody('li_rockford_body', TRADER),
    ]
    FEMALE = [
        FemaleBody('rh_female_elite_body', ELITE),
        FemaleBody('rh_female_guard_body', GUARD),
        FemaleBody('rh_greunwald_body', GENERAL, bust=True),
        FemaleBody('br_karina_body', TRADER),
    ]


class GenericBodyStore(PartsStore):
    MALE = [
        MaleBody('pl_male1_journeyman_body', JOURNEYMAN),
        MaleBody('pl_male1_peasant_body', PEASANT),
        MaleBody('pl_male2_journeyman_body', PLAYER),
        MaleBody('pl_male2_peasant_body', PEASANT),
        MaleBody('pl_male3_journeyman_body', JOURNEYMAN),
        MaleBody('pl_male3_peasant_body', PEASANT),
        # MaleBody('pl_male3_peasant_body_hurt', JOURNEYMAN),
        MaleBody('pi_orillion_body', ORDER),
        MaleBody('pi_pirate1_body', PIRATE),
        MaleBody('pi_pirate2_body', PIRATE),
        MaleBody('pi_pirate3_body', PIRATE),
        MaleBody('pi_pirate4_body', PIRATE),
        MaleBody('pi_pirate5_body', PIRATE),
        MaleBody('pi_pirate6_body', PIRATE),
        MaleBody('pi_pirate7_body', PIRATE),
        MaleBody('pi_pirate8_body', PIRATE),
        MaleBody('pl_trent_body', PLAYER),
        MaleBody('sc_scientist1_body', SCIENT),
        MaleBody('sc_scientist2_body', SCIENT),
        MaleBody('sc_scientist3_body', SCIENT),
        MaleBody('sc_scientist4_body', SCIENT),
        MaleBody('sh_male1_body', JOURNEYMAN),
        MaleBody('sh_male2_body', JOURNEYMAN),
        MaleBody('sh_male3_body', JOURNEYMAN),
        MaleBody('robot_body_a', ROBOT),
        MaleBody('robot_body_b', ROBOT),
        MaleBody('robot_body_c', ROBOT),
        MaleBody('robot_body_d', ROBOT),
        MaleBody('robot_body_e', ROBOT),
    ]
    FEMALE = [
        FemaleBody('pl_female1_journeyman_body', JOURNEYMAN),
        FemaleBody('pl_female1_peasant_body', PEASANT),
        FemaleBody('pl_female2_journeyman_body', JOURNEYMAN),
        FemaleBody('pl_female2_peasant_body', PEASANT),
        FemaleBody('sc_female1_body', SCIENT),
        FemaleBody('sh_female1_body', PIRATE),
        FemaleBody('pl_female1_peasant_body_bust', PEASANT, bust=True),
        FemaleBody('pl_female2_peasant_body_bust', PEASANT, bust=True),
    ]


class Head:

    def get_name(self):
        raise NotImplementedError

    def get_id(self):
        return NotImplementedError

    def get_usage(self):
        raise NotImplementedError

    def is_japan(self):
        raise NotImplementedError

    def is_black(self):
        raise NotImplementedError

    def get_hands(self):
        raise NotImplementedError

    def hat_mandatory(self):
        raise NotImplementedError


class MaleHead(Head):

    def __init__(self, name, usage, hat=True, black=False, japan=False, alt=None, crop=False):
        self.name = name
        self.usage = usage
        self.hat = hat
        self.black = black
        self.japan = japan
        self.alt = alt
        self.crop = crop

        if self.black and self.japan:
            raise Exception(f'head {self.name} could not be black and japan at same time')

    def get_name(self):
        return self.name

    def get_id(self):
        return self.alt if self.alt else self.get_name()

    def get_usage(self):
        return self.usage

    def is_japan(self):
        return self.japan

    def is_black(self):
        return self.black

    def can_mount_hat(self):
        return self.hat is True

    def get_hands(self):
        if self.is_black():
            return MALE_BLACK_HANDS
        return MALE_WHITE_HANDS

    def hat_mandatory(self):
        return self.crop


class FemaleHead(Head):

    def __init__(self, name, usage, hat=True, bust=False, black=False, japan=False, alt=None, crop=False):
        self.name = name
        self.usage = usage
        self.hat = hat
        self.bust = bust
        self.black = black
        self.japan = japan
        self.alt = alt
        self.crop = crop

        if self.black and self.japan:
            raise Exception(f'head {self.name} could not be black and japan at same time')

    def get_name(self):
        return self.name

    def get_id(self):
        return self.alt if self.alt else self.get_name()

    def get_usage(self):
        return self.usage

    def is_japan(self):
        return self.japan

    def is_black(self):
        return self.black

    def can_mount_hat(self):
        return self.hat is True

    def get_hands(self):
        if self.is_black():
            return FEMALE_BLACK_HANDS
        return FEMALE_WHITE_HANDS

    def have_bust(self):
        return self.bust

    def hat_mandatory(self):
        return self.crop


class HeadStore:
    MALE = [
        MaleHead('syd_head', PIRATE, hat=False),
        MaleHead('li_rockford_head', GENERIC),
        MaleHead('li_scrote_head', HERO),
        MaleHead('li_captain_head', GENERIC),
        MaleHead('li_sales_head', GENERIC),
        MaleHead('li_manhattan_bartender_head', HERO),
        MaleHead('br_brighton_head', GENERIC),
        MaleHead('br_quigly_head', TRADER),
        MaleHead('br_captain_head', GENERIC),
        MaleHead('br_sales_head', GENERIC),
        MaleHead('br_bartender_head', GENERIC),
        MaleHead('br_tobias_head', HERO),
        MaleHead('rh_alaric_head', MILITARY, hat=False),
        MaleHead('rh_deidrich_head', HERO),
        MaleHead('rh_reichman_head', HERO),
        MaleHead('rh_wilham_head', MILITARY),
        MaleHead('rh_hassler_head', MILITARY),
        MaleHead('rh_captain_head', CAPTAIN),
        MaleHead('rh_sales_head', GENERIC),
        MaleHead('rh_bartender_head', GENERIC),
        MaleHead('ku_edo_head', HERO, japan=True),
        MaleHead('ku_tenji_head', HERO, japan=True),
        MaleHead('ku_captain_head', CAPTAIN, japan=True),
        MaleHead('ku_sales_head', GENERIC, japan=True),
        MaleHead('ku_bartender_head', GENERIC, japan=True),
        MaleHead('pi_pirate1_head', PIRATE),
        MaleHead('pi_pirate2_head', PIRATE),
        MaleHead('pi_pirate3_head', PIRATE),
        MaleHead('pi_pirate3_head_hurt', PIRATE),
        MaleHead('pi_pirate4_head', PIRATE),
        MaleHead('pi_pirate5_head', PLAYER),
        MaleHead('sh_male1_head', GENERIC),
        MaleHead('sh_male2_head', GENERIC),
        MaleHead('sh_male3_head', GENERIC),
        MaleHead('sh_male4_head', GENERIC),
        MaleHead('sh_male5_head', MONKEY),
        MaleHead('sh_male5t_head', MONKEY),
        MaleHead('sh_male6_head', MONKEY),
        MaleHead('ge_male1_head', GENERIC),
        MaleHead('ge_male2_head', GENERIC, japan=True),
        MaleHead('ge_male3_head', GENERIC),
        MaleHead('ge_male4_head', GENERIC),
        MaleHead('ge_male6_head', GENERIC, black=True),
        MaleHead('ge_male7_head', SCIENT),
        MaleHead('sc_scientist1_head', SCIENT, hat=False),
        MaleHead('sc_scientist2_head', SCIENT, hat=False),
        MaleHead('pl_male1_head', GENERIC),
        MaleHead('pl_male2_head', GENERIC),
        MaleHead('pl_male3_head', GENERIC, hat=False),
        MaleHead('pl_male4_head', GENERIC, black=True),
        MaleHead('pl_male5_head', GENERIC, japan=True),
        MaleHead('pl_male6_head', GENERIC, black=True),
        MaleHead('pl_male7_head', GENERIC),
        MaleHead('pl_male8_head', GENERIC, hat=False, japan=True),
        MaleHead('li_sales_head_hat', GENERIC, crop=True, alt='li_sales_head'),
        MaleHead('br_sales_head_hat', GENERIC, crop=True, alt='br_sales_head'),
        MaleHead('ku_bartender_head_hat', GENERIC, crop=True, japan=True, alt='ku_bartender_head'),
        MaleHead('ku_tenji_head_hat', HERO, crop=True, alt='ku_bartender_head'),
        MaleHead('pl_male3_head_hat', GENERIC, crop=True, alt='pl_male3_head'),
        MaleHead('pl_male8_head_hat', GENERIC, crop=True, japan=True, alt='pl_male8_head'),
        MaleHead('rh_alaric_head_hat', HERO, crop=True, alt='rh_alaric_head'),
        MaleHead('sc_scientist1_head_hat', SCIENT, crop=True, alt='sc_scientist1_head'),
        MaleHead('sc_scientist2_head_hat', SCIENT, crop=True, alt='sc_scientist2_head'),
    ]

    FEMALE = [
        FemaleHead('li_hatcher_head', HERO, hat=False),
        FemaleHead('br_darcy_head', HERO, hat=False),
        FemaleHead('br_kaitlyn_head', GENERIC, hat=False),
        FemaleHead('br_karina_head_gen', GENERIC, alt='br_karina_head'),
        FemaleHead('rh_gruenwald_head_gen', GENERIC, hat=False, alt='rh_gruenwald_head'),
        FemaleHead('ku_kym_head_gen', GENERIC, japan=True, alt='ku_kym_head'),
        FemaleHead('ku_tashi_head', GENERIC, hat=False, japan=True),
        FemaleHead('sh_female1_head_gen', PIRATE, hat=False, alt='sh_female1_head'),
        FemaleHead('sh_female2_head_gen', PIRATE, hat=False, alt='sh_female2_head'),
        FemaleHead('ge_female1_head', GENERIC),
        FemaleHead('pl_female1_head', GENERIC, hat=False),
        FemaleHead('pl_female2_head', GENERIC),
        FemaleHead('pl_female3_head', GENERIC, black=True),
        FemaleHead('pl_female4_head', HERO),
        FemaleHead('pl_female5_head', GENERIC),
        FemaleHead('pl_female6_head', GENERIC),
        FemaleHead('br_newscaster_head_gen', GENERIC, alt='br_newscaster_head'),
        FemaleHead('ku_newscaster_head_gen', GENERIC, japan=True, alt='ku_newscaster_head'),
        FemaleHead('li_newscaster_head_gen', GENERIC, black=True, alt='li_newscaster_head'),
        FemaleHead('rh_newscaster_head_gen', GENERIC, alt='rh_newscaster_head'),
        FemaleHead('br_newscaster_head', GENERIC, bust=True),
        FemaleHead('ku_newscaster_head', GENERIC, bust=True, japan=True),
        FemaleHead('li_newscaster_head', GENERIC, hat=False, bust=True, black=True),
        FemaleHead('rh_newscaster_head', GENERIC, hat=False, bust=True),
        FemaleHead('sh_female2_head', PIRATE, bust=True),
        FemaleHead('sh_female1_head', PIRATE, bust=True),
        FemaleHead('sh_female5_head', MONKEY),
        FemaleHead('sh_female6_head', MONKEY),
        FemaleHead('br_karina_head', GENERIC, bust=True),
        FemaleHead('rh_gruenwald_head', GENERIC, bust=True),
        FemaleHead('ku_kym_head', GENERIC, bust=True, japan=True),
        FemaleHead('br_newscaster_head_hat', GENERIC, crop=True, bust=True, alt='br_newscaster_head'),
        FemaleHead('br_newscaster_head_gen_hat', GENERIC, crop=True, alt='br_newscaster_head'),
        FemaleHead('li_newscaster_head_hat', GENERIC, crop=True, bust=True, black=True, alt='li_newscaster_head'),
        FemaleHead('li_newscaster_head_gen_hat', GENERIC, crop=True, black=True, alt='li_newscaster_head'),
        FemaleHead('rh_newscaster_head_hat', GENERIC, crop=True, bust=True, alt='rh_newscaster_head'),
        FemaleHead('rh_newscaster_head_gen_hat', GENERIC, crop=True, alt='rh_newscaster_head'),
        FemaleHead('pl_female4_head_helmet', HERO, crop=True, alt='pl_female4_head'),
    ]

    def __init__(self):
        self.male_per_type = load_items_by_usage(self.MALE)
        self.female_per_type = load_items_by_usage(self.FEMALE)
        self.extracted = []

    def get_result(self, head):
        self.extracted.append(head.get_id())
        return head

    def get_male(self, types: list[int] = None, allow_hat: bool | None = None,
                 allow_black=True, allow_japan=True, japan_first=False, allow_crop=True,
                 safe=False):
        if not types:
            raise Exception('type is not set')

        if japan_first:
            for usage in types:
                shuffle(self.male_per_type[usage])
                for item in self.male_per_type[usage]:
                    if not item.is_japan():
                        continue
                    if item.hat_mandatory() and allow_crop is False:
                        continue
                    if not item.can_mount_hat() and allow_hat is False:
                        continue
                    if item.get_name() in self.extracted:
                        continue

                    return self.get_result(item)

        for usage in types:
            shuffle(self.male_per_type[usage])
            for item in self.male_per_type[usage]:
                if item.is_black() and not allow_black:
                    continue
                if item.is_japan() and not allow_japan:
                    continue
                if item.hat_mandatory() and allow_crop is False:
                    continue
                if not item.can_mount_hat() and allow_hat is False:
                    continue
                if item.get_name() in self.extracted:
                    continue

                return self.get_result(item)

        if not safe:
            raise Exception('no left male heads')

    def get_female(self, types: list[int], allow_bust=True, allow_hat: bool | None = None,
                   allow_black=True, allow_japan=True, japan_first=False, allow_crop=True,
                   safe=False):
        if japan_first:
            for usage in types:
                shuffle(self.female_per_type[usage])
                for item in self.female_per_type[usage]:
                    if not item.is_japan():
                        continue
                    if item.hat_mandatory() and allow_crop is False:
                        continue
                    if not item.can_mount_hat() and allow_hat is False:
                        continue
                    if not allow_bust and item.have_bust():
                        continue
                    if item.get_id() in self.extracted:
                        continue

                    return self.get_result(item)

        for usage in types:
            shuffle(self.female_per_type[usage])
            for item in self.female_per_type[usage]:
                if item.is_black() and not allow_black:
                    continue
                if item.is_japan() and not allow_japan:
                    continue
                if item.hat_mandatory() and allow_crop is False:
                    continue
                if not item.can_mount_hat() and allow_hat is False:
                    continue
                if not allow_bust and item.have_bust():
                    continue
                if item.get_id() in self.extracted:
                    continue

                return self.get_result(item)

        if not safe:
            raise Exception('no left female heads')


class Costume:
    def __init__(self, body, head, is_male=True, accessory=None):
        self.body = body
        self.head = head
        self.left_hand, self.right_hand = head.get_hands()
        self.is_male = is_male
        self.accessory = accessory

    def get_body(self):
        return self.body.get_name()

    def get_head(self):
        return self.head.get_name()

    def get_left_hand(self):
        return self.left_hand

    def get_right_hand(self):
        return self.right_hand

    def get_accessory(self):
        return self.accessory

    def dump(self):
        print(f'body: {self.body.get_name()}')
        print(f'head: {self.head.get_name()}')
        print(f'left_hand: {self.left_hand}')
        print(f'right_hand: {self.left_hand}')
        print(f'accessory: {self.accessory}')


class CharacterFactory:

    def __init__(self):
        self.rh_body = RheinlandBodyStore()
        self.li_body = LibertyBodyStore()
        self.br_body = BretoniaBodyStore()
        self.ku_body = KusariBodyStore()
        self.ge_body = GenericBodyStore()
        self.heads = HeadStore()

    def get_store_by_faction(self, faction):
        if faction == RHEINLAND:
            return self.rh_body
        if faction == LIBERTY:
            return self.li_body
        if faction == BRETONIA:
            return self.br_body
        if faction == KUSARI:
            return self.ku_body
        raise Exception('unknown faction for body')

    def get_kwargs_by_faction(self, faction):
        if faction == RHEINLAND:
            return {'allow_black': False, 'allow_japan': False}
        if faction == LIBERTY:
            return {'allow_black': True, 'allow_japan': False}
        if faction == BRETONIA:
            return {'allow_black': False, 'allow_japan': False}
        if faction == KUSARI:
            return {'allow_black': False, 'allow_japan': True, 'japan_first': True}
        if faction == BORDER_WORLD:
            return {'allow_black': True, 'allow_japan': True}
        raise Exception('unknown faction for body')

    def get_bartender(self, faction):
        body_store = self.get_store_by_faction(faction)
        head = self.heads.get_male(types=[GENERIC], allow_crop=False, **self.get_kwargs_by_faction(faction))
        body = body_store.get_male(BARTENDER)
        return Costume(head=head, body=body, is_male=True)

    def get_male_military(self, faction):
        body_store = self.get_store_by_faction(faction)
        head = self.heads.get_male(types=[GENERIC], **self.get_kwargs_by_faction(faction))
        body = body_store.get_male(ELITE, GUARD)
        hat = body_store.get_male_hat(MILITARY, hat_mandatory=head.hat_mandatory())
        return Costume(head=head, body=body, is_male=True, accessory=hat)

    def get_male_journeyman(self, faction):
        head = self.heads.get_male(types=[GENERIC], allow_crop=False, **self.get_kwargs_by_faction(faction))
        body = self.ge_body.get_male(JOURNEYMAN)
        shades = get_male_shades()
        return Costume(head=head, body=body, is_male=True, accessory=shades)

    def get_male_peasant(self, faction):
        head = self.heads.get_male(types=[GENERIC], allow_crop=False, **self.get_kwargs_by_faction(faction))
        body = self.ge_body.get_male(PEASANT)
        nn = get_peasant_nn()
        return Costume(head=head, body=body, is_male=True, accessory=nn)

    def get_male_trader(self, faction):
        body_store = self.get_store_by_faction(faction)
        head = self.heads.get_male(types=[GENERIC], allow_crop=False, **self.get_kwargs_by_faction(faction))
        body = body_store.get_male(TRADER)
        nn = get_trader_nn()
        return Costume(head=head, body=body, is_male=True, accessory=nn)

    def get_male_pirate(self, faction):
        head = self.heads.get_male(types=[PIRATE, GENERIC], allow_crop=False, **self.get_kwargs_by_faction(faction))
        body = self.ge_body.get_male(PIRATE)
        return Costume(head=head, body=body, is_male=True, accessory=None)

    def get_female_military(self, faction):
        body_store = self.get_store_by_faction(faction)
        head = self.heads.get_female(types=[GENERIC], allow_bust=False, **self.get_kwargs_by_faction(faction))
        body = body_store.get_female(ELITE, GUARD, bust=False)
        hat = body_store.get_female_hat(MILITARY, hat_mandatory=head.hat_mandatory())
        return Costume(head=head, body=body, is_male=False, accessory=hat)

    def get_female_journeyman(self, faction):
        head = self.heads.get_female(types=[GENERIC], allow_bust=False, allow_crop=False,
                                     **self.get_kwargs_by_faction(faction))
        body = self.ge_body.get_female(JOURNEYMAN, bust=head.have_bust())
        shades = get_female_shades()
        return Costume(head=head, body=body, is_male=False, accessory=shades)

    def get_female_peasant(self, faction):
        head = self.heads.get_female(types=[GENERIC], allow_bust=True, allow_crop=False,
                                     **self.get_kwargs_by_faction(faction))
        body = self.ge_body.get_female(PEASANT, bust=head.have_bust())
        nn = get_peasant_nn()
        return Costume(head=head, body=body, is_male=False, accessory=nn)

    def get_female_trader(self, faction):
        body_store = self.get_store_by_faction(faction)
        head = self.heads.get_female(types=[GENERIC], allow_crop=False, **self.get_kwargs_by_faction(faction))
        body = body_store.get_female(TRADER)
        nn = get_trader_nn()
        return Costume(head=head, body=body, is_male=False, accessory=nn)

    def get_female_pirate(self, faction):
        head = self.heads.get_female(types=[PIRATE, GENERIC], allow_bust=False,
                                     allow_crop=False, **self.get_kwargs_by_faction(faction))
        body = self.ge_body.get_female(PIRATE, JOURNEYMAN, bust=head.have_bust())
        return Costume(head=head, body=body, is_male=False, accessory=None)

    def get_military(self, faction):
        if randint(0, 2) == 1:
            return self.get_female_military(faction)
        return self.get_male_military(faction)

    def get_journeyman(self, faction):
        if randint(0, 2) == 1:
            return self.get_female_journeyman(faction)
        return self.get_male_journeyman(faction)

    def get_peasant(self, faction):
        if randint(0, 2) == 1:
            return self.get_female_peasant(faction)
        return self.get_male_peasant(faction)

    def get_trader(self, faction):
        if randint(0, 3) == 1:
            return self.get_female_trader(faction)
        return self.get_male_trader(faction)

    def get_pirate(self, faction):
        if randint(0, 3) == 1:
            return self.get_female_pirate(faction)
        return self.get_male_pirate(faction)
