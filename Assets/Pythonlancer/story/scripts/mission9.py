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
            en="Ready for what?"
        ),
        VoiceLine(
            30,
            Darcy,
            ru='К встрече с информатором! Мы понятия не имеем,, сколько тут агентов Нового Ордена!',
            en="To meet the informant! We have no idea how many New Order agents are here!"
        ),
        VoiceLine(
            40,
            Trent,
            ru='Так ты же у нас прикрытие! Или Бретонская корона уже не так+ая всесильная на территории Кус+ари?',
            en="I thought YOU were our cover! Or has the Bretonian Crown lost its influence in Kusari territory?"
        ),
        VoiceLine(
            50,
            Darcy,
            ru='Эй, всё с нашей короной в порядке! Только от выстрелов лазерных пушек она не защищает! Так что будь покладистей!',
            en="Hey, the Crown is doing just fine! But it doesn't stop laser cannon bolts! So play nice!"
        ),
        VoiceLine(
            60,
            Trent,
            ru='Как прикажете, мисс Д+ерси!',
            en="As you wish, Miss Darcy!"
        ),
    ]


class Msn9YokohamaCutscene(Msn9, script.CutsceneProps):
    ALIAS = 'yokohama'
    TITLE = 'Верхний бар станции Йокогама'
    THORN_CLASS = m09_yokohama.Msn9YokohamaCutsceneThorn
    DESCRIPTION = 'Трент и Д+ерси проходят по бару. Посетители косятся на них и буквально прожигают взглядом. '
    'Вскоре их находит Хасслер и проводит к лифту. Они едут вниз.'
    VOICE_LINES = [
        VoiceLine(
            10,
            Trent,
            ru='Честно сказать, я нервничаю, когда все в баре, включая самого бармена, смотрят исключительно на меня.',
            en="I'll be honest, it makes me nervous when everyone in the bar, including the bartender, is staring only at me."
        ),
        VoiceLine(
            20,
            Darcy,
            ru='Тоже заметил, да?',
            en="You noticed it too, huh?"
        ),
        VoiceLine(
            30,
            Trent,
            ru='Трудно на заметить. Они же не просто смотрят, они взглядом прожигают. Короче, если этот парламентер через полчаса не приходит - я сваливаю.',
            en="Hard not to. They're not just looking, they're staring a hole through me. Anyway, if this emissary isn't here in thirty minutes, I'm out."
        ),
        VoiceLine(
            40,
            Darcy,
            ru='Полностью согласна.',
            en="Couldn't agree more."
        ),
        VoiceLine(
            50,
            HasslerOrder,
            ru='Герр Трент, вы действительно верите, что бессмертны?',
            en="Herr Trent, do you truly believe you are immortal?"
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
            ru='С моей службой в Р+ейнланде покончено герр Трент. Вам повезло лично увидеть закат моей военной карьеры.',
            en="My service with Rheinland is over, Herr Trent. You are fortunate to witness the sunset of my military career in person."
        ),
        VoiceLine(
            80,
            HasslerOrder,
            ru='Но хватит про меня, в наших краях вы суперзвезда, за вашу голову назначена очень хорошая награда...',
            en="But enough about me. Around these parts, you are a superstar. There is a very substantial bounty on your head..."
        ),
        VoiceLine(
            90,
            Trent,
            ru='О как... И чем обязан?',
            en="Is that so... And what do I owe the pleasure?"
        ),
        VoiceLine(
            100,
            HasslerOrder,
            ru='(с усмешкой) А вы даже и не в курсе. Ха-ха. '
               'Многие думают что специально, а я считаю - по незнанию, вы такое количество раз перешли дорогу Новому Ордену, '
               'что у руководства не то что нервные тики - судороги начались. ',
            en="(Chuckles) And you aren't even aware. Ha-ha. "
               "Many think it's intentional, but I believe it's out of ignorance. You have crossed the New Order so many times "
               "hat its leadership doesn't just have nervous tics — they're having full-blown seizures."
        ),
        VoiceLine(
            110,
            HasslerOrder,
            ru='И что характ+ерно - каждый раз вы вых+одите сух+им из вод+ы. '
               'Я бы даже сказал не просто сухим из вод+ы, а («снимает шляпу перед дамой») '
               'унося на руках красивую девушку на фоне ядерного гриба.',
            en="I'd even say not just without a scratch, but "
               "walking away with a beautiful girl in your arms against the backdrop of a nuclear mushroom cloud."
        ),
        VoiceLine(
            120,
            Trent,
            ru='Именно поэтому на меня все здесь так пялятся?', en="Is that why everyone here is gawking at me?"
        ),
        VoiceLine(
            130,
            HasslerOrder,
            ru='Конечно. После всех этих подвигов так просто заявиться в штаб-квартиру Нового Ордена. '
               'Впрочем, в данный момент вы в полной безопасности, как вам и было обещано.',
            en="Of course. To just waltz into the New Order's headquarters after all those exploits... "
               'Nevertheless, at this moment, you are perfectly safe, as was promised to you.'
        ),
        VoiceLine(
            140,
            Trent,
            ru='Хасслер, в данный момент мне нужны ответы на пару вопросов.'
               'Первый и главный из них - где находится Аларик и что с ним?',
            en="Hassler, right now I need answers to a couple of questions. "
               'The first and most important one is: where is Alaric and what happened to him?'
        ),
        VoiceLine(
            150,
            HasslerOrder,
            ru='Тогда вам лучше говорить не со мной герр Трент, а с главой Нового Ордена, герром Ямамото.',
            en="Then you'd better speak not with me, Herr Trent, but with the head of the New Order, Herr Yamamoto."
        ),
        VoiceLine(
            160,
            Trent,
            ru='И вы сможете это устроить?', en="And you can arrange that?"
        ),
        VoiceLine(
            170,
            HasslerOrder,
            ru='Именно! Причем незамедлительно!', en="Precisely! And immediately!"
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
               'Ямамото-с+ама (-сама - это уважительный суффикс при обращении к мужчине в японии. как у нас господин или в германии герр) '
               'придерживается консервативных взглядов и очень уважает воинскую доблесть. ',
            en="You are already in the New Order's headquarters. You should have been afraid earlier. "
               'Yamamoto-sama holds conservative views and deeply respects martial prowess.'
        ),
        VoiceLine(
            200,
            HasslerOrder,
            ru='Я рассказал ему о наших с вами совместных приключениях, и '
               ' как мне показалось он проникся уважением к вам. Не думаю что вам что-то угрожает.',
            en="I told him about our past adventures together, "
               'and it seemed to me he developed a certain respect for you. I don\'t believe you are in any danger.'
        ),
        VoiceLine(
            210,
            Trent,
            ru='Хорошо, пойдёт!', en="Alright, let's do it!"
        ),
    ]


