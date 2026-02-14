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
        VoiceLine(10, Trent , ru="Вильгельм, я полагаю?", en="Wilhelm, I assume?"),
        VoiceLine(20, Wilham, ru="Так точно, герр Трент. Я рад, что вы согласились с нами работать.", en="Indeed, Herr Trent. I'm glad that you've chosen to work with us."),
        VoiceLine(30, Trent , ru="Еще не согласился, но определенно заинтересовался. Не каждый день представители вооруженных сил Рейнланда присылают мне сообщения на КПК с предложением личной встречи на борту линкора вооруженных сил Рейнланда.", en="I haven't agreed yet, but I'm definitely interested. It's not every day that a representative of the Rheinland military messages my PDA, with a proposal to meet in person, on board a Rheinland military battleship."),
        VoiceLine(40, Wilham, ru="Это вы о каких сообщениях?", en="Which messages are you referring to?"),
        VoiceLine(50, Trent, ru="Ну вот же... Черт. Что такое? Оно только что было...", en="These ones... Shit. What's going on? They were right there..."),
        VoiceLine(60, Wilham, ru="Да черт с ними, с сообщениями, герр Трент, давайте лучше о деле. И да, надеюсь, вы понимаете, что вне зависимости от того чем закончится наш разговор, все его детали должны остаться между нами?", en="To hell with those messages, Herr Trent, let's get to the point. And so, I hope you understand, that regardless of how our conversation ends, all its details should remain between us?"),
        VoiceLine(70, Trent, ru="Должны - значит останутся. Любите вы, военные, жути нагнать... Кстати, а почему именно я?", en="Should - means they would. You military guys don't like messing around... By the way, why me?"),
        VoiceLine(80, Wilham, ru="А почему бы и нет? Вы неплохо показали себя в инциденте у аванпоста Бранденбург.", en="Why not? You proved yourself well in the Brandenburg Outpost incident."),
        VoiceLine(90, Trent, ru="Понятно. Перейдем к сути задания?", en="Gotcha. Let's get to the mission, shall we?"),
        VoiceLine(100, Wilham, ru="Перейдем. Как и любое другое государство, мы имеем ряд информаторов на территории, скажем так, наших геополитических соперников. Понимаете о чем я?", en="Alright. Like any other government, we have some informants in territories of our, let's say, geopolitical rivals. You understand?"),
        VoiceLine(110, Trent, ru="О да.", en="Sure."),
        VoiceLine(120, Wilham, ru="Так вот, некоторое время назад один из информаторов вышел на связь по условленному каналу, сообщил, что имеет информацию крайней степени важности и вылетел на своем корабле в условленную точку для передачи данных. И в лучших традициях детективов в точке этой так и не появился. Не обозначил он своего присутствия в течении недели и по месту внедрения, и по аварийным каналам. Это может означать лишь одно - он мертв. ", en="Very well. Not so long ago, one of our informants contacted us via secure channel, reporting that he had extremely critical information and headed to our dedicated data transmission point. And, as traditional detective stories go, he never arrived there. No sign received from him during the last week, neither in the transmission point, nor through emergency channels. It can only mean one thing - he is dead."),
        VoiceLine(130, Wilham, ru="На основании анализа переговоров диспетчеров станций и операторов экстренных служб в интересующем нас районе с вероятностью более девяноста девяти процентов установлено что корабль нашего информатора был атакован, а сам он погиб.", en="Based on the analysis of chatter between station dispatchers and operators of emergency services in the area of our interest, with a probability of over ninety-nine percent, we've established that the ship of our informant was attacked, and he was killed."),
        VoiceLine(140, Trent, ru="Сочувствую. Но при чем тут я?", en="My condolences. But what do I have to do with it?"),
        VoiceLine(150, Wilham, ru="Вашей задачей будет найти этот корабль и снять с него интересующие нас данные. Сделать это необходимо как можно скорее, так как в данном районе активность так называемых мусорщиков, чрезвычайно высока. Вы должны их опередить.", en="Your mission is to find that ship and remove the data of interest from it. It has to be done as soon as possible, since the activity of so-called \"Junkers\" in the area is extremely high. You have to get ahead of them."),
        VoiceLine(160, Trent, ru="Я вряд ли смогу их опередить. Во-первых я толком не знаю эту область в отличии от них, а во-вторых, опять же в отличии от них я буду действовать один.", en="I doubt that I can get ahead of them. First of all, I don't know the area as well as they do. Secondly, unlike them, I'll be there on my own."),
        VoiceLine(170, Wilham, ru="Сможете. Дело в том, что есть один электронщик-энтузиаст, который занимается разработкой систем слежения и трекинга радиопереговоров. Мы давно заинтересованы в том, чтобы переманить его в наше ведомство, поэтому внимательно за ним наблюдаем.", en="You can. The thing is, there's a tech enthusiast who's developing devices that can track them and listen to their radio comms. We've been interested in luring him into our department for a while now, so we're closely watching him."),
        VoiceLine(180, Trent, ru="Как за мной?", en="Like you're watching me?"),
        VoiceLine(190, Wilham, ru="Еще пристальнее. Так вот все свои системы он тестирует как раз на интересующем нас районе. Таким образом, у него есть самая полная информация обо всем что произошло в интересующем нас секторе космоса за последнее время. Вам нужно будет связаться с ним, договориться о передаче координат крушения корабля нашего информатора, снять с него данные и передать их нам... естественно не позволив мусорщикам добраться до них раньше.", en="Even closer. He's been testing his devices in our area of interest. Therefore, he has the best intel regarding every event that recently occurred in that area of space. You'll have to get in touch with him, make an arrangement to get the informant's ship's wreckage coordinates, remove the data from it, and transfer it to us... Without letting any scavenger get to it before you do, naturally."),
        VoiceLine(200, Trent, ru="И всего делов-то? Могу приступать? ", en="And that's it? Can I start now?"),
        VoiceLine(210, Wilham, ru='Если вы согласны, то не "могу", а "можем". В этом задании я буду приписан к вам в качестве напарника.', en="If you agree, there's no \"I\", but a \"We\". I'll be assigned as your partner for the duration of this mission."),
        VoiceLine(220, Trent, ru="Будете контролировать мои действия?", en="Will you be in control of my actions?"),
        VoiceLine(230, Wilham, ru="Нет. Буду осуществлять поддержку и взаимодействие с властями - у меня достаточно высокий допуск в системах Райнланда. Стратегия операции и тактика её проведения целиком на вас, герр Трент.", en="No. I'll be your wingman and help you interact with the authorities - I have a fairly high level of clearance in Rheinland systems. The strategical and tactical sides of this operation are entirely on you, Herr Trent."),
        VoiceLine(240, Trent, ru="Спасибо за доверие... где поставить подпись?", en="Thanks for trusting me... Where do I sign?"),
        VoiceLine(250, Wilham, ru="Ха-ха-ха. Ну зачем нам эти условности? Встречаемся в космосе, герр Трент!", en="Ha-ha-ha. Why would we require such formalities? I'll meet you in space, Herr Trent!"),
    ]


