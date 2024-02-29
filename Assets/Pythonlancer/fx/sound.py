from fx.misc import TIER_ONE, TIER_TWO, TIER_THREE, TIER_FOUR, TIER_FIVE


class WeaponSound(object):
    BASE_TEMPLATE = '{base_name}{index}'
    BASE_NAME = ''
    INDEX_PER_TIER = {
        TIER_ONE: 1,
        TIER_TWO: 2,
        TIER_THREE: 3,
        TIER_FOUR: 4,
        TIER_FIVE: 5,
    }

    @classmethod
    def get_sound_for_tier(cls, tier):
        return cls.BASE_TEMPLATE.format(
            base_name=cls.BASE_NAME,
            index=cls.INDEX_PER_TIER[tier]
        )


class SoundLaser(WeaponSound):
    BASE_NAME = 'fire_laser'


class SoundNeutron(WeaponSound):
    BASE_NAME = 'fire_neutron'


class SoundParticle(WeaponSound):
    BASE_NAME = 'fire_particle'


class SoundPhoton(WeaponSound):
    BASE_NAME = 'fire_photon'


class SoundPlasma(WeaponSound):
    BASE_NAME = 'fire_plasma'


class SoundPulse(WeaponSound):
    BASE_NAME = 'fire_pulse'


class SoundTachyon(WeaponSound):
    BASE_NAME = 'fire_tachyon'
    INDEX_PER_TIER = {
        TIER_ONE: 2,
        TIER_TWO: 2,
        TIER_THREE: 3,
        TIER_FOUR: 4,
        TIER_FIVE: 5,
    }


class Ambience(object):
    AST_ICE = 'zone_field_asteroid_ice'
    AST_LAVA = 'zone_field_asteroid_lava'
    AST_MINE = 'zone_field_asteroid_mine'
    AST_ROCK = 'zone_field_asteroid_rock'
    DEBRIS = 'zone_field_debris'
    ICE = 'zone_field_ice'
    MINE = 'zone_field_mine'
    MINE_AST = 'zone_field_mine_asteroid'
    NEBULA_BARRIER = 'zone_nebula_barrier'
    NEBULA_CROW = 'zone_nebula_crow'
    NEBULA_DMATTER = 'zone_nebula_dmatter'
    NEBULA_EDGE = 'zone_nebula_edge'
    NEBULA_WALKER = 'zone_nebula_walker'
    BADLANDS = 'zone_badlands'
    ASTEROID_NOMAD = 'zone_field_asteroid_nomad'
    NOMAD = 'zone_nebula_nomad'
