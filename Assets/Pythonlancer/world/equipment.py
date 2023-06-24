from world.lootable import LootableEquip
from world.markets import MarketEquip

class Equipment(LootableEquip, MarketEquip):
    CLASS_1 = 1
    CLASS_2 = 2
    CLASS_3 = 3
    CLASS_4 = 4
    CLASS_5 = 5
    CLASS_6 = 6
    CLASS_7 = 7
    CLASS_8 = 8
    CLASS_9 = 9
    CLASS_10 = 10

    BASE_CLASSES = [
        CLASS_1,
        CLASS_2,
        CLASS_3,
        CLASS_4,
        CLASS_5,
        CLASS_6,
        CLASS_7,
        CLASS_8,
        CLASS_9,
    ]

    RATE_1 = 0.06
    RATE_2 = 0.07
    RATE_3 = 0.07
    RATE_4 = 0.08
    RATE_5 = 0.08
    RATE_6 = 0.09
    RATE_7 = 0.10
    RATE_8 = 0.11
    RATE_9 = 0.12
    RATE_10 = 0.13
    RATE_11 = 0.15
    RATE_12 = 0.17
    RATE_13 = 0.18
    RATE_14 = 0.21
    RATE_15 = 0.24
    RATE_16 = 0.27
    RATE_17 = 0.30
    RATE_18 = 0.34
    RATE_19 = 0.39
    RATE_20 = 0.45
    RATE_21 = 0.55
    RATE_22 = 0.61
    RATE_23 = 0.68
    RATE_24 = 0.75
    RATE_25 = 0.82
    RATE_26 = 0.88
    RATE_27 = 1.00
    RATE_28 = 1.50

    MAIN_RATES = {
        CLASS_1: RATE_3,
        CLASS_2: RATE_6,
        CLASS_3: RATE_9,
        CLASS_4: RATE_12,
        CLASS_5: RATE_15,
        CLASS_6: RATE_18,
        CLASS_7: RATE_21,
        CLASS_8: RATE_24,
        CLASS_9: RATE_27,
    }

    CIV_RATES = {
        CLASS_1: RATE_1,
        CLASS_2: RATE_4,
        CLASS_3: RATE_7,
        CLASS_4: RATE_10,
        CLASS_5: RATE_13,
        CLASS_6: RATE_16,
        CLASS_7: RATE_19,
        CLASS_8: RATE_22,
        CLASS_9: RATE_25,
    }

    PIRATE_RATES = {
        CLASS_1: RATE_2,
        CLASS_2: RATE_5,
        CLASS_3: RATE_8,
        CLASS_4: RATE_11,
        CLASS_5: RATE_14,
        CLASS_6: RATE_17,
        CLASS_7: RATE_20,
        CLASS_8: RATE_23,
        CLASS_9: RATE_26,
    }

    SHIPCLASS_FIGHTER = 1
    SHIPCLASS_ELITE = 2
    SHIPCLASS_FREIGHTER = 3

    SHIPCLASSES = [SHIPCLASS_FIGHTER, SHIPCLASS_ELITE, SHIPCLASS_FREIGHTER]

    FACTION_RH = 1
    FACTION_LI = 2
    FACTION_BR = 3
    FACTION_KU = 4
    FACTION_CO = 5

    RH_LETTER = 'rh'
    LI_LETTER = 'li'
    BR_LETTER = 'br'
    KU_LETTER = 'ku'
    CO_LETTER = 'co'
    GE_LETTER = 'ge'
    PI_LETTER = 'pi'
    
    LOOT_DEFAULTS = '''
debris_type = debris_normal
parent_impulse = 20
child_impulse = 80
separation_explosion = sever_debris'''

    DEFAULT_GOOD_TEMPLATE = '''[Good]
nickname = {nickname}
equipment = {nickname}
category = equipment
price = {price}
item_icon = {icon}
combinable = {combinable}'''

    def get_good_template(self):
        return self.DEFAULT_GOOD_TEMPLATE

    def get_equipment_class_digit(self):
        if (self.equipment_class < 10):
            return '0{0}'.format(self.equipment_class)
        else:
            return str(self.equipment_class)

    def get_shipclass_name(self):
        if self.ship_class == self.SHIPCLASS_FIGHTER:
            return 'FIGHTER'
        if self.ship_class == self.SHIPCLASS_ELITE:
            return 'ELITE'
        if self.ship_class == self.SHIPCLASS_FREIGHTER:
            return 'FREIGHTER'

        raise Exception('unknown shipclass for shipclass name')

    def get_shipclass_name_lower(self):
        self.get_shipclass_name().lower()

    def get_shipclass_hp_type_string(self):
        if self.ship_class == self.SHIPCLASS_FIGHTER:
            return 'fighter'
        if self.ship_class == self.SHIPCLASS_ELITE:
            return 'elite'
        if self.ship_class == self.SHIPCLASS_FREIGHTER:
            return 'freighter'

        raise Exception('unknown shipclass for hp type string')

    def get_main_rate(self):
        return self.MAIN_RATES.get(self.equipment_class)

    def get_civ_rate(self):
        return self.CIV_RATES.get(self.equipment_class)

    def get_pirate_rate(self):
        return self.PIRATE_RATES.get(self.equipment_class)

    DROP_WORTH_PER_CLASS = {
        CLASS_1: 5000,
        CLASS_2: 8000,
        CLASS_3: 11000,
        CLASS_4: 25396,
        CLASS_5: 52183,
        CLASS_6: 105206,
        CLASS_7: 211397,
        CLASS_8: 378331,
        CLASS_9: 646965,
        CLASS_10: 646965,
    }

    def get_drop_min_worth(self):
        return self.DROP_WORTH_PER_CLASS[self.equipment_class]

    def get_drop_worth_mult(self):
        return self.get_drop_min_worth()

    CLASS_TO_MARK = {
        CLASS_1: 'Mk.I',
        CLASS_2: 'Mk.II',
        CLASS_3: 'Mk.III',
        CLASS_4: 'Mk.IV',
        CLASS_5: 'Mk.V',
        CLASS_6: 'Mk.VI',
        CLASS_7: 'Mk.VII',
        CLASS_8: 'Mk.VIII',
        CLASS_9: 'Mk.IX',
        CLASS_10: 'Mk.X',
    }

    def get_mark_name(self):
        return self.CLASS_TO_MARK[self.equipment_class]

    def get_ru_equip_name(self):
        raise NotImplementedError('ru equip name must be defined')

    def get_ru_base_name(self):
        raise NotImplementedError('ru base name must be defined')

    def get_ru_shipclass_name(self):
        if self.ship_class == self.SHIPCLASS_FIGHTER:
            return 'Перехв'
        if self.ship_class == self.SHIPCLASS_ELITE:
            return 'Истреб'
        if self.ship_class == self.SHIPCLASS_FREIGHTER:
            return 'Груз'

        raise Exception('unknown ship class')

    def get_ru_name(self):
        raise NotImplementedError('ru name builder not defined')



