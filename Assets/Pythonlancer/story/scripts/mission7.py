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
        VoiceLine(10, CorsairBarman, ru="", en="Anything to drink?"),
        VoiceLine(20, Trent, ru="", en="I need a job. Preferably with good compensation."),
        VoiceLine(30, CorsairBarman, ru="", en="We’re not in shortage of local freelancers, believe it or not. Remember which system we’re in?"),
        VoiceLine(40, Trent, ru="", en="Actually... I’ll work for minimum wage. Seriously, friend, help me - I’m totally broke."),
        VoiceLine(50, CorsairBarman, ru="", en="Alright, Mr..."),
        VoiceLine(60, Trent, ru="", en="Trent"),
        VoiceLine(70, CorsairBarman, ru="", en="Very well, Mr. Trent. We do have something for you"),
        VoiceLine(80, CorsairBarman, ru="", en="A troupe of Liberty crooks recently took hold in our space. They call themselves Starline Robbers."),
        VoiceLine(90, CorsairBarman, ru="", en="Your task is to eliminate their leader, Bill Ironside. I’ll send you the coordinates if you’re interested."),
        VoiceLine(100, CorsairBarman, ru="", en="But as we discussed, your payment will be lower than usual"),
        VoiceLine(110, Trent, ru="", en="Sounds great, I’m in."),
    ]


class Msn7Cadiz(Msn7, script.CutsceneProps):
    ALIAS = 'cadiz'
    TITLE = 'Кадиз'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, CadizEnemyOne, ru="", en="Hey, bro, where Rockford is?"),
        VoiceLine(20, Trent, ru="", en="This is none of your business."),
        VoiceLine(30, CadizEnemyTwo, ru="", en="Playing brave, shithead? Answer the question before you'll dive deeper into the problems"),
        VoiceLine(40, CadizEnemyThree, ru="", en="This will make you talk."),
        VoiceLine(50, CadizEnemyFour, ru="", en="Where Rockford is, prick?"),
        VoiceLine(60, Rockford, ru="", en="I'm Rockford"),
        VoiceLine(65, Rockford, ru="", en="Follow me! Immediately!"),
    ]


class Msn7Omega13(Msn7, script.CutsceneProps):
    ALIAS = 'omega13'
    TITLE = 'Омега-13'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Trent, ru="", en="Damn, Rockford, I'm immobilized!"),
        VoiceLine(20, Rockford, ru="", en="I know."),
        VoiceLine(30, Trent, ru="", en="Rockford, what's happening? You are an ASF agent, you must help me."),
        VoiceLine(40, Rockford, ru="", en="I'm not an ASF agent."),
        VoiceLine(50, Trent, ru="", en="But you're going to destroy the artifacts."),
        VoiceLine(60, Rockford, ru="", en="The artifacts will survive the explosion of the ship."),
        VoiceLine(100, Trent, ru="", en="Come-on old-junk. Turn on!"),
    ]


class Msn7Battleship(Msn7, script.CutsceneProps):
    ALIAS = 'battleship'
    TITLE = 'Линкор Принц Уэльский'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Trent, ru="", en="I need help! It is a matter of national importance!"),
        VoiceLine(20, WalesBarman, ru="", en="Huh, is it really? If so, then you should ask someone representitive of the State."),
        VoiceLine(30, WalesBarman, ru="", en="Up there we have officer Darcy, she is one of a kind."),
        VoiceLine(40, Trent, ru="", en="My name is Trent. I work for a secret organisation tied to Order, and I must contact them ASAP."),
        VoiceLine(50, Darcy, ru="", en="And another one... Mister, don't you know that trading artifacts of alien origin is illegal?"),
        VoiceLine(60, Darcy, ru="", en="We caught a pair of dealers just like you recently. They were claiming to be agents of the Order too, when we jailed them."),
        VoiceLine(70, Darcy, ru="", en="Do you want to keep a company to them or, perhaps, their friend, Napoleon in a mental assylum? "),
        VoiceLine(80, Trent, ru="", en="I must deliver an artifact of great importance to the headquarters of our organistation as soon as possible."),
        VoiceLine(90, Trent, ru="", en="Or else I will be put to death and possibly you too. Speaking of artifacts..."),
        VoiceLine(100, Darcy, ru="", en="Oh, wow... Impressive."),
        VoiceLine(110, Darcy, ru="", en="How do I know that it isn't from some souvenir shop for tourists?"),
        VoiceLine(120, Trent, ru="", en="God damn it..."),
        VoiceLine(130, Darcy, ru="", en="All righty then, I have a friend who is an expert on various rarities at a nearby station."),
        VoiceLine(140, Darcy, ru="", en="Let him take a look at this thing, and if you're telling the truth, I promice you any help I can offer."),
        VoiceLine(150, Darcy, ru="", en="But if it is indeed a souvenir, mister joker, I promice you a teaparty today with Napoleon."),
        VoiceLine(160, Trent, ru="", en="There is a problem. Almost all of the electric circuits on my ship is scorched, I'm not even sure how I managed to make it to this base."),
        VoiceLine(170, Darcy, ru="", en="All right, I will give you one of our ships."),
        VoiceLine(180, Darcy, ru="", en="But if you decide to use it to escape, keep in mind, that all of our ships are equipped with track beacons, so I'll find you anywhere. "),
    ]


