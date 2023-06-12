from world.equipment import MainInternalEquip, MainMiscEquip, Equipment, AdoxaEquipClassGood, MainEquipPrice


class BasePower(MainInternalEquip):
    DROP_CHANCE = 4

    MAX_POWER_FIGHTER = 12000
    MAX_POWER_ELITE = 12000
    MAX_POWER_FREIGHTER = 12000
    MAX_POWER_REGEN_FIGHTER = 1200
    MAX_POWER_REGEN_ELITE = 1200
    MAX_POWER_REGEN_FREIGHTER = 1200

    BASE_THRUST_CAPACITY = 1000
    BASE_THRUST_REGEN = 100

    POWER_MAX_HIT_PTS = 8000

    POWER_TEMPLATE = '''[Power]
nickname = {nickname}
ids_name = {ids_name}
ids_info = {ids_info}
volume = 0
mass = 10
HP_child = HPMount
explosion_resistance = 1.0
lootable = true
hp_type = {hp_type}
hit_pts = {hit_pts}
capacity = {capacity}
charge_rate = {charge_rate}
thrust_capacity = {thrust_capacity}
thrust_charge_rate = {thrust_charge_rate}{loot_props}{faction_power_core}'''

    RH_POWER_CORE = '''
DA_archetype = Equipment\\models\\hardware\\rh_he4_fusion_reactor.3db
material_library = Equipment\\models\\hardware.mat'''

    LI_POWER_CORE = '''
DA_archetype = Equipment\\models\\hardware\\li_fusion_reactor.3db
material_library = Equipment\\models\\hardware.mat'''

    BR_POWER_CORE = '''
DA_archetype = Equipment\\models\\hardware\\br_fission_generator.3db
material_library = Equipment\\models\\hardware.mat'''

    KU_POWER_CORE = '''
DA_archetype = Equipment\\models\\hardware\\ku_phase_wave_generator.3db
material_library = Equipment\\models\\hardware.mat'''

    CO_POWER_CORE = '''
DA_archetype = Equipment\\models\\hardware\\ge_high_temp_nuclear_core.3db
material_library = Equipment\\models\\hardware.mat'''

    RH_POWER_MODEL = 'Equipment\\models\\hardware\\rh_he4_fusion_reactor.3db'
    LI_POWER_MODEL = 'Equipment\\models\\hardware\\li_fusion_reactor.3db'
    BR_POWER_MODEL = 'Equipment\\models\\hardware\\br_fission_generator.3db'
    KU_POWER_MODEL = 'Equipment\\models\\hardware\\ku_phase_wave_generator.3db'
    CO_POWER_MODEL = 'Equipment\\models\\hardware\\ge_high_temp_nuclear_core.3db'

    RH_POWER_ICON = 'equipment\\models\\icons\\rh\\rh_power.3db'
    LI_POWER_ICON = 'equipment\\models\\icons\\li\\li_power.3db'
    BR_POWER_ICON = 'equipment\\models\\icons\\br\\br_power.3db'
    KU_POWER_ICON = 'equipment\\models\\icons\\ku\\ku_power.3db'
    CO_POWER_ICON = 'equipment\\models\\icons\\co\\co_power.3db'

    def get_power_core(self):
        if self.equip_type in self.RH_EQUIP:
            return self.RH_POWER_CORE
        if self.equip_type in self.LI_EQUIP:
            return self.LI_POWER_CORE
        if self.equip_type in self.BR_EQUIP:
            return self.BR_POWER_CORE
        if self.equip_type in self.KU_EQUIP:
            return self.KU_POWER_CORE
        if self.equip_type in self.CO_EQUIP:
            return self.CO_POWER_CORE

        raise Exception('unknown power core')

    def get_nickname(self):
        return '{name}_power_{digit}_{shipclass}'.format(
            name=self.get_base_nickname(),
            digit=self.get_equipment_class_digit(),
            shipclass=self.get_shipclass_name()
        )

    def get_power_hit_pts(self):
        return self.POWER_MAX_HIT_PTS * self.rate

    def get_power_hp_type(self):
        return 'hp_{shipclass}_power_special_{equipment_class}'.format(
            shipclass=self.get_shipclass_hp_type_string(),
            equipment_class=self.equipment_class
        )

    def get_max_power_capacity(self):
        if self.ship_class == self.SHIPCLASS_FIGHTER:
            return self.MAX_POWER_FIGHTER
        if self.ship_class == self.SHIPCLASS_ELITE:
            return self.MAX_POWER_ELITE
        if self.ship_class == self.SHIPCLASS_FREIGHTER:
            return self.MAX_POWER_FREIGHTER

        raise Exception('unkown ship power capacity')

    def get_power_capacity(self):
        capacity = self.get_max_power_capacity()

        if self.equip_type in self.RH_EQUIP:
            capacity *= 1.1
        elif self.equip_type in self.BR_EQUIP:
            capacity *= 1.05

        return capacity

    def get_max_power_regen(self):
        if self.ship_class == self.SHIPCLASS_FIGHTER:
            return self.MAX_POWER_REGEN_FIGHTER
        if self.ship_class == self.SHIPCLASS_ELITE:
            return self.MAX_POWER_REGEN_ELITE
        if self.ship_class == self.SHIPCLASS_FREIGHTER:
            return self.MAX_POWER_REGEN_FREIGHTER

        raise Exception('unkown ship power regen')

    def get_power_regen(self):
        regen = self.get_max_power_regen()

        if self.equip_type in self.KU_EQUIP:
            regen *= 1.1
        elif self.equip_type in self.BR_EQUIP:
            regen *= 1.05

        return regen

    def get_thrust_capacity(self):
        thrust_capacity = self.BASE_THRUST_CAPACITY

        if self.equip_type in self.LI_EQUIP:
            thrust_capacity *= 1.5
        elif self.equip_type in self.BR_EQUIP:
            thrust_capacity *= 0.66

        return thrust_capacity

    def get_thrust_regen(self):
        thrust_regen = self.BASE_THRUST_REGEN

        if self.equip_type in self.CO_EQUIP:
            thrust_regen *= 1.33

        return thrust_regen


