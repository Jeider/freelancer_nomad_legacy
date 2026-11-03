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
        VoiceLine(10, Hatcher, ru="Как вы мистер Трент? Все в порядке?", en="How are you, Mr. Trent? Everything all right?"),
        VoiceLine(20, Trent, ru="Все отлично мисс Хетчер. Только вот, знаете, вчера ногу натер, а сегодня утром из душа выходил - так в пояснице кольнуло. ", en="All good, Miss Hatcher. Only, you know, I rubbed my foot raw yesterday, and this morning, getting out of the shower, my lower back twinged."),
        VoiceLine(30, Hatcher, ru="Мистер Трент, давайте не будем превращать традиционный обмен любезностями в цирк. ", en="Mr. Trent, let's not turn the usual exchange of pleasantries into a circus."),
        VoiceLine(40, Trent, ru="Так может обойдемся без обмена любезностями и перейдем сразу к делу? ", en="So maybe we skip the pleasantries and get straight to business?"),
        VoiceLine(50, Hatcher, ru="А с вами будет непросто... ", en="You're not going to make this easy..."),
        VoiceLine(60, Hatcher, ru="Мы проанализировали привезенные вами документы, они безусловно представляют огромную ценность для нас, но есть одна проблема. ", en="We've analyzed the documents you brought. They're certainly of great value to us, but there's one problem."),
        VoiceLine(70, Trent, ru="Всегда есть проблема ", en="There's always a problem."),
        VoiceLine(80, Hatcher, ru="Слишком много научных выкладок, причем настолько передовых, что у нас головастики драку устроили, не сойдясь в трактовках данных. ", en="Too many scientific calculations, and so advanced that our eggheads got into a fight because they couldn't agree on how to interpret the data."),
        VoiceLine(90, Hatcher, ru="Знаете, мистер Трент, драка между учеными выглядит со стороны весьма забавно. ", en="You know, Mr. Trent, a fight between scientists looks pretty amusing from the outside."),
        VoiceLine(100, Trent, ru="Жаль не видел. В чем моя роль? Не ученых же ваших разнимать? ", en="Shame I missed it. What's my part? Not breaking up your scientists, I hope?"),
        VoiceLine(110, Hatcher, ru="Нам нужно мнение не просто ученого, а гения, светилы в своей области, человека который мог бы дать однозначную трактовку этим данным. ", en="We need the opinion not just of a scientist, but of a genius, a leading light in his field, someone who could give a definitive reading of this data."),
        VoiceLine(120, Hatcher, ru="Я знаю такого человека, я с ним лично знакома. Это профессор Мандрейк. Он сможет во всем разобраться. ", en="I know such a person. I know him personally. It's Professor Mandrake. He'll be able to make sense of all of it."),
        VoiceLine(130, Trent, ru="Но вы не можете просто позвонить ему и попросить вам помочь потому что... ", en="But you can't just call him and ask him to help you because..."),
        VoiceLine(140, Hatcher, ru="Потому что он работает в ДипСпейсИнжиниринг и в данный момент отправился в исследовательскую экспедицию, судя по всему очень важную, потому что их служба противодействия промышленному шпионажу буквально на ушах стоит. ", en="Because he works at Deep Space Engineering, and right now he's gone on a research expedition. Apparently a very important one, because their industrial counterespionage service is practically in an uproar."),
        VoiceLine(150, Trent, ru="И мое задание будет состоять в... ", en="And my assignment will consist of..."),
        VoiceLine(160, Hatcher, ru="В полете... Мистер Трент, перестаньте. Вам нужно будет вылететь на станцию Детройт - в штаб квартиру ДипСпейс, узнать там местонахождение профессора Мандрейка, забрать его и привезти ко мне. ", en="Of flying... Mr. Trent, stop. You'll need to fly to Detroit station, to Deep Space headquarters, find out Professor Mandrake's location there, pick him up, and bring him to me."),
        VoiceLine(170, Hatcher, ru="Я дам вам свою визитку на случай проблем со службой безопасности ДипСпейс, скажете что действуете от моего имени.", en="I'll give you my card in case there's trouble with Deep Space security. Say you're acting on my behalf."),
        VoiceLine(180, Trent, ru="Служба безопасности Альянса? Никогда не слышал о такой.", en="Alliance Security Service? Never heard of it."),
        VoiceLine(190, Hatcher, ru="Это не имеет значения, мистер Трент. Гонорар за выполнение задания будет очень приятным.", en="That doesn't matter, Mr. Trent. The fee for completing the assignment will be very nice."),
        VoiceLine(200, Trent, ru="Ок. Как скажете.", en="Okay. As you say."),
        VoiceLine(210, Hatcher, ru="Окей, фрилансер, теперь посмотрим чего ты стоишь. Языком молотить научился, посмотрим как научился работать извилинами. А я за тобой присмотрю... Издалека.", en="Okay, freelancer, now we'll see what you're worth. You've learned to run your mouth. Let's see how well you've learned to use your head. And I'll be keeping an eye on you... From a distance."),
    ]


class Msn5Piratebar(Msn5, script.CutsceneProps):
    ALIAS = 'piratebar'
    TITLE = 'Пиратская база'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Trent, ru="Хай, бро! Есть чо? А то я тут с такого дальняка вернулся, что все мозги закисли, расслабиться бы... ", en="Hey, bro! Got anything? I just got back from so far out, my brain's gone sour. Could use a chance to unwind..."),
        VoiceLine(20, Smith, ru="Та не, откуда, сам с пятого на десятое перебиваюсь. ", en="Nah, where from? I'm barely scraping by myself."),
        VoiceLine(30, Trent, ru="Вот же козлы все эти пиджаки из ДипСпейс. Я им работу сработал, а они мне на Детройте даже посадку не дали, типа мордой не вышел, пропуска нет.", en="What assholes, all these suits from Deep Space. I did a job for them, and they wouldn't even let me land on Detroit. Like my face doesn't fit, no pass."),
        VoiceLine(40, Trent, ru="А у меня там заначка козырная, месяц оттопыриваться можно - из омикронов привез, дельце там одно провернул.", en="And I've got a prime stash there, enough to party for a month. Brought it from the Omicrons, pulled a little job out there."),
        VoiceLine(50, Trent, ru="А теперь из-за этой мать ее боевой готовности сидеть тут пойлом местным травиться...  А когда она еще закончится, готовность эта...", en="And now, because of this goddamn combat readiness, I'm stuck here poisoning myself on the local swill... And who knows when this readiness is even going to end..."),
        VoiceLine(55, Trent, ru="Эх, пропуск бы где раздобыть, я бы сундучок-то свой оттуда выцепил бы, оттянулись бы по полной...", en="Eh, if I could get a pass somewhere, I'd snag that chest of mine out of there, and we'd really live it up..."),
        VoiceLine(60, Smith, ru="Слыш, это, дружище... Тебя как зовут?", en="Hey, uh, buddy... What's your name?"),
        VoiceLine(70, Trent, ru="Трент. а тебя как?", en="Trent. And you?"),
        VoiceLine(80, Smith, ru="Смит. Мистер Смит.", en="Smith. Mister Smith."),
        VoiceLine(90, Trent, ru="Приятно познакомитьcя. Мистер Смит, ты там что-то сказать хотел. ", en="Nice to meet you. Mister Smith, you wanted to say something."),
        VoiceLine(100, Smith, ru="Да? Да. А, Да! Я знаю где можно пропуск достать. ", en="Yeah? Yeah. Oh, yeah! I know where you can get a pass."),
        VoiceLine(110, Trent, ru="Да ты что! И где. ", en="You don't say! And where."),
        VoiceLine(120, Smith, ru="Смотри. Вот тут склад есть секретный. Там у ребят пара штук на крайний случай точно есть. Я знаю. Попробуй с ними договориться. Только ты это... Никому. Склад-то секретный! ", en="Look. There's a secret warehouse right around here. The guys there definitely have a couple for an emergency. I know. Try to make a deal with them. Only, uh... Don't tell anyone. The warehouse is secret!"),
        VoiceLine(130, Trent, ru="Замётано, бро!", en="You got it, bro!"),
        VoiceLine(140, Smith, ru="Ты с сундучком-то забегай...", en="Swing by with that chest..."),
    ]


