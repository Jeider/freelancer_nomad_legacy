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
               en='Trent?... Yes, of course, have a seat.'
        ),
        VoiceLine(
            40,
            Trent,
            ru='(Ультиматум) Рокфорд, отдай номадский ключ.',
               en='Rockford, hand over the Nomad key.'
        ),
        VoiceLine(
            50,
            Rockford,
            ru='(Кладёт КПК на стол) Зачем? Чтобы ты отдал его СБА? Или Ордену? Или на кого ты сейчас работаешь?',
               en='Why? So you can hand it to the ASF? Or the Order? Or whoever you\'re working for now?'
        ),

        VoiceLine(
            60,
            Trent,
            comment='Попытки уговорить со стороны Трента',
            ru='Эти артефакты обладают слишком большой разрушительной силой, и если они попадут не в те руки...',
               en='These artifacts have far too much destructive power, and if they fall into the wrong hands...'
        ),
        VoiceLine(
            70,
            Trent,
            ru='Один псих по фамилии Т+илтон так недавно чуть не устроил локальный конец света в Тау-44. '
               'Они должн+ы находиться под присмотром таких организаций как СБА или Орден.',
               en='Some psycho named Tilton nearly caused a local apocalypse in Tau-44 not long ago. They need to be kept under the watch of organizations like the ASF or the Order.'
        ),

        VoiceLine(
            80,
            Rockford,
            comment='Гигантский философский мегадиалог, скорее ближе к "суперзлодей рассказывает суперплан"',
            ru='А что ты вообще знаешь про Орден и СБА? И от кого?',
               en='And what do you even know about the Order and the ASF? And from whom?'
        ),
        VoiceLine(
            90,
            Rockford,
            ru='Торговля артефактами давно стала прибыльным бизнесом. И не самым опасным, надо сказать.',
               en='Artifact trading became a profitable business a long time ago. And not the most dangerous one, I should add.'
        ),
        VoiceLine(
            100,
            Rockford,
            ru='А в отсутствии внешней угрозы эти структуры начали заниматься борьбой за власть.',
               en='And with no external threat, these organizations started fighting for power.'
        ),
        VoiceLine(
            110,
            Rockford,
            ru='За власть глобальную, позволяющую не считаться с правительствами. '
               'И ключ номадов, том Пр+отеуса и прочее - в этой игре не больше чем козыри.',
               en='For global power, the kind that lets them disregard governments. And the Nomad key, the Proteus Tome, and the rest are nothing more than trump cards in this game.'
        ),
        VoiceLine(
            120,
            Rockford,
            ru='И если возникнет необходимость, ни СБА, ни Орден не остановится перед тем чтобы применить их '
               'и устроить, как ты выразился, локальный конец света, например, в системе Форбс.',
               en='And if the need arises, neither the ASF nor the Order will hesitate to use them and bring about, as you put it, a local apocalypse, in the Forbes system, for example.'
        ),

        VoiceLine(
            130,
            Trent,
            comment='Трент удивляется, сколько всего сейчас выпалил Рокфорд',
            ru='Ого... Р+окфорд, ты сейчас произнес больше слов,, чем за всё время нашего знакомства.',
               en='Wow... Rockford, you\'ve just said more words than in all the time we\'ve known each other.'
        ),

        VoiceLine(
            150,
            Rockford,
            ru='Все эти р+ейнландцы, СБА - не более, чем дети, играющие в песочнице найденной боевой гранатой.',
               en='All these Rheinlanders, the ASF, are nothing more than children playing in a sandbox with a live grenade they found.'
        ),
        VoiceLine(
            160,
            Rockford,
            ru='И вот,, им уже стало интересно, что будет, если выдернуть это колечко.',
               en='And now they\'re already curious what happens if they pull that pin.'
        ),
        VoiceLine(
            170,
            Rockford,
            ru='А я знаю, как все это прекратить. Сейчас. Раз и навсегда.',
               en='And I know how to stop all of this. Now. Once and for all.'
        ),
        VoiceLine(
            180,
            Rockford,
            ru='В моём будущем не будет ни кочевников, ни их наследия. Только человечество. '
               'В полной безопасности от всего этого опасного мусора.',
               en='In my future there will be no Nomads, and no legacy of theirs. Only humanity. Completely safe from all this dangerous junk.'
        ),

        VoiceLine(
            200,
            Rockford,
            comment='Трент лишь офигевающе хлопает ушами',
            ru='(Давай вместе править Галактикой) Не хочешь пом+очь мне создать такой мир?...',
               en='Don\'t you want to help me build a world like that?...'
        ),

        VoiceLine(
            205,
            Trent,
            ru='Я-а... Не знаю-у... О чём вообще речь?',
               en='I... I don\'t know... What are we even talking about?'
        ),

        VoiceLine(
            210,
            Rockford,
            ru='(Смеясь, сматывает удочки) Они даже тебе не сказали... Забавно.',
               en='They didn\'t even tell you... Amusing.'
        ),
        VoiceLine(
            220,
            Rockford,
            ru='(Грозно) Хотя бы не мешайся у меня под ногами, Трент. Мое почтение.',
               en='At least stay out of my way, Trent. My regards.'
        ),

        VoiceLine(
            230,
            Trent,
            comment='Через пару мгновений ожидания до Трента доходит',
            ru='Какая же это всё херн+я, какой смысл...',
               en='What a load of bullshit this all is, what\'s the point...'
        ),

        VoiceLine(
            250,
            Trent,
            comment='Через пару мгновений ожидания до Трента доходит',
            ru='Чёрт... Сообщения от Кима н+е было!',
               en='Damn... There was no message from Kim!'
        ),
        VoiceLine(
            260,
            Kim,
            comment='Звонок с КПК',
            ru='(Панически кричит) Трент, Рокфорд уходит, скорее взлетаем!',
               en='Trent, Rockford\'s leaving, take off, now!'
        ),
        VoiceLine(
            270,
            Trent,
            ru='А что с нашими?',
               en='And what about our people?'
        ),
        VoiceLine(
            280,
            Kim,
            ru='Их убили...',
               en='They were killed...'
        ),
        VoiceLine(
            290,
            Trent,
            ru='Вот чёрт...',
               en='Oh, damn...'
        ),

    ]


