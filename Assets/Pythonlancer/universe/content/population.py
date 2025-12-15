from universe.content import encounter
from universe import faction

from text.dividers import SINGLE_DIVIDER

POP_FIRST = 'first'
POP_SECOND = 'second'
POP_MIXED = 'mixed'


class Population(object):

    GENERIC_PIRATES = None
    BOUNTY_HUNTERS = None
    GLOBAL_TRADERS = None
    JUNKERS = None

    LIFTER_ENCOUNTERS = '''
encounter = corp_lifter, 5, 1.00000
faction = {main_traders}, 1.00000'''

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
density = 12
repop_time = 10
max_battle_size = 8
pop_type = base_cluster_law
relief_time = 10
density_restriction = 1, unlawfuls'''

    TRADELANE_PARAMS = '''lane_id = 26
tradelane_down = 5
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
            raise Exception('simple defence encounters is not defined %s' % cls.__class__.__name__)
        if not cls.SIMPLE_ARRIVAL_TRADERS_ENCOUNTERS:
            raise Exception('simple arrived traders encounters is not defined %s' % cls.__class__.__name__)
        params = [
            cls.SIMPLE_DEFENCE_PARAMS,
            cls.SIMPLE_DEFENCE_ENCOUNTERS.format(**cls.get_main_defence_template_params()),
            cls.SIMPLE_ARRIVAL_TRADERS_ENCOUNTERS.format(**cls.get_trade_template_params()),
        ]
        return SINGLE_DIVIDER.join(params)

    @classmethod
    def get_medium_defence_params(cls, use_lifter=False):
        if not cls.GENERAL_DEFENCE_ENCOUNTERS:
            raise Exception('general defence encounters is not defined %s' % cls.__class__.__name__)
        if not cls.SIMPLE_ARRIVAL_TRADERS_ENCOUNTERS:
            raise Exception('simple arrived traders encounters is not defined %s' % cls.__class__.__name__)
        params = [
            cls.MEDIUM_DEFENCE_PARAMS,
            cls.GENERAL_DEFENCE_ENCOUNTERS.format(**cls.get_main_defence_template_params()),
            cls.MEDIUM_DEFENCE_ENCOUNTERS.format(**cls.get_medium_defence_template_params()),
            cls.SIMPLE_ARRIVAL_TRADERS_ENCOUNTERS.format(**cls.get_trade_template_params()),
        ]
        if use_lifter:
            params.append(
                cls.LIFTER_ENCOUNTERS.format(**cls.get_lifter_template_params())
            )
        return SINGLE_DIVIDER.join(params)

    @classmethod
    def get_high_defence_params(cls, use_lifter=False):
        if not cls.HIGH_DEFENCE_ENCOUNTERS:
            raise Exception('general defence encounters is not defined %s' % cls.__class__.__name__)
        if not cls.SIMPLE_ARRIVAL_TRADERS_ENCOUNTERS:
            raise Exception('simple arrived traders encounters is not defined %s' % cls.__class__.__name__)
        params = [
            cls.HIGH_DEFENCE_PARAMS,
            cls.GENERAL_DEFENCE_ENCOUNTERS.format(**cls.get_main_defence_template_params()),
            cls.HIGH_DEFENCE_ENCOUNTERS.format(**cls.get_high_defence_template_params()),
            cls.SIMPLE_ARRIVAL_TRADERS_ENCOUNTERS.format(**cls.get_trade_template_params()),
        ]
        if use_lifter:
            params.append(
                cls.LIFTER_ENCOUNTERS.format(**cls.get_lifter_template_params())
            )
        return SINGLE_DIVIDER.join(params)

    @classmethod
    def get_tradelane_arriaval_traders_params(cls):
        if not cls.TRADELANE_ARRIVAL_TRADERS_ENCOUNTERS:
            raise Exception('tradelane encounters is not defined %s' % cls.__class__.__name__)
        params = [
            cls.TRADELANE_PARAMS,
            cls.TRADELANE_ARRIVAL_TRADERS_ENCOUNTERS.format(**cls.get_trade_template_params()),
        ]
        return SINGLE_DIVIDER.join(params)

    @classmethod
    def get_pirate_defence_params(cls, faction):
        # if not cls.GENERAL_DEFENCE_ENCOUNTERS:
        #     raise Exception('general defence encounters is not defined %s' % cls.__class__.__name__)
        params = [
            cls.MEDIUM_DEFENCE_PARAMS,
            cls.GENERAL_DEFENCE_ENCOUNTERS.format(main_faction=faction.get_code()),
        ]
        return SINGLE_DIVIDER.join(params)

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

    @classmethod
    def get_lifter_template_params(cls):
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
        encounter.Lifter,
    ]
    POLICE_PATROL = encounter.PatrolPolice

    HIGH_CAPSHIP_ENC = None
    MEDIUM_CAPSHIP_ENC = None

    BH_PATROL_ENC = encounter.BhPatrol

    GLOBAL_TRADERS_ENC = None
    GLOBAL_TRADERS_TLR_ENC = None
    BH_TRADE_ENC = encounter.BhTrade
    BH_TRADE_TLR_ENC = encounter.BhTradeTLR

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
            'main_faction': cls.MAIN_FACTION.get_code(),
            'main_traders': cls.MAIN_TRADERS.get_code(),
            'global_traders': cls.GLOBAL_TRADERS.get_code(),
            'bounty_hunters': cls.BOUNTY_HUNTERS.get_code(),
            'global_traders_encounter': cls.GLOBAL_TRADERS_ENC.get_nickname(),
            'global_traders_encounter_tlr': cls.GLOBAL_TRADERS_TLR_ENC.get_nickname(),
            'bounter_hunter_trade_encounter': cls.BH_TRADE_ENC.get_nickname(),
            'bounter_hunter_trade_encounter_tlr': cls.BH_TRADE_TLR_ENC.get_nickname(),
        }

    @classmethod
    def get_main_defence_template_params(cls):
        return {
            'main_faction': cls.MAIN_FACTION.get_code(),
        }

    @classmethod
    def get_high_defence_template_params(cls):
        return {
            'high_defence_capship_encounter': cls.HIGH_CAPSHIP_ENC.get_nickname(),
            'main_faction': cls.MAIN_FACTION.get_code(),
        }

    @classmethod
    def get_medium_defence_template_params(cls):
        return {
            'medium_defence_capship_encounter': cls.MEDIUM_CAPSHIP_ENC.get_nickname(),
            'main_faction': cls.MAIN_FACTION.get_code(),
        }

    @classmethod
    def get_lifter_template_params(cls):
        return {
            'main_traders': cls.GLOBAL_TRADERS.get_code(),
        }

    @classmethod
    def get_lawful_factions(cls):
        factions = [
            cls.MAIN_FACTION,
            cls.MAIN_TRADERS,
            cls.BOUNTY_HUNTERS,
            cls.GLOBAL_TRADERS,
        ]
        return [f for f in factions if f is not None]

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
    GENERIC_PIRATES = None
    JUNKERS = None
    ATTACK_TLR_PATROL = encounter.PatrolTLR

    GENERAL_DEFENCE_ENCOUNTERS = '''
encounter = main_defend, 5, 0.80000
faction = {main_faction}, 1.00000'''

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
        factions = [
            cls.MAIN_PIRATES,
            cls.GENERIC_PIRATES,
            cls.JUNKERS,
        ]
        return [f for f in factions if f is not None]

    @classmethod
    def get_encounter_definitions(cls):
        return [cls.ATTACK_TLR_PATROL]


