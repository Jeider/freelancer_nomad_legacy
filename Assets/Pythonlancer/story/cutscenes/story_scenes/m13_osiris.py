from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import Male, Female, Trent

from story import actors


class EliteShip(Ship):
    COMPOUND_TEMPLATE_NAME = 'li_elite2'


class Msn13OsirisScene(Scene):
    POINT_ROTATE_OVERRIDES = {
        'li_comm': (0, 180, 0),
        'alaric_comm': (0, 90, 0),
    }

    def action(self):
        main_group = self.get_group(MAIN)
        # mandrake_floor_height = self.get_point('mandrake_floor').position[1]

        # CAMERAS

        cam_dbg = LookAtCamera(root=self, name='cam_dbg', fov=30)
        # cam_start = LookAtCamera(root=self, name='cam_start', fov=24)
        # cam_hatcher = LookAtCamera(root=self, name='cam_hatcher', fov=18)
        # cam_trent = LookAtCamera(root=self, name='cam_trent', fov=18)
        # cam_king = LookAtCamera(root=self, name='cam_king', fov=16)
        # cam_comm = LookAtCamera(root=self, name='cam_comm', fov=22)
        # cam_team = LookAtCamera(root=self, name='cam_team', fov=24)
        # cam_insane = LookAtCamera(root=self, name='cam_insane', fov=18)


        # PROPS

        elite_ship = EliteShip(root=self, name='liberty_elite_ship', init_point='ship', light_group=3, rotate_y=-130,
                               loadout='rtc_m13_osiris_ship')

        # CHARACTERS
        #
        # trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='trent_init', rotate_y=0)
        # king = Character(root=self, actor=actors.King, light_group=king_light, init_point='king_init', rotate_y=-135)
        # hatcher = Character(root=self, actor=actors.Hatcher, light_group=0, init_point='hatcher_init', rotate_y=0)
        # alaric = Character(root=self, actor=actors.Alaric, light_group=king_light, init_point='alaric_init', rotate_y=0)
        # darcy = Character(root=self, actor=actors.Darcy, light_group=0, init_point='darcy_init', rotate_y=0)
        # mandrake = Character(root=self, actor=actors.Mandrake, init_point='mandrake_comm', rotate_y=-90,
        #                      floor_height=mandrake_floor_height, light_group=comm_light)
        # bartender_fixture = Character(root=self, actor=actors.BartenderFixture, light_group=0, init_point=self.DEFAULT_POINT_NAME, rotate_y=180)
        #
        # guard = Character(root=self, actor=actors.OsirisOfficer, light_group=0, init_point='guard_init', rotate_y=90)
        #
        # MoveOffscreenEvent(root=self, group=BG, object_name=bartender_fixture.name)


        # MARKERS
        #
        # mrk_trent_talk = trent.get_stand_marker('trent_talk')
        # mrk_hatcher_talk = trent.get_stand_marker('hatcher_talk')
        # mrk_king = trent.get_stand_marker('king_init')
        # mrk_alaric_comm = trent.get_stand_marker('alaric_comm')
        # # mrk_mandrake_comm = trent.get_stand_marker('mandrake_comm')
        #
        # mrk_mandrake = self.get_automarker_name('mrk_mandrake')
        # mrk_trent_front = self.get_automarker_name('mrk_trent_front')
        # mrk_trent_front2 = self.get_automarker_name('mrk_trent_front2')
        # mrk_trent_front_eye = self.get_automarker_name('mrk_trent_front_eye')

        # PREPARE
        #
        # hatcher.move_head_ik(group=BG, target_name=mrk_king, immediately=True)
        # hatcher.move_eye_ik(group=BG, target_name=mrk_king, immediately=True)

        # ACTION!

        # cam_start.set(group=MAIN)

        elite_ship.anim(group=MAIN, anim='Sc_force extend')


        main_group.append_time(1000)