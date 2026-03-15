from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import Male, Female, Trent
from story.cutscenes import sequence

from story import actors



class PrinceWalesScene(Scene):
    DUMP_FILE = 'br_battleship_deck'

    def action(self):
        main_group = self.get_group(MAIN)

        Light(root=self, name='ROOMA', point_name='light1', light_group=0, diffuse=[1, 0.9, 0.8],
              ambient=[0, 0, 0], direction=[0, 0, -1], light_type=L_POINT, range=15)

        cam_greet = StaticCamera(root=self, name='cam_greetxx', fov=25)
        cam_char1 = StaticCamera(root=self, name='cam_char222', fov=16)
        cam_char2 = StaticCamera(root=self, name='cam_char111', fov=18)

        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='char222', rotate_from_quat=True,
                           camera=cam_char1, anim_sequence=sequence.SEQUENCE_MALE_STAND_FSTHIPB_CROSS)
        kenji = Character(root=self, actor=actors.Darcy, light_group=0, init_point='char111', rotate_from_quat=True,
                           camera=cam_char2, anim_sequence=sequence.SEQUENCE_FEMALE_STAND_FSTHIPB_ONCE)

        trent.idle(group=MAIN)
        kenji.idle(group=MAIN)

        mrk_trent = trent.get_stand_marker('char222')
        mrk_kenji = kenji.get_stand_marker('char111')

        trent.move_head_ik(group=MAIN, target_name=mrk_kenji, immediately=True)
        kenji.move_head_ik(group=MAIN, target_name=mrk_trent, immediately=True)

        trent.start_head_ik(group=MAIN, duration=1000)
        kenji.start_head_ik(group=MAIN, duration=1000)

        cam_greet.set(group=MAIN)
        cam_greet.move_cam(group=MAIN, index=2, duration=6, smooth=True)

        main_group.append_time(6)

        Autoplay(
            self,
            group=MAIN,
            start_index=0,
        )

        main_group.append_time(2)


class SpragueScene(Scene):
    DUMP_FILE = 'dig_site'

    def action(self):
        main_group = self.get_group(MAIN)

        cam_greet = StaticCamera(root=self, name='cam_greetx', fov=25)
        cam_char1 = StaticCamera(root=self, name='cam_char1', fov=18)
        cam_char1_from2 = StaticCamera(root=self, name='cam_char1_from2', fov=18)
        cam_char2 = StaticCamera(root=self, name='cam_char2', fov=18)
        cam_char2_from1 = StaticCamera(root=self, name='cam_char2_from1', fov=19)
        cam_char3 = StaticCamera(root=self, name='cam_char3', fov=18)
        cam_char4 = StaticCamera(root=self, name='cam_char4', fov=18)

        char1 = Character(root=self, light_group=0, init_point='char1', rotate_from_quat=True, camera=cam_char1_from2,
                          actor=actors.Trent, anim_sequence=sequence.SEQUENCE_MALE_STAND_FSTHIPB_CROSS_FAST)

        char2 = Character(root=self,light_group=0, init_point='char2', rotate_from_quat=True, camera=cam_char2,
                          actor=actors.Mandrake, anim_sequence=sequence.SEQUENCE_MALE_STAND_RHAND)
        #
        # char3 = Character(root=self, light_group=0, init_point='char3', rotate_from_quat=True, camera=cam_char3,
        #                   actor=actors.Kenji, anim_sequence=sequence.SEQUENCE_MALE_STAND_LHAND)

        char4 = Character(root=self,light_group=0, init_point='char4', rotate_from_quat=True, camera=cam_char4,
                          actor=actors.Hatcher, anim_sequence=sequence.SEQUENCE_FEMALE_STAND_RHAND_ALT)

        trent = char1
        mandrake = char2
        hatcher = char4

        char1.idle(group=MAIN)
        char2.idle(group=MAIN)
        # char3.idle(group=MAIN)
        char4.idle(group=MAIN)

        mrk_char1 = char1.get_stand_marker('char1')
        mrk_char2 = char2.get_stand_marker('char2')
        # mrk_char3 = char2.get_stand_marker('char3')
        mrk_char4 = char2.get_stand_marker('char4')
        mrk_char1_alt = self.get_automarker_name('mrk_char1_alt')
        mrk_char2_alt = self.get_automarker_name('mrk_char2_alt')
        mrk_char4_alt = self.get_automarker_name('mrk_char4_alt')


        char1.move_head_ik(group=MAIN, target_name=mrk_char2_alt, immediately=True)
        char2.move_head_ik(group=MAIN, target_name=mrk_char1_alt, immediately=True)
        # char3.move_head_ik(group=MAIN, target_name=mrk_char1_alt, immediately=True)
        char4.move_head_ik(group=MAIN, target_name=mrk_char1, immediately=True)

        char1.start_head_ik(group=MAIN, duration=1000)
        char2.start_head_ik(group=MAIN, duration=1000)
        # char3.start_head_ik(group=MAIN, duration=1000, time_delay=6)
        char4.start_head_ik(group=MAIN, duration=1000)

        cam_greet.set(group=MAIN)
        cam_greet.move_cam(group=MAIN, index=2, duration=6, smooth=True)





        main_group.append_time(6)

        Autoplay(
            self,
            group=MAIN,
            start_index=0,
            finish_index=100,
        )

        trent.set_camera(cam_char1)


        Autoplay(
            self,
            group=MAIN,
            start_index=110,
            # finish_index=60,
            head_ik_per_index={
                120: [
                    IkDelay(char1, mrk_char4, duration=2.6, time_delay=-0.25),
                ],
            }
        )

        main_group.append_time(2)

        return

        MoveFastEvent(root=self, group=MAIN, object_name=char2.name, target_name=self.get_automarker_name('char2'))
        char2.idle(group=MAIN)
        main_group.append_time(0.01)
        char2.start_head_ik(group=MAIN, duration=1000)

        darcy.set_camera(cam_char1_from2)


        Autoplay(
            self,
            group=MAIN,
            start_index=70,
            finish_index=80,
            head_ik_per_index={
                80: [
                    IkDelay(char1, mrk_char2_alt, duration=2.6, time_delay=-0.25),
                ],
            }
        )
        jack.set_camera(cam_char2_from1)
        jack.move_head_ik(group=MAIN, target_name=mrk_char1, duration=3)

        Autoplay(
            self,
            group=MAIN,
            start_index=90,
            finish_index=140,
        )

        darcy.move_head_ik(group=MAIN, target_name=mrk_char4, duration=2.5, time_delay=1)
        jack.set_camera(cam_char2)
        darcy.set_camera(cam_char1)

        Autoplay(
            self,
            group=MAIN,
            start_index=150,
            head_ik_per_index={
                170: [
                    IkDelay(char2, mrk_char4_alt, duration=2.5, time_delay=-0.5),
                ],
            }
        )

        main_group.append_time(1)
