from universe.audio.space_voice import DynamicLine as L


NAME_AT_END = 1

SCREAM_1 = '1'
SCREAM_2 = '2'
SCREAM_3 = '3'
SCREAM_4 = '4'
SCREAM_5 = '5'
SCREAM_6 = '6'
SCREAM_7 = '7'
SCREAM_8 = '8'

SCREAM_TEMPLATE = 'gcs_combat_scream_0{num}-'
FORMATION_TEMPLATE = 'gcs_refer_formationdesig_{num:02d}'
NUMBER_START_TEMPLATE = 'gcs_misc_number_{num}'
NUMBER_END_TEMPLATE = 'gcs_misc_number_{num}-'


class ParseRule:
    pass


class RuleScream(ParseRule):
    pass


class RuleStart(ParseRule):
    pass


# <десять> вейпоинтов
class RuleStartNumber(RuleStart):
    pass


# <что-то делаю> спасибо за помощь
class RuleContinueRequest(RuleStart):
    pass


# <что-то делаю> к стыковке
class RuleDockContinueRequest(RuleStart):
    pass


class RuleEnd(ParseRule):
    END_APPEND = None


# движусь к <станция>
class RuleEndTo(RuleEnd):
    END_APPEND = 'станции'


# мне нужно <что-то сделать>
class RuleEndThing(RuleEnd):
    END_APPEND = 'убивать'


# мне осталось <десять>
class RuleEndNumber(RuleEnd):
    END_APPEND = 'десять'


class RuleSplit(ParseRule):
    pass


class RuleHighAction(ParseRule):
    pass


class RuleNormalAction(ParseRule):
    pass


class RuleNormalActionWithEnd(ParseRule):
    pass


class RuleAngry(ParseRule):
    pass


class RuleDash(ParseRule):
    pass


class RuleFrom(ParseRule):
    pass


class RuleTo(ParseRule):
    pass


class RuleThisIs(ParseRule):
    pass


FORMATIONS = [
    (1, 'альфа'),
    (2, 'бета'),
    (3, 'гамма'),
    (4, 'дельта'),
    (5, 'эпсилон'),
    (6, 'зета'),
    (7, 'тета'),
    (8, 'йота'),
    (9, 'каппа'),
    (10, 'лямбда'),
    (11, 'омикрон'),
    (12, 'сигма'),
    (13, 'омега'),
    (14, 'красный'),
    (15, 'синий'),
    (16, 'золотой'),
    (17, 'зеленый'),
    (18, 'серебрянный'),
    (19, 'черный'),
    (20, 'белый'),
    (21, 'желтый'),
    (22, 'матсу'),
    (23, 'сакура'),
    (24, 'фудзи'),
    (25, 'ботан'),
    (26, 'хаги'),
    (27, 'сузуки'),
    (28, 'кику'),
    (29, 'янаги'),
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
    (11, 'одинадцать'),
    (12, 'двенадцать'),
    (13, 'тринадцать'),
    (14, 'четырнадцать'),
    (15, 'пятнадцать'),
    (16, 'шестнадцать'),
    (17, 'семнадцать'),
    (18, 'восемнадцать'),
    (19, 'девятнадцать'),
    (20, 'двадцать'),
]


