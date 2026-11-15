"""m05_arrest_camera06: постановка для ручного редактирования.

Точки: SCENES/m05_arrest_camera06.blend → DUMPS/m05_arrest_camera06.json.
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



class M05ArrestCamera06Scene(Scene):
    DUMP_FILE = 'm05_arrest_camera06'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(300.0)
        cam = LookAtCamera(root=self, name='cam', fov=25, farplane=5000, look_duration=300)
        preserve_entity(cam)
        preserve_entity(self.get_entity('automarker_cam_focus'), userprops={'main_object': 'main_object'})

        # Действия по абсолютному времени сцены.
        t = 0
        cam.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam', target_name='automarker_cam_pos2', duration=25,
            smooth=False, adjust_orient=False)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M05ArrestCamera06Scene
