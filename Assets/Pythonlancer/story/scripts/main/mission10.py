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
            ru='Герр Трент, фрау Дерси, вы готовы к следующей операции?',
               en='Herr Trent, Frau Darcy, are you ready for the next operation?'
        ),
        VoiceLine(
            20,
            Darcy,
            ru='Ты опять пошлешь нас воевать с моими союзниками. А, Хасслер?',
               en='You\'re going to send us to fight my allies again. Right, Hassler?'
        ),
        VoiceLine(
            30,
            HasslerOrder,
            ru='На этот раз нет. Эта операция будет более локальной.',
               en='Not this time. This operation will be more local.'
        ),
        VoiceLine(
            40,
            Darcy,
            ru='Тогда не томи, Хасслер. Переходи к делу.',
               en='Then don\'t drag it out, Hassler. Get to the point.'
        ),
        VoiceLine(
            60,
            HasslerOrder,
            ru='Хорошо! Итак, наши недавние... хмммм... манёвры, а так же резкая активизация вооруженных сил Р+ейнланда изменили '
               'общую ситуацию не лучшим образом.',
               en='Good! So, our recent... hmmm... maneuvers, as well as the sharp increase in activity of Rheinland\'s armed forces, have changed the overall situation not for the better.'
        ),
        VoiceLine(
            70,
            Trent,
            ru='(Дикий сарказм) Кто бы мог подумать, что локальная война с СБА в отдельно взятой системе изменит ситуацию не лучшим образом?',
               en='(savage sarcasm) Who could have thought that a local war with the ASF in one particular system would change the situation not for the better?'
        ),
        VoiceLine(
            80,
            HasslerOrder,
            ru='Это было необходимо,, герр Трент... А сейчас мы должн+ы реагировать на изменившуюся ситуацию.',
               en='It was necessary, Herr Trent... And now we must respond to the changed situation.'
        ),
        VoiceLine(
            90,
            Trent,
            ru='Кого убить на этот раз?',
               en='Who are we killing this time?'
        ),
        VoiceLine(
            100,
            HasslerOrder,
            ru='Нет, герр Трент, совсем наоборот. Нужно будет вытащить из тюрьм+ы Кс+еносов одного хор+ошего человека, героя войн+ы с кочевниками.',
               en='No, Herr Trent, quite the opposite. We\'ll need to pull one good man out of a Xeno prison, a hero of the war with the nomads.'
        ),
        VoiceLine(
            110,
            Trent,
            ru='Войн+ы с кочевниками официально ведь н+е б+ыло.',
               en='There was no war with the nomads, officially.'
        ),
        VoiceLine(
            120,
            HasslerOrder,
            ru='Это не отменяет того факта,, что были её герои.',
               en='That doesn\'t change the fact that it had its heroes.'
        ),
        VoiceLine(
            130,
            Trent,
            ru='Пусть так, но при чём тут я?',
               en='Fine, but what\'s it got to do with me?'
        ),
        VoiceLine(
            140,
            HasslerOrder,
            ru='Вы не первый, кто пытался освободить интересующего нас человека. Первым был ваш друг Аларик.',
               en='You\'re not the first who tried to free the man we\'re interested in. The first was your friend Alaric.'
        ),
        VoiceLine(
            150,
            Trent,
            ru='(Подытожив) И Аларик облажался...',
               en='(summing up) And Alaric screwed up...'
        ),
        VoiceLine(
            160,
            HasslerOrder,
            ru='Весьма прискорбно, но так и есть. Теперь он содержится в той же тюрьме.',
               en='Most regrettable, but so it is. Now he\'s being held in the same prison.'
        ),
        VoiceLine(
            170,
            Trent,
            ru='И вы хотите, чтобы я повторил его подвиг, и нас в тюрьме стало уже трое? И Аларику не скучно, и преферансик на троих можно будет раскинуть.',
               en='And you want me to repeat his feat, so there\'ll already be three of us in prison? Alaric won\'t be bored, and we can deal a three-handed game of preference.'
        ),
        VoiceLine(
            180,
            HasslerOrder,
            ru='При всём моем уважении к герру Аларику, его способности значительно уступают вашим, герр Трент.',
               en='With all my respect for Herr Alaric, his abilities are significantly inferior to yours, Herr Trent.'
        ),
        VoiceLine(
            190,
            Trent,
            ru='Хорошо... Если вы так считаете,, герр Хасслер. (тихо, в сторону) Эх как же я задолбался... Задолбался!',
            en='All right... If that\'s what you think, Herr Hassler. (quietly, aside) God, I\'m so sick of this... Sick of it!'
        ),
        # место для принятия миссии
        VoiceLine(
            200,
            Trent,
            ru='(Выдохнув) Ладно, каков план?',
               en='(exhaling) All right, what\'s the plan?'
        ),
        VoiceLine(
            210,
            HasslerOrder,
            ru='Тюрьма находится в Омега-38. Система представляет собой по большей части пылевое облако. '
                'Мус+аси переместится на окраину системы таким образом,, чтобы не привлечь внимание аборигенов.',
               en='The prison is in Omega-38. The system is mostly a dust cloud. The Musashi will move to the edge of the system so as not to attract the natives\' attention.'
        ),
        VoiceLine(
            220,
            HasslerOrder,
            ru='Герр Трент, вы с фр+ойляйн Д+ерси возглавите диверсионное звено. '
               'Ваши корабли получат дополнительную мимикрирующую обработку, чтобы вы могли пробраться к тюрьме незаметно.',
               en='Herr Trent, you and Fräulein Darcy will lead the sabotage wing. Your ships will receive additional mimetic treatment so you can get to the prison unnoticed.'
        ),
        VoiceLine(
            230,
            HasslerOrder,
            ru='Вы должн+ы б+удете подавить защитные системы тюрьм+ы. '
               'Следом в дело вступает наш транспорт с десантниками и звено прикрытия.',
               en='You will have to suppress the prison\'s defense systems. Then our transport with the assault troops and a cover wing come into play.'
        ),
        VoiceLine(
            240,
            HasslerOrder,
            ru='После того,, как десант сделает свое дело, все весело и с фейерверками прорываются обратно на Мус+аси.',
               en='After the landing party does its job, everyone breaks back through to the Musashi, merrily and with fireworks.'
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
               en='We\'ll see how it actually turns out.'
        ),
        VoiceLine(
            270,
            HasslerOrder,
            ru='Тогда можете готовиться к вылету. Я буду координировать операцию с мостика Мусаси.',
               en='Then you may prepare for launch. I\'ll be coordinating the operation from the Musashi\'s bridge.'
        ),
    ]


