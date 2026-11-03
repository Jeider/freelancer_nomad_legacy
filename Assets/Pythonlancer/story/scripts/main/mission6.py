from story import script
from audio.sound import VoiceLine
from story.actors import (
    Trent, Hatcher, HatcherStation, FinnRunner, Reitherman, DeltaOne, DeltaThree,
    SphereAssistant, SphereOutpost, SphereMissouri,
    Alaric, OrderPilot, Ceed, OrderGuard
)


class Msn6(object):
    MISSION_INDEX = 6


class Msn6Offer(Msn6, script.CutsceneProps):
    ALIAS = 'offer'
    TITLE = 'Предложение'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Trent, ru="Мисс Хетчер. Аларик, не ожидал, что ты уже здесь.", en="Miss Hatcher. Alaric, I didn't expect you to be here already."),
        VoiceLine(20, Alaric, ru="Как только ты со мной связался, я сразу же прибыл к мисс Хетчер. Видимо, я был ближе, чем ты.", en="As soon as you contacted me, I came straight to Miss Hatcher. Apparently I was closer than you."),
        VoiceLine(30, Hatcher, ru="А теперь, господа, когда все выяснили когда, откуда и каким образом мы все сюда прибыли, перейдем к делу? ... ", en="And now, gentlemen, now that everyone's sorted out when, from where, and how we all got here, shall we get to business? ..."),
        VoiceLine(40, Hatcher, ru="Отлично! Как вы уже поняли есть некий объект - Сфера. В свое время его обнаружил еще Орден, но тогда никто не смог понять что это, для чего предназначено и как работает. И про Сферу забыли. ", en="Excellent! As you've already understood, there's a certain object, the Sphere. The Order discovered it in its time, but back then no one could understand what it was, what it was for, or how it worked. And the Sphere was forgotten."),
        VoiceLine(50, Hatcher, ru="А теперь мы узнаём что рейнландцам удалось подобрать к ней ключ и они проводят на ней свои исследования. Есть обоснованное мнение, что ничем хорошим это не закончится. Поэтому исследования эти нужно, как бы это сказать... закрыть.", en="And now we're learning that the Rheinlanders have managed to find a key to it, and they're conducting their research on it. There's good reason to think this won't end well. So this research needs to be, how to put it... closed."),
        VoiceLine(60, Trent, ru="Ха-ха-ха, отлично. Если вы не смогли подобрать к Сфере ключ сами, то никто не должен. А если подобрал, то нужно срочно устранить либо ключ, либо Сферу, либо того кто это сделал. Браво! Так не доставайся же ты никому.", en="Ha-ha-ha, perfect. If you couldn't find a key to the Sphere yourselves, then no one should. And if someone did, then we urgently need to eliminate either the key, or the Sphere, or the one who did it. Bravo! Then let no one have you."),
        VoiceLine(70, Hatcher, ru="Я не разделяю вашего сарказма, мистер Трент. В прошлый раз подобная ситуация случилась, когда другие рейнландские ученые нашли нечто в Омикронах. Ох уж мне эти неугомонные рейнландцы.", en="I don't share your sarcasm, Mr. Trent. Last time, a similar situation happened when other Rheinland scientists found something in the Omicrons. Oh, these restless Rheinlanders."),
        VoiceLine(80, Hatcher, ru="И все закончилось тем самым кризисом, про который я вам рассказывала в присутствие профессора Мандрейка. Вы поняли, о чем я?", en="And it all ended in that very crisis I told you about in Professor Mandrake's presence. Do you understand what I mean?"),
        VoiceLine(90, Trent, ru="Да, понял. Не стоит шутить с ящиком Пандоры.", en="Yes, I understand. Best not to joke with Pandora's box."),
        VoiceLine(100, Hatcher, ru="Хорошо, с моральной подоплекой наших действий мы разобрались, теперь про материальную. Вы получите вознаграждение втрое больше обычного, и удостоверения внештатных сотрудников СБА. ", en="Good. We've settled the moral basis of our actions. Now the material one. You'll receive a reward three times the usual, and credentials as non-staff ASF employees."),
        VoiceLine(110, Alaric, ru="Чёрт побери, я за! Где ставить подпись? Могу кровью!", en="Damn, I'm in! Where do I sign? I can do it in blood!"),
        VoiceLine(120, Trent, ru="Аларик, угомонись. Мисс Хетчер, а что конкретно нужно сделать? Уничтожить Сферу, уничтожить ученых? Мне это совсем не по душе, я всё-таки не наёмный убийца.", en="Alaric, settle down. Miss Hatcher, what exactly needs to be done? Destroy the Sphere, destroy the scientists? I really don't like that. I'm not a hired killer, after all."),
        VoiceLine(130, Hatcher, ru='А вы уверены? Нет, все не так страшно и кроваво, как вы сейчас расписали. В полученных нами документах профессор нашел способ сделать Сферу невосприимчивой к внешним воздействиям, как сказал профессор "закрыться". ', en="Are you sure? No, it's not as frightening and bloody as you've just described. In the documents we received, the professor found a way to make the Sphere unreceptive to outside influence, as the professor said, to \"close\"."),
        VoiceLine(140, Hatcher, ru="Все дальнейшие подробности - в том случае, если вы согласитесь.", en="All further details, if you agree."),
        VoiceLine(150, Trent, ru='У меня дежавю. Вот только в прошлый раз меня называли не "мистер Трент", а "герр Трент"... С другой стороны, временами было весело... Хорошо, я в деле.', en="I'm having deja vu. Only last time I wasn't called \"Mr. Trent\", but \"Herr Trent\"... On the other hand, at times it was fun... All right, I'm in."),
        VoiceLine(160, Hatcher, ru="Тогда встретимся на орбите и продолжим разговор там.", en="Then we'll meet in orbit and continue the conversation there."),
    ]


