from story import script
from audio.sound import VoiceLine
from story.actors import Trent, Darcy, HasslerOrder, EdisonTrent, Alaric, Juni, Tor
from story.cutscenes.story_scenes import m10_offer, m10_rescued, m10_final


class Msn10(object):
    MISSION_INDEX = 10


class Msn10OfferCutscene(Msn10, script.CutsceneProps):
    ALIAS = 'offer'
    TITLE = 'Бар линкора Мусаси'
    THORN_CLASS = m10_offer.Msn10OfferCutsceneThorn
    THORN_DECISION_CLASS = m10_offer.Msn10OfferDecisionThorn
    THORN_ACCEPT_CLASS = m10_offer.Msn10OfferAcceptThorn
    DESCRIPTION = 'Трент и Дерси встречаются в баре по предложению Хасслера'
    VOICE_LINES = [
        VoiceLine(
            10,
            HasslerOrder,
            ru='Герр Трент, фрау Д+ерси',
               en='Herr Trent, Fraulein Darcy!'
        ),
        VoiceLine(
            20,
            Darcy,
            ru='Фр+ойляйн.',
               en='Fräulein.'
        ),
        VoiceLine(
            30,
            HasslerOrder,
            ru='Прост+ите?',
               en='What?'
        ),
        VoiceLine(
            40,
            Darcy,
            ru='Фр+ойляйн Д+ерси.',
               en='It\'s Fräulein Darcy.'
        ),
        VoiceLine(
            50,
            Trent,
            ru='(Возмущенно) Прошу меня извинить, но мы кажется собрались не лингвистические вопросы разбирать.',
               en='Excuse me, but I believe we have more pressing matters at hand than linguistics.'
        ),
        VoiceLine(
            60,
            HasslerOrder,
            ru='Йа! Точно так. К делу! Наши недавние... хмммм... манёвры, а так же резкая активизация вооруженных сил Р+ейнланда изменили '
               'общую ситуацию не лучшим образом.',
               en='Ja! Exactly. Let\'s get to the point! Our recent... hmmm... maneuvers, as well as the sudden increase in activity of Rheinland\'s armed forces,'
                  'have changed the situation for the worse.'
        ),
        VoiceLine(
            70,
            Trent,
            ru='(Дикий сарказм) Кто бы мог подумать, что локальная война с СБА в отдельно взятой системе изменит ситуацию не лучшим образом?',
               en='(sarcastically) Who would have imagined attacking the ASF in their system could make things worse?'
        ),
        VoiceLine(
            80,
            HasslerOrder,
            ru='Это было необходимо,, герр Трент... А сейчас мы должн+ы реагировать на изменившуюся ситуацию.',
               en='It was necessary, Herr Trent... And now we must deal with the fallout.'
        ),
        VoiceLine(
            90,
            Trent,
            ru='Кого убить на этот раз?',
               en='So who are we assassinating this time?'
        ),
        VoiceLine(
            100,
            HasslerOrder,
            ru='Нет, герр Трент, совсем наоборот. Нужно будет вытащить из тюрьм+ы кс+еносов одного хор+ошего человека, героя войн+ы с кочевниками.',
               en='Nein, Herr Trent, quite the opposite. We need you to break a man out of a Xeno prison. A hero in the war against the Nomads.'
        ),
        VoiceLine(
            110,
            Trent,
            ru='Войн+ы с кочевниками официально ведь н+е б+ыло.',
               en='But there was no war against the nomads. Officially.'
        ),
        VoiceLine(
            120,
            HasslerOrder,
            ru='Это не отменяет того,, что были её герои.',
               en='Of course. An unofficial hero then.'
        ),
        VoiceLine(
            130,
            Trent,
            ru='Пусть так, но при чём тут я?',
               en='Okay. So why me? What does this have to do with me?'
        ),
        VoiceLine(
            140,
            HasslerOrder,
            ru='Вы не первый, кто пытался освободить интересующего нас человека. Первым был ваш друг Аларик.',
               en='The first agent we recruited for this task was your friend, Alaric.'
        ),
        VoiceLine(
            150,
            Trent,
            ru='(Подытожив) И Аларик облажался...',
               en='Didn\'t you guys say Alaric went missing delivering information...'
        ),
        VoiceLine(
            160,
            HasslerOrder,
            ru='Весьма прискорбно, но так и есть. Теперь он содержится в той же тюрьме.',
               en='Need to know basis Mr Trent. Now you need to know. Alaric failed his mission and is being held prisoner in the prison too.'
        ),
        VoiceLine(
            170,
            Trent,
            ru='И вы хотите, чтобы я повторил его подвиг, и нас в тюрьме стало уже трое? И Аларику не скучно, и преферансик на троих можно будет раскинуть.',
               en='And you want me to repeat his failure, so there\'ll be three of us in there? At least Alaric won\'t be bored, we can play cards.'
        ),
        VoiceLine(
            180,
            HasslerOrder,
            ru='При всём моем уважении к герру Аларику, его способности значительно уступают вашим.',
               en='With all due respect to Herr Alaric, his capabilities were... significantly inferior to yours.'
        ),
        VoiceLine(
            190,
            Trent,
            ru='Хорошо... Если вы так считаете,, герр Хасслер. (тихо, в сторону) Эх как же я задолбался... Задолбался!',
               en='Alright... If you say so, Herr Hassler. Oh, I\'m so sick of this... And fresh out of matches.'
        ),
        # место для принятия миссии
        VoiceLine(
            200,
            Trent,
            ru='(Выдохнув) Ладно, каков план?',
               en='Alright, what\'s the plan?'
        ),
        VoiceLine(
            210,
            HasslerOrder,
            ru='Тюрьма находится в Омега-38. Система представляет собой по большей части пылевое облако. '
                'Мус+аси переместится на окраину системы таким образом,, чтобы не привлечь внимание аборигенов.',
               en='The prison is in Omega-38. The system is mostly dust cloud.'
                    'The Musashi will position itself on the system\'s outskirts to avoid drawing undue attention.'
        ),
        VoiceLine(
            220,
            HasslerOrder,
            ru='Герр Трент, вы с фр+ойляйн Д+ерси возглавите диверсионное звено. '
               'Ваши корабли получат дополнительную мимикрирующую обработку, чтобы вы могли пробраться к тюрьме незаметно.',
               en='Herr Trent, you and Fräulein Darcy will lead the infiltration wing.'
                  'Your ships will receive additional mimetic coating to allow you to slip into the prison undetected.'
        ),
        VoiceLine(
            230,
            HasslerOrder,
            ru='Вы должн+ы б+удете подавить защитные системы тюрьм+ы. '
               'Следом в дело вступает наш транспорт с десантниками и звено прикрытия.',
               en='Your task is to disable the prison\'s defense systems.'
                  'After you\'ve done that, our transport with the boarding team and an escort wing will move into position.'
        ),
        VoiceLine(
            240,
            HasslerOrder,
            ru='После того,, как десант сделает свое дело, все весело и с фейерверками прорываются обратно на Мус+аси.',
               en='Once the boarding party has completed the extraction, everyone makes a... calm and peaceful trip back to the Musashi, alive and well.'
        ),
        VoiceLine(
            250,
            Trent,
            ru='Звучит заманчиво.',
               en='Sounds appealing.'
        ),
        VoiceLine(
            260,
            Darcy,
            ru='Посмотрим, как окажется на самом деле.',
               en='Let\'s see how it plays out in reality.'
        ),
        VoiceLine(
            270,
            HasslerOrder,
            ru='Тогда можете готовиться к вылету. Я буду координировать операцию с мостика линкора.',
               en='Prepare for launch. I will be coordinating the operation from the bridge of the battleship.'
        ),
    ]


