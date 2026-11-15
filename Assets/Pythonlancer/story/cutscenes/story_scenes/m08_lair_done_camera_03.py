"""m08_lair_done_camera_03: постановка для ручного редактирования.

Точки: SCENES/m08_lair_done_camera_03.blend → DUMPS/m08_lair_done_camera_03.json.
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
    SourceAttachEvent,
    preserve_entity,
)
from story import actors



class M08LairDoneCamera03Scene(Scene):
    DUMP_FILE = 'm08_lair_done_camera_03'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(30.0)
        cam = LookAtCamera(root=self, name='cam', fov=25, farplane=5000, look_duration=300)
        preserve_entity(cam)
        preserve_entity(self.get_entity('automarker_cam_focus'), userprops={'main_object': 'main_object'})

        # Действия по абсолютному времени сцены.
        t = 0
        cam.set(group=MAIN, time_delay=t)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['cam', 'automarker_cam_focus'], duration=300,
            offset=[-18, 5, 5], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='POSITION')


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M08LairDoneCamera03Scene
