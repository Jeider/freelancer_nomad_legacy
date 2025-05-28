from story import script
from audio.sound import VoiceLine
from story.actors import (
    Trent, Alaric, Informer, Dietrich, Adelmar, Luc, BrandenburgOutpost, BrandenburgCruiser
)


class Msn1(object):
    MISSION_INDEX = 1


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
            en="Aha. Quite the kickstarter actually.",
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
    CUTSCENES = []
    SPACE_CLASS = Msn1Space
    SYNC_SPACE = False

    MISSION_TITLE = 'Миссия 1. Конвой в Бисмарк'
