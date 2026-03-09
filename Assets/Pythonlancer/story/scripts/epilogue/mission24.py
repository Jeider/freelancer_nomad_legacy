from story import script
from audio.sound import VoiceLine
from story.actors import Trent, EdisonTrentHolo, Mandrake, Juni, Washington
from story.cutscenes.epilogue_scenes import m24


class MsnCivilWar(object):
    MISSION_INDEX = 24


class RewardScene(MsnCivilWar, script.CutsceneProps):
    ALIAS = 'reward'
    TITLE = 'Планета Калифорния'
    THORN_CLASS = m24.RewardScene
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Washington, ru="Я хочу выразить благодарность за вашу работу,, м+истер Трент."),
        VoiceLine(20, Trent, ru="Всегда к вашим услугам,, м+истер президент."),
        VoiceLine(30, Washington, ru="Надеюсь эта история станет для вас важным уроком. Вы отлично справляетесь с ролью ренегата,, сражающегося с Орденом."),
        VoiceLine(40, Washington, ru="Но нашему миру нужен не только хаос,, но и настоящий порядок."),
        VoiceLine(50, Trent, ru="Я понял,, к чему вы клоните. Бандиты пор+ой хорошие временные союзники, но иногда они действительно бандиты."),
        VoiceLine(60, Trent, ru='Да,, кстати, м+истер президент, я ведь планировал использовать силы этих бандитов в составе флота "Комитета по спасению человечества".'),
        VoiceLine(70, Trent, ru="Мне эти силы пришлось уничтожить и теперь в составе моего флота для спасения мира поубавилось."),
        VoiceLine(80, Washington, ru="Не беспокойтесь об этом,, м+истер Трент. Правительство Л+иберти выделит вам один из линкоров в знак благодарности за ваши услуги."),
        VoiceLine(90, Washington, ru="Вы принесли мир, свободу, справедливость и безопасность нашей Республике."),
        VoiceLine(100, Washington, ru="И я надеюсь,, что вы сможете это сделать и для всего сектора Сириуса. Удачи вам,, м+истер Трент."),
    ]

class CivilWarSpace(MsnCivilWar, script.SpaceVoiceProps):
    VOICE_LINES = [
        # VoiceLine(5, Hatcher, ru='Направляемся в Сферу. Трент, веди нас', en='Setting course for the Sphere. Trent, lead the way!'),
    ]


class Mission17(MsnCivilWar, script.StoryMission):
    CUTSCENES = [
        RewardScene,
    ]
    SPACE_CLASS = CivilWarSpace
    SYNC_SPACE = True

    MISSION_TITLE = 'Эпилог. Гражданская война в Либерти'
