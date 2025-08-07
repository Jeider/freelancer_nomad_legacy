from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import Male, Female

from story import actors


class Msn10FinalCutsceneThorn(Scene):
    POINT_ROTATE_OVERRIDES = {
        'trent_talk': (0, 180, 0),
    }

    def action(self):
        main_group = self.get_group(MAIN)

        # CAMERAS

        cam_dbg = LookAtCamera(root=self, name='cam_dbg', fov=30)
        cam_start = LookAtCamera(root=self, name='cam_start', fov=30)

        cam_alaric = LookAtCamera(root=self, name='cam_alaric', fov=19)
        cam_trent_walkin = LookAtCamera(root=self, name='cam_trent_walkin', fov=22)

        cam_second = LookAtCamera(root=self, name='cam_second', fov=30)
        cam_junko = LookAtCamera(root=self, name='cam_junko', fov=17)
        cam_edison = LookAtCamera(root=self, name='cam_edison', fov=17)

        # PROPS

        lt_room = Light(root=self, name='ROOMA', point_name='trent_light', light_group=0, diffuse=[0.3, 0.35, 0.3],
                        ambient=[0, 0, 0], direction=[0, 0, -1], light_type=L_POINT, range=30)
        lt_room2 = Light(root=self, name='ROOMA1', point_name='alaric_light', light_group=0, diffuse=[0.45, 0.35, 0.35],
                        ambient=[0, 0, 0], direction=[0, 0, 1], light_type=L_POINT, range=30)

        # CHARACTERS

        alaric = Character(root=self, actor=actors.Alaric, light_group=0, init_point='alaric_talk', rotate_y=0)
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='trent_init', rotate_y=180)

        edison = Character(root=self, actor=actors.EdisonTrent, light_group=0, init_point='edison_talk', rotate_y=-45)
        junko = Character(root=self, actor=actors.Juni, light_group=0, init_point='junko_talk', rotate_y=-135)

        # MARKERS

        mrk_trent_init = trent.get_stand_marker('trent_init')
        mrk_trent_talk = trent.get_stand_marker('trent_talk')
        mrk_alaric_talk = alaric.get_sit_marker('alaric_talk')
        mrk_edison_talk = edison.get_sit_marker('edison_talk')
        mrk_junko_talk = junko.get_sit_marker('junko_talk')
        #
        mrk_alaric_head_top = self.get_automarker_name('alaric_head_top')
        mrk_alaric_look_front = self.get_automarker_name('alaric_look_front')
        mrk_alaric_look_side = self.get_automarker_name('alaric_look_side')
        mrk_trent_look_front = self.get_automarker_name('trent_look_front')
        mrk_trent_look_side = self.get_automarker_name('trent_look_side')
        mrk_edison_front = self.get_automarker_name('edison_front')
        mrk_junko_front = self.get_automarker_name('junko_front')
        mrk_edison_look_out = self.get_automarker_name('edison_look_out')

        # EXTRA DEFINITIONS

        trent.move_head_ik(group=BG, target_name=mrk_alaric_head_top, immediately=True)
        trent.move_eye_ik(group=BG, target_name=mrk_alaric_talk, immediately=True)
        alaric.move_head_ik(group=BG, target_name=mrk_trent_init, immediately=True)
        alaric.move_eye_ik(group=BG, target_name=mrk_trent_init, immediately=True)
        edison.move_head_ik(group=BG, target_name=mrk_junko_front, immediately=True)
        edison.move_eye_ik(group=BG, target_name=mrk_junko_talk, immediately=True)
        junko.move_head_ik(group=BG, target_name=mrk_edison_front, immediately=True)
        junko.move_eye_ik(group=BG, target_name=mrk_edison_talk, immediately=True)

        alaric.start_head_ik(group=MAIN, duration=1000)
        alaric.start_eye_ik(group=MAIN, duration=1000)
        trent_head_ik = trent.start_head_ik(group=MAIN, duration=1000)
        trent_eye_ik = trent.start_eye_ik(group=MAIN, duration=1000)

        # BEGIN TRENT-ALARIC SECTION

        alaric.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, time_scale=1)
        alaric.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, time_scale=0.6, time_delay=2, trans_time=0.5)
        alaric.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, time_scale=0.8, time_delay=6)
        trent.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, time_scale=0.8, time_delay=2.5)

        alaric.move_head_ik(group=MAIN, target_name=mrk_trent_talk, duration=6, time_delay=3)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=6, time_delay=3)

        cam_start.set(group=MAIN)

        cam_start.move_cam(group=MAIN, index=2, duration=7, smooth=True)
        cam_start.move_focus(group=MAIN, index=2, duration=7, smooth=True)

        main_group.append_time(9)

        cam_trent_walkin.set(group=MAIN)

        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, start_time=0.9, time_scale=0.8)
        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, time_scale=0.7, time_delay=2, trans_time=1)

        main_group.append_time(0.25)
        trent.facial(group=MAIN, index=10)

        cam_alaric.set(group=MAIN)

        alaric.move_head_ik(group=MAIN, target_name=mrk_alaric_look_front, duration=2, time_delay=2)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_alaric_look_side, duration=0.7, time_delay=2)

        alaric.facial(group=MAIN, index=20)

        cam_trent_walkin.set(group=MAIN)

        trent.facial(group=MAIN, index=30)

        cam_alaric.set(group=MAIN)

        alaric.move_head_ik(group=MAIN, target_name=mrk_trent_talk, duration=2.5, time_delay=1)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=1.5, time_delay=1)

        alaric.move_head_ik(group=MAIN, target_name=mrk_alaric_look_front, duration=2, time_delay=10)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_alaric_look_side, duration=0.7, time_delay=10)

        alaric.move_head_ik(group=MAIN, target_name=mrk_trent_talk, duration=2.5, time_delay=12)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=1.5, time_delay=12)

        alaric.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRB_CONV_RHNDUP_TRNS_000LV_XA_02, time_scale=0.6, trans_time=0.5, time_delay=3)
        alaric.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRB_CONV_RHND_CASL_000LV_xa_04, time_scale=0.6, trans_time=1, time_delay=5)
        alaric.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRB_CONV_RHNDDN_TRNS_000LV_XA_02, time_scale=0.6, trans_time=0.5, time_delay=9)

        alaric.facial(group=MAIN, index=40)
        alaric.facial(group=MAIN, index=50)

        cam_trent_walkin.set(group=MAIN)
        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, time_scale=0.7, trans_time=1, time_delay=2)

        trent.facial(group=MAIN, index=60)

        cam_alaric.set(group=MAIN)

        alaric.facial(group=MAIN, index=70)

        cam_trent_walkin.set(group=MAIN)

        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_GESTR_180LV_XA_02, time_scale=0.5, trans_time=1)

        trent.facial(group=MAIN, index=80)

        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, time_scale=0.7, trans_time=1, time_delay=-1)

        trent.move_head_ik(group=MAIN, target_name=mrk_trent_look_front, duration=2, time_delay=5)
        trent.move_eye_ik(group=MAIN, target_name=mrk_trent_look_side, duration=0.7, time_delay=5)

        trent.move_head_ik(group=MAIN, target_name=mrk_alaric_head_top, duration=2.5, time_delay=7)
        trent.move_eye_ik(group=MAIN, target_name=mrk_alaric_talk, duration=1.5, time_delay=7)

        trent.facial(group=MAIN, index=90)

        cam_alaric.set(group=MAIN)
        alaric.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_CHRB_GESTR_NO_000LV_XA_03, time_scale=0.5, trans_time=1)

        alaric.facial(group=MAIN, index=100)

        alaric.motion(group=MAIN, duration=40, loop=True, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, time_scale=0.5, trans_time=1, time_delay=-2)
        alaric.move_head_ik(group=MAIN, target_name=mrk_alaric_look_front, duration=2, time_delay=0)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_alaric_look_side, duration=1.3, time_delay=0)

        alaric.facial(group=MAIN, index=105)

        cam_trent_walkin.set(group=MAIN)
        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, time_scale=0.4, time_delay=1)

        trent.facial(group=MAIN, index=110)

        cam_alaric.set(group=MAIN)
        alaric.move_head_ik(group=MAIN, target_name=mrk_trent_talk, duration=1.3, time_delay=0)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.5, time_delay=0)

        alaric.facial(group=MAIN, index=120)

        main_group.append_time(0.5)

        cam_trent_walkin.set(group=MAIN)
        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, time_scale=0.7, trans_time=1)

        trent.facial(group=MAIN, index=130)

        alaric.move_head_ik(group=MAIN, target_name=mrk_alaric_look_front, duration=2, time_delay=1)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_alaric_look_side, duration=1.3, time_delay=1)


        trent.move_head_ik(group=MAIN, target_name=mrk_trent_look_front, duration=1.6, time_delay=-0.5)
        trent.move_eye_ik(group=MAIN, target_name=mrk_trent_look_side, duration=0.7, time_delay=-0.5)

        trent.move_head_ik(group=MAIN, target_name=mrk_alaric_head_top, duration=2.5, time_delay=2)
        trent.move_eye_ik(group=MAIN, target_name=mrk_alaric_talk, duration=1.5, time_delay=2)

        trent.facial(group=MAIN, index=140)


        # END TRENT-ALARIC SECTION


        # MoveFastEvent(root=self, group=MAIN, object_name=trent.name, target_name=self.get_automarker_name('trent_talk'))

        trent_head_ik.set_duration(main_group.get_time())
        trent_eye_ik.set_duration(main_group.get_time())

        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, time_scale=0.7)
        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_WALK_TRNS_180LV_XA_02, time_scale=0.73, time_delay=2)
        trent.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, time_scale=0.73, time_delay=5.6)

        edison.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRF_LOOK_270LV_XA_01, time_scale=1)
        junko.motion(group=MAIN, duration=100, loop=True, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, time_scale=1)

        main_group.append_time(0.5)

        lt_room.turn_off(group=MAIN)
        lt_room2.turn_off(group=MAIN)

        cam_edison.set(group=MAIN)


        cam_second.set(group=MAIN)

        cam_second.move_cam(group=MAIN, index=2, duration=12, smooth=True)
        cam_second.move_focus(group=MAIN, index=2, duration=12, smooth=True)

        main_group.append_time(9)

        junko.start_head_ik(group=MAIN, duration=1000)
        junko.start_eye_ik(group=MAIN, duration=1000)

        edison.start_head_ik(group=MAIN, duration=1000, time_delay=2)
        edison.start_eye_ik(group=MAIN, duration=1000, time_delay=2)

        edison.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_TWSTS_FROM_270LV_XA_02, time_scale=1, time_delay=0)

        edison.facial(group=MAIN, index=200)


        cam_junko.set(group=MAIN)

        junko.facial(group=MAIN, index=210)


        cam_edison.set(group=MAIN)


        edison.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, time_scale=0.7, time_delay=2)

        edison.facial(group=MAIN, index=220)


        cam_junko.set(group=MAIN)


        junko.motion(group=MAIN, duration=100, loop=True, anim=Female.Sc_FMBODY_CHRB_CONV_LHND_CASL_000LV_xa_03, time_scale=0.6, trans_time=1, time_delay=0)
        junko.motion(group=MAIN, duration=100, anim=Female.Sc_FMBODY_CHRB_CONV_LHNDDN_TRNS_000LV_XA_01, time_scale=0.6, trans_time=0.5, time_delay=2)

        junko.facial(group=MAIN, index=230)

        main_group.append_time(0.25)



        edison.start_head_ik(group=MAIN, duration=1000, time_delay=0)
        edison.start_eye_ik(group=MAIN, duration=1000, time_delay=0)

        cam_edison.set(group=MAIN)

        edison.move_head_ik(group=MAIN, target_name=mrk_edison_look_out, duration=2, time_delay=3)
        edison.move_eye_ik(group=MAIN, target_name=mrk_edison_look_out, duration=0.7, time_delay=3)

        edison.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, time_scale=1, time_delay=1)
        # edison.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_CHRF_TWSTS_LOOK_270LV_XA_02, trans_time=1, time_scale=0.8, time_delay=2)

        edison.facial(group=MAIN, index=240)

        main_group.append_time(1)
