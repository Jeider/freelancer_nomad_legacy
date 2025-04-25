from story import script
from audio.sound import VoiceLine
from story.actors import (
    Trent, Hatcher, HatcherStation, Tilton, DetroitDispatcher, AlaricStation, ForbesSmugglerOne, ForbesSmugglerTwo,
    Sigma17Trader, Sigma17Police, ClarkResearch, Mandrake, Sigma17Assassin
)


class Msn5(object):
    MISSION_INDEX = 5


class Msn5Space(Msn5, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(
            0,
            HatcherStation,
            ru="Мистер Трент, если вы все еще заинтересованы в высокооплачиваемой работе, встретимся в баре космопорта планеты Форбс. Хетчер.",
            en="Mr. Trent, if you're still interested in a high-income job, meet me at the bar on planet Forbes. Hatcher out.",
        ),
        VoiceLine(
            5,
            Trent,
            ru="Станция Детроит, это фрилансер Альфа-один, запрашиваю стыковку.",
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
        ),
        VoiceLine(
            110,
            ForbesSmugglerOne,
            ru="Ох, ёптыть, это еще что тут такое? ",
            en="Hey, what the hell was that? ",
        ),
        VoiceLine(
            120,
            ForbesSmugglerTwo,
            ru="Мил человек, ты откуда здесь такой нарисовался некрасивый? Заблудился что-ль? ",
            en="Hey stranger! You don't look like you belong here. Did you lose something? ",
        ),
        VoiceLine(
            130,
            Trent,
            ru="Мне тут некий мистер Смит намекнул, что у вас пропуск можно получить на Детройт по сходной цене. ",
            en="A little bird named Mr. Smith told me that I can get a Detroit security pass for a reasonable price here. ",
        ),
        VoiceLine(
            150,
            ForbesSmugglerTwo,
            ru="Твою же... Я сегодня же прикончу этого долбаного торчка. Все мозги себе скурил. ",
            en="That stupid… I'm gonna finish that stoner off right now! He smoked his last blunt.",
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
            en="Мисс Хетчер, приглашаю вас в романтическое путешествие до системы Сигма-17. ",
        ),
        VoiceLine(
            310,
            Trent,
            ru="Там правда нужно будет еще станцию какую-то найти. Ис-сле-до-ва-тель-ску-ю. Но, думаю, мы справимся. ",
            en="Miss Hatcher, would you like to go with me on a romantic getaway to Sigma-17? We'll have to find some station though. A r-e-s-e-a-r-c-h station. But I think we can handle it. ",
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
            ru="SOS! Всем кто рядом! Это торговец омега - девять. Подвергаюсь нападению пиратов! Срочно нужна помощь! Кларк, помогите! ",
            en="Mayday! To all ships in the vicinity! This is freighter convoy omega-nine. We are under attack by pirates! We require immediate assistance! Clark, please send someone!",
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
            ru="Трент, нам нужно спасти Мандрейка! Многие капсулы повреждены! Ищи Мандрейка! ",
            en="Trent, we have to save Mandrake! Most of the escape pods are damaged, look for Mandrake! ",
        ),
        VoiceLine(
            610,
            Trent,
            ru="Хетчер, а другим ты помочь не хочешь.",
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
        ),
        VoiceLine(
            730,
            Trent,
            ru="Да что за... Я просто летел к вратам в Форбс, в чем дело? ",
            en="What the... I was just flying to Forbes, what's the matter? ",
        ),
        VoiceLine(
            740,
            Sigma17Police,
            ru="Фриленсер альфа-один, повторяю, заблокируйте орудийные системы и проследуйте с нами до линкора Грифон. Приказ коммандера Тилтона. В случае сопротивления открываем огонь на поражение. ",
            en="Freelancer alpha-one, I repeat, turn your weapons down and follow us to battleship Griffin. That's an order from commander Tilton. If you fail to comply, we will open fire. ",
        ),
        VoiceLine(
            750,
            Hatcher,
            ru="Салют, мальчики! Он под моей юрисдикцией, расслабьтесь. Это наш человек, ясно вам?! ",
            en="Hey there, boys! This freelancer is under my jurisdiction. Calm down. He's on our side. Is that clear?",
        ),
        VoiceLine(
            760,
            Tilton,
            ru="Этот фрилансер обвиняется ни много ни мало в уничтожении научной станции Кларк! И я имею полномочия делать с ним все, что захочу! ",
            en="This freelancer is responsible for no less than the destruction of the Clark research station! And I have the authority, by all means, to deal with him as I please!",
        ),
        VoiceLine(
            770,
            Tilton,
            ru="Да я-то здесь причем? Станцию изнутри взорвали, я в это время вообще снаружи был, ожидал... ",
            en="I'm responsible for WHAT? The station blew up from the inside, while I was out in space waiting for...",
        ),
        VoiceLine(
            780,
            Trent,
            ru="Замолчи, Трент ",
            en="Shut up, Trent!",
        ),
        VoiceLine(
            790,
            Hatcher,
            ru="Заткнись, фрилансер",
            en="Shut up, freelancer! ",
        ),
        VoiceLine(
            810,
            Sigma17Police,
            ru="Внимание, враждебные контакты на радаре!",
            en="Attention, we're reading hostiles on our radar!",
        ),
        VoiceLine(
            820,
            Sigma17Assassin,
            ru="Какая встреча, герр Трент! А вы знаете, что полагается по законам Рейнланда за государственную измену? Правильно, смертная казнь! Звено, к бою! ",
            en="What a coincidence, Herr Trent! Do you know what's the penalty for treason in Rheinland? That's right, death! All wingmen, engage!",
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
    CUTSCENES = []
    SPACE_CLASS = Msn5Space
    SYNC_SPACE = False

    MISSION_TITLE = 'Миссия 5. Поиск учёного'
