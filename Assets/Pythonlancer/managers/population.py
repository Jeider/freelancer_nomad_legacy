from universe.faction import Faction
from world.npc import NPC, EqMap
from templates.hardcoded_inis.missions import NPCShipsTemplate

from tools.data_folder import DataFolder

from text.dividers import SINGLE_DIVIDER, DIVIDER

class PopulationManager(object):

    def __init__(self, lancer_core):
        self.core = lancer_core
        self.factions = Faction.subclasses

        self.misc_equip = self.core.misc_equip
        self.weapons = self.core.weapons
        self.shiparch = self.core.shiparch

        self.npc_db = {}
        self.npc_list = []
        self.loadouts_db = {}
        self.loadouts_list = []

        self.equip_maps = self.get_equipment_maps()

        self.load_game_data()

        self.sync_data()

    def get_equipment_maps(self):
        return {
            NPC.D1: EqMap(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0),
            NPC.D2: EqMap(2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0),
            NPC.D3: EqMap(2, 2, 2, 3, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1),
            NPC.D4: EqMap(3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2),
            NPC.D5: EqMap(3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 2, 1, 1, 3, 1, 1, 2),
            NPC.D6: EqMap(3, 3, 3, 4, 3, 3, 3, 3, 2, 3, 3, 1, 1, 3, 2, 1, 2),
            NPC.D7: EqMap(4, 4, 4, 4, 4, 4, 4, 3, 3, 4, 3, 1, 1, 3, 2, 1, 3),
            NPC.D8: EqMap(4, 4, 4, 4, 4, 4, 4, 3, 3, 4, 4, 1, 1, 3, 3, 2, 5),
            NPC.D9: EqMap(4, 4, 4, 5, 5, 4, 4, 4, 4, 5, 4, 1, 1, 3, 3, 2, 5),
            NPC.D10: EqMap(5, 5, 5, 5, 5, 5, 4, 4, 4, 5, 5, 1, 1, 3, 4, 2, 6),
            NPC.D11: EqMap(5, 5, 5, 6, 6, 5, 5, 4, 4, 6, 5, 1, 1, 5, 4, 2, 6),
            NPC.D12: EqMap(6, 6, 6, 6, 6, 6, 5, 5, 5, 6, 6, 1, 1, 5, 5, 3, 6),
            NPC.D13: EqMap(6, 6, 6, 7, 6, 6, 5, 5, 5, 7, 6, 1, 1, 5, 5, 3, 8),
            NPC.D14: EqMap(7, 7, 7, 7, 7, 6, 6, 5, 5, 7, 7, 1, 1, 5, 6, 3, 8),
            NPC.D15: EqMap(7, 7, 7, 7, 7, 7, 6, 6, 6, 7, 7, 1, 1, 7, 6, 3, 10),
            NPC.D16: EqMap(7, 7, 7, 8, 8, 7, 7, 7, 7, 8, 7, 1, 1, 7, 8, 5, 10),
            NPC.D17: EqMap(8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1, 1, 7, 10, 5, 10),
            NPC.D18: EqMap(8, 8, 8, 9, 9, 8, 8, 8, 8, 9, 8, 1, 1, 7, 10, 20, 20),
            NPC.D19: EqMap(9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 2, 9, 15, 25, 25),
        }

    def get_equip_map_by_level(self, level):
        return self.equip_maps[level]

    def get_equipment_package(self, npc):
        return {
            NPC.ENGINE: self.misc_equip.get_engine(npc.ship.EQUIPMENT_SHIPCLASS, npc.faction.ENGINE, npc.get_engine_class()),
            NPC.POWER: self.misc_equip.get_powerplant(npc.ship.EQUIPMENT_SHIPCLASS, npc.faction.POWER, npc.get_powerplant_class()),
            NPC.SHIELD: self.misc_equip.get_shield(npc.ship.EQUIPMENT_SHIPCLASS, npc.faction.SHIELD, npc.get_shield_class()),
            NPC.SHIELD_NPC: self.misc_equip.get_npc_shield(npc.ship.EQUIPMENT_SHIPCLASS, npc.faction.SHIELD, npc.get_shield_class()),
            NPC.ARMOR: self.misc_equip.get_npc_armor(npc.get_armor_index()),
            NPC.WEAPON_1: self.weapons.get_gun(npc.faction.WEAPON, npc.get_weapon1_class()),
            NPC.WEAPON_2: self.weapons.get_gun(npc.faction.WEAPON, npc.get_weapon2_class()),
            NPC.WEAPON_3: self.weapons.get_gun(npc.faction.WEAPON, npc.get_weapon3_class()),
            NPC.WEAPON_4: self.weapons.get_gun(npc.faction.WEAPON, npc.get_weapon4_class()),
            NPC.WEAPON_5: self.weapons.get_gun(npc.faction.WEAPON, npc.get_weapon5_class()),
            NPC.WEAPON_6: self.weapons.get_gun(npc.faction.WEAPON, npc.get_weapon6_class()),
            NPC.AFTERBURN_1: self.misc_equip.get_thruster(npc.faction.AFTERBURN, npc.get_afterburn1_class()),
            NPC.AFTERBURN_2: self.misc_equip.get_thruster(npc.faction.AFTERBURN, npc.get_afterburn2_class()),
            NPC.TORPEDO: None,
            NPC.CM: None,
            NPC.MINE: None,
            NPC.TORPEDO_AMMO: 0,
            NPC.CM_AMMO: 0,
            NPC.MINE_AMMO: 0,
        }

    def load_game_data(self):
        for faction in self.factions:
            if faction.STORY_ONLY:
                continue
            self.npc_db[faction.CODE] = []
            self.loadouts_db[faction.CODE] = []

            for ship_class in faction.SHIPS:
                for level in ship_class.NPC_LEVELS:
                    equip_map = self.get_equip_map_by_level(level)
                    npc = NPC(faction, ship_class, equip_map=equip_map, level=level)
                    npc.set_equipment_package(self.get_equipment_package(npc))

                    self.npc_db[faction.CODE].append(npc)
                    self.npc_list.append(npc)

                    loadout = npc.get_loadout(self.shiparch)
                    self.loadouts_db[faction.CODE].append(loadout)
                    self.loadouts_list.append(loadout)

    def get_npcships(self):
        return DIVIDER.join([npc.get_npc_shiparch() for npc in self.npc_list])

    def get_npcships_file_content(self):
        return NPCShipsTemplate().format({'generated': self.get_npcships()})

    def get_npc_names(self):
        faction_data = []

        for faction, npcs in self.npc_db.items():
            item = [
                'affilitation = ',
                faction,
                SINGLE_DIVIDER,
                SINGLE_DIVIDER.join(['npc_ship = ' + npc.get_npc_shiparch_nickname() for npc in npcs])
            ]
            faction_data.append(''.join(item))

        return DIVIDER.join(faction_data)

    def get_loadouts(self):
        return DIVIDER.join(self.loadouts_list)

    def sync_data(self):
        DataFolder.sync_ships_loadouts(self.get_loadouts())
        DataFolder.sync_npcships(self.get_npcships_file_content())
