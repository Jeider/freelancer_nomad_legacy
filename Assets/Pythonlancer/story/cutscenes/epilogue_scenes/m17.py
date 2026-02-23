from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import Male, Female, Trent
from story.cutscenes import sequence

from story import actors



class JackMeetScene(Scene):
    DUMP_FILE = 'cv_space_bar'

    def action(self):
        main_group = self.get_group(MAIN)

        # cam_dbg = StaticCamera(root=self, name='cam_dbg', fov=25)
        cam_greet = StaticCamera(root=self, name='cam_greet', fov=25)


        cam_char8 = StaticCamera(root=self, name='cam_char8', fov=18)
        cam_char9 = StaticCamera(root=self, name='cam_char9', fov=18)

        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='char9', rotate_from_quat=True,
                           camera=cam_char9, anim_sequence=sequence.SEQUENCE_MALE_STAND_FSTHIPB_CROSS)
        jack = Character(root=self, actor=actors.JackRazorBarber, light_group=0, init_point='char8', rotate_from_quat=True,
                           camera=cam_char8, anim_sequence=sequence.SEQUENCE_MALE_SIT_LHAND_PIRATE)

        trent.idle(group=MAIN)
        jack.idle_sit(group=MAIN)

        mrk_trent = trent.get_stand_marker('char9')
        mrk_jack = jack.get_sit_marker('char8')

        trent.move_head_ik(group=MAIN, target_name=mrk_jack, immediately=True)
        jack.move_head_ik(group=MAIN, target_name=mrk_trent, immediately=True)

        trent.start_head_ik(group=MAIN, duration=1000)
        jack.start_head_ik(group=MAIN, duration=1000)

        cam_greet.set(group=MAIN)
        cam_greet.move_cam(group=MAIN, index=2, duration=6, smooth=True)

        main_group.append_time(6)

        Autoplay(
            self,
            group=MAIN,
            start_index=0,
        )

        main_group.append_time(1)
