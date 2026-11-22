"""m05_barman: полная постановка из master; точки в m05_barman.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character, MAIN, Male, MotionEvent,
)
from story.cutscenes.anim import (
    Male,
)
from story import actors


class CharLiBartenderActor(actors.Actor):
    NAME = 'li_bartender'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm05_bartender'


class M05BarmanScene(Scene):
    DUMP_FILE = 'm05_barman'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)
        self.set_duration(63.498)

        # Персонажи, камеры, реквизит и звук.
        li_bartender = Character(root=self, actor=CharLiBartenderActor, name='Char_li_bartender', light_group=0,
            init_point='Char_li_bartender', rotate_from_quat=True, appearance='m05_bartender',
            actor_name='li_host')

        # Исходные точки взгляда.

        # Абсолютное время исходной сцены; часы MAIN не сдвигаются.
        t = 0
        MotionEvent(root=self, group=MAIN, object_name=li_bartender.name,
            anim=Male.Sc_MLBODY_STND_IDLE_BRTH_000LV_xa_05, duration=5, time_delay=t)
        t += 5
        MotionEvent(root=self, group=MAIN, object_name=li_bartender.name,
            anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, duration=3.833, time_delay=t)
        t += 3.833
        MotionEvent(root=self, group=MAIN, object_name=li_bartender.name,
            anim=Male.Sc_MLBODY_STND_HOLD_ARMS_CROSSED_000LV_XA_02, duration=5, loop=True, time_delay=t)
        t += 5
        MotionEvent(root=self, group=MAIN, object_name=li_bartender.name,
            anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, duration=2.033, time_delay=t)
        t += 2.033
        MotionEvent(root=self, group=MAIN, object_name=li_bartender.name,
            anim=Male.Sc_MLBODY_STND_LOOK_WATC_IMPA_315DN_XA_07, duration=7.099, time_delay=t)
        t += 7.099
        MotionEvent(root=self, group=MAIN, object_name=li_bartender.name,
            anim=Male.Sc_MLBODY_STND_IDLE_BRTH_000LV_xa_05, duration=5, time_delay=t)
        t += 5
        MotionEvent(root=self, group=MAIN, object_name=li_bartender.name,
            anim=Male.Sc_MLBODY_STND_ATEASE_HSEC_RLEASE_000LV_XA_03, duration=3, time_delay=t)
        t += 3
        MotionEvent(root=self, group=MAIN, object_name=li_bartender.name,
            anim=Male.Sc_MLBODY_STND_ATEASE_HOLD_000LV_XA_01, duration=3, loop=True, time_delay=t)
        t += 3
        MotionEvent(root=self, group=MAIN, object_name=li_bartender.name,
            anim=Male.Sc_MLBODY_STND_ATEASE_RLEASE_000LV_XA_01, duration=2.966, time_delay=t)
        t += 2.966
        MotionEvent(root=self, group=MAIN, object_name=li_bartender.name,
            anim=Male.Sc_MLBODY_STND_LOOK_AROU_CASL_000LV_XA_08, duration=8.666, time_delay=t)
        t += 8.666
        MotionEvent(root=self, group=MAIN, object_name=li_bartender.name,
            anim=Male.Sc_MLBODY_STND_GESTR_COME_000LV_XA_02, duration=2.266, time_delay=t)
        t += 2.266
        MotionEvent(root=self, group=MAIN, object_name=li_bartender.name,
            anim=Male.Sc_MLBODY_STND_IDLE_BRTH_000LV_xa_05, duration=5, time_delay=t)
        t += 5
        MotionEvent(root=self, group=MAIN, object_name=li_bartender.name,
            anim=Male.Sc_MLBODY_STND_LEAN_LLEG_000LV_XA_02, duration=2.166, time_delay=t)
        t += 2.166
        MotionEvent(root=self, group=MAIN, object_name=li_bartender.name,
            anim=Male.Sc_MLBODY_STND_LEAN_LLEG_SWAY_000LV_XA_03, duration=6.2, loop=True, time_delay=t)
        t += 6.2
        MotionEvent(root=self, group=MAIN, object_name=li_bartender.name,
            anim=Male.Sc_MLBODY_STND_RETURNL_NEUT_000LV_XA_02, duration=2, time_delay=t)
