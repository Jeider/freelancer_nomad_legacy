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

    THRUSTER_FX_PER_TYPE = {
        MainMiscEquip.RH_MAIN: 'gf_rh_thruster01',
        MainMiscEquip.RH_CIV: 'gf_rh_thruster02',
        MainMiscEquip.RH_PIRATE: 'gf_rh_thruster03',

        MainMiscEquip.LI_MAIN: 'gf_li_thruster01',
        MainMiscEquip.LI_CIV: 'gf_li_thruster01',
        MainMiscEquip.LI_PIRATE: 'gf_li_thruster01',

        MainMiscEquip.BR_MAIN: 'gf_br_thruster01',
        MainMiscEquip.BR_CIV: 'gf_br_thruster01',
        MainMiscEquip.BR_PIRATE: 'gf_br_thruster01',

        MainMiscEquip.KU_MAIN: 'gf_ku_thruster01',
        MainMiscEquip.KU_CIV: 'gf_ku_thruster01',
        MainMiscEquip.KU_PIRATE: 'gf_ku_thruster01',
        
        MainMiscEquip.CO_ORDER: 'gf_co_thruster01',
        MainMiscEquip.CO_CORSAIR: 'gf_co_thruster01',
        MainMiscEquip.CO_OUTCAST: 'gf_co_thruster01',
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
particles = {thruster_fx}
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
material_library = equipment\\models\\rh_equip.mat'''

    LI_THRUSTER_CORE = '''
DA_archetype = equipment\\models\\st\\li_thruster02.3db
material_library = equipment\\models\\li_equip.mat'''

    BR_THRUSTER_CORE = '''
DA_archetype = equipment\\models\\st\\br_thruster02.3db
material_library = equipment\\models\\br_equip.mat'''

    KU_THRUSTER_CORE = '''
DA_archetype = equipment\\models\\st\\ku_thruster02.3db
material_library = equipment\\models\\ku_equip.mat'''

    CO_THRUSTER_CORE = '''
DA_archetype = equipment\\models\\st\\co_thruster02.3db
material_library = equipment\\models\\ge_equip.mat'''

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

    def get_thruster_fx(self):
        return self.THRUSTER_FX_PER_TYPE[self.equip_type]

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

    def get_speed(self):
        speed = self.SPEED_PER_RATE[self.rate]

        if self.equip_type in self.RH_EQUIP:
            speed *= 1.1
        elif self.equip_type in self.BR_EQUIP:
            speed *= 0.9
        elif self.equip_type in self.CO_EQUIP:
            speed *= 1.2

        return speed

    def get_thruster_force(self):
        return int(self.get_speed() * self.LINEAR_DRAG)

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
            'thruster_fx': self.get_thruster_fx(),
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

    def get_ru_fullname(self):
        return self.get_ru_name()

    def get_ru_thrust_speed_text(self):
        return 'Скорость: {speed}'.format(
            speed=int(self.get_speed()),
        )

    def get_ru_description_content(self):
        content = []

        efficient_text = self.get_ru_equip_efficienty()
        if efficient_text:
            content.append(efficient_text)

        faction_features_text = RU_FEATURES_PER_FACTION.get(self.get_faction())
        if faction_features_text:
            content.append(faction_features_text)

        content.append(self.get_ru_thrust_speed_text())
        content.append(THRUSTER_SPEED_HINT)

        return content


RU_FEATURES_PER_FACTION = {
    MainMiscEquip.FACTION_RH: 'Рейнландские форсажи развивают повышенную скорость, но тратят больше энергии',
    MainMiscEquip.FACTION_LI: 'Форсажи Либерти на 50% лучше защищены от взрывов ракет, мин и т.п.',
    MainMiscEquip.FACTION_BR: 'Бретонские форсажи развивают низкую скорость, но при этом тратят значительно меньше энергии',
    MainMiscEquip.FACTION_KU: 'Форсажи Кусари тратят немного меньше энергии',
    MainMiscEquip.FACTION_CO: 'Форсажи кораблей пограничных миров развивают большую скорость, но при этом тратят значительно больше энергии',
}

THRUSTER_SPEED_HINT = 'Совет: Двигатель может влиять на скорость форсажа. С двигателями Рейнланда форсажи становятся медленнее, с двигателями Кусари быстрее'
