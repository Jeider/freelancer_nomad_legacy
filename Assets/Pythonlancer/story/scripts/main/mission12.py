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
                  en='So, Trent, I hope you called me here on important business.'),
        VoiceLine(20, Trent, ru='Чрезвычайно важному делу', en='Extremely important business.'),
        VoiceLine(30, Hatcher,
                  ru='Тогда будь добр расскажи,, в чём суть. А то я заметила твои выкрутасы в системе Сириус. Теперь у меня снова есть полномочия арестовать тебя',
                  en='Then kindly tell me what this is about. I noticed your stunts in the Sirius system. I have the authority to arrest you again now.'),
        VoiceLine(40, Alaric,
                  ru='(Распахивается дверь, приходят Аларик и Дерси) Эй, Трент! Что случилось? Почему так срочно?',
                  en='Hey, Trent! What happened? Why so urgent?'),
        VoiceLine(50, Trent,
                  ru='Рокфорд заполучил артефакты, направляется к Сфере и хочет уничтожить человечество. Мы должн+ы его остановить!',
                  en='Rockford has got the artifacts, he\'s heading for the Sphere, and he wants to destroy humanity. We have to stop him!'),

        VoiceLine(60, Hatcher, ru='Что ты несёшь? Как он это сможет сделать? Подорвёт Сферу динамитом? Трент, придумай что-нибудь более интересное.', en='What are you on about? How\'s he going to do that? Blow the Sphere up with dynamite? Trent, come up with something more interesting.'),

        VoiceLine(70, Trent, ru='Рокфорд продумал эту операцию когда работал на единый Орден. Здесь точно должн+ы быть какие-то документы, планы про это. Хоть что-нибудь', en='Rockford planned this operation when he worked for the united Order. There have to be some documents here, plans about this. Anything at all.'),
        VoiceLine(80, Hatcher, ru='Ничего такого не может быть. СБА никогда не будет заниматься этой чепухой!', en='Nothing like that can exist. The ASF would never get involved in this nonsense!'),

        VoiceLine(90, Mandrake, ru='Вообще-то...', en='Actually...'),
        VoiceLine(100, Hatcher, ru='Профессор? Вы что-то про это знаете?', en='Professor? Do you know something about this?'),

        VoiceLine(110, Mandrake, ru='Возможно. Я видел подобные документы в архиве, но они засекречены.', en='Possibly. I saw similar documents in the archive, but they\'re classified.'),
        VoiceLine(120, Mandrake, ru='Требуется максимальный уровень доступа, который есть только у двух человек - у Кинга, и еще у кого-то, о ком я не знаю.', en='It requires the maximum access level, which only two people have. King, and someone else I don\'t know.'),

        VoiceLine(130, Trent, ru='Полагаю,, этого ключа доступа должно быть достаточно. (прикладывает карту доступа)', en='I believe this access key should be enough.'),
        VoiceLine(140, Darcy, ru='Нихрен+а-ж себе.', en='Holy shit.'),
        VoiceLine(150, Alaric, ru='Я о тебе чего-то не знаю?', en='Is there something I don\'t know about you?'),

        VoiceLine(160, Hatcher, ru='Ладно,, Трент. Допустим,, я тебе верю. Но как ты собираешься проникнуть в Сферу? У тебя же нет ключа от неё', en='Alright, Trent. Suppose I believe you. But how do you plan to get into the Sphere? You don\'t have the key to it.'),
        VoiceLine(170, Trent, ru='(Достает ключ) Ключ от Сферы у меня тоже есть', en='I\'ve got a key to the Sphere too.'),
        VoiceLine(180, Darcy, ru='Трент, колись, на кого тебя подменили?', en='Trent, spill it. Who\'d they replace you with?'),

        VoiceLine(190, Alaric, comment='Тревога!', ru='Это еще что такое?', en='What\'s this now?'),

        VoiceLine(250, Hatcher, comment='Хетчер подходит к столу с коммуникатором. На её лице ужас',
        ru='Штаб СБА атакован. Всем силам СБА приказано прибыть в штаб.', en='ASF headquarters has been attacked. All ASF forces are ordered to report to headquarters.'),
        VoiceLine(260, Hatcher, ru='Силы противника превосходят... Да кто же это?', en='Enemy forces are superior... Who is this?'),

        VoiceLine(270, Trent, ru='(Ужас) Чёрт... Ким же говорил про спецоперацию... Твою мать... Они на это решились.', en='Damn... Kim did mention a special operation... Son of a bitch... They went and did it.'),
        VoiceLine(280, Hatcher, ru='Кто решился? На что? Ты о чём вообще?', en='Who did? Did what? What are you even talking about?'),

        VoiceLine(290, Trent, ru='Орден решил показать кто тут главный и устранить прямого конкурента. Орден атаковал СБА, понимаешь?', en='The Order decided to show who\'s in charge and eliminate a direct rival. The Order attacked the ASF, you understand?'),
        VoiceLine(300, Trent, ru='Чтобы полностью уничтожить СБА и стать главной силой в секторе Сириуса. И в самый неподходящий момент.', en='To completely destroy the ASF and become the main force in the Sirius sector. And at the worst possible moment.'),
        VoiceLine(310, Trent, ru='Н+ахрен. Не нужны нам никакие кочевники, мы сами друг другу глотку перегрызем. Просто ради удовлетворения амбиций.', en='Fuck it. We don\'t need any Nomads. We\'ll tear each other\'s throats out ourselves. Just to satisfy ambition.'),

        VoiceLine(320, Hatcher, ru='(Осознав, выдохнув и решившись) Я им этого не позволю! Вылетаем!', en='I won\'t let them! We\'re taking off!'),
    ]


