"""m05_barman: постановка для ручного редактирования.

Точки: SCENES/m05_barman.blend → DUMPS/m05_barman.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — абсолютные секунды исходной сцены; часы MAIN не сдвигаются.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character,
    MAIN,
    MotionEvent,
)
from story.cutscenes.anim import (
    Male,
)
from story.cutscenes.source_extensions import (
    preserve_entity,
)
from story import actors


class ExtraCharLiBartender(actors.Actor):
    NAME = 'li_bartender'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm05_bartender'
    GAME_ACTOR = 'li_host'



class M05BarmanScene(Scene):
    DUMP_FILE = 'm05_barman'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(63.498)
        li_bartender = Character(root=self, actor=ExtraCharLiBartender, light_group=0, init_point='Char_li_bartender',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(li_bartender, template_name='m05_bartender', userprops={'actor': 'li_host', 'category': 'Character'})

        # Действия по абсолютному времени сцены.
        t = 0
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_li_bartender',
            anim=Male.Sc_MLBODY_STND_IDLE_BRTH_000LV_xa_05, duration=5)
        t += 5
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_li_bartender',
            anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, duration=3.833)
        t += 3.833
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_li_bartender',
            anim=Male.Sc_MLBODY_STND_HOLD_ARMS_CROSSED_000LV_XA_02, duration=5, loop=True)
        t += 5.0
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_li_bartender',
            anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, duration=2.033)
        t += 2.033
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_li_bartender',
            anim=Male.Sc_MLBODY_STND_LOOK_WATC_IMPA_315DN_XA_07, duration=7.099)
        t += 7.099
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_li_bartender',
            anim=Male.Sc_MLBODY_STND_IDLE_BRTH_000LV_xa_05, duration=5)
        t += 5.0
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_li_bartender',
            anim=Male.Sc_MLBODY_STND_ATEASE_HSEC_RLEASE_000LV_XA_03, duration=3)
        t += 3.0
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_li_bartender',
            anim=Male.Sc_MLBODY_STND_ATEASE_HOLD_000LV_XA_01, duration=3, loop=True)
        t += 3.0
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_li_bartender',
            anim=Male.Sc_MLBODY_STND_ATEASE_RLEASE_000LV_XA_01, duration=2.966)
        t += 2.966
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_li_bartender',
            anim=Male.Sc_MLBODY_STND_LOOK_AROU_CASL_000LV_XA_08, duration=8.666)
        t += 8.666
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_li_bartender',
            anim=Male.Sc_MLBODY_STND_GESTR_COME_000LV_XA_02, duration=2.266)
        t += 2.266
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_li_bartender',
            anim=Male.Sc_MLBODY_STND_IDLE_BRTH_000LV_xa_05, duration=5)
        t += 5.0
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_li_bartender',
            anim=Male.Sc_MLBODY_STND_LEAN_LLEG_000LV_XA_02, duration=2.166)
        t += 2.166
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_li_bartender',
            anim=Male.Sc_MLBODY_STND_LEAN_LLEG_SWAY_000LV_XA_03, duration=6.2, loop=True)
        t += 6.2
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_li_bartender',
            anim=Male.Sc_MLBODY_STND_RETURNL_NEUT_000LV_XA_02, duration=2)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M05BarmanScene
