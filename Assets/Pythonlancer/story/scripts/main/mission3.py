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
        VoiceLine(10, Trent, ru="Салют, джентльмены.", en="Greetings, gentlemen."),
        VoiceLine(20, Wilham, ru="А вот и герр Трент. Познакомьтесь с герром Хасслером. В ходе этой миссии вам придется плотно сотрудничать.",
                  en="Herr Trent, please meet Herr Hassler. This next mission will require both of you to work closely together."),
        VoiceLine(30, Trent, ru="Герр Хасслер, мое почтение.", en="An honor to meet you, Herr Hassler."),
        VoiceLine(40, Trent, ru="И в чем же будет состоять эта миссия?", en="And what will we be doing on this mission?"),
        VoiceLine(50, Wilham, ru="Да как обычно. Летаем, стреляем, ничего нового.", en="The usual. Hours of boredom, seconds of terror, fly vast distances, blow things up. Nothing special."),
        VoiceLine(60, Trent, ru="А кто-то на безопасном расстоянии отсиживается. Действительно, ничего нового. А можно как-то конкретнее?",
                  en="While a certain someone is watching safely from afar. Starting to see a pattern here. Could you be any less specific?"),
        VoiceLine(70, Wilham, ru="Можно. Наша разведка локализовала местонахождение Дитриха. Это бывшая военная база Кёнигсберг. ",
                  en="Of course. Rhineland intelligence has managed to track down Dietrich's position. He's camping out on an old military base in Konigsberg."),
        VoiceLine(75, Wilham, ru="В данный момент собирается ударный флот для атаки базы. Но наши аналитики просчтитали, что прямое нападение на Кёнигсберг приведет к недопустимо большим потерям среди личного состава.",
                  en="We are amassing a strike fleet to raid his base as we speak. However our analysts project we will suffer massive casualties if we stage a frontal assault on Konigsberg."),
        VoiceLine(77, Wilham, ru="Поэтому мы так же формируем мобильную ударную группу, задачей которой будет нейтрализация защитной системы базы к моменту подхода основных сил.",
                  en="That's why we're forming a secondary strike team, which will neutralize the base's defense systems just in time for our main strike fleet to sweep in and decimate it."),
        VoiceLine(80, Trent, ru="То есть те, кто будет таскать вам каштаны из огня.", en="Let me guess, you need some stooges to make up the secondary strike team..."),
        VoiceLine(90, Wilham, ru="Именно так, герр Трент. Кстати на вашем участии в этой миссии настаивал лично адмирал Райхманн.",
                  en="You are so good at guessing, Herr Trent. By the way, Admiral Reichmann personally requested for you to be on the secondary strike team."),
        VoiceLine(100, Trent, ru="Весьма польщён. А можно узнать, как так оказалось, что элитная военная база с высшим классом защиты практически в самом центре территории Рейнланда осталась бесхозной и в итоге досталась мятежникам и корсарам?",
                  en="I don't know whether to be flattered or flustered. Could you explain to me how an ultra-secure military base with best in class defense systems, smack in the center of Rheinland came to be abandoned and fall into the hands of Corsairs, rebels and riff-raff?"),


        VoiceLine(110, Hassler, ru="Герр Трент, станция Кёнигисберг когда-то была частью Мюнхенского контура обороны. Военные Кусари рассматривали этот контур не иначе, чем шило у себя в заднице. ",
                  en="During the Kusari wars there were two major bases nearing completion in Rheinland territory - Konigsberg and Regensburg, both were in the Munich system, on the border with Kusari. The Kusari military saw Regensburg as a mere thorn in their side. Konigsberg, however was more significant strategically."),


        VoiceLine(115, Hassler, ru="В ходе разравившегося конфликта с Кусари мы потерпели сокрушительное поражение и по условиям мирного договора строительство контура было прекращено, а система Мюнхен была полностью демилитаризована.",
                  en="During our last conflict with Kusari, we were dealt a crushing defeat and under the terms of the resulting armistace we were forced to demilitarize Munich. The construction of Konigsberg was halted just before completion... "),


        VoiceLine(120, Hassler, ru="Станция Кёнигсберг была законсервирована до нынешних пор, когда Дитрих, воспользовавшись старыми ключами и доступами, не решил сделать из станции свой опорный пункт.",
                  en="Our government strangely did not take steps to scuttle or dismantle Konigsberg base. Perhaps they were hoping for a re-negotiation of the peace treaty, or perhaps they had some other scheme lost to history, I don't know. Eventually, Dietrich, having turned coat, and being in possession of all the access keys, just waltzed in and claimed it..."),



        VoiceLine(130, Trent, ru="Я так понимаю, спрашивать всякие глупости типа, есть ли у меня выбор, в этой ситуации неуместно.",
                  en="I'm guessing that asking whether I have a choice or not to participate is a stupid question."),
        VoiceLine(140, Wilham, ru=": Вы умный человек, герр Трент. ", en="You so wise, for a stupid man, Herr Trent. "),
        VoiceLine(150, Hassler, ru="Герр Трент, вам предлагают работу, которая и не снилась большей части местных фрилансеров.",
                  en="Herr Trent, ninety percent of the local freelancers could only dream of being in your shoes. Astronomical pay and reporting directly to none other than the legendary Admiral Reichmann. Something others would die for. In fact, many have."),
        VoiceLine(155, Hassler, ru="Что вы капризничаете как старшеклассница на выпускном? Давайте вылетать. Встречаемся в космосе.",
                  en="Are you well? You look as nervous as a highschool girl on graduation day. Or prom night. Ha ha. Let's fly. See you in space."),
    ]


