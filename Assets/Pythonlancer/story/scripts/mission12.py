from story import script
from audio.sound import VoiceLine
from story.actors import (Trent, Darcy, King, Hatcher, Alaric, Mandrake, Kruger, FortBush, Omaha,
                          PromDread1, PromDread2)
from story.cutscenes.story_scenes import m12_sprague, m12_captured


class Msn12(object):
    MISSION_INDEX = 12


class Msn12SpragueCutscene(Msn12, script.CutsceneProps):
    ALIAS = 'sprague'
    TITLE = 'Исследовательская зона планеты Спрага'
    THORN_CLASS = m12_sprague.Msn12SpragueScene
    THORN_DECISION_CLASS = m12_sprague.Msn12SpragueDecisionScene
    DESCRIPTION = 'Все в сборе, Трент сразу начинает за правду матку'
    VOICE_LINES = [

        VoiceLine(10, Hatcher,
                  ru='(стоит у стенки в томном ожидании) Итак,, Трент, надеюсь ты позвал меня по важному делу',
                  en='Alright, Trent. I hope you called me here for an important reason.'),
        VoiceLine(20, Trent, ru='Чрезвычайно важному делу', en='An extremely important one.'),
        VoiceLine(30, Hatcher,
                  ru='Тогда будь добр расскажи,, в чём суть. А то я заметила твои выкрутасы в системе Сириус. Теперь у меня снова есть полномочия арестовать тебя',
                  en='Then be so kind as to explain what this is about. Because I\'ve noticed your little stunt in the Sirius system. I once again have the authority to arrest you.'),
        VoiceLine(40, Alaric,
                  ru='(Распахивается дверь, приходят Аларик и Дерси) Эй, Трент! Что случилось? Почему так срочно?',
                  en='Hey, Trent! What\'s going on? Why the rush?'),
        VoiceLine(50, Trent,
                  ru='Рокфорд заполучил артефакты, направляется к Сфере и хочет уничтожить человечество. Мы должн+ы его остановить!',
                  en='Rockford has the artifacts, he\'s heading for the Sphere, and he intends to wipe out humanity.We have to stop him!'),

        VoiceLine(60, Hatcher, ru='Что ты несёшь? Как он это сможет сделать? Подорвёт Сферу динамитом? Трент, придумай что-нибудь более интересное.', en='What kind of nonsense is that? How is he going to do that? Blow up the Sphere with dynamite? Trent, come up with something more interesting.'),

        VoiceLine(70, Trent, ru='Рокфорд продумал эту операцию когда работал на единый Орден. Здесь точно должн+ы быть какие-то документы, планы про это. Хоть что-нибудь', en='Rockford planned this operation back when he worked for the unified Order. There must be documents, plans about it here. Anything!'),
        VoiceLine(80, Hatcher, ru='Ничего такого не может быть. СБА никогда не будет заниматься этой чепухой!', en='Nothing like that could exist. The ASF would never dabble in such nonsense!'),

        VoiceLine(90, Mandrake, ru='Вообще-то...', en='Actually...'),
        VoiceLine(100, Hatcher, ru='Профессор? Вы что-то про это знаете?', en='Professor? Do you know something about this?'),

        VoiceLine(110, Mandrake, ru='Возможно. Я видел подобные документы в архиве, но они засекречены.', en='Perhaps. I\'ve seen similar documents in the archive, but they are classified.'),
        VoiceLine(120, Mandrake, ru='Требуется максимальный уровень доступа, который есть только у двух человек - у Кинга, и еще у кого-то, о ком я не знаю.', en='They require the highest level of access, which only two people have — King, and someone else I\'m not aware of.'),

        VoiceLine(130, Trent, ru='Полагаю,, этого ключа доступа должно быть достаточно. (прикладывает карту доступа)', en='I believe this access key should be sufficient.'),
        VoiceLine(140, Darcy, ru='Нихрен+а-ж себе.', en='Well, I\'ll be damned!'),
        VoiceLine(150, Alaric, ru='Я о тебе чего-то не знаю?', en='Is there something I don\'t know about you?'),

        VoiceLine(160, Hatcher, ru='Ладно,, Трент. Допустим,, я тебе верю. Но как ты собираешься проникнуть в Сферу? У тебя же нет ключа от неё', en='Alright, Trent. Suppose I believe you. But how do you plan to get inside the Sphere? You don\'t have the key for it!'),
        VoiceLine(170, Trent, ru='(Достает ключ) Ключ от Сферы у меня тоже есть', en='I have the key to the Sphere as well.'),
        VoiceLine(180, Darcy, ru='Трент, колись, на кого тебя подменили?', en='Trent, confess, who replaced you?!'),

        VoiceLine(190, Alaric, comment='Тревога!', ru='Это еще что такое?', en='What\'s that now?'),

        VoiceLine(250, Hatcher, comment='Хетчер подходит к столу с коммуникатором. На её лице ужас',
        ru='Штаб СБА атакован. Всем силам СБА приказано прибыть в штаб.', en='ASF Headquarters is under attack. All ASF forces are ordered to report to HQ'),
        VoiceLine(260, Hatcher, ru='Силы противника превосходят... Да кто же это?', en='Enemy forces are superior... Who the hell is it?'),

        VoiceLine(270, Trent, ru='(Ужас) Чёрт... Ким же говорил про спецоперацию... Твою мать... Они на это решились.', en='Fuuuck... Kim mentioned a special operation... Goddammit... They actually went through with it.'),
        VoiceLine(280, Hatcher, ru='Кто решился? На что? Ты о чём вообще?', en='Who did? With what? What are you talking about?'),

        VoiceLine(290, Trent, ru='Орден решил показать кто тут главный и устранить прямого конкурента. Орден атаковал СБА, понимаешь?', en='The Order decided to show who\'s in charge and eliminate their direct competitor.The Order is attacking the ASF, don\'t you get it?'),
        VoiceLine(300, Trent, ru='Чтобы полностью уничтожить СБА и стать главной силой в секторе Сириуса. И в самый неподходящий момент.', en='To completely destroy the ASF and become the sole power in the Sirius sector. And they\'re doing it at the worst possible time.'),
        VoiceLine(310, Trent, ru='Н+ахрен. Не нужны нам никакие кочевники, мы сами друг другу глотку перегрызем. Просто ради удовлетворения амбиций.', en='Damn it! Who needs the Nomads when we\'re tearing each other\'s throats out ourselves! All for the sake of their ambition!'),

        VoiceLine(320, Hatcher, ru='(Осознав, выдохнув и решившись) Я им этого не позволю! Вылетаем!', en='I won\'t let them get away with this! Let\'s move!'),
    ]