class Msn12CapturedCutscene(Msn12, script.CutsceneProps):
    ALIAS = 'captured'
    TITLE = 'Бар линкора Осирис'
    THORN_CLASS = m12_captured.Msn12CapturedScene
    THORN_DECISION_CLASS = m12_captured.Msn12CapturedDecisionScene
    THORN_ACCEPT_CLASS = m12_captured.Msn12CapturedAcceptScene
    DESCRIPTION = 'Ямамото пленён. Теперь нужно убедить Кинга заняться Рокфордом'
    VOICE_LINES = [
        VoiceLine(10, King, ru='Что с Ямамото?', en='What\'s with Yamamoto?'),
        VoiceLine(20, Hatcher, ru='Ведем дознание. Не хотите ли поприсутствовать?', en='We\'re conducting an inquiry. Would you like to be present?'),
        VoiceLine(30, King, ru='Ооо,, да! Этот безбашенный самурай превзошел самог+о себя.',
                  en='Ohhh, yes! This reckless samurai has outdone himself.'),
        VoiceLine(40, King,
                  ru='С удовольствием посмотрел бы что творится у него в мозгах, а лучше заспиртовал бы их в банке.',
                  en='I\'d love to see what\'s going on in his brains, or better yet, preserve them in alcohol in a jar.'),

        VoiceLine(50, Trent, ru='Генерал Кинг, нужно срочно остановить Рокфорда!',
                  en='General King, we urgently need to stop Rockford!'),
        VoiceLine(60, King, ru='Дался вам этот Рокфорд... Если он где-нибудь набедокурит, наши силы всё подчистят.',
                  en='You and this Rockford... If he makes a mess somewhere, our forces will clean it all up.'),
        VoiceLine(70, King, ru='А его загонят,, как зайца,, далеко в приграничье. Сам сдаваться придет, вот увидите.', en='And they\'ll run him down like a hare, far out into the borderlands. He\'ll come and surrender on his own, you\'ll see.'),
        VoiceLine(80, Hatcher, ru='Генерал Кинг, вызов от профессора Мандрейка.', en='General King, a call from Professor Mandrake.'),
        VoiceLine(90, King, ru='Выведите на главный экран.', en='Put it on the main screen.'),

        VoiceLine(100, Mandrake, ru='Генерал Кинг, мистер Трент, мисс Хетчер. О, да я смотрю,, все в сборе.', en='General King, Mister Trent, Miss Hatcher. Oh, I see everyone\'s here.'),
        VoiceLine(110, Mandrake, ru='Я ознакомился с так называемым планом Рокфорда. Как ученый,, могу сказать - он хорош.', en='I\'ve reviewed Rockford\'s so-called plan. As a scientist, I can say it\'s good.'),
        VoiceLine(120, Mandrake, ru='Рокфорд собрал мощную излучающую установку и усилил её нома́дским энергоядром ', en='Rockford built a powerful emitter and boosted it with a Nomad power core.'),
        VoiceLine(130, Mandrake, ru='Он хочет направить получившийся в результате луч на Сферу чтобы уничтожить её, '
        'и вместе с ней всё,, так называемое,, наследие кочевников.',
        en='He wants to aim the resulting beam at the Sphere to destroy it, and with it all the so-called Nomad legacy.'),

        VoiceLine(140, Trent, ru='И как это произойдёт?', en='And how will that happen?'),
        VoiceLine(150, Mandrake, ru='Если простыми словами - Сфера перестанет существовать. '
        'Как и... от половины до двух третей сектора Сириуса.',
        en='In simple terms, the Sphere will cease to exist. As will... anywhere from half to two thirds of the Sirius sector.'),
        VoiceLine(160, Darcy, ru='Масштабненько.', en='Quite a scale.'),

        VoiceLine(170, Trent, ru='ЕГО... НАДО... ОСТАНОВИТЬ!!! Поймите это,, наконец!', en='HE... MUST... BE STOPPED!!! Understand this, finally!'),
        VoiceLine(180, Alaric, ru='Я с тобой дружище!', en='I\'m with you, buddy!'),
        VoiceLine(190, Darcy, ru='Не могу пропустить такое представление.', en='Can\'t miss a show like this.'),
        VoiceLine(200, King, ru='Мои ресурсы в вашем распоряжении. Я выделю вам нашу лучшую спецгруппу.', en='My resources are at your disposal. I\'ll assign you our best special team.'),
        VoiceLine(210, Hatcher, ru='И возглавлю её я.', en='And I will lead it.'),
    ]


