from world.equipment import Equipment, MainMiscEquip
from world.npc import NPC
import math
from universe.markets import MarketShip
from text.dividers import SINGLE_DIVIDER
from fx.light import Light

CLASS_INTERCEPTOR = 'class_interceptor'
CLASS_ELITE = 'class_elite_fighter'

CLASS_RHEINLAND_INTERCEPTOR = 'class_rheinland_interceptor'
CLASS_RHEINLAND_ELITE = 'class_rheinland_elite'
CLASS_RHEINLAND_FIGHTER_ONLY = 'class_rheinland_fighter_only'

CLASS_LIBERTY_INTERCEPTOR = 'class_liberty_interceptor'
CLASS_LIBERTY_ELITE = 'class_liberty_elite'
CLASS_LIBERTY_FIGHTER_ONLY = 'class_liberty_fighter_only'

CLASS_BRETONIA_INTERCEPTOR = 'class_bretonia_interceptor'
CLASS_BRETONIA_ELITE = 'class_bretonia_elite'
CLASS_BRETONIA_FIGHTER_ONLY = 'class_bretonia_fighter_only'

CLASS_KUSARI_INTERCEPTOR = 'class_kusari_interceptor'
CLASS_KUSARI_ELITE = 'class_kusari_elite'
CLASS_KUSARI_FIGHTER_ONLY = 'class_kusari_fighter_only'

CLASS_CORSAIR_INTERCEPTOR = 'class_corsair_interceptor'
CLASS_CORSAIR_ELITE = 'class_corsair_elite'
CLASS_CORSAIR_FIGHTER_ONLY = 'class_corsair_fighter_only'

CLASS_GENERIC_INTERCEPTOR = 'class_generic_interceptor'
CLASS_GENERIC_ELITE = 'class_generic_elite'
CLASS_GENERIC_FIGHTER_ONLY = 'class_generic_fighter_only'

HP_PCT_ENGINE_SINGLE = 0.5
HP_PCT_ENGINE_DOUBLE_SAME = 0.3
HP_PCT_ENGINE_DOUBLE_MAIN = 0.4
HP_PCT_ENGINE_DOUBLE_SECOND = 0.25
HP_PCT_ENGINE_TRIPLE_SAME = 0.3
HP_PCT_ENGINE_TRIPLE_MAIN = 0.4
HP_PCT_ENGINE_TRIPLE_SECONDARY = 0.25

HP_PCT_WING = 0.4
HP_PCT_TAIL = 0.5
HP_PCT_MISC = 0.25
HP_PCT_FIN = 0.25
HP_PCT_FIN_WITH_ENGINE = 0.4

EXPL_RESIST_ENGINE = 0.25
EXPL_RESIST_WING = 0.5
EXPL_RESIST_MISC = 1

SHIP_INDEX_1 = 1
SHIP_INDEX_2 = 2
SHIP_INDEX_3 = 3
SHIP_INDEX_4 = 4
SHIP_INDEX_5 = 5
SHIP_INDEX_6 = 6
SHIP_INDEX_7 = 7
SHIP_INDEX_8 = 8
SHIP_INDEX_9 = 9
SHIP_INDEX_10 = 10

SHIP_INDICES = [
    SHIP_INDEX_1,
    SHIP_INDEX_2,
    SHIP_INDEX_3,
    SHIP_INDEX_4,
    SHIP_INDEX_5,
    SHIP_INDEX_6,
    SHIP_INDEX_7,
    SHIP_INDEX_8,
    SHIP_INDEX_9,
    SHIP_INDEX_10,
]

PACKAGE_EQUIPMENT_PER_INDEX = {
    SHIP_INDEX_1: Equipment.CLASS_1,
    SHIP_INDEX_2: Equipment.CLASS_1,
    SHIP_INDEX_3: Equipment.CLASS_2,
    SHIP_INDEX_4: Equipment.CLASS_3,
    SHIP_INDEX_5: Equipment.CLASS_3,
    SHIP_INDEX_6: Equipment.CLASS_4,
    SHIP_INDEX_7: Equipment.CLASS_5,
    SHIP_INDEX_8: Equipment.CLASS_6,
    SHIP_INDEX_9: Equipment.CLASS_7,
    SHIP_INDEX_10: Equipment.CLASS_8,
}

EQUIPMENT_PER_INDEX = {
    SHIP_INDEX_1: Equipment.CLASS_2,
    SHIP_INDEX_2: Equipment.CLASS_3,
    SHIP_INDEX_3: Equipment.CLASS_4,
    SHIP_INDEX_4: Equipment.CLASS_5,
    SHIP_INDEX_5: Equipment.CLASS_5,
    SHIP_INDEX_6: Equipment.CLASS_6,
    SHIP_INDEX_7: Equipment.CLASS_7,
    SHIP_INDEX_8: Equipment.CLASS_8,
    SHIP_INDEX_9: Equipment.CLASS_9,
    SHIP_INDEX_10: Equipment.CLASS_10,
}

WEAPON_MAIN_CLASS_PER_INDEX = {
    SHIP_INDEX_1: Equipment.CLASS_1,
    SHIP_INDEX_2: Equipment.CLASS_2,
    SHIP_INDEX_3: Equipment.CLASS_2,
    SHIP_INDEX_4: Equipment.CLASS_3,
    SHIP_INDEX_5: Equipment.CLASS_4,
    SHIP_INDEX_6: Equipment.CLASS_5,
    SHIP_INDEX_7: Equipment.CLASS_6,
    SHIP_INDEX_8: Equipment.CLASS_7,
    SHIP_INDEX_9: Equipment.CLASS_8,
    SHIP_INDEX_10: Equipment.CLASS_9,
}

WEAPON_MAX_CLASS_PER_INDEX = {
    SHIP_INDEX_1: None,
    SHIP_INDEX_2: Equipment.CLASS_3,
    SHIP_INDEX_3: Equipment.CLASS_4,
    SHIP_INDEX_4: Equipment.CLASS_5,
    SHIP_INDEX_5: Equipment.CLASS_5,
    SHIP_INDEX_6: Equipment.CLASS_6,
    SHIP_INDEX_7: Equipment.CLASS_7,
    SHIP_INDEX_8: Equipment.CLASS_8,
    SHIP_INDEX_9: Equipment.CLASS_9,
    SHIP_INDEX_10: Equipment.CLASS_10,
}

BOT_REPAIR = 600
NUM_REPAIRS = 3

ARMOR_INDEX_1 = 1
ARMOR_INDEX_2 = 2
ARMOR_INDEX_3 = 3
ARMOR_INDEX_4 = 4
ARMOR_INDEX_5 = 5
ARMOR_INDEX_6 = 6
ARMOR_INDEX_7 = 7
ARMOR_INDEX_8 = 8
ARMOR_INDEX_9 = 9
ARMOR_INDEX_10 = 10
ARMOR_INDEX_11 = 11
ARMOR_INDEX_12 = 12
ARMOR_INDEX_13 = 13
ARMOR_INDEX_14 = 14
ARMOR_INDEX_15 = 15
ARMOR_INDEX_16 = 16
ARMOR_INDEX_17 = 17
ARMOR_INDEX_18 = 18
ARMOR_INDEX_19 = 19
ARMOR_INDEX_20 = 20
ARMOR_INDEX_21 = 21
ARMOR_INDEX_22 = 22
ARMOR_INDEX_23 = 23
ARMOR_INDEX_24 = 24
ARMOR_INDEX_25 = 25
ARMOR_INDEX_26 = 26
ARMOR_INDEX_27 = 27
ARMOR_INDEX_28 = 28
ARMOR_INDEX_29 = 29
ARMOR_INDEX_30 = 30

ENGINE_SINGLE = 1
ENGINE_DOUBLE_SAME = 2
ENGINE_DOUBLE_DIFF = 3
ENGINE_TRIPLE_SAME = 4

ENGINE_FORCE_PER_TYPE = {
    ENGINE_SINGLE: '''equip = single_eng_force, HpEngine01
equip = single_eng_weight, HpCockpit''',

    ENGINE_DOUBLE_SAME: '''equip = double_same_eng_force, HpEngine01
equip = double_same_eng_force, HpEngine02
equip = double_eng_weight, HpCockpit''',

    ENGINE_DOUBLE_DIFF: '''equip = double_diff_eng_force01, HpEngine01
equip = double_diff_eng_force02, HpEngine02
equip = double_eng_weight, HpCockpit''',

    ENGINE_TRIPLE_SAME: '''equip = triple_same_eng_force, HpEngine01
equip = triple_same_eng_force, HpEngine02
equip = triple_same_eng_force, HpEngine03
equip = triple_eng_weight, HpCockpit''',
}


