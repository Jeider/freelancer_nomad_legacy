SCREAM_1 = '1'
SCREAM_2 = '2'
SCREAM_3 = '3'
SCREAM_4 = '4'
SCREAM_5 = '5'
SCREAM_6 = '6'
SCREAM_7 = '7'
SCREAM_8 = '8'

SCREAMS = [
    SCREAM_1,
    SCREAM_2,
    SCREAM_3,
    SCREAM_4,
    SCREAM_5,
    SCREAM_6,
    SCREAM_7,
    SCREAM_8,
]

SUBFOLDER_DEFAULT = 'default'
SUBFOLDER_START = 'start'
SUBFOLDER_END = 'end'
SUBFOLDER_MIDDLE = 'middle'
SUBFOLDER_FORMATION = 'formation'
SUBFOLDER_NUMBER = 'number'
SUBFOLDER_BASE = 'base'
SUBFOLDER_SYSTEM = 'system'
SUBFOLDER_COMMODITY = 'commodity'
SUBFOLDER_FACTION = 'faction'

SUBFOLDERS = [
    SUBFOLDER_DEFAULT,
    SUBFOLDER_START,
    SUBFOLDER_END,
    SUBFOLDER_MIDDLE,
    SUBFOLDER_FORMATION,
    SUBFOLDER_NUMBER,
    SUBFOLDER_BASE,
    SUBFOLDER_SYSTEM,
    SUBFOLDER_COMMODITY,
    SUBFOLDER_FACTION,
]


class ParseRule:
    STEOS_PITCH = 0.3
    STEOS_SPEED = 1.1

    SUBFOLDER = SUBFOLDER_DEFAULT
    IS_STATIC = False

    @classmethod
    def get_temp_text(cls, text):
        return text

    @classmethod
    def process_temp(cls, code):
        pass  # skip, not processable

    @classmethod
    def get_subfolder(cls):
        return cls.SUBFOLDER

    @classmethod
    def is_static(cls):
        return cls.IS_STATIC

    @classmethod
    def get_static_file(cls, text):
        if not cls.is_static():
            raise Exception('not static')
        raise NotImplementedError


class RuleDefault(ParseRule):
    pass


class RuleProcessing(RuleDefault):
    TEXT_TEMPLATE = '{text}'

    @classmethod
    def get_temp_text(cls, text):
        return cls.TEXT_TEMPLATE.format(text=text)


class RuleScream(ParseRule):
    IS_STATIC = True

    @classmethod
    def get_static_file(cls, text):
        if not cls.is_static():
            raise Exception('not static')
        if text not in SCREAMS:
            raise Exception('unknown scream %s' % text)
        return f'gcs_combat_scream_0{text}-.wav'


class RuleStart(RuleProcessing):
    SUBFOLDER = SUBFOLDER_START


# <десять> вейпоинтов
class RuleStartNumber(RuleStart):
    TEXT_TEMPLATE = 'Десять {text}'


# <десять> вейпоинтов
class RuleStartNumberSingle(RuleStart):
    TEXT_TEMPLATE = 'Одна {text}'


# <что-то делаю> спасибо за помощь
class RuleContinueRequest(RuleStart):
    TEXT_TEMPLATE = 'Приехали, {text}'


# <что-то делаю> к стыковке
class RuleDockContinueRequest(RuleStart):
    TEXT_TEMPLATE = 'прошу разрешение на {text}'


class RuleEnd(RuleProcessing):
    SUBFOLDER = SUBFOLDER_END


# движусь к <станция>
class RuleEndTo(RuleEnd):
    TEXT_TEMPLATE = '{text} фрилансера'


# мне нужно <что-то сделать>
class RuleEndThing(RuleEnd):
    TEXT_TEMPLATE = '{text} стыковку'


# Я везу <что-то>
class RuleEndCargo(RuleEnd):
    TEXT_TEMPLATE = '{text} золото'


# Я везу <что-то>
class RuleEndObject(RuleEnd):
    TEXT_TEMPLATE = '{text} станция'


# мне осталось <десять>
class RuleEndNumber(RuleEnd):
    TEXT_TEMPLATE = '{text} десять'


class RuleHighAction(ParseRule):
    STEOS_PITCH = 0.7
    STEOS_SPEED = 1.4


class RuleNormalAction(ParseRule):
    STEOS_PITCH = 0.3
    STEOS_SPEED = 1.2


class RuleNormalActionWithEnd(RuleEnd):
    STEOS_PITCH = 0.5
    STEOS_SPEED = 1.2
    TEXT_TEMPLATE = '{text} точке станция'


class RuleAngry(ParseRule):
    STEOS_PITCH = -0.2
    STEOS_SPEED = 1.25


class RuleMiddle(RuleProcessing):
    FORCE_TEXT = None
    TARGET_WORD_NUMBER = 2
    SUBFOLDER = SUBFOLDER_MIDDLE


class RuleDash(RuleMiddle):
    TEXT_TEMPLATE = 'Один {text} один'


class RuleFrom(RuleMiddle):
    TEXT_TEMPLATE = 'Спокойно летит {text} красивых мест'


class RuleTo(RuleMiddle):
    TEXT_TEMPLATE = 'Спокойно направляюсь к {text} мальте'


class RuleThisIs(RuleEnd):
    TEXT_TEMPLATE = '{text} Р+эйнланд Омега семь'


class RuleFormation(RuleMiddle):
    SUBFOLDER = SUBFOLDER_FORMATION
    TEXT_TEMPLATE = 'фрилансер {text} три'
    TARGET_WORD_NUMBER = 2


class RuleNumberFirst(RuleProcessing):
    SUBFOLDER = SUBFOLDER_NUMBER
    TEXT_TEMPLATE = 'альфа {text} деш {text}'

    @classmethod
    def process_temp(cls, code):
        pass
        # song = AudioSegment.from_mp3(f'results/steos/temp/{code}.mp3')
        # chunks = split_on_silence(song, min_silence_len=MIN_SILENCE_LEN, silence_thresh=SILENCE_THRESH, keep_silence=1000)
        # silence_list = detect_silence(song, min_silence_len=MIN_SILENCE_LEN, silence_thresh=SILENCE_THRESH)
        #
        # i = 0
        # for chunk in chunks:
        #     chunk.export(f'results/steos/temp2/{code}_{i}.mp3')
        #     i += 1


class RuleNumberSecond(RuleNumberFirst):
    SUBFOLDER = SUBFOLDER_NUMBER
    TEXT_TEMPLATE = 'альфа {text} деш {text}'


class RuleBase(RuleDefault):
    SUBFOLDER = SUBFOLDER_BASE


class RuleSystem(RuleDefault):
    SUBFOLDER = SUBFOLDER_SYSTEM


class RuleCommodity(RuleDefault):
    SUBFOLDER = SUBFOLDER_COMMODITY


class RulePlayer(RuleProcessing):
    SUBFOLDER = SUBFOLDER_FACTION
    TEXT_TEMPLATE = '{text} альфа'


class RuleFaction(RuleProcessing):
    SUBFOLDER = SUBFOLDER_FACTION
    TEXT_TEMPLATE = 'говорит {text} бета'