class Msn6Briefieng(Msn6, script.CutsceneProps):
    ALIAS = 'briefing'
    TITLE = 'Брифинг'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Hatcher, ru="Итак, джентльмены, главная задача - ликвидировать рейнландского ученого, профессора Роттермана.", en="So, gentlemen, the main task is to liquidate the Rheinland scientist, Professor Rotterman."),
        VoiceLine(20, Trent, ru="Черт, я так и думал.", en="Damn, that's what I thought."),
        VoiceLine(30, Hatcher, ru="Не перебивайте, Трент!  Думал он. Может быть, вы также думали, что за такой гонорар вам поручат доставку суши? ", en="Don't interrupt, Trent! He thought. Maybe you also thought that for a fee like that you'd be assigned a sushi delivery?"),
        VoiceLine(40, Hatcher, ru="Пора взрослеть, мистер Трент. ", en="Time to grow up, Mr. Trent."),
        VoiceLine(50, Hatcher, ru="Итак, ликвидируете профессора Роттермана и забираете два артефакта - кристалл кочевников и том Протея, они должны находиться либо у профессора, либо рядом с ним.", en="So, you liquidate Professor Rotterman and take two artifacts, the Nomad crystal and the Proteus Tome. They should be either on the professor or near him."),
        VoiceLine(60, Hatcher, ru="В свое время они хранились в одном из тайников Ордена, но в так называемые смутные времена следы их потерялись.", en="In their time they were kept in one of the Order's caches, but in the so-called troubled times their trail was lost."),
        VoiceLine(70, Hatcher, ru="Вы забираете артефакты, увозите их и Сфера закрывается.", en="You take the artifacts, carry them away, and the Sphere closes."),
        VoiceLine(80, Alaric, ru="Орден? Смутные времена?", en="The Order? Troubled times?"),
        VoiceLine(90, Trent, ru="Позже, Аларик.", en="Later, Alaric."),
        VoiceLine(100, Hatcher, ru="Хватит, чёрт побери, меня перебивать, мы сейчас обсуждаем важнейшую миссию! ", en="Enough, damn it, of interrupting me. We're discussing the most important mission right now!"),
        VoiceLine(110, Trent, ru="Самую важную в вашей жизни, мисс Хетчер? Не забывайте что конкретные исполнители - мы, и вот как исполнители мы хотели бы подробностей о предшествующих ликвидации профессора этапах. ", en="The most important of your life, Miss Hatcher? Don't forget that the ones actually doing it are us, and as the ones doing it we'd like the details of the stages before the professor's liquidation."),
        VoiceLine(120, Hatcher, ru="Хорошо, Трент. Итак, проникновение внутрь Сферы. Охраняется она беспрецедентно. Я сомневаюсь, что кайзер Рейнланда охраняется так же как она. ", en="All right, Trent. So, getting inside the Sphere. It's guarded like nothing else. I doubt the Kaiser of Rheinland is guarded the way it is."),
        VoiceLine(130, Hatcher, ru="Рядом со сферой находится военная база, представляющая собою верфь, способную принимать по два линкора и четыре корабля среднего тоннажа одновременно. Понимаете, какая там развернута группировка? Поэтому силовое решение невозможно. ", en="Next to the Sphere there's a military base, a shipyard able to take two battleships and four medium-tonnage ships at once. Do you understand what kind of force is deployed there? That's why a solution by force is impossible."),
        VoiceLine(140, Hatcher, ru="Для проникновения вам понадобятся устройства, которые находятся в контейнерах, переданных мною вам перед стыковкой с Миссури. Это устройства, делающие ваши корабли невидимыми как визуально, так и всеми радарными системами. ", en="To get in, you'll need the devices in the containers I handed you before docking with Missouri. These devices make your ships invisible, both to the eye and to all radar systems."),
        VoiceLine(150, Hatcher, ru="Они создают вокруг корабля локальное искривление пространства, и ваши корабли как бы перестают находиться в нашей реальности. ", en="They create a local warp of space around the ship, and your ships sort of stop being in our reality."),
        VoiceLine(160, Hatcher, ru="Смонтируете их у себя на кораблях - просто устанавливаете где-нибудь внутри герметичного корпуса, подключаете к энергосистеме и выводите кнопку управления в удобное место приборной доски. Кнопка всего одна, не ошибетесь. ", en="You'll mount them on your ships. You just install them somewhere inside the sealed hull, connect them to the power system, and run the control button out to a convenient spot on the instrument panel. There's only one button. You won't get it wrong."),
        VoiceLine(170, Hatcher, ru="Нажимаете один раз - и ваш корабль невидим, нажимаете второй раз - и он снова видим. Проблема устройства в его одноразовости. ", en="Press once, and your ship is invisible. Press a second time, and it's visible again. The problem with the device is that it's single-use."),
        VoiceLine(180, Hatcher, ru="Я не ученый, поэтому скажу просто, после выключения там что-то перегорает, и оно превращается в коробочку с горелым пластиком и обугленным  металлом. ", en="I'm not a scientist, so I'll put it simply. After you switch it off, something in there burns out, and it turns into a box of burnt plastic and charred metal."),
        VoiceLine(190, Trent, ru="Огнетушителями запасаться? ", en="Should we stock up on fire extinguishers?"),
        VoiceLine(200, Hatcher, ru="Нет, все безопасно, все происходит внутри устройства, даже неприятного запаха не появится. ", en="No, it's all safe. It all happens inside the device. There won't even be an unpleasant smell."),
        VoiceLine(210, Hatcher, ru="По времени работы. Поскольку устройство одноразовое, постарайтесь использовать его максимально эффективно. Наши головастики гарантируют тридцать минут работы. Возможно, оно проработает сорок, больше вряд ли. ", en="As for operating time. Since the device is single-use, try to use it as effectively as possible. Our eggheads guarantee thirty minutes of operation. It might work for forty. More than that is unlikely."),
        VoiceLine(220, Hatcher, ru="Если тридцати минут работы не хватило, вы можете попробовать оставаться в невидимости дольше на свой страх и риск. Если устройство сгорит не во время выключения, а во время работы, локальное искривление пространства схлопывается вместе с кораблём. ", en="If thirty minutes of operation isn't enough, you can try to stay invisible longer at your own risk. If the device burns out during operation, not when it's switched off, the local space warp collapses together with the ship."),
        VoiceLine(230, Alaric, ru="И куда попадает корабль? В другое измерение? ", en="And where does the ship end up? Another dimension?"),
        VoiceLine(240, Hatcher, ru="Понятия не имею. Хотите узнать, мистер Аларик? По глазам вижу, что нет. И да, еще один момент. При включенном устройстве стрелять бесполезно. Выши выстрелы не покинут локальную зону искривления пространства.", en="I have no idea. Want to find out, Mr. Alaric? I can see in your eyes that you don't. And yes, one more thing. With the device on, shooting is useless. Your shots won't leave the local zone of warped space."),
        VoiceLine(250, Hatcher, ru="Вот трехмерный план Сферы и все данные по ней, которые нам удалось собрать.", en="Here's a three-dimensional plan of the Sphere, and all the data on it that we managed to collect."),
        VoiceLine(260, Alaric, ru="Вот это хреновина...", en="Now that's a hell of a thing..."),
        VoiceLine(270, Hatcher, ru="Я рада, что вы прониклись, мистер Аларик. Загрузите всё к себе в компьютер. В ходе операции будете передавать нужные данные мистеру Тренту. ", en="I'm glad it got through to you, Mr. Alaric. Load everything into your computer. During the operation you'll pass the needed data to Mr. Trent."),
        VoiceLine(280, Hatcher, ru="Ну и последнее - после прибытия на территорию Рейнланда никаких радиопереговоров со мной или с кем-то еще на территории Либерти. Вас запеленгуют их радарные станции, и миссия завершится так и не начавшись. ", en="And last. After you arrive in Rheinland territory, no radio contact with me or with anyone else in Liberty territory. Their radar stations will get a fix on you, and the mission will end before it starts."),
        VoiceLine(290, Hatcher, ru="Вот, собственно, и всё. По коням, джентльмены.", en="Well, that's all. Mount up, gentlemen."),
    ]


