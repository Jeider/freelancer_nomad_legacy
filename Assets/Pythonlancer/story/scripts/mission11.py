from story import script
from audio.sound import VoiceLine
from story.actors import Trent, Kim, Rockford, Yamamoto, KusariCaptain, Reichman, EdisonTrent, Hatcher, Darcy, Alaric
from story.cutscenes.story_scenes import m11_ambush, m11_drink


class Msn11(object):
    MISSION_INDEX = 11


class Msn11AmbushCutscene(Msn11, script.CutsceneProps):
    ALIAS = 'ambush'
    TITLE = 'Бар станции Харадзюку'
    THORN_CLASS = m11_ambush.Msn11AmbushScene
    DESCRIPTION = 'Трент подходит к столику Рокфорда'
    VOICE_LINES = [
        VoiceLine(
            10,
            Trent,
            ru='Рокфорд!',
               en='Rockford!'
        ),
        VoiceLine(
            30,
            Rockford,
            ru='(Реально удивлённо) Трент?... Да, конечно, присаживайтесь.',
               en='Trent?! Yeah, of course... have a seat...'
        ),
        VoiceLine(
            40,
            Trent,
            ru='(Ультиматум) Рокфорд, отдай номадский ключ.',
               en='Rockford, give me the Nomad key!'
        ),
        VoiceLine(
            50,
            Rockford,
            ru='(Кладёт КПК на стол) Зачем? Чтобы ты отдал его СБА? Или Ордену? Или на кого ты сейчас работаешь?',
               en='Why? So you can hand it over to the ASF? Or The Order? Who are you even working for these days?'
        ),

        VoiceLine(
            60,
            Trent,
            comment='Попытки уговорить со стороны Трента',
            ru='Эти артефакты обладают слишком большой разрушительной силой, и если они попадут не в те руки...',
               en='These artifacts possess too much destructive power. If they fall into the wrong hands...'
        ),
        VoiceLine(
            70,
            Trent,
            ru='Один псих по фамилии Т+илтон так недавно чуть не устроил локальный конец света в Тау-44. '
               'Они должн+ы находиться под присмотром таких организаций как СБА или Орден.',
               en='One lunatic named Tilton almost caused a local apocalypse in Tau-44 not long ago.'
                  'They must be under the supervision of organizations such as the ASF or The Order.'
        ),

        VoiceLine(
            80,
            Rockford,
            comment='Гигантский философский мегадиалог, скорее ближе к "суперзлодей рассказывает суперплан"',
            ru='А что ты вообще знаешь про Орден и СБА? И от кого?',
               en='And what do you REALLY know about The Order and the ASF? And who told you?'
        ),
        VoiceLine(
            90,
            Rockford,
            ru='Торговля артефактами давно стала прибыльным бизнесом. И не самым опасным, надо сказать.',
               en='Trading artifacts has been a profitable business for a long time. And not the most dangerous one, I might add.'
        ),
        VoiceLine(
            100,
            Rockford,
            ru='А в отсутствии внешней угрозы эти структуры начали заниматься борьбой за власть.',
               en=' In the absence of an external threat, these organizations have turned to fighting for power.'
        ),
        VoiceLine(
            110,
            Rockford,
            ru='За власть глобальную, позволяющую не считаться с правительствами. '
               'И ключ номадов, том Пр+отеуса и прочее - в этой игре не больше чем козыри.',
               en='For GLOBAL power, the kind that lets them ignore governments.'
                  'The Nomad Key, the Proteus Tome, and the rest... in this game, they\'re nothing more than bargaining chips.'
        ),
        VoiceLine(
            120,
            Rockford,
            ru='И если возникнет необходимость, ни СБА, ни Орден не остановится перед тем чтобы применить их '
               'и устроить, как ты выразился, локальный конец света, например, в системе Форбс.',
               en='And if the need arises, neither the ASF nor The Order will hesitate to use them'
                  'and cause, as you put it, a local apocalypse... in, say, the Forbes system.'
        ),

        VoiceLine(
            130,
            Trent,
            comment='Трент удивляется, сколько всего сейчас выпалил Рокфорд',
            ru='Ого... Р+окфорд, ты сейчас произнес больше слов,, чем за всё время нашего знакомства.',
               en='Wow... Rockford, you just said more words than in our entire acquaintance up to this point.'
        ),

        VoiceLine(
            150,
            Rockford,
            ru='Все эти р+ейнландцы, СБА - не более, чем дети, играющие в песочнице найденной боевой гранатой.',
               en='All these Rheinlanders, the ASF... they are nothing more than children in a sandbox, playing with a live grenade they found.'
        ),
        VoiceLine(
            160,
            Rockford,
            ru='И вот,, им уже стало интересно, что будет, если выдернуть это колечко.',
               en='And now they\'ve grown curious about what happens if you pull the pin.'
        ),
        VoiceLine(
            170,
            Rockford,
            ru='А я знаю, как все это прекратить. Сейчас. Раз и навсегда.',
               en='But I know how to end this. Right now. Once and for all.'
        ),
        VoiceLine(
            180,
            Rockford,
            ru='В моём будущем не будет ни кочевников, ни их наследия. Только человечество. '
               'В полной безопасности от всего этого опасного мусора.',
               en='In my future, there will be no Nomads. Or the Nomad Legacy. Only humanity.'
                  'Perfectly safe from all this dangerous garbage.'
        ),

        VoiceLine(
            200,
            Rockford,
            comment='Трент лишь офигевающе хлопает ушами',
            ru='(Давай вместе править Галактикой) Не хочешь пом+очь мне создать такой мир?...',
               en='Don\'t you want to help me build that world?'
        ),

        VoiceLine(
            205,
            Trent,
            ru='Я-а... Не знаю-у... О чём вообще речь?',
               en='I... I don\'t know... What are you even talking about?'
        ),

        VoiceLine(
            210,
            Rockford,
            ru='(Смеясь, сматывает удочки) Они даже тебе не сказали... Забавно.',
               en='They didn\'t even tell you... How amusing.'
        ),
        VoiceLine(
            220,
            Rockford,
            ru='(Грозно) Хотя бы не мешайся у меня под ногами, Трент. Мое почтение.',
               en='Then at least stay out of my way, Trent. My regards.'
        ),

        VoiceLine(
            230,
            Trent,
            comment='Через пару мгновений ожидания до Трента доходит',
            ru='Какая же это всё херн+я, какой смысл...',
               en='Oh, what is all this garbage, what\'s the point?'
        ),

        VoiceLine(
            250,
            Trent,
            comment='Через пару мгновений ожидания до Трента доходит',
            ru='Чёрт... Сообщения от Кима н+е было!',
               en='Damn it... There\'s been no message from Kym!'
        ),
        VoiceLine(
            260,
            Kim,
            comment='Звонок с КПК',
            ru='(Панически кричит) Трент, Рокфорд уходит, скорее взлетаем!',
               en='Trent, Rockford is getting away! Get to your ship, now!'
        ),
        VoiceLine(
            270,
            Trent,
            ru='А что с нашими?',
               en='What about our team?'
        ),
        VoiceLine(
            280,
            Kim,
            ru='Их убили...',
               en='They\'re dead...'
        ),
        VoiceLine(
            290,
            Trent,
            ru='Вот чёрт...',
               en='God damn it...'
        ),

    ]


