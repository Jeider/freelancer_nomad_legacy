from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import Male, Female

from story import actors


class Msn11DrinkScene(Scene):
    POINT_ROTATE_OVERRIDES = {
        'trent_talk': (0, 180, 0),
    }

    def action(self):
        main_group = self.get_group(MAIN)

        # CAMERAS

        cam_dbg = LookAtCamera(root=self, name='cam_dbg', fov=30)
        cam_start = LookAtCamera(root=self, name='cam_start', fov=20)
        cam_kim = LookAtCamera(root=self, name='cam_kim', fov=20)

        # PROPS

        # CHARACTERS

        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='trent_init', rotate_y=60)
        kim = Character(root=self, actor=actors.Kim, light_group=0, init_point='kim_listen', rotate_y=0)

        # MARKERS

        mrk_trent_init = trent.get_stand_marker('trent_init')
        mrk_trent_angry = trent.get_stand_marker('trent_angry')
        mrk_kim_listen = kim.get_stand_marker('kim_listen')
        # mrk_edison_talk = edison.get_sit_marker('edison_talk')
        # mrk_junko_talk = junko.get_sit_marker('junko_talk')
        #
        mrk_kim_forward = self.get_automarker_name('mrk_kim_forward')
        mrk_kim_forward2 = self.get_automarker_name('mrk_kim_forward2')
        mrk_kim_table = self.get_automarker_name('mrk_kim_table')
        mrk_kim_table2 = self.get_automarker_name('mrk_kim_table2')
        mrk_kim_leave = self.get_automarker_name('mrk_kim_leave')
        mrk_kim_away = self.get_automarker_name('mrk_kim_away')
        mrk_kim_away_door = self.get_automarker_name('mrk_kim_away_door')
        # mrk_edison_front = self.get_automarker_name('edison_front')
        # mrk_junko_front = self.get_automarker_name('junko_front')
        # mrk_edison_look_out = self.get_automarker_name('edison_look_out')

        # EXTRA DEFINITIONS

        trent.move_head_ik(group=BG, target_name=mrk_kim_table, immediately=True)
        trent.move_eye_ik(group=BG, target_name=mrk_kim_table, immediately=True)
        kim.move_head_ik(group=BG, target_name=mrk_kim_forward2, immediately=True)
        kim.move_eye_ik(group=BG, target_name=mrk_kim_forward2, immediately=True)
        # edison.move_head_ik(group=BG, target_name=mrk_junko_front, immediately=True)
        # edison.move_eye_ik(group=BG, target_name=mrk_junko_talk, immediately=True)
        # junko.move_head_ik(group=BG, target_name=mrk_edison_front, immediately=True)
        # junko.move_eye_ik(group=BG, target_name=mrk_edison_talk, immediately=True)
        #
        kim.start_head_ik(group=MAIN, duration=1000)
        kim.start_eye_ik(group=MAIN, duration=1000)
        trent_head_ik = trent.start_head_ik(group=MAIN, duration=1000)
        trent_eye_ik = trent.start_eye_ik(group=MAIN, duration=1000)

        cam_start.set(group=MAIN)

        cam_start.move_cam(group=MAIN, index=2, duration=12, smooth=True)
        cam_start.move_focus(group=MAIN, index=2, duration=4, smooth=True)

        # MoveFastEvent(root=self, group=MAIN, object_name=trent.name, target_name=self.get_automarker_name('trent_angry'))

        # trent.motion(group=MAIN, duration=1, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)





        kim.motion(group=MAIN, duration=5, anim=Male.Sc_MLBODY_STND_LEAN_BAR_TRNS_000LV_XA_02, start_time=0.7, time_scale=0.6)

        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, start_time=0.3, time_scale=0.9)
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=10, duration=2, smooth=True)

        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, start_time=0, time_scale=0.9, trans_time=1, time_delay=2.3)
        kim.motion(group=MAIN, duration=5, anim=Male.Sc_MLBODY_LEAN_STND_BAR_TRNS_000LV_XA_03, trans_time=0.5, time_delay=2.5)
        kim.motion(group=MAIN, duration=5, anim=Male.Sc_MLBODY_STND_TURN_270LV_XA_04, trans_time=0.5, time_delay=4.2)
        kim.motion(group=MAIN, duration=15, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, trans_time=0.5, time_delay=8)
        RotateAxisEvent(root=self, group=MAIN, object_name=kim.name, angle=20, duration=2, smooth=True, time_delay=6)

        kim.move_head_ik(group=MAIN, target_name=mrk_kim_forward, duration=2.5, time_delay=0)
        kim.move_eye_ik(group=MAIN, target_name=mrk_kim_forward, duration=1.5, time_delay=0)
        kim.move_head_ik(group=MAIN, target_name=mrk_kim_forward2, duration=1.5, time_delay=2.2)
        kim.move_eye_ik(group=MAIN, target_name=mrk_kim_forward2, duration=1, time_delay=2)
        kim.move_head_ik(group=MAIN, target_name=mrk_trent_angry, duration=4, time_delay=4)
        kim.move_eye_ik(group=MAIN, target_name=mrk_trent_angry, duration=2.5, time_delay=3)

        trent.move_head_ik(group=MAIN, target_name=mrk_kim_table2, duration=2.5, time_delay=5)
        trent.move_eye_ik(group=MAIN, target_name=mrk_kim_table2, duration=1.5, time_delay=5)

        main_group.append_time(1)
        trent.facial(group=MAIN, index=10)

        trent.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_STND_CONV_HNDS_CASL_000LV_xa_04, time_scale=0.6, trans_time=2, time_delay=0)
        trent.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLHAND_HNEUT_GESTL_CASL_000LV_00, time_scale=0.6, trans_time=0.2, time_delay=0.5)
        trent.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00, time_scale=0.6, trans_time=0.2, time_delay=0.5)

        trent.facial(group=MAIN, index=20)
        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, start_time=0, time_scale=0.9, trans_time=1, time_delay=0)
        trent.motion(group=MAIN, duration=1, anim=Male.Sc_MLHAND_HNEUT_EDGE_LEFT_000LV_00, time_scale=0.6, trans_time=0.2, time_delay=0)
        trent.motion(group=MAIN, duration=1, anim=Male.Sc_MLHAND_HNEUT_EDGE_RGHT_000LV_00, time_scale=0.6, trans_time=0.2, time_delay=0)
        trent.facial(group=MAIN, index=30)





        ### DBG


        # kim.motion(group=MAIN, duration=5, anim=Male.Sc_MLBODY_STND_TURN_270LV_XA_04, time_scale=2,  time_delay=0)
        # RotateAxisEvent(root=self, group=MAIN, object_name=kim.name, angle=20, duration=1, smooth=True, time_delay=0)
        #
        # kim.move_head_ik(group=BG, target_name=mrk_trent_angry, immediately=True, time_delay=0.1)
        # kim.move_eye_ik(group=BG, target_name=mrk_trent_angry, immediately=True, time_delay=0.1)
        #
        #
        # main_group.append_time(2)


        ### DBG


        cam_kim.set(group=MAIN)


        trent.move_head_ik(group=MAIN, target_name=mrk_kim_listen, duration=2.5, time_delay=1)
        trent.move_eye_ik(group=MAIN, target_name=mrk_kim_listen, duration=1.5, time_delay=1)

        trent.move_head_ik(group=MAIN, target_name=mrk_kim_table2, duration=2.5, time_delay=4)
        trent.move_eye_ik(group=MAIN, target_name=mrk_kim_table2, duration=1.5, time_delay=4)

        trent.move_head_ik(group=MAIN, target_name=mrk_kim_away, duration=2.5, time_delay=7.5)
        trent.move_eye_ik(group=MAIN, target_name=mrk_kim_away, duration=1.5, time_delay=7.5)

        trent.motion(group=MAIN, duration=5, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, time_scale=0.4, time_delay=1)

        kim.motion(group=MAIN, duration=5, anim=Male.Sc_MLBODY_STND_GESTR_NO_000LV_XA_02, time_scale=0.9, trans_time=0.5, time_delay=0)


        kim.facial(group=MAIN, index=40)

        kim.motion(group=MAIN, duration=5, anim=Male.Sc_MLBODY_STND_GEST_HNDS_WAIT_000LV_XA_02, time_scale=0.8, trans_time=0.5, time_delay=0)

        kim.facial(group=MAIN, index=50)


        kim.move_head_ik(group=MAIN, target_name=mrk_kim_leave, duration=1.5, time_delay=-0.5)
        kim.move_eye_ik(group=MAIN, target_name=mrk_kim_leave, duration=0.7, time_delay=-0.5)

        kim.move_head_ik(group=MAIN, target_name=mrk_kim_away_door, duration=1.5, time_delay=1)
        kim.move_eye_ik(group=MAIN, target_name=mrk_kim_away_door, duration=0.7, time_delay=-1)



        RotateAxisEvent(root=self, group=MAIN, object_name=kim.name, angle=45, duration=0.5, smooth=True, time_delay=0)
        kim.motion(group=MAIN, duration=4, anim=Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01)
        kim.motion(group=MAIN, duration=500, loop=True, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, time_delay=1.07)
        RotateAxisEvent(root=self, group=MAIN, object_name=kim.name, angle=-75, duration=1, smooth=True, time_delay=1.1)

        cam_start.set(group=MAIN)

        trent.facial(group=MAIN, index=60)

        main_group.append_time(1000)
