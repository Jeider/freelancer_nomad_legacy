from story import script
from audio.sound import VoiceLine
from story.actors import (
    Trent, Hatcher, HatcherStation, Jacobo, Alaric, Kreitmaier, Sigma8Cruiser, Reichman, Hassler, JacoboTrader, Sigma8Outpost
)


class Msn4(object):
    MISSION_INDEX = 4


class Msn4Offer(Msn4, script.CutsceneProps):
    ALIAS = 'offer'
    TITLE = 'Предложение'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Jacobo, ru="Герр Трент, это вы?", en="Herr Trent, is that you?"),
        VoiceLine(20, Jacobo, ru="Герр Трент, спасибо что согласились прилететь. У меня неприятности. Меня разыскивают власти Рейнланда.",
                  en="Herr Trent, thank you for agreeing to come. I'm in trouble. The Rheinland authorities are looking for me."),
        VoiceLine(30, Trent, ru="Это я уже понял. И у меня появилось знакомое ощущение что меня очень хотят втянуть в неприятности.",
                  en="I already figured that out. And I've got that familiar feeling that someone really wants to drag me into trouble."),
        VoiceLine(40, Jacobo, ru="Герр Трент, вы не понимаете. Дело исключительной важности. Мне необходимо доставить в Либерти важные документы.",
                  en="Herr Trent, you don't understand. This is a matter of exceptional importance. I need to deliver important documents to Liberty."),
        VoiceLine(50, Trent, ru="Опять меня угораздило вляпаться в шпионские игры... Джакобо, вы в курсе, что в данный момент я работаю на те самые власти Рейнланда, которые вас ищут?",
                  en="I've gone and gotten into spy games again... Jacobo, are you aware that right now I work for the very Rheinland authorities who are looking for you?"),
        VoiceLine(60, Jacobo, ru="Герр Трент, вы же фриленсер. Вы не давали никаких присяг. После выполнения задания вас с заказчиком ничего не связывает. ",
                  en="Herr Trent, you're a freelancer. You didn't take any oaths. Once a job is done, nothing ties you to the client."),
        VoiceLine(62, Jacobo, ru="Герр Трент, если мы сможем доставить эти ОЧЕНЬ важные документы в Либерти, в систему Форбс, нам заплатят очень большие деньги, ОЧЕНЬ большие, понимаете? ",
                  en="Herr Trent, if we can deliver these VERY important documents to Liberty, to the Forbes system, they'll pay us very big money, VERY big, you understand?"),
        VoiceLine(65, Jacobo, ru="У меня одного это скорее всего не получится, но если вы мне поможете... ", en="On my own I most likely won't manage it, but if you help me..."),
        VoiceLine(67, Jacobo, ru="А если вы мне не поможете, меня скорее всего просто убьют... ", en="And if you don't help me, they'll most likely just kill me..."),
        VoiceLine(70, Trent, ru="Я об этом еще пожалею... Хорошо, каков план?", en="I'm going to regret this... All right, what's the plan?"),
        VoiceLine(80, Jacobo, ru="Герр Трент, спасибо, вы не пожалеете! Вылетайте в космос, я с помощью друзей попробую незаметно пробраться на взлетную площадку. Встретимся на орбите.",
                  en="Herr Trent, thank you, you won't regret it! Launch into space. With my friends' help I'll try to sneak onto the launch pad unnoticed. We'll meet in orbit."),
        VoiceLine(90, Trent, ru="Тогда до встречи.", en="Then, see you."),
    ]


