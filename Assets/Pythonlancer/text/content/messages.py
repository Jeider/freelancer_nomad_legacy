from random import choice
from text.dividers import SINGLE_DIVIDER
from text.strings import MultiString as MS

import text.content.messages_text_ru as RU
import text.content.messages_text_en as EN
#
# PRODUCER_BEST = MS(RU.PRODUCER_BEST, EN.PRODUCER_BEST)
# PRODUCER_ANY = MS(RU.PRODUCER_ANY, EN.PRODUCER_ANY)
# PRODUCER_REQUIRE = MS(RU.PRODUCER_REQUIRE, EN.PRODUCER_REQUIRE)
#
# PRODUCER_SHOW_CONSUMER_BEST = MS(RU.PRODUCER_SHOW_CONSUMER_BEST, EN.PRODUCER_SHOW_CONSUMER_BEST)

ROID_MINER = MS(RU.ROID_MINER, EN.ROID_MINER)

GAS_MINER = MS(RU.GAS_MINER, EN.GAS_MINER)

ABANDONED_ICE_BASE = MS(RU.ABANDONED_ICE_BASE, EN.ABANDONED_ICE_BASE)

ABANDONED_ASTEROID_BASE = MS(RU.ABANDONED_ASTEROID_BASE, EN.ABANDONED_ASTEROID_BASE)

SMELTER = MS(RU.SMELTER, EN.SMELTER)

SOLAR_PLANT = MS(RU.SOLAR_PLANT, EN.SOLAR_PLANT)

HACKABLE_SOLAR_PLANT = MS(RU.HACKABLE_SOLAR_PLANT, EN.HACKABLE_SOLAR_PLANT)

RUINS = MS(RU.RUINS, EN.RUINS)

LOCKED_BATTLESHIP = MS(RU.LOCKED_BATTLESHIP, EN.LOCKED_BATTLESHIP)

HACKABLE_BATTLESHIP = MS(RU.HACKABLE_BATTLESHIP, EN.HACKABLE_BATTLESHIP)

LOCKED_LUXURY = MS(RU.LOCKED_LUXURY, EN.LOCKED_LUXURY)

HACKABLE_LUXURY = MS(RU.HACKABLE_LUXURY, EN.HACKABLE_LUXURY)



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
        return Rumor(self.core, MS(
            RU.PRODUCER_BEST.format(product=product.get_ru_name_rel2()),
            EN.PRODUCER_BEST.format(product=product.get_en_name_rel2()),
        ))

    def rumor_produce_any(self, product):
        return Rumor(self.core, MS(
            RU.PRODUCER_ANY.format(product=product.get_ru_name_rel1()),
            EN.PRODUCER_ANY.format(product=product.get_en_name_rel1())
        ))

    def rumor_produce_require(self, product, component):
        return Rumor(self.core, MS(
            RU.PRODUCER_REQUIRE.format(product=product.get_ru_name_rel2(), component=component.get_ru_name_rel3()),
            EN.PRODUCER_REQUIRE.format(product=product.get_en_name_rel2(), component=component.get_en_name_rel3())
        ))

    def knowledge_show_consumer_best(self, product, consumer_comm):
        return Knowledge(self.core, MS(
            RU.PRODUCER_SHOW_CONSUMER_BEST.format(product=product.get_ru_name_rel1()),
            EN.PRODUCER_SHOW_CONSUMER_BEST.format(product=product.get_en_name_rel1())
        ), system_object=consumer_comm.base.get_system_object(), price=500)

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