class Msn3Reward(Msn3, script.CutsceneProps):
    ALIAS = 'reward'
    TITLE = 'Финал'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Hassler, ru="Расспросил я местных, нихрена они не знают. В любом случае, спасибо, Трент, твоя работа на этом закончена, будем искать грузовик по нашим каналам.",
                  en="The locals haven't reported anything unusual. Anyway, thank you, Trent. Your work here is done, we'll continue searching for the transport on our own. Unfortunately, since we screwed up, Reichmann cut your payment significantly ."),
        VoiceLine(15, Hassler, ru="К сожалению, из-за того, что  мы с ним облажались, Райхманн значительно урезал гонорар.",
                  en="The locals haven't reported anything unusual. Anyway, thank you, Trent. Your work here is done, we'll continue searching for the transport on our own. Unfortunately, since we screwed up, Reichmann cut your payment significantly ."),
        VoiceLine(20, Trent, ru="Странные дела. Базу уничтожили, Дитриха грохнули, а Райхманн выбесился из-за какого-то грузовика. Не нравится мне это.",
                  en="Crap. The rebel base was destroyed, Dietrich's dead, yet Reichmann freaks out and stiffs me because of some puny transport. I'm not a happy camper."),
        VoiceLine(30, Hassler, ru="Мне тоже... Деньги уже на твоем счету. До скорого.", en="Nor me... The money's been transferred to your account. Go get a drink on me. See you later."),
    ]


