from text.translate import Lang_RU


class InfocardBuilder(object):

    @staticmethod
    def build_infocard(infocard_template, template_params):
        inline_template = ''.join(infocard_template)
        template_params.update(Lang_RU.TRANSLATIONS)

        return inline_template.format(**template_params)


INFO_SHIP_ABOUT = [
    '<?xml version="1.0" encoding="UTF-16"?>',
    '<RDL>',
    '<PUSH/>',
    '<TEXT>ТЕСТ</TEXT>',
    '<PARA/>',
    '<PARA/>',
    '<POP/>',
    '</RDL>',
]


INFO_SHIP_TABLE = [
    '<?xml version="1.0" encoding="UTF-16"?>',
    '<RDL>',
    '<PUSH/>',
    '<TEXT> </TEXT>',
    '<PARA/>',
    '<TRA data="1" mask="1" def="-2"/>',
    '<JUST loc="center"/>',
    '<TEXT>{text_stats}</TEXT>',
    '<PARA/>',
    '<TRA data="0" mask="1" def="-1"/>',
    '<JUST loc="left"/>',
    '<TEXT></TEXT>',
    '<PARA/>',
    '<TEXT>{text_gun_count}: {value_gun_count}</TEXT>',
    '<PARA/>',
    '<TEXT>{text_armor}: {value_armor}</TEXT>',
    '<PARA/>',
    '<TEXT>{text_mass}: {value_mass}</TEXT>',
    '<PARA/>',
    '<TEXT>{text_cargo}: {value_cargo}</TEXT>',
    '<PARA/>',
    '<TEXT>{text_bot_bats}: {value_bot_bats}</TEXT>',
    '<PARA/>',
    '<TEXT>{text_max_equip_class} : {value_max_equip_class}</TEXT>',
    '<PARA/>',
    '<TEXT>{text_max_weapon_class}: {value_max_weapon_class}</TEXT>',
    '<PARA/>',
    '<TEXT>{text_additional_equipment}: {value_additional_equipment}</TEXT>',
    '<PARA/>',
    '<PARA/>',
    '<POP/>',
    '</RDL>',
]

INFO_SHIP_KEYS = [
    '<?xml version="1.0" encoding="UTF-16"?>',
    '<RDL>',
    '<PUSH/>',
    '<TRA data="1" mask="1" def="-2"/>',
    '<TEXT>{text_stats}</TEXT>',
    '<PARA/>',
    '<TRA data="0" mask="1" def="-1"/>',
    '<TEXT> </TEXT>',
    '<PARA/>',
    '<TEXT>{text_gun_count}:</TEXT>',
    '<PARA/>',
    '<TEXT>{text_armor}:</TEXT>',
    '<PARA/>',
    '<TEXT>{text_mass}:</TEXT>',
    '<PARA/>',
    '<TEXT>{text_cargo}:</TEXT>',
    '<PARA/>',
    '<TEXT>{text_bot_bats}:</TEXT>',
    '<PARA/>',
    '<TEXT>{text_max_equip_class}:</TEXT>',
    '<PARA/>',
    '<TEXT>{text_max_weapon_class}:</TEXT>',
    '<PARA/>',
    '<TEXT>{text_additional_equipment}: </TEXT>',
    '<PARA/>',
    '<POP/>',
    '</RDL>',
]

INFO_SHIP_VALUES = [
    '<?xml version="1.0" encoding="UTF-16"?>',
    '<RDL>',
    '<PUSH/>',
    '<TEXT> </TEXT>',
    '<PARA/>',
    '<TEXT> </TEXT>',
    '<PARA/>',
    '<TEXT>{value_gun_count}</TEXT>',
    '<PARA/>',
    '<TEXT>{value_armor}</TEXT>',
    '<PARA/>',
    '<TEXT>{value_mass}</TEXT>',
    '<PARA/>',
    '<TEXT>{value_cargo}</TEXT>',
    '<PARA/>',
    '<TEXT>{value_bot_bats}</TEXT>',
    '<PARA/>',
    '<TEXT>{value_max_equip_class}</TEXT>',
    '<PARA/>',
    '<TEXT>{value_max_weapon_class}</TEXT>',
    '<PARA/>',
    '<TEXT>{value_additional_equipment}</TEXT>',
    '<PARA/>',
    '<POP/>',
    '</RDL>',
]
