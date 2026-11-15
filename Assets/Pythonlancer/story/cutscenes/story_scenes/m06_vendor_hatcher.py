"""m06_vendor_hatcher: постановка для ручного редактирования.

Точки: SCENES/m06_vendor_hatcher.blend → DUMPS/m06_vendor_hatcher.json.
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
    Female,
)
from story.cutscenes.source_extensions import (
    preserve_entity,
)
from story import actors



class M06VendorHatcherScene(Scene):
    DUMP_FILE = 'm06_vendor_hatcher'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(29.812)
        hatcher = Character(root=self, actor=actors.Hatcher, light_group=0, init_point='Char_hatcher',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(hatcher, template_name='hatcher', userprops={'category': 'Character'})

        # Действия по абсолютному времени сцены.
        t = 0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_IDLE_SMALL_000LV_XA_05, duration=5, trans_time=1)
        t += 5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_TWSTS_LOOK_090LV_XA_02, duration=2)
        t += 2
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_LOOK_090LV_XA_01, duration=1)
        t += 1
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_TWSTS_FROM_090LV_XA_02, duration=2.333)
        t += 2.333
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_IDLE_MED_000LV_XA_05, duration=5)
        t += 5.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_IDLE_BIG_000LV_XA_05, duration=5)
        t += 5.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_TWSTS_LOOK_270LV_XA_02, duration=2.166)
        t += 2.167
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_TWSTS_FROM_270LV_XA_02, duration=2.333)
        t += 2.333
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_IDLE_SMALL_000LV_XA_05, duration=5)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M06VendorHatcherScene
