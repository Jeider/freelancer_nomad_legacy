from universe.audio.base_pilot import SignedVoice

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


class ShipVoice(SignedVoice):
    VOICE_DATA = space_pilot_static.VOICE_DATA
    MVOICE_AUDIO_PROP = space_pilot_static.MVOICE_AUDIO_PROP
    MVOICE_MISSION_PROP = space_pilot_static.MVOICE_MISSION_PROP
    LINES = None

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)


class MilitaryOne(ShipVoice):
    STEOS_ID = 215  # Regis Witcher
    FOLDER = 'pilot01'
    STATIC_KIND = STATIC_MIL01
    ATTENUATION = -3
    LINES = male_mil_lines


class MilitaryTwo(ShipVoice):
    STEOS_ID = 210  # Hjalmar an Craite Witcher
    FOLDER = 'pilot02'
    STATIC_KIND = STATIC_MIL02
    ENABLED = True
    LINES = male_mil_lines


class MilitaryThree(ShipVoice):
    STEOS_ID = 211  # Lambert Witcher
    FOLDER = 'pilot03'
    STATIC_KIND = STATIC_MIL02
    LINES = male_mil_lines


class MilitaryFour(ShipVoice):
    STEOS_ID = 216  # Sylvia Anna Witcher
    FOLDER = 'pilot04'
    STATIC_KIND = STATIC_LEG_FEMALE
    IS_MALE = False
    LINES = female_mil_lines


class MilitaryFive(ShipVoice):
    STEOS_ID = 206  #"Cerys an Craite Witcher
    FOLDER = 'pilot05'
    STATIC_KIND = STATIC_LEG_FEMALE
    IS_MALE = False
    LINES = female_mil_lines


class PirateOne(ShipVoice):
    STEOS_ID = 10067
    FOLDER = 'pilot06'
    STATIC_KIND = STATIC_ILL01
    ATTENUATION = -12
    LINES = male_pir_lines


class PirateTwo(ShipVoice):
    STEOS_ID = 296
    FOLDER = 'pilot07'
    STATIC_KIND = STATIC_ILL01
    ATTENUATION = -12
    LINES = male_pir_lines


class PirateThree(ShipVoice):
    STEOS_ID = 181  # Reinhardt
    FOLDER = 'pilot08'
    STATIC_KIND = STATIC_ILL02
    ATTENUATION = -6
    LINES = male_pir_lines


class PirateFour(ShipVoice):
    STEOS_ID = 166  # Zarya
    FOLDER = 'pilot09'
    STATIC_KIND = STATIC_LEG_FEMALE
    IS_MALE = False
    ATTENUATION = -6
    LINES = female_pir_lines
