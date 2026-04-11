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
        VoiceLine(10, Trent , ru="Вильгельм, я полагаю?", en="Are you Wilhelm?"),
        VoiceLine(20, Wilham, ru="Так точно, герр Трент. Я рад, что вы согласились с нами работать.", en="Herr Trent. We are pleased you have agreed to work with us."),
        VoiceLine(30, Trent , ru="Еще не согласился, но определенно заинтересовался. Не каждый день представители вооруженных сил Рейнланда присылают мне сообщения на КПК с предложением личной встречи на борту линкора вооруженных сил Рейнланда.", en="Whoa now, let's not jump the gun. I can't say I'm not curious, but it's a little intimidating getting instructions on my Pad to report to a Rhineland battleship in the middle of nowhere. It's a little off-putting."),
        VoiceLine(40, Wilham, ru="Это вы о каких сообщениях?", en="Perhaps you are mistaken, Herr Trent. We would never resort to such unrefined tactics, as gentlemen of the Rhineland empire. Could you have imagined these... supposed messages?"),
        VoiceLine(50, Trent, ru="Ну вот же... Черт. Что такое? Оно только что было...", en="No, I'm dead certain. Look, they're right... here... what's going on? How did they disapp..."),
        VoiceLine(60, Wilham, ru="Да черт с ними, с сообщениями, герр Трент, давайте лучше о деле. И да, надеюсь, вы понимаете, что вне зависимости от того чем закончится наш разговор, все его детали должны остаться между нами?", en="Unimportant. That you are here now tells us you are agreeable. Herr Trent, let's cut to the chase. But before this, I hope you understand, regardless of how our conversation ends, all details must remain strictly confidential."),
        VoiceLine(70, Trent, ru="Должны - значит останутся. Любите вы, военные, жути нагнать... Кстати, а почему именно я?", en="Okay, my lips are sealed. You military types don't mess around... Give me the details. By the way, why me?"),
        VoiceLine(80, Wilham, ru="А почему бы и нет? Вы неплохо показали себя в инциденте у аванпоста Бранденбург.", en="You proved yourself earlier at Brandenburg. We couldn't help but notice how you managed to stay alive and even score kills in that death trap poop bucket you are flying."),
        VoiceLine(90, Trent, ru="Понятно. Перейдем к сути задания?", en="Again with the insults to my poor ship. She's a classic, okay? Let's get on to the mission, OK?"),
        VoiceLine(100, Wilham, ru="Перейдем. Как и любое другое государство, мы имеем ряд информаторов на территории, скажем так, наших геополитических соперников. Понимаете о чем я?", en="Alright. Like all governments, we have informants in the territories of our, shall we say, rivals. You are following?"),
        VoiceLine(110, Trent, ru="О да.", en="Sure. Spies."),
        VoiceLine(120, Wilham, ru="Так вот, некоторое время назад один из информаторов вышел на связь по условленному каналу, сообщил, что имеет информацию крайней степени важности и вылетел на своем корабле в условленную точку для передачи данных. И в лучших традициях детективов в точке этой так и не появился. Не обозначил он своего присутствия в течении недели и по месту внедрения, и по аварийным каналам. Это может означать лишь одно - он мертв. ", en="Informants. Not long ago, one of our sp... informants contacted us via a secure channel, reporting that he had critical information to disclose and that he was headed to our secured data transmission point. Predictably, he never arrived. We have had no word since, in the following week. It can only mean one thing - he is dead."),
        VoiceLine(130, Wilham, ru="На основании анализа переговоров диспетчеров станций и операторов экстренных служб в интересующем нас районе с вероятностью более девяноста девяти процентов установлено что корабль нашего информатора был атакован, а сам он погиб.", en="Based on analysis of chatter between station dispatchers and operators of emergency services in the area of interest, we have established that our informant was attacked and killed in his ship. There is an over 99% probability of this."),
        VoiceLine(140, Trent, ru="Сочувствую. Но при чем тут я?", en="My condolences for your loss. How do I come into the picture?"),
        VoiceLine(150, Wilham, ru="Вашей задачей будет найти этот корабль и снять с него интересующие нас данные. Сделать это необходимо как можно скорее, так как в данном районе активность так называемых мусорщиков, чрезвычайно высока. Вы должны их опередить.", en="We need you to find his ship and extricate the supposely critical data for us. Time is critical as activity of so-called \"Junkers\" in the area is escalating rapidly. You must get there ahead of them."),
        VoiceLine(160, Trent, ru="Я вряд ли смогу их опередить. Во-первых я толком не знаю эту область в отличии от них, а во-вторых, опять же в отличии от них я буду действовать один.", en="How am I supposed to do that? I'm a stranger here, and I'm all by my lonesome."),
        VoiceLine(170, Wilham, ru="Сможете. Дело в том, что есть один электронщик-энтузиаст, который занимается разработкой систем слежения и трекинга радиопереговоров. Мы давно заинтересованы в том, чтобы переманить его в наше ведомство, поэтому внимательно за ним наблюдаем.", en="You will have help. We are aware of a certain eccentric technophile who's been tapping into their radio comms and tracking them. We've been keeping a close eye on him for a while now, hoping to recruit him."),
        VoiceLine(180, Trent, ru="Как за мной?", en="Like me, eh? You going to send him an invitatory pad-Psalm too? Perhaps a firebomb?"),
        VoiceLine(190, Wilham, ru="Еще пристальнее. Так вот все свои системы он тестирует как раз на интересующем нас районе. Таким образом, у него есть самая полная информация обо всем что произошло в интересующем нас секторе космоса за последнее время. Вам нужно будет связаться с ним, договориться о передаче координат крушения корабля нашего информатора, снять с него данные и передать их нам... естественно не позволив мусорщикам добраться до них раньше.", en="No, Herr Kent, we are sending you to him. He has the most thorough intel regarding every event that's occurred in that region of space. You must find and recruit him, use him to locate the coordinates of the shipwreck, extricate the data and transfer it to us... Without letting any Junker or other scavengers beat you to it. Easy."),
        VoiceLine(200, Trent, ru="И всего делов-то? Могу приступать? ", en="Oh that's all there is to it? Why didn't you say so. Walk in the park. When do I start."),
        VoiceLine(210, Wilham, ru='Если вы согласны, то не "могу", а "можем". В этом задании я буду приписан к вам в качестве напарника.', en="There's no \"I\" in \"TEAM\". I'll be your assigned team-mate for this mission."),
        VoiceLine(220, Trent, ru="Будете контролировать мои действия?", en="Oh so you're the \"A\"? Will you be the boss of me?"),
        VoiceLine(230, Wilham, ru="Нет. Буду осуществлять поддержку и взаимодействие с властями - у меня достаточно высокий допуск в системах Райнланда. Стратегия операции и тактика её проведения целиком на вас, герр Трент.", en="Nein. I will be your wingman and liason to the authorities - I have a fairly high standing and security clearance in Rheinland. The strategic and tactical aspects of this operation are entirely yours, Herr Trent. So if we fail, it's entirely on you. You understand my meaning, yes?"),
        VoiceLine(240, Trent, ru="Спасибо за доверие... где поставить подпись?", en="Ominous... I like it already. So where do I sign?"),
        VoiceLine(250, Wilham, ru="Ха-ха-ха. Ну зачем нам эти условности? Встречаемся в космосе, герр Трент!", en="Ha-ha. No need for such formalities. They leave a lasting record. I'll meet you in space, Herr Trent. Tschuss!"),
    ]


