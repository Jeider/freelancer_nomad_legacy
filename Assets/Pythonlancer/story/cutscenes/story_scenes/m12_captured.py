from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import Male, Female, Trent

from story import actors


class LiComm(Prop):
    COMPOUND_TEMPLATE_NAME = 'm12_li_comm'


class LiCommScreen(Prop):
    COMPOUND_TEMPLATE_NAME = 'm12_li_comm_screen'


class Msn12CapturedScene(Scene):
    POINT_ROTATE_OVERRIDES = {
        'li_comm': (0, 180, 0),
        'alaric_comm': (0, 90, 0),
    }

    def action(self):
        main_group = self.get_group(MAIN)
        mandrake_floor_height = self.get_point('mandrake_floor').position[1]

        # CAMERAS

        cam_dbg = LookAtCamera(root=self, name='cam_dbg', fov=30)
        cam_start = LookAtCamera(root=self, name='cam_start', fov=24)
        cam_hatcher = LookAtCamera(root=self, name='cam_hatcher', fov=18)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=18)
        cam_king = LookAtCamera(root=self, name='cam_king', fov=16)
        cam_comm = LookAtCamera(root=self, name='cam_comm', fov=22)
        cam_team = LookAtCamera(root=self, name='cam_team', fov=24)
        cam_insane = LookAtCamera(root=self, name='cam_insane', fov=18)


        # PROPS

        comm_light = 30
        king_light = 35

        Light(root=self, name='ROOMA', point_name='comm_light1', light_group=comm_light, diffuse=[0.6, 0.4, 0.5],
            ambient=[0, 0, 0], direction=[0, 0, -1], light_type=L_POINT, range=15)

        Light(root=self, name='ROOMB', point_name='comm_light2', light_group=comm_light, diffuse=[0.4, 0.5, 0.2],
            ambient=[0, 0, 0], direction=[0, 0, -1], light_type=L_POINT, range=15)

        Light(root=self, name='ROOMC', point_name='king_light1', light_group=king_light, diffuse=[0.8, 0.8, 0.9],
            ambient=[0, 0, 0], direction=[0, 0, -1], light_type=L_POINT, range=15)

        Light(root=self, name='ROOMD', point_name='king_light2', light_group=king_light, diffuse=[0.7, 0.6, 0.4],
            ambient=[0, 0, 0], direction=[0, 0, -1], light_type=L_POINT, range=15)

        Light(root=self, name='ROOME', point_name='king_light3', light_group=king_light, diffuse=[0.2, 0.2, 0.25],
            ambient=[0, 0, 0], direction=[0, 0, -1], light_type=L_POINT, range=15)

        comm = LiComm(root=self, name='comm', init_point='li_comm', light_group=0)
        screen = LiCommScreen(root=self, name='screen', init_point='li_comm', light_group=0)

        bg_music = Music(root=self, name='the_bg_music', sound=BACKGROUND_MUSIC, attenuation=0, priority=None)
        bg_music.change_attenuation(group=BG, attenuation=-18, duration=3, time_delay=3)

        exposition_music = Music(root=self, name='exposition_music', sound='rtc_music_reveal_and_exposition', attenuation=-15)

        # CHARACTERS

        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='trent_init', rotate_y=0)
        king = Character(root=self, actor=actors.King, light_group=king_light, init_point='king_init', rotate_y=-135)
        hatcher = Character(root=self, actor=actors.Hatcher, light_group=0, init_point='hatcher_init', rotate_y=0)
        alaric = Character(root=self, actor=actors.Alaric, light_group=king_light, init_point='alaric_init', rotate_y=0)
        darcy = Character(root=self, actor=actors.Darcy, light_group=0, init_point='darcy_init', rotate_y=0)
        mandrake = Character(root=self, actor=actors.Mandrake, init_point='mandrake_comm', rotate_y=-90,
                             floor_height=mandrake_floor_height, light_group=comm_light)
        bartender_fixture = Character(root=self, actor=actors.BartenderFixture, light_group=0, init_point=self.DEFAULT_POINT_NAME, rotate_y=180)

        guard = Character(root=self, actor=actors.OsirisOfficer, light_group=0, init_point='guard_init', rotate_y=90)

        MoveOffscreenEvent(root=self, group=BG, object_name=bartender_fixture.name)


        # MARKERS

        mrk_trent_talk = trent.get_stand_marker('trent_talk')
        mrk_hatcher_talk = trent.get_stand_marker('hatcher_talk')
        mrk_king = trent.get_stand_marker('king_init')
        mrk_alaric_comm = trent.get_stand_marker('alaric_comm')
        # mrk_mandrake_comm = trent.get_stand_marker('mandrake_comm')

        mrk_mandrake = self.get_automarker_name('mrk_mandrake')
        mrk_trent_front = self.get_automarker_name('mrk_trent_front')
        mrk_trent_front2 = self.get_automarker_name('mrk_trent_front2')
        mrk_trent_front_eye = self.get_automarker_name('mrk_trent_front_eye')

        # PREPARE

        hatcher.move_head_ik(group=BG, target_name=mrk_king, immediately=True)
        hatcher.move_eye_ik(group=BG, target_name=mrk_king, immediately=True)

        trent.move_head_ik(group=BG, target_name=mrk_king, immediately=True)
        trent.move_eye_ik(group=BG, target_name=mrk_king, immediately=True)

        king.move_head_ik(group=BG, target_name=mrk_hatcher_talk, immediately=True)
        king.move_eye_ik(group=BG, target_name=mrk_hatcher_talk, immediately=True)

        darcy.move_head_ik(group=BG, target_name=mrk_king, immediately=True)
        darcy.move_eye_ik(group=BG, target_name=mrk_king, immediately=True)

        alaric.move_head_ik(group=BG, target_name=mrk_king, immediately=True)
        alaric.move_eye_ik(group=BG, target_name=mrk_king, immediately=True)

        hatcher.start_head_ik(group=MAIN, duration=1000)
        hatcher.start_eye_ik(group=MAIN, duration=1000)

        trent.start_head_ik(group=MAIN, duration=1000)
        trent.start_eye_ik(group=MAIN, duration=1000)
        #
        # king.start_head_ik(group=MAIN, duration=1000, time_delay=5)
        # king.start_eye_ik(group=MAIN, duration=1000, time_delay=5)
        king.start_head_ik(group=MAIN, duration=1000, time_delay=1)
        king.start_eye_ik(group=MAIN, duration=1000, time_delay=1)

        # ACTION!

        cam_start.set(group=MAIN)

        cam_start.move_cam(group=MAIN, index=2, duration=6, smooth=True)
        # cam_start.move_focus(group=MAIN, index=2, duration=10, smooth=True)

        guard.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_SALUT_000LV_XA_03, start_time=1)
        guard.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_WALK_TRNS_180LV_XA_02, time_delay=2, trans_time=1)
        guard.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_WLKG_000LV_XA_01, time_delay=4.45)




        king.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)
        # trent.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)
        # alaric.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)
        # hatcher.motion(group=MAIN, duration=10, loop=True, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05)
        # darcy.motion(group=MAIN, duration=10, loop=True, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05)

        king.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_TURN_315LV_XA_02, trans_time=0.5, time_delay=2)

        trent.motion(group=MAIN, duration=5, start_time=1, loop=True, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01)
        trent.motion(group=MAIN, duration=3, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, time_delay=(1.3*3)-1)

        hatcher.motion(group=MAIN, duration=2.65, loop=True, anim=Female.Sc_FMBODY_WLKG_000LV_XA_01)
        hatcher.motion(group=MAIN, duration=3, anim=Female.Sc_FMBODY_WALK_STND_TRNS_000LV_XA_01, time_delay=2.65)

        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=15, duration=1, smooth=True, time_delay=(1.3*3)-0.1)


        main_group.append_time(4)

        king.facial(group=MAIN, index=10)

        MoveOffscreenEvent(root=self, group=MAIN, object_name=guard.name)

        cam_hatcher.set(group=MAIN)

        hatcher.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01)

        hatcher.facial(group=MAIN, index=20, extra_delay=0)
        hatcher.motion(group=MAIN, duration=3, anim=Female.Sc_FMHEAD_BASEPOSE_000LV_02_01, time_scale=1, trans_time=1)
        main_group.append_time(0.3)



        cam_king.set(group=MAIN)

        king.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, time_scale=0.7)

        king.facial(group=MAIN, index=30)
        king.facial(group=MAIN, index=40)



        MoveFastEvent(root=self, group=MAIN, object_name=darcy.name, target_name=self.get_automarker_name('darcy_walk'))
        MoveFastEvent(root=self, group=MAIN, object_name=alaric.name, target_name=self.get_automarker_name('alaric_walk'))


        alaric.motion(group=MAIN, duration=5, start_time=1, loop=True, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01)
        alaric.motion(group=MAIN, duration=3, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, time_delay=(1.3*3)-1)

        darcy.motion(group=MAIN, duration=2.65, loop=True, anim=Female.Sc_FMBODY_WLKG_000LV_XA_01)
        darcy.motion(group=MAIN, duration=3, anim=Female.Sc_FMBODY_WALK_STND_TRNS_000LV_XA_01, time_delay=2.65)

        darcy.start_head_ik(group=MAIN, duration=1000, time_delay=0.1)
        darcy.start_eye_ik(group=MAIN, duration=1000, time_delay=0.1)

        alaric.start_head_ik(group=MAIN, duration=1000, time_delay=0.1)
        alaric.start_eye_ik(group=MAIN, duration=1000, time_delay=0.1)

        cam_trent.set(group=MAIN)

        trent.motion(group=MAIN, duration=5, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01)

        trent.facial(group=MAIN, index=50)

        cam_king.set(group=MAIN)

        king.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=1.8, time_delay=0)
        king.move_eye_ik(group=MAIN, target_name=mrk_trent_front_eye, duration=0.8, time_delay=0)

        king.facial(group=MAIN, index=60)

        king.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, time_delay=1, trans_time=0.5, time_scale=0.7)

        king.facial(group=MAIN, index=70)

        king.move_head_ik(group=MAIN, target_name=mrk_hatcher_talk, duration=2.3, time_delay=-1)
        king.move_eye_ik(group=MAIN, target_name=mrk_hatcher_talk, duration=0.8, time_delay=-1)


        cam_hatcher.set(group=MAIN)

        hatcher.motion(group=MAIN, duration=10, loop=True, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05)

        hatcher.facial(group=MAIN, index=80)



        # DBG!

        # MoveFastEvent(root=self, group=MAIN, object_name=darcy.name, target_name=self.get_automarker_name('darcy_walk'))
        #
        # darcy.motion(group=MAIN, duration=2.65, loop=True, anim=Female.Sc_FMBODY_WLKG_000LV_XA_01)
        # darcy.motion(group=MAIN, duration=3, anim=Female.Sc_FMBODY_WALK_STND_TRNS_000LV_XA_01, time_delay=2.65)
        #
        # darcy.start_head_ik(group=MAIN, duration=1000, time_delay=0.1)
        # darcy.start_eye_ik(group=MAIN, duration=1000, time_delay=0.1)
        #
        # alaric.start_head_ik(group=MAIN, duration=1000, time_delay=0.1)
        # alaric.start_eye_ik(group=MAIN, duration=1000, time_delay=0.1)
        #
        # main_group.append_time(5)

        # DBG!


        cam_king.set(group=MAIN)


        king.move_head_ik(group=MAIN, target_name=mrk_mandrake, duration=2.3, time_delay=1)
        king.move_eye_ik(group=MAIN, target_name=mrk_mandrake, duration=0.8, time_delay=1)
        king.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_TURN_315LV_XA_02, trans_time=0.5, time_delay=1)


        alaric.move_head_ik(group=MAIN, target_name=mrk_mandrake, immediately=True)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_mandrake, immediately=True)

        trent.move_head_ik(group=MAIN, target_name=mrk_mandrake, duration=2.3, time_delay=1.5)
        trent.move_eye_ik(group=MAIN, target_name=mrk_mandrake, duration=0.8, time_delay=1.5)

        bg_music.change_attenuation(group=MAIN, attenuation=-100, duration=3)

        king.facial(group=MAIN, index=90)


        MoveFastEvent(root=self, group=MAIN, object_name=hatcher.name, target_name=self.get_automarker_name('hatcher_comm'))
        MoveFastEvent(root=self, group=MAIN, object_name=alaric.name, target_name=self.get_automarker_name('alaric_comm'))

        hatcher.move_head_ik(group=MAIN, target_name=mrk_mandrake, duration=2.3, time_delay=1)
        hatcher.move_eye_ik(group=MAIN, target_name=mrk_mandrake, duration=0.8, time_delay=1)
        hatcher.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_TURN_045LV_XA_03, time_scale=0.8, trans_time=0.5)

        darcy.move_head_ik(group=MAIN, target_name=mrk_mandrake, duration=2.3, time_delay=0)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_mandrake, duration=0.8, time_delay=0)

        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_TURN_045LV_XA_04, time_scale=0.8, trans_time=0.5)
        alaric.motion(group=MAIN, duration=40, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, time_scale=0.8)

        trent.motion(group=MAIN, duration=40, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, trans_time=1, time_delay=3)
        king.motion(group=MAIN, duration=40, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, trans_time=1, time_delay=1)
        hatcher.motion(group=MAIN, duration=10, loop=True, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05, trans_time=1, time_delay=3)
        darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_CROSS_ARMS_000LV_xa_03, trans_time=1, time_scale=0.7, time_delay=2)


        cam_comm.set(group=MAIN)
        cam_comm.move_cam(group=MAIN, index=2, duration=60, smooth=False)

        exposition_music.start(group=MAIN, duration=100)

        mandrake.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)

        main_group.append_time(2)

        MoveOffscreenEvent(root=self, object_name=screen.name)

        mandrake.facial(group=MAIN, index=100)
        mandrake.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_CONV_HNDS_CASL_000LV_xa_04, start_time=2, trans_time=1, time_delay=0, time_scale=0.8)
        mandrake.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00, start_time=0, time_delay=0.5, trans_time=0.2)
        mandrake.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLHAND_HNEUT_GESTL_CASL_000LV_00, start_time=0, time_delay=0.5, trans_time=0.2)

        mandrake.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_CONV_HNDSDN_TRNS_000LV_XA_01, trans_time=1, time_delay=10, time_scale=0.8)
        mandrake.motion(group=MAIN, duration=10, anim=Male.Sc_MLHAND_HNEUT_EDGE_LEFT_000LV_00, start_time=0, time_delay=10, trans_time=0.2)
        mandrake.motion(group=MAIN, duration=10, anim=Male.Sc_MLHAND_HNEUT_EDGE_RGHT_000LV_00, start_time=0, time_delay=10, trans_time=0.2)


        mandrake.facial(group=MAIN, index=110)
        mandrake.facial(group=MAIN, index=120)
        mandrake.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_CONV_RHND_CASL_000LV_xa_01, trans_time=1, time_delay=0, time_scale=0.8)
        mandrake.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00, start_time=1, trans_time=0.2)
        mandrake.facial(group=MAIN, index=130)


        mandrake.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_02, trans_time=1, time_delay=0, time_scale=0.8)
        mandrake.motion(group=MAIN, duration=10, anim=Male.Sc_MLHAND_HNEUT_EDGE_LEFT_000LV_00, start_time=0, time_delay=0, trans_time=0.2)
        mandrake.motion(group=MAIN, duration=10, anim=Male.Sc_MLHAND_HNEUT_EDGE_RGHT_000LV_00, start_time=0, time_delay=0, trans_time=0.2)

        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_SHRG_SHLDRS_SMALL_000LV_XA_01, time_scale=0.8, trans_time=0.5)

        trent.facial(group=MAIN, index=140)

        mandrake.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, trans_time=1)
        mandrake.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, trans_time=0.5, time_delay=3)

        trent.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, time_scale=0.8, trans_time=0.5, time_delay=2)

        mandrake.facial(group=MAIN, index=150)

        cam_insane.set(group=MAIN)


        darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_UNCRSS_ARMS_000LV_XA_03, time_scale=0.7)

        darcy.facial(group=MAIN, index=160)
        darcy.motion(group=MAIN, duration=3, anim=Female.Sc_FMHEAD_BASEPOSE_000LV_02_01, time_scale=1, trans_time=1)

        darcy.move_head_ik(group=MAIN, target_name=mrk_king, duration=2.3, time_delay=1)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_king, duration=0.8, time_delay=1)


        trent.move_head_ik(group=MAIN, target_name=mrk_king, duration=1.5, time_delay=0)
        trent.move_eye_ik(group=MAIN, target_name=mrk_king, duration=0.8, time_delay=0)

        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_TURN_315LV_XA_02, trans_time=0.5, time_scale=0.8)


        trent.facial(group=MAIN, index=170)

        main_group.append_time(0)

        #
        # MoveFastEvent(root=self, group=MAIN, object_name=darcy.name, target_name=self.get_automarker_name('darcy_comm'))
        # darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05, trans_time=0.5)
        #
        # darcy.facial(group=MAIN, index=190)
        #
        #
        # king.move_head_ik(group=MAIN, target_name=mrk_trent_talk, duration=2, time_delay=-1)
        # king.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.8, time_delay=-1)
        # alaric.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=2.3, time_delay=-1)
        # alaric.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.8, time_delay=-1)
        # hatcher.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=2, time_delay=-1)
        # hatcher.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.8, time_delay=-1)
        #
        #
        # king.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_TURN_045LV_XA_04, trans_time=0.5, time_delay=-1)
        #
        #
        # cam_team.set(group=MAIN)
        # cam_team.move_cam(group=MAIN, index=2, duration=8, smooth=True)
        # cam_team.move_focus(group=MAIN, index=2, duration=8, smooth=True)
        #
        #
        # trent.move_head_ik(group=MAIN, target_name=mrk_alaric_comm, duration=1.6, time_delay=0)
        # trent.move_eye_ik(group=MAIN, target_name=mrk_alaric_comm, duration=0.7, time_delay=0)
        #
        # alaric.facial(group=MAIN, index=180)
        # trent.move_head_ik(group=MAIN, target_name=mrk_king, duration=1.6, time_delay=0)
        # trent.move_eye_ik(group=MAIN, target_name=mrk_king, duration=0.7, time_delay=0)
        #
        # king.facial(group=MAIN, index=200)
        # trent.move_head_ik(group=MAIN, target_name=mrk_alaric_comm, duration=1.6, time_delay=0)
        # trent.move_eye_ik(group=MAIN, target_name=mrk_alaric_comm, duration=0.7, time_delay=0)
        # hatcher.facial(group=MAIN, index=210)
        #
        #
        # main_group.append_time(4)
        #
        # MoveFastEvent(root=self, object_name=screen.name, target_name=self.get_automarker_name('li_comm'))
        #
        # main_group.append_time(1000)


