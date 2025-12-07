from world.equipment import Equipment, MainMiscEquip
from world.npc import NPC
import math
from universe.markets import MarketShip
from text.dividers import SINGLE_DIVIDER
from text.infocards import InfocardBuilder, INFO_SHIP_ABOUT, INFO_SHIP_TABLE, INFO_SHIP_KEYS, INFO_SHIP_VALUES
from text.strings import MultiString as MS
from text.translate import Lang_RU, Lang_EN
from fx.light import Light
from world import level

LIGHT_FIGHTER = 'light_fighter'
HEAVY_FIGHTER = 'heavy_fighter'
FREIGHTER = 'freighter'

SHIP_TYPES = [
    LIGHT_FIGHTER,
    HEAVY_FIGHTER,
    FREIGHTER,
]

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
HP_PCT_ENGINE_TRIPLE_SECOND = 0.25

HP_PCT_WING = 0.4
HP_PCT_TAIL = 0.5
HP_PCT_MISC = 0.25
HP_PCT_FIN = 0.25
HP_PCT_FIN_WITH_ENGINE = 0.4

EXPL_RESIST_ENGINE = 0.25
EXPL_RESIST_WING = 0.5
EXPL_RESIST_MISC = 1

BOT_REPAIR = 600
NUM_REPAIRS = 3

ENGINE_SINGLE = 1
ENGINE_DOUBLE_SAME = 2
ENGINE_DOUBLE_DIFF = 3
ENGINE_TRIPLE_SAME = 4
ENGINE_TRIPLE_DIFF = 5


