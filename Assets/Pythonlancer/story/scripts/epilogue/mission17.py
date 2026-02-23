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
        VoiceLine(10, Trent, ru='Эй, с протезом. Это ты Джек Брадобрей?', en="Hey, you with prosthesis. Are you Jack Razorbarber?"),
        VoiceLine(20, JackRazorBarber, ru='Прикус+и яз+ык, висельный прихвостень! Перед тобой сам капитан Джек Брадобр+ей!',
                  en="Bite your tongue, you gallows-bait! You stand before Captain The Jack Razorbarber himself!"),
        VoiceLine(30, JackRazorBarber, ru='Если пришёл содрать мо+ю шкуру ради горсти золот+ых, то сначала склони голову и прояви почтение, пока я не приколол твой язык к мачте на потеху чайкам!',
                  en="If you've come to claim my hide for a fistful of gold, you'd best bow your head and show some respect, lest I nail your tongue to the mast as sport for the gulls!"),
        VoiceLine(40, Trent, ru='Эй, дядя, следи за базаром! Я не охотник за головами, я Трент и я работаю на "Комитет по спасению человечества".',
                  en="Hey, Old Timer, watch your mouth! I'm no bounty hunter. I'm Trent, and I work for the Committee for the Salvation of Humanity."),
        VoiceLine(50, Trent, ru='И мне нужен ты, чтобы спасти это грёбаное человечество от новой угрозы!',
                  en="I need you to help save this damn humanity from a new threat!"),
        VoiceLine(60, JackRazorBarber, ru='Трент? Я помню Трента и ты на него... ну смахиваешь местами. ',
                  en="Trent? I remember a Trent, and you... bear a passing resemblance."),
        VoiceLine(70, JackRazorBarber, ru='Ты наверное тот второй Трент, который пошел на дн+о ч+ёрной дыр+ы вместе с большой злобной каракатицей.',
                  en="You must be that other Trent - the one who went down into the black hole with that great, malevolent kraken."),
        VoiceLine(80, JackRazorBarber, ru='Я скормил своей глотке три полновесных анкера рома, дабы упокоить твою душу! И что же я вижу? ',
                  en="I fed three full anchors of rum to me own gullet to lay your soul to rest! And what do I spy before me?"),
        VoiceLine(90, JackRazorBarber, ru='Ты сто+ишь тут,, целехонький,, как новенький пиастр, пока в моей голове палят все пушки форта! Какого дьявола ты ещё коптишь это небо?!',
                  en="You stand here, as hale and whole as a freshly minted doubloon, while every cannon in the fort fires a salute inside me skull! Why in devils name are you still blackening the sky?!"),
        VoiceLine(100, Trent, ru='Ну... я в+ыздоровел! Так,, давай на чистоту. У меня задание от мисс Зейн. Мне нужн+ы ты, твоя команда и твой пиратский корабль.',
                  en="I just got better! Now, let's cut to the chase. I've got a mission from Miss Zane. I need you with your clothes, your crew, and your pirate ship."),
        VoiceLine(110, Trent, ru='Так что ты или идёшь со мной. Или продолжишь тут киснуть до конца своих дней!',
                  en="So either you come with me, or you can rot here until the end of your days!"),
        VoiceLine(120, JackRazorBarber, ru='Притуши фитиль, юнга. Весточку от миледи я получил. Но мне сейчас страшно опасно выход+ить в море.',
                  en="Douse your fuse, lad. I received word from milady. But it's perilous for me to set sail now."),
        VoiceLine(130, JackRazorBarber, ru='За мо+ю голову назначили такую цену, что теперь даже у портовых крыс чешутся лапы сдать меня властям.',
                  en="There's such a price on my head that even the dock rats are itching to turn me over to the authorities."),
        VoiceLine(140, JackRazorBarber, ru='Но они дрейфят заколоть меня прямо здесь. Запрещают законы местного порта. А вот стоит мне поднять якорь, как все коршуны слетятся на мо+ю тушу.',
                  en="They daren't slit me throat here, though-port laws forbid it. But the moment I weigh anchor, every carrion bird in the sector will descend upon me carcass."),
        VoiceLine(150, Trent, ru='И что ты предлагаешь? Сидеть здесь и ждать, когда вместо местных крыс к тебе придут кочевники и сожрут твои мозги? Так чтоли?',
                  en="And what's your plan? Sit here and wait for the Nomads to show up instead of the locals and eat your brains? Is that it?"),
        VoiceLine(160, JackRazorBarber, ru='Действительно,, юнга, дело говоришь. Если не разорвут живьем эти шакалы, то набегут другие. И этих других я в одиночку своей шпагой не заколю.'),
        VoiceLine(170, JackRazorBarber, ru='Поднимай парус+а, юнга. Мы вых+одим в море. Насколько вместительно брюхо твоего корвета?', en="Ready the sails, lad. We're putting out to sea. How spacious is the belly of your corvette?"),
        VoiceLine(180, Trent, ru='Ну есть лишнее местечко в трюме. А ты к чему это?', en="There's some spare room in the hold. Why are you asking?"),
        VoiceLine(190, JackRazorBarber, ru='Заберу с собой тайную заначку. Не хочу возвращаться в эту гавань.', en="I'll be bringing me secret stash. No point returning to this harbor."),
        VoiceLine(200, Trent, ru='Влезет. Давай собирайся. Время не ждёт.', en="It'll fit. Get moving. Time's wasting."),
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
