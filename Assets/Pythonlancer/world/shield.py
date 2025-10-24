from world.equipment import DefaultGood, MainEquipPrice, MainMiscEquip
from world.power import BasePower
from world import level


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

    def get_market_level(self):
        return level.SHIELD_LEVEL_PER_CLASS[self.equipment_class]

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
            'ids_name': self.get_ids_name(),
            'ids_info': self.get_ids_info(),
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

    EN_NAME_PER_TYPE = {
        MainMiscEquip.RH_MAIN: 'Bastion',
        MainMiscEquip.RH_CIV: 'Rampart',
        MainMiscEquip.RH_PIRATE: 'Palisade',

        MainMiscEquip.LI_MAIN: 'Protector',
        MainMiscEquip.LI_CIV: 'Sentry',
        MainMiscEquip.LI_PIRATE: 'Sentinel',

        MainMiscEquip.BR_MAIN: 'Brigantine',
        MainMiscEquip.BR_CIV: 'Armet',
        MainMiscEquip.BR_PIRATE: 'Cuisse',

        MainMiscEquip.KU_MAIN: 'Barrier',
        MainMiscEquip.KU_CIV: 'Amulet',
        MainMiscEquip.KU_PIRATE: 'Pourpoint',

        MainMiscEquip.CO_ORDER: 'Champion',
        MainMiscEquip.CO_CORSAIR: 'Doublet',
        MainMiscEquip.CO_OUTCAST: 'Morion',
    }

    def get_ru_equip_name(self):
        return 'Щит'

    def get_ru_equip_fullname(self):
        return 'Щит'

    def get_en_equip_name(self):
        return 'Shield'

    def get_en_equip_fullname(self):
        return 'Shield'

    def get_ru_base_name(self):
        return self.RU_NAME_PER_TYPE[self.equip_type]

    def get_en_base_name(self):
        return self.EN_NAME_PER_TYPE[self.equip_type]

    def get_ru_description_content(self):
        content = []

        efficient_text = self.get_ru_equip_efficienty()
        if efficient_text:
            content.append(efficient_text)

        faction_features_text = RU_FEATURES_PER_FACTION.get(self.get_faction())
        if faction_features_text:
            content.append(faction_features_text)

        shipclass_restrict_text = RU_RESTRICTIONS_PER_SHIPCLASS.get(self.ship_class)
        if shipclass_restrict_text:
            content.append(shipclass_restrict_text)

        shipclass_features_text = RU_FEATURES_PER_SHIPCLASS.get(self.ship_class)
        if shipclass_features_text:
            content.append(shipclass_features_text)

        content.append(RU_SHIELD_HINT)

        return content

    def get_en_description_content(self):
        content = []

        efficient_text = self.get_en_equip_efficienty()
        if efficient_text:
            content.append(efficient_text)

        faction_features_text = EN_FEATURES_PER_FACTION.get(self.get_faction())
        if faction_features_text:
            content.append(faction_features_text)

        shipclass_restrict_text = EN_RESTRICTIONS_PER_SHIPCLASS.get(self.ship_class)
        if shipclass_restrict_text:
            content.append(shipclass_restrict_text)

        shipclass_features_text = EN_FEATURES_PER_SHIPCLASS.get(self.ship_class)
        if shipclass_features_text:
            content.append(shipclass_features_text)

        content.append(EN_SHIELD_HINT)

        return content


RU_FEATURES_PER_FACTION = {
    MainMiscEquip.FACTION_RH: 'Рейнландские щиты на 10% объемнее, но при этом тратят на 10% больше энергии во время восстановления',
    MainMiscEquip.FACTION_LI: 'Щиты Либерти тратят на 25% меньше энергии во время восстановления',
    MainMiscEquip.FACTION_BR: 'Бретонские щиты на 2 секунды меньше находятся в выключенном состоянии',
    MainMiscEquip.FACTION_KU: 'Щиты Кусари на 10% быстрее регенерируются, но постоянно тратят на 25% больше энергии',
    MainMiscEquip.FACTION_CO: 'Щиты кораблей пограничных миров тратят на 40% меньше посстоянно затрачиваемой энергии, но при этом на 10% менее объемны и на 10% медленнее регенерируются',
}


RU_RESTRICTIONS_PER_SHIPCLASS = {
    MainMiscEquip.SHIPCLASS_FIGHTER: 'Этот щит можно установить только на легкий истребитель',
    MainMiscEquip.SHIPCLASS_ELITE: 'Этот щит можно установить только на тяжелый истребитель',
    MainMiscEquip.SHIPCLASS_FREIGHTER: 'Этот щит можно установить только на грузовик или CSV',
}


RU_FEATURES_PER_SHIPCLASS = {
    MainMiscEquip.SHIPCLASS_FIGHTER: 'Щиты легких истребителей лучше сопротивляются орудиям станций и крупных кораблей',
    MainMiscEquip.SHIPCLASS_ELITE: None,
    MainMiscEquip.SHIPCLASS_FREIGHTER: 'Щиты грузовиков имеют 75% защиту от всех противощитовых пушек',
}

RU_SHIELD_HINT = 'Совет: Полностью заряженный щит потребляет меньше энергии, чем заряжаемый/отключенный'


EN_FEATURES_PER_FACTION = {
    MainMiscEquip.FACTION_RH: 'Rheinland shields have 10% more capacity, but it required 10% more energy for regeneration',
    MainMiscEquip.FACTION_LI: 'Liberty shields requires 25% less energy for regeneration',
    MainMiscEquip.FACTION_BR: 'Bretonia shields holds on 2 seconds less in deactivated state',
    MainMiscEquip.FACTION_KU: 'Kusari shields have 10% better regeneration, but requires additional 25% constant energy drain',
    MainMiscEquip.FACTION_CO: 'Border World shields requires 40% less constant energy drain, but have 10% less capacity and 10% less regeneration speed',
}


EN_RESTRICTIONS_PER_SHIPCLASS = {
    MainMiscEquip.SHIPCLASS_FIGHTER: 'This shield can be mounted on light fighters',
    MainMiscEquip.SHIPCLASS_ELITE: 'This shield can be mounted on heavy fighters',
    MainMiscEquip.SHIPCLASS_FREIGHTER: 'This shield can be mounted on freighters of CSVs',
}


EN_FEATURES_PER_SHIPCLASS = {
    MainMiscEquip.SHIPCLASS_FIGHTER: 'Shields of light fighters have better defence from station and capital ship turrets',
    MainMiscEquip.SHIPCLASS_ELITE: None,
    MainMiscEquip.SHIPCLASS_FREIGHTER: 'Freighter shields have 75% defence against shield guns',
}

EN_SHIELD_HINT = 'Hint: Full regenerated shield drains less energy than in rechargeable state'


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
