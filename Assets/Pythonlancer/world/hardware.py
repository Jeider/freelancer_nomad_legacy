from world.names import *
from world.equipment import Equipment, DefaultGood
from text.infocards import InfocardBuilder
from text.strings import MultiString as MS


class RepairKit(Equipment, DefaultGood):
    COMBINABLE = True
    WEAPON_CODE = REPAIR
    ARCHETYPE = 'RepairKit'

    INFO = MS('Комплект наноботов, предназначенный для быстрого ремонта корпуса.',
              'Nanobots pack, supposed to fast repair your ship hull on the flight.')

    PRICE_PER_MARK = [
        200,
        300,
        500,
        750,
        1000,
    ]

    REPAIR_PER_MARK = [
        500,
        600,
        800,
        1000,
        1500,
    ]

    RU_NAME_PER_MARK = [
        'Наноботы',
        'Модифициров. наноботы',
        'Продвинутые наноботы',
        'Улучшенные наноботы',
        'Элитные наноботы',
    ]

    RU_DESC_NAME_PER_MARK = [
        'Базовый комплект наноботов',
        'Модифицированный комплект наноботов',
        'Продвинутый комплект наноботов',
        'Улучшенный комплект наноботов',
        'Элитный комплект наноботов',
    ]

    EN_NAME_PER_MARK = [
        'Nanobots',
        'Modif. Nanobots',
        'Imp. Nanobots',
        'Adv. Nanobots',
        'Elite Nanobots',
    ]

    EN_DESC_NAME_PER_MARK = [
        'Basic Nanobots pack',
        'Modified Nanobots pack',
        'Improved Nanobots pack',
        'Advanced Nanobots pack',
        'Elite Nanobots pack',
    ]

    def __init__(self, ids, equipment_class):
        self.ids = ids

        self.equipment_class = equipment_class
        self.mark = equipment_class

        self.rate = self.get_rate()

        self.ids_name = ids.new_name(
            MS(
                self.get_ru_name(),
                self.get_en_name()
            )
        )
        self.ids_info = ids.new_info(
            MS(
                InfocardBuilder.build_equip_infocard(
                    self.get_ru_fullname(),
                    self.get_ru_description_content()
                ),
                InfocardBuilder.build_equip_infocard(
                    self.get_en_fullname(),
                    self.get_en_description_content()
                )
            )
        )

    def get_price(self):
        return self.PRICE_PER_MARK[self.mark-1]

    def get_market_level(self):
        return -1

    def get_nickname(self):
        return f'{self.WEAPON_CODE}_{self.mark:02d}'

    def get_rate(self):
        return self.get_civ_rate()

    def get_ru_name(self):
        return self.RU_NAME_PER_MARK[self.mark-1]

    def get_ru_fullname(self):
        return self.RU_DESC_NAME_PER_MARK[self.mark-1]

    def get_ru_description_content(self):
        content = []

        content.append(self.INFO.get_ru())

        return content

    def get_en_name(self):
        return self.EN_NAME_PER_MARK[self.mark-1]

    def get_en_fullname(self):
        return self.EN_DESC_NAME_PER_MARK[self.mark-1]

    def get_en_description_content(self):
        content = []

        content.append(self.INFO.get_en())

        return content

    def get_ids_name(self):
        return self.ids_name.id

    def get_ids_info(self):
        return self.ids_info.id

    def get_icon(self):
        return r'equipment\models\commodities\nn_icons\EQUIPICON_nanobots.3db'

    def get_repair_hit_pts(self):
        return self.REPAIR_PER_MARK[self.mark-1]

    def get_equip(self):
        equip_name = self.get_nickname()
        return f'''[LootCrate]
nickname = {equip_name}_loot
DA_archetype = equipment\\models\\commodities\\crates\\crate_grey.3db
LODranges = 0, 150, 350
hit_pts = 250
mass = 10
explosion_arch = debris_normal

[{self.ARCHETYPE}]
nickname = {equip_name}
ids_name = {self.get_ids_name()}
ids_info = {self.get_ids_info()}
volume = 0.000000
mass = 1
hit_pts = {self.get_repair_hit_pts()}
loot_appearance = {equip_name}_loot
units_per_container = 15
lootable = true
'''


