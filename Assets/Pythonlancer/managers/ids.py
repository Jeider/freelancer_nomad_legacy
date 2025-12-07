from text.strings import IDsDatabase
from text.static import RETURN_NAMES, STATIC_NAMES

INITIAL_WEAPON_ID = 280001
INITIAL_EQUIP_ID = 290001
INITIAL_COMMODITY_ID = 300001
INITIAL_KEY_ID = 315001
INITIAL_SHIP_ID = 110001
INITIAL_STORY_ID = 33500
INITIAL_STORY_SAVE_ID = 33330
INITIAL_HISTORY_ID = 45000
INITIAL_SCRIPT_ID = 150000
INITIAL_UNIVERSE_ID = 68200
INITIAL_RUMOR_ID = 138000
INITIAL_KNOWLEDGE_ID = 10001

INITIAL_STATICS_ID = 202607

INITIAL_FACTIONS_SHORTS_ID = 210200
INITIAL_FACTIONS_DESC_ID = 210300
INITIAL_FACTIONS_MAIN_ID = 196846
INITIAL_FACTIONS_OFFER1_ID = 328680
INITIAL_FACTIONS_OFFER2_ID = 328780
INITIAL_FACTIONS_OFFER3_ID = 328880
INITIAL_FACTIONS_OFFER4_ID = 328980

# 047050 - Navy (short)

# 196846 - Liberty Navy (Main!)

# 328680 - Liberty Navy
# 328780 - the Liberty Navy
# 328880 - Liberty Navy
# 328980 - The Liberty Navy


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
        self.history = IDsDatabase('history', INITIAL_HISTORY_ID)
        self.script = IDsDatabase('script', INITIAL_SCRIPT_ID)
        self.universe = IDsDatabase('universe', INITIAL_UNIVERSE_ID)
        self.rumors = IDsDatabase('rumor', INITIAL_RUMOR_ID)
        self.static = IDsDatabase('static', INITIAL_STATICS_ID)
        self.factions_shorts = IDsDatabase('factions_shorts', INITIAL_FACTIONS_SHORTS_ID)
        self.factions_desc = IDsDatabase('factions_desc', INITIAL_FACTIONS_DESC_ID)
        self.factions_main = IDsDatabase('factions_main', INITIAL_FACTIONS_MAIN_ID)
        self.factions_offer1 = IDsDatabase('factions_offer1', INITIAL_FACTIONS_OFFER1_ID)
        self.factions_offer2 = IDsDatabase('factions_offer2', INITIAL_FACTIONS_OFFER2_ID)
        self.factions_offer3 = IDsDatabase('factions_offer3', INITIAL_FACTIONS_OFFER3_ID)
        self.factions_offer4 = IDsDatabase('factions_offer4', INITIAL_FACTIONS_OFFER4_ID)

        self.databases = [
            self.weapon,
            self.equip,
            self.commodity,
            self.key,
            self.ship,
            self.story,
            self.story_save,
            self.history,
            self.script,
            self.universe,
            self.rumors,
            self.static,
            self.factions_shorts,
            self.factions_desc,
            self.factions_main,
            self.factions_offer1,
            self.factions_offer2,
            self.factions_offer3,
            self.factions_offer4,
        ]
        #
        # for item in RETURN_NAMES:
        #     self.static.new_name(item)

        for item in STATIC_NAMES:
            self.static.add_force(item.ids, item.ru_name)

    def get_databases(self):
        return self.databases
