from files.writer import FileWriter

from core import LancerCore

DIVIDER = '\n\n'


def main():
    core = LancerCore()

    nicknames_data = [
        core.misc_equip.get_ru_names(),
        core.weapons.get_ru_names(),
        core.shiparch.get_ship_ru_names(),
    ]

    infocards_data = [
        core.misc_equip.get_ru_infocards(),
        core.weapons.get_ru_infocards(),
        core.shiparch.get_ship_ru_infocards(),
    ]

    lootprops_data = [
        core.misc_equip.get_lootprops(),
        core.weapons.get_lootprops() 
    ]

    markets_demo_data = [
        core.misc_equip.get_demo_marketdata(),
        core.weapons.get_demo_marketdata() 
    ]

    files_map = [
        ('audio_ingame.ini', core.audio.get_ingame_sounds_ini()),
        ('audio_ingame.xml', core.audio.get_ingame_sounds_xml()),

        ('audio_cutscenes.ini', core.audio.get_cutscene_sounds_ini()),
        ('audio_cutscenes.lua', core.audio.get_cutscene_sounds_thn()),

        ('engine_equip.ini', core.misc_equip.get_engine_equip()),
        ('engine_good.ini', core.misc_equip.get_engine_good()),
        ('power_equip.ini', core.misc_equip.get_powerplant_equip()),
        ('power_good.ini', core.misc_equip.get_powerplant_good()),
        ('st_equip.ini', core.misc_equip.get_st_equip()),
        ('st_good.ini', core.misc_equip.get_st_good()),
        ('select_equip.ini', core.misc_equip.get_select_equip()),

        ('faction_prop_helper.ini', core.population.get_npc_names()),
        ('npcships.ini', core.population.get_npcships()),
        ('loadouts.ini', core.population.get_loadouts()),

        ('weapon_equip.ini', core.weapons.get_weapon_equip()),
        ('weapon_good.ini', core.weapons.get_weapon_good()),

        ('nicknames_ru.ini', ''.join(nicknames_data)),
        ('infocards_ru.ini', ''.join(infocards_data)),
        ('lootprops.ini', DIVIDER.join(lootprops_data)),

        ('demo_marketdata.ini', DIVIDER.join(markets_demo_data)),
        ('market_equip.ini', core.universe.get_market_equip()),
        ('market_ships.ini', core.universe.get_market_ships()),

        ('ship_packages.ini', core.shiparch.get_ship_goods()),

        ('shiparch.ini', str(core.shiparch.get_shiparch_content())),
    ]

    for file, content in files_map:
        FileWriter.write(file, content)


main()
