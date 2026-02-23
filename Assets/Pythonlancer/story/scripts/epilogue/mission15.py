from story import script
from audio.sound import VoiceLine
from story.actors import Trent, Kenji, Otomo, Shinja, HasslerEpilogue, Juni
from story.cutscenes.epilogue_scenes import m15


class MsnOdja(object):
    MISSION_INDEX = 15


class OdjaIntroCutscene(MsnOdja, script.CutsceneProps):
    ALIAS = 'intro'
    TITLE = 'База Кадиз'
    THORN_CLASS = m15.KenjiMeetScene
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Trent, ru='Так это ты тот самый Кендзи? Из клана Одзя.',
                  en='So, you\'re the famous Kenji? From the Odja clan?'),
        VoiceLine(20, Kenji, ru='Именно так, мистер Трент. Вы готовы пом+очь мне?',
                  en='Indeed, Mister Trent. Are you prepared to assist me?'),
        VoiceLine(30, Trent,
                  ru='Я гот+ов выполнить задачу от мисс Зейн. Вроде как она доверяет вам. Хотя мне казалось,, что вы будете постарше.',
                  en='I\'m ready to carry out Miss Zane\'s request. She seems to trust you. Though I must admit, I expected you to be... older.'),
        VoiceLine(40, Kenji,
                  ru='Мистер Трент, Кусари - это феодальное образование. Ваше происхождение гораздо больше влияет на ваш социальный статус, чем любые другие заслуги.',
                  en='Mister Trent, Kusari is a feudal state. One\'s lineage influences social standing far more than any personal accomplishments.'),
        VoiceLine(50, Kenji,
                  ru='Я наследник правившей ранее династии. Под мои знамёна готовы вступить множество военных из Кусари. Они уже ожидают,, когда я возглавлю эти силы.',
                  en='I am the heir to the former ruling dynasty. Countless Kusari warriors are ready to rally to my banner. They await my signal to rise.'),
        VoiceLine(60, Kenji,
                  ru='Люди ждут свободы от прогнившего режима. И я гот+ов предоставить им эту свободу и восстановить их честь.',
                  en='The people yearn for freedom from the corrupt regime. And I am prepared to grant them that freedom and restore their honor.'),
        VoiceLine(70, Trent, ru='Это звучало бы более убедительней,, если бы я мог увидеть этих ваших людей.',
                  en='That would sound a lot more convincing if I could actually see these people of yours.'),
        VoiceLine(80, Kenji,
                  ru='Я понимаю. Они сейчас находятся на базе Киото в системе Омега-7. Они лишь ждут нашего приказа. Вы поможете мне добраться туда?',
                  en='I understand. They are currently gathered at Kyoto Base in the Omega-7 system. They await only our command. Will you help me reach them?'),
        VoiceLine(90, Trent,
                  ru='Ну на моём корабле вы точно будете в безопасности. Дайте мне пару минут, я настрою корабль. И тогда полетим.',
                  en='Well, you\'ll be safe on my ship, that\'s for sure. Give me a few minutes to prep the vessel. Then we\'ll fly.'),
        VoiceLine(100, Kenji, ru='Я буду ждать вас,, мистер Трент.', en='I shall await you, Mister Trent.'),
    ]


