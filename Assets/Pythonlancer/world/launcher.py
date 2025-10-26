from world.names import *
from world.equipment import Equipment, Icon, MainEquipPrice, LauncherGood
from world import level
from text.infocards import InfocardBuilder
from text.strings import MultiString as MS


GEN_CLASS_TO_MARK = {
    1: MS('Тип A', 'Type A'),
    3: MS('Тип Б', 'Type B'),
    5: MS('Тип В', 'Type C'),
    7: MS('Тип Г', 'Type D'),
    9: MS('Тип Д', 'Type E'),
}

HEAVY_CLASS_TO_MARK = {
    2: MS('Тип A', 'Type A'),
    4: MS('Тип Б', 'Type B'),
    6: MS('Тип В', 'Type C'),
    8: MS('Тип Г', 'Type D'),
    10: MS('Тип Д', 'Type E'),
}

DYNAMIC_AMMO_LIMIT = [
    20,
    30,
    40,
    60,
    100,
]

MINE1_FX_PER_FACTION = {
    Equipment.FACTION_RH: 'rh_mine01',
    Equipment.FACTION_LI: 'li_mine01',
    Equipment.FACTION_BR: 'br_mine01',
    Equipment.FACTION_KU: 'ku_mine01',
    Equipment.FACTION_CO: 'pi_mine01',
}

MINE1_EXPLOSION_PER_FACTION = {
    Equipment.FACTION_RH: 'rh_mine01_blast25',
    Equipment.FACTION_LI: 'li_mine01_blast25',
    Equipment.FACTION_BR: 'br_mine01_blast25',
    Equipment.FACTION_KU: 'ku_mine01_blast25',
    Equipment.FACTION_CO: 'pi_mine01_blast25',
}

MINE2_FX_PER_FACTION = {
    Equipment.FACTION_RH: 'rh_mine02',
    Equipment.FACTION_LI: 'li_mine02',
    Equipment.FACTION_BR: 'br_mine02',
    Equipment.FACTION_KU: 'ku_mine02',
    Equipment.FACTION_CO: 'pi_mine02',
}

MINE2_EXPLOSION_PER_FACTION = {
    Equipment.FACTION_RH: 'rh_mine02_blast25',
    Equipment.FACTION_LI: 'li_mine02_blast25',
    Equipment.FACTION_BR: 'br_mine02_blast25',
    Equipment.FACTION_KU: 'ku_mine02_blast25',
    Equipment.FACTION_CO: 'pi_mine02_blast25',
}

RU_FEATURES_PER_FACTION = {
    Equipment.FACTION_RH: 'Бонус фракции: все рейнландские пусковые установки имеют на треть больший боезапас',
    Equipment.FACTION_LI: 'Бонус фракции: все пусковые установки Либерти имеют на 20% больший радуис взрыва снаряда',
    Equipment.FACTION_BR: 'Бонус фракции: бретонских пусковые установки наносят больше повреждений',
    Equipment.FACTION_KU: 'Бонус фракции: все пусковые установки Кусари перезаряжаются на треть быстрее',
    Equipment.FACTION_CO: 'Бонус фракции: все пусковые установки пограничных миров с 25% вероятностью наносят 40% критических повреждений',
}

RU_SUPER_FEATURES_PER_FACTION = {
    Equipment.FACTION_RH: 'Легендарный бонус фракции: двойной боекомплект',
    Equipment.FACTION_LI: 'Легендарный бонус фракции: на 50% больший радуис взрыва снаряда.',
    Equipment.FACTION_BR: 'Легендарный бонус фракции: значительный бонус к повреждениям',
    Equipment.FACTION_KU: 'Легендарный бонус фракции: моментальная скорость перезарядки',
    Equipment.FACTION_CO: 'Легендарный бонус фракции: 25% вероятность нанесения 100% критических повреждений',
}

EN_FEATURES_PER_FACTION = {
    Equipment.FACTION_RH: 'Faction bonus: all Rheinland launchers have extra 30% of ammo',
    Equipment.FACTION_LI: 'Faction bonus: all Liberty launchers have 20% explosion range of munition',
    Equipment.FACTION_BR: 'Faction bonus: all Bretonia launchers inflict extra damage',
    Equipment.FACTION_KU: 'Faction bonus: all Kusari launchers have 30% faster refire rate',
    Equipment.FACTION_CO: 'Faction bonus: all Border World launchers have 25% chance to inflict 40% extra damage',
}

EN_SUPER_FEATURES_PER_FACTION = {
    Equipment.FACTION_RH: 'Legendary faction bonus: double ammo limit',
    Equipment.FACTION_LI: 'Legendary faction bonus: 50% wider munition explosion range',
    Equipment.FACTION_BR: 'Legendary faction bonus: considerable increased damage',
    Equipment.FACTION_KU: 'Legendary faction bonus: instant reload',
    Equipment.FACTION_CO: 'Legendary faction bonus: 25% chance to inflict 100% extra damage',
}

LAUNCHER_ROOT_PER_FACTION = {
    Equipment.FACTION_RH: 10,
    Equipment.FACTION_LI: 20,
    Equipment.FACTION_BR: 30,
    Equipment.FACTION_KU: 40,
    Equipment.FACTION_CO: 50,
}

LAUNCHER_FX_PER_CLASS = {
    1: 1,
    2: 1,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 2,
    8: 2,
    9: 3,
    10: 3,
}

LAUNCHER_FX_PER_CLASS_ALT = {
    1: 5,
    2: 5,
    3: 5,
    4: 5,
    5: 6,
    6: 6,
    7: 6,
    8: 6,
    9: 7,
    10: 7,
}


