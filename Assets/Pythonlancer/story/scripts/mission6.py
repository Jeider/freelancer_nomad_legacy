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
        VoiceLine(10, Trent, ru="Мисс Хетчер. Аларик, не ожидал, что ты уже здесь.", en="Miss Hatcher. Alaric, I didn't expect to see you here so soon."),
        VoiceLine(20, Alaric, ru="Как только ты со мной связался, я сразу же прибыл к мисс Хетчер. Видимо, я был ближе к Нориджу, чем ты.", en="Well, as soon as you contacted me, I flew to see Miss Hatcher right away. Looks like I was closer to Norwich than you were."),
        VoiceLine(30, Hatcher, ru="А теперь, господа, когда все выяснили когда, откуда и каким образом мы все сюда прибыли, перейдем к делу? ... ", en="Gentlemen, now that we've all figured out when and how we all got here, shall we get down to business?"),
        VoiceLine(40, Hatcher, ru="Отлично! Как вы уже поняли есть некий объект - Сфера. В свое время его обнаружил еще Орден, но тогда никто не смог понять что это, для чего предназначено и как работает. И про Сферу забыли. ", en="Great! So, as I mentioned before, there's an alien object called The Sphere. Originally discovered by The Order, nobody could understand what it is or how it works back then. And so, it got lost in time."),
        VoiceLine(50, Hatcher, ru="А теперь мы узнаём что рейнландцам удалось подобрать к ней ключ и они проводят на ней свои исследования. Есть обоснованное мнение, что ничем хорошим это не закончится. Поэтому исследования эти нужно, как бы это сказать... закрыть.", en="We’ve learned that Rheinlanders have discovered its key, and are currently running their experiments on it. We have reasons to believe that this will not end well for us. That's why we need your help in... ceasing these experiments, so to speak."),
        VoiceLine(60, Trent, ru="Ха-ха-ха, отлично. Если вы не смогли подобрать к Сфере ключ сами, то никто не должен. А если подобрал, то нужно срочно устранить либо ключ, либо Сферу, либо того кто это сделал. Браво! Так не доставайся же ты никому.", en="Ha-ha-ha! Perfect. So, if you guys can't find the key to The Sphere, then no one can! And if someone else finds it, then either the key or The Sphere itself have to go. Bravo! This way no one will ever get in there."),
        VoiceLine(70, Hatcher, ru="Я не разделяю вашего сарказма, мистер Трент. В прошлый раз подобная ситуация случилась, когда другие рейнландские ученые нашли нечто в Омикронах. Ох уж мне эти неугомонные рейнландцы.", en="I don't appreciate you being sarcastic about it, Mr. Trent. It already happened once, when another group of Rheinland scientists discovered something in the Omicron sector... Oh, how I despise these Rheinlanders..."),
        VoiceLine(80, Hatcher, ru="И все закончилось тем самым кризисом, про который я вам рассказывала в присутствие профессора Мандрейка. Вы поняли, о чем я?", en="It escalated into the crisis that I told you about when Prof. Mandrake was here. You get the idea, right?"),
        VoiceLine(90, Trent, ru="Да, понял. Не стоит шутить с ящиком Пандоры.", en="Yeah, I get it. Don’t open Pandora's Box."),
        VoiceLine(100, Hatcher, ru="Хорошо, с моральной подоплекой наших действий мы разобрались, теперь про материальную. Вы получите вознаграждение втрое больше обычного, и удостоверения внештатных сотрудников СБА. ", en="Very well. Now that we’re done with the theory, let’s get practical. You’ll be receiving triple the usual payment, and you’ll be granted the privilege of being official partners of the ASF."),
        VoiceLine(110, Alaric, ru="Чёрт побери, я за! Где ставить подпись? Могу кровью!", en="Hell yeah, I'm in! Where do I sign? I can make it a blood oath!"),
        VoiceLine(120, Trent, ru="Аларик, угомонись. Мисс Хетчер, а что конкретно нужно сделать? Уничтожить Сферу, уничтожить ученых? Мне это совсем не по душе, я всё-таки не наёмный убийца.", en="Calm down, Alaric. Miss Hatcher, what exactly is the objective? Destroy The Sphere? Kill the scientists? I can’t just do that - I'm not an assassin, after all."),
        VoiceLine(130, Hatcher, ru='А вы уверены? Нет, все не так страшно и кроваво, как вы сейчас расписали. В полученных нами документах профессор нашел способ сделать Сферу невосприимчивой к внешним воздействиям, как сказал профессор "закрыться". ', en="Oh, is that so? Just kidding. No, it's nothing like that. Based on the secret documents you handed over, Professor Mandrake found a way to render The Sphere insensitive to external influences. To “seal it shut”, as the professor says."),
        VoiceLine(140, Hatcher, ru="Все дальнейшие подробности - в том случае, если вы согласитесь.", en="I'll provide the full details, but only if you accept this mission."),
        VoiceLine(150, Trent, ru='У меня дежавю. Вот только в прошлый раз меня называли не "мистер Трент", а "герр Трент"... С другой стороны, временами было весело... Хорошо, я в деле.', en="I'm having a de-ja-vu. Only last time, I was called \"Herr Trent\", not \"Mr. Trent\"... On the other hand, it was a lot of fun. Alright, count me in."),
        VoiceLine(160, Hatcher, ru="Тогда встретимся на орбите и продолжим разговор там.", en="Then I'll meet you in the orbit; we'll continue our conversation there."),
    ]


