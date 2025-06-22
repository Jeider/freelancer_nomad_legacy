from world.equipment import Equipment, Icon, DefaultGood
from text.dividers import SINGLE_DIVIDER
from text.infocards import InfocardBuilder

from fx.weapon import WeaponFX

USE_ANIMATION = 'use_animation = Sc_fire'

WEAPON_TYPE_PER_WEAPON_FX = {
    WeaponFX.FX_LASER: 'W_laser',
    WeaponFX.FX_PHOTON: 'W_photon',
    # WeaponFX.FX_PHOTON2: 'W_photon2',
    WeaponFX.FX_TACHYON: 'W_tachyon',
    WeaponFX.FX_PARTICLE: 'W_particle',
    WeaponFX.FX_NEUTRON: 'W_neutron',
    WeaponFX.FX_PLASMA: 'W_plasma',
    WeaponFX.FX_PULSE: 'W_pulse',
}


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


class Weapon(Equipment):
    ARCHETYPE = 'Gun'
    EXTRA = ['turn_rate = 90']
    DAMAGE_MULTIPLIER = 1
    IS_TURRET = False

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
auto_turret = {auto_turret}
lootable = true
LODranges = {lod_ranges}'''

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
    LI_HEAVY_ION_BLASTER = 'li_heavy_ion_blaster.cmp'
    LI_PLASMA_BLASTER = 'li_plasma_blaster.cmp'
    LI_SMLTURRET = 'li_smlturret.cmp'
    LI_THRUSTGUN = 'li_thrustgun.cmp'
    RH_GAMMA_BEAMER = 'rh_gamma_beamer.cmp'
    RH_PLASMA_GAT_CANNON = 'rh_plasma_gat_cannon.cmp'
    RH_PROTON_BLASTER = 'rh_proton_blaster.cmp'
    RH_THRUSTGUN = 'rh_thrustgun.cmp'

    ICON_PER_WEAPON_MODEL = {
        BR_SLUGGER: Icon.ICON_BR_LAUNCHER,
        KU_HORNET: Icon.ICON_KU_LAUNCHER,
        KU_RECOGNIZER: Icon.ICON_GE_HARPOON,
        GE_MINE: Icon.ICON_LI_LAUNCHER,
        GE_TORPEDO: Icon.ICON_GE_TRP_LAUNCHER,
        LI_CM: Icon.ICON_LI_LAUNCHER,
        LI_RAD: Icon.ICON_LI_LAUNCHER,
        RH_SEEKER: Icon.ICON_RH_LAUNCHER,

        BR_AUTO_SHOTGUN: Icon.ICON_BR_UBERGUN,
        BR_MASS_DRIVER: Icon.ICON_BR_LIGHTGUN,
        BR_RAILGUN: Icon.ICON_BR_HEAVYGUN,
        BR_THRUSTGUN: Icon.ICON_BR_THRUSTGUN,

        CO_PROTON_COOKER: Icon.ICON_CO_UBERGUN,
        CO_RAILDADDY: Icon.ICON_CO_LIGHTGUN,
        CO_SHOCK_THERAPY: Icon.ICON_CO_HEAVYGUN,
        CO_THRUSTGUN: Icon.ICON_LI_LIGHTGUN,

        GE_SHREDDER_SHOTGUN: Icon.ICON_GE_UBERGUN,

        KU_AUTO_BLASTER: Icon.ICON_KU_UBERGUN,
        KU_AUTO_TESLA: Icon.ICON_KU_HEAVYGUN,
        KU_ION_BLASTER: Icon.ICON_KU_LIGHTGUN,
        KU_THRUSTGUN: Icon.ICON_KU_THRUSTGUN,

        LI_AUTO_CANNON: Icon.ICON_LI_UBERGUN,
        LI_CANNON: Icon.ICON_LI_HEAVYGUN,
        LI_LASER_BEAM: Icon.ICON_LI_LIGHTGUN,
        LI_PLASMA_BLASTER: Icon.ICON_LI_HEAVYGUN,
        LI_HEAVY_ION_BLASTER: Icon.ICON_LI_HEAVYGUN,
        LI_SMLTURRET: Icon.ICON_LI_LIGHTGUN,
        LI_THRUSTGUN: Icon.ICON_LI_THRUSTGUN,

        RH_GAMMA_BEAMER: Icon.ICON_RH_LIGHTGUN,
        RH_PLASMA_GAT_CANNON: Icon.ICON_RH_UBERGUN,
        RH_PROTON_BLASTER: Icon.ICON_RH_HEAVYGUN,
        RH_THRUSTGUN: Icon.ICON_RH_THRUSTGUN,
    }  

    RH_MODELS = [
        RH_SEEKER, RH_GAMMA_BEAMER, RH_PLASMA_GAT_CANNON,
        RH_PROTON_BLASTER, RH_THRUSTGUN,
    ]

    LI_MODELS = [
        LI_CM, LI_RAD, LI_AUTO_CANNON, LI_CANNON, LI_THRUSTGUN,
        LI_LASER_BEAM, LI_PLASMA_BLASTER, LI_SMLTURRET, LI_HEAVY_ION_BLASTER
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

    NOT_ANIMATED_MODELS = [
        RH_THRUSTGUN,
        LI_THRUSTGUN,
        BR_THRUSTGUN,
        KU_THRUSTGUN,
        CO_THRUSTGUN,
        GE_MINE,
        GE_TORPEDO,
    ]

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

    SHIELDGUN = False
    EXTRA_SHIELD_DAMAGE_FACTOR = 0
    SHIELDGUN_HULL_DAMAGE_FACTOR = 0.1

    def __init__(self, ids, faction, equipment_class, weapon_fx):
        self.ids = ids
        self.faction = faction

        self.validate_model()

        self.equipment_class = equipment_class
        self.weapon_fx = weapon_fx

        self.set_rate()

        self.munition = self.create_munition()

        self.ids_name = ids.new_name(self.get_ru_name())
        self.ids_info = ids.new_info(
            InfocardBuilder.build_equip_infocard(
                self.get_ru_fullname(),
                self.get_ru_description_content()
            )
        )

    def validate_model(self):
        if self.MODEL not in self.MODELS:
            raise Exception('unknown gun model %s' % self.MODEL)

    def set_rate(self):
        if self.EQUIP_TYPE == self.EQUIP_MAIN:
            self.rate = self.get_main_rate()
        elif self.EQUIP_TYPE == self.EQUIP_CIV:
            self.rate = self.get_civ_rate()
        elif self.EQUIP_TYPE == self.EQUIP_PIRATE:
            self.rate = self.get_pirate_rate()

        if not self.rate:
            raise Exception('unknown rate')

    def get_nickname(self):
        return '{name}{digit}'.format(
            name=self.BASE_NICKNAME,
            digit=self.get_equipment_class_digit(),
        )

    def get_projectile_archetype_name(self):
        return '{name}_ammo'.format(
            name=self.get_nickname(),
        )

    def get_explosion_archetype_name(self):
        return '{name}_explosion'.format(
            name=self.get_nickname(),
        )

    def get_motor_archetype_name(self):
        return '{name}_motor'.format(
            name=self.get_nickname(),
        )

    def get_da_archetype(self):
        return self.DA_ARCHETYPE_PATH_TEMPLATE.format(model=self.MODEL)

    def get_faction_letter_by_model(self):
        if self.MODEL in self.RH_MODELS:
            return self.RH_LETTER
        if self.MODEL in self.LI_MODELS:
            return self.LI_LETTER
        if self.MODEL in self.BR_MODELS:
            return self.BR_LETTER
        if self.MODEL in self.KU_MODELS:
            return self.KU_LETTER
        if self.MODEL in self.GE_MODELS:
            return self.GE_LETTER

        raise Exception('Unknown faction for model')

    def get_material(self):
        return self.MATERIAL_PATH_TEMPLATE.format(faction_letter=self.get_faction_letter_by_model())

    def get_lod_ranges(self):
        return self.DEFAULT_LOD_RANGES

    def get_gun_hit_pts(self):
        hit_pts = self.GUN_MAX_HIT_PTS * self.rate

        if self.faction == Equipment.FACTION_BR:
            hit_pts *= 1.5

        return hit_pts

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
        return self.REFIRE_DELAY_PER_REFIRE_RATE[self.REFIRE_RATE]

    def get_refire_rate_multipler(self):
        return self.get_refire_delay()

    def get_power_usage(self):
        power_usage = self.MAX_POWER_USAGE * self.rate * self.get_refire_rate_multipler()
        if self.faction == Equipment.FACTION_CO:
            power_usage *= 0.9
        return power_usage

    def get_muzzle_velocity(self):
        return self.MUZZLE_VELOCITY

    def get_flash_particle_name(self):
        return self.weapon_fx.get_flash_particle_name()

    def get_one_shot_sound(self):
        return self.weapon_fx.get_one_shot_sound()

    def get_munition_hit_effect(self):
        return self.weapon_fx.get_munition_hit_effect()

    def get_const_effect(self):
        return self.weapon_fx.get_const_effect()

    def get_damage_multipler(self):
        return self.DAMAGE_MULTIPLIER * self.DAMAGE_PER_REFIRE_RATE_FACTOR[self.REFIRE_RATE]

    def get_hull_damage(self):
        hull_damage = self.MAX_HULL_DAMAGE * self.rate * self.get_refire_rate_multipler() * \
            self.get_damage_multipler()

        if self.SHIELDGUN:
            return hull_damage * self.SHIELDGUN_HULL_DAMAGE_FACTOR

        return hull_damage

    def get_extra_shield_damage_factor(self):
        factor = 0

        if self.EXTRA_SHIELD_DAMAGE_FACTOR > 0:
            factor += self.EXTRA_SHIELD_DAMAGE_FACTOR

        if self.faction == Equipment.FACTION_KU:
            factor += 0.1

        return factor

    def get_energy_damage(self):
        if not self.SHIELDGUN:
            if self.EXTRA_SHIELD_DAMAGE_FACTOR != 0:
                hull_damage = self.get_hull_damage()
                return hull_damage * self.EXTRA_SHIELD_DAMAGE_FACTOR
            else:
                return 0

        return self.MAX_SHIELD_GUN_DAMAGE * self.rate * self.get_refire_rate_multipler() * \
            self.get_damage_multipler()

    def get_munition_lifetime(self):
        lifetime = self.LIFETIME

        if self.faction == Equipment.FACTION_RH:
            lifetime += 0.2

        return lifetime

    def get_weapon_type(self):
        # if self.SHIELDGUN:
        #     return self.WEAPON_TYPE_SHIELDGUN

        # return self.WEAPON_TYPE_DEFAULT
        return WEAPON_TYPE_PER_WEAPON_FX[self.weapon_fx.get_appearance()]

    def get_munition_params(self):
        return {
            'nickname': self.get_projectile_archetype_name(),
            'hull_damage': self.get_hull_damage(),
            'energy_damage': self.get_energy_damage(),
            'weapon_type': self.get_weapon_type(),
            'one_shot_sound': self.get_one_shot_sound(),
            'munition_hit_effect': self.get_munition_hit_effect(),
            'const_effect': self.get_const_effect(),
            'lifetime': self.get_munition_lifetime(),
        }

    def create_munition(self):
        return WeaponMunition(**self.get_munition_params())

    def get_munition(self):
        return self.munition.get_munition()

    def get_auto_turret(self):
        return str(self.IS_TURRET).lower()

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
            'auto_turret': self.get_auto_turret(),
            'extra': self.EXTRA,
        }

    def get_extra_template_content(self):
        items = []
        if len(self.EXTRA):
            items.extend(self.EXTRA)
        #
        # if self.MODEL not in self.NOT_ANIMATED_MODELS:
        #     items.append(USE_ANIMATION)

        return items

    def get_gun(self):
        template = self.GUN_TEMPLATE.format(**self.get_gun_template_params())
        extra = self.get_extra_template_content()
        if len(extra):
            template += SINGLE_DIVIDER + SINGLE_DIVIDER.join(extra)
        return template

    def get_equip_template_params(self):
        return {
            'munition': self.get_munition(),
            'gun': self.get_gun(),
        }

    def get_equip(self):
        return self.EQUIP_TEMPLATE.format(**self.get_equip_template_params())