class ShieldBattery(RepairKit):
    COMBINABLE = True
    WEAPON_CODE = BATTERY
    ARCHETYPE = 'ShieldBattery'

    INFO = MS('Набор батарей, предназначенных для быстрой перезарядки щита. Используйте в экстренных ситуациях, '
              'когда вам нужно восстановить щит не дожидаясь его регенерации.',
              'Batteries pack, supposed to fast restore your shield. Use it in extremal situations, when you '
              'need to restore shield fast without waiting for regeneration.')

    PRICE_PER_MARK = [
        200,
        300,
        500,
        750,
        1000,
    ]

    REPAIR_PER_MARK = [
        250,
        300,
        400,
        500,
        750,
    ]

    RU_NAME_PER_MARK = [
        'Батареи щита',
        'Модифициров. батареи щита',
        'Продвинутые батареи щита',
        'Улучшенные батареи щита',
        'Элитные батареи щита',
    ]

    RU_DESC_NAME_PER_MARK = [
        'Базовый комплект батарей щита',
        'Модифицированный комплект батарей щита',
        'Продвинутый комплект батарей щита',
        'Улучшенный комплект батарей щита',
        'Элитный комплект батарей щита',
    ]

    EN_NAME_PER_MARK = [
        'Shield Batteries',
        'Modif. Shield Batteries',
        'Imp. Shield Batteries',
        'Adv. Shield Batteries',
        'Elite Shield Batteries',
    ]

    EN_DESC_NAME_PER_MARK = [
        'Basic Shield Batteries pack',
        'Modified Shield Batteries pack',
        'Improved Shield Batteries pack',
        'Advanced Shield Batteries pack',
        'Elite Shield Batteries pack',
    ]

    def get_icon(self):
        return r'equipment\models\icons\ge\ge_battery.3db'


class CloakingDevice(Equipment, DefaultGood):
    COMBINABLE = False
    WEAPON_CODE = CLOAK

    INFO1 = MS('Устройство, позволяющее вашему кораблю длительное время находиться в невидимости.',
               'With this device you can become invisible.')

    INFO2 = MS('Вы можете установить данное устройство только на точку монтирования Контрмеры.',
               'You can mount this device only on Countermeassure mount point.')

    INFO3 = MS('Для переключения режимов невидимости используйте ВТОРИЧНУЮ кнопку "МАГН.ЛУЧ (все). / Невидимость. '
               'Комбинация ОБЯЗАТЕЛЬНО должна включать кнопку Ctrl.',
               'To switch invisible modes use SECONDARY button "Tractor beam (ALL) / Invisibility". '
               'Combination MUST contain Ctrl button.')

    def __init__(self, ids, nickname, in_time, out_time, ru_name, ru_fullname, en_name, en_fullname,
                 ru_extra_descript, en_extra_descript, price):
        self.ids = ids

        self.nickname = nickname
        self.in_time = in_time
        self.out_time = out_time
        self.price = price

        self.ru_name = ru_name
        self.ru_fullname = ru_fullname
        self.en_name = en_name
        self.en_fullname = en_fullname
        self.ru_extra_descript = ru_extra_descript
        self.en_extra_descript = en_extra_descript

        self.ids_name = ids.new_name(
            MS(
                self.ru_name,
                self.en_name
            )
        )
        self.ids_info = ids.new_info(
            MS(
                InfocardBuilder.build_equip_infocard(
                    self.ru_fullname,
                    self.get_ru_description_content()
                ),
                InfocardBuilder.build_equip_infocard(
                    self.en_fullname,
                    self.get_en_description_content()
                )
            )
        )

    def get_price(self):
        return self.price

    def get_market_level(self):
        return -1  # ????

    def get_nickname(self):
        return self.nickname

    def get_rate(self):
        return self.get_civ_rate()

    def get_ru_description_content(self):
        content = []

        content.append(self.INFO1.get_ru())
        content.append(self.INFO2.get_ru())
        content.append(self.INFO3.get_ru())
        content.append(self.ru_extra_descript)

        return content

    def get_en_description_content(self):
        content = []

        content.append(self.INFO1.get_en())
        content.append(self.INFO2.get_en())
        content.append(self.INFO3.get_en())
        content.append(self.en_extra_descript)

        return content

    def get_ids_name(self):
        return self.ids_name.id

    def get_ids_info(self):
        return self.ids_info.id

    def get_icon(self):
        return r'equipment\models\icons\ge\ge_scanner01.3db'

    def get_equip(self):
        return f'''[CloakingDevice]
nickname = {self.get_nickname()}
ids_name = {self.get_ids_name()}
ids_info = {self.get_ids_info()}
hit_pts = 10000
DA_archetype = Equipment\\models\\hardware\\ge_cloak.3db
material_library = Equipment\\models\\hardware.mat
HP_child = HPMount
mass = 10
volume = 0
cloakin_time = {self.in_time}
cloakout_time = {self.out_time}
cloakin_fx = no_cloakeffect01
cloakout_fx = no_cloakeffect01
'''
