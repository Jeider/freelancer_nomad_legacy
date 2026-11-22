from audio import story_delivery as performance
from story.cutscenes.story_scenes import m07_tau_arrival
from story.cutscenes.story_scenes import m07_battleship, m07_check_artifact, m07_gunners, m07_offer, m07_offer_accept, m07_offer_decision, m07_omega13, m07_reward
from audio.delivery import HIGH_PITCH_NOT_FAST
from story import script
from audio.sound import VoiceLine
from story.actors import (
    Trent, Darcy, CorsairBarman, Rockford, Tortuga, JabbaBandit, RockfordStation,
    CadizEnemyOne, CadizEnemyTwo, CadizEnemyThree, CadizEnemyFour, WalesBarman, Jabba
)


class Msn7(object):
    MISSION_INDEX = 7


class Msn7Offer(Msn7, script.CutsceneProps):
    THORN_DECISION_CLASS = m07_offer_decision.M07OfferDecisionScene
    THORN_ACCEPT_CLASS = m07_offer_accept.M07OfferAcceptScene
    THORN_CLASS = m07_offer.M07OfferScene
    ALIAS = 'offer'
    TITLE = 'Предложение'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, CorsairBarman, ru="Чего налить?", en="What can I pour you?"),
        VoiceLine(20, Trent, ru="Дельца какого-нибудь, желательно с хорошей оплатой.", en="Some kind of job, preferably with good pay."),
        VoiceLine(30, CorsairBarman, ru="Да у нас тут вроде и в своих фрилансерах недостатка нет, понимаете же в какой системе находитесь.", en="Well, we don't seem short of our own freelancers here. You do understand what system you're in."),
        VoiceLine(40, Trent, ru="А я… скидку хорошую сделаю! Выручай дружище, я совсем на мели.", en="And I'll... give a good discount! Help me out, buddy, I'm completely broke.", delivery_en=performance.UNCERTAIN),
        VoiceLine(50, CorsairBarman, ru="Окей, мистер...", en="Okay, mister..."),
        VoiceLine(60, Trent, ru="Трент", en="My name is Trent"),
        VoiceLine(70, CorsairBarman, ru="Окей, мистер Трент. Будет для вас дельце.", en="Okay, Mr. Trent. There'll be a little job for you."),
        VoiceLine(80, CorsairBarman, ru="К нам тут гастролеры пожаловали из Либерти. Называют себя бандой Старлайна.", en="Some touring crews from Liberty have shown up. They call themselves the Starline gang."),
        VoiceLine(90, CorsairBarman, ru="Найдите их и убейте Билла Айронсайда - их лидера. Координаты их предположительного местонахождения я вам скину. ", en="Find them and kill Bill Ironside, their leader. I'll send you the coordinates of where they're likely to be."),
        VoiceLine(100, CorsairBarman, ru="Но учтите, гонорар будет ниже, чем обычно...", en="But keep in mind, the fee will be lower than usual..."),
        VoiceLine(110, Trent, ru="Звучит заманчиво, я в деле.", en="Sounds tempting. I'm in.", delivery_en=performance.SARDONIC),
    ]


class Msn7Cadiz(Msn7, script.CutsceneProps):
    THORN_CLASS = m07_gunners.M07GunnersScene
    ALIAS = 'cadiz'
    TITLE = 'Кадиз'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, CadizEnemyOne, comment='Два странных поцыка подходят к Тренту', ru="Здаров, земляк! Где Рокфорд?", en="Hey, countryman! Where's Rockford?"),
        VoiceLine(20, Trent, ru="Понятия не имею.", en="I have no idea."),
        VoiceLine(30, CadizEnemyTwo, ru="Слыш, земеля, ты чо такой дерзкий? Тебя по-хорошему спросили, где Рокфорд?", en="Hey, countryman, why so cocky? You were asked nicely. Where's Rockford?", delivery_en=performance.THREATENING),
        VoiceLine(40, CadizEnemyOne, ru="Сейчас наладим диалог (достаёт пушку).", en="We'll get a dialogue going now (draws a gun).", delivery_en=performance.THREATENING),
        VoiceLine(50, CadizEnemyOne, ru="Где Рокфорд, утырок?", en="Where's Rockford, you prick?!", delivery_en=performance.ANGRY),
        VoiceLine(60, Rockford, comment='Поцыков выносят ударом в спину', ru="Я Рокфорд. ", en="I'm Rockford.", delivery_en=performance.DRY),
        VoiceLine(65, Rockford, ru="За мной! Быстро!", en="Follow me! Fast!", delivery_en=performance.URGENT),
    ]


