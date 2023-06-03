from world import faction
from world.npc import NPC


class PopulationManager(object):

    def __init__(self):
        self.factions = [
            faction.RheinlandMain,
            faction.RheinlandCivilians,
            faction.RheinlandHunters,
            faction.RheinlandPirate,
            faction.Hessians,
            faction.Junkers,
        ]

        self.npc_db = {}

        self.load_game_data()

    def load_game_data(self):
        for faction in self.factions:
            for ship in faction.SHIPS:
                for level in ship.NPC_LEVELS:
                    self.npc_db[faction] = NPC(faction, ship, level)

                    # TODO: build loadout
