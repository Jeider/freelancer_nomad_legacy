from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import Male, Female

from story import actors


class DjBoard(Prop):
    COMPOUND_TEMPLATE_NAME = 'dj_board'


OVERRIDES = {
    'hassler_talk': (0, 150, 0),
    'trent_talk': (0, 135, 0),
    'darcy_talk': (0, 45, 0),
    'bottle_wine_1': (90, 0, 0),
    'tenji_glass': (90, 0, 0),
    'trent_glass': (90, 0, 0),
    'dj_board': (0, 180, 0),
    'tenji_dancer': (0, 0, 0),
    'hassler_dancer': (0, 70, 0),
    'trent_dancer': (0, 180, 0),
    'darcy_dancer': (0, 90, 0),
}


class Msn9OrderCutsceneThorn(Scene):
    SCENE_AMBIENT = [30, 30, 10]
    POINT_ROTATE_OVERRIDES = OVERRIDES

    def action(self):
        main_group = self.get_group(MAIN)

        music = Music(root=self, name='main_music', sound='music_bar_ku_palace', attenuation=0)
        music.start(group=BG, duration=1000, loop=True)

        DjBoard(root=self, name='dj_board', init_point='dj_board', light_group=9, matrix_scale=1.75)

        dancepoint_floor_height = self.get_point('dancepoint_floor').position[1]
        # spot_ambi = [0.3, 0.3, 0.1]
        start_diffuse = [0.7, 0.4, 0.1]
        start_diffuse_simple = [0.15, 0.05, 0.05]
        end_diffuse = [0, 0, 0]

        # CAMERAS

        cam_dbg = LookAtCamera(root=self, name='cam_dbg', fov=40)
        cam_start = LookAtCamera(root=self, name='cam_start', fov=35)
        cam_dance = LookAtCamera(root=self, name='cam_dance', fov=40)
        cam_hassler = LookAtCamera(root=self, name='cam_hassler', fov=20)
        cam_tenji = LookAtCamera(root=self, name='cam_tenji', fov=20)
        cam_tenji_near = LookAtCamera(root=self, name='cam_tenji_near', fov=18)
        cam_friends = LookAtCamera(root=self, name='cam_friends', fov=24)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=16)
        cam_darcy = LookAtCamera(root=self, name='cam_darcy', fov=16)

        light_anim_repeat = 400

        lt_room = Light(root=self, name='ROOMA', point_name='light_bartable', light_group=9, diffuse=[0, 0, 0],
                        ambient=[0.6, 0.8, 0.3], direction=[0, 0, -1], light_type=L_POINT, range=3)

        lt_room1 = Light(root=self, name='ROOM1', point_name='light1', light_group=9, diffuse=end_diffuse,
                         ambient=[0, 0, 0], direction=[0, 0, 1], light_type=L_POINT, range=6)

        lt_room2 = Light(root=self, name='ROOM2', point_name='light2', light_group=9, diffuse=start_diffuse,
                         ambient=[0, 0, 0], direction=[1, 0, 0], light_type=L_POINT, range=6)

        lt_room3 = Light(root=self, name='ROOM3', point_name='light3', light_group=9, diffuse=end_diffuse,
                         ambient=[0, 0, 0], direction=[-1, 0, 0], light_type=L_POINT, range=6)


        lt_room1b = Light(root=self, name='ROOM1b', point_name='light1', light_group=0, diffuse=end_diffuse,
                          ambient=[0, 0, 0], direction=[0, 0, 1], light_type=L_POINT, range=6)

        lt_room2b = Light(root=self, name='ROOM2b', point_name='light2', light_group=0, diffuse=start_diffuse_simple,
                          ambient=[0, 0, 0], direction=[1, 0, 0], light_type=L_POINT, range=6)

        lt_room3b = Light(root=self, name='ROOM3b', point_name='light3', light_group=0, diffuse=end_diffuse,
                         ambient=[0, 0, 0], direction=[-1, 0, 0], light_type=L_POINT, range=6)

        lt_room4b = Light(root=self, name='ROOM4b', point_name='light4', light_group=0, diffuse=start_diffuse,
                          ambient=[0, 0, 0], direction=[-1, 0, 0], light_type=L_POINT, range=6)

        lt_table1 = Light(root=self, name='TABLE1', light_group=15, diffuse=[0.5, 0.4, 0.3],
                          ambient=[0, 0, 0], direction=[1, 0, 0], light_type=L_DIRECT, range=2000)
        RotateAxisEvent(root=self, group=BG, object_name=lt_table1.name, angle=-45, duration=0.01, smooth=False)

        lt_table2 = Light(root=self, name='TABLE2', light_group=18, diffuse=[0.7, 0.5, 0.4],
                          ambient=[0.18, 0.1, 0.1], direction=[1, 0, 0], light_type=L_DIRECT, range=2000)

        lt_hassler = Light(root=self, name='HASSL', light_group=0, diffuse=[0.7, 0.6, 0.5],
                          ambient=[0.18, 0.1, 0.1], direction=[1, 0, 0], light_type=L_DIRECT, range=2000, on=False)

        # lt_room1.animate_ambient(BG, 'lt_room1_anim1', start_ambient=spot_ambi_off, end_ambient=spot_ambi,
        #                          duration=3, gap=1, smooth=True, repeat=3)
        lt_room1.animate_diffuse(BG, 'lt_room1_anim1', start_diffuse=end_diffuse, end_diffuse=start_diffuse,
                                 duration=0.6, start_gap=0.07, end_gap=0.15, smooth=True, repeat=light_anim_repeat)
        lt_room2.animate_diffuse(BG, 'lt_room2_anim1', start_diffuse=start_diffuse, end_diffuse=end_diffuse,
                                 duration=0.5, start_gap=0.05, end_gap=0.1, smooth=True, repeat=light_anim_repeat)
        lt_room3.animate_diffuse(BG, 'lt_room3_anim1', start_diffuse=start_diffuse, end_diffuse=end_diffuse,
                                 duration=0.4, start_gap=0.03, end_gap=0.08, smooth=True, repeat=light_anim_repeat)
        # lt_room2.animate_range(BG, 'lt_room2_anim2', start_range=6, end_range=5,
        #                          duration=2, gap=0, smooth=True, repeat=50)


        lt_room1b.animate_diffuse(BG, 'lt_room1b_anim1', start_diffuse=end_diffuse, end_diffuse=start_diffuse_simple,
                                  duration=0.6, start_gap=0.07, end_gap=0.15, smooth=True, repeat=light_anim_repeat)
        lt_room2b.animate_diffuse(BG, 'lt_room2b_anim1', start_diffuse=start_diffuse_simple, end_diffuse=end_diffuse,
                                  duration=0.5, start_gap=0.05, end_gap=0.1, smooth=True, repeat=light_anim_repeat)
        lt_room3b.animate_diffuse(BG, 'lt_room3b_anim1', start_diffuse=start_diffuse_simple, end_diffuse=end_diffuse,
                                  duration=0.4, start_gap=0.03, end_gap=0.08, smooth=True, repeat=light_anim_repeat)
        lt_room4b.animate_diffuse(BG, 'lt_room4b_anim1', start_diffuse=start_diffuse_simple, end_diffuse=start_diffuse,
                                  duration=0.6, start_gap=0.07, end_gap=0.15, smooth=True, repeat=light_anim_repeat)


        lt_dancepoint_indx = Light(root=self, name='DANCE1', light_group=90, diffuse=[1, 1, 1],
                                   ambient=[1, 0.6, 0.6], direction=[0, 0, 1]).get_index()
        lt_dancelook1_indx = Light(root=self, name='DANCE2', light_group=91, diffuse=[1, 0.2, 0.2],
                                   ambient=[0.1, 0.1, 0.1], direction=[0, 0, -1]).get_index()
        lt_dancelook2_indx = Light(root=self, name='DANCE3', light_group=92, diffuse=[1, 0.2, 0.2],
                                   ambient=[0.1, 0.1, 0.1], direction=[1, 0, 0]).get_index()
        lt_dancelook3_indx = Light(root=self, name='DANCE4', light_group=93, diffuse=[1, 0.2, 0.2],
                                   ambient=[0.1, 0.1, 0.1], direction=[0, 0, 1]).get_index()

        discoball1 = Alchemy(root=self, name='disco_fx1', particles='discobeam', point_name='discobeam1')
        discoball1.start(group=BG, duration=5000)
        RotateAxisEvent(root=self, group=BG, object_name=discoball1.name, angle=36000, duration=5000, smooth=False)

        # PROPS

        tenji_bottle = BottleWine(root=self, name='tenji_bottle', init_point='bottle_wine_1', light_group=0)
        tenji_glass = Glass(root=self, name='tenji_glass', init_point='tenji_glass', light_group=0)
        trent_glass = Glass(root=self, name='trent_glass', init_point='trent_glass', light_group=0)

        # CHARACTERS

        darcy = Character(root=self, actor=actors.Darcy, light_group=0, init_point='darcy_init', rotate_y=90,
                          floor_height=0)
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='trent_init', rotate_y=90,
                          floor_height=0)
        hassler = Character(root=self, actor=actors.HasslerOrder, light_group=0, init_point='hassler_init', rotate_y=90)


        tekagi = Character(root=self, actor=actors.TekagiDj, light_group=0, init_point='tekagi_dj', rotate_y=180)
        tekagi.motion(group=BG, duration=5000, loop=True, anim=Male.Sc_MLBODY_STND_WIPE_BAR_000LV_XA_14)

        tenji = Character(root=self, actor=actors.Yamamoto, light_group=0, init_point='yamamoto_init', rotate_y=-45, use_ambient=False)
        tenji.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05)

        dancepoint = Character(root=self, actor=actors.YokoDancepoint, light_group=lt_dancepoint_indx,
                               init_point='dancepoint', rotate_y=110,
                               floor_height=dancepoint_floor_height, use_ambient=True)
        dancelook1 = Character(root=self, actor=actors.YokoDancelook1, light_group=lt_dancelook1_indx,
                               init_point='dancelook1', rotate_y=-130,
                               floor_height=0, use_ambient=True)
        dancelook2 = Character(root=self, actor=actors.YokoDancelook2, light_group=lt_dancelook2_indx,
                               init_point='dancelook2', rotate_y=-90,
                               floor_height=0, use_ambient=True)
        dancelook3 = Character(root=self, actor=actors.YokoDancelook3, light_group=lt_dancelook3_indx,
                               init_point='dancelook3', rotate_y=-50,
                               floor_height=0, use_ambient=True)

        group_dancepoint = 'bg_dancepoint'
        self.add_group(group_dancepoint, group_type=BG_GROUP)

        dancepoint.motion(group=group_dancepoint, duration=1, anim=Female.Sc_FMBODY_STND_DANC_000LV_A_20, start_time=1.9, time_append=0.1)
        dancepoint.motion(group=group_dancepoint, duration=20, repeat=50, anim=Female.Sc_FMBODY_STND_DANC_000LV_A_20, start_time=2, time_append=15, trans_time=1)

        dancelook1.motion(group=BG, duration=1000, loop=True, anim=Male.Sc_MLBODY_STLF_000LV_A_27, start_time=3)
        dancelook2.motion(group=BG, duration=1000, loop=True, anim=Male.Sc_MLBODY_STLB_LSTN_090LV_A_19)
        dancelook3.motion(group=BG, duration=1000, loop=True, anim=Male.Sc_MLBODY_STLF_000LV_A_27)

        dancepoint_lookat = self.get_automarker_name('dancepoint_lookat')

        NeckIkEvent(root=self, group=MAIN, char_name=dancelook1.name, target_name=dancepoint_lookat,
                    duration=3000, transition_duration=1)
        NeckIkEvent(root=self, group=MAIN, char_name=dancelook2.name, target_name=dancepoint_lookat,
                    duration=3000, transition_duration=1)
        NeckIkEvent(root=self, group=MAIN, char_name=dancelook3.name, target_name=dancepoint_lookat,
                    duration=3000, transition_duration=1)

        dancer1 = Character(root=self, actor=actors.YokohamaDancer1, light_group=0, init_point='dancer1', rotate_y=180)
        dancer2 = Character(root=self, actor=actors.YokohamaDancer2, light_group=0, init_point='dancer2', rotate_y=0)
        dancer3 = Character(root=self, actor=actors.YokohamaDancer3, light_group=0, init_point='dancer3', rotate_y=180)
        dancer4 = Character(root=self, actor=actors.YokohamaDancer4, light_group=0, init_point='dancer4', rotate_y=0)
        dancer5 = Character(root=self, actor=actors.YokohamaDancer5, light_group=0, init_point='dancer5', rotate_y=145)


        table1 = Character(root=self, actor=actors.YokohamaTable1, light_group=lt_table1.light_group, init_point='table1', rotate_y=135, use_ambient=True)
        table2 = Character(root=self, actor=actors.YokohamaTable2, light_group=lt_table1.light_group, init_point='table2', rotate_y=-45, use_ambient=True)
        table3 = Character(root=self, actor=actors.YokohamaTable3, light_group=lt_table2.light_group, init_point='table3', rotate_y=-45)
        table4 = Character(root=self, actor=actors.YokohamaTable4, light_group=lt_table2.light_group, init_point='table4', rotate_y=-135)
        table5 = Character(root=self, actor=actors.YokohamaTable5, light_group=lt_table2.light_group, init_point='table5', rotate_y=80)
        table6 = Character(root=self, actor=actors.YokohamaTable6, light_group=0, init_point='table6', rotate_y=-10)

        table1.motion(group=BG, duration=1000, loop=True, anim=Female.Sc_FMBODY_CHRF_IDLE_BIG_000LV_XA_05)
        table2.motion(group=BG, duration=1000, loop=True, anim=Female.Sc_FMBODY_CHRB_IDLE_BIG_000LV_XA_05)
        table3.motion(group=BG, duration=1000, loop=True, anim=Male.Sc_MLBODY_CHRF_IDLE_BIG_000LV_XA_06)
        table4.motion(group=BG, duration=1000, loop=True, anim=Male.Sc_MLBODY_CHRB_IDLE_BIG_000LV_XA_05)
        table5.motion(group=BG, duration=30, loop=True, anim=Male.Sc_MLBODY_STLB_LSTN_090LV_A_19, start_time=3)
        table5.motion(group=BG, duration=1000, loop=True, anim=Male.Sc_MLBODY_STLF_000LV_A_27, time_delay=30)
        table6.motion(group=BG, duration=1000, loop=True, anim=Female.Sc_FMBODY_STLB_000LV_A_21)

        group_dancer1 = 'bg_dancer1'
        self.add_group(group_dancer1, group_type=BG_GROUP)

        group_dancer2 = 'bg_dancer2'
        self.add_group(group_dancer2, group_type=BG_GROUP)

        group_dancer3 = 'bg_dancer3'
        self.add_group(group_dancer3, group_type=BG_GROUP)

        group_dancer4 = 'bg_dancer4'
        self.add_group(group_dancer4, group_type=BG_GROUP)

        group_dancer5 = 'bg_dancer5'
        self.add_group(group_dancer5, group_type=BG_GROUP)


        dancer1.motion(group=group_dancer1, duration=1, anim=Male.Sc_MLBODY_STND_DANC_000LV_A_28, start_time=1.9, time_append=0.1)
        dancer1.motion(group=group_dancer1, duration=20, repeat=50, anim=Male.Sc_MLBODY_STND_DANC_000LV_A_28, start_time=2, time_append=15, trans_time=1)

        dancer2.motion(group=group_dancer2, duration=1, anim=Female.Sc_FMBODY_STND_DANC_000LV_A_20, start_time=1.9, time_append=0.1)
        dancer2.motion(group=group_dancer2, duration=20, repeat=50, anim=Female.Sc_FMBODY_STND_DANC_000LV_A_20, start_time=2, time_append=15, trans_time=1)

        dancer3.motion(group=group_dancer3, duration=1, anim=Female.Sc_FMBODY_STND_DANC_000LV_A_20, start_time=1.9, time_append=0.1)
        dancer3.motion(group=group_dancer3, duration=20, repeat=50, anim=Female.Sc_FMBODY_STND_DANC_000LV_A_20, start_time=2, time_append=15, trans_time=1)

        dancer4.motion(group=group_dancer4, duration=1, anim=Male.Sc_MLBODY_STND_DANC_000LV_A_28, start_time=1.9, time_append=0.1)
        dancer4.motion(group=group_dancer4, duration=20, repeat=50, anim=Male.Sc_MLBODY_STND_DANC_000LV_A_28, start_time=2, time_append=15, trans_time=1)

        dancer5.motion(group=group_dancer5, duration=1, anim=Male.Sc_MLBODY_STND_DANC_000LV_A_28, start_time=1.9, time_append=0.1)
        dancer5.motion(group=group_dancer5, duration=20, repeat=50, anim=Male.Sc_MLBODY_STND_DANC_000LV_A_28, start_time=2, time_append=15, trans_time=1)

        # MARKERS

        mrk_tenji_sit = trent.get_sit_marker('yamamoto_init')
        mrk_trent_sit = trent.get_sit_marker('trent_talk')
        mrk_darcy_sit = darcy.get_sit_marker('darcy_talk')

        mrk_tenji_front = self.get_automarker_name('yamamoto_front')
        mrk_tenji_to_trent = self.get_automarker_name('yamamoto_trentlook')
        mrk_darcy_front = self.get_automarker_name('darcy_front')
        mrk_trent_front = self.get_automarker_name('darcy_looktrent')
        mrk_go_start = self.get_automarker_name('go_start')
        mrk_go_end = self.get_automarker_name('go_end')


        # DANCING VERSION

        # main_group.append_time(1)
        #
        # cam_dance.set(group=MAIN)
        #
        #
        # tenji_dancer1 = 'tj_dancer1'
        # self.add_group(tenji_dancer1, group_type=BG_GROUP)
        #
        # trent_dancer1 = 'tr_dancer1'
        # self.add_group(trent_dancer1, group_type=BG_GROUP)
        #
        # darcy_dancer1 = 'dr_dancer1'
        # self.add_group(darcy_dancer1, group_type=BG_GROUP)
        #
        # hassler_dancer1 = 'hs_dancer1'
        # self.add_group(hassler_dancer1, group_type=BG_GROUP)
        #
        #
        # MoveFastEvent(root=self, group=MAIN, object_name=tenji.name, target_name=self.get_automarker_name('tenji_dancer'),
        #               adjust_pos=True)
        #
        # tenji.motion(group=tenji_dancer1, duration=1, anim=Male.Sc_MLBODY_STND_DANC_000LV_A_28, start_time=1.9, time_append=0.1)
        # tenji.motion(group=tenji_dancer1, duration=20, repeat=50, anim=Male.Sc_MLBODY_STND_DANC_000LV_A_28, start_time=2, time_append=15, trans_time=1)
        #
        # MoveFastEvent(root=self, group=MAIN, object_name=trent.name, target_name=self.get_automarker_name('trent_dancer'),
        #               adjust_pos=True)
        #
        # trent.motion(group=trent_dancer1, duration=1, anim=Male.Sc_MLBODY_STND_DANC_000LV_A_28, start_time=1.9, time_append=0.1)
        # trent.motion(group=trent_dancer1, duration=20, repeat=50, anim=Male.Sc_MLBODY_STND_DANC_000LV_A_28, start_time=2, time_append=15, trans_time=1)
        #
        # MoveFastEvent(root=self, group=MAIN, object_name=darcy.name, target_name=self.get_automarker_name('darcy_dancer'),
        #               adjust_pos=True)
        #
        # darcy.motion(group=darcy_dancer1, duration=1, anim=Female.Sc_FMBODY_STND_DANC_000LV_A_20, start_time=1.9, time_append=0.1)
        # darcy.motion(group=darcy_dancer1, duration=20, repeat=50, anim=Female.Sc_FMBODY_STND_DANC_000LV_A_20, start_time=2, time_append=15, trans_time=1)
        #
        #
        # MoveFastEvent(root=self, group=MAIN, object_name=hassler.name, target_name=self.get_automarker_name('hassler_dancer'),
        #               adjust_pos=True)
        #
        # hassler.motion(group=hassler_dancer1, duration=1, anim=Male.Sc_MLBODY_STND_DANC_000LV_A_28, start_time=1.9, time_append=0.1)
        # hassler.motion(group=hassler_dancer1, duration=20, repeat=50, anim=Male.Sc_MLBODY_STND_DANC_000LV_A_28, start_time=2, time_append=15, trans_time=1)
        #
        #
        #
        # main_group.append_time(1)
        #
        # music.start(group=MAIN, duration=1000, loop=True)
        #
        # cam_dance.move_cam(group=MAIN, index=2, duration=30, smooth=True)
        # cam_dance.move_focus(group=MAIN, index=2, duration=30, smooth=True)
        # main_group.append_time(30)
        #
        # cam_dance.move_cam(group=MAIN, index=3, duration=30, smooth=True)
        # cam_dance.move_focus(group=MAIN, index=3, duration=30, smooth=True)
        # main_group.append_time(30)
        #
        # cam_dance.move_cam(group=MAIN, index=4, duration=30, smooth=True)
        # cam_dance.move_focus(group=MAIN, index=4, duration=30, smooth=True)
        # main_group.append_time(30)
        # # cam_dance.move_cam(group=MAIN, index=2, duration=30, smooth=True)
        # # cam_dance.move_focus(group=MAIN, index=2, duration=30, smooth=True)
        #
        #
        # main_group.append_time(1000)
        #
        #
        #
        # return

        #
        # DANCING VERSION ENDS


        cam_start.set(group=MAIN)

        cam_start.move_cam(group=MAIN, index=2, duration=20, smooth=True)
        cam_start.move_focus(group=MAIN, index=2, duration=20, smooth=True)

        #
        # cam_start.move_cam(group=MAIN, index=2, duration=2, smooth=True)
        # cam_start.move_focus(group=MAIN, index=2, duration=2, smooth=True)

        main_group.append_time(7)

        trent.motion(group=MAIN, duration=21, loop=True, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01)
        darcy.motion(group=MAIN, duration=21, loop=True, anim=Female.Sc_FMBODY_WLKG_000LV_XA_01, time_scale=0.9)
        hassler.motion(group=MAIN, duration=21, loop=True, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01)

        hassler_walk = 'hassler_walk'
        self.clone_group(hassler_walk, MAIN)

        RotateAxisEvent(root=self, group=hassler_walk, object_name=hassler.name, angle=-60, duration=2, smooth=True, time_delay=3)
        RotateAxisEvent(root=self, group=hassler_walk, object_name=hassler.name, angle=30, duration=2, smooth=True, time_delay=8)

        RotateAxisEvent(root=self, group=hassler_walk, object_name=darcy.name, angle=-55, duration=2, smooth=True, time_delay=5.5)
        RotateAxisEvent(root=self, group=hassler_walk, object_name=darcy.name, angle=30, duration=2, smooth=True, time_delay=9.5)

        RotateAxisEvent(root=self, group=hassler_walk, object_name=trent.name, angle=-55, duration=2, smooth=True, time_delay=6)
        RotateAxisEvent(root=self, group=hassler_walk, object_name=trent.name, angle=30, duration=2, smooth=True, time_delay=11.5)


        main_group.append_time(17)

        trent.motion(group=MAIN, duration=1, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06)
        darcy.motion(group=MAIN, duration=1, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05)
        hassler.motion(group=MAIN, duration=1, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)



        cam_tenji.set(group=MAIN)

        tenji.move_head_ik(group=MAIN, target_name=mrk_go_start, immediately=True, time_delay=-3)
        tenji.start_head_ik(group=MAIN, duration=6, time_delay=-1)
        tenji.move_head_ik(group=MAIN, target_name=mrk_go_end, duration=4, smooth=True)

        main_group.append_time(4)


        MoveFastEvent(root=self, group=MAIN, object_name=hassler.name, target_name=self.get_automarker_name('hassler_talk'),
                      adjust_pos=True)


        music.change_attenuation(group=MAIN, duration=3, attenuation=-14, time_delay=-1)
        lt_hassler.turn_on(group=MAIN)
        hassler.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_A_11, time_scale=0.5, start_time=1)
        cam_hassler.set(group=MAIN)

        main_group.append_time(0.5)

        hassler.facial(group=MAIN, index=10)


        main_group.append_time(1)


        lt_hassler.turn_off(group=MAIN)



        MoveFastEvent(root=self, group=MAIN, object_name=trent.name, target_name=self.get_automarker_name('trent_talk'),
                      adjust_pos=True)
        MoveFastEvent(root=self, group=MAIN, object_name=darcy.name, target_name=self.get_automarker_name('darcy_talk'),
                      adjust_pos=True)

        hassler.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, time_scale=0.5)
        trent.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, time_scale=0.5)
        tenji.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, time_scale=1,  trans_time=1)
        darcy.motion(group=MAIN, duration=1000, loop=True, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, time_scale=0.5, time_delay=0.1)


        trent.move_head_ik(group=MAIN, target_name=mrk_tenji_to_trent, immediately=True)

        darcy.move_head_ik(group=MAIN, target_name=mrk_tenji_front, immediately=True)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_tenji_sit, immediately=True)
        darcy.start_head_ik(group=MAIN, duration=1000, time_delay=1)
        darcy.start_eye_ik(group=MAIN, duration=1000, time_delay=1)

        # main_group.append_time(1)

        #
        # tenji.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_CHRB_GRABR_PRDRNK_TABL_000LV_XA_08, time_scale=0.8, trans_time=1)
        # ConnectHardpointEvent(root=self, group=MAIN, target_name=tenji_bottle.name, parent_name=tenji.name,
        #                       duration=6, target_hardpoint="HpRightConnect_prop_bottle_wine_1",
        #                       parent_hardpoint="HpRightConnect", time_delay=2)

        #
        # tenji.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_CHRB_GRABL_DRINK_TABL_000LV_XA_02, time_scale=1, trans_time=1)
        # tenji.motion(group=MAIN, duration=0.2, anim=Male.Sc_MLHAND_HNEUT_HOLDD_LEFT_000LV_00, time_scale=10, trans_time=0.25)
        #
        # grab_time = main_group.get_time()
        # conn = ConnectHardpointEvent(root=self, group=MAIN, target_name=tenji_glass.name, parent_name=tenji.name,
        #                               duration=6, target_hardpoint="hpleftconnect_prop_glass_green",
        #                               parent_hardpoint="hpleftconnect", time_delay=3)
        #
        # main_group.append_time(4)
        #
        # print(grab_time)
        # print(main_group.get_time())
        #
        #
        # conn.set_duration(main_group.get_time() - grab_time)
        # print(conn.duration)
        # tenji.motion(group=MAIN, duration=1, anim=Male.Sc_MLHAND_NEUT_LEFT_000LV_A_00, time_scale=0.01, trans_time=0.25, time_delay=3)
        # tenji.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_CHRB_PUTDNL_DRINK_TABL_000LV_XA_06, time_scale=0.8, trans_time=1)
        #
        #
        # return






        cam_tenji_near.set(group=MAIN)

        tenji.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_CHRB_GRABL_DRINK_TABL_000LV_XA_02, time_scale=1, time_delay=3, trans_time=1)
        tenji.motion(group=MAIN, duration=0.2, anim=Male.Sc_MLHAND_HNEUT_HOLDD_LEFT_000LV_00, time_scale=10, trans_time=0.25)
        tenji.motion(group=MAIN, loop=True, duration=15, anim=Male.Sc_MLBODY_CHRB_HOLDD_TABL_000LV_XA_02, time_scale=0.8, trans_time=2, time_delay=8)

        grab_time1 = main_group.get_time()
        conn1 = ConnectHardpointEvent(root=self, group=MAIN, target_name=tenji_glass.name, parent_name=tenji.name,
                                      duration=6, target_hardpoint="hpleftconnect_prop_glass_green",
                                      parent_hardpoint="hpleftconnect", time_delay=6)

        tenji.facial(group=MAIN, index=20)

        tenji.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_CHRB_DRINK_LHND_SIP_000LV_XA_04, time_scale=1, time_delay=-1, trans_time=1)

        main_group.append_time(3)

        conn1.set_duration(main_group.get_time() - grab_time1 - 3)
        tenji.motion(group=MAIN, duration=1, anim=Male.Sc_MLHAND_NEUT_LEFT_000LV_A_00, time_scale=0.01, trans_time=0.25, time_delay=3)
        tenji.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_CHRB_PUTDNL_DRINK_TABL_000LV_XA_06, time_scale=0.8, trans_time=1)

        tenji.facial(group=MAIN, index=30)


        tenji.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_CHRB_GRABR_PRDRNK_TABL_000LV_XA_08, time_scale=0.8, time_delay=-2, trans_time=1)
        tenji.motion(group=MAIN, duration=0.2, anim=Male.Sc_MLHAND_HNEUT_HOLDD_RGHT_000LV_00, time_scale=10, trans_time=0.25)
        ConnectHardpointEvent(root=self, group=MAIN, target_name=tenji_bottle.name, parent_name=tenji.name,
                              duration=6, target_hardpoint="HpRightConnect_prop_bottle_wine_1",
                              parent_hardpoint="HpRightConnect", time_delay=0)

        tenji.facial(group=MAIN, index=40)

        tenji.move_head_ik(group=MAIN, target_name=mrk_trent_sit, immediately=True)
        tenji.start_head_ik(group=MAIN, duration=20, time_delay=1)

        tenji.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_CHRB_CONV_LHNDUP_TRNS_000LV_XA_02, time_scale=0.8, trans_time=1)
        tenji.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_CHRB_CONV_LHNDDN_TRNS_000LV_XA_02, time_scale=0.5, time_delay=2, trans_time=0.5)

        tenji.move_head_ik(group=MAIN, target_name=mrk_darcy_front, duration=4, time_delay=2)

        tenji.facial(group=MAIN, index=50)

        cam_friends.set(group=MAIN)

        darcy.facial(group=MAIN, index=60)

        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_CHRB_GRABL_DRINK_TABL_000LV_XA_02, time_scale=1, time_delay=0.5, trans_time=1)
        trent.motion(group=MAIN, duration=0.2, anim=Male.Sc_MLHAND_HNEUT_HOLDD_LEFT_000LV_00, time_scale=10, trans_time=0.25)

        ConnectHardpointEvent(root=self, group=MAIN, target_name=trent_glass.name, parent_name=trent.name,
                              duration=666, target_hardpoint="hpleftconnect_prop_glass_green",
                              parent_hardpoint="hpleftconnect", time_delay=3.5)

        trent.facial(group=MAIN, index=70)

        cam_tenji.set(group=MAIN)

        tenji.move_head_ik(group=MAIN, target_name=mrk_trent_sit, duration=3)
        tenji.facial(group=MAIN, index=80)

        cam_trent.set(group=MAIN)

        trent.facial(group=MAIN, index=90)

        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_CHRB_DRINK_LHND_LARG_000LV_XA_06, time_scale=0.8, time_delay=-1, trans_time=1)

        main_group.append_time(2)
        cam_tenji_near.set(group=MAIN)

        tenji.facial(group=MAIN, index=100)

        main_group.append_time(0.2)
        cam_trent.set(group=MAIN)
        main_group.append_time(1)


        trent.facial(group=MAIN, index=110)

        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, time_scale=0.8, time_delay=-0.5, trans_time=2)








        cam_tenji_near.set(group=MAIN)

        tenji.facial(group=MAIN, index=120)
        tenji.motion(group=MAIN, duration=25, anim=Male.Sc_MLBODY_CHRB_GRABR_PRDRNK_TABL_000LV_XA_08, time_scale=0.8, time_delay=-3, trans_time=1)
        ConnectHardpointEvent(root=self, group=MAIN, target_name=tenji_bottle.name, parent_name=tenji.name,
                              duration=6, target_hardpoint="HpRightConnect_prop_bottle_wine_1",
                              parent_hardpoint="HpRightConnect", time_delay=-1)

        tenji.facial(group=MAIN, index=130)


        tenji.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_CHRB_GRABL_DRINK_TABL_000LV_XA_02, time_scale=0.7, time_delay=-1, trans_time=1)
        tenji.motion(group=MAIN, duration=0.2, anim=Male.Sc_MLHAND_HNEUT_HOLDD_LEFT_000LV_00, time_scale=10, trans_time=0.25)

        grab_time3 = main_group.get_time()
        conn3 = ConnectHardpointEvent(root=self, group=MAIN, target_name=tenji_glass.name, parent_name=tenji.name,
                                      duration=6, target_hardpoint="hpleftconnect_prop_glass_green",
                                      parent_hardpoint="hpleftconnect", time_delay=3)

        tenji.facial(group=MAIN, index=140)

        tenji.facial(group=MAIN, index=150)

        tenji.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_CHRB_DRINK_LHND_SIP_000LV_XA_04, time_scale=0.7, time_delay=-2, trans_time=1)


        cam_trent.set(group=MAIN)
        trent.facial(group=MAIN, index=160)

        cam_tenji.set(group=MAIN)
        main_group.append_time(1)

        conn3.set_duration(main_group.get_time() - grab_time3)
        tenji.motion(group=MAIN, duration=1, anim=Male.Sc_MLHAND_NEUT_LEFT_000LV_A_00, time_scale=0.01, trans_time=0.25, time_delay=3)

        tenji.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_CHRB_PUTDNL_DRINK_TABL_000LV_XA_06, time_scale=0.7, trans_time=2)
        tenji.facial(group=MAIN, index=170)


        cam_trent.set(group=MAIN)
        trent.start_head_ik(group=MAIN, duration=5000)
        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, time_scale=0.7, trans_time=1)
        trent.facial(group=MAIN, index=180)

        cam_tenji_near.set(group=MAIN)

        tenji.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_CHRB_GRABL_DRINK_TABL_000LV_XA_02, time_scale=0.8, time_delay=-1, trans_time=1)
        tenji.motion(group=MAIN, duration=0.2, anim=Male.Sc_MLHAND_HNEUT_HOLDD_LEFT_000LV_00, time_scale=10, trans_time=0.25)
        tenji.motion(group=MAIN, loop=True, duration=15, anim=Male.Sc_MLBODY_CHRB_HOLDD_TABL_000LV_XA_02, time_scale=0.8, trans_time=2, time_delay=8)

        grab_time4 = main_group.get_time()
        conn4 = ConnectHardpointEvent(root=self, group=MAIN, target_name=tenji_glass.name, parent_name=tenji.name,
                                      duration=6, target_hardpoint="hpleftconnect_prop_glass_green",
                                      parent_hardpoint="hpleftconnect", time_delay=3)

        tenji.facial(group=MAIN, index=190)
        tenji.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_CHRB_DRINK_LHND_SIP_000LV_XA_04, time_scale=1, time_delay=-1, trans_time=1)
        main_group.append_time(2.5)


        conn4.set_duration(main_group.get_time() - grab_time4 + 2)
        tenji.motion(group=MAIN, duration=1, anim=Male.Sc_MLHAND_NEUT_LEFT_000LV_A_00, time_scale=0.01, trans_time=0.25, time_delay=5)

        tenji.motion(group=MAIN, duration=15, anim=Male.Sc_MLBODY_CHRB_PUTDNL_DRINK_TABL_000LV_XA_06, time_scale=0.8, time_delay=2, trans_time=1)
        tenji.facial(group=MAIN, index=200)

        tenji.motion(group=MAIN, duration=30, loop=True, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, time_scale=0.8, trans_time=1)

        tenji.facial(group=MAIN, index=210)



        cam_trent.set(group=MAIN)
        # trent.start_head_ik(group=MAIN, duration=5000)
        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, time_scale=0.7)
        trent.facial(group=MAIN, index=220)


        cam_tenji_near.set(group=MAIN)
        tenji.facial(group=MAIN, index=230)

        cam_trent.set(group=MAIN)
        trent.facial(group=MAIN, index=240)


        MoveOffscreenEvent(root=self, group=MAIN, object_name=hassler.name)

        cam_tenji_near.set(group=MAIN)


        tenji.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_CHRB_CONV_LHNDUP_TRNS_000LV_XA_02, time_scale=0.6, trans_time=1)
        tenji.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_CHRB_CONV_LHND_CASL_000LV_xa_03, time_scale=0.6, time_delay=3, trans_time=1)
        tenji.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_CHRB_CONV_LHNDDN_TRNS_000LV_XA_02, time_scale=0.6, time_delay=14, trans_time=0.8)

        tenji.facial(group=MAIN, index=250)
        tenji.facial(group=MAIN, index=260)

        cam_trent.set(group=MAIN)
        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, time_scale=0.7)
        trent.facial(group=MAIN, index=270)

        cam_tenji_near.set(group=MAIN)
        tenji.facial(group=MAIN, index=280)
        #
        # cam_trent.set(group=MAIN)
        # trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, time_scale=0.6, time_delay=-1)
        # main_group.append_time(1)
        # trent.facial(group=MAIN, index=290)
        # main_group.append_time(0.5)
        #
        # cam_tenji.set(group=MAIN)
        # darcy.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=3.5, time_delay=3.5)
        # darcy.move_eye_ik(group=MAIN, target_name=mrk_trent_sit, duration=2.5, time_delay=3.5)
        # tenji.facial(group=MAIN, index=320)
        # tenji.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_CHRB_STNDCR_TRNS_090LV_XA_05, time_scale=0.8, time_delay=-3, trans_time=1)
        #
        # cam_darcy.set(group=MAIN)
        # darcy.facial(group=MAIN, index=350)
        #
        # trent.start_eye_ik(group=MAIN, duration=5000)   # DBG!@
        #
        # cam_trent.set(group=MAIN)
        # trent.move_head_ik(group=MAIN, target_name=mrk_darcy_front, duration=3, time_delay=-1)
        # trent.move_eye_ik(group=MAIN, target_name=mrk_darcy_sit, duration=2, time_delay=-1)
        # trent.facial(group=MAIN, index=360)
        # trent.move_head_ik(group=MAIN, target_name=mrk_tenji_to_trent, duration=3, time_delay=-2)
        # trent.move_eye_ik(group=MAIN, target_name=mrk_tenji_sit, duration=2, time_delay=-2)
        #
        # main_group.append_time(1)


