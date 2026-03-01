from story import script
from audio.sound import VoiceLine
from story.actors import (
    Trent, Darcy, CorsairBarman, Rockford, Tortuga, JabbaBandit, RockfordStation,
    CadizEnemyOne, CadizEnemyTwo, CadizEnemyThree, CadizEnemyFour, WalesBarman, Jabba
)


class Msn7(object):
    MISSION_INDEX = 7


class Msn7Offer(Msn7, script.CutsceneProps):
    ALIAS = 'offer'
    TITLE = 'Предложение'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, CorsairBarman, ru="Чего налить?", en="Something to drink?"),
        VoiceLine(20, Trent, ru="Дельца какого-нибудь, желательно с хорошей оплатой.", en="Liberty ale. Got anything for a pro out for big bucks?"),
        VoiceLine(30, CorsairBarman, ru="Да у нас тут вроде и в своих фрилансерах недостатка нет, понимаете же в какой системе находитесь.", en="Yeah buddy? Look around you... look like there's big bucks here?"),
        VoiceLine(40, Trent, ru="А я… скидку хорошую сделаю! Выручай дружище, я совсем на мели.", en="In that case... got anything for a dead broke freelancer, will work for peanuts..."),
        VoiceLine(50, CorsairBarman, ru="Окей, мистер...", en="Alright, Peanut..."),
        VoiceLine(60, Trent, ru="", en="Mr Trent."),
        VoiceLine(70, CorsairBarman, ru="Трент.", en="Sure. Mr Peanut. I might have something for you if you're up for it."),
        VoiceLine(80, CorsairBarman, ru="Окей, мистер Трент. Будет для вас дельце.", en="Some of Liberty parasites recently took root in our turf. Shiny new ships, slick dressers. They call themselves Starline Express."),
        VoiceLine(90, CorsairBarman, ru="К нам тут гастролеры пожаловали из Либерти. Называют себя бандой Старлайна.", en="Your task is to take out their leader, Bill Ironside. They're flashy but no pushovers. Interested?"),
        VoiceLine(100, CorsairBarman, ru="Найдите их и убейте Билла Айронсайда - их лидера. Координаты их предположительного местонахождения я вам скину. ", en="But as discussed, peanuts."),
        VoiceLine(110, Trent, ru="Но учтите, гонорар будет ниже, чем обычно...", en="I'll take whatever I can get. Send me the brief."),
    ]


class Msn7Cadiz(Msn7, script.CutsceneProps):
    ALIAS = 'cadiz'
    TITLE = 'Кадиз'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, CadizEnemyOne, ru="Здаров, земляк! Где Рокфорд?", en="Hey, bro, know where Rockford's at?"),
        VoiceLine(20, Trent, ru="Понятия не имею.", en="None of your bees wax."),
        VoiceLine(30, CadizEnemyTwo, ru="Слыш, земеля, ты чо такой дерзкий? Тебя по-хорошему спросили нна, где Рокфорд?", en="Smart mouth, eh, shithead? Best answer before we make you."),
        VoiceLine(40, CadizEnemyThree, ru="Сейчас наладим диалог.", en="This'll make you talk."),
        VoiceLine(50, CadizEnemyFour, ru="Где Рокфорд, утырок?", en="Where's Rockford, you prick?"),
        VoiceLine(60, Rockford, ru="Я Рокфорд. ", en="Here. I'm Rockford"),
        VoiceLine(65, Rockford, ru="За мной! Быстро!", en="Follow me. Immediately!"),
    ]


