from story import script
from audio.sound import VoiceLine
from story.actors import (
    Trent, Hatcher, HatcherStation, Tilton, DetroitDispatcher, AlaricStation, ForbesSmugglerOne, ForbesSmugglerTwo,
    ForbesSmugglerThree, Sigma17Trader, Sigma17Police, ClarkResearch, Mandrake, Sigma17Assassin, Smith, DetroitBarman
)


class Msn5(object):
    MISSION_INDEX = 5


class Msn5Offer(Msn5, script.CutsceneProps):
    ALIAS = 'offer'
    TITLE = 'Предложение'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Hatcher, ru="Как вы мистер Трент? Все в порядке?", en="How are you, Mr. Trent? Doing fine?"),
        VoiceLine(20, Trent, ru="Все отлично мисс Хетчер. Только вот, знаете, вчера ногу натер, а сегодня утром из душа выходил - так в пояснице кольнуло. ", en="Well, Miss Hatcher, yesterday I twisted my ankle. And today, when I got out of the shower, I felt stinging pain in my back. But everything's fine regardless."),
        VoiceLine(30, Hatcher, ru="Мистер Трент, давайте не будем превращать традиционный обмен любезностями в цирк. ", en="Mr. Trent! Let's try not to turn a polite greeting into a massive joke. "),
        VoiceLine(40, Trent, ru="Так может обойдемся без обмена любезностями и перейдем сразу к делу? ", en="Then why won't we skip the politeness and get straight to business?"),
        VoiceLine(50, Hatcher, ru="А с вами будет непросто... ", en="You're not making it any easier for me..."),
        VoiceLine(60, Hatcher, ru="Мы проанализировали привезенные вами документы, они безусловно представляют огромную ценность для нас, но есть одна проблема. ", en="We've analyzed the documents you brought us, they proved to be of great value to us. However, there's only one problem."),
        VoiceLine(70, Trent, ru="Всегда есть проблема ", en="There's always a problem."),
        VoiceLine(80, Hatcher, ru="Слишком много научных выкладок, причем настолько передовых, что у нас головастики драку устроили, не сойдясь в трактовках данных. ", en="They're complicated scientific papers, consisting of very advanced scientific calculations. So advanced, in fact, that our scientists couldn't stop arguing over their meanings."),
        VoiceLine(90, Hatcher, ru="Знаете, мистер Трент, драка между учеными выглядит со стороны весьма забавно. ", en="You know, Mr. Trent, watching scientists fight each other is very entertaining."),
        VoiceLine(100, Trent, ru="Жаль не видел. В чем моя роль? Не ученых же ваших разнимать? ", en="Shame I couldn't watch them. So where do I come in? Surely you don't want me to watch over your scientists..."),
        VoiceLine(110, Hatcher, ru="Нам нужно мнение не просто ученого, а гения, светилы в своей области, человека который мог бы дать однозначную трактовку этим данным. ", en="We'll need the help of a very experienced scientist, an expert in his field. Someone who could give us an accurate interpretation of these documents."),
        VoiceLine(120, Hatcher, ru="Я знаю такого человека, я с ним лично знакома. Это профессор Мандрейк. Он сможет во всем разобраться. ", en="Luckily, I happen know a person of such skill; Professor Mandrake. If he can't figure it out, no one can."),
        VoiceLine(130, Trent, ru="Но вы не можете просто позвонить ему и попросить вам помочь потому что... ", en="And you can't just call him and ask for his help, because..."),
        VoiceLine(140, Hatcher, ru="Потому что он работает в ДипСпейсИнжиниринг и в данный момент отправился в исследовательскую экспедицию, судя по всему очень важную, потому что их служба противодействия промышленному шпионажу буквально на ушах стоит. ", en="Because he works for Deep Space Engineering, and he's currently occupied with a research expedition. A very important one it seems, because it serves to counter industrial espionage that has ears deep inside our companies."),
        VoiceLine(150, Trent, ru="И мое задание будет состоять в... ", en="And my assignment will be..."),
        VoiceLine(160, Hatcher, ru="В полете... Мистер Трент, перестаньте. Вам нужно будет вылететь на станцию Детройт - в штаб квартиру ДипСпейс, узнать там местонахождение профессора Мандрейка, забрать его и привезти ко мне. ", en="Flying in space... Enough, Mr. Trent. You'll need to fly to Detroit station, which is DSE's HQ. Fond Professor Mandrake, and bring him to me."),
        VoiceLine(170, Hatcher, ru="Я дам вам свою визитку на случай проблем со службой безопасности ДипСпейс, скажете что действуете от моего имени.", en="I'll give you my business card in case you encounter any problems with DSE's security officers. Tell them you're working for me."),
        VoiceLine(180, Trent, ru="Служба безопасности Альянса? Никогда не слышал о такой.", en="Alliance Security Force? Never heard of it."),
        VoiceLine(190, Hatcher, ru="Это не имеет значения, мистер Трент. Гонорар за выполнение задания будет очень приятным.", en="It matters not, Mr. Trent. Your reward for completing this assignment will be very generous."),
        VoiceLine(200, Trent, ru="Ок. Как скажете.", en="Ok, I'll get you what you need."),
        VoiceLine(210, Hatcher, ru="Окей, фрилансер, теперь посмотрим чего ты стоишь. Языком молотить научился, посмотрим как научился работать извилинами. А я за тобой присмотрю... Издалека.", en="O-kay freelancer, now let's see what you are all about. You've got quite a mouth there, now it's time to prove your worth in complicated situations. I'll be watching over you... From afar."),
    ]


