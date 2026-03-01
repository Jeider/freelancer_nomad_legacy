from story import script
from audio.sound import VoiceLine
from story.actors import (
    Trent, IntroBarman, Stewardess, Alaric, Informer, Dietrich, Adelmar, Luc, BrandenburgOutpost, BrandenburgCruiser
)


class Msn1(object):
    MISSION_INDEX = 1


class Msn1Intro(Msn1, script.CutsceneProps):
    ALIAS = 'intro'
    TITLE = 'Интро'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Trent, ru="Привет, целитель душ!", en="The Savior of my soul!"),
        VoiceLine(20, IntroBarman, ru="Здарова, Трент! Тебе как обычно?", en="Welcome back, Trent. The usual?"),
        VoiceLine(30, Trent, ru="Да, и сразу две!", en="No... you know what, gimme the good stuff."),
        VoiceLine(40, IntroBarman, ru="Есть что отпраздновать?", en="Celebrating something special?"),
        VoiceLine(50, Trent, ru="Есть. Даже два повода! Во-первых, я, наконец, рассчитался со всеми долгами!", en="Yeah. Two somethings. First up, I present the new improved debt-free Trent 2.0!"),
        VoiceLine(60, IntroBarman, ru="За начало новой жизни! Эта - за счет заведения!", en="Ah, life after debt. Lazarus, this one's on me."),
        VoiceLine(70, Trent, ru="Спасибо, дружище! Ты - лучший человек на этой богом забытой планете!",
                  en="Thanks, bud. Everytime I hear you say that I suddenly remember who my favouritest person in the whole wide world is..."),
        VoiceLine(80, IntroBarman,
        ru='Но если было "во-первых", то должно быть и "во-вторых". Давай рассказывай, я сейчас сдохну от любопытства.', en = "Yeah yeah. So if there's a \"first up\", there's gotta be a \"second up\". Spit it out already before I die of curiosity."),
        VoiceLine(90, Trent, ru="Только попробуй! Это будет непоправимой утратой.", en="Don't you die on me. Wouldn't know where to get free drinks."),
        VoiceLine(100, Trent, ru="Старый кореш прислал сообщение.", en="So anyway, an old friend sent me this pad-message."),
        VoiceLine(105, Trent, ru='Смотри', en="Check it out."),
        VoiceLine(110, Alaric, ru="Привет, Трент, это Аларик! У меня для тебя хорошие новости! Мне кажется, мы сможем поправить твое финансовое положение. Встречаемся на Магдебурге, в системе Сигма-13. До встречи!",
                  en=">Greetings, loser! This is Alaric, your old buddy and life coach. Great news - I've found a gig that'll patch that black hole in your wallet. Meet me on Magdeburg, Sigma-13 System ASAP! And I mean now, like yesterday, Trent!"),
        VoiceLine(120, Trent, ru="Что думаешь?", en="Whatcha reckon?"),
        VoiceLine(130, IntroBarman, ru="Думаю, сегодня ты самый счастливый сукин сын на всей этой гребаной планете.", en="I think you're the luckiest son of a bitch this side of the planet."),
        VoiceLine(140, Trent, ru="Да я не про это. Соглашаться? Лететь?", en="Naturally... but I mean... should I just up and go?"),
        VoiceLine(150, IntroBarman, ru="Можно, конечно, вообще ничего не делать, оставить все как есть. Денег на кусок хлеба хватит, да и риска никакого, разве что сдохнуть лет в сорок от работы на шахте. Но, мне кажется, что если судьба дает тебе шанс вырваться из этого болота - грех его не использовать. Хотя, решать тебе.",
                  en="Well let's see. You could stay here and hang with your only real friend in the universe, eke out a miserable living, freeze your ass in that dingy little flat of yours and die an alcoholic washed-up loser decades from now. Or you could grab the life by the horns and fly off to live a real life... but don't let me influence you unduly."),
        VoiceLine(160, Trent, ru="А почему сам не улетишь из \"этого болота\"?", en="If you feel so strongly why haven't you flown the coop?"),
        VoiceLine(170, IntroBarman, ru="Это - моё болото. Я к нему прирос и я его люблю. И друзей, присылающих мен сообщения с просьбой все бросить и прилететь на Магдебург у меня нет. Да и потом, если я улечу, кто здесь будет исцелять души страждущих?",
                  en="Well, see... this may be a shit hole, but it's my shit hole. My bar, my life... guess I've grown attached. And unlike you I don't have friends with get-rich-quick schemes offering to share the spoils. 'Sides if I leave, who'd save everyone's souls after a shitty day?"),
        VoiceLine(180, Trent, ru = "Да уж, без тебя здесь стало бы совсем тоскливо. Ну так я в космопорт?", en = "You're right, without you this place just wouldn't be the same. I guess I'll be heading out to spaceport, then. Take care."),
        VoiceLine(190, IntroBarman, ru = "Удачи, Трент, надеюсь, мы здесь больше не увидимся.", en = "Yeah go on, abandon me here. Good riddance to bad rubbish, don't let the door hit your ass on the way out... and Trent... good luck."),
    ]


