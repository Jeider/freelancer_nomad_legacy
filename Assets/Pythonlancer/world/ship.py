from world.equipment import Equipment
from world.npc import NPC
import math

DIVIDER = "\n"
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


class Ship(object):
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

    THRUSTERS = 'HpThruster01, HpThruster02'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04, HpWeapon05, HpWeapon06'
    MAX_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04'

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
        return DIVIDER.join(lines)

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
                lines.append(self.build_weapon_equip_line(equipment_class, self.MAX_WEAPONS))
            else:
                lines.append(self.build_weapon_equip_line(equipment_class, self.MAIN_WEAPONS))

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
            lines.append(self.build_equip_line(self.THRUSTER_CLASS, self.THRUSTERS))

        lines.append(self.build_equip_line(self.MINE_CLASS, self.HP_MINE))
        lines.append(self.build_equip_line(self.CM_CLASS, self.HP_CM))

        return lines

    def get_equipment_table(self):
        lines = self.get_weapon_lines() + self.get_torpedo_lines() + self.get_misc_equip_lines() + self.get_generic_equip_lines()
        return DIVIDER.join(lines)

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
        return math.ceil(self.MAX_HIT_PTS * self.HIT_PTS_MULTIPLER_PER_INDEX[self.SHIP_INDEX] * self.HULL_HIT_PTS_MULTIPLER)

    def get_bots_count(self):
        return math.ceil(((self.get_hit_pts() * NUM_REPAIRS) / BOT_REPAIR) * self.NANOBOTS_COUNT_MULTIPLER)

    def get_base_template_params(self):
        return {
            self.ship_param('shield_link'): self.HP_SHIELD,
            self.ship_param('mass'): self.get_ship_mass(),
            self.ship_param('hold_size'): self.get_hold_size(),
            self.ship_param('strafe_force'): self.get_strafe_force(),
            self.ship_param('strafe_power_usage'): self.get_strafe_force_power_usage(),
            self.ship_param('nanobot'): self.get_bots_count(),
            self.ship_param('hit_pts'): self.get_hit_pts(),
            self.ship_param('fuses'): self.get_fuses(),
            self.ship_param('equipment'): self.get_equipment_table(),
        }

    def get_collision_group_template_params(self):
        params = {}

        for name, hit_pts_pct in self.COLLISION_HIT_PTS_PERCENT.items():
            params[name] = self.get_hit_pts() * hit_pts_pct

        for name, resistance in self.COLLISION_EXPLOSION_RESISTANCE.items():
            params[name] = resistance

        return params

    def get_shiparch_params(self):
        params = {}
        params.update(self.get_base_template_params())
        params.update(self.get_collision_group_template_params())
        return params

    @staticmethod
    def get_extra_content(torpedo, cm, mine, torpedo_ammo, cm_ammo, mine_ammo):
        extra = []
        if torpedo:
            extra.append(Ship.EQUIP_TEMPLATE, format(torpedo, Ship.HP_TORPEDO))
            if torpedo_ammo:
                extra.append(Ship.CARGO_TEMPLATE, format(torpedo, torpedo_ammo))

        if cm:
            extra.append(Ship.EQUIP_TEMPLATE, format(cm, Ship.HP_CM))
            if cm_ammo:
                extra.append(Ship.CARGO_TEMPLATE, format(torpedo, cm_ammo))

        if mine:
            extra.append(Ship.EQUIP_TEMPLATE, format(mine, Ship.HP_MINE))
            if mine_ammo:
                extra.append(Ship.CARGO_TEMPLATE, format(torpedo, mine_ammo))

        return DIVIDER.join(extra)


class BaseInterceptorShip(Ship):
    MAX_HIT_PTS = 12000

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


class BaseFighterShip(Ship):
    MAX_HIT_PTS = 10000

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


class BaseFreighterShip(Ship):
    MAX_HIT_PTS = 14000

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


class RheinlandShip(Ship):
    # MAIN
    SHIP_MASS_MULTIPLER = 0.66
    CARGO_HOLD_MULTIPLER = 0.84
    EXTRA_CARGO = -3
    # ADDITIONAL
    HULL_HIT_PTS_MULTIPLER = 1.02
    STRAFE_FORCE_MULTIPLER = 0.9


class LibertyShip(Ship):
    # MAIN
    HULL_HIT_PTS_MULTIPLER = 0.83
    # ADDITIONAL
    STRAFE_POWER_USAGE_MULTIPLER = 1.5
    NANOBOTS_COUNT_MULTIPLER = 1.1


class BretoniaShip(Ship):
    # MAIN
    HULL_HIT_PTS_MULTIPLER = 1.15
    # ADDITIONAL
    EXTRA_CARGO = 2
    STRAFE_FORCE_MULTIPLER = 0.95
    SHIP_MASS_MULTIPLER = 1.1


class KusariShip(Ship):
    # MAIN
    NANOBOTS_COUNT_MULTIPLER = 1.5
    STRAFE_FORCE_MULTIPLER = 0.5
    STRAFE_POWER_USAGE_MULTIPLER = 0
    # ADDITIONAL
    HULL_HIT_PTS_MULTIPLER = 0.95
    EXTRA_CARGO = -1


class CorsairShip(Ship):
    # MAIN
    CARGO_HOLD_MULTIPLER = 1.1
    NANOBOTS_COUNT_MULTIPLER = 0.5
    # ADDITIONAL
    HULL_HIT_PTS_MULTIPLER = 1.06


