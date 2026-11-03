from story import script
from audio.sound import VoiceLine
from audio.delivery import *
from story.actors import (
    Trent, IntroBarman, Jameson, Stewardess, Alaric, Informer, Dietrich, Adelmar, Luc, BrandenburgOutpost, BrandenburgCruiser
)


class Msn1(object):
    MISSION_INDEX = 1


class Msn1Intro(Msn1, script.CutsceneProps):
    ALIAS = 'intro'
    TITLE = 'Интро'
    DESCRIPTION = 'Трент подходит к бармену и своему рабодателю, мистер Харрисону (из финала фрила 1.0)'
    VOICE_LINES = [
        VoiceLine(10, Trent, ru="Всем доброго дня.", en="Good day, everyone."),
        VoiceLine(20, Jameson, ru="Здорова, Трент, пришел за новым нарядом?", en="Hey, Trent. Here for a new assignment?"),
        VoiceLine(30, Trent, ru="Нет, спасибо. Мистер Джеймсон, я пришел увольняться!", en="No, thanks. Mr. Jameson, I came to quit."),
        VoiceLine(40, Jameson, ru="С чего это? Опять поругался с кем-то на объекте?", en="How come? You get in another fight on site?"),
        VoiceLine(50, Trent, ru="Нет, всё серьёзно, смотрите.", en="No. It's serious. Look."),
        VoiceLine(70, Alaric, ru="Привет, Трент, это Аларик! У меня для тебя хорошие новости! Мне кажется, мы сможем поправить твое финансовое положение. Встречаемся на Магдебурге, в системе Сигма-13. До встречи!",
                  en="Hey, Trent, it's Alaric! I've got good news. I think we can sort out your money. Meet me on Magdeburg, in Sigma-13. See you!",
                      delivery=VERY_HIGH_PITCH),
        VoiceLine(80, Jameson, ru="А, этот прохиндей Аларик даже не сгинул в приграничье?", en="Huh. That crook Alaric didn't even get himself killed in the Border Worlds?"),
        VoiceLine(90, Trent, ru="Да, жив здоров! Так что хватит работать на дядю, пойду во фрилансеры, как мой знаменитый тёзка! Почему бы и нет?", en="Alive and well! So I'm done working for the boss. I'll go freelance, like my famous namesake. Why not?"),
        VoiceLine(100, Trent, ru="Заработаю денег столько, сколько вы и во снах не видовали!", en="I'll make more money than you've ever seen, even in your dreams!"),
        VoiceLine(110, Jameson, ru="Да, ты там и медаль одинокой звезды получить не забудь. Смотри не зазвездись, звёздный боец!", en="Sure. And don't forget your Lone Star medal. Don't let it go to your head, star fighter."),


        VoiceLine(120, IntroBarman, comment="Харрисон уходит", ru="Ну что, Трент, поздравляю тебя с началом новой жизни и получением билета не покидание этого болота!", en="Well, Trent. Congratulations on the new life, and on getting a ticket out of this swamp!", delivery=HAPPY),
        VoiceLine(130, Trent, ru="А ты чего сам не улетишь из этого болота?", en="Then why don't you fly out of this swamp yourself?"),
        VoiceLine(140, IntroBarman, ru="Нет, Трент, это твоё дело молодое. А я буду дальше помогать местным заблудшим душам. Не все же такие амбициозные, как ты!", en="No, Trent. That's a young man's business. I'll keep helping the lost souls around here. Not everyone's as ambitious as you."),
        VoiceLine(150, Trent, ru="Да, друг, без тебя здесь стало бы совсем тоскливо. Так, мой транспорт почти прибыл. Так что мне пора.", en="Yeah, friend. It'd be pretty dull here without you. Right, my transport's almost here. I should go."),
        VoiceLine(160, IntroBarman, ru="Давай, Трент, удачи!", en="Go on, Trent. Good luck!"),


        # VoiceLine(10, Trent, ru="Привет, целитель душ!", en="The Savior of my soul!"),
        # VoiceLine(20, IntroBarman, ru="Здарова, Трент! Тебе как обычно?", en="Welcome back, Trent. The usual?"),
        # VoiceLine(30, Trent, ru="Да, и сразу две!", en="No... you know what, gimme the good stuff."),
        # VoiceLine(40, IntroBarman, ru="Есть что отпраздновать?", en="Celebrating something special?"),
        # VoiceLine(50, Trent, ru="Есть. Даже два повода! Во-первых, я, наконец, рассчитался со всеми долгами!",
        #           en="Yeah. Two somethings. First up, I present the new improved debt-free Trent 2.0!"),
        # VoiceLine(60, IntroBarman, ru="За начало новой жизни! Эта - за счет заведения!",
        #           en="Ah, life after debt. Lazarus, this one's on me."),
        # VoiceLine(70, Trent, ru="Спасибо, дружище! Ты - лучший человек на этой богом забытой планете!",
        #           en="Thanks, bud. Everytime I hear you say that I suddenly remember who my favouritest person in the whole wide world is..."),
        # VoiceLine(80, IntroBarman,
        #           ru='Но если было "во-первых", то должно быть и "во-вторых". Давай рассказывай, я сейчас сдохну от любопытства.',
        #           en="Yeah yeah. So if there's a 'first up', there's gotta be a 'second up'. Spit it out already before I die of curiosity."),
        # VoiceLine(90, Trent, ru="Только попробуй! Это будет непоправимой утратой.",
        #           en="Don't you die on me. Wouldn't know where to get free drinks."),
        # VoiceLine(100, Trent, ru="Старый кореш прислал сообщение.",
        #           en="So anyway, an old friend sent me this pad-message."),
        # VoiceLine(105, Trent, ru='Смотри', en="Check it out."),
        # VoiceLine(110, Alaric,
        #           ru="Привет, Трент, это Аларик! У меня для тебя хорошие новости! Мне кажется, мы сможем поправить твое финансовое положение. Встречаемся на Магдебурге, в системе Сигма-13. До встречи!",
        #           en=">Greetings, loser! This is Alaric, your old buddy and life coach. Great news - I've found a gig that'll patch that black hole in your wallet. Meet me on Magdeburg, Sigma-13 System ASAP! And I mean now, like yesterday, Trent!"),
        # VoiceLine(120, Trent, ru="Что думаешь?", en="Whatcha reckon?"),
        # VoiceLine(130, IntroBarman, ru="Думаю, сегодня ты самый счастливый сукин сын на всей этой гребаной планете.",
        #           en="I think you're the luckiest son of a bitch this side of the planet."),
        # VoiceLine(140, Trent, ru="Да я не про это. Соглашаться? Лететь?",
        #           en="Naturally... but I mean... should I just up and go?"),
        # VoiceLine(150, IntroBarman,
        #           ru="Можно, конечно, вообще ничего не делать, оставить все как есть. Денег на кусок хлеба хватит, да и риска никакого, разве что сдохнуть лет в сорок от работы на шахте. Но, мне кажется, что если судьба дает тебе шанс вырваться из этого болота - грех его не использовать. Хотя, решать тебе.",
        #           en="Well let's see. You could stay here and hang with your only real friend in the universe, eke out a miserable living, freeze your ass off in that dingy little flat of yours and die an alcoholic washed-up loser decades from now. Or you could grab life by the horns and fly off to live a real life... but don't let me influence you unduly."),
        # VoiceLine(160, Trent, ru="А почему сам не улетишь из \"этого болота\"?",
        #           en="If you feel so strongly about leaving here why haven't you flown the coop?"),
        # VoiceLine(170, IntroBarman,
        #           ru="Это - моё болото. Я к нему прирос и я его люблю. И друзей, присылающих мен сообщения с просьбой все бросить и прилететь на Магдебург у меня нет. Да и потом, если я улечу, кто здесь будет исцелять души страждущих?",
        #           en="Well, see... this may be a shit hole, but it's my shit hole. My bar, my life... guess I've grown attached. And unlike you I don't have friends with get-rich-quick schemes offering to share the spoils. 'Sides if I leave, who'd save everyone's souls after a shitty day?"),
        # VoiceLine(180, Trent, ru="Да уж, без тебя здесь стало бы совсем тоскливо. Ну так я в космопорт?",
        #           en="You're right, without you this place just wouldn't be the same. I guess I'll be heading out to spaceport, then. Take care."),
        # VoiceLine(190, IntroBarman, ru="Удачи, Трент, надеюсь, мы здесь больше не увидимся.",
        #           en="Yeah go on, abandon me here. Good riddance to bad rubbish, don't let the door hit your ass on the way out... and Trent... good luck."),

    ]


