from universe.audio.pilot_line import PilotLine as L
from universe.audio import parse_rule as R
from universe.audio.base_pilot import BaseIdentifiedVoice
from universe.audio.static import dispatcher as dispatcher_static

from text.strings import MultiString as MS


class StationDispatcher(BaseIdentifiedVoice):
    VOICE_DATA = dispatcher_static.VOICE_DATA
    MVOICE_AUDIO_PROP = dispatcher_static.MVOICE_AUDIO_PROP
    MVOICE_MISSION_PROP = dispatcher_static.MVOICE_MISSION_PROP
    LINES = [
        L('gcs_combat_announce_allclear_01-', 'Противников в радиусе базы не обнаружено'),
        L('gcs_combat_announce_allclear_02-', 'Бандитов в ближайшем радиусе не обнаруженов'),
        L('gcs_combat_announce_allclear_03-', 'Противников в ближайшем радиусе не обнаружено'),
        L('gcs_combat_announce_engage_01-', 'Внимание, обнаружены противники. Всем кораблям, срочно на перехват', R.RuleHighAction),
        L('gcs_combat_announce_engage_02-', 'Неприятель рядом с базой. Всем подготовиться к обороне', R.RuleHighAction),
        L('gcs_combat_announce_engage_03-', 'Всем кораблям! Обнаружен неприятель! Код красный, приготовиться к обороне!', R.RuleHighAction),
        L('gcs_combat_announce_engage_04-', 'Приготовиться к обороне! Обнаружен неприятель в зоне видимости базы!', R.RuleHighAction),
        L('gcs_combat_attentionallunits_01-', 'Внимание всем ближайшим контактам!', R.RuleHighAction),
        L('gcs_combat_attentionallunits_02-', 'Внимание всем кораблям в радиусе базы!', R.RuleHighAction),
        L('gcs_combat_manturrets_01-', 'Активировать защитный периметр!', R.RuleHighAction),
        L('gcs_combat_manturrets_02-', 'Активировать защитные турели!', R.RuleHighAction),
        L('gcs_combat_manturrets_03-', 'Приказ активировать защитные системы!', R.RuleHighAction),
        L('gcs_combat_manturrets_04-', 'Запустить защитные системы!', R.RuleHighAction),
        L('gcs_dhail_mbid_patrol_ill', 'налётчики', R.RuleShipTypeHail),
        L('gcs_dhail_mbid_patrol_leg', 'патруль', R.RuleShipTypeHail),
        L('gcs_dhail_mbid_patrollers_ill', 'налётчики', R.RuleShipTypeHail),
        L('gcs_dhail_mbid_patrollers_leg', 'патруль', R.RuleShipTypeHail),
        L('gcs_dhail_mbid_trader_ill', 'торговец', R.RuleShipTypeHail),
        L('gcs_dhail_mbid_trader_leg', 'торговец', R.RuleShipTypeHail),
        L('gcs_dhail_mbid_traders_ill', 'конвой', R.RuleShipTypeHail),
        L('gcs_dhail_mbid_traders_leg', 'конвой', R.RuleShipTypeHail),
        L('gcs_dhail_nopermission_01-', 'у вас нет разрешение на стыковку, я приказываю вам прекратить ман+ёвр.', R.RuleStartAsk),
        L('gcs_dockhail_dock_hailmethod_01-', 'мы видим вас на радаре', R.RuleMiddleAsk),
        L('gcs_dockhail_dock_hailmethod_02-', 'вы в зоне видимости нашего радара', R.RuleMiddleAsk),
        L('gcs_dockhail_dock_hailmethod_03-', 'вы в зоне сканирования', R.RuleMiddleAsk),
        L('gcs_dockhail_dock_hailmethod_04-', 'мы сканируем ваше направления движения', R.RuleMiddleAsk),
        L('gcs_dockhail_dock_hailmethod_05-', 'мы фиксируем ваше передвижение', R.RuleMiddleAsk),
        L('gcs_dockhail_dock_hailmethod_06-', 'мы перехватили ваше движение нашим радаром', R.RuleMiddleAsk),
        L('gcs_dockhail_dock_hailmethod_07-', 'наш радар фиксирует ваше перемещение', R.RuleMiddleAsk),
        L('gcs_dockhail_dock_idreq_01-', 'укажите направление вашего движения', R.RuleStartAsk),
        L('gcs_dockhail_dock_idreq_02-', 'укажите финальную точку вашего движения', R.RuleStartAsk),
        L('gcs_dockhail_dock_idreq_03-', 'перешлите нам ваш идентификатор и направление движения', R.RuleStartAsk),
        L('gcs_dockhail_dock_incoming+', 'Обращаюсь', R.RuleIncomingFighter),
        L('gcs_dockhail_dock_transreceived_01+', 'ваше сообщение принято', R.RuleMiddleAsk),
        L('gcs_dockhail_dock_transreceived_02+', 'ваши данные приняты', R.RuleMiddleAsk),
        L('gcs_dockhail_dock_whereheaded_01+', 'куда вы направляетесь', R.RuleStartAsk),
        L('gcs_dockhail_dock_whereheaded_02+', 'в какую точку вы движетесь', R.RuleStartAsk),
        L('gcs_docklaunch_clear_berth_01-', 'Вам разрешен взлёт', R.RuleGoodLuck),
        L('gcs_docklaunch_clear_berth_02-', 'Разрешаю взлёт', R.RuleGoodLuck),
        L('gcs_docklaunch_clear_berth_03-', 'Ваш взлёт разрешен', R.RuleGoodLuck),
        L('gcs_docklaunch_clear_berth_04-', 'Открываем шлюз, взлёт разрешен', R.RuleGoodLuck),
        L('gcs_docklaunch_clear_berth_05-', 'Разрешаем взлёт через шлюзовой отс+ек', R.RuleGoodLuck),
        L('gcs_docklaunch_clear_moor_01-', 'Вы отсоединены от причала', R.RuleGoodLuck),
        L('gcs_docklaunch_clear_moor_02-', 'Причал деактивирован', R.RuleGoodLuck),
        L('gcs_docklaunch_clear_moor_03-', 'Вам разрешено отчалить', R.RuleGoodLuck),
        L('gcs_docklaunch_clear_moor_04-', 'Приступайте к отшвартовке', R.RuleGoodLuck),
        L('gcs_docklaunch_clear_moor_05-', 'Начинайте отшвартовку', R.RuleGoodLuck),
        L('gcs_docklaunch_clear_ring_01-', 'Вы успешно вышли из стыковочного кольц+а', R.RuleGoodLuck),
        L('gcs_docklaunch_clear_ring_02-', 'Выход из планетарного кольц+а проведен успешно', R.RuleGoodLuck),
        L('gcs_docklaunch_clear_ring_03-', 'Вы успешно покинули планетарное кольцо', R.RuleGoodLuck),
        L('gcs_docklaunch_clear_ring_04-', 'Вы провели выход из стыковочного кольц+а', R.RuleGoodLuck),
        L('gcs_docklaunch_clear_ring_05-', 'Проход через стыковочное кольцо проведен успешно', R.RuleGoodLuck),
        L('gcs_dockrequest_delayedreason_01-', 'Очередь на стыковку переполнена', R.RuleGoodLuck),
        L('gcs_dockrequest_delayedreason_02-', 'Нет доступных точек для стыковки', R.RuleGoodLuck),
        L('gcs_dockrequest_delayedreason_03-', 'Все точки стыковки заняты', R.RuleGoodLuck),
        L('gcs_dockrequest_denied_01-', 'отклонён', R.RuleDockRequestResult),
        L('gcs_dockrequest_granted_01-', 'разрешен', R.RuleDockRequestResult),
        L('gcs_dockrequest_nofit_01-', 'Мы не можем обеспечить стыковку кораблей вашего размера', R.RuleStartAsk),
        L('gcs_dockrequest_nowcleared_01+', 'Теперь ваш доступ разрешён', R.RuleClearTo),
        L('gcs_dockrequest_proceed_01+', 'Можете приступать', R.RuleProceedToDock),
        L('gcs_dockrequest_responsehostile_01-', 'Запрос отклонён, вам запрещено находиться в этой зоне', R.RuleStartAskAngry),
        L('gcs_dockrequest_standby_01-', 'Пожалуйста, ожидайте', R.RuleGoodLuck),
        L('gcs_dockrequest_todock', 'к стыковке к узлу номер', R.RuleGrantedDockNumber),
        L('gcs_dockrequest_todock-', 'к стыковке к узлу номер', R.RuleGrantedDockNumber),
        L('gcs_dockrequest_todock_number', 'к стыковке к узлу номер', R.RuleGrantedDockNumber),
        L('gcs_dockrequest_todock-', 'Стыковаться', R.RuleGrantedDock),
        L('gcs_dockrequest_toland', 'к посадке на узел', R.RuleGrantedDockNumber),
        L('gcs_dockrequest_toland-', 'Садиться', R.RuleGrantedDock),
        L('gcs_dockrequest_tomoor', 'к швартовке на причал', R.RuleGrantedDockNumber),
        L('gcs_dockrequest_tomoor_number', 'к швартовке на причал', R.RuleGrantedDockNumber),
        L('gcs_dockrequest_tomoor-', 'Швартоваться', R.RuleGrantedDock),
        L('gcs_dockrequest_willbecleared_01-', 'Вы сможете продолжить, как только ваш место для стыковки освободится', R.RuleStartAsk),
        L('gcs_dockrequest_willbecleared_02-', 'Мы разрешим вам приступить к стыковке, когда ваше место будет свободно', R.RuleStartAsk),
        L('gcs_dockrequest_willbecleared_03-', 'Вы сможете продолжить стыковку, когда до вас дойдёт очередь', R.RuleStartAsk),
        L('gcs_dockrequest_yourrequest+', 'Ваш запрос', R.RuleYourRequest),
        L('gcs_misc_ack_01-', 'Подтверждаю', R.RuleAcknowledge),
        L('gcs_misc_ack_02-', 'Допуск подтвержден', R.RuleAcknowledge),
        L('gcs_misc_ack_03-', 'Подтверждено', R.RuleAcknowledge),

        L('gcs_misc_dash', 'дэш', R.RuleDash),
        L('gcs_misc_thisis+', 'говорит', R.RuleThisIs),
        L('gcs_misc_to', 'к', R.RuleTo),

        L('gcs_misc_wellwish_01-', 'Удачных полётов', R.RuleStartAsk),
        L('gcs_misc_wellwish_02-', 'Удачи', R.RuleStartAsk),
        L('gcs_misc_wellwish_03-', 'Успешных полётов', R.RuleStartAsk),
        L('gcs_misc_wellwish_04-', 'В добрый путь', R.RuleStartAsk),

        L('gcs_refer_shiparch_lfighter', 'лёгкому истребителю', R.RuleShipAsk),
        L('gcs_refer_shiparch_hfighter', 'тяжелому истребителю', R.RuleShipAsk),
        L('gcs_refer_shiparch_atransport', 'бронированному транспорту', R.RuleShipAsk),

        L('gcs_refer_shiparch_bhlf', 'Пиранья', R.RuleShipAskFighter),
        L('gcs_refer_shiparch_bhhf', 'Барракуда', R.RuleShipAskFighter),
        L('gcs_refer_shiparch_bhvhf', 'Рыба-молот', R.RuleShipAskFighter),

        L('gcs_refer_shiparch_borf', 'Дром+адер', R.RuleShipAskFreighter),
        L('gcs_refer_shiparch_borhf', 'Стилет', R.RuleShipAskFighter),
        L('gcs_refer_shiparch_borvhf', 'Сабля', R.RuleShipAskFighter),
        L('gcs_refer_shiparch_borlf', 'Кинжал', R.RuleShipAskFighter),
        L('gcs_refer_shiparch_Breb', 'линкору Брет+онии', R.RuleShipAsk),
        L('gcs_refer_shiparch_Bred', 'эсминцу Брет+онии', R.RuleShipAsk),
        L('gcs_refer_shiparch_Bref', 'Кл+ейндсаль', R.RuleShipAskFreighter),
        L('gcs_refer_shiparch_Breg', 'канонерке Брет+онии', R.RuleShipAsk),
        L('gcs_refer_shiparch_Brehf', 'Крестоносец', R.RuleShipAskFighter),
        L('gcs_refer_shiparch_Brelf', 'Кавалер', R.RuleShipAskFighter),
        L('gcs_refer_shiparch_ctransport', 'транспортному п+оезду', R.RuleShipAsk),
        L('gcs_refer_shiparch_hlifter', 'тяжелому погрузчику', R.RuleShipAsk),
        L('gcs_refer_shiparch_htransport', 'тяжелому транспортному судну', R.RuleShipAsk),
        L('gcs_refer_shiparch_Kusb', 'линкору Кус+ари', R.RuleShipAsk),
        L('gcs_refer_shiparch_Kusd', 'эсминцу Кус+ари', R.RuleShipAsk),
        L('gcs_refer_shiparch_Kusf', 'Дрон', R.RuleShipAskFreighter),
        L('gcs_refer_shiparch_Kusg', 'канонерке Кус+ари', R.RuleShipAsk),
        L('gcs_refer_shiparch_Kushf', 'Дракон', R.RuleShipAskFighter),
        L('gcs_refer_shiparch_Kuslf', 'Дрэйк', R.RuleShipAskFighter),
        L('gcs_refer_shiparch_Libb', 'линкору Л+иберти', R.RuleShipAsk),
        L('gcs_refer_shiparch_Libc', 'крейсеру Л+иберти', R.RuleShipAsk),
        L('gcs_refer_shiparch_Libf', 'Носорог', R.RuleShipAskFreighter),
        L('gcs_refer_shiparch_Libhf', 'Защитник', R.RuleShipAskFighter),
        L('gcs_refer_shiparch_Liblf', 'Патриот', R.RuleShipAskFighter),
        L('gcs_refer_shiparch_ordhf', 'Ан+убис', R.RuleShipAskFighter),
        L('gcs_refer_shiparch_pirf', 'Мул', R.RuleShipAskFreighter),
        L('gcs_refer_shiparch_pirhf', 'Волкодав', R.RuleShipAskFighter),
        L('gcs_refer_shiparch_pirlf', 'Гончая', R.RuleShipAskFighter),
        L('gcs_refer_shiparch_repair', 'ремонтному кораблю', R.RuleShipAsk),
        L('gcs_refer_shiparch_Rheb', 'линкору Р+ейнланда', R.RuleShipAsk),
        L('gcs_refer_shiparch_Rhed', 'крейсеру Р+ейнланда', R.RuleShipAsk),
        L('gcs_refer_shiparch_Rhef', 'Горбун', R.RuleShipAskFreighter),
        L('gcs_refer_shiparch_Rheg', 'канонерке Р+ейнланда', R.RuleShipAsk),
        L('gcs_refer_shiparch_Rhehf', 'Валькирия', R.RuleShipAskFighter),
        L('gcs_refer_shiparch_Rhelf', 'Баньш+и', R.RuleShipAskFighter),
        L('gcs_refer_shiparch_starblazer', 'Элитный Звездолёт', R.RuleShipAskFighter),
        L('gcs_refer_shiparch_starflier', 'Звездолёт', R.RuleShipAskFighter),
        L('gcs_refer_shiparch_startracker', 'Звёздный буксир', R.RuleShipAskFighter),
        L('gcs_refer_shiparch_gf4', 'Ястреб', R.RuleShipAskFighter),
        L('gcs_refer_shiparch_gf5', 'Сокол', R.RuleShipAskFighter),
        L('gcs_refer_shiparch_gf6', 'Орёл', R.RuleShipAskFighter),
        L('gcs_refer_shiparch_colf', 'Легионер', R.RuleShipAskFighter),
        L('gcs_refer_shiparch_cohf', 'Центурион', R.RuleShipAskFighter),
        L('gcs_refer_shiparch_covhf', 'Титан', R.RuleShipAskFighter),
        L('gcs_refer_shiparch_stransport', 'длинному транспортному судну', R.RuleShipAsk),
        L('gcs_refer_shiparch_support', 'судну поддержки', R.RuleShipAsk),
        #
        # L('gcs_refer_shiparch_luxliner', ''),
        # L('gcs_refer_shiparch_mining', ''),
        # L('gcs_refer_shiparch_pliner', ''),

        L('gcs_refer_faction_rh_short', 'Р+эйнланд', R.RuleFaction),
        L('gcs_refer_faction_rx_short', 'Г+ессенцы', R.RuleFaction),
        L('gcs_refer_faction_test_short', 'Фракция', R.RuleFaction),
        L('gcs_refer_faction_player_short', 'Фрил+ансер', R.RulePlayer),

        L('mod_refer_base_freeport-', 'точка фрипорт', R.RuleBase),
        L('mod_refer_base_prison-', 'точка тюрьма', R.RuleBase),
        L('mod_refer_base_outpost-', 'точка аванпост', R.RuleBase),
        L('mod_refer_base_battleship-', 'точка линкор', R.RuleBase),
        L('mod_refer_base_military-', 'точка военная база', R.RuleBase),
        L('mod_refer_base_research-', 'точка исследовательская станция', R.RuleBase),
        L('mod_refer_base_shipyard-', 'точка верфь', R.RuleBase),
        L('mod_refer_base_factory-', 'точка фабрика', R.RuleBase),
        L('mod_refer_base_station-', 'точка станция', R.RuleBase),
        L('mod_refer_base_border-', 'точка пограничный аванпост', R.RuleBase),

        L('mod_refer_base_liner-', MS('лайнер', 'liner'), R.RuleBase),
        L('mod_refer_base_roid_miner-', MS('добывающее судно', 'Roid Miner'), R.RuleBase),
        L('mod_refer_base_gas_miner-', MS('газодобытчик', 'Gas Miner'), R.RuleBase),
        L('mod_refer_base_solar_plant-', MS('солнечный генератор', 'Solar Plant'), R.RuleBase),
        L('mod_refer_base_research_base-', MS('исследовательская база', 'Research Base'), R.RuleBase),
    ]

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)


class MaleDispatcher(StationDispatcher):
    STEOS_ID = 294  # lebedev, stalker
    FOLDER = 'dispatcher01'
    ATTENUATION = -4


class FemaleDispatcher(StationDispatcher):
    STEOS_ID = 175  # Tracer ?
    FOLDER = 'dispatcher02'
    IS_MALE = False
    ATTENUATION = -4


class FemaleRoboDispatcher(StationDispatcher):
    STEOS_ID = 175  # Tracer ?
    FOLDER = 'dispatcher03'
    IS_MALE = False
    ATTENUATION = -4
