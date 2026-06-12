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
                  en="Thank you so much for coming. I need your help. I'm in big trouble. Rheinland authorities are coming for me."),
        VoiceLine(30, Trent, ru="Это я уже понял. И у меня появилось знакомое ощущение что меня очень хотят втянуть в неприятности.",
                  en="I figured. Rheinland seems to be making a habit of roughing up civilians."),
        VoiceLine(40, Jacobo, ru="Герр Трент, вы не понимаете. Дело исключительной важности. Мне необходимо доставить в Либерти важные документы.",
                  en="No, Herr Trent, you do not understand. I know too much. They are trying to kill me. Please, I must deliver these documents to Liberty - everything is explained inside. The fate of the universe depends on it."),
        VoiceLine(50, Trent, ru="Опять меня угораздило вляпаться в шпионские игры... Джакобо, вы в курсе, что в данный момент я работаю на те самые власти Рейнланда, которые вас ищут?",
                  en="Yet again I'm dragged into a game of international espionage and subterfuge... Jacobo, are you aware I literally just did a job for the very same Rheinland authorities you're running from now?"),
        VoiceLine(60, Jacobo, ru="Герр Трент, вы же фриленсер. Вы не давали никаких присяг. После выполнения задания вас с заказчиком ничего не связывает. ",
                  en="Herr Trent, you're a freelancer. You did not take an oath. You owe your allegiance to no one. After a job is done, it is done. I will make it worth your while."),
        VoiceLine(62, Jacobo, ru="Герр Трент, если мы сможем доставить эти ОЧЕНЬ важные документы в Либерти, в систему Форбс, нам заплатят очень большие деньги, ОЧЕНЬ большие, понимаете? ",
                  en="When we deliver these top secret documents to the Forbes system, Liberty will pay us a boat load of money, and I mean a huge aircraft carrier sized boat of money... do you understand?"),
        VoiceLine(65, Jacobo, ru="У меня одного это скорее всего не получится, но если вы мне поможете... ", en="I know I won't make it without your protection..."),
        VoiceLine(67, Jacobo, ru="А если вы мне не поможете, меня скорее всего просто убьют... ", en="If you don't help me, I'm a dead man..."),
        VoiceLine(70, Trent, ru="Я об этом еще пожалею... Хорошо, каков план?", en="I'm so gonna regret doing this... Sigh. Okay, what's the plan?"),
        VoiceLine(80, Jacobo, ru="Герр Трент, спасибо, вы не пожалеете! Вылетайте в космос, я с помощью друзей попробую незаметно пробраться на взлетную площадку. Встретимся на орбите.",
                  en="Herr Trent, my saviour! I'll make sure to pay off whatever regrets you might have in triplicate! Launch into space. Meet me in orbit."),
        VoiceLine(90, Trent, ru="Тогда до встречи.", en="See you up there, Jacobo."),
    ]