class Msn12Space(Msn12, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(10, Hatcher, comment='Этап 1. Путь к гипердыре',
                  ru='Скорее летим к гиперврат+ам в Штаб эСБА. У нас очень мало времени!',
                  en='Hurry, we\'re flying to the jump gates to ASF headquarters. We have very little time!'),

        VoiceLine(300, Hatcher, ru='Штаб, как обстановка?', en='Headquarters, what\'s the situation?'),
        VoiceLine(310, Kruger, ru='Ситуация крит+ическая. Они прорвали первую линию обороны', en='The situation is critical. They\'ve broken through the first line of defense.'),
        VoiceLine(320, Kruger, ru='Вражеские инженерные войск+а приступили к демонтаж+у минных заграждений', en='Enemy engineering troops have started dismantling the mine barriers.'),
        VoiceLine(330, Hatcher, ru='Чёрт! Серьезно взял+ись. Держ+итесь! Мы уже на подходе', en='Damn! They\'re serious about this. Hold on! We\'re already on approach.'),

        VoiceLine(340, Hatcher, comment='Этап 2. А что Бретония?', ru='Д+ерси, могут ли нам пом+очь силы Бретонии?', en='Darcy, can Bretonia\'s forces help us?'),
        VoiceLine(350, Darcy, ru='Я только что узнала... Королевский флот не прибудет на помощь. Они выжидают', en='I just found out... The Royal Fleet will not come to help. They\'re waiting.'),
        VoiceLine(360, Trent, ru='Чего выжидают? Вылететь на помощь нам или Ямамото?', en='Waiting for what? To fly out and help us, or Yamamoto?'),
        VoiceLine(370, Darcy, ru='Типа того...', en='Something like that...'),
        VoiceLine(380, Trent, ru='Вот суки', en='Those bitches.'),
        VoiceLine(390, Hatcher, ru='Значит нам нужно выиграть эту битву', en='Then we need to win this battle.'),

        VoiceLine(500, Hatcher, comment='Этап 3. Инженеры',
        ru='Форт Джефферсон, мы находимся в вашем секторе. Ваш статус?', en='Fort Jefferson, we are in your sector. Your status?'),
        VoiceLine(510, Kruger,
        ru='В нашем секторе находится группа вражеских инженерных сил под прикрытием линкора Нагато. Передаю координаты',
        en='There\'s a group of enemy engineering forces in our sector, under cover of the battleship Nagato. Sending coordinates.'),
        VoiceLine(520, Hatcher, ru='Принято, Джефферсон', en='Acknowledged, Jefferson.'),
        VoiceLine(530, Omaha, ru='Говорит крейсер Ом+аха. Мисс Х+етчер, сконцентрируйте ваш огонь на инженерах. Мы разберемся с линкорами', en='This is the cruiser Omaha. Miss Hatcher, concentrate your fire on the engineers. We\'ll deal with the battleships.'),
        VoiceLine(540, Hatcher, ru='Вас поняла, Ом+аха', en='Understood, Omaha.'),

        VoiceLine(550, Hatcher, ru='Трент, уничтожь рудокопы', en='Trent, destroy the miners.'),

        VoiceLine(600, Hatcher, ru='Рудокопы выведены из строя. Джефферсон, статус?', en='The miners are out of action. Jefferson, status?'),
        VoiceLine(610, FortBush, ru='Внимание! Говорит форт Буш! Прорыв в нашем секторе! Противник прорвал защитный периметр!', en='Attention! This is Fort Bush! Breakthrough in our sector! The enemy has broken through the defensive perimeter!'),
        VoiceLine(620, Hatcher, ru='Чёрт! Трент, срочно летим к форту Буш. Медлить нельзя', en='Damn! Trent, we\'re flying to Fort Bush, urgent. No delaying.'),

        VoiceLine(630, King, ru='Всем силам приказ вернуться внутрь защитного периметра. Код один один три восемь. Штаб под угрозой', en='All forces, order to return inside the defensive perimeter. Code one one three eight. Headquarters is under threat.'),

        VoiceLine(700, FortBush, comment='Этап 4. бывш. форт Буш', ru='Внимание! Всеобщая эвакуация! Всем...хрррхррр', en='Attention! General evacuation! Everyone...krrrkrrr'),
        VoiceLine(710, Trent, comment='Форт Буш взрывается нафиг', ru='Остались от Буша только ножки...', en='Nothing left of Bush but the legs...'),
        VoiceLine(720, Hatcher, ru='Ничего хорошего, форт был последним рубежом обороны на этом фланге', en='Nothing good about it. The fort was the last line of defense on this flank.'),
        VoiceLine(730, Hatcher, ru='Трент, нужно не дать линкорам добраться до Энтерпрайза. Сбей им двигатели! Затормози их!', en='Trent, we can\'t let the battleships reach the Enterprise. Shoot out their engines! Slow them down!'),
        VoiceLine(740, Darcy, ru='Линкоры будут терять скорость при потере каждого из двигателей. Трент, атакуй двигатели стратегически!', en='The battleships will lose speed with each engine they lose. Trent, attack the engines strategically!'),

        VoiceLine(800, Hatcher, ru='Генерал Кинг, срочно нужны резервы в районе бывшего форта Буш.', en='General King, we urgently need reserves in the area of the former Fort Bush.'),
        VoiceLine(810, King, ru='Мы прикрываем Энтерпайз на Осирисе. Мы в вашем секторе.', en='We\'re covering the Enterprise from the Osiris. We\'re in your sector.'),
        VoiceLine(820, Hatcher, ru='Ты рискуешь', en='You\'re taking a risk.'),
        VoiceLine(830, King, ru='У нас нет другого выбора...', en='We have no other choice...'),

        VoiceLine(850, Hatcher, ru='Есть! Линкоры остановлены!', en='Yes! The battleships are stopped!'),

        VoiceLine(1000, King, ru='Внимание! Мы получ+или сигнал о приближ+ении сил +Ордена со сторон+ы станции Промет+ей', en='Attention! We\'ve received a signal that Order forces are approaching from the direction of Prometheus Station.'),
        VoiceLine(1010, King, ru='Хетчер, со своей группой выдвигайся в систему Прометея', en='Hatcher, move out with your group to the Prometheus system.'),

        VoiceLine(1020, Hatcher, ru='Так точно, генерал Кинг! Трент, используй портал в ядре Энтерпрайза. Так мы и попадем к станции Прометей', en='Yes, sir, General King! Trent, use the portal in the Enterprise\'s core. That\'s how we\'ll get to Prometheus Station.'),

        VoiceLine(1030, King, ru='Хетчер, новые вводные. Мы обнаружили флагман противника. Наш агент докладывает, что Ямамото руководит операцией на линкоре Л+огос', en='Hatcher, new briefing. We\'ve found the enemy flagship. Our agent reports Yamamoto is directing the operation from the battleship Logos.'),
        VoiceLine(1040, King, ru='Приказываю исполнить операцию с кодом 66. Осирис прибудет к месту сражения в ближайшее время. Обеспечьте блокирование Л+огоса к нашему прибытию', en='I order you to carry out the operation, code 66. The Osiris will arrive at the battle shortly. Blockade the Logos by the time we arrive.'),

        VoiceLine(1050, Hatcher, ru='Вас поняли, генерал Кинг. Трент, выдвигаемся, срочно', en='Understood, General King. Trent, we\'re moving out, urgent.'),

        VoiceLine(1060, Alaric, ru='Что за операция 66?', en='What\'s operation 66?'),

        VoiceLine(1070, Hatcher, ru='Блокируем Л+огос нашими линкорами и ждем, когда Осирис появится и запустит ЭМИ', en='We blockade the Logos with our battleships and wait for the Osiris to arrive and launch the EMP.'),
        VoiceLine(1080, Hatcher, ru='После удара ЭМИ Л+огос будет беззащитен. Мы должны успеть сбить ему генератор щита, потом реактор, следом высадить десант и схватить Ямамото', en='After the EMP strike, the Logos will be defenseless. We have to take out its shield generator in time, then the reactor, then land troops and seize Yamamoto.'),

        VoiceLine(1090, Darcy, ru='А разве ЭМИ не повредит наши системы безопасности?', en='But won\'t the EMP damage our safety systems?'),

        VoiceLine(1100, Hatcher, ru='Да, повредит. Но у нас нет другого выбора. Линкоры класса Осирис имеют слишком крутой щит, мы не сможем его нейтрализовать иным способом', en='Yes, it will. But we have no other choice. Osiris-class battleships have too tough a shield. We can\'t neutralize it any other way.'),

        VoiceLine(1110, Alaric, ru='Вот это зар+уба! Да сколько их тут!', en='Now this is a brawl! How many of them are there!'),
        VoiceLine(1120, Hatcher, ru='Не отвлекаемся! Наша цель - Л+огос', en='Stay on task! Our target is the Logos.'),

        VoiceLine(1130, Hatcher, ru='Генерал Кинг, мы приблизились к Л+огосу', en='General King, we\'ve closed in on the Logos.'),
        VoiceLine(1140, King, ru='Осирис в пути. Рио-Гранде и Цинцинатти начинают блокирующий ман+ёвр', en='Osiris is on the way. Rio Grande and Cincinnati are starting the blocking maneuver.'),

        VoiceLine(1150, PromDread1, ru='Говорит Цинцинатти, ман+ёвр исполнен. Л+огос удержан, но мы находимся под значительным огнем противника', en='Cincinnati speaking, maneuver complete. The Logos is held, but we\'re under significant enemy fire.'),
        VoiceLine(1160, PromDread2, ru='Противник начинает защитный ман+ёвр! Ик+арус и Х+аммер разворачиваются к Л+огосу!', en='The enemy is starting a defensive maneuver! Icarus and Hammer are turning toward the Logos!'),
        VoiceLine(1170, Hatcher, ru='Кинг, мать твою, где Осирис?', en='King, damn you, where\'s the Osiris?'),

        VoiceLine(1180, King, ru='Осирис здесь. Всем приготовиться, запускаем ЭМИ', en='Osiris is here. Everyone, get ready, we\'re launching the EMP.'),

        VoiceLine(1190, Hatcher, ru='Трент, огонь по генератору щита! У нас мало времени! Снеси Л+огосу щит, срочно! Это ребристая штука у него на крыше!', en='Trent, fire on the shield generator! We don\'t have much time! Take down the Logos shield, now! It\'s that ribbed thing on its roof!'),

        VoiceLine(1200, Hatcher, ru='Есть! Щит Л+огоса нейтрализован. Теперь атакуем реактор. Сначала разбив+аем защитный п+ояс, а потом бьет центральный ст+ержень. Дав+айте! Ж+иво!',
                  en='Yes! The Logos shield is neutralized. Now we attack the reactor. First we break the protective belt, then we hit the central rod. Come on! Move!'),
        VoiceLine(1210, Hatcher, ru='Защитный пояс уничтожен! Теперь нужно уничтожить стержень!',
                  en='The protective belt is destroyed! Now we need to destroy the rod!'),

        VoiceLine(1220, Alaric, ru='Реактор Л+огоса уничтожен!', en='The Logos reactor is destroyed!'),

        VoiceLine(1230, PromDread1, ru='Внимание, замечен источник радиационной опасности!',
                  en='Attention, a radiation hazard source has been detected!'),
        VoiceLine(1240, Hatcher,
                  ru='А, чёрт. Этот чокнутый самурай решил устроить ядерную сеппуку! Трент, атакуй м+остик Л+огоса! Иначе тут рван+ёт так, что никому м+ало не пок+ажется!',
                  en='Ah, damn. This crazy samurai decided on nuclear seppuku! Trent, attack the Logos bridge! Otherwise it\'ll blow so hard here that nobody gets off easy!'),

        VoiceLine(1250, King,
                  ru='Хетчер. Мы высылаем десантный корабль. Обеспечьте ему защиту до тог+о, как он добер+ётся до Л+огоса',
                  en='Hatcher. We\'re sending a landing ship. Cover it until it reaches the Logos.'),
        VoiceLine(1260, Alaric, ru='Вот теперь Ямам+ото точно не поздоровится!', en='Now Yamamoto is definitely in for it!'),

        VoiceLine(1270, Hatcher, ru='Отлично! Десант продолжает штурм. Осталось немного',
                  en='Excellent! The landing party continues the assault. Not much left.'),

        VoiceLine(1280, Hatcher, ru='Генерал Кинг, пришл+о сообщение от десанта. Ямамото у нас в плен+у',
                  en='General King, a message came from the landing party. Yamamoto is our prisoner.'),
        VoiceLine(1290, King, ru='Отличная работа, мисс Хетчер. Доставьте пленников на Осирис',
                  en='Excellent work, Miss Hatcher. Deliver the prisoners to the Osiris.'),

        VoiceLine(1300, Hatcher, ru='Ямамото на Осирисе. Миссия выполнена. Трент, заходи на посадку на Осирис.',
                  en='Yamamoto is on the Osiris. Mission complete. Trent, come in and dock with the Osiris.'),
    ]


class Mission12(Msn12, script.StoryMission):
    CUTSCENES = [
        Msn12SpragueCutscene,
        Msn12CapturedCutscene,
    ]
    SPACE_CLASS = Msn12Space
    SYNC_SPACE = True
    SYNC_SUBS = True

    MISSION_TITLE = 'Миссия 12. Оборона Энтерпрайза'