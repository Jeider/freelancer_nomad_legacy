from story import script
from audio.sound import VoiceLine
from story.actors import Trent, EdisonTrentHolo, Mandrake, Juni, MonkeyKing
from story.cutscenes.epilogue_scenes import m23


class MsnBackToSphere(object):
    MISSION_INDEX = 23


class PygarScene(MsnBackToSphere, script.CutsceneProps):
    ALIAS = 'pygar'
    TITLE = 'Планета Пигар'
    THORN_CLASS = m23.PygarScene
    DESCRIPTION = ''
    VOICE_LINES = [

        VoiceLine(10, Mandrake, ru="Устройство подключено... ищу частоту... Нашел! Сигнал идёт!"),
        VoiceLine(20, Mandrake, ru="Сигнал идёт с добывающей станции Тай Тэгра."),
        VoiceLine(30, Mandrake, ru="Получаю изображение."),

        VoiceLine(40, EdisonTrentHolo, ru="Приём, приём, как слышно?"),
        VoiceLine(50, Mandrake, ru="Генерал Трент, мы вас слышим!"),

        VoiceLine(60, EdisonTrentHolo, ru="Отлично. Буду краток. Ситуация тяжелая. Нужно принимать крайние меры."),
        VoiceLine(70, EdisonTrentHolo, ru="Рокфорд заблокировал Сферу Д+айсона. Кинг и Хэтчер со мной. Мы окружены силами кочевников."),

        VoiceLine(80, Mandrake, ru="Сколько вы сможете продержаться?"),

        VoiceLine(90, EdisonTrentHolo, ru="Мы справимся. Рокфорд запускает телепорт. Тагава был прав. Разрешаю использовать план ХБ-ЧП-Три."),
        VoiceLine(100, EdisonTrentHolo, ru="Начинайте прямо сейчас, времени..."),

        VoiceLine(110, Trent, ru="Что случилось?"),
        VoiceLine(120, Mandrake, ru="Мы потеряли сигнал. Полностью."),
        VoiceLine(130, Trent, ru="Так почин+ите."),
        VoiceLine(140, Mandrake, ru="Это невозможно. Видимо, передатчик сломан на нашей или на той стороне."),

        VoiceLine(150, MonkeyKing, ru="Это не важно, мы узнали всё,, что хотели."),
        VoiceLine(160, Trent, ru="Что за ХБ-ЧП-Три?"),
        VoiceLine(170, MonkeyKing, ru="Мегапушка. Генерал Трент хочет,, чтобы мы её собрали."),

        VoiceLine(180, Trent, ru="Зачем?"),
        VoiceLine(190, MonkeyKing, ru="Рокфорд реактивирует систему телепортов. Если это действительно так, то у нас будет много гостей."),
        VoiceLine(200, Trent, ru="Например?"),
        VoiceLine(210, MonkeyKing, ru="Главным кочевником всегда был господин Санкрашер. Штука, которая уничтожила Солнечную систему."),
        VoiceLine(220, MonkeyKing, ru="Я смог отключить эту часть телепорта, чтобы дать человечеству время. Рокфорд сломает эту блокировку, чтобы достичь своих целей."),

        VoiceLine(230, Trent, ru="Хорошо, мегапушка. Как её сделать?"),

        VoiceLine(240, Mandrake, ru="Внимание! Пришл+о сообщение из Л+иберти."),
        VoiceLine(250, Mandrake, ru="Мисс Зейн, что случилось?"),
        VoiceLine(260, Juni, ru="Силы Конфедерации вступили в бой с правительственными войсками."),
        VoiceLine(270, Trent, ru="Вашу мать, что, опять? Я чувствую себя Рокфордом. Эти людишки могут хотя бы на минуту перестать желать перестрелять друг друга?"),

        VoiceLine(280, Mandrake, ru="Выдвигайтесь. Я пока перенесу лабораторию на Навохудон+осор. На Пиг+аре теперь слишком опасно."),
    ]

class BackToSphereSpace(MsnBackToSphere, script.SpaceVoiceProps):
    VOICE_LINES = [
        # VoiceLine(5, Hatcher, ru='Направляемся в Сферу. Трент, веди нас', en='Setting course for the Sphere. Trent, lead the way!'),
    ]


class Mission23(MsnBackToSphere, script.StoryMission):
    CUTSCENES = [
        PygarScene,
    ]
    SPACE_CLASS = BackToSphereSpace
    SYNC_SPACE = True

    MISSION_TITLE = 'Эпилог. Возвращение в Сферу'