class Msn6Mount(Msn6, script.CutsceneProps):
    ALIAS = 'mount'
    TITLE = 'Установка устройства'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Trent, ru="У тебя редкий талант постоянно влипать в неприятности, Аларик.", en="You have a rare talent for constantly getting into trouble, Alaric."),
        VoiceLine(20, Alaric, ru="Ты о чем? ", en="What do you mean?"),
        VoiceLine(30, Trent, ru="О том что с нами будет происходить в ближайшем будущем.", en="About what's going to happen to us in the near future."),
        VoiceLine(40, Alaric, ru="Ты про нашу миссию?", en="You mean our mission?"),
        VoiceLine(50, Trent, ru="Про нашу СУИЦИДАЛЬНУЮ миссию.", en="About our SUICIDAL mission."),
        VoiceLine(60, Alaric, ru="Зато какие выгоды в случае успеха! К тому же ты мог бы отказаться.", en="But think of the benefits if we succeed! Besides, you could have refused."),
        VoiceLine(70, Trent, ru="Боюсь, если бы я отказался, то уже летал бы в космосе без скафандра.", en="I'm afraid if I had refused, I'd already be flying in space without a suit."),
        VoiceLine(80, Alaric, ru="Трент, раз уж мы подписались, надо выполнять. Давай, Трент, полетели. Обещаю, в следующий раз заказчика будешь выбирать ты.", en="Trent, since we've signed on, we have to carry it out. Come on, Trent, let's fly. I promise, next time you'll choose the client."),
        VoiceLine(90, Trent, ru="Если он будет, этот следующий раз. ", en="If there is one, that next time."),
    ]