class Msn6Briefieng(Msn6, script.CutsceneProps):
    ALIAS = 'briefing'
    TITLE = 'Брифинг'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Hatcher, ru="Итак, джентльмены, главная задача - ликвидировать рейнландского ученого, профессора Роттермана.", en="Alright, gentlemen, our main objective is to eliminate a Rheinland scientist named Professor Rotterman."),
        VoiceLine(20, Trent, ru="Черт, я так и думал.", en="Damn, I knew it."),
        VoiceLine(30, Hatcher, ru="Не перебивайте, Трент!  Думал он. Может быть, вы также думали, что за такой гонорар вам поручат доставку суши? ", en="Don't interrupt me, Trent! “I knew it” … Did you really think that for such a generous payment you’d be delivering sushi?"),
        VoiceLine(40, Hatcher, ru="Пора взрослеть, мистер Трент. ", en="Time to grow up, Mr. Trent.. "),
        VoiceLine(50, Hatcher, ru="Итак, ликвидируете профессора Роттермана и забираете два артефакта - кристалл кочевников и том Протея, они должны находиться либо у профессора, либо рядом с ним.", en="Alright, so, you’ll need to eliminate Professor Rotterman and find two artifacts: the Nomad Crystal and the Protheus Tome, which should be either in his possession or somewhere around him."),
        VoiceLine(60, Hatcher, ru="В свое время они хранились в одном из тайников Ордена, но в так называемые смутные времена следы их потерялись.", en="These artifacts were once kept hidden by The Order, but during the so-called \"troubled\" times, they got lost."),
        VoiceLine(70, Hatcher, ru="Вы забираете артефакты, увозите их и Сфера закрывается.", en="You take away those artifacts, and The Sphere will close itself."),
        VoiceLine(80, Alaric, ru="Орден? Смутные времена?", en="The Order? \"Troubled\" times?"),
        VoiceLine(90, Trent, ru="Позже, Аларик.", en="Later, Alaric."),
        VoiceLine(100, Hatcher, ru="Хватит, чёрт побери, меня перебивать, мы сейчас обсуждаем важнейшую миссию! ", en="Dammit, stop interrupting me! We're discussing an extremely important mission here!"),
        VoiceLine(110, Trent, ru="Самую важную в вашей жизни, мисс Хетчер? Не забывайте что конкретные исполнители - мы, и вот как исполнители мы хотели бы подробностей о предшествующих ликвидации профессора этапах. ", en="The most important mission in your life, Miss Hatcher? Don't forget that WE are the ones doing the dirty work, and we deserve to know ALL the details leading up to our main objective."),
        VoiceLine(120, Hatcher, ru="Хорошо, Трент. Итак, проникновение внутрь Сферы. Охраняется она беспрецедентно. Я сомневаюсь, что кайзер Рейнланда охраняется так же как она. ", en="Very well, Trent. So, first, getting inside The Sphere. It is very heavily guarded. Probably even more than the Rheinland Kaiser’s palace itself."),
        VoiceLine(130, Hatcher, ru="Рядом со сферой находится военная база, представляющая собою верфь, способную принимать по два линкора и четыре корабля среднего тоннажа одновременно. Понимаете, какая там развернута группировка? Поэтому силовое решение невозможно. ", en="There is a military base near The Sphere; which looks like a shipyard capable of housing two battleships and four mid-sized vessels simultaneously. Do you understand the scale of the operation now? That's why a brute force solution is impossible."),
        VoiceLine(140, Hatcher, ru="Для проникновения вам понадобятся устройства, которые находятся в контейнерах, переданных мною вам перед стыковкой с Миссури. Это устройства, делающие ваши корабли невидимыми как визуально, так и всеми радарными системами. ", en="In order to infiltrate the base, you'll need to use the devices you got from those little containers you picked up earlier. Those are cloaking devices, which make your ships invisible to both eyes and radars."),
        VoiceLine(150, Hatcher, ru="Они создают вокруг корабля локальное искривление пространства, и ваши корабли как бы перестают находиться в нашей реальности. ", en="They change the local space curvature, essentially causing your ships to shift into a parallel universe."),
        VoiceLine(160, Hatcher, ru="Смонтируете их у себя на кораблях - просто устанавливаете где-нибудь внутри герметичного корпуса, подключаете к энергосистеме и выводите кнопку управления в удобное место приборной доски. Кнопка всего одна, не ошибетесь. ", en="Mounting them should be simple: Install them on your ships, connect them to the power generator, and route the cloak control button to your HUD. There's only one button - even you geniuses could never get it wrong."),
        VoiceLine(170, Hatcher, ru="Нажимаете один раз - и ваш корабль невидим, нажимаете второй раз - и он снова видим. Проблема устройства в его одноразовости. ", en="Push the button once, and you're cloaked. Push it once again, and you're back to being visible."),
        VoiceLine(180, Hatcher, ru="Я не ученый, поэтому скажу просто, после выключения там что-то перегорает, и оно превращается в коробочку с горелым пластиком и обугленным  металлом. ", en="But... there's only one problem. After turning it off, the device is rendered into a pile of melted plastic and metal. Simply speaKing, it overheats and becomes useless."),
        VoiceLine(190, Trent, ru="Огнетушителями запасаться? ", en="Should we bring fire extinguishers, then?"),
        VoiceLine(200, Hatcher, ru="Нет, все безопасно, все происходит внутри устройства, даже неприятного запаха не появится. ", en="No, it's safe. Everything happens within the device itself, and you won't even smell it."),
        VoiceLine(210, Hatcher, ru="По времени работы. Поскольку устройство одноразовое, постарайтесь использовать его максимально эффективно. Наши головастики гарантируют тридцать минут работы. Возможно, оно проработает сорок, больше вряд ли. ", en="Now, it’s all about the timing. Not only is this a one-time use device, it also won't work forever, so make sure to use it effectively. Our big brain scientists guarantee it’ll work for at least 30 minutes. Potentially up to 40 minutes, but probably no longer than that."),
        VoiceLine(220, Hatcher, ru="Если тридцати минут работы не хватило, вы можете попробовать оставаться в невидимости дольше на свой страх и риск. Если устройство сгорит не во время выключения, а во время работы, локальное искривление пространства схлопывается вместе с кораблём. ", en="If 30 minutes isn't enough for you, you could try staying cloacked longer, but at your own risk. If the cloaking device overheats during active use, the local space curvature collapses along with your ship."),
        VoiceLine(230, Alaric, ru="И куда попадает корабль? В другое измерение? ", en="And what happens to the ship? It goes to a different dimension?"),
        VoiceLine(240, Hatcher, ru="Понятия не имею. Хотите узнать, мистер Аларик? По глазам вижу, что нет. И да, еще один момент. При включенном устройстве стрелять бесполезно. Выши выстрелы не покинут локальную зону искривления пространства.", en="I have no idea. Would you like to find out? That look on your face tells me the answer is no. Oh, and one more thing: you can't shoot while the device is working. Your projectiles won't be able to escape the local space curvature zone."),
        VoiceLine(250, Hatcher, ru="Вот трехмерный план Сферы и все данные по ней, которые нам удалось собрать.", en="Here is the 3D map of The Sphere and all the other intel we managed to collect."),
        VoiceLine(260, Alaric, ru="Вот это хреновина...", en="Wow, just look at it..."),
        VoiceLine(270, Hatcher, ru="Я рада, что вы прониклись, мистер Аларик. Загрузите всё к себе в компьютер. В ходе операции будете передавать нужные данные мистеру Тренту. ", en="I'm glad you've come to appreciate its magnitude, Mr. Alaric. Please upload the data into your computer. You’ll be sending it over to Trend throughout the mission."),
        VoiceLine(280, Hatcher, ru="Ну и последнее - после прибытия на территорию Рейнланда никаких радиопереговоров со мной или с кем-то еще на территории Либерти. Вас запеленгуют их радарные станции, и миссия завершится так и не начавшись. ", en="And lastly, after you’ve arrived in Rheinland, there will be complete radio silence between us or anyone else in Liberty. Otherwise, you will be pinpointed and the mission will fail before it even started."),
        VoiceLine(290, Hatcher, ru="Вот, собственно, и всё. По коням, джентльмены.", en="That's about it. Onwards to your steeds, gentlemen."),
    ]


