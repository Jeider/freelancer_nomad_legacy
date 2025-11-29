from story import script
from audio.sound import VoiceLine
from story.actors import Trent, Rockford, Darcy, EdisonTrent, King, Hatcher, Alaric, Mandrake, Missouri, Neuralnet
from story.cutscenes.story_scenes import m13_osiris, m13_enter_bh, m13_death, m13_csv


class Msn13(object):
    MISSION_INDEX = 13


class Msn13OsirisCutscene(Msn13, script.CutsceneProps):
    ALIAS = 'osiris'
    TITLE = 'Ангар линкора Осирис'
    THORN_CLASS = m13_osiris.Msn13OsirisScene
    DESCRIPTION = 'Нужно перенести генератор на корабль Старого Трента'
    VOICE_LINES = [
        VoiceLine(10, Darcy, ru="Трент,, давай скорее! Брифинг уже началс+я!", en="Trent, hurry up! The briefing has already started!"),

        VoiceLine(20, King,
                  ru="Приходят плохие новости из штаба. Кочевники начинают вторжение в колониях. Угроза оказалась гораздо серьёзнее,, чем мы думали",
				  en="We're receiving bad news from headquarters. The Nomads have begun their invasion of the colonies. The threat is far more serious than we anticipated."),
        VoiceLine(30, King,
                  ru="Мистер Трент и профессор Мандрейк сейчас занимаются улучшением энергоустановки, которую мы отправим в чёрную дыру,, пока еще не поздно",
				  en="Mister Trent and Professor Mandrake are currently upgrading the power unit we will send into the black hole while we still have time."),

        VoiceLine(50, King,
                  ru="Обстановка. Кочевники уже в Омеге-13 и заполнили большую часть астероидных полей в системе.",
				  en="Situation: The Nomads are already in Omega-13 and have infested most of the system's asteroid fields."),
        VoiceLine(60, King,
                  ru="План операции. Основн+ая боевая группа в виде линкора Осирис и прикрытия совершит атаку на флот номадов, чтобы оттянуть их силы от зоны, примыкающей к чёрной дыре",
				  en="Operation Plan: The main battle group, consisting of the battleship Osiris and its escorts, will attack the Nomad fleet to draw their forces away from the area adjacent to the black hole."),
        VoiceLine(70, King,
                  ru="В это же время мобильная диверсионная группа в составе обоих мистеров Трентов отправится к чёрной дыре через зону со старыми шахтами",
				  en="Simultaneously, a mobile sabotage team, comprising both Misters Trent, will proceed to the black hole via the old mining zone."),
        VoiceLine(80, King,
                  ru="Сенсоры отмечают минимальную номадскую активность в этой локации. Путь ожидается относительно безопасным",
				  en="Sensors indicate minimal Nomad activity in that location. The route is expected to be relatively safe."),
        VoiceLine(90, King, ru="Есть вопросы?", en='Any questions?'),
        VoiceLine(100, Trent, ru="А почему путь через шахты лишь относительно безопасен?", en="Why is the route through the mines only relatively safe?"),
        VoiceLine(110, King,
                  ru="В этой зоне обнаружено скопление номадских зёрен. Они пассивны. Если быть осторожными и не будоражить зёрна, то иных препятствий на пути не замечено.",
				  en="A cluster of Nomad seeds has been detected in that area. They are dormant. If you are cautious and do not agitate the seeds, no other obstacles have been detected along the path."),
        VoiceLine(120, King, ru="Еще вопросы? Нет? Тогда вылетаем по сигналу. Всем удачи", en="Any other questions? No? Then launch on my signal. Good luck to everyone!"),

        VoiceLine(200, Trent, ru="Ну что,, Ал, гот+ов сегодня спасти мир?", en="So, Al, ready to save the world today?"),
        VoiceLine(210, Alaric, ru="Эй! Я смотрю тебе наконец понравилось работать на спецслужбы!", en="Hey! Look at you, finally starting to enjoy working for the intelligence agencies!"),
        VoiceLine(220, Trent, ru="По крайней мере сейчас я знаю за что воюю", en="At least now I know what I'm fighting for!"),
        VoiceLine(230, Alaric, ru="Только давай береги себя,, друг. Сейчас ставки как никогда высоки", en="Just make sure to watch your back, buddy. The stakes have never been higher!"),

        VoiceLine(240, Darcy, ru="Да, Трент. Даже самому крутому эксперту по номадам,, как ты, везение сегодня будет не лишним", en="Yeah, Trent. Even for a top Nomad expert like you, a little luck wouldn't hurt today."),
        VoiceLine(250, Trent,
                  ru="Да хватит уже. Мы тут все давно эксперты по дом-кавашам, кочевникам,, крыгам и всему подобному",
				  en="Oh, come on! At this point, we're all experts on the Dom\'Kavash, the Nomads, the Krieg, and everything in between."),
        VoiceLine(260, Alaric,
                  ru="Именно так. Так что давайте воспользуемся нашим экспертным опытом и надерём уже зад этой инопланетной нечисти",
				  en=" Damn right we are! So let's use our expert knowledge and finally kick this alien scum's ass!"),
        VoiceLine(270, Darcy, ru="Хочешь показать им,, кто тут главный гуманоид на районе?", en="Ready to show them who the top humanoid in the entire Sirius Sector is?"),
        VoiceLine(280, Trent, ru="Удачи,, друзья. А теперь приступим!", en="Good luck, friends. Now, let's do this!"),
    ]