class Msn1Cityscape(Msn1, script.CutsceneProps):
    ALIAS = 'cityscape'
    TITLE = 'Взлётная площадка'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Stewardess, ru="Ваши билет и документы, сэр.", en="Your ticket and documents, sir."),
        VoiceLine(20, Stewardess, ru="Трент?.. А вы...", en="Trent?.. And you are..."),
        VoiceLine(30, Trent, ru="Нет, просто однофамилец.", en="No. Just the same name."),
        VoiceLine(40, Trent, ru="Достало уже. Пока твой тезка спасает вселенную, ты впахиваешь на дядю не покладая рук и выплачиваешь долги.",
                  en="I'm sick of it. Your namesake saves the universe, and you break your back working for someone else, paying off debts."),
    ]


class Msn1Offer(Msn1, script.CutsceneProps):
    ALIAS = 'offer'
    TITLE = 'Сигма-13'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Alaric, ru="Здарова, дружище, рад видеть тебя!", en="Hey, friend. Good to see you!"),
        VoiceLine(20, Trent, ru="Привет, Аларик.", en="Hi, Alaric."),
        VoiceLine(30, Alaric, ru="Я слышал ты разобрался со всеми проблемами. Теперь никаких долгов, никаких обязательств, да?",
                  en="I heard you sorted everything out. No debts, no obligations now, right?"),
        VoiceLine(40, Trent, ru="Ага, а еще никаких денег и никакого корабля. Есть в этом и плюсы - никаких проблем с багажом. Все мое - на мне. ",
                  en="Yeah. And no money, and no ship. There's an upside, though. No luggage. Everything I own is on me."),
        VoiceLine(50, Alaric, ru="Подходящий момент чтобы начать жизнь с чистого листа, не так ли? ", en="Good time to start with a clean slate, isn't it?"),
        VoiceLine(60, Alaric, ru="Мне как раз нужен напарник для хорошо оплачиваемого задания.", en="I need a partner for a well-paid job."),
        VoiceLine(70, Alaric, ru="Корабль я тебе дам. Старичок, конечно, но пару полетов до регламентного ТО переживет.",
                  en="I'll give you a ship. It's old, sure, but it'll last a couple of runs until the next service."),
        VoiceLine(80, Alaric, ru="Нужно проводить пару рейнландских ребят из Берлина в Бисмарк. Платят хорошие деньги",
                  en="We need to escort a couple of Rheinland guys from Berlin to Bismark. They pay well."),
        VoiceLine(90, Trent, ru="Интересно, с чего бы рейнландским ребятам нанимать охрану для перелета из одной своей системы в другую? ",
                  en="Funny. Why would Rheinland guys hire an escort to fly from one of their own systems to another?"),
        VoiceLine(100, Trent, ru="А впрочем, корабль, говоришь? Ты не оставил мне шансов, Ал!", en="Anyway. A ship, you said? You didn't leave me a choice, Al!"),
        VoiceLine(110, Alaric, ru="Вот и договорились. Корабль ждет тебя в ангаре. Осмотри, все ли с ним в порядке. Я буду ждать тебя в космосе.",
                  en="Then it's a deal. The ship's waiting in the hangar. Check that it's all right. I'll wait for you in space."),
    ]