class Msn12CapturedDecisionScene(Scene):
    def action(self):
        main_group = self.get_group(MAIN)

        # CAMERAS

        cam_decision = LookAtCamera(root=self, name='cam_decision', fov=22)

        # PROPS

        king_light = 35

        Light(root=self, name='ROOMC', point_name='king_light1', light_group=king_light, diffuse=[0.8, 0.8, 0.9],
            ambient=[0, 0, 0], direction=[0, 0, -1], light_type=L_POINT, range=15)

        Light(root=self, name='ROOMD', point_name='king_light2', light_group=king_light, diffuse=[0.7, 0.6, 0.4],
            ambient=[0, 0, 0], direction=[0, 0, -1], light_type=L_POINT, range=15)

        Light(root=self, name='ROOME', point_name='king_light3', light_group=king_light, diffuse=[0.2, 0.2, 0.25],
            ambient=[0, 0, 0], direction=[0, 0, -1], light_type=L_POINT, range=15)


        # CHARACTERS

        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='trent_talk2', rotate_y=-5)
        king = Character(root=self, actor=actors.King, light_group=king_light, init_point='king_init', rotate_y=-180)
        hatcher = Character(root=self, actor=actors.Hatcher, light_group=0, init_point='hatcher_talk', rotate_y=45)
        alaric = Character(root=self, actor=actors.Alaric, light_group=king_light, init_point='alaric_comm', rotate_y=90)
        darcy = Character(root=self, actor=actors.Darcy, light_group=0, init_point='darcy_comm', rotate_y=0)


        # ACTION!

        cam_decision.set(group=MAIN)

        king.motion(group=MAIN, duration=1000, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)
        trent.motion(group=MAIN, duration=1000, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)
        alaric.motion(group=MAIN, duration=1000, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)
        hatcher.motion(group=MAIN, duration=1000, loop=True, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05)
        darcy.motion(group=MAIN, duration=1000, loop=True, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05)

        trent.motion(group=MAIN, duration=10, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, trans_time=0.25)

        main_group.append_time(1000)


