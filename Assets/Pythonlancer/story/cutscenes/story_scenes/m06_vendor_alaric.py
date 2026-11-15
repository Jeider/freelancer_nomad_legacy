"""m06_vendor_alaric: постановка для ручного редактирования.

Точки: SCENES/m06_vendor_alaric.blend → DUMPS/m06_vendor_alaric.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — абсолютные секунды исходной сцены; часы MAIN не сдвигаются.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character,
    MAIN,
)
from story.cutscenes.anim import (
    Male,
)
from story.cutscenes.source_extensions import (
    preserve_entity,
)
from story import actors



class M06VendorAlaricScene(Scene):
    DUMP_FILE = 'm06_vendor_alaric'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(61.464)
        alaric = Character(root=self, actor=actors.Alaric, light_group=0, init_point='Char_alaric', rotate_from_quat=True,
            use_ambient=True, floor_height=0)
        preserve_entity(alaric, template_name='Alaric', userprops={'category': 'Character'})

        # Действия по абсолютному времени сцены.
        t = 0
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_SMALL_000LV_XA_07, duration=7.9)
        t += 7.9
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_LOOK_AROU_000LV_XA_04, duration=4, loop=True)
        t += 4.0
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_SMALL_000LV_XA_07, duration=7.9)
        t += 7.9
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_LOOK_AROU_CASL_000LV_XA_04, duration=6.666,
            loop=True)
        t += 6.666
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_MED_000LV_XA_07, duration=7.233)
        t += 7.233
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_TWSTS_LOOK_090LV_XA_02, duration=2.6)
        t += 2.6
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_TWSTS_FROM_090LV_XA_04, duration=4.033)
        t += 4.033
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_MED_000LV_XA_07, duration=7.233)
        t += 7.233
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_LOOK_AROU_CASL_000LV_XA_04, duration=6.666)
        t += 6.666
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_MED_000LV_XA_07, duration=7.233)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M06VendorAlaricScene
