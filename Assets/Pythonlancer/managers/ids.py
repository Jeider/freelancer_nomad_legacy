from text.strings import IDsDatabase

INITIAL_EQUIP_ID = 280000
INITIAL_SHIP_ID = 263000
INITIAL_STORY_ID = 263000
INITIAL_UNIVERSE_ID = 263000
INITIAL_RUMOR_ID = 263000
INITIAL_KNOWLEDGE_ID = 10001


class IDsManager:

    def __init__(self, core):
        self.core = core

        self.equip = IDsDatabase(INITIAL_EQUIP_ID)
        self.ship = IDsDatabase(INITIAL_SHIP_ID)
        self.story = IDsDatabase(INITIAL_STORY_ID)
        self.universe = IDsDatabase(INITIAL_UNIVERSE_ID)
        self.rumors = IDsDatabase(INITIAL_RUMOR_ID)

        self.databases = [
            self.equip,
            self.ship,
            self.story,
            self.universe,
            self.rumors,
        ]

    def compile(self):
        return ''.join([db.compile() for db in self.databases])
