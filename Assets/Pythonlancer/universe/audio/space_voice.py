import random


class SpaceVoice(object):
    VOICE_MALE_RU = 'dispatcher01'
    VOICE_FEMALE_RU = 'dispatcher02'
    VOICE_ROBOT_RU = 'dispatcher03'

    VOICE_MALE_EN = 'atc_leg_m01_new'
    VOICE_FEMALE_EN = 'atc_leg_f01_new'
    VOICE_ROBOT_EN = 'atc_leg_f01a_new'

    DEFAULT_RU = VOICE_MALE_RU
    DEFAULT_EN = VOICE_MALE_EN

    LINER = 'mod_refer_base_liner'
    ROID_MINER = 'mod_refer_base_roid_miner'
    GAS_MINER = 'mod_refer_base_gas_miner'
    RESEARCH_BASE = 'mod_refer_base_research_base'
    SOLAR_PLANT = 'mod_refer_base_solar_plant'
    FREEPORT = 'mod_refer_base_freeport'
    PRISON = 'mod_refer_base_prison'
    OUTPOST = 'mod_refer_base_outpost'
    BATTLESHIP = 'mod_refer_base_battleship'
    MILITARY = 'mod_refer_base_military'
    RESEARCH = 'mod_refer_base_research'
    SHIPYARD = 'mod_refer_base_shipyard'
    FACTORY = 'mod_refer_base_factory'
    STATION = 'mod_refer_base_station'
    BORDER_STATION = 'mod_refer_base_border'
    MINING = 'mod_refer_base_mining'
    MINING_PLANET = 'mod_refer_base_mining_planet'
    ASTEROID = 'mod_refer_base_asteroid_station'
    RH_PLANET = 'mod_refer_base_rheinland_planet'
    LI_PLANET = 'mod_refer_base_liberty_planet'
    BR_PLANET = 'mod_refer_base_bretonia_planet'
    KU_PLANET = 'mod_refer_base_kusari_planet'
    CO_PLANET = 'mod_refer_base_corsairs_planet'
    OU_PLANET = 'mod_refer_base_outcasts_planet'
    PI_PLANET = 'mod_refer_base_pirates_planet'
    RH_GASMINER = 'mod_refer_base_rheinland_gasmining'
    LI_GASMINER = 'mod_refer_base_liberty_gasmining'
    BR_GASMINER = 'mod_refer_base_bretonia_gasmining'
    KU_GASMINER = 'mod_refer_base_kusari_gasmining'
    CO_GASMINER = 'mod_refer_base_corsairs_gasmining'
    PI_GASMINER = 'mod_refer_base_pirates_gasmining'


class SpaceCostume(object):
    DEFAULT = 'rh_captain_head, rh_male_guard_body, prop_hat_male_rh_grd_visor, prop_neuralnet_b_right'
    ROBOT_A = ', robot_body_A'
    ROBOT_B = ', robot_body_B'
    ROBOT_C = ', robot_body_C'
    ROBOT_D = ', robot_body_D'
    ROBOT_E = ', robot_body_E'

    ROBOTS = [
        ROBOT_A, ROBOT_B, ROBOT_C, ROBOT_D, ROBOT_E
    ]

    @staticmethod
    def random_robot():
        return random.choice(SpaceCostume.ROBOTS)