class Ship(MarketShip):
    ARCHETYPE = None
    TEMPLATE_CODE = None
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

    SHIP_TYPE = None

    FORCE_HIT_PTS = None

    SHIELD_LINK = 'l_elite_shield01'
    ENGINE_TYPE = ENGINE_SINGLE
    ENG_FORCE_FEATURE = False

    SHIP_CLASS = 3
    SHIP_KIND_CODE = None
    MAX_HIT_PTS = 10000
    HP_SHIELD = 'HpShield01'
    HP_ENGINE = 'HpDrive01'
    HP_POWERPLANT = 'HpPower01'
    SHIP_MASS = 100
    HOLD_SIZE = 10
    STRAFE_FORCE = 20000
    STRAFE_POWER_USAGE = 5
    NANOBOTS = 1

    HIT_PTS_PER_CLASS = {}
    CARGO_PER_CLASS = {}

    CONTRAILS_COUNT = 4

    HULL_HIT_PTS_MULTIPLER = 1
    NANOBOTS_COUNT_MULTIPLER = 1
    SHIP_MASS_MULTIPLER = 1
    CARGO_HOLD_MULTIPLER = 1
    EXTRA_CARGO = 0
    STRAFE_FORCE_MULTIPLER = 1
    STRAFE_POWER_USAGE_MULTIPLER = 1
    PACKAGE_EQUIPMENT_FACTOR = -3
    SECOND_WEAPON_CLASS_FACTOR = -1
    EXTRA_PACKAGE_ITEMS = []

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

    def __init__(self, ids):
        self.ids = ids
        ship_stats = self.get_infocard_values()
        self.ids_name = self.ids.new_name(self.get_ru_name())
        self.ids_info = self.ids.new_info(
            MS(
                InfocardBuilder.build_infocard(INFO_SHIP_TABLE, ship_stats, language=Lang_RU),
                InfocardBuilder.build_infocard(INFO_SHIP_TABLE, ship_stats, language=Lang_EN),
            )
        )
        self.ids_info1 = self.ids.new_info(
            MS(
                InfocardBuilder.build_infocard(INFO_SHIP_ABOUT, {}, language=Lang_RU),
                InfocardBuilder.build_infocard(INFO_SHIP_ABOUT, {}, language=Lang_EN)
            )
        )
        self.ids_info2 = self.ids.new_info(
            MS(
                InfocardBuilder.build_infocard(INFO_SHIP_KEYS, {}, language=Lang_RU),
                InfocardBuilder.build_infocard(INFO_SHIP_KEYS, {}, language=Lang_EN)
            )
        )
        self.ids_info3 = self.ids.new_info(
            MS(
                InfocardBuilder.build_infocard(INFO_SHIP_VALUES, ship_stats, language=Lang_RU),
                InfocardBuilder.build_infocard(INFO_SHIP_VALUES, ship_stats, language=Lang_EN)
            )
        )
        self.used = False

    def is_used(self):
        return self.used

    def get_market_level(self):
        return level.SHIP_LEVEL_PER_CLASS[self.SHIP_CLASS]

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
        'equip = {shield_npc}, HpShield01',
        'cargo = {shield}, 1',
        'equip = LargeWhiteSpecial, HpHeadlight',
        'equip = DockingLightRedSmall, HpDockLight01',
        'equip = DockingLightRedSmall, HpDockLight02',
    ]

    ICON = None
    GEN_ARMOR_TEMPLATE = 'equip = {armor}'

    HAS_ANIMATION = True
    LOADOUT_LAUNCH_ANIMATION = 'equip = launch_extend'
    LOADOUT_LIGHT_TEMPLATE = 'equip = {{small_light}}, HpRunningLight{light_id}'
    LOADOUT_CONTRAIL_TEMPLATE = 'equip = {{contrail}}, HpContrail{contrail_id}'
    LOADOUT_THRUSTER_TEMPLATE = 'equip = {{afterburn{thruster_index}}}, {hp_thruster}'
    LOADOUT_WEAPON_TEMPLATE = 'equip = {{weapon{weapon_index}}}, {hp_weapon}'

    HP_HEADLIGHT = 'HpHeadlight'
    PACKAGE_LAUNCH_ANIMATION = 'addon = launch_extend, internal, 1'
    PACKAGE_LIGHT_TEMPLATE = 'addon = {{small_light}}, HpRunningLight{light_id}, 1'
    PACKAGE_CONTRAIL_TEMPLATE = 'addon = player_contrail, HpContrail{contrail_id}, 1'

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

    ADDITIONAL_EQUIP = ''

    def get_loadout_components(self, have_afterburn1=True, have_afterburn2=True, have_gen_armor=True,
                               animated_wings=True):
        components = []
        components.extend(self.LOADOUT_TEMPLATE_BASE_COMPONENTS)

        if have_gen_armor:
            components.append(self.GEN_ARMOR_TEMPLATE)

        if self.HAS_ANIMATION and animated_wings:
            components.append(self.LOADOUT_LAUNCH_ANIMATION)

        i = 1
        for hp_weapon in self.MAIN_WEAPONS:
            components.append(self.LOADOUT_WEAPON_TEMPLATE.format(weapon_index=i, hp_weapon=hp_weapon))
            i += 1

        i = 1
        for hp_thruster in self.THRUSTERS:
            if i == 1 and not have_afterburn1:
                continue

            if i == 2 and not have_afterburn2:
                continue

            components.append(self.LOADOUT_THRUSTER_TEMPLATE.format(thruster_index=i, hp_thruster=hp_thruster))
            i += 1

        for i in range(1, self.CONTRAILS_COUNT + 1):
            components.append(self.LOADOUT_CONTRAIL_TEMPLATE.format(contrail_id=f'0{i}'))

        for i in range(1, self.LIGHTS + 1):
            components.append(self.LOADOUT_LIGHT_TEMPLATE.format(light_id=f'0{i}'))

        return components

    def get_loadout_template(self, have_afterburn1=True, have_afterburn2=True, have_gen_armor=True,
                             animated_wings=True):
        return self.BASE_LOADOUT.format(loadout=SINGLE_DIVIDER.join(self.get_loadout_components(
            have_afterburn1=have_afterburn1,
            have_afterburn2=have_afterburn2,
            have_gen_armor=have_gen_armor,
            animated_wings=animated_wings,
        )))

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

    def get_package_extra_template(self):
        components = []

        if self.HAS_ANIMATION:
            components.append(self.PACKAGE_LAUNCH_ANIMATION)

        for item in self.EXTRA_PACKAGE_ITEMS:
            components.append(item)

        for i in range(1, self.CONTRAILS_COUNT + 1):
            components.append(self.PACKAGE_CONTRAIL_TEMPLATE.format(contrail_id=f'0{i}'))

        for i in range(1, self.LIGHTS + 1):
            components.append(self.PACKAGE_LIGHT_TEMPLATE.format(light_id=f'0{i}'))

        return SINGLE_DIVIDER.join(components)

    def get_package_equipment_class(self):
        factor = self.SHIP_CLASS + self.PACKAGE_EQUIPMENT_FACTOR
        if factor < 1:
            return 1
        return factor

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

    PRICE_PER_CLASS = {
        3: 0.012,
        4: 0.02,
        5: 0.035,
        6: 0.08,
        7: 0.2,
        8: 0.5,
        9: 0.7,
        10: 1,
    }
    
    def get_ship_price(self):
        return self.MAX_PRICE * self.PRICE_PER_CLASS[self.SHIP_CLASS]

    def get_hull(self):
        if not self.ICON:
            raise Exception(f'ship {self} have no ICON')

        return self.HULL_BASE_TEMPLATE.format(
            hull_nickname=self.get_hull_nickname(),
            ship_archetype=self.ARCHETYPE,
            price=self.get_ship_price(),
            icon=self.ICON,
        )

    def get_equipment_level(self):
        return self.SHIP_CLASS

    def get_main_weapon_class(self):
        return self.SHIP_CLASS + self.SECOND_WEAPON_CLASS_FACTOR

    def get_max_weapon_class(self):
        return self.SHIP_CLASS

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
        return math.ceil((self.CARGO_PER_CLASS[self.SHIP_CLASS] * self.CARGO_HOLD_MULTIPLER) + self.EXTRA_CARGO)

    def get_strafe_force(self):
        return math.ceil(self.STRAFE_FORCE * self.STRAFE_FORCE_MULTIPLER)

    def get_strafe_force_power_usage(self):
        return math.ceil(self.STRAFE_POWER_USAGE * self.STRAFE_POWER_USAGE_MULTIPLER)

    def get_hit_pts(self):
        if self.FORCE_HIT_PTS:
            return self.FORCE_HIT_PTS
        return math.ceil(self.HIT_PTS_PER_CLASS[self.SHIP_CLASS] * self.HULL_HIT_PTS_MULTIPLER)

    def get_bots_count(self):
        return math.ceil(((self.get_hit_pts() * NUM_REPAIRS) / BOT_REPAIR) * self.NANOBOTS_COUNT_MULTIPLER)

    def get_ids_name(self):
        return self.ids_name.id

    def get_ids_info(self):
        return self.ids_info.id

    def get_ids_info1(self):
        return self.ids_info1.id

    def get_ids_info2(self):
        return self.ids_info2.id

    def get_ids_info3(self):
        return self.ids_info3.id

    def get_base_template_params(self):
        return {
            'shiparch_name': self.ARCHETYPE,
            'ids_name': self.get_ids_name(),
            'ids_info': self.get_ids_info(),
            'ids_info1': self.get_ids_info1(),
            'ids_info2': self.get_ids_info2(),
            'ids_info3': self.get_ids_info3(),
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

    @property
    def root(self):
        if self.is_used():
            raise Exception(f'ship {self} already used')
        self.used = True
        params = [
            f'nickname = {self.ARCHETYPE}',
            f'ship_class = {self.SHIP_KIND_CODE}',
            f'ids_name = {self.get_ids_name()}',
            f'ids_info = {self.get_ids_info()}',
            f'ids_info1 = {self.get_ids_info1()}',
            f'ids_info2 = {self.get_ids_info2()}',
            f'ids_info3 = {self.get_ids_info3()}',
            f'shield_link = {self.SHIELD_LINK}, HpMount, {self.HP_SHIELD}',
            f'mass = {self.get_ship_mass()}',
            f'hold_size = {self.get_hold_size()}',
            f'strafe_force = {self.get_strafe_force()}',
            f'strafe_power_usage = {self.get_strafe_force_power_usage()}',
            f'nanobot_limit = {self.get_bots_count()}',
            f'shield_battery_limit = {self.get_bots_count()}',
            f'hit_pts = {self.get_hit_pts()}',
            self.get_fuses(),
            self.get_equipment_table(),
        ]
        return SINGLE_DIVIDER.join(params)

    def get_part(self, hit_pts_pct, proxy_health, explosion_resistance):
        params = [
            f'hit_pts = {self.get_hit_pts() * hit_pts_pct}',
            f'root_health_proxy = {"true" if proxy_health else "false"}',
            f'explosion_resistance = {explosion_resistance}',
        ]
        return SINGLE_DIVIDER.join(params)

    FIN_PROXY_HEALTH = False
    WING_LIKE_FIN = False
    LARGE_FIRST_ENGINE = False

    FIN_HAVE_ENGINE = False

    @property
    def fin1(self):
        return self.get_part(
            HP_PCT_FIN,
            self.FIN_PROXY_HEALTH,
            EXPL_RESIST_MISC,
        )

    @property
    def fin2(self):
        return self.get_part(
            HP_PCT_FIN_WITH_ENGINE if self.FIN_HAVE_ENGINE else HP_PCT_FIN,
            self.FIN_PROXY_HEALTH,
            EXPL_RESIST_MISC,
        )

    @property
    def fin3(self):
        return self.get_part(
            HP_PCT_FIN,
            self.FIN_PROXY_HEALTH,
            EXPL_RESIST_MISC,
        )

    @property
    def fin4(self):
        return self.get_part(
            HP_PCT_FIN,
            self.FIN_PROXY_HEALTH,
            EXPL_RESIST_MISC,
        )

    @property
    def eng1(self):
        if self.ENGINE_TYPE == ENGINE_SINGLE:
            return self.get_part(HP_PCT_ENGINE_SINGLE, True, EXPL_RESIST_ENGINE)

        if self.ENGINE_TYPE == ENGINE_DOUBLE_SAME:
            return self.get_part(HP_PCT_ENGINE_DOUBLE_SAME, True, EXPL_RESIST_ENGINE)

        if self.ENGINE_TYPE == ENGINE_DOUBLE_DIFF:
            return self.get_part(HP_PCT_ENGINE_DOUBLE_MAIN, True, EXPL_RESIST_ENGINE)

        if self.ENGINE_TYPE == ENGINE_TRIPLE_SAME:
            return self.get_part(HP_PCT_ENGINE_TRIPLE_SAME, True, EXPL_RESIST_ENGINE)

        if self.ENGINE_TYPE == ENGINE_TRIPLE_DIFF:
            return self.get_part(HP_PCT_ENGINE_TRIPLE_MAIN, True, EXPL_RESIST_ENGINE)

        raise Exception(f'ship {self} have unknown engine type')

    @property
    def eng2(self):
        if self.ENGINE_TYPE == ENGINE_SINGLE:
            raise Exception(f'ship {self} cant use second engine')

        if self.ENGINE_TYPE == ENGINE_DOUBLE_SAME:
            return self.get_part(HP_PCT_ENGINE_DOUBLE_SAME, True, EXPL_RESIST_ENGINE)

        if self.ENGINE_TYPE == ENGINE_DOUBLE_DIFF:
            return self.get_part(HP_PCT_ENGINE_DOUBLE_SECOND, True, EXPL_RESIST_ENGINE)

        if self.ENGINE_TYPE == ENGINE_TRIPLE_SAME:
            return self.get_part(HP_PCT_ENGINE_TRIPLE_SAME, True, EXPL_RESIST_ENGINE)

        if self.ENGINE_TYPE == ENGINE_TRIPLE_DIFF:
            return self.get_part(HP_PCT_ENGINE_TRIPLE_SECOND, True, EXPL_RESIST_ENGINE)

        raise Exception(f'ship {self} have unknown engine type')

    @property
    def eng3(self):
        if self.ENGINE_TYPE in [ENGINE_SINGLE, ENGINE_DOUBLE_SAME, ENGINE_DOUBLE_DIFF]:
            raise Exception(f'ship {self} cant use third engine')

        if self.ENGINE_TYPE == ENGINE_TRIPLE_SAME:
            return self.get_part(HP_PCT_ENGINE_TRIPLE_SAME, True, EXPL_RESIST_ENGINE)

        if self.ENGINE_TYPE == ENGINE_TRIPLE_DIFF:
            return self.get_part(HP_PCT_ENGINE_TRIPLE_SECOND, True, EXPL_RESIST_ENGINE)

        raise Exception(f'ship {self} have unknown engine type')

    @property
    def wing1(self):
        if self.WING_LIKE_FIN:
            return self.get_part(HP_PCT_MISC, False, EXPL_RESIST_MISC)

        return self.get_part(HP_PCT_WING, True, EXPL_RESIST_WING)

    @property
    def wing2(self):
        if self.WING_LIKE_FIN:
            return self.get_part(HP_PCT_MISC, False, EXPL_RESIST_MISC)

        return self.get_part(HP_PCT_WING, True, EXPL_RESIST_WING)

    @property
    def wing3(self):
        if self.WING_LIKE_FIN:
            return self.get_part(HP_PCT_MISC, False, EXPL_RESIST_MISC)

        return self.get_part(HP_PCT_WING, True, EXPL_RESIST_WING)

    @property
    def wing4(self):
        if self.WING_LIKE_FIN:
            return self.get_part(HP_PCT_MISC, False, EXPL_RESIST_MISC)

        return self.get_part(HP_PCT_WING, True, EXPL_RESIST_WING)

    @property
    def tail(self):
        return self.get_part(HP_PCT_TAIL, True, EXPL_RESIST_ENGINE)

    @property
    def spoiler(self):
        return self.get_part(HP_PCT_TAIL, True, EXPL_RESIST_ENGINE)

    @property
    def spike1(self):
        return self.get_part(HP_PCT_WING, True, EXPL_RESIST_WING)

    @property
    def spike2(self):
        return self.get_part(HP_PCT_WING, True, EXPL_RESIST_WING)

    @property
    def panel1(self):
        return self.get_part(HP_PCT_WING, True, EXPL_RESIST_WING)

    @property
    def panel2(self):
        return self.get_part(HP_PCT_WING, True, EXPL_RESIST_WING)


class BaseInterceptorShip(object):
    SHIP_TYPE = LIGHT_FIGHTER
    MAX_HIT_PTS = 12000
    SHIP_KIND_CODE = 0

    MAX_PRICE = 400000

    ADDITIONAL_EQUIP = 'M, CM, CD'

    HIT_PTS_PER_CLASS = {
        1: 1000,
        2: 1100,
        3: 1200,
        4: 1800,
        5: 2200,
        6: 3000,
        7: 4500,
        8: 6000,
        9: 8000,
        10: 10000,
    }

    CARGO_PER_CLASS = {
        3: 20,
        4: 30,
        5: 40,
        6: 50,
        7: 55,
        8: 60,
    }


class BaseFighterShip(object):
    SHIP_TYPE = HEAVY_FIGHTER
    MAX_HIT_PTS = 10000
    SHIP_KIND_CODE = 1

    MAX_PRICE = 550000

    ADDITIONAL_EQUIP = 'M, CM, CD/T'

    HIT_PTS_PER_CLASS = {
        1: 1200,
        2: 1500,
        3: 1800,
        4: 2000,
        5: 3000,
        6: 4000,
        7: 5000,
        8: 8000,
        9: 10000,
        10: 12000,
    }

    CARGO_PER_CLASS = {
        4: 35,
        5: 40,
        6: 45,
        7: 55,
        8: 60,
        9: 70,
        10: 75,
    }


class BaseFreighterShip(object):
    SHIP_TYPE = FREIGHTER
    MAX_HIT_PTS = 14000
    SHIP_KIND_CODE = 2

    ADDITIONAL_EQUIP = 'M, CM'

    MAX_PRICE = 700000

    HIT_PTS_PER_CLASS = {
        1: 1500,
        2: 1800,
        3: 2000,
        4: 2500,
        5: 3250,
        6: 4500,
        7: 7500,
        8: 9500,
        9: 12000,
        10: 15000,
    }

    CARGO_PER_CLASS = {
        4: 70,
        5: 80,
        6: 90,
        7: 110,
        8: 120,
        9: 140,
        10: 150,
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

    ARMOR_PER_CLASS = {
        3: 1200,
        4: 1800,
        5: 2200,
        6: 3000,
    }


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


class ShipFreighter(Ship2, BaseFreighterShip):
    EQUIPMENT_SHIPCLASS = Equipment.SHIPCLASS_FREIGHTER
    SHIPCLASS_NAME = 'freighter'
    EXTRA_CLASSES = []

    SHIELD_CLASS_TEMPLATE = 'hp_freighter_shield_special_{class_digit}'
    ENGINE_CLASS_TEMPLATE = 'hp_freighter_engine_special_{class_digit}'
    POWERPLANT_CLASS_TEMPLATE = 'hp_freighter_power_special_{class_digit}'


# RHEINLAND


class Dagger(RheinlandShip, ShipInterceptor, Ship1, Ship):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_RHEINLAND_INTERCEPTOR]
    SHIP_CLASS = 4
    SHIELD_LINK = 'bw_fighter_shield01'
    ENGINE_TYPE = ENGINE_SINGLE
    LIGHTS = 8
    EXCLUDED_LIGHTS = [6, 7]

    ARCHETYPE = 'bw_fighter'
    RU_NAME = MS('Кинжал', 'Dagger')
    TEMPLATE_CODE = 'bwf'
    ICON = 'bw_fighter.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02']

    # mk2 
    # HP_TORPEDO = 'HpTorpedo01'
    # MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04, HpTurret01']
    # MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02, HpTurret01']


