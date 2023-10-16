TIER_ONE = 1
TIER_TWO = 2
TIER_THREE = 3
TIER_FOUR = 4

TIER_PER_CLASS = {
    1: 1,
    2: 1,
    3: 1,
    4: 2,
    5: 2,
    6: 2,
    7: 3,
    8: 3,
    9: 4,
}


'''
pirateguns

laser
fire_laser1

photon
photon2
tachyon
particle
neutron
plasma
pulse
'''


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

    def __init__(self, faction, fx_appearance, equip_class):
        self.faction = faction
        self.fx_appearance = fx_appearance
        self.equip_class = equip_class

    def get_tier(self):
        return TIER_PER_CLASS[self.equip_class]

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
        return 'fire_laser1'