class Msn9OrderCutscene(Msn9, script.CutsceneProps):
    ALIAS = 'order'
    TITLE = 'Нижний бар станции Йокогама'
    THORN_CLASS = m09_order.Msn9OrderCutsceneThorn
    THORN_DECISION_CLASS = m09_order.Msn9OrderDecisionThorn
    THORN_ACCEPT_CLASS = m09_order.Msn9OrderAcceptThorn
    DESCRIPTION = 'Лифт открывается. Энергичная музыка, треш, угар и прочие штуки. Стриптизерши танцуют. Герои входят'
    'Они подходят к барной стойке, где их поджидает глава Нового Ордена - Ямамаото-сама'
    VOICE_LINES = [
        VoiceLine(
            10,
            HasslerOrder,
            ru='Герр Ямамото, герр Трент, фрау Д+ерси.',
            en="Herr Yamamoto, Herr Trent, Frau Darcy."
        ),
        VoiceLine(
            20,
            Yamamoto,
            ru='(задумчиво-меланхолично, без пафсоа) Мистер Трент, я думал, что в свои годы уже утратил способность удивляться, '
               'но вы меня просто поразили. По вашей истории можно написать приключенческий роман. А может и не один роман.',
            en="Mr. Trent, I thought at my age I had lost the capacity for surprise, but you have simply astonished me. "
               'One could write an adventure novel based on your story. Perhaps even several.'
        ),
        VoiceLine(
            30,
            Yamamoto,
            ru='Вчера вы никто, потом работаете на спецслужбу одного государства, потом становитесь врагом этого государства, '
               'но не теряете времени и начинаете работать на спецслужбу другого государства, '
               'с которой у вас потом тоже начинаются серьёзные неприятности.',
            en="One day you are a nobody, the next you work for the intelligence service of one state, then you become an enemy of that state, "
               'but waste no time and begin working for the intelligence service of another, '
               'with whom you also eventually find yourself in serious trouble.'
        ),
        VoiceLine(
            40,
            Yamamoto,
            ru='Мимоходом отправляете в мусорную корзину долгосрочные планы надправительственной организации. '
               '(переход на доброжелательный тон) А теперь вот стоите здесь и мирно попиваете саке с её руководителем. ',
            en="Along the way, you casually consign the long-term plans of a supra-governmental organization to the trash bin. "
               '(Yamamoto shifts to a benevolent tone) And now, here you stand, peacefully sipping sake with its leader.'
        ),
        VoiceLine(
            50,
            Yamamoto,
            ru='(предложение) Кстати, саке, мистер Трент? Мисс Д+ерси?',
            en="Some sake, Mr. Trent? Miss Darcy?"
        ),
        VoiceLine(
            60,
            Darcy,
            ru='(берет рюмку) Спасибо, Ямамото-с+ама.',
            en="Thank you, Yamamoto-sama."
        ),
        VoiceLine(
            70,
            Trent,
            ru='(выпивши) Спасибо, мистер Ямамото, у меня к вам дело.',
            en="Thank you, Mr. Yamamoto. I have business with you."
        ),
        VoiceLine(
            80,
            Yamamoto,
            ru='(мудрец) Иначе вас бы здесь не было.',
            en="Otherwise, you would not be here."
        ),
        VoiceLine(
            90,
            Trent,
            ru='Я должен найти Аттикуса Рокфорда.',
            en="I need to find Atticus Rockford."
        ),
        VoiceLine(
            100,
            Yamamoto,
            ru='(мягко, заранее зная ответ) И зачем?',
            en="(in a soft tone, already knowing the answer) And why is that?"
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
            en="(with a sarcastic hint) As does General King, it would seem."
        ),
        VoiceLine(
            130,
            Yamamoto,
            ru='(Серьезный тон) Не надо темнить, мистер Трент. Я не бармен, которому изливают душу.',
            en="(turning serious) Do not be evasive, Mr. Trent. I am not a bartender for you to pour your heart out to."
        ),
        VoiceLine(
            140,
            Yamamoto,
            ru='(Саркастичский намёк) Кроме того, у меня появилось ощущение, что и к вам Кинг теплых чувств не испытывает.',
            en="(sarcastic again) Besides, I have a feeling King doesn't hold warm feelings for you either..."

        ),
        VoiceLine(
            150,
            Yamamoto,
            ru='(Сюжетный поворот)...Если послал на самоубийство...',
            en="(revealing a plot twist) if he sent you on a suicide mission..."
        ),
        VoiceLine(
            160,
            Trent,
            ru='(удивлённо) Самоубийство?!',
            en="A suicide mission?!"
        ),
        VoiceLine(
            170,
            Yamamoto,
            ru='Для того, чтобы ликвидировать Рокфорда не достаточно одного человека, даже такого везучего как вы, мистер Трент.',
            en="To eliminate Rockford, one man is not enough. Not even one as fortunate as you, Mr. Trent."
        ),
        VoiceLine(
            180,
            Trent,
            ru='(Уверенный и непоколебимый) Плевать на Кинга, мистер Ямамото, или, как вас правильно, Ямамото-сама? '
               'Я должен прикончить этого ублюдка и вернуть себе то, что он у меня украл.',
            en="(confident and unwavering) I don't give a damn about King, Mr. Yamamoto, or should I say, Yamamoto-sama? "
               'I have to kill that bastard and take back what he stole from me.'
        ),
        VoiceLine(
            190,
            Yamamoto,
            ru='(просит бармена подлить саке, рассуждает) Я вам немного завидую, мистер Трент. Вы молодой, в вас есть страсть...',
            en="I envy you a little, Mr. Trent. You are young, you have passion..."
        ),
        VoiceLine(
            200,
            Yamamoto,
            ru='(После глотка саке) Я готов помочь вам, Рокфорд и у нас, как там, "кость в горле", правильно?',
            en="I am willing to help you. Rockford is, as you say, \"a bone in the throat\" for us as well, correct?"
        ),
        VoiceLine(
            210,
            Yamamoto,
            ru='Но если вы хотите, чтобы я помог вам, окажите и нам одну услугу.',
            en="But if you want my help, you must do a service for us in return."
        ),
        VoiceLine(
            220,
            Trent,
            ru='И в чем же она заключается?',
            en="And what does that entail?"
        ),
        VoiceLine(
            230,
            Yamamoto,
            ru='(не напрягаясь) Нам нужно разместить специальные сканеры и обеспечить их долговременную работу.',
            en="We need to deploy special scanners and ensure their long-term operation."
        ),
        VoiceLine(
            240,
            Trent,
            ru='(и это всё? пффф) Уфф, интересная работа... А можно подробнее?',
            en="(surprised that the task doesn't sound too difficult) Huh, interesting work... Could you be more specific?"
        ),
        VoiceLine(
            250,
            Yamamoto,
            ru='Нас интересует система Энтерпрайз. И все защитные мероприятия, которые были проведены СБА после распада Ордена. '
               'У нас есть технические средства, чтобы получить интересующую нас информацию. ',
            en="We are interested in the Enterprise system. And all the defensive measures the ASF implemented after the Order's schism. "
               'We have the technical means to acquire the information we need.'
        ),
        VoiceLine(
            260,
            Yamamoto,
            ru='Их нужно разместить и удерживать в системе Сириус, охраняемой патрулями... '
               '(обрываем на высшей точке, фраза будет продолжена Трентом)',
            en="They must be deployed and maintained within the Sirius system, which is patrolled by..."
        ),
        VoiceLine(
            270,
            Trent,
            ru='(печальный выдох)СБА...',
            en="(with a sad sigh) The ASF..."
        ),
        VoiceLine(
            280,
            Yamamoto,
            ru='Итак, мистер Трент, вы согласны?',
            en="So, Mr. Trent, do you agree?"
        ),
        VoiceLine(
            290,
            Trent,
            ru='(А чё нет) А почему бы и нет.',
            en="Why not."
        ),
        VoiceLine(
            320,
            Yamamoto,
            ru='В таком случае, можете вылетать в космос. С вами свяжется лейтенант Ким. Он будет руководить операцией.',
            en="In that case, you may depart. Lieutenant Kim will contact you. He will be overseeing the operation."
        ),
        VoiceLine(
            350,
            Darcy,
            ru='Трент, ты в своём уме? Эта операция против СБА',
            en="Trent, are you out of your mind? This is an operation against the ASF!"
        ),
        VoiceLine(
            360,
            Trent,
            ru='(тёмные мысли, стоически) У меня уже давно ощущение, что я против всех, Д+ерси, остались только временные союзники.',
            en="(with bitterness, but stoically) I've had the feeling for a long time now that I'm against everyone, Darcy. All I have left are temporary allies."
        ),
    ]


