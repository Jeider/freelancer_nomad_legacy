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
        VoiceLine(10, Trent, ru="Мисс Хетчер. Аларик, не ожидал, что ты уже здесь.", en="Miss Hatcher. Alaric, I didn't expect to see you here already!"),
        VoiceLine(20, Alaric, ru="Как только ты со мной связался, я сразу же прибыл к мисс Хетчер. Видимо, я был ближе к Нориджу, чем ты.", en="I flew to see Miss Hatcher right away as soon as she contacted me. Looks like I was closer to Norwich than you were."),
        VoiceLine(30, Hatcher, ru="А теперь, господа, когда все выяснили когда, откуда и каким образом мы все сюда прибыли, перейдем к делу? ... ", en="Gentlemen, now that we're all caught up with our travel itineraries, shall we get down to business?"),
        VoiceLine(40, Hatcher, ru="Отлично! Как вы уже поняли есть некий объект - Сфера. В свое время его обнаружил еще Орден, но тогда никто не смог понять что это, для чего предназначено и как работает. И про Сферу забыли. ", en="So, to recap, you both remember the alien artefact we call The Sphere. Originally discovered by The Order, it was one of a very few active, and by far the largest and most complex artefact ever discovered. Naturally, it generated immense... interest amongst the houses. Everyone tried claim a stake in it. However despite the best efforts to crack it, it remained an inscrutable and eventually uncrackable puzzle. Left to rot."),
        VoiceLine(50, Hatcher, ru="А теперь мы узнаём что рейнландцам удалось подобрать к ней ключ и они проводят на ней свои исследования. Есть обоснованное мнение, что ничем хорошим это не закончится. Поэтому исследования эти нужно, как бы это сказать... закрыть.", en="However, thanks to Jacobo's misappropriated documents, we've learnt that the Rheinlanders are on the cusp of figuring out the technology required to to communicate with it, and are currently working on it even as we speak. Based on his readings, Professor Mandrake believes that the Sphere is a shuttered gateway to another system housing hostile beings wielding such unimagineable power even the creators were terrified of them. We need your help to stop the Rhinelanders before they activate the sphere and re-open the portal."),
        VoiceLine(60, Trent, ru="Ха-ха-ха, отлично. Если вы не смогли подобрать к Сфере ключ сами, то никто не должен. А если подобрал, то нужно срочно устранить либо ключ, либо Сферу, либо того кто это сделал. Браво! Так не доставайся же ты никому.", en="Ha-ha-ha! Perfect. So, if you guys can't work out the Sphere, then no one else can! And if someone else gets to it first, then either the key or The Sphere itself has to go. Bravo! This way no one will ever get in there."),
        VoiceLine(70, Hatcher, ru="Я не разделяю вашего сарказма, мистер Трент. В прошлый раз подобная ситуация случилась, когда другие рейнландские ученые нашли нечто в Омикронах. Ох уж мне эти неугомонные рейнландцы.", en="I don't appreciate you sarcasm, Mr. Trent. Remember, it's already happened once, when the other group of Rheinland scientists blundered into the Nomads in Omicron sector... Oh, how I despise these meddlesome Rheinlanders..."),
        VoiceLine(80, Hatcher, ru="И все закончилось тем самым кризисом, про который я вам рассказывала в присутствие профессора Мандрейка. Вы поняли, о чем я?", en="It escalated into the crisis we spoke about with Prof. Mandrake. You get the idea, right?"),
        VoiceLine(90, Trent, ru="Да, понял. Не стоит шутить с ящиком Пандоры.", en="Yeah, I get it. Pandora's Box."),
        VoiceLine(100, Hatcher, ru="Хорошо, с моральной подоплекой наших действий мы разобрались, теперь про материальную. Вы получите вознаграждение втрое больше обычного, и удостоверения внештатных сотрудников СБА. ", en="Very well. For this mission you’ll both be receiving triple the usual payout, and elevated to official partners of the ASF."),
        VoiceLine(110, Alaric, ru="Чёрт побери, я за! Где ставить подпись? Могу кровью!", en="Hell yeah, I'm in! Where do I sign? I'll sign in blood if needed!"),
        VoiceLine(120, Trent, ru="Аларик, угомонись. Мисс Хетчер, а что конкретно нужно сделать? Уничтожить Сферу, уничтожить ученых? Мне это совсем не по душе, я всё-таки не наёмный убийца.", en="Calm down, Alaric. Miss Hatcher, what exactly is the objective? Destroy The Sphere? Kill the scientists? I can’t just murder on a dime - I'm a lover, not a killer."),
        VoiceLine(130, Hatcher, ru='А вы уверены? Нет, все не так страшно и кроваво, как вы сейчас расписали. В полученных нами документах профессор нашел способ сделать Сферу невосприимчивой к внешним воздействиям, как сказал профессор "закрыться". ', en="Oh, is that so? I had no idea. Professor Mandrake thinks he's worked out a way to render The Sphere inert to external influences."),
        VoiceLine(140, Hatcher, ru="Все дальнейшие подробности - в том случае, если вы согласитесь.", en="I'll provide the full details, but only if you accept this mission."),
        VoiceLine(150, Trent, ru='У меня дежавю. Вот только в прошлый раз меня называли не "мистер Трент", а "герр Трент"... С другой стороны, временами было весело... Хорошо, я в деле.', en="I'm having a de-ja-vu moment. Only last time, I was called \"Herr Trent\", not \"Mr. Trent\"... On the other hand, I can't say it was boring. Alright, count us in."),
        VoiceLine(160, Hatcher, ru="Тогда встретимся на орбите и продолжим разговор там.", en="Then I'll meet you both in orbit; we'll continue our conversation there."),
    ]