class Msn1Cityscape(Msn1, script.CutsceneProps):
    ALIAS = 'cityscape'
    TITLE = 'Взлётная площадка'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Stewardess, ru="Ваши билет и документы, сэр.", en="Ticket and travel documents, please."),
        VoiceLine(20, Stewardess, ru="Трент?.. А вы...", en="Trent?.. You're not The Tr..."),
        VoiceLine(30, Trent, ru="Нет, просто однофамилец.", en="No, no I'm not."),
        VoiceLine(40, Trent, ru="Достало уже. Пока твой тезка спасает вселенную, ты впахиваешь на дядю не покладая рук и выплачиваешь долги.",
                  en="So tired of being reminded that Edison Trent saved the universe, while Addison Trent saved pennies."),
    ]


class Msn1Offer(Msn1, script.CutsceneProps):
    ALIAS = 'offer'
    TITLE = 'Сигма-13'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Alaric, ru="Здарова, дружище, рад видеть тебя!", en="Hey Trent, you slowpoke you sure took your sweet time!"),
        VoiceLine(20, Trent, ru="Привет, Аларик.", en="Good to see you too, Alaric. I came as fast as I could."),
        VoiceLine(30, Alaric, ru="Я слышал ты разобрался со всеми проблемами. Теперь никаких долгов, никаких обязательств, да?",
                  en="Yeah, you walk here or what? Anyway I heard you finally levelled up and beat your debt demon. Congrats. No debts, no strings, no lady... am I right?"),
        VoiceLine(40, Trent, ru="Ага, а еще никаких денег и никакого корабля. Есть в этом и плюсы - никаких проблем с багажом. Все мое - на мне. ",
                  en="Mhm, no ship nor spare cash either. But silver lining, - no headaches over filling other people's cargo holds, and what's mine is truly mine... all of this... lovely nothing."),
        VoiceLine(50, Alaric, ru="Подходящий момент чтобы начать жизнь с чистого листа, не так ли? ", en="A blank slate... great starting point to open a new chapter in your life, no?"),
        VoiceLine(60, Alaric, ru="Мне как раз нужен напарник для хорошо оплачиваемого задания.", en="Witty banter aside, I've found this crazy paying job, but I can't do it alone. I need a good pilot I can trust..."),
        VoiceLine(70, Alaric, ru="Корабль я тебе дам. Старичок, конечно, но пару полетов до регламентного ТО переживет.",
                  en="I'll provide you a ship of course. For my best friend, state of the art, all the bells and whistles.. bristling with weapons. From the last century. Maybe survive liftoff without exploding... or imploding... you never know. Classic Alaric, always a paragon of generosity."),
        VoiceLine(80, Alaric, ru="Нужно проводить пару рейнландских ребят из Берлина в Бисмарк. Платят хорошие деньги",
                  en="All we have to do is escort some flush Rheinlanders from New Berlin to Bismark. Deep pockets, real generous paycheck, Kaching."),
        VoiceLine(90, Trent, ru="Интересно, с чего бы рейнландским ребятам нанимать охрану для перелета из одной своей системы в другую? ",
                  en="Hmm... what's the catch? Why would Rheinlanders fork out for hired guns to escort them within their own territory? Why not go to the authorities..."),
        VoiceLine(100, Trent, ru="А впрочем, корабль, говоришь? Ты не оставил мне шансов, Ал!", en="I'm probably overthinking things. As they say, don't look a gift horse in the ass... And a genuine antique ship! I'm touched. You're really twisting my arm, Al!"),
        VoiceLine(110, Alaric, ru="Вот и договорились. Корабль ждет тебя в ангаре. Осмотри, все ли с ним в порядке. Я буду ждать тебя в космосе.",
                  en="I knew you'd see it my way. Your ship's awaiting you in the hangar. Best check it over, put some duct tape up on the holes if you know what I mean... I'll meet you topside when you're ready to blow... I mean roll."),
    ]


