"""m01b_armored_trap_camera: постановка для ручного редактирования.

Точки: SCENES/m01b_armored_trap_camera.blend → DUMPS/m01b_armored_trap_camera.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — абсолютные секунды исходной сцены; часы MAIN не сдвигаются.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    LookAtCamera,
    MAIN,
    MotionPath,
    Ship,
    StaticCamera,
)

from story.cutscenes.source_extensions import (
    SourceAttachEvent,
    SourcePathEvent,
    preserve_entity,
)
from story import actors


class PropRhCruiser1(Ship):
    COMPOUND_TEMPLATE_NAME = 'rh_cruiser'
    SRT_GRP = 0
    USR_FLG = 0



class M01bArmoredTrapCameraScene(Scene):
    DUMP_FILE = 'm01b_armored_trap_camera'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(54.375)
        CnB_Camera_00 = StaticCamera(root=self, name='CnB_Camera_00', fov=35, farplane=100000.0)
        preserve_entity(CnB_Camera_00, cameraprops={'nearplane': 0.1, 'hvaspect': 1.333333})
        CnB_Camera_01 = StaticCamera(root=self, name='CnB_Camera_01', fov=35, farplane=100000.0)
        preserve_entity(CnB_Camera_01, cameraprops={'nearplane': 0.1, 'hvaspect': 1.333333})
        aa_depot_Path = MotionPath(root=self, name='aa_depot_Path', point_name='aa_depot_Path',
            path_data='{85.947334,45.790657,136.607208}, {0.269080,0.925089,-0.113638,-0.242676}, {-50.846935,23.158363,185.705719}, {0.269080,0.925089,-0.113638,-0.242676}, {-162.610107,-15.626595,-2.601044}, {0.269080,0.925089,-0.113638,-0.242676}, {-110.065521,-45.919487,-117.121704}, {0.269080,0.925089,-0.113638,-0.242676}')
        preserve_entity(aa_depot_Path)
        Path_Camera_1 = LookAtCamera(root=self, name='Path_Camera_1', fov=45, farplane=100000.0, look_duration=50)
        preserve_entity(Path_Camera_1, cameraprops={'nearplane': 0.1, 'hvaspect': 1.333333})
        rh_cruiser_1 = PropRhCruiser1(root=self, name='rh_cruiser_1', light_group=0, init_point='rh_cruiser_1',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(rh_cruiser_1, userprops={'category': 'Spaceship'})
        preserve_entity(self.get_entity('automarker_Path_Camera_1_focus'), userprops={'main_object': 'main_object'})

        # Действия по абсолютному времени сцены.
        t = 0
        Path_Camera_1.set(group=MAIN, time_delay=t)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['CnB_Camera_01', 'automarker_Marker_2'],
            flags='POSITION', target_type='ROOT', target_part='', front='NEG_Z_AXIS', up='Y_AXIS', offset=[0, 0, 0],
            duration=56.200001)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['automarker_Marker_2', 'automarker_Marker_1'],
            flags='POSITION+ORIENTATION+ENTITY_RELATIVE', target_type='ROOT', target_part='', front='NEG_Z_AXIS',
            up='Y_AXIS', offset=[0, 0, 300], duration=54.400002)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['aa_depot_Path', 'automarker_Path_Camera_1_focus'],
            flags='POSITION+ORIENTATION+ENTITY_RELATIVE', target_type='ROOT', target_part='', front='NEG_Z_AXIS',
            up='Y_AXIS', offset=[0, 0, 0], duration=67.800003)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['rh_cruiser_1', 'automarker_Path_Camera_1_focus'],
            flags='POSITION+ORIENTATION+ENTITY_RELATIVE', target_type='ROOT', target_part='', front='NEG_Z_AXIS',
            up='Y_AXIS', offset=[0, 0, 0], duration=0)
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['Path_Camera_1', 'aa_depot_Path'],
            pcurve_period=-1000, param_curve={'points': [[0, 0, 0, 0], [1, 1, 0, 0]], 'CLSID': 'FreeFormPCurve'},
            flags='POSITION', front='NEG_Z_AXIS', up='Y_AXIS', offset=[0, 0, 0], stop_percent=1, start_percent=0,
            duration=40)
        t += 0.75
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['CnB_Camera_00', 'automarker_Path_Camera_1_focus'],
            flags='LOOK_AT', target_type='ROOT', target_part='', front='NEG_Z_AXIS', up='Y_AXIS', offset=[0, 0, 0],
            duration=0)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M01bArmoredTrapCameraScene