class Msn9OrderDecisionThorn(Scene):
    SCENE_AMBIENT = [30, 30, 10]
    POINT_ROTATE_OVERRIDES = OVERRIDES

    def action(self):
        main_group = self.get_group(MAIN)

        music = Music(root=self, name='main_music', sound='music_bar_ku_palace', attenuation=-10)
        music.start(group=BG, duration=1000, loop=True)

        DjBoard(root=self, name='dj_board', init_point='dj_board', light_group=9, matrix_scale=1.75)

        dancepoint_floor_height = self.get_point('dancepoint_floor').position[1]
        # spot_ambi = [0.3, 0.3, 0.1]
        start_diffuse = [0.7, 0.4, 0.1]
        start_diffuse_simple = [0.15, 0.05, 0.05]
        end_diffuse = [0, 0, 0]

        # CAMERAS

        cam_decision = LookAtCamera(root=self, name='cam_decision', fov=28)

        light_anim_repeat = 400

        lt_room = Light(root=self, name='ROOMA', point_name='light_bartable', light_group=9, diffuse=[0, 0, 0],
                        ambient=[0.6, 0.8, 0.3], direction=[0, 0, -1], light_type=L_POINT, range=3)

        lt_room1 = Light(root=self, name='ROOM1', point_name='light1', light_group=9, diffuse=end_diffuse,
                         ambient=[0, 0, 0], direction=[0, 0, 1], light_type=L_POINT, range=6)

        lt_room2 = Light(root=self, name='ROOM2', point_name='light2', light_group=9, diffuse=start_diffuse,
                         ambient=[0, 0, 0], direction=[1, 0, 0], light_type=L_POINT, range=6)

        lt_room3 = Light(root=self, name='ROOM3', point_name='light3', light_group=9, diffuse=end_diffuse,
                         ambient=[0, 0, 0], direction=[-1, 0, 0], light_type=L_POINT, range=6)


        lt_room1b = Light(root=self, name='ROOM1b', point_name='light1', light_group=0, diffuse=end_diffuse,
                          ambient=[0, 0, 0], direction=[0, 0, 1], light_type=L_POINT, range=6)

        lt_room2b = Light(root=self, name='ROOM2b', point_name='light2', light_group=0, diffuse=start_diffuse_simple,
                          ambient=[0, 0, 0], direction=[1, 0, 0], light_type=L_POINT, range=6)

        lt_room3b = Light(root=self, name='ROOM3b', point_name='light3', light_group=0, diffuse=end_diffuse,
                         ambient=[0, 0, 0], direction=[-1, 0, 0], light_type=L_POINT, range=6)

        lt_room4b = Light(root=self, name='ROOM4b', point_name='light4', light_group=0, diffuse=start_diffuse,
                          ambient=[0, 0, 0], direction=[-1, 0, 0], light_type=L_POINT, range=6)

        lt_table1 = Light(root=self, name='TABLE1', light_group=15, diffuse=[0.5, 0.4, 0.3],
                          ambient=[0, 0, 0], direction=[1, 0, 0], light_type=L_DIRECT, range=2000)
        RotateAxisEvent(root=self, group=BG, object_name=lt_table1.name, angle=-45, duration=0.01, smooth=False)

        lt_table2 = Light(root=self, name='TABLE2', light_group=18, diffuse=[0.7, 0.5, 0.4],
                          ambient=[0.18, 0.1, 0.1], direction=[1, 0, 0], light_type=L_DIRECT, range=2000)

        lt_hassler = Light(root=self, name='HASSL', light_group=0, diffuse=[0.7, 0.6, 0.5],
                          ambient=[0.18, 0.1, 0.1], direction=[1, 0, 0], light_type=L_DIRECT, range=2000, on=False)

        # lt_room1.animate_ambient(BG, 'lt_room1_anim1', start_ambient=spot_ambi_off, end_ambient=spot_ambi,
        #                          duration=3, gap=1, smooth=True, repeat=3)
        lt_room1.animate_diffuse(BG, 'lt_room1_anim1', start_diffuse=end_diffuse, end_diffuse=start_diffuse,
                                 duration=0.6, start_gap=0.07, end_gap=0.15, smooth=True, repeat=light_anim_repeat)
        lt_room2.animate_diffuse(BG, 'lt_room2_anim1', start_diffuse=start_diffuse, end_diffuse=end_diffuse,
                                 duration=0.5, start_gap=0.05, end_gap=0.1, smooth=True, repeat=light_anim_repeat)
        lt_room3.animate_diffuse(BG, 'lt_room3_anim1', start_diffuse=start_diffuse, end_diffuse=end_diffuse,
                                 duration=0.4, start_gap=0.03, end_gap=0.08, smooth=True, repeat=light_anim_repeat)
        # lt_room2.animate_range(BG, 'lt_room2_anim2', start_range=6, end_range=5,
        #                          duration=2, gap=0, smooth=True, repeat=50)


        lt_room1b.animate_diffuse(BG, 'lt_room1b_anim1', start_diffuse=end_diffuse, end_diffuse=start_diffuse_simple,
                                  duration=0.6, start_gap=0.07, end_gap=0.15, smooth=True, repeat=light_anim_repeat)
        lt_room2b.animate_diffuse(BG, 'lt_room2b_anim1', start_diffuse=start_diffuse_simple, end_diffuse=end_diffuse,
                                  duration=0.5, start_gap=0.05, end_gap=0.1, smooth=True, repeat=light_anim_repeat)
        lt_room3b.animate_diffuse(BG, 'lt_room3b_anim1', start_diffuse=start_diffuse_simple, end_diffuse=end_diffuse,
                                  duration=0.4, start_gap=0.03, end_gap=0.08, smooth=True, repeat=light_anim_repeat)
        lt_room4b.animate_diffuse(BG, 'lt_room4b_anim1', start_diffuse=start_diffuse_simple, end_diffuse=start_diffuse,
                                  duration=0.6, start_gap=0.07, end_gap=0.15, smooth=True, repeat=light_anim_repeat)


        lt_dancepoint_indx = Light(root=self, name='DANCE1', light_group=90, diffuse=[1, 1, 1],
                                   ambient=[1, 0.6, 0.6], direction=[0, 0, 1]).get_index()
        lt_dancelook1_indx = Light(root=self, name='DANCE2', light_group=91, diffuse=[1, 0.2, 0.2],
                                   ambient=[0.1, 0.1, 0.1], direction=[0, 0, -1]).get_index()
        lt_dancelook2_indx = Light(root=self, name='DANCE3', light_group=92, diffuse=[1, 0.2, 0.2],
                                   ambient=[0.1, 0.1, 0.1], direction=[1, 0, 0]).get_index()
        lt_dancelook3_indx = Light(root=self, name='DANCE4', light_group=93, diffuse=[1, 0.2, 0.2],
                                   ambient=[0.1, 0.1, 0.1], direction=[0, 0, 1]).get_index()

        discoball1 = Alchemy(root=self, name='disco_fx1', particles='discobeam', point_name='discobeam1')
        discoball1.start(group=BG, duration=5000)
        RotateAxisEvent(root=self, group=BG, object_name=discoball1.name, angle=36000, duration=5000, smooth=False)

        # PROPS

        tenji_bottle = BottleWine(root=self, name='tenji_bottle', init_point='bottle_wine_1', light_group=0)
        tenji_glass = Glass(root=self, name='tenji_glass', init_point='tenji_glass', light_group=0)
        trent_glass = Glass(root=self, name='trent_glass', init_point='trent_glass', light_group=0)

        # CHARACTERS

        darcy = Character(root=self, actor=actors.Darcy, light_group=0, init_point='darcy_talk', rotate_y=45,
                          floor_height=0)
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='trent_talk', rotate_y=135,
                          floor_height=0)

        tekagi = Character(root=self, actor=actors.TekagiDj, light_group=0, init_point='tekagi_dj', rotate_y=180)
        tekagi.motion(group=BG, duration=5000, loop=True, anim=Male.Sc_MLBODY_STND_WIPE_BAR_000LV_XA_14)

        tenji = Character(root=self, actor=actors.Yamamoto, light_group=0, init_point='yamamoto_init', rotate_y=-45, use_ambient=False)
        tenji.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05)

        dancepoint = Character(root=self, actor=actors.YokoDancepoint, light_group=lt_dancepoint_indx,
                               init_point='dancepoint', rotate_y=110,
                               floor_height=dancepoint_floor_height, use_ambient=True)
        dancelook1 = Character(root=self, actor=actors.YokoDancelook1, light_group=lt_dancelook1_indx,
                               init_point='dancelook1', rotate_y=-130,
                               floor_height=0, use_ambient=True)
        dancelook2 = Character(root=self, actor=actors.YokoDancelook2, light_group=lt_dancelook2_indx,
                               init_point='dancelook2', rotate_y=-90,
                               floor_height=0, use_ambient=True)
        dancelook3 = Character(root=self, actor=actors.YokoDancelook3, light_group=lt_dancelook3_indx,
                               init_point='dancelook3', rotate_y=-50,
                               floor_height=0, use_ambient=True)

        group_dancepoint = 'bg_dancepoint'
        self.add_group(group_dancepoint, group_type=BG_GROUP)

        dancepoint.motion(group=group_dancepoint, duration=1, anim=Female.Sc_FMBODY_STND_DANC_000LV_A_20, start_time=1.9, time_append=0.1)
        dancepoint.motion(group=group_dancepoint, duration=20, repeat=50, anim=Female.Sc_FMBODY_STND_DANC_000LV_A_20, start_time=2, time_append=15, trans_time=1)

        dancelook1.motion(group=BG, duration=1000, loop=True, anim=Male.Sc_MLBODY_STLF_000LV_A_27, start_time=3)
        dancelook2.motion(group=BG, duration=1000, loop=True, anim=Male.Sc_MLBODY_STLB_LSTN_090LV_A_19)
        dancelook3.motion(group=BG, duration=1000, loop=True, anim=Male.Sc_MLBODY_STLF_000LV_A_27)

        dancepoint_lookat = self.get_automarker_name('dancepoint_lookat')

        NeckIkEvent(root=self, group=MAIN, char_name=dancelook1.name, target_name=dancepoint_lookat,
                    duration=3000, transition_duration=1)
        NeckIkEvent(root=self, group=MAIN, char_name=dancelook2.name, target_name=dancepoint_lookat,
                    duration=3000, transition_duration=1)
        NeckIkEvent(root=self, group=MAIN, char_name=dancelook3.name, target_name=dancepoint_lookat,
                    duration=3000, transition_duration=1)

        dancer1 = Character(root=self, actor=actors.YokohamaDancer1, light_group=0, init_point='dancer1', rotate_y=180)
        dancer2 = Character(root=self, actor=actors.YokohamaDancer2, light_group=0, init_point='dancer2', rotate_y=0)
        dancer3 = Character(root=self, actor=actors.YokohamaDancer3, light_group=0, init_point='dancer3', rotate_y=180)
        dancer4 = Character(root=self, actor=actors.YokohamaDancer4, light_group=0, init_point='dancer4', rotate_y=0)
        dancer5 = Character(root=self, actor=actors.YokohamaDancer5, light_group=0, init_point='dancer5', rotate_y=145)

        table1 = Character(root=self, actor=actors.YokohamaTable1, light_group=lt_table1.light_group, init_point='table1', rotate_y=135, use_ambient=True)
        table2 = Character(root=self, actor=actors.YokohamaTable2, light_group=lt_table1.light_group, init_point='table2', rotate_y=-45, use_ambient=True)
        table3 = Character(root=self, actor=actors.YokohamaTable3, light_group=lt_table2.light_group, init_point='table3', rotate_y=-45)
        table4 = Character(root=self, actor=actors.YokohamaTable4, light_group=lt_table2.light_group, init_point='table4', rotate_y=-135)
        table5 = Character(root=self, actor=actors.YokohamaTable5, light_group=lt_table2.light_group, init_point='table5', rotate_y=80)
        table6 = Character(root=self, actor=actors.YokohamaTable6, light_group=0, init_point='table6', rotate_y=-10)

        table1.motion(group=BG, duration=1000, loop=True, anim=Female.Sc_FMBODY_CHRF_IDLE_BIG_000LV_XA_05)
        table2.motion(group=BG, duration=1000, loop=True, anim=Female.Sc_FMBODY_CHRB_IDLE_BIG_000LV_XA_05)
        table3.motion(group=BG, duration=1000, loop=True, anim=Male.Sc_MLBODY_CHRF_IDLE_BIG_000LV_XA_06)
        table4.motion(group=BG, duration=1000, loop=True, anim=Male.Sc_MLBODY_CHRB_IDLE_BIG_000LV_XA_05)
        table5.motion(group=BG, duration=30, loop=True, anim=Male.Sc_MLBODY_STLB_LSTN_090LV_A_19, start_time=3)
        table5.motion(group=BG, duration=1000, loop=True, anim=Male.Sc_MLBODY_STLF_000LV_A_27, time_delay=30)
        table6.motion(group=BG, duration=1000, loop=True, anim=Female.Sc_FMBODY_STLB_000LV_A_21)

        group_dancer1 = 'bg_dancer1'
        self.add_group(group_dancer1, group_type=BG_GROUP)

        group_dancer2 = 'bg_dancer2'
        self.add_group(group_dancer2, group_type=BG_GROUP)

        group_dancer3 = 'bg_dancer3'
        self.add_group(group_dancer3, group_type=BG_GROUP)

        group_dancer4 = 'bg_dancer4'
        self.add_group(group_dancer4, group_type=BG_GROUP)

        group_dancer5 = 'bg_dancer5'
        self.add_group(group_dancer5, group_type=BG_GROUP)


        dancer1.motion(group=group_dancer1, duration=1, anim=Male.Sc_MLBODY_STND_DANC_000LV_A_28, start_time=1.9, time_append=0.1)
        dancer1.motion(group=group_dancer1, duration=20, repeat=50, anim=Male.Sc_MLBODY_STND_DANC_000LV_A_28, start_time=2, time_append=15, trans_time=1)

        dancer2.motion(group=group_dancer2, duration=1, anim=Female.Sc_FMBODY_STND_DANC_000LV_A_20, start_time=1.9, time_append=0.1)
        dancer2.motion(group=group_dancer2, duration=20, repeat=50, anim=Female.Sc_FMBODY_STND_DANC_000LV_A_20, start_time=2, time_append=15, trans_time=1)

        dancer3.motion(group=group_dancer3, duration=1, anim=Female.Sc_FMBODY_STND_DANC_000LV_A_20, start_time=1.9, time_append=0.1)
        dancer3.motion(group=group_dancer3, duration=20, repeat=50, anim=Female.Sc_FMBODY_STND_DANC_000LV_A_20, start_time=2, time_append=15, trans_time=1)

        dancer4.motion(group=group_dancer4, duration=1, anim=Male.Sc_MLBODY_STND_DANC_000LV_A_28, start_time=1.9, time_append=0.1)
        dancer4.motion(group=group_dancer4, duration=20, repeat=50, anim=Male.Sc_MLBODY_STND_DANC_000LV_A_28, start_time=2, time_append=15, trans_time=1)

        dancer5.motion(group=group_dancer5, duration=1, anim=Male.Sc_MLBODY_STND_DANC_000LV_A_28, start_time=1.9, time_append=0.1)
        dancer5.motion(group=group_dancer5, duration=20, repeat=50, anim=Male.Sc_MLBODY_STND_DANC_000LV_A_28, start_time=2, time_append=15, trans_time=1)

        # MARKERS

        tenji.motion(group=MAIN, duration=1000, loop=True, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05)
        trent.motion(group=MAIN, duration=1000, loop=True, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06)
        darcy.motion(group=MAIN, duration=1000, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06)

        cam_decision.set(group=MAIN)

        main_group.append_time(300)


