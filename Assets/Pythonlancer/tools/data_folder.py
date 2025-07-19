import pathlib
import shutil
from pydub import AudioSegment

LOADOUTS_GEN = 'loadout_gen.ini'



def get_duration_pydub(file_path):
    audio_file = AudioSegment.from_file(file_path)
    duration = audio_file.duration_seconds
    return duration


class DataFolder(object):

    @staticmethod
    def get_root():
        current_path = pathlib.Path().resolve()
        return current_path.parent.parent / 'DATA'

    @classmethod
    def get_audio(cls):
        return cls.get_root() / 'AUDIO'

    @classmethod
    def get_equip(cls):
        return cls.get_root() / 'EQUIPMENT'

    @classmethod
    def get_solar(cls):
        return cls.get_root() / 'SOLAR'

    @classmethod
    def get_universe(cls):
        return cls.get_root() / 'UNIVERSE'

    @classmethod
    def get_missions(cls):
        return cls.get_root() / 'MISSIONS'

    @classmethod
    def get_ships(cls):
        return cls.get_root() / 'SHIPS'

    @classmethod
    def get_interface(cls):
        return cls.get_root() / 'INTERFACE'

    @classmethod
    def get_fx(cls):
        return cls.get_root() / 'FX'

    @classmethod
    def get_scripts(cls):
        return cls.get_root() / 'SCRIPTS'

    @classmethod
    def get_cutscene_audio(cls):
        return cls.get_audio() / 'MOD'

    @classmethod
    def sync_fuse(cls, fuse_name, content):
        loadouts_file = cls.get_fx() / f'{fuse_name}.ini'
        loadouts_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_solar_gen_loadouts(cls, content):
        loadouts_file = cls.get_solar() / LOADOUTS_GEN
        loadouts_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_to_test_workspace(cls, content, workspace_index=''):
        system_file = cls.get_universe() / 'GENERATION_DATA' / 'WORKSPACE' / f'test{workspace_index}.ini'
        system_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_system(cls, system_name, system_root, system_folder, content):
        system_file = cls.get_universe() / system_root / system_folder / f'{system_name}.ini'
        system_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_asteroid_definition(cls, definition_name, subfolder, content):
        asteroid_file = cls.get_solar() / 'ASTEROIDS_MOD' / subfolder / f'{definition_name}.ini'
        asteroid_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_templated_nebula(cls, nebula_file_name, subfolder, content):
        nebula_file = cls.get_solar() / 'NEBULA_MOD' / subfolder / f'{nebula_file_name}.ini'
        nebula_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_interior(cls, interior_file_name, content):
        asteroid_file = cls.get_universe() / 'GENERATED_INTERIORS' / f'{interior_file_name}.ini'
        asteroid_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_equip_root(cls, equip_file_name, content):
        equip_file = cls.get_equip() / f'{equip_file_name}.ini'
        equip_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_equip(cls, equip_file_name, subfolder, content):
        equip_file = cls.get_equip() / subfolder / f'{equip_file_name}.ini'
        equip_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_equip_hardcoded(cls, equip_file_name, content):
        equip_file = cls.get_equip()  / f'{equip_file_name}.ini'
        equip_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_knowledge_map(cls, content):
        equip_file = cls.get_interface() / 'knowledgemap.ini'
        equip_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_infocard_map(cls, content):
        equip_file = cls.get_interface() / 'infocardmap.ini'
        equip_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_universe(cls, content):
        equip_file = cls.get_universe() / 'universe.ini'
        equip_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_mbases(cls, content):
        equip_file = cls.get_missions() / 'mbases.ini'
        equip_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_npcships(cls, content):
        equip_file = cls.get_missions() / 'npcships.ini'
        equip_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_lootprops(cls, content):
        equip_file = cls.get_missions() / 'lootprops.ini'
        equip_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_shiparch(cls, content):
        equip_file = cls.get_ships() / 'shiparch.ini'
        equip_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_ships_loadouts(cls, content):
        equip_file = cls.get_ships() / 'loadout_gen.ini'
        equip_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_story_ships_loadouts(cls, content):
        equip_file = cls.get_ships() / 'loadout_gen_story.ini'
        equip_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_dock_key(cls, content):
        equip_file = cls.get_root() / 'dock_key.ini'
        equip_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_story_mission(cls, folder, file, content):
        equip_file = cls.get_missions() / folder / f'{file}.ini'
        equip_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_story_npcships(cls, folder, content):
        equip_file = cls.get_missions() / folder / f'npcships.ini'
        equip_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_story_ingame_thorn(cls, file, content):
        equip_file = cls.get_missions() / 'GENERATED_THORN' / f'{file}.thn'
        equip_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_audio_ini(cls, file, content):
        equip_file = cls.get_audio() / f'{file}.ini'
        equip_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_mission_voice_props(cls, content):
        equip_file = cls.get_missions() / 'voice_properties.ini'
        equip_file.write_text(content, encoding='utf-8')

    @classmethod
    def move_story_audio(cls, original_file_destination, out_file_name):
        shutil.move(
            original_file_destination,
            cls.get_audio() / out_file_name
        )

    @classmethod
    def sync_facial(cls, content):
        facial_file = cls.get_scripts() / 'WORKSPACE' / 'facial.thn'
        facial_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_scene(cls, scene_name, content):
        facial_file = cls.get_scripts() / 'GENERATED' / f'{scene_name}.thn'
        facial_file.write_text(content, encoding='utf-8')

    @classmethod
    def get_facial(cls):
        facial_file = open(cls.get_scripts() / 'WORKSPACE' / 'facial.thn')
        file_content = facial_file.readlines()
        facial_file.close()
        return file_content

    @classmethod
    def watch_cutscene_audio_duration(cls, subfolder, file_path):
        duration = get_duration_pydub(cls.get_cutscene_audio() / subfolder / file_path)
        return duration