class GenericShip(Ship):
    # MAIN
    HULL_HIT_PTS_MULTIPLER = 0.92
    # ADDITIONAL
    EXTRA_CARGO = -1
    STRAFE_POWER_USAGE_MULTIPLER = 1.1
    SHIP_MASS_MULTIPLER = 1.05


class Ship1(object):
    NPC_LEVELS = NPC.SHIP1_LEVELS


class Ship2(object):
    NPC_LEVELS = NPC.SHIP2_LEVELS


class Ship3(object):
    NPC_LEVELS = NPC.SHIP3_LEVELS


class ShipInterceptor(BaseInterceptorShip):
    SHIPCLASS_NAME = 'interceptor'
    EQUIPMENT_SHIPCLASS = Equipment.SHIPCLASS_FIGHTER
    EXTRA_CLASSES = [CLASS_INTERCEPTOR]
    TORPEDO_CLASSES = [Ship.TORPEDO_CD_CLASS]

    SHIELD_CLASS_TEMPLATE = 'hp_fighter_shield_special_{class_digit}'
    ENGINE_CLASS_TEMPLATE = 'hp_fighter_engine_special_{class_digit}'
    POWERPLANT_CLASS_TEMPLATE = 'hp_fighter_power_special_{class_digit}'


class ShipFighter(BaseFighterShip):
    SHIPCLASS_NAME = 'fighter'
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