class Power(MainEquipPrice, AdoxaEquipClassGood, BasePower):
    def get_power_template_params(self):
        return {
            'nickname': self.get_nickname(),
            'ids_name': self.ids_name,
            'ids_info': self.ids_info,
            'hp_type': self.get_power_hp_type(),
            'hit_pts': self.get_power_hit_pts(),
            'capacity': self.get_power_capacity(),
            'charge_rate': self.get_power_regen(),
            'thrust_capacity': self.get_thrust_capacity(),
            'thrust_charge_rate': self.get_thrust_regen(),
            'loot_props': self.LOOT_DEFAULTS,
            'faction_power_core': self.get_power_core(),
        }

    def get_equip(self):
        return self.POWER_TEMPLATE.format(**self.get_power_template_params())

    def get_equip_model(self):
        if self.equip_type in self.RH_EQUIP:
            return self.RH_POWER_MODEL
        if self.equip_type in self.LI_EQUIP:
            return self.LI_POWER_MODEL
        if self.equip_type in self.BR_EQUIP:
            return self.BR_POWER_MODEL
        if self.equip_type in self.KU_EQUIP:
            return self.KU_POWER_MODEL
        if self.equip_type in self.CO_EQUIP:
            return self.CO_POWER_MODEL

        raise Exception('unknown power model')

    def get_icon(self):
        if self.equip_type in self.RH_EQUIP:
            return self.RH_POWER_ICON
        if self.equip_type in self.LI_EQUIP:
            return self.LI_POWER_ICON
        if self.equip_type in self.BR_EQUIP:
            return self.BR_POWER_ICON
        if self.equip_type in self.KU_EQUIP:
            return self.KU_POWER_ICON
        if self.equip_type in self.CO_EQUIP:
            return self.CO_POWER_ICON

        raise Exception('unknown power icon')

    RU_NAME_PER_TYPE = {
        MainMiscEquip.RH_MAIN: 'Гайзенберг',
        MainMiscEquip.RH_CIV: 'Гейгер',
        MainMiscEquip.RH_PIRATE: 'Дёпель',

        MainMiscEquip.LI_MAIN: 'Ферми',
        MainMiscEquip.LI_CIV: 'Комптон',
        MainMiscEquip.LI_PIRATE: 'Сиборг',

        MainMiscEquip.BR_MAIN: 'Резерфорд',
        MainMiscEquip.BR_CIV: 'Содди',
        MainMiscEquip.BR_PIRATE: 'Чедвик',

        MainMiscEquip.KU_MAIN: 'Генкай',
        MainMiscEquip.KU_CIV: 'Иката',
        MainMiscEquip.KU_PIRATE: 'Омагава',

        MainMiscEquip.CO_ORDER: 'Юпитер',
        MainMiscEquip.CO_CORSAIR: 'Трильо',
        MainMiscEquip.CO_OUTCAST: 'Конфрентес',
    }

    def get_ru_equip_name(self):
        return 'Генер.'

    def get_ru_base_name(self):
        return self.RU_NAME_PER_TYPE[self.equip_type]