class Msn1Berlin(Msn1, script.CutsceneProps):
    ALIAS = 'berlin'
    TITLE = 'Берлин'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Alaric, ru="Приветствую, джентльмены. Это - Трент, мой друг о котором я вам рассказывал.", en="Guten tag, gentlemen. This is Trent, the friend and ace pilot I told you about previously."),
        VoiceLine(20, Adelmar, ru="Отлично. Рады вас видеть. У нас тут некоторые проблемы в системе, надеюсь, вам это не сильно помешало.", en="Most excellent. We are so glad to see you. We have been having a few, how do you say, problems with puppies... nein, I mean pirates in our system. We hope they did not inconvenience you too much on your journey here."),
        VoiceLine(30, Trent, ru="Нисколько. Я просто счастлив что прилетел сюда ", en="Just a teeny bit. I'm glad we made it here in one piece."),
        VoiceLine(40, Luc, ru="Вот и отлично. Если все в сборе, давайте начнем.", en="Fanstastisch. If alles is gut, then let us depart immediately."),
    ]


class Msn1Bizmark(Msn1, script.CutsceneProps):
    ALIAS = 'bizmark'
    TITLE = 'Бисмарк'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Adelmar, ru="Благодарю вас за сопровождение! Деньги уже перечислены на ваши счета!", en="Vielen Dank for the most excellent escort! We have transferred the money into your account!"),
        VoiceLine(20, Trent, ru="Не стоит благодарности. ", en="You're most welcome. Please feel free to contact us again if you need to."),
        VoiceLine(30, Luc, ru="Кроме того, мы, как члены Ганзейского торгового сообщества, добавили вас в белый лист фрилансеров. ", en="As a.. how do you say... bogus? Deal sweetener? We have added you to our Hanseatic trading community freelancers' whitelist."),
        VoiceLine(40, Luc, ru="Теперь вы можете брать к выполнению миссии Ганзейских купцов.", en="From now on, you may take on missions offered by Hanseatic merchants, mein friend."),
        VoiceLine(50, Alaric, ru="А вот за это отдельное спасибо, джентльмены! Трент, ты слышал? Мы теперь на Рейнландской территории не просто голодранцы какие-то, а аккредитованные Ганзейским торговым сообществом официальные фрилансеры!", en="Ah, thank you so much for your kind generosity, gentlemen! Trent, you heart that? We have been elevated from bottom feeding gutter trash to honest to God accredited freelancers of the Hanseatic trading community!"),
        VoiceLine(60, Trent, ru="Охренеть. ", en="I'm overwhelmed..."),
        VoiceLine(70, Luc, ru="И... Трент, бесплатный совет, как можно быстрее поменяй то на чём ты летаешь на что-нибудь более современное. Без обид, но подобные раритеты покупают из эстетических соображений, а не чтобы на них летать.", en="And Herr Trent, a friendly word of advice: that ship of yours... it is more holey than the church and leakier than a faucet. If it wasn't so ugly you might be able to sell it to a museum. Perhaps best to change to something less likely to kill you."),
        VoiceLine(80, Trent, ru="Я подумаю над этим.", en="Yeah... I'll think about it."),
        VoiceLine(90, Alaric, ru="И как тебе новая жизнь Трент?", en="So, Trent, how're you adjusting to the heady life of a debt free freelancer?"),
        VoiceLine(100, Trent, ru="Волнительно. Но... сейчас у меня есть свой корабль, а за это я хоть дьяволу в глотку готов залезть.", en="It's exciting I'll give you that. Now that I have my very own ship, I'm ready to fly down the maw of the devil himself."),
        VoiceLine(110, Alaric, ru="Теперь у тебя еще и деньги есть на его обслуживание и переоборудование. А если подумать - то и на покупку нового. По большому счету, Луц в чем-то прав.", en="Ah, perhaps patch it up with some newer parts before that. I'm sure they still sell them in novelty stores... Or maybe just buy a new ship. Luts had a point. I'm sorry, I just couldn't afford get better than that pile of junk at short notice."),
        VoiceLine(120, Trent, ru="Да пошел он. Может у него и хватает денег чтобы корабли раз в год менять, а я пока еще миллионером не стал. ", en="Yeah, well it's my pile of junk now. He can stick it where the sun don't shine. Not everyone is born a millionaire with a silver spoon stuck up his butt like him. Must be nice to have money to change ships as often as he changes women. Or men."),
        VoiceLine(125, Alaric, ru="Тогда стоит задуматься над апгрейдом того что есть. ", en="Well, cheapskate, then at least upgrade the guns. Those peashooters are just pathetic."),
        VoiceLine(130, Alaric, ru="В том бою, в астероидах, тебе иногда явно не хватало энергии. Тебе точно не помешает поменять генератор на более мощный. Да и остальную начинку посмотри. Этот корпус очень эластичен в плане апгрейда. Практически все модули можно поменять на более совершенные...", en="During the battle in that asteroid field, your generator looked like it was going to melt down trying to keep up with the guns. It certainly wouldn't hurt you to shell out for a better power generator. And take a close look at the rest of the package. The chassis, while classic, is very flexible and accomodates a lot of upgrades. Most of its modules can be replaced with... more modern ones..."),
        VoiceLine(140, Alaric, ru="О-кей, Трент, у меня тут есть дела, требующие немедленного разрешения, поэтому я побежал. Освоишься без меня тут?", en="OK Trent, I better get going. Got to attend to business and scout out our next job. Will you be okay here without me?"),
        VoiceLine(150, Trent, ru="Попробую... Удачи, Аларик!!!", en=" Yes mummy. I'll try to look after myself. Get going, asshole."),
        VoiceLine(160, Alaric, ru="Пока!", en="Tch, such language. See you soon!"),
    ]