class Msn11DrinkCutscene(Msn11, script.CutsceneProps):
    ALIAS = 'drink'
    TITLE = 'Бар линкора Мусаси'
    THORN_CLASS = m11_drink.Msn11DrinkScene
    DESCRIPTION = 'Трент хотел было набухаться от своих неуспехов, как тут к нему приходит "Старый" Трент...'
    VOICE_LINES = [

        VoiceLine(10, Trent, ru='Ким, что случилось с Ямамото? Р+айхманн сдавался. Откуда столько ненависти?',
                  en='Kym, what happened with Yamamoto? Reichmann was surrendering. Where did all that hatred come from?'),
        VoiceLine(20, Trent, ru='(Охеревающий) А Вавил+он? Почему он так плохо охранялся? Где линкоры, тучи истребителей?..',
                  en='And Babylon? Why was it so poorly guarded? Where were the battleships, the swarms of fighters?'),
        VoiceLine(30, Trent, ru='(Финально) Ким, ты можешь мне ответить?!!',
                  en='Kym, can you even answer me?!'),

        VoiceLine(40, Kim, ru='(Громкое "Я" с желанием вскрикнуть, вдох и... тихое нет на выдохе...) Я... Нет... Пока нет',
                  en='Me... Not... I can\'t... Not yet... '),
        VoiceLine(50, Kim, ru='Так знаешь, давай остынь. Скоро будет дело. Выдыхай. Я скоро выйду на связь.',
                  en='Look. You know what, just cool off. We\'ll have work to do soon. Take a breath. I\'ll be in touch.'),

        VoiceLine(60, Trent, ru='Ладно, гуляй себе', en='Fine... Do what you want...'),

        VoiceLine(110, EdisonTrent, ru='Неудачный день?', en='Having a bad day?'),
        VoiceLine(120, Trent, ru='Неудачная жизнь.', en='Having a bad life.'),
        VoiceLine(130, EdisonTrent, ru='Хм. А по мне так тебе сказочно везет. Да и с Р+окфордом у тебя почти получилось.',
                  en='For me you\'re incredibly lucky. And you almost done with Rockford.'),
        VoiceLine(140, Trent, ru='Я устал, нет серьезно, достало всё. Берешь простой заказ, а тебе вместе с оплатой впаривают человека, которому ну просто необходимо пом+очь.', en='I\'m so tired. Seriously, I\'ve had enough. You take a simple job, and it comes with a side of some guy who desperately needs your help.'),
        VoiceLine(150, Trent, ru='Он обещает тебе златые горы - и вот, трах-бах, и ты уже поуши увяз в интригах спецслужб, и за твою голову назначена неплохая такая цена.',
                  en='He promises you the world—and then, bam! You\'re neck-deep in some intelligence agency mess with a hefty bounty on your head.'),
        VoiceLine(160, Trent, ru='И ты пытаешься из всего этого выпутаться, но вместо этого запутываешься еще больше.',
                  en='And you try to find your way out of this mess, but you only dig yourself a deeper hole.'),
        VoiceLine(170, Trent, ru='И в конце концов, ты уже не понимаешь за кого и против кого ты, а самое главное - зачем это всё?',
                  en='In the end, you can\'t even tell friend from foe anymore. And the most important question is: what\'s the damn point of it all?'),

        VoiceLine(180, EdisonTrent, ru='Так всегда и бывает,, тёзка, ты же фрилансер. Либо ты отстреливаешь мелких бандюков в свободных мир+ах, летая на ржавом корыте и получаешь за это копейки. Либо вот так...',
                  en='That\'s how it always is, namesake. You\'re a freelancer. You either take the small jobs: popping two-bit thugs in the outer systems, flying a rusty can for scrap wages... Or you end up in a mess like this.'),
        VoiceLine(190, EdisonTrent, ru='И считай,, тебе  повезло. Сумма у тебя на счету с шестью нулями? Летаешь ты на чём? На самом новом, под тебя тюнингованном? Обвес у тебя из самого нового оружия?', en='And you know what? You got lucky. That credit balance of yours hitting six figures? What\'s your ride? Some brand-new, tricked-out ship, made just for you? Top-of-the-line weapons on every hardpoint!'),
        VoiceLine(200, EdisonTrent, ru='А если тебе нужно чего для корабля докупить, ты же даже в счет не заглядываешь - и так знаешь, что хватит, и еще останется.', en='And if you need to buy anything for your ship, you don\'t even bother checking the balance—you just know it\'s enough, and there\'ll be plenty left.'),
        VoiceLine(210, EdisonTrent, ru='И,, самое главное, врагов,, у тебя конечно становится всё больше и больше, но у тебя появляются друзья.',
            en='And most importantly... sure, you\'ve got more and more enemies. But you\'ve also made friends.'),
        VoiceLine(220, EdisonTrent, ru='Их немного, гораздо меньше чем врагов, но они настоящие, потому что испытаны боем, прошли огонь,, воду,, и медные трубы вместе с тобой.', en='Not many, far fewer than the enemies. But they\'re real. Tested in battle. They\'ve been through hell and high water with you.'),
        VoiceLine(230, EdisonTrent, ru='И ты уверен, что бы ни случилось, на них можно положиться. И вот эти друзья, они на самом деле намного ценнее, чем шестизначный счет или новейший корабль с лучшим обвесом.',
            en='And you know, no matter what happens, you can count on them. And these friends... they\'re actually worth far more than any six-figure account or a state-of-the-art ship with the best gear.'),
        VoiceLine(240, EdisonTrent, ru='Вот так. А пожалеть себя иногда очень хочется, по себе знаю. Главное не злоупотреблять этим - вредно для формы.',
            en='That\'s how it is. And feeling sorry for yourself is a powerful temptation, I know that firsthand. The trick is not to make a habit of it—it\'s bad for your edge.'),

        VoiceLine(250, Trent, ru='И вы мне не позволите,, да?', en='You won\'t let me, will you?'),
        VoiceLine(260, EdisonTrent, ru='Я лишь обрисую ситуацию, а ты сам решай...', en='I\'ll give you the facts. You call the shot...'),
        VoiceLine(270, Trent, ru='Слушаю внимательно.', en='I\'m all ears.'),
        VoiceLine(280, EdisonTrent, ru='Не здесь. Нам нужно лететь. Расскажу всё по дороге.', en='Not here. We have to fly. I\'ll fill you in on the journey.'),
    ]


