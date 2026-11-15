"""m04_offer_accept: постановка для ручного редактирования.

Точки: SCENES/m04_offer_accept.blend → DUMPS/m04_offer_accept.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — смещение внутри текущего блока; facial()/append_time() двигают часы.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character,
    EyeIkEvent,
    LookAtCamera,
    MAIN,
    MoveEvent,
    NeckIkEvent,
    SetCameraEvent,
    Sound,
)
from story.cutscenes.anim import (
    Male,
)
from story.cutscenes.source_extensions import (
    preserve_entity,
)
from story import actors



class M04OfferAcceptScene(Scene):
    DUMP_FILE = 'm04_offer_accept'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        DX_m04_offer_0010_jacobo = Sound(root=self, name='DX_m04_offer_0010_jacobo', sound='DX_m04_offer_0010_jacobo',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m04_offer_0010_jacobo, userprops={'category': 'Audio'})
        DX_m04_offer_0020_jacobo = Sound(root=self, name='DX_m04_offer_0020_jacobo', sound='DX_m04_offer_0020_jacobo',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m04_offer_0020_jacobo, userprops={'category': 'Audio'})
        DX_m04_offer_0030_trent = Sound(root=self, name='DX_m04_offer_0030_trent', sound='DX_m04_offer_0030_trent',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m04_offer_0030_trent, userprops={'category': 'Audio'})
        DX_m04_offer_0040_jacobo = Sound(root=self, name='DX_m04_offer_0040_jacobo', sound='DX_m04_offer_0040_jacobo',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m04_offer_0040_jacobo, userprops={'category': 'Audio'})
        DX_m04_offer_0050_trent = Sound(root=self, name='DX_m04_offer_0050_trent', sound='DX_m04_offer_0050_trent',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m04_offer_0050_trent, userprops={'category': 'Audio'})
        DX_m04_offer_0060_jacobo = Sound(root=self, name='DX_m04_offer_0060_jacobo', sound='DX_m04_offer_0060_jacobo',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m04_offer_0060_jacobo, userprops={'category': 'Audio'})
        DX_m04_offer_0062_jacobo = Sound(root=self, name='DX_m04_offer_0062_jacobo', sound='DX_m04_offer_0062_jacobo',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m04_offer_0062_jacobo, userprops={'category': 'Audio'})
        DX_m04_offer_0065_jacobo = Sound(root=self, name='DX_m04_offer_0065_jacobo', sound='DX_m04_offer_0065_jacobo',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m04_offer_0065_jacobo, userprops={'category': 'Audio'})
        DX_m04_offer_0067_jacobo = Sound(root=self, name='DX_m04_offer_0067_jacobo', sound='DX_m04_offer_0067_jacobo',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m04_offer_0067_jacobo, userprops={'category': 'Audio'})
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'actor': 'Player', 'category': 'Character'})
        jacobo = Character(root=self, actor=actors.Jacobo, light_group=0, init_point='Char_jacobo', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(jacobo, template_name='jacobo', userprops={'category': 'Character', 'actor': 'jacobo'})
        cam_jacobo_sitting = LookAtCamera(root=self, name='cam_jacobo_sitting', fov=16, farplane=5000, look_duration=300)
        preserve_entity(cam_jacobo_sitting)
        cam_trent_sitting = LookAtCamera(root=self, name='cam_trent_sitting', fov=16, farplane=5000, look_duration=300)
        preserve_entity(cam_trent_sitting)

        # Вход / начальная постановка.
        t = 0


        # Реплика 70 · trent · исходное время 0 с
        # Я об этом еще пожалею... Хорошо, каков план?
        # Исходное окно facial: 7 с.
        t = 0
        SetCameraEvent(root=self, group=MAIN, time_delay=t, camera_name='cam_start')
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=2)
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=3)
        cam_trent_sitting.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=5)
        trent.facial(group=MAIN, index=70, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-3)


        # Реплика 80 · jacobo · исходное время 4 с
        # Герр Трент, спасибо, вы не пожалеете! Вылетайте в космос, я с помощью друзей попробую незаметно
        # пробраться на взлетную площадку. Встретимся на орбите.
        # Исходное окно facial: 11 с.
        t = 0
        cam_jacobo_sitting.set(group=MAIN, time_delay=t)
        t += 8
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_STNDCL_TRNS_270LV_XA_06, duration=2.5, trans_time=1)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_jacobo_standing', duration=0.1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_jacobo_standing', duration=0.1, smooth=True)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_jacobo_standing_go_out', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_jacobo_standing_go_out', duration=1, smooth=True)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=2, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_eye_ik',
            duration=2, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        jacobo.facial(group=MAIN, index=80, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.5)


        # Реплика 90 · trent · исходное время 14.5 с
        # Тогда до встречи.
        # Исходное окно facial: 4 с.
        t = 0
        cam_trent_sitting.set(group=MAIN, time_delay=t)
        t += 1.0
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_STNDCR_TRNS_090LV_XA_05, duration=5, trans_time=1)
        trent.facial(group=MAIN, index=90, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(1.0)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M04OfferAcceptScene
