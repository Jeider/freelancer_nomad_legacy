from story import script
from audio.sound import VoiceLine
from story.actors import Trent, Rockford, Darcy, EdisonTrent, King, Hatcher, Alaric, Mandrake, Missouri, Neuralnet


class Msn13(object):
    MISSION_INDEX = 13


class Msn13BattleshipFirstCutscene(Msn13, script.CutsceneProps):
    ALIAS = 'mount'
    TITLE = 'Ангар линкора Осирис'
    DESCRIPTION = 'Нужно перенести генератор на корабль Старого Трента'
    VOICE_LINES = [
        VoiceLine(10, EdisonTrent, ru='Тезка, нужно перегрузить ко мне энергоэлементы кочевников.'),
        VoiceLine(20, Trent, ru='Хорошо, но зачем?'),
        VoiceLine(30, EdisonTrent, ru='Эта вундервафля запрограммирована на уничтожение кочевников.'),
        VoiceLine(40, EdisonTrent, ru='Если я смогу подключить все эти энергоячейки к реактору своего корабля, для Крыга они засветятся как первичная цель.'),
        VoiceLine(50, EdisonTrent, ru='Затем я отстрелю реактор в черную дыру, и он полетит за ним как мотылек на огонек, ничего не сможет с собой поделать.'),
        VoiceLine(60, EdisonTrent, ru='Только обеспечьте мне несколько спокойных минут, чтобы вся эта мошкара не надоедала.'),
        VoiceLine(70, Trent, ru='Понял! Делаем.'),
        VoiceLine(80, Trent,
                  comment='Затухание экрана. Сцена проявляется с черного экрана. Звук сирены, боевая готовность. Трент идёт к своему кораблю',
                  ru='Время покончить с этим Крыгом.'),
    ]


class Msn13SuccessCutscene(Msn13, script.CutsceneProps):
    ALIAS = 'success'
    TITLE = 'Осирис. Победа'
    DESCRIPTION = 'Раздача призов победителям. И финал'
    VOICE_LINES = [
        VoiceLine(10, King, ru='Сегодня мы чествуем героев! Благодаря их действиям сектор Сириуса и все мы с вами до сих пор существуем!'),
        VoiceLine(20, King, ru='Мы не забудем ваш подвиг никогда! Благодаря вам в секторе Сириуса наконец-то воцарился мир!'),

        VoiceLine(30, Trent, ru='Ага, на пару лет максимум.'),
        VoiceLine(40, Trent, ru='Потом какой-нибудь очередной сумрачный гений найдет очередной могущественный артефакт, '
                    ' все опять будут готовы за него друг другу глотки грызть.'),

        VoiceLine(50, Hatcher, ru='В этом сценарии отсутствуют очередные инопланетяне, а это упущение. Без них уже как-то скучно будет.'),
        VoiceLine(60, Hatcher, ru='Кстати, я тут знаю один отличный бар на нижней палубе, приглашаю всех нажраться за мой счет.'),
        VoiceLine(70, Hatcher, ru='(резко поворачиваясь в другую сторону) Да, Аларик, и тебя, не надо так страстно дышать мне в затылок!'),

        VoiceLine(80, Trent, comment='Бар, "танцуют все", Тренты пересекаются у выхода. Старый и новый',
                  ru='Не присоединишься к компании?'),
        VoiceLine(90, EdisonTrent, ru='Нееет, это вредно для моей формы.'),
        VoiceLine(100, Trent, ru='Что, теперь будешь отдыхать от приключений?'),
        VoiceLine(110, EdisonTrent, ru='Я? Неет, в крайних мирах еще много чего неизвестного. Возможно, там на краю и свидимся, мистер Трент!'),
        VoiceLine(120, Trent, ru='Тогда до скорой встречи, мистер Трент!'),
    ]