class Ship(MarketShip):
    ARCHETYPE = None
    MISSILE_MOUNT_POINT = None
    EQUIP_TEMPLATE= '''
equip = {nickname}, {hardpoint}'''
    CARGO_TEMPLATE = '''
cargo = {nickname}, {amount}'''
    EXTRA_CLASSES = []
    HP_CM = 'HpCM01'
    HP_MINE = 'HpMine01'
    DEFAULTS = {
        'scanner': 'scanner_npc',
        'tractor': 'tractor01',
    }
    COLLISION_HIT_PTS_PERCENT = {}
    COLLISION_EXPLOSION_RESISTANCE = {}
    LIGHTS = 0
    RU_NAME = ''

    FORCE_HIT_PTS = None
    HIT_PTS_MULTIPLER_PER_INDEX = {
        SHIP_INDEX_1: 0.11,
        SHIP_INDEX_2: 0.13,
        SHIP_INDEX_3: 0.16,
        SHIP_INDEX_4: 0.20,
        SHIP_INDEX_5: 0.25,
        SHIP_INDEX_6: 0.30,
        SHIP_INDEX_7: 0.44,
        SHIP_INDEX_8: 0.60,
        SHIP_INDEX_9: 0.80,
        SHIP_INDEX_10: 1,
    }

    SHIELD_LINK = 'l_elite_shield01'
    ENGINE_TYPE = ENGINE_SINGLE
    ENG_FORCE_FEATURE = True

    SHIP_INDEX = SHIP_INDEX_1
    MAX_HIT_PTS = 10000
    HP_SHIELD = 'HpShield01'
    HP_ENGINE = 'HpDrive01'
    HP_POWERPLANT = 'HpPower01'
    SHIP_MASS = 100
    HOLD_SIZE = 10
    STRAFE_FORCE = 20000
    STRAFE_POWER_USAGE = 5
    NANOBOTS = 1

    CONTRAILS_COUNT = 4

    HULL_HIT_PTS_MULTIPLER = 1
    NANOBOTS_COUNT_MULTIPLER = 1
    SHIP_MASS_MULTIPLER = 1
    CARGO_HOLD_MULTIPLER = 1
    EXTRA_CARGO = 0
    STRAFE_FORCE_MULTIPLER = 1
    STRAFE_POWER_USAGE_MULTIPLER = 1

    DAMAGE_MINIMAL_PCT = 0.3
    DAMAGE_HEAVY_PCT = 0.2
    DAMAGE_CRITICAL_PCT = 0.1

    DAMAGE_FUSES = {
        'intermed_damage_smallship01': DAMAGE_MINIMAL_PCT,
        'intermed_damage_smallship02': DAMAGE_HEAVY_PCT,
        'intermed_damage_smallship03': DAMAGE_CRITICAL_PCT,
    }

    FUSE_TEMPLATE = 'fuse = {fuse}, 0.000000, {hit_pts}'

    HP_TYPE_TEMPLATE = 'hp_type = {hp_class}, {hardpoints}'
    GUN_CLASS_TEMPLATE = 'hp_gun_special_{class_digit}'
    TORPEDO_MAIN_CLASS = 'hp_torpedo_special_1'
    TORPEDO_CD_CLASS = 'hp_torpedo_special_2'
    TORPEDO_CLASSES = []

    THRUSTER_CLASS = 'hp_thruster'
    MINE_CLASS = 'hp_mine_dropper'
    CM_CLASS = 'hp_countermeasure_dropper'

    SHIELD_CLASS_TEMPLATE = None
    ENGINE_CLASS_TEMPLATE = None
    POWERPLANT_CLASS_TEMPLATE = None

    HAS_TORPEDO = False

    THRUSTERS = ['HpThruster01', 'HpThruster02']
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']

    def __init__(self, ids_name, ids_info, ids_info1, ids_info2, ids_info3):
        self.ids_name = ids_name
        self.ids_info = ids_info
        self.ids_info1 = ids_info1
        self.ids_info2 = ids_info2
        self.ids_info3 = ids_info3

    def get_ru_name(self):
        return self.RU_NAME

    BASE_LOADOUT = '''[Loadout]
{loadout}'''

    LOADOUT_TEMPLATE_BASE_COMPONENTS = [
        'nickname = {loadout_nickname}',
        'archetype = {ship_archetype}',
        'equip = {engine}',
        'equip = infinite_power',
        'cargo = {power}, 1',
        'equip = {scanner}',
        'equip = {tractor}',
        'equip = {armor}',
        'equip = {shield_npc}, HpShield01',
        'cargo = {shield}, 1',
        'equip = LargeWhiteSpecial, HpHeadlight',
        'equip = DockingLightRedSmall, HpDockLight01',
        'equip = DockingLightRedSmall, HpDockLight02',
    ]

    HAS_ANIMATION = True
    LOADOUT_LAUNCH_ANIMATION = 'equip = launch_extend'
    LOADOUT_LIGHT_TEMPLATE = 'equip = {{small_light}}, HpRunningLight{light_id}'
    LOADOUT_CONTRAIL_TEMPLATE = 'equip = {{contrail}}, HpContrail{contrail_id}'
    LOADOUT_THRUSTER_TEMPLATE = 'equip = {{afterburn{thruster_index}}}, {hp_thruster}'
    LOADOUT_WEAPON_TEMPLATE = 'equip = {{weapon{weapon_index}}}, {hp_weapon}'

    HP_HEADLIGHT = 'HpHeadlight'
    PACKAGE_LAUNCH_ANIMATION = 'addon = launch_extend, internal, 1'
    PACKAGE_LIGHT_TEMPLATE = 'equip = {{small_light}}, HpRunningLight{light_id}, 1'
    PACKAGE_CONTRAIL_TEMPLATE = 'equip = player_contrail, HpContrail{contrail_id}, 1'

    def get_loadout_components(self):
        components = []
        components.extend(self.LOADOUT_TEMPLATE_BASE_COMPONENTS)

        if self.HAS_ANIMATION:
            components.append(self.LOADOUT_LAUNCH_ANIMATION)

        i = 1
        for hp_weapon in self.MAIN_WEAPONS:
            components.append(self.LOADOUT_WEAPON_TEMPLATE.format(weapon_index=i, hp_weapon=hp_weapon))
            i += 1

        i = 1
        for hp_thruster in self.THRUSTERS:
            components.append(self.LOADOUT_THRUSTER_TEMPLATE.format(thruster_index=i, hp_thruster=hp_thruster))
            i += 1

        for i in range(1, self.CONTRAILS_COUNT + 1):
            components.append(self.LOADOUT_CONTRAIL_TEMPLATE.format(contrail_id=f'0{i}'))

        for i in range(1, self.LIGHTS + 1):
            components.append(self.LOADOUT_LIGHT_TEMPLATE.format(light_id=f'0{i}'))

        if self.ENG_FORCE_FEATURE:
            components.append(ENGINE_FORCE_PER_TYPE[self.ENGINE_TYPE])

        return components

    def get_loadout_template(self):
        return self.BASE_LOADOUT.format(loadout=SINGLE_DIVIDER.join(self.get_loadout_components()))

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    def get_package_nickname(self):
        return '{archetype}_package'.format(archetype=self.ARCHETYPE)

    def get_nickname(self):
        return self.get_package_nickname()

    def get_hull_nickname(self):
        return '{archetype}_hull'.format(archetype=self.ARCHETYPE)

    PACKAGE_BASE_TEMPLATE = '''[Good]
nickname = {package_nickname}
category = ship
hull = {hull_nickname}
addon = LargeWhiteSpecialPlayer, {hp_headlight}, 1
addon = DockingLightRedSmall, HpDockLight01, 1
addon = DockingLightRedSmall, HpDockLight02, 1
addon = scanner01, internal, 1
addon = tractor01, internal, 1
addon = {shield}, {hp_shield}, 1
addon = {engine}, HpDrive01, 1
addon = {power}, HpPower01, 1'''

    def get_package_extra_template(self):
        components = []

        if self.HAS_ANIMATION:
            components.append(self.PACKAGE_LAUNCH_ANIMATION)

        for i in range(1, self.CONTRAILS_COUNT + 1):
            components.append(self.PACKAGE_CONTRAIL_TEMPLATE.format(contrail_id=f'0{i}'))

        for i in range(1, self.LIGHTS + 1):
            components.append(self.PACKAGE_LIGHT_TEMPLATE.format(light_id=f'0{i}'))

        return SINGLE_DIVIDER.join(components)

    def get_package_equipment_class(self):
        return PACKAGE_EQUIPMENT_PER_INDEX[self.SHIP_INDEX]

    def get_package(self, shield, engine, power, small_light):
        extra_content = self.get_package_extra_template()
        template = self.PACKAGE_BASE_TEMPLATE + SINGLE_DIVIDER + extra_content
        return template.format(
            package_nickname=self.get_package_nickname(),
            hull_nickname=self.get_hull_nickname(),
            hp_headlight=self.HP_HEADLIGHT,
            hp_shield=self.HP_SHIELD,
            shield=shield,
            engine=engine,
            power=power,
            small_light=small_light
        )

    HULL_BASE_TEMPLATE = '''[Good]
nickname = {hull_nickname}
category = shiphull
ship = {ship_archetype}
price = {price}
item_icon = Equipment\\models\\commodities\\nn_icons\\{icon}'''

    MAX_PRICE = None  # must redefine

    PRICE_PER_INDEX = {
        SHIP_INDEX_2: 0.012,
        SHIP_INDEX_3: 0.015,
        SHIP_INDEX_4: 0.03,
        SHIP_INDEX_5: 0.05,
        SHIP_INDEX_6: 0.1,
        SHIP_INDEX_7: 0.25,
        SHIP_INDEX_8: 0.6,
        SHIP_INDEX_9: 0.78,
        SHIP_INDEX_10: 1,
    }
    
    def get_ship_price(self):
        return self.MAX_PRICE * self.PRICE_PER_INDEX[self.SHIP_INDEX]

    def get_hull(self):
        return self.HULL_BASE_TEMPLATE.format(
            hull_nickname=self.get_hull_nickname(),
            ship_archetype=self.ARCHETYPE,
            price=self.get_ship_price(),
            icon=self.ICON,
        )

    CARGO_PER_INDEX = {}

    ARMOR_INDICES = {
        ARMOR_INDEX_1: 0.42,
        ARMOR_INDEX_2: 0.47,
        ARMOR_INDEX_3: 0.5,
        ARMOR_INDEX_4: 0.55,
        ARMOR_INDEX_5: 0.6,
        ARMOR_INDEX_6: 0.68,
        ARMOR_INDEX_7: 0.75,
        ARMOR_INDEX_8: 0.83,
        ARMOR_INDEX_9: 0.92,
        ARMOR_INDEX_10: 1,
        ARMOR_INDEX_11: 1.1,
        ARMOR_INDEX_12: 1.2,
        ARMOR_INDEX_13: 1.5,
        ARMOR_INDEX_14: 1.8,
        ARMOR_INDEX_15: 2,
        ARMOR_INDEX_16: 2.4,
        ARMOR_INDEX_17: 3,
        ARMOR_INDEX_18: 3.5,
        ARMOR_INDEX_19: 4,
        ARMOR_INDEX_20: 4.5,
        ARMOR_INDEX_21: 5,
        ARMOR_INDEX_22: 6,
        ARMOR_INDEX_23: 7.5,
        ARMOR_INDEX_24: 9,
        ARMOR_INDEX_25: 12,
        ARMOR_INDEX_26: 15,
        ARMOR_INDEX_27: 20,
        ARMOR_INDEX_28: 30,
    }

    START_ARMOR_INDEX_PER_SHIP_INDEX = {
        SHIP_INDEX_1: ARMOR_INDEX_10,
        SHIP_INDEX_2: ARMOR_INDEX_10,
        SHIP_INDEX_3: ARMOR_INDEX_9,
        SHIP_INDEX_4: ARMOR_INDEX_9,
        SHIP_INDEX_5: ARMOR_INDEX_8,
        SHIP_INDEX_6: ARMOR_INDEX_7,
        SHIP_INDEX_7: ARMOR_INDEX_6,
        SHIP_INDEX_8: ARMOR_INDEX_5,
        SHIP_INDEX_9: ARMOR_INDEX_4,
        SHIP_INDEX_10: ARMOR_INDEX_3,
    }

    def get_equipment_level(self):
        return EQUIPMENT_PER_INDEX[self.SHIP_INDEX]

    def get_main_weapon_class(self):
        return WEAPON_MAIN_CLASS_PER_INDEX[self.SHIP_INDEX]

    def get_max_weapon_class(self):
        return WEAPON_MAX_CLASS_PER_INDEX[self.SHIP_INDEX]

    def get_fuses(self):
        lines = []
        for fuse, hit_pts_pct in self.DAMAGE_FUSES.items():
            lines.append(self.FUSE_TEMPLATE.format(
                fuse=fuse,
                hit_pts=self.get_hit_pts()*hit_pts_pct,
            ))
        return SINGLE_DIVIDER.join(lines)

    def build_equip_line(self, hp_class, hardpoints):
        return self.HP_TYPE_TEMPLATE.format(
            hp_class=hp_class,
            hardpoints=hardpoints,
        )

    def build_weapon_equip_line(self, equipment_class, hardpoints):
        return self.HP_TYPE_TEMPLATE.format(
            hp_class=self.GUN_CLASS_TEMPLATE.format(class_digit=equipment_class),
            hardpoints=hardpoints,
        )

    def build_torpedo_equip_line(self, hp_class):
        return self.HP_TYPE_TEMPLATE.format(hp_class=hp_class, hardpoints=self.HP_TORPEDO)

    def build_shield_equip_line(self, equipment_class):
        return self.HP_TYPE_TEMPLATE.format(
            hp_class=self.SHIELD_CLASS_TEMPLATE.format(class_digit=equipment_class), 
            hardpoints=self.HP_SHIELD,
        )

    def build_engine_equip_line(self, equipment_class):
        return self.HP_TYPE_TEMPLATE.format(
            hp_class=self.ENGINE_CLASS_TEMPLATE.format(class_digit=equipment_class), 
            hardpoints=self.HP_ENGINE,
        )

    def build_powerplant_equip_line(self, equipment_class):
        return self.HP_TYPE_TEMPLATE.format(
            hp_class=self.POWERPLANT_CLASS_TEMPLATE.format(class_digit=equipment_class), 
            hardpoints=self.HP_POWERPLANT,
        )

    def get_weapon_lines(self):
        lines = []

        equipment_level = self.get_equipment_level()
        max_class = self.get_max_weapon_class()
        main_class = self.get_main_weapon_class()

        for equipment_class in Equipment.BASE_CLASSES:
            if equipment_class > equipment_level:
                break
            elif equipment_class == equipment_level and max_class is not None:
                lines.append(self.build_weapon_equip_line(equipment_class, ', '.join(self.MAX_WEAPONS)))
            else:
                lines.append(self.build_weapon_equip_line(equipment_class, ', '.join(self.MAIN_WEAPONS)))

        return lines

    def get_torpedo_lines(self):
        lines = []

        for torpedo_item in self.TORPEDO_CLASSES:
            lines.append(self.build_torpedo_equip_line(torpedo_item))

        return lines

    def get_misc_equip_lines(self):
        lines = []

        for equipment_class in Equipment.BASE_CLASSES:
            if equipment_class > self.get_equipment_level():
                break
            else:
                lines.append(self.build_shield_equip_line(equipment_class))

        for equipment_class in Equipment.BASE_CLASSES:
            if equipment_class > self.get_equipment_level():
                break
            else:
                lines.append(self.build_engine_equip_line(equipment_class))

        for equipment_class in Equipment.BASE_CLASSES:
            if equipment_class > self.get_equipment_level():
                break
            else:
                lines.append(self.build_powerplant_equip_line(equipment_class))

        return lines

    def get_generic_equip_lines(self):
        lines = []

        if self.THRUSTERS:
            lines.append(self.build_equip_line(self.THRUSTER_CLASS, ', '.join(self.THRUSTERS)))

        lines.append(self.build_equip_line(self.MINE_CLASS, self.HP_MINE))
        lines.append(self.build_equip_line(self.CM_CLASS, self.HP_CM))

        return lines

    def get_equipment_table(self):
        lines = self.get_weapon_lines() + self.get_torpedo_lines() + self.get_misc_equip_lines() + self.get_generic_equip_lines()
        return SINGLE_DIVIDER.join(lines)

    def ship_param(self, param):
        return '{ship_code}_{param}'.format(
            ship_code=self.TEMPLATE_CODE,
            param=param,
        )

    def get_ship_mass(self):
        return math.ceil(self.SHIP_MASS * self.SHIP_MASS_MULTIPLER)

    def get_hold_size(self):
        return math.ceil((self.CARGO_PER_INDEX[self.SHIP_INDEX] * self.CARGO_HOLD_MULTIPLER) + self.EXTRA_CARGO)

    def get_strafe_force(self):
        return math.ceil(self.STRAFE_FORCE * self.STRAFE_FORCE_MULTIPLER)

    def get_strafe_force_power_usage(self):
        return math.ceil(self.STRAFE_POWER_USAGE * self.STRAFE_POWER_USAGE_MULTIPLER)

    def get_hit_pts(self):
        if self.FORCE_HIT_PTS:
            return self.FORCE_HIT_PTS
        return math.ceil(self.MAX_HIT_PTS * self.HIT_PTS_MULTIPLER_PER_INDEX[self.SHIP_INDEX] * self.HULL_HIT_PTS_MULTIPLER)

    def get_bots_count(self):
        return math.ceil(((self.get_hit_pts() * NUM_REPAIRS) / BOT_REPAIR) * self.NANOBOTS_COUNT_MULTIPLER)

    PARAMS_TEMPLATE = '''nickname = {shiparch_name}
ids_name = {ids_name}
ids_info = {ids_info}
ids_info1 = {ids_info1}
ids_info2 = {ids_info2}
ids_info3 = {ids_info3}
shield_link = {shield_link_object}, HpMount, {shield_link_hp}
mass = {mass}
hold_size = {hold_size}
strafe_force = {strafe_force}
strafe_power_usage = {strafe_power_usage}
nanobot_limit = {nanobot}
shield_battery_limit = {nanobot}
hit_pts = {hit_pts}
{fuses}
{equipment}'''

    def get_base_template_params(self):
        return {
            'shiparch_name': self.ARCHETYPE,
            'ids_name': self.ids_name,
            'ids_info': self.ids_info,
            'ids_info1': self.ids_info1,
            'ids_info2': self.ids_info2,
            'ids_info3': self.ids_info3,
            'shield_link_object': self.SHIELD_LINK,
            'shield_link_hp': self.HP_SHIELD,
            'mass': self.get_ship_mass(),
            'hold_size': self.get_hold_size(),
            'strafe_force': self.get_strafe_force(),
            'strafe_power_usage': self.get_strafe_force_power_usage(),
            'nanobot': self.get_bots_count(),
            'hit_pts': self.get_hit_pts(),
            'fuses': self.get_fuses(),
            'equipment': self.get_equipment_table(),
        }

    ADDITIONAL_EQUIP = ''

    def get_infocard_values(self):
        return {
            'value_gun_count': len(self.MAIN_WEAPONS),
            'value_armor': int(self.get_hit_pts()),
            'value_mass': int(self.get_ship_mass()),
            'value_cargo': int(self.get_hold_size()),
            'value_bot_bats': int(self.get_bots_count()),
            'value_max_equip_class': self.get_max_weapon_class(),
            'value_max_weapon_class': self.get_max_weapon_class(),
            'value_additional_equipment': self.ADDITIONAL_EQUIP,
        }

    def get_collision_group_template_params(self):
        params = {}

        for name, hit_pts_pct in self.COLLISION_HIT_PTS_PERCENT.items():
            params[self.ship_param(name)] = self.get_hit_pts() * hit_pts_pct

        for name, resistance in self.COLLISION_EXPLOSION_RESISTANCE.items():
            params[self.ship_param(name)] = resistance

        return params

    def get_main_param_name(self):
        return 'ship_{shiparch_name}'.format(shiparch_name=self.ARCHETYPE)

    def get_shiparch_params(self):
        params = {
            self.get_main_param_name(): self.PARAMS_TEMPLATE.format(**self.get_base_template_params())
        }
        params.update(self.get_collision_group_template_params())
        return params

    @staticmethod
    def get_extra_items(torpedo, cm, mine, torpedo_ammo, cm_ammo, mine_ammo):
        extra = []
        if torpedo:
            extra.append(Ship.EQUIP_TEMPLATE.format(torpedo, Ship.HP_TORPEDO))
            if torpedo_ammo:
                extra.append(Ship.CARGO_TEMPLATE.format(torpedo, torpedo_ammo))

        if cm:
            extra.append(Ship.EQUIP_TEMPLATE.format(cm, Ship.HP_CM))
            if cm_ammo:
                extra.append(Ship.CARGO_TEMPLATE.format(torpedo, cm_ammo))

        if mine:
            extra.append(Ship.EQUIP_TEMPLATE.format(mine, Ship.HP_MINE))
            if mine_ammo:
                extra.append(Ship.CARGO_TEMPLATE.format(torpedo, mine_ammo))

        return extra


