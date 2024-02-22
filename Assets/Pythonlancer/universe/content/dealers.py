from text.dividers import SINGLE_DIVIDER


MALE_LEFT_HAND = 'lefthand = benchmark_male_hand_left'
MALE_RIGHT_HAND = 'righthand = benchmark_male_hand_right'


class DealerPack(object):
    HEADER = '[GF_NPC]'
    NICKNAME_TEMPLATE = 'nickname = {}'
    EQUIP = None
    TRADER = None
    SHIPDEALER = None

    @classmethod
    def get_dealer(cls, nickname, costume):
        return SINGLE_DIVIDER.join([
            cls.HEADER,
            cls.NICKNAME_TEMPLATE.format(nickname),
            *costume,
            MALE_LEFT_HAND,
            MALE_RIGHT_HAND
        ])

    @classmethod
    def get_equip(cls, nickname):
        return cls.get_dealer(nickname, cls.EQUIP)

    @classmethod
    def get_trader(cls, nickname):
        return cls.get_dealer(nickname, cls.TRADER)

    @classmethod
    def get_shipdealer(cls, nickname):
        return cls.get_dealer(nickname, cls.SHIPDEALER)


class GenericCivilianDealers(DealerPack):
    EQUIP = [
        'body = pl_male1_peasant_body',
        'head = ge_male1_head',
        'accessory = prop_neuralnet_a',
    ]

    TRADER = [
        'head = ge_male3_head',
        'body = pl_male3_peasant_body',
        'accessory = prop_neuralnet_f',
    ]

    SHIPDEALER = [
        'body = pl_male2_peasant_body',
        'head = pl_male7_head',
        'accessory = prop_neuralnet_c',
    ]


class GenericCorsairDealers(DealerPack):
    EQUIP = [
        'body = pl_male1_journeyman_body',
        'head = pi_pirate1_head',
        'accessory = prop_neuralnet_a',
    ]

    TRADER = [
        'body = pl_male3_journeyman_body',
        'head = pi_pirate2_head',
        'accessory = prop_neuralnet_f',
    ]

    SHIPDEALER = [
        'body = sh_male1_body',
        'head = pi_pirate3_head',
        'accessory = prop_neuralnet_c',
    ]


class RheinlandPlanetDealers(DealerPack):
    EQUIP = [
        'body = rh_shipdealer_body',
        'head = rh_captain_head',
        'accessory = prop_neuralnet_d',
    ]

    TRADER = [
        'body = rh_commtrader_body',
        'head = rh_sales_head',
        'accessory = prop_neuralnet_e',
    ]

    SHIPDEALER = [
        'body = rh_shipdealer_body',
        'head = rh_wilham_head',
        'accessory = prop_neuralnet_b',
    ]


class RheinlandMilitaryDealers(DealerPack):
    EQUIP = [
        'body = rh_male_guard_body',
        'head = rh_captain_head',
        'accessory = prop_hat_male_rh_grd',
        'accessory = prop_neuralnet_d',
    ]

    TRADER = [
        'body = rh_male_guard_body',
        'head = rh_sales_head',
        'accessory = prop_hat_male_rh_grd',
        'accessory = prop_neuralnet_e',
    ]

    SHIPDEALER = [
        'body = rh_male_elite_body',
        'head = rh_wilham_head',
        'accessory = prop_hat_male_rh_elite',
    ]


class RheinlandCivilianDealers(DealerPack):
    EQUIP = [
        'body = rh_shipdealer_body',
        'head = rh_captain_head',
        'accessory = prop_neuralnet_d',
    ]

    TRADER = [
        'body = rh_commtrader_body',
        'head = rh_sales_head',
        'accessory = prop_neuralnet_e',
    ]

    SHIPDEALER = [
        'body = rh_shipdealer_body',
        'head = rh_wilham_head',
        'accessory = prop_neuralnet_b',
    ]


class RheinlandPirateDealers(DealerPack):
    EQUIP = [
        'body = pi_pirate6_body',
        'head = rh_hassler_head',
        'accessory = prop_neuralnet_a',
    ]

    TRADER = [
        'body = pi_pirate2_body',
        'head = rh_wilham_head',
        'accessory = prop_neuralnet_f',
    ]

    SHIPDEALER = [
        'body = pi_pirate2_body',
        'head = rh_sales_head',
    ]


class LibertyPlanetDealers(DealerPack):
    EQUIP = [
        'body = li_shipdealer_body',
        'head = li_captain_head',
        'accessory = prop_neuralnet_d',
    ]

    TRADER = [
        'body = li_commtrader_body',
        'head = li_sales_head',
        'accessory = prop_neuralnet_e',
    ]

    SHIPDEALER = [
        'body = li_shipdealer_body',
        'head = li_rockford_head',
        'accessory = prop_neuralnet_b',
    ]


class LibertyMilitaryDealers(DealerPack):
    EQUIP = [
        'body = li_male_elite_body',
        'head = li_captain_head',
        'accessory = prop_hat_male_li_elite',
    ]

    TRADER = [
        'body = li_male_guard_body',
        'head = li_sales_head',
        'accessory = prop_hat_male_li_grd',
        'accessory = prop_neuralnet_e',
    ]

    SHIPDEALER = [
        'body = li_male_elite_body',
        'head = li_rockford_head',
        'accessory = prop_hat_male_li_elite_visor',
    ]


