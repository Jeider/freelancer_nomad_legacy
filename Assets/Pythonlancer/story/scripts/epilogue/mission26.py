from story import script
from audio.sound import VoiceLine
from story.actors import Trent, EdisonTrentHolo, Mandrake, Juni, Washington, Gruenwald
from story.cutscenes.epilogue_scenes import m26


class MsnGruenwald(object):
    MISSION_INDEX = 26


class BerlinScene(MsnGruenwald, script.CutsceneProps):
    ALIAS = 'berlin'
    TITLE = 'Планета Берлин'
    THORN_CLASS = m26.BerlinScene
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Gruenwald, ru="Приветствую вас, герр Трент."),
        VoiceLine(20, Trent, ru="Леди Грюнвальд? У вас ко мне какое-то дело?"),
        VoiceLine(30, Gruenwald, ru="Герр Трент, я знаю,, что ваши отношения с Рейнландом... не совсем заладились."),
        VoiceLine(40, Trent, ru="Конечно не заладились, меня ваши официальные власти несколько раз хотели убить!"),
        VoiceLine(50, Gruenwald, ru="Да, это так. Наша политика весьма экспансивна. И пор+ой наше правительство принимает ужасные решения."),
        VoiceLine(60, Gruenwald, ru="Но если дело касается спасения мира, то мы готовы предложить вам не только мир, но и даже вступить в союз."),
        VoiceLine(70, Trent, ru="Так а какая мне польза от такого союза?"),
        VoiceLine(80, Gruenwald, ru="Например,, мы в курсе, что вы хотите силой захватить систему Штутгарт, чтобы получить доступ к нашим производственным мощностям."),
        VoiceLine(90, Gruenwald, ru="Мы готовы предоставить вам эти мощности без боя. Если вы выполните одну нашу просьбу."),
        VoiceLine(100, Trent, ru="Это очень весомое предложение,, леди Грюнвальд. В чём состоит ваша просьба?"),
        VoiceLine(110, Gruenwald, ru="Мы хотим,, чтобы вы обеспечили нашу безопасность."),
        VoiceLine(120, Trent, ru="Безопасность? Каким образом?"),
        VoiceLine(130, Gruenwald, ru="Герр Трент... вы уверены в лояльности герра Хасслера?"),
        VoiceLine(140, Trent, ru="Честно говоря, я сам хотел его пару раз придушить. Не предлагаете ли вы мне убить его?"),
        VoiceLine(150, Gruenwald, ru="Нет,, что вы. Нас волнует не герр Хасслер, а союзы, которые он заключил."),
        VoiceLine(160, Gruenwald, ru="Выбор его союзников... весьма противоречив. Мы имеем веские обоснования того, что он планирует захватить и расколоть Рейнланд."),
        VoiceLine(170, Trent, ru="Звучит не слишком убедительно, фрау Грюнвальд. У вас есть какие-то доказательства?"),
        VoiceLine(180, Gruenwald, ru="Конечно,, герр Трент. Наши разведчики регулярно докладывают о концентрации значительных сил мусорщиков и гессенцев в системе Малый Омикрон."),
        VoiceLine(190, Gruenwald, ru="Они готовы выступить в бой в тот момент, как только вам удасться разобраться с инопланетной угрозой."),
        VoiceLine(200, Gruenwald, ru="Флот Рейнланда ослаблен, наши заводы захвачены кочевниками. Мы не уверены, что сможем справиться с очередным вторжением."),
        VoiceLine(210, Trent, ru="Я и не знаю,, что сказать, леди Грюнвальд. Мне нужно самому удостовериться,, говорите ли вы правду."),
        VoiceLine(220, Trent, ru="Но если это действительно так, то я постараюсь решить вашу проблему."),
        VoiceLine(230, Gruenwald, ru="Наша надежда только на вас, герр Трент."),
    ]

class GruenwaldSpace(MsnGruenwald, script.SpaceVoiceProps):
    VOICE_LINES = [
        # VoiceLine(5, Hatcher, ru='Направляемся в Сферу. Трент, веди нас', en='Setting course for the Sphere. Trent, lead the way!'),
    ]


class Mission17(MsnGruenwald, script.StoryMission):
    CUTSCENES = [
        BerlinScene,
    ]
    SPACE_CLASS = GruenwaldSpace
    SYNC_SPACE = True

    MISSION_TITLE = 'Эпилог. Миссия от Грюнвальд. Мирное получение Манхейма'