class BaseInterceptorShip(object):
    MAX_HIT_PTS = 12000

    MAX_PRICE = 500000

    ADDITIONAL_EQUIP = 'M, CM, CD'

    CARGO_PER_INDEX = {
        SHIP_INDEX_1: 20,
        SHIP_INDEX_2: 25,
        SHIP_INDEX_3: 30,
        SHIP_INDEX_4: 35,
        SHIP_INDEX_5: 40,
        SHIP_INDEX_6: 45,
        SHIP_INDEX_7: 50,
        SHIP_INDEX_8: 55,
        SHIP_INDEX_9: 60,
        SHIP_INDEX_10: 65,
    }


class BaseFighterShip(object):
    MAX_HIT_PTS = 10000

    MAX_PRICE = 650000

    ADDITIONAL_EQUIP = 'M, CM, CD/T'

    CARGO_PER_INDEX = {
        SHIP_INDEX_1: 25,
        SHIP_INDEX_2: 30,
        SHIP_INDEX_3: 35,
        SHIP_INDEX_4: 40,
        SHIP_INDEX_5: 45,
        SHIP_INDEX_6: 50,
        SHIP_INDEX_7: 55,
        SHIP_INDEX_8: 60,
        SHIP_INDEX_9: 65,
        SHIP_INDEX_10: 70,
    }


