from files.writer import FileWriter

from core import LancerCore

from templates.hardcoded_inis.missions import LootpropsTemplate

from tools.data_folder import DataFolder

DIVIDER = '\n\n'

ENABLE_STORY = False

GENERATED = 'GENERATED'


def main():
    core = LancerCore(enable_story=ENABLE_STORY, write=True)

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
        ('faction_prop_helper.ini', core.population.get_npc_names()),

        ('nicknames_ru.ini', ''.join(nicknames_data)),
        ('infocards_ru.ini', ''.join(infocards_data)),

        ('demo_marketdata.ini', DIVIDER.join(markets_demo_data)),
        ('key_for_story.ini', core.universe.get_key_story()),
        ('key_for_initial_world.ini', core.universe.get_key_initial_world()),
    ]

    if core.has_story:
        # Should be obsolete
        story_files = [
            ('audio_ingame.ini', core.audio.get_ingame_sounds_ini()),
            ('audio_ingame.xml', core.audio.get_ingame_sounds_xml()),

            ('audio_space_subtitle.xml', core.audio.get_space_subtitles_xml()),

            ('audio_cutscenes.ini', core.audio.get_cutscene_sounds_ini()),
            ('audio_cutscenes.lua', core.audio.get_cutscene_sounds_thn()),

            ('audio_ether_comm_strings.ini', core.audio.get_ether_comm_ru_strings()),
            ('audio_ether_comm_text.ini', core.audio.get_ether_comm_mission_texts()),

            ('misc_ru_strings.ini', core.audio.get_misc_ru_strings()),
            ('misc_ru_infocards.ini', core.audio.get_misc_ru_infocards()),
        ]
        files_map.extend(story_files)

    for file, content in files_map:
        FileWriter.write(file, content)

    DataFolder.sync_equip('weapon_equip', GENERATED, core.weapons.get_weapon_equip())
    DataFolder.sync_equip('weapon_good', GENERATED, core.weapons.get_weapon_good())

    DataFolder.sync_equip('key_equip', GENERATED, core.universe.get_key_equip())
    DataFolder.sync_equip('key_good', GENERATED, core.universe.get_key_good())

    DataFolder.sync_equip('engine_equip', GENERATED, core.misc_equip.get_engine_equip())
    DataFolder.sync_equip('engine_good', GENERATED, core.misc_equip.get_engine_good())

    DataFolder.sync_equip('power_equip', GENERATED, core.misc_equip.get_powerplant_equip())
    DataFolder.sync_equip('power_good', GENERATED, core.misc_equip.get_powerplant_good())

    DataFolder.sync_equip('st_equip', GENERATED, core.misc_equip.get_st_equip())
    DataFolder.sync_equip('st_good', GENERATED, core.misc_equip.get_st_good())

    DataFolder.sync_equip('select_equip', GENERATED, core.misc_equip.get_select_equip())

    DataFolder.sync_equip('ship_packages', GENERATED, core.shiparch.get_ship_goods())

    DataFolder.sync_equip('market_misc', GENERATED, core.universe.get_market_equip())
    DataFolder.sync_equip('market_ships', GENERATED, core.universe.get_market_ships())

    DataFolder.sync_lootprops(
        LootpropsTemplate().format({'generated': DIVIDER.join(lootprops_data)})
    )


main()
