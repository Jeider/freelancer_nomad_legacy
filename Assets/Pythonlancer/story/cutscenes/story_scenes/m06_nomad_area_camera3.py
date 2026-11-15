"""m06_nomad_area_camera3: постановка для ручного редактирования.

Точки: SCENES/m06_nomad_area_camera3.blend → DUMPS/m06_nomad_area_camera3.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — абсолютные секунды исходной сцены; часы MAIN не сдвигаются.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    MAIN,
    MotionPath,
    StaticCamera,
)

from story.cutscenes.source_extensions import (
    SourcePathEvent,
    preserve_entity,
)
from story import actors



class M06NomadAreaCamera3Scene(Scene):
    DUMP_FILE = 'm06_nomad_area_camera3'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(25.0)
        Path_1 = MotionPath(root=self, name='Path_1', point_name='Path_1',
            path_data='{-11400, 300, -25850}, {0.4,0,-0.6,0}, {-10800, -825, -23000}, {0,0,-1,0}')
        preserve_entity(Path_1)
        Shot06_Camera_0 = StaticCamera(root=self, name='Shot06_Camera_0', fov=35, farplane=100000)
        preserve_entity(Shot06_Camera_0, cameraprops={'hvaspect': 1.333333, 'nearplane': 0.1})

        # Действия по абсолютному времени сцены.
        t = 0
        Shot06_Camera_0.set(group=MAIN, time_delay=t)
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['Shot06_Camera_0', 'Path_1'], duration=12,
            start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS',
            flags='POSITION+ORIENTATION', param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]},
            pcurve_period=-1000)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M06NomadAreaCamera3Scene
