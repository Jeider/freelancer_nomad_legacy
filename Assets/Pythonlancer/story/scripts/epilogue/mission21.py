
from story import script
from audio.sound import VoiceLine
from story.actors import Trent, EdisonTrentHolo, Mandrake, Juni, Washington
from story.cutscenes.epilogue_scenes import m24


class MsnUlster(object):
    MISSION_INDEX = 21


class RewardScene(MsnUlster, script.CutsceneProps):
    ALIAS = 'reward'
    TITLE = 'Планета Калифорния'
    THORN_CLASS = m24.RewardScene
    DESCRIPTION = ''
    VOICE_LINES = [

    ]

class UlsterSpace(MsnUlster, script.SpaceVoiceProps):
    VOICE_LINES = [
        # VoiceLine(5, Hatcher, ru='Направляемся в Сферу. Трент, веди нас', en='Setting course for the Sphere. Trent, lead the way!'),
    ]


class Mission21(MsnUlster, script.StoryMission):
    CUTSCENES = [
        RewardScene,
    ]
    SPACE_CLASS = UlsterSpace
    SYNC_SPACE = True

    MISSION_TITLE = 'Эпилог. Путь в Ольстер'