class Msn11DrinkCutscene(Msn11, script.CutsceneProps):
    ALIAS = 'drink'
    TITLE = 'Бар линкора Мусаси'
    THORN_CLASS = m11_drink.Msn11DrinkScene
    DESCRIPTION = 'Трент хотел было набухаться от своих неуспехов, как тут к нему приходит "Старый" Трент...'
    VOICE_LINES = [

        VoiceLine(10, Trent, ru='Ким, что случилось с Ямамото? Р+айхманн сдавался. Откуда столько ненависти?',
                  en='Kim, what happened with Yamamoto? Reichman was surrendering. Where\'s all this hatred coming from?'),
        VoiceLine(20, Trent, ru='(Охеревающий) А Вавил+он? Почему он так плохо охранялся? Где линкоры, тучи истребителей?..',
                  en='And Babylon? Why was it guarded so poorly? Where were the battleships, the swarms of fighters?..'),
        VoiceLine(30, Trent, ru='(Финально) Ким, ты можешь мне ответить?!!',
                  en='Kim, can you answer me?!!'),

        VoiceLine(40, Kim, ru='(Громкое "Я" с желанием вскрикнуть, вдох и... тихое нет на выдохе...) Я... Нет... Пока нет',
                  en='I... No... Not yet.'),
        VoiceLine(50, Kim, ru='Так знаешь, давай остынь. Скоро будет дело. Выдыхай. Я скоро выйду на связь.',
                  en='You know what, cool off. There\'ll be a job soon. Breathe. I\'ll be in touch soon.'),

        VoiceLine(60, Trent, ru='Ладно, гуляй себе', en='Fine, go on.'),

        VoiceLine(110, EdisonTrent, ru='Неудачный день?', en='Bad day?'),
        VoiceLine(120, Trent, ru='Неудачная жизнь.', en='Bad life.'),
        VoiceLine(130, EdisonTrent, ru='Хм. А по мне так тебе сказочно везет. Да и с Р+окфордом у тебя почти получилось.',
                  en='Hm. The way I see it, you\'re incredibly lucky. And you almost pulled it off with Rockford.'),
        VoiceLine(140, Trent, ru='Я устал, нет серьезно, достало всё. Берешь простой заказ, а тебе вместе с оплатой впаривают человека, которому ну просто необходимо пом+очь.', en='I\'m tired, no, seriously, I\'m sick of all of it. You take a simple job, and along with the pay they stick you with someone you just have to help.'),
        VoiceLine(150, Trent, ru='Он обещает тебе златые горы - и вот, трах-бах, и ты уже поуши увяз в интригах спецслужб, и за твою голову назначена неплохая такая цена.',
                  en='He promises you mountains of gold, and then, bam, you\'re in up to your ears in secret-service intrigue, with a pretty nice price on your head.'),
        VoiceLine(160, Trent, ru='И ты пытаешься из всего этого выпутаться, но вместо этого запутываешься еще больше.',
                  en='And you try to untangle yourself from all of it, but instead you get tangled even more.'),
        VoiceLine(170, Trent, ru='И в конце концов, ты уже не понимаешь за кого и против кого ты, а самое главное - зачем это всё?',
                  en='And in the end, you no longer understand who you\'re for and who you\'re against, and most of all, what\'s it all for?'),

        VoiceLine(180, EdisonTrent, ru='Так всегда и бывает,, тёзка, ты же фрилансер. Либо ты отстреливаешь мелких бандюков в свободных мир+ах, летая на ржавом корыте и получаешь за это копейки. Либо вот так...',
                  en='That\'s always how it goes, namesake, you\'re a freelancer. Either you\'re shooting small-time thugs in the independent worlds, flying a rusty tub and getting pennies for it. Or it\'s like this...'),
        VoiceLine(190, EdisonTrent, ru='И считай,, тебе  повезло. Сумма у тебя на счету с шестью нулями? Летаешь ты на чём? На самом новом, под тебя тюнингованном? Обвес у тебя из самого нового оружия?', en='And count yourself lucky. Six zeros in your account? What are you flying? The newest thing, tuned just for you? A loadout of the newest weapons?'),
        VoiceLine(200, EdisonTrent, ru='А если тебе нужно чего для корабля докупить, ты же даже в счет не заглядываешь - и так знаешь, что хватит, и еще останется.', en='And if you need to buy something else for the ship, you don\'t even look at the account. You already know it\'ll be enough, and some left over.'),
        VoiceLine(210, EdisonTrent, ru='И,, самое главное, врагов,, у тебя конечно становится всё больше и больше, но у тебя появляются и друзья.',
            en='And, most important, enemies, sure, you\'re getting more and more of them, but you\'re getting friends too.'),
        VoiceLine(220, EdisonTrent, ru='Их немного, гораздо меньше чем врагов, но они настоящие, потому что испытаны боем, прошли огонь,, воду,, и медные трубы вместе с тобой.', en='There aren\'t many of them, far fewer than enemies, but they\'re real, because they\'ve been tested in battle, been through fire and water with you.'),
        VoiceLine(230, EdisonTrent, ru='И ты уверен, что бы ни случилось, на них можно положиться. И вот эти друзья, они на самом деле намного ценнее, чем шестизначный счет или новейший корабль с лучшим обвесом.',
            en='And you\'re sure that no matter what happens, you can count on them. And these friends are actually worth far more than a six-digit account or the newest ship with the best loadout.'),
        VoiceLine(240, EdisonTrent, ru='Вот так. А пожалеть себя иногда очень хочется, по себе знаю. Главное не злоупотреблять этим - вредно для формы.',
            en='That\'s how it is. And sometimes you really want to feel sorry for yourself, I know it myself. Just don\'t overdo it. Bad for your form.'),

        VoiceLine(250, Trent, ru='И вы мне не позволите,, да?', en='And you won\'t let me, will you?'),
        VoiceLine(260, EdisonTrent, ru='Я лишь обрисую ситуацию, а ты сам решай...', en='I\'m just laying out the situation. You decide...'),
        VoiceLine(270, Trent, ru='Слушаю внимательно.', en='I\'m listening carefully.'),
        VoiceLine(280, EdisonTrent, ru='Не здесь. Нам нужно лететь. Расскажу всё по дороге.', en='Not here. We need to fly. I\'ll tell you everything on the way.'),
    ]


