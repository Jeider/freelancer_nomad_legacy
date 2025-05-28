from files.writer import FileWriter

from core import LancerCore

from templates.hardcoded_inis.missions import LootpropsTemplate

from tools.data_folder import DataFolder

DIVIDER = '\n\n'

GENERATED = 'GENERATED'


def main():
    core = LancerCore(write=True)

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

        ('debug_store.ini', ''.join(core.universe.get_bases_store_debug_info())),

        ('demo_marketdata.ini', DIVIDER.join(markets_demo_data)),
        ('key_for_story.ini', core.universe.get_key_story()),
        ('key_for_initial_world.ini', core.universe.get_key_initial_world()),
    ]

    for db in core.ids.get_databases():
        files_map.append(
            (db.get_file_name(), db.compile())
        )

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

    DataFolder.sync_equip('comm_equip', GENERATED, core.store.get_comm_equip())
    DataFolder.sync_equip('comm_good', GENERATED, core.store.get_comm_good())

    DataFolder.sync_equip('select_equip', GENERATED, core.misc_equip.get_select_equip())

    DataFolder.sync_equip('ship_packages', GENERATED, core.shiparch.get_ship_goods())

    DataFolder.sync_equip('market_misc', GENERATED, core.universe.get_market_equip())
    DataFolder.sync_equip('market_ships', GENERATED, core.universe.get_market_ships())
    DataFolder.sync_equip('market_commodities', GENERATED, core.universe.get_market_commodities())

    DataFolder.sync_lootprops(
        LootpropsTemplate().format({'generated': DIVIDER.join(lootprops_data)})
    )


main()
