"""m03_kgb_death02: постановка для ручного редактирования.

Точки: SCENES/m03_kgb_death02.blend → DUMPS/m03_kgb_death02.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — абсолютные секунды исходной сцены; часы MAIN не сдвигаются.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    LookAtCamera,
    MAIN,
    MoveEvent,
)

from story.cutscenes.source_extensions import (
    preserve_entity,
)
from story import actors



class M03KgbDeath02Scene(Scene):
    DUMP_FILE = 'm03_kgb_death02'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(20.0)
        cam = LookAtCamera(root=self, name='cam', fov=25, farplane=5000, look_duration=300)
        preserve_entity(cam)

        # Действия по абсолютному времени сцены.
        t = 0
        cam.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam', target_name='automarker_cam_pos2', duration=20,
            smooth=True, adjust_orient=False)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M03KgbDeath02Scene