class Msn2Miner(Msn2, script.CutsceneProps):
    ALIAS = 'miner'
    TITLE = 'Рудокоп Матильда'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Trent, ru="Приветствую!", en="Jacobo?"),
        VoiceLine(20, Jacobo, ru="Симметрично. Чему обязан?", en="Hello. Do I know you?"),
        VoiceLine(30, Trent, ru="Вильгельму вы обязаны.", en="Wilhelm sent me."),
        VoiceLine(40, Jacobo, ru="Что есть -то есть. ", en="Ah crap."),
        VoiceLine(45, Jacobo, ru="И что же на этот раз понадобилось герру Вильгельму?", en="And what does the esteemed Herr Wilhelm need with me?"),
        VoiceLine(50, Trent, ru="Координаты одного разбившегося корабля. ", en="Coordinates of a certain informant's shipwreck."),
        VoiceLine(60, Jacobo, ru="А! Это проще простого. Я сейчас скину вам все точки происшествий с повреждением судов за прошедший месяц. Точность позиционирования плюс-минус двадцать миллиметров. Выбирайте что вам нужно, фильтруйте по критериям, спасибо говорить не нужно.", en="Ah a spy. Yeah I think I know a number of candidate shipwrecks that might fit the bill. I'll even throw in all the locations of all Corsair attacks dating back a month... no make that half a year... Accuracy of twenty millimeters, give or take a couple. No need to thank me."),
        VoiceLine(70, Trent, ru="Мы вместе полетим.", en="That won't be necessary, just the potential informer's wrecks. We'll fly together."),
        VoiceLine(80, Jacobo, ru="Это зачем еще?", en="And why should I risk my neck? I hate flying."),
        VoiceLine(90, Trent, ru="Вильгельм сказал, ты должен мне указать на место интересующего нас события, а я должен его найти. А как я могу быть уверен, что ты не слил мне туфту, чтобы через полчаса свалить в закат? У военных свои причуды, а у фриленсеров - свои.", en="Well, Wilhelm said that you'd be my guide, and time is money. How would I know you're not bullshitting me and wasting my time putting me on some wild goose chase while you kick up your heels and vanish? The Rheinland military is full of character... well so is this freelancer. You smell me?"),
        VoiceLine(100, Jacobo, ru="Сотню раз уже проклял тот день когда согласился Вильгельму помогать.", en="A hundred times I curse the day I agreed to help that accursed Wilhelm."),
        VoiceLine(110, Jacobo, ru="Сам-то он где сейчас? Сидит в баре на ближайшем торговом посту? ", en="Where is that laggard now? Chilling in some bar? Or beach? Or a bar on a beach?"),
        VoiceLine(120, Jacobo, ru="Что бы ни случилось, он тут не при чем окажется, а вот мы с тобой главные фигуранты.", en="Well, I know his type. Whatever action happens, we'll be the two in the thick of it while he kicks back and reaps the rewards."),
    ]


