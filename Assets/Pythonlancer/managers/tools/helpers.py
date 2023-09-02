from text.dividers import DIVIDER


def extract_equips(*equipment):
    results = []
    for equip_group in equipment:
        for item in equip_group:
            results.append(item.get_equip())
    return DIVIDER.join(results)


def extract_goods(*equipment):
    results = []
    for equip_group in equipment:
        for item in equip_group:
            results.append(item.get_good())
    return DIVIDER.join(results)


def extract_lootprops(*equipment):
    results = []
    for equip_group in equipment:
        for item in equip_group:
            results.append(item.get_lootprops())
    return DIVIDER.join(results)
