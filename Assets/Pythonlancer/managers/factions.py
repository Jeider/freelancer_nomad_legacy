from tools.data_folder import DataFolder
from universe.faction import Faction, PLAYER_RELATIONS, RELATIONS, FRIEND_MAX, BRIBE_GROUPS
from text.dividers import DIVIDER, SINGLE_DIVIDER

VIGNETTE_TEMPLATE = 'hardcoded_inis/static_content/vignette_params.ini'


class FactionManager:

    def __init__(self, core):
        self.core = core

        self.factions_db = {}
        self.factions_list = []
        self.player_relations = {}

        self.load_factions()
        self.load_relations_props()
        self.load_player_relations()
        self.load_bribe_factions()

        self.sync_data()

    def get_all(self):
        return self.factions_list

    def get_managed_factions(self):
        return [f for f in self.factions_list if f.is_managed()]

    def get_by_code(self, code):
        return self.factions_db[code]

    def load_player_relations(self):
        for rel in PLAYER_RELATIONS:
            if rel.faction.CODE in self.player_relations:
                self.player_relations[rel.faction.CODE] = rel.get_reputation()

    def get_player_relations(self):
        result = []
        for faction, reputation in self.player_relations.items():
            result.append(
                f'house = {reputation}, {faction}'
            )
        return SINGLE_DIVIDER.join(result)

    def load_factions(self):
        for faction_class in Faction.subclasses:
            if faction_class.ABSTRACT:
                continue
            faction = faction_class(self.core.russian, self.core.ids)

            self.factions_db[faction.CODE] = faction
            self.factions_list.append(faction)

        for faction in self.factions_list:
            if faction.is_listed():
                self.player_relations[faction.get_code()] = 0
            for rel_faction in self.factions_list:
                faction.init_relations(rel_faction)

    def load_relations_props(self):
        for rel in RELATIONS:
            current_faction = self.factions_db[rel.faction.CODE]
            for target_rel in rel.relations:
                target_faction = self.factions_db[target_rel.get_faction().CODE]

                if target_faction.CODE != current_faction.CODE:
                    current_faction.change_reputation(target_faction, target_rel.get_reputation())
                    current_faction.change_empathy(target_faction, target_rel.get_empathy())

                    target_faction.change_reputation(current_faction, target_rel.get_reputation())
                    target_faction.change_empathy(current_faction, target_rel.get_empathy())

    def load_bribe_factions(self):
        for faction in self.factions_list:
            for group in BRIBE_GROUPS:
                for bribe_faction in group:
                    if bribe_faction.get_code() == faction.get_code():
                        faction.add_bribe_group(group)
                        continue

    def get_initial_world_empty_reps(self, hate=False):
        return SINGLE_DIVIDER.join([x.get_empty_rep(hate=hate) for x in self.factions_list if x.LISTED])

    def get_initial_world_content(self):
        return DIVIDER.join([x.get_initial_world_content() for x in self.factions_list if x.LISTED])

    def get_empathy_content(self):
        return DIVIDER.join([x.get_empathy_content() for x in self.factions_list if x.LISTED])

    def get_military_factions_list(self):
        return ', '.join([x.get_code() for x in self.factions_list if x.has_military_mission() or x.has_pirate_mission()])

    def get_civilian_factions_list(self):
        return ', '.join([x.get_code() for x in self.factions_list if x.has_military_mission() or x.has_pirate_mission()])

    def get_pirate_factions_list(self):
        return ', '.join([x.get_code() for x in self.factions_list if x.has_pirate_mission()])

    def get_vignettes_content(self):
        context = {
            'military_factions': self.get_military_factions_list(),
            'civilian_factions': self.get_civilian_factions_list(),
            'pirate_factions': self.get_pirate_factions_list(),
        }
        # Keep not changed original file
        return self.core.tpl_manager.get_result(VIGNETTE_TEMPLATE, context)

    def sync_data(self):
        if not self.core.write:
            return

        data_folder = DataFolder(build_to_folder=self.core.build_folder)

        data_folder.sync_vignettes(self.get_vignettes_content())