class Msn7Omega13(Msn7, script.CutsceneProps):
    ALIAS = 'omega13'
    TITLE = 'Омега-13'
    DESCRIPTION = ''
    VOICE_LINES = [
        # duplicated for different fx
        VoiceLine(10, Trent, ru="Чёрт, Рокфорд, я обездвижен!", en="Dammit Rockford, I'm immobilized!"),
        VoiceLine(15, Trent, ru="Чёрт, Рокфорд, я обездвижен!", en="Dammit Rockford, I'm immobilized!"),

        VoiceLine(20, Rockford, ru="Я знаю.", en="I know."),

        VoiceLine(30, Trent, ru="Рокфорд, что происходит? Ты же агент СБА, ты должен мне помочь", en="Rockford, what's going on? You ASF!"),
        VoiceLine(35, Trent, ru="Рокфорд, что происходит? Ты же агент СБА, ты должен мне помочь", en="Rockford, what's going on? You ASF!"),

        VoiceLine(40, Rockford, ru="Я не агент СБА.", en="How guillible you are, Mr Trent."),

        VoiceLine(50, Trent, ru="Ты же уничтожишь артефакты.", en="If I go down, I'm taking the artifacts with me!"),
        VoiceLine(55, Trent, ru="Ты же уничтожишь артефакты.", en="If I go down, I'm taking the artifacts with me!"),

        VoiceLine(60, Rockford, ru="Артефакты переживут уничтожение корабля.", en="Ah poor Trent. Those artifacts are night indestructible. They will survive you."),


        VoiceLine(100, Trent, ru="Да за-пус-тись же ты, ста-ро-е ко-ры-то.", en="Ahcrap. Come-on you old rust bucket. Don't fail me now!"),
    ]


class Msn7Battleship(Msn7, script.CutsceneProps):
    ALIAS = 'battleship'
    TITLE = 'Линкор Принц Уэльский'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Trent, ru="Мне нужна помощь! Дело государственной важности!", en="I need help! It's a matter of national security!"),
        VoiceLine(20, WalesBarman, ru="Хе... Прям-таки государственной. Тогда вам к представителю государства.", en="Oh really? If so, then you should ask seek advice from a representative of the State."),
        VoiceLine(30, WalesBarman, ru="Вон там у нас офицер Дерси сидит, единственная и неповторимая.", en="Over there we have officer Darcy. Representative of the State. Best there is."),
        VoiceLine(40, Trent, ru="Меня зовут Трент. Я работаю на секретную организацию, связанную с Орденом и мне срочно нужно с ней связаться.", en="Hi, Officer Darcy. My name is Trent. I'm working for a secret organisation tied to Order, and I need to contact them ASAP."),
        VoiceLine(50, Darcy, ru="Еще один... Мистер, а вы в курсе, что торговля артефактами инопланетного происхождения является незаконной?", en="Another loser... Sir, you must know that smuggling alien artifacts is illegal..."),
        VoiceLine(60, Darcy, ru="Мы недавно взяли парочку вот таких вот продавцов. Когда сажали их в камеру, они тоже уверяли что являются агентами Ордена.", en="We caught a pair of your buddies recently. Claiming to be Order agents too, locked 'em up good."),
        VoiceLine(70, Darcy, ru="Не хотите ли составить им компанию или, быть может, их другу герцогу Веллингтону в психушке?", en="Guess you'll be wanting to join them... or perhaps, that other guy, Napoleon in a mental asylum. "),
        VoiceLine(80, Trent, ru="Я хочу доставить артефакт особой важности в штаб-квартиру нашей организации как можно быстрее. ", en="Look I'm not kidding. I need to deliver an artifact of utmost importance to Order HQ as soon as possible."),
        VoiceLine(90, Trent, ru="Иначе с меня шкуру спустят, а потом, возможно, и с вас. Кстати, об артефактах.", en="Or else I'll be executed, and anyone who's associated with me... that includes you."),
        VoiceLine(100, Darcy, ru="О как... Впечатляет.", en="Oh, wow... That's different. Let's have a look at it."),
        VoiceLine(110, Darcy, ru="А откуда мне знать что эта штука не из какой-нибудь сувенирной лавки для туристов?", en="How am I supposed to know this isn't some souvenir for tourists?"),
        VoiceLine(120, Trent, ru="Черт побери...", en="Goddamn it... I'm telling you..."),
        VoiceLine(130, Darcy, ru="Ладно, есть у меня знакомый специалист по разным редкостям на соседней станции.", en="Okay don't get your knickers in a twist. I have a friend who's a collector and expert on antiquities."),
        VoiceLine(140, Darcy, ru="Пусть он взглянет на эту штуку и если вы правы, то я обещаю вам всяческую поддержку.", en="Let's go on a field trip and see if he backs you. If he does, I'll help you in any way I can."),
        VoiceLine(150, Darcy, ru="Если же это все-таки сувенир, то у вас, мистер шутник, сегодня вечером будет назначено чаепитие с тем самым герцогом Веллингтоном в психушке!", en="But if it's a fake... Napolean could do with some company. He's partial to handsome yougn men."),
        VoiceLine(160, Trent, ru="Есть проблема. У меня на корабле сгорела почти вся электроника, даже и не знаю как смог сюда добраться живым.", en="Err. Okay. By the way, I have a small problem with my ship... It's pretty much fried. It's a miracle I made it here at all."),
        VoiceLine(170, Darcy, ru="Хорошо, я дам вам один из наших кораблей.", en="All right, you can use one of our ships."),
        VoiceLine(180, Darcy, ru="Но если захотите на нем смыться, имейте ввиду, что все наши корабли оборудованы маячками слежения, так что я вас найду где угодно. ", en="But if you decide to run off with it... think twice. All our ships are equipped with trackers. You can run, but you can't hide."),
    ]