class Msn5Detroit(Msn5, script.CutsceneProps):
    ALIAS = 'detroit'
    TITLE = 'Детроит'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Trent, ru="Дружище, я тут одного профессора ищу, по фамилии Мандрейк. Не слышал о таком. ",
                  en="Buddy, I'm looking for a professor here, last name Mandrake. Ever heard of one?"),
        VoiceLine(20, DetroitBarman, ru="Не видел, не слышал, не разговаривал. ", en="Didn't see him, didn't hear of him, didn't talk to him."),
        VoiceLine(30, Trent, ru="А ты душка, я смотрю. А взгляни вот на это, дружище, я из профсоюза барменов.", en="Aren't you a sweetheart. Take a look at this, buddy. I'm from the bartenders' union."),
        VoiceLine(40, DetroitBarman, ru="Чёрт, ты из этих... Светани-ка этой  штукой вон туда в камеру, чтобы я потом смог оправдаться.",
                  en="Damn, you're one of those... Flash that thing at the camera over there, so I can cover myself later."),
        VoiceLine(45, DetroitBarman, ru="Ага, спасибо. Исследовательская станция в Сигма-17.", en="Yeah, thanks. A research station in Sigma-17."),
        VoiceLine(50, Trent, ru="Какая именно станция? ", en="Which station exactly?"),
        VoiceLine(60, DetroitBarman, ru="Ис-сле-до-ва-тель-ска-я. Компренде? Странно, ваши обычно посообразительнее бывают. ",
                  en="Re-se-arch. Comprende? Strange, your people are usually a bit sharper."),
        VoiceLine(70, Trent, ru="Ок. Спасибо за инфу. Видишь как легко растопить лед и найти взаимопонимание?",
                  en="Okay. Thanks for the info. See how easy it is to melt the ice and find some mutual understanding?"),
        VoiceLine(80, Trent, ru="Вот чего не хватает человечеству - взаимопонимания.", en="That's what humanity is missing — mutual understanding."),
    ]