class Msn13Space(Msn13, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(5, Hatcher, ru='Направляемся в Сферу. Трент, веди нас'),
        VoiceLine(10, Trent, ru='Профессор, что-то удал+ось узн+ать из д+анных пол+ученных от Р+окфорда?'),
        VoiceLine(20, Mandrake, ru='Да, удал+ось. И всё достаточно серьёзно. В сфере заточён Кр+ыг.'),
        VoiceLine(30, Alaric, ru='Круг? В сф+ере?'),
        VoiceLine(40, Darcy, ru='Аларик, не вр+емя.'),
        VoiceLine(50, Mandrake, ru='Крыгом я для простот+ы называю корабль расы Крыг, '
                               'чтобы не выдумывать специ+ально название, не плодить с+ущности.'),

        VoiceLine(60, Hatcher, ru='Еще одн+а раса?'),
        VoiceLine(70, Mandrake, ru='Древн+ейший ест+ественный враг Дом Кавашей, создателей кочевников. '
                                         'Когда-то давн+о Дом Каваши практ+ически уничт+ожили Крыгов.'),
        VoiceLine(80, Mandrake, ru='И тогда Крыги созд+али оружие, спос+обное уничт+ожить Дом Кавашей, '
                                  'но не примен+яли до с+амого конца, так как оно могл+о навред+ить им сам+им.'),
        VoiceLine(90, Mandrake, ru='В общем, история др+евняя как мир. И, как всегд+а в таких случаях бывает, когда терять им стало нечего, они его таки применили.'),
        VoiceLine(100, Mandrake, ru='Дом Каваши смогли его остановить, хоть и очень дорог+ой ценой. Они построили вокруг Крыга сферу, которая непрерывна выкачивала его практически бесконечную энергию.'),
        VoiceLine(110, Mandrake, ru='И сейчас этой накопленной сферой энергии хватит чтобы уничтожить и саму сферу и Крыга...'),

        VoiceLine(120, Trent, ru='И Р+окфорд хочет запустить этот процесс.'),
        VoiceLine(130, Mandrake, ru='Правильно. А что происходит когда за короткий промежуток времени выделяется практически бесконечная энергия?'),
        VoiceLine(140, Hatcher, ru='Большой пиздец...'),
        VoiceLine(150, Darcy, ru=' Фи, мадам... Но по сути – точно.'),
        VoiceLine(160, Trent, ru='Попробуем остановить?'),
        VoiceLine(170, Mandrake, ru='Попытаемся, мистер Трент, попытаемся...'),

        VoiceLine(180, Mandrake, comment='У ядра Сферы', ru='Мистер Трент, нужно уничтожить энергосистемы до того как лазерная установка выстрелит!'),
        VoiceLine(190, Trent, ru='Принял.'),
        VoiceLine(200, Rockford, ru='Останов+итесь, глупцы, что вы делаете? Я уничт+ожу эту зар+азу раз и навсегда!'),
        VoiceLine(210, Hatcher, ru='И половину сектора Сириуса, придурок! Ох, попадись ты мне маленький засранец...'),
        VoiceLine(220, Rockford, ru='Вы не сможете меня остановить, сейчас всё свершится!'),
        VoiceLine(230, Alaric, ru='Слабительного принял что-ли?'),

        VoiceLine(240, Rockford, "Идиоты, вы сделаете только хуже!"),
        VoiceLine(250, Alaric, "Поздно пить Боржоми, твоим планам настал конец!"),

        VoiceLine(260, Darcy, "Лазер ударил по Крыгу! Мы не успели!"),
        VoiceLine(270, Alaric, "Но вроде мы спасены? Ничего не взорвалось? Всё хорошо ведь, да?"),

        VoiceLine(280, Darcy, "Что происходит?"),
        VoiceLine(290, King, "Всем срочно отойти на безопасную дистанцию!"),

        VoiceLine(300, Alaric, "Ёлки-п+алки..."),
        VoiceLine(310, Darcy, "Оно жив+ое!"),
        VoiceLine(320, Hatcher, "Всем приготовиться! Мы не знаем на что способна эта тварь!"),

        VoiceLine(323, Hatcher, "Миссури под прицелом, выполнить манёвр уклонения!"),
        VoiceLine(326, Alaric, "Слишком поздно!"),

        VoiceLine(330, Hatcher, "Мы потеряли Миссури нахер!"),
        VoiceLine(340, King, "Вышлите спасательные судна с Осириса, срочно!"),

        VoiceLine(350, Mandrake, "Генерал Кинг, Крыг еще слаб. Мы можем нейтрализовать его пока он еще не вошел в силу. Нужно уничтожить генераторы на его корпусе"),
        VoiceLine(360, Trent, "Эй, вы там совсем башкой поехали с такими идеями? Я к этой штуковине не полезу!"),
        VoiceLine(370, King, "Если мы это не сделаем, то Крыг зарядится и перебьет нас как куропаток. Выполняйте, это приказ!"),

        VoiceLine(380, Hatcher, 'Внимание! Крыг готовится к новому удару! Он целится в Осирис!'),
        VoiceLine(390, King, 'Мостик, срочно усильте щиты в зоне вероятного попадания!'),

        VoiceLine(400, Hatcher, 'Осирис получил попадание! Генератор щита выведен из строя, второе такое попадание он не выдержит!'),
        VoiceLine(410, King, 'Команда, срочно уничтожьте генераторы! Реактор Осириса поврежден, мы не сможем быстро выйти из зоны поражения Крыга!'),

        VoiceLine(420, Hatcher, 'Фиксирую новый заряд энергии!'),
        VoiceLine(430, King, 'Шевел+итесь!'),

        VoiceLine(440, Hatcher, 'Нет! Осирис уничтожен!'),

        VoiceLine(450, Hatcher, 'Есть, генераторы Крыга уничтожены! Он закрывается!'),
        VoiceLine(460, Alaric, 'А теперь что с ним?'),

        VoiceLine(470, Mandrake, 'Мы лишили Крыга естественного притока энергии, теперь он пытается восполнить её из Сферы'),

        VoiceLine(480, Mandrake, 'Мистер Трент, нужно дестабилизировать работу энергосистемы Сферы!'),
        VoiceLine(490, Mandrake, 'Вы должн+ы залезть в канализационные каналы и нарушить целостность энергосетей!'),

        VoiceLine(500, Trent, 'Выдвигаюсь!'),

        VoiceLine(510, King, 'Реактор Осириса вошел в норму. Приказ выйти из Сферы. Хетчер, прикрывайте Трента и следите за Крыгом'),
        VoiceLine(520, Hatcher, 'Вас поняли, генерал Кинг'),

        VoiceLine(530, Trent, 'При виде этих дверей у самог+о сжимается...'),

        VoiceLine(540, Hatcher, 'Сфера обесточена. Молодец Трент, теперь давай выбирайся из этих катакомб'),

        VoiceLine(550, Alaric, 'И что теперь? Что нам делать с Крыгом'),
        VoiceLine(560, Mandrake, 'У меня есть одна идея, только нам нужно...'),

        VoiceLine(570, Darcy, 'Корабли Кочевников! Как они тут оказались?!'),
        VoiceLine(580, Mandrake, 'Крыг их подчинил!'),
        VoiceLine(590, Alaric, 'Как?!'),
        VoiceLine(600, Mandrake, 'Полностью! Мистер Трент, нужно срочно вынуть номадское энергоядр+о из установки Р+окфорда!'),
        VoiceLine(610, Trent, 'Принято, сейчас сделаем'),

        VoiceLine(620, Trent, 'Генератор у меня, уходим отсюда!'),
        VoiceLine(630, Hatcher, 'Чёрт, кочевники перегородили проход, мы заблокированы!'),

        VoiceLine(640, EdisonTrent, 'Не падать духом! Вот выход, летите за мной!'),
        VoiceLine(650, Hatcher, 'Срочно улетаем через этот проход! Живо!'),

        VoiceLine(660, Darcy, 'Это +Эдисон Трент? Собственной персоной?'),
        VoiceLine(670, Hatcher, 'Легенда возвращается как никогда вовремя'),  # Alaric?

        VoiceLine(680, Trent, 'Что дальше, профессор?'),
        VoiceLine(690, Mandrake, 'Насколько я понимаю, уничтожить ЭТО сможет только гравитация черной дыры.'),
        VoiceLine(700, Hatcher, 'Ближайшая в омеге-13'),
        VoiceLine(710, Alaric, 'И как же мы заставим ЭТО переместиться в омегу-13?'),
        VoiceLine(720, EdisonTrent, 'Достаточно переместиться туда самим'),
        VoiceLine(730, EdisonTrent, 'Я правильно понял, профессор, зачем вы попросили моего тезку собрать энергоэлементы кочевников?'),
        VoiceLine(740, Mandrake, 'Всё верно. По моим рассчётам энергоядр+о способно издавать сигнатуры Дом Кавашей, на уничтожение которых запрограммирован Крыг'),
        VoiceLine(750, Mandrake, 'Мне лишь неизвестно каким образом это сделать'),
        VoiceLine(760, EdisonTrent, 'Не проблема. На моём корабле есть старая установка профессора Квентейна, которой мы победили кочевников в прошлый раз. Нужно лишь внести пару доработок'),
        VoiceLine(770, Mandrake, 'Мистер Трент, вы просто восхитительны!'),
        VoiceLine(780, King, 'Это звучит как хороший план. Трент, рад тебя слышать. Садитесь на Осирис. Мы доставим вас до Омеги-13'),

        VoiceLine(1000, King, "Сенсоры подтверждают скопление номадских зёрен в этом секторе"),
        VoiceLine(1010, EdisonTrent, "А истребители, линкоры? Есть активность?"),
        VoiceLine(1020, King, "Ответ отрицательный. Путь относительно спокоен. Вы справитесь. Удачи"),

        VoiceLine(1030, EdisonTrent, "Тёзка, держи путь к тому большому астероиду. Астероидное поле не однородно, а через тот большой астероид мы минуем зону радиации"),
        VoiceLine(1040, EdisonTrent, "Только давай не будем будоражить зёрна. Я не хочу нарваться на неприятности"),

        VoiceLine(1050, Trent, "А как ты хочешь забросить маяк в чёрную дыру?"),
        VoiceLine(1060, EdisonTrent, "Я установил на свой корабль специальную катапульту."),
        VoiceLine(1070, EdisonTrent, "Так что не беспокойся. Я запущу маяк с безопасного расстояния"),

        VoiceLine(1080, EdisonTrent, "Осторожней с этими зёрнами..."),

        VoiceLine(1090, EdisonTrent, "Зерно активировалось!"),
        VoiceLine(1100, EdisonTrent, "Да что такое! Тёзка, у нас нет времени!"),
        VoiceLine(1110, EdisonTrent, "Времени мало, мы должн+ы спеш+ить!"),

        VoiceLine(1120, EdisonTrent, "Нам нужно пробить проход в этом астероиде, чтобы пролететь через него"),
        VoiceLine(1130, EdisonTrent, "Отлично, залетаем в туннель!"),
        VoiceLine(1140, EdisonTrent, "Еще одно препятствие, пробей его!"),

        VoiceLine(1145, Trent, "А это еще что за хрень? Придется протискиваться"),

        VoiceLine(1150, Trent, "Эй, что за херн+я?!"),

        VoiceLine(1160, Trent, "Мы вообще где?"),
        VoiceLine(1170, EdisonTrent, "Крыг усилил зерно, оно образовало кокон и заблокировало нас"),
        VoiceLine(1180, EdisonTrent, "Нам нужно снест+и зерно как можно скорее, пока оно не наплодило истребители кочевников!"),

        VoiceLine(1200, Trent, 'Фух, вылетели'),
        VoiceLine(1210, EdisonTrent, "Да, нам повезло..."),
        VoiceLine(1220, EdisonTrent, "Осирис, это Альфа. У нас неприятности, Крыг перестроил зёрна. Теперь они чрезвычайно опасны"),
        VoiceLine(1230, EdisonTrent, 'Будьте осторожны, эти зёрна светятся красным светом и умеют образовывать коконы'),
        VoiceLine(1240, King, 'Вас поняли, Альфа. Вы сами в порядке?'),
        VoiceLine(1250, EdisonTrent, 'Да, всё идёт по плану'),

        VoiceLine(1260, EdisonTrent, 'Тёзка, надо сбить это препятствие'),
        VoiceLine(1270, EdisonTrent, 'Еще одно препятствие'),
        VoiceLine(1280, EdisonTrent, 'С+удя по сенсорам дальше препятствий пока нет, можем пролететь эту секцию на кру+изе'),

        VoiceLine(1290, EdisonTrent, 'Препятствие спереди'),
        VoiceLine(1300, Trent, 'Может лучше сюда?'),
        VoiceLine(1310, EdisonTrent, 'Да, действительно. Летим в этот проход'),

        VoiceLine(1320, EdisonTrent, 'Чёрт, зерно! Стой!'),
        VoiceLine(1330, EdisonTrent, 'Есть другой проход. Давай попробуем эту дорогу'),
        VoiceLine(1340, Trent, 'Кажется чисто'),

        VoiceLine(1350, EdisonTrent, 'Ещё препятствие. Мы почти пролет+ели'),
        VoiceLine(1360, EdisonTrent, 'Меня смущ+ает этот кр+асный свет. Летим остор+ожно...'),
        VoiceLine(1370, EdisonTrent, 'Мы зам+ечены! Чёрт!'),

        VoiceLine(1380, EdisonTrent, 'Попались, мы опять в коконе'),

        VoiceLine(1480, Trent, "Эй, что это за истребители?"),
        VoiceLine(1490, EdisonTrent, "Тяжелые истребители номадов. Они эволюционируют... дел+а плохи"),
        VoiceLine(1500, EdisonTrent, "Зерно тоже стало мощнее... Тёзка, надо ослабить зерно. Раскидай номадские истребители. Тогда зерно ослабнет и мы его разнесём"),
        VoiceLine(1510, Trent, "Сейчас сделаем"),

        VoiceLine(1520, EdisonTrent, "Зерно ослабло, его можно бить. Давай быстрее, времени не в обрез"),

        VoiceLine(1530, Trent, "Есть! Вышли!"),
        VoiceLine(1540, EdisonTrent, "Вот чёрт... кажется сегодня не мой день."),
        VoiceLine(1550, Trent, "Что стряслось?"),
        VoiceLine(1560, EdisonTrent, "Радиация зерна... разрушила мой корабль... А как ты смог её перенести?"),
        VoiceLine(1570, Trent, "Я не знаю... и что теперь делать"),
        VoiceLine(1580, EdisonTrent, "Так, знаешь... я передам маяк тебе. Доставь его сам, один"),
        VoiceLine(1590, Trent, "Но на моём корабле нет катапульты!"),
        VoiceLine(1600, EdisonTrent, "Знаю, знаю... чёрт..."),

        VoiceLine(1610, Mandrake, "Всем внимание! Крыг замечен в системе!"),

        VoiceLine(1620, Trent, "Тёзка, давай мне маяк. Деваться некуда, дотащу сам"),
        VoiceLine(1630, EdisonTrent, "Да, сейчас"),

        VoiceLine(1640, Trent, "Забрал, а ты тут справишься?"),
        VoiceLine(1650, EdisonTrent, "Да, всё будет хорошо. Скорее лети. Удачи там, тёзка"),
        VoiceLine(1660, Trent, "Тебе тоже..."),

        VoiceLine(1800, Hatcher, "Альфа, Крыг стремительно приближается к чёрной дыре! Тороп+итесь, видимо он хочет перегородить вам путь!"),
        VoiceLine(1810, Trent, "Я уже здесь, направляюсь к дыре"),
        VoiceLine(1820, Hatcher, "Трент? А гдеее... второй Трент?"),
        VoiceLine(1830, Trent, "С ним всё хорошо, он решил отдохнуть. Маяк у меня"),
        VoiceLine(1840, Hatcher, "Но ведь..."),
        VoiceLine(1850, Trent, "Плевать, веди меня к дыре"),
        VoiceLine(1860, Hatcher, "Ладно. Это астероидное поле ведет прям к дыре, препятствий быть не должно"),

        VoiceLine(1870, Trent, "Появились ном+адские корабли!"),
        VoiceLine(1880, Hatcher, "Трент, уходи в сторону, у них перехватывающие ракеты!"),

        VoiceLine(1890, Hatcher, "Еще кочевники!"),
        VoiceLine(1900, Trent, "Сколько их тут еще?"),
        VoiceLine(1910, Hatcher, "Предположительно ещё одна группа"),

        VoiceLine(1920, Trent, "А вот и они!"),

        VoiceLine(1930, Trent, "Влетаю в пояс лавовых астероидов"),
        VoiceLine(1940, Hatcher, "Спеши, Крыг рядом!"),

        VoiceLine(1950, Trent, "Странно, что мой корабль еще не развалился. Летим напролом!"),

        VoiceLine(2000, Trent, "Эй, что за дел+а?"),
        VoiceLine(2010, Neuralnet, "Двигатели корабля не работают в пространстве чёрной дыры"),
        VoiceLine(2020, Trent, "И какого хрена мне об этом никто не сказал?"),

        VoiceLine(2030, Neuralnet, "Предлагаю подключить номадское энергоядр+о к питанию корабля"),
        VoiceLine(2040, Trent, "Давай попробуем..."),
        VoiceLine(2050, Trent, "И поскор+ее!"),
        VoiceLine(2060, Trent, "Сколько еще?"),
        VoiceLine(2070, Neuralnet, "Подключение выполняется"),
        VoiceLine(2080, Trent, "Давай быстрее!"),
        VoiceLine(2090, Neuralnet, "Подключение выполняется"),
        VoiceLine(2095, Trent, "Скорее, мать твою!"),
        VoiceLine(2100, Neuralnet, "Подключено"),
        VoiceLine(2110, Trent, "Есть, давим на всю гашетку!"),

    ]

    PROTO3 = [
        "Альфа, Крыг стремительно приближается к чёрной дыре! Торопитесь, видимо он хочет перегородить вам путь!"
        "Я уже здесь, направляюсь к дыре"
        "Трент? А где это... второй Трент?"
        "С ним всё хорошо, он решил отдохнуть. Маяк у меня"
        "Но ведь..."
        "Плевать, веди меня к дыре"
        "Ладно. Это астероидное поле ведет прям к дыре, препятствий быть не должно"
        
        "Появились ном+адские корабли!"
        "Трент, уходи в сторону, у них перехватывающие ракеты!"
        
        "Еще кочевники!"
        "Сколько их тут еще?"
        "Предположительно ещё одна группа"
        
        "А вот и они!"
        
        "Влетаю в пояс лавовых астероидов"
        "Спеши, Крыг рядом!"
        
        "Странно, что мой корабль еще не развалился. Летим напролом!"
        
        "Эй, что за дела?"
        "Двигатели корабля не работают в пространстве чёрной дыры"
        "И какого хрена мне об этом никто не сказал?"
        
        "Предлагаю подключить номадское энергоядро к питанию корабля"
        "Давай попробуем..."
        "И поскорее!"
        "Сколько еще?"
        "Подключение выполняется"
        "Давай быстрее!"
        "Подключение выполняется"
        "Подключено"
        "Есть, давим на всю гашетку!"
    ]

    SECTOR2_NEW_PROTO = [
        "Пришли плохие новости из штаба. Кочевники начинают второжение в колониях. Угроза оказалась гораздо сильнее, чем мы думали",
        "Мистер Трент и профессор Мандрейк сейчас занимаются улучшением энергоустановки, которую мы отправим в чёрную дыру, пока еще не поздно"
        
        "Обстановка. Кочевники уже в Омеге-13. До Чёрной дыры мы можем добраться двумя способами"
        "Первый путь блокирован огромным номадским флотом. Второй путь относительно безопасен."
        "План операции. Группа Альфа в составе обоих Трентов отправится по второму маршруту и отправит маяк в чёрную дыру"
        "Остальными силами мы постараемся отвлечь номадский флот на первом маршруте"
        "Есть вопросы?"
        "А что не так со вторым маршрутом? Почему он относительно безопасен?"
        "Наши сканеры обнаружили скопление номадских зёрен. Точный уровень угрозы неизвестен."
        "Если что-то пойдет не так, то попробуем воспользоваться сложным маршрутом"
        "Именно поэтому мы и проведем отвлекающий маневр, чтобы отвлечь номадские силы и расчистить маршрут"
        "Еще вопросы? Тогда вылетаем по сигналу"
        
        "Осирис, это Трент. Дайте мне маршрут "


    ]


class Mission13(Msn13, script.StoryMission):
    CUTSCENES = [
        Msn13BattleshipFirstCutscene,
        Msn13SuccessCutscene,
    ]
    SPACE_CLASS = Msn13Space
    SYNC_SPACE = True

    MISSION_TITLE = 'Миссия 13. Финал'
