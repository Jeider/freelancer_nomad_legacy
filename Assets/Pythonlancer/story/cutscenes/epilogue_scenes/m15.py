from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import Male, Female, Trent
from story.cutscenes import sequence

from story import actors



class KenjiMeetScene(Scene):
    DUMP_FILE = 'bw_ocho_rios'

    def action(self):
        main_group = self.get_group(MAIN)

        cam_greet = StaticCamera(root=self, name='cam_greet', fov=25)
        cam_char1 = StaticCamera(root=self, name='cam_char1', fov=18)
        cam_char2 = StaticCamera(root=self, name='cam_char2', fov=18)

        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='char1', rotate_from_quat=True,
                           camera=cam_char1, anim_sequence=sequence.SEQUENCE_MALE_STAND_CROSS_FSTHIPB)
        kenji = Character(root=self, actor=actors.Kenji, light_group=0, init_point='char2', rotate_from_quat=True,
                           camera=cam_char2, anim_sequence=sequence.SEQUENCE_MALE_STAND_RHAND_ALT)

        trent.idle(group=MAIN)
        kenji.idle(group=MAIN)

        mrk_trent = trent.get_stand_marker('char1')
        mrk_kenji = kenji.get_stand_marker('char2')

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


class KyotoScene(Scene):
    DUMP_FILE = 'ku_station_bar'

    def action(self):
        main_group = self.get_group(MAIN)


        bartender_fixture = Character(root=self, actor=actors.BartenderFixture, light_group=0, init_point=self.DEFAULT_POINT_NAME, rotate_y=180)
        MoveOffscreenEvent(root=self, group=BG, object_name=bartender_fixture.name)


        cam_greet = StaticCamera(root=self, name='cam_greet', fov=25)
        cam_char1 = StaticCamera(root=self, name='cam_char1', fov=18)
        cam_char2 = StaticCamera(root=self, name='cam_char2', fov=18)
        cam_char3 = StaticCamera(root=self, name='cam_char3', fov=18)
        cam_char4 = StaticCamera(root=self, name='cam_char4', fov=18)

        char1 = Character(root=self,light_group=0, init_point='char1', rotate_from_quat=True, camera=cam_char1,
                          actor=actors.Otomo, anim_sequence=sequence.SEQUENCE_MALE_STAND_CROSS_FSTHIPB)

        char2 = Character(root=self,light_group=0, init_point='char2', rotate_from_quat=True, camera=cam_char2,
                          actor=actors.Shinja, anim_sequence=sequence.SEQUENCE_MALE_STAND_RHAND_ALT)

        char3 = Character(root=self, light_group=0, init_point='char3', rotate_from_quat=True, camera=cam_char3,
                          actor=actors.Kenji, anim_sequence=sequence.SEQUENCE_MALE_STAND_LHAND)

        char4 = Character(root=self,light_group=0, init_point='char4', rotate_from_quat=True, camera=cam_char4,
                          actor=actors.Trent, anim_sequence=sequence.SEQUENCE_MALE_STAND_FSTHIPB)

        char1.idle(group=MAIN)
        char2.idle(group=MAIN)
        char3.idle(group=MAIN)
        char4.idle(group=MAIN)

        mrk_char1 = char1.get_stand_marker('char1')
        mrk_char2 = char2.get_stand_marker('char2')
        mrk_char3 = char2.get_stand_marker('char3')
        mrk_char4 = char2.get_stand_marker('char4')
        mrk_char1_alt = self.get_automarker_name('mrk_char1_alt')



        char1.move_head_ik(group=MAIN, target_name=mrk_char3, immediately=True)
        char2.move_head_ik(group=MAIN, target_name=mrk_char3, immediately=True)
        char3.move_head_ik(group=MAIN, target_name=mrk_char1_alt, immediately=True)
        char4.move_head_ik(group=MAIN, target_name=mrk_char2, immediately=True)

        char1.start_head_ik(group=MAIN, duration=1000)
        char2.start_head_ik(group=MAIN, duration=1000, time_delay=4)
        char3.start_head_ik(group=MAIN, duration=1000, time_delay=6)
        char4.start_head_ik(group=MAIN, duration=1000, time_delay=6)

        cam_greet.set(group=MAIN)
        cam_greet.move_cam(group=MAIN, index=2, duration=6, smooth=True)

        main_group.append_time(6)

        Autoplay(
            self,
            group=MAIN,
            start_index=0,
            head_ik_per_index={
                30: [
                    IkDelay(char3, mrk_char4, duration=2.5, time_delay=0.5),
                ],
                40: [
                    IkDelay(char1, mrk_char4, duration=1.7),
                ],
                50: [
                    IkDelay(char2, mrk_char4, duration=1.2, time_delay=-0.5),
                    IkDelay(char3, mrk_char1_alt, duration=1.2),
                ],

                120: [
                    IkDelay(char1, mrk_char3, duration=1.3),
                ],

                130: [
                    IkDelay(char3, mrk_char2, duration=2),
                ],
                140: [
                    IkDelay(char3, mrk_char4, duration=2),
                    IkDelay(char4, mrk_char3, duration=2),
                ],
            }
        )

        main_group.append_time(2)