class Msn9OrderAcceptThorn(Scene):
    SCENE_AMBIENT = [30, 30, 10]
    POINT_ROTATE_OVERRIDES = OVERRIDES

    def action(self):
        main_group = self.get_group(MAIN)

        music = Music(root=self, name='main_music', sound='music_bar_ku_palace', attenuation=-14)
        music.start(group=BG, duration=1000, loop=True)

        DjBoard(root=self, name='dj_board', init_point='dj_board', light_group=9, matrix_scale=1.75)

        dancepoint_floor_height = self.get_point('dancepoint_floor').position[1]
        # spot_ambi = [0.3, 0.3, 0.1]
        start_diffuse = [0.7, 0.4, 0.1]
        start_diffuse_simple = [0.15, 0.05, 0.05]
        end_diffuse = [0, 0, 0]

        # CAMERAS

        cam_dbg = LookAtCamera(root=self, name='cam_dbg', fov=40)
        cam_start = LookAtCamera(root=self, name='cam_start', fov=35)
        cam_dance = LookAtCamera(root=self, name='cam_dance', fov=40)
        cam_hassler = LookAtCamera(root=self, name='cam_hassler', fov=20)
        cam_tenji = LookAtCamera(root=self, name='cam_tenji', fov=20)
        cam_tenji_near = LookAtCamera(root=self, name='cam_tenji_near', fov=18)
        cam_friends = LookAtCamera(root=self, name='cam_friends', fov=24)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=16)
        cam_darcy = LookAtCamera(root=self, name='cam_darcy', fov=16)

        light_anim_repeat = 400

        lt_room = Light(root=self, name='ROOMA', point_name='light_bartable', light_group=9, diffuse=[0, 0, 0],
                        ambient=[0.6, 0.8, 0.3], direction=[0, 0, -1], light_type=L_POINT, range=3)

        lt_room1 = Light(root=self, name='ROOM1', point_name='light1', light_group=9, diffuse=end_diffuse,
                         ambient=[0, 0, 0], direction=[0, 0, 1], light_type=L_POINT, range=6)

        lt_room2 = Light(root=self, name='ROOM2', point_name='light2', light_group=9, diffuse=start_diffuse,
                         ambient=[0, 0, 0], direction=[1, 0, 0], light_type=L_POINT, range=6)

        lt_room3 = Light(root=self, name='ROOM3', point_name='light3', light_group=9, diffuse=end_diffuse,
                         ambient=[0, 0, 0], direction=[-1, 0, 0], light_type=L_POINT, range=6)


        lt_room1b = Light(root=self, name='ROOM1b', point_name='light1', light_group=0, diffuse=end_diffuse,
                          ambient=[0, 0, 0], direction=[0, 0, 1], light_type=L_POINT, range=6)

        lt_room2b = Light(root=self, name='ROOM2b', point_name='light2', light_group=0, diffuse=start_diffuse_simple,
                          ambient=[0, 0, 0], direction=[1, 0, 0], light_type=L_POINT, range=6)

        lt_room3b = Light(root=self, name='ROOM3b', point_name='light3', light_group=0, diffuse=end_diffuse,
                         ambient=[0, 0, 0], direction=[-1, 0, 0], light_type=L_POINT, range=6)

        lt_room4b = Light(root=self, name='ROOM4b', point_name='light4', light_group=0, diffuse=start_diffuse,
                          ambient=[0, 0, 0], direction=[-1, 0, 0], light_type=L_POINT, range=6)

        lt_table1 = Light(root=self, name='TABLE1', light_group=15, diffuse=[0.5, 0.4, 0.3],
                          ambient=[0, 0, 0], direction=[1, 0, 0], light_type=L_DIRECT, range=2000)
        RotateAxisEvent(root=self, group=BG, object_name=lt_table1.name, angle=-45, duration=0.01, smooth=False)

        lt_table2 = Light(root=self, name='TABLE2', light_group=18, diffuse=[0.7, 0.5, 0.4],
                          ambient=[0.18, 0.1, 0.1], direction=[1, 0, 0], light_type=L_DIRECT, range=2000)

        lt_hassler = Light(root=self, name='HASSL', light_group=0, diffuse=[0.7, 0.6, 0.5],
                          ambient=[0.18, 0.1, 0.1], direction=[1, 0, 0], light_type=L_DIRECT, range=2000, on=False)

        # lt_room1.animate_ambient(BG, 'lt_room1_anim1', start_ambient=spot_ambi_off, end_ambient=spot_ambi,
        #                          duration=3, gap=1, smooth=True, repeat=3)
        lt_room1.animate_diffuse(BG, 'lt_room1_anim1', start_diffuse=end_diffuse, end_diffuse=start_diffuse,
                                 duration=0.6, start_gap=0.07, end_gap=0.15, smooth=True, repeat=light_anim_repeat)
        lt_room2.animate_diffuse(BG, 'lt_room2_anim1', start_diffuse=start_diffuse, end_diffuse=end_diffuse,
                                 duration=0.5, start_gap=0.05, end_gap=0.1, smooth=True, repeat=light_anim_repeat)
        lt_room3.animate_diffuse(BG, 'lt_room3_anim1', start_diffuse=start_diffuse, end_diffuse=end_diffuse,
                                 duration=0.4, start_gap=0.03, end_gap=0.08, smooth=True, repeat=light_anim_repeat)
        # lt_room2.animate_range(BG, 'lt_room2_anim2', start_range=6, end_range=5,
        #                          duration=2, gap=0, smooth=True, repeat=50)


        lt_room1b.animate_diffuse(BG, 'lt_room1b_anim1', start_diffuse=end_diffuse, end_diffuse=start_diffuse_simple,
                                  duration=0.6, start_gap=0.07, end_gap=0.15, smooth=True, repeat=light_anim_repeat)
        lt_room2b.animate_diffuse(BG, 'lt_room2b_anim1', start_diffuse=start_diffuse_simple, end_diffuse=end_diffuse,
                                  duration=0.5, start_gap=0.05, end_gap=0.1, smooth=True, repeat=light_anim_repeat)
        lt_room3b.animate_diffuse(BG, 'lt_room3b_anim1', start_diffuse=start_diffuse_simple, end_diffuse=end_diffuse,
                                  duration=0.4, start_gap=0.03, end_gap=0.08, smooth=True, repeat=light_anim_repeat)
        lt_room4b.animate_diffuse(BG, 'lt_room4b_anim1', start_diffuse=start_diffuse_simple, end_diffuse=start_diffuse,
                                  duration=0.6, start_gap=0.07, end_gap=0.15, smooth=True, repeat=light_anim_repeat)


        lt_dancepoint_indx = Light(root=self, name='DANCE1', light_group=90, diffuse=[1, 1, 1],
                                   ambient=[1, 0.6, 0.6], direction=[0, 0, 1]).get_index()
        lt_dancelook1_indx = Light(root=self, name='DANCE2', light_group=91, diffuse=[1, 0.2, 0.2],
                                   ambient=[0.1, 0.1, 0.1], direction=[0, 0, -1]).get_index()
        lt_dancelook2_indx = Light(root=self, name='DANCE3', light_group=92, diffuse=[1, 0.2, 0.2],
                                   ambient=[0.1, 0.1, 0.1], direction=[1, 0, 0]).get_index()
        lt_dancelook3_indx = Light(root=self, name='DANCE4', light_group=93, diffuse=[1, 0.2, 0.2],
                                   ambient=[0.1, 0.1, 0.1], direction=[0, 0, 1]).get_index()

        discoball1 = Alchemy(root=self, name='disco_fx1', particles='discobeam', point_name='discobeam1')
        discoball1.start(group=BG, duration=5000)
        RotateAxisEvent(root=self, group=BG, object_name=discoball1.name, angle=36000, duration=5000, smooth=False)

        # PROPS

        tenji_bottle = BottleWine(root=self, name='tenji_bottle', init_point='bottle_wine_1', light_group=0)
        tenji_glass = Glass(root=self, name='tenji_glass', init_point='tenji_glass', light_group=0)
        trent_glass = Glass(root=self, name='trent_glass', init_point='trent_glass', light_group=0)

        # CHARACTERS

        darcy = Character(root=self, actor=actors.Darcy, light_group=0, init_point='darcy_talk', rotate_y=45,
                          floor_height=0)
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='trent_talk', rotate_y=135,
                          floor_height=0)

        tekagi = Character(root=self, actor=actors.TekagiDj, light_group=0, init_point='tekagi_dj', rotate_y=180)
        tekagi.motion(group=BG, duration=5000, loop=True, anim=Male.Sc_MLBODY_STND_WIPE_BAR_000LV_XA_14)

        tenji = Character(root=self, actor=actors.Yamamoto, light_group=0, init_point='yamamoto_init', rotate_y=-45, use_ambient=True)
        tenji.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05)

        dancepoint = Character(root=self, actor=actors.YokoDancepoint, light_group=lt_dancepoint_indx,
                               init_point='dancepoint', rotate_y=110,
                               floor_height=dancepoint_floor_height, use_ambient=True)
        dancelook1 = Character(root=self, actor=actors.YokoDancelook1, light_group=lt_dancelook1_indx,
                               init_point='dancelook1', rotate_y=-130,
                               floor_height=0, use_ambient=True)
        dancelook2 = Character(root=self, actor=actors.YokoDancelook2, light_group=lt_dancelook2_indx,
                               init_point='dancelook2', rotate_y=-90,
                               floor_height=0, use_ambient=True)
        dancelook3 = Character(root=self, actor=actors.YokoDancelook3, light_group=lt_dancelook3_indx,
                               init_point='dancelook3', rotate_y=-50,
                               floor_height=0, use_ambient=True)

        group_dancepoint = 'bg_dancepoint'
        self.add_group(group_dancepoint, group_type=BG_GROUP)

        dancepoint.motion(group=group_dancepoint, duration=1, anim=Female.Sc_FMBODY_STND_DANC_000LV_A_20, start_time=1.9, time_append=0.1)
        dancepoint.motion(group=group_dancepoint, duration=20, repeat=50, anim=Female.Sc_FMBODY_STND_DANC_000LV_A_20, start_time=2, time_append=15, trans_time=1)

        dancelook1.motion(group=BG, duration=1000, loop=True, anim=Male.Sc_MLBODY_STLF_000LV_A_27, start_time=3)
        dancelook2.motion(group=BG, duration=1000, loop=True, anim=Male.Sc_MLBODY_STLB_LSTN_090LV_A_19)
        dancelook3.motion(group=BG, duration=1000, loop=True, anim=Male.Sc_MLBODY_STLF_000LV_A_27)

        dancepoint_lookat = self.get_automarker_name('dancepoint_lookat')

        NeckIkEvent(root=self, group=MAIN, char_name=dancelook1.name, target_name=dancepoint_lookat,
                    duration=3000, transition_duration=1)
        NeckIkEvent(root=self, group=MAIN, char_name=dancelook2.name, target_name=dancepoint_lookat,
                    duration=3000, transition_duration=1)
        NeckIkEvent(root=self, group=MAIN, char_name=dancelook3.name, target_name=dancepoint_lookat,
                    duration=3000, transition_duration=1)

        dancer1 = Character(root=self, actor=actors.YokohamaDancer1, light_group=0, init_point='dancer1', rotate_y=180)
        dancer2 = Character(root=self, actor=actors.YokohamaDancer2, light_group=0, init_point='dancer2', rotate_y=0)
        dancer3 = Character(root=self, actor=actors.YokohamaDancer3, light_group=0, init_point='dancer3', rotate_y=180)
        dancer4 = Character(root=self, actor=actors.YokohamaDancer4, light_group=0, init_point='dancer4', rotate_y=0)
        dancer5 = Character(root=self, actor=actors.YokohamaDancer5, light_group=0, init_point='dancer5', rotate_y=145)


        table1 = Character(root=self, actor=actors.YokohamaTable1, light_group=lt_table1.light_group, init_point='table1', rotate_y=135, use_ambient=True)
        table2 = Character(root=self, actor=actors.YokohamaTable2, light_group=lt_table1.light_group, init_point='table2', rotate_y=-45, use_ambient=True)
        table3 = Character(root=self, actor=actors.YokohamaTable3, light_group=lt_table2.light_group, init_point='table3', rotate_y=-45)
        table4 = Character(root=self, actor=actors.YokohamaTable4, light_group=lt_table2.light_group, init_point='table4', rotate_y=-135)
        table5 = Character(root=self, actor=actors.YokohamaTable5, light_group=lt_table2.light_group, init_point='table5', rotate_y=80)
        table6 = Character(root=self, actor=actors.YokohamaTable6, light_group=0, init_point='table6', rotate_y=-10)

        table1.motion(group=BG, duration=1000, loop=True, anim=Female.Sc_FMBODY_CHRF_IDLE_BIG_000LV_XA_05)
        table2.motion(group=BG, duration=1000, loop=True, anim=Female.Sc_FMBODY_CHRB_IDLE_BIG_000LV_XA_05)
        table3.motion(group=BG, duration=1000, loop=True, anim=Male.Sc_MLBODY_CHRF_IDLE_BIG_000LV_XA_06)
        table4.motion(group=BG, duration=1000, loop=True, anim=Male.Sc_MLBODY_CHRB_IDLE_BIG_000LV_XA_05)
        table5.motion(group=BG, duration=30, loop=True, anim=Male.Sc_MLBODY_STLB_LSTN_090LV_A_19, start_time=3)
        table5.motion(group=BG, duration=1000, loop=True, anim=Male.Sc_MLBODY_STLF_000LV_A_27, time_delay=30)
        table6.motion(group=BG, duration=1000, loop=True, anim=Female.Sc_FMBODY_STLB_000LV_A_21)

        group_dancer1 = 'bg_dancer1'
        self.add_group(group_dancer1, group_type=BG_GROUP)

        group_dancer2 = 'bg_dancer2'
        self.add_group(group_dancer2, group_type=BG_GROUP)

        group_dancer3 = 'bg_dancer3'
        self.add_group(group_dancer3, group_type=BG_GROUP)

        group_dancer4 = 'bg_dancer4'
        self.add_group(group_dancer4, group_type=BG_GROUP)

        group_dancer5 = 'bg_dancer5'
        self.add_group(group_dancer5, group_type=BG_GROUP)


        dancer1.motion(group=group_dancer1, duration=1, anim=Male.Sc_MLBODY_STND_DANC_000LV_A_28, start_time=1.9, time_append=0.1)
        dancer1.motion(group=group_dancer1, duration=20, repeat=50, anim=Male.Sc_MLBODY_STND_DANC_000LV_A_28, start_time=2, time_append=15, trans_time=1)

        dancer2.motion(group=group_dancer2, duration=1, anim=Female.Sc_FMBODY_STND_DANC_000LV_A_20, start_time=1.9, time_append=0.1)
        dancer2.motion(group=group_dancer2, duration=20, repeat=50, anim=Female.Sc_FMBODY_STND_DANC_000LV_A_20, start_time=2, time_append=15, trans_time=1)

        dancer3.motion(group=group_dancer3, duration=1, anim=Female.Sc_FMBODY_STND_DANC_000LV_A_20, start_time=1.9, time_append=0.1)
        dancer3.motion(group=group_dancer3, duration=20, repeat=50, anim=Female.Sc_FMBODY_STND_DANC_000LV_A_20, start_time=2, time_append=15, trans_time=1)

        dancer4.motion(group=group_dancer4, duration=1, anim=Male.Sc_MLBODY_STND_DANC_000LV_A_28, start_time=1.9, time_append=0.1)
        dancer4.motion(group=group_dancer4, duration=20, repeat=50, anim=Male.Sc_MLBODY_STND_DANC_000LV_A_28, start_time=2, time_append=15, trans_time=1)

        dancer5.motion(group=group_dancer5, duration=1, anim=Male.Sc_MLBODY_STND_DANC_000LV_A_28, start_time=1.9, time_append=0.1)
        dancer5.motion(group=group_dancer5, duration=20, repeat=50, anim=Male.Sc_MLBODY_STND_DANC_000LV_A_28, start_time=2, time_append=15, trans_time=1)

        # MARKERS

        mrk_tenji_sit = trent.get_sit_marker('yamamoto_init')
        mrk_trent_sit = trent.get_sit_marker('trent_talk')
        mrk_darcy_sit = darcy.get_sit_marker('darcy_talk')

        mrk_tenji_front = self.get_automarker_name('yamamoto_front')
        mrk_tenji_to_trent = self.get_automarker_name('yamamoto_trentlook')
        mrk_darcy_front = self.get_automarker_name('darcy_front')
        mrk_trent_front = self.get_automarker_name('darcy_looktrent')
        mrk_go_start = self.get_automarker_name('go_start')
        mrk_go_end = self.get_automarker_name('go_end')





        trent.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, time_scale=0.5)
        tenji.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, time_scale=1,  trans_time=1)
        darcy.motion(group=MAIN, duration=1000, loop=True, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, time_scale=0.5, time_delay=0.1)


        trent.move_head_ik(group=MAIN, target_name=mrk_tenji_to_trent, immediately=True)

        darcy.move_head_ik(group=MAIN, target_name=mrk_tenji_front, immediately=True)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_tenji_sit, immediately=True)

        trent.start_head_ik(group=MAIN, duration=5000)
        darcy.start_head_ik(group=MAIN, duration=1000, time_delay=1)
        darcy.start_eye_ik(group=MAIN, duration=1000, time_delay=1)

        cam_trent.set(group=MAIN)
        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, time_scale=0.6)
        main_group.append_time(1)
        trent.facial(group=MAIN, index=290)
        main_group.append_time(0.5)

        cam_tenji.set(group=MAIN)
        darcy.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=3.5, time_delay=3.5)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_trent_sit, duration=2.5, time_delay=3.5)
        tenji.facial(group=MAIN, index=320)
        tenji.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_CHRB_STNDCR_TRNS_090LV_XA_05, time_scale=0.8, time_delay=-3, trans_time=1)

        cam_darcy.set(group=MAIN)
        darcy.facial(group=MAIN, index=350)

        trent.start_eye_ik(group=MAIN, duration=5000)   # DBG!@

        cam_trent.set(group=MAIN)
        trent.move_head_ik(group=MAIN, target_name=mrk_darcy_front, duration=3, time_delay=-1)
        trent.move_eye_ik(group=MAIN, target_name=mrk_darcy_sit, duration=2, time_delay=-1)
        trent.facial(group=MAIN, index=360)
        trent.move_head_ik(group=MAIN, target_name=mrk_tenji_to_trent, duration=3, time_delay=-2)
        trent.move_eye_ik(group=MAIN, target_name=mrk_tenji_sit, duration=2, time_delay=-2)

        main_group.append_time(1)

