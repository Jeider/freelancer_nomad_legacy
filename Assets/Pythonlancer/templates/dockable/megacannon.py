from templates.space_object_template import SpaceObjectTemplate


class MegaCannon(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'br_wrw_03'
    TEMPLATE = '''[Object]
nickname = br_wrw_03
pos = -1280, 500, -320
rotate = 0, 0, 0
archetype = gun_core
{root_props}

[Object]
nickname = br_wrw_03_dock
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_shipping01
{dock_props}

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


class HeavyBarrelWithPlanet(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'br_hbr_01'
    TEMPLATE = '''[Object]
nickname = br_hbr_01_planet01
pos = 0.00000, 0.00000, 0.00000
rotate = 0, 0, 0
archetype = br_heavy_barrel_target_planet
atmosphere_range = 4000
loadout = heavy_barrel_pirate_planet

[Object]
nickname = br_hbr_01_planet_gen_counter
pos = 0.00000, -80.00000, 0.00000
rotate = 0, 0, 0
archetype = br_heavy_barrel_gens_progress_counter

[Object]
nickname = br_hbr_01_static_ast_01
pos = -900.00000, 0.00000, -800.00000
rotate = 10, 30, -34
archetype = om15_static_large_ast01

[Object]
nickname = br_hbr_01_static_ast_02
pos = 0.00000, -200.00000, -1700.00000
rotate = -120, 410, 20
archetype = om15_static_large_ast02

[Object]
nickname = br_hbr_01_static_ast_03
pos = 600.00000, 100.00000, -1500.00000
rotate = 0, 0, 0
archetype = om15_static_large_ast03

[Object]
nickname = br_hbr_01_static_ast_04
pos = 200.00000, 50.00000, 0.00000
rotate = 12, -334, -21
archetype = om15_static_large_ast04

[Object]
nickname = br_hbr_01_static_ast_05
pos = -100.00000, 600.00000, -700.00000
rotate = 12, 32 ,32
archetype = om15_static_large_ast03

[Object]
nickname = br_hbr_01_static_ast_06
pos = -50.00000, -150.00000, -750.00000
rotate = 412, 234, 12
archetype = om15_static_large_ast04

[Object]
nickname = br_hbr_01_static_ast_07
pos = 0.00000, -800.00000, -700.00000
rotate = 24, 234 ,234
archetype = om15_static_large_ast01

;[Object]
;nickname = br_hbr_01_reward_container
;pos = -150.00000, 50.00000, -750.00000
;rotate = 0, 0, 30
;archetype = br_heavy_barrel_reward_container

[Object]
nickname = br_hbr_01_planet_damage_01
pos = 400.00000, -150.00000, -750.00000
rotate = 0, 50, 0
archetype = space_industrial_dmg

;[Object]
;nickname = br_hbr_01_reward_target
;pos = -180.00000, 200.00000, -750.00000
;rotate = 0, 0, 0
;archetype = target_arrow

[Object]
nickname = br_hbr_01
ids_name = 203704
pos = 0.00000, -500.00000, -20380.00000
rotate = 0, 0, 0
archetype = gun_core_satellite
ids_info = 065621
base = br_hbr_01_base
reputation = br_p_grp
behavior = NOTHING
difficulty_level = 12

[Object]
nickname = br_hbr_01_dock
ids_name = 196722
pos = 1280.00000, -1000.00000, -20060.00000
rotate = 0, 90, 0
archetype = space_shipping01_satellite
ids_info = 065739
reputation = br_grp
behavior = NOTHING
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_POLYGON01
pos = 0.00000, -85.00000, -20080.00000
archetype = the_barrel
loadout = the_barrel_attacher
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_single_ind01
pos = 0.00000, 180.00000, -20700.00000
rotate = 0, 90, 0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_single_ind02
pos = 235.00000, 40.00000, -20700.00000
rotate = 60, 90, 0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_single_ind03
pos = 235.00000, -230.00000, -20700.00000
rotate = 120, 90, 0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_single_ind04
pos = 0.00000, -365.00000, -20700.00000
rotate = 0, 90, 0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_single_ind05
pos = -235.00000, -230.00000, -20700.00000
rotate = 60, 90, 0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_single_ind06
pos = -235.00000, 40.00000, -20700.00000
rotate = 120, 90, 0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_space_girder01
pos = 0.00000, 85.00000, -20467.00000
rotate = 30, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_space_girder02
pos = 0.00000, -270.00000, -20467.00000
rotate = -30, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_space_girder03
pos = -155.00000, -10.00000, -20467.00000
rotate = 0, -30, 150
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_space_girder04
pos = -155.00000, -185.00000, -20467.00000
rotate = 0, -30, 210
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_space_girder05
pos = 155.00000, -185.00000, -20467.00000
rotate = 0, -30, -30
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_space_girder06
pos = 155.00000, -10.00000, -20467.00000
rotate = 0, -30, 30
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_space_girder05a
pos = -135.00000, -390.00000, -20210.00000
rotate = -65, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_space_girder06a
pos = -135.00000, -400.00000, -20170.00000
rotate = -65, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_space_girder07
pos = 135.00000, -390.00000, -20210.00000
rotate = -65, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_space_girder08
pos = 135.00000, -400.00000, -20170.00000
rotate = -65, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_gen1
ids_name = 068019
pos = 0.00000, 480.00000, -20700.00000
rotate = 90, 90, 0
archetype = br_heavy_barrel_gen_appearance
ids_info = 068055

[Object]
nickname = br_hbr_01_BARREL_RING_gen1_hitbox
pos = 0.00000, 480.00000, 0.00000
rotate = 90, 90, 0
archetype = br_heavy_barrel_gen_hitbox
parent = br_hbr_01_BARREL_RING_gen1

[Object]
nickname = br_hbr_01_BARREL_RING_gen1_fx
pos = 0.00000, 481.00000, 0.00000
rotate = 90, 90, 0
archetype = br_heavy_barrel_gen_active_fx
parent = br_hbr_01_BARREL_RING_gen1

[Object]
nickname = br_hbr_01_BARREL_RING_gen2
ids_name = 068019
pos = 500.00000, 190.00000, -20700.00000
rotate = 60, 90, -90
archetype = br_heavy_barrel_gen_appearance
ids_info = 068055

[Object]
nickname = br_hbr_01_BARREL_RING_gen2_hitbox
pos = 500.00000, 190.00000, 0.00000
rotate = 60, 90, -90
archetype = br_heavy_barrel_gen_hitbox
parent = br_hbr_01_BARREL_RING_gen2

[Object]
nickname = br_hbr_01_BARREL_RING_gen2_fx
pos = 500.00000, 191.00000, 0.00000
rotate = 60, 90, -90
archetype = br_heavy_barrel_gen_active_fx
parent = br_hbr_01_BARREL_RING_gen2

[Object]
nickname = br_hbr_01_BARREL_RING_gen3
ids_name = 068019
pos = 500.00000, -380.00000, -20700.00000
rotate = 120, 90, -90
archetype = br_heavy_barrel_gen_appearance
ids_info = 068055

[Object]
nickname = br_hbr_01_BARREL_RING_gen3_hitbox
pos = 500.00000, -380.00000, 0.00000
rotate = 120, 90, -90
archetype = br_heavy_barrel_gen_hitbox
parent = br_hbr_01_BARREL_RING_gen3

[Object]
nickname = br_hbr_01_BARREL_RING_gen3_fx
pos = 500.00000, -379.00000, 0.00000
rotate = 120, 90, -90
archetype = br_heavy_barrel_gen_active_fx
parent = br_hbr_01_BARREL_RING_gen3

[Object]
nickname = br_hbr_01_BARREL_RING_gen4
ids_name = 068019
pos = 0.00000, -650.00000, -20700.00000
rotate = -90, 90, 0
archetype = br_heavy_barrel_gen_appearance
ids_info = 068055

[Object]
nickname = br_hbr_01_BARREL_RING_gen4_hitbox
pos = 0.00000, -650.00000, 0.00000
rotate = -90, 90, 0
archetype = br_heavy_barrel_gen_hitbox
parent = br_hbr_01_BARREL_RING_gen4

[Object]
nickname = br_hbr_01_BARREL_RING_gen4_fx
pos = 0.00000, -649.00000, 0.00000
rotate = -90, 90, 0
archetype = br_heavy_barrel_gen_active_fx
parent = br_hbr_01_BARREL_RING_gen4

[Object]
nickname = br_hbr_01_BARREL_RING_gen5
ids_name = 068019
pos = -500.00000, -380.00000, -20700.00000
rotate = -120, 90, -90
archetype = br_heavy_barrel_gen_appearance
ids_info = 068055

[Object]
nickname = br_hbr_01_BARREL_RING_gen5_hitbox
pos = -500.00000, -380.00000, 0.00000
rotate = -120, 90, -90
archetype = br_heavy_barrel_gen_hitbox
parent = br_hbr_01_BARREL_RING_gen5

[Object]
nickname = br_hbr_01_BARREL_RING_gen5_fx
pos = -500.00000, -379.00000, 0.00000
rotate = -120, 90, -90
archetype = br_heavy_barrel_gen_active_fx
parent = br_hbr_01_BARREL_RING_gen5

[Object]
nickname = br_hbr_01_BARREL_RING_gen6
ids_name = 068019
pos = -500.00000, 190.00000, -20700.00000
rotate = -60, 90, -90
archetype = br_heavy_barrel_gen_appearance
ids_info = 068055

[Object]
nickname = br_hbr_01_BARREL_RING_gen6_hitbox
pos = -500.00000, 190.00000, 0.00000
rotate = -60, 90, -90
archetype = br_heavy_barrel_gen_hitbox
parent = br_hbr_01_BARREL_RING_gen6

[Object]
nickname = br_hbr_01_BARREL_RING_gen6_fx
pos = -500.00000, 191.00000, 0.00000
rotate = -60, 90, -90
archetype = br_heavy_barrel_gen_active_fx
parent = br_hbr_01_BARREL_RING_gen6

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind01
pos = -135.00000, -650.00000, -20310.00000
rotate = -65, 0, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind02
pos = 135.00000, -650.00000, -20310.00000
rotate = -65, 0, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind03
pos = 0.00000, -860.00000, -20310.00000
rotate = 0, 90, 0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind04
pos = 0.00000, -650.00000, -20455.00000
rotate = 90, 0, 0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind05
pos = 0.00000, -650.00000, -20310.00000
rotate = 90, 0, 0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind06
pos = 0.00000, -860.00000, -20455.00000
rotate = 0, 90, 0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind07
pos = 0.00000, -860.00000, -19890.00000
rotate = 0, 180, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind08
pos = 0.00000, -860.00000, -20875.00000
rotate = 0, 0, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind09
pos = 495.00000, -860.00000, -20382.00000
rotate = 0, -90, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind10
pos = -110.00000, -550.00000, -20550.00000
rotate = -160, 0, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind11
pos = -110.50000, -393.50000, -20980.00000
rotate = 20,0,0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind12
pos = 110.00000, -550.00000, -20550.00000
rotate = -160, 0, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind13
pos = 109.50000, -393.50000, -20980.00000
rotate = 20, 0, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_girder01
pos = 90.00000, -393.50000, -20890.00000
rotate = 0, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_girder02
pos = 90.00000, -370.00000, -20890.00000
rotate = 0, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_girder03
pos = -90.00000, -393.50000, -20890.00000
rotate = 0, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_girder04
pos = -90.00000, -370.00000, -20890.00000
rotate = 0, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind14
pos = 350.00000, -860.00000, -20050.00000
rotate = 0, -135, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind15
pos = 350.00000, -860.00000, -20750.00000
rotate = 0, -45, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind16
pos = -350.00000, -860.00000, -20750.00000
rotate = 0, 45, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind17
pos = -350.00000, -860.00000, -20050.00000
rotate = 0, 135, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind18
pos = -455.00000, -860.00000, -20382.00000
rotate = 0, 90, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_single_ind01
pos = 0.00000, -80.00000, -21350.00000
rotate = 0, 0, 45
archetype = space_industrial01a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_girder01
pos = -50.00000, -80.00000, -21050.00000
rotate = 0, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_girder02
pos = 50.00000, -80.00000, -21050.00000
rotate = 0, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_girder03
pos = 0.00000, -30.00000, -21050.00000
rotate = 0, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_girder04
pos = 0.00000, -130.00000, -21050.00000
rotate = 0, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_girder05
pos = 0.00000, -80.00000, -21270.00000
rotate = 0, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_single_ind02
pos = 102.00000, 25.00000, -21350.00000
rotate = 0, 0, 45
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_single_ind03
pos = -102.00000, 25.00000, -21350.00000
rotate = 0, 0, 45
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_single_ind04
pos = 102.00000, -182.00000, -21350.00000
rotate = 0, 0, -45
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_single_ind05
pos = -102.00000, -182.00000, -21350.00000
rotate = 0, 0, -45
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_girder06
pos = 110.00000, -280.00000, -21140.00000
rotate = -135, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_girder07
pos = 110.00000, -280.00000, -21180.00000
rotate = -135, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_girder08
pos = -110.00000, -280.00000, -21140.00000
rotate = -135, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_girder09
pos = -110.00000, -280.00000, -21180.00000
rotate = -135, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_girder10
pos = -110.50000, -480.00000, -20820.00000
rotate = 20, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_girder11
pos = -110.50000, -440.00000, -20780.00000
rotate = 20, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_girder12
pos = 109.50000, -480.00000, -20820.00000
rotate = 20, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_girder13
pos = 109.50000, -440.00000, -20780.00000
rotate = 20, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_panel01
pos = 220.00000, -80.00000, -21350.00000
rotate = 0, 90, 0
archetype = space_panel
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_panel02
pos = 0.00000, -300.00000, -21350.00000
rotate = 0, 90, 0
archetype = space_panel
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_panel03
pos = -220.00000, -80.00000, -21350.00000
rotate = 0, 90, 0
archetype = space_panel
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_panel04
pos = 0.00000, 140.00000, -21350.00000
rotate = 0, 90,0
archetype = space_panel
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_panel05
pos = 0.00000, -80.00000, -21490.00000
rotate = 0, 90,0
archetype = space_panel
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_ind01
pos = 0.00000, -1000.00000, -19890.00000
rotate = 0, 90,0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_ind02
pos = 350.00000, -1000.00000, -20050.00000
rotate = 0, -45,0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_ind03
pos = 495.00000, -1000.00000, -20382.00000
rotate = 0, 0,0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_ind04
pos = 350.00000, -1000.00000, -20750.00000
rotate = 0, 45,0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_ind05
pos = 0.00000, -1000.00000, -20875.00000
rotate = 0, 90,0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_ind06
pos = -350.00000, -1000.00000, -20750.00000
rotate = 0, -45,0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_ind07
pos = -455.00000, -1000.00000, -20382.00000
rotate = 0, 0,0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_ind08
pos = -350.00000, -1000.00000, -20050.00000
rotate = 0, 45,0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_girder01
pos = 200.00000, -1000.00000, -19970.00000
rotate = 0, 118,0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_girder02
pos = 400.00000, -1000.00000, -20150.00000
rotate = 0, 150,0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_girder03
pos = 400.00000, -1000.00000, -20650.00000
rotate = 0, -155,0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_girder04
pos = 220.00000, -1000.00000, -20820.00000
rotate = 0,-105,0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_girder05
pos = -220.00000, -1000.00000, -20820.00000
rotate = 0, 105,0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_girder06
pos = -450.00000, -1000.00000, -20550.00000
rotate = 0, 165,0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_girder07
pos = -430.00000, -1000.00000, -20250.00000
rotate = 0, -165,0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_girder08
pos = -200.00000, -1000.00000, -19970.00000
rotate = 0, -118,0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_space_ind01
pos = 400.00000, -1000.00000, -21270.00000
rotate = 0, 0,0
archetype = space_industrial02
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_space_ind02
pos = 0.00000, -1000.00000, -21270.00000
rotate = 0, 0,0
archetype = space_industrial02
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_space_ind03
pos = -400.00000, -1000.00000, -21270.00000
rotate = 0, 0,0
archetype = space_industrial02
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_space_ind04
pos = 400.00000, -1000.00000, -21670.00000
rotate = 0, 0,0
archetype = space_industrial02
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_space_ind05
pos = 0.00000, -1000.00000, -21670.00000
rotate = 0, 0,0
archetype = space_industrial02
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_space_ind06
pos = -400.00000, -1000.00000, -21670.00000
rotate = 0, 0,0
archetype = space_industrial02
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_space_ind07
pos = 400.00000, -1000.00000, -22070.00000
rotate = 0, 0,0
archetype = space_industrial02
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_space_ind08
pos = 0.00000, -1000.00000, -22070.00000
rotate = 0, 0,0
archetype = space_industrial02
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_space_ind09
pos = -400.00000, -1000.00000, -22070.00000
rotate = 0, 0,0
archetype = space_industrial02
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_space_ind10
pos = 0.00000, -1420.00000, -21270.00000
rotate = -90, 0, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_space_ind11
pos = 0.00000, -1420.00000, -21670.00000
rotate = -90, 0, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_space_ind12
pos = 0.00000, -1420.00000, -22070.00000
rotate = -90, 0, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind01
pos = 400.00000, -1204.00000, -21270.00000
rotate = -90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind02
pos = 602.00000, -1000.00000, -21270.00000
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind03
pos = 400.00000, -796.00000, -21270.00000
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind04
pos = 0.00000, -796.00000, -21270.00000
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind05
pos = -400.00000, -796.00000, -21270.00000
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind06
pos = -602.00000, -1000.00000, -21270.00000
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind07
pos = -400.00000, -1204.00000, -21270.00000
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind08
pos = 400.00000, -1204.00000, -21670.00000
rotate = -90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind09
pos = 602.00000, -1000.00000, -21670.00000
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind10
pos = 400.00000, -796.00000, -21670.00000
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind11
pos = 0.00000, -796.00000, -21670.00000
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind12
pos = -400.00000, -796.00000, -21670.00000
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind13
pos = -602.00000, -1000.00000, -21670.00000
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind14
pos = -400.00000, -1204.00000, -22070.00000
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind15
pos = 400.00000, -1204.00000, -22070.00000
rotate = -90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind16
pos = 602.00000, -1000.00000, -22070.00000
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind17
pos = 400.00000, -796.00000, -22070.00000
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind18
pos = 0.00000, -796.00000, -22070.00000
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind19
pos = -400.00000, -796.00000, -22070.00000
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind20
pos = -602.00000, -1000.00000, -22070.00000
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind21
pos = -400.00000, -1204.00000, -22070.00000
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_ind01
pos = -400.00000, -1000.00000, -19525.00000
rotate = 0, 180,0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_ind02
pos = 400.00000, -1000.00000, -19525.00000
rotate = 0, 180,0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_ind03
pos = -400.00000, -1000.00000, -18165.00000
rotate = 0, 180,0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_ind04
pos = 400.00000, -1000.00000, -18165.00000
rotate = 0, 180,0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_girder01
pos = -400.00000, -1000.00000, -19210.00000
rotate = 0, 0,0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_girder02
pos = 400.00000, -1000.00000, -19210.00000
rotate = 0, 0,0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_girder03
pos = -400.00000, -1000.00000, -18830.00000
rotate = 0, 0,0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_girder04
pos = 400.00000, -1000.00000, -18830.00000
rotate = 0, 0,0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks01
pos = -270.00000, -1000.00000, -19200.00000
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks02
pos = -5.00000, -1000.00000, -19200.00000
rotate = 0,90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks03
pos = 260.00000, -1000.00000, -19200.00000
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks04
pos = -270.00000, -1000.00000, -19000.00000
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks05
pos = -5.00000, -1000.00000, -19000.00000
rotate = 0,90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks06
pos = 260.00000, -1000.00000, -19000.00000
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks07
pos = -270.00000, -1000.00000, -18800.00000
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks08
pos = -5.00000, -1000.00000, -18800.00000
rotate = 0,90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks09
pos = 260.00000, -1000.00000, -18800.00000
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks10
pos = -270.00000, -1000.00000, -18600.00000
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks11
pos = -5.00000, -1000.00000, -18600.00000
rotate = 0,90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks12
pos = 260.00000, -1000.00000, -18600.00000
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks13
pos = -270.00000, -1000.00000, -18400.00000
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks14
pos = -5.00000, -1000.00000, -18400.00000
rotate = 0,90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks15
pos = 260.00000, -1000.00000, -18400.00000
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_ind01
pos = -880.00000, -1000.00000, -20800.00000
rotate = 0, 90, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_ind02
pos = -880.00000, -1000.00000, -20000.00000
rotate = 0, 90, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_ind03
pos = -880.00000, -1000.00000, -20381.00000
rotate = 0, 90, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_ind04
pos = -1280.00000, -1000.00000, -20800.00000
rotate = 0, 90, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_ind05
pos = -1280.00000, -1000.00000, -20381.00000
rotate = 0, 90, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_ind06
pos = -1680.00000, -1000.00000, -20800.00000
rotate = 0, 90, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_dome01
pos = -1680.00000, -980.00000, -20435.00000
rotate = 0,180, 0
archetype = space_dome
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_dome02
pos = -1280.00000, -980.00000, -20015.00000
rotate = 0, 180, 0
archetype = space_dome
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_dome03
pos = -880.00000, -980.00000, -19635.00000
rotate = 0, 180, 0
archetype = space_dome
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_girder01
pos = -880.00000, -1000.00000, -20600.00000
rotate = 0, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_girder02
pos = -1280.00000, -1000.00000, -20600.00000
rotate = 0, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_girder03
pos = -880.00000, -1000.00000, -20200.00000
rotate = 0, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_hab_wide01
pos = -880.00000, -855.00000, -20800.00000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_hab_wide02
pos = -880.00000, -1142.00000, -20800.00000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_hab_wide03
pos = -880.00000, -855.00000, -20381.00000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_hab_wide04
pos = -880.00000, -700.00000, -20381.00000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_hab_wide05
pos = -880.00000, -1142.00000, -20381.00000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_hab_wide06
pos = -880.00000, -855.00000, -20000.00000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_hab_wide07
pos = -880.00000, -1142.00000, -20000.00000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_hab_wide08
pos = -1280.00000, -855.00000, -20381.00000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_hab_wide09
pos = -1280.00000, -1142.00000, -20381.00000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_hab_wide10
pos = -1680.00000, -1142.00000, -20800.00000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_hab_wide11
pos = -1680.00000, -855.00000, -20800.00000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_hab_wide12
pos = -1280.00000, -1142.00000, -20800.00000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_hab_tall01
pos = -1280.00000, -792.00000, -20800.00000
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_hab_tall02
pos = -880.00000, -637.00000, -20000.00000
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = br_hbr_01

[Object]
nickname = br_hbr_01_DOCK_space_ind01
pos = 880.00000, -1000.00000, -20795.00000
rotate = 0, -90, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_DOCK_space_ind02
pos = 1280.00000, -1000.00000, -20795.00000
rotate = 0, -90, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_DOCK_space_ind03
pos = 1680.00000, -1000.00000, -20795.00000
rotate = 0, -90, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_DOCK_shipyard01
pos = 1000.00000, -1215.00000, -20900.00000
rotate = 0, 135, 0
archetype = shipyard
parent = br_hbr_01

[Object]
nickname = br_hbr_01_DOCK_shipyard02
pos = 1400.00000, -1215.00000, -20900.00000
rotate = 0, 135, 0
archetype = shipyard
parent = br_hbr_01

[Object]
nickname = br_hbr_01_DOCK_shipyard03
pos = 1800.00000, -1215.00000, -20900.00000
rotate = 0, 135, 0
archetype = shipyard
parent = br_hbr_01

[Object]
nickname = br_hbr_01_DOCK_space_habitat01
pos = 880.00000, -855.00000, -20795.00000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_hbr_01

[Object]
nickname = br_hbr_01_DOCK_space_habitat02
pos = 1280.00000, -855.00000, -20795.00000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_hbr_01

[Object]
nickname = br_hbr_01_DOCK_space_habitat04
pos = 1680.00000, -793.00000, -20795.00000
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = br_hbr_01
'''


class HeavyBarrelWithPlanetNotDestroyable(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'br_hbr_01'
    TEMPLATE = '''[Object]
nickname = br_hbr_01_planet01
pos = 0.00000, 0.00000, 0.00000
rotate = 0, 0, 0
archetype = br_heavy_barrel_target_planet
atmosphere_range = 4000
loadout = heavy_barrel_pirate_planet

[Object]
nickname = br_hbr_01
pos = 0.00000, -500.00000, -20380.00000
rotate = 0, 0, 0
archetype = gun_core_satellite
{root_props}

[Object]
nickname = br_hbr_01_dock
ids_name = 196722
pos = 1280.00000, -1000.00000, -20060.00000
rotate = 0, 90, 0
archetype = space_shipping01_satellite
ids_info = 065739
behavior = NOTHING
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_POLYGON01
pos = 0.00000, -85.00000, -20080.00000
archetype = the_barrel
loadout = the_barrel_attacher
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_single_ind01
pos = 0.00000, 180.00000, -20700.00000
rotate = 0, 90, 0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_single_ind02
pos = 235.00000, 40.00000, -20700.00000
rotate = 60, 90, 0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_single_ind03
pos = 235.00000, -230.00000, -20700.00000
rotate = 120, 90, 0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_single_ind04
pos = 0.00000, -365.00000, -20700.00000
rotate = 0, 90, 0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_single_ind05
pos = -235.00000, -230.00000, -20700.00000
rotate = 60, 90, 0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_single_ind06
pos = -235.00000, 40.00000, -20700.00000
rotate = 120, 90, 0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_space_girder01
pos = 0.00000, 85.00000, -20467.00000
rotate = 30, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_space_girder02
pos = 0.00000, -270.00000, -20467.00000
rotate = -30, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_space_girder03
pos = -155.00000, -10.00000, -20467.00000
rotate = 0, -30, 150
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_space_girder04
pos = -155.00000, -185.00000, -20467.00000
rotate = 0, -30, 210
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_space_girder05
pos = 155.00000, -185.00000, -20467.00000
rotate = 0, -30, -30
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_space_girder06
pos = 155.00000, -10.00000, -20467.00000
rotate = 0, -30, 30
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_space_girder05a
pos = -135.00000, -390.00000, -20210.00000
rotate = -65, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_space_girder06a
pos = -135.00000, -400.00000, -20170.00000
rotate = -65, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_space_girder07
pos = 135.00000, -390.00000, -20210.00000
rotate = -65, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_space_girder08
pos = 135.00000, -400.00000, -20170.00000
rotate = -65, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_gen1
ids_name = 068019
pos = 0.00000, 480.00000, -20700.00000
rotate = 90, 90, 0
archetype = br_heavy_barrel_gen_appearance
ids_info = 068055
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_gen2
ids_name = 068019
pos = 500.00000, 190.00000, -20700.00000
rotate = 60, 90, -90
archetype = br_heavy_barrel_gen_appearance
ids_info = 068055
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_gen3
ids_name = 068019
pos = 500.00000, -380.00000, -20700.00000
rotate = 120, 90, -90
archetype = br_heavy_barrel_gen_appearance
ids_info = 068055
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_gen4
ids_name = 068019
pos = 0.00000, -650.00000, -20700.00000
rotate = -90, 90, 0
archetype = br_heavy_barrel_gen_appearance
ids_info = 068055
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_gen5
ids_name = 068019
pos = -500.00000, -380.00000, -20700.00000
rotate = -120, 90, -90
archetype = br_heavy_barrel_gen_appearance
ids_info = 068055
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_RING_gen6
ids_name = 068019
pos = -500.00000, 190.00000, -20700.00000
rotate = -60, 90, -90
archetype = br_heavy_barrel_gen_appearance
ids_info = 068055
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind01
pos = -135.00000, -650.00000, -20310.00000
rotate = -65, 0, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind02
pos = 135.00000, -650.00000, -20310.00000
rotate = -65, 0, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind03
pos = 0.00000, -860.00000, -20310.00000
rotate = 0, 90, 0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind04
pos = 0.00000, -650.00000, -20455.00000
rotate = 90, 0, 0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind05
pos = 0.00000, -650.00000, -20310.00000
rotate = 90, 0, 0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind06
pos = 0.00000, -860.00000, -20455.00000
rotate = 0, 90, 0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind07
pos = 0.00000, -860.00000, -19890.00000
rotate = 0, 180, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind08
pos = 0.00000, -860.00000, -20875.00000
rotate = 0, 0, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind09
pos = 495.00000, -860.00000, -20382.00000
rotate = 0, -90, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind10
pos = -110.00000, -550.00000, -20550.00000
rotate = -160, 0, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind11
pos = -110.50000, -393.50000, -20980.00000
rotate = 20,0,0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind12
pos = 110.00000, -550.00000, -20550.00000
rotate = -160, 0, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind13
pos = 109.50000, -393.50000, -20980.00000
rotate = 20, 0, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_girder01
pos = 90.00000, -393.50000, -20890.00000
rotate = 0, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_girder02
pos = 90.00000, -370.00000, -20890.00000
rotate = 0, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_girder03
pos = -90.00000, -393.50000, -20890.00000
rotate = 0, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_girder04
pos = -90.00000, -370.00000, -20890.00000
rotate = 0, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind14
pos = 350.00000, -860.00000, -20050.00000
rotate = 0, -135, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind15
pos = 350.00000, -860.00000, -20750.00000
rotate = 0, -45, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind16
pos = -350.00000, -860.00000, -20750.00000
rotate = 0, 45, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind17
pos = -350.00000, -860.00000, -20050.00000
rotate = 0, 135, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_BARREL_CONNECT_space_ind18
pos = -455.00000, -860.00000, -20382.00000
rotate = 0, 90, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_single_ind01
pos = 0.00000, -80.00000, -21350.00000
rotate = 0, 0, 45
archetype = space_industrial01a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_girder01
pos = -50.00000, -80.00000, -21050.00000
rotate = 0, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_girder02
pos = 50.00000, -80.00000, -21050.00000
rotate = 0, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_girder03
pos = 0.00000, -30.00000, -21050.00000
rotate = 0, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_girder04
pos = 0.00000, -130.00000, -21050.00000
rotate = 0, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_girder05
pos = 0.00000, -80.00000, -21270.00000
rotate = 0, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_single_ind02
pos = 102.00000, 25.00000, -21350.00000
rotate = 0, 0, 45
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_single_ind03
pos = -102.00000, 25.00000, -21350.00000
rotate = 0, 0, 45
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_single_ind04
pos = 102.00000, -182.00000, -21350.00000
rotate = 0, 0, -45
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_single_ind05
pos = -102.00000, -182.00000, -21350.00000
rotate = 0, 0, -45
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_girder06
pos = 110.00000, -280.00000, -21140.00000
rotate = -135, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_girder07
pos = 110.00000, -280.00000, -21180.00000
rotate = -135, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_girder08
pos = -110.00000, -280.00000, -21140.00000
rotate = -135, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_girder09
pos = -110.00000, -280.00000, -21180.00000
rotate = -135, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_girder10
pos = -110.50000, -480.00000, -20820.00000
rotate = 20, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_girder11
pos = -110.50000, -440.00000, -20780.00000
rotate = 20, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_girder12
pos = 109.50000, -480.00000, -20820.00000
rotate = 20, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_girder13
pos = 109.50000, -440.00000, -20780.00000
rotate = 20, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_panel01
pos = 220.00000, -80.00000, -21350.00000
rotate = 0, 90, 0
archetype = space_panel
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_panel02
pos = 0.00000, -300.00000, -21350.00000
rotate = 0, 90, 0
archetype = space_panel
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_panel03
pos = -220.00000, -80.00000, -21350.00000
rotate = 0, 90, 0
archetype = space_panel
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_panel04
pos = 0.00000, 140.00000, -21350.00000
rotate = 0, 90,0
archetype = space_panel
parent = br_hbr_01

[Object]
nickname = br_hbr_01_GUN_space_panel05
pos = 0.00000, -80.00000, -21490.00000
rotate = 0, 90,0
archetype = space_panel
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_ind01
pos = 0.00000, -1000.00000, -19890.00000
rotate = 0, 90,0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_ind02
pos = 350.00000, -1000.00000, -20050.00000
rotate = 0, -45,0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_ind03
pos = 495.00000, -1000.00000, -20382.00000
rotate = 0, 0,0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_ind04
pos = 350.00000, -1000.00000, -20750.00000
rotate = 0, 45,0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_ind05
pos = 0.00000, -1000.00000, -20875.00000
rotate = 0, 90,0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_ind06
pos = -350.00000, -1000.00000, -20750.00000
rotate = 0, -45,0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_ind07
pos = -455.00000, -1000.00000, -20382.00000
rotate = 0, 0,0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_ind08
pos = -350.00000, -1000.00000, -20050.00000
rotate = 0, 45,0
archetype = space_industrial02a
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_girder01
pos = 200.00000, -1000.00000, -19970.00000
rotate = 0, 118,0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_girder02
pos = 400.00000, -1000.00000, -20150.00000
rotate = 0, 150,0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_girder03
pos = 400.00000, -1000.00000, -20650.00000
rotate = 0, -155,0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_girder04
pos = 220.00000, -1000.00000, -20820.00000
rotate = 0,-105,0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_girder05
pos = -220.00000, -1000.00000, -20820.00000
rotate = 0, 105,0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_girder06
pos = -450.00000, -1000.00000, -20550.00000
rotate = 0, 165,0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_girder07
pos = -430.00000, -1000.00000, -20250.00000
rotate = 0, -165,0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_PLACE_space_girder08
pos = -200.00000, -1000.00000, -19970.00000
rotate = 0, -118,0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_space_ind01
pos = 400.00000, -1000.00000, -21270.00000
rotate = 0, 0,0
archetype = space_industrial02
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_space_ind02
pos = 0.00000, -1000.00000, -21270.00000
rotate = 0, 0,0
archetype = space_industrial02
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_space_ind03
pos = -400.00000, -1000.00000, -21270.00000
rotate = 0, 0,0
archetype = space_industrial02
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_space_ind04
pos = 400.00000, -1000.00000, -21670.00000
rotate = 0, 0,0
archetype = space_industrial02
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_space_ind05
pos = 0.00000, -1000.00000, -21670.00000
rotate = 0, 0,0
archetype = space_industrial02
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_space_ind06
pos = -400.00000, -1000.00000, -21670.00000
rotate = 0, 0,0
archetype = space_industrial02
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_space_ind07
pos = 400.00000, -1000.00000, -22070.00000
rotate = 0, 0,0
archetype = space_industrial02
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_space_ind08
pos = 0.00000, -1000.00000, -22070.00000
rotate = 0, 0,0
archetype = space_industrial02
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_space_ind09
pos = -400.00000, -1000.00000, -22070.00000
rotate = 0, 0,0
archetype = space_industrial02
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_space_ind10
pos = 0.00000, -1420.00000, -21270.00000
rotate = -90, 0, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_space_ind11
pos = 0.00000, -1420.00000, -21670.00000
rotate = -90, 0, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_space_ind12
pos = 0.00000, -1420.00000, -22070.00000
rotate = -90, 0, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind01
pos = 400.00000, -1204.00000, -21270.00000
rotate = -90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind02
pos = 602.00000, -1000.00000, -21270.00000
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind03
pos = 400.00000, -796.00000, -21270.00000
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind04
pos = 0.00000, -796.00000, -21270.00000
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind05
pos = -400.00000, -796.00000, -21270.00000
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind06
pos = -602.00000, -1000.00000, -21270.00000
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind07
pos = -400.00000, -1204.00000, -21270.00000
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind08
pos = 400.00000, -1204.00000, -21670.00000
rotate = -90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind09
pos = 602.00000, -1000.00000, -21670.00000
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind10
pos = 400.00000, -796.00000, -21670.00000
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind11
pos = 0.00000, -796.00000, -21670.00000
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind12
pos = -400.00000, -796.00000, -21670.00000
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind13
pos = -602.00000, -1000.00000, -21670.00000
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind14
pos = -400.00000, -1204.00000, -22070.00000
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind15
pos = 400.00000, -1204.00000, -22070.00000
rotate = -90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind16
pos = 602.00000, -1000.00000, -22070.00000
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind17
pos = 400.00000, -796.00000, -22070.00000
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind18
pos = 0.00000, -796.00000, -22070.00000
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind19
pos = -400.00000, -796.00000, -22070.00000
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind20
pos = -602.00000, -1000.00000, -22070.00000
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_REACTOR_single_ind21
pos = -400.00000, -1204.00000, -22070.00000
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_ind01
pos = -400.00000, -1000.00000, -19525.00000
rotate = 0, 180,0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_ind02
pos = 400.00000, -1000.00000, -19525.00000
rotate = 0, 180,0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_ind03
pos = -400.00000, -1000.00000, -18165.00000
rotate = 0, 180,0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_ind04
pos = 400.00000, -1000.00000, -18165.00000
rotate = 0, 180,0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_girder01
pos = -400.00000, -1000.00000, -19210.00000
rotate = 0, 0,0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_girder02
pos = 400.00000, -1000.00000, -19210.00000
rotate = 0, 0,0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_girder03
pos = -400.00000, -1000.00000, -18830.00000
rotate = 0, 0,0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_girder04
pos = 400.00000, -1000.00000, -18830.00000
rotate = 0, 0,0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks01
pos = -270.00000, -1000.00000, -19200.00000
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks02
pos = -5.00000, -1000.00000, -19200.00000
rotate = 0,90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks03
pos = 260.00000, -1000.00000, -19200.00000
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks04
pos = -270.00000, -1000.00000, -19000.00000
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks05
pos = -5.00000, -1000.00000, -19000.00000
rotate = 0,90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks06
pos = 260.00000, -1000.00000, -19000.00000
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks07
pos = -270.00000, -1000.00000, -18800.00000
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks08
pos = -5.00000, -1000.00000, -18800.00000
rotate = 0,90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks09
pos = 260.00000, -1000.00000, -18800.00000
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks10
pos = -270.00000, -1000.00000, -18600.00000
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks11
pos = -5.00000, -1000.00000, -18600.00000
rotate = 0,90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks12
pos = 260.00000, -1000.00000, -18600.00000
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks13
pos = -270.00000, -1000.00000, -18400.00000
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks14
pos = -5.00000, -1000.00000, -18400.00000
rotate = 0,90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_STORAGE_space_tanks15
pos = 260.00000, -1000.00000, -18400.00000
rotate = 0, 90,0
archetype = space_tankl4x4
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_ind01
pos = -880.00000, -1000.00000, -20800.00000
rotate = 0, 90, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_ind02
pos = -880.00000, -1000.00000, -20000.00000
rotate = 0, 90, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_ind03
pos = -880.00000, -1000.00000, -20381.00000
rotate = 0, 90, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_ind04
pos = -1280.00000, -1000.00000, -20800.00000
rotate = 0, 90, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_ind05
pos = -1280.00000, -1000.00000, -20381.00000
rotate = 0, 90, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_ind06
pos = -1680.00000, -1000.00000, -20800.00000
rotate = 0, 90, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_dome01
pos = -1680.00000, -980.00000, -20435.00000
rotate = 0,180, 0
archetype = space_dome
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_dome02
pos = -1280.00000, -980.00000, -20015.00000
rotate = 0, 180, 0
archetype = space_dome
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_dome03
pos = -880.00000, -980.00000, -19635.00000
rotate = 0, 180, 0
archetype = space_dome
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_girder01
pos = -880.00000, -1000.00000, -20600.00000
rotate = 0, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_girder02
pos = -1280.00000, -1000.00000, -20600.00000
rotate = 0, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_girder03
pos = -880.00000, -1000.00000, -20200.00000
rotate = 0, 0, 0
archetype = space_girder_lowdetail
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_hab_wide01
pos = -880.00000, -855.00000, -20800.00000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_hab_wide02
pos = -880.00000, -1142.00000, -20800.00000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_hab_wide03
pos = -880.00000, -855.00000, -20381.00000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_hab_wide04
pos = -880.00000, -700.00000, -20381.00000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_hab_wide05
pos = -880.00000, -1142.00000, -20381.00000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_hab_wide06
pos = -880.00000, -855.00000, -20000.00000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_hab_wide07
pos = -880.00000, -1142.00000, -20000.00000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_hab_wide08
pos = -1280.00000, -855.00000, -20381.00000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_hab_wide09
pos = -1280.00000, -1142.00000, -20381.00000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_hab_wide10
pos = -1680.00000, -1142.00000, -20800.00000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_hab_wide11
pos = -1680.00000, -855.00000, -20800.00000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_hab_wide12
pos = -1280.00000, -1142.00000, -20800.00000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_hab_tall01
pos = -1280.00000, -792.00000, -20800.00000
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = br_hbr_01

[Object]
nickname = br_hbr_01_CITY_space_hab_tall02
pos = -880.00000, -637.00000, -20000.00000
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = br_hbr_01

[Object]
nickname = br_hbr_01_DOCK_space_ind01
pos = 880.00000, -1000.00000, -20795.00000
rotate = 0, -90, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_DOCK_space_ind02
pos = 1280.00000, -1000.00000, -20795.00000
rotate = 0, -90, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_DOCK_space_ind03
pos = 1680.00000, -1000.00000, -20795.00000
rotate = 0, -90, 0
archetype = space_industrial
parent = br_hbr_01

[Object]
nickname = br_hbr_01_DOCK_shipyard01
pos = 1000.00000, -1215.00000, -20900.00000
rotate = 0, 135, 0
archetype = shipyard
parent = br_hbr_01

[Object]
nickname = br_hbr_01_DOCK_shipyard02
pos = 1400.00000, -1215.00000, -20900.00000
rotate = 0, 135, 0
archetype = shipyard
parent = br_hbr_01

[Object]
nickname = br_hbr_01_DOCK_shipyard03
pos = 1800.00000, -1215.00000, -20900.00000
rotate = 0, 135, 0
archetype = shipyard
parent = br_hbr_01

[Object]
nickname = br_hbr_01_DOCK_space_habitat01
pos = 880.00000, -855.00000, -20795.00000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_hbr_01

[Object]
nickname = br_hbr_01_DOCK_space_habitat02
pos = 1280.00000, -855.00000, -20795.00000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_hbr_01

[Object]
nickname = br_hbr_01_DOCK_space_habitat04
pos = 1680.00000, -793.00000, -20795.00000
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = br_hbr_01
'''