class Msn2Miner(Msn2, script.CutsceneProps):
    ALIAS = 'miner'
    TITLE = 'Рудокоп Матильда'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Trent, ru="Приветствую!", en="Greetings!"),
        VoiceLine(20, Jacobo, ru="Симметрично. Чему обязан?", en="Likewise. What'cha need?"),
        VoiceLine(30, Trent, ru="Вильгельму вы обязаны.", en="Wilhelm sent me."),
        VoiceLine(40, Jacobo, ru="Что есть -то есть. ", en="Very well."),
        VoiceLine(45, Jacobo, ru="И что же на этот раз понадобилось герру Вильгельму?", en="And what does Herr Wilhelm need this time?"),
        VoiceLine(50, Trent, ru="Координаты одного разбившегося корабля. ", en="Coordinates of some wrecked ship."),
        VoiceLine(60, Jacobo, ru="А! Это проще простого. Я сейчас скину вам все точки происшествий с повреждением судов за прошедший месяц. Точность позиционирования плюс-минус двадцать миллиметров. Выбирайте что вам нужно, фильтруйте по критериям, спасибо говорить не нужно.", en="Ah! Piece of cake. I'll throw in all the points of accidents involving damage to ships over the past month. Accuracy of twenty millimeters, give or take a few. Choose the one you need, filtered by criteria. No need to thank me."),
        VoiceLine(70, Trent, ru="Мы вместе полетим.", en="We'll fly there together."),
        VoiceLine(80, Jacobo, ru="Это зачем еще?", en="And why's that?"),
        VoiceLine(90, Trent, ru="Вильгельм сказал, ты должен мне указать на место интересующего нас события, а я должен его найти. А как я могу быть уверен, что ты не слил мне туфту, чтобы через полчаса свалить в закат? У военных свои причуды, а у фриленсеров - свои.", en="Wilhelm said that you'll point me to the place of our interest, and I'll have to find it. And how can I possibly know that you're not bullshitting me, to make a half-an-hour trip last till dawn? The military has their own quirks, and so does the freelancer."),
        VoiceLine(100, Jacobo, ru="Сотню раз уже проклял тот день когда согласился Вильгельму помогать.", en="A hundred times I curse the day I agreed to help Wilhelm."),
        VoiceLine(110, Jacobo, ru="Сам-то он где сейчас? Сидит в баре на ближайшем торговом посту? ", en="And where's he now? Chilling in a bar on a nearby trading outpost?"),
        VoiceLine(120, Jacobo, ru="Что бы ни случилось, он тут не при чем окажется, а вот мы с тобой главные фигуранты.", en="Whatever happens out there, he has nothing to do with it, while you and I are the main characters."),
    ]