class HokkaidoScene(Scene):
    DUMP_FILE = 'ku_hokkaido_bar'

    def action(self):
        main_group = self.get_group(MAIN)


        bartender_fixture = Character(root=self, actor=actors.BartenderFixture, light_group=0, init_point=self.DEFAULT_POINT_NAME, rotate_y=180)
        MoveOffscreenEvent(root=self, group=BG, object_name=bartender_fixture.name)


        cam_greet = StaticCamera(root=self, name='cam_greet', fov=25)
        cam_char1 = StaticCamera(root=self, name='cam_char1', fov=18)
        cam_char2 = StaticCamera(root=self, name='cam_char2', fov=18)
        cam_char3 = StaticCamera(root=self, name='cam_char3', fov=18)
        cam_char4 = StaticCamera(root=self, name='cam_char4', fov=18)

        char1 = Character(root=self,light_group=0, init_point='char1', rotate_from_quat=True, camera=cam_char1,
                          actor=actors.HasslerEpilogue, anim_sequence=sequence.SEQUENCE_MALE_STAND_LHAND)

        char2 = Character(root=self,light_group=0, init_point='char2', rotate_from_quat=True, camera=cam_char2,
                          actor=actors.Kenji, anim_sequence=sequence.SEQUENCE_MALE_STAND_LHAND_ONLY)
        #
        # char3 = Character(root=self, light_group=0, init_point='char3', rotate_from_quat=True, camera=cam_char3,
        #                   actor=actors.Kenji, anim_sequence=sequence.SEQUENCE_MALE_STAND_LHAND)

        char4 = Character(root=self,light_group=0, init_point='char4', rotate_from_quat=True, camera=cam_char4,
                          actor=actors.Trent, anim_sequence=sequence.SEQUENCE_MALE_STAND_FSTHIPB_CROSS)

        char1.idle(group=MAIN)
        char2.idle(group=MAIN)
        # char3.idle(group=MAIN)
        char4.idle(group=MAIN)

        mrk_char1 = char1.get_stand_marker('char1')
        mrk_char2 = char2.get_stand_marker('char2')
        # mrk_char3 = char2.get_stand_marker('char3')
        mrk_char4 = char2.get_stand_marker('char4')
        mrk_char2_alt = self.get_automarker_name('mrk_char2_alt')


        char1.move_head_ik(group=MAIN, target_name=mrk_char4, immediately=True)
        char2.move_head_ik(group=MAIN, target_name=mrk_char2_alt, immediately=True)
        # char3.move_head_ik(group=MAIN, target_name=mrk_char1_alt, immediately=True)
        char4.move_head_ik(group=MAIN, target_name=mrk_char1, immediately=True)

        char1.start_head_ik(group=MAIN, duration=1000, time_delay=6)
        char2.start_head_ik(group=MAIN, duration=1000, time_delay=14)
        # char3.start_head_ik(group=MAIN, duration=1000, time_delay=6)
        char4.start_head_ik(group=MAIN, duration=1000, time_delay=6)

        cam_greet.set(group=MAIN)
        cam_greet.move_cam(group=MAIN, index=2, duration=6, smooth=True)

        main_group.append_time(6)

        Autoplay(
            self,
            group=MAIN,
            start_index=0,
            head_ik_per_index={
                170: [
                    IkDelay(char1, mrk_char2, duration=1.8, time_delay=1),
                ],
                180: [
                    IkDelay(char2, mrk_char4, duration=1.7),
                    IkDelay(char4, mrk_char2_alt, duration=1.7),
                ],
                190: [
                    IkDelay(char4, mrk_char1, duration=2),
                ],
                200: [
                    IkDelay(char1, mrk_char4, duration=1.8),
                ],
            }
        )

        main_group.append_time(1)