class Msn11Space(Msn11, script.SpaceVoiceProps):
    VOICE_LINES = [

        VoiceLine(
            10,
            Kim,
            ru='Мистер Трент, Р+окфорд сейчас находится в баре станции Харадзюку. ',
               en='Mister Trent, Rockford is in the bar on Harajuku Station right now.'
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
               en='And how do you picture that?'
        ),
        VoiceLine(
            30,
            Kim,
            ru='Придумайте что-нибудь. Мне напомнить вам, как недавно несколько десятков пилотов вылетели в один конец, чтобы обеспечить ваше прикрытие?',
               en='Think of something. Need I remind you how, not long ago, several dozen pilots flew a one-way trip to cover you?'
        ),
        VoiceLine(
            40,
            Trent,
            ru='Ладно, значит я после посадки сразу иду в бар?',
               en='Alright, so right after I dock I go straight to the bar?'
        ),
        VoiceLine(
            50,
            Kim,
            ru='Да, а мы тут сразу займемся д+елом. Когда наши специалисты закончат, я пришлю вам сообщение на коммуникатор.',
               en='Yes, and we\'ll get right to work here. When our specialists are done, I\'ll send you a message on the communicator.'
        ),

        VoiceLine(
            60,
            Kim,
            comment='После вылета с Харадзюку',
            ru='Р+окфорд еще на радаре, мы еще можем его нагнать.',
               en='Rockford is still on radar. We can still catch up to him.'
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
               en='We failed to mine Rockford\'s ship. We\'re in pursuit now...'
        ),
        VoiceLine(
            80,
            Yamamoto,
            ru='Станция "Вавилон" атакована силами Р+ейнланда! Всем немедленно выдвинуться на защиту!',
               en='Station Babylon has been attacked by Rheinland forces! Everyone, move out to defend it immediately!'
        ),
        VoiceLine(
            90,
            Kim,
            ru='О, Цха! Трент, наш штаб атакован, срочно летим на защиту. Даю координаты гиперврат.',
               en='Tch! Trent, our headquarters is under attack, we\'re flying to defend it now. Sending the jump gate coordinates.'
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
               en='Screw him. We\'ve got serious problems somewhere else.'
        ),

        VoiceLine(
            110,
            Kim,
            comment='Появление в системе',
            ru='Мистер Трент, летите через туннель. Ваш доступ разрешен, защитные системы деактив+ированы.',
               en='Mister Trent, fly through the tunnel. Your access is cleared, the defense systems are deactivated.'
        ),

        VoiceLine(
            120,
            Kim,
            comment='Выдвигаемся к станции Вавилон',
            ru='Это лейтенант Ким, оборона, доложите обстановку.',
               en='This is Lieutenant Kim. Defense, report the situation.'
        ),
        VoiceLine(
            125,
            KusariCaptain,
            ru='Враг находится во внутреннем периметре. Станция Вавилон атакована, требуется поддержка!',
               en='The enemy is inside the inner perimeter. Station Babylon is under attack, support required!'
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
               en='The enemy has gotten inside Station Babylon!'
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
               en='What happened?'
        ),
        VoiceLine(
            170,
            Kim,
            ru='На Вавилоне находятся архивы Ордена. Артефакты. Видимо Р+ейнландцы здесь за этим. Нужно их остановить',
               en='The Order\'s archives are on Babylon. Artifacts. Apparently the Rheinlanders are here for that. We need to stop them.'
        ),

        VoiceLine(
            180,
            Kim,
            comment='Все диверсанты ликвидированы',
            ru='Кажется всё.',
               en='Seems that\'s all.'
        ),
        VoiceLine(
            190,
            KusariCaptain,
            ru='Говорит Вавилон, статус. Враг проник в главное хранилище и утащил номадское энергоядр+о.',
               en='Babylon speaking, status. The enemy got into the main vault and made off with the Nomad power core.'
        ),
        VoiceLine(
            200,
            Yamamoto,
            ru='Всеобщий приказ. Всем силам выдвинуться вслед за р+ейнландскими кораблями. Нельзя допустить того, что они заполучат энергоядр+о',
               en='General order. All forces, move out after the Rheinland ships. We cannot allow them to get the power core.'
        ),
        VoiceLine(
            210,
            Yamamoto,
            ru='Энергоядр+о было направлено на станцию Вена. Ударное звено и линкор Мус+аси уже выдвинулись. Ким, направляйтесь к Вене своим ходом.',
               en='The power core was sent to Station Vienna. The strike wing and the battleship Musashi have already moved out. Kim, make your own way to Vienna.'
        ),
        VoiceLine(
            240,
            Kim,
            ru='Так точно, уже летим',
               en='Affirmative, we\'re already on our way.'
        ),

        VoiceLine(
            250,
            Trent,
            ru='На кой ляд Р+ейнландцам сдалось это энергоядр+о',
               en='Why the hell do the Rheinlanders want this power core?'
        ),
        VoiceLine(
            260,
            Kim,
            ru='Ядр+о когда-то вынул твой тёзка из логова кочеников в ходе номадской войн+ы. Очень ценная и технологичная штука',
               en='Your namesake pulled that core out of the Nomad lair once, during the Nomad War. A very valuable, high-tech piece.'
        ),
        VoiceLine(
            270,
            Trent,
            ru='Ах да. Логово кочевников. Я видел как с этими технологиями работали ребята из Л+иберти. Весьма взрывоопасная вещица',
               en='Oh, right. The Nomad lair. I saw the Liberty guys working with that tech. Quite an explosive little thing.'
        ),
        VoiceLine(
            280,
            Kim,
            ru='Поэтому мы не дадим и шанса Р+ейнландцам воспользоваться ей',
               en='That\'s why we won\'t give the Rheinlanders even a chance to use it.'
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
               en='Destroy these containers. The core is most likely in one of them.'
        ),
        VoiceLine(
            310,
            Trent,
            ru='А энергоядр+о мы этим не уничтожим?',
               en='And we won\'t destroy the power core doing that?'
        ),
        VoiceLine(
            320,
            Kim,
            ru='Всё с ним будет хорошо, в наших лабораториях с ним и не такое вытворяли. Давай ищи, не мешкай',
               en='It\'ll be fine. Our labs have done worse to it. Come on, search, don\'t dawdle.'
        ),

        VoiceLine(
            330,
            Yamamoto,
            comment='После уничтожения контейнеров',
            ru='Внимание, сигнатура генератора обнаружена на улетающем корабле! Срочно перехватить, пока он не ушел к гипердыре!',
               en='Attention, generator signature detected on a ship that\'s leaving! Intercept immediately, before it reaches the jump hole!'
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
            en='Damn, it\'s Rockford!',
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
               en='Too late, he slipped away.'
        ),

        VoiceLine(
            390,
            Yamamoto,
            ru='(Ярость) Этого нельзя было допустить!',
               en='This should not have been allowed!'
        ),

        VoiceLine(
            400,
            Reichman,
            comment='Прибывает рейнландское подкрепление',
            ru='(Пока еще горделиво) Солдаты Ордена, с вами говорит адмирал Р+айхман!',
               en='Soldiers of the Order, this is Admiral Reichman speaking!'
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
               en='Surrendering? Like hell! Destroy the battleship Gneisenau!'
        ),
        VoiceLine(
            510,
            Reichman,
            ru='Ямамото, я же сдался, грязный, ублюдок...',
               en='Yamamoto, I surrendered, you dirty bastard...'
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
               en='Much better this way. Send a prize crew to Vienna. Take the Rheinland ships under escort.'
        ),
        VoiceLine(
            540,
            Yamamoto,
            ru='(Ярость) И если вы, герры сраные, только попробуете р+ыпнуться - проследуете за своим вонючим адмиралом.',
               en='And if you fucking Herrs so much as try to make a move, you\'ll follow your stinking admiral.'
        ),

        VoiceLine(
            550,
            Kim,
            ru='Трент, садись на Мус+аси. Наша работа тут выполнена',
               en='Trent, dock with the Musashi. Our work here is done.'
        ),





        VoiceLine(1170, Trent, ru='Ну так, о чём речь.', en='So, what\'s this about.'),

        VoiceLine(1180, EdisonTrent,
                  ru='Если коротко - то всё плохо. Р+окфорд, как ты понял, решил "спасти" всё человечество. И сейчас ни СБА ни Орден помешать ему уже не могут.',
                      en='In short, everything\'s bad. Rockford, as you\'ve gathered, decided to \'save\' all of humanity. And right now neither the ASF nor the Order can stop him anymore.'),
        VoiceLine(1190, EdisonTrent, ru='А вот у тебя учитывая твою патологическую везучесть, может и получиться.', en='But you, with that pathological luck of yours, might actually pull it off.'),

        VoiceLine(1200, Trent, ru='А кто такой вообще этот Р+окфорд?', en='And who is this Rockford, anyway?'),

        VoiceLine(1210, EdisonTrent,
                  ru='Один человек, внезапно слетевший с катушек и задавшийся целью осчастливить человечество.',
                      en='A man who suddenly went off the rails and set out to make humanity happy.'),
        VoiceLine(1220, EdisonTrent,
                  ru='Проблема в том что в этом случае обычные клерки приносят в патентные бюро чертежи вечных двигателей, а вот фигуры масштаба Р+окфорда могут и уничтожить человечество, пока его же и спасает.',
                      en='The problem is, in that case ordinary clerks bring perpetual-motion blueprints to the patent office, while figures on Rockford\'s scale can destroy humanity while saving it.'),

        VoiceLine(1230, Trent, ru='А поконкретнее?', en='More specifically?'),

        VoiceLine(1240, EdisonTrent, ru='Аттикус Р+окфорд был ветераном Ордена.', en='Atticus Rockford was a veteran of the Order.'),
        VoiceLine(1250, EdisonTrent,
                  ru='Он очень болезненно отнесся к тому что Орден не смог предотвратить экспансию кочевников во время того инцедента и занялся изучением артефактов - так называемого наследия кочевников.',
                      en='He took it very hard that the Order failed to prevent the Nomad expansion during that incident, and he took up studying the artifacts, the so-called Nomad legacy.'),
        VoiceLine(1260, EdisonTrent,
                  ru='Именно он обнаружил ту самую Сферу, и каким-то образом понял что она - своего рода ящик Панд+оры, и содержит в себе смертоносную силу.',
                      en='He\'s the one who discovered that Sphere, and somehow realized it\'s a kind of Pandora\'s box, and holds a deadly force inside.'),
        VoiceLine(1270, EdisonTrent,
                  ru='Мы вместе работали над Сферой. Он нашел способ ее уничтожить, но руководство Ордена было категорически против.',
                      en='We worked on the Sphere together. He found a way to destroy it, but the Order\'s leadership was categorically against it.'),
        VoiceLine(1280, EdisonTrent,
                  ru='Тогда уже начал+а проявляться его маниакальность в достижении цели, а я понял, что ключ номадов сможет управлять сферой.',
                      en='That\'s when his mania for reaching the goal started to show, and I realized the Nomad key could control the Sphere.'),
        VoiceLine(1290, EdisonTrent,
                  ru='И решил удалиться подальше. Так что мое пленение кс+еносами было мною подстроено.',
                      en='And I decided to get far away. So my capture by the Xenos was staged by me.'),

        VoiceLine(1300, Trent, ru='И что теперь делать? Ключ у Р+окфорда и он может делать со Сферой всё что захочет. И никто не сможет ему помешать.', en='So what do we do now? Rockford has the key, and he can do whatever he wants with the Sphere. And no one can stop him.'),

        VoiceLine(1350, EdisonTrent,
                  ru='Не совсем так. Есть еще один ключ, я его забрал с собой, когда отправился к добровольное изгнание к Кс+еносам. Он абсолютно идентичен тому, что у Р+окфорда.',
                      en='Not quite. There\'s another key. I took it with me when I went into voluntary exile with the Xenos. It\'s absolutely identical to the one Rockford has.'),
        VoiceLine(1360, Trent, ru='И что мне с ним делать?', en='And what am I supposed to do with it?'),
        VoiceLine(1370, EdisonTrent,
                  ru='Решать тебе, но я бы в лучшие свои годы собрал силы Ордена или СБА и полетел бы прямо к сфере, пытаясь остановить Р+окфорда, пока это еще возможно.',
                      en='That\'s your call, but in my best years I would\'ve gathered Order or ASF forces and flown straight to the Sphere, trying to stop Rockford while it\'s still possible.'),
        VoiceLine(1380, Trent,
                  ru='Тогда почему ты не сделаешь это сам? Почему я?', en='Then why don\'t you do it yourself? Why me?'),

        VoiceLine(1390, EdisonTrent, ru='Потому что сейчас в данный момент у тебя больше друзей, чем у меня', en='Because right now, at this moment, you have more friends than I do.'),
        VoiceLine(1400, EdisonTrent, ru='В своё время утекло много вод+ы. Мне сейчас они не поверят. А тебе да. Так что ты в силах изменить ход истории', 
                  en='A lot of water has passed since my time. They won\'t believe me now. They will believe you. So you have the power to change the course of history.'),

        VoiceLine(1440, Trent, ru='И какова вероятность, что друзья мне помогут?', en='And what are the odds my friends will help?'),
        VoiceLine(1450, EdisonTrent, ru='Есть только один способ это проверить', en='There\'s only one way to find out.'),
        VoiceLine(1460, EdisonTrent, ru='Забери этот контейнер. Внутри него номадский ключ и все доступы которые могут тебе пригодится', en='Take this container. Inside is the Nomad key and all the access you might need.'),

        VoiceLine(1500, Trent, ru='Что же, это должно сработать. Рад был видеть!', en='Well, this ought to work. Good to have seen you!'),

        VoiceLine(1510, EdisonTrent, ru='И хандры как ни бывало. Где-ж мои 16 лет? Удачи, тезка!', en='And the gloom is gone like it never was. Where are my sixteen years? Good luck, namesake!'),

        VoiceLine(2010, Trent, ru='Хетчер, сл+ышишь меня?', en='Hatcher, can you hear me?'),
        VoiceLine(2020, Hatcher, ru='Да, Трент, что случилось?', en='Yes, Trent, what happened?'),
        VoiceLine(2030, Trent, ru='Срочно вылетай на планету Спр+ага, все подробности там!', en='Get to planet Sprague immediately, all the details are there!'),
        VoiceLine(2040, Hatcher, ru='М-да? Ладно, вылетаю.', en='Huh? Alright, heading out.'),

        VoiceLine(2050, Trent, ru='Д+ерси!', en='Darcy!'),
        VoiceLine(2060, Darcy, ru='Д+ерси здесь.', en='Darcy here.'),
        VoiceLine(2070, Trent, ru='Вылетай на планету Спрага. Прямо сейчас, всё объясню при встрече.', en='Get to planet Sprague. Right now, I\'ll explain everything when we meet.'),
        VoiceLine(2080, Darcy, ru='Опять что-то интересненькое? Лечу!', en='Something interesting again? I\'m on my way!'),

        VoiceLine(2090, Trent, ru='Аларик!', en='Alaric!'),
        VoiceLine(2100, Alaric, ru='А, Трент, ты как раз в+овремя, я хотел...', en='Ah, Trent, you\'re just in time, I wanted...'),
        VoiceLine(2110, Trent, ru='Стоп! Аларик, помолчи. Срочно вылетай на планету Спр+ага!', en='Stop! Alaric, be quiet. Get to planet Sprague, now!'),
        VoiceLine(2120, Alaric, ru='Как на Спр+агу?', en='To Sprague? How?'),
        VoiceLine(2130, Trent, ru='М+олча! Аларик, ты понял?', en='Quiet! Alaric, do you understand?'),
        VoiceLine(2140, Alaric, ru='Да.', en='Yes.'),
        VoiceLine(2150, Trent, ru='Вот и хорош+о.', en='Good.'),
        VoiceLine(2160, Alaric, ru='Но...', en='But...'),
        VoiceLine(2170, Trent, ru='М+олча, Аларик, м+олча.', en='Quiet, Alaric, quiet.'),


        VoiceLine(2180, Kim, ru='Трент, ты куда делся?', en='Trent, where did you go?'),
        VoiceLine(2190, Trent, ru='Я улетел', en='I flew off.'),
        VoiceLine(2200, Kim,
                  ru='У нас готовится спецоперация, нам нужны все доступные силы. Пункт сбора в Омеге-3, прилетай',
                      en='A special operation is being prepared, we need all available forces. Rally point is in Omega-3, get here.'),
        VoiceLine(2210, Kim,
                  ru='Ямамото гарантирует хорошее вознаграждение всем участникам, можешь вызывать своих друзей и всех кого можешь',
                      en='Yamamoto guarantees a good reward for everyone taking part. You can call your friends and anyone you can.'),
        VoiceLine(2220, Trent, ru='Нет. Ким, у меня появилось очень срочное и очень важное дело.', en='No. Kim, I\'ve got a very urgent and very important matter.'),
        VoiceLine(2230, Kim, ru='Настолько срочное и важное, что решил Ямамото послать?', en='So urgent and important that you\'d blow Yamamoto off?'),
        VoiceLine(2240, Trent, ru='Именно.', en='Exactly.'),
        VoiceLine(2250, Kim, ru='(после долгого молчания) Ну как знаешь...', en='Well, suit yourself...'),
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