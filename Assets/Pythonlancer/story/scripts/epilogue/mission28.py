from story import script
from audio.sound import VoiceLine
from story.actors import Trent, EdisonTrentHolo, Mandrake, Juni, Washington
from story.cutscenes.epilogue_scenes import m24


class MsnBabylon(object):
    MISSION_INDEX = 28


class RewardScene(MsnBabylon, script.CutsceneProps):
    ALIAS = 'reward'
    TITLE = 'Планета Калифорния'
    THORN_CLASS = m24.RewardScene
    DESCRIPTION = ''
    VOICE_LINES = [

    ]

class BabylonSpace(MsnBabylon, script.SpaceVoiceProps):
    VOICE_LINES = [
        # VoiceLine(5, Hatcher, ru='Направляемся в Сферу. Трент, веди нас', en='Setting course for the Sphere. Trent, lead the way!'),
    ]


class Mission28(MsnBabylon, script.StoryMission):
    CUTSCENES = [
        RewardScene,
    ]
    SPACE_CLASS = BabylonSpace
    SYNC_SPACE = True

    MISSION_TITLE = 'Эпилог. Внутри Вавилона'
