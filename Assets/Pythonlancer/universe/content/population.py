from universe.content import encounter
from universe.content import faction

from text.dividers import DIVIDER, SINGLE_DIVIDER

POP_FIRST = 'first'
POP_SECOND = 'second'
POP_MIXED = 'mixed'


class Population(object):

    GENERIC_PIRATES = faction.PI_GRP
    BOUNTY_HUNTERS = faction.BH_GRP
    GLOBAL_TRADERS = faction.TR_GRP
    JUNKERS = faction.JUNK_GRP

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
    GENERAL_DEFENCE_ENCOUNTERS = None
    MEDIUM_DEFENCE_ENCOUNTERS = None
    HIGH_DEFENCE_ENCOUNTERS = None
    SIMPLE_ARRIVAL_TRADERS_ENCOUNTERS = None
    TRADELANE_ARRIVAL_TRADERS_ENCOUNTERS = None

    @classmethod
    def get_encounter_definitions(cls):
        return []

    @classmethod
    def get_simple_defence_params(cls):
        if not cls.SIMPLE_DEFENCE_ENCOUNTERS:
            import pdb;pdb.set_trace()
            raise Exception('simple defence encounters is not defined %s' % cls.__class__.__name__)
        if not cls.SIMPLE_ARRIVAL_TRADERS_ENCOUNTERS:
            raise Exception('simple arrived traders encounters is not defined %s' % cls.__class__.__name__)
        return SINGLE_DIVIDER.join([
            cls.SIMPLE_DEFENCE_PARAMS,
            cls.SIMPLE_DEFENCE_ENCOUNTERS.format(**cls.get_main_defence_template_params()),
            cls.SIMPLE_ARRIVAL_TRADERS_ENCOUNTERS.format(**cls.get_trade_template_params()),
        ])

    @classmethod
    def get_medium_defence_params(cls):
        if not cls.GENERAL_DEFENCE_ENCOUNTERS:
            raise Exception('general defence encounters is not defined %s' % cls.__class__.__name__)
        if not cls.SIMPLE_ARRIVAL_TRADERS_ENCOUNTERS:
            raise Exception('simple arrived traders encounters is not defined %s' % cls.__class__.__name__)
        return SINGLE_DIVIDER.join([
            cls.MEDIUM_DEFENCE_PARAMS,
            cls.GENERAL_DEFENCE_ENCOUNTERS.format(**cls.get_main_defence_template_params()),
            cls.MEDIUM_DEFENCE_ENCOUNTERS.format(**cls.get_medium_defence_template_params()),
            cls.SIMPLE_ARRIVAL_TRADERS_ENCOUNTERS.format(**cls.get_trade_template_params()),
        ])

    @classmethod
    def get_high_defence_params(cls):
        if not cls.HIGH_DEFENCE_ENCOUNTERS:
            raise Exception('general defence encounters is not defined %s' % cls.__class__.__name__)
        if not cls.SIMPLE_ARRIVAL_TRADERS_ENCOUNTERS:
            raise Exception('simple arrived traders encounters is not defined %s' % cls.__class__.__name__)
        return SINGLE_DIVIDER.join([
            cls.HIGH_DEFENCE_PARAMS,
            cls.GENERAL_DEFENCE_ENCOUNTERS.format(**cls.get_main_defence_template_params()),
            cls.HIGH_DEFENCE_ENCOUNTERS.format(**cls.get_high_defence_template_params()),
            cls.SIMPLE_ARRIVAL_TRADERS_ENCOUNTERS.format(**cls.get_trade_template_params()),
        ])

    @classmethod
    def get_tradelane_arriaval_traders_params(cls):
        if not cls.TRADELANE_ARRIVAL_TRADERS_ENCOUNTERS:
            raise Exception('tradelane encounters is not defined %s' % cls.__class__.__name__)
        return SINGLE_DIVIDER.join([
            cls.TRADELANE_PARAMS,
            cls.TRADELANE_ARRIVAL_TRADERS_ENCOUNTERS.format(**cls.get_trade_template_params()),
        ])

    @classmethod
    def get_trade_template_params(cls):
        return {}

    @classmethod
    def get_main_defence_template_params(cls):
        return {}

    @classmethod
    def get_high_defence_template_params(cls):
        return {}

    @classmethod
    def get_medium_defence_template_params(cls):
        return {}


