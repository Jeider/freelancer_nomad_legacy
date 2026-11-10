from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story import actors


class Propglass(Prop):
    COMPOUND_TEMPLATE_NAME = 'glass'


class BizmarkScene(Scene):
    DUMP_FILE = 'm01_bizmark'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        cam_entry = LookAtCamera(root=self, name='cam_entry', fov=25, look_duration=200)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=15, look_duration=200)
        cam_luc = LookAtCamera(root=self, name='cam_luc', fov=15, look_duration=200)
        cam_luc_big = LookAtCamera(root=self, name='cam_luc_big', fov=30, look_duration=200)
        cam_roll = LookAtCamera(root=self, name='cam_roll', fov=25, look_duration=200)
        cam_alaric = LookAtCamera(root=self, name='cam_alaric', fov=20, look_duration=200)
        cam_luc_ship = LookAtCamera(root=self, name='cam_luc_ship', fov=15, look_duration=200)
        cam_goaway = LookAtCamera(root=self, name='cam_goaway', fov=25, look_duration=200)
        cam_bar_start = LookAtCamera(root=self, name='cam_bar_start', fov=25, look_duration=200)
        cam_bar_alaric = LookAtCamera(root=self, name='cam_bar_alaric', fov=25, look_duration=200)
        cam_bar_trent = LookAtCamera(root=self, name='cam_bar_trent', fov=25, look_duration=200)
        cam_bar_alaric_expl = LookAtCamera(root=self, name='cam_bar_alaric_expl', fov=25, look_duration=200)
        cam_bar_final = LookAtCamera(root=self, name='cam_bar_final', fov=35, look_duration=200)

        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True)
        alaric = Character(root=self, actor=actors.Alaric, light_group=0, init_point='Char_alaric', rotate_from_quat=True)
        luc = Character(root=self, actor=actors.Luc, light_group=0, init_point='Char_luc', rotate_from_quat=True)
        adelmar = Character(root=self, actor=actors.Adelmar, light_group=0, init_point='Char_adelmar', rotate_from_quat=True)

        luc_glass = Propglass(root=self, name='luc_glass', init_point='luc_glass', light_group=0, rotate_from_quat=True)
        trent_glass = Propglass(root=self, name='trent_glass', init_point='trent_glass', light_group=0, rotate_from_quat=True)

        Path_cam_entry = MotionPath(root=self, name='Path_cam_entry', path_data='{-3.1, 6, 2.25}, {0.5,0,-0.5,0}, {-2.4, 4, 3.35}, {0.8,0,-0.2,0}, {-0.8, 3, 3.65}, {0.8,0,0.2,0}, {0.7, 3, 2.25}, {0.5,0,0.5,0}')
        Path_cam_roll = MotionPath(root=self, name='Path_cam_roll', path_data='{-3.1, 3, 2.25}, {0.5,0,-0.5,0}, {-2.4, 3, 3.35}, {0.8,0,-0.2,0}, {-0.8, 3, 3.65}, {0.8,0,0.2,0}, {0.7, 3, 2.25}, {0.5,0,0.5,0}')

        t = 0
        cam_entry.set(group=MAIN, time_delay=t)
        cam_entry.move_focus(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name='Char_trent', target_name='Char_adelmar', duration=15, time_delay=t, target_type=TARGET_HARDPOINT, target_part='hp_neck')
        self._m(trent, 'Sc_MLBODY_STND_IDLE_000LV_xa_04', t, 15)
        self._m(alaric, 'Sc_MLBODY_STND_IDLE_000LV_XB_04', t, 25)
        self._m(adelmar, 'Sc_MLBODY_STND_IDLE_000LV_xa_04', t, 25, start=1)
        self._m(luc, 'Sc_MLBODY_STND_HOLDDRNKL_TOAST_000LV_XA_06', t, 1, start=2)
        ConnectHardpointEvent(root=self, group=MAIN, target_name='luc_glass', parent_name='Char_luc', duration=600, target_hardpoint='hpleftconnect_prop_glass_green', parent_hardpoint='hpleftconnect', time_delay=t)
        self._m(luc, 'Sc_MLHAND_HNEUT_HOLDD_LEFT_000LV_00', t, 0.2, scale=10, trans=0.25)
        NeckIkEvent(root=self, group=MAIN, char_name='Char_adelmar', target_name='adelmar_head_ik', duration=150, time_delay=t, target_type=TARGET_ROOT)
        EyeIkEvent(root=self, group=MAIN, char_name='Char_adelmar', target_name='adelmar_eye_ik', duration=150, time_delay=t, target_type=TARGET_ROOT)
        NeckIkEvent(root=self, group=MAIN, char_name='Char_luc', target_name='luc_head_ik', duration=46, time_delay=t, target_type=TARGET_ROOT)
        EyeIkEvent(root=self, group=MAIN, char_name='Char_luc', target_name='luc_eye_ik', duration=150, time_delay=t, target_type=TARGET_ROOT)
        t += 6
        self._m(luc, 'Sc_MLHEAD_HAPPY_SMILE_PLEASD_000LV_XA_%', t, 15, scale=0.5)
        main_group.append_time(7)

        t = 0
        self._m(adelmar, 'Sc_dx_s021x_1302_tobias', t, 4)
        MoveFastEvent(root=self, group=MAIN, object_name='luc_eye_ik', target_name=self.get_automarker_name('head_alaric'), time_delay=t)
        t += 0.5
        MoveFastEvent(root=self, group=MAIN, object_name='adelmar_eye_ik', target_name=self.get_automarker_name('head_alaric'), time_delay=t)
        t += 0.5
        MoveFastEvent(root=self, group=MAIN, object_name='luc_head_ik', target_name=self.get_automarker_name('head_alaric'), time_delay=t)
        t += 0.5
        self._m(adelmar, 'Sc_dx_s021x_1302_tobias', t, 4, trans=0.25)
        MoveFastEvent(root=self, group=MAIN, object_name='adelmar_head_ik', target_name=self.get_automarker_name('head_alaric'), time_delay=t)
        t += 3
        cam_trent.set(group=MAIN, time_delay=t)
        self._m(trent, 'Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01', t, 3)
        adelmar.facial(group=MAIN, index=10, auto_lip=True)

        t = 0
        self._m(trent, 'Sc_dx_s038x_3101_trent', t, 6, start=1, trans=0.25)
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_0010', time_delay=t)
        t += 0.999
        self._m(trent, 'Sc_MLBODY_STND_FSTHIPB_HOLD_000LV_XA_02', t, 31, trans=1)
        t += 0.5
        self._m(trent, 'Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00', t, 6, scale=0.3, trans=0.25)
        trent.facial(group=MAIN, index=20, auto_lip=True)

        t = 0
        cam_luc.set(group=MAIN, time_delay=t)
        self._m(luc, 'Sc_dx_s059x_1004_jonner', t, 6)
        MoveFastEvent(root=self, group=MAIN, object_name='luc_eye_ik', target_name=self.get_automarker_name('head_trent'), time_delay=t)
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_0020', time_delay=t)
        t += 0.999
        MoveFastEvent(root=self, group=MAIN, object_name='luc_head_ik', target_name=self.get_automarker_name('head_trent_alaric_half'), time_delay=t)
        t += 2
        self._m(luc, 'Sc_MLBODY_STND_POINTR_LHNDDN_000LV_XA_04', t, 15, trans=1)
        t += 0.5
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_0030a', time_delay=t)
        self._m(luc, 'Sc_dx_s059x_1004_jonner', t, 3, start=1, trans=0.25)
        MoveFastEvent(root=self, group=MAIN, object_name='luc_eye_ik', target_name=self.get_automarker_name('head_alaric'), time_delay=t)
        t += 0.5
        MoveFastEvent(root=self, group=MAIN, object_name='adelmar_eye_ik', target_name=self.get_automarker_name('head_trent'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='adelmar_head_ik', target_name=self.get_automarker_name('head_trent_alaric_half'), time_delay=t)
        t += 0.5
        MoveFastEvent(root=self, group=MAIN, object_name='luc_head_ik', target_name=self.get_automarker_name('head_alaric'), time_delay=t)
        t += 0.5
        NeckIkEvent(root=self, group=MAIN, char_name='Char_trent', target_name='Char_luc', duration=7, time_delay=t, target_type=TARGET_HARDPOINT, target_part='hp_neck')
        NeckIkEvent(root=self, group=MAIN, char_name='Char_alaric', target_name='alaric_head_ik', duration=50, time_delay=t, target_type=TARGET_ROOT)
        EyeIkEvent(root=self, group=MAIN, char_name='Char_alaric', target_name='alaric_eye_ik', duration=50, time_delay=t, target_type=TARGET_ROOT)
        t += 1
        cam_luc_big.set(group=MAIN, time_delay=t)
        cam_luc_big.move_cam(group=MAIN, index=2, duration=6, smooth=True, time_delay=t)
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_0030b', time_delay=t)
        t += 0.499
        MoveFastEvent(root=self, group=MAIN, object_name='adelmar_eye_ik', target_name=self.get_automarker_name('head_luc'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='adelmar_head_ik', target_name=self.get_automarker_name('head_luc'), time_delay=t)
        luc.facial(group=MAIN, index=30, auto_lip=True)

        t = 0
        MoveFastEvent(root=self, group=MAIN, object_name='luc_eye_ik', target_name=self.get_automarker_name('head_trent_alaric_half'), time_delay=t)
        self._m(luc, 'Sc_dx_s059x_1004_jonner', t, 6, trans=0.25)
        self._m(luc, 'Sc_MLBODY_STND_HOLDDRNKL_TOAST_000LV_XA_06', t, 5, trans=0.25)
        t += 1
        MoveFastEvent(root=self, group=MAIN, object_name='adelmar_eye_ik', target_name=self.get_automarker_name('head_trent'), time_delay=t)
        t += 2
        MoveFastEvent(root=self, group=MAIN, object_name='adelmar_head_ik', target_name=self.get_automarker_name('head_trent'), time_delay=t)
        t += 1
        MoveFastEvent(root=self, group=MAIN, object_name='luc_head_ik', target_name=self.get_automarker_name('head_alaric_adelmar_half'), time_delay=t)
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_0040', time_delay=t)
        luc.facial(group=MAIN, index=40, auto_lip=True)

        t = 0
        MoveFastEvent(root=self, group=MAIN, object_name='luc_eye_ik', target_name=self.get_automarker_name('head_adelmar'), time_delay=t)
        cam_alaric.set(group=MAIN, time_delay=t)
        cam_alaric.move_cam(group=MAIN, index=2, duration=15, smooth=True, time_delay=t)
        cam_alaric.move_focus(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        self._m(alaric, 'Sc_dx_s037a_2001_tobias', t, 5, scale=1.25, start=0.5)
        self._m(alaric, 'Sc_MLBODY_STND_GESTR_THMBSUP_000LV_XA_02', t, 25)
        self._m(alaric, 'Sc_MLHAND_HNEUT_GESTR_THUMB_000LV_00', t, 25)
        MoveFastEvent(root=self, group=MAIN, object_name='adelmar_eye_ik', target_name=self.get_automarker_name('head_alaric'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_head_ik', target_name=self.get_automarker_name('head_luc_adelmar_half'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_eye_ik', target_name=self.get_automarker_name('head_adelmar'), time_delay=t)
        t += 0.5
        MoveFastEvent(root=self, group=MAIN, object_name='adelmar_head_ik', target_name=self.get_automarker_name('head_alaric'), time_delay=t)
        t += 0.5
        self._m(trent, 'Sc_MLBODY_STND_IDLE_000LV_xa_04', t, 25, trans=1)
        t += 0.5
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_head_ik', target_name=self.get_automarker_name('head_luc_trent_half'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_eye_ik', target_name=self.get_automarker_name('head_luc'), time_delay=t)
        t += 0.5
        MoveFastEvent(root=self, group=MAIN, object_name='luc_head_ik', target_name=self.get_automarker_name('head_alaric'), time_delay=t)
        t += 0.5
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_eye_ik', target_name=self.get_automarker_name('head_trent'), time_delay=t)
        t += 0.5
        MoveFastEvent(root=self, group=MAIN, object_name='luc_eye_ik', target_name=self.get_automarker_name('head_alaric'), time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name='Char_trent', target_name='trent_head_ik', duration=40, time_delay=t, target_type=TARGET_ROOT)
        EyeIkEvent(root=self, group=MAIN, char_name='Char_trent', target_name='trent_eye_ik', duration=40, time_delay=t, target_type=TARGET_ROOT)
        self._m(alaric, 'Sc_dx_s038x_4201_kress', t, 4.8, trans=0.25)
        t += 1
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_0050a', time_delay=t)
        self._m(alaric, 'Sc_MLBODY_STND_CONV_LHNDUP_TRNS_000LV_XA_01', t, 25)
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_head_ik', target_name=self.get_automarker_name('head_luc'), time_delay=t)
        t += 0.5
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_eye_ik', target_name=self.get_automarker_name('head_luc'), time_delay=t)
        t += 0.5
        MoveFastEvent(root=self, group=MAIN, object_name='luc_eye_ik', target_name=self.get_automarker_name('head_trent_alaric_half'), time_delay=t)
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_0040', time_delay=t)
        self._m(alaric, 'Sc_MLBODY_STND_CONV_LHND_CASL_000LV_xc_01', t, 3, trans=0.5)
        self._m(alaric, 'Sc_MLHAND_HNEUT_GESTL_CASL_000LV_00', t, 10)
        t += 0.5
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_eye_ik', target_name=self.get_automarker_name('head_adelmar'), time_delay=t)
        t += 1.5
        MoveFastEvent(root=self, group=MAIN, object_name='luc_eye_ik', target_name=self.get_automarker_name('head_alaric'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_head_ik', target_name=self.get_automarker_name('head_luc_adelmar_half'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_eye_ik', target_name=self.get_automarker_name('head_luc'), time_delay=t)
        t += 0.8
        self._m(alaric, 'Sc_dx_s037a_2001_tobias', t, 2.8, scale=1.25, start=0.5, trans=0.25)
        t += 0.2
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_0050b', time_delay=t)
        self._m(alaric, 'Sc_MLBODY_STND_CONV_LHND_EMPH_000LV_XA_02', t, 5, scale=0.75, trans=1)
        self._m(alaric, 'Sc_MLHAND_HNEUT_POINT_LEFT_CASL_000LV_00', t, 1, trans=0.25)
        t += 1
        self._m(alaric, 'Sc_MLHAND_NEUT_LEFT_000LV_A_00', t, 1, trans=0.25)
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_eye_ik', target_name=self.get_automarker_name('head_trent'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='trent_eye_ik', target_name=self.get_automarker_name('head_alaric'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='trent_head_ik', target_name=self.get_automarker_name('head_alaric_adelmar_half'), time_delay=t)
        t += 1
        self._m(alaric, 'Sc_MLBODY_STND_CONV_LHNDDN_TRNS_000LV_XA_01', t, 5, trans=1)
        t += 0.5
        self._m(alaric, 'Sc_dx_s038x_4201_kress', t, 4.5, start=2, trans=0.25)
        t += 1.5
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_head_ik', target_name=self.get_automarker_name('head_trent'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_eye_ik', target_name=self.get_automarker_name('head_luc_trent_half'), time_delay=t)
        t += 1
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_0050c', time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_head_ik', target_name=self.get_automarker_name('head_luc_adelmar_half'), time_delay=t)
        t += 1.5
        cam_trent.set(group=MAIN, time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='trent_head_ik', target_name=self.get_automarker_name('head_luc_adelmar_half'), time_delay=t)
        t += 0.5
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_eye_ik', target_name=self.get_automarker_name('head_luc'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='trent_eye_ik', target_name=self.get_automarker_name('head_luc'), time_delay=t)
        alaric.facial(group=MAIN, index=50, auto_lip=True)

        t = 0
        self._m(trent, 'Sc_dx_s050d_0201_trent', t, 6, trans=0.25)
        self._m(trent, 'Sc_dx_s046x_0601_trent', t, 6, trans=0.25)
        t += 1.5
        self._m(trent, 'Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01', t, 1, trans=1)
        t += 1
        MoveFastEvent(root=self, group=MAIN, object_name='Char_luc', target_name=self.get_automarker_name('luc_pos2'), time_delay=t)
        self._m(luc, 'Sc_MLBODY_STND_IDLE_000LV_xa_04', t, 0.5)
        t += 0.501
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_09', time_delay=t)
        t += 0.499
        MoveFastEvent(root=self, group=MAIN, object_name='Char_adelmar', target_name=self.get_automarker_name('adelmar_pos'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='Char_trent', target_name=self.get_automarker_name('trent_prebar'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='Char_alaric', target_name=self.get_automarker_name('alaric_prebar'), time_delay=t)
        cam_luc_ship.set(group=MAIN, time_delay=t)
        cam_luc_ship.move_cam(group=MAIN, index=2, duration=13, smooth=True, time_delay=t)
        self._m(alaric, 'Sc_MLBODY_STND_IDLE_000LV_xa_04', t, 10)
        self._m(trent, 'Sc_MLBODY_STND_IDLE_000LV_xa_04', t, 10)
        self._m(luc, 'Sc_MLBODY_STND_TURN_045LV_XA_04', t, 15, scale=0.75)
        MoveFastEvent(root=self, group=MAIN, object_name='luc_eye_ik', target_name=self.get_automarker_name('head_trent'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='trent_head_ik', target_name=self.get_automarker_name('head_luc2'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='trent_eye_ik', target_name=self.get_automarker_name('head_luc2'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_head_ik', target_name=self.get_automarker_name('head_luc2'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_eye_ik', target_name=self.get_automarker_name('head_luc2'), time_delay=t)
        t += 0.75
        self._m(luc, 'Sc_dx_s033x_0801_dexter', t, 6, scale=0.75, trans=0.5)
        trent.facial(group=MAIN, index=60, auto_lip=True)

        t = 0
        self._m(adelmar, 'Sc_MLBODY_STND_TURN_045LV_XA_04', t, 15, scale=0.75)
        MoveFastEvent(root=self, group=MAIN, object_name='adelmar_head_ik', target_name=self.get_automarker_name('outpoint'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='adelmar_eye_ik', target_name=self.get_automarker_name('outpoint'), time_delay=t)
        t += 3
        self._m(luc, 'Sc_MLBODY_STND_IDLE_BRTH_000LV_xa_05', t, 3.5, trans=1)
        t += 1
        self._m(luc, 'Sc_dx_s033x_0503_dexter', t, 6, trans=0.5)
        self._m(adelmar, 'Sc_MLBODY_STND_IDLE_000LV_xa_04', t, 9, trans=0.5)
        t += 2.5
        self._m(luc, 'Sc_MLBODY_STND_GESTL_STOP_000LV_XA_03', t, 15, trans=0.5)
        t += 0.5
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_10', time_delay=t)
        t += 0.5
        self._m(luc, 'Sc_dx_s032d_0301_dexter', t, 6, trans=0.5)
        t += 2.5
        self._m(luc, 'Sc_MLBODY_STND_NOPE_000LV_A_02', t, 15, trans=0.5)
        t += 2
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_11', time_delay=t)
        self._m(luc, 'Sc_MLBODY_STND_IDLE_BRTH_000LV_xa_05', t, 1, trans=0.2)
        t += 1
        self._m(luc, 'Sc_MLBODY_STND_WALK_TRNS_090LV_XA_02', t, 15, scale=0.75, trans=1)
        MoveFastEvent(root=self, group=MAIN, object_name='luc_head_ik', target_name=self.get_automarker_name('outpoint'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='luc_eye_ik', target_name=self.get_automarker_name('outpoint'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='trent_head_ik', target_name=self.get_automarker_name('head_luc2_walk'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='trent_eye_ik', target_name=self.get_automarker_name('head_luc2_walk'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_head_ik', target_name=self.get_automarker_name('head_luc2_walk'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_eye_ik', target_name=self.get_automarker_name('head_luc2_walk'), time_delay=t)
        cam_goaway.set(group=MAIN, time_delay=t)
        cam_goaway.move_focus(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        luc.facial(group=MAIN, index=70, auto_lip=True)

        t = 0
        self._m(adelmar, 'Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01', t, 15, scale=0.75, trans=0.5)
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_eye_ik', target_name=self.get_automarker_name('head_trent'), time_delay=t)
        self._m(trent, 'Sc_dx_s050d_0201_trent', t, 6, trans=0.25)
        t += 1.2
        self._m(adelmar, 'Sc_MLBODY_WLKG_000LV_XA_01', t, 15, scale=0.75, trans=0.5)
        t += 0.3
        self._m(trent, 'Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01', t, 6, trans=1)
        t += 0.5
        MoveFastEvent(root=self, group=MAIN, object_name='trent_head_ik', target_name=self.get_automarker_name('trent_front'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='trent_eye_ik', target_name=self.get_automarker_name('trent_front'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_head_ik', target_name=self.get_automarker_name('alaric_front'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_eye_ik', target_name=self.get_automarker_name('alaric_front'), time_delay=t)
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_12', time_delay=t)
        t += 1
        self._m(trent, 'Sc_MLBODY_STND_IDLE_LHNDUP_000LV_XA_03', t, 6, scale=1.25, trans=0.25)
        t += 1
        self._m(alaric, 'Sc_MLBODY_STND_2STEP_FRWD_TRNS_000LV_XA_02', t, 6, scale=0.8, trans=0.25)
        t += 1.5
        self._m(trent, 'Sc_MLBODY_STND_2STEP_FRWD_TRNS_000LV_XA_02', t, 3.4, scale=0.85, trans=0.25)
        t += 3.5
        MoveOffscreenEvent(root=self, group=MAIN, object_name='luc', time_delay=t)
        MoveOffscreenEvent(root=self, group=MAIN, object_name='adelmar', time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='trent_glass', target_name=self.get_automarker_name('trent_glass_placement'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='Char_trent', target_name=self.get_automarker_name('bar_trent'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='Char_alaric', target_name=self.get_automarker_name('bar_alaric'), time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name='Char_trent', target_name='trent_head_ik', duration=7, time_delay=t, target_type=TARGET_ROOT)
        EyeIkEvent(root=self, group=MAIN, char_name='Char_trent', target_name='trent_eye_ik', duration=10, time_delay=t, target_type=TARGET_ROOT)
        NeckIkEvent(root=self, group=MAIN, char_name='Char_alaric', target_name='alaric_head_ik', duration=145, time_delay=t, target_type=TARGET_ROOT)
        EyeIkEvent(root=self, group=MAIN, char_name='Char_alaric', target_name='alaric_eye_ik', duration=145, time_delay=t, target_type=TARGET_ROOT)
        cam_bar_start.set(group=MAIN, time_delay=t)
        cam_bar_start.move_cam(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        cam_bar_start.move_focus(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        self._m(alaric, 'Sc_MLBODY_STND_LEAN_BAR_TRNS_000LV_XA_02', t, 15, scale=0.5)
        self._m(trent, 'Sc_MLBODY_STND_IDLE_000LV_xa_04', t, 4)
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_head_ik', target_name=self.get_automarker_name('bar_trent_front'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_eye_ik', target_name=self.get_automarker_name('bar_head_trent'), time_delay=t)
        trent.facial(group=MAIN, index=80, auto_lip=True)

        t = 0
        self._m(alaric, 'Sc_dx_s038x_4201_kress', t, 4.8, start=3, trans=0.25)
        t += 1
        MoveFastEvent(root=self, group=MAIN, object_name='trent_eye_ik', target_name=self.get_automarker_name('bar_head_alaric'), time_delay=t)
        t += 0.5
        MoveFastEvent(root=self, group=MAIN, object_name='trent_head_ik', target_name=self.get_automarker_name('bar_front_half'), time_delay=t)
        alaric.facial(group=MAIN, index=90, auto_lip=True)

        t = 0
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_13', time_delay=t)
        self._m(trent, 'Sc_dx_s029x_1201_trent', t, 10, trans=0.25)
        t += 0.5
        self._m(trent, 'Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01', t, 15, scale=0.75, trans=0.1)
        t += 1
        MoveFastEvent(root=self, group=MAIN, object_name='trent_head_ik', target_name=self.get_automarker_name('bar_trent_front'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='trent_eye_ik', target_name=self.get_automarker_name('bar_trent_front'), time_delay=t)
        t += 1.5
        self._m(trent, 'Sc_dx_s045c_0301_trent', t, 10, trans=0.25)
        t += 0.3
        self._m(trent, 'Sc_MLBODY_STND_PUT_GLAS_000LV_A_11', t, 1.375, start=2.8, trans=1)
        t += 0.2
        self._m(trent, 'Sc_MLHAND_HNEUT_HOLDD_LEFT_000LV_00', t, 1.335, trans=0.3)
        MoveFastEvent(root=self, group=MAIN, object_name='trent_eye_ik', target_name=self.get_automarker_name('trent_glass'), time_delay=t)
        t += 1
        self._m(trent, 'Sc_MLBODY_STND_DRINK_LHND_LARG_000LV_XA_06', t, 6, scale=1.1, trans=1)
        ConnectHardpointEvent(root=self, group=MAIN, target_name='trent_glass', parent_name='Char_trent', duration=18.5, target_hardpoint='hpleftconnect_prop_glass_green', parent_hardpoint='hpleftconnect', time_delay=t)
        t += 0.4
        self._m(trent, 'Sc_MLHEAD_MOTION_DRINK_SWALLOW_TRENT_000LV_XA_%', t, 2, trans=0.3)
        t += 1.6
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_14', time_delay=t)
        trent.facial(group=MAIN, index=100, auto_lip=True)

        t = 0
        cam_bar_alaric.set(group=MAIN, time_delay=t)
        cam_bar_alaric.move_cam(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        cam_bar_alaric.move_focus(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        self._m(alaric, 'Sc_dx_s038x_2301_kress', t, 3.5, trans=0.25)
        self._m(alaric, 'Sc_MLBODY_LEAN_STND_BAR_TRNS_000LV_XA_03', t, 15)
        t += 3
        self._m(alaric, 'Sc_MLBODY_STND_LEAN_ARMB_090LV_A_08', t, 7, scale=0.5, trans=0.5)
        t += 0.5
        self._m(alaric, 'Sc_dx_s038x_2301_kress', t, 10, trans=0.25)
        t += 0.5
        NeckIkEvent(root=self, group=MAIN, char_name='Char_trent', target_name='trent_head_ik', duration=44.5, time_delay=t, target_type=TARGET_ROOT)
        EyeIkEvent(root=self, group=MAIN, char_name='Char_trent', target_name='trent_eye_ik', duration=44.5, time_delay=t, target_type=TARGET_ROOT)
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_15', time_delay=t)
        t += 3
        MoveFastEvent(root=self, group=MAIN, object_name='Char_trent', target_name=self.get_automarker_name('bar_trent'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='trent_eye_ik', target_name=self.get_automarker_name('bar_head_alaric'), time_delay=t)
        t += 2
        self._m(trent, 'Sc_MLBODY_STND_HOLDD_000LV_A_08', t, 3)
        alaric.facial(group=MAIN, index=110, auto_lip=True)

        t = 0
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_16', time_delay=t)
        cam_bar_trent.set(group=MAIN, time_delay=t)
        self._m(trent, 'Sc_dx_s038x_2602_trent', t, 2.25, trans=0.25)
        MoveFastEvent(root=self, group=MAIN, object_name='trent_head_ik', target_name=self.get_automarker_name('bar_front_half'), time_delay=t)
        t += 2
        self._m(trent, 'Sc_MLBODY_STND_PUTDNL_DRINK_BAR_000LV_XA_06', t, 15, trans=1)
        t += 0.25
        self._m(trent, 'Sc_dx_s037b_0401_trent', t, 10, trans=0.25)
        t += 0.75
        MoveFastEvent(root=self, group=MAIN, object_name='trent_head_ik', target_name=self.get_automarker_name('trent_glass_placement_upper'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='trent_eye_ik', target_name=self.get_automarker_name('trent_glass_placement'), time_delay=t)
        t += 0.5
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_17', time_delay=t)
        t += 0.5
        self._m(alaric, 'Sc_MLBODY_STND_IDLE_000LV_xa_04', t, 1)
        t += 1
        self._m(trent, 'Sc_MLHAND_HNEUT_HOLDD_LEFT_000LV_00', t, 1, start=9, trans=0.3)
        self._m(trent, 'Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01', t, 6, trans=1)
        MoveFastEvent(root=self, group=MAIN, object_name='Char_alaric', target_name=self.get_automarker_name('bar_alaric'), time_delay=t)
        t += 1
        MoveFastEvent(root=self, group=MAIN, object_name='trent_head_ik', target_name=self.get_automarker_name('bar_trent_front_right'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='trent_eye_ik', target_name=self.get_automarker_name('bar_trent_front_right'), time_delay=t)
        t += 0.5
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_18', time_delay=t)
        trent.facial(group=MAIN, index=120, auto_lip=True)

        t = 0
        cam_bar_alaric_expl.set(group=MAIN, time_delay=t)
        cam_bar_alaric_expl.move_cam(group=MAIN, index=2, duration=15, smooth=True, time_delay=t)
        cam_bar_alaric_expl.move_focus(group=MAIN, index=2, duration=15, smooth=True, time_delay=t)
        cam_bar_alaric_expl.move_cam(group=MAIN, index=2, duration=15, smooth=True, time_delay=t)
        cam_bar_alaric_expl.move_focus(group=MAIN, index=2, duration=15, smooth=True, time_delay=t)
        self._m(alaric, 'Sc_dx_s038x_2301_kress', t, 10, start=2.5)
        self._m(alaric, 'Sc_MLBODY_STND_LEAN_ARMB_090LV_A_08', t, 15, scale=0.5, start=2)
        t += 2
        self._m(trent, 'Sc_MLBODY_STND_IDLE_000LV_xa_04', t, 14, trans=1)
        alaric.facial(group=MAIN, index=125, auto_lip=True)

        t = 0
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_19', time_delay=t)
        self._m(alaric, 'Sc_dx_s038x_2301_kress', t, 1.5, trans=0.25)
        t += 1.5
        self._m(alaric, 'Sc_dx_s038x_2301_kress', t, 10, trans=0.25)
        t += 2.5
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_20', time_delay=t)
        t += 1
        self._m(alaric, 'Sc_dx_s038x_2301_kress', t, 10, trans=0.25)
        t += 2.5
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_21', time_delay=t)
        t += 1.5
        self._m(alaric, 'Sc_MLBODY_STND_CONV_HNDSUP_TRNS_000LV_XA_00', t, 15, scale=0.5, trans=0.5)
        t += 1
        self._m(alaric, 'Sc_dx_s038x_3401_kress', t, 10, trans=0.25)
        t += 0.25
        self._m(alaric, 'Sc_MLBODY_STND_CONV_HNDS_CASL_000LV_xb_03', t, 15, scale=0.75, trans=0.5)
        self._m(alaric, 'Sc_MLHAND_HNEUT_GESTL_CASL_000LV_00', t, 15, trans=0.25)
        t += 1.75
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_22', time_delay=t)
        t += 0.5
        self._m(alaric, 'Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00', t, 15, trans=0.25)
        t += 0.5
        self._m(alaric, 'Sc_dx_s038x_3401_kress', t, 10, start=1, trans=0.25)
        t += 1.25
        self._m(alaric, 'Sc_MLBODY_STND_CONV_HNDSDN_TRNS_000LV_XA_01', t, 15, scale=0.5, trans=0.5)
        alaric.facial(group=MAIN, index=130, auto_lip=True)

        t = 0
        cam_bar_alaric_expl.move_cam(group=MAIN, index=3, duration=10, smooth=True, time_delay=t)
        cam_bar_alaric_expl.move_focus(group=MAIN, index=3, duration=10, smooth=True, time_delay=t)
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_23', time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_head_ik', target_name=self.get_automarker_name('bar_alaric_front_bottom'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_eye_ik', target_name=self.get_automarker_name('bar_alaric_front_bottom_deep'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='trent_eye_ik', target_name=self.get_automarker_name('bar_trent_front_left'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='trent_head_ik', target_name=self.get_automarker_name('bar_trent_front_left'), time_delay=t)
        self._m(alaric, 'Sc_dx_s038x_2301_kress', t, 3, trans=0.25)
        self._m(alaric, 'Sc_MLBODY_STND_LOOK_WATC_IMPA_000LV_A_23', t, 5, start=3, trans=0.5)
        t += 2
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_head_ik', target_name=self.get_automarker_name('bar_trent_front'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_eye_ik', target_name=self.get_automarker_name('bar_head_trent'), time_delay=t)
        t += 1
        self._m(alaric, 'Sc_dx_s038x_3401_kress', t, 10, trans=0.25)
        t += 1
        MoveFastEvent(root=self, group=MAIN, object_name='trent_head_ik', target_name=self.get_automarker_name('bar_trent_front'), time_delay=t)
        self._m(alaric, 'Sc_MLBODY_STND_TURN_315LV_XA_02', t, 5, trans=1)
        t += 1
        MoveFastEvent(root=self, group=MAIN, object_name='trent_eye_ik', target_name=self.get_automarker_name('bar_trent_front_lower'), time_delay=t)
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_24', time_delay=t)
        t += 1.5
        self._m(alaric, 'Sc_MLBODY_STND_IDLE_BRTH_000LV_xa_05', t, 2.5, trans=0.2)
        MoveFastEvent(root=self, group=MAIN, object_name='trent_head_ik', target_name=self.get_automarker_name('bar_front_half_lower'), time_delay=t)
        alaric.facial(group=MAIN, index=140, auto_lip=True)

        t = 0
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_25', time_delay=t)
        self._m(trent, 'Sc_dx_s070x_2001_trent', t, 0.5, trans=0.25)
        MoveFastEvent(root=self, group=MAIN, object_name='trent_eye_ik', target_name=self.get_automarker_name('bar_head_alaric'), time_delay=t)
        t += 0.5
        self._m(trent, 'Sc_dx_s076x_1401_trent', t, 10, trans=0.25)
        trent.facial(group=MAIN, index=150, auto_lip=True)

        t = 0
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_26', time_delay=t)
        self._m(trent, 'Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01', t, 6, trans=1)
        self._m(alaric, 'Sc_dx_s021x_0301_tobias', t, 3, scale=0.75, start=1, trans=0.25)
        self._m(alaric, 'Sc_MLBODY_STND_WALK_TRNS_270LV_XA_02', t, 15, trans=1)
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_head_ik', target_name=self.get_automarker_name('outpoint'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='alaric_eye_ik', target_name=self.get_automarker_name('outpoint'), time_delay=t)
        t += 1
        MoveFastEvent(root=self, group=MAIN, object_name='trent_head_ik', target_name=self.get_automarker_name('bar_trent_front'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='trent_eye_ik', target_name=self.get_automarker_name('bar_trent_front'), time_delay=t)
        self._m(alaric, 'Sc_MLBODY_WLKG_000LV_XA_01', t, 25, trans=1)
        t += 0.5
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_27', time_delay=t)
        t += 0.5
        cam_bar_final.set(group=MAIN, time_delay=t)
        cam_bar_final.move_cam(group=MAIN, index=2, duration=8, smooth=True, time_delay=t)
        cam_bar_final.move_focus(group=MAIN, index=2, duration=8, smooth=True, time_delay=t)
        t += 1
        self._m(trent, 'Sc_MLBODY_STND_TURN_180LV_XA_04', t, 15, trans=1)
        t += 4
        self._m(trent, 'Sc_MLBODY_STND_LOOK_AROU_000LV_XA_09', t, 15, trans=1)
        alaric.facial(group=MAIN, index=160, auto_lip=True)

        main_group.append_time(2)

    def _m(self, char, anim, delay, duration, scale=1, start=0, trans=None):
        char.motion(group=MAIN, anim=anim, duration=duration, time_delay=delay,
                    time_scale=scale, start_time=start, trans_time=trans)