class BaseFreighterShip(object):
    MAX_HIT_PTS = 14000

    ADDITIONAL_EQUIP = 'M, CM'

    MAX_PRICE = 800000

    CARGO_PER_INDEX = {
        SHIP_INDEX_1: 60,
        SHIP_INDEX_2: 80,
        SHIP_INDEX_3: 100,
        SHIP_INDEX_4: 130,
        SHIP_INDEX_5: 160,
        SHIP_INDEX_6: 200,
        SHIP_INDEX_7: 250,
        SHIP_INDEX_8: 300,
        SHIP_INDEX_9: 350,
        SHIP_INDEX_10: 500,
    }


class RheinlandShip(object):
    # MAIN
    SHIP_MASS_MULTIPLER = 0.66
    CARGO_HOLD_MULTIPLER = 0.84
    EXTRA_CARGO = -3
    # ADDITIONAL
    HULL_HIT_PTS_MULTIPLER = 1.02
    STRAFE_FORCE_MULTIPLER = 0.9

    PACKAGE_EQUIPMENT_TYPE = MainMiscEquip.RH_CIV
    PACKAGE_LIGHT = Light.SMALL_YELLOW


class LibertyShip(object):
    # MAIN
    HULL_HIT_PTS_MULTIPLER = 0.83
    # ADDITIONAL
    STRAFE_POWER_USAGE_MULTIPLER = 1.5
    NANOBOTS_COUNT_MULTIPLER = 1.1

    PACKAGE_EQUIPMENT_TYPE = MainMiscEquip.LI_CIV
    PACKAGE_LIGHT = Light.SMALL_BLUE


class BretoniaShip(object):
    # MAIN
    HULL_HIT_PTS_MULTIPLER = 1.15
    # ADDITIONAL
    EXTRA_CARGO = 2
    STRAFE_FORCE_MULTIPLER = 0.95
    SHIP_MASS_MULTIPLER = 1.1

    PACKAGE_EQUIPMENT_TYPE = MainMiscEquip.BR_CIV
    PACKAGE_LIGHT = Light.SMALL_RED


class KusariShip(object):
    # MAIN
    NANOBOTS_COUNT_MULTIPLER = 1.5
    STRAFE_FORCE_MULTIPLER = 0.5
    STRAFE_POWER_USAGE_MULTIPLER = 0
    # ADDITIONAL
    HULL_HIT_PTS_MULTIPLER = 0.95
    EXTRA_CARGO = -1

    PACKAGE_EQUIPMENT_TYPE = MainMiscEquip.KU_CIV
    PACKAGE_LIGHT = Light.SMALL_ORANGE


class CorsairShip(object):
    # MAIN
    CARGO_HOLD_MULTIPLER = 1.1
    NANOBOTS_COUNT_MULTIPLER = 0.5
    # ADDITIONAL
    HULL_HIT_PTS_MULTIPLER = 1.06

    PACKAGE_EQUIPMENT_TYPE = MainMiscEquip.CO_CORSAIR
    PACKAGE_LIGHT = Light.SMALL_PURPLE


class GenericShip(object):
    # MAIN
    HULL_HIT_PTS_MULTIPLER = 0.92
    # ADDITIONAL
    EXTRA_CARGO = -1
    STRAFE_POWER_USAGE_MULTIPLER = 1.1
    SHIP_MASS_MULTIPLER = 1.05

    PACKAGE_EQUIPMENT_TYPE = MainMiscEquip.RH_CIV
    PACKAGE_LIGHT = Light.SMALL_YELLOW


class Ship1(object):
    NPC_LEVELS = NPC.SHIP1_LEVELS


class Ship2(object):
    NPC_LEVELS = NPC.SHIP2_LEVELS


class Ship3(object):
    NPC_LEVELS = NPC.SHIP3_LEVELS


class ShipInterceptor(BaseInterceptorShip):
    SHIPCLASS_NAME = 'interceptor'
    HAS_TORPEDO = True
    EQUIPMENT_SHIPCLASS = Equipment.SHIPCLASS_FIGHTER
    EXTRA_CLASSES = [CLASS_INTERCEPTOR]
    TORPEDO_CLASSES = [Ship.TORPEDO_CD_CLASS]

    SHIELD_CLASS_TEMPLATE = 'hp_fighter_shield_special_{class_digit}'
    ENGINE_CLASS_TEMPLATE = 'hp_fighter_engine_special_{class_digit}'
    POWERPLANT_CLASS_TEMPLATE = 'hp_fighter_power_special_{class_digit}'