class Msn13EnterBlackholeCutscene(Msn13, script.CutsceneProps):
    ALIAS = 'enter_bh'
    TITLE = 'Влёт в Чёрную Дыру'
    THORN_CLASS = m13_enter_bh.Msn13EnterBlackholeScene
    DESCRIPTION = ''
    VOICE_LINES = []


class Msn13KriegDeathCutscene(Msn13, script.CutsceneProps):
    ALIAS = 'death'
    TITLE = 'Внутренности Чёрной Дыры'
    THORN_CLASS = m13_death.Msn13KriegDeathScene
    DESCRIPTION = ''
    VOICE_LINES = []


class Msn13CsvMagnetCutscene(Msn13, script.CutsceneProps):
    ALIAS = 'csv'
    TITLE = 'Омега-13 после чёрной дыры'
    THORN_CLASS = m13_csv.Msn13CSVMagnetScene
    DESCRIPTION = ''
    VOICE_LINES = []


class Msn13Space(Msn13, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(5, Hatcher, ru='Направляемся в Сферу. Трент, веди нас', en='Setting course for the Sphere. Trent, lead the way!'),
        VoiceLine(10, Trent, ru='Профессор, что-то удал+ось узн+ать из д+анных пол+ученных от Р+окфорда?', en='Professor, were you able to learn anything from the data we got from Rockford?'),
        VoiceLine(20, Mandrake, ru='Да, удал+ось. И всё достаточно серьёзно. В сфере заточён Кр+ыг.', en='Yes, indeed. And it\'s quite serious. The Sphere contains a captive Krieg.'),
        VoiceLine(30, Alaric, ru='Круг? В сф+ере?', en='A Crab? Inside the Sphere?'),
        VoiceLine(40, Darcy, ru='Аларик, не вр+емя.', en='Alaric, not the time.'),
        VoiceLine(50, Mandrake, ru='Крыгом я для простот+ы называю корабль расы Крыг, '
                               'чтобы не выдумывать специ+ально название, не плодить с+ущности.',
							   en='For simplicity, I use "Krieg" to refer to the Warship of the Krieg race, '
							   'to avoid inventing a separate name and creating confusion by multiplying entities.'),

        VoiceLine(60, Hatcher, ru='Еще одн+а раса?', en='Another race?'),
        VoiceLine(70, Mandrake, ru='Древн+ейший ест+ественный враг Дом Кавашей, создателей кочевников. '
                                         'Когда-то давн+о Дом Каваши практ+ически уничт+ожили Крыгов.',
								en='The ancient, natural enemy of the Dom\'Kavash, the creators of the Nomads. '
										'Long ago, the Dom\'Kavash nearly wiped out the Krieg.'),
        VoiceLine(80, Mandrake, ru='И тогда Крыги созд+али оружие, спос+обное уничт+ожить Дом Кавашей, '
                                  'но не примен+яли до с+амого конца, так как оно могл+о навред+ить им сам+им.',
								en='In response, the Krieg created a weapon capable of destroying the Dom\'Kavash, '
								  'but they held back from using it until the very end, as it could also harm them.'),
        VoiceLine(90, Mandrake, ru='В общем, история др+евняя как мир. И, как всегд+а в таких случаях бывает, когда терять им стало нечего, они его таки применили.',
								en='It\'s a story as old as time. And, as always happens in such cases, when they had nothing left to lose—they finally used it.'),
        VoiceLine(100, Mandrake, ru='Дом Каваши смогли его остановить, хоть и очень дорог+ой ценой. Они построили вокруг Крыга сферу, которая непрерывна выкачивала его практически бесконечную энергию.', en='The Dom\'Kavash managed to stop it, albeit at a great cost. They built a Sphere around the Krieg, which continuously syphons its near-infinite energy.'),
        VoiceLine(110, Mandrake, ru='И сейчас этой накопленной сферой энергии хватит чтобы уничтожить и саму сферу и Крыга...',
								 en='And now, the energy accumulated by the Sphere is sufficient to destroy both the Sphere itself and the Krieg...'),

        VoiceLine(120, Trent, ru='И Р+окфорд хочет запустить этот процесс.', en='And Rockford wants to initiate that process.'),
        VoiceLine(130, Mandrake, ru='Правильно. А что происходит когда за короткий промежуток времени выделяется практически бесконечная энергия?', en='Correct. And what happens when a near-infinite amount of energy is released in a very short time?'),
        VoiceLine(140, Hatcher, ru='Большой пиздец...', en='A total fucking cataclysm...'),
        VoiceLine(150, Darcy, ru=' Фи, мадам... Но по сути – точно.', en='Phrasing, ma\'am... But in essence—absolutely.'),
        VoiceLine(160, Trent, ru='Попробуем остановить?', en='And we can stop it?'),
        VoiceLine(170, Mandrake, ru='Попытаемся, мистер Трент, попытаемся...', en='We can but try, Mister Trent... we can but try.'),

        VoiceLine(180, Mandrake, comment='У ядра Сферы', ru='Мистер Трент, нужно уничтожить энергосистемы до того как лазерная установка выстрелит!',
														 en='Mister Trent, you must destroy the power systems before the laser array fires!'),
        VoiceLine(190, Trent, ru='Принял.', en='Understood.'),
        VoiceLine(200, Rockford, ru='Останов+итесь, глупцы, что вы делаете? Я уничт+ожу эту зар+азу раз и навсегда!',
								 en='Stop, you fools! What are you doing? I will destroy this scourge once and for all!'),
        VoiceLine(210, Hatcher, ru='И половину сектора Сириуса, придурок! Ох, попадись ты мне маленький засранец...',
								en='And half the Sirius Sector with it, you maniac! Oh, just let me get my hands on you, you little shit...'),
        VoiceLine(220, Rockford, ru='Вы не сможете меня остановить, сейчас всё свершится!', en='You can\'t stop me now! It is almost done!'),
        VoiceLine(230, Alaric, ru='Слабительного принял что-ли?', en='What, did you take a laxative?'),

        VoiceLine(240, Rockford, ru="Идиоты, вы сделаете только хуже!", en="You idiots, you'll only make things worse!"),
        VoiceLine(250, Alaric, ru="Поздно пить Боржоми, твоим планам настал конец!", en="Too late, slowpoke! Your little plan is toast!"),

        VoiceLine(260, Darcy, ru="Лазер ударил по Крыгу! Мы не успели!", en="The laser has hit the Krieg! We were too late!"),
        VoiceLine(270, Alaric, ru="Но вроде мы спасены? Ничего не взорвалось? Всё хорошо ведь, да?", en="But... we're safe, right? Nothing\'s blowing up? It\'s all good, yeah?"),

        VoiceLine(280, Darcy, ru="Что происходит?", en="What\'s happening?"),
        VoiceLine(290, King, ru="Всем срочно отойти на безопасную дистанцию!", en="All units, pull back to a safe distance immediately!"),

        VoiceLine(300, Alaric, ru="Ёлки-п+алки...", en="Holy cow..."),
        VoiceLine(310, Darcy, ru="Оно жив+ое!", en="It\'s alive!"),
        VoiceLine(320, Hatcher, ru="Всем приготовиться! Мы не знаем на что способна эта тварь!", en="All ships, battle stations! We have no idea what that thing is capable of!"),

        VoiceLine(323, Hatcher, ru="Миссури под прицелом, выполнить манёвр уклонения!", en="Missouri is being targeted, execute evasive maneuvers!"),
        VoiceLine(326, Alaric, ru="Слишком поздно!", en="Too late!"),

        VoiceLine(330, Hatcher, ru="Мы потеряли Миссури нахер!", en="We've just lost the fucking Missouri!"),
        VoiceLine(340, King, ru="Вышлите спасательные судна с Осириса, срочно!", en="Dispatch rescue craft from the Osiris, now!"),

        VoiceLine(350, Mandrake, ru="Генерал Кинг, Крыг еще слаб. Мы можем нейтрализовать его пока он еще не вошел в силу. Нужно уничтожить генераторы на его корпусе",
								 en="General King, the Krieg is still weak. We can neutralize it before it fully powers up. We must destroy the generators on its hull!"),
        VoiceLine(360, Trent, ru="Эй, вы там совсем башкой поехали с такими идеями? Я к этой штуковине не полезу!",
							  en="Are you all out of your minds with that idea? I'm not going anywhere near that thing!"),
        VoiceLine(370, King, ru="Если мы это не сделаем, то Крыг зарядится и перебьет нас как куропаток. Выполняйте, это приказ!",
							 en="If we don't do this, the Krieg will recharge and pick us off like sitting ducks. Do it, that's an order!"),

        VoiceLine(380, Hatcher, ru='Внимание! Крыг готовится к новому удару! Он целится в Осирис!', en="Attention! The Krieg is preparing another strike! It's targeting the Osiris!"),
        VoiceLine(390, King, ru='Мостик, срочно усильте щиты в зоне вероятного попадания!', en="Bridge, reinforce shields in the projected impact zone, now!"),

        VoiceLine(400, Hatcher, ru='Осирис получил попадание! Генератор щита выведен из строя, второе такое попадание он не выдержит!',
								en="The Osiris has been hit! The shield generator is disabled; it won't survive another impact like that!"),
        VoiceLine(410, King, ru='Команда, срочно уничтожьте генераторы! Реактор Осириса поврежден, мы не сможем быстро выйти из зоны поражения Крыга!',
							 en='Team, destroy those generators now! The Osiris\'s reactor is damaged; we can\'t get out of the Krieg\'s firing range quickly enough!'),

        VoiceLine(420, Hatcher, ru='Фиксирую новый заряд энергии!', en='I\'m detecting a new energy buildup!'),
        VoiceLine(430, King, ru='Шевел+итесь!', en='Move it!'),

        VoiceLine(440, Hatcher, ru='Нет! Осирис уничтожен!', en="No! Osiris is destroyed!"),

        VoiceLine(450, Hatcher, ru='Есть, генераторы Крыга уничтожены! Он закрывается!', en='Yes, the Krieg\'s generators are destroyed! It\'s... sealing itself!'),
        VoiceLine(460, Alaric, ru='А теперь что с ним?', en='Now what\'s it doing?'),

        VoiceLine(470, Mandrake, ru='Мы лишили Крыга естественного притока энергии, теперь он пытается восполнить её из Сферы',
								 en='We\'ve cut off the Krieg\'s natural energy intake; now it\'s attempting to draw power directly from the Sphere.'),

        VoiceLine(480, Mandrake, ru='Мистер Трент, нужно дестабилизировать работу энергосистемы Сферы!', en='Mister Trent, you need to destabilize the Sphere\'s energy grid!'),
        VoiceLine(490, Mandrake, ru='Вы должн+ы залезть в канализационные каналы и нарушить целостность энергосетей!',
								 en='You must access the maintenance conduits and disrupt the power networks!'),

        VoiceLine(500, Trent, ru='Выдвигаюсь!', en='On my way!'),

        VoiceLine(510, King, ru='Реактор Осириса вошел в норму. Приказ выйти из Сферы. Хетчер, прикрывайте Трента и следите за Крыгом',
							 en='The Osiris\'s reactor is back to normal. All units, withdraw from the Sphere. Hatcher, provide cover for Trent and keep an eye on the Krieg!'),
        VoiceLine(520, Hatcher, ru='Вас поняли, генерал Кинг', en='Understood, General King!'),

        VoiceLine(530, Trent, ru='При виде этих дверей у самог+о сжимается...', en='Seeing these doors is making my own pucker up...'),

        VoiceLine(540, Hatcher, ru='Сфера обесточена. Молодец Трент, теперь давай выбирайся из этих катакомб',
								en='The Sphere is powered down. Good work, Trent, now get out of those catacombs!'),

        VoiceLine(550, Alaric, ru='И что теперь? Что нам делать с Крыгом', en=' So now what? What do we do with the Krieg?'),
        VoiceLine(560, Mandrake, ru='У меня есть одна идея, только нам нужно...', en='I have one idea, but we need to...'),

        VoiceLine(570, Darcy, ru='Корабли Кочевников! Как они тут оказались?!', en='Nomad ships! How did they get here?!'),
        VoiceLine(580, Mandrake, ru='Крыг их подчинил!', en='The Krieg has subjugated them!'),
        VoiceLine(590, Alaric, ru='Как?!', en='How?!'),
        VoiceLine(600, Mandrake, ru='Полностью! Мистер Трент, нужно срочно вынуть номадское энергоядр+о из установки Р+окфорда!',
								 en='Completely! Mister Trent, we must urgently remove the Nomad power core from Rockford\'s device!'),
        VoiceLine(610, Trent, ru='Принято, сейчас сделаем', en='Understood, on it!'),

        VoiceLine(620, Trent, ru='Генератор у меня, уходим отсюда!', en='I\'ve got the generator, let\'s get out of here!'),
        VoiceLine(630, Hatcher, ru='Чёрт, кочевники перегородили проход, мы заблокированы!', en='Damn it, the Nomads have blocked the passage! We\'re trapped!'),

        VoiceLine(640, EdisonTrent, ru='Не падать духом! Вот выход, летите за мной!', en='Don\'t lose hope! Here\'s an exit, follow me!'),
        VoiceLine(650, Hatcher, ru='Срочно улетаем через этот проход! Живо!', en='Everyone, through that passage, now! Move!'),

        VoiceLine(660, Darcy, ru='Это +Эдисон Трент? Собственной персоной?', en='Is that... Edison Trent? In the flesh?'),
        VoiceLine(670, Hatcher, ru='Легенда возвращается как никогда вовремя', en='The legend returns, and not a moment too soon!'),  # Alaric?

        VoiceLine(680, Trent, ru='Что дальше, профессор?', en='What\'s the next step, Professor?'),
        VoiceLine(690, Mandrake, ru='Насколько я понимаю, уничтожить ЭТО сможет только гравитация черной дыры.',
								 en='As I understand it, the only thing that can destroy the Krieg is the gravity of a black hole.'),
        VoiceLine(700, Hatcher, ru='Ближайшая в омеге-13', en='The nearest one is in Omega-13.'),
        VoiceLine(710, Alaric, ru='И как же мы заставим ЭТО переместиться в омегу-13?', en='And how do we get THAT thing to move to Omega-13?'),
        VoiceLine(720, EdisonTrent, ru='Достаточно переместиться туда самим', en='We just have to go there ourselves.'),
        VoiceLine(730, EdisonTrent, ru='Я правильно понял, профессор, зачем вы попросили моего тезку собрать энергоэлементы кочевников?',
									en='If I understand you correctly, Professor, that\'s why you had my namesake gather the Nomad power cells?'),
        VoiceLine(740, Mandrake, ru='Всё верно. По моим рассчётам энергоядр+о способно издавать сигнатуры Дом Кавашей, на уничтожение которых запрограммирован Крыг',
								 en='Precisely. My calculations indicate the power core can emit Dom\'Kavash signatures—the very entity the Krieg is programmed to annihilate.'),
        VoiceLine(750, Mandrake, ru='Мне лишь неизвестно каким образом это сделать', en='I was just unsure of the method to achieve this.'),
        VoiceLine(760, EdisonTrent, ru='Не проблема. На моём корабле есть старая установка профессора Квентейна, которой мы победили кочевников в прошлый раз. Нужно лишь внести пару доработок', en='Not a problem. My ship has Professor Quintaine\'s old device, the one we used to defeat the Nomads last time. It just needs a few modifications.'),
        VoiceLine(770, Mandrake, ru='Мистер Трент, вы просто восхитительны!', en='Mister Trent, you are truly remarkable!'),
        VoiceLine(780, King, ru='Это звучит как хороший план. Трент, рад тебя слышать. Садитесь на Осирис. Мы доставим вас до Омеги-13',
							 en='Now that sounds like a solid plan. Trent, good to hear your voice. Everyone, dock with the Osiris. We\'ll get you to Omega-13.'),

        VoiceLine(1000, King, ru="Сенсоры подтверждают скопление номадских зёрен в этом секторе", en='Sensors confirm a cluster of Nomad seeds in this sector.'),
        VoiceLine(1010, EdisonTrent, ru="А истребители, линкоры? Есть активность?", en='And fighters? Battleships? Any activity?'),
        VoiceLine(1020, King, ru="Ответ отрицательный. Путь относительно спокоен. Вы справитесь. Удачи", en='Negative. The path is relatively clear. You can handle it. Good luck!'),

        VoiceLine(1030, EdisonTrent, ru="Тёзка, держи путь к тому большому астероиду. Астероидное поле не однородно, а через тот большой астероид мы минуем зону радиации",
									 en='Namesake, set a course for that large asteroid. The field isn\'t uniform; passing by that big rock will let us bypass the radiation zone.'),
        VoiceLine(1040, EdisonTrent, ru="Только давай не будем будоражить зёрна. Я не хочу нарваться на неприятности", en='Just let\'s not agitate the seeds. I don\'t want any trouble.'),

        VoiceLine(1050, Trent, ru="А как ты хочешь забросить маяк в чёрную дыру?", en='How do you plan to get the beacon into the black hole?'),
        VoiceLine(1060, EdisonTrent, ru="Я установил на свой корабль специальную катапульту.", en='I\'ve fitted my ship with a special catapult.'),
        VoiceLine(1070, EdisonTrent, ru="Так что не беспокойся. Я запущу маяк с безопасного расстояния", en='So don\'t worry. I\'ll launch the beacon from a safe distance.'),

        VoiceLine(1080, EdisonTrent, ru="Осторожней с этими зёрнами...", en='Careful with those seeds...'),

        VoiceLine(1090, EdisonTrent, ru="Зерно активировалось!", en='The seed is activated!'),
        VoiceLine(1100, EdisonTrent, ru="Да что такое! Тёзка, у нас нет времени!", en='What the hell! Namesake, we don\'t have time for this!'),
        VoiceLine(1110, EdisonTrent, ru="Времени мало, мы должн+ы спеш+ить!", en='Time is short, we have to hurry!'),

        VoiceLine(1120, EdisonTrent, ru="Нам нужно пробить проход в этом астероиде, чтобы пролететь через него", en='We need to blast a passage through this asteroid to fly through it.'),
        VoiceLine(1130, EdisonTrent, ru="Отлично, залетаем в туннель!", en='Perfect, heading into the tunnel!'),
        VoiceLine(1140, EdisonTrent, ru="Еще одно препятствие, пробей его!", en='Another obstacle, blast through it!'),

        VoiceLine(1145, Trent, ru="А это еще что за хрень? Придется протискиваться", en='What the hell is this now? Gotta squeeze through!'),

        VoiceLine(1150, Trent, ru="Эй, что за херн+я?!", en='Hey, what the hell?!'),

        VoiceLine(1160, Trent, ru="Мы вообще где?", en='Where even are we?'),
        VoiceLine(1170, EdisonTrent, ru="Крыг усилил зерно, оно образовало кокон и заблокировало нас", en='The Krieg has enhanced the seed! It\'s formed a cocoon and trapped us!'),
        VoiceLine(1180, EdisonTrent, ru="Нам нужно снест+и зерно как можно скорее, пока оно не наплодило истребители кочевников!",
									 en='We need to take that seed out ASAP, before it spawns more Nomad fighters!'),

        VoiceLine(1200, Trent, ru='Фух, вылетели', en='Phew, we\'re out!'),
        VoiceLine(1210, EdisonTrent, ru="Да, нам повезло...", en='Yeah, we got lucky...'),
        VoiceLine(1220, EdisonTrent, ru="Осирис, это Альфа. У нас неприятности, Крыг перестроил зёрна. Теперь они чрезвычайно опасны",
									 en='Osiris, this is Alpha. We\'ve got a problem. The Krieg has reconfigured the seeds. They\'re extremely dangerous now!'),
        VoiceLine(1230, EdisonTrent, ru='Будьте осторожны, эти зёрна светятся красным светом и умеют образовывать коконы',
									 en='Be advised, these seeds glow red and can form containment cocoons!'),
        VoiceLine(1240, King, ru='Вас поняли, Альфа. Вы сами в порядке?', en='Understood, Alpha. Are you two alright?'),
        VoiceLine(1250, EdisonTrent, ru='Да, всё идёт по плану', en='Affirmative. Still on plan.'),

        VoiceLine(1260, EdisonTrent, ru='Тёзка, надо сбить это препятствие', en='Namesake, need to clear that obstruction.'),
        VoiceLine(1270, EdisonTrent, ru='Еще одно препятствие', en='Another one!'),
        VoiceLine(1280, EdisonTrent, ru='С+удя по сенсорам дальше препятствий пока нет, можем пролететь эту секцию на кру+изе',
									 en='Sensors show the way is clear for a stretch, we can cruise through this section.'),

        VoiceLine(1290, EdisonTrent, ru='Препятствие спереди', en='Obstruction ahead!'),
        VoiceLine(1300, Trent, ru='Может лучше сюда?', en='Maybe this way is better?'),
        VoiceLine(1310, EdisonTrent, ru='Да, действительно. Летим в этот проход', en='Yes, you\'re right. Let\'s take this passage!'),

        VoiceLine(1320, EdisonTrent, ru='Чёрт, зерно! Стой!', en='Damn, a seed! Stop!'),
        VoiceLine(1330, EdisonTrent, ru='Есть другой проход. Давай попробуем эту дорогу', en='There\'s another passage. Let\'s try that route!'),
        VoiceLine(1340, Trent, ru='Кажется чисто', en='Looks clear.'),

        VoiceLine(1350, EdisonTrent, ru='Ещё препятствие. Мы почти пролет+ели', en='Another obstacle. We\'re almost through!'),
        VoiceLine(1360, EdisonTrent, ru='Меня смущ+ает этот кр+асный свет. Летим остор+ожно...', en='That red glow is making me nervous. Proceed with caution...'),
        VoiceLine(1370, EdisonTrent, ru='Мы зам+ечены! Чёрт!', en='We\'ve been spotted! Damn it!'),

        VoiceLine(1380, EdisonTrent, ru='Попались, мы опять в коконе', en='We\'re caught, another cocoon!'),

        VoiceLine(1480, Trent, ru="Эй, что это за истребители?", en='Hey, what kind of fighters are these?'),
        VoiceLine(1490, EdisonTrent, ru="Тяжелые истребители номадов. Они эволюционируют... дел+а плохи", en='Heavy Nomad fighters. They\'re evolving... this is bad.'),
        VoiceLine(1500, EdisonTrent, ru="Зерно тоже стало мощнее... Тёзка, надо ослабить зерно. Раскидай номадские истребители. Тогда зерно ослабнет и мы его разнесём",
									 en='The seed is more powerful too... Namesake, we need to weaken the seed. Take out the Nomad fighters. That will weaken the seed, and then we can destroy it!'),
        VoiceLine(1510, Trent, ru="Сейчас сделаем", en='On it!'),

        VoiceLine(1520, EdisonTrent, ru="Зерно ослабло, его можно бить. Давай быстрее, времени не в обрез", en='The seed is vulnerable, it can be hit now. Hurry, we\'re running out of time!'),

        VoiceLine(1530, Trent, ru="Есть! Вышли!", en='Yes! We\'re out!'),
        VoiceLine(1540, EdisonTrent, ru="Вот чёрт... кажется сегодня не мой день.", en='Ah, damn it... Seems it\'s not my day.'),
        VoiceLine(1550, Trent, ru="Что стряслось?", en='What\'s wrong?'),
        VoiceLine(1560, EdisonTrent, ru="Радиация зерна... разрушила мой корабль... А как ты смог её перенести?",
									 en='The seed\'s radiation... it\'s wrecked my ship... How were you able to withstand it?'),
        VoiceLine(1570, Trent, ru="Я не знаю... и что теперь делать", en='I don\'t know... So what do we do now?'),
        VoiceLine(1580, EdisonTrent, ru="Так, знаешь... я передам маяк тебе. Доставь его сам, один",
									 en='Okay, listen... I\'m transferring the beacon to you. You have to deliver it alone.'),
        VoiceLine(1590, Trent, ru="Но на моём корабле нет катапульты!", en='But my ship doesn\'t have a catapult!'),
        VoiceLine(1600, EdisonTrent, ru="Знаю, знаю... чёрт...", en='I know, I know... damn it...'),

        VoiceLine(1610, Mandrake, ru="Всем внимание! Крыг замечен в системе!", en='Everyone, attention! The Krieg has been detected in the system!'),

        VoiceLine(1620, Trent, ru="Тёзка, давай мне маяк. Деваться некуда, дотащу сам", en='Namesake, give me the beacon. I have no choice, I\'ll carry it myself!'),
        VoiceLine(1630, EdisonTrent, ru="Да, сейчас", en='Yeah, here...'),

        VoiceLine(1640, Trent, ru="Забрал, а ты тут справишься?", en='I\'ve got it. Will you be okay here?'),
        VoiceLine(1650, EdisonTrent, ru="Да, всё будет хорошо. Скорее лети. Удачи там, тёзка", en='Yeah, I\'ll be fine. Now fly, quickly. Good luck out there, namesake!'),
        VoiceLine(1660, Trent, ru="Тебе тоже...", en='You too...'),

        VoiceLine(1800, Hatcher, ru="Альфа, Крыг стремительно приближается к чёрной дыре! Тороп+итесь, видимо он хочет перегородить вам путь!",
								 en='Alpha, the Krieg is approaching the black hole at high velocity! Hurry, it seems to be trying to cut you off!'),
        VoiceLine(1810, Trent, ru="Я уже здесь, направляюсь к дыре", en='I\'m already here, heading for the hole!'),
        VoiceLine(1820, Hatcher, ru="Трент? А гдеее... второй Трент?", en='Trent? Where\'s the... other Trent?'),
        VoiceLine(1830, Trent, ru="С ним всё хорошо, он решил отдохнуть. Маяк у меня", en='He\'s fine, he decided to take a break. I have the beacon!'),
        VoiceLine(1840, Hatcher, ru="Но ведь...", en='But...'),
        VoiceLine(1850, Trent, ru="Плевать, веди меня к дыре", en='Doesn\'t matter! Just guide me to the hole!'),
        VoiceLine(1860, Hatcher, ru="Ладно. Это астероидное поле ведет прям к дыре, препятствий быть не должно",
								       en='Alright. This asteroid field leads straight to it. There shouldn\'t be any obstacles.'),

        VoiceLine(1870, Trent, ru="Появились ном+адские корабли!", en='Nomad ships incoming!'),
        VoiceLine(1880, Hatcher, ru="Трент, уходи в сторону, у них перехватывающие ракеты!", en='Trent, break off! They have tracking missiles!'),

        VoiceLine(1890, Hatcher, ru="Еще кочевники!", en='More Nomads!'),
        VoiceLine(1900, Trent, ru="Сколько их тут еще?", en='How many are there?!'),
        VoiceLine(1910, Hatcher, ru="Предположительно ещё одна группа", en='We\'re detecting another group.'),

        VoiceLine(1920, Trent, ru="А вот и они!", en='There they are!'),

        VoiceLine(1930, Trent, ru="Влетаю в пояс лавовых астероидов", en='Entering the lava asteroid belt!'),
        VoiceLine(1940, Hatcher, ru="Спеши, Крыг рядом!", en='Go faster, the Krieg is right behind you!'),

        VoiceLine(1950, Trent, ru="Странно, что мой корабль еще не развалился. Летим напролом!", en='It\'s a miracle my ship is still in one piece. We\'re going through!'),

        VoiceLine(2000, Trent, ru="Эй, что за дел+а?", en='Hey, what\'s going on?!'),
        VoiceLine(2010, Neuralnet, ru="Двигатели корабля не работают в пространстве чёрной дыры", en='Ship engines are non-functional this close to the event horizon.'),
        VoiceLine(2020, Trent, ru="И какого хрена мне об этом никто не сказал?", en='And why the hell didn\'t anyone tell me that?!'),

        VoiceLine(2030, Neuralnet, ru="Предлагаю подключить номадское энергоядр+о к питанию корабля", en='Suggest connecting the Nomad power core to the ship\'s systems.'),
        VoiceLine(2040, Trent, ru="Давай попробуем...", en='Let\'s try it...'),
        VoiceLine(2050, Trent, ru="И поскор+ее!", en='And make it quick!'),
        VoiceLine(2060, Trent, ru="Сколько еще?", en='How much longer?!'),
        VoiceLine(2070, Neuralnet, ru="Подключение выполняется", en='Connection in progress.'),
        VoiceLine(2080, Trent, ru="Давай быстрее!", en='Faster!'),
        VoiceLine(2090, Neuralnet, ru="Подключение выполняется", en='Connection in progress.'),
        VoiceLine(2095, Trent, ru="Скорее, мать твою!", en='Hurry up, goddammit!'),
        VoiceLine(2100, Neuralnet, ru="Подключено", en='Connected.'),
        VoiceLine(2110, Trent, ru="Есть, давим на всю гашетку!", en='Yes! Punch it! Full throttle!'),

        VoiceLine(3010, Trent, ru="Класное местечко чтобы помереть. Ну зато мы спасли мир", en='Nice place to die. Well, at least we saved the world.'),
        VoiceLine(3020, Neuralnet, ru="Внимание! Крыг обнаружен!", en='Warning! The Krieg has been detected!'),
        VoiceLine(3030, Trent, ru="В смысле? Он живой? Показывай, где он", en='What do you mean? It\'s alive? Show me where it is!'),

        VoiceLine(3040, Trent, ru="Что он делает", en='What\'s it doing?'),
        VoiceLine(3050, Neuralnet, ru="Он использует энергию чёрной дыр+ы, чтобы восполнить свою энергию", en='It is utilizing the black hole\'s energy to replenish its own power reserves.'),
        VoiceLine(3060, Trent, ru="Да когда уже он этой энергией нажрётся то", en='When is that thing gonna have its fill?!'),

        VoiceLine(3070, Trent, ru="А это что такое?", en='And what\'s that?'),
        VoiceLine(3080, Neuralnet, ru="Крыг использовал энергию чёрной дыр+ы и номадские технологии, чтобы сделать непробиваемый щит и производить кочевников",
								   en='The Krieg has used the black hole\'s energy and Nomad technology to generate an impenetrable shield and produce Nomad units.'),
        VoiceLine(3090, Trent, ru="Что, опять эволюционировал? И что теперь делать?", en='What, it evolved again? So what do we do now?'),
        VoiceLine(3100, Neuralnet, ru="Мы можем усилить энергоядр+о и пушки корабля, собрав энергию чёрной дыр+ы",
								   en='We can enhance the power core and ship\'s weapons by harvesting energy from the black hole.'),
        VoiceLine(3110, Trent, ru="Давай попробуем", en='Let\'s try it!'),

        VoiceLine(3120, Trent, ru="А этой энергии чёрной дыр+ы хватит Крыгу, чтобы высвободиться отсюда?", en='Will this black hole energy be enough for the Krieg to break free from here?'),
        VoiceLine(3130, Neuralnet, ru="Теоретически да", en='Theoretically, yes.'),
        VoiceLine(3140, Trent, ru="Вот чёрт! Кстати, а нам по силам выбраться отсюда?", en='Damn it! By the way, can WE get out of here?'),
        VoiceLine(3150, Neuralnet, ru="Теоретически да", en='Theoretically, yes.'),
        VoiceLine(3160, Trent, ru="А вот это уже звучит гораздо лучше!", en='Now that sounds much better!'),

        VoiceLine(3170, Neuralnet, ru="Мы накопили достаточно сил, чтобы уничтожить щит Крыга. Но сначала нужно уничтожить номадские нар+осты",
								   en='We have accumulated sufficient power to destroy the Krieg\'s shield. But first, the Nomad growths must be eliminated.'),
        VoiceLine(3180, Trent, ru="Снести эти три сиськи? Зачётно! Сейчас сделаем!", en='Take out these three "tits"? Awesome! On my way!'),

        VoiceLine(3190, Trent, ru="Нейросеть, а что будет потом? Есть план на уничтожение Крыга?", en='Neural Net, what\'s the plan after that? Any ideas for destroying the Krieg?'),
        VoiceLine(3200, Neuralnet, ru="Теоретически усиленных пушек вашего корабля хватит, чтобы повредить внутренние системы Крыга",
								   en='Theoretically, your ship\'s enhanced weaponry will be sufficient to damage the Krieg\'s internal systems.'),
        VoiceLine(3210, Neuralnet, ru="Номадское энергоядр+о подключено к устройству доктора Квентейна", en='The Nomad power core has been linked to Professor Quintaine\'s device.'),
        VoiceLine(3220, Neuralnet, ru="С помощью этого излучателя мы можем нанести сокрушительный урон по ослабленному Крыгу",
								   en='Using this emitter, we can deal a crippling blow to the weakened Krieg.'),
        VoiceLine(3230, Trent, ru="Мне нравится этот план", en='I like this plan!'),

        VoiceLine(3240, Neuralnet, ru="Щит Крыга уничтожен. Теперь мы можем проникнуть в его чрево и повредить его внутренние системы",
								   en='The Krieg\'s shield has been destroyed. We can now penetrate its core and damage its internal systems.'),
        VoiceLine(3250, Trent, ru="Я честно говоря уже ничего не боюсь. Влетаем так влетаем. Разнесём эту тварь до конца",
							   en='To be honest, I\'m not afraid of anything anymore. If we\'re going in, we\'re going in. Let\'s finish this thing off for good!'),

        VoiceLine(3260, Neuralnet, ru="Системы Крыга подавлены. Нужно покинуть его чрево", en="The Krieg\'s systems have been compromised. We must vacate its core immediately."),
        VoiceLine(3270, Trent, ru="Поддерживаю", en="I strongly agree!"),

    ]


class Mission13(Msn13, script.StoryMission):
    CUTSCENES = [
        Msn13OsirisCutscene,
        Msn13EnterBlackholeCutscene,
        Msn13KriegDeathCutscene,
        Msn13CsvMagnetCutscene,
    ]
    SPACE_CLASS = Msn13Space
    SYNC_SPACE = True

    MISSION_TITLE = 'Миссия 13. Финал'
