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
               en='Trent?! But of course... please have a seat...'
        ),
        VoiceLine(
            40,
            Trent,
            ru='(Ультиматум) Рокфорд, отдай номадский ключ.',
               en='Rockford, you bastard! You tried to kill me! Return the Key to me at once!'
        ),
        VoiceLine(
            50,
            Rockford,
            ru='(Кладёт КПК на стол) Зачем? Чтобы ты отдал его СБА? Или Ордену? Или на кого ты сейчас работаешь?',
               en='Can\'t make a cake without breaking a few eggs. Return the Key? For you to hand over to your precious ASF? Or The Order? Who\'s your master now? You change so often it gets confusing.'
        ),

        VoiceLine(
            60,
            Trent,
            comment='Попытки уговорить со стороны Трента',
            ru='Эти артефакты обладают слишком большой разрушительной силой, и если они попадут не в те руки...',
               en='Look, you don\'t understand. These artifacts are really, really dangerous. We can\'t risk them falling into the worong hands...'
        ),
        VoiceLine(
            70,
            Trent,
            ru='Один псих по фамилии Т+илтон так недавно чуть не устроил локальный конец света в Тау-44. '
               'Они должн+ы находиться под присмотром таких организаций как СБА или Орден.',
               en='We barely stopped a megalomaniac from bringing on the apocalpyse in Tau-44 recently.'
                  'These artefacts belong under lock and key with an organization powerful enough to keep them secure... for all our sakes.'
        ),

        VoiceLine(
            80,
            Rockford,
            comment='Гигантский философский мегадиалог, скорее ближе к "суперзлодей рассказывает суперплан"',
            ru='А что ты вообще знаешь про Орден и СБА? И от кого?',
               en='Trent, whatever you think you know about The Order and the ASF - I guarantee you it doesn\'t begin to scratch the surface. And it\'s almost certainly one-sided.'
        ),
        VoiceLine(
            90,
            Rockford,
            ru='Торговля артефактами давно стала прибыльным бизнесом. И не самым опасным, надо сказать.',
               en='Artifact trading has never posed a serious danger, ever, and it\'s been around for a very, very long time.'
        ),
        VoiceLine(
            100,
            Rockford,
            ru='А в отсутствии внешней угрозы эти структуры начали заниматься борьбой за власть.',
               en='The culmination of the Nomad War, and the schism of the Order left a void in their wake. Without an external existential threat, the ASF and Order rushed to fill that void, and everything ever since then has been a power play.'
        ),
        VoiceLine(
            110,
            Rockford,
            ru='За власть глобальную, позволяющую не считаться с правительствами. '
               'И ключ номадов, том Пр+отеуса и прочее - в этой игре не больше чем козыри.',
               en='For absolute power, the kind that lets them ignore governments.'
                  'Your precious Nomad Key, the Proteus Tome, and many more - yes there have been more, I assure you... all these toys are just bit parts... in a bigger game of cosmic chess - mere bargaining chips for one-upmanship between two bitter rivals.'
        ),
        VoiceLine(
            120,
            Rockford,
            ru='И если возникнет необходимость, ни СБА, ни Орден не остановится перед тем чтобы применить их '
               'и устроить, как ты выразился, локальный конец света, например, в системе Форбс.',
               en='And if the need arises, neither the ASF nor The Order will hesitate to use them. Mark my words.'
                  'These fools don\'t care if there\'s an - apocalypse - as you put it, that wipes out half of interstellar space. They don\'t care if millions, or billions of lives are lost. All they care is about is winning.'
        ),

        VoiceLine(
            130,
            Trent,
            comment='Трент удивляется, сколько всего сейчас выпалил Рокфорд',
            ru='Ого... Р+окфорд, ты сейчас произнес больше слов,, чем за всё время нашего знакомства.',
               en='Wow... Rockford, you\'ve just said more in these ten minutes than our entire acquaintance up to this point.'
        ),

        VoiceLine(
            150,
            Rockford,
            ru='Все эти р+ейнландцы, СБА - не более, чем дети, играющие в песочнице найденной боевой гранатой.',
               en='And now even the Rheinlanders rush to the Sphere. The ASF, the Order...  children in a sandbox, fighting over hand grenades they uncover while they dig in the dirt.'
        ),
        VoiceLine(
            160,
            Rockford,
            ru='И вот,, им уже стало интересно, что будет, если выдернуть это колечко.',
               en='Now they are, as you say, pulling the pins, out of... what? Ego? These are the people trying to pull the strings of the cosmos behind the scenes. Children, and fools.'
        ),
        VoiceLine(
            170,
            Rockford,
            ru='А я знаю, как все это прекратить. Сейчас. Раз и навсегда.',
               en='But I have found a way to end all of it. Forever. For good.'
        ),
        VoiceLine(
            180,
            Rockford,
            ru='В моём будущем не будет ни кочевников, ни их наследия. Только человечество. '
               'В полной безопасности от всего этого опасного мусора.',
               en='No more Nomads. No more aliens. No petty organizations squabbling in the sandbox.'
                  'I can save everyone. All of them. And bring lasting peace to us all.'
        ),

        VoiceLine(
            200,
            Rockford,
            comment='Трент лишь офигевающе хлопает ушами',
            ru='(Давай вместе править Галактикой) Не хочешь пом+очь мне создать такой мир?...',
               en='Wouldn\'t you want such a world for your children, Mr Trent?'
        ),

        VoiceLine(
            205,
            Trent,
            ru='Я-а... Не знаю-у... О чём вообще речь?',
               en='This is a lot to take in. I\'m struggling to keep up here, man. What\'s your plan, exactly?'
        ),

        VoiceLine(
            210,
            Rockford,
            ru='(Смеясь, сматывает удочки) Они даже тебе не сказали... Забавно.',
               en='They didn\'t tell you... how pathetic. Forget it, I can manage without you.'
        ),
        VoiceLine(
            220,
            Rockford,
            ru='(Грозно) Хотя бы не мешайся у меня под ногами, Трент. Мое почтение.',
               en='Stay the hell out of my way, you poor fool. For your own safety. Goodbye.'
        ),

        VoiceLine(
            230,
            Trent,
            comment='Через пару мгновений ожидания до Трента доходит',
            ru='Какая же это всё херн+я, какой смысл...',
               en='Wait! Come back... Bah. Any more of this enigmatic crap that goes nowhere and I swear I\'m gonna lose it.'
        ),

        VoiceLine(
            250,
            Trent,
            comment='Через пару мгновений ожидания до Трента доходит',
            ru='Чёрт... Сообщения от Кима н+е было!',
               en='Damn it... Still no word from Kim!'
        ),
        VoiceLine(
            260,
            Kim,
            comment='Звонок с КПК',
            ru='(Панически кричит) Трент, Рокфорд уходит, скорее взлетаем!',
               en='Trent, Rockford is getting away! Get after him now!'
        ),
        VoiceLine(
            270,
            Trent,
            ru='А что с нашими?',
               en='What? You still haven\'t taken out his ship? What about your demolition team?'
        ),
        VoiceLine(
            280,
            Kim,
            ru='Их убили...',
               en='They\'re all dead...'
        ),
        VoiceLine(
            290,
            Trent,
            ru='Вот чёрт...',
               en='Goddamn it...'
        ),

    ]