class Msn5Equip(Msn5, script.CutsceneProps):
    ALIAS = 'equip'
    TITLE = 'Вознаграждение'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Mandrake, ru="(слабый и радостный) Хетчер, рад тебя видеть. Вы с фрилансером оказались очень вовремя.", en="(weak and joyful) Hatcher, good to see you. You and the freelancer showed up just in time."),
        VoiceLine(20, Hatcher, ru="Профессор, простите нас, вы лишний час просидели в капсуле из-за этого идиота Тилтона", en="Professor, forgive us. You sat an extra hour in the capsule because of that idiot Tilton."),

        VoiceLine(30, Mandrake, ru="Что с Тилтоном на этот раз? Опять хочет отжать полномия у СБА и получить доступ к вашим разработкам?", en="What's with Tilton this time? Trying to muscle the authority away from the ASF again and get access to your work?"),
        VoiceLine(40, Hatcher, ru="Чёрта с два у него это выйдет! Я этого никогда не допущу!", en="Like hell he'll pull that off! I'll never allow it!"),

        VoiceLine(50, Mandrake, ru="Да, я знаю. Ты никогда не отступаешь. Но зачем тебе понадобился я?", en="Yes, I know. You never back down. But why did you need me?"),

        VoiceLine(60, Hatcher, ru="Мы получили секретную информацию о разработках рейнландских учёных. Они что-то делают в Сфере. И у них большой прогресс.", en="We've received secret information on the Rheinland scientists' work. They're doing something in the Sphere. And they've made a lot of progress."),

        VoiceLine(70, Mandrake, ru="(возмущение) Как... как вы это могли допустить? Где же флот, охрана? Как?", en="(outraged) How... how could you let this happen? Where's the fleet, the security? How?"),
        VoiceLine(80, Hatcher, ru="Ну... У Тилтона стали появляться союзники. Наши силы поубавились... поэтому нам нужна ваша помощь.", en="Well... Tilton's been gaining allies. Our forces have thinned... so we need your help."),
        VoiceLine(90, Mandrake, ru="Конечно, Хетчер! Нужно действовать как можно скорее.", en="Of course, Hatcher! We need to act as soon as possible."),

        VoiceLine(100, Trent, ru="Кхм кхм. Можно я вас перебью?", en="Ahem, ahem. Mind if I interrupt?"),

        VoiceLine(110, Hatcher, ru="Что такое, Трент?", en="What is it, Trent?"),

        VoiceLine(120, Trent, ru="У меня два вопроса. Во-первых, о чеканной монете.", en="I've got two questions. First, about the hard cash."),
        VoiceLine(130, Hatcher, ru="Ах, да. Сейчас переведу деньги на твой. Счёт. А что еще?", en="Oh, right. I'll transfer the money to your account now. What else?"),
        VoiceLine(140, Trent, ru="Во-вторых, что-то твоя СБА не кажется такой уж мегаструктурой, если Либерти крутит её направо и налево.", en="Second, your ASF doesn't seem like much of a megastructure if Liberty pushes it around any way it likes."),
        VoiceLine(150, Hatcher, ru="Так, знаешь Трент, если тебе что-то не нравится, то можешь задать такой же вопрос Тилтону. Или ты хочешь, чтобы я отменила тот звонок на Грифон?", en="Look, Trent, if you don't like something, you can ask Tilton the same question. Or do you want me to cancel that call to the Griffin?"),

        VoiceLine(160, Trent, ru="Не стоит, я всё понял. Тогда до связи.", en="No need. I get it. Talk later, then."),

        # VoiceLine(10, Hatcher, ru="Профессор Мандрейк.", en="Professor Mandrake."),
        # VoiceLine(20, Mandrake, ru="Мисс Хетчер.", en="Miss Hatcher."),
        # VoiceLine(30, Hatcher, ru="Профессор, вы лишний час просидели в капсуле из-за этого идиота Тилтона. ", en="Professor, I apologize for Tilton delaying you in your capsule over an hour. It must have been uncomfortable."),
        # VoiceLine(40, Mandrake, ru="Этот недоросль, хотя, скорее, переросль, все никак не может отделаться от навязчивой идеи подловить вас, мисс Хетчер. ", en="That bastard, I thought he was over you but he clearly isn't, Miss Hatcher."),
        # VoiceLine(50, Hatcher, ru="Ага, и чем дальше, тем проще и тупее его схемы. ", en="Yeah, well the more he tries, the dumber he gets."),
        # VoiceLine(60, Mandrake, ru="Все-таки стоит опасаться таких людей. По теории больших чисел, рано или поздно они смогут добиться своего. ", en="You'd better be careful, Miss Hatcher. Statistically, if he tries enough times, he will eventually achieve his goal."),
        # VoiceLine(70, Hatcher, ru='Тилтон - вряд ли. Он считает, что постоянное повторение одних и тех же действий  в расчете на другой результат не считается сумасшествием.', en="Tilton? Insanity is doing the same thing over and over again and expecting different results. The fool is incapable of change."),
        # VoiceLine(80, Mandrake, ru='Да, но эти его "прогрессивные идеи" про то, что Орден уже отжил свое, и пора бы властям Либерти перестать оказывать хоть какую-то поддержку и вообще считаться с мнением Ордена... ', en="Yeah, but these \"progressive ideas\" of his about the Order having outlived its usefulness, and Liberty needing to pull the plug on it..."),
        # VoiceLine(90, Hatcher, ru="Могут найти поддержку только среди таких же великовозрастных дебилов, как он сам. ", en="Only fools like him would lend him support, and there aren't many fools like him."),
        # VoiceLine(100, Trent, ru="Стоп, стоп, стоп! Я тут в качестве мебели что-ли? Объясните, наконец, что происходит. ", en="Uh excuse me? I'm right here. Could someone fill me in?"),
        # VoiceLine(110, Mandrake, ru="Это очень сложно и очень долго, мистер Трент. ", en="Too difficult and time consuming."),
        # VoiceLine(120, Trent, ru="Начнем с простого. Что такое Орден?", en="How about we start with the basics, what's the Order?"),
        # VoiceLine(130, Hatcher, ru="Не так уж это и просто, Трент... Это организация... ", en="The Order, Trent is an organization..."),
        # VoiceLine(140, Trent, ru="Это я понял. Давайте мы не будем выжимать из мисс Хетчер информацию тисками, оставим ей свободу выбора. ", en="I got that much. Please don't patronize me. What do they do? Are they the bad guys or the good guys?"),
        # VoiceLine(150, Mandrake, ru="Расскажи ему. ", en="Tell him."),
        # VoiceLine(160, Hatcher, ru="Хорошо. Но то, что я скажу должно не просто остаться между нами. Это секретная информация, и за ее разглашение, Трент... ", en="Okay fine. But what I'm about to say is highly classified. If you ever disclose it..."),
        # VoiceLine(170, Trent, ru="Да-да, я понял, ты лично открутишь мне яйца. ", en="Yeah, yeah, I get it. You'll bite my head off."),
        # VoiceLine(180, Hatcher, ru="Не льсти себе. Этим займутся ребята типа Тилтона. ", en="Don't flatter yourself. That's Tilton's kind of gig. I prefer performing orchidectomies."),
        # VoiceLine(190, Trent, ru="Окей, я достаточно напуган, можно перейти к сути дела. ", en="Okay, I'm shaking in my boots. Strictly between us. "),
        # VoiceLine(200, Hatcher, ru="Никто не знает теперь как и кем был создан Орден, но он был создан влиятельными людьми, так как в свое время это была могущественная организация, которая следила за угрозами человечеству в целом и его выживанием. ", en="Nobody knows how exactly the Order was formed, or who founded it. All we know is that it's been around for a very, very long time, and its' goal is to ensure humanity's survival by monitoring for extinction level threats,"),
        # VoiceLine(210, Hatcher, ru="Её не интересовали войны между государствами, даже 80-летняя война, хотя к их чести стоит сказать, что в определенный момент это им надоело и они приложили некоторые усилия, чтобы она стала 80-летней, а не 200-летней. ", en="Not trivial things like wars between nations. Not even the 80-year war, which claimed innumerable lives."),
        # VoiceLine(220, Hatcher, ru="Эта организация была создана на случай серьезной угрозы человечеству в целом. И вот однажды этот момент наступил. ", en="The Order only intervenes when humanity faces extinction. One such threat occurred a while back,"),
        # VoiceLine(230, Hatcher, ru="Некоторое время назад все народы столкнулись с угрозой паразитической инопланетной формы жизни, но при помощи Ордена, ее воздействие удалось локализовать. ", en="when we encountered a parasitic, mind-controlling alien race. That threat was neutralized by the Order."),
        # VoiceLine(240, Trent, ru="Ряд загадочных смертей в правительствах разных стран, острые языки журналистов обозвали этот феномен чумой венценосных. ", en="I remember. There was a number of sudden unexpected deaths among top government officials from different nations. The media described it as a series of unfortunate coincidences."),
        # VoiceLine(250, Hatcher, ru='Именно. Все в итоге удалось замять, хотя человечество и стояло на пороге глобальной междоусобной войны и войны с этими космическими паразитами, прозванными "кочевниками". ', en="No coincidence. The media covered it up at the will of their collective governments. Humanity was on the verge of all-out interstellar war, our leaders puppeted by an alien race called the \"Nomads\"."),
        # VoiceLine(260, Trent, ru='Целый ряд "пограничных инцидентов". ', en="Disguised as isolated \"cross-border incidents\". "),
        # VoiceLine(270, Hatcher, ru='Точно. Только на самом деле это были не пограничные инциденты. Это была война всех со всеми и всех против "кочевников". ', en="Exactly. But in reality, these weren't isolated border incidents. It was a war of everyone against everyone, and the Order against the \"Nomads\". "),
        # VoiceLine(280, Hatcher, ru="Но как я уже сказала, всё это удалось замять, при участии Ордена, кстати. Все причастные получили награды, в узком кругу. И все договорились всё забыть. ", en="All those who had a hand in overcoming the Nomads were rewarded discreetly, and the matter was buried. "),
        # VoiceLine(290, Trent, ru="Майор Кинг, мой тезка, Джунко Зейн? ", en="Oh, Major King, Jun'Ko Zhane and my namesake, Edison Trent?"),
        # VoiceLine(300, Mandrake, ru="А он - молодец. ", en="He's smarter than he looks."),
        # VoiceLine(310, Hatcher, ru="Сама выбирала... Так вот, Трент, после этого инцидента, Орден обрел действительно большой вес в нашей геополитической системе. И это сразу поставило его под угрозу. ", en="I'm not so sure... Anyway, Trent, the Order coming out of the shadows put it at immediate risk. "),
        # VoiceLine(320, Hatcher, ru="А в нашей демократической свято системе исповедуется правило царя горы - кто смог пролезть по головам и взобраться на вершину распихивая локтями других - тот и молодец. ", en="In our Liberterian society where democracy is supposedly sacrosanct, the sad truth is whoever rises to the top of the shit pile is king."),
        # VoiceLine(330, Hatcher, ru="Вот и появилась целая орда молодых борцов уж не знаю за что, но против Ордена. ", en="And so a horde of rival organizations has appeared, all hell-bent on usurping the Order."),
        # VoiceLine(340, Hatcher, ru='Нет, если их отправить в бой против флота "кочевников", они, конечно, сразу же обделаются и сбегут, но это не мешает им в мирное время бороться против засилия Ордена в повседневной жизни Либерти. ', en="If you sent them into battle against the Nomads they'd shit their pants and run home with their tails between their legs. But right now, after such a long period of peace, these pampered upstarts are happy to politic the Order out of existence in a war of words."),
        # VoiceLine(350, Hatcher, ru="Ну и не стоит забывать что в Ордене тоже люди, а не роботы... А там, где люди - там власть и борьба за власть... ", en="And the Order itself has softened, done in by internal egos and petty conflicts."),
        # VoiceLine(360, Trent, ru="Все плохо кончилось, да? ", en="...and they lived happily ever after, right?."),
        # VoiceLine(370, Hatcher, ru="Ничего еще не кончилось... Но да, все плохо. Орден распался на две самостоятельные организации - Службу Безопасности Альянса и Новый Орден. ", en="Don't interrupt... I'm still talking. The Order fractured into two separate entities: The Alliance Security Force, and the new Order."),
        # VoiceLine(380, Trent, ru="Я понял. Ордену конец. ", en="The Order is dead? Tell me it ain't so, mummy."),
        # VoiceLine(390, Hatcher, ru="Нет, не конец. Служба Безопасности Альянса курирует кроме прочего и территорию Либерти, несмотря на противодействие со стороны некоторой части элиты Либерти, которая и натравливает против нас дуболомов типа Тилтона. ", en="Not quite. Today, the Alliance Security Force oversees Liberty but faces low-level resistance from some of the other Liberterian sub-factions."),
        # VoiceLine(400, Hatcher, ru="Но это не значит, что мы забыли свою главную функцию - защиту человечества от внешней угрозы. ", en="The new Order operates out of the shadows, a shadow of its' former self. It supposedly remains true to its' original goal – to protect humanity from extinction level threats. But they rarely make an appearance, dwindling away with time."),
        # VoiceLine(410, Trent, ru="Как скажешь...", en="I'm so confused..."),
        # VoiceLine(420, Hatcher, ru="Трент, а можно теперь я наконец... ", en="Now you know, Trent. Run along now, the grown ups need to talk."),
        # VoiceLine(430, Trent, ru="Можно. ", en="Okay."),
        # VoiceLine(440, Hatcher, ru="Профессор, рейнландцы откуда-то нашли информацию об Омикроне альфа... ", en="Professor, Rheinland officials have managed to steal our intel on Omicron Alpha..."),
        # VoiceLine(450, Mandrake, ru="И...", en="And I should care because?"),
        # VoiceLine(460, Hatcher, ru="Они нашли объект и ведут на нем работы.", en="They've set up camp around it and are experimenting on it right now."),
        # VoiceLine(470, Mandrake, ru="Рейнландцы экспериментируют со Сферой в омикроне альфа??? Вы что там, с ума посходили??? Вы чем занимаетесь??? Мистер Трент был прав... Ордену конец...", en="What? Are they out of their minds??? The fools!!! Who knows what could happen! Why was't the Sphere secured? Hatcher, how could the Order have allowed this??? Mr. Trent is right... it really is dead..."),
        # VoiceLine(480, Trent, ru="Кстати, про мистера Трента... ", en="About Mr. Trent..."),
        # VoiceLine(490, Hatcher, ru="Чего тебе еще? ", en="Why are you still here?"),
        # VoiceLine(500, Trent, ru="Чеканную монету, не более... ", en="Spare change?"),
        # VoiceLine(510, Hatcher, ru="Ах, да, извини. Делаю перевод. Свяжусь с тобой позже.", en="Ah, yes, of course. I'm transferring you your credits now. We'll be in touch. Professor, I have some Rheinland documents I need you to take a look at..."),
    ]


