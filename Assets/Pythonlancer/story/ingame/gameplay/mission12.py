import random

from universe import sirius as S
from story.ingame import ingame_mission
from story.math import euler_to_quat
from story import actors

from story.ingame.tools import Point, Obj, Conn, NNObj, Ship, Solar, Capital
from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT

from world.npc import NPC, EqMap
from world import ship
from universe import faction

NPCSHIPS = '''
nickname = ms12_ku_gunboat
loadout = ku_grp_gunboat
level = d10
ship_archetype = ku_gunboat
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER, d5

[NPCShipArch]
nickname = ms12_ku_destroyer
loadout = ku_grp_destroyer
level = d10
ship_archetype = ku_destroyer
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER, d5

[NPCShipArch]
nickname = ms12_ku_battleship
loadout = ku_grp_battleship
level = d10
ship_archetype = ku_battleship
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER, d5

[NPCShipArch]
nickname = ms12_ku_battleship_assault
loadout = ku_battleship_m13_assault
level = d10
ship_archetype = ku_battleship_m13_assault
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER, d5



[NPCShipArch]
nickname = ms12_li_dread
loadout = li_dreadnought_03_surv1_evil
level = d10
ship_archetype = li_dreadnought
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER, d5

[NPCShipArch]
nickname = ms12_li_cruiser
loadout = li_grp_cruiser
level = d10
ship_archetype = li_cruiser
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER, d5

[NPCShipArch]
nickname = ms12_osiris
loadout = li_battleship_02
level = d10
ship_archetype = or_osiris
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER, d5



'''


