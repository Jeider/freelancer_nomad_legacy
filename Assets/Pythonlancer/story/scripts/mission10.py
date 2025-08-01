from story import script
from audio.sound import VoiceLine
from story.actors import Trent, Darcy, Hassler, HasslerOrder, EdisonTrent, Alaric, Juni, Tor
from story.cutscenes.story_scenes import m10_rescued


class Msn10(object):
    MISSION_INDEX = 10


class Msn10OfferCutscene(Msn10, script.CutsceneProps):
    ALIAS = 'offer'
    TITLE = 'Бар линкора Мусаси'
    DESCRIPTION = 'Трент и Дерси встречаются в баре по предложению Хасслера'
    VOICE_LINES = [
        VoiceLine(
            10,
            HasslerOrder,
            ru='Герр Трент, фрау Д+ерси'
        ),
        VoiceLine(
            20,
            Darcy,
            ru='Фр+ойляйн.'
        ),
        VoiceLine(
            30,
            HasslerOrder,
            ru='Прост+ите?'
        ),
        VoiceLine(
            40,
            Darcy,
            ru='Фр+ойляйн Д+ерси.'
        ),
        VoiceLine(
            50,
            Trent,
            ru='(Возмущенно) Прошу меня извинить, но мы кажется собрались не лингвистические вопросы разбирать.'
        ),
        VoiceLine(
            60,
            HasslerOrder,
            ru='Йа! Точно так. К делу! Наши недавние... хмммм... манёвры, а так же резкая активизация вооруженных сил Р+ейнланда изменили '
               'общую ситуацию не лучшим образом.'
        ),
        VoiceLine(
            70,
            Trent,
            ru='(Дикий сарказм) Кто бы мог подумать, что локальная война с СБА в отдельно взятой системе изменит ситуацию не лучшим образом?'
        ),
        VoiceLine(
            80,
            HasslerOrder,
            ru='Это было необходимо,, герр Трент... А сейчас мы должн+ы реагировать на изменившуюся ситуацию.'
        ),
        VoiceLine(
            90,
            Trent,
            ru='Кого убить на этот раз?'
        ),
        VoiceLine(
            100,
            HasslerOrder,
            ru='Нет,, герр Трент, совсем наоборот. Нужно будет вытащить из тюрьм+ы кс+еносов одного хор+ошего человека, героя войн+ы с кочевниками.'
        ),
        VoiceLine(
            110,
            Trent,
            ru='Войн+ы с кочевниками официально ведь н+е б+ыло.'
        ),
        VoiceLine(
            120,
            HasslerOrder,
            ru='Это не отменяет того,, что были её герои.'
        ),
        VoiceLine(
            130,
            Trent,
            ru='Пусть так, но при чём тут я?'
        ),
        VoiceLine(
            140,
            HasslerOrder,
            ru='Вы не первый, кто пытался освободить интересующего нас человека. Первым был ваш друг Аларик.'
        ),
        VoiceLine(
            150,
            Trent,
            ru='(Подытожив) И Аларик облажался...'
        ),
        VoiceLine(
            160,
            HasslerOrder,
            ru='Весьма прискорбно, но так и есть. Теперь он содержится в той же тюрьме.'
        ),
        VoiceLine(
            170,
            Trent,
            ru='И вы хотите, чтобы я повторил его подвиг, и нас в тюрьме стало уже трое? И Аларику не скучно, и преферансик на троих можно будет раскинуть.'
        ),
        VoiceLine(
            180,
            HasslerOrder,
            ru='При всём моем уважении к герру Аларику, его способности значительно уступают вашим.'
        ),
        VoiceLine(
            190,
            Trent,
            ru='Хорошо... Если вы так считаете,, герр Хасслер. (тихо, в сторону) Эх как же я задолбался... И канистры-то нет...'
        ),
        # место для принятия миссии
        VoiceLine(
            200,
            Trent,
            ru='(Выдохнув) Ладно, каков план?'
        ),
        VoiceLine(
            210,
            HasslerOrder,
            ru='Тюрьма находится в Омега-ирсутае. Система представляет собой по большей части пылевое облако. '
                'Мус+аси переместится на окраину системы таким образом,, чтобы не привлечь внимание аборигенов.'
        ),
        VoiceLine(
            220,
            HasslerOrder,
            ru='Герр Трент, вы с фр+ойляйн Д+ерси возглавите диверсионное звено. '
               'Ваши корабли получат дополнительную мимикрирующую обработку, чтобы вы могли пробраться к тюрьме незаметно.'
        ),
        VoiceLine(
            230,
            HasslerOrder,
            ru='Вы должн+ы б+удете подавить защитные системы тюрьм+ы. '
               'Следом в дело вступает наш транспорт с десантниками и звено прикрытия.'
        ),
        VoiceLine(
            240,
            HasslerOrder,
            ru='После того,, как десант сделает свое дело, все весело и с фейерверками прорываются обратно на Мус+аси.'
        ),
        VoiceLine(
            250,
            Trent,
            ru='Звучит заманчиво.'
        ),
        VoiceLine(
            260,
            Darcy,
            ru='Посмотрим, как окажется на самом деле.'
        ),
        VoiceLine(
            270,
            HasslerOrder,
            ru='Тогда можете готовиться к вылету. Я буду координировать операцию с мостика линкора.'
        ),
    ]


