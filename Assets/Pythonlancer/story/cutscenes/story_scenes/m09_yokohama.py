from story.cutscenes.scene import Scene
from story.cutscenes.content import Character, LookAtCamera, MoveEvent, BG, MAIN

from story.actors import Trent, Darcy, HasslerOrder


class Msn9YokohamaCutsceneThorn(Scene):

    def action(self):
        cam_dbg = LookAtCamera(root=self, name='cam_dbg', fov=25)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=22)
        cam_darcy = LookAtCamera(root=self, name='cam_darcy', fov=22)
        cam_hassler = LookAtCamera(root=self, name='cam_hassler', fov=22)

        # cam_dbg.move_cam(group=MAIN, index=2, duration=10, smooth=False)
        # cam_dbg.move_focus(group=MAIN, index=2, duration=10, time_delay=2)

        cam_dbg.set(group=MAIN)

        darcy = Character(root=self, actor=Darcy, light_group=0, init_point='darcy_init', rotate=90)
        darcy.idle(group=MAIN)

        trent = Character(root=self, actor=Trent, light_group=0, init_point='trent_init', rotate=90)
        trent.idle(group=MAIN)

        hassler = Character(root=self, actor=HasslerOrder, light_group=0, init_point='hassler_init', rotate=90)
        hassler.idle(group=MAIN)

        cam_trent.set(group=MAIN, time_delay=2, time_append=2)
        trent.facial(group=MAIN, index=10)

        cam_darcy.set(group=MAIN)
        darcy.facial(group=MAIN, index=20)

        cam_trent.set(group=MAIN)
        trent.facial(group=MAIN, index=30)

        cam_darcy.set(group=MAIN)
        darcy.facial(group=MAIN, index=40)

        cam_hassler.set(group=MAIN)
        hassler.facial(group=MAIN, index=50)

        cam_trent.set(group=MAIN)
        trent.facial(group=MAIN, index=60)

        cam_hassler.set(group=MAIN)
        hassler.facial(group=MAIN, index=70)
        hassler.facial(group=MAIN, index=80, extra_delay=0)

        cam_trent.set(group=MAIN)
        trent.facial(group=MAIN, index=90)

        cam_hassler.set(group=MAIN)
        hassler.facial(group=MAIN, index=100)
        hassler.facial(group=MAIN, index=110, extra_delay=0)

        cam_trent.set(group=MAIN)
        trent.facial(group=MAIN, index=120)

        cam_hassler.set(group=MAIN)
        hassler.facial(group=MAIN, index=130)