class Msn1Space(Msn1, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(
            10,
            Alaric,
            ru="Эй, Трент! Поди забыл уже, с какой стороны подходить к креслу пилота?",
            en="Hey, Trent. Have you forgotten how to fly a spaceship already? Get a move on, grandpa.",
        ),
        VoiceLine(
            20,
            Alaric,
            ru="Нам нужно добраться до гиперврат в Берлин. Я загрузил координаты торгового маршрута в твою нейросеть. Полетели!",
            en="We need to take the New Berlin jump gate. I've uploaded the trade-lane's coordinates to your neural net. Let's go.",
        ),
        VoiceLine(
            30,
            Alaric,
            ru="Торговый маршрут активирован. Набираем максимальную скорость.",
            en="Trade-lane sequence activated. Full speed ahead.",
        ),
        VoiceLine(
            40,
            Alaric,
            ru="Дело осталось за малым, активировать гиперврата в Берлин. Давай, Трент, ты первый.",
            en="Just one more step - activate the jump gate to New Berlin. Come on Trent, you go first.",
        ),
        VoiceLine(
            50,
            Informer,
            ru="Приветствуем Вас в системе Берлин! В связи с аномальной пиратской активностью в системе все прибывающие должны пройти проверку и регистрацию на аванпосте Бранденбург.",
            en="Welcome to the New Berlin system. Due to escalated pirate activities in the system, all incoming ships must submit to scanning and registration at Brandenburg outpost.",
        ),
        VoiceLine(
            60,
            Trent,
            ru="Твою ж мать, что происходит?",
            en="What the hell? Why all the security? What's going on?",
        ),
        VoiceLine(
            70,
            Alaric,
            ru="Трент, не заморачивайся, кто-то из генералитета Рейнланда решил снюхаться с корсарами. И все бы ничего, да это был кто-то из самых высших кругов Рейнланда. ",
            en="Relax Trent, it's not for us. Rumour is some government bigwig in Rheinlands' decided to go on a witch-hunt for Corsairs. Someone really high up from the looks of it. We're talking Inntermost circles.",
        ),
        VoiceLine(
            80,
            Alaric,
            ru="Человек который мог знать то, чего обычный смертный вояка знать не может. Теперь здесь все на ушах стоят, меняют позывные, допуски, ну в общем ты понимаешь, да?",
            en="The way he's got everyone on their tiptoes using call-signs, requiring access codes…  They must be protecting someone or something pretty important. Something big.",
        ),
        VoiceLine(
            90,
            Trent,
            ru="Интересно, с чего бы это ему в голову пришло...",
            en="Curiouser and curiouser.",
        ),
        VoiceLine(
            100,
            BrandenburgOutpost,
            ru="Приветствую вас в системе Берлин! В связи с аномальной пиратской активностью в системе вам необходимо пройти проверку и регистрацию.",
            en="Welcome to the New Berlin system. Due to escalating pirate activities you will submit to scanning and registration now.",
        ),
        VoiceLine(
            110,
            Alaric,
            ru="Да мы в курсе, давайте, проводите вашу проверку.",
            en="Thanks, we are aware. Let's get this over with.",
        ),
        VoiceLine(
            120,
            BrandenburgOutpost,
            ru="Спасибо за вашу лояльность! Проверка закончена. Вам выдано постоянное разрешение на посещение системы Берлин на весь период антитеррористической операции. Прошу извинить нас за доставленные неудобства.",
            en="Thank you for your patience. We're all done. You are granted a permanent permit to stay in New Berlin for the duration of our anti-terrorist operations. We apologize for any inconvenience incurred.",
        ),
        VoiceLine(
            130,
            Alaric,
            ru="Охтыж... А это еще что такое???",
            en="Oh, man… How long's that gonna be???",
        ),
        VoiceLine(
            140,
            Dietrich,
            ru="Великие воины Рейнланда, задумайтесь, кого, чью власть вы защищаете? ",
            en="Warriors of Rheinland, I greet you. Take stock and consider your misguided loyalties. Just who are you fighting for?",
        ),
        VoiceLine(
            150,
            Dietrich,
            ru="Прогнившую верхушку нынешнего кайзера? Им недолго осталось стоять у власти. Переходите на сторону истинных патриотов Рейнланда!",
            en="The corrupt, vile politicians of our beloved Konig? Who indiscriminately levy tariffs, terrorize the people and enrich their own pockets? Who watch our children starve and deport citizens?? We the people are Rheinland! Rise up and join us, true patriots!..",
        ),
        VoiceLine(
            160,
            BrandenburgCruiser,
            ru="Что-то, я смотрю, истинные патриоты Рейнланда слишком часто используют наёмников - корсаров, а они очень быстро заканчиваются.",
            en="Funny how starving patriots of Rheinland resort to paying mercenary scum to do their dirty work - Corsairs? You'd do better with Xenos!",
        ),
        VoiceLine(
            170,
            Dietrich,
            ru="Хорошо смеется тот, кто смеется последним! Посмейся теперь над этим!",
            en="You are a man of humour, huh? Let's see who gets the last laugh! Rebels, attack!",
        ),
        VoiceLine(
            180,
            Trent,
            ru="Кто мне объяснит, что это было? Сначала корсары, потом появляются легендарные орденские корабли и превращают Рейнландский крейсер в рейнладском пространстве в рейнлайндскую, мать её, пыль!",
            en="Could someone please explain to me what the hell is going on? First Corsairs show up, then the Order. The Order! From the history books and fairy tales. And they ripped apart that Rheinland cruiser like it was a child's toy.",
        ),
        VoiceLine(
            190,
            Alaric,
            ru="Вот точно не я. Я сам нихрена не понял!",
            en="Search me. I'm as lost at sea as you are…",
        ),
        VoiceLine(
            200,
            BrandenburgOutpost,
            ru="Пилоты, я как официальный представитель правительства Рейнланда, выражаю вам благодарность за помощь в уничтожении террористов.",
            en="Pilots and representatives of the Rheinland government, this is Brandenburg. Our deepest gratitude for your assistance defeating the terrorist scum. ",
        ),
        VoiceLine(
            210,
            BrandenburgOutpost,
            ru="С данного момента на территории Рейнланда вы пользуетесь привилегиями согласно пункту 8 третьего параграфа шестой главы кодекса Рейнланда в отношении пребывающих на его территории иностранных граждан. ",
            en="From this point on you are granted free passage throughout the territories of Rhineland, in accordance with clause 8, paragraph three of chapter six of the Rhineland Constitution relating to foreign nationals resident within our territory. ",
        ),
        VoiceLine(
            220,
            Alaric,
            ru="Мы у Берлина. Приземляемся, а потом встретимся в баре. Там нас уже заждались.",
            en="New Berlin at last. Let's land now. I'm sure you could do with a quick shower, then let's meet our Rhineland friends in the bar. They've waited long enough.",
        ),
        VoiceLine(
            230,
            Alaric,
            ru="Мы только тебя и ждем, Трент. Давай входи в формацию с Аделмаром и полетели.",
            en="We've been waiting for you, slowpoke. Form up with Adelmar and let's go.",
        ),
        VoiceLine(
            240,
            Alaric,
            ru="Трент, мы не можем ждать. Входи в формацию, сейчас же!",
            en="Trent, we really can't wait any longer. Get your ass in formation right now!",
        ),
        VoiceLine(
            250,
            Adelmar,
            ru="Луц, ты слышал, сегодня рядом с Бранденбургом творилось черт-знает-что.",
            en="Lutz, I'm sure you've heard of the god-knows-what-happened kerfuffle at Brandenburg today.",
        ),
        VoiceLine(
            260,
            Adelmar,
            ru="Ходят слухи что чуть ли не флотилия корсаров потеряла страх и решила расхреначить станцию и поживиться всем что смогут достать из ее обломков.",
            en="Word is that a wing of Corsairs decided to attack the station. They were going to sell the salvage and personnel for profit.",
        ),
        VoiceLine(
            270,
            Luc,
            ru="Ага, ты больше слушай этих придурков-репортеров, они тебе ради сенсации такооого порасскажут. ",
            en="Ah, don't go listening to those idiotic reporters. They'd say anything for better ratings.",
        ),
        VoiceLine(
            280,
            Luc,
            ru="Кто-то в туалете воздух испортил - они раструбят что взрыв на станции.",
            en="Someone just farted in the toilet - then made it out as an explosion in the station.",
        ),
        VoiceLine(
            290,
            Alaric,
            ru="Нет, на самом деле, сегодня на Бранденбург корсары напали вместе с этим вашим мятежным генералом. Мы как раз в эту заваруху попали когда летели к вам, да Трент?",
            en="No, seriously, Corsairs attacked Brandenburg today along with that self-styled general of the resistance. We were caught in the net on our way here, right Trent?",
        ),
        VoiceLine(
            300,
            Trent,
            ru="Ага. Обнадеживающее начало.",
            en="Yep. Quite the show stopper actually.",
        ),
        VoiceLine(
            310,
            Luc,
            ru="М-да, Дитрих, похоже, окончательно съехал с катушек...",
            en="Hm, yeah, Ditrich. Seems like he's finally lost it...",
        ),
        VoiceLine(
            320,
            Alaric,
            ru="А кто вообще такой этот Дитрих?",
            en="Remind me, who is this Ditrich, actually?",
        ),
        VoiceLine(
            330,
            Luc,
            ru="Очень влиятельный сукин сын.",
            en="One influential son of a bitch.",
        ),
        VoiceLine(
            340,
            Adelmar,
            ru="Он был вторым человеком после кайзера. Совсем недавно. А затем. ",
            en="He used to be the Kaizer's second in command, not too long ago. Loyal as they came, lapdog type.",
        ),
        VoiceLine(
            350,
            Adelmar,
            ru="Я не знаю что произошло, но он вдруг ополчился на всех и ушёл в жёсткую оппозицию. А потом... Ну в общем, вы все видите.",
            en="But all of a sudden for reasons unknown he went rogue and joined the rebel extremist nuts. And then… Well… You've saw for yourself.",
        ),
        VoiceLine(
            360,
            Luc,
            ru="В общем, слухов ходит дохрена и больше, а я могу только порекомендовать держаться от этой всей политики подальше. ",
            en="Really, there are way too many rumors. My advice to you is keep your head down and steer clear of politics.",
        ),
        VoiceLine(
            370,
            Luc,
            ru="И чем дальше - тем лучше, выше вероятность голову на плечах сохранить во всем этом винегрете.",
            en="The further you are from it, the better your chances of keeping your head attached to your shoulders.",
        ),
        VoiceLine(
            380,
            Alaric,
            ru="Джентльмены, а Трент недавно мне очень своевременный вопрос задал. Что же вы такое везете, если вам внутри Рейнланда охрана из фриленсеров понадобилась?",
            en="Gentlemen, Trent here asks a very astute question. Why would you need to hire freelancer escorts inside your own territory?",
        ),
        VoiceLine(
            390,
            Luc,
            ru="Груз ценный. Желающих его получить много. Деньги мы вам платим. На этом и закончим, хорошо?",
            en="Precious cargo. Many would kill to get their hands on it. We cannot trust anyone. We pay you good money, you do the job. No more questions, OK?",
        ),
        VoiceLine(
            400,
            Alaric,
            ru="Клиент всегда прав.",
            en="Noted. As Trent's mother always used to say, the client is always right.",
        ),
        VoiceLine(
            410,
            Alaric,
            ru="Все на месте. Собираем формацию. Трент, ты тоже подключайся в звено Аделмара.",
            en="Formation complete, everything's in order. Trent, join us on Adelmar's comm channel.",
        ),
        VoiceLine(
            420,
            Alaric,
            ru="Так, теперь прокладываю маршрут до Штарке...",
            en="Setting course for Starke now...",
        ),
        VoiceLine(
            430,
            Luc,
            ru="Нет. Мы не пролетим до Штарке.",
            en="No. We aren't going to Starke.",
        ),
        VoiceLine(
            440,
            Alaric,
            ru="Эмм, простите...",
            en="What? But the plan...",
        ),
        VoiceLine(
            450,
            Luc,
            ru="Если кто-то захочет нас перехватить, он сделает засаду на точке самого очевидного маршрута. например в районе Штарке.",
            en="Change of plans. If someone is going to hijack our cargo, they'll hit us on the most commonly used route. Starke's on that route.",
        ),
        VoiceLine(
            460,
            Trent,
            ru="Что бы он там не хотел сделать, но Штарке - государственная станция, она хорошо охраняется, как и весь маршрут.",
            en="But Starke is a government station. It's guarded like a fortress by military patrols, like all the other stops on that route",
        ),
        VoiceLine(
            470,
            Luc,
            ru="Помните, Бранденбург тоже хорошо охранялся.",
            en="Brandenburg was a well-guarded station too, look what happened there.",
        ),
        VoiceLine(
            480,
            Trent,
            ru="Ваши предложения?",
            en="Okay, so what's the plan?",
        ),
        VoiceLine(
            490,
            Luc,
            ru="Идем напрямую, через астероидное поле.",
            en="We're going fly directly through the asteroid field.",
        ),
        VoiceLine(
            500,
            Alaric,
            ru="Даже если вас там никто специально не ждет мы рискуем абсолютно случайно нарваться на пиратов, майнеров, мусорщиков, и чёрт-еще-знает на кого. ",
            en="Huh? Even without an ambush by imaginary assailants that runs the risk of running into pirates, miners, scavengers, space monkeys and hell knows what else.",
        ),
        VoiceLine(
            510,
            Alaric,
            ru="В астероидных поясах это всегда непредсказуемо. Вы серьезно?",
            en="Asteroid fields are always hairy to fly through. Are you serious?",
        ),
        VoiceLine(
            520,
            Luc,
            ru="Абсолютно.",
            en="Dead serious.",
        ),
        VoiceLine(
            530,
            Adelmar,
            ru="Друзья, мы вам деньги платим за охрану не просто так. По охраняемым магистралям мы и сами смогли бы пролететь.",
            en="Friends, we're not paying you money to babysit us on a milk run. We do this our way.",
        ),
        VoiceLine(
            540,
            Trent,
            ru="Ох как это все мне не нравится...",
            en="Oh boy, I'm getting a bad feeling about this...",
        ),
        VoiceLine(
            550,
            Alaric,
            ru="Черт, это ловушка! Атакуйте неприятеля! ",
            en="Ambush! Pirates! Trent, Lutz, engage!",
        ),
        VoiceLine(
            560,
            Trent,
            ru="Мы не вывозим! Луц, Аделмар, астероидный пояс экранирует исходящие вызовы, нужно долететь до ближайшей полицейской станции и вызвать подмогу!",
            en="We're not gonna make it! Lutz, Adelmar, the asteroids are jamming our transmissions. You'll have to fly to the nearest police base and bring help!",
        ),
        VoiceLine(
            570,
            Adelmar,
            ru="Луц, они правы, вызови подмогу!",
            en="Lutz, they're right, go call for help!",
        ),
        VoiceLine(
            580,
            Trent,
            ru="Это было потно.",
            en="That was painful.",
        ),
        VoiceLine(
            590,
            Alaric,
            ru="И не говори, я уже пару раз с жизнью прощался.",
            en="Did you say something? I was just watching my life flash before my eyes.",
        ),
        VoiceLine(
            600,
            Adelmar,
            ru="Спасибо, друзья, вы были великолепны. ",
            en="Thank you, friends. You did a great job.",
        ),
        VoiceLine(
            610,
            Alaric,
            ru="Аделмар, давай к полицейскому аванпосту, да? Шутки кончились.",
            en="Adelmar, we're going to a police base, right? No more messing around.",
        ),
        VoiceLine(
            620,
            Adelmar,
            ru="Луц, ты бы видел наших охранников в том бою. Я рад что мы остановили свой выбор на них. ",
            en="Lutz, did you see how our escorts did in that fight. I'm so glad that we picked them for the job. ",
        ),
        VoiceLine(
            630,
            Adelmar,
            ru="Трент на своем древнем металлоломе творил такое... Временами мне казалось, что сами валькирии парят рядом с его кораблём.",
            en="Yeah, that Trent with his ancient piece of crap, was transcendent... At times it almost seemed like the Valkyries were flying alongside him clawing the other ships apart.",
        ),
        VoiceLine(
            640,
            Luc,
            ru="Я уже хотел весь этот полицейский гадюшник на уши поднять, но эта их непробиваемая бюрократия... ",
            en="I tried to call in the police, but for their ridiculous bureaucracy and a thousand questions... ",
        ),
        VoiceLine(
            650,
            Luc,
            ru="Иногда мне кажется, что если тебя будут убивать у них на пороге, они с тебя же справку потребуют что это не по обоюдному согласию...",
            en="Yes, sometimes it feels like if someone were to murder you on their doorstep, they'd demand proof that it wasn't done by mutual consent before taking action…",
        ),
        VoiceLine(
            660,
            Trent,
            ru="Джентльмены, что у нас следующим пунктом? Гиперврата в Бисмарк? Давайте туда и выдвинемся, пока не произошло еще что-нибудь, на что наш рейс так богат, будь он неладен.",
            en="Gentlemen, if you're done flirting, where to next? The jump gate to Bismark? Let's get going, before anything else life endangering develops.",
        ),
        VoiceLine(
            670,
            Alaric,
            ru="Вижу, что все прилетели. Располагайтесь в формации и полетели, нам осталось совсем немного.",
            en="I see you've arrived at last. Re-enter formation and let's fly, we still have some way to go.",
        ),
        VoiceLine(
            680,
            Alaric,
            ru="Мы добрались до пункта назначения. Давайте поскорее приземлимся, а остальные наши дела решим в баре.",
            en="We've reached our destination. Let's land quickly. Talk over drinks in the bar.",
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

    MISSION_TITLE = 'Миссия 1. Конвой в Бисмарк'