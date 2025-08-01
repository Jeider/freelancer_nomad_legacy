from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import Male, Female

from story import actors


class Msn9RescuedCutsceneThorn(Scene):
    POINT_ROTATE_OVERRIDES = {
        'hassler_arrive': (0, -60, 0),
        # 'trent_talk': (0, 90, 0),
    }

    def action(self):
        main_group = self.get_group(MAIN)

        floor_height = self.get_point('floor_height').position[1]

        # CAMERAS

        cam_dbg = LookAtCamera(root=self, name='cam_dbg', fov=40)
        cam_start = LookAtCamera(root=self, name='cam_start', fov=35)

        cam_alaric = LookAtCamera(root=self, name='cam_alaric', fov=18)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=16)
        cam_trent_top = LookAtCamera(root=self, name='cam_trent_top', fov=20)
        cam_trent_bottom = LookAtCamera(root=self, name='cam_trent_bottom', fov=20)
        cam_edison = LookAtCamera(root=self, name='cam_edison', fov=16)
        cam_hassler_arrive = LookAtCamera(root=self, name='cam_hassler_arrive', fov=25)
        cam_hassler = LookAtCamera(root=self, name='cam_hassler', fov=18)

        # cam_hassler_answer = LookAtCamera(root=self, name='cam_hassler_answer', fov=16)

        # cam_kim = LookAtCamera(root=self, name='cam_kim', fov=16)
        # cam_trent_top = LookAtCamera(root=self, name='cam_trent_top', fov=20)

        # PROPS

        # CHARACTERS

        darcy = Character(root=self, actor=actors.Darcy, light_group=0, init_point='darcy_init', rotate_y=0,
                          floor_height=floor_height)
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='trent_init', rotate_y=0,
                          floor_height=floor_height)
        alaric = Character(root=self, actor=actors.Alaric, light_group=0, init_point='alaric_init', rotate_y=135,
                           floor_height=floor_height)
        hassler = Character(root=self, actor=actors.HasslerOrder, light_group=0, init_point='hassler_init', rotate_y=-90,
                            floor_height=floor_height)
        edison = Character(root=self, actor=actors.EdisonTrent, light_group=0, init_point='edison_init', rotate_y=0,
                           floor_height=floor_height)
        # medic = Character(root=self, actor=actors.OrderMedic, light_group=0, init_point='medic_init', rotate_y=180,
        #                   floor_height=floor_height)

        # MARKERS

        mrk_darcy_talk = darcy.get_stand_marker('darcy_talk', floor_height=floor_height)
        mrk_trent_talk = trent.get_stand_marker('trent_talk', floor_height=floor_height)
        mrk_alaric = darcy.get_stand_marker('alaric_init', floor_height=floor_height)
        mrk_edison = darcy.get_stand_marker('edison_reveal', floor_height=floor_height)
        mrk_hassler_talk = darcy.get_stand_marker('hassler_talk', floor_height=floor_height)

        mrk_trent_front = self.get_automarker_name('trent_front')
        mrk_alaric_front = self.get_automarker_name('alaric_front')
        mrk_edison_front = self.get_automarker_name('edison_front')
        mrk_hassler_front = self.get_automarker_name('hassler_front')
        mrk_hassler_front2 = self.get_automarker_name('hassler_front2')
        mrk_darcy_front = self.get_automarker_name('darcy_front')

        # EXTRA DEFINITIONS

        alaric.move_head_ik(group=BG, target_name=mrk_trent_front, immediately=True)
        alaric.move_eye_ik(group=BG, target_name=mrk_trent_talk, immediately=True)

        darcy.move_head_ik(group=BG, target_name=mrk_alaric_front, immediately=True)
        darcy.move_eye_ik(group=BG, target_name=mrk_alaric, immediately=True)
        trent.move_head_ik(group=BG, target_name=mrk_alaric_front, immediately=True)
        trent.move_eye_ik(group=BG, target_name=mrk_alaric, immediately=True)
        edison.move_head_ik(group=BG, target_name=mrk_trent_front, immediately=True)
        edison.move_eye_ik(group=BG, target_name=mrk_trent_talk, immediately=True)

        hassler.move_head_ik(group=BG, target_name=mrk_edison_front, immediately=True)
        hassler.move_eye_ik(group=BG, target_name=mrk_edison, immediately=True)

        # ACTION!

        trent.motion(group=MAIN, duration=12, loop=True, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01)
        darcy.motion(group=MAIN, duration=12, loop=True, anim=Female.Sc_FMBODY_WLKG_000LV_XA_01, time_scale=0.9)
        alaric.motion(group=MAIN, duration=12, loop=True, anim=Male.Sc_MLBODY_STND_HOLD_ARMS_CROSSED_000LV_XA_02)
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=-5, duration=8, smooth=False)

        # edison.motion(group=MAIN, duration=12, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)
        #
        # trent.start_head_ik(group=MAIN, duration=100, transition_duration=2, time_delay=3)
        # darcy.start_head_ik(group=MAIN, duration=100, transition_duration=2, time_delay=3)
        # alaric.start_head_ik(group=MAIN, duration=100, transition_duration=2, time_delay=8)

        cam_start.set(group=MAIN)

        cam_start.move_cam(group=MAIN, index=2, duration=12, smooth=True)
        cam_start.move_focus(group=MAIN, index=2, duration=12, smooth=True)
        #
        # cam_start.move_cam(group=MAIN, index=2, duration=2, smooth=True)
        # cam_start.move_focus(group=MAIN, index=2, duration=2, smooth=True)

        # main_group.append_time(100)
        main_group.append_time(12)


        # return
        # self.set_start_time(main_group.get_time())


        # INITS ENDS

        trent.start_head_ik(group=BG, duration=1000)
        trent.start_eye_ik(group=BG, duration=1000)
        darcy.start_head_ik(group=BG, duration=1000, transition_duration=2)
        darcy.start_eye_ik(group=BG, duration=1000, transition_duration=2)
        alaric.start_head_ik(group=BG, duration=1000)
        alaric.start_eye_ik(group=BG, duration=1000)


        MoveFastEvent(root=self, group=MAIN, object_name=darcy.name, target_name=self.get_automarker_name('darcy_talk'),
                      adjust_pos=True)
        MoveFastEvent(root=self, group=MAIN, object_name=trent.name, target_name=self.get_automarker_name('trent_talk'),
                      adjust_pos=True)
        trent.motion(group=MAIN, duration=12, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)
        darcy.motion(group=MAIN, duration=12, loop=True, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05)



        # main_group.append_time(0.1)


        alaric.motion(group=MAIN, duration=12, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, time_scale=0.6)
        alaric.motion(group=MAIN, duration=12, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, time_scale=0.6, time_delay=4, trans_time=1)

        cam_alaric.set(group=MAIN)

        alaric.facial(group=MAIN, index=10)


        cam_trent.set(group=MAIN)

        trent.motion(group=MAIN, duration=12, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, time_scale=0.4, time_delay=2, trans_time=0.3)
        trent.facial(group=MAIN, index=20)


        cam_alaric.set(group=MAIN)

        cam_alaric.move_cam(group=MAIN, index=2, duration=5, smooth=True, time_delay=3)
        cam_alaric.move_focus(group=MAIN, index=2, duration=5, smooth=True, time_delay=3)


        alaric.motion(group=MAIN, duration=12, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, time_scale=0.6)
        alaric.motion(group=MAIN, duration=8, anim=Male.Sc_MLBODY_STND_1STEP_BKWD_PVOTL_270LV_XA_06, time_scale=0.3, time_delay=3)
        edison.motion(group=MAIN, duration=12, anim=Male.Sc_MLBODY_STND_TURN_180LV_XA_04, time_scale=1, time_delay=5)
        edison.motion(group=MAIN, duration=12, anim=Male.Sc_MLBODY_STND_SHAK_RHAND_000LV_XA_03, time_scale=0.4, time_delay=9, trans_time=1)


        alaric.move_head_ik(group=MAIN, target_name=mrk_edison_front, duration=3, time_delay=4)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_edison, duration=2, time_delay=4)

        MoveFastEvent(root=self, group=MAIN, object_name=edison.name, target_name=self.get_automarker_name('edison_reveal'),
                      adjust_pos=True)
        edison.motion(group=MAIN, duration=12, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)

        edison_ik1 = edison.start_head_ik(group=MAIN, duration=100, time_delay=7)
        edison_ik2 = edison.start_eye_ik(group=MAIN, duration=100, time_delay=7)
        edison_ik_time = main_group.get_time() + 7

        alaric.facial(group=MAIN, index=30)



        cam_trent_top.set(group=MAIN)

        darcy.move_head_ik(group=MAIN, target_name=mrk_edison_front, immediately=True)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_edison, immediately=True)

        trent.move_head_ik(group=MAIN, target_name=mrk_edison_front, immediately=True)
        trent.move_eye_ik(group=MAIN, target_name=mrk_edison, immediately=True)

        darcy.motion(group=MAIN, duration=12, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, time_scale=0.5, time_delay=2)
        darcy.motion(group=MAIN, duration=12, anim=Female.Sc_FMHEAD_SURPRSE_QUZZCLLY_000LV_XA_, time_scale=1, time_delay=1, trans_time=0.25)
        trent.motion(group=MAIN, duration=12, anim=Male.Sc_MLBODY_STND_SHAK_RHAND_000LV_XA_03, time_scale=0.6)
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=-15, duration=2, smooth=False)

        alaric.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=3, time_delay=3)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=2, time_delay=2)

        trent.facial(group=MAIN, index=40)

        cam_edison.set(group=MAIN)

        edison.motion(group=MAIN, duration=12, anim=Male.Sc_MLBODY_STND_GESTR_SELF_000LV_XA_02, time_scale=1, time_delay=3)

        edison.facial(group=MAIN, index=50)

        cam_trent.set(group=MAIN)

        trent.motion(group=MAIN, duration=12, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, time_scale=0.8)

        trent.facial(group=MAIN, index=60)
        main_group.append_time(0.5)

        cam_edison.set(group=MAIN)

        edison.motion(group=MAIN, duration=12, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, time_scale=0.8)
        edison.facial(group=MAIN, index=70)

        main_group.append_time(0.5)













        #
        #
        # # DBG
        # MoveFastEvent(root=self, group=MAIN, object_name=edison.name, target_name=self.get_automarker_name('edison_reveal'),
        #               adjust_pos=True)
        # edison.motion(group=MAIN, duration=12, anim=Male.Sc_MLBODY_STND_TURN_180LV_XA_04, time_scale=1)
        #
        #
        # main_group.append_time(2)
        # # DBG


        MoveFastEvent(root=self, group=MAIN, object_name=hassler.name, target_name=self.get_automarker_name('hassler_arrive'),
                      adjust_pos=True)

        hassler.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, start_time=0.5, time_scale=1)
        cam_hassler_arrive.set(group=MAIN)

        darcy.motion(group=MAIN, duration=12, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, time_scale=0.5)
        trent.motion(group=MAIN, duration=12, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, time_scale=0.5, time_delay=2)

        alaric.move_head_ik(group=MAIN, target_name=mrk_hassler_front, duration=3, time_delay=1)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_hassler_talk, duration=2, time_delay=1)

        darcy.move_head_ik(group=MAIN, target_name=mrk_hassler_front, duration=3, time_delay=0.5)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_hassler_talk, duration=2, time_delay=0.5)


        trent.move_head_ik(group=MAIN, target_name=mrk_hassler_front2, duration=3)
        trent.move_eye_ik(group=MAIN, target_name=mrk_hassler_talk, duration=2)

        edison.move_head_ik(group=MAIN, target_name=mrk_hassler_front, duration=3, time_delay=0.9)
        edison.move_eye_ik(group=MAIN, target_name=mrk_hassler_talk, duration=2, time_delay=1)



        hassler.start_head_ik(group=MAIN, duration=1000, time_delay=1)
        hassler.start_eye_ik(group=MAIN, duration=1000, time_delay=1)

        main_group.append_time(1)


        hassler.facial(group=MAIN, index=80)


        cam_edison.set(group=MAIN)


        edison.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=2.5, time_delay=2)
        edison.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=1.5, time_delay=2)

        edison.motion(group=MAIN, duration=12, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, time_scale=0.8, time_delay=1)

        edison.facial(group=MAIN, index=90)

        ik_end_time = main_group.get_time() - edison_ik_time
        edison_ik1.set_duration(ik_end_time)
        edison_ik2.set_duration(ik_end_time)

        main_group.append_time(0.2)

        edison.motion(group=MAIN, duration=12, anim=Male.Sc_MLBODY_STND_WALK_TRNS_270LV_XA_02, time_scale=0.8, trans_time=0.25)


        main_group.append_time(2)

        cam_hassler_arrive.set(group=MAIN)



        #
        # cam_hassler_arrive.set(group=MAIN)
        #
        # MoveFastEvent(root=self, group=MAIN, object_name=hassler.name, target_name=self.get_automarker_name('hassler_arrive'),
        #               adjust_pos=True)
        #
        # hassler.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, start_time=0.5, time_scale=1)
        #
        #
        # hassler.start_head_ik(group=MAIN, duration=1000, time_delay=1, transition_duration=1)
        # hassler.start_eye_ik(group=MAIN, duration=1000, time_delay=1, transition_duration=1)
        #
        # main_group.append_time(2)

        cam_hassler.set(group=MAIN)


        hassler.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_TURN_315LV_XA_02, time_scale=1)

        hassler.move_head_ik(group=MAIN, target_name=mrk_trent_talk, duration=2, time_delay=-1)
        hassler.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=2, time_delay=-1)

        main_group.append_time(1)

        hassler.facial(group=MAIN, index=100)



        #
        # # DBG
        # darcy.move_head_ik(group=MAIN, target_name=mrk_hassler_front2, duration=1)
        # darcy.move_eye_ik(group=MAIN, target_name=mrk_hassler_talk, duration=1)
        # trent.move_head_ik(group=MAIN, target_name=mrk_hassler_front2, duration=1)
        # trent.move_eye_ik(group=MAIN, target_name=mrk_hassler_talk, duration=1)
        # # DBG

        # main_group.append_time(1)

        darcy.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=2.5)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=2)


        cam_trent_bottom.set(group=MAIN)

        cam_trent_bottom.move_cam(group=MAIN, index=2, duration=12, smooth=True)
        cam_trent_bottom.move_focus(group=MAIN, index=2, duration=12, smooth=True)

        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_TURN_045LV_XA_04, time_scale=1)

        trent.facial(group=MAIN, index=110)

        trent.move_head_ik(group=MAIN, target_name=mrk_darcy_front, duration=2.5)
        trent.move_eye_ik(group=MAIN, target_name=mrk_darcy_talk, duration=2)
        darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_CROSS_ARMS_000LV_XB_03, time_scale=0.7, trans_time=0.5)
        darcy.motion(group=MAIN, duration=2, anim=Female.Sc_FMHAND_HNEUT_GESTL_FIST_000LV_00, time_scale=1)
        darcy.motion(group=MAIN, duration=2, anim=Female.Sc_FMHAND_HNEUT_GESTR_FIST_000LV_00, time_scale=1)

        darcy.facial(group=MAIN, index=120)

        trent.move_head_ik(group=MAIN, target_name=mrk_hassler_front2, duration=2.5)
        trent.move_eye_ik(group=MAIN, target_name=mrk_hassler_talk, duration=2)

        darcy.move_head_ik(group=MAIN, target_name=mrk_hassler_front2, duration=2.5, time_delay=0.5)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_hassler_talk, duration=2, time_delay=0.5)


        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, time_scale=0.6, trans_time=0.5)

        trent.facial(group=MAIN, index=130)

        main_group.append_time(1)

        cam_hassler.set(group=MAIN)

        hassler.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, time_scale=0.6, trans_time=0.5, time_delay=2)
        hassler.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, time_scale=0.6, trans_time=0.5, time_delay=7)

        hassler.facial(group=MAIN, index=140)

        cam_trent_bottom.set(group=MAIN)

        darcy.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=2.5)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=2)

        trent.facial(group=MAIN, index=150)

        cam_hassler.set(group=MAIN)

        hassler.facial(group=MAIN, index=160)

        cam_trent_bottom.set(group=MAIN)

        darcy.move_head_ik(group=MAIN, target_name=mrk_hassler_front2, duration=2.5, time_delay=0.5)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_hassler_talk, duration=2, time_delay=0.5)

        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, time_scale=0.6, trans_time=0.5)
        darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_UNCRSS_ARMS_000LV_XA_03, time_scale=0.7, trans_time=0.5)

        trent.facial(group=MAIN, index=170)

        main_group.append_time(1)






        # main_group.append_time(1000)