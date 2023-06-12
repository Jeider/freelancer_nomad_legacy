from files.writer import FileWriter

from core import LancerCore


def main():
    core = LancerCore()

    files_map = [
        ('equipment_nicknames.txt', core.misc_equip.get_ru_names()),

        ('engine_equip.ini', core.misc_equip.get_engine_equip()),
        ('engine_good.ini', core.misc_equip.get_engine_good()),
        ('power_equip.ini', core.misc_equip.get_powerplant_equip()),
        ('power_good.ini', core.misc_equip.get_powerplant_good()),
        ('st_equip.ini', core.misc_equip.get_st_equip()),
        ('st_good.ini', core.misc_equip.get_st_good()),

        ('equip_lootprops.ini', core.misc_equip.get_lootprops()),

        ('faction_prop_helper.ini', core.population.get_npc_names()),
        ('npcships.ini', core.population.get_npcships()),
        ('loadouts.ini', core.population.get_loadouts()),

        ('weapon_nicknames.txt', core.weapons.get_ru_names()),

        ('weapon_equip.ini', core.weapons.get_weapon_equip()),
        ('weapon_good.ini', core.weapons.get_weapon_good()),

        ('weapon_lootprops.ini', core.weapons.get_lootprops()),

    ]

    for file, content in files_map:
        FileWriter.write(file, content)


main()




# print(engine.get_good())
# print('')

