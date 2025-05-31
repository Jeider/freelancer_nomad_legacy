from story import script
from audio.sound import VoiceLine
from story.actors import (
    Trent, Wilham, WilhamStation, Hassler, Reichman, Marauder, Punisher, Dietrich, Neuralnet
)


class Msn3(object):
    MISSION_INDEX = 3


class Msn3Space(Msn3, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(
            0,
            WilhamStation,
            ru="Герр Трент, нам опять понадобились ваши услуги. Все подробности на станции Штарке, система Сигма-8. Вильгельм.",
            en="Herr Trent, we need your services again. We'll discuss the details on Starke station in the Sigma-8 system. Wilhelm",
        ),
        VoiceLine(
            1010,
            Hassler,
            ru="Направляемся к пункту сбора. Координаты уже в вашем бортовом компьютере, герр Трент.  ",
            en="We're heading to the rendezvous point. The coordinates are already on your HUD, Herr Trent.",
        ),
        VoiceLine(
            1020,
            Wilham,
            ru="Я доложил Адмирал Райхманну, что мы уже в пути. Он начинает брифинг миссии.",
            en="I've informed Admiral Reichmann that we're on the way. He'll begin the mission's briefing.",
        ),
        VoiceLine(
            1030,
            Hassler,
            ru="Ретранслируй брифинг в общий канал. Герр Трент, слушайте внимательно. ",
            en="I'm relaying the briefing to a common channel. Herr Trent, listen carefully.",
        ),
        VoiceLine(
            1040,
            Wilham,
            ru="Сейчас… (нажимает на кнопочку) готово, слушайте.",
            en="Now… (presses a button) ready, listen. ",
        ),
        VoiceLine(
            20,
            Reichman,
            ru="Напоминаю всем диспозицию. Основное средство защиты станции - энергетический щит, разделенный на две полусферы.",
            en="I'll recap the situation. The station's main mean of defense is its energy shield, divided into two hemispheres. ",
        ),
        VoiceLine(
            30,
            Reichman,
            ru="Щит способен долгое время выдерживать прямые попадания главного калибра наших линкоров. Недостаток щита - долгое время зарядки.",
            en="The shield is able to withstand too many direct hits from our battleships' weapons. Its weakness is a prolonged charge period.",
        ),
        VoiceLine(
            35,
            Reichman,
            ru="После зарядки времени его работы хватит чтобы наш ударный флот был рассеян.",
            en="After it's fully charged, it gives them enough time to completely obliterate our fleet. ",
        ),
        VoiceLine(
            40,
            Reichman,
            ru="Для нейтрализации щита были сформированы две мобильные боевые группы под командованием Хасслера и Греве. Одна из них займется уничтожением генераторов верхней полусферы щита, вторая – нижней.",
            en="To neutralize the shield, two mobile strike teams were formed under the command of Hassler and Greave. One will destroy the generators of the upper hemisphere, and the other – the lower.  ",
        ),
        VoiceLine(
            50,
            Reichman,
            ru="Эти группы должны будут выдвинуться к месту назначения через аномалию, которая будет активирована с корабля герра Хасслера. Вот в общем и все. Начинаем!",
            en="These teams will have to advance to their destination through an anomaly that will be activated by Herr Hassler's ship. That'll be all. Let's go!",
        ),
        VoiceLine(
            1050,
            Hassler,
            ru="Всё поняли, ребята? Выдвигаемся.",
            en="Everything clear, people? Moving in.  ",
        ),
        VoiceLine(
            1060,
            Marauder,
            ru="Аномалия прямо по курсу. Судя по сканерам, она еще активна.",
            en="Anomaly up ahead. Judging by the scanners, it's still active. ",
        ),
        VoiceLine(
            1070,
            Hassler,
            ru="Принял, начинаю подготовку устройства.",
            en="Roger, start preparing the device.",
        ),
        VoiceLine(
            60,
            Hassler,
            ru="Каратели, говорит Каратель-1, активирую аномалию.",
            en="Punishers, this is Punisher-1; activating the anomaly.",
        ),
        VoiceLine(
            65,
            Hassler,
            ru="Входим.",
            en="Get in.",
        ),
        VoiceLine(
            70,
            Hassler,
            ru="Внимание! Вижу корабли корсаров! Боевое построение!",
            en="Attention! I'm reading Corsair ships! Enter battle formation!",
        ),
        VoiceLine(
            1100,
            Marauder,
            ru="Сектор чист.",
            en="Sector clear. ",
        ),
        VoiceLine(
            1110,
            Hassler,
            ru="Направляемся к станции.",
            en="Heading to the station. ",
        ),
        VoiceLine(
            80,
            Hassler,
            ru="Генераторы станции начали зарядку щита! Задача - уничтожить генераторы до полной зарядки! Повторяю - основная цель - генераторы!",
            en="The station's generators started charging the shields! Ourtask–destroy the generators before they're fully charged! I repeat–our main goal is the generators!",
        ),
        VoiceLine(
            1130,
            Marauder,
            ru="Так точно, Каратель-1.",
            en="Roger that, Punisher-1.",
        ),
        VoiceLine(
            90,
            Hassler,
            ru="Генераторы верхней полусферы уничтожены!",
            en="The upper hemisphere's generators are down!",
        ),
        VoiceLine(
            100,
            Hassler,
            ru="Мародер-1, говорит Каратель-1, уходите под наше прикрытие!!! Повторяю, уходите под прикрытие звена Карателей!",
            en="Marauder-1, this is Punisher-1, we'll cover your fire!!!I repeat, the Punisher wing is covering your fire!",
        ),
        VoiceLine(
            110,
            Marauder,
            ru="Не можем уничтожить генераторы! Противодействие против...",
            en="We can't destroy the generators! We're up against... chhhhhhhh",
        ),
        VoiceLine(
            120,
            Hassler,
            ru="Башня, говорит Каратель-1, звено Мародер полностью уничтожено. Приступаем к уничтожению генераторов нижней полусферы.",
            en="Tower, this is Punisher-1, the entire Marauder wing is down. We're proceeding to destroy the lower hemisphere's generators.",
        ),
        VoiceLine(
            130,
            Reichman,
            ru="Понял вас, Каратель-1.",
            en="Roger that, Punisher-1.",
        ),
        VoiceLine(
            140,
            Dietrich,
            ru="Каратель, Мародер, какие красочные позывные! Как жаль что придется вас уничтожить. Мародер уже готов, Каратель - на очереди.",
            en="Punisher, Marauder, such fancy call signs! Such a shame I'll have to destroy you. Marauder is done. Punisher – it's your turn.",
        ),
        VoiceLine(
            150,
            Hassler,
            ru="К черту тебя, предатель! Зубы ты о нас обломаешь.",
            en="To hell with you, traitor! You'll break your teeth trying to bite us.",
        ),
        VoiceLine(
            160,
            Dietrich,
            ru="Кто это? Хасслер? Хватит служить этому гнилому коррумпированному правительству! Переходи на сторону истинных патриотов Рейнланда! Сдавайся и я сохраню жизнь тебе и твоим людям.",
            en="Who's that? Hassler? Stop serving this rotten, corrupted government! Come join the true patriots of Rheinland! Surrender, and I'll spare the life of you and your people.",
        ),
        VoiceLine(
            170,
            Hassler,
            ru="Себе попробуй сохранить!",
            en="You better hold on to yours instead!",
        ),
        VoiceLine(
            180,
            Hassler,
            ru="Говорит Каратель-1! Генераторы нижней полусферы уничтожены! Повторяю, генераторы щита уничтожены!",
            en="This is Punisher-1! Lower hemisphere generators destroyed! I repeat, the shield generators are destroyed!",
        ),
        VoiceLine(
            190,
            Reichman,
            ru="Понял вас, Каратель-1. Начинаем атаку на базу.",
            en="Roger that, Punisher-1. We'll begin our attack on the base.",
        ),
        VoiceLine(
            1150,
            Wilham,
            ru="Флот прибыл. Каратели, расчистите зону от оставшихся кораблей неприятеля.",
            en="The fleet is here. Punishers, clear all remaining hostile ships in the area. ",
        ),
        VoiceLine(
            1160,
            Hassler,
            ru="Это каратель-1, вас понял.",
            en="This is Punisher-1, loud and clear. ",
        ),
        VoiceLine(
            1170,
            Hassler,
            ru="Щит упал. Каратели, выдвигаемся к базе.",
            en="The shield is down. Punishers, move closer to the base.",
        ),
        VoiceLine(
            200,
            Trent,
            ru="Хасслер, что это? Группа меток на девять часов.",
            en="Hassler, what IS that? A few scratches take nine hours!",
        ),
        VoiceLine(
            210,
            Hassler,
            ru="А, черт. Башня, это Каратель-1. Похоже Дитрих с небольшой группой прикрытия решил уйти от нас!",
            en="Oh, hell. Tower, this is Punisher-1. It seems like Dietrich is fleeing away with a small escort!",
        ),
        VoiceLine(
            220,
            Reichman,
            ru="Каратель-1, остановите их любой ценой!!!",
            en="Punisher-1, stop them at all costs!!!",
        ),
        VoiceLine(
            230,
            Hassler,
            ru="Каратели, боевое построение! Цель - группа уходящих кораблей с грузовиком в центре. ",
            en="Punishers, battle formation! Our goal – a group of departing ships with a transport ahead of the formation.",
        ),
        VoiceLine(
            240,
            Hassler,
            ru="Уничтожить корабли противника!",
            en="Destroy the hostile ships!",
        ),
        VoiceLine(
            250,
            Trent,
            ru="Грузовик уходит.",
            en="The transport's leaving.",
        ),
        VoiceLine(
            260,
            Hassler,
            ru="Займемся им позже.",
            en="We'll deal with him later.",
        ),
        VoiceLine(
            1200,
            Punisher,
            ru="Дитрих включил какой-то дополнительный щит и стал неуязвимым ко всем атакам!",
            en="Dietrich turned some kind of additional shield on, he's now invulnerable to all attacks! ",
        ),
        VoiceLine(
            1210,
            Hassler,
            ru="Продолжайте огонь по нему, он не сможет защищаться бесконечно.",
            en="Keep firing, he won't be able to hold on for much longer.",
        ),
        VoiceLine(
            270,
            Reichman,
            ru="Говорит адмирал Райхманн. Станция уничтожена. Всем спасибо. Хасслер, доложите статус.",
            en="This is Admiral Reichmann. The station is destroyed. Well done everyone. Hassler, status report.",
        ),
        VoiceLine(
            280,
            Hassler,
            ru="Дитрих и его отряд уничтожен. Ушел один грузовик из их отряда.",
            en="Dietrich and his squad are destroyed. One transport has managed to escape.",
        ),
        VoiceLine(
            290,
            Reichman,
            ru="ХАССЛЕР, ТВОЮ МАТЬ!!! Как ты мог это допустить??? Срочно найти грузовик и уничтожить его!!!",
            en="HASSLER, YOU SON OF A-!!! How could you allow this??? Find that transport and destroy it immediately!!!",
        ),
        VoiceLine(
            300,
            Hassler,
            ru="Каратели, за мной.",
            en="Punishers, follow me.",
        ),
        VoiceLine(
            1180,
            Punisher,
            ru="Тепловой след ведет к неизвестным гипервратам и обрывается.",
            en="The heat trail leads to an unknown jump gate and breaks off. ",
        ),
        VoiceLine(
            1190,
            Hassler,
            ru="Летим следом. Может, еще нагоним.",
            en="We'll follow in. Maybe we can still catch up.",
        ),
        VoiceLine(
            310,
            Trent,
            ru="Это гиперврата. Здесь столько кораблей проходит ежедневно, что мы не сможем их отследить.",
            en="That's a jump gate. There are so many ships passing by every day, we can't keep track of them.",
        ),
        VoiceLine(
            320,
            Hassler,
            ru="Направляемся на базу изгоев Виго. Может там что-нибудь знают...",
            en="We'll head to the rogue base, Vigo. Maybe they'll know something...",
        ),

        VoiceLine(
            9010,
            Neuralnet,
            ru="Ост+алось 10 минут до активации щита К+ёнигсберга",
        ),
        VoiceLine(
            9020,
            Neuralnet,
            ru="Ост+алось 9 минут до активации щита К+ёнигсберга",
        ),
        VoiceLine(
            9030,
            Neuralnet,
            ru="Ост+алось 8 минут до активации щита К+ёнигсберга",
        ),
        VoiceLine(
            9040,
            Neuralnet,
            ru="Ост+алось 7 минут до активации щита К+ёнигсберга",
        ),
        VoiceLine(
            9050,
            Neuralnet,
            ru="Ост+алось 6 минут до активации щита К+ёнигсберга",
        ),
        VoiceLine(
            9060,
            Neuralnet,
            ru="Ост+алось 5 минут до активации щита К+ёнигсберга",
        ),
        VoiceLine(
            9070,
            Neuralnet,
            ru="Ост+алось 4 минуты до активации щита К+ёнигсберга",
        ),
        VoiceLine(
            9080,
            Neuralnet,
            ru="Ост+алось 3 минуты до активации щита К+ёнигсберга",
        ),
        VoiceLine(
            9090,
            Neuralnet,
            ru="Ост+алось 2 минуты до активации щита К+ёнигсберга",
        ),
        VoiceLine(
            9100,
            Neuralnet,
            ru="Ост+алось 1 минута до активации щита К+ёнигсберга",
        ),
        VoiceLine(
            9110,
            Neuralnet,
            ru="Ост+алось 30 секунд до активации щита К+ёнигсберга",
        ),
    ]


class Mission3(Msn3, script.StoryMission):
    MISSION_INDEX = 3
    CUTSCENES = []
    SPACE_CLASS = Msn3Space
    SYNC_SPACE = True

    MISSION_TITLE = 'Миссия 3. Штурм Кёнигсберга'
