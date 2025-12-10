import pathlib
import shutil
import json

LOADOUTS_GEN = 'loadout_gen.ini'



def get_and_create(folder):
    if not folder.exists():
        folder.mkdir()
    return folder


class DataFolder:

    def __init__(self, build_to_folder=None):
        self.root = pathlib.Path().resolve().parent.parent
        self.build_to_folder = build_to_folder
        if self.build_to_folder:
            self.root = self.root / 'BUILDS' / self.build_to_folder

    def get_root(self):
        return self.root

    def get_static(self):
        return get_and_create(self.get_root() / 'STATIC')

    def get_data(self):
        return get_and_create(self.get_root() / 'DATA')

    def get_exe(self):
        return get_and_create(self.get_root() / 'EXE')

    def get_save(self):
        return get_and_create(self.get_root() / 'SAVE')

    def get_d3d8(self):
        return self.get_exe() / 'd3d8.dll'

    def get_base_dxwrapper(self):
        return self.get_static() / 'd3d8_dxwrapper.dll'

    def get_autosave(self):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        return self.get_root() / 'SAVE' / 'Accts' / 'SinglePlayer' / 'AutoSave.fl'

    def get_crashes_root(self):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        folder = self.get_save() / 'CrashData'
        if not folder.exists():
            folder.mkdir()
        return folder

    def get_audio(self):
        return get_and_create(self.get_data() / 'AUDIO')

    def get_equip(self):
        return get_and_create(self.get_data() / 'EQUIPMENT')

    def get_solar(self):
        return get_and_create(self.get_data() / 'SOLAR')

    def get_universe(self):
        return get_and_create(self.get_data() / 'UNIVERSE')

    def get_missions(self):
        return get_and_create(self.get_data() / 'MISSIONS')

    def get_random_missions(self):
        return get_and_create(self.get_data() / 'RANDOMMISSIONS')

    def get_ships(self):
        return get_and_create(self.get_data() / 'SHIPS')

    def get_interface(self):
        return get_and_create(self.get_data() / 'INTERFACE')

    def get_fx(self):
        return get_and_create(self.get_data() / 'FX')

    def get_fonts(self):
        return get_and_create(self.get_data() / 'FONTS')

    def get_scripts(self):
        return get_and_create(self.get_data() / 'SCRIPTS')

    def get_player(self):
        return get_and_create(self.get_data() / 'PLAYER')

    def get_characters(self):
        return get_and_create(self.get_data() / 'CHARACTERS')

    def get_cutscene_audio_ru(self):
        if self.build_to_folder:
            return

        return get_and_create(self.get_audio() / 'MOD')

    def get_cutscene_audio_en(self):
        if self.build_to_folder:
            return

        return get_and_create(self.get_audio() / 'MOD_ENG')

    def sync_fuse(self, fuse_name, content):
        loadouts_file = self.get_fx() / f'{fuse_name}.ini'
        loadouts_file.write_text(content, encoding='utf-8')

    def sync_effects(self, content):
        if self.build_to_folder:
            return

        equip_file = self.get_fx() / 'effects_gen.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_vis_effects(self, content):
        if self.build_to_folder:
            return

        equip_file = get_and_create(self.get_fx() / 'GENERATED') / 'gen_ale.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_solar_gen_loadouts(self, content):
        loadouts_file = self.get_solar() / LOADOUTS_GEN
        loadouts_file.write_text(content, encoding='utf-8')

    def sync_to_test_workspace(self, content, workspace_index=''):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        system_file = self.get_universe() / 'GENERATION_DATA' / 'WORKSPACE' / f'test{workspace_index}.ini'
        system_file.write_text(content, encoding='utf-8')

    def sync_system(self, system_name, system_root, system_folder, content):
        system_file = get_and_create(get_and_create(self.get_universe() / system_root) / system_folder) / f'{system_name}.ini'
        system_file.write_text(content, encoding='utf-8')

    def sync_asteroid_definition(self, definition_name, subfolder, content):
        if self.build_to_folder:
            return

        asteroid_file = self.get_solar() / 'ASTEROIDS_MOD' / subfolder / f'{definition_name}.ini'
        asteroid_file.write_text(content, encoding='utf-8')

    def sync_templated_nebula(self, nebula_file_name, subfolder, content):
        if self.build_to_folder:
            return

        nebula_file = self.get_solar() / 'NEBULA_MOD' / subfolder / f'{nebula_file_name}.ini'
        nebula_file.write_text(content, encoding='utf-8')

    def sync_interior(self, interior_file_name, content):
        if self.build_to_folder:
            return

        asteroid_file = self.get_universe() / 'GENERATED_INTERIORS' / f'{interior_file_name}.ini'
        asteroid_file.write_text(content, encoding='utf-8')

    def sync_equip_root(self, equip_file_name, content):
        equip_file = self.get_equip() / f'{equip_file_name}.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_equip(self, equip_file_name, subfolder, content):
        equip_file = get_and_create(self.get_equip() / subfolder) / f'{equip_file_name}.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_equip_hardcoded(self, equip_file_name, content):
        equip_file = self.get_equip()  / f'{equip_file_name}.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_knowledge_map(self, content):
        equip_file = self.get_interface() / 'knowledgemap.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_infocard_map(self, content):
        equip_file = self.get_interface() / 'infocardmap.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_universe(self, content):
        equip_file = self.get_universe() / 'universe.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_initial_world(self, content):
        equip_file = self.get_data() / 'initialworld.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_new_player(self, content):
        equip_file = self.get_exe() / 'newplayer.fl'
        equip_file.write_text(content, encoding='utf-8')

    def sync_empathy(self, content):
        equip_file = self.get_missions() / 'empathy.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_dacom(self, content):
        equip_file = self.get_exe() / 'dacom.ini'
        equip_file.write_text(content, encoding='utf-8')

    def get_perf_options(self):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        perf_file = self.get_save() / 'PerfOptions.ini'
        if perf_file.exists():
            opened_file = open(perf_file)
            file_content = opened_file.readlines()
            opened_file.close()
            return file_content
        return ''

    def get_startup_settings(self):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        data_file = self.get_save() / 'startup_settings.json'
        data = {}
        if data_file.exists():
            with open(data_file) as db_file:
                data = json.load(db_file)
        return data

    def save_startup_settings(self, settings):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        with open(self.get_save() / 'startup_settings.json', 'w') as data_file:
            json.dump(settings, data_file)

    def sync_perf_options(self, content):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        equip_file = self.get_save() / 'PerfOptions.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_hud_shift(self, content):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        equip_file = self.get_interface() / 'HudShift.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_cameras(self, content):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        equip_file = self.get_data() / 'cameras.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_front_light(self, content):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        equip_file = self.get_player() / 'front_light.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_contrail(self, content):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        equip_file = self.get_player() / 'contrail.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_player_bodyparts(self, content):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        equip_file = self.get_characters() / 'bodyparts_player.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_fonts(self, content):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        equip_file = self.get_fonts() / 'fonts.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_vignettes(self, content):
        equip_file = self.get_random_missions() / 'VignetteParams.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_mbases(self, content):
        equip_file = self.get_missions() / 'mbases.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_npcships(self, content):
        equip_file = self.get_missions() / 'npcships.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_faction_prop(self, content):
        equip_file = self.get_missions() / 'faction_prop.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_lootprops(self, content):
        equip_file = self.get_missions() / 'lootprops.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_shiparch(self, content):
        equip_file = self.get_ships() / 'shiparch.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_ships_loadouts(self, content):
        equip_file = self.get_ships() / 'loadout_gen.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_msn_ships_loadouts(self, content):
        equip_file = self.get_ships() / 'loadout_msn.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_story_ships_loadouts(self, content):
        equip_file = self.get_ships() / 'loadout_gen_story.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_dock_key(self, content):
        if self.build_to_folder:
            return

        equip_file = self.get_data() / 'dock_key.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_story_mission(self, folder, file, content):
        equip_file = get_and_create(self.get_missions() / folder) / f'{file}.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_story_npcships(self, folder, content):
        equip_file = get_and_create(self.get_missions() / folder) / f'npcships.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_story_ingame_thorn(self, file, content):
        if self.build_to_folder:
            return

        equip_file = self.get_missions() / 'GENERATED_THORN' / f'{file}.thn'
        equip_file.write_text(content, encoding='utf-8')

    def sync_audio_ini(self, file, content):
        if self.build_to_folder:
            return

        equip_file = self.get_audio() / f'{file}.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_mission_voice_props(self, content):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        equip_file = self.get_missions() / 'voice_properties.ini'
        equip_file.write_text(content, encoding='utf-8')

    def move_story_audio(self, original_file_destination, out_file_name):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        shutil.move(
            original_file_destination,
            self.get_audio() / out_file_name
        )

    def sync_facial(self, content):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        facial_file = self.get_scripts() / 'WORKSPACE' / 'facial.thn'
        facial_file.write_text(content, encoding='utf-8')

    def sync_scene(self, scene_name, content):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        facial_file = self.get_scripts() / 'GENERATED' / f'{scene_name}.thn'
        facial_file.write_text(content, encoding='utf-8')

    def get_facial(self):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        facial_file = open(self.get_scripts() / 'WORKSPACE' / 'facial.thn')
        file_content = facial_file.readlines()
        facial_file.close()
        return file_content

    def place_dxwrapper(self):
        self.remove_all_d3d8_wrappers()

        shutil.copy(
            self.get_base_dxwrapper(),
            self.get_d3d8()
        )

    def remove_all_d3d8_wrappers(self):
        d3d8 = self.get_d3d8()
        if d3d8.exists():
            self.get_d3d8().unlink()

    def remove_redundant_files(self):
        nnvoice = self.get_audio() / 'nnvoice.utf'
        trent_voice = self.get_audio() / 'trent_voice.utf'
        if nnvoice.exists():
            nnvoice.unlink()
        if trent_voice.exists():
            trent_voice.unlink()