class LawfulPopulation(Population):
    MAIN_FACTION = None
    MAIN_TRADERS = None

    MAIN_ENCOUNTERS = [
        encounter.MainDefend,
        encounter.MainPatrol,
        encounter.MainScout,
        encounter.MainTrade,
        encounter.MainTradeTLR,
        encounter.AresXScout,
    ]
    POLICE_PATROL = encounter.PatrolPolice

    HIGH_CAPSHIP_ENC = None
    MEDIUM_CAPSHIP_ENC = None

    BH_PATROL_ENC = None

    GLOBAL_TRADERS_ENC = None
    GLOBAL_TRADERS_TLR_ENC = None
    BH_TRADE_ENC = None
    BH_TRADE_TLR_ENC = None

    SIMPLE_DEFENCE_ENCOUNTERS = '''
encounter = main_defend, 5, 1.00000
faction = {main_faction}, 1.00000'''

    GENERAL_DEFENCE_ENCOUNTERS = '''
encounter = main_defend, 5, 0.80000
faction = {main_faction}, 1.00000'''

    HIGH_DEFENCE_ENCOUNTERS = '''
encounter = {high_defence_capship_encounter}, 5, 0.20000
faction = {main_faction}, 1.00000'''

    MEDIUM_DEFENCE_ENCOUNTERS = '''
encounter = {medium_defence_capship_encounter}, 5, 0.20000
faction = {main_faction}, 1.00000'''

    SIMPLE_ARRIVAL_TRADERS_ENCOUNTERS = '''
encounter = {global_traders_encounter}, 5, 0.5
faction = {global_traders}, 1.00000
encounter = main_trade, 5, 0.7
faction = {main_faction}, 0.50000
faction = {main_traders}, 0.50000
encounter = {bounter_hunter_trade_encounter}, 5, 0.5
faction = {bounty_hunters}, 1.00000'''

    TRADELANE_ARRIVAL_TRADERS_ENCOUNTERS = '''
encounter = {global_traders_encounter_tlr}, 5, 0.5
faction = {global_traders}, 1.00000
encounter = main_trade_tlr, 5, 0.7
faction = {main_faction}, 0.50000
faction = {main_traders}, 0.50000
encounter = {bounter_hunter_trade_encounter_tlr}, 5, 0.5
faction = {bounty_hunters}, 1.00000'''

    @classmethod
    def get_police_encounter(cls):
        return cls.POLICE_PATROL.get_nickname()

    @classmethod
    def get_police_faction(cls):
        if not cls.MAIN_FACTION:
            raise Exception('Population %s have no main faction' % cls.__class__.__name__)
        return cls.MAIN_FACTION

    @classmethod
    def get_bounty_hunter_encounter(cls):
        if not cls.BH_PATROL_ENC:
            raise Exception('Population %s have no BH patrol' % cls.__class__.__name__)
        return cls.BH_PATROL_ENC.get_nickname()

    @classmethod
    def get_bounty_hunter_faction(cls):
        return cls.BOUNTY_HUNTERS

    @classmethod
    def get_trade_template_params(cls):
        return {
            'main_faction': cls.MAIN_FACTION,
            'main_traders': cls.MAIN_TRADERS,
            'global_traders': cls.GLOBAL_TRADERS,
            'bounty_hunters': cls.BOUNTY_HUNTERS,
            'global_traders_encounter': cls.GLOBAL_TRADERS_ENC.get_nickname(),
            'global_traders_encounter_tlr': cls.GLOBAL_TRADERS_TLR_ENC.get_nickname(),
            'bounter_hunter_trade_encounter': cls.BH_TRADE_ENC.get_nickname(),
            'bounter_hunter_trade_encounter_tlr': cls.BH_TRADE_TLR_ENC.get_nickname(),
        }

    @classmethod
    def get_main_defence_template_params(cls):
        return {
            'main_faction': cls.MAIN_FACTION,
        }

    @classmethod
    def get_high_defence_template_params(cls):
        return {
            'high_defence_capship_encounter': cls.HIGH_CAPSHIP_ENC.get_nickname(),
            'main_faction': cls.MAIN_FACTION,
        }

    @classmethod
    def get_medium_defence_template_params(cls):
        return {
            'medium_defence_capship_encounter': cls.MEDIUM_CAPSHIP_ENC.get_nickname(),
            'main_faction': cls.MAIN_FACTION,
        }

    @classmethod
    def get_lawful_factions(cls):
        return [
            cls.MAIN_FACTION,
            cls.MAIN_TRADERS,
            cls.BOUNTY_HUNTERS,
            cls.GLOBAL_TRADERS,
        ]

    @classmethod
    def get_encounter_definitions(cls):
        extra_encounters = [
            cls.HIGH_CAPSHIP_ENC,
            cls.MEDIUM_CAPSHIP_ENC,
            cls.BH_PATROL_ENC,
            cls.GLOBAL_TRADERS_ENC,
            cls.GLOBAL_TRADERS_TLR_ENC,
            cls.BH_TRADE_ENC,
            cls.BH_TRADE_TLR_ENC,
        ]
        return cls.MAIN_ENCOUNTERS + [
            cls.POLICE_PATROL,
        ] + [enc for enc in extra_encounters if enc is not None]


