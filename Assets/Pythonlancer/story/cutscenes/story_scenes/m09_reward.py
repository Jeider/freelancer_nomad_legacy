from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import Male, Female

from story import actors


class Msn9RewardCutsceneThorn(Scene):
    SCENE_AMBIENT = [30, 30, 10]
    POINT_ROTATE_OVERRIDES = {
        'kim_talk': (0, 90, 0),
        'trent_talk': (0, 90, 0),
    }

    def action(self):
        main_group = self.get_group(MAIN)

        floor_height = self.get_point('floor_height').position[1]

        # CAMERAS

        cam_dbg = LookAtCamera(root=self, name='cam_dbg', fov=40)
        cam_start = LookAtCamera(root=self, name='cam_start', fov=35)
        cam_hassler = LookAtCamera(root=self, name='cam_hassler', fov=16)
        cam_hassler_answer = LookAtCamera(root=self, name='cam_hassler_answer', fov=16)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=16)

        cam_kim = LookAtCamera(root=self, name='cam_kim', fov=16)
        cam_trent_top = LookAtCamera(root=self, name='cam_trent_top', fov=20)

        # PROPS

        # CHARACTERS

        darcy = Character(root=self, actor=actors.Darcy, light_group=0, init_point='darcy_init', rotate_y=90,
                          floor_height=floor_height)
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='trent_init', rotate_y=90,
                          floor_height=floor_height)
        hassler = Character(root=self, actor=actors.HasslerOrder, light_group=0, init_point='hassler_init', rotate_y=-90,
                            floor_height=floor_height)
        kim = Character(root=self, actor=actors.Kim, light_group=0, init_point='kim_init', rotate_y=90,
                        floor_height=floor_height)

        # MARKERS

        mrk_darcy_talk = darcy.get_stand_marker('darcy_talk')
        mrk_trent_talk = trent.get_stand_marker('trent_talk')
        mrk_hassler_stand = darcy.get_stand_marker('hassler_init')

        mrk_darcy_ik1 = self.get_automarker_name('darcy_ik1')
        mrk_darcy_ik2 = self.get_automarker_name('darcy_ik2')

        hassler.motion(group=MAIN, duration=110, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, time_scale=0.5)
        hassler.motion(group=MAIN, duration=20, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, trans_time=1, time_scale=0.5, time_delay=7)

        hassler.motion(group=MAIN, duration=1, anim=Male.Sc_MLHAND_HNEUT_GESTL_FIST_000LV_00, time_scale=2, time_delay=1)
        hassler.motion(group=MAIN, duration=1, anim=Male.Sc_MLHAND_HNEUT_GESTR_FIST_000LV_00, time_scale=2, time_delay=1)

        # cam_dbg.set(group=MAIN)
        cam_start.set(group=MAIN)

        cam_start.move_cam(group=MAIN, index=2, duration=10, smooth=True)
        cam_start.move_focus(group=MAIN, index=2, duration=10, smooth=True)

        main_group.append_time(8)

        # cam_start.move_cam(group=MAIN, index=2, duration=2, smooth=True)
        # cam_start.move_focus(group=MAIN, index=2, duration=2, smooth=True)
        #
        # main_group.append_time(3)

        trent.motion(group=MAIN, duration=7, loop=True, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01)
        darcy.motion(group=MAIN, duration=7, loop=True, anim=Female.Sc_FMBODY_WLKG_000LV_XA_01, time_scale=0.9)
        kim.motion(group=MAIN, duration=7, loop=True, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01)

        main_group.append_time(7)

        cam_kim.set(group=MAIN)

        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XC_03)
        darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_WALK_STND_TRNS_000LV_XA_01)
        kim.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, start_time=0.9, time_scale=0.6)


        trent.move_head_ik(group=MAIN, target_name=mrk_hassler_stand, immediately=True)

        darcy.move_head_ik(group=MAIN, target_name=mrk_darcy_ik1, immediately=True)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_darcy_ik1, immediately=True)
        darcy.start_head_ik(group=MAIN, time_delay=1, duration=1000, transition_duration=3)
        darcy.start_eye_ik(group=MAIN, time_delay=1, duration=1000, transition_duration=2)

        kim.facial(group=MAIN, index=10)

        main_group.append_time(0.4)

        cam_hassler.set(group=MAIN)

        hassler.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, start_time=0.5, time_scale=0.4)

        hassler.facial(group=MAIN, index=20)

        cam_kim.set(group=MAIN)

        darcy.motion(group=MAIN, duration=1, anim=Female.Sc_FMHAND_HNEUT_GESTL_FIST_000LV_00, time_scale=2)
        darcy.motion(group=MAIN, duration=1, anim=Female.Sc_FMHAND_HNEUT_GESTR_FIST_000LV_00, time_scale=2)
        darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_CROSS_ARMS_000LV_XB_03, time_scale=0.7, time_delay=-1)
        darcy.move_head_ik(group=MAIN, target_name=mrk_darcy_ik2, duration=3)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_darcy_ik2, duration=3)

        kim.facial(group=MAIN, index=30)

        cam_hassler.set(group=MAIN)

        # hassler.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_GESTR_THMBSUP_000LV_XA_02, time_scale=0.4)

        hassler.facial(group=MAIN, index=40)


        # self.set_start_time(main_group.get_time())

        MoveFastEvent(root=self, group=MAIN, object_name=kim.name, target_name=self.get_automarker_name('kim_talk'),
                      adjust_pos=True)
        MoveFastEvent(root=self, group=MAIN, object_name=trent.name, target_name=self.get_automarker_name('trent_talk'),
                      adjust_pos=True)

        trent.motion(group=MAIN, duration=1, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)
        kim.motion(group=MAIN, duration=1, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)
        # hassler.motion(group=MAIN, duration=1, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)

        trent.start_head_ik(group=MAIN,  duration=1000)

        hassler.move_head_ik(group=MAIN, target_name=mrk_trent_talk, immediately=True)
        hassler.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, immediately=True)

        main_group.append_time(0.3)

        cam_trent_top.set(group=MAIN)


        darcy.move_head_ik(group=MAIN, target_name=mrk_hassler_stand, duration=3)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_hassler_stand, duration=2)

        darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_UNCRSS_ARMS_000LV_XB_03, time_scale=0.6,
                     time_delay=2, trans_time=0.25)

        darcy.motion(group=MAIN, duration=3, anim=Female.Sc_FMHAND_NEUT_LEFT_000LV_A_00, time_scale=2, time_delay=2, trans_time=2)
        darcy.motion(group=MAIN, duration=3, anim=Female.Sc_FMHAND_NEUT_RGHT_000LV_A_00, time_scale=2, time_delay=2, trans_time=2)

        trent.motion(group=MAIN, duration=4, anim=Male.Sc_MLBODY_STND_TURN_315LV_XA_02, time_delay=1)
        trent.motion(group=MAIN, duration=4, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01,
                     time_delay=4, time_scale=0.6,  trans_time=0.5)
        trent.motion(group=MAIN, duration=2, anim=Male.Sc_MLHAND_HNEUT_GESTL_FIST_000LV_00, time_scale=1, time_delay=4, trans_time=0.5)
        trent.motion(group=MAIN, duration=2, anim=Male.Sc_MLHAND_HNEUT_GESTR_FIST_000LV_00, time_scale=1, time_delay=4, trans_time=0.5)

        kim.motion(group=MAIN, duration=4, anim=Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01)
        kim.motion(group=MAIN, duration=500, loop=True, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, time_delay=1.07)
        RotateAxisEvent(root=self, group=MAIN, object_name=kim.name, angle=20, duration=1, smooth=True)

        RotateAxisEvent(root=self, group=MAIN, object_name=kim.name, angle=-20, duration=1, smooth=True, time_delay=4)

        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=-10, duration=1, smooth=True, time_delay=1)

        hassler.motion(group=MAIN, duration=8, anim=Male.Sc_MLBODY_STND_1STEP_BKWD_PVOTR_090LV_XA_06)

        main_group.append_time(2)

        trent.facial(group=MAIN, index=100)


        main_group.append_time(1)


        cam_hassler_answer.set(group=MAIN)

        hassler.start_head_ik(group=MAIN, time_delay=-1, duration=1000)
        hassler.start_eye_ik(group=MAIN, time_delay=-1, duration=1000)

        hassler.facial(group=MAIN, index=110)

        cam_trent.set(group=MAIN)


        # MoveFastEvent(root=self, group=MAIN, object_name=kim.name, target_name=OFFSCREEN, adjust_pos=True)

        trent.motion(group=MAIN, duration=4, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01,
                     time_scale=0.6, trans_time=0.5)

        trent.facial(group=MAIN, index=120)

        cam_hassler_answer.set(group=MAIN)


        RotateAxisEvent(root=self, group=MAIN, object_name=kim.name, angle=-45, duration=1, smooth=True, time_delay=-1)
        #
        # hassler.move_head_ik(group=MAIN, target_name=mrk_darcy_talk, duration=2, time_delay=1)
        # hassler.move_eye_ik(group=MAIN, target_name=mrk_darcy_talk, duration=1.5, time_delay=1)
        # hassler.move_head_ik(group=MAIN, target_name=mrk_trent_talk, duration=2, time_delay=4)
        # hassler.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=1.5, time_delay=4)

        hassler.facial(group=MAIN, index=130)

        main_group.append_time(1)






        # main_group.append_time(1000)