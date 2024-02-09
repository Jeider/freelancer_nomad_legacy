import random

from templates.solar.base_solar import MineableSolar


RH_FIGHTER = 'suprise_rh_fighter'
RH_ELITE = 'suprise_rh_elite'
RH_FREIGHTER = 'suprise_rh_freighter'

BW_FIGHTER = 'suprise_bw_fighter'
BW_ELITE = 'suprise_bw_elite'
BW_ELITE2 = 'suprise_bw_elite2'
BW_FREIGHTER = 'suprise_bw_freighter'


class Suprise(MineableSolar):
    ALIAS = 'suprise'
    DEFAULT_ARCHETYPES = []

    def get_default_archetype(self):
        return random.choice(self.DEFAULT_ARCHETYPES)

    def get_medium_reward_archetype(self):
        raise Exception('Not supported')

    def get_high_reward_archetype(self):
        raise Exception('Not supported')

    def get_ultra_reward_archetype(self):
        raise Exception('Not supported')


class RheinlandMainFighter(Suprise):
    DEFAULT_ARCHETYPES = [RH_FIGHTER, RH_ELITE]


class RheinlandMiscFighter(Suprise):
    DEFAULT_ARCHETYPES = [BW_FIGHTER, BW_ELITE, BW_ELITE2]


class RheinlandAllShip(Suprise):
    DEFAULT_ARCHETYPES = [RH_FIGHTER, RH_ELITE, RH_FREIGHTER, BW_FIGHTER, BW_ELITE, BW_ELITE2, BW_FREIGHTER]