class Msn10Space(Msn10, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(
            10,
            Darcy,
            comment='Взлёт после принятия миссии',
            ru='Эй, Хасслер, чего там твои инженеры шаманили над нашими кораблями?'
        ),
        VoiceLine(
            20,
            HasslerOrder,
            ru='Устанавливали мимикрирующие панели, фр+ойляйн Д+ерси.'
        ),
        VoiceLine(
            30,
            HasslerOrder,
            ru='Эти панели снизят вашу заметность на радарах в разы. В зависимости от характера окружающего пространства от двух до семи раз.'
        ),
        VoiceLine(
            40,
            HasslerOrder,
            ru='Кроме того они подстраиваются под характер окружающего пространства визуально. В плотном пылевом облаке если вы не двигаетесь вас можно будет обнаружить только радаром и только вплотную.'
        ),
        VoiceLine(
            50,
            Trent,
            ru='Будем изображать из себя ниндзя?'
        ),
        VoiceLine(
            60,
            HasslerOrder,
            ru='Придется. Кс+еносы очень не любят чужаков. А чужаков, которые приближаются к их тюрьме с намерением выкрасть парочку заключенных, они не любят особенно сильно.'
        ),

        VoiceLine(70, HasslerOrder, ru='Трент, ты ведешь звено Локи. Уничтожьте защитные системы и дайте нам сигнал '
                                        'в случае успеха. Карта местности загружена в компьютер Д+ерси.'),
        VoiceLine(80, Darcy, ru='Да, я буду помогать. Трент, лети вперед! Мы полетим за тобой'),

        VoiceLine(110, Trent, ru='Панели работают, даже устройство невидимости не нужно.'),

        VoiceLine(200, Trent, ru='Я прошел. Что дальше?'),
        VoiceLine(210, Darcy, ru='Мы еще летим. А ты пока отключи местную систему безопасности.'),
        VoiceLine(220, Darcy,
                  ru='Я только что передала тебе координаты управляющего аванпоста. '
                     'Только давай осторожно, тут много мин'),

        VoiceLine(300, Trent, ru='Я у аванпоста, он закрыт'),
        VoiceLine(320, Darcy, ru='Трент, ты что как маленький. Там есть дверь. Ты уже умеешь такие взрывать'),

        VoiceLine(350, Darcy,
                  ru='Давно практиковал хакерские навыки? Определи нужный цвет, стреляя одиночным огнём по цветным блокам'),

        VoiceLine(360, Darcy,
                  ru='Твоя нейрос+еть укажет насколько этот цвет близок к нужному. Искомый цвет будет назван "максимальным"'),
        VoiceLine(370, Darcy, ru='Найди такой цвет и уничтожь все подобные блоки'),

        VoiceLine(390, Trent, ru='Ладно, будем вспоминать как это делается.'),

        VoiceLine(400, Trent, ru='Система взломана.'),
        VoiceLine(410, Darcy, ru='Есть! Давай летим к нашему звену. Мы уже готовы к атаке'),
        VoiceLine(420, Trent, ru='А чего тут за система защиты, что её надо прям ломать'),
        VoiceLine(430, Darcy, ru='Тяжелые турели, которые защищают проход без мин. Он самый простой и безопасный. Конечно когда турели в+ыключены'),

        VoiceLine(450, Darcy,
                  ru='Давай Трент, командуй парадом. Резко подлетаем к базе и разносим орудийные платформы вокруг неё'),

        VoiceLine(470, Darcy,
                  ru='Огонь по орудийным платформам, пока Кс+еносы не вызвали подкрепление!'),
        VoiceLine(490, Darcy, ru='Платформа сбита'),
        VoiceLine(500, Darcy, ru='Еще три штуки!'),
        VoiceLine(510, Darcy, ru='Осталось две платформы!'),
        VoiceLine(520, Darcy, ru='Осталась последняя!'),
        VoiceLine(530, Darcy, ru='Тор, платформы сбиты. Выдвигайтесь к нам!'),

        VoiceLine(550, Tor, ru='Тор с эскортом в пути. Обеспечьте нашу безопасность'),

        VoiceLine(570, HasslerOrder, ru='+Один и Тор на месте. Трент, Л+оки, обеспечьте прикрытие транспорту.'),
        VoiceLine(580, Darcy, ru='Тор сел! Трент, надо раскидать Кс+еносов, чтобы Тор смог безопасно покинуть базу!'),

        VoiceLine(600, Tor, ru='Тор на связи, груз упакован.'),
        VoiceLine(620, Darcy, ru='Отлично! Продолжаем давить истребители кс+еносов!'),

        VoiceLine(650, HasslerOrder, ru='Тор покинул зону битвы. Трент, Д+ерси, Л+оки, выход+ите из зоны сражения'),
        VoiceLine(670, Darcy, ru='Так точно Хасслер! Трент, летим по указанной точке пути'),

        VoiceLine(700, Darcy, ru='Миссия выполнена! Все сад+имся на Мус+аси. Трент, садись первым'),
    ]


