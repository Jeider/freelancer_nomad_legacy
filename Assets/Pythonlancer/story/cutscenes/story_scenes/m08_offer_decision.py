"""m08_offer_decision: постановка для ручного редактирования.

Точки: SCENES/m08_offer_decision.blend → DUMPS/m08_offer_decision.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — абсолютные секунды исходной сцены; часы MAIN не сдвигаются.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character,
    LookAtCamera,
    MAIN,
    MotionEvent,
    RotateAxisEvent,
)
from story.cutscenes.anim import (
    Female,
    Male,
)
from story.cutscenes.source_extensions import (
    preserve_entity,
)
from story import actors


class ExtraCharKaytlin(actors.Actor):
    NAME = 'kaytlin'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'kaytlin'
    GAME_ACTOR = 'Kaytlin'



class M08OfferDecisionScene(Scene):
    DUMP_FILE = 'm08_offer_decision'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(267111111.0)
        kaytlin = Character(root=self, actor=ExtraCharKaytlin, light_group=0, init_point='Char_kaytlin',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(kaytlin, template_name='kaytlin', userprops={'actor': 'Kaytlin', 'category': 'Character'})
        brighton = Character(root=self, actor=actors.Brighton, light_group=0, init_point='Char_brighton',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(brighton, template_name='brighton', userprops={'actor': 'Brighton', 'category': 'Character'})
        darcy = Character(root=self, actor=actors.Darcy, light_group=0, init_point='Char_darcy', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(darcy, template_name='darcy', userprops={'Actor': 'Darcy', 'category': 'Character'})
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'Actor': 'Player', 'category': 'Character'})
        cam_trent_far = LookAtCamera(root=self, name='cam_trent_far', fov=18, farplane=5000, look_duration=710)
        preserve_entity(cam_trent_far)

        # Действия по абсолютному времени сцены.
        t = 0
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRF_IDLE_000LV_XA_05, duration=10)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_kaytlin',
            anim=Female.Sc_FMBODY_CHRF_IDLE_000LV_XA_05, duration=10)
        brighton.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=100, time_scale=0.6,
            loop=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=100, time_scale=0.6,
            loop=True)
        cam_trent_far.set(group=MAIN, time_delay=t)
        t += 0.01
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_darcy', angle=-25, axis='Y_AXIS', duration=0,
            smooth=False)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_kaytlin', angle=-125, axis='Y_AXIS',
            duration=0, smooth=False)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_brighton', angle=10, axis='Y_AXIS',
            duration=0, smooth=False)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=20, axis='Y_AXIS', duration=0,
            smooth=False)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M08OfferDecisionScene
