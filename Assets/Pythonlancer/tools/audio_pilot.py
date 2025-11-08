from tools.utf_xml import XML_UTF
from tools.data_folder import DataFolder
from tools.steos import SteosVoice
from tools.audio_folder import AudioFolder
from tools.create_id import CreateId
import pathlib
import shutil
import os
from time import sleep

from universe.audio.parse_rule import SUBFOLDERS
from universe.audio.base_pilot import PilotVoice

PILOTS_FOLDER = 'PILOTS'
RAW_FOLDER = 'RAW'


class TempPilot:

    @staticmethod
    def get_root_pilot_path():
        current_path = pathlib.Path().resolve()
        return current_path.parent / PILOTS_FOLDER

    @classmethod
    def prepare_temp_folders(cls, pilot: PilotVoice):
        pilot_folder = cls.get_root_pilot_path() / pilot.FOLDER

        pilot_folder.mkdir(exist_ok=True)

        for subfolder in SUBFOLDERS:
            subfolder_path = pilot_folder / subfolder
            subfolder_path.mkdir(exist_ok=True)

    @classmethod
    def fill_audio(cls, pilot: PilotVoice, skip=True):
        pilot_folder = cls.get_root_pilot_path() / pilot.FOLDER

        lines = pilot.get_lines()
        for line in lines:
            code = line.get_code()
            file_destination = pilot_folder / line.get_subfolder() / f'{code}.mp3'

            if skip and file_destination.exists():
                continue

            if line.is_static():
                continue

            SteosVoice.generate_sound(
                actor=line.get_actor(steos_id=pilot.STEOS_ID),
                text=line.get_temp_text(),
                file_destination=file_destination
            )
            sleep(0.2)

    @classmethod
    def fill_files_for_xml(cls, pilot: PilotVoice):
        pilots_folder = cls.get_root_pilot_path() / pilot.FOLDER
        audios_root = AudioFolder.get_apply_xml_audio_path() / f'{pilot.FOLDER}.xml'
        audios_folder = audios_root / pilot.FOLDER
        audios_root.mkdir(exist_ok=True)
        audios_folder.mkdir(exist_ok=True)

        lines = pilot.get_lines()
        for line in lines:
            code = line.get_code()

            if not line.is_static():
                file_destination = pilots_folder / line.get_subfolder() / f'{code}.mp3'
                target_destination = audios_folder / f'{code}.mp3'
            else:
                if line.is_static_from_root():
                    file_destination = cls.get_root_pilot_path() / line.get_static_file()
                else:
                    file_destination = cls.get_root_pilot_path() / pilot.STATIC_KIND / line.get_static_file()

                target_destination = audios_folder / f'{code}.wav'

            if not target_destination.exists():
                shutil.copy(str(file_destination), str(target_destination))

    @classmethod
    def build_voice_xml(cls, pilot: PilotVoice, skip=False):
        voice_path = AudioFolder.get_apply_xml_audio_path() / f'{pilot.FOLDER}.xml'

        voice = pilot.get_voice()

        xml_path = voice_path / f'{voice.voice_name}.utf.xml'
        if xml_path.exists():
            if not skip:
                raise Exception(f'Voice {voice.voice_name} is already exist. Remove it if you want to create it again')
            return

        xml_path.write_text(voice.get_xml(), encoding='utf-8')


class VanillaProps:

    def __init__(self):
        self.props = {}

    def add_prop(self, prop_name):
        self.props[prop_name] = VanillaVoiceProp(name=prop_name)

    def add_line_to_prop(self, prop_name, line):
        self.props[prop_name].add_line(line)

    def dump_names(self):
        for prop in self.props.values():
            print(prop.name)

    def dump_prop(self, prop_name):
        self.props[prop_name].dump_all()

    def convert_prop(self, prop_name):
        map = self.props[prop_name].get_id_map()
        pilot_path = TempPilot.get_root_pilot_path()
        for valid, code in map:
            file = pilot_path / prop_name / f'{code}.wav'
            if not file.exists():
                print(f'Code of {valid} is not exist')
                continue

            file.rename(pilot_path / prop_name / f'{valid}.wav')


class VanillaVoiceProp:
    def __init__(self, name):
        self.name = name
        self.lines = []

    def add_line(self, line):
        self.lines.append(line)

    def dump_all(self):
        for line in self.lines:
            print(f"L('{line}', ''),")

    def get_id_map(self):
        map = []
        for line in self.lines:
            map.append(
                (
                    line.lower(),
                    CreateId.get_audio_id(line)
                )
            )
        return map


VOICE_NAME_KEY = 'nickname'
SOUND_NAME_KEY = 'msg'


class VanillaPilot:
    FILES = [
        'voices_space_male.ini',
        'voices_space_female.ini',
        'voices_recognizable.ini',
        'voices_base_male.ini',
    ]

    @classmethod
    def get_vanilla_props_dir(cls):
        return pathlib.Path().resolve() / 'tools' / 'static'

    @classmethod
    def get_vanilla_props_lines(cls, file_name):
        response_file = open(cls.get_vanilla_props_dir() / file_name, "r")
        file_content = response_file.readlines()
        response_file.close()
        return file_content

    @classmethod
    def parse_vanilla_voice_props(cls):
        voice_props = VanillaProps()
        last_prop = None

        for file in cls.FILES:
            file_content = cls.get_vanilla_props_lines(file)
            for file_line in file_content:
                line_parsed = file_line.split('=')
                if len(line_parsed) < 2:
                    continue

                key = line_parsed[0].strip()
                value = line_parsed[1].strip()

                if key == VOICE_NAME_KEY:
                    voice_props.add_prop(value)
                    last_prop = value
                elif key == SOUND_NAME_KEY:
                    voice_props.add_line_to_prop(last_prop, value)

        return voice_props
