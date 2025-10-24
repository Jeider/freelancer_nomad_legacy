from universe.content.messages import MessageBuilder, Knowledge

from world.bodyparts import CharacterFactory

from tools.data_folder import DataFolder

from text.strings import IndexDatabase
from text.dividers import SINGLE_DIVIDER

INITIAL_KNOWLEDGE_ID = 10001


class CharacterManager:

    def __init__(self, core):
        self.core = core

        self.know_indexes = IndexDatabase(INITIAL_KNOWLEDGE_ID)
        self.msg = MessageBuilder(core=self.core)
        self.knowledge: list[Knowledge] = []

    def add_knowledge(self, knowledge):
        self.knowledge.append(knowledge)

    def get_knowledge_map_content(self):
        knowledge_map = ['[KnowledgeMapTable]']
        for know in self.knowledge:
            knowledge_map.append(f'Map = {know.get_knowledge_id()}, {know.get_system_object()}, 1')
            knowledge_map.append(f'Map = {know.get_knowledge_id()}, {know.get_system_name()}, 1')

        return SINGLE_DIVIDER.join(knowledge_map)

    def post_load(self):

        self.sync_data()

    def sync_data(self):
        if not self.core.write:
            return

        DataFolder(build_to_folder=self.core.build_folder).sync_knowledge_map(self.get_knowledge_map_content())

