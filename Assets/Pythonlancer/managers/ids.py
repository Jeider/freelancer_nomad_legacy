from text.strings import IDsDatabase

INITIAL_EQUIP_ID = 280000
INITIAL_SHIP_ID = 263000
INITIAL_STORY_ID = 263000
INITIAL_UNIVERSE_ID = 263000


class IDsManager:

    def __init__(self, core):
        self.core = core

        self.equip = IDsDatabase(INITIAL_EQUIP_ID)
        self.ship = IDsDatabase(INITIAL_SHIP_ID)
        self.story = IDsDatabase(INITIAL_STORY_ID)
        self.universe = IDsDatabase(INITIAL_UNIVERSE_ID)

        self.databases = [
            self.equip,
            self.ship,
            self.story,
            self.universe
        ]

    def compile(self):
        return ''.join([db.compile() for db in self.databases])