class Msn5Space(Msn5, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(
            0,
            HatcherStation,
            ru="Мистер Трент, если вы всё ещё заинтересованы в высокооплачиваемой работе, встретимся в баре космопорта планеты Форбс",
            en="Mr. Trent, if you're still interested in highly paid work, we'll meet at the spaceport bar on planet Forbes.",
        ),
        VoiceLine(
            2,
            Trent,
            ru="Детр+оит значит. До него лететь всего ничего. Легкотня, а не миссия.",
            en="Detroit, then. It's barely a flight to get there. Easy, not a mission.",
        ),
        VoiceLine(
            5,
            Trent,
            ru="Станция Детр+оит, это фрилансер Альфа-один, запрашиваю стыковку.",
            en="Detroit Station, this is freelancer Alpha-One, requesting docking.",
        ),
        VoiceLine(
            10,
            DetroitDispatcher,
            ru="Фриленсер альфа-один, в стыковке отказано, повторяю, стыковку запрещаю, у вас отсутствует спецпропуск. ",
            en="Freelancer alpha-one, docking denied. I repeat, docking is forbidden. You don't have a special pass.",
        ),
        VoiceLine(
            20,
            Trent,
            ru="Замечательно. И где мне его взять? ",
            en="Wonderful. And where am I supposed to get one?",
        ),
        VoiceLine(
            30,
            DetroitDispatcher,
            ru="Фрилансер альфа-один немедленно покиньте зону стыковки! ",
            en="Freelancer alpha-one, leave the docking zone immediately!",
        ),
        VoiceLine(
            40,
            Trent,
            ru="Да покидаю, покидаю, угомонись.",
            en="Yeah, I'm leaving, I'm leaving. Calm down.",
        ),
        VoiceLine(
            50,
            Trent,
            ru="У нас на родине пропуск куда-нибудь можно получить задорого и потратив кучу времени у властей, либо очень быстро и потратив совсем уж баснословные деньги,  у контрабандистов.",
            en="Back home, you can get a pass somewhere from the authorities for a lot of money and a pile of time, or very fast, and for truly outrageous money, from smugglers.",
        ),
        VoiceLine(
            60,
            Trent,
            ru="Здаров! Нужна твоя помощь! Что есть по контрабандистам в районе станции Детройт?",
            en="Hey! I need your help! What have you got on smugglers around Detroit station?",
        ),
        VoiceLine(
            70,
            AlaricStation,
            ru="Попробуй базу Монтгомери - то еще злачное местечко. ",
            en="Try Montgomery base. It's quite the seedy spot.",
        ),
        VoiceLine(
            80,
            Trent,
            ru="Значит нам туда дорога. Если и не выгорит ничего - хоть горло промочу.",
            en="Then that's where we're headed. Even if nothing pans out, at least I'll wet my throat.",
        ),
        VoiceLine(
            100,
            Trent,
            ru="Здравствуйте, хозяева, дома есть? ",
            en="Hello, hosts, anyone home?",
            cinematic=True,
        ),
        VoiceLine(
            110,
            ForbesSmugglerOne,
            ru="Ох, ёптыть, это еще что тут такое? ",
            en="Oh, shit, what the hell is this now?",
            cinematic=True,
        ),
        VoiceLine(
            120,
            ForbesSmugglerTwo,
            ru="Мил человек, ты откуда здесь такой нарисовался некрасивый? Заблудился что-ль? ",
            en="My good man, where did an ugly one like you turn up from? Lost, are you?",
            cinematic=True,
        ),
        VoiceLine(
            130,
            Trent,
            ru="Мне тут некий мистер Смит намекнул, что у вас пропуск можно получить на Детройт по сходной цене. ",
            en="A certain Mister Smith hinted that I could get a Detroit pass from you at a fair price.",
            cinematic=True,
        ),
        VoiceLine(
            140,
            ForbesSmugglerThree,
            ru="Твою же... Я сегодня же прикончу этого долбаного торчка. Все мозги себе скурил. ",
            en="Goddamn... I'm killing that damn junkie today. He's smoked his brains out.",
            cinematic=True,
        ),
        VoiceLine(
            150,
            ForbesSmugglerTwo,
            ru="Сначала займемся эти пионэром.",
            en="First we'll deal with this pioneer.",
            cinematic=True,
        ),
        VoiceLine(
            160,
            Hatcher,
            ru="Мистер Трент, у вас неприятности? ",
            en="Mr. Trent, are you in trouble?",
        ),
        VoiceLine(
            170,
            Trent,
            ru="Самую малость. ",
            en="Just a little.",
        ),
        VoiceLine(
            180,
            Hatcher,
            ru="Мистер Трент, этими джентльменами займусь я, а вы пока найдите пропуск, он должен быть на одном из этих складов",
            en="Mr. Trent, I'll deal with these gentlemen, and you find the pass in the meantime. It should be in one of these warehouses.",
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
            en="Excellent. Now, to Detroit!",
        ),
        VoiceLine(
            210,
            Trent,
            ru="Ну и как, проверочку прошел? ",
            en="So, did I pass the little test?",
        ),
        VoiceLine(
            220,
            Hatcher,
            ru="Вы это о... ",
            en="You mean...",
        ),
        VoiceLine(
            230,
            Trent,
            ru="Не делайте мне мозг, Хетчер.",
            en="Don't mess with my head, Hatcher.",
        ),
        VoiceLine(
            240,
            Hatcher,
            ru="Да, прошел.",
            en="Yes, you passed.",
        ),
        VoiceLine(
            300,
            Trent,
            ru="Мисс Хетчер, приглашаю вас в романтическое путешествие до системы Сигма-17. ",
            en="Miss Hatcher, I invite you on a romantic trip to the Sigma-17 system.",
        ),
        VoiceLine(
            310,
            Trent,
            ru="Там правда нужно будет еще станцию какую-то найти. Ис-сле-до-ва-тель-ску-ю. Но, думаю, мы справимся. ",
            en="Though we'll also have to find some station or other. A re-se-arch one. But I think we'll manage.",
        ),
        VoiceLine(
            320,
            Hatcher,
            ru="Не могу вам отказать, мистер Трент. ",
            en="I can't refuse you, Mr. Trent.",
        ),
        VoiceLine(
            330,
            Trent,
            ru="Вот так бы всегда с женщинами. ",
            en="If only it were always like this with women.",
        ),
        VoiceLine(
            340,
            Hatcher,
            ru="Есть проблема, мистер Трент. ",
            en="There's a problem, Mr. Trent.",
        ),
        VoiceLine(
            350,
            Trent,
            ru="Всегда есть проблема. Какая на этот раз? ",
            en="There's always a problem. What is it this time?",
        ),
        VoiceLine(
            360,
            Hatcher,
            ru="В этой системе находится линкор вооруженных сил Либерти. ",
            en="There's a battleship of the Liberty armed forces in this system.",
        ),
        VoiceLine(
            370,
            Trent,
            ru="А вы с вашей службой безопасности Альянса разве не сотрудничаете с военными Либерти? ",
            en="Don't you and your Alliance Security Service cooperate with the Liberty military?",
        ),
        VoiceLine(
            380,
            Hatcher,
            ru="У нас с ними есть некий конфликт интересов. ",
            en="We have a certain conflict of interest with them.",
        ),
        VoiceLine(
            390,
            Trent,
            ru="Это обнадеживает...",
            en="That's reassuring...",
        ),
        VoiceLine(
            395,
            Trent,
            ru="Станция Кларк, это фрилансер Альфа-один, запрашиваю стыковку.",
            en="Clark Station, this is freelancer Alpha-One, requesting docking.",
        ),
        VoiceLine(
            400,
            ClarkResearch,
            ru="Фрилансер альфа-один, в стыковке отказано! Немедленно покиньте зону стыковки, или мы будем вынуждены открыть огонь! ",
            en="Freelancer alpha-one, docking denied! Leave the docking zone immediately, or we will be forced to open fire!",
        ),
        VoiceLine(
            410,
            Trent,
            ru="Да что-ж такое-то. Все как сговорились. Мисс Хет... ",
            en="What is this. Like they all agreed. Miss Hat...",
        ),
        VoiceLine(
            420,
            Sigma17Trader,
            ru="SOS! Всем кто рядом! Это торговец омега-9. Подвергаюсь нападению пиратов! Срочно нужна помощь! Кларк, помогите! ",
            en="SOS! Everyone nearby! This is trader omega-9. I'm under attack by pirates! I need help urgently! Clark, help!",
        ),
        VoiceLine(
            430,
            ClarkResearch,
            ru="Ответ отрицательный. Все боевые единицы на задании, справляйтесь своими силами. ",
            en="Negative. All combat units are on assignment. Handle it with your own forces.",
        ),
        VoiceLine(
            440,
            Trent,
            ru="Вот тупые уроды. Какие у них свои силы? Там вообще люди или роботы сидят? Хетчер, за мной! ",
            en="What stupid bastards. What forces of their own do they have? Are there even people in there, or robots? Hatcher, follow me!",
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
            en="Thank you, freelancer! We're in your debt! If we can help with anything...",
        ),
        VoiceLine(
            470,
            Trent,
            ru="Хорошо, что вы сами об этом заговорили. Нам тут в доступе на Кларк отказывают, а прямо вот жуть как надо попасть. ",
            en="Good thing you brought it up. They're refusing us access to Clark, and we desperately need to get in.",
        ),
        VoiceLine(
            480,
            Sigma17Trader,
            ru="Окей, вставайте в формацию с нами, мы как раз везем груз на эту станцию.",
            en="Okay, get into formation with us. We're hauling cargo to this station right now.",
        ),
        VoiceLine(
            490,
            Sigma17Trader,
            ru="Будем считать вас кораблями охранения, тем более что это недалеко от истины, сейчас внесу вас в ведомость.",
            en="We'll count you as escort ships, especially since that's not far from the truth. I'll add you to the manifest now.",
        ),
        VoiceLine(
            500,
            Sigma17Trader,
            ru="Фрилансер, ожидайте нас рядом со станцией. Мы проведем процедуру разгрузки в доке, после чего решим вашу проблему. ",
            en="Freelancer, wait for us near the station. We'll carry out the unloading procedure in the dock, and after that we'll solve your problem.",
        ),
        VoiceLine(
            510,
            ClarkResearch,
            ru="Торговый омега-девять разрешена стыковка во втором доке. ",
            en="Trader omega-nine, docking is permitted in dock two.",
        ),
        VoiceLine(
            520,
            Sigma17Trader,
            ru="Принял, стыкуюсь.",
            en="Copy, docking.",
        ),
        VoiceLine(
            530,
            Mandrake,
            ru="Чёрт, что вы привезли? ",
            en="Damn, what did you bring?",
        ),
        VoiceLine(
            540,
            Sigma17Trader,
            ru="Что, собственно, заказывали, то и привезли. ",
            en="We brought exactly what was ordered.",
        ),
        VoiceLine(
            550,
            Mandrake,
            ru="Я заказывал компоненты для лазера из Штутгарта, от наших проверенных поставщиков, а вижу непонятные ящики с какой-то нелепой маркировкой. ",
            en="I ordered laser components from Stuttgart, from our trusted suppliers, and I see strange crates with some ridiculous markings.",
        ),
        VoiceLine(
            560,
            Sigma17Trader,
            ru="Мы забирали товар у вашего проверенного поставщика, о чем вы договаривались с ним я не знаю, но привезли мы именно то что он нам отгрузил. ",
            en="We picked the goods up from your trusted supplier. I don't know what you arranged with him, but we brought exactly what he loaded for us.",
        ),
        VoiceLine(
            570,
            ClarkResearch,
            ru="Внимание техническому персоналу, отправить инженерную команду в док два. Резкое повышение температуры в складских помещениях. ",
            en="Attention, technical personnel. Send an engineering team to dock two. Sharp rise in temperature in the storage rooms.",
        ),
        VoiceLine(
            580,
            ClarkResearch,
            ru="Взрывная разгерметизация дока два! Нарушение конструктивной целостности станции! ",
            en="Explosive decompression in dock two! Station structural integrity compromised!",
        ),
        VoiceLine(
            590,
            ClarkResearch,
            ru="Всему персоналу немедленно проследовать к ближайшим спасательным капсулам! Повторяю Всему персоналу неме... сле... жа...",
            en="All personnel, proceed immediately to the nearest escape pods! I repeat, all personnel, imme... diate... ly...",
        ),
        VoiceLine(
            600,
            Hatcher,
            ru="Капсулы не вылетели! Трент, нам нужно спасти Мандрейка! Достань капсулы из обломков базы!",
            en="The pods didn't launch! Trent, we need to save Mandrake! Get the pods out of the station wreckage!"
        ),
        VoiceLine(
            605,
            Hatcher,
            ru="Мандрейк у нас! Теперь давай постар+аемся спаст+и как можно больше учёных!",
            en="We've got Mandrake! Now let's try to save as many scientists as we can!"
        ),
        # VoiceLine(
        #     610,
        #     Trent,
        #     ru="Хетчер, а другим ты помочь не хочешь?",
        #     en="Hatcher, don't you want to help the other people too?",
        # ),
        VoiceLine(
            1300,
            Trent,
            ru="Итак, Мандрейк у меня. Куда дальше?",
            en="So, I've got Mandrake. Where next?",
        ),
        VoiceLine(
            1310,
            Hatcher,
            ru="Пора возвращаться на базу. Летим в систему Форбс.",
            en="Time to head back to base. We're flying to the Forbes system.",
        ),
        # VoiceLine(
        #     620,
        #     Trent,
        #     ru="Профессор Мандрейк. ",
        #     en="Professor Mandrake. ",
        # ),
        # VoiceLine(
        #     630,
        #     Mandrake,
        #     ru="Спасибо за своевременное спасение фриленсер... ",
        #     en="Thanks for saving me. You got here just in time, freelancer... ",
        # ),
        # VoiceLine(
        #     640,
        #     Mandrake,
        #     ru="Хотя, у меня ощущения что в тех местах, где изволите находиться вы, постоянно  что-нибудь взрывается и кто-нибудь с кем-нибудь сражается... ",
        #     en="Although, one hazards that wherever you go death and destruction follow...",
        # ),
        # VoiceLine(
        #     650,
        #     Trent,
        #     ru="Хетчер была права. Гений. ",
        #     en="Hatcher was right. You are a genius! ",
        # ),
        # VoiceLine(
        #     660,
        #     Mandrake,
        #     ru="Мисс Хетчер? Впрочем, неважно, нам нужно срочно вылететь на планету Форбс, мистер... ",
        #     en="Miss Hatcher said that? Never mind. We have to fly to planet Forbes as fast as we can go, Mr. ... ",
        # ),
        # VoiceLine(
        #     670,
        #     Trent,
        #     ru="Трент. Но у меня задание... ",
        #     en="Trent. But I'm already on a mission...",
        # ),
        # VoiceLine(
        #     680,
        #     Mandrake,
        #     ru="Молодой человек, у нас нет времени на все это. Мистер... э ... Трент, нам необходимо срочно прибыть на планету Форбс, понимаете, СРОЧНО! ",
        #     en="Young man, we don't have time for that. Mr. … Trent, we have to get to Forbes IMMEDIATELY, this is NOT NEGOTIABLE! ",
        # ),
        # VoiceLine(
        #     690,
        #     Mandrake,
        #     ru="Если вопрос в деньгах, то вопроса нет, я заплачу вам столько, сколько стоит ваш корабль вместе с вами. Я вас покупаю!!! ",
        #     en="If this is about money, I'll pay you double whatever you're owed. Triple, even!!!",
        # ),
        # VoiceLine(
        #     700,
        #     Hatcher,
        #     ru="Трент, если ты не понял - отказывать профессору бесполезно. Проще сделать то, чего он хочет и уж потом вернуться к нашим делам. ",
        #     en="Trent, as you can see, it's impossible to bargain with the professor. It'd be much easier if we just do what he wants and get back to our business later.",
        # ),
        # VoiceLine(
        #     710,
        #     Trent,
        #     ru="Как скажете. Я только за. К вратам в Форбс, леди и джентльмены! ",
        #     en="Yeah, I read you. Onwards to Forbes, ladies and gentlemen!  ",
        # ),
        VoiceLine(
            720,
            Sigma17Police,
            ru="Фриленсер альфа-один, заблокируйте орудийные системы и проследуйте с нами до линкора Грифон. ",
            en="Freelancer alpha-one, lock your weapon systems and proceed with us to the battleship Griffin.",
            cinematic=True,
        ),
        VoiceLine(
            730,
            Trent,
            ru="Да что за... Я просто летел к вратам в Форбс, в чем дело? ",
            en="What the... I was just flying to the jump gate to Forbes. What's the matter?",
            cinematic=True,
        ),
        VoiceLine(
            740,
            Sigma17Police,
            ru="Фриленсер альфа-один, повторяю, заблокируйте орудийные системы и проследуйте с нами до линкора Грифон. Приказ коммандера Тилтона. В случае сопротивления открываем огонь на поражение. ",
            en="Freelancer alpha-one, I repeat, lock your weapon systems and proceed with us to the battleship Griffin. Order of Commander Tilton. If you resist, we open fire to kill.",
            cinematic=True,
        ),
        VoiceLine(
            750,
            Hatcher,
            ru="Салют, мальчики! Он под моей юрисдикцией, расслабьтесь. Это наш человек, ясно вам?! ",
            en="Hey, boys! He's under my jurisdiction. Relax. This is our man, is that clear?!",
            cinematic=True,
        ),
        VoiceLine(
            760,
            Tilton,
            ru="Хетчер, давно не виделись. Ваши агенты влияния изрядно у нас попили крови, но сейчас ты облажалась по полной!",
            en="Hatcher, long time no see. Your agents of influence have given us plenty of grief, but now you've screwed up completely!",
            cinematic=True,
        ),
        VoiceLine(
            765,
            Tilton,
            ru="Этот фрилансер обвиняется в уничтожении научной станции Кларк! И я имею полномочия делать с ним всё, что захочу! ",
            en="This freelancer is accused of destroying Clark research station! And I have the authority to do whatever I want with him!",
            cinematic=True,
        ),
        VoiceLine(
            780,
            Trent,
            ru="Да я-то здесь причем? Станцию изнутри взорвали, я в это время вообще снаружи был, ожидал... ",
            en="What do I have to do with this? The station was blown up from the inside. I was outside the whole time, waiting...",
            cinematic=True,
        ),
        VoiceLine(
            785,
            Tilton,
            ru="Заткнись, фрилансер",
            en="Shut up, freelancer.",
            cinematic=True,
        ),
        VoiceLine(
            790,
            Hatcher,
            ru="Замолчи, Трент ",
            en="Be quiet, Trent.",
            cinematic=True,
        ),
        VoiceLine(
            810,
            Sigma17Police,
            ru="Внимание, враждебные контакты на радаре!",
            en="Attention, hostile contacts on radar!",
            cinematic=True,
        ),
        VoiceLine(
            820,
            Sigma17Assassin,
            ru="Какая встреча, герр Трент! А вы знаете, что полагается по законам Рейнланда за государственную измену? Правильно, смертная казнь! Звено, к бою! ",
            en="What a meeting, Herr Trent! Do you know what Rheinland law prescribes for treason? That's right, the death penalty! Wing, to battle!",
            cinematic=True,
        ),
        VoiceLine(
            830,
            Sigma17Police,
            ru="Звено, к бою! ",
            en="Wing, to battle!",
        ),
        VoiceLine(
            840,
            Tilton,
            ru="Капитан, промежуточный калибр на подавление враждебных контактов! Уничтожить агрессора!",
            en="Captain, intermediate caliber to suppress hostile contacts! Destroy the aggressor!",
        ),
        VoiceLine(
            850,
            Tilton,
            ru="Мистер Трент, вижу, у вас дар заводить себе друзей. ",
            en="Mr. Trent, I see you have a gift for making friends.",
        ),
        VoiceLine(
            860,
            Hatcher,
            ru="Тилтон, не тяни кота за яйца. ",
            en="Tilton, quit dragging this out.",
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
            en="I'm talking about the order that should already have reached you over the secure line, right to the Griffin's bridge.",
        ),
        VoiceLine(
            890,
            Tilton,
            ru="Я действительно, как будто что-то получил, сейчас прочитаю... ",
            en="I did seem to receive something. I'll read it now...",
        ),
        VoiceLine(
            900,
            Hatcher,
            ru="Тилтон, мать твою, если в течении пяти секунд... Ты получишь лично от меня и перед твоим личным составом. ",
            en="Tilton, damn you, if within five seconds... You'll get it from me personally, and in front of your personnel.",
        ),
        VoiceLine(
            910,
            Tilton,
            ru="Мистер Трент, в связи со вновь открывшимися обстоятельствами, вы можете быть свободны... ",
            en="Mr. Trent, in light of newly discovered circumstances, you are free to go...",
        ),
        VoiceLine(
            920,
            Trent,
            ru="О, спасибо, коммандер... ",
            en="Oh, thank you, commander...",
        ),
        VoiceLine(
            930,
            Hatcher,
            ru="Валим отсюда, быстро!!! В этой игре столько игроков что никогда не знаешь какой следующий приказ в течение этих пяти минут получит этот паладин-переросток! ",
            en="Let's get out of here, fast!!! There are so many players in this game, you never know what next order this overgrown paladin will get within these five minutes!",
        ),

        # перед джампом в форбс

        VoiceLine(1010, Trent, ru="Хетчер, я вот не пойму, ты вот вроде за Либерти, но с военными не особо в ладах.", en="Hatcher, I don't get it. You seem to be for Liberty, but you're not exactly on good terms with the military."),
        VoiceLine(1020, Trent, ru="А стоит показать твою карточку, так все гражданские сразу становятся на короткой ноге. В чём твой секрет?", en="But show your card, and all the civilians are instantly on familiar terms. What's your secret?"),

        VoiceLine(1030, Hatcher, ru='Ты хочешь спросить, с какой теперь спецслужбой работаешь?', en="You want to ask which intelligence service you're working for now?"),

        VoiceLine(1040, Trent, ru="Да-да, что-то вроде того.", en="Yeah, yeah, something like that."),

        # прилетели

        VoiceLine(1050, Hatcher, ru="Ладно. Трент. Ты слышал историю про Орден?", en="All right. Trent. Have you heard the story about the Order?"),
        VoiceLine(1060, Trent, ru="Это про моего тёзку, Джунко Зейн и прочих?", en="The one about my namesake, Jun'ko Zane, and the others?"),

        VoiceLine(1070, Hatcher, ru="Да, про них. Вкратце - организация СБА это часть того самого Ордена", en="Yes, about them. In short, the ASF is part of that same Order."),
        VoiceLine(1080, Trent, ru="Тогда почему только часть?", en="Then why only a part?"),
        VoiceLine(1090, Hatcher, ru="Ну, когда-то Орден стал своего рода одной большой спецслужбой, которая следила за всем Сектором Сириуса.", en="Well, at one point the Order became a sort of one big intelligence service that watched over the entire Sirius Sector."),
        VoiceLine(1100, Hatcher, ru="Но потом случился раздор, эта структура разделилась на Новый Орден и СБА. По началу организации сотрудничали, а со временем стали соперничать.", en="But then there was a split. This structure divided into the New Order and the ASF. At first the organizations cooperated, and over time they became rivals."),

        VoiceLine(1110, Trent, ru="То есть Аларик был прав. Вы тут местные большие шишки. Примерно как у меня было с Рейнландом.", en="So Alaric was right. You're the local big shots. Roughly like I had it with Rheinland."),
        VoiceLine(1120, Hatcher, ru="Что-то вроде такого. Только СБА гораздо больше. Мы занимаемся защитой человечества от инопланетных угроз.", en="Something like that. Only the ASF is much bigger. We handle protecting humanity from alien threats."),

        VoiceLine(1130, Trent, ru="Звучит так, будто вы действительно серьёзные ребята.", en="Sounds like you really are serious people."),

        VoiceLine(1140, Hatcher, ru="Только будь на чеку, фрилансер, эта информация не для всеобщего распространения.", en="Just stay sharp, freelancer. This information isn't for general distribution."),

        VoiceLine(1150, Trent, ru="Понял, понял. Всё как обычно.", en="Got it, got it. Same as always."),



        #
        # "Хетчер, я вот не пойму, ты вот вроде за Либерти, но с военными не особо в ладах."
        # "А стоит показать твою карточку, так все гражданские сразу становятся на короткой ноге. В чём твой секрет?"
        #
        # 'Ты хочешь спросить, с какой теперь спецслужбой работаешь?'
        #
        # "Да-да, что-то вроде того."
        #
        # "Ладно. Трент. Ты слышал историю про Орден?"
        # "Это про моего тёзку, Джунко Зейн и прочих?"
        #
        # "Да, про них. Вкратце - организация СБА это часть того самого Ордена"
        # "Тогда почему только часть?"
        # "Ну, когда-то Орден стал своего рода одной большой спецслужбой, которая следит за всем Сектором Сириуса."
        # "Но потом случился раздор, эта структура разделилась на Новый Орден и СБА. По началу организации сотрудничали, а со временем стали соперничать."
        #
        # "То есть Аларик был прав. Вы тут местные большие шишки. Примерно как у меня было с Рейнландом."
        # "Что-то вроде такого. Только СБА гораздо больше. Мы занимаемся защитой человечества от инопланетных угроз."
        #
        # "Звучит так, будто вы действительно серьёзные ребята."
        #
        # "Только будь на чеку, фрилансер, эта информация не для всеобщего распространения."
        #
        # "Понял, понял. Всё как обычно."
        #
        #
        #
        # "Хетчер, рад тебя видеть. Вы с фрилансером оказались очень вовремя."
        # "Профессор, простите нас, вы лишний час просидели в капсуле из-за этого идиота Тилтона"
        #
        # "Что с Тилтоном на этот раз? Опять хочет отжать полномия у СБА и получить доступ к вашим разработкам?"
        # "Чёрта с два у него это выйдет! Я этого никогда не допущу!"
        #
        # "Да, я знаю. Ты никогда не отступаешь. Но зачем тебе понадобился я?"
        #
        # "Мы получили секретную информацию о разработках рейнландских учёных. Они что-то делают в Сфере. И у них большой прогресс."
        #
        # "Как... как вы это могли допустить? Где же флот, охрана? Как?"
        # "Ну... У Тилтона стали появляться союзники. Наши силы поубавились... поэтому нам нужна ваша помощь."
        # "Конечно, Хетчер! Нужно действовать как можно скорее."
        #
        # "Кхм кхм. Можно я вас перебью"
        #
        # "Что такое, Трент?"
        #
        # "У меня два вопроса. Во-первых, о чеканной монете."
        #
        # "Ах, да. Сейчас переведу деньги на твой. Счёт. А что еще?"
        #
        # "Во-вторых, что-то твоя СБА не кажется такой уж мегаструктурой, если Либерти крутит её направо и налево."
        # "Так, знаешь Трент, если тебе что-то не нравится, то можешь задать такой же вопрос Тилтону. Или ты хочешь, чтобы я отменила тот звонок на Грифон?"
        #
        # "Не стоит, я всё понял. Тогда до связи."
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
    SYNC_SUBS = True

    MISSION_TITLE = 'Миссия 5. Поиск учёного'
