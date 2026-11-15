"""m05_rheinlanders_camera: постановка для ручного редактирования.

Точки: SCENES/m05_rheinlanders_camera.blend → DUMPS/m05_rheinlanders_camera.json.
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



class M05RheinlandersCameraScene(Scene):
    DUMP_FILE = 'm05_rheinlanders_camera'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(300.0)
        Shot06_Camera_1 = LookAtCamera(root=self, name='Shot06_Camera_1', fov=35, farplane=100000, look_duration=5)
        preserve_entity(Shot06_Camera_1, cameraprops={'hvaspect': 1.333333, 'nearplane': 0.1})
        preserve_entity(self.get_entity('automarker_Shot06_Camera_1_focus'), userprops={'main_object': 'main_object'})

        # Действия по абсолютному времени сцены.
        t = 0
        Shot06_Camera_1.set(group=MAIN, time_delay=t)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M05RheinlandersCameraScene
