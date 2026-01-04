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
        VoiceLine(10, Trent, ru="Привет, целитель душ!", en="The savior of souls!"),
        VoiceLine(20, IntroBarman, ru="Здарова, Трент! Тебе как обычно?", en="Welcome back, Trent. The usual?"),
        VoiceLine(30, Trent, ru="Да, и сразу две!", en="Sure, I'll have two!"),
        VoiceLine(40, IntroBarman, ru="Есть что отпраздновать?", en="Any reason for this celebration?"),
        VoiceLine(50, Trent, ru="Есть. Даже два повода! Во-первых, я, наконец, рассчитался со всеми долгами!", en="Absolutely. Two reasons actually! First of all, I have finally managed to pay off all my debts!"),
        VoiceLine(60, IntroBarman, ru="За начало новой жизни! Эта - за счет заведения!", en="For the beginning of a new life! This one's on me!"),
        VoiceLine(70, Trent, ru="Спасибо, дружище! Ты - лучший человек на этой богом забытой планете!",
                  en="Thanks, friend! You are definitely the best person in this godforsaken place!"),
        VoiceLine(80, IntroBarman,
        ru='Но если было "во-первых", то должно быть и "во-вторых". Давай рассказывай, я сейчас сдохну от любопытства.', en = "But if there's a \"first of all\", there should be \"second\". Go on and tell me, or else I'll die of curiousity."),
        VoiceLine(90, Trent, ru="Только попробуй! Это будет непоправимой утратой.", en="Don't you dare die on me! I'd never get over the loss."),
        VoiceLine(100, Trent, ru="Старый кореш прислал сообщение.", en="An old friend sent me a message."),
        VoiceLine(105, Trent, ru='Смотри', en="Look."),
        VoiceLine(110, Alaric, ru="Привет, Трент, это Аларик! У меня для тебя хорошие новости! Мне кажется, мы сможем поправить твое финансовое положение. Встречаемся на Магдебурге, в системе Сигма-13. До встречи!",
                  en="Greetings, Trent! This is Alaric! Good news. I think we can fix the hole in your finnances. Meet me at Magdeburg, Sigma-13 System. See you soon!"),
        VoiceLine(120, Trent, ru="Что думаешь?", en="What do you think?"),
        VoiceLine(130, IntroBarman, ru="Думаю, сегодня ты самый счастливый сукин сын на всей этой гребаной планете.", en="I think you're the luckiest son of a bitch on this junkpile of a planet."),
        VoiceLine(140, Trent, ru="Да я не про это. Соглашаться? Лететь?", en="No, I mean... Should I agree and go there?"),
        VoiceLine(150, IntroBarman, ru="Можно, конечно, вообще ничего не делать, оставить все как есть. Денег на кусок хлеба хватит, да и риска никакого, разве что сдохнуть лет в сорок от работы на шахте. Но, мне кажется, что если судьба дает тебе шанс вырваться из этого болота - грех его не использовать. Хотя, решать тебе.",
                  en="You could, of course, let things be as they are and do nothing. Got enough money to sustain yourself; a risk-free life, other than dying in your 40s working in the mine. But, I think, if life gives you a chance to get out of this mud-hole - it's a sin not to take that chance. But, it's your call."),
        VoiceLine(160, Trent, ru="А почему сам не улетишь из \"этого болота\"?", en="So why aren't you flying away from this \"mud-hole\" yourself?"),
        VoiceLine(170, IntroBarman, ru="Это - моё болото. Я к нему прирос и я его люблю. И друзей, присылающих мен сообщения с просьбой все бросить и прилететь на Магдебург у меня нет. Да и потом, если я улечу, кто здесь будет исцелять души страждущих?",
                  en="This, friend, is my mud-hole. I've grown into it and I love it. And I don't have friends like yours, asking me to drop everything I'm doing and come over to Magdeburg. And if I would leave, who's going to be the savior of strangers' souls?"),
        VoiceLine(180, Trent, ru = "Да уж, без тебя здесь стало бы совсем тоскливо. Ну так я в космопорт?", en = "You're right, without you this place would've been gloomy. I guess I'll head to the spaceport, then."),
        VoiceLine(190, IntroBarman, ru = "Удачи, Трент, надеюсь, мы здесь больше не увидимся.", en = "Good luck, Trent! Hopefully, we'll never meet here again."),
    ]


