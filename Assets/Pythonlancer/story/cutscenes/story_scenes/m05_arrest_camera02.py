"""m05_arrest_camera02: постановка для ручного редактирования.

Точки: SCENES/m05_arrest_camera02.blend → DUMPS/m05_arrest_camera02.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — абсолютные секунды исходной сцены; часы MAIN не сдвигаются.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    LookAtCamera,
    MAIN,
    MotionPath,
    StaticCamera,
)

from story.cutscenes.source_extensions import (
    SourceAttachEvent,
    SourcePathEvent,
    preserve_entity,
)
from story import actors



class M05ArrestCamera02Scene(Scene):
    DUMP_FILE = 'm05_arrest_camera02'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(300.0)
        Shot06_Camera_1 = LookAtCamera(root=self, name='Shot06_Camera_1', fov=35, farplane=100000, look_duration=50)
        preserve_entity(Shot06_Camera_1, cameraprops={'hvaspect': 1.333333, 'nearplane': 0.1})
        Camera_1 = StaticCamera(root=self, name='Camera_1', fov=45, farplane=100000)
        preserve_entity(Camera_1, cameraprops={'hvaspect': 1.333333, 'nearplane': 0.1})
        Path_1 = MotionPath(root=self, name='Path_1', point_name='Path_1',
            path_data='{-25,5,-5}, {1,0,0,0}, {-25,50,200}, {1,0,0,0}')
        preserve_entity(Path_1)
        Path_mrk = MotionPath(root=self, name='Path_mrk', point_name='Path_mrk',
            path_data='{0, 0, 0}, {1,0,0,0}, {0,0,-50}, {1,0,0,0}')
        preserve_entity(Path_mrk)
        Path_mrk_static = MotionPath(root=self, name='Path_mrk_static', point_name='Path_mrk_static',
            path_data='{0, 0.1, 0}, {1,0,0,0}, {0,0,0}, {1,0,0,0}')
        preserve_entity(Path_mrk_static)
        preserve_entity(self.get_entity('automarker_main_object'), userprops={'main_object': 'main_object'})

        # Действия по абсолютному времени сцены.
        t = 0
        Shot06_Camera_1.set(group=MAIN, time_delay=t)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['Path_1', 'automarker_main_object'], duration=50,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT',
            flags='POSITION+ORIENTATION+ENTITY_RELATIVE')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['Path_mrk', 'automarker_main_object'], duration=50,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT',
            flags='POSITION+ORIENTATION+ENTITY_RELATIVE')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['Path_mrk_static', 'automarker_main_object'],
            duration=50, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT',
            flags='POSITION+ORIENTATION+ENTITY_RELATIVE')
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['Shot06_Camera_1', 'Path_1'], duration=20,
            start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', flags='POSITION',
            param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]}, pcurve_period=-1000)
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['automarker_Shot06_Camera_1_focus', 'Path_mrk'],
            duration=30, start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS',
            flags='POSITION', param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]},
            pcurve_period=-1000)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M05ArrestCamera02Scene
