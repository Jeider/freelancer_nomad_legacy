from fx.misc import TIER_ONE, TIER_TWO, TIER_THREE, TIER_FOUR, TIER_FIVE
from text.dividers import SINGLE_DIVIDER


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


class SoundTachyonOnlyFive(WeaponSound):
    BASE_NAME = 'fire_tachyon'
    INDEX_PER_TIER = {
        TIER_ONE: 5,
        TIER_TWO: 5,
        TIER_THREE: 5,
        TIER_FOUR: 5,
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


class AutoSoundFX:
    MEMBERS = [
        'neutron1',
        'neutron2',
        'neutron3',
        'neutron4',
        'neutron5',
        'dangeon_rules',
        'dangeon_forward',
        'dangeon_final_exit',
        'dyson_rubic',
        'nomad_shield',
        'lab_shield',
        'debris_box',
        'roid_mining',
        'hacking',

        'arch_step2',
        'arch_step3',
        'arch_step4',
        'battleship_shield_lock',
        'repair',
        'mod_valid_rubic',


        'nn_hbr1_help1',
        'nn_hbr1_help2',
        'nn_hbr1_help3',
        'nn_hbr1_help4',

        'nn_hbr2_help1',
        'nn_hbr2_help2',
        'nn_hbr2_help3',
        'nn_hbr2_help4',

        'nn_hbr_planet_loot',
        'nn_hbr_planet_exploded',


    ]
    EFFECT_TYPE = 'EFT_EXPLOSION_LARGE'
    PARTICLE_FX = 'ku_laser_01_impact'

    subclasses = []

    def __init__(self, russian=True):
        self.russian = russian

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    def get_members(cls):
        return cls.MEMBERS

    @classmethod
    def get_effect(cls, member):
        if not cls.EFFECT_TYPE:
            raise Exception(f'Wrong configured fx {cls}')

        items = [
            '[Effect]',
            f'nickname = snd_{member}',
            f'effect_type = {cls.EFFECT_TYPE}',
            f'vis_effect = {cls.PARTICLE_FX}',
            f'snd_effect = {member}',
        ]

        return SINGLE_DIVIDER.join(items)

    def get_sound(self, member):
        folder = 'mod' if self.russian else 'mod_eng'

        items = [
            '[Sound]',
            f'nickname = {member}',
            f'file = audio\\{folder}\\GENERATED\\{member}.wav',
            'type = voice',
            'attenuation = -1',
            'range = 10000, 10100',
            'persistent = space',
            'is_2d = true',
        ]

        return SINGLE_DIVIDER.join(items)

    def get_equip(self, member):
        content = f'''
[Motor]
nickname = sound_trigger_{member}_motor
lifetime = 0.1
accel = 0.000000
delay = 0

[Explosion]
nickname = sound_trigger_{member}_explosion
effect = snd_{member}
lifetime = 0.000000, 0.000000
process = disappear
strength = 100
radius = 25
hull_damage = 500
energy_damage = 0
impulse = 0

[Munition]
nickname = sound_trigger_{member}_ammo
explosion_arch = sound_trigger_{member}_explosion
hp_type = hp_gun
requires_ammo = false
hit_pts = 2
one_shot_sound = null
detonation_dist = 50
lifetime = 1000
Motor = sound_trigger_{member}_motor
force_gun_ori = false
const_effect = fx_null
HP_trail_parent = HPExhaust
seeker = LOCK
time_to_lock = 0
seeker_range = 7000
seeker_fov_deg = 360
max_angular_velocity = 1
DA_archetype = equipment\models\weapons\li_rad_missile.3db
material_library = equipment\models\li_equip.mat
mass = 10
volume = 0.000000
owner_safe_time = 0.02

[Gun]
nickname = sound_trigger_{member}
ids_name = 238120
ids_info = 1
DA_archetype = Equipment\\models\\turret\\weapons_platform_small_weapon2.cmp

;DA_archetype = Solar\\dockable\\nomad_lair_turret01.cmp
;material_library = solar\\nomad.mat

HP_child = HPConnect
hit_pts = 90000
explosion_resistance = 0
debris_type = debris_silent
parent_impulse = 20
child_impulse = 80
volume = 50.000000
mass = 10
damage_per_fire = 0
power_usage = 0
refire_delay = 0.1
muzzle_velocity = 100
toughness = 10.600000
flash_particle_name = fx_null
flash_radius = 0
projectile_archetype = sound_trigger_{member}_ammo
separation_explosion = sever_debris
auto_turret = true
turn_rate = 9000
lootable = false
LODranges = 0, 1
'''
        return content

    def get_loadout(self, member):
        return f'''
[Loadout]
nickname = infocard_playback_{member}
equip = dangeon_wp_animation
equip = infinite_power
equip = scanner_auto_infocard
equip = sound_trigger_{member}, HpWeapon01
equip = sound_trigger_{member}, HpWeapon02
;;equip = lair_turret01, HpWeapon01
'''
