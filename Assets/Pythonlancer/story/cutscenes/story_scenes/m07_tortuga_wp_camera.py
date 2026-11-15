"""m07_tortuga_wp_camera: постановка для ручного редактирования.

Точки: SCENES/m07_tortuga_wp_camera.blend → DUMPS/m07_tortuga_wp_camera.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — абсолютные секунды исходной сцены; часы MAIN не сдвигаются.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    LookAtCamera,
    MAIN,
    MotionPath,
)

from story.cutscenes.source_extensions import (
    SourcePathEvent,
    preserve_entity,
)
from story import actors



class M07TortugaWpCameraScene(Scene):
    DUMP_FILE = 'm07_tortuga_wp_camera'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(10000.0)
        Shot06_Camera_0 = LookAtCamera(root=self, name='Shot06_Camera_0', fov=35, farplane=100000, look_duration=30)
        preserve_entity(Shot06_Camera_0, cameraprops={'hvaspect': 1.333333, 'nearplane': 0.1})
        Path_Camera = MotionPath(root=self, name='Path_Camera', point_name='Path_Camera',
            path_data='{19920, -1980, 5000}, {1,0,0,0}, {19990, -2000, 5000}, {1,0,0,0}')
        preserve_entity(Path_Camera)
        Path_Marker = MotionPath(root=self, name='Path_Marker', point_name='Path_Marker',
            path_data='{19020, -1980, 5000}, {1,0,0,0}, {19090, -2000, 5000}, {1,0,0,0}')
        preserve_entity(Path_Marker)

        # Действия по абсолютному времени сцены.
        t = 0
        Shot06_Camera_0.set(group=MAIN, time_delay=t)
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['Shot06_Camera_0', 'Path_Camera'], duration=10,
            start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', flags='POSITION',
            param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]}, pcurve_period=-1000)
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['automarker_Shot06_Camera_0_focus', 'Path_Marker'],
            duration=10, start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS',
            flags='POSITION', param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]},
            pcurve_period=-1000)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M07TortugaWpCameraScene
