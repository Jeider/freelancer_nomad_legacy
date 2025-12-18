from text.translate import Lang_RU


class InfocardBuilder(object):

    @staticmethod
    def build_infocard(infocard_template, template_params=None, language=Lang_RU):
        if template_params is None:
            template_params = {}
        inline_template = ''.join(infocard_template)
        template_params.update(language.TRANSLATIONS)

        return inline_template.format(**template_params)

    @staticmethod
    def build_row(infocard_template, content, language=Lang_RU):
        inline_template = ''.join(infocard_template)
        template_params = {
            KEY_CONTENT: content
        }
        template_params.update(language.TRANSLATIONS)

        return inline_template.format(**template_params)

    @staticmethod
    def merge_rows(rows):
        return ''.join([INFO_ROW_BASIC_INLINE.format(content=row) for row in rows])

    @staticmethod
    def build_equip_infocard(equip_name, equip_raw_info):
        compiled_content = []
        for item_content in equip_raw_info:
            compiled_content.append(
                InfocardBuilder.build_row(INFO_ROW_BASIC, item_content)
            )

        template_params = {
            KEY_EQUIP_NAME: equip_name,
            KEY_EQUIP_DESCRIPTION: INFO_EXTRA_DIVIDER.join(compiled_content)
        }
        return InfocardBuilder.build_infocard(INFO_EQUIPMENT, template_params)


INFO_SHIP_ABOUT = [
    '<?xml version="1.0" encoding="UTF-16"?>',
    '<RDL>',
    '<PUSH/>',
    '<TEXT>TEST</TEXT>',
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

KEY_CONTENT = 'content'
KEY_EQUIP_NAME = 'equipment_fullname'
KEY_EQUIP_DESCRIPTION = 'equipment_description'

INFO_EQUIPMENT = [
    '<?xml version="1.0" encoding="UTF-16"?>',
    '<RDL>',
    '<PUSH/>',
    '<TRA data="1" mask="1" def="-2"/>',
    '<JUST loc="center"/>',
    '<TEXT>{equipment_fullname}</TEXT>',
    '<PARA/>',
    '<TRA data="0" mask="1" def="-1"/>',
    '<JUST loc="left"/>',
    '<TEXT> </TEXT>',
    '<PARA/>',
    '{equipment_description}'
    '<TEXT> </TEXT>',
    '<PARA/>',
    '<POP/>',
    '</RDL>',
]


INFO_ROW_BASIC = [
    '<TEXT>{content}</TEXT>',
    '<PARA/>',
]
INFO_ROW_BASIC_DOUBLE_DIVIDED = [
    '<TEXT>{content}</TEXT>',
    '<PARA/>',
    '<TEXT> </TEXT>',
    '<PARA/>',
]
INFO_ROW_BASIC_INLINE = ''.join(INFO_ROW_BASIC_DOUBLE_DIVIDED)

INFO_ROW_BOLD = [
    '<TRA data="1" mask="1" def="-2"/>',
    '<TEXT>{content}</TEXT>',
    '<PARA/>',
    '<TRA data="0" mask="1" def="-1"/>',
]

INFO_ROW_DANGER = [
    '<TRA data="65281" mask="-31" def="30"/>',
    '<TEXT>{content}</TEXT>',
    '<PARA/>',
    '<TRA data="96" mask="-31" def="-1"/>',
]

INFO_EXTRA_DIVIDER = '<TEXT> </TEXT><PARA/>'


INFO_BASIC = [
    '<?xml version="1.0" encoding="UTF-16"?>',
    '<RDL>',
    '<PUSH/>',
    '{content}'
    '<POP/>',
    '</RDL>',
]
