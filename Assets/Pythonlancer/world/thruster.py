from world.equipment import MainMiscEquip, Equipment, DefaultGood, MainEquipPrice


class Thruster(MainEquipPrice, DefaultGood, MainMiscEquip):
    DROP_CHANCE = 12

    SPEED_PER_RATE = {
        Equipment.RATE_1: 18,
        Equipment.RATE_2: 19,
        Equipment.RATE_3: 20,
        Equipment.RATE_4: 20.3,
        Equipment.RATE_5: 20.6,
        Equipment.RATE_6: 21,
        Equipment.RATE_7: 21.5,
        Equipment.RATE_8: 22,
        Equipment.RATE_9: 22.5,
        Equipment.RATE_10: 23,
        Equipment.RATE_11: 23.5,
        Equipment.RATE_12: 24,
        Equipment.RATE_13: 25,
        Equipment.RATE_14: 26,
        Equipment.RATE_15: 27,
        Equipment.RATE_16: 28,
        Equipment.RATE_17: 29,
        Equipment.RATE_18: 30,
        Equipment.RATE_19: 31.2,
        Equipment.RATE_20: 32.7,
        Equipment.RATE_21: 34,
        Equipment.RATE_22: 35.5,
        Equipment.RATE_23: 37,
        Equipment.RATE_24: 39,
        Equipment.RATE_25: 41,
        Equipment.RATE_26: 43,
        Equipment.RATE_27: 45,
        Equipment.RATE_28: 50,
    }

    LINEAR_DRAG = 600

    RH_THRUST_POWER = 110  # 220
    LI_THRUST_POWER = 100  # 200 - DEFAULT
    BR_THRUST_POWER = 80  # 160
    KU_THRUST_POWER = 90  # 180
    CO_THRUST_POWER = 120  # 240

    DEFAULT_EXPLOSION_RESISTANCE = 0.25

    THRUSTER_MAX_HIT_PTS = 5000

    THRUSTER_TEMPLATE = '''[Thruster]
nickname = {nickname}
ids_name = {ids_name}
ids_info = {ids_info}
hit_pts = {hit_pts}
explosion_resistance = {explosion_resistance}
max_force = {max_force}
power_usage = {power_usage}{thruster_defaults}{faction_thruster_core}'''

    THRUSTER_DEFAULTS = '''
HP_child = HpConnect
volume = 0
mass = 10
hp_particles = hpthrust
lootable = true
separation_explosion = sever_debris
LODranges = 0, 600'''

    RH_THRUSTER_CORE = '''
DA_archetype = equipment\\models\\st\\rh_thruster02.3db
material_library = equipment\\models\\rh_equip.mat
particles = gf_rh_thruster01'''

    LI_THRUSTER_CORE = '''
DA_archetype = equipment\\models\\st\\li_thruster02.3db
material_library = equipment\\models\\li_equip.mat
particles = gf_li_thruster01'''

    BR_THRUSTER_CORE = '''
DA_archetype = equipment\\models\\st\\br_thruster02.3db
material_library = equipment\\models\\br_equip.mat
particles = gf_br_thruster01'''

    KU_THRUSTER_CORE = '''
DA_archetype = equipment\\models\\st\\ku_thruster02.3db
material_library = equipment\\models\\ku_equip.mat
particles = gf_ku_thruster01'''

    CO_THRUSTER_CORE = '''
DA_archetype = equipment\\models\\st\\co_thruster02.3db
material_library = equipment\\models\\ge_equip.mat
particles = gf_co_thruster01'''

    RH_THRUSTER_ICON = 'equipment\\models\\icons\\rh\\rh_afterburn.3db'
    LI_THRUSTER_ICON = 'equipment\\models\\icons\\li\\li_afterburn.3db'
    BR_THRUSTER_ICON = 'equipment\\models\\icons\\br\\br_afterburn.3db'
    KU_THRUSTER_ICON = 'equipment\\models\\icons\\ku\\ku_afterburn.3db'
    CO_THRUSTER_ICON = 'equipment\\models\\icons\\co\\co_afterburn.3db'

    MAX_PRICE = 60000

    def get_thruster_core(self):
        if self.equip_type in self.RH_EQUIP:
            return self.RH_THRUSTER_CORE
        if self.equip_type in self.LI_EQUIP:
            return self.LI_THRUSTER_CORE
        if self.equip_type in self.BR_EQUIP:
            return self.BR_THRUSTER_CORE
        if self.equip_type in self.KU_EQUIP:
            return self.KU_THRUSTER_CORE
        if self.equip_type in self.CO_EQUIP:
            return self.CO_THRUSTER_CORE

        raise Exception('unknown thruster core')

    def get_nickname(self):
        return '{name}_afterburn_{digit}'.format(
            name=self.get_base_nickname(),
            digit=self.get_equipment_class_digit()
        )

    def get_explosion_resistance(self):
        resistance = self.DEFAULT_EXPLOSION_RESISTANCE

        if self.equip_type in self.LI_EQUIP:
            resistance /= 2

        return resistance

    def get_thruster_hit_pts(self):
        hit_pts =  self.THRUSTER_MAX_HIT_PTS * self.rate

        if self.equip_type in self.BR_EQUIP:
            hit_pts *= 1.5       

        return hit_pts

    def get_thruster_force(self):
        force = self.SPEED_PER_RATE[self.rate] * self.LINEAR_DRAG

        if self.equip_type in self.RH_EQUIP:
            force *= 1.1
        elif self.equip_type in self.BR_EQUIP:
            force *= 0.9
        elif self.equip_type in self.CO_EQUIP:
            force *= 1.2

        return int(force)

    def get_thruster_power(self):
        if self.equip_type in self.RH_EQUIP:
            return self.RH_THRUST_POWER
        if self.equip_type in self.LI_EQUIP:
            return self.LI_THRUST_POWER
        if self.equip_type in self.BR_EQUIP:
            return self.BR_THRUST_POWER
        if self.equip_type in self.KU_EQUIP:
            return self.KU_THRUST_POWER
        if self.equip_type in self.CO_EQUIP:
            return self.CO_THRUST_POWER

        raise Exception('unknown thruster power')

    def get_thruster_template_params(self):
        return {
            'nickname': self.get_nickname(),
            'ids_name': self.ids_name,
            'ids_info': self.ids_info,
            'hit_pts': self.get_thruster_hit_pts(),
            'explosion_resistance': self.get_explosion_resistance(),
            'max_force': self.get_thruster_force(),
            'power_usage': self.get_thruster_power(),
            'loot_props': self.LOOT_DEFAULTS,
            'thruster_defaults': self.THRUSTER_DEFAULTS,
            'faction_thruster_core': self.get_thruster_core(),
        }

    def get_equip(self):
        return self.THRUSTER_TEMPLATE.format(**self.get_thruster_template_params())

    def get_icon(self):
        if self.equip_type in self.RH_EQUIP:
            return self.RH_THRUSTER_ICON
        if self.equip_type in self.LI_EQUIP:
            return self.LI_THRUSTER_ICON
        if self.equip_type in self.BR_EQUIP:
            return self.BR_THRUSTER_ICON
        if self.equip_type in self.KU_EQUIP:
            return self.KU_THRUSTER_ICON
        if self.equip_type in self.CO_EQUIP:
            return self.CO_THRUSTER_ICON

        raise Exception('unknown thruster icon')

    RU_NAME_PER_TYPE = {
        MainMiscEquip.RH_MAIN: 'Форсаж Цвай',
        MainMiscEquip.RH_CIV: 'Форсаж Нуль',
        MainMiscEquip.RH_PIRATE: 'Форсаж Айн',

        MainMiscEquip.LI_MAIN: 'Форсаж Гамма',
        MainMiscEquip.LI_CIV: 'Форсаж Альфа',
        MainMiscEquip.LI_PIRATE: 'Форсаж Бета',

        MainMiscEquip.BR_MAIN: 'Улучшенный форсаж',
        MainMiscEquip.BR_CIV: 'Стандартный форсаж',
        MainMiscEquip.BR_PIRATE: 'Продвинутый форсаж',

        MainMiscEquip.KU_MAIN: 'Форсаж тип В',
        MainMiscEquip.KU_CIV: 'Форсаж тип А',
        MainMiscEquip.KU_PIRATE: 'Форсаж тип Б',

        MainMiscEquip.CO_ORDER: 'Элитный форсаж',
        MainMiscEquip.CO_CORSAIR: 'Тяжелый форсаж',
        MainMiscEquip.CO_OUTCAST: 'Перегруженный форсаж',
    }

    def get_max_price(self):
        return self.MAX_PRICE

    def get_ru_base_name(self):
        return self.RU_NAME_PER_TYPE[self.equip_type]

    def get_ru_name(self):
        return '{model} {mark}'.format(
            model=self.get_ru_base_name(),
            mark=self.get_mark_name(),
        )
