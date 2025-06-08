from story import script
from audio.sound import VoiceLine
from story.actors import (
    Trent, Wilham, Jacobo, Punisher, PunisherCatcher, OmegaJunkerOne, OmegaJunkerTwo, OmegaJunkerThree, Neuralnet
)


class Msn2(object):
    MISSION_INDEX = 2


class Msn2Space(Msn2, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(
            30,
            Trent,
            ru="А зачем вам вообще фриленсеры? Вооруженные силы Рейнланда вполне способны сами решить любую проблему. Оцепили сектор, нашли обломки, изъяли данные...",
            en="Why do you need freelancers? The Rheinland military is fully capable of solving any problem of such. Search the sector, find the wreckage, download the data...",
        ),
        VoiceLine(
            40,
            Wilham,
            ru="Тем самым дезавуировали своего бывшего агента, выставили на всеобщее обозрение все свои интересы. ",
            en="That's exactly how we lost our former agent, exposing our interests to the public eye.",
        ),
        VoiceLine(
            45,
            Wilham,
            ru="Не говоря уже о том, что интересующая нас область находится вне юрисдикции Рейнланда. И кто согласился бы с нами работать после того, как мы устроили подобный цирк?",
            en="Not mentioning the fact that our area of interest is located outside of Rheinland's jurisdiction. And who'd ever agree to work with us, after all this circus?",
        ),
        VoiceLine(
            50,
            Wilham,
            ru="Работать с агентами не напрямую, а через сторонних лиц и независимые организации - это мудрость, идущая из глубины веков. Мы можем играть в игру, герр Трент, или не играть.",
            en="Working with agents indirectly, but rather through third-parties and independent organizations, is an age-old best practice. We can either play the game, Herr Trent, or not.",
        ),
        VoiceLine(
            55,
            Wilham,
            ru="Единственное что мы ОБЯЗАНЫ делать - это соблюдать правила. Кстати, одно из правил, герр Трент. Если вдруг с вами произойдет что-то неприятное, то мое ведомство ничего о вас не знает, а вы, в свою очередь, ничего не знаете о нём.",
            en="The only thing we absolutely MUST do – is follow the rules. By the way, that's one of the rules, Herr Trent: If something unpleasant happens to you, then my department knows nothing about you, and in turn, you know nothing about it.",
        ),
        VoiceLine(
            60,
            Trent,
            ru="Ясно все с вами, работники ножа и топора, ох, извините, плаща и кинжала.",
            en="It's all clear with you, workers of the knife and axe. Oh, sorry, of cloak and dagger.",
        ),
        VoiceLine(
            70,
            Wilham,
            ru="Герр Трент, мы приближаемся к общине местных шахтеров, они добывают редкие металлы на астероидах. Интересующий нас человек находится на добывающем судне Матильда. Позывной - Джакобо.",
            en="Herr Trent, we're approaching a local miners community. They mine rare metals on asteroids. The person of our interest is aboard the mining ship named Matilda. Callsign - Jacobo.",
        ),
        VoiceLine(
            75,
            Wilham,
            ru="Просто передайте ему, что вы от Вильгельма. Мне светиться в этом секторе нельзя, тем более на этом корабле, поэтому я на время сойду со сцены.",
            en="Just tell him Wilhelm sent you. I must not stand out in this area, especially with this ship, so I'll leave the stage for now.",
        ),
        VoiceLine(
            1030,
            Jacobo,
            ru="Я переслал вам координаты ближайшего разбившегося корабля. Постарайтесь быстрее их осмотреть, у  нас не так много времени. ",
            en="I've sent you the coordinates of the nearest crashed ship. Try to scan them as fast as you can, we don't have much time.",
        ),
        VoiceLine(
            100,
            Trent,
            ru="Джакобо, а почему здесь так мусорщиков боятся? Собирают себе мусор - и пусть собирают, полезное дело делают.",
            en="Jacobo, why's everyone so scared of Junkers around here? They're collecting garbage – so let them do their good work for the community.",
        ),
        VoiceLine(
            110,
            Jacobo,
            ru="Бесконечно далеки вы от народа, мальчики из центральных систем. Изначально мусорщики занимались сбором мусора, сортировкой и продажей разных категорий отходов.",
            en="You central system boys are infinitely far from civilization. At first, the Junkers were engaged in garbage collection, sorting and selling different categories of junk.",
        ),
        VoiceLine(
            112,
            Jacobo,
            ru="И это было настолько прибыльно, что ряды мусорщиков в свое время росли не по дням а по часам. ",
            en="And it was so profitable, that Junker units were multiplying not by the day, but by the hour.",
        ),
        VoiceLine(
            115,
            Jacobo,
            ru="Сейчас, например, они могут начать рассматривать в качестве мусора любой звездолет случайно попавший в их зону влияния и не имеющий должной охраны. Разберут его на составляющие и продадут в виде вторсырья.",
            en="Now, for example, their definition of junk could include any spaceship making its way through their area of influence without proper escort. They'll tear it down to pieces and sell it in form of recycled components.",
        ),
        VoiceLine(
            120,
            Jacobo,
            ru="Подошли к первой точке вероятного крушения.",
            en="We've reached the first potential crash site.",
        ),
        VoiceLine(
            130,
            Trent,
            ru="Начинаю сканировать...",
            en="Commencing a scan...",
        ),
        VoiceLine(
            140,
            Trent,
            ru="Нет, не то.",
            en="Nope, not it.",
        ),
        VoiceLine(
            150,
            Jacobo,
            ru="Есть еще две точки с координатами разбившихся кораблей, которые могут стать интересующими нас объектами...",
            en="There are two more points with crash site coordinates, which could contain our object of interest...",
        ),
        VoiceLine(
            155,
            Jacobo,
            ru="Что за помехи? Что за помехи на радаре???",
            en="What's that? What's with the radar interference???",
        ),
        VoiceLine(
            160,
            Trent,
            ru="Я полагаю, эти пять..., нет,  семь... девять... враждебных кораблей создают нам помехи. ",
            en="I think there are five… No, seven… Nine… Hostile ships on an interception course.",
        ),
        VoiceLine(
            170,
            OmegaJunkerOne,
            ru="О! А шо это шевелится на нашей территории?",
            en="Oh! What's that, fiddling in our territory?",
        ),
        VoiceLine(
            180,
            OmegaJunkerTwo,
            ru="Металлолом какой-то...",
            en="Some kind of scrap metal...",
        ),
        VoiceLine(
            190,
            OmegaJunkerThree,
            ru="Ну вот, опять сортировать мусор.",
            en="Here we go again, sorting junk.",
        ),
        VoiceLine(
            200,
            OmegaJunkerOne,
            ru="Да шо вы переживаете, там дел-то на пять минут.",
            en="Don't worry, it'll only take five minutes.",
        ),
        VoiceLine(
            210,
            Jacobo,
            ru="Трент - возможно это тот корабль, который вы искали, сканируйте.",
            en="Trent – this could be the chip you're looking for. Scan it.",
        ),
        VoiceLine(
            230,
            Trent,
            ru="Бинго! Тот самый корабль. Считываю данные с бортового журнала...",
            en="Bingo! That's out ship.",
        ),
        VoiceLine(
            240,
            Trent,
            ru="Все. Можем возвращаться. ",
            en="Done. We can go back now.",
        ),
        VoiceLine(
            250,
            Jacobo,
            ru="Трент, ты же наёмник? А наемник работает в принципе на любого, кто платит за услуги?",
            en="Trent, you're a freelancer right? And technically, freelancers work for anyone who pays.",
        ),
        VoiceLine(
            260,
            Trent,
            ru="Не на любого, но в принципе, да, это мой хлеб.",
            en="Not anyone, but technically, yeah. That's my bread.",
        ),
        VoiceLine(
            270,
            Jacobo,
            ru="А сможешь поработать на меня, если придется?",
            en="Would you work for me, if I ever need anything?",
        ),
        VoiceLine(
            280,
            Trent,
            ru="Конечно!",
            en="Of course!",
        ),
        VoiceLine(
            290,
            Jacobo,
            ru="Тогда я обсужу это со знакомыми шахтерами. И если ты не против, мы хотели бы нанять тебя.",
            en="Then I'll discuss that with some miner friends of mine, and if you don't mind, we'd like to hire you.",
        ),
        VoiceLine(
            300,
            Trent,
            ru="Да не вопрос.",
            en="It'll be my pleasure.",
        ),
        VoiceLine(
            310,
            Wilham,
            ru="герр Трент, встречаемся у гиперврат в систему Бисмарк.",
            en="Herr Trent, meet me at the jump gate to Bismarck.",
        ),
        VoiceLine(
            320,
            Wilham,
            ru="Мы рады, что вы смогли выполнить миссию. Пожалуйста, передайте данные Карателю 1.",
            en="We're glad that you could make it through the mission. Please, transfer the data to Punisher 1.",
        ),
        VoiceLine(
            330,
            Trent,
            ru="Вильгельм, НАПАРНИК, а ты не мог помочь мне в бою с мусорщиками когда я получал эти ваши сверхсекретные данные?",
            en="Wilhelm, my PARTNER, could you really not help me fight off the Junkers when I collected your top secret data?",
        ),
        VoiceLine(
            340,
            Wilham,
            ru="Нет, это выходило за рамки моей компетенции.",
            en="No, it was beyond my level of expertise.",
        ),
        VoiceLine(
            350,
            Punisher,
            ru="Внимание, это каратель - 1! Нами обнаружен нелегальный склад оружия, находящийся в облаке Майсен.",
            en=", this is Punisher-1! We've discovered an illegal weapon storage facility, located in the Maison cloud.",
        ),
        VoiceLine(
            360,
            Wilham,
            ru="Передавайте координаты! Трент, не хочешь поучаствовать в операции федерального масштаба? ",
            en="Send us coordinates! Trent, would you like to participate in a federal-scale operation?",
        ),
        VoiceLine(
            370,
            Trent,
            ru="А у меня есть выбор?",
            en="Do I have a choice?",
        ),
        VoiceLine(
            380,
            Wilham,
            ru="Ха-ха-ха! Нет!",
            en="Ha-ha-ha! No!",
        ),
        VoiceLine(
            390,
            Trent,
            ru="Тогда, пожалуй, поучаствую!",
            en="Then I'd very much like to!",
        ),
        VoiceLine(
            1050,
            Punisher,
            ru="Склад обнаружен. Вижу противника!",
            en="Storage facility located. Bogies inbound!",
        ),
        VoiceLine(
            1060,
            Wilham,
            ru="Каратель-4, на вас грузовики. Остановите их! Остальным – уничтожать истребители.",
            en="Punisher-4, the transports are heading your way. Stop them! Everyone else – destroy the fighters.",
        ),
        VoiceLine(
            1070,
            PunisherCatcher,
            ru="Вас понял, выполняю.",
            en="Roger that, on my way.",
        ),
        VoiceLine(
            410,
            Wilham,
            ru="Каратель- 4, что там с грузовиками?",
            en="Punisher-4, what about the transports?",
        ),
        VoiceLine(
            420,
            PunisherCatcher,
            ru="Грузовики продолжают движение. Нет, стоп, грузовики остановились! Грузовики остановились!",
            en="The transports are on the move. No, wait, they've stopped! The transports have stopped!",
        ),
        VoiceLine(
            430,
            PunisherCatcher,
            ru="База! Вижу базу!",
            en="A base! I see a base!",
        ),
        VoiceLine(
            440,
            Wilham,
            ru="Каратели, входим в зону действия!",
            en="Punishers, let's get moving!",
        ),
        VoiceLine(
            450,
            Wilham,
            ru="Трент!!! Приказ оказывать поддержку звену Карателей! Атакуй оружейные платформы!!!",
            en="Trent!!! Your order is to assist the Punisher wing!Attack the weapon platforms!!!",
        ),
        VoiceLine(
            1080,
            Wilham,
            ru="Отлично, герр Трент, осталась еще одна.",
            en="Excellent, Herr Trent, only one left.",
        ),
        VoiceLine(
            1090,
            Wilham,
            ru="Каратель-1, мы готовы к ликвидации базы?",
            en="Punisher-1, are we ready to liquidate the base?",
        ),
        VoiceLine(
            1100,
            Punisher,
            ru="Никак нет. Здесь слишком много кораблей противника.",
            en="Not yet. There are too many enemy ships.",
        ),
        VoiceLine(
            1110,
            Wilham,
            ru="Вас понял. Трент, разберитесь с оставшимися корсарами.",
            en="Roger that. Trent, you take care of the rest of them.",
        ),
        VoiceLine(
            1120,
            Punisher,
            ru="Сектор чист, торпеды готовы к запуску!",
            en="Area clear, torpedoes ready to launch!",
        ),
        VoiceLine(
            1130,
            Wilham,
            ru="Объект уничтожен, миссия выполнена. Каратели, оцепите район и изучите останки базы. Герр Трент, следуйте на Шарнхорст.",
            en="Objective destroyed, mission accomplished. Punishers, scout the area and inspect the base's debris. Herr Trent, follow me to Scharnhorst.",
        ),
        VoiceLine(
            460,
            Wilham,
            ru="Мне только что передали, герр Трент, что с вами хочет пообщаться один из адмиралов Рейнланда.",
            en="I just received the message, Herr Trent, that one of Rheinland's admirals would like to talk to you.",
        ),
        VoiceLine(
            470,
            Trent,
            ru="И много у вас адмиралов?",
            en="Do you have lots of admirals?",
        ),
        VoiceLine(
            480,
            Wilham,
            ru="По пальцам одной руки можно пересчитать. Тебе оказали большую честь.",
            en="You can count them with one hand. You're being greatly honored.",
        ),
        VoiceLine(
            490,
            Trent,
            ru="Охренеть. Будет что вспомнить в старости.",
            en="Will I live… That's something to remember when I'm old.",
        ),
        VoiceLine(
            1140,
            Wilham,
            ru="Герр Трент, вы первый.",
            en="Herr Trent, you go first.",
        ),
        VoiceLine(
            7000,
            Neuralnet,
            ru="Чтобы получ+ить д+оступ на рудок+оп, вы должн+ы доб+ыть кл+юч. Кл+юч м+ожно доб+ыть в астер+оидах. Атак+уйте вн+утренние п+олости ближ+айших астер+оидов сво+ими п+ушками.",
        ),
        VoiceLine(
            7010,
            Neuralnet,
            ru="+Если п+олость астер+оида разр+ушилась с зел+ёным взр+ывом, зн+ачит с астер+оида м+ожно доб+ыть кл+юч.",
        ),
        VoiceLine(
            7020,
            Neuralnet,
            ru="Уничтошьте все п+олости +этого астер+оида до тех пор, пока ключ не в+ыпадет. Д+оступ к ст+анции б+удет откр+ыт ср+азу же, как т+олько вы забер+ёте ключ в свой трюм.",
        ),
        VoiceLine(
            7030,
            Neuralnet,
            ru="Если п+олость астер+оида была разрушена с б+елым взр+ывом, то на этом астер+оиде не б+удет ключ+а. Вы должн+ы будете направиться к сл+едующему астер+оиду и попр+обовать сн+ова.",
        ),
        VoiceLine(
            7040,
            Neuralnet,
            ru="В Секторе Сириуса различные станции нужно взламывать различными способами. "
               "Чтобы получить информацию о методике взлома обратитесь к инфокарте взламываемого объекта.",
        ),
    ]


class Mission2(Msn2, script.StoryMission):
    MISSION_INDEX = 2
    CUTSCENES = []
    SPACE_CLASS = Msn2Space
    SYNC_SPACE = True

    MISSION_TITLE = 'Миссия 2. Мусорная работа'