class Msn1Cityscape(Msn1, script.CutsceneProps):
    ALIAS = 'cityscape'
    TITLE = 'Взлётная площадка'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Stewardess, ru="Ваши билет и документы, сэр.", en="Your ticket and documents, sir."),
        VoiceLine(20, Stewardess, ru="Трент?.. А вы...", en="Trent?.. Are you..."),
        VoiceLine(30, Trent, ru="Нет, просто однофамилец.", en="No, just a coincidence."),
        VoiceLine(40, Trent, ru="Достало уже. Пока твой тезка спасает вселенную, ты впахиваешь на дядю не покладая рук и выплачиваешь долги.",
                  en="I'm so sick of it. While my namesake was saving the universe, I was working my ass off to pay off those stupid debts..."),
    ]


class Msn1Offer(Msn1, script.CutsceneProps):
    ALIAS = 'offer'
    TITLE = 'Сигма-13'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Alaric, ru="Здарова, дружище, рад видеть тебя!", en="Hi Trent, glad to see you!"),
        VoiceLine(20, Trent, ru="Привет, Аларик.", en="You too, Alaric."),
        VoiceLine(30, Alaric, ru="Я слышал ты разобрался со всеми проблемами. Теперь никаких долгов, никаких обязательств, да?",
                  en="I heard that you've finally dealt with that problem. No more debts, no more duties, right?"),
        VoiceLine(40, Trent, ru="Ага, а еще никаких денег и никакого корабля. Есть в этом и плюсы - никаких проблем с багажом. Все мое - на мне. ",
                  en="Mhm, no ship and no money either. But it has its benefits - no problems with cargo holds. What's mine is mine."),
        VoiceLine(50, Alaric, ru="Подходящий момент чтобы начать жизнь с чистого листа, не так ли? ", en="A great time to start a new page in your life, isn't it?"),
        VoiceLine(60, Alaric, ru="Мне как раз нужен напарник для хорошо оплачиваемого задания.", en="I could use a partner for a well-paid job."),
        VoiceLine(70, Alaric, ru="Корабль я тебе дам. Старичок, конечно, но пару полетов до регламентного ТО переживет.",
                  en="I'll give you a ship. An old one, of course, but it will definitely survive a few flights till decommission."),
        VoiceLine(80, Alaric, ru="Нужно проводить пару рейнландских ребят из Берлина в Бисмарк. Платят хорошие деньги",
                  en="Gotta escort a few Rheinlanders from New Berlin to Bismark. They pay good, real good."),
        VoiceLine(90, Trent, ru="Интересно, с чего бы рейнландским ребятам нанимать охрану для перелета из одной своей системы в другую? ",
                  en="Interesting, why would Rheinlanders hire escorts to fly from one system to another, inside their own territory?"),
        VoiceLine(100, Trent, ru="А впрочем, корабль, говоришь? Ты не оставил мне шансов, Ал!", en="And a spaceship, you say? You're leaving me no choice, Al!"),
        VoiceLine(110, Alaric, ru="Вот и договорились. Корабль ждет тебя в ангаре. Осмотри, все ли с ним в порядке. Я буду ждать тебя в космосе.",
                  en="Excellent! The ship's waiting for you in the hangar. Check everything over, and I'll meet you outside when you're ready."),
    ]


class Msn1Berlin(Msn1, script.CutsceneProps):
    ALIAS = 'berlin'
    TITLE = 'Берлин'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Alaric, ru="Приветствую, джентльмены. Это - Трент, мой друг о котором я вам рассказывал.", en="Guten tag, gentlemen. This is Trent, my friend I was telling you about."),
        VoiceLine(20, Adelmar, ru="Отлично. Рады вас видеть. У нас тут некоторые проблемы в системе, надеюсь, вам это не сильно помешало.", en="Excellent. We're glad to see you. We have a few problems in our system. Hopefully, they didn't bother you too much."),
        VoiceLine(30, Trent, ru="Нисколько. Я просто счастлив что прилетел сюда ", en="A little bit. I'm just glad we made it here."),
        VoiceLine(40, Luc, ru="Вот и отлично. Если все в сборе, давайте начнем.", en="Great. If you're doing fine, then let's begin."),
    ]