class KyotoCutscene(MsnOdja, script.CutsceneProps):
    ALIAS = 'kyoto'
    TITLE = 'База Киото'
    THORN_CLASS = m15.KyotoScene
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Otomo, ru='Лорд Кендзи! Вы здесь!', en='Lord Kenji! You\'re here!'),
        VoiceLine(20, Shinja, ru='Наконец-то! Лорд Одзя вернулся!', en='At last! The Odja lord has returned!'),
        VoiceLine(30, Kenji, ru='Друзья, знакомьтесь, это мистер Трент. Он поможет нам в этой операции.',
                  en='Friends, allow me to introduce Mister Trent. He will be assisting us in this operation.'),
        VoiceLine(40, Otomo, ru='Это больш+ая честь увидеть вас лично,, мистер Трент!',
                  en='It is a profound honor to meet you in person, Mister Trent!'),
        VoiceLine(50, Shinja, ru='Надеюсь,, вы когда-либо участвовали в штурмах больш+их систем?',
                  en='I trust you have experience assaulting major systems?'),
        VoiceLine(60, Trent, ru='На самом деле это для меня новый опыт. Обычно такие системы я от пиратов защищаю.',
                  en='Actually, this is new experience for me. Usually, I\'m on the other side, defending such territories from pirates.'),
        VoiceLine(70, Shinja,
                  ru='В этом мире очень легко стать преступником. Но сейчас вы точно на верной стороне,, мистер Трент.',
                  en='In this world, one can easily be branded a criminal. But today, you are unquestionably on the righteous side, Mister Trent.'),
        VoiceLine(80, Shinja,
                  ru='Сегодня вы помогаете пиратам, а завтра они будут править троном и восстанавливать империю!',
                  en='Today, you aid those called pirates. Tomorrow, they may sit upon the throne and restore the Empire!'),

        VoiceLine(110, Kenji, ru='Флот в сборе?', en='Is the fleet assembled?'),
        VoiceLine(120, Otomo, ru='Так точно,, господин.', en='Yes, my lord.'),
        VoiceLine(130, Kenji, ru='Хорошо. Я переберусь на Рюкю. Действуем по плану.',
                  en='Excellent. I will transfer to the Ryukyu. We proceed with the plan.'),
        VoiceLine(140, Kenji,
                  ru='Мистер Трент, присоединяйтесь к Ш+индзя и От+омо. Вместе с линкором Тюг+оку вы будете основн+ой ударной группировкой.',
                  en='Mister Trent, you will join Shinja and Otomo. Together with the battleship Chugoku, you will form the primary strike force.'),
        VoiceLine(150, Kenji, ru='Просто выполняйте приказы. Всю вводную вы получите по дороге.',
                  en='Simply follow orders. You will receive your full briefing en route.'),
        VoiceLine(160, Trent, ru='Слушаюсь и повинуюсь.', en='I hear and obey.'),
    ]

