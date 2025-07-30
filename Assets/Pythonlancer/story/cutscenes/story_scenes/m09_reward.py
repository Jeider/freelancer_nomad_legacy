from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import Male, Female

from story import actors


class Msn9RewardCutsceneThorn(Scene):
    SCENE_AMBIENT = [30, 30, 10]
    POINT_ROTATE_OVERRIDES = {
        'hassler_talk': (0, 150, 0),
        'trent_talk': (0, 135, 0),
        'darcy_talk': (0, 45, 0),
        'bottle_wine_1': (90, 0, 0),
        'tenji_glass': (90, 0, 0),
        'trent_glass': (90, 0, 0),
        'dj_board': (0, 180, 0),
    }

    def action(self):
        main_group = self.get_group(MAIN)

        floor_height = self.get_point('floor_height').position[1]


        # CAMERAS

        cam_dbg = LookAtCamera(root=self, name='cam_dbg', fov=40)
        # cam_start = LookAtCamera(root=self, name='cam_start', fov=35)
        # cam_dance = LookAtCamera(root=self, name='cam_dance', fov=30)
        # cam_hassler = LookAtCamera(root=self, name='cam_hassler', fov=20)
        # cam_tenji = LookAtCamera(root=self, name='cam_tenji', fov=20)
        # cam_tenji_near = LookAtCamera(root=self, name='cam_tenji_near', fov=18)
        # cam_friends = LookAtCamera(root=self, name='cam_friends', fov=24)
        # cam_trent = LookAtCamera(root=self, name='cam_trent', fov=16)
        # cam_darcy = LookAtCamera(root=self, name='cam_darcy', fov=16)

        # PROPS

        # CHARACTERS

        # darcy = Character(root=self, actor=actors.Darcy, light_group=0, init_point='darcy_init', rotate_y=90,
        #                   floor_height=0)
        # trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='trent_init', rotate_y=90,
        #                   floor_height=0)
        # hassler = Character(root=self, actor=actors.HasslerOrder, light_group=0, init_point='hassler_init', rotate_y=90)

        # MARKERS

        # mrk_tenji_sit = trent.get_sit_marker('yamamoto_init')
        # mrk_trent_sit = trent.get_sit_marker('trent_talk')
        # mrk_darcy_sit = darcy.get_sit_marker('darcy_talk')
        #
        # mrk_tenji_front = self.get_automarker_name('yamamoto_front')
        # mrk_tenji_to_trent = self.get_automarker_name('yamamoto_trentlook')
        # mrk_darcy_front = self.get_automarker_name('darcy_front')
        # mrk_trent_front = self.get_automarker_name('darcy_looktrent')
        # mrk_go_start = self.get_automarker_name('go_start')
        # mrk_go_end = self.get_automarker_name('go_end')

        cam_dbg.set(group=MAIN)
