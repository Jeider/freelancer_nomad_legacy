from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import Male, Female

from story import actors


OVERRIDES = {
    'trent_talk': (0, 135, 0),
    'trent_near_table': (0, 115, 0),
    'darcy_talk': (0, 45, 0),
    'darcy_near_table': (0, 55, 0),
}


class Msn10OfferCutsceneThorn(Scene):
    POINT_ROTATE_OVERRIDES = OVERRIDES

    def action(self):
        main_group = self.get_group(MAIN)

        # CAMERAS

        cam_dbg = LookAtCamera(root=self, name='cam_dbg', fov=30)
        cam_start = LookAtCamera(root=self, name='cam_start', fov=30)

        cam_scene = LookAtCamera(root=self, name='cam_scene', fov=28)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=18)
        cam_trent_two = LookAtCamera(root=self, name='cam_trent_two', fov=18)
        cam_hassler = LookAtCamera(root=self, name='cam_hassler', fov=18)
        cam_hassler_alone = LookAtCamera(root=self, name='cam_hassler_alone', fov=16)
        cam_darcy = LookAtCamera(root=self, name='cam_darcy', fov=22)

        # PROPS

        # CHARACTERS

        darcy = Character(root=self, actor=actors.Darcy, light_group=0, init_point='darcy_init', rotate_y=180)
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='trent_init', rotate_y=180)
        hassler = Character(root=self, actor=actors.HasslerOrder, light_group=0, init_point='hassler_talk', rotate_y=-45)

        # MARKERS

        mrk_darcy_talk = darcy.get_sit_marker('darcy_talk')
        mrk_trent_talk = trent.get_sit_marker('trent_talk')
        mrk_hassler_talk = darcy.get_sit_marker('hassler_talk')

        mrk_trent_front = self.get_automarker_name('trent_front')
        mrk_hassler_front = self.get_automarker_name('hassler_front')
        mrk_hassler_front2 = self.get_automarker_name('hassler_front2')
        mrk_darcy_front = self.get_automarker_name('darcy_front')
        mrk_trent_begin_sit = self.get_automarker_name('trent_begin_sit')
        mrk_darcy_begin_sit = self.get_automarker_name('darcy_begin_sit')
        mrk_trent_look_side = self.get_automarker_name('trent_look_side')
        mrk_walking = self.get_automarker_name('mrk_walking')



        # EXTRA DEFINITIONS

        darcy.move_head_ik(group=BG, target_name=mrk_hassler_talk, immediately=True)
        darcy.move_eye_ik(group=BG, target_name=mrk_hassler_talk, immediately=True)
        trent.move_head_ik(group=BG, target_name=mrk_hassler_talk, immediately=True)
        trent.move_eye_ik(group=BG, target_name=mrk_hassler_talk, immediately=True)
        hassler.move_head_ik(group=BG, target_name=mrk_walking, immediately=True)
        hassler.move_eye_ik(group=BG, target_name=mrk_walking, immediately=True)

        hassler.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, time_scale=1)


        cam_start.set(group=MAIN)

        trent.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, time_scale=0.8)
        darcy.motion(group=MAIN, duration=10, loop=True, anim=Female.Sc_FMBODY_WLKG_000LV_XA_01, time_scale=0.75)

        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=-5, duration=6, smooth=False)

        RotateAxisEvent(root=self, group=MAIN, object_name=darcy.name, angle=35, duration=3, smooth=False, time_delay=6)
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=35, duration=4, smooth=False, time_delay=6)


        cam_start.move_cam(group=MAIN, index=2, duration=8, smooth=True)
        cam_start.move_focus(group=MAIN, index=2, duration=8, smooth=True)

        main_group.append_time(10)

        darcy.start_head_ik(group=BG, duration=1000)
        darcy.start_eye_ik(group=BG, duration=1000)
        hassler.start_head_ik(group=BG, duration=1000)
        hassler.start_eye_ik(group=BG, duration=1000)
        trent.start_head_ik(group=BG, duration=1000)
        trent.start_eye_ik(group=BG, duration=1000)

        MoveFastEvent(root=self, group=MAIN, object_name=trent.name, target_name=self.get_automarker_name('trent_near_table'))
        trent.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_STND_SITCR_TRNS_180DN_XA_06, time_scale=1, start_time=2)


        MoveFastEvent(root=self, group=MAIN, object_name=darcy.name, target_name=self.get_automarker_name('darcy_near_table'))
        darcy.motion(group=MAIN, duration=100, anim=Female.Sc_FMBODY_STND_SITCL_TRNS_180DN_XA_07, time_scale=1.3, time_delay=0)

        trent.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, time_scale=1, time_delay=3, trans_time=1)
        darcy.motion(group=MAIN, duration=100, loop=True, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, time_scale=1, time_delay=4, trans_time=1)



        darcy.move_head_ik(group=MAIN, target_name=mrk_hassler_front2, immediately=True)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_hassler_front2, immediately=True)
        trent.move_head_ik(group=MAIN, target_name=mrk_hassler_talk, immediately=True)
        trent.move_eye_ik(group=MAIN, target_name=mrk_hassler_talk, immediately=True)

        hassler.move_head_ik(group=MAIN, target_name=mrk_trent_begin_sit, duration=2.5, time_delay=-2)
        hassler.move_eye_ik(group=MAIN, target_name=mrk_trent_begin_sit, duration=1, time_delay=-2)

        cam_hassler_alone.set(group=MAIN)

        hassler.move_head_ik(group=MAIN, target_name=mrk_darcy_front, duration=2.5)
        hassler.move_eye_ik(group=MAIN, target_name=mrk_darcy_talk, duration=2)

        hassler.facial(group=MAIN, index=10)

        cam_darcy.set(group=MAIN)

        main_group.append_time(0.4)

        darcy.facial(group=MAIN, index=20)

        cam_hassler_alone.set(group=MAIN)

        hassler.facial(group=MAIN, index=30)

        cam_darcy.set(group=MAIN)

        darcy.move_head_ik(group=MAIN, target_name=mrk_hassler_front, duration=1.2)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_hassler_talk, duration=0.4)

        darcy.facial(group=MAIN, index=40)

        # cam_trent.set(group=MAIN)
        darcy.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=3, time_delay=1)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=1.3, time_delay=1)

        trent.move_head_ik(group=MAIN, target_name=mrk_darcy_front, duration=2.5)
        trent.move_eye_ik(group=MAIN, target_name=mrk_darcy_talk, duration=1.3)
        trent.move_head_ik(group=MAIN, target_name=mrk_hassler_front, duration=1.8, time_delay=3.5)
        trent.move_eye_ik(group=MAIN, target_name=mrk_hassler_front, duration=0.8, time_delay=3.5)

        trent.facial(group=MAIN, index=50)
        #
        # darcy.move_head_ik(group=MAIN, target_name=mrk_hassler_front, duration=2.5, time_delay=-1)
        # darcy.move_eye_ik(group=MAIN, target_name=mrk_hassler_talk, duration=1, time_delay=-1)

        cam_hassler.set(group=MAIN)

        MoveFastEvent(root=self, group=MAIN, object_name=darcy.name, target_name=self.get_automarker_name('darcy_talk'))
        MoveFastEvent(root=self, group=MAIN, object_name=trent.name, target_name=self.get_automarker_name('trent_talk'))

        trent.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, time_scale=1)
        darcy.motion(group=MAIN, duration=100, loop=True, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, time_scale=1)

        hassler.move_head_ik(group=MAIN, target_name=mrk_trent_talk, duration=1.5)
        hassler.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.5)

        hassler.move_head_ik(group=MAIN, target_name=mrk_darcy_front, duration=2.5, time_delay=6)
        hassler.move_eye_ik(group=MAIN, target_name=mrk_darcy_talk, duration=1, time_delay=6)

        hassler.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, time_scale=1, trans_time=0.5, time_delay=2)
        hassler.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, time_scale=1, trans_time=0.5, time_delay=5)

        hassler.facial(group=MAIN, index=60)

        cam_trent.set(group=MAIN)
        trent.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRB_SHRG_SHLDRS_BIG_000LV_XA_03, time_scale=0.8, trans_time=0.5, time_delay=0)
        trent.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, time_scale=1, trans_time=0.5, time_delay=3.7)

        trent.facial(group=MAIN, index=70)

        cam_hassler.set(group=MAIN)

        hassler.move_head_ik(group=MAIN, target_name=mrk_trent_talk, duration=1.5)
        hassler.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.5)

        hassler.facial(group=MAIN, index=80)

        cam_trent.set(group=MAIN)
        trent.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, time_scale=1, trans_time=0.5)

        trent.facial(group=MAIN, index=90)

        cam_hassler.set(group=MAIN)

        hassler.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDUP_TRNS_000LV_XA_02, time_scale=0.6, trans_time=0.5, time_delay=0)
        hassler.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRF_CONV_RHND_CASL_000LV_XA_04, time_scale=0.6, trans_time=1, time_delay=2)
        hassler.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDDN_TRNS_000LV_XA_02, time_scale=0.6, trans_time=0.5, time_delay=6)

        hassler.facial(group=MAIN, index=100)

        cam_trent.set(group=MAIN)
        trent.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, time_scale=1, trans_time=0.5)

        trent.facial(group=MAIN, index=110)

        cam_hassler.set(group=MAIN)

        hassler.facial(group=MAIN, index=120)


        cam_trent.set(group=MAIN)

        trent.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, time_scale=1, trans_time=0.5)
        trent.facial(group=MAIN, index=130)


        cam_hassler.set(group=MAIN)
        hassler.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, time_scale=0.6, trans_time=0.5)

        hassler.facial(group=MAIN, index=140)

        cam_trent.set(group=MAIN)
        trent.motion(group=MAIN, duration=4, anim=Male.Sc_MLBODY_CHRF_LSTN_000UP_B_15, time_scale=0.5, start_time=2, trans_time=2)

        trent.facial(group=MAIN, index=150)

        cam_hassler.set(group=MAIN)

        hassler.facial(group=MAIN, index=160)

        cam_trent.set(group=MAIN)
        trent.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, time_scale=1, trans_time=2)
        trent.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, time_scale=0.6, trans_time=0.5, time_delay=4)

        trent.facial(group=MAIN, index=170)

        cam_hassler.set(group=MAIN)

        hassler.facial(group=MAIN, index=180)

        cam_trent_two.set(group=MAIN)
        trent.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, time_scale=0.8)

        trent.move_head_ik(group=MAIN, target_name=mrk_trent_look_side, duration=3, time_delay=2.5)
        trent.move_eye_ik(group=MAIN, target_name=mrk_trent_look_side, duration=0.5, time_delay=2.5)

        trent.facial(group=MAIN, index=190)

        main_group.append_time(0.3)

        trent.move_head_ik(group=MAIN, target_name=mrk_hassler_talk, duration=1.6)
        trent.move_eye_ik(group=MAIN, target_name=mrk_hassler_talk, duration=0.5)

        trent.facial(group=MAIN, index=200)



        # main_group.append_time(0.1)
        # hassler.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, time_scale=1, time_delay=0.1)
        # main_group.append_time(0.1)


        hassler.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, time_scale=1)
        trent.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRB_IDLE_BIG_000LV_XA_05, time_scale=0.5)
        darcy.motion(group=MAIN, duration=100, loop=True, anim=Female.Sc_FMBODY_CHRB_IDLE_BIG_000LV_XA_05, time_scale=0.5)
        darcy.motion(group=MAIN, duration=100, anim=Female.Sc_FMBODY_CHRB_CHRF_TRNS_000LV_XA_02, time_scale=0.4, time_delay=5, trans_time=1)
        darcy.motion(group=MAIN, duration=100, anim=Female.Sc_FMBODY_CHRF_CHRB_TRNS_000LV_XA_02, time_scale=0.4, time_delay=15)


        darcy.move_head_ik(group=MAIN, target_name=mrk_hassler_front, duration=1.2)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_hassler_talk, duration=0.4)

        darcy.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=2, time_delay=17)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.7, time_delay=17)

        darcy.move_head_ik(group=MAIN, target_name=mrk_hassler_front, duration=1.6, time_delay=21)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_hassler_talk, duration=0.7, time_delay=21)


        hassler.move_head_ik(group=MAIN, target_name=mrk_darcy_front, duration=1.6, time_delay=11)
        hassler.move_eye_ik(group=MAIN, target_name=mrk_darcy_talk, duration=0.5, time_delay=11)

        hassler.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=1.5, time_delay=14)
        hassler.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.5, time_delay=14)

        trent.move_head_ik(group=MAIN, target_name=mrk_darcy_front, duration=2, time_delay=18)
        trent.move_eye_ik(group=MAIN, target_name=mrk_darcy_talk, duration=0.7, time_delay=18)

        trent.move_head_ik(group=MAIN, target_name=mrk_hassler_front, duration=1.9, time_delay=22)
        trent.move_eye_ik(group=MAIN, target_name=mrk_hassler_talk, duration=0.7, time_delay=22)




        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_CHRF_LSTN_000UP_B_15, time_scale=0.5, start_time=5, trans_time=2, time_delay=3)
        trent.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRB_IDLE_BIG_000LV_XA_05, time_scale=0.5, trans_time=2, time_delay=8)

        cam_scene.set(group=MAIN)
        cam_scene.move_cam(group=MAIN, index=2, duration=33)
        cam_scene.move_focus(group=MAIN, index=2, duration=33)


        hassler.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, time_scale=1, trans_time=0.5)
        hassler.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDUP_TRNS_000LV_XA_02, time_scale=0.6, trans_time=0.5, time_delay=8)
        hassler.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRF_CONV_RHND_CASL_000LV_XA_04, time_scale=0.6, trans_time=1, time_delay=10)
        hassler.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDDN_TRNS_000LV_XA_02, time_scale=0.6, trans_time=0.5, time_delay=20)

        hassler.facial(group=MAIN, index=210)
        hassler.facial(group=MAIN, index=220)
        hassler.facial(group=MAIN, index=230)
        hassler.facial(group=MAIN, index=240)

        main_group.append_time(1)


