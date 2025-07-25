from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import Male, Female

from story import actors


class Msn9OrderCutsceneThorn(Scene):
    SCENE_AMBIENT = [30, 30, 10]
    POINT_ROTATE_OVERRIDES = {
        # 'tekagi_dj': (0, 180, 0),
    }

    def action(self):
        main_group = self.get_group(MAIN)

        dancepoint_floor_height = self.get_point('dancepoint_floor').position[1]
        spot_ambi = [0.3, 0.3, 0.3]

        # CAMERAS

        cam_dbg = LookAtCamera(root=self, name='cam_dbg', fov=45)
        cam_dance = LookAtCamera(root=self, name='cam_dance', fov=20)

        lt_room = Light(root=self, name='ROOMA', light_group=9, diffuse=[0, 0, 0], point_name='light_bartable',
                        ambient=[0.6, 0.8, 0.3], direction=[0, 0, -1], light_type=L_POINT, range=3)

        lt_room1 = Light(root=self, name='ROOM1', light_group=9, diffuse=[0, 0, 0],
                         ambient=spot_ambi, direction=[0, 0, 1], light_type=L_SPOT, range=6, on=False)

        lt_room2 = Light(root=self, name='ROOM2', light_group=9, diffuse=[0, 0, 0],
                         ambient=spot_ambi, direction=[1, 0, 0], light_type=L_SPOT, range=6)

        lt_room3 = Light(root=self, name='ROOM3', light_group=9, diffuse=[0, 0, 0],
                         ambient=spot_ambi, direction=[-1, 0, 0], light_type=L_SPOT, range=6)

        lt_dancepoint_indx = Light(root=self, name='DANCE1', light_group=90, diffuse=[1, 1, 1],
                                   ambient=[1, 0.6, 0.6], direction=[0, 0, 1]).get_index()
        lt_dancelook1_indx = Light(root=self, name='DANCE2', light_group=91, diffuse=[1, 0.2, 0.2],
                                   ambient=[0.1, 0.1, 0.1], direction=[0, 0, -1]).get_index()
        lt_dancelook2_indx = Light(root=self, name='DANCE3', light_group=92, diffuse=[1, 0.2, 0.2],
                                   ambient=[0.1, 0.1, 0.1], direction=[1, 0, 0]).get_index()
        lt_dancelook3_indx = Light(root=self, name='DANCE4', light_group=93, diffuse=[1, 0.2, 0.2],
                                   ambient=[0.1, 0.1, 0.1], direction=[0, 0, 1]).get_index()

        # CHARACTERS

        # darcy = Character(root=self, actor=actors.Darcy, light_group=0, init_point='darcy_bottom', rotate=-90,
        #                   floor_height=0)
        # trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='trent_bottom', rotate=-90,
        #                   floor_height=0)
        #
        # darcy.motion(group=MAIN, duration=13, loop=True, anim=Female.Sc_FMBODY_STND_HOLD_ARMS_CROSSED_000LV_XA_03)
        # trent.motion(group=MAIN, duration=13, loop=True, anim=Male.Sc_MLBODY_STND_FSTHIPB_HOLD_000LV_XA_02)
        #
        # hassler = Character(root=self, actor=actors.HasslerOrder, light_group=0, init_point='hassler_init', rotate=90)
        # hassler.idle(group=MAIN)


        tekagi = Character(root=self, actor=actors.TekagiDj, light_group=0, init_point='tekagi_dj', rotate=180)
        tekagi.motion(group=BG, duration=5000, loop=True, anim=Male.Sc_MLBODY_STND_WIPE_BAR_000LV_XA_14)

        dancepoint = Character(root=self, actor=actors.YokoDancepoint, light_group=lt_dancepoint_indx,
                               init_point='dancepoint', rotate=100,
                               floor_height=dancepoint_floor_height, use_ambient=True)
        dancelook1 = Character(root=self, actor=actors.YokoDancelook1, light_group=lt_dancelook1_indx,
                               init_point='dancelook1', rotate=-130,
                               floor_height=0, use_ambient=True)
        dancelook2 = Character(root=self, actor=actors.YokoDancelook2, light_group=lt_dancelook2_indx,
                               init_point='dancelook2', rotate=-90,
                               floor_height=0, use_ambient=True)
        dancelook3 = Character(root=self, actor=actors.YokoDancelook3, light_group=lt_dancelook3_indx,
                               init_point='dancelook3', rotate=-50,
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

        # MARKERS
        #
        # mrk_trent_goend = trent.get_stand_marker('trent_goend')
        # mrk_darcy_goend = darcy.get_stand_marker('darcy_goend')
        # mrk_hassler_walk = hassler.get_stand_marker('hassler_talk')
        # mrk_darcy_left = self.get_automarker_name('head_darcy_left')
        # mrk_darcy_right = self.get_automarker_name('head_darcy_right')

        cam_dbg.set(group=MAIN)