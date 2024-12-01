from story.actors import DynamicActor

from pydub import AudioSegment
from pydub.silence import split_on_silence, detect_silence

from audio.sound import SpaceSound
from audio.voice import Voice

MIN_SILENCE_LEN = 18
SILENCE_THRESH = -18


class L(object):
    def __init__(self, code, ru_text, parse_rule=None):
        self.code = code
        self.ru_text = ru_text
        self.parse_rule = parse_rule if parse_rule else RuleDefault

    def get_text(self):
        return self.ru_text

    def get_temp_text(self):
        return self.parse_rule.get_temp_text(self.ru_text)

    def get_actor(self, steos_id):
        return DynamicActor(
            steos_id=steos_id,
            steos_pitch=self.parse_rule.STEOS_PITCH,
            steos_speed=self.parse_rule.STEOS_SPEED,
        )

    def get_code(self):
        return self.code

    def get_subfolder(self):
        return self.parse_rule.get_subfolder()

    def process_temp(self):
        return self.parse_rule.process_temp(self.code)

    def is_static(self):
        return self.parse_rule.is_static()

    def get_static_file(self):
        return self.parse_rule.get_static_file(self.ru_text)


NAME_AT_END = 1

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

SCREAM_TEMPLATE = 'gcs_combat_scream_0{digit}-'
FORMATION_TEMPLATE = 'gcs_refer_formationdesig_{digit:02d}'
NUMBER_START_TEMPLATE = 'gcs_misc_number_{digit}'
NUMBER_END_TEMPLATE = 'gcs_misc_number_{digit}-'
TEMP_FORMATION_TEMPLATE = 'formation_{digit}'
TEMP_NUMBER_TEMPLATE = 'number_{digit}'

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
    TEXT_TEMPLATE = 'Разрешите {text}'


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
    TEXT_TEMPLATE = '{text} три'
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


class RuleFaction(RuleDefault):
    SUBFOLDER = SUBFOLDER_FACTION


FORMATIONS = [
    (1, '+альфа'),
    (2, 'б+эта'),
    (3, 'г+амма'),
    (4, 'д+ельта'),
    (5, '+эпсилон'),
    (6, 'з+ета'),
    (7, 'т+ета'),
    (8, 'й+ота'),
    (9, 'к+аппа'),
    (10, 'л+ямбда'),
    (11, 'омикр+он'),
    (12, 'с+игма'),
    (13, 'ом+ега'),
    (14, 'кр+асный'),
    (15, 'с+иний'),
    (16, 'золот+ой'),
    (17, 'зел+ёный'),
    (18, 'сер+ебрянный'),
    (19, 'ч+ерный'),
    (20, 'б+елый'),
    (21, 'ж+елтый'),
    (22, 'м+атсу'),
    (23, 'с+акура'),
    (24, 'ф+удзи'),
    (25, 'бот+ан'),
    (26, 'х+аги'),
    (27, 'суз+уки'),
    (28, 'к+ику'),
    (29, 'ян+аги'),
]

NUMBERS = [
    (0, 'ноль'),
    (1, 'один'),
    (2, 'два'),
    (3, 'три'),
    (4, 'четыре'),
    (5, 'пять'),
    (6, 'шесть'),
    (7, 'семь'),
    (8, 'восемь'),
    (9, 'девять'),
    (10, 'десять'),
    (11, 'од+иннадцать'),
    (12, 'двен+адцать'),
    (13, 'трин+адцать'),
    (14, 'чет+ырнадцать'),
    (15, 'пятн+адцать'),
    (16, 'шестн+адцать'),
    (17, 'семн+адцать'),
    (18, 'восемн+адцать'),
    (19, 'девятн+адцать'),
    (20, 'дв+адцать'),
]


