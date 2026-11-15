"""m08_wales_init: постановка для ручного редактирования.

Точки: SCENES/m08_wales_init.blend → DUMPS/m08_wales_init.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — абсолютные секунды исходной сцены; часы MAIN не сдвигаются.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Alchemy,
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


class PropOrOsiris3(Ship):
    COMPOUND_TEMPLATE_NAME = 'or_osiris'
    SRT_GRP = 0
    USR_FLG = 0



class M08WalesInitScene(Scene):
    DUMP_FILE = 'm08_wales_init'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(42.187)
        Cam_1 = StaticCamera(root=self, name='Cam_1', fov=35, farplane=15000.00293)
        preserve_entity(Cam_1)
        Path_Cam = MotionPath(root=self, name='Path_Cam', point_name='Path_Cam',
            path_data='{-85.689896,26.338867,101.477631}, {-0.307891,0.015419,0.950106,0.047581}, {-75.231155,31.868593,62.621788}, {-0.305912,0.019128,0.950123,0.057602}, {-65.390533,36.809349,23.529247}, {-0.304080,0.022608,0.950015,0.067054}, {-56.867748,40.504162,-15.973808}, {-0.302676,0.025474,0.949801,0.074942}, {-49.715878,42.909122,-55.843277}, {-0.301718,0.027729,0.949522,0.081279}, {-43.547993,44.389893,-95.960167}, {-0.301084,0.029545,0.949207,0.086500}, {-40.453144,43.032909,-136.380844}, {-0.301477,0.030008,0.948903,0.088280}, {-41.421852,37.994816,-176.514038}, {-0.303212,0.028698,0.948642,0.085543}, {-49.928040,26.338858,-214.082718}, {-0.307332,0.024144,0.948374,0.074506}, {-73.942848,0.366351,-253.139297}, {-0.316392,0.012752,0.947423,0.046070}, {-102.190987,-28.920418,-286.865631}, {-0.326223,-0.000393,0.945202,0.013069}, {-132.423294,-59.708736,-317.592621}, {-0.336074,-0.014343,0.941468,-0.022048}, {-164.066742,-91.523491,-345.785767}, {-0.345703,-0.028837,0.936068,-0.058614}, {-196.153152,-123.662025,-373.198639}, {-0.354844,-0.043465,0.929012,-0.095562}, {-228.828278,-156.213287,-399.405029}, {-0.363480,-0.058256,0.920222,-0.132969}, {-262.074219,-189.160294,-424.398407}, {-0.371615,-0.073278,0.909553,-0.171013}, {-295.579102,-222.283508,-448.809387}, {-0.378998,-0.088060,0.897296,-0.208487}')
        preserve_entity(Path_Cam)
        Cam_2 = StaticCamera(root=self, name='Cam_2', fov=35, farplane=15000.00293)
        preserve_entity(Cam_2)
        or_osiris_3 = PropOrOsiris3(root=self, name='or_osiris_3', light_group=0, init_point='or_osiris_3',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(or_osiris_3, userprops={'category': 'Spaceship'})
        no_cloakeffect04_1 = Alchemy(root=self, name='no_cloakeffect04_1', particles='no_cloakeffect04',
            point_name='no_cloakeffect04_1', sparam=0)
        preserve_entity(no_cloakeffect04_1, flags='LIT_DYNAMIC+LIT_AMBIENT')
        Cam_1b = StaticCamera(root=self, name='Cam_1b', fov=35, farplane=15000.00293)
        preserve_entity(Cam_1b)
        preserve_entity(self.get_entity('automarker_Mk_main_object'), userprops={'main_object': 'main_object'})

        # Действия по абсолютному времени сцены.
        t = 0
        Cam_1.set(group=MAIN, time_delay=t)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['Path_Cam', 'automarker_Mk_main_object'],
            flags='POSITION+ORIENTATION+ENTITY_RELATIVE', target_type='ROOT', target_part='', front='NEG_Z_AXIS',
            up='Y_AXIS', offset=[0, 0, 0], duration=61.75)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['or_osiris_3', 'automarker_Mk_main_object'],
            flags='POSITION+ORIENTATION', target_type='ROOT', target_part='', front='NEG_Z_AXIS', up='Y_AXIS',
            offset=[0, 0, 0], duration=1)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['no_cloakeffect04_1', 'or_osiris_3'],
            flags='POSITION+ORIENTATION', target_type='HARDPOINT', target_part='hpcloak01', front='NEG_Z_AXIS', up='Y_AXIS',
            offset=[0, 0, 0], duration=51.5)
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['Cam_1', 'Path_Cam'], pcurve_period=-1000,
            param_curve={'points': [[0, 0, 0, 0.5], [1, 1, 0, 0]], 'CLSID': 'FreeFormPCurve'}, flags='POSITION+ORIENTATION',
            front='NEG_Z_AXIS', up='Y_AXIS', offset=[0, 0, 0], stop_percent=1, start_percent=0.3, duration=36.875)
        t += 35
        no_cloakeffect04_1.start(group=MAIN, time_delay=t, duration=6)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M08WalesInitScene