class Msn7Omega13(Msn7, script.CutsceneProps):
    THORN_CLASS = m07_omega13.M07Omega13Scene
    ALIAS = 'omega13'
    TITLE = 'Омега-13'
    DESCRIPTION = ''
    VOICE_LINES = [
        # duplicated for different fx
        VoiceLine(10, Trent, ru="Чёрт, Рокфорд, я обездвижен!", en="Damn, Rockford, I'm immobilized!", delivery_en=performance.ALARMED),
        VoiceLine(15, Trent, ru="Чёрт, Рокфорд, я обездвижен!", en="Damn, Rockford, I'm immobilized!", delivery_en=performance.ALARMED),

        VoiceLine(20, Rockford, ru="Я знаю.", en="I know.", delivery_en=performance.DRY),

        VoiceLine(30, Trent, ru="Рокфорд, что происходит? Ты же агент СБА, ты должен мне помочь", en="Rockford, what's going on? You're an ASF agent, you're supposed to help me.", delivery_en=performance.SHOCKED),
        VoiceLine(35, Trent, ru="Рокфорд, что происходит? Ты же агент СБА, ты должен мне помочь", en="Rockford, what's going on? You're an ASF agent, you're supposed to help me.", delivery_en=performance.SHOCKED),

        VoiceLine(40, Rockford, ru="Я не агент СБА.", en="I'm not an ASF agent.", delivery_en=performance.DRY),

        VoiceLine(50, Trent, ru="Ты же уничтожишь артефакты.", en="You'll destroy the artifacts.", delivery_en=performance.ALARMED),
        VoiceLine(55, Trent, ru="Ты же уничтожишь артефакты.", en="You'll destroy the artifacts.", delivery_en=performance.ALARMED),

        VoiceLine(60, Rockford, ru="Артефакты переживут уничтожение корабля.", en="The artifacts will survive the destruction of the ship.", delivery_en=performance.DRY),


        VoiceLine(100, Trent, ru="Да за-пус-тись же ты, ста-ро-е ко-ры-то.", en="Come on, sta-rt, you o-ld tub.", delivery_en=performance.PANICKED),
    ]


