from story import script
from audio.sound import VoiceLine
from story.actors import (
    Trent, Wilham, Jacobo, Reichman, Punisher, PunisherCatcher, OmegaJunkerOne, OmegaJunkerTwo, OmegaJunkerThree, Neuralnet
)


class Msn2(object):
    MISSION_INDEX = 2


class Msn2Offer(Msn2, script.CutsceneProps):
    ALIAS = 'offer'
    TITLE = 'Предложение на линкоре'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Trent, ru="Вильгельм, полагаю?", en="Wilhelm, I presume?"),
        VoiceLine(20, Wilham, ru="Так точно, герр Трент. Я рад, что вы согласились с нами работать.", en="That's right, Herr Trent. I'm glad you agreed to work with us."),
        VoiceLine(30, Trent , ru="Еще не согласился, но определенно заинтересовался.", en="Haven't agreed yet, but I'm definitely interested."),
        VoiceLine(40, Wilham, ru="Тогда присаживайтесь, я введу вас в курс дела. Только давайте договоримся, что вне зависимости от того чем закончится наш разговор, все его детали должны остаться между нами. Хорошо?", en="Then have a seat. I'll bring you up to speed. But let's agree that no matter how this conversation ends, every detail of it stays between us. All right?"),
        VoiceLine(50, Trent, ru="Должны - значит останутся. Любите вы, военные, жути нагнать...", en="If they must, they will. You military types love to spook people..."),
        VoiceLine(60, Wilham, ru="Тогда перейдём к делу. Силы Рейнланда проводят регулярный мониторинг ситуации в системе Омега-15. Один наш секретный агент добыл важные сведения и должен был доставить на полицейский аванпост в зоне рудокопов", en="Then let's get to business. Rheinland forces regularly monitor the situation in the Omega-15 system. One of our secret agents obtained important information and was supposed to deliver it to a police outpost in the miners' zone."),
        VoiceLine(70, Wilham, ru="Но по непонятной для нас причине он так и не добрался до указанного места встречи. Скорее всего он был перехвачен и убит.", en="But for a reason we don't understand, he never made it to the designated meeting place. Most likely he was intercepted and killed."),
        VoiceLine(80, Trent, ru="Сочувствую. Но при чем тут я?", en="I'm sorry. But what does that have to do with me?"),
        VoiceLine(90, Wilham, ru="Вашей задачей будет найти этот корабль и получить с него интересующие нас данные.", en="Your job will be to find that ship and get the data we're interested in off it."),
        VoiceLine(100, Wilham, ru="Вам в этом поможет наш внешний агент, электронщик-энтузиаст. Он работает в местной общие рудокопов.", en="Our outside agent will help you with that, an electronics enthusiast. He works in the local miners' community."),
        VoiceLine(110, Wilham, ru="Там он помогает рабочим находить астероиды с ценной рудой, а так же имеет все данные об обломках кораблей, которые могут быть нам интересны.", en="There he helps the workers find asteroids with valuable ore, and he also has all the data on ship wrecks that might interest us."),
        VoiceLine(120, Trent, ru="И всего делов-то? Могу приступать? ", en="That's all? Can I get started?"),

        VoiceLine(210, Wilham, ru='Не "могу", а "можем", герр Трент. В этом задании я буду приписан к вам в качестве напарника.', en="Not \"I can\", but \"we can\", Herr Trent. On this assignment I'll be attached to you as a partner."),
        VoiceLine(220, Trent, ru="Будете контролировать мои действия?", en="You'll be controlling my actions?"),
        VoiceLine(230, Wilham, ru="Нет. Буду осуществлять поддержку и взаимодействие с властями. Стратегия операции и тактика её проведения целиком на вас, герр Трент.", en="No. I'll provide support and handle contact with the authorities. The strategy of the operation, and the tactics of carrying it out, are entirely up to you, Herr Trent."),
        VoiceLine(240, Trent, ru="Спасибо за доверие... где поставить подпись?", en="Thanks for the trust... where do I sign?"),
        VoiceLine(250, Wilham, ru="Ха-ха-ха. Ну зачем нам эти условности? Встречаемся в космосе, герр Трент!", en="Ha-ha-ha. And why do we need these formalities? We'll meet in space, Herr Trent!"),
    ]


