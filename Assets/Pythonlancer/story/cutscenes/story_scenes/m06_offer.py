"""m06_offer: постановка для ручного редактирования.

Точки: SCENES/m06_offer.blend → DUMPS/m06_offer.json.
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
    Sound,
)
from story.cutscenes.anim import (
    Female,
    Male,
)
from story.cutscenes.source_extensions import (
    preserve_entity,
)
from story import actors



class M06OfferScene(Scene):
    DUMP_FILE = 'm06_offer'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        DX_m06_offer_0150_trent = Sound(root=self, name='DX_m06_offer_0150_trent', sound='DX_m06_offer_0150_trent',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m06_offer_0150_trent, userprops={'category': 'Audio'})
        DX_m06_offer_0160_hatcher = Sound(root=self, name='DX_m06_offer_0160_hatcher', sound='DX_m06_offer_0160_hatcher',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m06_offer_0160_hatcher, userprops={'category': 'Audio'})
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'Actor': 'Player', 'category': 'Character'})
        alaric = Character(root=self, actor=actors.Alaric, light_group=0, init_point='Char_alaric', rotate_from_quat=True,
            use_ambient=True, floor_height=0)
        preserve_entity(alaric, template_name='alaric', userprops={'actor': 'Alaric', 'category': 'Character'})
        hatcher = Character(root=self, actor=actors.Hatcher, light_group=0, init_point='Char_hatcher',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(hatcher, template_name='hatcher', userprops={'actor': 'Hatcher', 'category': 'Character'})
        cam_start = LookAtCamera(root=self, name='cam_start', fov=30, farplane=5000, look_duration=30)
        preserve_entity(cam_start)
        cam_trent_arrive = LookAtCamera(root=self, name='cam_trent_arrive', fov=25, farplane=5000, look_duration=1)
        preserve_entity(cam_trent_arrive)
        cam_greetings = LookAtCamera(root=self, name='cam_greetings', fov=22, farplane=5000, look_duration=300)
        preserve_entity(cam_greetings)
        cam_hatcher = LookAtCamera(root=self, name='cam_hatcher', fov=20, farplane=5000, look_duration=300)
        preserve_entity(cam_hatcher)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=22, farplane=5000, look_duration=1)
        preserve_entity(cam_trent)
        cam_friends = LookAtCamera(root=self, name='cam_friends', fov=22, farplane=5000, look_duration=1)
        preserve_entity(cam_friends)
        cam_alaric = LookAtCamera(root=self, name='cam_alaric', fov=22, farplane=5000, look_duration=1)
        preserve_entity(cam_alaric)

        # Вход / начальная постановка.
        t = 0
        cam_start.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, duration=0.01)
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_XB_04, duration=2, loop=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=3.8, time_scale=0.8, loop=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_start', target_name='automarker_cam_start_pos2',
            duration=3.8, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_start_focus',
            target_name='automarker_cam_start_marker_pos2', duration=3.8, smooth=True)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_hatcher', target_name='Char_trent', duration=10,
            transition_duration=2, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 2
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_SITCR_TRNS_180DN_XA_06, duration=1.8, trans_time=1)
        t += 1.8
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=4, time_scale=0.8)
        cam_trent_arrive.set(group=MAIN, time_delay=t)
        t += 0.001
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_alaric', target_name='automarker_point_alaric_sit',
            duration=0.001, smooth=False)
        t += 0.01
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=5)
        t += 0.189
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=200, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_eye_ik',
            duration=200, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        main_group.append_time(5)


        # Реплика 10 · trent · исходное время 5 с
        # Мисс Хетчер. Аларик, не ожидал, что ты уже здесь.
        # Исходное окно facial: 8 с.
        t = 0
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_table_center', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_alaric_btm', duration=1.3, smooth=True)
        t += 0.5
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=10, axis='Y_AXIS', duration=2,
            smooth=True)
        t += 0.5
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_alaric', target_name='automarker_alaric_head_ik',
            duration=25, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_alaric', target_name='automarker_alaric_eye_ik',
            duration=25, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_alaric', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_alaric', duration=1.5, smooth=True)
        t += 0.5
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_SITCR_TRNS_180DN_XA_06, duration=1, time_scale=0.7,
            trans_time=1)
        trent.facial(group=MAIN, index=10, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-4.5)


        # Реплика 20 · alaric · исходное время 8.5 с
        # Как только ты со мной связался, я сразу же прибыл к мисс Хетчер. Видимо, я был ближе, чем ты.
        # Исходное окно facial: 12 с.
        t = 0
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_CONV_LHNDUP_TRNS_000LV_XA_02, duration=7,
            time_scale=0.5, trans_time=0.25)
        cam_greetings.set(group=MAIN, time_delay=t)
        t += 0.001
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', target_name='automarker_point_trent_sit',
            duration=0.001, smooth=False)
        t += 0.01
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=5)
        t += 2.489
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_CONV_LHND_CASL_000LV_xa_03, duration=2,
            time_scale=0.5, trans_time=1)
        t += 2.0
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_CONV_LHNDDN_TRNS_000LV_XA_02, duration=4,
            time_scale=0.5, trans_time=2)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_greetings',
            target_name='automarker_cam_greetings_pos2', duration=6, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_greetings_focus',
            target_name='automarker_cam_greetings_marker_pos2', duration=6, smooth=True)
        t += 1.5
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_hatcher', target_name='automarker_hatcher_head_ik',
            duration=200, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_hatcher', target_name='automarker_hatcher_eye_ik',
            duration=200, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_alaric_head_ik',
            target_name='automarker_head_hatcher', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_alaric_eye_ik',
            target_name='automarker_head_hatcher', duration=1.5, smooth=True)
        alaric.facial(group=MAIN, index=20, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-5.0)


        # Реплика 30 · hatcher · исходное время 15.5 с
        # А теперь, господа, когда все выяснили когда, откуда и каким образом мы все сюда прибыли, перейдем к делу?
        # ...
        # Исходное окно facial: 17.5 с.
        t = 0
        t += 1.0
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=25, loop=True,
            trans_time=2)
        t += 1.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_trent', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1.5, smooth=True)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=5,
            time_scale=0.7, trans_time=1)
        t += 2.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_alaric_near', duration=1.75, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_alaric_near', duration=1.25, smooth=True)
        t += 1.8
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHEAD_MOTION_MOUTH_CLENCH_000LV_, duration=1,
            trans_time=0.4)
        t += 0.2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_trent', duration=1.8, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1.25, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_greetings',
            target_name='automarker_cam_greetings_pos3', duration=30, smooth=True)
        t += 1.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHEAD_BASEPOSE_000LV_02_01, duration=0.5, time_scale=0.8,
            trans_time=0.5)
        hatcher.facial(group=MAIN, index=30, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-9.0)


        # Реплика 40 · hatcher · исходное время 24 с
        # Отлично! Как вы уже поняли есть некий объект - Сфера. В свое время его обнаружил еще Орден, но тогда
        # никто не смог понять что это, для чего предназначено и как работает. И про Сферу забыли.
        # Исходное окно facial: 12.2 с.
        t = 0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=4,
            time_scale=0.6, trans_time=1)
        t += 3
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_alaric_near', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_alaric_near', duration=1.4, smooth=True)
        t += 1
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, duration=8, time_scale=0.6,
            loop=True, trans_time=1)
        t += 5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_trent', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1.4, smooth=True)
        t += 2
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_CONV_LHNDUP_TRNS_000LV_XA_01, duration=2,
            time_scale=0.5, trans_time=1)
        hatcher.facial(group=MAIN, index=40, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.2)


        # Реплика 50 · hatcher · исходное время 36 с
        # А теперь мы узнаём что рейнландцам удалось подобрать к ней ключ и они проводят на ней свои исследования.
        # Есть обоснованное мнение, что ничем хорошим это не закончится. Поэтому исследования эти нужно, как бы это
        # сказать... закрыть.
        # Исходное окно facial: 15 с.
        t = 0
        t += 0.7
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_CONV_LHND_CASL_000LV_xa_03, duration=3,
            time_scale=0.5, loop=True, trans_time=1)
        t += 1.3
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_alaric_near', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_alaric_near', duration=1.4, smooth=True)
        t += 1.8
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_CONV_LHNDDN_TRNS_000LV_XA_01, duration=3,
            time_scale=0.5, trans_time=1.5)
        t += 0.2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_trent', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1.4, smooth=True)
        t += 1
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHEAD_BASEPOSE_000LV_02_01, duration=0.5, time_scale=0.8,
            trans_time=0.5)
        t += 3
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_alaric_near', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_alaric_near', duration=1.4, smooth=True)
        t += 1
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=5,
            time_scale=0.7, trans_time=1)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_hatcher', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_hatcher', duration=1, smooth=True)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_trent', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1.2, smooth=True)
        hatcher.facial(group=MAIN, index=50, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.5)


        # Реплика 60 · trent · исходное время 50.5 с
        # Ха-ха-ха, отлично. Если вы не смогли подобрать к Сфере ключ сами, то никто не должен. А если подобрал, то
        # нужно срочно устранить либо ключ, либо Сферу, либо того кто это сделал. Браво! Так не доставайся же ты
        # никому.
        # Исходное окно facial: 18.3 с.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=6)
        t += 6.0
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_GRABR_CHIN_RLEASE_000LV_XA_02, duration=3,
            time_scale=0.6, trans_time=1)
        t += 1.0
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_GESTR_FIST_000LV_00, duration=4, trans_time=0.25)
        t += 3.0
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_HOLD_CHIN_RLEASE_000LV_XA_03, duration=7,
            time_scale=0.6, trans_time=1)
        t += 1.0
        trent.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHAND_NEUT_RGHT_000LV_A_00, duration=4, time_scale=0.5,
            trans_time=1)
        t += 2.5
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=6, trans_time=1)
        trent.facial(group=MAIN, index=60, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.3)


        # Реплика 70 · hatcher · исходное время 66.5 с
        # Я не разделяю вашего сарказма, мистер Трент. В прошлый раз подобная ситуация случилась, когда другие
        # рейнландские ученые нашли нечто в Омикронах. Ох уж мне эти неугомонные рейнландцы.
        # Исходное окно facial: 13.5 с.
        t = 0
        cam_hatcher.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_TILT_HEAD_QUZZCLLY_000LV_XA_04, duration=4,
            time_scale=0.6, start_time=1)
        t += 2.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=5,
            time_scale=0.8, trans_time=1)
        t += 2.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRF_CONV_RHNDUP_TRNS_000LV_XA_02, duration=2,
            time_scale=0.6, trans_time=1)
        t += 2.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRF_CONV_RHNDDN_TRNS_000LV_XA_02, duration=4,
            time_scale=0.5, trans_time=1)
        t += 4.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=4,
            time_scale=0.6, trans_time=1)
        hatcher.facial(group=MAIN, index=70, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.5)


        # Реплика 80 · hatcher · исходное время 77.5 с
        # И все закончилось тем самым кризисом, про который я вам рассказывала в присутствие профессора Мандрейка.
        # Вы поняли, о чем я?
        # Исходное окно facial: 10.8 с.
        t = 0
        t += 2.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_TILT_HEAD_QUZZCLLY_000LV_XA_04, duration=2,
            time_scale=0.6, start_time=1, trans_time=1)
        t += 2.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, duration=5, loop=True,
            trans_time=3)
        hatcher.facial(group=MAIN, index=80, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.8)


        # Реплика 90 · trent · исходное время 85.5 с
        # Да, понял. Не стоит шутить с ящиком Пандоры.
        # Исходное окно facial: 15 с.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=8, loop=True)
        trent.facial(group=MAIN, index=90, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-11.0)


        # Реплика 100 · hatcher · исходное время 89.5 с
        # Хорошо, с моральной подоплекой наших действий мы разобрались, теперь про материальную. Вы получите
        # вознаграждение втрое больше обычного, и удостоверения внештатных сотрудников СБА.
        # Исходное окно facial: 12.7 с.
        t = 0
        cam_hatcher.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_alaric_near', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_alaric_near', duration=1.5, smooth=True)
        t += 4.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=5,
            time_scale=0.7, trans_time=1)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_trent', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1.4, smooth=True)
        t += 5.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_alaric_near', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_alaric_near', duration=1.4, smooth=True)
        t += 1.0
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_alaric', target_name='automarker_alaric_eye_ik',
            duration=25, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        hatcher.facial(group=MAIN, index=100, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.7)


        # Реплика 110 · alaric · исходное время 101.5 с
        # Чёрт побери, я за! Где ставить подпись? Могу кровью!
        # Исходное окно facial: 5.7 с.
        t = 0
        cam_alaric.set(group=MAIN, time_delay=t)
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_SHRG_SHLDRS_BIG_000LV_XA_03, duration=1.25,
            time_scale=0.6, trans_time=1)
        t += 1.25
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=6, time_scale=0.6,
            loop=True, trans_time=2.2)
        t += 0.25
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_alaric_eye_ik',
            target_name='automarker_head_hatcher_near', duration=1, smooth=True)
        t += 2.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_alaric_near_far', duration=0.01, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_alaric_near', duration=0.01, smooth=True)
        t += 0.8
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_alaric_eye_ik',
            target_name='automarker_head_trent', duration=1, smooth=True)
        alaric.facial(group=MAIN, index=110, append=True, auto_lip=True, extra_delay=0)
        t = 0
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=2, trans_time=2)
        main_group.append_time(0.3)


        # Реплика 120 · trent · исходное время 107.5 с
        # Аларик, угомонись. Мисс Хетчер, а что конкретно нужно сделать? Уничтожить Сферу, уничтожить ученых? Мне
        # это совсем не по душе, я всё-таки не наёмный убийца.
        # Исходное окно facial: 14.1 с.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        t += 1.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_hatcher', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_hatcher', duration=1.25, smooth=True)
        t += 6.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_trent', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1, smooth=True)
        t += 2.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRF_CONV_RHNDDN_TRNS_000LV_XA_02, duration=2,
            time_scale=0.5, start_time=1.2)
        trent.facial(group=MAIN, index=120, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-4.1)


        # Реплика 130 · hatcher · исходное время 117.5 с
        # А вы уверены? Нет, все не так страшно и кроваво, как вы сейчас расписали. В полученных нами документах
        # профессор нашел способ сделать Сферу невосприимчивой к внешним воздействиям, как сказал профессор
        # "закрыться".
        # Исходное окно facial: 14.5 с.
        t = 0
        cam_hatcher.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_greetings',
            target_name='automarker_cam_greetings_pos3', duration=18, smooth=True)
        t += 2.2
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=5,
            time_scale=0.6, trans_time=1)
        t += 4.8
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_alaric_near', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_alaric', duration=1.8, smooth=True)
        t += 0.5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, duration=15, loop=True,
            trans_time=1)
        t += 2.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_trent', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1.4, smooth=True)
        hatcher.facial(group=MAIN, index=130, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.5)


        # Реплика 140 · hatcher · исходное время 131.5 с
        # Все дальнейшие подробности - в том случае, если вы согласитесь.
        # Исходное окно facial: 6 с.
        t = 0
        hatcher.facial(group=MAIN, index=140, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.0)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M06OfferScene