class Misson12(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m12/m12.ini'
    FOLDER = 'M12'
    FILE = 'm12'
    SCRIPT_INDEX = 12
    DIRECT_SYSTEMS = [S.asf_hq]
    STATIC_NPCSHIPS = NPCSHIPS

    def get_static_points(self):
        defined_points = []

        asf_points = [
            'asf_miner01',
            'asf_miner02',
            'to_bush01',
            'to_bush02',
            'to_bush03',
            'to_bush04',
            'to_bush05',
            'to_bush06',
        ]
        for p in asf_points:
            defined_points.append(
                Point(self, S.asf_hq, p)
            )

        asf_solars = [
            'ku_miner01',
            'ku_miner02',
            'ku_miner03',
            'fort_bush',
            'fort1',
            'fort2',
            'fort3',
            'fort4',
            'fort5',

            'counter_relative_obj',
            'counter_assault',
        ]
        for sol in asf_solars:
            defined_points.append(
                Solar(self, S.asf_hq, sol),
            )

        return defined_points

    def get_capital_ships(self):
        ku_bship = {
            'npc_ship_arch': 'ms12_ku_battleship',
            'faction': 'or_grp',
            'labels': ['enemy'],
        }
        ku_destroyer = {
            'npc_ship_arch': 'ms12_ku_destroyer',
            'faction': 'or_grp',
            'labels': ['enemy', 'ku_destroyer'],
        }
        li_dread = {
            'npc_ship_arch': 'ms12_li_dread',
            'faction': 'asf_grp',
            'labels': ['friend', 'asf'],
        }
        omaha = {
            'npc_ship_arch': 'ms12_li_cruiser',
            'faction': 'asf_grp',
            'labels': ['friend', 'omaha', 'asf', 'li_cruiser'],
        }
        li_cruiser = {
            'npc_ship_arch': 'ms12_li_cruiser',
            'faction': 'asf_grp',
            'labels': ['friend', 'asf', 'li_cruiser'],
        }
        ku_bship_assault = {
            'npc_ship_arch': 'ms12_ku_battleship_assault',
            'faction': 'or_grp',
            'labels': ['ku_bship_assault'],
        }
        osiris = {
            'npc_ship_arch': 'ms12_osiris',
            'faction': 'asf_grp',
            'labels': ['friend', 'asf'],
        }

        return [
            Capital('road_ku_bship', ids_name=1, **ku_bship),
            Capital('road_li_dread', ids_name=1, **li_dread),
            Capital('road_ku_destroyer1', ids_name=1, **ku_destroyer),
            Capital('road_ku_destroyer2', ids_name=1, **ku_destroyer),
            Capital('omaha1', ids_name=1, **omaha),
            Capital('omaha2', ids_name=1, **omaha),
            Capital('omaha3', ids_name=1, **omaha),

            Capital('nagato', ids_name=1, **ku_bship),

            Capital('to_bush_ku_bship', ids_name=1, **ku_bship),
            Capital('to_bush_li_dread', ids_name=1, **li_dread),

            Capital('ku_assault1', ids_name=1, **ku_bship_assault),
            Capital('ku_assault2', ids_name=1, **ku_bship_assault),
            Capital('ku_assault3', ids_name=1, **ku_bship_assault),

            Capital('ku_cr_assault1', ids_name=1, **ku_destroyer),
            Capital('ku_cr_assault2', ids_name=1, **ku_destroyer),
            Capital('ku_cr_assault3', ids_name=1, **ku_destroyer),
            Capital('ku_cr_assault4', ids_name=1, **ku_destroyer),

            Capital('li_cr_defend1', ids_name=1, **li_cruiser),
            Capital('li_cr_defend2', ids_name=1, **li_cruiser),

            Capital('osiris_on_assault', ids_name=1, **osiris),


        ]



    def get_nn_objectives(self):
        return [
            NNObj(self, 93003, name='asf_miner01', target='asf_miner01'),
            NNObj(self, 93003, name='asf_miner02', target='asf_miner02'),

            NNObj(self, 93020, name='destroy_miners'),

            NNObj(self, 93003, name='to_bush01', target='to_bush01'),
            NNObj(self, 93003, name='to_bush02', target='to_bush02'),
            NNObj(self, 93003, name='to_bush03', target='to_bush03'),
            NNObj(self, 93003, name='to_bush04', target='to_bush04'),
            NNObj(self, 93003, name='to_bush05', target='to_bush05'),
            NNObj(self, 93003, name='to_bush06', target='to_bush06'),

            NNObj(self, 93020, name='stop_assault_battleships'),
        ]

    def get_ships(self):
        return [
            Ship(
                self,
                'ku_miner_defence',
                count=5,
                affiliation=faction.KusariMain.CODE,
                system_class=S.asf_hq,
                slide_z=-50,
                labels=[
                    'miner_defence',
                    'new_order',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.KusariMain,
                    ship=ship.Dragon,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'li_miner_help',
                count=5,
                affiliation=faction.ASF.CODE,
                system_class=S.asf_hq,
                slide_z=-50,
                labels=[
                    'li_miner_help',
                    'asf',
                    'friend',
                ],
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.Defender,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'hatcher',
                jumper=True,
                actor=actors.Hatcher,
                labels=[
                    'asf',
                    'friend',
                    'trent_wing',
                ],
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.DefenderJuni,
                    level=NPC.D6,
                    equip_map=EqMap(base_level=6),
                )
            ),
            Ship(
                self,
                'darcy',
                jumper=True,
                actor=actors.Hatcher,
                labels=[
                    'asf',
                    'friend',
                    'trent_wing',
                ],
                npc=NPC(
                    faction=faction.BretoniaMain,
                    ship=ship.Cavalier,
                    level=NPC.D6,
                    equip_map=EqMap(base_level=6),
                )
            ),
            Ship(
                self,
                'alaric',
                jumper=True,
                actor=actors.Hatcher,
                labels=[
                    'asf',
                    'friend',
                    'trent_wing',
                ],
                npc=NPC(
                    faction=faction.LibertyPirate,
                    ship=ship.Hammerhead,
                    level=NPC.D6,
                    equip_map=EqMap(base_level=6),
                )
            ),

            Ship(
                self,
                'ku_f_assault1',
                count=5,
                affiliation=faction.KusariMain.CODE,
                system_class=S.asf_hq,
                slide_x=-50,
                labels=[
                    'assault',
                    'enemy_fighter',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.KusariMain,
                    ship=ship.Dragon,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'ku_f_assault2',
                count=5,
                affiliation=faction.KusariMain.CODE,
                system_class=S.asf_hq,
                slide_x=-50,
                labels=[
                    'assault',
                    'enemy_fighter',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.KusariMain,
                    ship=ship.Drake,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'li_f_defend1',
                count=5,
                affiliation=faction.ASF.CODE,
                system_class=S.asf_hq,
                slide_x=-50,
                labels=[
                    'li_fighter',
                    'asf',
                    'friend',
                ],
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.Defender,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'li_f_defend2',
                count=5,
                affiliation=faction.ASF.CODE,
                system_class=S.asf_hq,
                slide_x=-50,
                labels=[
                    'li_fighter',
                    'asf',
                    'friend',
                ],
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.Defender,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),
        ]
