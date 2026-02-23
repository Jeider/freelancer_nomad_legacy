from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import Male, Female, Trent
from story.cutscenes import sequence

from story import actors





class SceneBackground(BackgroundProp):
    COMPOUND_TEMPLATE_NAME = 'co_cad_nebula'


class DebugScene(Scene):
    DUMP_FILE = 'debug'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        SceneBackground(root=self, name='scene_bg1', light_group=100, init_point=self.DEFAULT_POINT_NAME, rotate_y=-180)

        PlayerShip(root=self, name='playership_the', light_group=0, init_point='waypoin')

        cam_char1 = StaticCamera(root=self, name='cam_char1', fov=18)

        trent = Character(root=self, actor=actors.EdisonTrentHolo, light_group=0, init_point='char1', rotate_from_quat=True,
                           use_ambient=True)

        trent.idle(group=MAIN)
        cam_char1.set(group=MAIN)

        main_group.append_time(1111)
