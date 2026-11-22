"""m03_offer_decision: полная постановка из master; точки в m03_offer_decision.blend."""
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


class M03OfferDecisionScene(Scene):
    DUMP_FILE = 'm03_offer_decision'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)
        self.set_duration(1000.0)

        # Персонажи, камеры, реквизит и звук.
        trent = Character(root=self, actor=CharTrentActor, name='Char_trent', light_group=0,
            init_point='Char_trent', rotate_from_quat=True, appearance='trent', actor_name='Player')
        hassler = Character(root=self, actor=actors.Hassler, name='Char_hassler', light_group=0,
            init_point='Char_hassler', rotate_from_quat=True, appearance='hassler', actor_name='hassler')
        wilham = Character(root=self, actor=actors.Wilham, name='Char_wilham', light_group=0,
            init_point='Char_wilham', rotate_from_quat=True, appearance='wilham', actor_name='wilham')
        cam_decision = LookAtCamera(root=self, name='cam_decision', fov=35, look_duration=300)

        # Исходные точки взгляда.

        # Абсолютное время исходной сцены; часы MAIN не сдвигаются.
        t = 0
        cam_decision.set(group=MAIN, time_delay=t)
        hassler.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_BRTH_000LV_xa_05, duration=1000, time_scale=0.5,
            loop=True, time_delay=t)
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_MED_000LV_xa_05, duration=1000, time_scale=0.5,
            loop=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=trent.name, anim=Male.Sc_MLBODY_STND_IDLE_BIG_000LV_xa_05,
            duration=1000, time_scale=0.5, loop=True, time_delay=t)
