from templates.template import Template

class ShiparchTemplate(Template):
    TEMPLATE = '''
[Simple]
nickname = generic_pilot
DA_archetype = equipment\\models\\pilot\\ship_pilot_trent.3db
material_library = Equipment\\models\\pilots.mat
LODranges = 0, 250
MinSpecLOD = 2

[Ship]
ship_class = 4
{ship_li_fighter}
LODranges = 0, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_Liblf
mission_property = can_use_berths
type = FIGHTER
linear_drag = 1.000000
max_bank_angle = 5 ;35
camera_offset = 6, 22
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 23
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 30
camera_turn_look_ahead_slerp_amount = 1.000000
DA_archetype = ships\\liberty\\li_fighter\\li_fighter.cmp
material_library = ships\\liberty\\li_playerships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
cockpit = cockpits\\liberty\\l_fighter.ini
pilot_mesh = generic_pilot
explosion_arch = explosion_li
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 300, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 600, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 24000.000000, 24000.000000, 58000.000000
angular_drag = 15000.000000, 15000.000000, 35000.000000
rotation_inertia = 2800.000000, 2800.000000, 1000.000000
nudge_force = 60000.000000
bay_door_anim = Sc_open baydoor
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
num_exhaust_nozzles = 1
HP_tractor_source = HpTractor_Source

[CollisionGroup]
obj = port fin_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
dmg_hp = DpPortfin
dmg_obj = li_fighter_dmg_portfin_cap
mass = 5.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
type = Port_Fin
hit_pts = {lf_fin_hit_pts}
root_health_proxy = false
explosion_resistance = {lf_fin_expl_resist}

[CollisionGroup]
obj = star fin_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpStarboardfin
dmg_obj = li_fighter_dmg_starboardfin_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Fin
hit_pts = {lf_fin_hit_pts}
root_health_proxy = false
explosion_resistance = {lf_fin_expl_resist}

[CollisionGroup] 
obj = Engine_lod1 
separable = true 
parent_impulse = 250.000000 
child_impulse = 7.000000 
debris_type = debris_small_ship 
dmg_hp = DpEngine 
dmg_obj = li_fighter_dmg_engine_cap
separation_explosion = explosion_small_ship_breakoff 
mass = 5.000000 
type = Engine 
hit_pts = {lf_engine_hit_pts}
root_health_proxy = false 
explosion_resistance = {lf_engine_expl_resist}

[Simple]
nickname = li_fighter_dmg_portfin_cap
DA_archetype = ships\\liberty\\li_fighter\\li_fighter_dmg_portfin.3db
material_library = ships\\liberty\\li_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2000

[Simple]
nickname = li_fighter_dmg_starboardfin_cap
DA_archetype = ships\\liberty\\li_fighter\\li_fighter_dmg_starboardfin.3db
material_library = ships\\liberty\\li_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2000

[Simple]
nickname = li_fighter_dmg_engine_cap
DA_archetype = ships\\liberty\\li_fighter\\li_fighter_dmg_engine.3db
material_library = ships\\liberty\\li_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2000

[Ship]
ship_class = 5
{ship_li_elite}
msg_id_prefix = gcs_refer_shiparch_Libhf
mission_property = can_use_berths ;can_use_med_moors ;
LODranges = 0, 1000, 5000, 10000
type = FIGHTER
DA_archetype = ships\\liberty\\li_elite\\li_elite.cmp
; DA_archetype = ships\\liberty\\li_elite\\lx_elite.cmp
material_library = ships\\liberty\\li_playerships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
cockpit = cockpits\\liberty\\l_elite.ini
pilot_mesh = generic_pilot
linear_drag = 1.000000
max_bank_angle = 2 ;30
camera_offset = 8, 34
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 17
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 25
camera_turn_look_ahead_slerp_amount = 1.000000
explosion_arch = explosion_li
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 300, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 500, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 50000.000000, 50000.000000, 230000.000000
angular_drag = 40000.000000, 40000.000000, 141000.000000
rotation_inertia = 8400.000000, 8400.000000, 8400.000000
nudge_force = 60000.000000
bay_door_anim = Sc_open baydoor
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2

[CollisionGroup]
obj = Li_star_wing_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpStarboardwing
dmg_obj = li_elite_dmg_star_wing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Wing
hit_pts = {le_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {le_wing_expl_resist}

[CollisionGroup]
obj = Li_port_wing_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpPortwing
dmg_obj = li_elite_dmg_port_wing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Wing
hit_pts = {le_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {le_wing_expl_resist}

[CollisionGroup]
obj = li_Spoiler_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpSpoiler
dmg_obj = li_elite_dmg_Spoiler_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Spoiler
hit_pts = {le_spoiler_hit_pts}
root_health_proxy = false
explosion_resistance = {le_spoiler_expl_resist}

[CollisionGroup] 
obj = li_Engine01_lod1 
separable = true 
parent_impulse = 250.000000 
child_impulse = 7.000000 
debris_type = debris_small_ship 
dmg_hp = DpEngine01 
dmg_obj = li_elite_dmg_Engine01_cap 
separation_explosion = explosion_small_ship_breakoff 
mass = 5.000000 
type = Top_Engine 
hit_pts = {le_engine1_hit_pts}
root_health_proxy = false 
explosion_resistance = {le_engine1_expl_resist}

[CollisionGroup] 
obj = li_Engine02_lod1 
separable = true 
parent_impulse = 250.000000 
child_impulse = 7.000000 
debris_type = debris_small_ship 
dmg_hp = DpEngine02 
dmg_obj = li_elite_dmg_Engine02_cap 
separation_explosion = explosion_small_ship_breakoff 
mass = 5.000000 
type = Bottom_Engine 
hit_pts = {le_engine2_hit_pts}
root_health_proxy = false
explosion_resistance = {le_engine2_expl_resist}

[Simple]
nickname = li_elite_dmg_star_wing_cap
DA_archetype = ships\\liberty\\li_elite\\li_elite_dmg_starboardwing.3db
material_library = ships\\liberty\\li_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2000

[Simple]
nickname = li_elite_dmg_port_wing_cap
DA_archetype = ships\\liberty\\li_elite\\li_elite_dmg_portwing.3db
material_library = ships\\liberty\\li_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2000

[Simple]
nickname = li_elite_dmg_Spoiler_cap
DA_archetype = ships\\liberty\\li_elite\\li_elite_dmg_spoiler.3db
material_library = ships\\liberty\\li_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2000

[Simple]
nickname = li_elite2_dmg_Spoiler_cap
DA_archetype = ships\\liberty\\li_elite2\\li_elite2_dmg_spoiler.3db
material_library = ships\\liberty\\li_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2000

[Simple]
nickname = li_elite_dmg_Engine01_cap
DA_archetype = ships\\liberty\\li_elite\\li_elite_dmg_engine01.3db
material_library = ships\\liberty\\li_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2000

[Simple]
nickname = li_elite_dmg_Engine02_cap
DA_archetype = ships\\liberty\\li_elite\\li_elite_dmg_engine02.3db
material_library = ships\\liberty\\li_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2000

[Ship]
ship_class = 6
{ship_li_elite2}
msg_id_prefix = gcs_refer_shiparch_Libhf
mission_property = can_use_berths
LODranges = 0, 1000, 5000, 10000
type = FIGHTER
;DA_archetype = ships\\liberty\\li_elite2\\li_elite2.cmp
DA_archetype = ships\\liberty\\li_elite2\\juni_elite.cmp
material_library = ships\\liberty\\li_playerships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
cockpit = cockpits\\liberty\\l_elite.ini
pilot_mesh = generic_pilot
linear_drag = 1
max_bank_angle = 2 ;30
camera_offset = 9.5, 29
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 10
camera_vertical_turn_down_angle = 20
camera_turn_look_ahead_slerp_amount = 1.000000
explosion_arch = explosion_li
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 50000.000000, 50000.000000, 183000.000000
angular_drag = 40000.000000, 40000.000000, 141000.000000
rotation_inertia = 8400.000000, 8400.000000, 8400.000000
nudge_force = 10000.000000
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2

[CollisionGroup]
obj = Li_star_wing_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpStarboardwing
dmg_obj = li_elite_dmg_star_wing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Wing
hit_pts = {le2_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {le2_wing_expl_resist}

[CollisionGroup]
obj = Li_port_wing_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpPortwing
dmg_obj = li_elite_dmg_port_wing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Wing
hit_pts = {le2_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {le2_wing_expl_resist}

[CollisionGroup]
obj = li_Spoiler_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpSpoiler
dmg_obj = li_elite2_dmg_Spoiler_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Top_Fin
hit_pts = {le2_spoiler_hit_pts}
root_health_proxy = false
explosion_resistance = {le2_spoiler_expl_resist}

[CollisionGroup] 
obj = li_Engine01_lod1 
separable = true 
parent_impulse = 250.000000 
child_impulse = 7.000000 
debris_type = debris_small_ship 
dmg_hp = DpEngine01 
dmg_obj = li_elite_dmg_Engine01_cap 
separation_explosion = explosion_small_ship_breakoff 
mass = 5.000000 
type = Engine 
hit_pts = {le2_engine1_hit_pts}
root_health_proxy = false 
explosion_resistance = {le2_engine1_expl_resist}

[CollisionGroup] 
obj = li_Engine02_lod1 
separable = true 
parent_impulse = 250.000000 
child_impulse = 7.000000 
debris_type = debris_small_ship 
dmg_hp = DpEngine02 
dmg_obj = li_elite_dmg_Engine02_cap 
separation_explosion = explosion_small_ship_breakoff 
mass = 5.000000 
type = Engine 
hit_pts = {le2_engine2_hit_pts}
root_health_proxy = false
explosion_resistance = {le2_engine2_expl_resist}

[Ship]
ship_class = 8
{ship_li_freighter}
LODranges = 0, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_Libf
mission_property = can_use_berths
type = FREIGHTER
DA_archetype = ships\\liberty\\li_freighter\\li_freighter.cmp
material_library = ships\\liberty\\li_playerships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
cockpit = cockpits\\liberty\\l_freighter.ini
pilot_mesh = generic_pilot
linear_drag = 1.000000
max_bank_angle = 1 ;15
camera_offset = 8, 45
camera_angular_acceleration = 0.035000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 20
camera_turn_look_ahead_slerp_amount = 1.000000
explosion_arch = explosion_li
nudge_force = 30000.000000
bay_door_anim = Sc_open baydoor
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2
steering_torque = 54000.000000, 54000.000000, 104000.000000
angular_drag = 60000.000000, 60000.000000, 60000.000000
rotation_inertia = 16800.000000, 16800.000000, 16800.000000


[CollisionGroup]
obj = li_starboard_sidepanel_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpStarboardsidepanel
dmg_obj = li_freighter_dmg_starboard_sidepanel_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Side_Panel
hit_pts = {lfr_panel_expl_resist}
root_health_proxy = false
explosion_resistance = {lfr_panel_expl_resist}

[CollisionGroup]
obj = li_port_sidepanel_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpPortsidepanel
dmg_obj = li_freighter_dmg_port_sidepanel_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Side_Panel
hit_pts = {lfr_panel_hit_pts}
root_health_proxy = false
explosion_resistance = {lfr_panel_expl_resist}

[CollisionGroup] 
obj = Engine01_lod1 
separable = true 
parent_impulse = 250.000000 
child_impulse = 7.000000 
debris_type = debris_small_ship 
dmg_hp = DpEngine01 
dmg_obj = li_fr_dmg_Engine01_cap
separation_explosion = explosion_small_ship_breakoff 
mass = 5.000000 
type = Engine 
hit_pts = {lfr_engine_hit_pts}
root_health_proxy = false 
explosion_resistance = {lfr_engine_expl_resist}

[CollisionGroup] 
obj = Engine02_lod1 
separable = true 
parent_impulse = 250.000000 
child_impulse = 7.000000 
debris_type = debris_small_ship 
dmg_hp = DpEngine02 
dmg_obj = li_fr_dmg_Engine02_cap
separation_explosion = explosion_small_ship_breakoff 
mass = 5.000000 
type = Engine 
hit_pts = {lfr_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {lfr_engine_expl_resist}

[Simple]
nickname = li_freighter_dmg_starboard_sidepanel_cap
DA_archetype = ships\\liberty\\li_freighter\\li_freighter_dmg_starboard_sidepanel.3db
material_library = ships\\liberty\\li_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2200

[Simple]
nickname = li_freighter_dmg_port_sidepanel_cap
DA_archetype = ships\\liberty\\li_freighter\\li_freighter_dmg_port_sidepanel.3db
material_library = ships\\liberty\\li_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2200

[Simple]
nickname = li_fr_dmg_Engine01_cap
DA_archetype = ships\\liberty\\li_freighter\\li_freighter_dmg_engine01.3db
material_library = ships\\liberty\\li_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2300

[Simple]
nickname = li_fr_dmg_Engine02_cap
DA_archetype = ships\\liberty\\li_freighter\\li_freighter_dmg_engine02.3db
material_library = ships\\liberty\\li_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2300

[Ship]
ids_name = 237031
ids_info = 66565
nickname = li_cruiser
ship_class = 14
LODranges = 0, 1000, 5000, 15000, 25000
msg_id_prefix = gcs_refer_shiparch_Libc
mission_property = can_use_med_moors
type = CRUISER
DA_archetype = ships\\liberty\\li_cruiser\\li_cruiser.cmp
material_library = ships\\liberty\\li_capships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
linear_drag = 1.000000
mass = 5000.000000
hold_size = 5
hit_pts = 500000
explosion_arch = explosion_li_cruiser
fuse = li_cruiser_body_fuse, 0.000000, 1
fuse = li_cruiser_burning_fuse01, 0.000000, 100000
fuse = li_cruiser_burning_fuse02, 0.000000, 50000
steering_torque = 20000000.000000, 20000000.000000, 20000000.000000
angular_drag = 132000000.000000, 132000000.000000, 132000000.000000
rotation_inertia = 40000000.000000, 40000000.000000, 40000000.000000
;surface_hit_effects = 1, gf_big_hit01
nudge_force = 300000.000000
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 4
camera_offset = 30, 125
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 10
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 5
camera_turn_look_ahead_slerp_amount = 1.000000
cockpit = cockpits\\liberty\\li_cruiser.ini
nanobot_limit = 0 ; = 0 
shield_battery_limit = 0 ; = 0
hp_type = hp_turret_special_1, HpTurret_L5_01, HpTurret_L5_02, HpTurret_L5_03, HpTurret_L5_04, HpTurret_L5_05, HpTurret_L5_06, HpTurret_L5_07
hp_type = hp_turret_special_10, HpWeapon02

[CollisionGroup]
obj = Li_cruiser_cntrltwr_lod1
separable = true
debris_type = debris_vanish
separation_explosion = explosion_li
fuse = lcr_tower_fuse, 0.500000, 1
dmg_obj = l_cruiser_tower_cap
dmg_hp = DpCntrltwr
mass = 100.000000
parent_impulse = 10.000000
child_impulse = 10.000000
hit_pts = 500000
root_health_proxy = false

[CollisionGroup]
obj = Li_cruiser_nose_lod1
separable = true
debris_type = cap_ship_piece
fuse = li_cruiser_body_fuse, 0.000000, 1
parent_impulse = 10.000000
child_impulse = 60.000000
group_dmg_hp = DpFront
group_dmg_obj = l_cruiser_front_cap
mass = 10.000000
hit_pts = 5000000
root_health_proxy = true

[CollisionGroup]
obj = Li_cruiser_engine01_lod1
separable = true
debris_type = cap_ship_piece
;fuse = li_cruiser_engine1_fuse, 0.000000, 1
fuse = lcr_eng01_fuse, 0.500000, 1
separation_explosion = explosion_li
dmg_obj = l_cruiser_engine01_cap
dmg_hp = DpEngine01
group_dmg_hp = DpEng01
group_dmg_obj = l_cruiser_engine01_cap
mass = 100.000000
parent_impulse = 10.000000
child_impulse = 1000.000000
hit_pts = 400000
root_health_proxy = false

[CollisionGroup]
obj = Li_cruiser_engine02_lod1
separable = true
debris_type = cap_ship_piece
;fuse = li_cruiser_engine2_fuse, 0.000000, 1
fuse = lcr_eng02_fuse, 0.500000, 1
dmg_obj = l_cruiser_engine02_cap
dmg_hp = DpEngine02
mass = 100.000000
parent_impulse = 10.000000
child_impulse = 3000.000000
hit_pts = 400000
root_health_proxy = false

[CollisionGroup]
obj = Li_cruiser_engine03_lod1
separable = true
debris_type = cap_ship_piece
;fuse = li_cruiser_engine3_fuse, 0.000000, 1
fuse = lcr_eng03_fuse, 0.500000, 1
dmg_obj = l_cruiser_engine03_cap
dmg_hp = DpEngine03
mass = 100.000000
parent_impulse = 10.000000
child_impulse = 9000.000000
hit_pts = 400000
root_health_proxy = false

[CollisionGroup]
obj = Li_cruiser_engine04_lod1
separable = true
debris_type = cap_ship_piece
;fuse = li_cruiser_engine4_fuse, 0.000000, 1
fuse = lcr_eng04_fuse, 0.500000, 1
dmg_obj = l_cruiser_engine04_cap
dmg_hp = DpEngine04
mass = 100.000000
parent_impulse = 10.000000
child_impulse = 5000.000000
hit_pts = 400000
root_health_proxy = false

[Simple]
nickname = l_cruiser_tower_cap
DA_archetype = Ships\\liberty\\li_cruiser\\li_dmg_cruiser_cntrltwr.3db
material_library = ships\\liberty\\li_capships.mat
mass = 1000.000000
hit_pts = 200
LODranges = 0, 6000

[Simple]
nickname = l_cruiser_front_cap
DA_archetype = Ships\\liberty\\li_cruiser\\li_dmg_cruiser_front.3db
material_library = ships\\liberty\\li_capships.mat
mass = 10.000000
hit_pts = 200
LODranges = 0, 600, 6000

[Simple]
nickname = l_cruiser_engine01_cap
DA_archetype = Ships\\liberty\\li_cruiser\\li_dmg_cruiser_engine01.3db
material_library = ships\\liberty\\li_capships.mat
mass = 1000.000000
hit_pts = 200
LODranges = 0, 6000

[Simple]
nickname = l_cruiser_engine02_cap
DA_archetype = Ships\\liberty\\li_cruiser\\li_dmg_cruiser_engine02.3db
material_library = ships\\liberty\\li_capships.mat
mass = 1000.000000
hit_pts = 200
LODranges = 0, 6000

[Simple]
nickname = l_cruiser_engine03_cap
DA_archetype = Ships\\liberty\\li_cruiser\\li_dmg_cruiser_engine03.3db
material_library = ships\\liberty\\li_capships.mat
mass = 1000.000000
hit_pts = 200
LODranges = 0, 6000

[Simple]
nickname = l_cruiser_engine04_cap
DA_archetype = Ships\\liberty\\li_cruiser\\li_dmg_cruiser_engine04.3db
material_library = ships\\liberty\\li_capships.mat
mass = 1000.000000
hit_pts = 200
LODranges = 0, 6000

[Ship]
ids_name = 237032
ids_info = 66566
ship_class = 16
nickname = li_dreadnought
LODranges = 0, 1000, 4000, 10000, 20000, 40000, 100000
msg_id_prefix = gcs_refer_shiparch_Libb
mission_property = can_use_large_moors
type = CAPITAL
DA_archetype = ships\\liberty\\li_dreadnought\\li_dreadnought.cmp
material_library = ships\\liberty\\li_capships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
mass = 100000.000000
linear_drag = 1.000000
hold_size = 5
fuse = l_dreadnought_fuse, 0.500000, 1
fuse = li_dreadnought_burning_fuse03, 0.000000, 5000000
fuse = li_dreadnought_burning_fuse02, 0.000000, 2000000
fuse = li_dreadnought_burning_fuse01, 0.000000, 1000000
hit_pts =  9000000
explosion_arch = explosion_li_dread
steering_torque = 1501900032.000000, 1501900032.000000, 1501900032.000000
angular_drag = 13200000000.000000, 13200000000.000000, 13200000000.000000
rotation_inertia = 660000000.000000, 15000000512.000000, 15000000512.000000
nudge_force = 3000000.000000
bay_door_anim = Sc_open baydoor
bay_doors_open_snd = hanger_doors_opening
bay_doors_close_snd = hanger_doors_closing
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 1
camera_offset = 50, 300
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 10
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 5
camera_turn_look_ahead_slerp_amount = 1.000000
cockpit = cockpits\\liberty\\li_dread.ini
nanobot_limit = 0 ; = 0
shield_battery_limit = 0 ; = 0
hp_type = hp_turret_special_2, HpTurret_L4_01, HpTurret_L4_02, HpTurret_L3_01, HpTurret_L3_02
hp_type = hp_turret_special_3, HpTurret_L4_03, HpTurret_L4_04
hp_type = hp_turret_special_4, HpTurret_L1_01, HpTurret_L2_01, HpTurret_L4_06, HpTurret_L4_07, HpTurret_L4_05
hp_type = hp_turret_special_6, HpTurret_L2_01


[CollisionGroup]
obj = Leaf01_d1_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 10.000000
debris_type = cap_ship_piece
mass = 10.000000
fuse = ldr_reactor1_damage, 1.000000, 1
separation_explosion = explosion_li
hit_pts = 200000
root_health_proxy = false

[CollisionGroup]
obj = Leaf02_d1_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 300.000000
debris_type = cap_ship_piece
mass = 10.000000
fuse = ldr_reactor2_damage, 1.000000, 1
separation_explosion = explosion_li
hit_pts = 200000
root_health_proxy = false

[CollisionGroup]
obj = Leaf03_d1_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 10.000000
debris_type = cap_ship_piece
mass = 10.000000
fuse = ldr_reactor3_damage, 1.000000, 1
separation_explosion = explosion_li
hit_pts = 200000
root_health_proxy = false

[CollisionGroup]
obj = Leaf04_d1_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 10.000000
debris_type = cap_ship_piece
mass = 10.000000
fuse = ldr_reactor4_damage, 1.000000, 1
separation_explosion = explosion_li
hit_pts = 200000
root_health_proxy = false

[CollisionGroup]
obj = Leaf05_d1_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 600.000000
debris_type = cap_ship_piece
mass = 10.000000
fuse = ldr_reactor5_damage, 1.000000, 1
separation_explosion = explosion_li
hit_pts = 200000
root_health_proxy = false

[CollisionGroup]
obj = Leaf06_d1_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 10.000000
debris_type = cap_ship_piece
mass = 10.000000
fuse = ldr_reactor6_damage, 1.000000, 1
separation_explosion = explosion_li
hit_pts = 200000
root_health_proxy = false

[CollisionGroup]
obj = Leaf07_d1_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 10.000000
debris_type = cap_ship_piece
mass = 10.000000
fuse = ldr_reactor7_damage, 1.000000, 1
separation_explosion = explosion_li
hit_pts = 200000
root_health_proxy = false

[CollisionGroup]
obj = Leaf08_d1_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 500.000000
debris_type = cap_ship_piece
mass = 10.000000
separation_explosion = explosion_li
fuse = ldr_reactor8_damage, 1.000000, 1
hit_pts = 200000
root_health_proxy = false

[CollisionGroup]
obj = Li_bottom_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 10.000000
debris_type = debris_vanish
mass = 200.000000
separation_explosion = explosion_li
fuse = ldr_bottom_damage, 0.500000, 1
dmg_obj = li_dread_bottom_cap
dmg_hp = DpBottom
hit_pts = 1000000
root_health_proxy = true

[CollisionGroup]
obj = Li_cntrltwr_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 10.000000
debris_type = debris_vanish
mass = 200.000000
separation_explosion = explosion_li
fuse = ldr_tower_damage, 0.500000, 1
dmg_obj = li_dread_tower_cap
dmg_hp = DpCntrltwr
hit_pts = 500000
root_health_proxy = false

[CollisionGroup]
obj = Li_rear_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 10.000000
debris_type = debris_vanish
mass = 200.000000
fuse = l_dreadnought_fuse, 0.750000, 1
fuse = li_dreadnought_burning_fuse04, 0.000000, 2000000
dmg_obj = li_dread_rearsection_cap
dmg_hp = DpRearsection
hit_pts = 20000000
root_health_proxy = true

[CollisionGroup]
obj = Li_nose_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 2000.000000
debris_type = cap_ship_piece2
mass = 50.000000
fuse = l_dreadnought_fuse, 0.000000, 1
fuse = li_dreadnought_burning_fuse01, 0.000000, 2000000
group_dmg_hp = DpFrnt
group_dmg_obj = li_dread_front_cap
hit_pts = 20000000
root_health_proxy = true

[CollisionGroup]
obj = Li_frnt_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 10.000000
debris_type = debris_vanish
mass = 200.000000
fuse = l_dreadnought_fuse, 0.250000, 1
fuse = li_dreadnought_burning_fuse02, 0.000000, 2000000
dmg_obj = li_dread_midsection_cap
dmg_hp = DpMidsection
hit_pts = 20000000
root_health_proxy = true

[CollisionGroup]
obj = Li_port_skid_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 10.000000
debris_type = debris_vanish
mass = 200.000000
fuse = ldr_portskid_damage, 0.500000, 1
dmg_obj = li_dread_port_skid_cap
dmg_hp = DpPortskid
separation_explosion = explosion_li
hit_pts = 500000
root_health_proxy = true

[CollisionGroup]
obj = Li_starboard_skid_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 10.000000
debris_type = debris_vanish
mass = 200.000000
fuse = ldr_starskid_damage, 0.600000, 1
separation_explosion = explosion_li
dmg_obj = li_dread_starboard_skid_cap
dmg_hp = DpStarboardskid
hit_pts = 500000
root_health_proxy = true

[CollisionGroup]
obj = Li_reactor_core_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 500.000000
debris_type = cap_ship_piece2
mass = 20.000000
fuse = l_dreadnought_fuse, 1.000000, 1
hit_pts = 100000000
root_health_proxy = false

[CollisionGroup]
obj = Li_reactor_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 10.000000
debris_type = debris_vanish
mass = 200.000000
fuse = l_dreadnought_fuse, 1.000000, 1
hit_pts = 20000000
root_health_proxy = true

[CollisionGroup]
obj = Li_engine_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 10.000000
debris_type = debris_vanish
mass = 200.000000
fuse = ldr_engine_damage, 1.000000, 1
dmg_obj = li_dread_engine_cap
dmg_hp = DpEngine
hit_pts = 1000000
separation_explosion = explosion_li
root_health_proxy = false

[Simple]
nickname = li_dread_bottom_cap
DA_archetype = Ships\\liberty\\li_dreadnought\\li_dreadnought_dmg_bottom.3db
material_library = ships\\liberty\\li_capships.mat
mass = 10.000000
hit_pts = 200
LODranges = 0, 20000

[Simple]
nickname = li_dread_tower_cap
DA_archetype = Ships\\liberty\\li_dreadnought\\li_dreadnought_dmg_cntrltwr.3db
material_library = ships\\liberty\\li_capships.mat
mass = 10.000000
hit_pts = 200
LODranges = 0, 20000

[Simple]
nickname = li_dread_engine_cap
DA_archetype = Ships\\liberty\\li_dreadnought\\li_dreadnought_dmg_engine.3db
material_library = ships\\liberty\\li_capships.mat
mass = 10.000000
hit_pts = 200
LODranges = 0, 20000

[Simple]
nickname = li_dread_front_cap
DA_archetype = Ships\\liberty\\li_dreadnought\\li_dreadnought_dmg_front.3db
material_library = ships\\liberty\\li_capships.mat
mass = 10.000000
hit_pts = 200
LODranges = 0, 20000

[Simple]
nickname = li_dread_midsection_cap
DA_archetype = Ships\\liberty\\li_dreadnought\\li_dreadnought_dmg_midsection.3db
material_library = ships\\liberty\\li_capships.mat
mass = 10.000000
hit_pts = 200
LODranges = 0, 20000

[Simple]
nickname = li_dread_port_skid_cap
DA_archetype = Ships\\liberty\\li_dreadnought\\li_dreadnought_dmg_port_skid.3db
material_library = ships\\liberty\\li_capships.mat
mass = 10.000000
hit_pts = 200
LODranges = 0, 20000

[Simple]
nickname = li_dread_rearsection_cap
DA_archetype = Ships\\liberty\\li_dreadnought\\li_dreadnought_dmg_rearsection.3db
material_library = ships\\liberty\\li_capships.mat
mass = 10.000000
hit_pts = 200
LODranges = 0, 20000

[Simple]
nickname = li_dread_starboard_skid_cap
DA_archetype = Ships\\liberty\\li_dreadnought\\li_dreadnought_dmg_starboard_skid.3db
material_library = ships\\liberty\\li_capships.mat
mass = 10.000000
hit_pts = 200
LODranges = 0, 20000

[Ship]
ship_class = 4
{ship_br_fighter}
LODranges = 0, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_Brelf
mission_property = can_use_berths
type = FIGHTER
DA_archetype = ships\\bretonia\\br_fighter\\br_fighter.cmp
material_library = ships\\bretonia\\br_playerships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
cockpit = cockpits\\bretonia\\b_fighter.ini
pilot_mesh = generic_pilot
linear_drag = 1.000000
steering_torque = 18000.000000, 18000.000000, 58000.000000
angular_drag = 15000.000000, 15000.000000, 35000.000000
rotation_inertia = 2800.000000, 2800.000000, 1000.000000
max_bank_angle = 5 ;35
camera_offset = 9, 29
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 23
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 30
camera_turn_look_ahead_slerp_amount = 1.000000
explosion_arch = explosion_br
nudge_force = 50000.000000
bay_door_anim = Sc_open dock1
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 1

[CollisionGroup]
obj = br_fighter_tail_lod1
separable = true
parent_impulse = 20.000000
child_impulse = 8.000000
debris_type = debris_small_ship
dmg_hp = DpTail
dmg_obj = br_fighter_dmg_tail_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Tail
hit_pts = {bf_tail_hit_pts}
root_health_proxy = false
explosion_resistance = {bf_tail_expl_resist}

[CollisionGroup] 
obj = br_fighter_engine_lod1 
separable = true 
parent_impulse = 250.000000 
child_impulse = 7.000000 
debris_type = debris_small_ship 
dmg_hp = DpEngine
dmg_obj = br_fighter_dmg_engine_cap
separation_explosion = explosion_small_ship_breakoff 
mass = 5.000000 
type = Engine 
hit_pts = {bf_engine_hit_pts}
root_health_proxy = false 
explosion_resistance = {bf_engine_expl_resist}

[Simple]
nickname = br_fighter_dmg_tail_cap
DA_archetype = ships\\bretonia\\br_fighter\\br_fighter_dmg_tail.3db
material_library = ships\\bretonia\\br_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2000

[Simple]
nickname = br_fighter_dmg_engine_cap
DA_archetype = ships\\BRETONIA\\BR_FIGHTER\\br_fighter_dmg_engine.3db
material_library = ships\\bretonia\\br_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2000

[Ship]
ship_class = 5
{ship_br_elite}
msg_id_prefix = gcs_refer_shiparch_Brehf
mission_property = can_use_berths
LODranges = 0, 1000, 5000, 10000
type = FIGHTER
DA_archetype = ships\\bretonia\\br_elite\\br_elite.cmp
material_library = ships\\bretonia\\br_playerships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
cockpit = cockpits\\bretonia\\b_elite.ini
pilot_mesh = generic_pilot
max_bank_angle = 2 ;30
camera_offset = 9, 39
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 17
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 26
camera_turn_look_ahead_slerp_amount = 1.000000
linear_drag = 1.000000
explosion_arch = explosion_br
nudge_force = 10000.000000
bay_door_anim = sc_open baydoor
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2
steering_torque = 43000.000000, 43000.000000, 230000.000000
angular_drag = 41000.000000, 41000.000000, 141000.000000
rotation_inertia = 8400.000000, 8400.000000, 8400.000000

[CollisionGroup]
obj = br_port_wing_lod1
separable = true
parent_impulse = 90.000000
child_impulse = 20.000000
debris_type = debris_small_ship
dmg_hp = DpPort_Wing
dmg_obj = br_elite_dmg_port_wing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Wing
hit_pts = {be_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {be_wing_expl_resist}

[CollisionGroup]
obj = br_star_wing_lod1
separable = true
parent_impulse = 90.000000
child_impulse = 20.000000
debris_type = debris_small_ship
dmg_hp = DpStarboard_Wing
dmg_obj = br_elite_dmg_star_wing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Wing
hit_pts = {be_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {be_wing_expl_resist}

[CollisionGroup]
obj = br_tail_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpTail
dmg_obj = br_elite_dmg_tail_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Tail
hit_pts = {be_tail_hit_pts}
root_health_proxy = false
explosion_resistance = {be_tail_expl_resist}

[CollisionGroup] 
obj = br_port_eng_lod1 
separable = true 
parent_impulse = 250.000000 
child_impulse = 7.000000 
debris_type = debris_small_ship 
dmg_hp = DpPort_Engine
dmg_obj = br_elite_dmg_port_eng_cap
separation_explosion = explosion_small_ship_breakoff 
mass = 5.000000 
type = Engine 
hit_pts = {be_engine_hit_pts} 
root_health_proxy = false 
explosion_resistance = {be_engine_expl_resist}

[CollisionGroup] 
obj = br_star_eng_lod1 
separable = true 
parent_impulse = 250.000000 
child_impulse = 7.000000 
debris_type = debris_small_ship 
dmg_hp = DpStarBoard_engine 
dmg_obj = br_elite_dmg_star_eng_cap
separation_explosion = explosion_small_ship_breakoff 
mass = 5.000000 
type = Engine 
hit_pts = {be_engine_hit_pts} 
root_health_proxy = false
explosion_resistance = {be_engine_expl_resist}

[Ship]
ship_class = 6
{ship_br_elite2}
msg_id_prefix = gcs_refer_shiparch_Brehf
mission_property = can_use_berths
LODranges = 0, 1000, 5000, 10000
type = FIGHTER
DA_archetype = ships\\bretonia\\br_elite\\br_elite.cmp
material_library = ships\\bretonia\\br_playerships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapknight
cockpit = cockpits\\bretonia\\b_elite.ini
pilot_mesh = generic_pilot
max_bank_angle = 2 ;30
camera_offset = 9, 39
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 17
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 26
camera_turn_look_ahead_slerp_amount = 1.000000
linear_drag = 1.000000
explosion_arch = explosion_br
nudge_force = 80000.000000
bay_door_anim = sc_open baydoor
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2
steering_torque = 43000.000000, 43000.000000, 230000.000000
angular_drag = 41000.000000, 41000.000000, 141000.000000
rotation_inertia = 8400.000000, 8400.000000, 8400.000000

[CollisionGroup]
obj = br_port_wing_lod1
separable = true
parent_impulse = 90.000000
child_impulse = 20.000000
debris_type = debris_small_ship
dmg_hp = DpPort_Wing
dmg_obj = br_elite_dmg_port_wing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Wing
hit_pts = {be2_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {be2_wing_expl_resist}

[CollisionGroup]
obj = br_star_wing_lod1
separable = true
parent_impulse = 90.000000
child_impulse = 20.000000
debris_type = debris_small_ship
dmg_hp = DpStarboard_Wing
dmg_obj = br_elite_dmg_star_wing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Wing
hit_pts = {be2_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {be2_wing_expl_resist}

[CollisionGroup]
obj = br_tail_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpTail
dmg_obj = br_elite_dmg_tail_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Tail
hit_pts = {be2_tail_hit_pts}
root_health_proxy = false
explosion_resistance = {be2_tail_expl_resist}

[CollisionGroup] 
obj = br_port_eng_lod1 
separable = true 
parent_impulse = 250.000000 
child_impulse = 7.000000 
debris_type = debris_small_ship 
dmg_hp = DpPort_Engine
dmg_obj = br_elite_dmg_port_eng_cap
separation_explosion = explosion_small_ship_breakoff 
mass = 5.000000 
type = Engine 
hit_pts = {be2_engine_hit_pts} 
root_health_proxy = false 
explosion_resistance = {be2_engine_expl_resist}

[CollisionGroup] 
obj = br_star_eng_lod1 
separable = true 
parent_impulse = 250.000000 
child_impulse = 7.000000 
debris_type = debris_small_ship 
dmg_hp = DpStarBoard_engine 
dmg_obj = br_elite_dmg_star_eng_cap
separation_explosion = explosion_small_ship_breakoff 
mass = 5.000000 
type = Engine 
hit_pts = {be2_engine_hit_pts} 
root_health_proxy = false
explosion_resistance = {be2_engine_expl_resist}

[Simple]
nickname = br_elite_dmg_port_wing_cap
DA_archetype = ships\\bretonia\\br_elite\\br_elite_dmg_port_wing.3db
material_library = ships\\bretonia\\br_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2000

[Simple]
nickname = br_elite_dmg_star_wing_cap
DA_archetype = ships\\bretonia\\br_elite\\br_elite_dmg_starboard_wing.3db
material_library = ships\\bretonia\\br_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2000

[Simple]
nickname = br_elite_dmg_tail_cap
DA_archetype = ships\\bretonia\\br_elite\\br_elite_dmg_tail.3db
material_library = ships\\bretonia\\br_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2000

[Simple]
nickname = br_elite_dmg_port_eng_cap
DA_archetype = ships\\bretonia\\br_elite\\br_elite_dmg_port_engine.3db
material_library = ships\\bretonia\\br_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2000

[Simple]
nickname = br_elite_dmg_star_eng_cap
DA_archetype = ships\\bretonia\\br_elite\\br_elite_dmg_starboard_engine.3db
material_library = ships\\bretonia\\br_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2000

[Ship]
ship_class = 8
{ship_br_freighter}
msg_id_prefix = gcs_refer_shiparch_Bref
mission_property = can_use_berths
LODranges = 0, 1000, 5000, 10000
type = FREIGHTER
DA_archetype = ships\\bretonia\\br_freighter\\br_freighter.cmp
material_library = ships\\bretonia\\br_playerships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
cockpit = cockpits\\bretonia\\b_freighter.ini
pilot_mesh = generic_pilot
linear_drag = 1.000000
max_bank_angle = 1 ;15
camera_offset = 14, 54
camera_angular_acceleration = 0.035000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 20
camera_turn_look_ahead_slerp_amount = 1.000000
explosion_arch = explosion_br
steering_torque = 54000.000000, 54000.000000, 104000.000000
angular_drag = 60000.000000, 60000.000000, 60000.000000
rotation_inertia = 16800.000000, 16800.000000, 16800.000000
nudge_force = 100000.000000
bay_door_anim = Sc_open dock1
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2

[CollisionGroup]
obj = br_freighter_port_wing_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 30.000000
debris_type = debris_small_ship
dmg_hp = DpPort_Wing
dmg_obj = br_freighter_dmg_port_wing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Wing
hit_pts = {bfr_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {bfr_wing_expl_resist}

[CollisionGroup]
obj = br_freighter_star_wing_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 30.000000
debris_type = debris_small_ship
dmg_hp = DpStarboard_Wing
dmg_obj = br_freighter_dmg_star_wing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Wing
hit_pts = {bfr_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {bfr_wing_expl_resist}

[CollisionGroup]
obj = br_freighter_star_eng_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 30.000000
debris_type = debris_small_ship
dmg_hp = DpStarboard_Engine
dmg_obj = br_freighter_dmg_star_eng_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Engine
hit_pts = {bfr_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {bfr_engine_expl_resist}

[CollisionGroup]
obj = br_freighter_port_eng_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 30.000000
debris_type = debris_small_ship
dmg_hp = DpPort_Engine
dmg_obj = br_freighter_dmg_port_eng_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Engine
hit_pts = {bfr_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {bfr_engine_expl_resist}

[Simple]
nickname = br_freighter_dmg_port_wing_cap
DA_archetype = ships\\bretonia\\br_freighter\\br_freighter_dmg_port_wing.3db
material_library = ships\\bretonia\\br_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2200

[Simple]
nickname = br_freighter_dmg_star_wing_cap
DA_archetype = ships\\bretonia\\br_freighter\\br_freighter_dmg_starboard_wing.3db
material_library = ships\\bretonia\\br_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2200

[Simple]
nickname = br_freighter_dmg_port_eng_cap
DA_archetype = ships\\bretonia\\br_freighter\\br_freighter_dmg_port_engine.3db
material_library = ships\\bretonia\\br_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2200

[Simple]
nickname = br_freighter_dmg_star_eng_cap
DA_archetype = ships\\bretonia\\br_freighter\\br_freighter_dmg_starboard_engine.3db
material_library = ships\\bretonia\\br_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2200

[Ship]
ship_class = 12
nickname = br_gunboat
LODranges = 0, 5000, 10000, 25000
msg_id_prefix = gcs_refer_shiparch_Breg
mission_property = can_use_med_moors
type = GUNBOAT
DA_archetype = ships\\bretonia\\br_gunship\\br_gunship.cmp
material_library = ships\\bretonia\\br_capships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
linear_drag = 1.000000
mass = 1000.000000
hold_size = 10
hit_pts = 250000
explosion_arch = explosion_br_gship
fuse = br_gunship_fuse, 0.000000, 1
fuse = br_gunship_burning_fuse01, 0.000000, 100000
fuse = br_gunship_burning_fuse02, 0.000000, 30000
steering_torque = 60000000.000000, 60000000.000000, 60000000.000000
angular_drag = 120000000.000000, 120000000.000000, 120000000.000000
rotation_inertia = 16800000.000000, 16800000.000000, 16800000.000000
nudge_force = 150000.000000
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2
max_bank_angle = 1 ;15
camera_offset = 40, 100
camera_angular_acceleration = 0.035000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 20
camera_turn_look_ahead_slerp_amount = 1.000000
cockpit = cockpits\\bretonia\\br_gunboat.ini
nanobot_limit = 0 ; = 0
shield_battery_limit = 0 ; = 0
;hp_type = hp_thruster, HpEngine01, HpEngine02
hp_type = hp_turret_special_1, HpTurret_B4_01
hp_type = hp_turret_special_2, HpTurret_B3_02, HpTurret_B3_03
hp_type = hp_turret_special_5, HpTurret_B3_01
strafe_force = 20000
strafe_power_usage = 5

[CollisionGroup]
obj = br_cntrl_twr_lod1
separable = true
debris_type = debris_vanish
parent_impulse = 500.000000
child_impulse = 10.000000
mass = 200.000000
fuse = bgb_tower_damage, 0.000000, 1
separation_explosion = explosion_br
dmg_obj = b_gunship_tower_cap
dmg_hp = DpCntrltwr
hit_pts = 100000
root_health_proxy = false
linked_equip = ge_bg_engine_01

[CollisionGroup]
obj = br_tail_lod1
separable = true
parent_impulse = 500.000000
child_impulse = 10.000000
debris_type = debris_vanish
mass = 200.000000
fuse = bgb_tail_damage, 0.000000, 1
separation_explosion = explosion_br
dmg_obj = b_gunship_tail_cap
dmg_hp = DpTail
hit_pts = 3500
root_health_proxy = false

[CollisionGroup]
obj = br_port_eng_lod1
separable = true
parent_impulse = 500.000000
child_impulse = 10.000000
debris_type = debris_vanish
mass = 200.000000
fuse = bgb_port_eng_damage, 0.000000, 1
separation_explosion = explosion_br
dmg_obj = b_gunship_port_eng_cap
dmg_hp = DpPortengine
hit_pts = 150000
root_health_proxy = false

[CollisionGroup]
obj = br_star_eng_lod1
separable = true
parent_impulse = 500.000000
child_impulse = 10.000000
debris_type = debris_vanish
mass = 200.000000
fuse = bgb_star_eng_damage, 0.000000, 1
separation_explosion = explosion_br
dmg_obj = b_gunship_starboard_eng_cap
dmg_hp = DpStarboardengine
hit_pts = 150000
root_health_proxy = false

[CollisionGroup]
obj = br_port_wing_lod1
separable = true
parent_impulse = 0
child_impulse = 1500.000000
debris_type = cap_ship_piece
mass = 200.000000
fuse = br_gunship_fuse, 0.000000, 1
group_dmg_hp = DpPortwing
group_dmg_obj = b_gunship_port_wing_cap
hit_pts = 1500000
root_health_proxy = true

[CollisionGroup]
obj = br_star_wing_lod1
separable = true
parent_impulse = 0
child_impulse = 1800.000000
debris_type = cap_ship_piece
mass = 200.000000
fuse = br_gunship_fuse, 0.000000, 1
group_dmg_hp = DpStarboardwing
group_dmg_obj = b_gunship_starboard_wing_cap
hit_pts = 1500000
root_health_proxy = true

[Simple]
nickname = b_gunship_tower_cap
DA_archetype = Ships\\bretonia\\br_gunship\\br_gunship_dmg_cntrl_twr.3db
material_library = ships\\bretonia\\br_capships.mat
mass = 10.000000
hit_pts = 200
LODranges = 0, 300, 4000

[Simple]
nickname = b_gunship_tail_cap
DA_archetype = Ships\\bretonia\\br_gunship\\br_gunship_dmg_tail.3db
material_library = ships\\bretonia\\br_capships.mat
mass = 10.000000
hit_pts = 200
LODranges = 0, 300, 4000

[Simple]
nickname = b_gunship_port_wing_cap
DA_archetype = Ships\\bretonia\\br_gunship\\br_gunship_dmg_port_wing.3db
material_library = ships\\bretonia\\br_capships.mat
mass = 10.000000
hit_pts = 200
LODranges = 0, 300, 4000

[Simple]
nickname = b_gunship_starboard_wing_cap
DA_archetype = Ships\\bretonia\\br_gunship\\br_gunship_dmg_starboard_wing.3db
material_library = ships\\bretonia\\br_capships.mat
mass = 10.000000
hit_pts = 200
LODranges = 0, 300, 4000

[Simple]
nickname = b_gunship_port_eng_cap
DA_archetype = Ships\\bretonia\\br_gunship\\br_gunship_dmg_port_engine.3db
material_library = ships\\bretonia\\br_capships.mat
mass = 10.000000
hit_pts = 200
LODranges = 0, 300, 4000

[Simple]
nickname = b_gunship_starboard_eng_cap
DA_archetype = Ships\\bretonia\\br_gunship\\br_gunship_dmg_starboard_engine.3db
material_library = ships\\bretonia\\br_capships.mat
mass = 10.000000
hit_pts = 200
LODranges = 0, 300, 4000

[Ship]
ids_name = 237006
ids_info = 66504
ship_class = 13
nickname = br_destroyer
msg_id_prefix = gcs_refer_shiparch_Bred
mission_property = can_use_med_moors
LODranges = 0, 5000, 10000, 25000
type = CRUISER
DA_archetype = ships\\bretonia\\br_destroyer\\br_destroyer.cmp
material_library = ships\\bretonia\\br_capships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
linear_drag = 1.000000
mass = 500.000000
hold_size = 10
hit_pts = 500000
explosion_arch = explosion_br_destroyer
fuse = br_destroyer_fuse, 1.000000, 1
fuse = br_destroyer_burning_fuse01, 0.000000, 100000
fuse = br_destroyer_burning_fuse02, 0.000000, 50000
steering_torque = 20000000.000000, 20000000.000000, 20000000.000000
angular_drag = 132000000.000000, 132000000.000000, 132000000.000000
rotation_inertia = 40000000.000000, 40000000.000000, 40000000.000000
nudge_force = 360000.000000
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2
max_bank_angle = 5 ;35
camera_offset = 30, 125
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 20
camera_turn_look_ahead_slerp_amount = 1.000000
cockpit = cockpits\\bretonia\\br_destroyer.ini
nanobot_limit = 0 ; = 0
shield_battery_limit = 0 ; = 0
hp_type = hp_thruster, HpThruster01
hp_type = hp_turret_special_2, HpTurret_B3_01, HpTurret_B3_02
hp_type = hp_turret_special_4, HpTurret_B1_01, HpTurret_B2_02, HpTurret_B2_01

[CollisionGroup]
obj = Br_frnt_bdy_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 600.000000
debris_type = cap_ship_piece
mass = 201.000000
fuse = br_destroyer_fuse, 0.000000, 1
hit_pts = 5000000
root_health_proxy = true

[CollisionGroup]
obj = Br_frnt_bdy_top_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 10.000000
debris_type = cap_ship_piece
mass = 201.000000
fuse = br_destroyer_fuse, 0.000000, 1
dmg_hp = DpFrnt_bdy_top
dmg_obj = b_destroyer_body_cap
hit_pts = 5000000
root_health_proxy = true

[CollisionGroup]
obj = Br_wpn_platform_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 10.000000
debris_type = debris_vanish
mass = 201.000000
separation_explosion = explosion_br
fuse = bdr_platform_damage, 0.000000, 1
dmg_obj = b_destroyer_wplat_cap
dmg_hp = DpWpn_platform
hit_pts = 1500000
root_health_proxy = false

[CollisionGroup]
obj = br_cntrl_twr_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 10.000000
debris_type = debris_vanish
mass = 201.000000
fuse = bdr_tower_damage, 0.000000, 1
dmg_obj = b_destroyer_tower_cap
dmg_hp = DpCntrltwr
hit_pts = 500000
root_health_proxy = false

[CollisionGroup]
obj = br_port_eng_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 10.000000
debris_type = debris_vanish
mass = 201.000000
separation_explosion = explosion_br
fuse = bdr_port_eng_damage, 0.000000, 1
dmg_obj = b_destroyer_port_eng_cap
dmg_hp = DpPortengine
hit_pts = 500000
root_health_proxy = false

[CollisionGroup]
obj = br_star_eng_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 10.000000
debris_type = debris_vanish
mass = 201.000000
separation_explosion = explosion_br
fuse = bdr_star_eng_damage, 0.000000, 1
dmg_obj = b_destroyer_starboard_eng_cap
dmg_hp = DpStarboardengine
hit_pts = 500000
root_health_proxy = false

[Simple]
nickname = b_destroyer_tower_cap
DA_archetype = Ships\\bretonia\\br_destroyer\\br_destroyer_dmg_cntrl_twr.3db
material_library = ships\\bretonia\\br_capships.mat
LODranges = 0, 350, 6000
mass = 10.000000
hit_pts = 200

[Simple]
nickname = b_destroyer_body_cap
DA_archetype = Ships\\bretonia\\br_destroyer\\br_destroyer_dmg_frnt_bdy_top.3db
material_library = ships\\bretonia\\br_capships.mat
LODranges = 0, 350, 6000
mass = 10.000000
hit_pts = 200

[Simple]
nickname = b_destroyer_wplat_cap
DA_archetype = Ships\\bretonia\\br_destroyer\\br_destroyer_dmg_wpn_platform.3db
material_library = ships\\bretonia\\br_capships.mat
LODranges = 0, 350, 6000
mass = 10.000000
hit_pts = 200

[Simple]
nickname = b_destroyer_port_eng_cap
DA_archetype = Ships\\bretonia\\br_destroyer\\br_destroyer_dmg_port_engine.3db
material_library = ships\\bretonia\\br_capships.mat
LODranges = 0, 350, 6000
mass = 10.000000
hit_pts = 200

[Simple]
nickname = b_destroyer_starboard_eng_cap
DA_archetype = Ships\\bretonia\\br_destroyer\\br_destroyer_dmg_starboard_engine.3db
material_library = ships\\bretonia\\br_capships.mat
LODranges = 0, 350, 6000
mass = 10.000000
hit_pts = 200

[Ship]
ids_name = 237005
ids_info = 66503
ship_class = 16
nickname = br_battleship
LODranges = 0, 5000, 10000, 20000, 50000
msg_id_prefix = gcs_refer_shiparch_Breb
mission_property = can_use_large_moors
type = CAPITAL
DA_archetype = ships\\bretonia\\br_battleship\\br_battleship.cmp
material_library = ships\\bretonia\\br_capships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
linear_drag = 1.000000
mass = 100000.000000
hold_size = 10
hit_pts = 9000000
fuse = b_battleship_body_fuse, 0.500000, 1
fuse = br_battleship_burning_fuse02, 0.000000, 5000000
fuse = br_battleship_burning_fuse02, 0.000000, 2500000
fuse = br_battleship_burning_fuse01, 0.000000, 1000000
explosion_arch = explosion_br_bship
steering_torque = 1501900032.000000, 1501900032.000000, 1501900032.000000
angular_drag = 13200000000.000000, 13200000000.000000, 13200000000.000000
rotation_inertia = 15000000512.000000, 15000000512.000000, 15000000512.000000
nudge_force = 3000000.000000
bay_door_anim = Sc_open dock1
bay_doors_open_snd = hanger_doors_opening
bay_doors_close_snd = hanger_doors_closing
HP_bay_surface = HpRunninglight15
HP_bay_external = HpRunninglight16
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 1
max_bank_angle = 5 ;35
camera_offset = 50, 160
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 20
camera_turn_look_ahead_slerp_amount = 1.000000
cockpit = cockpits\\bretonia\\br_battleship.ini
nanobot_limit = 0 ; = 0
shield_battery_limit = 0 ; = 0
hp_type = hp_turret_special_3, HpTurret_B2_01, HpTurret_B2_02, HpTurret_B2_03, HpTurret_B2_04
hp_type = hp_turret_special_4, HpTurret_B1_01, HpTurret_B1_02, HpTurret_B1_03
hp_type = hp_turret_special_6, HpTurret_B1_01

[CollisionGroup]
obj = br_cntrl_twr_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 10.000000
debris_type = debris_vanish
mass = 30.000000
dmg_hp = DpCntrltwr
dmg_obj = b_battleship_tower_cap
fuse = bbs_tower_damage, 0.100000, 1
separation_explosion = explosion_br
hit_pts = 500000
root_health_proxy = false

[CollisionGroup]
obj = Br_frnt_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 5000.000000
debris_type = cap_ship_piece2
mass = 200.000000
fuse = b_battleship_body_fuse, 0.000000, 1
fuse = br_battleship_burning_fuse01, 0.000000, 2000000
group_dmg_hp = DpNeck
group_dmg_obj = b_battleship_head_dmg_cap
hit_pts = 20000000
root_health_proxy = true

[CollisionGroup]
obj = Br_main_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 10.000000
debris_type = debris_vanish
mass = 200.000000
dmg_hp = DpMain
dmg_obj = b_battleship_neck_dmg_cap
fuse = b_battleship_body_fuse, 0.300000, 1
fuse = br_battleship_burning_fuse01, 0.000000, 2000000
hit_pts = 20000000
root_health_proxy = true

[CollisionGroup]
obj = Br_port_gen_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 10.000000
debris_type = debris_vanish
mass = 20.000000
dmg_hp = DpPortgen
dmg_obj = b_battleship_port_gen_cap
fuse = bbs_port_gen_damage, 0.000000, 1
separation_explosion = explosion_br
hit_pts = 300000
root_health_proxy = false

[CollisionGroup]
obj = Br_starboard_gen_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 10.000000
debris_type = debris_vanish
mass = 20.000000
dmg_hp = DpStarboardgen
dmg_obj = b_battleship_starboard_gen_cap
fuse = bbs_star_gen_damage, 0.000000, 1
separation_explosion = explosion_br
hit_pts = 300000
root_health_proxy = false

[CollisionGroup]
obj = br_tail_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 10.000000
debris_type = debris_vanish
mass = 200.000000
dmg_hp = DpTail
dmg_obj = b_battleship_butt_dmg_cap
fuse = bbs_rear_damage, 0.900000, 1
hit_pts = 2000000
root_health_proxy = true

[CollisionGroup]
obj = Br_thruster_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 5000.000000
debris_type = cap_ship_piece
mass = 200.000000
dmg_hp = DpReactor
dmg_obj = b_battleship_tail_dmg_cap
fuse = bbs_rear_damage, 0.900000, 10
hit_pts = 1000000
root_health_proxy = false

[CollisionGroup]
obj = Br_engine_lod1
separable = true
debris_type = debris_vanish
mass = 30.000000
dmg_hp = DpEngine
dmg_obj = b_battleship_engine_cap
fuse = bbs_rear_damage, 1.000000, 1
separation_explosion = explosion_br
parent_impulse = 10.000000
child_impulse = 10.000000
hit_pts = 1000000
root_health_proxy = false

[Simple]
nickname = b_battleship_head_dmg_cap
DA_archetype = Ships\\bretonia\\br_battleship\\br_battleship_dmg_neck.3db
mass = 1000.000000
hit_pts = 200
material_library = ships\\bretonia\\br_capships.mat
LODranges = 0, 20000

[Simple]
nickname = b_battleship_neck_dmg_cap
DA_archetype = Ships\\bretonia\\br_battleship\\br_battleship_dmg_main.3db
mass = 1000.000000
hit_pts = 200
material_library = ships\\bretonia\\br_capships.mat
LODranges = 0, 20000

[Simple]
nickname = b_battleship_butt_dmg_cap
DA_archetype = Ships\\bretonia\\br_battleship\\br_battleship_dmg_tail.3db
mass = 1000.000000
hit_pts = 200
material_library = ships\\bretonia\\br_capships.mat
LODranges = 0, 20000

[Simple]
nickname = b_battleship_tail_dmg_cap
DA_archetype = Ships\\bretonia\\br_battleship\\br_battleship_dmg_reactor.3db
mass = 1000.000000
hit_pts = 200
material_library = ships\\bretonia\\br_capships.mat
LODranges = 0, 20000

[Simple]
nickname = b_battleship_tower_cap
DA_archetype = Ships\\bretonia\\br_battleship\\br_battleship_dmg_cntrltwr.3db
mass = 1000.000000
hit_pts = 200
material_library = ships\\bretonia\\br_capships.mat
LODranges = 0, 20000

[Simple]
nickname = b_battleship_port_gen_cap
DA_archetype = Ships\\bretonia\\br_battleship\\br_battleship_dmg_port_gen.3db
mass = 10.000000
hit_pts = 200
material_library = ships\\bretonia\\br_capships.mat
LODranges = 0, 20000

[Simple]
nickname = b_battleship_starboard_gen_cap
DA_archetype = Ships\\bretonia\\br_battleship\\br_battleship_dmg_starboard_gen.3db
mass = 10.000000
hit_pts = 200
material_library = ships\\bretonia\\br_capships.mat
LODranges = 0, 20000

[Simple]
nickname = b_battleship_engine_cap
DA_archetype = Ships\\bretonia\\br_battleship\\br_battleship_dmg_engine.3db
mass = 10.000000
hit_pts = 200
material_library = ships\\bretonia\\br_capships.mat
LODranges = 0, 20000

[Ship]
ship_class = 4
{ship_ku_fighter}
msg_id_prefix = gcs_refer_shiparch_Kuslf
mission_property = can_use_berths
LODranges = 0, 1000, 5000, 10000
type = FIGHTER
DA_archetype = ships\\kusari\\ku_fighter\\ku_fighter.cmp
material_library = ships\\kusari\\ku_playerships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
cockpit = cockpits\\kusari\\k_fighter.ini
pilot_mesh = generic_pilot
linear_drag = 1.000000
max_bank_angle = 5 ;35
camera_offset = 6, 25
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 23
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 30
camera_turn_look_ahead_slerp_amount = 1.000000
explosion_arch = explosion_ku
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 25000.000000, 25000.000000, 58000.000000
angular_drag = 15000.000000, 15000.000000, 35000.000000
rotation_inertia = 3800.000000, 3800.000000, 1000.000000
nudge_force = 60000.000000
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 1

[CollisionGroup]
obj = wing_starboard_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
dmg_hp = DpWing_starboard
dmg_obj = ku_fighter_dmg_wing_starboard_cap
type = Starboard_Fin
hit_pts = {kf_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {kf_wing_expl_resist}

[CollisionGroup]
obj = wing_port_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
dmg_hp = DpWing_port
dmg_obj = ku_fighter_dmg_wing_port_cap
type = Port_Fin
hit_pts = {kf_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {kf_wing_expl_resist}

[CollisionGroup] 
obj = engine_lod1 
separable = true 
parent_impulse = 250.000000 
child_impulse = 7.000000 
debris_type = debris_small_ship 
dmg_hp = DpEngine01 
dmg_obj = ku_fighter_dmg_engine_cap
separation_explosion = explosion_small_ship_breakoff 
mass = 5.000000 
type = Engine 
hit_pts = {kf_engine_hit_pts}
root_health_proxy = false 
explosion_resistance = {kf_engine_expl_resist}


[Simple]
nickname = ku_fighter_dmg_wing_starboard_cap
DA_archetype = Ships\\kusari\\ku_fighter\\ku_fighter_dmg_wing_starboard.3db
material_library = ships\\kusari\\ku_playerships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = ku_fighter_dmg_wing_port_cap
DA_archetype = Ships\\kusari\\ku_fighter\\ku_fighter_dmg_wing_port.3db
material_library = ships\\kusari\\ku_playerships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = ku_fighter_dmg_engine_cap
DA_archetype = Ships\\kusari\\ku_fighter\\ku_fighter_dmg_engine01.3db
material_library = ships\\kusari\\ku_playerships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Ship]
ship_class = 5
{ship_ku_elite}
msg_id_prefix = gcs_refer_shiparch_Kushf
mission_property = can_use_berths
LODranges = 0, 1000, 5000, 10000
type = FIGHTER
DA_archetype = ships\\kusari\\ku_elite\\ku_elite.cmp
material_library = ships\\kusari\\ku_playerships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
cockpit = cockpits\\kusari\\k_elite.ini
pilot_mesh = generic_pilot
linear_drag = 1.000000
max_bank_angle = 2 ;30
camera_offset = 6.500000, 29
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 17
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 25
camera_turn_look_ahead_slerp_amount = 1.000000
explosion_arch = explosion_ku
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 43000.000000, 43000.000000, 230000.000000
angular_drag = 41000.000000, 41000.000000, 141000.000000
rotation_inertia = 8400.000000, 8400.000000, 8400.000000
nudge_force = 80000.000000
bay_door_anim = Sc_open baydoor
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2

[CollisionGroup]
obj = starboard_wing_lod1
separable = true
parent_impulse = 160.000000
child_impulse = 60.000000
debris_type = debris_small_ship
dmg_hp = DpStarboard_Wing
dmg_obj = ku_elite_dmg_starboard_wing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Wing
hit_pts = {ke_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {ke_wing_expl_resist}

[CollisionGroup]
obj = port_wing_lod1
separable = true
parent_impulse = 160.000000
child_impulse = 60.000000
debris_type = debris_small_ship
dmg_hp = DpPort_Wing
dmg_obj = ku_elite_dmg_port_wing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Wing
hit_pts = {ke_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {ke_wing_expl_resist}


[CollisionGroup]
obj = tail_lod1
separable = true
parent_impulse = 160.000000
child_impulse = 60.000000
debris_type = debris_small_ship
dmg_hp = DpTail
dmg_obj = ku_elite_dmg_port_tail_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Tail
hit_pts = {ke_tail_hit_pts}
root_health_proxy = false
explosion_resistance = {ke_tail_expl_resist}

[CollisionGroup]
obj = starboard_spike_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
dmg_hp = DpStarboard _arm rotator
dmg_obj = ku_elite_dmg_starboard_arm_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Arm
hit_pts = {ke_spike_hit_pts}
root_health_proxy = false
explosion_resistance = {ke_spike_expl_resist}

[CollisionGroup]
obj = port_spike_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
dmg_hp = DpPort _arm rotator
dmg_obj = ku_elite_dmg_port_arm_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Arm
hit_pts = {ke_spike_hit_pts}
root_health_proxy = false
explosion_resistance = {ke_spike_expl_resist}


[CollisionGroup] 
obj = starboard_engine_lod1 
separable = true 
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship 
dmg_hp = DpStarBoard_engine 
dmg_obj = ku_elite_dmg_starboard_engine_cap 
separation_explosion = explosion_small_ship_breakoff 
mass = 5.000000 
type = Starboard_Engine 
hit_pts = {ke_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {ke_engine_expl_resist}

[CollisionGroup] 
obj = port_engine_lod1 
separable = true 
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship 
dmg_hp = DpStarBoard_engine 
dmg_obj = ku_elite_dmg_port_engine_cap 
separation_explosion = explosion_small_ship_breakoff 
mass = 5.000000 
type = Port_Engine 
hit_pts = {ke_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {ke_engine_expl_resist}

[Simple]
nickname = ku_elite_dmg_starboard_engine_cap
DA_archetype = Ships\\kusari\\ku_elite\\ku_elite_dmg_starboard_engine.3db
material_library = ships\\kusari\\ku_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2000

[Simple]
nickname = ku_elite_dmg_port_engine_cap
DA_archetype = Ships\\kusari\\ku_elite\\ku_elite_dmg_port_engine.3db
material_library = ships\\kusari\\ku_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2000


[Simple]
nickname = ku_elite_dmg_starboard_wing_cap
DA_archetype = Ships\\kusari\\ku_elite\\ku_elite_dmg_starboard_wing.3db
material_library = ships\\kusari\\ku_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2000

[Simple]
nickname = ku_elite_dmg_port_wing_cap
DA_archetype = Ships\\kusari\\ku_elite\\ku_elite_dmg_port_wing.3db
material_library = ships\\kusari\\ku_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2000

[Simple]
nickname = ku_elite_dmg_port_tail_cap
DA_archetype = Ships\\kusari\\ku_elite\\ku_elite_dmg_tail.3db
material_library = ships\\kusari\\ku_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2000

[Simple]
nickname = ku_elite_dmg_starboard_arm_cap
DA_archetype = Ships\\kusari\\ku_elite\\ku_elite_dmg_starboard_arm_rotator.3db
material_library = ships\\kusari\\ku_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2000

[Simple]
nickname = ku_elite_dmg_port_arm_cap
DA_archetype = Ships\\kusari\\ku_elite\\ku_elite_dmg_port_arm_rotator.3db
material_library = ships\\kusari\\ku_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2000

[Ship]
ship_class = 6
{ship_ku_elite2}
msg_id_prefix = gcs_refer_shiparch_hfighter
mission_property = can_use_berths
LODranges = 0, 1000, 5000, 10000
type = FIGHTER
DA_archetype = ships\\kusari\\ku_elite\\ku_elite.cmp
material_library = ships\\kusari\\ku_playerships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapblood
cockpit = cockpits\\kusari\\k_elite.ini
pilot_mesh = generic_pilot
linear_drag = 1.000000
max_bank_angle = 2 ;30
camera_offset = 7, 24
camera_angular_acceleration = 0.060000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 10
camera_vertical_turn_down_angle = 20
camera_turn_look_ahead_slerp_amount = 1.000000
explosion_arch = explosion_ku
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 43000.000000, 43000.000000, 183000.000000
angular_drag = 41000.000000, 41000.000000, 141000.000000
rotation_inertia = 8400.000000, 8400.000000, 8400.000000
nudge_force = 60000.000000
bay_door_anim = Sc_open baydoor
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2

[CollisionGroup]
obj = starboard_wing_lod1
separable = true
parent_impulse = 160.000000
child_impulse = 60.000000
debris_type = debris_small_ship
dmg_hp = DpStarboard_Wing
dmg_obj = ku_elite_dmg_starboard_wing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Wing
hit_pts = {ke2_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {ke2_wing_expl_resist}

[CollisionGroup]
obj = port_wing_lod1
separable = true
parent_impulse = 160.000000
child_impulse = 60.000000
debris_type = debris_small_ship
dmg_hp = DpPort_Wing
dmg_obj = ku_elite_dmg_port_wing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Wing
hit_pts = {ke2_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {ke2_wing_expl_resist}


[CollisionGroup]
obj = tail_lod1
separable = true
parent_impulse = 160.000000
child_impulse = 60.000000
debris_type = debris_small_ship
dmg_hp = DpTail
dmg_obj = ku_elite_dmg_port_tail_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Tail
hit_pts = {ke2_tail_hit_pts}
root_health_proxy = false
explosion_resistance = {ke2_tail_expl_resist}

[CollisionGroup]
obj = starboard_spike_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
dmg_hp = DpStarboard _arm rotator
dmg_obj = ku_elite_dmg_starboard_arm_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Arm
hit_pts = {ke2_spike_hit_pts}
root_health_proxy = false
explosion_resistance = {ke2_spike_expl_resist}

[CollisionGroup]
obj = port_spike_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
dmg_hp = DpPort _arm rotator
dmg_obj = ku_elite_dmg_port_arm_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Arm
hit_pts = {ke2_spike_hit_pts}
root_health_proxy = false
explosion_resistance = {ke2_spike_expl_resist}


[CollisionGroup] 
obj = starboard_engine_lod1 
separable = true 
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship 
dmg_hp = DpStarBoard_engine 
dmg_obj = ku_elite_dmg_starboard_engine_cap 
separation_explosion = explosion_small_ship_breakoff 
mass = 5.000000 
type = Starboard_Engine 
hit_pts = {ke2_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {ke2_engine_expl_resist}

[CollisionGroup] 
obj = port_engine_lod1 
separable = true 
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship 
dmg_hp = DpStarBoard_engine 
dmg_obj = ku_elite_dmg_port_engine_cap 
separation_explosion = explosion_small_ship_breakoff 
mass = 5.000000 
type = Port_Engine 
hit_pts = {ke2_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {ke2_engine_expl_resist}


[Ship]
ship_class = 8
{ship_ku_freighter}
LODranges = 0, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_Kusf
mission_property = can_use_berths
type = FREIGHTER
DA_archetype = ships\\kusari\\ku_freighter\\ku_freighter.cmp
material_library = ships\\kusari\\ku_playerships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
cockpit = cockpits\\kusari\\k_freighter.ini
pilot_mesh = generic_pilot
linear_drag = 1.000000
max_bank_angle = 1 ;15
camera_offset = 9, 45
camera_angular_acceleration = 0.035000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 20
camera_turn_look_ahead_slerp_amount = 1.000000
explosion_arch = explosion_ku
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 54000.000000, 54000.000000, 104000.000000
angular_drag = 60000.000000, 60000.000000, 60000.000000
rotation_inertia = 16800.000000, 16800.000000, 16800.000000
nudge_force = 30000.000000
bay_door_anim = Sc_open baydoor
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2

[CollisionGroup]
obj = starboard_wing_lod1
separable = true
parent_impulse = 160.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
dmg_hp = DpStarboard_Wing
dmg_obj = ku_freighter_dmg_starboard_wing_cap
type = Starboard_Fin
hit_pts = {kfr_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {kfr_wing_expl_resist}

[CollisionGroup]
obj = port_wing_lod1
separable = true
parent_impulse = 160.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
dmg_hp = DpPort_Wing
dmg_obj = ku_freighter_dmg_port_wing_cap
type = Port_Fin
hit_pts = {kfr_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {kfr_wing_expl_resist}

[CollisionGroup] 
obj = starboard_engine_lod1 
separable = true 
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship 
dmg_hp = DpStarBoard_eng
dmg_obj = ku_freighter_dmg_star_eng_cap 
separation_explosion = explosion_small_ship_breakoff 
mass = 5.000000 
type = Starboard_Engine 
hit_pts = {kfr_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {kfr_engine_expl_resist}

[CollisionGroup] 
obj = port_engine_lod1 
separable = true 
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship 
dmg_hp = DpPort_eng
dmg_obj = ku_freighter_dmg_port_eng_cap 
separation_explosion = explosion_small_ship_breakoff 
mass = 5.000000 
type = Port_Engine 
hit_pts = {kfr_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {kfr_engine_expl_resist}

[Simple]
nickname = ku_freighter_dmg_starboard_wing_cap
DA_archetype = Ships\\kusari\\ku_freighter\\ku_freighter_dmg_starboard_wing.3db
material_library = ships\\kusari\\ku_playerships.mat
mass = 5.000000
LODranges = 0, 200, 2200

[Simple]
nickname = ku_freighter_dmg_port_wing_cap
DA_archetype = Ships\\kusari\\ku_freighter\\ku_freighter_dmg_port_wing.3db
material_library = ships\\kusari\\ku_playerships.mat
mass = 5.000000
LODranges = 0, 200, 2200

[Simple]
nickname = ku_freighter_dmg_star_eng_cap
DA_archetype = Ships\\kusari\\ku_freighter\\ku_freighter_dmg_starboard_eng.3db
material_library = ships\\kusari\\ku_playerships.mat
mass = 5.000000
LODranges = 0, 200, 2200

[Simple]
nickname = ku_freighter_dmg_port_eng_cap
DA_archetype = Ships\\kusari\\ku_freighter\\ku_freighter_dmg_port_eng.3db
material_library = ships\\kusari\\ku_playerships.mat
mass = 5.000000
LODranges = 0, 200, 2200

[Ship]
ids_name = 237030
ids_info = 066601
ids_info1 = 066606
ids_info2 = 066602
ids_info3 = 066603
ship_class = 12
nickname = ku_gunboat
msg_id_prefix = gcs_refer_shiparch_Kusg
mission_property = can_use_med_moors
LODranges = 0, 10000, 20000, 30000, 40000
type = GUNBOAT
DA_archetype = ships\\kusari\\ku_gunship\\ku_gunship.cmp
material_library = ships\\kusari\\ku_capships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
linear_drag = 1.000000
mass = 1000.000000
hold_size = 5
hit_pts = 250000
explosion_arch = explosion_ku_gship
fuse = ku_gunship_body_fuse, 0.000000, 1
fuse = ku_gunship_burning_fuse01, 0.000000, 100000
fuse = ku_gunship_burning_fuse01, 0.000000, 30000
steering_torque = 60000000.000000, 60000000.000000, 60000000.000000
angular_drag = 120000000.000000, 120000000.000000, 120000000.000000
rotation_inertia = 16800000.000000, 16800000.000000, 16800000.000000
nudge_force = 150000.000000
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2
max_bank_angle = 1 ;15
camera_offset = 15, 55
camera_angular_acceleration = 0.035000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 20
camera_turn_look_ahead_slerp_amount = 1.000000
cockpit = cockpits\\kusari\\ku_gunboat.ini
nanobot_limit = 0 ; = 0 
shield_battery_limit = 0 ; = 0
hp_type = hp_turret_special_1, HpTurret_K4_03
hp_type = hp_turret_special_2, HpTurret_K4_01, HpTurret_K4_02
hp_type = hp_turret_special_5, HpTurret_K5_01

[CollisionGroup]
obj = ku_star_spike_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 500.000000
separation_explosion = explosion_ku
dmg_hp = DpSpkmnt_starboard
dmg_obj = ku_gunboat_dmg_star_spike_cap
fuse = kgb_star_spike_damage, 0.000000, 1
debris_type = cap_ship_piece
mass = 20.000000
hit_pts = 50000
root_health_proxy = false

[CollisionGroup]
obj = ku_port_spike_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 300.000000
separation_explosion = explosion_ku
dmg_hp = DpSpkMnt_Port
dmg_obj = ku_gunboat_dmg_port_spike_cap
fuse = kgb_port_spike_damage, 0.000000, 1
debris_type = cap_ship_piece
mass = 20.000000
hit_pts = 50000
root_health_proxy = false

[CollisionGroup]
obj = ku_port_wing_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 600.000000
separation_explosion = explosion_ku
dmg_hp = DpWing_port
dmg_obj = ku_gunboat_dmg_port_wing_cap
fuse = kgb_port_wing_damage, 0.000000, 1
debris_type = cap_ship_piece
mass = 20.000000
hit_pts = 100000
root_health_proxy = false

[CollisionGroup]
obj = ku_star_wing_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 500.000000
separation_explosion = explosion_ku
dmg_hp = DpWing_starboard
dmg_obj = ku_gunboat_dmg_star_wing_cap
fuse = kgb_star_wing_damage, 0.000000, 1
debris_type = cap_ship_piece
mass = 20.000000
hit_pts = 100000
root_health_proxy = false

[CollisionGroup]
obj = ku_port_eng_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 30.000000
separation_explosion = explosion_ku
dmg_hp = DpEng_port
dmg_obj = ku_gunboat_dmg_port_eng_cap
fuse = kgb_port_eng_damage, 0.000000, 1
debris_type = debris_vanish
mass = 20.000000
hit_pts = 150000
root_health_proxy = false

[CollisionGroup]
obj = ku_star_eng_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 30.000000
separation_explosion = explosion_ku
dmg_hp = DpEng_starboard
dmg_obj = ku_gunboat_dmg_star_eng_cap
fuse = kgb_star_eng_damage, 0.000000, 1
debris_type = debris_vanish
mass = 20.000000
hit_pts = 150000
root_health_proxy = false

[CollisionGroup]
obj = ku_cntrltwr_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 30.000000
debris_type = debris_vanish
separation_explosion = explosion_ku
fuse = kgb_tower_damage, 0.000000, 1
dmg_hp = DpCntrltwr
dmg_obj = ku_gunboat_dmg_tower_cap
mass = 20.000000
hit_pts = 250000
root_health_proxy = false

[CollisionGroup]
obj = ku_frnt_port_lod1
separable = true
parent_impulse = 10.000000
child_impulse = 3000.000000
debris_type = cap_ship_piece
fuse = ku_gunship_body_fuse, 0.000000, 1
group_dmg_hp = DpFrnt
group_dmg_obj = ku_gunboat_dmg_front_cap
mass = 200.000000
hit_pts = 1500000
root_health_proxy = true

[Simple]
nickname = ku_gunboat_dmg_tower_cap
DA_archetype = Ships\\kusari\\ku_gunship\\ku_gunship_dmg_cntrltwr.3db
material_library = ships\\kusari\\ku_capships.mat
mass = 1000.000000
LODranges = 0, 3000

[Simple]
nickname = ku_gunboat_dmg_port_eng_cap
DA_archetype = Ships\\kusari\\ku_gunship\\ku_gunship_dmg_eng_port.3db
material_library = ships\\kusari\\ku_capships.mat
mass = 1000.000000
LODranges = 0, 100, 3000

[Simple]
nickname = ku_gunboat_dmg_star_eng_cap
DA_archetype = Ships\\kusari\\ku_gunship\\ku_gunship_dmg_eng_starboard.3db
material_library = ships\\kusari\\ku_capships.mat
mass = 1000.000000
LODranges = 0, 100, 3000

[Simple]
nickname = ku_gunboat_dmg_front_cap
DA_archetype = Ships\\kusari\\ku_gunship\\ku_gunship_dmg_frnt.3db
material_library = ships\\kusari\\ku_capships.mat
mass = 1000.000000
LODranges = 0, 100, 3000

[Simple]
nickname = ku_gunboat_dmg_port_spike_cap
DA_archetype = Ships\\kusari\\ku_gunship\\ku_gunship_dmg_spkmnt_port.3db
material_library = ships\\kusari\\ku_capships.mat
mass = 1000.000000
LODranges = 0, 3000

[Simple]
nickname = ku_gunboat_dmg_star_spike_cap
DA_archetype = Ships\\kusari\\ku_gunship\\ku_gunship_dmg_spkmnt_starboard.3db
material_library = ships\\kusari\\ku_capships.mat
mass = 1000.000000
LODranges = 0, 3000

[Simple]
nickname = ku_gunboat_dmg_port_wing_cap
DA_archetype = Ships\\kusari\\ku_gunship\\ku_gunship_dmg_wing_port.3db
material_library = ships\\kusari\\ku_capships.mat
mass = 1000.000000
LODranges = 0, 100, 3000

[Simple]
nickname = ku_gunboat_dmg_star_wing_cap
DA_archetype = Ships\\kusari\\ku_gunship\\ku_gunship_dmg_wing_starboard.3db
material_library = ships\\kusari\\ku_capships.mat
mass = 1000.000000
LODranges = 0, 100, 3000

[Ship]
ids_name = 237026
ids_info = 66554
ship_class = 13
nickname = ku_destroyer
LODranges = 0, 1000, 5000, 10000, 25000
msg_id_prefix = gcs_refer_shiparch_Kusd
mission_property = can_use_med_moors
type = CRUISER
DA_archetype = ships\\kusari\\ku_destroyer\\ku_destroyer.cmp
material_library = ships\\kusari\\ku_capships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
linear_drag = 1.000000
mass = 5000.000000
hold_size = 5
hit_pts = 500000
explosion_arch = explosion_ku_destroyer
fuse = ku_destroyer_body_fuse, 0.000000, 1
fuse = ku_destroyer_burning_fuse01, 0.000000, 100000
fuse = ku_destroyer_burning_fuse02, 0.000000, 50000
steering_torque = 20000000.000000, 20000000.000000, 20000000.000000
angular_drag = 132000000.000000, 132000000.000000, 132000000.000000
rotation_inertia = 6600000.000000, 40000000.000000, 40000000.000000
nudge_force = 300000.000000
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 3
max_bank_angle = 20
camera_offset = 23, 80
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 10
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 5
camera_turn_look_ahead_slerp_amount = 1.000000
cockpit = cockpits\\kusari\\ku_destroyer.ini
nanobot_limit = 0 ; = 0 
shield_battery_limit = 0 ; = 0

hp_type = hp_turret_special_2, HpTurret_K2_02, HpTurret_K2_03, HpTurret_K2_01, HpTurret_K2_04, HpTurret_K2_05
hp_type = hp_turret_special_4, HpTurret_K1_01, HpTurret_K1_02

[CollisionGroup]
obj = ku_front_lod1
mass = 200.000000
separable = true
parent_impulse = 0
child_impulse = 500.000000
fuse = ku_destroyer_body_fuse, 0.000000, 1
group_dmg_hp = DpMain
group_dmg_obj = ku_destroyer_dmg_body_cap
debris_type = cap_ship_piece2
hit_pts = 5000000
root_health_proxy = true

[CollisionGroup]
obj = ku_cntrltwr_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 30.000000
separation_explosion = explosion_ku
dmg_hp = DpCntrltwr
dmg_obj = ku_destroyer_dmg_tower_cap
debris_type = debris_vanish
mass = 20.000000
hit_pts = 500000
root_health_proxy = false

[CollisionGroup]
obj = ku_eng01_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 30.000000
separation_explosion = explosion_ku
dmg_hp = DpEng01
dmg_obj = ku_destroyer_dmg_top_engine_cap
debris_type = debris_vanish
mass = 20.000000
hit_pts = 320000
root_health_proxy = false

[CollisionGroup]
obj = ku_eng02_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 30.000000
separation_explosion = explosion_ku
dmg_hp = DpEng02
dmg_obj = ku_destroyer_dmg_mid_engine_cap
debris_type = debris_vanish
mass = 20.000000
hit_pts = 350000
root_health_proxy = false

[CollisionGroup]
obj = ku_eng03_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 30.000000
separation_explosion = explosion_ku
dmg_hp = DpEng03
dmg_obj = ku_destroyer_dmg_low_engine_cap
debris_type = debris_vanish
mass = 20.000000
hit_pts = 320000
root_health_proxy = false

[Simple]
nickname = ku_destroyer_dmg_tower_cap
DA_archetype = Ships\\kusari\\ku_destroyer\\ku_destroyer_dmg_cntrltwr.3db
material_library = ships\\kusari\\ku_capships.mat
mass = 5.000000
LODranges = 0, 150, 6000

[Simple]
nickname = ku_destroyer_dmg_body_cap
DA_archetype = Ships\\kusari\\ku_destroyer\\ku_destroyer_dmg_main.3db
material_library = ships\\kusari\\ku_capships.mat
mass = 5.000000
LODranges = 0, 150, 6000

[Simple]
nickname = ku_destroyer_dmg_top_engine_cap
DA_archetype = Ships\\kusari\\ku_destroyer\\ku_destroyer_dmg_eng01.3db
material_library = ships\\kusari\\ku_capships.mat
mass = 5.000000
LODranges = 0, 150, 6000

[Simple]
nickname = ku_destroyer_dmg_mid_engine_cap
DA_archetype = Ships\\kusari\\ku_destroyer\\ku_destroyer_dmg_eng02.3db
material_library = ships\\kusari\\ku_capships.mat
mass = 5.000000
LODranges = 0, 150, 6000

[Simple]
nickname = ku_destroyer_dmg_low_engine_cap
DA_archetype = Ships\\kusari\\ku_destroyer\\ku_destroyer_dmg_eng03.3db
material_library = ships\\kusari\\ku_capships.mat
mass = 5.000000
LODranges = 0, 150, 6000

[Ship]
ids_name = 237025
ids_info = 66553
ship_class = 16
nickname = ku_battleship
LODranges = 0, 5000, 10000, 20000, 50000
msg_id_prefix = gcs_refer_shiparch_Kusb
mission_property = can_use_large_moors
type = CAPITAL
DA_archetype = ships\\kusari\\ku_battleship\\ku_battleship.cmp
material_library = ships\\kusari\\ku_capships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
linear_drag = 1.000000
mass = 100000.000000
hold_size = 10
hit_pts = 9000000
explosion_arch = explosion_ku_bship
steering_torque = 1501900032.000000, 1501900032.000000, 1501900032.000000
angular_drag = 13200000000.000000, 13200000000.000000, 13200000000.000000
rotation_inertia = 15000000512.000000, 15000000512.000000, 15000000512.000000
nudge_force = 3000000.000000
bay_doors_open_snd = hanger_doors_opening
bay_doors_close_snd = hanger_doors_closing
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
docking_sphere = berth, HpDockMountA, 2, Sc_open dock A
docking_camera = 0
fuse = ku_battleship_body_fuse, 0.500000, 1
fuse = ku_battleship_burning_fuse01, 0.500000, 5000000
fuse = ku_battleship_burning_fuse02, 0.500000, 3000000
fuse = ku_battleship_burning_fuse03, 0.500000, 1500000
fuse = ku_battleship_burning_fuse04, 0.500000, 500000
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 4
max_bank_angle = 20
camera_offset = 80, 350
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 10
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 5
camera_turn_look_ahead_slerp_amount = 1.000000
cockpit = cockpits\\kusari\\ku_battleship.ini
nanobot_limit = 0 ; = 0 
shield_battery_limit = 0 ; = 0
hp_type = hp_turret_special_3, HpTurret_K3_01, HpTurret_K3_02, HpTurret_K3_03, HpTurret_K3_04, HpTurret_K3_05, HpTurret_K3_06
hp_type = hp_turret_special_4, HpTurret_K1_01, HpTurret_K1_02, HpTurret_K1_03, HpTurret_K1_04

[CollisionGroup]
obj = ku_cntrltwr_lod1
parent_impulse = 10.000000
child_impulse = 10.000000
debris_type = debris_vanish
mass = 50.000000
separable = true
separation_explosion = explosion_ku
fuse = kbs_tower_fire, 0.500000, 1
dmg_hp = DpCntrltwr
dmg_obj = ku_battleship_dmg_tower_cap
hit_pts = 5000 ;500000
root_health_proxy = false

[CollisionGroup]
obj = Ku_nose_lod1
parent_impulse = 10.000000
child_impulse = 5000.000000
debris_type = cap_ship_piece2
mass = 200.000000
separable = true
fuse = ku_battleship_body_fuse, 0.000000, 1
group_dmg_obj = ku_battleship_dmg_nose_cap
group_dmg_hp = DpNose
hit_pts = 15000000
root_health_proxy = true

[CollisionGroup]
obj = ku_front_lod1
parent_impulse = 10.000000
child_impulse = 10.000000
debris_type = debris_vanish
mass = 80.000000
separable = true
fuse = ku_battleship_body_fuse, 0.250000, 1
dmg_obj = ku_battleship_dmg_front_cap
dmg_hp = DpFront
hit_pts = 15000000
root_health_proxy = true

[CollisionGroup]
obj = Ku_rear_lod1
parent_impulse = 10.000000
child_impulse = 10.000000
debris_type = debris_vanish
mass = 80.000000
separable = true
fuse = ku_battleship_body_fuse, 0.750100, 1
dmg_obj = ku_battleship_dmg_rear_cap
dmg_hp = DpRear
hit_pts = 15000000
root_health_proxy = true

[CollisionGroup]
obj = Ku_engine_lod1
parent_impulse = 10.000000
child_impulse = 5000.000000
debris_type = cap_ship_piece2
mass = 200.000000
separable = true
fuse = ku_battleship_body_fuse, 0.900000, 1
dmg_obj = ku_battleship_dmg_front_cap
dmg_hp = DpEngine
hit_pts = 15000000
root_health_proxy = true

[CollisionGroup]
obj = Ku_port_engine01_lod1
separable = true
parent_impulse = 600.000000
child_impulse = 300.000000
debris_type = debris_vanish
mass = 3.000000
fuse = kbs_pe01_fire, 0.500000, 1
dmg_obj = ku_battleship_dmg_port_engine01_cap
separation_explosion = explosion_ku
dmg_hp = DpPortengine01
hit_pts = 5000 ;350000
root_health_proxy = false

[CollisionGroup]
obj = Ku_port_engine02_lod1
dmg_obj = ku_battleship_dmg_port_engine01_cap
dmg_hp = DpPortengine02
separable = true
parent_impulse = 600.000000
child_impulse = 300.000000
debris_type = debris_vanish
mass = 3.000000
fuse = kbs_pe02_fire, 0.500000, 1
separation_explosion = explosion_ku
hit_pts = 5000 ;350000
root_health_proxy = false

[CollisionGroup]
obj = Ku_port_fan_lod1
separable = true
parent_impulse = 600.000000
child_impulse = 80.000000
debris_type = cap_ship_piece
mass = 3.000000
fuse = kbs_pwing_fire, 0.500000, 1
separation_explosion = explosion_ku
hit_pts = 100000
root_health_proxy = false

[CollisionGroup]
obj = Ku_port_spikemount_lod1
separable = true
parent_impulse = 600.000000
child_impulse = 150.000000
debris_type = cap_ship_piece
mass = 4.000000
fuse = kbs_parm_fire, 0.500000, 1
separation_explosion = explosion_ku
hit_pts = 100000
root_health_proxy = false

[CollisionGroup]
obj = Ku_star_engine01_lod1
separable = true
parent_impulse = 600.000000
child_impulse = 100.000000
debris_type = cap_ship_piece
mass = 3.000000
fuse = kbs_se01_fire, 0.500000, 1
dmg_obj = ku_battleship_dmg_starboard_engine01_cap
dmg_hp = DpStarboardengine01
separation_explosion = explosion_ku
hit_pts = 5000 ;350000
root_health_proxy = true

[CollisionGroup]
obj = Ku_star_engine02_lod1
separable = true
parent_impulse = 600.000000
child_impulse = 100.000000
debris_type = cap_ship_piece
mass = 3.000000
fuse = kbs_se02_fire, 0.500000, 1
dmg_obj = ku_battleship_dmg_starboard_engine02_cap
dmg_hp = DpStarboardengine02
separation_explosion = explosion_ku
hit_pts = 5000 ;350000
root_health_proxy = true

[CollisionGroup]
obj = Ku_star_fan_lod1
separable = true
parent_impulse = 600.000000
child_impulse = 100.000000
debris_type = cap_ship_piece
fuse = kbs_swing_fire, 0.500000, 1
separation_explosion = explosion_ku
mass = 2.000000
hit_pts = 50000
root_health_proxy = true

[CollisionGroup]
obj = Ku_star_spikemount_lod1
separable = true
parent_impulse = 600.000000
child_impulse = 150.000000
debris_type = cap_ship_piece
fuse = kbs_sarm_fire, 0.500000, 1
separation_explosion = explosion_ku
mass = 4.000000
hit_pts = 100000
root_health_proxy = true

[Simple]
nickname = ku_battleship_dmg_tower_cap
DA_archetype = Ships\\kusari\\ku_battleship\\ku_battleship_dmg_cntrltwr.3db
material_library = ships\\kusari\\ku_capships.mat
mass = 1000.000000
LODranges = 0, 900, 20000

[Simple]
nickname = ku_battleship_dmg_nose_cap
DA_archetype = Ships\\kusari\\ku_battleship\\ku_battleship_dmg_frnt.3db
material_library = ships\\kusari\\ku_capships.mat
mass = 1000.000000
LODranges = 0, 900, 20000

[Simple]
nickname = ku_battleship_dmg_front_cap
DA_archetype = Ships\\kusari\\ku_battleship\\ku_battleship_dmg_mid.3db
material_library = ships\\kusari\\ku_capships.mat
mass = 1000.000000
LODranges = 0, 900, 20000

[Simple]
nickname = ku_battleship_dmg_rear_cap
DA_archetype = Ships\\kusari\\ku_battleship\\ku_battleship_dmg_mid2.3db
material_library = ships\\kusari\\ku_capships.mat
mass = 1000.000000
LODranges = 0, 900, 20000

[Simple]
nickname = ku_battleship_dmg_engine_cap
DA_archetype = Ships\\kusari\\ku_battleship\\ku_battleship_dmg_rear.3db
material_library = ships\\kusari\\ku_capships.mat
mass = 1000.000000
LODranges = 0, 900, 20000

[Simple]
nickname = ku_battleship_dmg_port_engine01_cap
DA_archetype = Ships\\kusari\\ku_battleship\\ku_battleship_dmg_port_eng1.3db
material_library = ships\\kusari\\ku_capships.mat
mass = 1000.000000
LODranges = 0, 900, 20000

[Simple]
nickname = ku_battleship_dmg_starboard_engine01_cap
DA_archetype = Ships\\kusari\\ku_battleship\\ku_battleship_dmg_starboard_eng1.3db
material_library = ships\\kusari\\ku_capships.mat
mass = 1000.000000
LODranges = 0, 900, 20000

[Simple]
nickname = ku_battleship_dmg_starboard_engine02_cap
DA_archetype = Ships\\kusari\\ku_battleship\\ku_battleship_dmg_starboard_eng2.3db
material_library = ships\\kusari\\ku_capships.mat
mass = 1000.000000
LODranges = 0, 900, 20000

[Ship]
ship_class = 4
{ship_rh_fighter}
LODranges = 0, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_Rhelf
mission_property = can_use_berths
type = FIGHTER
DA_archetype = ships\\rheinland\\rh_fighter\\rh_fighter.cmp
material_library = ships\\rheinland\\rh_playerships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
cockpit = cockpits\\rheinland\\r_fighter.ini
pilot_mesh = generic_pilot
linear_drag = 1.000000
max_bank_angle = 5 ;35
camera_offset = 11, 34
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 23
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 30
camera_turn_look_ahead_slerp_amount = 1.000000
explosion_arch = explosion_rh
steering_torque = 18000.000000, 18000.000000, 58000.000000
angular_drag = 15000.000000, 15000.000000, 35000.000000
rotation_inertia = 2800.000000, 2800.000000, 1000.000000
nudge_force = 60000.000000
bay_door_anim = Sc_open baydoor
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 1

[CollisionGroup]
obj = port_wing_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 30.000000
debris_type = debris_small_ship
dmg_hp = DpPort_Wing
dmg_obj = rh_fighter_dmg_port_wing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Wing
hit_pts = {rf_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {rf_wing_expl_resist}

[CollisionGroup]
obj = starboard_wing_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 30.000000
debris_type = debris_small_ship
dmg_hp = DpStarboard_Wing
dmg_obj = rh_fighter_dmg_starboard_wing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Wing
hit_pts = {rf_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {rf_wing_expl_resist}

[CollisionGroup] 
obj = engine_lod1 
separable = true 
parent_impulse = 250.000000 
child_impulse = 7.000000 
debris_type = debris_small_ship 
dmg_hp = DpEngine 
dmg_obj = rh_fighter_dmg_engine_cap
separation_explosion = explosion_small_ship_breakoff 
mass = 5.000000 
type = Engine 
hit_pts = {rf_engine_hit_pts} 
root_health_proxy = false
explosion_resistance = {rf_engine_expl_resist}


[Simple]
nickname = rh_fighter_dmg_port_wing_cap
DA_archetype = ships\\rheinland\\rh_fighter\\rh_fighter_dmg_port_wing.3db
material_library = ships\\rheinland\\rh_playerships.mat
mass = 5.000000
LODranges = 0, 1000, 2000

[Simple]
nickname = rh_fighter_dmg_starboard_wing_cap
DA_archetype = ships\\rheinland\\rh_fighter\\rh_fighter_dmg_starboard_wing.3db
material_library = ships\\rheinland\\rh_playerships.mat
mass = 5.000000
LODranges = 0, 1000, 2000

[Simple] 
nickname = rh_fighter_dmg_engine_cap
DA_archetype = ships\\rheinland\\rh_fighter\\rh_fighter_dmg_engine.3db 
material_library = ships\\RHEINLAND\\rh_playerships.mat
mass = 5.000000
LODranges = 0, 1000, 2000 

;RH_SHIP
[Ship]
ship_class = 5
{ship_rh_elite}
LODranges = 0, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_Rhehf
mission_property = can_use_berths
type = FIGHTER
DA_archetype = ships\\rheinland\\rh_elite\\rh_elite.cmp
material_library = ships\\rheinland\\rh_playerships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship03
cockpit = cockpits\\rheinland\\r_elite.ini
pilot_mesh = generic_pilot
linear_drag = 1.000000
max_bank_angle = 2 ;30
camera_offset = 10, 42
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 17
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 25
camera_turn_look_ahead_slerp_amount = 1.000000
explosion_arch = explosion_rh
steering_torque = 43000.000000, 43000.000000, 230000.000000
angular_drag = 41000.000000, 41000.000000, 141000.000000
rotation_inertia = 8400.000000, 8400.000000, 8400.000000
nudge_force = 60000.000000
bay_door_anim = Sc_open baydoor
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
num_exhaust_nozzles = 2

[CollisionGroup]
obj = Rh_port_wing_lod1
separable = true
parent_impulse = 90.000000
child_impulse = 20.000000
debris_type = debris_small_ship
dmg_hp = DpPort_Wing
dmg_obj = rh_elite_dmg_port_wing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Wing
hit_pts = {re_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {re_wing_expl_resist}

[CollisionGroup]
obj = Rh_starboard_wing_lod1
separable = true
parent_impulse = 90.000000
child_impulse = 20.000000
debris_type = debris_small_ship
dmg_hp = DpStarboard_Wing
dmg_obj = rh_elite_dmg_starboard_wing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Wing
hit_pts = {re_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {re_wing_expl_resist}

[CollisionGroup]
obj = Rh_tail_lod1
separable = true
parent_impulse = 90.000000
child_impulse = 20.000000
debris_type = debris_small_ship
dmg_hp = DpTail
dmg_obj = rh_elite_dmg_tail_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Tail
hit_pts = {re_tail_hit_pts}
root_health_proxy = false
explosion_resistance = {re_tail_expl_resist}

[CollisionGroup] 
obj = rh_port_engine_lod1
separable = true 
parent_impulse = 250.000000 
child_impulse = 20.000000 
debris_type = debris_small_ship
dmg_hp = DpPort_Engine 
dmg_obj = rh_elite_dmg_portengine_cap
separation_explosion = explosion_small_ship_breakoff 
mass = 5.000000 
type = Port_Engine 
hit_pts = {re_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {re_engine_expl_resist}

[CollisionGroup] 
obj = rh_starboard_engine_lod1
separable = true 
parent_impulse = 250.000000 
child_impulse = 20.000000 
debris_type = debris_small_ship 
dmg_hp = DpStarBoard_engine 
dmg_obj = rh_elite_dmg_starengine_cap 
separation_explosion = explosion_small_ship_breakoff 
mass = 5.000000 
type = Starboard_Engine 
hit_pts = {re_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {re_engine_expl_resist}

[Simple]
nickname = rh_elite_dmg_port_wing_cap
DA_archetype = ships\\rheinland\\rh_elite\\rh_elite_dmg_port_wing.3db
material_library = ships\\rheinland\\rh_playerships.mat
mass = 5.000000
LODranges = 0, 1000, 2000

[Simple]
nickname = rh_elite_dmg_starboard_wing_cap
DA_archetype = ships\\rheinland\\rh_elite\\rh_elite_dmg_starboard_wing.3db
material_library = ships\\rheinland\\rh_playerships.mat
mass = 5.000000
LODranges = 0, 1000, 2000

[Simple]
nickname = rh_elite_dmg_tail_cap
DA_archetype = ships\\rheinland\\rh_elite\\rh_elite_dmg_tail.3db
material_library = ships\\rheinland\\rh_playerships.mat
mass = 5.000000
LODranges = 0, 1000, 2000

[Simple] 
nickname = rh_elite_dmg_portengine_cap
DA_archetype = ships\\RHEINLAND\\RH_ELITE\\rh_elite_dmg_port_engine.3db 
material_library = ships\\RHEINLAND\\rh_playerships.mat
mass = 5.000000
LODranges = 0, 1000, 2000 

[Simple] 
nickname = rh_elite_dmg_starengine_cap 
DA_archetype = ships\\rheinland\\rh_elite\\rh_elite_dmg_starboard_engine.3db 
material_library = ships\\rheinland\\rh_playerships.mat 
mass = 5.000000 
LODranges = 0, 1000, 2000

[Ship]
ship_class = 6
{ship_rh_elite2}
LODranges = 0, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_Rhehf
mission_property = can_use_berths
type = FIGHTER
DA_archetype = ships\\rheinland\\rh_elite\\rh_elite.cmp 
material_library = ships\\rheinland\\rh_playerships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapjunker
cockpit = cockpits\\rheinland\\r_elite.ini
linear_drag = 1
max_bank_angle = 2 ;30
camera_offset = 10, 42
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 17
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 25
camera_turn_look_ahead_slerp_amount = 1.000000
explosion_arch = explosion_rh
steering_torque = 43000.000000, 43000.000000, 230000.000000
angular_drag = 41000.000000, 41000.000000, 141000.000000
rotation_inertia = 8400.000000, 8400.000000, 8400.000000
nudge_force = 10000.000000
bay_door_anim = Sc_open baydoor
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2

[CollisionGroup]
obj = Rh_port_wing_lod1
separable = true
parent_impulse = 90.000000
child_impulse = 20.000000
debris_type = debris_small_ship
dmg_hp = DpPort_Wing
dmg_obj = rh_elite_dmg_port_wing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Wing
hit_pts = {re2_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {re2_wing_expl_resist}

[CollisionGroup]
obj = Rh_starboard_wing_lod1
separable = true
parent_impulse = 90.000000
child_impulse = 20.000000
debris_type = debris_small_ship
dmg_hp = DpStarboard_Wing
dmg_obj = rh_elite_dmg_starboard_wing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Wing
hit_pts = {re2_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {re2_wing_expl_resist}

[CollisionGroup]
obj = Rh_tail_lod1
separable = true
parent_impulse = 90.000000
child_impulse = 20.000000
debris_type = debris_small_ship
dmg_hp = DpTail
dmg_obj = rh_elite_dmg_tail_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Tail
hit_pts = {re2_tail_hit_pts}
root_health_proxy = false
explosion_resistance = {re2_tail_expl_resist}

[CollisionGroup] 
obj = rh_port_engine_lod1
separable = true 
parent_impulse = 250.000000 
child_impulse = 20.000000 
debris_type = debris_small_ship
dmg_hp = DpPort_Engine 
dmg_obj = rh_elite_dmg_portengine_cap
separation_explosion = explosion_small_ship_breakoff 
mass = 5.000000 
type = Port_Engine 
hit_pts = {re2_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {re2_engine_expl_resist}

[CollisionGroup] 
obj = rh_starboard_engine_lod1
separable = true 
parent_impulse = 250.000000 
child_impulse = 20.000000 
debris_type = debris_small_ship 
dmg_hp = DpStarBoard_engine 
dmg_obj = rh_elite_dmg_starengine_cap 
separation_explosion = explosion_small_ship_breakoff 
mass = 5.000000 
type = Starboard_Engine 
hit_pts = {re2_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {re2_engine_expl_resist}


;RH_SHIP
[Ship]
ship_class = 8
{ship_rh_freighter}
LODranges = 0, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_Rhef
mission_property = can_use_berths
type = FIGHTER
DA_archetype = ships\\rheinland\\rh_freighter\\rh_freighter.cmp
material_library = ships\\rheinland\\rh_playerships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
cockpit = cockpits\\rheinland\\r_freighter.ini
pilot_mesh = generic_pilot
linear_drag = 1.000000
max_bank_angle = 1 ;15
camera_offset = 13, 52
camera_angular_acceleration = 0.025000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 20
camera_turn_look_ahead_slerp_amount = 1.000000
explosion_arch = explosion_rh
steering_torque = 48000.000000, 48000.000000, 104000.000000
angular_drag = 60000.000000, 60000.000000, 60000.000000
rotation_inertia = 16800.000000, 16800.000000, 16800.000000
nudge_force = 100000.000000
bay_door_anim = Sc_rh_freighter
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2

[CollisionGroup]
obj = rh_port_side_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 11.000000
debris_type = debris_small_ship
dmg_hp = DpPort_side panel
dmg_obj = rh_freighter_dmg_port_side_panel_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Side_Panel
hit_pts = {rfr_panel_hit_pts}
root_health_proxy = false
explosion_resistance = {rfr_panel_expl_resist}

[CollisionGroup]
obj = rh_star_side_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 11.000000
debris_type = debris_small_ship
dmg_hp = DpStarboard_side panel
dmg_obj = rh_freighter_dmg_starboard_side_panel_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Side_Panel
hit_pts = {rfr_panel_hit_pts}
root_health_proxy = false
explosion_resistance = {rfr_panel_expl_resist}

[CollisionGroup] 
obj = port_engine_lod1 
separable = true 
parent_impulse = 250.000000 
child_impulse = 7.000000 
debris_type = debris_small_ship 
dmg_hp = DpPort_Engine 
dmg_obj = rh_freighter_dmg_portengine_cap
separation_explosion = explosion_small_ship_breakoff 
mass = 5.000000 
type = Port_Engine 
hit_pts = {rfr_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {rfr_engine_expl_resist}

[CollisionGroup] 
obj = starboard_engine_lod1 
separable = true 
parent_impulse = 250.000000 
child_impulse = 7.000000 
debris_type = debris_small_ship 
dmg_hp = DpStarBoard_engine 
dmg_obj = rh_freighter_dmg_starengine_cap 
separation_explosion = explosion_small_ship_breakoff 
mass = 5.000000 
type = StarBoard_Engine 
hit_pts = {rfr_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {rfr_engine_expl_resist}

[Simple]
nickname = rh_freighter_dmg_port_side_panel_cap
DA_archetype = ships\\rheinland\\rh_freighter\\rh_freighter_dmg_port_side_panel.3db
material_library = ships\\rheinland\\rh_playerships.mat
mass = 5.000000
LODranges = 0, 1000, 2000

[Simple]
nickname = rh_freighter_dmg_starboard_side_panel_cap
DA_archetype = ships\\rheinland\\rh_freighter\\rh_freighter_dmg_starboard_side_panel.3db
material_library = ships\\rheinland\\rh_playerships.mat
mass = 5.000000
LODranges = 0, 1000, 2000

[Simple] 
nickname = rh_freighter_dmg_portengine_cap
DA_archetype = ships\\RHEINLAND\\rh_freighter\\rh_freighter_dmg_port_engine.3db 
material_library = ships\\RHEINLAND\\rh_playerships.mat
mass = 5.000000
LODranges = 0, 1000, 2000 

[Simple] 
nickname = rh_freighter_dmg_starengine_cap 
DA_archetype = ships\\rheinland\\rh_freighter\\rh_freighter_dmg_starboard_engine.3db
material_library = ships\\rheinland\\rh_playerships.mat 
mass = 5.000000 
LODranges = 0, 1000, 2000

[Ship]
ids_name = 237054
ids_info = 066601
ids_info1 = 066604
ids_info2 = 066602
ids_info3 = 066603
nickname = rh_gunboat
LODranges = 0, 1000, 5000, 10000, 20000
msg_id_prefix = gcs_refer_shiparch_Rheg
mission_property = can_use_med_moors
type = GUNBOAT
ship_class = 12
DA_archetype = ships\\rheinland\\rh_gunship\\rh_gunship.cmp
material_library = ships\\rheinland\\rh_capships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
mass = 2500.000000
hold_size = 5
hit_pts = 250000
fuse = rh_gunship_body_fuse, 0.000000, 1
fuse = rh_gunship_burning_fuse01, 0.000000, 100000
fuse = rh_gunship_burning_fuse02, 0.000000, 30000
explosion_arch = explosion_rh_gship
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 300, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 600, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
linear_drag = 1.000000
; steering_torque = 60000000.000000, 60000000.000000, 60000000.000000
; angular_drag = 120000000.000000, 120000000.000000, 120000000.000000
; rotation_inertia = 3000000.000000, 16800000.000000, 16800000.000000
steering_torque = 60000000.000000, 60000000.000000, 60000000.000000
angular_drag = 120000000.000000, 120000000.000000, 120000000.000000
rotation_inertia = 16800000.000000, 16800000.000000, 16800000.000000
nudge_force = 60000.000000
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 1
camera_offset = 40, 100
camera_angular_acceleration = 0.035000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 20
camera_turn_look_ahead_slerp_amount = 1.000000
cockpit = cockpits\\rheinland\\r_gunboat.ini
nanobot_limit = 0 ; = 0
shield_battery_limit = 0 ; = 0

shield_link = r_fighter_shield01, HpMount, HpShield01
;;;hp_type = hp_freighter_shield_special_3, HpShield01

hp_type = hp_turret_special_1, HpTurret_R4_05
hp_type = hp_turret_special_2, HpTurret_R4_03, HpTurret_R4_04
hp_type = hp_turret_special_5, HpTurret_R3_01

[CollisionGroup]
obj = Rh_front_lod1
separable = true
parent_impulse = 0
child_impulse = 500.000000
debris_type = cap_ship_piece2
mass = 200.000000
group_dmg_hp = DpFront
group_dmg_obj = rh_gunship_dmg_front_cap
fuse = rh_gunship_body_fuse, 0.000000, 1
hit_pts = 1500000
root_health_proxy = true

[CollisionGroup]
obj = engine_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 11.000000
debris_type = debris_vanish
dmg_hp = DpEngine
dmg_obj = rh_gunship_dmg_engine_cap
mass = 5.000000
fuse = rgb_engine_damage, 0.000000, 1
hit_pts = 300000
root_health_proxy = false

[CollisionGroup]
obj = Rh_cntrltwr_lod1
separable = true
parent_impulse = 0
child_impulse = 30.000000
debris_type = debris_vanish
dmg_hp = DpCntrltwr
dmg_obj = rh_gunship_dmg_tower_cap
mass = 200.000000
fuse = rgb_tower_damage, 0.000000, 1
hit_pts = 100000
root_health_proxy = false

[Simple]
nickname = rh_gunship_dmg_tower_cap
DA_archetype = Ships\\rheinland\\rh_gunship\\rh_dmg_cntrltwr.3db
material_library = ships\\rheinland\\rh_capships.mat
mass = 5.000000
LODranges = 0, 4000

[Simple]
nickname = rh_gunship_dmg_front_cap
DA_archetype = Ships\\rheinland\\rh_gunship\\rh_dmg_frnt.3db
material_library = ships\\rheinland\\rh_capships.mat
mass = 5.000000
LODranges = 0, 150, 4000

[Simple]
nickname = rh_gunship_dmg_engine_cap
DA_archetype = ships\\rheinland\\rh_gunship\\rh_dmg_engine.3db
material_library = ships\\rheinland\\rh_capships.mat
mass = 5.000000
LODranges = 0, 150, 4000

[Ship]
ids_name = 237050
ids_info = 66597
ship_class = 14
nickname = rh_cruiser
LODranges = 0, 5000, 10000, 20000, 25000
msg_id_prefix = gcs_refer_shiparch_Rhed
mission_property = can_use_med_moors
type = CRUISER
DA_archetype = ships\\rheinland\\rh_cruiser\\rh_cruiser.cmp
material_library = ships\\rheinland\\rh_capships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
linear_drag = 1.000000
mass = 10000.000000
hold_size = 2
explosion_arch = explosion_rh_cruiser
fuse = rh_cruiser_body_fuse, 0.000000, 1
fuse = rh_cruiser_burning_fuse01, 0.000000, 100000
fuse = rh_cruiser_burning_fuse02, 0.000000, 50000
; steering_torque = 20000000.000000, 20000000.000000, 20000000.000000
; angular_drag = 132000000.000000, 132000000.000000, 132000000.000000
; rotation_inertia = 1300000.000000, 40000000.000000, 40000000.000000
steering_torque = 20000000.000000, 20000000.000000, 20000000.000000
angular_drag = 132000000.000000, 132000000.000000, 132000000.000000
rotation_inertia = 40000000.000000, 40000000.000000, 40000000.000000
hit_pts = 500000
nudge_force = 300000.000000
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 1
camera_offset = 40, 150
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 20
camera_turn_look_ahead_slerp_amount = 1.000000
cockpit = cockpits\\rheinland\\r_cruiser.ini
nanobot_limit = 0 ; = 0
shield_battery_limit = 0 ; = 0

hp_type = hp_turret_special_3, HpTurret_R2_01, HpTurret_R2_02, HpTurret_R2_03, HpTurret_R2_04, HpTurret_R2_06
hp_type = hp_turret_special_4, HpTurret_R1_01

surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 300, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 600, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03

[CollisionGroup]
obj = Rh_front_lod1
separable = true
parent_impulse = 10.000000
child_impulse = 5000.000000
debris_type = cap_ship_piece2
;fuse = rh_cruiser_body_fuse, 0.000000, 1
;fuse = rh_cruiser_burning_fuse01, 0.000000, 10825
group_dmg_hp = DpFront
group_dmg_obj = rh_cruiser_dmg_front_cap
mass = 500.000000
hit_pts = 5000000
root_health_proxy = true

[CollisionGroup]
obj = Rh_cntrltwr_lod1
separable = true
parent_impulse = 90.000000
child_impulse = 60.000000
debris_type = cap_ship_piece2
separation_explosion = explosion_rh
fuse = rcr_tower_damage, 0.000000, 1
dmg_hp = DpCntrltwr
dmg_obj = rh_cruiser_dmg_control_tower_cap
hit_pts = 500000
root_health_proxy = false

[CollisionGroup]
obj = engine_lod1
separable = true
parent_impulse = 90.000000
child_impulse = 60.000000
debris_type = cap_ship_piece2
separation_explosion = explosion_rh
fuse = rcr_engine_damage, 0.000000, 1
dmg_hp = DpEngine
dmg_obj = rh_cruiser_dmg_engine_cap
hit_pts = 1000000
root_health_proxy = false

[CollisionGroup]
obj = Rh_starboard_tower_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 30.000000
debris_type = cap_ship_piece2
separation_explosion = explosion_rh
fuse = rcr_star_tower_damage, 0.000000, 1
dmg_hp = DpStarboard tower
dmg_obj = rh_cruiser_dmg_starboard_tower_cap
hit_pts = 500000
root_health_proxy = false

[CollisionGroup]
obj = Rh_port_tower_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 30.000000
;debris_type = cap_ship_piece2
debris_type = debris_small_ship
separation_explosion = explosion_rh
fuse = rcr_port_tower_damage, 0.000000, 1
dmg_hp = DPPort tower
dmg_obj = rh_cruiser_dmg_port_tower_cap
hit_pts = 500000
root_health_proxy = false

[Simple]
nickname = rh_cruiser_dmg_control_tower_cap
DA_archetype = Ships\\rheinland\\rh_cruiser\\rh_cruiser_dmg_cntrltwr.3db
material_library = ships\\rheinland\\rh_capships.mat
mass = 5.000000
LODranges = 0, 6000

[Simple]
nickname = rh_cruiser_dmg_front_cap
DA_archetype = Ships\\rheinland\\rh_cruiser\\rh_cruiser_dmg_frnt.3db
material_library = ships\\rheinland\\rh_capships.mat
mass = 5.000000
LODranges = 0, 200, 6000

[Simple]
nickname = rh_cruiser_dmg_engine_cap
DA_archetype = Ships\\rheinland\\rh_cruiser\\rh_cruiser_dmg_engine.3db
material_library = ships\\rheinland\\rh_capships.mat
mass = 5.000000
LODranges = 0, 200, 6000

[Simple]
nickname = rh_cruiser_dmg_port_tower_cap
DA_archetype = Ships\\rheinland\\rh_cruiser\\rh_cruiser_dmg_port_tower.3db
material_library = ships\\rheinland\\rh_capships.mat
mass = 5.000000
LODranges = 0, 200, 6000

[Simple]
nickname = rh_cruiser_dmg_starboard_tower_cap
DA_archetype = Ships\\rheinland\\rh_cruiser\\rh_cruiser_dmg_starboard_tower.3db
material_library = ships\\rheinland\\rh_capships.mat
mass = 5.000000
LODranges = 0, 200, 6000

[Ship]
ids_name = 237049
ids_info = 66596
ship_class = 16
nickname = rh_battleship
LODranges = 0, 10000, 20000, 30000, 40000, 50000
msg_id_prefix = gcs_refer_shiparch_Rheb
mission_property = can_use_large_moors
type = CAPITAL
DA_archetype = ships\\rheinland\\rh_battleship\\rh_battleship.cmp
material_library = ships\\rheinland\\rh_capships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
hold_size = 2
hit_pts = 9000000
fuse = r_battleship_body_fuse, 0.500000, 1
fuse = rh_battleship_burning_fuse02, 0.000000, 17325
explosion_arch = explosion_rh_bship
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
linear_drag = 1.000000
mass = 100000.000000
steering_torque = 1501900032.000000, 1501900032.000000, 1501900032.000000
angular_drag = 13200000000.000000, 13200000000.000000, 13200000000.000000
rotation_inertia = 15000000512.000000, 15000000512.000000, 15000000512.000000
nudge_force = 3000000.000000
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
docking_sphere = berth, HpDockMountA, 2, Sc_open dock A
docking_camera = 0
bay_door_anim = Sc_open dock A
bay_doors_open_snd = hanger_doors_opening
bay_doors_close_snd = hanger_doors_closing
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 1
camera_offset = 60, 200
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 20
camera_turn_look_ahead_slerp_amount = 1.000000
cockpit = cockpits\\rheinland\\r_battleship.ini
nanobot_limit = 0 ; = 0
shield_battery_limit = 0 ; = 0

shield_link = r_fighter_shield01, HpMount, HpShield01, HpShield02
hp_type = hp_freighter_shield_special_2, HpShield01, HpShield02

hp_type = hp_turret_special_3, HpTurret_R2_01, HpTurret_R2_02, HpTurret_R2_03, HpTurret_R2_04, HpTurret_R1_05
hp_type = hp_turret_special_4, HpTurret_R1_01, HpTurret_R1_02, HpTurret_R1_03, HpTurret_R1_04

[CollisionGroup]
obj = Rh_frnt_lod1
separable = true
parent_impulse = 0
child_impulse = 5000.000000
debris_type = cap_ship_piece2
mass = 200.000000
fuse = r_battleship_body_fuse, 0.000000, 1
group_dmg_hp = DpFrnt
group_dmg_obj = rh_battleship_head_dmg_cap
hit_pts = 20000000
root_health_proxy = true

[CollisionGroup]
obj = Rh_cntrl_twr_lod1
separable = true
parent_impulse = 0
child_impulse = 30.000000
debris_type = debris_vanish
mass = 200.000000
fuse = rbs_tower_damage, 0.000000, 1
dmg_hp = DpCntrltwr
dmg_obj = rh_battleship_control_tower_dmg_cap
hit_pts = 500000
root_health_proxy = false

[CollisionGroup]
obj = Rh_thruster_lod1
separable = true
parent_impulse = 0
child_impulse = 5000.000000
debris_type = cap_ship_piece
mass = 200.000000
fuse = r_battleship_body_fuse, 1.000000, 1
group_dmg_hp = DpReactor
group_dmg_obj = rh_battleship_tail_dmg_cap
hit_pts = 20000000
root_health_proxy = false

[CollisionGroup]
obj = Rh_engine_lod1
separable = true
parent_impulse = 0
child_impulse = 30.000000
debris_type = debris_vanish
mass = 200.000000
fuse = rbs_engine_damage, 1.000000, 1
dmg_hp = DpThruster
dmg_obj = rh_battleship_engine_dmg_cap
hit_pts = 1000000
root_health_proxy = false

[CollisionGroup]
obj = Rh_star_shield_lod1
separable = true
parent_impulse = 0
child_impulse = 30.000000
debris_type = debris_vanish
mass = 200.000000
fuse = rbs_star_shield_damage, 0.000000, 1
dmg_hp = DpStarboard_shield
dmg_obj = rh_battleship_starboard_shield_dmg_cap
hit_pts = 250000
root_health_proxy = false

[CollisionGroup]
obj = Rh_port_shield_lod1
separable = true
parent_impulse = 0
child_impulse = 30.000000
debris_type = debris_vanish
mass = 200.000000
fuse = rbs_port_shield_damage, 0.000000, 1
dmg_hp = DpPort_shield
dmg_obj = rh_battleship_port_shield_dmg_cap
hit_pts = 250000
root_health_proxy = false

[CollisionGroup]
obj = Rh_main_lod1
separable = true
parent_impulse = 0
child_impulse = 30.000000
debris_type = debris_vanish
mass = 200.000000
fuse = r_battleship_body_fuse, 0.750000, 1
dmg_hp = DpMain
dmg_obj = rh_battleship_butt_dmg_cap
hit_pts = 20000000
root_health_proxy = true

[CollisionGroup]
obj = Rh_midfrnt_lod1
separable = true
parent_impulse = 0
child_impulse = 30.000000
debris_type = debris_vanish
mass = 200.000000
fuse = r_battleship_body_fuse, 0.400000, 1
dmg_hp = DpMidfrnt
dmg_obj = rh_battleship_neck_dmg_cap
hit_pts = 20000000
root_health_proxy = true

[Simple]
nickname = rh_battleship_control_tower_dmg_cap
DA_archetype = Ships\\rheinland\\rh_battleship\\rh_battleship_dmg_cntrltwr.3db
material_library = ships\\rheinland\\rh_capships.mat
mass = 1000.000000
LODranges = 0, 9000, 20000

[Simple]
nickname = rh_battleship_head_dmg_cap
DA_archetype = Ships\\rheinland\\rh_battleship\\rh_battleship_dmg_frnt.3db
material_library = ships\\rheinland\\rh_capships.mat
mass = 1000.000000
LODranges = 0, 9000, 20000

[Simple]
nickname = rh_battleship_neck_dmg_cap
DA_archetype = Ships\\rheinland\\rh_battleship\\rh_battleship_dmg_midfrnt.3db
material_library = ships\\rheinland\\rh_capships.mat
mass = 1000.000000
LODranges = 0, 9000, 20000

[Simple]
nickname = rh_battleship_butt_dmg_cap
DA_archetype = Ships\\rheinland\\rh_battleship\\rh_battleship_dmg_main.3db
material_library = ships\\rheinland\\rh_capships.mat
mass = 1000.000000
LODranges = 0, 9000, 20000

[Simple]
nickname = rh_battleship_tail_dmg_cap
DA_archetype = Ships\\rheinland\\rh_battleship\\rh_battleship_dmg_reactor.3db
material_library = ships\\rheinland\\rh_capships.mat
mass = 1000.000000
LODranges = 0, 9000, 20000

[Simple]
nickname = rh_battleship_engine_dmg_cap
DA_archetype = Ships\\rheinland\\rh_battleship\\rh_battleship_dmg_thruster.3db
material_library = ships\\rheinland\\rh_capships.mat
mass = 1000.000000
LODranges = 0, 9000, 20000

[Simple]
nickname = rh_battleship_port_shield_dmg_cap
DA_archetype = Ships\\rheinland\\rh_battleship\\rh_battleship_dmg_port_shield2.3db
material_library = ships\\rheinland\\rh_capships.mat
mass = 1000.000000
LODranges = 0, 9000, 20000

[Simple]
nickname = rh_battleship_starboard_shield_dmg_cap
DA_archetype = Ships\\rheinland\\rh_battleship\\rh_battleship_dmg_starboard_shield2.3db
material_library = ships\\rheinland\\rh_capships.mat
mass = 1000.000000
LODranges = 0, 9000, 20000

[Ship]
ship_class = 0
{ship_bh_fighter}
LODranges = 0, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_lfighter
mission_property = can_use_berths
type = FIGHTER
linear_drag = 1.000000
fuse = intermed_damage_smallship02, 0.000000, 1000
fuse = intermed_damage_smallship03, 0.000000, 500
max_bank_angle = 5 ;35
camera_offset = 9, 33
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 10
camera_vertical_turn_down_angle = 20
camera_turn_look_ahead_slerp_amount = 1.000000
DA_archetype = ships\\bounty_hunter\\bh_fighter\\bh_fighter.cmp
material_library = ships\\liberty\\li_playerships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
cockpit = cockpits\\liberty\\bh_fighter.ini
pilot_mesh = generic_pilot
distance_render = 3000
explosion_arch = explosion_li
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 18000.000000, 18000.000000, 58000.000000
angular_drag = 15000.000000, 15000.000000, 35000.000000
rotation_inertia = 2800.000000, 2800.000000, 1000.000000
nudge_force = 30000.000000
bay_door_anim = Sc_open baydoor
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
num_exhaust_nozzles = 1
HP_tractor_source = HpTractor_Source

[CollisionGroup]
obj = bh_topfin_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
mass = 5.000000
debris_type = debris_small_ship
dmg_hp = Dptopfin
dmg_obj = bh_fighter_dmg_topfin_cap
separation_explosion = explosion_small_ship_breakoff
type = Top_Fin
hit_pts = {bhf_fin_hit_pts}
root_health_proxy = false
explosion_resistance = {bhf_fin_expl_resist}

[CollisionGroup]
obj = bh_btmfin_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpBtmfin
dmg_obj = bh_fighter_dmg_btmfin_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Fin
hit_pts = {bhf_fin_hit_pts}
root_health_proxy = false
explosion_resistance = {bhf_fin_expl_resist}

[CollisionGroup]
obj = bh_eng01_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpEngine01
dmg_obj = bh_fighter_dmg_engine_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Engine
hit_pts = {bhf_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {bhf_engine_expl_resist}

[Simple]
nickname = bh_fighter_dmg_topfin_cap
DA_archetype = ships\\bounty_hunter\\bh_fighter\\bh_dmg_topfin.3db
material_library = ships\\liberty\\li_playerships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = bh_fighter_dmg_btmfin_cap
DA_archetype = ships\\bounty_hunter\\bh_fighter\\bh_dmg_btmfin.3db
material_library = ships\\liberty\\li_playerships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = bh_fighter_dmg_port_wing_cap
DA_archetype = ships\\bounty_hunter\\bh_fighter\\bh_dmg_port_wing.3db
material_library = ships\\liberty\\li_playerships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = bh_fighter_dmg_star_wing_cap
DA_archetype = ships\\bounty_hunter\\bh_fighter\\bh_dmg_star_wing.3db
material_library = ships\\liberty\\li_playerships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Ship]
ship_class = 1
{ship_bh_elite}
LODranges = 0, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_hfighter
mission_property = can_use_berths
type = FIGHTER
DA_archetype = ships\\bounty_hunter\\bh_elite\\bh_elite.cmp
material_library = ships\\liberty\\li_playerships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
cockpit = cockpits\\liberty\\bh_elite.ini
pilot_mesh = generic_pilot
linear_drag = 1.000000
max_bank_angle = 20
camera_offset = 7, 33
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 17
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 25
camera_turn_look_ahead_slerp_amount = 1.000000
explosion_arch = explosion_li
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 55000.000000, 55000.000000, 230000.000000
angular_drag = 41000.000000, 41000.000000, 141000.000000
rotation_inertia = 8400.000000, 8400.000000, 8400.000000
nudge_force = 30000.000000
bay_door_anim = Sc_open baydoor
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2

[CollisionGroup]
obj = bh_eng02_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpEngine02
dmg_obj = bh_fighter_dmg_engine_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Bottom_Engine
hit_pts = {bhe_engine2_hit_pts}
root_health_proxy = false
explosion_resistance = {bhe_engine2_expl_resist}


[CollisionGroup]
obj = bh_topfin_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
mass = 5.000000
debris_type = debris_small_ship
dmg_hp = Dptopfin
dmg_obj = bh_fighter_dmg_topfin_cap
separation_explosion = explosion_small_ship_breakoff
type = Top_Fin
hit_pts = {bhe_fin1_hit_pts}
root_health_proxy = false
explosion_resistance = {bhe_fin1_expl_resist}

[CollisionGroup]
obj = bh_btmfin_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpBtmfin
dmg_obj = bh_fighter_dmg_btmfin_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Fin
hit_pts = {bhe_fin2_hit_pts}
root_health_proxy = false
explosion_resistance = {bhe_fin2_expl_resist}

[CollisionGroup]
obj = bh_port_wing_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpPortwing
dmg_obj = bh_fighter_dmg_port_wing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Wing
hit_pts = {bhe_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {bhe_wing_expl_resist}

[CollisionGroup]
obj = bh_star_wing_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpStarwing
dmg_obj = bh_fighter_dmg_star_wing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Wing
hit_pts = {bhe_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {bhe_wing_expl_resist}

[CollisionGroup]
obj = bh_eng01_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpEngine01
dmg_obj = bh_fighter_dmg_engine_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Top_engine
hit_pts = {bhe_engine1_hit_pts}
root_health_proxy = false
explosion_resistance = {bhe_engine1_expl_resist}

[Ship]
ship_class = 7
{ship_bh_elite2}
LODranges = 0, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_hfighter
mission_property = can_use_berths
type = FIGHTER
DA_archetype = ships\\bounty_hunter\\bh_vheavy_fighter\\bh_vheavy_fighter.cmp
; DA_archetype = ships\\bounty_hunter\\bh_vheavy_fighter\\bhu_elite.cmp
material_library = ships\\liberty\\li_playerships.mat
aterial_library = fx\\envmapbasic.mat
envmap_material = envmapship
cockpit = cockpits\\liberty\\bh_elite2.ini
pilot_mesh = generic_pilot
linear_drag = 1
max_bank_angle = 2 ;30
camera_offset = 9, 35
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 10
camera_vertical_turn_down_angle = 20
camera_turn_look_ahead_slerp_amount = 1.000000
explosion_arch = explosion_li
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 55000.000000, 55000.000000, 143000.000000
angular_drag = 41000.000000, 41000.000000, 141000.000000
rotation_inertia = 8400.000000, 8400.000000, 8400.000000
nudge_force = 10000.000000
bay_door_anim = Sc_open baydoor
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2

[CollisionGroup]
obj = bh_eng02_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpEngine02
dmg_obj = bh_fighter_dmg_engine_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Bottom_Engine
hit_pts = {bhe2_engine2_hit_pts}
root_health_proxy = false
explosion_resistance = {bhe2_engine2_expl_resist}

[CollisionGroup]
obj = bh_topfin_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
mass = 5.000000
debris_type = debris_small_ship
dmg_hp = Dptopfin
dmg_obj = bh_fighter_dmg_topfin_cap
separation_explosion = explosion_small_ship_breakoff
type = Top_Fin
hit_pts = {bhe2_fin1_hit_pts}
root_health_proxy = false
explosion_resistance = {bhe2_fin1_expl_resist}

[CollisionGroup]
obj = bh_btmfin_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpBtmfin
dmg_obj = bh_fighter_dmg_btmfin_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Fin
hit_pts = {bhe2_fin2_hit_pts}
root_health_proxy = false
explosion_resistance = {bhe2_fin2_expl_resist}

[CollisionGroup]
obj = bh_port_wing_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpPortwing
dmg_obj = bh_fighter_dmg_port_wing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Wing
hit_pts = {bhe2_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {bhe2_wing_expl_resist}

[CollisionGroup]
obj = bh_star_wing_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpStarwing
dmg_obj = bh_fighter_dmg_star_wing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Wing
hit_pts = {bhe2_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {bhe2_wing_expl_resist}

[CollisionGroup]
obj = bh_eng01_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpEngine01
dmg_obj = bh_fighter_dmg_engine_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Top_engine
hit_pts = {bhe2_engine1_hit_pts}
root_health_proxy = false
explosion_resistance = {bhe2_engine1_expl_resist}

[Simple]
nickname = bh_fighter_dmg_engine_cap
DA_archetype = ships\\bounty_hunter\\bh_fighter\\bh_dmg_engine01.3db
material_library = ships\\liberty\\li_playerships.mat
mass = 5.000000
LODranges = 0, 500, 2000


[Ship] ; real corsair fighter
ship_class = 4
{ship_pi_fighter}
LODranges = 0, 2000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_pirlf
mission_property = can_use_berths
type = FIGHTER
DA_archetype = Ships\\corsair\\co_fighter\\co_fighter.cmp
material_library = ships\\corsair\\co_ships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
max_bank_angle = 25
camera_offset = 13, 52
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 25
camera_turn_look_ahead_slerp_amount = 1.000000
cockpit = cockpits\\corsair\\corsair_fighter.ini
pilot_mesh = generic_pilot
linear_drag = 1.000000
explosion_arch = explosion_co
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 18000.000000, 18000.000000, 58000.000000
angular_drag = 15000.000000, 15000.000000, 35000.000000
rotation_inertia = 2800.000000, 2800.000000, 1000.000000
nudge_force = 60000.000000
bay_door_anim = Sc_open baydoor
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2

[CollisionGroup]
obj = fins_mid_lod1
separable = true
parent_impulse = 320.000000
child_impulse = 4.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Middle_Wing
hit_pts = {pf_fin_hit_pts}
root_health_proxy = false
explosion_resistance = {pf_fin_expl_resist}

[CollisionGroup]
obj = fins_top_lod1
separable = true
parent_impulse = 320.000000
child_impulse = 4.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Top_Fin
hit_pts = {pf_fin_hit_pts}
root_health_proxy = false
explosion_resistance = {pf_fin_expl_resist}

[CollisionGroup]
obj = starboard_engine_lod1
separable = true
parent_impulse = 320.000000
child_impulse = 4.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Engine
hit_pts = {pf_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {pf_engine_expl_resist}

[CollisionGroup]
obj = port_engine_lod1
separable = true
parent_impulse = 320.000000
child_impulse = 4.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Engine
hit_pts = {pf_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {pf_engine_expl_resist}

[Ship] ; real corsair elite fighter
ship_class = 5
{ship_pi_elite}
LODranges = 0, 1000, 2000, 10000
msg_id_prefix = gcs_refer_shiparch_pirhf
mission_property = can_use_berths
type = FIGHTER
DA_archetype = Ships\\corsair\\co_elite\\co_elite.cmp
material_library = ships\\corsair\\co_ships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
max_bank_angle = 2 ;20
camera_offset = 10, 40
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 17
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 25
camera_turn_look_ahead_slerp_amount = 1.000000
cockpit = cockpits\\corsair\\corsair_elite.ini
pilot_mesh = generic_pilot
linear_drag = 1.000000
explosion_arch = explosion_co
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 43000.000000, 43000.000000, 230000.000000
angular_drag = 41000.000000, 41000.000000, 141000.000000
rotation_inertia = 8400.000000, 8400.000000, 8400.000000
nudge_force = 30000.000000
bay_door_anim = Sc_open door
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 3

[CollisionGroup]
obj = fins_top1_lod1
separable = true
parent_impulse = 320.000000
child_impulse = 4.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Top_Fin
hit_pts = {pe_fin_hit_pts}
root_health_proxy = false
explosion_resistance = {pe_fin_expl_resist}

[CollisionGroup]
obj = fin_starboard1_lod1
separable = true
parent_impulse = 320.000000
child_impulse = 4.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Fin
hit_pts = {pe_fin_hit_pts}
root_health_proxy = false
explosion_resistance = {pe_fin_expl_resist}

[CollisionGroup]
obj = fin_port1_lod1
separable = true
parent_impulse = 320.000000
child_impulse = 4.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Fin
hit_pts = {pe_fin_hit_pts}
root_health_proxy = false
explosion_resistance = {pe_fin_expl_resist}

[CollisionGroup]
obj = fins_lwr1_lod1
separable = true
parent_impulse = 320.000000
child_impulse = 4.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Fin
hit_pts = {pe_fin_hit_pts}
root_health_proxy = false
explosion_resistance = {pe_fin_expl_resist}

[CollisionGroup]
obj = middle_engine_lod1
separable = true
parent_impulse = 320.000000
child_impulse = 4.000000
debris_type = debris_small_ship
dmg_hp = DpMiddle_Engine
dmg_obj = corsair_elite_dmg_middle_engine
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Engine
hit_pts = {pe_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {pe_engine_expl_resist}

[CollisionGroup]
obj = starboard_engine_lod1
separable = true
parent_impulse = 320.000000
child_impulse = 4.000000
debris_type = debris_small_ship
dmg_hp = DpStarboard_Engine
dmg_obj = corsair_elite_dmg_starboard_engine
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Engine
hit_pts = {pe_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {pe_engine_expl_resist}

[CollisionGroup]
obj = port_engine_lod1
separable = true
parent_impulse = 320.000000
child_impulse = 4.000000
debris_type = debris_small_ship
dmg_hp = DpPort_Engine
dmg_obj = corsair_elite_dmg_port_engine
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Engine
hit_pts = {pe_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {pe_engine_expl_resist}

[Simple]
nickname = corsair_elite_dmg_middle_engine
DA_archetype = ships\\corsair\\co_elite\\co_elite_dmg_middle_engine.3db
material_library = ships\\corsair\\co_ships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = corsair_elite_dmg_starboard_engine
DA_archetype = ships\\corsair\\co_elite\\co_elite_dmg_starboard_engine.3db
material_library = ships\\corsair\\co_ships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = corsair_elite_dmg_port_engine
DA_archetype = ships\\corsair\\co_elite\\co_elite_dmg_port_engine.3db
material_library = ships\\corsair\\co_ships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Ship] ; real corsair freighter
ship_class = 8
{ship_pi_freighter}
LODranges = 0, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_pirf
mission_property = can_use_berths
type = FREIGHTER
DA_archetype = Ships\\corsair\\co_freighter\\co_freighter.cmp
material_library = ships\\corsair\\co_ships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
max_bank_angle = 1 ;15
camera_offset = 10, 47
camera_angular_acceleration = 0.035000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 20
camera_turn_look_ahead_slerp_amount = 1.000000
cockpit = cockpits\\corsair\\corsair_freighter.ini
pilot_mesh = generic_pilot
linear_drag = 1.000000
explosion_arch = explosion_co_freighter
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 54000.000000, 54000.000000, 104000.000000
angular_drag = 60000.000000, 60000.000000, 60000.000000
rotation_inertia = 16800.000000, 16800.000000, 16800.000000
nudge_force = 100000.000000
bay_door_anim = Sc_open baydoor
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2

[CollisionGroup]
obj = starboard_wing_lod1
separable = true
parent_impulse = 320.000000
child_impulse = 15.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Fin
hit_pts = {pfr_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {pfr_wing_expl_resist}

[CollisionGroup]
obj = port_wing_lod1
separable = true
parent_impulse = 320.000000
child_impulse = 15.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Fin
hit_pts = {pfr_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {pfr_wing_expl_resist}

[CollisionGroup]
obj = fins_top_lod1
separable = true
parent_impulse = 320.000000
child_impulse = 15.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Top_Fin
hit_pts = {pfr_fin_hit_pts}
root_health_proxy = false
explosion_resistance = {pfr_fin_expl_resist}

[CollisionGroup]
obj = starboard_engine_lod1
separable = true
parent_impulse = 320.000000
child_impulse = 4.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Engine
hit_pts = {pfr_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {pfr_engine_expl_resist}

[CollisionGroup]
obj = port_engine_lod1
separable = true
parent_impulse = 320.000000
child_impulse = 4.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Engine
hit_pts = {pfr_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {pfr_engine_expl_resist}

[Ship]
ship_class = 0
{ship_co_fighter}
LODranges = 0, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_lfighter
mission_property = can_use_berths
type = FIGHTER
DA_archetype = Ships\\pirate\\pi_fighter\\pi_fighter.cmp
;DA_archetype = Ships\\pirate\\pi_fighter\\BAT.cmp
material_library = ships\\kusari\\ku_playerships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
cockpit = cockpits\\kusari\\pi_fighter.ini
max_bank_angle = 5 ;35
camera_offset = 9, 33
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 8
camera_vertical_turn_down_angle = 28
camera_turn_look_ahead_slerp_amount = 1.000000
pilot_mesh = generic_pilot
linear_drag = 1.000000
explosion_arch = explosion_co_fighter
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 18000.000000, 18000.000000, 58000.000000
angular_drag = 15000.000000, 15000.000000, 35000.000000
rotation_inertia = 2800.000000, 2800.000000, 1000.000000
nudge_force = 30000.000000
bay_door_anim = Sc_pi_fighter
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02

[CollisionGroup]
obj = wing_port_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpWing_port
dmg_obj = corsair_wing_port_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Wing
hit_pts = {cf_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {cf_wing_expl_resist}

[CollisionGroup]
obj = wing_starboard_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpWing_starboard
dmg_obj = corsair_wing_star_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Wing
hit_pts = {cf_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {cf_wing_expl_resist}

[CollisionGroup]
obj = engine_port_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpEngine01
dmg_obj = corsair_dmg_port_heavyeng_cap2
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Engine
hit_pts = {cf_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {cf_engine_expl_resist}

[CollisionGroup]
obj = engine_starboard_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpEngine02
dmg_obj = corsair_dmg_star_heavyeng_cap2
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Engine
hit_pts = {cf_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {cf_engine_expl_resist}

[Simple]
nickname = corsair_wing_port_cap
DA_archetype = ships\\pirate\\pi_fighter\\pi_dmg_port_wing.3db
material_library = ships\\kusari\\ku_playerships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = corsair_wing_star_cap
DA_archetype = ships\\pirate\\pi_fighter\\pi_dmg_star_wing.3db
material_library = ships\\kusari\\ku_playerships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = corsair_top_fin_cap
DA_archetype = ships\\pirate\\pi_fighter\\pi_dmg_topfin.3db
material_library = ships\\kusari\\ku_playerships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = corsair_btm_fin_cap
DA_archetype = ships\\pirate\\pi_fighter\\pi_dmg_btmfin.3db
material_library = ships\\kusari\\ku_playerships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = corsair_dmg_port_heavyeng_cap
DA_archetype = ships\\pirate\\pi_fighter\\pi_dmg_port_heavyeng.3db
material_library = ships\\kusari\\ku_playerships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = corsair_dmg_star_heavyeng_cap
DA_archetype = ships\\pirate\\pi_fighter\\pi_dmg_star_heavyeng.3db
material_library = ships\\kusari\\ku_playerships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = corsair_dmg_star_heavywing_cap
DA_archetype = ships\\pirate\\pi_fighter\\pi_dmg_star_heavywing.3db
material_library = ships\\kusari\\ku_playerships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = corsair_dmg_port_heavywing_cap
DA_archetype = ships\\pirate\\pi_fighter\\pi_dmg_port_heavywing.3db
material_library = ships\\kusari\\ku_playerships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Ship]
ship_class = 1
{ship_co_elite}
LODranges = 0, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_hfighter
mission_property = can_use_berths
type = FIGHTER
DA_archetype = Ships\\pirate\\pi_elite\\pi_elite.cmp
material_library = ships\\kusari\\ku_playerships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
cockpit = cockpits\\kusari\\pi_elite.ini
max_bank_angle = 2 ;30
camera_offset = 11, 35
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 17
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 25
camera_turn_look_ahead_slerp_amount = 1.000000
pilot_mesh = generic_pilot
linear_drag = 1.000000
explosion_arch = explosion_co_elite
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 43000.000000, 43000.000000, 230000.000000
angular_drag = 41000.000000, 41000.000000, 141000.000000
rotation_inertia = 8400.000000, 8400.000000, 8400.000000
nudge_force = 30000.000000
bay_door_anim = Sc_pi_elite
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02

[CollisionGroup]
obj = wing_port_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpWing_port
dmg_obj = corsair_wing_port_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Wing
hit_pts = {ce_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {ce_wing_expl_resist}

[CollisionGroup]
obj = wing_starboard_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpWing_starboard
dmg_obj = corsair_wing_star_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Wing
hit_pts = {ce_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {ce_wing_expl_resist}

[CollisionGroup]
obj = fin_top_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpFin_top
dmg_obj = corsair_top_fin_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Top_Fin
hit_pts = {ce_fin_hit_pts}
root_health_proxy = false
explosion_resistance = {ce_fin_expl_resist}

[CollisionGroup]
obj = fin_bottom_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DPFin_bottom
dmg_obj = corsair_btm_fin_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Fin
hit_pts = {ce_fin_hit_pts}
root_health_proxy = false
explosion_resistance = {ce_fin_expl_resist}

[CollisionGroup]
obj = engine_port_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpEngine01
dmg_obj = corsair_dmg_port_heavyeng_cap2
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Engine
hit_pts = {ce_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {ce_engine_expl_resist}

[CollisionGroup]
obj = engine_starboard_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpEngine02
dmg_obj = corsair_dmg_star_heavyeng_cap2
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Engine
hit_pts = {ce_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {ce_engine_expl_resist}

[Ship]
ship_class = 7
{ship_co_elite2}
LODranges = 0, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_hfighter
mission_property = can_use_berths
type = FIGHTER
;DA_archetype = Ships\\pirate\\pi_vheavy_fighter\\pi_vheavy_fighter.cmp
DA_archetype = Ships\\pirate\\pi_vheavy_fighter\\pir_elite.cmp
material_library = ships\\kusari\\ku_playerships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
cockpit = cockpits\\kusari\\pi_elite2.ini
max_bank_angle = 2 ;30
camera_offset = 11, 33
camera_angular_acceleration = 0.060000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 10
camera_vertical_turn_down_angle = 20
camera_turn_look_ahead_slerp_amount = 1.000000
pilot_mesh = generic_pilot
linear_drag = 1.000000
explosion_arch = explosion_ku
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 43000.000000, 43000.000000, 143000.000000
angular_drag = 41000.000000, 41000.000000, 141000.000000
rotation_inertia = 8400.000000, 8400.000000, 8400.000000
nudge_force = 30000.000000
bay_door_anim = Sc_pi_vheavy_fighter
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2

[CollisionGroup]
obj = wing_port_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpWing_port
dmg_obj = corsair_dmg_port_heavywing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Wing
hit_pts = {ce2_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {ce2_wing_expl_resist}

[CollisionGroup]
obj = wing_starboard_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpWing_starboard
dmg_obj = corsair_dmg_star_heavywing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Wing
hit_pts = {ce2_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {ce2_wing_expl_resist}

[CollisionGroup]
obj = fin_top_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpFin_top
dmg_obj = corsair_top_fin_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Top_Fin
hit_pts = {ce2_fin_hit_pts}
root_health_proxy = false
explosion_resistance = {ce2_fin_expl_resist}

[CollisionGroup]
obj = fin_bottom_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DPFin_bottom
dmg_obj = corsair_btm_fin_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Fin
hit_pts = {ce2_fin_hit_pts}
root_health_proxy = false
explosion_resistance = {ce2_fin_expl_resist}

[CollisionGroup]
obj = engine_port_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpEngine01
dmg_obj = corsair_dmg_port_heavyeng_cap2
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Engine
hit_pts = {ce2_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {ce2_engine_expl_resist}

[CollisionGroup]
obj = engine_starboard_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpEngine02
dmg_obj = corsair_dmg_star_heavyeng_cap2
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Engine
hit_pts = {ce2_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {ce2_engine_expl_resist}

[Simple]
nickname = corsair_dmg_port_heavyeng_cap2
DA_archetype = ships\\pirate\\pi_fighter\\pi_dmg_port_heavyeng.3db
material_library = ships\\kusari\\ku_playerships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = corsair_dmg_star_heavyeng_cap2
DA_archetype = ships\\pirate\\pi_fighter\\pi_dmg_star_heavyeng.3db
material_library = ships\\kusari\\ku_playerships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = cv_dmg_port_wing01_cap
DA_archetype = Ships\\civilian\\cv_starflier\\cv_dmg_port_wing.3db
material_library = ships\\civilian\\cv_ships.mat
mass = 5.000000
LODranges = 0, 100, 1500

[Simple]
nickname = cv_dmg_starboard_wing01_cap
DA_archetype = Ships\\civilian\\cv_starflier\\cv_dmg_starboard_wing.3db
material_library = ships\\civilian\\cv_ships.mat
mass = 5.000000
LODranges = 0, 100, 1500

[Simple]
nickname = cv_dmg_mid_wing_cap
DA_archetype = Ships\\civilian\\cv_starflier\\cv_dmg_mid_wing.3db
material_library = ships\\civilian\\cv_ships.mat
mass = 5.000000
LODranges = 0, 100, 1500

[Simple]
nickname = cv_dmg_engine01
DA_archetype = Ships\\civilian\\CV_STARFLIER\\cv_dmg_engine01.3db
material_library = ships\\civilian\\cv_ships.mat
mass = 5.000000
LODranges = 0, 200, 2000


[Ship]
ship_class = 19
{ship_ge_fighter}
LODranges = 0, 300, 500, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_starflier
mission_property = can_use_berths
type = FIGHTER
DA_archetype = ships\\civilian\\cv_starflier\\cv_starflier.cmp
material_library = ships\\civilian\\cv_ships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship02
cockpit = cockpits\\civilian\\civilian.ini
pilot_mesh = generic_pilot
linear_drag = 1.000000
max_bank_angle = 5 ;35
camera_offset = 13, 42
; camera_offset = 10, 42
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 30
camera_turn_look_ahead_slerp_amount = 1.000000
explosion_arch = explosion_ku
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 25000.000000, 25000.000000, 58000.000000
angular_drag = 15000.000000, 15000.000000, 35000.000000
rotation_inertia = 3800.000000, 3800.000000, 1000.000000
nudge_force = 30000.000000
bay_door_anim = Sc_open baydoor
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 1

[CollisionGroup]
obj = port_wing_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
dmg_hp = DpPort_Wing
dmg_obj = cv_dmg_port_wing01_cap
type = Port_Wing
hit_pts = {gf1_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {gf1_wing_expl_resist}

[CollisionGroup]
obj = star_wing_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
dmg_hp = DpStarboard_Wing
dmg_obj = cv_dmg_starboard_wing01_cap
type = Starboard_Wing
hit_pts = {gf1_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {gf1_wing_expl_resist}

[CollisionGroup]
obj = engine_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Engine
dmg_hp = DpEngine
dmg_obj = cv_dmg_engine01
hit_pts = {gf1_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {gf1_engine_expl_resist}





[Ship]
ship_class = 19
{ship_ge_fighter_mk2}
LODranges = 0, 300, 500, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_starflier
mission_property = can_use_berths
type = FIGHTER
DA_archetype = ships\\civilian\\cv_starflier\\cv_starflier.cmp
material_library = ships\\civilian\\cv_ships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship02
cockpit = cockpits\\civilian\\civilian.ini
pilot_mesh = generic_pilot
linear_drag = 1.000000
max_bank_angle = 5 ;35
camera_offset = 13, 42
; camera_offset = 10, 42
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 30
camera_turn_look_ahead_slerp_amount = 1.000000
explosion_arch = explosion_ku
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 25000.000000, 25000.000000, 58000.000000
angular_drag = 15000.000000, 15000.000000, 35000.000000
rotation_inertia = 3800.000000, 3800.000000, 1000.000000
nudge_force = 30000.000000
bay_door_anim = Sc_open baydoor
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 1

[CollisionGroup]
obj = port_wing_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
dmg_hp = DpPort_Wing
dmg_obj = cv_dmg_port_wing01_cap
type = Port_Wing
hit_pts = {gf1_mk2_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {gf1_mk2_wing_expl_resist}

[CollisionGroup]
obj = star_wing_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
dmg_hp = DpStarboard_Wing
dmg_obj = cv_dmg_starboard_wing01_cap
type = Starboard_Wing
hit_pts = {gf1_mk2_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {gf1_mk2_wing_expl_resist}

[CollisionGroup]
obj = engine_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Engine
dmg_hp = DpEngine
dmg_obj = cv_dmg_engine01
hit_pts = {gf1_mk2_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {gf1_mk2_engine_expl_resist}


[Ship]
ship_class = 4
{ship_ge_fighter2}
LODranges = 0, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_startracker
mission_property = can_use_berths
type = FIGHTER
DA_archetype = ships\\civilian\\cv_startracker\\cv_startracker.cmp
material_library = ships\\civilian\\cv_ships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship02
cockpit = cockpits\\civilian\\civilian.ini
pilot_mesh = generic_pilot
linear_drag = 1.000000
max_bank_angle = 5 ;35
camera_offset = 13, 42
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 30
camera_turn_look_ahead_slerp_amount = 1.000000
explosion_arch = explosion_ku
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 15800.000000, 15800.000000, 58000.000000
angular_drag = 15000.000000, 15000.000000, 35000.000000
rotation_inertia = 2800.000000, 2800.000000, 1000.000000
nudge_force = 60000.000000
bay_door_anim = Sc_open baydoor
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2

[CollisionGroup]
obj = port_wing_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
dmg_hp = DpPort_Wing
dmg_obj = cv_dmg_port_wing01_cap
type = Port_Wing
hit_pts = {gf2_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {gf2_wing_expl_resist}

[CollisionGroup]
obj = star_wing_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Wing
dmg_hp = DpStarboard_Wing
dmg_obj = cv_dmg_starboard_wing01_cap
hit_pts = {gf2_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {gf2_wing_expl_resist}

[CollisionGroup]
obj = mid_wing_lod1
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Middle_Wing
dmg_hp = DpMid_wing
dmg_obj = cv_dmg_mid_wing_cap
hit_pts = {gf2_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {gf2_wing_expl_resist}

[CollisionGroup]
obj = engine_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Engine
dmg_hp = DpEngine
dmg_obj = cv_dmg_engine01
hit_pts = {gf2_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {gf2_engine_expl_resist}


[Ship]
ship_class = 4
{ship_ge_fighter3}
LODranges = 0, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_startracker
mission_property = can_use_berths
type = FIGHTER
DA_archetype = ships\\civilian\\cv_starblazer\\cv_starblazer.cmp
material_library = ships\\civilian\\cv_ships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship02
cockpit = cockpits\\civilian\\civilian.ini
pilot_mesh = generic_pilot
linear_drag = 1.000000
max_bank_angle = 5 ;35
camera_offset = 13, 42
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 30
camera_turn_look_ahead_slerp_amount = 1.000000
explosion_arch = explosion_ku
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 15800.000000, 15800.000000, 58000.000000
angular_drag = 15000.000000, 15000.000000, 35000.000000
rotation_inertia = 2800.000000, 2800.000000, 1000.000000
nudge_force = 60000.000000
bay_door_anim = Sc_open baydoor
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2

[CollisionGroup]
obj = port_wing_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
dmg_hp = DpPort_Wing
dmg_obj = cv_dmg_port_wing01_cap
type = Port_Wing
hit_pts = {gf3_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {gf3_wing_expl_resist}

[CollisionGroup]
obj = star_wing_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Wing
dmg_hp = DpStarboard_Wing
dmg_obj = cv_dmg_starboard_wing01_cap
hit_pts = {gf3_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {gf3_wing_expl_resist}

[CollisionGroup]
obj = mid_wing_lod1
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Middle_Wing
dmg_hp = DpMid_wing
dmg_obj = cv_dmg_mid_wing_cap
hit_pts = {gf3_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {gf3_wing_expl_resist}

[CollisionGroup]
obj = engine_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Engine
dmg_hp = DpEngine
dmg_obj = cv_dmg_engine01
hit_pts = {gf3_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {gf3_engine_expl_resist}

[CollisionGroup]
obj = engine02_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Engine
dmg_hp = DpEngine
dmg_obj = cv_dmg_engine01
hit_pts = {gf3_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {gf3_engine_expl_resist}


[Ship]
ship_class = 4
{ship_ge_fighter4}
LODranges = 0, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_lfighter
mission_property = can_use_berths
type = FIGHTER
linear_drag = 1.000000
max_bank_angle = 5 ;35
camera_offset = 13, 42
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 30
camera_turn_look_ahead_slerp_amount = 1.000000
DA_archetype = ships\\civilian\\cv_fighter\\cv_fighter.cmp
material_library = ships\\civilian\\cv_ships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
cockpit = cockpits\\civilian\\civilian_fighter.ini
pilot_mesh = generic_pilot
distance_render = 3000
explosion_arch = explosion_cv_fighter
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 18000.000000, 18000.000000, 58000.000000
angular_drag = 15000.000000, 15000.000000, 35000.000000
rotation_inertia = 2800.000000, 2800.000000, 1000.000000
nudge_force = 30000.000000
bay_door_anim = Sc_open baydoor
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
num_exhaust_nozzles = 1
HP_tractor_source = HpTractor_Source

[CollisionGroup]
obj = cv_port_wing_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Wing
dmg_hp = DpDmg_portwing
dmg_obj = cv_fighter4_port_wing_cap
hit_pts = {gf4_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {gf4_wing_expl_resist}

[CollisionGroup]
obj = cv_star_wing_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Wing
dmg_hp = DpDmg_starwing
dmg_obj = cv_fighter4_star_wing_cap
hit_pts = {gf4_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {gf4_wing_expl_resist}

[CollisionGroup]
obj = cv_engine01_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Top_Engine
dmg_hp = DpEngine01
dmg_obj = gf6_topengine_dmg
hit_pts = {gf4_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {gf4_engine_expl_resist}

[CollisionGroup]
obj = cv_engine02_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Bottom_Engine
dmg_hp = DpEngine02
dmg_obj = gf6_bottomengine_dmg
hit_pts = {gf4_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {gf4_engine_expl_resist}

[Simple]
nickname = cv_fighter4_port_wing_cap
DA_archetype = Ships\\civilian\\cv_fighter\\cv_fighter_dmg_pwing.3db
material_library = ships\\civilian\\cv_ships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = cv_fighter4_star_wing_cap
DA_archetype = Ships\\civilian\\cv_fighter\\cv_fighter_dmg_swing.3db
material_library = ships\\civilian\\cv_ships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = cv_fighter5_top_wing_cap
DA_archetype = Ships\\civilian\\cv_fighter\\cv_fighter_dmg_topfin.3db
material_library = ships\\civilian\\cv_ships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = cv_fighter5_btm_wing_cap
DA_archetype = Ships\\civilian\\cv_fighter\\cv_fighter_dmg_btmwing.3db
material_library = ships\\civilian\\cv_ships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Ship]
ship_class = 1
{ship_ge_fighter5}
msg_id_prefix = gcs_refer_shiparch_hfighter
mission_property = can_use_berths
LODranges = 0, 1000, 5000, 10000
type = FIGHTER
DA_archetype = ships\\civilian\\cv_elite\\cv_elite.cmp
material_library = ships\\civilian\\cv_ships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
cockpit = cockpits\\civilian\\civilian_elite.ini
pilot_mesh = generic_pilot
linear_drag = 1.000000
max_bank_angle = 2 ;30
camera_offset = 13, 42
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 30
camera_turn_look_ahead_slerp_amount = 1.000000
explosion_arch = explosion_cv_fighter
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 55000.000000, 55000.000000, 48000.000000
angular_drag = 41000.000000, 41000.000000, 35000.000000
rotation_inertia = 8400.000000, 8400.000000, 1000.000000
nudge_force = 30000.000000
bay_door_anim = Sc_open baydoor
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2

[CollisionGroup]
obj = cv_port_wing_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Middle_Wing
dmg_hp = DpDmg_portwing
dmg_obj = cv_fighter4_port_wing_cap
hit_pts = {gf5_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {gf5_wing_expl_resist}

[CollisionGroup]
obj = cv_star_wing_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Wing
dmg_hp = DpDmg_starwing
dmg_obj = cv_fighter4_star_wing_cap
hit_pts = {gf5_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {gf5_wing_expl_resist}

[CollisionGroup]
obj = cv_topfin_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Top_Fin
dmg_hp = DpDmg_topfin
dmg_obj = cv_fighter5_top_wing_cap
hit_pts = {gf5_fin_hit_pts}
root_health_proxy = false
explosion_resistance = {gf5_fin_expl_resist}

[CollisionGroup]
obj = cv_engine01_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Top_Engine
dmg_hp = DpEngine01
dmg_obj = gf6_topengine_dmg
hit_pts = {gf5_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {gf5_engine_expl_resist}

[CollisionGroup]
obj = cv_engine02_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Bottom_Engine
dmg_hp = DpEngine02
dmg_obj = gf6_bottomengine_dmg
hit_pts = {gf5_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {gf5_engine_expl_resist}

[Ship]
ship_class = 7
{ship_ge_fighter6}
LODranges = 0, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_hfighter
mission_property = can_use_berths
type = FIGHTER
;DA_archetype = ships\\civilian\\cv_vheavy_fighter\\cv_vheavy_fighter.cmp
DA_archetype = ships\\civilian\\cv_vheavy_fighter\\civ_elite.cmp
material_library = ships\\civilian\\cv_ships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
cockpit = cockpits\\civilian\\civilian_vheavy.ini
pilot_mesh = generic_pilot
linear_drag = 1.000000
max_bank_angle = 2 ;30
camera_offset = 13, 42
camera_angular_acceleration = 0.030000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 30
camera_turn_look_ahead_slerp_amount = 1.000000
explosion_arch = explosion_br
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 55000.000000, 55000.000000, 48000.000000
angular_drag = 41000.000000, 41000.000000, 35000.000000
rotation_inertia = 8400.000000, 8400.000000, 1000.000000
nudge_force = 10000.000000
bay_door_anim = Sc_open baydoor
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2

[CollisionGroup]
obj = cv_port_wing_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Wing
dmg_hp = DpDmg_portwing
dmg_obj = civ_dmg_port_wing
hit_pts = {gf6_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {gf6_wing_expl_resist}

[CollisionGroup]
obj = cv_star_wing_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Wing
dmg_hp = DpDmg_starwing
dmg_obj = civ_dmg_star_wing
hit_pts = {gf6_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {gf6_wing_expl_resist}

[CollisionGroup]
obj = cv_topfin_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Top_Fin
dmg_hp = DpDmg_topfin
dmg_obj = cv_fighter5_top_wing_cap
hit_pts = {gf6_fin_hit_pts}
root_health_proxy = false
explosion_resistance = {gf6_fin_expl_resist}

[CollisionGroup]
obj = cv_btmwing_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Middle_Wing
dmg_hp = DpDmg_btmwing
dmg_obj = cv_fighter5_btm_wing_cap
hit_pts = {gf6_btmwing_hit_pts}
root_health_proxy = false
explosion_resistance = {gf6_btmwing_expl_resist}

[CollisionGroup]
obj = cv_engine01_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Top_Engine
dmg_hp = DpEngine01
dmg_obj = gf6_topengine_dmg
hit_pts = {gf6_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {gf6_engine_expl_resist}

[CollisionGroup]
obj = cv_engine02_lod1
separable = true
parent_impulse = 120.000000
child_impulse = 60.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Bottom_Engine
dmg_hp = DpEngine02
dmg_obj = gf6_bottomengine_dmg
hit_pts = {gf6_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {gf6_engine_expl_resist}

[Simple]
nickname = gf6_topengine_dmg
DA_archetype = Ships\\civilian\\CV_STARFLIER\\cv_dmg_engine01.3db
material_library = ships\\civilian\\cv_ships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = gf6_bottomengine_dmg
DA_archetype = Ships\\civilian\\CV_STARFLIER\\cv_dmg_engine02.3db
material_library = ships\\civilian\\cv_ships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = civ_dmg_star_wing
DA_archetype = Ships\\civilian\\CV_VHEAVY_FIGHTER\\civ_dmg_star_wing.3db
material_library = ships\\civilian\\cv_ships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = civ_dmg_port_wing
DA_archetype = Ships\\civilian\\CV_VHEAVY_FIGHTER\\civ_dmg_port_wing.3db
material_library = ships\\civilian\\cv_ships.mat
mass = 5.000000
LODranges = 0, 200, 2000


;RH_SHIP
[Ship]
ship_class = 4
{ship_bw_fighter}
LODranges = 0, 500, 1000, 10000
msg_id_prefix = gcs_refer_shiparch_Rhelf
mission_property = can_use_berths
type = FIGHTER
linear_drag = 1.000000
max_bank_angle = 1
camera_offset = 9, 33
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 23
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 30
camera_turn_look_ahead_slerp_amount = 1.000000
DA_archetype = ships\\border_world\\bw_fighter\\bw_fighter.cmp
material_library = ships\\border_world\\bw_ships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship02
cockpit = cockpits\\corsair\\bw_fighter.ini
pilot_mesh = generic_pilot
explosion_arch = explosion_rh
steering_torque = 18000.000000, 18000.000000, 58000.000000
angular_drag = 15000.000000, 15000.000000, 35000.000000
rotation_inertia = 2800.000000, 2800.000000, 1000.000000
nudge_force = 30000.000000
bay_door_anim = Sc_open baydoor
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 1

[CollisionGroup]
obj = bw_port_wing01_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
dmg_hp = dpport_wing01
dmg_obj = ew_dmg_portwing01_cap
mass = 5.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
type = Port_Wing
hit_pts = {bwf_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {bwf_wing_expl_resist}

[CollisionGroup]
obj = bw_star_wing01_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
dmg_hp = dpstar_wing01
dmg_obj = ew_dmg_starwing01_cap
mass = 5.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
type = Starboard_Wing
hit_pts = {bwf_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {bwf_wing_expl_resist}

[CollisionGroup]
obj = bw_eng01_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
dmg_hp = dpeng01
dmg_obj = ew_dmg_engine01_cap
mass = 5.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
type = engine
hit_pts = {bwf_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {bwf_engine_expl_resist}

;RH_SHIP
[Ship]
ship_class = 7
{ship_bw_elite}
LODranges = 0, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_Rhehf
mission_property = can_use_berths
type = FIGHTER
DA_archetype = ships\\border_world\\bw_elite\\bw_elite.cmp
material_library = ships\\border_world\\bw_ships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
cockpit = cockpits\\corsair\\bw_elite.ini
pilot_mesh = generic_pilot
linear_drag = 1.000000
max_bank_angle = 2 ;30
camera_offset = 7, 33
camera_angular_acceleration = 0.060000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 10
camera_vertical_turn_down_angle = 20
camera_turn_look_ahead_slerp_amount = 1.000000
explosion_arch = explosion_rh
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 43000.000000, 43000.000000, 230000.000000
angular_drag = 41000.000000, 41000.000000, 141000.000000
rotation_inertia = 8400.000000, 8400.000000, 8400.000000
nudge_force = 30000.000000
bay_door_anim = Sc_open baydoor
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2

[CollisionGroup]
obj = bw_port_wing01_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
dmg_hp = dpport_wing01
dmg_obj = ew_dmg_portwing01_cap
mass = 5.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
type = Port_Wing
hit_pts = {bwe_wing1_hit_pts}
root_health_proxy = false
explosion_resistance = {bwe_wing1_expl_resist}

[CollisionGroup]
obj = bw_port_wing02_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
dmg_hp = dpport_wing02
dmg_obj = ew_dmg_portwing02_cap
mass = 5.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
type = Port_Wing
hit_pts = {bwe_wing1_hit_pts}
root_health_proxy = false
explosion_resistance = {bwe_wing1_expl_resist}

[CollisionGroup]
obj = bw_star_wing01_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
dmg_hp = dpstar_wing01
dmg_obj = ew_dmg_starwing01_cap
mass = 5.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
type = Starboard_Wing
hit_pts = {bwe_wing2_hit_pts}
root_health_proxy = false
explosion_resistance = {bwe_wing2_expl_resist}

[CollisionGroup]
obj = bw_star_wing02_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
dmg_hp = dpstar_wing02
dmg_obj = ew_dmg_starwing02_cap
mass = 5.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
type = Starboard_Wing
hit_pts = {bwe_wing2_hit_pts}
root_health_proxy = false
explosion_resistance = {bwe_wing2_expl_resist}

[CollisionGroup]
obj = bw_eng01_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
dmg_hp = dpeng01
dmg_obj = ew_dmg_engine01_cap
mass = 5.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
type = top_engine
hit_pts = {bwe_engine1_hit_pts}
root_health_proxy = false
explosion_resistance = {bwe_engine1_expl_resist}

[CollisionGroup]
obj = bw_eng02_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
dmg_hp = dpeng02
dmg_obj = ew_dmg_engine02_cap
mass = 5.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
type = top_engine
hit_pts = {bwe_engine2_hit_pts}
root_health_proxy = false
explosion_resistance = {bwe_engine2_expl_resist}

[Simple]
nickname = ew_dmg_portwing01_cap
DA_archetype = ships\\border_world\\bw_elite\\bw_dmg_port_wing01.3db
material_library = ships\\border_world\\bw_ships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = ew_dmg_portwing02_cap
DA_archetype = ships\\border_world\\bw_elite\\bw_dmg_port_wing02.3db
material_library = ships\\border_world\\bw_ships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = ew_dmg_starwing01_cap
DA_archetype = ships\\border_world\\bw_elite\\bw_dmg_star_wing01.3db
material_library = ships\\border_world\\bw_ships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = ew_dmg_starwing02_cap
DA_archetype = ships\\border_world\\bw_elite\\bw_dmg_star_wing02.3db
material_library = ships\\border_world\\bw_ships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = ew_dmg_engine01_cap
DA_archetype = ships\\border_world\\bw_elite\\bw_dmg_engine01.3db
material_library = ships\\border_world\\bw_ships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = ew_dmg_engine02_cap
DA_archetype = ships\\border_world\\bw_elite\\bw_dmg_engine02.3db
material_library = ships\\border_world\\bw_ships.mat
mass = 5.000000
LODranges = 0, 200, 2000

;RH_SHIP
[Ship]
ship_class = 7
{ship_bw_elite2}
LODranges = 0, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_borhf
mission_property = can_use_berths
type = FIGHTER
DA_archetype = ships\\border_world\\bw_vheavy_fighter\\bw_vheavy_fighter.cmp
material_library = ships\\border_world\\bw_ships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
cockpit = cockpits\\corsair\\bw_elite2.ini
pilot_mesh = generic_pilot
linear_drag = 1.000000
max_bank_angle = 2 ;30
camera_offset = 9, 33
camera_angular_acceleration = 0.060000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 10
camera_vertical_turn_down_angle = 20
camera_turn_look_ahead_slerp_amount = 1.000000
explosion_arch = explosion_rh
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 300, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 600, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 43000.000000, 43000.000000, 63000.000000
angular_drag = 41000.000000, 41000.000000, 41000.000000
rotation_inertia = 8400.000000, 8400.000000, 2400.000000
nudge_force = 10000.000000
bay_door_anim = Sc_open baydoor
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2

[CollisionGroup]
obj = bw_port_wing01_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
dmg_hp = dpport_wing01
dmg_obj = ew_dmg_portwing01_cap
mass = 5.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
type = Port_Wing
hit_pts = {bwe2_wing1_hit_pts}
root_health_proxy = false
explosion_resistance = {bwe2_wing1_expl_resist}

[CollisionGroup]
obj = bw_port_wing02_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
dmg_hp = dpport_wing02
dmg_obj = ew_dmg_portwing02_cap
mass = 5.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
type = Port_Wing
hit_pts = {bwe2_wing1_hit_pts}
root_health_proxy = false
explosion_resistance = {bwe2_wing1_expl_resist}

[CollisionGroup]
obj = bw_star_wing01_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
dmg_hp = dpstar_wing01
dmg_obj = ew_dmg_starwing01_cap
mass = 5.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
type = Starboard_Wing
hit_pts = {bwe2_wing2_hit_pts}
root_health_proxy = false
explosion_resistance = {bwe2_wing2_expl_resist}

[CollisionGroup]
obj = bw_star_wing02_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
dmg_hp = dpstar_wing02
dmg_obj = ew_dmg_starwing02_cap
mass = 5.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
type = Starboard_Wing
hit_pts = {bwe2_wing2_hit_pts}
root_health_proxy = false
explosion_resistance = {bwe2_wing2_expl_resist}

[CollisionGroup]
obj = bw_eng01_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
dmg_hp = dpeng01
dmg_obj = ew_dmg_engine01_cap
mass = 5.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
type = top_engine
hit_pts = {bwe2_engine1_hit_pts}
root_health_proxy = false
explosion_resistance = {bwe2_engine1_expl_resist}

[CollisionGroup]
obj = bw_eng02_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
dmg_hp = dpeng02
dmg_obj = ew_dmg_engine02_cap
mass = 5.000000
debris_type = debris_small_ship
separation_explosion = explosion_small_ship_breakoff
type = top_engine
hit_pts = {bwe2_engine2_hit_pts}
root_health_proxy = false
explosion_resistance = {bwe2_engine2_expl_resist}

[Ship]
ship_class = 8
{ship_bw_freighter}
LODranges = 0, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_borf
mission_property = can_use_berths
type = FREIGHTER
DA_archetype = Ships\\border_world\\bw_freighter\\bw_freighter.cmp
material_library = ships\\border_world\\bw_ships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
cockpit = cockpits\\corsair\\bw_freighter.ini
pilot_mesh = generic_pilot
linear_drag = 1.000000
max_bank_angle = 1 ;15
camera_offset = 10, 49
camera_angular_acceleration = 0.035000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 20
camera_turn_look_ahead_slerp_amount = 1.000000
explosion_arch = explosion_li
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
nudge_force = 30000.000000
bay_door_anim = Sc_open baydoor
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 3
steering_torque = 54000.000000, 54000.000000, 54000.000000
angular_drag = 60000.000000, 60000.000000, 60000.000000
rotation_inertia = 16800.000000, 16800.000000, 16800.000000

[CollisionGroup]
obj = bw_port_wing_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpPort_Wing
dmg_obj = ew_freighter_dmg_port_wing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Side_Panel
hit_pts = {bwfr_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {bwfr_wing_expl_resist}

[CollisionGroup]
obj = bw_star_wing_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = dpstar_wing
dmg_obj = ew_freighter_dmg_starboard_wing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Side_Panel
hit_pts = {bwfr_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {bwfr_wing_expl_resist}



[CollisionGroup]
obj = bw_port_eng_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpPort_Eng
dmg_obj = ew_freighter_dmg_port_eng_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Engine
hit_pts = {bwfr_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {bwfr_engine_expl_resist}

[CollisionGroup]
obj = bw_star_eng_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpStar_Eng
dmg_obj = ew_freighter_dmg_star_eng_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Engine
hit_pts = {bwfr_engine_hit_pts}
root_health_proxy = false
explosion_resistance = {bwfr_engine_expl_resist}








[Simple]
nickname = ew_freighter_dmg_port_wing_cap
DA_archetype = Ships\\border_world\\bw_freighter\\bw_dmg_port_wing.3db
material_library = ships\\border_world\\bw_ships.mat
mass = 5.000000
LODranges = 0, 500, 2200

[Simple]
nickname = ew_freighter_dmg_starboard_wing_cap
DA_archetype = Ships\\border_world\\bw_freighter\\bw_dmg_star_wing.3db
material_library = ships\\border_world\\bw_ships.mat
mass = 5.000000
LODranges = 0, 500, 2200

[Simple]
nickname = ew_freighter_dmg_port_eng_cap
DA_archetype = Ships\\border_world\\bw_freighter\\bw_dmg_port_engine.3db
material_library = ships\\border_world\\bw_ships.mat
mass = 5.000000
LODranges = 0, 500, 2200

[Simple]
nickname = ew_freighter_dmg_star_eng_cap
DA_archetype = Ships\\border_world\\bw_freighter\\bw_dmg_star_engine.3db
material_library = ships\\border_world\\bw_ships.mat
mass = 5.000000
LODranges = 0, 500, 2200

[Ship]
ship_class = 6
{ship_or_elite}
LODranges = 0, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_Ordhf
mission_property = can_use_berths
type = FIGHTER
DA_archetype = ships\\order\\or_elite\\or_elite.cmp
material_library = Ships\\order\\or_ships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
cockpit = cockpits\\liberty\\or_elite.ini
pilot_mesh = generic_pilot
linear_drag = 1.000000
max_bank_angle = 2 ;30
camera_offset = 12, 46
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 17
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 25
camera_turn_look_ahead_slerp_amount = 1.000000
explosion_arch = explosion_li
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 43000.000000, 43000.000000, 230000.000000
angular_drag = 41000.000000, 41000.000000, 141000.000000
rotation_inertia = 8400.000000, 8400.000000, 8400.000000
nudge_force = 30000.000000
bay_door_anim = Sc_open baydoor
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 3

[CollisionGroup]
obj = Or_star_wing_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpStarboardwing
dmg_obj = or_elite_dmg_star_wing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Starboard_Wing
hit_pts = {oe_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {oe_wing_expl_resist}

[CollisionGroup]
obj = Or_port_wing_lod1
separable = true
parent_impulse = 240.000000
child_impulse = 7.000000
debris_type = debris_small_ship
dmg_hp = DpPortwing
dmg_obj = or_elite_dmg_port_wing_cap
separation_explosion = explosion_small_ship_breakoff
mass = 5.000000
type = Port_Wing
hit_pts = {oe_wing_hit_pts}
root_health_proxy = false
explosion_resistance = {oe_wing_expl_resist}

[CollisionGroup] 
obj = Or_Engine01_lod1
separable = true 
parent_impulse = 250.000000 
child_impulse = 7.000000 
debris_type = debris_small_ship 
dmg_hp = DpEngine01 
dmg_obj = or_elite_dmg_engine01 
separation_explosion = explosion_small_ship_breakoff 
mass = 5.000000 
type = Top_Engine 
hit_pts = {oe_engine1_hit_pts}
root_health_proxy = false 
explosion_resistance = {oe_engine1_expl_resist}

[CollisionGroup] 
obj = Or_Engine02_lod1
separable = true 
parent_impulse = 250.000000 
child_impulse = 7.000000 
debris_type = debris_small_ship 
dmg_hp = DpEngine01 
dmg_obj = or_elite_dmg_engine02 
separation_explosion = explosion_small_ship_breakoff 
mass = 5.000000 
type = Middle_Engine 
hit_pts = {oe_engine2_hit_pts}
root_health_proxy = false 
explosion_resistance = {oe_engine2_expl_resist}

[CollisionGroup] 
obj = Or_Engine03_lod1
separable = true 
parent_impulse = 250.000000 
child_impulse = 7.000000 
debris_type = debris_small_ship 
dmg_hp = DpEngine01 
dmg_obj = or_elite_dmg_engine03
separation_explosion = explosion_small_ship_breakoff 
mass = 5.000000 
type = Bottom_Engine 
hit_pts = {oe_engine3_hit_pts}
root_health_proxy = false 
explosion_resistance = {oe_engine3_expl_resist}

[Simple]
nickname = or_elite_dmg_star_wing_cap
DA_archetype = ships\\order\\or_elite\\or_elite_dmg_starboardwing.3db
material_library = Ships\\order\\or_ships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = or_elite_dmg_port_wing_cap
DA_archetype = ships\\order\\or_elite\\or_elite_dmg_portwing.3db
material_library = Ships\\order\\or_ships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = or_elite_dmg_engine01
DA_archetype = ships\\order\\or_elite\\or_elite_dmg_engine01.3db
material_library = Ships\\order\\or_ships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = or_elite_dmg_engine02
DA_archetype = ships\\order\\or_elite\\or_elite_dmg_engine02.3db
material_library = Ships\\order\\or_ships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Simple]
nickname = or_elite_dmg_engine03
DA_archetype = ships\\order\\or_elite\\or_elite_dmg_engine03.3db
material_library = Ships\\order\\or_ships.mat
mass = 5.000000
LODranges = 0, 200, 2000

[Ship] ;Li_Battleship
ids_name = 237043
ids_info = 66584
nickname = or_osiris
LODranges = 0, 10000, 25000, 50000
msg_id_prefix = gcs_refer_shiparch_Ordb
mission_property = can_use_large_moors
type = FIGHTER
DA_archetype = ships\\order\\or_osiris\\or_osiris.cmp
material_library = Ships\\order\\or_ships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
explosion_arch = explosion_li_dread
fuse = o_osiris_fuse, 0.500000, 1
fuse = or_osiris_burning_fuse01, 0.000000, 5000000
fuse = or_osiris_burning_fuse02, 0.000000, 2000000
fuse = or_osiris_burning_fuse03, 0.000000, 1000000
steering_torque = 250000000.000000, 250000000.000000, 250000000.000000
rotation_inertia = 200000000.000000, 4000000000, 4000000000 ; 25806999552.000000, 638700032.000000
angular_drag = 4000000000.000000, 4000000000.000000, 4000000000.000000
linear_drag = 2.000000
nudge_force = 360000.000000
mass = 100000.000000
hold_size = 5
bay_door_anim = Sc_open baydoor
bay_doors_open_snd = hanger_doors_opening
bay_doors_close_snd = hanger_doors_closing
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 1
hit_pts = 10000000
camera_offset = 50, 300
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 10
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 5
camera_turn_look_ahead_slerp_amount = 1.000000
cockpit = cockpits\\liberty\\li_dread.ini
nanobot_limit = 0 ; = 0
shield_battery_limit = 0 ; = 0
shield_link = l_fighter_shield01, HpMount, HpShield01
hp_type = hp_freighter_shield_special_1, HpShield01
hp_type = hp_turret_special_2, HpTurret_O3_01, HpTurret_O3_02, HpTurret_O4_02, HpTurret_O4_03
hp_type = hp_turret_special_3, HpTurret_O4_01, HpTurret_O4_04
hp_type = hp_turret_special_4, HpTurret_O1_01, HpTurret_O2_01

[CollisionGroup]
obj = Leaf01_d1_lod1
parent_impulse = 10.000000
child_impulse = 30.000000
separable = true
debris_type = cap_ship_piece
mass = 5.000000
;fuse = o_osiris_fuse, 1.000000, 1
separation_explosion = explosion_li
hit_pts = 200000
root_health_proxy = false

[CollisionGroup]
obj = Leaf02_d1_lod1
separable = true
debris_type = cap_ship_piece
mass = 5.000000
parent_impulse = 10.000000
child_impulse = 30.000000
;fuse = o_osiris_fuse, 1.000000, 1
separation_explosion = explosion_li
hit_pts = 200000
root_health_proxy = false

[CollisionGroup]
obj = Leaf03_d1_lod1
separable = true
debris_type = cap_ship_piece
mass = 5.000000
parent_impulse = 10.000000
child_impulse = 30.000000
;fuse = o_osiris_fuse, 1.000000, 1
separation_explosion = explosion_li
hit_pts = 200000
root_health_proxy = false

[CollisionGroup]
obj = Leaf04_d1_lod1
separable = true
debris_type = cap_ship_piece
mass = 5.000000
parent_impulse = 10.000000
child_impulse = 30.000000
;fuse = o_osiris_fuse, 1.000000, 1
separation_explosion = explosion_li
hit_pts = 200000
root_health_proxy = false

[CollisionGroup]
obj = Leaf05_d1_lod1
separable = true
debris_type = cap_ship_piece
mass = 5.000000
parent_impulse = 10.000000
child_impulse = 30.000000
;fuse = o_osiris_fuse, 1.000000, 1
separation_explosion = explosion_li
hit_pts = 200000
root_health_proxy = false

[CollisionGroup]
obj = Leaf06_d1_lod1
separable = true
debris_type = cap_ship_piece
mass = 5.000000
parent_impulse = 10.000000
child_impulse = 30.000000
;fuse = o_osiris_fuse, 1.000000, 1
separation_explosion = explosion_li
hit_pts = 200000
root_health_proxy = false

[CollisionGroup]
obj = Leaf07_d1_lod1
separable = true
debris_type = cap_ship_piece
mass = 5.000000
parent_impulse = 10.000000
child_impulse = 30.000000
;fuse = o_osiris_fuse, 1.000000, 1
separation_explosion = explosion_li
hit_pts = 200000
root_health_proxy = false

[CollisionGroup]
obj = Leaf08_d1_lod1
separable = true
debris_type = cap_ship_piece
mass = 5.000000
parent_impulse = 10.000000
child_impulse = 30.000000
;fuse = o_osiris_fuse, 1.000000, 1
separation_explosion = explosion_li
hit_pts = 200000
root_health_proxy = false

[CollisionGroup]
obj = osiris_nose_lod1
separable = true
debris_type = cap_ship_piece
mass = 10.000000
parent_impulse = 10.000000
child_impulse = 80.000000
fuse = o_osiris_fuse, 0.000000, 1
fuse = or_osiris_burning_fuse01, 0.000000, 17325
group_dmg_hp = DpNose
group_dmg_obj = or_osiris_head_dmg_cap
hit_pts = 69300
root_health_proxy = false

[CollisionGroup]
obj = osiris_interior_lod1
separable = true
debris_type = debris_vanish
mass = 10.000000
parent_impulse = 10.000000
child_impulse = 50.000000
fuse = o_osiris_fuse, 0.000000, 1
fuse = or_osiris_burning_fuse01, 0.000000, 5000000
separation_explosion = explosion_li
group_dmg_hp = DpNose
group_dmg_obj = or_osiris_head_dmg_cap
hit_pts = 10000000
root_health_proxy = false

[CollisionGroup]
obj = osiris_front_lod1
separable = true
debris_type = debris_vanish
mass = 10.000000
parent_impulse = 10.000000
child_impulse = 10.000000
fuse = o_osiris_fuse, 0.250000, 1
fuse = or_osiris_burning_fuse02, 0.000000, 2000000
dmg_hp = DpFront
dmg_obj = or_osiris_neck_dmg_cap
hit_pts = 20000000
root_health_proxy = false

[CollisionGroup]
obj = osiris_rear_lod1
separable = true
debris_type = debris_vanish
mass = 10.000000
parent_impulse = 10.000000
child_impulse = 10.000000
fuse = o_osiris_fuse, 0.750000, 1
fuse = or_osiris_burning_fuse04, 0.000000, 2000000
dmg_hp = DpRear
dmg_obj = or_osiris_butt_dmg_cap
hit_pts = 20000000
root_health_proxy = false

[CollisionGroup]
obj = osiris_cntrltwr_lod1
separable = true
debris_type = debris_vanish
mass = 10.000000
parent_impulse = 10.000000
child_impulse = 10.000000
dmg_hp = DpCntrltwr
dmg_obj = or_osiris_tower_cap
;fuse = o_osiris_fuse, 0.500000, 1
;fuse = or_osiris_burning_fuse03, 0.000000, 17325
separation_explosion = explosion_li
hit_pts = 500000
root_health_proxy = false

[CollisionGroup]
obj = osiris_shield_generator_lod1
separable = true
debris_type = debris_vanish
mass = 10.000000
parent_impulse = 10.000000
child_impulse = 10.000000
;fuse = o_osiris_fuse, 0.500000, 1
;fuse = or_osiris_burning_fuse02, 0.000000, 17325
dmg_hp = DpShieldgen
dmg_obj = or_osiris_shield_gen_cap
separation_explosion = explosion_li
hit_pts = 500000
root_health_proxy = false

[CollisionGroup]
obj = osiris_reactor_lod1
separable = true
debris_type = debris_vanish
mass = 10.000000
parent_impulse = 10.000000
child_impulse = 10.000000
fuse = o_osiris_fuse, 1.000000, 1
fuse = or_osiris_burning_fuse04, 0.000000, 2000000
hit_pts = 20000000
root_health_proxy = false

[CollisionGroup]
obj = osiris_reactor_core_lod1
separable = true
debris_type = cap_ship_piece
mass = 10.000000
parent_impulse = 10.000000
child_impulse = 300.000000
;fuse = o_osiris_fuse, 1.000000, 1
;fuse = or_osiris_burning_fuse04, 0.000000, 17325
group_dmg_hp = DpEngine
group_dmg_obj = or_osiris_engine_cap
separation_explosion = explosion_li
hit_pts = 2000000
root_health_proxy = false

[CollisionGroup]
obj = osiris_engine_lod1
separable = true
debris_type = debris_vanish
mass = 10.000000
parent_impulse = 10.000000
child_impulse = 50.000000
;fuse = o_osiris_fuse, 1.000000, 1
;fuse = or_osiris_burning_fuse04, 0.000000, 17325
separation_explosion = explosion_li
hit_pts = 1000000
root_health_proxy = false

[Simple]
nickname = or_osiris_head_dmg_cap
DA_archetype = ships\\order\\or_osiris\\or_osiris_dmg_nose.3db
material_library = Ships\\order\\or_ships.mat
mass = 10.000000
hit_pts = 200
LODranges = 0, 20000

[Simple]
nickname = or_osiris_neck_dmg_cap
DA_archetype = ships\\order\\or_osiris\\or_osiris_dmg_front.3db
material_library = Ships\\order\\or_ships.mat
mass = 10.000000
hit_pts = 200
LODranges = 0, 20000

[Simple]
nickname = or_osiris_butt_dmg_cap
DA_archetype = ships\\order\\or_osiris\\or_osiris_dmg_rear.3db
material_library = Ships\\order\\or_ships.mat
mass = 10.000000
hit_pts = 200
LODranges = 0, 20000

[Simple]
nickname = or_osiris_tower_cap
DA_archetype = ships\\order\\or_osiris\\or_osiris_dmg_cntrltwr.3db
material_library = Ships\\order\\or_ships.mat
mass = 10.000000
hit_pts = 200
LODranges = 0, 20000

[Simple]
nickname = or_osiris_shield_gen_cap
DA_archetype = ships\\order\\or_osiris\\or_osiris_dmg_sheild_generator.3db
material_library = Ships\\order\\or_ships.mat
mass = 10.000000
hit_pts = 200
LODranges = 0, 20000

[Simple]
nickname = or_osiris_engine_cap
DA_archetype = ships\\order\\or_osiris\\or_osiris_dmg_engine.3db
material_library = Ships\\order\\or_ships.mat
mass = 10.000000
hit_pts = 200
LODranges = 0, 20000

[Ship]
ids_name = 237039
ids_info = 66579
nickname = no_fighter
LODranges = 0, 1000, 5000, 10000
type = FIGHTER
DA_archetype = ships\\nomad\\no_fighter\\no_fighter.3db
material_library = ships\\nomad\\nomad_fx.txm
nomad = true
cockpit = cockpits\\liberty\\l_elite.ini
mass = 50.000000
hold_size = 1
linear_drag = 1.000000
explosion_arch = explosion_no_elite
surface_hit_effects = 0, small_nomad_hull_hit_light01, small_nomad_hull_hit_light02, small_nomad_hull_hit_light03
surface_hit_effects = 150, small_nomad_hull_hit_medium01, small_nomad_hull_hit_medium02, small_nomad_hull_hit_medium03
surface_hit_effects = 300, small_nomad_hull_hit_heavy01, small_nomad_hull_hit_heavy02, small_nomad_hull_hit_heavy03
steering_torque = 43000.000000, 43000.000000, 58000.000000
angular_drag = 41000.000000, 41000.000000, 41000.000000
rotation_inertia = 8400.000000, 8400.000000, 8400.000000
nudge_force = 30000.000000
HP_tractor_source = HpMount
num_exhaust_nozzles = 1
hit_pts = 30000

[Ship]
ids_name = 237040
ids_info = 66580
nickname = no_gunboat
LODranges = 0, 5000, 10000, 25000
type = GUNBOAT
DA_archetype = ships\\nomad\\no_gunship\\no_gunship.3db
material_library = ships\\nomad\\nomad_fx.txm
nomad = true
mass = 1000.000000
hold_size = 1
explosion_arch = explosion_no_gunboat
fuse = fuse_no_gunboat_death, 0.000000, 1
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
linear_drag = 1.000000
steering_torque = 60000000.000000, 60000000.000000, 60000000.000000
angular_drag = 120000000.000000, 120000000.000000, 120000000.000000
rotation_inertia = 16800000.000000, 16800000.000000, 16800000.000000
nudge_force = 150000.000000
HP_tractor_source = HpMount
num_exhaust_nozzles = 1
hit_pts = 10000

[Ship]
ids_name = 237038
ids_info = 66578
nickname = no_battleship
LODranges = 0, 10000, 30000, 40000, 50000
type = CAPITAL
DA_archetype = ships\\nomad\\no_battleship\\no_battleship.3db
material_library = ships\\nomad\\nomad_fx.txm
nomad = true
hold_size = 1
explosion_arch = explosion_no_battleship
fuse = fuse_no_battleship_death, 0.000000, 1
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
linear_drag = 1.000000
mass = 100000.000000
steering_torque = 1501900032.000000, 1501900032.000000, 1501900032.000000
angular_drag = 13200000000.000000, 13200000000.000000, 13200000000.000000
rotation_inertia = 15000000512.000000, 15000000512.000000, 15000000512.000000
nudge_force = 3000000.000000
HP_tractor_source = HpMount
num_exhaust_nozzles = 1
hit_pts = 69300

[Ship]
ids_name = 237036
ids_info = 66576
nickname = ge_liner
LODranges = 0, 10000, 20000, 50000
msg_id_prefix = gcs_refer_shiparch_luxliner
mission_property = can_use_large_moors
type = CAPITAL
DA_archetype = ships\\utility\\luxury_liner\\luxury_liner.cmp
material_library = ships\\utility\\utility_liner.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
linear_drag = 1.000000
mass = 5000.000000
hold_size = 5000
hit_pts = 69300
explosion_arch = explosion_instant
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 20000000.000000, 20000000.000000, 20000000.000000
angular_drag = 132000000.000000, 132000000.000000, 132000000.000000
rotation_inertia = 40000000.000000, 40000000.000000, 40000000.000000
nudge_force = 360000.000000
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
bay_door_anim = Sc_open bay
bay_doors_open_snd = hanger_doors_opening
bay_doors_close_snd = hanger_doors_closing
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 1
fuse = fuse_ge_liner_death, 0.000000, 1
max_bank_angle = 5
camera_offset = 50, 160
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 20
camera_turn_look_ahead_slerp_amount = 1.000000
cockpit = cockpits\\bretonia\\br_destroyer.ini
nanobot_limit = 0 ; = 0
shield_battery_limit = 0 ; = 0

[CollisionGroup]
obj = liner_frnt_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 2000.000000
debris_type = cap_ship_piece2
mass = 50.000000
fuse = fuse_ge_prison_death, 0.000000, 1
group_dmg_hp = DpFrnt
group_dmg_obj = ge_luxury_frnt_dmg_cap
hit_pts = 69300
root_health_proxy = false

[CollisionGroup]
obj = liner_mid_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 2000.000000
debris_type = debris_vanish
mass = 50.000000
fuse = fuse_ge_prison_death, 0.000000, 1
dmg_hp = DpMid
dmg_obj = ge_luxury_mid_dmg_cap
hit_pts = 69300
root_health_proxy = false

[CollisionGroup]
obj = liner_rear_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 2000.000000
debris_type = debris_vanish
mass = 50.000000
fuse = fuse_ge_prison_death, 0.000000, 1
dmg_hp = DpRear
dmg_obj = ge_luxury_rear_dmg_cap
hit_pts = 69300
root_health_proxy = false

[CollisionGroup]
obj = liner_reactor_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 2000.000000
debris_type = cap_ship_piece2
mass = 50.000000
fuse = fuse_ge_prison_death, 0.000000, 1
group_dmg_hp = DpReactor
group_dmg_obj = ge_luxury_reactor_dmg_cap
hit_pts = 69300
root_health_proxy = false

[Simple]
nickname = ge_luxury_frnt_dmg_cap
DA_archetype = Ships\\utility\\luxury_liner\\liner_dmg_frnt.3db
material_library = ships\\utility\\utility_liner.mat
mass = 1000.000000
LODranges = 0, 20000

[Simple]
nickname = ge_luxury_mid_dmg_cap
DA_archetype = Ships\\utility\\luxury_liner\\liner_dmg_mid.3db
material_library = ships\\utility\\utility_liner.mat
mass = 1000.000000
LODranges = 0, 20000

[Simple]
nickname = ge_luxury_reactor_dmg_cap
DA_archetype = Ships\\utility\\luxury_liner\\liner_dmg_reactor.3db
material_library = ships\\utility\\utility_liner.mat
mass = 1000.000000
LODranges = 0, 20000

[Simple]
nickname = ge_luxury_rear_dmg_cap
DA_archetype = Ships\\utility\\luxury_liner\\liner_dmg_rear.3db
material_library = ships\\utility\\utility_liner.mat
mass = 1000.000000
LODranges = 0, 20000

[Ship]
ids_name = 237047
ids_info = 66594
nickname = ge_prison
LODranges = 0, 10000, 20000, 50000
msg_id_prefix = gcs_refer_shiparch_pliner
mission_property = can_use_large_moors
type = CAPITAL
DA_archetype = Ships\\utility\\prison_liner\\prison_liner.cmp
material_library = ships\\utility\\utility_liner.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
linear_drag = 1.000000
mass = 5000.000000
hold_size = 5000
hit_pts = 69300
explosion_arch = explosion_rh_battleship
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 20000000.000000, 20000000.000000, 20000000.000000
angular_drag = 132000000.000000, 132000000.000000, 132000000.000000
rotation_inertia = 40000000.000000, 40000000.000000, 40000000.000000
nudge_force = 1.000000
bay_door_anim = Sc_prison_liner
bay_doors_open_snd = hanger_doors_opening
bay_doors_close_snd = hanger_doors_closing
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 1
fuse = prison_burning_fuse, 0.000000, -1
fuse = prison_m01b_damage_fuse, 0.000000, -1
fuse = fuse_ge_prison_death, 0.000000, 1

[CollisionGroup]
obj = prison_frnt_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 2000.000000
debris_type = cap_ship_piece2
mass = 50.000000
fuse = fuse_ge_prison_death, 0.000000, 1
group_dmg_hp = DpFrnt
group_dmg_obj = ge_prison_frnt_dmg_cap
hit_pts = 69300
root_health_proxy = false

[CollisionGroup]
obj = prison_mid_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 2000.000000
debris_type = debris_vanish
mass = 50.000000
fuse = fuse_ge_prison_death, 0.000000, 1
dmg_hp = DpMid
dmg_obj = ge_prison_mid_dmg_cap
hit_pts = 69300
root_health_proxy = false

[CollisionGroup]
obj = prison_rear_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 2000.000000
debris_type = debris_vanish
mass = 50.000000
fuse = fuse_ge_prison_death, 0.000000, 1
dmg_hp = DpRear
dmg_obj = ge_prison_rear_dmg_cap
hit_pts = 69300
root_health_proxy = false

[CollisionGroup]
obj = prison_reactor_lod1
separable = true
parent_impulse = 60.000000
child_impulse = 2000.000000
debris_type = cap_ship_piece2
mass = 50.000000
fuse = fuse_ge_prison_death, 0.000000, 1
group_dmg_hp = DpReactor
group_dmg_obj = ge_prison_reactor_dmg_cap
hit_pts = 69300
root_health_proxy = false

[Simple]
nickname = ge_prison_frnt_dmg_cap
DA_archetype = Ships\\utility\\prison_liner\\prison_dmg_frnt.3db
material_library = ships\\utility\\utility_liner.mat
mass = 1000.000000
LODranges = 0, 20000

[Simple]
nickname = ge_prison_mid_dmg_cap
DA_archetype = Ships\\utility\\prison_liner\\prison_dmg_mid.3db
material_library = ships\\utility\\utility_liner.mat
mass = 1000.000000
LODranges = 0, 20000

[Simple]
nickname = ge_prison_reactor_dmg_cap
DA_archetype = Ships\\utility\\prison_liner\\prison_dmg_reactor.3db
material_library = ships\\utility\\utility_liner.mat
mass = 1000.000000
LODranges = 0, 20000

[Simple]
nickname = ge_prison_rear_dmg_cap
DA_archetype = Ships\\utility\\prison_liner\\prison_dmg_rear.3db
material_library = ships\\utility\\utility_liner.mat
mass = 1000.000000
LODranges = 0, 20000

[Ship]
ids_name = 237037
ids_info = 66577
nickname = ge_miner
LODranges = 0, 10000, 50000
msg_id_prefix = gcs_refer_shiparch_mining
mission_property = can_use_large_moors
type = FIGHTER
DA_archetype = ships\\utility\\mining\\mining.cmp
material_library = ships\\utility\\utility_ships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
linear_drag = 10000.000000
mass = 50000.000000
hold_size = 1000
hit_pts = 50000
explosion_arch = explosion_asteroid_miner
steering_torque = 20000000.000000, 20000000.000000, 20000000.000000
angular_drag = 132000000.000000, 132000000.000000, 132000000.000000
rotation_inertia = 40000000.000000, 40000000.000000, 40000000.000000
nudge_force = 400000.000000
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 8
fuse = miner_death_fuse, 0.000000, 1
camera_offset = 30, 200
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 10
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 5
camera_turn_look_ahead_slerp_amount = 1.000000
cockpit = cockpits\\utility\\ge_miner.ini
nanobot_limit = 0 ; = 0
shield_battery_limit = 0 ; = 0
hp_type = hp_turret_special_1, HpTurret_U1_01, HpTurret_U1_02
hp_type = hp_turret_special_2, HpTurret_U3_01, HpTurret_U3_02
hp_type = hp_turret_special_3, HpTurret_U2_01, HpTurret_U2_02

[Ship]
ids_name = 237048
ids_info = 66595
nickname = ge_repair
LODranges = 0, 10000, 25000
msg_id_prefix = gcs_refer_shiparch_repair
mission_property = can_use_med_moors
type = FREIGHTER
DA_archetype = ships\\utility\\repair\\repair.cmp
material_library = ships\\utility\\utility_ships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
linear_drag = 184.000000
mass = 400.000000
hold_size = 150
hit_pts = 55000
explosion_arch = shatter_utility_small
steering_torque = 25000.000000, 25000.000000, 25000.000000
angular_drag = 100000.000000, 100000.000000, 100000.000000
rotation_inertia = 48000.000000, 48000.000000, 48000.000000
nudge_force = 3000.000000
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2
camera_offset = 8, 34
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 17
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 25
camera_turn_look_ahead_slerp_amount = 1.000000
cockpit = cockpits\\liberty\\l_elite.ini
pilot_mesh = generic_pilot
nanobot_limit = 0 ; = 0
shield_battery_limit = 0 ; = 0
hp_type = hp_turret_special_9, HpTurret01, HpTurret02

[Ship]
ids_name = 237024
ids_info = 66552
nickname = ge_lifter
LODranges = 0, 10000, 20000
msg_id_prefix = gcs_refer_shiparch_hlifter
mission_property = can_use_large_moors
type = FIGHTER
DA_archetype = ships\\utility\\heavy_lifter\\heavy_lifter.cmp
material_library = ships\\utility\\utility_ships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
linear_drag = 1.000000
mass = 1000.000000
hold_size = 250
hit_pts = 75000
;explosion_arch = shatter_utility
explosion_arch = explosion_li_cruiser
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 25000.000000, 25000.000000, 25000.000000
angular_drag = 100000.000000, 100000.000000, 100000.000000
rotation_inertia = 48000.000000, 48000.000000, 48000.000000
nudge_force = 100000.000000
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 6
fuse = lifter_death_fuse, 0.000000, 1

[CollisionGroup]
obj = lifter_clamp01_lod1
separable = true
child_impulse = 1.000000
parent_impulse = 60.000000
debris_type = debris_normal
fuse = lifter_death_fuse, 0.000000, 1
hit_pts = 400
root_health_proxy = false

[Ship]
{ship_ge_armored}
LODranges = 0, 2000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_atransport
mission_property = can_use_berths
;cockpit = cockpits\\CIVILIAN\\ge_armored.ini
type = FREIGHTER
DA_archetype = ships\\utility\\transport_armored\\transport_armored_beta.cmp
material_library = ships\\utility\\utility_misc.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
pilot_mesh = generic_pilot
linear_drag = 1.000000
max_bank_angle = 5 ;35 
camera_offset = 20, 78 
camera_angular_acceleration = 0.050000 
camera_horizontal_turn_angle = 10 
camera_vertical_turn_up_angle = 5 
camera_vertical_turn_down_angle = 20 
camera_turn_look_ahead_slerp_amount = 1.000000 
explosion_arch = explosion_li 
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03

steering_torque = 50000.000000, 50000.000000, 50000.000000
angular_drag = 100000.000000, 100000.000000, 100000.000000
rotation_inertia = 60000.000000, 60000.000000, 60000.000000
nudge_force = 150000.000000
bay_door_anim = Sc_open
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2

[Ship]
ids_name = 237057
ids_info = 66611
nickname = ge_transport2
msg_id_prefix = gcs_refer_shiparch_htransport
mission_property = can_use_med_moors
LODranges = 0, 1000, 5000, 10000
type = FIGHTER
DA_archetype = ships\\utility\\transport_small\\transport_small.cmp
material_library = ships\\utility\\utility_transport.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
fuse = transport_death_fuse, 0.000000, 1
fuse = intermed_damage_transport01, 0.000000, 5000
fuse = intermed_damage_transport02, 0.000000, 375
linear_drag = 1.000000
mass = 1000.000000
hold_size = 2
explosion_arch = explosion_instant
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 300, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 600, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 7000000.000000, 7000000.000000, 3000000.000000
angular_drag = 25000000.000000, 25000000.000000, 25000000.000000
rotation_inertia = 1250000.000000, 12000000.000000, 12000000.000000
nudge_force = 150000.000000
HP_bay_surface = HpRunningLight08
HP_bay_external = HpMount
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 5
hit_pts = 100000
camera_offset = 40, 100
camera_angular_acceleration = 0.035000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 20
camera_turn_look_ahead_slerp_amount = 1.000000
cockpit = cockpits\\rheinland\\r_gunboat.ini
hp_type = hp_turret_special_1, HpTurret_U1_01, HpTurret_U1_02, HpTurret_U1_03, HpTurret_U1_04, HpTurret_U3_01
hp_type = hp_cargo_pod, HpCargo01, HpCargo02
hp_type = hp_fighter_shield_special_1, HpCargo01, HpCargo02

[CollisionGroup]
obj = trans_frnt_lod1
mass = 20.000000
separable = true
parent_impulse = 60
child_impulse = 400
group_dmg_hp = DpFrnt
group_dmg_obj = transport_dmg_frnt_cap
debris_type = cap_ship_piece
fuse = transport_death_fuse, 0.000000, 1
hit_pts = 20000
root_health_proxy = true

[CollisionGroup]
obj = trans_rear_lod1
separable = true
parent_impulse = 60
child_impulse = 200
group_dmg_hp = DpMain
group_dmg_obj = transport_dmg_main_cap
debris_type = cap_ship_piece
fuse = transport_death_fuse, 0.000000, 1
hit_pts = 20000
root_health_proxy = true

[CollisionGroup]
obj = trans_cntrl_twr_lod1
separable = true
child_impulse = 1.000000
parent_impulse = 60.000000
debris_type = debris_vanish
dmg_hp = DpCntrl_twr
dmg_obj = transport_dmg_twr_cap
;fuse = transport_death_fuse, 0.000000, 1
separation_explosion = explosion_li
hit_pts = 20000
root_health_proxy = false

[CollisionGroup]
obj = trans_eng_lod1
separable = true
child_impulse = 1.000000
parent_impulse = 60.000000
debris_type = debris_vanish
dmg_hp = DpEng
dmg_obj = transport_dmg_eng_cap
;fuse = transport_death_fuse, 0.000000, 1
separation_explosion = explosion_li
hit_pts = 20000
root_health_proxy = false

[CollisionGroup]
obj = trans_port_eng_lod1
separable = true
child_impulse = 1.000000
parent_impulse = 60.000000
debris_type = debris_vanish
dmg_hp = DpPort_eng
dmg_obj = transport_dmg_port_eng_cap
;fuse = transport_port_eng_fuse, 0.000000, 1
separation_explosion = explosion_li
hit_pts = 20000
root_health_proxy = false

[CollisionGroup]
obj = trans_star_eng_lod1
separable = true
child_impulse = 1.000000
parent_impulse = 60.000000
debris_type = debris_vanish
dmg_hp = DpStar_eng
dmg_obj = transport_dmg_star_eng_cap
;fuse = transport_star_eng_fuse, 0.000000, 1
separation_explosion = explosion_li
hit_pts = 20000
root_health_proxy = false

[CollisionGroup]
obj = trans_tail_fin_lod1
mass = 20.000000
separable = true
child_impulse = 2000.000000
parent_impulse = 12000.000000
debris_type = debris_vanish
dmg_hp = DpTail
dmg_obj = transport_dmg_fin_cap
;fuse = transport_death_fuse, 0.000000, 1
separation_explosion = explosion_li
hit_pts = 5000
root_health_proxy = false

[Simple]
nickname = transport_dmg_twr_cap
DA_archetype = Ships\\utility\\transport_small\\trans_cntrl_twr_dmg.3db
material_library = ships\\utility\\utility_transport.mat
mass = 5.000000
LODranges = 0, 7000

[Simple]
nickname = transport_dmg_frnt_cap
DA_archetype = Ships\\utility\\transport_small\\trans_mid_frnt_dmg.3db
material_library = ships\\utility\\utility_transport.mat
mass = 5.000000
LODranges = 0, 7000

[Simple]
nickname = transport_dmg_fin_cap
DA_archetype = Ships\\utility\\transport_small\\trans_tail_fin_dmg.3db
material_library = ships\\utility\\utility_transport.mat
mass = 5.000000
LODranges = 0, 7000

[Simple]
nickname = transport_dmg_main_cap
DA_archetype = Ships\\utility\\transport_small\\trans_mid_rear_dmg.3db
material_library = ships\\utility\\utility_transport.mat
mass = 5.000000
LODranges = 0, 7000

[Simple]
nickname = transport_dmg_port_eng_cap
DA_archetype = Ships\\utility\\transport_small\\trans_port_eng_dmg.3db
material_library = ships\\utility\\utility_transport.mat
mass = 5.000000
LODranges = 0, 7000

[Simple]
nickname = transport_dmg_star_eng_cap
DA_archetype = Ships\\utility\\transport_small\\trans_star_eng_dmg.3db
material_library = ships\\utility\\utility_transport.mat
mass = 5.000000
LODranges = 0, 7000

[Simple]
nickname = transport_dmg_eng_cap
DA_archetype = Ships\\utility\\transport_small\\trans_eng_dmg.3db
material_library = ships\\utility\\utility_transport.mat
mass = 5.000000
LODranges = 0, 7000

[Ship]
ids_name = 237057
ids_info = 66611
nickname = ge_transport
msg_id_prefix = gcs_refer_shiparch_htransport
mission_property = can_use_med_moors
LODranges = 0, 1000, 5000, 10000
type = FIGHTER
DA_archetype = ships\\utility\\transport_small\\transport_small.cmp
material_library = ships\\utility\\utility_transport.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
fuse = transport_death_fuse, 0.000000, 1
fuse = intermed_damage_transport01, 0.000000, 5000
fuse = intermed_damage_transport02, 0.000000, 375
linear_drag = 1.000000
mass = 5000.000000
hold_size = 5000
explosion_arch = explosion_ge_transport
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 300, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 600, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 700000.000000, 700000.000000, 300000.000000
angular_drag = 2500000.000000, 2500000.000000, 2500000.000000
rotation_inertia = 1200000.000000, 1200000.000000, 1200000.000000
nudge_force = 150000.000000
HP_bay_surface = HpRunningLight08
HP_bay_external = HpMount
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 3
hit_pts = 100000
camera_offset = 40, 100
camera_angular_acceleration = 0.035000
camera_horizontal_turn_angle = 20
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 20
camera_turn_look_ahead_slerp_amount = 1.000000
cockpit = cockpits\\rheinland\\r_gunboat.ini
hp_type = hp_turret_special_1, HpTurret_U1_01, HpTurret_U1_02, HpTurret_U1_03, HpTurret_U1_04, HpTurret_U3_01
hp_type = hp_cargo_pod, HpCargo01, HpCargo02

[CollisionGroup]
obj = trans_frnt_lod1
mass = 80.000000
separable = true
parent_impulse = 60
child_impulse = 400
group_dmg_hp = DpFrnt
group_dmg_obj = transport_dmg_frnt_cap
debris_type = cap_ship_piece
fuse = transport_death_fuse, 0.000000, 1
hit_pts = 20000
root_health_proxy = false

[CollisionGroup]
obj = trans_rear_lod1
separable = true
parent_impulse = 60
child_impulse = 200
group_dmg_hp = DpMain
group_dmg_obj = transport_dmg_main_cap
debris_type = cap_ship_piece
fuse = transport_death_fuse, 0.000000, 1
hit_pts = 20000
root_health_proxy = false

[CollisionGroup]
obj = trans_cntrl_twr_lod1
separable = true
child_impulse = 1.000000
parent_impulse = 60.000000
debris_type = debris_vanish
dmg_hp = DpCntrl_twr
dmg_obj = transport_dmg_twr_cap
;fuse = transport_death_fuse, 0.000000, 1
separation_explosion = explosion_li
hit_pts = 20000
root_health_proxy = false

[CollisionGroup]
obj = trans_eng_lod1
separable = true
child_impulse = 1.000000
parent_impulse = 60.000000
debris_type = debris_vanish
dmg_hp = DpEng
dmg_obj = transport_dmg_eng_cap
;fuse = transport_death_fuse, 0.000000, 1
separation_explosion = explosion_li
hit_pts = 20000
root_health_proxy = false

[CollisionGroup]
obj = trans_port_eng_lod1
separable = true
child_impulse = 1.000000
parent_impulse = 60.000000
debris_type = debris_vanish
dmg_hp = DpPort_eng
dmg_obj = transport_dmg_port_eng_cap
;fuse = transport_port_eng_fuse, 0.000000, 1
separation_explosion = explosion_li
hit_pts = 20000
root_health_proxy = false

[CollisionGroup]
obj = trans_star_eng_lod1
separable = true
child_impulse = 1.000000
parent_impulse = 60.000000
debris_type = debris_vanish
dmg_hp = DpStar_eng
dmg_obj = transport_dmg_star_eng_cap
;fuse = transport_star_eng_fuse, 0.000000, 1
separation_explosion = explosion_li
hit_pts = 20000
root_health_proxy = false

[CollisionGroup]
obj = trans_tail_fin_lod1
mass = 20.000000
separable = true
child_impulse = 2000.000000
parent_impulse = 12000.000000
debris_type = debris_vanish
dmg_hp = DpTail
dmg_obj = transport_dmg_fin_cap
;fuse = transport_death_fuse, 0.000000, 1
separation_explosion = explosion_li
hit_pts = 10000
root_health_proxy = false

[Ship]
ids_name = 237058
ids_info = 66612
nickname = ge_large_transport
LODranges = 0, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_stransport
mission_property = can_use_med_moors
type = TRANSPORT
DA_archetype = ships\\utility\\transport_large\\transport_large.cmp
material_library = ships\\utility\\utility_transport.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
fuse = transport_death_fuse, 0.000000, 1
fuse = intermed_damage_transport01, 0.000000, 750
fuse = intermed_damage_transport02, 0.000000, 375
explosion_arch = explosion_instant
hp_type = hp_turret, HpTurret_U1_01, HpTurret_U1_02, HpTurret_U1_03, HpTurret_U1_04, HpTurret_U3_01
hp_type = hp_cargo_pod, HpCargo01, HpCargo02, HpCargo03, HpCargo04
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 1000000.000000, 1000000.000000, 500000.000000
angular_drag = 5000000.000000, 5000000.000000, 5000000.000000
rotation_inertia = 2424000.000000, 2424000.000000, 2424000.000000
linear_drag = 1.000000
nudge_force = 150000.000000
mass = 1000.000000
hold_size = 10000
HP_bay_surface = HpRunningLight08
HP_bay_external = HpMount
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 1
hit_pts = 3000

[CollisionGroup]
obj = trans_frnt_lod1
mass = 80.000000
separable = true
parent_impulse = 60.000000
child_impulse = 400.000000
group_dmg_hp = DpFrnt
group_dmg_obj = transport_dmg_frnt_cap
debris_type = cap_ship_piece
fuse = transport_death_fuse, 0.000000, 1
hit_pts = 3000
root_health_proxy = false

[CollisionGroup]
obj = trans_rear_lod1
separable = true
parent_impulse = 60
child_impulse = 200
group_dmg_hp = DpMain
group_dmg_obj = transport_dmg_main_cap
debris_type = cap_ship_piece
fuse = transport_death_fuse, 0.000000, 1
hit_pts = 3000
root_health_proxy = false

[CollisionGroup]
obj = trans_cntrl_twr_lod1
separable = true
child_impulse = 1.000000
parent_impulse = 60.000000
debris_type = debris_vanish
dmg_hp = DpCntrl_twr
dmg_obj = transport_dmg_twr_cap
fuse = transport_death_fuse, 0.000000, 1
hit_pts = 3000
root_health_proxy = false

[CollisionGroup]
obj = trans_eng_lod1
separable = true
child_impulse = 1.000000
parent_impulse = 60.000000
debris_type = debris_vanish
dmg_hp = DpEng
dmg_obj = transport_dmg_eng_cap
root_health_proxy = false
hit_pts = 3000

[CollisionGroup]
obj = trans_port_eng_lod1
separable = true
child_impulse = 1.000000
parent_impulse = 60.000000
debris_type = debris_vanish
dmg_hp = DpPort_eng
dmg_obj = transport_dmg_port_eng_cap
fuse = transport_death_fuse, 0.000000, 1
hit_pts = 700
root_health_proxy = false

[CollisionGroup]
obj = trans_star_eng_lod1
separable = true
child_impulse = 1.000000
parent_impulse = 60.000000
debris_type = debris_vanish
dmg_hp = DpStar_eng
dmg_obj = transport_dmg_star_eng_cap
fuse = transport_death_fuse, 0.000000, 1
hit_pts = 700
root_health_proxy = false

[CollisionGroup]
obj = trans_tail_fin_lod1
mass = 20.000000
separable = true
child_impulse = 2000.000000
parent_impulse = 12000.000000
debris_type = debris_vanish
dmg_hp = DpTail
dmg_obj = transport_dmg_fin_cap
fuse = transport_death_fuse, 0.000000, 1
hit_pts = 350
root_health_proxy = false

[Ship]
ids_name = 237055
ids_info = 66609
nickname = ge_train
LODranges = 0, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_ctransport
mission_property = can_use_med_moors
type = TRANSPORT
DA_archetype = ships\\utility\\freight_train\\freight_trainx2.3db
material_library = ships\\utility\\utility_misc.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
linear_drag = 1.000000
mass = 500.000000
hold_size = 20000
explosion_arch = explosion_cap_ship1
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
hp_type = hp_turret, HpTurret01, HpTurret02, HpTurret03, HpTurret04, HpTurret05, HpTurret06
hp_type = hp_cargo_pod, HpCargo01, HpCargo02, HpCargo03, HpCargo04
steering_torque = 190000.000000, 190000.000000, 90000.000000
angular_drag = 900000.000000, 900000.000000, 900000.000000
rotation_inertia = 600000.000000, 600000.000000, 600000.000000
nudge_force = 150000.000000
HP_bay_surface = HpCargo01
HP_bay_external = HpCargo02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2
fuse = train_transport_death_fuse, 0.000000, 1
fuse = intermed_damage_train01, 0.000000, 2625
fuse = intermed_damage_train02, 0.000000, 1313
hit_pts = 10500

[Ship]
ids_name = 237056
ids_info = 66610
nickname = ge_large_train
LODranges = 0, 1000, 4000, 6000
msg_id_prefix = gcs_refer_shiparch_ctransport
mission_property = can_use_med_moors
type = TRANSPORT
DA_archetype = ships\\utility\\freight_train\\freight_trainx3.3db
material_library = ships\\utility\\utility_misc.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
linear_drag = 1.000000
mass = 1000.000000
hold_size = 30000
explosion_arch = explosion_li_cruiser
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
hp_type = hp_turret, HpTurret01, HpTurret02, HpTurret03, HpTurret04, HpTurret05, HpTurret06
hp_type = hp_cargo_pod, HpCargo01, HpCargo02, HpCargo03, HpCargo04, HpCargo05, HpCargo06
steering_torque = 190000.000000, 190000.000000, 90000.000000
angular_drag = 900000.000000, 900000.000000, 900000.000000
rotation_inertia = 600000.000000, 600000.000000, 600000.000000
nudge_force = 150000.000000
HP_bay_surface = HpCargo01
HP_bay_external = HpCargo02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2
fuse = train_transport_death_fuse, 0.000000, 1
fuse = intermed_damage_train01, 0.000000, 500000
fuse = intermed_damage_train02, 0.000000, 250000
hit_pts = 150000

[;CollisionGroup]
obj = Engine02_lod1
separable = true
child_impulse = 1.000000
parent_impulse = 60.000000
debris_type = debris_vanish
dmg_hp = DpPort_eng
dmg_obj = transport_dmg_port_eng_cap
hit_pts = 25000
root_health_proxy = false

[;CollisionGroup]
obj = Engine01_lod1
separable = true
child_impulse = 1.000000
parent_impulse = 60.000000
debris_type = debris_vanish
dmg_hp = DpStar_eng
dmg_obj = transport_dmg_star_eng_cap
hit_pts = 25000
root_health_proxy = false

[Ship]
{ship_ge_csv}
LODranges = 0, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_support
mission_property = can_use_berths
type = FIGHTER
DA_archetype = ships\\utility\\csv\\csv.cmp
material_library = ships\\utility\\utility_ships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
linear_drag = 1.000000
explosion_arch = explosion_li
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 33000.000000, 33000.000000, 230000.000000
angular_drag = 41000.000000, 41000.000000, 141000.000000
rotation_inertia = 8400.000000, 8400.000000, 8400.000000
nudge_force = 30000.000000
bay_door_anim = Sc_open door
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 1
pilot_mesh = generic_pilot
camera_offset = 10, 30
;camera_offset = 12, 46 
camera_angular_acceleration = 0.050000 
camera_horizontal_turn_angle = 25 
camera_vertical_turn_up_angle = 5 
camera_vertical_turn_down_angle = 25 
camera_turn_look_ahead_slerp_amount = 1.000000 
cockpit = cockpits\\liberty\\or_elite.ini 

[Ship]
{ship_ge_csv2}
LODranges = 0, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_support
mission_property = can_use_berths
type = FIGHTER
DA_archetype = ships\\utility\\csv\\csv.cmp
material_library = ships\\utility\\utility_ships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
linear_drag = 1.000000
explosion_arch = explosion_li
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 33000.000000, 33000.000000, 230000.000000
angular_drag = 41000.000000, 41000.000000, 141000.000000
rotation_inertia = 8400.000000, 8400.000000, 8400.000000
nudge_force = 30000.000000
bay_door_anim = Sc_open door
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 1
pilot_mesh = generic_pilot
camera_offset = 10, 30
;camera_offset = 12, 46 
camera_angular_acceleration = 0.050000 
camera_horizontal_turn_angle = 25 
camera_vertical_turn_up_angle = 5 
camera_vertical_turn_down_angle = 25 
camera_turn_look_ahead_slerp_amount = 1.000000 
cockpit = cockpits\\liberty\\or_elite.ini 

[Ship]
{ship_ge_csv3}
LODranges = 0, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_support
mission_property = can_use_berths
type = FIGHTER
DA_archetype = ships\\utility\\csv\\csv.cmp
material_library = ships\\utility\\utility_ships.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
linear_drag = 1.000000
explosion_arch = explosion_li
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 33000.000000, 33000.000000, 230000.000000
angular_drag = 41000.000000, 41000.000000, 141000.000000
rotation_inertia = 8400.000000, 8400.000000, 8400.000000
nudge_force = 30000.000000
bay_door_anim = Sc_open door
bay_doors_open_snd = cargo_doors_open
bay_doors_close_snd = cargo_doors_close
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 1
pilot_mesh = generic_pilot
camera_offset = 10, 30
;camera_offset = 12, 46 
camera_angular_acceleration = 0.050000 
camera_horizontal_turn_angle = 25 
camera_vertical_turn_up_angle = 5 
camera_vertical_turn_down_angle = 25 
camera_turn_look_ahead_slerp_amount = 1.000000 
cockpit = cockpits\\liberty\\or_elite.ini 

[Ship]
ids_name = 237001
ids_info = 66493
nickname = ge_armored_nobay
LODranges = 0, 1000, 5000, 10000
msg_id_prefix = gcs_refer_shiparch_atransport
mission_property = can_use_berths
type = TRANSPORT
DA_archetype = ships\\utility\\transport_armored\\transport_armored_nobay.3db
material_library = ships\\utility\\utility_misc.mat
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
linear_drag = 20000.000000
mass = 4000.000000
hold_size = 100000
explosion_arch = explosion_ge_atransport
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 5000000, 5000000, 5000000
angular_drag = 100000.000000, 100000.000000, 100000.000000
rotation_inertia = 60000.000000, 60000.000000, 60000.000000
nudge_force = 300000.000000
HP_bay_surface = HpBayDoor01
HP_bay_external = HpBayDoor02
HP_tractor_source = HpTractor_Source
num_exhaust_nozzles = 2
hit_pts = 10000

 

[Ship]
ids_name = 1
ids_info = 1
nickname = bh_damager
LODranges = 0
type = FREIGHTER
DA_archetype = polygon.cmp
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
linear_drag = 500.000000
mass = 500.000000
hold_size = 100000
hit_pts = 500
explosion_arch = explosion_damager
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 25000.000000, 25000.000000, 25000.000000
angular_drag = 100000.000000, 100000.000000, 100000.000000
rotation_inertia = 48000.000000, 48000.000000, 48000.000000
nudge_force = 3000.000000
num_exhaust_nozzles = 1



[Ship]
ids_name = 1
ids_info = 1
nickname = m04_bship_reactor_damager
LODranges = 0
type = FREIGHTER
DA_archetype = polygon.cmp
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
linear_drag = 500.000000
mass = 500.000000
hold_size = 100000
hit_pts = 500
explosion_arch = reactor_damager
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 25000.000000, 25000.000000, 25000.000000
angular_drag = 100000.000000, 100000.000000, 100000.000000
rotation_inertia = 48000.000000, 48000.000000, 48000.000000
nudge_force = 3000.000000
num_exhaust_nozzles = 1



[Ship]
ids_name = 1
ids_info = 1
nickname = krieg_ship
LODranges = 0, 10000
type = FREIGHTER
DA_archetype = polygon.cmp
material_library = fx\\envmapbasic.mat
envmap_material = envmapship
linear_drag = 500.000000
mass = 1.000000
hold_size = 4
hit_pts = 500
explosion_arch = explosion_damager
surface_hit_effects = 0, small_hull_hit_light01, small_hull_hit_light02, small_hull_hit_light03
surface_hit_effects = 150, small_hull_hit_medium01, small_hull_hit_medium02, small_hull_hit_medium03
surface_hit_effects = 300, small_hull_hit_heavy01, small_hull_hit_heavy02, small_hull_hit_heavy03
steering_torque = 25000.000000, 25000.000000, 58000.000000
angular_drag = 15000.000000, 15000.000000, 35000.000000
rotation_inertia = 3800.000000, 3800.000000, 1000.000000
nudge_force = 60000.000000
num_exhaust_nozzles = 1
cockpit = cockpits\\krieg.ini
camera_offset = 100, 500
camera_angular_acceleration = 0.050000
camera_horizontal_turn_angle = 17
camera_vertical_turn_up_angle = 5
camera_vertical_turn_down_angle = 25
camera_turn_look_ahead_slerp_amount = 1.000000
msg_id_prefix = gcs_refer_shiparch_Liblf
mission_property = can_use_berths

'''

