from story import script
from audio.sound import VoiceLine
from story.actors import Trent, EdisonTrentHolo, Mandrake, Juni, Washington
from story.cutscenes.epilogue_scenes import m24


class MsnDixie(object):
    MISSION_INDEX = 22


class RewardScene(MsnDixie, script.CutsceneProps):
    ALIAS = 'reward'
    TITLE = 'Планета Калифорния'
    THORN_CLASS = m24.RewardScene
    DESCRIPTION = ''
    VOICE_LINES = [

    ]

class DixieSpace(MsnDixie, script.SpaceVoiceProps):
    VOICE_LINES = [
        # VoiceLine(5, Hatcher, ru='Направляемся в Сферу. Трент, веди нас', en='Setting course for the Sphere. Trent, lead the way!'),
    ]


class Mission22(MsnDixie, script.StoryMission):
    CUTSCENES = [
        RewardScene,
    ]
    SPACE_CLASS = DixieSpace
    SYNC_SPACE = True

    MISSION_TITLE = 'Эпилог. Союз с конфедератами'
