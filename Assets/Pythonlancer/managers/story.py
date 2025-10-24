from managers.script import ScriptManager

from story.ingame.gameplay import *  # initialize mission files
from story.ingame.ingame_mission import IngameMission
from story.ingame.history import get_history_items_dict, HistoryItem

from tools.data_folder import DataFolder

from text.dividers import DIVIDER, SINGLE_DIVIDER


class HistoryManager:

    def __init__(self, ids):
        self.ids = ids
        self.histories: dict[str, HistoryItem] = get_history_items_dict(ids)
        self.used = []
        self.left_keys: list = list(self.histories.keys())

    def item(self, index):
        if index in self.used:
            raise Exception(f'index {index} already used')
        self.left_keys.remove(index)
        self.used.append(index)
        return self.histories[index].show()

    def validate_after(self):
        if len(self.left_keys) > 0:
            raise Exception(f'Some keys are left ({",".join(self.left_keys)})')


class StoryManager:

    def __init__(self, lancer_core):
        self.core = lancer_core
        self.universe = self.core.universe
        self.population = self.core.population
        self.shiparch = self.core.shiparch
        self.ids = self.core.ids.story
        self.ids_save = self.core.ids.story_save
        self.history_manager = HistoryManager(ids=self.core.ids.history)

        self.missions = []

        self.script = ScriptManager(ids=self.core.ids.script)

        self.thorns = []
        self.ship_loadouts = []
        self.rtc_files = []
        data_folder = DataFolder(build_to_folder=self.core.build_folder)

        for mission_class in IngameMission.subclasses:

            print(mission_class)
            mission = mission_class(russian=self.core.russian,
                                    ids=self.ids, ids_save=self.ids_save,
                                    full_script=self.script, universe=self.universe,
                                    history_manager=self.history_manager)
            self.missions.append(mission)
            content = self.core.tpl_manager.get_result(mission.get_template(), mission.get_context())
            self.thorns.extend(mission.ingame_thorns)

            npc_shiparchs = []

            if mission.STATIC_NPCSHIPS:
                npc_shiparchs.append(mission.STATIC_NPCSHIPS)

            for npc in mission.get_npcs():
                npc.set_equipment_package(self.population.get_equipment_package(npc))
                loadout = npc.get_loadout(self.shiparch)
                self.ship_loadouts.append(loadout)
                npc_shiparchs.append(npc.get_npc_shiparch())

            if self.core.write:
                data_folder.sync_story_mission(mission.FOLDER, mission.FILE, content)

            for rtc_name, rtc_template in mission.get_rtc_files():
                rtc_context = mission.get_rtc_context()
                rtc_content = self.core.tpl_manager.get_result(rtc_template, rtc_context)

                if self.core.write:
                    data_folder.sync_story_mission(mission.FOLDER, rtc_name, rtc_content)

            if len(npc_shiparchs):
                npcships = DIVIDER.join(npc_shiparchs)
                data_folder.sync_story_npcships(mission.FOLDER, npcships)

        self.history_manager.validate_after()

        loadouts = DIVIDER.join(self.ship_loadouts)
        if self.core.write:
            data_folder.sync_story_ships_loadouts(loadouts)

        for thorn in self.thorns:
            content = self.core.tpl_manager.get_result(thorn.get_template(), thorn.get_context())
            if self.core.write:
                data_folder.sync_story_ingame_thorn(thorn.get_name(), content)

        if self.core.write:
            self.script.write_script_sounds()