class ShipVoice(object):
    LINES = [
        L('gcs_combat_announce_allclear_01-', 'Противников не обнаружено.'),
        L('gcs_combat_announce_allclear_02-', 'На сканерах больше нет неприятелей.'),
        L('gcs_combat_announce_allclear_03-', 'Зона зачищена.'),
        L('gcs_combat_announce_allclear_04-', 'Врагов не видно.'),
        L('gcs_combat_announce_allclear_05-', 'Зона в зеленом статусе. Врагов не обнаружено.'),
        L('gcs_combat_announce_allclear_06-', 'Зона чиста. Враждебные контакты отсутствуют.'),
        # L('gcs_combat_announce_combatdrift_01-', ),
        # L('gcs_combat_announce_combatdrift_02-', ),
        # L('gcs_combat_announce_combatdrift_03-', ),
        L('gcs_combat_announce_enemysighted_01-', 'Вижу нового неприятеля.'),
        L('gcs_combat_announce_enemysighted_02-', 'На радаре новый противник.'),
        L('gcs_combat_announce_enemysighted_03-', 'Замечена новая угроза. Неприятель.'),
        L('gcs_combat_announce_enemysighted_04-', 'На сканере замечены неприятели!'),
        L('gcs_combat_announce_ff_01-', 'Смотри куда стреляешь!'),
        L('gcs_combat_announce_ff_02-', 'Прекрати стрелять, фрилансер!'),
        L('gcs_combat_announce_ff_03-', 'Хватит стрелять по мне!'),
        L('gcs_combat_announce_flee_01-', 'Уходим!'),
        L('gcs_combat_announce_flee_02-', 'Я улетаю!'),
        L('gcs_combat_announce_flee_03-', 'К чёрту всё, я улетаю отсюда.'),
        L('gcs_combat_announce_flee_04-', 'Я отступаю.'),
        L('gcs_combat_announce_flee_05-', 'Мне нужна прегрупировка.'),
        L('gcs_combat_announce_flee_06-', 'Я сваливаю отсюда.'),
        L('gcs_combat_askengage_01-', 'Разрешите атаковать.'),
        L('gcs_combat_askengage_02-', 'Запрашиваю открыть огонь.'),
        L('gcs_combat_askengage_03-', 'Ожидаю приказа на перехват.'),
        L('gcs_combat_askengage_04-', 'Запрашиваю разрешение открыть огонь!'),
        L('gcs_combat_askforhelp_01-', 'Мне нужна поддержка!'),
        L('gcs_combat_askforhelp_02-', 'Запращиваю поддержку!'),
        L('gcs_combat_askforhelp_03-', 'Прикройте меня!'),
        L('gcs_combat_askforhelp_04-', 'Нужна поддержка!'),
        L('gcs_combat_askforhelp_05-', 'Запрашиваю дополнительную поддержку!'),
        L('gcs_combat_brag_01-', 'Неприятель уничтожен.'),
        L('gcs_combat_brag_02-', 'Враг уничтожен.'),
        L('gcs_combat_brag_03-', 'Вражеская цель ликвидирована.'),
        L('gcs_combat_brag_04-', 'Неприятель ликвидирован.'),
        L('gcs_combat_brag_05-', 'Враг нейтрализован.'),
        L('gcs_combat_brag_06-', 'Неприятель был нейтрализован.'),
        L('gcs_combat_comingin_p_01-', 'Мы на пути к тебе.'),
        L('gcs_combat_comingin_p_02-', 'Подожди, скоро будем тут.'),
        L('gcs_combat_comingin_p_03-', 'Жди, летим к тебе.'),
        L('gcs_combat_comingin_s_01-', 'Я скоро буду здесь.'),
        L('gcs_combat_comingin_s_02-', 'Я в пути.'),
        L('gcs_combat_comingin_s_03-', 'Жди, я лечу к тебе.'),
        L('gcs_combat_deathsympathy_01-', 'Нашего сбили!'),
        L('gcs_combat_deathsympathy_02-', 'Я потерял ведомого!'),
        L('gcs_combat_deathsympathy_03-', 'Член крыла убит!'),
        L('gcs_combat_deathsympathy_04-', 'Моего сбили!'),
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
        L('gcs_combat_fleereason_other_01-', 'Дела плохи, в+алим', RuleHighAction),
        L('gcs_combat_fleereason_other_02-', 'Пора сваливать, тут делать нечего', RuleHighAction),
        L('gcs_combat_fleereason_other_03-', 'Наше положение ужасное', RuleHighAction),
        L('gcs_combat_fleereason_tough_01-', 'Ситуация ужасная', RuleHighAction),
        L('gcs_combat_fleereason_tough_02-', 'Всё очень плохо, сражаться бессмысленно', RuleHighAction),
        L('gcs_combat_fleereason_tough_03-', 'Не вижу смысла продолжать сражение', RuleHighAction),
        L('gcs_combat_hasinsights_01-', 'Контакт в радиусе видимости', RuleNormalAction),
        L('gcs_combat_hasinsights_02-', 'Наблюдаю противника', RuleNormalAction),
        L('gcs_combat_hasinsights_03-', 'Визуальный контакт. Готовлюсь к атаке', RuleNormalAction),
        L('gcs_combat_hasinsights_04-', 'Рядом враг', RuleNormalAction),
        L('gcs_combat_hasinsights_05-', 'Противник недалеко от меня', RuleNormalAction),
        L('gcs_combat_hasinsights_06-', 'Направлюсь к вражеской цели', RuleNormalAction),
        L('gcs_combat_inflicting_damage_01-', 'Враг на мушке', RuleHighAction),
        L('gcs_combat_inflicting_damage_02-', 'Противник повреждён!', RuleHighAction),
        L('gcs_combat_inflicting_damage_03-', 'Противник терпит повреждения!', RuleHighAction),
        L('gcs_combat_inflicting_damage_04-', 'Наношу повреждения противнику!', RuleHighAction),
        L('gcs_combat_inflicting_damage_05-', 'Попал по нему!', RuleHighAction),
        L('gcs_combat_inflicting_damage_06-', 'Враг под моим огнём!', RuleHighAction),
        L('gcs_combat_inflicting_damage_worst_01-', 'Враг почти уничтожен', RuleHighAction),
        L('gcs_combat_inflicting_damage_worst_02-', 'Цель горит!', RuleHighAction),
        L('gcs_combat_inflicting_damage_worst_03-', 'Враг больше не выдержит', RuleHighAction),
        L('gcs_combat_inflicting_damage_worst_04-', 'Почти убил его', RuleHighAction),
        L('gcs_combat_inflicting_damage_worst_05-', 'Противник почти убит', RuleHighAction),
        L('gcs_combat_inflicting_damage_worst_06-', 'Цель почти уничтожена', RuleHighAction),
        L('gcs_combat_insights_01-', 'Преследую врага', RuleHighAction),
        L('gcs_combat_insights_02-', 'Враг на прицеле', RuleHighAction),
        L('gcs_combat_insights_03-', 'Вражеская цель захвачена', RuleHighAction),
        L('gcs_combat_insights_04-', 'Иду за врагом', RuleHighAction),
        L('gcs_combat_insights_05-', 'Взял цель', RuleHighAction),
        L('gcs_combat_insights_06-', 'Преследую его', RuleHighAction),
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
        L('gcs_combat_takinglead_01-', 'Я беру контроль на себя'),
        L('gcs_combat_takinglead_02-', 'Теперь я ведомый'),
        L('gcs_combat_takinglead_03-', 'Беру командование на себя'),
        L('gcs_combat_takinglead_04-', 'Я ведомый звена'),
        L('gcs_dhail_angry_response_01-', 'А ну отвали, тебе тут нечего смотреть!', RuleAngry),
        L('gcs_dockhail_hailee_datasubmit_01-', 'Высылаю данные'),
        L('gcs_dockhail_hailee_datasubmit_02-', 'Начинаю отсылать данные'),
        L('gcs_dockrequest_goingto_01+', 'Мы движемся к', RuleEndTo),
        L('gcs_dockrequest_jumpgatedelayed_01-', 'Мы не единственные, кто движется к', RuleEndTo),
        L('gcs_dockrequest_jumpgateopen_01-', 'Ребята, доступ открыт, движемся к', RuleEndTo),
        L('gcs_dockrequest_jumpgateopenafterdelay_01-','Доступ получен, теперь наш черёд'),
        L('gcs_dockrequest_request_01+', 'Мне нужно', RuleEndThing),
        L('gcs_dockrequest_request_02+', 'Я запрашиваю', RuleEndThing),
        L('gcs_dockrequest_thankshelp_01-', 'спасибо за помощь', RuleContinueRequest),
        L('gcs_dockrequest_thisourstop_01-', 'Так, тут наша остановка'),
        L('gcs_dockrequest_todock-', 'стыковку', RuleDockContinueRequest),
        L('gcs_dockrequest_toland-', 'посадку', RuleDockContinueRequest),
        L('gcs_dockrequest_tomoor-', 'швартовку', RuleDockContinueRequest),
        L('gcs_dockrequest_tradelanestart_01-', 'Запускаю торговую линию'),
        # L('gcs_fidget_patrol_wpremainquery_01-', 'Как много точек пути нам нужно пролететь?'),
        # L('gcs_fidget_patrolrumor_01-', 'А ты слышал про артефакты в Омикрон Тете?'),
        # L('gcs_fidget_patrolsimple_01-', ''),
        L('gcs_fidget_saystatus_damagelarge_01-', 'Повреждения корабля значительны, не знаю как я долечу до базы'),
        L('gcs_fidget_saystatus_damagemedium_01-', 'Корабль заметно повреждён, но функционирует'),
        L('gcs_fidget_saystatus_damagenone_01-', 'Статус корабля: все системы работают штатно'),
        L('gcs_fidget_saystatus_damagesmall_01-', 'Меня потрепало, но в целом всё в порядке'),
        # L('gcs_fidget_talkcargo_01-', ),
        # L('gcs_fidget_trade_ihear_01+', ),
        # L('gcs_fidget_trade_simple_01-', ),
        # L('gcs_fidget_trade_simple_02-', ),
        # L('gcs_fidget_trade_simple_03-', ),
        # L('gcs_fidget_traderumor_01-', ),
        # L('gcs_fidget_whatstatus_01-', ''),


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
        L('gcs_patrol_morewptogo-', 'точка пути', RuleStartNumber),
        L('gcs_patrol_wehave+', 'Нам осталось', RuleEndNumber),
        L('gcs_patrol_wehaveonly+', 'Нам осталась', RuleEndNumber),
        L('gcs_phail_blowoff_01-', 'Нужно что-то еще?'),
        L('gcs_phail_blowoff_02-', 'Я уже тебе всё рассказал'),
        L('gcs_phail_combatblowoff_01-', 'Хватит меня отвлекать, я в бою!', RuleHighAction),


        L('gcs_misc_dash', 'дэш', RuleDash),
        L('gcs_misc_from', 'из', RuleFrom),
        L('gcs_misc_to', 'в', RuleTo),
        L('gcs_misc_thisis+', 'это', RuleThisIs),

        # L('gcs_scan_angry_01-', ),
        # L('gcs_scan_angry_02-', ),
        # L('gcs_scan_angry_03-', ),
        # L('gcs_scan_announce_01-', ),
        # L('gcs_scan_announce_02-', ),
        # L('gcs_scan_announce_03-', ),
        # L('gcs_scan_comply_01-', ),
        # L('gcs_scan_comply_02-', ),
        # L('gcs_scan_comply_03-', ),
        # L('gcs_scan_happy_01-', ),
        # L('gcs_scan_happy_02-', ),
        # L('gcs_scan_happy_03-', ),
        # L('gcs_scan_lootdestroyed_01-', ),
        # L('gcs_scan_lootdestroyed_02-', ),
        # L('gcs_scan_lootdestroyed_03-', ),
        # L('gcs_scan_nothingfound_01-', ),
        # L('gcs_scan_nothingfound_02-', ),
        # L('gcs_scan_nothingfound_03-', ),
        # L('gcs_scan_orderdrop_01-', ),
        # L('gcs_scan_orderdrop_02-', ),
        # L('gcs_scan_orderdrop_03-', ),
        # L('gcs_scan_refuse_01-', ),
        # L('gcs_scan_refuse_02-', ),
        # L('gcs_scan_refuse_03-', ),
        # L('gcs_trade_carrying_p_01+', ),
        # L('gcs_trade_carrying_s_01+', ),
        # L('gcs_trade_idhome_p_01+', ),
        # L('gcs_trade_idhome_p_02+', ),
        # L('gcs_trade_idhome_s_01+', ),
        # L('gcs_trade_idhome_s_02+', ),
        # L('gcs_trade_wanttoget_p_01+', ),
        # L('gcs_trade_wanttoget_s_01+', ),
        # L('rms_bigshiptaunt_01-', ),
        # L('rms_bigshiptaunt_02-', ),
        # L('rms_bigshiptaunt_03-', ),
        # L('rms_defendleader_01-', ),
        # L('rms_defendleader_02-', ),
        # L('rms_defendleader_03-', ),
        # L('rms_defendsolar_01-', ),
        # L('rms_defendsolar_02-', ),
        # L('rms_defendsolar_03-', ),
        # L('rms_friendlyarrival_01-', ),
        # L('rms_friendlyarrival_02-', ),
        # L('rms_friendlyarrival_03-', ),
        # L('rms_friendlyarrival_04-', ),
        # L('rms_friendlywelcome_01-', ),
        # L('rms_friendlywelcome_02-', ),
        # L('rms_friendlywelcome_03-', ),
        # L('rms_friendlywelcome_04-', ),
        # L('rms_shiprunning_01-', ),
        # L('rms_shiprunning_02-', ),
        # L('rms_shiprunning_03-', ),
        # L('rms_smallshiptaunt_01-', ),
        # L('rms_smallshiptaunt_02-', ),
        # L('rms_smallshiptaunt_03-', ),
        # L('rms_smallshiptaunt_04-', ),
        # L('rms_targetrunning_01-', ),
        # L('rms_targetrunning_02-', ),
        # L('rms_targetrunning_03-', ),
        # L('rms_targetrunning_04-', ),

        # GENERICS
        # L('gcs_refer_base_Br01_01_base-', ),
        # L('gcs_refer_system_Br01-', ),
        # L('gcs_gen_commodity_alienartifacts', ),
        # L('gcs_refer_faction_br_m_short', ),
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