class Msn2Done(Msn2, script.CutsceneProps):
    ALIAS = 'done'
    TITLE = 'Вознаграждение на линкоре'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Reichman, ru="А вот и сам знаменитый Трент.", en="So, the infamous Trent."),
        VoiceLine(20, Trent, ru="И чем же я так знаменит, мистер, эмм...", en="My reputation precedes me, Mr... Umm...?"),
        VoiceLine(30, Reichman, ru="Райхманн. Адмирал Райхманн, если позволите.", en="Reichmann. Admiral Reichmann, if you may."),
        VoiceLine(40, Trent, ru="Моё почтение, адмирал Райхманн! Так чем же я знаменит?", en="An honour, Admiral Reichmann! What am I so famous for, pray tell?"),
        VoiceLine(50, Reichman, ru="О, мистер Трент, в последнее время в некоторых кругах только и разговоров, что о вас! Надеюсь, герр Вильгельм достойно оплачивает вашу работу?",
                  en="The inner circles have been all abuzz about the conquering hero in his piece of crap ship. I hope Herr Wilhelm has been compensating you adequately."),
        VoiceLine(60, Trent, ru="Не жалуюсь.", en="No complaints here."),
        VoiceLine(70, Reichman, ru="Скромность - похвальная благодетель, герр Трент, но одной благодетелью сыт не будешь, ха-ха. Я распоряжусь, чтобы ваш гонорар за предыдущую миссию был удвоен. Всех благ, герр Трент!",
                  en="Modesty - a commendable and often underrated virtue, Herr Trent. I'll make sure to double your payment. All the best to your travels, Herr Trent!"),
        VoiceLine(80, Reichman, ru="Так вы считаете, что он - тот кто нам нужен?", en="So Wilham, you really think that he's the one?"),
        VoiceLine(90, Wilham, ru="Безусловно, герр Адмирал. Он - тот, кто поможет нам выполнить все известные вам задачи.",
                  en="Undoubtedly, Admiral. I can vouch for him personally. He's perfect."),
        VoiceLine(100, Reichman, ru="И вы это гарантируете?", en="Will you stake your reputation and career on him?"),
        VoiceLine(110, Wilham, ru="Абсолютно!", en="Without hesitation."),
        VoiceLine(120, Reichman, ru="Хорошо, мы принимаем в работу ваш сценарий.", en="Very well, execute your plan."),
        VoiceLine(130, Wilham, ru="Благодарю за оказанное доверие.", en="Yes Sir. Thank you for your trust."),
        VoiceLine(140, Reichman, ru="Посмотрим что из этого получится. Не смею задерживать, герр Вильгельм.", en="Trust... we shall see. You're dismissed, Herr Wilhelm."),
    ]