class MainMiscEquip(Equipment):
    FACTION_RH = 1
    FACTION_LI = 2
    FACTION_BR = 3
    FACTION_KU = 4
    FACTION_CO = 5

    RH_MAIN = 1
    RH_CIV = 2
    RH_PIRATE = 3

    LI_MAIN = 4
    LI_CIV = 5
    LI_PIRATE = 6

    BR_MAIN = 7
    BR_CIV = 8
    BR_PIRATE = 9

    KU_MAIN = 10
    KU_CIV = 11
    KU_PIRATE = 12

    CO_ORDER = 13
    CO_CORSAIR = 14
    CO_OUTCAST = 15

    RH_EQUIP = [RH_MAIN, RH_CIV, RH_PIRATE]
    LI_EQUIP = [LI_MAIN, LI_CIV, LI_PIRATE]
    BR_EQUIP = [BR_MAIN, BR_CIV, BR_PIRATE]
    KU_EQUIP = [KU_MAIN, KU_CIV, KU_PIRATE]
    CO_EQUIP = [CO_ORDER, CO_CORSAIR, CO_OUTCAST]

    ALL_EQUIP_TYPES = RH_EQUIP + LI_EQUIP + BR_EQUIP + KU_EQUIP + CO_EQUIP

    MAIN_EQUIP = [RH_MAIN, LI_MAIN, BR_MAIN, KU_MAIN, CO_ORDER]
    CIV_EQUIP = [RH_CIV, LI_CIV, BR_CIV, KU_CIV, CO_OUTCAST]
    PIRATE_EQUIP = [RH_PIRATE, LI_PIRATE, BR_PIRATE, KU_PIRATE, CO_CORSAIR]

    MAX_PRICE_FIGHTER = 240000
    MAX_PRICE_ELITE = 260000
    MAX_PRICE_FREIGHTER = 320000

    def __init__(self, equip_type, equipment_class, ids_name, ids_info):
        self.equip_type = equip_type
        self.equipment_class = equipment_class

        self.set_rate()

        self.ids_name = ids_name
        self.ids_info = ids_info

    def get_base_nickname(self):
        if self.equip_type == self.RH_MAIN:
            return 'rh'
        if self.equip_type == self.RH_CIV:
            return 'rh_civ'
        if self.equip_type == self.RH_PIRATE:
            return 'rh_pirate'

        if self.equip_type == self.LI_MAIN:
            return 'li'
        if self.equip_type == self.LI_CIV:
            return 'li_civ'
        if self.equip_type == self.LI_PIRATE:
            return 'li_pirate'

        if self.equip_type == self.BR_MAIN:
            return 'br'
        if self.equip_type == self.BR_CIV:
            return 'br_civ'
        if self.equip_type == self.BR_PIRATE:
            return 'br_pirate'

        if self.equip_type == self.KU_MAIN:
            return 'ku'
        if self.equip_type == self.KU_CIV:
            return 'ku_civ'
        if self.equip_type == self.KU_PIRATE:
            return 'ku_pirate'

        if self.equip_type == self.CO_ORDER:
            return 'or'
        if self.equip_type == self.CO_CORSAIR:
            return 'co'
        if self.equip_type == self.CO_OUTCAST:
            return 'out'

        raise Exception('unknown base nickname')

    def set_rate(self):
        if self.equip_type in self.MAIN_EQUIP:
            self.rate = self.get_main_rate()
        if self.equip_type in self.CIV_EQUIP:
            self.rate = self.get_civ_rate()
        if self.equip_type in self.PIRATE_EQUIP:
            self.rate = self.get_pirate_rate()

    def get_faction_code(self):
        if self.equip_type in self.RH_EQUIP:
            return 'rh'
        if self.equip_type in self.LI_EQUIP:
            return 'li'
        if self.equip_type in self.BR_EQUIP:
            return 'br'
        if self.equip_type in self.KU_EQUIP:
            return 'ku'
        if self.equip_type in self.CO_EQUIP:
            return 'co'

        raise Exception('unknown faction code')