class Msn7CheckArtifact(Msn7, script.CutsceneProps):
    ALIAS = 'check_artifact'
    TITLE = 'Проверка артефакта'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Trent, ru="", en="Wow! Looks like this guy's area of interests is wast."),
        VoiceLine(20, Jabba, ru="", en="I'm interested in rare trinkets, that are profitable to buy and even more profitable to sell."),
        VoiceLine(30, Jabba, ru="", en="Greetings, Darcy."),
        VoiceLine(40, Darcy, ru="", en="Hi, Jabba. I want you to check out something."),
        VoiceLine(50, Jabba, ru="", en="Wow! Quite an interesting thing, clearly of alien origin."),
        VoiceLine(60, Jabba, ru="", en="If you're so happened to be broke right now, I can pay you ten thosands credits right away."),
        VoiceLine(70, Darcy, ru="", en="Oh, shit... So much for \"drink a beer at the bar\". Okay, Trent, we're leaving."),
        VoiceLine(80, Darcy, ru="", en="Jabba, you aren't a fool, are you? You will keep your mouth shut, am I right?"),
        VoiceLine(90, Jabba, ru="", en="Of course, Darcy, of course...  "),
    ]


class Msn7Reward(Msn7, script.CutsceneProps):
    ALIAS = 'reward'
    TITLE = 'Вознаграждение'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Darcy, ru="", en="Thank you, Trent. I understand that one good turn deserves another, but can't it wait a bit? Turns out not all of the trinkets this bastard had were \"bought\"."),
        VoiceLine(20, Darcy, ru="", en="To convince some of the least conforming customers, he used the guys we just burnt near the station. All of this needs to be sorted out..."),
        VoiceLine(30, Darcy, ru="", en="By the way, here is the official payment for your help from the Bretonian goverment. Ten thousands credits."),
        VoiceLine(40, Trent, ru="", en="I'm still not going to sell you the artifact, Darcy."),
        VoiceLine(50, Darcy, ru="", en="Yeah-yeah. Very funny, Trent. See you later."),
        VoiceLine(60, Trent, ru="", en="Try not to drag this, Darcy."),
    ]

