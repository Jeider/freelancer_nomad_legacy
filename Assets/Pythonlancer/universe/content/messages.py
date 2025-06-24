from random import choice
from text.dividers import SINGLE_DIVIDER


CONSUMER_TRADER = ('Я торговец из {from}. Прилетел сюда за {comm}. Мы нуждаемся в этом товаре. '
                   'Я могу тебе показать местоположение {from} за {credits}')
CONSUMER_RUMOR = ('Товар {comm} очень хорошо продается на станции {destination}. '
                  'Я могу тебе показать где это находится за {credits}')

TRADING_BASE_PROMOTER = ('Я прилет на эту базу с тороговой станции {tradingbase}. '
                         'Это большая база разнообразных товаров, которые мы продаем по адекватным ценам. '
                         'Можешь прилететь и посмотреть на наши товары. Могу показать местоположение '
                         '{tradingbase} за {credits}')

RESELLER_FROM = ('На этой базе я продал товар {comm}, который я привез из {from}. Сейчас я загружусь и полечу '
                 'обратно. Если тебе интересно, где находится {from}, то могу показать ')
RESELLER_TO = ('Я прилетел на эту базу, чтобы перепродать {comm}. Я его повезу на {to}. Если не знаешь, '
               'где это, то могу показать ')

PRODUCER_REQUIREMENTS_BEST = ('Эта база является поставщиком {comm}. Но мы нуждаемся в {component}, чтобы продолжать '
                              'его поставки. Могу показать, где дешевле всего купить {component} за {credits}')
PRODUCER_REQUIREMENTS_NEAR = ('Эта база является поставщиком {comm}. Но мы нуждаемся в {component}, чтобы продолжать '
                              'его поставки. Могу показать, где ближе всего купить {component} за {credits}')

PRODUCER_BEST = ('Эта база лучший поставщик {product}. Это лучшая цена в секторе Сириуса')
PRODUCER_ANY = ('Эта база поставляет {product}. Это не лучшая цена, но определённо хорошее предложение')
PRODUCER_REQUIRE = ('Эта база является поставщиком {product}. Но мы нуждаемся в {component}, чтобы продолжать '
                    'его поставки. Если у тебя есть товар, то ты можешь его выгодно продать на нашей базе.')
PRODUCER_SHOW_CONSUMER_BEST = ('На этой базе можно купить {product}. Я могу показать лучшее место, где можно '
                               'сбыть этот товар. Покажу за ___ ')
PRODUCER_SHOW_CONSUMER_NEAR = ('Тут продают товар {comm}. Могу показать, где его можно выгодно продать. '
                               'Расскажу за ___')

ROID_MINER = ('В этой системе есть добывающие судна. На них можно найти особое оборудование, если конечно ты сможешь '
              'добыть особую руду рядом с добывающим судном. Показать тебе, где оно находится? ')
GAS_MINER = ('В этой системе есть газодобытчики, они могут произвести тебе особые устройства, но только если ты '
             'сможешь добыть особый газ в ледяных астероидах, которые находятся рядом с базой. '
             'Могу показать такой ')
ABANDONED_ICE_BASE = ('В этой системе есть старая ледяная добывающая база. На ней остались производственные мощности. '
                      'Если сможешь добыть в ледяных астероидах особый газ, то на этой базе тебе смогут собрать '
                      'интересное оборудование. Могу показать тебе ')

ABANDONED_ASTEROID_BASE = ('Ты можешь найти в этой системе старую добывающую станцию. Она частично функционирует, ты '
                           'даже можешь получить на ней особое оборудование, но для начала надо найти в ближайщих '
                           'астероидах особую руду. Хочешь попробовать? Могу показать это место ')
SMELTER = ('В нашей системе много мусора, самый радиактивный и токсичный перерабатывают на мусороперабатывающих '
           'фабриках. Это станции так же могут производить особые энергетические установки. Только для этого '
           'нужно в ближайших блоках мусора отыскать особые радиактивные компоненты. Попробуешь? Покажу базу ')
SOLAR_PLANT = ('В центре этой системы ты можешь найти солнечный генератор энергии. Если сможешь заполучить к нему '
               'доступ, то сможешь найти интересное оборудование. Я думаю ты сможешь найти способ его взломать на '
               'одном из разломанных кораблей, недалеко от генератора энергии. Давай покажу тебе генератор ')
HACKABLE_SOLAR_PLANT = ('В центре этой системы ты можешь найти солнечный генератор энергии. Если сможешь заполучить к нему '
                        'доступ, то сможешь найти интересное оборудование. Двери плотно закрыты, но точно должен '
                        'быть какой-то способ сломать систему защиты. Могу показать тебе генератор ')

RUINS = ('Я знаю где находятся руины интересной станции. Внутри точно осталась интересное оборудование, нужно только '
         'найти способ туда пробраться. Показать? Я знаю где она ')
LOCKED_BATTLESHIP = ('Я могу показать где находятся руины линкора, на нем остался военный арсенал. Вот только бы найти '
                     'способ в него проникнуть. Я думаю можно что-то найти в разломанных кораблях, находящихся '
                     'поблизости от этого линкора. Могу показать где находится этот линкор ')
HACKABLE_BATTLESHIP = ('Я могу показать где находятся руины линкора, на нем остался военный арсенал. Вот только бы найти '
                       'способ в него проникнуть. Его двери плотно закрыты, но должны быть способ обойти систему '
                       'безопасности.  Могу показать где находится этот линкор ')
LOCKED_LUXURY = ('Я могу показать где находятся руины лайнера, на нем точно что-то осталось. Вот только бы найти '
                 'способ в него проникнуть. Я думаю можно что-то найти в разломанных кораблях, находящихся '
                 'поблизости от этого лайнера. Могу показать где находится этот лайнер ')
