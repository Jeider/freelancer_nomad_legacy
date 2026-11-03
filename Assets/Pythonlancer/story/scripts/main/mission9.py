from story import script
from audio.sound import VoiceLine
from story.actors import Trent, HatcherStation, Darcy, HasslerOrder, Yamamoto, Kim, SakuraOne, Chrysanthemum, Matome
from story.cutscenes.story_scenes import m09_deck, m09_yokohama, m09_order, m09_reward


class Msn9(object):
    MISSION_INDEX = 9


class Msn9DeckCutscene(Msn9, script.CutsceneProps):
    ALIAS = 'deck'
    TITLE = 'Стыковочный шлюз Йокогамы'
    DESCRIPTION = 'Трент и Дерси сели на станцию Йокогама и готовятся зайти в бар'
    THORN_CLASS = m09_deck.Msn9YokoDeckScene
    VOICE_LINES = [
        VoiceLine(
            10,
            Darcy,
            ru='Ну что,, Трент, гот+ов?',
            en="Well, Trent, ready?"
        ),
        VoiceLine(
            20,
            Trent,
            ru='К чему это?',
            en="For what?"
        ),
        VoiceLine(
            30,
            Darcy,
            ru='К встрече с информатором! Мы понятия не имеем,, сколько тут агентов Нового Ордена!',
            en="For the meeting with the informant! We have no idea how many New Order agents are here!"
        ),
        VoiceLine(
            40,
            Trent,
            ru='Так ты же у нас прикрытие! Или Бретонская корона уже не так+ая всесильная на территории Кус+ари?',
            en="But you're our cover! Or is the Bretonian Crown not so all-powerful in Kusari territory anymore?"
        ),
        VoiceLine(
            50,
            Darcy,
            ru='Эй, всё с нашей короной в порядке! Только от выстрелов лазерных пушек она не защищает! Так что будь покладистей!',
            en="Hey, our crown is just fine! It just doesn't protect you from laser cannon fire! So be a bit more obliging!"
        ),
        VoiceLine(
            60,
            Trent,
            ru='Как прикажете, мисс Д+ерси!',
            en="As you command, Miss Darcy!"
        ),
    ]


