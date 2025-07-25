from text.strings import IDsDatabase
from text.static import RETURN_NAMES

INITIAL_WEAPON_ID = 280001
INITIAL_EQUIP_ID = 290001
INITIAL_COMMODITY_ID = 300001
INITIAL_KEY_ID = 315001
INITIAL_SHIP_ID = 110001
INITIAL_STORY_ID = 33500
INITIAL_STORY_SAVE_ID = 33330
INITIAL_SCRIPT_ID = 150000
INITIAL_UNIVERSE_ID = 68200
INITIAL_RUMOR_ID = 138000
INITIAL_KNOWLEDGE_ID = 10001

INITIAL_STATICS_ID = 202607


class IDsManager:

    def __init__(self, core):
        self.core = core

        self.weapon = IDsDatabase('weapon', INITIAL_WEAPON_ID)
        self.equip = IDsDatabase('equip', INITIAL_EQUIP_ID)
        self.commodity = IDsDatabase('commodity', INITIAL_COMMODITY_ID)
        self.key = IDsDatabase('key', INITIAL_KEY_ID)
        self.ship = IDsDatabase('ship', INITIAL_SHIP_ID)
        self.story = IDsDatabase('story', INITIAL_STORY_ID)
        self.story_save = IDsDatabase('story_save', INITIAL_STORY_SAVE_ID)
        self.script = IDsDatabase('script', INITIAL_SCRIPT_ID)
        self.universe = IDsDatabase('universe', INITIAL_UNIVERSE_ID)
        self.rumors = IDsDatabase('rumor', INITIAL_RUMOR_ID)
        self.static = IDsDatabase('static', INITIAL_STATICS_ID)

        self.databases = [
            self.weapon,
            self.equip,
            self.commodity,
            self.key,
            self.ship,
            self.story,
            self.story_save,
            self.script,
            self.universe,
            self.rumors,
            self.static,
        ]

        for item in RETURN_NAMES:
            self.static.new_name(item)


    def compile(self):
        return ''.join([db.compile() for db in self.databases]).replace('+', '')

    def get_databases(self):
        return self.databases