class HokkaidoCutscene(MsnOdja, script.CutsceneProps):
    ALIAS = 'hokk'
    TITLE = 'Планета Хоккайдо'
    THORN_CLASS = m15.HokkaidoScene
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Trent, ru='Хасслер! Опять играешь в гениального комбинатора! Снова сменил свой прикид?',
                  en='Hassler! Still playing the grand strategist, I see! Changed your outfit again?'),
        VoiceLine(20, HasslerEpilogue,
                  ru='Я рад,, что вы живы, мистер Трент. Особенно после всего,, что вы пережили.',
                  en='I am relieved to see you alive, Mister Trent. Especially after everything you\'ve endured.'),
        VoiceLine(30, Trent, ru='Вообще-то,, Хасслер, это были тво+и планы,, которые я отчаянно переживал.',
                  en='Actually, Hassler, those were YOUR plans that I so desperately endured.'),
        VoiceLine(40, HasslerEpilogue,
                  ru='Это всё была инициатива Ямамото, герр Трент. Как вы помните, вместе с вами мы уже пытались изменить ситуацию, когда вызволяли легендарного генерала Трента.',
                  en='That was all Yamamoto\'s initiative, Herr Trent. As you may recall, we had already tried to change the situation together when we extracted the legendary General Trent.'),
        VoiceLine(50, HasslerEpilogue,
                  ru='Герр Ямамото в любом случае решился бы на эту операцию. Со мной или без. С другой сторон+ы, сами подумайте.',
                  en='Herr Yamamoto would have greenlit that operation regardless of my involvement. On the other hand, consider this:'),
        VoiceLine(60, HasslerEpilogue,
                  ru='Так ли был хорош тот план, по итогу которого глава самой могущественной организации в Сириусе попад+ает в плен ко своему главному врагу?',
                  en='how brilliant could that plan have been, if it resulted in the leader of the most powerful organization in Sirius being captured by his mortal enemy?'),
        VoiceLine(70, Trent, ru='А ты хорош, Хасслер, умеешь красиво убеждать. Так ты по службе и продвигаешься?',
                  en='You\'re good, Hassler. You\'ve got a way with words. Is that how you\'re climbing the ladder?'),
        VoiceLine(80, HasslerEpilogue, ru='Не без этого, герр Трент. Красивая презентация всегда имеет значение.',
                  en='It certainly helps, Herr Trent. A polished presentation always matters.'),
        VoiceLine(90, Trent, ru='Тогда какой прок с меня теперь? Давайте презентуйте!',
                  en='So, what use do you have for me now? By all means, present away!'),

        VoiceLine(100, HasslerEpilogue,
                  ru='Я пытался вернуться на работу в Р+ейнланде, но столкнулся с той же ситуацией, что происходит сейчас везде. В верхних эшелонах власти происходит что-то странное.',
                  en='I attempted to return to service in Rheinland, but encountered the same situation now plaguing everyone. Something strange is happening in the upper echelons of power.'),
        VoiceLine(110, HasslerEpilogue,
                  ru='Всё идёт почти точно по тому же сценарию, что был во время первого номадского нашествия. Ситуация может ухудшиться в любой момент. И ухудшиться стремительно.',
                  en='Everything is unfolding almost exactly as it did during the first Nomad incursion. The situation could deteriorate at any moment - and rapidly.'),
        VoiceLine(120, HasslerEpilogue,
                  ru='Количество лояльных нам сил после всех войн не велик+о. Поэтому нам нужн+а помощь пиратов из внешних миров.',
                  en='Our loyal forces are depleted after so many wars. That\'s why we need the help of the pirates from the Edge Worlds.'),

        VoiceLine(130, Trent, ru='Ты хочешь сказать, что мне опять придется отправиться в опасную зону? Почему я?',
                  en='Are you telling me I have to go into another danger zone? Why me?'),

        VoiceLine(140, HasslerEpilogue,
                  ru='Герр Трент, вы теперь человек-легенда. Вы теперь вне правил, вне системы. Вы можете всё. Мы - нет.',
                  en='Herr Trent, you are now a living legend. You operate outside the rules, outside the system. You can do anything. We cannot.'),
        VoiceLine(150, HasslerEpilogue,
                  ru='Да и ставки снова высок+и,, как никогда. Поэтому мы нуждаемся в вашей помощи.',
                  en='Besides, the stakes are once again higher than ever. That is why we need your help.'),

        VoiceLine(160, Trent,
                  ru='Я уже и стал забывать,, что когда-то получал за работу деньги, а не просто похлопывание по плечу и вселенское спасибо.',
                  en='I was starting to forget that I once got paid for my work, instead of just a pat on the back and the universe\'s gratitude.'),
        VoiceLine(170, HasslerEpilogue,
                  ru='Хм... Да, действительно. Герр Кендзи, я могу вас попросить выплатить герру Тренту вознаграждение за его сегодняшнюю работу?',
                  en='Hmm... Yes, a fair point. Herr Kenji, might I ask you to compensate Herr Trent for his efforts today?'),

        VoiceLine(180, Kenji,
                  ru='Конечно. Мистер Трент,, мы не просто у вас в долг+у. Вы получите своё вознаграждение и даже больше в ближайшее время.',
                  en='Of course. Mister Trent, we are not merely in your debt. You will receive your reward - and more - very soon.'),

        VoiceLine(190, Trent, ru='Вот такой формат работы мне нравится гораздо больше!',
                  en='Now THATS a working arrangement I can get behind!'),

        VoiceLine(200, HasslerEpilogue,
                  ru='Это очень хорошо,, что мы нашли с вами общий язык, герр Трент. Отправляйтесь в космос. Вскоре мисс Зейн свяжется с вами по поводу следующего задания.',
                  en='I am delighted we\'ve reached an understanding, Herr Trent. Launch when ready. Miss Zane will contact you shortly with details of your next assignment.'),
    ]

class OdjaSpace(MsnOdja, script.SpaceVoiceProps):
    VOICE_LINES = [
        # VoiceLine(5, Hatcher, ru='Направляемся в Сферу. Трент, веди нас', en='Setting course for the Sphere. Trent, lead the way!'),

    ]

class Mission15(MsnOdja, script.StoryMission):
    CUTSCENES = [
        OdjaIntroCutscene,
        KyotoCutscene,
        HokkaidoCutscene,
    ]
    SPACE_CLASS = OdjaSpace
    SYNC_SPACE = True

    MISSION_TITLE = 'Эпилог. Миссия клана Одзя'