class Launcher(Equipment, MainEquipPrice, LauncherGood):
    RU_KIND: MS = None
    RU_BASE_INFO: MS = None
    LAUNCHER_MAX_HIT_PTS = 6000
    RU_NAME_PER_FACTION = {}
    RU_NAME_DESC_PER_FACTION = {}
    EN_NAME_PER_FACTION = {}
    EN_NAME_DESC_PER_FACTION = {}
    CLASSES = None
    CLASSES_KEYS = None
    WEAPON_CODE = None
    MAX_PRICE = None
    MAX_AMMO_PRICE = None
    AMMO_LIMIT = 50

    USE_INTRO_NAME = True

    EXPLOSION_RADIUS = None
    MAX_HULL_DAMAGE = None
    MAX_ENERGY_DAMAGE = None

    REFIRE_DELAY = None
    MUZZLE_VELOCITY = None
    DETONATION_DIST = None

    RH_AMMO_LIMIT_MILTIPLIER = 1.4
    KU_REFIRE_MULTIPLIER = 0.67
    LI_EXPLOSION_MULTIPLIER = 1.2
    CRITICAL_DAMAGE_POSSIBILITY = 25
    CRITICAL_DAMAGE = 1.4

    DAMAGE_MULTIPLIER_PER_FACTION = {
        Equipment.FACTION_RH: 1.1,
        Equipment.FACTION_LI: 0.8,
        Equipment.FACTION_BR: 1.3,
        Equipment.FACTION_KU: 1,
        Equipment.FACTION_CO: 0.9,
    }

    DA_ARCHETYPE_PATH_TEMPLATE = 'equipment\\models\\weapons\\{model}'
    MATERIAL_PATH_TEMPLATE = 'equipment\\models\\{faction_letter}_equip.mat'

    BR_SLUGGER = 'br_slugger_launcher.cmp'
    KU_HORNET = 'ku_hornet_launcher.cmp'
    KU_RECOGNIZER = 'ku_recognizer_launcher.cmp'
    GE_MINE = 'ge_mine_dropper.3db'
    GE_TORPEDO = 'ge_torpedo_launcher.cmp'
    LI_CM = 'li_cm_dropper01.cmp'
    LI_RAD = 'li_rad_launcher.cmp'
    RH_SEEKER = 'rh_seeker_launcher.cmp'

    ICON_PER_WEAPON_MODEL = {
        BR_SLUGGER: Icon.ICON_BR_LAUNCHER,
        KU_HORNET: Icon.ICON_KU_LAUNCHER,
        KU_RECOGNIZER: Icon.ICON_GE_HARPOON,
        GE_MINE: Icon.ICON_GE_DROPPER,
        GE_TORPEDO: Icon.ICON_GE_TRP_LAUNCHER,
        LI_CM: Icon.ICON_LI_LAUNCHER,
        LI_RAD: Icon.ICON_LI_LAUNCHER,
        RH_SEEKER: Icon.ICON_RH_LAUNCHER,
    }

    AMMO_ICON_PER_WEAPON_MODEL = {
        BR_SLUGGER: Icon.ICON_BR_MISSILE,
        KU_HORNET: Icon.ICON_KU_ROUND,
        KU_RECOGNIZER: Icon.ICON_KU_ROUND,
        GE_TORPEDO: Icon.ICON_BR_MISSILE,
        LI_CM: Icon.ICON_LI_MISSILE,
        LI_RAD: Icon.ICON_LI_MISSILE,
        RH_SEEKER: Icon.ICON_RH_ROUND,
    }

    RH_MODELS = [RH_SEEKER]
    LI_MODELS = [LI_CM, LI_RAD]
    BR_MODELS = [BR_SLUGGER]
    KU_MODELS = [KU_HORNET, KU_RECOGNIZER]
    GE_MODELS = [GE_MINE, GE_TORPEDO]

    MODEL_PER_FACTION = {
        Equipment.FACTION_RH: RH_SEEKER,
        Equipment.FACTION_LI: LI_RAD,
        Equipment.FACTION_BR: BR_SLUGGER,
        Equipment.FACTION_KU: KU_RECOGNIZER,
        Equipment.FACTION_CO: GE_TORPEDO,
    }

    MODELS = RH_MODELS + LI_MODELS + BR_MODELS + KU_MODELS + GE_MODELS

    FACTION_LETTERS = {
        Equipment.FACTION_RH: 'rh',
        Equipment.FACTION_LI: 'li',
        Equipment.FACTION_BR: 'br',
        Equipment.FACTION_KU: 'ku',
        Equipment.FACTION_CO: 'bw',
    }

    MARK_PER_CLASS = {
        1: 1,
        2: 1,
        3: 2,
        4: 2,
        5: 3,
        6: 3,
        7: 4,
        8: 4,
        9: 5,
        10: 5,
    }

    def __init__(self, ids, faction, equipment_class):
        self.ids = ids
        self.faction = faction

        self.equipment_class = equipment_class

        self.rate = self.get_rate()
        self.mark = self.MARK_PER_CLASS[self.equipment_class]

        self.ids_name = ids.new_name(
            MS(
                self.get_ru_name(),
                self.get_en_name()
            )
        )
        self.ids_info = ids.new_info(
            MS(
                InfocardBuilder.build_equip_infocard(
                    self.get_ru_fullname(),
                    self.get_ru_description_content()
                ),
                InfocardBuilder.build_equip_infocard(
                    self.get_en_fullname(),
                    self.get_en_description_content()
                )
            )
        )

        self.ammo_ids_name = ids.new_name(
            MS(
                self.get_ru_ammo_name(),
                self.get_en_ammo_name()
            )
        )
        self.ammo_ids_info = ids.new_info(
            MS(
                InfocardBuilder.build_equip_infocard(
                    self.get_ru_ammo_fullname(),
                    self.get_ru_ammo_description_content()
                ),
                InfocardBuilder.build_equip_infocard(
                    self.get_en_ammo_fullname(),
                    self.get_en_ammo_description_content()
                )
            )
        )

    def get_fx_index(self):
        return LAUNCHER_ROOT_PER_FACTION[self.faction] + LAUNCHER_FX_PER_CLASS[self.equipment_class]

    def get_mark_name(self):
        return self.CLASSES[self.equipment_class]

    def get_market_level(self):
        return level.MISSILE_LEVEL_PER_CLASS[self.equipment_class]

    def get_faction_letter(self):
        return self.FACTION_LETTERS[self.faction]

    def get_nickname(self):
        return f'{self.get_faction_letter()}_{self.WEAPON_CODE}_{self.get_equipment_class_digit()}'

    def get_ammo_nickname(self):
        return f'{self.get_nickname()}_ammo'

    def get_critical_damage_value(self):
        return f'critical_hit = {self.CRITICAL_DAMAGE_POSSIBILITY}, {self.CRITICAL_DAMAGE}'

    def get_rate(self):
        return self.get_main_rate()

    def get_initial_ammo_limit(self):
        return DYNAMIC_AMMO_LIMIT[self.mark-1]

    def get_ammo_limit(self):
        ammo = self.get_initial_ammo_limit()
        if self.faction == Equipment.FACTION_RH:
            ammo *= self.RH_AMMO_LIMIT_MILTIPLIER
        return int(ammo)

    def get_ru_base_name(self):
        return self.RU_NAME_PER_FACTION[self.faction]

    def get_ru_name(self):
        if self.USE_INTRO_NAME:
            return '{ru_kind} {base_name} {mark}'.format(
                ru_kind=self.RU_KIND.get_ru(),
                base_name=self.get_ru_base_name(),
                mark=self.get_mark_name().get_ru(),
            )
        else:
            return '{base_name} {mark}'.format(
                base_name=self.get_ru_base_name(),
                mark=self.get_mark_name().get_ru(),
            )

    def get_ru_ammo_name(self):
        return f'Снаряд: {self.get_ru_base_name()} {self.get_mark_name().get_ru()}'

    def get_ru_name_desc(self):
        return self.RU_NAME_DESC_PER_FACTION[self.faction]

    def get_ru_ammo_fullname(self):
        return 'Снаряд для установки {name}'.format(
            name=self.get_ru_name()
        )

    def get_ru_fullname(self):
        return '{described_name} {name} {mark}'.format(
            name=self.get_ru_base_name(),
            mark=self.get_mark_name().get_ru(),
            described_name=self.get_ru_name_desc(),
        )

    def get_ru_description_content(self):
        content = []

        content.append(self.RU_BASE_INFO.get_ru())

        faction_bonus_text = RU_FEATURES_PER_FACTION.get(self.faction)
        if faction_bonus_text:
            content.append(faction_bonus_text)

        content.append(f'Боекомплект: {self.get_ammo_limit()}')

        content.append(
            f'*Требуются снаряды типа {self.get_ru_name()}'
        )

        return content

    def get_ru_ammo_description_content(self):
        content = []

        content.append(self.RU_BASE_INFO.get_ru())

        content.append(f'Боекомплект: {self.get_ammo_limit()}')

        content.append(
            f'Требуется для стрельбы установкой {self.get_ru_name()}'
        )

        return content

    def get_en_base_name(self):
        return self.EN_NAME_PER_FACTION[self.faction]

    def get_en_name(self):
        return '{base_name} {ru_kind} {mark}'.format(
            ru_kind=self.RU_KIND.get_en(),
            base_name=self.get_en_base_name(),
            mark=self.get_mark_name().get_en(),
        )

    def get_en_ammo_name(self):
        return f'Munition: {self.get_en_base_name()} {self.get_mark_name().get_en()}'

    def get_en_name_desc(self):
        return self.EN_NAME_DESC_PER_FACTION[self.faction]

    def get_en_ammo_fullname(self):
        return 'Munition for launcher {name}'.format(
            name=self.get_en_name()
        )

    def get_en_fullname(self):
        return '{described_name} {name} {mark}'.format(
            name=self.get_en_base_name(),
            mark=self.get_mark_name().get_en(),
            described_name=self.get_en_name_desc(),
        )

    def get_en_description_content(self):
        content = []

        content.append(self.RU_BASE_INFO.get_en())

        faction_bonus_text = EN_FEATURES_PER_FACTION.get(self.faction)
        if faction_bonus_text:
            content.append(faction_bonus_text)

        content.append(f'Ammo limit: {self.get_ammo_limit()}')

        content.append(
            f'*Requires munition with type: {self.get_en_name()}'
        )

        return content

    def get_en_ammo_description_content(self):
        content = []

        content.append(self.RU_BASE_INFO.get_en())

        content.append(f'Ammo limit: {self.get_ammo_limit()}')

        content.append(
            f'This munition is required by launcher: {self.get_en_name()}'
        )

        return content

    def get_launcher_hit_pts(self):
        return self.LAUNCHER_MAX_HIT_PTS * self.rate

    def get_ammo_ids_name(self):
        return self.ammo_ids_name.id

    def get_ammo_ids_info(self):
        return self.ammo_ids_info.id

    def get_ids_name(self):
        return self.ids_name.id

    def get_ids_info(self):
        return self.ids_info.id

    def get_damage_multipler_per_faction(self):
        return self.DAMAGE_MULTIPLIER_PER_FACTION[self.faction]

    def get_model(self):
        return self.MODEL_PER_FACTION[self.faction]

    def get_da_archetype(self):
        return self.DA_ARCHETYPE_PATH_TEMPLATE.format(model=self.get_model())

    def get_faction_letter_by_model(self):
        model = self.get_model()
        if model in self.RH_MODELS:
            return self.RH_LETTER
        if model in self.LI_MODELS:
            return self.LI_LETTER
        if model in self.BR_MODELS:
            return self.BR_LETTER
        if model in self.KU_MODELS:
            return self.KU_LETTER
        if model in self.GE_MODELS:
            return self.GE_LETTER

        raise Exception('Unknown faction for model')

    def get_material(self):
        return self.MATERIAL_PATH_TEMPLATE.format(faction_letter=self.get_faction_letter_by_model())

    def get_critical_hit(self):
        return (
            self.get_critical_damage_value()
            if self.faction == Equipment.FACTION_CO
            else ''
        )

    def get_icon(self):
        icon = self.ICON_PER_WEAPON_MODEL[self.get_model()]
        return Icon.get_icon_path(icon)

    def get_ammo_icon(self):
        icon = self.AMMO_ICON_PER_WEAPON_MODEL[self.get_model()]
        return Icon.get_icon_path(icon)

    def get_max_price(self):
        return self.MAX_PRICE

    def get_max_ammo_price(self):
        return self.MAX_AMMO_PRICE

    def get_explosion_radius(self):
        radius = self.EXPLOSION_RADIUS

        if self.faction == Equipment.FACTION_LI:
            radius *= self.LI_EXPLOSION_MULTIPLIER

        return radius

    def get_hull_damage(self):
        return self.MAX_HULL_DAMAGE * self.get_damage_multipler_per_faction() * self.rate

    def get_energy_damage(self):
        if self.MAX_ENERGY_DAMAGE == 0:
            return 0

        return self.MAX_ENERGY_DAMAGE * self.get_damage_multipler_per_faction() * self.rate

    def get_refire_delay(self):
        refire = self.REFIRE_DELAY
        if self.faction == Equipment.FACTION_KU:
            refire *= self.KU_REFIRE_MULTIPLIER
        return refire