class ShipFighter(BaseFighterShip):
    SHIPCLASS_NAME = 'fighter'
    HAS_TORPEDO = True
    EQUIPMENT_SHIPCLASS = Equipment.SHIPCLASS_ELITE
    EXTRA_CLASSES = [CLASS_ELITE]
    TORPEDO_CLASSES = [Ship.TORPEDO_MAIN_CLASS, Ship.TORPEDO_CD_CLASS]

    SHIELD_CLASS_TEMPLATE = 'hp_elite_shield_special_{class_digit}'
    ENGINE_CLASS_TEMPLATE = 'hp_elite_engine_special_{class_digit}'
    POWERPLANT_CLASS_TEMPLATE = 'hp_elite_power_special_{class_digit}'


class ShipElite(ShipFighter):
    SHIPCLASS_NAME = 'elite'


class ShipFreighter(BaseFreighterShip):
    EQUIPMENT_SHIPCLASS = Equipment.SHIPCLASS_FREIGHTER
    SHIPCLASS_NAME = 'freighter'
    EXTRA_CLASSES = []

    SHIELD_CLASS_TEMPLATE = 'hp_freighter_shield_special_{class_digit}'
    ENGINE_CLASS_TEMPLATE = 'hp_freighter_engine_special_{class_digit}'
    POWERPLANT_CLASS_TEMPLATE = 'hp_freighter_power_special_{class_digit}'


# RHEINLAND


