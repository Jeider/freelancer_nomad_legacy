from audio.delivery import HIGH_PITCH
from universe.audio.base_pilot import EnglishSystemIdentifiedVoice


class EnglishShipVoice(EnglishSystemIdentifiedVoice):
    DENOISE = False
    VOICE_DELIVERY = HIGH_PITCH
    LINES = []

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)


class EngMilitaryOne(EnglishShipVoice):
    FOLDER = 'pilot_f_mil_m01'


class EngMilitaryTwo(EnglishShipVoice):
    FOLDER = 'pilot_f_mil_m02'


class EngLegalOne(EnglishShipVoice):
    FOLDER = 'pilot_f_leg_m01'


class EngFemaleOne(EnglishShipVoice):
    FOLDER = 'pilot_f_leg_f01'
    IS_MALE = False


class EngFemaleTwo(EnglishShipVoice):
    FOLDER = 'pilot_f_leg_f01a'
    IS_MALE = False


class EngPirateOne(EnglishShipVoice):
    FOLDER = 'pilot_f_ill_m01'
    ATTENUATION = -6


class EngPirateTwo(EnglishShipVoice):
    FOLDER = 'pilot_f_ill_m02'
    ATTENUATION = -6