class Missile(Launcher):
    SHOT_SOUND = None
    MOTOR_LIFETIME = None
    MOTOR_ACCEL = None

    MUNITION_LIFETIME = None
    SEEKER_RANGE = None
    SEEKER_FOV = None
    ANGULAR_VELOCITY = None


    IS_DISRUPTOR = False

    def get_explosion_fx(self):
        raise NotImplementedError

    def get_const_fx(self):
        raise NotImplementedError

    def get_hp_gun_type(self):
        return 'hp_gun_special_{equipment_class}'.format(
            equipment_class=self.equipment_class
        )

    def get_muzzle_velocity(self):
        return self.MUZZLE_VELOCITY

    def is_disruptor(self):
        return (
            'cruise_disruptor = true'
            if self.IS_DISRUPTOR
            else ''
        )

    def get_seeker_fov(self):
        return self.SEEKER_FOV

    def get_seeker_range(self):
        return self.SEEKER_RANGE

    def get_motor_accel(self):
        return self.MOTOR_ACCEL

    def get_equip(self):
        equip_name = self.get_nickname()
        ammo_name = self.get_ammo_nickname()
        return f'''[Motor]
nickname = {equip_name}_motor
lifetime = {self.MOTOR_LIFETIME}
accel = {self.get_motor_accel()}
delay = 0

[Explosion]
nickname = {equip_name}_explosion
effect = {self.get_explosion_fx()}
lifetime = 0.000000, 0.000000
process = disappear
strength = 100
radius = {self.get_explosion_radius()}
hull_damage = {self.get_hull_damage()}
energy_damage = {self.get_energy_damage()}
impulse = 0

[Munition]
nickname = {ammo_name}
explosion_arch = {equip_name}_explosion
loot_appearance = ammo_crate
units_per_container = 10
hp_type = hp_gun
requires_ammo = true
hit_pts = 2
one_shot_sound = {self.SHOT_SOUND}
detonation_dist = {self.DETONATION_DIST}
lifetime = {self.MUNITION_LIFETIME}
Motor = {equip_name}_motor
force_gun_ori = false
const_effect = {self.get_const_fx()}
HP_trail_parent = HPExhaust
seeker = LOCK
time_to_lock = 0
seeker_range = {self.get_seeker_range()}
seeker_fov_deg = {self.get_seeker_fov()}
max_angular_velocity = {self.ANGULAR_VELOCITY}
DA_archetype = equipment\\models\\weapons\\li_rad_missile.3db
material_library = equipment\\models\\li_equip.mat
ids_name = {self.get_ammo_ids_name()}
ids_info = {self.get_ammo_ids_info()}
mass = 1
volume = 0.000000
ammo_limit = {self.get_ammo_limit()}
{self.is_disruptor()}
{self.get_critical_hit()}

[Gun]
nickname = {equip_name}
ids_name = {self.get_ids_name()}
ids_info = {self.get_ids_info()}
DA_archetype = {self.get_da_archetype()}
material_library = {self.get_material()}
HP_child = HPConnect
hit_pts = {self.get_launcher_hit_pts()}
explosion_resistance = 1.000000
debris_type = debris_normal
parent_impulse = 20
child_impulse = 80
volume = 0.000000
mass = 10
hp_gun_type = {self.get_hp_gun_type()}
damage_per_fire = 0
power_usage = 0
refire_delay = {self.get_refire_delay()}
muzzle_velocity = {self.get_muzzle_velocity()}
toughness = 1
projectile_archetype = {ammo_name}
dry_fire_sound = fire_dry
separation_explosion = sever_debris
auto_turret = false
turn_rate = 90
lootable = true
LODranges = 0, 200, 300, 500
'''