class Msn9YokohamaCutscene(Msn9, script.CutsceneProps):
    ALIAS = 'yokohama'
    TITLE = 'Верхний бар станции Йокогама'
    THORN_CLASS = m09_yokohama.Msn9YokohamaCutsceneThorn
    DESCRIPTION = ('Трент и Д+ерси проходят по бару. Посетители косятся на них и буквально прожигают взглядом. '
                   'Вскоре их находит Хасслер и предлагает встретиться с Ямамото.')
    VOICE_LINES = [
        VoiceLine(
            10,
            Trent,
            ru='Честно сказать, я нервничаю, когда все в баре, включая самого бармена, смотрят исключительно на меня.',
            en="Honestly, I get nervous when everyone in the bar, including the bartender himself, is looking only at me."
        ),
        VoiceLine(
            20,
            Darcy,
            ru='Тоже заметил, да?',
            en="You noticed too, huh?"
        ),
        VoiceLine(
            30,
            Trent,
            ru='Трудно на заметить. Они же не просто смотрят, они взглядом прожигают. Короче, если этот парламентер через полчаса не приходит - я сваливаю.',
            en="Hard not to notice. They're not just looking, they're burning holes with their eyes. Anyway, if this envoy doesn't show in half an hour, I'm out."
        ),
        VoiceLine(
            40,
            Darcy,
            ru='Полностью согласна.',
            en="I completely agree."
        ),
        VoiceLine(
            50,
            HasslerOrder,
            comment='Появление из-за спины',
            ru='Герр Трент, вы действительно верите, что бессмертны?',
            en="Herr Trent, do you really believe you're immortal?"
        ),
        VoiceLine(
            60,
            Trent,
            ru='Герр Хасслер? Рад видеть. Сегодня в штатском?',
            en="Herr Hassler? Good to see you. Out of uniform today?"
        ),
        VoiceLine(
            70,
            HasslerOrder,
            ru='С моей службой в Р+ейнланде покончено, герр Трент. Вам повезло лично увидеть закат моей военной карьеры.',
            en="My service in Rheinland is over, Herr Trent. You were lucky enough to personally witness the sunset of my military career."
        ),
        VoiceLine(
            80,
            HasslerOrder,
            ru='Но хватит про меня, в наших краях вы суперзвезда, за вашу голову назначена очень хорошая награда...',
            en="But enough about me. In our parts you're a superstar. There's a very good reward on your head..."
        ),
        VoiceLine(
            90,
            Trent,
            ru='О как... И чем обязан?',
            en="Oh... And to what do I owe this?"
        ),
        VoiceLine(
            100,
            HasslerOrder,
            ru='(с усмешкой) А вы даже и не в курсе. Ха-ха. '
               'Многие думают что специально, а я считаю - по незнанию, вы такое количество раз перешли дорогу Новому Ордену, '
               'что у руководства не то что нервные тики - судороги начались. ',
            en="(with a smirk) And you don't even know. Ha-ha. Many think it was on purpose, but I think it was out of ignorance. You've crossed the New Order so many times that the leadership doesn't just have nervous tics, the convulsions have started."
        ),
        VoiceLine(
            110,
            HasslerOrder,
            ru='И что характ+ерно - каждый раз вы вых+одите сух+им из вод+ы. '
               'Я бы даже сказал не просто сухим из вод+ы, а («снимает шляпу перед дамой») '
               'унося на руках красивую даму на фоне ядерного гриба.',
            en="And what's characteristic is, every time you come out of the water dry. I'd even say not just dry from the water, but (removes his hat to the lady) carrying a beautiful lady in your arms against a nuclear mushroom cloud."
        ),
        VoiceLine(
            120,
            Trent,
            ru='Именно поэтому на меня все здесь так пялятся?', en="So that's why everyone's staring at me here?"
        ),
        VoiceLine(
            130,
            HasslerOrder,
            ru='Конечно. После всех этих подвигов так просто заявиться в штаб-квартиру Нового Ордена. '
               'Впрочем, в данный момент вы в полной безопасности, как вам и было обещано.',
            en="Of course. After all these feats, to just show up at New Order headquarters. However, at the moment you are completely safe, as you were promised."
        ),
        VoiceLine(
            140,
            Trent,
            ru='Хасслер, в данный момент мне нужны ответы на пару вопросов.'
               'Первый и главный из них - где находится Аларик и что с ним?',
            en="Hassler, right now I need answers to a couple of questions. The first and main one is, where is Alaric, and what's happened to him?"
        ),
        VoiceLine(
            150,
            HasslerOrder,
            ru='Тогда вам лучше говорить не со мной, герр Трент, а с главой Нового Ордена, герром Ямамото.',
            en="Then you'd better talk not to me, Herr Trent, but to the head of the New Order, Herr Yamamoto."
        ),
        VoiceLine(
            160,
            Trent,
            ru='И вы сможете это устроить?', en="And you can arrange that?"
        ),
        VoiceLine(
            170,
            HasslerOrder,
            ru='Именно! Причем незамедлительно!', en="Exactly! And immediately!"
        ),
        VoiceLine(
            180,
            Darcy,
            ru='Разумно ли это, Трент?', en="Is this wise, Trent?"
        ),
        VoiceLine(
            190,
            HasslerOrder,
            ru='Вы и так находитесь в штаб-квартире Нового Ордена, бояться нужно было раньше. '
               'Ямамото-сан придерживается консервативных взглядов и очень уважает воинскую доблесть. ',
            en="You're already at New Order headquarters. You should have been afraid earlier. Yamamoto-san holds conservative views and has great respect for martial valor."
        ),
        VoiceLine(
            200,
            HasslerOrder,
            ru='Я рассказал ему о наших с вами совместных приключениях, и '
               ' как мне показалось, он проникся уважением к вам. Не думаю что вам что-то угрожает.',
            en="I told him about our adventures together, and it seemed to me he came to respect you. I don't think anything threatens you."
        ),
        VoiceLine(
            210,
            Trent,
            ru='Хорошо, пойдёт!', en="All right, that'll do!"
        ),
    ]