class Msn11DrinkCutscene(Msn11, script.CutsceneProps):
    ALIAS = 'drink'
    TITLE = 'Бар линкора Мусаси'
    THORN_CLASS = m11_drink.Msn11DrinkScene
    DESCRIPTION = 'Трент хотел было набухаться от своих неуспехов, как тут к нему приходит "Старый" Трент...'
    VOICE_LINES = [

        VoiceLine(10, Trent, ru='Ким, что случилось с Ямамото? Р+айхманн сдавался. Откуда столько ненависти?',
                  en='Kim, what happened back there with Yamamoto? Reichmann was surrendering. What the hell? Was that really necessary?'),
        VoiceLine(20, Trent, ru='(Охеревающий) А Вавил+он? Почему он так плохо охранялся? Где линкоры, тучи истребителей?..',
                  en='And Babylon? Why the skeleton crew? Where were the battleships and fighter wings?'),
        VoiceLine(30, Trent, ru='(Финально) Ким, ты можешь мне ответить?!!',
                  en='Kim, answer me! What\'s going on, really?!'),

        VoiceLine(40, Kim, ru='(Громкое "Я" с желанием вскрикнуть, вдох и... тихое нет на выдохе...) Я... Нет... Пока нет',
                  en='I can\'t... you don\'t understand...'),
        VoiceLine(50, Kim, ru='Так знаешь, давай остынь. Скоро будет дело. Выдыхай. Я скоро выйду на связь.',
                  en='Nevermind. Look Trent, take a breath and chill out. Everything will be made clear to you in good time. I\'ll be in touch.'),

        VoiceLine(60, Trent, ru='Ладно, гуляй себе', en='Fine... Whatever...'),

        VoiceLine(110, EdisonTrent, ru='Неудачный день?', en='Hey, Trent. Having a bad day?'),
        VoiceLine(120, Trent, ru='Неудачная жизнь.', en='Hey Trent. Having a bad life, more like.'),
        VoiceLine(130, EdisonTrent, ru='Хм. А по мне так тебе сказочно везет. Да и с Р+окфордом у тебя почти получилось.',
                  en='Well, from where I\'m standing you look incredibly lucky. You\'re still alive. Even despite your brush with Rockford.'),
        VoiceLine(140, Trent, ru='Я устал, нет серьезно, достало всё. Берешь простой заказ, а тебе вместе с оплатой впаривают человека, которому ну просто необходимо пом+очь.', en='I\'m just so tired. I\'ve had enough. Every job I take comes with a side order of espionage and interstellar intrigue, when all I ordered was goddamn fries.'),
        VoiceLine(150, Trent, ru='Он обещает тебе златые горы - и вот, трах-бах, и ты уже поуши увяз в интригах спецслужб, и за твою голову назначена неплохая такая цена.',
                  en='Someone promises you a paycheck — then, bam! You\'re neck-deep in some galactic shit with a crazy bounty on your head.'),
        VoiceLine(160, Trent, ru='И ты пытаешься из всего этого выпутаться, но вместо этого запутываешься еще больше.',
                  en='And every time you try to get out, you sink deeper into the shit.'),
        VoiceLine(170, Trent, ru='И в конце концов, ты уже не понимаешь за кого и против кого ты, а самое главное - зачем это всё?',
                  en='In the end, friends are foes, foes are friends. And nobody can tell me... What\'s the damn point of it all?'),

        VoiceLine(180, EdisonTrent, ru='Так всегда и бывает,, тёзка, ты же фрилансер. Либо ты отстреливаешь мелких бандюков в свободных мир+ах, летая на ржавом корыте и получаешь за это копейки. Либо вот так...',
                  en='That\'s the way it goes, Trent. That\s what being a freelancer\'s all about. You either settle for small-time jobs popping two-bit thugs in obscure outer systems... Or you go after the big fish and wind up neck deep in.... this. Take it from me, I\'ve been where you are now.'),
        VoiceLine(190, EdisonTrent, ru='И считай,, тебе  повезло. Сумма у тебя на счету с шестью нулями? Летаешь ты на чём? На самом новом, под тебя тюнингованном? Обвес у тебя из самого нового оружия?', en='And know what? You\'re lucky. Crazy lucky, you just don\'t appreciate it. That credit balance of yours is looking mighty healthy. You\'re not wanting for cash. You\'ve made enough to afford that tricked-out hot rod of yours. Top-of-the-line weapons, generators, the works!'),
        VoiceLine(200, EdisonTrent, ru='А если тебе нужно чего для корабля докупить, ты же даже в счет не заглядываешь - и так знаешь, что хватит, и еще останется.', en='I\'ll bet these days you don\'t even bother checking your bank balance when you decide on an upgrade.'),
        VoiceLine(210, EdisonTrent, ru='И,, самое главное, врагов,, у тебя конечно становится всё больше и больше, но у тебя появляются друзья.',
            en='And sure, you\'re accumulating enemies. But you\'re making friends, too.'),
        VoiceLine(220, EdisonTrent, ru='Их немного, гораздо меньше чем врагов, но они настоящие, потому что испытаны боем, прошли огонь,, воду,, и медные трубы вместе с тобой.', en='Granted, maybe more enemies than friends... But real friends, Trent are hard to find. People willing to go through hell and high water with you. Even if they might not make it.'),
        VoiceLine(230, EdisonTrent, ru='И ты уверен, что бы ни случилось, на них можно положиться. И вот эти друзья, они на самом деле намного ценнее, чем шестизначный счет или новейший корабль с лучшим обвесом.',
            en='People you can count on. People like this... and the experiences you\'ve had are worth way more all the wealth in the cosmos.'),
        VoiceLine(240, EdisonTrent, ru='Вот так. А пожалеть себя иногда очень хочется, по себе знаю. Главное не злоупотреблять этим - вредно для формы.',
            en='You should be feeling grateful, not sorry for yourself.'),

        VoiceLine(250, Trent, ru='И вы мне не позволите,, да?', en='Just can\'t let a guy cry into his beer, right?'),
        VoiceLine(260, EdisonTrent, ru='Я лишь обрисую ситуацию, а ты сам решай...', en='You done moping? I think it\'s about time someone filled you in on the truth about Rockford. You ready for it?'),
        VoiceLine(270, Trent, ru='Слушаю внимательно.', en='I\'m all ears.'),
        VoiceLine(280, EdisonTrent, ru='Не здесь. Нам нужно лететь. Расскажу всё по дороге.', en='Not here. We gotta fly. I\'ll fill you in on the way.'),
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
               en='And how do you imagine I\'ll do that? Show him some leg?'
        ),
        VoiceLine(
            30,
            Kim,
            ru='Придумайте что-нибудь. Мне напомнить вам, как недавно несколько десятков пилотов вылетели в один конец, чтобы обеспечить ваше прикрытие?',
               en='Improvise. Need I remind you how many of my men died getting you to this precise point in time and space?'
        ),
        VoiceLine(
            40,
            Trent,
            ru='Ладно, значит я после посадки сразу иду в бар?',
               en='Alright, alright. So head straight to the bar after docking?'
        ),
        VoiceLine(
            50,
            Kim,
            ru='Да, а мы тут сразу займемся д+елом. Когда наши специалисты закончат, я пришлю вам сообщение на коммуникатор.',
               en='Yes, and we\'ll get to work immediately. I\'ll contact you once our demolition specialists are done.'
        ),

        VoiceLine(
            60,
            Kim,
            comment='После вылета с Харадзюку',
            ru='Р+окфорд еще на радаре, мы еще можем его нагнать.',
               en='Rockford is still on our scanners, we can catch up to him.'
        ),

        VoiceLine(
            65,
            Yamamoto,
            comment='Связь с Ямамото',
            ru='Ямамото на связи.',
               en='Kim, are you there?'
        ),
        VoiceLine(
            70,
            Kim,
            ru='Заминировать корабль Р+окфорда не удалось. Сейчас ведем погоню...',
               en='Yamamoto-san, we failed to destroy Rockford\'s ship but are currently pursuing...'
        ),
        VoiceLine(
            80,
            Yamamoto,
            ru='Станция "Вавилон" атакована силами Р+ейнланда! Всем немедленно выдвинуться на защиту!',
               en='Station Babylon is under assault by Rheinland forces! Return to base immediately! We won\'t last much longer!'
        ),
        VoiceLine(
            90,
            Kim,
            ru='О, Цха! Трент, наш штаб атакован, срочно летим на защиту. Даю координаты гиперврат.',
               en='Fuck! Trent, headquarters is under attack, we\'re moving to defend it now. Sending you the hypergate coordinates.'
        ),
        VoiceLine(
            100,
            Trent,
            ru='А Р+окфорд уйдет...',
               en='But Rockford\'s getting away...'
        ),
        VoiceLine(
            105,
            Kim,
            ru='Чёрт с ним. У нас серьезные проблемы в друг+ом месте.',
               en='Screw him! There are a thousand souls on that station! We have to save them!'
        ),

        VoiceLine(
            110,
            Kim,
            comment='Появление в системе',
            ru='Мистер Трент, летите через туннель. Ваш доступ разрешен, защитные системы деактив+ированы.',
               en='Mister Trent, proceed through the passage. Defense systems have been deactivated.'
        ),

        VoiceLine(
            120,
            Kim,
            comment='Выдвигаемся к станции Вавилон',
            ru='Это лейтенант Ким, оборона, доложите обстановку.',
               en='This is Lieutenant Kim to all squads, report your status.'
        ),
        VoiceLine(
            125,
            KusariCaptain,
            ru='Враг находится во внутреннем периметре. Станция Вавилон атакована, требуется поддержка!',
               en='The enemy has breached the inner perimeter. Station Babylon is under attack, we require assistance!'
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
               en='The enemy is breaching the station airlock!'
        ),
        VoiceLine(
            150,
            Kim,
            ru='Дело очень плохо...',
               en='Oh my God...'
        ),
        VoiceLine(
            160,
            Trent,
            ru='Что стряслось?',
               en='What?'
        ),
        VoiceLine(
            170,
            Kim,
            ru='На Вавилоне находятся архивы Ордена. Артефакты. Видимо Р+ейнландцы здесь за этим. Нужно их остановить',
               en='All the Order\'s archives are on Babylon. And all the artifacts. The Rheinlanders must be here to steal them. We must stop them at all costs!'
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
               en='Babylon here, over. The enemy entered the main vault and escaped with the Nomad power core.'
        ),
        VoiceLine(
            200,
            Yamamoto,
            ru='Всеобщий приказ. Всем силам выдвинуться вслед за р+ейнландскими кораблями. Нельзя допустить того, что они заполучат энергоядр+о',
               en='To all ships. Chase down the Rheinland ships. We cannot allow them to escape with the power core!'
        ),
        VoiceLine(
            210,
            Yamamoto,
            ru='Энергоядр+о было направлено на станцию Вена. Ударное звено и линкор Мус+аси уже выдвинулись. Ким, направляйтесь к Вене своим ходом.',
               en='We\'ve tracked the power core to Station Vienna. The battleship Musashi is en route with a strike wing. Kym, Trent, proceed to Vienna.'
        ),
        VoiceLine(
            240,
            Kim,
            ru='Так точно, уже летим',
               en='Affirmative, we\'re on our way!'
        ),

        VoiceLine(
            250,
            Trent,
            ru='На кой ляд Р+ейнландцам сдалось это энергоядр+о',
               en='Kim, why would the Rheinlanders steal a power core? What do you think they\'re up to?'
        ),
        VoiceLine(
            260,
            Kim,
            ru='Ядр+о когда-то вынул твой тёзка из логова кочеников в ходе номадской войн+ы. Очень ценная и технологичная штука',
               en='Not just any power core. A Nomad core. This particular core was extracted from the Nomad Lair during the Nomad War by Edison Trent. It\'s an exceedingly valuable piece of advanced technology...'
        ),
        VoiceLine(
            270,
            Trent,
            ru='Ах да. Логово кочевников. Я видел как с этими технологиями работали ребята из Л+иберти. Весьма взрывоопасная вещица',
               en='Oh, the Nomad Lair. I saw what happened last time Liberty messed with that kind of tech. It\'s incomprehensibly powerful and highly unstable!'
        ),
        VoiceLine(
            280,
            Kim,
            ru='Поэтому мы не дадим и шанса Р+ейнландцам воспользоваться ей',
               en='We mustn\'t give the Rheinlanders a chance to use it, whatever their intentions.'
        ),

        VoiceLine(
            290,
            Kim,
            comment='Рядом со станцией',
            ru='Так, Трент. Мы обнаружили сигнатуры в исследовательских контейнерах по периметру базы.',
               en='Alright, Trent. We\'ve detected the Core\'s signature in the research containers around the base\'s perimeter.'
        ),
        VoiceLine(
            300,
            Kim,
            ru='Уничтожь эти контейнеры. Скорее всего ядр+о в одном из них',
               en='Destroy the containers. The core is likely in one of them.'
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
               en='No, it\'ll be fine. Our scientists put it through worse and couldn\'t even scratch it. Hurry up, Trent!'
        ),

        VoiceLine(
            330,
            Yamamoto,
            comment='После уничтожения контейнеров',
            ru='Внимание, сигнатура генератора обнаружена на улетающем корабле! Срочно перехватить, пока он не ушел к гипердыре!',
               en='Attention! The core\'s signature is moving! It\'s on a ship! Intercept it immediately before they reach the wormhole!'
        ),

        VoiceLine(
            340,
            Kim,
            ru='Трент, сделай что-нибудь!',
            en='Trent, full power to thrusters!'
        ),

        VoiceLine(
            350,
            Trent,
            comment='Проигрывается катсцена. Корабль попадает в засаду и взрывается, а лут забирает Р+окфорд',
            ru='Чёрт, это Р+окфорд!',
            en='Gods damn it, it\'s Rockford!',
            cinematic=True
        ),
        VoiceLine(
            360,
            Kim,
            ru='Он угоняет энергоядр+о!',
            en='He\'s stealing the power core!',
            cinematic=True
        ),
        VoiceLine(
            370,
            Yamamoto,
            ru='Останов+ите его!',
            en='Stop him!',
            cinematic=True
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
               en='This is a catastrophe!'
        ),

        VoiceLine(
            400,
            Reichman,
            comment='Прибывает рейнландское подкрепление',
            ru='(Пока еще горделиво) Солдаты Ордена, с вами говорит адмирал Р+айхман!',
               en='Soldiers of The Order! This is Admiral Reichman speaking! Surrender now or we will destroy you!'
        ),
        VoiceLine(
            410,
            Yamamoto,
            ru='(Яростная злоба) Р+айхман? Уничтожить его! Всем приказ атаковать линкор Гнейзенау!',
               en='Reichman? Damn him! All units, concentrate fire on the battleship Gneisenau!'
        ),

        VoiceLine(
            450,
            Reichman,
            comment='Линкор райхмана почти уничтожен',
            ru='(Паника) Мы сдаемся! Я сдаюсь! Ямам+ото!',
               en='We surrender! I repeat, we surrender! Yamamoto! Cease fire!'
        ),


        VoiceLine(
            500,
            Yamamoto,
            ru='(Абсолютный гнев) Сдаешься? Ч+ёрта с два! Уничтожить линкор Гнейзенау!',
               en='Surrender? That\'s too good a fate for you! Send him to meet his maker!'
        ),
        VoiceLine(
            510,
            Reichman,
            ru='Ямамото, я же сдался, грязный, ублюдок...',
               en='Yamamoto, I\'ve surrendered, cease fire! By the terms of war, you are obliged to... what the hell are you doing?? Nooooo.....'
        ),

        VoiceLine(
            520,
            Kim,
            comment='Линкор и флот рейнланда подавлены',
            ru='Все отряды Р+ейнланда прекратили сопротивление.',
               en='All Rheinland units have ceased resisting.'
        ),
        VoiceLine(
            530,
            Yamamoto,
            ru='(Злобный) Так гораздо лучше. Отправить призовую партию на Вену. Взять под конвой корабли Р+ейнланда.',
               en='Very good. Round up any survivors.'
        ),
        VoiceLine(
            540,
            Yamamoto,
            ru='(Ярость) И если вы, герры сраные, только попробуете р+ыпнуться - проследуете за своим вонючим адмиралом.',
               en='To all Rhineland ships, if any of you bastards get any funny ideas, you\'ll follow your bastard admiral straight to hell!'
        ),

        VoiceLine(
            550,
            Kim,
            ru='Трент, садись на Мус+аси. Наша работа тут выполнена',
               en='Trent, dock with the Musashi. Our work here is done.'
        ),

        VoiceLine(1170, Trent, ru='Ну так, о чём речь.', en='Trent, what\'s the deal?'),

        VoiceLine(1180, EdisonTrent,
                  ru='Если коротко - то всё плохо. Р+окфорд, как ты понял, решил "спасти" всё человечество. И сейчас ни СБА ни Орден помешать ему уже не могут.',
                      en='Everything\'s gone to hell. Rockford, as you\'ve gathered, is determined to save all of humanity by destroying the one thing dividing it - the Sphere. And right now, neither the ASF nor The Order can stop him.'),
        VoiceLine(1190, EdisonTrent, ru='А вот у тебя учитывая твою патологическую везучесть, может и получиться.', en='But you, with your diabolical luck might just be able to.'),

        VoiceLine(1200, Trent, ru='А кто такой вообще этот Р+окфорд?', en='Just who is Rockford, really?'),

        VoiceLine(1210, EdisonTrent,
                  ru='Один очень хороший человек, внезапно слетевший с катушек и задавшийся целью осчастливить человечество.',
                      en='A complete nutcase.'),
        VoiceLine(1220, EdisonTrent,
                  ru='Проблема в том что в этом случае обычные клерки приносят в патентные бюро чертежи вечных двигателей, а вот фигуры масштаба Р+окфорда могут и уничтожить человечество, пока его же и спасает.',
                      en='Rockford is unhinged and totally unpredictable. He\'s just as capable of destroying all humanity as saving it, and quite likely to do the former in his attempt at the latter. Nobody knows what will happen if the Sphere were to be destroyed.'),

        VoiceLine(1230, Trent, ru='А поконкретнее?', en='But who is he really? Who does he work for?'),

        VoiceLine(1240, EdisonTrent, ru='Аттикус Р+окфорд... великий и ужасный. Он - из ветеранов Ордена.', en='He was a brilliant Order scientist until he went rogue. '),
        VoiceLine(1250, EdisonTrent,
                  ru='Очень болезненно отнесся к тому что Орден не смог предотвратить экспансию кочевников во время того инцедента и занялся изучением артефактов - так называемого наследия кочевников.',
                      en='When The Order failed to prevent the Nomad incursion during the... incident, he began to lose faith and decided to take things into his own hands. He threw himself into studying the artifacts—the so-called Nomad Legacy.'),
        VoiceLine(1260, EdisonTrent,
                  ru='Именно он обнаружил ту самую Сферу, и каким-то образом понял что она - своего рода ящик Панд+оры, и содержит в себе смертоносную силу.',
                      en='He\'s the one who discovered the Sphere, and we believe he actually figured out what exactly it does.'),
        VoiceLine(1270, EdisonTrent,
                  ru='Мы вместе работали над Сферой. Он нашел способ ее уничтожить, но руководство Ордена было категорически против.',
                      en='It terrified him, whatever it was, and after he discovered a way to destroy it, he lobbied hard for to do just that but the Order\'s leadership refused. There was just no telling what would happen if an object that incomprehensibly powerful were to be destroyed. Our scientists predicted the end of all existence. Everything. Not just a star system or two.'),
        VoiceLine(1280, EdisonTrent,
                  ru='Тогда уже начал+а проявляться его маниакальность в достижении цели, а я понял, что ключ номадов сможет управлять сферой.',
                      en='That\'s when he... started to unravel. In his wild rants he mentioned that the Nomad Key controls the Sphere and was the, well, key.'),
        VoiceLine(1290, EdisonTrent,
                  ru='И решил удалиться подальше. Так что мое пленение кс+еносами было мною подстроено.',
                      en='One day he flew into a rage at me for not supporting him and pulled a gun. I barely escaped alive. I decided I\'d better make myself scarce and let myself be captured by the Xenos so I\'d be safe and hidden from him.'),

        VoiceLine(1300, Trent, ru='И что теперь делать? Ключ у Р+окфорда и он может делать со Сферой всё что захочет. И никто не сможет ему помешать.', en='So what now? Rockford has his hands on the Key. It\'s too late for us to stop him destroying the Sphere.'),

        VoiceLine(1350, EdisonTrent,
                  ru='Не совсем так. Есть еще один ключ, я его забрал с собой, когда отправился к добровольное изгнание к Кс+еносам. Он абсолютно идентичен тому, что у Р+окфорда.',
                      en='Well... actually there\'s another Key. I took it with me when I went into voluntary exile with the Xenos. It\'s absolutely identical to the one Rockford has. I\'m giving it to you.'),
        VoiceLine(1360, Trent, ru='И что мне с ним делать?', en='Me? What am I supposed to do with it?'),
        VoiceLine(1370, EdisonTrent,
                  ru='Решать тебе, но я бы в лучшие свои годы собрал силы Ордена или СБА и полетел бы прямо к сфере, пытаясь остановить Р+окфорда, пока это еще возможно.',
                      en='You\'ll have to figure it out for yourself. In my prime I\'d have rallied a group of friends and made a beeline for the Sphere to stop Rockford while there\'s still time.'),
        VoiceLine(1380, Trent,
                  ru='Тогда почему ты не сделаешь это сам? Почему я?', en='Then why can\'t you do it? Why me?'),

        VoiceLine(1390, EdisonTrent, ru='Потому что сейчас в данный момент у тебя больше друзей, чем у меня', en='Because right now you\'ve got more friends than me, and I\'m way too old for this crap.'),
        VoiceLine(1400, EdisonTrent, ru='В своё время утекло много вод+ы. Мне сейчас они не поверят. А тебе да. Так что ты в силах изменить ход истории', 
                  en='My fighting days are over. I\'m done. I\'ve been watching you. You\'ve got the smarts and the skills, and people trust you now. You have to be the one to do this. You, Trent.'),

        VoiceLine(1440, Trent, ru='И какова вероятность, что друзья мне помогут?', en='And what if my friends won\'t help? Can\'t you come?'),
        VoiceLine(1450, EdisonTrent, ru='Есть только один способ это проверить', en='Hells no. You think I\'m crazy?'),
        VoiceLine(1460, EdisonTrent, ru='Забери этот контейнер. Внутри него номадский ключ и все доступы которые могут тебе пригодится', en='But here, take it. The Nomad Key, and an access card with the access codes you\'re ever gonna need.'),

        VoiceLine(1500, Trent, ru='Что же, это должно сработать. Рад был видеть!', en='Well, at least that helps. Thanks.'),

        VoiceLine(1510, EdisonTrent, ru='И хандры как ни бывало. Где-ж мои 16 лет? Удачи, тезка!', en='Good luck. Give \'em hell.'),

        VoiceLine(2010, Trent, ru='Хетчер, сл+ышишь меня?', en='Hatcher, are you reading me?'),
        VoiceLine(2020, Hatcher, ru='Да, Трент, что случилось?', en='Yeah, Trent, loud and clear. What\'s up?'),
        VoiceLine(2030, Trent, ru='Срочно вылетай на планету Спр+ага, все подробности там!', en='Get to planet Sprague, ASAP! I\'ll fill you in there!'),
        VoiceLine(2040, Hatcher, ru='М-да? Ладно, вылетаю.', en='Alright, I\'m on my way.'),

        VoiceLine(2050, Trent, ru='Д+ерси!', en='Darcy!'),
        VoiceLine(2060, Darcy, ru='Д+ерси здесь.', en='Darcy here.'),
        VoiceLine(2070, Trent, ru='Вылетай на планету Спрага. Прямо сейчас, всё объясню при встрече.', en='Get to planet Sprague. Right now, I\'ll explain everything when you get there.'),
        VoiceLine(2080, Darcy, ru='Опять что-то интересненькое? Лечу!', en='More shits and giggles? I\'m on my way!'),

        VoiceLine(2090, Trent, ru='Аларик!', en='Alaric!'),
        VoiceLine(2100, Alaric, ru='А, Трент, ты как раз в+овремя, я хотел...', en='Ah, Trent, perfect timing, I was just about to...'),
        VoiceLine(2110, Trent, ru='Стоп! Аларик, помолчи. Срочно вылетай на планету Спр+ага!', en='Alaric, just listen up. I need you to get to planet Sprague, now!'),
        VoiceLine(2120, Alaric, ru='Как на Спр+агу?', en='To Sprague? Why?'),
        VoiceLine(2130, Trent, ru='М+олча! Аларик, ты понял?', en='It\'s, really really important! Look, old friend, do you trust me?'),
        VoiceLine(2140, Alaric, ru='Да.', en='Yeah.'),
        VoiceLine(2150, Trent, ru='Вот и хорош+о.', en='Good. Sprague.'),
        VoiceLine(2160, Alaric, ru='Но...', en='But what...'),
        VoiceLine(2170, Trent, ru='М+олча, Аларик, м+олча.', en='No time. Fill you in later.'),


        VoiceLine(2180, Kim, ru='Трент, ты куда делся?', en='Trent, where the hell are you?'),
        VoiceLine(2190, Trent, ru='Я улетел', en='Something pressing\'s come up.'),
        VoiceLine(2200, Kim,
                  ru='У нас готовится спецоперация, нам нужны все доступные силы. Пункт сбора в Омеге-3, прилетай',
                      en='We\'re preparing a huge mission and need all available men on this one. Our rally point is in Omega-3, get over here.'),
        VoiceLine(2210, Kim,
                  ru='Ямамото гарантирует хорошее вознаграждение всем участникам, можешь вызывать своих друзей и всех кого можешь',
                      en='Yamamoto guarantees extremely generous remuneration...'),
        VoiceLine(2220, Trent, ru='Нет. Ким, у меня появилось очень срочное и очень важное дело.', en='Sorry, Kim. I\'ve got a more urgent and important matter to attend to.'),
        VoiceLine(2230, Kim, ru='Настолько срочное и важное, что решил Ямамото послать?', en='So urgent you\'d risk blowing off Yamamoto?'),
        VoiceLine(2240, Trent, ru='Именно.', en='Much more.'),
        VoiceLine(2250, Kim, ru='(после долгого молчания) Ну как знаешь...', en='Okay, well, good luck with that...'),
    ]


class Mission11(Msn11, script.StoryMission):
    CUTSCENES = [
        Msn11AmbushCutscene,
        Msn11DrinkCutscene,
    ]
    SPACE_CLASS = Msn11Space
    SYNC_SPACE = True
    SYNC_SUBS = True

    MISSION_TITLE = 'Миссия 11. Засада на Рокфорда'