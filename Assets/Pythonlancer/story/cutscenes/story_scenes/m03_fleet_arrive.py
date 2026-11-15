"""m03_fleet_arrive: постановка для ручного редактирования.

Точки: SCENES/m03_fleet_arrive.blend → DUMPS/m03_fleet_arrive.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — абсолютные секунды исходной сцены; часы MAIN не сдвигаются.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    LookAtCamera,
    MAIN,
    MoveEvent,
)

from story.cutscenes.source_extensions import (
    preserve_entity,
)
from story import actors



class M03FleetArriveScene(Scene):
    DUMP_FILE = 'm03_fleet_arrive'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(6.0)
        cam = LookAtCamera(root=self, name='cam', fov=25, farplane=5000, look_duration=300)
        preserve_entity(cam)

        # Действия по абсолютному времени сцены.
        t = 0
        cam.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam', target_name='automarker_cam_pos2', duration=6,
            smooth=True, adjust_orient=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_focus',
            target_name='automarker_cam_marker_pos2', duration=6, smooth=False, adjust_orient=False)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M03FleetArriveScene
