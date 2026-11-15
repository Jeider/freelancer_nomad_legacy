"""m02_bship_bar_decision: постановка для ручного редактирования.

Точки: SCENES/m02_bship_bar_decision.blend → DUMPS/m02_bship_bar_decision.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — абсолютные секунды исходной сцены; часы MAIN не сдвигаются.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character,
    LookAtCamera,
    MAIN,
)
from story.cutscenes.anim import (
    Male,
)
from story.cutscenes.source_extensions import (
    preserve_entity,
)
from story import actors



class M02BshipBarDecisionScene(Scene):
    DUMP_FILE = 'm02_bship_bar_decision'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(2000.0)
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='Trent', userprops={'category': 'Character', 'actor': 'Player'})
        wilham = Character(root=self, actor=actors.Wilham, light_group=0, init_point='Char_wilham', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(wilham, template_name='wilham', userprops={'category': 'Character', 'actor': 'wilham'})
        cam_start = LookAtCamera(root=self, name='cam_start', fov=35, farplane=5000, look_duration=300)
        preserve_entity(cam_start)

        # Действия по абсолютному времени сцены.
        t = 0
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_SMALL_000LV_XA_07, duration=2000, loop=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_SMALL_000LV_XA_07, duration=2000, loop=True)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M02BshipBarDecisionScene