class MainInternalEquip(MainMiscEquip):

    MAIN_INTERNAL_GOOD_TEMPLATE = '''[Good]
nickname = {nickname}
equipment = {nickname}
category = equipment
price = {price}
item_icon = {icon}
combinable = {combinable}
shop_archetype = {model}
attachment_archetype = {model}'''

    def __init__(self, equip_type, ship_class, equipment_class, ids_name, ids_info):
        self.equip_type = equip_type
        self.ship_class = ship_class
        self.equipment_class = equipment_class

        self.set_rate()

        self.ids_name = ids_name
        self.ids_info = ids_info

    def get_equip_model(self):
        raise NotImplementedError

    def get_good_template(self):
        return self.MAIN_INTERNAL_GOOD_TEMPLATE

    def get_good_template_params(self):
        nickname = self.get_nickname()
        return {
            'nickname': nickname,
            'equipment': nickname,
            'price': self.get_price(),
            'icon': self.get_icon(),
            'model': self.get_equip_model(),
            'combinable': False
        }

    def get_max_price(self):
        if self.ship_class == self.SHIPCLASS_FIGHTER:
            return self.MAX_PRICE_FIGHTER
        if self.ship_class == self.SHIPCLASS_ELITE:
            return self.MAX_PRICE_ELITE
        if self.ship_class == self.SHIPCLASS_FREIGHTER:
            return self.MAX_PRICE_FREIGHTER

        raise Exception('unknown max price')

    def get_ru_name(self):
        return '{equip} {model} {mark} [{shipclass}]'.format(
            equip=self.get_ru_equip_name(),
            model=self.get_ru_base_name(),
            mark=self.get_mark_name(),
            shipclass=self.get_ru_shipclass_name(),
        )


class DefaultGood(object):

    DEFAULT_GOOD_TEMPLATE = '''[Good]
nickname = {nickname}
equipment = {nickname}
category = equipment
price = {price}
item_icon = {icon}
combinable = {combinable}'''

    def get_price(self):
        raise NotImplementedError()

    def get_icon(self):
        raise NotImplementedError

    def get_good_template(self):
        return self.DEFAULT_GOOD_TEMPLATE

    def get_good_template_params(self):
        nickname = self.get_nickname()
        return {
            'nickname': nickname,
            'equipment': nickname,
            'price': self.get_price(),
            'icon': self.get_icon(),
            'combinable': False
        }

    def get_good(self):
        return self.get_good_template().format(**self.get_good_template_params())


class AdoxaEquipClassGood(DefaultGood):

    MAIN_INTERNAL_GOOD_TEMPLATE = '''[Good]
nickname = {nickname}
equipment = {nickname}
category = equipment
price = {price}
item_icon = {icon}
combinable = {combinable}
shop_archetype = {model}
attachment_archetype = {model}'''

    def get_equip_model(self):
        raise NotImplementedError

    def get_good_template(self):
        return self.MAIN_INTERNAL_GOOD_TEMPLATE

    def get_good_template_params(self):
        nickname = self.get_nickname()
        return {
            'nickname': nickname,
            'equipment': nickname,
            'price': self.get_price(),
            'icon': self.get_icon(),
            'model': self.get_equip_model(),
            'combinable': False
        }



