"""m07_offer_decision: постановка для ручного редактирования.

Точки: SCENES/m07_offer_decision.blend → DUMPS/m07_offer_decision.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — абсолютные секунды исходной сцены; часы MAIN не сдвигаются.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character,
    LookAtCamera,
    MAIN,
    MoveEvent,
)
from story.cutscenes.anim import (
    Male,
)
from story.cutscenes.source_extensions import (
    preserve_entity,
)
from story import actors


class ExtraCharBartenderFixture(actors.Actor):
    NAME = 'bartender_fixture'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'li_bartender_1'
    GAME_ACTOR = 'bartender'


class ExtraCharTrentBase(actors.Actor):
    NAME = 'trent_base'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'trent'
    GAME_ACTOR = 'Player'



class M07OfferDecisionScene(Scene):
    DUMP_FILE = 'm07_offer_decision'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(140.0)
        # Исправлена опечатка исходного THN: floor_height==-110 → числовое -110.
        bartender_fixture = Character(root=self, actor=ExtraCharBartenderFixture, light_group=0,
            init_point='Char_bartender_fixture', rotate_from_quat=True, use_ambient=False, floor_height=-110)
        preserve_entity(bartender_fixture, template_name='li_bartender_1',
            userprops={'actor': 'bartender', 'category': 'Character'})
        trent_base = Character(root=self, actor=ExtraCharTrentBase, light_group=0, init_point='Char_trent_base',
            rotate_from_quat=True, use_ambient=False, floor_height=-1000)
        preserve_entity(trent_base, template_name='trent', userprops={'Actor': 'Player', 'category': 'Character'})
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='trent_original', userprops={'actor': 'TrentOriginal', 'category': 'Character'})
        # Исправлена опечатка исходного THN: floor_height==-110 → числовое -110.
        barman = Character(root=self, actor=actors.DetroitBarman, light_group=0, init_point='Char_barman',
            rotate_from_quat=True, use_ambient=False, floor_height=-110)
        preserve_entity(barman, template_name='m07_bartender', userprops={'actor': 'm6_bartender', 'category': 'Character'})
        cam_trent_deal = LookAtCamera(root=self, name='cam_trent_deal', fov=20, farplane=5000, look_duration=70)
        preserve_entity(cam_trent_deal)

        # Действия по абсолютному времени сцены.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_bartender_fixture', target_name='offscreen',
            duration=0, smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent_base', target_name='offscreen', duration=0,
            smooth=False)
        barman.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=10000, loop=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=10000, loop=True)
        cam_trent_deal.set(group=MAIN, time_delay=t)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M07OfferDecisionScene