class Msn6LabLand(Msn6, script.CutsceneProps):
    ALIAS = 'lab_land'
    TITLE = 'Посадка на лабораторию'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Alaric, ru="Трент, у нас мало времени. Я уже установил взрывчатку с таймером обратного отсчета.", en="Trent, we don't have much time. I've already set explosives with a countdown timer."),
        VoiceLine(20, Trent, ru="Мы же хотели просто закрыть сферу?", en="We just wanted to close the sphere, didn't we?"),
        VoiceLine(30, Alaric, ru="Вот мы и закроем. Хетчер решила подстраховаться. Мы уничтожим лабораторию.", en="And that's how we'll close it. Hatcher decided to play it safe. We're going to destroy the laboratory."),
        VoiceLine(40, Trent, ru="Ясно.", en="I see."),
    ]


class Msn6LabRoom(Msn6, script.CutsceneProps):
    ALIAS = 'lab_room'
    TITLE = 'Лаборатория'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Trent, ru="Обалдеть...", en="Whoa..."),
        VoiceLine(20, Alaric, ru="Трент, бежим! Потом рассмотришь.", en="Trent, let's run! You'll look later."),
    ]


class Msn6TorpedoAlert(Msn6, script.CutsceneProps):
    ALIAS = 'torpedo_alert'
    TITLE = 'Торпедная тревога'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Hatcher, ru="Трент, у нас критическая ситуация! Рейнландцы выпустили против Миссури торпедные канонерки. ", en="Trent, we have a critical situation! The Rheinlanders have launched torpedo gunboats against Missouri."),
        VoiceLine(20, Hatcher, ru="Мы не успеваем запустить гипердвигатель, а системы ПВО линкора не смогут перехватить все выпущенные торпеды. ", en="We won't have time to start the hyperdrive, and the battleship's air defenses won't be able to intercept all the torpedoes that were launched."),
        VoiceLine(40, Trent, ru="Но сначала нужно выгрузить артефакты.", en="But first we need to unload the artifacts."),
        VoiceLine(50, Hatcher, ru="В данной ситуации они большей безопасности у вас на борту, а не на Миссури. Вылетайте! Быстрее!", en="In this situation they're safer aboard your ship than on Missouri. Take off! Faster!"),
    ]


class Msn6OrderDeck(Msn6, script.CutsceneProps):
    ALIAS = 'order_deck'
    TITLE = 'Стыковочный узел Навухудоносора'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, OrderPilot, ru="Капитан Сид, мы обнаружили артефакты на борту этого фриленсера.", en="Captain Ceed, we've found the artifacts aboard this freelancer."),
        VoiceLine(20, Ceed, ru="Отлично. Спасибо за работу, ребята. Артефакты – на склад, пленных – в кают-компанию.", en="Excellent. Thanks for the work, guys. Artifacts to storage, prisoners to the wardroom."),

    ]