class Msn9RewardCutscene(Msn9, script.CutsceneProps):
    ALIAS = 'reward'
    TITLE = 'Ангар линкора Мусаси'
    DESCRIPTION = 'Трент и Д+ерси подходит к Хасслеру'
    THORN_CLASS = m09_reward.Msn9RewardCutsceneThorn
    VOICE_LINES = [
        VoiceLine(
            10,
            Kim,
            ru='(грубо) Эта операция была безрассудной',
            en="(rude) This operation was reckless!"
        ),
        VoiceLine(
            20,
            HasslerOrder,
            ru='Ким, остынь',
            en="Kim, stand down."
        ),
        VoiceLine(
            30,
            Kim,
            ru='(грубо) Теперь выполни свою часть работы, чтобы наша жертва не была напрасной',
            en="(rude) Now hold up your end of the deal, so our sacrifice isn't in vain."
        ),
        VoiceLine(
            40,
            HasslerOrder,
            ru='Я гарантирую это',
            en="I guarantee it."
        ),

        VoiceLine(
            100,
            Trent,
            ru='Ей, Хасслер, тут все такие безбашенные?',
            en="Hey, Hassler, is everyone around here this crazy?"
        ),
        VoiceLine(
            110,
            HasslerOrder,
            ru='Не все, герр Трент. Но целеустремленность этих людей воодушевляет',
            en="Not everyone, Herr Trent. But their... determination is inspiring."
        ),
        VoiceLine(
            120,
            Trent,
            ru='Это точно, а что теперь делать?',
            en="That's one word for it. So, what now?"
        ),
        VoiceLine(
            130,
            HasslerOrder,
            ru='Пока нужно отдохнуть. Для вас и фрау Д+ерси на линкоре выделены индивидуальные каюты, вас проводят',
            en="For now, we rest. Individual quarters have been prepared for you and Frau Darcy on the battleship. An escort will take you there."
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
            en="Trent, we've made contact with representatives of the New Order. They've agreed to a meeting and guarantee your safety, "
               'but as a precaution, you are to attend with Darcy. The meeting point is Yokohama Station in the Omega-3 system.'
        ),

        VoiceLine(200, Kim, comment='Операция',
                  ru='Мистер Трент, я лейтенант Ким. Я буду руководить операцией. '
                     'А это Мат+омэ, он будет управлять инженерными войсками',
                  en="Mister Trent, I am Lieutenant Kim. I will be overseeing this operation. "
                     'This is Matome, he will be leading the engineering corps.'),
        VoiceLine(210, Kim,
                  ru='Нам нужно добраться в место сбора в системе Сириус. Я отметил точки пути в вашей нейросети',
                  en="We need to reach the rally point in the Sirius system. I've marked the waypoints in your neural net."),

        VoiceLine(300, Matome,
                  ru='Это больш+ая честь участвовать в операции вместе с вами мистер Трент. У вас благородная репутация. Хоть вы и работали на СБА',
                  en="It is a great honor to be part of an operation with you, Mister Trent. You have a noble reputation. Even if you did work for the ASF."),

        VoiceLine(310, Trent,
                  ru='А чем вам не нравится СБА? Вроде же ребята официалы, с пиратами не сотрудничают. В отличие от...',
                  en="What's your problem with the ASF? They're the official guys, don't work with pirates. Unlike..."),

        VoiceLine(325, Kim,
                  ru='Мы понимаем ваши намёки, мистер Трент. Орден занимается этим. Мы создаем зону всеобщего процветания в Сириусе',
                  en="We understand your insinuation, Mister Trent. The Order is involved in this. We are creating a zone of shared prosperity in Sirius."),

        VoiceLine(326, Trent, ru='Зону всепроцветания?', en="A zone of shared prosperity?"),

        VoiceLine(328, Kim,
                  ru='Именно. К примеру, после нашего прихода во внешние миры наконец добралась цивилизация',
                  en="Precisely. For instance, since our arrival, civilization has finally reached the Border Worlds."),
        VoiceLine(330, Kim,
                  ru='Мы занимаемся инфраструктурой, терраформировали Кадиз. Искоренили производство Кардамина. Теперь испанцы живут лучше',
                  en="We are building infrastructure, we terraformed planet Cadiz. We eradicated the production of Cardamine. Now the spaniards live better."),

        VoiceLine(340, Trent,
                  ru='Но это все равно не мешает корсарам продолжать совершать набеги и терроризировать Сириус',
                  en="Yet that doesn't stop corsairs from continuing their raids and terrorizing Sirius."),
        VoiceLine(350, Darcy,
                  ru='Да и проблему наркотиков в целом это не решило. А то я знаю знакомых принцесс, которые любят припудрить свой носик',
                  en="And it hasn't solved the drug problem as a whole. I know a few socialites who still like to powder their noses."),
        VoiceLine(355, Darcy, ru='Преимущественно изнутри, если вы понимаете о чём я.',
                  en="Mostly from the inside, if you catch my drift."),

        VoiceLine(360, Kim,
                  ru='Всему своё время, мисс Д+ерси. Мы не можем решить все противоречия сразу. Особенно в то время, когда СБА проводит такую политику протекционизма',
                  en="All in due time, Miss Darcy. We cannot resolve all conflicts at once. Especially while the ASF pursues such a policy of protectionism."),
        VoiceLine(370, Matome,
                  ru='СБА больше заинтересованы в защите мифического ящика Панд+оры вместо того, чтобы реально помогать людям и решать их проблемы',
                  en="The ASF is more interested in guarding a mythical Pandora's Box than in actually helping people and solving their problems."),

        VoiceLine(380, Trent, ru='Очень хочется надеяться, что вы действительно говорите правду',
                  en="I really hope you're telling the truth."),

        VoiceLine(390, Kim, ru='Не сомневайтесь мистер Трент. Тем более, что сегодня вы нам с этим поможете',
                  en="Have no doubt, Mister Trent. Especially since today, you will be helping us with it."),

        VoiceLine(450, Kim,
                  ru='Мистер Трент, мисс Д+ерси, нам нужно присоединиться к транспортному конвою. Я указал точку в вашей нейросети.',
                  en="Mister Trent, Miss Darcy, we need to join the transport convoy. I've marked the location in your neural net."),

        VoiceLine(500, Kim,
                  ru='Итак. Порядок действий такой - мы добираемся вместе с транспортом до точки размещения сканера.',
                  en="Alright. Here's the plan: we escort the transport to the scanner's deployment point."),
        VoiceLine(510, Kim,
                  ru='По периметру области обеспечения находятся буи-детекторы кораблей противника. Обеспечивают нам дистанционную пеленгацию.',
                  en="The perimeter of the operational area is covered by enemy ship detector buoys. They provide long-range tracking."),
        VoiceLine(520, Kim,
                  ru='Вокруг каждого буя небольшая команда прикрытия. Мой отряд и вы - оперативные силы.',
                  en="Each buoy has a small security detail. My squad and you are the rapid response force."),
        VoiceLine(530, Kim, ru='Выдвигаемся в сторону наибольшей угрозы и ликвидируем её. Все ясно?',
                  en="We move to the point of greatest threat and eliminate it. Is that clear?"),
        VoiceLine(540, Trent, ru='Вполне.', en="Clear enough."),
        VoiceLine(550, Darcy, ru='Да.', en="Yes."),

        VoiceLine(610, Trent, ru='И вы думаете что на этом отшибе системы нас заметят?',
                  en="And you think they'll spot us in this backwater of the system?"),
        VoiceLine(620, Kim, ru='Сейчас нет. Но они смогут запеленговать Хризантему, когда мы её запустим',
                  en="Not right now. But they will be able to get a lock on the Chrysanthemum once we activate it."),
        VoiceLine(630, Trent, ru='Значит у нас не так много времени. Долго собирать эту махину?',
                  en="So we don't have much time. How long to assemble that beast?"),

        VoiceLine(640, Matome, ru='Мои люди профессионалы своего дела. Мы сделаем свою работу быстро.',
                  en="My people are professionals. We'll get it done quickly."),
        VoiceLine(650, Matome,
                  ru='А вы должн+ы всеми силами отвлечь СБА от Хризантемы, пока она будет работать',
                  en="Your job is to draw the ASF away from the Chrysanthemum while it's operational."),

        VoiceLine(660, Trent, ru='Сделаю всё, что могу', en="I'll do what I can."),

        VoiceLine(680, Matome, ru='Мы на месте. Приступаем к сборке Хризантемы',
                  en="We're on site. Beginning Chrysanthemum assembly."),

        VoiceLine(700, SakuraOne, ru='Сакура на связи, наш сканер фиксирует приближение патруля',
                  en="Sakura here, our scanner is picking up an approaching patrol."),
        VoiceLine(710, Kim,
                  ru='А вот и они. Слишком быстро. Мистер Трент, летим на помощь Сакуре. Мисс Д+ерси, прикрывайте инженеров',
                  en="And there they are. Too fast. Mister Trent, we're moving to assist Sakura. Miss Darcy, you cover the engineers."),
        VoiceLine(720, Darcy, ru='Поняла, буду тут', en="Understood, I'll hold here."),

        VoiceLine(730, Kim, ru='Сакура, статус', en="Sakura, status."),
        VoiceLine(740, SakuraOne, ru='Летят в нашу сторону', en="They're heading right for us."),
        VoiceLine(750, Kim,
                  ru='Постараемся их пропустить. Мистер Трент, нам нужно поставить свои корабли как можно ближе к датчику, чтобы снизить нашу заметность',
                  en="Let's try to let them pass. Mister Trent, we need to position our ships as close to the sensor buoy as possible to reduce our signature."),

        VoiceLine(760, Kim, ru='Трент, ты что творишь. Нас так заметят! Ср+очно подлети к датчику!',
                  en="Trent, what are you doing? They'll spot us! Get close to the buoy, now!"),

        VoiceLine(765, Kim, ru='Не двигаться! Сто+им ждём!', en="Hold position! Don't move!"),
        VoiceLine(770, Kim, ru='Пролетели мимо. Пронесл+о', en="They flew right past us. We're clear!"),

        VoiceLine(800, Matome, ru='Хризантема собрана. Запускаем сканирование',
                  en="The Chrysanthemum is assembled. Initiating scan."),

        VoiceLine(810, SakuraOne,
                  ru='Внимание! Патруль разворачивается! Скорее всего мы обнаружены! Летит к Хризантеме!',
                  en="Attention! The patrol is turning around! We're likely detected! They're heading for the Chrysanthemum!"),
        VoiceLine(820, Kim, ru='Аах, к чёрту всё! Дайте нам их местоположение, летим на перехват',
                  en="Aah, to hell with it all! Give me their position, we're moving to intercept!"),

        VoiceLine(830, Kim, ru='Уничтожить патруль СБА!', en="Destroy the ASF patrol!"),

        VoiceLine(840, Kim, ru='Хризантема, статус', en="Chrysanthemum, status!"),
        VoiceLine(850, Chrysanthemum,
                  ru='Датчики фиксируют приближение еще одного патруля. На этот раз они вызвали тяжелую технику',
                  en="Sensors detect another patrol approaching. This time, they've called in heavy assets!"),
        VoiceLine(860, Kim, ru='Летим на перехват', en="Moving to intercept!"),

        VoiceLine(870, Trent, ru='А этот отряд уже более серьёзный.',
                  en="This squadron is a lot more serious."),
        VoiceLine(880, Kim, ru='Всё верно, они явно готовят группу зачистки.',
                  en="Correct. They're clearly assembling a strike group."),

        VoiceLine(890, Kim, ru='Атакуйте уязвимые точки Канонерок! Они не должн+ы добраться до Хризантемы!',
                  en="Attack the Gunboats' weak spots! They must not reach the Chrysanthemum!"),

        VoiceLine(900, Kim, ru='Канонерки уничтожены', en="Gunboats destroyed!"),

        VoiceLine(910, Chrysanthemum, ru='Внимание! Приближаются значительные силы противника! Эсминцы!',
                  en="Warning! Significant enemy forces approaching! Destroyers!"),
        VoiceLine(920, Kim,
                  ru="А вот и вражеская кавалерия. Хризантема, дайте нам ближайшие координаты. Постараемся атаковать врага на подлёте",
                  en="And here comes their cavalry. Chrysanthemum, give us the nearest coordinates. We'll try to hit them on approach."),

        VoiceLine(950, Kim,
                  ru='Атакуйте эсминцы! Нужно повредить их до того как они в+ыйдут на огневую позицию!',
                  en="Attack the destroyers! We need to damage them before they reach firing positions!"),
        VoiceLine(960, Kim, ru='Атакуйте двигатели, пилоны, всё что угодно!',
                  en="Target their engines, weapon pylons, anything!"),

        VoiceLine(980, Kim, ru='Эсминцы стали выход+ить на боевой рубеж',
                  en="The destroyers are moving into attack formation."),
        VoiceLine(985, Kim, ru='Трент, нужно уничтожить торпеды. Мы должн+ы защитить Хризантему любой ценой',
                  en="Trent, we need to destroy the torpedoes! We must protect the Chrysanthemum at all costs!"),

        VoiceLine(1000, Chrysanthemum, ru='Приближается новая группа эсминцев',
                  en="A new group of destroyers is approaching!"),
        VoiceLine(1010, Chrysanthemum, ru='Замечено новое вражеское подкрепление',
                  en="New enemy reinforcements detected!"),
        VoiceLine(1020, Chrysanthemum, ru='Новая группа эсминцев готовится к залпу',
                  en="A new group of destroyers is preparing to fire!"),
        VoiceLine(1030, Chrysanthemum, ru='Еще группа эсминцев на изгот+овке',
                  en="Another group of destroyers is lining up for a salvo!"),
        VoiceLine(1035, Chrysanthemum, ru='Прилетело еще одно звено вражеских эсминцев',
                  en="Another wing of enemy destroyers has arrived!"),

        VoiceLine(1050, Chrysanthemum, ru='Мы получили удар торпедой! Прикрытие, сделайте что-нибудь!',
                  en="We've been hit by a torpedo! Cover, do something!"),
        VoiceLine(1060, Chrysanthemum, ru='Хризантема получила повреждения!',
                  en="The Chrysanthemum has sustained damage!"),
        VoiceLine(1070, Chrysanthemum, ru='Хризантема получила серьезные повреждения! Требуется помощь!',
                  en="The Chrysanthemum has sustained critical damage! Assistance required!"),

        VoiceLine(1080, Kim, ru='Нет... мы потеряли Хризантему до завершения сканирования. Это провал',
                  en="No... we've lost the Chrysanthemum before the scan completed. This is a failure!"),

        VoiceLine(1100, Kim, ru='Мат+омэ, как идет сканирование', en="Matome, what's the scan status?"),
        VoiceLine(1110, Matome, ru='Готово на 50 процентов. Нам нужно еще время',
                  en="50 percent complete. We need more time."),

        VoiceLine(1120, Matome, ru='Сканирование проведено на 70 процентов', en="Scan is 70 percent complete."),
        VoiceLine(1140, Matome, ru='Сканирование проведено на 90 процентов. Еще немного!',
                  en="Scan is 90 percent complete. Almost there!"),
        VoiceLine(1170, Matome, ru='Сканирование завершено!', en="Scan complete!"),

        VoiceLine(1200, Kim, ru='Хризантема включайте самоуничтожение и эвакуируйтесь.',
                  en="Chrysanthemum, activate self-destruct and evacuate."),
        VoiceLine(1210, Kim, ru='Трент, подбери капсулу с хризантемы',
                  en="Trent, retrieve the pod from the Chrysanthemum!"),

        VoiceLine(1250, Kim, ru='Уходим!', en="We're leaving!"),

        VoiceLine(1300, SakuraOne, ru='Прибыли вражеские линкоры! Пути отступления перекрыты! Мы окружены!',
                  en="Enemy battleships have arrived! Our retreat is cut off! We're surrounded!"),

        VoiceLine(1310, Matome,
                  ru='Ким, нам нужно сделать отвлекающий ман+ёвр. Эти данные слишком важны для Ордена',
                  en="Kim, we need to create a diversion. This data is too important for the Order!"),
        VoiceLine(1320, Kim, ru='И что ты предлагаешь', en="So what are you proposing?"),

        VoiceLine(1330, Matome,
                  ru='Мы совершим атаку камикадзе и отвлечем вражеские силы. А вы уход+ите и доставьте данные на Мус+аси сами',
                  en="We'll launch a kamikaze attack and distract the enemy forces. You escape and deliver the data to the Musashi yourself!"),
        VoiceLine(1340, Kim, ru='Мат+омэ, идиот, остановись!', en="Matome, you idiot, stop!",
                  cinematic=True),

        VoiceLine(1350, Matome, ru='Это наш единственный шанс! Прощай друг!',
                  en="It's our only chance! Farewell, my friend!",
                  cinematic=True),
        VoiceLine(1355, Matome, ru='Банзай!', en="Banzai!",
                  cinematic=True),

        VoiceLine(1360, Kim, ru='Стой! Нет!', en="Stop! No!",
                  cinematic=True),

        VoiceLine(1400, Darcy, ru='Кажется нам пор+а уходить', en="I think it's time for us to go..."),
        VoiceLine(1410, Kim, ru='Всё верно мисс Д+ерси. Летим к указанной точке пути',
                  en="You're right, Miss Darcy. Heading for the designated waypoint."),

        VoiceLine(1420, HasslerOrder, ru='Мус+аси на связи. Ким, наш статус',
                  en="Musashi here. Kim, what's your status?"),
        VoiceLine(1430, Kim, ru='Данные успешно получены. Но прикрытие потеряно полностью',
                  en="Data successfully retrieved. But we've lost all covering forces."),

        VoiceLine(1500, HasslerOrder,
                  ru='Они погибли во славу Ордена. Садитесь на Мус+аси. Нужно убираться отсюда',
                  en="They died for the glory of the Order. Dock with the Musashi. We need to get out of here!"),
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

    MISSION_TITLE = 'Миссия 9. Услуга Новому Ордену'