class Msn11Space(Msn11, script.SpaceVoiceProps):
    VOICE_LINES = [

        VoiceLine(
            10,
            Kim,
            ru='Мистер Трент, Р+окфорд сейчас находится в баре станции Харадзюку. ',
               en='Mister Trent, Rockford is currently in the bar on Harajuku Station.'
        ),
        VoiceLine(
            15,
            Kim,
            ru='Отвлеките его, чтобы наши ребята могли начать работу с его кораблем.',
               en='Distract him so our guys can start working on his ship.'
        ),
        VoiceLine(
            20,
            Trent,
            ru='И как вы это себе представляете?',
               en='And how do you imagine this is going to work?'
        ),
        VoiceLine(
            30,
            Kim,
            ru='Придумайте что-нибудь. Мне напомнить вам, как недавно несколько десятков пилотов вылетели в один конец, чтобы обеспечить ваше прикрытие?',
               en='Improvise something. Do I need to remind you how dozens of pilots recently flew a one-way mission to provide you with cover?'
        ),
        VoiceLine(
            40,
            Trent,
            ru='Ладно, значит я после посадки сразу иду в бар?',
               en='Alright, so I head straight to the bar after docking?'
        ),
        VoiceLine(
            50,
            Kim,
            ru='Да, а мы тут сразу займемся д+елом. Когда наши специалисты закончат, я пришлю вам сообщение на коммуникатор.',
               en='Yes, and we\'ll get to work here immediately. Once our specialists are done, I\'ll send a message to your communicator.'
        ),

        VoiceLine(
            60,
            Kim,
            comment='После вылета с Харадзюку',
            ru='Р+окфорд еще на радаре, мы еще можем его нагнать.',
               en='Rockford is still on our scanners, we can still catch him.'
        ),

        VoiceLine(
            65,
            Yamamoto,
            comment='Связь с Ямамото',
            ru='Ямамото на связи.',
               en='Yamamoto here.'
        ),
        VoiceLine(
            70,
            Kim,
            ru='Заминировать корабль Р+окфорда не удалось. Сейчас ведем погоню...',
               en='Mining Rockford\'s ship has failed. We are in pursuit...'
        ),
        VoiceLine(
            80,
            Yamamoto,
            ru='Станция "Вавилон" атакована силами Р+ейнланда! Всем немедленно выдвинуться на защиту!',
               en='Station Babylon is under attack by Rheinland forces! All units, proceed to its defense immediately!'
        ),
        VoiceLine(
            90,
            Kim,
            ru='О, Цха! Трент, наш штаб атакован, срочно летим на защиту. Даю координаты гиперврат.',
               en='Fuck! Trent, our headquarters is under attack, we\'re moving to defend it now. Sending you the hypergate coordinates.'
        ),
        VoiceLine(
            100,
            Trent,
            ru='А Р+окфорд уйдет...',
               en='But Rockford will get away...'
        ),
        VoiceLine(
            105,
            Kim,
            ru='Чёрт с ним. У нас серьезные проблемы в друг+ом месте.',
               en='To hell with him! We have serious problems elsewhere!'
        ),

        VoiceLine(
            110,
            Kim,
            comment='Появление в системе',
            ru='Мистер Трент, летите через туннель. Ваш доступ разрешен, защитные системы деактив+ированы.',
               en='Mister Trent, proceed through the tunnel. Your access is granted, defense systems are deactivated.'
        ),

        VoiceLine(
            120,
            Kim,
            comment='Выдвигаемся к станции Вавилон',
            ru='Это лейтенант Ким, оборона, доложите обстановку.',
               en='This is Lieutenant Kym to defense forces, report your status.'
        ),
        VoiceLine(
            125,
            KusariCaptain,
            ru='Враг находится во внутреннем периметре. Станция Вавилон атакована, требуется поддержка!',
               en='The enemy is inside the inner perimeter. Station Babylon is under attack, we require support!'
        ),
        VoiceLine(
            130,
            Kim,
            ru='Мы летим!',
               en='We\'re on our way!'
        ),

        VoiceLine(
            140,
            KusariCaptain,
            ru='Враг проник в станцию Вавилон!',
               en='The enemy has breached Babylon Station!'
        ),
        VoiceLine(
            150,
            Kim,
            ru='Дело очень плохо...',
               en='This is very bad...'
        ),
        VoiceLine(
            160,
            Trent,
            ru='Что стряслось?',
               en='What\'s happened?'
        ),
        VoiceLine(
            170,
            Kim,
            ru='На Вавилоне находятся архивы Ордена. Артефакты. Видимо Р+ейнландцы здесь за этим. Нужно их остановить',
               en='Babylon holds The Order\'s archives. The artifacts. It seems the Rheinlanders are here for them. We have to stop them!'
        ),

        VoiceLine(
            180,
            Kim,
            comment='Все диверсанты ликвидированы',
            ru='Кажется всё.',
               en='That seems to be all of them.'
        ),
        VoiceLine(
            190,
            KusariCaptain,
            ru='Говорит Вавилон, статус. Враг проник в главное хранилище и утащил номадское энергоядр+о.',
               en='Babylon here, status report. The enemy breached the main vault and stole the Nomad power core.'
        ),
        VoiceLine(
            200,
            Yamamoto,
            ru='Всеобщий приказ. Всем силам выдвинуться вслед за р+ейнландскими кораблями. Нельзя допустить того, что они заполучат энергоядр+о',
               en='General order. All forces are to pursue the Rheinland ships. We cannot allow them to secure the power core!'
        ),
        VoiceLine(
            210,
            Yamamoto,
            ru='Энергоядр+о было направлено на станцию Вена. Ударное звено и линкор Мус+аси уже выдвинулись. Ким, направляйтесь к Вене своим ходом.',
               en='The power core was tracked to Station Vienna. A strike wing and the battleship Musashi are already en route. Kym, proceed to Vienna by your own means.'
        ),
        VoiceLine(
            240,
            Kim,
            ru='Так точно, уже летим',
               en='Affirmative, we\'re already on our way!'
        ),

        VoiceLine(
            250,
            Trent,
            ru='На кой ляд Р+ейнландцам сдалось это энергоядр+о',
               en='Why the hell would the Rheinlanders even want that power core?'
        ),
        VoiceLine(
            260,
            Kim,
            ru='Ядр+о когда-то вынул твой тёзка из логова кочеников в ходе номадской войн+ы. Очень ценная и технологичная штука',
               en='The core was originally extracted by Edison Trent from the Nomad Lair during the Nomad War. It\'s an extremely valuable and advanced piece of technology.'
        ),
        VoiceLine(
            270,
            Trent,
            ru='Ах да. Логово кочевников. Я видел как с этими технологиями работали ребята из Л+иберти. Весьма взрывоопасная вещица',
               en='Oh right, the Nomad Lair. I\'ve seen how the Liberty guys worked with that kind of tech. It\'s a highly volatile thing!'
        ),
        VoiceLine(
            280,
            Kim,
            ru='Поэтому мы не дадим и шанса Р+ейнландцам воспользоваться ей',
               en='Which is exactly why we won\'t give the Rheinlanders a single chance to use it.'
        ),

        VoiceLine(
            290,
            Kim,
            comment='Рядом со станцией',
            ru='Так, Трент. Мы обнаружили сигнатуры в исследовательских контейнерах по периметру базы.',
               en='Alright, Trent. We\'ve detected signatures in the research containers around the base\'s perimeter.'
        ),
        VoiceLine(
            300,
            Kim,
            ru='Уничтожь эти контейнеры. Скорее всего ядр+о в одном из них',
               en='Destroy those containers. The core is likely in one of them.'
        ),
        VoiceLine(
            310,
            Trent,
            ru='А энергоядр+о мы этим не уничтожим?',
               en='But won\'t we destroy the core itself in the process?'
        ),
        VoiceLine(
            320,
            Kim,
            ru='Всё с ним будет хорошо, в наших лабораториях с ним и не такое вытворяли. Давай ищи, не мешкай',
               en='It\'ll be fine. Our labs have put it through worse. Now search, and don\'t dawdle!'
        ),

        VoiceLine(
            330,
            Yamamoto,
            comment='После уничтожения контейнеров',
            ru='Внимание, сигнатура генератора обнаружена на улетающем корабле! Срочно перехватить, пока он не ушел к гипердыре!',
               en='Attention! The core\'s signature is detected on a departing ship! Intercept it immediately, before it reaches the wormhole!'
        ),

        VoiceLine(
            340,
            Kim,
            ru='Трент, сделай что-нибудь!',
               en='Trent, do something!'
        ),

        VoiceLine(
            350,
            Trent,
            comment='Проигрывается катсцена. Корабль попадает в засаду и взрывается, а лут забирает Р+окфорд',
            ru='Чёрт, это Р+окфорд!',
               en='Damn, it\'s Rockford!'
        ),
        VoiceLine(
            360,
            Kim,
            ru='Он угоняет энергоядр+о!',
               en='He\'s stealing the power core!'
        ),
        VoiceLine(
            370,
            Yamamoto,
            ru='Останов+ите его!',
               en='Stop him!'
        ),
        VoiceLine(
            380,
            Trent,
            ru='Поздно, он скрылся',
               en='Too late, he\'s gone!'
        ),

        VoiceLine(
            390,
            Yamamoto,
            ru='(Ярость) Этого нельзя было допустить!',
               en='This is a catastrophic failure!'
        ),

        VoiceLine(
            400,
            Reichman,
            comment='Прибывает рейнландское подкрепление',
            ru='(Пока еще горделиво) Солдаты Ордена, с вами говорит адмирал Р+айхман!',
               en='Soldiers of The Order! This is Admiral Reichman speaking!'
        ),
        VoiceLine(
            410,
            Yamamoto,
            ru='(Яростная злоба) Р+айхман? Уничтожить его! Всем приказ атаковать линкор Гнейзенау!',
               en='Reichman? Destroy him! All units, attack the battleship Gneisenau!'
        ),

        VoiceLine(
            450,
            Reichman,
            comment='Линкор райхмана почти уничтожен',
            ru='(Паника) Мы сдаемся! Я сдаюсь! Ямам+ото!',
               en='We surrender! I surrender! Yamamoto!'
        ),


        VoiceLine(
            500,
            Yamamoto,
            ru='(Абсолютный гнев) Сдаешься? Ч+ёрта с два! Уничтожить линкор Гнейзенау!',
               en='Surrender? Like hell you do! Destroy the Gneisenau!'
        ),
        VoiceLine(
            510,
            Reichman,
            ru='Ямамото, я же сдался, грязный, ублюдок...',
               en='Yamamoto, I surrendered, you filthy bastard...'
        ),

        VoiceLine(
            520,
            Kim,
            comment='Линкор и флот рейнланда подавлены',
            ru='Все отряды Р+ейнланда прекратили сопротивление.',
               en='All Rheinland units have ceased resistance.'
        ),
        VoiceLine(
            530,
            Yamamoto,
            ru='(Злобный) Так гораздо лучше. Отправить призовую партию на Вену. Взять под конвой корабли Р+ейнланда.',
               en='Much better. Send a prize crew to Vienna. Take the Rheinland ships under escort.'
        ),
        VoiceLine(
            540,
            Yamamoto,
            ru='(Ярость) И если вы, герры сраные, только попробуете р+ыпнуться - проследуете за своим вонючим адмиралом.',
               en='And if you sorry Herren so much as twitch, you\'ll follow your stinking admiral!'
        ),

        VoiceLine(
            550,
            Kim,
            ru='Трент, садись на Мус+аси. Наша работа тут выполнена',
               en='Trent, dock with the Musashi. Our work here is done.'
        ),

        VoiceLine(1170, Trent, ru='Ну так, о чём речь.', en='So, what\'s the deal?'),

        VoiceLine(1180, EdisonTrent,
                  ru='Если коротко - то всё плохо. Р+окфорд, как ты понял, решил "спасти" всё человечество. И сейчас ни СБА ни Орден помешать ему уже не могут.',
                      en='The short version? Everything\'s gone to hell. Rockford, as you\'ve gathered, has decided to "save" all of humanity. And right now, neither the ASF nor The Order can stop him.'),
        VoiceLine(1190, EdisonTrent, ru='А вот у тебя учитывая твою патологическую везучесть, может и получиться.', en='But you, with your pathological luck, might just pull it off.'),

        VoiceLine(1200, Trent, ru='А кто такой вообще этот Р+окфорд?', en='But who is this Rockford guy, really?'),

        VoiceLine(1210, EdisonTrent,
                  ru='Один очень хороший человек, внезапно слетевший с катушек и задавшийся целью осчастливить человечество.',
                      en='He\'s a brilliant man who suddenly went off the deep end, hell-bent on fixing humanity.'),
        VoiceLine(1220, EdisonTrent,
                  ru='Проблема в том что в этом случае обычные клерки приносят в патентные бюро чертежи вечных двигателей, а вот фигуры масштаба Р+окфорда могут и уничтожить человечество, пока его же и спасает.',
                      en='The problem is, while most crackpots just bring blueprints for perpetual motion machines to a patent office, people like Rockford are capable of destroying humanity in their attempts to save it.'),

        VoiceLine(1230, Trent, ru='А поконкретнее?', en='Can you be more specific?'),

        VoiceLine(1240, EdisonTrent, ru='Аттикус Р+окфорд... великий и ужасный. Он - из ветеранов Ордена.', en='Atticus Rockford... the great and terrible. He\'s a veteran of The Order. '),
        VoiceLine(1250, EdisonTrent,
                  ru='Очень болезненно отнесся к тому что Орден не смог предотвратить экспансию кочевников во время того инцедента и занялся изучением артефактов - так называемого наследия кочевников.',
                      en='He took it very hard when The Order failed to prevent the Nomad incursion during the... incident. He threw himself into studying the artifacts—the so-called Nomad Legacy.'),
        VoiceLine(1260, EdisonTrent,
                  ru='Именно он обнаружил ту самую Сферу, и каким-то образом понял что она - своего рода ящик Панд+оры, и содержит в себе смертоносную силу.',
                      en='He was the one who discovered that Sphere, and somehow he understood that it was a kind of Pandora\'s box, containing a devastating power.'),
        VoiceLine(1270, EdisonTrent,
                  ru='Мы вместе работали над Сферой. Он нашел способ ее уничтожить, но руководство Ордена было категорически против.',
                      en='We worked on the Sphere together. He found a way to destroy it, but the Order\'s leadership was categorically against it.'),
        VoiceLine(1280, EdisonTrent,
                  ru='Тогда уже начал+а проявляться его маниакальность в достижении цели, а я понял, что ключ номадов сможет управлять сферой.',
                      en='hat\'s when his... manic obsession with his goal began to show. And I realized that the Nomad Key could control the Sphere.'),
        VoiceLine(1290, EdisonTrent,
                  ru='И решил удалиться подальше. Так что мое пленение кс+еносами было мною подстроено.',
                      en='So I decided to get as far away as possible. My capture by the Xenos was staged.'),

        VoiceLine(1300, Trent, ru='И что теперь делать? Ключ у Р+окфорда и он может делать со Сферой всё что захочет. И никто не сможет ему помешать.', en='So what do we do now? Rockford has the Key and can do whatever he wants with the Sphere. And no one can stop him.'),

        VoiceLine(1350, EdisonTrent,
                  ru='Не совсем так. Есть еще один ключ, я его забрал с собой, когда отправился к добровольное изгнание к Кс+еносам. Он абсолютно идентичен тому, что у Р+окфорда.',
                      en='Not quite. There is another Key. I took it with me when I went into voluntary exile with the Xenos. It\'s absolutely identical to the one Rockford has.'),
        VoiceLine(1360, Trent, ru='И что мне с ним делать?', en='And what am I supposed to do with it?'),
        VoiceLine(1370, EdisonTrent,
                  ru='Решать тебе, но я бы в лучшие свои годы собрал силы Ордена или СБА и полетел бы прямо к сфере, пытаясь остановить Р+окфорда, пока это еще возможно.',
                      en='That\'s your choice. But in my prime, I would have rallied the forces of The Order or the ASF and flown straight for the Sphere, trying to stop Rockford while there\'s still time.'),
        VoiceLine(1380, Trent,
                  ru='Тогда почему ты не сделаешь это сам? Почему я?', en='Then why don\'t you do it? Why me?'),

        VoiceLine(1390, EdisonTrent, ru='Потому что сейчас в данный момент у тебя больше друзей, чем у меня', en='Because right now, at this moment, you have more friends than I do.'),
        VoiceLine(1400, EdisonTrent, ru='В своё время утекло много вод+ы. Мне сейчас они не поверят. А тебе да. Так что ты в силах изменить ход истории', 
                  en='A lot of water has passed under the bridge since my "heroic days." They wouldn\'t believe me now. But they\'ll believe you. So you are the one who can change the course of history.'),

        VoiceLine(1440, Trent, ru='И какова вероятность, что друзья мне помогут?', en='And what are the odds that my friends will actually help?'),
        VoiceLine(1450, EdisonTrent, ru='Есть только один способ это проверить', en='There\'s only one way to find out.'),
        VoiceLine(1460, EdisonTrent, ru='Забери этот контейнер. Внутри него номадский ключ и все доступы которые могут тебе пригодится', en='Take this container. Inside is the Nomad Key and all the access codes you might need.'),

        VoiceLine(1500, Trent, ru='Что же, это должно сработать. Рад был видеть!', en='Well, it looks like I\'ve got a chance! Thank you!'),

        VoiceLine(1510, EdisonTrent, ru='И хандры как ни бывало. Где-ж мои 16 лет? Удачи, тезка!', en='See? And just like that, the melancholy is gone. Ah, youth! Good luck, namesake!'),

        VoiceLine(2010, Trent, ru='Хетчер, сл+ышишь меня?', en='Hatcher, do you read me?'),
        VoiceLine(2020, Hatcher, ru='Да, Трент, что случилось?', en='Yeah, Trent, what\'s up?'),
        VoiceLine(2030, Trent, ru='Срочно вылетай на планету Спр+ага, все подробности там!', en='Get to planet Sprague, ASAP! All the details there!'),
        VoiceLine(2040, Hatcher, ru='М-да? Ладно, вылетаю.', en='Hm, really? Alright, I\'m on my way.'),

        VoiceLine(2050, Trent, ru='Д+ерси!', en='Darcy!'),
        VoiceLine(2060, Darcy, ru='Д+ерси здесь.', en='Darcy here.'),
        VoiceLine(2070, Trent, ru='Вылетай на планету Спрага. Прямо сейчас, всё объясню при встрече.', en='Get to planet Sprague. Right now, I\'ll explain everything when you get there.'),
        VoiceLine(2080, Darcy, ru='Опять что-то интересненькое? Лечу!', en='Something fun again? I\'m on my way!'),

        VoiceLine(2090, Trent, ru='Аларик!', en='Alaric!'),
        VoiceLine(2100, Alaric, ru='А, Трент, ты как раз в+овремя, я хотел...', en='Ah, Trent, perfect timing, I was just about to...'),
        VoiceLine(2110, Trent, ru='Стоп! Аларик, помолчи. Срочно вылетай на планету Спр+ага!', en='Stop! Alaric, just listen. Get to planet Sprague, now!'),
        VoiceLine(2120, Alaric, ru='Как на Спр+агу?', en='To Sprague?'),
        VoiceLine(2130, Trent, ru='М+олча! Аларик, ты понял?', en='Yes, to Sprague! Alaric, do you copy?'),
        VoiceLine(2140, Alaric, ru='Да.', en='Yeah.'),
        VoiceLine(2150, Trent, ru='Вот и хорош+о.', en='Good.'),
        VoiceLine(2160, Alaric, ru='Но...', en='But...'),
        VoiceLine(2170, Trent, ru='М+олча, Аларик, м+олча.', en='All talks later.'),


        VoiceLine(2180, Kim, ru='Трент, ты куда делся?', en='Trent, where did you go?'),
        VoiceLine(2190, Trent, ru='Я улетел', en='I left.'),
        VoiceLine(2200, Kim,
                  ru='У нас готовится спецоперация, нам нужны все доступные силы. Пункт сбора в Омеге-3, прилетай',
                      en='We\'re preparing a special op, we need all available forces. The rally point is in Omega-3, get here.'),
        VoiceLine(2210, Kim,
                  ru='Ямамото гарантирует хорошее вознаграждение всем участникам, можешь вызывать своих друзей и всех кого можешь',
                      en='Yamamoto guarantees good pay for all participants, you can call your friends and anyone you can.'),
        VoiceLine(2220, Trent, ru='Нет. Ким, у меня появилось очень срочное и очень важное дело.', en='Negative, Kim. I\'ve got a very urgent and very important matter to attend to.'),
        VoiceLine(2230, Kim, ru='Настолько срочное и важное, что решил Ямамото послать?', en='So urgent and important you\'re blowing off Yamamoto?'),
        VoiceLine(2240, Trent, ru='Именно.', en='Precisely.'),
        VoiceLine(2250, Kim, ru='(после долгого молчания) Ну как знаешь...', en='Well, suit yourself...'),
    ]


class Mission11(Msn11, script.StoryMission):
    CUTSCENES = [
        Msn11AmbushCutscene,
        Msn11DrinkCutscene,
    ]
    SPACE_CLASS = Msn11Space
    SYNC_SPACE = True

    MISSION_TITLE = 'Миссия 11. Засада на Рокфорда'