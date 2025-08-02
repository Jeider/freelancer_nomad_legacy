from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import Male, Female

from story import actors


class Msn9YokoDeckScene(Scene):
    POINT_ROTATE_OVERRIDES = {
        'hassler_arrive': (0, -60, 0),
    }

    def action(self):
        main_group = self.get_group(MAIN)


        # CAMERAS

        cam_dbg = LookAtCamera(root=self, name='cam_dbg', fov=40)
        cam_start = LookAtCamera(root=self, name='cam_start', fov=20)
        #
        cam_darcy = LookAtCamera(root=self, name='cam_darcy', fov=14)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=16)
        # cam_trent_top = LookAtCamera(root=self, name='cam_trent_top', fov=20)
        # cam_trent_bottom = LookAtCamera(root=self, name='cam_trent_bottom', fov=20)
        # cam_edison = LookAtCamera(root=self, name='cam_edison', fov=16)
        # cam_hassler_arrive = LookAtCamera(root=self, name='cam_hassler_arrive', fov=25)
        # cam_hassler = LookAtCamera(root=self, name='cam_hassler', fov=18)

        # PROPS

        # CHARACTERS

        darcy = Character(root=self, actor=actors.Darcy, light_group=0, init_point='darcy_init', rotate_y=220,
                          floor_height=0)
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='trent_init', rotate_y=40,
                          floor_height=0)

        # MARKERS

        mrk_darcy = darcy.get_stand_marker('darcy_init', floor_height=0)
        mrk_trent_talk = trent.get_stand_marker('trent_talk', floor_height=0)

        mrk_darcy_walkout = self.get_automarker_name('darcy_walkout')

        # EXTRA DEFINITIONS

        # alaric.move_head_ik(group=BG, target_name=mrk_trent_front, immediately=True)
        # alaric.move_eye_ik(group=BG, target_name=mrk_trent_talk, immediately=True)
        #
        darcy.move_head_ik(group=BG, target_name=mrk_trent_talk, immediately=True)
        # darcy.move_eye_ik(group=BG, target_name=mrk_alaric, immediately=True)
        trent.move_head_ik(group=BG, target_name=mrk_darcy, immediately=True)
        # trent.move_eye_ik(group=BG, target_name=mrk_alaric, immediately=True)
        # edison.move_head_ik(group=BG, target_name=mrk_trent_front, immediately=True)
        # edison.move_eye_ik(group=BG, target_name=mrk_trent_talk, immediately=True)
        #
        # hassler.move_head_ik(group=BG, target_name=mrk_edison_front, immediately=True)
        # hassler.move_eye_ik(group=BG, target_name=mrk_edison, immediately=True)

        # ACTION!


        cam_start.set(group=MAIN)

        cam_start.move_cam(group=MAIN, index=2, duration=4, smooth=True)
        cam_start.move_focus(group=MAIN, index=2, duration=4, smooth=True)

        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, start_time=0, time_scale=0.9)
        trent.start_head_ik(group=BG, duration=1000)
        darcy_ik = darcy.start_head_ik(group=BG, duration=1000)

        darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_UNCRSS_ARMS_000LV_XA_03, time_scale=0.7)
        darcy.motion(group=MAIN, duration=1, anim=Female.Sc_FMHAND_HNEUT_GESTL_FIST_000LV_00, time_scale=4)
        darcy.motion(group=MAIN, duration=1, anim=Female.Sc_FMHAND_HNEUT_GESTR_FIST_000LV_00, time_scale=4)
        darcy.motion(group=MAIN, duration=2, anim=Female.Sc_FMHAND_NEUT_LEFT_000LV_A_00, time_scale=1, trans_time=1, time_delay=2)
        darcy.motion(group=MAIN, duration=2, anim=Female.Sc_FMHAND_NEUT_RGHT_000LV_A_00, time_scale=1, trans_time=1,time_delay=2)

        main_group.append_time(2)

        darcy.facial(group=MAIN, index=10)

        cam_trent.set(group=MAIN)

        trent.facial(group=MAIN, index=20)

        cam_darcy.set(group=MAIN)

        darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, time_scale=0.7)
        darcy.facial(group=MAIN, index=30)

        cam_trent.set(group=MAIN)

        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, start_time=0, time_scale=0.7)
        trent.facial(group=MAIN, index=40)

        cam_darcy.set(group=MAIN)

        darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, time_scale=0.5)
        darcy.facial(group=MAIN, index=50)

        darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_WALK_TRNS_270LV_XA_02, time_scale=1, time_delay=-2, trans_time=0.5)
        darcy_ik.set_duration(main_group.get_time() - 2)
        RotateAxisEvent(root=self, group=MAIN, object_name=darcy.name, angle=35, duration=2, smooth=False, time_delay=-2)

        cam_trent.set(group=MAIN)

        trent.move_head_ik(group=MAIN, target_name=mrk_darcy_walkout, duration=4)
        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, start_time=0, time_scale=0.7)
        trent.facial(group=MAIN, index=60)

        main_group.append_time(1)