class RheinlandLegalPopulation(LawfulPopulation):
    MAIN_FACTION = faction.RheinlandMain
    MAIN_TRADERS = faction.RheinlandCivilians
    GENERIC_PIRATES = faction.Hessians
    BOUNTY_HUNTERS = faction.RheinlandHunters
    GLOBAL_TRADERS = faction.RheinlandTraders
    JUNKERS = faction.Junkers

    HIGH_CAPSHIP_ENC = encounter.RhCruiser
    MEDIUM_CAPSHIP_ENC = encounter.RhGunboat

    GLOBAL_TRADERS_ENC = encounter.RhTransport
    GLOBAL_TRADERS_TLR_ENC = encounter.RhTransportTLR


class LibertyLegalPopulation(LawfulPopulation):
    MAIN_FACTION = faction.LibertyMain
    MAIN_TRADERS = faction.LibertyCivilians
    GENERIC_PIRATES = faction.LibertyPirate
    BOUNTY_HUNTERS = faction.LibertyHunters
    GLOBAL_TRADERS = faction.LibertyTraders
    JUNKERS = faction.LibertyRogues

    HIGH_CAPSHIP_ENC = encounter.LiCruiser
    MEDIUM_CAPSHIP_ENC = encounter.LiCruiser

    GLOBAL_TRADERS_ENC = encounter.LiTransport
    GLOBAL_TRADERS_TLR_ENC = encounter.LiTransportTLR


