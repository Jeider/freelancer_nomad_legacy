"""m06_nomad_area_camera2: постановка для ручного редактирования.

Точки: SCENES/m06_nomad_area_camera2.blend → DUMPS/m06_nomad_area_camera2.json.
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



class M06NomadAreaCamera2Scene(Scene):
    DUMP_FILE = 'm06_nomad_area_camera2'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(25.0)
        Shot06_Camera_0 = LookAtCamera(root=self, name='Shot06_Camera_0', fov=35, farplane=100000, look_duration=30)
        preserve_entity(Shot06_Camera_0, cameraprops={'hvaspect': 1.333333, 'nearplane': 0.1})

        # Действия по абсолютному времени сцены.
        t = 0
        Shot06_Camera_0.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Shot06_Camera_0',
            target_name='automarker_Shot06_Camera_0_Position2', duration=15, smooth=True)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M06NomadAreaCamera2Scene