class Msn2Space(Msn2, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(
            30,
            Trent,
            ru="А зачем вам вообще фриленсеры? Вооруженные силы Рейнланда вполне способны сами решить любую проблему. Оцепили сектор, нашли обломки, изъяли данные...",
            en="Why would you need a freelancer for this? The Rheinland military is fully capable of such simple work. Search out the wreckage, download the data...",
        ),
        VoiceLine(
            40,
            Wilham,
            ru="Тем самым дезавуировали своего бывшего агента, выставили на всеобщее обозрение все свои интересы. ",
            en="Ya, that's exactly how we lost our last agent, not to mention exposing our intents to our enemies.",
        ),
        VoiceLine(
            45,
            Wilham,
            ru="Не говоря уже о том, что интересующая нас область находится вне юрисдикции Рейнланда. И кто согласился бы с нами работать после того, как мы устроили подобный цирк?",
            en="Not to mention the fact that the area of interest is outside of Rheinland's jurisdiction. And after the fiasco at Brandenburg willing collaborators have dwindled.",
        ),
        VoiceLine(
            50,
            Wilham,
            ru="Работать с агентами не напрямую, а через сторонних лиц и независимые организации - это мудрость, идущая из глубины веков. Мы можем играть в игру, герр Трент, или не играть.",
            en="Working through third-party free agents and independent organizations is a time-tested practice dating back millenia. We can play the game, Herr Trent, or not.",
        ),
        VoiceLine(
            55,
            Wilham,
            ru="Единственное что мы ОБЯЗАНЫ делать - это соблюдать правила. Кстати, одно из правил, герр Трент. Если вдруг с вами произойдет что-то неприятное, то мое ведомство ничего о вас не знает, а вы, в свою очередь, ничего не знаете о нём.",
            en="The only rule is that we must appear to follow the rules. Oh by the way, another unwritten rule, Herr Trent: If something unpleasant were to happen to you... we had nothing to do with you, and we never met.",
        ),
        VoiceLine(
            60,
            Trent,
            ru="Ясно все с вами, работники ножа и топора, ох, извините, плаща и кинжала.",
            en="Great. Thanks for the reassurance Makes me all warm and tingly inside.",
        ),
        VoiceLine(
            70,
            Wilham,
            ru="Герр Трент, мы приближаемся к общине местных шахтеров, они добывают редкие металлы на астероидах. Интересующий нас человек находится на добывающем судне Матильда. Позывной - Джакобо.",
            en="Herr Trent, we're approaching a local mining community. They mine rare metals from the asteroids. Our target is aboard the mining ship Matilda. Callsign - Jacobo.",
        ),
        VoiceLine(
            75,
            Wilham,
            ru="Просто передайте ему, что вы от Вильгельма. Мне светиться в этом секторе нельзя, тем более на этом корабле, поэтому я на время сойду со сцены.",
            en="Just tell him Wilhelm sent you. He should welcome you with open arms. I must remain incognito so I'll leave the rest to you.",
        ),
        VoiceLine(
            1030,
            Jacobo,
            ru="Я переслал вам координаты ближайшего разбившегося корабля. Постарайтесь быстрее их осмотреть, у  нас не так много времени. ",
            en="I've sent you the coordinates of the closest shipwreck. Try to scan it as fast as you can, we don't have much time.",
        ),
        VoiceLine(
            100,
            Trent,
            ru="Джакобо, а почему здесь так мусорщиков боятся? Собирают себе мусор - и пусть собирают, полезное дело делают.",
            en="Jacobo, why's everyone around here so scared of the Junkers? They're just garbage collectors right? Cleaning up space one wreck at a time?",
        ),
        VoiceLine(
            110,
            Jacobo,
            ru="Бесконечно далеки вы от народа, мальчики из центральных систем. Изначально мусорщики занимались сбором мусора, сортировкой и продажей разных категорий отходов.",
            en="You central system boys so clueless. Look, at first, yes the Junkers just engaged in garbage collection, sorting and selling junk.",
        ),
        VoiceLine(
            112,
            Jacobo,
            ru="И это было настолько прибыльно, что ряды мусорщиков в свое время росли не по дням а по часам. ",
            en="It got so profitable people were signing up in droves. The Junkers were growing not by day, but by the hour. The more of them there were, the more desperate they became to make the bucks.",
        ),
        VoiceLine(
            115,
            Jacobo,
            ru="Сейчас, например, они могут начать рассматривать в качестве мусора любой звездолет случайно попавший в их зону влияния и не имеющий должной охраны. Разберут его на составляющие и продадут в виде вторсырья.",
            en="Eventually their definition of junk became more and more loose... now it includes... say any inadequately guarded spaceship traversing their territory - they tear them apart and sell them as spare parts. And any crew...",
        ),
        VoiceLine(
            120,
            Jacobo,
            ru="Подошли к первой точке вероятного крушения.",
            en="We've reached the first crash site candidate.",
        ),
        VoiceLine(
            130,
            Trent,
            ru="Начинаю сканировать...",
            en="Commencing scan...",
        ),
        VoiceLine(
            140,
            Trent,
            ru="Нет, не то.",
            en="Nope, that's not it.",
        ),
        VoiceLine(
            150,
            Jacobo,
            ru="Есть еще две точки с координатами разбившихся кораблей, которые могут стать интересующими нас объектами...",
            en="There are two more crash site candidates, which could contain our object of interest...",
        ),
        VoiceLine(
            155,
            Jacobo,
            ru="Что за помехи? Что за помехи на радаре???",
            en="What's that? Our radar is being jammed!",
        ),
        VoiceLine(
            160,
            Trent,
            ru="Я полагаю, эти пять..., нет,  семь... девять... враждебных кораблей создают нам помехи. ",
            en="I think there are five… No, seven… Nine… Hostile ships on an intercept course.",
        ),
        VoiceLine(
            170,
            OmegaJunkerOne,
            ru="О! А шо это шевелится на нашей территории?",
            en="Oh, lookie. A little mouse, scampering into mi casa.",
            cinematic=True,
        ),
        VoiceLine(
            180,
            OmegaJunkerTwo,
            ru="Металлолом какой-то...",
            en="Nah, looks like scrap to me",
            cinematic=True,
        ),
        VoiceLine(
            190,
            OmegaJunkerThree,
            ru="Ну вот, опять сортировать мусор.",
            en="Recycle 'em, boys.",
            cinematic=True,
        ),
        VoiceLine(
            200,
            OmegaJunkerOne,
            ru="Да шо вы переживаете, там дел-то на пять минут.",
            en="Don't worry little mousies, it's for the greater good. Recyclingness is Godliness!",
            cinematic=True,
        ),
        VoiceLine(
            210,
            Jacobo,
            ru="Трент - возможно это тот корабль, который вы искали, сканируйте.",
            en="Trent – this could be the ship you're looking for. Scan it.",
        ),
        VoiceLine(
            230,
            Trent,
            ru="Бинго! Тот самый корабль. Считываю данные с бортового журнала...",
            en="Bingo! That's our ship.",
        ),
        VoiceLine(
            240,
            Trent,
            ru="Все. Можем возвращаться. ",
            en="Done. Let's get out of here.",
        ),
        VoiceLine(
            250,
            Jacobo,
            ru="Трент, ты же наёмник? А наемник работает в принципе на любого, кто платит за услуги?",
            en="Trent, you're a freelancer right? And technically, freelancers work for whoever pays best.",
        ),
        VoiceLine(
            260,
            Trent,
            ru="Не на любого, но в принципе, да, это мой хлеб.",
            en="Well, not whoever, but yeah pretty much. That's my bread and butter.",
        ),
        VoiceLine(
            270,
            Jacobo,
            ru="А сможешь поработать на меня, если придется?",
            en="Would you work for me, if I ever needed help?",
        ),
        VoiceLine(
            280,
            Trent,
            ru="Конечно!",
            en="Of course... for the right price.",
        ),
        VoiceLine(
            290,
            Jacobo,
            ru="Тогда я обсужу это со знакомыми шахтерами. И если ты не против, мы хотели бы нанять тебя.",
            en="Okay. I'll have to discuss it with some miner friends. If you don't mind, we'd like to hire you.",
        ),
        VoiceLine(
            300,
            Trent,
            ru="Да не вопрос.",
            en="It'd be my pleasure.",
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
            en="We're glad that you could completed the mission. Please, transfer the data to Punisher 1.",
        ),
        VoiceLine(
            330,
            Trent,
            ru="Вильгельм, НАПАРНИК, а ты не мог помочь мне в бою с мусорщиками когда я получал эти ваши сверхсекретные данные?",
            en="Wilhelm, PARTNER, could you have done less to help me fight off those Junkers while I collected your precious top secret data? What happened to there is no I in Team?",
        ),
        VoiceLine(
            340,
            Wilham,
            ru="Нет, это выходило за рамки моей компетенции.",
            en="Nah, it was beyond my level of expertise. I'm a lover, not a fighter.",
        ),
        VoiceLine(
            350,
            Punisher,
            ru="Внимание, это каратель - 1! Нами обнаружен нелегальный склад оружия, находящийся в облаке Майсен.",
            en=", this is Punisher-1! We've decoded the data. There is an illegal weapon storage facility located in the Maison cloud. We need to lock it down.",
        ),
        VoiceLine(
            360,
            Wilham,
            ru="Передавайте координаты! Трент, не хочешь поучаствовать в операции федерального масштаба? ",
            en="Send us the coordinates! Trent, how would you like to participate in a federal-scale operation?",
        ),
        VoiceLine(
            370,
            Trent,
            ru="А у меня есть выбор?",
            en="Are you really asking?",
        ),
        VoiceLine(
            380,
            Wilham,
            ru="Ха-ха-ха! Нет!",
            en="Ha-ha-ha! No.",
        ),
        VoiceLine(
            390,
            Trent,
            ru="Тогда, пожалуй, поучаствую!",
            en="Then I suppose I'd love to.",
        ),
        VoiceLine(
            1050,
            Punisher,
            ru="Склад обнаружен. Вижу противника!",
            en="Storage facility located. Bogeys inbound!",
        ),
        VoiceLine(
            1060,
            Wilham,
            ru="Каратель-4, на вас грузовики. Остановите их! Остальным – уничтожать истребители.",
            en="Punisher-4, the transports are heading your way. Stop them at all costs! Everyone else – destroy the fighters.",
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
            en="Punisher-4, what's going on with the transports?",
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
            en="A base! I see the Corsair base!",
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
            en="Trent!!! Your orders are to support Punisher wing! Take out the weapon platforms!!!",
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
            en="Punisher-1, are we ready to neutralize the base?",
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
            en="Roger that. Trent, take care of the fighters.",
        ),
        VoiceLine(
            1120,
            Punisher,
            ru="Сектор чист, торпеды готовы к запуску!",
            en="Area clear, torpedoes away!",
        ),
        VoiceLine(
            1130,
            Wilham,
            ru="Объект уничтожен, миссия выполнена. Каратели, оцепите район и изучите останки базы. Герр Трент, следуйте на Шарнхорст.",
            en="Objective destroyed, mission accomplished. Punishers, scout the area and search the debris for survivors. Herr Trent, come with me to Scharnhorst.",
        ),
        VoiceLine(
            460,
            Wilham,
            ru="Мне только что передали, герр Трент, что с вами хочет пообщаться один из адмиралов Рейнланда.",
            en="I just received word, Herr Trent. One of Rheinland's admirals would like to talk to you.",
        ),
        VoiceLine(
            470,
            Trent,
            ru="И много у вас адмиралов?",
            en="Do you many admirals?",
        ),
        VoiceLine(
            480,
            Wilham,
            ru="По пальцам одной руки можно пересчитать. Тебе оказали большую честь.",
            en="As many as I can count. On one hand. Ha-ha. You are being greatly honored.",
        ),
        VoiceLine(
            490,
            Trent,
            ru="Охренеть. Будет что вспомнить в старости.",
            en="Well... this'll be something to tell the grandkids about when I'm old. Assuming I make it long enough to have kids.",
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
            en='To access the roid miner you must find the key. The key is hidden inside an asteroid. You must mine it out. Attack the sides of the asteroids with your guns.',
        ),
        VoiceLine(
            7010,
            Neuralnet,
            ru="+Если п+олость астер+оида разр+ушилась с зел+ёным взр+ывом, зн+ачит с астер+оида м+ожно доб+ыть кл+юч.",
            en='If the side under attack shows up green this asteroid contains the key',
        ),
        VoiceLine(
            7020,
            Neuralnet,
            ru="Уничтошьте все п+олости +этого астер+оида до тех пор, пока ключ не в+ыпадет. Д+оступ к ст+анции б+удет откр+ыт ср+азу же, как т+олько вы забер+ёте ключ в свой трюм.",
            en='Destroy all remaining internal sides of asteroid until you get the key. Once you tractor the key into your cargo hold you will be able to board the miner.',
        ),
        VoiceLine(
            7030,
            Neuralnet,
            ru="Если п+олость астер+оида была разрушена с б+елым взр+ывом, то на этом астер+оиде не б+удет ключ+а. Вы должн+ы будете направиться к сл+едующему астер+оиду и попр+обовать сн+ова.",
            en="If side under attack shows up white this asteroid does not have the key inside.",
        ),
        VoiceLine(
            7040,
            Neuralnet,
            ru="В Секторе Сириуса различные станции нужно взламывать различными способами. "
               "Чтобы получить информацию о методике взлома обратитесь к инфокарте взламываемого объекта.",
            en="You can find various locked objects in Sirius Sector. They are all accessed differently. "
               "Check the inforcard on each locked object to get more information.",
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