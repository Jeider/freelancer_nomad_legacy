from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import Male, Female, Trent

from story import actors


class MetalGlass(Prop):
    COMPOUND_TEMPLATE_NAME = 'glass_metal_1'


class BottleWine1(Prop):
    COMPOUND_TEMPLATE_NAME = 'bottle_wine_2'


class Msn11DrinkScene(Scene):
    POINT_ROTATE_OVERRIDES = {
        'trent_talk': (0, 180, 0),
        'trent_angry': (0, 60, 0),
        'bottle_wine_bar': (90, 0, 0),
        'glass_bar': (90, 0, 0),
        'glass_trent': (90, 0, 0),
        'edison_go': (0, -90, 0),
    }

    def action(self):
        main_group = self.get_group(MAIN)

        # CAMERAS

        cam_dbg = LookAtCamera(root=self, name='cam_dbg', fov=30)
        cam_start = LookAtCamera(root=self, name='cam_start', fov=20)
        cam_kim = LookAtCamera(root=self, name='cam_kim', fov=20)
        cam_kim_leave = LookAtCamera(root=self, name='cam_kim_leave', fov=22)
        cam_edison = LookAtCamera(root=self, name='cam_edison', fov=18)
        cam_drinkins = LookAtCamera(root=self, name='cam_drinkins', fov=18)
        cam_ready = LookAtCamera(root=self, name='cam_ready', fov=16)
        cam_final = LookAtCamera(root=self, name='cam_final', fov=22)

        # PROPS

        bottle_wine_bar = BottleWine1(root=self, name='bottle_wine_bar', init_point='bottle_wine_bar', light_group=0)
        glass_bar = MetalGlass(root=self, name='glass_bar', init_point='glass_bar', light_group=0)
        glass_trent = MetalGlass(root=self, name='glass_trent', init_point='glass_trent', light_group=0)

        # CHARACTERS

        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='trent_init', rotate_y=60,
                          extra_ik_markers=['LUpArm', 'LLowArm', 'RUpArm', 'RLowArm', 'LHand'])
        kim = Character(root=self, actor=actors.Kim, light_group=0, init_point='kim_listen', rotate_y=0)
        edison = Character(root=self, actor=actors.EdisonTrent, light_group=0, init_point='edison_init', rotate_y=0)
        bartender = Character(root=self, actor=actors.MusashiBartender, light_group=0, init_point='bartender', rotate_y=180)
        bartender_fixture = Character(root=self, actor=actors.BartenderFixture, light_group=0, init_point='bartender_fixture', rotate_y=180)



        # ConnectHardpointEvent(root=self, group=MAIN, target_name=tenji_bottle.name, parent_name=tenji.name,
        #                       duration=6, target_hardpoint="HpRightConnect_prop_bottle_wine_1",
        #                       parent_hardpoint="HpRightConnect", time_delay=2)


        # MARKERS

        mrk_trent_init = trent.get_stand_marker('trent_init')
        mrk_trent_angry = trent.get_stand_marker('trent_angry')
        mrk_trent_drink = trent.get_stand_marker('trent_drink')
        mrk_kim_listen = kim.get_stand_marker('kim_listen')
        mrk_edison_bar = edison.get_stand_marker('edison_bar')
        # mrk_junko_talk = junko.get_sit_marker('junko_talk')
        #


        mrk_trent_angry_front = self.get_automarker_name('mrk_trent_angry_front')
        mrk_kim_forward = self.get_automarker_name('mrk_kim_forward')
        mrk_kim_forward2 = self.get_automarker_name('mrk_kim_forward2')
        mrk_kim_table = self.get_automarker_name('mrk_kim_table')
        mrk_kim_table2 = self.get_automarker_name('mrk_kim_table2')
        mrk_kim_leave = self.get_automarker_name('mrk_kim_leave')
        mrk_kim_away = self.get_automarker_name('mrk_kim_away')
        mrk_kim_away_door = self.get_automarker_name('mrk_kim_away_door')
        mrk_trent_table = self.get_automarker_name('mrk_trent_table')
        mrk_trent_front = self.get_automarker_name('mrk_trent_front')
        mrk_trent_front2 = self.get_automarker_name('mrk_trent_front2')
        mrk_trent_drink_low_arm_left = self.get_automarker_name('mrk_trent_drink_low_arm_left')
        mrk_trent_drink_low_arm_right = self.get_automarker_name('mrk_trent_drink_low_arm_right')
        mrk_trent_drink_low_arm_right_drink = self.get_automarker_name('mrk_trent_drink_low_arm_right_drink')

        mrk_trent_drink_top_arm_left = self.get_automarker_name('mrk_trent_drink_top_arm_left')
        mrk_trent_drink_top_arm_left2 = self.get_automarker_name('mrk_trent_drink_top_arm_left2')
        mrk_trent_drink_top_arm_right = self.get_automarker_name('mrk_trent_drink_top_arm_right')
        mrk_trent_drink_top_arm_right2 = self.get_automarker_name('mrk_trent_drink_top_arm_right2')
        mrk_trent_drink_top_arm_left_drink = self.get_automarker_name('mrk_trent_drink_top_arm_left_drink')
        mrk_trent_drink_low_arm_left_drink = self.get_automarker_name('mrk_trent_drink_low_arm_left_drink')
        mrk_trent_drink_top_arm_left_drink2 = self.get_automarker_name('mrk_trent_drink_top_arm_left_drink2')
        mrk_trent_drink_low_arm_left_drink2 = self.get_automarker_name('mrk_trent_drink_low_arm_left_drink2')

        mrk_trent_drink_hand_drink = self.get_automarker_name('mrk_trent_drink_hand_drink')
        mrk_trent_drink_hand_drink2 = self.get_automarker_name('mrk_trent_drink_hand_drink2')
        mrk_trent_backspine = self.get_automarker_name('mrk_trent_backspine')
        mrk_trent_spine = self.get_automarker_name('mrk_trent_spine')


        mrk_look_trent_front = self.get_automarker_name('mrk_look_trent_front')
        mrk_look_trent_front2 = self.get_automarker_name('mrk_look_trent_front2')
        mrk_look_trent_front3 = self.get_automarker_name('mrk_look_trent_front3')

        mrk_look_edison_front = self.get_automarker_name('mrk_look_edison_front')
        mrk_look_edison_front2 = self.get_automarker_name('mrk_look_edison_front2')
        mrk_look_edison_front3 = self.get_automarker_name('mrk_look_edison_front3')
        mrk_look_edison_front4 = self.get_automarker_name('mrk_look_edison_front4')


        mrk_trent_bottom = self.get_automarker_name('mrk_trent_bottom')
        mrk_trent_bottom2 = self.get_automarker_name('mrk_trent_bottom2')
        mrk_trent_bottom3 = self.get_automarker_name('mrk_trent_bottom3')
        mrk_trent_bottom4 = self.get_automarker_name('mrk_trent_bottom4')
        mrk_trent_mid = self.get_automarker_name('mrk_trent_mid')
        mrk_trent_mid2 = self.get_automarker_name('mrk_trent_mid2')
        mrk_trent_mid3 = self.get_automarker_name('mrk_trent_mid3')
        mrk_trent_mid4 = self.get_automarker_name('mrk_trent_mid4')

        mrk_edison_front = self.get_automarker_name('mrk_edison_front')
        mrk_edison_left = self.get_automarker_name('mrk_edison_left')
        mrk_edison_left2 = self.get_automarker_name('mrk_edison_left2')
        mrk_edison_mid = self.get_automarker_name('mrk_edison_mid')
        mrk_edison_mid2 = self.get_automarker_name('mrk_edison_mid2')
        mrk_edison_right = self.get_automarker_name('mrk_edison_right')
        mrk_edison_right2 = self.get_automarker_name('mrk_edison_right2')

        mrk_drink = self.get_automarker_name('mrk_drink')
        mrk_drink_top = self.get_automarker_name('mrk_drink_top')


        # EXTRA DEFINITIONS

        trent.move_head_ik(group=BG, target_name=mrk_kim_table, immediately=True)
        trent.move_eye_ik(group=BG, target_name=mrk_kim_table, immediately=True)
        kim.move_head_ik(group=BG, target_name=mrk_kim_forward2, immediately=True)
        kim.move_eye_ik(group=BG, target_name=mrk_kim_forward2, immediately=True)
        edison.move_head_ik(group=BG, target_name=mrk_look_trent_front3, immediately=True)
        edison.move_eye_ik(group=BG, target_name=mrk_look_trent_front2, immediately=True)

        # junko.move_head_ik(group=BG, target_name=mrk_edison_front, immediately=True)
        # junko.move_eye_ik(group=BG, target_name=mrk_edison_talk, immediately=True)
        #
        kim.start_head_ik(group=MAIN, duration=1000)
        kim.start_eye_ik(group=MAIN, duration=1000)
        trent_head_ik1 = trent.start_head_ik(group=MAIN, duration=1000)
        trent_eye_ik1 = trent.start_eye_ik(group=MAIN, duration=1000)

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
        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, start_time=0, time_scale=0.9, trans_time=1, time_delay=-0.5)
        trent.motion(group=MAIN, duration=1, anim=Male.Sc_MLHAND_HNEUT_EDGE_LEFT_000LV_00, time_scale=0.6, trans_time=0.2, time_delay=-0.5)
        trent.motion(group=MAIN, duration=1, anim=Male.Sc_MLHAND_HNEUT_EDGE_RGHT_000LV_00, time_scale=0.6, trans_time=0.2, time_delay=-0.5)
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

        trent.move_head_ik(group=MAIN, target_name=mrk_kim_table2, duration=2.5, time_delay=3)
        trent.move_eye_ik(group=MAIN, target_name=mrk_kim_table2, duration=1.5, time_delay=3)

        trent.move_head_ik(group=MAIN, target_name=mrk_trent_angry_front, duration=2, time_delay=6)
        trent.move_eye_ik(group=MAIN, target_name=mrk_trent_angry_front, duration=0.5, time_delay=6)

        trent_head_ik1.set_duration(main_group.get_time() + 8)
        trent_eye_ik1.set_duration(main_group.get_time() + 8)

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





        # main_group.append_time(0.1)
        #
        #
        # main_group.append_time(1000)
        # self.set_start_time(main_group.get_time())

        # MoveFastEvent(root=self, group=MAIN, object_name=trent.name, target_name=self.get_automarker_name('trent_angry'))
        # trent.move_head_ik(group=MAIN, target_name=mrk_kim_away, duration=0.1, time_delay=0.1)
        # trent.move_eye_ik(group=MAIN, target_name=mrk_kim_away, duration=0.1, time_delay=0.1)

        # trent.motion(group=MAIN, duration=1, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, time_delay=0.1)

        # main_group.append_time(0.2)



        # cam_dbg.set(group=MAIN)
        cam_kim_leave.set(group=MAIN)
        cam_kim_leave.move_cam(group=MAIN, index=2, duration=12, smooth=True)
        cam_kim_leave.move_focus(group=MAIN, index=2, duration=12, smooth=True)


        ConnectHardpointEvent(root=self, group=MAIN, target_name=bottle_wine_bar.name, parent_name=bartender.name,
                              duration=61, target_hardpoint="HpRightConnect_prop_bottle_wine_1",
                              parent_hardpoint="HpRightConnect")

        ConnectHardpointEvent(root=self, group=MAIN, target_name=glass_bar.name, parent_name=bartender.name,
                              duration=61, target_hardpoint="HpLeftConnect_prop_glass_metal_1",
                              parent_hardpoint="hpleftconnect")

        conn_time = main_group.get_time()-7  # remove delay
        conn = ConnectHardpointEvent(root=self, group=MAIN, target_name=glass_trent.name, parent_name=trent.name,
                                     duration=61, target_hardpoint="HpLeftConnect_prop_glass_metal_1",
                                     parent_hardpoint="hpleftconnect", time_delay=7)


        bartender.motion(group=MAIN, duration=0.5, anim=Male.Sc_MLHAND_HNEUT_HOLDD_LEFT_000LV_00, time_scale=2, trans_time=0.25, time_delay=0)
        bartender.motion(group=MAIN, duration=0.5, anim=Male.Sc_MLHAND_HNEUT_HOLDD_RGHT_000LV_00, time_scale=2, trans_time=0.25, time_delay=0)

        bartender.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_GRABR_PRDRNK_BAR_000LV_XA_07)
        bartender.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_PUSH_DRINK_BAR_000LV_XA_05, trans_time=2, time_delay=3.5)
        bartender.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_WALK_TRNS_180LV_XA_02, trans_time=1, time_delay=8)


        MoveFastEvent(root=self, group=MAIN, object_name=edison.name, target_name=self.get_automarker_name('edison_go'), time_delay=2)
        edison.motion(group=MAIN, duration=12, loop=True, anim=Male.Sc_MLBODY_STROLL_000LV_XA_01, time_scale=1, time_delay=2)
        edison.motion(group=MAIN, duration=12, anim=Male.Sc_MLBODY_STROLL_STND_TRNS_000LV_XA_01, trans_time=0.5, time_scale=0.8, time_delay=10)
        edison.motion(group=MAIN, duration=12, anim=Male.Sc_MLBODY_STND_LEAN_BAR_TRNS_000LV_XA_02, trans_time=0.5, time_scale=0.8, time_delay=13)

        RotateAxisEvent(root=self, group=MAIN, object_name=edison.name, angle=-90, duration=2.1, smooth=True, time_delay=7.8)

        edison.start_head_ik(group=MAIN, duration=1000, time_delay=9)
        edison.start_eye_ik(group=MAIN, duration=1000, time_delay=9)

        edison.move_head_ik(group=MAIN, target_name=mrk_look_trent_front3, duration=2.5, time_delay=11)
        edison.move_eye_ik(group=MAIN, target_name=mrk_look_trent_front2, duration=1.5, time_delay=11)


        trent.move_head_ik(group=MAIN, target_name=mrk_trent_table, duration=3, time_delay=0.5)
        trent.move_eye_ik(group=MAIN, target_name=mrk_trent_table, duration=1.5, time_delay=0.3)

        trent.motion(group=MAIN, duration=5, anim=Male.Sc_MLBODY_STND_TURN_270LV_XA_04, time_delay=0.1)
        trent.motion(group=MAIN, duration=5, anim=Male.Sc_MLBODY_STND_LEAN_BAR_TRNS_000LV_XA_02, trans_time=0.3, time_delay=2.8)
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=-36, duration=1.5, smooth=True, time_delay=1.5)

        trent.motion(group=MAIN, duration=5, anim=Male.Sc_MLBODY_LEAN_STND_BAR_TRNS_000LV_XA_03, time_delay=4.5)
        trent.motion(group=MAIN, duration=5, anim=Male.Sc_MLBODY_STND_GRABL_DRINK_BAR_000LV_XA_06, start_time=1.5, trans_time=1, time_delay=6)

        trent.motion(group=MAIN, duration=1, anim=Male.Sc_MLHAND_HNEUT_HOLDD_LEFT_000LV_00, trans_time=0.25, time_delay=7)
        trent.motion(group=MAIN, duration=8, loop=True, anim=Male.Sc_MLBODY_STND_DRINK_LHND_LARG_000LV_XA_06, start_time=1, trans_time=1, time_delay=8)
        # trent.motion(group=MAIN, duration=2, anim=Male.Sc_MLBODY_STND_PUTDNL_DRINK_BAR_000LV_XA_06, start_time=1, trans_time=1, time_delay=9.8)

        MoveEvent(root=self, group=MAIN, object_name=trent.name, target_name=self.get_automarker_name('trent_drink'), duration=3, smooth=True, time_delay=2, adjust_orient=True)





        # trent.motion(group=MAIN, duration=5, anim=Male.BODYGRA, trans_time=0.3, time_delay=4.5)

        trent.facial(group=MAIN, index=60)


        main_group.append_time(8)

        edison.facial(group=MAIN, index=110)
        main_group.append_time(1)
        trent.facial(group=MAIN, index=120)
        main_group.append_time(1)



        cam_edison.set(group=MAIN)


        ### DBG!!

        #
        # conn_time = main_group.get_time()
        # conn = ConnectHardpointEvent(root=self, group=MAIN, target_name=glass_trent.name, parent_name=trent.name,
        #                              duration=61, target_hardpoint="HpLeftConnect_prop_glass_metal_1",
        #                              parent_hardpoint="hpleftconnect", time_delay=0)
        # edison.start_head_ik(group=MAIN, duration=1000, time_delay=0)
        # edison.start_eye_ik(group=MAIN, duration=1000, time_delay=0)
        # MoveFastEvent(root=self, group=MAIN, object_name=edison.name, target_name=self.get_automarker_name('edison_bar'))

        ### DBG!!


        edison.motion(group=MAIN, duration=1, anim=Male.Sc_MLBODY_STND_LEAN_HNDS_BAR_000LV_XA_01, time_scale=1)

        edison.move_head_ik(group=MAIN, target_name=mrk_look_trent_front2, duration=1.5, time_delay=1)
        edison.move_eye_ik(group=MAIN, target_name=mrk_look_trent_front, duration=0.5, time_delay=1)

        edison.move_head_ik(group=MAIN, target_name=mrk_look_trent_front3, duration=1.5, time_delay=4)
        edison.move_eye_ik(group=MAIN, target_name=mrk_look_trent_front, duration=0.5, time_delay=4)

        edison.motion(group=MAIN, duration=12, anim=Male.Sc_MLBODY_LEAN_STND_BAR_TRNS_000LV_XA_03, time_scale=1, time_delay=2)




        trent.start_head_ik(group=MAIN, duration=1000)
        trent.start_eye_ik(group=MAIN, duration=1000)


        # MoveEvent(root=self, group=MAIN, object_name=trent.name, target_name=self.get_automarker_name('trent_drink2'), duration=1, smooth=True, time_delay=-1.2)

        MoveFastEvent(root=self, group=MAIN, object_name=trent.name, target_name=self.get_automarker_name('trent_drink2'), time_delay=2)


        trent.move_head_ik(group=MAIN, target_name=mrk_trent_mid2, duration=0.1, time_delay=0.1)
        trent.move_eye_ik(group=MAIN, target_name=mrk_trent_bottom2, duration=0.1, time_delay=0.1)


        trent.motion(group=MAIN, duration=510, loop=True, anim=Male.Sc_MLBODY_STND_LEAN_HNDS_BAR_000LV_XA_01, time_delay=3)
        trent.motion(group=MAIN, duration=1, anim=Male.Sc_MLHAND_HNEUT_GESTR_FIST_000LV_00, time_delay=3)
        trent.motion(group=MAIN, duration=1, anim=Male.Sc_MLHAND_HNEUT_HOLDD_LEFT_000LV_00, start_time=1, time_delay=3)




        trent.move_ik(group=BG, ik_marker='LUpArm', target_name=mrk_trent_drink_top_arm_left, immediately=True)
        trent.move_ik(group=BG, ik_marker='LLowArm', target_name=mrk_trent_drink_low_arm_left, immediately=True)
        trent.move_ik(group=BG, ik_marker='RUpArm', target_name=mrk_trent_drink_top_arm_right, immediately=True)
        trent.move_ik(group=BG, ik_marker='RLowArm', target_name=mrk_trent_drink_low_arm_right, immediately=True)
        trent.move_ik(group=BG, ik_marker='LHand', target_name=mrk_trent_drink_hand_drink, immediately=True)


        edison.facial(group=MAIN, index=130)
        main_group.append_time(0.5)




        drinkins_time = main_group.get_time()
        cam_drinkins.set(group=MAIN)
        drinkins_time_mov1 = cam_drinkins.move_cam(group=MAIN, index=2, duration=14, smooth=True, time_delay=0)

        ik_start = main_group.get_time()
        ik1 = trent.start_ik(group=MAIN, ik_marker='LUpArm', duration=711,
                             end_effector="LUpArm", up=NEG_Y_AXIS, front=Z_AXIS, transition_duration=0.5, time_delay=-1.2)
        ik2 = trent.start_ik(group=MAIN, ik_marker='LLowArm', duration=711,
                             end_effector="LLowArm", up=Y_AXIS, front=Z_AXIS, transition_duration=0.5, time_delay=-1.2)

        ik3 = trent.start_ik(group=MAIN, ik_marker='RUpArm', duration=711,
                             end_effector="RUpArm", up=NEG_Y_AXIS, front=Z_AXIS, transition_duration=1, time_delay=-0.25)
        ik4 = trent.start_ik(group=MAIN, ik_marker='RLowArm', duration=711,
                             end_effector="RLowArm", up=Y_AXIS, front=Z_AXIS, transition_duration=1, time_delay=-0.25)

        trent.move_ik(group=MAIN, ik_marker='LUpArm', target_name=mrk_trent_drink_top_arm_left2,
                      duration=1.5, smooth=True, time_delay=2)

        trent.move_ik(group=MAIN, ik_marker='LUpArm', target_name=mrk_trent_drink_top_arm_left,
                      duration=1.8, smooth=True, time_delay=5)

        trent.move_ik(group=MAIN, ik_marker='LUpArm', target_name=mrk_trent_drink_top_arm_left2,
                      duration=1.2, smooth=True, time_delay=8)

        trent.move_ik(group=MAIN, ik_marker='LUpArm', target_name=mrk_trent_drink_top_arm_left,
                      duration=1.8, smooth=True, time_delay=10)

        trent.move_ik(group=MAIN, ik_marker='LUpArm', target_name=mrk_trent_drink_top_arm_left2,
                      duration=1.2, smooth=True, time_delay=12)


        trent.move_ik(group=MAIN, ik_marker='RUpArm', target_name=mrk_trent_drink_top_arm_right2,
                      duration=1.3, smooth=True, time_delay=3)

        trent.move_ik(group=MAIN, ik_marker='RUpArm', target_name=mrk_trent_drink_top_arm_right,
                      duration=1.57, smooth=True, time_delay=6)

        trent.move_ik(group=MAIN, ik_marker='RUpArm', target_name=mrk_trent_drink_top_arm_right2,
                      duration=1, smooth=True, time_delay=9.5)

        trent.move_ik(group=MAIN, ik_marker='RUpArm', target_name=mrk_trent_drink_top_arm_right,
                      duration=1.57, smooth=True, time_delay=11)

        trent.move_ik(group=MAIN, ik_marker='RUpArm', target_name=mrk_trent_drink_top_arm_right2,
                      duration=1, smooth=True, time_delay=14)

        trent.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=1.5, time_delay=1.1)
        trent.move_eye_ik(group=MAIN, target_name=mrk_trent_front, duration=0.5, time_delay=1.1)

        trent.move_head_ik(group=MAIN, target_name=mrk_look_edison_front4, duration=1.5, time_delay=3)
        trent.move_eye_ik(group=MAIN, target_name=mrk_look_edison_front, duration=0.5, time_delay=3)

        trent.move_head_ik(group=MAIN, target_name=mrk_trent_mid4, duration=1.5, time_delay=6)
        trent.move_eye_ik(group=MAIN, target_name=mrk_trent_mid4, duration=0.5, time_delay=6)

        trent.move_head_ik(group=MAIN, target_name=mrk_trent_mid2, duration=1.5, time_delay=8)
        trent.move_eye_ik(group=MAIN, target_name=mrk_trent_bottom2, duration=0.5, time_delay=8)

        trent.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=1.5, time_delay=11)
        trent.move_eye_ik(group=MAIN, target_name=mrk_trent_front, duration=0.5, time_delay=11)

        trent.move_head_ik(group=MAIN, target_name=mrk_trent_mid2, duration=1.5, time_delay=13)
        trent.move_eye_ik(group=MAIN, target_name=mrk_trent_bottom2, duration=0.5, time_delay=13)


        trent.facial(group=MAIN, index=140)
        trent.facial(group=MAIN, index=150)

        trent.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=1.5, time_delay=-1.5)
        trent.move_eye_ik(group=MAIN, target_name=mrk_trent_front, duration=0.5, time_delay=-1.5)

        trent.move_ik(group=MAIN, ik_marker='LUpArm',
                      target_name=mrk_trent_drink_top_arm_left_drink,
                      duration=1.5, smooth=True, time_delay=-1)

        trent.move_ik(group=MAIN, ik_marker='LLowArm',
                      target_name=mrk_trent_drink_low_arm_left_drink,
                      duration=1.5, smooth=True, time_delay=-1)

        trent.move_ik(group=MAIN, ik_marker='LLowArm',
                      target_name=mrk_trent_drink_low_arm_left_drink2,
                      duration=1, smooth=True, time_delay=0.5)

        trent.move_ik(group=MAIN, ik_marker='LUpArm',
                      target_name=mrk_trent_drink_top_arm_left_drink2,
                      duration=1, smooth=True, time_delay=0.5)

        trent.move_ik(group=MAIN, ik_marker='LUpArm',
                      target_name=mrk_trent_drink_top_arm_left,
                      duration=1.5, smooth=True, time_delay=2)

        trent.move_ik(group=MAIN, ik_marker='LLowArm',
                      target_name=mrk_trent_drink_low_arm_left,
                      duration=2, smooth=True, time_delay=2)


        trent.motion(group=MAIN, duration=8, anim=Trent.Sc_MLHEAD_MOTION_DRINK_SWALLOW_TRENT_000LV_XA_, trans_time=0.25, time_delay=-0.2)

        trent.move_head_ik(group=MAIN, target_name=mrk_trent_front2, duration=1.5, time_delay=0.5)
        trent.move_eye_ik(group=MAIN, target_name=mrk_trent_front2, duration=0.5, time_delay=0.5)

        trent.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=1.5, time_delay=1.5)
        trent.move_eye_ik(group=MAIN, target_name=mrk_trent_front, duration=0.5, time_delay=1.5)


        IkEvent(root=self, group=MAIN, char_name=trent.name, target_name=mrk_trent_drink_hand_drink, duration=3,
                end_effector="LHand", up=Y_AXIS, front=Z_AXIS, time_delay=-0.5, transition_duration=1)

        IkEvent(root=self, group=MAIN, char_name=trent.name, target_name=mrk_trent_spine, duration=3,
                end_effector="UpperTorso", up=NEG_Y_AXIS, front=Z_AXIS, time_delay=-0.5, transition_duration=2)


        trent.move_ik(group=MAIN, ik_marker='RLowArm',
                      target_name=mrk_trent_drink_low_arm_right_drink,
                      duration=1.5, smooth=True, time_delay=-0.5)


        trent.move_ik(group=MAIN, ik_marker='RLowArm',
                      target_name=mrk_trent_drink_low_arm_right,
                      duration=1.5, smooth=True, time_delay=2)

        main_group.append_time(3)


        trent.move_ik(group=MAIN, ik_marker='LUpArm', target_name=mrk_trent_drink_top_arm_left2,
                      duration=1.5, smooth=True, time_delay=2)

        trent.move_ik(group=MAIN, ik_marker='LUpArm', target_name=mrk_trent_drink_top_arm_left,
                      duration=1.8, smooth=True, time_delay=5)

        trent.move_ik(group=MAIN, ik_marker='LUpArm', target_name=mrk_trent_drink_top_arm_left2,
                      duration=1.2, smooth=True, time_delay=8)

        trent.move_ik(group=MAIN, ik_marker='LUpArm', target_name=mrk_trent_drink_top_arm_left,
                      duration=1.8, smooth=True, time_delay=10)

        trent.move_ik(group=MAIN, ik_marker='LUpArm', target_name=mrk_trent_drink_top_arm_left2,
                      duration=1.2, smooth=True, time_delay=12)


        trent.move_ik(group=MAIN, ik_marker='RUpArm', target_name=mrk_trent_drink_top_arm_right2,
                      duration=1.3, smooth=True, time_delay=3)

        trent.move_ik(group=MAIN, ik_marker='RUpArm', target_name=mrk_trent_drink_top_arm_right,
                      duration=1.57, smooth=True, time_delay=6)

        trent.move_ik(group=MAIN, ik_marker='RUpArm', target_name=mrk_trent_drink_top_arm_right2,
                      duration=1, smooth=True, time_delay=9.5)

        trent.move_ik(group=MAIN, ik_marker='RUpArm', target_name=mrk_trent_drink_top_arm_right,
                      duration=1.57, smooth=True, time_delay=11)

        trent.move_ik(group=MAIN, ik_marker='RUpArm', target_name=mrk_trent_drink_top_arm_right2,
                      duration=1, smooth=True, time_delay=14)

        trent.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=1.5, time_delay=1.1)
        trent.move_eye_ik(group=MAIN, target_name=mrk_trent_front, duration=0.5, time_delay=1.1)

        trent.move_head_ik(group=MAIN, target_name=mrk_look_edison_front4, duration=1.5, time_delay=3)
        trent.move_eye_ik(group=MAIN, target_name=mrk_look_edison_front, duration=0.5, time_delay=3)

        trent.move_head_ik(group=MAIN, target_name=mrk_trent_mid4, duration=1.5, time_delay=6)
        trent.move_eye_ik(group=MAIN, target_name=mrk_trent_mid4, duration=0.5, time_delay=6)

        trent.move_head_ik(group=MAIN, target_name=mrk_trent_mid2, duration=1.5, time_delay=8)
        trent.move_eye_ik(group=MAIN, target_name=mrk_trent_bottom2, duration=0.5, time_delay=8)

        trent.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=1.5, time_delay=11)
        trent.move_eye_ik(group=MAIN, target_name=mrk_trent_front, duration=0.5, time_delay=11)

        trent.move_head_ik(group=MAIN, target_name=mrk_trent_mid2, duration=1.5, time_delay=13)
        trent.move_eye_ik(group=MAIN, target_name=mrk_trent_bottom2, duration=0.5, time_delay=13)

        trent.facial(group=MAIN, index=160)
        trent.facial(group=MAIN, index=170)

        main_group.append_time(0.35)
        drinkins_time_mov1.set_duration(main_group.get_time() - drinkins_time)



        edison.motion(group=MAIN, duration=12, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, time_scale=1, time_delay=-2)

        edison_time = main_group.get_time()
        cam_edison.set(group=MAIN)
        edison_time_mov1 = cam_edison.move_cam(group=MAIN, index=2, duration=14, smooth=True)
        edison_time_mov2 = cam_edison.move_focus(group=MAIN, index=2, duration=14, smooth=True)


        edison.motion(group=MAIN, duration=12, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, time_scale=0.8)


        edison.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, time_scale=0.6, trans_time=1, time_delay=3)
        edison.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_STND_CONV_RHND_CASL_000LV_xa_01, time_scale=0.6, trans_time=1, time_delay=5)
        edison.motion(group=MAIN, duration=8, loop=True, anim=Male.Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00, time_scale=1, trans_time=0.5, time_delay=5)
        edison.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_02, time_scale=0.6, trans_time=0.5, time_delay=9)

        edison.move_head_ik(group=MAIN, target_name=mrk_look_trent_front3, duration=1.5, time_delay=0)
        edison.move_eye_ik(group=MAIN, target_name=mrk_look_trent_front, duration=0.5, time_delay=0)

        edison.facial(group=MAIN, index=180)

        edison.motion(group=MAIN, duration=1, anim=Male.Sc_MLHAND_NEUT_LEFT_000LV_A_00, time_scale=0.6, trans_time=0.2, time_delay=1)
        edison.motion(group=MAIN, duration=1, anim=Male.Sc_MLHAND_NEUT_RGHT_000LV_A_00, time_scale=0.6, trans_time=0.2, time_delay=1)

        edison.move_head_ik(group=MAIN, target_name=mrk_edison_front, duration=2, time_delay=-1)
        edison.move_eye_ik(group=MAIN, target_name=mrk_edison_left, duration=0.8, time_delay=-1)

        edison.motion(group=MAIN, duration=12, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, time_scale=0.8, trans_time=1, time_delay=2)

        edison.move_head_ik(group=MAIN, target_name=mrk_look_trent_front3, duration=1.5, time_delay=3)
        edison.move_eye_ik(group=MAIN, target_name=mrk_look_trent_front, duration=0.5, time_delay=3)

        edison.move_head_ik(group=MAIN, target_name=mrk_look_trent_front2, duration=1.5, time_delay=6)
        edison.move_eye_ik(group=MAIN, target_name=mrk_look_trent_front, duration=0.5, time_delay=6)

        edison.facial(group=MAIN, index=190)

        edison.move_head_ik(group=MAIN, target_name=mrk_look_trent_front3, duration=1.5, time_delay=-1)
        edison.move_eye_ik(group=MAIN, target_name=mrk_look_trent_front, duration=0.5, time_delay=-1)

        edison.motion(group=MAIN, duration=12, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, time_scale=0.8, trans_time=1, time_delay=2)

        edison.motion(group=MAIN, duration=12, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, time_scale=1, trans_time=0.5, time_delay=5)

        edison.facial(group=MAIN, index=200)

        edison.move_head_ik(group=MAIN, target_name=mrk_edison_right, duration=2, time_delay=-1)
        edison.move_eye_ik(group=MAIN, target_name=mrk_edison_mid2, duration=0.8, time_delay=-1)

        edison.motion(group=MAIN, duration=12, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, time_scale=0.8, trans_time=1, time_delay=2)
        edison.motion(group=MAIN, duration=12, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, time_scale=0.8, trans_time=1, time_delay=6)

        edison.move_head_ik(group=MAIN, target_name=mrk_look_trent_front3, duration=1.5, time_delay=3)
        edison.move_eye_ik(group=MAIN, target_name=mrk_look_trent_front, duration=0.5, time_delay=3)

        edison.move_head_ik(group=MAIN, target_name=mrk_look_trent_front2, duration=1.5, time_delay=6)
        edison.move_eye_ik(group=MAIN, target_name=mrk_look_trent_front, duration=0.5, time_delay=6)



        edison.facial(group=MAIN, index=210)

        edison.move_head_ik(group=MAIN, target_name=mrk_look_trent_front3, duration=1.5, time_delay=-1)
        edison.move_eye_ik(group=MAIN, target_name=mrk_look_trent_front, duration=0.5, time_delay=-1)

        edison.move_head_ik(group=MAIN, target_name=mrk_look_trent_front2, duration=1.5, time_delay=2)
        edison.move_eye_ik(group=MAIN, target_name=mrk_look_trent_front, duration=0.5, time_delay=2)


        edison.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_STND_CONV_HNDSUP_TRNS_000LV_XA_00, time_scale=0.6, trans_time=1, time_delay=1.5)
        edison.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_STND_CONV_HNDS_CASL_000LV_xa_04, time_scale=0.6, trans_time=1, time_delay=3)
        edison.motion(group=MAIN, duration=6, loop=True, anim=Male.Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00, time_scale=1, trans_time=0.5, time_delay=3)
        edison.motion(group=MAIN, duration=6, loop=True, anim=Male.Sc_MLHAND_HNEUT_GESTL_CASL_000LV_00, time_scale=1, trans_time=0.5, time_delay=3)
        edison.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_CONV_HNDSDN_TRNS_000LV_XA_01, time_scale=0.6, trans_time=0.5, time_delay=7)

        edison.move_head_ik(group=MAIN, target_name=mrk_look_trent_front3, duration=1.5, time_delay=4)
        edison.move_eye_ik(group=MAIN, target_name=mrk_look_trent_front, duration=0.5, time_delay=4)

        edison.move_head_ik(group=MAIN, target_name=mrk_look_trent_front2, duration=1.5, time_delay=7)
        edison.move_eye_ik(group=MAIN, target_name=mrk_look_trent_front, duration=0.5, time_delay=7)

        edison.facial(group=MAIN, index=220)

        edison.motion(group=MAIN, duration=1, anim=Male.Sc_MLHAND_NEUT_LEFT_000LV_A_00, time_scale=0.6, trans_time=0.2, time_delay=1)
        edison.motion(group=MAIN, duration=1, anim=Male.Sc_MLHAND_NEUT_RGHT_000LV_A_00, time_scale=0.6, trans_time=0.2, time_delay=1)

        edison.motion(group=MAIN, duration=12, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, time_scale=0.8, trans_time=1, time_delay=2)

        edison.move_head_ik(group=MAIN, target_name=mrk_look_trent_front3, duration=1.5, time_delay=-1)
        edison.move_eye_ik(group=MAIN, target_name=mrk_look_trent_front, duration=0.5, time_delay=-1)

        edison.move_head_ik(group=MAIN, target_name=mrk_look_trent_front2, duration=1.5, time_delay=2)
        edison.move_eye_ik(group=MAIN, target_name=mrk_look_trent_front, duration=0.5, time_delay=2)


        edison.move_head_ik(group=MAIN, target_name=mrk_look_trent_front3, duration=1.5, time_delay=4)
        edison.move_eye_ik(group=MAIN, target_name=mrk_look_trent_front, duration=0.5, time_delay=4)

        edison.move_head_ik(group=MAIN, target_name=mrk_look_trent_front2, duration=1.5, time_delay=7)
        edison.move_eye_ik(group=MAIN, target_name=mrk_look_trent_front, duration=0.5, time_delay=7)


        edison.facial(group=MAIN, index=230)

        edison.motion(group=MAIN, duration=12, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, time_scale=0.8, trans_time=1, time_delay=1)


        edison.motion(group=MAIN, duration=12, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, time_scale=0.8, trans_time=1, time_delay=4)

        edison.move_head_ik(group=MAIN, target_name=mrk_drink, duration=1.5, time_delay=3)
        edison.move_eye_ik(group=MAIN, target_name=mrk_drink, duration=0.5, time_delay=3)


        edison.facial(group=MAIN, index=240)

        edison.move_head_ik(group=MAIN, target_name=mrk_look_trent_front2, duration=1.5, time_delay=1)
        edison.move_eye_ik(group=MAIN, target_name=mrk_look_trent_front, duration=0.5, time_delay=1)


        edison_time_mov1.set_duration(main_group.get_time() - edison_time)
        edison_time_mov2.set_duration(main_group.get_time() - edison_time)


        main_group.append_time(0.35)

        cam_drinkins.set(group=MAIN)

        trent.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_LEAN_STND_BAR_TRNS_000LV_XA_03, trans_time=1, time_delay=0)
        trent.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, trans_time=1, time_delay=2)
        # trent.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_STND_PUTDNL_DRINK_BAR_000LV_XA_06, start_time=3, trans_time=1, time_delay=3)
        trent.motion(group=MAIN, duration=15, anim=Male.Sc_MLHAND_HNEUT_GESTL_CASL_000LV_00, trans_time=0.25, time_delay=1.5)

        ik3.set_duration(main_group.get_time()-ik_start)
        ik4.set_duration(main_group.get_time()-ik_start)
        ik1.set_duration(main_group.get_time()-ik_start)
        ik2.set_duration(main_group.get_time()+3-ik_start)

        conn.set_duration(main_group.get_time()+1.8-conn_time)


        trent.move_head_ik(group=MAIN, target_name=mrk_look_edison_front4, duration=2.5, time_delay=1)
        trent.move_eye_ik(group=MAIN, target_name=mrk_look_edison_front, duration=1, time_delay=1)

        main_group.append_time(1)


        trent.facial(group=MAIN, index=250)
        main_group.append_time(0.5)

        cam_edison.set(group=MAIN)


        edison.motion(group=MAIN, duration=12, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, time_scale=0.8)
        MoveOffscreenEvent(root=self, group=MAIN, object_name=glass_trent.name)
        edison.facial(group=MAIN, index=260)
        main_group.append_time(0.25)

        cam_ready.set(group=MAIN)


        trent.move_head_ik(group=MAIN, target_name=mrk_kim_table, duration=1.5, time_delay=1)
        trent.move_eye_ik(group=MAIN, target_name=mrk_edison_bar, duration=0.5, time_delay=1)

        MoveFastEvent(root=self, group=MAIN, object_name=trent.name, target_name=self.get_automarker_name('trent_drink'))
        trent.motion(group=MAIN, duration=5, anim=Male.Sc_MLBODY_STND_TURN_045LV_XA_04)
        trent.facial(group=MAIN, index=270)
        main_group.append_time(1)

        cam_final.set(group=MAIN)

        edison.move_head_ik(group=MAIN, target_name=mrk_trent_drink, duration=2.5, time_delay=1)
        edison.move_eye_ik(group=MAIN, target_name=mrk_trent_drink, duration=1, time_delay=1)


        trent.move_head_ik(group=MAIN, target_name=mrk_kim_away, duration=1.5, time_delay=1)
        trent.move_eye_ik(group=MAIN, target_name=mrk_kim_away, duration=0.5, time_delay=1)


        edison.motion(group=MAIN, duration=5, anim=Male.Sc_MLBODY_STND_TURN_270LV_XA_04, trans_time=0.5)
        trent.motion(group=MAIN, duration=5, anim=Male.Sc_MLBODY_STND_TURN_090LV_XA_02, time_delay=1.5)
        edison.facial(group=MAIN, index=280)
        main_group.append_time(0.5)



        # main_group.append_time(1000)
