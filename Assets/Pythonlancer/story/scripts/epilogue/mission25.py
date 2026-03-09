from story import script
from audio.sound import VoiceLine
from story.actors import Trent, EdisonTrentHolo, Mandrake, Juni, Washington
from story.cutscenes.epilogue_scenes import m24


class MsnHeavyBarrel(object):
    MISSION_INDEX = 25


class RewardScene(MsnHeavyBarrel, script.CutsceneProps):
    ALIAS = 'reward'
    TITLE = 'Планета Калифорния'
    THORN_CLASS = m24.RewardScene
    DESCRIPTION = ''
    VOICE_LINES = [

    ]

class HeavyBarrelSpace(MsnHeavyBarrel, script.SpaceVoiceProps):
    VOICE_LINES = [
        # VoiceLine(5, Hatcher, ru='Направляемся в Сферу. Трент, веди нас', en='Setting course for the Sphere. Trent, lead the way!'),
    ]


class Mission25(MsnHeavyBarrel, script.StoryMission):
    CUTSCENES = [
        RewardScene,
    ]
    SPACE_CLASS = HeavyBarrelSpace
    SYNC_SPACE = True

    MISSION_TITLE = 'Эпилог. Сборка компонентов Мегапушки'