class Banshee(RheinlandShip, ShipInterceptor, Ship2, Ship):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_RHEINLAND_INTERCEPTOR]
    SHIP_CLASS = 8
    SHIELD_LINK = 'r_fighter_shield01'
    ENGINE_TYPE = ENGINE_SINGLE
    LIGHTS = 6

    ARCHETYPE = 'rh_fighter'
    RU_NAME = MS('Баньши', 'Banshee')
    TEMPLATE_CODE = 'rf'
    ICON = 'rh_fighter.3db'
    HP_TORPEDO = 'HpTorpedo02'
    MAIN_WEAPONS = ['HpTorpedo01', 'HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']
    MAX_WEAPONS = ['HpTorpedo01', 'HpWeapon03', 'HpWeapon04']


class Stiletto(RheinlandShip, ShipFighter, Ship1, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_RHEINLAND_ELITE, CLASS_RHEINLAND_FIGHTER_ONLY]
    SHIP_CLASS = 5
    SHIELD_LINK = 'bw_elite_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 6

    ARCHETYPE = 'bw_elite'
    RU_NAME = MS('Стилет', 'Stiletto')
    TEMPLATE_CODE = 'bwe'
    ICON = 'bw_elite.3db'
    HP_TORPEDO = 'HpWeapon06'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03']

    # mk2: minds??

    # HP_TORPEDO = 'HpTorpedo01'
    # MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    # MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']


