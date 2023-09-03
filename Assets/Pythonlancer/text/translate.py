class Language(object):
    pass


class Lang_RU(Language):
    TRANSLATIONS = {
        # SHIPS
        'text_stats': 'Характеристики',
        'text_gun_count': 'Число пушек',
        'text_armor': 'Броня',
        'text_mass': 'Масса',
        'text_cargo': 'Объем трюма',
        'text_bot_bats': 'Число батарей/наноботов',
        'text_max_equip_class': 'Макс.класс оборудования',
        'text_max_weapon_class': 'Макс.класс пушек',
        'text_additional_equipment': 'Дополнительное оборудование',
    }


class Lang_EN(Language):
    TRANSLATIONS = {
        'text_stats': 'Stats',
        'text_gun_count': 'Gun Mounts',
        'text_armor': 'Armor',
        'text_mass': 'Mass',
        'text_cargo': 'Cargo Space',
        'text_bot_bats': 'Max Batteries/NanoBots',
        'text_max_equip_class': 'Max Equipment Class',
        'text_max_weapon_class': 'Max Gun Class',
        'text_additional_equipment': 'Additional Equipment',
    }
