from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import Male, Female, Trent
from story.cutscenes import sequence

from story import actors



class Msn14TrentRescuedScene(Scene):
    DUMP_FILE = 'li_station_bar'


    def action(self):
        main_group = self.get_group(MAIN)

        cam_dbg = StaticCamera(root=self, name='cam_dbg', fov=40)

        cam_char6_to8 = StaticCamera(root=self, name='cam_char6_to8', fov=18)
        cam_char6_to8_alt = StaticCamera(root=self, name='cam_char6_to8_alt', fov=22)
        cam_char7 = StaticCamera(root=self, name='cam_char7', fov=18)
        cam_char8 = StaticCamera(root=self, name='cam_char8', fov=18)

        cam_char6_to8_alt.set(group=MAIN)


        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='char6', rotate_from_quat=True, camera=cam_char6_to8)
        edison = Character(root=self, actor=actors.EdisonTrent, light_group=0, init_point='char7', rotate_from_quat=True,
                           camera=cam_char7, anim_sequence=sequence.SEQUENCE_MALE_STAND_RHAND)
        robot = Character(root=self, actor=actors.LogosRobot, light_group=0, init_point='char8', rotate_from_quat=True, camera=cam_char8)

        trent.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05)
        edison.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)
        robot.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, time_scale=0.6)



        mrk_robo = self.get_automarker_name('mrk_robo')
        mrk_robo2 = self.get_automarker_name('mrk_robo2')
        mrk_edison2 = self.get_automarker_name('mrk_edison2')
        mrk_edison = edison.get_stand_marker('char7')
        mrk_trent = trent.get_sit_marker('char6')

        trent.move_head_ik(group=MAIN, target_name=mrk_robo2, immediately=True)
        trent.move_eye_ik(group=MAIN, target_name=mrk_robo, immediately=True)

        robot.move_head_ik(group=MAIN, target_name=mrk_edison, immediately=True)

        edison.move_head_ik(group=MAIN, target_name=mrk_trent, immediately=True)

        edison.start_head_ik(group=MAIN, duration=1000)
        trent.start_head_ik(group=MAIN, duration=1000)
        trent.start_eye_ik(group=MAIN, duration=1000)


        main_group.append_time(1)
        trent.facial(group=MAIN, index=10, auto_lip=True)

        trent.move_head_ik(group=MAIN, target_name=mrk_edison2, duration=1.6, time_delay=0.5)
        trent.move_eye_ik(group=MAIN, target_name=mrk_edison, duration=0.8, time_delay=0.5)

        main_group.append_time(1)


        cam_char7.set(group=MAIN, time_delay=2)

        edison.facial(group=MAIN, index=20, auto_lip=True)

        robot.start_head_ik(group=MAIN, duration=1000)

        Autoplay(
            self,
            group=MAIN,
            start_index=30,
        )

        # trent.facial(group=MAIN, index=30, auto_lip=True)

        # main_group.append_time(1000)
