from universe.audio.base_pilot import SystemIdentifiedVoice

from universe.audio.static import space_pilot as space_pilot_static
from universe.audio.static.lines_male_military import LINES as male_mil_lines
from universe.audio.static.lines_female_military import LINES as female_mil_lines
from universe.audio.static.lines_male_pirate import LINES as male_pir_lines
from universe.audio.static.lines_female_pirate import LINES as female_pir_lines


STATIC_MIL01 = 'pilot_f_mil_m01'
STATIC_MIL02 = 'pilot_f_mil_m02'
STATIC_LEG_MALE = 'pilot_f_leg_m01'
STATIC_LEG_FEMALE = 'pilot_f_leg_f01'
STATIC_ILL01 = 'pilot_f_ill_m01'
STATIC_ILL02 = 'pilot_f_ill_m02'


class EngShipVoice(SystemIdentifiedVoice):
    '''This voice is only for extending of vanilla Freelancer voices'''
    VOICE_DATA = space_pilot_static.VOICE_DATA
    MVOICE_AUDIO_PROP = ''
    MVOICE_MISSION_PROP = ''
    LINES = None

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)


class EngMilitaryOne(EngShipVoice):
    STEOS_ID = 215  # Regis Witcher
    FOLDER = 'pilot01'
    STATIC_KIND = STATIC_MIL01
    ATTENUATION = -3
    LINES = male_mil_lines