class Msn6Mount(Msn6, script.CutsceneProps):
    ALIAS = 'mount'
    TITLE = 'Установка устройства'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Trent, ru="У тебя редкий талант постоянно влипать в неприятности, Аларик.", en="You have a rare talent of getting into sticky situations, Alaric."),
        VoiceLine(20, Alaric, ru="Ты о чем? ", en="What are you talking about?"),
        VoiceLine(30, Trent, ru="О том что с нами будет происходить в ближайшем будущем.", en="About what will happen very soon."),
        VoiceLine(40, Alaric, ru="Ты про нашу миссию?", en="Are you talking about our mission?"),
        VoiceLine(50, Trent, ru="Про нашу СУИЦИДАЛЬНУЮ миссию.", en="About our SUICIDE mission."),
        VoiceLine(60, Alaric, ru="Зато какие выгоды в случае успеха! К тому же ты мог бы отказаться.", en="Ah, but think of the profits!!! Besides, you could've said \"no\" at any time."),
        VoiceLine(70, Trent, ru="Боюсь, если бы я отказался, то уже летал бы в космосе без скафандра.", en="I'm afraid if I had said \"no\", I'd end up flying in space without a space suit."),
        VoiceLine(80, Alaric, ru="Трент, раз уж мы подписались, надо выполнять. Давай, Трент, полетели. Обещаю, в следующий раз заказчика будешь выбирать ты.", en="Trent, since we’ve already signed this contract, we have to do it. Come on, Trent, let’s fly. Next time I’ll let you choose the contract, I promise."),
        VoiceLine(90, Trent, ru="Если он будет, этот следующий раз. ", en="Assuming there’ll be a \"next time\" in the first place."),
    ]


