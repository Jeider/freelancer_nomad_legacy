from universe.content.messages import MessageBuilder
from text.strings import IndexDatabase

INITIAL_KNOWLEDGE_ID = 10001


class CharacterManager:

    def __init__(self, core):
        self.core = core

        self.knowledge = IndexDatabase(INITIAL_KNOWLEDGE_ID)
        self.msg = MessageBuilder(core=self.core)