class UnlawfulPopulation(Population):
    MAIN_PIRATES = None
    ATTACK_TLR_PATROL = encounter.PatrolTLR

    @classmethod
    def get_tlr_attackers_encounter(cls):
        return cls.ATTACK_TLR_PATROL.get_nickname()

    @classmethod
    def get_tlr_attackers_faction(cls):
        if not cls.MAIN_PIRATES:
            raise Exception('Population %s have no main pirates' % cls.__class__.__name__)
        return cls.MAIN_PIRATES

    @classmethod
    def get_unlawful_factions(cls):
        return [
            cls.MAIN_PIRATES,
            cls.GENERIC_PIRATES,
            cls.JUNKERS,
        ]

    @classmethod
    def get_encounter_definitions(cls):
        return [cls.ATTACK_TLR_PATROL]


class RheinlandLegalPopulation(LawfulPopulation):
    MAIN_FACTION = faction.RH_GRP
    MAIN_TRADERS = faction.RC_GRP

    HIGH_CAPSHIP_ENC = encounter.RhCruiser
    MEDIUM_CAPSHIP_ENC = encounter.RhGunboat

    BH_PATROL_ENC = encounter.BhPatrolRh

    GLOBAL_TRADERS_ENC = encounter.RhTransport
    GLOBAL_TRADERS_TLR_ENC = encounter.RhTransportTLR
    BH_TRADE_ENC = encounter.BhTradeRh
    BH_TRADE_TLR_ENC = encounter.BhTradeRhTLR


class LibertyLegalPopulation(LawfulPopulation):
    MAIN_FACTION = faction.LI_GRP
    MAIN_TRADERS = faction.LC_GRP

    HIGH_CAPSHIP_ENC = encounter.LiCruiser
    MEDIUM_CAPSHIP_ENC = encounter.LiCruiser

    BH_PATROL_ENC = encounter.BhPatrolLi

    GLOBAL_TRADERS_ENC = encounter.LiTransport
    GLOBAL_TRADERS_TLR_ENC = encounter.LiTransportTLR
    BH_TRADE_ENC = encounter.BhTradeLi
    BH_TRADE_TLR_ENC = encounter.BhTradeLiTLR


class BretoniaLegalPopulation(LawfulPopulation):
    MAIN_FACTION = faction.BR_GRP
    MAIN_TRADERS = faction.BC_GRP

    HIGH_CAPSHIP_ENC = encounter.BrDestroyer
    MEDIUM_CAPSHIP_ENC = encounter.BrGunboat

    BH_PATROL_ENC = encounter.BhPatrolBr

    GLOBAL_TRADERS_ENC = encounter.BrTransport
    GLOBAL_TRADERS_TLR_ENC = encounter.BrTransportTLR
    BH_TRADE_ENC = encounter.BhTradeBr
    BH_TRADE_TLR_ENC = encounter.BhTradeBrTLR


class KusariLegalPopulation(LawfulPopulation):
    MAIN_FACTION = faction.KU_GRP
    MAIN_TRADERS = faction.KC_GRP

    HIGH_CAPSHIP_ENC = encounter.KuDestroyer
    MEDIUM_CAPSHIP_ENC = encounter.KuGunboat

    BH_PATROL_ENC = encounter.BhPatrolKu

    GLOBAL_TRADERS_ENC = encounter.KuTransport
    GLOBAL_TRADERS_TLR_ENC = encounter.KuTransportTLR
    BH_TRADE_ENC = encounter.BhTradeKu
    BH_TRADE_TLR_ENC = encounter.BhTradeKuTLR


class RheinlandPiratePopulation(UnlawfulPopulation):
    MAIN_PIRATES = faction.RX_GRP


class LibertyPiratePopulation(UnlawfulPopulation):
    MAIN_PIRATES = faction.LX_GRP


class BretoniaPiratePopulation(UnlawfulPopulation):
    MAIN_PIRATES = faction.BX_GRP


class KusariPiratePopulation(UnlawfulPopulation):
    MAIN_PIRATES = faction.KX_GRP


class CorsairAttackersPopulation(UnlawfulPopulation):
    MAIN_PIRATES = faction.CO_GRP