class Msn4Reward(Msn4, script.CutsceneProps):
    ALIAS = 'reward'
    TITLE = 'Вознаграждение'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Hatcher, ru="Мисс Хетчер.", en="Gentlemen."),
        VoiceLine(20, Trent, ru="Мисс Хетчер.", en="Miss Hatcher."),
        VoiceLine(30, Alaric, ru="Мисс Хетчер, у вас такие красивые бездонные глаза, что...", en="Why Miss Hatcher, what big eyes you have."),
        VoiceLine(40, Hatcher, ru="Что вы перестанете нести эту околесицу, иначе я рассержусь", en="Cut the crap mister, you don't wanna see my teeth. I bite."),
        VoiceLine(45, Hatcher, ru=". О деле. Все выполнено на лучшем уровне. ", en="Anyway, let's get to business. You two have done a stand-up job."),
        VoiceLine(50, Hatcher, ru="Я даже не буду спрашивать чего стоило вам сбежать из Рейнланда с ТАКИМИ документами", en="I won't ask how you managed to escape Rheinland in possession of something like THIS."),
        VoiceLine(55, Hatcher, ru="Я девушка впечатлительная, боюсь в обморок упасть.", en="I'm afraid it might be too much for my delicate disposition."),
        VoiceLine(60, Trent, ru="Мы старались.", en="*coughs* Well, let's just say we did what we had to do."),
        VoiceLine(70, Hatcher, ru="Хе, вы тоже были в этом заинтересованы. А кстати, нам как раз нужны такие умелые и предприимчивые люди как вы, для выполнения, скажем так, нестандартных заданий. Вы в ближайшее время не слишком заняты?", en="Sounds like you two had fun. Good job again. By the way, we're in the market for top Freelancers to execute some... unusual missions. Are you two available?"),
        VoiceLine(80, Alaric, ru="Заткнись, Аларик. Нет, с тех пор как мы стали врагами Рейнландского государства, работы у нас поубавилось.", en="For you, Miss Wolf, anything..."),
        VoiceLine(90, Trent, ru="Заткнись, Аларик. Нет, с тех пор как мы стали врагами Рейнландского государства, работы у нас поубавилось.", en="Shut up, Alaric. Well, seeing as we're now enemies of Rheinland, I suppose some vacancies have opened up."),
        VoiceLine(100, Hatcher, ru="То есть если у нас найдется пара заданий по вашему профилю за достойную плату...", en="So, if say I had a couple of well-paying missions..."),
        VoiceLine(110, Trent, ru="То мы не против их выполнить, если конечно же эти задания не приведут к тому что мы станем государственными преступниками и в Либерти.", en="Say no more. That is, unless these missions wind up turning all of Liberty against us too..."),
        VoiceLine(120, Hatcher, ru="О, нет, я думаю до этого не дойдет.", en="Oh no, I don't think you'll be in that deep."),
        VoiceLine(130, Trent, ru="Я вот тоже думал...", en="That's what she said..."),
    ]


class Msn4Final(Msn4, script.CutsceneProps):
    ALIAS = 'final'
    TITLE = 'Вознаграждение'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Alaric, ru="Круто, Трент, ты умеешь находить себе заказчиков и покровителей.", en="Awesome, Trent! Who knew you'd turn out so good at bagging clients and closing deals? The student has become the master!"),
        VoiceLine(20, Trent, ru="А так же врагов и убийц.", en="Seems more like my talent is making enemies and getting us half killed."),
        VoiceLine(30, Alaric, ru="Да ладно тебе. Ты фриленесером работать стал всего ничего, и вот уже задания на уровне правительств с соответствующей оплатой.", en="Oh come now... one moment you're a newbie freelancer, the next you're raking in big bucks from international governments! Don't sell yourself short!"),
        VoiceLine(40, Trent, ru="Ага, и одно из правительств уже назначило награду за мою голову, и я сомневаюсь что у этого правительства короткая память.", en="Mhm, well we're wanted fugitives of one of those government now. Think they'll forget about us anytime soon? I kinda crave Sauerkraut."),
        VoiceLine(50, Alaric, ru="Да ладно тебе, с таким прикрытием рейнландцы пупок себе скорее надорвут, чем нас достанут.", en="Well, word is the Rheinland military has much bigger fish to fry. I doubt they'll bother coming after small fry like us."),
        VoiceLine(60, Trent, ru="С каким-таким прикрытием? Ну-ка Аларик, чего я не знаю?", en="Hmm. I know that tone of voice. Same's when you went after my ex girlfriend... Come on, Alaric, what are you hiding from me?"),
        VoiceLine(70, Alaric, ru="Эта мисс Хетчер, ты в курсе кто она?", en="That was a long time ago... and nothing happened. That foxy lady, Miss Hatcher, you don't know who she is?"),
        VoiceLine(80, Trent, ru="Ну конечно в курсе. Я знаю её уже целых три часа, я в курсе. Аларик, короче, мать твою!", en="Yeah sure I do. She's our next paycheck. And way out of your league. Spit it out, Alaric."),
        VoiceLine(90, Alaric, ru="Она офицер в одной из спецслужб Либерти.", en="She's only one of the most senior officers in one of Liberty's most clandestine agencies."),
        VoiceLine(100, Trent, ru="О боже! Нет... Опять...", en="Oh..."),
        VoiceLine(110, Alaric, ru="Ты не понимаешь, это настолько крутая спецслужба, что другие спецслужбы даже не подозревают о её существовании.", en="Yeah. It's so secret most of Liberty doesn't even know it exists."),
        VoiceLine(120, Trent, ru="Аларик, тогда ты то откуда про это знаешь?", en="So then how do you know about it, Alaric?"),
        VoiceLine(130, Alaric, ru="А... Э-э-э...", en="Oh look at the time... I need to go..."),
        VoiceLine(140, Trent, ru="Короче, трындец, опять вляпался.", en="I can't believe this is happening again! Just my dumb luck."),
    ]


