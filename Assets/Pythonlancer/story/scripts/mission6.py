from story import script
from audio.sound import VoiceLine
from story.actors import (
    Trent, Hatcher, HatcherStation, FinnRunner, Reitherman, DeltaOne, DeltaThree,
    SphereAssistant, SphereOutpost, SphereMissouri,
    Alaric, OrderPilot, Ceed
)


class Msn6(object):
    MISSION_INDEX = 6


class Msn6Space(Msn6, script.SpaceVoiceProps):
    VOICE_LINES = [
        VoiceLine(
            0,
            HatcherStation,
            ru="Мистер Трент, я жду вас и вашего компаньона баре космопорта планеты Питтсбург, система Нью-Йорк.",
            en="Mr. Trent, I'm waiting for you and your companion on Planet Pittsburg in the New-York System..",
        ),
        VoiceLine(
            10,
            Hatcher,
            ru="Джентльмены, берем курс на линкор Миссури.",
            en="Gentlemen, please set course to Battleship Missouri.",
        ),
        VoiceLine(
            20,
            Trent,
            ru="Зная рейнландцев, они вокруг этой сферы и ученых наверняка военных на каждый астеорид понапихали, пригнали в систему линкор.",
            en="Knowing Rheinland, there’s probably tight guard around each and every asteroid around the sphere, and I bet they stuck a battleship in there.",
        ),
        VoiceLine(
            30,
            Hatcher,
            ru="Берите выше, мистер Трент, у них там развернута военная база.",
            en="That's an understatement, Mr. Trent. In fact, they have a fully deployed military base there.",
        ),
        VoiceLine(
            40,
            Trent,
            ru="Тогда, простите, каким образом мы с напарником должны будем с ними справиться? Вы выдадите нам карманную черную дыру?",
            en="Excuse me, but how exactly do you expect me and my wingman to deal with that? Are you gonna give us a black hole that can fit in our pockets?",
        ),
        VoiceLine(
            50,
            Hatcher,
            ru="Нет, она еще проходит стендовые испытания. Я сейчас сброшу вам по контейнеру, подберите их и стыкуемся с Миссури. ",
            en="No, that device is still being tested. I'll drop a few containers for you, tractor them in and dock with Missouri.",
        ),
        VoiceLine(
            55,
            HatcherStation,
            ru="Наши военные аналитики разработали стратегии выполнения задания. Эти стратегии уже загружены в ваши корабли. "
               "Можете воспользоваться при необходимости.",
        ),
        VoiceLine(
            60,
            HatcherStation,
            ru="Удачи, джентльмены. Напоминаю, на территории Рейнланда никаких радиопереговоров со мной.",
            en="Best of luck, gentlemen. And remember – maintain radio silence with me once you've reached Rheinland.",
        ),
        VoiceLine(
            70,
            Alaric,
            ru="Трент, чтобы увеличить наши шансы, предлагаю разделиться. Встречаемся внутри Сферы.",
            en="Trent, we’ll have a better chance at it if we split up. I'll meet you inside the sphere.",
        ),
        VoiceLine(
            80,
            SphereOutpost,
            ru="Подключен последний аванпост. Внешний периметр замкнут.",
            en="Last outpost is operational. External perimeter is locked down.",
        ),
        VoiceLine(
            90,
            Alaric,
            ru="У нас получилось, Трент.",
            en="We made it, Trent!",
        ),
        VoiceLine(
            100,
            Trent,
            ru="Только теперь внешний периметр закрыт, и назад дороги нет.",
            en="Except the outer perimeter is locked down, so there's no longer a way back.",
        ),
        VoiceLine(
            110,
            Alaric,
            ru="Трент, мы входим в зал в котором рейнландцы развернули лабораторию. Артефакты должны быть где-то внутри. ",
            en="Trent, we're entering the hall where Rheinlanders deployed their lab. Artifacts should be somewhere inside.",
        ),
        VoiceLine(
            120,
            Alaric,
            ru="Попробуй пробраться внутрь через шлюзы и найти Роттермана, а я в это время попробую снять или хотя бы ослабить щиты.",
            en="Try sneaking in through the airlocks and find Rotterman, while I try to take down or weaken the shields.",
        ),
        VoiceLine(
            130,
            Trent,
            ru="Аларик, тут все задраено. Не пройти.",
            en="Alaric, it's all sealed down here. I can't get through.",
        ),
        VoiceLine(
            140,
            Alaric,
            ru="Трент, есть другой путь, через технические тоннели. Скидываю координаты.",
            en="Trent, there's another way, through maintenance vents. I'm sending you the coordinates.",
        ),
        VoiceLine(
            150,
            Trent,
            ru="Аларик, тут что-то непонятное. Какой-то кристалл, вокруг которого летают корабли Кочевников.",
            en="Alaric, there's something weird in here. Some kind of crystal, surrounded by Nomad ships.",
        ),
        VoiceLine(
            160,
            Alaric,
            ru="По данным СБА этот кристалл назвали 'Номадским зерном'. Если кочевники тебя заметят, то из Зерна будут появляться все новые и новые истребители.",
            en="ASF intel says this crystal is called 'The Nomad Seed'. If Nomads sense your presence, their ships will start pouring out of this thing.",
        ),
        VoiceLine(
            170,
            Alaric,
            ru="Выход должен находиться рядом, но он был автоматически закрыт после активации Зерна. Чтобы система безопасности разблокировала выход необходимо ликвидировать угрозу в этом зале, то есть уничтожить Зерно и все корабли кочевников. ",
            en="The exit was somewhere around here, but it was automatically sealed after the Seed activated. In order to unseal it, you need to eliminate all the threats:",
        ),
        VoiceLine(
            180,
            Alaric,
            ru="Проблема в том, что если ты сильно нашумишь, наши рейнландские друзья могут перевозбудиться, поэтому действовать надо быстро.",
            en="The only problem is, if you make too much noise, our Rheinland friends will join the party. So, you have to act quickly.",
        ),
        VoiceLine(
            190,
            Trent,
            ru="Черт... Ладно, выключаю невидимость и уничтожаю Зерно.",
            en="Dammit… Alright, powering off cloak and attacking the Seed.",
        ),
        VoiceLine(
            200,
            Alaric,
            ru="Трент, быстрее, рейнландцы почуяли неладное в этом зале, хотят направить к тебе оперативную группу.",
            en="Trent, hurry up! The Rheinlanders are sensing something’s wrong in that hall. They want to send a group of scouts there.",
        ),
        VoiceLine(
            210,
            Trent,
            ru="Охренеть. Это что же за адская машина?",
            en="Holy shit! What the hell is this kind of machine?",
        ),
        VoiceLine(
            220,
            SphereAssistant,
            ru="Финн, срочно летите к лаборатории! Поднимайте тревогу!",
            en="Finn, get to the lab immediately! Sound the alarm!",
        ),
        VoiceLine(
            225,
            Alaric,
            ru="Трент, ну сколько можно возиться? Присоединяйся, щиты уже основательно просели, им осталось недолго.",
            en="Trent, what's taking you so long? Come here, the shields are almost gone - it won't take much longer.",
        ),
        VoiceLine(
            230,
            Alaric,
            ru="Дело в шляпе, уходим.",
            en="It's finished. Let's get out of here.",
        ),
        VoiceLine(
            240,
            HatcherStation,
            ru="Джентльмены, для успешного завершения миссии осталось совсем немного. Линкор Миссури уже рядом со Сферой. Стыкуйтесь быстрее!",
            en="Gentlemen, we're almost done with this mission. Battleship Missouri is approaching the Sphere. Proceed to dock, quickly!",
        ),
        VoiceLine(
            300,
            SphereMissouri,
            ru="Канонерки вышли на огневой рубеж!",
            en="Gunships at the firing range.",
        ),
        VoiceLine(
            310,
            SphereMissouri,
            ru="Внимание, канонерки сделали залп!",
            en="Ready, set... fire!",
        ),
        VoiceLine(
            320,
            HatcherStation,
            ru="Трент, Миссури не может совершить прыжок. Повреждены двигатели, требуется ремонт.",
            en="Trent, Missouri won't be able to jump. Its engines are damaged and need repairs.",
        ),
        VoiceLine(
            330,
            HatcherStation,
            ru="Здесь становится жарко. Вы с должны будете доставить артефакты на нашу базу в Сигма-17 сами. Я выделю вам для прикрытия звено Дельта.",
            en="It's getting hot here. You’ll have to deliver these artifacts to our base in Sigma-17 on your own. The Delta wing will escort you.",
        ),
        VoiceLine(
            340,
            Trent,
            ru="Понял вас, выдвигаюсь. Удачи вам здесь.",
            en="Acknowledged, moving out. Good luck out here.",
        ),
        VoiceLine(
            350,
            HatcherStation,
            ru="Спасибо, Трент. Поверьте, вам она понадобится не меньше.",
            en="Thanks Trent. Trust me, you'll need it more than I do.",
        ),
        VoiceLine(
            360,
            Alaric,
            ru="Трент, я останусь помогу тут.",
            en="Trent, I'm staying here to help.",
        ),
        VoiceLine(
            370,
            Trent,
            ru="И только попробуй мне тут помереть.",
            en="Just try to stay alive, OK?",
        ),
        VoiceLine(
            380,
            DeltaOne,
            ru="Лидер звена Дельта. Даю координаты прыжковой дыры в Сигма-17.",
            en="This is Delta leader; I'm sending you the coordinates for the Sigma-17 jump hole.",
        ),
        VoiceLine(
            390,
            OrderPilot,
            ru="Капитан Сид, цели успешно перехвачены.",
            en="Captain Syd, targets successfully intercepted.",
        ),
        VoiceLine(
            400,
            Ceed,
            ru="Фиксируйте их и доставьте на борт Навуходоносора.",
            en="Freeze them and deliver them to Nebuchadnezzar.",
        ),
        VoiceLine(
            410,
            Trent,
            ru="Теперь бы еще понять где мы.",
            en="Now, where the hell are we?",
        ),
        VoiceLine(
            420,
            DeltaOne,
            ru="Я знаю эту систему. Это Кадиз. Территория Корсаров. Здесь есть свободный порт, куда пускают всех кто смог до него добраться. Называется Фрипорт Тринидад. Там можно будет отсидеться. Вот координаты.",
            en="I know this system. This is Cadiz, in the Corsair territory. There's a Freeport here that allows anyone to dock, it's called Trinidad Freeport. We can wait there. Sending you the coordinates.",
        ),
        VoiceLine(
            430,
            Trent,
            ru="Окей, идем туда.",
            en="Sweet, let's go there.",
        ),
        VoiceLine(
            440,
            DeltaThree,
            ru="Командир, а вы не хотите направиться в более легальное место?",
            en="Hey commander, wouldn't you prefer to fly to a slightly more lawful place?",
        ),
        VoiceLine(
            450,
            DeltaOne,
            ru="В более легальном месте нас тут же возьмут под стражу за утрату артефактов и в лучшем случае обвинят в шпионаже. И хрен вы отмоетесь. ",
            en="In a slightly more lawful place, you'd immediately get apprehended for losing the artifacts. And, in the best case, get accused of espionage. Good luck getting out of prison.",
        ),
        VoiceLine(
            460,
            DeltaOne,
            ru="Улетело пять истребителей с артефактами. Вернулись живые все пятеро, но на одном истребителе и без артефактов. И никто в сказочки с Капитаном Сидом не поверит. Я сам не верил когда однажды задерживал попавших в похожую ситуацию.",
            en="Think of it this way:",
        ),
        VoiceLine(
            470,
            DeltaOne,
            ru="Есть конечно еще один вариант - напасть на этом истребителе на Навуходоносор, победить там всех узнать координаты базы Ордена, захватить ее и уже с артефактами и высоко поднятой головой торжественно вернуться в систему Манхеттен. ",
            en="Of course, there's another option - quickly kill everyone on Nebuchadnezzar, steal the coordinates for their secret base, capture it, and come back to Manhattan. Glorious, victorious, and with artifacts in your hands.",
        ),
        VoiceLine(
            480,
            DeltaOne,
            ru="Как думаете, мистер Трент, ваш истребитель способен на такие боевые действия?",
            en="Mr. Trent, is your ship capable of such aggressive maneuvers?",
        ),
        VoiceLine(
            490,
            Trent,
            ru="Не-а. Сто процентов. К тому же, хочу напомнить, господа, вы сейчас находитесь на моем корабле, а посему полетим мы туда, куда скажу я. И сейчас мы летим на Тринидад.",
            en="Rest assure it cannot. By the way, since you gentlemen are on board my ship, let me remind you that you're going to fly where I say. And right now, we're going to Trinidad.",
        ),
        VoiceLine(
            1010,
            Reitherman,
            ru="Финн, срочно летите на главную базу, у нас несанкционированный доступ!",
            en="Finn, we have a security breach, come to the main base immediately!",
        ),
        VoiceLine(
            1020,
            FinnRunner,
            ru="Неизвестный пилот, внимание, укажите свой идентификационный код.",
            en="Unidentified pilot, please transmit your ID code immediately.",
        ),
        VoiceLine(
            1030,
            FinnRunner,
            ru="Профессор, у нас несанкционированный доступ! Неизвестный корабль не отвечает! Включаю всеобщую тревогу!",
            en="Professor, we have a breach! The unidentified ship isn’t responding! Activating the alarm!",
        ),
        VoiceLine(
            1040,
            FinnRunner,
            ru="Профессор, мой аванпост атакован неизвестным пилотом. Всеобщая тревога!",
            en="Professor, my outpost is being attacked by the unknown vessel. Alarm! Alarm!",
        ),
        VoiceLine(
            1050,
            FinnRunner,
            ru="Профессор, у нас несанкционированный доступ! В вашу зону направляется неизвестный корабль, спасайтесь! ",
            en="Professor, we’re being breached! The unknown ship is headed towards you. You must escape!",
        ),
        VoiceLine(
            1060,
            FinnRunner,
            ru="Двери не работают... Всему персоналу, всеобщая тревога! Несанкционированный доступ!",
            en="Doors are sealed… To all personnel, this is not a drill! We have a security breach! ",
        ),
        VoiceLine(
            1100,
            SphereOutpost,
            ru="Патруль Омега-4, это станция Гамбург. Обнаружены неполадки на одном из телескопов. Осмотр+ите его, возможно разрядился генератор.",
            en="Omega-4 patrol, this is Hamburg station. We found issues on one of the telescopes. Take a look, maybe its battery is low. ",
        ),
        VoiceLine(
            1200,
            Hatcher,
            ru="Мы получили попадание торпедой!",
            en="We’ve been hit by a torpedo!",
        ),
        VoiceLine(
            1210,
            Hatcher,
            ru="Повреждения критические! Миссури срочно требуется поддержка! Всем истребителям, приказ перехватить торпеды!",
            en="Sustained critical damage! Missouri needs immediate assistance! To all fighter wings, your order is to intercept the torpedoes at once!",
        ),
        VoiceLine(
            1220,
            SphereMissouri,
            ru="Канонерки израсходовали боеприпасы и покидают поле битвы. Миссури в безопасности.",
            en="Gunships have exhausted their ammo and are leaving the battlefield. Missouri is safe.",
        ),

    ]


class Mission6(Msn6, script.StoryMission):
    MISSION_INDEX = 6
    CUTSCENES = []
    SPACE_CLASS = Msn6Space
    SYNC_SPACE = True

    MISSION_TITLE = 'Миссия 6. Вход в Сферу'