class Msn6Prison(Msn6, script.CutsceneProps):
    ALIAS = 'order_prison'
    TITLE = 'Тюремная камера'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Ceed, ru="Вольно, рядовой. Идите в диспетчерскую, пусть подготовят корабль для доставки пленных на нашу базу. А я пока начну допрос.", en="At ease, private. Go to the dispatch room. Have them prepare a ship to deliver the prisoners to our base. And I'll start the interrogation in the meantime."),
        VoiceLine(20, OrderGuard, ru="Сэр, но если...", en="Sir, but what if..."),
        VoiceLine(30, Ceed, ru="Никаких если. На них же шокеры, пусть только попробуют рыпнуться.", en="No ifs. They've got shockers on. Let them just try to make a move."),
        VoiceLine(40, OrderGuard, ru="Есть, сэр.", en="Yes, sir."),
        VoiceLine(50, Ceed, ru="Спокойно, джентльмены, я не кусаюсь. Вам повезло, что все произошло во время моего дежурства.", en="Easy, gentlemen, I don't bite. You got lucky that all this happened during my watch."),
        VoiceLine(60, Ceed, ru="Забыл представиться. Хари Сид, капитан Ордена, лейтенант СБА, работаю тут под прикрытием.", en="Forgot to introduce myself. Harry Ceed, Order captain, ASF lieutenant. I work here undercover."),
        VoiceLine(65, Ceed, ru="Сейчас подождем некоторое время, а потом я помогу вам покинуть негостеприимный борт Навуходоносора", en="We'll wait a while now, and then I'll help you leave the inhospitable deck of the Nebuchadnezzar."),
        VoiceLine(70, DeltaThree, ru="Сдается мне, ребята, что это очередная провокация Ордена, и выведет нас этот милый капитан на шеренгу бойцов со штурмовыми винтовками.", en="Seems to me, guys, this is another Order provocation, and this nice captain will lead us out to a line of fighters with assault rifles."),
        VoiceLine(80, DeltaOne, ru="А у тебя что, есть предложения получше? В любом случае, лучше на шеренгу бойцов с винтовками, чем на допрос к специалистам Ордена.", en="And you, got any better ideas? In any case, better a line of fighters with rifles than an interrogation by Order specialists."),
        VoiceLine(90, Trent, ru="А что там с артефактами, капитан?", en="And what about the artifacts, captain?"),
        VoiceLine(100, Ceed, ru="Летят на базу Ордена.", en="They're flying to an Order base."),
        VoiceLine(110, DeltaOne, ru=" И вы позволили?", en="And you allowed that?"),
        VoiceLine(120, Ceed, ru="А что я, по-вашему, должен был сделать? Если бы я начал вставлять Ордену палки в колеса, то сидел бы тут с вами, только не с сигаретой в руке, а с таким же милым ошейником на шее как у вас.", en="And what do you think I was supposed to do? If I'd started putting a spoke in the Order's wheels, I'd be sitting here with you, only not with a cigarette in my hand, but with the same nice collar on my neck as you."),
        VoiceLine(130, Trent, ru="А как вы собираетесь помочь нам бежать?", en="And how are you planning to help us escape?"),
        VoiceLine(140, Ceed, ru="Для начала вы примерите вот это...", en="For a start, you'll try this on..."),
        VoiceLine(145, Ceed, ru="А потом спокойно и небрежно проследуете в ангар к кораблю мистера Трента. ", en="And then, calmly and casually, you'll proceed to the hangar, to Mr. Trent's ship."),
        VoiceLine(150, Ceed, ru="К сожалению, все остальные уже разбирают на запчасти. А вот корабль Трента пока еще в целости и сохранности. Так что, как говорится, в тесноте, да не в обиде.", en="Unfortunately, all the others are already being taken apart for parts. But Trent's ship is still in one piece. So, as they say, cramped, but no hard feelings."),
        VoiceLine(160, Trent, ru="А после нашего побега... Как это скажется на вас? Вы не будете сидеть здесь не с сигаретой в руке, а с ошейником как у нас на шее?", en="And after our escape... How will that affect you? You won't be sitting here, not with a cigarette in your hand, but with a collar like ours on your neck?"),
        VoiceLine(170, Ceed, ru="О, нет. Вы же меня вырубили, этому найдутся неоспоримые доказательства. ", en="Oh, no. You knocked me out. There'll be indisputable proof of that."),
        VoiceLine(180, Ceed, ru="К тому же, что такое побег пленников в сравнении с тем, что я передал в руки  Ордена артефакты, за которыми охотится весь сектор Сириуса.", en="Besides, what's a prisoners' escape compared to me handing the Order the artifacts the entire Sirius sector is hunting for."),
        VoiceLine(190, Trent, ru="Толково, не поспоришь. ", en="Sound. Can't argue with that."),

    ]


class Msn6Freeport(Msn6, script.CutsceneProps):
    ALIAS = 'freeport'
    TITLE = 'Фрипорт'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, DeltaOne, ru="Мистер Трент, мы благодарим вас за вашу работу. Мы виноваты в том, что вы попали в неприятности. И мы постараемся исправить ситуацию.", en="Mr. Trent, we thank you for your work. We're to blame for you getting into trouble. And we'll try to fix the situation."),
        VoiceLine(20, Trent, ru="Это все хорошо, конечно, но что мне, собственно, делать сейчас?", en="That's all well and good, of course, but what am I actually supposed to do now?"),
        VoiceLine(30, DeltaOne, ru="Ведите себя тихо, пока можете выполнять контрактны на местных базах, но ни в коем случае не возвращайтесь в легальные системы.", en="Keep your head down. For now you can take contracts on the local bases, but under no circumstances go back to the lawful systems."),
        VoiceLine(40, DeltaOne, ru="А я пока постараюсь наладить связь со штабом СБА и выработать дальнейший план действий.", en="And I'll try to get in touch with ASF headquarters in the meantime and work out a further plan."),
        VoiceLine(50, DeltaOne, ru="В благодарность за вашу работу я сейчас переведу вам пять тысяч кредитов. Обещанное вознаграждение за миссию так же остается за вами и будет выплачено позже.", en="In thanks for your work, I'll transfer you five thousand credits now. The promised reward for the mission is still yours too, and will be paid later."),
        VoiceLine(70, Trent, ru="А как же компенсация за моральный ущерб?", en="And what about compensation for moral damages?"),
        VoiceLine(80, DeltaOne, ru="Будьте реалистом, мистер Трент. Сейчас больше стоит вопрос вашей жизни, а не лишних денег.", en="Be a realist, Mr. Trent. Right now it's more a question of your life, not extra money."),
        VoiceLine(90, DeltaOne, ru="Так что... как только появятся новости, мы с вами свяжемся.", en="So... as soon as there's news, we'll contact you."),
    ]