class Msn6Briefieng(Msn6, script.CutsceneProps):
    ALIAS = 'briefing'
    TITLE = 'Брифинг'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Hatcher, ru="Итак, джентльмены, главная задача - ликвидировать рейнландского ученого, профессора Роттермана.", en="Alright, gentlemen, our primary objective is the termination of a Rheinland scientist named Professor Rotterman."),
        VoiceLine(20, Trent, ru="Черт, я так и думал.", en="Called it."),
        VoiceLine(30, Hatcher, ru="Не перебивайте, Трент!  Думал он. Может быть, вы также думали, что за такой гонорар вам поручат доставку суши? ", en="“Called it?” … You were hoping for a moonlit walk on the beach?"),
        VoiceLine(40, Hatcher, ru="Пора взрослеть, мистер Трент. ", en="Grow up, Mr. Trent. Everything is on the line. We must do what needs to be done, morals and ethics be damned."),
        VoiceLine(50, Hatcher, ru="Итак, ликвидируете профессора Роттермана и забираете два артефакта - кристалл кочевников и том Протея, они должны находиться либо у профессора, либо рядом с ним.", en="Your secondary objective is to secure the two alien artifacts crucial for communicating with the Sphere: the Nomad Crystal and the Proteus Tome. They should be in Professor Rotterman's posession, or at least close by."),
        VoiceLine(60, Hatcher, ru="В свое время они хранились в одном из тайников Ордена, но в так называемые смутные времена следы их потерялись.", en="These artifacts were once kept secure by The Order, but during the \"Chaotic\" time of the Schism, they were misplaced."),
        VoiceLine(70, Hatcher, ru="Вы забираете артефакты, увозите их и Сфера закрывается.", en="According to Professor Mandrake all we have to do to deactivate the Sphere is to remove the artefacts from its vicinity."),
        VoiceLine(80, Alaric, ru="Орден? Смутные времена?", en="The Order? \"Chaotic\" times? Schism?"),
        VoiceLine(90, Trent, ru="Позже, Аларик.", en="I'll fill you in later, Alaric. It's a lot to take in."),
        VoiceLine(100, Hatcher, ru="Хватит, чёрт побери, меня перебивать, мы сейчас обсуждаем важнейшую миссию! ", en="Guys, stop interrupting me! We're wasting time!"),
        VoiceLine(110, Trent, ru="Самую важную в вашей жизни, мисс Хетчер? Не забывайте что конкретные исполнители - мы, и вот как исполнители мы хотели бы подробностей о предшествующих ликвидации профессора этапах. ", en="Respectfully, Miss Hatcher, Alaric and I are putting our lives on the line. We deserve to know ALL the details - no nasty surprises, especially if you want us to succeed."),
        VoiceLine(120, Hatcher, ru="Хорошо, Трент. Итак, проникновение внутрь Сферы. Охраняется она беспрецедентно. Я сомневаюсь, что кайзер Рейнланда охраняется так же как она. ", en="Point taken. Ok, firstly, getting inside the complex housing The Sphere isn't going to be easy. It's locked down tight - there's more security swarming over that place than the Kaiser’s palace."),
        VoiceLine(130, Hatcher, ru="Рядом со сферой находится военная база, представляющая собою верфь, способную принимать по два линкора и четыре корабля среднего тоннажа одновременно. Понимаете, какая там развернута группировка? Поэтому силовое решение невозможно. ", en="Secondly, there's a massive shipyard set up practically on top of The Sphere; intel indicates two battleships and four mid-sized vessels at the least. A brute force approach isn't going to work."),
        VoiceLine(140, Hatcher, ru="Для проникновения вам понадобятся устройства, которые находятся в контейнерах, переданных мною вам перед стыковкой с Миссури. Это устройства, делающие ваши корабли невидимыми как визуально, так и всеми радарными системами. ", en="We're providing you with some prototype cloaking devices the Order has been developing which should turn your ships invisible to radar and vision."),
        VoiceLine(150, Hatcher, ru="Они создают вокруг корабля локальное искривление пространства, и ваши корабли как бы перестают находиться в нашей реальности. ", en="They work by warping the curvature of space around your ships, essentially phasing your ships into a parallel universe for a while."),
        VoiceLine(160, Hatcher, ru="Смонтируете их у себя на кораблях - просто устанавливаете где-нибудь внутри герметичного корпуса, подключаете к энергосистеме и выводите кнопку управления в удобное место приборной доски. Кнопка всего одна, не ошибетесь. ", en="Installation is simple: hook them up behind your seats, plug the big power cable into your power generator, and run the small control cable to your HUD interface. There's just one on / off button - even you stable geniuses should be able to figure it out."),
        VoiceLine(170, Hatcher, ru="Нажимаете один раз - и ваш корабль невидим, нажимаете второй раз - и он снова видим. Проблема устройства в его одноразовости. ", en="Press once to cloak. Press again and to decloak."),
        VoiceLine(180, Hatcher, ru="Я не ученый, поэтому скажу просто, после выключения там что-то перегорает, и оно превращается в коробочку с горелым пластиком и обугленным  металлом. ", en="Be warned that the cloak technology is still unstable, and unfortunately single-use. So after 30 minutes, or after deactivation, you're done for good."),
        VoiceLine(190, Trent, ru="Огнетушителями запасаться? ", en="Unstable? Done for good? Does it self destruct or something? Can't we just steal Rheinland cloaking tech?"),
        VoiceLine(200, Hatcher, ru="Нет, все безопасно, все происходит внутри устройства, даже неприятного запаха не появится. ", en="Where do you think we got the blueprints from. You don't want to know what happens when Rhineland cloaks overheat. Don't worry, ours just melt down a little. You'll be okay."),
        VoiceLine(210, Hatcher, ru="По времени работы. Поскольку устройство одноразовое, постарайтесь использовать его максимально эффективно. Наши головастики гарантируют тридцать минут работы. Возможно, оно проработает сорок, больше вряд ли. ", en="Before any wisecracks about hot asses, you'll barely feel the heat. The devices have elaborate cooling systems that keep fire risk at a minimum."),
        VoiceLine(220, Hatcher, ru="Если тридцати минут работы не хватило, вы можете попробовать оставаться в невидимости дольше на свой страх и риск. Если устройство сгорит не во время выключения, а во время работы, локальное искривление пространства схлопывается вместе с кораблём. ", en="If 30 minutes isn't enough, you can opt to maintain the cloak, but at your own risk. Theoretically, if you fail to deactivate the device in time and your ship is still in warped space, you could remain stuck there..."),
        VoiceLine(230, Alaric, ru="И куда попадает корабль? В другое измерение? ", en="In the other dimension?"),
        VoiceLine(240, Hatcher, ru="Понятия не имею. Хотите узнать, мистер Аларик? По глазам вижу, что нет. И да, еще один момент. При включенном устройстве стрелять бесполезно. Выши выстрелы не покинут локальную зону искривления пространства.", en="We don't know, Alaric. Perhaps you could find out and send us a postcard? Oh, and one last thing: you can't shoot while cloaked. Your projectiles won't be able to escape the bubble of distorted space."),
        VoiceLine(250, Hatcher, ru="Вот трехмерный план Сферы и все данные по ней, которые нам удалось собрать.", en="Here is a 3D map of The Sphere from our intelligence agents."),
        VoiceLine(260, Alaric, ru="Вот это хреновина...", en="Wow, just look at the size of it..."),
        VoiceLine(270, Hatcher, ru="Я рада, что вы прониклись, мистер Аларик. Загрузите всё к себе в компьютер. В ходе операции будете передавать нужные данные мистеру Тренту. ", en="That's what she said. Great now you've got me doing it. Please upload the data into your computer. You’ll be relaying it, and all updates to Trent throughout the mission."),
        VoiceLine(280, Hatcher, ru="Ну и последнее - после прибытия на территорию Рейнланда никаких радиопереговоров со мной или с кем-то еще на территории Либерти. Вас запеленгуют их радарные станции, и миссия завершится так и не начавшись. ", en="Lastly, after you arrive in Rheinland, you are to maintain strict radio silence. If you so much as squeak they'll be all over you and the mission will fail before it even gets started."),
        VoiceLine(290, Hatcher, ru="Вот, собственно, и всё. По коням, джентльмены.", en="Okay, that's it. Mount up, gentlemen."),
    ]