class Msn4Reward(Msn4, script.CutsceneProps):
    ALIAS = 'reward'
    TITLE = 'Вознаграждение'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Hatcher, ru="Мисс Хетчер.", en="Miss Hatcher."),
        VoiceLine(20, Trent, ru="Мисс Хетчер.", en="Miss Hatcher."),
        VoiceLine(30, Alaric, ru="Мисс Хетчер, у вас такие красивые бездонные глаза, что...", en="Miss Hatcher, you have such beautiful, bottomless eyes that..."),
        VoiceLine(40, Hatcher, ru="Что вы перестанете нести эту околесицу, иначе я рассержусь", en="That you'll stop talking this nonsense, or I'll get angry"),
        VoiceLine(45, Hatcher, ru=". О деле. Все выполнено на лучшем уровне. ", en=". To business. Everything was done at the highest level."),
        VoiceLine(50, Hatcher, ru="Я даже не буду спрашивать чего стоило вам сбежать из Рейнланда с ТАКИМИ документами", en="I won't even ask what it cost you to escape Rheinland with SUCH documents"),
        VoiceLine(55, Hatcher, ru="Я девушка впечатлительная, боюсь в обморок упасть.", en="I'm an impressionable girl. I'm afraid I'll faint."),
        VoiceLine(60, Trent, ru="Мы старались.", en="We did our best."),
        VoiceLine(70, Hatcher, ru="Хе, вы тоже были в этом заинтересованы. А кстати, нам как раз нужны такие умелые и предприимчивые люди как вы, для выполнения, скажем так, нестандартных заданий. Вы в ближайшее время не слишком заняты?", en="Heh, you had a stake in this too. By the way, we happen to need skilled, enterprising people like you for, shall we say, nonstandard jobs. You're not too busy in the near future?"),
        VoiceLine(80, Alaric, ru="Для вас мы всегда...", en="For you, we're always..."),
        VoiceLine(90, Trent, ru="Заткнись, Аларик. Нет, с тех пор как мы стали врагами Рейнландского государства, работы у нас поубавилось.", en="Shut up, Alaric. No. Ever since we became enemies of the Rheinland state, we've had less work."),
        VoiceLine(100, Hatcher, ru="То есть если у нас найдется пара заданий по вашему профилю за достойную плату...", en="So if we happen to have a couple of jobs in your line, for decent pay..."),
        VoiceLine(110, Trent, ru="То мы не против их выполнить, если конечно же эти задания не приведут к тому что мы станем государственными преступниками и в Либерти.", en="Then we don't mind doing them, provided of course these jobs don't make us state criminals in Liberty too."),
        VoiceLine(120, Hatcher, ru="О, нет, я думаю до этого не дойдет.", en="Oh, no, I don't think it'll come to that."),
        VoiceLine(130, Trent, ru="Я вот тоже думал...", en="That's what I thought too..."),
    ]


class Msn4Final(Msn4, script.CutsceneProps):
    ALIAS = 'final'
    TITLE = 'Вознаграждение'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Alaric, ru="Круто, Трент, ты умеешь находить себе заказчиков и покровителей.", en="Nice, Trent. You know how to find yourself clients and patrons."),
        VoiceLine(20, Trent, ru="А так же врагов и убийц.", en="And also enemies and killers."),
        VoiceLine(30, Alaric, ru="Да ладно тебе. Ты фриланесером работать стал всего ничего, и вот уже задания на уровне правительств с соответствующей оплатой.", en="Come on. You've barely started working as a freelancer, and already you're getting government-level jobs with the pay to match."),
        VoiceLine(40, Trent, ru="Ага, и одно из правительств уже назначило награду за мою голову, и я сомневаюсь что у этого правительства короткая память.", en="Yeah, and one of those governments has already put a bounty on my head, and I doubt that government has a short memory."),
        VoiceLine(50, Alaric, ru="Да ладно тебе, с таким прикрытием рейнландцы пупок себе скорее надорвут, чем нас достанут.", en="Come on, with cover like this the Rheinlanders will bust a gut before they ever get to us."),
        VoiceLine(60, Trent, ru="С каким-таким прикрытием? Ну-ка Аларик, чего я не знаю?", en="What cover is that? Come on, Alaric, what don't I know?"),
        VoiceLine(70, Alaric, ru="Эта мисс Хетчер, ты в курсе кто она?", en="This Miss Hatcher, do you know who she is?"),
        VoiceLine(80, Trent, ru="Ну конечно в курсе. Я знаю её уже целых три часа, я в курсе. Аларик, короче, мать твою!", en="Oh, of course I do. I've known her for a whole three hours, I do. Alaric, get to the point, damn it!"),
        VoiceLine(90, Alaric, ru="Она офицер в одной из спецслужб Либерти.", en="She's an officer in one of Liberty's intelligence services."),
        VoiceLine(100, Trent, ru="О боже! Нет... Опять...", en="Oh God! No... Again..."),
        VoiceLine(110, Alaric, ru="Ты не понимаешь, это настолько крутая спецслужба, что другие спецслужбы даже не подозревают о её существовании.", en="You don't understand. This service is so serious that other intelligence services don't even suspect it exists."),
        VoiceLine(120, Trent, ru="Аларик, тогда ты то откуда про это знаешь?", en="Alaric, then how do you know about this?"),
        VoiceLine(130, Alaric, ru="А... Э-э-э...", en="Ah... Uh..."),
        VoiceLine(140, Trent, ru="Короче, трындец, опять вляпался.", en="Short version: I'm screwed. Got into it again."),
    ]


