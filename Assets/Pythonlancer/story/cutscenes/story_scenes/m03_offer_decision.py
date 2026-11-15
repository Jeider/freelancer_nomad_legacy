"""m03_offer_decision: постановка для ручного редактирования.

Точки: SCENES/m03_offer_decision.blend → DUMPS/m03_offer_decision.json.
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



class M03OfferDecisionScene(Scene):
    DUMP_FILE = 'm03_offer_decision'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(1000.0)
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'actor': 'Player', 'category': 'Character'})
        hassler = Character(root=self, actor=actors.Hassler, light_group=0, init_point='Char_hassler',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(hassler, template_name='hassler', userprops={'category': 'Character', 'actor': 'hassler'})
        wilham = Character(root=self, actor=actors.Wilham, light_group=0, init_point='Char_wilham', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(wilham, template_name='wilham', userprops={'category': 'Character', 'actor': 'wilham'})
        cam_decision = LookAtCamera(root=self, name='cam_decision', fov=35, farplane=5000, look_duration=300)
        preserve_entity(cam_decision)

        # Действия по абсолютному времени сцены.
        t = 0
        cam_decision.set(group=MAIN, time_delay=t)
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_BRTH_000LV_xa_05, duration=1000,
            time_scale=0.5, loop=True)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_MED_000LV_xa_05, duration=1000,
            time_scale=0.5, loop=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_BIG_000LV_xa_05, duration=1000, time_scale=0.5,
            loop=True)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M03OfferDecisionScene
