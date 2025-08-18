from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import Male, Female, Trent

from story import actors


class DigSiteDoors(Prop):
    COMPOUND_TEMPLATE_NAME = 'st_01_dig_site_doors'


class Artifact(Prop):
    COMPOUND_TEMPLATE_NAME = 'prop_artifact_crystal'


class DigSiteTable(Prop):
    COMPOUND_TEMPLATE_NAME = 'table_analyzer'
    FORCE_POS = [
        -3.686486,
        0.398995,
        -8.169765
    ]
    FORCE_MATRIX = [
        [
            0.715366,
            0.016323,
            0.698559
        ],
        [
            0.698559,
            0.006647,
            -0.715522
        ],
        [
            -0.016323,
            0.999845,
            -0.006647
        ]
    ]


class Msn12SpragueScene(Scene):
    POINT_ROTATE_OVERRIDES = {
        'trent_talk': (0, -150, 0),
        'alaric_arrive': (0, -170, 0),
        'darcy_arrive': (0, -170, 0),
        'hatcher_talk': (0, 30, 0),
        'hatcher_init': (0, -135, 0),
        'mandrake_alarm': (0, -180, 0),

    }

    def action(self):
        main_group = self.get_group(MAIN)

        # CAMERAS

        cam_dbg = LookAtCamera(root=self, name='cam_dbg', fov=30)
        cam_start = LookAtCamera(root=self, name='cam_start', fov=25)
        cam_welcome = LookAtCamera(root=self, name='cam_welcome', fov=18)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=18)
        cam_trent_two = LookAtCamera(root=self, name='cam_trent_two', fov=18)
        cam_trent_three = LookAtCamera(root=self, name='cam_trent_three', fov=18)
        cam_trent_final = LookAtCamera(root=self, name='cam_trent_final', fov=18)
        cam_deal = LookAtCamera(root=self, name='cam_deal', fov=20)
        cam_impossible = LookAtCamera(root=self, name='cam_impossible', fov=22)
        cam_access = LookAtCamera(root=self, name='cam_access', fov=18)
        cam_alarm = LookAtCamera(root=self, name='cam_alarm', fov=22)
        cam_what_operation = LookAtCamera(root=self, name='cam_what_operation', fov=18)
        cam_final = LookAtCamera(root=self, name='cam_final', fov=18)


        # PROPS

        alarm = Music(root=self, name='alarm', sound='rtc_klaxon_loop_3', attenuation=-12)

        doors = DigSiteDoors(root=self, name='doors', init_point=self.DEFAULT_POINT_NAME, light_group=0)
        anim_open = 'Sc_door_open'
        anim_close = 'Sc_door_close'

        table = DigSiteTable(root=self, name='table', init_point=self.DEFAULT_POINT_NAME, light_group=0, use_ambient=True)
        anim_table = 'Sc_table animation'

        artifact = Artifact(root=self, name='prop_artifact', init_point=self.DEFAULT_POINT_NAME, light_group=0)

        # CHARACTERS

        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='trent_init', rotate_y=180)
        mandrake = Character(root=self, actor=actors.Mandrake, light_group=0, init_point='mandrake_init', rotate_y=-170)
        hatcher = Character(root=self, actor=actors.Hatcher, light_group=0, init_point='hatcher_init', rotate_y=-135)
        alaric = Character(root=self, actor=actors.Alaric, light_group=0, init_point='alaric_init', rotate_y=0)
        darcy = Character(root=self, actor=actors.Darcy, light_group=0, init_point='darcy_init', rotate_y=0)

        # MARKERS


        mrk_trent_init = trent.get_stand_marker('trent_init')
        mrk_trent_talk = trent.get_stand_marker('trent_talk')
        mrk_hatcher_talk = trent.get_stand_marker('hatcher_talk')
        mrk_mandrake_init = trent.get_stand_marker('mandrake_init')

        mrk_hatcher_work = self.get_automarker_name('mrk_hatcher_work')
        mrk_hatcher_work_top = self.get_automarker_name('mrk_hatcher_work_top')
        mrk_look_on_alaric = self.get_automarker_name('mrk_look_on_alaric')
        mrk_look_on_alaric_front = self.get_automarker_name('mrk_look_on_alaric_front')
        mrk_trent_front = self.get_automarker_name('mrk_trent_front')
        mrk_trent_back = self.get_automarker_name('mrk_trent_back')
        mrk_hatcher_front = self.get_automarker_name('mrk_hatcher_front')
        mrk_hatcher_front2 = self.get_automarker_name('mrk_hatcher_front2')
        mrk_hatcher_front_bottom = self.get_automarker_name('mrk_hatcher_front_bottom')
        mrk_mandrake_front = self.get_automarker_name('mrk_mandrake_front')
        mrk_mandrake_hand_chin = self.get_automarker_name('mrk_mandrake_hand_chin')
        mrk_mandrake_think = self.get_automarker_name('mrk_mandrake_think')
        mrk_mandrake_think_bottom = self.get_automarker_name('mrk_mandrake_think_bottom')
        mrk_mandrake_front_right = self.get_automarker_name('mrk_mandrake_front_right')
        mrk_alarm = self.get_automarker_name('mrk_alarm')
        mrk_alarm_top = self.get_automarker_name('mrk_alarm_top')

        # PREPARE

        mandrake.move_head_ik(group=BG, target_name=mrk_hatcher_work_top, immediately=True)
        mandrake.move_eye_ik(group=BG, target_name=mrk_hatcher_work, immediately=True)

        hatcher.move_head_ik(group=BG, target_name=mrk_trent_talk, immediately=True)
        hatcher.move_eye_ik(group=BG, target_name=mrk_trent_talk, immediately=True)

        alaric.move_head_ik(group=BG, target_name=mrk_trent_front, immediately=True)
        alaric.move_eye_ik(group=BG, target_name=mrk_trent_talk, immediately=True)

        darcy.move_head_ik(group=BG, target_name=mrk_trent_front, immediately=True)
        darcy.move_eye_ik(group=BG, target_name=mrk_trent_talk, immediately=True)

        trent.move_head_ik(group=BG, target_name=mrk_look_on_alaric_front, immediately=True)
        trent.move_eye_ik(group=BG, target_name=mrk_look_on_alaric, immediately=True)




        mandrake.start_head_ik(group=MAIN, duration=1000)
        mandrake.start_eye_ik(group=MAIN, duration=1000)

        hatcher_head_ik1 = hatcher.start_head_ik(group=MAIN, duration=1000, time_delay=8)
        hatcher_eye_ik1 = hatcher.start_eye_ik(group=MAIN, duration=1000, time_delay=7)

        # ACTION!

        cam_start.set(group=MAIN)
        # cam_welcome.set(group=MAIN)
        cam_start.move_cam(group=MAIN, index=2, duration=6, smooth=True)

        doors.anim(group=MAIN, anim=anim_open)

        mandrake.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06)
        mandrake.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_STND_TURN_270LV_XA_04, time_scale=0.8, trans_time=1, time_delay=6)
        mandrake.motion(group=MAIN, duration=90, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, trans_time=1, time_delay=10)

        mandrake.move_head_ik(group=MAIN, target_name=mrk_trent_talk, duration=4, time_delay=5)
        mandrake.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=1.5, time_delay=5)

        trent.motion(group=MAIN, duration=25, loop=True, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, start_time=0.5)
        trent.motion(group=MAIN, duration=5, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, time_delay=(1.3*7)-0.5)

        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=-25, duration=4, smooth=True, time_delay=3.5)

        hatcher.motion(group=MAIN, duration=7, start_time=7, anim=Female.Sc_SPCBODY_s002x_sinclair_XC_STND_000LV_26)
        hatcher.motion(group=MAIN, duration=7, anim=Female.Sc_FMBODY_STND_TURN_090LV_XA_03, time_scale=1, trans_time=2, time_delay=7)

        RotateAxisEvent(root=self, group=MAIN, object_name=hatcher.name, angle=-25, duration=3, smooth=True, time_delay=8)

        doors.anim(group=MAIN, anim=anim_close, time_delay=5)


        table.anim(group=MAIN, anim=anim_table, duration=2, time_scale=1, time_delay=0)

        main_group.append_time(8)
        cam_welcome.set(group=MAIN)

        table.anim(group=MAIN, anim=anim_table, duration=2, start_time=2)


        main_group.append_time(0.8)

        MoveFastEvent(root=self, group=MAIN, object_name=trent.name, target_name=self.get_automarker_name('trent_talk'))
        trent.motion(group=MAIN, duration=150, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)

        hatcher.facial(group=MAIN, index=10, extra_delay=0)
        hatcher.motion(group=MAIN, duration=3, anim=Female.Sc_FMHEAD_MAD_COLD_000LV_XA_, time_scale=1, trans_time=0.5)
        main_group.append_time(0.25)


        cam_trent.set(group=MAIN)



        trent.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_STND_CONV_RHND_CASL_000LV_xa_01, time_scale=0.8)
        trent.motion(group=MAIN, duration=5, loop=True, anim=Male.Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00, start_time=1, trans_time=0.2)

        trent.facial(group=MAIN, index=20)
        trent.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, trans_time=1, time_delay=-0.6)
        doors.anim(group=MAIN, anim=anim_open, time_delay=-0.25)

        cam_welcome.set(group=MAIN)

        hatcher.motion(group=MAIN, duration=7, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, trans_time=0.25)
        hatcher.motion(group=MAIN, duration=7, anim=Female.Sc_FMBODY_STND_CROSS_ARMS_000LV_XB_03, start_time=1, trans_time=1, time_delay=2)
        hatcher.motion(group=MAIN, duration=7, anim=Female.Sc_FMBODY_STND_UNCRSS_ARMS_000LV_XA_03, trans_time=1, time_scale=0.5, time_delay=4)
        hatcher.motion(group=MAIN, duration=7, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, time_scale=0.9, trans_time=1, time_delay=6)
        hatcher.facial(group=MAIN, index=30)
        hatcher.motion(group=MAIN, duration=3, anim=Female.Sc_FMHEAD_MAD_COLD_000LV_XA_, time_scale=1, trans_time=0.2)

        cam_deal.set(group=MAIN)
        cam_deal.move_cam(group=MAIN, index=2, duration=8, smooth=True)
        cam_deal.move_focus(group=MAIN, index=2, duration=6, smooth=True)


        MoveFastEvent(root=self, group=MAIN, object_name=trent.name, target_name=self.get_automarker_name('trent_talk'))
        trent.motion(group=MAIN, duration=150, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)

        trent.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_STND_TURN_045LV_XA_04, trans_time=0.3, time_delay=0.5)

        MoveFastEvent(root=self, group=MAIN, object_name=alaric.name, target_name=self.get_automarker_name('alaric_arrive'))
        alaric.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02)

        MoveFastEvent(root=self, group=MAIN, object_name=darcy.name, target_name=self.get_automarker_name('darcy_arrive'))
        darcy.motion(group=MAIN, duration=15, anim=Female.Sc_FMBODY_WLKG_000LV_XA_01)
        darcy.motion(group=MAIN, duration=15, anim=Female.Sc_FMBODY_WALK_STND_TRNS_000LV_XA_01, time_delay=1.3)
        darcy.motion(group=MAIN, duration=15, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, time_delay=3)

        alaric.start_head_ik(group=MAIN, duration=1000, time_delay=0.1)
        alaric.start_eye_ik(group=MAIN, duration=1000, time_delay=0.1)

        darcy.start_head_ik(group=MAIN, duration=1000, time_delay=0.1)
        darcy.start_eye_ik(group=MAIN, duration=1000, time_delay=0.1)

        darcy.move_head_ik(group=MAIN, target_name=mrk_mandrake_init, duration=1.5, time_delay=1)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_mandrake_init, duration=0.6, time_delay=1)

        darcy.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=1.5, time_delay=3.4)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_trent_back, duration=0.6, time_delay=3.4)

        trent.start_head_ik(group=MAIN, duration=1000, time_delay=1)
        trent.start_eye_ik(group=MAIN, duration=1000, time_delay=1)


        doors.anim(group=MAIN, anim=anim_close)

        main_group.append_time(0.5)
        alaric.facial(group=MAIN, index=40)

        trent.motion(group=MAIN, duration=150, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, time_scale=0.8)
        darcy.motion(group=MAIN, duration=15, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, time_delay=2)

        trent.move_head_ik(group=MAIN, target_name=mrk_hatcher_front, duration=2.8, time_delay=3)
        trent.move_eye_ik(group=MAIN, target_name=mrk_hatcher_talk, duration=1.2, time_delay=3)

        alaric.move_head_ik(group=MAIN, target_name=mrk_hatcher_front, duration=1.5, time_delay=2)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_hatcher_talk, duration=0.6, time_delay=2)

        alaric.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=1.5, time_delay=4.3)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.6, time_delay=4.3)

        darcy.move_head_ik(group=MAIN, target_name=mrk_mandrake_init, duration=1.5, time_delay=1)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_mandrake_init, duration=0.6, time_delay=1)

        darcy.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=1.5, time_delay=3.4)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_trent_back, duration=0.6, time_delay=3.4)

        trent.facial(group=MAIN, index=50)

        cam_welcome.set(group=MAIN)

        MoveFastEvent(root=self, group=MAIN, object_name=hatcher.name, target_name=self.get_automarker_name('hatcher_talk'))
        hatcher.motion(group=MAIN, duration=7, anim=Female.Sc_FMBODY_STND_FSTHIPB_HOLD_000LV_XA_01, time_scale=1)
        hatcher.motion(group=MAIN, duration=7, loop=True, anim=Female.Sc_FMBODY_STND_CONV_HNDS_CASL_000LV_xa_03, trans_time=1, time_delay=2)
        hatcher.motion(group=MAIN, duration=7, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, trans_time=1, time_delay=4.4)

        hatcher.facial(group=MAIN, index=60)

        cam_trent_two.set(group=MAIN)

        trent.motion(group=MAIN, duration=15, loop=True, anim=Male.Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00, time_delay=1, trans_time=0.2)
        trent.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, time_delay=2, trans_time=1)
        trent.motion(group=MAIN, duration=15, loop=True, anim=Male.Sc_MLBODY_STND_CONV_RHND_CASL_000LV_xa_01, time_delay=3, trans_time=0.5)
        trent.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_02, time_delay=6, trans_time=1)

        trent.move_head_ik(group=MAIN, target_name=mrk_look_on_alaric_front, duration=2.8, time_delay=2)
        trent.move_eye_ik(group=MAIN, target_name=mrk_look_on_alaric, duration=1.2, time_delay=2)

        trent.move_head_ik(group=MAIN, target_name=mrk_hatcher_front, duration=2.3, time_delay=5)
        trent.move_eye_ik(group=MAIN, target_name=mrk_hatcher_talk, duration=0.7, time_delay=5)

        trent.facial(group=MAIN, index=70)

        cam_impossible.set(group=MAIN)

        cam_impossible.move_cam(group=MAIN, index=2, duration=12, smooth=True, time_delay=5)
        cam_impossible.move_focus(group=MAIN, index=2, duration=4, smooth=True, time_delay=3)

        hatcher.facial(group=MAIN, index=80, extra_delay=0)
        hatcher.motion(group=MAIN, duration=3, anim=Female.Sc_FMHEAD_MAD_COLD_000LV_XA_, time_scale=1, trans_time=0.5)


        mandrake.move_head_ik(group=MAIN, target_name=mrk_hatcher_front, duration=2.3, time_delay=-1)
        mandrake.move_eye_ik(group=MAIN, target_name=mrk_hatcher_talk, duration=0.7, time_delay=-1)

        mandrake.facial(group=MAIN, index=90)
        main_group.append_time(0)

        hatcher.motion(group=MAIN, duration=7, anim=Female.Sc_FMBODY_STND_UNCRSS_ARMS_000LV_XA_03, trans_time=1, time_delay=1)

        hatcher.move_head_ik(group=MAIN, target_name=mrk_mandrake_front, duration=2.3, time_delay=-0.7)
        hatcher.move_eye_ik(group=MAIN, target_name=mrk_mandrake_init, duration=0.7, time_delay=-0.7)

        hatcher.facial(group=MAIN, index=100)

        mandrake.motion(group=MAIN, duration=90, anim=Male.Sc_MLBODY_STND_GRABR_CHIN_RLEASE_000LV_XA_01, time_scale=0.8, trans_time=1)

        group_think = 'bg_think'
        self.clone_group(group_think, MAIN)
        self.get_group(group_think).append_time(1)
        mandrake.motion(group=group_think, duration=0.5, anim=Male.Sc_MLHAND_HNEUT_GESTR_FIST_000LV_00, start_time=0.4, time_scale=0.2, trans_time=0.1, repeat=6, time_append=0.5)

        IkEvent(root=self, group=MAIN, char_name=mandrake.name, target_name=mrk_mandrake_hand_chin, duration=4,
                end_effector="RHand", up=X_AXIS, front=Z_AXIS, time_delay=0.01, transition_duration=1)

        mandrake.move_head_ik(group=MAIN, target_name=mrk_mandrake_think, duration=2.3, time_delay=0)
        mandrake.move_eye_ik(group=MAIN, target_name=mrk_mandrake_think_bottom, duration=0.7, time_delay=0)

        mandrake.move_head_ik(group=MAIN, target_name=mrk_hatcher_front, duration=2.3, time_delay=3)
        mandrake.move_eye_ik(group=MAIN, target_name=mrk_hatcher_talk, duration=0.7, time_delay=3)

        cam_impossible.move_focus(group=MAIN, index=3, duration=7, smooth=True)

        hatcher.motion(group=MAIN, duration=7, anim=Female.Sc_FMBODY_STND_IDLE_BIG_000LV_xa_05, trans_time=1, time_delay=-1)
        hatcher.motion(group=MAIN, duration=7, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, time_scale=0.6, trans_time=1, time_delay=3)
        hatcher.motion(group=MAIN, duration=7, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, time_scale=0.4, trans_time=1, time_delay=8)

        mandrake.facial(group=MAIN, index=110)

        hatcher.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=2.3, time_delay=1)
        hatcher.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.7, time_delay=1)

        hatcher.move_head_ik(group=MAIN, target_name=mrk_mandrake_front, duration=2.3, time_delay=4)
        hatcher.move_eye_ik(group=MAIN, target_name=mrk_mandrake_init, duration=0.7, time_delay=4)


        mandrake.motion(group=MAIN, duration=90, anim=Male.Sc_MLBODY_STND_HOLD_CHIN_RLEASE_000LV_XA_01, time_scale=1, trans_time=1, time_delay=-1)
        mandrake.motion(group=MAIN, duration=90, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, time_scale=0.58, trans_time=1, time_delay=1)

        mandrake.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=2.3, time_delay=2)
        mandrake.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.7, time_delay=2)

        mandrake.move_head_ik(group=MAIN, target_name=mrk_hatcher_front, duration=2.3, time_delay=5)
        mandrake.move_eye_ik(group=MAIN, target_name=mrk_hatcher_talk, duration=0.7, time_delay=5)

        mandrake.facial(group=MAIN, index=120)

        #

        alaric.move_head_ik(group=MAIN, target_name=mrk_mandrake_front, immediately=True, time_delay=-1)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_mandrake_init, immediately=True, time_delay=-1)

        darcy.move_head_ik(group=MAIN, target_name=mrk_mandrake_front, immediately=True, time_delay=-1)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_mandrake_init, immediately=True, time_delay=-1)

        cam_access.set(group=MAIN)

        darcy.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=1.5, time_delay=1)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.6, time_delay=1)

        alaric.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=2, time_delay=1)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.6, time_delay=1)



        trent.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_STND_GIVE_VEND_000LV_B_07, trans_time=1)

        alaric.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, trans_time=1)
        darcy.motion(group=MAIN, duration=15, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05, trans_time=1)

        darcy.motion(group=MAIN, duration=15, anim=Female.Sc_FMBODY_STND_CROSS_ARMS_000LV_XB_03, time_scale=0.7,
                     trans_time=1, time_delay=2)
        darcy.motion(group=MAIN, duration=2, anim=Female.Sc_FMHAND_HNEUT_GESTL_FIST_000LV_00, time_scale=1,
                     time_delay=2)
        darcy.motion(group=MAIN, duration=2, anim=Female.Sc_FMHAND_HNEUT_GESTR_FIST_000LV_00, time_scale=1,
                     time_delay=2)

        trent.move_head_ik(group=MAIN, target_name=mrk_mandrake_front_right, duration=1.8, time_delay=0)
        trent.move_eye_ik(group=MAIN, target_name=mrk_mandrake_front_right, duration=0.7, time_delay=0)

        trent.move_head_ik(group=MAIN, target_name=mrk_look_on_alaric_front, duration=1.8, time_delay=5)
        trent.move_eye_ik(group=MAIN, target_name=mrk_look_on_alaric, duration=0.7, time_delay=5)

        trent.facial(group=MAIN, index=130)
        darcy.facial(group=MAIN, index=140)

        alaric.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, time_scale=0.7,
                      trans_time=0.2)
        trent.motion(group=MAIN, duration=5, loop=True, anim=Male.Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00, start_time=1, trans_time=0.2)
        alaric.facial(group=MAIN, index=150)

        cam_welcome.set(group=MAIN)

        hatcher.motion(group=MAIN, duration=7, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01)
        hatcher.motion(group=MAIN, duration=7, anim=Female.Sc_FMBODY_STND_CONV_HNDS_CASL_000LV_xb_03, trans_time=1, time_delay=2.5)
        hatcher.motion(group=MAIN, duration=7, anim=Female.Sc_FMBODY_STND_SHRG_SHLDRS_SMALL_000LV_XA_02, trans_time=1, time_delay=4)

        hatcher.move_head_ik(group=MAIN, target_name=mrk_trent_talk, duration=2)
        hatcher.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.6)

        hatcher.facial(group=MAIN, index=160)
        darcy.motion(group=MAIN, duration=15, anim=Female.Sc_FMBODY_STND_UNCRSS_ARMS_000LV_XA_03)
        darcy.motion(group=MAIN, duration=15, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, trans_time=1,
                     time_delay=3)
        alaric.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)

        cam_trent_three.set(group=MAIN)

        conn_time = main_group.get_time()
        conn = ConnectHardpointEvent(root=self, group=MAIN, target_name=artifact.name, parent_name=trent.name,
                                     duration=61, target_hardpoint="hplefthandconnect_prop_crystal",
                                     parent_hardpoint="hpleftconnect")

        trent.motion(group=MAIN, duration=15, anim=Male.Sc_SPCBODY_s020x_Trent_XA_STND_SHOW_ARTFCT_000LV_06,
                     time_delay=0)

        trent.move_head_ik(group=MAIN, target_name=mrk_hatcher_front2, duration=1.8, time_delay=0)
        trent.move_eye_ik(group=MAIN, target_name=mrk_hatcher_talk, duration=0.7, time_delay=0)

        trent.move_head_ik(group=MAIN, target_name=mrk_look_on_alaric_front, duration=2.5, time_delay=3)
        trent.move_eye_ik(group=MAIN, target_name=mrk_look_on_alaric, duration=0.7, time_delay=3)

        alaric.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=2, time_delay=1.1)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.7, time_delay=1)

        darcy.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=1.7, time_delay=0.9)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.7, time_delay=1)

        alaric.motion(group=MAIN, duration=15, anim=Female.Sc_FMHEAD_SURPRSE_IMPRESSED_000LV_XA_, trans_time=0.25,
                      time_delay=1)

        trent.facial(group=MAIN, index=170)
        darcy.facial(group=MAIN, index=180)
        alarm.start(group=MAIN, duration=30, loop=True)
        alarm.change_attenuation(group=MAIN, duration=2, attenuation=-20, time_delay=4)

        cam_trent_three.move_cam(group=MAIN, index=2, duration=5, smooth=True)
        cam_trent_three.move_focus(group=MAIN, index=2, duration=5, smooth=True)

        main_group.append_time(1)

        alaric.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_STND_TURN_315LV_XA_02, trans_time=0.25, time_delay=0)
        trent.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_STND_TURN_045LV_XA_04, trans_time=0.25,
                     time_delay=-0.25)
        darcy.motion(group=MAIN, duration=15, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, trans_time=0.25,
                     time_delay=0)

        trent.move_head_ik(group=MAIN, target_name=mrk_alarm, duration=1.8, time_delay=0)
        trent.move_eye_ik(group=MAIN, target_name=mrk_alarm_top, duration=0.7, time_delay=0)

        alaric.move_head_ik(group=MAIN, target_name=mrk_alarm, duration=2, time_delay=0)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_alarm_top, duration=0.7, time_delay=0)

        darcy.move_head_ik(group=MAIN, target_name=mrk_alarm, duration=1.7, time_delay=0.9)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_alarm_top, duration=0.7, time_delay=1)

        main_group.append_time(1)

        alaric.facial(group=MAIN, index=190)

        hatcher_head_ik1.set_duration(main_group.get_time()-10)
        hatcher_eye_ik1.set_duration(main_group.get_time()-10)

        conn.set_duration(main_group.get_time() - conn_time)

        MoveOffscreenEvent(root=self, object_name=artifact.name, time_delay=1)

        main_group.append_time(2)

        # cam_start.set(group=MAIN)
        #




        #
        #
        # main_group.append_time(1000)
        #
        #
        # cam_deal.set(group=MAIN)
        #
        #
        # main_group.append_time(1000)
        #
        #
        # self.set_start_time(main_group.get_time())
        #
        #
        #
        # main_group.append_time(0.1)
        # trent.move_head_ik(group=MAIN, target_name=mrk_alarm, immediately=True)
        # trent.move_eye_ik(group=MAIN, target_name=mrk_alarm_top, immediately=True)
        #
        # alaric.move_head_ik(group=MAIN, target_name=mrk_alarm, immediately=True)
        # alaric.move_eye_ik(group=MAIN, target_name=mrk_alarm_top, immediately=True)
        #
        # darcy.move_head_ik(group=MAIN, target_name=mrk_alarm, immediately=True)
        # darcy.move_eye_ik(group=MAIN, target_name=mrk_alarm_top, immediately=True)
        #
        # mandrake.move_head_ik(group=MAIN, target_name=mrk_alarm, immediately=True)
        # mandrake.move_eye_ik(group=MAIN, target_name=mrk_alarm_top, immediately=True)
        #
        #
        # alaric.start_head_ik(group=MAIN, duration=1000, time_delay=0.1)
        # alaric.start_eye_ik(group=MAIN, duration=1000, time_delay=0.1)
        #
        # darcy.start_head_ik(group=MAIN, duration=1000, time_delay=0.1)
        # darcy.start_eye_ik(group=MAIN, duration=1000, time_delay=0.1)
        #
        # trent.start_head_ik(group=MAIN, duration=1000, time_delay=1.1)
        # trent.start_eye_ik(group=MAIN, duration=1000, time_delay=1.1)
        #
        # mandrake.start_head_ik(group=MAIN, duration=1000, time_delay=1.1)
        # mandrake.start_eye_ik(group=MAIN, duration=1000, time_delay=1.1)
        #
        # cam_dbg.set(group=MAIN)
        #
        #
        #
        # MoveFastEvent(root=self, group=MAIN, object_name=trent.name, target_name=self.get_automarker_name('trent_talk'))
        # trent.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_STND_TURN_045LV_XA_04, time_scale=10, time_delay=0)
        # trent.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_STND_TURN_045LV_XA_04, time_scale=10, time_delay=0.25)
        #
        # MoveFastEvent(root=self, group=MAIN, object_name=mandrake.name, target_name=self.get_automarker_name('mandrake_alarm'))
        # mandrake.motion(group=MAIN, duration=5, anim=Male.Sc_MLBODY_STND_TURN_270LV_XA_04, time_scale=10, time_delay=0.1)

        #
        # trent.start_head_ik(group=MAIN, duration=1000, time_delay=0.1)
        # trent.start_eye_ik(group=MAIN, duration=1000, time_delay=0.1)

        # trent.move_head_ik(group=MAIN, target_name=mrk_look_on_alaric_front, immediately=True, time_delay=0.1)
        # trent.move_eye_ik(group=MAIN, target_name=mrk_look_on_alaric_front, immediately=True, time_delay=0.1)
        #
        #
        #
        # MoveFastEvent(root=self, group=MAIN, object_name=alaric.name, target_name=self.get_automarker_name('alaric_arrive'))
        # alaric.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02)
        #
        # MoveFastEvent(root=self, group=MAIN, object_name=darcy.name, target_name=self.get_automarker_name('darcy_arrive'))
        # darcy.motion(group=MAIN, duration=15, anim=Female.Sc_FMBODY_WLKG_000LV_XA_01)
        # darcy.motion(group=MAIN, duration=15, anim=Female.Sc_FMBODY_WALK_STND_TRNS_000LV_XA_01, time_delay=1.3)
        #
        #
        #
        # main_group.append_time(3.1)
        #
        # alaric.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_STND_TURN_315LV_XA_02, time_scale=10, time_delay=0)
        #
        # main_group.append_time(1)
        #
        #
        #
        #
        #


















        #
        #
        #
        # trent.move_head_ik(group=MAIN, target_name=mrk_look_on_alaric_front, duration=1.8, time_delay=0)
        # trent.move_eye_ik(group=MAIN, target_name=mrk_look_on_alaric, duration=0.7, time_delay=0)
        #
        # trent.motion(group=MAIN, duration=7, anim=Male.Sc_MLBODY_STND_TURN_270LV_XA_04, time_scale=10, time_delay=1)
        # trent.motion(group=MAIN, duration=7, anim=Male.Sc_MLBODY_STND_TURN_045LV_XA_04, time_scale=10, time_delay=2)
        #
        #
        #
        #
        #
        # main_group.append_time(4)


        # main_group.append_time(1000)

        MoveFastEvent(root=self, group=MAIN, object_name=hatcher.name,
                      target_name=self.get_automarker_name('hatcher_init'))

        cam_alarm.set(group=MAIN)
        cam_alarm.move_cam(group=MAIN, index=2, duration=10, smooth=True)
        cam_alarm.move_focus(group=MAIN, index=2, duration=10, smooth=True)

        trent.motion(group=MAIN, duration=5, anim=Male.Sc_MLHAND_NEUT_LEFT_000LV_A_00, start_time=0, trans_time=0.2)
        trent.motion(group=MAIN, duration=5, anim=Male.Sc_MLHAND_NEUT_RGHT_000LV_A_00, start_time=0, trans_time=0.2)
        trent.motion(group=MAIN, duration=7, anim=Male.Sc_MLBODY_STND_TURN_270LV_XA_04, trans_time=0.5, time_delay=1)

        mandrake.motion(group=MAIN, duration=7, anim=Male.Sc_MLBODY_STND_TURN_045LV_XA_04, trans_time=0.5, time_delay=4)
        mandrake.motion(group=MAIN, duration=35, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, trans_time=0.5, time_delay=7)
        alaric.motion(group=MAIN, duration=7, anim=Male.Sc_MLBODY_STND_TURN_045LV_XA_04, trans_time=0.5, time_delay=2)

        mandrake.move_head_ik(group=MAIN, target_name=mrk_hatcher_work_top, duration=2.5, time_delay=3)
        mandrake.move_eye_ik(group=MAIN, target_name=mrk_hatcher_work, duration=0.7, time_delay=3)

        trent.move_head_ik(group=MAIN, target_name=mrk_look_on_alaric_front, duration=2.5, time_delay=0.1)
        trent.move_eye_ik(group=MAIN, target_name=mrk_look_on_alaric, duration=0.7, time_delay=0.1)

        trent.move_head_ik(group=MAIN, target_name=mrk_hatcher_work_top, duration=2.5, time_delay=2)
        trent.move_eye_ik(group=MAIN, target_name=mrk_hatcher_work_top, duration=0.7, time_delay=2)

        alaric.move_head_ik(group=MAIN, target_name=mrk_hatcher_work_top, duration=1.8, time_delay=2)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_hatcher_work_top, duration=0.7, time_delay=2)

        darcy.move_head_ik(group=MAIN, target_name=mrk_hatcher_work_top, duration=1.8, time_delay=1)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_hatcher_work_top, duration=0.7, time_delay=1)

        table.anim(group=MAIN, anim=anim_table, start_time=1, duration=1, time_scale=1, time_delay=0)
        hatcher.motion(group=MAIN, duration=15, start_time=12, anim=Female.Sc_SPCBODY_s002x_sinclair_XC_STND_000LV_26)
        hatcher.motion(group=MAIN, duration=15, anim=Female.Sc_FMBODY_STND_TURN_RGHT_180LV_XA_02, time_scale=0.8, trans_time=0.6, time_delay=11)
        hatcher.motion(group=MAIN, duration=15, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, trans_time=0.6, time_delay=14)

        hatcher.facial(group=MAIN, index=250)


        alaric.motion(group=MAIN, duration=7, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, trans_time=0.5)
        darcy.motion(group=MAIN, duration=7, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, trans_time=0.5, time_delay=-1)

        darcy.motion(group=MAIN, duration=7, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, trans_time=0.5, time_delay=4)

        hatcher.facial(group=MAIN, index=260)


        mandrake.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=1.8, time_delay=1)
        mandrake.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.7, time_delay=1)

        alaric.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=1.8, time_delay=-0.5)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.7, time_delay=-0.5)

        darcy.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=1.8, time_delay=0)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.7, time_delay=0)

        alaric.move_head_ik(group=MAIN, target_name=mrk_hatcher_work_top, duration=1.8, time_delay=2)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_hatcher_work_top, duration=0.7, time_delay=2)

        alaric.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=1.8, time_delay=4)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_trent_front, duration=0.7, time_delay=4)

        darcy.move_head_ik(group=MAIN, target_name=mrk_hatcher_work_top, duration=1.8, time_delay=3)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_hatcher_work_top, duration=0.7, time_delay=3)

        trent.move_head_ik(group=MAIN, target_name=mrk_look_on_alaric_front, duration=1.8, time_delay=2)
        trent.move_eye_ik(group=MAIN, target_name=mrk_look_on_alaric, duration=0.7, time_delay=2)

        trent.motion(group=MAIN, duration=7, anim=Male.Sc_MLBODY_STND_TURN_045LV_XA_04, trans_time=0.5, time_delay=3)

        trent.facial(group=MAIN, index=270)

        cam_what_operation.set(group=MAIN)
        table.anim(group=MAIN, anim=anim_table, duration=2, start_time=2)

        hatcher.facial(group=MAIN, index=280)

        MoveOffscreenEvent(root=self, group=MAIN, object_name=hatcher.name)



        alaric.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=1.8, time_delay=1)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.7, time_delay=1)

        darcy.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=1.8, time_delay=1)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.7, time_delay=1)

        darcy.move_head_ik(group=MAIN, target_name=mrk_hatcher_front2, duration=1.8, time_delay=4)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_hatcher_front2, duration=0.7, time_delay=4)

        darcy.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=1.8, time_delay=7)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_trent_front, duration=0.7, time_delay=7)

        darcy.move_head_ik(group=MAIN, target_name=mrk_hatcher_front2, duration=1.8, time_delay=9)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_hatcher_front2, duration=0.7, time_delay=9)

        cam_trent_final.set(group=MAIN)
        cam_trent_final.move_cam(group=MAIN, index=2, duration=20, smooth=True)
        cam_trent_final.move_focus(group=MAIN, index=2, duration=20, smooth=True)

        trent.move_head_ik(group=MAIN, target_name=mrk_hatcher_talk, duration=1.8, time_delay=0)
        trent.move_eye_ik(group=MAIN, target_name=mrk_hatcher_talk, duration=0.7, time_delay=0)

        trent.motion(group=MAIN, duration=7, anim=Male.Sc_MLBODY_STND_TURN_270LV_XA_04, trans_time=0.25, time_delay=0)

        trent.facial(group=MAIN, index=290)

        trent.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_CONV_HNDS_CASL_000LV_xa_04, trans_time=1, time_delay=0)
        trent.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00, start_time=1, trans_time=0.2)
        trent.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLHAND_HNEUT_GESTL_CASL_000LV_00, start_time=1, trans_time=0.2)

        trent.facial(group=MAIN, index=300)

        alaric.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, trans_time=1, time_delay=-1)
        darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_CROSS_ARMS_000LV_XB_03, trans_time=1, time_delay=-4)
        darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_UNCRSS_ARMS_000LV_XA_03, trans_time=1, time_delay=1)
        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, trans_time=1, time_delay=2)

        darcy.move_head_ik(group=MAIN, target_name=mrk_hatcher_front2, duration=2.5, time_delay=0)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_hatcher_front2, duration=0.7, time_delay=0)


        MoveOffscreenEvent(root=self, object_name=mandrake.name)

        trent.facial(group=MAIN, index=310)

        alaric.move_head_ik(group=MAIN, target_name=mrk_hatcher_front2, duration=1.8, time_delay=-6)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_hatcher_talk, duration=0.7, time_delay=-6)

        alaric.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=1.8, time_delay=-4)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.7, time_delay=-4)

        alaric.move_head_ik(group=MAIN, target_name=mrk_hatcher_front2, duration=1.8, time_delay=-2)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_hatcher_talk, duration=0.7, time_delay=-2)



        darcy.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=1.8, time_delay=-5)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_trent_front, duration=0.7, time_delay=-5)

        darcy.move_head_ik(group=MAIN, target_name=mrk_hatcher_front2, duration=1.8, time_delay=-3)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_hatcher_front2, duration=0.7, time_delay=-3)

        darcy.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=1.8, time_delay=-1)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_trent_front, duration=0.7, time_delay=-1)

        # main_group.append_time(10)
        #
        # self.set_start_time(main_group.get_time())

        MoveFastEvent(root=self, group=MAIN, object_name=hatcher.name, target_name=self.get_automarker_name('hatcher_talk'))
        hatcher.motion(group=MAIN, duration=7, anim=Female.Sc_FMBODY_STND_FSTHIPB_HOLD_000LV_XA_01)
        hatcher.motion(group=MAIN, duration=7, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, trans_time=0.5, time_delay=1)
        hatcher.motion(group=MAIN, duration=7, anim=Female.Sc_FMBODY_STND_WALK_TRNS_000LV_XA_01, trans_time=0.5, time_delay=2)

        cam_final.set(group=MAIN)


        hatcher.facial(group=MAIN, index=320, extra_delay=0)
        hatcher.motion(group=MAIN, duration=7, anim=Female.Sc_FMHEAD_MAD_SNARL_000LV_XA_)

        main_group.append_time(1.1)




        #
        #
        #
        #
        #
        #
        # cam_welcome.set(group=MAIN)
        #
        # hatcher.move_head_ik(group=MAIN, target_name=mrk_mandrake_front, immediately=True, time_delay=0.1)
        # hatcher.move_eye_ik(group=MAIN, target_name=mrk_mandrake_init, immediately=True, time_delay=0.1)
        #
        # MoveFastEvent(root=self, group=MAIN, object_name=hatcher.name, target_name=self.get_automarker_name('hatcher_talk'))
        # hatcher.motion(group=MAIN, duration=7, anim=Female.Sc_FMBODY_STND_FSTHIPB_HOLD_000LV_XA_01)
        #
        # hatcher.start_head_ik(group=MAIN, duration=1000)
        # hatcher.start_eye_ik(group=MAIN, duration=1000)
        #
        #
        # main_group.append_time(1)
        # hatcher.motion(group=MAIN, duration=7, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01)
        # hatcher.motion(group=MAIN, duration=7, anim=Female.Sc_FMBODY_STND_CONV_HNDS_CASL_000LV_xb_03, trans_time=1, time_delay=2.5)
        # hatcher.motion(group=MAIN, duration=7, anim=Female.Sc_FMBODY_STND_SHRG_SHLDRS_SMALL_000LV_XA_02, trans_time=1, time_delay=4)
        #
        # hatcher.move_head_ik(group=MAIN, target_name=mrk_trent_talk, duration=2)
        # hatcher.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.6)
        #
        # hatcher.facial(group=MAIN, index=160)

        #
        #
        #
        #
        # MoveFastEvent(root=self, group=MAIN, object_name=trent.name, target_name=self.get_automarker_name('trent_talk'))
        # trent.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_STND_TURN_045LV_XA_04, time_scale=10, time_delay=0)
        #
        # trent.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, time_delay=0.5)
        #
        # trent.start_head_ik(group=MAIN, duration=1000, time_delay=0.1)
        # trent.start_eye_ik(group=MAIN, duration=1000, time_delay=0.1)
        #
        # trent.move_head_ik(group=MAIN, target_name=mrk_look_on_alaric_front, immediately=True, time_delay=0.1)
        # trent.move_eye_ik(group=MAIN, target_name=mrk_look_on_alaric_front, immediately=True, time_delay=0.1)
        #
        #
        #
        # MoveFastEvent(root=self, group=MAIN, object_name=alaric.name, target_name=self.get_automarker_name('alaric_arrive'))
        # alaric.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02)
        #
        # MoveFastEvent(root=self, group=MAIN, object_name=darcy.name, target_name=self.get_automarker_name('darcy_arrive'))
        # darcy.motion(group=MAIN, duration=15, anim=Female.Sc_FMBODY_WLKG_000LV_XA_01)
        # darcy.motion(group=MAIN, duration=15, anim=Female.Sc_FMBODY_WALK_STND_TRNS_000LV_XA_01, time_delay=1.3)
        #
        #
        #
        # alaric.move_head_ik(group=MAIN, target_name=mrk_mandrake_front, immediately=True, time_delay=0.01)
        # alaric.move_eye_ik(group=MAIN, target_name=mrk_mandrake_init, immediately=True, time_delay=0.01)
        #
        # darcy.move_head_ik(group=MAIN, target_name=mrk_mandrake_front, immediately=True, time_delay=0.01)
        # darcy.move_eye_ik(group=MAIN, target_name=mrk_mandrake_init, immediately=True, time_delay=0.01)
        #
        # alaric.start_head_ik(group=MAIN, duration=1000, time_delay=0.1)
        # alaric.start_eye_ik(group=MAIN, duration=1000, time_delay=0.1)
        #
        # darcy.start_head_ik(group=MAIN, duration=1000, time_delay=0.1)
        # darcy.start_eye_ik(group=MAIN, duration=1000, time_delay=0.1)
        #
        #
        # main_group.append_time(3)








        # main_group.append_time(5)
        #
        # darcy.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=1.5, time_delay=1)
        # darcy.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.6, time_delay=1)
        #
        # alaric.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=2, time_delay=1)
        # alaric.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.6, time_delay=1)
        #
        #
        # trent.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_STND_GIVE_VEND_000LV_B_07, trans_time=1)
        #
        # alaric.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, trans_time=1)
        # darcy.motion(group=MAIN, duration=15, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05, trans_time=1)
        #
        # darcy.motion(group=MAIN, duration=15, anim=Female.Sc_FMBODY_STND_CROSS_ARMS_000LV_XB_03, time_scale=0.7, trans_time=1, time_delay=2)
        # darcy.motion(group=MAIN, duration=2, anim=Female.Sc_FMHAND_HNEUT_GESTL_FIST_000LV_00, time_scale=1, time_delay=2)
        # darcy.motion(group=MAIN, duration=2, anim=Female.Sc_FMHAND_HNEUT_GESTR_FIST_000LV_00, time_scale=1, time_delay=2)
        #
        # trent.move_head_ik(group=MAIN, target_name=mrk_mandrake_front_right, duration=1.8, time_delay=0)
        # trent.move_eye_ik(group=MAIN, target_name=mrk_mandrake_front_right, duration=0.7, time_delay=0)
        #
        # trent.move_head_ik(group=MAIN, target_name=mrk_look_on_alaric_front, duration=1.8, time_delay=5)
        # trent.move_eye_ik(group=MAIN, target_name=mrk_look_on_alaric, duration=0.7, time_delay=5)
        #
        # trent.facial(group=MAIN, index=130)
        # darcy.facial(group=MAIN, index=140)
        #
        # alaric.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, time_scale=0.7, trans_time=0.2)
        # alaric.facial(group=MAIN, index=150)
        #
        # cam_welcome.set(group=MAIN)
        #




        # trent.motion(group=MAIN, duration=15, loop=True, anim=Male.Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00, time_delay=1, trans_time=0.2)
        # trent.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, time_delay=2, trans_time=1)
        # trent.motion(group=MAIN, duration=15, loop=True, anim=Male.Sc_MLBODY_STND_CONV_RHND_CASL_000LV_xa_01, time_delay=3, trans_time=0.5)
        # trent.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_02, time_delay=6, trans_time=1)
        # # trent.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, time_delay=7, trans_time=1)
        #
        # trent.move_head_ik(group=MAIN, target_name=mrk_look_on_alaric_front, duration=2.8, time_delay=2)
        # trent.move_eye_ik(group=MAIN, target_name=mrk_look_on_alaric, duration=1.2, time_delay=2)
        #
        # trent.move_head_ik(group=MAIN, target_name=mrk_hatcher_front, duration=2.3, time_delay=5)
        # trent.move_eye_ik(group=MAIN, target_name=mrk_hatcher_talk, duration=0.7, time_delay=5)
        #
        # trent.facial(group=MAIN, index=70)

        #
        # main_group.append_time(1000)
        #
        #
        #
        # self.set_start_time(main_group.get_time())
        #
        # mandrake.move_head_ik(group=MAIN, target_name=mrk_trent_talk, immediately=True, time_delay=0.1)
        # mandrake.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, immediately=True, time_delay=0.1)
        #
        # mandrake.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_STND_TURN_270LV_XA_04, time_scale=10)
        # mandrake.motion(group=MAIN, duration=90, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, time_delay=1)
        #
        # MoveFastEvent(root=self, group=MAIN, object_name=hatcher.name, target_name=self.get_automarker_name('hatcher_talk'))
        # hatcher.motion(group=MAIN, duration=7, anim=Female.Sc_FMBODY_STND_FSTHIPB_HOLD_000LV_XA_01)
        # hatcher.motion(group=MAIN, duration=7, anim=Female.Sc_FMBODY_STND_SHRG_SHLDRS_SMALL_000LV_XA_02, trans_time=1, time_delay=1)
        # hatcher.motion(group=MAIN, duration=7, anim=Female.Sc_FMBODY_STND_CROSS_ARMS_000LV_XB_03, trans_time=1, time_delay=3)
        #
        # hatcher.start_head_ik(group=MAIN, duration=1000)
        # hatcher.start_eye_ik(group=MAIN, duration=1000)
        #
        # mandrake.start_head_ik(group=MAIN, duration=1000)
        # mandrake.start_eye_ik(group=MAIN, duration=1000)

        # main_group.append_time(1.1)

        # mandrake.move_head_ik(group=MAIN, target_name=mrk_hatcher_front, immediately=True, time_delay=0.2)
        # mandrake.move_eye_ik(group=MAIN, target_name=mrk_hatcher_talk, immediately=True, time_delay=0.2)

        #
        # cam_impossible.move_cam(group=MAIN, index=2, duration=1, smooth=True, time_delay=0)
        # cam_impossible.move_focus(group=MAIN, index=2, duration=1, smooth=True, time_delay=0)




