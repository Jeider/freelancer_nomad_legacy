from core import get_core

from universe.audio.pilot import ShipVoice
from universe.audio.base_pilot import PilotVoice
from universe.audio.dispatcher import StationDispatcher

from templates.hardcoded_inis.audio import VoicesSpaceMaleTemplate, VoicesSpaceFemaleTemplate
from templates.hardcoded_inis.missions import VoicePropertiesTemplate

from tools.data_folder import DataFolder
from tools.audio_pilot import TempPilot
from tools.audio_folder import AudioFolder

from text.dividers import DIVIDER


class PilotManager:

    @classmethod
    def compile_pilots_ini(cls):
        core = get_core()
        pilots: list[PilotVoice] = StationDispatcher.subclasses + ShipVoice.subclasses
        male_voices = []
        male_props = []
        female_voices = []
        female_props = []
        mission_props = []

        for the_pilot in pilots:
            pilot = the_pilot(core)
            if not pilot.ENABLED:
                continue

            if pilot.IS_MALE:
                male_voices.append(pilot.get_voice_ini())
                male_props.append(pilot.get_voice_props_ini())
            else:
                female_voices.append(pilot.get_voice_ini())
                female_props.append(pilot.get_voice_props_ini())

            mission_props.append(pilot.get_mission_props_ini())

        DataFolder.sync_audio_ini(
            'voices_space_male',
            VoicesSpaceMaleTemplate().format({
                'voices': DIVIDER.join(male_voices),
                'props': DIVIDER.join(male_props),
            })
        )

        DataFolder.sync_audio_ini(
            'voices_space_female',
            VoicesSpaceFemaleTemplate().format({
                'voices': DIVIDER.join(female_voices),
                'props': DIVIDER.join(female_props),
            })
        )

        DataFolder.sync_mission_voice_props(
            VoicePropertiesTemplate().format({
                'props': DIVIDER.join(mission_props),
            })
        )

    @classmethod
    def prepare_pilots_audio(cls):
        core = get_core()
        for a_pilot in ShipVoice.subclasses:
            the_pilot = a_pilot(core)
            TempPilot.prepare_temp_folders(the_pilot)
            TempPilot.fill_audio(the_pilot, skip=True)

            TempPilot.fill_files_for_xml(the_pilot)
            TempPilot.build_voice_xml(the_pilot, skip=True)

            # return

    @classmethod
    def compile_pilots_audio(cls):
        for a_pilot in ShipVoice.subclasses:
            folder = a_pilot.FOLDER
            AudioFolder.compile_file(folder)
