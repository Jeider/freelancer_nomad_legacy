from story import script
from story.voice.sound import VoiceLine
from story.actors import Trent, Kim, Darcy, King, Hatcher, Alaric, Mandrake, Kruger, FortBush


class Msn12(object):
    MISSION_INDEX = 12


class Msn12PigarCutscene(Msn12, script.CutsceneProps):
    ALIAS = 'pigar'
    TITLE = 'Исследовательская зона планеты Пигар'
    DESCRIPTION = 'Все в сборе, Трент сразу начинает за правду матку'
    VOICE_LINES = [
        VoiceLine(10, Trent, ru='В данный момент Рокфорд летит к сфере кочевников, чтобы реализовать план, который, по его мнению, должен спасти человечество.'),
        VoiceLine(20, Trent, ru='Есть мнение, что в процессе своего спасения человечество может погибнуть. Его нужно остановить!'),

        VoiceLine(30, Hatcher, ru='Кого? Рокфорда или человечество? Человечество мы не остановить не сможем, а Рокфорда...'),
        VoiceLine(40, Hatcher, ru='Как ты себе это предстваляешь? У него есть ключ, и он летит к сфере. Или не к сфере. Что мы вообще знаем о его плане?'),

        VoiceLine(50, Trent, ru='Ключ есть и у меня,(показывает всем ключ) как видите.'),
        VoiceLine(60, Trent, ru='А по поводу деталей плана... Наверняка их можно найти в архивах СБА.'),
        VoiceLine(70, Trent, ru='Он достаточно долго и успешно работал на эту организацию, и наверняка предлагал его осуществление руководству.'),

        VoiceLine(80, Mandrake, ru='Я видел эти документы в архиве, но они засекречены.'),
        VoiceLine(90, Mandrake, ru='Требуется максимальный уровень доступа, который есть только у двух человек - у Кинга, и еще у кого-то, о ком я не знаю.'),
        VoiceLine(100, Mandrake, ru='Чисто теоретически их можно просмотреть хоть с этого компьютера, если бы среди нас был один из этих двух.'),

        VoiceLine(110, Trent, ru='Полагаю, у меня получится. (прикладывает карту доступа) Вот как-то так.'),
        VoiceLine(120, Darcy, ru='Нихрена-ж себе.'),
        VoiceLine(130, Alaric, ru='Я о тебе чего-то не знаю?'),

        VoiceLine(140, Hatcher, comment='Тревога! Хетчер подходит к столу с коммуникатором. На её лице ужас',
                  ru='Эт-то что еще за? Так... Штаб СБА атакован.'),
        VoiceLine(150, Hatcher, ru='Всем силам СБА в системе Сириуса приказано прибыть в штаб.'),
        VoiceLine(160, Hatcher, ru='Силы противника превосходят... Да кто же это?'),

        VoiceLine(170, Trent, ru='(Ужас) Черт... Ким же говорила про спецоперацию... Твою мать... Они на это решились.'),
        VoiceLine(180, Hatcher, ru='Кто решился? На что? Ты о чем вообще?'),

        VoiceLine(190, Trent, ru='Орден решил показать кто тут главный и устранить прямого конкурента. Орден атаковал СБА, понимаешь?'),
        VoiceLine(200, Trent, ru='Чтобы полностью уничтожить СБА и стать главной силой в секторе Сириуса. И в самый неподходящий момент.'),
        VoiceLine(210, Trent, ru='Нахрен. Не нужны нам никакие кочевники, мы сами друг другу глотку перегрызем. Просто ради удовлетворения амбиций.'),

        VoiceLine(220, Hatcher, ru='(Осознав, выдохнув и решившись) Я им этого не позволю! Вылетаем!'),
    ]


