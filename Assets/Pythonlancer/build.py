import sys
from files.writer import FileWriter

from core import LancerCore

from templates.hardcoded_inis.missions import LootpropsTemplate

from tools.data_folder import DataFolder

from text.dividers import DIVIDER

GENERATED = 'GENERATED'


class DifficultySettings:
    M9_SPAWN_DESTROYER_C = True
    M9_DESTROYER_B_DELAY = 60
    M9_DESTROYER_C_DELAY = 120
    M9_DESTROYER_D_DELAY = 150
    M9_DESTROYER_E_DELAY = 200
    M9_DESTROYER_F_DELAY = 300


class EasyDifficulty(DifficultySettings):
    pass


class NormalDifficulty(DifficultySettings):
    M9_SPAWN_WAVE_C = False
    M9_DESTROYER_B_DELAY = 80
    M9_DESTROYER_C_DELAY = 150  # Not spawn C wave
    M9_DESTROYER_D_DELAY = 150
    M9_DESTROYER_E_DELAY = 220
    M9_DESTROYER_F_DELAY = 300


class HardDifficulty(DifficultySettings):
    pass


class ExtremeDifficulty(DifficultySettings):
    pass



class BuildProp:

    def __init__(self, folder, russian: bool, difficulty: type[DifficultySettings]):
        self.folder = folder
        self.russian = russian
        self.difficulty = difficulty


BUILD_PROPS = [
    BuildProp('RU_NORMAL', russian=True, difficulty=NormalDifficulty),
    BuildProp('EN_NORMAL', russian=False, difficulty=NormalDifficulty),
]

PROPS_DB = {b.folder: b for b in BUILD_PROPS}
DEFAULT_RU = BuildProp(folder=None, russian=True, difficulty=NormalDifficulty)
DEFAULT_EN = BuildProp(folder=None, russian=False, difficulty=NormalDifficulty)



def build(build_props: BuildProp):
    core = LancerCore(write=True, russian=build_props.russian, build_folder=build_props.folder,
                      difficulty=build_props.difficulty)

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
    ]
    for file, content in files_map:
        FileWriter.write(file, content)

    for db in core.ids.get_databases():
        FileWriter.write_to_subfolder('ru', db.get_file_name(), db.compile_ru())
        FileWriter.write_to_subfolder('en', db.get_file_name(), db.compile_en())

    data_folder = DataFolder()

    data_folder.sync_equip('weapon_equip', GENERATED, core.weapons.get_weapon_equip())
    data_folder.sync_equip('weapon_good', GENERATED, core.weapons.get_weapon_good())

    data_folder.sync_equip('key_equip', GENERATED, core.universe.get_key_equip())
    data_folder.sync_equip('key_good', GENERATED, core.universe.get_key_good())

    data_folder.sync_equip('engine_equip', GENERATED, core.misc_equip.get_engine_equip())
    data_folder.sync_equip('engine_good', GENERATED, core.misc_equip.get_engine_good())

    data_folder.sync_equip('power_equip', GENERATED, core.misc_equip.get_powerplant_equip())
    data_folder.sync_equip('power_good', GENERATED, core.misc_equip.get_powerplant_good())

    data_folder.sync_equip('st_equip', GENERATED, core.misc_equip.get_st_equip())
    data_folder.sync_equip('st_good', GENERATED, core.misc_equip.get_st_good())

    data_folder.sync_equip('comm_equip', GENERATED, core.store.get_comm_equip())
    data_folder.sync_equip('comm_good', GENERATED, core.store.get_comm_good())

    data_folder.sync_equip('select_equip', GENERATED, core.npc_armor.get_select_equip())

    data_folder.sync_equip('ship_packages', GENERATED, core.shiparch.get_ship_goods())

    data_folder.sync_equip('market_misc', GENERATED, core.universe.get_market_equip())
    data_folder.sync_equip('market_ships', GENERATED, core.universe.get_market_ships())
    data_folder.sync_equip('market_commodities', GENERATED, core.universe.get_market_commodities())

    data_folder.sync_lootprops(
        LootpropsTemplate().format({'generated': DIVIDER.join(lootprops_data)})
    )


def build_all():
    for build_prop in BUILD_PROPS:
        build(build_prop)


def main():
    try:
        if sys.argv[1] == 'all':
            print('build all packages')
            build_all()
        elif sys.argv[1] == 'ru':
            print('build ru direct')
            build(DEFAULT_RU)
        elif sys.argv[1] == 'en':
            print('build en direct')
            build(DEFAULT_EN)
        else:
            print(f'build {sys.argv[1]}')
            build(
                PROPS_DB[sys.argv[1]]
            )

    except IndexError:
        print('build type not found')


main()