class ShipVoice(object):
    STEOS_ID = None
    FOLDER = None
    STATIC_KIND = None
    LINES = [
        L('gcs_combat_announce_allclear_01-', 'Противников не обнаружено.'),
        L('gcs_combat_announce_allclear_02-', 'На сканерах больше нет неприятелей.'),
        L('gcs_combat_announce_allclear_03-', 'Зона зачищена.'),
        L('gcs_combat_announce_allclear_04-', 'Врагов не видно.'),
        L('gcs_combat_announce_allclear_05-', 'Зона в зеленом статусе. Врагов не обнаружено.'),
        L('gcs_combat_announce_allclear_06-', 'Зона чиста. Враждебные контакты отсутствуют.'),
        L('gcs_combat_announce_combatdrift_01-', 'Этот контакт отвлечет нас задания. Давайте не отвлекаться на него', RuleNormalAction),
        L('gcs_combat_announce_combatdrift_02-', 'Держать строй, мы постараемся избежать сражения', RuleNormalAction),
        L('gcs_combat_announce_combatdrift_03-', 'Концентрируемся на нашей задаче, у нас нет времени отвлекаться на каждого неприятеля', RuleNormalAction),
        L('gcs_combat_announce_enemysighted_01-', 'Вижу нового неприятеля.', RuleNormalAction),
        L('gcs_combat_announce_enemysighted_02-', 'На радаре новый противник.', RuleNormalAction),
        L('gcs_combat_announce_enemysighted_03-', 'Замечена новая угроза. Неприятель.', RuleNormalAction),
        L('gcs_combat_announce_enemysighted_04-', 'На сканере замечены неприятели!', RuleNormalAction),
        L('gcs_combat_announce_ff_01-', 'Смотри куда стреляешь!', RuleAngry),
        L('gcs_combat_announce_ff_02-', 'Прекрати стрелять, фрилансер!', RuleAngry),
        L('gcs_combat_announce_ff_03-', 'Хватит стрелять по мне!', RuleAngry),
        L('gcs_combat_announce_flee_01-', 'Уходим!', RuleHighAction),
        L('gcs_combat_announce_flee_02-', 'Я улетаю!', RuleHighAction),
        L('gcs_combat_announce_flee_03-', 'К чёрту всё, я улетаю отсюда.', RuleHighAction),
        L('gcs_combat_announce_flee_04-', 'Я отступаю.', RuleHighAction),
        L('gcs_combat_announce_flee_05-', 'Мне нужна прегрупировка.', RuleHighAction),
        L('gcs_combat_announce_flee_06-', 'Я сваливаю отсюда.', RuleHighAction),
        L('gcs_combat_askengage_01-', 'Разрешите атаковать.', RuleNormalAction),
        L('gcs_combat_askengage_02-', 'Запрашиваю открыть огонь.', RuleNormalAction),
        L('gcs_combat_askengage_03-', 'Ожидаю приказа на перехват.', RuleNormalAction),
        L('gcs_combat_askengage_04-', 'Запрашиваю разрешение открыть огонь!', RuleNormalAction),
        L('gcs_combat_askforhelp_01-', 'Мне нужна поддержка!', RuleHighAction),
        L('gcs_combat_askforhelp_02-', 'Запрашиваю поддержку!', RuleHighAction),
        L('gcs_combat_askforhelp_03-', 'Прикройте меня!', RuleHighAction),
        L('gcs_combat_askforhelp_04-', 'Нужна поддержка!', RuleHighAction),
        L('gcs_combat_askforhelp_05-', 'Запрашиваю дополнительную поддержку!', RuleHighAction),
        L('gcs_combat_brag_01-', 'Неприятель уничтожен.', RuleNormalAction),
        L('gcs_combat_brag_02-', 'Враг уничтожен.', RuleNormalAction),
        L('gcs_combat_brag_03-', 'Вражеская цель ликвидирована.', RuleNormalAction),
        L('gcs_combat_brag_04-', 'Неприятель ликвидирован.', RuleNormalAction),
        L('gcs_combat_brag_05-', 'Враг нейтрализован.', RuleNormalAction),
        L('gcs_combat_brag_06-', 'Неприятель был нейтрализован.', RuleNormalAction),
        L('gcs_combat_comingin_p_01-', 'Мы на пути к тебе.', RuleNormalAction),
        L('gcs_combat_comingin_p_02-', 'Подожди, скоро будем тут.', RuleNormalAction),
        L('gcs_combat_comingin_p_03-', 'Жди, летим к тебе.', RuleNormalAction),
        L('gcs_combat_comingin_s_01-', 'Я скоро буду здесь.', RuleNormalAction),
        L('gcs_combat_comingin_s_02-', 'Я в пути.', RuleNormalAction),
        L('gcs_combat_comingin_s_03-', 'Жди, я лечу к тебе.', RuleNormalAction),
        L('gcs_combat_deathsympathy_01-', 'Нашего сбили!', RuleHighAction),
        L('gcs_combat_deathsympathy_02-', 'Я потерял ведомого!', RuleHighAction),
        L('gcs_combat_deathsympathy_03-', 'Член крыла убит!', RuleHighAction),
        L('gcs_combat_deathsympathy_04-', 'Моего сбили!', RuleHighAction),
        L('gcs_combat_engaging_01+', 'Готовлюсь к перехвату', RuleEndTo),
        L('gcs_combat_engaging_02+', 'Я перехватываю', RuleEndTo),
        L('gcs_combat_engaging_03+', 'Перехватываю', RuleEndTo),
        L('gcs_combat_engaging_04+', 'Приступаю к перехвату', RuleEndTo),
        L('gcs_combat_fleereason_damaged_01-', 'Я сильно поврежден', RuleHighAction),
        L('gcs_combat_fleereason_damaged_02-', 'Мои повреждения критические', RuleHighAction),
        L('gcs_combat_fleereason_damaged_03-', 'Мой корабль повреждён', RuleHighAction),
        L('gcs_combat_fleereason_noweapons_01-', 'Я потерял пушки', RuleHighAction),
        L('gcs_combat_fleereason_noweapons_02-', 'У меня больше нет пушек', RuleHighAction),
        L('gcs_combat_fleereason_noweapons_03-', 'Я потерял своё вооружение', RuleHighAction),
        L('gcs_combat_fleereason_other_01-', 'Дел+а плохи, в+алим', RuleHighAction),
        L('gcs_combat_fleereason_other_02-', 'Пор+а сваливать, тут делать нечего', RuleHighAction),
        L('gcs_combat_fleereason_other_03-', 'Наше положение ужасное', RuleHighAction),
        L('gcs_combat_fleereason_tough_01-', 'Ситуация ужасная', RuleHighAction),
        L('gcs_combat_fleereason_tough_02-', 'Всё очень плохо, сражаться бессмысленно', RuleHighAction),
        L('gcs_combat_fleereason_tough_03-', 'Не вижу смысла продолжать сражение', RuleHighAction),
        L('gcs_combat_hasinsights_01-', 'Контакт в радиусе видимости', RuleNormalAction),
        L('gcs_combat_hasinsights_02-', 'Наблюдаю противника', RuleNormalAction),
        L('gcs_combat_hasinsights_03-', 'Визуальный контакт. Готовлюсь к атаке', RuleNormalAction),
        L('gcs_combat_hasinsights_04-', 'Рядом враг', RuleNormalAction),
        L('gcs_combat_hasinsights_05-', 'Противник вблиз+и от меня', RuleNormalAction),
        L('gcs_combat_hasinsights_06-', 'Направляюсь к вражеской цели', RuleNormalAction),
        L('gcs_combat_inflicting_damage_01-', 'Враг на мушке', RuleNormalAction),
        L('gcs_combat_inflicting_damage_02-', 'Противник повреждён!', RuleNormalAction),
        L('gcs_combat_inflicting_damage_03-', 'Противник терпит повреждения!', RuleNormalAction),
        L('gcs_combat_inflicting_damage_04-', 'Наношу повреждения противнику!', RuleNormalAction),
        L('gcs_combat_inflicting_damage_05-', 'Попал по нему!', RuleNormalAction),
        L('gcs_combat_inflicting_damage_06-', 'Враг под моим огнём!', RuleNormalAction),
        L('gcs_combat_inflicting_damage_worst_01-', 'Враг почти уничтожен', RuleNormalAction),
        L('gcs_combat_inflicting_damage_worst_02-', 'Цель горит!', RuleNormalAction),
        L('gcs_combat_inflicting_damage_worst_03-', 'Враг больше не выдержит', RuleNormalAction),
        L('gcs_combat_inflicting_damage_worst_04-', 'Почти убил его', RuleNormalAction),
        L('gcs_combat_inflicting_damage_worst_05-', 'Противник почти убит', RuleNormalAction),
        L('gcs_combat_inflicting_damage_worst_06-', 'Цель почти уничтожена', RuleNormalAction),
        L('gcs_combat_insights_01-', 'Преследую врага', RuleNormalAction),
        L('gcs_combat_insights_02-', 'Враг на прицеле', RuleNormalAction),
        L('gcs_combat_insights_03-', 'Вражеская цель захвачена', RuleNormalAction),
        L('gcs_combat_insights_04-', 'Иду за врагом', RuleNormalAction),
        L('gcs_combat_insights_05-', 'Взял цель', RuleNormalAction),
        L('gcs_combat_insights_06-', 'Преследую его', RuleNormalAction),
        L('gcs_combat_noengagereason_toofar_01-', 'Он улетел слишком далеко', RuleNormalAction),
        L('gcs_combat_noengagereason_toofar_02-', 'Не вижу смысла догонять его', RuleNormalAction),
        L('gcs_combat_noengagereason_toofar_03-', 'Кажется враг что-то задумал, давайте не поддаваться на это', RuleNormalAction),
        L('gcs_combat_noengagereason_tootough_01-', 'Слишком опасно', RuleNormalAction),
        L('gcs_combat_noengagereason_tootough_02-', 'У нас нет столько сил', RuleNormalAction),
        L('gcs_combat_noengagereason_tootough_03-', 'Мне это не нравится', RuleNormalAction),
        L('gcs_combat_noengaging_01+', 'Я не преследую', RuleNormalAction),
        L('gcs_combat_noengaging_02+', 'Нет, я не преследую', RuleNormalAction),
        L('gcs_combat_offerhelp_01-', 'Нужна помощь?', RuleNormalAction),
        L('gcs_combat_offerhelp_02-', 'Подкрепление прибыло.', RuleNormalAction),
        L('gcs_combat_offerhelp_03-', 'Мы пришли на помощь', RuleNormalAction),
        L('gcs_combat_offerhelp_04-', 'Я думаю вам нужна поддержка', RuleNormalAction),
        L('gcs_combat_offerhelp_05-', 'Эй, друг, нужна помощь?', RuleNormalAction),
        L('gcs_combat_order_disengage_01-', 'Прекратить атаку, пилоты', RuleNormalAction),
        L('gcs_combat_order_disengage_02-', 'Звено, отменить атаку', RuleNormalAction),
        L('gcs_combat_order_disengage_03-', 'Прекратить стрельбу', RuleNormalAction),
        L('gcs_combat_order_disengage_04-', 'Звено, прекратить стрильбу', RuleNormalAction),
        L('gcs_combat_order_disengage_05-', 'Пилоты, прекращаем атаку', RuleNormalAction),
        L('gcs_combat_order_engage_01-', 'Огонь на поражение', RuleNormalAction),
        L('gcs_combat_order_engage_02-', 'Огонь по готовности!', RuleNormalAction),
        L('gcs_combat_order_engage_03-', 'Открыть огонь!', RuleNormalAction),
        L('gcs_combat_order_engage_04-', 'Преследуем!', RuleNormalAction),
        L('gcs_combat_order_engage_05-', 'Атакуем!', RuleNormalAction),
        L('gcs_combat_order_engage_06-', 'Уничтожить!', RuleNormalAction),
        L('gcs_combat_order_noengage_01-', 'Не преследуйте вражескую цель', RuleNormalAction),
        L('gcs_combat_order_noengage_02-', 'Внимание всем, запрещаю атаковать вражескую цель!', RuleNormalAction),
        L('gcs_combat_order_noengage_03-', 'Не стрелять! Остановить атаку!', RuleNormalAction),
        L('gcs_combat_order_noengage_04-', 'Не стреляем', RuleNormalAction),
        L('gcs_combat_order_retreattowards_01+', 'Уходим, направляемся к', RuleNormalActionWithEnd),
        L('gcs_combat_order_retreattowards_02+', 'Прекращаем атаку и возвращаемся к', RuleNormalActionWithEnd),
        L('gcs_combat_order_retreattowards_03+', 'Все назад к', RuleNormalActionWithEnd),
        L('gcs_combat_order_retreattowards_04+', 'Приказываю орстановить операцию, летим к', RuleNormalActionWithEnd),
        L('gcs_combat_order_retreattowards_05+', 'Уходим к', RuleNormalActionWithEnd),
        L('gcs_combat_order_retreattowards_06+', 'Приказ направляться к', RuleNormalActionWithEnd),
        L('gcs_combat_rejoiningform_01-', 'Отменяю цель и возвращаюсь в формацию', RuleNormalAction),
        L('gcs_combat_rejoiningform_02-', 'Возвращаюсь в формацию', RuleNormalAction),
        L('gcs_combat_resume_patrol_01-', 'Возвращаемся к нашему патрулированию', RuleNormalAction),
        L('gcs_combat_resume_patrol_02-', 'Возобновляем патруль', RuleNormalAction),
        L('gcs_combat_resume_patrol_03-', 'Приступаем к плану патрулированию', RuleNormalAction),
        L('gcs_combat_resume_patrol_04-', 'Возобновляем наш патруль', RuleNormalAction),
        L('gcs_combat_resume_trade_01+', 'Возвращаемся к нашей торговой миссии', RuleNormalAction),
        L('gcs_combat_resume_trade_02+', 'Возобновляем торговую миссию', RuleNormalAction),
        L('gcs_combat_resume_trade_03+', 'Приступаем к нашей торговой миссии', RuleNormalAction),
        L('gcs_combat_resume_trade_04+', 'Возобновляем движение по торговому пути', RuleNormalAction),
        L('gcs_combat_scream_01-', SCREAM_1, RuleScream),
        L('gcs_combat_scream_02-', SCREAM_2, RuleScream),
        L('gcs_combat_scream_03-', SCREAM_3, RuleScream),
        L('gcs_combat_scream_04-', SCREAM_4, RuleScream),
        L('gcs_combat_scream_05-', SCREAM_5, RuleScream),
        L('gcs_combat_scream_06-', SCREAM_6, RuleScream),
        L('gcs_combat_scream_07-', SCREAM_7, RuleScream),
        L('gcs_combat_scream_08-', SCREAM_8, RuleScream),
        L('gcs_combat_taking_damage_01-', 'Я поврежден!', RuleHighAction),
        L('gcs_combat_taking_damage_02-', 'Меня атаковали!', RuleHighAction),
        L('gcs_combat_taking_damage_03-', 'Я под огнём!', RuleHighAction),
        L('gcs_combat_taking_damage_04-', 'Противник стреляет по мне!', RuleHighAction),
        L('gcs_combat_taking_damage_05-', 'Я атакован, но вроде в порядке!', RuleHighAction),
        L('gcs_combat_taking_damage_06-', 'Меня преследуют!', RuleHighAction),
        L('gcs_combat_taking_damage_07-', 'Противник атакует меня!', RuleHighAction),
        L('gcs_combat_taking_damage_08-', 'Я под вражеским огнём!', RuleHighAction),
        L('gcs_combat_taking_damage_worst_01-', 'Системы едва функционируют!', RuleHighAction),
        L('gcs_combat_taking_damage_worst_02-', 'Я не выдерживаю!', RuleHighAction),
        L('gcs_combat_taking_damage_worst_03-', 'Системы обеспечения отказывают!', RuleHighAction),
        L('gcs_combat_taking_damage_worst_04-', 'Я под огнём! Корабль горит!', RuleHighAction),
        L('gcs_combat_taking_damage_worst_05-', 'Я на грани!', RuleHighAction),
        L('gcs_combat_taking_damage_worst_06-', 'Повреждения критичны...', RuleHighAction),
        L('gcs_combat_taking_damage_worst_07-', 'Я почти уничтожен!', RuleHighAction),
        L('gcs_combat_taking_damage_worst_08-', 'Я теряю контроль!', RuleHighAction),
        L('gcs_combat_takinglead_01-', 'Я беру контроль на себя', RuleNormalAction),
        L('gcs_combat_takinglead_02-', 'Теперь я вед+у звен+о', RuleNormalAction),
        L('gcs_combat_takinglead_03-', 'Беру командование на себя', RuleNormalAction),
        L('gcs_combat_takinglead_04-', 'Я вед+у звен+о', RuleNormalAction),
        L('gcs_dhail_angry_response_01-', 'А ну отвали, тебе тут нечего смотреть!', RuleAngry),
        L('gcs_dockhail_hailee_datasubmit_01-', 'Высылаю данные'),
        L('gcs_dockhail_hailee_datasubmit_02-', 'Начинаю отсылать данные'),
        L('gcs_dockrequest_goingto_01+', 'Мы движемся к', RuleEndObject),
        L('gcs_dockrequest_jumpgatedelayed_01-', 'Мы не единственные, кто движется к', RuleEndObject),
        L('gcs_dockrequest_jumpgateopen_01-', 'Ребята, доступ открыт, движемся к', RuleEndObject),
        L('gcs_dockrequest_jumpgateopenafterdelay_01-','Доступ получен, теперь наш черёд'),
        L('gcs_dockrequest_request_01+', 'Мне нужно', RuleEndThing),
        L('gcs_dockrequest_request_02+', 'Я запрашиваю', RuleEndThing),
        L('gcs_dockrequest_thankshelp_01-', 'спасибо за помощь', RuleContinueRequest),
        L('gcs_dockrequest_thisourstop_01-', 'Так, здесь наша остановка'),
        L('gcs_dockrequest_todock-', 'стыковку', RuleDockContinueRequest),
        L('gcs_dockrequest_toland-', 'посадку', RuleDockContinueRequest),
        L('gcs_dockrequest_tomoor-', 'швартовку', RuleDockContinueRequest),
        L('gcs_dockrequest_tradelanestart_01-', 'Запускаю торговую линию'),
        L('gcs_fidget_patrol_wpremainquery_01-', 'Как много точек пути нам нужно пролететь?'),
        L('gcs_fidget_patrolrumor_01-', 'Когда-то и меняла вела дорога приключений. А потом мне прострелили колено'),
        L('gcs_fidget_patrolsimple_01-', 'Давайте спокойно, у нас обычная патрульная миссия'),
        L('gcs_fidget_saystatus_damagelarge_01-', 'Повреждения корабля значительны, не знаю как я долечу до базы'),
        L('gcs_fidget_saystatus_damagemedium_01-', 'Корабль заметно повреждён, но функционирует'),
        L('gcs_fidget_saystatus_damagenone_01-', 'Статус корабля: все системы работают штатно'),
        L('gcs_fidget_saystatus_damagesmall_01-', 'Меня потрепало, но в целом всё в порядке'),
        L('gcs_fidget_talkcargo_01-', 'обещает хорошую выручку'),
        L('gcs_fidget_trade_ihear_01+', 'Я слышал о месте, полном...'),
        L('gcs_fidget_trade_simple_01-', 'С этим грузом я заработаю себе билет в новую жизнь!'),
        L('gcs_fidget_trade_simple_02-', 'Надеюсь в этот раз на нас никто не нападёт'),
        L('gcs_fidget_trade_simple_03-', 'Доделаю эту торговую миссию и займусь чем-то более спокойным...'),
        L('gcs_fidget_traderumor_01-', 'Я слышал можно заработать на перепродаже особых сплавов'),
        L('gcs_fidget_whatstatus_01-', 'Команда, должите ситуацию. Какой наш статус?'),


        L('gcs_misc_ack_01-', 'Подтверждаю'),
        L('gcs_misc_ack_02-', 'Цель понял'),
        L('gcs_misc_ack_03-', 'Так точно'),
        L('gcs_misc_attentionallwingmen_01+', 'Внимание всем участникам звена'),
        L('gcs_misc_goingto_p_01+', 'мы направляемся'),
        L('gcs_misc_goingto_s_01+', 'я движусь'),
        L('gcs_patrol_finished_p_01-', 'Мы завершаем наш патруль'),
        L('gcs_patrol_finished_s_01-', 'Я завершаю патрулирование'),
        L('gcs_patrol_idhome_p_01+', 'Мы на пути из', RuleEndTo),
        L('gcs_patrol_idhome_p_02+', 'Мы в патруле из', RuleEndTo),
        L('gcs_patrol_idhome_s_01+', 'Я направляюсь из', RuleEndTo),
        L('gcs_patrol_idhome_s_02+', 'Я в патруле из', RuleEndTo),
        L('gcs_patrol_ihave+', 'Мне осталось', RuleEndNumber),
        L('gcs_patrol_ihaveonly+', 'Мне осталась только', RuleEndNumber),
        L('gcs_patrol_morewpstogo-', 'точек пути', RuleStartNumber),
        L('gcs_patrol_morewptogo-', 'точка пути', RuleStartNumberSingle),
        L('gcs_patrol_wehave+', 'Нам осталось', RuleEndNumber),
        L('gcs_patrol_wehaveonly+', 'Нам осталась', RuleEndNumber),
        L('gcs_phail_blowoff_01-', 'Тебе нужно что-то еще?', RuleAngry),
        L('gcs_phail_blowoff_02-', 'Я уже тебе всё рассказал!', RuleAngry),
        L('gcs_phail_combatblowoff_01-', 'Хватит меня отвлекать, я в бо+ю!', RuleHighAction),


        L('gcs_misc_dash', 'дэш', RuleDash),
        L('gcs_misc_from', 'из', RuleFrom),
        L('gcs_misc_to', 'к', RuleTo),
        L('gcs_misc_thisis+', 'говорит', RuleThisIs),

        L('gcs_trade_carrying_p_01+', 'Вы везем', RuleEndCargo),
        L('gcs_trade_carrying_s_01+', 'Я везу', RuleEndCargo),
        L('gcs_trade_idhome_p_01+', 'Наш торговый конвой направляется из точки', RuleEndObject),
        L('gcs_trade_idhome_p_02+', 'Мы на торговой миссии из точки', RuleEndObject),
        L('gcs_trade_idhome_s_01+', 'Я торговец с пункта', RuleEndObject),
        L('gcs_trade_idhome_s_02+', 'Я выполняю торговую миссию из пункта', RuleEndObject),
        L('gcs_trade_wanttoget_p_01+', 'Мы планируем загрузить', RuleEndCargo),
        L('gcs_trade_wanttoget_s_01+', 'Я хочу загрузить', RuleEndCargo),

        L('gcs_scan_angry_01-', 'Ты совершил очень больш+ую ошибку...', RuleAngry),
        L('gcs_scan_angry_02-', 'Штож, ты не оставил мне выбора.', RuleAngry),
        L('gcs_scan_angry_03-', 'Ты теперь попал по полной...', RuleAngry),
        L('gcs_scan_announce_01-', 'Сейчас я просканирую твой трюм на наличие контрабанды.'),
        L('gcs_scan_announce_02-', 'Стой на месте, я сканирую трюм твоего корабля.'),
        L('gcs_scan_announce_03-', 'Я исполняю приказ на сканирование твоего трюма.'),
        L('gcs_scan_comply_01-', 'Ладно, ч+ёрт с тобой, лети. Но я тебя не забуду и точно найду'),
        L('gcs_scan_comply_02-', 'Ты можешь улететь с этим грузом, но тебе от нас не уйти. Мы тебя найдём везде'),
        L('gcs_scan_comply_03-', 'Ну штож, таким образом ты нарушаешь закон. Ты это понимаешь?'),
        L('gcs_scan_happy_01-', 'Ты сделал правильный выбор'),
        L('gcs_scan_happy_02-', 'Это ты правильно поступил.'),
        L('gcs_scan_happy_03-', 'Отлично. Спасибо за сотрудничество'),
        L('gcs_scan_lootdestroyed_01-', 'Да блин, мы потеряли груз', RuleAngry),
        L('gcs_scan_lootdestroyed_02-', 'Чёрт, груз уничтожен.', RuleAngry),
        L('gcs_scan_lootdestroyed_03-', 'Мы потеряли груз...', RuleAngry),
        L('gcs_scan_nothingfound_01-', 'Трюм чист, ты свободен.'),
        L('gcs_scan_nothingfound_02-', 'Всё в порядке, можешь продолжать движение.'),
        L('gcs_scan_nothingfound_03-', 'Всё хорошо. Ничего запрещенного не обнаружено.'),
        L('gcs_scan_orderdrop_01-', 'Так, так, так... Что тут у нас. А ну давай выбрасывай запрещенный груз. Быстро!', RuleAngry),
        L('gcs_scan_orderdrop_02-', 'Внимание всем, у нас тут неопознанный груз! Фрилансер, выкидывай груз. Это приказ!', RuleAngry),
        L('gcs_scan_orderdrop_03-', 'Я нашел то что искал. Давай выбрасывай груз из трюма. Иначе тебе не поздоровится', RuleAngry),
        L('gcs_scan_refuse_01-', 'Отказ, ты от меня ничего не получишь'),
        L('gcs_scan_refuse_02-', 'Ни за что, ты не имеешь такого права, так что я тебе ничего не выдам'),
        L('gcs_scan_refuse_03-', 'Отказано, я не пойду на сотрудничество'),

        L('rms_bigshiptaunt_01-', 'Ты совсем берега попутал?', RuleAngry),
        L('rms_bigshiptaunt_02-', 'Тебе не понравится то, что сейчас будет', RuleAngry),
        L('rms_bigshiptaunt_03-', 'Не слишком ли ты много на себя взял?', RuleAngry),
        L('rms_defendleader_01-', 'Тебе не достать нашего командира!', RuleAngry),
        L('rms_defendleader_02-', 'Чтобы добраться до моего командира, тебе надо сначала сразиться со мной, ут+ырок', RuleAngry),
        L('rms_defendleader_03-', 'Пока я здесь, ты не достигнешь своей цели, урод', RuleAngry),
        L('rms_defendsolar_01-', 'Наша база тебе не по зубам!', RuleAngry),
        L('rms_defendsolar_02-', 'Тебе не совладать с нашей базой!', RuleAngry),
        L('rms_defendsolar_03-', 'Я с удовольствием отобью твои нат+ужные поп+ытки атаковать нашу базу!', RuleAngry),
        L('rms_friendlyarrival_01-', 'Нужна помощь?'),
        L('rms_friendlyarrival_02-', 'Подкрепление прибыло'),
        L('rms_friendlyarrival_03-', 'Мы тебе поможем'),
        L('rms_friendlyarrival_04-', 'Я думаю, поддержка лишней не будет'),
        L('rms_friendlywelcome_01-', 'Отлично, мы вас заждались!'),
        L('rms_friendlywelcome_02-', 'Вы как раз вовремя!'),
        L('rms_friendlywelcome_03-', 'Мы бы без вас не справились!'),
        L('rms_friendlywelcome_04-', 'Рад вас видеть!'),
        L('rms_shiprunning_01-', 'Даже не пытайся догнать меня', RuleAngry),
        L('rms_shiprunning_02-', 'Я бы советовал тебе не следовать за мной', RuleAngry),
        L('rms_shiprunning_03-', 'Лучше не пытайся преследовать меня', RuleAngry),
        L('rms_smallshiptaunt_01-', 'Друган, ты попал', RuleAngry),
        L('rms_smallshiptaunt_02-', 'Сейчас ты получишь удар правосудием по полной', RuleAngry),
        L('rms_smallshiptaunt_03-', 'Я не собираюсь церемониться с тобой', RuleAngry),
        L('rms_smallshiptaunt_04-', 'Будет больно, не беспокойся', RuleAngry),
        L('rms_targetrunning_01-', 'А ну отвали, ублюдок!', RuleAngry),
        L('rms_targetrunning_02-', 'Иди к ч+ёрту!', RuleAngry),
        L('rms_targetrunning_03-', 'А ну прекрати стрелять, пока можешь!', RuleAngry),
        L('rms_targetrunning_04-', 'Ты сильнее, чем я думал...', RuleAngry),

        # GENERICS
        # L('gcs_refer_base_Br01_01_base-', ),
        # L('gcs_refer_system_Br01-', ),
        # L('gcs_gen_commodity_alienartifacts', ),
        # L('gcs_refer_faction_br_m_short', ),

        L('gcs_refer_base_testbase-', 'Станция Т+эрра', RuleBase),
        L('gcs_refer_system_testsystem-', 'Сист+ема Ом+ега-13', RuleSystem),
        L('gcs_gen_commodity_gold', 'з+олото', RuleCommodity),
        L('gcs_refer_faction_test_short', 'Р+эйнланд', RuleFaction),
        L('gcs_refer_faction_player_short', 'Фрил+ансер', RuleFaction),

        L('mod_refer_base_freeport-', 'точка фрипорт', RuleBase),
        L('mod_refer_base_prison-', 'точка тюрьма', RuleBase),
        L('mod_refer_base_outpost-', 'точка аванпост', RuleBase),
        L('mod_refer_base_battleship-', 'точка линкор', RuleBase),
        L('mod_refer_base_military-', 'точка военная база', RuleBase),
        L('mod_refer_base_research-', 'точка исследовательская станция', RuleBase),
        L('mod_refer_base_shipyard-', 'точка верфь', RuleBase),
        L('mod_refer_base_factory-', 'точка фабрика', RuleBase),
        L('mod_refer_base_station-', 'точка станция', RuleBase),
        L('mod_refer_base_border-', 'точка пограничный аванпост', RuleBase),

    ]

    @classmethod
    def get_id_map(cls):
        map = []
        for line in cls.LINES:
            map.append(
                (
                    line.code.lower(),
                    line.hash
                )
            )
        return map

    def get_number_lines(self):
        lines = []
        for digit, text in NUMBERS:
            lines.append(
                L(
                    code=NUMBER_START_TEMPLATE.format(digit=digit),
                    ru_text=text,
                    parse_rule=RuleNumberFirst
                )
            )
            lines.append(
                L(
                    code=NUMBER_END_TEMPLATE.format(digit=digit),
                    ru_text=text,
                    parse_rule=RuleNumberSecond
                )
            )
        return lines

    def get_formation_lines(self):
        lines = []
        for digit, text in FORMATIONS:
            lines.append(
                L(
                    code=FORMATION_TEMPLATE.format(digit=digit),
                    ru_text=text,
                    parse_rule=RuleFormation
                )
            )
        return lines

    def get_lines(self):
        lines = self.LINES + self.get_number_lines() + self.get_formation_lines()
        return lines

    def get_sounds(self):
        lines = self.get_lines()
        sounds = []
        for line in lines:
            sounds.append(
                SpaceSound(
                    name=line.get_code(),
                    line=line.get_text(),
                )
            )
        return sounds

    def get_voice(self):
        return Voice(
            voice_name=self.FOLDER,
            sounds=self.get_sounds(),
        )


class FirstPilot(ShipVoice):
    STEOS_ID = 215
    FOLDER = 'pilot01'
    STATIC_KIND = 'TYPE1'