class LibertyCivilianDealers(DealerPack):
    EQUIP = [
        'body = li_shipdealer_body',
        'head = li_captain_head',
        'accessory = prop_neuralnet_d',
    ]

    TRADER = [
        'body = li_commtrader_body',
        'head = li_sales_head',
        'accessory = prop_neuralnet_e',
    ]

    SHIPDEALER = [
        'body = li_shipdealer_body',
        'head = li_rockford_head',
        'accessory = prop_neuralnet_b',
    ]


class LibertyPirateDealers(DealerPack):
    EQUIP = [
        'body = pi_pirate3_body',
        'head = li_rockford_head',
        'accessory = prop_neuralnet_d',
    ]

    TRADER = [
        'body = pi_pirate5_body',
        'head = li_scrote_head',
        'accessory = prop_neuralnet_e',
    ]

    SHIPDEALER = [
        'body = pi_pirate5_body',
        'head = li_sales_head',
    ]


class BretoniaPlanetDealers(DealerPack):
    EQUIP = [
        'body = br_shipdealer_body',
        'head = br_captain_head',
        'accessory = prop_neuralnet_d',
    ]

    TRADER = [
        'body = br_commtrader_body',
        'head = br_sales_head',
        'accessory = prop_neuralnet_e',
    ]

    SHIPDEALER = [
        'body = br_shipdealer_body',
        'head = br_brighton_head',
        'accessory = prop_neuralnet_b',
    ]


class BretoniaMilitaryDealers(DealerPack):
    EQUIP = [
        'body = br_male_elite_body',
        'head = br_captain_head',
        'accessory = prop_hat_male_br_elite',
    ]

    TRADER = [
        'body = br_male_guard_body',
        'head = br_sales_head_hat',
        'accessory = prop_hat_male_br_grd',
    ]

    SHIPDEALER = [
        'body = br_male_elite_body',
        'head = br_brighton_head',
        'accessory = prop_hat_male_br_elite_visor',
    ]


class BretoniaCivilianDealers(DealerPack):
    EQUIP = [
        'body = br_shipdealer_body',
        'head = br_captain_head',
        'accessory = prop_neuralnet_d',
    ]

    TRADER = [
        'body = br_commtrader_body',
        'head = br_sales_head',
        'accessory = prop_neuralnet_e',
    ]

    SHIPDEALER = [
        'body = br_shipdealer_body',
        'head = br_brighton_head',
        'accessory = prop_neuralnet_b',
    ]


class BretoniaPirateDealers(DealerPack):
    EQUIP = [
        'body = pi_pirate1_body',
        'head = br_brighton_head',
        'accessory = prop_neuralnet_d',
    ]

    TRADER = [
        'body = pi_pirate7_body',
        'head = br_quigly_head',
        'accessory = prop_neuralnet_f',
    ]

    SHIPDEALER = [
        'body = pi_pirate7_body',
        'head = br_sales_head',
    ]


class KusariPlanetDealers(DealerPack):
    EQUIP = [
        'body = ku_shipdealer_body',
        'head = ku_captain_head',
        'accessory = prop_neuralnet_d',
    ]

    TRADER = [
        'body = ku_commtrader_body',
        'head = ku_sales_head',
        'accessory = prop_neuralnet_e',
    ]

    SHIPDEALER = [
        'body = ku_shipdealer_body',
        'head = ku_bartender_head',
        'accessory = prop_neuralnet_b',
    ]


class KusariMilitaryDealers(DealerPack):
    EQUIP = [
        'body = ku_male_elite_body',
        'head = ku_captain_head',
        'accessory = prop_hat_male_ku_elite',
    ]

    TRADER = [
        'body = ku_male_guard_body',
        'head = ku_sales_head',
        'accessory = prop_hat_male_ku_grd',
    ]

    SHIPDEALER = [
        'body = ku_male_elite_body',
        'head = ku_bartender_head_hat',
        'accessory = prop_hat_male_ku_elite_visor',
    ]


class KusariCivilianDealers(DealerPack):
    EQUIP = [
        'body = ku_shipdealer_body',
        'head = ku_captain_head',
        'accessory = prop_neuralnet_d',
    ]

    TRADER = [
        'body = ku_commtrader_body',
        'head = ku_sales_head',
        'accessory = prop_neuralnet_e',
    ]

    SHIPDEALER = [
        'body = ku_shipdealer_body',
        'head = ku_bartender_head',
        'accessory = prop_neuralnet_b',
    ]


class KusariPirateDealers(DealerPack):
    EQUIP = [
        'body = pi_pirate4_body',
        'head = ku_tenji_head',
        'accessory = prop_neuralnet_d',
    ]

    TRADER = [
        'body = pi_pirate8_body',
        'head = ku_captain_head',
        'accessory = prop_neuralnet_f',
    ]

    SHIPDEALER = [
        'body = pi_pirate8_body',
        'head = ku_sales_head',
    ]