class Msn12CapturedCutscene(Msn12, script.CutsceneProps):
    ALIAS = 'captured'
    TITLE = 'Бар линкора Осирис'
    THORN_CLASS = m12_captured.Msn12CapturedScene
    THORN_DECISION_CLASS = m12_captured.Msn12CapturedDecisionScene
    THORN_ACCEPT_CLASS = m12_captured.Msn12CapturedAcceptScene
    DESCRIPTION = 'Ямамото пленён. Теперь нужно убедить Кинга заняться Рокфордом'
    VOICE_LINES = [
        VoiceLine(10, King, ru='Что с Ямамото?', en='What\'s the status on Yamamoto?'),
        VoiceLine(20, Hatcher, ru='Ведем дознание. Не хотите ли поприсутствовать?', en='We\'re conducting the interrogation. Would you like to be present?'),
        VoiceLine(30, King, ru='Ооо,, да! Этот безбашенный самурай превзошел самог+о себя.',
                  en='Oh, yes! That reckless samurai has outdone himself.'),
        VoiceLine(40, King,
                  ru='С удовольствием посмотрел бы что творится у него в мозгах, а лучше заспиртовал бы их в банке.',
                  en='I\'d love to see what\'s going on in his head, or better yet, pickle his brains in a jar.'),

        VoiceLine(50, Trent, ru='Генерал Кинг, нужно срочно остановить Рокфорда!',
                  en='General King, we need to stop Rockford, now!'),
        VoiceLine(60, King, ru='Дался вам этот Рокфорд... Если он где-нибудь набедокурит, наши силы всё подчистят.',
                  en='You\'re so obsessed with this Rockford... If he makes trouble somewhere, our forces will clean it up.'),
        VoiceLine(70, King, ru='А его загонят,, как зайца,, далеко в приграничье. Сам сдаваться придет, вот увидите.', en='We\'ll run him down like a rabbit in the Border Worlds.He\'ll surrender on his own, you\'ll see.'),
        VoiceLine(80, Hatcher, ru='Генерал Кинг, вызов от профессора Мандрейка.', en='General King, an incoming call from Professor Mandrake.'),
        VoiceLine(90, King, ru='Выведите на главный экран.', en='Put it on the main screen.'),

        VoiceLine(100, Mandrake, ru='Генерал Кинг, мистер Трент, мисс Хетчер. О, да я смотрю,, все в сборе.', en='General King, Mister Trent, Miss Hatcher. Oh, I see everyone is here. '),
        VoiceLine(110, Mandrake, ru='Я ознакомился с так называемым планом Рокфорда. Как ученый,, могу сказать - он хорош.', en=' I\'ve reviewed Rockford\'s so-called plan. As a scientist, I must say — it\'s sound.'),
        VoiceLine(120, Mandrake, ru='Рокфорд связал около двадцати лазерных орудий кочевников в единую систему. '
        'Интересное с инженерной точки зрения решение,, надо сказать.',
        en='ockford has linked about twenty Nomad laser weapons into a single, unified system.'
        'An interesting engineering solution, I must say.'),
        VoiceLine(130, Mandrake, ru='Он хочет направить получившийся в результате луч на Сферу чтобы уничтожить её, '
        'и вместе с ней всё,, так называемое,, наследие кочевников.',
        en='He intends to fire the resulting beam at the Sphere to destroy it,'
        'and along with it, the entire so-called the Nomad Legacy.'),

        VoiceLine(140, Trent, ru='И как это произойдёт?', en='And what will happen?'),
        VoiceLine(150, Mandrake, ru='Если простыми словами - Сфера перестанет существовать. '
        'Как и... от половины до двух третей сектора Сириуса.',
        en='In simple terms? The Sphere will cease to exist.'
        'As will... approximately half to two-thirds of the Sirius Sector.'),
        VoiceLine(160, Darcy, ru='Масштабненько.', en='Well, that\'s ambitious!'),

        VoiceLine(170, Trent, ru='ЕГО... НАДО... ОСТАНОВИТЬ!!! Поймите это,, наконец!', en='HE... MUST... BE... STOPPED!!! Will you finally understand that?!'),
        VoiceLine(180, Alaric, ru='Я с тобой дружище!', en='I\'m with you, buddy!'),
        VoiceLine(190, Darcy, ru='Не могу пропустить такое представление.', en='I can\'t miss a show like this.'),
        VoiceLine(200, King, ru='Мои ресурсы в вашем распоряжении. Я выделю вам нашу лучшую спецгруппу.', en='My resources are at your disposal. I\'m assigning you our best special operations team.'),
        VoiceLine(210, Hatcher, ru='И возглавлю её я.', en='And I\'ll be leading it.'),
    ]