class Msn1Bizmark(Msn1, script.CutsceneProps):
    ALIAS = 'bizmark'
    TITLE = 'Бисмарк'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Adelmar, ru="Благодарю вас за сопровождение! Деньги уже перечислены на ваши счета!", en="Thank you for the escort! The money's already being transferred to your accounts!"),
        VoiceLine(20, Trent, ru="Не стоит благодарности. ", en="You're welcome."),
        VoiceLine(30, Luc, ru="Кроме того, мы, как члены Ганзейского торгового сообщества, добавили вас в белый лист фрилансеров. ", en="Additionally, we, as members of the Hanseatic trading community, have added you to our freelancers' whitelist."),
        VoiceLine(40, Luc, ru="Теперь вы можете брать к выполнению миссии Ганзейских купцов.", en="From now on, you can take any missions offered by the Hanseatic merchants."),
        VoiceLine(50, Alaric, ru="А вот за это отдельное спасибо, джентльмены! Трент, ты слышал? Мы теперь на Рейнландской территории не просто голодранцы какие-то, а аккредитованные Ганзейским торговым сообществом официальные фрилансеры!", en="And here's for a special thanks to you, gentlemen! Trent, have you heard? We are no longer some kind of beggers in Rheinland territory, but official freelancers accredited by the Hanseatic trading community!"),
        VoiceLine(60, Trent, ru="Охренеть. ", en="Will I live..."),
        VoiceLine(70, Luc, ru="И... Трент, бесплатный совет, как можно быстрее поменяй то на чём ты летаешь на что-нибудь более современное. Без обид, но подобные раритеты покупают из эстетических соображений, а не чтобы на них летать.", en="And... Trent, a quick word of advice: As soon as you can, get yourself a newer ship to fly around in. No offense, but such antiquities are bought for novelty reasons. Not to actually fly in space."),
        VoiceLine(80, Trent, ru="Я подумаю над этим.", en="I'll think about it."),
        VoiceLine(90, Alaric, ru="И как тебе новая жизнь Трент?", en="So, how's your new life going, Trent?"),
        VoiceLine(100, Trent, ru="Волнительно. Но... сейчас у меня есть свой корабль, а за это я хоть дьяволу в глотку готов залезть.", en="Exciting. But... Now that I have my own ship, I'm ready to go down the devil's throat."),
        VoiceLine(110, Alaric, ru="Теперь у тебя еще и деньги есть на его обслуживание и переоборудование. А если подумать - то и на покупку нового. По большому счету, Луц в чем-то прав.", en="Now that you have the money to maintain and refurbish it. And to think it through - you should buy a new one. As painful as it may sound, Luts made a great point."),
        VoiceLine(120, Trent, ru="Да пошел он. Может у него и хватает денег чтобы корабли раз в год менять, а я пока еще миллионером не стал. ", en="He can suck it. Maybe he has enough money to change ships every goddamn year, but I'm not a millionaire yet."),
        VoiceLine(125, Alaric, ru="Тогда стоит задуматься над апгрейдом того что есть. ", en="Then just think about upgrading what you already have."),
        VoiceLine(130, Alaric, ru="В том бою, в астероидах, тебе иногда явно не хватало энергии. Тебе точно не помешает поменять генератор на более мощный. Да и остальную начинку посмотри. Этот корпус очень эластичен в плане апгрейда. Практически все модули можно поменять на более совершенные...", en="On that battle, in the asteroid field, you most certainly didn't have enough energy. It certainly won't hurt you to get a better power generator. And take a look at the rest of the package. This chassis is very flexible in terms of upgrades. Most of its modules can be replaced with better ones..."),
        VoiceLine(140, Alaric, ru="О-кей, Трент, у меня тут есть дела, требующие немедленного разрешения, поэтому я побежал. Освоишься без меня тут?", en="OK Trent, I got some business to take care of. It requires my immediate attention so I better get going. Will you manage here without me?"),
        VoiceLine(150, Trent, ru="Попробую... Удачи, Аларик!!!", en=" I'll try... Good luck, Alaric!!!"),
        VoiceLine(160, Alaric, ru="Пока!", en="Bye-bye!"),
    ]


