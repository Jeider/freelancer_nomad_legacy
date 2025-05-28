from tools.utf_xml import XML_UTF
from tools.data_folder import DataFolder
from tools import steos
import pathlib


XML_FOLDERS = [
    'echo_m01',
    'echo_m01_player',
    # 'echo_m02',
    # 'echo_m02_player',
    # 'echo_m03',
    # 'echo_m03_player',
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
    # 'echo_m09',
    # 'echo_m09_female',
    # 'echo_m09_player',
    # 'echo_m10',
    # 'echo_m10_female',
    # 'echo_m10_player',
    # 'echo_m11',
    # 'echo_m11_female',
    # 'echo_m11_player',
    # 'echo_m12',
    # 'echo_m12_female',
    # 'echo_m12_player',
    # 'echo_m13',
    # 'echo_m13_female',
    # 'echo_m13_player',
    # "pilot01",
    # "pilot05",
    # "pilot06",
    # "pilot07",
    # "pilot08",
    # "pilot08",
    # "pilot08",
    # "pilot08",
    # "pilot08",
    # "mc_leg_m01",
    # "dispatcher01",
    # "dispatcher02",
    # "dispatcher03",
    "nnvoice",
]
STORY_XML_TEMPLATE = '{file}.utf.xml'
STORY_UTF_TEMPLATE = '{file}.utf'

INITIAL_AUDIO_XML_FOLDER = 'AUDIO_XML_RU'
APPLY_AUDIO_XML_FOLDER = 'AUDIO_XML_RU_APPLY'

STORY_FOLDER_TEMPLATE = '../AUDIO_XML_RU_APPLY/{file}.xml'


class AudioFolder:

    @staticmethod
    def get_initial_audio_path():
        current_path = pathlib.Path().resolve()
        return current_path.parent / INITIAL_AUDIO_XML_FOLDER

    @staticmethod
    def get_apply_audio_path():
        current_path = pathlib.Path().resolve()
        return current_path.parent / APPLY_AUDIO_XML_FOLDER

    @classmethod
    def compile_xml_to_utf(cls):
        for file in XML_FOLDERS:
            cls.compile_file(file)

    @classmethod
    def compile_file(cls, file):
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
    def compile_story_voice_to_xml(cls, voice, skip=True):
        # voice.validate_ai_compatibility()

        root_path = cls.get_initial_audio_path()
        voice_path = root_path / f'{voice.voice_name}.xml'
        voice_path.mkdir(parents=True, exist_ok=True)

        sounds_path = voice_path / voice.voice_name
        sounds_path.mkdir(parents=True, exist_ok=True)

        xml_path = voice_path / f'{voice.voice_name}.utf.xml'
        if xml_path.exists():
            if not skip:
                raise Exception(f'Voice {voice.voice_name} is already exist. Remove it if you want to create it again')

        xml_path.write_text(voice.get_xml(), encoding='utf-8')

        for sound in voice.sounds:
            file_destination = sounds_path / f"{sound.name}.mp3"
            alt_file_destination = sounds_path / f"{sound.name}.wav"
            if file_destination.exists() or alt_file_destination.exists():
                continue

            if sound.line.actor.STEOS_ID is None:
                raise Exception('actor %s have no steos for line name %s' % (sound.line.actor.NAME, sound.name))

            steos.SteosVoice.generate_ru_voice(file_destination=file_destination, sound=sound)
