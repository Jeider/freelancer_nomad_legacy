import random

from universe import sirius as S
from universe.systems import rh_mnh, rh_biz, sig8, li_for
from story.ingame import ingame_mission
from story.math import euler_to_quat
from story import actors

from story.ingame.tools import Point, Obj, Conn, NNObj, Ship, Solar
from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT

from world.npc import NPC, EqMap
from world import ship
from universe import faction

NPCSHIPS = '''

[NPCShipArch]
nickname = ms4_rh_battleship_ship
loadout = rh_battleship_01
level = d10
ship_archetype = rh_battleship_ms4
pilot = cruiser_default_lowgun
state_graph = CRUISER
npc_class = lawful, CRUISER

[NPCShipArch]
nickname = ms4_rh_cruiser_ship
loadout = rh_grp_cruiser
level = d10
ship_archetype = rh_cruiser
pilot = cruiser_default_lowgun
state_graph = CRUISER
npc_class = lawful, CRUISER

[NPCShipArch]
nickname = ms4_rh_gunboat_ship
loadout = rh_grp_gunboat_no_torpedoes
level = d10
ship_archetype = rh_gunboat
pilot = cruiser_default_lowgun
state_graph = CRUISER
npc_class = lawful, CRUISER, d22
'''



class Misson04(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m04/m04.ini'
    FOLDER = 'M04'
    FILE = 'm04'
    STATIC_NPCSHIPS = NPCSHIPS

    def get_real_objects(self):
        return {
            'vendor_planet': Obj(self, rh_mnh.MunchDockring),
            'mnh_tlr_1': Conn(self, rh_mnh.MunchCivRuinsConn2, rh_mnh.MunchDockring),
            'mnh_tlr_2': Conn(self, rh_mnh.MunchCivRuinsConn1, rh_mnh.MunchCivilianStationRuins),
            'mnh_to_biz': Obj(self, rh_mnh.MunchBizmarkJumpgate),

            'keln': Obj(self, rh_biz.BizmarkMilitary),
            'biz_to_sig8': Obj(self, rh_biz.BizmarkSigma8Jumphole),

            'sig8_to_for': Obj(self, sig8.Sig8ForbesJumphole),

            'shipyard': Obj(self, li_for.ForbesShipyard),
            'for_tlr_1': Conn(self, li_for.ForbesPlanetConn2, li_for.ForbesShipyard),
            'final_planet': Obj(self, li_for.ForbesPlanet1),
        }

    def get_nn_objectives(self):
        return [
            NNObj(self, 94001, name='meet_vendor', target='vendor_planet'),

            NNObj(self, 94003, name='launch'),

            NNObj(self, 94005, target='mnh_tlr_1'),
            NNObj(self, 94005, target='mnh_tlr_2'),
            NNObj(self, 94006, target='mnh_to_biz'),

            NNObj(self, 94008, name='follow_officer'),
            NNObj(self, 94009, name='destroy_keln_enemy'),

            NNObj(self, 94010, name='destroy_reactor', target='bs_reactor', nag=False),

            NNObj(self, 94011, name='biz_to_sig8_fly', target='biz_to_sig8', towards=True),
            NNObj(self, 94012, target='biz_to_sig8'),

            NNObj(self, 94013, name='defend_jacobo'),
            NNObj(self, 94014, name='destroy_fighters'),

            NNObj(self, 94015, name='goto_escape_point1', target='point_escape1', towards=True),
            NNObj(self, 94015, name='goto_escape_point2', target='point_escape2', towards=True),

            NNObj(self, 94016, name='destroy_corsairs'),


            #
            # NNObj(self, 92007, target='om15_tlr_1'),
            # NNObj(self, 92008, target='om15_jacobo_miner'),
            # NNObj(self, 92010, name='scan_wp1', target='waypoint1'),
            # NNObj(self, 92010, name='scan_wp2', target='waypoint2'),
            #
            #
            #
            #
            # NNObj(self, 93020, name='destroy_corsairs'),

        ]

    '''

    [NNObjective]
    nickname = ms4_13_destroy_corsairs
    state = HIDDEN
    type = ids, 094016

    [NNObjective]
    nickname = ms4_14_go_to_forbes_jumphole
    state = HIDDEN
    type = rep_inst, sig8, 094017, 094017, 40000, 0, 40000, sig8_to_for

    [NNObjective]
    nickname = ms4_15_wait_for_activation
    state = HIDDEN
    type = ids, 094018

    [NNObjective]
    nickname = ms4_16_be_near_jumphole
    state = HIDDEN
    type = rep_inst, sig8, 094019, 094019, 40000, 0, 40000, sig8_to_for

    [NNObjective]
    nickname = ms4_16_use_jumphole
    state = HIDDEN
    type = rep_inst, sig8, 094019, 094019, 40000, 0, 40000, sig8_to_for

    [NNObjective]
    nickname = ms4_17_go_to_shipyard
    state = HIDDEN
    type = rep_inst, li_for, 094020, 094020, 25000, -18000, 44000, li_for_03

    [NNObjective]
    nickname = ms4_18_use_tradelane
    state = HIDDEN
    type = rep_inst, li_for, 094021, 094021, 25187, -18208, 40695, LI_FOR_F_Trade_Lane_Ring_L2_06

    [NNObjective]
    nickname = ms4_19_dock_on_planet_forbes
    state = HIDDEN
    type = rep_inst, li_for, 094022, 094022, 31888, 0, -24814, li_for_dock_ring

    [NNObjective]
    nickname = ms4_20_meet_hatcher_in_bar
    state = HIDDEN
    type = ids, 094023

    '''
    def get_static_points(self):
        biz_points = [
            'officer_init',
            'arrest_player',
            'arrest_jacobo',
            'officer_flyback',
            'officer_flyback1',
            'officer_flyback2',
            'officer_flyback3',
            'officer_flyback4',
            'to_keln1',
            'to_keln2',
            'gb1',
            'gb2',
            'gb3',
            'cr1',
            'cr2',
            'keln_hassler',
            'keln_alaric',
            'keln_player',
            'keln_jacobo',
            'keln_officer'
        ]

        sig8_points = [
            'point_escape1',
            'point_escape2',
            'ms4_cr1',
            'ms4_cr2',
        ]

        defined_points = [
            Point(self, S.rh_mnh, 'jacobo_init'),
        ]
        for p in biz_points:
            defined_points.append(
                Point(self, S.rh_biz, p)
            )
        for p in sig8_points:
            defined_points.append(
                Point(self, S.sig8, p)
            )

        solar_points = [
            Solar(self, S.rh_biz, 'bs'),
            Solar(self, S.rh_biz, 'bs_reactor'),
        ]

        defined_points.extend(solar_points)

        return defined_points

    def get_ships(self):
        return [
            Ship(
                self,
                'jacobo',
                jumper=True,
                labels=[
                    'friend',
                ],
                actor=actors.Jacobo,
                npc=NPC(
                    faction=faction.Outcasts,
                    ship=ship.Dromader,
                    level=NPC.D4,
                    equip_map=EqMap(base_level=3),
                )
            ),
            Ship(
                self,
                'hassler',
                jumper=True,
                actor=actors.Hassler,
                labels=[
                    'friend',
                    'friend_fighter',
                ],
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D4,
                    equip_map=EqMap(base_level=4),
                )
            ),
            Ship(
                self,
                'alaric',
                jumper=True,
                actor=actors.Alaric,
                labels=[
                    'friend',
                    'friend_fighter',
                ],
                npc=NPC(
                    faction=faction.AlaricLike,
                    ship=ship.Barracuda,
                    level=NPC.D4,
                    equip_map=EqMap(base_level=4),
                )
            ),
            Ship(
                self,
                'officer_wing',
                count=5,
                labels=[
                    'officer',
                    'rheinland',
                ],
                unique_npc_entry=True,
                name_ids=[
                    94205,
                ],
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D4,
                    equip_map=EqMap(base_level=4),
                )
            ),
            Ship(
                self,
                'keln_reinforcement',
                count=6,
                relative_pos=True,
                relative_range=1500,
                labels=[
                    'keln',
                    'rheinland',
                ],
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D4,
                    equip_map=EqMap(base_level=4),
                )
            ),

        ]
