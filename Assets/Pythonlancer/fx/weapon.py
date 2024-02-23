from fx.misc import TIER_ONE, TIER_TWO, TIER_THREE, TIER_FOUR, TIER_FIVE
from fx.sound import SoundLaser, SoundNeutron, SoundParticle, SoundPhoton, SoundPlasma, SoundPulse, SoundTachyon


TIER_PER_CLASS = {
    1: TIER_ONE,
    2: TIER_ONE,
    3: TIER_TWO,
    4: TIER_TWO,
    5: TIER_THREE,
    6: TIER_THREE,
    7: TIER_FOUR,
    8: TIER_FOUR,
    9: TIER_FOUR,
}


class WeaponFX(object):
    FX_TEMPLATE = '{faction}_{fx_appearance}_0{tier}_{fx_usage}'
    FLASH = 'flash'
    PROJ = 'proj'
    IMPACT = 'impact'

    FX_LASER = 'laser'
    FX_PHOTON = 'photon'
    FX_PHOTON2 = 'photon2'
    FX_TACHYON = 'tachyon'
    FX_PARTICLE = 'particle'
    FX_NEUTRON = 'neutron'
    FX_PLASMA = 'plasma'
    FX_PULSE = 'pulse'

    FX_RH = 'rh'
    FX_LI = 'li'
    FX_BR = 'br'
    FX_KU = 'ku'
    FX_PI = 'pi'
    FX_GE = 'ge'
    FX_CI = 'ci'

    SOUND_CLASS_PER_APPEARANCE = {
        FX_LASER: SoundLaser,
        FX_PHOTON: SoundPhoton,
        FX_PHOTON2: SoundPhoton,
        FX_TACHYON: SoundTachyon,
        FX_PARTICLE: SoundParticle,
        FX_NEUTRON: SoundNeutron,
        FX_PLASMA: SoundPlasma,
        FX_PULSE: SoundPulse,
    }

    def __init__(self, faction, fx_appearance, equip_class):
        self.faction = faction
        self.fx_appearance = fx_appearance
        self.equip_class = equip_class
        self.sound_class = self.get_sound_class()

    def get_tier(self):
        return TIER_PER_CLASS[self.equip_class]

    def get_sound_class(self):
        return self.SOUND_CLASS_PER_APPEARANCE[self.fx_appearance]

    def get_fx_params(self, fx_usage):
        return {
            'faction': self.faction,
            'fx_appearance': self.fx_appearance,
            'tier': self.get_tier(),
            'fx_usage': fx_usage,
        }

    def get_fx_name(self, fx_usage):
        return self.FX_TEMPLATE.format(**self.get_fx_params(fx_usage))

    def get_flash_particle_name(self):
        return self.get_fx_name(fx_usage=self.FLASH)

    def get_munition_hit_effect(self):
        return self.get_fx_name(fx_usage=self.IMPACT)

    def get_const_effect(self):
        return self.get_fx_name(fx_usage=self.PROJ)

    def get_one_shot_sound(self):
        return self.sound_class.get_sound_for_tier(self.get_tier())

    def get_appearance(self):
        return self.fx_appearance
