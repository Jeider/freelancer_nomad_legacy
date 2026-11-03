from story import script
from audio.sound import VoiceLine
from story.actors import (
    Trent, Wilham, WilhamStation, Hassler, Reichman, Marauder, Punisher, Dietrich, Neuralnet
)


class Msn3(object):
    MISSION_INDEX = 3


class Msn3Offer(Msn3, script.CutsceneProps):
    ALIAS = 'offer'
    TITLE = 'Штарке'
    DESCRIPTION = 'Бар станции. Два военных проводят брифинг и предлагают, как обычно, сверх опасную миссию.'
    VOICE_LINES = [
        VoiceLine(10, Trent, ru="Салют, джентльмены.", en="Hey, gentlemen."),
        VoiceLine(20, Wilham, ru="А вот и герр Трент. Познакомьтесь с герром Хасслером. В ходе этой миссии вам придется плотно сотрудничать.",
                  en="And here's Herr Trent. Meet Herr Hassler. On this mission you will have to work closely together."),
        VoiceLine(30, Trent, ru="Герр Хасслер, мое почтение.", en="Herr Hassler, my respects."),
        VoiceLine(40, Trent, ru="И в чем же будет состоять эта миссия?", en="And what will this mission consist of?"),

        VoiceLine(70, Wilham, ru="Наша разведка локализовала местонахождение Дитриха. Это бывшая военная база Кёнигсберг. ",
                  en="Our intelligence has pinpointed Dietrich's location. It's the former military base Königsberg."),
        VoiceLine(75, Wilham, ru="В данный момент собирается ударный флот для атаки базы, но её системы защита будет готова к лобовому удару.",
                  en="A strike fleet is being assembled right now to attack the base, but its defense systems will be ready for a frontal strike."),
        VoiceLine(77, Wilham, ru="Поэтому мы формируем мобильную диверсионную группу, которая нанесет критические повреждения Кёнигсбергу до момента подхода основных сил.",
                  en="So we're forming a mobile sabotage group that will inflict critical damage on Königsberg before the main forces arrive."),

        VoiceLine(80, Trent, ru="То есть те, кто будет таскать вам каштаны из огня.",
                  en="Meaning the ones who'll pull your chestnuts out of the fire."),

        VoiceLine(90, Wilham,
                  ru="Именно так, герр Трент. Кстати на вашем участии в этой миссии настаивал лично адмирал Райхманн.",
                  en="Exactly so, Herr Trent. By the way, Admiral Reichmann personally insisted on your participation in this mission."),

        VoiceLine(100, Trent, ru="А можно узнать, как так оказалось, что элитная военная база осталась бесхозной и в итоге досталась мятежникам и корсарам?",
                  en="Can I ask how an elite military base came to be left ownerless and ended up with rebels and Corsairs?"),

        VoiceLine(110, Hassler, ru="Герр Трент, станция Кёнигисберг когда-то была частью Мюнхенского контура обороны. Военные Кусари рассматривали этот контур не иначе, чем шило у себя в заднице. ",
                  en="Herr Trent, Königsberg station was once part of the Munich defense perimeter. The Kusari military regarded that perimeter as nothing less than an awl up their ass."),


        VoiceLine(115, Hassler, ru="В ходе разравившегося конфликта с Кусари мы потерпели сокрушительное поражение и по условиям мирного договора строительство контура было прекращено, а система Мюнхен была полностью демилитаризована.",
                  en="In the conflict with Kusari that broke out, we suffered a crushing defeat, and under the terms of the peace treaty construction of the perimeter was stopped, and the Munich system was completely demilitarized."),


        VoiceLine(120, Hassler, ru="Станция Кёнигсберг была законсервирована до нынешних пор, когда Дитрих, воспользовавшись старыми ключами и доступами, не решил сделать из станции свой опорный пункт.",
                  en="Königsberg station was mothballed until now, when Dietrich, using the old keys and access codes, went and made the station his strongpoint."),


        VoiceLine(130, Trent, ru="Я так понимаю, спрашивать всякие глупости типа, есть ли у меня выбор, в этой ситуации неуместно.",
                  en="I take it that asking foolish things, like whether I have a choice, is out of place in this situation."),
        VoiceLine(140, Wilham, ru="Вы умный человек, герр Трент. ", en="You're a smart man, Herr Trent."),
        VoiceLine(150, Hassler, ru="Герр Трент, вам предлагают работу, которая и не снилась большей части местных фрилансеров.",
                  en="Herr Trent, you're being offered work that most local freelancers never even dreamed of."),
        VoiceLine(155, Hassler, ru="Что вы капризничаете как старшеклассница на выпускном? Давайте вылетать. Встречаемся в космосе.",
                  en="Why are you fussing like a high school girl at graduation? Let's fly. We'll meet in space."),
    ]