class Dagger(RheinlandShip, ShipInterceptor, Ship1, Ship):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_RHEINLAND_INTERCEPTOR]
    SHIP_INDEX = SHIP_INDEX_3
    SHIELD_LINK = 'bw_fighter_shield01'
    ENGINE_TYPE = ENGINE_SINGLE
    LIGHTS = 8
    EXCLUDED_LIGHTS = [6, 7]

    ARCHETYPE = 'bw_fighter'
    RU_NAME = 'Кинжал'
    TEMPLATE_CODE = 'bwf'
    ICON = 'bw_fighter.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02']

    # mk2 
    # HP_TORPEDO = 'HpTorpedo01'
    # MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04, HpTurret01']
    # MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02, HpTurret01']

    COLLISION_HIT_PTS_PERCENT = {
        'wing_hit_pts': HP_PCT_WING,
        'engine_hit_pts': HP_PCT_ENGINE_SINGLE,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'wing_expl_resist': EXPL_RESIST_WING,
        'engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Banshee(RheinlandShip, ShipInterceptor, Ship2, Ship):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_RHEINLAND_INTERCEPTOR]
    SHIP_INDEX = SHIP_INDEX_7
    SHIELD_LINK = 'r_fighter_shield01'
    ENGINE_TYPE = ENGINE_SINGLE
    LIGHTS = 6

    ARCHETYPE = 'rh_fighter'
    RU_NAME = 'Баньши'
    TEMPLATE_CODE = 'rf'
    ICON = 'rh_fighter.3db'
    HP_TORPEDO = 'HpTorpedo02'
    MAIN_WEAPONS = ['HpTorpedo01', 'HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']
    MAX_WEAPONS = ['HpTorpedo01', 'HpWeapon03', 'HpWeapon04']

    COLLISION_HIT_PTS_PERCENT = {
        'wing_hit_pts': HP_PCT_WING,
        'engine_hit_pts': HP_PCT_ENGINE_SINGLE, 
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'wing_expl_resist': EXPL_RESIST_WING,
        'engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Stiletto(RheinlandShip, ShipFighter, Ship1, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_RHEINLAND_ELITE, CLASS_RHEINLAND_FIGHTER_ONLY]
    SHIP_INDEX = SHIP_INDEX_3
    SHIELD_LINK = 'bw_elite_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 6

    ARCHETYPE = 'bw_elite'
    RU_NAME = 'Стилет'
    TEMPLATE_CODE = 'bwe'
    ICON = 'bw_elite.3db'
    HP_TORPEDO = 'HpWeapon06'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03']

    # mk2: minds??

    # HP_TORPEDO = 'HpTorpedo01'
    # MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    # MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']

    COLLISION_HIT_PTS_PERCENT = {
        'wing1_hit_pts': HP_PCT_WING,
        'wing2_hit_pts': HP_PCT_WING,
        'engine1_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
        'engine2_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'wing1_expl_resist': EXPL_RESIST_WING,
        'wing2_expl_resist': EXPL_RESIST_WING,
        'engine1_expl_resist': EXPL_RESIST_ENGINE,
        'engine2_expl_resist': EXPL_RESIST_ENGINE,
    }


class Sabre(RheinlandShip, ShipFighter, Ship2, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_RHEINLAND_ELITE, CLASS_RHEINLAND_FIGHTER_ONLY]
    SHIP_INDEX = SHIP_INDEX_7
    SHIELD_LINK = 'bw_vheavy_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 8

    ARCHETYPE = 'bw_elite2'
    RU_NAME = 'Сабля'
    TEMPLATE_CODE = 'bwe2'
    ICON = 'bw_heavy.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']

    COLLISION_HIT_PTS_PERCENT = {
        'wing1_hit_pts': HP_PCT_WING,
        'wing2_hit_pts': HP_PCT_WING,
        'engine1_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
        'engine2_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'wing1_expl_resist': EXPL_RESIST_WING,
        'wing2_expl_resist': EXPL_RESIST_WING,
        'engine1_expl_resist': EXPL_RESIST_ENGINE,
        'engine2_expl_resist': EXPL_RESIST_ENGINE,
    }


class Valkyrie(RheinlandShip, ShipElite, Ship3, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_RHEINLAND_ELITE]
    SHIP_INDEX = SHIP_INDEX_8
    SHIELD_LINK = 'r_elite_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 6

    ARCHETYPE = 'rh_elite'
    RU_NAME = 'Валькирия'
    TEMPLATE_CODE = 're'
    ICON = 'rh_elite.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    MAX_WEAPONS = ['HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']

    COLLISION_HIT_PTS_PERCENT = {
        'wing_hit_pts': HP_PCT_WING,
        'tail_hit_pts': HP_PCT_TAIL,
        'engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'wing_expl_resist': EXPL_RESIST_WING,
        'tail_expl_resist': EXPL_RESIST_WING,
        'engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class ValkyrieMk2(RheinlandShip, ShipElite, Ship3, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_RHEINLAND_ELITE]
    SHIP_INDEX = SHIP_INDEX_10
    LIGHTS = 6

    ARCHETYPE = 'rh_elite2'
    RU_NAME = 'Валькирия Мк.II'
    TEMPLATE_CODE = 're2'
    ICON = 'rh_elite.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    MAX_WEAPONS = ['HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']

    COLLISION_HIT_PTS_PERCENT = {
        'wing_hit_pts': HP_PCT_WING,
        'tail_hit_pts': HP_PCT_TAIL,
        'engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'wing_expl_resist': EXPL_RESIST_WING,
        'tail_expl_resist': EXPL_RESIST_WING,
        'engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Humpback(RheinlandShip, ShipFreighter, Ship):
    ARCHETYPE = 'rh_freighter'
    RU_NAME = 'Горбун'
    SHIELD_LINK = 'r_freighter_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    SHIP_INDEX = SHIP_INDEX_6
    LIGHTS = 7

    TEMPLATE_CODE = 'rfr'
    ICON = 'rh_freighter.3db'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon05', 'HpWeapon06', 'HpWeapon10']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon05', 'HpWeapon06']

    COLLISION_HIT_PTS_PERCENT = {
        'panel_hit_pts': HP_PCT_WING,
        'engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'panel_expl_resist': EXPL_RESIST_WING,
        'engine_expl_resist': EXPL_RESIST_ENGINE,
    }


# LIBERTY


class Piranha(LibertyShip, ShipInterceptor, Ship1, Ship):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_LIBERTY_INTERCEPTOR]
    SHIP_INDEX = SHIP_INDEX_3
    SHIELD_LINK = 'bh_fighter_shield01'
    ENGINE_TYPE = ENGINE_SINGLE
    LIGHTS = 6

    ARCHETYPE = 'bh_fighter'
    RU_NAME = 'Пиранья'
    TEMPLATE_CODE = 'bhf'
    ICON = 'bh_fighter.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']
    MAX_WEAPONS = ['HpWeapon03', 'HpWeapon04']

    COLLISION_HIT_PTS_PERCENT = {
        'fin_hit_pts': HP_PCT_FIN,
        'engine_hit_pts': HP_PCT_ENGINE_SINGLE,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'fin_expl_resist': EXPL_RESIST_MISC,
        'engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Patriot(LibertyShip, ShipInterceptor, Ship2, Ship):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_LIBERTY_INTERCEPTOR]
    SHIP_INDEX = SHIP_INDEX_7
    LIGHTS = 4

    ARCHETYPE = 'li_fighter'
    RU_NAME = 'Патриот'
    SHIELD_LINK = 'l_fighter_shield01'
    ENGINE_TYPE = ENGINE_SINGLE
    TEMPLATE_CODE = 'lf'
    ICON = 'li_fighter.3db'
    HP_TORPEDO = 'HpTorpedo02'
    MAIN_WEAPONS = ['HpTorpedo01', 'HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']
    MAX_WEAPONS = ['HpWeapon03', 'HpWeapon04']

    COLLISION_HIT_PTS_PERCENT = {
        'fin_hit_pts': HP_PCT_FIN,
        'engine_hit_pts': HP_PCT_ENGINE_SINGLE,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'fin_expl_resist': EXPL_RESIST_MISC,  
        'engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Barracuda(LibertyShip, ShipFighter, Ship1, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_LIBERTY_ELITE, CLASS_LIBERTY_FIGHTER_ONLY]
    SHIP_INDEX = SHIP_INDEX_3
    SHIELD_LINK = 'bh_elite_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 6

    ARCHETYPE = 'bh_elite'
    RU_NAME = 'Барракуда'
    TEMPLATE_CODE = 'bhe'
    ICON = 'bh_elite.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05']
    MAX_WEAPONS = ['HpWeapon03', 'HpWeapon04', 'HpWeapon05']

    # mk 2
    # HP_TORPEDO = 'HpTorpedo02'
    # MAIN_WEAPONS = ['HpTorpedo01', 'HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05']
    # MAX_WEAPONS = ['HpTorpedo01', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05']

    COLLISION_HIT_PTS_PERCENT = {
        'fin1_hit_pts': HP_PCT_FIN,
        'fin2_hit_pts': HP_PCT_FIN_WITH_ENGINE,
        'wing_hit_pts': HP_PCT_WING,
        'engine1_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
        'engine2_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'fin1_expl_resist': EXPL_RESIST_MISC,
        'fin2_expl_resist': EXPL_RESIST_MISC,
        'wing_expl_resist': EXPL_RESIST_WING,
        'engine1_expl_resist': EXPL_RESIST_ENGINE,
        'engine2_expl_resist': EXPL_RESIST_ENGINE,
    }


class Hammerhead(LibertyShip, ShipFighter, Ship2, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_LIBERTY_ELITE, CLASS_LIBERTY_FIGHTER_ONLY]
    SHIP_INDEX = SHIP_INDEX_7
    SHIELD_LINK = 'bh_elite_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 6

    ARCHETYPE = 'bh_elite2'
    RU_NAME = 'Молот'
    TEMPLATE_CODE = 'bhe2'
    ICON = 'bh_heavy.3db'
    HP_TORPEDO = 'HpWeapon06'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon07']
    MAX_WEAPONS = ['HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon07']

    COLLISION_HIT_PTS_PERCENT = {
        'fin1_hit_pts': HP_PCT_FIN,
        'fin2_hit_pts': HP_PCT_FIN_WITH_ENGINE,
        'wing_hit_pts': HP_PCT_WING,
        'engine1_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
        'engine2_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'fin1_expl_resist': EXPL_RESIST_MISC,
        'fin2_expl_resist': EXPL_RESIST_MISC,
        'wing_expl_resist': EXPL_RESIST_WING,
        'engine1_expl_resist': EXPL_RESIST_ENGINE,
        'engine2_expl_resist': EXPL_RESIST_ENGINE,
    }


class Defender(LibertyShip, ShipElite, Ship3, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_LIBERTY_ELITE]
    SHIP_INDEX = SHIP_INDEX_8
    SHIELD_LINK = 'l_elite_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_DIFF
    LIGHTS = 4

    ARCHETYPE = 'li_elite'
    RU_NAME = 'Защитник'
    TEMPLATE_CODE = 'le'
    ICON = 'li_elite.3db'
    HP_TORPEDO = 'HpTorpedo02'
    MAIN_WEAPONS = ['HpTorpedo01', 'HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05']
    MAX_WEAPONS = ['HpTorpedo01', 'HpWeapon03', 'HpWeapon04']

    COLLISION_HIT_PTS_PERCENT = {
        'wing_hit_pts': HP_PCT_WING,
        'spoiler_hit_pts': HP_PCT_TAIL,
        'engine1_hit_pts': HP_PCT_ENGINE_DOUBLE_MAIN,
        'engine2_hit_pts': HP_PCT_ENGINE_DOUBLE_SECOND,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'wing_expl_resist': EXPL_RESIST_WING,
        'spoiler_expl_resist': EXPL_RESIST_WING,
        'engine1_expl_resist': EXPL_RESIST_ENGINE,
        'engine2_expl_resist': EXPL_RESIST_ENGINE,
    }


class DefenderJuni(LibertyShip, ShipElite, Ship3, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_LIBERTY_ELITE]
    SHIP_INDEX = SHIP_INDEX_10
    SHIELD_LINK = 'l_elite2_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_DIFF
    LIGHTS = 4

    ARCHETYPE = 'li_elite2'
    RU_NAME = 'Рейнджер'
    TEMPLATE_CODE = 'le2'
    ICON = 'li_elite.3db'
    HP_TORPEDO = 'HpTorpedo02'
    MAIN_WEAPONS = ['HpTorpedo01', 'HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05']
    MAX_WEAPONS = ['HpTorpedo01', 'HpWeapon03', 'HpWeapon04']

    COLLISION_HIT_PTS_PERCENT = {
        'wing_hit_pts': HP_PCT_WING,
        'spoiler_hit_pts': HP_PCT_TAIL,
        'engine1_hit_pts': HP_PCT_ENGINE_DOUBLE_MAIN,
        'engine2_hit_pts': HP_PCT_ENGINE_DOUBLE_SECOND,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'wing_expl_resist': EXPL_RESIST_WING,
        'spoiler_expl_resist': EXPL_RESIST_WING,
        'engine1_expl_resist': EXPL_RESIST_ENGINE,
        'engine2_expl_resist': EXPL_RESIST_ENGINE,
    }


class Rhino(LibertyShip, ShipFreighter, Ship):
    ARCHETYPE = 'li_freighter'
    RU_NAME = 'Носорог'
    SHIP_INDEX = SHIP_INDEX_6
    SHIELD_LINK = 'l_freighter_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 7

    TEMPLATE_CODE = 'lfr'
    ICON = 'li_freighter.3db'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03, HpTurret01, HpTurret02, HpTurret03']
    MAX_WEAPONS = ['HpWeapon02', 'HpWeapon03, HpTurret01, HpTurret02']

    COLLISION_HIT_PTS_PERCENT = {
        'panel_hit_pts': HP_PCT_WING,
        'engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'panel_expl_resist': EXPL_RESIST_WING,
        'engine_expl_resist': EXPL_RESIST_ENGINE,
    }


# BRETONIA


class Legionnaire(BretoniaShip, ShipInterceptor, Ship1, Ship):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_BRETONIA_INTERCEPTOR]
    SHIP_INDEX = SHIP_INDEX_3
    SHIELD_LINK = 'co_fighter_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 3

    ARCHETYPE = 'co_fighter'
    RU_NAME = 'Легионер'
    TEMPLATE_CODE = 'cf'
    ICON = 'pi_fighter.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']
    MAX_WEAPONS = ['HpWeapon03', 'HpWeapon04']

    COLLISION_HIT_PTS_PERCENT = {
        'wing_hit_pts': HP_PCT_WING,
        'engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'wing_expl_resist': EXPL_RESIST_WING,
        'engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Cavalier(BretoniaShip, ShipInterceptor, Ship2, Ship):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_BRETONIA_INTERCEPTOR]
    SHIP_INDEX = SHIP_INDEX_7
    SHIELD_LINK = 'b_fighter_shield01'
    ENGINE_TYPE = ENGINE_SINGLE
    LIGHTS = 3

    ARCHETYPE = 'br_fighter'
    RU_NAME = 'Кавалер'
    TEMPLATE_CODE = 'bf'
    ICON = 'br_fighter.3db'
    HP_TORPEDO = 'HpTorpedo02'
    MAIN_WEAPONS = ['HpTorpedo01', 'HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']
    MAX_WEAPONS = ['HpTorpedo01', 'HpWeapon03', 'HpWeapon04']

    COLLISION_HIT_PTS_PERCENT = {
        'tail_hit_pts': HP_PCT_TAIL,
        'engine_hit_pts': HP_PCT_ENGINE_SINGLE,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'tail_expl_resist': EXPL_RESIST_WING,
        'engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Centurion(BretoniaShip, ShipFighter, Ship1, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_BRETONIA_ELITE, CLASS_BRETONIA_FIGHTER_ONLY]
    SHIP_INDEX = SHIP_INDEX_3
    SHIELD_LINK = 'co_elite_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 3

    ARCHETYPE = 'co_elite'
    RU_NAME = 'Центурион'
    TEMPLATE_CODE = 'ce'
    ICON = 'pi_elite.3db'
    HP_TORPEDO = 'HpTorpedo02'
    MAIN_WEAPONS = ['HpTorpedo01', 'HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']
    MAX_WEAPONS = ['HpTorpedo01', 'HpWeapon03', 'HpWeapon04']

    # mk 2 version
    # HP_TORPEDO = 'HpTorpedo01'
    # MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    # MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']

    COLLISION_HIT_PTS_PERCENT = {
        'wing_hit_pts': HP_PCT_WING,
        'fin_hit_pts': HP_PCT_FIN,
        'engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'wing_expl_resist': EXPL_RESIST_WING,
        'fin_expl_resist': EXPL_RESIST_MISC,
        'engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Titan(BretoniaShip, ShipFighter, Ship2, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_BRETONIA_ELITE, CLASS_BRETONIA_FIGHTER_ONLY]
    SHIP_INDEX = SHIP_INDEX_7
    SHIELD_LINK = 'co_elite2_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 3

    ARCHETYPE = 'co_elite2'
    RU_NAME = 'Титан'
    TEMPLATE_CODE = 'ce2'
    ICON = 'pi_heavy.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']

    # mk 2
    # HP_TORPEDO = 'HpTorpedo02'
    # MAIN_WEAPONS = ['HpTorpedo01', 'HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    # MAX_WEAPONS = ['HpTorpedo01', 'HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']

    COLLISION_HIT_PTS_PERCENT = {
        'wing_hit_pts': HP_PCT_WING,
        'fin_hit_pts': HP_PCT_FIN,
        'engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'wing_expl_resist': EXPL_RESIST_WING,
        'fin_expl_resist': EXPL_RESIST_MISC,
        'engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Crusader(BretoniaShip, ShipElite, Ship3, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_BRETONIA_ELITE]
    SHIP_INDEX = SHIP_INDEX_8
    SHIELD_LINK = 'b_elite_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 6

    ARCHETYPE = 'br_elite'
    RU_NAME = 'Крестоносец'
    TEMPLATE_CODE = 'be'
    ICON = 'br_elite.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon05', 'HpWeapon06']

    COLLISION_HIT_PTS_PERCENT = {
        'wing_hit_pts': HP_PCT_WING,
        'tail_hit_pts': HP_PCT_TAIL,
        'engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'wing_expl_resist': EXPL_RESIST_WING,
        'tail_expl_resist': EXPL_RESIST_WING,
        'engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class CrusaderMk2(BretoniaShip, ShipElite, Ship3, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_BRETONIA_ELITE]
    SHIP_INDEX = SHIP_INDEX_10
    LIGHTS = 6

    ARCHETYPE = 'br_elite2'
    RU_NAME = 'Крестоносец Мк.II'
    TEMPLATE_CODE = 'be2'
    ICON = 'br_elite.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon05', 'HpWeapon06']

    COLLISION_HIT_PTS_PERCENT = {
        'wing_hit_pts': HP_PCT_WING,
        'tail_hit_pts': HP_PCT_TAIL,
        'engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME, 
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'wing_expl_resist': EXPL_RESIST_WING,
        'tail_expl_resist': EXPL_RESIST_WING,
        'engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Clydesdale(BretoniaShip, ShipFreighter, Ship):
    ARCHETYPE = 'br_freighter'
    RU_NAME = 'Клейндсаль'
    SHIELD_LINK = 'b_freighter_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 8

    SHIP_INDEX = SHIP_INDEX_6

    TEMPLATE_CODE = 'bfr'
    ICON = 'br_freighter.3db'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03, HpTurret01, HpTurret02, HpTurret03']
    MAX_WEAPONS = ['HpWeapon02', 'HpWeapon03, HpTurret01, HpTurret02']

    COLLISION_HIT_PTS_PERCENT = {
        'wing_hit_pts': HP_PCT_WING,
        'engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'wing_expl_resist': EXPL_RESIST_WING,
        'engine_expl_resist': EXPL_RESIST_ENGINE,
    }


# KUSARI


class Hawk(KusariShip, ShipInterceptor, Ship1, Ship):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_KUSARI_INTERCEPTOR]
    SHIP_INDEX = SHIP_INDEX_3
    SHIELD_LINK = 'cv_fighter4_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 6

    ARCHETYPE = 'ge_fighter4'
    RU_NAME = 'Ястреб'
    TEMPLATE_CODE = 'gf4'
    ICON = 'cv_fighter.3db'
    HP_TORPEDO = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'wing_hit_pts': HP_PCT_WING,
        'engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'wing_expl_resist': EXPL_RESIST_WING,
        'engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Drake(KusariShip, ShipInterceptor, Ship2, Ship):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_KUSARI_INTERCEPTOR]
    SHIP_INDEX = SHIP_INDEX_7
    SHIELD_LINK = 'k_fighter_shield01'
    ENGINE_TYPE = ENGINE_SINGLE
    LIGHTS = 4

    ARCHETYPE = 'ku_fighter'
    RU_NAME = 'Дрейк'
    TEMPLATE_CODE = 'kf'
    ICON = 'ku_fighter.3db'
    HP_TORPEDO = 'HpTorpedo02'
    MAIN_WEAPONS = ['HpTorpedo01', 'HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02']

    COLLISION_HIT_PTS_PERCENT = {
        'wing_hit_pts': HP_PCT_WING,
        'engine_hit_pts': HP_PCT_ENGINE_SINGLE,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'wing_expl_resist': EXPL_RESIST_WING,
        'engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Falcon(KusariShip, ShipFighter, Ship1, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_KUSARI_ELITE, CLASS_KUSARI_FIGHTER_ONLY]
    SHIP_INDEX = SHIP_INDEX_3
    SHIELD_LINK = 'cv_fighter5_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 8

    ARCHETYPE = 'ge_fighter5'
    RU_NAME = 'Сокол'
    TEMPLATE_CODE = 'gf5'
    ICON = 'cv_elite.3db'
    HP_TORPEDO = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'wing_hit_pts': HP_PCT_WING,
        'fin_hit_pts': HP_PCT_FIN,
        'engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'wing_expl_resist': EXPL_RESIST_WING,
        'fin_expl_resist': EXPL_RESIST_MISC,
        'engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Eagle(KusariShip, ShipFighter, Ship2, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_KUSARI_ELITE, CLASS_KUSARI_FIGHTER_ONLY]
    SHIP_INDEX = SHIP_INDEX_7
    SHIELD_LINK = 'cv_fighter6_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 10

    ARCHETYPE = 'ge_fighter6'
    RU_NAME = 'Орел'
    TEMPLATE_CODE = 'gf6'
    ICON = 'cv_heavy.3db'

    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']

    # HP_SHIELD = 'HpShield02'
    # HP_TORPEDO = 'HpTorpedo01'
    # MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06', 'HpWeapon07']
    # MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon07']

    COLLISION_HIT_PTS_PERCENT = {
        'wing_hit_pts': HP_PCT_WING,
        'fin_hit_pts': HP_PCT_FIN,
        'btmwing_hit_pts': HP_PCT_WING,
        'engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'wing_expl_resist': EXPL_RESIST_WING,
        'fin_expl_resist': EXPL_RESIST_MISC,
        'btmwing_expl_resist': EXPL_RESIST_WING,
        'engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Dragon(KusariShip, ShipElite, Ship3, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_KUSARI_ELITE]
    SHIP_INDEX = SHIP_INDEX_8
    SHIELD_LINK = 'k_elite_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 10

    ARCHETYPE = 'ku_elite'
    RU_NAME = 'Дракон'
    TEMPLATE_CODE = 'ke'
    ICON = 'ku_elite.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon05', 'HpWeapon06']

    COLLISION_HIT_PTS_PERCENT = {
        'wing_hit_pts': HP_PCT_MISC,
        'tail_hit_pts': HP_PCT_TAIL,
        'spike_hit_pts': HP_PCT_WING,
        'engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'wing_expl_resist': EXPL_RESIST_MISC,
        'tail_expl_resist': EXPL_RESIST_WING,
        'spike_expl_resist': EXPL_RESIST_WING,
        'engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class DragonMk2(KusariShip, ShipElite, Ship3, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_KUSARI_ELITE]
    SHIP_INDEX = SHIP_INDEX_10
    LIGHTS = 10

    ARCHETYPE = 'ku_dragon'
    RU_NAME = 'Дракон Мk.II'
    TEMPLATE_CODE = 'ke2'
    ICON = 'ku_elite.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon05', 'HpWeapon06']

    COLLISION_HIT_PTS_PERCENT = {
        'wing_hit_pts': HP_PCT_MISC,
        'tail_hit_pts': HP_PCT_TAIL,
        'spike_hit_pts': HP_PCT_WING,
        'engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'wing_expl_resist': EXPL_RESIST_MISC,
        'tail_expl_resist': EXPL_RESIST_WING,
        'spike_expl_resist': EXPL_RESIST_WING,
        'engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Dron(KusariShip, ShipFreighter, Ship):
    ARCHETYPE = 'ku_freighter'
    RU_NAME = 'Дрон'
    SHIELD_LINK = 'k_freighter_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 12

    SHIP_INDEX = SHIP_INDEX_6

    TEMPLATE_CODE = 'kfr'
    ICON = 'ku_freighter.3db'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04, HpTurret02, HpTurret03']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']

    COLLISION_HIT_PTS_PERCENT = {
        'wing_hit_pts': HP_PCT_WING,
        'engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'wing_expl_resist': EXPL_RESIST_MISC,
        'engine_expl_resist': EXPL_RESIST_ENGINE,
    }


# CORSAIR / ORDER


class Bloodhound(CorsairShip, ShipFighter, Ship1, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_CORSAIR_ELITE, CLASS_CORSAIR_FIGHTER_ONLY]
    SHIP_INDEX = SHIP_INDEX_3
    SHIELD_LINK = 'pi_fighter_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 7

    ARCHETYPE = 'pi_fighter'
    RU_NAME = 'Гончая'
    TEMPLATE_CODE = 'pf'
    ICON = 'co_fighter.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03']

    # mk 2
    # HP_TORPEDO = 'HpTorpedo01'
    # MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05, HpTurret01']
    # MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03, HpTurret01']

    COLLISION_HIT_PTS_PERCENT = {
        'fin_hit_pts': HP_PCT_FIN,
        'engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'fin_expl_resist': EXPL_RESIST_MISC,
        'engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Wolfhound(CorsairShip, ShipFighter, Ship2, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_CORSAIR_ELITE, CLASS_CORSAIR_FIGHTER_ONLY]
    SHIP_INDEX = SHIP_INDEX_7
    SHIELD_LINK = 'pi_elite_shield01'
    ENGINE_TYPE = ENGINE_TRIPLE_SAME
    LIGHTS = 6

    ARCHETYPE = 'pi_elite'
    RU_NAME = 'Волкодав'
    TEMPLATE_CODE = 'pe'
    ICON = 'co_elite.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']

    # mk 2
    # HP_TORPEDO = 'HpTorpedo02'
    # MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06, HpTorpedo01']
    # MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04, HpTorpedo01']

    COLLISION_HIT_PTS_PERCENT = {
        'fin_hit_pts': HP_PCT_FIN,
        'engine_hit_pts': HP_PCT_ENGINE_TRIPLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'fin_expl_resist': EXPL_RESIST_MISC,
        'engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Anubis(CorsairShip, ShipElite, Ship3, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_CORSAIR_ELITE]
    SHIP_INDEX = SHIP_INDEX_8
    SHIELD_LINK = 'or_elite_shield01'
    ENGINE_TYPE = ENGINE_TRIPLE_SAME
    LIGHTS = 6

    ARCHETYPE = 'or_elite'
    RU_NAME = 'Анубис'
    TEMPLATE_CODE = 'oe'
    ICON = 'or_elite.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']

    # mk 2
    # MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06', 'HpWeapon07']
    # MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon07']

    COLLISION_HIT_PTS_PERCENT = {
        'wing_hit_pts': HP_PCT_WING,
        'engine1_hit_pts': HP_PCT_ENGINE_TRIPLE_MAIN,
        'engine2_hit_pts': HP_PCT_ENGINE_TRIPLE_SECONDARY,
        'engine3_hit_pts': HP_PCT_ENGINE_TRIPLE_SECONDARY,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'wing_expl_resist': EXPL_RESIST_WING,
        'engine1_expl_resist': EXPL_RESIST_ENGINE,
        'engine2_expl_resist': EXPL_RESIST_ENGINE,
        'engine3_expl_resist': EXPL_RESIST_ENGINE,
    }


class Mule(CorsairShip, ShipFreighter, Ship):
    ARCHETYPE = 'pi_freighter'
    RU_NAME = 'Мул'
    SHIELD_LINK = 'pi_freighter_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 6

    SHIP_INDEX = SHIP_INDEX_6

    TEMPLATE_CODE = 'pfr'
    ICON = 'co_freighter.3db'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']

    # mk2 
    # MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06, HpTurret01']
    # MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04, HpTurret01']

    COLLISION_HIT_PTS_PERCENT = {
        'wing_hit_pts': HP_PCT_WING,
        'fin_hit_pts': HP_PCT_FIN,
        'engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'wing_expl_resist': EXPL_RESIST_WING,
        'fin_expl_resist': EXPL_RESIST_MISC,
        'engine_expl_resist': EXPL_RESIST_ENGINE,
    }


# GENERIC


class Dromader(GenericShip, ShipFreighter, Ship):
    SHIP_INDEX = SHIP_INDEX_3
    ARCHETYPE = 'bw_freighter'
    RU_NAME = 'Дромадер'
    TEMPLATE_CODE = 'bwfr'
    ICON = 'bw_freighter.3db'
    SHIELD_LINK = 'bw_freighter_shield01'
    ENGINE_TYPE = ENGINE_TRIPLE_SAME
    LIGHTS = 8

    COLLISION_HIT_PTS_PERCENT = {
        'wing_hit_pts': HP_PCT_WING,
        'engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'wing_expl_resist': EXPL_RESIST_WING,
        'engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class CSV(GenericShip, ShipFreighter, Ship):
    SHIP_INDEX = SHIP_INDEX_2
    ARCHETYPE = 'ge_csv'
    RU_NAME = 'CSV'
    TEMPLATE_CODE = 'csv'
    ICON = 'co_freighter.3db'
    SHIELD_LINK = 'csv_shield01'
    ENGINE_TYPE = ENGINE_SINGLE
    ENG_FORCE_FEATURE = False
    LIGHTS = 8

    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04, HpTurret01']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02, HpTurret01']


class CSV_Mk2(CSV):
    SHIP_INDEX = SHIP_INDEX_5
    ARCHETYPE = 'ge_csv2'
    RU_NAME = 'CSV Mk.II'
    TEMPLATE_CODE = 'csv2'

    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']


class CSV_Mk3(CSV):
    SHIP_INDEX = SHIP_INDEX_9
    ARCHETYPE = 'ge_csv3'
    RU_NAME = 'CSV Mk.III'
    TEMPLATE_CODE = 'csv3'

    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06, HpTurret01']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04, HpTurret01']


class Armored(GenericShip, ShipFreighter, Ship):
    SHIP_INDEX = SHIP_INDEX_10
    ARCHETYPE = 'ge_armored'
    RU_NAME = 'Бронированный транспорт'
    TEMPLATE_CODE = 'armored'
    ICON = 'ku_freighter.3db'
    LIGHTS = 7
    FORCE_HIT_PTS = 220000


class Starflier(GenericShip, ShipInterceptor, Ship1, Ship):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_GENERIC_INTERCEPTOR]
    SHIP_INDEX = SHIP_INDEX_2
    SHIELD_LINK = 'cv_fighter_shield01'
    ENGINE_TYPE = ENGINE_SINGLE
    LIGHTS = 5

    ARCHETYPE = 'ge_fighter'
    RU_NAME = 'Старфлаер'
    TEMPLATE_CODE = 'gf1'
    ICON = 'cv_starflier.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03']
    MAX_WEAPONS = ['HpWeapon03']

    # mk 2    
    # HP_TORPEDO = 'HpTorpedo02'
    # MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03, HpTorpedo01']
    # MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02']

    COLLISION_HIT_PTS_PERCENT = {
        'wing_hit_pts': HP_PCT_WING,
        'engine_hit_pts': HP_PCT_ENGINE_SINGLE,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'wing_expl_resist': EXPL_RESIST_WING,
        'engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Starflier2(Starflier):
    SHIP_INDEX = SHIP_INDEX_2

    ARCHETYPE = 'ge_fighter_mk2'
    RU_NAME = 'Старфлаер Мк.II'
    TEMPLATE_CODE = 'gf1_mk2'
    HP_TORPEDO = 'HpTorpedo02'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03, HpTorpedo01']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02']