class Msn7Battleship(Msn7, script.CutsceneProps):
    THORN_CLASS = m07_battleship.M07BattleshipScene
    ALIAS = 'battleship'
    TITLE = 'Линкор Принц Уэльский'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Trent, ru="Мне нужна помощь! Дело государственной важности!", en="I need help! It's a matter of state importance!", delivery_en=performance.URGENT),
        VoiceLine(20, WalesBarman, ru="Хе... Прям-таки государственной. Тогда вам к представителю государства.", en="Heh... State importance, is it. Then you want a representative of the state.", delivery_en=performance.SARDONIC),
        VoiceLine(30, WalesBarman, ru="Вон там у нас офицер Дерси сидит, единственная и неповторимая.", en="Officer Darcy is sitting right over there. The one and only."),
        VoiceLine(40, Trent, ru="Меня зовут Трент. Я работаю на секретную организацию, связанную с Орденом и мне срочно нужно с ней связаться.", en="My name is Trent. I work for a secret organization connected to the Order, and I urgently need to contact it.", delivery_en=performance.URGENT),
        VoiceLine(50, Darcy, ru="Еще один... Эй, мистер, ты у меня уже третий агент Ордена на неделе.", en="Another one... Hey, mister, you're already my third Order agent this week.", delivery_en=performance.SARDONIC),
        VoiceLine(70, Darcy, ru="Сейчас сидят в камере и ждут своей участи. Хочешь составить им компанию?", en="They're sitting in a cell right now, waiting for their fate. Want to keep them company?", delivery_en=performance.THREATENING),
        VoiceLine(80, Trent, ru="Я хочу доставить артефакт особой важности в штаб-квартиру нашей организации как можно быстрее. ", en="I want to deliver an artifact of special importance to our organization's headquarters as quickly as possible.", delivery_en=performance.URGENT),
        VoiceLine(90, Trent, ru="Иначе с меня шкуру спустят, а потом, возможно, и с вас. Кстати, об артефактах.", en="Otherwise they'll skin me, and then maybe you too. Speaking of the artifacts.", delivery_en=performance.URGENT),
        VoiceLine(100, Darcy, ru="О как... Впечатляет.", en="Oh my... Impressive.", delivery_en=performance.SHOCKED),
        VoiceLine(110, Darcy, ru="А откуда мне знать что эта штука не из какой-нибудь сувенирной лавки для туристов?", en="And how am I supposed to know this thing isn't from some souvenir shop for tourists?", delivery_en=performance.SARDONIC),
        VoiceLine(120, Trent, ru="Черт побери...", en="Damn it...", delivery_en=performance.ANGRY),
        VoiceLine(130, Darcy, ru="Ладно, есть у меня знакомый специалист по разным редкостям.", en="All right, I know a specialist in various rarities."),
        VoiceLine(140, Darcy, ru="Пусть он взглянет на эту штуку и если ты говоришь правду, то я постараюсь помочь чем смогу.", en="Let him take a look at this thing, and if you're telling the truth, I'll try to help however I can.", delivery_en=performance.REASSURING),
        VoiceLine(150, Darcy, ru="Если же это все-таки сувенир, то отправишь в камеру к тем ребятам из Ордена!", en="But if it is a souvenir after all, you'll go to the cell with those guys from the Order!", delivery_en=performance.THREATENING),

        VoiceLine(160, Trent, ru="Есть проблема. У меня на корабле сгорела почти вся электроника, даже и не знаю как смог сюда добраться живым.",
                  en="There's a problem. Almost all the electronics on my ship are fried. I don't even know how I made it here alive.", delivery_en=performance.WEARY),
        VoiceLine(170, Darcy, ru="(после долгого молчания и закатывания глаз) Хорошо, я дам вам один из наших кораблей",
                  en="(after a long silence and an eye roll) All right, I'll give you one of our ships.", delivery_en=performance.WEARY),
        VoiceLine(180, Darcy, ru="(угрожающе) Но если захотите на нем смыться, имейте ввиду, что все наши корабли оборудованы маячками слежения, так что я вас найду где угодно.",
                  en="(threateningly) But if you're thinking of taking off with it, keep in mind that all our ships have tracking beacons. I'll find you wherever you go.", delivery_en=performance.THREATENING),
    ]