class Sabre(RheinlandShip, ShipFighter, Ship2, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_RHEINLAND_ELITE, CLASS_RHEINLAND_FIGHTER_ONLY]
    SHIP_CLASS = 9
    SHIELD_LINK = 'bw_vheavy_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 8

    ARCHETYPE = 'bw_elite2'
    RU_NAME = MS('Сабля', 'Sabre')
    TEMPLATE_CODE = 'bwe2'
    ICON = 'bw_heavy.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']


class Valkyrie(RheinlandShip, ShipElite, Ship3, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_RHEINLAND_ELITE]
    SHIP_CLASS = 8
    SHIELD_LINK = 'r_elite_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 6

    ARCHETYPE = 'rh_elite'
    RU_NAME = MS('Валькирия', 'Valkyrie')
    TEMPLATE_CODE = 're'
    ICON = 'rh_elite.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    MAX_WEAPONS = ['HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']


class Humpback(RheinlandShip, ShipFreighter, Ship):
    ARCHETYPE = 'rh_freighter'
    RU_NAME = MS('Горбун', 'Humpback')
    SHIELD_LINK = 'r_freighter_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    SHIP_CLASS = 8
    LIGHTS = 7

    TEMPLATE_CODE = 'rfr'
    ICON = 'rh_freighter.3db'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon05', 'HpWeapon06', 'HpWeapon10']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon05', 'HpWeapon06']