class Msn12CapturedCutscene(Msn12, script.CutsceneProps):
    ALIAS = 'captured'
    TITLE = 'Бар линкора Осирис'
    DESCRIPTION = 'Ямамото пленён. Теперь нужно убедить Кинга заняться Рокфордом'
    VOICE_LINES = [
        VoiceLine(10, King, ru='Что с Ямамото?'),
        VoiceLine(20, Hatcher, ru='Ведем дознание. Не хотите ли поприсутствовать?'),
        VoiceLine(30, King, ru='О, да! Этот безбашенный самурай превзошел самого себя.'),
        VoiceLine(40, King, ru='С удовольствием посмотрел бы что творится у него в мозгах, а лучше, заспиртовал бы их в банке.'),

        VoiceLine(50, Trent, ru='Генерал Кинг, нужно срочно остановить Рокфорда!'),
        VoiceLine(60, King, ru='Дался вам этот Рокфорд... Если он где-нибудь набедокурит, наши силы все подчистят.'),
        VoiceLine(70, King, ru='А его загонят, как зайца, далеко в приграничье. Сам сдаваться придет, вот увидите.'),
        VoiceLine(80, Hatcher, ru='Генерал Кинг, вызов от профессора Мандрейка.'),
        VoiceLine(90, King, ru='Выведите на главный экран.'),

        VoiceLine(100, Mandrake, ru='Генерал Кинг, мистер Трент, мисс Хетчер. О, да я смотрю, все в сборе.'),
        VoiceLine(110, Mandrake, ru='Я ознакомился с так называемым планом Рокфорда. Как ученый, могу сказать - он хорош.'),
        VoiceLine(120, Mandrake, ru='Рокфорд связал около двадцати лазерных орудий кочевников в единую систему. '
                               'Интересное с инженерной точки зрения решение, надо сказать.'),
        VoiceLine(130, Mandrake, ru='Он хочет направить получившийся в результате луч на сферу чтобы уничтожить её, '
                               'и вместе с ней все, так называемое, наследие кочевников.'),

        VoiceLine(140, Trent, ru='И как это произойдет?'),
        VoiceLine(150, Mandrake, ru='Если простыми словами - сфера перестанет существовать. '
                               'Как и... от половины до двух третей сектора Сириуса.'),
        VoiceLine(160, Darcy, ru='Масштабненько.'),

        VoiceLine(170, Trent, ru='ЕГО... НАДО... ОСТАНОВИТЬ!!! Поймите это, наконец!'),
        VoiceLine(180, Alaric, ru='Я с тобой дружище!'),
        VoiceLine(190, Darcy, ru='Не могу пропустить такое представление.'),
        VoiceLine(200, King, ru='Мои ресурсы в вашем распоряжении. Я выделю вам нашу лучшую спецгруппу.'),
        VoiceLine(210, Hatcher, ru='И возглавлю её я.'),
    ]