class Msn7Space(Msn7, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(10, Trent, ru='Я тут каких-то гопников раскидал, но Железного Зада среди них не было.',
							 en="I roughed up some local punks here, but Iron Butt wasn't among them."),
        VoiceLine(20, CorsairBarman,
                  ru='Айронсайда, мистер Трент, Билла Айронсайда. Если его не было здесь, попробуйте во втором вероятном месте его пребывания. Скидываю координаты.',
				  en="Ironside, Mr. Trent. Bill Ironside. If he wasn't here, try the second most likely spot. Sending you the coordinates now."),
        VoiceLine(30, Trent, ru='Сколько сколько прилетело? 500 кредитов? Они тут совсем охренели?',
							 en="They paid me how much? 500 credits? Are they kidding me?"),
        VoiceLine(35, Trent,
                  ru='Проще было вообще перевод не делать - на банковской комиссии больше потеряли. Стоит, пожалуй, еще пару вопросов этому бармену задать. Например, "где деньги, Лебовски?".',
				  en="They'd have lost less just keeping the money — the bank transfer fee probably cost more. Guess I should ask this bartender a couple more questions. Like, \"where's the money, Lebowski?\"."),
        VoiceLine(40, RockfordStation,
                  ru='Мистер Трент, меня зовут Р+окфорд, СБА прислало меня пом+очь вам в поиске артефактов. Жду вас в баре на планете Кадиз. Прошу вас быть как можно скорее, счет идет на секунды.',
				  en="Mr. Trent, my name is Rockford. The ASF has sent me to assist you in the artifact retrieval. I'm waiting for you at the bar on planet Cadiz. I need you here ASAP, we are counting seconds."),
        VoiceLine(60, Rockford, ru='Трент, жить хочешь? Помогай!', en="Trent, you wanna live? Then help me!"),
        VoiceLine(70, Rockford,
                  ru='Трент, теперь летим в торговую линию! Нам нужно добраться до Малого Омикрона.',
				  en="Trent, now get us to the trade lane! We need to reach Omicron Minor."),
        VoiceLine(80, Trent, ru='Приятно познакомиться, мистер Рокфорд.', en="A pleasure to meet you, Mister Rockford."),
        VoiceLine(90, Rockford, ru='Не мистер. Просто Р+окфорд.', en="Not 'Mister'. Just Rockford."),
        VoiceLine(100, Trent, ru='Кто были все эти люди, Рокфорд?', en="Who were all those people, Rockford?"),
        VoiceLine(110, Rockford, ru='Агенты Ордена.', en="Agents of The Order."),
        VoiceLine(120, Trent, ru='А можно поподробнее?', en="Care to be a bit more specific?"),
        VoiceLine(130, Rockford, ru='О чём?', en="About what?"),
        VoiceLine(140, Trent, ru='Вообще о многом. Если вкратце, кто вы и во что я в очередной раз вляпался.',
							  en="About a lot of things. The short version: who are you people, and what kind of mess have I stepped in this time?"),
        VoiceLine(150, Rockford,
                  ru='Я агент СБА Р+окфорд и меня прислали на помощь группе Дельта и вам, Трент, потому что вы вляпались в неприятности.',
				  en="I'm ASF Agent Rockford. I was sent to assist Delta Squad and you, Trent, because you've stumbled into a situation."),
        VoiceLine(160, Trent,
                  ru='Да твою же налево... Хорошо, тогда расскажите более развернуто, как вы меня нашли, почему вас, то есть нас на Кадизе ждали, и что вообще мы теперь планируем делать.',
				  en="Oh, for fuck's sake... Alright. Then give me the full picture. How did you find me? Why were they waiting for us at Cadiz? And what's the plan now?"),
        VoiceLine(170, Rockford,
                  ru='Когда я прибыл в систему Кадиз, я вышел на связь с лидером Дельта и узнал от него о сложившейся ситуации и о том, что боеспособный корабль остался только у вас.',
				  en="When I arrived in the Cadiz system, I made contact with Delta Lead. He briefed me on the situation and informed me that your ship was the only combat-capable one left."),
        VoiceLine(180, Rockford,
                  ru='Я отследил все взятые в этой системе фрилансерами контракты и определил ваше местонахождение. Кстати, Трент, вы действительно готовы работать за такие грош+и?',
				  en="I cross-referenced all freelance contracts taken in this system and pinpointed your location. By the way, Trent, are you really that desperate for work?"),
        VoiceLine(190, Trent, ru='Не будем об этом. Что было дальше?', en="Let's not go there. What happened next?"),
        VoiceLine(200, Rockford,
                  ru='Я знал что за вами следят агенты Ордена. Кроме того, они подозревали о моем присутствии в системе.',
				  en="I knew Order agents were tracking you. They were also aware of my presence in the system."),
        VoiceLine(210, Rockford,
                  ru='Поэтому я решил устроить им ловушку и послал вам сообщение с просьбой о встрече в максимально удаленной от их главных сил точке - на планете Кадиз.',
				  en="So, I set a trap. I sent you a message to meet at the location farthest from their main force—the planet Cadiz itself."),
        VoiceLine(220, Rockford,
                  ru='Они смогли отправить на Кадиз только небольшую группу перехвата, а мы с вами, Трент смогли ее уничтожить. Насчет того, что делать дальше, по-моему очевидно, забирать артефакты.',
				  en="hey could only dispatch a small interception team there, which you and I, Trent, managed to eliminate. As for our next move, I think it's obvious. We retrieve the artifacts."),
        VoiceLine(230, Trent, ru='И у нас уже есть план?', en="And do we have a plan?"),
        VoiceLine(240, Rockford, ru='Конечно. Как можно лететь куда-то без плана?', en="Of course. Who flies anywhere without a plan?"),
        VoiceLine(250, Trent, ru='Меня в него не посветите?', en="Care to let me in on it?"),
        VoiceLine(260, Rockford,
                  ru='Артефакты содержатся на базе Тортуга в системе Малый Омикрон. Формально это пиратская база, но она используется агентами Ордена и поэтому отлично защищена.',
				  en="The artifacts are being held at the Tortuga Base in the Omicron Minor system. It's officially a pirate outpost, but it's used by Order agents and is therefore heavily fortified."),
        VoiceLine(270, Rockford,
                  ru='На станции находится передатчик, обеспечивающий постоянную двустороннюю связь со штабом Ордена.',
				  en="The station houses a transmitter that maintains a constant two-way link with Order High Command."),
        VoiceLine(280, Rockford,
                  ru='Если передатчик будет выведен из строя, по протоколу они обязаны эвакуировать все важные объекты на ближайшую другую базу. Мы разрушим передатчик и нападем на конвой, перевозящий артефакты.',
				  en="If the transmitter is disabled, protocol mandates they evacuate all high-value assets to the nearest secure facility. We will destroy the transmitter and ambush the convoy transporting the artifacts."),
        VoiceLine(290, Trent, ru='Эмм... Ну ты у нас тут специалист, тебе виднее.', en="Uh-huh... Well, you're the expert here. You call the shots."),
        VoiceLine(310, Rockford,
                  ru='Сейчас я сброшу контейнеры с зарядами направленного действия. Подберите их, Трент, расположите вокруг передатчика и подорвите.',
				  en=" I'm jettisoning canisters with shaped charges now. Pick them up, Trent, position them around the transmitter, and detonate."),
        VoiceLine(320, Rockford,
                  ru='Устанавливайте заряды с выключенным щитом, иначе они сдетонируют. Координаты передатчика в вашем компьютере. Вперед!',
				  en="Deploy the charges with your shields down, or they will detonate prematurely. The transmitter's coordinates are in your computer. Move out!"),
        VoiceLine(330, Tortuga, ru='Фрилансер альфа-один, немедленно покиньте запретную зону...', en="Freelancer Alpha-One, you are in a restricted zone. Withdraw immediately."),
        VoiceLine(340, Tortuga,
                  ru='Фрилансер альфа-один, если вы не покинете зону, мы будем вынуждены активировать защитный периметр!',
				  en="Freelancer Alpha-One, if you do not leave the area, we will be forced to activate the defense perimeter!"),
        VoiceLine(350, Trent, ru='Готово. Передатчик уничтожен.', en="It's done. The transmitter is destroyed."),
        VoiceLine(355, Rockford, ru='Я заметил. Судя по переговорам вся станция на ушах сто+ит. Теперь посм+отрим, что они сделают.',
								 en="I noticed. Judging by the comms traffic, the whole station is in an uproar. Now, let's see what they do."),
        VoiceLine(360, Rockford, ru='Вижу конвой выходящий из Тортуги. Направляюсь за ним. Передаю координаты.', en="I see a convoy leaving Tortuga. I'm moving to intercept. Sending you the coordinates."),
        VoiceLine(370, Rockford, ru='Перехватываю грузовик. Нужна помощь.', en="Engaging the freighter. I need backup."),

        VoiceLine(380, Rockford, ru='Трент, атакуй грузовик!', en="Trent, attack the freighter!"),
        VoiceLine(390, Trent, ru='Щит грузовика просто непробиваем. Что делать то?', en="The freighter's shields are impenetrable! What are we supposed to do?"),
        VoiceLine(395, Rockford,
                  ru='Трент, атакуй грузовик! Это сверхзащищённая модель, его щит неуязв+им. Но есть способ преодолеть эту защиту.',
				  en="Trent, attack the freighter! It's a heavily fortified model; its shields are invulnerable. But there is a way to bypass this defense."),
        VoiceLine(400, Rockford,
                  ru='Частое использование Электромагнитной пушки приведет к перегреву генераторов и отключению щита. Подлети ближе к транспорту, чтобы пилот мог по тебе стрелять.',
				  en="Rapid fire from an EMP cannon will overheat its generators and drop the shields. Get closer to the transport so its turrets engage you."),
        VoiceLine(410, Trent, ru='В смысле? Быть приманкой?', en="What, you mean be the bait?"),
        VoiceLine(420, Rockford, ru='Да.', en="Yes."),
        VoiceLine(430, Rockford, ru='Щит упал. Трент, уничтожь грузовик! Целься в уявзимые точки!', en="Shields are down! Trent, destroy the freighter! Aim for its weak spots!"),
        VoiceLine(440, Rockford, ru='Они вызывают подкрепление. Скоро вся эта зона будет кишать пилотами Ордена. Уничтожь транспорт! Быстрее!',
								 en="They're calling for reinforcements. This entire sector will be swarming with Order pilots soon. Destroy the transport! Now!"),
        VoiceLine(445, Rockford, ru='Транспорт взорван, подбери артефакты!', en="The transport is destroyed. Retrieve the artifacts!"),

        VoiceLine(450, Trent, ru='Это было потно. Куда теперь?', en="That was intense. Where to now?"),
        VoiceLine(460, Rockford,
                  ru='У меня есть убежище в Омега-13. Проведем там обслуживание кораблей и разработаем план доставки артефактов в штаб СБА.',
				  en="I have a shelter in Omega-13. We'll perform ship maintenance there and plan the delivery of the artifacts to ASF High Command."),
        VoiceLine(470, Trent,
                  ru='Звучит отлично! Веди. Кстати, а что попалось тебе? У меня какая-то мелочевка кочевников и том Протея... Значит ключ у тебя?',
				  en="Sounds good to me. Lead the way. By the way, what did you get on your end? I've got some Nomad trinkets and The Proteus Tome... So, you have the key?"),
        VoiceLine(480, Rockford, ru='Да.', en="Affirmative."),

        VoiceLine(490, Trent,
                  ru='Кстати, Рокфорд, а почему тебя так хотят убить агенты Ордена? Стоило тебе выйти на связь и на место встречи прибыла целая армия.',
				  en="By the way, Rockford, why do the Order agents want you dead so badly? The moment you made contact, a whole army showed up at the rendezvous."),
        VoiceLine(495, Rockford,
                  ru='Я был агентом еще старого, большого Ордена. Я слишком много знаю. С момента раскола постоянно приходится спать вполглаза.',
				  en="I was an agent of the original, larger Order. I know too much. Ever since the schism, I've had to sleep with one eye open."),
        VoiceLine(498, Rockford, ru='Даже сейчас нужно держать ухо в остро. Мы можем нарваться на патруль в любой момент', en="Even now, we have to stay sharp. We could run into a patrol at any moment."),

        VoiceLine(500, Trent, ru='Нужно добраться до ближайшей базы.', en="We need to get to the nearest base."),
        VoiceLine(510, Darcy, ru='Давай, шутник, залетай в торговую линию. Тут лететь не далеко.', en="Get a move on, hotshot, get in the trade lane. It's not a long flight."),
        VoiceLine(520, Darcy, ru='Ты там особо с ним не откровенничай. Эта личность чрезвычайно мутная.', en="And don't get too chummy with him. That character is extremely shady."),
        VoiceLine(530, Darcy,
                  ru='Он часто бывает нам полезен, поэтому мы закрываем глаза на его мелкие шалости, но, чует мое сердце, до поры до времени. Когда-нибудь он нарвется.',
				  en="He's often useful to us, so we turn a blind eye to his little schemes. But I've got a feeling it's only a matter of time. He'll push his luck too far one day."),
        VoiceLine(550, JabbaBandit, ru='Фрилансер, у тебя есть кое-что что, что очень нужно нам. Отдавай по-хорошему!', en="Freelancer, you've got something we want. Hand it over the easy way!"),
        VoiceLine(560, Darcy,
                  ru='Мальчики, а вы не охренели? Это мой участок, я здесь главный коп. Трент, давай разберем эту шпану.',
				  en="Boys, have you completely lost your minds? This is my turf, I'm the top cop around here. Trent, let's clean up this scum."),
        VoiceLine(570, Darcy,
                  ru='Джабба, засранец, теперь ты точно доигрался. Трент, я вернусь, поговорю с нашим другом еще раз. Увидимся на станции.',
				  en="Jabba, you son of a bitch, you've really crossed the line now. Trent, I'll be back; I need to have another... chat with our friend. See you at the station."),
        VoiceLine(2000, CorsairBarman,
                  ru='Координаты последнего местоположения бандитов Старлайна в вашей нейросети. Возможно, Билл Айронсайд там. Разыщите его.',
				  en="The coordinates for the last known location of the Starliner thugs are in your neural net. Bill Ironside might be there. Track him down."),
        VoiceLine(2010, CorsairBarman,
                  ru='Айронсайд убит, теперь эти ублюдки нас долго не побеспокоят. Пересылаю ваше вознаграждение. Конец связи.',
				  en="Ironside is dead. Those bastards won't be a problem for a long time. Transferring your payment. Channel closed."),
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
