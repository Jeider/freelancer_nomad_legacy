from story import script
from audio.sound import VoiceLine
from story.actors import (
    Trent, Darcy, CorsairBarman, Rockford, Tortuga, JabbaBandit, RockfordStation
)


class Msn7(object):
    MISSION_INDEX = 7


class Msn7Space(Msn7, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(10, Trent, ru='Я тут каких-то гопников раскидал, но Железного Зада среди них не было.'),
        VoiceLine(20, CorsairBarman,
                  ru='Айронсайда, мистер Трент, Билла Айронсайда. Если его не было здесь, попробуйте во втором вероятном месте его пребывания. Скидываю координаты.'),
        VoiceLine(30, Trent, ru='Сколько сколько прилетело? 500 кредитов? Они тут совсем охренели?'),
        VoiceLine(35, Trent,
                  ru='Проще было вообще перевод не делать - на банковской комиссии больше потеряли. Стоит, пожалуй, еще пару вопросов этому бармену задать. Например, "где деньги, Лебовски?".'),
        VoiceLine(40, RockfordStation,
                  ru='Мистер Трент, меня зовут Р+окфорд, СБА прислало меня пом+очь вам в поиске артефактов. Жду вас в баре на планете Кадиз. Прошу вас быть как можно скорее, счет идет на секунды.'),
        VoiceLine(60, Rockford, ru='Трент, жить хочешь? Помогай!'),
        VoiceLine(70, Rockford,
                  ru='Трент, теперь летим в торговую линию! Нам нужно добраться до Малого Омикрона'),
        VoiceLine(80, Trent, ru='Приятно познакомиться, мистер Рокфорд.'),
        VoiceLine(90, Rockford, ru='Не мистер. Просто Р+окфорд.'),
        VoiceLine(100, Trent, ru='Кто были все эти люди, Рокфорд?'),
        VoiceLine(110, Rockford, ru='Агенты Ордена.'),
        VoiceLine(120, Trent, ru='А можно поподробнее?'),
        VoiceLine(130, Rockford, ru='О чём?'),
        VoiceLine(140, Trent, ru='Вообще о многом. Если вкратце, кто вы и во что я в очередной раз вляпался.'),
        VoiceLine(150, Rockford,
                  ru='Я агент СБА Р+окфорд и меня прислали на помощь группе Дельта и вам, Трент, потому что вы вляпались в неприятности.'),
        VoiceLine(160, Trent,
                  ru='Да твою же налево... Хорошо, тогда расскажите более развернуто, как вы меня нашли, почему вас, то есть нас на Кадизе ждали, и что вообще мы теперь планируем делать.'),
        VoiceLine(170, Rockford,
                  ru='Когда я прибыл в систему Кадиз, я вышел на связь с лидером Дельта и узнал от него о сложившейся ситуации и о том, что боеспособный корабль остался только у вас. '),
        VoiceLine(180, Rockford,
                  ru='Я отследил все взятые в этой системе фрилансерами контракты и определил ваше местонахождение. Кстати, Трент, вы действительно готовы работать за такие грош+и?'),
        VoiceLine(190, Trent, ru='Не будем об этом. Что было дальше?'),
        VoiceLine(200, Rockford,
                  ru='Я знал что за вами следят агенты Ордена. Кроме того, они подозревали о моем присутствии в системе.'),
        VoiceLine(210, Rockford,
                  ru='Поэтому я решил устроить им ловушку и послал вам сообщение с просьбой о встрече в максимально удаленной от их главных сил точке - на планете Кадиз.'),
        VoiceLine(220, Rockford,
                  ru='Они смогли отправить на Кадиз только небольшую группу перехвата, а мы с вами, Трент смогли ее уничтожить. Насчет того, что делать дальше, по-моему очевидно, забирать артефакты.'),
        VoiceLine(230, Trent, ru='И у нас уже есть план?'),
        VoiceLine(240, Rockford, ru='Конечно. Как можно лететь куда-то без плана?'),
        VoiceLine(250, Trent, ru='Меня в него не посветите?'),
        VoiceLine(260, Rockford,
                  ru='Артефакты содержатся на базе Тортуга в системе Малый Омикрон. Формально это пиратская база, но она используется агентами Ордена и поэтому отлично защищена.'),
        VoiceLine(270, Rockford,
                  ru='На станции находится передатчик, обеспечивающий постоянную двустороннюю связь со штабом Ордена.'),
        VoiceLine(280, Rockford,
                  ru='Если передатчик будет выведен из строя, по протоколу они обязаны эвакуировать все важные объекты на ближайшую другую базу. Мы разрушим передатчик и нападем на конвой, перевозящий артефакты.'),
        VoiceLine(290, Trent, ru='Эмм... Ну ты у нас тут специалист, тебе виднее. '),
        VoiceLine(310, Rockford,
                  ru='Сейчас я сброшу контейнеры с зарядами направленного действия. Подберите их, Трент, расположите вокруг передатчика и подорвите. '),
        VoiceLine(320, Rockford,
                  ru='Устанавливайте заряды с выключенным щитом, иначе они сдетонируют. Координаты передатчика в вашем компьютере. Вперед!'),
        VoiceLine(330, Tortuga, ru='Фрилансер альфа-один, немедленно покиньте запретную зону... '),
        VoiceLine(340, Tortuga,
                  ru='Фрилансер альфа-один, если вы не покинете зону, мы будем вынуждены активировать защитный периметр!'),
        VoiceLine(350, Trent, ru='Готово. Передатчик уничтожен.'),
        VoiceLine(355, Rockford, ru='Я заметил. Судя по переговорам вся станция на ушах сто+ит. Теперь посм+отрим, что они сделают.'),
        VoiceLine(360, Rockford, ru='Вижу конвой выходящий из Тортуги. Направляюсь за ним. Передаю координаты.'),
        VoiceLine(370, Rockford, ru='Перехватываю грузовик. Нужна помощь.'),

        VoiceLine(380, Rockford, ru='Трент, атакуй грузовик!'),
        VoiceLine(390, Trent, ru='Щит грузовика просто непробиваем. Что делать то?'),
        VoiceLine(395, Rockford,
                  ru='Трент, атакуй грузовик! Это сверхзащищённая модель, его щит неуязв+им. Но есть способ преодолеть эту защиту.'),
        VoiceLine(400, Rockford,
                  ru='Частое использование Электромагнитной пушки приведет к перегреву генераторов и отключению щита. Подлети ближе к транспорту, чтобы пилот мог по тебе стрелять.'),
        VoiceLine(410, Trent, ru='В смысле? Быть приманкой?'),
        VoiceLine(420, Rockford, ru='Да. '),
        VoiceLine(430, Rockford, ru='Щит упал. Трент, уничтожь грузовик! Целься в уявзимые точки!'),
        VoiceLine(440, Rockford, ru='Они вызывают подкрепление. Скоро вся эта зона будет кишать пилотами Ордена. Уничтожь транспорт! Быстрее!'),
        VoiceLine(445, Rockford, ru='Транспорт взорван, подбери артефакты!'),

        VoiceLine(450, Trent, ru='Это было потно. Куда теперь?'),
        VoiceLine(460, Rockford,
                  ru='У меня есть убежище в Омега-13. Проведем там обслуживание кораблей и разработаем план доставки артефактов в штаб СБА.'),
        VoiceLine(470, Trent,
                  ru='Звучит отлично! Веди. Кстати, а что попалось тебе? У меня какая-то мелочевка кочевников и том Протея... Значит ключ у тебя?'),
        VoiceLine(480, Rockford, ru='Да.'),

        VoiceLine(490, Trent,
                  'Кстати, Рокфорд, а почему тебя так хотят убить агенты Ордена? Стоило тебе выйти на связь и на место встречи прибыла целая армия.'),
        VoiceLine(495, Rockford,
                  ru='Я был агентом еще старого, большого Ордена. Я слишком много знаю. С момента раскола постоянно приходится спать вполглаза.'),
        VoiceLine(498, Rockford, ru='Даже сейчас нужно держать ухо в остро. Мы можем нарваться на патруль в любой момент'),

        VoiceLine(500, Trent, ru='Нужно добраться до ближайшей базы.'),
        VoiceLine(510, Darcy, ru='Давай, шутник, залетай в торговую линию. Тут лететь не далеко.'),
        VoiceLine(520, Darcy, ru='Ты там особо с ним не откровенничай. Эта личность чрезвычайно мутная. '),
        VoiceLine(530, Darcy,
                  ru='Он часто бывает нам полезен, поэтому мы закрываем глаза на его мелкие шалости, но, чует мое сердце, до поры до времени. Когда-нибудь он нарвется.'),
        VoiceLine(550, JabbaBandit, ru='Фрилансер, у тебя есть кое-что что, что очень нужно нам. Отдавай по-хорошему!'),
        VoiceLine(560, Darcy,
                  ru='Мальчики, а вы не охренели? Это мой участок, я здесь главный коп. Трент, давай разберем эту шпану. '),
        VoiceLine(570, Darcy,
                  ru='Джабба, засранец, теперь ты точно доигрался. Трент, я вернусь, поговорю с нашим другом еще раз. Увидимся на станции.'),
        VoiceLine(2000, CorsairBarman,
                  ru='Координаты последнего местоположения бандитов Старлайна в вашей нейросети. Возможно, Билл Айронсайд там. Разыщите его.'),
        VoiceLine(2010, CorsairBarman,
                  ru='Айронсайд убит, теперь эти ублюдки нас долго не побеспокоят. Пересылаю ваше вознаграждение. Конец связи.'),
    ]


class Mission7(Msn7, script.StoryMission):
    MISSION_INDEX = 7
    CUTSCENES = []
    SPACE_CLASS = Msn7Space
    SYNC_SPACE = True

    MISSION_TITLE = 'Миссия 7. Возвращение артефактов'
