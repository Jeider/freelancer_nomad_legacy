from story import script
from audio.sound import VoiceLine
from story.actors import Trent, EdisonTrentHolo, Mandrake, Juni, Washington
from story.cutscenes.epilogue_scenes import m24


class MsnManheimConvoy(object):
    MISSION_INDEX = 27


class RewardScene(MsnManheimConvoy, script.CutsceneProps):
    ALIAS = 'reward'
    TITLE = 'Планета Калифорния'
    THORN_CLASS = m24.RewardScene
    DESCRIPTION = ''
    VOICE_LINES = [

    ]

class ManheimConvoySpace(MsnManheimConvoy, script.SpaceVoiceProps):
    VOICE_LINES = [
        # VoiceLine(5, Hatcher, ru='Направляемся в Сферу. Трент, веди нас', en='Setting course for the Sphere. Trent, lead the way!'),
    ]


class Mission27(MsnManheimConvoy, script.StoryMission):
    CUTSCENES = [
        RewardScene,
    ]
    SPACE_CLASS = ManheimConvoySpace
    SYNC_SPACE = True

    MISSION_TITLE = 'Эпилог. Конвой к Манхейму'
