"""m04_offer_decision: полная постановка из master; точки в m04_offer_decision.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character, LookAtCamera, MAIN, Male, MotionEvent,
)
from story.cutscenes.anim import (
    Male,
)
from story import actors


class CharTrentActor(actors.Actor):
    NAME = 'trent'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'trent'


class M04OfferDecisionScene(Scene):
    DUMP_FILE = 'm04_offer_decision'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)
        self.set_duration(5555.0)

        # Персонажи, камеры, реквизит и звук.
        trent = Character(root=self, actor=CharTrentActor, name='Char_trent', light_group=0,
            init_point='Char_trent', rotate_from_quat=True, appearance='trent', actor_name='Player')
        jacobo = Character(root=self, actor=actors.Jacobo, name='Char_jacobo', light_group=0,
            init_point='Char_jacobo', rotate_from_quat=True, appearance='jacobo', actor_name='jacobo')
        cam_table = LookAtCamera(root=self, name='cam_table', fov=20, look_duration=300)

        # Исходные точки взгляда.

        # Абсолютное время исходной сцены; часы MAIN не сдвигаются.
        t = 0
        cam_table.set(group=MAIN, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=trent.name, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06,
            duration=5555, loop=True, time_delay=t)
        jacobo.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=5555, loop=True,
            time_delay=t)
