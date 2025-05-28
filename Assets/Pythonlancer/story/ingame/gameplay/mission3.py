import random

from universe import sirius as S
from universe.systems import sig8, rh_kgb, rh_mnh
from story.ingame import ingame_mission
from story.math import euler_to_quat
from story import actors

from story.ingame import objectives as O
from story.ingame.tools import Point, Obj, Conn, NNObj, Ship, Solar
from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT

from world.npc import NPC, EqMap
from world import ship
from universe import faction


NPCSHIPS = '''
[NPCShipArch]
nickname = ms3_rh_gunship
loadout = rh_grp_gunboat
level = d10
ship_archetype = rh_gunboat
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER, d22

[NPCShipArch]
nickname = ms3_rh_cruiser
loadout = rh_grp_cruiser
level = d10
ship_archetype = rh_cruiser
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER, d22

[NPCShipArch]
nickname = ms3_rh_battleship
loadout = rh_battleship_01
level = d10
ship_archetype = rh_battleship
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER, d22

'''

class Misson03(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m03/m03.ini'
    FOLDER = 'M03'
    FILE = 'm03'
    START_SAVE_ID = 32300
    STATIC_NPCSHIPS = NPCSHIPS

    def get_ingame_thorns(self):
        return [
            IngameThorn(
                self,
                system_class=S.sig8,
                template=GENERIC_TWO_POINT,
                name='m03_jumphole_activation',
                points={
                    'camera': 'jh1_m2_cam',
                    'marker': 'jh1',
                },
            ),

        ]

    def get_real_objects(self):
        return {
            'starke': Obj(self, sig8.Sig8Station),
            'sig8_to_kgb': Obj(self, sig8.Sig8KoenigsbergJumphole),
            'kgb_to_rh_mnh': Obj(self, rh_kgb.KgbMunchenJumpgate),
            'final_base': Obj(self, rh_mnh.MunchOutcastBase),
        }

    def get_static_points(self):
        s8_points = [
            'm3_init_point',
            'm3_init_bship',
            'm3_init_cruiser1',
            'm3_init_cruiser2',
            'm3_init_gb1',
            'm3_init_gb2',
            'm3_init_gb3',
            'm3_init_gb4',
            'm3_init_fleet_wing',
            'm3_init_assist_wing',
            'm3_init_ship1',
            'm3_init_ship2',
            'm3_init_ship3',
            'm3_init_ship4',
            'launch_wilham',
            'launch_hassler',
        ]
        kgb_points = [
            # 'base1',
            # 'gen1',
            # 'gen2',
            'gen1_laser',
            'gen2_laser',

            'nebula_exit',
            'neb_assist',
            'neb_hassler',
            'neb_punisher1',
            'neb_punisher2',
            'neb_punisher3',
            'neb_punisher4',

            'wp_to_gen1',
            'wp_to_gen2',

            'deidrich1',
            'deidrich2',
            'deidrich3',
            'deidrich4',
            'deidrich5',
            'deidrich6',
            'deidrich7',
            'deidrich8',
            'tradepoint',

            'catcher_player',
            'catcher_hassler',
            'catcher_punisher1',
            'catcher_punisher2',
            'catcher_punisher3',
            'catcher_punisher4',

            'bsh_arrive',
            'cr1_arrive',
            'cr2_arrive',
            'gb1_arrive',
            'gb2_arrive',
            'gb3_arrive',
            'gb4_arrive',
            'wing_arrive',
            'wilham_arrive',
            'bsh_goto',
            'cr1_goto',
            'cr2_goto',
            'gb1_goto',
            'gb2_goto',
            'gb3_goto',
            'gb4_goto',

            'escaper1_start',
            'escaper2_start',
            'escaper3_start',
            'escaper4_start',

            'escaper1_goto',
            'escaper2_goto',
            'escaper3_goto',
            'escaper4_goto',

            'bsh_attack',
            'cr1_attack',
            'cr2_attack',
            'gb1_attack',
            'gb2_attack',
            'gb3_attack',
            'gb4_attack',
        ]

        defined_points = []
        for p in s8_points:
            defined_points.append(
                Point(self, S.sig8, p)
            )
        for p in kgb_points:
            defined_points.append(
                Point(self, S.rh_kgb, p)
            )

        solar_points = [
            Solar(self, S.rh_kgb, 'kgb', ru_name='Кёнигсберг'),
            Solar(self, S.rh_kgb, 'gen1', ru_name='Генератор'),
            Solar(self, S.rh_kgb, 'gen2', ru_name='Генератор'),
            Solar(self, S.rh_kgb, 'gen1_laser', ru_name='Заряжающая установка'),
            Solar(self, S.rh_kgb, 'gen2_laser', ru_name='Заряжающая установка'),
            Solar(self, S.rh_kgb, 'dock1', ru_name='Стыковочный узел 1'),
            Solar(self, S.rh_kgb, 'dock2', ru_name='Стыковочный узел 2'),
        ]

        defined_points.extend(solar_points)

        return defined_points

    def get_ships(self):
        return [
            Ship(
                self,
                'wilham',
                jumper=False,
                actor=actors.Wilham,
                labels=[
                    'rheinland',
                    'friend',
                ],
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D2,
                    equip_map=EqMap(base_level=3),
                )
            ),
            Ship(
                self,
                'hassler',
                jumper=True,
                actor=actors.Hassler,
                labels=[
                    'rheinland',
                    'friend',
                    'trent_wing',
                ],
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D2,
                    equip_map=EqMap(base_level=3),
                )
            ),
            Ship(
                self,
                'punisher',
                jumper=True,
                count=4,
                labels=[
                    'rheinland',
                    'friend',
                    'trent_wing',
                ],
                unique_npc_entry=True,
                base_name='Каратель',
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D3,
                    equip_map=EqMap(shield=4, base_level=3),
                )
            ),
            Ship(
                self,
                'assist',
                jumper=True,
                count=4,
                labels=[
                    'rheinland',
                    'friend',
                    'assistance',
                ],
                unique_npc_entry=True,
                base_name='Марадёр',
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D3,
                    equip_map=EqMap(shield=4, base_level=3),
                )
            ),
            Ship(
                self,
                'fleet_fighter',
                count=4,
                labels=[
                    'rheinland',
                    'friend',
                    'fleet_defender',
                ],
                base_name='Беркут',
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D3,
                    equip_map=EqMap(base_level=3),
                )
            ),
            Ship(
                self,
                'kgb_welcome_fighter',
                count=8,
                relative_pos=True,
                relative_range=1600,
                affiliation=faction.Corsairs.CODE,
                labels=[
                    'first_meet',
                    'corsairs',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.Corsairs,
                    ship=ship.Bloodhound,
                    level=NPC.D3,
                    equip_map=EqMap(shield=2, power=2, base_level=3),
                )
            ),
            Ship(
                self,
                'gen1_defence',
                count=5,
                affiliation=faction.DeidrichPeople.CODE,
                system_class=S.rh_kgb,
                slide_z=-50,
                labels=[
                    'gen1_defender',
                    'corsairs',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.DeidrichPeople,
                    ship=ship.Banshee,
                    level=NPC.D3,
                    equip_map=EqMap(base_level=3),
                )
            ),
            Ship(
                self,
                'gen1_reinforcement',
                count=3,
                affiliation=faction.DeidrichPeople.CODE,
                relative_pos=True,
                relative_range=1300,
                labels=[
                    'gen1_defender',
                    'corsairs',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.DeidrichPeople,
                    ship=ship.Banshee,
                    level=NPC.D3,
                    equip_map=EqMap(base_level=3),
                )
            ),
            Ship(
                self,
                'gen2_main_defence',
                count=5,
                affiliation=faction.Corsairs.CODE,
                system_class=S.rh_kgb,
                slide_z=50,
                labels=[
                    'gen2_defender',
                    'corsairs',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.Corsairs,
                    ship=ship.Bloodhound,
                    level=NPC.D3,
                    equip_map=EqMap(shield=2, base_level=3),
                )
            ),
            Ship(
                self,
                'gen2_second_defence',
                count=5,
                affiliation=faction.DeidrichPeople.CODE,
                system_class=S.rh_kgb,
                slide_z=50,
                labels=[
                    'gen2_defender',
                    'corsairs',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.DeidrichPeople,
                    ship=ship.Banshee,
                    level=NPC.D3,
                    equip_map=EqMap(shield=2, base_level=3),
                )
            ),
            Ship(
                self,
                'gen2_co_reinforcement',
                count=4,
                affiliation=faction.Corsairs.CODE,
                relative_pos=True,
                relative_range=1300,
                labels=[
                    'gen2_defender',
                    'corsairs',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.Corsairs,
                    ship=ship.Bloodhound,
                    level=NPC.D3,
                    equip_map=EqMap(base_level=3),
                )
            ),
            Ship(
                self,
                'gen2_rh_reinforcement',
                count=4,
                affiliation=faction.DeidrichPeople.CODE,
                relative_pos=True,
                relative_range=1300,
                labels=[
                    'gen2_defender',
                    'corsairs',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.DeidrichPeople,
                    ship=ship.Banshee,
                    level=NPC.D3,
                    equip_map=EqMap(base_level=3),
                )
            ),
            Ship(
                self,
                'last_defence',
                count=10,
                affiliation=faction.Corsairs.CODE,
                system_class=S.rh_kgb,
                slide_z=-60,
                labels=[
                    'defend',
                    'corsairs',
                ],
                npc=NPC(
                    faction=faction.Corsairs,
                    ship=ship.Bloodhound,
                    level=NPC.D2,
                    equip_map=EqMap(base_level=2),
                )
            ),
            Ship(
                self,
                'escaper1',
                count=3,
                affiliation=faction.Corsairs.CODE,
                system_class=S.rh_kgb,
                slide_z=-50,
                labels=[
                    'escaper',
                    'corsairs',
                ],
                npc=NPC(
                    faction=faction.Corsairs,
                    ship=ship.Bloodhound,
                    level=NPC.D2,
                    equip_map=EqMap(engine=1, base_level=3),
                )
            ),
            Ship(
                self,
                'escaper2',
                count=3,
                affiliation=faction.Corsairs.CODE,
                system_class=S.rh_kgb,
                slide_z=-50,
                labels=[
                    'escaper',
                    'corsairs',
                ],
                npc=NPC(
                    faction=faction.Corsairs,
                    ship=ship.Bloodhound,
                    level=NPC.D2,
                    equip_map=EqMap(engine=1, base_level=3),
                )
            ),
            Ship(
                self,
                'escaper3',
                count=3,
                affiliation=faction.Corsairs.CODE,
                system_class=S.rh_kgb,
                slide_z=-50,
                labels=[
                    'escaper',
                    'corsairs',
                ],
                npc=NPC(
                    faction=faction.Corsairs,
                    ship=ship.Bloodhound,
                    level=NPC.D2,
                    equip_map=EqMap(engine=1, base_level=3),
                )
            ),
            Ship(
                self,
                'escaper4',
                count=3,
                affiliation=faction.Corsairs.CODE,
                system_class=S.rh_kgb,
                slide_z=-50,
                labels=[
                    'escaper',
                    'corsairs',
                ],
                npc=NPC(
                    faction=faction.Corsairs,
                    ship=ship.Bloodhound,
                    level=NPC.D2,
                    equip_map=EqMap(engine=1, base_level=3),
                )
            ),
            Ship(
                self,
                'deidrich',
                count=1,
                labels=[
                    'deidrich_team',
                    'deidrich_the',
                    'enemy',
                ],
                actor=actors.Dietrich,
                npc=NPC(
                    faction=faction.DeidrichPeople,
                    ship=ship.Valkyrie,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=4),
                    extra_equip=[
                        'equip = attached_fx_connect01, HpRoot01',
                        'equip = attached_fx_connect02, HpRoot02',
                        'equip = attached_fx_connect03, HpRoot03',
                        'equip = rh_heavyturret06, HpTurret02',
                        'equip = rh_heavyturret06, HpTurret03',
                    ]
                )
            ),
            Ship(
                self,
                'evil_freighter',
                count=1,
                affiliation=faction.DeidrichPeople.CODE,
                labels=[
                    'deidrich_team',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.DeidrichPeople,
                    ship=ship.Humpback,
                    level=NPC.D3,
                    equip_map=EqMap(power=9, shield=9, base_level=3),
                )
            ),
            Ship(
                self,
                'evil_fighter',
                count=3,
                affiliation=faction.DeidrichPeople.CODE,
                labels=[
                    'deidrich_team',
                    'deidrich_defend',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.DeidrichPeople,
                    ship=ship.Valkyrie,
                    level=NPC.D3,
                    equip_map=EqMap(base_level=3),
                )
            ),

        ]

    def get_nn_objectives(self):
        return [
            NNObj(self, 'Встретьтесь с Вильгельмом в баре станции Штарке', name='meet_vendor', target='starke'),

            NNObj(self, O.LAUNCH, name='launch'),
            NNObj(self, O.DESTROY_CORSAIRS, name='destroy_corsairs'),

            NNObj(self, O.GOTO, name='goto_fleet', target='m3_init_point'),

            NNObj(self, O.GOTO_JUMPHOLE, name='sig8_to_kgb_fly', target='sig8_to_kgb', towards=True),
            NNObj(self, 'Ждите активации гипердыры', name='wait_for_activation'),
            NNObj(self, O.JUMPHOLE, target='sig8_to_kgb'),

            NNObj(self, O.GOTO, name='goto_nebula_exit', target='nebula_exit'),
            NNObj(self, O.GOTO, name='goto_kgb_core', target='kgb', towards=True),

            NNObj(self, 'Направлйтесь к генератору', name='goto_gen1', target='gen1', towards=True),
            NNObj(self, 'Уничтожьте генератор', name='destroy_gen1', target='gen1', nag=False),

            NNObj(self, O.GOTO, name='goto_gen2_wp1', target='wp_to_gen1', towards=True),
            NNObj(self, O.GOTO, name='goto_gen2_wp2', target='wp_to_gen2', towards=True),

            NNObj(self, 'Направляйтесь к генератору', name='goto_gen2', target='gen2', towards=True),
            NNObj(self, 'Уничтожьте генератор', name='destroy_gen2', target='gen2', nag=False),

            NNObj(self, O.CATCH_DEIDRICH, name='goto_deidrich'),

            NNObj(self, O.CATCH_DEIDRICH, name='goto_deidrich_pos2', target='deidrich2', towards=True),
            NNObj(self, O.CATCH_DEIDRICH, name='goto_deidrich_pos3', target='deidrich3', towards=True),
            NNObj(self, O.CATCH_DEIDRICH, name='goto_deidrich_pos4', target='deidrich4', towards=True),
            NNObj(self, O.CATCH_DEIDRICH, name='goto_deidrich_pos5', target='deidrich5', towards=True),
            NNObj(self, O.CATCH_DEIDRICH, name='goto_deidrich_pos6', target='deidrich6', towards=True),
            NNObj(self, O.CATCH_DEIDRICH, name='goto_deidrich_pos7', target='deidrich7', towards=True),
            NNObj(self, O.CATCH_DEIDRICH, name='goto_deidrich_pos8', target='deidrich8', towards=True),

            NNObj(self, 'Уничтожьте Дитриха', name='destroy_deidrich'),

            NNObj(self, 'Следуйте за грузовиком', name='goto_freighter', target='tradepoint', towards=True),
            NNObj(self, O.GOTO_JUMPGATE, name='kgb_to_rh_mnh_fly', target='kgb_to_rh_mnh', towards=True),
            NNObj(self, O.JUMPGATE, target='kgb_to_rh_mnh'),

            NNObj(self, O.GOTO, name='final_base_fly', target='final_base', towards=True),
            NNObj(self, 'Совершите стыковку с базой Виго', target='final_base'),
        ]
