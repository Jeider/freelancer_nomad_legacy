"""Reimported from DATA/SCRIPTS/MOD/m01_berlin_bar.thn.

Dialogue uses relative time. Old facial windows define pauses/overlaps;
facial() supplies the current voice and lipsync. Blender: m01_berlin.blend.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (MAIN, Character, LookAtCamera, MoveEvent,
                                     NeckIkEvent, EyeIkEvent)
from story.cutscenes.anim import Male
from story import actors


class BerlinScene(Scene):
    DUMP_FILE = 'm01_berlin'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        cam_entry = LookAtCamera(root=self, name='cam_entry', fov=35, look_duration=300)
        cam_stand = LookAtCamera(root=self, name='cam_stand', fov=22, look_duration=300)
        cam_adelmar = LookAtCamera(root=self, name='cam_adelmar', fov=20, look_duration=300)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=15, look_duration=300)
        cam_luc = LookAtCamera(root=self, name='cam_luc', fov=20, look_duration=300)

        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True)
        alaric = Character(root=self, actor=actors.Alaric, light_group=0, init_point='Char_alaric', rotate_from_quat=True)
        luc = Character(root=self, actor=actors.Luc, light_group=0, init_point='Char_luc', rotate_from_quat=True)
        adelmar = Character(root=self, actor=actors.Adelmar, light_group=0, init_point='Char_adelmar', rotate_from_quat=True)

        # Entrance; source time 0s.
        t = 0
        cam_entry.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name='cam_entry', target_name='automarker_cam_entry2', duration=4, smooth=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name='automarker_cam_entry_focus', target_name='automarker_cam_entry_focus2', duration=4, smooth=True, time_delay=t)
        adelmar.motion(group=MAIN, anim=Male.Sc_MLHEAD_HAPPY_SMILE_PLEASD_000LV_XA_, duration=1, time_delay=t, time_scale=1)
        adelmar.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_MED_000LV_XA_07, duration=25, time_delay=t, time_scale=1, loop=True)
        luc.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_TWSTS_LOOK_090LV_XA_02, duration=25, time_delay=t, time_scale=1)
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=4, time_delay=t, time_scale=1, loop=True)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=4, time_delay=t, time_scale=1, start_time=1.1, loop=True)
        NeckIkEvent(root=self, group=MAIN, char_name='Char_trent', target_name='Char_adelmar', duration=4, transition_duration=1, target_type='HARDPOINT', target_part='hp_neck', up='NEG_Y_AXIS', front='Z_AXIS', time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name='Char_alaric', target_name='automarker_alaric_stand_ik', duration=15, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', time_delay=t)
        t += 1
        NeckIkEvent(root=self, group=MAIN, char_name='Char_adelmar', target_name='automarker_head_alaric', duration=7, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name='automarker_head_alaric', target_name='automarker_head_alaric2', duration=4, smooth=True, time_delay=t)
        t += 1
        NeckIkEvent(root=self, group=MAIN, char_name='Char_luc', target_name='automarker_head_alaric', duration=9, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', time_delay=t)
        t += 2
        luc.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_TWSTS_FROM_090LV_XA_04, duration=25, time_delay=t, time_scale=1)
        cam_stand.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name='cam_stand', target_name='automarker_cam_stand2', duration=8, smooth=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name='automarker_cam_stand_focus', target_name='automarker_cam_stand_focus2', duration=8, smooth=False, time_delay=t)
        t += 0.01
        MoveEvent(root=self, group=MAIN, object_name='Char_trent', target_name='automarker_trent_pos_table', duration=0.001, smooth=False, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name='Char_alaric', target_name='automarker_alaric_pos_table', duration=0.001, smooth=False, time_delay=t)
        t += 0.01
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=10, time_delay=t, time_scale=1)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=10, time_delay=t, time_scale=1)
        t += 0.98
        MoveEvent(root=self, group=MAIN, object_name='automarker_alaric_stand_ik', target_name='automarker_head_luc', duration=4, smooth=True, time_delay=t)
        main_group.append_time(5.5)

        # Line 10; source time 5.5s.
        t = 0
        t += 0.7
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_GESTL_LEFT_000LV_XA_02, duration=10, time_delay=t, time_scale=1)
        t += 0.8
        NeckIkEvent(root=self, group=MAIN, char_name='Char_trent', target_name='automarker_trents_stand_ik', duration=5, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', time_delay=t)
        t += 1
        NeckIkEvent(root=self, group=MAIN, char_name='Char_adelmar', target_name='Char_alaric', duration=3, transition_duration=1, target_type='HARDPOINT', target_part='hp_neck', up='NEG_Y_AXIS', front='Z_AXIS', time_delay=t)
        t += 2
        EyeIkEvent(root=self, group=MAIN, char_name='Char_trent', target_name='automarker_head_adelmar', duration=5, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, object_name='automarker_trents_stand_ik', target_name='automarker_head_adelmar', duration=1.5, smooth=True, time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, object_name='automarker_alaric_stand_ik', target_name='automarker_head_adelmar', duration=3, smooth=True, time_delay=t)
        alaric.facial(group=MAIN, index=10, auto_lip=True, extra_delay=0)
        # Source facial window: 6s; following pause/overlap: 0.5s.
        main_group.append_time(0.5)

        # Line 20; source time 12s.
        t = 0
        cam_adelmar.set(group=MAIN, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name='Char_adelmar', target_name='automarker_adelmar_ik', duration=5, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, object_name='automarker_adelmar_ik', target_name='automarker_head_trent', duration=2, smooth=True, time_delay=t)
        t += 2
        MoveEvent(root=self, group=MAIN, object_name='automarker_adelmar_ik', target_name='automarker_head_alaric', duration=2, smooth=True, time_delay=t)
        t += 2
        NeckIkEvent(root=self, group=MAIN, char_name='Char_trent', target_name='automarker_trent_table_ik', duration=15, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', time_delay=t)
        t += 0.5
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_TILT_HEAD_QUZZCLLY_000LV_XA_03, duration=2, time_delay=t, time_scale=1)
        adelmar.facial(group=MAIN, index=20, auto_lip=True, extra_delay=0)
        # Source facial window: 5.5s; following pause/overlap: 0.5s.
        main_group.append_time(0.5)

        # Line 30; source time 18s.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name='automarker_trent_table_ik', target_name='automarker_head_luc', duration=4, smooth=True, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name='Char_trent', target_name='automarker_trent_mega_ik', duration=4, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name='automarker_trent_mega_ik', target_name='automarker_table_top', duration=1, smooth=False, time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, object_name='automarker_trent_mega_ik', target_name='automarker_head_luc', duration=1, smooth=False, time_delay=t)
        t += 0.5
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_000LV_E_20, duration=10, time_delay=t, time_scale=1, trans_time=1)
        t += 0.5
        NeckIkEvent(root=self, group=MAIN, char_name='Char_luc', target_name='automarker_luc_ik', duration=10, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', time_delay=t)
        trent.facial(group=MAIN, index=30, auto_lip=True, extra_delay=0)
        main_group.append_time(0.5)
        # Source facial window: 6s; following pause/overlap: 0s.
        # Luc waits for Trent; do not restore the old two-second overlap.

        # Line 40; source time 22s.
        t = 0
        MoveEvent(root=self, group=MAIN, object_name='automarker_luc_ik', target_name='automarker_head_adelmar', duration=4, smooth=True, time_delay=t)
        cam_luc.set(group=MAIN, time_delay=t)
        luc.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_SHRG_SHLDRS_BIG_000LV_XA_03, duration=25, time_delay=t, time_scale=1)
        t += 2.5
        luc.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_STNDCR_TRNS_090LV_XA_05, duration=25, time_delay=t, time_scale=1, trans_time=0.5)
        luc.facial(group=MAIN, index=40, auto_lip=True, extra_delay=0)
        # Source facial window: 6s; following pause/overlap: -0.5s.
        main_group.append_time(2)
