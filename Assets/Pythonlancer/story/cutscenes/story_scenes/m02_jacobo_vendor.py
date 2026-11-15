"""m02_jacobo_vendor: постановка для ручного редактирования.

Точки: SCENES/m02_jacobo_vendor.blend → DUMPS/m02_jacobo_vendor.json.
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



class M02JacoboVendorScene(Scene):
    DUMP_FILE = 'm02_jacobo_vendor'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(15.133)
        the_char = Character(root=self, actor=actors.Jacobo, light_group=0, init_point='Char_jacobo', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(the_char, template_name='jacobo', userprops={'category': 'Character'})

        # Действия по абсолютному времени сцены.
        t = 0
        the_char.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_MED_000LV_XA_07, duration=7.232, loop=True,
            trans_time=1)
        t += 7.233
        the_char.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_SMALL_000LV_XA_07, duration=7.9)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M02JacoboVendorScene