class Msn9OrderCutscene(Msn9, script.CutsceneProps):
    ALIAS = 'order'
    TITLE = 'Нижний бар станции Йокогама'
    THORN_CLASS = m09_order.Msn9OrderCutsceneThorn
    THORN_DECISION_CLASS = m09_order.Msn9OrderDecisionThorn
    THORN_ACCEPT_CLASS = m09_order.Msn9OrderAcceptThorn
    DESCRIPTION = 'Лифт открывается. Энергичная музыка, треш, угар и прочие штуки. Стриптизерши танцуют. Герои входят. Хасслер ведёт Трента и Дерси к столику Ямамото'
    'Они подходят к барной стойке, где их поджидает глава Нового Ордена - Ямамаото-сама'
    VOICE_LINES = [
        VoiceLine(
            10,
            HasslerOrder,
            ru='Герр Ямамото. Знакомьтесь - это герр Трент и фрау Д+ерси.',
            en="Herr Yamamoto. Meet Herr Trent and Frau Darcy."
        ),
        VoiceLine(
            20,
            Yamamoto,
            ru='(задумчиво-меланхолично, без пафоса) Мистер Трент, я думал, что в свои годы уже утратил способность удивляться, '
               'но вы меня просто поразили. По вашей истории можно написать приключенческий роман. А может и не один роман.',
            en="(thoughtful, melancholy, without pomp) Mister Trent, I thought that at my age I had already lost the ability to be surprised, but you have simply astonished me. One could write an adventure novel about your story. Or perhaps more than one novel."
        ),
        VoiceLine(
            30,
            Yamamoto,
            ru='Вчера вы никто, потом работаете на спецслужбу одного государства, потом становитесь врагом этого государства, '
               'но не теряете времени и начинаете работать на спецслужбу другого государства, '
               'с которой у вас потом тоже начинаются серьёзные неприятности.',
            en="Yesterday you were nobody, then you work for one state's intelligence service, then you become an enemy of that state, but you waste no time and start working for another state's intelligence service, with which you then also run into serious trouble."
        ),
        VoiceLine(
            40,
            Yamamoto,
            ru='Мимоходом отправляете в мусорную корзину долгосрочные планы надправительственной организации. '
               '(переход на доброжелательный тон) А теперь вот стоите здесь и мирно попиваете саке с её руководителем. ',
            en="In passing, you toss the long-term plans of a supra-governmental organization into the trash. (shifts to a friendly tone) And now here you stand, peacefully sipping sake with its leader."
        ),
        VoiceLine(
            50,
            Yamamoto,
            ru='(предложение) Кстати, саке, мистер Трент? Мисс Д+ерси?',
            en="(offering) By the way, sake, Mister Trent? Miss Darcy?"
        ),
        VoiceLine(
            60,
            Darcy,
            ru='(берет рюмку) Спасибо, Ямамото-с+ама.',
            en="(takes the cup) Thank you, Yamamoto-sama."
        ),
        VoiceLine(
            70,
            Trent,
            ru='(выпивши) Спасибо, мистер Ямамото, у меня к вам дело.',
            en="(having had a drink) Thank you, Mister Yamamoto. I have business with you."
        ),
        VoiceLine(
            80,
            Yamamoto,
            ru='(мудрец) Иначе вас бы здесь не было.',
            en="(the sage) Otherwise you wouldn't be here."
        ),
        VoiceLine(
            90,
            Trent,
            ru='Я должен найти Аттикуса Рокфорда.',
            en="I have to find Atticus Rockford."
        ),
        VoiceLine(
            100,
            Yamamoto,
            ru='(мягко, заранее зная ответ) И зачем?',
            en="(softly, already knowing the answer) And why?"
        ),
        VoiceLine(
            110,
            Trent,
            ru='(напряженно) У меня к нему личные счеты. ',
            en="(tense) I have a personal score to settle with him."
        ),
        VoiceLine(
            120,
            Yamamoto,
            ru='(саркастический намёк) У генерала Кинга, видимо тоже.',
            en="(a sarcastic hint) General King, it seems, does too."
        ),
        VoiceLine(
            130,
            Yamamoto,
            ru='(Серьезный тон) Не надо темнить, мистер Трент. Я не бармен, которому изливают душу.',
            en="(serious tone) Don't be evasive, Mister Trent. I'm not a bartender people pour their hearts out to."
        ),
        VoiceLine(
            140,
            Yamamoto,
            ru='(Саркастичский намёк) Кроме того, у меня появилось ощущение, что и к вам Кинг теплых чувств не испытывает.',
            en="(a sarcastic hint) Besides, I have a feeling King doesn't have warm feelings toward you either."

        ),
        VoiceLine(
            150,
            Yamamoto,
            ru='(Сюжетный поворот)...Если послал на самоубийство...',
            en="(plot twist)...If he sent you to commit suicide..."
        ),
        VoiceLine(
            160,
            Trent,
            ru='(удивлённо) Самоубийство?!',
            en="(surprised) Suicide?!"
        ),
        VoiceLine(
            170,
            Yamamoto,
            ru='Для того, чтобы ликвидировать Рокфорда не достаточно одного человека, даже такого везучего как вы, мистер Трент.',
            en="One person is not enough to eliminate Rockford, not even one as lucky as you, Mister Trent."
        ),
        VoiceLine(
            180,
            Trent,
            ru='(Уверенный и непоколебимый) Плевать на Кинга, мистер Ямамото, или, как вас правильно, Ямамото-сама? '
               'Я должен прикончить этого ублюдка и вернуть себе то, что он у меня украл.',
            en="(confident and unwavering) I don't give a damn about King, Mister Yamamoto, or, how should I address you, Yamamoto-sama? I have to finish this bastard and take back what he stole from me."
        ),
        VoiceLine(
            190,
            Yamamoto,
            ru='(просит бармена подлить саке, рассуждает) Я вам немного завидую, мистер Трент. Вы молодой, в вас есть страсть...',
            en="(asks the bartender for more sake, reflecting) I envy you a little, Mister Trent. You're young, there's passion in you..."
        ),
        VoiceLine(
            200,
            Yamamoto,
            ru='(После глотка саке) Я готов помочь вам, Рокфорд и у нас, как там, "кость в горле", правильно?',
            en="(after a sip of sake) I'm ready to help you. Rockford is, for us as well, how does it go, \"a bone in the throat\", correct?"
        ),
        VoiceLine(
            210,
            Yamamoto,
            ru='Но если вы хотите, чтобы я помог вам, окажите и нам одну услугу.',
            en="But if you want me to help you, do us one favor as well."
        ),
        VoiceLine(
            220,
            Trent,
            ru='И в чем же она заключается?',
            en="And what does it involve?"
        ),
        VoiceLine(
            230,
            Yamamoto,
            ru='(не напрягаясь) Нам нужно разместить специальные сканеры и обеспечить их долговременную работу.',
            en="(offhand) We need to place special scanners and keep them working long-term."
        ),
        VoiceLine(
            240,
            Trent,
            ru='(и это всё? пффф) Уфф, интересная работа... А можно подробнее?',
            en="(and that's all? pfft) Oof, interesting work... Can I have more detail?"
        ),
        VoiceLine(
            250,
            Yamamoto,
            ru='Нас интересует система Энтерпрайз. И все защитные мероприятия, которые были проведены СБА после распада Ордена. '
               'У нас есть технические средства, чтобы получить интересующую нас информацию. ',
            en="We're interested in the Enterprise system. And all the defensive measures the ASF carried out after the Order's collapse. We have the technical means to obtain the information we're interested in."
        ),
        VoiceLine(
            260,
            Yamamoto,
            ru='Их нужно разместить и удерживать в системе Сириус, охраняемой патрулями... '
               '(обрываем на высшей точке, фраза будет продолжена Трентом)',
            en="They need to be placed and held in the Sirius system, which is patrolled by... (cut off at the high point, the line will be continued by Trent)"
        ),
        VoiceLine(
            270,
            Trent,
            ru='(печальный выдох)СБА...',
            en="(a sad sigh) The ASF..."
        ),
        VoiceLine(
            280,
            Yamamoto,
            ru='Итак, мистер Трент, вы согласны?',
            en="So, Mister Trent, do you agree?"
        ),
        VoiceLine(
            290,
            Trent,
            ru='(А чё нет) А почему бы и нет.',
            en="(why not) Well, why not."
        ),
        VoiceLine(
            320,
            Yamamoto,
            ru='В таком случае, можете вылетать в космос. С вами свяжется лейтенант Ким. Он будет руководить операцией.',
            en="In that case, you may launch into space. Lieutenant Kim will contact you. He will lead the operation."
        ),
        VoiceLine(
            350,
            Darcy,
            ru='Трент, ты в своём уме? Эта операция против СБА',
            en="Trent, are you in your right mind? This operation is against the ASF."
        ),
        VoiceLine(
            360,
            Trent,
            ru='(тёмные мысли, стоически) У меня уже давно ощущение, что я против всех, Д+ерси, остались только временные союзники.',
            en="(dark thoughts, stoically) For a long time now I've had the feeling I'm against everyone, Darcy. Only temporary allies left."
        ),
    ]


