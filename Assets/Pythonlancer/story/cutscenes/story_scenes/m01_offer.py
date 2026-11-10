from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story import actors


class Propglass(Prop):
    COMPOUND_TEMPLATE_NAME = 'glass'


class OfferScene(Scene):
    DUMP_FILE = 'm01_offer'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=20, look_duration=200)
        cam_alaric2 = LookAtCamera(root=self, name='cam_alaric2', fov=20, look_duration=200)
        cam_alaric = LookAtCamera(root=self, name='cam_alaric', fov=20, look_duration=200)
        cam_default = LookAtCamera(root=self, name='cam_default', fov=20, look_duration=200)
        cam_sit = LookAtCamera(root=self, name='cam_sit', fov=25, look_duration=200)
        cam_alaric_talking = LookAtCamera(root=self, name='cam_alaric_talking', fov=20, look_duration=200)
        cam_trent_talking = LookAtCamera(root=self, name='cam_trent_talking', fov=20, look_duration=200)
        cam_trent_drinking = LookAtCamera(root=self, name='cam_trent_drinking', fov=20, look_duration=200)
        cam_full_scene = LookAtCamera(root=self, name='cam_full_scene', fov=20, look_duration=200)

        alaric = Character(root=self, actor=actors.Alaric, light_group=0, init_point='char_alaric', rotate_from_quat=True)
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='char_trent_real', rotate_from_quat=True)

        trent_glass = Propglass(root=self, name='trent_glass', init_point='trent_glass', light_group=0, rotate_from_quat=True)


        t = 0
        MoveFastEvent(root=self, group=MAIN, object_name='Char_trent', target_name=self.get_automarker_name('trent_pos'), time_delay=t)
        cam_sit.set(group=MAIN, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name='Char_alaric', target_name='Char_trent', duration=5, time_delay=t, target_type=TARGET_PART, target_part='Body_Neck')
        NeckIkEvent(root=self, group=MAIN, char_name='Char_trent', target_name='Char_alaric', duration=5, time_delay=t, target_type=TARGET_PART, target_part='Body_Neck')
        cam_sit.move_focus(group=MAIN, index=2, duration=7, smooth=True, time_delay=t)
        cam_sit.move_cam(group=MAIN, index=2, duration=7, smooth=True, time_delay=t)
        self._m(trent, 'Sc_MLBODY_STND_SITCR_TRNS_180DN_XA_06', t, 10, scale=1.25)
        self._m(alaric, 'Sc_MLBODY_CHRB_WAVE_LHND_000LV_XA_03', t, 10, scale=0.6)
        main_group.append_time(1)

        t = 0
        self._m(alaric, 'Sc_dx_s038x_3001_kress', t, 2.7)
        t += 2
        self._m(alaric, 'Sc_MLHAND_HNEUT_EDGE_LEFT_000LV_00', t, 1)
        self._m(alaric, 'Sc_MLHAND_HNEUT_EDGE_RGHT_000LV_00', t, 1)
        t += 0.5
        self._m(trent, 'Sc_dx_s006x_0401_trent', t, 2)
        alaric.facial(group=MAIN, index=10, auto_lip=True)

        t = 0
        self._m(alaric, 'Sc_MLHEAD_CONCNTRTE_000LV_XA_%', t, 1, trans=1)
        EyeIkEvent(root=self, group=MAIN, char_name='Char_alaric', target_name='trent_glass', duration=4, time_delay=t, target_type=TARGET_ROOT)
        t += 0.5
        self._m(trent, 'Sc_MLBODY_CHRB_IDLE_BIG_000LV_XA_05', t, 5, trans=1)
        trent.facial(group=MAIN, index=20, auto_lip=True)

        t = 0
        self._m(alaric, 'Sc_MLBODY_CHRB_PUSH_DRINK_TABL_000LV_XA_06', t, 10, trans=0.25)
        self._m(alaric, 'Sc_dx_s038x_2501_kress', t, 3)
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_0010', time_delay=t)
        t += 1.499
        MoveFastEvent(root=self, group=MAIN, object_name='trent_glass', target_name=self.get_automarker_name('marker_trent_glass_last'), time_delay=t)
        cam_alaric_talking.set(group=MAIN, time_delay=t)
        self._m(alaric, 'Sc_dx_s038x_1701_kress', t, 10)
        t += 0.5
        t += 2
        EyeIkEvent(root=self, group=MAIN, char_name='Char_alaric', target_name='head_trent', duration=5, time_delay=t, target_type=TARGET_ROOT)
        self._m(alaric, 'Sc_MLHEAD_NEUT_BLINK_EYES_HALF_000LV_A_00', t, 2)
        t += 2
        self._m(alaric, 'Sc_MLHEAD_NEUT_BLINK_EYES_HALF_000LV_A_00', t, 2)
        self._m(alaric, 'Sc_MLBODY_CHRB_IDLE_MED_000LV_XA_07', t, 10, trans=2)
        self._m(trent, 'Sc_MLBODY_CHRB_LSTN_000LV_A_19', t, 3)
        EyeIkEvent(root=self, group=MAIN, char_name='Char_trent', target_name='head_alaric', duration=8, time_delay=t, target_type=TARGET_ROOT)
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_0030', time_delay=t)
        alaric.facial(group=MAIN, index=30, auto_lip=True)

        t = 0
        cam_trent_drinking.set(group=MAIN, time_delay=t)
        cam_trent_drinking.move_cam(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        self._m(trent, 'Sc_dx_s034x_1301_Trent', t, 6, trans=0.25)
        t += 2.5
        self._m(trent, 'Sc_MLBODY_CHRB_GRABL_DRINK_TABL_000LV_XA_02', t, 3, trans=2)
        t += 0.501
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_0040a', time_delay=t)
        t += 2.999
        self._m(trent, 'Sc_dx_s026c_0301_Trent', t, 6, trans=0.25)
        t += 1.5
        EyeIkEvent(root=self, group=MAIN, char_name='Char_trent', target_name='trent_glass', duration=3, time_delay=t, target_type=TARGET_ROOT)
        NeckIkEvent(root=self, group=MAIN, char_name='Char_trent', target_name='trent_glass', duration=3, time_delay=t, target_type=TARGET_ROOT)
        t += 1
        self._m(trent, 'Sc_MLBODY_CHRB_DRINK_LHND_SIP_000LV_XA_04', t, 10, trans=1)
        self._m(trent, 'Sc_MLHAND_HNEUT_HOLDD_LEFT_000LV_00', t, 0.2, scale=10, trans=0.25)
        ConnectHardpointEvent(root=self, group=MAIN, target_name='trent_glass', parent_name='Char_trent', duration=4, target_hardpoint='hpleftconnect_prop_glass_green', parent_hardpoint='hpleftconnect', time_delay=t)
        t += 0.501
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_0040b', time_delay=t)
        t += 0.499
        self._m(trent, 'Sc_MLHEAD_MOTION_DRINK_SWALLOW_TRENT_000LV_XA_%', t, 2, trans=0.25)
        t += 1
        EyeIkEvent(root=self, group=MAIN, char_name='Char_trent', target_name='head_alaric', duration=4, time_delay=t, target_type=TARGET_ROOT)
        trent.facial(group=MAIN, index=40, auto_lip=True)

        t = 0
        self._m(trent, 'Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01', t, 3, trans=0.25)
        self._m(trent, 'Sc_MLHAND_NEUT_LEFT_000LV_A_00', t, 3, trans=0.25)
        cam_alaric_talking.set(group=MAIN, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name='Char_alaric', target_name='head_trent', duration=10, time_delay=t, target_type=TARGET_ROOT)
        cam_alaric_talking.move_cam(group=MAIN, index=2, duration=8, smooth=True, time_delay=t)
        self._m(alaric, 'Sc_MLBODY_CHRB_CONV_RHNDUP_TRNS_000LV_XA_02', t, 10, scale=0.5, start=1)
        self._m(alaric, 'Sc_dx_s038x_1701_Kress', t, 10)
        t += 1
        self._m(alaric, 'Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00', t, 10, scale=0.75)
        t += 1
        self._m(alaric, 'Sc_MLBODY_CHRB_CONV_RHND_CASL_000LV_xb_02', t, 2, scale=0.5, trans=0.25)
        t += 2
        self._m(alaric, 'Sc_MLBODY_CHRB_CONV_RHNDDN_TRNS_000LV_XA_02', t, 10, scale=0.5, trans=1)
        alaric.facial(group=MAIN, index=50, auto_lip=True)

        t = 0
        self._m(alaric, 'Sc_MLBODY_CHRB_TALK_000UP_A_17', t, 5, scale=0.5, trans=1)
        self._m(alaric, 'Sc_dx_s038x_3402_kress', t, 10, trans=0.25)
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_0050', time_delay=t)
        t += 3.999
        self._m(alaric, 'Sc_MLBODY_CHRF_TALK_HNSTBL_000LV_A_34', t, 7, trans=1)
        EyeIkEvent(root=self, group=MAIN, char_name='Char_trent', target_name='head_alaric', duration=12, time_delay=t, target_type=TARGET_ROOT)
        EyeIkEvent(root=self, group=MAIN, char_name='Char_alaric', target_name='head_trent', duration=12, time_delay=t, target_type=TARGET_ROOT)
        alaric.facial(group=MAIN, index=60, auto_lip=True)

        t = 0
        cam_full_scene.set(group=MAIN, time_delay=t)
        cam_full_scene.move_cam(group=MAIN, index=2, duration=15, smooth=True, time_delay=t)
        self._m(alaric, 'Sc_dx_s038x_1801_kress', t, 10, trans=0.25)
        self._m(trent, 'Sc_MLBODY_CHRB_LSTN_000UP_A_18', t, 12)
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_0060', time_delay=t)
        t += 2.499
        self._m(alaric, 'Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00', t, 12, trans=0.25)
        t += 2
        cam_full_scene.move_focus(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        t += 2
        self._m(alaric, 'Sc_MLBODY_CHRF_CONV_RHNDUP_TRNS_000LV_XA_02', t, 10, trans=2)
        alaric.facial(group=MAIN, index=70, auto_lip=True)

        t = 0
        self._m(alaric, 'Sc_dx_s038x_1801_kress', t, 10, trans=0.25)
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_0070', time_delay=t)
        t += 0.499
        self._m(alaric, 'Sc_MLBODY_CHRF_CONV_RHND_CASL_000LV_XA_04', t, 4, trans=1)
        t += 2
        self._m(alaric, 'Sc_MLHAND_HNEUT_POINT_RGHT_CASL_000LV_00', t, 12, trans=0.25)
        t += 2
        self._m(alaric, 'Sc_MLBODY_CHRF_CONV_RHNDDN_TRNS_000LV_XA_02', t, 12, trans=1)
        t += 0.5
        self._m(alaric, 'Sc_MLHAND_NEUT_RGHT_000LV_A_00', t, 12, trans=1)
        alaric.facial(group=MAIN, index=80, auto_lip=True)

        t = 0
        cam_trent_talking.set(group=MAIN, time_delay=t)
        self._m(alaric, 'Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02', t, 10, trans=1)
        self._m(trent, 'Sc_MLBODY_CHRB_GRABR_CHIN_RLEASE_000LV_XA_01', t, 10, scale=0.8)
        self._m(trent, 'Sc_MLHAND_NEUT_WALK_RGHT_000LV_XB_%', t, 10)
        self._m(trent, 'Sc_dx_s034x_1301_Trent', t, 5)
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_0080', time_delay=t)
        t += 2.299
        self._m(trent, 'Sc_MLBODY_CHRB_CHIN_HOLDR_000LV_XA_04', t, 10, trans=0.25)
        t += 2.651
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_0090', time_delay=t)
        t += 0.049
        self._m(trent, 'Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01', t, 0.5, trans=0.5)
        trent.facial(group=MAIN, index=90, auto_lip=True)

        main_group.append_time(2)

    def _m(self, char, anim, delay, duration, scale=1, start=0, trans=None):
        char.motion(group=MAIN, anim=anim, duration=duration, time_delay=delay,
                    time_scale=scale, start_time=start, trans_time=trans)

