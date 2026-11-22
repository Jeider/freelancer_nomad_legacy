"""m08_offer_decision: полная постановка из master; точки в m08_offer_decision.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character, Female, LookAtCamera, MAIN, Male, MotionEvent, RotateAxisEvent,
)
from story.cutscenes.anim import (
    Female, Male,
)
from story import actors


class CharKaytlinActor(actors.Actor):
    NAME = 'kaytlin'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'kaytlin'

class CharTrentActor(actors.Actor):
    NAME = 'trent'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'trent'


class M08OfferDecisionScene(Scene):
    DUMP_FILE = 'm08_offer_decision'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)
        self.set_duration(267111111.0)

        # Персонажи, камеры, реквизит и звук.
        kaytlin = Character(root=self, actor=CharKaytlinActor, name='Char_kaytlin', light_group=0,
            init_point='Char_kaytlin', rotate_from_quat=True, appearance='kaytlin', actor_name='Kaytlin')
        brighton = Character(root=self, actor=actors.Brighton, name='Char_brighton', light_group=0,
            init_point='Char_brighton', rotate_from_quat=True, appearance='brighton', actor_name='Brighton')
        darcy = Character(root=self, actor=actors.Darcy, name='Char_darcy', light_group=0,
            init_point='Char_darcy', rotate_from_quat=True, appearance='darcy', actor_name='Darcy')
        trent = Character(root=self, actor=CharTrentActor, name='Char_trent', light_group=0,
            init_point='Char_trent', rotate_from_quat=True, appearance='trent', actor_name='Player')
        cam_trent_far = LookAtCamera(root=self, name='cam_trent_far', fov=18, look_duration=710)

        # Исходные точки взгляда.

        # Абсолютное время исходной сцены; часы MAIN не сдвигаются.
        t = 0
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_IDLE_000LV_XA_05, duration=10, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=kaytlin.name, anim=Female.Sc_FMBODY_CHRF_IDLE_000LV_XA_05,
            duration=10, time_delay=t)
        brighton.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=100, time_scale=0.6,
            loop=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=trent.name, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05,
            duration=100, time_scale=0.6, loop=True, time_delay=t)
        cam_trent_far.set(group=MAIN, time_delay=t)
        t += 0.01
        RotateAxisEvent(root=self, group=MAIN, object_name=darcy.name, angle=-25, axis='Y_AXIS', duration=0,
            smooth=False, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=kaytlin.name, angle=-125, axis='Y_AXIS', duration=0,
            smooth=False, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=brighton.name, angle=10, axis='Y_AXIS', duration=0,
            smooth=False, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=20, axis='Y_AXIS', duration=0,
            smooth=False, time_delay=t)
