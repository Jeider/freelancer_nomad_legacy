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
				  en="Bad news is coming in from headquarters. The Nomads are starting an invasion in the colonies. The threat turned out much more serious than we thought."),
        VoiceLine(30, King,
                  ru="Мистер Трент и профессор Мандрейк сейчас занимаются улучшением энергоустановки, которую мы отправим в чёрную дыру,, пока еще не поздно",
				  en="Mister Trent and Professor Mandrake are currently improving the power plant we'll send into the black hole, while it's not too late yet."),

        VoiceLine(50, King,
                  ru="Обстановка. Кочевники уже в Омеге-13 и заполнили большую часть астероидных полей в системе.",
				  en="Situation. The Nomads are already in Omega-13 and have filled most of the asteroid fields in the system."),
        VoiceLine(60, King,
                  ru="План операции. Основн+ая боевая группа в виде линкора Осирис и прикрытия совершит атаку на флот номадов, чтобы оттянуть их силы от зоны, примыкающей к чёрной дыре",
				  en="Plan of the operation. The main battle group, the battleship Osiris and its escort, will attack the Nomad fleet to draw their forces away from the zone next to the black hole."),
        VoiceLine(70, King,
                  ru="В это же время мобильная диверсионная группа в составе обоих мистеров Трентов отправится к чёрной дыре через зону со старыми шахтами",
				  en="At the same time, a mobile sabotage group made up of both Mister Trents will head to the black hole through the zone with the old mines."),
        VoiceLine(80, King,
                  ru="Сенсоры отмечают минимальную номадскую активность в этой локации. Путь ожидается относительно безопасным",
				  en="Sensors show minimal Nomad activity in this location. The route is expected to be relatively safe."),
        VoiceLine(90, King, ru="Есть вопросы?", en='Any questions?'),
        VoiceLine(100, Trent, ru="А почему путь через шахты лишь относительно безопасен?", en="And why is the path through the mines only relatively safe?"),
        VoiceLine(110, King,
                  ru="В этой зоне обнаружено скопление номадских зёрен. Они пассивны. Если быть осторожными и не будоражить зёрна, то иных препятствий на пути не замечено.",
				  en="A cluster of Nomad seeds has been found in this zone. They're passive. If you're careful and don't stir up the seeds, no other obstacles have been noted on the way."),
        VoiceLine(120, King, ru="Еще вопросы? Нет? Тогда вылетаем по сигналу. Всем удачи", en="Any more questions? No? Then we launch on the signal. Good luck to everyone."),

        VoiceLine(200, Trent, ru="Ну что,, Ал, гот+ов сегодня спасти мир?", en="So, Al, ready to save the world today?"),
        VoiceLine(210, Alaric, ru="Эй! Я смотрю тебе наконец понравилось работать на спецслужбы!", en="Hey! I see you finally like working for the agencies!"),
        VoiceLine(220, Trent, ru="По крайней мере сейчас я знаю за что воюю", en="At least now I know what I'm fighting for."),
        VoiceLine(230, Alaric, ru="Только давай береги себя,, друг. Сейчас ставки как никогда высоки", en="Just take care of yourself, friend. The stakes have never been this high."),

        VoiceLine(240, Darcy, ru="Да, Трент. Даже самому крутому эксперту по номадам,, как ты, везение сегодня будет не лишним", en="Yes, Trent. Even the toughest Nomad expert, like you, could use some luck today."),
        VoiceLine(250, Trent,
                  ru="Да хватит уже. Мы тут все давно эксперты по дом-кавашам, кочевникам,, крыгам и всему подобному",
				  en="Enough already. All of us here have long been experts on the Dom'Kavash, the Nomads, the Krieg, and all the rest."),
        VoiceLine(260, Alaric,
                  ru="Именно так. Так что давайте воспользуемся нашим экспертным опытом и надерём уже зад этой инопланетной нечисти",
				  en="Exactly. So let's use that expert experience and kick this alien scum's ass already."),
        VoiceLine(270, Darcy, ru="Хочешь показать им,, кто тут главный гуманоид на районе?", en="Want to show them who's the top humanoid around here?"),
        VoiceLine(280, Trent, ru="Удачи,, друзья. А теперь приступим!", en="Good luck, friends. And now let's get to it!"),
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
        VoiceLine(5, Hatcher, ru='Направляемся в Сферу. Трент, веди нас', en='Heading for the Sphere. Trent, lead us.'),
        VoiceLine(10, Trent, ru='Профессор, что-то удал+ось узн+ать из д+анных пол+ученных от Р+окфорда?', en='Professor, did you manage to learn anything from the data we got from Rockford?'),
        VoiceLine(20, Mandrake, ru='Да, удал+ось. И всё достаточно серьёзно. В сфере заточён Кр+ыг.', en='Yes. And it\'s quite serious. A Krieg is sealed inside the Sphere.'),
        VoiceLine(30, Alaric, ru='Круг? В сф+ере?', en='A circle? In the Sphere?'),
        VoiceLine(40, Darcy, ru='Аларик, не вр+емя.', en='Alaric, not the time.'),
        VoiceLine(50, Mandrake, ru='Крыгом я для простот+ы называю корабль расы Крыг, чтобы не плодить с+ущности.',
							   en='For simplicity, I use Krieg to mean a ship of the Krieg race, so we don\'t multiply entities.'),

        VoiceLine(60, Hatcher, ru='Еще одн+а раса?', en='Another race?'),
        VoiceLine(70, Mandrake, ru='Древн+ейший ест+ественный враг Дом Кавашей, создателей кочевников. '
                                         'Когда-то давн+о Дом Каваши практ+ически уничт+ожили Крыгов.',
								en='The ancient natural enemy of the Dom\'Kavash, the creators of the Nomads. Long ago, the Dom\'Kavash nearly wiped out the Krieg.'),
        VoiceLine(80, Mandrake, ru='И тогда Крыги созд+али оружие, спос+обное уничт+ожить Дом Кавашей, '
                                  'но не примен+яли до с+амого конца, так как оно могл+о навред+ить им сам+им.',
								en='And then the Krieg created a weapon capable of destroying the Dom\'Kavash, but they didn\'t use it until the very end, because it could harm them too.'),
        VoiceLine(90, Mandrake, ru='В общем, история др+евняя как мир. И, как всегд+а в таких случаях бывает, когда терять им стало нечего, они его таки применили.',
								en='In short, a story as old as the world. And, as always happens in such cases, when they had nothing left to lose, they did use it.'),
        VoiceLine(100, Mandrake, ru='Дом Каваши смогли его остановить, хоть и очень дорог+ой ценой. Они построили вокруг Крыга сферу, которая непрерывна выкачивала его практически бесконечную энергию.', en='The Dom\'Kavash managed to stop it, though at a very high cost. They built a sphere around the Krieg that continuously drained its practically infinite energy.'),
        VoiceLine(110, Mandrake, ru='И сейчас этой накопленной сферой энергии хватит чтобы уничтожить и саму сферу и Крыга...',
								 en='And now the energy stored by the Sphere is enough to destroy both the Sphere itself and the Krieg...'),

        VoiceLine(120, Trent, ru='И Р+окфорд хочет запустить этот процесс.', en='And Rockford wants to start this process.'),
        VoiceLine(130, Mandrake, ru='Правильно. А что происходит когда за короткий промежуток времени выделяется практически бесконечная энергия?', en='Correct. And what happens when a practically infinite amount of energy is released in a short time?'),
        VoiceLine(140, Hatcher, ru='Большой пипец...', en='We\'re fucked...'),
        VoiceLine(150, Darcy, ru=' Фи, мадам... Но по сути – точно.', en=' Language, madam... But in essence, exactly.'),
        VoiceLine(160, Trent, ru='Попробуем остановить?', en='Shall we try to stop it?'),
        VoiceLine(170, Mandrake, ru='Попытаемся, мистер Трент, попытаемся...', en='We\'ll try, Mister Trent, we\'ll try...'),

        VoiceLine(180, Mandrake, comment='У ядра Сферы', ru='Мистер Трент, нужно уничтожить энергосистемы до того как лазерная установка выстрелит!',
														 en='Mister Trent, the power systems must be destroyed before the laser rig fires!'),
        VoiceLine(190, Trent, ru='Принял.', en='Copy.'),
        VoiceLine(200, Rockford, ru='Останов+итесь, глупцы, что вы делаете? Я уничт+ожу эту зар+азу раз и навсегда!',
								 en='Stop, you fools, what are you doing? I\'ll destroy this plague once and for all!'),
        VoiceLine(210, Hatcher, ru='И половину сектора Сириуса, придурок!',
								en='And half the Sirius sector, you idiot!'),
        VoiceLine(220, Rockford, ru='Вы не сможете меня остановить, сейчас всё свершится!', en='You won\'t be able to stop me. It\'s all about to come to pass now!'),
        VoiceLine(230, Alaric, ru='Слабительного принял что-ли?', en='You take a laxative or what?'),

        VoiceLine(240, Rockford, ru="Идиоты, вы сделаете только хуже!", en="Idiots, you'll only make it worse!"),
        VoiceLine(250, Alaric, ru="Поздно пить Боржоми, твоим планам настал конец!", en="Too late for that. Your plans are finished!"),

        VoiceLine(260, Darcy, ru="Лазер ударил по Крыгу! Мы не успели!", en="The laser hit the Krieg! We didn't make it in time!", cinematic=True),
        VoiceLine(270, Alaric, ru="Но вроде мы спасены? Ничего не взорвалось? Всё хорошо ведь, да?", en="But it seems we're saved? Nothing exploded? Everything's fine, right?", cinematic=True),

        VoiceLine(280, Darcy, ru="Что происходит?", en="What\'s happening?", cinematic=True),
        VoiceLine(290, King, ru="Всем срочно отойти на безопасную дистанцию!", en="Everyone, fall back to a safe distance, now!", cinematic=True),

        VoiceLine(300, Alaric, ru="Ёлки-п+алки...", en="Oh, man...", cinematic=True),
        VoiceLine(310, Darcy, ru="Оно жив+ое!", en="It's alive!", cinematic=True),
        VoiceLine(320, Hatcher, ru="Всем приготовиться! Мы не знаем на что способна эта тварь!", en="Everyone, get ready! We don't know what this beast is capable of!", cinematic=True),

        VoiceLine(323, Hatcher, ru="Миссури под прицелом, выполнить манёвр уклонения!", en="Missouri is in the sights, execute an evasive maneuver!", cinematic=True),
        VoiceLine(326, Alaric, ru="Слишком поздно!", en="Too late!", cinematic=True),

        VoiceLine(330, Hatcher, ru="Мы потеряли Миссури нахер!", en="We lost the fucking Missouri!"),
        VoiceLine(340, King, ru="Вышлите спасательные судна с Осириса, срочно!", en="Send rescue ships from the Osiris, now!"),

        VoiceLine(350, Mandrake, ru="Генерал Кинг, Крыг еще слаб. Мы можем нейтрализовать его пока он еще не вошел в силу. Нужно уничтожить генераторы на его корпусе",
								 en="General King, the Krieg is still weak. We can neutralize it before it comes into its strength. We need to destroy the generators on its hull."),
        VoiceLine(360, Trent, ru="Эй, вы там совсем башкой поехали с такими идеями? Я к этой штуковине не полезу!",
							  en="Hey, have you all completely lost your minds with ideas like that? I'm not going near that thing!"),
        VoiceLine(370, King, ru="Если мы это не сделаем, то Крыг зарядится и перебьет нас как куропаток. Выполняйте, это приказ!",
							 en="If we don't do this, the Krieg will charge up and gun us down like partridges. Carry it out, that's an order!"),

        VoiceLine(380, Hatcher, ru='Внимание! Крыг готовится к новому удару! Он целится в Осирис!', en="Attention! The Krieg is preparing a new strike! It's aiming at the Osiris!"),
        VoiceLine(390, King, ru='Мостик, срочно усильте щиты в зоне вероятного попадания!', en="Bridge, reinforce the shields in the likely impact zone, now!"),

        VoiceLine(400, Hatcher, ru='Осирис получил попадание! Генератор щита выведен из строя, второе такое попадание он не выдержит!',
								en="The Osiris took a hit! The shield generator is out of action. It won't survive a second hit like that!"),
        VoiceLine(410, King, ru='Команда, срочно уничтожьте генераторы! Реактор Осириса поврежден, мы не сможем быстро выйти из зоны поражения Крыга!',
							 en='Team, destroy the generators, now! The Osiris reactor is damaged. We can\'t quickly get out of the Krieg\'s kill zone!'),

        VoiceLine(420, Hatcher, ru='Фиксирую новый заряд энергии!', en='I\'m reading a new energy charge!'),
        VoiceLine(430, King, ru='Шевел+итесь!', en='Move it!'),

        VoiceLine(440, Hatcher, ru='Нет! Осирис уничтожен!', en="No! The Osiris is destroyed!"),

        VoiceLine(450, Hatcher, ru='Есть, генераторы Крыга уничтожены! Он закрывается!', en='Yes, the Krieg\'s generators are destroyed! It\'s closing up!'),
        VoiceLine(460, Alaric, ru='А теперь что с ним?', en='And now what\'s with it?'),

        VoiceLine(470, Mandrake, ru='Мы лишили Крыга естественного притока энергии, теперь он пытается восполнить её из Сферы',
								 en='We\'ve cut the Krieg off from its natural energy inflow. Now it\'s trying to replenish that from the Sphere.'),

        VoiceLine(480, Mandrake, ru='(приказ!) Мистер Трент, нужно дестабилизировать работу энергосистемы Сферы!', en='Mister Trent, we need to destabilize the Sphere\'s power system!'),
        VoiceLine(490, Mandrake, ru='Вы должн+ы залезть в канализационные каналы и нарушить целостность энергосетей!',
								 en='You have to get into the sewer channels and break the power networks!'),

        VoiceLine(500, Trent, ru='Выдвигаюсь!', en='Moving out!'),

        VoiceLine(510, King, ru='Реактор Осириса вошел в норму. Приказ выйти из Сферы. Хетчер, прикрывайте Трента и следите за Крыгом',
							 en='The Osiris reactor is back to normal. Order to leave the Sphere. Hatcher, cover Trent and watch the Krieg.'),
        VoiceLine(520, Hatcher, ru='Вас поняли, генерал Кинг', en='Understood, General King.'),

        VoiceLine(530, Trent, ru='При виде этих дверей у самог+о сжимается...', en='At the sight of these doors, even I\'m clenching...'),

        VoiceLine(540, Hatcher, ru='Сфера обесточена. Молодец Трент, теперь давай выбирайся из этих катакомб',
								en='The Sphere is powered down. Well done, Trent, now get out of these catacombs.'),

        VoiceLine(550, Alaric, ru='И что теперь? Что нам делать с Крыгом', en='And what now? What do we do with the Krieg?'),
        VoiceLine(560, Mandrake, ru='(не успеть сказать как...)У меня есть одна идея, только нам нужно...', en='I have one idea, only we need...'),

        VoiceLine(570, Darcy, comment='Появилися корабли инопланетян!', ru='Корабли Кочевников! Как они тут оказались?!', en='Nomad ships! How did they end up here?!'),
        VoiceLine(580, Mandrake, ru='Крыг их подчинил!', en='The Krieg has taken control of them!'),
        VoiceLine(590, Alaric, ru='Как?!', en='How?!'),
        VoiceLine(600, Mandrake, ru='(приказ, все на панике!) Полностью! Мистер Трент, нужно срочно вынуть номадское энергоядр+о из установки Р+окфорда!',
								 en='Completely! Mister Trent, we urgently need to pull the Nomad power core out of Rockford\'s rig!'),
        VoiceLine(610, Trent, ru='Принято, сейчас сделаем', en='Copy, we\'ll do it now.'),

        VoiceLine(620, Trent, ru='Генератор у меня, уходим отсюда!', en='I\'ve got the generator, let\'s get out of here!'),
        VoiceLine(630, Hatcher, ru='Чёрт, кочевники перегородили проход, мы заблокированы!', en='Damn, the Nomads have blocked the passage. We\'re trapped!'),

        VoiceLine(640, EdisonTrent, ru='Не падать духом! Вот выход, летите за мной!', en='Don\'t lose heart! Here\'s a way out, fly after me!', cinematic=True),
        VoiceLine(650, Hatcher, ru='Срочно улетаем через этот проход! Живо!', en='Out through this passage, now! Move!'),

        VoiceLine(660, Darcy, ru='Это +Эдисон Трент? Собственной персоной?', en='Is that Edison Trent? In the flesh?'),
        VoiceLine(670, Hatcher, ru='Легенда возвращается как никогда вовремя', en='The legend returns, and never so on time.'),  # Alaric?

        VoiceLine(680, Trent, ru='Что дальше, профессор?', en='What next, Professor?'),
        VoiceLine(690, Mandrake, ru='Насколько я понимаю, уничтожить ЭТО сможет только гравитация черной дыры.',
								 en='As far as I understand, only a black hole\'s gravity can destroy THIS.'),
        VoiceLine(700, Hatcher, ru='Ближайшая в омеге-13', en='The nearest one is in Omega-13.'),
        VoiceLine(710, Alaric, ru='И как же мы заставим ЭТО переместиться в омегу-13?', en='And how are we going to make THIS move to Omega-13?'),
        VoiceLine(720, EdisonTrent, ru='Достаточно переместиться туда самим', en='It\'s enough if we go there ourselves.'),
        VoiceLine(730, EdisonTrent, ru='Я правильно понял, профессор, зачем вы попросили моего тезку собрать энергоэлементы кочевников?',
									en='Professor, did I understand right why you asked my namesake to collect the Nomads\' energy elements?'),
        VoiceLine(740, Mandrake, ru='Всё верно. По моим рассчётам энергоядр+о способно издавать сигнатуры Дом Кавашей, на уничтожение которых запрограммирован Крыг',
								 en='That\'s correct. By my calculations, the power core can emit Dom\'Kavash signatures, which the Krieg is programmed to destroy.'),
        VoiceLine(750, Mandrake, ru='Мне лишь неизвестно каким образом это сделать', en='I simply don\'t know how to do it.'),
        VoiceLine(760, EdisonTrent, ru='Не проблема. На моём корабле есть старая установка профессора Квентейна, которой мы победили кочевников в прошлый раз. Нужно лишь внести пару доработок', en='No problem. My ship has Professor Quintaine\'s old device, the one we beat the Nomads with last time. It just needs a couple of modifications.'),
        VoiceLine(770, Mandrake, comment='В сюжете два "Трент", первый это персонаж первой части, опытный чувак, поэтому Мандрейк обращается к нему с большим уважением', ru='Мистер Трент, вы просто восхитительны!', en='Mister Trent, you are simply magnificent!'),
        VoiceLine(780, King, ru='Это звучит как хороший план. Трент, рад тебя слышать. Садитесь на Осирис. Мы доставим вас до Омеги-13',
							 en='That sounds like a good plan. Trent, glad to hear you. Dock with the Osiris. We\'ll take you to Omega-13.'),

        VoiceLine(1000, King, ru="Сенсоры подтверждают скопление номадских зёрен в этом секторе", en='Sensors confirm a cluster of Nomad seeds in this sector.'),
        VoiceLine(1010, EdisonTrent, ru="А истребители, линкоры? Есть активность?", en='And fighters, battleships? Any activity?'),
        VoiceLine(1020, King, ru="Ответ отрицательный. Путь относительно спокоен. Вы справитесь. Удачи", en='Negative. The path is relatively calm. You\'ll manage. Good luck.'),

        VoiceLine(1030, EdisonTrent, ru="Тёзка, держи путь к тому большому астероиду. Астероидное поле не однородно, а через тот большой астероид мы минуем зону радиации",
									 en='Namesake, hold course for that large asteroid. The asteroid field isn\'t uniform, and through that big asteroid we\'ll bypass the radiation zone.'),
        VoiceLine(1040, EdisonTrent, ru="Только давай не будем будоражить зёрна. Я не хочу нарваться на неприятности", en='Just let\'s not stir up the seeds. I don\'t want to run into trouble.'),

        VoiceLine(1050, Trent, ru="А как ты хочешь забросить маяк в чёрную дыру?", en='And how do you want to throw the beacon into the black hole?'),
        VoiceLine(1060, EdisonTrent, ru="Я установил на свой корабль специальную катапульту.", en='I installed a special catapult on my ship.'),
        VoiceLine(1070, EdisonTrent, ru="Так что не беспокойся. Я запущу маяк с безопасного расстояния", en='So don\'t worry. I\'ll launch the beacon from a safe distance.'),

        VoiceLine(1080, EdisonTrent, ru="Осторожней с этими зёрнами...", en='Careful with these seeds...'),

        VoiceLine(1090, EdisonTrent, ru="Зерно активировалось!", en='A seed has activated!'),
        VoiceLine(1100, EdisonTrent, ru="Да что такое! Тёзка, у нас нет времени!", en='What is this! Namesake, we have no time!'),
        VoiceLine(1110, EdisonTrent, ru="Времени мало, мы должн+ы спеш+ить!", en='Time is short, we have to hurry!'),

        VoiceLine(1120, EdisonTrent, ru="Нам нужно пробить проход в этом астероиде, чтобы пролететь через него", en='We need to blast a passage through this asteroid so we can fly through it.'),
        VoiceLine(1130, EdisonTrent, ru="Отлично, залетаем в туннель!", en='Excellent, into the tunnel!'),
        VoiceLine(1140, EdisonTrent, ru="Еще одно препятствие, пробей его!", en='Another obstacle, blast through it!'),

        VoiceLine(1145, Trent, ru="А это еще что за хрень? Придется протискиваться", en='And what the hell is this crap? We\'ll have to squeeze through.'),

        VoiceLine(1150, Trent, ru="Эй, что за херн+я?!", en='Hey, what the fuck is this?!'),

        VoiceLine(1160, Trent, ru="Мы вообще где?", en='Where are we, even?'),
        VoiceLine(1170, EdisonTrent, ru="Крыг усилил зерно, оно образовало кокон и заблокировало нас", en='The Krieg strengthened the seed. It formed a cocoon and blocked us in.'),
        VoiceLine(1180, EdisonTrent, ru="Нам нужно снест+и зерно как можно скорее, пока оно не наплодило истребители кочевников!",
									 en='We need to take that seed down as soon as possible, before it breeds Nomad fighters!'),

        VoiceLine(1200, Trent, ru='Фух, вылетели', en='Phew, we\'re out.'),
        VoiceLine(1210, EdisonTrent, ru="Да, нам повезло...", en='Yes, we got lucky...'),
        VoiceLine(1220, EdisonTrent, ru="Осирис, это Альфа. У нас неприятности, Крыг перестроил зёрна. Теперь они чрезвычайно опасны",
									 en='Osiris, this is Alpha. We\'ve got trouble. The Krieg has reworked the seeds. Now they\'re extremely dangerous.'),
        VoiceLine(1230, EdisonTrent, ru='Будьте осторожны, эти зёрна светятся красным светом и умеют образовывать коконы',
									 en='Be careful. These seeds glow red and can form cocoons.'),
        VoiceLine(1240, King, ru='Вас поняли, Альфа. Вы сами в порядке?', en='Understood, Alpha. Are you yourselves all right?'),
        VoiceLine(1250, EdisonTrent, ru='Да, всё идёт по плану', en='Yes, everything\'s going to plan.'),

        VoiceLine(1260, EdisonTrent, ru='Тёзка, надо сбить это препятствие', en='Namesake, we need to take out this obstacle.'),
        VoiceLine(1270, EdisonTrent, ru='Еще одно препятствие', en='Another obstacle.'),
        VoiceLine(1280, EdisonTrent, ru='С+удя по сенсорам дальше препятствий пока нет, можем пролететь эту секцию на кру+изе',
									 en='Judging by the sensors, no obstacles ahead for now. We can fly this section at cruise.'),

        VoiceLine(1290, EdisonTrent, ru='Препятствие спереди', en='Obstacle ahead.'),
        VoiceLine(1300, Trent, ru='Может лучше сюда?', en='Maybe this way is better?'),
        VoiceLine(1310, EdisonTrent, ru='Да, действительно. Летим в этот проход', en='Yes, really. Let\'s fly into this passage.'),

        VoiceLine(1320, EdisonTrent, ru='Чёрт, зерно! Стой!', en='Damn, a seed! Stop!'),
        VoiceLine(1330, EdisonTrent, ru='Есть другой проход. Давай попробуем эту дорогу', en='There\'s another passage. Let\'s try this path.'),
        VoiceLine(1340, Trent, ru='Кажется чисто', en='Seems clear.'),

        VoiceLine(1350, EdisonTrent, ru='Ещё препятствие. Мы почти пролет+ели', en='Another obstacle. We\'ve almost flown through.'),
        VoiceLine(1360, EdisonTrent, ru='Меня смущ+ает этот кр+асный свет. Летим остор+ожно...', en='This red light unsettles me. Let\'s fly carefully...'),
        VoiceLine(1370, EdisonTrent, ru='Мы зам+ечены! Чёрт!', en='We\'ve been spotted! Damn!'),

        VoiceLine(1380, EdisonTrent, ru='Попались, мы опять в коконе', en='Caught. We\'re in a cocoon again.'),

        VoiceLine(1480, Trent, ru="Эй, что это за истребители?", en='Hey, what kind of fighters are these?'),
        VoiceLine(1490, EdisonTrent, ru="Тяжелые истребители номадов. Они эволюционируют... дел+а плохи", en='Heavy Nomad fighters. They\'re evolving... things are bad.'),
        VoiceLine(1500, EdisonTrent, ru="Зерно тоже стало мощнее... Тёзка, надо ослабить зерно. Раскидай номадские истребители. Тогда зерно ослабнет и мы его разнесём",
									 en='The seed got stronger too... Namesake, we need to weaken the seed. Scatter the Nomad fighters. Then the seed will weaken and we\'ll smash it.'),
        VoiceLine(1510, Trent, ru="Сейчас сделаем", en='We\'ll do it now.'),

        VoiceLine(1520, EdisonTrent, ru="Зерно ослабло, его можно бить. Давай быстрее, времени не в обрез", en='The seed has weakened, we can hit it. Come on, faster, we don\'t have time to spare.'),

        VoiceLine(1530, Trent, ru="Есть! Вышли!", en='Yes! We\'re out!'),
        VoiceLine(1540, EdisonTrent, ru="Вот чёрт... кажется сегодня не мой день.", en='Oh, damn... seems today isn\'t my day.', cinematic=True),
        VoiceLine(1550, Trent, ru="Что стряслось?", en='What happened?', cinematic=True),
        VoiceLine(1560, EdisonTrent, ru="Радиация зерна... разрушила мой корабль... А как ты смог её перенести?",
									 en='The seed\'s radiation... destroyed my ship... And how did you withstand it?', cinematic=True),
        VoiceLine(1570, Trent, ru="Я не знаю... и что теперь делать", en='I don\'t know... and what do we do now.', cinematic=True),
        VoiceLine(1580, EdisonTrent, ru="Так, знаешь... я передам маяк тебе. Доставь его сам, один",
									 en='Okay, listen... I\'ll transfer the beacon to you. Deliver it yourself, alone.', cinematic=True),
        VoiceLine(1590, Trent, ru="Но на моём корабле нет катапульты!", en='But my ship doesn\'t have a catapult!', cinematic=True),
        VoiceLine(1600, EdisonTrent, ru="Знаю, знаю... чёрт...", en='I know, I know... damn...', cinematic=True),

        VoiceLine(1610, Mandrake, ru="(Вниманиеее!) Всем внимание! Крыг замечен в системе!", en='Everyone, attention! The Krieg has been spotted in the system!', cinematic=True),

        VoiceLine(1620, Trent, ru="Тёзка, давай мне маяк. Деваться некуда, дотащу сам", en='Namesake, give me the beacon. No choice, I\'ll haul it myself.', cinematic=True),
        VoiceLine(1630, EdisonTrent, ru="Да, сейчас", en='Yes, now.'),

        VoiceLine(1640, Trent, ru="Забрал, а ты тут справишься?", en='Got it. Will you manage here?'),
        VoiceLine(1650, EdisonTrent, ru="Да, всё будет хорошо. Скорее лети. Удачи там, тёзка", en='Yes, it\'ll be fine. Fly, hurry. Good luck out there, namesake.'),
        VoiceLine(1660, Trent, ru="Тебе тоже...", en='You too...'),

        VoiceLine(1800, Hatcher, ru="Альфа, Крыг стремительно приближается к чёрной дыре! Тороп+итесь, видимо он хочет перегородить вам путь!",
								 en='Alpha, the Krieg is closing fast on the black hole! Hurry, it seems it wants to block your path!'),
        VoiceLine(1810, Trent, ru="Я уже здесь, направляюсь к дыре", en='I\'m already here, heading for the hole.'),
        VoiceLine(1820, Hatcher, ru="Трент? А гдеее... второй Трент?", en='Trent? And wheeere... is the second Trent?'),
        VoiceLine(1830, Trent, ru="С ним всё хорошо, он решил отдохнуть. Маяк у меня", en='He\'s fine, he decided to rest. I\'ve got the beacon.'),
        VoiceLine(1840, Hatcher, ru="Но ведь...", en='But...'),
        VoiceLine(1850, Trent, ru="Плевать, веди меня к дыре", en='Whatever, lead me to the hole.'),
        VoiceLine(1860, Hatcher, ru="Ладно. Это астероидное поле ведет прям к дыре, препятствий быть не должно",
								       en='Alright. This asteroid field leads straight to the hole. There shouldn\'t be any obstacles.'),

        VoiceLine(1870, Trent, ru="Появились ном+адские корабли!", en='Nomad ships have shown up!'),
        VoiceLine(1880, Hatcher, ru="Трент, уходи в сторону, у них перехватывающие ракеты!", en='Trent, break away, they\'ve got interceptor missiles!'),

        VoiceLine(1890, Hatcher, ru="Еще кочевники!", en='More Nomads!'),
        VoiceLine(1900, Trent, ru="Сколько их тут еще?", en='How many more of them are there?'),
        VoiceLine(1910, Hatcher, ru="Предположительно ещё одна группа", en='Presumably one more group.'),

        VoiceLine(1920, Trent, ru="А вот и они!", en='And there they are!'),

        VoiceLine(1930, Trent, ru="Влетаю в пояс лавовых астероидов", en='Entering the lava asteroid belt.'),
        VoiceLine(1940, Hatcher, ru="Спеши, Крыг рядом!", en='Hurry, the Krieg is close!'),

        VoiceLine(1950, Trent, ru="Странно, что мой корабль еще не развалился. Летим напролом!", en='Strange my ship hasn\'t fallen apart yet. We\'re going straight through!'),

        VoiceLine(2000, Trent, ru="Эй, что за дел+а?", en='Hey, what\'s going on?', cinematic=True),
        VoiceLine(2010, Neuralnet, ru="Двигатели корабля не работают в пространстве чёрной дыры", en='Ship engines do not function in black hole space.', cinematic=True),
        VoiceLine(2020, Trent, ru="И какого хрена мне об этом никто не сказал?", en='And why the hell did nobody tell me about this?', cinematic=True),

        VoiceLine(2030, Neuralnet, ru="Предлагаю подключить номадское энергоядр+о к питанию корабля", en='Suggest connecting the Nomad power core to the ship\'s power supply.', cinematic=True),
        VoiceLine(2040, Trent, ru="Давай попробуем...", en='Let\'s try...', cinematic=True),
        VoiceLine(2050, Trent, ru="И поскор+ее!", en='And make it quick!', cinematic=True),
        VoiceLine(2060, Trent, ru="Сколько еще?", en='How much longer?', cinematic=True),
        VoiceLine(2070, Neuralnet, ru="Подключение выполняется", en='Connection in progress.', cinematic=True),
        VoiceLine(2080, Trent, ru="Давай быстрее!", en='Come on, faster!', cinematic=True),
        VoiceLine(2090, Neuralnet, ru="Подключение выполняется", en='Connection in progress.', cinematic=True),
        VoiceLine(2095, Trent, ru="Скорее, мать твою!", en='Faster, damn you!', cinematic=True),
        VoiceLine(2100, Neuralnet, ru="Подключено", en='Connected.', cinematic=True),
        VoiceLine(2110, Trent, ru="Есть, давим на всю гашетку!", en='Yes, throttle to the floor!'),

        VoiceLine(3010, Trent, ru="Класное местечко чтобы помереть. Ну зато мы спасли мир", en='Nice little spot to die. Well, at least we saved the world.'),
        VoiceLine(3020, Neuralnet, ru="Внимание! Крыг обнаружен!", en='Attention! Krieg detected!'),
        VoiceLine(3030, Trent, ru="В смысле? Он живой? Показывай, где он", en='What do you mean? It\'s alive? Show me where it is.'),

        VoiceLine(3040, Trent, ru="Что он делает", en='What\'s it doing.'),
        VoiceLine(3050, Neuralnet, ru="Он использует энергию чёрной дыр+ы, чтобы восполнить свою энергию", en='It is using the black hole\'s energy to replenish its own energy.'),
        VoiceLine(3060, Trent, ru="Да когда уже он этой энергией нажрётся то", en='So when is it gonna stuff itself on that energy already.'),

        VoiceLine(3070, Trent, ru="А это что такое?", en='And what\'s this?'),
        VoiceLine(3080, Neuralnet, ru="Крыг использовал энергию чёрной дыр+ы и номадские технологии, чтобы сделать непробиваемый щит и производить кочевников",
								   en='The Krieg used the black hole\'s energy and Nomad technology to make an impenetrable shield and produce Nomads.'),
        VoiceLine(3090, Trent, ru="Что, опять эволюционировал? И что теперь делать?", en='What, it evolved again? And what do we do now?'),
        VoiceLine(3100, Neuralnet, ru="Мы можем усилить энергоядр+о и пушки корабля, собрав энергию чёрной дыр+ы",
								   en='We can boost the power core and the ship\'s guns by gathering black hole energy.'),
        VoiceLine(3110, Trent, ru="Давай попробуем", en='Let\'s try.'),

        VoiceLine(3120, Trent, ru="А этой энергии чёрной дыр+ы хватит Крыгу, чтобы высвободиться отсюда?", en='And will this black hole energy be enough for the Krieg to break free from here?'),
        VoiceLine(3130, Neuralnet, ru="Теоретически да", en='Theoretically, yes.'),
        VoiceLine(3140, Trent, ru="Вот чёрт! Кстати, а нам по силам выбраться отсюда?", en='Damn! By the way, are we able to get out of here?'),
        VoiceLine(3150, Neuralnet, ru="Теоретически да", en='Theoretically, yes.'),
        VoiceLine(3160, Trent, ru="А вот это уже звучит гораздо лучше!", en='Now that sounds much better!'),

        VoiceLine(3170, Neuralnet, ru="Мы накопили достаточно сил, чтобы уничтожить щит Крыга. Но сначала нужно уничтожить номадские нар+осты",
								   en='We\'ve gathered enough power to destroy the Krieg\'s shield. But first we need to destroy the Nomad growths.'),
        VoiceLine(3180, Trent, ru="Снести эти три сиськи? Зачётно! Сейчас сделаем!", en='Shoot off these three tits? Nice! We\'ll do it now!'),

        VoiceLine(3190, Trent, ru="Нейросеть, а что будет потом? Есть план на уничтожение Крыга?", en='Neural net, and what then? Is there a plan to destroy the Krieg?'),
        VoiceLine(3200, Neuralnet, ru="Теоретически усиленных пушек вашего корабля хватит, чтобы повредить внутренние системы Крыга",
								   en='Theoretically, your ship\'s boosted guns will be enough to damage the Krieg\'s internal systems.'),
        VoiceLine(3210, Neuralnet, ru="Номадское энергоядр+о подключено к устройству доктора Квентейна", en='The Nomad power core is connected to Doctor Quintaine\'s device.'),
        VoiceLine(3220, Neuralnet, ru="С помощью этого излучателя мы можем нанести сокрушительный урон по ослабленному Крыгу",
								   en='With this emitter we can deal crushing damage to the weakened Krieg.'),
        VoiceLine(3230, Trent, ru="Мне нравится этот план", en='I like this plan.'),

        VoiceLine(3240, Neuralnet, ru="Щит Крыга уничтожен. Теперь мы можем проникнуть в его чрево и повредить его внутренние системы",
								   en='The Krieg\'s shield is destroyed. Now we can get into its belly and damage its internal systems.'),
        VoiceLine(3250, Trent, ru="Я честно говоря уже ничего не боюсь. Влетаем так влетаем. Разнесём эту тварь до конца",
							   en='Honestly, I\'m not afraid of anything anymore. In we go, then. We\'ll smash this beast completely.'),

        VoiceLine(3260, Neuralnet, ru="Системы Крыга подавлены. Нужно покинуть его чрево", en="The Krieg's systems are suppressed. We need to leave its belly."),
        VoiceLine(3270, Trent, ru="Поддерживаю", en="Agreed."),

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
    SYNC_SUBS = True

    MISSION_TITLE = 'Миссия 13. Финал'