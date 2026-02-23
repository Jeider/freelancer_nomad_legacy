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
        VoiceLine(10, Trent, ru='Эй, друг. Ты не знаешь где тут объект LV-426?'),
        VoiceLine(20, TripoliBarman, ru='Чего? Четыреста сколько? Слушай, я в этом не секу,, братан.'),
        VoiceLine(30, TripoliBarman, ru='Хотя знаешь...  Есть тут одна шняга. Мы её называем Терновником.'),
        VoiceLine(40, Trent, ru='Это еще что такое?'),
        VoiceLine(50, TripoliBarman, ru='Минное загорождение, внутри которого Орден проводил какие-то исследования.'),
        VoiceLine(60, Trent, ru='Скорее всего это именно то,, что мне нужно. Покажешь,, где это?'),
        VoiceLine(70, TripoliBarman, ru='Ну координаты то я скину... А ты не боишься туда лететь? Это как бы режимный объект Ордена и всё такое.'),
        VoiceLine(80, Trent, ru='Ну и где сейчас этот твой Орден?'),
        VoiceLine(90, TripoliBarman, ru='А ты шаришь... Мы агентов Ордена уже давно не видели. Всякие слухи ходят.'),
        VoiceLine(100, Trent, ru='У вас не было никакого орденского коменданта?'),
        VoiceLine(110, TripoliBarman, ru='Был. Да и есть. Но он из Мадрида редко вылезает. В нашей системе только его прихвостни ошивались. До какого-то времени.'),
        VoiceLine(120, Trent, ru='Ладно, вроде всё понятно. Спасибо за наводку на этот ваш Терновник!'),
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
