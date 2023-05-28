from world.equipment import Equipment 



class Motor(object):

    MOTOR_TEMPLATE = '''[Motor]
nickname = {nickname}
lifetime = {lifetime}
accel = {accel}
delay = {delay}'''
    
    def __init__(self, nickname, lifetime=1, accel=20, delay=0):
        self.nickname = nickname
        self.lifetime = lifetime
        self.accel = accel
        self.delay = delay

    def get_template_params(self):
        return {
            'nickname': self.nickname,
            'lifetime': self.lifetime,
            'accel': self.accel,
            'delay': self.delay,
        }


    def get_motor(self):
        return self.MOTOR_TEMPLATE.format(**self.get_template_params())


class Explosion(object):
    
    EXPLOSION_TEMPLATE = '''[Explosion]
nickname = {nickname}
effect = {effect}
lifetime = 0, 0
process = disappear
strength = 100
radius = {radius}
hull_damage = {hull_damage}
energy_damage = {energy_damage}
impulse = 0
'''
    
    def __init__(self, nickname, effect, radius,
                 hull_damage, energy_damage):
        self.nickname = nickname
        self.effect = effect
        self.radius = radius
        self.hull_damage = hull_damage
        self.energy_damage = energy_damage

    def get_template_params(self):
        return {
            'nickname': self.nickname,
            'effect': self.effect,
            'radius': self.radius,
            'hull_damage': self.hull_damage,
            'energy_damage': self.energy_damage,
        }

    def get_explosion(self):
        return self.EXPLOSION_TEMPLATE.format(**self.get_template_params())


class CriticalHitMunition(object):

    CRITICAL_HIT_TEMPLATE = '''
critical_hit = {percent}, {multipler}'''

    def get_critical_hit(self, percent, multipler):
        return CRITICAL_HIT_TEMPLATE.format(percent, multipler)


class WeaponMunition(object):

    MUNITION_TEMPLATE = '''[Munition]
nickname = {nickname}
hp_type = hp_gun
requires_ammo = false
hit_pts = 2
hull_damage = {hull_damage}
energy_damage = {energy_damage}
weapon_type = {weapon_type}
one_shot_sound = {one_shot_sound}
munition_hit_effect = {munition_hit_effect}
const_effect = {const_effect}
lifetime = {lifetime}
force_gun_ori = false
mass = 1
volume = 0.000100'''
    
    def __init__(self, nickname, hull_damage, energy_damage, weapon_type,
                 one_shot_sound, munition_hit_effect, const_effect,
                 lifetime):
        self.nickname = nickname
        self.hull_damage = hull_damage
        self.energy_damage = energy_damage
        self.weapon_type = weapon_type
        self.one_shot_sound = one_shot_sound
        self.munition_hit_effect = munition_hit_effect
        self.const_effect = const_effect
        self.lifetime = lifetime

    def get_template_params(self):
        return {
            'nickname': self.nickname,
            'hull_damage': self.hull_damage,
            'energy_damage': self.energy_damage,
            'weapon_type': self.weapon_type,
            'one_shot_sound': self.one_shot_sound,
            'munition_hit_effect': self.munition_hit_effect,
            'const_effect': self.const_effect,
            'lifetime': self.lifetime,
        }

    def get_munition(self):
        return self.MUNITION_TEMPLATE.format(**self.get_template_params())