class Msn10RescuedCutscene(Msn10, script.CutsceneProps):
    ALIAS = 'rescued'
    TITLE = 'Ангар линкора Мусаси'
    THORN_CLASS = m10_rescued.Msn10RescuedCutsceneThorn
    THORN_DECISION_CLASS = m10_rescued.Msn10RescuedDecisionThorn
    THORN_ACCEPT_CLASS = m10_rescued.Msn10RescuedAcceptThorn
    DESCRIPTION = 'Поздравления со спасением'
    VOICE_LINES = [
        VoiceLine(
            10,
            Alaric,
            ru='Как я рад тебя видеть,, дружище!!! Ты нас спас. А я уже думал сдохну в этой дыре'
        ),
        VoiceLine(
            20,
            Trent,
            ru='(Подкалываем по доброму) Никто больше не соглашался вытаскивать твою задницу из лап сектантов, вот и пришлось мне... Хотя, я уже подумывал оставить тебя там, в назидание.'
        ),
        VoiceLine(
            30,
            Alaric,
            ru='Дружище, я там с одним хорошим человеком познакомился. Ты сейчас охренеешь. Итак... Мистер Трент, познакомьтесь, мистер Трент.'
        ),
        VoiceLine(
            40,
            Trent,
            ru='(Обалдевание) Очень приятно. Не каждый день получается вот так запросто поболтать с легендой.'
        ),
        VoiceLine(
            50,
            EdisonTrent,
            ru='Вытащить легенду из передряги, в которой ей угораздило утонуть с головой по собственной глупости, вы хотели сказать. Предрекаю вам блестящее будущее.'
        ),
        VoiceLine(
            60,
            Trent,
            ru='Неужели в правительство пробьюсь?'
        ),
        VoiceLine(
            70,
            EdisonTrent,
            ru='Не смешите меня, ком+у нужны эти правительства?'
        ),
        VoiceLine(
            80,
            HasslerOrder,
            ru='Герр Трент, фрау Зейн передаёт, что лорду Ямамото срочно нужна ваша помощь!'
        ),
        VoiceLine(
            90,
            EdisonTrent,
            ru='Если фрау Зейн, то это меня. Рад знакомству, мистер Трент!'
        ),
        VoiceLine(
            100,
            HasslerOrder,
            comment='Старый Трент уходит',
            ru='Герр Трент, лейтенант Ким обнаружил Р+окфорда.'
        ),
        VoiceLine(
            110,
            Trent,
            ru='А если лейтенант Ким - то это,, видимо меня.'
        ),
        VoiceLine(
            120,
            Darcy,
            ru='В последнее время немудрено запутаться в этих Трентах.'
        ),
        VoiceLine(
            130,
            Trent,
            ru='И где же Р+окфорд?'
        ),
        VoiceLine(
            140,
            HasslerOrder,
            ru='На станции Харадзюку, система Омега 7. Мы планируем подорвать корабль герра Р+окфорда, но для осуществления миссии нам необходимо чтобы вы отвлекли его на себя.'
        ),
        VoiceLine(
            150,
            Trent,
            ru='Хасслер, а ты всех "геррами" называешь? Даже таких засранцев,, как Р+окфорд.'
        ),
        VoiceLine(
            160,
            HasslerOrder,
            ru='К сожалению... Чертово воспитание дает о себе знать.'
        ),
        VoiceLine(
            170,
            Trent,
            ru='Хорошо, я в деле'
        ),
    ]