class Msn7CheckArtifact(Msn7, script.CutsceneProps):
    THORN_CLASS = m07_check_artifact.M07CheckArtifactScene
    ALIAS = 'check_artifact'
    TITLE = 'Проверка артефакта'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Trent, ru="Ничего себе. Похоже, у этого парня очень разносторонние интересы.", en="Wow. Looks like this guy has very wide-ranging interests.", delivery_en=performance.TEASING),
        VoiceLine(20, Jabba, ru="Я интересуюсь редкими вещами, которые можно выгодно купить и еще более выгодно продать.", en="Some may call this junk. Me, I call them treasures.", delivery_en=performance.PROUD),
        VoiceLine(30, Jabba, ru="Привет, Дерси.", en="Hi, Darcy.", delivery_en=performance.WARM),
        VoiceLine(40, Darcy, ru="Привет Джабба. Я хочу, чтобы ты взглянул на одну вещицу.", en="Hi, Jabba. I want you to take a look at a little item.", delivery_en=performance.WARM),
        VoiceLine(50, Jabba, ru="Ух ты! Весьма интересная вещица, явно инопланетного происхождения. ", en="Whoa! Quite an interesting little item. Clearly of alien origin.", delivery_en=performance.EXCITED),
        VoiceLine(60, Jabba, ru="Если вы, вдруг, на мели готов дать вам за нее десять тысяч прямо сейчас.", en="If you happen to be broke, I'm ready to give you ten thousand for it right now."),
        VoiceLine(70, Darcy, ru="Вот дерьмо... Попила пивка в баре, нечего сказать. Ладно, Трент, уходим.", en="Well, shit... Had a beer at the bar, what can you say. All right, Trent, we're leaving.", delivery=HIGH_PITCH_NOT_FAST, delivery_en=performance.SARDONIC),
        VoiceLine(80, Darcy, ru="Джабба, ты же не дурак да? Ты же будешь держать язык за зубами?", en="Jabba, you're not a fool, right? You'll keep your mouth shut?", delivery_en=performance.THREATENING),
        VoiceLine(90, Jabba, ru="Само собой, Дерси, само собой.", en="Of course, Darcy, of course.", delivery_en=performance.UNCERTAIN),
    ]


class Msn7Reward(Msn7, script.CutsceneProps):
    THORN_CLASS = m07_reward.M07RewardScene
    ALIAS = 'reward'
    TITLE = 'Вознаграждение'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Darcy, ru="Спасибо, Трент. Я понимаю что долг платежом красен, но чуть попозже, хорошо? Оказывается этот урод далеко не всегда «покупал» свои вещички.", en="Thank you, Trent. I know one good turn deserves another, but a little later, all right? Turns out this bastard didn't always \"buy\" his little things.", delivery_en=performance.WARM),
        VoiceLine(20, Darcy, ru="С особо несговорчивыми покупателями ему помогали те самые ребятки, которых мы сожгли рядом со станцией. Нам надо с этим всем разобраться...", en="With the especially stubborn buyers, he had help from those same guys we burned near the station. We need to sort all this out...", delivery_en=performance.DISGUSTED),
        VoiceLine(50, Darcy, ru="Я выплачу бонус за твою работу. До скорого, Трент.", en="I'll pay a bonus for your work. See you soon, Trent.", delivery_en=performance.WARM),
        VoiceLine(60, Trent, ru="Постарайтесь побыстрее, Дерси.", en="Try to be quicker, Darcy.", delivery_en=performance.WEARY),
    ]


class Msn7TauArrival(Msn7, script.CutsceneProps):
    THORN_CLASS = m07_tau_arrival.M07TauArrivalScene
    ALIAS = 'tau_arrival'
    TITLE = 'm07_tau_arrival'
    DESCRIPTION = ''

