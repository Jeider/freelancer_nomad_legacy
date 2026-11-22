from core import get_core
from managers.jinja_manager import JinjaTemplateManager

from universe.audio.pilot import ShipVoice
from universe.audio import pilot_en
from universe.audio.base_pilot import PilotVoice
from universe.audio.dispatcher import StationDispatcher
from universe.audio import dispatcher_en

from tools.data_folder import DataFolder
from tools.audio_pilot import TempPilot
from tools.audio_folder import AudioFolder

from text.dividers import DIVIDER

VOICES_MALE_TEMPLATE = 'hardcoded_inis/static_content/voices_space_male.ini'
VOICES_FEMALE_TEMPLATE = 'hardcoded_inis/static_content/voices_space_female.ini'
VOICE_PROPS_TEMPLATE = 'hardcoded_inis/static_content/voice_properties.ini'


class PilotManager:

    def __init__(self):
        self.core = get_core()
        self.tpl_manager = JinjaTemplateManager()

    def compile_pilots_ini(self):
        pilots: list[PilotVoice] = StationDispatcher.subclasses + ShipVoice.subclasses
        # eng_pilots: list[PilotVoice] = EnglishStationDispatcher.subclasses
        male_voices = []
        male_props = []
        female_voices = []
        female_props = []
        mission_props = []

        for the_pilot in pilots:
            pilot = the_pilot(self.core)
            if not pilot.ENABLED:
                continue

            if pilot.IS_MALE:
                male_voices.append(pilot.get_voice_ini())
                male_props.append(pilot.get_voice_props_ini())
            else:
                female_voices.append(pilot.get_voice_ini())
                female_props.append(pilot.get_voice_props_ini())

            mission_props.append(pilot.get_mission_props_ini())

        data_folder = DataFolder()

        voice_male_params = {
            'voices': DIVIDER.join(male_voices),
            'props': DIVIDER.join(male_props),
            'dispatcher_en01_props': dispatcher_en.EngMaleDispatcher(core=self.core).get_file_sounds_ini(),
            'pilot_en_mil01_props': pilot_en.EngMilitaryOne(core=self.core).get_file_sounds_ini(),
            'pilot_en_mil02_props': pilot_en.EngMilitaryTwo(core=self.core).get_file_sounds_ini(),
            'pilot_en_leg01_props': pilot_en.EngLegalOne(core=self.core).get_file_sounds_ini(),
            'pilot_en_pir01_props': pilot_en.EngPirateOne(core=self.core).get_file_sounds_ini(),
            'pilot_en_pir02_props': pilot_en.EngPirateTwo(core=self.core).get_file_sounds_ini(),
        }

        voice_female_params = {
            'voices': DIVIDER.join(female_voices),
            'props': DIVIDER.join(female_props),
            'dispatcher_en02_props': dispatcher_en.EngFemaleDispatcher(core=self.core).get_file_sounds_ini(),
            'dispatcher_en03_props': dispatcher_en.EngFemaleRoboDispatcher(core=self.core).get_file_sounds_ini(),
            'pilot_leg01_props': pilot_en.EngFemaleOne(core=self.core).get_file_sounds_ini(),
            'pilot_leg02_props': pilot_en.EngFemaleTwo(core=self.core).get_file_sounds_ini(),
        }

        # RU dispatcher WAVs and their INI paths form one verified transaction.
        from pathlib import Path
        from tools.dispatcher_files import compile_dispatchers
        files = {
            'AUDIO/voices_space_male.ini': self.core.tpl_manager.get_result(VOICES_MALE_TEMPLATE, voice_male_params).encode('utf-8'),
            'AUDIO/voices_space_female.ini': self.core.tpl_manager.get_result(VOICES_FEMALE_TEMPLATE, voice_female_params).encode('utf-8'),
            'MISSIONS/voice_properties.ini': self.core.tpl_manager.get_result(VOICE_PROPS_TEMPLATE, {
                'props': DIVIDER.join(mission_props),
            }).encode('utf-8'),
        }
        project = Path(__file__).resolve().parents[2]
        return compile_dispatchers(project, data_folder, files, output=project/'results/dispatcher_files')

    def prepare_pilots_audio(self):
        for a_pilot in pilot_en.EnglishShipVoice.subclasses:
            the_pilot = a_pilot(self.core)
            TempPilot.prepare_temp_folders(the_pilot)
            TempPilot.fill_audio(the_pilot, skip=True)

            TempPilot.fill_files_for_xml(the_pilot, russian=False)
            # TempPilot.build_voice_xml(the_pilot, skip=True)

            # return

    def compile_pilots_audio(self):
        # Keep the established command, now compiling WAV files and matching INIs.
        return self.compile_pilots_ini()