HACKABLE_LUXURY = ('Могу показать тебе где находятся руины круизного лайнера. Это была трагедия, '
                   'но большую часть посетителей эвакуировали. Но что-то на нем точно осталось, '
                   'надо только найти способ в него проникнуть. Двери плотно закрыты, но должен быть способ их взломать. '
                   'Давай я покажу его тебе ')


class Message:

    def get_definition(self):
        raise NotImplementedError

    def dump(self):
        raise NotImplementedError


class Rumor(Message):

    def __init__(self, core, text):
        self.text = text
        self.rumor_id = core.ids.rumors.new_name(self.text)

    def get_rumor_id(self):
        return self.rumor_id.id

    def get_definition(self):
        return f'rumor = base_0_rank, mission_end, 1, {self.get_rumor_id()}'

    def dump(self):
        return self.text


class KnowRumor(Message):

    def __init__(self, core, text, knows):
        self.knows = knows
        self.text = text
        self.rumor_id = core.rumor_ids.new_name(self.text)

    def get_rumor_id(self):
        return self.rumor_id.id

    def get_knows(self):
        return ", ".join(self.knows)

    def get_definition(self):
        return SINGLE_DIVIDER.join([
            f'rumor = base_0_rank, mission_end, 1, {self.rumor_id()}'            
            f'rumorknowdb = {self.get_knows()}'
        ])

    def dump(self):
        return f'{self.text} --- {self.get_knows()}'


class StoryRumor(Message):

    def __init__(self, core, start, end, text):
        self.start = start
        self.end = end
        self.text = text
        self.rumor_id = core.rumor_ids.new_name(self.text)

    def get_rumor_id(self):
        return self.rumor_id.id

    def get_definition(self):
        return f'rumor_type2 = {self.start}, {self.end}, 1, {self.rumor_id()}'


class Knowledge(Message):

    def __init__(self, core, text, system_object, price):
        self.text = text
        self.system_object = system_object
        self.price = price
        self.rumor_id = core.ids.rumors.new_name(self.text)
        self.know_index = core.chars.know_indexes.new_id()
        core.chars.add_knowledge(self)

    def get_rumor_id(self):
        return self.rumor_id.id

    def get_knowledge_id(self):
        return self.know_index.id

    def get_system_object(self):
        return self.system_object.get_inspace_nickname()

    def get_system_name(self):
        return self.system_object.system.NAME

    def get_definition(self):
        return SINGLE_DIVIDER.join([
            f'know = {self.get_rumor_id()}, {self.get_knowledge_id()}, {self.price}, 1',
            f'knowdb = {self.system_object.get_inspace_nickname()}',
        ])

    def dump(self):
        return f'{self.text} --- {self.system_object.get_inspace_nickname()}'


class Bribe(Message):
    BRIBE_IDS = (16100, 16101, 16102, 16103)

    def __init__(self, faction, price):
        self.faction = faction
        self.price = price

    def get_bribe_id(self):
        return choice(self.BRIBE_IDS)

    def get_definition(self):
        return f'bribe = {self.faction}, {self.price}, {self.get_bribe_id()}'


class MessageBuilder:

    def __init__(self, core):
        self.core = core

    def rumor_produce_best(self, product):
        text = PRODUCER_BEST.format(product=product.get_ru_name_rel2())
        return Rumor(self.core, text)

    def rumor_produce_any(self, product):
        text = PRODUCER_ANY.format(product=product.get_ru_name_rel1())
        return Rumor(self.core, text)

    def rumor_produce_require(self, product, component):
        text = PRODUCER_REQUIRE.format(product=product.get_ru_name_rel2(), component=component.get_ru_name_rel3())
        return Rumor(self.core, text)

    def knowledge_show_consumer_best(self, product, consumer_comm):
        text = PRODUCER_SHOW_CONSUMER_BEST.format(
            product=product.get_ru_name_rel1(),
        )
        return Knowledge(self.core, text, system_object=consumer_comm.base.get_system_object(), price=500)

    def journey_roid_miner(self, system_object):
        return Knowledge(self.core, ROID_MINER, system_object=system_object, price=500)

    def journey_gas_miner(self, system_object):
        return Knowledge(self.core, GAS_MINER, system_object=system_object, price=500)

    def journey_ice(self, system_object):
        return Knowledge(self.core, ABANDONED_ICE_BASE, system_object=system_object, price=500)

    def journey_ast(self, system_object):
        return Knowledge(self.core, ABANDONED_ASTEROID_BASE, system_object=system_object, price=500)

    def journey_smelter(self, system_object):
        return Knowledge(self.core, SMELTER, system_object=system_object, price=500)

    def journey_solar_plant(self, system_object):
        return Knowledge(self.core, SOLAR_PLANT, system_object=system_object, price=500)

    def journey_solar_plant_hackable(self, system_object):
        return Knowledge(self.core, HACKABLE_SOLAR_PLANT, system_object=system_object, price=500)

    def journey_ruins(self, system_object):
        return Knowledge(self.core, RUINS, system_object=system_object, price=500)

    def journey_battleship_locked(self, system_object):
        return Knowledge(self.core, LOCKED_BATTLESHIP, system_object=system_object, price=500)

    def journey_battleship_hackable(self, system_object):
        return Knowledge(self.core, HACKABLE_BATTLESHIP, system_object=system_object, price=500)

    def journey_luxury_locked(self, system_object):
        return Knowledge(self.core, LOCKED_LUXURY, system_object=system_object, price=500)

    def journey_luxury(self, system_object):
        return Knowledge(self.core, HACKABLE_LUXURY, system_object=system_object, price=500)
