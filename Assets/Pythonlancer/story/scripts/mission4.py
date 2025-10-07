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
        VoiceLine(10, Jacobo, ru="", en="Herr Trent, is that you?"),
        VoiceLine(20, Jacobo, ru="",
                  en="Herr Trent, thank you so much for coming. I'm in trouble. The Rheinland authorities are looking for me."),
        VoiceLine(30, Trent, ru="",
                  en="I already guessed that. And I'm getting that familiar sense of someone trying to get me into trouble."),
        VoiceLine(40, Jacobo, ru="",
                  en="Herr Trent, you do not understand. A matter of utmost importance. I need to deliver important documents to Liberty."),
        VoiceLine(50, Trent, ru="",
                  en="And yet again I'm being dragged into a game of espionage... Jacobo, are you aware that I'm currently working for the very same Rheinland authorities you're trying to avoid?"),
        VoiceLine(60, Jacobo, ru="",
                  en="Herr Trent, you're a freelancer. You did not take an oath. After the job is done, nothing connects you to your client."),
        VoiceLine(62, Jacobo, ru="",
                  en="Herr Trent, if we can deliver these VERY important documents to Liberty, to the Forbes system, they'll pay us a lot of money, and I mean a LOT, you see?"),
        VoiceLine(65, Jacobo, ru="", en="I probably won't make it alone, but with you on my side..."),
        VoiceLine(67, Jacobo, ru="", en="And if you don't help me, they'll probably just kill me..."),
        VoiceLine(70, Trent, ru="", en="I'm gonna regret doing that... So, what's the plan?"),
        VoiceLine(80, Jacobo, ru="",
                  en="Herr Trent, thank you! You won't regret it! Launch into space. My friends will help me get to the landing pad quietly. Meet me in orbit."),
        VoiceLine(90, Trent, ru="", en="See you there."),
    ]


class Msn4Reward(Msn4, script.CutsceneProps):
    ALIAS = 'reward'
    TITLE = 'Вознаграждение'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Hatcher, ru="", en="Gentlemen."),
        VoiceLine(20, Trent, ru="", en="Miss Hatcher."),
        VoiceLine(30, Alaric, ru="", en="Miss Hatcher, you have such lovely, deep eyes."),
        VoiceLine(40, Hatcher, ru="", en="Cut this nonsense immediately, you don't want to irritate me."),
        VoiceLine(45, Hatcher, ru="", en="Let's get to our business. You've done a fine job."),
        VoiceLine(50, Hatcher, ru="", en="I will avoid asking how you managed to escape Rheinland with THIS kind of material."),
        VoiceLine(55, Hatcher, ru="", en="I'm a delicate lady, I'm afraid I might not be able to handle it."),
        VoiceLine(60, Trent, ru="", en="We did what we had to do."),
        VoiceLine(70, Hatcher, ru="", en="Heh, seems like you had fun. And by the way, we are looking for top-notch skilled Freelancers such as yourselves to help us perform, say, some non-standard tasks. Have you got any plans for the near future?"),
        VoiceLine(80, Alaric, ru="", en="We've always got time for you..."),
        VoiceLine(90, Trent, ru="", en="Shut up, Alaric. Since we're now considered enemies of the Rheinland state, I suppose we don't have any plans yet."),
        VoiceLine(100, Hatcher, ru="", en="So, if we have a couple of well-paid tasks that fit your field of work..."),
        VoiceLine(110, Trent, ru="", en="Then we won't hesitate to fulfill them. That is, unless these tasks make us enemies of the Liberty state, too."),
        VoiceLine(120, Hatcher, ru="", en="Oh dear, no, I don't think it'll ever come to this."),
        VoiceLine(130, Trent, ru="", en="Sure hope so..."),
    ]