class MissileMunition(CriticalHitMunition):

    MUNITION_TEMPLATE = '''[Munition]
nickname = {nickname}
explosion_arch = {explosion_arch}
loot_appearance = ammo_crate
units_per_container = 10
hp_type = hp_gun
requires_ammo = true
hit_pts = 2
one_shot_sound = fire_missile_regular
detonation_dist = {detonation_dist}
lifetime = {lifetime}
Motor = {motor}
force_gun_ori = false
const_effect = {const_effect}
HP_trail_parent = HPExhaust
seeker = LOCK
time_to_lock = 0
seeker_range = {seeker_range}
seeker_fov_deg = {seeker_fov_deg}
max_angular_velocity = {max_angular_velocity}
DA_archetype = {model}
material_library = {material}
ids_name = {ids_name}
ids_info = {ids_info}
mass = 1
volume = 0.000000{appearance}{critical_hit}'''

    RH_MISSILE_SEEKER = '''
DA_archetype = equipment\\models\\weapons\\rh_seeker_missile.3db
material_library = equipment\\models\\rh_equip.mat'''

    LI_MISSILE_RAD = '''
DA_archetype = equipment\\models\\weapons\\li_rad_missile.3db
material_library = equipment\\models\\li_equip.mat'''

    BR_MISSILE_SLUGGER = '''
DA_archetype = equipment\\models\\weapons\\br_slugger_missile.3db
material_library = equipment\\models\\br_equip.mat'''

    KU_MISSILE_HORNET = '''
DA_archetype = equipment\\models\\weapons\\ku_hornet_missile.3db
material_library = equipment\\models\\ku_equip.mat'''

    KU_MISSILE_RECOGNIZER = '''
DA_archetype = equipment\\models\\weapons\\ku_recognizer_missile.3db
material_library = equipment\\models\\ku_equip.mat'''
    
    def __init__(self, nickname, explosion_arch, detonation_dist, lifetime,
                 motor, const_effect, seeker_range, seeker_fov_deg, max_angular_velocity,
                 ids_name, ids_info, appearance, critical_hit=None):
        self.nickname = nickname
        self.explosion_arch = explosion_arch
        self.detonation_dist = detonation_dist
        self.lifetime = lifetime
        self.motor = motor
        self.const_effect = const_effect
        self.seeker_range = seeker_range
        self.seeker_fov_deg = seeker_fov_deg
        self.max_angular_velocity = max_angular_velocity
        self.ids_name = ids_name
        self.ids_info = ids_info
        self.appearance = appearance
        # self.critical_hit = critical_hit

    def get_template_params(self):
        return {
            'nickname': self.nickname,
            'explosion_arch': self.explosion_arch,
            'detonation_dist': self.detonation_dist,
            'lifetime': self.lifetime,
            'motor': self.motor,
            'const_effect': self.const_effect,
            'seeker_range': self.seeker_range,
            'seeker_fov_deg': self.seeker_fov_deg,
            'max_angular_velocity': self.max_angular_velocity,
            'ids_name': self.ids_name,
            'ids_info': self.ids_info,
            'appearance': self.appearance,
            # 'critical_hit': self.
        }

    def get_munition(self):
        return self.MUNITION_TEMPLATE.format(**self.get_template_params())


class MineMunition(CriticalHitMunition):
    
    MUNITION_TEMPLATE = '''[Mine]
nickname = {nickname}
explosion_arch = {explosion_arch}
loot_appearance = ammo_crate
units_per_container = 10
requires_ammo = true
hit_pts = 2
one_shot_sound = fire_mine_regular
detonation_dist = {detonation_dist}
lifetime = {lifetime}
force_gun_ori = true
DA_archetype = equipment\\models\\mines\\br_plasma_mine.3db
material_library = equipment\\models\\br_equip.mat
ids_name = {ids_name}
ids_info = {ids_info}
mass = 0.100000
volume = 0.000000
owner_safe_time = {owner_safe_time}
linear_drag = {linear_drag}
seek_dist = {seek_dist}
top_speed = {top_speed}
acceleration = {acceleration}
const_effect = {const_effect}'''
    
    def __init__(self, nickname, explosion_arch, detonation_dist, lifetime,
                 ids_name, ids_info, owner_safe_time,
                 linear_drag, seek_dist, top_speed, acceleration, const_effect):
        self.nickname = nickname
        self.explosion_arch = explosion_arch
        self.detonation_dist = detonation_dist
        self.lifetime = lifetime
        self.ids_name = ids_name
        self.ids_info = ids_info
        self.owner_safe_time = owner_safe_time
        self.linear_drag = linear_drag
        self.seek_dist = seek_dist
        self.top_speed = top_speed
        self.acceleration = acceleration
        self.const_effect = const_effect

    def get_template_params(self):
        return {
            'nickname': self.nickname,
            'explosion_arch': self.explosion_arch,
            'detonation_dist': self.detonation_dist,
            'lifetime': self.lifetime,
            'ids_name': self.ids_name,
            'ids_info': self.ids_info,
            'owner_safe_time': self.owner_safe_time,
            'linear_drag': self.linear_drag,
            'seek_dist': self.seek_dist,
            'top_speed': self.top_speed,
            'acceleration': self.acceleration,
            'const_effect': self.const_effect,
        }

    def get_munition(self):
        return self.MUNITION_TEMPLATE.format(**self.get_template_params())


