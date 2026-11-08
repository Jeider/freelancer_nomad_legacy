from text.strings import MultiString as MS

RETURN_NAMES = [
    "г. МакКинли ",
    "Скалистые",
    "Аппалачи",
    "Миссури",
    "Миссисипи",
    "Колорадо",
    "Великие Озера",
    "о. Кичоби",
    "г. Витни",
    "Долина Смерти",
    "Рио-Гранде",
    "Арканзас",
    "Бразос",
    "Колумбия",
    "Пекос",
    "Платт",
    "р. Красная",
    "Сан-Жоаквин",
    "Река Змейка",
    "Вобош ",
    "Йеллоустоун",
    "Гила",
    "Чаттахучи",
    "Канадский",
    "Иллинойс",
    "Сусьюханна",
    "Теннесси",
    "Огайо",
    "Великий Каньон",
    "о. Онтарио",
    "о. Соленое",
    "о. Эри",
    "Озеро Верхнее",
    "Озеро Гурон",
    "Озеро Мичиган",
    "Пик Пайка",
    "Гора Рушмор",
    "Гора Уилсон",
    "Гора Паломар",
    "Гора Св. Елены",
    "Остин",
    "Амарильо",
    "Абилен",
    "Даллас",
    "Эль-Пасо",
    "Сан-Антонио",
    "Александрия",
    "Лафайет",
    "Батон-Руж",
    "Новый Орлеан",
    "Албани",
    "Дюрхем",
    "Рочестер",
    "Пауфкипси",
    "Сиракузы",
    "Уотертаун",
    "Фрешно",
    "Окленд",
    "Сакраменто",
    "Сан-Франциско",
    "Сан-Хосе",
    "Дюранго",
    "Стерлинг",
    "Анхораж",
    "Фэрбенкс",
    "Джуно",
    "Кадьяк",
    "Ном",
    "Сьюард",
    "Винстон Салем",
    "Конкорд",
    "Шарлотта",
    "Роли",
    "Джэксонвилл",
    "Риф Ларго",
    "Западный  риф",
    "Киссими",
    "Майами",
    "Орландо",
    "Таллахаси",
    "Тампо",
    "Бостон",
    "Кембридж",
    "Лексингтон",
    "Провиденс",
    "Глендейл",
    "Джеймстаун",
    "Биллингс",
    "Бойсе",
    "Абердин",
    "Аннаполис",
    "Сиэтл",
    "Спокан",
    "Тахома",
    "Редмонд",
    "Портленд",
    "Мэдисон",
    "Милуоки",
    "Акрон",
    "Кливленд",
    "Гибралтар",
    "Шевиот",
    "Пенины",
    "Темза",
    "Хирдон Берн",
    "Тэйн",
    "Кэмел",
    "Гретта",
    "Тисс",
    "Край",
    "Минт",
    "Кент",
    "Траутбэк",
    "Тейв",
    "Твоч",
    "Стенли",
    "Тим",
    "Гаур",
    "Лохей",
    "Tay",
    "Гарб Гайор",
    "Браан",
    "Кинлас",
    "Твид",
    "Тайн",
    "Вайтаддер",
    "Гойт",
    "Эден",
    "Эйвон",
    "Блэквотер",
    "Торридж",
    "Кряж Англетарна",
    "Болото Блуберри",
    "Бли Ригг",
    "Биркхаус Мур",
    "Гибсон Нотт",
    "Гленридинг Додд",
    "Грасмур",
    "Нотбери",
    "Инглборо",
    "Белфаст",
    "Ноттингем",
    "Глазго",
    "Данди",
    "Плимут",
    "Сандерленд",
    "Блэкберн",
    "Бристоль",
    "Ливерпуль",
    "Флитвуд",
    "Дерби",
    "Оксфорд",
    "Салисбари",
    "Брайтон",
    "Кроули",
    "Глочестер",
    "Лютон",
    "Истбор",
    "Бирмингем",
    "Дамфри",
    "Близ",
    "Гленрот",
    "Шака Бра",
    "Дафтаун",
    "Калландер",
    "Брей",
    "Обан",
    "Маллайг",
    "Авимур",
    "Инвернесс",
    "Наас",
    "Лонгфорд",
    "Кастлбар",
    "Лофри",
    "Лимерик",
    "Гленгарифф",
    "Тюрле",
    "Лисберн",
    "Кардифф",
    "Монтгомери",
    "Херефорд",
    "Мертир Титфил",
    "Ньюпорт",
    "Суонси",
    "Саутгемптон",
    "Андовер",
    "Кантербери",
    "Эшфорд",
    "Фолкстон",
    "Ипсвич",
    "Шаффрон",
    "Хантингдон",
    "Ширнис",
    "Норвич",
    "Скарборо",
    "Перт",
    "Крифф",
    "Лочинвер",
    "Дюрнесс",
    "Стромнесс",
    "Фудзияма",
    "Кусиро",
    "Нагара",
    "Нара Иошино",
    "Симанто",
    "Иошино",
    "Нисики",
    "Бива",
    "Хируга",
    "Осако",
    "Иансе",
    "Оно",
    "Джинзай",
    "Фатацуно",
    "Иого",
    "Сакамото",
    "Казайа",
    "Шингу",
    "Шинджи",
    "Миката-Гоко",
    "Джизо Гатаке",
    "Каннот Иет-Даке",
    "Кита-Даке",
    "Осава-Даке",
    "Ока-Хиджири",
    "Камикучи-Даке",
    "Чаусу-Даке",
    "Акайши-Даке",
    "Сенмай-Даке",
    "Раусу",
    "Кинпу-Сан",
    "Асаки-Даке",
    "Танзава",
    "Сенджо-Даке",
    "Ниши-Нутори-Даке",
    "Шиоми-Даке",
    "Кай Кома-Га-Тaкe",
    "Пролив Иашаджин",
    "Иру-Даке",
    "Текари-Даке",
    "Чиба",
    "Фудзиошида",
    "Фукай",
    "Фукуока",
    "Фушики",
    "Гамагори",
    "Хашинох",
    "Хакодате",
    "Хигашикава",
    "Химеджи",
    "Какогава",
    "Камакура",
    "Карийа",
    "Кисаразу",
    "Китакушу",
    "Кобе",
    "Куре",
    "Киото",
    "Муцу",
    "Нагойа",
    "Намерикава",
    "Нара",
    "Оита",
    "Окинава",
    "Осака",
    "Сагамихара",
    "Саганосеки",
    "Сакаи",
    "Саката",
    "Саппоро",
    "Шига",
    "Такамацу",
    "Токушима",
    "Тоттори",
    "Цуиама",
    "Урава",
    "Вакайама",
    "Иокогама",
    "Иокосука",
    "Ассабу",
    "Сетана",
    "Румой",
    "Отару",
    "Тойокоро",
    "Обихиро",
    "Накаджима",
    "Шио",
    "Каназава",
    "Иаманака",
    "Иида",
    "Хакуба",
    "Иеда",
    "Шиоджири",
    "Дайто",
    "Ито",
    "Шизуока",
    "Фукушима",
    "Отама",
    "Нихонмацу",
    "Иамацури",
    "Мур",
    "Эльбе",
    "Эмс",
    "Альстерфлит",
    "Райн",
    "Вессер",
    "Загспиц",
    "Шварцвальд",
    "Воцманн",
    "Гроссглокнер",
    "Гроссвендигер",
    "Харз",
    "Хура",
    "Ветерштайнгебирг",
    "Эрцгебирг",
    "Хоген Таерн",
    "Некар",
    "Одер",
    "Саал",
    "Боденси",
    "Мюриц",
    "Шверинер",
    "Старнбергер",
    "Чимси",
    "Тироль",
    "Тофана",
    "Ахр",
    "Нах",
    "Саар",
    "Мозель",
    "Рувер",
    "Зольканал",
    "Балтик",
    "Ользетт",
    "Петруссе",
    "Спри",
    "Ландворканал",
    "Брукторхафен",
    "Нордеркайбе",
    "Обехафен",
    "Блоберен",
    "Хайдельберг",
    "Карлзрух",
    "Ульм",
    "Бремен",
    "Бремерхэвен",
    "Ансбах",
    "Бамберг",
    "Эрдинг",
    "Фризинг",
    "Графенвур",
    "Ингольштадт",
    "Ландшат",
    "Мюнхен",
    "Пассо",
    "Роттенбург",
    "Швондорф",
    "Виден",
    "Гельнхаусен",
    "Ханау",
    "Оффенбах",
    "Росток",
    "Бюргдорф",
    "Эмден",
    "Гарбсен",
    "Гамельн",
    "Ганновер",
    "Норденхэм",
    "Оснабрюкер",
    "Паттенсен",
    "Спринг",
    "Вильхельмшейвен",
    "Вольфенбуттен",
    "Бирхим",
    "Бонн",
    "Дортмунд",
    "Доссельдорф",
    "Кельн",
    "Липпштадт",
    "Духротт",
    "Мейнц",
    "Триэр",
    "Лейпциг",
    "Риса",
    "Аренсбургер",
    "Любек",
    "Рендсбург",
    "Соннеберг",
    "Вимар",
    "Визбаден",
    "Мюнхен",
    "Киель",
    "Постдам",
    "Магдебург",
    "Эрфурт",
    "Майнинген",
    "Саарбрюкен",
    "Варен",
    "Шенебек",
    "Верден",
]


class Static:
    def __init__(self, ids, ru_name):
        self.ids = ids
        self.ru_name = ru_name