class MainMissile(Missile):
    WEAPON_CODE = MAIN_MISSILE
    RU_KIND = MS('Ракета', 'Missile')
    RU_BASE_INFO = MS('Сбалансированная ракета с умеренной скоростью и мощностью',
                      'A balanced missile with moderate speed and power')
    MAX_PRICE = 120000
    MAX_AMMO_PRICE = 6000
    SHOT_SOUND = 'fire_missile_regular'

    CLASSES = GEN_CLASS_TO_MARK
    CLASSES_KEYS = CLASSES.keys()

    MOTOR_LIFETIME = 2.750000
    MOTOR_ACCEL = 22.038601

    EXPLOSION_RADIUS = 16
    MAX_HULL_DAMAGE = 5000
    MAX_ENERGY_DAMAGE = 0

    MUNITION_LIFETIME = 13.750000
    SEEKER_RANGE = 1000
    SEEKER_FOV = 35
    ANGULAR_VELOCITY = 2.903330

    REFIRE_DELAY = 3
    MUZZLE_VELOCITY = 30.299999
    DETONATION_DIST = 4

    RU_NAME_PER_FACTION = {
        Equipment.FACTION_RH: 'Разрушитель',
        Equipment.FACTION_LI: 'Джавелин',
        Equipment.FACTION_BR: 'Мортира',
        Equipment.FACTION_KU: 'Катапульта',
        Equipment.FACTION_CO: 'Дрот',
    }

    RU_NAME_DESC_PER_FACTION = {
        Equipment.FACTION_RH: 'Основная рейнландская ракетница',
        Equipment.FACTION_LI: 'Основная ракетница Либерти',
        Equipment.FACTION_BR: 'Основная бретонская ракетница',
        Equipment.FACTION_KU: 'Основная ракетница Кусари',
        Equipment.FACTION_CO: 'Основная ракетница пограничья',
    }

    EN_NAME_PER_FACTION = {
        Equipment.FACTION_RH: 'Destroyer',
        Equipment.FACTION_LI: 'Javelin',
        Equipment.FACTION_BR: 'Mortar',
        Equipment.FACTION_KU: 'Catapult',
        Equipment.FACTION_CO: 'Dart',
    }

    EN_NAME_DESC_PER_FACTION = {
        Equipment.FACTION_RH: 'Main Rheinland missile launcher',
        Equipment.FACTION_LI: 'Main Liberty missile launcher',
        Equipment.FACTION_BR: 'Main Bretonia missile launcher',
        Equipment.FACTION_KU: 'Main Kusari missile launcher',
        Equipment.FACTION_CO: 'Main Border World missile launcher',
    }

    def get_fx_index(self):
        return LAUNCHER_ROOT_PER_FACTION[self.faction] + LAUNCHER_FX_PER_CLASS_ALT[self.equipment_class]

    def get_explosion_fx(self):
        return f'li_missile{self.get_fx_index()}_impact'

    def get_const_fx(self):
        return f'li_missile{self.get_fx_index()}_drive'


class FastMissile(Missile):
    WEAPON_CODE = FAST_MISSILE
    RU_KIND = MS('Ракета', 'Missile')
    RU_BASE_INFO = MS('Быстрая ракета для скоростной нейтрализации противника, но с меньшими наносимыми повреждениями',
                      'A fast missile for quickly neutralizing an enemy, but with less damage inflicted.')
    MAX_PRICE = 150000
    MAX_AMMO_PRICE = 8000
    SHOT_SOUND = 'fire_missile_homing'

    CLASSES = GEN_CLASS_TO_MARK
    CLASSES_KEYS = CLASSES.keys()

    MOTOR_LIFETIME = 2.5
    MOTOR_ACCEL = 26.666700

    EXPLOSION_RADIUS = 16
    MAX_HULL_DAMAGE = 2500
    MAX_ENERGY_DAMAGE = 0

    MUNITION_LIFETIME = 12.500000
    SEEKER_RANGE = 1000
    SEEKER_FOV = 35
    ANGULAR_VELOCITY = 4.355000

    REFIRE_DELAY = 2
    MUZZLE_VELOCITY = 33.299999
    DETONATION_DIST = 4

    RU_NAME_PER_FACTION = {
        Equipment.FACTION_RH: 'Охотник',
        Equipment.FACTION_LI: 'Сталкер',
        Equipment.FACTION_BR: 'Рибадекин',
        Equipment.FACTION_KU: 'Баллиста',
        Equipment.FACTION_CO: 'Огненный охотник',
    }

    RU_NAME_DESC_PER_FACTION = {
        Equipment.FACTION_RH: 'Скоростная рейнландская ракетница',
        Equipment.FACTION_LI: 'Скоростная ракетница Либерти',
        Equipment.FACTION_BR: 'Скоростная бретонская ракетница',
        Equipment.FACTION_KU: 'Скоростная ракетница Кусари',
        Equipment.FACTION_CO: 'Скоростная ракетница внешних миров',
    }

    EN_NAME_PER_FACTION = {
        Equipment.FACTION_RH: 'Hunter',
        Equipment.FACTION_LI: 'Stalker',
        Equipment.FACTION_BR: 'Ribauldequin',
        Equipment.FACTION_KU: 'Ballista',
        Equipment.FACTION_CO: 'FireStalker',
    }

    EN_NAME_DESC_PER_FACTION = {
        Equipment.FACTION_RH: 'Fast Rheinland missile launcher',
        Equipment.FACTION_LI: 'Fast Liberty missile launcher',
        Equipment.FACTION_BR: 'Fast Bretonia missile launcher',
        Equipment.FACTION_KU: 'Fast Kusari missile launcher',
        Equipment.FACTION_CO: 'Fast Border World missile launcher',
    }

    def get_explosion_fx(self):
        return f'li_missile{self.get_fx_index()}_impact'

    def get_const_fx(self):
        return f'li_missile{self.get_fx_index()}_drive'


