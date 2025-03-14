from story import script
from audio.sound import VoiceLine
from story.actors import Trent, Kim, Rockford, Yamamoto, MaleCaptain, Reichman, EdisonTrent


class Msn11(object):
    MISSION_INDEX = 11



class Msn11AmbushCutscene(Msn11, script.CutsceneProps):
    ALIAS = 'ambush'
    TITLE = 'Бар станции Харадзюку'
    DESCRIPTION = 'Трент подходит к столику Рокфорда'
    VOICE_LINES = [
        VoiceLine(
            10,
            Rockford,
            ru='(Реально удивлённо) Трент?... Да, конечно, присаживайтесь.'
        ),
        VoiceLine(
            20,
            Trent,
            ru='(Заглядывая в КПК Рокфорда) Энгри бёрдс? Какой несерьезный выбор для столь серьезного человека.'
        ),
        VoiceLine(
            30,
            Rockford,
            ru='(Незаинтересованный) Есть еще "Космические Рейнджеры".'
        ),
        VoiceLine(
            40,
            Trent,
            ru='(Ультиматум) Рокфорд, отдай номадский ключ.'
        ),
        VoiceLine(
            50,
            Rockford,
            ru='(Кладёт КПК на стол) Зачем? Чтобы ты отдал его СБА? Или Ордену? Или на кого ты сейчас работаешь?'
        ),

        VoiceLine(
            60,
            Trent,
            comment='Попытки уговорить со стороны Трента',
            ru='Эти артефакты обладают слишком большой разрушительной силой, и если они попадут не в те руки...'
        ),
        VoiceLine(
            70,
            Trent,
            ru='Один псих по фамилии Тилтон так недавно чуть не устроил локальный конец света в Тау-44. '
               'Они должны находиться под присмотром таких организаций как СБА или Орден.'
        ),

        VoiceLine(
            80,
            Rockford,
            comment='Гигантский философский мегадиалог, скорее ближе к "суперзлодей рассказывает суперплан"',
            ru='А что ты вообще знаешь про Орден и СБА? И от кого?'
        ),
        VoiceLine(
            90,
            Rockford,
            ru='Торговля артефактами давно стала прибыльным бизнесом. И не самым опасным, надо сказать.'
        ),
        VoiceLine(
            100,
            Rockford,
            ru='А в отсутствии внешней угрозы эти структуры начали заниматься тем, '
               'на что обречены подобные структуры при отсутствии работы по прямому профилю - борьбе за власть.'
        ),
        VoiceLine(
            110,
            Rockford,
            ru='За власть глобальную, позволяющую не считаться с правительствами. '
               'И ключ номадов, том Протеуса и прочее - в этой игре не больше чем козыри.'
        ),
        VoiceLine(
            120,
            Rockford,
            ru='И если возникнет необходимость, ни СБА, ни Орден не остановится перед тем чтобы применить их '
               'и устроить, как ты выразился, локальный конец света, например, в системе Форбс.'
        ),

        VoiceLine(
            130,
            Trent,
            comment='Трент удивляется, сколько всего сейчас выпалил Рокфорд',
            ru='Ого... Рокфорд, ты сейчас произнес больше слов, чем за все время нашего знакомства.'
        ),

        VoiceLine(
            140,
            Rockford,
            comment='Рокфорд мотивирует свои действия тем, что номады выпилили Коалицию в Солнечной системе',
            ru='Потому что я уже видел гибель миллиардов людей.'
        ),
        VoiceLine(
            150,
            Rockford,
            ru='И все эти рейнландцы, СБА - не более, чем дети, играющие в песочнице найденной боевой гранатой.'
        ),
        VoiceLine(
            160,
            Rockford,
            ru='И вот, им уже стало интересно, что будет, если выдернуть это колечко.'
        ),
        VoiceLine(
            170,
            Rockford,
            ru='А я знаю, как все это прекратить. Сейчас. Раз и навсегда.'
        ),
        VoiceLine(
            180,
            Rockford,
            ru='В моем будущем не будет ни кочевников, ни их наследия. Только человечество. '
               'В полной безопасности от всего этого опасного мусора.'
        ),

        VoiceLine(
            200,
            Rockford,
            comment='Трент лишь офигевающе хлопает ушами',
            ru='(Давай вместе править Галактикой) Не хочешь помочь мне создать такой мир?...'
        ),
        VoiceLine(
            210,
            Rockford,
            ru='(Сматывает удочки) Впрочем, я понимаю, подобные решения трудно принять вот так сразу.'
        ),
        VoiceLine(
            220,
            Rockford,
            ru='(Грозно) Хотя бы не мешайся у меня под ногами, Трент. Мое почтение.'
        ),

        VoiceLine(
            250,
            Trent,
            comment='Через пару мгновений ожидания до Трента доходит',
            ru='Черт... Сообщения от Ким не было!'
        ),
        VoiceLine(
            260,
            Kim,
            comment='Звонок с КПК',
            ru='(Панически кричит) Трент, Рокфорд уходит, скорее взлетаем!'
        ),
        VoiceLine(
            270,
            Trent,
            ru='А что с нашими?'
        ),
        VoiceLine(
            280,
            Kim,
            ru='Их убили...'
        ),
        VoiceLine(
            290,
            Trent,
            ru='Вот чёрт...'
        ),

    ]