class Msn10Space(Msn10, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(
            10,
            Darcy,
            comment='Взлёт после принятия миссии',
            ru='Эй, Хасслер, чего там твои инженеры шаманили над нашими кораблями?',
               en='Hey, Hassler, what were your engineers doing to our ships?'
        ),
        VoiceLine(
            20,
            HasslerOrder,
            ru='Устанавливали мимикрирующие панели, фр+ойляйн Д+ерси.',
               en='They were installing the mimetic panels, Fräulein Darcy. I mentioned this during the briefing.'
        ),
        VoiceLine(
            30,
            HasslerOrder,
            ru='Эти панели снизят вашу заметность на радарах в разы. В зависимости от характера окружающего пространства от двух до семи раз.',
               en='These panels reduce your radar signature significantly. Depending on the environment, by a factor of two to seven.'
        ),
        VoiceLine(
            40,
            HasslerOrder,
            ru='Кроме того они подстраиваются под характер окружающего пространства визуально. В плотном пылевом облаке если вы не двигаетесь вас можно будет обнаружить только радаром и только вплотную.',
               en='They also react to the surrounding space and warp the flow of light around your ship. In a dense dust cloud, if you remain completely stationary, you will be virtually invisible, until the enemy is right on top of you.'
        ),
        VoiceLine(
            50,
            Trent,
            ru='Будем изображать из себя ниндзя?',
               en='So, we\'re ninjas now?'
        ),
        VoiceLine(
            60,
            HasslerOrder,
            ru='Придется. Кс+еносы очень не любят чужаков. А чужаков, которые приближаются к их тюрьме с намерением выкрасть парочку заключенных, они не любят особенно сильно.',
               en='Stealth is essential, Herr Trent. The Xenos do not care for outsiders. And for some reason they are particularly unwelcoming to outsiders staging a jailbreak.'
        ),

        VoiceLine(70, HasslerOrder, ru='Трент, ты ведешь звено Локи. Уничтожьте защитные системы и дайте нам сигнал '
                                        'в случае успеха. Карта местности загружена в компьютер Д+ерси.',
                                             en='Trent, you\'re leading Loki Wing. Take out the defense systems then send us the signal '
                                                'when it\'s done. The terrain map has been loaded into Darcy\'s computer.'),
        VoiceLine(80, Darcy, ru='Да, я буду помогать. Трент, лети вперед! Мы полетим за тобой',
                  en='Confirmed, I\'m on it. Trent, go on up ahead! We\'ll follow your lead.'),

        VoiceLine(110, Trent, ru='Панели работают, даже устройство невидимости не нужно.',
                  en='The panels are working. No need for some cloaking device microwaving my ass.'),

        VoiceLine(200, Trent, ru='Я прошел. Что дальше?', en='I\'m through. What\'s next?'),
        VoiceLine(210, Darcy, ru='Мы еще летим. А ты пока отключи местную систему безопасности.',
                  en='We\'re still on route. In the meantime, disable the security system.'),
        VoiceLine(220, Darcy,
                  ru='Я только что передала тебе координаты управляющего аванпоста. '
                     'Только давай осторожно, тут много мин',
                      en='I just sent you the coordinates to the control outpost.'
                          'Be careful, though, it\'s heavily mined.'),

        VoiceLine(300, Trent, ru='Я у аванпоста, он закрыт', en='I\'m at the outpost, it\'s sealed!'),
        VoiceLine(320, Darcy, ru='Трент, ты что как маленький. Там есть дверь. Ты уже умеешь такие взрывать',
                  en='Come on Trent. You should know what to do with doors by now!'),

        VoiceLine(350, Darcy,
                  ru='Давно практиковал хакерские навыки? Определи нужный цвет, стреляя одиночным огнём по цветным блокам',
                      en='Been a while since you dusted off your hacking skills? Identify the target color by shooting single shots at the colored blocks.'),

        VoiceLine(360, Darcy,
                  ru='Твоя нейрос+еть укажет насколько этот цвет близок к нужному. Искомый цвет будет назван "максимальным"',
                      en='Your neural net will show you how close that color is to the target. The color you\'re looking for will be called "MAXIMUM"'),
        VoiceLine(370, Darcy, ru='Найди такой цвет и уничтожь все подобные блоки', en='Find it and destroy all blocks of that color.'),

        VoiceLine(390, Trent, ru='Ладно, будем вспоминать как это делается.', en='Alright, the funny bone\'s connected to the...'),

        VoiceLine(400, Trent, ru='Система взломана.', en='All done. System hacked.'),
        VoiceLine(410, Darcy, ru='Есть! Давай летим к нашему звену. Мы уже готовы к атаке', en='Got it! Let\'s move to rejoin our wing. We\'re ready to attack!'),
        VoiceLine(420, Trent, ru='А чего тут за система защиты, что её надо прям ломать', en='Why the geeky hacker approach anyway? Couldn\'t we just blast our way through?'),
        VoiceLine(430, Darcy, ru='Тяжелые турели, которые защищают проход без мин. Он самый простой и безопасный. Конечно когда турели в+ыключены',
                  en='The ingress is guarded by heavy turrets covering a tiny mine-free passage. We just took the turrets offline.'),

        VoiceLine(450, Darcy,
                  ru='Давай Трент, командуй парадом. Резко подлетаем к базе и разносим орудийные платформы вокруг неё',
                      en='Trent, lead us in. We need to get as close to the base as we can undetected, and take out the gun emplacements!'),

        VoiceLine(470, Darcy,
                  ru='Огонь по орудийным платформам, пока Кс+еносы не вызвали подкрепление!',
                      en='Fire on the gun platforms before the Xenos call for backup!'),
        VoiceLine(490, Darcy, ru='Платформа сбита', en='One Platform down!'),
        VoiceLine(500, Darcy, ru='Еще три штуки!', en='Three more to go!'),
        VoiceLine(510, Darcy, ru='Осталось две платформы!', en='Two platforms left!'),
        VoiceLine(520, Darcy, ru='Осталась последняя!', en='Last one!'),
        VoiceLine(530, Darcy, ru='Тор, платформы сбиты. Выдвигайтесь к нам!', en='Thor, the platforms are down. Move to our position!'),

        VoiceLine(550, Tor, ru='Тор с эскортом в пути. Обеспечьте нашу безопасность', en='Thor and escort are en route. Provide us with cover!'),

        VoiceLine(570, HasslerOrder, ru='+Один и Тор на месте. Трент, Л+оки, обеспечьте прикрытие транспорту.', en='Odin and Thor are on scene. Trent, Loki, provide cover for the transport!'),
        VoiceLine(580, Darcy, ru='Тор сел! Трент, надо раскидать Кс+еносов, чтобы Тор смог безопасно покинуть базу!', en='Thor has landed! Trent, we need to clear out the Xenos so Thor can evacuate safely!'),

        VoiceLine(600, Tor, ru='Тор на связи, груз упакован.', en='Thor here, the package is secured!'),
        VoiceLine(620, Darcy, ru='Отлично! Продолжаем давить истребители кс+еносов!', en='Excellent! Everyone, keep pressure on the Xeno fighters!'),

        VoiceLine(650, HasslerOrder, ru='Тор покинул зону битвы. Трент, Д+ерси, Л+оки, выход+ите из зоны сражения', en='Thor has left the combat zone. Trent, Darcy, Loki, disengage!'),
        VoiceLine(670, Darcy, ru='Так точно Хасслер! Трент, летим по указанной точке пути', en='Copy that, Hassler! Trent, head for the designated waypoint!'),

        VoiceLine(700, Darcy, ru='Миссия выполнена! Все сад+имся на Мус+аси. Трент, садись первым', en='Mission accomplished! Everyone dock with the Musashi. Trent, you go first!'),
    ]


