from world.equipment import DefaultGood, MainEquipPrice, MainMiscEquip
from world.power import BasePower


class Shield(MainEquipPrice, DefaultGood, BasePower):
    DROP_CHANCE = 10

    MAX_SHIELD_CAPACITY_FIGHTER = 12000
    MAX_SHIELD_CAPACITY_ELITE = 15000
    MAX_SHIELD_CAPACITY_FREIGHTER = 18000

    MAX_SHIELD_REGEN_FIGHTER = 400
    MAX_SHIELD_REGEN_ELITE = 500
    MAX_SHIELD_REGEN_FREIGHTER = 700

    SHIELD_ACTIVE_POWER_FACTOR = 0.1
    SHIELD_PASSIVE_POWER_FACTOR = 0.2

    SHIELD_MAX_HIT_PTS = 8000

    SHIELD_OFFLINE_REBUILD_TIME = 10

    SHIELD_TEMPLATE = '''[ShieldGenerator]
nickname = {nickname}
ids_name = {ids_name}
ids_info = {ids_info}
hp_type = {hp_type}
shield_type = {shield_type}
hit_pts = {hit_pts}
offline_rebuild_time = {offline_rebuild_time}
max_capacity = {max_capacity}
regeneration_rate = {regeneration_rate}
rebuild_power_draw = {rebuild_power_draw}
constant_power_draw = {constant_power_draw}{loot_props}{shield_defaults}{faction_shield_core}'''

    SHIELD_DEFAULTS = '''
HP_child = HpConnect
explosion_resistance = 0.25
volume = 0
mass = 10
offline_threshold = 0.15
LODranges = 0, 600
lootable = true
shield_collapse_sound = shield_offline
shield_rebuilt_sound = shield_rebuilt'''

    RH_SHIELD_CORE = '''
DA_archetype = equipment\\models\\st\\rh_radiation_shield.3db
material_library = equipment\\models\\rh_equip.mat
shield_collapse_particle = rh_shield_offline
shield_hit_effects = {hit_one}, gf_rh_shield01
shield_hit_effects = {hit_two}, gf_rh_shield02
shield_hit_effects = {hit_three}, gf_rh_shield03'''

    LI_SHIELD_CORE = '''
DA_archetype = equipment\\models\\st\\li_disruptor_shield.3db
material_library = equipment\\models\\li_equip.mat
shield_collapse_particle = li_shield_offline
shield_hit_effects = {hit_one}, gf_li_shield01
shield_hit_effects = {hit_two}, gf_li_shield02
shield_hit_effects = {hit_three}, gf_li_shield03'''

    BR_SHIELD_CORE = '''
DA_archetype = equipment\\models\\st\\br_conversion_shield.3db
material_library = equipment\\models\\br_equip.mat
shield_collapse_particle = br_shield_offline
shield_hit_effects = {hit_one}, gf_br_shield01
shield_hit_effects = {hit_two}, gf_br_shield02
shield_hit_effects = {hit_three}, gf_br_shield03'''

    KU_SHIELD_CORE = '''
DA_archetype = equipment\\models\\st\\ku_displacement_shield.3db
material_library = equipment\\models\\ku_equip.mat
shield_collapse_particle = ku_shield_offline
shield_hit_effects = {hit_one}, gf_ku_shield01
shield_hit_effects = {hit_two}, gf_ku_shield02
shield_hit_effects = {hit_three}, gf_ku_shield03'''

    CO_SHIELD_CORE = '''
DA_archetype = equipment\\models\\st\\li_refractor_shield.3db
material_library = equipment\\models\\li_equip.mat
shield_collapse_particle = co_shield_offline
shield_hit_effects = {hit_one}, gf_pi_shield01
shield_hit_effects = {hit_two}, gf_pi_shield02
shield_hit_effects = {hit_three}, gf_pi_shield03'''

    RH_SHIELD_ICON = 'equipment\\models\\icons\\rh\\rh_shield.3db'
    LI_SHIELD_ICON = 'equipment\\models\\icons\\li\\li_shield.3db'
    BR_SHIELD_ICON = 'equipment\\models\\icons\\br\\br_shield.3db'
    KU_SHIELD_ICON = 'equipment\\models\\icons\\ku\\ku_shield.3db'
    CO_SHIELD_ICON = 'equipment\\models\\icons\\co\\co_shield.3db'

    def get_shield_core_template_params(self):
        return {
            'hit_one': 0,
            'hit_two': 100,
            'hit_three': 500,
        }

    def get_shield_core_template(self):
        if self.equip_type in self.RH_EQUIP:
            return self.RH_SHIELD_CORE
        if self.equip_type in self.LI_EQUIP:
            return self.LI_SHIELD_CORE
        if self.equip_type in self.BR_EQUIP:
            return self.BR_SHIELD_CORE
        if self.equip_type in self.KU_EQUIP:
            return self.KU_SHIELD_CORE
        if self.equip_type in self.CO_EQUIP:
            return self.CO_SHIELD_CORE

        raise Exception('unknown shield core')

    def get_shield_core(self):
        return self.get_shield_core_template().format(**self.get_shield_core_template_params())

    def get_nickname(self):
        return '{name}_shield_{digit}_{shipclass}'.format(
            name=self.get_base_nickname(),
            digit=self.get_equipment_class_digit(),
            shipclass=self.get_shipclass_name()
        )

    def get_shield_hit_pts(self):
        return self.SHIELD_MAX_HIT_PTS * self.rate

    def get_shield_type(self):
        return 'S_{faction_code}_{shipclass_lower}'.format(
            faction_code=self.get_faction_code(),
            shipclass_lower=self.get_shipclass_name_lower()
        )

    def get_shield_hp_type(self):
        return 'hp_{shipclass}_shield_special_{equipment_class}'.format(
            shipclass=self.get_shipclass_hp_type_string(),
            equipment_class=self.equipment_class
        )

    def get_offline_rebuild_time(self):
        offline_time = self.SHIELD_OFFLINE_REBUILD_TIME

        if self.equip_type in self.BR_EQUIP:
            offline_time -= 2

        return offline_time

    def get_max_shield_capacity(self):
        if self.ship_class == self.SHIPCLASS_FIGHTER:
            return self.MAX_SHIELD_CAPACITY_FIGHTER
        if self.ship_class == self.SHIPCLASS_ELITE:
            return self.MAX_SHIELD_CAPACITY_ELITE
        if self.ship_class == self.SHIPCLASS_FREIGHTER:
            return self.MAX_SHIELD_CAPACITY_FREIGHTER

        raise Exception('unkown ship shield capacity')

    def get_shield_capacity(self):
        capacity = self.get_max_shield_capacity()

        if self.equip_type in self.RH_EQUIP:
            capacity *= 1.1
        elif self.equip_type in self.CO_EQUIP:
            capacity *= 0.9

        return capacity * self.rate

    def get_max_shield_regen(self):
        if self.ship_class == self.SHIPCLASS_FIGHTER:
            return self.MAX_SHIELD_REGEN_FIGHTER
        if self.ship_class == self.SHIPCLASS_ELITE:
            return self.MAX_SHIELD_REGEN_ELITE
        if self.ship_class == self.SHIPCLASS_FREIGHTER:
            return self.MAX_SHIELD_REGEN_FREIGHTER

        raise Exception('unkown ship shield regen')

    def get_shield_regeneration_rate(self):
        regen = self.get_max_shield_regen()

        if self.equip_type in self.KU_EQUIP:
            regen *= 1.1
        elif self.equip_type in self.CO_EQUIP:
            regen *= 0.9

        return regen * self.rate

    def get_shield_rebuild_power_draw(self):
        required_power = self.get_power_regen() * self.SHIELD_ACTIVE_POWER_FACTOR

        if self.equip_type in self.RH_EQUIP:
            required_power *= 1.1
        elif self.equip_type in self.LI_EQUIP:
            required_power *= 0.75

        return required_power

    def get_shield_constant_power_draw(self):
        required_power = self.get_power_regen() * self.SHIELD_PASSIVE_POWER_FACTOR

        if self.equip_type in self.KU_EQUIP:
            required_power *= 1.25
        elif self.equip_type in self.BR_EQUIP:
            required_power *= 0.6

        return required_power

    def get_shield_template_params(self):
        return {
            'nickname': self.get_nickname(),
            'ids_name': self.ids_name,
            'ids_info': self.ids_info,
            'hp_type': self.get_shield_hp_type(),
            'hit_pts': self.get_shield_hit_pts(),
            'shield_type': self.get_shield_type(),
            'offline_rebuild_time': self.get_offline_rebuild_time(),
            'max_capacity': self.get_shield_capacity(),
            'regeneration_rate': self.get_shield_regeneration_rate(),
            'rebuild_power_draw': self.get_shield_rebuild_power_draw(),
            'constant_power_draw': self.get_shield_constant_power_draw(),
            'loot_props': self.LOOT_DEFAULTS,
            'shield_defaults': self.SHIELD_DEFAULTS,
            'faction_shield_core': self.get_shield_core(),
        }

    def get_equip(self):
        return self.SHIELD_TEMPLATE.format(**self.get_shield_template_params())

    def get_icon(self):
        if self.equip_type in self.RH_EQUIP:
            return self.RH_SHIELD_ICON
        if self.equip_type in self.LI_EQUIP:
            return self.LI_SHIELD_ICON
        if self.equip_type in self.BR_EQUIP:
            return self.BR_SHIELD_ICON
        if self.equip_type in self.KU_EQUIP:
            return self.KU_SHIELD_ICON
        if self.equip_type in self.CO_EQUIP:
            return self.CO_SHIELD_ICON

        raise Exception('unknown shield icon')


    RU_NAME_PER_TYPE = {
        MainMiscEquip.RH_MAIN: 'Бастион',
        MainMiscEquip.RH_CIV: 'Укрытие',
        MainMiscEquip.RH_PIRATE: 'Частокол',

        MainMiscEquip.LI_MAIN: 'Заступник',
        MainMiscEquip.LI_CIV: 'Охранник',
        MainMiscEquip.LI_PIRATE: 'Хранитель',

        MainMiscEquip.BR_MAIN: 'Бригантина',
        MainMiscEquip.BR_CIV: 'Армет',
        MainMiscEquip.BR_PIRATE: 'Куиззе',

        MainMiscEquip.KU_MAIN: 'Барьер',
        MainMiscEquip.KU_CIV: 'Амулет',
        MainMiscEquip.KU_PIRATE: 'Оберег',

        MainMiscEquip.CO_ORDER: 'Кираса',
        MainMiscEquip.CO_CORSAIR: 'Дублет',
        MainMiscEquip.CO_OUTCAST: 'Морион',
    }

    def get_ru_equip_name(self):
        return 'Щит'

    def get_ru_base_name(self):
        return self.RU_NAME_PER_TYPE[self.equip_type]



class ShieldNPC(Shield):

    MAX_SHIELD_REGEN_FIGHTER = 200
    MAX_SHIELD_REGEN_ELITE = 250
    MAX_SHIELD_REGEN_FREIGHTER = 350

    SHIELD_DEFAULTS = '''
HP_child = HpConnect
explosion_resistance = 0.25
volume = 0
mass = 10
offline_threshold = 0.15
LODranges = 0, 600
lootable = false
shield_collapse_sound = shield_offline
shield_rebuilt_sound = shield_rebuilt'''

    def get_nickname(self):
        return '{name}_shield_{digit}_{shipclass}_npc'.format(
            name=self.get_base_nickname(),
            digit=self.get_equipment_class_digit(),
            shipclass=self.get_shipclass_name()
        )

    def get_price(self):
        return 100  # NPC equipment - not for sell
