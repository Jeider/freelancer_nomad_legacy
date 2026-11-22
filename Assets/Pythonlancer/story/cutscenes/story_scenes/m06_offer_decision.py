"""m06_offer_decision: полная постановка из master; точки в m06_offer_decision.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character, Female, LookAtCamera, MAIN, Male, MotionEvent,
)
from story.cutscenes.anim import (
    Female, Male,
)
from story import actors


class CharTrentActor(actors.Actor):
    NAME = 'trent'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'trent'


class M06OfferDecisionScene(Scene):
    DUMP_FILE = 'm06_offer_decision'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)
        self.set_duration(5000.0)

        # Персонажи, камеры, реквизит и звук.
        trent = Character(root=self, actor=CharTrentActor, name='Char_trent', light_group=0,
            init_point='Char_trent', rotate_from_quat=True, appearance='trent', actor_name='Player')
        alaric = Character(root=self, actor=actors.Alaric, name='Char_alaric', light_group=0,
            init_point='Char_alaric', rotate_from_quat=True, use_ambient=True, appearance='alaric',
            actor_name='Alaric')
        hatcher = Character(root=self, actor=actors.Hatcher, name='Char_hatcher', light_group=0,
            init_point='Char_hatcher', rotate_from_quat=True, appearance='hatcher', actor_name='Hatcher')
        cam_scene = LookAtCamera(root=self, name='cam_scene', fov=30, look_duration=1)

        # Исходные точки взгляда.

        # Абсолютное время исходной сцены; часы MAIN не сдвигаются.
        t = 0
        cam_scene.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, duration=5000, loop=True,
            time_delay=t)
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=5000, loop=True,
            time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=trent.name, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05,
            duration=5000, loop=True, time_delay=t)
