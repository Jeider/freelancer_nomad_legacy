from story import script
from audio.sound import VoiceLine
from story.actors import Trent, JackRazorBarber
from story.cutscenes.epilogue_scenes import m17


class MsnRobigo(object):
    MISSION_INDEX = 17


class JackMeetScene(MsnRobigo, script.CutsceneProps):
    ALIAS = 'intro'
    TITLE = 'База Робиго'
    THORN_CLASS = m17.JackMeetScene
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, Trent, ru='Эй, с протезом. Это ты Джек Брадобрей?'),
        VoiceLine(20, JackRazorBarber, ru='Прикус+и яз+ык, висельный прихвостень! Перед тобой сам капитан Джек Брадобр+ей! '),
        VoiceLine(30, JackRazorBarber, ru='Если пришёл содрать мо+ю шкуру ради горсти золот+ых, то сначала склони голову и прояви почтение, пока я не приколол твой язык к мачте на потеху чайкам!'),
        VoiceLine(40, Trent, ru='Эй, дядя, следи за базаром! Я не охотник за головами, я Трент и я работаю на "Комитет по спасению человечества".'),
        VoiceLine(50, Trent, ru='И мне нужен ты, чтобы спасти это грёбаное человечество от новой угрозы!'),
        VoiceLine(60, JackRazorBarber, ru='Трент? Я помню Трента и ты на него... ну смахиваешь местами. '),
        VoiceLine(70, JackRazorBarber, ru='Ты наверное тот второй Трент, который пошел на дн+о ч+ёрной дыр+ы вместе с большой злобной каракатицей.'),
        VoiceLine(80, JackRazorBarber, ru='Я скормил своей глотке три полновесных анкера рома, дабы упокоить твою душу! И что же я вижу? '),
        VoiceLine(90, JackRazorBarber, ru='Ты сто+ишь тут,, целехонький,, как новенький пиастр, пока в моей голове палят все пушки форта! Какого дьявола ты ещё коптишь это небо?!'),
        VoiceLine(100, Trent, ru='Ну... я    в+ыздоровел! Так, давай на чистоту. У меня задание от мисс Зейн. Мне нужн+ы ты, твоя команда и твой пиратский корабль.'),
        VoiceLine(110, Trent, ru='Так что ты или идёшь со мной. Или продолжишь тут киснуть до конца своих дней!'),
        VoiceLine(120, JackRazorBarber, ru='Притуши фитиль, юнга. Весточку от миледи я получил. Но мне сейчас страшно опасно выход+ить в море.'),
        VoiceLine(130, JackRazorBarber, ru='За мо+ю голову назначили такую цену, что теперь даже у портовых крыс чешутся лапы сдать меня властям.'),
        VoiceLine(140, JackRazorBarber, ru='Но они дрейфят заколоть меня прямо здесь. Запрещают законы местного порта. А вот стоит мне поднять якорь, как все коршуны слетятся на мо+ю тушу.'),
        VoiceLine(150, Trent, ru='И что ты предлагаешь? Сидеть здесь и ждать, когда вместо местных крыс к тебе придут кочевники и сожрут твои мозги? Так чтоли?'),
        VoiceLine(160, JackRazorBarber, ru='Действительно,, юнга, дело говоришь. Если не разорвут живьем эти шакалы, то набегут другие. И этих других я в одиночку своей шпагой не заколю.'),
        VoiceLine(170, JackRazorBarber, ru='Поднимай парус+а, юнга. Мы вых+одим в море. Насколько вместительно брюхо твоего корвета?'),
        VoiceLine(180, Trent, ru='Ну есть лишнее местечко в трюме. А ты к чему это?'),
        VoiceLine(190, JackRazorBarber, ru='Заберу с собой тайную заначку. Не хочу возвращаться в эту гавань.'),
        VoiceLine(200, Trent, ru='Влезет. Давай собирайся. Время не ждёт.'),
    ]


class RobigoSpace(MsnRobigo, script.SpaceVoiceProps):
    VOICE_LINES = [
        # VoiceLine(5, Hatcher, ru='Направляемся в Сферу. Трент, веди нас', en='Setting course for the Sphere. Trent, lead the way!'),
    ]


class Mission17(MsnRobigo, script.StoryMission):
    CUTSCENES = [
        JackMeetScene,
    ]
    SPACE_CLASS = RobigoSpace
    SYNC_SPACE = True

    MISSION_TITLE = 'Эпилог. Миссия в Терновнике'