class Msn9RewardCutscene(Msn9, script.CutsceneProps):
    ALIAS = 'reward'
    TITLE = 'Ангар линкора Мусаси'
    DESCRIPTION = 'Это была тяжелая миссия. Трент, Дерси и Ким подходят к Хасслеру. Ким в бешенстве.'
    THORN_CLASS = m09_reward.Msn9RewardCutsceneThorn
    VOICE_LINES = [
        VoiceLine(
            10,
            Kim,
            ru='(грубо) Эта операция была безрассудной',
            en="(rudely) This operation was reckless."
        ),
        VoiceLine(
            20,
            HasslerOrder,
            ru='Ким, давай остынь',
            en="Kim, cool off."
        ),
        VoiceLine(
            30,
            Kim,
            ru='(грубо) Теперь выполни свою часть работы, чтобы наша жертва не была напрасной',
            en="(rudely) Now do your part of the work, so our sacrifice wasn't in vain."
        ),
        VoiceLine(
            40,
            HasslerOrder,
            ru='Так и будет. Я гарантирую это',
            en="So it will be. I guarantee it."
        ),

        VoiceLine(
            100,
            Trent,
            ru='Ей, Хасслер, тут все такие безбашенные?',
            en="Hey, Hassler, is everyone here this unhinged?"
        ),
        VoiceLine(
            110,
            HasslerOrder,
            ru='Не все, герр Трент. Но целеустремленность этих людей и правда воодушевляет',
            en="Not everyone, Herr Trent. But these people's determination really is inspiring."
        ),
        VoiceLine(
            120,
            Trent,
            ru='Это точно, а что теперь делать?',
            en="That's for sure. So what now?"
        ),
        VoiceLine(
            130,
            HasslerOrder,
            ru='Пока нужно отдохнуть. Для вас и фрау Д+ерси на линкоре выделены индивидуальные каюты, вас проводят',
            en="For now you need to rest. Private cabins have been set aside for you and Frau Darcy on the battleship. You'll be shown to them."
        ),
    ]