class MainSuperMissile(MainMissile):
    WEAPON_CODE = MAIN_SUPER_MISSILE
    RU_KIND = MS('Ракета', 'Missile')
    RU_BASE_INFO = MS('Легендарная ракета с усиленными бонусами фракции',
                      'Legendary missile with improved faction bonuses')
    MAX_PRICE = 250000
    MAX_AMMO_PRICE = 8000

    CLASSES = HEAVY_CLASS_TO_MARK
    CLASSES_KEYS = CLASSES.keys()

    RH_AMMO_LIMIT_MILTIPLIER = 2
    KU_REFIRE_MULTIPLIER = 0.33
    LI_EXPLOSION_MULTIPLIER = 1.5
    CRITICAL_DAMAGE_POSSIBILITY = 25
    CRITICAL_DAMAGE = 2

    DAMAGE_MULTIPLIER_PER_FACTION = {
        Equipment.FACTION_RH: 1.3,
        Equipment.FACTION_LI: 1,
        Equipment.FACTION_BR: 1.6,
        Equipment.FACTION_KU: 1.2,
        Equipment.FACTION_CO: 1,
    }

    RU_NAME_PER_FACTION = {
        Equipment.FACTION_RH: 'Подавитель',
        Equipment.FACTION_LI: 'Томагавк',
        Equipment.FACTION_BR: 'Бомбарда',
        Equipment.FACTION_KU: 'Требучет',
        Equipment.FACTION_CO: 'Ланцет',
    }

    RU_NAME_DESC_PER_FACTION = {
        Equipment.FACTION_RH: 'Легендарная рейнландская ракетница',
        Equipment.FACTION_LI: 'Легендарная ракетница Либерти',
        Equipment.FACTION_BR: 'Легендарная бретонская ракетница',
        Equipment.FACTION_KU: 'Легендарная ракетница Кусари',
        Equipment.FACTION_CO: 'Легендарная ракетница внешних миров',
    }

    EN_NAME_PER_FACTION = {
        Equipment.FACTION_RH: 'Supressor',
        Equipment.FACTION_LI: 'Tomahawk',
        Equipment.FACTION_BR: 'Bombard',
        Equipment.FACTION_KU: 'Trebuchet',
        Equipment.FACTION_CO: 'Lancer',
    }

    EN_NAME_DESC_PER_FACTION = {
        Equipment.FACTION_RH: 'Legendary Rheinland missile launcher',
        Equipment.FACTION_LI: 'Legendary Liberty missile launcher',
        Equipment.FACTION_BR: 'Legendary Bretonia missile launcher',
        Equipment.FACTION_KU: 'Legendary Kusari missile launcher',
        Equipment.FACTION_CO: 'Legendary Border World missile launcher',
    }


class ShieldMissile(Missile):
    WEAPON_CODE = SHIELD_MISSILE
    RU_KIND = MS('Ракета', 'Missile')
    RU_BASE_INFO = MS('Легкая ракета, предназначенная для выведения вражеских щитов из строя',
                      'A lightweight missile designed to disable enemy shields')
    MAX_PRICE = 130000
    MAX_AMMO_PRICE = 7500
    SHOT_SOUND = 'fire_missile_emp'

    CLASSES = HEAVY_CLASS_TO_MARK
    CLASSES_KEYS = CLASSES.keys()

    MOTOR_LIFETIME = 2.75
    MOTOR_ACCEL = 22.038601

    EXPLOSION_RADIUS = 16
    MAX_HULL_DAMAGE = 200
    MAX_ENERGY_DAMAGE = 8000

    MUNITION_LIFETIME = 13.750000
    SEEKER_RANGE = 1000
    SEEKER_FOV = 35
    ANGULAR_VELOCITY = 2.903330

    REFIRE_DELAY = 2
    MUZZLE_VELOCITY = 30.299999
    DETONATION_DIST = 4

    RU_NAME_PER_FACTION = {
        Equipment.FACTION_RH: 'Парализатор',
        Equipment.FACTION_LI: 'Маверик',
        Equipment.FACTION_BR: 'Кулеврина',
        Equipment.FACTION_KU: 'Арбалет',
        Equipment.FACTION_CO: 'Ночной охотник',
    }

    RU_NAME_DESC_PER_FACTION = {
        Equipment.FACTION_RH: 'Рейнландская противощитовая ракетница',
        Equipment.FACTION_LI: 'Противощитовая ракетница Либерти',
        Equipment.FACTION_BR: 'Противощитовая бретонская ракетница',
        Equipment.FACTION_KU: 'Противощитовая ракетница Кусари',
        Equipment.FACTION_CO: 'Противощитовая ракетница внешних миров',
    }

    EN_NAME_PER_FACTION = {
        Equipment.FACTION_RH: 'Paralyzer',
        Equipment.FACTION_LI: 'Maverick',
        Equipment.FACTION_BR: 'Culverine',
        Equipment.FACTION_KU: 'Arbalet',
        Equipment.FACTION_CO: 'NightStalker',
    }

    EN_NAME_DESC_PER_FACTION = {
        Equipment.FACTION_RH: 'Rheinland anti-shield missile launcher',
        Equipment.FACTION_LI: 'Liberty anti-shield missile launcher',
        Equipment.FACTION_BR: 'Bretonia anti-shield missile launcher',
        Equipment.FACTION_KU: 'Kusari anti-shield missile launcher',
        Equipment.FACTION_CO: 'Border World anti-shield missile launcher',
    }

    def get_explosion_fx(self):
        return f'li_empmissile{self.get_fx_index()}_impact'

    def get_const_fx(self):
        return f'li_empmissile{self.get_fx_index()}_drive'


class CruiseDisruptor(Missile):
    WEAPON_CODE = CD_MISSILE
    RU_KIND = MS('Блокир.', 'CD')
    RU_BASE_INFO = MS('Легкая ракета, способная перехватывать вражеские ракеты и нейтрализовывать круизные двигатели вражеских кораблей. '
                      'Блокиратор может быть установлен только на истребитель',
                      'A lightweight missile capable of intercepting enemy missiles and neutralizing the cruise engines of enemy ships. '
                      'Cruise disruptor can be mounted only on fighters')
    MAX_PRICE = 80000
    MAX_AMMO_PRICE = 2500
    SHOT_SOUND = 'fire_cruise_disruptor'

    CLASSES = HEAVY_CLASS_TO_MARK
    CLASSES_KEYS = CLASSES.keys()

    IS_DISRUPTOR = True

    MOTOR_LIFETIME = 0.9
    MOTOR_ACCEL_PER_MARK = [
        500,
        520,
        530,
        550,
        570
    ]

    EXPLOSION_RADIUS = 50
    MAX_HULL_DAMAGE = 500
    MAX_ENERGY_DAMAGE = 0

    MUNITION_LIFETIME = 4.462500
    SEEKER_RANGE_PER_MARK = [
        2500,
        2600,
        2700,
        2800,
        3000
    ]
    SEEKER_FOV_PER_MARK = [
        80, 90, 100, 110, 120
    ]

    ANGULAR_VELOCITY = 8.710000
    REFIRE_DELAY = 2
    MUZZLE_VELOCITY_PER_MARK = [
        200,
        215,
        230,
        250,
        275,
    ]

    DETONATION_DIST = 12.500000

    RU_NAME_PER_FACTION = {
        Equipment.FACTION_RH: 'Оса',
        Equipment.FACTION_LI: 'Стингер',
        Equipment.FACTION_BR: 'Фальконет',
        Equipment.FACTION_KU: 'Гарпун',
        Equipment.FACTION_CO: 'Хорнет',
    }

    RU_NAME_DESC_PER_FACTION = {
        Equipment.FACTION_RH: 'Рейнландский блокиратор круиза',
        Equipment.FACTION_LI: 'Блокиратор круиза Либерти',
        Equipment.FACTION_BR: 'Бретонский блокиратор круиза ',
        Equipment.FACTION_KU: 'Блокиратор круиза Кусари',
        Equipment.FACTION_CO: 'Блокиратор круиза из внешних миров',
    }

    EN_NAME_PER_FACTION = {
        Equipment.FACTION_RH: 'Wasp',
        Equipment.FACTION_LI: 'Stinger',
        Equipment.FACTION_BR: 'Falconet',
        Equipment.FACTION_KU: 'Harpoon',
        Equipment.FACTION_CO: 'Hornet',
    }

    EN_NAME_DESC_PER_FACTION = {
        Equipment.FACTION_RH: 'Rheinland cruise disruptor launcher',
        Equipment.FACTION_LI: 'Liberty cruise disruptor launcher',
        Equipment.FACTION_BR: 'Bretonia cruise disruptor launcher',
        Equipment.FACTION_KU: 'Kusari cruise disruptor launcher',
        Equipment.FACTION_CO: 'Border World cruise disruptor launcher',
    }

    def get_motor_accel(self):
        return self.MOTOR_ACCEL_PER_MARK[self.mark-1]

    def get_muzzle_velocity(self):
        return self.MUZZLE_VELOCITY_PER_MARK[self.mark-1]

    def get_seeker_fov(self):
        return self.SEEKER_FOV_PER_MARK[self.mark-1]

    def get_seeker_range(self):
        return self.SEEKER_RANGE_PER_MARK[self.mark-1]

    def get_explosion_fx(self):
        return f'li_cruisedis{self.get_fx_index():02d}_impact'

    def get_const_fx(self):
        return f'li_cruisedis{self.get_fx_index():02d}_drive'

    def get_hp_gun_type(self):
        return 'hp_torpedo_special_2'

    def get_model(self):
        return self.KU_HORNET