class Msn4Final(Msn4, script.CutsceneProps):
    ALIAS = 'final'
    TITLE = 'Вознаграждение'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Alaric, ru="", en="Awesome, Trent! Who knew you'd be so good at finding clients and closing deals?"),
        VoiceLine(20, Trent, ru="", en="I'm also good at making enemies and getting close to being murdered."),
        VoiceLine(30, Alaric, ru="", en="Oh come on... You just started your freelancing career, a complete newbie, and now you're taking jobs for the government with appropriate payments!"),
        VoiceLine(40, Trent, ru="", en="Mhm, one of those governments have already put a price on my head. And oh do I hope they forget about me soon with everything that's going on there."),
        VoiceLine(50, Alaric, ru="", en="Seriously, the Rheinland military will most likely fall apart soon. They won't bother looking for us."),
        VoiceLine(60, Trent, ru="", en="You seem very confident. Come on, Alaric, what are you hiding from me?"),
        VoiceLine(70, Alaric, ru="", en="That Miss Hatcher, do you know who she is?"),
        VoiceLine(80, Trent, ru="", en="Well, of course I do! I've known her for a whole three hours! Screw you, Alaric."),
        VoiceLine(90, Alaric, ru="", en="She's an officer in one of Liberty's secret service agencies."),
        VoiceLine(100, Trent, ru="", en="God dammit! Not again..."),
        VoiceLine(110, Alaric, ru="", en="You don't get it. It's such a special and secret service, that not even their own counterparts in their own government know they exist."),
        VoiceLine(120, Trent, ru="", en="Then how do you know that, Alaric?"),
        VoiceLine(130, Alaric, ru="", en="Oh... I need to go..."),
        VoiceLine(140, Trent, ru="", en="I can't believe I got into this botch again!"),
    ]