class Msn9Space(Msn9, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(
            0,
            HatcherStation,
            comment='интро-диалог',
            ru='Трент, мы связались с представителями Нового Ордена. Они готовы к встрече и гарантируют безопасность, '
               'но для надежности ты должен придти на встречу вместе с Д+ерси. Место встречи: станция Йокогама, система Омега-3.',
            en="Trent, we've contacted representatives of the New Order. They're ready to meet and they guarantee safety, but to be sure you must come to the meeting together with Darcy. Meeting place: Yokohama Station, Omega-3 system."
        ),

        VoiceLine(200, Kim, comment='Операция',
                  ru='Мистер Трент, я лейтенант Ким. Я буду руководить операцией. '
                     'А это Мат+омэ, он будет управлять инженерными войсками',
                  en="Mister Trent, I'm Lieutenant Kim. I'll be leading the operation. And this is Matome. He'll be commanding the engineering troops."),
        VoiceLine(210, Kim,
                  ru='Нам нужно добраться в место сбора в системе Сириус. Я отметил точки пути в вашей нейросети',
                  en="We need to get to the rally point in the Sirius system. I've marked the waypoints in your neural net."),

        VoiceLine(300, Matome,
                  ru='Это больш+ая честь участвовать в операции вместе с вами мистер Трент. У вас благородная репутация. Хоть вы и работали на СБА',
                  en="It's a great honor to take part in an operation with you, Mister Trent. You have a noble reputation. Even though you worked for the ASF."),

        VoiceLine(310, Trent,
                  ru='А чем вам не нравится СБА? Вроде же ребята официалы, с пиратами не сотрудничают. В отличие от...',
                  en="And what don't you like about the ASF? They seem like the official side. They don't work with pirates. Unlike..."),

        VoiceLine(325, Kim,
                  ru='Мы понимаем ваши намёки, мистер Трент. Орден занимается этим. Мы создаем зону всеобщего процветания в Сириусе',
                  en="We understand your hints, Mister Trent. The Order does that. We are creating a zone of universal prosperity in Sirius."),

        VoiceLine(326, Trent, ru='Зону всепроцветания?', en="A zone of total prosperity?"),

        VoiceLine(328, Kim,
                  ru='Именно. К примеру, после нашего прихода во внешние миры наконец добралась цивилизация',
                  en="Exactly. For example, after we arrived, civilization finally reached the outer worlds."),
        VoiceLine(330, Kim,
                  ru='Мы занимаемся инфраструктурой, терраформировали Мальту. Искоренили производство Кардамина. Теперь испанцы живут лучше',
                  en="We work on infrastructure. We terraformed Malta. We eradicated Cardamine production. Now the Spanish live better."),

        VoiceLine(340, Trent,
                  ru='Но это все равно не мешает корсарам продолжать совершать набеги и терроризировать Сириус',
                  en="But that still doesn't stop the Corsairs from raiding and terrorizing Sirius."),
        VoiceLine(350, Darcy,
                  ru='Да и проблему наркотиков в целом это не решило. А то я знаю знакомых принцесс, которые любят припудрить свой носик',
                  en="And it didn't solve the drug problem as a whole. I happen to know some princesses who like to powder their noses."),
        VoiceLine(355, Darcy, ru='Преимущественно изнутри, если вы понимаете о чём я.',
                  en="Mostly from the inside, if you know what I mean."),

        VoiceLine(360, Kim,
                  ru='Всему своё время, мисс Д+ерси. Мы не можем решить все противоречия сразу. Особенно в то время, когда СБА проводит такую политику протекционизма',
                  en="All in good time, Miss Darcy. We can't resolve all the contradictions at once. Especially at a time when the ASF is pursuing such a policy of protectionism."),
        VoiceLine(370, Matome,
                  ru='СБА больше заинтересованы в защите мифического ящика Панд+оры вместо того, чтобы реально помогать людям и решать их проблемы',
                  en="The ASF is more interested in protecting a mythical Pandora's box than in actually helping people and solving their problems."),

        VoiceLine(380, Trent, ru='Очень хочется надеяться, что вы действительно говорите правду',
                  en="I'd really like to hope that you're actually telling the truth."),

        VoiceLine(390, Kim, ru='Не сомневайтесь мистер Трент. Тем более, что сегодня вы нам с этим поможете',
                  en="Have no doubt, Mister Trent. Especially since today you'll be helping us with this."),

        VoiceLine(450, Kim,
                  ru='Мистер Трент, мисс Д+ерси, нам нужно присоединиться к транспортному конвою. Я указал точку в вашей нейросети.',
                  en="Mister Trent, Miss Darcy, we need to join the transport convoy. I've marked the point in your neural net."),

        VoiceLine(500, Kim,
                  ru='Итак. Порядок действий такой - мы добираемся вместе с транспортом до точки размещения сканера.',
                  en="So. The procedure is this: we reach the scanner deployment point together with the transport."),
        VoiceLine(510, Kim,
                  ru='По периметру области обеспечения находятся буи-детекторы кораблей противника. Обеспечивают нам дистанционную пеленгацию.',
                  en="Around the perimeter of the support area are buoys that detect enemy ships. They give us long-range direction finding."),
        VoiceLine(520, Kim,
                  ru='Вокруг каждого буя небольшая команда прикрытия. Мой отряд и вы - оперативные силы.',
                  en="Around each buoy is a small cover team. My squad and you are the operational force."),
        VoiceLine(530, Kim, ru='Выдвигаемся в сторону наибольшей угрозы и ликвидируем её. Все ясно?',
                  en="We move toward the greatest threat and eliminate it. Is that clear?"),
        VoiceLine(540, Trent, ru='Вполне.', en="Quite."),
        VoiceLine(550, Darcy, ru='Да.', en="Yes."),

        VoiceLine(610, Trent, ru='И вы думаете что на этом отшибе системы нас заметят?',
                  en="And you think they'll spot us out in this back end of the system?"),
        VoiceLine(620, Kim, ru='Сейчас нет. Но они смогут запеленговать Хризантему, когда мы её запустим',
                  en="Not now. But they'll be able to get a bearing on the Chrysanthemum once we start it up."),
        VoiceLine(630, Trent, ru='Значит у нас не так много времени. Долго собирать эту махину?',
                  en="So we don't have much time. Will it take long to assemble this hulk?"),

        VoiceLine(640, Matome, ru='Мои люди профессионалы своего дела. Мы сделаем свою работу быстро.',
                  en="My people are professionals. We'll do our job quickly."),
        VoiceLine(650, Matome,
                  ru='А вы должн+ы всеми силами отвлечь СБА от Хризантемы, пока она будет работать',
                  en="And you must do everything you can to draw the ASF away from the Chrysanthemum while it's working."),

        VoiceLine(660, Trent, ru='Сделаю всё, что могу', en="I'll do everything I can."),

        VoiceLine(680, Matome, ru='Мы на месте. Приступаем к сборке Хризантемы',
                  en="We're on site. Starting assembly of the Chrysanthemum."),

        VoiceLine(700, SakuraOne, ru='Сакура на связи, наш сканер фиксирует приближение патруля',
                  en="Sakura here. Our scanner is picking up an approaching patrol."),
        VoiceLine(710, Kim,
                  ru='А вот и они. Слишком быстро. Мистер Трент, летим на помощь Сакуре. Мисс Д+ерси, прикрывайте инженеров',
                  en="And there they are. Too fast. Mister Trent, we're flying to help Sakura. Miss Darcy, cover the engineers."),
        VoiceLine(720, Darcy, ru='Поняла, буду тут', en="Got it. I'll be here."),

        VoiceLine(730, Kim, ru='Сакура, статус', en="Sakura, status."),
        VoiceLine(740, SakuraOne, ru='Летят в нашу сторону', en="They're flying our way."),
        VoiceLine(750, Kim,
                  ru='Постараемся их пропустить. Мистер Трент, нам нужно поставить свои корабли как можно ближе к датчику, чтобы снизить нашу заметность',
                  en="We'll try to let them pass. Mister Trent, we need to put our ships as close to the sensor as possible to reduce our visibility."),

        VoiceLine(760, Kim, ru='Трент, ты что творишь. Нас так заметят! Ср+очно подлети к датчику!',
                  en="Trent, what are you doing. They'll spot us like this! Get to the sensor, now!"),

        VoiceLine(765, Kim, ru='Не двигаться! Сто+им ждём!', en="Don't move! We hold and wait!"),
        VoiceLine(770, Kim, ru='Пролетели мимо. Пронесл+о', en="They flew past. We slipped by."),

        VoiceLine(800, Matome, ru='Хризантема собрана. Запускаем сканирование',
                  en="The Chrysanthemum is assembled. Starting the scan."),

        VoiceLine(810, SakuraOne,
                  ru='Внимание! Патруль разворачивается! Скорее всего мы обнаружены! Летит к Хризантеме!',
                  en="Attention! The patrol is turning around! We've most likely been detected! It's flying toward the Chrysanthemum!"),
        VoiceLine(820, Kim, ru='Аах, к чёрту всё! Дайте нам их местоположение, летим на перехват',
                  en="Aah, to hell with it all! Give us their position. We're flying to intercept."),

        VoiceLine(830, Kim, ru='Уничтожить патруль СБА!', en="Destroy the ASF patrol!"),

        VoiceLine(840, Kim, ru='Хризантема, статус', en="Chrysanthemum, status."),
        VoiceLine(850, Chrysanthemum,
                  ru='Датчики фиксируют приближение еще одного патруля. На этот раз они вызвали тяжелую технику',
                  en="Sensors are detecting another patrol approaching. This time they've called in heavy equipment."),
        VoiceLine(860, Kim, ru='Летим на перехват', en="Flying to intercept."),

        VoiceLine(870, Trent, ru='А этот отряд уже более серьёзный.',
                  en="And this squad is already more serious."),
        VoiceLine(880, Kim, ru='Всё верно, они явно готовят группу зачистки.',
                  en="That's right. They're clearly preparing a cleanup team."),

        VoiceLine(890, Kim, ru='Атакуйте уязвимые точки Канонерок! Они не должн+ы добраться до Хризантемы!',
                  en="Attack the gunboats' weak points! They must not reach the Chrysanthemum!"),

        VoiceLine(900, Kim, ru='Канонерки уничтожены', en="Gunboats destroyed."),

        VoiceLine(910, Chrysanthemum, ru='Внимание! Приближаются значительные силы противника! Эсминцы!',
                  en="Attention! Significant enemy forces approaching! Destroyers!"),
        VoiceLine(920, Kim,
                  ru="А вот и вражеская кавалерия. Хризантема, дайте нам ближайшие координаты. Постараемся атаковать врага на подлёте",
                  en="And here's the enemy cavalry. Chrysanthemum, give us the nearest coordinates. We'll try to attack the enemy on approach."),

        VoiceLine(950, Kim,
                  ru='Атакуйте эсминцы! Нужно повредить их до того как они в+ыйдут на огневую позицию!',
                  en="Attack the destroyers! We need to damage them before they reach firing position!"),
        VoiceLine(960, Kim, ru='Атакуйте двигатели, пилоны, всё что угодно!',
                  en="Attack the engines, the pylons, anything!"),

        VoiceLine(980, Kim, ru='Эсминцы стали выход+ить на боевой рубеж',
                  en="The destroyers have started moving to the line of battle."),
        VoiceLine(985, Kim, ru='Трент, нужно уничтожить торпеды. Мы должн+ы защитить Хризантему любой ценой',
                  en="Trent, we need to destroy the torpedoes. We must protect the Chrysanthemum at any cost."),

        VoiceLine(1000, Chrysanthemum, ru='Приближается новая группа эсминцев',
                  en="A new group of destroyers is approaching."),
        VoiceLine(1010, Chrysanthemum, ru='Замечено новое вражеское подкрепление',
                  en="New enemy reinforcement spotted."),
        VoiceLine(1020, Chrysanthemum, ru='Новая группа эсминцев готовится к залпу',
                  en="A new group of destroyers is preparing for a salvo."),
        VoiceLine(1030, Chrysanthemum, ru='Еще группа эсминцев на изгот+овке',
                  en="Another group of destroyers is standing ready."),
        VoiceLine(1035, Chrysanthemum, ru='Прилетело еще одно звено вражеских эсминцев',
                  en="Another flight of enemy destroyers has flown in."),

        VoiceLine(1050, Chrysanthemum, ru='Мы получили удар торпедой! Прикрытие, сделайте что-нибудь!',
                  en="We've been hit by a torpedo! Cover, do something!"),
        VoiceLine(1060, Chrysanthemum, ru='Хризантема получила повреждения!',
                  en="The Chrysanthemum has taken damage!"),
        VoiceLine(1070, Chrysanthemum, ru='Хризантема получила серьезные повреждения! Требуется помощь!',
                  en="The Chrysanthemum has taken serious damage! Assistance required!"),

        VoiceLine(1080, Kim, ru='Нет... мы потеряли Хризантему до завершения сканирования. Это провал',
                  en="No... we lost the Chrysanthemum before the scan was finished. This is a failure."),

        VoiceLine(1100, Kim, ru='Мат+омэ, как идет сканирование', en="Matome, how's the scan going?"),
        VoiceLine(1110, Matome, ru='Готово на 50 процентов. Нам нужно еще время',
                  en="Fifty percent done. We need more time."),

        VoiceLine(1120, Matome, ru='Сканирование проведено на 70 процентов', en="Scan is seventy percent complete."),
        VoiceLine(1140, Matome, ru='Сканирование проведено на 90 процентов. Еще немного!',
                  en="Scan is ninety percent complete. A little more!"),
        VoiceLine(1170, Matome, ru='Сканирование завершено!', en="Scan complete!"),

        VoiceLine(1200, Kim, ru='Хризантема включайте самоуничтожение и эвакуируйтесь.',
                  en="Chrysanthemum, activate self-destruct and evacuate."),
        VoiceLine(1210, Kim, ru='Трент, подбери капсулу с хризантемы',
                  en="Trent, pick up the capsule from the Chrysanthemum."),

        VoiceLine(1250, Kim, ru='Уходим!', en="We're leaving!"),

        VoiceLine(1300, SakuraOne, ru='Прибыли вражеские линкоры! Пути отступления перекрыты! Мы окружены!',
                  en="Enemy battleships have arrived! Retreat routes are cut off! We're surrounded!"),

        VoiceLine(1310, Matome,
                  ru='Ким, нам нужно сделать отвлекающий ман+ёвр. Эти данные слишком важны для Ордена',
                  en="Kim, we need to make a diversion. This data is too important for the Order."),
        VoiceLine(1320, Kim, ru='И что ты предлагаешь', en="And what do you propose?"),

        VoiceLine(1330, Matome,
                  ru='Мы совершим атаку камикадзе и отвлечем вражеские силы. А вы уход+ите и доставьте данные на Мус+аси сами',
                  en="We'll make a kamikaze attack and draw off the enemy forces. And you leave, and deliver the data to the Musashi yourselves."),
        VoiceLine(1340, Kim, ru='Мат+омэ, идиот, остановись!', en="Matome, you idiot, stop!",
                  cinematic=True),

        VoiceLine(1350, Matome, ru='Это наш единственный шанс! Прощай друг!',
                  en="This is our only chance! Goodbye, friend!",
                  cinematic=True),
        VoiceLine(1355, Matome, ru='Банзай!', en="Banzai!",
                  cinematic=True),

        VoiceLine(1360, Kim, ru='Стой! Нет!', en="Stop! No!",
                  cinematic=True),

        VoiceLine(1400, Darcy, ru='Кажется нам пор+а уходить', en="I think it's time for us to leave."),
        VoiceLine(1410, Kim, ru='Всё верно мисс Д+ерси. Летим к указанной точке пути',
                  en="That's right, Miss Darcy. We're flying to the designated waypoint."),

        VoiceLine(1420, HasslerOrder, ru='Мус+аси на связи. Ким, наш статус',
                  en="Musashi here. Kim, our status."),
        VoiceLine(1430, Kim, ru='Данные успешно получены. Но прикрытие потеряно полностью',
                  en="Data successfully obtained. But the cover is completely lost."),

        VoiceLine(1500, HasslerOrder,
                  ru='Они погибли во славу Ордена. Садитесь на Мус+аси. Нужно скорее убираться отсюда',
                  en="They died for the glory of the Order. Dock with the Musashi. We need to get out of here quickly."),
    ]

class Mission9(Msn9, script.StoryMission):
    MISSION_INDEX = 9
    CUTSCENES = [
        Msn9DeckCutscene,
        Msn9YokohamaCutscene,
        Msn9OrderCutscene,
        Msn9RewardCutscene,
    ]
    SPACE_CLASS = Msn9Space
    SYNC_SPACE = True
    SYNC_SUBS = True

    MISSION_TITLE = 'Миссия 9. Услуга Новому Ордену'