# LIBERTY


class Piranha(LibertyShip, ShipInterceptor, Ship1, Ship):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_LIBERTY_INTERCEPTOR]
    SHIP_CLASS = 5
    SHIELD_LINK = 'bh_fighter_shield01'
    ENGINE_TYPE = ENGINE_SINGLE
    LIGHTS = 6

    ARCHETYPE = 'bh_fighter'
    RU_NAME = MS('Пиранья', 'Piranha')
    TEMPLATE_CODE = 'bhf'
    ICON = 'bh_fighter.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']
    MAX_WEAPONS = ['HpWeapon03', 'HpWeapon04']


class Patriot(LibertyShip, ShipInterceptor, Ship2, Ship):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_LIBERTY_INTERCEPTOR]
    SHIP_CLASS = 6
    LIGHTS = 4

    ARCHETYPE = 'li_fighter'
    RU_NAME = MS('Патриот', 'Patriot')
    SHIELD_LINK = 'l_fighter_shield01'
    ENGINE_TYPE = ENGINE_SINGLE
    TEMPLATE_CODE = 'lf'
    ICON = 'li_fighter.3db'
    HP_TORPEDO = 'HpTorpedo02'
    MAIN_WEAPONS = ['HpTorpedo01', 'HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']
    MAX_WEAPONS = ['HpWeapon03', 'HpWeapon04']


class Barracuda(LibertyShip, ShipFighter, Ship1, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_LIBERTY_ELITE, CLASS_LIBERTY_FIGHTER_ONLY]
    SHIP_CLASS = 5
    SHIELD_LINK = 'bh_elite_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 6

    ARCHETYPE = 'bh_elite'
    RU_NAME = MS('Барракуда', 'Barracuda')
    TEMPLATE_CODE = 'bhe'
    ICON = 'bh_elite.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05']
    MAX_WEAPONS = ['HpWeapon03', 'HpWeapon04', 'HpWeapon05']

    FIN_HAVE_ENGINE = True

    # mk 2
    # HP_TORPEDO = 'HpTorpedo02'
    # MAIN_WEAPONS = ['HpTorpedo01', 'HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05']
    # MAX_WEAPONS = ['HpTorpedo01', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05']


