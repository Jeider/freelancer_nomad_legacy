from world.equipment import MainMiscEquip, Equipment


class Engine(MainMiscEquip):
    SPEED_PER_RATE = {
        Equipment.RATE_1: 76,
        Equipment.RATE_2: 78,
        Equipment.RATE_3: 80,
        Equipment.RATE_4: 82,
        Equipment.RATE_5: 84,
        Equipment.RATE_6: 86,
        Equipment.RATE_7: 88,
        Equipment.RATE_8: 90,
        Equipment.RATE_9: 92,
        Equipment.RATE_10: 94,
        Equipment.RATE_11: 96,
        Equipment.RATE_12: 98,
        Equipment.RATE_13: 100,
        Equipment.RATE_14: 102,
        Equipment.RATE_15: 105,
        Equipment.RATE_16: 107,
        Equipment.RATE_17: 109,
        Equipment.RATE_18: 112,
        Equipment.RATE_19: 114,
        Equipment.RATE_20: 118,
        Equipment.RATE_21: 120,
        Equipment.RATE_22: 122,
        Equipment.RATE_23: 126,
        Equipment.RATE_24: 130,
        Equipment.RATE_25: 135,
        Equipment.RATE_26: 140,
        Equipment.RATE_27: 145,
        Equipment.RATE_28: 150,
    }

    CRUISE_PER_RATE = {
        Equipment.RATE_1: 395,
        Equipment.RATE_2: 398,
        Equipment.RATE_3: 400,
        Equipment.RATE_4: 403,
        Equipment.RATE_5: 406,
        Equipment.RATE_6: 410,
        Equipment.RATE_7: 414,
        Equipment.RATE_8: 417,
        Equipment.RATE_9: 420,
        Equipment.RATE_10: 425,
        Equipment.RATE_11: 430,
        Equipment.RATE_12: 435,
        Equipment.RATE_13: 439,
        Equipment.RATE_14: 444,
        Equipment.RATE_15: 450,
        Equipment.RATE_16: 458,
        Equipment.RATE_17: 464,
        Equipment.RATE_18: 470,
        Equipment.RATE_19: 479,
        Equipment.RATE_20: 485,
        Equipment.RATE_21: 490,
        Equipment.RATE_22: 497,
        Equipment.RATE_23: 506,
        Equipment.RATE_24: 515,
        Equipment.RATE_25: 522,
        Equipment.RATE_26: 533,
        Equipment.RATE_27: 540,
        Equipment.RATE_28: 550,
    }

    DEFAULT_DRAG = 599
    RH_DRAG = 659
    KU_DRAG = 559
    EXTRA_DRAG = 1

    SPEED_MULTIPLER = 1.0
    CRUISE_MULTIPLER = 1.0

    MAX_POWER_REGEN = 1200
    BASE_POWER_DRAIN_MULTIPLER = 0.5
    CRUISE_POWER_DRAIN_MULTIPLER = 1

    BASE_CRUISE_CHARGE_TIME = 5

    ENGINE_MAX_HIT_PTS = 8000

    BASE_REVERSE = 0.1

    BASE_STRAFE_MULTIPER = 1.0

    ENGINE_TEMPLATE = '''[Engine]
nickname = {nickname}
ids_name = {ids_name}
ids_info = {ids_info}
max_force = {max_force}
cruise_speed = {cruise_speed}
linear_drag = {linear_drag}
power_usage = {power_usage}
cruise_charge_time = {cruise_charge_time}
cruise_power_usage = {cruise_power_usage}
hit_pts = {hit_pts}
reverse_fraction = {reverse_fraction}
strafe_force_multiplier = {reverse_fraction}
hp_type = {hp_type}{loot_props}{engine_defaults}{faction_engine_core}{faction_engine_generics}{faction_engine_ship}'''

    ENGINE_DEFAULTS = '''
volume = 0
character_pitch_range = -50, 25
rumble_atten_range = -5, 0
rumble_pitch_range = -25, 25
cruise_disrupt_sound = cruise_disrupt
cruise_backfire_sound = cruise_backfire
indestructible = false
outside_cone_attenuation = -3
inside_sound_cone = 60
outside_sound_cone = 180
HP_child = HPMount
explosion_resistance = 1.0
lootable = true
mass = 10'''

    RH_ENGINE_CORE = '''
DA_archetype = Equipment\\models\\hardware\\rh_coaxial_nuclear_drive.3db
material_library = Equipment\\models\\hardware.mat
flame_effect = gf_rh_smallengine02_fire
trail_effect = gf_rh_smallengine02_trail
trail_effect_player = gf_rh_smallengine02_trail'''

    RH_MAIN_ENGINE_GENERICS = '''
cruise_start_sound = engine_rh_cruise_start
cruise_loop_sound = engine_rh_cruise_loop
cruise_stop_sound = engine_rh_cruise_stop'''

    RH_MAIN_ENGINE_FIGHTER = '''
character_start_sound = engine_rh_fighter_start
character_loop_sound = engine_rh_fighter_loop
rumble_sound = rumble_fighter
engine_kill_sound = engine_rh_fighter_kill'''

    RH_MAIN_ENGINE_ELITE = '''
character_start_sound = engine_rh_fighter_start
character_loop_sound = engine_rh_fighter_loop
rumble_sound = rumble_h_fighter
engine_kill_sound = engine_rh_fighter_kill'''

    RH_MAIN_ENGINE_FREIGHTER = '''
character_start_sound = engine_rh_freighter_start
character_loop_sound = engine_rh_freighter_loop
rumble_sound = rumble_freighter
engine_kill_sound = engine_rh_freighter_kill'''


    LI_ENGINE_CORE = '''
DA_archetype = Equipment\\models\\hardware\\li_free_flow_ion_drive.3db
material_library = Equipment\\models\\hardware.mat
flame_effect = gf_li_smallengine02_fire
trail_effect = gf_li_smallengine02_trail
trail_effect_player = gf_li_smallengine02_trail'''

    LI_MAIN_ENGINE_GENERICS = '''
cruise_start_sound = engine_li_cruise_start
cruise_loop_sound = engine_li_cruise_loop
cruise_stop_sound = engine_li_cruise_stop'''

    LI_MAIN_ENGINE_FIGHTER = '''
character_start_sound = engine_li_fighter_start
character_loop_sound = engine_li_fighter_loop
rumble_sound = rumble_fighter
engine_kill_sound = engine_li_fighter_kill'''

    LI_MAIN_ENGINE_ELITE = '''
character_start_sound = engine_li_fighter_start
character_loop_sound = engine_li_fighter_loop
rumble_sound = rumble_h_fighter
engine_kill_sound = engine_li_fighter_kill'''

    LI_MAIN_ENGINE_FREIGHTER = '''
character_start_sound = engine_li_freighter_start
character_loop_sound = engine_li_freighter_loop
rumble_sound = rumble_freighter
engine_kill_sound = engine_li_freighter_kill'''


    BR_ENGINE_CORE = '''
DA_archetype = Equipment\\models\\hardware\\br_xenon_ion_drive.3db
material_library = Equipment\\models\\hardware.mat
flame_effect = gf_br_smallengine02_fire
trail_effect = gf_br_smallengine02_trail
trail_effect_player = gf_br_smallengine02_trail'''

    BR_MAIN_ENGINE_GENERICS = '''
cruise_start_sound = engine_br_cruise_start
cruise_loop_sound = engine_br_cruise_loop
cruise_stop_sound = engine_br_cruise_stop'''

    BR_MAIN_ENGINE_FIGHTER = '''
character_start_sound = engine_br_fighter_start
character_loop_sound = engine_br_fighter_loop
rumble_sound = rumble_fighter
engine_kill_sound = engine_br_fighter_kill'''

    BR_MAIN_ENGINE_ELITE = '''
character_start_sound = engine_br_fighter_start
character_loop_sound = engine_br_fighter_loop
rumble_sound = rumble_h_fighter
engine_kill_sound = engine_br_fighter_kill'''

    BR_MAIN_ENGINE_FREIGHTER = '''
character_start_sound = engine_br_freighter_start
character_loop_sound = engine_br_freighter_loop
rumble_sound = rumble_freighter
engine_kill_sound = engine_br_freighter_kill'''


    KU_ENGINE_CORE = '''
DA_archetype = Equipment\\models\\hardware\\ku_cylindrical_nuclear_drive.3db
material_library = Equipment\\models\\hardware.mat
flame_effect = gf_ku_smallengine02_fire
trail_effect = gf_ku_smallengine02_trail
trail_effect_player = gf_ku_smallengine02_trail'''

    KU_MAIN_ENGINE_GENERICS = '''
cruise_start_sound = engine_ku_cruise_start
cruise_loop_sound = engine_ku_cruise_loop
cruise_stop_sound = engine_ku_cruise_stop'''

    KU_MAIN_ENGINE_FIGHTER = '''
character_start_sound = engine_ku_fighter_start
character_loop_sound = engine_ku_fighter_loop
rumble_sound = rumble_fighter
engine_kill_sound = engine_ku_fighter_kill'''

    KU_MAIN_ENGINE_ELITE = '''
character_start_sound = engine_ku_fighter_start
character_loop_sound = engine_ku_fighter_loop
rumble_sound = rumble_h_fighter
engine_kill_sound = engine_ku_fighter_kill'''

    KU_MAIN_ENGINE_FREIGHTER = '''
character_start_sound = engine_ku_freighter_start
character_loop_sound = engine_ku_freighter_loop
rumble_sound = rumble_freighter
engine_kill_sound = engine_ku_freighter_kill'''


    CIV_ENGINE_GENERICS = '''
cruise_start_sound = engine_ci_cruise_start
cruise_loop_sound = engine_ci_cruise_loop
cruise_stop_sound = engine_ci_cruise_stop'''

    CIV_ENGINE_FIGHTER = '''
character_start_sound = engine_ci_fighter_start
character_loop_sound = engine_ci_fighter_loop
rumble_sound = rumble_ci_fighter
engine_kill_sound = engine_ci_fighter_kill'''

    CIV_ENGINE_ELITE = '''
character_start_sound = engine_ci_fighter_start
character_loop_sound = engine_ci_fighter_loop
rumble_sound = rumble_ci_h_fighter
engine_kill_sound = engine_ci_fighter_kill'''

    CIV_ENGINE_FREIGHTER = '''
character_start_sound = engine_ci_freighter_start
character_loop_sound = engine_ci_freighter_loop
rumble_sound = rumble_freighter
engine_kill_sound = engine_ci_freighter_kill'''


    PIRATE_ENGINE_GENERICS = '''
cruise_start_sound = engine_bw_cruise_start
cruise_loop_sound = engine_bw_cruise_loop
cruise_stop_sound = engine_bw_cruise_stop'''

    PIRATE_ENGINE_FIGHTER = '''
character_start_sound = engine_bw_fighter_start
character_loop_sound = engine_bw_fighter_loop
rumble_sound = rumble_bw_fighter
engine_kill_sound = engine_bw_fighter_kill'''

    PIRATE_ENGINE_ELITE = '''
character_start_sound = engine_bw_fighter_start
character_loop_sound = engine_bw_fighter_loop
rumble_sound = rumble_bw_h_fighter
engine_kill_sound = engine_bw_fighter_kill'''

    PIRATE_ENGINE_FREIGHTER = '''
character_start_sound = engine_bw_freighter_start
character_loop_sound = engine_bw_freighter_loop
rumble_sound = rumble_bw_freighter
engine_kill_sound = engine_bw_freighter_kill'''


    CO_ENGINE_CORE = '''
DA_archetype = Equipment\\models\\hardware\\co_compact_toroidal_nuclear_drive.3db
material_library = Equipment\\models\\hardware.mat
flame_effect = gf_co_smallengine02_fire
trail_effect = gf_co_smallengine02_trail
trail_effect_player = gf_co_smallengine02_trail'''

    CO_MAIN_ENGINE_GENERICS = '''
cruise_start_sound = engine_bw_cruise_start
cruise_loop_sound = engine_bw_cruise_loop
cruise_stop_sound = engine_bw_cruise_stop'''

    CO_MAIN_ENGINE_FIGHTER = '''
character_start_sound = engine_pi_fighter_start
character_loop_sound = engine_pi_fighter_loop
rumble_sound = rumble_pi_fighter
engine_kill_sound = engine_pi_fighter_kill'''

    CO_MAIN_ENGINE_ELITE = '''
character_start_sound = engine_pi_fighter_start
character_loop_sound = engine_pi_fighter_loop
rumble_sound = rumble_oe_h_fighter
engine_kill_sound = engine_pi_fighter_kill'''

    CO_MAIN_ENGINE_FREIGHTER = '''
character_start_sound = engine_pi_freighter_start
character_loop_sound = engine_pi_freighter_loop
rumble_sound = rumble_pi_freighter
engine_kill_sound = engine_pi_freighter_kill'''


    OUTCAST_ENGINE_GENERICS = '''
cruise_start_sound = engine_bw_cruise_start
cruise_loop_sound = engine_bw_cruise_loop
cruise_stop_sound = engine_bw_cruise_stop'''

    OUTCAST_ENGINE_FIGHTER = '''
character_start_sound = engine_oe_h_fighter_start
character_loop_sound = engine_oe_h_fighter_loop
rumble_sound = rumble_pi_fighter
engine_kill_sound = engine_pi_fighter_kill'''

    OUTCAST_ENGINE_ELITE = '''
character_start_sound = engine_oe_h_fighter_start
character_loop_sound = engine_oe_h_fighter_loop
rumble_sound = rumble_pi_h_fighter
engine_kill_sound = engine_pi_fighter_kill
'''

    OUTCAST_ENGINE_FREIGHTER = '''
character_start_sound = engine_bw_freighter_start
character_loop_sound = engine_bw_freighter_loop
rumble_sound = rumble_pi_freighter
engine_kill_sound = engine_pi_freighter_kill'''

    RH_ENGINE_MODEL = 'Equipment\\models\\hardware\\rh_coaxial_nuclear_drive.3db'
    LI_ENGINE_MODEL = 'Equipment\\models\\hardware\\li_free_flow_ion_drive.3db'
    BR_ENGINE_MODEL = 'Equipment\\models\\hardware\\br_xenon_ion_drive.3db'
    KU_ENGINE_MODEL = 'Equipment\\models\\hardware\\ku_cylindrical_nuclear_drive.3db'
    CO_ENGINE_MODEL = 'Equipment\\models\\hardware\\co_compact_toroidal_nuclear_drive.3db'

    RH_ENGINE_ICON = 'equipment\\models\\icons\\rh\\rh_engine.3db'
    LI_ENGINE_ICON = 'equipment\\models\\icons\\li\\li_engine.3db'
    BR_ENGINE_ICON = 'equipment\\models\\icons\\br\\br_engine.3db'
    KU_ENGINE_ICON = 'equipment\\models\\icons\\ku\\ku_engine.3db'
    CO_ENGINE_ICON = 'equipment\\models\\icons\\co\\co_engine.3db'

    def __init__(self, equip_type, ship_class, equipment_class, ids_name, ids_info):
        self.equip_type = equip_type
        self.ship_class = ship_class
        self.equipment_class = equipment_class

        if self.equip_type in self.MAIN_EQUIP:
            self.rate = self.get_main_rate()
        if self.equip_type in self.CIV_EQUIP:
            self.rate = self.get_civ_rate()
        if self.equip_type in self.PIRATE_EQUIP:
            self.rate = self.get_pirate_rate()
        if self.equip_type == self.CO_OUTCAST:
            self.rate = self.get_civ_rate()

        self.ids_name = ids_name
        self.ids_info = ids_info

    def get_engine_core(self):
        if self.equip_type in self.RH_EQUIP:
            return self.RH_ENGINE_CORE
        if self.equip_type in self.LI_EQUIP:
            return self.LI_ENGINE_CORE
        if self.equip_type in self.BR_EQUIP:
            return self.BR_ENGINE_CORE
        if self.equip_type in self.KU_EQUIP:
            return self.KU_ENGINE_CORE
        if self.equip_type in self.CO_EQUIP:
            return self.CO_ENGINE_CORE

        raise Exception('unknown engine core')

    def get_engine_generics(self):
        if self.equip_type == self.RH_MAIN:
            return self.RH_MAIN_ENGINE_GENERICS
        if self.equip_type == self.RH_CIV:
            return self.CIV_ENGINE_GENERICS
        if self.equip_type == self.RH_PIRATE:
            return self.PIRATE_ENGINE_GENERICS

        if self.equip_type == self.LI_MAIN:
            return self.LI_MAIN_ENGINE_GENERICS
        if self.equip_type == self.LI_CIV:
            return self.CIV_ENGINE_GENERICS
        if self.equip_type == self.LI_PIRATE:
            return self.PIRATE_ENGINE_GENERICS

        if self.equip_type == self.BR_MAIN:
            return self.BR_MAIN_ENGINE_GENERICS
        if self.equip_type == self.BR_CIV:
            return self.CIV_ENGINE_GENERICS
        if self.equip_type == self.BR_PIRATE:
            return self.PIRATE_ENGINE_GENERICS

        if self.equip_type == self.KU_MAIN:
            return self.KU_MAIN_ENGINE_GENERICS
        if self.equip_type == self.KU_CIV:
            return self.CIV_ENGINE_GENERICS
        if self.equip_type == self.KU_PIRATE:
            return self.PIRATE_ENGINE_GENERICS

        if self.equip_type == self.CO_MAIN:
            return self.CO_MAIN_ENGINE_GENERICS
        if self.equip_type == self.CO_OUTCAST:
            return self.OUTCAST_ENGINE_GENERICS

        raise Exception('unknown engine generic')

    def get_fighter_engine(self):
        if self.equip_type == self.RH_MAIN:
            return self.RH_MAIN_ENGINE_FIGHTER
        if self.equip_type == self.RH_CIV:
            return self.CIV_ENGINE_FIGHTER
        if self.equip_type == self.RH_PIRATE:
            return self.PIRATE_ENGINE_FIGHTER

        if self.equip_type == self.LI_MAIN:
            return self.LI_MAIN_ENGINE_FIGHTER
        if self.equip_type == self.LI_CIV:
            return self.CIV_ENGINE_FIGHTER
        if self.equip_type == self.LI_PIRATE:
            return self.PIRATE_ENGINE_FIGHTER

        if self.equip_type == self.BR_MAIN:
            return self.BR_MAIN_ENGINE_FIGHTER
        if self.equip_type == self.BR_CIV:
            return self.CIV_ENGINE_FIGHTER
        if self.equip_type == self.BR_PIRATE:
            return self.PIRATE_ENGINE_FIGHTER

        if self.equip_type == self.KU_MAIN:
            return self.KU_MAIN_ENGINE_FIGHTER
        if self.equip_type == self.KU_CIV:
            return self.CIV_ENGINE_FIGHTER
        if self.equip_type == self.KU_PIRATE:
            return self.PIRATE_ENGINE_FIGHTER

        if self.equip_type == self.CO_MAIN:
            return self.CO_MAIN_ENGINE_FIGHTER
        if self.equip_type == self.CO_OUTCAST:
            return self.OUTCAST_ENGINE_FIGHTER

        raise Exception('unkown fighter engine')

    def get_elite_engine(self):
        if self.equip_type == self.RH_MAIN:
            return self.RH_MAIN_ENGINE_ELITE
        if self.equip_type == self.RH_CIV:
            return self.CIV_ENGINE_ELITE
        if self.equip_type == self.RH_PIRATE:
            return self.PIRATE_ENGINE_ELITE

        if self.equip_type == self.LI_MAIN:
            return self.LI_MAIN_ENGINE_ELITE
        if self.equip_type == self.LI_CIV:
            return self.CIV_ENGINE_ELITE
        if self.equip_type == self.LI_PIRATE:
            return self.PIRATE_ENGINE_ELITE

        if self.equip_type == self.BR_MAIN:
            return self.BR_MAIN_ENGINE_ELITE
        if self.equip_type == self.BR_CIV:
            return self.CIV_ENGINE_ELITE
        if self.equip_type == self.BR_PIRATE:
            return self.PIRATE_ENGINE_ELITE

        if self.equip_type == self.KU_MAIN:
            return self.KU_MAIN_ENGINE_ELITE
        if self.equip_type == self.KU_CIV:
            return self.CIV_ENGINE_ELITE
        if self.equip_type == self.KU_PIRATE:
            return self.PIRATE_ENGINE_ELITE

        if self.equip_type == self.CO_MAIN:
            return self.CO_MAIN_ENGINE_ELITE
        if self.equip_type == self.CO_OUTCAST:
            return self.OUTCAST_ENGINE_ELITE

        raise Exception('unkown elite engine')

    def get_freighter_engine(self):
        if self.equip_type == self.RH_MAIN:
            return self.RH_MAIN_ENGINE_FREIGHTER
        if self.equip_type == self.RH_CIV:
            return self.CIV_ENGINE_FREIGHTER
        if self.equip_type == self.RH_PIRATE:
            return self.PIRATE_ENGINE_FREIGHTER

        if self.equip_type == self.LI_MAIN:
            return self.LI_MAIN_ENGINE_FREIGHTER
        if self.equip_type == self.LI_CIV:
            return self.CIV_ENGINE_FREIGHTER
        if self.equip_type == self.LI_PIRATE:
            return self.PIRATE_ENGINE_FREIGHTER

        if self.equip_type == self.BR_MAIN:
            return self.BR_MAIN_ENGINE_FREIGHTER
        if self.equip_type == self.BR_CIV:
            return self.CIV_ENGINE_FREIGHTER
        if self.equip_type == self.BR_PIRATE:
            return self.PIRATE_ENGINE_FREIGHTER

        if self.equip_type == self.KU_MAIN:
            return self.KU_MAIN_ENGINE_FREIGHTER
        if self.equip_type == self.KU_CIV:
            return self.CIV_ENGINE_FREIGHTER
        if self.equip_type == self.KU_PIRATE:
            return self.PIRATE_ENGINE_FREIGHTER

        if self.equip_type == self.CO_MAIN:
            return self.CO_MAIN_ENGINE_FREIGHTER
        if self.equip_type == self.CO_OUTCAST:
            return self.OUTCAST_ENGINE_FREIGHTER

        raise Exception('unkown freighter engine')

    def get_ship_engine(self):
        if self.ship_class == self.SHIPCLASS_FIGHTER:
            return self.get_fighter_engine()
        if self.ship_class == self.SHIPCLASS_ELITE:
            return self.get_elite_engine()
        if self.ship_class == self.SHIPCLASS_FREIGHTER:
            return self.get_freighter_engine()

        raise Exception('unkown ship engine')

    def get_nickname(self):
        return '{name}_engine_{digit}_{shipclass}'.format(
            name=self.get_base_nickname(),
            digit=self.get_equipment_class_digit(),
            shipclass=self.get_shipclass_name()
        )

    def get_max_force(self):
        force = self.SPEED_PER_RATE[self.rate] * self.get_force_multipler()

        if self.equip_type in self.KU_EQUIP:
            force *= 0.95
        if self.equip_type in self.BR_EQUIP:
            force *= 1.1

        return force

    def get_cruise_speed(self):
        cruise_speed = self.CRUISE_PER_RATE[self.rate]
        multipler = self.CRUISE_MULTIPLER
        if self.equip_type in self.LI_EQUIP:
            multipler += 0.05
        if self.ship_class == self.SHIPCLASS_FREIGHTER:
            multipler += 0.05
        return cruise_speed * multipler

    def get_linear_drag(self):
        if self.equip_type in self.RH_EQUIP:
            return self.RH_DRAG
        if self.equip_type in self.KU_EQUIP:
            return self.KU_DRAG

        return self.DEFAULT_DRAG

    def get_force_multipler(self):
        return self.get_linear_drag() + self.EXTRA_DRAG

    def get_base_power(self):
        return self.MAX_POWER_REGEN * self.BASE_POWER_DRAIN_MULTIPLER * self.rate

    def get_cruise_power(self):
        return self.MAX_POWER_REGEN * self.CRUISE_POWER_DRAIN_MULTIPLER * self.rate

    def get_cruise_charge_time(self):
        charge_time = self.BASE_CRUISE_CHARGE_TIME

        if self.equip_type in self.CO_EQUIP:
            charge_time -= 2
        elif self.equip_type in self.LI_EQUIP:
            charge_time += 1

        if self.ship_class == self.SHIPCLASS_ELITE:
            charge_time += 1
        elif self.ship_class == self.SHIPCLASS_FREIGHTER:
            charge_time += 2

        return charge_time

    def get_engine_hit_pts(self):
        return self.ENGINE_MAX_HIT_PTS * self.rate

    def get_reverse(self):
        reverse = self.BASE_REVERSE

        if self.equip_type in self.BR_EQUIP:
            reverse /= 2
        elif self.equip_type in self.RH_EQUIP:
            reverse *= 2

        if self.ship_class == self.SHIPCLASS_ELITE:
            reverse *= 2

        return reverse

    def get_strafe_force_multiper(self):
        strafe_multipler = self.BASE_STRAFE_MULTIPER

        if self.equip_type in self.BR_EQUIP:
            strafe_multipler /= 2
        elif self.equip_type in self.RH_EQUIP:
            strafe_multipler *= 2

        if self.ship_class == self.SHIPCLASS_ELITE:
            strafe_multipler *= 2

        return strafe_multipler

    def get_engine_hp_type(self):
        return 'hp_{shipclass}_engine_special_{equipment_class}'.format(
            shipclass=self.get_shipclass_hp_type_string(),
            equipment_class=self.equipment_class
        )

    def get_engine_template_params(self):
        return {
            'nickname': self.get_nickname(),
            'ids_name': self.ids_name,
            'ids_info': self.ids_info,
            'max_force': self.get_max_force(),
            'cruise_speed': self.get_cruise_speed(),
            'linear_drag': self.get_linear_drag(),
            'power_usage': self.get_base_power(),
            'cruise_charge_time': self.get_cruise_charge_time(),
            'cruise_power_usage': self.get_cruise_power(),
            'hit_pts': self.get_engine_hit_pts(),
            'reverse_fraction': self.get_reverse(),
            'strafe_force_multiplier': self.get_strafe_force_multiper(),
            'hp_type': self.get_engine_hp_type(),
            'loot_props': self.LOOT_DEFAULTS,
            'engine_defaults': self.ENGINE_DEFAULTS,
            'faction_engine_core': self.get_engine_core(),
            'faction_engine_generics': self.get_engine_generics(),
            'faction_engine_ship': self.get_ship_engine(),

        }

    def get_equip(self):
        return self.ENGINE_TEMPLATE.format(**self.get_engine_template_params())

    def get_price(self):
        return 100  # TODO: correct price

    def get_equip_model(self):
        if self.equip_type in self.RH_EQUIP:
            return self.RH_ENGINE_MODEL
        if self.equip_type in self.LI_EQUIP:
            return self.LI_ENGINE_MODEL
        if self.equip_type in self.BR_EQUIP:
            return self.BR_ENGINE_MODEL
        if self.equip_type in self.KU_EQUIP:
            return self.KU_ENGINE_MODEL
        if self.equip_type in self.CO_EQUIP:
            return self.CO_ENGINE_MODEL

        raise Exception('unknown engine model')

    def get_icon(self):
        if self.equip_type in self.RH_EQUIP:
            return self.RH_ENGINE_ICON
        if self.equip_type in self.LI_EQUIP:
            return self.LI_ENGINE_ICON
        if self.equip_type in self.BR_EQUIP:
            return self.BR_ENGINE_ICON
        if self.equip_type in self.KU_EQUIP:
            return self.KU_ENGINE_ICON
        if self.equip_type in self.CO_EQUIP:
            return self.CO_ENGINE_ICON

        raise Exception('unknown engine icon')