class Msn6Mount(Msn6, script.CutsceneProps):
    ALIAS = 'mount'
    TITLE = 'Установка устройства'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Trent, ru="У тебя редкий талант постоянно влипать в неприятности, Аларик.", en="You have a real talent for getting us into sticky situations, Alaric."),
        VoiceLine(20, Alaric, ru="Ты о чем? ", en="What do you mean?"),
        VoiceLine(30, Trent, ru="О том что с нами будет происходить в ближайшем будущем.", en="You know."),
        VoiceLine(40, Alaric, ru="Ты про нашу миссию?", en="Are you talking about the mission?"),
        VoiceLine(50, Trent, ru="Про нашу СУИЦИДАЛЬНУЮ миссию.", en="Yeah, SUICIDE mission."),
        VoiceLine(60, Alaric, ru="Зато какие выгоды в случае успеха! К тому же ты мог бы отказаться.", en="Think of the paycheck!!! 'sides, you could've said \"no\" at any time."),
        VoiceLine(70, Trent, ru="Боюсь, если бы я отказался, то уже летал бы в космосе без скафандра.", en="I was afraid if I said \"no\", I'd end up flying in space without a spacesuit."),
        VoiceLine(80, Alaric, ru="Трент, раз уж мы подписались, надо выполнять. Давай, Трент, полетели. Обещаю, в следующий раз заказчика будешь выбирать ты.", en="Yeah. Hatcher scares me too. Come on, Trent, let’s just do it. Next time round I’ll let you choose the contract, I promise."),
        VoiceLine(90, Trent, ru="Если он будет, этот следующий раз. ", en="Assuming there’s a \"next time\". I got a bad feeling about this one."),
    ]


