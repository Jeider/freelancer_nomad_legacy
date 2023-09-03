from text.dividers import SINGLE_DIVIDER, DIVIDER
from text.infocards import InfocardBuilder


class ManagerHelper(object):
    @staticmethod
    def extract_equips(*equipment):
        results = []
        for equip_group in equipment:
            for item in equip_group:
                results.append(item.get_equip())
        return DIVIDER.join(results)

    @staticmethod
    def extract_goods(*equipment):
        results = []
        for equip_group in equipment:
            for item in equip_group:
                results.append(item.get_good())
        return DIVIDER.join(results)

    @staticmethod
    def extract_lootprops(*equipment):
        results = []
        for equip_group in equipment:
            for item in equip_group:
                results.append(item.get_lootprops())
        return DIVIDER.join(results)

    @staticmethod
    def extract_ru_names(*equipment):
        results = {}
        for equip_group in equipment:
            for item in equip_group:
                results[item.ids_name] = item.get_ru_name()
        return results

    @staticmethod
    def extract_ru_infocards(*equipment):
        infocards = {}

        for equip_group in equipment:
            for item in equip_group:
                infocards[item.ids_info] = InfocardBuilder.build_equip_infocard(
                    item.get_ru_fullname(),
                    item.get_ru_description_content()
                )

        return infocards

    @staticmethod
    def extract_marketdata(*equipment):
        results = []
        for equip_group in equipment:
            for item in equip_group:
                results.append(item.get_marketdata())
        return SINGLE_DIVIDER.join(results)