STATIC_NAMES = [
    # Port UI: HUD and preferences. MS(Russian, English); keep numeric IDs stable.
    Static(238400, MS('Цветокоррекция', 'Color grading')),  # ColorGradeLabel
    Static(238401, MS('Естественный', 'Natural')),  # ColorGradeNatural
    Static(238402, MS('Тёплый', 'Warm')),  # ColorGradeWarm
    Static(238403, MS('Холодный', 'Cool')),  # ColorGradeCool
    Static(238404, MS('Цвет и DLSS — сразу; прочие настройки — после перезапуска', 'Color and DLSS apply immediately; other settings require a restart')),  # ColorGradeHint
    Static(238405, MS('Включить DLSS 5', 'Enable DLSS 5')),  # NeuralEnabled

    # Port UI: HUD and preferences. MS(Russian, English); keep numeric IDs stable.
    Static(238267, MS('Сила DLSS 5', 'DLSS 5 strength')),  # NeuralStrength
    Static(238268, MS('DLSS 5 — сразу; прочие настройки — после перезапуска', 'DLSS 5 applies immediately; other settings require a restart')),  # NeuralStrengthHint

    Static(238391, MS('Парковка', 'Parking')),  # Parking service
    Static(238289, MS('Грузовые перевозки', 'Freight Transport')),  # TrainCourier mission_title
    Static(238290, MS('Грузовой состав', 'Freight Train')),  # TrainCourier cargo_name
    Static(238390, MS('Смотритель стоянки', 'Parking manager')),  # Ship parking
    Static(238288, MS('<?xml version="1.0" encoding="UTF-16"?><RDL><PUSH/><TRA bold="true"/><TEXT>Груз: </TEXT><TRA bold="false"/><TEXT>%s0</TEXT><PARA/><TRA bold="true"/><TEXT>Отправитель: </TEXT><TRA bold="false"/><TEXT>%s1</TEXT><PARA/><TRA bold="true"/><TEXT>Получатель: </TEXT><TRA bold="false"/><TEXT>%s2</TEXT><PARA/><TRA bold="true"/><TEXT>Целевая система: </TEXT><TRA bold="false"/><TEXT>%s3</TEXT><PARA/><PARA/><TEXT>%!0</TEXT><PARA/><PARA/><TRA bold="true"/><TEXT>Состав: </TEXT><TRA bold="false"/><TEXT>%d0 вагонов · %d1 ед. груза</TEXT><PARA/><TRA bold="true"/><TEXT>Маршрут: </TEXT><TRA bold="false"/><TEXT>%d2 участков</TEXT><PARA/><TRA bold="true"/><TEXT>Награда: </TEXT><TRA bold="false"/><TEXT>%d3 кр.</TEXT><PARA/><TRA bold="true"/><TEXT>Утрачено контейнеров: </TEXT><TRA bold="false"/><TEXT>%d5</TEXT><PARA/><TRA bold="true"/><TEXT>К выплате: </TEXT><TRA bold="false"/><TEXT>%d6 кр.</TEXT><PARA/><TRA bold="true"/><TEXT>Удержание за контейнер: </TEXT><TRA bold="false"/><TEXT>%d4 кр., суммарно не больше награды</TEXT><PARA/><TRA bold="true"/><TEXT>Ожидаемое время: </TEXT><TRA bold="false"/><TEXT>%d7 мин.</TEXT><PARA/><TRA bold="true"/><TEXT>Открытый максимум: </TEXT><TRA bold="false"/><TEXT>%d8 вагонов · %d9 ед. груза</TEXT><PARA/><PARA/><TEXT>Таймер запускается при первом сцеплении. Опоздание не отменяет заказ и не уменьшает оплату.</TEXT><PARA/><PARA/><TEXT>Подцепите состав у отправителя, доставьте груз получателю и отцепите вагоны в отмеченной точке.</TEXT><POP/></RDL>', '<?xml version="1.0" encoding="UTF-16"?><RDL><PUSH/><TRA bold="true"/><TEXT>Cargo: </TEXT><TRA bold="false"/><TEXT>%s0</TEXT><PARA/><TRA bold="true"/><TEXT>Shipper: </TEXT><TRA bold="false"/><TEXT>%s1</TEXT><PARA/><TRA bold="true"/><TEXT>Receiver: </TEXT><TRA bold="false"/><TEXT>%s2</TEXT><PARA/><TRA bold="true"/><TEXT>Destination system: </TEXT><TRA bold="false"/><TEXT>%s3</TEXT><PARA/><PARA/><TEXT>%!0</TEXT><PARA/><PARA/><TRA bold="true"/><TEXT>Train: </TEXT><TRA bold="false"/><TEXT>%d0 wagons · %d1 cargo units</TEXT><PARA/><TRA bold="true"/><TEXT>Route: </TEXT><TRA bold="false"/><TEXT>%d2 legs</TEXT><PARA/><TRA bold="true"/><TEXT>Reward: </TEXT><TRA bold="false"/><TEXT>%d3 credits</TEXT><PARA/><TRA bold="true"/><TEXT>Containers lost: </TEXT><TRA bold="false"/><TEXT>%d5</TEXT><PARA/><TRA bold="true"/><TEXT>Payment due: </TEXT><TRA bold="false"/><TEXT>%d6 credits</TEXT><PARA/><TRA bold="true"/><TEXT>Deduction per container: </TEXT><TRA bold="false"/><TEXT>%d4 credits, total capped at the reward</TEXT><PARA/><TRA bold="true"/><TEXT>Expected in: </TEXT><TRA bold="false"/><TEXT>%d7 minutes</TEXT><PARA/><TRA bold="true"/><TEXT>Unlocked capacity: </TEXT><TRA bold="false"/><TEXT>%d8 wagons · %d9 cargo units</TEXT><PARA/><PARA/><TEXT>The timer starts when you first couple the train. Late arrival does not cancel the order or reduce payment.</TEXT><PARA/><PARA/><TEXT>Collect the train at the shipper, deliver the cargo to the receiver, and uncouple at the marked point.</TEXT><POP/></RDL>')),  # TrainCourier description_capacity
    Static(238287, MS('Следуйте к точке %s0 за назначенным составом и подцепите его.', 'Proceed to %s0 to collect and couple the assigned train.')),  # TrainCourier pickup_from
    Static(238283, MS('<?xml version="1.0" encoding="UTF-16"?><RDL><PUSH/><TRA bold="true"/><TEXT>Груз: </TEXT><TRA bold="false"/><TEXT>%s0</TEXT><PARA/><TRA bold="true"/><TEXT>Отправитель: </TEXT><TRA bold="false"/><TEXT>%s1</TEXT><PARA/><TRA bold="true"/><TEXT>Получатель: </TEXT><TRA bold="false"/><TEXT>%s2</TEXT><PARA/><TRA bold="true"/><TEXT>Целевая система: </TEXT><TRA bold="false"/><TEXT>%s3</TEXT><PARA/><PARA/><TEXT>%!0</TEXT><PARA/><PARA/><TRA bold="true"/><TEXT>Состав: </TEXT><TRA bold="false"/><TEXT>%d0 вагонов · %d1 ед. груза</TEXT><PARA/><TRA bold="true"/><TEXT>Маршрут: </TEXT><TRA bold="false"/><TEXT>%d2 участков</TEXT><PARA/><TRA bold="true"/><TEXT>Награда: </TEXT><TRA bold="false"/><TEXT>%d3 кр.</TEXT><PARA/><TRA bold="true"/><TEXT>Утрачено контейнеров: </TEXT><TRA bold="false"/><TEXT>%d5</TEXT><PARA/><TRA bold="true"/><TEXT>К выплате: </TEXT><TRA bold="false"/><TEXT>%d6 кр.</TEXT><PARA/><TRA bold="true"/><TEXT>Удержание за контейнер: </TEXT><TRA bold="false"/><TEXT>%d4 кр., суммарно не больше награды</TEXT><PARA/><TRA bold="true"/><TEXT>Ожидаемое время: </TEXT><TRA bold="false"/><TEXT>%d7 мин.</TEXT><PARA/><PARA/><TEXT>Таймер запускается при первом сцеплении. Опоздание не отменяет заказ и не уменьшает оплату.</TEXT><PARA/><PARA/><TEXT>Подцепите состав у отправителя, доставьте груз получателю и отцепите вагоны в отмеченной точке.</TEXT><POP/></RDL>', '<?xml version="1.0" encoding="UTF-16"?><RDL><PUSH/><TRA bold="true"/><TEXT>Cargo: </TEXT><TRA bold="false"/><TEXT>%s0</TEXT><PARA/><TRA bold="true"/><TEXT>Shipper: </TEXT><TRA bold="false"/><TEXT>%s1</TEXT><PARA/><TRA bold="true"/><TEXT>Receiver: </TEXT><TRA bold="false"/><TEXT>%s2</TEXT><PARA/><TRA bold="true"/><TEXT>Destination system: </TEXT><TRA bold="false"/><TEXT>%s3</TEXT><PARA/><PARA/><TEXT>%!0</TEXT><PARA/><PARA/><TRA bold="true"/><TEXT>Train: </TEXT><TRA bold="false"/><TEXT>%d0 wagons · %d1 cargo units</TEXT><PARA/><TRA bold="true"/><TEXT>Route: </TEXT><TRA bold="false"/><TEXT>%d2 legs</TEXT><PARA/><TRA bold="true"/><TEXT>Reward: </TEXT><TRA bold="false"/><TEXT>%d3 credits</TEXT><PARA/><TRA bold="true"/><TEXT>Containers lost: </TEXT><TRA bold="false"/><TEXT>%d5</TEXT><PARA/><TRA bold="true"/><TEXT>Payment due: </TEXT><TRA bold="false"/><TEXT>%d6 credits</TEXT><PARA/><TRA bold="true"/><TEXT>Deduction per container: </TEXT><TRA bold="false"/><TEXT>%d4 credits, total capped at the reward</TEXT><PARA/><TRA bold="true"/><TEXT>Expected in: </TEXT><TRA bold="false"/><TEXT>%d7 minutes</TEXT><PARA/><PARA/><TEXT>The timer starts when you first couple the train. Late arrival does not cancel the order or reduce payment.</TEXT><PARA/><PARA/><TEXT>Collect the train at the shipper, deliver the cargo to the receiver, and uncouple at the marked point.</TEXT><POP/></RDL>')),  # TrainCourier description
    Static(238284, MS('Груз ждут через', 'Cargo expected in')),  # TrainCourier timer
    Static(238285, MS('Груз всё ещё ждут · +', 'Cargo still awaited · +')),  # TrainCourier overdue
    Static(238286, MS('Груз утрачен: контейнеров %d0. К выплате: %d1 кр.', 'Cargo lost: %d0 containers. Payment due: %d1 credits.')),  # TrainCourier loss
    Static(238500, MS('Привезите груз к точке %s0: цех изготавливает простые крепления и конструкционные детали. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a workshop is making basic brackets and structural parts. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_alloy_basic_01
    Static(238501, MS('Привезите груз к точке %s0: производственная линия пополняет запас базового сплава. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a production line is replenishing its basic-alloy stock. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_alloy_basic_02
    Static(238502, MS('Привезите груз к точке %s0: монтажникам нужны заготовки для ненагруженных конструкций. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: assembly crews need stock for lightly loaded structures. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_alloy_basic_03
    Static(238503, MS('Привезите груз к точке %s0: ремонтные мастерские готовят партию обычных металлических деталей. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: repair shops are preparing a batch of standard metal parts. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_alloy_basic_04
    Static(238504, MS('Привезите груз к точке %s0: участок сборки закладывает запас металла для следующей серии. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the assembly section is stocking metal for its next production run. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_alloy_basic_05
    Static(238505, MS('Пункт назначения — %s0. Здесь цех изготавливает простые крепления и конструкционные детали. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a workshop is making basic brackets and structural parts. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_alloy_basic_06
    Static(238506, MS('Пункт назначения — %s0. Здесь производственная линия пополняет запас базового сплава. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a production line is replenishing its basic-alloy stock. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_alloy_basic_07
    Static(238507, MS('Пункт назначения — %s0. Здесь монтажникам нужны заготовки для ненагруженных конструкций. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, assembly crews need stock for lightly loaded structures. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_alloy_basic_08
    Static(238508, MS('Пункт назначения — %s0. Здесь ремонтные мастерские готовят партию обычных металлических деталей. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, repair shops are preparing a batch of standard metal parts. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_alloy_basic_09
    Static(238509, MS('Пункт назначения — %s0. Здесь участок сборки закладывает запас металла для следующей серии. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the assembly section is stocking metal for its next production run. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_alloy_basic_10
    Static(238510, MS('Привезите груз к точке %s0: электромонтажный цех готовит новые силовые кабели. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the electrical workshop is preparing new power cables. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_alloy_conductor_01
    Static(238511, MS('Привезите груз к точке %s0: сборщикам нужна партия сверхпроводящего сплава для проводки. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: assemblers need superconducting alloy for wiring. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_alloy_conductor_02
    Static(238512, MS('Привезите груз к точке %s0: инженеры заменяют изношенные силовые шины. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: engineers are replacing worn power busbars. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_alloy_conductor_03
    Static(238513, MS('Привезите груз к точке %s0: производство электрических узлов пополняет запас проводников. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: electrical-component production is replenishing conductor stocks. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_alloy_conductor_04
    Static(238514, MS('Привезите груз к точке %s0: новые энергетические модули ждут кабельную разводку. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: new power modules await their cabling. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_alloy_conductor_05
    Static(238515, MS('Пункт назначения — %s0. Здесь электромонтажный цех готовит новые силовые кабели. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the electrical workshop is preparing new power cables. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_alloy_conductor_06
    Static(238516, MS('Пункт назначения — %s0. Здесь сборщикам нужна партия сверхпроводящего сплава для проводки. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, assemblers need superconducting alloy for wiring. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_alloy_conductor_07
    Static(238517, MS('Пункт назначения — %s0. Здесь инженеры заменяют изношенные силовые шины. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, engineers are replacing worn power busbars. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_alloy_conductor_08
    Static(238518, MS('Пункт назначения — %s0. Здесь производство электрических узлов пополняет запас проводников. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, electrical-component production is replenishing conductor stocks. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_alloy_conductor_09
    Static(238519, MS('Пункт назначения — %s0. Здесь новые энергетические модули ждут кабельную разводку. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, new power modules await their cabling. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_alloy_conductor_10
    Static(238520, MS('Привезите груз к точке %s0: сборочный цех готовит силовой каркас. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the assembly shop is preparing a load-bearing frame. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_alloy_heavy_01
    Static(238521, MS('Привезите груз к точке %s0: ремонтники заменяют наиболее нагруженные конструкционные элементы. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: repair crews are replacing heavily loaded structural members. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_alloy_heavy_02
    Static(238522, MS('Привезите груз к точке %s0: производство корпусов требует высокопрочного сплава. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: hull production requires high-strength alloy. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_alloy_heavy_03
    Static(238523, MS('Привезите груз к точке %s0: инженеры усиливают ответственные узлы конструкции. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: engineers are reinforcing critical structural joints. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_alloy_heavy_04
    Static(238524, MS('Привезите груз к точке %s0: новая серия каркасных деталей ждёт металл. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a new run of frame components awaits its metal supply. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_alloy_heavy_05
    Static(238525, MS('Пункт назначения — %s0. Здесь сборочный цех готовит силовой каркас. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the assembly shop is preparing a load-bearing frame. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_alloy_heavy_06
    Static(238526, MS('Пункт назначения — %s0. Здесь ремонтники заменяют наиболее нагруженные конструкционные элементы. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, repair crews are replacing heavily loaded structural members. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_alloy_heavy_07
    Static(238527, MS('Пункт назначения — %s0. Здесь производство корпусов требует высокопрочного сплава. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, hull production requires high-strength alloy. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_alloy_heavy_08
    Static(238528, MS('Пункт назначения — %s0. Здесь инженеры усиливают ответственные узлы конструкции. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, engineers are reinforcing critical structural joints. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_alloy_heavy_09
    Static(238529, MS('Пункт назначения — %s0. Здесь новая серия каркасных деталей ждёт металл. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a new run of frame components awaits its metal supply. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_alloy_heavy_10
    Static(238530, MS('Привезите груз к точке %s0: реакторный цех собирает защитные экраны. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the reactor workshop is assembling radiation shields. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_alloy_radiation_01
    Static(238531, MS('Привезите груз к точке %s0: инженеры обновляют радиационную защиту технических отсеков. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: engineers are renewing radiation protection in technical compartments. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_alloy_radiation_02
    Static(238532, MS('Привезите груз к точке %s0: сборка энергетических установок требует защитного сплава. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: power-plant assembly requires radiation-resistant alloy. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_alloy_radiation_03
    Static(238533, MS('Привезите груз к точке %s0: защитные кожухи реакторов готовят к замене. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: reactor shielding casings are due for replacement. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_alloy_radiation_04
    Static(238534, MS('Привезите груз к точке %s0: монтажники изолируют жилые помещения от источников излучения. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: assembly crews are shielding living quarters from radiation sources. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_alloy_radiation_05
    Static(238535, MS('Пункт назначения — %s0. Здесь реакторный цех собирает защитные экраны. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the reactor workshop is assembling radiation shields. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_alloy_radiation_06
    Static(238536, MS('Пункт назначения — %s0. Здесь инженеры обновляют радиационную защиту технических отсеков. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, engineers are renewing radiation protection in technical compartments. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_alloy_radiation_07
    Static(238537, MS('Пункт назначения — %s0. Здесь сборка энергетических установок требует защитного сплава. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, power-plant assembly requires radiation-resistant alloy. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_alloy_radiation_08
    Static(238538, MS('Пункт назначения — %s0. Здесь защитные кожухи реакторов готовят к замене. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, reactor shielding casings are due for replacement. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_alloy_radiation_09
    Static(238539, MS('Пункт назначения — %s0. Здесь монтажники изолируют жилые помещения от источников излучения. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, assembly crews are shielding living quarters from radiation sources. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_alloy_radiation_10
    Static(238540, MS('Привезите груз к точке %s0: цех двигателей готовит жаропрочные детали. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the engine workshop is preparing heat-resistant parts. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_alloy_temperature_01
    Static(238541, MS('Привезите груз к точке %s0: инженеры заменяют элементы, работающие при высокой температуре. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: engineers are replacing components exposed to high temperatures. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_alloy_temperature_02
    Static(238542, MS('Привезите груз к точке %s0: производственная линия собирает термостойкие узлы. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a production line is assembling heat-resistant units. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_alloy_temperature_03
    Static(238543, MS('Привезите груз к точке %s0: ремонтникам нужны заготовки для горячих секций двигателей. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: repair crews need stock for engine hot sections. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_alloy_temperature_04
    Static(238544, MS('Привезите груз к точке %s0: новая серия тепловых экранов ждёт специальный сплав. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a new batch of heat shields awaits its specialist alloy. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_alloy_temperature_05
    Static(238545, MS('Пункт назначения — %s0. Здесь цех двигателей готовит жаропрочные детали. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the engine workshop is preparing heat-resistant parts. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_alloy_temperature_06
    Static(238546, MS('Пункт назначения — %s0. Здесь инженеры заменяют элементы, работающие при высокой температуре. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, engineers are replacing components exposed to high temperatures. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_alloy_temperature_07
    Static(238547, MS('Пункт назначения — %s0. Здесь производственная линия собирает термостойкие узлы. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a production line is assembling heat-resistant units. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_alloy_temperature_08
    Static(238548, MS('Пункт назначения — %s0. Здесь ремонтникам нужны заготовки для горячих секций двигателей. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, repair crews need stock for engine hot sections. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_alloy_temperature_09
    Static(238549, MS('Пункт назначения — %s0. Здесь новая серия тепловых экранов ждёт специальный сплав. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a new batch of heat shields awaits its specialist alloy. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_alloy_temperature_10
    Static(238550, MS('Привезите груз к точке %s0: жилой сектор получает новую партию одежды и бытовых принадлежностей. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the residential sector is receiving clothing and household supplies. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_consumer_01
    Static(238551, MS('Привезите груз к точке %s0: снабженцы комплектуют комнаты для новых работников. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: supply crews are furnishing rooms for new workers. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_consumer_02
    Static(238552, MS('Привезите груз к точке %s0: изношенную бытовую технику пора заменить. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: worn household appliances are due for replacement. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_consumer_03
    Static(238553, MS('Привезите груз к точке %s0: магазины пополняют запас повседневных товаров. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: shops are replenishing everyday goods. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_consumer_04
    Static(238554, MS('Привезите груз к точке %s0: после ремонта жилых помещений требуется бытовое оснащение. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: refurbished living quarters need household equipment. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_consumer_05
    Static(238555, MS('Пункт назначения — %s0. Здесь жилой сектор получает новую партию одежды и бытовых принадлежностей. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the residential sector is receiving clothing and household supplies. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_consumer_06
    Static(238556, MS('Пункт назначения — %s0. Здесь снабженцы комплектуют комнаты для новых работников. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, supply crews are furnishing rooms for new workers. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_consumer_07
    Static(238557, MS('Пункт назначения — %s0. Здесь изношенную бытовую технику пора заменить. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, worn household appliances are due for replacement. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_consumer_08
    Static(238558, MS('Пункт назначения — %s0. Здесь магазины пополняют запас повседневных товаров. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, shops are replenishing everyday goods. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_consumer_09
    Static(238559, MS('Пункт назначения — %s0. Здесь после ремонта жилых помещений требуется бытовое оснащение. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, refurbished living quarters need household equipment. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_consumer_10
    Static(238560, MS('Привезите груз к точке %s0: столовая пополняет запас синтетических рационов для рабочих смен. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the canteen is replenishing synthetic rations for its work shifts. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_food_01
    Static(238561, MS('Привезите груз к точке %s0: жилой сектор принимает новую группу работников. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the residential sector is receiving a new group of workers. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_food_02
    Static(238562, MS('Привезите груз к точке %s0: кладовые должны обеспечить питание экипажей на длительных дежурствах. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the stores must feed crews assigned to extended duty. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_food_03
    Static(238563, MS('Привезите груз к точке %s0: служба снабжения обновляет продовольственный резерв. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the supply office is renewing its food reserve. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_food_04
    Static(238564, MS('Привезите груз к точке %s0: поставку рационов ждут перед началом большого ремонта. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a ration shipment is expected before a major maintenance operation. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_food_05
    Static(238565, MS('Пункт назначения — %s0. Здесь столовая пополняет запас синтетических рационов для рабочих смен. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the canteen is replenishing synthetic rations for its work shifts. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_food_06
    Static(238566, MS('Пункт назначения — %s0. Здесь жилой сектор принимает новую группу работников. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the residential sector is receiving a new group of workers. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_food_07
    Static(238567, MS('Пункт назначения — %s0. Здесь кладовые должны обеспечить питание экипажей на длительных дежурствах. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the stores must feed crews assigned to extended duty. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_food_08
    Static(238568, MS('Пункт назначения — %s0. Здесь служба снабжения обновляет продовольственный резерв. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the supply office is renewing its food reserve. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_food_09
    Static(238569, MS('Пункт назначения — %s0. Здесь поставку рационов ждут перед началом большого ремонта. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a ration shipment is expected before a major maintenance operation. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_food_10
    Static(238570, MS('Привезите груз к точке %s0: медпункт пополняет запас перевязочных материалов после тяжёлой смены. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the medical bay is replenishing dressings after a difficult shift. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_meds_01
    Static(238571, MS('Привезите груз к точке %s0: врачи готовят запас лекарств для прибывающих рабочих. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: doctors are preparing medicines for incoming workers. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_meds_02
    Static(238572, MS('Привезите груз к точке %s0: хирургическому отделению нужны стерильные медицинские наборы. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the surgical ward needs sterile medical kits. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_meds_03
    Static(238573, MS('Привезите груз к точке %s0: выездные медицинские бригады комплектуют аптечки. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: mobile medical teams are stocking their first-aid kits. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_meds_04
    Static(238574, MS('Привезите груз к точке %s0: аптека должна восстановить резерв препаратов для длительного лечения. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the pharmacy must restore its reserve of medicines for long-term treatment. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_meds_05
    Static(238575, MS('Пункт назначения — %s0. Здесь медпункт пополняет запас перевязочных материалов после тяжёлой смены. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the medical bay is replenishing dressings after a difficult shift. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_meds_06
    Static(238576, MS('Пункт назначения — %s0. Здесь врачи готовят запас лекарств для прибывающих рабочих. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, doctors are preparing medicines for incoming workers. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_meds_07
    Static(238577, MS('Пункт назначения — %s0. Здесь хирургическому отделению нужны стерильные медицинские наборы. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the surgical ward needs sterile medical kits. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_meds_08
    Static(238578, MS('Пункт назначения — %s0. Здесь выездные медицинские бригады комплектуют аптечки. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, mobile medical teams are stocking their first-aid kits. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_meds_09
    Static(238579, MS('Пункт назначения — %s0. Здесь аптека должна восстановить резерв препаратов для длительного лечения. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the pharmacy must restore its reserve of medicines for long-term treatment. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_meds_10
    Static(238580, MS('Привезите груз к точке %s0: служба жизнеобеспечения пополняет кислородный резерв. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: life support is replenishing its oxygen reserve. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_oxygen_01
    Static(238581, MS('Привезите груз к точке %s0: герметичные жилые отсеки готовят к заселению. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: sealed residential compartments are being prepared for occupancy. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_oxygen_02
    Static(238582, MS('Привезите груз к точке %s0: после обслуживания воздушного контура требуется запас кислорода. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: oxygen stocks are needed after servicing the air circulation system. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_oxygen_03
    Static(238583, MS('Привезите груз к точке %s0: инженеры готовят резерв на время ремонта генераторов воздуха. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: engineers are stocking a reserve while air generators undergo repairs. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_oxygen_04
    Static(238584, MS('Привезите груз к точке %s0: дополнительная рабочая смена увеличила расход кислорода. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: an additional work shift has increased oxygen consumption. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_oxygen_05
    Static(238585, MS('Пункт назначения — %s0. Здесь служба жизнеобеспечения пополняет кислородный резерв. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, life support is replenishing its oxygen reserve. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_oxygen_06
    Static(238586, MS('Пункт назначения — %s0. Здесь герметичные жилые отсеки готовят к заселению. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, sealed residential compartments are being prepared for occupancy. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_oxygen_07
    Static(238587, MS('Пункт назначения — %s0. Здесь после обслуживания воздушного контура требуется запас кислорода. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, oxygen stocks are needed after servicing the air circulation system. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_oxygen_08
    Static(238588, MS('Пункт назначения — %s0. Здесь инженеры готовят резерв на время ремонта генераторов воздуха. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, engineers are stocking a reserve while air generators undergo repairs. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_oxygen_09
    Static(238589, MS('Пункт назначения — %s0. Здесь дополнительная рабочая смена увеличила расход кислорода. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, an additional work shift has increased oxygen consumption. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_oxygen_10
    Static(238590, MS('Привезите груз к точке %s0: участок утилизации принимает отходы реакторных установок. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the disposal facility is accepting reactor waste. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_toxic_01
    Static(238591, MS('Привезите груз к точке %s0: накопившиеся токсичные отходы отправляют на безопасную переработку. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: accumulated toxic waste is being sent for safe processing. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_toxic_02
    Static(238592, MS('Привезите груз к точке %s0: специалисты готовят очередную партию к обезвреживанию. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: specialists are preparing another batch for decontamination. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_toxic_03
    Static(238593, MS('Привезите груз к точке %s0: линия переработки опасных отходов ждёт сырьё в герметичных контейнерах. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the hazardous-waste processing line awaits sealed containers. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_toxic_04
    Static(238594, MS('Привезите груз к точке %s0: служба утилизации распределила мощности под эту партию отходов. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the disposal service has reserved capacity for this waste shipment. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_toxic_05
    Static(238595, MS('Пункт назначения — %s0. Здесь участок утилизации принимает отходы реакторных установок. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the disposal facility is accepting reactor waste. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_toxic_06
    Static(238596, MS('Пункт назначения — %s0. Здесь накопившиеся токсичные отходы отправляют на безопасную переработку. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, accumulated toxic waste is being sent for safe processing. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_toxic_07
    Static(238597, MS('Пункт назначения — %s0. Здесь специалисты готовят очередную партию к обезвреживанию. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, specialists are preparing another batch for decontamination. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_toxic_08
    Static(238598, MS('Пункт назначения — %s0. Здесь линия переработки опасных отходов ждёт сырьё в герметичных контейнерах. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the hazardous-waste processing line awaits sealed containers. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_toxic_09
    Static(238599, MS('Пункт назначения — %s0. Здесь служба утилизации распределила мощности под эту партию отходов. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the disposal service has reserved capacity for this waste shipment. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_toxic_10
    Static(238600, MS('Привезите груз к точке %s0: система жизнеобеспечения пополняет резерв питьевой воды. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: life support is replenishing its drinking-water reserve. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_water_01
    Static(238601, MS('Привезите груз к точке %s0: ремонт водоочистки требует внешнего запаса воды. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: water-treatment maintenance requires an external water supply. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_water_02
    Static(238602, MS('Привезите груз к точке %s0: жилые модули готовят к приёму новых работников. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: residential modules are preparing for new workers. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_water_03
    Static(238603, MS('Привезите груз к точке %s0: кухонному и бытовому хозяйству требуется очередная партия воды. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: kitchens and domestic services need their next water shipment. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_water_04
    Static(238604, MS('Привезите груз к точке %s0: служба снабжения обновляет аварийный запас воды. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the supply office is renewing its emergency water reserve. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_water_05
    Static(238605, MS('Пункт назначения — %s0. Здесь система жизнеобеспечения пополняет резерв питьевой воды. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, life support is replenishing its drinking-water reserve. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_water_06
    Static(238606, MS('Пункт назначения — %s0. Здесь ремонт водоочистки требует внешнего запаса воды. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, water-treatment maintenance requires an external water supply. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_water_07
    Static(238607, MS('Пункт назначения — %s0. Здесь жилые модули готовят к приёму новых работников. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, residential modules are preparing for new workers. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_water_08
    Static(238608, MS('Пункт назначения — %s0. Здесь кухонному и бытовому хозяйству требуется очередная партия воды. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, kitchens and domestic services need their next water shipment. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_water_09
    Static(238609, MS('Пункт назначения — %s0. Здесь служба снабжения обновляет аварийный запас воды. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the supply office is renewing its emergency water reserve. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_water_10
    Static(238610, MS('Привезите груз к точке %s0: служба безопасности обновляет запас личного оружия. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: security is renewing its stock of personal weapons. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_weapons_01
    Static(238611, MS('Привезите груз к точке %s0: охранные смены получают новое штатное вооружение. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: guard shifts are receiving new service weapons. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_weapons_02
    Static(238612, MS('Привезите груз к точке %s0: оружейная мастерская заменяет изношенные образцы. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the armoury is replacing worn weapons. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_weapons_03
    Static(238613, MS('Привезите груз к точке %s0: новым постам охраны требуется комплект вооружения. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: new security posts need their weapons allocation. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_weapons_04
    Static(238614, MS('Привезите груз к точке %s0: служба безопасности формирует резерв для защиты причалов. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: security is preparing a reserve to protect the docks. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_basic_weapons_05
    Static(238615, MS('Пункт назначения — %s0. Здесь служба безопасности обновляет запас личного оружия. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, security is renewing its stock of personal weapons. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_weapons_06
    Static(238616, MS('Пункт назначения — %s0. Здесь охранные смены получают новое штатное вооружение. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, guard shifts are receiving new service weapons. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_weapons_07
    Static(238617, MS('Пункт назначения — %s0. Здесь оружейная мастерская заменяет изношенные образцы. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the armoury is replacing worn weapons. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_weapons_08
    Static(238618, MS('Пункт назначения — %s0. Здесь новым постам охраны требуется комплект вооружения. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, new security posts need their weapons allocation. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_weapons_09
    Static(238619, MS('Пункт назначения — %s0. Здесь служба безопасности формирует резерв для защиты причалов. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, security is preparing a reserve to protect the docks. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_basic_weapons_10
    Static(238620, MS('Привезите груз к точке %s0: служба безопасности обновляет защитные установки. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: security is renewing defensive installations. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_defence_systems_01
    Static(238621, MS('Привезите груз к точке %s0: инженеры готовят новые системы обороны. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: engineers are preparing new defence systems. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_defence_systems_02
    Static(238622, MS('Привезите груз к точке %s0: ремонтный участок восстанавливает оборонительное оборудование. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a repair section is restoring defensive equipment. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_defence_systems_03
    Static(238623, MS('Привезите груз к точке %s0: охранная инфраструктура требует дополнительных защитных узлов. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: security infrastructure requires additional defensive units. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_defence_systems_04
    Static(238624, MS('Привезите груз к точке %s0: техническая служба пополняет резерв оборонительных систем. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: technical services are stocking spare defence systems. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_defence_systems_05
    Static(238625, MS('Пункт назначения — %s0. Здесь служба безопасности обновляет защитные установки. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, security is renewing defensive installations. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_defence_systems_06
    Static(238626, MS('Пункт назначения — %s0. Здесь инженеры готовят новые системы обороны. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, engineers are preparing new defence systems. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_defence_systems_07
    Static(238627, MS('Пункт назначения — %s0. Здесь ремонтный участок восстанавливает оборонительное оборудование. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a repair section is restoring defensive equipment. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_defence_systems_08
    Static(238628, MS('Пункт назначения — %s0. Здесь охранная инфраструктура требует дополнительных защитных узлов. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, security infrastructure requires additional defensive units. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_defence_systems_09
    Static(238629, MS('Пункт назначения — %s0. Здесь техническая служба пополняет резерв оборонительных систем. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, technical services are stocking spare defence systems. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_defence_systems_10
    Static(238630, MS('Привезите груз к точке %s0: ремонтный цех заменяет отказавшие электронные блоки. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a repair shop is replacing failed electronic units. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_electronics_01
    Static(238631, MS('Привезите груз к точке %s0: сборщики оснащают новые модули управляющей электроникой. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: assemblers are fitting new modules with control electronics. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_electronics_02
    Static(238632, MS('Привезите груз к точке %s0: станционные службы обновляют вычислительное оборудование. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: station services are renewing computing equipment. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_electronics_03
    Static(238633, MS('Привезите груз к точке %s0: производственная линия ждёт электронные компоненты. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a production line awaits electronic components. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_electronics_04
    Static(238634, MS('Привезите груз к точке %s0: инженеры формируют резерв плат для текущего обслуживания. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: engineers are stocking spare boards for routine maintenance. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_electronics_05
    Static(238635, MS('Пункт назначения — %s0. Здесь ремонтный цех заменяет отказавшие электронные блоки. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a repair shop is replacing failed electronic units. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_electronics_06
    Static(238636, MS('Пункт назначения — %s0. Здесь сборщики оснащают новые модули управляющей электроникой. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, assemblers are fitting new modules with control electronics. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_electronics_07
    Static(238637, MS('Пункт назначения — %s0. Здесь станционные службы обновляют вычислительное оборудование. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, station services are renewing computing equipment. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_electronics_08
    Static(238638, MS('Пункт назначения — %s0. Здесь производственная линия ждёт электронные компоненты. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a production line awaits electronic components. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_electronics_09
    Static(238639, MS('Пункт назначения — %s0. Здесь инженеры формируют резерв плат для текущего обслуживания. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, engineers are stocking spare boards for routine maintenance. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_electronics_10
    Static(238640, MS('Привезите груз к точке %s0: сборочный цех готовит новую серию корабельных двигателей. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: an assembly shop is preparing new ship engines. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_engine_components_01
    Static(238641, MS('Привезите груз к точке %s0: ремонтники восстанавливают изношенные двигательные установки. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: repair crews are restoring worn propulsion units. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_engine_components_02
    Static(238642, MS('Привезите груз к точке %s0: производство двигателей пополняет запас комплектующих. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: engine production is replenishing components. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_engine_components_03
    Static(238643, MS('Привезите груз к точке %s0: сервисная служба готовит комплекты для ремонта тяговых агрегатов. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a service team is preparing propulsion-unit repair kits. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_engine_components_04
    Static(238644, MS('Привезите груз к точке %s0: корабельные мастерские заменяют отработавшие моторные узлы. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: ship workshops are replacing worn engine assemblies. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_engine_components_05
    Static(238645, MS('Пункт назначения — %s0. Здесь сборочный цех готовит новую серию корабельных двигателей. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, an assembly shop is preparing new ship engines. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_engine_components_06
    Static(238646, MS('Пункт назначения — %s0. Здесь ремонтники восстанавливают изношенные двигательные установки. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, repair crews are restoring worn propulsion units. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_engine_components_07
    Static(238647, MS('Пункт назначения — %s0. Здесь производство двигателей пополняет запас комплектующих. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, engine production is replenishing components. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_engine_components_08
    Static(238648, MS('Пункт назначения — %s0. Здесь сервисная служба готовит комплекты для ремонта тяговых агрегатов. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a service team is preparing propulsion-unit repair kits. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_engine_components_09
    Static(238649, MS('Пункт назначения — %s0. Здесь корабельные мастерские заменяют отработавшие моторные узлы. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, ship workshops are replacing worn engine assemblies. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_engine_components_10
    Static(238650, MS('Привезите груз к точке %s0: перерабатывающая линия готовит сырьё для водородного топлива. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a processing line is preparing feedstock for hydrogen fuel. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_gas_balloons_01
    Static(238651, MS('Привезите груз к точке %s0: топливный завод пополняет запас сжиженного газа. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a fuel plant is replenishing liquefied-gas stocks. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_gas_balloons_02
    Static(238652, MS('Привезите груз к точке %s0: газовую партию ждут для следующего цикла переработки. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the next processing cycle awaits its gas shipment. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_gas_balloons_03
    Static(238653, MS('Привезите груз к точке %s0: ёмкости приёмного участка освободили под сжиженный газ. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: receiving tanks have been cleared for liquefied gas. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_gas_balloons_04
    Static(238654, MS('Привезите груз к точке %s0: технологи готовят газ к превращению в корабельное топливо. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: technicians are preparing gas for conversion into ship fuel. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_gas_balloons_05
    Static(238655, MS('Пункт назначения — %s0. Здесь перерабатывающая линия готовит сырьё для водородного топлива. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a processing line is preparing feedstock for hydrogen fuel. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_gas_balloons_06
    Static(238656, MS('Пункт назначения — %s0. Здесь топливный завод пополняет запас сжиженного газа. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a fuel plant is replenishing liquefied-gas stocks. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_gas_balloons_07
    Static(238657, MS('Пункт назначения — %s0. Здесь газовую партию ждут для следующего цикла переработки. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the next processing cycle awaits its gas shipment. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_gas_balloons_08
    Static(238658, MS('Пункт назначения — %s0. Здесь ёмкости приёмного участка освободили под сжиженный газ. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, receiving tanks have been cleared for liquefied gas. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_gas_balloons_09
    Static(238659, MS('Пункт назначения — %s0. Здесь технологи готовят газ к превращению в корабельное топливо. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, technicians are preparing gas for conversion into ship fuel. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_gas_balloons_10
    Static(238660, MS('Привезите груз к точке %s0: заправочная служба пополняет запас топлива для кораблей. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: refuelling services are replenishing ship fuel. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_gas_fuel_01
    Static(238661, MS('Привезите груз к точке %s0: транспортные экипажи готовятся к очередному рейсу. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: transport crews are preparing for their next voyage. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_gas_fuel_02
    Static(238662, MS('Привезите груз к точке %s0: топливное хозяйство обновляет рабочий резерв. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: fuel services are renewing their working reserve. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_gas_fuel_03
    Static(238663, MS('Привезите груз к точке %s0: возросшее движение у причалов увеличило расход топлива. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: increased dock traffic has raised fuel consumption. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_gas_fuel_04
    Static(238664, MS('Привезите груз к точке %s0: служебным кораблям требуется регулярная заправка. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: service ships need their regular refuelling. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_gas_fuel_05
    Static(238665, MS('Пункт назначения — %s0. Здесь заправочная служба пополняет запас топлива для кораблей. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, refuelling services are replenishing ship fuel. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_gas_fuel_06
    Static(238666, MS('Пункт назначения — %s0. Здесь транспортные экипажи готовятся к очередному рейсу. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, transport crews are preparing for their next voyage. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_gas_fuel_07
    Static(238667, MS('Пункт назначения — %s0. Здесь топливное хозяйство обновляет рабочий резерв. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, fuel services are renewing their working reserve. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_gas_fuel_08
    Static(238668, MS('Пункт назначения — %s0. Здесь возросшее движение у причалов увеличило расход топлива. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, increased dock traffic has raised fuel consumption. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_gas_fuel_09
    Static(238669, MS('Пункт назначения — %s0. Здесь служебным кораблям требуется регулярная заправка. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, service ships need their regular refuelling. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_gas_fuel_10
    Static(238670, MS('Привезите груз к точке %s0: газодобывающие установки проходят плановое обслуживание. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: gas-mining installations are undergoing scheduled maintenance. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_gasminer_parts_01
    Static(238671, MS('Привезите груз к точке %s0: изношенные насосы требуют заводских запчастей. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: worn pumps need factory spare parts. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_gasminer_parts_02
    Static(238672, MS('Привезите груз к точке %s0: газозаборный контур готовят к ремонту. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the gas intake circuit is being prepared for repair. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_gasminer_parts_03
    Static(238673, MS('Привезите груз к точке %s0: механики формируют резерв деталей для непрерывной добычи. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: mechanics are stocking spares to keep gas extraction running. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_gasminer_parts_04
    Static(238674, MS('Привезите груз к точке %s0: оборудование наполнения баллонов нуждается в обслуживании. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: cylinder-filling equipment needs servicing. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_gasminer_parts_05
    Static(238675, MS('Пункт назначения — %s0. Здесь газодобывающие установки проходят плановое обслуживание. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, gas-mining installations are undergoing scheduled maintenance. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_gasminer_parts_06
    Static(238676, MS('Пункт назначения — %s0. Здесь изношенные насосы требуют заводских запчастей. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, worn pumps need factory spare parts. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_gasminer_parts_07
    Static(238677, MS('Пункт назначения — %s0. Здесь газозаборный контур готовят к ремонту. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the gas intake circuit is being prepared for repair. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_gasminer_parts_08
    Static(238678, MS('Пункт назначения — %s0. Здесь механики формируют резерв деталей для непрерывной добычи. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, mechanics are stocking spares to keep gas extraction running. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_gasminer_parts_09
    Static(238679, MS('Пункт назначения — %s0. Здесь оборудование наполнения баллонов нуждается в обслуживании. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, cylinder-filling equipment needs servicing. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_gasminer_parts_10
    Static(238680, MS('Привезите груз к точке %s0: тепличные модули готовят к плановому ремонту. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: greenhouse modules are preparing for scheduled maintenance. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_greenhouse_parts_01
    Static(238681, MS('Привезите груз к точке %s0: система фотосинтеза нуждается в замене изношенных деталей. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the photosynthesis system needs worn parts replaced. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_greenhouse_parts_02
    Static(238682, MS('Привезите груз к точке %s0: биологический контур жизнеобеспечения получает новое оснащение. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the biological life-support loop is receiving new equipment. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_greenhouse_parts_03
    Static(238683, MS('Привезите груз к точке %s0: техники восстанавливают производительность станционных теплиц. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: technicians are restoring station greenhouse output. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_greenhouse_parts_04
    Static(238684, MS('Привезите груз к точке %s0: запас деталей нужен для бесперебойного обновления воздуха. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: spare parts are needed to keep biological air renewal running. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_greenhouse_parts_05
    Static(238685, MS('Пункт назначения — %s0. Здесь тепличные модули готовят к плановому ремонту. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, greenhouse modules are preparing for scheduled maintenance. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_greenhouse_parts_06
    Static(238686, MS('Пункт назначения — %s0. Здесь система фотосинтеза нуждается в замене изношенных деталей. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the photosynthesis system needs worn parts replaced. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_greenhouse_parts_07
    Static(238687, MS('Пункт назначения — %s0. Здесь биологический контур жизнеобеспечения получает новое оснащение. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the biological life-support loop is receiving new equipment. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_greenhouse_parts_08
    Static(238688, MS('Пункт назначения — %s0. Здесь техники восстанавливают производительность станционных теплиц. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, technicians are restoring station greenhouse output. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_greenhouse_parts_09
    Static(238689, MS('Пункт назначения — %s0. Здесь запас деталей нужен для бесперебойного обновления воздуха. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, spare parts are needed to keep biological air renewal running. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_greenhouse_parts_10
    Static(238690, MS('Привезите груз к точке %s0: ремонтная бригада комплектует запас для обслуживания прыжковых ворот. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a maintenance team is stocking parts for jump-gate servicing. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_jumpgate_parts_01
    Static(238691, MS('Привезите груз к точке %s0: изношенные узлы ворот должны пройти замену. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: worn gate components are due for replacement. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_jumpgate_parts_02
    Static(238692, MS('Привезите груз к точке %s0: плановые работы на межсистемном переходе ждут комплектующих. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: scheduled work on an intersystem crossing awaits components. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_jumpgate_parts_03
    Static(238693, MS('Привезите груз к точке %s0: инженеры готовят резерв оборудования для прыжковых ворот. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: engineers are preparing spare equipment for jump gates. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_jumpgate_parts_04
    Static(238694, MS('Привезите груз к точке %s0: сборка узлов межсистемной связи требует новых деталей. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: assembly of intersystem transit units requires new parts. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_jumpgate_parts_05
    Static(238695, MS('Пункт назначения — %s0. Здесь ремонтная бригада комплектует запас для обслуживания прыжковых ворот. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a maintenance team is stocking parts for jump-gate servicing. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_jumpgate_parts_06
    Static(238696, MS('Пункт назначения — %s0. Здесь изношенные узлы ворот должны пройти замену. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, worn gate components are due for replacement. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_jumpgate_parts_07
    Static(238697, MS('Пункт назначения — %s0. Здесь плановые работы на межсистемном переходе ждут комплектующих. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, scheduled work on an intersystem crossing awaits components. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_jumpgate_parts_08
    Static(238698, MS('Пункт назначения — %s0. Здесь инженеры готовят резерв оборудования для прыжковых ворот. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, engineers are preparing spare equipment for jump gates. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_jumpgate_parts_09
    Static(238699, MS('Пункт назначения — %s0. Здесь сборка узлов межсистемной связи требует новых деталей. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, assembly of intersystem transit units requires new parts. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_jumpgate_parts_10
    Static(238700, MS('Привезите груз к точке %s0: магазины готовят поставку фирменных вещей для состоятельных клиентов. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: shops are preparing branded goods for wealthy customers. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_luxury_consumer_01
    Static(238701, MS('Привезите груз к точке %s0: торговые представители собирают заказы на дорогие бытовые изделия. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: merchants are assembling orders for premium household goods. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_luxury_consumer_02
    Static(238702, MS('Привезите груз к точке %s0: салон пополняет коллекцию товаров известных марок. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a showroom is replenishing its collection of established brands. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_luxury_consumer_03
    Static(238703, MS('Привезите груз к точке %s0: заказчики ждут подлинные изделия с заводскими сертификатами. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: customers await genuine goods with manufacturer certificates. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_luxury_consumer_04
    Static(238704, MS('Привезите груз к точке %s0: снабжение гостевых апартаментов требует дорогого оснащения. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: guest apartments require premium furnishings. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_luxury_consumer_05
    Static(238705, MS('Пункт назначения — %s0. Здесь магазины готовят поставку фирменных вещей для состоятельных клиентов. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, shops are preparing branded goods for wealthy customers. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_luxury_consumer_06
    Static(238706, MS('Пункт назначения — %s0. Здесь торговые представители собирают заказы на дорогие бытовые изделия. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, merchants are assembling orders for premium household goods. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_luxury_consumer_07
    Static(238707, MS('Пункт назначения — %s0. Здесь салон пополняет коллекцию товаров известных марок. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a showroom is replenishing its collection of established brands. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_luxury_consumer_08
    Static(238708, MS('Пункт назначения — %s0. Здесь заказчики ждут подлинные изделия с заводскими сертификатами. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, customers await genuine goods with manufacturer certificates. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_luxury_consumer_09
    Static(238709, MS('Пункт назначения — %s0. Здесь снабжение гостевых апартаментов требует дорогого оснащения. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, guest apartments require premium furnishings. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_luxury_consumer_10
    Static(238710, MS('Привезите груз к точке %s0: ювелирные салоны пополняют коллекции изделий с бриллиантами. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: jewellery showrooms are replenishing diamond collections. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_luxury_diamonds_01
    Static(238711, MS('Привезите груз к точке %s0: покупатели ждут заказанные украшения ручной огранки. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: customers await jewellery featuring hand-cut diamonds. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_luxury_diamonds_02
    Static(238712, MS('Привезите груз к точке %s0: торговый дом готовит показ новой ювелирной партии. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a trading house is preparing a presentation of new jewellery. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_luxury_diamonds_03
    Static(238713, MS('Привезите груз к точке %s0: дилеры распределяют украшения между постоянными клиентами. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: dealers are allocating jewellery to regular customers. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_luxury_diamonds_04
    Static(238714, MS('Привезите груз к точке %s0: ювелирный отдел готовит подарочные заказы. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the jewellery department is preparing gift orders. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_luxury_diamonds_05
    Static(238715, MS('Пункт назначения — %s0. Здесь ювелирные салоны пополняют коллекции изделий с бриллиантами. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, jewellery showrooms are replenishing diamond collections. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_luxury_diamonds_06
    Static(238716, MS('Пункт назначения — %s0. Здесь покупатели ждут заказанные украшения ручной огранки. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, customers await jewellery featuring hand-cut diamonds. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_luxury_diamonds_07
    Static(238717, MS('Пункт назначения — %s0. Здесь торговый дом готовит показ новой ювелирной партии. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a trading house is preparing a presentation of new jewellery. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_luxury_diamonds_08
    Static(238718, MS('Пункт назначения — %s0. Здесь дилеры распределяют украшения между постоянными клиентами. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, dealers are allocating jewellery to regular customers. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_luxury_diamonds_09
    Static(238719, MS('Пункт назначения — %s0. Здесь ювелирный отдел готовит подарочные заказы. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the jewellery department is preparing gift orders. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_luxury_diamonds_10
    Static(238720, MS('Привезите груз к точке %s0: кухня готовится принять гостей, предпочитающих натуральные продукты. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a kitchen is preparing for guests who prefer natural food. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_luxury_food_01
    Static(238721, MS('Привезите груз к точке %s0: ресторан пополняет запас редких натуральных ингредиентов. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a restaurant is replenishing rare natural ingredients. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_luxury_food_02
    Static(238722, MS('Привезите груз к точке %s0: холодильные склады подготовлены под деликатесы. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: cold stores have been prepared for delicacies. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_luxury_food_03
    Static(238723, MS('Привезите груз к точке %s0: заказчики ожидают продукты для торжественного приёма. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: customers await food for a formal reception. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_luxury_food_04
    Static(238724, MS('Привезите груз к точке %s0: поставщики комплектуют продовольственные заказы для взыскательных клиентов. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: suppliers are assembling food orders for demanding customers. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_luxury_food_05
    Static(238725, MS('Пункт назначения — %s0. Здесь кухня готовится принять гостей, предпочитающих натуральные продукты. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a kitchen is preparing for guests who prefer natural food. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_luxury_food_06
    Static(238726, MS('Пункт назначения — %s0. Здесь ресторан пополняет запас редких натуральных ингредиентов. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a restaurant is replenishing rare natural ingredients. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_luxury_food_07
    Static(238727, MS('Пункт назначения — %s0. Здесь холодильные склады подготовлены под деликатесы. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, cold stores have been prepared for delicacies. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_luxury_food_08
    Static(238728, MS('Пункт назначения — %s0. Здесь заказчики ожидают продукты для торжественного приёма. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, customers await food for a formal reception. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_luxury_food_09
    Static(238729, MS('Пункт назначения — %s0. Здесь поставщики комплектуют продовольственные заказы для взыскательных клиентов. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, suppliers are assembling food orders for demanding customers. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_luxury_food_10
    Static(238730, MS('Привезите груз к точке %s0: ювелирный салон ждёт новую коллекцию золотых украшений. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a jeweller awaits a new gold collection. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_luxury_gold_01
    Static(238731, MS('Привезите груз к точке %s0: состоятельные клиенты заказали золотые изделия. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: wealthy clients have ordered gold jewellery. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_luxury_gold_02
    Static(238732, MS('Привезите груз к точке %s0: торговый дом пополняет запас дорогих подарков. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a trading house is replenishing premium gifts. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_luxury_gold_03
    Static(238733, MS('Привезите груз к точке %s0: дилеры готовят поставку украшений для частных покупателей. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: dealers are preparing jewellery for private buyers. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_luxury_gold_04
    Static(238734, MS('Привезите груз к точке %s0: салон обновляет витрину изделий из драгоценного металла. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a showroom is renewing its precious-metal display. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_luxury_gold_05
    Static(238735, MS('Пункт назначения — %s0. Здесь ювелирный салон ждёт новую коллекцию золотых украшений. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a jeweller awaits a new gold collection. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_luxury_gold_06
    Static(238736, MS('Пункт назначения — %s0. Здесь состоятельные клиенты заказали золотые изделия. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, wealthy clients have ordered gold jewellery. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_luxury_gold_07
    Static(238737, MS('Пункт назначения — %s0. Здесь торговый дом пополняет запас дорогих подарков. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a trading house is replenishing premium gifts. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_luxury_gold_08
    Static(238738, MS('Пункт назначения — %s0. Здесь дилеры готовят поставку украшений для частных покупателей. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, dealers are preparing jewellery for private buyers. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_luxury_gold_09
    Static(238739, MS('Пункт назначения — %s0. Здесь салон обновляет витрину изделий из драгоценного металла. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a showroom is renewing its precious-metal display. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_luxury_gold_10
    Static(238740, MS('Привезите груз к точке %s0: шахтёры обновляют оборудование рабочих забоев. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: miners are renewing working-face equipment. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_mining_equip_01
    Static(238741, MS('Привезите груз к точке %s0: добывающий участок готовит новую рабочую смену. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a mining section is preparing a new work shift. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_mining_equip_02
    Static(238742, MS('Привезите груз к точке %s0: изношенные горные машины требуют замены. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: worn mining machines need replacement. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_mining_equip_03
    Static(238743, MS('Привезите груз к точке %s0: шахта расширяет участок добычи руды. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a mine is expanding its ore-extraction section. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_mining_equip_04
    Static(238744, MS('Привезите груз к точке %s0: ремонтники формируют резерв горнодобывающего оборудования. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: maintenance crews are stocking spare mining equipment. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_mining_equip_05
    Static(238745, MS('Пункт назначения — %s0. Здесь шахтёры обновляют оборудование рабочих забоев. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, miners are renewing working-face equipment. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_mining_equip_06
    Static(238746, MS('Пункт назначения — %s0. Здесь добывающий участок готовит новую рабочую смену. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a mining section is preparing a new work shift. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_mining_equip_07
    Static(238747, MS('Пункт назначения — %s0. Здесь изношенные горные машины требуют замены. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, worn mining machines need replacement. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_mining_equip_08
    Static(238748, MS('Пункт назначения — %s0. Здесь шахта расширяет участок добычи руды. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a mine is expanding its ore-extraction section. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_mining_equip_09
    Static(238749, MS('Пункт назначения — %s0. Здесь ремонтники формируют резерв горнодобывающего оборудования. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, maintenance crews are stocking spare mining equipment. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_mining_equip_10
    Static(238750, MS('Привезите груз к точке %s0: энергетики готовятся к перезагрузке реакторов. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: power crews are preparing to refuel reactors. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_mox_fuel_01
    Static(238751, MS('Привезите груз к точке %s0: реакторный участок пополняет запас радиоактивного топлива. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the reactor section is replenishing radioactive fuel. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_mox_fuel_02
    Static(238752, MS('Привезите груз к точке %s0: крупные корабли готовят энергетические установки к дальнему рейсу. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: large ships are preparing their power plants for a long voyage. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_mox_fuel_03
    Static(238753, MS('Привезите груз к точке %s0: служба снабжения обновляет резерв реакторного топлива. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the supply office is renewing its reactor-fuel reserve. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_mox_fuel_04
    Static(238754, MS('Привезите груз к точке %s0: после длительной работы реакторам требуется новая загрузка. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: reactors need a fresh fuel load after extended operation. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_mox_fuel_05
    Static(238755, MS('Пункт назначения — %s0. Здесь энергетики готовятся к перезагрузке реакторов. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, power crews are preparing to refuel reactors. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_mox_fuel_06
    Static(238756, MS('Пункт назначения — %s0. Здесь реакторный участок пополняет запас радиоактивного топлива. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the reactor section is replenishing radioactive fuel. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_mox_fuel_07
    Static(238757, MS('Пункт назначения — %s0. Здесь крупные корабли готовят энергетические установки к дальнему рейсу. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, large ships are preparing their power plants for a long voyage. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_mox_fuel_08
    Static(238758, MS('Пункт назначения — %s0. Здесь служба снабжения обновляет резерв реакторного топлива. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the supply office is renewing its reactor-fuel reserve. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_mox_fuel_09
    Static(238759, MS('Пункт назначения — %s0. Здесь после длительной работы реакторам требуется новая загрузка. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, reactors need a fresh fuel load after extended operation. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_mox_fuel_10
    Static(238760, MS('Привезите груз к точке %s0: экипажи пополняют боекомплект после дежурства. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: crews are replenishing ammunition after duty. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_munitions_01
    Static(238761, MS('Привезите груз к точке %s0: оружейный склад принимает комплекты боеприпасов. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the armoury is receiving ammunition kits. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_munitions_02
    Static(238762, MS('Привезите груз к точке %s0: патрульные подразделения готовятся к новым вылетам. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: patrol units are preparing for new sorties. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_munitions_03
    Static(238763, MS('Привезите груз к точке %s0: охранение торговых маршрутов увеличило расход боеприпасов. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: trade-route protection has increased ammunition consumption. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_munitions_04
    Static(238764, MS('Привезите груз к точке %s0: служба снабжения формирует резерв боекомплекта. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the supply office is building an ammunition reserve. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_munitions_05
    Static(238765, MS('Пункт назначения — %s0. Здесь экипажи пополняют боекомплект после дежурства. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, crews are replenishing ammunition after duty. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_munitions_06
    Static(238766, MS('Пункт назначения — %s0. Здесь оружейный склад принимает комплекты боеприпасов. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the armoury is receiving ammunition kits. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_munitions_07
    Static(238767, MS('Пункт назначения — %s0. Здесь патрульные подразделения готовятся к новым вылетам. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, patrol units are preparing for new sorties. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_munitions_08
    Static(238768, MS('Пункт назначения — %s0. Здесь охранение торговых маршрутов увеличило расход боеприпасов. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, trade-route protection has increased ammunition consumption. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_munitions_09
    Static(238769, MS('Пункт назначения — %s0. Здесь служба снабжения формирует резерв боекомплекта. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the supply office is building an ammunition reserve. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_munitions_10
    Static(238770, MS('Привезите груз к точке %s0: сборщики вычислительных блоков ждут оптические чипы. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: computer-unit assemblers await optical chips. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_optical_chips_01
    Static(238771, MS('Привезите груз к точке %s0: цех электроники готовит новую серию управляющих модулей. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: an electronics workshop is preparing new control modules. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_optical_chips_02
    Static(238772, MS('Привезите груз к точке %s0: инженеры обновляют оптические вычислительные узлы. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: engineers are renewing optical processing units. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_optical_chips_03
    Static(238773, MS('Привезите груз к точке %s0: производство точных приборов нуждается в чипах. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: precision-instrument production needs chips. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_optical_chips_04
    Static(238774, MS('Привезите груз к точке %s0: ремонтная линия заменяет повреждённые вычислительные платы. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a repair line is replacing damaged processor boards. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_optical_chips_05
    Static(238775, MS('Пункт назначения — %s0. Здесь сборщики вычислительных блоков ждут оптические чипы. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, computer-unit assemblers await optical chips. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_optical_chips_06
    Static(238776, MS('Пункт назначения — %s0. Здесь цех электроники готовит новую серию управляющих модулей. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, an electronics workshop is preparing new control modules. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_optical_chips_07
    Static(238777, MS('Пункт назначения — %s0. Здесь инженеры обновляют оптические вычислительные узлы. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, engineers are renewing optical processing units. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_optical_chips_08
    Static(238778, MS('Пункт назначения — %s0. Здесь производство точных приборов нуждается в чипах. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, precision-instrument production needs chips. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_optical_chips_09
    Static(238779, MS('Пункт назначения — %s0. Здесь ремонтная линия заменяет повреждённые вычислительные платы. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a repair line is replacing damaged processor boards. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_optical_chips_10
    Static(238780, MS('Привезите груз к точке %s0: производство готовит партию полимерных деталей. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: production is preparing a batch of polymer parts. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_polymers_01
    Static(238781, MS('Привезите груз к точке %s0: сборочная линия пополняет запас технических полимеров. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: an assembly line is replenishing engineering polymers. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_polymers_02
    Static(238782, MS('Привезите груз к точке %s0: цех изготавливает изоляционные элементы. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a workshop is making insulating components. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_polymers_03
    Static(238783, MS('Привезите груз к точке %s0: ремонтникам нужен материал для новых уплотнений. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: repair crews need material for new seals. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_polymers_04
    Static(238784, MS('Привезите груз к точке %s0: технологи готовят сырьё для формования сложных деталей. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: technicians are preparing feedstock for moulded components. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_polymers_05
    Static(238785, MS('Пункт назначения — %s0. Здесь производство готовит партию полимерных деталей. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, production is preparing a batch of polymer parts. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_polymers_06
    Static(238786, MS('Пункт назначения — %s0. Здесь сборочная линия пополняет запас технических полимеров. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, an assembly line is replenishing engineering polymers. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_polymers_07
    Static(238787, MS('Пункт назначения — %s0. Здесь цех изготавливает изоляционные элементы. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a workshop is making insulating components. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_polymers_08
    Static(238788, MS('Пункт назначения — %s0. Здесь ремонтникам нужен материал для новых уплотнений. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, repair crews need material for new seals. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_polymers_09
    Static(238789, MS('Пункт назначения — %s0. Здесь технологи готовят сырьё для формования сложных деталей. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, technicians are preparing feedstock for moulded components. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_polymers_10
    Static(238790, MS('Привезите груз к точке %s0: энергетики заменяют разряженные солнечные генераторы. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: power crews are replacing depleted solar generators. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_power_solar_01
    Static(238791, MS('Привезите груз к точке %s0: станционные службы пополняют запас чистой энергии. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: station services are replenishing their clean-energy supply. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_power_solar_02
    Static(238792, MS('Привезите груз к точке %s0: новому жилому модулю нужен заряженный источник питания. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a new residential module needs a charged power source. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_power_solar_03
    Static(238793, MS('Привезите груз к точке %s0: резервное питание переводят на заряженные солнечные блоки. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: backup power is being transferred to charged solar units. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_power_solar_04
    Static(238794, MS('Привезите груз к точке %s0: ремонт основного питания требует запаса заряженных генераторов. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: main-power maintenance requires a reserve of charged generators. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_power_solar_05
    Static(238795, MS('Пункт назначения — %s0. Здесь энергетики заменяют разряженные солнечные генераторы. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, power crews are replacing depleted solar generators. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_power_solar_06
    Static(238796, MS('Пункт назначения — %s0. Здесь станционные службы пополняют запас чистой энергии. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, station services are replenishing their clean-energy supply. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_power_solar_07
    Static(238797, MS('Пункт назначения — %s0. Здесь новому жилому модулю нужен заряженный источник питания. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a new residential module needs a charged power source. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_power_solar_08
    Static(238798, MS('Пункт назначения — %s0. Здесь резервное питание переводят на заряженные солнечные блоки. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, backup power is being transferred to charged solar units. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_power_solar_09
    Static(238799, MS('Пункт назначения — %s0. Здесь ремонт основного питания требует запаса заряженных генераторов. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, main-power maintenance requires a reserve of charged generators. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_power_solar_10
    Static(238800, MS('Привезите груз к точке %s0: зарядная площадка принимает отработавшие солнечные генераторы. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the charging facility is accepting depleted solar generators. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_power_solar_empty_01
    Static(238801, MS('Привезите груз к точке %s0: энергетики готовят разряженные блоки к повторному использованию. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: power crews are preparing depleted units for reuse. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_power_solar_empty_02
    Static(238802, MS('Привезите груз к точке %s0: солнечная установка освободила мощности для зарядки этой партии. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the solar installation has capacity to recharge this batch. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_power_solar_empty_03
    Static(238803, MS('Привезите груз к точке %s0: возвращаемые генераторы должны пройти зарядку и проверку. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: returned generators need recharging and inspection. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_power_solar_empty_04
    Static(238804, MS('Привезите груз к точке %s0: цикл оборота солнечных блоков требует возврата пустых накопителей. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the solar-unit supply cycle needs its empty storage units returned. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_power_solar_empty_05
    Static(238805, MS('Пункт назначения — %s0. Здесь зарядная площадка принимает отработавшие солнечные генераторы. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the charging facility is accepting depleted solar generators. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_power_solar_empty_06
    Static(238806, MS('Пункт назначения — %s0. Здесь энергетики готовят разряженные блоки к повторному использованию. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, power crews are preparing depleted units for reuse. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_power_solar_empty_07
    Static(238807, MS('Пункт назначения — %s0. Здесь солнечная установка освободила мощности для зарядки этой партии. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the solar installation has capacity to recharge this batch. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_power_solar_empty_08
    Static(238808, MS('Пункт назначения — %s0. Здесь возвращаемые генераторы должны пройти зарядку и проверку. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, returned generators need recharging and inspection. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_power_solar_empty_09
    Static(238809, MS('Пункт назначения — %s0. Здесь цикл оборота солнечных блоков требует возврата пустых накопителей. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the solar-unit supply cycle needs its empty storage units returned. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_power_solar_empty_10
    Static(238810, MS('Привезите груз к точке %s0: цех готовит новую линию серийного производства. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a workshop is preparing a new mass-production line. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_prod_machines_01
    Static(238811, MS('Привезите груз к точке %s0: изношенные станки мешают выдерживать точность обработки деталей. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: worn machine tools can no longer maintain machining tolerances. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_prod_machines_02
    Static(238812, MS('Привезите груз к точке %s0: завод расширяет участок изготовления корабельных узлов. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a factory is expanding its ship-component production section. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_prod_machines_03
    Static(238813, MS('Привезите груз к точке %s0: ремонтный цех заменяет станки, выработавшие свой ресурс. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a repair shop is replacing machine tools at the end of their service life. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_prod_machines_04
    Static(238814, MS('Привезите груз к точке %s0: производственники готовят резерв оборудования на время планового ремонта. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: production crews are preparing spare machinery for scheduled maintenance. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_prod_machines_05
    Static(238815, MS('Пункт назначения — %s0. Здесь цех готовит новую линию серийного производства. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a workshop is preparing a new mass-production line. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_prod_machines_06
    Static(238816, MS('Пункт назначения — %s0. Здесь изношенные станки мешают выдерживать точность обработки деталей. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, worn machine tools can no longer maintain machining tolerances. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_prod_machines_07
    Static(238817, MS('Пункт назначения — %s0. Здесь завод расширяет участок изготовления корабельных узлов. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a factory is expanding its ship-component production section. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_prod_machines_08
    Static(238818, MS('Пункт назначения — %s0. Здесь ремонтный цех заменяет станки, выработавшие свой ресурс. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a repair shop is replacing machine tools at the end of their service life. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_prod_machines_09
    Static(238819, MS('Пункт назначения — %s0. Здесь производственники готовят резерв оборудования на время планового ремонта. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, production crews are preparing spare machinery for scheduled maintenance. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_prod_machines_10
    Static(238820, MS('Привезите груз к точке %s0: энергетики заменяют отработавшие реакторные блоки. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: power crews are replacing worn reactor units. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_reactors_01
    Static(238821, MS('Привезите груз к точке %s0: основное питание готовят к плановому обновлению. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the main power supply is preparing for scheduled renewal. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_reactors_02
    Static(238822, MS('Привезите груз к точке %s0: техническая служба создаёт резерв реакторных установок. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: technical services are stocking spare reactor installations. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_reactors_03
    Static(238823, MS('Привезите груз к точке %s0: новые энергопотребители требуют дополнительных реакторов. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: new power consumers require additional reactors. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_reactors_04
    Static(238824, MS('Привезите груз к точке %s0: изношенная энергетическая установка ожидает замену. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a worn power plant awaits replacement. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_reactors_05
    Static(238825, MS('Пункт назначения — %s0. Здесь энергетики заменяют отработавшие реакторные блоки. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, power crews are replacing worn reactor units. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_reactors_06
    Static(238826, MS('Пункт назначения — %s0. Здесь основное питание готовят к плановому обновлению. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the main power supply is preparing for scheduled renewal. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_reactors_07
    Static(238827, MS('Пункт назначения — %s0. Здесь техническая служба создаёт резерв реакторных установок. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, technical services are stocking spare reactor installations. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_reactors_08
    Static(238828, MS('Пункт назначения — %s0. Здесь новые энергопотребители требуют дополнительных реакторов. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, new power consumers require additional reactors. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_reactors_09
    Static(238829, MS('Пункт назначения — %s0. Здесь изношенная энергетическая установка ожидает замену. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a worn power plant awaits replacement. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_reactors_10
    Static(238830, MS('Привезите груз к точке %s0: лаборатория готовится к новой серии измерений. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a laboratory is preparing a new measurement series. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_research_equip_01
    Static(238831, MS('Привезите груз к точке %s0: учёные обновляют приборы для точного анализа образцов. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: scientists are upgrading instruments for precise sample analysis. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_research_equip_02
    Static(238832, MS('Привезите груз к точке %s0: исследовательская группа расширяет экспериментальную установку. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a research team is expanding its experimental apparatus. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_research_equip_03
    Static(238833, MS('Привезите груз к точке %s0: аналитический отдел заменяет устаревшее оборудование. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: an analysis department is replacing obsolete equipment. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_research_equip_04
    Static(238834, MS('Привезите груз к точке %s0: новая исследовательская программа требует дополнительных приборов. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a new research programme requires additional instruments. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_research_equip_05
    Static(238835, MS('Пункт назначения — %s0. Здесь лаборатория готовится к новой серии измерений. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a laboratory is preparing a new measurement series. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_research_equip_06
    Static(238836, MS('Пункт назначения — %s0. Здесь учёные обновляют приборы для точного анализа образцов. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, scientists are upgrading instruments for precise sample analysis. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_research_equip_07
    Static(238837, MS('Пункт назначения — %s0. Здесь исследовательская группа расширяет экспериментальную установку. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a research team is expanding its experimental apparatus. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_research_equip_08
    Static(238838, MS('Пункт назначения — %s0. Здесь аналитический отдел заменяет устаревшее оборудование. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, an analysis department is replacing obsolete equipment. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_research_equip_09
    Static(238839, MS('Пункт назначения — %s0. Здесь новая исследовательская программа требует дополнительных приборов. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a new research programme requires additional instruments. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_research_equip_10
    Static(238840, MS('Привезите груз к точке %s0: металлурги готовят сырьё для жаропрочных сплавов. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: metallurgists are preparing feedstock for heat-resistant alloys. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_berilium_01
    Static(238841, MS('Привезите груз к точке %s0: линия переработки бериллия пополняет запас руды. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a beryllium processing line is replenishing ore. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_berilium_02
    Static(238842, MS('Привезите груз к точке %s0: производство деталей торговых путей ждёт бериллиевое сырьё. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: trade-lane component production awaits beryllium feedstock. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_berilium_03
    Static(238843, MS('Привезите груз к точке %s0: изготовление узлов прыжковых ворот требует новой партии бериллия. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: jump-gate component production needs a new beryllium shipment. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_berilium_04
    Static(238844, MS('Привезите груз к точке %s0: плавильный участок готовит очередную загрузку бериллиевой руды. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a smelting section is preparing its next beryllium ore charge. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_berilium_05
    Static(238845, MS('Пункт назначения — %s0. Здесь металлурги готовят сырьё для жаропрочных сплавов. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, metallurgists are preparing feedstock for heat-resistant alloys. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_berilium_06
    Static(238846, MS('Пункт назначения — %s0. Здесь линия переработки бериллия пополняет запас руды. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a beryllium processing line is replenishing ore. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_berilium_07
    Static(238847, MS('Пункт назначения — %s0. Здесь производство деталей торговых путей ждёт бериллиевое сырьё. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, trade-lane component production awaits beryllium feedstock. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_berilium_08
    Static(238848, MS('Пункт назначения — %s0. Здесь изготовление узлов прыжковых ворот требует новой партии бериллия. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, jump-gate component production needs a new beryllium shipment. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_berilium_09
    Static(238849, MS('Пункт назначения — %s0. Здесь плавильный участок готовит очередную загрузку бериллиевой руды. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a smelting section is preparing its next beryllium ore charge. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_berilium_10
    Static(238850, MS('Привезите груз к точке %s0: ограночный участок принимает необработанные алмазы. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a cutting workshop is receiving rough diamonds. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_diamonds_01
    Static(238851, MS('Привезите груз к точке %s0: производство точного инструмента ждёт алмазное сырьё. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: precision-tool production awaits raw diamonds. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_diamonds_02
    Static(238852, MS('Привезите груз к точке %s0: специалисты отбирают камни для промышленной обработки. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: specialists are selecting stones for industrial processing. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_diamonds_03
    Static(238853, MS('Привезите груз к точке %s0: ювелирные мастерские готовят алмазы к огранке. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: jewellery workshops are preparing diamonds for cutting. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_diamonds_04
    Static(238854, MS('Привезите груз к точке %s0: линия обработки камней пополняет запас сырья. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a stone-processing line is replenishing raw materials. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_diamonds_05
    Static(238855, MS('Пункт назначения — %s0. Здесь ограночный участок принимает необработанные алмазы. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a cutting workshop is receiving rough diamonds. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_diamonds_06
    Static(238856, MS('Пункт назначения — %s0. Здесь производство точного инструмента ждёт алмазное сырьё. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, precision-tool production awaits raw diamonds. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_diamonds_07
    Static(238857, MS('Пункт назначения — %s0. Здесь специалисты отбирают камни для промышленной обработки. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, specialists are selecting stones for industrial processing. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_diamonds_08
    Static(238858, MS('Пункт назначения — %s0. Здесь ювелирные мастерские готовят алмазы к огранке. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, jewellery workshops are preparing diamonds for cutting. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_diamonds_09
    Static(238859, MS('Пункт назначения — %s0. Здесь линия обработки камней пополняет запас сырья. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a stone-processing line is replenishing raw materials. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_diamonds_10
    Static(238860, MS('Привезите груз к точке %s0: переработчики готовят золото для электронных компонентов. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: processors are preparing gold for electronic components. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_gold_01
    Static(238861, MS('Привезите груз к точке %s0: ювелирное производство пополняет запас драгоценного сырья. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: jewellery production is replenishing precious-metal feedstock. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_gold_02
    Static(238862, MS('Привезите груз к точке %s0: аффинажный участок готовит новую партию золота. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a refining section is preparing a new gold batch. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_gold_03
    Static(238863, MS('Привезите груз к точке %s0: производители контактов ждут золотосодержащее сырьё. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: contact manufacturers await gold-bearing feedstock. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_gold_04
    Static(238864, MS('Привезите груз к точке %s0: плавильщики формируют запас для следующего цикла очистки. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: smelters are stocking material for the next refining cycle. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_gold_05
    Static(238865, MS('Пункт назначения — %s0. Здесь переработчики готовят золото для электронных компонентов. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, processors are preparing gold for electronic components. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_gold_06
    Static(238866, MS('Пункт назначения — %s0. Здесь ювелирное производство пополняет запас драгоценного сырья. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, jewellery production is replenishing precious-metal feedstock. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_gold_07
    Static(238867, MS('Пункт назначения — %s0. Здесь аффинажный участок готовит новую партию золота. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a refining section is preparing a new gold batch. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_gold_08
    Static(238868, MS('Пункт назначения — %s0. Здесь производители контактов ждут золотосодержащее сырьё. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, contact manufacturers await gold-bearing feedstock. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_gold_09
    Static(238869, MS('Пункт назначения — %s0. Здесь плавильщики формируют запас для следующего цикла очистки. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, smelters are stocking material for the next refining cycle. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_gold_10
    Static(238870, MS('Привезите груз к точке %s0: металлурги готовят никель для жаропрочных сплавов. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: metallurgists are preparing nickel for heat-resistant alloys. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_nicollum_01
    Static(238871, MS('Привезите груз к точке %s0: производство двигателей нуждается в никелевом сырье. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: engine production needs nickel feedstock. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_nicollum_02
    Static(238872, MS('Привезите груз к точке %s0: перерабатывающая линия пополняет запас никелевой руды. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a processing line is replenishing nickel ore. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_nicollum_03
    Static(238873, MS('Привезите груз к точке %s0: плавильщики готовят следующую загрузку никеля. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: smelters are preparing their next nickel charge. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_nicollum_04
    Static(238874, MS('Привезите груз к точке %s0: изготовление термостойких деталей требует новой партии руды. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: heat-resistant component production needs a new ore shipment. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_nicollum_05
    Static(238875, MS('Пункт назначения — %s0. Здесь металлурги готовят никель для жаропрочных сплавов. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, metallurgists are preparing nickel for heat-resistant alloys. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_nicollum_06
    Static(238876, MS('Пункт назначения — %s0. Здесь производство двигателей нуждается в никелевом сырье. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, engine production needs nickel feedstock. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_nicollum_07
    Static(238877, MS('Пункт назначения — %s0. Здесь перерабатывающая линия пополняет запас никелевой руды. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a processing line is replenishing nickel ore. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_nicollum_08
    Static(238878, MS('Пункт назначения — %s0. Здесь плавильщики готовят следующую загрузку никеля. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, smelters are preparing their next nickel charge. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_nicollum_09
    Static(238879, MS('Пункт назначения — %s0. Здесь изготовление термостойких деталей требует новой партии руды. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, heat-resistant component production needs a new ore shipment. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_nicollum_10
    Static(238880, MS('Привезите груз к точке %s0: плавильный цех готовит сырьё для сверхпрочного сплава. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the smelting shop is preparing feedstock for superalloy. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_niobium_01
    Static(238881, MS('Привезите груз к точке %s0: кораблестроительная цепочка пополняет запас ниобия. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the shipbuilding supply chain is replenishing niobium. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_niobium_02
    Static(238882, MS('Привезите груз к точке %s0: металлурги запускают следующую партию высокопрочного металла. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: metallurgists are starting another high-strength metal batch. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_niobium_03
    Static(238883, MS('Привезите груз к точке %s0: переработчики ниобиевой руды ждут загрузку. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: niobium ore processors await their next charge. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_niobium_04
    Static(238884, MS('Привезите груз к точке %s0: производство силовых конструкций требует ниобиевое сырьё. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: load-bearing structure production requires niobium feedstock. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_niobium_05
    Static(238885, MS('Пункт назначения — %s0. Здесь плавильный цех готовит сырьё для сверхпрочного сплава. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the smelting shop is preparing feedstock for superalloy. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_niobium_06
    Static(238886, MS('Пункт назначения — %s0. Здесь кораблестроительная цепочка пополняет запас ниобия. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the shipbuilding supply chain is replenishing niobium. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_niobium_07
    Static(238887, MS('Пункт назначения — %s0. Здесь металлурги запускают следующую партию высокопрочного металла. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, metallurgists are starting another high-strength metal batch. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_niobium_08
    Static(238888, MS('Пункт назначения — %s0. Здесь переработчики ниобиевой руды ждут загрузку. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, niobium ore processors await their next charge. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_niobium_09
    Static(238889, MS('Пункт назначения — %s0. Здесь производство силовых конструкций требует ниобиевое сырьё. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, load-bearing structure production requires niobium feedstock. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_niobium_10
    Static(238890, MS('Привезите груз к точке %s0: плавильщики готовят свинец для радиационно-защитного сплава. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: smelters are preparing lead for radiation-shielding alloy. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_plumbum_01
    Static(238891, MS('Привезите груз к точке %s0: производство реакторных экранов ждёт свинцовое сырьё. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: reactor-shield production awaits lead feedstock. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_plumbum_02
    Static(238892, MS('Привезите груз к точке %s0: перерабатывающий участок пополняет запас свинцовой руды. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a processing section is replenishing lead ore. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_plumbum_03
    Static(238893, MS('Привезите груз к точке %s0: металлурги готовят загрузку для защитных материалов. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: metallurgists are preparing a charge for shielding materials. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_plumbum_04
    Static(238894, MS('Привезите груз к точке %s0: изготовителям радиационной защиты требуется новая партия свинца. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: radiation-shield manufacturers need a new lead shipment. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_plumbum_05
    Static(238895, MS('Пункт назначения — %s0. Здесь плавильщики готовят свинец для радиационно-защитного сплава. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, smelters are preparing lead for radiation-shielding alloy. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_plumbum_06
    Static(238896, MS('Пункт назначения — %s0. Здесь производство реакторных экранов ждёт свинцовое сырьё. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, reactor-shield production awaits lead feedstock. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_plumbum_07
    Static(238897, MS('Пункт назначения — %s0. Здесь перерабатывающий участок пополняет запас свинцовой руды. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a processing section is replenishing lead ore. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_plumbum_08
    Static(238898, MS('Пункт назначения — %s0. Здесь металлурги готовят загрузку для защитных материалов. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, metallurgists are preparing a charge for shielding materials. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_plumbum_09
    Static(238899, MS('Пункт назначения — %s0. Здесь изготовителям радиационной защиты требуется новая партия свинца. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, radiation-shield manufacturers need a new lead shipment. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_plumbum_10
    Static(238900, MS('Привезите груз к точке %s0: производство электроники пополняет запас серебра. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: electronics production is replenishing silver. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_silver_01
    Static(238901, MS('Привезите груз к точке %s0: металлургам нужно серебро для сверхпроводящих сплавов. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: metallurgists need silver for superconducting alloys. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_silver_02
    Static(238902, MS('Привезите груз к точке %s0: аффинажная линия принимает серебросодержащее сырьё. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a refining line is receiving silver-bearing feedstock. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_silver_03
    Static(238903, MS('Привезите груз к точке %s0: ювелирные мастерские готовят новую партию серебряных изделий. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: jewellery workshops are preparing a new silver batch. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_silver_04
    Static(238904, MS('Привезите груз к точке %s0: производство проводников ждёт очищенное серебро. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: conductor production awaits refined silver. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_silver_05
    Static(238905, MS('Пункт назначения — %s0. Здесь производство электроники пополняет запас серебра. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, electronics production is replenishing silver. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_silver_06
    Static(238906, MS('Пункт назначения — %s0. Здесь металлургам нужно серебро для сверхпроводящих сплавов. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, metallurgists need silver for superconducting alloys. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_silver_07
    Static(238907, MS('Пункт назначения — %s0. Здесь аффинажная линия принимает серебросодержащее сырьё. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a refining line is receiving silver-bearing feedstock. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_silver_08
    Static(238908, MS('Пункт назначения — %s0. Здесь ювелирные мастерские готовят новую партию серебряных изделий. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, jewellery workshops are preparing a new silver batch. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_silver_09
    Static(238909, MS('Пункт назначения — %s0. Здесь производство проводников ждёт очищенное серебро. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, conductor production awaits refined silver. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_silver_10
    Static(238910, MS('Привезите груз к точке %s0: обогатительная линия готовит новую партию урановой руды. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: an enrichment line is preparing a new uranium ore batch. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_uranium_01
    Static(238911, MS('Привезите груз к точке %s0: производство радиоактивного топлива пополняет запас сырья. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: radioactive-fuel production is replenishing feedstock. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_uranium_02
    Static(238912, MS('Привезите груз к точке %s0: переработчики урана ждут следующую загрузку. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: uranium processors await their next charge. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_uranium_03
    Static(238913, MS('Привезите груз к точке %s0: топливный цикл требует поставки уранового сырья. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the fuel cycle requires uranium feedstock. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_uranium_04
    Static(238914, MS('Привезите груз к точке %s0: участок подготовки руды освобождён под новую партию. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the ore preparation section is ready for a new batch. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roid_uranium_05
    Static(238915, MS('Пункт назначения — %s0. Здесь обогатительная линия готовит новую партию урановой руды. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, an enrichment line is preparing a new uranium ore batch. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_uranium_06
    Static(238916, MS('Пункт назначения — %s0. Здесь производство радиоактивного топлива пополняет запас сырья. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, radioactive-fuel production is replenishing feedstock. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_uranium_07
    Static(238917, MS('Пункт назначения — %s0. Здесь переработчики урана ждут следующую загрузку. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, uranium processors await their next charge. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_uranium_08
    Static(238918, MS('Пункт назначения — %s0. Здесь топливный цикл требует поставки уранового сырья. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the fuel cycle requires uranium feedstock. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_uranium_09
    Static(238919, MS('Пункт назначения — %s0. Здесь участок подготовки руды освобождён под новую партию. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the ore preparation section is ready for a new batch. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roid_uranium_10
    Static(238920, MS('Привезите груз к точке %s0: автономные добывающие установки проходят плановый ремонт. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: autonomous mining units are undergoing scheduled repairs. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roidminer_parts_01
    Static(238921, MS('Привезите груз к точке %s0: механики заменяют изношенные узлы астероидных добытчиков. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: mechanics are replacing worn asteroid-miner components. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roidminer_parts_02
    Static(238922, MS('Привезите груз к точке %s0: сервисная бригада собирает комплекты заводских запчастей. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a service team is assembling factory spare-part kits. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roidminer_parts_03
    Static(238923, MS('Привезите груз к точке %s0: добывающая техника готовится к следующему рабочему циклу. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: mining machinery is preparing for its next work cycle. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roidminer_parts_04
    Static(238924, MS('Привезите груз к точке %s0: резерв деталей нужен для сокращения простоя добывающих установок. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: spare parts are needed to reduce mining-unit downtime. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_roidminer_parts_05
    Static(238925, MS('Пункт назначения — %s0. Здесь автономные добывающие установки проходят плановый ремонт. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, autonomous mining units are undergoing scheduled repairs. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roidminer_parts_06
    Static(238926, MS('Пункт назначения — %s0. Здесь механики заменяют изношенные узлы астероидных добытчиков. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, mechanics are replacing worn asteroid-miner components. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roidminer_parts_07
    Static(238927, MS('Пункт назначения — %s0. Здесь сервисная бригада собирает комплекты заводских запчастей. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a service team is assembling factory spare-part kits. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roidminer_parts_08
    Static(238928, MS('Пункт назначения — %s0. Здесь добывающая техника готовится к следующему рабочему циклу. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, mining machinery is preparing for its next work cycle. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roidminer_parts_09
    Static(238929, MS('Пункт назначения — %s0. Здесь резерв деталей нужен для сокращения простоя добывающих установок. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, spare parts are needed to reduce mining-unit downtime. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_roidminer_parts_10
    Static(238930, MS('Привезите груз к точке %s0: плавильщики готовят партию вторичного металла. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: smelters are preparing a batch of recycled metal. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_scrap_metal_01
    Static(238931, MS('Привезите груз к точке %s0: производство базового сплава нуждается в металлическом ломе. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: basic-alloy production needs scrap metal. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_scrap_metal_02
    Static(238932, MS('Привезите груз к точке %s0: металл от разобранных кораблей возвращают в производственный цикл. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: metal from dismantled ships is returning to production. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_scrap_metal_03
    Static(238933, MS('Привезите груз к точке %s0: цех станционных панелей пополняет запас вторичного сырья. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the station-panel workshop is replenishing recycled feedstock. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_scrap_metal_04
    Static(238934, MS('Привезите груз к точке %s0: сортировочная линия готовит лом к переплавке. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the sorting line is preparing scrap for remelting. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_scrap_metal_05
    Static(238935, MS('Пункт назначения — %s0. Здесь плавильщики готовят партию вторичного металла. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, smelters are preparing a batch of recycled metal. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_scrap_metal_06
    Static(238936, MS('Пункт назначения — %s0. Здесь производство базового сплава нуждается в металлическом ломе. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, basic-alloy production needs scrap metal. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_scrap_metal_07
    Static(238937, MS('Пункт назначения — %s0. Здесь металл от разобранных кораблей возвращают в производственный цикл. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, metal from dismantled ships is returning to production. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_scrap_metal_08
    Static(238938, MS('Пункт назначения — %s0. Здесь цех станционных панелей пополняет запас вторичного сырья. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the station-panel workshop is replenishing recycled feedstock. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_scrap_metal_09
    Static(238939, MS('Пункт назначения — %s0. Здесь сортировочная линия готовит лом к переплавке. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the sorting line is preparing scrap for remelting. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_scrap_metal_10
    Static(238940, MS('Привезите груз к точке %s0: ремонтники заменяют повреждённую корабельную обшивку. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: repair crews are replacing damaged ship plating. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_shiphull_panels_01
    Static(238941, MS('Привезите груз к точке %s0: сборочный участок готовит корпуса небольших кораблей. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: an assembly section is preparing small-ship hulls. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_shiphull_panels_02
    Static(238942, MS('Привезите груз к точке %s0: ремонтные доки пополняют запас корпусных панелей. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: repair docks are replenishing hull panels. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_shiphull_panels_03
    Static(238943, MS('Привезите груз к точке %s0: изношенные секции обшивки готовят к замене. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: worn hull sections are due for replacement. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_shiphull_panels_04
    Static(238944, MS('Привезите груз к точке %s0: мастерские раскраивают панели под ремонт кораблей. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: workshops are cutting panels for ship repairs. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_shiphull_panels_05
    Static(238945, MS('Пункт назначения — %s0. Здесь ремонтники заменяют повреждённую корабельную обшивку. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, repair crews are replacing damaged ship plating. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_shiphull_panels_06
    Static(238946, MS('Пункт назначения — %s0. Здесь сборочный участок готовит корпуса небольших кораблей. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, an assembly section is preparing small-ship hulls. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_shiphull_panels_07
    Static(238947, MS('Пункт назначения — %s0. Здесь ремонтные доки пополняют запас корпусных панелей. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, repair docks are replenishing hull panels. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_shiphull_panels_08
    Static(238948, MS('Пункт назначения — %s0. Здесь изношенные секции обшивки готовят к замене. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, worn hull sections are due for replacement. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_shiphull_panels_09
    Static(238949, MS('Пункт назначения — %s0. Здесь мастерские раскраивают панели под ремонт кораблей. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, workshops are cutting panels for ship repairs. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_shiphull_panels_10
    Static(238950, MS('Привезите груз к точке %s0: плавильное оборудование готовят к плановому обслуживанию. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: smelting equipment is preparing for scheduled servicing. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_smelter_parts_01
    Static(238951, MS('Привезите груз к точке %s0: металлургический участок заменяет изношенные агрегаты. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a metallurgical section is replacing worn assemblies. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_smelter_parts_02
    Static(238952, MS('Привезите груз к точке %s0: ремонтная бригада восстанавливает оборудование плавильной линии. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a repair team is restoring smelting-line equipment. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_smelter_parts_03
    Static(238953, MS('Привезите груз к точке %s0: запасные узлы нужны между циклами переработки руды. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: spare assemblies are needed between ore-processing cycles. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_smelter_parts_04
    Static(238954, MS('Привезите груз к точке %s0: механики формируют резерв деталей для плавильных установок. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: mechanics are stocking spares for smelting installations. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_smelter_parts_05
    Static(238955, MS('Пункт назначения — %s0. Здесь плавильное оборудование готовят к плановому обслуживанию. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, smelting equipment is preparing for scheduled servicing. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_smelter_parts_06
    Static(238956, MS('Пункт назначения — %s0. Здесь металлургический участок заменяет изношенные агрегаты. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a metallurgical section is replacing worn assemblies. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_smelter_parts_07
    Static(238957, MS('Пункт назначения — %s0. Здесь ремонтная бригада восстанавливает оборудование плавильной линии. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a repair team is restoring smelting-line equipment. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_smelter_parts_08
    Static(238958, MS('Пункт назначения — %s0. Здесь запасные узлы нужны между циклами переработки руды. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, spare assemblies are needed between ore-processing cycles. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_smelter_parts_09
    Static(238959, MS('Пункт назначения — %s0. Здесь механики формируют резерв деталей для плавильных установок. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, mechanics are stocking spares for smelting installations. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_smelter_parts_10
    Static(238960, MS('Привезите груз к точке %s0: энергетики заменяют изношенные светочувствительные элементы. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: power crews are replacing worn photosensitive elements. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_solarplant_parts_01
    Static(238961, MS('Привезите груз к точке %s0: солнечные панели готовят к плановому обновлению. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: solar panels are preparing for scheduled renewal. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_solarplant_parts_02
    Static(238962, MS('Привезите груз к точке %s0: техники восстанавливают эффективность солнечной генерации. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: technicians are restoring solar-generation efficiency. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_solarplant_parts_03
    Static(238963, MS('Привезите груз к точке %s0: ремонтная группа собирает комплекты для обслуживания панелей. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a maintenance team is assembling panel-servicing kits. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_solarplant_parts_04
    Static(238964, MS('Привезите груз к точке %s0: солнечная установка пополняет запас заводских деталей. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a solar installation is replenishing factory spare parts. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_solarplant_parts_05
    Static(238965, MS('Пункт назначения — %s0. Здесь энергетики заменяют изношенные светочувствительные элементы. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, power crews are replacing worn photosensitive elements. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_solarplant_parts_06
    Static(238966, MS('Пункт назначения — %s0. Здесь солнечные панели готовят к плановому обновлению. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, solar panels are preparing for scheduled renewal. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_solarplant_parts_07
    Static(238967, MS('Пункт назначения — %s0. Здесь техники восстанавливают эффективность солнечной генерации. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, technicians are restoring solar-generation efficiency. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_solarplant_parts_08
    Static(238968, MS('Пункт назначения — %s0. Здесь ремонтная группа собирает комплекты для обслуживания панелей. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a maintenance team is assembling panel-servicing kits. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_solarplant_parts_09
    Static(238969, MS('Пункт назначения — %s0. Здесь солнечная установка пополняет запас заводских деталей. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a solar installation is replenishing factory spare parts. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_solarplant_parts_10
    Static(238970, MS('Привезите груз к точке %s0: монтажники ремонтируют наружную обшивку. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: assembly crews are repairing exterior plating. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_station_panels_01
    Static(238971, MS('Привезите груз к точке %s0: строительный участок собирает новые станционные секции. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a construction section is assembling new station sections. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_station_panels_02
    Static(238972, MS('Привезите груз к точке %s0: повреждённые стенки технических модулей требуют замены. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: damaged technical-module walls need replacement. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_station_panels_03
    Static(238973, MS('Привезите груз к точке %s0: склад ремонта конструкций пополняет запас прочных панелей. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: the structural repair store is replenishing strong panels. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_station_panels_04
    Static(238974, MS('Привезите груз к точке %s0: строители готовят материал для расширения модулей. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: construction crews are preparing material for module expansion. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_station_panels_05
    Static(238975, MS('Пункт назначения — %s0. Здесь монтажники ремонтируют наружную обшивку. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, assembly crews are repairing exterior plating. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_station_panels_06
    Static(238976, MS('Пункт назначения — %s0. Здесь строительный участок собирает новые станционные секции. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a construction section is assembling new station sections. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_station_panels_07
    Static(238977, MS('Пункт назначения — %s0. Здесь повреждённые стенки технических модулей требуют замены. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, damaged technical-module walls need replacement. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_station_panels_08
    Static(238978, MS('Пункт назначения — %s0. Здесь склад ремонта конструкций пополняет запас прочных панелей. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, the structural repair store is replenishing strong panels. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_station_panels_09
    Static(238979, MS('Пункт назначения — %s0. Здесь строители готовят материал для расширения модулей. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, construction crews are preparing material for module expansion. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_station_panels_10
    Static(238980, MS('Привезите груз к точке %s0: служба путей готовит ремонт колец торговой линии. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: lane maintenance is preparing repairs to trade-lane rings. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_tlr_parts_01
    Static(238981, MS('Привезите груз к точке %s0: повреждённые узлы торгового пути требуют замены. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: damaged trade-lane components need replacement. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_tlr_parts_02
    Static(238982, MS('Привезите груз к точке %s0: инженеры комплектуют резерв для восстановления движения. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: engineers are stocking spares to restore lane traffic. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_tlr_parts_03
    Static(238983, MS('Привезите груз к точке %s0: плановое обслуживание торговой линии ждёт запчастей. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: scheduled trade-lane servicing awaits spare parts. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_tlr_parts_04
    Static(238984, MS('Привезите груз к точке %s0: ремонтная бригада восстанавливает надёжность транспортного коридора. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: a maintenance team is restoring transport-corridor reliability. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_tlr_parts_05
    Static(238985, MS('Пункт назначения — %s0. Здесь служба путей готовит ремонт колец торговой линии. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, lane maintenance is preparing repairs to trade-lane rings. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_tlr_parts_06
    Static(238986, MS('Пункт назначения — %s0. Здесь повреждённые узлы торгового пути требуют замены. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, damaged trade-lane components need replacement. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_tlr_parts_07
    Static(238987, MS('Пункт назначения — %s0. Здесь инженеры комплектуют резерв для восстановления движения. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, engineers are stocking spares to restore lane traffic. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_tlr_parts_08
    Static(238988, MS('Пункт назначения — %s0. Здесь плановое обслуживание торговой линии ждёт запчастей. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, scheduled trade-lane servicing awaits spare parts. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_tlr_parts_09
    Static(238989, MS('Пункт назначения — %s0. Здесь ремонтная бригада восстанавливает надёжность транспортного коридора. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, a maintenance team is restoring transport-corridor reliability. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_tlr_parts_10
    Static(238990, MS('Привезите груз к точке %s0: заказчики ждут природную минеральную воду. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: customers await natural mineral water. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_water_extra_01
    Static(238991, MS('Привезите груз к точке %s0: салоны и рестораны пополняют запас воды из природных источников. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: lounges and restaurants are replenishing natural spring water. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_water_extra_02
    Static(238992, MS('Привезите груз к точке %s0: торговцы собирают заказы ценителей минеральной воды. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: merchants are assembling orders for mineral-water enthusiasts. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_water_extra_03
    Static(238993, MS('Привезите груз к точке %s0: гостевое хозяйство готовит запас натуральной воды. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: guest services are stocking natural water. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_water_extra_04
    Static(238994, MS('Привезите груз к точке %s0: поставщики распределяют бутилированную воду между постоянными клиентами. Приёмная смена уже получила накладную и ждёт состав.', 'Deliver the cargo to %s0: suppliers are allocating bottled water to regular customers. The receiving shift has the manifest and is expecting your train.')),  # TrainCourier brief_water_extra_05
    Static(238995, MS('Пункт назначения — %s0. Здесь заказчики ждут природную минеральную воду. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, customers await natural mineral water. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_water_extra_06
    Static(238996, MS('Пункт назначения — %s0. Здесь салоны и рестораны пополняют запас воды из природных источников. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, lounges and restaurants are replenishing natural spring water. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_water_extra_07
    Static(238997, MS('Пункт назначения — %s0. Здесь торговцы собирают заказы ценителей минеральной воды. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, merchants are assembling orders for mineral-water enthusiasts. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_water_extra_08
    Static(238998, MS('Пункт назначения — %s0. Здесь гостевое хозяйство готовит запас натуральной воды. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, guest services are stocking natural water. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_water_extra_09
    Static(238999, MS('Пункт назначения — %s0. Здесь поставщики распределяют бутилированную воду между постоянными клиентами. Диспетчер выделил место для приёма этой партии.', 'Your destination is %s0. Here, suppliers are allocating bottled water to regular customers. Dispatch has reserved space to receive this shipment.')),  # TrainCourier brief_water_extra_10
    Static(238270, MS('Диспетчер грузовых перевозок', 'Freight dispatcher')),  # TrainCourier title
    Static(238271, MS('Совершите стыковку с локомотивом.', 'Dock with the locomotive.')),  # TrainCourier board
    Static(238272, MS('Подцепите назначенный состав.', 'Couple the assigned wagons.')),  # TrainCourier pickup
    Static(238273, MS('Привезите груз к точке %s0 и отцепите состав.', 'Deliver the cargo to %s0 and uncouple the train.')),  # TrainCourier deliver
    Static(238274, MS('Припаркуйте локомотив в отмеченном месте у базы %s0.', 'Park the locomotive at the marked berth near %s0.')),  # TrainCourier park
    Static(238275, MS('Доставка оплачена. Продолжить работу?', 'Delivery paid. Continue working?')),  # TrainCourier continue
    Static(238276, MS('Вылетите в космос.', 'Launch into space.')),  # TrainCourier launch
    Static(238277, MS('Груз отцеплен. Подцепите его обратно.', 'Cargo detached. Couple the wagons again.')),  # TrainCourier recover
    Static(238278, MS('Есть работа для машиниста. Выберите начальный состав; каждый рейс оплачивается отдельно.', 'We need a train driver. Choose your starting train; each delivery is paid separately.')),  # TrainCourier offer
    Static(238279, MS('Берусь: 2 вагона.', 'Start with 2 wagons.')),  # TrainCourier accept
    Static(238280, MS('Берусь: 10 вагонов.', 'Start with 10 wagons.')),  # TrainCourier accept_10
    Static(238281, MS('Берусь: 20 вагонов.', 'Start with 20 wagons.')),  # TrainCourier accept_20
    Static(238282, MS('Не сейчас.', 'Not now.')),  # TrainCourier decline
    # Port UI: HUD and preferences. MS(Russian, English); keep numeric IDs stable.
    Static(238227, MS('Интерфейс', 'Interface')),  # Interface
    Static(238228, MS('Общее', 'General')),  # GeneralTab
    Static(238229, MS('Навигация', 'Navigation')),  # NavigationTab
    Static(238230, MS('Автопоказ радара', 'Show radar automatically')),  # RadarAuto
    Static(238231, MS('Автоматически открывать статус врага', 'Open enemy status automatically')),  # TargetAutoOpen
    Static(238232, MS('Автоматически показывать статус корабля', 'Show ship status automatically')),  # HealthAutoOpen
    Static(238233, MS('Включить автотурели', 'Enable auto turrets')),  # AutoTurrets
    Static(238234, MS('Резерв энергии автотурелей', 'Auto turret energy reserve')),  # AutoTurretReserve
    Static(238235, MS('Генератор маршрута', 'Route generator')),  # RouteGenerator
    Static(238236, MS('Автопролёт маршрута по F2', 'Follow route with F2')),  # RouteFollowF2
    Static(238237, MS('Автостыковка с базами', 'Auto-dock with bases')),  # AutoDock
    Static(238238, MS('Наклон HUD', 'HUD tilt')),  # HudTilt
    Static(238239, MS('Кнопки в статусе корабля', 'Ship status buttons')),  # ShipStatusButtons
    Static(238240, MS('Автовыбор элементов крупных кораблей', 'Capship subtarget autoselect')),  # CapshipAutoselect
    Static(238241, MS('Анимация крыльев на круизе', 'Wing animation in cruise')),  # CruiseWingAnimation
    Static(238242, MS('Анимация корабля', 'Ship animation')),  # ShipAnimation
    Static(238243, MS('Группы орудий', 'Weapon groups')),  # WeaponGroups
    Static(238244, MS('Стандартный', 'Standard')),  # Standard
    Static(238245, MS('Обход препятствий', 'Avoid obstacles')),  # AvoidObstacles
    Static(238246, MS('Нет', 'No')),  # RadarNever
    Static(238247, MS('При появлении любой цели', 'When any contact appears')),  # RadarAnyContact
    Static(238248, MS('При появлении противника', 'When an enemy appears')),  # RadarEnemy
    Static(238249, MS('Не удалось сохранить настройки', 'Could not save settings')),  # SettingsSaveFailed
    Static(238250, MS('Недоступно', 'Unavailable')),  # Unavailable
    Static(238251, MS('Тени', 'Shadows')),  # GraphicsShadows
    Static(238252, MS('Рельеф поверхностей', 'Surface relief')),  # GraphicsSurfaceRelief
    Static(238253, MS('Блики', 'Highlights')),  # GraphicsHighlights
    Static(238254, MS('Отражения', 'Reflections')),  # GraphicsReflections
    Static(238255, MS('Анизотропная фильтрация', 'Anisotropic filtering')),  # GraphicsAnisotropy
    Static(238256, MS('Сглаживание', 'Antialiasing')),  # GraphicsAntialiasing
    Static(238257, MS('Объёмные туманности', 'Volumetric nebulae')),  # GraphicsNebulae
    Static(238258, MS('Вертикальная синхронизация', 'Vertical sync')),  # GraphicsVsync
    Static(238259, MS('Лимит FPS', 'FPS limit')),  # GraphicsFpsLimit
    Static(238260, MS('Выкл', 'Off')),  # GraphicsOff
    Static(238261, MS('Вкл', 'On')),  # GraphicsOn
    Static(238262, MS('Низкое', 'Low')),  # GraphicsLow
    Static(238263, MS('Среднее', 'Medium')),  # GraphicsMedium
    Static(238264, MS('Высокое', 'High')),  # GraphicsHigh
    Static(238265, MS('Изменения вступят в силу после перезапуска игры', 'Changes take effect after restarting the game')),  # GraphicsRestartPending
    Static(238266, MS('Эти настройки применяются после перезапуска игры', 'These settings apply after restarting the game')),  # GraphicsRestartHint

    Static(238226, MS('Нажми Enter, чтобы пропустить катсцену', 'Press Enter to skip the cutscene')),  # CutsceneSkipPrompt
    Static(238225, MS('Список целей', 'Target list')),  # TargetList
    # HUD: Targeting / Health. MS(Russian, English); keep numeric IDs stable.
    Static(238200, MS('Показать/скрыть окно цели', 'Show/hide target window')),  # TargetWindow
    Static(238201, MS('Зафиксировать состояние окна цели', 'Lock target window open/closed state')),  # TargetLock
    Static(238202, MS('Разрешить автоматическое открытие и скрытие окна цели', 'Enable automatic target window opening and hiding')),  # TargetUnlock
    Static(238203, MS('Включить выбор деталей под курсором', 'Enable subsystem selection under the cursor')),  # AutoselectEnable
    Static(238204, MS('Отключить выбор деталей под курсором', 'Disable subsystem selection under the cursor')),  # AutoselectDisable
    Static(238205, MS('Цель: стандартный вид', 'Target: standard view')),  # TargetVanilla
    Static(238206, MS('Цель: вписать в окно', 'Target: fit to window')),  # TargetFit
    Static(238207, MS('Цель: вид сверху', 'Target: top view')),  # TargetTop
    Static(238208, MS('Цель: вид справа', 'Target: right view')),  # TargetRight
    Static(238209, MS('Закрыть окно цели', 'Close target window')),  # TargetClose
    Static(238210, MS('Показать/скрыть состояние корабля', 'Show/hide ship status')),  # HealthWindow
    Static(238211, MS('Запретить открытие окна при повреждениях', 'Disable opening on ship damage')),  # HealthLock
    Static(238212, MS('Разрешить открытие окна при повреждениях', 'Enable opening on ship damage')),  # HealthUnlock
    Static(238213, MS('Сложить/разложить крылья', 'Fold/unfold wings')),  # WingPlay
    Static(238214, MS('Продолжить движение крыльев', 'Resume wing animation')),  # WingResume
    Static(238215, MS('Приостановить движение крыльев', 'Pause wing animation')),  # WingPause
    Static(238216, MS('Отключить автоматическое движение крыльев на круизе', 'Disable automatic cruise wing animation')),  # WingLock
    Static(238217, MS('Включить автоматическое движение крыльев на круизе', 'Enable automatic cruise wing animation')),  # WingUnlock
    Static(238218, MS('Корабль: вид сверху', 'Ship: top view')),  # HealthTop
    Static(238219, MS('Корабль: вид слева', 'Ship: left view')),  # HealthLeft
    Static(238220, MS('Закрыть окно состояния корабля', 'Close ship status window')),  # HealthClose
    Static(238221, MS('Группа орудий 1', 'Weapon group 1')),  # WeaponGroup1
    Static(238222, MS('Группа орудий 2', 'Weapon group 2')),  # WeaponGroup2
    Static(238223, MS('Группа орудий 3', 'Weapon group 3')),  # WeaponGroup3
    Static(238224, MS('Показать список орудий', 'Show weapon list')),  # WeaponList

    # Static(196850, 'Рейнландская империя'),
    # Static(196851, 'Промышленность Дауманн'),
    # Static(196852, 'Гессенцы'),
    # Static(196853, 'Республика Либерти'),
    # Static(196854, 'Корпорация ДипСпейс'),
    # Static(196855, 'Бродяги Либерти'),
    # Static(196856, 'Королевство Бретония'),
    # Static(196857, 'Королевские перевозки'),
    # Static(196858, 'Ирландская республиканская армия'),
    # Static(196859, 'Сёгунат Кусари'),
    # Static(196860, 'Киширо'),
    # Static(196861, 'Клан Синоби'),
    # Static(196862, 'Испанские Корсары'),
    # Static(196863, 'Испанские Изгои'),
    # Static(196864, 'Гильдия наёмников'),
    # Static(196865, 'Торговая федерация'),
    # Static(196866, 'Пираты'),
    # Static(196867, 'Отшельники'),
    # Static(196868, 'Банда Старлайна'),
    # Static(196869, 'Номады'),
    # Static(196870, 'Служба безопасности Альянса'),
    # Static(196871, 'Орден'),
    # Static(196878, 'Мусорщики'),
    # Static(196885, 'Люди Дитриха'),
    # Static(196886, 'РЕЙНЛАНД'),
    # Static(196887, 'ЛИБЕРТИ'),
    # Static(196888, 'БРЕТОНИЯ'),
    # Static(196889, 'КУСАРИ'),
    #
    # Static(210100, 'Рейнландская империя'),
    # Static(210101, 'Промышленность Дауманн'),
    # Static(210102, 'Гессенцы'),
    # Static(210103, 'Республика Либерти'),
    # Static(210104, 'Корпорация ДипСпейс'),
    # Static(210105, 'Бродяги Либерти'),
    # Static(210106, 'Королевство Бретония'),
    # Static(210107, 'Королевские перевозки'),
    # Static(210108, 'Ирландская республиканская армия'),
    # Static(210109, 'Сёгунат Кусари'),
    # Static(210110, 'Киширо'),
    # Static(210111, 'Клан Синоби'),
    # Static(210112, 'Испанские Корсары'),
    # Static(210113, 'Испанские Изгои'),
    # Static(210114, 'Гильдия наёмников'),
    # Static(210115, 'Торговая федерация'),
    # Static(210116, 'Пираты'),
    # Static(210117, 'Номады'),
    # Static(210120, 'Банда Старлайна'),
    # Static(210122, 'Служба безопасности Альянса'),
    # Static(210123, 'Орден'),
    # Static(210121, 'Мусорщики'),
    # Static(210124, 'Люди Дитриха'),
    #
    # Static(210300, 'Рейнланд'),
    # Static(210301, 'Дауманн'),
    # Static(210302, 'Гессенцы'),
    # Static(210303, 'Либерти'),
    # Static(210304, 'ДипСпейс'),
    # Static(210305, 'Бродяги'),
    # Static(210306, 'Бретония'),
    # Static(210307, 'Королевские перевозки'),
    # Static(210308, 'ИРА'),
    # Static(210309, 'Кусари'),
    # Static(210310, 'Киширо'),
    # Static(210311, 'Синоби'),
    # Static(210312, 'Корсары'),
    # Static(210313, 'Изгои'),
    # Static(210314, 'Наёмники'),
    # Static(210315, 'Торговцы'),
    # Static(210316, 'Пираты'),
    # Static(210320, 'Старлайн'),
    # Static(210317, 'Номады'),
    # Static(210322, 'СБА'),
    # Static(210323, 'Орден'),
    # Static(210330, 'Мусорщики'),
    # Static(210337, 'Люди Дитриха'),

    Static(190000, MS('РЕЙНЛАНД', 'RHEINLAND')),
    Static(190001, MS('ЛИБЕРТИ', 'LIBERTY')),
    Static(190002, MS('БРЕТОНИЯ', 'BRETONIA')),
    Static(190003, MS('КУСАРИ', 'KUSARI')),



    Static(238100, MS('Гиперврата в Большой Омикрон', 'Jumpgate to Omicron Major')),
    Static(238101, MS('Гиперврата в Малый Омикрон', 'Jumpgate to Omicron Minor')),
    Static(238102, MS('Гиперврата на Мальту', 'Jumpgate to Malta')),
    Static(238103, MS('Гипердыра в Омегу-13', 'Jumphole to Omega-13')),
    Static(238104, MS('Планета Мальта', 'Planet Malta')),
    Static(238105, MS('Станция Гавана', "Havana Station")),
    Static(238106, MS('Фрипорт Тринидад', 'Freeport Trinidad')),
    Static(238107, MS('Планета Эрбо', 'Planet Erba')),
    Static(238108, MS('Планета Тахо', 'Planet Tahoe')),
    Static(238109, MS('База Тортуга', 'Tortuga Base')),
    Static(238110, MS('Станция Замора', 'Zamora Station')),
    Static(238111, MS('Платформа Магента', 'Magentha Platform')),
    Static(238112, MS('Планета Теруэл', 'Planet Teruel')),
    Static(238115, MS('Чёрная дыра', 'Black hole')),
    Static(238116, MS('Звезда', 'Star')),
    Static(238117, MS('Стыковочное кольцо', 'Docking ring')),
    Static(238118, MS('Стыковочный узел', 'Docking point')),

    Static(238119, MS('Гипердыра в Сигму-8', 'Jumphole to Sigma-8')),

    Static(238120, MS('Турель', 'Turret')),
    Static(238121, MS('Торпедная установка', 'Torpedo Launcher')),
    Static(238122, MS('Торпеда', 'Torpedo')),
    Static(238123, MS('Бомба', 'Bomb')),
    Static(238124, MS('ЭМИ', 'EMI')),

    Static(238125, MS('База Рапануи', 'Rapa Nui Base')),
    Static(238126, MS('Аванпост', 'Outpost')),
    Static(238127, MS('Орудийная платформа', 'Weapon platform')),
    Static(238128, MS('Станция Страсбург', 'Strasbourg station')),
    Static(238129, MS('Станция Вена', 'Vienna station')),
    Static(238130, MS('Гипервата в Вавилон', 'Jumpgate to Babylon')),
    Static(238131, MS('Гипервата в Омегу-7', 'Jumpgate to Omega-7')),
    Static(238132, MS('Гипервата в Сириус', 'Jumpgate to Sirius')),
    Static(238133, MS('Гипервата в Энтерпрайз', 'Jumpgate to Enterprise')),
    Static(238134, MS('Гипервата в Вену', 'Jumpgate to Vienna')),

    Static(238135, MS('Планета Терра', 'Planet Terra')),
    Static(238136, MS('Верфь Ордена', 'Order\'s Shipyard')),
    Static(238137, MS('Терраформирующая станция', 'Terraforming station')),
    Static(238138, MS('Станция Вавилон', 'Babylon station')),
    Static(238139, MS('Логово Номадов', 'Nomad Lair')),
    Static(238140, MS('Шлюз Логова Номадов', 'Nomad Lair Airlock')),
    Static(238141, MS('Обломки корабля', 'Ship Wreck')),
    Static(238142, MS('Исследовательская станция', 'Research station')),
    Static(238143, MS('Станция Энтерпрайз', 'Enterprise station')),
    Static(238144, MS('Станция Прометей', 'Prometheus station')),
    Static(238145, MS('Гипердыра в Тау-44', 'Jumphole to Tau-44')),
    Static(238146, MS('Линкор Либерти', 'Liberty Dreadnought')),

    Static(238150, MS(
        ('Торговые линии используются для ускорения торговых маршрутов. Они позволяют разгоняться до внушительных скоростей, но с учетом, что надо лететь только по указанной траектории. '
        ' Это делает все торговые маршруты в Сириусе гораздо быстрее, но имеет негативный эффект в том плане, что торговые линии являются предметом интереса различных пиратов. При этом сам торговые пути достигли максимума своего развития даже в текущем виде. '
         'В Либерти были разработаны более современные торговые линии, но они так и не вошли в серию, т.к. к тому моменту уже были улучшены круизные двигатели обычных кораблей и замена торговых линий на более современную версию стало не целесообразным.'),
        ('Trade lanes are used to accelerate trade routes. They allow travel at impressive speeds, but only along a fixed trajectory. '
         'This makes all trade routes in Sirius much faster, but has the negative effect of making trade lanes a target for various pirates. Yet, the trade routes themselves have reached the peak of their development even in their current form. '
         'In Liberty, more modern trade lanes were developed, but they never entered series production because, by that time, the cruise engines of regular ships had already been improved, making the replacement of trade lanes with a more modern version impractical.')
    )),
    Static(238151, MS('Торговая линия', 'Trade Lane')),

    Static(238152, MS(
        'Стыковочный пирс предназначен для крупных кораблей, планирующих получить обслуживание с помощью персонала с планеты. Например, пришвартованные транспорты ожидают, как будут разгружены или загружены новыми товарами.',
        'The docking pier is intended for large ships planning to receive service from planet-side personnel. For example, docked transports await being unloaded or loaded with new goods.'
    )),
    Static(238153, MS(
        'Гиперврата – основное средство перемещения между системами. Личные варп-двигатели так и не смогли дойти до достаточно малого размера, чтобы их можно было легко устанавливать на малые корабли. Гиперврата в свою очередь позволяют абсолютно любому кораблю переместиться в соседнюю систему, поэтому еще долго не потеряют свою популярность.    ',
        'Hyperspace gates are the primary means of travel between systems. Personal warp drives never achieved a sufficiently small size to be easily installed on small ships. Hyperspace gates, in turn, allow absolutely any ship to travel to a neighboring system, thus they will not lose their popularity for a long time.'
    )),
    Static(238154, MS(
        'Гипераномалии являются менее стабильными аналогами гиперврат, и по большей части используются пиратами и корсарами. Для активации гипераномалий нужно куда меньше средств, но только некоторые из них могут доставить в нужное место.',
        'Hyperspace anomalies are less stable analogues of hyperspace gates, and are mostly used by pirates and corsairs. Activating hyperspace anomalies requires far fewer resources, but only some of them lead to the desired destination.'
    )),







    # Static(238119, MS('Звезда', 'Star')),
]