class Msn7CheckArtifact(Msn7, script.CutsceneProps):
    ALIAS = 'check_artifact'
    TITLE = 'Проверка артефакта'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Trent, ru="Ничего себе. Похоже, у этого парня очень разносторонние интересы.", en="Wow, talk about eclectic taste."),
        VoiceLine(20, Jabba, ru="Я интересуюсь редкими вещами, которые можно выгодно купить и еще более выгодно продать.", en="Rare trinkets generate huge profits from buyers with unusual tastes, Mr Linguist."),
        VoiceLine(30, Jabba, ru="Привет, Дерси.", en="Ms Darcy. You look well."),
        VoiceLine(40, Darcy, ru="Привет Джабба. Я хочу, чтобы ты взглянул на одну вещицу.", en="Hi, Jabba. I need you to check something for me."),
        VoiceLine(50, Jabba, ru="Ух ты! Весьма интересная вещица, явно инопланетного происхождения. ", en="Hmm. Yes.. this... is evidently of alien origin."),
        VoiceLine(60, Jabba, ru="Если вы, вдруг, на мели готов дать вам за нее десять тысяч прямо сейчас.", en="I'll pay you ten thosands credits for it right now, Mr Linguist."),
        VoiceLine(70, Darcy, ru="Вот дерьмо... Попила пивка в баре, нечего сказать. Ладно, Трент, уходим.", en="Oh... wow... So much for the Barman's \"fake as fake can be, drinks on me\". Okay, Trent, we're outta here."),
        VoiceLine(80, Darcy, ru="Джабба, ты же не дурак да? Ты же будешь держать язык за зубами?", en="Jabba, Not a peep to anyone, you got it?"),
        VoiceLine(90, Jabba, ru="Само собой, Дерси, само собой.", en="Of course, Ms Darcy, of course...  "),
    ]


class Msn7Reward(Msn7, script.CutsceneProps):
    ALIAS = 'reward'
    TITLE = 'Вознаграждение'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Darcy, ru="Спасибо, Трент. Я понимаю что долг платежом красен, но чуть попозже, хорошо? Оказывается этот урод далеко не всегда «покупал» свои вещички.", en="Thanks Trent. While one good turn deserves another, it'll have to wait a bit. Turns out that jerk wasn't always \"buying\" his stuff."),
        VoiceLine(20, Darcy, ru="С особо несговорчивыми покупателями ему помогали те самые ребятки, которых мы сожгли рядом со станцией. Нам надо с этим всем разобраться...", en="Those goons we took out near the station helped him eliminate some particularly... stubborn.. customers. We need to sort this all out..."),
        VoiceLine(30, Darcy, ru="Кстати, вот вам официально от правительства Бретонии за помощь. Десять тысяч.", en="Oh yes, payment for your troubles, from the Bretonian goverment. Ten thousands credits."),
        VoiceLine(40, Trent, ru="Но артефакт я тебе все равно не продам.", en="Gonna take more than that to make me part with the artifact, Darcy."),
        VoiceLine(50, Darcy, ru="Да-да. Очень смешно, Трент. До скорого.", en="Yeah-yeah. Very funny, Trent. See you later."),
        VoiceLine(60, Trent, ru="Постарайтесь побыстрее, Дерси.", en="See you soon, Darcy."),
    ]

