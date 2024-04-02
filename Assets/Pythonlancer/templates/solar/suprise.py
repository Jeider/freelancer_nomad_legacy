import random

from templates.solar.base_solar import MineableSolar


RH_FIGHTER = 'suprise_rh_fighter'
RH_ELITE = 'suprise_rh_elite'
RH_FREIGHTER = 'suprise_rh_freighter'

BW_FIGHTER = 'suprise_bw_fighter'
BW_ELITE = 'suprise_bw_elite'
BW_ELITE2 = 'suprise_bw_elite2'
BW_FREIGHTER = 'suprise_bw_freighter'

KU_FIGHTER = 'suprise_ku_fighter'
KU_ELITE = 'suprise_ku_elite'
KU_FREIGHTER = 'suprise_ku_freighter'

GE_FIGHTER4 = 'suprise_ge_fighter4'
GE_FIGHTER5 = 'suprise_ge_fighter5'
GE_FIGHTER6 = 'suprise_ge_fighter6'

CO_FIGHTER = 'suprise_co_fighter'
CO_ELITE = 'suprise_co_elite'
CO_ELITE2 = 'suprise_co_elite2'

BH_FIGHTER = 'suprise_bh_fighter'
BH_ELITE = 'suprise_bh_elite'
BH_ELITE2 = 'suprise_bh_elite2'

LI_FIGHTER = 'suprise_li_fighter'
LI_ELITE = 'suprise_li_elite'
LI_FREIGHTER = 'suprise_li_freighter'


class Suprise(MineableSolar):
    ALIAS = 'suprise'
    DEFAULT_ARCHETYPES = []
    DROP_HARDPOINT = None

    def get_default_archetype(self):
        return random.choice(self.DEFAULT_ARCHETYPES)

    def get_medium_reward_archetype(self):
        raise Exception('Not supported')

    def get_high_reward_archetype(self):
        raise Exception('Not supported')

    def get_ultra_reward_archetype(self):
        raise Exception('Not supported')

    def get_drop_hardpoint(self):
        if not self.DROP_HARDPOINT:
            raise Exception('Unknown drop hardpoint for %s' % self.__class__.__name__)
        return self.DROP_HARDPOINT


class RheinlandMainFighter(Suprise):
    DROP_HARDPOINT = 'HpShield01'
    DEFAULT_ARCHETYPES = [RH_FIGHTER, RH_ELITE]


class RheinlandMiscFighter(Suprise):
    DROP_HARDPOINT = 'HpCM01'
    DEFAULT_ARCHETYPES = [BW_FIGHTER, BW_ELITE, BW_ELITE2]


class RheinlandAllShip(Suprise):
    DEFAULT_ARCHETYPES = [RH_FIGHTER, RH_ELITE, RH_FREIGHTER, BW_FIGHTER, BW_ELITE, BW_ELITE2, BW_FREIGHTER]


class KusariMainFighter(Suprise):
    DROP_HARDPOINT = 'HpShield01'
    DEFAULT_ARCHETYPES = [KU_FIGHTER, KU_ELITE]


class KusariMiscFighter(Suprise):
    DROP_HARDPOINT = 'HpShield01'
    DEFAULT_ARCHETYPES = [GE_FIGHTER4, GE_FIGHTER5, GE_FIGHTER6]


class LibertyMiscFighter(Suprise):
    DROP_HARDPOINT = 'HpShield01'
    DEFAULT_ARCHETYPES = [BH_FIGHTER, BH_ELITE, BH_ELITE2]
