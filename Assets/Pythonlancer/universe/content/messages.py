from random import choice
from text.dividers import SINGLE_DIVIDER


class Message:

    def get_definition(self):
        raise NotImplementedError


class Rumor(Message):

    def __init__(self, core, text):
        self.rumor_id = core.rumor_ids.new_name(text)

    def get_rumor_id(self):
        return self.rumor_id.id

    def get_definition(self):
        return f'rumor = base_0_rank, mission_end, 2, {self.rumor_id()}'


class KnowRumor(Message):

    def __init__(self, core, text, knows):
        self.knows = knows
        self.rumor_id = core.rumor_ids.new_name(text)

    def get_rumor_id(self):
        return self.rumor_id.id

    def get_definition(self):
        return SINGLE_DIVIDER.join([
            f'rumor = base_0_rank, mission_end, 2, {self.rumor_id()}'            
            f'rumorknowdb = {", ".join(self.knows)}'
        ])


class StoryRumor(Message):

    def __init__(self, core, start, end, text):
        self.start = start
        self.end = end
        self.rumor_id = core.rumor_ids.new_name(text)

    def get_rumor_id(self):
        return self.rumor_id.id

    def get_definition(self):
        return f'rumor_type2 = {self.start}, {self.end}, 1, {self.rumor_id()}'


class Knowledge(Message):

    def __init__(self, core, text, nickname, price):
        self.nickname = nickname
        self.price = price
        self.rumor_id = core.ids.rumor_ids.new_name(text)
        self.knowledge = core.ids.knowledge_ids.new_id()

    def get_rumor_id(self):
        return self.rumor_id.id

    def get_knowledge_id(self):
        return self.knowledge.id

    def get_definition(self):
        return SINGLE_DIVIDER.join([
            f'know = {self.get_rumor_id()}, {self.get_knowledge_id()}, {self.price}, 1',
            f'knowdb = {self.nickname}',
        ])


class Bribe(Message):
    BRIBE_IDS = (16100, 16101, 16102, 16103)

    def __init__(self, faction, price):
        self.faction = faction
        self.price = price

    def get_bribe_id(self):
        return choice(self.BRIBE_IDS)

    def get_definition(self):
        return f'bribe = {self.faction}, {self.price}, {self.get_bribe_id()}'