class Msn3Reward(Msn3, script.CutsceneProps):
    ALIAS = 'reward'
    TITLE = 'Финал'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Hassler, ru="Расспросил я местных, нихрена они не знают. В любом случае, спасибо, Трент, твоя работа на этом закончена, будем искать грузовик по нашим каналам.",
                  en="I asked the locals. They don't know a damn thing. Anyway, thanks, Trent, your work here is done. We'll look for the transport through our own channels."),
        VoiceLine(15, Hassler, ru="К сожалению, из-за того, что  мы с ним облажались, Райхманн значительно урезал гонорар.",
                  en="Unfortunately, because he and I screwed up, Reichmann cut the fee significantly."),
        VoiceLine(20, Trent, ru="Странные дела. Базу уничтожили, Дитриха грохнули, а Райхманн выбесился из-за какого-то грузовика. Не нравится мне это.",
                  en="Strange business. The base is destroyed, Dietrich's been taken out, and Reichmann lost it over some transport. I don't like this."),
        VoiceLine(30, Hassler, ru="Мне тоже... Деньги уже на твоем счету. До скорого.", en="Me neither... The money's already in your account. See you soon."),
    ]


class Msn3Space(Msn3, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(
            0,
            WilhamStation,
            ru="Герр Трент, нам опять понадобились ваши услуги. Все подробности на станции Штарке, система Сигма-8. Вильгельм.",
            en="Herr Trent, we need your services again. All the details are at Starke station, Sigma-8 system. Wilhelm.",
        ),
        VoiceLine(
            1010,
            Hassler,
            ru="Направляемся к пункту сбора. Координаты уже в вашем бортовом компьютере, герр Трент.  ",
            en="Heading to the assembly point. The coordinates are already in your onboard computer, Herr Trent.",
        ),
        VoiceLine(
            1020,
            Wilham,
            ru="Я доложил Адмирал Райхманну, что мы уже в пути. Он начинает брифинг миссии.",
            en="I've reported to Admiral Reichmann that we're already on the way. He's starting the mission briefing.",
        ),
        VoiceLine(
            1030,
            Hassler,
            ru="Ретранслируй брифинг в общий канал. Герр Трент, слушайте внимательно. ",
            en="Relay the briefing to the common channel. Herr Trent, listen carefully.",
        ),
        VoiceLine(
            1040,
            Wilham,
            ru="Сейчас… (нажимает на кнопочку) готово, слушайте.",
            en="One moment... (presses a button) done, listen.",
        ),
        VoiceLine(
            20,
            Reichman,
            ru="Напоминаю всем диспозицию. Основное средство защиты станции - энергетический щит, разделенный на две полусферы.",
            en="Let me remind everyone of the disposition. The station's main defense is an energy shield, divided into two hemispheres.",
        ),
        VoiceLine(
            30,
            Reichman,
            ru="Щит способен долгое время выдерживать прямые попадания главного калибра наших линкоров. Недостаток щита - долгое время зарядки.",
            en="The shield can withstand direct hits from our battleships' main guns for a long time. The shield's weakness is a long charging time.",
        ),
        VoiceLine(
            35,
            Reichman,
            ru="После зарядки времени его работы хватит чтобы наш ударный флот был рассеян.",
            en="After charging, its operating time will be enough for our strike fleet to be scattered.",
        ),
        VoiceLine(
            40,
            Reichman,
            ru="Для нейтрализации щита были сформированы две мобильные боевые группы под командованием Хасслера и Греве. Одна из них займется уничтожением генераторов верхней полусферы щита, вторая – нижней.",
            en="To neutralize the shield, two mobile combat groups have been formed under the command of Hassler and Greve. One of them will destroy the generators of the shield's upper hemisphere, the other — the lower.",
        ),
        VoiceLine(
            50,
            Reichman,
            ru="Эти группы должны будут выдвинуться к месту назначения через аномалию, которая будет активирована с корабля герра Хасслера. Вот в общем и все. Начинаем!",
            en="These groups will move out to their destination through an anomaly that will be activated from Herr Hassler's ship. That's about all. Let's begin!",
        ),
        VoiceLine(
            1050,
            Hassler,
            comment='Брифинг окончен',
            ru="Всё поняли, ребята? Выдвигаемся.",
            en="Everyone got that, guys? Moving out.",
        ),
        VoiceLine(
            1060,
            Marauder,
            ru="Аномалия прямо по курсу. Судя по сканерам, она еще активна.",
            en="Anomaly dead ahead. Judging by the scanners, it's still active.",
        ),
        VoiceLine(
            1070,
            Hassler,
            ru="Принял, начинаю подготовку устройства.",
            en="Copy. I'm starting to prepare the device.",
        ),
        VoiceLine(
            60,
            Hassler,
            ru="Каратели, говорит Каратель-1, активирую аномалию.",
            en="Punishers, this is Punisher-1, activating the anomaly.",
        ),
        VoiceLine(
            65,
            Hassler,
            ru="Готово. Входим в аномалию.",
            en="Done. Entering the anomaly.",
        ),
        VoiceLine(
            70,
            Hassler,
            ru="(Кругом враги!) Внимание! Обнаружены корабли корсаров! Боевое построение! Уничтожить вражеские истребители!",
            en="(Enemies all around!) Attention! Corsair ships detected! Battle formation! Destroy the enemy fighters!",
        ),
        VoiceLine(
            1100,
            Marauder,
            ru="Сектор чист.",
            en="Sector clear.",
        ),
        VoiceLine(
            1110,
            Hassler,
            ru="Каратели, Мародёры, направляемся к станции Кёнигсберг.",
            en="Punishers, Marauders, heading to Königsberg station.",
        ),
        VoiceLine(
            80,
            Hassler,
            comment='Мы вылетели из туманности и видим Кёнигсберг',
            ru="Генераторы станции начали зарядку щита! Задача - уничтожить генераторы до полной зарядки! Повторяю: основная цель - генераторы!",
            en="The station's generators have started charging the shield! The task is to destroy the generators before they're fully charged! I repeat: the primary target is the generators!",
        ),
        VoiceLine(
            1130,
            Marauder,
            ru="Так точно, Каратель-1.",
            en="Affirmative, Punisher-1.",
        ),
        VoiceLine(
            90,
            Hassler,
            comment='Взорвали первый генератор щита',
            ru="Генераторы верхней полусферы уничтожены!",
            en="Upper hemisphere generators destroyed!",
        ),
        VoiceLine(
            100,
            Hassler,
            ru="Мародер-1, говорит Каратель-1, уходите под наше прикрытие!!! Повторяю, уходите под прикрытие звена Карателей!",
            en="Marauder-1, this is Punisher-1, get under our cover!!! I repeat, get under the cover of the Punisher flight!",
        ),
        VoiceLine(
            110,
            Marauder,
            ru="Не можем уничтожить генераторы! Противодействие против...",
            en="We can't destroy the generators! Resistance against...",
        ),
        VoiceLine(
            120,
            Hassler,
            ru="Башня, говорит Каратель-1, звено Мародер полностью уничтожено. Приступаем к уничтожению генераторов нижней полусферы.",
            en="Tower, this is Punisher-1. Marauder flight is completely destroyed. Proceeding to destroy the lower hemisphere generators.",
        ),
        VoiceLine(
            130,
            Reichman,
            ru="Понял вас, Каратель-1.",
            en="Understood, Punisher-1.",
        ),
        VoiceLine(
            140,
            Dietrich,
            comment='Дитрих выходит на связь и начинает переманивать на тёмную сторону силы',
            ru="Каратель, Мародер, какие красочные позывные! Как жаль что придется вас уничтожить. Мародер уже готов, Каратель - на очереди.",
            en="Punisher, Marauder, what colorful callsigns! What a shame I'll have to destroy you. Marauder is already finished. Punisher is next.",
        ),
        VoiceLine(
            150,
            Hassler,
            ru="Пошёл ты к чёрту, Дитрих! Ты ответишь за все свои преступления против народа Рейнланда!",
            en="Go to hell, Dietrich! You'll answer for all your crimes against the people of Rheinland!",
        ),
        VoiceLine(
            160,
            Dietrich,
            ru="Кто это? Хасслер? Хватит служить этому гнилому коррумпированному правительству! Переходи на сторону истинных патриотов Рейнланда! Сдавайся и я сохраню жизнь тебе и твоим людям.",
            en="Who is this? Hassler? Stop serving this rotten, corrupt government! Come over to the side of Rheinland's true patriots! Surrender, and I'll spare you and your men.",
        ),
        VoiceLine(
            170,
            Hassler,
            ru="Себе попробуй сохранить, предатель! Тебе грозит смертный приговор. Сдавайся сам, пока я до тебя еще не добрался!",
            en="Try saving your own, traitor! You're facing a death sentence. Surrender yourself before I get to you!",
        ),
        VoiceLine(
            180,
            Hassler,
            comment='Мы уничтожили второй генератор',
            ru="Говорит Каратель-1! Генераторы нижней полусферы уничтожены! Повторяю, генераторы щита уничтожены!",
            en="This is Punisher-1! Lower hemisphere generators destroyed! I repeat, the shield generators are destroyed!",
        ),
        VoiceLine(
            190,
            Reichman,
            ru="Понял вас, Каратель-1. Начинаем атаку на базу.",
            en="Understood, Punisher-1. Beginning the attack on the base.",
        ),
        VoiceLine(
            1150,
            Wilham,
            comment='Флот тут!',
            ru="Флот прибыл. Каратели, расчистите зону от оставшихся кораблей неприятеля.",
            en="The fleet has arrived. Punishers, clear the zone of the remaining enemy ships.",
        ),
        VoiceLine(
            1160,
            Hassler,
            ru="Это каратель-1, вас понял. Приказ - уничтожить все истребители противника!",
            en="This is Punisher-1, understood. Order — destroy all enemy fighters!",
        ),
        VoiceLine(
            1170,
            Hassler,
            comment='Мы раскидали истребителей, щит Кёнигсберга вырубился',
            ru="Щит упал. Каратели, выдвигаемся к базе.",
            en="Shield's down. Punishers, moving out to the base.",
        ),
        VoiceLine(
            200,
            Trent,
            ru="Хасслер, что это? Группа меток на девять часов.",
            en="Hassler, what is that? A group of contacts at nine o'clock.",
        ),
        VoiceLine(
            210,
            Hassler,
            ru="А, чёрт. Башня, это Каратель-1. Похоже Дитрих с небольшой группой прикрытия решил уйти от нас!",
            en="Ah, damn. Tower, this is Punisher-1. Looks like Dietrich has decided to slip away from us with a small cover group!",
        ),
        VoiceLine(
            220,
            Reichman,
            ru="Каратель-1, остановите их любой ценой!!!",
            en="Punisher-1, stop them at any cost!!!",
        ),
        VoiceLine(
            230,
            Hassler,
            ru="Каратели, боевое построение! Цель - группа уходящих кораблей с грузовиком в центре. ",
            en="Punishers, battle formation! Target — the group of departing ships with the transport in the center.",
        ),
        VoiceLine(
            240,
            Hassler,
            comment='Догнали Дитриха, он развернулся и вступил с нами в бой',
            ru="Уничтожить Дитриха! Немедленно!",
            en="Destroy Dietrich! Immediately!",
        ),
        VoiceLine(
            250,
            Trent,
            ru="Грузовик уходит.",
            en="The transport's getting away.",
        ),
        VoiceLine(
            260,
            Hassler,
            ru="Займемся им позже. Сейчас нужно разобраться с Дитрихом.",
            en="We'll deal with it later. Right now we need to deal with Dietrich.",
        ),
        VoiceLine(
            1200,
            Punisher,
            ru="Дитрих включил какой-то дополнительный щит и стал неуязвимым ко всем атакам!",
            en="Dietrich activated some kind of extra shield and became invulnerable to all attacks!",
        ),
        VoiceLine(
            1210,
            Hassler,
            ru="Продолжайте огонь по Дитриху. Чтобы там у него на корабле не было, он не сможет сопротивляться бесконечно.",
            en="Keep firing on Dietrich. Whatever he has on that ship, he won't be able to hold out forever.",
        ),
        VoiceLine(
            270,
            Reichman,
            comment='Дитрих всё, Кёнигсберг взорван',
            ru="Говорит адмирал Райхманн. Станция уничтожена. Всем спасибо. Хасслер, доложите статус.",
            en="This is Admiral Reichmann. The station is destroyed. Thank you, everyone. Hassler, report status.",
        ),
        VoiceLine(
            280,
            Hassler,
            ru="(сухой отчёт) Дитрих и его эскорт уничтожен. Грузовик, который был в формации Дитриха, покинул место боя и скрылся.",
            en="(dry report) Dietrich and his escort are destroyed. The transport that was in Dietrich's formation left the battle and disappeared.",
        ),
        VoiceLine(
            290,
            Reichman,
            ru="ХАССЛЕР, ТВОЮ МАТЬ!!! Как ты мог это допустить??? Срочно найти грузовик и уничтожить его!!!",
            en="HASSLER, GOD DAMN YOU!!! How could you let this happen??? Find the transport immediately and destroy it!!!",
        ),
        VoiceLine(
            300,
            Hassler,
            ru="(выдохнув после оплеухи) Каратели, за мной.",
            en="(exhaling after the slap) Punishers, on me.",
        ),
        VoiceLine(
            1180,
            Punisher,
            ru="Тепловой след ведет к неизвестным гипервратам и обрывается.",
            en="The heat trail leads to unknown jump gates and breaks off.",
        ),
        VoiceLine(
            1190,
            Hassler,
            ru="Летим следом. Возможно мы ещё его нагоним.",
            en="We'll follow it. We might still catch up.",
        ),
        VoiceLine(
            310,
            Trent,
            ru="Это гиперврата. Здесь столько кораблей проходит ежедневно, что мы не сможем их отследить.",
            en="It's a jump gate. So many ships pass through here every day that we won't be able to track them.",
        ),
        VoiceLine(
            320,
            Hassler,
            ru="Ладно, направляемся на базу Виго. Может хоть там что-то знают...",
            en="All right, heading to Vigo base. Maybe they'll know something there...",
        ),

        VoiceLine(
            9010,
            Neuralnet,
            ru="Ост+алось 10 минут до активации щита К+ёнигсберга",
            en="10 minutes left until the Königsberg shield activates.",
        ),
        VoiceLine(
            9020,
            Neuralnet,
            ru="Ост+алось 9 минут до активации щита К+ёнигсберга",
            en="9 minutes left until the Königsberg shield activates.",
        ),
        VoiceLine(
            9030,
            Neuralnet,
            ru="Ост+алось 8 минут до активации щита К+ёнигсберга",
            en="8 minutes left until the Königsberg shield activates.",
        ),
        VoiceLine(
            9040,
            Neuralnet,
            ru="Ост+алось 7 минут до активации щита К+ёнигсберга",
            en="7 minutes left until the Königsberg shield activates.",
        ),
        VoiceLine(
            9050,
            Neuralnet,
            ru="Ост+алось 6 минут до активации щита К+ёнигсберга",
            en="6 minutes left until the Königsberg shield activates.",
        ),
        VoiceLine(
            9060,
            Neuralnet,
            ru="Ост+алось 5 минут до активации щита К+ёнигсберга",
            en="5 minutes left until the Königsberg shield activates.",
        ),
        VoiceLine(
            9070,
            Neuralnet,
            ru="Ост+алось 4 минуты до активации щита К+ёнигсберга",
            en="4 minutes left until the Königsberg shield activates.",
        ),
        VoiceLine(
            9080,
            Neuralnet,
            ru="Ост+алось 3 минуты до активации щита К+ёнигсберга",
            en="3 minutes left until the Königsberg shield activates.",
        ),
        VoiceLine(
            9090,
            Neuralnet,
            ru="Ост+алось две минуты до активации щита К+ёнигсберга",
            en="Two minutes left until the Königsberg shield activates.",
        ),
        VoiceLine(
            9100,
            Neuralnet,
            ru="Ост+алась одна минута до активации щита К+ёнигсберга",
            en="One minute left until the Königsberg shield activates.",
        ),
        VoiceLine(
            9110,
            Neuralnet,
            ru="Ост+алось 30 секунд до активации щита К+ёнигсберга",
            en="30 seconds left until the Königsberg shield activates.",
        ),
    ]


class Mission3(Msn3, script.StoryMission):
    MISSION_INDEX = 3
    CUTSCENES = [
        Msn3Offer,
        Msn3Reward,
    ]
    SPACE_CLASS = Msn3Space
    SYNC_SPACE = True
    SYNC_SUBS = True

    MISSION_TITLE = 'Миссия 3. Штурм Кёнигсберга'