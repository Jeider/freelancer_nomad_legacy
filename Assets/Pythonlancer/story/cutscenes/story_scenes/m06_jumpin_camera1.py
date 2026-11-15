"""m06_jumpin_camera1: постановка для ручного редактирования.

Точки: SCENES/m06_jumpin_camera1.blend → DUMPS/m06_jumpin_camera1.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — абсолютные секунды исходной сцены; часы MAIN не сдвигаются.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    LookAtCamera,
    MAIN,
)

from story.cutscenes.source_extensions import (
    preserve_entity,
)
from story import actors



class M06JumpinCamera1Scene(Scene):
    DUMP_FILE = 'm06_jumpin_camera1'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(10.0)
        Shot06_Camera_0 = LookAtCamera(root=self, name='Shot06_Camera_0', fov=35, farplane=100000, look_duration=1)
        preserve_entity(Shot06_Camera_0, cameraprops={'hvaspect': 1.333333, 'nearplane': 0.1})

        # Действия по абсолютному времени сцены.
        t = 0
        Shot06_Camera_0.set(group=MAIN, time_delay=t)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M06JumpinCamera1Scene
