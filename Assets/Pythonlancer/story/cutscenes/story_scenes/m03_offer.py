"""m03_offer: постановка для ручного редактирования.

Точки: SCENES/m03_offer.blend → DUMPS/m03_offer.json.
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
    RotateAxisEvent,
)
from story.cutscenes.anim import (
    Male,
    Trent,
)
from story.cutscenes.source_extensions import (
    preserve_entity,
)
from story import actors



class M03OfferScene(Scene):
    DUMP_FILE = 'm03_offer'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'actor': 'Player', 'category': 'Character'})
        hassler = Character(root=self, actor=actors.Hassler, light_group=0, init_point='Char_hassler',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(hassler, template_name='hassler', userprops={'category': 'Character', 'actor': 'hassler'})
        wilham = Character(root=self, actor=actors.Wilham, light_group=0, init_point='Char_wilham', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(wilham, template_name='wilham', userprops={'category': 'Character', 'actor': 'wilham'})
        cam_start = LookAtCamera(root=self, name='cam_start', fov=20, farplane=5000, look_duration=300)
        preserve_entity(cam_start)
        cam_trent_hands = LookAtCamera(root=self, name='cam_trent_hands', fov=15, farplane=5000, look_duration=300)
        preserve_entity(cam_trent_hands)
        cam_wilham_near = LookAtCamera(root=self, name='cam_wilham_near', fov=15, farplane=5000, look_duration=300)
        preserve_entity(cam_wilham_near)
        cam_trent_near = LookAtCamera(root=self, name='cam_trent_near', fov=15, farplane=5000, look_duration=300)
        preserve_entity(cam_trent_near)
        cam_wilham_far = LookAtCamera(root=self, name='cam_wilham_far', fov=16, farplane=5000, look_duration=300)
        preserve_entity(cam_wilham_far)
        cam_trent_far = LookAtCamera(root=self, name='cam_trent_far', fov=15, farplane=5000, look_duration=300)
        preserve_entity(cam_trent_far)
        cam_top = LookAtCamera(root=self, name='cam_top', fov=25, farplane=5000, look_duration=300)
        preserve_entity(cam_top)

        # Вход / начальная постановка.
        t = 0
        cam_start.set(group=MAIN, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_wilham', target_name='automarker_wilham_head_ik',
            duration=19.5, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_wilham', target_name='automarker_wilham_eye_ik',
            duration=90, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_hassler', target_name='automarker_hassler_head_ik',
            duration=90, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_hassler', target_name='automarker_hassler_eye_ik',
            duration=90, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_start', target_name='automarker_cam_start_pos2',
            duration=6, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_start_focus',
            target_name='automarker_cam_start_marker_pos2', duration=6, smooth=True)
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_HOLD_ARMS_CROSSED_000LV_XA_02, duration=7,
            time_scale=0.8, loop=True)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=5, time_scale=0.5,
            loop=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=15, time_scale=0.6)
        main_group.append_time(2)


        # Реплика 10 · trent · исходное время 2 с
        # Салют, джентльмены.
        # Исходное окно facial: 4.5 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_head_ik',
            target_name='automarker_head_trent', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_head_trent', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_wilham_half', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_wilham', duration=2, smooth=True)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hassler_head_ik',
            target_name='automarker_head_trent', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hassler_eye_ik',
            target_name='automarker_head_trent', duration=3, smooth=True)
        trent.facial(group=MAIN, index=10, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.5)


        # Реплика 20 · wilham · исходное время 4 с
        # А вот и герр Трент. Познакомьтесь с герром Хасслером. В ходе этой миссии вам придется плотно
        # сотрудничать.
        # Исходное окно facial: 12 с.
        t = 0
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_head_ik',
            target_name='automarker_head_hassler_half', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_head_hassler_half', duration=1, smooth=True)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_GESTR_RGHT_000LV_XA_02, duration=10,
            time_scale=0.4, trans_time=1.5)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=90, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_eye_ik',
            duration=90, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hassler_head_ik',
            target_name='automarker_head_trent_half', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hassler_eye_ik',
            target_name='automarker_head_wilham_half', duration=2, smooth=True)
        t += 2.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_head_ik',
            target_name='automarker_head_trent', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_head_trent', duration=1, smooth=True)
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, duration=7,
            time_scale=0.8)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_hassler', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_hassler', duration=3, smooth=True)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hassler_head_ik',
            target_name='automarker_head_trent', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hassler_eye_ik',
            target_name='automarker_head_trent', duration=2, smooth=True)
        t += 1.5
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=25, axis='Y_AXIS', duration=2,
            smooth=True)
        wilham.facial(group=MAIN, index=20, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-5)


        # Реплика 30 · trent · исходное время 11 с
        # Герр Хасслер, мое почтение.
        # Исходное окно facial: 4.5 с.
        t = 0
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_SHAK_RHAND_000LV_XA_03, duration=15, time_scale=0.7,
            trans_time=0.25)
        cam_trent_hands.set(group=MAIN, time_delay=t)
        t += 0.3
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_SHAK_RGHT_000LV_A_03, duration=15, time_scale=0.7,
            trans_time=0.25)
        t += 1.7
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_trent_hands_focus',
            target_name='automarker_cam_trent_hands_marker_pos2', duration=5, smooth=True)
        t += 0.5
        trent.motion(group=MAIN, time_delay=t, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, duration=5, trans_time=1)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_wilham_half', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_wilham', duration=2, smooth=True)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=-25, axis='Y_AXIS', duration=3,
            smooth=True)
        trent.facial(group=MAIN, index=30, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.0)


        # Реплика 40 · trent · исходное время 14.5 с
        # И в чем же будет состоять эта миссия?
        # Исходное окно facial: 4.5 с.
        t = 0
        t += 2.0
        trent.motion(group=MAIN, time_delay=t, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, duration=5, trans_time=1)
        t += 0.75
        cam_wilham_far.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=40, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.5)


        # Реплика 50 · wilham · исходное время 17.5 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m03_offer_0050_wilham
        # Исходное окно facial: 10 с.
        t = 0
        t += 0.5
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_LSTN_SMALL_000LV_A_34, duration=40,
            time_scale=0.5, loop=True, trans_time=1)
        t += 1.5
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_SHAKHEAD_NO_SLGHTLY_000LV_XA_02, duration=15)
        t += 0.5
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=3, time_scale=0.4)
        t += 1.2
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=1, time_scale=0.75)
        # wilham.facial(group=MAIN, index=50, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(10.0)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-5.5)


        # Реплика 60 · trent · исходное время 22 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m03_offer_0060_trent
        # Исходное окно facial: 8.2 с.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=2.5,
            time_scale=0.5, trans_time=0.25)
        t += 2.5
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_HOLD_000LV_XA_02, duration=2.5,
            time_scale=0.5, loop=True, trans_time=0.25)
        t += 0.5
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=3, time_scale=0.4)
        # trent.facial(group=MAIN, index=60, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(8.2)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.2)


        # Реплика 70 · wilham · исходное время 30 с
        # Наша разведка локализовала местонахождение Дитриха. Это бывшая военная база Кёнигсберг.
        # Исходное окно facial: 8.5 с.
        t = 0
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_wilham', target_name='automarker_wilham_head_ik',
            duration=40, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=3, time_scale=0.4)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_wilham', angle=10, axis='Y_AXIS', duration=1,
            smooth=True)
        cam_wilham_far.set(group=MAIN, time_delay=t)
        t += 1
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_MED_000LV_xa_05, duration=5, time_scale=0.5,
            trans_time=2)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_wilham_far',
            target_name='automarker_cam_wilham_far_pos2', duration=23, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_wilham_far_focus',
            target_name='automarker_cam_wilham_far_marker_pos2', duration=23, smooth=True)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_HNDSUP_TRNS_000LV_XA_00, duration=3,
            time_scale=0.5, trans_time=1.5)
        t += 3
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=3, time_scale=0.4)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_head_ik',
            target_name='automarker_head_hassler_half', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_head_hassler', duration=1, smooth=True)
        wilham.facial(group=MAIN, index=70, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.5)


        # Реплика 75 · wilham · исходное время 37 с
        # В данный момент собирается ударный флот для атаки базы, но её системы защита будет готова к лобовому
        # удару.
        # Исходное окно facial: 16 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hassler_head_ik',
            target_name='automarker_head_wilham_half', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hassler_eye_ik',
            target_name='automarker_head_wilham', duration=1.5, smooth=True)
        t += 3
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=3, time_scale=0.4)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_head_ik',
            target_name='automarker_head_trent_half', duration=1.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_head_trent', duration=1, smooth=True)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hassler_head_ik',
            target_name='automarker_head_trent', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hassler_eye_ik',
            target_name='automarker_head_trent', duration=1.5, smooth=True)
        t += 2
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_HNDS_CASL_000LV_xc_01, duration=8,
            time_scale=0.5, loop=True, trans_time=1.5)
        t += 1
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=3, time_scale=0.4)
        wilham.facial(group=MAIN, index=75, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-3.8)


        # Реплика 77 · wilham · исходное время 49.2 с
        # Поэтому мы формируем мобильную диверсионную группу, которая нанесет критические повреждения Кёнигсбергу
        # до момента подхода основных сил.
        # Исходное окно facial: 11.8 с.
        t = 0
        t += 0.8
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=3, time_scale=0.4)
        t += 2.0
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_HNDSDN_TRNS_000LV_XA_01, duration=3,
            time_scale=0.5, trans_time=1.5)
        t += 3.0
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=3, time_scale=0.4)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_GESTL_FIST_000LV_00, duration=1, time_scale=2)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_GESTR_FIST_000LV_00, duration=1, time_scale=2)
        wilham.facial(group=MAIN, index=77, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-3.0)


        # Реплика 80 · trent · исходное время 58 с
        # То есть те, кто будет таскать вам каштаны из огня.
        # Исходное окно facial: 3 с.
        t = 0
        cam_top.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_top', target_name='automarker_cam_top_pos2',
            duration=10, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_top_focus',
            target_name='automarker_cam_top_marker_pos2', duration=10, smooth=True)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_LSTN_SMALL_000LV_A_34, duration=3, loop=True)
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_LSTN_000DN_A_18, duration=15, loop=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_HOLD_000LV_XA_02, duration=5,
            time_scale=0.5, loop=True)
        trent.facial(group=MAIN, index=80, append=True, auto_lip=True, extra_delay=0)
        t = 0
        trent.motion(group=MAIN, time_delay=t, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, duration=5, trans_time=0.25)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_GESTR_THMBSUP_000LV_XA_02, duration=5,
            time_scale=0.75, trans_time=0.25)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_POINT_RGHT_CASL_000LV_00, duration=4,
            time_scale=1.5, start_time=3, trans_time=0.5)
        main_group.append_time(0.5)


        # Реплика 90 · wilham · исходное время 61.5 с
        # Именно так, герр Трент. Кстати на вашем участии в этой миссии настаивал лично адмирал Райхманн.
        # Исходное окно facial: 12 с.
        t = 0
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_hassler_trent', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_hassler', duration=1.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_head_ik',
            target_name='automarker_head_trent_half_right', duration=2.5, smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=5,
            time_scale=0.5, trans_time=0.25)
        t += 3.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_wilham_half', duration=2.2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_wilham', duration=1.1, smooth=True)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_TALK_SMALL_000DN_A_17, duration=15, time_scale=0.3,
            loop=True, trans_time=1)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_LSTN_SMALL_000LV_B_09, duration=5, time_scale=0.75,
            trans_time=0.25)
        wilham.facial(group=MAIN, index=90, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-5.5)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M03OfferScene
