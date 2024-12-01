from tools.utf_xml import XML_UTF
from tools.data_folder import DataFolder
from tools.steos import SteosVoice
from tools.audio_folder import AudioFolder
import pathlib
import shutil
from time import sleep

from universe.audio.pilot import SUBFOLDERS, ShipVoice

PILOTS_FOLDER = 'PILOTS'
RAW_FOLDER = 'RAW'

class TempPilot:

    @staticmethod
    def get_root_pilot_path():
        current_path = pathlib.Path().resolve()
        return current_path.parent / PILOTS_FOLDER

    @classmethod
    def prepare_temp_folders(cls, pilot: ShipVoice):
        pilot_folder = cls.get_root_pilot_path() / pilot.FOLDER

        pilot_folder.mkdir(exist_ok=True)

        for subfolder in SUBFOLDERS:
            subfolder_path = pilot_folder / subfolder
            subfolder_path.mkdir(exist_ok=True)

    @classmethod
    def fill_audio(cls, pilot: ShipVoice, skip=True):
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
    def fill_files_for_xml(cls, pilot: ShipVoice):
        pilots_folder = cls.get_root_pilot_path() / pilot.FOLDER
        audios_folder = AudioFolder.get_apply_audio_path() / f'{pilot.FOLDER}.xml' / pilot.FOLDER

        lines = pilot.get_lines()
        for line in lines:
            code = line.get_code()

            if not line.is_static():
                file_destination = pilots_folder / line.get_subfolder() / f'{code}.mp3'
            else:
                file_destination = cls.get_root_pilot_path() / 'STATIC' / pilot.STATIC_KIND / f'{code}.wav'

            target_destination = audios_folder / f'{code}.mp3'

            if not target_destination.exists():
                shutil.copy(str(file_destination), str(target_destination))

    @classmethod
    def build_voice_xml(cls, pilot: ShipVoice, skip=False):
        voice_path = AudioFolder.get_apply_audio_path() / f'{pilot.FOLDER}.xml'

        voice = pilot.get_voice()

        xml_path = voice_path / f'{voice.voice_name}.utf.xml'
        if xml_path.exists():
            if not skip:
                raise Exception(f'Voice {voice.voice_name} is already exist. Remove it if you want to create it again')
            return

        xml_path.write_text(voice.get_xml(), encoding='utf-8')
