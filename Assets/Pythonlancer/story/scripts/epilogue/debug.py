from story import script
from audio.sound import VoiceLine
from story.actors import Trent, JackRazorBarber
from story.cutscenes.epilogue_scenes import debug


class MsnDebug(object):
    MISSION_INDEX = 99


class DebugScene(MsnDebug, script.CutsceneProps):
    ALIAS = 'debug'
    TITLE = 'Дебажка'
    THORN_CLASS = debug.DebugScene
    DESCRIPTION = ''
    VOICE_LINES = [

    ]

class DebugSpace(MsnDebug, script.SpaceVoiceProps):
    VOICE_LINES = [
        # VoiceLine(5, Hatcher, ru='Направляемся в Сферу. Трент, веди нас', en='Setting course for the Sphere. Trent, lead the way!'),
    ]


class Mission17(MsnDebug, script.StoryMission):
    CUTSCENES = [
        DebugScene,
    ]
    SPACE_CLASS = DebugSpace
    SYNC_SPACE = True

    MISSION_TITLE = 'Эпилог. Тестовый'