class Msn6LabLand(Msn6, script.CutsceneProps):
    ALIAS = 'lab_land'
    TITLE = 'Посадка на лабораторию'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Alaric, ru="Трент, у нас мало времени. Я уже установил взрывчатку с таймером обратного отсчета.", en="Trent, we don't have much time. The bomb is already ticking."),
        VoiceLine(20, Trent, ru="Мы же хотели просто закрыть сферу?", en="I thought we were going to close the sphere, not blow it up!"),
        VoiceLine(30, Alaric, ru="Вот мы и закроем. Хетчер решила подстраховаться. Мы уничтожим лабораторию.", en="We will. This is Hatcher’s plan B, just in case. We're gonna blow up the lab."),
        VoiceLine(40, Trent, ru="Ясно.", en="Got it."),
    ]


class Msn6LabRoom(Msn6, script.CutsceneProps):
    ALIAS = 'lab_room'
    TITLE = 'Лаборатория'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Trent, ru="Обалдеть…", en="Holy moly, look..."),
        VoiceLine(20, Alaric, ru="Трент, бежим! Потом рассмотришь.", en="Trent we need to run! You can look at it later"),
    ]


class Msn6TorpedoAlert(Msn6, script.CutsceneProps):
    ALIAS = 'torpedo_alert'
    TITLE = 'Торпедная тревога'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Hatcher, ru="Трент, у нас критическая ситуация! Рейнландцы выпустили против Миссури торпедные канонерки. ", en="Trent, we have a critical situation! Rheinland gunboats have just fired torpedoes at Missouri."),
        VoiceLine(20, Hatcher, ru="Мы не успеваем запустить гипердвигатель, а системы ПВО линкора не смогут перехватить все выпущенные торпеды. ", en="Our hyperdrive is not ready yet, and our defense systems won't be able to shoot down all the torpedoes."),
        VoiceLine(40, Trent, ru="Но сначала нужно выгрузить артефакты.", en="But we need to unload the artifacts first..."),
        VoiceLine(50, Hatcher, ru="В данной ситуации они большей безопасности у вас на борту, а не на Миссури. Вылетайте! Быстрее!", en="No, right now they'll be much safer in your cargo hold than on Missouri. Get out there, quickly!"),
    ]


class Msn6OrderDeck(Msn6, script.CutsceneProps):
    ALIAS = 'order_deck'
    TITLE = 'Стыковочный узел Навухудоносора'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, OrderPilot, ru="Капитан Сид, мы обнаружили артефакты на борту этого фриленсера.", en="Captain Ceed, we found artifacts in this Freelancer's cargo hold."),
        VoiceLine(20, Ceed, ru="Отлично. Спасибо за работу, ребята. Артефакты – на склад, пленных – в кают-компанию.", en="Excellent. Good work, guys. Send the artifacts to the storage facility, and put the prisoners into the wardroom."),

    ]


