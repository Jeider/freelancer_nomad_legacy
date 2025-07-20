from story.cutscenes.scene import Scene
from story.cutscenes.content import Character, LookAtCamera, MoveEvent, BG, MAIN

from story.actors import Trent, Darcy


class Msn9YokohamaCutsceneThorn(Scene):

    def action(self):
        cam_dbg = LookAtCamera(root=self, name='cam_dbg', fov=25)
        cam_dbg.move_cam(group=MAIN, index=2, duration=10, smooth=False)
        cam_dbg.move_focus(group=MAIN, index=2, duration=10, time_delay=2)

        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=22)
        cam_darcy = LookAtCamera(root=self, name='cam_darcy', fov=22)

        darcy = Character(root=self, actor=Darcy, light_group=0, init_point='darcy_init', rotate=90)
        darcy.idle(group=MAIN)

        darcy = Character(root=self, actor=Trent, light_group=0, init_point='trent_init', rotate=90)
        darcy.idle(group=MAIN)