class Msn2Miner(Msn2, script.CutsceneProps):
    ALIAS = 'miner'
    TITLE = 'Рудокоп Матильда'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Trent, ru="Приветствую!", en="Greetings!"),
        VoiceLine(20, Jacobo, ru="Симметрично. Чему обязан?", en="Likewise. To what do I owe this?"),
        VoiceLine(30, Trent, ru="Вильгельму вы обязаны.", en="You owe it to Wilhelm."),
        VoiceLine(40, Jacobo, ru="Что есть -то есть. ", en="It is what it is."),
        VoiceLine(45, Jacobo, ru="И что же на этот раз понадобилось герру Вильгельму?", en="And what does Herr Wilhelm need this time?"),
        VoiceLine(50, Trent, ru="Координаты одного разбившегося корабля. ", en="Coordinates of one crashed ship."),
        VoiceLine(60, Jacobo, ru="А! Это проще простого. Я сейчас скину вам все точки происшествий с повреждением судов за прошедший месяц. Точность позиционирования плюс-минус двадцать миллиметров. Выбирайте что вам нужно, фильтруйте по критериям, спасибо говорить не нужно.", en="Ah! Nothing to it. I'll send you all the incident points with damaged ships from the past month. Positioning accuracy plus or minus twenty millimeters. Pick what you need, filter by criteria, no need to say thanks."),
        VoiceLine(70, Trent, ru="Мы вместе полетим.", en="We'll fly together."),
        VoiceLine(80, Jacobo, ru="Это зачем еще?", en="And why's that?"),
        VoiceLine(90, Trent, ru="Вильгельм сказал, ты должен мне указать на место интересующего нас события, а я должен его найти. А как я могу быть уверен, что ты не слил мне туфту, чтобы через полчаса свалить в закат? У военных свои причуды, а у фриленсеров - свои.", en="Wilhelm said you're supposed to point me to the site of the incident we're after, and I'm supposed to find it. And how can I be sure you didn't feed me junk so you can vanish into the sunset in half an hour? The military have their quirks, and freelancers have theirs."),
        VoiceLine(100, Jacobo, ru="Сотню раз уже проклял тот день когда согласился Вильгельму помогать.", en="I've already cursed the day I agreed to help Wilhelm a hundred times."),
        VoiceLine(110, Jacobo, ru="Сам-то он где сейчас? Сидит в баре на ближайшем торговом посту? ", en="And where is he himself right now? Sitting in a bar on the nearest trading post?"),
        VoiceLine(120, Jacobo, ru="Что бы ни случилось, он тут не при чем окажется, а вот мы с тобой главные фигуранты.", en="Whatever happens, he'll turn out to have nothing to do with it, and you and I will be the main ones implicated."),
    ]


class Msn2Done(Msn2, script.CutsceneProps):
    ALIAS = 'done'
    TITLE = 'Вознаграждение на линкоре'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Reichman, ru="А вот и сам знаменитый Трент.", en="And here's the famous Trent himself."),
        VoiceLine(20, Trent, ru="И чем же я так знаменит, мистер, эмм...", en="And what am I so famous for, mister, um..."),
        VoiceLine(30, Reichman, ru="Райхманн. Адмирал Райхманн, если позволите.", en="Reichmann. Admiral Reichmann, if I may."),
        VoiceLine(40, Trent, ru="Моё почтение, адмирал Райхманн! Так чем же я знаменит?", en="My respects, Admiral Reichmann! So what am I famous for?"),
        VoiceLine(50, Reichman, ru="О, мистер Трент, в последнее время в некоторых кругах только и разговоров, что о вас! Надеюсь, герр Вильгельм достойно оплачивает вашу работу?",
                  en="Oh, Mr. Trent, lately in certain circles you're all anyone talks about! I hope Herr Wilhelm pays you decently for your work?"),
        VoiceLine(60, Trent, ru="Не жалуюсь.", en="No complaints."),
        VoiceLine(70, Reichman, ru="Скромность - похвальная благодетель, герр Трент, но одной благодетелью сыт не будешь, ха-ха. Я распоряжусь, чтобы ваш гонорар за предыдущую миссию был удвоен. Всех благ, герр Трент!",
                  en="Modesty is a commendable virtue, Herr Trent, but virtue alone won't feed you, ha-ha. I'll see to it that your fee for the previous mission is doubled. All the best, Herr Trent!"),
        VoiceLine(80, Reichman, ru="Так вы считаете, что он - тот кто нам нужен?", en="So you believe he's the one we need?"),
        VoiceLine(90, Wilham, ru="Безусловно, герр Адмирал. Он - тот, кто поможет нам выполнить все известные вам задачи.",
                  en="Undoubtedly, Herr Admiral. He's the one who will help us carry out all the tasks known to you."),
        VoiceLine(100, Reichman, ru="И вы это гарантируете?", en="And you guarantee that?"),
        VoiceLine(110, Wilham, ru="Абсолютно!", en="Absolutely!"),
        VoiceLine(120, Reichman, ru="Хорошо, мы принимаем в работу ваш сценарий.", en="Good. We'll put your scenario into action."),
        VoiceLine(130, Wilham, ru="Благодарю за оказанное доверие.", en="Thank you for the trust you've placed in me."),
        VoiceLine(140, Reichman, ru="Посмотрим что из этого получится. Не смею задерживать, герр Вильгельм.", en="We'll see what comes of this. I won't keep you, Herr Wilhelm."),
    ]


