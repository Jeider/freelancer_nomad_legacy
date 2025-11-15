from core import get_core
from managers.jinja_manager import JinjaTemplateManager

from universe.audio.pilot import ShipVoice
from universe.audio.base_pilot import PilotVoice
from universe.audio.dispatcher import StationDispatcher

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

        data_folder.sync_audio_ini(
            'voices_space_male',
            self.core.tpl_manager.get_result(VOICES_MALE_TEMPLATE, {
                'voices': DIVIDER.join(male_voices),
                'props': DIVIDER.join(male_props),
            }),
        )

        data_folder.sync_audio_ini(
            'voices_space_female',
            self.core.tpl_manager.get_result(VOICES_FEMALE_TEMPLATE, {
                'voices': DIVIDER.join(female_voices),
                'props': DIVIDER.join(female_props),
            }),
        )

        data_folder.sync_mission_voice_props(
            self.core.tpl_manager.get_result(VOICE_PROPS_TEMPLATE, {
                'props': DIVIDER.join(mission_props),
            }),
        )

    def prepare_pilots_audio(self):
        for a_pilot in ShipVoice.subclasses:
            the_pilot = a_pilot(self.core)
            TempPilot.prepare_temp_folders(the_pilot)
            TempPilot.fill_audio(the_pilot, skip=True)

            # TempPilot.fill_files_for_xml(the_pilot)
            # TempPilot.build_voice_xml(the_pilot, skip=True)

            # return

    def compile_pilots_audio(self):
        for a_pilot in ShipVoice.subclasses:
            folder = a_pilot.FOLDER
            AudioFolder.compile_file(folder)
