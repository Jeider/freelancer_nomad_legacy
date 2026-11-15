"""Bizmark reimport. Removed lines 30/40/50/60 are archived as comments.
No negative dialogue delays: each next speaker waits for the previous voice.
Original facial windows and non-dialogue pauses remain documented below.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (MAIN, LookAtCamera, MoveEvent,
    NeckIkEvent, EyeIkEvent, Prop, MotionPath, ConnectHardpointEvent, Light, LightAnimEvent)
from story.cutscenes.anim import Male
from story import actors
from story.cutscenes.ru_dialogue_timing import RuDialogueTiming, RuTimedCharacter as Character


class Propglass(Prop):
    COMPOUND_TEMPLATE_NAME = 'glass'


class BizmarkScene(Scene):
    DUMP_FILE = 'm01_bizmark'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        RuDialogueTiming(self).build(self._action_ru)

    def _action_ru(self):
        # Author all delays against RU; adaptation maps both event endpoints.
        main_group = self.get_group(MAIN)

        cam_entry = LookAtCamera(root=self, name='cam_entry', fov=25, look_duration=1000)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=15, look_duration=1000)
        cam_luc = LookAtCamera(root=self, name='cam_luc', fov=15, look_duration=1000)
        cam_luc_big = LookAtCamera(root=self, name='cam_luc_big', fov=30, look_duration=1000)
        cam_roll = LookAtCamera(root=self, name='cam_roll', fov=25, look_duration=1000)
        cam_alaric = LookAtCamera(root=self, name='cam_alaric', fov=20, look_duration=1000)
        cam_luc_ship = LookAtCamera(root=self, name='cam_luc_ship', fov=15, look_duration=1000)
        cam_goaway = LookAtCamera(root=self, name='cam_goaway', fov=25, look_duration=1000)
        cam_bar_start = LookAtCamera(root=self, name='cam_bar_start', fov=25, look_duration=1000)
        cam_bar_alaric = LookAtCamera(root=self, name='cam_bar_alaric', fov=25, look_duration=1000)
        cam_bar_trent = LookAtCamera(root=self, name='cam_bar_trent', fov=25, look_duration=1000)
        cam_bar_alaric_expl = LookAtCamera(root=self, name='cam_bar_alaric_expl', fov=25, look_duration=1000)
        cam_bar_final = LookAtCamera(root=self, name='cam_bar_final', fov=35, look_duration=1000)
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True, use_ambient=True, floor_height=1.39)
        alaric = Character(root=self, actor=actors.Alaric, light_group=0, init_point='Char_alaric', rotate_from_quat=True, use_ambient=True, floor_height=1.39)
        luc = Character(root=self, actor=actors.Luc, light_group=0, init_point='Char_luc', rotate_from_quat=True, use_ambient=True, floor_height=1.39)
        adelmar = Character(root=self, actor=actors.Adelmar, light_group=0, init_point='Char_adelmar', rotate_from_quat=True, use_ambient=True, floor_height=1.39)
        luc_glass = Propglass(root=self, name='luc_glass', init_point='luc_glass', light_group=0, rotate_from_quat=True, use_ambient=True)
        trent_glass = Propglass(root=self, name='trent_glass', init_point='trent_glass', light_group=0, rotate_from_quat=True, use_ambient=True)
        Path_cam_entry = MotionPath(root=self, name='Path_cam_entry', point_name='Path_cam_entry', path_data='{-3.1, 6, 2.25}, {0.5,0,-0.5,0}, {-2.4, 4, 3.35}, {0.8,0,-0.2,0}, {-0.8, 3, 3.65}, {0.8,0,0.2,0}, {0.7, 3, 2.25}, {0.5,0,0.5,0}')
        Path_cam_roll = MotionPath(root=self, name='Path_cam_roll', point_name='Path_cam_roll', path_data='{-3.1, 3, 2.25}, {0.5,0,-0.5,0}, {-2.4, 3, 3.35}, {0.8,0,-0.2,0}, {-0.8, 3, 3.65}, {0.8,0,0.2,0}, {0.7, 3, 2.25}, {0.5,0,0.5,0}')
        Light(root=self, name="additional_light", point_name="additional_light", extra_name="", light_group=0,
              diffuse=[0.786275, 0.758824, 0.776471], ambient=[0, 0, 0], direction=[0, 0, 1],
              color=[214, 187, 133], attenuation=[0.8999999762, 0, 0.0060000001], light_type='L_POINT', on=False,
              range=10, cutoff=25, theta=180)

        # Entrance, source 0..7s.
        t = 0
        # THN event 14, source 0s
        cam_entry.set(group=MAIN, time_delay=t)
        # THN event 15, source 0s
        Path_cam_entry.anim(group=MAIN, target_name='cam_entry', duration=11, start_percent=0, stop_percent=0.5, adjust_orient=True, smooth=True, time_delay=t)
        # THN event 16, source 0s
        MoveEvent(root=self, group=MAIN, object_name='automarker_cam_entry_focus', target_name='automarker_cam_entry_focus2', duration=10, smooth=True, time_delay=t)
        # THN event 17, source 0s
        # NeckIkEvent(root=self, group=MAIN, char_name='Char_trent', target_name='Char_adelmar', duration=15, transition_duration=1, target_type='HARDPOINT', target_part='hp_neck', up='NEG_Y_AXIS', front='Z_AXIS', time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name='Char_trent', target_name='automarker_trent_head_ik', duration=25, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', time_delay=t)

        MoveEvent(root=self, group=MAIN, object_name='automarker_trent_head_ik', target_name='automarker_head_adelmar', duration=1.5, smooth=True, time_delay=t)

        # THN event 18, source 0s
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=15, time_delay=t, time_scale=1, loop=True)
        # THN event 19, source 0s
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_XB_04, duration=25, time_delay=t, time_scale=1, loop=True)
        # THN event 20, source 0s
        adelmar.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=25, time_delay=t, time_scale=1, start_time=1, loop=True)
        # THN event 21, source 0s
        luc.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_HOLDDRNKL_TOAST_000LV_XA_06, duration=1, time_delay=t, time_scale=1, start_time=2)
        # THN event 22, source 0s
        ConnectHardpointEvent(root=self, group=MAIN, target_name='luc_glass', parent_name='Char_luc', duration=600, target_hardpoint='hpleftconnect_prop_glass_green', parent_hardpoint='hpleftconnect', time_delay=t)
        # THN event 23, source 0s
        luc.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_HOLDD_LEFT_000LV_00, duration=0.2, time_delay=t, time_scale=10, trans_time=0.25)
        # THN event 30, source 0s
        NeckIkEvent(root=self, group=MAIN, char_name='Char_adelmar', target_name='automarker_adelmar_head_ik', duration=150, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', time_delay=t)
        # THN event 31, source 0s
        EyeIkEvent(root=self, group=MAIN, char_name='Char_adelmar', target_name='automarker_adelmar_eye_ik', duration=150, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', time_delay=t)
        # THN event 32, source 0s
        NeckIkEvent(root=self, group=MAIN, char_name='Char_luc', target_name='automarker_luc_head_ik', duration=46, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', time_delay=t)
        # THN event 33, source 0s
        EyeIkEvent(root=self, group=MAIN, char_name='Char_luc', target_name='automarker_luc_eye_ik', duration=150, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', time_delay=t)
        t += 6
        # THN event 29, source 6s
        luc.motion(group=MAIN, anim=Male.Sc_MLHEAD_HAPPY_SMILE_PLEASD_000LV_XA_, duration=15, time_delay=t, time_scale=0.5)
        main_group.append_time(7)



        # Line 10, source 7..12s.
        t = 0
        # THN event 36, source 7s
        MoveEvent(root=self, group=MAIN, object_name='automarker_luc_eye_ik', target_name='automarker_head_alaric', duration=2, smooth=False, time_delay=t)
        t += 0.5
        # THN event 34, source 7.5s
        MoveEvent(root=self, group=MAIN, object_name='automarker_adelmar_eye_ik', target_name='automarker_head_alaric', duration=2, smooth=False, time_delay=t)
        t += 0.5
        # THN event 37, source 8s
        MoveEvent(root=self, group=MAIN, object_name='automarker_luc_head_ik', target_name='automarker_head_alaric', duration=3, smooth=False, time_delay=t)
        t += 0.5
        # THN event 35, source 8.5s
        MoveEvent(root=self, group=MAIN, object_name='automarker_adelmar_head_ik', target_name='automarker_head_alaric', duration=2.5, smooth=False, time_delay=t)
        t += 3
        # THN event 38, source 11.5s
        cam_trent.set(group=MAIN, time_delay=t)
        # THN event 39, source 11.5s
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=3, time_delay=t, time_scale=1)
        adelmar.facial(group=MAIN, index=10, auto_lip=True, extra_delay=1)
        # Original facial allocation 5.5s; source gap -0.5s.
        # Source overlap omitted: wait until the current voice finishes.

        # Line 20, source 12..15s.
        t = 0
        t += 1
        # THN event 40, source 13s
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_HOLD_000LV_XA_02, duration=31, time_delay=t, time_scale=1, trans_time=1)
        t += 0.5
        # THN event 45, source 13.5s
        trent.motion(group=MAIN, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=6, time_delay=t, time_scale=0.3, trans_time=0.25)
        trent.facial(group=MAIN, index=20, auto_lip=True, extra_delay=0)
        # Original facial allocation 6s; source gap -3s.
        # Source overlap omitted: wait until the current voice finishes.


        t = 0

        MoveEvent(root=self, group=MAIN, object_name='automarker_luc_head_ik', target_name='automarker_head_trent',
                  duration=2, smooth=False, time_delay=0.5)

        NeckIkEvent(root=self, group=MAIN, char_name='Char_alaric', target_name='automarker_alaric_head_ik', duration=25, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name='Char_alaric', target_name='automarker_alaric_eye_ik', duration=25, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', time_delay=t)
        # NeckIkEvent(root=self, group=MAIN, char_name='Char_trent', target_name='automarker_trent_head_ik', duration=25, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name='Char_trent', target_name='automarker_trent_eye_ik', duration=25, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', time_delay=t)
        trent.motion(group=MAIN, anim='Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01', duration=2, time_delay=0, time_scale=1, trans_time=1)

        MoveEvent(root=self, group=MAIN, object_name='automarker_trent_head_ik', target_name='automarker_head_luc2',
                  duration=1, smooth=False, time_delay=2.5)
        t = 0
        # THN event 138, source 45s
        MoveEvent(root=self, group=MAIN, object_name='Char_luc', target_name='automarker_luc_pos2', duration=0.001, smooth=False, time_delay=t)
        # THN event 139, source 45s
        luc.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=0.5, time_delay=t, time_scale=1)
        t += 1
        # THN event 140, source 46s
        MoveEvent(root=self, group=MAIN, object_name='Char_adelmar', target_name='automarker_adelmar_pos', duration=0.001, smooth=False, time_delay=t)
        # THN event 141, source 46s
        MoveEvent(root=self, group=MAIN, object_name='Char_trent', target_name='automarker_trent_prebar', duration=0.001, smooth=False, time_delay=t)
        # THN event 142, source 46s
        MoveEvent(root=self, group=MAIN, object_name='Char_alaric', target_name='automarker_alaric_prebar', duration=0.001, smooth=False, time_delay=t)
        # THN event 143, source 46s
        cam_luc_ship.set(group=MAIN, time_delay=t)
        # THN event 144, source 46s
        MoveEvent(root=self, group=MAIN, object_name='cam_luc_ship', target_name='automarker_cam_luc_ship2', duration=13, smooth=True, time_delay=t)
        # THN event 145, source 46s
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=10, time_delay=t, time_scale=1, loop=True)
        # THN event 146, source 46s
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=10, time_delay=t, time_scale=1, loop=True)
        # THN event 155, source 46s
        luc.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_TURN_045LV_XA_04, duration=15, time_delay=t, time_scale=0.75)
        # THN event 167, source 46s
        MoveEvent(root=self, group=MAIN, object_name='automarker_luc_eye_ik', target_name='automarker_head_trent', duration=2, smooth=True, time_delay=t)
        # THN event 170, source 46s
        MoveEvent(root=self, group=MAIN, object_name='automarker_trent_head_ik', target_name='automarker_head_luc2', duration=1, smooth=True, time_delay=t)
        # THN event 171, source 46s
        MoveEvent(root=self, group=MAIN, object_name='automarker_trent_eye_ik', target_name='automarker_head_luc2', duration=1, smooth=True, time_delay=t)
        # THN event 176, source 46s
        MoveEvent(root=self, group=MAIN, object_name='automarker_alaric_head_ik', target_name='automarker_head_luc2', duration=1, smooth=True, time_delay=t)
        # THN event 177, source 46s
        MoveEvent(root=self, group=MAIN, object_name='automarker_alaric_eye_ik', target_name='automarker_head_luc2', duration=1, smooth=True, time_delay=t)
        main_group.append_time(2)

        # Line 70, source 47..61s.
        t = 0
        # THN event 161, source 47s
        adelmar.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_TURN_045LV_XA_04, duration=15, time_delay=t, time_scale=0.75)
        # THN event 165, source 47s
        MoveEvent(root=self, group=MAIN, object_name='automarker_adelmar_head_ik', target_name='automarker_outpoint', duration=2, smooth=True, time_delay=t)
        # THN event 166, source 47s
        MoveEvent(root=self, group=MAIN, object_name='automarker_adelmar_eye_ik', target_name='automarker_outpoint', duration=2, smooth=True, time_delay=t)
        t += 3
        # THN event 156, source 50s
        luc.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_BRTH_000LV_xa_05, duration=3.5, time_delay=t, time_scale=1, trans_time=1)
        t += 1
        # THN event 162, source 51s
        adelmar.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=9, time_delay=t, time_scale=1, trans_time=0.5, loop=True)
        t += 2.5
        # THN event 157, source 53.5s
        luc.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_GESTL_STOP_000LV_XA_03, duration=15, time_delay=t, time_scale=1, trans_time=0.5)
        t += 3.5
        # THN event 158, source 57s
        luc.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_NOPE_000LV_A_02, duration=15, time_delay=t, time_scale=1, trans_time=0.5)
        t += 2
        # THN event 159, source 59s
        luc.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_BRTH_000LV_xa_05, duration=1, time_delay=t, time_scale=1, trans_time=0.2)
        t += 1
        # THN event 160, source 60s
        luc.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WALK_TRNS_090LV_XA_02, duration=15, time_delay=t, time_scale=0.75, trans_time=1)
        # THN event 168, source 60s
        MoveEvent(root=self, group=MAIN, object_name='automarker_luc_head_ik', target_name='automarker_outpoint', duration=2, smooth=True, time_delay=t)
        # THN event 169, source 60s
        MoveEvent(root=self, group=MAIN, object_name='automarker_luc_eye_ik', target_name='automarker_outpoint', duration=2, smooth=True, time_delay=t)
        # THN event 172, source 60s
        MoveEvent(root=self, group=MAIN, object_name='automarker_trent_head_ik', target_name='automarker_head_luc2_walk', duration=3, smooth=True, time_delay=t)
        # THN event 173, source 60s
        MoveEvent(root=self, group=MAIN, object_name='automarker_trent_eye_ik', target_name='automarker_head_luc2_walk', duration=2, smooth=True, time_delay=t)
        # THN event 178, source 60s
        MoveEvent(root=self, group=MAIN, object_name='automarker_alaric_head_ik', target_name='automarker_head_luc2_walk', duration=3, smooth=True, time_delay=t)
        # THN event 179, source 60s
        MoveEvent(root=self, group=MAIN, object_name='automarker_alaric_eye_ik', target_name='automarker_head_luc2_walk', duration=2, smooth=True, time_delay=t)
        # THN event 183, source 60s
        # cam_goaway.set(group=MAIN, time_delay=t)
        # THN event 184, source 60s
        MoveEvent(root=self, group=MAIN, object_name='automarker_cam_goaway_focus', target_name='automarker_cam_goaway_focus2', duration=10, smooth=True, time_delay=t)
        luc.facial(group=MAIN, index=70, auto_lip=True, extra_delay=0)
        # Original facial allocation 13.5s; source gap 0.5s.
        main_group.append_time(0.5)

        # Line 80, source 61..71s.
        t = 0
        # THN event 163, source 61s
        adelmar.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01, duration=15, time_delay=t+2, time_scale=0.75, trans_time=0.5)
        # THN event 180, source 61s
        MoveEvent(root=self, group=MAIN, object_name='automarker_alaric_eye_ik', target_name='automarker_head_trent', duration=1, smooth=True, time_delay=t)
        t += 1.2
        # THN event 164, source 62.2s
        adelmar.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=15, time_delay=t+2, time_scale=0.75, trans_time=0.5, loop=True)
        t += 0.3
        # THN event 189, source 62.5s
        trent.motion(group=MAIN, anim='Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01', duration=6, time_delay=t, time_scale=1, trans_time=1)
        t += 0.5
        # THN event 174, source 63s
        MoveEvent(root=self, group=MAIN, object_name='automarker_trent_head_ik', target_name='automarker_trent_front', duration=1.5, smooth=True, time_delay=t)
        # THN event 175, source 63s
        MoveEvent(root=self, group=MAIN, object_name='automarker_trent_eye_ik', target_name='automarker_trent_front', duration=1, smooth=True, time_delay=t)
        # THN event 181, source 63s
        MoveEvent(root=self, group=MAIN, object_name='automarker_alaric_head_ik', target_name='automarker_alaric_front', duration=4, smooth=True, time_delay=t)
        # THN event 182, source 63s
        MoveEvent(root=self, group=MAIN, object_name='automarker_alaric_eye_ik', target_name='automarker_alaric_front', duration=1, smooth=True, time_delay=t)
        t += 1
        # THN event 191, source 64s
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_LHNDUP_000LV_XA_03, duration=6, time_delay=t, time_scale=1.25, trans_time=0.25)
        t += 3
        # THN event 190, source 65s
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_2STEP_FRWD_TRNS_000LV_XA_02, duration=6, time_delay=t, time_scale=0.8, trans_time=0.25)
        # THN event 192, source 66.5s
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_2STEP_FRWD_TRNS_000LV_XA_02, duration=3.4, time_delay=t, time_scale=0.85, trans_time=0.25)
        trent.facial(group=MAIN, index=80, auto_lip=True, extra_delay=0)
        # Original facial allocation 6s; source gap 4s.
        t = 0
        t += 4.9999
        # THN event 193, source 69.9999s
        MoveEvent(root=self, group=MAIN, object_name='Char_luc', target_name='automarker_offscreen_point', duration=0.001, smooth=False, time_delay=t)
        # THN event 194, source 69.9999s
        MoveEvent(root=self, group=MAIN, object_name='Char_adelmar', target_name='automarker_offscreen_point', duration=0.001, smooth=False, time_delay=t)
        # THN event 195, source 69.9999s
        MoveEvent(root=self, group=MAIN, object_name='trent_glass', target_name='automarker_trent_glass_placement', duration=0.001, smooth=False, time_delay=t)
        # THN event 196, source 69.9999s
        MoveEvent(root=self, group=MAIN, object_name='Char_trent', target_name='automarker_bar_trent', duration=0.001, smooth=False, time_delay=t)
        # THN event 197, source 69.9999s
        MoveEvent(root=self, group=MAIN, object_name='Char_alaric', target_name='automarker_bar_alaric', duration=0.001, smooth=False, time_delay=t)
        t += 0.0001
        # THN event 198, source 70s
        LightAnimEvent(root=self, group=MAIN, object_name='additional_light', duration=0.001, on=True, time_delay=t)
        # THN event 199, source 70s
        NeckIkEvent(root=self, group=MAIN, char_name='Char_trent', target_name='automarker_trent_head_ik', duration=7, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', time_delay=t)
        # THN event 200, source 70s
        EyeIkEvent(root=self, group=MAIN, char_name='Char_trent', target_name='automarker_trent_eye_ik', duration=10, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', time_delay=t)
        # THN event 203, source 70s
        NeckIkEvent(root=self, group=MAIN, char_name='Char_alaric', target_name='automarker_alaric_head_ik', duration=145, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', time_delay=t)
        # THN event 204, source 70s
        EyeIkEvent(root=self, group=MAIN, char_name='Char_alaric', target_name='automarker_alaric_eye_ik', duration=145, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', time_delay=t)
        # THN event 205, source 70s
        cam_bar_start.set(group=MAIN, time_delay=t)
        # THN event 206, source 70s
        MoveEvent(root=self, group=MAIN, object_name='cam_bar_start', target_name='automarker_cam_bar_start2', duration=10, smooth=True, time_delay=t)
        # THN event 207, source 70s
        MoveEvent(root=self, group=MAIN, object_name='automarker_cam_bar_start_focus', target_name='automarker_cam_bar_start_focus2', duration=10, smooth=True, time_delay=t)
        # THN event 208, source 70s
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_LEAN_BAR_TRNS_000LV_XA_02, duration=15, time_delay=t, time_scale=0.5)
        # THN event 209, source 70s
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=4, time_delay=t, time_scale=1)
        # THN event 214, source 70s
        MoveEvent(root=self, group=MAIN, object_name='automarker_alaric_head_ik', target_name='automarker_bar_trent_front', duration=1, smooth=True, time_delay=t)
        # THN event 215, source 70s
        MoveEvent(root=self, group=MAIN, object_name='automarker_alaric_eye_ik', target_name='automarker_bar_head_trent', duration=1, smooth=True, time_delay=t)
        main_group.append_time(4)

        # Line 90, source 71..73.5s.
        t = 0
        t += 1
        # THN event 228, source 72s
        MoveEvent(root=self, group=MAIN, object_name='automarker_trent_eye_ik', target_name='automarker_bar_head_alaric', duration=1.5, smooth=True, time_delay=t)
        t += 0.5
        # THN event 229, source 72.5s
        MoveEvent(root=self, group=MAIN, object_name='automarker_trent_head_ik', target_name='automarker_bar_front_half', duration=1.5, smooth=True, time_delay=t)
        alaric.facial(group=MAIN, index=90, auto_lip=True, extra_delay=0)
        # Original facial allocation 4.8s; source gap -2.3s.
        # Source overlap omitted: wait until the current voice finishes.

        # Line 100, source 73.5..81s.
        t = 0
        t += 0.5
        # THN event 221, source 74s
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=15, time_delay=t, time_scale=0.75, trans_time=0.1)
        t += 1
        # THN event 230, source 75s
        MoveEvent(root=self, group=MAIN, object_name='automarker_trent_head_ik', target_name='automarker_bar_trent_front', duration=1.25, smooth=True, time_delay=t)
        # THN event 231, source 75s
        MoveEvent(root=self, group=MAIN, object_name='automarker_trent_eye_ik', target_name='automarker_bar_trent_front', duration=1.75, smooth=True, time_delay=t)
        t += 1.8
        # THN event 222, source 76.8s
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_PUT_GLAS_000LV_A_11, duration=1.375, time_delay=t, time_scale=1, start_time=2.8, trans_time=1)
        t += 0.2
        # THN event 223, source 77s
        trent.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_HOLDD_LEFT_000LV_00, duration=1.335, time_delay=t, time_scale=1, trans_time=0.3)
        # THN event 232, source 77s
        MoveEvent(root=self, group=MAIN, object_name='automarker_trent_eye_ik', target_name='trent_glass', duration=1, smooth=True, time_delay=t)
        t += 1
        # THN event 224, source 78s
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_DRINK_LHND_LARG_000LV_XA_06, duration=6, time_delay=t, time_scale=1.1, trans_time=1)
        # THN event 226, source 78s
        ConnectHardpointEvent(root=self, group=MAIN, target_name='trent_glass', parent_name='Char_trent', duration=16.4, target_hardpoint='hpleftconnect_prop_glass_green', parent_hardpoint='hpleftconnect', time_delay=t)
        t += 0.4
        # THN event 225, source 78.4s
        trent.motion(group=MAIN, anim='Sc_MLHEAD_MOTION_DRINK_SWALLOW_TRENT_000LV_XA_%', duration=2, time_delay=t+0.5, time_scale=1, trans_time=0.3)
        trent.facial(group=MAIN, index=100, auto_lip=True, extra_delay=0)
        # Original facial allocation 13s; source gap -5.5s.
        # Source overlap omitted: wait until the current voice finishes.

        # Line 110, source 81..91s.
        t = 0
        # THN event 233, source 81s
        cam_bar_alaric.set(group=MAIN, time_delay=t)
        # THN event 234, source 81s
        MoveEvent(root=self, group=MAIN, object_name='cam_bar_alaric', target_name='automarker_cam_bar_alaric2', duration=10, smooth=True, time_delay=t)
        # THN event 235, source 81s
        MoveEvent(root=self, group=MAIN, object_name='automarker_cam_bar_alaric_focus', target_name='automarker_cam_bar_alaric_focus2', duration=10, smooth=True, time_delay=t)
        # THN event 243, source 81s
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_LEAN_STND_BAR_TRNS_000LV_XA_03, duration=15, time_delay=t, time_scale=1)
        t += 3
        # THN event 244, source 84s
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_LEAN_ARMB_090LV_A_08, duration=7, time_delay=t, time_scale=0.5, trans_time=0.5)
        t += 1
        # THN event 201, source 85s
        NeckIkEvent(root=self, group=MAIN, char_name='Char_trent', target_name='automarker_trent_head_ik', duration=44.5, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', time_delay=t)
        # THN event 202, source 85s
        EyeIkEvent(root=self, group=MAIN, char_name='Char_trent', target_name='automarker_trent_eye_ik', duration=44.5, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', time_delay=t)
        t += 3
        # THN event 245, source 88s
        MoveEvent(root=self, group=MAIN, object_name='Char_trent', target_name='automarker_bar_trent', duration=0.001, smooth=False, time_delay=t)
        # THN event 258, source 88s
        MoveEvent(root=self, group=MAIN, object_name='automarker_trent_eye_ik', target_name='automarker_bar_head_alaric', duration=2, smooth=True, time_delay=t)
        t += 2
        # THN event 255, source 90s
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_HOLDD_000LV_A_08, duration=3, time_delay=t, time_scale=1)
        alaric.facial(group=MAIN, index=110, auto_lip=True, extra_delay=0)
        # Original facial allocation 13.5s; source gap -3.5s.
        # Source overlap omitted: wait until the current voice finishes.

        # Line 120, source 91..98s.
        t = 0
        # THN event 246, source 91s
        cam_bar_trent.set(group=MAIN, time_delay=t)
        # THN event 257, source 91s
        MoveEvent(root=self, group=MAIN, object_name='automarker_trent_head_ik', target_name='automarker_bar_front_half', duration=1, smooth=True, time_delay=t)
        t += 2
        # THN event 256, source 93s
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_PUTDNL_DRINK_BAR_000LV_XA_06, duration=15, time_delay=t, time_scale=1, trans_time=1)
        t += 1
        # THN event 259, source 94s
        MoveEvent(root=self, group=MAIN, object_name='automarker_trent_head_ik', target_name='automarker_trent_glass_placement_upper', duration=3, smooth=True, time_delay=t)
        # THN event 260, source 94s
        MoveEvent(root=self, group=MAIN, object_name='automarker_trent_eye_ik', target_name='automarker_trent_glass_placement', duration=2, smooth=True, time_delay=t)
        t += 1
        # THN event 263, source 95s
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=1, time_delay=t, time_scale=1)
        t += 1
        # THN event 227, source 96s
        trent.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_HOLDD_LEFT_000LV_00, duration=1, time_delay=t, time_scale=1, start_time=9, trans_time=0.3)
        # THN event 254, source 96s
        trent.motion(group=MAIN, anim='Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01', duration=6, time_delay=t, time_scale=1, trans_time=1)
        # THN event 264, source 96s
        MoveEvent(root=self, group=MAIN, object_name='Char_alaric', target_name='automarker_bar_alaric', duration=0.001, smooth=False, time_delay=t)
        t += 1
        # THN event 261, source 97s
        MoveEvent(root=self, group=MAIN, object_name='automarker_trent_head_ik', target_name='automarker_bar_trent_front_right', duration=1.5, smooth=True, time_delay=t)
        # THN event 262, source 97s
        MoveEvent(root=self, group=MAIN, object_name='automarker_trent_eye_ik', target_name='automarker_bar_trent_front_right', duration=1.25, smooth=True, time_delay=t)
        trent.facial(group=MAIN, index=120, auto_lip=True, extra_delay=0)
        # Original facial allocation 12.25s; source gap -5.25s.
        # Source overlap omitted: wait until the current voice finishes.

        # Line 125, source 98..101.5s.
        t = 0
        # THN event 266, source 98s
        cam_bar_alaric_expl.set(group=MAIN, time_delay=t)
        # THN event 267, source 98s
        MoveEvent(root=self, group=MAIN, object_name='cam_bar_alaric_expl', target_name='automarker_cam_bar_alaric_expl2', duration=15, smooth=True, time_delay=t)
        # THN event 268, source 98s
        MoveEvent(root=self, group=MAIN, object_name='automarker_cam_bar_alaric_expl_focus', target_name='automarker_cam_bar_alaric_expl_focus2', duration=15, smooth=True, time_delay=t)
        # THN event 269, source 98s
        MoveEvent(root=self, group=MAIN, object_name='cam_bar_alaric_expl', target_name='automarker_cam_bar_alaric_expl2', duration=15, smooth=True, time_delay=t)
        # THN event 270, source 98s
        MoveEvent(root=self, group=MAIN, object_name='automarker_cam_bar_alaric_expl_focus', target_name='automarker_cam_bar_alaric_expl_focus2', duration=15, smooth=True, time_delay=t)
        # THN event 291, source 98s
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_LEAN_ARMB_090LV_A_08, duration=15, time_delay=t, time_scale=0.5, start_time=2)
        t += 2
        # THN event 265, source 100s
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=14, time_delay=t, time_scale=1, trans_time=1, loop=True)
        alaric.facial(group=MAIN, index=125, auto_lip=True, extra_delay=0)
        # Original facial allocation 10s; source gap -6.5s.
        # Source overlap omitted: wait until the current voice finishes.

        # Line 130, source 101.5..117.5s.
        t = 0
        t += 9
        # THN event 292, source 110.5s
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_HNDSUP_TRNS_000LV_XA_00, duration=15, time_delay=t, time_scale=0.5, trans_time=0.5)
        t += 1.25
        # THN event 293, source 111.75s
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_HNDS_CASL_000LV_xb_03, duration=15, time_delay=t, time_scale=0.75, trans_time=0.5)
        # THN event 294, source 111.75s
        alaric.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_GESTL_CASL_000LV_00, duration=15, time_delay=t, time_scale=1, trans_time=0.25)
        t += 2.25
        # THN event 295, source 114s
        alaric.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00, duration=15, time_delay=t, time_scale=1, trans_time=0.25)
        t += 1.75
        # THN event 296, source 115.75s
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_HNDSDN_TRNS_000LV_XA_01, duration=15, time_delay=t, time_scale=0.5, trans_time=0.5)
        alaric.facial(group=MAIN, index=130, auto_lip=True, extra_delay=0)
        # Original facial allocation 23s; source gap -7s.
        # Source overlap omitted: wait until the current voice finishes.

        # Line 140, source 117.5..124.5s.
        t = 0
        # THN event 271, source 117.5s
        MoveEvent(root=self, group=MAIN, object_name='cam_bar_alaric_expl', target_name='automarker_cam_bar_alaric_expl3', duration=10, smooth=True, time_delay=t)
        # THN event 272, source 117.5s
        MoveEvent(root=self, group=MAIN, object_name='automarker_cam_bar_alaric_expl_focus', target_name='automarker_cam_bar_alaric_expl_focus3', duration=10, smooth=True, time_delay=t)
        # THN event 297, source 117.5s
        MoveEvent(root=self, group=MAIN, object_name='automarker_alaric_head_ik', target_name='automarker_bar_alaric_front_bottom', duration=2, smooth=True, time_delay=t)
        # THN event 298, source 117.5s
        MoveEvent(root=self, group=MAIN, object_name='automarker_alaric_eye_ik', target_name='automarker_bar_alaric_front_bottom_deep', duration=1, smooth=True, time_delay=t)
        # THN event 301, source 117.5s
        MoveEvent(root=self, group=MAIN, object_name='automarker_trent_eye_ik', target_name='automarker_bar_trent_front_left', duration=1, smooth=True, time_delay=t)
        # THN event 302, source 117.5s
        MoveEvent(root=self, group=MAIN, object_name='automarker_trent_head_ik', target_name='automarker_bar_trent_front_left', duration=1, smooth=True, time_delay=t)
        # THN event 312, source 117.5s
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_LOOK_WATC_IMPA_000LV_A_23, duration=5, time_delay=t, time_scale=1, start_time=3, trans_time=0.5)
        t += 2
        # THN event 299, source 119.5s
        MoveEvent(root=self, group=MAIN, object_name='automarker_alaric_head_ik', target_name='automarker_bar_trent_front', duration=1, smooth=True, time_delay=t)
        # THN event 300, source 119.5s
        MoveEvent(root=self, group=MAIN, object_name='automarker_alaric_eye_ik', target_name='automarker_bar_head_trent', duration=1, smooth=True, time_delay=t)
        t += 2
        # THN event 304, source 121.5s
        MoveEvent(root=self, group=MAIN, object_name='automarker_trent_head_ik', target_name='automarker_bar_trent_front', duration=2.8, smooth=True, time_delay=t)
        # THN event 313, source 121.5s
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_TURN_315LV_XA_02, duration=5, time_delay=t, time_scale=1, trans_time=1)
        t += 1
        # THN event 303, source 122.5s
        MoveEvent(root=self, group=MAIN, object_name='automarker_trent_eye_ik', target_name='automarker_bar_trent_front_lower', duration=1.8, smooth=True, time_delay=t)
        t += 1.5
        # THN event 314, source 124s
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_BRTH_000LV_xa_05, duration=2.5, time_delay=t, time_scale=1, trans_time=0.2)
        # THN event 321, source 124s
        MoveEvent(root=self, group=MAIN, object_name='automarker_trent_head_ik', target_name='automarker_bar_front_half_lower', duration=2, smooth=True, time_delay=t)
        alaric.facial(group=MAIN, index=140, auto_lip=True, extra_delay=0)
        # Original facial allocation 13s; source gap -6s.
        # Source overlap omitted: wait until the current voice finishes.

        # Line 150, source 124.5..126.5s.
        t = 0
        # THN event 322, source 124.5s
        MoveEvent(root=self, group=MAIN, object_name='automarker_trent_eye_ik', target_name='automarker_bar_head_alaric', duration=2, smooth=True, time_delay=t)
        trent.facial(group=MAIN, index=150, auto_lip=True, extra_delay=0)
        # Original facial allocation 10.5s; source gap -8.5s.
        # Source overlap omitted: wait until the current voice finishes.

        # Line 160, source 126.5..137s.
        # Physical exit: keep RU turn, walking speed and one-second lead-in.
        # Only the whole block follows the preceding dialogue; lipsync cannot compress it.
        with self._ru_dialogue_timing.fixed_actions(MAIN, minimum_duration=4):
            t = 0
            # THN event 320, source 126.5s
            trent.motion(group=MAIN, anim='Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01', duration=6, time_delay=t, time_scale=1, trans_time=1)
            # THN event 329, source 126.5s
            alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WALK_TRNS_270LV_XA_02, duration=15, time_delay=t, time_scale=1, trans_time=1)
            # THN event 331, source 126.5s
            MoveEvent(root=self, group=MAIN, object_name='automarker_alaric_head_ik', target_name='automarker_outpoint', duration=2, smooth=True, time_delay=t)
            # THN event 332, source 126.5s
            MoveEvent(root=self, group=MAIN, object_name='automarker_alaric_eye_ik', target_name='automarker_outpoint', duration=2, smooth=True, time_delay=t)
            t += 1
            # THN event 323, source 127.5s
            MoveEvent(root=self, group=MAIN, object_name='automarker_trent_head_ik', target_name='automarker_bar_trent_front', duration=2, smooth=True, time_delay=t)
            # THN event 324, source 127.5s
            MoveEvent(root=self, group=MAIN, object_name='automarker_trent_eye_ik', target_name='automarker_bar_trent_front', duration=2, smooth=True, time_delay=t)
            # THN event 330, source 127.5s
            alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=25, time_delay=t, time_scale=1, trans_time=1, loop=True)
            t += 1
            # THN event 335, source 128.5s
            # cam_bar_final.set(group=MAIN, time_delay=t)
            # THN event 336, source 128.5s
            MoveEvent(root=self, group=MAIN, object_name='cam_bar_final', target_name='automarker_cam_bar_final2', duration=8, smooth=True, time_delay=t)
            # THN event 337, source 128.5s
            MoveEvent(root=self, group=MAIN, object_name='automarker_cam_bar_final_focus', target_name='automarker_cam_bar_final_focus2', duration=8, smooth=True, time_delay=t)
        alaric.facial(group=MAIN, index=160, auto_lip=True, extra_delay=0)
        # Original facial allocation 3s; source gap 7.5s.
        t = 0
        main_group.append_time(3)

        return

        # THN event 333, source 129.5s
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_TURN_180LV_XA_04, duration=15, time_delay=t, time_scale=1, trans_time=1)
        MoveEvent(root=self, group=MAIN, object_name='automarker_trent_head_ik', target_name='automarker_final_look',
                  duration=3, smooth=True, time_delay=0)
        t += 4
        # THN event 334, source 133.5s
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_LOOK_AROU_000LV_XA_09, duration=15, time_delay=t, time_scale=1, trans_time=1)
        main_group.append_time(7.5)
