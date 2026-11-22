"""m07_offer_decision: полная постановка из master; точки в m07_offer_decision.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character, LookAtCamera, MAIN, Male, MotionEvent, MoveEvent,
)
from story.cutscenes.anim import (
    Male,
)
from story import actors


class CharTrentBaseActor(actors.Actor):
    NAME = 'trent_base'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'trent'

class CharTrentActor(actors.Actor):
    NAME = 'trent'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'trent_original'

class CharBarmanActor(actors.Actor):
    NAME = 'barman'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm07_bartender'


class M07OfferDecisionScene(Scene):
    DUMP_FILE = 'm07_offer_decision'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)
        self.set_duration(140.0)

        # Персонажи, камеры, реквизит и звук.
        bartender_fixture = Character(root=self, actor=actors.BartenderFixture, name='Char_bartender_Fixture',
            light_group=0, init_point='Char_bartender_Fixture', rotate_from_quat=True,
            appearance='li_bartender_1', actor_name='bartender', floor_height=-110.0)
        trent_base = Character(root=self, actor=CharTrentBaseActor, name='Char_trent_base', light_group=0,
            init_point='Char_trent_base', rotate_from_quat=True, appearance='trent', actor_name='Player',
            floor_height=-1000)
        trent = Character(root=self, actor=CharTrentActor, name='Char_trent', light_group=0,
            init_point='Char_trent', rotate_from_quat=True, appearance='trent_original',
            actor_name='TrentOriginal')
        barman = Character(root=self, actor=CharBarmanActor, name='Char_barman', light_group=0,
            init_point='Char_barman', rotate_from_quat=True, appearance='m07_bartender',
            actor_name='m6_bartender', floor_height=-110.0)
        cam_trent_deal = LookAtCamera(root=self, name='cam_trent_deal', fov=20, look_duration=70)

        # Исходные точки взгляда.

        # Абсолютное время исходной сцены; часы MAIN не сдвигаются.
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=bartender_fixture.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=trent_base.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=barman.name, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04,
            duration=10000, loop=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=trent.name, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04,
            duration=10000, loop=True, time_delay=t)
        cam_trent_deal.set(group=MAIN, time_delay=t)