class Msn4Space(Msn4, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(
            0,
            JacoboTrader,
            ru="Герр Трент, это Джакобо! Герр Трент, вы помните меня? Герр Трент, нам очень нужна ваша помощь. Вы же были не против помочь нам если понадобится, помните? Герр Трент, прошу вас как можно быстрее прибыть на планету Норторф в систему Мюнхен!",
            en="Herr Trent, this is JacoboTrader! Herr Trent, do you remember me? Herr Trent, I really need your help. You said you wouldn't mind helping me if I needed anything, remember? Herr Trent, I need you to come to planet Nortorf in the Munich system as fast as you can!",
        ),
        VoiceLine(
            10,
            Trent,
            ru="Джакобо, Дромадер? Что это за ведро?",
            en="JacoboTrader, a Dormedary? What kind of trash can is that? ",
        ),
        VoiceLine(
            20,
            JacoboTrader,
            ru="Мой корабль засвечен, за ним постоянная слежка, это единственное, что я смог быстро и незаметно купить.",
            en="My ship has been flagged; it's constantly monitored. That's the only thing I could get my hands on unnoticeably.",
        ),
        VoiceLine(
            30,
            Trent,
            ru="Но ты же понимаешь, что если начнется заварушка, он развалится от первого же плевка?",
            en="But you do understand that if things get hot, it'll fall apart very quickly, right? ",
        ),
        VoiceLine(
            40,
            JacoboTrader,
            ru="У меня нет выбора. Хотя вы правы, Герр Трент, документы обязательно должны попасть к заказчику. Сейчас я передам вам копии, откройте канал.",
            en="I have no choice. Although you have a point, Herr Trent. The documents must reach the customer. I'll send you copies, open your channel.",
        ),
        VoiceLine(
            50,
            Trent,
            ru="Передача завершена успешно. Как будем пробиваться в Либерти?",
            en="Transfer complete. Which way are we taking to Liberty?",
        ),
        VoiceLine(
            60,
            JacoboTrader,
            ru="Власти Рейнланда в курсе всех моих действий, мне еле удалось улизнуть когда они за мной пришли, поэтому короткая дорога не для нас. ",
            en="The Rheinland authorities are aware of every move I make. I barely managed to slip away when they came for me, So the short way is not an option.",
        ),
        VoiceLine(
            70,
            JacoboTrader,
            ru="У врат в Хонсю нас скорее всего ждут. Попробуем в обход через территорию Рейналанда. Берем курс на систему Бисмарк.",
            en="They're probably waiting for us at the gate to Honshu. Let's try to make a cut through Rheinland territory. We're setting course to Bismarck.",
        ),
        VoiceLine(
            80,
            Trent,
            ru="Логично. Если тебя разыскивают власти Рейнланда, куда лучше всего лететь? Правильно, в столицу...",
            en="Makes perfect sense. If you're wanted by the Rheinland authorities, what's the best place to go? That's right, the capital...",
        ),
        VoiceLine(
            90,
            JacoboTrader,
            ru="Если есть другие предложения...",
            en="If you have any other suggestions... ",
        ),
        VoiceLine(
            100,
            Trent,
            ru="Нет других предложений, Джакобо, просто мысли вслух.",
            en="No other suggestions, JacoboTrader. Just thinking out loud. ",
        ),
        VoiceLine(
            110,
            Kreitmaier,
            ru="С вами говорит командир спецгруппы Гессенский Лев Маркус Крейтмайер.",
            en="This is commander Marcus Creitmire of the Hessian Lions spec ops unit.",
        ),
        VoiceLine(
            120,
            Kreitmaier,
            ru="Немедленно отключите оружейные системы и следуйте с нами под конвоем. В случае сопротивления у нас есть полномочия вас уничтожить.",
            en="Turn your weapon systems off immediately, and follow our lead. If you try to resist, we have the authority to destroy you.",
        ),
        VoiceLine(
            130,
            Trent,
            ru="Недолго музыка играла... Джакобо, тут без шансов. Маркус, банкуйте, мы сдаемся.",
            en="The fun didn't last long... JacoboTrader, we don't stand a chance. Marcus, you win. We surrender. ",
        ),
        VoiceLine(
            140,
            Kreitmaier,
            ru="Следуйте под нашим конвоем к станции Кёльн.",
            en="We'll escort you to the Cologne station. ",
        ),
        VoiceLine(
            150,
            JacoboTrader,
            ru="Это же главная военная база Рейнланда! Да что мы такого сделали? На каком основании? Какие преступления нам вменяют, в конце концов?",
            en="That's Rheinland's central military base! What did we do to deserve this? What kind of crimes are we being charged with?",
        ),
        VoiceLine(
            160,
            Kreitmaier,
            ru="Вы не в том положении, чтобы задавать вопросы. Следуйте нашим указаниям.",
            en="You're not in a position to ask these questions. Follow our lead.",
        ),
        VoiceLine(
            170,
            Trent,
            ru="Джакобо, угомонись.",
            en="JacoboTrader, calm down. ",
        ),
        VoiceLine(
            180,
            Reichman,
            ru="Герр Крейтмайер, говорит адмирал Р+айхманн. Благодарю вас за успешно выполненное задание.",
            en="Herr Creitmire, this is Admiral Reichmann. Congratulations for completing your task.",
        ),
        VoiceLine(
            190,
            Reichman,
            ru="Доставьте грузовик типа Дромадер на базу для досмотра. Сопровождавший его корабль приказываю уничтожить.",
            en="Take the Dromedary transport to the base for inspection. Your orders are to destroy its convoy. ",
        ),
        VoiceLine(
            200,
            Kreitmaier,
            ru="Уничтожить? Он доставлен под конвоем, адмирал. Как уничтожить?",
            en="Destroy? He's just n escort, admiral. Destroy how?",
        ),
        VoiceLine(
            210,
            Reichman,
            ru="М+олча и быстро. И не пререкаясь со старшими по званию!",
            en="Quickly and silently. And do not argue with your superior officer!",
        ),
        VoiceLine(
            220,
            Hassler,
            ru="Герр Крейтмайер, вас ввели в заблуждение! Заговор! Освободите конвоируемых!",
            en="Herr Creitmeier, you're being misled! Manipulated! Let go of the escort!",
        ),
        VoiceLine(
            230,
            Alaric,
            ru="Слова - это слишком долго. Торпеды быстрее.",
            en="Words – they take too much time. Torpedoes are faster.",
        ),
        VoiceLine(
            240,
            Reichman,
            ru="Боевая тревога! Уничтожить агрессоров!",
            en="Battle alert! Destroy the attackers!",
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
            ru="Спасибо, ребята, теперь валим отсюда!",
            en="Thanks, guys. Now get the hell outta here! ",
        ),
        VoiceLine(
            270,
            Hassler,
            ru="Не так быстро, Трент. Видишь этот линкор поблизости? Стоит нам отлететь от станции - он нас на атомы распылит из своих орудий.",
            en="Not so fast, Trent. You see that battleship there? As soon as we get far enough from the station, it'll turn us into stardust with its guns.",
        ),
        VoiceLine(
            280,
            Hassler,
            ru="А пока мы рядом с Кёльном он стрелять не будет, побоится задеть станцию. Но у меня есть одна идея.",
            en="As long as we're near Cologne, it won't fire because it wouldn't want to hit the station. But I have an idea.",
        ),
        VoiceLine(
            290,
            Hassler,
            ru="Маленький сюрприз от знакомых изгоев. Трент, я уничтожил броневой пояс линкора в районе реактора торпедой. Второй у меня нет. Ты должен нанести урон реактору и пустить его вразнос!",
            en="A little surprise from our Outcast friends. Trent, I've weakened the battleship's armor around the reactor area with my torpedo. I don't have another one. You'll have to damage the reactor to make it blow up! ",
        ),
        VoiceLine(
            300,
            Hassler,
            ru="Этот линкор - Вотан, он идет на ремонт, у них как раз проблемы с системой охлаждения. Постарайся как можно быстрее! Мы с Алариком займемся истребителями!",
            en="The battleship's name is Wotan, it's heading for a repair, their cooling system is damaged. You have to be fast! Alaric and I will take care of the fighters! ",
        ),
        VoiceLine(
            310,
            Hassler,
            ru="А теперь, валим отсюда, как метко выразился герр Трент.",
            en="Now, let's get the hell outta here, as Herr Trent aptly put it. ",
        ),
        VoiceLine(
            320,
            Alaric,
            ru="Включаем круиз.",
            en="Cruise engines online.",
        ),
        VoiceLine(
            330,
            Trent,
            ru="А теперь, объясните мне, пожалуйста, что за хрень вообще происходит? Во что влип Джакобо и я вместе с ним?",
            en="Now, can someone please tell me what the hell is going on? What did JacoboTrader drag us into?",
        ),
        VoiceLine(
            340,
            Hassler,
            ru="Герр Трент, вы оказались не в том месте и не в то время.",
            en="Herr Trent, you appeared in the wrong place, in the wrong time.",
        ),
        VoiceLine(
            350,
            Trent,
            ru="у, с этим у меня как раз порядок, люблю я это дело.",
            en="Oh, I’m just soooo lucky...",
        ),
        VoiceLine(
            360,
            Hassler,
            ru="Герр Трент, если вы помните, финал миссии в Кёнигсберге выглядел со всех сторон сомнительно. И я решил копнуть глубже.",
            en="Herr Trent, remember how our mission in Konigsberg ended? It was suspicious, so I dug deeper into it.",
        ),
        VoiceLine(
            410,
            Hassler,
            ru="Ну так вот, Дитрих в свое время смог выкрасть из генштаба Рейнланда некие очень важные и сверхсекретные документы. Так вот вся операция была затеяна для того чтобы эти документы вернуть.",
            en="Well, it appears he’s stolen some very important top-secret documents from Rheinland’s Joint Staff. So the real goal was to retrieve these documents.",
        ),
        VoiceLine(
            420,
            Hassler,
            ru="И даже если бы Дитрих скрылся, но документы оказались бы в руках Райхманна, операция была бы признана успешной.",
            en="Even if Dietrich escaped, had only the documents fell into Reichmann’s hands, the operation would’ve been considered a success. ",
        ),
        VoiceLine(
            560,
            Hassler,
            ru="Кстати, герр Трент, позвольте поинтересоваться, а чем вы вообще занимались непосредственно перед нашим появлением? Вас конвоировали в сопровождении государственного преступника.",
            en="By the way, Herr Trent, if I may ask: what were you doing right before we arrived? You were escorting a state criminal! ",
        ),
        VoiceLine(
            570,
            JacoboTrader,
            ru="Это все какое-то недоразумение.",
            en="This is all just a big misunderstanding... ",
        ),
        VoiceLine(
            590,
            Trent,
            ru="Джакобо попросил эскортировать его на территорию Либерти. Неплохой парень, мы с ним пересекались по делу когда я работал под юрисдикцией небезызвестного вам герра Вильгельма.",
            en="And to answer your question, JacoboTrader asked me to escort him to Liberty. He’s a nice guy, we crossed paths when I worked for Herr WIlhelm. ",
        ),
        VoiceLine(
            600,
            Hassler,
            ru="Интересно, и зачем же этому неплохому парню понадобился эскорт в Либерти?",
            en="Fascinating. And why did this “nice guy” need to be escorted to Liberty? ",
        ),
        VoiceLine(
            610,
            JacoboTrader,
            ru="Мне нужно срочно доставить важные документы в систему Форбс.",
            en="I urgently need to deliver important documents to the Forbes system. ",
        ),
        VoiceLine(
            620,
            Hassler,
            ru="Важные документы, говорите... В либерти... В любом случае, господа, нам необходимо как можно скорее покинуть территорию Рейнланда. Нельзя слишком долго искушать судьбу.",
            en=" Important documents, you say... To Liberty... Either way, we have to leave Rheinland as soon as possible. One can only be lucky for so long. ",
        ),
        VoiceLine(
            630,
            Hassler,
            ru="Как они нас нашли?",
            en="How did they find us?",
        ),
        VoiceLine(
            9150,
            Alaric,
            ru="Тут целый крейсер, а у меня кончились боеприпасы! Трент, атакуй уязвимые точки крейсера! Мы его и так разнесём!",
            en="There is entire cruiser! My ammo is left, Trent, attack the vulnerable points of the cruiser!",
        ),
        VoiceLine(
            9200,
            Sigma8Cruiser,
            ru="Прекратите сопротивление! Вам не уйти!",
            en="You'll never escape us! Resistance is futile!",
        ),
        VoiceLine(
            640,
            JacoboTrader,
            ru="Помогите! Они сейчас меня сожгут!",
            en="Help! They’re gonna burn me alive!",
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
            en="Motherfuckers!",
        ),
        VoiceLine(
            9300,
            Hassler,
            ru="Скорее уходим.",
            en="Let's get outta here.",
        ),
        VoiceLine(
            670,
            Hassler,
            ru="Очень интересно.",
            en="Very interesting. ",
        ),
        VoiceLine(
            680,
            Trent,
            ru="И что же вас так заинтересовало, герр Хасслер.",
            en="What’s so interesting, Herr Hassler? ",
        ),
        VoiceLine(
            690,
            Hassler,
            ru="Меня заинтересовала странная тактика этого отряда. Они целенаправленно преследовали самый безобидный корабль в нашем отряде, пока мы продолжали бой с ними.",
            en="These fighters’ tactics were odd. They went after the weakest ship in our wing, while we continued fending them off.",
        ),
        VoiceLine(
            700,
            Hassler,
            ru="Было бы логичнее связать боем и уничтожить самый опасный - меня или вас, герр Трент.",
            en="It would make more sense for them to focus on the more serious threats, like you and I, Herr Trent. ",
        ),
        VoiceLine(
            710,
            Trent,
            ru="Значит, они преследовали определенный корабль и то, что на нем находится.",
            en="It means they were only after a certain ship. More specifically, whatever was on that ship. ",
        ),
        VoiceLine(
            720,
            Hassler,
            ru="Вот и я о том же. Документы. Кстати, герр Трент, документов теперь нет? конец истории?",
            en="That’s what I was pointing out. The documents. By the way, (maliciously) Herr Trent, are these documents gone? Is it over? ",
        ),
        VoiceLine(
            730,
            Trent,
            ru="Не совсем. У меня сохранились копии.",
            en="Not quite. I have copies. ",
        ),
        VoiceLine(
            740,
            Hassler,
            ru="Ха-ха-ха, герр Трент, с вами очень приятно и интересно работать. Я не завидую вашим врагам.",
            en="Ha-ha-ha, Herr Trent, I really do enjoy working with you. I certainly wouldn’t want to get on your bad side.",
        ),
        VoiceLine(
            750,
            Alaric,
            ru="А знаете что... Было бы еще интереснее завершить эту миссию. Джакобо убит, но у нас есть координаты заказчика и есть то, что ему нужно. Думаю, это будет не только интересно, но и прибыльно.",
            en="Guys, you know what... Let’s deliver these documents. JacoboTrader’s dead, but we have the buyer’s location and got the goods. I’m just curious to see how it ends, and wouldn’t mind getting paid. ",
        ),
        VoiceLine(
            760,
            Hassler,
            ru="А нам больше и деваться некуда. Герр Трент?",
            en="Well, we’ve got nothing better to do. Herr Trent? ",
        ),
        VoiceLine(
            770,
            Trent,
            ru="слушайте, Хасслер, мне этот ваш герр настолько надоел в Рейнланде... Можно просто Трент? Тем более что мы в Либерти летим?",
            en="Listen here, Hassler. I’m so sick and tired of your Herr, we’re not in Rheinland anymore... Can you just call me Trent? You know, getting into the Liberty vibe and all... ",
        ),
        VoiceLine(
            780,
            Hassler,
            ru="Как скажете, герр Трент.",
            en="As you wish, Herr Trent!",
        ),
        VoiceLine(
            790,
            Trent,
            ru="Не самое подходящее время веселиться. Лучше посоветуйте как в Либерти проще пробраться, мы все-таки еще на территории Рейнланда, где нас, скорее всего уже в государственных преступников записали.",
            en="Enough with the jokes now. Got any idea how we can get to Liberty really fast? We’re still in Rheinland territory, and we’re probably most wanted criminals by now. ",
        ),
        VoiceLine(
            800,
            Hassler,
            ru="Нет ничего проще, летим к аванпосту Аугсбург.",
            en="Piece of cake. Let’s go to the Augsburg outpost.",
        ),
        VoiceLine(
            810,
            Trent,
            ru="Вам Кёльна мало показалось, герр Хасслер?",
            en="Don’t you mean Cologne, Herr Hassler? ",
        ),
        VoiceLine(
            820,
            Hassler,
            ru="Трент, вы помните как мы попали к станции Кёнигсберг в той самой, вызывающей у нас теперь столь устойчивую икоту миссии? И давайте без герров, вы же сами предложили",
            en="Trent, do you remember how we got to Konigsberg, when all this rumble of a journey started? And let’s drop the Herr from now on, you’re the one who asked for it. ",
        ),
        VoiceLine(
            830,
            Trent,
            ru="Через аномалию, которую открыл... Открыл ты, Хасслер, каким-то специальным устройством!",
            en="Through the space anomaly, that... You, Hassler, activated with some special device! ",
        ),
        VoiceLine(
            840,
            Hassler,
            ru="Ну так вот, это устройство все еще на моем корабле, а ближайшая аномалия недалеко от аванпоста Аугсбург.",
            en="So that device is still on my ship, and the nearest anomaly is just by Augsburg. ",
        ),
        VoiceLine(
            850,
            Trent,
            ru="Я понял. Веди.",
            en="Roger that. Lead on. ",
        ),
        VoiceLine(
            900,
            Sigma8Outpost,
            ru="Внимание, вы вошли в зону ответственности аванпоста Аугсбург. Немедленно отключите оружейные системы и проследуйте в зону шлюзов!",
            en="Attention! You’ve entered the Augsburg outpost’s vicinity. Turn off your weapon systems immediately, and proceed to the docking bays! ",
        ),
        VoiceLine(
            910,
            Hassler,
            ru="Не обращайте внимания, у них нет сил, достаточных чтобы перехватить нас. Видите, ни один истребитель не вылетел на перехват. Продолжаем движение.",
            en="Don’t pay attention to them, they’re completely harmless. You see, they didn’t even have any fighters to launch at us. Keep moving.",
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
            en="Augsburg, piss off immediately. I repeat, piss off immediately. ",
        ),
        VoiceLine(
            940,
            Alaric,
            ru="Ха-ха-ха.",
            en="Ha-ha-ha. ",
        ),
        VoiceLine(
            950,
            Hassler,
            ru="Как изысканно...",
            en="How inappropriate... ",
        ),
        VoiceLine(
            860,
            Hassler,
            ru="Предупреждаю вас, друзья мои, аномалия ведет куда-то на территорию Либерти, куда конкретно, я не знаю, поэтому вам придется в первое время вспомнить все навыки ориентирования на местности.",
            en="But let me give you guys a warning  first: the anomaly leads to Liberty, but I’m clueless as to where exactly in Liberty. So be ready for anything, just in case. ",
        ),
        VoiceLine(
            870,
            Alaric,
            ru="В смысле вам? Ты с нами не летишь?",
            en="What do you mean by you guys? Aren’t you flying with us? ",
        ),
        VoiceLine(
            875,
            Hassler,
            ru="Нет, мне гораздо комфортнее будет залечь на дно на периферии Рейнланда, чем лететь на территорию стратегического союзника, где меня обязательно выпотрошат на предмет всех знаний которыми я обладаю как бывший офицер спецслужб. Нет, увольте.",
            en="No. I’m better off sinking to the bottom here in Rheinland’s periphery, rather than flying straight into the hands of a strategic ally. I’d end up being gutted for the knowledge I possess, as a former intelligence officer. So, no thanks. ",
        ),
        VoiceLine(
            880,
            Trent,
            ru="Но тебя же разыскивают власти.",
            en="But the authorities will find you... ",
        ),
        VoiceLine(
            890,
            Hassler,
            ru="Наши власти много кого разыскивают, но далеко не всех находят, поверьте мне, с моими связями и навыками мне будет гораздо безопаснее на территории Рейнланда, чем на территории Либерти.",
            en="Our authorities are looking for a lot of people, but not all that’s lost can be found. Trust me, with my connections and skills I’ll be much safer in Rheinland than anywhere else. ",
        ),
        VoiceLine(
            960,
            Hassler,
            ru="А вот и аномалия. Активирую...",
            en="And there’s the anomaly. Activating... ",
        ),
        VoiceLine(
            970,
            Alaric,
            ru="Черт, корсары!",
            en="Shit, Corsairs! ",
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
            ru="Надеюсь, на этот раз нам не помешают. Активирую аномалию...",
            en="No one’s going to disrupt us now, I hope. Activating the anomaly...",
        ),
        VoiceLine(
            995,
            Hassler,
            ru="Есть! Быстрее, друзья!",
            en="Yes! Faster, guys! ",
        ),
        VoiceLine(
            1000,
            Alaric,
            ru="Спасибо за все, Хасслер, удачи!",
            en="Thank you, Hassler, for everything. And good luck!",
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
            en="I don’t know about it. You’re a lot of trouble, Trent. But, nevertheless, I bid you farewell! ",
        ),
        VoiceLine(
            1030,
            Alaric,
            ru="Уф, проскочили. Трент, а где мы?",
            en="Oof, we slipped right through. Where are we, Trent?",
        ),
        VoiceLine(
            1040,
            Trent,
            ru="Ты будешь удивлен, но, по-видимому, где-то в системе Форбс. После прохода аномалии навигационная система с ума сходит, надо дать ей время прийти в себя.",
            en="You won’t believe it, we’re in the Forbes system. The anomaly really messes your sensors up, you need to give them time to recover. ",
        ),
        VoiceLine(
            1050,
            Trent,
            ru="А пока... Поблизости есть верфь Филадельфия, полетели на неё.",
            en="In the meantime... Ah! I see the Philadelphia shipyard. Let’s go there. ",
        ),
        VoiceLine(
            1060,
            Alaric,
            ru="Вперед!",
            en="Onwards!",
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
            en="That’s right. ",
        ),
        VoiceLine(
            1090,
            HatcherStation,
            ru="Мы ждали вас и... это не мистер Джакобо!",
            en="We were waiting for you, and... Wait, that’s not Mr. JacoboTrader!  ",
        ),
        VoiceLine(
            1100,
            Trent,
            ru="Правильно, это не мистер Джакобо. Мистер Джакобо погиб, когда нас прижали Рейнландские военные. ",
            en="That’s right, it’s not Mr. JacoboTrader. Mr. JacoboTrader died when we got attacked by Rheinland’s military.",
        ),
        VoiceLine(
            1110,
            Trent,
            ru="Однако, копия того что он вез, у меня на борту. Вам все еще интересны эти документы?",
            en="However, a copy of his precious cargo is onboard my ship. Are you still interested in these documents? ",
        ),
        VoiceLine(
            1120,
            HatcherStation,
            ru="Да! Безусловно интересны!",
            en="Yes! Very interested!",
        ),
        VoiceLine(
            1130,
            Trent,
            ru="Я готов их вам передать. Кстати, с кем имею честь?",
            en="And I’ll gladly hand them over to you. By the way, to whom do I owe the honor? ",
        ),
        VoiceLine(
            1140,
            HatcherStation,
            ru="Можете звать меня Хетчер, мистер Трент. Мы доверяем вам, мистер Трент. Для обмена проследуйте, пожалуйста, на планету Форбс. Встретимся в баре.",
            en="You can call me Hatcher, Mr. Trent. We trust you, Mr. Trent. We’ll make the exchange on planet Forbes, please follow us there. Meet me at the bar.",
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

    MISSION_TITLE = 'Миссия 4. Сопровождение Джакобо'