class Msn5Piratebar(Msn5, script.CutsceneProps):
    ALIAS = 'piratebar'
    TITLE = 'Пиратская база'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Trent, ru="Хай, бро! Есть чо? А то я тут с такого дальняка вернулся, что все мозги закисли, расслабиться бы... ", en="Hey, bro! Got some more of that? I've been flying in space all day long, could use something to clear my mind..."),
        VoiceLine(20, Smith, ru="Та не, откуда, сам с пятого на десятое перебиваюсь. ", en="No way, man! Been doing this shit for hours now, that's some of the good stuff!"),
        VoiceLine(30, Trent, ru="Вот же козлы все эти пиджаки из ДипСпейс. Я им работу сработал, а они мне на Детройте даже посадку не дали, типа мордой не вышел, пропуска нет.", en="Those jackasses from Deep Space really pissed me off. I did a fair job for them, and they can't even let me land on Detroit! Not even for a quick drop-off, these assholes just won't let me in! "),
        VoiceLine(40, Trent, ru="А у меня там заначка козырная, месяц оттопыриваться можно - из омикронов привез, дельце там одно провернул.", en="And I have some really fine stuff in my cargo hold... Went on a months-long journey all the way to Omicron, and that stupid businessman just fends me off like I'm nothing."),
        VoiceLine(50, Trent, ru="А теперь из-за этой мать ее боевой готовности сидеть тут пойлом местным травиться...  А когда она еще закончится, готовность эта...", en="And now, since they're apparently ready to kill me, I'm sitting here dunking myself in poison... Heck knows when they're gonna calm down..."),
        VoiceLine(55, Trent, ru="Эх, пропуск бы где раздобыть, я бы сундучок-то свой оттуда выцепил бы, оттянулись бы по полной...", en="Ah, could be really nice if I just stumbled upon a security pass... I'd just go and grab my hard-earned payment and get out with my hands full..."),
        VoiceLine(60, Smith, ru="Слыш, это, дружище... Тебя как зовут?", en="Listen, friend... What's your name? "),
        VoiceLine(70, Trent, ru="Трент. а тебя как?", en="Trent. And you are?"),
        VoiceLine(80, Smith, ru="Смит. Мистер Смит.", en="Smith. Mister Smith."),
        VoiceLine(90, Trent, ru="Приятно познакомитьcя. Мистер Смит, ты там что-то сказать хотел. ", en="Nice to meet you, Mister Smith. You were saying...?"),
        VoiceLine(100, Smith, ru="Да? Да. А, Да! Я знаю где можно пропуск достать. ", en="Yeah? Yeah... Oh, yeah! I know where you can get a security pass."),
        VoiceLine(110, Trent, ru="Да ты что! И где. ", en="Oh, really? Where?"),
        VoiceLine(120, Smith, ru="Смотри. Вот тут склад есть секретный. Там у ребят пара штук на крайний случай точно есть. Я знаю. Попробуй с ними договориться. Только ты это... Никому. Склад-то секретный! ", en="Look. There's a secret warehouse in this area. They got a couple of security passes kept there just in case, that I know for sure. You could try negotiating with them, but, you're a... Nobody. And the warehouse is top secret!"),
        VoiceLine(130, Trent, ru="Замётано, бро!", en="Gotcha, bro! "),
        VoiceLine(140, Smith, ru="Ты с сундучком-то забегай...", en="Come back with those full hands of yours..."),
    ]


class Msn5Detroit(Msn5, script.CutsceneProps):
    ALIAS = 'detroit'
    TITLE = 'Детроит'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Trent, ru="Дружище, я тут одного профессора ищу, по фамилии Мандрейк. Не слышал о таком. ",
                  en="Hey friend, I'm looking for some professor named Mandrake. Have you seen him around here?"),
        VoiceLine(20, DetroitBarman, ru="Не видел, не слышал, не разговаривал. ", en="I've never heard this name before."),
        VoiceLine(30, Trent, ru="А ты душка, я смотрю. А взгляни вот на это, дружище, я из профсоюза барменов.", en="Aren't you a nice one. Take a look, friend. I'm from the bartender's union."),
        VoiceLine(40, DetroitBarman, ru="Чёрт, ты из этих... Светани-ка этой  штукой вон туда в камеру, чтобы я потом смог оправдаться.",
                  en="Oh shit, you're one of these... Could you just show it to the camera over there, so that I can verify later?"),
        VoiceLine(45, DetroitBarman, ru="Ага, спасибо. Исследовательская станция в Сигма-17.", en="Aha, thanks. He's on a research station in Sigma-17."),
        VoiceLine(50, Trent, ru="Какая именно станция? ", en="What station?"),
        VoiceLine(60, DetroitBarman, ru="Ис-сле-до-ва-тель-ска-я. Компренде? Странно, ваши обычно посообразительнее бывают. ",
                  en="Re-se-arch Station. Got it? Strange, your kind are usually the smart ones."),
        VoiceLine(70, Trent, ru="Ок. Спасибо за инфу. Видишь как легко растопить лед и найти взаимопонимание?",
                  en="OK, thanks for the info. You see how easy it is to just go ahead and melt the ice? "),
        VoiceLine(80, Trent, ru="Вот чего не хватает человечеству - взаимопонимания.", en="That's exactly what Humanity lacks – a little bit of warmth."),
    ]