class Msn12CapturedAcceptScene(Scene):
    def action(self):
        main_group = self.get_group(MAIN)

        # CAMERAS

        cam_team = LookAtCamera(root=self, name='cam_team', fov=24)
        cam_insane = LookAtCamera(root=self, name='cam_insane', fov=18)


        # bg_music = Music(root=self, name='the_bg_music', sound=BACKGROUND_MUSIC, attenuation=-100, priority=None)
        # bg_music.change_attenuation(group=BG, attenuation=-100, duration=0.1)

        hero_music = Music(root=self, name='hero_music', sound='rtc_music_reveal_enemy_position_of_strength', attenuation=-25)

        hero_music.start(group=MAIN, duration=1000, start_time=13000)
        hero_music.change_attenuation(group=MAIN, duration=3, attenuation=-15)


        # PROPS

        king_light = 35

        Light(root=self, name='ROOMC', point_name='king_light1', light_group=king_light, diffuse=[0.8, 0.8, 0.9],
            ambient=[0, 0, 0], direction=[0, 0, -1], light_type=L_POINT, range=15)

        Light(root=self, name='ROOMD', point_name='king_light2', light_group=king_light, diffuse=[0.7, 0.6, 0.4],
            ambient=[0, 0, 0], direction=[0, 0, -1], light_type=L_POINT, range=15)

        Light(root=self, name='ROOME', point_name='king_light3', light_group=king_light, diffuse=[0.2, 0.2, 0.25],
            ambient=[0, 0, 0], direction=[0, 0, -1], light_type=L_POINT, range=15)


        # CHARACTERS

        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='trent_talk2', rotate_y=-5)
        king = Character(root=self, actor=actors.King, light_group=king_light, init_point='king_init', rotate_y=-180)
        hatcher = Character(root=self, actor=actors.Hatcher, light_group=0, init_point='hatcher_talk', rotate_y=45)
        alaric = Character(root=self, actor=actors.Alaric, light_group=king_light, init_point='alaric_comm', rotate_y=90)
        darcy = Character(root=self, actor=actors.Darcy, light_group=0, init_point='darcy_comm', rotate_y=0)

        # MARKERS

        mrk_trent_talk = trent.get_stand_marker('trent_talk')
        mrk_hatcher_talk = trent.get_stand_marker('hatcher_talk')
        mrk_king = trent.get_stand_marker('king_init')
        mrk_alaric_comm = trent.get_stand_marker('alaric_comm')

        mrk_trent_front = self.get_automarker_name('mrk_trent_front')
        mrk_trent_front2 = self.get_automarker_name('mrk_trent_front2')

        # PREPARE

        hatcher.move_head_ik(group=BG, target_name=mrk_trent_front2, immediately=True)
        hatcher.move_eye_ik(group=BG, target_name=mrk_trent_talk, immediately=True)

        trent.move_head_ik(group=BG, target_name=mrk_king, immediately=True)
        trent.move_eye_ik(group=BG, target_name=mrk_king, immediately=True)

        king.move_head_ik(group=BG, target_name=mrk_trent_talk, immediately=True)
        king.move_eye_ik(group=BG, target_name=mrk_trent_talk, immediately=True)

        darcy.move_head_ik(group=BG, target_name=mrk_trent_front, immediately=True)
        darcy.move_eye_ik(group=BG, target_name=mrk_trent_front, immediately=True)

        alaric.move_head_ik(group=BG, target_name=mrk_trent_talk, immediately=True)
        alaric.move_eye_ik(group=BG, target_name=mrk_trent_talk, immediately=True)

        hatcher.start_head_ik(group=MAIN, duration=1000)
        hatcher.start_eye_ik(group=MAIN, duration=1000)

        trent.start_head_ik(group=MAIN, duration=1000)
        trent.start_eye_ik(group=MAIN, duration=1000)

        darcy.start_head_ik(group=MAIN, duration=1000)
        darcy.start_eye_ik(group=MAIN, duration=1000)

        alaric.start_head_ik(group=MAIN, duration=1000)
        alaric.start_eye_ik(group=MAIN, duration=1000)

        king.start_head_ik(group=MAIN, duration=1000)
        king.start_eye_ik(group=MAIN, duration=1000)

        # ACTION!

        cam_insane.set(group=MAIN)

        king.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)
        trent.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)
        alaric.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)
        hatcher.motion(group=MAIN, duration=10, loop=True, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05)
        darcy.motion(group=MAIN, duration=10, loop=True, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05)

        trent.motion(group=MAIN, duration=10, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, trans_time=0.25)

        darcy.facial(group=MAIN, index=190)

        cam_team.set(group=MAIN)
        cam_team.move_cam(group=MAIN, index=2, duration=8, smooth=True)
        cam_team.move_focus(group=MAIN, index=2, duration=8, smooth=True)

        trent.move_head_ik(group=MAIN, target_name=mrk_alaric_comm, duration=1.6, time_delay=0)
        trent.move_eye_ik(group=MAIN, target_name=mrk_alaric_comm, duration=0.7, time_delay=0)

        alaric.facial(group=MAIN, index=180)
        trent.move_head_ik(group=MAIN, target_name=mrk_king, duration=1.6, time_delay=0)
        trent.move_eye_ik(group=MAIN, target_name=mrk_king, duration=0.7, time_delay=0)

        king.facial(group=MAIN, index=200)
        trent.move_head_ik(group=MAIN, target_name=mrk_alaric_comm, duration=1.6, time_delay=0)
        trent.move_eye_ik(group=MAIN, target_name=mrk_alaric_comm, duration=0.7, time_delay=0)
        hatcher.facial(group=MAIN, index=210)


        hero_music.change_attenuation(group=MAIN, duration=2, attenuation=-25)
        main_group.append_time(2)
