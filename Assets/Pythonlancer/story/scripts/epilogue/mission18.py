from story import script
from audio.sound import VoiceLine
from story.actors import Trent, JackRazorBarber, Darcy
from story.cutscenes.epilogue_scenes import m18


class MsnJackCrew(object):
    MISSION_INDEX = 18


class ReunionScene(MsnJackCrew, script.CutsceneProps):
    ALIAS = 'reunion'
    TITLE = 'База Ксеносов'
    THORN_CLASS = m18.ReunionScene
    DESCRIPTION = ''
    VOICE_LINES = [
        # Воссоединение с Дерси
        VoiceLine(10, Darcy, ru="Трент,, вот ты даёшь. Ты за эти 10 лет никак не изменился. Как будто это было вчера."),
        VoiceLine(20, Trent, ru="Ты тоже отлично выглядишь,, Дерси. Рад снова тебя видеть."),
        VoiceLine(30, Darcy, ru="Слушай,, а чем фрилансеры занимаются в свободное время? Так же воюют и зарабатывают деньги?"),
        VoiceLine(40, Trent, ru="Если бы так, теперь любое мое действие приправлено необходимостью спасать мир."),
        VoiceLine(50, Trent, ru="Я стал себя ощущать дружелюбным соседом фрилансером, которому всегда есть чем заняться для других, но не хватает времени на себя."),
        VoiceLine(60, Darcy, ru="Доведём дело до конца и глянем,, на что ты еще способен,, кроме работы,, фрилансер!"),
        VoiceLine(70, JackRazorBarber, ru="Эй,, голубк+и, наворковались?"),
        VoiceLine(80, Darcy, ru="Капитан Джек Брадобрей! Я даже не могла представить,, что буду работать с тобой!"),
        VoiceLine(90, JackRazorBarber, ru="Взаимно,, Дерси. Ты обещала,, что достанешь из тюрьмы мо+ю команду. Так что с ней?"),
        VoiceLine(100, Darcy, ru="Твоя команда находится в тюрьме Г+олспи. Их планируют перевезти в тюремный блок в системе Уорик."),
        VoiceLine(110, JackRazorBarber, ru="Разреши узнать,, какого ляда законникам нужно это делать?"),
        VoiceLine(120, Darcy, ru="Обычно это означает,, что в друг+ом тюремном блоке их тихо расстреляют. Но мы их успеем вызволить."),
        VoiceLine(130, Darcy, ru="Мы перехватим тюремный конвой во время транспортировки и достанем твою команду."),
        VoiceLine(140, JackRazorBarber, ru="Разрази меня гром! Их нужно спасти от виселицы! Когда отплываем?"),
        VoiceLine(150, Darcy, ru="Нужно выступать немедленно. Трент, готовь свой корабль. Джек снова полетит с тобой."),
        VoiceLine(160, Trent, ru="Понял,, принял."),
        VoiceLine(170, JackRazorBarber, ru="Давай,, матрос, готовь свой корабль быстрее,, пока мо+я команда не станцевала джигу на пеньковой верёвке!"),

    ]

class JackCrewSpace(MsnJackCrew, script.SpaceVoiceProps):
    VOICE_LINES = [
        # VoiceLine(5, Hatcher, ru='Направляемся в Сферу. Трент, веди нас', en='Setting course for the Sphere. Trent, lead the way!'),
    ]


class Mission18(MsnJackCrew, script.StoryMission):
    CUTSCENES = [
        ReunionScene,
    ]
    SPACE_CLASS = JackCrewSpace
    SYNC_SPACE = True

    MISSION_TITLE = 'Эпилог. Вызволение команды Джека'