class Hammerhead(LibertyShip, ShipFighter, Ship2, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_LIBERTY_ELITE, CLASS_LIBERTY_FIGHTER_ONLY]
    SHIP_CLASS = 8
    SHIELD_LINK = 'bh_elite_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 6

    ARCHETYPE = 'bh_elite2'
    RU_NAME = MS('Рыба-молот', 'Hammerhead')
    TEMPLATE_CODE = 'bhe2'
    ICON = 'bh_heavy.3db'
    HP_TORPEDO = 'HpWeapon06'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon07']
    MAX_WEAPONS = ['HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon07']


class Defender(LibertyShip, ShipElite, Ship3, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_LIBERTY_ELITE]
    SHIP_CLASS = 6
    SHIELD_LINK = 'l_elite_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_DIFF
    LIGHTS = 4

    ARCHETYPE = 'li_elite'
    RU_NAME = MS('Защитник', 'Defender')
    TEMPLATE_CODE = 'le'
    ICON = 'li_elite.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05']
    MAX_WEAPONS = ['HpWeapon03', 'HpWeapon04']


class DefenderJuni(LibertyShip, ShipElite, Ship3, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_LIBERTY_ELITE]
    SHIP_CLASS = 9
    SHIELD_LINK = 'l_elite2_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_DIFF
    LIGHTS = 4

    ARCHETYPE = 'li_elite2'
    RU_NAME = MS('Рейнджер', 'Ranger')
    TEMPLATE_CODE = 'le2'
    ICON = 'li_elite.3db'
    HP_TORPEDO = 'HpTorpedo02'
    MAIN_WEAPONS = ['HpTorpedo01', 'HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05']
    MAX_WEAPONS = ['HpTorpedo01', 'HpWeapon03', 'HpWeapon04']


class Rhino(LibertyShip, ShipFreighter, Ship):
    ARCHETYPE = 'li_freighter'
    RU_NAME = MS('Носорог', 'Rhino')
    SHIP_CLASS = 5
    SHIELD_LINK = 'l_freighter_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 7

    TEMPLATE_CODE = 'lfr'
    ICON = 'li_freighter.3db'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03, HpTurret01, HpTurret02, HpTurret03']
    MAX_WEAPONS = ['HpWeapon02', 'HpWeapon03, HpTurret01, HpTurret02']


# BRETONIA


class Legionnaire(BretoniaShip, ShipInterceptor, Ship1, Ship):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_BRETONIA_INTERCEPTOR]
    SHIP_CLASS = 6
    SHIELD_LINK = 'co_fighter_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 3

    ARCHETYPE = 'co_fighter'
    RU_NAME = MS('Легионер', 'Legionnaire')
    TEMPLATE_CODE = 'cf'
    ICON = 'pi_fighter.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']
    MAX_WEAPONS = ['HpWeapon03', 'HpWeapon04']


class Cavalier(BretoniaShip, ShipInterceptor, Ship2, Ship):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_BRETONIA_INTERCEPTOR]
    SHIP_CLASS = 7
    SHIELD_LINK = 'b_fighter_shield01'
    ENGINE_TYPE = ENGINE_SINGLE
    LIGHTS = 3

    ARCHETYPE = 'br_fighter'
    RU_NAME = MS('Кавалер', 'Cavalier')
    TEMPLATE_CODE = 'bf'
    ICON = 'br_fighter.3db'
    HP_TORPEDO = 'HpTorpedo02'
    MAIN_WEAPONS = ['HpTorpedo01', 'HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']
    MAX_WEAPONS = ['HpTorpedo01', 'HpWeapon03', 'HpWeapon04']


class Centurion(BretoniaShip, ShipFighter, Ship1, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_BRETONIA_ELITE, CLASS_BRETONIA_FIGHTER_ONLY]
    SHIP_CLASS = 6
    SHIELD_LINK = 'co_elite_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 3

    ARCHETYPE = 'co_elite'
    RU_NAME = MS('Центурион', 'Centurion')
    TEMPLATE_CODE = 'ce'
    ICON = 'pi_elite.3db'
    HP_TORPEDO = 'HpTorpedo02'
    MAIN_WEAPONS = ['HpTorpedo01', 'HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']
    MAX_WEAPONS = ['HpTorpedo01', 'HpWeapon03', 'HpWeapon04']

    # mk 2 version
    # HP_TORPEDO = 'HpTorpedo01'
    # MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    # MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']


class CenturionDarcy(Centurion, Ship):
    ARCHETYPE = 'co_elite_darcy'
    TEMPLATE_CODE = 'ced'

    def get_ship_price(self):
        return 5000


class Titan(BretoniaShip, ShipFighter, Ship2, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_BRETONIA_ELITE, CLASS_BRETONIA_FIGHTER_ONLY]
    SHIP_CLASS = 9
    SHIELD_LINK = 'co_elite2_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 3

    ARCHETYPE = 'co_elite2'
    RU_NAME = MS('Титан', 'Titan')
    TEMPLATE_CODE = 'ce2'
    ICON = 'pi_heavy.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']

    # mk 2
    # HP_TORPEDO = 'HpTorpedo02'
    # MAIN_WEAPONS = ['HpTorpedo01', 'HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    # MAX_WEAPONS = ['HpTorpedo01', 'HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']