class Msn2Done(Msn2, script.CutsceneProps):
    ALIAS = 'done'
    TITLE = 'Вознаграждение на линкоре'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Reichman, ru="А вот и сам знаменитый Трент.", en="So here's the famous Trent."),
        VoiceLine(20, Trent, ru="И чем же я так знаменит, мистер, эмм...", en="And what am I so famous for, Mr... Umm..."),
        VoiceLine(30, Reichman, ru="Райхманн. Адмирал Райхманн, если позволите.", en="Reichmann. Admiral Reichmann, if you may."),
        VoiceLine(40, Trent, ru="Моё почтение, адмирал Райхманн! Так чем же я знаменит?", en="It's my honor, Admiral Reichmann! So, what am I so famous for?"),
        VoiceLine(50, Reichman, ru="О, мистер Трент, в последнее время в некоторых кругах только и разговоров, что о вас! Надеюсь, герр Вильгельм достойно оплачивает вашу работу?",
                  en="Oh, Herr Trent, lately some of the higher circles have all been talking about you! I hope Herr Wilhelm adequately pays for your work."),
        VoiceLine(60, Trent, ru="Не жалуюсь.", en="I'm not complaining."),
        VoiceLine(70, Reichman, ru="Скромность - похвальная благодетель, герр Трент, но одной благодетелью сыт не будешь, ха-ха. Я распоряжусь, чтобы ваш гонорар за предыдущую миссию был удвоен. Всех благ, герр Трент!",
                  en="Modesty - a commendable virtue, Herr Trent, I see virtue often taken for granted. I'll make sure the payment for your last mission will be doubled. All the best to you, Herr Trent!"),
        VoiceLine(80, Reichman, ru="Так вы считаете, что он - тот кто нам нужен?", en="So you think that he's the one we need?"),
        VoiceLine(90, Wilham, ru="Безусловно, герр Адмирал. Он - тот, кто поможет нам выполнить все известные вам задачи.",
                  en="Undoubtedly, Herr Admiral. He's the one who can help us accomplish all our tasks at hand."),
        VoiceLine(100, Reichman, ru="И вы это гарантируете?", en="Can you guarantee that?"),
        VoiceLine(110, Wilham, ru="Абсолютно!", en="Absolutely!"),
        VoiceLine(120, Reichman, ru="Хорошо, мы принимаем в работу ваш сценарий.", en="Very well, We execute your plan."),
        VoiceLine(130, Wilham, ru="Благодарю за оказанное доверие.", en="Thank you for your trust."),
        VoiceLine(140, Reichman, ru="Посмотрим что из этого получится. Не смею задерживать, герр Вильгельм.", en="We will see what comes out of that. You're dismissed, Herr Wilhelm."),
    ]