class Msn5Equip(Msn5, script.CutsceneProps):
    ALIAS = 'equip'
    TITLE = 'Вознаграждение'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Hatcher, ru="Профессор Мандрейк.", en="Professor Mandrake."),
        VoiceLine(20, Mandrake, ru="Мисс Хетчер.", en="Miss Hatcher."),
        VoiceLine(30, Hatcher, ru="Профессор, вы лишний час просидели в капсуле из-за этого идиота Тилтона. ", en="Professor, I apologize in Tilton's name for keeping you in your capsule an extra hour."),
        VoiceLine(40, Mandrake, ru="Этот недоросль, хотя, скорее, переросль, все никак не может отделаться от навязчивой идеи подловить вас, мисс Хетчер. ", en="That bastard, I thought he was over you but he can't stop trying to catch you, Miss Hatcher."),
        VoiceLine(50, Hatcher, ru="Ага, и чем дальше, тем проще и тупее его схемы. ", en="The more he tries, the simpler and dumber his schemes become."),
        VoiceLine(60, Mandrake, ru="Все-таки стоит опасаться таких людей. По теории больших чисел, рано или поздно они смогут добиться своего. ", en="You'd better be wary of this kind of person. Statistically, if he tried enough times, he will eventually achieve his goal."),
        VoiceLine(70, Hatcher, ru='Тилтон - вряд ли. Он считает, что постоянное повторение одних и тех же действий  в расчете на другой результат не считается сумасшествием.', en="With Tilton? That's highly unlikely. He thinks that doing the same thing over and over again, expecting different results, is not considered crazy."),
        VoiceLine(80, Mandrake, ru='Да, но эти его "прогрессивные идеи" про то, что Орден уже отжил свое, и пора бы властям Либерти перестать оказывать хоть какую-то поддержку и вообще считаться с мнением Ордена... ', en="Yeah, but it's all about his \"progressive ideas\" that the Order have already outlived their purpose, and it's time for Liberty to stop playing around and end them once and for all..."),
        VoiceLine(90, Hatcher, ru="Могут найти поддержку только среди таких же великовозрастных дебилов, как он сам. ", en="Only childish morons like him would support his ideas."),
        VoiceLine(100, Trent, ru="Стоп, стоп, стоп! Я тут в качестве мебели что-ли? Объясните, наконец, что происходит. ", en="Wait, wait, wait! Am I just a decoration here? Please explain what's going on."),
        VoiceLine(110, Mandrake, ru="Это очень сложно и очень долго, мистер Трент. ", en="It'll be very difficult and time consuming."),
        VoiceLine(120, Trent, ru="Начнем с простого. Что такое Орден?", en="Let's start with the simple things, what's the Order?"),
        VoiceLine(130, Hatcher, ru="Не так уж это и просто, Трент... Это организация... ", en="It's not that simple, Trent... It's an organization..."),
        VoiceLine(140, Trent, ru="Это я понял. Давайте мы не будем выжимать из мисс Хетчер информацию тисками, оставим ей свободу выбора. ", en="That much I understand. Let's not force the information out of Miss Hatcher; give her the freedom of choice."),
        VoiceLine(150, Mandrake, ru="Расскажи ему. ", en="Tell him."),
        VoiceLine(160, Hatcher, ru="Хорошо. Но то, что я скажу должно не просто остаться между нами. Это секретная информация, и за ее разглашение, Трент... ", en="Fine. But what I'm about to say shouldn't just stay between us. This information is highly classified, and Trent, if you ever disclose it..."),
        VoiceLine(170, Trent, ru="Да-да, я понял, ты лично открутишь мне яйца. ", en="Yeah, yeah, I get it. You'll personally kick my balls."),
        VoiceLine(180, Hatcher, ru="Не льсти себе. Этим займутся ребята типа Тилтона. ", en="Don't flatter yourself. It's a job for guys like Tilton."),
        VoiceLine(190, Trent, ru="Окей, я достаточно напуган, можно перейти к сути дела. ", en="Okay, I'm shaking in fear. Now let's get down to business. "),
        VoiceLine(200, Hatcher, ru="Никто не знает теперь как и кем был создан Орден, но он был создан влиятельными людьми, так как в свое время это была могущественная организация, которая следила за угрозами человечеству в целом и его выживанием. ", en="Nobody knows how the Order was formed, or who formed it. All we know is that it used to be a powerful organization founded by people of massive influence. Their goal was to ensure humanity's survival by monitoring threats,"),
        VoiceLine(210, Hatcher, ru="Её не интересовали войны между государствами, даже 80-летняя война, хотя к их чести стоит сказать, что в определенный момент это им надоело и они приложили некоторые усилия, чтобы она стала 80-летней, а не 200-летней. ", en="and they weren't interested in wars between nations. Not even the 80-year war, although they do deserve credit for making it an 80-year war rather than 200."),
        VoiceLine(220, Hatcher, ru="Эта организация была создана на случай серьезной угрозы человечеству в целом. И вот однажды этот момент наступил. ", en="The Order only takes care of serious threats to humanity as a whole. One such threat has already come upon us a good while ago,"),
        VoiceLine(230, Hatcher, ru="Некоторое время назад все народы столкнулись с угрозой паразитической инопланетной формы жизни, но при помощи Ордена, ее воздействие удалось локализовать. ", en="when we faced a parasitic alien race. That threat was isolated, all thanks to the Order."),
        VoiceLine(240, Trent, ru="Ряд загадочных смертей в правительствах разных стран, острые языки журналистов обозвали этот феномен чумой венценосных. ", en="A series of mysterious deaths among government officials of several nations, which the media described as unfortunate events."),
        VoiceLine(250, Hatcher, ru='Именно. Все в итоге удалось замять, хотя человечество и стояло на пороге глобальной междоусобной войны и войны с этими космическими паразитами, прозванными "кочевниками". ', en="Exactly. The media hushed it, even though humanity was on the verge of war between all nations, played by an alien race called \"Nomads\"."),
        VoiceLine(260, Trent, ru='Целый ряд "пограничных инцидентов". ', en="Disguised as \"cross-border incidents\". "),
        VoiceLine(270, Hatcher, ru='Точно. Только на самом деле это были не пограничные инциденты. Это была война всех со всеми и всех против "кочевников". ', en="Precise. Although, they were never really incidents. It was a full-on war involving everyone, Nomads included. A silent war, however, with the influence of the Order. "),
        VoiceLine(280, Hatcher, ru="Но как я уже сказала, всё это удалось замять, при участии Ордена, кстати. Все причастные получили награды, в узком кругу. И все договорились всё забыть. ", en="All those involved received their awards discretely, and everyone agreed it should never be spoken of again. "),
        VoiceLine(290, Trent, ru="Майор Кинг, мой тезка, Джунко Зейн? ", en="Major King, my own namesake, Jun'Ko Zhane?"),
        VoiceLine(300, Mandrake, ru="А он - молодец. ", en="He's smarter than he looks."),
        VoiceLine(310, Hatcher, ru="Сама выбирала... Так вот, Трент, после этого инцидента, Орден обрел действительно большой вес в нашей геополитической системе. И это сразу поставило его под угрозу. ", en="I picked him myself... And so, Trent, the Order gained massive influence over our geopolitical systems, putting the organization under immediate risk. "),
        VoiceLine(320, Hatcher, ru="А в нашей демократической свято системе исповедуется правило царя горы - кто смог пролезть по головам и взобраться на вершину распихивая локтями других - тот и молодец. ", en="But, in our conservatively democratic society, the king of the hill rules. Whoever gets a chance to climb over by pushing others down, wins."),
        VoiceLine(330, Hatcher, ru="Вот и появилась целая орда молодых борцов уж не знаю за что, но против Ордена. ", en="And so, an aspiring group of warriors decided to rise against the Order for no apparent reason."),
        VoiceLine(340, Hatcher, ru='Нет, если их отправить в бой против флота "кочевников", они, конечно, сразу же обделаются и сбегут, но это не мешает им в мирное время бороться против засилия Ордена в повседневной жизни Либерти. ', en="If you sent them to battle against a Nomad fleet, they'll shit their pants and cry for their moms. But in the peaceful days of modern Liberty, they'll happily wage war against the Order."),
        VoiceLine(350, Hatcher, ru="Ну и не стоит забывать что в Ордене тоже люди, а не роботы... А там, где люди - там власть и борьба за власть... ", en="And it goes without saying that the Order is run by people, not robots. Where there's people involved, conflict arises..."),
        VoiceLine(360, Trent, ru="Все плохо кончилось, да? ", en="And they lived happily ever after, right?"),
        VoiceLine(370, Hatcher, ru="Ничего еще не кончилось... Но да, все плохо. Орден распался на две самостоятельные организации - Службу Безопасности Альянса и Новый Орден. ", en="The story's not over yet... And there's not really a happy ending. The Order split into two independent organizations: The Alliance Security Force, and the New Order."),
        VoiceLine(380, Trent, ru="Я понял. Ордену конец. ", en="So the Order is no more."),
        VoiceLine(390, Hatcher, ru="Нет, не конец. Служба Безопасности Альянса курирует кроме прочего и территорию Либерти, несмотря на противодействие со стороны некоторой части элиты Либерти, которая и натравливает против нас дуболомов типа Тилтона. ", en="Well, not exactly. The Alliance Security Force oversees Liberty territories, among other things, despite resistance from some of Liberty's powers. Those powers are run by douchebags like Tilton."),
        VoiceLine(400, Hatcher, ru="Но это не значит, что мы забыли свою главную функцию - защиту человечества от внешней угрозы. ", en="But in no way does it mean that we forgot our main goal – to protect humanity from external threats."),
        VoiceLine(410, Trent, ru="Как скажешь...", en="If you say so..."),
        VoiceLine(420, Hatcher, ru="Трент, а можно теперь я наконец... ", en="Now, Trent, can I finally..."),
        VoiceLine(430, Trent, ru="Можно. ", en="Sure."),
        VoiceLine(440, Hatcher, ru="Профессор, рейнландцы откуда-то нашли информацию об Омикроне альфа... ", en="Professor, Rheinland officials have gotten their hands on intel about Omicron Alpha..."),
        VoiceLine(450, Mandrake, ru="И...", en="And..."),
        VoiceLine(460, Hatcher, ru="Они нашли объект и ведут на нем работы.", en="They've captured the objective and are making progress with it."),
        VoiceLine(470, Mandrake, ru="Рейнландцы экспериментируют со Сферой в омикроне альфа??? Вы что там, с ума посходили??? Вы чем занимаетесь??? Мистер Трент был прав... Ордену конец...", en="Rheinlanders are running experiments on the sphere in Omicron Alpha??? Are you out of your mind??? What have you done??? Mr. Trent was right... The Order really is no more..."),
        VoiceLine(480, Trent, ru="Кстати, про мистера Трента... ", en="About that Mr. Trent..."),
        VoiceLine(490, Hatcher, ru="Чего тебе еще? ", en="What else do you need?"),
        VoiceLine(500, Trent, ru="Чеканную монету, не более... ", en="Toss a coin to your freelancer."),
        VoiceLine(510, Hatcher, ru="Ах, да, извини. Делаю перевод. Свяжусь с тобой позже.", en="Ah, yes, sorry. I'm transferring your credits. We'll be in touch."),
    ]