class Msn11FinalCutscene(Msn11, script.CutsceneProps):
    ALIAS = 'final'
    TITLE = 'Бар планеты Хонсю'
    DESCRIPTION = 'Трент хотел было набухаться от своих неуспехов, как тут к нему приходит "Старый" Трент...'
    VOICE_LINES = [

        VoiceLine(0, Trent, ru='Мне чего-нибудь покрепче. И побольше.'),

        VoiceLine(10, EdisonTrent, ru='Неудачный день?'),
        VoiceLine(20, Trent, ru='Неудачная жизнь.'),
        VoiceLine(30, EdisonTrent, ru='Хм. А по мне так тебе сказочно везет. Да и с Рокфордом у тебя почти получилось.'),
        VoiceLine(40, Trent, ru='Я устал, нет серьезно, достало все. Берешь простой заказ, а тебе вместе с оплатой впаривают человека, которому ну просто необходимо помочь.'),
        VoiceLine(50, Trent, ru='Он обещает тебе златые горы - и вот, трах-бах, и ты уже по уши увяз в интригах спецслужб, и за твою голову назначена неплохая такая цена.'),
        VoiceLine(60, Trent, ru='И ты пытаешься из всего этого выпутаться, но вместо этого запутываешься еще больше.'),
        VoiceLine(70, Trent, ru='И в конце концов, ты уже не понимаешь за кого и против кого ты, а самое главное - зачем все это?'),

        VoiceLine(80, EdisonTrent, ru='Так всегда и бывает, тезка, ты же фриленсер. Либо ты отстреливаешь мелких бандюков в свободных мирах, летая на ржавом корыте и получаешь за это копейки. Либо так.'),
        VoiceLine(90, EdisonTrent, ru='И считай, тебе  повезло. Сумма у тебя на счету с шестью нулями? Летаешь ты на чем? На самом новом, под тебя тюнингованном? Обвес у тебя из самого нового оружия?'),
        VoiceLine(100, EdisonTrent, ru='А если тебе нужно чего для корабля докупить, ты же даже в счет не заглядываешь - и так знаешь, что хватит, и еще останется.'),
        VoiceLine(110, EdisonTrent, ru='И, самое главное, врагов, у тебя конечно все больше и больше становится, но у тебя появляются друзья.'),
        VoiceLine(120, EdisonTrent, ru='Их немного, гораздо меньше чем врагов, но они настоящие, потому что испытаны боем, прошли огонь, воду, и медные трубы вместе с тобой.'),
        VoiceLine(130, EdisonTrent, ru='И ты уверен, что бы ни случилось, на них можно положиться. И вот эти друзья, они на самом деле намного ценнее, чем шестизначный счет или новейший корабль с лучшим обвесом.'),
        VoiceLine(140, EdisonTrent, ru='Вот так. А пожалеть себя иногда очень хочется, по себе знаю. Главное - не злоупотреблять этим - вредно для формы.'),

        VoiceLine(150, Trent, ru='И вы мне не позволите, да?'),
        VoiceLine(160, EdisonTrent, ru='Я лишь обрисую ситуацию, а ты сам решай...'),
        VoiceLine(170, Trent, ru='Слушаю внимательно.'),
        VoiceLine(180, EdisonTrent, ru='Не здесь. Нам нужно лететь. Расскажу всё по дороге.'),



        VoiceLine(1170, Trent, ru='Ну так, о чём речь.'),

        VoiceLine(1180, EdisonTrent, ru='Если коротко - то все плохо. Рокфорд, как ты понял, решил "спасти" все человечество. И сейчас ни СБА, ни Орден помешать ему уже не могут.'),
        VoiceLine(1190, EdisonTrent, ru='А вот у тебя, учитывая твою патологическую везучесть, может и получиться.'),

        VoiceLine(1200, Trent, ru='А кто такой вообще этот Рокфорд?'),

        VoiceLine(1210, EdisonTrent, ru='Один очень хороший человек, внезапно слетевший с катушек и задавшийся целью осчастливить человечество.'),
        VoiceLine(1220, EdisonTrent, ru='Проблема в том, что в этом случае, обычные клерки приносят в патентные бюро чертежи вечных двигателей, а вот фигуры масштаба Рокфорда могут и уничтожить человечество в процессе спасения.'),

        VoiceLine(1230, Trent, ru='А поконкретнее?'),

        VoiceLine(1240, EdisonTrent, ru='Аттикус Рокфорд... великий и ужасный. Он - из ветеранов Ордена.'),
        VoiceLine(1250, EdisonTrent, ru='Очень болезненно отнесся к тому что Орден не смог предотвратить экспансию кочевников во время того инцедента и занялся изучением артефактов - так называемого наследия кочевников.'),
        VoiceLine(1260, EdisonTrent, ru='Именно он обнаружил ту самую Сферу, и каким-то образом понял что она - своего рода ящик Пандоры, и содержит в себе смертоносную силу.'),
        VoiceLine(1270, EdisonTrent, ru='Мы вместе работали над Сферой. Он нашел способ ее уничтожить, но руководство Ордена было категорически против.'),
        VoiceLine(1280, EdisonTrent, ru='Тогда уже начала проявляться его маниакальность в достижении цели, а я понял, что ключ номадов сможет управлять сферой.'),
        VoiceLine(1290, EdisonTrent, ru='И решил удалиться подальше. Так что мое пленение ксеносами было мною подстроено.'),

        VoiceLine(1300, Trent, ru='Рокфорд как-то в беседе обмолвился, что видел смерть миллиардов человек. О чем он?'),
        VoiceLine(1310, EdisonTrent, ru='О Солнечной Системе. Не забивай себе голову, забудь.'),
        VoiceLine(1320, Trent, ru='Так сколько ему лет? Он был на корабле спящих?'),
        VoiceLine(1330, EdisonTrent, ru='Не о том думаешь, тезка. Не это сейчас главное.'),
        VoiceLine(1340, Trent, ru='Сейчас главное то - что ключ номадов у Рокфорда и он сможет сделать со сферой все что захочет, и никто не сможет ему помешать.'),


        VoiceLine(1350, EdisonTrent, ru='Не совсем так. (достает еще один ключ) В добровольное изгнание к ксенос я отправился не с пустыми руками. Он абсолютно идентичен тому, который сейчас у Рокфорда.'),
        VoiceLine(1360, Trent, ru='И что мне с ним делать?'),
        VoiceLine(1370, EdisonTrent, ru='Решать тебе, но я бы в лучшие свои годы собрал силы, Ордена или СБА и полетел бы прямо к сфере, пытаясь остановить Рокфорда, пока это еще возможно.'),
        VoiceLine(1380, Trent, ru='И почему же вместо того чтобы это сделать, ты сидишь и разговариваешь со мной в баре?'),

        VoiceLine(1390, EdisonTrent, ru='Потому что много лет назад мы сильно разошлись во мнениях с моим бывшим другом и нынешним руководителем СБА, Кингом.'),
        VoiceLine(1400, EdisonTrent, ru='Как раз после того, как я нашел место крушения Испании и... Аттикуса.'),
        VoiceLine(1410, EdisonTrent, ru='Тогда я сильно расстроился, и даже продал свой корабль, надеясь затеряться на узких улочках одной из планет Кусари, но, видимо, не судьба.'),
        VoiceLine(1420, EdisonTrent, ru='А Ямамото... Черт бы побрал этих самураев. Сейчас он занят истреблением врагов и ему плевать на всё.'),
        VoiceLine(1430, EdisonTrent, ru='Даже если этот мир исчезнет во взрыве сверхновой, но с этим взрывом погибнет последний его враг, он будет доволен.'),

        VoiceLine(440, Trent, ru='И какова вероятность, что мне они помогут?'),
        VoiceLine(450, EdisonTrent, ru='Ямамото сейчас не до тебя, а вот на Кинга, полагаю, можешь рассчитывать, его всегда отличали ум и прагматичность.'),
        VoiceLine(460, Trent, ru='Для того, чтобы попросить Кинга о помощи, мне нужно к нему как-то попасть.'),
        VoiceLine(470, EdisonTrent, ru='Держи. Это пропуск СБА высшего уровня.'),
        VoiceLine(480, Trent, ru='И как он поможет мне попасть к Кингу?'),
        VoiceLine(490, EdisonTrent, ru='А в чем проблема? Ты Трент, и я Трент. Мы даже внешне похожи. Поверь, пропуска такого уровня отшибают у охранников все желание создавать проблемы.'),
        VoiceLine(500, Trent, ru='Это настолько тупо, что должно сработать. Рад был видеть!'),

        VoiceLine(510, EdisonTrent, ru='И хандры как ни бывало. Где-ж мои 16 лет? Удачи, тезка!'),
    ]