class Msn10OfferDecisionThorn(Scene):
    POINT_ROTATE_OVERRIDES = OVERRIDES

    def action(self):
        main_group = self.get_group(MAIN)


        # CAMERAS

        cam_decision = LookAtCamera(root=self, name='cam_decision', fov=30)

        # PROPS

        # CHARACTERS

        darcy = Character(root=self, actor=actors.Darcy, light_group=0, init_point='darcy_talk', rotate_y=45)
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='trent_talk', rotate_y=135)
        hassler = Character(root=self, actor=actors.HasslerOrder, light_group=0, init_point='hassler_talk', rotate_y=-45)


        darcy.motion(group=MAIN, duration=100, loop=True, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, time_scale=1)
        trent.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, time_scale=1)
        hassler.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, time_scale=1)


        cam_decision.set(group=MAIN)
        main_group.append_time(1000)


class Msn10OfferAcceptThorn(Scene):
    POINT_ROTATE_OVERRIDES = OVERRIDES

    def action(self):
        main_group = self.get_group(MAIN)


        # CAMERAS

        cam_dbg = LookAtCamera(root=self, name='cam_dbg', fov=30)
        cam_start = LookAtCamera(root=self, name='cam_start', fov=30)

        cam_scene = LookAtCamera(root=self, name='cam_scene', fov=28)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=16)
        cam_trent_two = LookAtCamera(root=self, name='cam_trent_two', fov=16)
        cam_hassler = LookAtCamera(root=self, name='cam_hassler', fov=16)
        cam_hassler_alone = LookAtCamera(root=self, name='cam_hassler_alone', fov=16)
        cam_darcy = LookAtCamera(root=self, name='cam_darcy', fov=22)

        # PROPS

        # CHARACTERS

        darcy = Character(root=self, actor=actors.Darcy, light_group=0, init_point='darcy_talk', rotate_y=45)
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='trent_talk', rotate_y=135)
        hassler = Character(root=self, actor=actors.HasslerOrder, light_group=0, init_point='hassler_talk', rotate_y=-45)

        # MARKERS

        mrk_darcy_talk = darcy.get_sit_marker('darcy_talk')
        mrk_trent_talk = trent.get_sit_marker('trent_talk')
        mrk_hassler_talk = darcy.get_sit_marker('hassler_talk')

        mrk_trent_front = self.get_automarker_name('trent_front')
        mrk_hassler_front = self.get_automarker_name('hassler_front')
        mrk_hassler_front2 = self.get_automarker_name('hassler_front2')
        mrk_darcy_front = self.get_automarker_name('darcy_front')
        mrk_trent_begin_sit = self.get_automarker_name('trent_begin_sit')
        mrk_darcy_begin_sit = self.get_automarker_name('darcy_begin_sit')
        mrk_trent_look_side = self.get_automarker_name('trent_look_side')
        mrk_walking = self.get_automarker_name('mrk_walking')


        darcy.motion(group=MAIN, duration=100, loop=True, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, time_scale=1)
        trent.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, time_scale=1)
        hassler.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, time_scale=1)


        # EXTRA DEFINITIONS

        darcy.move_head_ik(group=BG, target_name=mrk_hassler_front2, immediately=True)
        darcy.move_eye_ik(group=BG, target_name=mrk_hassler_front, immediately=True)
        trent.move_head_ik(group=BG, target_name=mrk_hassler_front, immediately=True)
        trent.move_eye_ik(group=BG, target_name=mrk_hassler_talk, immediately=True)
        hassler.move_head_ik(group=BG, target_name=mrk_darcy_front, immediately=True)
        hassler.move_eye_ik(group=BG, target_name=mrk_darcy_talk, immediately=True)

        cam_darcy.set(group=MAIN)

        darcy.start_head_ik(group=BG, duration=1000)
        darcy.start_eye_ik(group=BG, duration=1000)
        hassler.start_head_ik(group=BG, duration=1000)
        hassler.start_eye_ik(group=BG, duration=1000)
        trent.start_head_ik(group=BG, duration=1000)
        trent.start_eye_ik(group=BG, duration=1000)

        main_group.append_time(1)

        darcy.move_head_ik(group=MAIN, target_name=mrk_hassler_front, duration=1.2)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_hassler_talk, duration=0.4)

        trent.facial(group=MAIN, index=250)

        trent.move_head_ik(group=MAIN, target_name=mrk_darcy_front, duration=2.4)
        trent.move_eye_ik(group=MAIN, target_name=mrk_darcy_talk, duration=0.8)

        darcy.facial(group=MAIN, index=260)

        cam_hassler.set(group=MAIN)
        hassler.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, time_scale=1)

        hassler.move_head_ik(group=MAIN, target_name=mrk_trent_talk, duration=2, time_delay=2)
        hassler.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.8, time_delay=2)

        hassler.facial(group=MAIN, index=270)

        main_group.append_time(1)
