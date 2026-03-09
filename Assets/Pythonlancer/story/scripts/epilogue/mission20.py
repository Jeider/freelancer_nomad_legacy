from story import script
from audio.sound import VoiceLine
from story.actors import Trent, JackRazorBarber, Darcy
from story.cutscenes.epilogue_scenes import m20


class MsnJabba(object):
    MISSION_INDEX = 20


class CollectionScene(MsnJabba, script.CutsceneProps):
    ALIAS = 'collection'
    TITLE = 'Станция Антилия'
    THORN_CLASS = m20.CollectionScene
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, JackRazorBarber, ru="Слушай, Трент, а может возьмем на борт эту барышню? Я бы с ней спас мир и не раз..."),
        VoiceLine(20, Trent, ru="Попридержи коней,, пират. Нам нужна не она. Ищем дальше."),
        VoiceLine(30, Darcy, ru="Трент, кажется,, это оно."),
        VoiceLine(40, JackRazorBarber, ru="Что, серьёзно? Вот этот капуцин?"),
        VoiceLine(50, Darcy, ru="Капитан, вообще-то это павиан."),
        VoiceLine(60, Trent, ru="Сигнал маяка ведёт точно к нему... Значит забираем."),
        VoiceLine(70, Darcy, ru="А что делать с остальными экспонатами? Пираты раздербанят эту коллекцию д+очиста."),
        VoiceLine(80, Trent, ru="Да, все эти вещи слишком ценные. Нужно их сохранить. Каков наш дальнейший путь?"),
        VoiceLine(90, JackRazorBarber, ru="У нас есть тихая гавань в +Ольстере. Предлагаю пришфартоваться там. Место безопасное."),
        VoiceLine(100, Trent, ru="Окей, тогда давайте паковаться. Берём всё органическое или артефактное. Железяки и прочую мелочь оставляем."),
        VoiceLine(110, JackRazorBarber, ru="Чур та барышня плывёт в моей каюте!"),
        VoiceLine(120, Darcy, ru="Трент, есть еще одно дело. Профессор Мандрейк сообщил, что ему нужна помощь одного учёного из Кембриджа, моего друга."),
        VoiceLine(130, Darcy, ru="Ты можешь подхватить его и доставить в +Ольстер,, пока мы тут собираемся?"),
        VoiceLine(140, Trent, ru="Да,, могу. Тогда полечу за ним. А вы пакуйтесь и догоняйте."),
    ]

class JabbaSpace(MsnJabba, script.SpaceVoiceProps):
    VOICE_LINES = [
        # VoiceLine(5, Hatcher, ru='Направляемся в Сферу. Трент, веди нас', en='Setting course for the Sphere. Trent, lead the way!'),
    ]


class Mission20(MsnJabba, script.StoryMission):
    CUTSCENES = [
        CollectionScene,
    ]
    SPACE_CLASS = JabbaSpace
    SYNC_SPACE = True

    MISSION_TITLE = 'Эпилог. Битва с Джаббой'