class Msn6LabLand(Msn6, script.CutsceneProps):
    ALIAS = 'lab_land'
    TITLE = 'Посадка на лабораторию'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Alaric, ru="Трент, у нас мало времени. Я уже установил взрывчатку с таймером обратного отсчета.", en="Trent, we don't have much time. The bomb is already ticking."),
        VoiceLine(20, Trent, ru="Мы же хотели просто закрыть сферу?", en="Bomb? I thought we were going to deactivate the sphere, not blow it up!"),
        VoiceLine(30, Alaric, ru="Вот мы и закроем. Хетчер решила подстраховаться. Мы уничтожим лабораторию.", en="That's plan A. But if Plan A doesn't work out... well now you know Hatcher's fallback plan."),
        VoiceLine(40, Trent, ru="Ясно.", en="Thanks a lot. Makes me feel all warm and toasty."),
    ]


class Msn6LabRoom(Msn6, script.CutsceneProps):
    ALIAS = 'lab_room'
    TITLE = 'Лаборатория'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Trent, ru="Обалдеть…", en="Holy crap, look at that..."),
        VoiceLine(20, Alaric, ru="Трент, бежим! Потом рассмотришь.", en="Trent we need to skedaddle! You can play with it later!!"),
    ]


class Msn6TorpedoAlert(Msn6, script.CutsceneProps):
    ALIAS = 'torpedo_alert'
    TITLE = 'Торпедная тревога'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Hatcher, ru="Трент, у нас критическая ситуация! Рейнландцы выпустили против Миссури торпедные канонерки. ", en="Trent, we have an emergency! Rheinland gunboats just fired a spread of torpedoes at Missouri."),
        VoiceLine(20, Hatcher, ru="Мы не успеваем запустить гипердвигатель, а системы ПВО линкора не смогут перехватить все выпущенные торпеды. ", en="Our hyperdrive isn't spooled up yet and our defense systems won't be able to handle all the torpedoes."),
        VoiceLine(40, Trent, ru="Но сначала нужно выгрузить артефакты.", en="But don't we need to unload the artifacts first..."),
        VoiceLine(50, Hatcher, ru="В данной ситуации они большей безопасности у вас на борту, а не на Миссури. Вылетайте! Быстрее!", en="Save lives first! Artefacts later!! Get on it!!"),
    ]


class Msn6OrderDeck(Msn6, script.CutsceneProps):
    ALIAS = 'order_deck'
    TITLE = 'Стыковочный узел Навухудоносора'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, OrderPilot, ru="Капитан Сид, мы обнаружили артефакты на борту этого фриленсера.", en="Captain Ceed, we've found the artifacts present and intact in the Freelancer's cargo hold."),
        VoiceLine(20, Ceed, ru="Отлично. Спасибо за работу, ребята. Артефакты – на склад, пленных – в кают-компанию.", en="Excellent work, guys. You bring the artifacts to storage. We'll escort the prisoners to the brig."),

    ]


