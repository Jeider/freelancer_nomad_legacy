from templates.space_object_template import SpaceObjectTemplate


class MegaCannon(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'br_wrw_03'
    TEMPLATE = '''[Object]
nickname = br_wrw_03
ids_name = 203704
pos = -1280, 500, -320
rotate = 0, 0, 0
archetype = gun_core
ids_info = 065621
reputation = br_grp
behavior = NOTHING
difficulty_level = 12
base = br_wrw_03_base

[Object]
nickname = br_wrw_03_dock
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_shipping01
reputation = br_grp
behavior = NOTHING
difficulty_level = 12
dock_with = br_wrw_03_base
base = br_wrw_03_base
voice = atc_leg_f01
space_costume = br_newscaster_head_gen_hat, br_female_elite_body, prop_hat_female_br_elite
ids_name = 196722
ids_info = 065739

[Object]
nickname = br_wrw_03_BARREL_POLYGON01
pos = -1280, 915, -20
archetype = the_barrel
loadout = the_barrel_attacher
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_RING_single_ind01
pos = -1280, 1180, -640
rotate = 0, 90, 0
archetype = space_industrial02a
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_RING_single_ind02
pos = -1045, 1040, -640
rotate = 60, 90, 0
archetype = space_industrial02a
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_RING_single_ind03
pos = -1045, 770, -640
rotate = 120, 90, 0
archetype = space_industrial02a
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_RING_single_ind04
pos = -1280, 635, -640
rotate = 0, 90, 0
archetype = space_industrial02a
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_RING_single_ind05
pos = -1515, 770, -640
rotate = 60, 90, 0
archetype = space_industrial02a
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_RING_single_ind06
pos = -1515, 1040, -640
rotate = 120, 90, 0
archetype = space_industrial02a
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_RING_space_girder01
pos = -1280, 1085, -407
rotate = 30, 0, 0
archetype = space_girder
parent = br_wrw_03
;loadout = the_barrel_prebarrel_power

[Object]
nickname = br_wrw_03_BARREL_RING_space_girder02
pos = -1280, 730, -407
rotate = -30, 0, 0
archetype = space_girder
parent = br_wrw_03
;loadout = the_barrel_prebarrel_power

[Object]
nickname = br_wrw_03_BARREL_RING_space_girder03
pos = -1435, 990, -407
rotate = 0, -30, 150
archetype = space_girder
parent = br_wrw_03
;loadout = the_barrel_prebarrel_power

[Object]
nickname = br_wrw_03_BARREL_RING_space_girder04
pos = -1435, 815, -407
rotate = 0, -30, 210
archetype = space_girder
parent = br_wrw_03
;loadout = the_barrel_prebarrel_power

[Object]
nickname = br_wrw_03_BARREL_RING_space_girder05
pos = -1125, 815, -407
rotate = 0, -30, -30
archetype = space_girder
parent = br_wrw_03
;loadout = the_barrel_prebarrel_power

[Object]
nickname = br_wrw_03_BARREL_RING_space_girder06
pos = -1125, 990, -407
rotate = 0, -30, 30
archetype = space_girder
parent = br_wrw_03
;loadout = the_barrel_prebarrel_power

;-29865,8610,4790
;-29865,8600,4830
;angle -65 on X


[Object]
nickname = br_wrw_03_BARREL_RING_space_girder05a
pos = -1415, 610, -150
rotate = -65, 0, 0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_RING_space_girder06a
pos = -1415, 600, -110
rotate = -65, 0, 0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_RING_space_girder07
pos = -1145, 610, -150
rotate = -65, 0, 0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_RING_space_girder08
pos = -1145, 600, -110
rotate = -65, 0, 0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_RING_space_ind01
pos = -1280, 1480, -640
rotate = 90, 0, 0
archetype = space_industrial01
parent = br_wrw_03
;loadout = the_barrel_center_power

[Object]
nickname = br_wrw_03_BARREL_RING_space_ind02
pos = -780, 1190, -640
rotate = 60, 90, -90
archetype = space_industrial01
parent = br_wrw_03
;loadout = the_barrel_center_power

[Object]
nickname = br_wrw_03_BARREL_RING_space_ind03
pos = -780, 620, -640
rotate = 120, 90, -90
archetype = space_industrial01
parent = br_wrw_03
;loadout = the_barrel_center_power

[Object]
nickname = br_wrw_03_BARREL_RING_space_ind04
pos = -1280, 350, -640
rotate = -90, 0, 0
archetype = space_industrial01
parent = br_wrw_03
;loadout = the_barrel_center_power

[Object]
nickname = br_wrw_03_BARREL_RING_space_ind05
pos = -1780, 620, -640
rotate = -120, 90, -90
archetype = space_industrial01
parent = br_wrw_03
;loadout = the_barrel_center_power

[Object]
nickname = br_wrw_03_BARREL_RING_space_ind06
pos = -1780, 1190, -640
rotate = -60, 90, -90
archetype = space_industrial01
parent = br_wrw_03
;loadout = the_barrel_center_power

[Object]
nickname = br_wrw_03_BARREL_CONNECT_space_ind01
pos = -1415, 350, -250
rotate = -65, 0, 0
archetype = space_industrial
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_CONNECT_space_ind02
pos = -1145, 350, -250
rotate = -65, 0, 0
archetype = space_industrial
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_CONNECT_space_ind03
pos = -1280, 140, -250
rotate = 0, 90, 0
archetype = space_industrial02a
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_CONNECT_space_ind04
pos = -1280, 350, -395
rotate = 90, 0, 0
archetype = space_industrial02a
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_CONNECT_space_ind05
pos = -1280, 350, -250
rotate = 90, 0, 0
archetype = space_industrial02a
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_CONNECT_space_ind06
pos = -1280, 140, -395
rotate = 0, 90, 0
archetype = space_industrial02a
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_CONNECT_space_ind07
pos = -1280, 140, 170
rotate = 0, 180, 0
archetype = space_industrial
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_CONNECT_space_ind08
pos = -1280, 140, -815
rotate = 0, 0, 0
archetype = space_industrial
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_CONNECT_space_ind09
pos = -785, 140, -322
rotate = 0, -90, 0
archetype = space_industrial
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_CONNECT_space_ind10
pos = -1390, 450, -490
rotate = -160, 0, 0
archetype = space_industrial
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_CONNECT_space_ind11
pos = -1390.5, 606.5, -920
rotate = 20,0,0
archetype = space_industrial
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_CONNECT_space_ind12
pos = -1170, 450, -490
rotate = -160, 0, 0
archetype = space_industrial
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_CONNECT_space_ind13
pos = -1170.5, 606.5, -920
rotate = 20, 0, 0
archetype = space_industrial
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_CONNECT_space_girder01
pos = -1190, 606.5, -830
rotate = 0, 0, 0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_CONNECT_space_girder02
pos = -1190, 630, -830
rotate = 0, 0, 0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_CONNECT_space_girder03
pos = -1370, 606.5, -830
rotate = 0, 0, 0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_CONNECT_space_girder04
pos = -1370, 630, -830
rotate = 0, 0, 0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_CONNECT_space_ind14
pos = -930, 140, 10
rotate = 0, -135, 0
archetype = space_industrial
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_CONNECT_space_ind15
pos = -930, 140, -690
rotate = 0, -45, 0
archetype = space_industrial
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_CONNECT_space_ind16
pos = -1630, 140, -690
rotate = 0, 45, 0
archetype = space_industrial
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_CONNECT_space_ind17
pos = -1630, 140, 10
rotate = 0, 135, 0
archetype = space_industrial
parent = br_wrw_03

[Object]
nickname = br_wrw_03_BARREL_CONNECT_space_ind18
pos = -1735, 140, -322
rotate = 0, 90, 0
archetype = space_industrial
parent = br_wrw_03




;GUN

[Object]
nickname = br_wrw_03_GUN_single_ind01
pos = -1280, 920, -1290
rotate = 0, 0, 45
archetype = space_industrial01a
parent = br_wrw_03

[Object]
nickname = br_wrw_03_GUN_space_girder01
pos = -1330, 920, -990
rotate = 0, 0, 0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_GUN_space_girder02
pos = -1230, 920, -990
rotate = 0, 0, 0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_GUN_space_girder03
pos = -1280, 970, -990
rotate = 0, 0, 0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_GUN_space_girder04
pos = -1280, 870, -990
rotate = 0, 0, 0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_GUN_space_girder05
pos = -1280, 920, -1210
rotate = 0, 0, 0
archetype = space_girder
parent = br_wrw_03
;loadout = the_barrel_first_beamer

[Object]
nickname = br_wrw_03_GUN_single_ind02
pos = -1178, 1025, -1290
rotate = 0, 0, 45
archetype = space_industrial02a
parent = br_wrw_03

[Object]
nickname = br_wrw_03_GUN_single_ind03
pos = -1382, 1025, -1290
rotate = 0, 0, 45
archetype = space_industrial02a
parent = br_wrw_03

[Object]
nickname = br_wrw_03_GUN_single_ind04
pos = -1178, 818, -1290
rotate = 0, 0, -45
archetype = space_industrial02a
parent = br_wrw_03

[Object]
nickname = br_wrw_03_GUN_single_ind05
pos = -1382, 818, -1290
rotate = 0, 0, -45
archetype = space_industrial02a
parent = br_wrw_03

[Object]
nickname = br_wrw_03_GUN_space_girder06
pos = -1170, 720, -1080
rotate = -135, 0, 0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_GUN_space_girder07
pos = -1170, 720, -1120
rotate = -135, 0, 0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_GUN_space_girder08
pos = -1390, 720, -1080
rotate = -135, 0, 0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_GUN_space_girder09
pos = -1390, 720, -1120
rotate = -135, 0, 0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_GUN_space_girder10
pos = -1390.5, 520, -760
rotate = 20, 0, 0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_GUN_space_girder11
pos = -1390.5, 560, -720
rotate = 20, 0, 0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_GUN_space_girder12
pos = -1170.5, 520, -760
rotate = 20, 0, 0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_GUN_space_girder13
pos = -1170.5, 560, -720
rotate = 20, 0, 0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_GUN_space_panel01
pos = -1060, 920, -1290
rotate = 0, 90, 0
archetype = space_panel
parent = br_wrw_03

[Object]
nickname = br_wrw_03_GUN_space_panel02
pos = -1280, 700, -1290
rotate = 0, 90, 0
archetype = space_panel
parent = br_wrw_03

[Object]
nickname = br_wrw_03_GUN_space_panel03
pos = -1500, 920, -1290
rotate = 0, 90, 0
archetype = space_panel
parent = br_wrw_03

[Object]
nickname = br_wrw_03_GUN_space_panel04
pos = -1280, 1140, -1290
rotate = 0, 90,0
archetype = space_panel
parent = br_wrw_03

[Object]
nickname = br_wrw_03_GUN_space_panel05
pos = -1280, 920, -1430
rotate = 0, 90,0
archetype = space_panel
parent = br_wrw_03
spin = 20, 0, 0

;Placement

[Object]
nickname = br_wrw_03_PLACE_space_ind01
pos = -1280, 0, 170
rotate = 0, 90,0
archetype = space_industrial02a
parent = br_wrw_03

[Object]
nickname = br_wrw_03_PLACE_space_ind02
pos = -930, 0, 10
rotate = 0, -45,0
archetype = space_industrial02a
parent = br_wrw_03

[Object]
nickname = br_wrw_03_PLACE_space_ind03
pos = -785, 0, -322
rotate = 0, 0,0
archetype = space_industrial02a
parent = br_wrw_03

[Object]
nickname = br_wrw_03_PLACE_space_ind04
pos = -930, 0, -690
rotate = 0, 45,0
archetype = space_industrial02a
parent = br_wrw_03

[Object]
nickname = br_wrw_03_PLACE_space_ind05
pos = -1280, 0, -815
rotate = 0, 90,0
archetype = space_industrial02a
parent = br_wrw_03

[Object]
nickname = br_wrw_03_PLACE_space_ind06
pos = -1630, 0, -690
rotate = 0, -45,0
archetype = space_industrial02a
parent = br_wrw_03

[Object]
nickname = br_wrw_03_PLACE_space_ind07
pos = -1735, 0, -322
rotate = 0, 0,0
archetype = space_industrial02a
parent = br_wrw_03

[Object]
nickname = br_wrw_03_PLACE_space_ind08
pos = -1630, 0, 10
rotate = 0, 45,0
archetype = space_industrial02a
parent = br_wrw_03

[Object]
nickname = br_wrw_03_PLACE_space_girder01
pos = -1080, 0, 90
rotate = 0, 118,0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_PLACE_space_girder02
pos = -880, 0, -90
rotate = 0, 150,0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_PLACE_space_girder03
pos = -880, 0, -590
rotate = 0, -155,0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_PLACE_space_girder04
pos = -1060, 0, -760
rotate = 0,-105,0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_PLACE_space_girder05
pos = -1500, 0, -760
rotate = 0, 105,0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_PLACE_space_girder06
pos = -1730, 0, -490
rotate = 0, 165,0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_PLACE_space_girder07
pos = -1710, 0, -190
rotate = 0, -165,0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_PLACE_space_girder08
pos = -1480, 0, 90
rotate = 0, -118,0
archetype = space_girder
parent = br_wrw_03

;REACTOR

[Object]
nickname = br_wrw_03_REACTOR_space_ind01
pos = -880, 0, -1210
rotate = 0, 0,0
archetype = space_industrial02
parent = br_wrw_03

[Object]
nickname = br_wrw_03_REACTOR_space_ind02
pos = -1280, 0, -1210
rotate = 0, 0,0
archetype = space_industrial02
parent = br_wrw_03

[Object]
nickname = br_wrw_03_REACTOR_space_ind03
pos = -1680, 0, -1210
rotate = 0, 0,0
archetype = space_industrial02
parent = br_wrw_03

[Object]
nickname = br_wrw_03_REACTOR_space_ind04
pos = -880, 0, -1610
rotate = 0, 0,0
archetype = space_industrial02
parent = br_wrw_03

[Object]
nickname = br_wrw_03_REACTOR_space_ind05
pos = -1280, 0, -1610
rotate = 0, 0,0
archetype = space_industrial02
parent = br_wrw_03

[Object]
nickname = br_wrw_03_REACTOR_space_ind06
pos = -1680, 0, -1610
rotate = 0, 0,0
archetype = space_industrial02
parent = br_wrw_03

[Object]
nickname = br_wrw_03_REACTOR_space_ind07
pos = -880, 0, -2010
rotate = 0, 0,0
archetype = space_industrial02
parent = br_wrw_03

[Object]
nickname = br_wrw_03_REACTOR_space_ind08
pos = -1280, 0, -2010
rotate = 0, 0,0
archetype = space_industrial02
parent = br_wrw_03

[Object]
nickname = br_wrw_03_REACTOR_space_ind09
pos = -1680, 0, -2010
rotate = 0, 0,0
archetype = space_industrial02
parent = br_wrw_03

;REACTOR POWER PLANTS

[Object]
nickname = br_wrw_03_REACTOR_space_ind10
pos = -1280, -420, -1210
rotate = -90, 0, 0
archetype = space_industrial01
parent = br_wrw_03
loadout = space_ind01_reactor

[Object]
nickname = br_wrw_03_REACTOR_space_ind11
pos = -1280, -420, -1610
rotate = -90, 0, 0
archetype = space_industrial01
parent = br_wrw_03
loadout = space_ind01_reactor

[Object]
nickname = br_wrw_03_REACTOR_space_ind12
pos = -1280, -420, -2010
rotate = -90, 0, 0
archetype = space_industrial01
parent = br_wrw_03
loadout = space_ind01_reactor

[Object]
nickname = br_wrw_03_REACTOR_single_ind01
pos = -880, -204, -1210
rotate = -90, 0, 0
archetype = space_industrial01a
parent = br_wrw_03
loadout = space_ind01_reactor

[Object]
nickname = br_wrw_03_REACTOR_single_ind02
pos = -678, 0, -1210
rotate = 0, 90, 0
archetype = space_industrial01a
parent = br_wrw_03
loadout = space_ind01_reactor

[Object]
nickname = br_wrw_03_REACTOR_single_ind03
pos = -880, 204, -1210
rotate = 90, 0, 0
archetype = space_industrial01a
parent = br_wrw_03
loadout = space_ind01_reactor

[Object]
nickname = br_wrw_03_REACTOR_single_ind04
pos = -1280, 204, -1210
rotate = 90, 0, 0
archetype = space_industrial01a
parent = br_wrw_03
loadout = space_ind01_reactor

[Object]
nickname = br_wrw_03_REACTOR_single_ind05
pos = -1680, 204, -1210
rotate = 90, 0, 0
archetype = space_industrial01a
parent = br_wrw_03
loadout = space_ind01_reactor

[Object]
nickname = br_wrw_03_REACTOR_single_ind06
pos = -1882, 0, -1210
rotate = 0, 90, 0
archetype = space_industrial01a
parent = br_wrw_03
loadout = space_ind01_reactor

[Object]
nickname = br_wrw_03_REACTOR_single_ind07
pos = -1680, -204, -1210
rotate = 90, 0, 0
archetype = space_industrial01a
parent = br_wrw_03
loadout = space_ind01_reactor

[Object]
nickname = br_wrw_03_REACTOR_single_ind08
pos = -880, -204, -1610
rotate = -90, 0, 0
archetype = space_industrial01a
parent = br_wrw_03
loadout = space_ind01_reactor

[Object]
nickname = br_wrw_03_REACTOR_single_ind09
pos = -678, 0, -1610
rotate = 0, 90, 0
archetype = space_industrial01a
parent = br_wrw_03
loadout = space_ind01_reactor

[Object]
nickname = br_wrw_03_REACTOR_single_ind10
pos = -880, 204, -1610
rotate = 90, 0, 0
archetype = space_industrial01a
parent = br_wrw_03
loadout = space_ind01_reactor

[Object]
nickname = br_wrw_03_REACTOR_single_ind11
pos = -1280, 204, -1610
rotate = 90, 0, 0
archetype = space_industrial01a
parent = br_wrw_03
loadout = space_ind01_reactor

[Object]
nickname = br_wrw_03_REACTOR_single_ind12
pos = -1680, 204, -1610
rotate = 90, 0, 0
archetype = space_industrial01a
parent = br_wrw_03
loadout = space_ind01_reactor

[Object]
nickname = br_wrw_03_REACTOR_single_ind13
pos = -1882, 0, -1610
rotate = 0, 90, 0
archetype = space_industrial01a
parent = br_wrw_03
loadout = space_ind01_reactor

[Object]
nickname = br_wrw_03_REACTOR_single_ind14
pos = -1680, -204, -2010
rotate = 90, 0, 0
archetype = space_industrial01a
parent = br_wrw_03
loadout = space_ind01_reactor

[Object]
nickname = br_wrw_03_REACTOR_single_ind15
pos = -880, -204, -2010
rotate = -90, 0, 0
archetype = space_industrial01a
parent = br_wrw_03
loadout = space_ind01_reactor

[Object]
nickname = br_wrw_03_REACTOR_single_ind16
pos = -678, 0, -2010
rotate = 0, 90, 0
archetype = space_industrial01a
parent = br_wrw_03
loadout = space_ind01_reactor

[Object]
nickname = br_wrw_03_REACTOR_single_ind17
pos = -880, 204, -2010
rotate = 90, 0, 0
archetype = space_industrial01a
parent = br_wrw_03
loadout = space_ind01_reactor

[Object]
nickname = br_wrw_03_REACTOR_single_ind18
pos = -1280, 204, -2010
rotate = 90, 0, 0
archetype = space_industrial01a
parent = br_wrw_03
loadout = space_ind01_reactor

[Object]
nickname = br_wrw_03_REACTOR_single_ind19
pos = -1680, 204, -2010
rotate = 90, 0, 0
archetype = space_industrial01a
parent = br_wrw_03
loadout = space_ind01_reactor

[Object]
nickname = br_wrw_03_REACTOR_single_ind20
pos = -1882, 0, -2010
rotate = 0, 90, 0
archetype = space_industrial01a
parent = br_wrw_03
loadout = space_ind01_reactor

[Object]
nickname = br_wrw_03_REACTOR_single_ind21
pos = -1680, -204, -2010
rotate = 90, 0, 0
archetype = space_industrial01a
parent = br_wrw_03
loadout = space_ind01_reactor

;ENGINE

[Object]
nickname = br_wrw_03_REACTOR_space_panel01
pos = -1680, 0, -2140
rotate = 0, 90, 0
archetype = space_panel
parent = br_wrw_03

[Object]
nickname = br_wrw_03_REACTOR_space_panel02
pos = -1280, 0, -2140
rotate = 0, 90, 0
archetype = space_panel
parent = br_wrw_03

[Object]
nickname = br_wrw_03_REACTOR_space_panel03
pos = -880, 0, -2140
rotate = 0, 90, 0
archetype = space_panel
parent = br_wrw_03

;STORAGE BLOCK

[Object]
nickname = br_wrw_03_STORAGE_space_ind01
pos = -1680, 0, 535
rotate = 0, 180,0
archetype = space_industrial
parent = br_wrw_03

[Object]
nickname = br_wrw_03_STORAGE_space_ind02
pos = -880, 0, 535
rotate = 0, 180,0
archetype = space_industrial
parent = br_wrw_03

[Object]
nickname = br_wrw_03_STORAGE_space_ind03
pos = -1680, 0, 1895
rotate = 0, 180,0
archetype = space_industrial
parent = br_wrw_03

[Object]
nickname = br_wrw_03_STORAGE_space_ind04
pos = -880, 0, 1895
rotate = 0, 180,0
archetype = space_industrial
parent = br_wrw_03

[Object]
nickname = br_wrw_03_STORAGE_space_girder01
pos = -1680, 0, 850
rotate = 0, 0,0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_STORAGE_space_girder02
pos = -880, 0, 850
rotate = 0, 0,0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_STORAGE_space_girder03
pos = -1680, 0, 1230
rotate = 0, 0,0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_STORAGE_space_girder04
pos = -880, 0, 1230
rotate = 0, 0,0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_STORAGE_space_tanks01
pos = -1550, 0, 860
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_wrw_03

[Object]
nickname = br_wrw_03_STORAGE_space_tanks02
pos = -1285, 0, 860
rotate = 0,90,0
archetype = space_tankl4x4
parent = br_wrw_03

[Object]
nickname = br_wrw_03_STORAGE_space_tanks03
pos = -1020, 0, 860
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_wrw_03

[Object]
nickname = br_wrw_03_STORAGE_space_tanks04
pos = -1550, 0, 1060
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_wrw_03

[Object]
nickname = br_wrw_03_STORAGE_space_tanks05
pos = -1285, 0, 1060
rotate = 0,90,0
archetype = space_tankl4x4
parent = br_wrw_03

[Object]
nickname = br_wrw_03_STORAGE_space_tanks06
pos = -1020, 0, 1060
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_wrw_03

[Object]
nickname = br_wrw_03_STORAGE_space_tanks07
pos = -1550, 0, 1260
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_wrw_03

[Object]
nickname = br_wrw_03_STORAGE_space_tanks08
pos = -1285, 0, 1260
rotate = 0,90,0
archetype = space_tankl4x4
parent = br_wrw_03

[Object]
nickname = br_wrw_03_STORAGE_space_tanks09
pos = -1020, 0, 1260
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_wrw_03

[Object]
nickname = br_wrw_03_STORAGE_space_tanks10
pos = -1550, 0, 1460
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_wrw_03

[Object]
nickname = br_wrw_03_STORAGE_space_tanks11
pos = -1285, 0, 1460
rotate = 0,90,0
archetype = space_tankl4x4
parent = br_wrw_03

[Object]
nickname = br_wrw_03_STORAGE_space_tanks12
pos = -1020, 0, 1460
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_wrw_03


[Object]
nickname = br_wrw_03_STORAGE_space_tanks13
pos = -1550, 0, 1660
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_wrw_03

[Object]
nickname = br_wrw_03_STORAGE_space_tanks14
pos = -1285, 0, 1660
rotate = 0,90,0
archetype = space_tankl4x4
parent = br_wrw_03

[Object]
nickname = br_wrw_03_STORAGE_space_tanks15
pos = -1020, 0, 1660
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_wrw_03


;Citizen block

[Object]
nickname = br_wrw_03_CITY_space_ind01
pos = -2160, 0, -740
rotate = 0, 90, 0
archetype = space_industrial
parent = br_wrw_03

[Object]
nickname = br_wrw_03_CITY_space_ind02
pos = -2160, 0, 60
rotate = 0, 90, 0
archetype = space_industrial
parent = br_wrw_03

[Object]
nickname = br_wrw_03_CITY_space_ind03
pos = -2160, 0, -321
rotate = 0, 90, 0
archetype = space_industrial
parent = br_wrw_03

[Object]
nickname = br_wrw_03_CITY_space_ind04
pos = -2560, 0, -740
rotate = 0, 90, 0
archetype = space_industrial
parent = br_wrw_03

[Object]
nickname = br_wrw_03_CITY_space_ind05
pos = -2560, 0, -321
rotate = 0, 90, 0
archetype = space_industrial
parent = br_wrw_03

[Object]
nickname = br_wrw_03_CITY_space_ind06
pos = -2960, 0, -740
rotate = 0, 90, 0
archetype = space_industrial
parent = br_wrw_03

[Object]
nickname = br_wrw_03_CITY_space_ind07
pos = -2560, 0, -1155
rotate = 0, 0, 0
archetype = space_industrial02
parent = br_wrw_03

[Object]
nickname = br_wrw_03_CITY_space_ind08
pos = -2960, 0, -1155
rotate = 0, 0, 0
archetype = space_industrial02
parent = br_wrw_03

[Object]
nickname = br_wrw_03_CITY_space_panel01
pos = -2560, 0, -1282
rotate = 0, 90, 0
archetype = space_panel
parent = br_wrw_03

[Object]
nickname = br_wrw_03_CITY_space_panel02
pos = -2960, 0, -1282
rotate = 0, 90, 0
archetype = space_panel
parent = br_wrw_03

[Object]
nickname = br_wrw_03_CITY_space_dome01
pos = -2960, 20, -375
rotate = 0,180, 0
archetype = space_dome
parent = br_wrw_03

[Object]
nickname = br_wrw_03_CITY_space_dome02
pos = -2560, 20, 45
rotate = 0, 180, 0
archetype = space_dome
parent = br_wrw_03

[Object]
nickname = br_wrw_03_CITY_space_dome03
pos = -2160, 20, 425
rotate = 0, 180, 0
archetype = space_dome
parent = br_wrw_03

[Object]
nickname = br_wrw_03_CITY_space_girder01
pos = -2160, 0, -540
rotate = 0, 0, 0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_CITY_space_girder02
pos = -2560, 0, -540
rotate = 0, 0, 0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_CITY_space_girder03
pos = -2160, 0, -140
rotate = 0, 0, 0
archetype = space_girder
parent = br_wrw_03

[Object]
nickname = br_wrw_03_CITY_space_hab_wide01
pos = -2160, 145, -740
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_wrw_03

[Object]
nickname = br_wrw_03_CITY_space_hab_wide02
pos = -2160, -142, -740
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_wrw_03

[Object]
nickname = br_wrw_03_CITY_space_hab_wide03
pos = -2160, 145, -321
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_wrw_03

[Object]
nickname = br_wrw_03_CITY_space_hab_wide04
pos = -2160, 300, -321
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_wrw_03

[Object]
nickname = br_wrw_03_CITY_space_hab_wide05
pos = -2160, -142, -321
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_wrw_03

[Object]
nickname = br_wrw_03_CITY_space_hab_wide06
pos = -2160, 145, 60
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_wrw_03

[Object]
nickname = br_wrw_03_CITY_space_hab_wide07
pos = -2160, -142, 60
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_wrw_03

[Object]
nickname = br_wrw_03_CITY_space_hab_wide08
pos = -2560, 145, -321
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_wrw_03

[Object]
nickname = br_wrw_03_CITY_space_hab_wide09
pos = -2560, -142, -321
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_wrw_03

[Object]
nickname = br_wrw_03_CITY_space_hab_wide10
pos = -2960, -142, -740
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_wrw_03

[Object]
nickname = br_wrw_03_CITY_space_hab_wide11
pos = -2960, 145, -740
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_wrw_03

[Object]
nickname = br_wrw_03_CITY_space_hab_wide12
pos = -2560, -142, -740
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_wrw_03

[Object]
nickname = br_wrw_03_CITY_space_hab_tall01
pos = -2560, 208, -740
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = br_wrw_03

[Object]
nickname = br_wrw_03_CITY_space_hab_tall02
pos = -2160, 363, 60
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = br_wrw_03

;DOCK BLOCK

[Object]
nickname = br_wrw_03_DOCK_space_ind01
pos = -400, 0, -735
rotate = 0, -90, 0
archetype = space_industrial
parent = br_wrw_03

[Object]
nickname = br_wrw_03_DOCK_space_ind02
pos = 0, 0, -735
rotate = 0, -90, 0
archetype = space_industrial
parent = br_wrw_03

[Object]
nickname = br_wrw_03_DOCK_space_ind03
pos = 400, 0, -735
rotate = 0, -90, 0
archetype = space_industrial
parent = br_wrw_03

[Object]
nickname = br_wrw_03_DOCK_space_ind04
pos = 0, 0, -1155
rotate = 0, 0, 0
archetype = space_industrial02
parent = br_wrw_03

[Object]
nickname = br_wrw_03_DOCK_space_ind05
pos = 400, 0, -1155
rotate = 0, 0, 0
archetype = space_industrial02
parent = br_wrw_03

[Object]
nickname = br_wrw_03_DOCK_space_panel01
pos = 0, 0, -1282
rotate = 0, 90, 0
archetype = space_panel
parent = br_wrw_03

[Object]
nickname = br_wrw_03_DOCK_space_panel02
pos = 400, 0, -1282
rotate = 0, 90, 0
archetype = space_panel
parent = br_wrw_03

[Object]
nickname = br_wrw_03_DOCK_shipyard01
pos = -280, -215, -840
rotate = 0, 135, 0
archetype = shipyard
parent = br_wrw_03

[Object]
nickname = br_wrw_03_DOCK_shipyard02
pos = 120, -215, -840
rotate = 0, 135, 0
archetype = shipyard
parent = br_wrw_03

[Object]
nickname = br_wrw_03_DOCK_shipyard03
pos = 520, -215, -840
rotate = 0, 135, 0
archetype = shipyard
parent = br_wrw_03

[Object]
nickname = br_wrw_03_DOCK_space_habitat01
pos = -400, 145, -735
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_wrw_03

[Object]
nickname = br_wrw_03_DOCK_space_habitat02
pos = 0, 145, -735
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_wrw_03

[Object]
nickname = br_wrw_03_DOCK_space_habitat03
pos = 0, 300, -735
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_wrw_03

[Object]
nickname = br_wrw_03_DOCK_space_habitat04
pos = 400, 207, -735
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = br_wrw_03

'''