from world import faction
from world.npc import NPC


class PopulationManager(object):

    def __init__(self, misc_equip, weapons):
        self.factions = [
            faction.RheinlandMain,
            faction.RheinlandCivilians,
            faction.RheinlandHunters,
            faction.RheinlandPirate,
            faction.Hessians,
            faction.Junkers,
        ]

        self.misc_equip = misc_equip
        self.weapons = weapons

        self.npc_db = {}
        self.loadouts_db = {}

        self.load_game_data()

    def get_equipment_package(self, faction, npc):
        return {
            NPC.ENGINE: self.misc_equip.get_engine(npc.ship.EQUIPMENT_SHIPCLASS, faction.ENGINE, npc.get_engine_class()),
            NPC.POWER: self.misc_equip.get_powerplant(npc.ship.EQUIPMENT_SHIPCLASS, faction.POWER, npc.get_powerplant_class()),
            NPC.SHIELD: self.misc_equip.get_shield(npc.ship.EQUIPMENT_SHIPCLASS, faction.SHIELD, npc.get_shield_class()),
            NPC.SHIELD_NPC: self.misc_equip.get_npc_shield(npc.ship.EQUIPMENT_SHIPCLASS, faction.SHIELD, npc.get_shield_class()),
            NPC.WEAPON_1: self.weapons.get_gun(faction.WEAPON, npc.get_weapon1_class()),
            NPC.WEAPON_2: self.weapons.get_gun(faction.WEAPON, npc.get_weapon2_class()),
            NPC.WEAPON_3: self.weapons.get_gun(faction.WEAPON, npc.get_weapon3_class()),
            NPC.WEAPON_4: self.weapons.get_gun(faction.WEAPON, npc.get_weapon4_class()),
            NPC.WEAPON_5: self.weapons.get_gun(faction.WEAPON, npc.get_weapon5_class()),
            NPC.WEAPON_6: self.weapons.get_gun(faction.WEAPON, npc.get_weapon6_class()),
            NPC.AFTERBURN_1: self.misc_equip.get_thruster(faction.AFTERBURN, npc.get_afterburn1_class()),
            NPC.AFTERBURN_2: self.misc_equip.get_thruster(faction.AFTERBURN, npc.get_afterburn2_class()),
            NPC.TORPEDO: None,
            NPC.CM: None,
            NPC.MINE: None,
            NPC.TORPEDO_AMMO: 0,
            NPC.CM_AMMO: 0,
            NPC.MINE_AMMO: 0,
        }

    def load_game_data(self):
        for faction in self.factions:
            self.npc_db[faction.CODE] = []
            self.loadouts_db[faction.CODE] = []


            for ship in faction.SHIPS:
                for level in ship.NPC_LEVELS:
                    npc = NPC(faction, ship, level)
                    npc.set_equipment_package(self.get_equipment_package(faction, npc))

                    self.npc_db[faction.CODE].append(npc)
                    self.loadouts_db[faction.CODE].append(npc.get_loadout())
