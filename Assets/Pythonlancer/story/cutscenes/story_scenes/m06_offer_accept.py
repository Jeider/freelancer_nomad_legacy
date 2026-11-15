"""m06_offer_accept: постановка для ручного редактирования.

Точки: SCENES/m06_offer_accept.blend → DUMPS/m06_offer_accept.json.
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
    StaticCamera,
)
from story.cutscenes.anim import (
    Female,
    Male,
)
from story.cutscenes.source_extensions import (
    preserve_entity,
)
from story import actors



class M06OfferAcceptScene(Scene):
    DUMP_FILE = 'm06_offer_accept'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'Actor': 'Player', 'category': 'Character'})
        alaric = Character(root=self, actor=actors.Alaric, light_group=0, init_point='Char_alaric', rotate_from_quat=True,
            use_ambient=True, floor_height=0)
        preserve_entity(alaric, template_name='alaric', userprops={'actor': 'Alaric', 'category': 'Character'})
        hatcher = Character(root=self, actor=actors.Hatcher, light_group=0, init_point='Char_hatcher',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(hatcher, template_name='hatcher', userprops={'actor': 'Hatcher', 'category': 'Character'})
        cam_hatcher = LookAtCamera(root=self, name='cam_hatcher', fov=20, farplane=5000, look_duration=300)
        preserve_entity(cam_hatcher)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=22, farplane=5000, look_duration=1)
        preserve_entity(cam_trent)
        cam_friends = StaticCamera(root=self, name='cam_friends', fov=22, farplane=5000)
        preserve_entity(cam_friends)
        cam_alaric = StaticCamera(root=self, name='cam_alaric', fov=22, farplane=5000)
        preserve_entity(cam_alaric)

        # Вход / начальная постановка.
        t = 0
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=51, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_eye_ik',
            duration=51, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, duration=13, loop=True)
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=25, loop=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=25, loop=True)
        cam_trent.set(group=MAIN, time_delay=t)
        main_group.append_time(1)


        # Реплика 150 · trent · исходное время 1 с
        # У меня дежавю. Вот только в прошлый раз меня называли не "мистер Трент", а "герр Трент"... С другой
        # стороны, временами было весело... Хорошо, я в деле.
        # Исходное окно facial: 17.4 с.
        t = 0
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_alaric_near_far', duration=2.25, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_alaric_near', duration=1.25, smooth=True)
        t += 4
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_hatcher', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_hatcher', duration=1.25, smooth=True)
        trent.facial(group=MAIN, index=150, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-7.9)


        # Реплика 160 · hatcher · исходное время 10.5 с
        # Тогда встретимся на орбите и продолжим разговор там.
        # Исходное окно facial: 6 с.
        t = 0
        cam_hatcher.set(group=MAIN, time_delay=t)
        t += 2.5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_WALK_TRNS_270LV_XA_02, duration=15)
        hatcher.facial(group=MAIN, index=160, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.5)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M06OfferAcceptScene
