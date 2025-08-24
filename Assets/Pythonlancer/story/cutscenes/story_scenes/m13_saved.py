from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import Male, Female, Trent

from story import actors


class TestShip(Ship):
    COMPOUND_TEMPLATE_NAME = 'li_elite'


class SceneBackground(BackgroundProp):
    COMPOUND_TEMPLATE_NAME = 'edge_exclusion'


class Msn13KriegDeathScene(Scene):
    POINT_ROTATE_OVERRIDES = {}

    def action(self):
        main_group = self.get_group(MAIN)

        cam_dbg = LookAtCamera(root=self, name='cam_dbg', fov=40)

        ship_ambi = Light(root=self, name='test_ambi', point_name=self.DEFAULT_POINT_NAME,
                          light_group=0, diffuse=[1, 1, 0.5],
                          ambient=[0, 0, 0], direction=[0, 0, 1], light_type=L_DIRECT, range=2000, cutoff=150)

        bg = SceneBackground(root=self, name='the_scene_bg', light_group=0, init_point=self.DEFAULT_POINT_NAME)


        elite_ship = TestShip(root=self, name='liberty_elite_ship', init_point='ship', light_group=0)
        #
        # path = MotionPath(root=self, name='the_path1', path_data=PATH_3)
        # path.anim(group=MAIN, duration=10, target_name=elite_ship.name, adjust_orient=True, time_delay=1, smooth=True)

        # LookAtEvent(
        #     root=self, group=BG,
        #     point=elite_ship, focus=self.get_automarker('shiplook'),
        #     duration=20,
        # )

        cam_dbg.set(group=MAIN)

        main_group.append_time(1000)
