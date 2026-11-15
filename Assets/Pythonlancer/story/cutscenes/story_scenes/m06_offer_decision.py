"""m06_offer_decision: постановка для ручного редактирования.

Точки: SCENES/m06_offer_decision.blend → DUMPS/m06_offer_decision.json.
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
    Female,
    Male,
)
from story.cutscenes.source_extensions import (
    preserve_entity,
)
from story import actors



class M06OfferDecisionScene(Scene):
    DUMP_FILE = 'm06_offer_decision'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(5000.0)
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'Actor': 'Player', 'category': 'Character'})
        alaric = Character(root=self, actor=actors.Alaric, light_group=0, init_point='Char_alaric', rotate_from_quat=True,
            use_ambient=True, floor_height=0)
        preserve_entity(alaric, template_name='alaric', userprops={'actor': 'Alaric', 'category': 'Character'})
        hatcher = Character(root=self, actor=actors.Hatcher, light_group=0, init_point='Char_hatcher',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(hatcher, template_name='hatcher', userprops={'actor': 'Hatcher', 'category': 'Character'})
        cam_scene = LookAtCamera(root=self, name='cam_scene', fov=30, farplane=5000, look_duration=1)
        preserve_entity(cam_scene)

        # Действия по абсолютному времени сцены.
        t = 0
        cam_scene.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, duration=5000, loop=True)
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=5000, loop=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=5000, loop=True)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M06OfferDecisionScene
