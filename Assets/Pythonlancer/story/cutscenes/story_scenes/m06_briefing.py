"""m06_briefing: постановка для ручного редактирования.

Точки: SCENES/m06_briefing.blend → DUMPS/m06_briefing.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — смещение внутри текущего блока; facial()/append_time() двигают часы.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character,
    ConnectHardpointEvent,
    Equipment,
    EyeIkEvent,
    LookAtCamera,
    MAIN,
    MoveEvent,
    NeckIkEvent,
    Prop,
    RotateAxisEvent,
    SoundEvent,
)
from story.cutscenes.anim import (
    Female,
    Male,
)
from story.cutscenes.source_extensions import (
    SourceAttachEvent,
    preserve_entity,
    preserve_spatial,
)
from story import actors


class PropSceneObj01(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_hardware_li_free_flow_ion_drive'
    SRT_GRP = 0
    USR_FLG = 0


class PropSceneObj02(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_hardware_li_fusion_reactor'
    SRT_GRP = 0
    USR_FLG = 0


class PropSceneObj03(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_hardware_li_fusion_reactor'
    SRT_GRP = 0
    USR_FLG = 0


class PropSceneObj04(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_hardware_li_fusion_reactor'
    SRT_GRP = 0
    USR_FLG = 0


class PropSceneObj05(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_hardware_li_fusion_reactor'
    SRT_GRP = 0
    USR_FLG = 0


class PropSceneObj06(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_hardware_li_free_flow_ion_drive'
    SRT_GRP = 0
    USR_FLG = 0


class PropSceneObj07(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_hardware_li_fusion_reactor'
    SRT_GRP = 0
    USR_FLG = 0


class PropSceneObj08(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_hardware_li_fusion_reactor'
    SRT_GRP = 0
    USR_FLG = 0


class PropSceneObj09(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_hardware_li_fusion_reactor'
    SRT_GRP = 0
    USR_FLG = 0


class PropSceneObj10(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_hardware_li_fusion_reactor'
    SRT_GRP = 0
    USR_FLG = 0


class PropSceneMonitorProjector(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_hardware_ge_nano_weavers1'
    SRT_GRP = 0
    USR_FLG = 0


class PropSceneCloakingDevice(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_hardware_co_stealth2'
    SRT_GRP = 0
    USR_FLG = 0


class PropInfopanelShipyardView(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_infopanel05'
    SRT_GRP = 0
    USR_FLG = 0


class PropInfopanelShipyardShips(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_infopanel04'
    SRT_GRP = 0
    USR_FLG = 0


class PropInfopanelStealthConnection(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_infopanel06'
    SRT_GRP = 0
    USR_FLG = 0


class PropShipMonitor(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_fiber_struts_sml'
    SRT_GRP = 0
    USR_FLG = 0


class PropInfopanelMonitor(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_monitor'
    SRT_GRP = 0
    USR_FLG = 0


class PropSphereMap(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_sphere_map_1_5x'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropGlasses(Prop):
    COMPOUND_TEMPLATE_NAME = 'new_fem_glasses'
    SRT_GRP = 0
    USR_FLG = 0



class M06BriefingScene(Scene):
    DUMP_FILE = 'm06_briefing'
    SCENE_AMBIENT = [55, 55, 55]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        scene_obj_01 = PropSceneObj01(root=self, name='scene_obj_01', light_group=3, init_point='scene_obj_01',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(scene_obj_01, userprops={'category': 'Equipment'})
        scene_obj_02 = PropSceneObj02(root=self, name='scene_obj_02', light_group=3, init_point='scene_obj_02',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(scene_obj_02, userprops={'category': 'Equipment'})
        scene_obj_03 = PropSceneObj03(root=self, name='scene_obj_03', light_group=3, init_point='scene_obj_03',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(scene_obj_03, userprops={'category': 'Equipment'})
        scene_obj_04 = PropSceneObj04(root=self, name='scene_obj_04', light_group=3, init_point='scene_obj_04',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(scene_obj_04, userprops={'category': 'Equipment'})
        scene_obj_05 = PropSceneObj05(root=self, name='scene_obj_05', light_group=3, init_point='scene_obj_05',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(scene_obj_05, userprops={'category': 'Equipment'})
        scene_obj_06 = PropSceneObj06(root=self, name='scene_obj_06', light_group=3, init_point='scene_obj_06',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(scene_obj_06, userprops={'category': 'Equipment'})
        scene_obj_07 = PropSceneObj07(root=self, name='scene_obj_07', light_group=3, init_point='scene_obj_07',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(scene_obj_07, userprops={'category': 'Equipment'})
        scene_obj_08 = PropSceneObj08(root=self, name='scene_obj_08', light_group=3, init_point='scene_obj_08',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(scene_obj_08, userprops={'category': 'Equipment'})
        scene_obj_09 = PropSceneObj09(root=self, name='scene_obj_09', light_group=3, init_point='scene_obj_09',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(scene_obj_09, userprops={'category': 'Equipment'})
        scene_obj_10 = PropSceneObj10(root=self, name='scene_obj_10', light_group=3, init_point='scene_obj_10',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(scene_obj_10, userprops={'category': 'Equipment'})
        scene_monitor_projector = PropSceneMonitorProjector(root=self, name='scene_monitor_projector', light_group=3,
            init_point='scene_monitor_projector', rotate_from_quat=True, use_ambient=True)
        preserve_entity(scene_monitor_projector, userprops={'category': 'Equipment'})
        scene_cloaking_device = PropSceneCloakingDevice(root=self, name='scene_cloaking_device', light_group=3,
            init_point='scene_cloaking_device', rotate_from_quat=True, use_ambient=True)
        preserve_entity(scene_cloaking_device, userprops={'category': 'Equipment'})
        infopanel_shipyard_view = PropInfopanelShipyardView(root=self, name='infopanel_shipyard_view', light_group=3,
            init_point='infopanel_shipyard_view', rotate_from_quat=True, use_ambient=True)
        preserve_entity(infopanel_shipyard_view, userprops={'category': 'Prop'})
        infopanel_shipyard_ships = PropInfopanelShipyardShips(root=self, name='infopanel_shipyard_ships', light_group=3,
            init_point='infopanel_shipyard_ships', rotate_from_quat=True, use_ambient=True)
        preserve_entity(infopanel_shipyard_ships, userprops={'category': 'Prop'})
        infopanel_stealth_connection = PropInfopanelStealthConnection(root=self, name='infopanel_stealth_connection',
            light_group=3, init_point='infopanel_stealth_connection', rotate_from_quat=True, use_ambient=True)
        preserve_entity(infopanel_stealth_connection, userprops={'category': 'Prop'})
        ship_monitor = PropShipMonitor(root=self, name='ship_monitor', light_group=3, init_point='ship_monitor',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(ship_monitor, userprops={'category': 'Prop'})
        infopanel_monitor = PropInfopanelMonitor(root=self, name='infopanel_monitor', light_group=3,
            init_point='infopanel_monitor', rotate_from_quat=True, use_ambient=True)
        preserve_entity(infopanel_monitor, userprops={'category': 'Prop'})
        sphere_map = PropSphereMap(root=self, name='sphere_map', light_group=3, init_point='sphere_map',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(sphere_map, userprops={'category': 'Prop'})
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=True, floor_height=-13)
        preserve_entity(trent, template_name='trent', userprops={'Actor': 'Player', 'category': 'Character'})
        alaric = Character(root=self, actor=actors.Alaric, light_group=0, init_point='Char_alaric', rotate_from_quat=True,
            use_ambient=True, floor_height=-13)
        preserve_entity(alaric, template_name='alaric', userprops={'actor': 'Alaric', 'category': 'Character'})
        hatcher = Character(root=self, actor=actors.Hatcher, light_group=0, init_point='Char_hatcher',
            rotate_from_quat=True, use_ambient=True, floor_height=-13)
        preserve_entity(hatcher, template_name='hatcher_glassless',
            userprops={'actor': 'Hatcher_noglass', 'category': 'Character'})
        prop_glasses = PropPropGlasses(root=self, name='prop_glasses', light_group=0, init_point='prop_glasses',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(prop_glasses, userprops={'category': 'Prop'})
        cam_start = LookAtCamera(root=self, name='cam_start', fov=25, farplane=5000, look_duration=30)
        preserve_entity(cam_start)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=22, farplane=5000, look_duration=150)
        preserve_entity(cam_trent)
        cam_alaric = LookAtCamera(root=self, name='cam_alaric', fov=20, farplane=5000, look_duration=30)
        preserve_entity(cam_alaric)
        cam_hatcher = LookAtCamera(root=self, name='cam_hatcher', fov=25, farplane=5000, look_duration=250)
        preserve_entity(cam_hatcher)
        cam_stealth = LookAtCamera(root=self, name='cam_stealth', fov=28, farplane=5000, look_duration=150)
        preserve_entity(cam_stealth)

        # Вход / начальная постановка.
        t = 0
        cam_start.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_start', target_name='automarker_cam_start_pos2',
            duration=10, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_start_focus',
            target_name='automarker_cam_start_marker_pos2', duration=10, smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=8, time_scale=0.7,
            start_time=0.73, loop=True)
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=7.5, time_scale=0.7,
            start_time=0.53, loop=True)
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='prop_glasses', parent_name='Char_hatcher',
            duration=12, target_hardpoint='hp_eyewear', parent_hardpoint='hp_eyewear')
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_HOLD_ARMS_CROSSED_000LV_XA_03, duration=1)
        t += 4
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_UNCRSS_ARMS_000LV_XA_03, duration=10)
        main_group.append_time(4.8)


        # Реплика 10 · hatcher · исходное время 4.8 с
        # Итак, джентльмены, главная задача - ликвидировать рейнландского ученого, профессора Роттермана.
        # Исходное окно facial: 7 с.
        t = 0
        t += 0.2
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_hatcher', target_name='automarker_hatcher_head_ik',
            duration=13, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_hatcher', target_name='automarker_hatcher_eye_ik',
            duration=13, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 3.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_alaric', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_alaric', duration=1.5, smooth=True)
        t += 2.2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', target_name='automarker_point_trent_stand',
            duration=0.001, smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_alaric',
            target_name='automarker_point_alaric_stand', duration=0.001, smooth=False)
        t += 0.1
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_XB_04, duration=1)
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_XB_04, duration=1)
        t += 0.2
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_alaric', target_name='automarker_alaric_head_ik',
            duration=250, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_alaric', target_name='automarker_alaric_eye_ik',
            duration=250, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        hatcher.facial(group=MAIN, index=10, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.8)


        # Реплика 20 · trent · исходное время 11 с
        # Черт, я так и думал.
        # Исходное окно facial: 15 с.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        t += 1.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_trent', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1.25, smooth=True)
        trent.facial(group=MAIN, index=20, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-13)


        # Реплика 30 · hatcher · исходное время 13 с
        # Не перебивайте, Трент!  Думал он. Может быть, вы также думали, что за такой гонорар вам поручат доставку
        # суши?
        # Исходное окно facial: 8 с.
        t = 0
        cam_hatcher.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_hatcher', target_name='automarker_cam_hatcher_pos2',
            duration=10, smooth=True)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=5,
            trans_time=0.5)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHAND_HNEUT_PROBE_RGHT_000LV_00, duration=1)
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='prop_glasses', parent_name='Char_hatcher',
            duration=6.1399, target_hardpoint='hp_eyewear', parent_hardpoint='hp_eyewear')
        t += 5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_SALUT_000LV_XA_03, duration=2, start_time=1,
            trans_time=1)
        t += 1
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_hatcher', target_name='automarker_hatcher_head_ik',
            duration=551, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_hatcher', target_name='automarker_hatcher_eye_ik',
            duration=551, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_point_glass_clean_middle', duration=1.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_point_glass_clean', duration=1, smooth=True)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['automarker_glass_connect_marker', 'Char_hatcher'],
            duration=10, offset=[0.05, 0.05, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpRightGlassTouch',
            target_type='HARDPOINT', flags='POSITION+ORIENTATION+ENTITY_RELATIVE')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['automarker_glass_connect_marker_second', 'automarker_glass_connect_marker'], duration=10,
            offset=[0, 0, -0.015], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT',
            flags='POSITION+ORIENTATION+ENTITY_RELATIVE+ORIENTATION_RELATIVE')
        t += 0.15
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='prop_glasses',
            target_name='automarker_glass_connect_marker_second', duration=0.1, smooth=False)
        t += 0.1
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='prop_glasses', parent_name='Char_hatcher',
            duration=5.199, target_hardpoint='HpRightTouch', parent_hardpoint='HpRightGlassTouch')
        t += 0.75
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=55, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_eye_ik',
            duration=55, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_IDLE_MED_000LV_xa_05, duration=3.5, loop=True,
            trans_time=1)
        hatcher.facial(group=MAIN, index=30, append=True, auto_lip=True, extra_delay=0)
        t = 0


        # Реплика 40 · hatcher · исходное время 21 с
        # Пора взрослеть, мистер Трент.
        # Исходное окно facial: 6 с.
        t = 0
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_trent', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1, smooth=True)
        t += 1.5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_SALUT_000LV_XA_03, duration=5, start_time=1,
            trans_time=1)
        t += 0.5
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['automarker_glass_head_connect_marker', 'Char_hatcher'], duration=5, offset=[0, -0.01, -0.08],
            up='Y_AXIS', front='NEG_Z_AXIS', target_part='hp_eyewear', target_type='HARDPOINT',
            flags='POSITION+ENTITY_RELATIVE')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['automarker_glass_head_connect_marker_second', 'automarker_glass_head_connect_marker'], duration=5,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT',
            flags='POSITION+ORIENTATION+ENTITY_RELATIVE+ORIENTATION_RELATIVE')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_alaric', duration=1.25, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_alaric', duration=1, smooth=True)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHEAD_CONCNTRTE_000LV_XA_, duration=0.5, time_scale=0.8,
            trans_time=0.5)
        t += 0.45
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='prop_glasses',
            target_name='automarker_glass_head_connect_marker_second', duration=0.4, smooth=False, adjust_orient=False)
        t += 0.4
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='prop_glasses', parent_name='Char_hatcher',
            duration=351, target_hardpoint='hp_eyewear', parent_hardpoint='hp_eyewear')
        hatcher.facial(group=MAIN, index=40, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2)


        # Реплика 50 · hatcher · исходное время 25 с
        # Итак, ликвидируете профессора Роттермана и забираете два артефакта - кристалл кочевников и том Протея,
        # они должны находиться либо у профессора, либо рядом с ним.
        # Исходное окно facial: 11 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_hatcher', target_name='automarker_cam_hatcher_pos3',
            duration=20, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_hatcher_focus',
            target_name='automarker_cam_hatcher_marker_pos3', duration=20, smooth=True)
        t += 0.5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_TALK_EMPH_000LV_A_04, duration=7.5,
            time_scale=0.7, trans_time=0.5)
        t += 1.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_trent', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1.35, smooth=True)
        t += 4
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_alaric', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_alaric', duration=1.35, smooth=True)
        t += 1
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=5,
            time_scale=0.7, trans_time=0.5)
        t += 2
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_HOLD_000LV_XA_01, duration=4, loop=True,
            trans_time=0.5)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_trent', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1.35, smooth=True)
        hatcher.facial(group=MAIN, index=50, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.5)


        # Реплика 60 · hatcher · исходное время 35.5 с
        # В свое время они хранились в одном из тайников Ордена, но в так называемые смутные времена следы их
        # потерялись.
        # Исходное окно facial: 15 с.
        t = 0
        t += 2.5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=5,
            time_scale=0.7, trans_time=0.5)
        t += 2.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_alaric', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_alaric', duration=1.35, smooth=True)
        hatcher.facial(group=MAIN, index=60, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-9.0)


        # Реплика 70 · hatcher · исходное время 41.5 с
        # Вы забираете артефакты, увозите их и Сфера закрывается.
        # Исходное окно facial: 6.5 с.
        t = 0
        t += 0.3
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CROSS_ARMS_000LV_xa_03, duration=5,
            time_scale=0.7, trans_time=0.5)
        t += 1.2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_trent', duration=2.25, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1.2, smooth=True)
        hatcher.facial(group=MAIN, index=70, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.0)


        # Реплика 80 · alaric · исходное время 46 с
        # Орден? Смутные времена?
        # Исходное окно facial: 12 с.
        t = 0
        cam_alaric.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_alaric_head_ik',
            target_name='automarker_head_trent_alaric_middle', duration=3.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_alaric_eye_ik',
            target_name='automarker_head_trent', duration=1.5, smooth=True)
        t += 1
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=10, loop=True)
        t += 1.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_trent_alaric_middle', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_alaric', duration=1, smooth=True)
        alaric.facial(group=MAIN, index=80, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-8.5)


        # Реплика 90 · trent · исходное время 49.5 с
        # Позже, Аларик.
        # Исходное окно facial: 15 с.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=90, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-13.0)


        # Реплика 100 · hatcher · исходное время 51.5 с
        # Хватит, чёрт побери, меня перебивать, мы сейчас обсуждаем важнейшую миссию!
        # Исходное окно facial: 7 с.
        t = 0
        cam_hatcher.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_IDLE_MED_000LV_xa_05, duration=5, trans_time=2)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_alaric', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_alaric', duration=1.35, smooth=True)
        hatcher.facial(group=MAIN, index=100, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.0)


        # Реплика 110 · trent · исходное время 56.5 с
        # Самую важную в вашей жизни, мисс Хетчер? Не забывайте что конкретные исполнители - мы, и вот как
        # исполнители мы хотели бы подробностей о предшествующих ликвидации профессора этапах.
        # Исходное окно facial: 12.8 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_trent_front', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_trent_front', duration=1.3, smooth=True)
        cam_trent.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_trent', target_name='automarker_cam_trent_pos2',
            duration=13, smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_GESTR_THMBSUP_000LV_XA_02, duration=4,
            time_scale=0.7)
        t += 4.0
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=3,
            time_scale=0.7, trans_time=0.5)
        t += 2.0
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_HOLD_000LV_XA_02, duration=3,
            time_scale=0.7, loop=True, trans_time=0.5)
        t += 6.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_trent', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='infopanel_monitor',
            target_name='automarker_monitor_start_point', duration=0.01, smooth=False, adjust_orient=False)
        trent.facial(group=MAIN, index=110, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(0.2)


        # Реплика 120 · hatcher · исходное время 69.5 с
        # Хорошо, Трент. Итак, проникновение внутрь Сферы. Охраняется она беспрецедентно. Я сомневаюсь, что кайзер
        # Рейнланда охраняется так же как она.
        # Исходное окно facial: 12 с.
        t = 0
        cam_hatcher.set(group=MAIN, time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='infopanel_monitor',
            target_name='automarker_monitor_viewpoint', duration=10, smooth=True, adjust_orient=False)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_hatcher',
            target_name='automarker_cam_hatcher_brief_pos1', duration=15, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_hatcher_focus',
            target_name='automarker_cam_hatcher_brief_marker_pos1', duration=15, smooth=True)
        t += 2.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_alaric', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_alaric', duration=1.5, smooth=True)
        t += 6.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_hatcher_front', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1.5, smooth=True)
        hatcher.facial(group=MAIN, index=120, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.0)


        # Реплика 130 · hatcher · исходное время 80.5 с
        # Рядом со сферой находится военная база, представляющая собою верфь, способную принимать по два линкора и
        # четыре корабля среднего тоннажа одновременно. Понимаете, какая там развернута группировка? Поэтому
        # силовое решение невозможно.
        # Исходное окно facial: 19.5 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='infopanel_shipyard_view',
            target_name='automarker_monitor_viewpoint', duration=0.01, smooth=False, adjust_orient=False)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, duration=7,
            time_scale=0.7, trans_time=0.25)
        t += 2.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_RHND_CASL_000LV_xa_03, duration=6,
            time_scale=0.75, loop=True, trans_time=1)
        t += 2.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_alaric', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_alaric', duration=1.5, smooth=True)
        t += 1.5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHAND_NEUT_RGHT_000LV_A_00, duration=2, trans_time=0.25)
        t += 2.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_01, duration=3,
            time_scale=0.75, trans_time=1)
        t += 1.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHAND_HNEUT_GESTR_CASL_000LV_00, duration=6,
            time_scale=0.8, loop=True, trans_time=0.25)
        t += 1.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_hatcher_front', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1.5, smooth=True)
        hatcher.facial(group=MAIN, index=130, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-3.5)


        # Реплика 140 · hatcher · исходное время 96.5 с
        # Для проникновения вам понадобятся устройства, которые находятся в контейнерах, переданных мною вам перед
        # стыковкой с Миссури. Это устройства, делающие ваши корабли невидимыми как визуально, так и всеми
        # радарными системами.
        # Исходное окно facial: 13.5 с.
        t = 0
        t += 0.5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=3,
            time_scale=0.4, trans_time=0.5)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='infopanel_shipyard_view', target_name='offscreen',
            duration=1e-05, smooth=False, adjust_orient=False)
        t += 1e-05
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='infopanel_stealth_connection',
            target_name='automarker_monitor_viewpoint', duration=1e-06, smooth=False, adjust_orient=False)
        t += 2.99999
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_HOLD_000LV_XA_01, duration=4,
            time_scale=0.6, loop=True, trans_time=0.5)
        t += 5.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_alaric', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_alaric', duration=1.5, smooth=True)
        t += 1.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=2,
            time_scale=0.5, trans_time=0.5)
        hatcher.facial(group=MAIN, index=140, append=True, auto_lip=True, extra_delay=0)
        t = 0
        cam_stealth.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_stealth', target_name='automarker_cam_stealth_pos2',
            duration=8, smooth=True)
        main_group.append_time(0.5)


        # Реплика 150 · hatcher · исходное время 110.5 с
        # Они создают вокруг корабля локальное искривление пространства, и ваши корабли как бы перестают находиться
        # в нашей реальности.
        # Исходное окно facial: 0 с.
        t = 0
        voice_sound = self.lookup_single_sound(150)
        SoundEvent(root=self, group=MAIN, sound_name=voice_sound.get_nickname())
        t = 0
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_hatcher_front', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1.5, smooth=True)
        t += 4.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='infopanel_stealth_connection', target_name='offscreen',
            duration=0.01, smooth=False, adjust_orient=False)
        t += 0.01
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='ship_monitor',
            target_name='automarker_monitor_viewpoint', duration=0.01, smooth=False, adjust_orient=False)
        main_group.append_time(7.5)


        # Реплика 160 · hatcher · исходное время 118 с
        # Смонтируете их у себя на кораблях - просто устанавливаете где-нибудь внутри герметичного корпуса,
        # подключаете к энергосистеме и выводите кнопку управления в удобное место приборной доски. Кнопка всего
        # одна, не ошибетесь.
        # Исходное окно facial: 13.5 с.
        t = 0
        cam_hatcher.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_hatcher',
            target_name='automarker_cam_hatcher_brief_pos2', duration=25, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_hatcher_focus',
            target_name='automarker_cam_hatcher_brief_marker_pos2', duration=25, smooth=True)
        t += 1.5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CROSS_ARMS_000LV_xa_03, duration=3.6,
            time_scale=0.8, trans_time=0.5)
        t += 3.6
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_HOLD_ARMS_CROSSED_000LV_XA_03, duration=3.4,
            time_scale=0.8, loop=True, trans_time=0.5)
        t += 1.9
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_alaric', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_alaric', duration=1.5, smooth=True)
        t += 1.5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_UNCRSS_ARMS_000LV_XA_03, duration=8,
            time_scale=0.8, trans_time=0.5)
        hatcher.facial(group=MAIN, index=160, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.5)


        # Реплика 170 · hatcher · исходное время 131 с
        # Нажимаете один раз - и ваш корабль невидим, нажимаете второй раз - и он снова видим. Проблема устройства
        # в его одноразовости.
        # Исходное окно facial: 13.5 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_hatcher_front', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1.5, smooth=True)
        t += 0.5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, duration=7,
            time_scale=0.7, trans_time=0.25)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHAND_HNEUT_GESTR_CASL_000LV_00, duration=7,
            time_scale=0.8, loop=True, trans_time=0.25)
        t += 2.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_RHND_CASL_000LV_xa_03, duration=3,
            time_scale=0.75, loop=True, trans_time=1)
        t += 3.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_01, duration=3,
            time_scale=0.75, trans_time=1)
        hatcher.facial(group=MAIN, index=170, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-5.0)


        # Реплика 180 · hatcher · исходное время 139.5 с
        # Я не ученый, поэтому скажу просто, после выключения там что-то перегорает, и оно превращается в коробочку
        # с горелым пластиком и обугленным  металлом.
        # Исходное окно facial: 13.5 с.
        t = 0
        t += 0.5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=3,
            time_scale=0.4, trans_time=0.5)
        t += 3.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_HOLD_000LV_XA_01, duration=4,
            time_scale=0.6, loop=True, trans_time=0.5)
        t += 3.0
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=10, loop=True)
        hatcher.facial(group=MAIN, index=180, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-5.0)


        # Реплика 190 · trent · исходное время 148 с
        # Огнетушителями запасаться?
        # Исходное окно facial: 15 с.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=190, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-12.5)


        # Реплика 200 · hatcher · исходное время 150.5 с
        # Нет, все безопасно, все происходит внутри устройства, даже неприятного запаха не появится.
        # Исходное окно facial: 5 с.
        t = 0
        cam_hatcher.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_hatcher',
            target_name='automarker_cam_hatcher_brief_pos3', duration=25, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_hatcher_focus',
            target_name='automarker_cam_hatcher_brief_marker_pos1', duration=25, smooth=True)
        cam_hatcher.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=5,
            time_scale=0.7, trans_time=0.5)
        t += 3.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_alaric', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_alaric', duration=1.5, smooth=True)
        hatcher.facial(group=MAIN, index=200, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(0.5)


        # Реплика 210 · hatcher · исходное время 156 с
        # По времени работы. Поскольку устройство одноразовое, постарайтесь использовать его максимально
        # эффективно. Наши головастики гарантируют тридцать минут работы. Возможно, оно проработает сорок, больше
        # вряд ли.
        # Исходное окно facial: 15 с.
        t = 0
        t += 0.5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CROSS_ARMS_000LV_xa_03, duration=3.6,
            time_scale=0.8, trans_time=0.5)
        t += 3.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_hatcher_front', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1.5, smooth=True)
        t += 0.1
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_HOLD_ARMS_CROSSED_000LV_XA_03, duration=6.4,
            time_scale=0.8, loop=True, trans_time=0.5)
        t += 6.4
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_UNCRSS_ARMS_000LV_XA_03, duration=8,
            time_scale=0.8, trans_time=0.5)
        hatcher.facial(group=MAIN, index=210, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1)


        # Реплика 220 · hatcher · исходное время 170 с
        # Если тридцати минут работы не хватило, вы можете попробовать оставаться в невидимости дольше на свой
        # страх и риск. Если устройство сгорит не во время выключения, а во время работы, локальное искривление
        # пространства схлопывается вместе с кораблём.
        # Исходное окно facial: 15.5 с.
        t = 0
        t += 0.5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, duration=7,
            time_scale=0.7, trans_time=0.25)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHAND_HNEUT_GESTR_CASL_000LV_00, duration=7,
            time_scale=0.8, loop=True, trans_time=0.25)
        t += 2.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_RHND_CASL_000LV_xa_03, duration=3,
            time_scale=0.75, loop=True, trans_time=1)
        t += 1.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_alaric', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_alaric', duration=1.5, smooth=True)
        t += 1.5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_01, duration=1,
            time_scale=0.75, trans_time=1)
        t += 4.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_hatcher_front', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_alaric_head_ik',
            target_name='automarker_head_hatcher', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_alaric_eye_ik',
            target_name='automarker_head_hatcher', duration=1.5, smooth=True)
        t += 5
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=10, loop=True)
        hatcher.facial(group=MAIN, index=220, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(0.5)


        # Реплика 230 · alaric · исходное время 186 с
        # И куда попадает корабль? В другое измерение?
        # Исходное окно facial: 14.5 с.
        t = 0
        cam_alaric.set(group=MAIN, time_delay=t)
        alaric.facial(group=MAIN, index=230, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-9.5)


        # Реплика 240 · hatcher · исходное время 191 с
        # Понятия не имею. Хотите узнать, мистер Аларик? По глазам вижу, что нет. И да, еще один момент. При
        # включенном устройстве стрелять бесполезно. Выши выстрелы не покинут локальную зону искривления
        # пространства.
        # Исходное окно facial: 16 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_alaric', duration=1.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_alaric', duration=0.9, smooth=True)
        cam_hatcher.set(group=MAIN, time_delay=t)
        t += 0.5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=3,
            time_scale=0.9, trans_time=0.5)
        t += 2.5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_HOLD_000LV_XA_01, duration=3,
            time_scale=0.8, loop=True, trans_time=0.5)
        t += 3
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_hatcher_front', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1.5, smooth=True)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=3,
            time_scale=0.6, trans_time=0.5)
        t += 8
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='ship_monitor', target_name='offscreen', duration=0.01,
            smooth=False, adjust_orient=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='infopanel_monitor',
            target_name='automarker_monitor_start_point', duration=10, smooth=True, adjust_orient=False)
        t += 1
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, duration=7,
            time_scale=0.7, trans_time=0.25)
        hatcher.facial(group=MAIN, index=240, append=True, auto_lip=True, extra_delay=0)
        t = 0


        # Реплика 250 · hatcher · исходное время 207 с
        # Вот трехмерный план Сферы и все данные по ней, которые нам удалось собрать.
        # Исходное окно facial: 5 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_hatcher',
            target_name='automarker_cam_hatcher_brief_pos4', duration=5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_hatcher_focus',
            target_name='automarker_cam_hatcher_brief_marker_pos4', duration=5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='sphere_map',
            target_name='automarker_sphere_projector_viewpoint', duration=0.01, smooth=False, adjust_orient=False)
        t += 0.001
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='sphere_map', angle=-360, axis='Y_AXIS',
            duration=19, smooth=False)
        t += 0.999
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_RHND_CASL_000LV_xa_03, duration=3,
            time_scale=0.75, loop=True, trans_time=1)
        t += 3
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_01, duration=2,
            time_scale=0.75, trans_time=1)
        hatcher.facial(group=MAIN, index=250, append=True, auto_lip=True, extra_delay=0)
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_alaric_head_ik',
            target_name='automarker_sphere_projector_viewpoint', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_alaric_eye_ik',
            target_name='automarker_sphere_projector_viewpoint', duration=1.5, smooth=True)
        main_group.append_time(1)


        # Реплика 260 · alaric · исходное время 213 с
        # Вот это хреновина...
        # Исходное окно facial: 12 с.
        t = 0
        cam_alaric.set(group=MAIN, time_delay=t)
        t += 3
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='infopanel_monitor',
            target_name='automarker_monitor_start_point', duration=0.01, smooth=False, adjust_orient=False)
        alaric.facial(group=MAIN, index=260, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-8)


        # Реплика 270 · hatcher · исходное время 217 с
        # Я рада, что вы прониклись, мистер Аларик. Загрузите всё к себе в компьютер. В ходе операции будете
        # передавать нужные данные мистеру Тренту.
        # Исходное окно facial: 10 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_alaric', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_alaric', duration=1.5, smooth=True)
        cam_hatcher.set(group=MAIN, time_delay=t)
        t += 8
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_hatcher_front', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1.5, smooth=True)
        hatcher.facial(group=MAIN, index=270, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1)


        # Реплика 280 · hatcher · исходное время 226 с
        # Ну и последнее - после прибытия на территорию Рейнланда никаких радиопереговоров со мной или с кем-то еще
        # на территории Либерти. Вас запеленгуют их радарные станции, и миссия завершится так и не начавшись.
        # Исходное окно facial: 14.5 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_hatcher',
            target_name='automarker_cam_hatcher_final_pos1', duration=10, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_hatcher_focus',
            target_name='automarker_cam_hatcher_final_marker_pos1', duration=10, smooth=True)
        t += 0.1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='sphere_map', target_name='offscreen', duration=0.01,
            smooth=False, adjust_orient=False)
        t += 2.9
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_alaric', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_alaric', duration=1.5, smooth=True)
        t += 4
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_hatcher_front', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1.5, smooth=True)
        t += 4
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=3,
            time_scale=0.4, trans_time=0.5)
        hatcher.facial(group=MAIN, index=280, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.5)


        # Реплика 290 · hatcher · исходное время 239 с
        # Вот, собственно, и всё. По коням, джентльмены.
        # Исходное окно facial: 7 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_alaric', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_alaric', duration=1.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_hatcher',
            target_name='automarker_cam_hatcher_final_pos2', duration=5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_hatcher_focus',
            target_name='automarker_cam_hatcher_final_marker_pos2', duration=5, smooth=True)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_trent', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1.5, smooth=True)
        hatcher.facial(group=MAIN, index=290, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-3.0)
        preserve_spatial(self.get_entity('scene_obj_01'), source_basis=[[2, 0, 0], [0, 2, 0], [0, 0, 2]],
            reference_orientation=[1.0, -0.0, -0.0, -0.0])
        preserve_spatial(self.get_entity('scene_obj_02'), source_basis=[[2, 0, 0], [0, 2, 0], [0, 0, 2]],
            reference_orientation=[1.0, -0.0, -0.0, -0.0])
        preserve_spatial(self.get_entity('scene_obj_03'), source_basis=[[2, 0, 0], [0, 2, 0], [0, 0, 2]],
            reference_orientation=[1.0, -0.0, -0.0, -0.0])
        preserve_spatial(self.get_entity('scene_obj_04'), source_basis=[[2, 0, 0], [0, 2, 0], [0, 0, 2]],
            reference_orientation=[1.0, -0.0, -0.0, -0.0])
        preserve_spatial(self.get_entity('scene_obj_05'), source_basis=[[2, 0, 0], [0, 2, 0], [0, 0, 2]],
            reference_orientation=[1.0, -0.0, -0.0, -0.0])
        preserve_spatial(self.get_entity('scene_obj_06'), source_basis=[[-2, 0, 0], [0, 2, 0], [0, 0, -2]],
            reference_orientation=[0.0, -0.0, 1.0, -0.0])
        preserve_spatial(self.get_entity('scene_obj_07'), source_basis=[[-2, 0, 0], [0, 2, 0], [0, 0, -2]],
            reference_orientation=[0.0, -0.0, 1.0, -0.0])
        preserve_spatial(self.get_entity('scene_obj_08'), source_basis=[[-2, 0, 0], [0, 2, 0], [0, 0, -2]],
            reference_orientation=[0.0, -0.0, 1.0, -0.0])
        preserve_spatial(self.get_entity('scene_obj_09'), source_basis=[[-2, 0, 0], [0, 2, 0], [0, 0, -2]],
            reference_orientation=[0.0, -0.0, 1.0, -0.0])
        preserve_spatial(self.get_entity('scene_obj_10'), source_basis=[[-2, 0, 0], [0, 2, 0], [0, 0, -2]],
            reference_orientation=[0.0, -0.0, 1.0, -0.0])
        preserve_spatial(self.get_entity('scene_monitor_projector'), source_basis=[[-0.8, 0, 0], [0, 0.8, 0], [0, 0, -0.8]],
            reference_orientation=[0.0, -0.0, 1.0, -0.0])
        preserve_spatial(self.get_entity('scene_cloaking_device'), source_basis=[[-1.5, 0, 0], [0, 1.5, 0], [0, 0, -1.5]],
            reference_orientation=[0.0, -0.0, 1.0, -0.0])


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M06BriefingScene