class Msn6Prison(Msn6, script.CutsceneProps):
    ALIAS = 'order_prison'
    TITLE = 'Тюремная камера'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Ceed, ru="Вольно, рядовой. Идите в диспетчерскую, пусть подготовят корабль для доставки пленных на нашу базу. А я пока начну допрос.", en="At ease, soldier. Head on up to the control room and tell them to issue a transport. We need to deliver these prisoners to base. In the meantime, I'll start interrogating them."),
        VoiceLine(20, OrderGuard, ru="Сэр, но если...", en="Sir, but what if..."),
        VoiceLine(30, Ceed, ru="Никаких если. На них же шокеры, пусть только попробуют рыпнуться.", en="Relax. They're wearing shock collars - they won't dare try anything."),
        VoiceLine(40, OrderGuard, ru="Есть, сэр.", en="Immediately, sir."),
        VoiceLine(50, Ceed, ru="Спокойно, джентльмены, я не кусаюсь. Вам повезло, что все произошло во время моего дежурства.", en="Don't worry, lads, I'm on your side. Count your lucky stars I was on duty."),
        VoiceLine(60, Ceed, ru="Забыл представиться. Хари Сид, капитан Ордена, лейтенант СБА, работаю тут под прикрытием.", en="Forgot to introduce meself. Ceed, Harry Ceed, Order Captain by day. ASF Lieutenant by night. Double agent. Spy extraordinaire."),
        VoiceLine(65, Ceed, ru="Сейчас подождем некоторое время, а потом я помогу вам покинуть негостеприимный борт Навуходоносора", en="We're just going to kick our heels up for a while, and when the time is right I'll sneak you off the Nebuchadnezzar."),
        VoiceLine(70, DeltaThree, ru="Сдается мне, ребята, что это очередная провокация Ордена, и выведет нас этот милый капитан на шеренгу бойцов со штурмовыми винтовками.", en="Do you guys get the feeling this is just another Order trick to get us in the line of hostile fire..."),
        VoiceLine(80, DeltaOne, ru="А у тебя что, есть предложения получше? В любом случае, лучше на шеренгу бойцов с винтовками, чем на допрос к специалистам Ордена.", en="You got a better idea? I dunno about you but I'd rather take my chances getting shot at on the run than being interrogated here by these guys."),
        VoiceLine(90, Trent, ru="А что там с артефактами, капитан?", en="Captain, what about the artifacts?"),
        VoiceLine(100, Ceed, ru="Летят на базу Ордена.", en="They're being transported to an Order base."),
        VoiceLine(110, DeltaOne, ru=" И вы позволили?", en="Isn't ASF going to hold you to task for letting that happen?"),
        VoiceLine(120, Ceed, ru="А что я, по-вашему, должен был сделать? Если бы я начал вставлять Ордену палки в колеса, то сидел бы тут с вами, только не с сигаретой в руке, а с таким же милым ошейником на шее как у вас.", en="Got it all covered, along with your escape plan."),
        VoiceLine(130, Trent, ru="А как вы собираетесь помочь нам бежать?", en="Okay, so, what’s our escape plan?"),
        VoiceLine(140, Ceed, ru="Для начала вы примерите вот это...", en="Step one, put these civilian clothes on"),
        VoiceLine(145, Ceed, ru="А потом спокойно и небрежно проследуете в ангар к кораблю мистера Трента. ", en="Step two, follow me to Mr. Trent’s ship in the hanger. Act natural."),
        VoiceLine(150, Ceed, ru="К сожалению, все остальные уже разбирают на запчасти. А вот корабль Трента пока еще в целости и сохранности. Так что, как говорится, в тесноте, да не в обиде.", en="Unfortunately, all your other ships have been stripped for parts already. Luckily, they haven't gotten to Mr Trent's ship yet."),
        VoiceLine(160, Trent, ru="А после нашего побега... Как это скажется на вас? Вы не будете сидеть здесь не с сигаретой в руке, а с ошейником как у нас на шее?", en="What's step three? How're you getting out of this?"),
        VoiceLine(170, Ceed, ru="О, нет. Вы же меня вырубили, этому найдутся неоспоримые доказательства. ", en="Step three. Rough me up and knock me out. I'll tell them you overpowered me and escaped."),
        VoiceLine(180, Ceed, ru="К тому же, что такое побег пленников в сравнении с тем, что я передал в руки  Ордена артефакты, за которыми охотится весь сектор Сириуса.", en="They're not going to divert significant resources to chase down a few escaped prisoners with those precious artefacts in transit."),
        VoiceLine(190, Trent, ru="Толково, не поспоришь. ", en="Clever. Clever spy."),

    ]


class Msn6Freeport(Msn6, script.CutsceneProps):
    ALIAS = 'freeport'
    TITLE = 'Фрипорт'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, DeltaOne, ru="Мистер Трент, Хочу вас поблагодарить за проделанную работу. Прошу извинить нас за то, что попали в неприятности по нашей вине, и я обещаю, что сделаю все возможное, чтобы восстановить вашу репутацию.", en="Mr. Trent, I'd like to thank you for all the help. Please accept our apologies for dragging you into such a dangerous situation, and I promise that I'll do everything I can to restore your reputation with Liberty when we can."),
        VoiceLine(20, Trent, ru="Это все хорошо, конечно, но что мне, собственно, делать сейчас?", en="Well that's all fine and dandy, but what do I do now?"),
        VoiceLine(30, DeltaOne, ru="Ведите себя тихо, принимайте контракты на этом фрипорте, в других независимых или пиратских системах, но ни в коем случае не возвращайтесь в легальные системы.", en="Keep a low profile. Feel free to work a few jobs here on this freeport, or any other independent stations, or hell, possibly even work for the pirates. But under no circumstances return to lawful space."),
        VoiceLine(40, DeltaOne, ru="Если вас там задержат, мы будем бессильны что-то с этим сделать. А вас превратят в козла отпущения.", en="If you're caught there, we won't be able to help you. You'll be turned into a scapegoat and executed. Or worse."),
        VoiceLine(50, DeltaOne, ru="А сейчас мне нужно выйти на связь со штабом СБА, обсудить создавшуюся ситуацию и выработать дальнейший план действий. ", en="I need to contact ASF headquarters right away to discuss the situation and develop an action plan."),
        VoiceLine(60, DeltaOne, ru="В благодарность за вашу работу я перевожу вам со своего счета пять тысяч кредитов. Кроме того, вознаграждение за предыдущую миссию остается за вами, и как только мы разрешим эту ситуацию, вы его получите.", en="As a token of our gratitude, I'm transferring you 5,000 credits from my personal account. Additionally, the promised reward from this mission still stands, and you should receive it as soon as our situation is resolved."),
        VoiceLine(70, Trent, ru="А как же компенсация за моральный ущерб?", en="And what about compensation for all the emotional damage?"),
        VoiceLine(90, DeltaOne, ru="Мистер Трент, вы никогда не производили впечатление жадного человека. Вы достаточно долго и успешно действуете в непростых ситуациях. ", en="Mr. Trent, I'm pretty sure whatever emotional damage you had was pre-existing.... Frankly speaking, you've been extraordinarily calm, precise and reliable throughout this entire mission. You strike me as a professional, paid his weight in gold for the quality of his work, and proud of it."),
        VoiceLine(100, DeltaOne, ru="А вот жадные люди, я слышал, долго не живут... Как только появятся новости, я свяжусь с вами, мистер Трент.", en="Don't make me think you're a greedy person... greedy people live much shorter lives, in my experience... I'll be in touch once I’ve got news. Stay safe."),
    ]


