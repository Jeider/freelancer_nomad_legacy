"""m08_lair_done_camera_04: постановка для ручного редактирования.

Точки: SCENES/m08_lair_done_camera_04.blend → DUMPS/m08_lair_done_camera_04.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — абсолютные секунды исходной сцены; часы MAIN не сдвигаются.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    MAIN,
    MoveEvent,
    StaticCamera,
)

from story.cutscenes.source_extensions import (
    SourceAttachEvent,
    preserve_entity,
)
from story import actors



class M08LairDoneCamera04Scene(Scene):
    DUMP_FILE = 'm08_lair_done_camera_04'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(30.0)
        cam = StaticCamera(root=self, name='cam', fov=25, farplane=5000)
        preserve_entity(cam)
        preserve_entity(self.get_entity('automarker_main_object'), userprops={'main_object': 'main_object'})

        # Действия по абсолютному времени сцены.
        t = 0
        cam.set(group=MAIN, time_delay=t)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['cam', 'automarker_main_object'], duration=300,
            offset=[0, 0, 10], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['automarker_cam_root01', 'automarker_main_object'],
            duration=300, offset=[50, 5, 10], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT',
            flags='POSITION')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['automarker_cam_root02', 'automarker_main_object'],
            duration=300, offset=[75, 5, 10], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT',
            flags='POSITION')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam', target_name='automarker_cam_root01', duration=0,
            smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam', target_name='automarker_cam_root02', duration=10,
            smooth=True)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M08LairDoneCamera04Scene
