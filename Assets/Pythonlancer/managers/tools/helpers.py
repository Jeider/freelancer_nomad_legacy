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
    def extract_ammo_lootprops(*equipment):
        results = []
        for equip_group in equipment:
            for item in equip_group:
                results.append(item.get_ammo_lootprops())
        return DIVIDER.join(results)

    @staticmethod
    def extract_marketdata(*equipment):
        results = []
        for equip_group in equipment:
            for item in equip_group:
                results.append(item.get_marketdata())
        return SINGLE_DIVIDER.join(results)
