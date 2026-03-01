from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import Male, Female, Trent
from story.cutscenes import sequence

from story import actors



class RewardScene(Scene):
    DUMP_FILE = 'li_manhattan_bar'

    def action(self):
        main_group = self.get_group(MAIN)

        cam_greet = StaticCamera(root=self, name='cam_greet', fov=25)
        cam_char1 = StaticCamera(root=self, name='cam_char1', fov=18)
        cam_char2 = StaticCamera(root=self, name='cam_char2', fov=18)

        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='char1', rotate_from_quat=True,
                           camera=cam_char1, anim_sequence=sequence.SEQUENCE_MALE_STAND_FSTHIPB_CROSS)
        kenji = Character(root=self, actor=actors.Washington, light_group=0, init_point='char2', rotate_from_quat=True,
                           camera=cam_char2, anim_sequence=sequence.SEQUENCE_MALE_STAND_RHAND_ALT2)

        trent.idle(group=MAIN)
        kenji.idle(group=MAIN)

        mrk_trent = trent.get_stand_marker('char1')
        mrk_kenji = kenji.get_stand_marker('char2')

        trent.move_head_ik(group=MAIN, target_name=mrk_kenji, immediately=True)
        kenji.move_head_ik(group=MAIN, target_name=mrk_trent, immediately=True)

        trent.start_head_ik(group=MAIN, duration=1000)
        kenji.start_head_ik(group=MAIN, duration=1000)

        cam_greet.set(group=MAIN)
        cam_greet.move_cam(group=MAIN, index=2, duration=10, smooth=True)

        main_group.append_time(10)

        Autoplay(
            self,
            group=MAIN,
            start_index=0,
        )

        main_group.append_time(2)