class Msn5Space(Msn5, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(
            0,
            HatcherStation,
            ru="Мистер Трент, если вы всё ещё заинтересованы в высокооплачиваемой работе, встретимся в баре космопорта планеты Форбс",
            en="Mr. Trent, if you're still interested in a high-income job, meet me at the bar on planet Forbes. Hatcher out.",
        ),
        VoiceLine(
            2,
            Trent,
            ru="Детр+оит значит. До него лететь всего ничего. Легкотня, а не миссия.",
            en="So, Detroit. This is close station. Piece of cake.",
        ),
        VoiceLine(
            5,
            Trent,
            ru="Станция Детр+оит, это фрилансер Альфа-один, запрашиваю стыковку.",
            en="Destroit Station, this is freelancer alpha-one, requesting to dock.",
        ),
        VoiceLine(
            10,
            DetroitDispatcher,
            ru="Фриленсер альфа-один, в стыковке отказано, повторяю, стыковку запрещаю, у вас отсутствует спецпропуск. ",
            en="Freelancer alpha-one, your request to dock is denied. You do not have clearance to dock with this station.",
        ),
        VoiceLine(
            20,
            Trent,
            ru="Замечательно. И где мне его взять? ",
            en="Just my luck. Where do I get that clearance?",
        ),
        VoiceLine(
            30,
            DetroitDispatcher,
            ru="Фрилансер альфа-один немедленно покиньте зону стыковки! ",
            en="Freelancer alpha-one, leave the docking area immediately!",
        ),
        VoiceLine(
            40,
            Trent,
            ru="Да покидаю, покидаю, угомонись.",
            en="I'm leaving, I'm leaving… Calm down...",
        ),
        VoiceLine(
            50,
            Trent,
            ru="У нас на родине пропуск куда-нибудь можно получить задорого и потратив кучу времени у властей, либо очень быстро и потратив совсем уж баснословные деньги,  у контрабандистов.",
            en="Back on my home planet, you could either spend a lot of time and money to get where you need, or take a shortcut and spend even more money on smugglers.",
        ),
        VoiceLine(
            60,
            Trent,
            ru="Здаров! Нужна твоя помощь! Что есть по контрабандистам в районе станции Детройт?",
            en="Sup? I need your help. Where can I find smugglers around Detroit?",
        ),
        VoiceLine(
            70,
            AlaricStation,
            ru="Попробуй базу Монтгомери - то еще злачное местечко. ",
            en="You could try Montgomery station, although it's a rather mischievous place.",
        ),
        VoiceLine(
            80,
            Trent,
            ru="Значит нам туда дорога. Если и не выгорит ничего - хоть горло промочу.",
            en="Then I'm up for some mischief. If nothing comes up my alley, at least I'll know I got my hands dirty.",
        ),
        VoiceLine(
            100,
            Trent,
            ru="Здравствуйте, хозяева, дома есть? ",
            en="Hello? Is anyone home?",
            cinematic=True,
        ),
        VoiceLine(
            110,
            ForbesSmugglerOne,
            ru="Ох, ёптыть, это еще что тут такое? ",
            en="Hey, what the hell was that? ",
            cinematic=True,
        ),
        VoiceLine(
            120,
            ForbesSmugglerTwo,
            ru="Мил человек, ты откуда здесь такой нарисовался некрасивый? Заблудился что-ль? ",
            en="Hey stranger! You don't look like you belong here. Did you lose something? ",
            cinematic=True,
        ),
        VoiceLine(
            130,
            Trent,
            ru="Мне тут некий мистер Смит намекнул, что у вас пропуск можно получить на Детройт по сходной цене. ",
            en="A little bird named Mr. Smith told me that I can get a Detroit security pass for a reasonable price here. ",
            cinematic=True,
        ),
        VoiceLine(
            140,
            ForbesSmugglerThree,
            ru="Твою же... Я сегодня же прикончу этого долбаного торчка. Все мозги себе скурил. ",
            en="That stupid… I'm gonna finish that stoner off right now! He smoked his last blunt.",
            cinematic=True,
        ),
        VoiceLine(
            150,
            ForbesSmugglerTwo,
            ru="Сначала займемся эти пионэром.",
            en="Let's deal with this douchebag first.",
            cinematic=True,
        ),
        VoiceLine(
            160,
            Hatcher,
            ru="Мистер Трент, у вас неприятности? ",
            en="Mr. Trent, are you having trouble?",
        ),
        VoiceLine(
            170,
            Trent,
            ru="Самую малость. ",
            en="A little bit.",
        ),
        VoiceLine(
            180,
            Hatcher,
            ru="Мистер Трент, этими джентльменами займусь я, а вы пока найдите пропуск, он должен быть на одном из этих складов",
            en="Mr. Trent, I'll take care of these gentlemen. Go ahead and look for the security pass, it has to be in one of these warehouses.",
        ),
        VoiceLine(
            190,
            Trent,
            ru="Пропуск у меня. ",
            en="I have the pass.",
        ),
        VoiceLine(
            200,
            Hatcher,
            ru="Отлично, теперь - в Детройт! ",
            en="Great! Now, head to Detroit!",
        ),
        VoiceLine(
            210,
            Trent,
            ru="Ну и как, проверочку прошел? ",
            en="Well, did I pass the test?",
        ),
        VoiceLine(
            220,
            Hatcher,
            ru="Вы это о... ",
            en="How did you...",
        ),
        VoiceLine(
            230,
            Trent,
            ru="Не делайте мне мозг, Хетчер.",
            en="Don't mess with me, Hatcher.",
        ),
        VoiceLine(
            240,
            Hatcher,
            ru="Да, прошел.",
            en="You passed.",
        ),
        VoiceLine(
            300,
            Trent,
            ru="Мисс Хетчер, приглашаю вас в романтическое путешествие до системы Сигма-17. ",
            en="Miss Hatcher, would you like to go with me on a romantic getaway to Sigma-17?",
        ),
        VoiceLine(
            310,
            Trent,
            ru="Там правда нужно будет еще станцию какую-то найти. Ис-сле-до-ва-тель-ску-ю. Но, думаю, мы справимся. ",
            en="We'll have to find some station though. A r-e-s-e-a-r-c-h station. But I think we can handle it. ",
        ),
        VoiceLine(
            320,
            Hatcher,
            ru="Не могу вам отказать, мистер Трент. ",
            en="How could I refuse, Mr. Trent?",
        ),
        VoiceLine(
            330,
            Trent,
            ru="Вот так бы всегда с женщинами. ",
            en="If only other women were like that...",
        ),
        VoiceLine(
            340,
            Hatcher,
            ru="Есть проблема, мистер Трент. ",
            en="But there's a problem, Mr. Trent.",
        ),
        VoiceLine(
            350,
            Trent,
            ru="Всегда есть проблема. Какая на этот раз? ",
            en="Always a problem. Which one is it this time?",
        ),
        VoiceLine(
            360,
            Hatcher,
            ru="В этой системе находится линкор вооруженных сил Либерти. ",
            en="There's a Navy battleship in that system.",
        ),
        VoiceLine(
            370,
            Trent,
            ru="А вы с вашей службой безопасности Альянса разве не сотрудничаете с военными Либерти? ",
            en="And your Alliance Security Force is not working with the Liberty Navy?",
        ),
        VoiceLine(
            380,
            Hatcher,
            ru="У нас с ними есть некий конфликт интересов. ",
            en="There's a certain conflict of interests between us. ",
        ),
        VoiceLine(
            390,
            Trent,
            ru="Это обнадеживает...",
            en="Boy, am I glad to hear that...",
        ),
        VoiceLine(
            395,
            Trent,
            ru="Станция Кларк, это фрилансер Альфа-один, запрашиваю стыковку.",
            en="Station Clark, this is freelancer alpha-one, requesting to dock.",
        ),
        VoiceLine(
            400,
            ClarkResearch,
            ru="Фрилансер альфа-один, в стыковке отказано! Немедленно покиньте зону стыковки, или мы будем вынуждены открыть огонь! ",
            en="Freelancer alpha one, your request to dock is denied! Leave the area immediately, or we will open fire!",
        ),
        VoiceLine(
            410,
            Trent,
            ru="Да что-ж такое-то. Все как сговорились. Мисс Хет... ",
            en="Yeah, yeah, just as I suspected. Miss Hatc...",
        ),
        VoiceLine(
            420,
            Sigma17Trader,
            ru="SOS! Всем кто рядом! Это торговец омега-9. Подвергаюсь нападению пиратов! Срочно нужна помощь! Кларк, помогите! ",
            en="Mayday! To all ships in the vicinity! This is freighter convoy omega-9. We are under attack by pirates! We require immediate assistance! Clark, please send someone!",
        ),
        VoiceLine(
            430,
            ClarkResearch,
            ru="Ответ отрицательный. Все боевые единицы на задании, справляйтесь своими силами. ",
            en="Negative. All units are currently on a mission. You are on your own.",
        ),
        VoiceLine(
            440,
            Trent,
            ru="Вот тупые уроды. Какие у них свои силы? Там вообще люди или роботы сидят? Хетчер, за мной! ",
            en="Goddamn idiots. Do they even have their own units? I bet they have more robots than humans on board. Hatcher, come on!",
        ),
        VoiceLine(
            450,
            Hatcher,
            ru="Трент... Чёрт!",
            en="Trent... Damn!",
        ),
        VoiceLine(
            460,
            Sigma17Trader,
            ru="Спасибо вам, фриленсер! Мы у вас в долгу! Если можем чем-то помочь... ",
            en="Thank you, freelancer! We owe you! If there's anything we can help you with...",
        ),
        VoiceLine(
            470,
            Trent,
            ru="Хорошо, что вы сами об этом заговорили. Нам тут в доступе на Кларк отказывают, а прямо вот жуть как надо попасть. ",
            en="I'm glad you offered. We don't have clearance to dock with Clark, but we really, really have to get there.",
        ),
        VoiceLine(
            480,
            Sigma17Trader,
            ru="Окей, вставайте в формацию с нами, мы как раз везем груз на эту станцию.",
            en="Okay, get into formation with us. We're transporting cargo over to the station.",
        ),
        VoiceLine(
            490,
            Sigma17Trader,
            ru="Будем считать вас кораблями охранения, тем более что это недалеко от истины, сейчас внесу вас в ведомость.",
            en="We can consider you an escort since you helped us out in a battle. I'll add you to our manifest.",
        ),
        VoiceLine(
            500,
            Sigma17Trader,
            ru="Фрилансер, ожидайте нас рядом со станцией. Мы проведем процедуру разгрузки в доке, после чего решим вашу проблему. ",
            en="Freelancer, wait for us outside the station. We'll unload the cargo in the docking bay, and then fulfill our end of the deal.",
        ),
        VoiceLine(
            510,
            ClarkResearch,
            ru="Торговый омега-девять разрешена стыковка во втором доке. ",
            en="Freighter convoy omega-nine, you are clear to dock. Please proceed dock two. ",
        ),
        VoiceLine(
            520,
            Sigma17Trader,
            ru="Принял, стыкуюсь.",
            en="Roger that.",
        ),
        VoiceLine(
            530,
            Mandrake,
            ru="Чёрт, что вы привезли? ",
            en="What the hell is that?",
        ),
        VoiceLine(
            540,
            Sigma17Trader,
            ru="Что, собственно, заказывали, то и привезли. ",
            en="That's what you ordered, sir. ",
        ),
        VoiceLine(
            550,
            Mandrake,
            ru="Я заказывал компоненты для лазера из Штутгарта, от наших проверенных поставщиков, а вижу непонятные ящики с какой-то нелепой маркировкой. ",
            en="I ordered laser components from Stuttgart, from our trusted suppliers. What you got me are strange boxes with some ridiculous markings on them.",
        ),
        VoiceLine(
            560,
            Sigma17Trader,
            ru="Мы забирали товар у вашего проверенного поставщика, о чем вы договаривались с ним я не знаю, но привезли мы именно то что он нам отгрузил. ",
            en="We got these boxes from your trusted suppliers and brought them all the way to you. We have no clue as to what you ordered.",
        ),
        VoiceLine(
            570,
            ClarkResearch,
            ru="Внимание техническому персоналу, отправить инженерную команду в док два. Резкое повышение температуры в складских помещениях. ",
            en="Attention engineers, send a team to dock two immediately. I'm reading a sharp increase in temperature from the freshly unloaded cargo.",
        ),
        VoiceLine(
            580,
            ClarkResearch,
            ru="Взрывная разгерметизация дока два! Нарушение конструктивной целостности станции! ",
            en="There's been an explosion in dock two! Structural integrity has been compromised! ",
        ),
        VoiceLine(
            590,
            ClarkResearch,
            ru="Всему персоналу немедленно проследовать к ближайшим спасательным капсулам! Повторяю Всему персоналу неме... сле... жа...",
            en="All personnel, proceed to the escape pods immediately! I repeat, all personnel, pro... esca...",
        ),
        VoiceLine(
            600,
            Hatcher,
            ru="Капсулы не вылетели! Трент, нам нужно спасти Мандрейка! Достань капсулы из обломков базы!",
            en="Escape pod did not launched! Trent, we need to save Mandrake! Get the capsules from the base chunks!"
        ),
        VoiceLine(
            605,
            Hatcher,
            ru="Мандрейк у нас! Теперь давай постар+аемся спаст+и как можно больше учёных!",
            en="We got Mandrake! May be we still can save everyone of scientists!"
        ),
        VoiceLine(
            610,
            Trent,
            ru="Хетчер, а другим ты помочь не хочешь?",
            en="Hatcher, don't you want to help the others too?",
        ),
        VoiceLine(
            620,
            Trent,
            ru="Профессор Мандрейк. ",
            en="Professor Mandrake. ",
        ),
        VoiceLine(
            630,
            Mandrake,
            ru="Спасибо за своевременное спасение фриленсер... ",
            en="Thanks for being there on time, freelancer... ",
        ),
        VoiceLine(
            640,
            Mandrake,
            ru="Хотя, у меня ощущения что в тех местах, где изволите находиться вы, постоянно  что-нибудь взрывается и кто-нибудь с кем-нибудь сражается... ",
            en="Although, I have a feeling that wherever you go, explosions and death battles will follow...",
        ),
        VoiceLine(
            650,
            Trent,
            ru="Хетчер была права. Гений. ",
            en="Hatcher was right. You're a genius! ",
        ),
        VoiceLine(
            660,
            Mandrake,
            ru="Мисс Хетчер? Впрочем, неважно, нам нужно срочно вылететь на планету Форбс, мистер... ",
            en="Miss Hatcher? Never mind. We have to fly to planet Forbes as fast as we can, Mr. ... ",
        ),
        VoiceLine(
            670,
            Trent,
            ru="Трент. Но у меня задание... ",
            en="Trent. But I have a mission...",
        ),
        VoiceLine(
            680,
            Mandrake,
            ru="Молодой человек, у нас нет времени на все это. Мистер... э ... Трент, нам необходимо срочно прибыть на планету Форбс, понимаете, СРОЧНО! ",
            en="Young man, we don't have any time for that. Mr. … Um… Trent, we have to get to Forbes IMMEDIATELY, this is URGENT! ",
        ),
        VoiceLine(
            690,
            Mandrake,
            ru="Если вопрос в деньгах, то вопроса нет, я заплачу вам столько, сколько стоит ваш корабль вместе с вами. Я вас покупаю!!! ",
            en="If that's about money, I'll pay you whatever you and your ship are worth. I'll buy you, dammit!!!",
        ),
        VoiceLine(
            700,
            Hatcher,
            ru="Трент, если ты не понял - отказывать профессору бесполезно. Проще сделать то, чего он хочет и уж потом вернуться к нашим делам. ",
            en="Trent, as you can see, it's impossible to bargain with the professor. It'd be much easier if we just do what he wants and get back to our business later.",
        ),
        VoiceLine(
            710,
            Trent,
            ru="Как скажете. Я только за. К вратам в Форбс, леди и джентльмены! ",
            en="Yeah, whatever, I'm with you. Onwards to Forbes, ladies and gentlemen!  ",
        ),
        VoiceLine(
            720,
            Sigma17Police,
            ru="Фриленсер альфа-один, заблокируйте орудийные системы и проследуйте с нами до линкора Грифон. ",
            en="Freelancer alpha-one, turn your weapons down and follow us to battleship Griffin.",
            cinematic=True,
        ),
        VoiceLine(
            730,
            Trent,
            ru="Да что за... Я просто летел к вратам в Форбс, в чем дело? ",
            en="What the... I was just flying to Forbes, what's the matter? ",
            cinematic=True,
        ),
        VoiceLine(
            740,
            Sigma17Police,
            ru="Фриленсер альфа-один, повторяю, заблокируйте орудийные системы и проследуйте с нами до линкора Грифон. Приказ коммандера Тилтона. В случае сопротивления открываем огонь на поражение. ",
            en="Freelancer alpha-one, I repeat, turn your weapons down and follow us to battleship Griffin. That's an order from commander Tilton. If you fail to comply, we will open fire. ",
            cinematic=True,
        ),
        VoiceLine(
            750,
            Hatcher,
            ru="Салют, мальчики! Он под моей юрисдикцией, расслабьтесь. Это наш человек, ясно вам?! ",
            en="Hey there, boys! This freelancer is under my jurisdiction. Calm down. He's on our side. Is that clear?",
            cinematic=True,
        ),
        VoiceLine(
            760,
            Tilton,
            ru="Этот фрилансер обвиняется ни много ни мало в уничтожении научной станции Кларк! И я имею полномочия делать с ним все, что захочу! ",
            en="This freelancer is responsible for no less than the destruction of the Clark research station! And I have the authority, by all means, to deal with him as I please!",
            cinematic=True,
        ),
        VoiceLine(
            770,
            Tilton,
            ru="Да я-то здесь причем? Станцию изнутри взорвали, я в это время вообще снаружи был, ожидал... ",
            en="I'm responsible for WHAT? The station blew up from the inside, while I was out in space waiting for...",
            cinematic=True,
        ),
        VoiceLine(
            780,
            Tilton,
            ru="Замолчи, Трент ",
            en="Shut up, Trent!",
            cinematic=True,
        ),
        VoiceLine(
            790,
            Hatcher,
            ru="Заткнись, фрилансер",
            en="Shut up, freelancer! ",
            cinematic=True,
        ),
        VoiceLine(
            810,
            Sigma17Police,
            ru="Внимание, враждебные контакты на радаре!",
            en="Attention, we're reading hostiles on our radar!",
            cinematic=True,
        ),
        VoiceLine(
            820,
            Sigma17Assassin,
            ru="Какая встреча, герр Трент! А вы знаете, что полагается по законам Рейнланда за государственную измену? Правильно, смертная казнь! Звено, к бою! ",
            en="What a coincidence, Herr Trent! Do you know what's the penalty for treason in Rheinland? That's right, death! All wingmen, engage!",
            cinematic=True,
        ),
        VoiceLine(
            830,
            Sigma17Police,
            ru="Звено, к бою! ",
            en="Blast them!",
        ),
        VoiceLine(
            840,
            Tilton,
            ru="Капитан, промежуточный калибр на подавление враждебных контактов! Уничтожить агрессора!",
            en="Captain, we must destroy all hostile ships in the vicinity. Fire at will!",
        ),
        VoiceLine(
            850,
            Tilton,
            ru="Мистер Трент, вижу, у вас дар заводить себе друзей. ",
            en="Mr. Trent, I see you're good at making friends. ",
        ),
        VoiceLine(
            860,
            Hatcher,
            ru="Тилтон, не тяни кота за яйца. ",
            en="Tilton, you're such a laggard.",
        ),
        VoiceLine(
            870,
            Tilton,
            ru="Это ты о чем, Хетчер? ",
            en="What are you talking about, Hatcher?",
        ),
        VoiceLine(
            880,
            Hatcher,
            ru="Это я о том приказе который уже должен был тебе прийти по защищенной линии прямо на мостик Грифона. ",
            en="I'm talking about the order that should've come through a protected channel directly to the Griffin's bridge by now.",
        ),
        VoiceLine(
            890,
            Tilton,
            ru="Я действительно, как будто что-то получил, сейчас прочитаю... ",
            en="Now that you mention it, I thing I did just receive something...",
        ),
        VoiceLine(
            900,
            Hatcher,
            ru="Тилтон, мать твою, если в течении пяти секунд... Ты получишь лично от меня и перед твоим личным составом. ",
            en="Dammit, Tilton, if you don't read it in 5 seconds, I'll come over to your bridge and personally scold you in front of your subordinates.",
        ),
        VoiceLine(
            910,
            Tilton,
            ru="Мистер Трент, в связи со вновь открывшимися обстоятельствами, вы можете быть свободны... ",
            en="Mr. Trent, it appears that according to current circumstances, you are free to go...",
        ),
        VoiceLine(
            920,
            Trent,
            ru="О, спасибо, коммандер... ",
            en="Great, thank commander...",
        ),
        VoiceLine(
            930,
            Hatcher,
            ru="Валим отсюда, быстро!!! В этой игре столько игроков что никогда не знаешь какой следующий приказ в течение этих пяти минут получит этот паладин-переросток! ",
            en="Let's get out of here, fast!!! There are too many players in the game, I can't guarantee this buffoon won't get any more orders in the next five minutes!",
        ),
        VoiceLine(
            950,
            Trent,
            ru="Хетчер, мне кажется, или у вас с этим Тилтоном давняя любовная история? ",
            en="Hatcher, I get a feeling that you and Tilton had an affair in the distant past.",
        ),
        VoiceLine(
            960,
            Hatcher,
            ru="Не твоё дело, фриленсер! ",
            en="None of your business, freelancer!",
        ),
        VoiceLine(
            970,
            Trent,
            ru="Понял, входим во врата...",
            en="Gotcha, docking with the gate...",
        ),

    ]


class Mission5(Msn5, script.StoryMission):
    MISSION_INDEX = 5
    CUTSCENES = [
        Msn5Offer,
        Msn5Piratebar,
        Msn5Detroit,
        Msn5Equip,
    ]
    SPACE_CLASS = Msn5Space
    SYNC_SPACE = True

    MISSION_TITLE = 'Миссия 5. Поиск учёного'