class Msn3Space(Msn3, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(
            0,
            WilhamStation,
            ru="Герр Трент, нам опять понадобились ваши услуги. Все подробности на станции Штарке, система Сигма-8. Вильгельм.",
            en="Herr Trent, we are in need of your services once again. We will discuss the details on Starke station in the Sigma-8 system. Wilham base, over.",
        ),
        VoiceLine(
            1010,
            Hassler,
            ru="Направляемся к пункту сбора. Координаты уже в вашем бортовом компьютере, герр Трент.  ",
            en="We're heading to the rendezvous point. The coordinates are already on your system, Herr Trent.",
        ),
        VoiceLine(
            1020,
            Wilham,
            ru="Я доложил Адмирал Райхманну, что мы уже в пути. Он начинает брифинг миссии.",
            en="I've informed Admiral Reichmann that we're on the way. He'll commence the mission briefing shortly.",
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
            en="Testing… (presses a button) okay everyone, listen up. ",
        ),
        VoiceLine(
            20,
            Reichman,
            ru="Напоминаю всем диспозицию. Основное средство защиты станции - энергетический щит, разделенный на две полусферы.",
            en="To recap. The station's main defence is its' energy shield, divided into two hemispheres. ",
        ),
        VoiceLine(
            30,
            Reichman,
            ru="Щит способен долгое время выдерживать прямые попадания главного калибра наших линкоров. Недостаток щита - долгое время зарядки.",
            en="The shield is able to withstand direct hits from our battleships' weapons. Its weakness is a prolonged charging period before activation.",
        ),
        VoiceLine(
            35,
            Reichman,
            ru="После зарядки времени его работы хватит чтобы наш ударный флот был рассеян.",
            en="After it's fully charged, it stays active for about an hour, long enough for their fighters to take out our strike teams. ",
        ),
        VoiceLine(
            40,
            Reichman,
            ru="Для нейтрализации щита были сформированы две мобильные боевые группы под командованием Хасслера и Греве. Одна из них займется уничтожением генераторов верхней полусферы щита, вторая – нижней.",
            en="To neutralize the shield, two mobile strike teams under the command of Hassler and Greave will move in. One will destroy the generators of the upper hemisphere, and the other – the lower.  ",
        ),
        VoiceLine(
            50,
            Reichman,
            ru="Эти группы должны будут выдвинуться к месту назначения через аномалию, которая будет активирована с корабля герра Хасслера. Вот в общем и все. Начинаем!",
            en="These teams will advance to their destinations through an anomaly that will be activated by Herr Hassler. That is all. Let's go!",
        ),
        VoiceLine(
            1050,
            Hassler,
            comment='Брифинг окончен',
            ru="Всё поняли, ребята? Выдвигаемся.",
            en="Everything clear, people? Moving in.  ",
        ),
        VoiceLine(
            1060,
            Marauder,
            ru="Аномалия прямо по курсу. Судя по сканерам, она еще активна.",
            en="Anomaly ahead. Judging by the scanners, it's active. ",
        ),
        VoiceLine(
            1070,
            Hassler,
            ru="Принял, начинаю подготовку устройства.",
            en="Roger, prepare the device.",
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
            ru="Готово. Входим в аномалию.",
            en="Go on in.",
        ),
        VoiceLine(
            70,
            Hassler,
            ru="(Кругом враги!) Внимание! Обнаружены корабли корсаров! Боевое построение! Уничтожить вражеские истребители!",
            en="Achtung! I'm reading Corsair ships! Enter battle formation!",
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
            ru="Каратели, Мародёры, направляемся к станции Кёнигсберг.",
            en="Heading to the station. ",
        ),
        VoiceLine(
            80,
            Hassler,
            comment='Мы вылетели из туманности и видим Кёнигсберг',
            ru="Генераторы станции начали зарядку щита! Задача - уничтожить генераторы до полной зарядки! Повторяю: основная цель - генераторы!",
            en="The stations' generators have started charging the shields! Destroy the generators before they're fully charged! I repeat–our main goal is the generators!",
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
            comment='Взорвали первый генератор щита',
            ru="Генераторы верхней полусферы уничтожены!",
            en="The upper hemispheres' generators are down!",
        ),
        VoiceLine(
            100,
            Hassler,
            ru="Мародер-1, говорит Каратель-1, уходите под наше прикрытие!!! Повторяю, уходите под прикрытие звена Карателей!",
            en="Marauder-1, this is Punisher-1, close in with us, we'll cover you!!!I repeat, close in with us, Punisher wing will provide cover fire!",
        ),
        VoiceLine(
            110,
            Marauder,
            ru="Не можем уничтожить генераторы! Противодействие против...",
            en="There's too many of them! We won't be able to take out the generators! Tell my family... chhhhhhhh",
        ),
        VoiceLine(
            120,
            Hassler,
            ru="Башня, говорит Каратель-1, звено Мародер полностью уничтожено. Приступаем к уничтожению генераторов нижней полусферы.",
            en="Tower, this is Punisher-1, Marauder wing is down. We're diverting to destroy the lower hemisphere generators.",
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
            comment='Дитрих выходит на связь и начинает переманивать на тёмную сторону силы',
            ru="Каратель, Мародер, какие красочные позывные! Как жаль что придется вас уничтожить. Мародер уже готов, Каратель - на очереди.",
            en="Punisher, Marauder, such sexy call signs! Such a shame you are in my way. Marauder wing is dead. Punisher wing – it's your turn.",
        ),
        VoiceLine(
            150,
            Hassler,
            ru="Пошёл ты к чёрту, Дитрих! Ты ответишь за все свои преступления против народа Рейнланда!",
            en="Go to hell, you traitor! Chew on this, I hope you break your teeth!",
        ),
        VoiceLine(
            160,
            Dietrich,
            ru="Кто это? Хасслер? Хватит служить этому гнилому коррумпированному правительству! Переходи на сторону истинных патриотов Рейнланда! Сдавайся и я сохраню жизнь тебе и твоим людям.",
            en="Who is that? Is that you, Hassler? It's not too late to quit your rotten, self-serving government! You know I'm right - come and join the people and patriots of Rheinland! If you do, I'll give you and your men a chance to surrender and live, on my honour!",
        ),
        VoiceLine(
            170,
            Hassler,
            ru="Себе попробуй сохранить, предатель! Тебе грозит смертный приговор. Сдавайся сам, пока я до тебя еще не добрался!",
            en="Honour? What about all the men you've murdered! I'll trade your honour for justice.",
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
            en="Roger that, Punisher-1. Commencing our attack on the base.",
        ),
        VoiceLine(
            1150,
            Wilham,
            comment='Флот тут!',
            ru="Флот прибыл. Каратели, расчистите зону от оставшихся кораблей неприятеля.",
            en="The fleet has arrived. Punishers, clear the area of any remaining hostiles. ",
        ),
        VoiceLine(
            1160,
            Hassler,
            ru="Это каратель-1, вас понял. Приказ - уничтожить все истребители противника!",
            en="This is Punisher-1, receiving loud and clear. ",
        ),
        VoiceLine(
            1170,
            Hassler,
            comment='Мы раскидали истребителей, щит Кёнигсберга вырубился',
            ru="Щит упал. Каратели, выдвигаемся к базе.",
            en="The shield is down. Punishers, close on the base.",
        ),
        VoiceLine(
            200,
            Trent,
            ru="Хасслер, что это? Группа меток на девять часов.",
            en="Hassler, what is THAT? Targets at nine o'clock!",
        ),
        VoiceLine(
            210,
            Hassler,
            ru="А, чёрт. Башня, это Каратель-1. Похоже Дитрих с небольшой группой прикрытия решил уйти от нас!",
            en="Oh, hell. Tower, this is Punisher-1. Dietrich is escaping with a small fighter wing and a transport!",
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
            en="Punishers, battle formation! Take out the Dietrich, the transport and the fighter escorts.",
        ),
        VoiceLine(
            240,
            Hassler,
            comment='Догнали Дитриха, он развернулся и вступил с нами в бой',
            ru="Уничтожить Дитриха! Немедленно!",
            en="Destroy the enemy!",
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
            en="Too much heat. We'll deal with the transport later. Stay on Dietrich and his men.",
        ),
        VoiceLine(
            1200,
            Punisher,
            ru="Дитрих включил какой-то дополнительный щит и стал неуязвимым ко всем атакам!",
            en="Dietrich's activated some kind of super shield - it's like nothing I've seen before! He's practically invulnerable! ",
        ),
        VoiceLine(
            1210,
            Hassler,
            ru="Продолжайте огонь по Дитриху. Чтобы там у него на корабле не было, он не сможет сопротивляться бесконечно.",
            en="Keep firing, I'm sure it can't last forever.",
        ),
        VoiceLine(
            270,
            Reichman,
            comment='Дитрих всё, Кёнигсберг взорван',
            ru="Говорит адмирал Райхманн. Станция уничтожена. Всем спасибо. Хасслер, доложите статус.",
            en="This is Admiral Reichmann. The station is destroyed. Well done everyone. Hassler, status report.",
        ),
        VoiceLine(
            280,
            Hassler,
            ru="(сухой отчёт) Дитрих и его эскорт уничтожен. Грузовик, который был в формации Дитриха, покинул место боя и скрылся.",
            en="Dietrich and his squad are destroyed. The transport got away.",
        ),
        VoiceLine(
            290,
            Reichman,
            ru="ХАССЛЕР, ТВОЮ МАТЬ!!! Как ты мог это допустить??? Срочно найти грузовик и уничтожить его!!!",
            en="HASSLER, YOU FOOL!!! Of all the incompetent... Locate the transport and destroy it immediately!!!",
        ),
        VoiceLine(
            300,
            Hassler,
            ru="(выдохнув после оплеухи) Каратели, за мной.",
            en="Punishers, on me.",
        ),
        VoiceLine(
            1180,
            Punisher,
            ru="Тепловой след ведет к неизвестным гипервратам и обрывается.",
            en="The heat signature leads to an unknown jump gate then disappears. ",
        ),
        VoiceLine(
            1190,
            Hassler,
            ru="Летим следом. Возможно мы ещё его нагоним.",
            en="Follow it in. We may still be able to catch up with it.",
        ),
        VoiceLine(
            310,
            Trent,
            ru="Это гиперврата. Здесь столько кораблей проходит ежедневно, что мы не сможем их отследить.",
            en="There's the jump gate. There are too many ship signatures, we can't isolate the shuttle's.",
        ),
        VoiceLine(
            320,
            Hassler,
            ru="Ладно, направляемся на базу Виго. Может хоть там что-то знают...",
            en="We'll head to the Rogue base Vigo. They might know something...",
        ),

        VoiceLine(
            9010,
            Neuralnet,
            ru="Ост+алось 10 минут до активации щита К+ёнигсберга",
            en="10 minutes remaining to activation of Königsberg's shield",
        ),
        VoiceLine(
            9020,
            Neuralnet,
            ru="Ост+алось 9 минут до активации щита К+ёнигсберга",
            en="9 minutes remaining to activation of Königsberg's shield",
        ),
        VoiceLine(
            9030,
            Neuralnet,
            ru="Ост+алось 8 минут до активации щита К+ёнигсберга",
            en="8 minutes remaining to activation of Königsberg's shield",
        ),
        VoiceLine(
            9040,
            Neuralnet,
            ru="Ост+алось 7 минут до активации щита К+ёнигсберга",
            en="7 minutes remaining to activation of Königsberg's shield",
        ),
        VoiceLine(
            9050,
            Neuralnet,
            ru="Ост+алось 6 минут до активации щита К+ёнигсберга",
            en="6 minutes remaining to activation of Königsberg's shield",
        ),
        VoiceLine(
            9060,
            Neuralnet,
            ru="Ост+алось 5 минут до активации щита К+ёнигсберга",
            en="5 minutes remaining to activation of Königsberg's shield",
        ),
        VoiceLine(
            9070,
            Neuralnet,
            ru="Ост+алось 4 минуты до активации щита К+ёнигсберга",
            en="4 minutes remaining to activation of Königsberg's shield",
        ),
        VoiceLine(
            9080,
            Neuralnet,
            ru="Ост+алось 3 минуты до активации щита К+ёнигсберга",
            en="3 minutes remaining to activation of Königsberg's shield",
        ),
        VoiceLine(
            9090,
            Neuralnet,
            ru="Ост+алось две минуты до активации щита К+ёнигсберга",
            en="2 minutes remaining to activation of Königsberg's shield",
        ),
        VoiceLine(
            9100,
            Neuralnet,
            ru="Ост+алась одна минута до активации щита К+ёнигсберга",
            en="1 minute remaining to activation of Königsberg's shield",
        ),
        VoiceLine(
            9110,
            Neuralnet,
            ru="Ост+алось 30 секунд до активации щита К+ёнигсберга",
            en="30 seconds remaining to activation of Königsberg's shield",
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