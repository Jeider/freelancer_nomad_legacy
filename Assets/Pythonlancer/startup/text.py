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
        ('Normal', 'Нормальной'),
        ('Hard', 'Сложный'),
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