class Startracker(GenericShip, ShipInterceptor, Ship2, Ship):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_GENERIC_INTERCEPTOR]
    SHIP_INDEX = SHIP_INDEX_5
    SHIELD_LINK = 'cv_fighter_shield01'
    ENGINE_TYPE = ENGINE_SINGLE
    LIGHTS = 7

    ARCHETYPE = 'ge_fighter2'
    RU_NAME = 'Стартрекер'
    TEMPLATE_CODE = 'gf2'
    ICON = 'cv_startracker.3db'
    HP_TORPEDO = 'HpTorpedo02'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03, HpTorpedo01']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02']

    # mk 2
    # HP_TORPEDO = 'HpTorpedo01'
    # MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05']
    # MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03']

    COLLISION_HIT_PTS_PERCENT = {
        'wing_hit_pts': HP_PCT_WING,
        'engine_hit_pts': HP_PCT_ENGINE_SINGLE,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'wing_expl_resist': EXPL_RESIST_WING,
        'engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Starblazer(GenericShip, ShipElite, Ship2, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_GENERIC_ELITE]
    SHIP_INDEX = SHIP_INDEX_5
    SHIELD_LINK = 'cv_fighter_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 7

    ARCHETYPE = 'ge_fighter3'
    RU_NAME = 'Старблейзер'
    TEMPLATE_CODE = 'gf3'
    ICON = 'cv_starblazer.3db'
    HP_TORPEDO = 'HpWeapon04'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon05', 'HpWeapon06']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03']

    # mk2
    # HP_TORPEDO = 'HpTorpedo02'
    # MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    # MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']

    COLLISION_HIT_PTS_PERCENT = {
        'wing_hit_pts': HP_PCT_WING,
        'engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'wing_expl_resist': EXPL_RESIST_WING,
        'engine_expl_resist': EXPL_RESIST_ENGINE,
    }
