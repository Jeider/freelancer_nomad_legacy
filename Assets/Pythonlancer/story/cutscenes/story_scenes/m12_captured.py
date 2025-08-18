from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import Male, Female, Trent

from story import actors


class Msn12CapturedScene(Scene):
    POINT_ROTATE_OVERRIDES = {
        'trent_talk': (0, 0, 0),
    }

    def action(self):
        main_group = self.get_group(MAIN)

        # CAMERAS

        cam_dbg = LookAtCamera(root=self, name='cam_dbg', fov=30)


        # PROPS

        # CHARACTERS

        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='trent_init', rotate_y=60)

        # MARKERS

        mrk_trent_init = trent.get_stand_marker('trent_init')

        # mrk_trent_angry_front = self.get_automarker_name('mrk_trent_angry_front')



        # EXTRA DEFINITIONS
        #
        # trent.move_head_ik(group=BG, target_name=mrk_kim_table, immediately=True)
        # trent.move_eye_ik(group=BG, target_name=mrk_kim_table, immediately=True)

        # kim.start_head_ik(group=MAIN, duration=1000)
        # kim.start_eye_ik(group=MAIN, duration=1000)
        # trent_head_ik1 = trent.start_head_ik(group=MAIN, duration=1000)
        # trent_eye_ik1 = trent.start_eye_ik(group=MAIN, duration=1000)
        #
        # cam_start.set(group=MAIN)
        #
        # cam_start.move_cam(group=MAIN, index=2, duration=12, smooth=True)
        # cam_start.move_focus(group=MAIN, index=2, duration=4, smooth=True)

        main_group.append_time(1000)