class Gun(Equipment):
    ARCHETYPE = 'Gun'
    EXTRA = '''
turn_rate = 90'''
    
    GUN_TEMPLATE = '''[{archetype}]
nickname = {nickname}
ids_name = {ids_name}
ids_info = {ids_info}
DA_archetype = {da_archetype}
material_library = {material}
HP_child = HPConnect
hit_pts = {hit_pts}
explosion_resistance = {explosion_resistance}
volume = 0.000000
mass = 10
hp_gun_type = {hp_gun_type}
damage_per_fire = {damage_per_fire}
power_usage = {power_usage}
refire_delay = {refire_delay}
muzzle_velocity = {muzzle_velocity}
flash_particle_name = {flash_particle_name}
flash_radius = 12
light_anim = multi_gun_flash
turn_rate = 90
projectile_archetype = {projectile_archetype}
auto_turret = false
lootable = true
LODranges = {lod_ranges}{extra}'''

    EQUIP_TEMPLATE = '''{munition}

{gun}'''

    DA_ARCHETYPE_PATH_TEMPLATE = 'equipment\\models\\weapons\\{model}'
    MATERIAL_PATH_TEMPLATE = 'equipment\\models\\{faction_letter}_equip.mat'

    BR_SLUGGER = 'br_slugger_launcher.cmp'
    KU_HORNET = 'ku_hornet_launcher.cmp'
    KU_RECOGNIZER = 'ku_recognizer_launcher.cmp'
    GE_MINE = 'ge_mine_dropper.cmp'
    GE_TORPEDO = 'ge_torpedo_launcher.cmp'
    LI_CM = 'li_cm_dropper01.cmp'
    LI_RAD = 'li_rad_launcher.cmp'
    RH_SEEKER = 'rh_seeker_launcher.cmp'

    BR_AUTO_SHOTGUN = 'br_auto_shotgun.cmp'
    BR_MASS_DRIVER = 'br_mass_driver.cmp'
    BR_RAILGUN = 'br_railgun.cmp'
    BR_THRUSTGUN = 'br_thrustgun.cmp'
    CO_PROTON_COOKER = 'co_proton_cooker.cmp'
    CO_RAILDADDY = 'co_raildaddy.cmp'
    CO_SHOCK_THERAPY = 'co_shock_therapy.cmp'
    CO_THRUSTGUN = 'co_thrustgun.cmp'
    GE_SHREDDER_SHOTGUN = 'ge_shredder_shotgun.cmp'
    KU_AUTO_BLASTER = 'ku_auto_blaster.cmp'
    KU_AUTO_TESLA = 'ku_auto_tesla.cmp'
    KU_ION_BLASTER = 'ku_ion_blaster.cmp'
    KU_THRUSTGUN = 'ku_thrustgun.cmp'
    LI_AUTO_CANNON = 'li_auto_cannon.cmp'
    LI_CANNON = 'li_cannon.cmp'
    LI_LASER_BEAM = 'li_laser_beam.cmp'
    LI_PLASMA_BLASTER = 'li_plasma_blaster.cmp'
    LI_SMLTURRET = 'li_smlturret.cmp'
    LI_THRUSTGUN = 'li_thrustgun.cmp'
    RH_GAMMA_BEAMER = 'rh_gamma_beamer.cmp'
    RH_PLASMA_GAT_CANNON = 'rh_plasma_gat_cannon.cmp'
    RH_PROTON_BLASTER = 'rh_proton_blaster.cmp'
    RH_SEEKER_LAUNCHER = 'rh_seeker_launcher.cmp'
    RH_THRUSTGUN = 'rh_thrustgun.cmp'

    RH_MODELS = [
        RH_SEEKER, RH_GAMMA_BEAMER, RH_PLASMA_GAT_CANNON,
        RH_PROTON_BLASTER, RH_SEEKER_LAUNCHER, RH_THRUSTGUN,
    ]

    LI_MODELS = [
        LI_CM, LI_RAD, LI_AUTO_CANNON, LI_CANNON, LI_THRUSTGUN,
        LI_LASER_BEAM, LI_PLASMA_BLASTER, LI_SMLTURRET,
    ]

    BR_MODELS = [
        BR_SLUGGER, BR_AUTO_SHOTGUN, BR_MASS_DRIVER,
        BR_RAILGUN, BR_THRUSTGUN,
    ]

    KU_MODELS = [
        KU_HORNET, KU_RECOGNIZER, KU_AUTO_BLASTER, KU_AUTO_TESLA,
        KU_ION_BLASTER, KU_THRUSTGUN,
    ]

    GE_MODELS = [
        GE_MINE, GE_TORPEDO, CO_PROTON_COOKER, CO_RAILDADDY,
        CO_SHOCK_THERAPY, CO_THRUSTGUN, GE_SHREDDER_SHOTGUN
    ]

    MODELS = RH_MODELS + LI_MODELS + BR_MODELS + KU_MODELS + GE_MODELS

    REFIRE_RATE_1 = 1
    REFIRE_RATE_2 = 2
    REFIRE_RATE_3 = 3
    REFIRE_RATE_4 = 4
    REFIRE_RATE_6 = 6
    REFIRE_RATE_8 = 8
    REFIRE_RATE_10 = 10

    REFIRE_RATES = [
        REFIRE_RATE_1, REFIRE_RATE_2, REFIRE_RATE_3, REFIRE_RATE_4,
        REFIRE_RATE_6, REFIRE_RATE_8, REFIRE_RATE_10,
    ]

    REFIRE_DELAY_PER_REFIRE_RATE = {
        REFIRE_RATE_1: 1,
        REFIRE_RATE_2: 0.5,
        REFIRE_RATE_3: 0.33,
        REFIRE_RATE_4: 0.25,
        REFIRE_RATE_6: 0.17,
        REFIRE_RATE_8: 0.12,
        REFIRE_RATE_10: 0.09,
    }

    MAX_HULL_DAMAGE = 2000

    DAMAGE_PER_REFIRE_RATE_FACTOR = {
        REFIRE_RATE_1: 1.2,
        REFIRE_RATE_2: 1.1,
        REFIRE_RATE_3: 1.05,
        REFIRE_RATE_4: 1,
        REFIRE_RATE_6: 0.95,
        REFIRE_RATE_8: 0.9,
        REFIRE_RATE_10: 0.8,
    }

    MAX_SHIELD_GUN_DAMAGE = 2000
    MAX_POWER_USAGE = 500

    DEFAULT_LIFETIME = 1
    DEFAULT_MUZZLE_VELOCITY = 1
    DEFAULT_LOD_RANGES = '0, 100, 300, 500'
    DEFAULT_EXPLOSION_RESISTANCE = 0.25
    DEFAULT_DAMAGE_PER_FIRE = 0

    WEAPON_TYPE_DEFAULT = 'W_fighter'
    WEAPON_TYPE_SHIELDGUN = 'W_fighter_shieldgun'

    GUN_MAX_HIT_PTS = 6500

    EQUIP_MAIN = 1
    EQUIP_PIRATE = 2
    EQUIP_CIV = 3

    def __init__(self, faction, base_nickname, ids_name, ids_info, model,
                 equipment_class, equip_type, refire_rate, muzzle_velocity,
                 lifetime, shieldgun=False, extra_shield_damage_factor=0):
        self.faction = faction
        self.base_nickname = base_nickname
        self.ids_name = ids_name
        self.ids_info = ids_info

        self.model = model
        self.validate_model()

        self.equipment_class = equipment_class
        self.equip_type = equip_type

        self.set_rate()

        self.refire_rate = refire_rate
        self.muzzle_velocity = muzzle_velocity
        self.lifetime = lifetime
        self.shieldgun = shieldgun

        self.extra_shield_damage_factor = extra_shield_damage_factor

        self.munition = self.create_munition()

    def validate_model(self):
        if self.model not in self.MODELS:
            raise Exception('unknown gun model')

    def set_rate(self):
        if self.equip_type == self.EQUIP_MAIN:
            self.rate = self.get_main_rate()
        elif self.equip_type == self.EQUIP_CIV:
            self.rate = self.get_civ_rate()
        elif self.equip_type == self.EQUIP_PIRATE:
            self.rate = self.get_pirate_rate()

        if not self.rate:
            raise Exception('unknown rate')

    def get_nickname(self):
        return '{name}{digit}'.format(
            name=self.base_nickname,
            digit=self.get_equipment_class_digit(),
        )

    def get_projectile_archetype_name(self):
        return '{name}_ammo'.format(
            name=self.get_nickname(),
        )

    def get_da_archetype(self):
        return self.DA_ARCHETYPE_PATH_TEMPLATE.format(model=self.model)

    def get_faction_letter_by_model(self):
        if self.model in self.RH_MODELS:
            return self.RH_LETTER
        if self.model in self.LI_MODELS:
            return self.LI_LETTER
        if self.model in self.BR_MODELS:
            return self.BR_LETTER
        if self.model in self.KU_MODELS:
            return self.KU_LETTER
        if self.model in self.GE_MODELS:
            return self.GE_LETTER

        raise Exception('Unknown faction for model')

    def get_material(self):
        return self.MATERIAL_PATH_TEMPLATE.format(faction_letter=self.get_faction_letter_by_model())

    def get_lod_ranges(self):
        return self.DEFAULT_LOD_RANGES

    def get_gun_hit_pts(self):
        return self.GUN_MAX_HIT_PTS * self.rate

    def get_explosion_resistance(self):
        explosion_resistance = self.DEFAULT_EXPLOSION_RESISTANCE

        if self.faction == Equipment.FACTION_LI:
            explosion_resistance *= 0.5

        return explosion_resistance

    def get_hp_gun_type(self):
        return 'hp_gun_special_{equipment_class}'.format(
            equipment_class=self.equipment_class
        )

    def get_damage_per_fire(self):
        return self.DEFAULT_DAMAGE_PER_FIRE

    def get_refire_delay(self):
        return self.REFIRE_DELAY_PER_REFIRE_RATE[self.refire_rate]

    def get_refire_rate_multipler(self):
        return self.get_refire_delay()

    def get_power_usage(self):
        return self.MAX_POWER_USAGE * self.rate * self.get_refire_rate_multipler()

    def get_muzzle_velocity(self):
        return self.muzzle_velocity

    def get_flash_particle_name(self):
        return 'li_laser_01_flash'

    def get_damage_multipler(self):
        return self.DAMAGE_PER_REFIRE_RATE_FACTOR[self.refire_rate]

    def get_hull_damage(self):
        if self.shieldgun:
            return 0

        return self.MAX_HULL_DAMAGE * self.rate * self.get_refire_rate_multipler() * \
            self.get_damage_multipler()

    def get_energy_damage(self):
        if not self.shieldgun:
            if self.extra_shield_damage_factor != 0:
                hull_damage = self.get_hull_damage()
                return hull_damage * self.extra_shield_damage_factor
            else:
                return 0


        return self.MAX_SHIELD_GUN_DAMAGE * self.rate * self.get_refire_rate_multipler() * \
            self.get_damage_multipler()

    def get_munition_lifetime(self):
        lifetime = self.lifetime

        if self.faction == Equipment.FACTION_RH:
            lifetime += 0.2

        return lifetime

    def get_weapon_type(self):
        if self.shieldgun:
            return self.WEAPON_TYPE_SHIELDGUN

        return self.WEAPON_TYPE_DEFAULT

    def get_munition_params(self):
        return {
            'nickname': self.get_projectile_archetype_name(),
            'hull_damage': self.get_hull_damage(),
            'energy_damage': self.get_energy_damage(),
            'weapon_type': self.get_weapon_type(),
            'one_shot_sound': 'fire_laser1',
            'munition_hit_effect': 'li_laser_01_impact',
            'const_effect': 'li_laser_01_proj',
            'lifetime': self.get_munition_lifetime(),
        }

    def create_munition(self):
        return WeaponMunition(**self.get_munition_params())

    def get_munition(self):
        return self.munition.get_munition()

    def get_gun_template_params(self):
        return {
            'archetype': self.ARCHETYPE,
            'nickname': self.get_nickname(),
            'ids_name': self.ids_name,
            'ids_info': self.ids_info,
            'da_archetype': self.get_da_archetype(),
            'material': self.get_material(),
            'hit_pts': self.get_gun_hit_pts(),
            'explosion_resistance': self.get_explosion_resistance(),
            'hp_gun_type': self.get_hp_gun_type(),
            'damage_per_fire': self.get_damage_per_fire(),
            'power_usage': self.get_power_usage(),
            'refire_delay': self.get_refire_delay(),
            'muzzle_velocity': self.get_muzzle_velocity(),
            'flash_particle_name': self.get_flash_particle_name(),
            'projectile_archetype': self.get_projectile_archetype_name(),
            'lod_ranges': self.get_lod_ranges(),
            'extra': self.EXTRA,
        }

    def get_gun(self):
        return self.GUN_TEMPLATE.format(**self.get_gun_template_params())

    def get_equip_template_params(self):
        return {
            'munition': self.get_munition(),
            'gun': self.get_gun(),
        }

    def get_equip(self):
        return self.EQUIP_TEMPLATE.format(**self.get_equip_template_params())