class Icon(object):
    ICONS_FOLDER = 'equipment\\models\\icons\\'

    ICON_RH_LIGHTGUN = 'rh\\rh_lightgun.3db'
    ICON_RH_HEAVYGUN = 'rh\\rh_heavygun.3db'
    ICON_RH_THRUSTGUN = 'rh\\rh_miscgun.3db'
    ICON_RH_LAUNCHER = 'rh\\rh_launcher.3db'
    ICON_RH_UBERGUN = 'rh\\rh_ubergun.3db'

    ICON_LI_LIGHTGUN = 'li\\li_lightgun.3db'
    ICON_LI_HEAVYGUN = 'li\\li_heavygun.3db'
    ICON_LI_THRUSTGUN = 'li\\li_miscgun.3db'
    ICON_LI_LAUNCHER = 'li\\li_launcher.3db'
    ICON_LI_UBERGUN = 'li\\li_ubergun.3db'

    ICON_BR_LIGHTGUN = 'br\\br_lightgun.3db'
    ICON_BR_HEAVYGUN = 'br\\br_heavygun.3db'
    ICON_BR_THRUSTGUN = 'br\\br_miscgun.3db'
    ICON_BR_LAUNCHER = 'br\\br_launcher.3db'
    ICON_BR_UBERGUN = 'br\\br_ubergun.3db'

    ICON_KU_LIGHTGUN = 'ku\\ku_lightgun.3db'
    ICON_KU_HEAVYGUN = 'ku\\ku_heavygun.3db'
    ICON_KU_THRUSTGUN = 'ku\\ku_miscgun.3db'
    ICON_KU_LAUNCHER = 'ku\\ku_launcher.3db'
    ICON_KU_UBERGUN = 'ku\\ku_ubergun.3db'

    ICON_CO_LIGHTGUN = 'co\\co_lightgun.3db'
    ICON_CO_HEAVYGUN = 'co\\co_heavygun.3db'
    ICON_CO_THRUSTGUN = 'co\\co_miscgun.3db'
    ICON_CO_LAUNCHER = 'co\\co_launcher.3db'
    ICON_CO_UBERGUN = 'co\\co_ubergun.3db'

    ICON_GE_HARPOON = 'ge\\ge_harpoon.3db'
    ICON_GE_TRP_LAUNCHER = 'ge\\ge_trp_launcher.3db'
    ICON_GE_UBERGUN = 'ge\\ge_ubergun.3db'

    ICON_PATH_TEMPLATE = '{root}{icon}'

    @staticmethod
    def get_icon_path(icon):
        return Icon.ICON_PATH_TEMPLATE.format(root=Icon.ICONS_FOLDER, icon=icon)


class MainEquipPrice(object):

    PRICE_PER_RATE = {
        Equipment.RATE_1: 0.0038,
        Equipment.RATE_2: 0.0040,
        Equipment.RATE_3: 0.0042,
        Equipment.RATE_4: 0.0063,
        Equipment.RATE_5: 0.0068,
        Equipment.RATE_6: 0.0075,
        Equipment.RATE_7: 0.0130,
        Equipment.RATE_8: 0.0140,
        Equipment.RATE_9: 0.0155,
        Equipment.RATE_10: 0.0280,
        Equipment.RATE_11: 0.0300,
        Equipment.RATE_12: 0.0320,
        Equipment.RATE_13: 0.0600,
        Equipment.RATE_14: 0.0610,
        Equipment.RATE_15: 0.0650,
        Equipment.RATE_16: 0.1000,
        Equipment.RATE_17: 0.1100,
        Equipment.RATE_18: 0.1200,
        Equipment.RATE_19: 0.1800,
        Equipment.RATE_20: 0.1950,
        Equipment.RATE_21: 0.2100,
        Equipment.RATE_22: 0.4000,
        Equipment.RATE_23: 0.4300,
        Equipment.RATE_24: 0.4600,
        Equipment.RATE_25: 0.8200,
        Equipment.RATE_26: 0.9600,
        Equipment.RATE_27: 1.0000,
        Equipment.RATE_28: 1.5000,
    }

    def get_price_multipler(self):
        return self.PRICE_PER_RATE[self.rate]

    def get_price(self):
        return int(self.get_max_price() * self.get_price_multipler())
