from story import script
from audio.sound import VoiceLine
from story.actors import Trent, TripoliBarman
from story.cutscenes.epilogue_scenes import m16


class MsnFish(object):
    MISSION_INDEX = 16


class TripoliScene(MsnFish, script.CutsceneProps):
    ALIAS = 'tripoli'
    TITLE = 'Верфь Триполи'
    THORN_CLASS = m16.TripoliScene
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Trent, ru='Эй, друг. Ты не знаешь где тут объект LV-426?', en="Hey, buddy. You know where I can find object LV-426 around here?"),
        VoiceLine(20, TripoliBarman, ru='Чего? Четыреста сколько? Слушай, я в этом не секу,, братан.', en="Huh? Four hundred what? Listen, man, I don't know jack about that, bro."),
        VoiceLine(30, TripoliBarman, ru='Хотя знаешь...  Есть тут одна шняга. Мы её называем Терновником.', en="Although... wait. There is this one thing. We call it The Crown of Thorns."),
        VoiceLine(40, Trent, ru='Это еще что такое?', en="What's that?"),
        VoiceLine(50, TripoliBarman, ru='Минное загорождение, внутри которого Орден проводил какие-то исследования.', en="It's a minefield. The Order was running some kinda research ops inside it."),
        VoiceLine(60, Trent, ru='Скорее всего это именно то,, что мне нужно. Покажешь,, где это?', en="Sounds like exactly what I'm looking for. Can you point me there?"),
        VoiceLine(70, TripoliBarman, ru='Ну координаты то я скину... А ты не боишься туда лететь? Это как бы режимный объект Ордена и всё такое.', en="Yeah, I can drop you the coordinates... But ain't you scared to fly in there? That's like, classified Order territory and all that."),
        VoiceLine(80, Trent, ru='Ну и где сейчас этот твой Орден?', en="And where's your precious Order now?"),
        VoiceLine(90, TripoliBarman, ru='А ты шаришь... Мы агентов Ордена уже давно не видели. Всякие слухи ходят.', en="Heh, you got a point... Ain't seen no Order agents around here in ages. Lots of rumors floating around."),
        VoiceLine(100, Trent, ru='У вас не было никакого орденского коменданта?', en="Didn't you have some Order commander stationed here?"),
        VoiceLine(110, TripoliBarman, ru='Был. Да и есть. Но он из Мадрида редко вылезает. В нашей системе только его прихвостни ошивались. До какого-то времени.', en="Yeah, we did. Still do, technically. But the guy barely ever leaves Madrid. Only his flunkies used to hang around our system. Until they didn't."),
        VoiceLine(120, Trent, ru='Ладно, вроде всё понятно. Спасибо за наводку на этот ваш Терновник!', en="Alright, got the picture. Thanks for the tip about this Crown of Thorns of yours!"),
    ]


class FishSpace(MsnFish, script.SpaceVoiceProps):
    VOICE_LINES = [
        # VoiceLine(5, Hatcher, ru='Направляемся в Сферу. Трент, веди нас', en='Setting course for the Sphere. Trent, lead the way!'),

    ]


class Mission16(MsnFish, script.StoryMission):
    CUTSCENES = [
        TripoliScene,
    ]
    SPACE_CLASS = FishSpace
    SYNC_SPACE = True

    MISSION_TITLE = 'Эпилог. Миссия в Терновнике'
