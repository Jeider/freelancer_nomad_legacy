from story.cutscenes.scene import Scene
from story.cutscenes.content import BG, MAIN, Character, LookAtCamera, MoveEvent, FloorHeightEvent
from story.cutscenes.anim import Male, Female

from story import actors


class Msn9YokohamaCutsceneThorn(Scene):

    def action(self):
        down_floor_height = self.get_point('floor_bottom').position[1]

        # CAMERAS

        cam_dbg = LookAtCamera(root=self, name='cam_dbg', fov=25)
        cam_lift = LookAtCamera(root=self, name='cam_lift', fov=22)
        cam_liftback = LookAtCamera(root=self, name='cam_liftback', fov=20)
        # cam_trent = LookAtCamera(root=self, name='cam_trent', fov=22)
        # cam_darcy = LookAtCamera(root=self, name='cam_darcy', fov=22)
        # cam_hassler = LookAtCamera(root=self, name='cam_hassler', fov=22)

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
        chair2.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_CHRB_TWSTU_CCL_LESS_000LV_A_14, time_scale=0.7)
        chair3.motion(group=MAIN, duration=15, anim=Female.Sc_FMBODY_CHRB_CHRF_TRNS_000LV_XA_02, time_scale=0.6)
        chair5.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_CHRF_TWSTS_LOOK_090LV_XA_02, time_scale=0.7)


        # cam_trent.set(group=MAIN, time_delay=2, time_append=2)
        # trent.facial(group=MAIN, index=10)
        #
        # cam_darcy.set(group=MAIN)
        # darcy.facial(group=MAIN, index=20)
        #
        # cam_trent.set(group=MAIN)
        # trent.facial(group=MAIN, index=30)
        #
        # cam_darcy.set(group=MAIN)
        # darcy.facial(group=MAIN, index=40)
        #
        # cam_hassler.set(group=MAIN)
        # hassler.facial(group=MAIN, index=50)
        #
        # cam_trent.set(group=MAIN)
        # trent.facial(group=MAIN, index=60)
        #
        # cam_hassler.set(group=MAIN)
        # hassler.facial(group=MAIN, index=70)
        # hassler.facial(group=MAIN, index=80, extra_delay=0)
        #
        # cam_trent.set(group=MAIN)
        # trent.facial(group=MAIN, index=90)
        #
        # cam_hassler.set(group=MAIN)
        # hassler.facial(group=MAIN, index=100)
        # hassler.facial(group=MAIN, index=110, extra_delay=0)
        #
        # cam_trent.set(group=MAIN)
        # trent.facial(group=MAIN, index=120)
        #
        # cam_hassler.set(group=MAIN)
        # hassler.facial(group=MAIN, index=130)
        #
        #