class Msn2Space(Msn2, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(
            10,
            Wilham,
            ru="Мистер Трент, с вами говорит лейтенант Вильгельм. У нас есть для вас предложение о работе. Расскажу всё на личной встрече. Жду вас в баре линкора Шархорст, система Бисмарк.",
            en="Mr. Trent, this is Lieutenant Wilhelm. We have a job offer for you. I'll tell you everything in person. I'll be waiting in the bar of the battleship Scharnhorst, Bismarck system.",
        ),
        VoiceLine(
            30,
            Trent,
            ru="А зачем вам вообще фриленсеры? Вооруженные силы Рейнланда вполне способны сами решить любую проблему. Оцепили сектор, нашли обломки, изъяли данные...",
            en="And why do you need freelancers at all? The Rheinland armed forces are quite capable of solving any problem themselves. Cordon off the sector, find the wreckage, seize the data...",
        ),
        VoiceLine(
            40,
            Wilham,
            ru="Тем самым дезавуировали своего бывшего агента, выставили на всеобщее обозрение все свои интересы. ",
            en="And thereby disavowed your former agent, and put all your interests on public display.",
        ),
        VoiceLine(
            50,
            Wilham,
            ru="Работать с агентами не напрямую, а через сторонних лиц и независимые организации - это мудрость, идущая из глубины веков. Мы можем играть в игру, герр Трент, или не играть.",
            en="Working with agents not directly, but through third parties and independent organizations, is wisdom that comes from the depths of centuries. We can play the game, Herr Trent, or not play.",
        ),
        VoiceLine(
            55,
            Wilham,
            ru="Единственное что мы ОБЯЗАНЫ делать - это соблюдать правила. Кстати, одно из правил, герр Трент. Если вдруг с вами произойдет что-то неприятное, то мое ведомство ничего о вас не знает, а вы, в свою очередь, ничего не знаете о нём.",
            en="The only thing we are OBLIGED to do is follow the rules. By the way, one of the rules, Herr Trent. If something unpleasant should happen to you, my department knows nothing about you, and you, in turn, know nothing about it.",
        ),
        VoiceLine(
            60,
            Trent,
            ru="Ясно все с вами, работники ножа и топора, ох, извините, плаща и кинжала.",
            en="I see how it is with you people. Workers of the knife and the axe — oh, excuse me, cloak and dagger.",
        ),
        VoiceLine(
            70,
            Wilham,
            ru="Герр Трент, мы приближаемся к общине местных шахтеров, они добывают редкие металлы на астероидах. Интересующий нас человек находится на добывающем судне Матильда. Позывной - Джакобо.",
            en="Herr Trent, we're approaching the local miners' community. They extract rare metals from the asteroids. The man we're interested in is on the mining ship Matilda. Callsign — Jacobo.",
        ),
        VoiceLine(
            75,
            Wilham,
            ru="Просто передайте ему, что вы от Вильгельма. Мне светиться в этом секторе нельзя, тем более на этом корабле, поэтому я на время сойду со сцены.",
            en="Just tell him you're from Wilhelm. I can't show myself in this sector, especially on this ship, so I'll step off the stage for a while.",
        ),
        VoiceLine(
            1030,
            Jacobo,
            ru="Я переслал вам координаты ближайшего разбившегося корабля. Постарайтесь быстрее их осмотреть, у  нас не так много времени. ",
            en="I've sent you the coordinates of the nearest crashed ship. Try to inspect it quickly, we don't have much time.",
        ),
        VoiceLine(
            100,
            Trent,
            ru="Джакобо, а почему здесь так мусорщиков боятся? Собирают себе мусор - и пусть собирают, полезное дело делают.",
            en="Jacobo, why is everyone so afraid of the Junkers here? They collect garbage — let them collect it, they're doing useful work.",
        ),
        VoiceLine(
            110,
            Jacobo,
            ru="Бесконечно далеки вы от народа, мальчики из центральных систем. Изначально мусорщики занимались сбором мусора, сортировкой и продажей разных категорий отходов.",
            en="You boys from the central systems are a long way from ordinary people. Originally the Junkers collected garbage, sorted it, and sold different categories of waste.",
        ),
        VoiceLine(
            112,
            Jacobo,
            ru="И это было настолько прибыльно, что ряды мусорщиков в свое время росли не по дням а по часам. ",
            en="And it was so profitable that, in their day, the Junkers' ranks grew not by the day but by the hour.",
        ),
        VoiceLine(
            115,
            Jacobo,
            ru="Сейчас, например, они могут начать рассматривать в качестве мусора любой звездолет случайно попавший в их зону влияния и не имеющий должной охраны. Разберут его на составляющие и продадут в виде вторсырья.",
            en="Now, for example, they might start treating as garbage any starship that happens to enter their zone of influence and doesn't have proper protection. They'll take it apart and sell it as scrap.",
        ),
        VoiceLine(
            120,
            Jacobo,
            ru="Подошли к первой точке вероятного крушения.",
            en="We've reached the first likely crash point.",
        ),
        VoiceLine(
            130,
            Trent,
            ru="Начинаю сканировать...",
            en="Starting to scan...",
        ),
        VoiceLine(
            140,
            Trent,
            ru="Нет, не то.",
            en="No, not this.",
        ),
        VoiceLine(
            150,
            Jacobo,
            ru="Есть еще две точки с координатами разбившихся кораблей, которые могут стать интересующими нас объектами...",
            en="There are two more points with coordinates of crashed ships that might turn out to be what we're looking for...",
        ),
        VoiceLine(
            155,
            Jacobo,
            ru="Что за помехи? Что за помехи на радаре???",
            en="What's that interference? What's that interference on the radar???",
        ),
        VoiceLine(
            160,
            Trent,
            ru="Я полагаю, эти пять..., нет,  семь... девять... враждебных кораблей создают нам помехи. ",
            en="I suppose these five... no, seven... nine... hostile ships are causing the interference.",
        ),
        VoiceLine(
            170,
            OmegaJunkerOne,
            ru="О! А шо это шевелится на нашей территории?",
            en="Oh! And what's that moving on our territory?",
            cinematic=True,
        ),
        VoiceLine(
            180,
            OmegaJunkerTwo,
            ru="Металлолом какой-то...",
            en="Some scrap metal...",
            cinematic=True,
        ),
        VoiceLine(
            190,
            OmegaJunkerThree,
            ru="Ну вот, опять сортировать мусор.",
            en="Well, sorting garbage again.",
            cinematic=True,
        ),
        VoiceLine(
            200,
            OmegaJunkerOne,
            ru="Да шо вы переживаете, там дел-то на пять минут.",
            en="What are you worrying about? It's five minutes' work.",
            cinematic=True,
        ),
        VoiceLine(
            210,
            Jacobo,
            ru="Трент - возможно это тот корабль, который вы искали, сканируйте.",
            en="Trent — this might be the ship you were looking for. Scan it.",
        ),
        VoiceLine(
            230,
            Trent,
            ru="Бинго! Тот самый корабль. Считываю данные с бортового журнала...",
            en="Bingo! That's the ship. Reading the data from the ship's log...",
        ),
        VoiceLine(
            240,
            Trent,
            ru="Все. Можем возвращаться. ",
            en="Done. We can head back.",
        ),
        VoiceLine(
            250,
            Jacobo,
            ru="Трент, ты же наёмник? А наемник работает в принципе на любого, кто платит за услуги?",
            en="Trent, you're a mercenary, right? And a mercenary, in principle, works for anyone who pays for the service?",
        ),
        VoiceLine(
            260,
            Trent,
            ru="Не на любого, но в принципе, да, это мой хлеб.",
            en="Not just anyone, but in principle, yes, that's my living.",
        ),
        VoiceLine(
            270,
            Jacobo,
            ru="А сможешь поработать на меня, если придется?",
            en="And could you work for me, if it comes to that?",
        ),
        VoiceLine(
            280,
            Trent,
            ru="Конечно!",
            en="Of course!",
        ),
        VoiceLine(
            290,
            Jacobo,
            ru="Тогда я обсужу это со знакомыми шахтерами. И если ты не против, мы хотели бы нанять тебя.",
            en="Then I'll discuss it with some miners I know. And if you don't mind, we'd like to hire you.",
        ),
        VoiceLine(
            300,
            Trent,
            ru="Да не вопрос.",
            en="Yeah, no problem.",
        ),
        VoiceLine(
            310,
            Wilham,
            ru="герр Трент, встречаемся у гиперврат в систему Бисмарк.",
            en="Herr Trent, let's meet at the jump gate to the Bismarck system.",
        ),
        VoiceLine(
            320,
            Wilham,
            ru="Мы рады, что вы смогли выполнить миссию. Пожалуйста, передайте данные Карателю 1.",
            en="We're glad you were able to complete the mission. Please transfer the data to Punisher 1.",
        ),
        VoiceLine(
            330,
            Trent,
            ru="Вильгельм, НАПАРНИК, а ты не мог помочь мне в бою с мусорщиками когда я получал эти ваши сверхсекретные данные?",
            en="Wilhelm, PARTNER, couldn't you have helped me in the fight with the Junkers while I was getting that top-secret data of yours?",
        ),
        VoiceLine(
            340,
            Wilham,
            ru="Нет, это выходило за рамки моей компетенции.",
            en="No, that was outside my competence.",
        ),
        VoiceLine(
            350,
            Punisher,
            ru="Внимание, это каратель - 1! Нами обнаружен нелегальный склад оружия, находящийся в облаке Майсен.",
            en="Attention, this is Punisher-1! We have located an illegal weapons depot in the Maisen cloud.",
        ),
        VoiceLine(
            360,
            Wilham,
            ru="Передавайте координаты! Трент, не хочешь поучаствовать в операции федерального масштаба? ",
            en="Send the coordinates! Trent, don't you want to take part in a federal-scale operation?",
        ),
        VoiceLine(
            370,
            Trent,
            ru="А у меня есть выбор?",
            en="Do I have a choice?",
        ),
        VoiceLine(
            380,
            Wilham,
            ru="Ха-ха-ха! Нет!",
            en="Ha-ha-ha! No!",
        ),
        VoiceLine(
            390,
            Trent,
            ru="Тогда, пожалуй, поучаствую!",
            en="Then I suppose I'll take part!",
        ),
        VoiceLine(
            1050,
            Punisher,
            ru="Склад обнаружен. Вижу противника!",
            en="Depot located. I see the enemy!",
        ),
        VoiceLine(
            1060,
            Wilham,
            ru="Каратель-4, на вас грузовики. Остановите их! Остальным – уничтожать истребители.",
            en="Punisher-4, the transports are yours. Stop them! Everyone else — destroy the fighters.",
        ),
        VoiceLine(
            1070,
            PunisherCatcher,
            ru="Вас понял, выполняю.",
            en="Understood, executing.",
        ),
        VoiceLine(
            410,
            Wilham,
            ru="Каратель- 4, что там с грузовиками?",
            en="Punisher-4, what's going on with the transports?",
        ),
        VoiceLine(
            420,
            PunisherCatcher,
            ru="Грузовики продолжают движение. Нет, стоп, грузовики остановились! Грузовики остановились!",
            en="The transports are still moving. No, wait, the transports have stopped! The transports have stopped!",
        ),
        VoiceLine(
            430,
            PunisherCatcher,
            ru="База! Вижу базу!",
            en="A base! I see a base!",
        ),
        VoiceLine(
            440,
            Wilham,
            ru="Каратели, входим в зону действия!",
            en="Punishers, we're entering the engagement zone!",
        ),
        VoiceLine(
            450,
            Wilham,
            ru="Трент!!! Приказ оказывать поддержку звену Карателей! Атакуй оружейные платформы!!!",
            en="Trent!!! Order is to support the Punisher flight! Attack the weapon platforms!!!",
        ),
        VoiceLine(
            1080,
            Wilham,
            ru="Отлично, герр Трент, осталась еще одна.",
            en="Excellent, Herr Trent, there's still one left.",
        ),
        VoiceLine(
            1090,
            Wilham,
            ru="Каратель-1, мы готовы к ликвидации базы?",
            en="Punisher-1, are we ready to destroy the base?",
        ),
        VoiceLine(
            1100,
            Punisher,
            ru="Никак нет. Здесь слишком много кораблей противника.",
            en="Negative. There are too many enemy ships here.",
        ),
        VoiceLine(
            1110,
            Wilham,
            ru="Вас понял. Трент, разберитесь с оставшимися корсарами.",
            en="Understood. Trent, deal with the remaining Corsairs.",
        ),
        VoiceLine(
            1120,
            Punisher,
            ru="Сектор чист, торпеды готовы к запуску!",
            en="Sector clear, torpedoes ready to launch!",
        ),
        VoiceLine(
            1130,
            Wilham,
            ru="Объект уничтожен, миссия выполнена. Каратели, оцепите район и изучите останки базы. Герр Трент, следуйте на Шарнхорст.",
            en="Target destroyed, mission complete. Punishers, cordon off the area and examine the remains of the base. Herr Trent, proceed to the Scharnhorst.",
        ),
        VoiceLine(
            460,
            Wilham,
            ru="Мне только что передали, герр Трент, что с вами хочет пообщаться один из адмиралов Рейнланда.",
            en="I've just been informed, Herr Trent, that one of Rheinland's admirals wants to speak with you.",
        ),
        VoiceLine(
            470,
            Trent,
            ru="И много у вас адмиралов?",
            en="And do you have many admirals?",
        ),
        VoiceLine(
            480,
            Wilham,
            ru="По пальцам одной руки можно пересчитать. Тебе оказали большую честь.",
            en="You can count them on the fingers of one hand. You've been shown a great honor.",
        ),
        VoiceLine(
            490,
            Trent,
            ru="Охренеть. Будет что вспомнить в старости.",
            en="Holy shit. Something to remember in my old age.",
        ),
        VoiceLine(
            1140,
            Wilham,
            ru="Герр Трент, вы первый.",
            en="Herr Trent, you first.",
        ),
        VoiceLine(
            7000,
            Neuralnet,
            ru="Чтобы получ+ить д+оступ на рудок+оп, вы должн+ы доб+ыть кл+юч. Кл+юч м+ожно доб+ыть в астер+оидах. Атак+уйте вн+утренние п+олости ближ+айших астер+оидов сво+ими п+ушками.",
            en='To get access to the miner, you must obtain a key. The key can be obtained in the asteroids. Attack the inner cavities of the nearest asteroids with your guns.',
        ),
        VoiceLine(
            7010,
            Neuralnet,
            ru="+Если п+олость астер+оида разр+ушилась с зел+ёным взр+ывом, зн+ачит с астер+оида м+ожно доб+ыть кл+юч.",
            en='If an asteroid cavity is destroyed with a green explosion, that means a key can be obtained from that asteroid.',
        ),
        VoiceLine(
            7020,
            Neuralnet,
            ru="Уничтошьте все п+олости +этого астер+оида до тех пор, пока ключ не в+ыпадет. Д+оступ к ст+анции б+удет откр+ыт ср+азу же, как т+олько вы забер+ёте ключ в свой трюм.",
            en='Destroy all the cavities of this asteroid until the key falls out. Access to the station will open as soon as you take the key into your cargo hold.',
        ),
        VoiceLine(
            7030,
            Neuralnet,
            ru="Если п+олость астер+оида была разрушена с б+елым взр+ывом, то на этом астер+оиде не б+удет ключ+а. Вы должн+ы будете направиться к сл+едующему астер+оиду и попр+обовать сн+ова.",
            en="If an asteroid cavity was destroyed with a white explosion, there will be no key on this asteroid. You will have to go to the next asteroid and try again.",
        ),
        VoiceLine(
            7040,
            Neuralnet,
            ru="В Секторе Сириуса различные станции нужно взламывать различными способами. "
               "Чтобы получить информацию о методике взлома обратитесь к инфокарте взламываемого объекта.",
            en="In the Sirius Sector, different stations have to be hacked in different ways. For information on the hacking method, consult the infocard of the object you are hacking.",
        ),
    ]


class Mission2(Msn2, script.StoryMission):
    MISSION_INDEX = 2
    CUTSCENES = [
        Msn2Offer,
        Msn2Miner,
        Msn2Done,
    ]
    SPACE_CLASS = Msn2Space
    SYNC_SPACE = True
    SYNC_SUBS = True

    MISSION_TITLE = 'Миссия 2. Мусорная работа'