class Torpedo(Missile):
    WEAPON_CODE = TORPEDO_MISSILE
    RU_KIND = MS('Торпеда', 'Torpedo')
    RU_BASE_INFO = MS('Торпеда предназначена для нанесения внушительных повреждений по корпусу противника, '
                      'но при этом имеет минимальную маневренность. '
                      'Торпеды можно устанавливать только на тяжелые истребители',

                      "The torpedo is designed to inflict significant damage to the "
                      "enemy's hull, but has minimal maneuverability. "
                      "Torpedo can be mounted only on heavy fighters"
                      )
    MAX_PRICE = 160000
    MAX_AMMO_PRICE = 7500
    SHOT_SOUND = 'fire_torpedo'

    CLASSES = HEAVY_CLASS_TO_MARK
    CLASSES_KEYS = CLASSES.keys()

    MOTOR_LIFETIME = 11.25
    MOTOR_ACCEL = 3.555600

    EXPLOSION_RADIUS = 25
    MAX_HULL_DAMAGE = 12000
    MAX_ENERGY_DAMAGE = 0

    MUNITION_LIFETIME = 56.250000
    SEEKER_RANGE = 2700
    SEEKER_FOV = 35
    ANGULAR_VELOCITY = 0.580670

    REFIRE_DELAY = 4
    MUZZLE_VELOCITY = 20
    DETONATION_DIST = 6.250000

    RU_NAME_PER_FACTION = {
        Equipment.FACTION_RH: 'Опустошитель',
        Equipment.FACTION_LI: 'Старкиллер',
        Equipment.FACTION_BR: 'Василиск',
        Equipment.FACTION_KU: 'Онагр',
        Equipment.FACTION_CO: 'Катер убийца звёзд',
    }

    RU_NAME_DESC_PER_FACTION = {
        Equipment.FACTION_RH: 'Рейнландская торпедная установка',
        Equipment.FACTION_LI: 'торпедная установка Либерти',
        Equipment.FACTION_BR: 'Бретонская торпедная установка',
        Equipment.FACTION_KU: 'Торпедная установка Кусари',
        Equipment.FACTION_CO: 'Торпедная установка внешних миров',
    }

    EN_NAME_PER_FACTION = {
        Equipment.FACTION_RH: 'Devastator',
        Equipment.FACTION_LI: 'Starkiller',
        Equipment.FACTION_BR: 'Basilisk',
        Equipment.FACTION_KU: 'Onager',
        Equipment.FACTION_CO: 'Sunslayer',
    }

    EN_NAME_DESC_PER_FACTION = {
        Equipment.FACTION_RH: 'Rheinland torpedo launcher',
        Equipment.FACTION_LI: 'Liberty torpedo launcher',
        Equipment.FACTION_BR: 'Bretonia torpedo launcher',
        Equipment.FACTION_KU: 'Kusari torpedo launcher',
        Equipment.FACTION_CO: 'Border World torpedo launcher',
    }

    def get_explosion_fx(self):
        return f'li_torpedo{self.get_fx_index():02d}_impact'

    def get_const_fx(self):
        return f'li_torpedo{self.get_fx_index():02d}_drive'

    def get_hp_gun_type(self):
        return 'hp_torpedo_special_1'

    def get_model(self):
        return self.GE_TORPEDO


class Mine(Launcher):
    SHOT_SOUND = 'fire_mine_tracking'
    MUNITION_LIFETIME = 10
    MAX_ENERGY_DAMAGE = 0

    EXPLOSION_RADIUS = 16
    REFIRE_DELAY = 2
    MUZZLE_VELOCITY = 20
    DETONATION_DIST = 4

    SEEK_RANGE = 400
    TOP_SPEED = 80
    ACCELERATION = 200

    RU_NAME_DESC_PER_FACTION = {
        Equipment.FACTION_RH: 'Рейнландская мина',
        Equipment.FACTION_LI: 'Мина Либерти',
        Equipment.FACTION_BR: 'Бретонская мина',
        Equipment.FACTION_KU: 'Мина Кусари',
        Equipment.FACTION_CO: 'Мина внешних миров',
    }

    EN_NAME_DESC_PER_FACTION = {
        Equipment.FACTION_RH: 'Rheinland mine dropper',
        Equipment.FACTION_LI: 'Liberty mine dropper',
        Equipment.FACTION_BR: 'Bretonia mine dropper',
        Equipment.FACTION_KU: 'Kusari mine dropper',
        Equipment.FACTION_CO: 'Border World mine dropper',
    }

    def get_explosion_fx(self):
        raise NotImplementedError

    def get_const_fx(self):
        raise NotImplementedError

    def get_hp_gun_type(self):
        return 'hp_gun_special_{equipment_class}'.format(
            equipment_class=self.equipment_class
        )

    def get_refire_delay(self):
        refire = self.REFIRE_DELAY
        if self.faction == Equipment.FACTION_KU:
            refire *= self.KU_REFIRE_MULTIPLIER
        return refire

    def get_muzzle_velocity(self):
        return self.MUZZLE_VELOCITY

    def get_model(self):
        return self.GE_MINE

    def get_ammo_icon(self):
        icon = Icon.ICON_MINE_AMMO
        return Icon.get_icon_path(icon)

    def get_equip(self):
        equip_name = self.get_nickname()
        ammo_name = self.get_ammo_nickname()
        return f'''[Explosion]
nickname = {equip_name}_explosion
effect = {self.get_explosion_fx()}
lifetime = 0.000000, 0.000000
process = disappear
strength = 100
radius = {self.get_explosion_radius()}
hull_damage = {self.get_hull_damage()}
energy_damage = {self.get_energy_damage()}
impulse = 0

[Mine]
nickname = {ammo_name}
explosion_arch = {equip_name}_explosion
loot_appearance = ammo_crate
units_per_container = 10
requires_ammo = true
hit_pts = 2
one_shot_sound = {self.SHOT_SOUND}
detonation_dist = {self.DETONATION_DIST}
lifetime = {self.MUNITION_LIFETIME}
force_gun_ori = true
DA_archetype = equipment\\models\\mines\\br_plasma_mine.3db
material_library = equipment\\models\\br_equip.mat
ids_name = {self.get_ammo_ids_name()}
ids_info = {self.get_ammo_ids_info()}
mass = 0.100000
volume = 0.000000
owner_safe_time = 4
linear_drag = 0.400000
seek_dist = {self.SEEK_RANGE}
top_speed = {self.TOP_SPEED}
acceleration = {self.ACCELERATION}
const_effect = {self.get_const_fx()}
ammo_limit = {self.get_ammo_limit()}

[MineDropper]
nickname = {equip_name}
ids_name = {self.get_ids_name()}
ids_info = {self.get_ids_info()}
DA_archetype = {self.get_da_archetype()}
material_library = {self.get_material()}
HP_child = HPConnect
hit_pts = {self.get_launcher_hit_pts()}
explosion_resistance = 1.000000
debris_type = debris_normal
parent_impulse = 20
child_impulse = 80
volume = 0.000000
mass = 10
damage_per_fire = 0
power_usage = 0
refire_delay = {self.get_refire_delay()}
muzzle_velocity = {self.get_muzzle_velocity()}
toughness = 1
projectile_archetype = {ammo_name}
dry_fire_sound = fire_dry
separation_explosion = sever_debris
lootable = true
LODranges = 0, 300
'''


