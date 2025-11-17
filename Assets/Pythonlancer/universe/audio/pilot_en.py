from universe.audio.base_pilot import EnglishSystemIdentifiedVoice


class EnglishShipVoice(EnglishSystemIdentifiedVoice):
    LINES = []

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)


class EnglishMilitaryLow(EnglishShipVoice):
    STEOS_ID = 215  # Regis Witcher
    FOLDER = 'pilot_en01'


class EnglishMilitaryHigh(EnglishShipVoice):
    STEOS_ID = 211  # Lambert Witcher
    FOLDER = 'pilot_en03'


class EnglishFemale(EnglishShipVoice):
    STEOS_ID = 216  # Sylvia Anna Witcher
    FOLDER = 'pilot_en04'
    IS_MALE = False


class EnglishPirate(EnglishShipVoice):
    STEOS_ID = 181  # Reinhardt
    FOLDER = 'pilot_en08'
    ATTENUATION = -6