class Crusader(BretoniaShip, ShipElite, Ship3, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_BRETONIA_ELITE]
    SHIP_CLASS = 7
    SHIELD_LINK = 'b_elite_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 6

    ARCHETYPE = 'br_elite'
    RU_NAME = MS('Крестоносец', 'Crusader')
    TEMPLATE_CODE = 'be'
    ICON = 'br_elite.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon05', 'HpWeapon06']


class Clydesdale(BretoniaShip, ShipFreighter, Ship):
    ARCHETYPE = 'br_freighter'
    RU_NAME = MS('Клейндсаль', 'Clydesdale')
    SHIELD_LINK = 'b_freighter_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 8

    SHIP_CLASS = 6

    TEMPLATE_CODE = 'bfr'
    ICON = 'br_freighter.3db'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03, HpTurret01, HpTurret02, HpTurret03']
    MAX_WEAPONS = ['HpWeapon02', 'HpWeapon03, HpTurret01, HpTurret02']


# KUSARI


class Hawk(KusariShip, ShipInterceptor, Ship1, Ship):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_KUSARI_INTERCEPTOR]
    SHIP_CLASS = 6
    SHIELD_LINK = 'cv_fighter4_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 6

    ARCHETYPE = 'ge_fighter4'
    RU_NAME = MS('Ястреб', 'Hawk')
    TEMPLATE_CODE = 'gf4'
    ICON = 'cv_fighter.3db'
    HP_TORPEDO = 'HpTorpedo01'


class Drake(KusariShip, ShipInterceptor, Ship2, Ship):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_KUSARI_INTERCEPTOR]
    SHIP_CLASS = 7
    SHIELD_LINK = 'k_fighter_shield01'
    ENGINE_TYPE = ENGINE_SINGLE
    LIGHTS = 4

    WING_LIKE_FIN = True

    ARCHETYPE = 'ku_fighter'
    RU_NAME = MS('Дрейк', 'Drake')
    TEMPLATE_CODE = 'kf'
    ICON = 'ku_fighter.3db'
    HP_TORPEDO = 'HpTorpedo02'
    MAIN_WEAPONS = ['HpTorpedo01', 'HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02']


class Falcon(KusariShip, ShipFighter, Ship1, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_KUSARI_ELITE, CLASS_KUSARI_FIGHTER_ONLY]
    SHIP_CLASS = 6
    SHIELD_LINK = 'cv_fighter5_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 8

    ARCHETYPE = 'ge_fighter5'
    RU_NAME = MS('Сокол', 'Falcon')
    TEMPLATE_CODE = 'gf5'
    ICON = 'cv_elite.3db'
    HP_TORPEDO = 'HpTorpedo01'


class Eagle(KusariShip, ShipFighter, Ship2, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_KUSARI_ELITE, CLASS_KUSARI_FIGHTER_ONLY]
    SHIP_CLASS = 9
    SHIELD_LINK = 'cv_fighter6_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 10

    ARCHETYPE = 'ge_fighter6'
    RU_NAME = MS('Орел', "Eagle")
    TEMPLATE_CODE = 'gf6'
    ICON = 'cv_heavy.3db'

    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']

    # HP_SHIELD = 'HpShield02'
    # HP_TORPEDO = 'HpTorpedo01'
    # MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06', 'HpWeapon07']
    # MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon07']


class Dragon(KusariShip, ShipElite, Ship3, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_KUSARI_ELITE]
    SHIP_CLASS = 7
    SHIELD_LINK = 'k_elite_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 10

    WING_LIKE_FIN = True

    ARCHETYPE = 'ku_elite'
    RU_NAME = MS('Дракон', 'Dragon')
    TEMPLATE_CODE = 'ke'
    ICON = 'ku_elite.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon05', 'HpWeapon06']


class Dron(KusariShip, ShipFreighter, Ship):
    ARCHETYPE = 'ku_freighter'
    RU_NAME = MS('Дрон', 'Drone')
    SHIELD_LINK = 'k_freighter_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 12
    CONTRAILS_COUNT = 6

    SHIP_CLASS = 7

    TEMPLATE_CODE = 'kfr'
    ICON = 'ku_freighter.3db'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04, HpTurret02, HpTurret03']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']


# CORSAIR / ORDER


class Bloodhound(CorsairShip, ShipInterceptor, Ship1, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_CORSAIR_ELITE, CLASS_CORSAIR_FIGHTER_ONLY]
    SHIP_CLASS = 5
    SHIELD_LINK = 'pi_fighter_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 7

    ARCHETYPE = 'pi_fighter'
    RU_NAME = MS('Гончая', 'Bloodhound')
    TEMPLATE_CODE = 'pf'
    ICON = 'co_fighter.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03']

    # mk 2
    # HP_TORPEDO = 'HpTorpedo01'
    # MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05, HpTurret01']
    # MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03, HpTurret01']