class Msn6Space(Msn6, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(
            0,
            HatcherStation,
            ru="Мистер Трент, я жду вас и вашего компаньона баре космопорта планеты Питтсбург, система Нью-Йорк.",
            en="Mr. Trent, I'm waiting for you and your companion at the spaceport bar on planet Pittsburgh, New York system.",
        ),
        VoiceLine(
            10,
            Hatcher,
            ru="Джентльмены, берем курс на линкор Миссури.",
            en="Gentlemen, we set course for the battleship Missouri.",
        ),
        VoiceLine(
            20,
            Trent,
            ru="Зная рейнландцев, они вокруг этой сферы и ученых наверняка военных на каждый астеорид понапихали, пригнали в систему линкор.",
            en="Knowing the Rheinlanders, they've surely stuffed soldiers onto every asteroid around this sphere and the scientists, and brought a battleship into the system.",
        ),
        VoiceLine(
            30,
            Hatcher,
            ru="Берите выше, мистер Трент, у них там развернута военная база.",
            en="Aim higher, Mr. Trent. They've got a military base deployed there.",
        ),
        VoiceLine(
            40,
            Trent,
            ru="Тогда, простите, каким образом мы с напарником должны будем с ними справиться? Вы выдадите нам карманную черную дыру?",
            en="Then, excuse me, how are my partner and I supposed to deal with them? Will you issue us a pocket black hole?",
        ),
        VoiceLine(
            50,
            Hatcher,
            ru="Нет, она еще проходит стендовые испытания. Я сейчас сброшу вам по контейнеру, подберите их и стыкуемся с Миссури. ",
            en="No, it's still undergoing bench tests. I'll drop you a container each now. Pick them up, and we dock with Missouri.",
        ),
        VoiceLine(
            55,
            HatcherStation,
            ru="Наши военные аналитики разработали стратегии выполнения задания. Эти стратегии уже загружены в ваши корабли. "
               "Можете воспользоваться при необходимости.",
            en="Our military analysts have developed strategies for carrying out the assignment. These strategies are already loaded into your ships. You can use them if necessary."
        ),
        VoiceLine(
            60,
            HatcherStation,
            ru="Удачи, джентльмены. Напоминаю, на территории Рейнланда никаких радиопереговоров со мной.",
            en="Good luck, gentlemen. I remind you, no radio contact with me in Rheinland territory.",
        ),
        VoiceLine(
            70,
            Alaric,
            ru="Трент, чтобы увеличить наши шансы, предлагаю разделиться. Встречаемся внутри Сферы.",
            en="Trent, to improve our chances, I suggest we split up. We meet inside the Sphere.",
        ),
        VoiceLine(
            80,
            SphereOutpost,
            ru="Подключен последний аванпост. Внешний периметр замкнут.",
            en="The last outpost is connected. The outer perimeter is closed.",
        ),
        VoiceLine(
            90,
            Alaric,
            ru="У нас получилось, Трент.",
            en="We did it, Trent.",
        ),
        VoiceLine(
            100,
            Trent,
            ru="Только теперь внешний периметр закрыт, и назад дороги нет.",
            en="Only now the outer perimeter is closed, and there's no way back.",
        ),
        VoiceLine(
            110,
            Alaric,
            ru="Трент, мы входим в зал в котором рейнландцы развернули лабораторию. Артефакты должны быть где-то внутри. ",
            en="Trent, we're entering the hall where the Rheinlanders have set up their laboratory. The artifacts should be somewhere inside.",
        ),
        VoiceLine(
            120,
            Alaric,
            ru="Попробуй пробраться внутрь через шлюзы и найти Роттермана, а я в это время попробую снять или хотя бы ослабить щиты.",
            en="Try to get inside through the airlocks and find Rotterman, and in the meantime I'll try to take down or at least weaken the shields.",
        ),
        VoiceLine(
            130,
            Trent,
            ru="Аларик, тут все задраено. Не пройти.",
            en="Alaric, it's all sealed up here. No way through.",
        ),
        VoiceLine(
            140,
            Alaric,
            ru="Трент, есть другой путь, через технические тоннели. Скидываю координаты.",
            en="Trent, there's another way, through the service tunnels. Sending coordinates.",
        ),
        VoiceLine(
            150,
            Trent,
            ru="Аларик, тут что-то непонятное. Какой-то кристалл, вокруг которого летают корабли Кочевников.",
            en="Alaric, there's something unclear here. Some kind of crystal, with Nomad ships flying around it.",
            cinematic=True,
        ),
        VoiceLine(
            160,
            Alaric,
            ru="По данным СБА этот кристалл назвали 'Номадским зерном'. Если кочевники тебя заметят, то из Зерна будут появляться все новые и новые истребители.",
            en="According to ASF data, this crystal was named the 'Nomad Seed'. If the Nomads notice you, more and more fighters will keep coming out of the Seed.",
            cinematic=True,
        ),
        VoiceLine(
            170,
            Alaric,
            ru="Выход должен находиться рядом, но он был автоматически закрыт после активации Зерна. Чтобы система безопасности разблокировала выход необходимо ликвидировать угрозу в этом зале, то есть уничтожить Зерно и все корабли кочевников. ",
            en="The exit should be nearby, but it was closed automatically after the Seed activated. For the security system to unlock the exit, you have to eliminate the threat in this hall, meaning destroy the Seed and all the Nomad ships.",
            cinematic=True,
        ),
        VoiceLine(
            180,
            Alaric,
            ru="Проблема в том, что если ты сильно нашумишь, наши рейнландские друзья могут перевозбудиться, поэтому действовать надо быстро.",
            en="The problem is, if you make too much noise, our Rheinland friends might get overexcited, so you have to act fast.",
            cinematic=True,
        ),
        VoiceLine(
            190,
            Trent,
            ru="Черт... Ладно, выключаю невидимость и уничтожаю Зерно.",
            en="Damn... All right, switching off invisibility and destroying the Seed.",
        ),
        VoiceLine(
            200,
            Alaric,
            ru="Трент, быстрее, рейнландцы почуяли неладное в этом зале, хотят направить к тебе оперативную группу.",
            en="Trent, faster. The Rheinlanders have sensed something wrong in this hall. They want to send a response team to you.",
        ),
        VoiceLine(
            210,
            Trent,
            ru="Охренеть. Это что же за адская машина?",
            en="Holy shit. What kind of hellish machine is this?",
        ),
        VoiceLine(
            220,
            SphereAssistant,
            ru="Финн, срочно летите к лаборатории! Поднимайте тревогу!",
            en="Finn, fly to the laboratory at once! Raise the alarm!",
        ),
        VoiceLine(
            225,
            Alaric,
            ru="Трент, ну сколько можно возиться? Присоединяйся, щиты уже основательно просели, им осталось недолго.",
            en="Trent, how long are you going to mess around? Join in. The shields have already dropped hard. They don't have long left.",
        ),
        VoiceLine(
            230,
            Alaric,
            ru="Дело в шляпе, уходим.",
            en="It's in the bag. Let's go.",
        ),
        VoiceLine(
            240,
            HatcherStation,
            ru="Джентльмены, для успешного завершения миссии осталось совсем немного. Линкор Миссури уже рядом со Сферой. Стыкуйтесь быстрее!",
            en="Gentlemen, very little is left for the mission to succeed. The battleship Missouri is already near the Sphere. Dock, faster!",
        ),
        VoiceLine(
            300,
            SphereMissouri,
            ru="Канонерки вышли на огневой рубеж!",
            en="The gunboats have reached firing range!",
        ),
        VoiceLine(
            310,
            SphereMissouri,
            ru="Внимание, канонерки сделали залп!",
            en="Attention, the gunboats have fired a salvo!",
        ),
        VoiceLine(
            320,
            HatcherStation,
            ru="Трент, Миссури не может совершить прыжок. Повреждены двигатели, требуется ремонт.",
            en="Trent, Missouri can't make the jump. The engines are damaged. Repairs are required.",
        ),
        VoiceLine(
            330,
            HatcherStation,
            ru="Здесь становится жарко. Вы с должны будете доставить артефакты на нашу базу в Сигма-17 сами. Я выделю вам для прикрытия звено Дельта.",
            en="It's getting hot here. You'll have to deliver the artifacts to our base in Sigma-17 yourselves. I'll assign Delta wing to cover you.",
        ),
        VoiceLine(
            340,
            Trent,
            ru="Понял вас, выдвигаюсь. Удачи вам здесь.",
            en="Understood. Moving out. Good luck to you here.",
        ),
        VoiceLine(
            350,
            HatcherStation,
            ru="Спасибо, Трент. Поверьте, вам она понадобится не меньше.",
            en="Thank you, Trent. Believe me, you'll need it no less.",
        ),
        VoiceLine(
            360,
            Alaric,
            ru="Трент, я останусь помогу тут.",
            en="Trent, I'll stay and help here.",
        ),
        VoiceLine(
            370,
            Trent,
            ru="И только попробуй мне тут помереть.",
            en="And just you try dying on me here.",
        ),
        VoiceLine(
            380,
            DeltaOne,
            ru="Лидер звена Дельта. Даю координаты прыжковой дыры в Сигма-17.",
            en="Delta wing leader. Giving the coordinates of the jump hole to Sigma-17.",
            cinematic=True,
        ),
        VoiceLine(
            390,
            OrderPilot,
            ru="Капитан Сид, цели успешно перехвачены.",
            en="Captain Ceed, targets successfully intercepted.",
            cinematic=True,
        ),
        VoiceLine(
            400,
            Ceed,
            ru="Фиксируйте их и доставьте на борт Навуходоносора.",
            en="Secure them and deliver them aboard the Nebuchadnezzar.",
            cinematic=True,
        ),
        VoiceLine(
            410,
            Trent,
            ru="Теперь бы еще понять где мы.",
            en="Now if we could just figure out where we are.",
        ),
        VoiceLine(
            420,
            DeltaOne,
            ru="Я знаю эту систему. Это Мальта. Территория Изгоев. Здесь есть свободный порт, куда пускают всех, кто смог до него добраться. Называется Фрипорт Тринидад. Там можно будет отсидеться. Вот координаты.",
            en="I know this system. This is Malta. Outcast territory. There's a free port here that lets in anyone who managed to reach it. It's called Freeport Trinidad. We can lie low there. Here are the coordinates.",
        ),
        VoiceLine(
            430,
            Trent,
            ru="Окей, идем туда.",
            en="Okay, let's go there.",
        ),
        VoiceLine(
            440,
            DeltaThree,
            ru="Командир, а вы не хотите направиться в более легальное место?",
            en="Commander, don't you want to head somewhere more lawful?",
        ),
        VoiceLine(
            450,
            DeltaOne,
            ru="В более легальном месте нас тут же возьмут под стражу за утрату артефактов и в лучшем случае обвинят в шпионаже. И хрен вы отмоетесь. ",
            en="In a more lawful place they'll take us into custody at once for losing the artifacts, and at best charge us with espionage. And there's no way in hell you'll wash that off.",
        ),
        VoiceLine(
            460,
            DeltaOne,
            ru="Улетело пять истребителей с артефактами. Вернулись живые все пятеро, но на одном истребителе и без артефактов. И никто в сказочки с Капитаном Сидом не поверит.",
            en="Five fighters left with the artifacts. All five came back alive, but on one fighter, and without the artifacts. And nobody will believe fairy tales about Captain Ceed.",
        ),

        VoiceLine(
            1010,
            Reitherman,
            ru="Финн, срочно летите на главную базу, у нас несанкционированный доступ!",
            en="Finn, fly to the main base at once. We have unauthorized access!",
        ),
        VoiceLine(
            1020,
            FinnRunner,
            ru="Неизвестный пилот, внимание, укажите свой идентификационный код.",
            en="Unknown pilot, attention, state your identification code.",
        ),
        VoiceLine(
            1030,
            FinnRunner,
            ru="Профессор, у нас несанкционированный доступ! Неизвестный корабль не отвечает! Включаю всеобщую тревогу!",
            en="Professor, we have unauthorized access! The unknown ship isn't responding! I'm sounding the general alarm!",
        ),
        VoiceLine(
            1040,
            FinnRunner,
            ru="Профессор, мой аванпост атакован неизвестным пилотом. Всеобщая тревога!",
            en="Professor, my outpost is under attack by an unknown pilot. General alarm!",
        ),
        VoiceLine(
            1050,
            FinnRunner,
            ru="Профессор, у нас несанкционированный доступ! В вашу зону направляется неизвестный корабль, спасайтесь! ",
            en="Professor, we have unauthorized access! An unknown ship is heading into your zone. Save yourself!",
        ),
        VoiceLine(
            1060,
            FinnRunner,
            ru="Двери не работают... Всему персоналу, всеобщая тревога! Несанкционированный доступ!",
            en="The doors aren't working... All personnel, general alarm! Unauthorized access!",
        ),
        VoiceLine(
            1100,
            SphereOutpost,
            ru="Патруль Омега-4, это станция Гамбург. Обнаружены неполадки на одном из телескопов. Осмотр+ите его, возможно разрядился генератор.",
            en="Patrol Omega-4, this is Hamburg station. Malfunctions detected on one of the telescopes. Inspect it. The generator may have discharged.",
        ),
        VoiceLine(
            1200,
            Hatcher,
            ru="Мы получили попадание торпедой!",
            en="We’ve been hit by a torpedo!",
        ),
        VoiceLine(
            1210,
            Hatcher,
            ru="Повреждения критические! Миссури срочно требуется поддержка! Всем истребителям, приказ перехватить торпеды!",
            en="Damage is critical! Missouri urgently needs support! All fighters, order to intercept the torpedoes!",
        ),
        VoiceLine(
            1220,
            SphereMissouri,
            ru="Канонерки израсходовали боеприпасы и покидают поле битвы. Миссури в безопасности.",
            en="The gunboats have used up their ammunition and are leaving the battlefield. Missouri is safe.",
        ),

    ]


class Mission6(Msn6, script.StoryMission):
    MISSION_INDEX = 6
    CUTSCENES = [
        Msn6Offer,
        Msn6Briefieng,
        Msn6Mount,
        Msn6LabLand,
        Msn6LabRoom,
        Msn6TorpedoAlert,
        Msn6OrderDeck,
        Msn6Prison,
        Msn6Freeport,
    ]
    SPACE_CLASS = Msn6Space
    SYNC_SPACE = True
    SYNC_SUBS = True

    MISSION_TITLE = 'Миссия 6. Вход в Сферу'