class Msn12Space(Msn12, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(10, Trent, ru='Хетчер, слышишь меня?'),
        VoiceLine(20, Hatcher, ru='Да, Трент, что случилось?'),
        VoiceLine(30, Trent, ru='Срочно вылетай на планету Пигар, все подробности там!'),
        VoiceLine(40, Hatcher, ru='М-да? Ладно, вылетаю.'),

        VoiceLine(50, Trent, ru='Дерси!'),
        VoiceLine(60, Trent, ru='Дерси здесь.'),
        VoiceLine(70, Trent, ru='Вылетай на планету Пигар. Прямо сейчас, все объясню при встрече.'),
        VoiceLine(80, Trent, ru='Опять что-то интересненькое? Лечу!'),

        VoiceLine(90, Trent, ru='Аларик!'),
        VoiceLine(100, Alaric, ru='А, Трент, ты как раз во время, я хотел...'),
        VoiceLine(110, Trent, ru='Стоп! Аларик, помолчи. Срочно вылетай на планету Пигар!'),
        VoiceLine(120, Alaric, ru='Как на Пигар?'),
        VoiceLine(130, Trent, ru='Молча! Аларик, ты понял?'),
        VoiceLine(140, Alaric, ru='Да.'),
        VoiceLine(150, Trent, ru='Вот и хорошо.'),
        VoiceLine(160, Alaric, ru='Но...'),
        VoiceLine(170, Trent, ru='Молча, Аларик, молча.'),

        VoiceLine(180, Kim, ru='Трент?'),
        VoiceLine(190, Trent, ru='На связи.'),
        VoiceLine(200, Kim, ru='Ямамото вызывает тебя в Омега-3. Готовится спецоперация, нам нужны все доступные силы.'),
        VoiceLine(210, Kim, ru='Поэтому позови друзей, всех кто может, их участие будет вознаграждено.'),
        VoiceLine(220, Trent, ru='Нет. Ким, у меня появилось очень срочное и очень важное дело.'),
        VoiceLine(230, Kim, ru='Настолько срочное и важное, что решил Ямамото послать?'),
        VoiceLine(240, Trent, ru='Именно.'),
        VoiceLine(250, Kim, ru='(после долгого молчания) Как знаешь...'),

        VoiceLine(260, Hatcher, ru='Штаб, как обстановка?'),
        VoiceLine(270, Kruger, ru='Мы сдержали первый удар, но они готовят новую атаку.'),
        VoiceLine(280, Hatcher, ru='Держитесь! Подкрепление уже на подходе!'),

        VoiceLine(290, Hatcher, comment='Этап 1 - мясорубка',
                  ru='Штаб, мой отряд находится рядом с вражеским линкором Нагато. Мы вступаем в бой.'),
        VoiceLine(300, Kruger, ru='Вас поняли, мисс Хетчер.'),

        VoiceLine(310, Hatcher, ru='Флотилия Нагато разбита.'),
        VoiceLine(320, Kruger, ru='Вижу приближающуюся к вам группу торпедных канонерок.'),
        VoiceLine(330, Kruger, ru='Внимание! Форт Буш атакован значительными силами противника!'),
        VoiceLine(340, Alaric, ru='Займитесь прорывом. Я беру канонерки на себя.'),
        VoiceLine(350, Hatcher, ru='Отлично, Аларик. Трент, не тормози. Летим к форту.'),

        VoiceLine(360, FortBush, comment='Этап 2 - бывш. форт Буш', ru='Внимание! Всеобщая эвакуация! Всем...хрррхррр'),
        VoiceLine(370, Darcy, comment='Форт Буш взрывается нафиг', ru='Остались от Буша только ножки...'),
        VoiceLine(380, Hatcher, ru='Ничего хорошего, форт был последним рубежом обороны на этом фланге. '
                               'Срочно атакуйте вражеские корабли.'),
        VoiceLine(390, Hatcher, ru='Ни в коем случае нельзя им дать приблизиться к Энтерпрайзу!'),

        VoiceLine(400, Hatcher, ru='Генерал Кинг, срочно нужны резервы в районе бывшего форта Буш.'),
        VoiceLine(410, King, ru='Мы летим. Осирис выдвинулся к вам на помощь.'),
        VoiceLine(420, Hatcher, ru='Ты не рискуешь?'),
        VoiceLine(430, King, ru='У нас нет другого выбора...'),

        VoiceLine(440, Hatcher, ru='Есть! Наступление врага захлебнулось!'),
        VoiceLine(450, King, comment='Этап 3 - Мусаси',
                  ru='Внимание всем! Обнаружен линкор Мусаси. Нам нужно выбивать его двигатели в кратчайшее время, '
                    'иначе Ямамото сбежит и всё начнется сначала. Как поняли?'),
        VoiceLine(460, Alaric, ru='Аларик, принял!'),
        VoiceLine(470, Darcy, ru='Дерси, принято!'),
        VoiceLine(480, Trent, ru='Трент, принял!'),

        VoiceLine(490, Trent, ru='Мусаси на прицеле.'),
        VoiceLine(500, Darcy, ru='Атакуем двигатели. Мусаси уже разогревает гипердвигатель, но у нас еще есть время.'),
        VoiceLine(510, Trent, comment='Неудача', ru='Чёрт! Мусаси смылся! Мы не успели...'),

        VoiceLine(520, Trent, comment='Двигатели снесены', ru='Двигатели Мусаси нейтрализованы.'),
        VoiceLine(530, Darcy, ru='Замечена аномальная радиационная активность. Что там происходит?'),
        VoiceLine(540, Hatcher, ru='Да вашу ж... он хочет перегрузить реактор и самоуничтожиться. Устроить эдакое сеппуку.'),
        VoiceLine(550, Hatcher, ru='Атакуйте рубку Мусаси, чтобы ликвидировать управление. Давайте скорее, а то взрывом заденет и нас. Мало не покажется.'),

        VoiceLine(560, Darcy, comment='Рубка снесена', ru='Сделано, рубки нет.'),
        VoiceLine(570, Hatcher, ru='Трент, мы хотим десантироваться на Мусаси. Нужно взломать двери. Справишься?'),
        VoiceLine(580, Trent, ru='Да как нечего делать. Я уже профи хакер.'),

        VoiceLine(590, Hatcher, comment='Двери взломаны', ru='Есть! Десант уже начинает стыковку.'),
        VoiceLine(600, Hatcher, ru='Генерал Кинг, Ямамото у нас в плену.'),
        VoiceLine(610, King, ru='Отличная работа, мисс Хетчер. Заходите на посадку на Осирис.'),
    ]


class Mission12(Msn12, script.StoryMission):
    CUTSCENES = [
        Msn12PigarCutscene,
        Msn12CapturedCutscene,
    ]
    SPACE_CLASS = Msn12Space

    MISSION_TITLE = 'Миссия 12. Оборона Энтерпрайза'