class Msn4Space(Msn4, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(
            0,
            JacoboTrader,
            ru="Герр Трент, это Джакобо! Герр Трент, вы помните меня? Герр Трент, нам очень нужна ваша помощь. Вы же были не против помочь нам если понадобится, помните? Герр Трент, прошу вас как можно быстрее прибыть на планету Норторф в систему Мюнхен!",
            en="Herr Trent, this is Jacobo! You said you would help me if I ever had need, do you recall? My friend, I really need your help now. I am in grave danger. Please come to me at planet Nortorf in the Munich system as quickly as you can!",
        ),
        VoiceLine(
            10,
            Trent,
            ru="Джакобо, Дромадер? Что это за ведро?",
            en="Jacobo, a Dromedary? You couldn't have found something slower for a quick getaway? Just how many documents are you stealing anyway!",
        ),
        VoiceLine(
            20,
            JacoboTrader,
            ru="Мой корабль засвечен, за ним постоянная слежка, это единственное, что я смог быстро и незаметно купить.",
            en="My old ship was tagged by the authorities. This was the only thing I could get my hands on at short notice.",
        ),
        VoiceLine(
            30,
            Trent,
            ru="Но ты же понимаешь, что если начнется заварушка, он развалится от первого же плевка?",
            en="Dude, that crate is even less spaceworthy than my old ship, and twice as slow! ",
        ),
        VoiceLine(
            40,
            JacoboTrader,
            ru="У меня нет выбора. Хотя вы правы, Герр Трент, документы обязательно должны попасть к заказчику. Сейчас я передам вам копии, откройте канал.",
            en="Beggars can't be choosers, but you have a point. Just in case I don't survive, these documents must reach the customer. I will send you a copy now, please open your comms channel.",
        ),
        VoiceLine(
            50,
            Trent,
            ru="Передача завершена успешно. Как будем пробиваться в Либерти?",
            en="Transfer complete. Which way are going?",
        ),
        VoiceLine(
            60,
            JacoboTrader,
            ru="Власти Рейнланда в курсе всех моих действий, мне еле удалось улизнуть когда они за мной пришли, поэтому короткая дорога не для нас. ",
            en="The Rheinland authorities are tracking me. I barely managed to escape when they first came for me, so conventional routes are not an option.",
        ),
        VoiceLine(
            70,
            JacoboTrader,
            ru="У врат в Хонсю нас скорее всего ждут. Попробуем в обход через территорию Рейналанда. Берем курс на систему Бисмарк.",
            en="They are probably waiting for me at the gate to Honshu. Let's make a beeline through Rheinland territory. Set course to Bismarck.",
        ),
        VoiceLine(
            80,
            Trent,
            ru="Логично. Если тебя разыскивают власти Рейнланда, куда лучше всего лететь? Правильно, в столицу...",
            en="The capital?! Riiight... makes perfect sense. Just make a beeline for the beehive... uh huh.",
        ),
        VoiceLine(
            90,
            JacoboTrader,
            ru="Если есть другие предложения...",
            en="I'm open to alternatives... ",
        ),
        VoiceLine(
            100,
            Trent,
            ru="Нет других предложений, Джакобо, просто мысли вслух.",
            en="Nah I got nothing. Let's go. ",
        ),
        VoiceLine(
            110,
            Kreitmaier,
            ru="С вами говорит командир спецгруппы Гессенский Лев Маркус Крейтмайер.",
            en="This is commander Marcus Creitmire of the Hessian Lions special operations unit.",
            cinematic=True,
        ),
        VoiceLine(
            120,
            Kreitmaier,
            ru="Немедленно отключите оружейные системы и следуйте с нами под конвоем. В случае сопротивления у нас есть полномочия вас уничтожить.",
            en="Power down your weapons immediately and follow our lead. If you resist, we are authorized to use deadly force.",
            cinematic=True,
        ),
        VoiceLine(
            130,
            Trent,
            ru="Недолго музыка играла... Джакобо, тут без шансов. Маркус, банкуйте, мы сдаемся.",
            en="Well so much for that genius plan... Jacobo, we don't stand a chance. We have to surrender. Marcus, be gentle on us.",
        ),
        VoiceLine(
            140,
            Kreitmaier,
            ru="Следуйте под нашим конвоем к станции Кёльн.",
            en="We're escorting you to the Cologne station. ",
        ),
        VoiceLine(
            150,
            JacoboTrader,
            ru="Это же главная военная база Рейнланда! Да что мы такого сделали? На каком основании? Какие преступления нам вменяют, в конце концов?",
            en="What? That's the Rheinland ministry of war! What crimes are we accused of? Do you have probable cause?",
        ),
        VoiceLine(
            160,
            Kreitmaier,
            ru="Вы не в том положении, чтобы задавать вопросы. Следуйте нашим указаниям.",
            en="We aren't obliged to answer your questions. You can do this the easy way, or the dead way.",
        ),
        VoiceLine(
            170,
            Trent,
            ru="Джакобо, угомонись.",
            en="Jacobo, calm down. Don't give them a reason to hurt us.",
        ),
        VoiceLine(
            180,
            Reichman,
            ru="Герр Крейтмайер, говорит адмирал Р+айхманн. Благодарю вас за успешно выполненное задание.",
            en="Herr Creitmire, this is Admiral Reichmann. Congratulations on completing your mission.",
            cinematic=True,
        ),
        VoiceLine(
            190,
            Reichman,
            ru="Доставьте грузовик типа Дромадер на базу для досмотра. Сопровождавший его корабль приказываю уничтожить.",
            en="Take the Dromedary to base for inspection. Dispose of the escort. ",
            cinematic=True,
        ),
        VoiceLine(
            200,
            Kreitmaier,
            ru="Уничтожить? Он доставлен под конвоем, адмирал. Как уничтожить?",
            en="Dispose of...? He's just an escort, admiral.",
        ),
        VoiceLine(
            210,
            Reichman,
            ru="М+олча и быстро. И не пререкаясь со старшими по званию!",
            en="Question me again and you will be... replaced. Schnell. And be discreet.",
        ),
        VoiceLine(
            220,
            Hassler,
            comment='Вот это поворот! Появляется внезапный бог из машины!',
            ru="Герр Крейтмайер, вас ввели в заблуждение! Заговор! Освободите конвоируемых!",
            en="Herr Creitmeier, you are making huge a mistake. Release the escort now!",
        ),
        VoiceLine(
            230,
            Alaric,
            ru="Слова - это слишком долго. Торпеды быстрее.",
            en="Words slow. Torpedoes fast. Eat my Boom.",
        ),
        VoiceLine(
            240,
            Reichman,
            ru="Боевая тревога! Уничтожить агрессоров!",
            en="Red alert! To your stations! Destroy the aggressors!",
        ),
        VoiceLine(
            250,
            Kreitmaier,
            ru="Боевая тревога!",
            en="Battle alert! ",
        ),
        VoiceLine(
            260,
            Trent,
            comment='Начинается битва!',
            ru="Спасибо, ребята, теперь валим отсюда!",
            en="Thanks for the save, guys. Now let's get the hell outta here! ",
        ),
        VoiceLine(
            270,
            Hassler,
            ru="Не так быстро, Трент. Видишь этот линкор поблизости? Стоит нам отлететь от станции - он нас на атомы распылит из своих орудий.",
            en="Not so fast, Herr Trent. You see that battleship over there? As soon as we get far enough from the station, it'll pound us into stardust with its railgun.",
        ),
        VoiceLine(
            280,
            Hassler,
            ru="А пока мы рядом с Кёльном он стрелять не будет, побоится задеть станцию. Но у меня есть одна идея.",
            en="It can't fire as long as we stay near to Cologne because it might destroy the station... this gives me an idea...",
        ),
        VoiceLine(
            290,
            Hassler,
            comment='Хасслер выстреливает какой-то торпедой по боковой панели реактора линкора',
            ru="(в пылу боя) Маленький сюрприз от знакомых Изгоев: сверхмощная торпеда. Трент, я нанёс критический урон по линкору, но второй такой торпеды у меня нет. Ты должен добить реактор линкора и пустить его вразнос!",
            en="A little torpedo surprise from our Outcast friends. Trent, I've weakened the armor around the battleships' reactor. I don't have another torpedo. We need to punch through to the reactor. ",
        ),
        VoiceLine(
            300,
            Hassler,
            ru="(в пылу боя) Этот линкор стоит на ремонте, у него как раз проблемы с системой охлаждения. Постарайся как можно быстрее! Мы с Алариком займемся истребителями!",
            en="According to our intelligence the battleship is the Wotan, and it has a malfunctioning cooling system. Even minor damage to the reactor should result in catastrophic failure. Be fast and precise. Alaric and I will hold off of the fighters!",
        ),
        VoiceLine(
            310,
            Hassler,
            comment='Линкор взорвался!',
            ru="А теперь действительно валим отсюда. Скорее!",
            en="Now, let's, as Herr Trent put it so well, get the hell outta here. ",
        ),
        VoiceLine(
            320,
            Alaric,
            ru="Включаем круиз!",
            en="Cruise engines online!",
        ),
        VoiceLine(
            330,
            Trent,
            comment='Летим',
            ru="А теперь, объясните мне, пожалуйста, что за хрень вообще происходит? Во что влип Джакобо и я вместе с ним?",
            en="Now, could someone please tell me what the hell is going on? What has Jacobo gotten me into now?",
        ),
        VoiceLine(
            340,
            Hassler,
            ru="Герр Трент, вы оказались не в том месте и не в то время.",
            en="Herr Trent, you seem to make a habit of being in the wrong place, at the wrong time.",
        ),
        VoiceLine(
            350,
            Trent,
            ru="у, с этим у меня как раз порядок, люблю я это дело.",
            en="Yeah it's my lucky day...",
        ),
        VoiceLine(
            360,
            Hassler,
            ru="Как вы помните, финал миссии в Кёнигсберге выглядел со всех сторон сомнительно. И я решил копнуть глубже.",
            en="Do you recall how our stint in Konigsberg wound up disappointing the General? I found it suspicious, so I dug deeper.",
        ),
        VoiceLine(
            410,
            Hassler,
            ru="Я выяснил, что Дитрих в своё время смог выкрасть из генштаба Рейнланда некие важные сверхсекретные документы. Так вот, вся операция была затеяна для того чтобы эти документы вернуть.",
            en="Turns out someone... acquired some extremely important documents from a mole in Rheinland’s Joint Staff. So the real goal of the mission all along was to retrieve the documents, not to take out Dietrich and his men.",
        ),
        VoiceLine(
            420,
            Hassler,
            ru="Если бы Райхман достал документы, а Дитрих при этом скрылся, операция всё равно была бы признана успешной.",
            en="Dietrich was just a red herring to lend legitimacy to the whole operation.",
        ),
        VoiceLine(
            560,
            Hassler,
            ru="Кстати, герр Трент, позвольте поинтересоваться, а чем вы вообще занимались непосредственно перед нашим появлением? Вас конвоировали в сопровождении государственного преступника.",
            en="By the way, Herr Trent, i'm curious: what were you doing here when we arrived? You weren't escorting a known fugitive and enemy of the state by any chance...? ",
        ),
        VoiceLine(
            570,
            JacoboTrader,
            ru="Это все какое-то недоразумение.",
            en="Uhhh... this is all just a huge misunderstanding...",
        ),
        VoiceLine(
            590,
            Trent,
            ru="Джакобо попросил эскортировать его на территорию Либерти. Неплохой парень, мы с ним пересекались по делу когда я работал под юрисдикцией небезызвестного вам герра Вильгельма.",
            en="Jacobo here paid me to escort him to Liberty. He’s a friend of mine, helped me out when I was on the job for Herr Wilhelm. I'm sure this is all just a setup.",
        ),
        VoiceLine(
            600,
            Hassler,
            ru="Интересно, и зачем же этому неплохому парню понадобился эскорт в Либерти?",
            en="Fascinating. And why exactly does your friend need an escort to Liberty?",
        ),
        VoiceLine(
            610,
            JacoboTrader,
            ru="Мне нужно срочно доставить важные документы в систему Форбс.",
            en="Uh, I urgently need to deliver some important documents to the Forbes system. ",
        ),
        VoiceLine(
            620,
            Hassler,
            ru="Важные документы, говорите... В либерти... В любом случае, господа, нам необходимо как можно скорее покинуть территорию Рейнланда. Нельзя слишком долго искушать судьбу.",
            en="What a curious coincidence. Secret documents bound for Liberty, you say... Well, whatever the case we need to get out of Rheinland as soon as possible. Luck only favours the foolish, until she kills them. ",
        ),
        VoiceLine(
            630,
            Hassler,
            comment='Вражеский крейсер и истребители после вылета из гипердыры',
            ru="Засада! Как они нас нашли?",
            en="Sheisse! How'd they find us?",
        ),
        VoiceLine(
            9150,
            Alaric,
            ru="Тут целый крейсер, а у меня кончились боеприпасы! Трент, атакуй уязвимые точки крейсера! Мы его и так разнесём!",
            en="Mein Gott, a battle cruiser! My ammo is spent, Trent, take out the cruiser!",
        ),
        VoiceLine(
            9200,
            Sigma8Cruiser,
            ru="Прекратите сопротивление! Вам не уйти!",
            en="Resistance is futile! You will be as.. saulted!",
        ),
        VoiceLine(
            640,
            JacoboTrader,
            ru="Помогите! Они сейчас меня сожгут!",
            en="I'm hit! On fire! All systems failing!",
        ),
        VoiceLine(
            650,
            JacoboTrader,
            ru="А-а-а-ргхх...",
            en="А-а-а-rrgghhhh...",
        ),
        VoiceLine(
            660,
            Trent,
            ru="Твою же мать!",
            en="Motherfuckers! You'll pay for that!",
        ),
        VoiceLine(
            9300,
            Hassler,
            comment='Враги уничтожены',
            ru="Скорее уходим!",
            en="Come on Trent, we gave to get outta here.",
        ),
        VoiceLine(
            670,
            Hassler,
            comment='Пока летим...',
            ru="Очень интересно.",
            en="Strange.",
        ),
        VoiceLine(
            680,
            Trent,
            ru="И что же вас так заинтересовало, герр Хасслер.",
            en="Jacobo's dead. What are you going on about, Herr Hassler? ",
        ),
        VoiceLine(
            690,
            Hassler,
            ru="Вражеский отряд вёл концентрированный огонь по самому безобидному кораблю из нашей команды. Это выглядит весь странно, герр Трент, не находите?",
            en="Those fighters’ tactics - didn't they strike you as strange? They only targeted the weakest ship without concern for their own lives while we picked them off.",
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
            en="I guess their mission was to take out the Dromedary at all costs... Or its' cargo. ",
        ),
        VoiceLine(
            720,
            Hassler,
            ru="Вот и я о том же. Документы. Кстати, герр Трент, документов теперь нет? Конец истории?",
            en="Yes I think so too. So, (maliciously) Mr Trent, what now? Another last-minute failure like Konigsberg, now that the documents are vaporized?",
        ),
        VoiceLine(
            730,
            Trent,
            ru="Не совсем. У меня сохранились копии.",
            en="Not this time. I have a backup.",
        ),
        VoiceLine(
            740,
            Hassler,
            ru="Ха-ха-ха, герр Трент, с вами очень приятно и интересно работать. Я не завидую вашим врагам.",
            en="Ha-ha-ha, Mr Trent, I do enjoy working with you. I certainly wouldn’t want to get on your bad side.",
        ),
        VoiceLine(
            750,
            Alaric,
            ru="А знаете что... Было бы еще интереснее завершить эту миссию. Джакобо убит, но у нас есть координаты заказчика и есть то, что ему нужно. Думаю, это будет не только интересно, но и прибыльно.",
            en="Guys, you know what... Let’s complete the delivery. Jacobo may be dead, but we have the buyers' location. Aren't you all curious how this ends? And... somebody has to collect all that money...",
        ),
        VoiceLine(
            760,
            Hassler,
            ru="А нам ведь больше и некуда деваться. Так ведь, герр Трент?",
            en="Well, it's not like we have anything better to do. Herr Trent? ",
        ),
        VoiceLine(
            770,
            Trent,
            ru="Слушайте, Хасслер, мне этот ваш герр настолько надоел в Рейнланде... Можно просто Трент? Тем более что мы в Либерти летим?",
            en="Listen, Hassler. I’m sick and tired of your Herr this and that, let's just lose the formalities okay? Call me Trent. You know, when in Rome, do as the Romans do.",
        ),
        VoiceLine(
            780,
            Hassler,
            ru="Как вам будет угодно, герр Трент.",
            en="But that's all Greek to me, Mr Trent.",
        ),
        VoiceLine(
            790,
            Trent,
            ru="Не самое подходящее время веселиться. Лучше посоветуйте как в Либерти проще пробраться, мы все-таки еще на территории Рейнланда, где нас, скорее всего уже в государственных преступников записали.",
            en="Guess I walked into that one. Okay any idea how we can get to Liberty stat? We’re still in Rheinland territory, and after taking out a battleship and cruiser we’re probably on the naughty list. ",
        ),
        VoiceLine(
            800,
            Hassler,
            ru="Нет ничего проще, мы воспользуемся моим устройством для активации аномалий и покинем Рейнланд через обходной путь.",
            en="Augsburg outpost.",
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
            en="Attention! You are entering restricted space. Turn off your weapon systems immediately and land or face the consequences! ",
        ),
        VoiceLine(
            910,
            Hassler,
            ru="Не обращайте внимания, у них нет сил, достаточных чтобы перехватить нас. Видите, ни один истребитель не вылетел на перехват. Продолжаем движение.",
            en="Don’t pay them any heed, they’re all bark and no bite. They don't even have a fighter wing. Keep moving.",
        ),
        VoiceLine(
            920,
            Sigma8Outpost,
            ru="Это аванпост Аугсбург, повторяю, немедленно...",
            en="This is Augsburg, I repeat, turn off your...",
        ),
        VoiceLine(
            930,
            Trent,
            ru="Аванпост Аугсбург, отвалите, немедленно, повторяю, немедленно отвалите.",
            en="Augsburg, piss off. I repeat, piss off, motherfuckers. ",
        ),
        VoiceLine(
            940,
            Alaric,
            ru="Ха-ха-ха.",
            en="Ha-ha-ha. ",
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
            en="Ok, heads up: the anomaly will get you to Liberty, but I’m not sure where exactly in Liberty it'll pop up. So be ready for anything when you exit, you guys. ",
        ),
        VoiceLine(
            870,
            Alaric,
            ru="В смысле вам? Ты с нами не летишь?",
            en="What do you mean you guys? Aren’t you coming with us? ",
        ),
        VoiceLine(
            875,
            Hassler,
            ru="Нет, спасибо, мне гораздо комфортнее будет залечь на дно на периферии Рейнланда. Ну и как бывшему офицеру спецслужб мне было бы очень опасно появляться в Либерти. Я слишком много знаю.",
            en="No. I’m better off going to ground here in Rheinland than being seen flying straight into the hands of Liberty. I imagine I'd be gutted for the things I could disclose as a former intelligence officer...  So, no thanks. ",
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
            en="And here's the anomaly. Activating... ",
        ),
        VoiceLine(
            970,
            Alaric,
            ru="Чёрт, корсары!",
            en="Curses, Corsairs! Of all the shitty timing! ",
        ),
        VoiceLine(
            980,
            Trent,
            ru="Атакуем",
            en="Engaging!",
        ),
        VoiceLine(
            990,
            Hassler,
            comment='Корсары убиты, теперь точно прощаемся',
            ru="Надеюсь, на этот раз нам не помешают. Активирую аномалию...",
            en="Okay, that's sorted. Peace and quiet at last, I hope. Activating the anomaly...",
        ),
        VoiceLine(
            995,
            Hassler,
            ru="Есть! Быстрее, друзья!",
            en="Get a move on, guys! ",
        ),
        VoiceLine(
            1000,
            Alaric,
            ru="Спасибо за все, Хасслер, удачи!",
            en="Thank you for everything Hassler. And best of luck!",
        ),
        VoiceLine(
            1010,
            Trent,
            ru="Спасибо, Хасслер, надеюсь еще встретимся!",
            en="Thanks, Hassler. I hope we meet again! ",
        ),
        VoiceLine(
            1020,
            Hassler,
            ru="Даже и не знаю. Вы приносите неприятности, Трент. Но, тем не менее, счастливо!",
            en="I don’t. You're a one-man disaster magnet, Trent. Take care, and be safe, guys! ",
        ),
        VoiceLine(
            1030,
            Alaric,
            ru="Уф, проскочили. Трент, а где мы?",
            en="Oof, that was rough. I feel sick. Where are we, Trent?",
        ),
        VoiceLine(
            1040,
            Trent,
            ru="Ты будешь удивлен, но, по-видимому, где-то в системе Форбс. После прохода аномалии навигационная система с ума сходит, надо дать ей время прийти в себя.",
            en="Well what do you know, we’re in the Forbes system! My luck must be turning around. ",
        ),
        VoiceLine(
            1050,
            Trent,
            ru="А пока... Поблизости есть верфь Филадельфия, полетели на неё.",
            en="Ah! I see Philadelphia shipyard. Let’s get going. ",
        ),
        VoiceLine(
            1060,
            Alaric,
            ru="Вперед!",
            en="Crack on, then!",
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
            en="That’s me. ",
        ),
        VoiceLine(
            1090,
            HatcherStation,
            ru="Мы ждали вас и... это не мистер Джакобо!",
            en="We've been waiting for you and... Wait, that’s not Mr. Jacobo!",
        ),
        VoiceLine(
            1100,
            Trent,
            ru="Правильно, это не мистер Джакобо. Мистер Джакобо погиб, когда нас прижали Рейнландские военные. ",
            en="Nope, it’s not Mr. Jacobo. Mr. Jacobo died at the hands of the Rheinland military.",
        ),
        VoiceLine(
            1110,
            Trent,
            ru="Однако, копия того что он вез, у меня на борту. Вам все еще интересны эти документы?",
            en="However, he left me a copy of his precious cargo in my databanks. Are you still interested in doing business? ",
        ),
        VoiceLine(
            1120,
            HatcherStation,
            ru="Да! Безусловно интересны!",
            en="Yes. Yes we are.",
        ),
        VoiceLine(
            1130,
            Trent,
            ru="Я готов их вам передать. Кстати, с кем имею честь?",
            en="I’ll gladly hand them over to you for the payment. By the way, to whom do I owe the honor? ",
        ),
        VoiceLine(
            1140,
            HatcherStation,
            ru="Можете звать меня Хетчер, мистер Трент. Мы доверяем вам, мистер Трент. Для обмена проследуйте, пожалуйста, на планету Форбс. Встретимся в баре.",
            en="You can call me Hatcher, Mr. Trent. We’ll make the exchange at the bar on planet Forbes, please follow us there and allow me to buy you a drink.",
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