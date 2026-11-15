"""m07_offer_accept: постановка для ручного редактирования.

Точки: SCENES/m07_offer_accept.blend → DUMPS/m07_offer_accept.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — смещение внутри текущего блока; facial()/append_time() двигают часы.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character,
    LookAtCamera,
    MAIN,
    MoveEvent,
    NeckIkEvent,
    Prop,
    Sound,
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


class PropPropCigarette2(Prop):
    COMPOUND_TEMPLATE_NAME = 'cigarette_2'
    SRT_GRP = 0
    USR_FLG = 0


class ExtraCharTrentBase(actors.Actor):
    NAME = 'trent_base'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'trent'
    GAME_ACTOR = 'Player'



class M07OfferAcceptScene(Scene):
    DUMP_FILE = 'm07_offer_accept'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        # Исправлена опечатка исходного THN: floor_height==-110 → числовое -110.
        bartender_fixture = Character(root=self, actor=ExtraCharBartenderFixture, light_group=0,
            init_point='Char_bartender_fixture', rotate_from_quat=True, use_ambient=False, floor_height=-110)
        preserve_entity(bartender_fixture, template_name='li_bartender_1',
            userprops={'actor': 'bartender', 'category': 'Character'})
        prop_cigarette_2 = PropPropCigarette2(root=self, name='prop_cigarette_2', light_group=0,
            init_point='prop_cigarette_2', rotate_from_quat=True, use_ambient=True)
        preserve_entity(prop_cigarette_2, userprops={'category': 'Prop'})
        DX_m06_freeport_0010_delta1 = Sound(root=self, name='DX_m06_freeport_0010_delta1',
            sound='DX_m06_freeport_0010_delta1', attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m06_freeport_0010_delta1, userprops={'category': 'Audio'})
        DX_m06_freeport_0020_trent = Sound(root=self, name='DX_m06_freeport_0020_trent', sound='DX_m06_freeport_0020_trent',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m06_freeport_0020_trent, userprops={'category': 'Audio'})
        DX_m06_freeport_0030_delta1 = Sound(root=self, name='DX_m06_freeport_0030_delta1',
            sound='DX_m06_freeport_0030_delta1', attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m06_freeport_0030_delta1, userprops={'category': 'Audio'})
        DX_m06_freeport_0040_delta1 = Sound(root=self, name='DX_m06_freeport_0040_delta1',
            sound='DX_m06_freeport_0040_delta1', attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m06_freeport_0040_delta1, userprops={'category': 'Audio'})
        DX_m06_freeport_0050_delta1 = Sound(root=self, name='DX_m06_freeport_0050_delta1',
            sound='DX_m06_freeport_0050_delta1', attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m06_freeport_0050_delta1, userprops={'category': 'Audio'})
        DX_m06_freeport_0060_delta1 = Sound(root=self, name='DX_m06_freeport_0060_delta1',
            sound='DX_m06_freeport_0060_delta1', attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m06_freeport_0060_delta1, userprops={'category': 'Audio'})
        DX_m06_freeport_0070_trent = Sound(root=self, name='DX_m06_freeport_0070_trent', sound='DX_m06_freeport_0070_trent',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m06_freeport_0070_trent, userprops={'category': 'Audio'})
        DX_m06_freeport_0090_delta1 = Sound(root=self, name='DX_m06_freeport_0090_delta1',
            sound='DX_m06_freeport_0090_delta1', attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m06_freeport_0090_delta1, userprops={'category': 'Audio'})
        DX_m06_freeport_0100_delta1 = Sound(root=self, name='DX_m06_freeport_0100_delta1',
            sound='DX_m06_freeport_0100_delta1', attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m06_freeport_0100_delta1, userprops={'category': 'Audio'})
        DX_m07_offer_0010_barman = Sound(root=self, name='DX_m07_offer_0010_barman', sound='DX_m07_offer_0010_barman',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m07_offer_0010_barman, userprops={'category': 'Audio'})
        DX_m07_offer_0020_trent = Sound(root=self, name='DX_m07_offer_0020_trent', sound='DX_m07_offer_0020_trent',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m07_offer_0020_trent, userprops={'category': 'Audio'})
        DX_m07_offer_0030_barman = Sound(root=self, name='DX_m07_offer_0030_barman', sound='DX_m07_offer_0030_barman',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m07_offer_0030_barman, userprops={'category': 'Audio'})
        DX_m07_offer_0040_trent = Sound(root=self, name='DX_m07_offer_0040_trent', sound='DX_m07_offer_0040_trent',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m07_offer_0040_trent, userprops={'category': 'Audio'})
        DX_m07_offer_0050_barman = Sound(root=self, name='DX_m07_offer_0050_barman', sound='DX_m07_offer_0050_barman',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m07_offer_0050_barman, userprops={'category': 'Audio'})
        DX_m07_offer_0060_trent = Sound(root=self, name='DX_m07_offer_0060_trent', sound='DX_m07_offer_0060_trent',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m07_offer_0060_trent, userprops={'category': 'Audio'})
        DX_m07_offer_0070_barman = Sound(root=self, name='DX_m07_offer_0070_barman', sound='DX_m07_offer_0070_barman',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m07_offer_0070_barman, userprops={'category': 'Audio'})
        DX_m07_offer_0080_barman = Sound(root=self, name='DX_m07_offer_0080_barman', sound='DX_m07_offer_0080_barman',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m07_offer_0080_barman, userprops={'category': 'Audio'})
        DX_m07_offer_0090_barman = Sound(root=self, name='DX_m07_offer_0090_barman', sound='DX_m07_offer_0090_barman',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m07_offer_0090_barman, userprops={'category': 'Audio'})
        DX_m07_offer_0100_barman = Sound(root=self, name='DX_m07_offer_0100_barman', sound='DX_m07_offer_0100_barman',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m07_offer_0100_barman, userprops={'category': 'Audio'})
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
        cam_trent_deal = LookAtCamera(root=self, name='cam_trent_deal', fov=15, farplane=5000, look_duration=70)
        preserve_entity(cam_trent_deal)

        # Вход / начальная постановка.
        t = 0


        # Реплика 110 · trent · исходное время 0 с
        # Звучит заманчиво, я в деле.
        # Исходное окно facial: 6 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_bartender_fixture', target_name='offscreen',
            duration=0, smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent_base', target_name='offscreen', duration=0,
            smooth=False)
        barman.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=10000, loop=True)
        cam_trent_deal.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=15,
            time_scale=0.5)
        cam_trent_deal.set(group=MAIN, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_head_barman_near',
            duration=100, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        trent.facial(group=MAIN, index=110, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.0)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M07OfferAcceptScene