class Msn10FinalCutscene(Msn10, script.CutsceneProps):
    ALIAS = 'final'
    TITLE = 'Бар линкора Мусаси'
    DESCRIPTION = 'Трент подошел к Аларику обсудить планы на будущее'
    VOICE_LINES = [
        VoiceLine(
            10,
            Trent,
            ru='Ну ка+к т+ы, узник замка Иф, невольник чести?'
        ),
        VoiceLine(
            20,
            Alaric,
            ru='Теперь - отлично. А там... Я уже с жизнью прощался.'
        ),
        VoiceLine(
            30,
            Trent,
            ru='А нахрена полез-то во всё это'
        ),
        VoiceLine(
            40,
            Alaric,
            ru='А как еще? У тебя есть крутой друг, который на одном месте вертел спецслужбы сразу нескольких государств, '
               'жёг врагов пачками и всегда выходил сухим из воды.'
        ),
        VoiceLine(
            50,
            Alaric,
            ru='Надо же как-то соответствовать... Вот я и решил... Когда ко мне обратились... Тоже поиграть в спецагентов.'
        ),
        VoiceLine(
            60,
            Trent,
            ru='Балбес ты, Аларик... Слушай, достало меня все это. Может сольёмся отсюда по-тихому?'
        ),
        VoiceLine(
            70,
            Alaric,
            ru='Это как?'
        ),
        VoiceLine(
            80,
            Trent,
            ru='Это мы садимся в свои корабли и уходим молча, по-английски. '
               'Не думаю, что нас начнут расстреливать сразу после отстыковки.'
        ),
        VoiceLine(
            90,
            Trent,
            ru='А там - рванем в приграничье, будем выполнять обычные заказы за толику малую. А то меня от этой политики уже тошнит. '
               'Я уже запутался кто против кого, и за кого сейчас я!'
        ),
        VoiceLine(
            100,
            Alaric,
            ru='Да поздно уже когти рвать-то. Улетишь ты в приграничье, '
               'а за тобой через недельку какой-нибудь Хасслер вылетит, и вежливо так прикончит. '
        ),
        VoiceLine(
            105,
            Alaric,
            ru='Слишком уж мы с тобой в этом увязли, дружище, слишком много знаем.'
        ),
        VoiceLine(
            110,
            Trent,
            ru='Да... И главная причина - ужасно досмотреть хочется, чем все закончится.'
        ),
        VoiceLine(
            120,
            Alaric,
            ru='Ага...'
        ),
        VoiceLine(
            130,
            Trent,
            ru='Да ладно, не смотри ты так, никуда я не смоюсь, ты же без меня опять во что-нибудь вляпаешься... '
        ),
        VoiceLine(
            140,
            Trent,
            ru='Досмотрим этот боевичек до конца. (в сторону) Пока еще не ясно, до чьего конца!'
        ),
    ]


class Mission10(Msn10, script.StoryMission):
    CUTSCENES = [
        Msn10OfferCutscene,
        Msn10RescuedCutscene,
        Msn10FinalCutscene,
    ]
    SPACE_CLASS = Msn10Space
    SYNC_SPACE = True

    MISSION_TITLE = 'Миссия 10. Вызволение заключенных'