class Msn1Space(Msn1, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(
            10,
            Alaric,
            ru="Эй, Трент! Поди забыл уже, с какой стороны подходить к креслу пилота?",
            en="Hey, Trent. Did you already forget how to pilot a spaceship?",
        ),
        VoiceLine(
            20,
            Alaric,
            ru="Нам нужно добраться до гиперврат в Берлин. Я загрузил координаты торгового маршрута в твою нейросеть. Полетели!",
            en="We need to reach the New Berlin jump gate. I've uploaded the trade-lane's coordinates to your neural net. Let's go.",
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
            en="Welcome to the New Berlin system! Due to anomalous pirate activities in the system, all incoming ships have to be scanned and registered on Brandenburg outpost.",
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
            en="Trent, don't bother, someone in the Rheinland government decided to sniff around for Corsairs. But not just anyone, it was someone in the HIGHEST CIRCLES of Rheinland.",
        ),
        VoiceLine(
            80,
            Alaric,
            ru="Человек который мог знать то, чего обычный смертный вояка знать не может. Теперь здесь все на ушах стоят, меняют позывные, допуски, ну в общем ты понимаешь, да?",
            en="A man who could know what any mortal can never. Now everyone's up on their toes, exchanging call-signs, access codes… You understand, right?",
        ),
        VoiceLine(
            90,
            Trent,
            ru="Интересно, с чего бы это ему в голову пришло...",
            en="I wonder, how the hell did he come up with that...",
        ),
        VoiceLine(
            100,
            BrandenburgOutpost,
            ru="Приветствую вас в системе Берлин! В связи с аномальной пиратской активностью в системе вам необходимо пройти проверку и регистрацию.",
            en="Welcome to the New Berlin system! Due to anomalous pirate activities in the system, You'll have to be scanned and registered here.",
        ),
        VoiceLine(
            110,
            Alaric,
            ru="Да мы в курсе, давайте, проводите вашу проверку.",
            en="We know that. Let's get these scans over with.",
        ),
        VoiceLine(
            120,
            BrandenburgOutpost,
            ru="Спасибо за вашу лояльность! Проверка закончена. Вам выдано постоянное разрешение на посещение системы Берлин на весь период антитеррористической операции. Прошу извинить нас за доставленные неудобства.",
            en="Thank you for your compliance! We're done scanning. You've been granted a permanent permit to stay in New Berlin for the entire period of our anti-terrorist operations. We apologize for causing any inconvenience.",
        ),
        VoiceLine(
            130,
            Alaric,
            ru="Охтыж... А это еще что такое???",
            en="Oh, wow… What's that supposed to be???",
        ),
        VoiceLine(
            140,
            Dietrich,
            ru="Великие воины Рейнланда, задумайтесь, кого, чью власть вы защищаете? ",
            en="Great warriors of Rheinland, Take a moment to think, who's reign are you defending?",
        ),
        VoiceLine(
            150,
            Dietrich,
            ru="Прогнившую верхушку нынешнего кайзера? Им недолго осталось стоять у власти. Переходите на сторону истинных патриотов Рейнланда!",
            en="The rotting government of our current Kaiser? They're not long for the throne. Take sides with the true patriots of Rheinland!..",
        ),
        VoiceLine(
            160,
            BrandenburgCruiser,
            ru="Что-то, я смотрю, истинные патриоты Рейнланда слишком часто используют наёмников - корсаров, а они очень быстро заканчиваются.",
            en="For some reason, I've noticed that the true patriots of Rheinland often hire mercenaries - Corsairs, and they meet their end ever so quickly.",
        ),
        VoiceLine(
            170,
            Dietrich,
            ru="Хорошо смеется тот, кто смеется последним! Посмейся теперь над этим!",
            en="You find it funny, don't you? Let's see who gets the final laugh!",
        ),
        VoiceLine(
            180,
            Trent,
            ru="Кто мне объяснит, что это было? Сначала корсары, потом появляются легендарные орденские корабли и превращают Рейнландский крейсер в рейнладском пространстве в рейнлайндскую, мать её, пыль!",
            en="Can anyone explain what the hell was that? First it's Corsairs, then suddenly legendary Order ships appear and turn a Rheinland cruiser in Rheinland territory into goddamn Rheinland space dust.",
        ),
        VoiceLine(
            190,
            Alaric,
            ru="Вот точно не я. Я сам нихрена не понял!",
            en="Definitely not me. I have no idea what's going on…",
        ),
        VoiceLine(
            200,
            BrandenburgOutpost,
            ru="Пилоты, я как официальный представитель правительства Рейнланда, выражаю вам благодарность за помощь в уничтожении террористов.",
            en="Pilots, and official representatives of the Rheinland government, I express my gratitude for your help in defeating the terrorists. ",
        ),
        VoiceLine(
            210,
            BrandenburgOutpost,
            ru="С данного момента на территории Рейнланда вы пользуетесь привилегиями согласно пункту 8 третьего параграфа шестой главы кодекса Рейнланда в отношении пребывающих на его территории иностранных граждан. ",
            en="From this point on, you are granted privileges on the territory of the Rhineland, in accordance with clause 8 of the third paragraph of the sixth chapter of the Rhineland Code regarding foreign nationals residing its territory. ",
        ),
        VoiceLine(
            220,
            Alaric,
            ru="Мы у Берлина. Приземляемся, а потом встретимся в баре. Там нас уже заждались.",
            en="We've arrived to New Berlin. Let's land, and then I'll meet you at the bar. They've already waited enough.",
        ),
        VoiceLine(
            230,
            Alaric,
            ru="Мы только тебя и ждем, Трент. Давай входи в формацию с Аделмаром и полетели.",
            en="We've been waiting just for you, Trent. Enter formation with Adelmar and let's go.",
        ),
        VoiceLine(
            240,
            Alaric,
            ru="Трент, мы не можем ждать. Входи в формацию, сейчас же!",
            en="Trent, we really can't wait. Enter formation, right now!",
        ),
        VoiceLine(
            250,
            Adelmar,
            ru="Луц, ты слышал, сегодня рядом с Бранденбургом творилось черт-знает-что.",
            en="Lutz, I'm sure you've heard of the hell-knows-what-happened near Brandenburg today.",
        ),
        VoiceLine(
            260,
            Adelmar,
            ru="Ходят слухи что чуть ли не флотилия корсаров потеряла страх и решила расхреначить станцию и поживиться всем что смогут достать из ее обломков.",
            en="Rumor has it that a fleet of Corsairs have lost their fear and decided to wreck havoc on a station and make profits off its wreckage.",
        ),
        VoiceLine(
            270,
            Luc,
            ru="Ага, ты больше слушай этих придурков-репортеров, они тебе ради сенсации такооого порасскажут. ",
            en="Aha, you go on and listen to these idiot reporters. They'll tell you whateeeever it takes just to get more rating.",
        ),
        VoiceLine(
            280,
            Luc,
            ru="Кто-то в туалете воздух испортил - они раструбят что взрыв на станции.",
            en="Someone let some air go in the toilet - they claim there was an explosion at the station.",
        ),
        VoiceLine(
            290,
            Alaric,
            ru="Нет, на самом деле, сегодня на Бранденбург корсары напали вместе с этим вашим мятежным генералом. Мы как раз в эту заваруху попали когда летели к вам, да Трент?",
            en="No, actually, some Corsairs attacked Brandenburg today along with your rebellious general. We were caught inside this boiling pot on our way here, right Trent?",
        ),
        VoiceLine(
            300,
            Trent,
            ru="Ага. Обнадеживающее начало.",
            en="Yep. Quite the kickstarter actually.",
        ),
        VoiceLine(
            310,
            Luc,
            ru="М-да, Дитрих, похоже, окончательно съехал с катушек...",
            en="Hm, yeah, Ditrich. Seems like he finally lost it...",
        ),
        VoiceLine(
            320,
            Alaric,
            ru="А кто вообще такой этот Дитрих?",
            en="Who is this Ditrich actually?",
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
            en="He used to be the Kaizer's second, not too long ago. After that, I don't know what happened,",
        ),
        VoiceLine(
            350,
            Adelmar,
            ru="Я не знаю что произошло, но он вдруг ополчился на всех и ушёл в жёсткую оппозицию. А потом... Ну в общем, вы все видите.",
            en="But all of a sudden he rose against everyone and went into the cruel opposition. And then… Well… You've already seen that.",
        ),
        VoiceLine(
            360,
            Luc,
            ru="В общем, слухов ходит дохрена и больше, а я могу только порекомендовать держаться от этой всей политики подальше. ",
            en="Really, there are way too many rumors, but my advice to you would be to stay clear of all those politics.",
        ),
        VoiceLine(
            370,
            Luc,
            ru="И чем дальше - тем лучше, выше вероятность голову на плечах сохранить во всем этом винегрете.",
            en="And the farther you are, the better your chances are to keep a head on your shoulders in this hot mess.",
        ),
        VoiceLine(
            380,
            Alaric,
            ru="Джентльмены, а Трент недавно мне очень своевременный вопрос задал. Что же вы такое везете, если вам внутри Рейнланда охрана из фриленсеров понадобилась?",
            en="Gentlemen, Trent has recently asked me a very timely question. How lucky should you be, if you need to hire freelance escorts inside of Rheinland?",
        ),
        VoiceLine(
            390,
            Luc,
            ru="Груз ценный. Желающих его получить много. Деньги мы вам платим. На этом и закончим, хорошо?",
            en="Precious cargo. Many would want to put their hands on it. We pay you money. End of conversation. OK?",
        ),
        VoiceLine(
            400,
            Alaric,
            ru="Клиент всегда прав.",
            en="The client's always right.",
        ),
        VoiceLine(
            410,
            Alaric,
            ru="Все на месте. Собираем формацию. Трент, ты тоже подключайся в звено Аделмара.",
            en="Formation complete, everything's in order. Trent, enter Adelmar's comm channel as well.",
        ),
        VoiceLine(
            420,
            Alaric,
            ru="Так, теперь прокладываю маршрут до Штарке...",
            en="Setting course to Starke now...",
        ),
        VoiceLine(
            430,
            Luc,
            ru="Нет. Мы не пролетим до Штарке.",
            en="No. We wouldn't make it to Starke.",
        ),
        VoiceLine(
            440,
            Alaric,
            ru="Эмм, простите...",
            en="Huh, excuse me...",
        ),
        VoiceLine(
            450,
            Luc,
            ru="Если кто-то захочет нас перехватить, он сделает засаду на точке самого очевидного маршрута. например в районе Штарке.",
            en="If someone wants to steal our cargo, they'll ambush us at the most obvious route. Starke is one of these routes.",
        ),
        VoiceLine(
            460,
            Trent,
            ru="Что бы он там не хотел сделать, но Штарке - государственная станция, она хорошо охраняется, как и весь маршрут.",
            en="No matter what they'd want to do there, Starke is a governmental station. It's well-guarded, like all other stops in the way of military patrols",
        ),
        VoiceLine(
            470,
            Luc,
            ru="Помните, Бранденбург тоже хорошо охранялся.",
            en="Brandenburg is a well-guarded station as well.",
        ),
        VoiceLine(
            480,
            Trent,
            ru="Ваши предложения?",
            en="Got any better ideas?",
        ),
        VoiceLine(
            490,
            Luc,
            ru="Идем напрямую, через астероидное поле.",
            en="We're taking a direct course, through the asteroid field.",
        ),
        VoiceLine(
            500,
            Alaric,
            ru="Даже если вас там никто специально не ждет мы рискуем абсолютно случайно нарваться на пиратов, майнеров, мусорщиков, и чёрт-еще-знает на кого. ",
            en="Even if nobody's waiting for you there, we take the risk of accidentally running into pirates, miners, scavengers, and hell knows what.",
        ),
        VoiceLine(
            510,
            Alaric,
            ru="В астероидных поясах это всегда непредсказуемо. Вы серьезно?",
            en="Asteroid fields are always unpredictable. Are you serious?",
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
            en="Friends, we're not paying you money to protect us from nothing. We could fly through guarded routes on our own.",
        ),
        VoiceLine(
            540,
            Trent,
            ru="Ох как это все мне не нравится...",
            en="I really don't like where this is going...",
        ),
        VoiceLine(
            550,
            Alaric,
            ru="Черт, это ловушка! Атакуйте неприятеля! ",
            en="Ambush! Pirates! Trent, Lutz, engage the enemies!",
        ),
        VoiceLine(
            560,
            Trent,
            ru="Мы не вывозим! Луц, Аделмар, астероидный пояс экранирует исходящие вызовы, нужно долететь до ближайшей полицейской станции и вызвать подмогу!",
            en="We won't make it! Lutz, Adelmar, the asteroids are blocking outgoing calls. You'll have to fly to the nearest police station and call for help!",
        ),
        VoiceLine(
            570,
            Adelmar,
            ru="Луц, они правы, вызови подмогу!",
            en="Lutz, they're right, call for help!",
        ),
        VoiceLine(
            580,
            Trent,
            ru="Это было потно.",
            en="That was tedious. ",
        ),
        VoiceLine(
            590,
            Alaric,
            ru="И не говори, я уже пару раз с жизнью прощался.",
            en="You're talking? I saw my life passing in front of me already.",
        ),
        VoiceLine(
            600,
            Adelmar,
            ru="Спасибо, друзья, вы были великолепны. ",
            en="Thank you, friends. You did great. ",
        ),
        VoiceLine(
            610,
            Alaric,
            ru="Аделмар, давай к полицейскому аванпосту, да? Шутки кончились.",
            en="Adelmar, we're going to a police station, right? No more joking.",
        ),
        VoiceLine(
            620,
            Adelmar,
            ru="Луц, ты бы видел наших охранников в том бою. Я рад что мы остановили свой выбор на них. ",
            en="Lutz, had you seen our escorts in that fight. I'm so glad that we picked them for this job. ",
        ),
        VoiceLine(
            630,
            Adelmar,
            ru="Трент на своем древнем металлоломе творил такое... Временами мне казалось, что сами валькирии парят рядом с его кораблём.",
            en="Trent, with his ancient piece of scrap, did so well... At times it seemed like the Valkyries themselves have flewn around his ship.",
        ),
        VoiceLine(
            640,
            Luc,
            ru="Я уже хотел весь этот полицейский гадюшник на уши поднять, но эта их непробиваемая бюрократия... ",
            en="I was just about to call in the policemen, if not their impenetrable bureaucracy... ",
        ),
        VoiceLine(
            650,
            Luc,
            ru="Иногда мне кажется, что если тебя будут убивать у них на пороге, они с тебя же справку потребуют что это не по обоюдному согласию...",
            en="Sometimes it seems as if someone were to kill you at their doorstep, they'd demand to see proof it was not done by mutual consent…",
        ),
        VoiceLine(
            660,
            Trent,
            ru="Джентльмены, что у нас следующим пунктом? Гиперврата в Бисмарк? Давайте туда и выдвинемся, пока не произошло еще что-нибудь, на что наш рейс так богат, будь он неладен.",
            en="Gentlemen, what's next on our list? The jump gate to Bismark? Let's start heading there, before anything else that would put our lives at risk happens.",
        ),
        VoiceLine(
            670,
            Alaric,
            ru="Вижу, что все прилетели. Располагайтесь в формации и полетели, нам осталось совсем немного.",
            en="I see you've finally arrived. Re-enter formation and let's fly, we still have some way to go.",
        ),
        VoiceLine(
            680,
            Alaric,
            ru="Мы добрались до пункта назначения. Давайте поскорее приземлимся, а остальные наши дела решим в баре.",
            en="We've reached our destination. Let's land real quick, and leave the rest of our discussions to the bar.",
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