class Msn10Space(Msn10, script.SpaceVoiceProps):
    VOICE_LINES = [
        # VoiceLine(
        #     10,
        #     Darcy,
        #     comment='Взлёт после принятия миссии',
        #     ru='Эй, Хасслер, чего там твои инженеры шаманили над нашими кораблями?',
        #        en='Hey, Hassler, what were your engineers doing to our ships?'
        # ),
        VoiceLine(
            20,
            HasslerOrder,
            ru='Господа, на ваши корабли были установлены особые мимикрирующие панели. Они заметно снизят вашу заметность на радарах, пока вы будете находиться в туманности.',
               en='Gentlemen, special mimetic panels have been installed on your ships. They will noticeably reduce your radar visibility while you\'re in the nebula.'
        ),
        # VoiceLine(
        #     30,
        #     HasslerOrder,
        #     ru='ы. В зависимости от характера окружающего пространства от двух до семи раз.',
        #        en='These panels will significantly reduce your radar signatures. Depending on the environment, by a factor of two up to seven.'
        # ),
        # VoiceLine(
        #     40,
        #     HasslerOrder,
        #     ru='Кроме того они подстраиваются под характер окружающего пространства визуально. В плотном пылевом облаке если вы не двигаетесь вас можно будет обнаружить только радаром и только вплотную.',
        #        en='They also react to the surrounding space and warp the flow of light around your ship. In a dense dust cloud, if you remain completely stationary, you will be virtually invisible, until the enemy is right on top of you.'
        # ),
        VoiceLine(
            50,
            Trent,
            ru='Будем изображать из себя ниндзя?',
               en='We\'ll pretend to be ninjas?'
        ),
        VoiceLine(
            60,
            HasslerOrder,
            ru='Придется. Кс+еносы очень не любят чужаков. Особенно тех чужаков, которые приближаются к местной тюрьме с намерением выкрасть парочку заключенных.',
            en='We\'ll have to. The Xenos really don\'t like outsiders. Especially outsiders who approach the local prison intending to snatch a couple of prisoners.'
        ),

        VoiceLine(70, HasslerOrder, ru='Трент, ты ведешь звено Локи. Уничтожьте защитные системы и в случае успеха дайте нам сигнал. Карта местности загружена в компьютер Д+ерси.',
                                             en='Trent, you\'re leading Loki wing. Destroy the defense systems and, if you succeed, give us the signal. The terrain map is loaded into Darcy\'s computer.'),
        VoiceLine(80, Darcy, ru='Да, я буду помогать. Трент, лети вперед! Мы полетим за тобой',
                  en='Yes, I\'ll be helping. Trent, fly ahead! We\'ll fly after you.'),

        VoiceLine(110, Trent, ru='Панели работают, даже устройство невидимости не нужно.',
                  en='The panels are working. Don\'t even need an invisibility device.'),

        VoiceLine(200, Trent, ru='Я прошел. Что дальше?', en='I\'m through. What\'s next?'),
        VoiceLine(210, Darcy, ru='Мы еще летим. А ты пока отключи местную систему безопасности.',
                  en='We\'re still flying. Meanwhile, you switch off the local security system.'),
        VoiceLine(220, Darcy,
                  ru='Я только что передала тебе координаты управляющего аванпоста. '
                     'Только давай осторожно, тут много мин',
                      en='I just sent you the coordinates of the control outpost. Just be careful, there are a lot of mines here.'),

        VoiceLine(300, Trent, ru='Я у аванпоста, он закрыт', en='I\'m at the outpost. It\'s closed.'),
        VoiceLine(320, Darcy, ru='Трент, ты что как маленький. Там есть дверь. Ты уже умеешь такие взрывать',
                  en='Trent, you\'re like a little kid. There\'s a door there. You already know how to blow those up.'),

        VoiceLine(350, Darcy,
                  ru='Давно практиковал хакерские навыки? Определи нужный цвет, стреляя одиночным огнём по цветным блокам',
                      en='Been a while since you practiced your hacking skills? Identify the right color by firing single shots at the colored blocks.'),

        VoiceLine(360, Darcy,
                  ru='Твоя нейрос+еть укажет насколько этот цвет близок к нужному. Искомый цвет будет назван "максимальным"',
                      en='Your neural net will indicate how close that color is to the right one. The color you\'re looking for will be called "maximum".'),
        VoiceLine(370, Darcy, ru='Найди такой цвет и уничтожь все подобные блоки', en='Find that color and destroy all blocks like it.'),

        VoiceLine(390, Trent, ru='Ладно, будем вспоминать как это делается.', en='All right, time to remember how this is done.'),

        VoiceLine(400, Trent, ru='Система взломана.', en='System hacked.'),
        VoiceLine(410, Darcy, ru='Есть! Давай летим к нашему звену. Мы уже готовы к атаке', en='Got it! Let\'s fly to our wing. We\'re already ready to attack.'),
        VoiceLine(420, Trent, ru='А чего тут за система защиты, что её надо прям ломать', en='And what\'s with this defense system that we have to actually crack it?'),
        VoiceLine(430, Darcy, ru='Тяжелые турели, которые защищают проход без мин. Он самый простой и безопасный. Конечно когда турели в+ыключены',
                  en='Heavy turrets guarding the mine-free passage. It\'s the simplest and safest. When the turrets are off, of course.'),

        VoiceLine(450, Darcy,
                  ru='Давай Трент, командуй парадом. Резко подлетаем к базе и разносим орудийные платформы вокруг неё',
                      en='Come on, Trent, lead the parade. We fly in fast on the base and smash the gun platforms around it.'),

        VoiceLine(470, Darcy,
                  ru='Огонь по орудийным платформам, пока Кс+еносы не вызвали подкрепление!',
                      en='Fire on the gun platforms before the Xenos call in reinforcements!'),
        VoiceLine(490, Darcy, ru='Платформа сбита', en='Platform down.'),
        VoiceLine(500, Darcy, ru='Еще три штуки!', en='Three more!'),
        VoiceLine(510, Darcy, ru='Осталось две платформы!', en='Two platforms left!'),
        VoiceLine(520, Darcy, ru='Осталась последняя!', en='The last one left!'),
        VoiceLine(530, Darcy, ru='Тор, платформы сбиты. Выдвигайтесь к нам!', en='Thor, the platforms are down. Move to us!'),

        VoiceLine(550, Tor, ru='Тор с эскортом в пути. Обеспечьте нашу безопасность', en='Thor and escort are on the way. See to our safety.'),

        VoiceLine(570, HasslerOrder, ru='+Один и Тор на месте. Трент, Л+оки, обеспечьте прикрытие транспорту.', en='Odin and Thor are on site. Trent, Loki, provide cover for the transport.'),
        VoiceLine(580, Darcy, ru='Тор сел! Трент, надо раскидать Кс+еносов, чтобы Тор смог безопасно покинуть базу!', en='Thor has landed! Trent, we need to scatter the Xenos so Thor can leave the base safely!'),

        VoiceLine(600, Tor, ru='Тор на связи, груз упакован.', en='Thor here. The cargo is packed.'),
        VoiceLine(620, Darcy, ru='Отлично! Продолжаем давить истребители кс+еносов!', en='Excellent! Keep pressing the Xeno fighters!'),

        VoiceLine(650, HasslerOrder, ru='Тор покинул зону битвы. Трент, Д+ерси, Л+оки, выход+ите из зоны сражения', en='Thor has left the battle zone. Trent, Darcy, Loki, leave the combat zone.'),
        VoiceLine(670, Darcy, ru='Так точно Хасслер! Трент, летим по указанной точке пути', en='Yes, sir, Hassler! Trent, we\'re flying to the designated waypoint.'),

        VoiceLine(700, Darcy, ru='Миссия выполнена! Все сад+имся на Мус+аси. Трент, садись первым', en='Mission complete! Everyone dock with the Musashi. Trent, you dock first.'),
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
               en='Am I glad to see you, buddy!!! You saved us. I already thought I\'d die in this hole.'
        ),
        VoiceLine(
            20,
            Trent,
            ru='(Подкалываем по доброму) Никто больше не соглашался вытаскивать твою задницу из лап сектантов, вот и пришлось мне... Хотя, я уже подумывал оставить тебя там, в назидание.',
               en='(teasing kindly) Nobody else would agree to pull your ass out of the cultists\' clutches, so I had to... Although I was already thinking of leaving you there as a lesson.'
        ),
        VoiceLine(
            30,
            Alaric,
            ru='Дружище, я там с одним хорошим человеком познакомился. Ты сейчас охренеешь. Итак... Мистер Трент, познакомьтесь, мистер Трент.',
            en='Buddy, I met one good man in there. You\'re about to lose it. So... Mister Trent, meet Mister Trent.'
        ),
        VoiceLine(
            40,
            Trent,
            ru='(Обалдевание) Очень приятно. Не каждый день получается вот так запросто поболтать с легендой.',
               en='(stunned) Pleased to meet you. It\'s not every day you get to just chat with a legend.'
        ),
        VoiceLine(
            50,
            EdisonTrent,
            ru='Вытащить легенду из передряги, в которой ей угораздило утонуть с головой по собственной глупости, вы хотели сказать. Предрекаю вам блестящее будущее.',
               en='Pull the legend out of the mess it was stupid enough to drown in, head and all, you meant to say. I predict a brilliant future for you.'
        ),
        VoiceLine(
            60,
            Trent,
            ru='Неужели в правительство пробьюсь?',
               en='You mean I\'ll break into the government?'
        ),
        VoiceLine(
            70,
            EdisonTrent,
            ru='Не смешите меня, ком+у нужны эти правительства?',
               en='Don\'t make me laugh. Who needs these governments?'
        ),
        VoiceLine(
            80,
            HasslerOrder,
            ru='Герр Трент, фрау Зейн передаёт, что лорду Ямамото срочно нужна ваша помощь!',
               en='Herr Trent, Frau Zane sends word that Lord Yamamoto urgently needs your help!'
        ),
        VoiceLine(
            90,
            EdisonTrent,
            ru='Если фрау Зейн, то это меня. Рад знакомству, мистер Трент!',
               en='If it\'s Frau Zane, then that\'s for me. Pleased to meet you, Mister Trent!'
        ),
        VoiceLine(
            100,
            HasslerOrder,
            comment='Старый Трент уходит',
            ru='Герр Трент, лейтенант Ким обнаружил Р+окфорда.',
               en='Herr Trent, Lieutenant Kim has found Rockford.'
        ),
        VoiceLine(
            110,
            Trent,
            ru='А если лейтенант Ким - то это,, видимо меня.',
               en='And if it\'s Lieutenant Kim, then that\'s apparently for me.'
        ),
        VoiceLine(
            120,
            Darcy,
            ru='В последнее время немудрено запутаться в этих Трентах.',
               en='Lately it\'s no wonder you get these Trents mixed up.'
        ),
        VoiceLine(
            130,
            Trent,
            ru='И где же Р+окфорд?',
               en='And where is Rockford?'
        ),
        VoiceLine(
            140,
            HasslerOrder,
            ru='На станции Харадзюку, система Омега-7. Мы планируем подорвать корабль герра Р+окфорда, но для осуществления миссии нам необходимо чтобы вы отвлекли Р+окфорда на себя.',
               en='At Harajuku Station, Omega-7 system. We plan to blow up Herr Rockford\'s ship, but to carry out the mission we need you to draw Rockford onto yourself.'
        ),
        VoiceLine(
            150,
            Trent,
            ru='Хасслер, а ты всех "геррами" называешь? Даже таких засранцев,, как Р+окфорд.',
               en='Hassler, do you call everyone "Herr"? Even assholes like Rockford.'
        ),
        VoiceLine(
            160,
            HasslerOrder,
            ru='К сожалению... Чертово воспитание дает о себе знать.',
               en='Unfortunately... Damn upbringing makes itself known.'
        ),
        VoiceLine(
            170,
            Trent,
            ru='Хорошо, я в деле',
               en='All right, I\'m in.'
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
               en='So how are you, prisoner of the Château d\'If, slave of honor?'
        ),
        VoiceLine(
            20,
            Alaric,
            ru='Теперь - отлично. А там... Я уже с жизнью прощался.',
               en='Now, fine. But there... I was already saying goodbye to life.'
        ),
        VoiceLine(
            30,
            Trent,
            ru='А нахрена полез-то во всё это',
               en='And why the hell did you get into all this?'
        ),
        VoiceLine(
            40,
            Alaric,
            ru='А как еще? У тебя есть крутой друг, который на одном месте вертел спецслужбы сразу нескольких государств, '
               'жёг врагов пачками и всегда выходил сухим из воды.',
               en='What else? You\'ve got a tough friend who didn\'t give a damn about the intelligence services of several states at once, burned enemies in batches, and always came out dry.'
        ),
        VoiceLine(
            50,
            Alaric,
            ru='Надо же как-то соответствовать... Вот я и решил... Когда ко мне обратились... Тоже поиграть в спецагентов.',
               en='Had to measure up somehow... So I decided... When they came to me... To play secret agent too.'
        ),
        VoiceLine(
            60,
            Trent,
            ru='Балбес ты, Аларик... Слушай, достало меня всё это. Может сольёмся отсюда по-тихому?',
               en='You fool, Alaric... Listen, I\'m sick of all this. Maybe we slip out of here quietly?'
        ),
        VoiceLine(
            70,
            Alaric,
            ru='Это как?',
               en='How\'s that?'
        ),
        VoiceLine(
            80,
            Trent,
            ru='Это мы сад+имся в свои корабли и уходим м+олча, по-англ+ийски. '
               'Не думаю, что нас начнут расстреливать сразу после отстыковки.',
               en='We get in our ships and leave without a word, the English way. I don\'t think they\'ll start shooting us right after we undock.'
        ),
        VoiceLine(
            90,
            Trent,
            ru='А там - рванем в приграничье, будем выполнять обычные заказы за толику малую. А то меня от этой политики уже тошнит. '
               'Я уже запутался кто против кого, и за кого сейчас я!',
               en='And from there we\'ll run for the borderlands, take ordinary jobs for a pittance. Because this politics already makes me sick. I\'ve lost track of who\'s against whom, and who I\'m for right now!'
        ),
        VoiceLine(
            100,
            Alaric,
            ru='Да поздно уже когти рвать-то. Улетишь ты в приграничье, '
               'а за тобой через недельку какой-нибудь Хасслер вылетит, и вежливо так прикончит. ',
               en='It\'s too late to cut and run. You\'ll fly off to the borderlands, and a week later some Hassler will fly out after you and ever so politely finish you off.'
        ),
        VoiceLine(
            105,
            Alaric,
            ru='Слишком уж мы с тобой в этом увязли, дружище, слишком много знаем.',
               en='We\'re in way too deep in this, buddy. We know too much.'
        ),
        VoiceLine(
            110,
            Trent,
            ru='Да... И главная причина - ужасно досмотреть хочется, чем всё закончится.',
               en='Yeah... And the main reason is, I really want to see how it all ends.'
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
               en='Come on, don\'t look at me like that. I\'m not running off anywhere. Without me you\'ll just land in something again...'
        ),
        VoiceLine(
            140,
            Trent,
            ru='Досмотрим этот боевичёк до конца. (в сторону) Пока еще не ясно, до чьег+о конца!',
               en='We\'ll watch this little action movie through to the end. (aside) Not clear yet whose end!'
        ),
        VoiceLine(
            200,
            EdisonTrent,
            comment='После ухода главного героя из бара',
            ru='А этот парень хор+ош, способный товарищ. Как думаешь?',
               en='And this guy is good. A capable fellow. What do you think?'
        ),
        VoiceLine(
            210,
            Juni,
            ru='Такой же безрассудный,, как и ты. Помогает местным фанатикам, а лучше бы их остановил.',
               en='Just as reckless as you. Helping the local fanatics, when he\'d be better off stopping them.'
        ),
        VoiceLine(
            220,
            EdisonTrent,
            ru='А кто их остановит? Ты думаешь я смогу уломать Ямамото? Он же упёртый похлеще Ор+илиона с Кингом вместе взятыми.',
               en='And who\'s going to stop them? You think I can talk Yamamoto around? He\'s more stubborn than Orillion and King put together.'
        ),
        VoiceLine(
            230,
            Juni,
            ru='Упёртый,, алчный и коварный. И Ор+илиона больше нет,, чтобы его остановить.',
               en='Stubborn, greedy, and cunning. And Orillion is no longer around to stop him.'
        ),
        VoiceLine(
            240,
            EdisonTrent,
            ru='Да. Вот я и боюсь делать по твоему плану А. Но у меня есть свой план Бэ... ',
               en='Yes. That\'s why I\'m afraid to follow your plan A. But I have my own plan B...'
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
    SYNC_SUBS = True

    MISSION_TITLE = 'Миссия 10. Вызволение заключенных'