class Msn7Space(Msn7, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(10, Trent, ru='Я тут каких-то гопников раскидал, но Железного Зада среди них не было.',
							 en="I took out some punks here, but Iron Ass wasn't among them."),
        VoiceLine(20, CorsairBarman,
                  ru='Айронсайда, мистер Трент, Билла Айронсайда. Если его не было здесь, попробуйте во втором вероятном месте его пребывания. Скидываю координаты.',
				  en="Ironside, Mr. Trent. Bill Ironside. If he wasn't here, try the second likely place he might be. Sending coordinates.", delivery_en=performance.DRY),

        VoiceLine(2000, CorsairBarman,
                  ru='Координаты последнего местоположения бандитов Старлайна в вашей нейросети. Возможно, Билл Айронсайд там. Разыщите его.',
                  en="The coordinates of the Starline bandits' last location are in your neural net. Bill Ironside may be there. Find him."),
        VoiceLine(2010, CorsairBarman,
                  ru='Айронсайд убит, теперь эти ублюдки нас долго не побеспокоят. Пересылаю ваше вознаграждение. Конец связи.',
                  en="Ironside is dead. Now these bastards won't bother us for a long time. Transferring your reward. End of transmission."),

        VoiceLine(30, Trent, ru='Сколько сколько прилетело? 500 кредитов? Они тут совсем охренели?',
							 en="How much came in? 500 credits? Have they completely lost it?", delivery_en=performance.ANGRY),
        VoiceLine(35, Trent,
                  ru='Проще было вообще перевод не делать - на банковской комиссии больше потеряли. Стоит, пожалуй, еще пару вопросов этому бармену задать. Например, "где деньги, Лебовски?".',
				  en="It would've been easier not to make the transfer at all. They lost more on the bank fee. I should probably ask that barman a couple more questions. For example, \"where's the money, Lebowski?\".", delivery_en=performance.SARDONIC),
        VoiceLine(40, RockfordStation,
                  ru='Мистер Трент, меня зовут Р+окфорд, СБА прислало меня пом+очь вам в поиске артефактов. Жду вас в баре на планете Мальта. Прошу вас быть как можно скорее, счет идет на секунды.',
				  en="Mr. Trent, my name is Rockford. The ASF sent me to help you search for the artifacts. I'm waiting for you at the bar on planet Malta. Please get here as soon as you can. Time is counted in seconds.", delivery_en=performance.URGENT),
        VoiceLine(60, Rockford, ru='Трент, жить хочешь? Помогай!', en="Trent, want to live? Help!", delivery_en=performance.URGENT),
        VoiceLine(70, Rockford,
                  ru='Трент, теперь летим в торговую линию! Нам нужно добраться до Малого Омикрона.',
				  en="Trent, now we fly into the trade lane! We need to get to Omicron Minor.", delivery_en=performance.URGENT),
        VoiceLine(80, Trent, ru='Приятно познакомиться, мистер Рокфорд.', en="Pleased to meet you, Mr. Rockford.", delivery_en=performance.SARDONIC),
        VoiceLine(90, Rockford, ru='Не мистер. Просто Р+окфорд.', en="Not 'Mister'. Just Rockford."),
        VoiceLine(100, Trent, ru='Кто были все эти люди, Рокфорд?', en="Who were all those people, Rockford?"),
        VoiceLine(110, Rockford, ru='Агенты Ордена.', en="Order agents."),
        VoiceLine(120, Trent, ru='А можно поподробнее?', en="And in a bit more detail?"),
        VoiceLine(130, Rockford, ru='О чём?', en="About what?"),
        VoiceLine(140, Trent, ru='Вообще о многом. Если вкратце, кто вы и во что я в очередной раз вляпался.',
							  en="About a lot of things, actually. In short, who are you, and what have I gotten into this time."),
        VoiceLine(150, Rockford,
                  ru='Я агент СБА Р+окфорд и меня прислали на помощь группе Дельта и вам, Трент, потому что вы вляпались в неприятности.',
				  en="I'm ASF agent Rockford, and I was sent to help Delta group and you, Trent, because you've gotten into trouble."),
        VoiceLine(160, Trent,
                  ru='Да твою же налево... Хорошо, тогда расскажите более развернуто, как вы меня нашли, почему вас, то есть нас на Мальте ждали, и что вообще мы теперь планируем делать.',
				  en="Oh, for fuck's sake... All right, then tell me in more detail how you found me, why they were waiting for you, that is, for us, on Malta, and what we're planning to do now.", delivery_en=performance.ANGRY),
        VoiceLine(170, Rockford,
                  ru='Когда я прибыл в систему Мальта, я вышел на связь с лидером Дельта и узнал от него о сложившейся ситуации и о том, что боеспособный корабль остался только у вас.',
				  en="When I arrived in the Malta system, I made contact with the Delta leader and learned from him about the situation, and that a combat-capable ship was left only with you."),
        VoiceLine(180, Rockford,
                  ru='Я отследил все взятые в этой системе фрилансерами контракты и определил ваше местонахождение. Кстати, Трент, вы действительно готовы работать за такие грош+и?',
				  en="I tracked every contract freelancers took in this system and found your location. By the way, Trent, are you really willing to work for pennies like that?", delivery_en=performance.TEASING),
        VoiceLine(190, Trent, ru='Не будем об этом. Что было дальше?', en="Let's not talk about that. What happened next?", delivery_en=performance.STERN),
        VoiceLine(200, Rockford,
                  ru='Я знал что за вами следят агенты Ордена. Кроме того, они подозревали о моем присутствии в системе.',
				  en="I knew Order agents were following you. Besides that, they suspected I was in the system."),
        VoiceLine(210, Rockford,
                  ru='Поэтому я решил устроить им ловушку и послал вам сообщение с просьбой о встрече в максимально удаленной от их главных сил точке - на планете Мальта.',
				  en="So I decided to set a trap for them, and sent you a message asking to meet at the point farthest from their main forces, on planet Malta."),
        VoiceLine(220, Rockford,
                  ru='Они смогли отправить на Мальту только небольшую группу перехвата, а мы с вами, Трент смогли ее уничтожить. Насчет того, что делать дальше, по-моему очевидно, забирать артефакты.',
				  en="They were able to send only a small interception group to Malta, and you and I, Trent, were able to destroy it. As for what to do next, I think it's obvious: take the artifacts."),
        VoiceLine(230, Trent, ru='И у нас уже есть план?', en="And we already have a plan?"),
        VoiceLine(240, Rockford, ru='Конечно. Как можно лететь куда-то без плана?', en="Of course. How can you fly somewhere without a plan?"),
        VoiceLine(250, Trent, ru='Меня в него не посветите?', en="Won't you let me in on it?"),
        VoiceLine(260, Rockford,
                  ru='Артефакты содержатся на базе Тортуга в системе Малый Омикрон. Формально это пиратская база, но она используется агентами Ордена и поэтому отлично защищена.',
				  en="The artifacts are held at Tortuga base in the Omicron Minor system. Formally it's a pirate base, but it's used by Order agents, and so it's well protected."),
        VoiceLine(270, Rockford,
                  ru='На станции находится передатчик, обеспечивающий постоянную двустороннюю связь со штабом Ордена.',
				  en="There's a transmitter on the station that keeps a constant two-way link with Order headquarters."),
        VoiceLine(280, Rockford,
                  ru='Если передатчик будет выведен из строя, по протоколу они обязаны эвакуировать все важные объекты на ближайшую другую базу. Мы разрушим передатчик и нападем на конвой, перевозящий артефакты.',
				  en="If the transmitter is put out of action, by protocol they have to evacuate all important objects to the nearest other base. We'll destroy the transmitter and attack the convoy carrying the artifacts."),
        VoiceLine(290, Trent, ru='Эмм... Ну ты у нас тут специалист, тебе виднее.', en="Umm... Well, you're the specialist here. You know better.", delivery_en=performance.UNCERTAIN),
        VoiceLine(310, Rockford,
                  ru='Сейчас я сброшу контейнеры с зарядами направленного действия. Подберите их, Трент, расположите вокруг передатчика и подорвите.',
				  en="I'll drop containers with shaped charges now. Pick them up, Trent, place them around the transmitter, and detonate them."),
        VoiceLine(320, Rockford,
                  ru='Устанавливайте заряды с выключенным щитом, иначе они сдетонируют. Координаты передатчика в вашем компьютере. Вперед!',
				  en="Set the charges with your shield off, or they'll detonate. The transmitter coordinates are in your computer. Forward!"),
        VoiceLine(330, Tortuga, ru='Фрилансер альфа-один, немедленно покиньте запретную зону...', en="Freelancer alpha-one, leave the restricted zone immediately..."),
        VoiceLine(340, Tortuga,
                  ru='Фрилансер альфа-один, если вы не покинете зону, мы будем вынуждены активировать защитный периметр!',
				  en="Freelancer alpha-one, if you don't leave the zone, we will be forced to activate the defensive perimeter!", delivery_en=performance.THREATENING),
        VoiceLine(350, Trent, ru='Готово. Передатчик уничтожен.', en="It's done. The transmitter is destroyed."),
        VoiceLine(355, Rockford, ru='Я заметил. Судя по переговорам вся станция на ушах сто+ит. Теперь посм+отрим, что они сделают.',
								 en="I noticed. Judging by the comms, the whole station is in an uproar. Now let's see what they do."),
        VoiceLine(360, Rockford, ru='Вижу конвой выходящий из Тортуги. Направляюсь за ним. Передаю координаты.', en="I see a convoy leaving Tortuga. I'm heading after it. Transmitting coordinates."),
        VoiceLine(370, Rockford, ru='Перехватываю грузовик. Нужна помощь.', en="Intercepting the freighter. Need help.", delivery_en=performance.URGENT),

        VoiceLine(380, Rockford, ru='Трент, атакуй грузовик!', en="Trent, attack the freighter!", delivery_en=performance.URGENT),
        VoiceLine(390, Trent, ru='Щит грузовика просто непробиваем. Что делать то?', en="The freighter's shield is just impenetrable. So what do we do?", delivery_en=performance.UNCERTAIN),
        VoiceLine(395, Rockford,
                  ru='Трент, атакуй грузовик! Это сверхзащищённая модель, его щит неуязв+им. Но есть способ преодолеть эту защиту.',
				  en="Trent, attack the freighter! This is an ultra-protected model. Its shield is invulnerable. But there's a way to get past this defense.", delivery_en=performance.URGENT),
        VoiceLine(400, Rockford,
                  ru='Частое использование Электромагнитной пушки приведет к перегреву генераторов и отключению щита. Подлети ближе к транспорту, чтобы пилот мог по тебе стрелять.',
				  en="Frequent use of the electromagnetic cannon will overheat the generators and shut the shield off. Fly closer to the transport so the pilot can shoot at you."),
        VoiceLine(410, Trent, ru='В смысле? Быть приманкой?', en="What do you mean? Be bait?", delivery_en=performance.SHOCKED),
        VoiceLine(420, Rockford, ru='Да.', en="Yes.", delivery_en=performance.DRY),
        VoiceLine(430, Rockford, ru='Щит упал. Трент, уничтожь грузовик! Целься в уявзимые точки!', en="The shield is down. Trent, destroy the freighter! Aim at the vulnerable points!", delivery_en=performance.URGENT),
        VoiceLine(440, Rockford, ru='Они вызывают подкрепление. Скоро вся эта зона будет кишать пилотами Ордена. Уничтожь транспорт! Быстрее!',
								 en="They're calling reinforcements. Soon this whole zone will be swarming with Order pilots. Destroy the transport! Faster!", delivery_en=performance.URGENT),
        VoiceLine(445, Rockford, ru='Транспорт взорван, подбери артефакты!', en="The transport is blown up. Pick up the artifacts!", delivery_en=performance.URGENT),

        VoiceLine(450, Trent, ru='Это было потно. Куда теперь?', en="That was intense. Where to now?", delivery_en=performance.WEARY),
        VoiceLine(460, Rockford,
                  ru='У меня есть убежище в Омега-13. Проведем там обслуживание кораблей и разработаем план доставки артефактов в штаб СБА.',
				  en="I have a hideout in Omega-13. We'll service the ships there and work out a plan to deliver the artifacts to ASF headquarters."),
        VoiceLine(470, Trent,
                  ru='Звучит отлично! Веди. Кстати, а что попалось тебе? У меня какая-то мелочевка кочевников и том Протея... Значит ключ у тебя?',
				  en="Sounds great! Lead on. By the way, what did you get? I've got some Nomad odds and ends and the Proteus Tome... So the key is with you?", delivery_en=performance.RELIEVED),
        VoiceLine(480, Rockford, ru='Да.', en="Yes."),

        VoiceLine(490, Trent,
                  ru='Кстати, Рокфорд, а почему тебя так хотят убить агенты Ордена? Стоило тебе выйти на связь и на место встречи прибыла целая армия.',
				  en="By the way, Rockford, why do the Order agents want to kill you so badly? The moment you made contact, a whole army showed up at the meeting place."),
        VoiceLine(495, Rockford,
                  ru='Я был агентом еще старого, большого Ордена. Я слишком много знаю. С момента раскола постоянно приходится спать вполглаза.',
				  en="I was an agent of the old, big Order. I know too much. Since the split, I've constantly had to sleep with one eye open.", delivery_en=performance.SOMBRE),
        VoiceLine(498, Rockford, ru='Даже сейчас нужно держать ухо в остро. Мы можем нарваться на патруль в любой момент', en="Even now, we have to stay sharp. We could run into a patrol at any moment.", delivery_en=performance.CONCERNED),

        VoiceLine(500, Trent, ru='Нужно добраться до ближайшей базы.', en="We need to get to the nearest base."),
        VoiceLine(510, Darcy, ru='Давай, тайный агент, залетай в торговую линию. Тут лететь не далеко.', en="Come on, secret agent, get into the trade lane. It's not a long flight from here.", delivery_en=performance.TEASING),
        VoiceLine(520, Darcy, ru='Ты там особо с ним не откровенничай. Эта личность чрезвычайно мутная.', en="Don't get too open with him there. This character is extremely shady.", delivery_en=performance.CONCERNED),
        VoiceLine(530, Darcy,
                  ru='Он часто бывает нам полезен, поэтому мы закрываем глаза на его мелкие шалости. И чует мое сердце, что до поры до времени. Когда-нибудь он нарвется.',
				  en="He's often useful to us, so we turn a blind eye to his little pranks. And my heart tells me that's only for the time being. One day he'll push it too far.", delivery_en=performance.CONCERNED),
        VoiceLine(550, JabbaBandit, ru='Фрилансер, у тебя есть кое-что что, что очень нужно нам. Отдавай по-хорошему!', en="Freelancer, you've got something we really need. Hand it over the nice way!", cinematic=True, delivery_en=performance.THREATENING),
        VoiceLine(560, Darcy,
                  ru='Мальчики, а вы не охренели? Это мой участок, я здесь главный коп. Трент, давай разберем эту шпану.',
				  en="Boys, have you lost your minds? This is my beat. I'm the head cop here. Trent, let's take this rabble apart.",
                  cinematic=True, delivery_en=performance.COMMAND),
        VoiceLine(570, Darcy,
                  ru='Джабба, засранец, теперь ты точно доигрался. Трент, я вернусь, поговорю с нашим другом еще раз. Увидимся в лавке Джаббы.',
				  en="Jabba, you asshole, now you've really played it out. Trent, I'll be back. I'll talk to our friend again. See you at Jabba's shop.", delivery_en=performance.ANGRY),
    ]

class Mission7(Msn7, script.StoryMission):
    MISSION_INDEX = 7
    CUTSCENES = [
        Msn7TauArrival,
        Msn7Offer,
        Msn7Cadiz,
        Msn7Omega13,
        Msn7Battleship,
        Msn7CheckArtifact,
        Msn7Reward,
    ]
    SPACE_CLASS = Msn7Space
    SYNC_SPACE = True
    SYNC_SUBS = True

    MISSION_TITLE = 'Миссия 7. Возвращение артефактов'