class MineDropper(Gun):
    ARCHETYPE = 'MineDropper'
    EXTRA = '''
dry_fire_sound = fire_dry'''

class Launcher(Gun):
    EXTRA = '''
dry_fire_sound = fire_dry'''


class WeaponFactory(object):
    RH_GUNS = [
        {
            'base_nickname': 'rh_lightgun',
            'model': Gun.RH_GAMMA_BEAMER,
            'equip_type': Gun.EQUIP_MAIN,
            'refire_rate': Gun.REFIRE_RATE_6,
            'muzzle_velocity': 700,
            'lifetime': 1.0,
            'ids_name': 1,
            'ids_info': 1,
        },
        {
            'base_nickname': 'rh_heavygun',
            'model': Gun.RH_PROTON_BLASTER,
            'equip_type': Gun.EQUIP_MAIN,
            'refire_rate': Gun.REFIRE_RATE_2,
            'muzzle_velocity': 500,
            'lifetime': 1.2,
            'ids_name': 1,
            'ids_info': 1,
        },
        {
            'base_nickname': 'rh_civgun',
            'model': Gun.RH_GAMMA_BEAMER,
            'equip_type': Gun.EQUIP_CIV,
            'refire_rate': Gun.REFIRE_RATE_8,
            'muzzle_velocity': 750,
            'lifetime': 0.8,
            'ids_name': 1,
            'ids_info': 1,
        },
        {
            'base_nickname': 'rh_heassiangun',
            'model': Gun.RH_GAMMA_BEAMER,
            'equip_type': Gun.EQUIP_PIRATE,
            'refire_rate': Gun.REFIRE_RATE_8,
            'muzzle_velocity': 750,
            'lifetime': 0.8,
            'ids_name': 1,
            'ids_info': 1,
        },
        {
            'base_nickname': 'rh_junkergun',
            'model': Gun.RH_GAMMA_BEAMER,
            'equip_type': Gun.EQUIP_PIRATE,
            'refire_rate': Gun.REFIRE_RATE_8,
            'muzzle_velocity': 600,
            'lifetime': 1,
            'ids_name': 1,
            'ids_info': 1,
        },
        {
            'base_nickname': 'rh_shieldgun',
            'model': Gun.GE_SHREDDER_SHOTGUN,
            'equip_type': Gun.EQUIP_MAIN,
            'refire_rate': Gun.REFIRE_RATE_4,
            'muzzle_velocity': 600,
            'lifetime': 1.0,
            'ids_name': 1,
            'ids_info': 1,
            'shieldgun': True,
        },
    ]

    def __init__(self):
        self.rh_guns = []

        for gun in self.RH_GUNS:
            for equipment_class in Equipment.BASE_CLASSES:
                self.rh_guns.append(
                    Gun(equipment_class=equipment_class, faction=Equipment.FACTION_RH, **gun)
                )

    def get_rh_guns(self):
        return self.rh_guns