class Msn6Space(Msn6, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(
            0,
            HatcherStation,
            ru="Мистер Трент, я жду вас и вашего компаньона баре космопорта планеты Питтсбург, система Нью-Йорк.",
            en="Mr. Trent, I'm waiting for you and your companion on Planet Pittsburg in the New-York System..",
        ),
        VoiceLine(
            10,
            Hatcher,
            ru="Джентльмены, берем курс на линкор Миссури.",
            en="Gentlemen, please set course to Battleship Missouri.",
        ),
        VoiceLine(
            20,
            Trent,
            ru="Зная рейнландцев, они вокруг этой сферы и ученых наверняка военных на каждый астеорид понапихали, пригнали в систему линкор.",
            en="Knowing how Rheinland operates, they've probably got guards posted around the Sphere, and maybe even a battleship waiting to swoop in.",
        ),
        VoiceLine(
            30,
            Hatcher,
            ru="Берите выше, мистер Трент, у них там развернута военная база.",
            en="That's an understatement, Mr. Trent. In fact, they have a fully deployed military base there with at least two battleships.",
        ),
        VoiceLine(
            40,
            Trent,
            ru="Тогда, простите, каким образом мы с напарником должны будем с ними справиться? Вы выдадите нам карманную черную дыру?",
            en="Excuse me, but how exactly do you expect my wingman and me to deal with that kind of firepower? Do you have a pocket black hole to spare?",
        ),
        VoiceLine(
            50,
            Hatcher,
            ru="Нет, она еще проходит стендовые испытания. Я сейчас сброшу вам по контейнеру, подберите их и стыкуемся с Миссури. ",
            en="No, we're still working out the kinks on that one. I'll drop a few goodies for you, tractor them in and dock with Missouri.",
        ),
        VoiceLine(
            55,
            HatcherStation,
            ru="Наши военные аналитики разработали стратегии выполнения задания. Эти стратегии уже загружены в ваши корабли. "
               "Можете воспользоваться при необходимости.",
            en="Our military analysts have prepared special mission strategies just for you. These strategies have been uploaded to "
               "your neuralnets. You should consider using them."
        ),
        VoiceLine(
            60,
            HatcherStation,
            ru="Удачи, джентльмены. Напоминаю, на территории Рейнланда никаких радиопереговоров со мной.",
            en="Best of luck, gentlemen. And remember – maintain strict radio silence once you're in Rheinland.",
        ),
        VoiceLine(
            70,
            Alaric,
            ru="Трент, чтобы увеличить наши шансы, предлагаю разделиться. Встречаемся внутри Сферы.",
            en="Trent, we’ll stand a better chance if we split up. I'll meet up with you inside the sphere.",
        ),
        VoiceLine(
            80,
            SphereOutpost,
            ru="Подключен последний аванпост. Внешний периметр замкнут.",
            en="Last outpost is operational. External perimeter is locked down.",
        ),
        VoiceLine(
            90,
            Alaric,
            ru="У нас получилось, Трент.",
            en="We made it, Trent!",
        ),
        VoiceLine(
            100,
            Trent,
            ru="Только теперь внешний периметр закрыт, и назад дороги нет.",
            en="Except the outer perimeter is locked down, so now there's no way back.",
        ),
        VoiceLine(
            110,
            Alaric,
            ru="Трент, мы входим в зал в котором рейнландцы развернули лабораторию. Артефакты должны быть где-то внутри. ",
            en="Trent, we're entering the chamber where the Rheinlanders have deployed their lab. The artifacts should be somewhere inside.",
        ),
        VoiceLine(
            120,
            Alaric,
            ru="Попробуй пробраться внутрь через шлюзы и найти Роттермана, а я в это время попробую снять или хотя бы ослабить щиты.",
            en="Try sneaking in through the airlock and locate Rotterman, while I try to take down or compromise the shields.",
        ),
        VoiceLine(
            130,
            Trent,
            ru="Аларик, тут все задраено. Не пройти.",
            en="Alaric, the airlock is sealed. I can't get through.",
        ),
        VoiceLine(
            140,
            Alaric,
            ru="Трент, есть другой путь, через технические тоннели. Скидываю координаты.",
            en="Trent, they've overlooked a nearby maintenance vent. You should just be able to squeeze through. I'm sending you the coordinates.",
        ),
        VoiceLine(
            150,
            Trent,
            ru="Аларик, тут что-то непонятное. Какой-то кристалл, вокруг которого летают корабли Кочевников.",
            en="Alaric, there's some kind of crystal surrounded by a swarm of Nomad ships in here.",
            cinematic=True,
        ),
        VoiceLine(
            160,
            Alaric,
            ru="По данным СБА этот кристалл назвали 'Номадским зерном'. Если кочевники тебя заметят, то из Зерна будут появляться все новые и новые истребители.",
            en="ASF intel calls it the 'The Nomad Seed'. It's a gate to a pocket dimension. If the Nomads sense your presence they'll start swarming out of it.",
            cinematic=True,
        ),
        VoiceLine(
            170,
            Alaric,
            ru="Выход должен находиться рядом, но он был автоматически закрыт после активации Зерна. Чтобы система безопасности разблокировала выход необходимо ликвидировать угрозу в этом зале, то есть уничтожить Зерно и все корабли кочевников. ",
            en="The exit is around here somewhere, but was automatically sealed after the Seed activated. In order to unseal it, you'll need to eliminate all the threats:",
            cinematic=True,
        ),
        VoiceLine(
            180,
            Alaric,
            ru="Проблема в том, что если ты сильно нашумишь, наши рейнландские друзья могут перевозбудиться, поэтому действовать надо быстро.",
            en="The only problem is, if you make too much noise, our Rheinland friends will join the party. So, you have to act quickly. Destroy the Seed first.",
            cinematic=True,
        ),
        VoiceLine(
            190,
            Trent,
            ru="Черт... Ладно, выключаю невидимость и уничтожаю Зерно.",
            en="Dammit... Alright, powering off cloak and starting my run.",
        ),
        VoiceLine(
            200,
            Alaric,
            ru="Трент, быстрее, рейнландцы почуяли неладное в этом зале, хотят направить к тебе оперативную группу.",
            en="Trent, hurry up! The Rheinlanders are beginning to suspect something’s up in the chamber. They about to send a group of scouts over.",
        ),
        VoiceLine(
            210,
            Trent,
            ru="Охренеть. Это что же за адская машина?",
            en="Holy shit! What the hell is this monstrosity?",
        ),
        VoiceLine(
            220,
            SphereAssistant,
            ru="Финн, срочно летите к лаборатории! Поднимайте тревогу!",
            en="Finn, get to the lab immediately! Sound the alarm!",
        ),
        VoiceLine(
            225,
            Alaric,
            ru="Трент, ну сколько можно возиться? Присоединяйся, щиты уже основательно просели, им осталось недолго.",
            en="Trent, what's taking you so long? Come quickly, the shields are almost down - anytime now.",
        ),
        VoiceLine(
            230,
            Alaric,
            ru="Дело в шляпе, уходим.",
            en="It's finished. Let's get out of here.",
        ),
        VoiceLine(
            240,
            HatcherStation,
            ru="Джентльмены, для успешного завершения миссии осталось совсем немного. Линкор Миссури уже рядом со Сферой. Стыкуйтесь быстрее!",
            en="Gentlemen, we're pulling out. Battleship Missouri is approaching the Sphere. Proceed to dock, quickly!",
        ),
        VoiceLine(
            300,
            SphereMissouri,
            ru="Канонерки вышли на огневой рубеж!",
            en="Gunships at firing range.",
        ),
        VoiceLine(
            310,
            SphereMissouri,
            ru="Внимание, канонерки сделали залп!",
            en="Ready, set... fire!",
        ),
        VoiceLine(
            320,
            HatcherStation,
            ru="Трент, Миссури не может совершить прыжок. Повреждены двигатели, требуется ремонт.",
            en="Trent, Missouri won't be able to make the jump. Its engines are damaged and need repairs.",
        ),
        VoiceLine(
            330,
            HatcherStation,
            ru="Здесь становится жарко. Вы с должны будете доставить артефакты на нашу базу в Сигма-17 сами. Я выделю вам для прикрытия звено Дельта.",
            en="It's getting too hot here. I'll cover them while they withdraw. You have to deliver these artifacts to our base in Sigma-17 without me. Delta wing will escort you.",
        ),
        VoiceLine(
            340,
            Trent,
            ru="Понял вас, выдвигаюсь. Удачи вам здесь.",
            en="Acknowledged, moving out. Good luck and stay safe.",
        ),
        VoiceLine(
            350,
            HatcherStation,
            ru="Спасибо, Трент. Поверьте, вам она понадобится не меньше.",
            en="Thanks Trent. Godspeed.",
        ),
        VoiceLine(
            360,
            Alaric,
            ru="Трент, я останусь помогу тут.",
            en="Trent, I'm staying here to help Hatcher.",
        ),
        VoiceLine(
            370,
            Trent,
            ru="И только попробуй мне тут помереть.",
            en="Stay alive, OK? You owe me money.",
        ),
        VoiceLine(
            380,
            DeltaOne,
            ru="Лидер звена Дельта. Даю координаты прыжковой дыры в Сигма-17.",
            en="This is Delta leader; I'm sending you the coordinates for the Sigma-17 jump hole.",
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
            en="Immobilize them and deliver them to Nebuchadnezzar.",
            cinematic=True,
        ),
        VoiceLine(
            410,
            Trent,
            ru="Теперь бы еще понять где мы.",
            en="Where the hell are we now?",
        ),
        VoiceLine(
            420,
            DeltaOne,
            ru="Я знаю эту систему. Это Мальта. Территория Изгоев. Здесь есть свободный порт, куда пускают всех кто смог до него добраться. Называется Фрипорт Тринидад. Там можно будет отсидеться. Вот координаты.",
            en="I know this system. This is Malta, in Outcast territory. There's a Freeport here that welcomes allcomers, it's called Trinidad Freeport. We can wait it out there. Sending you the coordinates.",
        ),
        VoiceLine(
            430,
            Trent,
            ru="Окей, идем туда.",
            en="Sweet, let's move.",
        ),
        VoiceLine(
            440,
            DeltaThree,
            ru="Командир, а вы не хотите направиться в более легальное место?",
            en="Hey commander, wouldn't you prefer to fly to a slightly more lawful place?",
        ),
        VoiceLine(
            450,
            DeltaOne,
            ru="В более легальном месте нас тут же возьмут под стражу за утрату артефактов и в лучшем случае обвинят в шпионаже. И хрен вы отмоетесь. ",
            en="Don't be daft, they'd be all over you for losing the artifacts. In the best case, you'd be accused of espionage. Good luck getting out of prison.",
        ),
        VoiceLine(
            460,
            DeltaOne,
            ru="Улетело пять истребителей с артефактами. Вернулись живые все пятеро, но на одном истребителе и без артефактов. И никто в сказочки с Капитаном Сидом не поверит. Я сам не верил когда однажды задерживал попавших в похожую ситуацию.",
            en="Of course, there's another option:",
        ),
        VoiceLine(
            470,
            DeltaOne,
            ru="Есть конечно еще один вариант - напасть на этом истребителе на Навуходоносор, победить там всех узнать координаты базы Ордена, захватить ее и уже с артефактами и высоко поднятой головой торжественно вернуться в систему Манхеттен. ",
            en="- deftly assassinate every soul aboard this battleship, decipher the secret coordinates to their base, fly over and capture it, return to Manhattan glorious victors, with the artifacts held triumphantly aloft in our hands.",
        ),
        VoiceLine(
            480,
            DeltaOne,
            ru="Как думаете, мистер Трент, ваш истребитель способен на такие боевые действия?",
            en="Okay, no need to be sarcastic. Mr. Trent, your thoughts?",
        ),
        VoiceLine(
            490,
            Trent,
            ru="Не-а. Сто процентов. К тому же, хочу напомнить, господа, вы сейчас находитесь на моем корабле, а посему полетим мы туда, куда скажу я. И сейчас мы летим на Тринидад.",
            en="Trinidad it is.",
        ),
        VoiceLine(
            1010,
            Reitherman,
            ru="Финн, срочно летите на главную базу, у нас несанкционированный доступ!",
            en="Finn, we have a security breach, return to base immediately!",
        ),
        VoiceLine(
            1020,
            FinnRunner,
            ru="Неизвестный пилот, внимание, укажите свой идентификационный код.",
            en="Unidentified pilot, please transmit your ID code immediately.",
        ),
        VoiceLine(
            1030,
            FinnRunner,
            ru="Профессор, у нас несанкционированный доступ! Неизвестный корабль не отвечает! Включаю всеобщую тревогу!",
            en="Professor, we have an intruder! Sound the alarm!",
        ),
        VoiceLine(
            1040,
            FinnRunner,
            ru="Профессор, мой аванпост атакован неизвестным пилотом. Всеобщая тревога!",
            en="Professor, my outpost is being attacked by an unknown vessel. Alert! Alert!",
        ),
        VoiceLine(
            1050,
            FinnRunner,
            ru="Профессор, у нас несанкционированный доступ! В вашу зону направляется неизвестный корабль, спасайтесь! ",
            en="Professor, we’re being breached! The unknown ship is coming for you. You must flee!",
        ),
        VoiceLine(
            1060,
            FinnRunner,
            ru="Двери не работают... Всему персоналу, всеобщая тревога! Несанкционированный доступ!",
            en="Doors are sealed… To all personnel, this is not a drill! We have a security breach! ",
        ),
        VoiceLine(
            1100,
            SphereOutpost,
            ru="Патруль Омега-4, это станция Гамбург. Обнаружены неполадки на одном из телескопов. Осмотр+ите его, возможно разрядился генератор.",
            en="Patrol Omega-4, this is Hamburg station. There's an issue with one of the telescopes. Have a look, its probably a battery problem. ",
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
            en="Critical damage! Battleship Missouri is in need of immediate assistance! To all fighter wings, intercept the torpedoes at once before they take us out!",
        ),
        VoiceLine(
            1220,
            SphereMissouri,
            ru="Канонерки израсходовали боеприпасы и покидают поле битвы. Миссури в безопасности.",
            en="The gunships have exhausted their ammunition and are leaving the field. Missouri is safe.",
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

    MISSION_TITLE = 'Миссия 6. Вход в Сферу'