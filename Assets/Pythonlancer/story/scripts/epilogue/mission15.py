from story import script
from audio.sound import VoiceLine
from story.actors import Trent, Rockford, Darcy, EdisonTrent, King, Hatcher, Alaric, Mandrake, Missouri, Neuralnet
from story.cutscenes.story_scenes import m13_osiris, m13_enter_bh, m13_death, m13_csv


class MsnOdja(object):
    MISSION_INDEX = 20


class OdjaIntroCutscene(MsnOdja, script.CutsceneProps):
    ALIAS = 'intro'
    TITLE = 'База Кадиз'
    THORN_CLASS = m13_osiris.Msn13OsirisScene
    DESCRIPTION = ''
    VOICE_LINES = [
        # VoiceLine(10, Darcy, ru="Трент,, давай скорее! Брифинг уже началс+я!", en="Trent, hurry up! The briefing has already started!"),

    ]
    PROTOS = [
        'Мистер Трент?',
        'Это вас зовут Кендзи? Я думал что... ну вы наследник престола. Должны быть постарше.',
        'Да, я наследник рода Одзя. И последний его представитель. Люди Ордена постарались уничтожить нашу династию, убили моего отца и старшего брата.',
        'Так что я и мои люди полны решимости отомстить и устроить реванш. Или вы уже в нас сомневаетесь?',
        'Я? Нет. Это задание Джунко Зэйн. Если она вам доверяет, то значит будут и я.'
    ]





class OdjaSpace(MsnOdja, script.SpaceVoiceProps):
    VOICE_LINES = [
        # VoiceLine(5, Hatcher, ru='Направляемся в Сферу. Трент, веди нас', en='Setting course for the Sphere. Trent, lead the way!'),


    ]


class MissionOdja(MsnOdja, script.StoryMission):
    CUTSCENES = [

    ]
    SPACE_CLASS = OdjaSpace
    SYNC_SPACE = True

    MISSION_TITLE = 'Эпилог. Миссия клана Одзя'
