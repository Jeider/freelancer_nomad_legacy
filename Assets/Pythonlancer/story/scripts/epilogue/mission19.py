from story import script
from audio.sound import VoiceLine
from story.actors import Trent, JackRazorBarber, MisterAndrew
from story.cutscenes.epilogue_scenes import m19


class MsnHispanyola(object):
    MISSION_INDEX = 19


class ReactorScene(MsnHispanyola, script.CutsceneProps):
    ALIAS = 'reactor'
    TITLE = 'Линкор Испаньола'
    THORN_CLASS = m19.ReactorScene
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(10, JackRazorBarber, ru="Ну что, соскучилась по открытому морю, старая подруга?"),
        VoiceLine(20, JackRazorBarber, ru="Мистер Эндрю! Статус систем корабля!"),
        VoiceLine(30, MisterAndrew,
                  ru="Капитан,, все системы работают штатно. Обнаружен недостаток энергии. Нам нужны новые реакторы."),
        VoiceLine(40, JackRazorBarber, ru="Мистер Эндрю,, где мы можем получить новые реакторы."),
        VoiceLine(50, MisterAndrew,
                  ru="Мы находимся в зоне разбора кораблей. Возможно,, в этих обломках остались подходящие нам реакторы."),
        VoiceLine(60, JackRazorBarber, ru="Капрал Трент!"),
        VoiceLine(70, Trent, ru="Да,, капитан?"),
        VoiceLine(80, JackRazorBarber,
                  ru="Трент, нам н+ужно получить новые реакторы,, чтобы раскочегарить сердце Испаньолы."),
        VoiceLine(90, JackRazorBarber, ru="Ты сможешь достать их?"),
        VoiceLine(100, Trent, ru="Смогу. Отправляюсь."),
    ]


class ReadyScene(MsnHispanyola, script.CutsceneProps):
    ALIAS = 'ready'
    TITLE = 'Линкор Испаньола'
    THORN_CLASS = m19.ReadyScene
    DESCRIPTION = ''
    VOICE_LINES = [
        VoiceLine(20, JackRazorBarber, ru="Испаньола снова дышит! Теперь нас не догонит даже сам дьявол!"),
        VoiceLine(30, JackRazorBarber, ru="Эй,, капрал, может ну его спасение мира и отправимся грабить караваны?"),
        VoiceLine(40, Trent, ru="Никак нет,, капитан. У нас есть дело."),
        VoiceLine(50, JackRazorBarber, ru="Всё хочешь обокрасть этого коллекционера?"),
        VoiceLine(60, Trent, ru="Возможно я найду более дипломатические способы."),
        VoiceLine(70, JackRazorBarber,
                  ru="Этот старый лис вцепился в свой сундук мертвой хваткой! Придется отрубить ему руки вместе с ключами!"),
        VoiceLine(80, Trent, ru="Капитан,, я не улавливаю суть этой гиперболы."),
        VoiceLine(90, JackRazorBarber, ru="Тебе придётся надрать ему жопу."),
        VoiceLine(100, Trent,
                  ru="Ну так надерём. Если повезет,, то с кого с кого,, а с Дж+аббы мы точно сможем содрать что-то ценное."),
        VoiceLine(110, JackRazorBarber, ru="А ты смекаешь,, капрал. Дж+абба самый богатый хрыщ в этих морях."),
        VoiceLine(120, Trent, ru="Тогда я отправлюсь на рекогносцировку, а вы плывите следом."),
        VoiceLine(130, Trent, ru="Подготовьте корабль к сражению. Будет жарко."),
    ]

class HispanyolaSpace(MsnHispanyola, script.SpaceVoiceProps):
    VOICE_LINES = [
        # VoiceLine(5, Hatcher, ru='Направляемся в Сферу. Трент, веди нас', en='Setting course for the Sphere. Trent, lead the way!'),
    ]


class Mission19(MsnHispanyola, script.StoryMission):
    CUTSCENES = [
        ReactorScene,
        ReadyScene,
    ]
    SPACE_CLASS = HispanyolaSpace
    SYNC_SPACE = True

    MISSION_TITLE = 'Эпилог. Получени Испаньолы'
