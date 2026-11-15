"""m02_junkers: постановка для ручного редактирования.

Точки: SCENES/m02_junkers.blend → DUMPS/m02_junkers.json.
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



class M02JunkersScene(Scene):
    DUMP_FILE = 'm02_junkers'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(33.5)
        Camera_1 = LookAtCamera(root=self, name='Camera_1', fov=45, farplane=100000, look_duration=30)
        preserve_entity(Camera_1, cameraprops={'hvaspect': 1.333333, 'nearplane': 0.1})
        Camera_2 = LookAtCamera(root=self, name='Camera_2', fov=45, farplane=100000, look_duration=30)
        preserve_entity(Camera_2, cameraprops={'hvaspect': 1.333333, 'nearplane': 0.1})

        # Действия по абсолютному времени сцены.
        t = 0
        Camera_1.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Camera_1', target_name='automarker_mark_cam_pos2',
            duration=15, smooth=True, adjust_orient=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_Camera_1_focus',
            target_name='automarker_mark_obj_pos2', duration=15, smooth=True, adjust_orient=False)
        t += 16
        Camera_2.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Camera_2', target_name='automarker_mark_cam2_pos2',
            duration=11, smooth=True, adjust_orient=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_Camera_2_focus',
            target_name='automarker_mark_obj2_pos2', duration=11, smooth=True, adjust_orient=False)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M02JunkersScene