class Msn4Space(Msn4, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(
            0,
            JacoboTrader,
            ru="Герр Трент, это Джакобо! Герр Трент, вы помните меня? Герр Трент, нам очень нужна ваша помощь. Вы же были не против помочь нам если понадобится, помните? Герр Трент, прошу вас как можно быстрее прибыть на планету Норторф в систему Мюнхен!",
            en="Herr Trent, this is Jacobo! Herr Trent, do you remember me? Herr Trent, we really need your help. You weren't against helping us if the need came, remember? Herr Trent, please get to planet Nortorf in the Munich system as quickly as you can!",
        ),
        VoiceLine(
            10,
            Trent,
            ru="Джакобо, Дромадер? Что это за ведро?",
            en="Jacobo, a Dromedary? What is this bucket?",
        ),
        VoiceLine(
            20,
            JacoboTrader,
            ru="Мой корабль засвечен, за ним постоянная слежка, это единственное, что я смог быстро и незаметно купить.",
            en="My ship's been exposed. It's under constant surveillance. This is the only thing I could buy quickly and without being noticed.",
        ),
        VoiceLine(
            30,
            Trent,
            ru="Но ты же понимаешь, что если начнется заварушка, он развалится от первого же плевка?",
            en="But you do understand that if a fight starts, it'll fall apart if you spit on it?",
        ),
        VoiceLine(
            40,
            JacoboTrader,
            ru="У меня нет выбора. Хотя вы правы, Герр Трент, документы обязательно должны попасть к заказчику. Сейчас я передам вам копии, откройте канал.",
            en="I have no choice. Though you're right, Herr Trent, the documents absolutely must reach the client. I'll transfer the copies to you now. Open a channel.",
        ),
        VoiceLine(
            50,
            Trent,
            ru="Передача завершена успешно. Как будем пробиваться в Либерти?",
            en="Transfer completed successfully. How are we going to break through to Liberty?",
        ),
        VoiceLine(
            60,
            JacoboTrader,
            ru="Власти Рейнланда в курсе всех моих действий, мне еле удалось улизнуть когда они за мной пришли, поэтому короткая дорога не для нас. ",
            en="The Rheinland authorities know all my actions. I barely managed to slip away when they came for me, so the short road isn't for us.",
        ),
        VoiceLine(
            70,
            JacoboTrader,
            ru="У врат в Хонсю нас скорее всего ждут. Попробуем в обход через территорию Рейналанда. Берем курс на систему Бисмарк.",
            en="They're most likely waiting for us at the jump gate to Honshu. Let's go around through Rheinland territory. Setting course for the Bismarck system.",
        ),
        VoiceLine(
            80,
            Trent,
            ru="Логично. Если тебя разыскивают власти Рейнланда, куда лучше всего лететь? Правильно, в столицу...",
            en="Logical. If the Rheinland authorities are looking for you, where's the best place to fly? Right, the capital...",
        ),
        VoiceLine(
            90,
            JacoboTrader,
            ru="Если есть другие предложения...",
            en="If there are other suggestions...",
        ),
        VoiceLine(
            100,
            Trent,
            ru="Нет других предложений, Джакобо, просто мысли вслух.",
            en="No other suggestions, Jacobo, just thinking out loud.",
        ),
        VoiceLine(
            110,
            Kreitmaier,
            ru="С вами говорит командир спецгруппы Гессенский Лев Маркус Крейтмайер.",
            en="This is Marcus Kreitmaier, commander of the Hessian Lion special group.",
            cinematic=True,
        ),
        VoiceLine(
            120,
            Kreitmaier,
            ru="Немедленно отключите оружейные системы и следуйте с нами под конвоем. В случае сопротивления у нас есть полномочия вас уничтожить.",
            en="Shut down your weapon systems immediately and follow us under escort. If you resist, we are authorized to destroy you.",
            cinematic=True,
        ),
        VoiceLine(
            130,
            Trent,
            ru="Недолго музыка играла... Джакобо, тут без шансов. Маркус, банкуйте, мы сдаемся.",
            en="That didn't last long... Jacobo, no chance here. Marcus, you deal, we surrender.",
        ),
        VoiceLine(
            140,
            Kreitmaier,
            ru="Следуйте под нашим конвоем к станции Кёльн.",
            en="Follow under our escort to Cologne station.",
        ),
        VoiceLine(
            150,
            JacoboTrader,
            ru="Это же главная военная база Рейнланда! Да что мы такого сделали? На каком основании? Какие преступления нам вменяют, в конце концов?",
            en="That's Rheinland's main military base! What did we even do? On what grounds? What crimes are they charging us with, anyway?",
        ),
        VoiceLine(
            160,
            Kreitmaier,
            ru="Вы не в том положении, чтобы задавать вопросы. Следуйте нашим указаниям.",
            en="You are not in a position to ask questions. Follow our instructions.",
        ),
        VoiceLine(
            170,
            Trent,
            ru="Джакобо, угомонись.",
            en="Jacobo, settle down.",
        ),
        VoiceLine(
            180,
            Reichman,
            ru="Герр Крейтмайер, говорит адмирал Р+айхманн. Благодарю вас за успешно выполненное задание.",
            en="Herr Kreitmaier, this is Admiral Reichmann. Thank you for successfully completing the assignment.",
            cinematic=True,
        ),
        VoiceLine(
            190,
            Reichman,
            ru="Доставьте грузовик типа Дромадер на базу для досмотра. Сопровождавший его корабль приказываю уничтожить.",
            en="Deliver the Dromedary-type transport to base for inspection. I order the ship that was escorting it destroyed.",
            cinematic=True,
        ),
        VoiceLine(
            200,
            Kreitmaier,
            ru="Уничтожить? Он доставлен под конвоем, адмирал. Как уничтожить?",
            en="Destroy him? He was delivered under escort, Admiral. Destroy him how?",
        ),
        VoiceLine(
            210,
            Reichman,
            ru="М+олча и быстро. И не пререкаясь со старшими по званию!",
            en="Quietly and quickly. And don't talk back to your superiors!",
        ),
        VoiceLine(
            220,
            Hassler,
            comment='Вот это поворот! Появляется внезапный бог из машины!',
            ru="Герр Крейтмайер, вас ввели в заблуждение! Заговор! Освободите конвоируемых!",
            en="Herr Kreitmaier, you've been misled! Conspiracy! Release the people under escort!",
        ),
        VoiceLine(
            230,
            Alaric,
            ru="Слова - это слишком долго. Торпеды быстрее.",
            en="Words take too long. Torpedoes are faster.",
        ),
        VoiceLine(
            240,
            Reichman,
            ru="Боевая тревога! Уничтожить агрессоров!",
            en="Battle alert! Destroy the aggressors!",
        ),
        VoiceLine(
            250,
            Kreitmaier,
            ru="Боевая тревога!",
            en="Battle alert!",
        ),
        VoiceLine(
            260,
            Trent,
            comment='Начинается битва!',
            ru="Спасибо, ребята, теперь валим отсюда!",
            en="Thanks, guys, now let's get out of here!",
        ),
        VoiceLine(
            270,
            Hassler,
            ru="Не так быстро, Трент. Видишь этот линкор поблизости? Стоит нам отлететь от станции - он нас на атомы распылит из своих орудий.",
            en="Not so fast, Trent. See that battleship nearby? The moment we fly away from the station, it'll blast us into atoms with its guns.",
        ),
        VoiceLine(
            280,
            Hassler,
            ru="А пока мы рядом с Кёльном он стрелять не будет, побоится задеть станцию. Но у меня есть одна идея.",
            en="And while we're next to Cologne, it won't fire. It'll be afraid of hitting the station. But I have an idea.",
        ),
        VoiceLine(
            290,
            Hassler,
            comment='Хасслер выстреливает какой-то торпедой по боковой панели реактора линкора',
            ru="(в пылу боя) Маленький сюрприз от знакомых Изгоев: сверхмощная торпеда. Трент, я нанёс критический урон по линкору, но второй такой торпеды у меня нет. Ты должен добить реактор линкора и пустить его вразнос!",
            en="(in the heat of battle) A little surprise from some Outcasts I know: an ultra-powerful torpedo. Trent, I've done critical damage to the battleship, but I don't have a second torpedo like that. You have to finish off the battleship's reactor and send it into runaway!",
        ),
        VoiceLine(
            300,
            Hassler,
            ru="(в пылу боя) Этот линкор стоит на ремонте, у него как раз проблемы с системой охлаждения. Постарайся как можно быстрее! Мы с Алариком займемся истребителями!",
            en="(in the heat of battle) This battleship is in for repairs. It's got problems with the cooling system right now. Do it as fast as you can! Alaric and I will handle the fighters!",
        ),
        VoiceLine(
            310,
            Hassler,
            comment='Линкор взорвался!',
            ru="А теперь действительно валим отсюда. Скорее!",
            en="And now we really are getting out of here. Hurry!",
        ),
        VoiceLine(
            320,
            Alaric,
            ru="Включаем круиз!",
            en="Engaging cruise!",
        ),
        VoiceLine(
            330,
            Trent,
            comment='Летим',
            ru="А теперь, объясните мне, пожалуйста, что за хрень вообще происходит? Во что влип Джакобо и я вместе с ним?",
            en="And now, would you please explain to me what the hell is going on? What has Jacobo gotten into, and me along with him?",
        ),
        VoiceLine(
            340,
            Hassler,
            ru="Герр Трент, вы оказались не в том месте и не в то время.",
            en="Herr Trent, you were in the wrong place at the wrong time.",
        ),
        VoiceLine(
            350,
            Trent,
            ru="у, с этим у меня как раз порядок, люблю я это дело.",
            en="Uh, that I've got covered. I love that sort of thing.",
        ),
        VoiceLine(
            360,
            Hassler,
            ru="Как вы помните, финал миссии в Кёнигсберге выглядел со всех сторон сомнительно. И я решил копнуть глубже.",
            en="As you remember, the end of the Königsberg mission looked suspicious from every side. So I decided to dig deeper.",
        ),
        VoiceLine(
            410,
            Hassler,
            ru="Я выяснил, что Дитрих в своё время смог выкрасть из генштаба Рейнланда некие важные сверхсекретные документы. Так вот, вся операция была затеяна для того чтобы эти документы вернуть.",
            en="I found out that Dietrich at one time managed to steal certain important top-secret documents from Rheinland's General Staff. So the whole operation was started in order to get those documents back.",
        ),
        VoiceLine(
            420,
            Hassler,
            ru="Если бы Райхман достал документы, а Дитрих при этом скрылся, операция всё равно была бы признана успешной.",
            en="If Reichmann had gotten the documents, and Dietrich had escaped, the operation would still have been considered a success.",
        ),
        VoiceLine(
            560,
            Hassler,
            ru="Кстати, герр Трент, позвольте поинтересоваться, а чем вы вообще занимались непосредственно перед нашим появлением? Вас конвоировали в сопровождении государственного преступника.",
            en="By the way, Herr Trent, allow me to ask: what exactly were you doing right before we showed up? You were under escort, in the company of a state criminal.",
        ),
        VoiceLine(
            570,
            JacoboTrader,
            ru="Это все какое-то недоразумение.",
            en="This is all some kind of misunderstanding.",
        ),
        VoiceLine(
            590,
            Trent,
            ru="Джакобо попросил эскортировать его на территорию Либерти. Неплохой парень, мы с ним пересекались по делу когда я работал под юрисдикцией небезызвестного вам герра Вильгельма.",
            en="Jacobo asked me to escort him into Liberty territory. Decent guy. We crossed paths on a job when I was working under the jurisdiction of Herr Wilhelm, who is not unknown to you.",
        ),
        VoiceLine(
            600,
            Hassler,
            ru="Интересно, и зачем же этому неплохому парню понадобился эскорт в Либерти?",
            en="Interesting. And why did this decent guy need an escort to Liberty?",
        ),
        VoiceLine(
            610,
            JacoboTrader,
            ru="Мне нужно срочно доставить важные документы в систему Форбс.",
            en="I urgently need to deliver important documents to the Forbes system.",
        ),
        VoiceLine(
            620,
            Hassler,
            ru="Важные документы, говорите... В либерти... В любом случае, господа, нам необходимо как можно скорее покинуть территорию Рейнланда. Нельзя слишком долго искушать судьбу.",
            en="Important documents, you say... To Liberty... In any case, gentlemen, we need to leave Rheinland territory as soon as possible. We can't tempt fate for too long.",
        ),
        VoiceLine(
            630,
            Hassler,
            comment='Вражеский крейсер и истребители после вылета из гипердыры',
            ru="Засада! Как они нас нашли?",
            en="Ambush! How did they find us?",
        ),
        VoiceLine(
            9150,
            Alaric,
            ru="Тут целый крейсер, а у меня кончились боеприпасы! Трент, атакуй уязвимые точки крейсера! Мы его и так разнесём!",
            en="There's a whole cruiser here, and I'm out of ammo! Trent, attack the cruiser's weak points! We'll tear it apart anyway!",
        ),
        VoiceLine(
            9200,
            Sigma8Cruiser,
            ru="Прекратите сопротивление! Вам не уйти!",
            en="Stop resisting! You won't get away!",
        ),
        VoiceLine(
            640,
            JacoboTrader,
            ru="Помогите! Они сейчас меня сожгут!",
            en="Help! They're about to burn me up!",
        ),
        VoiceLine(
            650,
            JacoboTrader,
            ru="А-а-а-ргхх...",
            en="A-a-a-rghh...",
        ),
        VoiceLine(
            660,
            Trent,
            ru="Твою же мать!",
            en="God damn it!",
        ),
        VoiceLine(
            9300,
            Hassler,
            comment='Враги уничтожены',
            ru="Скорее уходим!",
            en="Quick, we're leaving!",
        ),
        VoiceLine(
            670,
            Hassler,
            comment='Пока летим...',
            ru="Очень интересно.",
            en="Very interesting.",
        ),
        VoiceLine(
            680,
            Trent,
            ru="И что же вас так заинтересовало, герр Хасслер.",
            en="And what is it that has you so interested, Herr Hassler.",
        ),
        VoiceLine(
            690,
            Hassler,
            ru="Вражеский отряд вёл концентрированный огонь по самому безобидному кораблю из нашей команды. Это выглядит весь странно, герр Трент, не находите?",
            en="The enemy unit laid concentrated fire on the most harmless ship in our group. That looks quite strange, Herr Trent, don't you think?",
        ),
        # VoiceLine(
        #     700,
        #     Hassler,
        #     ru="Было бы логичнее связать боем и уничтожить самый опасный - меня или вас, герр Трент.",
        #     en="It would have made more sense for them to take out the fighters first then pick off the Dromedary. ",
        # ),
        VoiceLine(
            710,
            Trent,
            ru="Значит, они преследовали определенный корабль и то, что на нем находится.",
            en="So they were after a specific ship, and what's on it.",
        ),
        VoiceLine(
            720,
            Hassler,
            ru="Вот и я о том же. Документы. Кстати, герр Трент, документов теперь нет? Конец истории?",
            en="That's exactly my point. The documents. By the way, Herr Trent, so the documents are gone now? End of the story?",
        ),
        VoiceLine(
            730,
            Trent,
            ru="Не совсем. У меня сохранились копии.",
            en="Not quite. I still have the copies.",
        ),
        VoiceLine(
            740,
            Hassler,
            ru="Ха-ха-ха, герр Трент, с вами очень приятно и интересно работать. Я не завидую вашим врагам.",
            en="Ha-ha-ha, Herr Trent, it's very pleasant and interesting working with you. I don't envy your enemies.",
        ),
        VoiceLine(
            750,
            Alaric,
            ru="А знаете что... Было бы еще интереснее завершить эту миссию. Джакобо убит, но у нас есть координаты заказчика и есть то, что ему нужно. Думаю, это будет не только интересно, но и прибыльно.",
            en="You know what... It would be even more interesting to finish this mission. Jacobo is dead, but we have the client's coordinates, and we have what he needs. I think it'll be not only interesting, but profitable.",
        ),
        VoiceLine(
            760,
            Hassler,
            ru="А нам ведь больше и некуда деваться. Так ведь, герр Трент?",
            en="And anyway, we have nowhere else to go. Right, Herr Trent?",
        ),
        VoiceLine(
            770,
            Trent,
            ru="Слушайте, Хасслер, мне этот ваш герр настолько надоел в Рейнланде... Можно просто Трент? Тем более что мы в Либерти летим?",
            en="Listen, Hassler, I got so tired of that Herr of yours back in Rheinland... Can it just be Trent? Especially since we're flying to Liberty?",
        ),
        VoiceLine(
            780,
            Hassler,
            ru="Как вам будет угодно, герр Трент.",
            en="As you wish, Herr Trent.",
        ),
        VoiceLine(
            790,
            Trent,
            ru="Не самое подходящее время веселиться. Лучше посоветуйте как в Либерти проще пробраться, мы все-таки еще на территории Рейнланда, где нас, скорее всего уже в государственных преступников записали.",
            en="Not the best time for jokes. Better tell me the easier way to slip into Liberty. We're still in Rheinland territory, where they've most likely already listed us as state criminals.",
        ),
        VoiceLine(
            800,
            Hassler,
            ru="Нет ничего проще, мы воспользуемся моим устройством для активации аномалий и покинем Рейнланд через обходной путь.",
            en="Nothing simpler. We'll use my device for activating anomalies and leave Rheinland by a roundabout route.",
        ),
        # VoiceLine(
        #     810,
        #     Trent,
        #     ru="Вам Кёльна мало показалось, герр Хасслер?",
        #     en="Don’t you mean Cologne, Hassler? ",
        # ),
        # VoiceLine(
        #     820,
        #     Hassler,
        #     ru="Трент, вы помните как мы попали к станции Кёнигсберг в той самой, вызывающей у нас теперь столь устойчивую икоту миссии? И давайте без герров, вы же сами предложили",
        #     en="Trent, do you remember how we got to Konigsberg, when this whole messed-up... mess... started? And please drop the Herr too, you’re the one who asked to dispense with formalities. ",
        # ),
        # VoiceLine(
        #     830,
        #     Trent,
        #     ru="Через аномалию, которую открыл... Открыл ты, Хасслер, каким-то специальным устройством!",
        #     en="Sure. The space anomaly, that... you activated. You still have that ability?",
        # ),
        # VoiceLine(
        #     840,
        #     Hassler,
        #     ru="Ну так вот, это устройство все еще на моем корабле, а ближайшая аномалия недалеко от аванпоста Аугсбург.",
        #     en="Yes, my ship has been outfitted with some quite unusual technology. It can open dormant anomalies. The nearest anomaly out of Rheinland is just next to Augsburg. ",
        # ),
        # VoiceLine(
        #     850,
        #     Trent,
        #     ru="Я понял. Веди.",
        #     en="Roger that. Take the lead. ",
        # ),
        VoiceLine(
            900,
            Sigma8Outpost,
            ru="Внимание, вы вошли в зону ответственности аванпоста Аугсбург. Немедленно отключите оружейные системы и проследуйте в зону шлюзов!",
            en="Attention, you have entered the area of responsibility of Augsburg outpost. Shut down your weapon systems immediately and proceed to the docking zone!",
        ),
        VoiceLine(
            910,
            Hassler,
            ru="Не обращайте внимания, у них нет сил, достаточных чтобы перехватить нас. Видите, ни один истребитель не вылетел на перехват. Продолжаем движение.",
            en="Pay them no attention. They don't have enough forces to intercept us. See, not a single fighter has launched to intercept. We keep moving.",
        ),
        VoiceLine(
            920,
            Sigma8Outpost,
            ru="Это аванпост Аугсбург, повторяю, немедленно...",
            en="This is Augsburg outpost, I repeat, immediately...",
        ),
        VoiceLine(
            930,
            Trent,
            ru="Аванпост Аугсбург, отвалите, немедленно, повторяю, немедленно отвалите.",
            en="Augsburg outpost, piss off, immediately. I repeat, immediately piss off.",
        ),
        VoiceLine(
            940,
            Alaric,
            ru="Ха-ха-ха.",
            en="Ha-ha-ha.",
        ),
        # VoiceLine(
        #     950,
        #     Hassler,
        #     ru="Как изысканно...",
        #     en="What shocking language... ",
        # ),
        VoiceLine(
            860,
            Hassler,
            ru="Предупреждаю вас, друзья мои, аномалия ведет куда-то на территорию Либерти, куда конкретно, я не знаю, поэтому вам придется в первое время вспомнить все навыки ориентирования на местности.",
            en="I warn you, my friends: the anomaly leads somewhere into Liberty territory. Where exactly, I don't know, so at first you'll have to remember all your navigation skills.",
        ),
        VoiceLine(
            870,
            Alaric,
            ru="В смысле вам? Ты с нами не летишь?",
            en="What do you mean, you? You're not flying with us?",
        ),
        VoiceLine(
            875,
            Hassler,
            ru="Нет, спасибо, мне гораздо комфортнее будет залечь на дно на периферии Рейнланда. Ну и как бывшему офицеру спецслужб мне было бы очень опасно появляться в Либерти. Я слишком много знаю.",
            en="No, thank you. I'll be much more comfortable lying low on the edge of Rheinland. And as a former intelligence officer, it would be very dangerous for me to show up in Liberty. I know too much.",
        ),
        # VoiceLine(
        #     880,
        #     Trent,
        #     ru="Но тебя же разыскивают власти.",
        #     en="But the authorities, if they find you... ",
        # ),
        # VoiceLine(
        #     890,
        #     Hassler,
        #     ru="Наши власти много кого разыскивают, но далеко не всех находят, поверьте мне, с моими связями и навыками мне будет гораздо безопаснее на территории Рейнланда, чем на территории Либерти.",
        #     en="Our authorities are looking for a great deal of people, but not all that’s lost is found. Believe me, with my connections and skillset I’ll be much safer right here in Rheinland. ",
        # ),
        VoiceLine(
            960,
            Hassler,
            comment='Аномалия рядом',
            ru="А вот и аномалия. Активирую...",
            en="And here's the anomaly. Activating...",
        ),
        VoiceLine(
            970,
            Alaric,
            ru="Чёрт, корсары!",
            en="Damn, Corsairs!",
        ),
        VoiceLine(
            980,
            Trent,
            ru="Атакуем",
            en="Attacking.",
        ),
        VoiceLine(
            990,
            Hassler,
            comment='Корсары убиты, теперь точно прощаемся',
            ru="Надеюсь, на этот раз нам не помешают. Активирую аномалию...",
            en="I hope they won't get in the way this time. Activating the anomaly...",
        ),
        VoiceLine(
            995,
            Hassler,
            ru="Есть! Быстрее, друзья!",
            en="Done! Hurry, friends!",
        ),
        VoiceLine(
            1000,
            Alaric,
            ru="Спасибо за все, Хасслер, удачи!",
            en="Thanks for everything, Hassler. Good luck!",
        ),
        VoiceLine(
            1010,
            Trent,
            ru="Спасибо, Хасслер, надеюсь еще встретимся!",
            en="Thanks, Hassler. I hope we meet again!",
        ),
        VoiceLine(
            1020,
            Hassler,
            ru="Даже и не знаю. Вы приносите неприятности, Трент. Но, тем не менее, счастливо!",
            en="I don't even know. You bring trouble, Trent. But all the same, farewell!",
        ),
        VoiceLine(
            1030,
            Alaric,
            ru="Уф, проскочили. Трент, а где мы?",
            en="Whew, we made it through. Trent, where are we?",
        ),
        VoiceLine(
            1040,
            Trent,
            ru="Ты будешь удивлен, но, по-видимому, где-то в системе Форбс. После прохода аномалии навигационная система с ума сходит, надо дать ей время прийти в себя.",
            en="You'll be surprised, but apparently somewhere in the Forbes system. After going through the anomaly, the navigation system goes crazy. We need to give it time to recover.",
        ),
        VoiceLine(
            1050,
            Trent,
            ru="А пока... Поблизости есть верфь Филадельфия, полетели на неё.",
            en="Meanwhile... There's the Philadelphia shipyard nearby. Let's fly to it.",
        ),
        VoiceLine(
            1060,
            Alaric,
            ru="Вперед!",
            en="Forward!",
        ),
        VoiceLine(
            1070,
            HatcherStation,
            ru="Мистер Трент, полагаю?",
            en="Mr. Trent, I presume?",
        ),
        VoiceLine(
            1080,
            Trent,
            ru="Правильно полагаете.",
            en="You presume correctly.",
        ),
        VoiceLine(
            1090,
            HatcherStation,
            ru="Мы ждали вас и... это не мистер Джакобо!",
            en="We were waiting for you and... this isn't Mr. Jacobo!",
        ),
        VoiceLine(
            1100,
            Trent,
            ru="Правильно, это не мистер Джакобо. Мистер Джакобо погиб, когда нас прижали Рейнландские военные. ",
            en="Correct. This isn't Mr. Jacobo. Mr. Jacobo died when the Rheinland military had us cornered.",
        ),
        VoiceLine(
            1110,
            Trent,
            ru="Однако, копия того что он вез, у меня на борту. Вам все еще интересны эти документы?",
            en="However, a copy of what he was carrying is aboard. Are these documents still of interest to you?",
        ),
        VoiceLine(
            1120,
            HatcherStation,
            ru="Да! Безусловно интересны!",
            en="Yes! They certainly are!",
        ),
        VoiceLine(
            1130,
            Trent,
            ru="Я готов их вам передать. Кстати, с кем имею честь?",
            en="I'm ready to transfer them to you. By the way, with whom do I have the honor?",
        ),
        VoiceLine(
            1140,
            HatcherStation,
            ru="Можете звать меня Хетчер, мистер Трент. Мы доверяем вам, мистер Трент. Для обмена проследуйте, пожалуйста, на планету Форбс. Встретимся в баре.",
            en="You may call me Hatcher, Mr. Trent. We trust you, Mr. Trent. For the exchange, please proceed to planet Forbes. We'll meet in the bar.",
        ),
    ]


class Mission4(Msn4, script.StoryMission):
    MISSION_INDEX = 4
    CUTSCENES = [
        Msn4Offer,
        Msn4Reward,
        Msn4Final,
    ]
    SPACE_CLASS = Msn4Space
    SYNC_SPACE = True
    SYNC_SUBS = True

    MISSION_TITLE = 'Миссия 4. Сопровождение Джакобо'