class Msn7Space(Msn7, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(10, Trent, ru='Я тут каких-то гопников раскидал, но Железного Зада среди них не было.',
							 en="I roughed up some bozos out there, but Iron Butt wasn't amongst them."),
        VoiceLine(20, CorsairBarman,
                  ru='Айронсайда, мистер Трент, Билла Айронсайда. Если его не было здесь, попробуйте во втором вероятном месте его пребывания. Скидываю координаты.',
				  en="Ironside, Mr. Trent. Bill Ironside. Try his next most likely haunt. Sending you the coordinates now."),
        VoiceLine(30, Trent, ru='Сколько сколько прилетело? 500 кредитов? Они тут совсем охренели?',
							 en="500 credits? Are they kidding me?"),
        VoiceLine(35, Trent,
                  ru='Проще было вообще перевод не делать - на банковской комиссии больше потеряли. Стоит, пожалуй, еще пару вопросов этому бармену задать. Например, "где деньги, Лебовски?".',
				  en="Skinflint. Transfer fees probably set him back more than 500. Next time I'm him \"where's the money, Lebowski?\"."),
        VoiceLine(40, RockfordStation,
                  ru='Мистер Трент, меня зовут Р+окфорд, СБА прислало меня пом+очь вам в поиске артефактов. Жду вас в баре на планете Кадиз. Прошу вас быть как можно скорее, счет идет на секунды.',
				  en="Mr. Trent, my name is Rockford. I've been sent to help you extract the artifact. I'm waiting for you at the bar on planet Cadiz. Come ASAP, time is of the essence."),
        VoiceLine(60, Rockford, ru='Трент, жить хочешь? Помогай!', en="Trent, you wanna get out of here alive? Then help me out!"),
        VoiceLine(70, Rockford,
                  ru='Трент, теперь летим в торговую линию! Нам нужно добраться до Малого Омикрона.',
				  en="Now get us to the trade lane! We've got to get to Omicron Minor."),
        VoiceLine(80, Trent, ru='Приятно познакомиться, мистер Рокфорд.', en="A pleasure to meet you, Mister Rockford."),
        VoiceLine(90, Rockford, ru='Не мистер. Просто Р+окфорд.', en="Not 'Mister'. Just Rockford."),
        VoiceLine(100, Trent, ru='Кто были все эти люди, Рокфорд?', en="Who were all those people, Rockford?"),
        VoiceLine(110, Rockford, ru='Агенты Ордена.', en="Order."),
        VoiceLine(120, Trent, ru='А можно поподробнее?', en="Care to be more specific?"),
        VoiceLine(130, Rockford, ru='О чём?', en="About what?"),
        VoiceLine(140, Trent, ru='Вообще о многом. Если вкратце, кто вы и во что я в очередной раз вляпался.',
							  en="Everything. Who are you people, and what mess have I stepped into this time?"),
        VoiceLine(150, Rockford,
                  ru='Я агент СБА Р+окфорд и меня прислали на помощь группе Дельта и вам, Трент, потому что вы вляпались в неприятности.',
				  en="I'm Rockford. ASF. I've been sent to assist Delta Squad and you, Trent, because you've stumbled into this."),
        VoiceLine(160, Trent,
                  ru='Да твою же налево... Хорошо, тогда расскажите более развернуто, как вы меня нашли, почему вас, то есть нас на Кадизе ждали, и что вообще мы теперь планируем делать.',
				  en="Oh, for fuck's sake... Alright. Then be straight with me. How did you find me? Why were they waiting for us at Cadiz? And what's the plan now?"),
        VoiceLine(170, Rockford,
                  ru='Когда я прибыл в систему Кадиз, я вышел на связь с лидером Дельта и узнал от него о сложившейся ситуации и о том, что боеспособный корабль остался только у вас.',
				  en="I made contact with Delta Lead when I reached Cadiz. He briefed me on the situation and informed me that your ship was the only combat-capable one left."),
        VoiceLine(180, Rockford,
                  ru='Я отследил все взятые в этой системе фрилансерами контракты и определил ваше местонахождение. Кстати, Трент, вы действительно готовы работать за такие грош+и?',
				  en="I cross-referenced all freelance contracts taken in this system and acquired your location. By the way, Trent, just how desperate for work are you? 500 credits?"),
        VoiceLine(190, Trent, ru='Не будем об этом. Что было дальше?', en="Let's not go there. Keep going."),
        VoiceLine(200, Rockford,
                  ru='Я знал что за вами следят агенты Ордена. Кроме того, они подозревали о моем присутствии в системе.',
				  en="I knew Order agents were tracking you. They were also aware of my presence in the system."),
        VoiceLine(210, Rockford,
                  ru='Поэтому я решил устроить им ловушку и послал вам сообщение с просьбой о встрече в максимально удаленной от их главных сил точке - на планете Кадиз.',
				  en="So, I set a trap. I sent you a message to meet at the location farthest from their main force—the planet Cadiz itself."),
        VoiceLine(220, Rockford,
                  ru='Они смогли отправить на Кадиз только небольшую группу перехвата, а мы с вами, Трент смогли ее уничтожить. Насчет того, что делать дальше, по-моему очевидно, забирать артефакты.',
				  en="they could only dispatch a small team to intercept, which you and I just cleaned up. As for our next move, it's obvious. We retrieve the artifacts."),
        VoiceLine(230, Trent, ru='И у нас уже есть план?', en="And do you have a plan?"),
        VoiceLine(240, Rockford, ru='Конечно. Как можно лететь куда-то без плана?', en="Of course."),
        VoiceLine(250, Trent, ru='Меня в него не посветите?', en="Care to share?"),
        VoiceLine(260, Rockford,
                  ru='Артефакты содержатся на базе Тортуга в системе Малый Омикрон. Формально это пиратская база, но она используется агентами Ордена и поэтому отлично защищена.',
				  en="The artifacts are currently being held at Tortuga Base in the Omicron Minor system. It's supposedly a pirate outpost, but in actuality it belongs to the Order. It's heavily fortified."),
        VoiceLine(270, Rockford,
                  ru='На станции находится передатчик, обеспечивающий постоянную двустороннюю связь со штабом Ордена.',
				  en="The station houses a transmitter that maintains a constant two-way link with Order High Command."),
        VoiceLine(280, Rockford,
                  ru='Если передатчик будет выведен из строя, по протоколу они обязаны эвакуировать все важные объекты на ближайшую другую базу. Мы разрушим передатчик и нападем на конвой, перевозящий артефакты.',
				  en="If the transmitter is disabled, protocol mandates they evacuate all high-value assets to the nearest secure facility. We will destroy the transmitter and ambush the convoy transporting the artifacts."),
        VoiceLine(290, Trent, ru='Эмм... Ну ты у нас тут специалист, тебе виднее.', en="Uh-huh... Well, you're the expert here. You call the shots."),
        VoiceLine(310, Rockford,
                  ru='Сейчас я сброшу контейнеры с зарядами направленного действия. Подберите их, Трент, расположите вокруг передатчика и подорвите.',
				  en=" I'm jettisoning canisters with shaped charges now. Pick them up, Trent, position them around the transmitter, and deploy them. You'll need to access your inventory and use the bin icon next to the item descriptor to deploy them."),
        VoiceLine(320, Rockford,
                  ru='Устанавливайте заряды с выключенным щитом, иначе они сдетонируют. Координаты передатчика в вашем компьютере. Вперед!',
				  en="You'll need to manually detonate them by shooting at them. The coordinates for the transmitter are in your computer. Move out!"),
        VoiceLine(330, Tortuga, ru='Фрилансер альфа-один, немедленно покиньте запретную зону...', en="Freelancer Alpha-One, you are in a restricted area. Withdraw immediately."),
        VoiceLine(340, Tortuga,
                  ru='Фрилансер альфа-один, если вы не покинете зону, мы будем вынуждены активировать защитный периметр!',
				  en="Freelancer Alpha-One, if you do not withdraw we will be forced to destroy you!"),
        VoiceLine(350, Trent, ru='Готово. Передатчик уничтожен.', en="It's done. The transmitter is destroyed."),
        VoiceLine(355, Rockford, ru='Я заметил. Судя по переговорам вся станция на ушах сто+ит. Теперь посм+отрим, что они сделают.',
								 en="OK. Judging from the comms chatter, the whole station is in uproar. Now, let's see what they do next."),
        VoiceLine(360, Rockford, ru='Вижу конвой выходящий из Тортуги. Направляюсь за ним. Передаю координаты.', en="Scanners are showing a convoy leaving Tortuga. Moving to intercept. Sending you the coordinates."),
        VoiceLine(370, Rockford, ru='Перехватываю грузовик. Нужна помощь.', en="Engaging the freighter. I need backup."),

        VoiceLine(380, Rockford, ru='Трент, атакуй грузовик!', en="Trent, attack the freighter!"),
        VoiceLine(390, Trent, ru='Щит грузовика просто непробиваем. Что делать то?', en="The freighter's shields are impenetrable! What are we supposed to do?"),
        VoiceLine(395, Rockford,
                  ru='Трент, атакуй грузовик! Это сверхзащищённая модель, его щит неуязв+им. Но есть способ преодолеть эту защиту.',
				  en="Trent, keep up the attack! Its experimental shields are invulnerable but there's an Achilles heel."),
        VoiceLine(400, Rockford,
                  ru='Частое использование Электромагнитной пушки приведет к перегреву генераторов и отключению щита. Подлети ближе к транспорту, чтобы пилот мог по тебе стрелять.',
				  en="Its generators overheat and reboot if they cycle the guns too rapidly. It's vulnerable during the downtime. Close in to the transport so its turrets engage you."),
        VoiceLine(410, Trent, ru='В смысле? Быть приманкой?', en="What, and get blown to swiss cheese?"),
        VoiceLine(420, Rockford, ru='Да.', en="Yep."),
        VoiceLine(430, Rockford, ru='Щит упал. Трент, уничтожь грузовик! Целься в уявзимые точки!', en="Shields are down! Trent, take it out!"),
        VoiceLine(440, Rockford, ru='Они вызывают подкрепление. Скоро вся эта зона будет кишать пилотами Ордена. Уничтожь транспорт! Быстрее!',
								 en="They're calling in reinforcements. This entire sector will be swarming with Order scum in a heartbeat. Destroy the transport! Now!"),
        VoiceLine(445, Rockford, ru='Транспорт взорван, подбери артефакты!', en="The transport is destroyed. Retrieve the artifacts!"),

        VoiceLine(450, Trent, ru='Это было потно. Куда теперь?', en="That was intense. Where to now?"),
        VoiceLine(460, Rockford,
                  ru='У меня есть убежище в Омега-13. Проведем там обслуживание кораблей и разработаем план доставки артефактов в штаб СБА.',
				  en="I have a safe house in Omega-13. We'll perform ship maintenance there and plan delivery of the artifacts to ASF High Command."),
        VoiceLine(470, Trent,
                  ru='Звучит отлично! Веди. Кстати, а что попалось тебе? У меня какая-то мелочевка кочевников и том Протея... Значит ключ у тебя?',
				  en="Sounds good to me. Lead the way. By the way, what did you get on your end? I've got some Nomad trinkets and The Proteus Tome... So, you have the key?"),
        VoiceLine(480, Rockford, ru='Да.', en="Affirmative."),

        VoiceLine(490, Trent,
                  ru='Кстати, Рокфорд, а почему тебя так хотят убить агенты Ордена? Стоило тебе выйти на связь и на место встречи прибыла целая армия.',
				  en="By the way, Rockford, why do the Order want you dead so badly? The moment you made contact, a whole army showed up at the rendezvous."),
        VoiceLine(495, Rockford,
                  ru='Я был агентом еще старого, большого Ордена. Я слишком много знаю. С момента раскола постоянно приходится спать вполглаза.',
				  en="I was an agent of the original Order pre-Schism. I know too much. Ever since then I've had to sleep with one eye open."),
        VoiceLine(498, Rockford, ru='Даже сейчас нужно держать ухо в остро. Мы можем нарваться на патруль в любой момент', en="Even now, we have to stay sharp. We could run into a patrol at any moment."),

        VoiceLine(500, Trent, ru='Нужно добраться до ближайшей базы.', en="We need to get to the nearest base."),
        VoiceLine(510, Darcy, ru='Давай, шутник, залетай в торговую линию. Тут лететь не далеко.', en="Get a move on, hotshot, get in the trade lane. It's not a long flight."),
        VoiceLine(520, Darcy, ru='Ты там особо с ним не откровенничай. Эта личность чрезвычайно мутная.', en="And don't get too chummy with him. There's something off about him."),
        VoiceLine(530, Darcy,
                  ru='Он часто бывает нам полезен, поэтому мы закрываем глаза на его мелкие шалости, но, чует мое сердце, до поры до времени. Когда-нибудь он нарвется.',
				  en="He's proven useful to us, so we turn a blind eye to his little schemes. But I've got a feeling it's only a matter of time before he pushes his luck too far one day."),
        VoiceLine(550, JabbaBandit, ru='Фрилансер, у тебя есть кое-что что, что очень нужно нам. Отдавай по-хорошему!', en="Freelancer, you've got something we want. Hand it over!", cinematic=True),
        VoiceLine(560, Darcy,
                  ru='Мальчики, а вы не охренели? Это мой участок, я здесь главный коп. Трент, давай разберем эту шпану.',
				  en="Boys, have you completely lost your minds? This is my turf, I'm top dog around here. Trent, let's wipe the floor with these scum.",
                  cinematic=True),
        VoiceLine(570, Darcy,
                  ru='Джабба, засранец, теперь ты точно доигрался. Трент, я вернусь, поговорю с нашим другом еще раз. Увидимся на планете.',
				  en="Jabba, you son of a bitch, you've really crossed the line now. Trent, I'll be back; I need to have another... chat with our friend. See you at the planet."),
        VoiceLine(2000, CorsairBarman,
                  ru='Координаты последнего местоположения бандитов Старлайна в вашей нейросети. Возможно, Билл Айронсайд там. Разыщите его.',
				  en="The coordinates to the last known location of the Starliner stooges are in your neural net. Track down Bill Ironside and make him an offer he can't refuse."),
        VoiceLine(2010, CorsairBarman,
                  ru='Айронсайд убит, теперь эти ублюдки нас долго не побеспокоят. Пересылаю ваше вознаграждение. Конец связи.',
				  en="Ironside is dead. Those bastards won't be a problem again. Transferring your payment. Channel closed."),
    ]

class Mission7(Msn7, script.StoryMission):
    MISSION_INDEX = 7
    CUTSCENES = [
        Msn7Offer,
        Msn7Cadiz,
        Msn7Omega13,
        Msn7Battleship,
        Msn7CheckArtifact,
        Msn7Reward,
    ]
    SPACE_CLASS = Msn7Space
    SYNC_SPACE = True

    MISSION_TITLE = 'Миссия 7. Возвращение артефактов'