class Msn2Space(Msn2, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(
            30,
            Trent,
            ru="А зачем вам вообще фриленсеры? Вооруженные силы Рейнланда вполне способны сами решить любую проблему. Оцепили сектор, нашли обломки, изъяли данные...",
            en="Why do you need freelancers? The Rheinland military is fully capable of solving any problem of such. Search the sector, find the wreckage, download the data...",
        ),
        VoiceLine(
            40,
            Wilham,
            ru="Тем самым дезавуировали своего бывшего агента, выставили на всеобщее обозрение все свои интересы. ",
            en="That's exactly how we lost our former agent, exposing our interests to the public eye.",
        ),
        VoiceLine(
            45,
            Wilham,
            ru="Не говоря уже о том, что интересующая нас область находится вне юрисдикции Рейнланда. И кто согласился бы с нами работать после того, как мы устроили подобный цирк?",
            en="Not mentioning the fact that our area of interest is located outside of Rheinland's jurisdiction. And who'd ever agree to work with us, after all this circus?",
        ),
        VoiceLine(
            50,
            Wilham,
            ru="Работать с агентами не напрямую, а через сторонних лиц и независимые организации - это мудрость, идущая из глубины веков. Мы можем играть в игру, герр Трент, или не играть.",
            en="Working with agents indirectly, but rather through third-parties and independent organizations, is an age-old best practice. We can either play the game, Herr Trent, or not.",
        ),
        VoiceLine(
            55,
            Wilham,
            ru="Единственное что мы ОБЯЗАНЫ делать - это соблюдать правила. Кстати, одно из правил, герр Трент. Если вдруг с вами произойдет что-то неприятное, то мое ведомство ничего о вас не знает, а вы, в свою очередь, ничего не знаете о нём.",
            en="The only thing we absolutely MUST do – is follow the rules. By the way, that's one of the rules, Herr Trent: If something unpleasant happens to you, then my department knows nothing about you, and in turn, you know nothing about it.",
        ),
        VoiceLine(
            60,
            Trent,
            ru="Ясно все с вами, работники ножа и топора, ох, извините, плаща и кинжала.",
            en="It's all clear with you, workers of the knife and axe. Oh, sorry, of cloak and dagger.",
        ),
        VoiceLine(
            70,
            Wilham,
            ru="Герр Трент, мы приближаемся к общине местных шахтеров, они добывают редкие металлы на астероидах. Интересующий нас человек находится на добывающем судне Матильда. Позывной - Джакобо.",
            en="Herr Trent, we're approaching a local miners community. They mine rare metals on asteroids. The person of our interest is aboard the mining ship named Matilda. Callsign - Jacobo.",
        ),
        VoiceLine(
            75,
            Wilham,
            ru="Просто передайте ему, что вы от Вильгельма. Мне светиться в этом секторе нельзя, тем более на этом корабле, поэтому я на время сойду со сцены.",
            en="Just tell him Wilhelm sent you. I must not stand out in this area, especially with this ship, so I'll leave the stage for now.",
        ),
        VoiceLine(
            1030,
            Jacobo,
            ru="Я переслал вам координаты ближайшего разбившегося корабля. Постарайтесь быстрее их осмотреть, у  нас не так много времени. ",
            en="I've sent you the coordinates of the nearest crashed ship. Try to scan them as fast as you can, we don't have much time.",
        ),
        VoiceLine(
            100,
            Trent,
            ru="Джакобо, а почему здесь так мусорщиков боятся? Собирают себе мусор - и пусть собирают, полезное дело делают.",
            en="Jacobo, why's everyone so scared of Junkers around here? They're collecting garbage – so let them do their good work for the community.",
        ),
        VoiceLine(
            110,
            Jacobo,
            ru="Бесконечно далеки вы от народа, мальчики из центральных систем. Изначально мусорщики занимались сбором мусора, сортировкой и продажей разных категорий отходов.",
            en="You central system boys are infinitely far from civilization. At first, the Junkers were engaged in garbage collection, sorting and selling different categories of junk.",
        ),
        VoiceLine(
            112,
            Jacobo,
            ru="И это было настолько прибыльно, что ряды мусорщиков в свое время росли не по дням а по часам. ",
            en="And it was so profitable, that Junker units were multiplying not by the day, but by the hour.",
        ),
        VoiceLine(
            115,
            Jacobo,
            ru="Сейчас, например, они могут начать рассматривать в качестве мусора любой звездолет случайно попавший в их зону влияния и не имеющий должной охраны. Разберут его на составляющие и продадут в виде вторсырья.",
            en="Now, for example, their definition of junk could include any spaceship making its way through their area of influence without proper escort. They'll tear it down to pieces and sell it in form of recycled components.",
        ),
        VoiceLine(
            120,
            Jacobo,
            ru="Подошли к первой точке вероятного крушения.",
            en="We've reached the first potential crash site.",
        ),
        VoiceLine(
            130,
            Trent,
            ru="Начинаю сканировать...",
            en="Commencing a scan...",
        ),
        VoiceLine(
            140,
            Trent,
            ru="Нет, не то.",
            en="Nope, not it.",
        ),
        VoiceLine(
            150,
            Jacobo,
            ru="Есть еще две точки с координатами разбившихся кораблей, которые могут стать интересующими нас объектами...",
            en="There are two more points with crash site coordinates, which could contain our object of interest...",
        ),
        VoiceLine(
            155,
            Jacobo,
            ru="Что за помехи? Что за помехи на радаре???",
            en="What's that? What's with the radar interference???",
        ),
        VoiceLine(
            160,
            Trent,
            ru="Я полагаю, эти пять..., нет,  семь... девять... враждебных кораблей создают нам помехи. ",
            en="I think there are five… No, seven… Nine… Hostile ships on an interception course.",
        ),
        VoiceLine(
            170,
            OmegaJunkerOne,
            ru="О! А шо это шевелится на нашей территории?",
            en="Oh! What's that, fiddling in our territory?",
            cinematic=True,
        ),
        VoiceLine(
            180,
            OmegaJunkerTwo,
            ru="Металлолом какой-то...",
            en="Some kind of scrap metal...",
            cinematic=True,
        ),
        VoiceLine(
            190,
            OmegaJunkerThree,
            ru="Ну вот, опять сортировать мусор.",
            en="Here we go again, sorting junk.",
            cinematic=True,
        ),
        VoiceLine(
            200,
            OmegaJunkerOne,
            ru="Да шо вы переживаете, там дел-то на пять минут.",
            en="Don't worry, it'll only take five minutes.",
            cinematic=True,
        ),
        VoiceLine(
            210,
            Jacobo,
            ru="Трент - возможно это тот корабль, который вы искали, сканируйте.",
            en="Trent – this could be the chip you're looking for. Scan it.",
        ),
        VoiceLine(
            230,
            Trent,
            ru="Бинго! Тот самый корабль. Считываю данные с бортового журнала...",
            en="Bingo! That's out ship.",
        ),
        VoiceLine(
            240,
            Trent,
            ru="Все. Можем возвращаться. ",
            en="Done. We can go back now.",
        ),
        VoiceLine(
            250,
            Jacobo,
            ru="Трент, ты же наёмник? А наемник работает в принципе на любого, кто платит за услуги?",
            en="Trent, you're a freelancer right? And technically, freelancers work for anyone who pays.",
        ),
        VoiceLine(
            260,
            Trent,
            ru="Не на любого, но в принципе, да, это мой хлеб.",
            en="Not anyone, but technically, yeah. That's my bread.",
        ),
        VoiceLine(
            270,
            Jacobo,
            ru="А сможешь поработать на меня, если придется?",
            en="Would you work for me, if I ever need anything?",
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
            en="Then I'll discuss that with some miner friends of mine, and if you don't mind, we'd like to hire you.",
        ),
        VoiceLine(
            300,
            Trent,
            ru="Да не вопрос.",
            en="It'll be my pleasure.",
        ),
        VoiceLine(
            310,
            Wilham,
            ru="герр Трент, встречаемся у гиперврат в систему Бисмарк.",
            en="Herr Trent, meet me at the jump gate to Bismarck.",
        ),
        VoiceLine(
            320,
            Wilham,
            ru="Мы рады, что вы смогли выполнить миссию. Пожалуйста, передайте данные Карателю 1.",
            en="We're glad that you could make it through the mission. Please, transfer the data to Punisher 1.",
        ),
        VoiceLine(
            330,
            Trent,
            ru="Вильгельм, НАПАРНИК, а ты не мог помочь мне в бою с мусорщиками когда я получал эти ваши сверхсекретные данные?",
            en="Wilhelm, my PARTNER, could you really not help me fight off the Junkers when I collected your top secret data?",
        ),
        VoiceLine(
            340,
            Wilham,
            ru="Нет, это выходило за рамки моей компетенции.",
            en="No, it was beyond my level of expertise.",
        ),
        VoiceLine(
            350,
            Punisher,
            ru="Внимание, это каратель - 1! Нами обнаружен нелегальный склад оружия, находящийся в облаке Майсен.",
            en=", this is Punisher-1! We've discovered an illegal weapon storage facility, located in the Maison cloud.",
        ),
        VoiceLine(
            360,
            Wilham,
            ru="Передавайте координаты! Трент, не хочешь поучаствовать в операции федерального масштаба? ",
            en="Send us coordinates! Trent, would you like to participate in a federal-scale operation?",
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
            en="Then I'd very much like to!",
        ),
        VoiceLine(
            1050,
            Punisher,
            ru="Склад обнаружен. Вижу противника!",
            en="Storage facility located. Bogies inbound!",
        ),
        VoiceLine(
            1060,
            Wilham,
            ru="Каратель-4, на вас грузовики. Остановите их! Остальным – уничтожать истребители.",
            en="Punisher-4, the transports are heading your way. Stop them! Everyone else – destroy the fighters.",
        ),
        VoiceLine(
            1070,
            PunisherCatcher,
            ru="Вас понял, выполняю.",
            en="Roger that, on my way.",
        ),
        VoiceLine(
            410,
            Wilham,
            ru="Каратель- 4, что там с грузовиками?",
            en="Punisher-4, what about the transports?",
        ),
        VoiceLine(
            420,
            PunisherCatcher,
            ru="Грузовики продолжают движение. Нет, стоп, грузовики остановились! Грузовики остановились!",
            en="The transports are on the move. No, wait, they've stopped! The transports have stopped!",
        ),
        VoiceLine(
            430,
            PunisherCatcher,
            ru="База! Вижу базу!",
            en="A base! I see corsair base!",
        ),
        VoiceLine(
            440,
            Wilham,
            ru="Каратели, входим в зону действия!",
            en="Punishers, let's get moving!",
        ),
        VoiceLine(
            450,
            Wilham,
            ru="Трент!!! Приказ оказывать поддержку звену Карателей! Атакуй оружейные платформы!!!",
            en="Trent!!! Your order is to assist the Punisher wing!Attack the weapon platforms!!!",
        ),
        VoiceLine(
            1080,
            Wilham,
            ru="Отлично, герр Трент, осталась еще одна.",
            en="Excellent, Herr Trent, only one left.",
        ),
        VoiceLine(
            1090,
            Wilham,
            ru="Каратель-1, мы готовы к ликвидации базы?",
            en="Punisher-1, are we ready to liquidate the base?",
        ),
        VoiceLine(
            1100,
            Punisher,
            ru="Никак нет. Здесь слишком много кораблей противника.",
            en="Not yet. There are too many enemy ships.",
        ),
        VoiceLine(
            1110,
            Wilham,
            ru="Вас понял. Трент, разберитесь с оставшимися корсарами.",
            en="Roger that. Trent, you take care of the rest of them.",
        ),
        VoiceLine(
            1120,
            Punisher,
            ru="Сектор чист, торпеды готовы к запуску!",
            en="Area clear, torpedoes ready to launch!",
        ),
        VoiceLine(
            1130,
            Wilham,
            ru="Объект уничтожен, миссия выполнена. Каратели, оцепите район и изучите останки базы. Герр Трент, следуйте на Шарнхорст.",
            en="Objective destroyed, mission accomplished. Punishers, scout the area and inspect the base's debris. Herr Trent, follow me to Scharnhorst.",
        ),
        VoiceLine(
            460,
            Wilham,
            ru="Мне только что передали, герр Трент, что с вами хочет пообщаться один из адмиралов Рейнланда.",
            en="I just received the message, Herr Trent, that one of Rheinland's admirals would like to talk to you.",
        ),
        VoiceLine(
            470,
            Trent,
            ru="И много у вас адмиралов?",
            en="Do you have lots of admirals?",
        ),
        VoiceLine(
            480,
            Wilham,
            ru="По пальцам одной руки можно пересчитать. Тебе оказали большую честь.",
            en="You can count them with one hand. You're being greatly honored.",
        ),
        VoiceLine(
            490,
            Trent,
            ru="Охренеть. Будет что вспомнить в старости.",
            en="Will I live… That's something to remember when I'm old.",
        ),
        VoiceLine(
            1140,
            Wilham,
            ru="Герр Трент, вы первый.",
            en="Herr Trent, you go first.",
        ),
        VoiceLine(
            7000,
            Neuralnet,
            ru="Чтобы получ+ить д+оступ на рудок+оп, вы должн+ы доб+ыть кл+юч. Кл+юч м+ожно доб+ыть в астер+оидах. Атак+уйте вн+утренние п+олости ближ+айших астер+оидов сво+ими п+ушками.",
            en='To get access to roid miner you must get the key. You can mine key inside asteroids. Attack internal sides of nearest asterods by your guns.',
        ),
        VoiceLine(
            7010,
            Neuralnet,
            ru="+Если п+олость астер+оида разр+ушилась с зел+ёным взр+ывом, зн+ачит с астер+оида м+ожно доб+ыть кл+юч.",
            en='If side was destroyed with green color, it means this asteroid contains a key',
        ),
        VoiceLine(
            7020,
            Neuralnet,
            ru="Уничтошьте все п+олости +этого астер+оида до тех пор, пока ключ не в+ыпадет. Д+оступ к ст+анции б+удет откр+ыт ср+азу же, как т+олько вы забер+ёте ключ в свой трюм.",
            en='Destroy all remaining internal sides of asteroid until you get the key. You will get access to roid miner right after collecting this key into your cargo hold.',
        ),
        VoiceLine(
            7030,
            Neuralnet,
            ru="Если п+олость астер+оида была разрушена с б+елым взр+ывом, то на этом астер+оиде не б+удет ключ+а. Вы должн+ы будете направиться к сл+едующему астер+оиду и попр+обовать сн+ова.",
            en="If side was destroyed with white color, it means this asteroid have no key inside. You must check next asteroid and try again",
        ),
        VoiceLine(
            7040,
            Neuralnet,
            ru="В Секторе Сириуса различные станции нужно взламывать различными способами. "
               "Чтобы получить информацию о методике взлома обратитесь к инфокарте взламываемого объекта.",
            en="You can find different locked objects in Sirius Sector. They should be opened by different ways. "
               "Check the inforcard of locked object to get more information.",
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

    MISSION_TITLE = 'Миссия 2. Мусорная работа'
