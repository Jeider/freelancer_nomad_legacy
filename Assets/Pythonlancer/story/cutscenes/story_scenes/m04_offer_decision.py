"""m04_offer_decision: постановка для ручного редактирования.

Точки: SCENES/m04_offer_decision.blend → DUMPS/m04_offer_decision.json.
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



class M04OfferDecisionScene(Scene):
    DUMP_FILE = 'm04_offer_decision'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(5555.0)
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'actor': 'Player', 'category': 'Character'})
        jacobo = Character(root=self, actor=actors.Jacobo, light_group=0, init_point='Char_jacobo', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(jacobo, template_name='jacobo', userprops={'category': 'Character', 'actor': 'jacobo'})
        cam_table = LookAtCamera(root=self, name='cam_table', fov=20, farplane=5000, look_duration=300)
        preserve_entity(cam_table)

        # Действия по абсолютному времени сцены.
        t = 0
        cam_table.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, duration=5555, loop=True)
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=5555, loop=True)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M04OfferDecisionScene
