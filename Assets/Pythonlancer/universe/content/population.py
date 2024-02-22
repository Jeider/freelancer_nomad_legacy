from text.dividers import SINGLE_DIVIDER


class Population(object):
    SIMPLE_DEFENCE_PARAMS = '''sort = 9
toughness = 10
density = 2
repop_time = 12
max_battle_size = 3
relief_time = 20'''

    MEDIUM_DEFENCE_PARAMS = '''sort = 9
toughness = 10
density = 6
repop_time = 6
max_battle_size = 8
pop_type = rh_grp, base_cluster_law
relief_time = 10
density_restriction = 1, unlawfuls'''

    HIGH_DEFENCE_PARAMS = '''sort = 9
toughness = 10
density = 6
repop_time = 6
max_battle_size = 8
pop_type = rh_grp, base_cluster_law
relief_time = 10
density_restriction = 1, unlawfuls'''

    TRADELANE_PARAMS = '''lane_id = 26
tradelane_down = 10
sort = 6
toughness = 1
density = 6
repop_time = 15
max_battle_size = 4
pop_type = major_tradelane
relief_time = 15'''

    SIMPLE_DEFENCE_ENCOUNTERS = None
    MEDIUM_DEFENCE_ENCOUNTERS = None
    HIGH_DEFENCE_ENCOUNTERS = None
    SIMPLE_ARRIVAL_TRADERS_ENCOUNTERS = None
    TRADELANE_ARRIVAL_TRADERS_ENCOUNTERS = None

    @classmethod
    def get_simple_defence_params(cls):
        if not cls.SIMPLE_DEFENCE_PARAMS:
            raise Exception('simple defence encounters is not defined %s' % cls.__class__.__name__)
        if not cls.SIMPLE_ARRIVAL_TRADERS_ENCOUNTERS:
            raise Exception('simple arrived traders encounters is not defined %s' % cls.__class__.__name__)
        return SINGLE_DIVIDER.join([
            cls.SIMPLE_DEFENCE_PARAMS,
            cls.SIMPLE_DEFENCE_ENCOUNTERS,
            cls.SIMPLE_ARRIVAL_TRADERS_ENCOUNTERS,
        ])

    @classmethod
    def get_medium_defence_params(cls):
        if not cls.MEDIUM_DEFENCE_PARAMS:
            raise Exception('medium defence encounters is not defined %s' % cls.__class__.__name__)
        if not cls.SIMPLE_ARRIVAL_TRADERS_ENCOUNTERS:
            raise Exception('simple arrived traders encounters is not defined %s' % cls.__class__.__name__)
        return SINGLE_DIVIDER.join([
            cls.MEDIUM_DEFENCE_PARAMS,
            cls.MEDIUM_DEFENCE_ENCOUNTERS,
            cls.SIMPLE_ARRIVAL_TRADERS_ENCOUNTERS,
        ])

    @classmethod
    def get_high_defence_params(cls):
        if not cls.HIGH_DEFENCE_ENCOUNTERS:
            raise Exception('high defence encounters is not defined %s' % cls.__class__.__name__)
        if not cls.SIMPLE_ARRIVAL_TRADERS_ENCOUNTERS:
            raise Exception('simple arrived traders encounters is not defined %s' % cls.__class__.__name__)
        return SINGLE_DIVIDER.join([
            cls.HIGH_DEFENCE_PARAMS,
            cls.HIGH_DEFENCE_ENCOUNTERS,
            cls.SIMPLE_ARRIVAL_TRADERS_ENCOUNTERS,
        ])

    @classmethod
    def get_tradelane_arriaval_traders_params(cls):
        if not cls.TRADELANE_ARRIVAL_TRADERS_ENCOUNTERS:
            raise Exception('tradelane encounters is not defined %s' % cls.__class__.__name__)
        return SINGLE_DIVIDER.join([
            cls.TRADELANE_PARAMS,
            cls.TRADELANE_ARRIVAL_TRADERS_ENCOUNTERS,
        ])


class RheinlandLegalPopulation(Population):
    SIMPLE_DEFENCE_ENCOUNTERS = '''
encounter = rh_grp_main_defend, 5, 1.00000
faction = rh_grp, 1.00000'''

    HIGH_DEFENCE_ENCOUNTERS = '''
encounter = rh_grp_main_defend, 5, 0.80000
faction = rh_grp, 1.00000
encounter = rh_grp_main_cruiser, 5, 0.20000
faction = rh_grp, 1.00000'''

    MEDIUM_DEFENCE_ENCOUNTERS = '''
encounter = rh_grp_main_defend, 5, 0.80000
faction = rh_grp, 1.00000
encounter = rh_grp_main_gunboat, 5, 0.20000
faction = rh_grp, 1.00000'''

    SIMPLE_ARRIVAL_TRADERS_ENCOUNTERS = '''
encounter = tr_grp_rh_transport, 5, 0.5
faction = tr_grp, 1.00000
encounter = rh_grp_main_trade, 5, 0.7
faction = rh_grp, 0.50000
faction = rc_grp, 0.50000
encounter = bh_grp_rh_trade, 5, 0.5
faction = bh_grp, 1.00000'''

    TRADELANE_ARRIVAL_TRADERS_ENCOUNTERS = '''
encounter = tr_grp_rh_transport_tlr, 5, 0.5
faction = tr_grp, 1.00000
encounter = rh_grp_main_trade_tlr, 5, 0.7
faction = rh_grp, 0.50000
faction = rc_grp, 0.50000
encounter = bh_grp_rh_trade_tlr, 5, 0.5
faction = bh_grp, 1.00000'''
