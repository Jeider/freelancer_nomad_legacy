from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import Male, Trent as TrentAnim
from story import actors


class GlassGreen(Prop):
    COMPOUND_TEMPLATE_NAME = 'glass_green'


class BarCloth(Prop):
    COMPOUND_TEMPLATE_NAME = 'barcloth_wadded'


class PDA(Prop):
    COMPOUND_TEMPLATE_NAME = 'pda'


class Handie(Prop):
    COMPOUND_TEMPLATE_NAME = 'handie'
    SRT_GRP = -55


class HandieBackdrop(BackgroundProp):
    COMPOUND_TEMPLATE_NAME = 'handie_back'
    SRT_GRP = 0
    USR_FLG = 0


class BarmanScene(Scene):
    DUMP_FILE = 'm01_barman'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)
        cam_dbg = LookAtCamera(root=self, name='cam_dbg', fov=20, look_duration=200)

        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=30, look_duration=200)
        cam_barman = LookAtCamera(root=self, name='cam_barman', fov=20, look_duration=200)
        cam_bottleput = LookAtCamera(root=self, name='cam_bottleput', fov=22, look_duration=200)
        cam_drinking = LookAtCamera(root=self, name='cam_drinking', fov=22, look_duration=200)
        cam_handie = LookAtCamera(root=self, name='cam_handie', fov=16, look_duration=200)
        cam_jameson = LookAtCamera(root=self, name='cam_jameson', fov=16, look_duration=200)
        cam_pda_done = LookAtCamera(root=self, name='cam_pda_done', fov=25, look_duration=200)
        cam_wonderfull = LookAtCamera(root=self, name='cam_wonderfull', fov=30, look_duration=200)
        cam_whatdo = LookAtCamera(root=self, name='cam_whatdo', fov=25, look_duration=200)
        cam_explain = LookAtCamera(root=self, name='cam_whatdo_explanation', fov=30, look_duration=200)
        cam_last = LookAtCamera(root=self, name='cam_last', fov=25, look_duration=200)

        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='char_trent',
                          rotate_from_quat=True)
        barman = Character(root=self, actor=actors.IntroBarman, light_group=0, init_point='char_barman',
                           rotate_from_quat=True)
        jameson = Character(root=self, actor=actors.Jameson, light_group=0, init_point='char_jameson',
                           rotate_from_quat=True)
        alaric = Character(root=self, actor=actors.Alaric, light_group=3, init_point='char_alaric',
                           rotate_from_quat=True, use_ambient=True)

        glass = GlassGreen(root=self, name='glass', init_point='glass', light_group=0, rotate_from_quat=True)
        glass_trent = GlassGreen(root=self, name='glass_trent', init_point=self.OFFSCREEN_POINT_NAME, light_group=0)
        cloth = BarCloth(root=self, name='cloth', init_point=self.OFFSCREEN_POINT_NAME, light_group=0)
        pda = PDA(root=self, name='pda', init_point=self.OFFSCREEN_POINT_NAME, light_group=0)
        handie = Handie(root=self, name='handie', init_point='handie', light_group=0, matrix_scale=0.5, rotate_y=180, use_ambient=True)
        HandieBackdrop(root=self, name='handie_backdrop', init_point='handie_backdrop', light_group=0,
                       use_ambient=True)

        mrk_barman = barman.get_stand_marker('char_barman')
        mrk_jameson = barman.get_stand_marker('char_jameson')

        mrk_pda = self.get_automarker('mrk_pda')
        mrk_pda2 = self.get_automarker('mrk_pda2')

        AttachEvent(root=self, group=BG, target_name=handie.name, parent_name=cam_handie.name,
                    duration=500, target_part='', target_type=TARGET_ROOT,
                    offset_x=0, offset_y=0.1, offset_z=1.5)

        self.trent = trent
        self.barman = barman
        self.alaric = alaric
        self.glass = glass
        self.glass_trent = glass_trent
        self.cloth = cloth
        self.pda = pda
        self._sfx()

        # cam_dbg.set(group=MAIN)

        EyeIkEvent(root=self, group=MAIN, char_name=alaric.name, target_name=cam_handie.name,
                   duration=500, time_delay=0)
        # self._m(barman, Male.Sc_MLBODY_BASEPOSE_LARG_FRAME_000LV_XA_04, 0, 1)

        cam_trent.set(group=MAIN)
        cam_trent.move_cam(group=MAIN, index=2, duration=10, smooth=True)
        cam_trent.move_focus(group=MAIN, index=2, duration=10, smooth=True)
        cam_trent.change_fov(group=MAIN, fov=10, duration=10, smooth=True)
        cam_trent.move_cam(group=MAIN, index=3, duration=7, smooth=True, time_delay=10)
        cam_trent.change_fov(group=MAIN, fov=15, duration=7, smooth=True, time_delay=10)

        self._m(trent, Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01, 5, 1)
        self._m(trent, Male.Sc_MLBODY_WLKG_000LV_XA_01, 6, 3, trans=0.25)
        self._m(trent, Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, 7.3, 3)
        self._m(trent, Male.Sc_MLBODY_STND_LOOK_AROU_CASL_000LV_XA_08, 9.5, 9)
        self._m(trent, Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01, 18, 3)
        self._m(trent, Male.Sc_MLBODY_WLKG_000LV_XA_01, 19, 2)

        main_group.append_time(20)

        # cam_wonderfull.set(group=MAIN)
        # MoveFastEvent(root=self, group=MAIN, object_name=barman.name,
        #               target_name=self.get_automarker_name('char_barman'), rotate_y=30, time_delay=-0.01)
        # MoveOffscreenEvent(root=self, group=MAIN, object_name=pda.name, time_delay=3)
        # self._m(barman, Male.Sc_MLBODY_STND_LEAN_BAR_TRNS_000LV_XA_02, 0, 10)
        # self._m(barman, Male.Sc_MLBODY_LEAN_STND_BAR_TRNS_000LV_XA_03, 3, 10, trans=0.25)
        # barman.facial(group=MAIN, index=120, auto_lip=True)
        #
        # return
        #







        trent.move_head_ik(group=MAIN, target_name=mrk_barman, duration=0, time_delay=0)

        self._m(jameson, Male.Sc_MLBODY_STND_POINTR_OVRTHRE_000LV_XA_03, 0, 10, scale=0.9, start=0.5)
        self._m(jameson, Male.Sc_MLBODY_STND_TURN_270LV_XA_04, 2, 10, scale=1, trans=0.5)
        cam_barman.set(group=MAIN, time_delay=0)
        cam_barman.move_cam(group=MAIN, index=2, duration=10, smooth=True, time_delay=0)
        cam_barman.move_focus(group=MAIN, index=2, duration=10, smooth=True, time_delay=0)
        self._hold(cloth, barman, 0, 15, 'hprightconnect_prop_barcloth_wadded', 'hprightconnect')
        self._hold(glass, barman, 0, 15, 'hpleftconnect_prop_glass_green', 'hpleftconnect')
        self._m(barman, Male.Sc_MLBODY_STND_CLEAN_GLAS_000LV_A_26, 0, 50, start=10)
        self._m(barman, 'Sc_MLHAND_HNEUT_HOLDD_LEFT_000LV_00', 0, 0.1, start=5)
        MoveFastEvent(root=self, group=MAIN, object_name=trent.name,
                      target_name=self.get_automarker_name('trent_bar'), rotate_y=210, time_delay=1)

        trent.start_head_ik(group=MAIN, duration=1000)


        self._m(trent, Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, 1, 10, scale=0.8, start=0.25, trans=0.1)
        self._head(barman, trent.name, 2, 25, 'Body_Neck', TARGET_PART)
        self._m(barman, 'Sc_MLHEAD_HAPPY_SMILE_PLEASD_000LV_XA_%', 2, 5, trans=0.1)

        main_group.append_time(4)

        self._m(trent, Male.Sc_MLBODY_STND_LEAN_BAR_TRNS_000LV_XA_02, 0, 10, scale=0.8, trans=0.1)
        self._m(barman, Male.Sc_MLHAND_NEUT_LEFT_000LV_A_00, 1, 1)
        trent.facial(group=MAIN, index=10, auto_lip=True)

        trent.move_head_ik(group=MAIN, target_name=mrk_jameson, duration=2, time_delay=-0.25)
        self._m(jameson, Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, 0, 10, trans=0.25, scale=0.8)
        jameson.facial(group=MAIN, index=20, auto_lip=True)

        # cam_barman.set(group=MAIN)
        # self._m(barman, 'Sc_dx_s012x_0801_manhtn_bar', 0, 2, trans=0.25)
        # barman.facial(group=MAIN, index=20, auto_lip=True)




        cam_drinking.set(group=MAIN)
        # self._m(trent, 'Sc_dx_s037b_0501_Trent', 0, 2, trans=0.25)
        self._m(trent, Male.Sc_MLBODY_LEAN_STND_BAR_TRNS_000LV_XA_03, 1, 5, scale=0.8, trans=0.25)
        trent.facial(group=MAIN, index=30, auto_lip=True)

        cam_jameson.set(group=MAIN)
        jameson.facial(group=MAIN, index=40, auto_lip=True)


        # cam_barman.set(group=MAIN)
        # self._m(barman, 'Sc_dx_s012x_0801_manhtn_bar', 0, 1.3, trans=0.25)
        # self._m(trent, 'Sc_MLHEAD_HAPPY_SMILE_PLEASD_000LV_XA_%', 1, 5, trans=0.25)
        # barman.facial(group=MAIN, index=40, auto_lip=True)
        #
        # cam_trent.set(group=MAIN)
        # self._m(trent, 'Sc_dx_s038x_4501_Trent', 0, 10, trans=0.25)
        # self._m(trent, Male.Sc_MLBODY_STND_GESTL_LEFT_000LV_XA_02, 1, 10, scale=0.5, trans=0.25)
        # self._m(trent, 'Sc_MLHAND_HNEUT_GESTL_SMALL_000LV_00', 1, 10, scale=0.5, trans=0.25)
        # trent.facial(group=MAIN, index=50, auto_lip=True)
        #
        # cam_bottleput.set(group=MAIN)
        # self._m(barman, 'Sc_dx_s012x_0801_manhtn_bar', 0.25, 1.5, trans=0.25)
        # self._m(barman, 'Sc_SPCBODY_s003_LI_BARKEEP_XA_STND_PUSH_DRINK_000LV_05', 0, 10)
        # self._m(barman, 'Sc_dx_s003x_1401_manhtn_bar', 2, 2, trans=0.25)
        # self._m(barman, 'Sc_MLHEAD_HAPPY_SMILE_PLEASD_000LV_XA_%', 3.8, 2, trans=0.1)
        # self._sfx_at('sfx_put_down_glass05', 2.5)
        # self._sfx_at('sfx_pick_up_glass01', 4)
        # EyeIkEvent(root=self, group=MAIN, char_name=barman.name, target_name=trent.name,
        #            duration=5, time_delay=0, target_part='hp_head', target_type=TARGET_ROOT)
        # MoveOffscreenEvent(root=self, group=MAIN, object_name=glass.name, time_delay=1)
        # MoveOffscreenEvent(root=self, group=MAIN, object_name=cloth.name, time_delay=1)
        # cam_drinking.set(group=MAIN, time_delay=5)
        # cam_drinking.move_cam(group=MAIN, index=2, duration=20, smooth=True, time_delay=5)
        # self._m(trent, 'Sc_dx_s052x_0401_Trent', 5.9, 4, trans=0.25)
        # self._m(trent, Male.Sc_MLBODY_STND_HOLDDRNKL_TOAST_000LV_XA_06, 5, 10)
        # self._m(trent, 'Sc_MLHAND_HNEUT_HOLDD_LEFT_000LV_00', 5, 0.2, scale=10, trans=0.25)
        # self._hold(glass_trent, trent, 5, 11.5, 'hpleftconnect_prop_glass_green', 'hpleftconnect')
        # barman.facial(group=MAIN, index=60, auto_lip=True)
        #
        # cam_drinking.set(group=MAIN)
        # self._m(trent, Male.Sc_MLBODY_STND_DRINK_LHND_000LV_A_06, 3, 10, trans=0.5)
        # trent.facial(group=MAIN, index=70, auto_lip=True)
        #
        # cam_barman.set(group=MAIN)
        # self._m(trent, 'Sc_MLHEAD_MOTION_DRINK_SWALLOW_TRENT_000LV_XA_%', 0.8, 3, trans=0.3)
        # self._sfx_at('sfx_gulp01', 1.8)
        # self._m(barman, 'Sc_dx_s003x_0601_manhtn_bar', 0, 4, trans=0.25)
        # self._m(trent, Male.Sc_MLBODY_STND_PUTDNL_DRINK_BAR_000LV_XA_06, 3, 10, trans=2)
        # barman.facial(group=MAIN, index=80, auto_lip=True)





        cam_drinking.set(group=MAIN)
        # self._m(trent, 'Sc_dx_s037b_0501_Trent', 0, 4, trans=0.25)
        # self._m(trent, 'Sc_MLHAND_HNEUT_HOLDD_LEFT_000LV_00', 1, 1, start=9, trans=0.3)
        # self._m(trent, 'Sc_dx_s037b_0501_Trent', 1.5, 1, trans=0.25)
        # self._sfx_at('sfx_put_down_glass05', 1)
        # cam_drinking.move_focus(group=MAIN, index=2, duration=10, smooth=True, time_delay=3)
        self._hold(pda, trent, 0, 23, 'Hp_LHand_PDA', 'HpLeftConnect')
        # NeckIkEvent(root=self, group=MAIN, char_name=trent.name, target_name=pda.name,
        #             duration=2, time_delay=3.5, target_type=TARGET_ROOT)
        trent.move_head_ik(group=MAIN, target_name=mrk_pda.name, duration=1, time_delay=0.4)
        trent.move_head_ik(group=MAIN, target_name=mrk_pda2.name, duration=3, time_delay=1.4)
        self._m(trent, Male.Sc_MLBODY_STND_DEALR_PDA_000LV_XA_09, 0, 8, trans=1)
        self._m(trent, Male.Sc_MLHAND_HNEUT_PDA_LEFT_000LV_00, 0, 4, scale=2, trans=0.25)
        trent.facial(group=MAIN, index=50, auto_lip=True)
        self._m(trent, TrentAnim.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, 0, 2, scale=2, trans=0.25)

        # cam_trent.set(group=MAIN)
        self._m(trent, 'Sc_MLHAND_HNEUT_GESTR_TYPING_000LV_XB', 0, 5, scale=0.2)
        self._sfx_at('sfx_ui_react_accept01', 1)
        # trent.facial(group=MAIN, index=100, auto_lip=True)

        self._m(trent, 'Sc_dx_s059x_0501_Trent', 0, 2, trans=0.25)
        self._sfx_at('sfx_ui_react_accept02', 0.5)
        self._sfx_at('sfx_ui_react_data01', 2)
        # trent.facial(group=MAIN, index=105, auto_lip=True)
        main_group.append_time(2)

        cam_handie.set(group=MAIN)
        self._m(alaric, Male.Sc_MLBODY_STND_IDLE_LHNDUP_000LV_XA_03, 0, 5)
        self._m(alaric, Male.Sc_MLBODY_STND_GESTL_NOPE_000LV_A_03, 3, 5, trans=1)
        self._m(alaric, Male.Sc_MLBODY_STND_IDLE_DEEP_BRTH_000LV_XA_04, 6.5, 5, trans=1)
        self._m(alaric, Male.Sc_MLBODY_STND_TALK_SMALL_000DN_A_17, 10, 6, trans=1)
        self._m(trent, Male.Sc_MLHAND_NEUT_RGHT_000LV_A_00, 1, 5, trans=0.25)
        alaric.facial(group=MAIN, index=70, auto_lip=True)
        self._m(alaric, Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, 0, 3, trans=0.25)
        #
        # cam_pda_done.set(group=MAIN, time_delay=1)

        #
        # trent.facial(group=MAIN, index=80, auto_lip=True)

        cam_jameson.set(group=MAIN)
        # self._m(jameson, Male.Sc_MLBODY_STND_SHRG_SHLDRS_BIG_000LV_XA_03, 0, 12, trans=0.25, scale=0.8)
        jameson.facial(group=MAIN, index=80, auto_lip=True)



        cam_drinking.set(group=MAIN)
        cam_drinking.move_cam(group=MAIN, index=2, duration=10, smooth=True, time_delay=3)
        cam_drinking.move_focus(group=MAIN, index=2, duration=10, smooth=True, time_delay=3)
        self._m(trent, Male.Sc_MLBODY_STND_DEALR_PDA_000LV_XA_09, 0, 3, start=7)
        # self._sfx_at('sfx_ui_react_denied01', 12)
        trent.move_head_ik(group=MAIN, target_name=mrk_jameson, duration=2, time_delay=0.1)

        self._m(trent, Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, 3, 6, trans=0.25, scale=0.8)
        trent.facial(group=MAIN, index=90, auto_lip=True)
        trent.move_head_ik(group=MAIN, target_name=mrk_barman, duration=2, time_delay=-2)
        self._m(trent, Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, 0, 6, trans=0.25, scale=0.8)
        main_group.append_time(0.5)
        trent.facial(group=MAIN, index=100, auto_lip=True)
        trent.move_head_ik(group=MAIN, target_name=mrk_jameson, duration=2, time_delay=-3)

        cam_jameson.set(group=MAIN)
        self._m(jameson, Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, 0, 10, trans=0.25, scale=0.8)
        jameson.facial(group=MAIN, index=110, auto_lip=True)
        self._m(jameson, Male.Sc_MLBODY_STND_WALK_TRNS_270LV_XA_02, -2, 10, trans=0.25, scale=0.8)
        main_group.append_time(1)

        cam_bottleput.set(group=MAIN)
        self._m(barman, 'Sc_SPCBODY_s003_LI_BARKEEP_XA_STND_PUSH_DRINK_000LV_05', 0, 10, scale=0.7)
        # self._m(barman, 'Sc_MLHEAD_HAPPY_SMILE_PLEASD_000LV_XA_%', 3.8, 2, trans=0.1)
        EyeIkEvent(root=self, group=MAIN, char_name=barman.name, target_name=trent.name,
                   duration=5, time_delay=0, target_part='hp_head', target_type=TARGET_ROOT)
        MoveOffscreenEvent(root=self, group=MAIN, object_name=glass.name, time_delay=1)
        MoveOffscreenEvent(root=self, group=MAIN, object_name=cloth.name, time_delay=1)
        barman.facial(group=MAIN, index=120, auto_lip=True,
                      auto_anim_force=Male.Sc_dx_s003x_1401_manhtn_bar, auto_anim_force_seconds=2)

        trent.move_head_ik(group=MAIN, target_name=mrk_barman, duration=0, time_delay=0)

        cam_drinking.set(group=MAIN)
        self._m(trent, Male.Sc_MLBODY_STND_DRINK_LHND_SIP_000LV_XA_06, 0, 10, scale=0.7)
        self._m(trent, Male.Sc_MLBODY_STND_DRINK_LHND_SIP_000LV_XA_06, 1, 10, scale=0.6, trans=0.5)
        self._m(trent, 'Sc_MLHAND_HNEUT_HOLDD_LEFT_000LV_00', 0, 0.1, start=5)
        self._hold(glass_trent, trent, 0, 4, 'hpleftconnect_prop_glass_green', 'hpleftconnect')

        trent.facial(group=MAIN, index=130, auto_lip=True)




        cam_bottleput.set(group=MAIN)
        self._hold(cloth, barman, 0, 25, 'hprightconnect_prop_barcloth_wadded', 'hprightconnect')
        self._hold(glass, barman, 4, 25, 'hpleftconnect_prop_glass_green', 'hpleftconnect')
        self._m(barman, 'Sc_MLHAND_HNEUT_HOLDD_LEFT_000LV_00', 4, 0.1, start=5)
        self._m(barman, Male.Sc_MLBODY_STND_CLEAN_GLAS_000LV_A_26, 0, 20)
        barman.facial(group=MAIN, index=140, auto_lip=True,
                      auto_anim_force=Male.Sc_dx_s003x_0601_manhtn_bar, auto_anim_force_seconds=4)


        MoveOffscreenEvent(root=self, group=MAIN, object_name=glass_trent.name, time_delay=-1)

        cam_drinking.set(group=MAIN)
        self._m(trent, Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, -1, 10, scale=0.8)
        self._m(trent, Male.Sc_MLHAND_NEUT_LEFT_000LV_A_00, -1, 10, scale=0.8)
        self._m(trent, Male.Sc_MLBODY_STND_GESTL_180LV_XA_02, 5, 10, scale=0.8, trans=1)
        # self._m(barman, Male.Sc_MLBODY_STND_LEAN_BAR_TRNS_000LV_XA_02, 4, 10, trans=1)

        trent.facial(group=MAIN, index=150, auto_lip=True)
        MoveFastEvent(root=self, group=MAIN, object_name=barman.name,
                      target_name=self.get_automarker_name('char_barman'), rotate_y=0, time_delay=-1)

        self._m(barman, Male.Sc_MLBODY_STND_CLEAN_GLAS_000LV_A_26, 0, 20, start=7)
        cam_bottleput.set(group=MAIN)
        barman.facial(group=MAIN, index=160, auto_lip=True,
                      auto_anim_force=Male.Sc_dx_s003x_1401_manhtn_bar, auto_anim_force_seconds=2)



        main_group.append_time(2)
        return


        main_group.append_time(15)
        return

        cam_wonderfull.set(group=MAIN)
        MoveFastEvent(root=self, group=MAIN, object_name=barman.name,
                      target_name=self.get_automarker_name('char_barman'), rotate_y=30, time_delay=-0.01)
        MoveOffscreenEvent(root=self, group=MAIN, object_name=pda.name, time_delay=3)
        self._m(barman, Male.Sc_MLBODY_STND_LEAN_BAR_TRNS_000LV_XA_02, 0, 10)
        self._m(barman, 'Sc_dx_s003x_1401_manhtn_bar', 0, 10, trans=0.25)
        self._m(barman, 'Sc_dx_s003x_1401_manhtn_bar', 2, 10, trans=0.25)
        self._m(barman, Male.Sc_MLBODY_LEAN_STND_BAR_TRNS_000LV_XA_03, 3, 10, trans=0.25)
        barman.facial(group=MAIN, index=130, auto_lip=True)

        cam_whatdo.set(group=MAIN)
        EyeIkEvent(root=self, group=MAIN, char_name=trent.name, target_name=barman.name,
                   duration=3, time_delay=0, target_part='Body_Neck', target_type=TARGET_PART)
        self._m(trent, 'Sc_dx_s063x_0101_Trent', 0, 3, trans=0.25)
        self._m(trent, Male.Sc_MLBODY_STND_SHRG_SHLDRS_BIG_000LV_XA_03, 0, 10, trans=0.1)
        trent.facial(group=MAIN, index=140, auto_lip=True)

        cam_explain.set(group=MAIN)
        cam_explain.move_cam(group=MAIN, index=2, duration=20, smooth=True)
        self._hold(cloth, barman, 0, 20, 'hprightconnect_prop_barcloth_wadded', 'hprightconnect')
        self._hold(glass, barman, 4, 16, 'hpleftconnect_prop_glass_green', 'hpleftconnect')
        self._m(barman, 'Sc_MLHAND_HNEUT_HOLDD_LEFT_000LV_00', 4, 0.1, start=5)
        self._m(barman, Male.Sc_MLBODY_STND_CLEAN_GLAS_000LV_A_26, 0, 20)
        self._m(barman, 'Sc_dx_s003x_0601_manhtn_bar', 0, 4.5, trans=0.25)
        self._m(barman, 'Sc_dx_s003x_0601_manhtn_bar', 4.5, 4.5, trans=0.25)
        self._m(barman, 'Sc_dx_s003x_0601_manhtn_bar', 9, 4.5, trans=0.25)
        self._m(barman, 'Sc_dx_s003x_0601_manhtn_bar', 13.5, 4.5, trans=0.25)
        cam_whatdo.set(group=MAIN, time_delay=19)
        self._m(trent, Male.Sc_MLBODY_STND_TURN_ARML_090LV_A_08, 19, 10)
        barman.facial(group=MAIN, index=150, auto_lip=True)

        cam_whatdo.set(group=MAIN)
        self._m(trent, 'Sc_dx_s063x_0101_Trent', 0, 3, trans=0.25)
        self._head(trent, barman.name, 2, 5, 'hp_neck', TARGET_HARDPOINT)
        MoveFastEvent(root=self, group=MAIN, object_name=barman.name,
                      target_name=self.get_automarker_name('char_barman'), rotate_y=30, time_delay=3)
        MoveOffscreenEvent(root=self, group=MAIN, object_name=glass.name)
        MoveOffscreenEvent(root=self, group=MAIN, object_name=cloth.name)
        trent.facial(group=MAIN, index=160, auto_lip=True)

        cam_explain.set(group=MAIN)
        self._m(barman, Male.Sc_MLBODY_STND_TALK_SMALL_000LV_A_16, 0, 13)
        self._m(barman, 'Sc_dx_s003x_0601_manhtn_bar', 0, 4.5, trans=0.25)
        self._m(barman, Male.Sc_MLBODY_STND_RUB_CHIN_000LV_A_07, 4, 14, scale=0.5, trans=1)
        self._m(barman, 'Sc_dx_s003x_0601_manhtn_bar', 4.5, 4.5, trans=0.25)
        self._m(barman, 'Sc_dx_s003x_0601_manhtn_bar', 9, 4.5, trans=0.25)
        self._m(barman, 'Sc_dx_s003x_1401_manhtn_bar', 13.5, 4.5, trans=0.25)
        cam_last.set(group=MAIN, time_delay=17)
        cam_last.move_cam(group=MAIN, index=2, duration=10, smooth=True, time_delay=17)
        cam_last.move_focus(group=MAIN, index=2, duration=10, smooth=True, time_delay=17)
        self._m(trent, Male.Sc_MLBODY_STND_LOOK_WATC_IMPA_000LV_A_23, 17, 4, scale=0.8, start=3)
        barman.facial(group=MAIN, index=170, auto_lip=True)

        cam_last.set(group=MAIN)
        self._m(trent, 'Sc_dx_s038x_4501_Trent', 0, 6, trans=0.25)
        self._m(trent, Male.Sc_MLBODY_STND_GESTL_180LV_XA_02, 3, 10, scale=0.8, trans=1)
        self._m(barman, Male.Sc_MLBODY_STND_LEAN_BAR_TRNS_000LV_XA_02, 4, 10, trans=1)
        self._head(barman, trent.name, 4, 25, 'Body_Neck', TARGET_PART)
        trent.facial(group=MAIN, index=180, auto_lip=True)

        cam_barman.set(group=MAIN)
        self._m(barman, 'Sc_dx_s003x_1801_manhtn_bar', 0, 4.5, trans=0.25)
        self._m(trent, Male.Sc_MLBODY_STND_WALK_TRNS_270LV_XA_02, 1.5, 10, trans=1)
        self._m(barman, Male.Sc_MLBODY_LEAN_STND_BAR_TRNS_000LV_XA_03, 3.5, 2.786)
        barman.facial(group=MAIN, index=190, auto_lip=True)

        main_group.append_time(2)

    def _m(self, char, anim, delay, duration, scale=1, start=0, trans=None, loop=False):
        char.motion(group=MAIN, anim=anim, duration=duration, time_delay=delay,
                    time_scale=scale, start_time=start, trans_time=trans, loop=loop)

    def _hold(self, prop, parent, delay, duration, target_hp, parent_hp):
        ConnectHardpointEvent(root=self, group=MAIN, target_name=prop.name, parent_name=parent.name,
                              duration=duration, target_hardpoint=target_hp, parent_hardpoint=parent_hp,
                              time_delay=delay)

    def _head(self, char, target, delay, duration, part, target_type):
        NeckIkEvent(root=self, group=MAIN, char_name=char.name, target_name=target,
                    duration=duration, time_delay=delay, target_part=part, target_type=target_type)

    def _sfx(self):
        self.sfx = {}
        for name in (
            'sfx_put_down_glass05',
            'sfx_pick_up_glass01',
            'sfx_gulp01',
            'sfx_ui_react_accept01',
            'sfx_ui_react_accept02',
            'sfx_ui_react_data01',
            'sfx_ui_react_denied01',
        ):
            self.sfx[name] = Sound(root=self, name=name, sound=name, attenuation=-10)

    def _sfx_at(self, name, delay, duration=4):
        self.sfx[name].start(group=MAIN, duration=duration, time_delay=delay)
