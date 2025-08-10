from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import Male, Female

from story import actors


class Cigarette(Prop):
    COMPOUND_TEMPLATE_NAME = 'cigarette_2'


class Ashtray(Prop):
    COMPOUND_TEMPLATE_NAME = 'ashtray_2'


class BottleWine2(Prop):
    COMPOUND_TEMPLATE_NAME = 'bottle_wine_1'


class Msn11AmbushScene(Scene):
    POINT_ROTATE_OVERRIDES = {
        'trent_near_table': (0, 220, 0),
        'bottle_wine_1': (90, 0, 0),
        'glass1': (90, 0, 0),
        'glass2': (90, 0, 0),
        'trent_talk': (0, -135, 0),
    }

    def action(self):
        main_group = self.get_group(MAIN)

        # CAMERAS

        cam_dbg = LookAtCamera(root=self, name='cam_dbg', fov=30)
        cam_start = LookAtCamera(root=self, name='cam_start', fov=21)
        cam_trent_stand = LookAtCamera(root=self, name='cam_trent_stand', fov=18)
        cam_trent_sitting = LookAtCamera(root=self, name='cam_trent_sitting', fov=18)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=18)
        cam_trent_damn = LookAtCamera(root=self, name='cam_trent_damn', fov=19)
        cam_trent_pda = LookAtCamera(root=self, name='cam_trent_pda', fov=22)

        cam_rockford_first = LookAtCamera(root=self, name='cam_rockford_first', fov=20)
        cam_rockford = LookAtCamera(root=self, name='cam_rockford', fov=18)
        cam_rockford_walkout = LookAtCamera(root=self, name='cam_rockford_walkout', fov=22)

        # PROPS

        cig = Cigarette(root=self, name='rock_cig', init_point='mrk_offscreen', light_group=0)
        Ashtray(root=self, name='rock_ash', init_point='ashtray_2', light_group=0)
        Glass(root=self, name='glass1', init_point='glass1', light_group=0)
        Glass(root=self, name='glass2', init_point='glass2', light_group=0)
        BottleWine2(root=self, name='bottle_wine_1', init_point='bottle_wine_1', light_group=0)

        lt_room1 = Light(root=self, name='ROOMA', point_name='light1', light_group=0, diffuse=[0.8, 0.7, 0.3],
                         ambient=[0, 0, 0], direction=[0, 0, -1], light_type=L_POINT, range=15)

        lt_room2 = Light(root=self, name='ROOMV', point_name='light2', light_group=0, diffuse=[0.3, 0.0, 0.0],
                         ambient=[0, 0, 0], direction=[0, 0, -1], light_type=L_POINT, range=15)

        lt_room3 = Light(root=self, name='ROOMX', point_name='light3', light_group=0, diffuse=[0.6, 0.5, 0.2],
                         ambient=[0, 0, 0], direction=[0, 0, -1], light_type=L_POINT, range=15, on=False)

        # CHARACTERS

        rockford = Character(root=self, actor=actors.Rockford, light_group=0, init_point='rockford_talk', rotate_y=45)
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='trent_init', rotate_y=-90)
        kim = Character(root=self, actor=actors.Kim, light_group=0, init_point='kim_init', rotate_y=0)

        cig_conn = ConnectHardpointEvent(root=self, group=BG, target_name=cig.name, parent_name=rockford.name,
                                         duration=1000, target_hardpoint="hprightconnect_cigarette2",
                                         parent_hardpoint="hprightconnect")



        # MARKERS

        mrk_trent_init = trent.get_stand_marker('trent_init')
        mrk_trent_talk = trent.get_sit_marker('trent_talk')
        mrk_rockford_talk = rockford.get_sit_marker('rockford_talk')
        # mrk_edison_talk = edison.get_sit_marker('edison_talk')
        # mrk_junko_talk = junko.get_sit_marker('junko_talk')
        #
        mrk_trent_walk = self.get_automarker_name('mrk_trent_walk')
        mrk_trent_arrive = self.get_automarker_name('mrk_trent_arrive')
        mrk_rockford_top = self.get_automarker_name('mrk_rockford_top')
        mrk_trent_sitdown = self.get_automarker_name('mrk_trent_sitdown')
        mrk_rockford_smoking = self.get_automarker_name('mrk_rockford_smoking')
        mrk_rockford_smoking2 = self.get_automarker_name('mrk_rockford_smoking2')
        mrk_rockford_smoke_eye = self.get_automarker_name('mrk_rockford_smoke_eye')
        mrk_rockford_smoke_head = self.get_automarker_name('mrk_rockford_smoke_head')
        mrk_rockford_stand_look = self.get_automarker_name('mrk_rockford_stand_look')
        mrk_trent_talk_top = self.get_automarker_name('mrk_trent_talk_top')
        mrk_rockford_walking = self.get_automarker_name('mrk_rockford_walking')
        # mrk_trent_look_side = self.get_automarker_name('trent_look_side')
        # mrk_edison_front = self.get_automarker_name('edison_front')
        # mrk_junko_front = self.get_automarker_name('junko_front')
        # mrk_edison_look_out = self.get_automarker_name('edison_look_out')

        # ACTION!

        rockford.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, time_scale=1)
        rockford.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_GRABR_CHIN_RLEASE_000LV_XA_02, time_scale=0.7, time_delay=1)

        first_chin_ik1 = IkEvent(root=self, group=MAIN, char_name=rockford.name, target_name=mrk_rockford_smoking, duration=7,
                                 end_effector="RLowArm", up=Y_AXIS, front=Z_AXIS, time_delay=2, transition_duration=1)
        first_chin_ik2 = IkEvent(root=self, group=MAIN, char_name=rockford.name, target_name=mrk_rockford_smoking2, duration=7,
                                 end_effector="RHand", up=X_AXIS, front=Z_AXIS, time_delay=2, transition_duration=1)

        trent.move_head_ik(group=MAIN, target_name=mrk_trent_walk, immediately=True)
        trent.move_eye_ik(group=MAIN, target_name=mrk_trent_walk, immediately=True)
        rockford.move_head_ik(group=MAIN, target_name=mrk_trent_arrive, immediately=True)
        rockford.move_eye_ik(group=MAIN, target_name=mrk_trent_arrive, immediately=True)

        trent_head_ik = trent.start_head_ik(group=MAIN, duration=1000)
        trent_eye_ik = trent.start_eye_ik(group=MAIN, duration=1000)


        trent.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, time_scale=1, time_delay=4)
        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, time_scale=1, time_delay=6.6)

        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=45, duration=2.5, smooth=True, time_delay=6)

        trent.move_head_ik(group=MAIN, target_name=mrk_rockford_top, duration=2.5, time_delay=6)
        trent.move_eye_ik(group=MAIN, target_name=mrk_rockford_talk, duration=1.5, time_delay=6)

        cam_start.set(group=MAIN)

        cam_start.move_cam(group=MAIN, index=2, duration=7, smooth=True)
        cam_start.move_focus(group=MAIN, index=2, duration=7, smooth=True)

        main_group.append_time(7)

        cam_trent_stand.set(group=MAIN)

        main_group.append_time(1)

        trent.facial(group=MAIN, index=10)

        main_group.append_time(0.25)



        cam_rockford_first.set(group=MAIN)

        # trent_head_ik.set_duration(duration=main_group.get_time())
        # trent_eye_ik.set_duration(duration=main_group.get_time())
        trent.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, time_scale=1)

        first_chin_ik1.set_duration(main_group.get_time()-1.5)
        first_chin_ik2.set_duration(main_group.get_time()-1.5)

        rockford.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_HOLD_CHIN_RLEASE_000LV_XA_03, time_scale=0.7)
        rockford.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, time_scale=0.7, trans_time=1, time_delay=2)

        rockford.start_head_ik(group=MAIN, duration=1000, time_delay=1)
        rockford.start_eye_ik(group=MAIN, duration=1000)

        main_group.append_time(2)

        rockford.facial(group=MAIN, index=30, extra_delay=0)

        # self.set_start_time(main_group.get_time())



        cam_trent_sitting.set(group=MAIN)

        cam_trent_sitting.move_cam(group=MAIN, index=2, duration=4, smooth=True)
        cam_trent_sitting.move_focus(group=MAIN, index=2, duration=4, smooth=True)

        MoveFastEvent(root=self, group=MAIN, object_name=trent.name, target_name=self.get_automarker_name('trent_near_table'))
        trent.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_STND_SITCR_TRNS_180DN_XA_06, time_scale=1)


        # DEBUG ONLY!

        trent.move_head_ik(group=MAIN, target_name=mrk_rockford_talk, immediately=True)
        trent.move_eye_ik(group=MAIN, target_name=mrk_rockford_talk, immediately=True)
        rockford.move_head_ik(group=MAIN, target_name=mrk_trent_talk, immediately=True)
        rockford.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, immediately=True)



        main_group.append_time(2.6)

        trent.facial(group=MAIN, index=40)

        main_group.append_time(0.8)

        cam_rockford.set(group=MAIN)

        MoveFastEvent(root=self, group=MAIN, object_name=trent.name, target_name=self.get_automarker_name('trent_talk'))
        trent.motion(group=MAIN, duration=20, loop=True, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, time_scale=1)

        rockford.facial(group=MAIN, index=50)

        cam_trent.set(group=MAIN)
        cam_trent.move_cam(group=MAIN, index=2, duration=14, smooth=True)

        trent.facial(group=MAIN, index=60)
        trent.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, time_scale=0.8, trans_time=0.5, time_delay=-0.25)
        trent.motion(group=MAIN, duration=20, loop=True, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, time_delay=2)
        trent.facial(group=MAIN, index=70)



        main_group.append_time(1)

        rockford.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06)

        cam_rockford.set(group=MAIN)
        rck_cam_mov1_time = main_group.get_time()
        rck_cam_mov1 = cam_rockford.move_cam(group=MAIN, index=2, duration=14, smooth=True)

        rockford.facial(group=MAIN, index=80)
        rockford.facial(group=MAIN, index=90)

        rockford.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_GRABR_CHIN_RLEASE_000LV_XA_02, time_scale=0.6, time_delay=-2)
        rockford.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_HOLD_CHIN_RLEASE_000LV_XA_03, trans_time=1, time_delay=2)
        rockford.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, trans_time=1, time_delay=3.5)



        rockford.move_head_ik(group=MAIN, target_name=mrk_rockford_smoke_head, duration=1, time_delay=0)
        rockford.move_eye_ik(group=MAIN, target_name=mrk_rockford_smoke_eye, duration=0.5, time_delay=0)
        rockford.move_head_ik(group=MAIN, target_name=mrk_trent_talk, duration=1, time_delay=2)
        rockford.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.5, time_delay=2)

        IkEvent(root=self, group=MAIN, char_name=rockford.name, target_name=mrk_rockford_smoking, duration=3,
                end_effector="RLowArm", up=Y_AXIS, front=Z_AXIS, time_delay=0, transition_duration=1)
        IkEvent(root=self, group=MAIN, char_name=rockford.name, target_name=mrk_rockford_smoking2, duration=3,
                end_effector="RHand", up=X_AXIS, front=Z_AXIS, time_delay=0, transition_duration=1)

        main_group.append_time(3)

        rockford.facial(group=MAIN, index=100)
        rockford.facial(group=MAIN, index=110)


        rockford.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDUP_TRNS_000LV_XA_02, time_scale=0.6, trans_time=0.5, time_delay=-2)
        rockford.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRF_CONV_RHND_CASL_000LV_XA_04, time_scale=0.6, trans_time=1, time_delay=0)
        rockford.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDDN_TRNS_000LV_XA_02, time_scale=0.6, trans_time=0.5, time_delay=4)
        rockford.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, time_scale=1,
                        trans_time=0.5, time_delay=6)


        rockford.facial(group=MAIN, index=120)

        rck_cam_mov1.set_duration(main_group.get_time() - rck_cam_mov1_time)

        cam_trent.set(group=MAIN)
        trent.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, time_scale=0.8,
                     trans_time=0.5)
        trent.facial(group=MAIN, index=130)







        cam_rockford.move_cam(group=MAIN, index=2, duration=0.1, smooth=False)  # # DBG!!!
        main_group.append_time(0.2)

        cam_rockford.set(group=MAIN)
        rck_cam_mov2_time = main_group.get_time()
        rck_cam_mov2 = cam_rockford.move_cam(group=MAIN, index=3, duration=14, smooth=True)

        rockford.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, time_scale=1)

        rockford.facial(group=MAIN, index=150)


        rockford.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDUP_TRNS_000LV_XA_02, time_scale=0.6, trans_time=0.5, time_delay=-4)
        rockford.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRF_CONV_RHND_CASL_000LV_XA_04, time_scale=0.6, trans_time=1, time_delay=-2)

        rockford.facial(group=MAIN, index=160)


        rockford.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_GRABR_CHIN_RLEASE_000LV_XA_02, trans_time=1, start_time=0.5, time_scale=0.6, time_delay=-2)
        rockford.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_HOLD_CHIN_RLEASE_000LV_XA_03, trans_time=1, time_delay=2)
        rockford.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, trans_time=1, time_delay=3.5)

        rockford.move_head_ik(group=MAIN, target_name=mrk_rockford_smoke_head, duration=1, time_delay=0)
        rockford.move_eye_ik(group=MAIN, target_name=mrk_rockford_smoke_eye, duration=0.5, time_delay=0)
        rockford.move_head_ik(group=MAIN, target_name=mrk_trent_talk, duration=1, time_delay=2)
        rockford.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.5, time_delay=2)

        IkEvent(root=self, group=MAIN, char_name=rockford.name, target_name=mrk_rockford_smoking, duration=3,
                end_effector="RLowArm", up=Y_AXIS, front=Z_AXIS, time_delay=-0.5, transition_duration=1)
        IkEvent(root=self, group=MAIN, char_name=rockford.name, target_name=mrk_rockford_smoking2, duration=3,
                end_effector="RHand", up=X_AXIS, front=Z_AXIS, time_delay=-0.5, transition_duration=1)

        rockford.move_head_ik(group=MAIN, target_name=mrk_rockford_smoke_head, duration=1, time_delay=-0.5)
        rockford.move_eye_ik(group=MAIN, target_name=mrk_rockford_smoke_eye, duration=0.5, time_delay=-0.5)
        rockford.move_head_ik(group=MAIN, target_name=mrk_trent_talk, duration=1, time_delay=2)
        rockford.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.5, time_delay=2)

        main_group.append_time(3)

        rockford.facial(group=MAIN, index=170)
        rockford.facial(group=MAIN, index=180)


        rockford.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, time_scale=0.6, trans_time=1, time_delay=0)

        rockford.facial(group=MAIN, index=200)

        rck_cam_mov2.set_duration(main_group.get_time() - rck_cam_mov2_time)



        main_group.append_time(0.3)

        cam_trent.set(group=MAIN)

        trent.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, time_scale=0.8, trans_time=0.5, time_delay=0)
        trent.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRB_SHRG_SHLDRS_BIG_000LV_XA_03, time_scale=0.8, trans_time=0.5, time_delay=0.5)
        trent.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, time_scale=1, trans_time=0.5, time_delay=4.2)

        trent.facial(group=MAIN, index=205)

        cam_rockford_walkout.set(group=MAIN)

        cam_rockford_walkout.move_cam(group=MAIN, index=2, duration=5, smooth=True, time_delay=3)
        cam_rockford_walkout.move_focus(group=MAIN, index=2, duration=5, smooth=True, time_delay=3)

        rockford.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, time_scale=1)

        rockford.move_head_ik(group=MAIN, target_name=mrk_rockford_stand_look, duration=1, time_delay=3)
        rockford.move_eye_ik(group=MAIN, target_name=mrk_rockford_stand_look, duration=0.5, time_delay=3)
        rockford.move_head_ik(group=MAIN, target_name=mrk_trent_talk_top, duration=1, time_delay=6)
        rockford.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.5, time_delay=6)



        rockford.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRB_STNDCL_TRNS_270LV_XA_06, time_scale=1, time_delay=2)
        RotateAxisEvent(root=self, group=MAIN, object_name=rockford.name, angle=-60, duration=2, smooth=False, time_delay=5)


        rockford.facial(group=MAIN, index=210)

        main_group.append_time(2.5)


        trent_head_ik.set_duration(main_group.get_time())
        trent_eye_ik.set_duration(main_group.get_time())

        rockford.facial(group=MAIN, index=220, extra_delay=0)

        rockford.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01, time_scale=0.85, trans_time=0.5, time_delay=0)
        rockford.motion(group=MAIN, duration=25, loop=True, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, time_scale=0.85, time_delay=1.27)

        rockford.move_head_ik(group=MAIN, target_name=mrk_rockford_walking, duration=1, time_delay=0)
        rockford.move_eye_ik(group=MAIN, target_name=mrk_rockford_walking, duration=0.5, time_delay=0)

        RotateAxisEvent(root=self, group=MAIN, object_name=rockford.name, angle=20, duration=1, smooth=False, time_delay=1.6)


        trent.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, time_scale=1, time_delay=0)

        main_group.append_time(2)


        cam_trent_damn.set(group=MAIN)
        cam_trent_damn.move_cam(group=MAIN, index=2, duration=10, smooth=True)

        trent.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_GRABR_HEAD_RLEASE_000LV_XA_02, time_scale=0.85, time_delay=0)

        main_group.append_time(1.5)
        trent.facial(group=MAIN, index=230)
        main_group.append_time(2)


        trent.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_HOLD_HEAD_RLEASE_000LV_XA_02, time_scale=1, time_delay=0)

        trent.facial(group=MAIN, index=250)

        main_group.append_time(1.2)

        lt_room3.turn_on(group=MAIN)
        cam_trent_pda.set(group=MAIN)
        cam_trent_pda.move_cam(group=MAIN, index=2, duration=12, smooth=True)

        trent.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRB_STNDCR_TRNS_090LV_XA_05, trans_time=2, time_scale=1, time_delay=-2)
        trent.motion(group=MAIN, duration=3, anim=Male.Sc_MLBODY_STND_GET_MAP_000LV_A_10, trans_time=1, start_time=2, time_scale=1, time_delay=1.6)


        main_group.append_time(2.5)

        kim.facial(group=MAIN, index=260)

        trent.facial(group=MAIN, index=270)
        kim.facial(group=MAIN, index=280)

        trent.motion(group=MAIN, duration=6, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, trans_time=2, time_scale=1, time_delay=-1)

        trent.facial(group=MAIN, index=290)
        trent.motion(group=MAIN, duration=6, anim=Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01, trans_time=1, time_scale=1, time_delay=0)

        main_group.append_time(1)