class Msn6Prison(Msn6, script.CutsceneProps):
    ALIAS = 'order_prison'
    TITLE = 'Тюремная камера'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Ceed, ru="Вольно, рядовой. Идите в диспетчерскую, пусть подготовят корабль для доставки пленных на нашу базу. А я пока начну допрос.", en="At ease, soldier. Go to the control room and tell them to order a transport. The prisoners need to be delivered to our base. In the meantime, I'll start interrogating them."),
        VoiceLine(20, OrderGuard, ru="Сэр, но если...", en="Sir, but what if..."),
        VoiceLine(30, Ceed, ru="Никаких если. На них же шокеры, пусть только попробуют рыпнуться.", en="No. They got shockers on them - they'll regret even thinking about it."),
        VoiceLine(40, OrderGuard, ru="Есть, сэр.", en="Yes, sir."),
        VoiceLine(50, Ceed, ru="Спокойно, джентльмены, я не кусаюсь. Вам повезло, что все произошло во время моего дежурства.", en="Don't worry, lads, I don't bite. Consider yourselves lucky that it all happened while I was on duty."),
        VoiceLine(60, Ceed, ru="Забыл представиться. Хари Сид, капитан Ордена, лейтенант СБА, работаю тут под прикрытием.", en="Also, forgot to introduce myself. Harry Ceed, captain of The Order, but also an ASF lieutenant working here undercover."),
        VoiceLine(65, Ceed, ru="Сейчас подождем некоторое время, а потом я помогу вам покинуть негостеприимный борт Навуходоносора", en="We're going to wait here for a little while, and then I'll help you get off the inhospitable board of Nebuchadnezzar."),
        VoiceLine(70, DeltaThree, ru="Сдается мне, ребята, что это очередная провокация Ордена, и выведет нас этот милый капитан на шеренгу бойцов со штурмовыми винтовками.", en="Guys, I have a feeling that this is yet another trick from The Order and that this lovely captain is about to put us in front of a squad of fighters with assault rifles..."),
        VoiceLine(80, DeltaOne, ru="А у тебя что, есть предложения получше? В любом случае, лучше на шеренгу бойцов с винтовками, чем на допрос к специалистам Ордена.", en="You got any better idea? Either way, being shot is probably a better alternative to being interrogated by Order specialists."),
        VoiceLine(90, Trent, ru="А что там с артефактами, капитан?", en="Captain, what about the artifacts?"),
        VoiceLine(100, Ceed, ru="Летят на базу Ордена.", en="They're being transported to an Order base."),
        VoiceLine(110, DeltaOne, ru=" И вы позволили?", en="And you allowed that?"),
        VoiceLine(120, Ceed, ru="А что я, по-вашему, должен был сделать? Если бы я начал вставлять Ордену палки в колеса, то сидел бы тут с вами, только не с сигаретой в руке, а с таким же милым ошейником на шее как у вас.", en="What was I supposed to do? If I messed with The Order, I'd end up sitting down here beside you with a cute little shocker around my neck; rather than smoking my favorite brand of cigarettes."),
        VoiceLine(130, Trent, ru="А как вы собираетесь помочь нам бежать?", en="So, what’s your escape plan for us?"),
        VoiceLine(140, Ceed, ru="Для начала вы примерите вот это...", en="First, put these clothes on"),
        VoiceLine(145, Ceed, ru="А потом спокойно и небрежно проследуете в ангар к кораблю мистера Трента. ", en="Then, follow me calmly to the hangar, to Mr. Trent’s ship."),
        VoiceLine(150, Ceed, ru="К сожалению, все остальные уже разбирают на запчасти. А вот корабль Трента пока еще в целости и сохранности. Так что, как говорится, в тесноте, да не в обиде.", en="Unfortunately, all the other ships are being taken down for spare parts. Luckily, Trent's ship is still in one piece. It’s like they say, the more people at the party, the merrier."),
        VoiceLine(160, Trent, ru="А после нашего побега... Как это скажется на вас? Вы не будете сидеть здесь не с сигаретой в руке, а с ошейником как у нас на шее?", en="And after we're gone, how’s that going to affect you? You certainly won't be sitting here smoking a cigarette. Rather, you'll likely be trying to smoke a shocker off your neck."),
        VoiceLine(170, Ceed, ru="О, нет. Вы же меня вырубили, этому найдутся неоспоримые доказательства. ", en="Oh, no. You guys have knocked me out, there will be irrefutable proof of this."),
        VoiceLine(180, Ceed, ru="К тому же, что такое побег пленников в сравнении с тем, что я передал в руки  Ордена артефакты, за которыми охотится весь сектор Сириуса.", en="Besides, a few escaped prisoners pale in comparison to putting the artifacts, which are sought by the whole Sirius sector, into the hands of The Order."),
        VoiceLine(190, Trent, ru="Толково, не поспоришь. ", en="Clever, indeed."),

    ]


