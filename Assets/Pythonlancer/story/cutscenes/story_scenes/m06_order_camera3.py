"""m06_order_camera3: постановка для ручного редактирования.

Точки: SCENES/m06_order_camera3.blend → DUMPS/m06_order_camera3.json.
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



class M06OrderCamera3Scene(Scene):
    DUMP_FILE = 'm06_order_camera3'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(20.0)
        Path_1 = MotionPath(root=self, name='Path_1', point_name='Path_1',
            path_data='{41776, 5027, -27157}, {0.4,0,-0.6,0}, {41708, 4999, -27593}, {0,0,-1,0}')
        preserve_entity(Path_1)
        Shot06_Camera_0 = LookAtCamera(root=self, name='Shot06_Camera_0', fov=35, farplane=100000, look_duration=1)
        preserve_entity(Shot06_Camera_0, cameraprops={'hvaspect': 1.333333, 'nearplane': 0.1})

        # Действия по абсолютному времени сцены.
        t = 0
        Shot06_Camera_0.set(group=MAIN, time_delay=t)
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['Shot06_Camera_0', 'Path_1'], duration=15,
            start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', flags='POSITION',
            param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]}, pcurve_period=-1000)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M06OrderCamera3Scene
