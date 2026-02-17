from story import script
from audio.sound import VoiceLine
from story.actors import Trent, EdisonTrent, LogosRobot, Juni
from story.cutscenes.epilogue_scenes import m14


class Msn14(object):
    MISSION_INDEX = 14


class TrentRescuedCutscene(Msn14, script.CutsceneProps):
    ALIAS = 'intro'
    TITLE = 'Линкор Логос'
    THORN_CLASS = m14.Msn14TrentRescuedScene
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Trent, ru='Что за дел+а...', en='What a hell is it...'),
        VoiceLine(20, EdisonTrent, ru='Проснулся,, чемпион? Твое долгое путешествие подошло к концу!', en='You\'re finally awake, champ. Congrats! Your long journey is over!'),
        VoiceLine(30, Trent, ru='Долгое... что происходит, где я? Где Крыг?', en='Long... what\'s going on? Where am I? Where\'s the Krieg?'),
        VoiceLine(40, EdisonTrent, ru='Я посмотрел записи твоей нейросети. Крыга ты уничтожил. Молодчина,, тёзка. А время... я наблюдаю за местом твоего прибытия последние 10 лет',
					  en='I reviewed your neural net logs. You destroyed the Krieg. Well done, namesake. As for time... I\'ve been monitoring your emergence point for the last 10 years.'),
        VoiceLine(50, Trent, ru='10 лет? Что? Как?', en='10 years? What? How?'),
        VoiceLine(60, EdisonTrent, ru='Ну ты же не думал,, что в чёрную дыру можно так просто в взять и залететь? Время в ней шло для тебя быстрее,, чем для обычного мира. Я вообще удивлён,, что ты выжил, но я всё равно в тебя верил.',
					  en='You didn\t think you could just fly in a black hole without consequences for yourself, did you? Time moved faster for you in there than for the rest of us. Honestly, I\'m amazed you survived at all. But I never doubted you.'),
        VoiceLine(70, EdisonTrent, ru='Ах да. Знакомься с моими друзьями. Это роботы с планеты Гамму. И ты находишься на борт+у моего личного линкора Логос.',
					  en='Oh, right. Meet my new friends. They\'re robots from the planet Gammu. And you\'re aboard my personal battleship - the Logos.'),
        VoiceLine(80, Trent, ru='Логос?! Я же его разнёс!', en='The Logos?! But I destroyed that ship!'),
        VoiceLine(90, EdisonTrent, ru='Да,, ты хорошо постарался. Мы с Кингом всё думали,, что теперь делать с линкором. Даже перевозка его на слом это была бы целая история.',
					  en='Yes, you did a thorough job. King and I spent ages debating what to do with the wreck. Even hauling it for scrap would\'ve been an epic undertaking.'),
        VoiceLine(100, EdisonTrent, ru='Вот мы с Кингом и сошлись на том,, что Логоса я восстановлю и оставлю себе в счёт старой дружбы. Роботы с Гамму помогли мне с ремонтом, линкор теперь как новенький. Только щитовая установка сбоит, но мы её чиним.',
					  en='So King and I agreed — I\'d rebuild the Logos and keep it as a token of old friendship. The robots from Gammu helped with the repairs - the ship is as good as new now. The shield generator glitches occasionally, but we\'re working on it.'),
        VoiceLine(110, Trent, ru='Кинг... Логос... Рокфорд! А что с Рокфордом?', en='King... the Logos... Rockford! What about Rockford?'),
        VoiceLine(120, EdisonTrent, ru='Рокфорд... Я понимаю,, что пришло время для ответов. Давай начнем с моих друзей.', en='Rockford... I know you deserve answers. Let\'s start with my friends here.'),
        VoiceLine(125, EdisonTrent, ru='Ты же помнишь про Альянс, который воевал с Коалицией. Альянс когда-то разослал огромное количество исследовательских кораблей. Чтобы найти новый дом. Так Альянс,, кстати,, и нашел сектор Сириуса и все планеты,, доступные для заселения.',
					   en='Do you remember the Alliance that fought the Coalition? They once sent out countless exploration ships searching for a new home world. That\'s how they eventually found the Sirius Sector and all its habitable planets.'),
        VoiceLine(130, EdisonTrent, ru='И вот когда-то я нашел такой старый аванпост, управляемыми роботами на планете Гамму. Роботы сообщили мне, что нашли странный корабль во льдах.',
					   en='Well, I once discovered an old outpost on Gammu, run entirely by robots. They told me they\'d found a strange ship trapped in the ice.'),
        VoiceLine(140, EdisonTrent, ru='Я добрался до него и нашел там старый корабль Альянса. Это был корабль Рокфорда. Он отправился к нам с планеты Плутон ровно после того момента, как кочевники уничтожили Солнечную систему.',
					   en='I reached it and found an old Alliance vessel. It was Rockford\'s ship. He\'d left the planet Pluto right after the Nomads destroyed the Solar System.'),
        VoiceLine(150, Trent, ru='Подожди. Ты хочешь сказать, что этот Рокфорд живёт больше восьмиста лет?', en='Wait a second. Are you telling me this Rockford is over eight hundred years old?'),
        VoiceLine(160, EdisonTrent, ru='Да... его корабль должен был прилететь в сектор Сириуса. Но он сбился с курса. Автоматика отправила его к маяку аванпоста планеты Гамму. Корабль совершил неудачную посадку, но никто не пришел к нему на помощь.',
					   en='Yes... His ship was supposed to reach the Sirius Sector. But it was thrown off course. The autopilot locked onto the outpost\'s beacon on Gammu. The landing was catastrophic, and no one came to help.'),
        VoiceLine(170, EdisonTrent, ru='А персонал аванпоста решил законсервировать корабль, так как не имел средств поддержания человеческой жизни. Это же роботы! Им кислород и медпрепараты не нужн+ы!', en='The outpost crew were robots. They had no life support, no medical supplies! They just... preserved the ship.'),
        VoiceLine(180, EdisonTrent, ru='Когда я прибыл на Гамму, роботы отправили меня к кораблю. Вот тогда я и нашел Рокфорда и пробудил его.',
									en='When I arrived on Gammu, the robots sent me to investigate the ship. That\'s when I found Rockford and woke him up.'),
        VoiceLine(190, Trent, ru='Значит это ты открыл этот "ящик Панд+оры"', en='So you\'re the one who opened this Pandora\'s Box.'),
        VoiceLine(200, EdisonTrent, ru='Да,, действительно. Я не знал,, что всё пойдёт вот так.', en='Yes, I suppose I am. But I never imagined it would lead to all this...'),

        VoiceLine(210, LogosRobot, ru='Командир.', en='Commander!'),
        VoiceLine(220, EdisonTrent, ru='Ах,, да. Слушай,, тёзка. Я уже думал покинуть это место. Хорошо,, что я успел тебя поймать. У нас появились новые проблемы и нам надо спеш+ить.',
					   en='Ah, listen, namesake. I was actually about to leave this system. Lucky I caught you. We have new problems, and we need to move fast.'),
        VoiceLine(230, Trent, ru='Что на этот раз? Разве мы не победили?', en='What now? Didn\'t we already win?'),
        VoiceLine(240, EdisonTrent, ru='Победили, но не совсем. Недавно  произошел инцидент. И мы потеряли связь как с Энтерпрайзом, так и с базами у Сферы Д+айсона.',
					   en='We won a battle, but not the war. There was an incident recently. We\'ve lost contact with both the Enterprise and the bases near the Dyson Sphere.'),
        VoiceLine(250, EdisonTrent, ru='Мне срочно пор+а лететь. А здесь мне нужны глаз+а и ушии Ордена', en='I have to leave immediately. And I need someone here — eyes and ears for the...'),
        VoiceLine(260, Trent, ru='Ордена?', en='The Order?'),
        VoiceLine(270, EdisonTrent, ru='Нет, давай это назовём "Комитетом по спасению человечества"!', en='Let\'s call it the "Committee for the Salvation of Humanity" for now!'),
        VoiceLine(275, EdisonTrent, ru='Рядом в этой системе мы обнаружили номадское вторжение. Активировалось логово Номадов.', en='We\'ve detected a Nomad incursion in this system. The Nomad Lair has reactivated.'),
        VoiceLine(280, Trent, ru='Как? Все генераторы же были демонтированы.', en='How?! All the generators were dismantled!'),
        VoiceLine(290, EdisonTrent, ru='Да, в этом и проблема. Ты справишься с этим?', en='That\'s exactly the problem... Can you handle this?'),
        VoiceLine(300, Trent, ru='Да без проблем.', en='Without a doubt.'),
        VoiceLine(310, EdisonTrent, ru='Тогда готовь свой корабль. Арсенал Логоса в твоем полном распоряжении. Остальное я тебе расскажу в космосе.',
					   en='Then prepare your ship. The Logos\'s arsenal is at your disposal. I\'ll brief you on the rest in space.'),
    ]


class Msn14Space(Msn14, script.SpaceVoiceProps):
    VOICE_LINES = [
        # VoiceLine(5, Hatcher, ru='Направляемся в Сферу. Трент, веди нас', en='Setting course for the Sphere. Trent, lead the way!'),
    ]


class Mission14(Msn14, script.StoryMission):
    CUTSCENES = [
        TrentRescuedCutscene,
    ]
    SPACE_CLASS = Msn14Space
    SYNC_SPACE = True

    MISSION_TITLE = 'Эпилог. Миссия 14'
