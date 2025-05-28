from text.strings import IDsDatabase

INITIAL_EQUIP_ID = 280001
INITIAL_SHIP_ID = 110001
INITIAL_STORY_ID = 33500
INITIAL_SCRIPT_ID = 150000
INITIAL_UNIVERSE_ID = 68200
INITIAL_RUMOR_ID = 138000
INITIAL_KNOWLEDGE_ID = 10001


class IDsManager:

    def __init__(self, core):
        self.core = core

        self.equip = IDsDatabase('equip', INITIAL_EQUIP_ID)
        self.ship = IDsDatabase('ship', INITIAL_SHIP_ID)
        self.story = IDsDatabase('story', INITIAL_STORY_ID)
        self.script = IDsDatabase('script', INITIAL_SCRIPT_ID)
        self.universe = IDsDatabase('universe', INITIAL_UNIVERSE_ID)
        self.rumors = IDsDatabase('rumor', INITIAL_RUMOR_ID)

        self.databases = [
            self.equip,
            self.ship,
            self.story,
            self.script,
            self.universe,
            self.rumors,
        ]

    def compile(self):
        return ''.join([db.compile() for db in self.databases]).replace('+', '')

    def get_databases(self):
        return self.databases
