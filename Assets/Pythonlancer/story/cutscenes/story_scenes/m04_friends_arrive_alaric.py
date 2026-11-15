"""m04_friends_arrive_alaric: постановка для ручного редактирования.

Точки: SCENES/m04_friends_arrive_alaric.blend → DUMPS/m04_friends_arrive_alaric.json.
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
    preserve_spatial,
)
from story import actors



class M04FriendsArriveAlaricScene(Scene):
    DUMP_FILE = 'm04_friends_arrive_alaric'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(300.0)
        Shot06_Camera_1 = LookAtCamera(root=self, name='Shot06_Camera_1', fov=35, farplane=100000, look_duration=300)
        preserve_entity(Shot06_Camera_1, cameraprops={'hvaspect': 1.333333, 'nearplane': 0.1})
        Camera_1 = StaticCamera(root=self, name='Camera_1', fov=45, farplane=100000)
        preserve_entity(Camera_1, cameraprops={'hvaspect': 1.333333, 'nearplane': 0.1})
        Path_1 = MotionPath(root=self, name='Path_1', point_name='Path_1',
            path_data='{0.000000,0.000000,0.000000}, {1.000000,0.000000,0.000000,0.000000}, {0.000000,0.100000,0.000000}, {1.000000,0.000000,0.000000,0.000000}')
        preserve_entity(Path_1)
        preserve_entity(self.get_entity('automarker_main_object'), userprops={'main_object': 'main_object'})

        # Действия по абсолютному времени сцены.
        t = 0
        Shot06_Camera_1.set(group=MAIN, time_delay=t)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['Path_1', 'automarker_main_object'], duration=300,
            offset=[-10, 3, -20], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT',
            flags='POSITION+ORIENTATION+ENTITY_RELATIVE')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['automarker_Shot06_Camera_1_focus', 'automarker_main_object'], duration=300, offset=[0, 0, 0],
            up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT',
            flags='POSITION+ORIENTATION+ENTITY_RELATIVE')
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['Shot06_Camera_1', 'Path_1'], duration=300,
            start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', flags='POSITION',
            param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]}, pcurve_period=-1000)
        preserve_spatial(self.get_entity('Camera_1'),
            source_basis=[[0.2, 0, 0.148444], [0.019341, 0.991476, -0.128849], [-0.147179, 0.130293, 0.980491]],
            reference_orientation=[0.9789364337921143, 0.06720173358917236, 0.19173350930213928, 0.020137280225753784])


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M04FriendsArriveAlaricScene
