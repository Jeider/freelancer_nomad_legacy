from tools.utf_xml import XML_UTF
from tools.data_folder import DataFolder
from tools import steos
import pathlib


STORY_FILES = [
    # 'echo_m01',
    # 'echo_m01_player',
    # 'echo_m02',
    # 'echo_m02_player',
    'echo_m03',
    'echo_m03_player',
    # 'echo_m04',
    # 'echo_m04_female',
    # 'echo_m04_player',
    # 'echo_m05',
    # 'echo_m05_female',
    # 'echo_m05_player',
    # 'echo_m06',
    # 'echo_m06_female',
    # 'echo_m06_player',
    # 'echo_m07',
    # 'echo_m07_female',
    # 'echo_m07_player',
    # 'echo_m08',
    # 'echo_m08_female',
    # 'echo_m08_player',
]
STORY_XML_TEMPLATE = '{file}.utf.xml'
STORY_UTF_TEMPLATE = '{file}.utf'

INITIAL_AUDIO_XML_FOLDER = 'AUDIO_XML_RU'

STORY_FOLDER_TEMPLATE = '../AUDIO_XML_RU_APPLY/{file}.xml'


class AudioFolder:

    @staticmethod
    def get_initial_audio_path():
        current_path = pathlib.Path().resolve()
        return current_path.parent / INITIAL_AUDIO_XML_FOLDER

    @classmethod
    def compile_xml_to_utf(cls):
        for file in STORY_FILES:
            XML_UTF.run_command(
                STORY_XML_TEMPLATE.format(file=file),
                STORY_FOLDER_TEMPLATE.format(file=file),
            )
            out_file_name = STORY_UTF_TEMPLATE.format(file=file)
            new_xml = XML_UTF.get_out_path() / out_file_name

            DataFolder.move_story_audio(
                new_xml,
                out_file_name,
            )

    @classmethod
    def compile_voice_to_xml(cls, voice, skip=True):
        voice.validate_ai_compatibility()

        root_path = cls.get_initial_audio_path()
        voice_path = root_path / f'{voice.voice_name}.xml'
        voice_path.mkdir(parents=True, exist_ok=True)

        sounds_path = voice_path / voice.voice_name
        sounds_path.mkdir(parents=True, exist_ok=True)

        xml_path = voice_path / f'{voice.voice_name}.utf.xml'
        if xml_path.exists():
            if not skip:
                raise Exception(f'Voice {voice.voice_name} is already exist. Remove it if you want to create it again')
            return

        xml_path.write_text(voice.get_xml(), encoding='utf-8')

        for sound in voice.sounds:
            steos.SteosVoice.generate_ru_voice(voice_root=sounds_path, sound=sound)
