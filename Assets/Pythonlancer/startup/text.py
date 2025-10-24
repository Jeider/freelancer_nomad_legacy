class LauncherText:
    STRINGS = [
        ('Freelancer The Nomad Legacy', 'Freelancer Наследие Номадов'),
        ('Show dangerous settings', 'Показать опасные настройки'),
        ('Screen resolution:', 'Разрешение экрана:'),
        ('Windowed mode:', 'Оконный режим:'),
        ('Field of view Y (fish eye):', 'Угол обзора по высоте (вкл. рыбий глаз):'),
        ('(default: 70)', '(по умолчанию: 70)'),
        ('Run Freelancer', 'Запустить Freelancer'),

        ('Level of difficulty', 'Уровень сложности'),

        ('Easy', 'Лёгкий'),
        ('Normal', 'Нормальный'),
        ('Hard', 'Тяжелый'),
        ('Extreme', 'Экстремальный'),

        ('Cannot change powerplants and engines', 'Невозможно менять генераторы и двигатели'),
        ('Simple difficulty', 'Простая сложность'),
        ('For game journalists', 'Для игровых журналистов'),

        ('Default difficulty', 'Стандартная сложность'),
        ('Main features is available', 'Доступны все основные возможности игры'),

        ('High difficulty', 'Высокая сложность'),
        ('Can change tractor beam and scanner', 'Можно менять магнитный луч и сканер'),
        ('First tractor beam and scanner are not efficient', 'Первые магнитные лучи и сканеры имеют слабые возможности'),

        ('Extreme challenge for the best freelancers', 'Экстремальное испытание для лучших фрилансеров'),
        ('Minimal drop loot chance', 'Минимальный шанс дропа лута'),

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
