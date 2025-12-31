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
               en='Herr Trent, Frau Darcy!'
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
               en='Excuse me, but I believe we gathered here to discuss matters slightly more pressing than linguistic formalities.'
        ),
        VoiceLine(
            60,
            HasslerOrder,
            ru='Йа! Точно так. К делу! Наши недавние... хмммм... манёвры, а так же резкая активизация вооруженных сил Р+ейнланда изменили '
               'общую ситуацию не лучшим образом.',
               en='Ja! Exactly. To business! Our recent... hmmm... maneuvers, as well as Rheinland\'s sudden military mobilization,'
                  'have altered the overall situation. For the worse.'
        ),
        VoiceLine(
            70,
            Trent,
            ru='(Дикий сарказм) Кто бы мог подумать, что локальная война с СБА в отдельно взятой системе изменит ситуацию не лучшим образом?',
               en='Who could have possibly imagined that a localized war with the ASF in a single system would alter the situation for the worse?'
        ),
        VoiceLine(
            80,
            HasslerOrder,
            ru='Это было необходимо,, герр Трент... А сейчас мы должн+ы реагировать на изменившуюся ситуацию.',
               en='It was necessary, Herr Trent... And now we must react to the new circumstances.'
        ),
        VoiceLine(
            90,
            Trent,
            ru='Кого убить на этот раз?',
               en='Who do you need me to kill this time?'
        ),
        VoiceLine(
            100,
            HasslerOrder,
            ru='Нет, герр Трент, совсем наоборот. Нужно будет вытащить из тюрьм+ы кс+еносов одного хор+ошего человека, героя войн+ы с кочевниками.',
               en='Nein, Herr Trent, quite the opposite. We need you to break a good man out of the Xeno prison. A hero of the war against the Nomads.'
        ),
        VoiceLine(
            110,
            Trent,
            ru='Войн+ы с кочевниками официально ведь н+е б+ыло.',
               en='There was never an official war with the Nomads.'
        ),
        VoiceLine(
            120,
            HasslerOrder,
            ru='Это не отменяет того,, что были её герои.',
               en='That does not negate the fact that there were heroes in it.'
        ),
        VoiceLine(
            130,
            Trent,
            ru='Пусть так, но при чём тут я?',
               en='Be that as it may, what does this have to do with me?'
        ),
        VoiceLine(
            140,
            HasslerOrder,
            ru='Вы не первый, кто пытался освободить интересующего нас человека. Первым был ваш друг Аларик.',
               en='You are not the first to attempt to free the person in question. The first was your friend, Alaric.'
        ),
        VoiceLine(
            150,
            Trent,
            ru='(Подытожив) И Аларик облажался...',
               en='And Alaric screwed up...'
        ),
        VoiceLine(
            160,
            HasslerOrder,
            ru='Весьма прискорбно, но так и есть. Теперь он содержится в той же тюрьме.',
               en='Most regrettably, yes. Now he is being held in the same prison.'
        ),
        VoiceLine(
            170,
            Trent,
            ru='И вы хотите, чтобы я повторил его подвиг, и нас в тюрьме стало уже трое? И Аларику не скучно, и преферансик на троих можно будет раскинуть.',
               en='And you want me to repeat his glorious feat, so there will be three of us in there? At least Alaric won\'t be bored, and we can play a round of cards.'
        ),
        VoiceLine(
            180,
            HasslerOrder,
            ru='При всём моем уважении к герру Аларику, его способности значительно уступают вашим.',
               en='With all due respect to Herr Alaric, his capabilities are... significantly inferior to your own.'
        ),
        VoiceLine(
            190,
            Trent,
            ru='Хорошо... Если вы так считаете,, герр Хасслер. (тихо, в сторону) Эх как же я задолбался... Задолбался!',
               en='Alright then... If you say so, Herr Hassler. Oh, I\'m so tired of this... And I\'m fresh out of matches.'
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
               en='The prison is in Omega-38. The system is mostly a dust cloud.'
                    'The Musashi will position itself on the system\'s outskirts to avoid drawing local attention.'
        ),
        VoiceLine(
            220,
            HasslerOrder,
            ru='Герр Трент, вы с фр+ойляйн Д+ерси возглавите диверсионное звено. '
               'Ваши корабли получат дополнительную мимикрирующую обработку, чтобы вы могли пробраться к тюрьме незаметно.',
               en='Herr Trent, you and Fräulein Darcy will lead the sabotage wing.'
                  'Your ships will receive additional mimetic coating to allow you to slip into the prison undetected.'
        ),
        VoiceLine(
            230,
            HasslerOrder,
            ru='Вы должн+ы б+удете подавить защитные системы тюрьм+ы. '
               'Следом в дело вступает наш транспорт с десантниками и звено прикрытия.',
               en='Your task is to disable the prison\'s defense systems.'
                  'Then, our transport with the boarding team and an escort wing will move in.'
        ),
        VoiceLine(
            240,
            HasslerOrder,
            ru='После того,, как десант сделает свое дело, все весело и с фейерверками прорываются обратно на Мус+аси.',
               en='Once the boarding party has done its job, everyone makes a... lively and fireworks-filled escape back to the Musashi.'
        ),
        VoiceLine(
            250,
            Trent,
            ru='Звучит заманчиво.',
               en='Sounds tempting.'
        ),
        VoiceLine(
            260,
            Darcy,
            ru='Посмотрим, как окажется на самом деле.',
               en='We\'ll see how it plays out in reality.'
        ),
        VoiceLine(
            270,
            HasslerOrder,
            ru='Тогда можете готовиться к вылету. Я буду координировать операцию с мостика линкора.',
               en='You may prepare for launch then. I will be coordinating the operation from the battleship\'s bridge.'
        ),
    ]