class CivMine(Mine):
    WEAPON_CODE = MINE_CIV
    SEEK_RANGE = 400
    TOP_SPEED = 60
    ACCELERATION = 200
    MAX_HULL_DAMAGE = 4000
    MAX_PRICE = 120000
    MAX_AMMO_PRICE = 7000

    CLASSES = GEN_CLASS_TO_MARK
    CLASSES_KEYS = CLASSES.keys()

    RU_KIND = MS('Мина', 'Mine')
    RU_BASE_INFO = MS('Гражданская мина для защиты от пиратских атак',
                      'Civilian mines for defence against pirate attacks')

    RU_NAME_PER_FACTION = {
        Equipment.FACTION_RH: 'Шнек',
        Equipment.FACTION_LI: 'Каттер',
        Equipment.FACTION_BR: 'Дрон',
        Equipment.FACTION_KU: 'Искатель',
        Equipment.FACTION_CO: 'Мышеловка',
    }

    EN_NAME_PER_FACTION = {
        Equipment.FACTION_RH: 'Screw',
        Equipment.FACTION_LI: 'Cutter',
        Equipment.FACTION_BR: 'Drone',
        Equipment.FACTION_KU: 'Seeker',
        Equipment.FACTION_CO: 'Mousetrap',
    }

    def get_explosion_fx(self):
        return MINE1_EXPLOSION_PER_FACTION[self.faction]

    def get_const_fx(self):
        return MINE1_FX_PER_FACTION[self.faction]

    def get_rate(self):
        return self.get_civ_rate()


class ProfMine(Mine):
    WEAPON_CODE = MINE_PROF
    SEEK_RANGE = 450
    TOP_SPEED = 90
    ACCELERATION = 200
    MAX_HULL_DAMAGE = 4000
    MAX_PRICE = 120000
    MAX_AMMO_PRICE = 7000

    CLASSES = HEAVY_CLASS_TO_MARK
    CLASSES_KEYS = CLASSES.keys()

    RU_KIND = MS('Мина', 'Mine')
    RU_BASE_INFO = MS('Профессиональная боевая мина для эффективных заграждений от надвигающегося противника',
                      'A professional combat mine for effective barriers against an advancing enemy')

    RU_NAME_PER_FACTION = {
        Equipment.FACTION_RH: 'Буровик',
        Equipment.FACTION_LI: 'Рейзор',
        Equipment.FACTION_BR: 'Коптер',
        Equipment.FACTION_KU: 'Цепной пёс',
        Equipment.FACTION_CO: 'Мухобойка',
    }

    EN_NAME_PER_FACTION = {
        Equipment.FACTION_RH: 'Driller',
        Equipment.FACTION_LI: 'Razor',
        Equipment.FACTION_BR: 'Multicopter',
        Equipment.FACTION_KU: 'Chained dog',
        Equipment.FACTION_CO: 'Swatter',
    }

    def get_explosion_fx(self):
        return MINE1_EXPLOSION_PER_FACTION[self.faction]

    def get_const_fx(self):
        return MINE1_FX_PER_FACTION[self.faction]

    def get_rate(self):
        return self.get_pirate_rate()


class MilMine(Mine):
    WEAPON_CODE = MINE_MIL
    SEEK_RANGE = 500
    TOP_SPEED = 120
    ACCELERATION = 300
    MAX_HULL_DAMAGE = 5000
    MAX_PRICE = 150000
    MAX_AMMO_PRICE = 7500

    CLASSES = HEAVY_CLASS_TO_MARK
    CLASSES_KEYS = CLASSES.keys()

    RU_KIND = MS('Мина', 'Mine')
    RU_BASE_INFO = MS('Тяжелая военная мина для использования в регулярных воинских частях и подразделениях',
                      'A heavy military mine for use in regular military units and subdivisions')

    RU_NAME_PER_FACTION = {
        Equipment.FACTION_RH: 'Крикун',
        Equipment.FACTION_LI: 'Риппер',
        Equipment.FACTION_BR: 'Дедал',
        Equipment.FACTION_KU: 'Хищник',
        Equipment.FACTION_CO: 'Капкан',
    }

    EN_NAME_PER_FACTION = {
        Equipment.FACTION_RH: 'Screamer',
        Equipment.FACTION_LI: 'Ripper',
        Equipment.FACTION_BR: 'Dedal',
        Equipment.FACTION_KU: 'Predator',
        Equipment.FACTION_CO: 'Beartrap',
    }

    def get_explosion_fx(self):
        return MINE2_EXPLOSION_PER_FACTION[self.faction]

    def get_const_fx(self):
        return MINE2_FX_PER_FACTION[self.faction]