class Msn1Berlin(Msn1, script.CutsceneProps):
    ALIAS = 'berlin'
    TITLE = 'Берлин'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Alaric, ru="Приветствую, джентльмены. Это - Трент, мой друг о котором я вам рассказывал.", en="Hello, gentlemen. This is Trent, the friend I told you about."),
        VoiceLine(20, Adelmar, ru="Отлично. Рады вас видеть. У нас тут некоторые проблемы в системе, надеюсь, вам это не сильно помешало.", en="Excellent. Glad to see you. We've had some trouble in the system. I hope it didn't bother you much."),
        VoiceLine(30, Trent, ru="Нисколько. Я просто счастлив что прилетел сюда ", en="Not at all. I'm just glad I made it here."),
        VoiceLine(40, Luc, ru="Вот и отлично. Если все в сборе, давайте начнем.", en="Good. If everyone's here, let's begin."),
    ]


class Msn1Bizmark(Msn1, script.CutsceneProps):
    ALIAS = 'bizmark'
    TITLE = 'Бисмарк'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Adelmar, ru="Благодарю вас за сопровождение! Деньги уже перечислены на ваши счета!",
                  en="Thank you for the escort! The money is already in your accounts!"),
        VoiceLine(20, Trent, ru="Не стоит благодарности. ", en="Don't mention it."),
        # VoiceLine(30, Luc, ru="Кроме того, мы, как члены Ганзейского торгового сообщества, добавили вас в белый лист фрилансеров. ", en="As a.. how do you say... bogus? Sweetener of the deal? We have added you to our Hanseatic trading community freelancers' whitelist."),
        #VoiceLine(40, Luc, ru="Теперь вы можете брать к выполнению миссии Ганзейских купцов.", en="From now on, you may take on missions offered by Hanseatic merchants, mein friend."),
        #VoiceLine(50, Alaric, ru="А вот за это отдельное спасибо, джентльмены! Трент, ты слышал? Мы теперь на Рейнландской территории не просто голодранцы какие-то, а аккредитованные Ганзейским торговым сообществом официальные фрилансеры!", en="Ah, thank you so much for your kind generosity, gentlemen! Trent, you hear that? We have been elevated from bottom feeding gutter trash to honest to God accredited freelancers of the Hanseatic trading community!"),
        #VoiceLine(60, Trent, ru="Охренеть. ", en="I'm overwhelmed..."),
        VoiceLine(70, Luc, ru="И... Трент, бесплатный совет: как можно быстрее поменяй свой звездолёт на что-нибудь более современное. Без обид, но подобные раритеты нужно выставлять в музее, а не летать на них..", en="And... Trent, a free piece of advice. Change that ship for something more modern, as soon as you can. No offense, but relics like that belong in a museum, not in flight."),
        VoiceLine(80, Trent, ru="Я подумаю над этим.", en="I'll think about it."),
        VoiceLine(90, Alaric, ru="И как тебе новая жизнь Трент?", en="So, how's the new life, Trent?"),
        VoiceLine(100, Trent, ru="Волнительно. Но... сейчас у меня есть свой корабль, а за это я хоть дьяволу в глотку готов залезть.", en="Exciting. But... I've got my own ship now, and for that I'd fly down the devil's throat."),
        VoiceLine(110, Alaric, ru="Теперь у тебя еще и деньги есть на его обслуживание и переоборудование. А если подумать - то и на покупку нового. По большому счету, Луц в чем-то прав.", en="Now you've got money to maintain it and refit it. Enough for a new one, if you think about it. Lutz is right, more or less."),
        VoiceLine(120, Trent, ru="Да пошел он. Может у него и хватает денег чтобы корабли раз в год менять, а я пока еще миллионером не стал. ", en="Screw him. Maybe he's got the money to change ships once a year. I'm not a millionaire yet."),
        VoiceLine(125, Alaric, ru="Тогда стоит задуматься над апгрейдом того что есть. ", en="Then think about upgrading what you've got."),
        VoiceLine(130, Alaric, ru="В том бою, в астероидах, тебе иногда явно не хватало энергии. Тебе точно не помешает поменять генератор на более мощный. Да и остальную начинку посмотри. Этот корпус очень эластичен в плане апгрейда. Практически все модули можно поменять на более совершенные...", en="In that fight, in the asteroids, you were clearly short on power at times. You should swap the generator for a stronger one. And look at the rest of the hardware. This hull takes upgrades well. Almost every module can be replaced with a better one..."),
        VoiceLine(140, Alaric, ru="О-кей, Трент, у меня тут есть дела, требующие немедленного разрешения, поэтому я побежал. Освоишься без меня тут?", en="Okay, Trent. I've got business that can't wait, so I'm off. You'll manage here without me?"),
        VoiceLine(150, Trent, ru="Попробую... Удачи, Аларик!!!", en="I'll try... Good luck, Alaric!"),
        VoiceLine(160, Alaric, ru="Пока!", en="Bye!"),
    ]


