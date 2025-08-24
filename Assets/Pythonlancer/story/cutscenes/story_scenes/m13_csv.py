from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import Male, Female, Trent

from story import actors


class CSV(Ship):
    COMPOUND_TEMPLATE_NAME = 'ge_csv'


class SceneBackground(BackgroundProp):
    COMPOUND_TEMPLATE_NAME = 'om13_nebula'


class Stars(BackgroundProp):
    COMPOUND_TEMPLATE_NAME = 'new_generic'


class Msn13CSVMagnetScene(Scene):
    POINT_ROTATE_OVERRIDES = {}

    def action(self):
        main_group = self.get_group(MAIN)

        SceneBackground(root=self, name='scene_bg1', light_group=100, init_point=self.DEFAULT_POINT_NAME)
        SceneBackground(root=self, name='scene_bg2', light_group=100, init_point=self.DEFAULT_POINT_NAME)

        playership = PlayerShip(root=self, name='playership_the', light_group=0, init_point=self.DEFAULT_POINT_NAME)

        cam_dbg = LookAtCamera(root=self, name='cam_dbg', fov=40)

        Light(root=self, name='test_ambi', point_name=self.DEFAULT_POINT_NAME,
              light_group=0, diffuse=[1, 0.5, 0.8],
              ambient=[0, 0, 0], direction=[0, 0, 1], light_type=L_DIRECT, range=2000, cutoff=150)


        # elite_ship = TestShip(root=self, name='liberty_elite_ship', init_point='ship', light_group=0)
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