class BretoniaLegalPopulation(LawfulPopulation):
    MAIN_FACTION = faction.BretoniaMain
    MAIN_TRADERS = faction.BretoniaCivilians
    GENERIC_PIRATES = faction.BretoniaPirate
    BOUNTY_HUNTERS = faction.BretoniaHunters
    GLOBAL_TRADERS = faction.BretoniaTraders
    JUNKERS = faction.Xenos

    HIGH_CAPSHIP_ENC = encounter.BrDestroyer
    MEDIUM_CAPSHIP_ENC = encounter.BrGunboat

    GLOBAL_TRADERS_ENC = encounter.BrTransport
    GLOBAL_TRADERS_TLR_ENC = encounter.BrTransportTLR


class KusariLegalPopulation(LawfulPopulation):
    MAIN_FACTION = faction.KusariMain
    MAIN_TRADERS = faction.KusariCivilians
    GENERIC_PIRATES = faction.KusariPirate
    BOUNTY_HUNTERS = faction.KusariHunters
    GLOBAL_TRADERS = faction.KusariTraders
    JUNKERS = faction.FarmerAlliance

    HIGH_CAPSHIP_ENC = encounter.KuDestroyer
    MEDIUM_CAPSHIP_ENC = encounter.KuGunboat

    GLOBAL_TRADERS_ENC = encounter.KuTransport
    GLOBAL_TRADERS_TLR_ENC = encounter.KuTransportTLR


class RheinlandPiratePopulation(UnlawfulPopulation):
    MAIN_PIRATES = faction.RheinlandPirate
    GENERIC_PIRATES = faction.Hessians
    JUNKERS = faction.Junkers


class RheinlandOutcastPopulation(UnlawfulPopulation):
    MAIN_PIRATES = faction.RheinlandPirate
    GENERIC_PIRATES = faction.Outcasts
    JUNKERS = faction.Junkers


class LibertyPiratePopulation(UnlawfulPopulation):
    MAIN_PIRATES = faction.LibertyPirate
    GENERIC_PIRATES = faction.LibertyRogues
    JUNKERS = faction.LaneHackers


class LibertyHackersPopulation(UnlawfulPopulation):
    MAIN_PIRATES = faction.LibertyPirate
    GENERIC_PIRATES = faction.LaneHackers
    JUNKERS = faction.LaneHackers


class BretoniaPiratePopulation(UnlawfulPopulation):
    MAIN_PIRATES = faction.BretoniaPirate
    GENERIC_PIRATES = faction.Ireland
    JUNKERS = faction.Xenos


class BretoniaXenosPopulation(UnlawfulPopulation):
    MAIN_PIRATES = faction.BretoniaPirate
    GENERIC_PIRATES = faction.Xenos
    JUNKERS = faction.Xenos


class KusariPiratePopulation(UnlawfulPopulation):
    MAIN_PIRATES = faction.KusariPirate
    GENERIC_PIRATES = faction.FarmerAlliance
    JUNKERS = faction.FarmerAlliance


class KusariShinobiPopulation(UnlawfulPopulation):
    MAIN_PIRATES = faction.KusariPirate
    GENERIC_PIRATES = faction.Shinobi
    JUNKERS = faction.FarmerAlliance


class LibertyCorsairAttackersPopulation(UnlawfulPopulation):
    MAIN_PIRATES = faction.Corsairs
    GENERIC_PIRATES = faction.LibertyRogues
    # ATTACK_TLR_PATROL = encounter.PatrolTLREliteOnly


class KusariCorsairAttackersPopulation(UnlawfulPopulation):
    MAIN_PIRATES = faction.Corsairs
    GENERIC_PIRATES = faction.FarmerAlliance
    # ATTACK_TLR_PATROL = encounter.PatrolTLREliteOnly


class BretoniaCorsairAttackersPopulation(UnlawfulPopulation):
    MAIN_PIRATES = faction.Corsairs
    GENERIC_PIRATES = faction.Ireland
    # ATTACK_TLR_PATROL = encounter.PatrolTLREliteOnly