class Msn10RescuedCutscene(Msn10, script.CutsceneProps):
    ALIAS = 'rescued'
    TITLE = 'Ангар линкора Мусаси'
    THORN_CLASS = m10_rescued.Msn10RescuedCutsceneThorn
    THORN_DECISION_CLASS = m10_rescued.Msn10RescuedDecisionThorn
    THORN_ACCEPT_CLASS = m10_rescued.Msn10RescuedAcceptThorn
    DESCRIPTION = 'Поздравления со спасением'
    VOICE_LINES = [
        VoiceLine(
            10,
            Alaric,
            ru='Как я рад тебя видеть,, дружище!!! Ты нас спас. А я уже думал сдохну в этой дыре',
               en='I\'m so glad to see you, my friend!!! You saved us. I was starting to think I was gonna die in that shit hole!'
        ),
        VoiceLine(
            20,
            Trent,
            ru='(Подкалываем по доброму) Никто больше не соглашался вытаскивать твою задницу из лап сектантов, вот и пришлось мне... Хотя, я уже подумывал оставить тебя там, в назидание.',
               en='Yeah, they couldn\'t find anybody else dumb enough to volunteer to rescue your ass... Although, truth be told I was considering leaving you in there as a lesson.'
        ),
        VoiceLine(
            30,
            Alaric,
            ru='Дружище, я там с одним хорошим человеком познакомился. Ты сейчас охренеешь. Итак... Мистер Трент, познакомьтесь, мистер Трент.',
            en='Buddy, I met this incredible man in there. I\'ve been waiting to say this... Mister Trent, meet Mister Trent.'
        ),
        VoiceLine(
            40,
            Trent,
            ru='(Обалдевание) Очень приятно. Не каждый день получается вот так запросто поболтать с легендой.',
               en='It\'s an honour to finally meet the Hero of the Nomad War! Strange place to meet the living legend...'
        ),
        VoiceLine(
            50,
            EdisonTrent,
            ru='Вытащить легенду из передряги, в которой ей угораздило утонуть с головой по собственной глупости, вы хотели сказать. Предрекаю вам блестящее будущее.',
               en='It\'s all over your face. "How did the legendary Hero of the Nomad War manage to get himself locked up in a crummy Xeno prison?" I\'ll save you the trouble. Stupidity and carelessness. I predict a brilliant future for you.'
        ),
        VoiceLine(
            60,
            Trent,
            ru='Неужели в правительство пробьюсь?',
               en='What, I\'ll become a politician, rising star, rise to presidency one day?'
        ),
        VoiceLine(
            70,
            EdisonTrent,
            ru='Не смешите меня, ком+у нужны эти правительства?',
               en='Don\'t make me laugh. Who needs those government types anyway?'
        ),
        VoiceLine(
            80,
            HasslerOrder,
            ru='Герр Трент, фрау Зейн передаёт, что лорду Ямамото срочно нужна ваша помощь!',
               en='Herr Trent, Frau Zane informs me that Lord Yamamoto urgently requires your assistance!'
        ),
        VoiceLine(
            90,
            EdisonTrent,
            ru='Если фрау Зейн, то это меня. Рад знакомству, мистер Трент!',
               en='If it\'s from Frau Zane then it\'s this Herr Trent she\'s asking for. A pleasure to meet you, Trent!'
        ),
        VoiceLine(
            100,
            HasslerOrder,
            comment='Старый Трент уходит',
            ru='Герр Трент, лейтенант Ким обнаружил Р+окфорда.',
               en='Herr Trent, Lieutenant Kim has located Rockford.'
        ),
        VoiceLine(
            110,
            Trent,
            ru='А если лейтенант Ким - то это,, видимо меня.',
               en='And that\'s Lieutenant Kim... then it\'s for this Herr Trent.'
        ),
        VoiceLine(
            120,
            Darcy,
            ru='В последнее время немудрено запутаться в этих Трентах.',
               en='Starting to get a bit confused by all these Herr Trents.'
        ),
        VoiceLine(
            130,
            Trent,
            ru='И где же Р+окфорд?',
               en='So, have you tracked down Rockford?'
        ),
        VoiceLine(
            140,
            HasslerOrder,
            ru='На станции Харадзюку, система Омега 7. Мы планируем подорвать корабль герра Р+окфорда, но для осуществления миссии нам необходимо чтобы вы отвлекли его на себя.',
               en='Harajuku Station, Omega-7 system. We plan to blow up Herr Rockford\'s ship, but we\'ll need you to draw his attention while we do it.'
        ),
        VoiceLine(
            150,
            Trent,
            ru='Хасслер, а ты всех "геррами" называешь? Даже таких засранцев,, как Р+окфорд.',
               en='Hassler, you call everyone "Herr"? Even scumbags like Rockford?'
        ),
        VoiceLine(
            160,
            HasslerOrder,
            ru='К сожалению... Чертово воспитание дает о себе знать.',
               en='Unfortunately... A good upbringing with a loving family is hard to shake. Bah!'
        ),
        VoiceLine(
            170,
            Trent,
            ru='Хорошо, я в деле',
               en='Alright, Let\'s do this!'
        ),
    ]