class Wolfhound(CorsairShip, ShipFighter, Ship2, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_CORSAIR_ELITE, CLASS_CORSAIR_FIGHTER_ONLY]
    SHIP_CLASS = 7
    SHIELD_LINK = 'pi_elite_shield01'
    ENGINE_TYPE = ENGINE_TRIPLE_SAME
    LIGHTS = 6

    ARCHETYPE = 'pi_elite'
    RU_NAME = MS('Волкодав', 'Wolfhound')
    TEMPLATE_CODE = 'pe'
    ICON = 'co_elite.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']

    # mk 2
    # HP_TORPEDO = 'HpTorpedo02'
    # MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06, HpTorpedo01']
    # MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04, HpTorpedo01']


class Anubis(CorsairShip, ShipElite, Ship3, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_CORSAIR_ELITE]
    SHIP_CLASS = 9
    SHIELD_LINK = 'or_elite_shield01'
    ENGINE_TYPE = ENGINE_TRIPLE_SAME
    LIGHTS = 6

    ARCHETYPE = 'or_elite'
    RU_NAME = MS('Анубис', 'Anubis')
    TEMPLATE_CODE = 'oe'
    ICON = 'or_elite.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']

    # mk 2
    # MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06', 'HpWeapon07']
    # MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon07']


class Mule(CorsairShip, ShipFreighter, Ship):
    ARCHETYPE = 'pi_freighter'
    RU_NAME = MS('Мул', 'Mule')
    SHIELD_LINK = 'pi_freighter_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 6

    SHIP_CLASS = 7

    TEMPLATE_CODE = 'pfr'
    ICON = 'co_freighter.3db'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']

    # mk2 
    # MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06, HpTurret01']
    # MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04, HpTurret01']


# GENERIC


class Dromader(GenericShip, ShipFreighter, Ship):
    SHIP_CLASS = 4
    ARCHETYPE = 'bw_freighter'
    RU_NAME = MS('Дромадер', 'Dromader')
    TEMPLATE_CODE = 'bwfr'
    ICON = 'bw_freighter.3db'
    SHIELD_LINK = 'bw_freighter_shield01'
    ENGINE_TYPE = ENGINE_TRIPLE_SAME
    LIGHTS = 8

    MAIN_WEAPONS = ['HpWeapon02', 'HpWeapon03', 'HpTurret02', 'HpTurret03', 'HpTurret04', 'HpTurret05']
    MAX_WEAPONS = ['HpWeapon02', 'HpWeapon03', 'HpTurret02', 'HpTurret03']


class CSV(GenericShip, ShipFreighter, Ship):
    SHIP_CLASS = 5
    ARCHETYPE = 'ge_csv'
    RU_NAME = MS('CSV', 'CSV')
    TEMPLATE_CODE = 'csv1'
    ICON = 'co_freighter.3db'
    SHIELD_LINK = 'csv_shield01'
    ENGINE_TYPE = ENGINE_SINGLE
    ENG_FORCE_FEATURE = False
    LIGHTS = 8

    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04, HpTurret01']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02, HpTurret01']
    EXTRA_PACKAGE_ITEMS = [
        'addon = csv_manipulator01, HpWeapon10',
    ]


class Starflier(GenericShip, ShipInterceptor, Ship1, Ship):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_GENERIC_INTERCEPTOR]
    SHIP_CLASS = 3
    SHIELD_LINK = 'cv_fighter_shield01'
    ENGINE_TYPE = ENGINE_SINGLE
    LIGHTS = 5

    ARCHETYPE = 'ge_fighter'
    RU_NAME = MS('Старфлаер', 'Starflyer')
    TEMPLATE_CODE = 'gf1'
    ICON = 'cv_starflier.3db'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03']
    MAX_WEAPONS = ['HpWeapon03']

    # mk 2    
    # HP_TORPEDO = 'HpTorpedo02'
    # MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03, HpTorpedo01']
    # MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02']


class Startracker(GenericShip, ShipInterceptor, Ship2, Ship):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_GENERIC_INTERCEPTOR]
    SHIP_CLASS = 4
    SHIELD_LINK = 'cv_fighter_shield01'
    ENGINE_TYPE = ENGINE_SINGLE
    LIGHTS = 7

    ARCHETYPE = 'ge_fighter2'
    RU_NAME = MS('Стартрекер', 'Startracker')
    TEMPLATE_CODE = 'gf2'
    ICON = 'cv_startracker.3db'
    HP_TORPEDO = 'HpTorpedo02'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03, HpTorpedo01']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02']

    # mk 2
    # HP_TORPEDO = 'HpTorpedo01'
    # MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05']
    # MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03']


class Starblazer(GenericShip, ShipElite, Ship2, Ship):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_GENERIC_ELITE]
    SHIP_CLASS = 4
    SHIELD_LINK = 'cv_fighter_shield01'
    ENGINE_TYPE = ENGINE_DOUBLE_SAME
    LIGHTS = 7

    ARCHETYPE = 'ge_fighter3'
    RU_NAME = MS('Старблейзер', 'Starblazer')
    TEMPLATE_CODE = 'gf3'
    ICON = 'cv_starblazer.3db'
    HP_TORPEDO = 'HpWeapon04'
    MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon05', 'HpWeapon06']
    MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03']

    # mk2
    # HP_TORPEDO = 'HpTorpedo02'
    # MAIN_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04', 'HpWeapon05', 'HpWeapon06']
    # MAX_WEAPONS = ['HpWeapon01', 'HpWeapon02', 'HpWeapon03', 'HpWeapon04']
