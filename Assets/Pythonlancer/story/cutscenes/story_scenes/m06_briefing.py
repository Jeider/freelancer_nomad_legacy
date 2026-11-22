"""m06_briefing: полная постановка из master; точки в m06_briefing.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    AttachEvent, Character, ConnectHardpointEvent, Equipment, EyeIkEvent, Female, LookAtCamera, MAIN, Male, MoveEvent, NeckIkEvent, Prop, RotateAxisEvent, SoundEvent,
)
from story.cutscenes.anim import (
    Female, Male,
)
from story import actors


class SceneObj01Prop(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_hardware_li_free_flow_ion_drive'

class SceneObj02Prop(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_hardware_li_fusion_reactor'

class SceneObj03Prop(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_hardware_li_fusion_reactor'

class SceneObj04Prop(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_hardware_li_fusion_reactor'

class SceneObj05Prop(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_hardware_li_fusion_reactor'

class SceneObj06Prop(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_hardware_li_free_flow_ion_drive'

class SceneObj07Prop(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_hardware_li_fusion_reactor'

class SceneObj08Prop(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_hardware_li_fusion_reactor'

class SceneObj09Prop(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_hardware_li_fusion_reactor'

class SceneObj10Prop(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_hardware_li_fusion_reactor'

class SceneMonitorProjectorProp(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_hardware_ge_nano_weavers1'

class SceneCloakingDeviceProp(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_hardware_co_stealth2'

class InfopanelShipyardViewProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_infopanel05'

class InfopanelShipyardShipsProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_infopanel04'

class InfopanelStealthConnectionProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_infopanel06'

class ShipMonitorProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_fiber_struts_sml'

class InfopanelMonitorProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_monitor'

class SphereMapProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_sphere_map_1_5x'

class PropGlassesProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'new_fem_glasses'


class M06BriefingScene(Scene):
    DUMP_FILE = 'm06_briefing'
    SCENE_AMBIENT = [55, 55, 55]

    def action(self):
        main_group = self.get_group(MAIN)

        # Персонажи, камеры, реквизит и звук.
        scene_obj_01 = SceneObj01Prop(root=self, name='scene_obj_01', light_group=3, init_point='scene_obj_01',
            rotate_from_quat=True, use_ambient=True)
        scene_obj_02 = SceneObj02Prop(root=self, name='scene_obj_02', light_group=3, init_point='scene_obj_02',
            rotate_from_quat=True, use_ambient=True)
        scene_obj_03 = SceneObj03Prop(root=self, name='scene_obj_03', light_group=3, init_point='scene_obj_03',
            rotate_from_quat=True, use_ambient=True)
        scene_obj_04 = SceneObj04Prop(root=self, name='scene_obj_04', light_group=3, init_point='scene_obj_04',
            rotate_from_quat=True, use_ambient=True)
        scene_obj_05 = SceneObj05Prop(root=self, name='scene_obj_05', light_group=3, init_point='scene_obj_05',
            rotate_from_quat=True, use_ambient=True)
        scene_obj_06 = SceneObj06Prop(root=self, name='scene_obj_06', light_group=3, init_point='scene_obj_06',
            rotate_from_quat=True, use_ambient=True)
        scene_obj_07 = SceneObj07Prop(root=self, name='scene_obj_07', light_group=3, init_point='scene_obj_07',
            rotate_from_quat=True, use_ambient=True)
        scene_obj_08 = SceneObj08Prop(root=self, name='scene_obj_08', light_group=3, init_point='scene_obj_08',
            rotate_from_quat=True, use_ambient=True)
        scene_obj_09 = SceneObj09Prop(root=self, name='scene_obj_09', light_group=3, init_point='scene_obj_09',
            rotate_from_quat=True, use_ambient=True)
        scene_obj_10 = SceneObj10Prop(root=self, name='scene_obj_10', light_group=3, init_point='scene_obj_10',
            rotate_from_quat=True, use_ambient=True)
        scene_monitor_projector = SceneMonitorProjectorProp(root=self, name='scene_monitor_projector',
            light_group=3, init_point='scene_monitor_projector', rotate_from_quat=True, use_ambient=True)
        scene_cloaking_device = SceneCloakingDeviceProp(root=self, name='scene_cloaking_device', light_group=3,
            init_point='scene_cloaking_device', rotate_from_quat=True, use_ambient=True)
        infopanel_shipyard_view = InfopanelShipyardViewProp(root=self, name='infopanel_shipyard_view',
            light_group=3, init_point='infopanel_shipyard_view', rotate_from_quat=True, use_ambient=True)
        infopanel_shipyard_ships = InfopanelShipyardShipsProp(root=self, name='infopanel_shipyard_ships',
            light_group=3, init_point='infopanel_shipyard_ships', rotate_from_quat=True, use_ambient=True)
        infopanel_stealth_connection = InfopanelStealthConnectionProp(root=self,
            name='infopanel_stealth_connection', light_group=3, init_point='infopanel_stealth_connection',
            rotate_from_quat=True, use_ambient=True)
        ship_monitor = ShipMonitorProp(root=self, name='ship_monitor', light_group=3, init_point='ship_monitor',
            rotate_from_quat=True, use_ambient=True)
        infopanel_monitor = InfopanelMonitorProp(root=self, name='infopanel_monitor', light_group=3,
            init_point='infopanel_monitor', rotate_from_quat=True, use_ambient=True)
        sphere_map = SphereMapProp(root=self, name='sphere_map', light_group=3, init_point='sphere_map',
            rotate_from_quat=True, use_ambient=True)
        trent = Character(root=self, actor=actors.Trent, name='Char_trent', light_group=0,
            init_point='Char_trent', rotate_from_quat=True, use_ambient=True, appearance='trent',
            actor_name='Player', floor_height=-13)
        alaric = Character(root=self, actor=actors.Alaric, name='Char_alaric', light_group=0,
            init_point='Char_alaric', rotate_from_quat=True, use_ambient=True, appearance='alaric',
            actor_name='Alaric', floor_height=-13)
        hatcher = Character(root=self, actor=actors.Hatcher, name='Char_hatcher', light_group=0,
            init_point='Char_hatcher', rotate_from_quat=True, use_ambient=True, appearance='hatcher_glassless',
            actor_name='Hatcher_noglass', floor_height=-13)
        prop_glasses = PropGlassesProp(root=self, name='prop_glasses', light_group=0, init_point='prop_glasses',
            rotate_from_quat=True, use_ambient=True)
        cam_start = LookAtCamera(root=self, name='cam_start', fov=25, look_duration=30)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=22, look_duration=150)
        cam_alaric = LookAtCamera(root=self, name='cam_alaric', fov=20, look_duration=30)
        cam_hatcher = LookAtCamera(root=self, name='cam_hatcher', fov=25, look_duration=250)
        cam_stealth = LookAtCamera(root=self, name='cam_stealth', fov=28, look_duration=150)

        # Исходные точки взгляда.

        # Вход.
        t = 0
        cam_start.set(group=MAIN, time_delay=t)
        cam_start.move_cam(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        cam_start.move_focus(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=8, time_scale=0.7,
            start_time=0.73, loop=True, time_delay=t)
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=7.5, time_scale=0.7,
            start_time=0.53, loop=True, time_delay=t)
        ConnectHardpointEvent(root=self, group=MAIN, target_name=prop_glasses.name, parent_name=hatcher.name,
            duration=12, target_hardpoint='hp_eyewear', parent_hardpoint='hp_eyewear', time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_HOLD_ARMS_CROSSED_000LV_XA_03, duration=1,
            time_delay=t)
        t += 4
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_UNCRSS_ARMS_000LV_XA_03, duration=10, time_delay=t)
        main_group.append_time(4.8)

        # m06_briefing 10: Hatcher.
        # Итак, джентльмены, главная задача - ликвидировать рейнландского ученого, профессора Роттермана.
        t = 0.2
        NeckIkEvent(root=self, group=MAIN, char_name=hatcher.name,
            target_name=self.get_automarker_name('hatcher_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=13, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=hatcher.name,
            target_name=self.get_automarker_name('hatcher_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=13, transition_duration=1, time_delay=t)
        t += 3
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 2.2
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('point_trent_stand'), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=alaric.name,
            target_name=self.get_automarker_name('point_alaric_stand'), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.1
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_XB_04, duration=1, time_delay=t)
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_XB_04, duration=1, time_delay=t)
        t += 0.2
        NeckIkEvent(root=self, group=MAIN, char_name=alaric.name,
            target_name=self.get_automarker_name('alaric_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=250, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=alaric.name,
            target_name=self.get_automarker_name('alaric_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=250, transition_duration=1, time_delay=t)
        hatcher.facial(group=MAIN, index=10, auto_lip=True, extra_delay=0)

        # m06_briefing 20: Trent.
        # Черт, я так и думал.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        t += 1.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.25, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        trent.facial(group=MAIN, index=20, auto_lip=True, extra_delay=0)

        # m06_briefing 30: Hatcher.
        # Не перебивайте, Трент!  Думал он. Может быть, вы также думали, что за такой гонорар вам поручат
        # доставку суши?
        t = 0
        cam_hatcher.set(group=MAIN, time_delay=t)
        cam_hatcher.move_cam(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=5,
            trans_time=0.5, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMHAND_HNEUT_PROBE_RGHT_000LV_00, duration=1, time_delay=t)
        ConnectHardpointEvent(root=self, group=MAIN, target_name=prop_glasses.name, parent_name=hatcher.name,
            duration=6.1399, target_hardpoint='hp_eyewear', parent_hardpoint='hp_eyewear', time_delay=t)
        t += 5
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_SALUT_000LV_XA_03, duration=2, start_time=1,
            trans_time=1, time_delay=t)
        t += 1
        NeckIkEvent(root=self, group=MAIN, char_name=hatcher.name,
            target_name=self.get_automarker_name('hatcher_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=551, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=hatcher.name,
            target_name=self.get_automarker_name('hatcher_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=551, transition_duration=1, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('point_glass_clean_middle'), duration=1.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('point_glass_clean'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=self.get_automarker_name('glass_connect_marker'),
            parent_name=hatcher.name, duration=10, target_part='HpRightGlassTouch', target_type='HARDPOINT',
            adjust_pos=True, adjust_orient=True, entity_relative=True, up='Y_AXIS', front='NEG_Z_AXIS',
            offset_x=0.05, offset_y=0.05, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=self.get_automarker_name('glass_connect_marker_second'),
            parent_name=self.get_automarker_name('glass_connect_marker'), duration=10, target_part='',
            target_type='ROOT', adjust_pos=True, adjust_orient=True, entity_relative=True,
            orientation_relative=True, up='Y_AXIS', front='NEG_Z_AXIS', offset_z=-0.015, time_delay=t)
        t += 0.15
        MoveEvent(root=self, group=MAIN, object_name=prop_glasses.name,
            target_name=self.get_automarker_name('glass_connect_marker_second'), duration=0.1, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.1
        ConnectHardpointEvent(root=self, group=MAIN, target_name=prop_glasses.name, parent_name=hatcher.name,
            duration=5.199, target_hardpoint='HpRightTouch', parent_hardpoint='HpRightGlassTouch', time_delay=t)
        t += 0.75
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=55, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=55, transition_duration=1, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_IDLE_MED_000LV_xa_05, duration=3.5, trans_time=1,
            loop=True, time_delay=t)
        hatcher.facial(group=MAIN, index=30, auto_lip=True, extra_delay=0)

        # m06_briefing 40: Hatcher.
        # Пора взрослеть, мистер Трент.
        t = 1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 1.5
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_SALUT_000LV_XA_03, duration=5, start_time=1,
            trans_time=1, time_delay=t)
        t += 0.5
        AttachEvent(root=self, group=MAIN, target_name=self.get_automarker_name('glass_head_connect_marker'),
            parent_name=hatcher.name, duration=5, target_part='hp_eyewear', target_type='HARDPOINT',
            adjust_pos=True, adjust_orient=False, entity_relative=True, up='Y_AXIS', front='NEG_Z_AXIS',
            offset_y=-0.01, offset_z=-0.08, time_delay=t)
        AttachEvent(root=self, group=MAIN,
            target_name=self.get_automarker_name('glass_head_connect_marker_second'),
            parent_name=self.get_automarker_name('glass_head_connect_marker'), duration=5, target_part='',
            target_type='ROOT', adjust_pos=True, adjust_orient=True, entity_relative=True,
            orientation_relative=True, up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=1.25, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMHEAD_CONCNTRTE_000LV_XA_, duration=0.5, time_scale=0.8,
            trans_time=0.5, time_delay=t)
        t += 0.45
        MoveEvent(root=self, group=MAIN, object_name=prop_glasses.name,
            target_name=self.get_automarker_name('glass_head_connect_marker_second'), duration=0.4, smooth=False,
            adjust_pos=True, adjust_orient=False, time_delay=t)
        t += 0.4
        ConnectHardpointEvent(root=self, group=MAIN, target_name=prop_glasses.name, parent_name=hatcher.name,
            duration=351, target_hardpoint='hp_eyewear', parent_hardpoint='hp_eyewear', time_delay=t)
        hatcher.facial(group=MAIN, index=40, auto_lip=True, extra_delay=0)

        # m06_briefing 50: Hatcher.
        # Итак, ликвидируете профессора Роттермана и забираете два артефакта - кристалл кочевников и том
        # Протея, они должны находиться либо у профессора, либо рядом с ним.
        t = 0
        cam_hatcher.move_cam(group=MAIN, index=3, duration=20, smooth=True, time_delay=t)
        cam_hatcher.move_focus(group=MAIN, index=3, duration=20, smooth=True, time_delay=t)
        t += 0.5
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_TALK_EMPH_000LV_A_04, duration=7.5, time_scale=0.7,
            trans_time=0.5, time_delay=t)
        t += 1.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.35, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 4
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=1.35, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 1
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=5,
            time_scale=0.7, trans_time=0.5, time_delay=t)
        t += 2
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_FSTHIPB_HOLD_000LV_XA_01, duration=4,
            trans_time=0.5, loop=True, time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.35, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        hatcher.facial(group=MAIN, index=50, auto_lip=True, extra_delay=0)

        # m06_briefing 60: Hatcher.
        # В свое время они хранились в одном из тайников Ордена, но в так называемые смутные времена следы их
        # потерялись.
        t = 2.5
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=5,
            time_scale=0.7, trans_time=0.5, time_delay=t)
        t += 2
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=1.35, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        hatcher.facial(group=MAIN, index=60, auto_lip=True, extra_delay=0)

        # m06_briefing 70: Hatcher.
        # Вы забираете артефакты, увозите их и Сфера закрывается.
        t = 0.3
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_CROSS_ARMS_000LV_xa_03, duration=5, time_scale=0.7,
            trans_time=0.5, time_delay=t)
        t += 1.2
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=2.25, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        hatcher.facial(group=MAIN, index=70, auto_lip=True, extra_delay=0)

        # m06_briefing 80: Alaric.
        # Орден? Смутные времена?
        t = 0
        cam_alaric.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('alaric_head_ik'),
            target_name=self.get_automarker_name('head_trent_alaric_middle'), duration=3.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('alaric_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 1
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=10, loop=True, time_delay=t)
        t += 1.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_trent_alaric_middle'), duration=1, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        alaric.facial(group=MAIN, index=80, auto_lip=True, extra_delay=0)

        # m06_briefing 90: Trent.
        # Позже, Аларик.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=90, auto_lip=True, extra_delay=0)

        # m06_briefing 100: Hatcher.
        # Хватит, чёрт побери, меня перебивать, мы сейчас обсуждаем важнейшую миссию!
        t = 0
        cam_hatcher.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_IDLE_MED_000LV_xa_05, duration=5, trans_time=2,
            time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=1.35, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        hatcher.facial(group=MAIN, index=100, auto_lip=True, extra_delay=0)

        # m06_briefing 110: Trent.
        # Самую важную в вашей жизни, мисс Хетчер? Не забывайте что конкретные исполнители - мы, и вот как
        # исполнители мы хотели бы подробностей о предшествующих ликвидации профессора этапах.
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_trent_front'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_trent_front'), duration=1.3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        cam_trent.set(group=MAIN, time_delay=t)
        cam_trent.move_cam(group=MAIN, index=2, duration=13, smooth=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_GESTR_THMBSUP_000LV_XA_02, duration=4, time_scale=0.7,
            time_delay=t)
        t += 4
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=3,
            time_scale=0.7, trans_time=0.5, time_delay=t)
        t += 2
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_HOLD_000LV_XA_02, duration=3, time_scale=0.7,
            trans_time=0.5, loop=True, time_delay=t)
        t += 6.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=infopanel_monitor.name,
            target_name=self.get_automarker_name('monitor_start_point'), duration=0.01, smooth=False,
            adjust_pos=True, adjust_orient=False, time_delay=t)
        trent.facial(group=MAIN, index=110, auto_lip=True, extra_delay=0)
        main_group.append_time(0.2)

        # m06_briefing 120: Hatcher.
        # Хорошо, Трент. Итак, проникновение внутрь Сферы. Охраняется она беспрецедентно. Я сомневаюсь, что
        # кайзер Рейнланда охраняется так же как она.
        t = 0
        cam_hatcher.set(group=MAIN, time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, object_name=infopanel_monitor.name,
            target_name=self.get_automarker_name('monitor_viewpoint'), duration=10, smooth=True, adjust_pos=True,
            adjust_orient=False, time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, object_name=cam_hatcher.name,
            target_name=self.get_automarker_name('cam_hatcher_brief_pos1'), duration=15, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('cam_hatcher_focus'),
            target_name=self.get_automarker_name('cam_hatcher_brief_marker_pos1'), duration=15, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 2.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 6
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('hatcher_front'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        hatcher.facial(group=MAIN, index=120, auto_lip=True, extra_delay=0)

        # m06_briefing 130: Hatcher.
        # Рядом со сферой находится военная база, представляющая собою верфь, способную принимать по два
        # линкора и четыре корабля среднего тоннажа одновременно. Понимаете, какая там развернута группировка?
        # Поэтому силовое решение невозможно.
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=infopanel_shipyard_view.name,
            target_name=self.get_automarker_name('monitor_viewpoint'), duration=0.01, smooth=False,
            adjust_pos=True, adjust_orient=False, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, duration=7,
            time_scale=0.7, trans_time=0.25, time_delay=t)
        t += 2
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_CONV_RHND_CASL_000LV_xa_03, duration=6,
            time_scale=0.75, trans_time=1, loop=True, time_delay=t)
        t += 2.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 1.5
        hatcher.motion(group=MAIN, anim=Female.Sc_FMHAND_NEUT_RGHT_000LV_A_00, duration=2, trans_time=0.25,
            time_delay=t)
        t += 2
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_01, duration=3,
            time_scale=0.75, trans_time=1, time_delay=t)
        t += 1
        hatcher.motion(group=MAIN, anim=Female.Sc_FMHAND_HNEUT_GESTR_CASL_000LV_00, duration=6, time_scale=0.8,
            trans_time=0.25, loop=True, time_delay=t)
        t += 1.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('hatcher_front'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        hatcher.facial(group=MAIN, index=130, auto_lip=True, extra_delay=0)

        # m06_briefing 140: Hatcher.
        # Для проникновения вам понадобятся устройства, которые находятся в контейнерах, переданных мною вам
        # перед стыковкой с Миссури. Это устройства, делающие ваши корабли невидимыми как визуально, так и
        # всеми радарными системами.
        t = 0.5
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=3,
            time_scale=0.4, trans_time=0.5, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=infopanel_shipyard_view.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=1e-05, smooth=False,
            adjust_pos=True, adjust_orient=False, time_delay=t)
        t += 1e-05
        MoveEvent(root=self, group=MAIN, object_name=infopanel_stealth_connection.name,
            target_name=self.get_automarker_name('monitor_viewpoint'), duration=1e-06, smooth=False,
            adjust_pos=True, adjust_orient=False, time_delay=t)
        t += 2.99999
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_FSTHIPB_HOLD_000LV_XA_01, duration=4,
            time_scale=0.6, trans_time=0.5, loop=True, time_delay=t)
        t += 5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 1
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=2,
            time_scale=0.5, trans_time=0.5, time_delay=t)
        hatcher.facial(group=MAIN, index=140, auto_lip=True, extra_delay=0)
        # Действие после исходного окна реплики.
        t = 0
        cam_stealth.set(group=MAIN, time_delay=t)
        cam_stealth.move_cam(group=MAIN, index=2, duration=8, smooth=True, time_delay=t)
        main_group.append_time(0.5)

        # m06_briefing 150: Hatcher.
        # Они создают вокруг корабля локальное искривление пространства, и ваши корабли как бы перестают
        # находиться в нашей реальности.
        t = 0.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('hatcher_front'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 4
        MoveEvent(root=self, group=MAIN, object_name=infopanel_stealth_connection.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0.01, smooth=False,
            adjust_pos=True, adjust_orient=False, time_delay=t)
        t += 0.01
        MoveEvent(root=self, group=MAIN, object_name=ship_monitor.name,
            target_name=self.get_automarker_name('monitor_viewpoint'), duration=0.01, smooth=False,
            adjust_pos=True, adjust_orient=False, time_delay=t)
        line_sound = self.lookup_single_sound(150)
        SoundEvent(root=self, group=MAIN, sound_name=line_sound.get_nickname())
        main_group.append_time(7.5)

        # m06_briefing 160: Hatcher.
        # Смонтируете их у себя на кораблях - просто устанавливаете где-нибудь внутри герметичного корпуса,
        # подключаете к энергосистеме и выводите кнопку управления в удобное место приборной доски. Кнопка
        # всего одна, не ошибетесь.
        t = 0
        cam_hatcher.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=cam_hatcher.name,
            target_name=self.get_automarker_name('cam_hatcher_brief_pos2'), duration=25, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('cam_hatcher_focus'),
            target_name=self.get_automarker_name('cam_hatcher_brief_marker_pos2'), duration=25, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 1.5
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_CROSS_ARMS_000LV_xa_03, duration=3.6,
            time_scale=0.8, trans_time=0.5, time_delay=t)
        t += 3.6
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_HOLD_ARMS_CROSSED_000LV_XA_03, duration=3.4,
            time_scale=0.8, trans_time=0.5, loop=True, time_delay=t)
        t += 1.9
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 1.5
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_UNCRSS_ARMS_000LV_XA_03, duration=8, time_scale=0.8,
            trans_time=0.5, time_delay=t)
        hatcher.facial(group=MAIN, index=160, auto_lip=True, extra_delay=0)

        # m06_briefing 170: Hatcher.
        # Нажимаете один раз - и ваш корабль невидим, нажимаете второй раз - и он снова видим. Проблема
        # устройства в его одноразовости.
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('hatcher_front'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 0.5
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, duration=7,
            time_scale=0.7, trans_time=0.25, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMHAND_HNEUT_GESTR_CASL_000LV_00, duration=7, time_scale=0.8,
            trans_time=0.25, loop=True, time_delay=t)
        t += 2
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_CONV_RHND_CASL_000LV_xa_03, duration=3,
            time_scale=0.75, trans_time=1, loop=True, time_delay=t)
        t += 3
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_01, duration=3,
            time_scale=0.75, trans_time=1, time_delay=t)
        hatcher.facial(group=MAIN, index=170, auto_lip=True, extra_delay=0)

        # m06_briefing 180: Hatcher.
        # Я не ученый, поэтому скажу просто, после выключения там что-то перегорает, и оно превращается в
        # коробочку с горелым пластиком и обугленным  металлом.
        t = 0.5
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=3,
            time_scale=0.4, trans_time=0.5, time_delay=t)
        t += 3
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_FSTHIPB_HOLD_000LV_XA_01, duration=4,
            time_scale=0.6, trans_time=0.5, loop=True, time_delay=t)
        t += 3
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=10, loop=True, time_delay=t)
        hatcher.facial(group=MAIN, index=180, auto_lip=True, extra_delay=0)

        # m06_briefing 190: Trent.
        # Огнетушителями запасаться?
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=190, auto_lip=True, extra_delay=0)

        # m06_briefing 200: Hatcher.
        # Нет, все безопасно, все происходит внутри устройства, даже неприятного запаха не появится.
        t = 0
        cam_hatcher.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=cam_hatcher.name,
            target_name=self.get_automarker_name('cam_hatcher_brief_pos3'), duration=25, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('cam_hatcher_focus'),
            target_name=self.get_automarker_name('cam_hatcher_brief_marker_pos1'), duration=25, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        cam_hatcher.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=5,
            time_scale=0.7, trans_time=0.5, time_delay=t)
        t += 3.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        hatcher.facial(group=MAIN, index=200, auto_lip=True, extra_delay=0)
        main_group.append_time(0.5)

        # m06_briefing 210: Hatcher.
        # По времени работы. Поскольку устройство одноразовое, постарайтесь использовать его максимально
        # эффективно. Наши головастики гарантируют тридцать минут работы. Возможно, оно проработает сорок,
        # больше вряд ли.
        t = 0.5
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_CROSS_ARMS_000LV_xa_03, duration=3.6,
            time_scale=0.8, trans_time=0.5, time_delay=t)
        t += 3.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('hatcher_front'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 0.1
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_HOLD_ARMS_CROSSED_000LV_XA_03, duration=6.4,
            time_scale=0.8, trans_time=0.5, loop=True, time_delay=t)
        t += 6.4
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_UNCRSS_ARMS_000LV_XA_03, duration=8, time_scale=0.8,
            trans_time=0.5, time_delay=t)
        hatcher.facial(group=MAIN, index=210, auto_lip=True, extra_delay=0)

        # m06_briefing 220: Hatcher.
        # Если тридцати минут работы не хватило, вы можете попробовать оставаться в невидимости дольше на свой
        # страх и риск. Если устройство сгорит не во время выключения, а во время работы, локальное
        # искривление пространства схлопывается вместе с кораблём.
        t = 0.5
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, duration=7,
            time_scale=0.7, trans_time=0.25, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMHAND_HNEUT_GESTR_CASL_000LV_00, duration=7, time_scale=0.8,
            trans_time=0.25, loop=True, time_delay=t)
        t += 2
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_CONV_RHND_CASL_000LV_xa_03, duration=3,
            time_scale=0.75, trans_time=1, loop=True, time_delay=t)
        t += 1.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 1.5
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_01, duration=1,
            time_scale=0.75, trans_time=1, time_delay=t)
        t += 4.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('hatcher_front'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('alaric_head_ik'),
            target_name=self.get_automarker_name('head_hatcher'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('alaric_eye_ik'),
            target_name=self.get_automarker_name('head_hatcher'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 5
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=10, loop=True, time_delay=t)
        hatcher.facial(group=MAIN, index=220, auto_lip=True, extra_delay=0)
        main_group.append_time(0.5)

        # m06_briefing 230: Alaric.
        # И куда попадает корабль? В другое измерение?
        t = 0
        cam_alaric.set(group=MAIN, time_delay=t)
        alaric.facial(group=MAIN, index=230, auto_lip=True, extra_delay=0)

        # m06_briefing 240: Hatcher.
        # Понятия не имею. Хотите узнать, мистер Аларик? По глазам вижу, что нет. И да, еще один момент. При
        # включенном устройстве стрелять бесполезно. Выши выстрелы не покинут локальную зону искривления
        # пространства.
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=0.9, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        cam_hatcher.set(group=MAIN, time_delay=t)
        t += 0.5
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=3,
            time_scale=0.9, trans_time=0.5, time_delay=t)
        t += 2.5
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_FSTHIPB_HOLD_000LV_XA_01, duration=3,
            time_scale=0.8, trans_time=0.5, loop=True, time_delay=t)
        t += 3
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('hatcher_front'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=3,
            time_scale=0.6, trans_time=0.5, time_delay=t)
        t += 8
        MoveEvent(root=self, group=MAIN, object_name=ship_monitor.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0.01, smooth=False,
            adjust_pos=True, adjust_orient=False, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=infopanel_monitor.name,
            target_name=self.get_automarker_name('monitor_start_point'), duration=10, smooth=True,
            adjust_pos=True, adjust_orient=False, time_delay=t)
        t += 1
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, duration=7,
            time_scale=0.7, trans_time=0.25, time_delay=t)
        hatcher.facial(group=MAIN, index=240, auto_lip=True, extra_delay=0)

        # m06_briefing 250: Hatcher.
        # Вот трехмерный план Сферы и все данные по ней, которые нам удалось собрать.
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=cam_hatcher.name,
            target_name=self.get_automarker_name('cam_hatcher_brief_pos4'), duration=5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('cam_hatcher_focus'),
            target_name=self.get_automarker_name('cam_hatcher_brief_marker_pos4'), duration=5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=sphere_map.name,
            target_name=self.get_automarker_name('sphere_projector_viewpoint'), duration=0.01, smooth=False,
            adjust_pos=True, adjust_orient=False, time_delay=t)
        t += 0.001
        RotateAxisEvent(root=self, group=MAIN, object_name=sphere_map.name, angle=-360, axis='Y_AXIS',
            duration=19, smooth=False, time_delay=t)
        t += 0.999
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_CONV_RHND_CASL_000LV_xa_03, duration=3,
            time_scale=0.75, trans_time=1, loop=True, time_delay=t)
        t += 3
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_01, duration=2,
            time_scale=0.75, trans_time=1, time_delay=t)
        hatcher.facial(group=MAIN, index=250, auto_lip=True, extra_delay=0)
        # Действие после исходного окна реплики.
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('alaric_head_ik'),
            target_name=self.get_automarker_name('sphere_projector_viewpoint'), duration=2, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('alaric_eye_ik'),
            target_name=self.get_automarker_name('sphere_projector_viewpoint'), duration=1.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        main_group.append_time(1)

        # m06_briefing 260: Alaric.
        # Вот это хреновина...
        t = 0
        cam_alaric.set(group=MAIN, time_delay=t)
        t += 3
        MoveEvent(root=self, group=MAIN, object_name=infopanel_monitor.name,
            target_name=self.get_automarker_name('monitor_start_point'), duration=0.01, smooth=False,
            adjust_pos=True, adjust_orient=False, time_delay=t)
        alaric.facial(group=MAIN, index=260, auto_lip=True, extra_delay=0)

        # m06_briefing 270: Hatcher.
        # Я рада, что вы прониклись, мистер Аларик. Загрузите всё к себе в компьютер. В ходе операции будете
        # передавать нужные данные мистеру Тренту.
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        cam_hatcher.set(group=MAIN, time_delay=t)
        t += 8
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('hatcher_front'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        hatcher.facial(group=MAIN, index=270, auto_lip=True, extra_delay=0)

        # m06_briefing 280: Hatcher.
        # Ну и последнее - после прибытия на территорию Рейнланда никаких радиопереговоров со мной или с кем-
        # то еще на территории Либерти. Вас запеленгуют их радарные станции, и миссия завершится так и не
        # начавшись.
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=cam_hatcher.name,
            target_name=self.get_automarker_name('cam_hatcher_final_pos1'), duration=10, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('cam_hatcher_focus'),
            target_name=self.get_automarker_name('cam_hatcher_final_marker_pos1'), duration=10, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.1
        MoveEvent(root=self, group=MAIN, object_name=sphere_map.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0.01, smooth=False,
            adjust_pos=True, adjust_orient=False, time_delay=t)
        t += 2.9
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 4
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('hatcher_front'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 4
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=3,
            time_scale=0.4, trans_time=0.5, time_delay=t)
        hatcher.facial(group=MAIN, index=280, auto_lip=True, extra_delay=0)

        # m06_briefing 290: Hatcher.
        # Вот, собственно, и всё. По коням, джентльмены.
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=cam_hatcher.name,
            target_name=self.get_automarker_name('cam_hatcher_final_pos2'), duration=5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('cam_hatcher_focus'),
            target_name=self.get_automarker_name('cam_hatcher_final_marker_pos2'), duration=5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 2
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        hatcher.facial(group=MAIN, index=290, auto_lip=True, extra_delay=0)
