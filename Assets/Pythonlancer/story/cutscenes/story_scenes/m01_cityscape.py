from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story import actors


class Propglass_green(Prop):
    COMPOUND_TEMPLATE_NAME = 'glass_green'


class Propli_elite(Prop):
    COMPOUND_TEMPLATE_NAME = 'li_elite'


class Propge_armored(Prop):
    COMPOUND_TEMPLATE_NAME = 'ge_armored'


class CityscapeScene(Scene):
    DUMP_FILE = 'm01_cityscape'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        cam_bar = LookAtCamera(root=self, name='cam_bar', fov=30, look_duration=200)
        cam_start = LookAtCamera(root=self, name='cam_start', fov=25, look_duration=200)
        cam_stuard = LookAtCamera(root=self, name='cam_stuard', fov=20, look_duration=200)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=15, look_duration=200)
        cam_read = LookAtCamera(root=self, name='cam_read', fov=15, look_duration=200)
        cam_walk = LookAtCamera(root=self, name='cam_walk', fov=15, look_duration=200)

        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True)
        stuard = Character(root=self, actor=actors.Stewardess, light_group=0, init_point='Char_stuard', rotate_from_quat=True)

        position_item = Propglass_green(root=self, name='position_item', init_point='position_item', light_group=0, rotate_from_quat=True)
        Wingman1 = Propli_elite(root=self, name='Wingman1', init_point='Wingman1', light_group=0, rotate_from_quat=True)
        Wingman2 = Propli_elite(root=self, name='Wingman2', init_point='Wingman2', light_group=0, rotate_from_quat=True)
        Wingman3 = Propli_elite(root=self, name='Wingman3', init_point='Wingman3', light_group=0, rotate_from_quat=True)
        Prop_armored_transport = Propge_armored(root=self, name='Prop_armored_transport', init_point='Prop_armored_transport', light_group=0, rotate_from_quat=True)


        t = 0
        cam_bar.set(group=MAIN, time_delay=t)
        cam_start.move_cam(group=MAIN, index=2, duration=7, smooth=True, time_delay=t)
        cam_start.move_focus(group=MAIN, index=2, duration=7, smooth=True, time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='Wingman1', target_name=self.get_automarker_name('Wingman1_path'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='Wingman2', target_name=self.get_automarker_name('Wingman2_path'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='Wingman3', target_name=self.get_automarker_name('Wingman3_path'), time_delay=t)
        Wingman1.anim(group=MAIN, anim='Sc_force extend', duration=30, time_delay=t, time_scale=1, start_time=0)
        Wingman2.anim(group=MAIN, anim='Sc_force extend', duration=30, time_delay=t, time_scale=1, start_time=0)
        Wingman3.anim(group=MAIN, anim='Sc_force extend', duration=30, time_delay=t, time_scale=1, start_time=0)
        self._m(stuard, 'Sc_FMBODY_STND_IDLE_MED_000LV_xa_05', t, 12)
        t += 7
        cam_start.move_cam(group=MAIN, index=3, duration=5, smooth=True, time_delay=t)
        cam_start.move_focus(group=MAIN, index=3, duration=5, smooth=True, time_delay=t)
        t += 5
        MoveFastEvent(root=self, group=MAIN, object_name='Char_trent', target_name=self.get_automarker_name('trent_init_pos'), time_delay=t)
        cam_stuard.set(group=MAIN, time_delay=t)
        cam_stuard.move_cam(group=MAIN, index=2, duration=6, smooth=True, time_delay=t)
        cam_stuard.move_focus(group=MAIN, index=2, duration=6, smooth=True, time_delay=t)
        self._m(stuard, 'Sc_FMBODY_STND_WAVE_LHND_000LV_XA_03', t, 15)
        EyeIkEvent(root=self, group=MAIN, char_name='Char_stuard', target_name='stuard_look_at_eyes', duration=19, time_delay=t, target_type=TARGET_ROOT)
        self._m(trent, 'Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02', t, 15, scale=0.5)
        t += 0.999
        NeckIkEvent(root=self, group=MAIN, char_name='Char_stuard', target_name='stuard_look_at_head', duration=19, time_delay=t, target_type=TARGET_ROOT)
        main_group.append_time(15)

        t = 0
        self._m(stuard, 'Sc_dx_s028x_0702_sinclair', t, 4)
        self._m(stuard, 'Sc_FMBODY_STND_IDLE_MED_000LV_xa_05', t, 15, trans=1)
        NeckIkEvent(root=self, group=MAIN, char_name='Char_stuard', target_name='Char_trent', duration=5, time_delay=t, target_type=TARGET_HARDPOINT, target_part='hp_neck')
        NeckIkEvent(root=self, group=MAIN, char_name='Char_trent', target_name='Char_stuard', duration=5, time_delay=t, target_type=TARGET_HARDPOINT, target_part='hp_neck')
        t += 1.5
        self._m(trent, 'Sc_MLBODY_STND_GIVE_VEND_000LV_B_07', t, 5, trans=0.25)
        t += 0.5
        self._m(stuard, 'Sc_FMBODY_STND_IDLE_SMALL_000LV_xa_05', t, 15, trans=1)
        t += 0.2
        self._m(stuard, 'Sc_FMHEAD_BASEPOSE_000LV_02_01', t, 4, trans=0.5)
        t += 0.301
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_0010', time_delay=t)
        t += 0.499
        MoveFastEvent(root=self, group=MAIN, object_name='stuard_look_at_head', target_name=self.get_automarker_name('marker_trent_head_middle'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='stuard_look_at_eyes', target_name=self.get_automarker_name('marker_docs'), time_delay=t)
        t += 1
        cam_read.set(group=MAIN, time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='stuard_look_at_head', target_name=self.get_automarker_name('marker_trent_head_middle_left'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='stuard_look_at_eyes', target_name=self.get_automarker_name('marker_docs_left'), time_delay=t)
        t += 0.8
        self._m(stuard, 'Sc_FMHEAD_MOTION_MOUTH_CLENCH_000LV_%', t, 2, trans=0.4)
        t += 0.5
        MoveFastEvent(root=self, group=MAIN, object_name='stuard_look_at_eyes', target_name=self.get_automarker_name('marker_docs_right'), time_delay=t)
        t += 0.2
        MoveFastEvent(root=self, group=MAIN, object_name='stuard_look_at_head', target_name=self.get_automarker_name('marker_trent_head_middle_right'), time_delay=t)
        stuard.facial(group=MAIN, index=10, auto_lip=True)

        t = 0
        self._m(stuard, 'Sc_dx_s037a_1301_sinclair', t, 4)
        t += 1
        MoveFastEvent(root=self, group=MAIN, object_name='stuard_look_at_head', target_name=self.get_automarker_name('marker_trent_head_top'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='stuard_look_at_eyes', target_name=self.get_automarker_name('marker_trent_head_top'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name='stuard_look_at_eyes', target_name=self.get_automarker_name('marker_trent_head_top'), time_delay=t)
        self._m(trent, 'Sc_MLBODY_STND_IDLE_000LV_xa_04', t, 1, trans=0.2)
        t += 0.3
        self._m(stuard, 'Sc_dx_s037a_1301_sinclair', t, 4, scale=0.25, trans=0.25)
        t += 0.7
        MoveFastEvent(root=self, group=MAIN, object_name='stuard_look_at_eyes', target_name=self.get_automarker_name('marker_trent_head_top_left'), time_delay=t)
        self._m(trent, 'Sc_MLBODY_STND_SHAKHEAD_NO_SLGHTLY_000LV_XA_02', t, 3, scale=0.5, trans=0.5)
        t += 1
        cam_trent.set(group=MAIN, time_delay=t)
        self._m(trent, 'Sc_MLHEAD_MOTION_EYES_SQUINTSML_TRENT_000LV_XB_%', t, 4, trans=0.2)
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_0020', time_delay=t)
        stuard.facial(group=MAIN, index=20, auto_lip=True)

        t = 0
        self._m(trent, 'Sc_dx_s045d_0401_trent', t, 4, trans=0.2)
        t += 1
        self._m(trent, 'Sc_MLBODY_STND_GIVE_VEND_000LV_B_07', t, 4, start=3, trans=1)
        t += 4
        self._m(trent, 'Sc_MLBODY_STND_WALK_TRNS_090LV_XA_02', t, 15, scale=0.6, trans=0.2)
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_0030', time_delay=t)
        t += 1.999
        cam_walk.set(group=MAIN, time_delay=t)
        t += 0.4
        self._m(trent, 'Sc_MLBODY_WLKG_000LV_XA_01', t, 15, scale=0.6, trans=0.5)
        t += 0.6
        cam_walk.move_cam(group=MAIN, index=2, duration=6, smooth=True, time_delay=t)
        cam_walk.move_focus(group=MAIN, index=2, duration=6, smooth=True, time_delay=t)
        trent.facial(group=MAIN, index=30, auto_lip=True)

        t = 0
        self._m(trent, 'Sc_dx_s045d_0401_trent', t, 4, trans=0.2)
        t += 1.5
        self._m(stuard, 'Sc_FMBODY_STND_WALK_TRNS_180LV_XA_02', t, 15, trans=0.5)
        t += 0.5
        self._m(trent, 'Sc_dx_s050c_0101_trent', t, 4, trans=0.2)
        t += 0.501
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_0040a', time_delay=t)
        t += 1.199
        self._m(stuard, 'Sc_FMBODY_WLKG_000LV_XA_01', t, 15, trans=0.5)
        t += 1.1
        self._m(trent, 'Sc_dx_s003x_0101_trent', t, 4, trans=0.2)
        t += 1.702
        MoveOffscreenEvent(root=self, group=MAIN, object_name='subtitles_0040b', time_delay=t)
        t += 2.998
        MoveOffscreenEvent(root=self, group=MAIN, object_name='trent', time_delay=t)
        cam_bar.set(group=MAIN, time_delay=t)
        cam_bar.move_cam(group=MAIN, index=2, duration=12, smooth=True, time_delay=t)
        cam_bar.move_focus(group=MAIN, index=2, duration=12, smooth=True, time_delay=t)
        t += 1
        MoveFastEvent(root=self, group=MAIN, object_name='Prop_armored_transport', target_name=self.get_automarker_name('armored_pos2'), time_delay=t)
        t += 6.25
        t += 0.75
        MoveFastEvent(root=self, group=MAIN, object_name='Prop_armored_transport', target_name=self.get_automarker_name('armored_pos3'), time_delay=t)
        trent.facial(group=MAIN, index=40, auto_lip=True)

        main_group.append_time(2)

    def _m(self, char, anim, delay, duration, scale=1, start=0, trans=None):
        char.motion(group=MAIN, anim=anim, duration=duration, time_delay=delay,
                    time_scale=scale, start_time=start, trans_time=trans)