class Msn12Space(Msn12, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(10, Hatcher, comment='Этап 1. Путь к гипердыре',
                  ru='Скорее летим к гиперврат+ам в Штаб эСБА. У нас очень мало времени!',
                  en='Everyone, to the hypergates! We\'re heading for ASF Headquarters.We have very little time!'),

        VoiceLine(300, Hatcher, ru='Штаб, как обстановка?', en='Headquarters, what\'s your status?'),
        VoiceLine(310, Kruger, ru='Ситуация крит+ическая. Они прорвали первую линию обороны', en='The situation is critical. They\'ve broken through the first line of defense.'),
        VoiceLine(320, Kruger, ru='Вражеские инженерные войск+а приступили к демонтаж+у минных заграждений', en='Enemy engineering units have begun dismantling the minefields.'),
        VoiceLine(330, Hatcher, ru='Чёрт! Серьезно взял+ись. Держ+итесь! Мы уже на подходе', en='Damn it! They\'re not holding back.Hold on! We\'re almost there!'),

        VoiceLine(340, Hatcher, comment='Этап 2. А что Бретония?', ru='Д+ерси, могут ли нам пом+очь силы Бретонии?', en='Darcy, can Bretonia send us any support?'),
        VoiceLine(350, Darcy, ru='Я только что узнала... Королевский флот не прибудет на помощь. Они выжидают', en='I just found out... The Royal Fleet is not coming. They\'re...waiting.'),
        VoiceLine(360, Trent, ru='Чего выжидают? Вылететь на помощь нам или Ямамото?', en='Waiting for what? To decide whether to help us or Yamamoto?'),
        VoiceLine(370, Darcy, ru='Типа того...', en='Something like that...'),
        VoiceLine(380, Trent, ru='Вот суки', en='Bastards!'),
        VoiceLine(390, Hatcher, ru='Значит нам нужно выиграть эту битву', en='Then it looks like we\'ll have to win this battle on our own!'),

        VoiceLine(500, Hatcher, comment='Этап 3. Инженеры',
        ru='Форт Джефферсон, мы находимся в вашем секторе. Ваш статус?', en='Fort Jefferson, we are in your sector. What is your status?'),
        VoiceLine(510, Kruger,
        ru='В нашем секторе находится группа вражеских инженерных сил под прикрытием линкора Нагато. Передаю координаты',
        en='We have a group of enemy engineers in our sector, covered by the battleship Nagato. Sending coordinates.'),
        VoiceLine(520, Hatcher, ru='Принято, Джефферсон', en='Acknowledged, Jefferson.'),
        VoiceLine(530, Omaha, ru='Говорит крейсер Ом+аха. Мисс Х+етчер, сконцентрируйте ваш огонь на инженерах. Мы разберемся с линкорами', en='This is the cruiser Omaha. Miss Hatcher, focus your fire on the engineers. We will handle the battleships.'),
        VoiceLine(540, Hatcher, ru='Вас поняла, Ом+аха', en='Understood, Omaha!'),

        VoiceLine(550, Hatcher, ru='Трент, уничтожь рудокопы', en='Trent, take out the mining vessels!'),

        VoiceLine(600, Hatcher, ru='Рудокопы выведены из строя. Джефферсон, статус?', en='The mining vessels are disabled. Jefferson, status?'),
        VoiceLine(610, FortBush, ru='Внимание! Говорит форт Буш! Прорыв в нашем секторе! Противник прорвал защитный периметр!', en='Attention! This is Fort Bush reporting! We have a breach in our sector! The enemy has broken through the defensive perimeter!'),
        VoiceLine(620, Hatcher, ru='Чёрт! Трент, срочно летим к форту Буш. Медлить нельзя', en='Damn it! Trent, we\'re heading to Fort Bush, now! No delays!'),

        VoiceLine(630, King, ru='Всем силам приказ вернуться внутрь защитного периметра. Код один один три восемь. Штаб под угрозой', en='All units, fall back inside the defensive perimeter. Code one-one-three-eight. Headquarters is under direct threat!'),

        VoiceLine(700, FortBush, comment='Этап 4. бывш. форт Буш', ru='Внимание! Всеобщая эвакуация! Всем...хрррхррр', en='Attention! General evacuation! All perso'),
        VoiceLine(710, Trent, comment='Форт Буш взрывается нафиг', ru='Остались от Буша только ножки...', en='Nothing left of Bush but the foundation...'),
        VoiceLine(720, Hatcher, ru='Ничего хорошего, форт был последним рубежом обороны на этом фланге', en='This is bad, the fort was the last defensive line on this flank!'),
        VoiceLine(730, Hatcher, ru='Трент, нужно не дать линкорам добраться до Энтерпрайза. Сбей им двигатели! Затормози их!', en='Trent, we can\'t let those battleships reach the Enterprise.Take out their engines! Slow them down!'),
        VoiceLine(740, Darcy, ru='Линкоры будут терять скорость при потере каждого из двигателей. Трент, атакуй двигатели стратегически!', en='The battleships will lose speed with each engine you destroy. Trent, target the engines strategically!'),

        VoiceLine(800, Hatcher, ru='Генерал Кинг, срочно нужны резервы в районе бывшего форта Буш.', en='General King, we urgently need reinforcements in the former Fort Bush sector.'),
        VoiceLine(810, King, ru='Мы прикрываем Энтерпайз на Осирисе. Мы в вашем секторе.', en='We are covering the Enterprise at Osiris. We are stretched thin across your sector.'),
        VoiceLine(820, Hatcher, ru='Ты рискуешь', en='You\'re taking a huge risk!'),
        VoiceLine(830, King, ru='У нас нет другого выбора...', en='We have no other choice...'),

        VoiceLine(850, Hatcher, ru='Есть! Линкоры остановлены!', en='It worked! The battleships are stopped!'),

        VoiceLine(1000, King, ru='Внимание! Мы получ+или сигнал о приближ+ении сил +Ордена со сторон+ы станции Промет+ей', en='Attention! We are detecting Order forces approaching from the direction of Prometheus Station!'),
        VoiceLine(1010, King, ru='Хетчер, со своей группой выдвигайся в систему Прометея', en='Hatcher, take your group and move to the Prometheus system!'),

        VoiceLine(1020, Hatcher, ru='Так точно, генерал Кинг! Трент, используй портал в ядре Энтерпрайза. Так мы и попадем к станции Прометей', en='Yes, sir, General King! Trent, use the portal in the Enterprise\'s core. That\'s our way to Prometheus Station!'),

        VoiceLine(1030, King, ru='Хетчер, новые вводные. Мы обнаружили флагман противника. Наш агент докладывает, что Ямамото руководит операцией на линкоре Л+огос', en='Hatcher, new intel. We\'ve identified the enemy flagship.Our agent reports Yamamoto is commanding the operation from the battleship Logos.'),
        VoiceLine(1040, King, ru='Приказываю исполнить операцию с кодом 66. Осирис прибудет к месту сражения в ближайшее время. Обеспечьте блокирование Л+огоса к нашему прибытию', en='I am authorizing Operation Code 66. The Osiris will arrive at the combat zone shortly. You are to blockade the Logos until our arrival!'),

        VoiceLine(1050, Hatcher, ru='Вас поняли, генерал Кинг. Трент, выдвигаемся, срочно', en='Understood, General King. Trent, we\'re moving out, now!'),

        VoiceLine(1060, Alaric, ru='Что за операция 66?', en='What\'s Operation 66?'),

        VoiceLine(1070, Hatcher, ru='Блокируем Л+огос нашими линкорами и ждем, когда Осирис появится и запустит ЭМИ', en='We blockade the Logos with our battleships and wait for the Osiris to arrive and deploy an EMP.'),
        VoiceLine(1080, Hatcher, ru='После удара ЭМИ Л+огос будет беззащитен. Мы должны успеть сбить ему генератор щита, потом реактор, следом высадить десант и схватить Ямамото', en='After the EMP strike, the Logos will be defenseless. We must then take out its shield generator, then the reactor, board it, and capture Yamamoto.'),

        VoiceLine(1090, Darcy, ru='А разве ЭМИ не повредит наши системы безопасности?', en='But won\'t the EMP fry our own systems as well?'),

        VoiceLine(1100, Hatcher, ru='Да, повредит. Но у нас нет другого выбора. Линкоры класса Осирис имеют слишком крутой щит, мы не сможем его нейтрализовать иным способом', en='Yes, it will. But we have no other choice. Osiris-class battleships have incredibly powerful shields; we can\'t neutralize them any other way.'),

        VoiceLine(1110, Alaric, ru='Вот это зар+уба! Да сколько их тут!', en='Now this is a real brawl! How many of them are there?!'),
        VoiceLine(1120, Hatcher, ru='Не отвлекаемся! Наша цель - Л+огос', en='Stay focused! Our target is the Logos!'),

        VoiceLine(1130, Hatcher, ru='Генерал Кинг, мы приблизились к Л+огосу', en='General King, we are approaching the Logos!'),
        VoiceLine(1140, King, ru='Осирис в пути. Рио-Гранде и Цинцинатти начинают блокирующий ман+ёвр', en='Osiris is en route. Rio-Grande and Cincinnati, begin the blockade maneuver!'),

        VoiceLine(1150, PromDread1, ru='Говорит Цинцинатти, ман+ёвр исполнен. Л+огос удержан, но мы находимся под значительным огнем противника', en='Cincinnati here, maneuver complete. The Logos is contained, but we are taking heavy fire!'),
        VoiceLine(1160, PromDread2, ru='Противник начинает защитный ман+ёвр! Ик+арус и Х+аммер разворачиваются к Л+огосу!', en='The enemy is executing a defensive maneuver! Icarus and Hammer are turning towards the Logos!'),
        VoiceLine(1170, Hatcher, ru='Кинг, мать твою, где Осирис?', en='King, goddammit, where is the Osiris?'),

        VoiceLine(1180, King, ru='Осирис здесь. Всем приготовиться, запускаем ЭМИ', en='Osiris is here. All units, brace for EMP launch!'),

        VoiceLine(1190, Hatcher, ru='Трент, огонь по генератору щита! У нас мало времени! Снеси Л+огосу щит, срочно! Это ребристая штука у него на крыше!', en='Trent, fire on the shield generator! We have little time! Take down the Logos\' shield, now! It\'s that ribbed structure on its roof!'),

        VoiceLine(1200, Hatcher, ru='Есть! Щит Л+огоса нейтрализован. Теперь атакуем реактор. Сначала разбив+аем защитный п+ояс, а потом бьет центральный ст+ержень. Дав+айте! Ж+иво!',
                  en='Yes! The Logos\' shield is neutralized. Now we attack the reactor. First, break the protective casing, then hit the central core. Let\'s go! Move!'),
        VoiceLine(1210, Hatcher, ru='Защитный пояс уничтожен! Теперь нужно уничтожить стержень!',
                  en='The protective casing is destroyed! Now we need to destroy the core!'),

        VoiceLine(1220, Alaric, ru='Реактор Л+огоса уничтожен!', en='The Logos\' reactor is destroyed!'),

        VoiceLine(1230, PromDread1, ru='Внимание, замечен источник радиационной опасности!',
                  en='Warning, radiation hazard detected!'),
        VoiceLine(1240, Hatcher,
                  ru='А, чёрт. Этот чокнутый самурай решил устроить ядерную сеппуку! Трент, атакуй м+остик Л+огоса! Иначе тут рван+ёт так, что никому м+ало не пок+ажется!',
                  en='Ah, damn it. That crazy samurai has decided to go out with a nuclear sepukku! Trent, attack the Logos\' bridge! Otherwise, this whole place is going to blow sky-high!'),

        VoiceLine(1250, King,
                  ru='Хетчер. Мы высылаем десантный корабль. Обеспечьте ему защиту до тог+о, как он добер+ётся до Л+огоса',
                  en='Hatcher. We are deploying a boarding craft. Provide cover until it reaches the Logos!'),
        VoiceLine(1260, Alaric, ru='Вот теперь Ямам+ото точно не поздоровится!', en='Now Yamamoto is really in for it!'),

        VoiceLine(1270, Hatcher, ru='Отлично! Десант продолжает штурм. Осталось немного',
                  en='Excellent! The boarding party is pushing forward. Almost there!'),

        VoiceLine(1280, Hatcher, ru='Генерал Кинг, пришл+о сообщение от десанта. Ямамото у нас в плен+у',
                  en='General King, we have a message from the boarding team. Yamamoto is our prisoner!'),
        VoiceLine(1290, King, ru='Отличная работа, мисс Хетчер. Доставьте пленников на Осирис',
                  en='Outstanding work, Miss Hatcher! Bring the prisoners to the Osiris!'),

        VoiceLine(1300, Hatcher, ru='Ямамото на Осирисе. Миссия выполнена. Трент, заходи на посадку на Осирис.',
                  en='Yamamoto is aboard the Osiris. Mission accomplished. Trent, dock with the Osiris.'),
    ]


class Mission12(Msn12, script.StoryMission):
    CUTSCENES = [
        Msn12SpragueCutscene,
        Msn12CapturedCutscene,
    ]
    SPACE_CLASS = Msn12Space
    SYNC_SPACE = True

    MISSION_TITLE = 'Миссия 12. Оборона Энтерпрайза'
