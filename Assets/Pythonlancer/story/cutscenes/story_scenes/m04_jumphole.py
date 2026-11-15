"""m04_jumphole: постановка для ручного редактирования.

Точки: SCENES/m04_jumphole.blend → DUMPS/m04_jumphole.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — абсолютные секунды исходной сцены; часы MAIN не сдвигаются.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    LookAtCamera,
    MAIN,
    StaticCamera,
)

from story.cutscenes.source_extensions import (
    SourceAttachEvent,
    preserve_entity,
)
from story import actors



class M04JumpholeScene(Scene):
    DUMP_FILE = 'm04_jumphole'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(8.0)
        Shot06_Camera_1 = LookAtCamera(root=self, name='Shot06_Camera_1', fov=35, farplane=100000, look_duration=30)
        preserve_entity(Shot06_Camera_1, cameraprops={'hvaspect': 1.333333, 'nearplane': 0.1})
        Camera_1 = StaticCamera(root=self, name='Camera_1', fov=45, farplane=100000)
        preserve_entity(Camera_1, cameraprops={'hvaspect': 1.333333, 'nearplane': 0.1})
        preserve_entity(self.get_entity('automarker_Shot06_Camera_1_focus'), userprops={'main_object': 'main_object'})

        # Действия по абсолютному времени сцены.
        t = 0
        Shot06_Camera_1.set(group=MAIN, time_delay=t)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['Shot06_Camera_1', 'automarker_Shot06_Camera_1_focus'], duration=30, offset=[0, 250, 250], up='Y_AXIS',
            front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='POSITION+ENTITY_RELATIVE')


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M04JumpholeScene