class CM(Equipment, MainEquipPrice, LauncherGood):
    WEAPON_CODE = CM
    MAX_PRICE = 5000
    MAX_AMMO_PRICE = 50
    LAUNCHER_MAX_HIT_PTS = 5000

    CLASSES = GEN_CLASS_TO_MARK
    CLASSES_KEYS = CLASSES.keys()

    RU_BASE_INFO = MS('Установка, предназначенная для отвлечения вражеских ракет. Используйте в случае ракетной опасности',
                      'A device designed to divert enemy missiles. Use in the event of a missile threat.')

    CM_FX_PER_MARK = [
        'br_countermeasures',
        'br_countermeasures',
        'br_countermeasures',
        'br_countermeasures',
        'ku_countermeasures',
    ]

    CM_DIVERSION_PCT_PER_MARK = [
        60, 70, 75, 80, 90
    ]

    CM_AMMO_PRICE_PER_MARK = [
        20, 25, 35, 40, 50
    ]

    RU_CM_NAME_PER_MARK = [
        'Контрмера',
        'Модифициров. контрмера',
        'Продвинутая контрмера',
        'Улучшенная контрмера',
        'Элитная контрмера',
    ]

    RU_CM_DESC_NAME_PER_MARK = [
        'Базовый постановщик помех',
        'Модифицированный помостановщик помех',
        'Продвинутый постановщик помех',
        'Улучшенный постановщик помех',
        'Элитный постановщик помех',
    ]

    EN_CM_NAME_PER_MARK = [
        'Countermeassure',
        'Modif. Countermeassure',
        'Imp. Countermeassure',
        'Adv. Countermeassure',
        'Elite Countermeassure',
    ]

    EN_CM_DESC_NAME_PER_MARK = [
        'Basic Countermeassure dropper',
        'Modified Countermeassure dropper',
        'Improved Countermeassure dropper',
        'Advanced Countermeassure dropper',
        'Elite Countermeassure dropper',
    ]

    def __init__(self, ids, equipment_class):
        self.ids = ids

        self.equipment_class = equipment_class

        self.rate = self.get_rate()
        self.mark = Launcher.MARK_PER_CLASS[self.equipment_class]

        self.ids_name = ids.new_name(
            MS(
                self.get_ru_name(),
                self.get_en_name()
            )
        )
        self.ids_info = ids.new_info(
            MS(
                InfocardBuilder.build_equip_infocard(
                    self.get_ru_fullname(),
                    self.get_ru_description_content()
                ),
                InfocardBuilder.build_equip_infocard(
                    self.get_en_fullname(),
                    self.get_en_description_content()
                )
            )
        )

        self.ammo_ids_name = ids.new_name(
            MS(
                self.get_ru_ammo_name(),
                self.get_en_ammo_name()
            )
        )
        self.ammo_ids_info = ids.new_info(
            MS(
                InfocardBuilder.build_equip_infocard(
                    self.get_ru_ammo_fullname(),
                    self.get_ru_ammo_description_content()
                ),
                InfocardBuilder.build_equip_infocard(
                    self.get_en_ammo_fullname(),
                    self.get_en_ammo_description_content()
                )
            )
        )

    def get_ammo_price(self):
        return self.CM_AMMO_PRICE_PER_MARK[self.mark-1]

    def get_mark_name(self):
        return self.CLASSES[self.equipment_class]

    def get_market_level(self):
        return level.MISSILE_LEVEL_PER_CLASS[self.equipment_class]

    def get_nickname(self):
        return f'{self.WEAPON_CODE}_{self.mark:02d}'

    def get_ammo_nickname(self):
        return f'{self.get_nickname()}_ammo'

    def get_rate(self):
        return self.get_civ_rate()

    def get_ru_name(self):
        return self.RU_CM_NAME_PER_MARK[self.mark-1]

    def get_ru_ammo_name(self):
        return f'Снаряд: {self.get_ru_name()}'

    def get_ru_ammo_fullname(self):
        return 'Снаряд для установки {name}'.format(
            name=self.get_ru_name()
        )

    def get_ru_fullname(self):
        return self.RU_CM_DESC_NAME_PER_MARK[self.mark-1]

    def get_ru_description_content(self):
        content = []

        content.append(self.RU_BASE_INFO.get_ru())

        content.append(f'Боекомплект: {self.get_ammo_limit()}')

        content.append(
            f'*Требуются снаряды типа {self.get_ru_name()}'
        )

        return content

    def get_ru_ammo_description_content(self):
        content = []

        content.append(self.RU_BASE_INFO.get_ru())

        content.append(f'Боекомплект: {self.get_ammo_limit()}')

        content.append(
            f'Требуется для использования установки {self.get_ru_name()}'
        )

        return content

    def get_en_name(self):
        return self.EN_CM_NAME_PER_MARK[self.mark-1]

    def get_en_ammo_name(self):
        return f'Munition: {self.get_en_name()}'

    def get_en_ammo_fullname(self):
        return 'Munition for launcher {name}'.format(
            name=self.get_en_name()
        )

    def get_en_fullname(self):
        return self.EN_CM_DESC_NAME_PER_MARK[self.mark-1]

    def get_en_description_content(self):
        content = []

        content.append(self.RU_BASE_INFO.get_en())

        content.append(f'Ammo limit: {self.get_ammo_limit()}')

        content.append(
            f'*Requires munition with type {self.get_en_name()}'
        )

        return content

    def get_en_ammo_description_content(self):
        content = []

        content.append(self.RU_BASE_INFO.get_en())

        content.append(f'Ammo limit: {self.get_ammo_limit()}')

        content.append(
            f'This munition is required by launcher {self.get_en_name()}'
        )

        return content

    def get_launcher_hit_pts(self):
        return self.LAUNCHER_MAX_HIT_PTS * self.rate

    def get_ammo_ids_name(self):
        return self.ammo_ids_name.id

    def get_ammo_ids_info(self):
        return self.ammo_ids_info.id

    def get_ids_name(self):
        return self.ids_name.id

    def get_ids_info(self):
        return self.ids_info.id

    def get_faction_letter_by_model(self):
        return self.GE_LETTER

    def get_material(self):
        return Launcher.MATERIAL_PATH_TEMPLATE.format(faction_letter=self.get_faction_letter_by_model())

    def get_icon(self):
        icon = Launcher.ICON_PER_WEAPON_MODEL[self.get_model()]
        return Icon.get_icon_path(icon)

    def get_ammo_icon(self):
        icon = Icon.ICON_CM_AMMO
        return Icon.get_icon_path(icon)

    def get_max_price(self):
        return self.MAX_PRICE

    def get_max_ammo_price(self):
        return self.MAX_AMMO_PRICE

    def get_model(self):
        return Launcher.GE_MINE

    def get_da_archetype(self):
        return Launcher.DA_ARCHETYPE_PATH_TEMPLATE.format(model=self.get_model())

    def get_ammo_limit(self):
        return DYNAMIC_AMMO_LIMIT[self.mark-1]

    def get_const_fx(self):
        return self.CM_FX_PER_MARK[self.mark-1]

    def get_diversion_pct(self):
        return self.CM_DIVERSION_PCT_PER_MARK[self.mark-1]

    def get_equip(self):
        equip_name = self.get_nickname()
        ammo_name = self.get_ammo_nickname()
        return f'''[CounterMeasure]
nickname = {ammo_name}
hit_pts = 2
loot_appearance = ammo_crate
units_per_container = 10
one_shot_sound = fire_countermeasure
const_effect = {self.get_const_fx()}
lifetime = 3
DA_archetype = equipment\\models\\countermeasures\\ge_cm_mark3.cmp
material_library = equipment\\models\\ge_equip.mat
ids_name = {self.get_ammo_ids_name()}
ids_info = {self.get_ammo_ids_info()}
mass = 1
volume = 0.000000
owner_safe_time = 2
force_gun_ori = true
requires_ammo = true
linear_drag = 0.500000
range = 1000
diversion_pctg = {self.get_diversion_pct()}
ammo_limit = {self.get_ammo_limit()}

[CounterMeasureDropper]
nickname = {equip_name}
ids_name = {self.get_ids_name()}
ids_info = {self.get_ids_info()}
DA_archetype = {self.get_da_archetype()}
material_library = {self.get_material()}
HP_child = HpConnect
hit_pts = 1000
explosion_resistance = 0.500000
debris_type = debris_normal
parent_impulse = 20
child_impulse = 80
volume = 0.000000
mass = 10
power_usage = 2
refire_delay = 0.250000
muzzle_velocity = 10
flash_particle_name = li_laser_01_flash
flash_radius = 15
light_anim = l_gun01_flash
projectile_archetype = {ammo_name}
separation_explosion = sever_debris
AI_range = 999
lootable = true
LODranges = 0, 300
'''
