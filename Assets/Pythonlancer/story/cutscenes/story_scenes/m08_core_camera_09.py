"""m08_core_camera_09: постановка для ручного редактирования.

Точки: SCENES/m08_core_camera_09.blend → DUMPS/m08_core_camera_09.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — абсолютные секунды исходной сцены; часы MAIN не сдвигаются.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    LookAtCamera,
    MAIN,
    MoveEvent,
    RotateAxisEvent,
)

from story.cutscenes.source_extensions import (
    SourceAttachEvent,
    preserve_entity,
)
from story import actors



class M08CoreCamera09Scene(Scene):
    DUMP_FILE = 'm08_core_camera_09'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(60.0)
        Camera_1 = LookAtCamera(root=self, name='Camera_1', fov=45, farplane=100000, look_duration=60)
        preserve_entity(Camera_1, cameraprops={'hvaspect': 1.333333, 'nearplane': 0.1})
        preserve_entity(self.get_entity('automarker_Camera_1_focus'), userprops={'main_object': 'main_object'})

        # Действия по абсолютному времени сцены.
        t = 0
        Camera_1.set(group=MAIN, time_delay=t)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['automarker_CoreMarker', 'automarker_Camera_1_focus'], duration=18, offset=[0, 0, 0], up='Y_AXIS',
            front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='POSITION')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['automarker_CameraMarker', 'automarker_CoreMarker'],
            duration=18, offset=[-370, 60, 70], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT',
            flags='POSITION+ORIENTATION+ENTITY_RELATIVE')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['Camera_1', 'automarker_CameraMarker'], duration=18,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT',
            flags='POSITION+ORIENTATION')
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_CoreMarker', angle=70, axis='Y_AXIS',
            duration=18, smooth=True)
        t += 22
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Camera_1', target_name='automarker_cam_final_pos',
            duration=5, smooth=True)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M08CoreCamera09Scene
