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
            en="Trent, ready for action?"
        ),
        VoiceLine(
            20,
            Trent,
            ru='К чему это?',
            en="Yeah. Sure. Uhh... what action was that again, exactly?"
        ),
        VoiceLine(
            30,
            Darcy,
            ru='К встрече с информатором! Мы понятия не имеем,, сколько тут агентов Нового Ордена!',
            en="We're meeting informants from the Order! We have no idea how many of them there'll be, much less their disposition!"
        ),
        VoiceLine(
            40,
            Trent,
            ru='Так ты же у нас прикрытие! Или Бретонская корона уже не так+ая всесильная на территории Кус+ари?',
            en="Aren't YOU all the protection I need? Or is Bretonia's influence in Kusari territory dwindling?"
        ),
        VoiceLine(
            50,
            Darcy,
            ru='Эй, всё с нашей короной в порядке! Только от выстрелов лазерных пушек она не защищает! Так что будь покладистей!',
            en="Bretonia's influence is doing just fine. But even the strongest political influence can't stop a laser bolt to the head. So play nice."
        ),
        VoiceLine(
            60,
            Trent,
            ru='Как прикажете, мисс Д+ерси!',
            en="As you wish, Buttercup."
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
            en="I'll be honest, it's kind of unsettling how everyone in the bar, including the bartender, is staring at me."
        ),
        VoiceLine(
            20,
            Darcy,
            ru='Тоже заметил, да?',
            en="I was going to make a quip about you and main character syndrome, but in this instance I'm inclined to agree with you. They're not sparing me a second glance, which is peculiar."
        ),
        VoiceLine(
            30,
            Trent,
            ru='Трудно на заметить. Они же не просто смотрят, они взглядом прожигают. Короче, если этот парламентер через полчаса не приходит - я сваливаю.',
            en="Yeah. Creepy. If this guy doesn't show in the next thirty minutes, I'm outta here."
        ),
        VoiceLine(
            40,
            Darcy,
            ru='Полностью согласна.',
            en="I'm with you."
        ),
        VoiceLine(
            50,
            HasslerOrder,
            ru='Герр Трент, вы действительно верите, что бессмертны?',
            en="Herr Trent, we meet again."
        ),
        VoiceLine(
            60,
            Trent,
            ru='Герр Хасслер? Рад видеть. Сегодня в штатском?',
            en="Herr Hassler? You're the contact? Looking sharp! Out of uniform today?"
        ),
        VoiceLine(
            70,
            HasslerOrder,
            ru='С моей службой в Р+ейнланде покончено герр Трент. Вам повезло лично увидеть закат моей военной карьеры.',
            en="My service for Rheinland is permanently terminated, Herr Trent. You have witnessed the sunset of a decorated military career. Kaputt. Now I have found a new home with the Order."
        ),
        VoiceLine(
            80,
            HasslerOrder,
            ru='Но хватит про меня, в наших краях вы суперзвезда, за вашу голову назначена очень хорошая награда...',
            en="But enough about me. Around here, you are a superstar. As you are aware, there is a substantial bounty on your head..."
        ),
        VoiceLine(
            90,
            Trent,
            ru='О как... И чем обязан?',
            en="There is? ... Why?"
        ),
        VoiceLine(
            100,
            HasslerOrder,
            ru='(с усмешкой) А вы даже и не в курсе. Ха-ха. '
               'Многие думают что специально, а я считаю - по незнанию, вы такое количество раз перешли дорогу Новому Ордену, '
               'что у руководства не то что нервные тики - судороги начались. ',
            en="(Chuckles) And he doesn't even know. Ha-ha. "
               "People are saying that you are one cool cucumber to show up here... if they only knew it was just, how do you say it... ignorance is bliss. Herr Trent, let's just say that you have crossed the Order so many times..."
               "our leadership don't just have nervous tics when your name comes up — they have full-blown seizures. And when they recover, they have another seizure..."
        ),
        VoiceLine(
            110,
            HasslerOrder,
            ru='И что характ+ерно - каждый раз вы вых+одите сух+им из вод+ы. '
               'Я бы даже сказал не просто сухим из вод+ы, а («снимает шляпу перед дамой») '
               'унося на руках красивую девушку на фоне ядерного гриба.',
            en="You seem to attract calamity, yet each time you somehow emerge from the brink of disaster not only unscathed,"
               "but with a beautiful girl on your arm, set against the backdrop of a big, black mushroom cloud."
        ),
        VoiceLine(
            120,
            Trent,
            ru='Именно поэтому на меня все здесь так пялятся?', en="Oh so that's why everyone's gawking at me."
        ),
        VoiceLine(
            130,
            HasslerOrder,
            ru='Конечно. После всех этих подвигов так просто заявиться в штаб-квартиру Нового Ордена. '
               'Впрочем, в данный момент вы в полной безопасности, как вам и было обещано.',
            en="You are a legend. To just waltz into an Order base after all this just to meet me... you are either very brave, or very stupid."
               'Nonetheless, for now you are perfectly safe, as promised.'
        ),
        VoiceLine(
            140,
            Trent,
            ru='Хасслер, в данный момент мне нужны ответы на пару вопросов.'
               'Первый и главный из них - где находится Аларик и что с ним?',
            en="Hassler, right now I just need answers. "
               'I really need to know, where is Alaric? Is he alive and well?'
        ),
        VoiceLine(
            150,
            HasslerOrder,
            ru='Тогда вам лучше говорить не со мной герр Трент, а с главой Нового Ордена, герром Ямамото.',
            en="For this, Herr Trent, you will have to speak to the head of the New Order, Herr Yamamoto."
        ),
        VoiceLine(
            160,
            Trent,
            ru='И вы сможете это устроить?', en="Can you set it up?"
        ),
        VoiceLine(
            170,
            HasslerOrder,
            ru='Именно! Причем незамедлительно!', en="Already on it!"
        ),
        VoiceLine(
            180,
            Darcy,
            ru='Разумно ли это, Трент?', en="Let's not be too hasty..."
        ),
        VoiceLine(
            190,
            HasslerOrder,
            ru='Вы и так находитесь в штаб-квартире Нового Ордена, бояться нужно было раньше. '
               'Ямамото-с+ама (-сама - это уважительный суффикс при обращении к мужчине в японии. как у нас господин или в германии герр) '
               'придерживается консервативных взглядов и очень уважает воинскую доблесть. ',
            en="You're already in New Order HQ. It's a little late to be getting cold feet. "
               'Heads up. Yamamoto-san holds deeply conservative views and has a profound respect for martial prowess. Or rather, he only respects martial prowess.'
        ),
        VoiceLine(
            200,
            HasslerOrder,
            ru='Я рассказал ему о наших с вами совместных приключениях, и '
               ' как мне показалось он проникся уважением к вам. Не думаю что вам что-то угрожает.',
            en="I told him about our previous adventures... or misadventures, "
               'and he seems to have developed a peculiar respect for you. Or perhaps a morbid curiosity. Or both. I don\'t believe you\'re in any danger. Not mortal danger at least.'
        ),
        VoiceLine(
            210,
            Trent,
            ru='Хорошо, пойдёт!', en="Into the Dragon's maw!"
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
            en="Herr Yamamoto please meet Herr Trent and Fraulein Darcy."
        ),
        VoiceLine(
            20,
            Yamamoto,
            ru='(задумчиво-меланхолично, без пафсоа) Мистер Трент, я думал, что в свои годы уже утратил способность удивляться, '
               'но вы меня просто поразили. По вашей истории можно написать приключенческий роман. А может и не один роман.',
            en="Mr. Trent, I thought that at my age I had lost all capacity for surprise, but you, you surprise me. "
               'One could write an epic tale about your adventures. Or two!'
        ),
        VoiceLine(
            30,
            Yamamoto,
            ru='Вчера вы никто, потом работаете на спецслужбу одного государства, потом становитесь врагом этого государства, '
               'но не теряете времени и начинаете работать на спецслужбу другого государства, '
               'с которой у вас потом тоже начинаются серьёзные неприятности.',
            en="One day you are a nobody, the next day you work for the intelligence service of one state, then you become an enemy of that state, "
               'and then suddenly you are working for the intelligence service of another, '
               'and then you are most wanted by THAT state! Ha ha. It is very entertaining.'
        ),
        VoiceLine(
            40,
            Yamamoto,
            ru='Мимоходом отправляете в мусорную корзину долгосрочные планы надправительственной организации. '
               '(переход на доброжелательный тон) А теперь вот стоите здесь и мирно попиваете саке с её руководителем. ',
            en="And then you casually cast the long-term plans of a supra-governmental secret organization into the trash. "
               '(Yamamoto shifts to a benevolent tone) And here you stand, looking surprisingly alive and well, before its leader.'
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
            en="Thank you, Yamamoto-san."
        ),
        VoiceLine(
            70,
            Trent,
            ru='(выпивши) Спасибо, мистер Ямамото, у меня к вам дело.',
            en="Thank you, Mr. Yamamoto. I need a favour from you."
        ),
        VoiceLine(
            80,
            Yamamoto,
            ru='(мудрец) Иначе вас бы здесь не было.',
            en="Of course, why would you be here otherwise."
        ),
        VoiceLine(
            90,
            Trent,
            ru='Я должен найти Аттикуса Рокфорда.',
            en="I need to locate an Atticus Rockford."
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
            en="(with a sarcastic hint) General King too, it would seem."
        ),
        VoiceLine(
            130,
            Yamamoto,
            ru='(Серьезный тон) Не надо темнить, мистер Трент. Я не бармен, которому изливают душу.',
            en="(turning serious) Do not be coy, Mr. Trent. I am not some bartender with loose lips."
        ),
        VoiceLine(
            140,
            Yamamoto,
            ru='(Саркастичский намёк) Кроме того, у меня появилось ощущение, что и к вам Кинг теплых чувств не испытывает.',
            en="(sarcastic again) Besides, I have a feeling King may not feel too kindly about you either..."

        ),
        VoiceLine(
            150,
            Yamamoto,
            ru='(Сюжетный поворот)...Если послал на самоубийство...',
            en="(revealing a plot twist) considering he sent you on a suicide mission..."
        ),
        VoiceLine(
            160,
            Trent,
            ru='(удивлённо) Самоубийство?!',
            en="Suicide mission?!"
        ),
        VoiceLine(
            170,
            Yamamoto,
            ru='Для того, чтобы ликвидировать Рокфорда не достаточно одного человека, даже такого везучего как вы, мистер Трент.',
            en="One man is not enough to eliminate a man such as Rockford. Not even a man as ridiculously lucky as you, Mr. Trent."
        ),
        VoiceLine(
            180,
            Trent,
            ru='(Уверенный и непоколебимый) Плевать на Кинга, мистер Ямамото, или, как вас правильно, Ямамото-сама? '
               'Я должен прикончить этого ублюдка и вернуть себе то, что он у меня украл.',
            en="(confident and unwavering) I don't give a damn about King's feelings right now, Mr. Yamamoto, or should I say, Yamamoto-san? "
               'I\'m going track down that murderous bastard Rockford, reclaim what he stole from me and pay him back in kind.'
        ),
        VoiceLine(
            190,
            Yamamoto,
            ru='(просит бармена подлить саке, рассуждает) Я вам немного завидую, мистер Трент. Вы молодой, в вас есть страсть...',
            en="Ah, to be young and passionate again... or foolish..."
        ),
        VoiceLine(
            200,
            Yamamoto,
            ru='(После глотка саке) Я готов помочь вам, Рокфорд и у нас, как там, "кость в горле", правильно?',
            en="I will help you, Mr Trent. Rockford is, as you say, \"a bone in the throat\" for us as well, correct?"
        ),
        VoiceLine(
            210,
            Yamamoto,
            ru='Но если вы хотите, чтобы я помог вам, окажите и нам одну услугу.',
            en="But if you want my help, you must return the favour."
        ),
        VoiceLine(
            220,
            Trent,
            ru='И в чем же она заключается?',
            en="I'm not sure we say bone in the throat... sounds kinda dirty. How exactly will I be repaying the favour?"
        ),
        VoiceLine(
            230,
            Yamamoto,
            ru='(не напрягаясь) Нам нужно разместить специальные сканеры и обеспечить их долговременную работу.',
            en="We just need you to deploy an experimental scanner in space. We call it the Chrysanthemum."
        ),
        VoiceLine(
            240,
            Trent,
            ru='(и это всё? пффф) Уфф, интересная работа... А можно подробнее?',
            en="(surprised that the task doesn't sound too difficult) Huh, doesn't sound too difficult... What's the catch?"
        ),
        VoiceLine(
            250,
            Yamamoto,
            ru='Нас интересует система Энтерпрайз. И все защитные мероприятия, которые были проведены СБА после распада Ордена. '
               'У нас есть технические средства, чтобы получить интересующую нас информацию. ',
            en="We have interests in the Enterprise system. And knowledge of all defensive measures the ASF has implemented since the schism of the Order. "
               'We have the technical means to acquire all the information we need with this scanner.'
        ),
        VoiceLine(
            260,
            Yamamoto,
            ru='Их нужно разместить и удерживать в системе Сириус, охраняемой патрулями... '
               '(обрываем на высшей точке, фраза будет продолжена Трентом)',
            en="We just need to deploy it within the Sirius system, which is patrolled by..."
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
            en="Yeah, why not. Just another day in my life."
        ),
        VoiceLine(
            320,
            Yamamoto,
            ru='В таком случае, можете вылетать в космос. С вами свяжется лейтенант Ким. Он будет руководить операцией.',
            en="In that case, you may depart now. Lieutenant Kim will contact you. He will oversee the operation."
        ),
        VoiceLine(
            350,
            Darcy,
            ru='Трент, ты в своём уме? Эта операция против СБА',
            en="Trent, are crazy? This operation is against the bloody ASF!"
        ),
        VoiceLine(
            360,
            Trent,
            ru='(тёмные мысли, стоически) У меня уже давно ощущение, что я против всех, Д+ерси, остались только временные союзники.',
            en="(with bitterness, but stoically) Well, Darcy, it's starting to feel like the big Scriptwriter in the Sky is yanking my chain... friend one day, foe the next."
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
            en="(rude) The operation was a complete fiasco!"
        ),
        VoiceLine(
            20,
            HasslerOrder,
            ru='Ким, остынь',
            en="Kim, stand down please."
        ),
        VoiceLine(
            30,
            Kim,
            ru='(грубо) Теперь выполни свою часть работы, чтобы наша жертва не была напрасной',
            en="(rude) You better hold up your end of the deal, or the sacrifices of my men would have been in vain."
        ),
        VoiceLine(
            40,
            HasslerOrder,
            ru='Я гарантирую это',
            en="We will. I promise"
        ),

        VoiceLine(
            100,
            Trent,
            ru='Ей, Хасслер, тут все такие безбашенные?',
            en="Hey, Hassler, is everyone around here loony-tunes or what?"
        ),
        VoiceLine(
            110,
            HasslerOrder,
            ru='Не все, герр Трент. Но целеустремленность этих людей воодушевляет',
            en="Not everyone, Herr Trent. But their determination is ...inspiring."
        ),
        VoiceLine(
            120,
            Trent,
            ru='Это точно, а что теперь делать?',
            en="There's another word for it. Anway, what now?"
        ),
        VoiceLine(
            130,
            HasslerOrder,
            ru='Пока нужно отдохнуть. Для вас и фрау Д+ерси на линкоре выделены индивидуальные каюты, вас проводят',
            en="For now, you rest. We have prepared quarters for you and Fraulein Darcy on our battleship. An escort will lead you there."
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
            en="Trent, we've made contact with representatives of the New Order. They've agreed to a meeting and to guarantee your safety, "
               'but as a precaution, you will take Darcy. The meeting point is Yokohama Station in the Omega-3 system.'
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
                  en="It is an honor to join you on this operation, Mister Trent. You have a noble reputation. Even despite you working for the ASF."),

        VoiceLine(310, Trent,
                  ru='А чем вам не нравится СБА? Вроде же ребята официалы, с пиратами не сотрудничают. В отличие от...',
                  en="What's your beef with the ASF? They're the good guys, and they don't work with pirates. Unlike..."),

        VoiceLine(325, Kim,
                  ru='Мы понимаем ваши намёки, мистер Трент. Орден занимается этим. Мы создаем зону всеобщего процветания в Сириусе',
                  en="Be careful what you insinuate, Mister Trent. We in the Order are creating a zone of shared prosperity in Sirius, agnostic to past or present affiliations."),

        VoiceLine(326, Trent, ru='Зону всепроцветания?', en="A zone of shared prosperity?"),

        VoiceLine(328, Kim,
                  ru='Именно. К примеру, после нашего прихода во внешние миры наконец добралась цивилизация',
                  en="Precisely. Civilization finally reached the Border Worlds after the Order arrived."),
        VoiceLine(330, Kim,
                  ru='Мы занимаемся инфраструктурой, терраформировали Кадиз. Искоренили производство Кардамина. Теперь испанцы живут лучше',
                  en="We terraformed planet Malta, eradicated Cardamine production and implemented universal healthcare. Now the citizens of Hispania lead prosperous lives. We are building up infrastructure, creating jobs and enriching lives."),

        VoiceLine(340, Trent,
                  ru='Но это все равно не мешает корсарам продолжать совершать набеги и терроризировать Сириус',
                  en="Yet that doesn't stop the Corsairs from raiding and terrorizing the rest of Sirius."),
        VoiceLine(350, Darcy,
                  ru='Да и проблему наркотиков в целом это не решило. А то я знаю знакомых принцесс, которые любят припудрить свой носик',
                  en="And it hasn't stopped Cardamine oozing out to the rest of Sirius. I know a socialite or two who still \"powders\" her nose."),
        VoiceLine(355, Darcy, ru='Преимущественно изнутри, если вы понимаете о чём я.',
                  en="On the inside, if you know what I mean."),

        VoiceLine(360, Kim,
                  ru='Всему своё время, мисс Д+ерси. Мы не можем решить все противоречия сразу. Особенно в то время, когда СБА проводит такую политику протекционизма',
                  en="Change takes time, Miss Darcy. Baby steps. The ASF pursuing their nationalistic agenda is not helping."),
        VoiceLine(370, Matome,
                  ru='СБА больше заинтересованы в защите мифического ящика Панд+оры вместо того, чтобы реально помогать людям и решать их проблемы',
                  en="The ASF is more interested in safeguarding their mystical Pandora's Box from imaginery threats than helping citizens solve their mundane problems."),

        VoiceLine(380, Trent, ru='Очень хочется надеяться, что вы действительно говорите правду',
                  en="I really hope you're telling the truth."),

        VoiceLine(390, Kim, ru='Не сомневайтесь мистер Трент. Тем более, что сегодня вы нам с этим поможете',
                  en="I assure you we are, Mister Trent. And today, you will helping real people."),

        VoiceLine(450, Kim,
                  ru='Мистер Трент, мисс Д+ерси, нам нужно присоединиться к транспортному конвою. Я указал точку в вашей нейросети.',
                  en="Mister Trent, Miss Darcy, we need to join the transport convoy. I've marked the location in your neural net."),

        VoiceLine(500, Kim,
                  ru='Итак. Порядок действий такой - мы добираемся вместе с транспортом до точки размещения сканера.',
                  en="Alright. Here is the plan: we will first escort the transport to the deployment point."),
        VoiceLine(510, Kim,
                  ru='По периметру области обеспечения находятся буи-детекторы кораблей противника. Обеспечивают нам дистанционную пеленгацию.',
                  en="The perimeter of the operational area is covered by the enemy's ship detector buoys. They provide long-range detection and tracking."),
        VoiceLine(520, Kim,
                  ru='Вокруг каждого буя небольшая команда прикрытия. Мой отряд и вы - оперативные силы.',
                  en="Each buoy has a small security detail."),
        VoiceLine(530, Kim, ru='Выдвигаемся в сторону наибольшей угрозы и ликвидируем её. Все ясно?',
                  en="Our combined strike force will move to the point of greatest threat and eliminate it. Is that clear?"),
        VoiceLine(540, Trent, ru='Вполне.', en="Roger."),
        VoiceLine(550, Darcy, ru='Да.', en="Yes."),

        VoiceLine(610, Trent, ru='И вы думаете что на этом отшибе системы нас заметят?',
                  en="Any chance they'll spot us?"),
        VoiceLine(620, Kim, ru='Сейчас нет. Но они смогут запеленговать Хризантему, когда мы её запустим',
                  en="Unlikely. But once the Chrysanthemum activates, they'll home in on it like bees to honey."),
        VoiceLine(630, Trent, ru='Значит у нас не так много времени. Долго собирать эту махину?',
                  en="So we won't have much time. How long will it take to assemble that monstrosity?"),

        VoiceLine(640, Matome, ru='Мои люди профессионалы своего дела. Мы сделаем свою работу быстро.',
                  en="My people are professionals. They will be done before you know it."),
        VoiceLine(650, Matome,
                  ru='А вы должн+ы всеми силами отвлечь СБА от Хризантемы, пока она будет работать',
                  en="Your job is to draw the ASF away from the Chrysanthemum while it is acquiring the data. This will take some time."),

        VoiceLine(660, Trent, ru='Сделаю всё, что могу', en="Roger."),

        VoiceLine(680, Matome, ru='Мы на месте. Приступаем к сборке Хризантемы',
                  en="We're on site. Beginning assembly of the Chrysanthemum now."),

        VoiceLine(700, SakuraOne, ru='Сакура на связи, наш сканер фиксирует приближение патруля',
                  en="Sakura here, our scanners are detecting an approaching patrol."),
        VoiceLine(710, Kim,
                  ru='А вот и они. Слишком быстро. Мистер Трент, летим на помощь Сакуре. Мисс Д+ерси, прикрывайте инженеров',
                  en="What? Already? Too fast. Mister Trent, we're moving to assist Sakura. Miss Darcy, you cover the engineers."),
        VoiceLine(720, Darcy, ru='Поняла, буду тут', en="Understood, I'll hold here."),

        VoiceLine(730, Kim, ru='Сакура, статус', en="Sakura, status."),
        VoiceLine(740, SakuraOne, ru='Летят в нашу сторону', en="They're heading right for us."),
        VoiceLine(750, Kim,
                  ru='Постараемся их пропустить. Мистер Трент, нам нужно поставить свои корабли как можно ближе к датчику, чтобы снизить нашу заметность',
                  en="Let them pass. Mister Trent, we need to position our ships as close to the sensor buoy as possible to reduce our radar signature."),

        VoiceLine(760, Kim, ru='Трент, ты что творишь. Нас так заметят! Ср+очно подлети к датчику!',
                  en="Trent, what are you doing? They'll spot us! Close up with the buoy, now!"),

        VoiceLine(765, Kim, ru='Не двигаться! Сто+им ждём!', en="Hold position! Don't move!"),
        VoiceLine(770, Kim, ru='Пролетели мимо. Пронесл+о', en="They flew right past us. We're in the clear!"),

        VoiceLine(800, Matome, ru='Хризантема собрана. Запускаем сканирование',
                  en="The Chrysanthemum is assembled. Initiating scan."),

        VoiceLine(810, SakuraOne,
                  ru='Внимание! Патруль разворачивается! Скорее всего мы обнаружены! Летит к Хризантеме!',
                  en="Attention! The patrol is coming back around! We've been spotted! They're heading for the Chrysanthemum!"),
        VoiceLine(820, Kim, ru='Аах, к чёрту всё! Дайте нам их местоположение, летим на перехват',
                  en="Aah, to hell with it! Move to intercept!"),

        VoiceLine(830, Kim, ru='Уничтожить патруль СБА!', en="Take out the ASF patrol!"),

        VoiceLine(840, Kim, ru='Хризантема, статус', en="Chrysanthemum, status!"),
        VoiceLine(850, Chrysanthemum,
                  ru='Датчики фиксируют приближение еще одного патруля. На этот раз они вызвали тяжелую технику',
                  en="Sensors are picking up another incoming patrol. This time they've got heavyweights!"),
        VoiceLine(860, Kim, ru='Летим на перехват', en="Moving to intercept!"),

        VoiceLine(870, Trent, ru='А этот отряд уже более серьёзный.',
                  en="Oh you've got to be kidding me."),
        VoiceLine(880, Kim, ru='Всё верно, они явно готовят группу зачистки.',
                  en="Gunboats! This is gonna be rough."),

        VoiceLine(890, Kim, ru='Атакуйте уязвимые точки Канонерок! Они не должн+ы добраться до Хризантемы!',
                  en="Hit the Gunboats with everything you've got! They must not reach the Chrysanthemum!"),

        VoiceLine(900, Kim, ru='Канонерки уничтожены', en="Gunboats destroyed!"),

        VoiceLine(910, Chrysanthemum, ru='Внимание! Приближаются значительные силы противника! Эсминцы!',
                  en="Warning! Yet more forces incoming! Oh my God! Destroyers!"),
        VoiceLine(920, Kim,
                  ru="А вот и вражеская кавалерия. Хризантема, дайте нам ближайшие координаты. Постараемся атаковать врага на подлёте",
                  en="My God, capital ships! Chrysanthemum, give us the coordinates. We'll try to hit them on approach."),

        VoiceLine(950, Kim,
                  ru='Атакуйте эсминцы! Нужно повредить их до того как они в+ыйдут на огневую позицию!',
                  en="Attack the destroyers! We need to hit them before they reach firing position!"),
        VoiceLine(960, Kim, ru='Атакуйте двигатели, пилоны, всё что угодно!',
                  en="Target their engines, weapon pylons, anything! Just stop them! It doesn't matter how!!"),

        VoiceLine(980, Kim, ru='Эсминцы стали выход+ить на боевой рубеж',
                  en="The destroyers are moving into attack formation."),
        VoiceLine(985, Kim, ru='Трент, нужно уничтожить торпеды. Мы должн+ы защитить Хризантему любой ценой',
                  en="Trent, we need to destroy the torpedoes! Protect the Chrysanthemum at all costs!"),

        VoiceLine(1000, Chrysanthemum, ru='Приближается новая группа эсминцев',
                  en="A new group of destroyers is approaching!"),
        VoiceLine(1010, Chrysanthemum, ru='Замечено новое вражеское подкрепление',
                  en="New enemy reinforcements detected!"),
        VoiceLine(1020, Chrysanthemum, ru='Новая группа эсминцев готовится к залпу',
                  en="Another group of destroyers is preparing to fire!"),
        VoiceLine(1030, Chrysanthemum, ru='Еще группа эсминцев на изгот+овке',
                  en="Another group of destroyers is lining up for a salvo!"),
        VoiceLine(1035, Chrysanthemum, ru='Прилетело еще одно звено вражеских эсминцев',
                  en="Another wing of enemy destroyers has arrived!"),

        VoiceLine(1050, Chrysanthemum, ru='Мы получили удар торпедой! Прикрытие, сделайте что-нибудь!',
                  en="We've been hit by a torpedo! Strike team, please try harder!"),
        VoiceLine(1060, Chrysanthemum, ru='Хризантема получила повреждения!',
                  en="The Chrysanthemum is taking damage!"),
        VoiceLine(1070, Chrysanthemum, ru='Хризантема получила серьезные повреждения! Требуется помощь!',
                  en="We have sustained critical damage! Urgent assistance required!"),

        VoiceLine(1080, Kim, ru='Нет... мы потеряли Хризантему до завершения сканирования. Это провал',
                  en="No... we lost the Chrysanthemum before the scan could complete. We failed!"),

        VoiceLine(1100, Kim, ru='Мат+омэ, как идет сканирование', en="Matome, what's the scan status?"),
        VoiceLine(1110, Matome, ru='Готово на 50 процентов. Нам нужно еще время',
                  en="Scan at 50 percent. We need more time."),

        VoiceLine(1120, Matome, ru='Сканирование проведено на 70 процентов', en="Scan is 70 percent complete."),
        VoiceLine(1140, Matome, ru='Сканирование проведено на 90 процентов. Еще немного!',
                  en="Scan is 90 percent completed. Almost there!"),
        VoiceLine(1170, Matome, ru='Сканирование завершено!', en="Scan complete!"),

        VoiceLine(1200, Kim, ru='Хризантема включайте самоуничтожение и эвакуируйтесь.',
                  en="Chrysanthemum, activate self-destruct and bail out!"),
        VoiceLine(1210, Kim, ru='Трент, подбери капсулу с хризантемы',
                  en="Trent, retrieve their escape pod from the Chrysanthemum!"),

        VoiceLine(1250, Kim, ru='Уходим!', en="We're bailing!"),

        VoiceLine(1300, SakuraOne, ru='Прибыли вражеские линкоры! Пути отступления перекрыты! Мы окружены!',
                  en="Enemy battleships have arrived! Our retreat is cut off! We're surrounded!"),

        VoiceLine(1310, Matome,
                  ru='Ким, нам нужно сделать отвлекающий ман+ёвр. Эти данные слишком важны для Ордена',
                  en="Kim, we need to create a diversion. We have to get this data out of here!"),
        VoiceLine(1320, Kim, ru='И что ты предлагаешь', en="What do you propose?"),

        VoiceLine(1330, Matome,
                  ru='Мы совершим атаку камикадзе и отвлечем вражеские силы. А вы уход+ите и доставьте данные на Мус+аси сами',
                  en="We will launch a kamikaze attack on the battleships. The ensuing chaos should give you a window to escape. Deliver the data to the Musashi. Tell them that I died with honor."),
        VoiceLine(1340, Kim, ru='Мат+омэ, идиот, остановись!', en="Matome.. we will honour your memory. Thank you.",
                  cinematic=True),

        VoiceLine(1350, Matome, ru='Это наш единственный шанс! Прощай друг!',
                  en="Go now! May we meet again, in another life, my friend.",
                  cinematic=True),
        VoiceLine(1355, Matome, ru='Банзай!', en="Banzai!",
                  cinematic=True),

        VoiceLine(1360, Kim, ru='Стой! Нет!', en="Godspeed, dear friend. May the heavens smile on you.",
                  cinematic=True),

        VoiceLine(1400, Darcy, ru='Кажется нам пор+а уходить', en="I think it's about time we left..."),
        VoiceLine(1410, Kim, ru='Всё верно мисс Д+ерси. Летим к указанной точке пути',
                  en="Yes, Miss Darcy. Heading for designated waypoint."),

        VoiceLine(1420, HasslerOrder, ru='Мус+аси на связи. Ким, наш статус',
                  en="Musashi here. Kim, what's your status?"),
        VoiceLine(1430, Kim, ru='Данные успешно получены. Но прикрытие потеряно полностью',
                  en="The Data has been successfully acquired. But all our men... are lost."),

        VoiceLine(1500, HasslerOrder,
                  ru='Они погибли во славу Ордена. Садитесь на Мус+аси. Нужно убираться отсюда',
                  en="They died with honour, for the good of all. Their deaths shall not be forgotten. Dock with the Musashi. We need to leave, now."),
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