class Msn10FinalCutscene(Msn10, script.CutsceneProps):
    ALIAS = 'final'
    TITLE = 'Бар линкора Мусаси'
    THORN_CLASS = m10_final.Msn10FinalCutsceneThorn
    DESCRIPTION = 'Трент подошел к Аларику обсудить планы на будущее'
    VOICE_LINES = [
        VoiceLine(
            10,
            Trent,
            ru='Ну к+ак т+ы, узник замка Иф, невольник чести?',
               en='So, how are you holding up, ex-prisoner of Azkaban?'
        ),
        VoiceLine(
            20,
            Alaric,
            ru='Теперь - отлично. А там... Я уже с жизнью прощался.',
               en='Right now? Good. I thought I was a goner back there. And the dement..ia was real.'
        ),
        VoiceLine(
            30,
            Trent,
            ru='А нахрена полез-то во всё это',
               en='Why the hell did you get involved with the Order in the first place?!'
        ),
        VoiceLine(
            40,
            Alaric,
            ru='А как еще? У тебя есть крутой друг, который на одном месте вертел спецслужбы сразу нескольких государств, '
               'жёг врагов пачками и всегда выходил сухим из воды.',
               en='What was I supposed to do? My best friend was running circles around the intelligence agencies of multiple states,'
                  'burning through enemies, and coming out smelling like roses.'
        ),
        VoiceLine(
            50,
            Alaric,
            ru='Надо же как-то соответствовать... Вот я и решил... Когда ко мне обратились... Тоже поиграть в спецагентов.',
               en='I felt like I needed to match up... So when they approached me... I thought I\'d try my hand at espionage too.'
        ),
        VoiceLine(
            60,
            Trent,
            ru='Балбес ты, Аларик... Слушай, достало меня всё это. Может сольёмся отсюда по-тихому?',
               en='You idiot... Listen up, I never enjoyed this one bit. All this spy kids stuff is shit. What about we just slip away quietly?'
        ),
        VoiceLine(
            70,
            Alaric,
            ru='Это как?',
               en='How do you mean?'
        ),
        VoiceLine(
            80,
            Trent,
            ru='Это мы сад+имся в свои корабли и уходим м+олча, по-англ+ийски. '
               'Не думаю, что нас начнут расстреливать сразу после отстыковки.',
               en='Get in our ships and just go. Wham bam, thank you ma\'am. Like right proper Englishmen. '
                  'I doubt they\'ll start shooting when we undock and afterburner the hell out of here.'
        ),
        VoiceLine(
            90,
            Trent,
            ru='А там - рванем в приграничье, будем выполнять обычные заказы за толику малую. А то меня от этой политики уже тошнит. '
               'Я уже запутался кто против кого, и за кого сейчас я!',
               en='Then we make a run for the Border Worlds, take on some simple jobs for a change. I\'m so sick of politics. '
                  'I\'ve lost track of who\'s who, who\'s fighting who, and who I am today!!'
        ),
        VoiceLine(
            100,
            Alaric,
            ru='Да поздно уже когти рвать-то. Улетишь ты в приграничье, '
               'а за тобой через недельку какой-нибудь Хасслер вылетит, и вежливо так прикончит. ',
               en='Forget it, Trent. You know it\'s too late to back out now. Fly off to the Border Worlds, '
                  'a week later some Hassler type will show up and put a bullet in your head after shaking your hand.'
        ),
        VoiceLine(
            105,
            Alaric,
            ru='Слишком уж мы с тобой в этом увязли, дружище, слишком много знаем.',
               en='We\'re in too deep, my friend. As they say, we know too much.'
        ),
        VoiceLine(
            110,
            Trent,
            ru='Да... И главная причина - ужасно досмотреть хочется, чем всё закончится.',
               en='Yeah... ah hell. Anyway I\'m dying to see how this story ends.'
        ),
        VoiceLine(
            120,
            Alaric,
            ru='Ага...',
               en='Yeah...'
        ),
        VoiceLine(
            130,
            Trent,
            ru='Да ладно, не смотри ты так, никуда я не смоюсь, ты же без меня опять во что-нибудь вляпаешься... ',
               en='Aww come on, don\'t look at me like that. I\'m not going anywhere. You\'ll just get in trouble again without me...'
        ),
        VoiceLine(
            140,
            Trent,
            ru='Досмотрим этот боевичёк до конца. (в сторону) Пока еще не ясно, до чьег+о конца!',
               en='Let\'s see this epic mess through to the end. Whoever\'s end it be!'
        ),
        VoiceLine(
            200,
            EdisonTrent,
            comment='После ухода главного героя из бара',
            ru='А этот парень хор+ош, способный товарищ. Как думаешь?',
               en='That kid\'s got the chops. What do you think?'
        ),
        VoiceLine(
            210,
            Juni,
            ru='Такой же безрассудный,, как и ты. Помогает местным фанатикам, а лучше бы их остановил.',
               en='As dumb and reckless as you were. Enabling the fanatics instead of reigning them in.'
        ),
        VoiceLine(
            220,
            EdisonTrent,
            ru='А кто их остановит? Ты думаешь я смогу уломать Ямамото? Он же упёртый похлеще Ор+илиона с Кингом вместе взятыми.',
               en='Well who\'s going to stop them? You think I can talk Yamamoto down? He\'s more stubborn than Orillion and King put together on a bad day.'
        ),
        VoiceLine(
            230,
            Juni,
            ru='Упёртый,, алчный и коварный. И Ор+илиона больше нет,, чтобы его остановить.',
               en='He\'s stubborn, and greedy, and cunning. And without Orillion around to keep him in check...'
        ),
        VoiceLine(
            240,
            EdisonTrent,
            ru='Да. Вот я и боюсь делать по твоему плану А. Но у меня есть свой план Бэ... ',
               en='Yeah. You\'re right. Yamamoto\'s a loose cannon. So I\'m no fan, but let\'s stick to Plan A. But if that falls through, we pivot to Plan B...'
        ),
    ]


class Mission10(Msn10, script.StoryMission):
    CUTSCENES = [
        Msn10OfferCutscene,
        Msn10RescuedCutscene,
        Msn10FinalCutscene,
    ]
    SPACE_CLASS = Msn10Space
    SYNC_SPACE = True

    MISSION_TITLE = 'Миссия 10. Вызволение заключенных'