class Msn10Space(Msn10, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(
            10,
            Darcy,
            comment='Взлёт после принятия миссии',
            ru='Эй, Хасслер, чего там твои инженеры шаманили над нашими кораблями?',
               en='Hey, Hassler, what were your engineers tinkering with on our ships?'
        ),
        VoiceLine(
            20,
            HasslerOrder,
            ru='Устанавливали мимикрирующие панели, фр+ойляйн Д+ерси.',
               en='They were installing mimetic panels, Fräulein Darcy.'
        ),
        VoiceLine(
            30,
            HasslerOrder,
            ru='Эти панели снизят вашу заметность на радарах в разы. В зависимости от характера окружающего пространства от двух до семи раз.',
               en='These panels will reduce your radar signature significantly. Depending on the environment, by a factor of two to seven.'
        ),
        VoiceLine(
            40,
            HasslerOrder,
            ru='Кроме того они подстраиваются под характер окружающего пространства визуально. В плотном пылевом облаке если вы не двигаетесь вас можно будет обнаружить только радаром и только вплотную.',
               en='Furthermore, they adapt visually to the surrounding space. In a dense dust cloud, if you remain stationary, you can only be detected by radar and only at point-blank range.'
        ),
        VoiceLine(
            50,
            Trent,
            ru='Будем изображать из себя ниндзя?',
               en='So, we\'re supposed to be ninjas now?'
        ),
        VoiceLine(
            60,
            HasslerOrder,
            ru='Придется. Кс+еносы очень не любят чужаков. А чужаков, которые приближаются к их тюрьме с намерением выкрасть парочку заключенных, они не любят особенно сильно.',
               en='You\'ll have to be. The Xenos do not care for outsiders. And they are particularly unfond of outsiders who approach their prison with the intent of springing a few inmates.'
        ),

        VoiceLine(70, HasslerOrder, ru='Трент, ты ведешь звено Локи. Уничтожьте защитные системы и дайте нам сигнал '
                                        'в случае успеха. Карта местности загружена в компьютер Д+ерси.',
                                             en='Trent, you are leading Loki Wing. Take out the defense systems and give us the signal '
                                                'when it\'s done. The terrain map has been loaded into Darcy\'s computer.'),
        VoiceLine(80, Darcy, ru='Да, я буду помогать. Трент, лети вперед! Мы полетим за тобой',
                  en='Confirmed, I\'m on it. Trent, go on ahead! We\'ll follow your lead.'),

        VoiceLine(110, Trent, ru='Панели работают, даже устройство невидимости не нужно.',
                  en='The panels are working. Don\'t even need a cloaking device.'),

        VoiceLine(200, Trent, ru='Я прошел. Что дальше?', en='I\'m through. What\'s next?'),
        VoiceLine(210, Darcy, ru='Мы еще летим. А ты пока отключи местную систему безопасности.',
                  en='We\'re still on route. In the meantime, disable the local security system.'),
        VoiceLine(220, Darcy,
                  ru='Я только что передала тебе координаты управляющего аванпоста. '
                     'Только давай осторожно, тут много мин',
                      en='I just sent you the coordinates for the control outpost.'
                          'Be careful, though, it\'s heavily mined.'),

        VoiceLine(300, Trent, ru='Я у аванпоста, он закрыт', en='I\'m at the outpost, it\'s sealed!'),
        VoiceLine(320, Darcy, ru='Трент, ты что как маленький. Там есть дверь. Ты уже умеешь такие взрывать',
                  en='Trent, don\'t be such a child. There\'s a door. You know how to blow those up by now!'),

        VoiceLine(350, Darcy,
                  ru='Давно практиковал хакерские навыки? Определи нужный цвет, стреляя одиночным огнём по цветным блокам',
                      en='Been a while since you practiced your hacking skills? Identify the target color by shooting single shots at the colored blocks.'),

        VoiceLine(360, Darcy,
                  ru='Твоя нейрос+еть укажет насколько этот цвет близок к нужному. Искомый цвет будет назван "максимальным"',
                      en='Your neural net will show you how close that color is to the target. The color you\'re looking for will be labeled "MAXIMUM"'),
        VoiceLine(370, Darcy, ru='Найди такой цвет и уничтожь все подобные блоки', en='Find it and destroy all blocks of that color.'),

        VoiceLine(390, Trent, ru='Ладно, будем вспоминать как это делается.', en='Alright, let\'s try to remember how this is done...'),

        VoiceLine(400, Trent, ru='Система взломана.', en='System\'s hacked.'),
        VoiceLine(410, Darcy, ru='Есть! Давай летим к нашему звену. Мы уже готовы к атаке', en='Got it! Let\'s move to join our wing. We\'re ready to attack!'),
        VoiceLine(420, Trent, ru='А чего тут за система защиты, что её надо прям ломать', en='What kind of defense system was so important to crack, anyway?'),
        VoiceLine(430, Darcy, ru='Тяжелые турели, которые защищают проход без мин. Он самый простой и безопасный. Конечно когда турели в+ыключены',
                  en='Heavy turrets guarding the only mine-free passage. It\'s the simplest and safest route. Well, it is now, with the turrets offline.'),

        VoiceLine(450, Darcy,
                  ru='Давай Трент, командуй парадом. Резко подлетаем к базе и разносим орудийные платформы вокруг неё',
                      en='Let\'s go, Trent, lead us in. We need to get close to the base undetected and take out the gun platforms around it!'),

        VoiceLine(470, Darcy,
                  ru='Огонь по орудийным платформам, пока Кс+еносы не вызвали подкрепление!',
                      en='Fire on the gun platforms before the Xenos can call for backup!'),
        VoiceLine(490, Darcy, ru='Платформа сбита', en='Platform down!'),
        VoiceLine(500, Darcy, ru='Еще три штуки!', en='Three more to go!'),
        VoiceLine(510, Darcy, ru='Осталось две платформы!', en='Two platforms left!'),
        VoiceLine(520, Darcy, ru='Осталась последняя!', en='Last one!'),
        VoiceLine(530, Darcy, ru='Тор, платформы сбиты. Выдвигайтесь к нам!', en='Thor, the platforms are down. Move to our position!'),

        VoiceLine(550, Tor, ru='Тор с эскортом в пути. Обеспечьте нашу безопасность', en='Thor and escort are en route. Provide us with cover!'),

        VoiceLine(570, HasslerOrder, ru='+Один и Тор на месте. Трент, Л+оки, обеспечьте прикрытие транспорту.', en='Odin and Thor are on site. Trent, Loki, provide cover for the transport!'),
        VoiceLine(580, Darcy, ru='Тор сел! Трент, надо раскидать Кс+еносов, чтобы Тор смог безопасно покинуть базу!', en='Thor has landed! Trent, we need to clear out the Xenos so Thor can safely leave the base!'),

        VoiceLine(600, Tor, ru='Тор на связи, груз упакован.', en='Thor here, the package is secured!'),
        VoiceLine(620, Darcy, ru='Отлично! Продолжаем давить истребители кс+еносов!', en='Excellent! Keep pressing the Xeno fighters!'),

        VoiceLine(650, HasslerOrder, ru='Тор покинул зону битвы. Трент, Д+ерси, Л+оки, выход+ите из зоны сражения', en='Thor has left the combat zone. Trent, Darcy, Loki, disengage!'),
        VoiceLine(670, Darcy, ru='Так точно Хасслер! Трент, летим по указанной точке пути', en='Copy that, Hassler! Trent, heading for the designated waypoint!'),

        VoiceLine(700, Darcy, ru='Миссия выполнена! Все сад+имся на Мус+аси. Трент, садись первым', en='Mission accomplished! Everyone dock with the Musashi. Trent, you\'re up first!'),
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
               en='I am so glad to see you, my friend!!! You saved us. I was starting to think I\'d die in that hole!'
        ),
        VoiceLine(
            20,
            Trent,
            ru='(Подкалываем по доброму) Никто больше не соглашался вытаскивать твою задницу из лап сектантов, вот и пришлось мне... Хотя, я уже подумывал оставить тебя там, в назидание.',
               en='Nobody else would volunteer to haul your ass out of the clutches of those fanatics, so I had to... Although, I was considering leaving you there as a lesson.'
        ),
        VoiceLine(
            30,
            Alaric,
            ru='Дружище, я там с одним хорошим человеком познакомился. Ты сейчас охренеешь. Итак... Мистер Трент, познакомьтесь, мистер Трент.',
            en='Buddy, I met a really good man in there. You\'re not gonna believe this. So... Mister Trent, meet Mister Trent.'
        ),
        VoiceLine(
            40,
            Trent,
            ru='(Обалдевание) Очень приятно. Не каждый день получается вот так запросто поболтать с легендой.',
               en='A real pleasure! You don\'t get to chat so casually with a living legend every day!'
        ),
        VoiceLine(
            50,
            EdisonTrent,
            ru='Вытащить легенду из передряги, в которой ей угораздило утонуть с головой по собственной глупости, вы хотели сказать. Предрекаю вам блестящее будущее.',
               en='"You rescued a legend from a mess he managed to get himself into headfirst out of sheer stupidity," is what you meant to say. I predict a brilliant future for you.'
        ),
        VoiceLine(
            60,
            Trent,
            ru='Неужели в правительство пробьюсь?',
               en='What, I\'ll make it into the government?'
        ),
        VoiceLine(
            70,
            EdisonTrent,
            ru='Не смешите меня, ком+у нужны эти правительства?',
               en='Don\'t make me laugh. Who needs those governments anyway?'
        ),
        VoiceLine(
            80,
            HasslerOrder,
            ru='Герр Трент, фрау Зейн передаёт, что лорду Ямамото срочно нужна ваша помощь!',
               en='Herr Trent, Frau Zane conveys that Lord Yamamoto urgently requires your assistance!'
        ),
        VoiceLine(
            90,
            EdisonTrent,
            ru='Если фрау Зейн, то это меня. Рад знакомству, мистер Трент!',
               en='If it\'s from Frau Zane, then it\'s me she is asking. A pleasure to meet you, Mister Trent!'
        ),
        VoiceLine(
            100,
            HasslerOrder,
            comment='Старый Трент уходит',
            ru='Герр Трент, лейтенант Ким обнаружил Р+окфорда.',
               en='Herr Trent, Lieutenant Kym has located Rockford.'
        ),
        VoiceLine(
            110,
            Trent,
            ru='А если лейтенант Ким - то это,, видимо меня.',
               en='And if it\'s Lieutenant Kym... then that\'s for me.'
        ),
        VoiceLine(
            120,
            Darcy,
            ru='В последнее время немудрено запутаться в этих Трентах.',
               en='Lately, it\'s not hard to get confused with all these Trents.'
        ),
        VoiceLine(
            130,
            Trent,
            ru='И где же Р+окфорд?',
               en='So, where is Rockford?'
        ),
        VoiceLine(
            140,
            HasslerOrder,
            ru='На станции Харадзюку, система Омега 7. Мы планируем подорвать корабль герра Р+окфорда, но для осуществления миссии нам необходимо чтобы вы отвлекли его на себя.',
               en='At Harajuku Station, Omega-7 system. We plan to detonate Herr Rockford\'s ship, but to carry out the mission, we need you to draw his attention onto yourself.'
        ),
        VoiceLine(
            150,
            Trent,
            ru='Хасслер, а ты всех "геррами" называешь? Даже таких засранцев,, как Р+окфорд.',
               en='Hassler, do you call everyone "Herr"? Even scumbags like Rockford?'
        ),
        VoiceLine(
            160,
            HasslerOrder,
            ru='К сожалению... Чертово воспитание дает о себе знать.',
               en='Unfortunately... My damned upbringing is hard to shake.'
        ),
        VoiceLine(
            170,
            Trent,
            ru='Хорошо, я в деле',
               en='Alright, I\'m in!'
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
               en='So, how are you holding up, prisoner of Azkaban, entrapped by honour?'
        ),
        VoiceLine(
            20,
            Alaric,
            ru='Теперь - отлично. А там... Я уже с жизнью прощался.',
               en='Right now? Great. Back there... I was already saying my goodbyes to life.'
        ),
        VoiceLine(
            30,
            Trent,
            ru='А нахрена полез-то во всё это',
               en='Then why the hell did you get involved in all this in the first place?!'
        ),
        VoiceLine(
            40,
            Alaric,
            ru='А как еще? У тебя есть крутой друг, который на одном месте вертел спецслужбы сразу нескольких государств, '
               'жёг врагов пачками и всегда выходил сухим из воды.',
               en='What else was I supposed to do? You have this badass friend who\'s been running circles around the intelligence agencies of multiple states,'
                  'burning through enemies by the dozen, and always coming out without a scratch.'
        ),
        VoiceLine(
            50,
            Alaric,
            ru='Надо же как-то соответствовать... Вот я и решил... Когда ко мне обратились... Тоже поиграть в спецагентов.',
               en='A guy\'s gotta try to measure up... So I thought... when they approached me... I\'d play the spy game too.'
        ),
        VoiceLine(
            60,
            Trent,
            ru='Балбес ты, Аларик... Слушай, достало меня всё это. Может сольёмся отсюда по-тихому?',
               en='You idiot, Alaric... Listen, I\'m sick of all this. What if we just slip away quietly?'
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
               en='We get in our ships and leave without a word, like proper Englishmen. '
                  'I don\'t think they\'ll start shooting the moment we undock.'
        ),
        VoiceLine(
            90,
            Trent,
            ru='А там - рванем в приграничье, будем выполнять обычные заказы за толику малую. А то меня от этой политики уже тошнит. '
               'Я уже запутался кто против кого, и за кого сейчас я!',
               en='Then we make a run for the Border Worlds, take on simple jobs for small change. I\'m so sick of this politics. '
                  'I\'ve lost track of who\'s against who, and who I\'m even fighting for anymore!'
        ),
        VoiceLine(
            100,
            Alaric,
            ru='Да поздно уже когти рвать-то. Улетишь ты в приграничье, '
               'а за тобой через недельку какой-нибудь Хасслер вылетит, и вежливо так прикончит. ',
               en='It\'s too late to back out now. You fly off to the Border Worlds, '
                  'and a week later some Hassler will show up and politely put a bullet in your head.'
        ),
        VoiceLine(
            105,
            Alaric,
            ru='Слишком уж мы с тобой в этом увязли, дружище, слишком много знаем.',
               en='We\'re in too deep, my friend. We know too much.'
        ),
        VoiceLine(
            110,
            Trent,
            ru='Да... И главная причина - ужасно досмотреть хочется, чем всё закончится.',
               en='Yeah... And the main reason is, I\'m dying to see how this story ends.'
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
               en='Ah, come on, don\'t look at me like that. I\'m not going anywhere. You\'d just get into trouble again without me...'
        ),
        VoiceLine(
            140,
            Trent,
            ru='Досмотрим этот боевичёк до конца. (в сторону) Пока еще не ясно, до чьег+о конца!',
               en='Let\'s see this action movie through to the end. Even if it\'s not yet clear whose end it will be!'
        ),
        VoiceLine(
            200,
            EdisonTrent,
            comment='После ухода главного героя из бара',
            ru='А этот парень хор+ош, способный товарищ. Как думаешь?',
               en='That kid\'s good. A capable fellow. Don\'t you think?'
        ),
        VoiceLine(
            210,
            Juni,
            ru='Такой же безрассудный,, как и ты. Помогает местным фанатикам, а лучше бы их остановил.',
               en='As reckless as you are. He\'s helping the local fanatics instead of stopping them.'
        ),
        VoiceLine(
            220,
            EdisonTrent,
            ru='А кто их остановит? Ты думаешь я смогу уломать Ямамото? Он же упёртый похлеще Ор+илиона с Кингом вместе взятыми.',
               en='And who\'s going to stop them? Do you think I can talk Yamamoto down? He\'s more stubborn than Orillion and King put together.'
        ),
        VoiceLine(
            230,
            Juni,
            ru='Упёртый,, алчный и коварный. И Ор+илиона больше нет,, чтобы его остановить.',
               en='Stubborn, greedy, and cunning. And Orillion is no longer here to keep him in check.'
        ),
        VoiceLine(
            240,
            EdisonTrent,
            ru='Да. Вот я и боюсь делать по твоему плану А. Но у меня есть свой план Бэ... ',
               en='Yeah. That\'s why I\'m afraid to go with your Plan A. But I have my own Plan B...'
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
