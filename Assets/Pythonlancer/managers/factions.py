from universe.faction import Faction, PlayerFaction, RELATIONS, FRIEND_MAX
from text.dividers import DIVIDER


class FactionManager:

    def __init__(self, core):
        self.core = core

        self.factions_db = {}
        self.factions_list = []

        self.load_factions()
        self.load_relations_props()

    def get_all(self):
        return self.factions_list

    def get_managed_factions(self):
        return [f for f in self.factions_list if f.is_managed()]

    def get_player_relations(self):
        return PlayerFaction.get_init_factions()

    def load_factions(self):
        for faction_class in Faction.subclasses:
            if faction_class.ABSTRACT:
                continue
            faction = faction_class(self.core.russian, self.core.ids)

            self.factions_db[faction.CODE] = faction
            self.factions_list.append(faction)

        for faction in self.factions_list:
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

    def get_initial_world_content(self):
        return DIVIDER.join([x.get_initial_world_content() for x in self.factions_list])

    def get_empathy_content(self):
        return DIVIDER.join([x.get_empathy_content() for x in self.factions_list])
