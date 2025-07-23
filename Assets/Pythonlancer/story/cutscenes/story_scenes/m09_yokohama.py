from story.cutscenes.scene import Scene
from story.cutscenes.content import (BG, MAIN, Character, LookAtCamera, FloorHeightEvent, RotateAxisEvent,
                                     NeckIkEvent, Char2CharNeckIkEvent, MoveFastEvent)
from story.cutscenes.anim import Male, Female

from story import actors


class Msn9YokohamaCutsceneThorn(Scene):
    POINT_ROTATE_OVERRIDES = {
        'darcy_goend': (0, -130, 0),
        'hassler_walkin': (0, 90, 0),
        'hassler_talk': (0, 90, 0),
    }

    def action(self):
        main_group = self.get_group(MAIN)

        down_floor_height = self.get_point('floor_bottom').position[1]

        # CAMERAS

        cam_dbg = LookAtCamera(root=self, name='cam_dbg', fov=30)
        cam_lift = LookAtCamera(root=self, name='cam_lift', fov=22)
        cam_liftback = LookAtCamera(root=self, name='cam_liftback', fov=20)
        cam_go = LookAtCamera(root=self, name='cam_go', fov=20)
        cam_goend = LookAtCamera(root=self, name='cam_goend', fov=14)
        cam_walkin = LookAtCamera(root=self, name='cam_walkin', fov=20)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=18)
        # cam_darcy = LookAtCamera(root=self, name='cam_darcy', fov=22)
        cam_hassler = LookAtCamera(root=self, name='cam_hassler', fov=18)

        # cam_dbg.move_cam(group=MAIN, index=2, duration=10, smooth=False)
        # cam_dbg.move_focus(group=MAIN, index=2, duration=10, time_delay=2)

        # CHARACTERS

        darcy = Character(root=self, actor=actors.Darcy, light_group=0, init_point='darcy_bottom', rotate=-90,
                          floor_height=down_floor_height)
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='trent_bottom', rotate=-90,
                          floor_height=down_floor_height)

        darcy.motion(group=MAIN, duration=13, loop=True, anim=Female.Sc_FMBODY_STND_HOLD_ARMS_CROSSED_000LV_XA_03)
        trent.motion(group=MAIN, duration=13, loop=True, anim=Male.Sc_MLBODY_STND_FSTHIPB_HOLD_000LV_XA_02)

        hassler = Character(root=self, actor=actors.HasslerOrder, light_group=0, init_point='hassler_init', rotate=90)
        hassler.idle(group=MAIN)

        # not used
        # chair4 = Character(root=self, actor=actors.YokohamaBarFour, light_group=0, init_point='chair_four', rotate=90)
        # chair4.motion(group=MAIN, duration=15, loop=True, anim=Female.Sc_FMBODY_CHRF_IDLE_000LV_XA_05)

        chair1 = Character(root=self, actor=actors.YokohamaBarOne, light_group=0, init_point='chair_one', rotate=-90)
        chair2 = Character(root=self, actor=actors.YokohamaBarTwo, light_group=0, init_point='chair_two', rotate=90)
        chair3 = Character(root=self, actor=actors.YokohamaBarThree, light_group=0, init_point='chair_five', rotate=90)
        chair5 = Character(root=self, actor=actors.YokohamaBarFive, light_group=0, init_point='chair_three', rotate=-90)

        chair1.motion(group=MAIN, duration=15, loop=True, anim=Male.Sc_MLBODY_CHRB_LSTN_000LV_A_19, start_time=4)
        chair2.motion(group=MAIN, duration=15, loop=True, anim=Male.Sc_MLBODY_CHRB_TALK_000UP_A_17, start_time=3)
        chair3.motion(group=MAIN, duration=15, loop=True, anim=Female.Sc_FMBODY_CHRF_IDLE_000LV_XA_05)
        chair5.motion(group=MAIN, duration=15, loop=True, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06)

        FloorHeightEvent(root=self, group=MAIN,
                         char_name=trent.name,
                         floor_height=0,
                         duration=10,
                         smooth=True,
                         time_delay=1)

        FloorHeightEvent(root=self, group=MAIN,
                         char_name=darcy.name,
                         floor_height=0,
                         duration=10,
                         smooth=True,
                         time_delay=1)

        cam_lift.set(group=MAIN)
        cam_lift.move_focus(group=MAIN, index=2, duration=10)
        cam_liftback.set(group=MAIN, time_delay=12, time_append=12)

        chair1.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_CHRB_TWSTS_LOOK_090LV_XA_02, time_scale=0.8)
        chair2.motion(group=MAIN, duration=7, anim=Male.Sc_MLBODY_CHRB_TWSTU_CCL_LESS_000LV_A_14, time_scale=0.5)
        chair3.motion(group=MAIN, duration=15, anim=Female.Sc_FMBODY_CHRF_CHRB_TRNS_000LV_XA_02, time_scale=0.6)
        chair5.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_CHRF_TWSTS_LOOK_090LV_XA_02, time_scale=0.7)

        RotateAxisEvent(root=self, group=MAIN, object_name=chair5.name, angle=-35, duration=6, smooth=True)
        RotateAxisEvent(root=self, group=MAIN, object_name=chair3.name, angle=15, duration=4, smooth=True)
        NeckIkEvent(root=self, group=MAIN, char_name=chair3.name, target_name=self.get_automarker_name('intro_trent_lift'),
                duration=10, transition_duration=4)

        NeckIkEvent(root=self, group=MAIN, char_name=chair5.name, target_name=self.get_automarker_name('intro_trent_lift'),
                duration=10, transition_duration=4, time_delay=2)

        main_group.append_time(6)

        # self.set_start_time(main_group.get_time())

        MoveFastEvent(root=self, group=MAIN, object_name=trent.name, target_name=self.get_automarker_name('trent_go'),
                      adjust_pos=True)
        MoveFastEvent(root=self, group=MAIN, object_name=darcy.name, target_name=self.get_automarker_name('darcy_go'),
                      adjust_pos=True)

        trent.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, time_scale=0.5, start_time=1)
        darcy.motion(group=MAIN, duration=20, loop=True, anim=Female.Sc_FMBODY_WLKG_000LV_XA_01, time_scale=0.5)

        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=-3, duration=5, smooth=False)

        cam_go.set(group=MAIN)
        # cam_dbg.set(group=MAIN)
        # cam_goend.set(group=MAIN, time_delay=0.1)

        cam_go.move_cam(group=MAIN, index=2, duration=9, smooth=False)
        cam_go.move_focus(group=MAIN, index=2, duration=9, smooth=False)

        main_group.append_time(0.2)

        trent.facial(group=MAIN, index=10)
        darcy.facial(group=MAIN, index=20)

        cam_goend.set(group=MAIN)

        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, time_scale=0.5)
        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, time_scale=0.8, time_delay=5)

        trent.facial(group=MAIN, index=30)

        self.set_start_time(main_group.get_time())

        cam_walkin.set(group=MAIN)

        MoveFastEvent(root=self, group=MAIN, object_name=trent.name, target_name=self.get_automarker_name('trent_goend'),
                      adjust_pos=True)
        MoveFastEvent(root=self, group=MAIN, object_name=darcy.name, target_name=self.get_automarker_name('darcy_goend'),
                      adjust_pos=True)
        MoveFastEvent(root=self, group=MAIN, object_name=hassler.name, target_name=self.get_automarker_name('hassler_walkin'),
                      adjust_pos=True)

        trent.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_FSTHIPB_HOLD_000LV_XA_02, time_scale=1)
        darcy.motion(group=MAIN, duration=13, loop=True, anim=Female.Sc_FMBODY_STND_HOLD_ARMS_CROSSED_000LV_XA_03)
        hassler.idle(group=MAIN)

        hassler.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, time_scale=0.8, time_delay=1)
        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_TURN_270LV_XA_04, time_scale=1, time_delay=2, trans_time=1)
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=-30, duration=3, smooth=True, time_delay=3)

        Char2CharNeckIkEvent(root=self, group=MAIN, char_name=darcy.name, target_name=hassler.name,
                             duration=10, transition_duration=1, time_delay=2)

        darcy.facial(group=MAIN, index=40)
        hassler.facial(group=MAIN, index=50)

        cam_trent.set(group=MAIN)
        # cam_dbg.set(group=MAIN)
        trent.facial(group=MAIN, index=60)

        # self.set_start_time(main_group.get_time())

        MoveFastEvent(root=self, group=MAIN, object_name=hassler.name, target_name=self.get_automarker_name('hassler_talk'),
                      adjust_pos=True)
        hassler.idle(group=MAIN)

        cam_hassler.set(group=MAIN)
        hassler.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, time_scale=0.5, time_delay=2, trans_time=0.25)
        hassler.facial(group=MAIN, index=70)
        hassler.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, time_scale=0.5, time_delay=2, trans_time=0.25)
        hassler.facial(group=MAIN, index=80, extra_delay=0)

        cam_trent.set(group=MAIN, time_delay=0.5, time_append=0.5)

        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, time_scale=1, trans_time=0.25)
        trent.facial(group=MAIN, index=90)





        # self.set_start_time(main_group.get_time())
        #
        # MoveFastEvent(root=self, group=MAIN, object_name=hassler.name, target_name=self.get_automarker_name('hassler_talk'),
        #               adjust_pos=True)
        # hassler.idle(group=MAIN)
        #


        cam_hassler.set(group=MAIN, time_delay=1, time_append=1)
        hassler.facial(group=MAIN, index=100)
        hassler.facial(group=MAIN, index=110, extra_delay=0)

        # cam_trent.set(group=MAIN)
        # trent.facial(group=MAIN, index=120)
        #
        # cam_hassler.set(group=MAIN)
        # hassler.facial(group=MAIN, index=130)
        #


        main_group.append_time(20)

        #