class Msn11Space(Msn11, script.SpaceVoiceProps):
    VOICE_LINES = [

        VoiceLine(
            10,
            Kim,
            ru='Мистер Трент, Рокфорд сейчас находится в баре станции. Отвлеките его, чтобы наши специалисты могли начать работу с его кораблем.'
        ),
        VoiceLine(
            20,
            Trent,
            ru='И как вы это себе представляете?'
        ),
        VoiceLine(
            30,
            Kim,
            ru='Придумайте что-нибудь. Мне напомнить вам, как недавно несколько десятков пилотов вылетели в один конец, чтобы обеспечить ваше прикрытие?'
        ),
        VoiceLine(
            40,
            Trent,
            ru='Ладно, значит я после посадки сразу иду в бар?'
        ),
        VoiceLine(
            50,
            Kim,
            ru='Да, а мы тут сразу займемся делом. Когда наши специалисты закончат, я пришлю вам сообщение на коммуникатор.'
        ),

        VoiceLine(
            60,
            Kim,
            comment='После вылета с Харадзюку',
            ru='Рокфорд еще на радаре, мы еще можем его нагнать.'
        ),

        VoiceLine(
            60,
            Yamamoto,
            comment='Связь с Ямамото',
            ru='Ямамото на связи.'
        ),
        VoiceLine(
            70,
            Kim,
            ru='Заминировать корабль Рокфорда не удалось. Сейчас ведем погоню...'
        ),
        VoiceLine(
            80,
            Yamamoto,
            ru='Станция "Вавилон" атакована силами Рейнланда! Всем немедленно выдвинуться на защиту!'
        ),
        VoiceLine(
            90,
            Kim,
            ru='О, Цха! Трент, наш штаб атакован, срочно летим на защиту. Даю координаты прыжковой дыры.'
        ),
        VoiceLine(
            100,
            Trent,
            ru='А Рокфорд уйдет...'
        ),

        VoiceLine(
            110,
            Kim,
            comment='Схватка с отрядом рейнланда на выходе из дыры',
            ru='Диверсанты. Уничтожить!'
        ),

        VoiceLine(
            120,
            Kim,
            comment='Выдвигаемся к станции Вавилон',
            ru='Это лейтенант Ким, оборона, доложите обстановку.'
        ),
        VoiceLine(
            120,
            MaleCaptain,
            ru='Враг находится во внутреннем периметре, нужна поддержка!'
        ),
        VoiceLine(
            130,
            Kim,
            ru='Мы летим!'
        ),

        VoiceLine(
            140,
            Kim,
            comment='Все диверсанты ликвидированы',
            ru='Кажется всё.'
        ),
        VoiceLine(
            150,
            Yamamoto,
            ru='Ким, рейнландцы атаковали наше главное хранилище. Был похищен артефакт "генератор номадов". Мы смогли отследить его.'
        ),
        VoiceLine(
            160,
            Yamamoto,
            ru='Генератор доставили на станцию Вена. Немедленно вылетайте с Трентом и звеном прикрытия к этой станции. Я прибуду туда на Мусаси как только смогу.'
        ),

        VoiceLine(
            170,
            Yamamoto,
            comment='Рядом со станцией',
            ru='Ким, наш флот разберется с обороной станции. Вы с Трентом должны заполучить генератор.'
        ),
        VoiceLine(
            180,
            Kim,
            ru='Так точно! Трент, я обнаружила сигнатуры возможного расположения генератора на одном из указанных складов. Их нужно уничтожить.'
        ),
        VoiceLine(
            190,
            Trent,
            ru='А генератор то уцелеет после этого?'
        ),
        VoiceLine(
            200,
            Kim,
            ru='Ты должен был уже усвоить этот урок от Рокфорда. Не мешкай.'
        ),

        VoiceLine(
            210,
            Yamamoto,
            comment='После уничтожения пары складов',
            ru='Обнаружен Вильгельм! Он отстыковался от Вены и двигается в сторону прыжковой дыры. Генератор находится на борту его корабля. Срочно перехватить!'
        ),

        VoiceLine(
            220,
            Trent,
            comment='Проигрывается катсцена. Вильгельм попадает в засаду, его корабль взрывается, а лут забирает Рокфорд',
            ru='Черт, это был Рокфорд! Он ушел в невидимость, прежде чем мы смогли что-то сделать.'
        ),
        VoiceLine(
            230,
            Yamamoto,
            ru='(Ярость) Нееет! Этого нельзя было допустить!'
        ),

        VoiceLine(
            240,
            Reichman,
            comment='Прибывает рейнландское подкрепление',
            ru='(Пока еще горделиво) С вами говорит адмирал Райхман!'
        ),
        VoiceLine(
            250,
            Yamamoto,
            ru='(Яростная злоба) Райхман? Уничтожить его!'
        ),

        VoiceLine(
            260,
            Reichman,
            comment='Линкор райхмана почти уничтожен',
            ru='(Паника) Мы сдаемся! Я сдаюсь!'
        ),
        VoiceLine(
            270,
            Yamamoto,
            ru='(Абсолютный гнев) Сдаешься? Черта с два! Уничтожить линкор Гнейзенау!'
        ),
        VoiceLine(
            280,
            Reichman,
            ru='Ямамото, я же сдался, грязный, ублюдок...'
        ),

        VoiceLine(
            290,
            Kim,
            comment='Линкор и флот рейнланда подавлены',
            ru='Все отряды Рейнланда прекратили сопротивление.'
        ),
        VoiceLine(
            270,
            Yamamoto,
            ru='(Злобный) Так гораздо лучше. Отправить призовую партию на Вену. Взять под конвой корабли Рейнланда.'
        ),
        VoiceLine(
            280,
            Yamamoto,
            ru='(Ярость) И если вы, герры сраные, только попробуете рыпнуться - проследуете за своим вонючим адмиралом.'
        ),

        VoiceLine(
            300,
            Trent,
            ru='А мне что делать?'
        ),


        VoiceLine(
            310,
            Kim,
            ru='Нужна передышка. Возвращемся в Вавилон'
        ),
        VoiceLine(
            320,
            Trent,
            comment='Разговоры во время полёта',
            ru='Ким, что случилось с Ямамото? Райхманн сдавался. Откуда столько ненависти?'
        ),
        VoiceLine(
            330,
            Trent,
            ru='(Охеревающий) А Вавилон? Почему она так плохо охранялась? Где линкоры, тучи истребителей?.. Ким, ты можешь мне ответить?!!'
        ),
        VoiceLine(
            340,
            Kim,
            ru='(Громкое "Я" с желанием вскрикнуть, вдох и... тихое нет на выдохе...) Я... Нет.'
        ),

        VoiceLine(
            350,
            Kim,
            comment='Прошли внешний кордон Вавилон',
            ru='Мистер Трент, у меня срочные дела в штабе. Будьте на связи, вы совсем скоро нам понадобитесь. Можете отдохнуть на станции Вавилон.'
        ),
    ]




class Mission11(Msn11, script.StoryMission):
    CUTSCENES = [
        Msn11AmbushCutscene,
        Msn11FinalCutscene,
    ]
    SPACE_CLASS = Msn11Space

    MISSION_TITLE = 'Миссия 11. Засада на Рокфорда'