class Msn1Space(Msn1, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(
            10,
            Alaric,
            ru="Эй, Трент! Поди забыл уже, с какой стороны подходить к креслу пилота?",
            en="Hey, Trent! Forgotten which side of the pilot's chair to get in from?",
        ),
        VoiceLine(
            20,
            Alaric,
            ru="Нам нужно добраться до гиперврат в Берлин. Я загрузил координаты торгового маршрута в твою нейросеть. Полетели!",
            en="We need to reach the jump gate to Berlin. I've uploaded the trade lane coordinates to your neural net. Let's go!",
        ),
        VoiceLine(
            30,
            Alaric,
            ru="Торговый маршрут активирован. Набираем максимальную скорость.",
            en="Trade lane activated. Full speed.",
        ),
        VoiceLine(
            40,
            Alaric,
            ru="Дело осталось за малым, активировать гиперврата в Берлин. Давай, Трент, ты первый.",
            en="Just one thing left. Activate the jump gate to Berlin. Go on, Trent, you first.",
        ),
        VoiceLine(
            50,
            Informer,
            ru="Приветствуем Вас в системе Берлин! В связи с аномальной пиратской активностью в системе все прибывающие должны пройти проверку и регистрацию на аванпосте Бранденбург.",
            en="Welcome to the Berlin system. Due to unusual pirate activity, all arriving ships must be checked and registered at Brandenburg Outpost.",
        ),
        VoiceLine(
            60,
            Trent,
            ru="Твою ж мать, что происходит?",
            en="What the hell is going on?",
        ),
        VoiceLine(
            70,
            Alaric,
            ru="Трент, не заморачивайся, кто-то из генералитета Рейнланда решил снюхаться с корсарами. И все бы ничего, да это был кто-то из самых высших кругов Рейнланда. ",
            en="Don't worry about it, Trent. Someone in the Rheinland general staff decided to get in bed with the Corsairs. That'd be one thing, but it was someone from the very top.",
        ),
        VoiceLine(
            80,
            Alaric,
            ru="Человек который мог знать то, чего обычный смертный вояка знать не может. Теперь здесь все на ушах стоят, меняют позывные, допуски, ну в общем ты понимаешь, да?",
            en="Someone who knew things an ordinary soldier isn't supposed to know. Now everyone's on edge, changing callsigns, clearances, you know how it is.",
        ),
        VoiceLine(
            90,
            Trent,
            ru="Интересно, с чего бы это ему в голову пришло...",
            en="Wonder what put that idea in his head...",
        ),
        VoiceLine(
            100,
            BrandenburgOutpost,
            ru="Приветствую вас в системе Берлин! В связи с аномальной пиратской активностью в системе вам необходимо пройти проверку и регистрацию.",
            en="Welcome to the Berlin system. Due to unusual pirate activity, you need to be checked and registered.",
        ),
        VoiceLine(
            110,
            Alaric,
            ru="Да мы в курсе, давайте, проводите вашу проверку.",
            en="Yeah, we know. Go ahead and run your check.",
        ),
        VoiceLine(
            120,
            BrandenburgOutpost,
            ru="Спасибо за вашу лояльность! Проверка закончена. Вам выдано постоянное разрешение на посещение системы Берлин на весь период антитеррористической операции. Прошу извинить нас за доставленные неудобства.",
            en="Thank you for your cooperation. The check is finished. You are granted a standing permit to enter the Berlin system for the duration of the anti-terror operation. Sorry for the inconvenience.",
        ),
        VoiceLine(
            130,
            Alaric,
            ru="Охтыж... А это еще что такое???",
            en="Oh... and what the hell is that???",
        ),
        VoiceLine(
            140,
            Dietrich,
            ru="Великие воины Рейнланда, задумайтесь, кого, чью власть вы защищаете? ",
            en="Great warriors of Rheinland, think. Who are you protecting? Whose power?",
        ),
        VoiceLine(
            150,
            Dietrich,
            ru="Прогнившую верхушку нынешнего кайзера? Им недолго осталось стоять у власти. Переходите на сторону истинных патриотов Рейнланда!",
            en="The rotten top around the current Kaiser? They won't be in power for long. Come over to the true patriots of Rheinland!",
        ),
        VoiceLine(
            160,
            BrandenburgCruiser,
            ru="Что-то, я смотрю, истинные патриоты Рейнланда слишком часто используют наёмников - корсаров, а они очень быстро заканчиваются.",
            en="Funny how the true patriots of Rheinland keep using mercenaries. Corsairs. And they run out pretty fast.",
        ),
        VoiceLine(
            170,
            Dietrich,
            ru="Хорошо смеется тот, кто смеется последним! Посмейся теперь над этим!",
            en="He who laughs last, laughs best! Laugh at this!",
        ),
        VoiceLine(
            180,
            Trent,
            ru="Кто мне объяснит, что это было? Сначала корсары, потом появляются легендарные орденские корабли и превращают Рейнландский крейсер в рейнладском пространстве в рейнлайндскую, мать её, пыль!",
            en="Will someone explain what that was? First Corsairs, then legendary Order ships show up and turn a Rheinland cruiser, in Rheinland space, into Rheinland dust!",
        ),
        VoiceLine(
            190,
            Alaric,
            ru="Вот точно не я. Я сам нихрена не понял!",
            en="Don't look at me. I didn't understand a damn thing!",
        ),
        VoiceLine(
            200,
            BrandenburgOutpost,
            ru="Пилоты, я как официальный представитель правительства Рейнланда, выражаю вам благодарность за помощь в уничтожении террористов.",
            en="Pilots, as an official representative of the Rheinland government, I thank you for your help destroying the terrorists.",
        ),
        VoiceLine(
            210,
            BrandenburgOutpost,
            ru="С данного момента на территории Рейнланда вы пользуетесь привилегиями согласно пункту 8 третьего параграфа шестой главы кодекса Рейнланда в отношении пребывающих на его территории иностранных граждан. ",
            en="From this moment, on Rheinland territory, you hold the privileges of article 8, paragraph three, chapter six of the Rheinland Code, regarding foreign nationals present on its territory.",
        ),
        VoiceLine(
            220,
            Alaric,
            ru="Мы у Берлина. Приземляемся, а потом встретимся в баре. Там нас уже заждались.",
            en="We're at Berlin. Let's land, then meet in the bar. They're already waiting for us.",
        ),
        VoiceLine(
            230,
            Alaric,
            ru="Мы только тебя и ждем, Трент. Давай входи в формацию с Аделмаром и полетели.",
            en="We're just waiting on you, Trent. Form up with Adelmar and let's go.",
        ),
        VoiceLine(
            240,
            Alaric,
            ru="Трент, мы не можем ждать. Входи в формацию, сейчас же!",
            en="Trent, we can't wait. Form up, right now!",
        ),
        VoiceLine(
            250,
            Adelmar,
            ru="Луц, ты слышал, сегодня рядом с Бранденбургом творилось черт-знает-что.",
            en="Lutz, did you hear? God knows what went on near Brandenburg today.",
        ),
        VoiceLine(
            260,
            Adelmar,
            ru="Ходят слухи что чуть ли не флотилия корсаров потеряла страх и решила расхреначить станцию и поживиться всем что смогут достать из ее обломков.",
            en="Word is a whole flotilla of Corsairs lost their fear and decided to smash the station and grab whatever they could from the wreckage.",
        ),
        VoiceLine(
            270,
            Luc,
            ru="(акцент на такооого) Ага, ты больше слушай этих придурков-репортеров. Ради сенсации они тебе такого порасскажут. ",
            en="Yeah, listen to those idiot reporters. They'll tell you anything for a sensation.",
        ),
        VoiceLine(
            280,
            Luc,
            ru="В туалете кто-то воздух испортил, а в статье напишут, что взрыв на станции.",
            en="Someone farts in the toilet, and the article says the station exploded.",
        ),
        VoiceLine(
            290,
            Alaric,
            ru="Нет, на самом деле, сегодня на Бранденбург корсары напали вместе с этим вашим мятежным генералом. Мы как раз в эту заваруху попали когда летели к вам, да Трент?",
            en="No, really. Corsairs hit Brandenburg today, together with that rebel general of yours. We flew right into it on the way here, right, Trent?",
        ),
        VoiceLine(
            300,
            Trent,
            ru="Ага. Обнадеживающее начало.",
            en="Yeah. Encouraging start.",
        ),
        VoiceLine(
            310,
            Luc,
            ru="М-да, Дитрих, похоже, окончательно съехал с катушек...",
            en="Yeah. Dietrich's finally lost it...",
        ),
        VoiceLine(
            320,
            Alaric,
            ru="А кто вообще такой этот Дитрих?",
            en="Who is this Dietrich, anyway?",
        ),
        VoiceLine(
            330,
            Luc,
            ru="Очень влиятельный сукин сын.",
            en="A very influential son of a bitch.",
        ),
        VoiceLine(
            340,
            Adelmar,
            ru="Он был вторым человеком после кайзера. Совсем недавно. А затем...",
            en="He was the second man after the Kaiser. Not long ago. And then...",
        ),
        VoiceLine(
            350,
            Adelmar,
            ru="Я не знаю что произошло, но он вдруг ополчился на всех и ушёл в жёсткую оппозицию. А потом... Ну в общем, вы всё и сами видите.",
            en="I don't know what happened, but he suddenly turned on everyone and went into hard opposition. And then... well, you can see for yourselves.",
        ),
        VoiceLine(
            360,
            Luc,
            ru="В общем, слухов ходит мама не горюй. Но я дам тебе совет. Держись подальше от всей этой политики.",
            en="There are more rumors than you can count. But I'll give you some advice. Stay away from all this politics.",
        ),
        VoiceLine(
            370,
            Luc,
            ru="И чем дальше, тем лучше. А то сам попадёшь под чью-либу горячую руку.",
            en="The further, the better. Or you'll end up on the wrong side of someone's temper.",
        ),
        VoiceLine(
            380,
            Alaric,
            ru="Джентльмены, а Трент недавно мне очень своевременный вопрос задал. Что же вы такое везете, если вам внутри Рейнланда охрана из фриленсеров понадобилась?",
            en="Gentlemen, Trent asked me a very timely question. What are you carrying, if you need freelancer escorts inside Rheinland?",
        ),
        VoiceLine(
            390,
            Luc,
            ru="Груз ценный. Желающих его получить много. Деньги мы вам платим. На этом и закончим, хорошо?",
            en="Valuable cargo. A lot of people want it. We're paying you. Let's leave it at that, all right?",
        ),
        VoiceLine(
            400,
            Alaric,
            ru="Клиент всегда прав.",
            en="The client is always right.",
        ),
        VoiceLine(
            410,
            Alaric,
            ru="Все на месте. Собираем формацию. Трент, ты тоже подключайся в звено Аделмара.",
            en="Everyone's here. Form up. Trent, you join Adelmar's wing too.",
        ),
        VoiceLine(
            420,
            Alaric,
            ru="Так, теперь прокладываю маршрут до Штарке...",
            en="All right, plotting a course to Starke...",
        ),
        VoiceLine(
            430,
            Luc,
            ru="Нет. Мы не пролетим до Штарке.",
            en="No. We won't fly to Starke.",
        ),
        VoiceLine(
            440,
            Alaric,
            ru="Эмм, простите...",
            en="Uh, excuse me...",
        ),
        VoiceLine(
            450,
            Luc,
            ru="Если кто-то захочет нас перехватить, он сделает засаду на точке самого очевидного маршрута. Например в районе Штарке.",
            en="If someone wants to intercept us, they'll set an ambush on the most obvious route. Around Starke, for example.",
        ),
        VoiceLine(
            460,
            Trent,
            ru="Что бы он там не хотел сделать, но Штарке - государственная станция, она хорошо охраняется, как и весь маршрут.",
            en="Whatever he wants to do, Starke is a government station. It's well guarded, and so is the whole route.",
        ),
        VoiceLine(
            470,
            Luc,
            ru="Помните, Бранденбург тоже хорошо охранялся.",
            en="Remember, Brandenburg was well guarded too.",
        ),
        VoiceLine(
            480,
            Trent,
            ru="Ваши предложения?",
            en="What do you suggest?",
        ),
        VoiceLine(
            490,
            Luc,
            ru="Идем напрямую, через астероидное поле.",
            en="We go straight through the asteroid field.",
        ),
        VoiceLine(
            500,
            Alaric,
            ru="Даже если вас там никто специально не ждет мы рискуем абсолютно случайно нарваться на пиратов, майнеров, мусорщиков, и чёрт-еще-знает на кого. ",
            en="Even if nobody's waiting for you there, we can still run into pirates, miners, scavengers, and God knows who else.",
        ),
        VoiceLine(
            510,
            Alaric,
            ru="В астероидных поясах это всегда непредсказуемо. Вы серьезно?",
            en="Asteroid belts are always unpredictable. Are you serious?",
        ),
        VoiceLine(
            520,
            Luc,
            ru="Абсолютно.",
            en="Absolutely.",
        ),
        VoiceLine(
            530,
            Adelmar,
            ru="Друзья, мы вам деньги платим за охрану не просто так. По охраняемым магистралям мы и сами смогли бы пролететь.",
            en="Friends, we aren't paying you for an escort for nothing. We could fly the guarded lanes ourselves.",
        ),
        VoiceLine(
            540,
            Trent,
            ru="Ох как это все мне не нравится...",
            en="I really don't like this...",
        ),
        VoiceLine(
            550,
            Alaric,
            ru="Черт, это ловушка! Атакуйте неприятеля! ",
            en="Damn, it's a trap! Attack!",
        ),
        VoiceLine(
            560,
            Trent,
            ru="Мы не вывозим! Луц, Аделмар, астероидный пояс экранирует исходящие вызовы, нужно долететь до ближайшей полицейской станции и вызвать подмогу!",
            en="We can't hold them! Lutz, Adelmar, the asteroid belt is blocking outgoing calls. Someone has to reach the nearest police station and call for help!",
        ),
        VoiceLine(
            570,
            Adelmar,
            ru="Луц, они правы, вызови подмогу!",
            en="Lutz, they're right. Call for help!",
        ),
        VoiceLine(
            580,
            Trent,
            ru="Это было потно.",
            en="That was rough.",
        ),
        VoiceLine(
            590,
            Alaric,
            ru="И не говори, я уже пару раз с жизнью прощался.",
            en="Tell me about it. I said goodbye to my life a couple of times.",
        ),
        VoiceLine(
            600,
            Adelmar,
            ru="Спасибо, друзья, вы были великолепны. ",
            en="Thank you, friends. You were magnificent.",
        ),
        VoiceLine(
            610,
            Alaric,
            ru="Аделмар, давай к полицейскому аванпосту, да? Шутки кончились.",
            en="Adelmar, let's head for the police outpost, yeah? The jokes are over.",
        ),
        VoiceLine(
            620,
            Adelmar,
            ru="Луц, ты бы видел наших охранников в том бою. Я рад что мы остановили свой выбор на них. ",
            en="Lutz, you should have seen our escorts in that fight. I'm glad we chose them.",
        ),
        VoiceLine(
            630,
            Adelmar,
            ru="Трент на своем древнем металлоломе творил такое... Временами мне казалось, что сами валькирии парят рядом с его кораблём.",
            en="Trent, in that ancient scrap heap, did things... At times I thought the Valkyries themselves were flying beside his ship.",
        ),
        VoiceLine(
            640,
            Luc,
            ru="Как я не пытался поднять этот полицейский гадюшник, но их бюрократия абсолютно непробиваема.",
            en="I tried to stir up that police snake pit, but their bureaucracy is impenetrable.",
        ),
        VoiceLine(
            650,
            Luc,
            ru="Иногда мне кажется, что если тебя будут убивать у них на пороге, то они с тебя же справку потребуют, что это не по обоюдному согласию...",
            en="Sometimes I think if someone were killing you on their doorstep, they'd still demand a certificate that it wasn't by mutual consent...",
        ),
        VoiceLine(
            660,
            Trent,
            ru="Джентльмены, что у нас следующим пунктом? Гиперврата в Бисмарк? Давайте туда и выдвинемся, пока не произошло еще что-нибудь, на что наш рейс так богат, будь он неладен.",
            en="Gentlemen, what's next? The jump gate to Bismark? Let's head there before something else happens. This run has had enough of that.",
        ),
        VoiceLine(
            670,
            Alaric,
            ru="Вижу, что все прилетели. Располагайтесь в формации и полетели, нам осталось совсем немного.",
            en="I see everyone's here. Form up and let's go. We don't have far left.",
        ),
        VoiceLine(
            680,
            Alaric,
            ru="Мы добрались до пункта назначения. Давайте поскорее приземлимся, а остальные наши дела решим в баре.",
            en="We've reached the destination. Let's land, and sort out the rest in the bar.",
        ),
    ]


class Mission1(Msn1, script.StoryMission):
    MISSION_INDEX = 1
    CUTSCENES = [
        Msn1Intro,
        Msn1Cityscape,
        Msn1Offer,
        Msn1Berlin,
        Msn1Bizmark,
    ]
    SPACE_CLASS = Msn1Space
    SYNC_SPACE = True
    SYNC_SUBS = True

    MISSION_TITLE = 'Миссия 1. Конвой в Бисмарк'