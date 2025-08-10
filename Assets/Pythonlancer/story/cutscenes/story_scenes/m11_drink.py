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
        # cam_start = LookAtCamera(root=self, name='cam_start', fov=30)

        # PROPS

        # CHARACTERS

        # alaric = Character(root=self, actor=actors.Alaric, light_group=0, init_point='alaric_talk', rotate_y=0)
        # trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='trent_init', rotate_y=180)


        # MARKERS

        # mrk_trent_init = trent.get_stand_marker('trent_init')
        # mrk_trent_talk = trent.get_stand_marker('trent_talk')
        # mrk_alaric_talk = alaric.get_sit_marker('alaric_talk')
        # mrk_edison_talk = edison.get_sit_marker('edison_talk')
        # mrk_junko_talk = junko.get_sit_marker('junko_talk')
        #
        # mrk_alaric_head_top = self.get_automarker_name('alaric_head_top')
        # mrk_alaric_look_front = self.get_automarker_name('alaric_look_front')
        # mrk_alaric_look_side = self.get_automarker_name('alaric_look_side')
        # mrk_trent_look_front = self.get_automarker_name('trent_look_front')
        # mrk_trent_look_side = self.get_automarker_name('trent_look_side')
        # mrk_edison_front = self.get_automarker_name('edison_front')
        # mrk_junko_front = self.get_automarker_name('junko_front')
        # mrk_edison_look_out = self.get_automarker_name('edison_look_out')

        # EXTRA DEFINITIONS

        # trent.move_head_ik(group=BG, target_name=mrk_alaric_head_top, immediately=True)
        # trent.move_eye_ik(group=BG, target_name=mrk_alaric_talk, immediately=True)
        # alaric.move_head_ik(group=BG, target_name=mrk_trent_init, immediately=True)
        # alaric.move_eye_ik(group=BG, target_name=mrk_trent_init, immediately=True)
        # edison.move_head_ik(group=BG, target_name=mrk_junko_front, immediately=True)
        # edison.move_eye_ik(group=BG, target_name=mrk_junko_talk, immediately=True)
        # junko.move_head_ik(group=BG, target_name=mrk_edison_front, immediately=True)
        # junko.move_eye_ik(group=BG, target_name=mrk_edison_talk, immediately=True)
        #
        # alaric.start_head_ik(group=MAIN, duration=1000)
        # alaric.start_eye_ik(group=MAIN, duration=1000)
        # trent_head_ik = trent.start_head_ik(group=MAIN, duration=1000)
        # trent_eye_ik = trent.start_eye_ik(group=MAIN, duration=1000)

        cam_dbg.set(group=MAIN)


        main_group.append_time(1)
