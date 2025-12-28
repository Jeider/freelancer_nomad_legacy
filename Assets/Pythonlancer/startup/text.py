class LauncherText:
    STRINGS = [
        ('Freelancer The Nomad Legacy', 'Freelancer Наследие Номадов'),
        ('Show dangerous settings', 'Показать опасные настройки'),
        ('Screen resolution:', 'Разрешение экрана:'),
        ('Windowed mode:', 'Оконный режим:'),
        ('Use dxWrapper:', 'Использовать dxWrapper:'),
        ('Fixes DirectX 8 errors, enables hardware smoothing and filtering', 'Исправляет ошибки DirectX 8, включает фильтрацию и сглаживание'),

        ('Use ReShade:', 'Использовать ReShade:'),
        ('Enables additional post-processed effects, editable right from game. Requires dxwrapper to be active',
         'Включает эффекты пост-процессинга, которые можно настроить прямо в игре. Требует включенного dxwrapper'),
        ('WARNING! Only for fullscreen mode! Because it can broke you mouse crosshair', 'ВНИМАНИЕ! Работает только в полноэкранном режиме, потому что может сломать работу курсора вашей мыши'),

        (
            'This is fan project. You can play it for free. If you want to support the developer, you can send donate or subscribe to project by Boosty.',
            'Вы играете в фанатский проект. Он бесплатный. Но вы можете поддержать проект, отправив донат или подписавшись через Boosty.'
        ),
        ('Support project', 'Поддержать проект'),

        ('Field of view Y (fish eye):', 'Угол обзора по высоте (вкл. рыбий глаз):'),
        ('(default: 70)', '(по умолчанию: 70)'),
        ('Run Freelancer', 'Запустить Freelancer'),

        ('Level of difficulty', 'Уровень сложности'),

        ('Easy', 'Лёгкий'),
        ('Normal', 'Нормальная'),
        ('Hard', 'Тяжелая'),
        ('Extreme', 'Экстремальная'),

        ('Makes game like visual novel with fights. Best for game journalists',
         'Делает игру чем-то вроде визуальной новеллы с боями. Идеально для игровых журналистов'),

        ('More difficult enemies with higher shield and armor. NPC cause more damage on player',
         'Более сложные противники, которые имеют более мощные щиты и броню, а так же наносят игроку больше повреждений'),

        ('Cannot change powerplants and engines', 'Невозможно менять генераторы и двигатели'),
        ('Simple difficulty', 'Простая сложность'),
        ('For game journalists', 'Для игровых журналистов'),
        ('Also you can use it, when you get stuck in mission 6 or mission 9. It changes some game rules and simplify it',
         'Так же вы можете использовать эту сложность, если застряли в некоторых местах миссии 6 и миссии 9. Сложность меняет некоторые правила игры и упрощает их'),

        ('Default difficulty', 'Стандартная сложность'),
        ('Main features are available', 'Доступны все основные возможности игры'),

        ('High difficulty', 'Высокая сложность'),
        ('Can change tractor beam and scanner', 'Можно менять магнитный луч и сканер'),
        ('First tractor beam and scanner are not efficient', 'Первые магнитные лучи и сканеры имеют слабые возможности'),

        ('Extreme challenge for the best freelancers', 'Экстремальное испытание для лучших фрилансеров'),
        ('Minimal drop loot chance', 'Минимальный шанс дропа лута'),


        ('Visual settings', 'Настройки визуала'),
        ('Game settings', 'Настройки игры'),
        ('Ship effects', 'Эффекты корабля'),
        ('Character', 'Персонаж'),

        ('Front-light color', 'Цвет фонаря'),
        ('Contrail color', 'Цвет трассеров'),

        ('White (default)', 'Белый (по умолчанию)'),
        ('Half-Transparent (default)', 'Полупрозрачный (по умолчанию)'),
        ('Green', 'Зелёный'),
        ('Blue', 'Синий'),
        ('Orange', 'Оранжевый'),
        ('Red', 'Красный'),
        ('Yellow', 'Желтый'),
        ('White', 'Белый'),
        ('Purple', 'Фиолетовый'),

        ('Clothes', 'Одежда'),
        ('Hat', 'Шляпа'),
        ('Communication helmet', 'Шлем во время связи'),

        ('Default suit', 'Стандартная одежда'),
        ('None (default)', 'Нет (по умолчанию)'),
        ('Rheinland guard', 'Офицер Рейнланда'),
        ('Rheinland elite', 'Элита Рейнланда'),
        ('Liberty guard', 'Офицер Либерти'),
        ('Liberty elite', 'Элита Либерти'),
        ('Bretonia guard', 'Офицер Бретонии'),
        ('Bretonia elite', 'Элита Бретонии'),
        ('Kusari guard', 'Офицер Кусари'),
        ('Kusari elite', 'Элита Кусари'),
        ('Order suit', 'Одежда Ордена'),
        ('Classic Trent', 'Классический Трент'),
        ('Rheinland', 'Рейнланд'),
        ('Liberty', 'Либерти'),
        ('Bretonia', 'Бретония'),
        ('Kusari', 'Кусари'),

        ('Default helmet', 'Стандартный шлем'),
        ('Brighton\'s helmet', 'Шлем Брайтона'),
        ('Darcy\'s helmet', 'Шлем Дерси'),
        ('Caitlyn\'s helmet', 'Шлем Кейтлин'),
        ('Yamamoto\'s helmet', 'Шлем Ямамото'),
        ('Hatcher\'s helmet', 'Шлем Хетчер'),
        ('Pirate\'s helmet', 'Пиратский шлем'),
        ('Alaric\'s helmet', 'Шлем Аларика'),
        ('Hassler\'s helmet', 'Шлем Хасслера'),
        ('Wilham\'s helmet', 'Шлем Вильгельма'),


    ]

    def __init__(self, russian=True):
        self.russian = russian
        self.ru_strings_per_id = {}
        self.en_strings_per_id = {}

        for en, ru in self.STRINGS:
            self.ru_strings_per_id[en] = ru
            self.en_strings_per_id[en] = en

    def text(self, code):
        if self.russian:
            return self.ru_strings_per_id[code]
        return self.en_strings_per_id[code]