class Msn6Freeport(Msn6, script.CutsceneProps):
    ALIAS = 'freeport'
    TITLE = 'Фрипорт'
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, DeltaOne, ru="Мистер Трент, Хочу вас поблагодарить за проделанную работу. Прошу извинить нас за то, что попали в неприятности по нашей вине, и я обещаю, что сделаю все возможное, чтобы восстановить вашу репутацию.", en="Mr. Trent, I'd like to thank you for your work. Please accept our apologies for dragging you into such a dangerous situation, and I promise that I'll do everything I can to restore your reputation with us."),
        VoiceLine(20, Trent, ru="Это все хорошо, конечно, но что мне, собственно, делать сейчас?", en="This is all well and good, but what should I do now?"),
        VoiceLine(30, DeltaOne, ru="Ведите себя тихо, принимайте контракты на этом фрипорте, в других независимых или пиратских системах, но ни в коем случае не возвращайтесь в легальные системы.", en="Keep a low profile. Feel free to work a few odd jobs on this freeport, other independent stations, or hell, possibly even with the pirates. But under no circumstances should you return to lawful space."),
        VoiceLine(40, DeltaOne, ru="Если вас там задержат, мы будем бессильны что-то с этим сделать. А вас превратят в козла отпущения.", en="If you're caught there, we won't be able to help you. You'll be turned into a scapegoat."),
        VoiceLine(50, DeltaOne, ru="А сейчас мне нужно выйти на связь со штабом СБА, обсудить создавшуюся ситуацию и выработать дальнейший план действий. ", en="I must contact with ASF headquarters right away to discuss the situation and develop an action plan."),
        VoiceLine(60, DeltaOne, ru="В благодарность за вашу работу я перевожу вам со своего счета пять тысяч кредитов. Кроме того, вознаграждение за предыдущую миссию остается за вами, и как только мы разрешим эту ситуацию, вы его получите.", en="As a token of gratitude, I'm transferring you 5,,000 credits from my personal account. Additionally, the promised reward from this mission still stands, and you should receive it as soon as our situation is resolved."),
        VoiceLine(70, Trent, ru="А как же компенсация за моральный ущерб?", en="And what about a compensation for the mental damage?"),
        VoiceLine(90, DeltaOne, ru="Мистер Трент, вы никогда не производили впечатление жадного человека. Вы достаточно долго и успешно действуете в непростых ситуациях. ", en="Mr. Trent, frankly speaKing, you never gave the impression of a greedy man. You operate very patiently and very effectively in risky life-or-death situations. And you survived thus far."),
        VoiceLine(100, DeltaOne, ru="А вот жадные люди, я слышал, долго не живут... Как только появятся новости, я свяжусь с вами, мистер Трент.", en="Greedy people, on the other hand, tend to live much shorter lives in my experience. I'll be in touch once I’ve got any news for you, Mr. Trent."),
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
            en="Knowing Rheinland, there’s probably tight guard around each and every asteroid around the sphere, and I bet they stuck a battleship in there.",
        ),
        VoiceLine(
            30,
            Hatcher,
            ru="Берите выше, мистер Трент, у них там развернута военная база.",
            en="That's an understatement, Mr. Trent. In fact, they have a fully deployed military base there.",
        ),
        VoiceLine(
            40,
            Trent,
            ru="Тогда, простите, каким образом мы с напарником должны будем с ними справиться? Вы выдадите нам карманную черную дыру?",
            en="Excuse me, but how exactly do you expect me and my wingman to deal with that? Are you gonna give us a black hole that can fit in our pockets?",
        ),
        VoiceLine(
            50,
            Hatcher,
            ru="Нет, она еще проходит стендовые испытания. Я сейчас сброшу вам по контейнеру, подберите их и стыкуемся с Миссури. ",
            en="No, that device is still being tested. I'll drop a few containers for you, tractor them in and dock with Missouri.",
        ),
        VoiceLine(
            55,
            HatcherStation,
            ru="Наши военные аналитики разработали стратегии выполнения задания. Эти стратегии уже загружены в ваши корабли. "
               "Можете воспользоваться при необходимости.",
            en="Our military analytics prepared special mission strategies. Those strategies was uploaded to "
               "your neuralenets. You can use it at your will."
        ),
        VoiceLine(
            60,
            HatcherStation,
            ru="Удачи, джентльмены. Напоминаю, на территории Рейнланда никаких радиопереговоров со мной.",
            en="Best of luck, gentlemen. And remember – maintain radio silence with me once you've reached Rheinland.",
        ),
        VoiceLine(
            70,
            Alaric,
            ru="Трент, чтобы увеличить наши шансы, предлагаю разделиться. Встречаемся внутри Сферы.",
            en="Trent, we’ll have a better chance at it if we split up. I'll meet you inside the sphere.",
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
            en="Except the outer perimeter is locked down, so there's no longer a way back.",
        ),
        VoiceLine(
            110,
            Alaric,
            ru="Трент, мы входим в зал в котором рейнландцы развернули лабораторию. Артефакты должны быть где-то внутри. ",
            en="Trent, we're entering the hall where Rheinlanders deployed their lab. Artifacts should be somewhere inside.",
        ),
        VoiceLine(
            120,
            Alaric,
            ru="Попробуй пробраться внутрь через шлюзы и найти Роттермана, а я в это время попробую снять или хотя бы ослабить щиты.",
            en="Try sneaking in through the airlocks and find Rotterman, while I try to take down or weaken the shields.",
        ),
        VoiceLine(
            130,
            Trent,
            ru="Аларик, тут все задраено. Не пройти.",
            en="Alaric, it's all sealed down here. I can't get through.",
        ),
        VoiceLine(
            140,
            Alaric,
            ru="Трент, есть другой путь, через технические тоннели. Скидываю координаты.",
            en="Trent, there's another way, through maintenance vents. I'm sending you the coordinates.",
        ),
        VoiceLine(
            150,
            Trent,
            ru="Аларик, тут что-то непонятное. Какой-то кристалл, вокруг которого летают корабли Кочевников.",
            en="Alaric, there's something weird in here. Some kind of crystal, surrounded by Nomad ships.",
            cinematic=True,
        ),
        VoiceLine(
            160,
            Alaric,
            ru="По данным СБА этот кристалл назвали 'Номадским зерном'. Если кочевники тебя заметят, то из Зерна будут появляться все новые и новые истребители.",
            en="ASF intel says this crystal is called 'The Nomad Seed'. If Nomads sense your presence, their ships will start pouring out of this thing.",
            cinematic=True,
        ),
        VoiceLine(
            170,
            Alaric,
            ru="Выход должен находиться рядом, но он был автоматически закрыт после активации Зерна. Чтобы система безопасности разблокировала выход необходимо ликвидировать угрозу в этом зале, то есть уничтожить Зерно и все корабли кочевников. ",
            en="The exit was somewhere around here, but it was automatically sealed after the Seed activated. In order to unseal it, you need to eliminate all the threats:",
            cinematic=True,
        ),
        VoiceLine(
            180,
            Alaric,
            ru="Проблема в том, что если ты сильно нашумишь, наши рейнландские друзья могут перевозбудиться, поэтому действовать надо быстро.",
            en="The only problem is, if you make too much noise, our Rheinland friends will join the party. So, you have to act quickly.",
            cinematic=True,
        ),
        VoiceLine(
            190,
            Trent,
            ru="Черт... Ладно, выключаю невидимость и уничтожаю Зерно.",
            en="Dammit... Alright, powering off cloak and attacking the Seed.",
        ),
        VoiceLine(
            200,
            Alaric,
            ru="Трент, быстрее, рейнландцы почуяли неладное в этом зале, хотят направить к тебе оперативную группу.",
            en="Trent, hurry up! The Rheinlanders are sensing something’s wrong in that hall. They want to send a group of scouts there.",
        ),
        VoiceLine(
            210,
            Trent,
            ru="Охренеть. Это что же за адская машина?",
            en="Holy shit! What the hell is this kind of machine?",
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
            en="Trent, what's taking you so long? Come here, the shields are almost gone - it won't take much longer.",
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
            en="Gentlemen, we're almost done with this mission. Battleship Missouri is approaching the Sphere. Proceed to dock, quickly!",
        ),
        VoiceLine(
            300,
            SphereMissouri,
            ru="Канонерки вышли на огневой рубеж!",
            en="Gunships at the firing range.",
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
            en="Trent, Missouri won't be able to jump. Its engines are damaged and need repairs.",
        ),
        VoiceLine(
            330,
            HatcherStation,
            ru="Здесь становится жарко. Вы с должны будете доставить артефакты на нашу базу в Сигма-17 сами. Я выделю вам для прикрытия звено Дельта.",
            en="It's getting hot here. You’ll have to deliver these artifacts to our base in Sigma-17 on your own. The Delta wing will escort you.",
        ),
        VoiceLine(
            340,
            Trent,
            ru="Понял вас, выдвигаюсь. Удачи вам здесь.",
            en="Acknowledged, moving out. Good luck out here.",
        ),
        VoiceLine(
            350,
            HatcherStation,
            ru="Спасибо, Трент. Поверьте, вам она понадобится не меньше.",
            en="Thanks Trent. Trust me, you'll need it more than I do.",
        ),
        VoiceLine(
            360,
            Alaric,
            ru="Трент, я останусь помогу тут.",
            en="Trent, I'm staying here to help.",
        ),
        VoiceLine(
            370,
            Trent,
            ru="И только попробуй мне тут помереть.",
            en="Just try to stay alive, OK?",
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
            en="Freeze them and deliver them to Nebuchadnezzar.",
            cinematic=True,
        ),
        VoiceLine(
            410,
            Trent,
            ru="Теперь бы еще понять где мы.",
            en="Now, where the hell are we?",
        ),
        VoiceLine(
            420,
            DeltaOne,
            ru="Я знаю эту систему. Это Мальта. Территория Изгоев. Здесь есть свободный порт, куда пускают всех кто смог до него добраться. Называется Фрипорт Тринидад. Там можно будет отсидеться. Вот координаты.",
            en="I know this system. This is Malta, in the Outcast territory. There's a Freeport here that allows anyone to dock, it's called Trinidad Freeport. We can wait there. Sending you the coordinates.",
        ),
        VoiceLine(
            430,
            Trent,
            ru="Окей, идем туда.",
            en="Sweet, let's go there.",
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
            en="In a slightly more lawful place, you'd immediately get apprehended for losing the artifacts. And, in the best case, get accused of espionage. Good luck getting out of prison.",
        ),
        VoiceLine(
            460,
            DeltaOne,
            ru="Улетело пять истребителей с артефактами. Вернулись живые все пятеро, но на одном истребителе и без артефактов. И никто в сказочки с Капитаном Сидом не поверит. Я сам не верил когда однажды задерживал попавших в похожую ситуацию.",
            en="Think of it this way:",
        ),
        VoiceLine(
            470,
            DeltaOne,
            ru="Есть конечно еще один вариант - напасть на этом истребителе на Навуходоносор, победить там всех узнать координаты базы Ордена, захватить ее и уже с артефактами и высоко поднятой головой торжественно вернуться в систему Манхеттен. ",
            en="Of course, there's another option - quickly kill everyone on Nebuchadnezzar, steal the coordinates for their secret base, capture it, and come back to Manhattan. Glorious, victorious, and with artifacts in your hands.",
        ),
        VoiceLine(
            480,
            DeltaOne,
            ru="Как думаете, мистер Трент, ваш истребитель способен на такие боевые действия?",
            en="Mr. Trent, is your ship capable of such aggressive maneuvers?",
        ),
        VoiceLine(
            490,
            Trent,
            ru="Не-а. Сто процентов. К тому же, хочу напомнить, господа, вы сейчас находитесь на моем корабле, а посему полетим мы туда, куда скажу я. И сейчас мы летим на Тринидад.",
            en="Rest assure it cannot. By the way, since you gentlemen are on board my ship, let me remind you that you're going to fly where I say. And right now, we're going to Trinidad.",
        ),
        VoiceLine(
            1010,
            Reitherman,
            ru="Финн, срочно летите на главную базу, у нас несанкционированный доступ!",
            en="Finn, we have a security breach, come to the main base immediately!",
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
            en="Professor, we have a breach! The unidentified ship isn’t responding! Activating the alarm!",
        ),
        VoiceLine(
            1040,
            FinnRunner,
            ru="Профессор, мой аванпост атакован неизвестным пилотом. Всеобщая тревога!",
            en="Professor, my outpost is being attacked by the unknown vessel. Alarm! Alarm!",
        ),
        VoiceLine(
            1050,
            FinnRunner,
            ru="Профессор, у нас несанкционированный доступ! В вашу зону направляется неизвестный корабль, спасайтесь! ",
            en="Professor, we’re being breached! The unknown ship is headed towards you. You must escape!",
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
            en="Omega-4 patrol, this is Hamburg station. We found issues on one of the telescopes. Take a look, maybe its battery is low. ",
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
            en="Sustained critical damage! Missouri needs immediate assistance! To all fighter wings, your order is to intercept the torpedoes at once!",
        ),
        VoiceLine(
            1220,
            SphereMissouri,
            ru="Канонерки израсходовали боеприпасы и покидают поле битвы. Миссури в безопасности.",
            en="Gunships have exhausted their ammo and are leaving the battlefield. Missouri is safe.",
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