class Dagger(RheinlandShip, ShipInterceptor, Ship1):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_RHEINLAND_INTERCEPTOR]
    SHIP_INDEX = SHIP_INDEX_3

    ARCHETYPE = 'bw_fighter'
    TEMPLATE_CODE = 'bwf'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04'
    MAX_WEAPONS = 'HpWeapon01, HpWeapon02'

    # mk2 
    # HP_TORPEDO = 'HpTorpedo01'
    # MAIN_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04, HpTurret01'
    # MAX_WEAPONS = 'HpWeapon01, HpWeapon02, HpTurret01'

    SHIP_TEMPLATE = '''[Loadout]
nickname = {loadout_nickname}
archetype = {ship_archetype}
equip = launch_extend
equip = {engine}
equip = infinite_power
cargo = {power}, 1
equip = {scanner}
equip = {tractor}
equip = {armor}
equip = {shield_npc}, HpShield01
cargo = {shield}, 1
equip = {weapon1}, HpWeapon01
equip = {weapon2}, HpWeapon02
equip = {weapon3}, HpWeapon03
equip = {weapon4}, HpWeapon04
equip = {afterburn1}, HpThruster01
equip = {afterburn2}, HpThruster02
equip = LargeWhiteSpecial, HpHeadlight
equip = {small_light}, HpRunningLight01
equip = {small_light}, HpRunningLight02
equip = {small_light}, HpRunningLight03
equip = {small_light}, HpRunningLight04
equip = {small_light}, HpRunningLight05
equip = {small_light}, HpRunningLight08
equip = DockingLightRedSmall, HpDockLight01
equip = DockingLightRedSmall, HpDockLight02
equip = {contrail}, HpContrail01
equip = {contrail}, HpContrail02
equip = {contrail}, HpContrail03
equip = {contrail}, HpContrail04
equip = single_eng_force, HpEngine01
equip = single_eng_weight, HpCockpit
{extra}'''

    COLLISION_HIT_PTS_PERCENT = {
        'bwf_wing_hit_pts': HP_PCT_WING,
        'bwf_engine_hit_pts': HP_PCT_ENGINE_SINGLE,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'bwf_wing_expl_resist': EXPL_RESIST_WING,
        'bwf_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Banshee(RheinlandShip, ShipInterceptor, Ship2):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_RHEINLAND_INTERCEPTOR]
    SHIP_INDEX = SHIP_INDEX_7

    ARCHETYPE = 'rh_fighter'
    TEMPLATE_CODE = 'rf'
    HP_TORPEDO = 'HpTorpedo02'
    MAIN_WEAPONS = 'HpTorpedo01, HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04'
    MAX_WEAPONS = 'HpTorpedo01, HpWeapon03, HpWeapon04'

    SHIP_TEMPLATE = '''[Loadout]
nickname = {loadout_nickname}
archetype = {ship_archetype}
equip = launch_extend
equip = {engine}
equip = infinite_power
cargo = {power}, 1
equip = {scanner}
equip = {tractor}
equip = {armor}
equip = {shield_npc}, HpShield01
cargo = {shield}, 1
equip = {weapon1}, HpWeapon01
equip = {weapon2}, HpWeapon02
equip = {weapon3}, HpWeapon03
equip = {weapon4}, HpWeapon04
equip = {afterburn1}, HpThruster01
equip = {afterburn2}, HpThruster02
equip = LargeWhiteSpecial, HpHeadlight
equip = {small_light}, HpRunningLight01
equip = {small_light}, HpRunningLight02
equip = {small_light}, HpRunningLight03
equip = {small_light}, HpRunningLight04
equip = {small_light}, HpRunningLight05
equip = {small_light}, HpRunningLight06
equip = DockingLightRedSmall, HpDockLight01
equip = DockingLightRedSmall, HpDockLight02
equip = {contrail}, HpContrail01
equip = {contrail}, HpContrail02
equip = {contrail}, HpContrail03
equip = {contrail}, HpContrail04
equip = single_eng_force, HpEngine01
equip = single_eng_weight, HpCockpit
{extra}'''

    COLLISION_HIT_PTS_PERCENT = {
        'rf_wing_hit_pts': HP_PCT_WING,
        'rf_engine_hit_pts': HP_PCT_ENGINE_SINGLE, 
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'rf_wing_expl_resist': EXPL_RESIST_WING,
        'rf_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Stiletto(RheinlandShip, ShipFighter, Ship1):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_RHEINLAND_ELITE, CLASS_RHEINLAND_FIGHTER_ONLY]
    SHIP_INDEX = SHIP_INDEX_3

    ARCHETYPE = 'bw_elite'
    TEMPLATE_CODE = 'bwe'
    HP_TORPEDO = 'HpWeapon06'
    MAIN_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04, HpWeapon05'
    MAX_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03'

    # mk2: minds??

    # HP_TORPEDO = 'HpTorpedo01'
    # MAIN_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04, HpWeapon05, HpWeapon06'
    # MAX_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04'

    SHIP_TEMPLATE = '''[Loadout]
nickname = {loadout_nickname}
archetype = {ship_archetype}
equip = launch_extend
equip = {engine}
equip = infinite_power
cargo = {power}, 1
equip = {scanner}
equip = {tractor}
equip = {armor}
equip = {shield_npc}, HpTurret01
cargo = {shield}, 1
equip = {weapon1}, HpWeapon01
equip = {weapon2}, HpWeapon02
equip = {weapon3}, HpWeapon03
equip = {weapon4}, HpWeapon04
equip = {weapon5}, HpWeapon05
equip = {weapon6}, HpWeapon06
equip = {afterburn1}, HpThruster01
equip = {afterburn2}, HpShield01
equip = LargeWhiteSpecial, HpHeadlight
equip = {small_light}, HpRunningLight01
equip = {small_light}, HpRunningLight02
equip = {small_light}, HpRunningLight03
equip = {small_light}, HpRunningLight04
equip = {small_light}, HpRunningLight05
equip = {small_light}, HpRunningLight06
equip = {small_light}, HpRunningLight07
equip = {small_light}, HpRunningLight08
equip = DockingLightRedSmall, HpDockLight01
equip = DockingLightRedSmall, HpDockLight02
equip = {contrail}, HpContrail01
equip = {contrail}, HpContrail02
equip = {contrail}, HpContrail03
equip = {contrail}, HpContrail04
equip = double_same_eng_force, HpEngine01
equip = double_same_eng_force, HpEngine02
equip = double_eng_weight, HpCockpit
{extra}'''

    COLLISION_HIT_PTS_PERCENT = {
        'bwe_wing1_hit_pts': HP_PCT_WING,
        'bwe_wing2_hit_pts': HP_PCT_WING,
        'bwe_engine1_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
        'bwe_engine2_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'bwe_wing1_expl_resist': EXPL_RESIST_WING,
        'bwe_wing2_expl_resist': EXPL_RESIST_WING,
        'bwe_engine1_expl_resist': EXPL_RESIST_ENGINE,
        'bwe_engine2_expl_resist': EXPL_RESIST_ENGINE,
    }


class Sabre(RheinlandShip, ShipFighter, Ship2):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_RHEINLAND_ELITE, CLASS_RHEINLAND_FIGHTER_ONLY]
    SHIP_INDEX = SHIP_INDEX_7

    ARCHETYPE = 'bw_elite2'
    TEMPLATE_CODE = 'bwe2'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04, HpWeapon05, HpWeapon06'
    MAX_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04'

    SHIP_TEMPLATE = '''[Loadout]
nickname = {loadout_nickname}
archetype = {ship_archetype}
equip = launch_extend
equip = {engine}
equip = infinite_power
cargo = {power}, 1
equip = {scanner}
equip = {tractor}
equip = {armor}
equip = {shield_npc}, HpTurret01
cargo = {shield}, 1
equip = {weapon1}, HpWeapon01
equip = {weapon2}, HpWeapon02
equip = {weapon3}, HpWeapon03
equip = {weapon4}, HpWeapon04
equip = {weapon5}, HpWeapon05
equip = {weapon6}, HpWeapon06
equip = {afterburn1}, HpThruster01
equip = {afterburn2}, HpShield01
equip = LargeWhiteSpecial, HpHeadlight
equip = {small_light}, HpRunningLight01
equip = {small_light}, HpRunningLight02
equip = {small_light}, HpRunningLight03
equip = {small_light}, HpRunningLight04
equip = {small_light}, HpRunningLight05
equip = {small_light}, HpRunningLight06
equip = {small_light}, HpRunningLight07
equip = {small_light}, HpRunningLight08
equip = DockingLightRedSmall, HpDockLight01
equip = DockingLightRedSmall, HpDockLight02
equip = {contrail}, HpContrail01
equip = {contrail}, HpContrail02
equip = {contrail}, HpContrail03
equip = {contrail}, HpContrail04
equip = double_same_eng_force, HpEngine01
equip = double_same_eng_force, HpEngine02
equip = double_eng_weight, HpCockpit
{extra}'''

    COLLISION_HIT_PTS_PERCENT = {
        'bwe2_wing1_hit_pts': HP_PCT_WING,
        'bwe2_wing2_hit_pts': HP_PCT_WING,
        'bwe2_engine1_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
        'bwe2_engine2_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'bwe2_wing1_expl_resist': EXPL_RESIST_WING,
        'bwe2_wing2_expl_resist': EXPL_RESIST_WING,
        'bwe2_engine1_expl_resist': EXPL_RESIST_ENGINE,
        'bwe2_engine2_expl_resist': EXPL_RESIST_ENGINE,
    }


class Valkyrie(RheinlandShip, ShipElite, Ship3):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_RHEINLAND_ELITE]
    SHIP_INDEX = SHIP_INDEX_8

    ARCHETYPE = 'rh_elite'
    TEMPLATE_CODE = 're'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04, HpWeapon05, HpWeapon06'
    MAX_WEAPONS = 'HpWeapon03, HpWeapon04, HpWeapon05, HpWeapon06'

    SHIP_TEMPLATE = '''[Loadout]
nickname = {loadout_nickname}
archetype = {ship_archetype}
equip = launch_extend
equip = {engine}
equip = infinite_power
cargo = {power}, 1
equip = {scanner}
equip = {tractor}
equip = {armor}
equip = {shield_npc}, HpShield01
cargo = {shield}, 1
equip = {weapon1}, HpWeapon01
equip = {weapon2}, HpWeapon02
equip = {weapon3}, HpWeapon03
equip = {weapon4}, HpWeapon04
equip = {weapon5}, HpWeapon05
equip = {weapon6}, HpWeapon06
equip = {afterburn1}, HpThruster01
equip = {afterburn2}, HpThruster02
equip = LargeWhiteSpecial, HpHeadlight
equip = {small_light}, HpRunningLight01
equip = {small_light}, HpRunningLight02
equip = {small_light}, HpRunningLight03
equip = {small_light}, HpRunningLight04
equip = {small_light}, HpRunningLight05
equip = {small_light}, HpRunningLight06
equip = DockingLightRedSmall, HpDockLight01
equip = DockingLightRedSmall, HpDockLight02
equip = {contrail}, HpContrail01
equip = {contrail}, HpContrail02
equip = {contrail}, HpContrail03
equip = {contrail}, HpContrail04
equip = double_same_eng_force, HpEngine01
equip = double_same_eng_force, HpEngine02
equip = double_eng_weight, HpCockpit
{extra}'''

    COLLISION_HIT_PTS_PERCENT = {
        're_wing_hit_pts': HP_PCT_WING,
        're_tail_hit_pts': HP_PCT_TAIL,
        're_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        're_wing_expl_resist': EXPL_RESIST_WING,
        're_tail_expl_resist': EXPL_RESIST_WING,
        're_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class ValkyrieMk2(RheinlandShip, ShipElite, Ship3):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_RHEINLAND_ELITE]
    SHIP_INDEX = SHIP_INDEX_10

    ARCHETYPE = 'rh_elite2'
    TEMPLATE_CODE = 're2'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04, HpWeapon05, HpWeapon06'
    MAX_WEAPONS = 'HpWeapon03, HpWeapon04, HpWeapon05, HpWeapon06'

    COLLISION_HIT_PTS_PERCENT = {
        're2_wing_hit_pts': HP_PCT_WING,
        're2_tail_hit_pts': HP_PCT_TAIL,
        're2_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        're2_wing_expl_resist': EXPL_RESIST_WING,
        're2_tail_expl_resist': EXPL_RESIST_WING,
        're2_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Humpback(RheinlandShip, ShipFreighter):
    ARCHETYPE = 'rh_freighter'
    SHIP_INDEX = SHIP_INDEX_6

    TEMPLATE_CODE = 'rfr'
    MAIN_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon05, HpWeapon06, HpWeapon10'
    MAX_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon05, HpWeapon06'

    COLLISION_HIT_PTS_PERCENT = {
        'rfr_panel_hit_pts': HP_PCT_WING,
        'rfr_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'rfr_panel_expl_resist': EXPL_RESIST_WING,
        'rfr_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


# LIBERTY


class Piranha(LibertyShip, ShipInterceptor, Ship1):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_LIBERTY_INTERCEPTOR]
    SHIP_INDEX = SHIP_INDEX_3

    ARCHETYPE = 'bh_fighter'
    TEMPLATE_CODE = 'bhf'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04'
    MAX_WEAPONS = 'HpWeapon03, HpWeapon04'

    COLLISION_HIT_PTS_PERCENT = {
        'bhf_fin_hit_pts': HP_PCT_FIN,
        'bhf_engine_hit_pts': HP_PCT_ENGINE_SINGLE,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'bhf_fin_expl_resist': EXPL_RESIST_MISC,
        'bhf_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Patriot(LibertyShip, ShipInterceptor, Ship2):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_LIBERTY_INTERCEPTOR]
    SHIP_INDEX = SHIP_INDEX_7

    ARCHETYPE = 'li_fighter'
    TEMPLATE_CODE = 'lf'
    HP_TORPEDO = 'HpTorpedo02'
    MAIN_WEAPONS = 'HpTorpedo01, HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04'
    MAX_WEAPONS = 'HpWeapon03, HpWeapon04'

    COLLISION_HIT_PTS_PERCENT = {
        'lf_fin_hit_pts': HP_PCT_FIN,
        'lf_engine_hit_pts': HP_PCT_ENGINE_SINGLE,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'lf_fin_expl_resist': EXPL_RESIST_MISC,  
        'lf_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Barracuda(LibertyShip, ShipFighter, Ship1):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_LIBERTY_ELITE, CLASS_LIBERTY_FIGHTER_ONLY]
    SHIP_INDEX = SHIP_INDEX_3

    ARCHETYPE = 'bh_elite'
    TEMPLATE_CODE = 'bhe'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04, HpWeapon05'
    MAX_WEAPONS = 'HpWeapon03, HpWeapon04, HpWeapon05'

    # mk 2
    # HP_TORPEDO = 'HpTorpedo02'
    # MAIN_WEAPONS = 'HpTorpedo01, HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04, HpWeapon05'
    # MAX_WEAPONS = 'HpTorpedo01, HpWeapon03, HpWeapon04, HpWeapon05'

    COLLISION_HIT_PTS_PERCENT = {
        'bhe_fin1_hit_pts': HP_PCT_FIN,
        'bhe_fin2_hit_pts': HP_PCT_FIN_WITH_ENGINE,
        'bhe_wing_hit_pts': HP_PCT_WING,
        'bhe_engine1_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
        'bhe_engine2_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'bhe_fin1_expl_resist': EXPL_RESIST_MISC,
        'bhe_fin2_expl_resist': EXPL_RESIST_MISC,
        'bhe_wing_expl_resist': EXPL_RESIST_WING,
        'bhe_engine1_expl_resist': EXPL_RESIST_ENGINE,
        'bhe_engine2_expl_resist': EXPL_RESIST_ENGINE,
    }


class Hammerhead(LibertyShip, ShipFighter, Ship2):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_LIBERTY_ELITE, CLASS_LIBERTY_FIGHTER_ONLY]
    SHIP_INDEX = SHIP_INDEX_7

    ARCHETYPE = 'bh_elite2'
    TEMPLATE_CODE = 'bhe2'
    HP_TORPEDO = 'HpWeapon06'
    MAIN_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04, HpWeapon05, HpWeapon07'
    MAX_WEAPONS = 'HpWeapon03, HpWeapon04, HpWeapon05, HpWeapon07'

    COLLISION_HIT_PTS_PERCENT = {
        'bhe2_fin1_hit_pts': HP_PCT_FIN,
        'bhe2_fin2_hit_pts': HP_PCT_FIN_WITH_ENGINE,
        'bhe2_wing_hit_pts': HP_PCT_WING,
        'bhe2_engine1_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
        'bhe2_engine2_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'bhe2_fin1_expl_resist': EXPL_RESIST_MISC,
        'bhe2_fin2_expl_resist': EXPL_RESIST_MISC,
        'bhe2_wing_expl_resist': EXPL_RESIST_WING,
        'bhe2_engine1_expl_resist': EXPL_RESIST_ENGINE,
        'bhe2_engine2_expl_resist': EXPL_RESIST_ENGINE,
    }


class Defender(LibertyShip, ShipElite, Ship3):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_LIBERTY_ELITE]
    SHIP_INDEX = SHIP_INDEX_8

    ARCHETYPE = 'li_elite'
    TEMPLATE_CODE = 'le'
    HP_TORPEDO = 'HpTorpedo02'
    MAIN_WEAPONS = 'HpTorpedo01, HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04, HpWeapon05'
    MAX_WEAPONS = 'HpTorpedo01, HpWeapon03, HpWeapon04'

    COLLISION_HIT_PTS_PERCENT = {
        'le_wing_hit_pts': HP_PCT_WING,
        'le_spoiler_hit_pts': HP_PCT_TAIL,
        'le_engine1_hit_pts': HP_PCT_ENGINE_DOUBLE_MAIN,
        'le_engine2_hit_pts': HP_PCT_ENGINE_DOUBLE_SECOND,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'le_wing_expl_resist': EXPL_RESIST_WING,
        'le_spoiler_expl_resist': EXPL_RESIST_WING,
        'le_engine1_expl_resist': EXPL_RESIST_ENGINE,
        'le_engine2_expl_resist': EXPL_RESIST_ENGINE,
    }


class DefenderJuni(LibertyShip, ShipElite, Ship3):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_LIBERTY_ELITE]
    SHIP_INDEX = SHIP_INDEX_10

    ARCHETYPE = 'li_elite2'
    TEMPLATE_CODE = 'le2'
    HP_TORPEDO = 'HpTorpedo02'
    MAIN_WEAPONS = 'HpTorpedo01, HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04, HpWeapon05'
    MAX_WEAPONS = 'HpTorpedo01, HpWeapon03, HpWeapon04'

    COLLISION_HIT_PTS_PERCENT = {
        'le2_wing_hit_pts': HP_PCT_WING,
        'le2_spoiler_hit_pts': HP_PCT_TAIL,
        'le2_engine1_hit_pts': HP_PCT_ENGINE_DOUBLE_MAIN,
        'le2_engine2_hit_pts': HP_PCT_ENGINE_DOUBLE_SECOND,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'le2_wing_expl_resist': EXPL_RESIST_WING,
        'le2_spoiler_expl_resist': EXPL_RESIST_WING,
        'le2_engine1_expl_resist': EXPL_RESIST_ENGINE,
        'le2_engine2_expl_resist': EXPL_RESIST_ENGINE,
    }


class Rhino(LibertyShip, ShipFreighter):
    ARCHETYPE = 'li_freighter'
    SHIP_INDEX = SHIP_INDEX_6

    TEMPLATE_CODE = 'lfr'
    MAIN_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpTurret01, HpTurret02, HpTurret03'
    MAX_WEAPONS = 'HpWeapon02, HpWeapon03, HpTurret01, HpTurret02'

    COLLISION_HIT_PTS_PERCENT = {
        'lfr_panel_hit_pts': HP_PCT_WING,
        'lfr_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'lfr_panel_expl_resist': EXPL_RESIST_WING,
        'lfr_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


# BRETONIA


class Legionnaire(BretoniaShip, ShipInterceptor, Ship1):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_BRETONIA_INTERCEPTOR]
    SHIP_INDEX = SHIP_INDEX_3

    ARCHETYPE = 'co_fighter'
    TEMPLATE_CODE = 'cf'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04'
    MAX_WEAPONS = 'HpWeapon03, HpWeapon04'

    COLLISION_HIT_PTS_PERCENT = {
        'cf_wing_hit_pts': HP_PCT_WING,
        'cf_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'cf_wing_expl_resist': EXPL_RESIST_WING,
        'cf_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Cavalier(BretoniaShip, ShipInterceptor, Ship2):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_BRETONIA_INTERCEPTOR]
    SHIP_INDEX = SHIP_INDEX_7

    ARCHETYPE = 'br_fighter'
    TEMPLATE_CODE = 'bf'
    HP_TORPEDO = 'HpTorpedo02'
    MAIN_WEAPONS = 'HpTorpedo01, HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04'
    MAX_WEAPONS = 'HpTorpedo01, HpWeapon03, HpWeapon04'

    COLLISION_HIT_PTS_PERCENT = {
        'bf_tail_hit_pts': HP_PCT_TAIL,
        'bf_engine_hit_pts': HP_PCT_ENGINE_SINGLE,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'bf_tail_expl_resist': EXPL_RESIST_WING,
        'bf_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Centurion(BretoniaShip, ShipFighter, Ship1):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_BRETONIA_ELITE, CLASS_BRETONIA_FIGHTER_ONLY]
    SHIP_INDEX = SHIP_INDEX_3

    ARCHETYPE = 'co_elite'
    TEMPLATE_CODE = 'ce'
    HP_TORPEDO = 'HpTorpedo02'
    MAIN_WEAPONS = 'HpTorpedo01, HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04'
    MAX_WEAPONS = 'HpTorpedo01, HpWeapon03, HpWeapon04'

    # mk 2 version
    # HP_TORPEDO = 'HpTorpedo01'
    # MAIN_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04, HpWeapon05, HpWeapon06'
    # MAX_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04'

    COLLISION_HIT_PTS_PERCENT = {
        'ce_wing_hit_pts': HP_PCT_WING,
        'ce_fin_hit_pts': HP_PCT_FIN,
        'ce_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'ce_wing_expl_resist': EXPL_RESIST_WING,
        'ce_fin_expl_resist': EXPL_RESIST_MISC,
        'ce_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Titan(BretoniaShip, ShipFighter, Ship2):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_BRETONIA_ELITE, CLASS_BRETONIA_FIGHTER_ONLY]
    SHIP_INDEX = SHIP_INDEX_7

    ARCHETYPE = 'co_elite2'
    TEMPLATE_CODE = 'ce2'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04, HpWeapon05, HpWeapon06'
    MAX_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04'

    # mk 2
    # HP_TORPEDO = 'HpTorpedo02'
    # MAIN_WEAPONS = 'HpTorpedo01, HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04, HpWeapon05, HpWeapon06'
    # MAX_WEAPONS = 'HpTorpedo01, HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04'

    COLLISION_HIT_PTS_PERCENT = {
        'ce2_wing_hit_pts': HP_PCT_WING,
        'ce2_fin_hit_pts': HP_PCT_FIN,
        'ce2_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'ce2_wing_expl_resist': EXPL_RESIST_WING,
        'ce2_fin_expl_resist': EXPL_RESIST_MISC,
        'ce2_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Crusader(BretoniaShip, ShipElite, Ship3):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_BRETONIA_ELITE]
    SHIP_INDEX = SHIP_INDEX_8

    ARCHETYPE = 'br_elite'
    TEMPLATE_CODE = 'be'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04, HpWeapon05, HpWeapon06'
    MAX_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon05, HpWeapon06'

    COLLISION_HIT_PTS_PERCENT = {
        'be_wing_hit_pts': HP_PCT_WING,
        'be_tail_hit_pts': HP_PCT_TAIL,
        'be_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'be_wing_expl_resist': EXPL_RESIST_WING,
        'be_tail_expl_resist': EXPL_RESIST_WING,
        'be_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class CrusaderMk2(BretoniaShip, ShipElite, Ship3):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_BRETONIA_ELITE]
    SHIP_INDEX = SHIP_INDEX_10

    ARCHETYPE = 'br_elite2'
    TEMPLATE_CODE = 'be2'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04, HpWeapon05, HpWeapon06'
    MAX_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon05, HpWeapon06'

    COLLISION_HIT_PTS_PERCENT = {
        'be2_wing_hit_pts': HP_PCT_WING,
        'be2_tail_hit_pts': HP_PCT_TAIL,
        'be2_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME, 
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'be2_wing_expl_resist': EXPL_RESIST_WING,
        'be2_tail_expl_resist': EXPL_RESIST_WING,
        'be2_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Clydesdale(BretoniaShip, ShipFreighter):
    ARCHETYPE = 'br_freighter'

    SHIP_INDEX = SHIP_INDEX_6

    TEMPLATE_CODE = 'bfr'
    MAIN_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpTurret01, HpTurret02, HpTurret03'
    MAX_WEAPONS = 'HpWeapon02, HpWeapon03, HpTurret01, HpTurret02'

    COLLISION_HIT_PTS_PERCENT = {
        'bfr_wing_hit_pts': HP_PCT_WING,
        'bfr_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'bfr_wing_expl_resist': EXPL_RESIST_WING,
        'bfr_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


# KUSARI


class Hawk(KusariShip, ShipInterceptor, Ship1):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_KUSARI_INTERCEPTOR]
    SHIP_INDEX = SHIP_INDEX_3

    ARCHETYPE = 'ge_fighter4'
    TEMPLATE_CODE = 'gf4'
    HP_TORPEDO = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'gf4_wing_hit_pts': HP_PCT_WING,
        'gf4_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'gf4_wing_expl_resist': EXPL_RESIST_WING,
        'gf4_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Drake(KusariShip, ShipInterceptor, Ship2):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_KUSARI_INTERCEPTOR]
    SHIP_INDEX = SHIP_INDEX_7

    ARCHETYPE = 'ku_fighter'
    TEMPLATE_CODE = 'kf'
    HP_TORPEDO = 'HpTorpedo02'
    MAIN_WEAPONS = 'HpTorpedo01, HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04'
    MAX_WEAPONS = 'HpWeapon01, HpWeapon02'

    COLLISION_HIT_PTS_PERCENT = {
        'kf_wing_hit_pts': HP_PCT_WING,
        'kf_engine_hit_pts': HP_PCT_ENGINE_SINGLE,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'kf_wing_expl_resist': EXPL_RESIST_WING,
        'kf_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Falcon(KusariShip, ShipFighter, Ship1):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_KUSARI_ELITE, CLASS_KUSARI_FIGHTER_ONLY]
    SHIP_INDEX = SHIP_INDEX_3

    ARCHETYPE = 'ge_fighter5'
    TEMPLATE_CODE = 'gf5'
    HP_TORPEDO = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'gf5_wing_hit_pts': HP_PCT_WING,
        'gf5_fin_hit_pts': HP_PCT_FIN,
        'gf5_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'gf5_wing_expl_resist': EXPL_RESIST_WING,
        'gf5_fin_expl_resist': EXPL_RESIST_MISC,
        'gf5_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Eagle(KusariShip, ShipFighter, Ship2):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_KUSARI_ELITE, CLASS_KUSARI_FIGHTER_ONLY]
    SHIP_INDEX = SHIP_INDEX_7

    ARCHETYPE = 'ge_fighter6'
    TEMPLATE_CODE = 'gf6'

    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04, HpWeapon05, HpWeapon06'
    MAX_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04'

    # HP_SHIELD = 'HpShield02'
    # HP_TORPEDO = 'HpTorpedo01'
    # MAIN_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04, HpWeapon05, HpWeapon06, HpWeapon07'
    # MAX_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04, HpWeapon07'

    COLLISION_HIT_PTS_PERCENT = {
        'gf6_wing_hit_pts': HP_PCT_WING,
        'gf6_fin_hit_pts': HP_PCT_FIN,
        'gf6_btmwing_hit_pts': HP_PCT_WING,
        'gf6_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'gf6_wing_expl_resist': EXPL_RESIST_WING,
        'gf6_fin_expl_resist': EXPL_RESIST_MISC,
        'gf6_btmwing_expl_resist': EXPL_RESIST_WING,
        'gf6_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Dragon(KusariShip, ShipElite, Ship3):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_KUSARI_ELITE]
    SHIP_INDEX = SHIP_INDEX_8

    ARCHETYPE = 'ku_elite'
    TEMPLATE_CODE = 'ke'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04, HpWeapon05, HpWeapon06'
    MAX_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon05, HpWeapon06'

    COLLISION_HIT_PTS_PERCENT = {
        'ke_wing_hit_pts': HP_PCT_MISC,
        'ke_tail_hit_pts': HP_PCT_TAIL,
        'ke_spike_hit_pts': HP_PCT_WING,
        'ke_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'ke_wing_expl_resist': EXPL_RESIST_MISC,
        'ke_tail_expl_resist': EXPL_RESIST_WING,
        'ke_spike_expl_resist': EXPL_RESIST_WING,
        'ke_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class DragonMk2(KusariShip, ShipElite, Ship3):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_KUSARI_ELITE]
    SHIP_INDEX = SHIP_INDEX_10

    ARCHETYPE = 'ku_elite2'
    TEMPLATE_CODE = 'ke2'
    HP_TORPEDO = 'HpTorpedo01'
    MAIN_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon04, HpWeapon05, HpWeapon06'
    MAX_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon05, HpWeapon06'

    COLLISION_HIT_PTS_PERCENT = {
        'ke2_wing_hit_pts': HP_PCT_MISC,
        'ke2_tail_hit_pts': HP_PCT_TAIL,
        'ke2_spike_hit_pts': HP_PCT_WING,
        'ke2_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'ke2_wing_expl_resist': EXPL_RESIST_MISC,
        'ke2_tail_expl_resist': EXPL_RESIST_WING,
        'ke2_spike_expl_resist': EXPL_RESIST_WING,
        'ke2_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Dron(KusariShip, ShipFreighter):
    ARCHETYPE = 'ku_freighter'

    SHIP_INDEX = SHIP_INDEX_6

    TEMPLATE_CODE = 'kfr'
    MAIN_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon03, HpTurret01, HpTurret02'
    MAX_WEAPONS = 'HpWeapon01, HpWeapon02, HpWeapon03, HpWeapon03'

    COLLISION_HIT_PTS_PERCENT = {
        'kfr_wing_hit_pts': HP_PCT_WING,
        'kfr_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'kfr_wing_expl_resist': EXPL_RESIST_MISC,
        'kfr_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


# CORSAIR / ORDER


class Bloodhound(CorsairShip, ShipFighter, Ship1):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_CORSAIR_ELITE, CLASS_CORSAIR_FIGHTER_ONLY]
    SHIP_INDEX = SHIP_INDEX_3

    ARCHETYPE = 'pi_fighter'
    TEMPLATE_CODE = 'pf'
    HP_TORPEDO = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'pf_fin_hit_pts': HP_PCT_FIN,
        'pf_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'pf_fin_expl_resist': EXPL_RESIST_MISC,
        'pf_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Wolfhound(CorsairShip, ShipFighter, Ship2):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_CORSAIR_ELITE, CLASS_CORSAIR_FIGHTER_ONLY]
    SHIP_INDEX = SHIP_INDEX_7

    ARCHETYPE = 'pi_elite'
    TEMPLATE_CODE = 'pe'
    HP_TORPEDO = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'pe_fin_hit_pts': HP_PCT_FIN,
        'pe_engine_hit_pts': HP_PCT_ENGINE_TRIPLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'pe_fin_expl_resist': EXPL_RESIST_MISC,
        'pe_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Anubis(CorsairShip, ShipElite, Ship3):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_CORSAIR_ELITE]
    SHIP_INDEX = SHIP_INDEX_8

    ARCHETYPE = 'or_elite'
    TEMPLATE_CODE = 'oe'
    HP_TORPEDO = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'oe_wing_hit_pts': HP_PCT_WING,
        'oe_engine1_hit_pts': HP_PCT_ENGINE_TRIPLE_MAIN,
        'oe_engine2_hit_pts': HP_PCT_ENGINE_TRIPLE_SECONDARY,
        'oe_engine3_hit_pts': HP_PCT_ENGINE_TRIPLE_SECONDARY,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'oe_wing_expl_resist': EXPL_RESIST_WING,
        'oe_engine1_expl_resist': EXPL_RESIST_ENGINE,
        'oe_engine2_expl_resist': EXPL_RESIST_ENGINE,
        'oe_engine3_expl_resist': EXPL_RESIST_ENGINE,
    }


class Mule(CorsairShip, ShipFreighter):
    ARCHETYPE = 'pi_freighter'

    SHIP_INDEX = SHIP_INDEX_6

    TEMPLATE_CODE = 'pfr'

    COLLISION_HIT_PTS_PERCENT = {
        'pfr_wing_hit_pts': HP_PCT_WING,
        'pfr_fin_hit_pts': HP_PCT_FIN,
        'pfr_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'pfr_wing_expl_resist': EXPL_RESIST_WING,
        'pfr_fin_expl_resist': EXPL_RESIST_MISC,
        'pfr_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


# GENERIC


class Dromader(GenericShip, ShipFreighter):
    SHIP_INDEX = SHIP_INDEX_3
    ARCHETYPE = 'bw_freighter'
    TEMPLATE_CODE = 'bwfr'

    COLLISION_HIT_PTS_PERCENT = {
        'bwfr_wing_hit_pts': HP_PCT_WING,
        'bwfr_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'bwfr_wing_expl_resist': EXPL_RESIST_WING,
        'bwfr_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class CSV(GenericShip, ShipFreighter):
    SHIP_INDEX = SHIP_INDEX_2
    ARCHETYPE = 'ge_csv'
    TEMPLATE_CODE = 'csv'


class Armored(GenericShip, ShipFreighter):
    SHIP_INDEX = SHIP_INDEX_10
    ARCHETYPE = 'ge_armored'
    TEMPLATE_CODE = 'armored'


class Starflier(GenericShip, ShipInterceptor, Ship1):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_GENERIC_INTERCEPTOR]
    SHIP_INDEX = SHIP_INDEX_1

    ARCHETYPE = 'ge_fighter'
    TEMPLATE_CODE = 'gf1'
    HP_TORPEDO = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'gf1_wing_hit_pts': HP_PCT_WING,
        'gf1_engine_hit_pts': HP_PCT_ENGINE_SINGLE,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'gf1_wing_expl_resist': EXPL_RESIST_WING,
        'gf1_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Startracker(GenericShip, ShipInterceptor, Ship2):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_GENERIC_INTERCEPTOR]
    SHIP_INDEX = SHIP_INDEX_5

    ARCHETYPE = 'ge_fighter2'
    TEMPLATE_CODE = 'gf2'
    HP_TORPEDO = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'gf2_wing_hit_pts': HP_PCT_WING,
        'gf2_engine_hit_pts': HP_PCT_ENGINE_SINGLE,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'gf2_wing_expl_resist': EXPL_RESIST_WING,
        'gf2_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Starblazer(GenericShip, ShipElite, Ship2):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_GENERIC_ELITE]
    SHIP_INDEX = SHIP_INDEX_5

    ARCHETYPE = 'ge_fighter3'
    TEMPLATE_CODE = 'gf3'
    HP_TORPEDO = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'gf3_wing_hit_pts': HP_PCT_WING,
        'gf3_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'gf3_wing_expl_resist': EXPL_RESIST_WING,
        'gf3_engine_expl_resist': EXPL_RESIST_ENGINE,
    }
