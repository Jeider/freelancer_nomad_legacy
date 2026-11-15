"""m08_offer: постановка для ручного редактирования.

Точки: SCENES/m08_offer.blend → DUMPS/m08_offer.json.
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
    SoundEvent,
)
from story.cutscenes.anim import (
    Female,
    Male,
)
from story.cutscenes.source_extensions import (
    preserve_entity,
)
from story import actors



class M08OfferScene(Scene):
    DUMP_FILE = 'm08_offer'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        DX_m08_offer_0440_trent = Sound(root=self, name='DX_m08_offer_0440_trent', sound='DX_m08_offer_0440_trent',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m08_offer_0440_trent, userprops={'category': 'Audio'})
        DX_m08_offer_0450_kaitlyn = Sound(root=self, name='DX_m08_offer_0450_kaitlyn', sound='DX_m08_offer_0450_kaitlyn',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m08_offer_0450_kaitlyn, userprops={'category': 'Audio'})
        DX_m08_offer_0460_kaitlyn = Sound(root=self, name='DX_m08_offer_0460_kaitlyn', sound='DX_m08_offer_0460_kaitlyn',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m08_offer_0460_kaitlyn, userprops={'category': 'Audio'})
        DX_m08_offer_0470_brighton = Sound(root=self, name='DX_m08_offer_0470_brighton', sound='DX_m08_offer_0470_brighton',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m08_offer_0470_brighton, userprops={'category': 'Audio'})
        DX_m08_offer_0480_darcy = Sound(root=self, name='DX_m08_offer_0480_darcy', sound='DX_m08_offer_0480_darcy',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m08_offer_0480_darcy, userprops={'category': 'Audio'})
        DX_m08_bship_wales_0010_brighton = Sound(root=self, name='DX_m08_bship_wales_0010_brighton',
            sound='DX_m08_bship_wales_0010_brighton', attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m08_bship_wales_0010_brighton, userprops={'category': 'Audio'})
        DX_m08_bship_wales_0020_brighton = Sound(root=self, name='DX_m08_bship_wales_0020_brighton',
            sound='DX_m08_bship_wales_0020_brighton', attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m08_bship_wales_0020_brighton, userprops={'category': 'Audio'})
        DX_m08_bship_wales_0030_brighton = Sound(root=self, name='DX_m08_bship_wales_0030_brighton',
            sound='DX_m08_bship_wales_0030_brighton', attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m08_bship_wales_0030_brighton, userprops={'category': 'Audio'})
        DX_m08_bship_wales_0040_trent = Sound(root=self, name='DX_m08_bship_wales_0040_trent',
            sound='DX_m08_bship_wales_0040_trent', attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m08_bship_wales_0040_trent, userprops={'category': 'Audio'})
        DX_m08_bship_wales_0050_brighton = Sound(root=self, name='DX_m08_bship_wales_0050_brighton',
            sound='DX_m08_bship_wales_0050_brighton', attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m08_bship_wales_0050_brighton, userprops={'category': 'Audio'})
        DX_m08_bship_wales_0060_darcy = Sound(root=self, name='DX_m08_bship_wales_0060_darcy',
            sound='DX_m08_bship_wales_0060_darcy', attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m08_bship_wales_0060_darcy, userprops={'category': 'Audio'})
        DX_m08_final_0010_mandrake = Sound(root=self, name='DX_m08_final_0010_mandrake', sound='DX_m08_final_0010_mandrake',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m08_final_0010_mandrake, userprops={'category': 'Audio'})
        DX_m08_final_0020_hatcher = Sound(root=self, name='DX_m08_final_0020_hatcher', sound='DX_m08_final_0020_hatcher',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m08_final_0020_hatcher, userprops={'category': 'Audio'})
        DX_m08_final_0030_darcy = Sound(root=self, name='DX_m08_final_0030_darcy', sound='DX_m08_final_0030_darcy',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m08_final_0030_darcy, userprops={'category': 'Audio'})
        DX_m08_final_0040_darcy = Sound(root=self, name='DX_m08_final_0040_darcy', sound='DX_m08_final_0040_darcy',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m08_final_0040_darcy, userprops={'category': 'Audio'})
        kaytlin = Character(root=self, actor=actors.Kaitlyn, light_group=0, init_point='Char_kaitlyn',
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
        cam_start = LookAtCamera(root=self, name='cam_start', fov=20, farplane=5000, look_duration=70)
        preserve_entity(cam_start)
        cam_start_darcy = LookAtCamera(root=self, name='cam_start_darcy', fov=20, farplane=5000, look_duration=70)
        preserve_entity(cam_start_darcy)
        cam_start_trent = LookAtCamera(root=self, name='cam_start_trent', fov=20, farplane=5000, look_duration=70)
        preserve_entity(cam_start_trent)
        cam_greetings = LookAtCamera(root=self, name='cam_greetings', fov=20, farplane=5000, look_duration=70)
        preserve_entity(cam_greetings)
        cam_greetings_kaytlin = LookAtCamera(root=self, name='cam_greetings_kaytlin', fov=15, farplane=5000,
            look_duration=70)
        preserve_entity(cam_greetings_kaytlin)
        cam_darcy_sit = LookAtCamera(root=self, name='cam_darcy_sit', fov=22, farplane=5000, look_duration=70)
        preserve_entity(cam_darcy_sit)
        cam_brighton = LookAtCamera(root=self, name='cam_brighton', fov=18, farplane=5000, look_duration=710)
        preserve_entity(cam_brighton)
        cam_brighton_near = LookAtCamera(root=self, name='cam_brighton_near', fov=18, farplane=5000, look_duration=710)
        preserve_entity(cam_brighton_near)
        cam_trent_sit = LookAtCamera(root=self, name='cam_trent_sit', fov=18, farplane=5000, look_duration=710)
        preserve_entity(cam_trent_sit)
        cam_trent_far = LookAtCamera(root=self, name='cam_trent_far', fov=18, farplane=5000, look_duration=710)
        preserve_entity(cam_trent_far)
        cam_trent_near = LookAtCamera(root=self, name='cam_trent_near', fov=18, farplane=5000, look_duration=710)
        preserve_entity(cam_trent_near)
        cam_trent_xnear = LookAtCamera(root=self, name='cam_trent_xnear', fov=15, farplane=5000, look_duration=710)
        preserve_entity(cam_trent_xnear)
        cam_kaytlin = LookAtCamera(root=self, name='cam_kaytlin', fov=15, farplane=5000, look_duration=710)
        preserve_entity(cam_kaytlin)

        # Вход / начальная постановка.
        t = 0
        kaytlin.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRF_IDLE_000LV_XA_05, duration=10)
        brighton.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=100, time_scale=0.6,
            loop=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_start', target_name='automarker_cam_start_pos2',
            duration=9, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_start_focus',
            target_name='automarker_cam_start_marker_pos2', duration=7, smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=2.6, loop=True)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_darcy', angle=-67, axis='Y_AXIS', duration=0,
            smooth=False)
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_HOLD_ARMS_CROSSED_000LV_XA_03, duration=1)
        t += 0.01
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_kaitlyn', angle=-125, axis='Y_AXIS',
            duration=0, smooth=False)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_brighton', angle=10, axis='Y_AXIS',
            duration=0, smooth=False)
        cam_start.set(group=MAIN, time_delay=t)
        t += 2.59
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=6)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=5, axis='Y_AXIS', duration=1,
            smooth=False)
        t += 0.4
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_UNCRSS_ARMS_000LV_XA_03, duration=5,
            time_scale=0.8)
        main_group.append_time(5)


        # Реплика 10 · darcy · исходное время 5 с
        # Привет. Мы сейчас пройдем в одну комнату, в которой будет пара очень больших шишек.
        # Исходное окно facial: 7 с.
        t = 0
        cam_start_darcy.set(group=MAIN, time_delay=t)
        t += 3
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=5,
            time_scale=0.8)
        darcy.facial(group=MAIN, index=10, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.2)


        # Реплика 20 · darcy · исходное время 10.8 с
        # Очень прошу, постарайся вести себя посдержаннее.
        # Исходное окно facial: 5 с.
        t = 0
        t += 2.7
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_WALK_TRNS_270LV_XA_02, duration=5, time_scale=0.8,
            trans_time=1)
        darcy.facial(group=MAIN, index=20, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.5)


        # Реплика 30 · trent · исходное время 14.3 с
        # Ничего не понял, но постараюсь.
        # Исходное окно facial: 3.5 с.
        t = 0
        cam_start_trent.set(group=MAIN, time_delay=t)
        t += 0.5
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent',
            target_name='automarker_head_darcy_move_from_start', duration=5, transition_duration=2, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 2.2
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01, duration=1, time_scale=0.5,
            trans_time=1)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=-8, axis='Y_AXIS', duration=1,
            smooth=False)
        trent.facial(group=MAIN, index=30, append=True, auto_lip=True, extra_delay=0)
        t = 0
        t += 0.2
        cam_greetings.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_greetings',
            target_name='automarker_cam_greetings_pos2', duration=7, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_greetings_focus',
            target_name='automarker_cam_greetings_marker_pos2', duration=5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_darcy', target_name='automarker_point_darcy_walk',
            duration=0, smooth=False)
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_WLKG_000LV_XA_01, duration=4, time_scale=0.6, loop=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', target_name='automarker_point_trent_walk',
            duration=0, smooth=False)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=4, time_scale=0.6,
            start_time=0.5, loop=True)
        t += 0.01
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_darcy', angle=25, axis='Y_AXIS', duration=0,
            smooth=False)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=25, axis='Y_AXIS', duration=0,
            smooth=False)
        t += 0.99
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_brighton',
            target_name='automarker_head_darcy_near_table', duration=15, transition_duration=2, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        main_group.append_time(2.2)


        # Реплика 40 · brighton · исходное время 20 с
        # А это мисс Дерси, наша краса и надежда на светлое будущее.
        # Исходное окно facial: 6 с.
        t = 0
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_kaitlyn',
            target_name='automarker_head_darcy_near_table', duration=5, transition_duration=2, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        brighton.facial(group=MAIN, index=40, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1)


        # Реплика 50 · kaitlyn · исходное время 25 с
        # А это, если я все правильно поняла, эксперт по Ордену, о котором мне столько рассказывали.
        # Исходное окно facial: 12 с.
        t = 0
        cam_greetings_kaytlin.set(group=MAIN, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_kaitlyn',
            target_name='automarker_head_trent_near_table_up', duration=15, transition_duration=2, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_kaitlyn',
            target_name='automarker_head_trent_near_table', duration=15, transition_duration=2, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 2
        kaytlin.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRF_GRABR_CHIN_RLEASE_000LV_XA_03, duration=7,
            time_scale=0.3, trans_time=1)
        t += 2
        kaytlin.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHAND_HNEUT_GESTR_THUMB_000LV_00, duration=0.5,
            trans_time=1)
        t += 4
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_darcy', target_name='automarker_point_darcy_sit',
            duration=0, smooth=False)
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, duration=1)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_darcy', target_name='automarker_darcy_head_ik',
            duration=2555, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_darcy', target_name='automarker_darcy_eye_ik',
            duration=2555, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 0.01
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_darcy', angle=-15, axis='Y_AXIS', duration=0,
            smooth=False)
        kaytlin.facial(group=MAIN, index=50, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-3)


        # Реплика 60 · darcy · исходное время 34 с
        # Да, это мистер Трент. Трент, это адмирал Брайтон и принцесса Кейтлин.
        # Исходное окно facial: 11.5 с.
        t = 0
        cam_darcy_sit.set(group=MAIN, time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_darcy_head_ik',
            target_name='automarker_head_trent_front', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_darcy_eye_ik',
            target_name='automarker_head_trent', duration=1.5, smooth=True)
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_CONV_LHNDUP_TRNS_000LV_XA_01, duration=2,
            time_scale=0.5, trans_time=1)
        t += 0.8
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_CONV_LHND_CASL_000LV_xa_03, duration=3,
            time_scale=0.4, loop=True, trans_time=1)
        t += 3.0
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_CONV_LHNDDN_TRNS_000LV_XA_01, duration=3,
            time_scale=0.5, trans_time=1.5)
        t += 0.2
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_brighton',
            target_name='automarker_brighton_head_ik', duration=2555, transition_duration=1, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_brighton', target_name='automarker_brighton_eye_ik',
            duration=2555, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        darcy.facial(group=MAIN, index=60, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-5.5)


        # Реплика 70 · brighton · исходное время 40 с
        # И у нас к вам, мистер Трент, чрезвычайно важное дело.
        # Исходное окно facial: 6 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', target_name='automarker_point_trent_sit',
            duration=0, smooth=False)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=1050, time_scale=0.6,
            loop=True)
        cam_brighton.set(group=MAIN, time_delay=t)
        t += 0.01
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=20, axis='Y_AXIS', duration=0,
            smooth=False)
        t += 0.99
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=555, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_eye_ik',
            duration=555, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        brighton.facial(group=MAIN, index=70, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-3)


        # Реплика 80 · trent · исходное время 43 с
        # Шо, опять?
        # Исходное окно facial: 3.5 с.
        t = 0
        cam_trent_xnear.set(group=MAIN, time_delay=t)
        t += 1.7
        cam_brighton_near.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=80, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.7)


        # Реплика 90 · brighton · исходное время 44.8 с
        # Мистер Трент, давайте чуточку серьёзнее. Речь идет о государственной безопасности Бретонии.
        # Исходное окно facial: 6 с.
        t = 0
        brighton.facial(group=MAIN, index=90, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.5)


        # Реплика 100 · trent · исходное время 50.3 с
        # Я постараюсь.
        # Исходное окно facial: 3.5 с.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=100, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.8)


        # Реплика 110 · brighton · исходное время 52 с
        # У нас для вас, мистер Трент, будет небольшое задание по вашему профилю.
        # Исходное окно facial: 8 с.
        t = 0
        cam_brighton.set(group=MAIN, time_delay=t)
        t += 1
        brighton.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_GESTR_SELF_000LV_XA_03, duration=2.3,
            time_scale=0.2, trans_time=0.3)
        brighton.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_POINT_RGHT_CASL_000LV_XB_01, duration=2.3,
            time_scale=0.5)
        t += 2.5
        brighton.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=3, trans_time=1)
        brighton.facial(group=MAIN, index=110, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-4.3)


        # Реплика 120 · trent · исходное время 55.7 с
        # Моему профилю?
        # Исходное окно facial: 3.5 с.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=120, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.0)


        # Реплика 130 · brighton · исходное время 57.2 с
        # Орден, мистер Трент, Орден.
        # Исходное окно facial: 6 с.
        t = 0
        cam_brighton_near.set(group=MAIN, time_delay=t)
        brighton.facial(group=MAIN, index=130, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-3.2)


        # Реплика 140 · trent · исходное время 60 с
        # А... Аааа...
        # Исходное окно facial: 5.5 с.
        t = 0
        cam_trent_xnear.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_SHRG_SHLDRS_SMALL_000LV_XA_03, duration=100,
            time_scale=0.4)
        trent.facial(group=MAIN, index=140, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.5)


        # Реплика 150 · brighton · исходное время 63 с
        # Мистер Трент, смею вас заверить, что данная миссия находится на контроле у самых высокопоставленных лиц
        # Бретонии.
        # Исходное окно facial: 8 с.
        t = 0
        cam_brighton.set(group=MAIN, time_delay=t)
        t += 6
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_brighton_head_ik',
            target_name='automarker_head_kaytlin_front_fwd2', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_brighton_eye_ik',
            target_name='automarker_head_kaytlin_lwr', duration=1.5, smooth=True)
        brighton.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_GESTL_180LV_XA_03, duration=100, time_scale=0.4,
            trans_time=0.5)
        brighton.facial(group=MAIN, index=150, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.3)


        # Реплика 160 · brighton · исходное время 69.7 с
        # Одно то, что на встрече с вами присутствует принцесса Кейтлин, должно о многом вам говорить.
        # Исходное окно facial: 4.7 с.
        t = 0
        t += 2.3
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_brighton_head_ik',
            target_name='automarker_head_trent_brightonside_front', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_brighton_eye_ik',
            target_name='automarker_head_trent_brightonside', duration=1.25, smooth=True)
        brighton.facial(group=MAIN, index=160, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(0.3)


        # Реплика 170 · trent · исходное время 74.7 с
        # Минуй нас пуще всех печалей и барский гнев, и барская любовь...
        # Исходное окно facial: 5.3 с.
        t = 0
        cam_trent_sit.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=170, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(0.0)


        # Реплика 180 · brighton · исходное время 80 с
        # Я не понимаю вашего скептицизма, мистер Трент, будьте чуточку прозорливее
        # Исходное окно facial: 5 с.
        t = 0
        cam_brighton_near.set(group=MAIN, time_delay=t)
        brighton.facial(group=MAIN, index=180, append=True, auto_lip=True, extra_delay=0)
        t = 0


        # Реплика 190 · brighton · исходное время 85 с
        # Вы окажете услугу нам, а мы, при случае, окажем услугу вам.
        # Исходное окно facial: 3.9 с.
        t = 0
        brighton.facial(group=MAIN, index=190, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(0.5)


        # Реплика 200 · trent · исходное время 89.4 с
        # Допустим. А в чём задание-то?
        # Исходное окно facial: 3.5 с.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=200, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.9)


        # Реплика 210 · brighton · исходное время 92 с
        # Вот это уже серьёзный разговор, мистер Трент. Принцесса?
        # Исходное окно facial: 7.8 с.
        t = 0
        cam_brighton.set(group=MAIN, time_delay=t)
        t += 2
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_kaitlyn',
            target_name='automarker_kaytlin_ik_not_interested_head', duration=1000, transition_duration=2,
            target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_kaitlyn',
            target_name='automarker_kaytlin_ik_not_interested_eye', duration=1000, transition_duration=2,
            target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_brighton_head_ik',
            target_name='automarker_head_kaytlin_front_fwd2', duration=1.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_brighton_eye_ik',
            target_name='automarker_head_kaytlin_lwr', duration=1, smooth=True)
        t += 0.5
        kaytlin.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRF_GRABR_HEAD_RLEASE_000LV_XA_03, duration=7,
            trans_time=1)
        kaytlin.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHAND_HNEUT_GESTR_CASL_000LV_00, duration=0.9, trans_time=1)
        brighton.facial(group=MAIN, index=210, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.8)


        # Реплика 215 · kaitlyn · исходное время 97 с
        # Угу...
        # Исходное окно facial: 0 с.
        t = 0
        voice_sound = self.lookup_single_sound(215)
        SoundEvent(root=self, group=MAIN, sound_name=voice_sound.get_nickname())
        t = 0
        cam_kaytlin.set(group=MAIN, time_delay=t)
        kaytlin.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHEAD_MAD_COLD_000LV_XA_, duration=5, start_time=0.8,
            trans_time=0.25)
        t += 2.5
        cam_brighton.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_brighton_head_ik',
            target_name='automarker_head_trent_brightonside_front', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_brighton_eye_ik',
            target_name='automarker_head_trent_brightonside', duration=1.25, smooth=True)
        main_group.append_time(3)


        # Реплика 220 · brighton · исходное время 100 с
        # Мистер Трент, в свое время правительство Бретонии заключило некое соглашение с Орденом.
        # Исходное окно facial: 4.7 с.
        t = 0
        brighton.facial(group=MAIN, index=220, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.2)


        # Реплика 230 · brighton · исходное время 104.5 с
        # Оно сводилось к тому, что Бретония, хм…
        # Исходное окно facial: 4.7 с.
        t = 0
        t += 1.8
        brighton.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_MAD_COLD_000LV_XA_, duration=4.7, start_time=0.6,
            trans_time=0.25)
        t += 0.7
        brighton.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=100,
            time_scale=0.7)
        brighton.facial(group=MAIN, index=230, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.0)


        # Реплика 235 · brighton · исходное время 108.2 с
        # Мистер Трент, а вы слышали о проблеме кочевников?
        # Исходное окно facial: 4.7 с.
        t = 0
        brighton.facial(group=MAIN, index=235, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.7)


        # Реплика 240 · trent · исходное время 111.2 с
        # В общем и целом.
        # Исходное окно facial: 3.5 с.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=240, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.7)


        # Реплика 250 · brighton · исходное время 113 с
        # Отлично. Чуточку осторожности не помешает, вы же меня понимаете?
        # Исходное окно facial: 7.3 с.
        t = 0
        cam_brighton.set(group=MAIN, time_delay=t)
        t += 4
        brighton.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDUP_TRNS_000LV_XA_02, duration=4)
        brighton.facial(group=MAIN, index=250, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.9)


        # Реплика 260 · brighton · исходное время 117.4 с
        # Так вот, по этому соглашению Бретония отказывалась от своих интересов в секторах так называемого
        # "Наследия Номадов", кочевников то есть. Вы понимаете, о чем я, мистер Трент?
        # Исходное окно facial: 16.6 с.
        t = 0
        t += 0.6
        brighton.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00, duration=10)
        t += 0.7
        brighton.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_RHND_CASL_000LV_xb_03, duration=2.3,
            time_scale=0.5, trans_time=1)
        t += 2.3
        brighton.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDDN_TRNS_000LV_XA_02, duration=4,
            trans_time=1)
        brighton.facial(group=MAIN, index=260, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-6.4)


        # Реплика 270 · trent · исходное время 127.6 с
        # Чуточку
        # Исходное окно facial: 3.5 с.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=270, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.1)


        # Реплика 280 · brighton · исходное время 131 с
        # Гхм, хорошо. Взамен Орден обязался ограничить доступ к этим системам для всех. То есть совсем ограничить.
        # Вы меня понимаете, мистер Трент?
        # Исходное окно facial: 14 с.
        t = 0
        cam_brighton.set(group=MAIN, time_delay=t)
        brighton.facial(group=MAIN, index=280, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-4)


        # Реплика 290 · brighton · исходное время 141 с
        # И мы наивно полагали, что СБА, как прямой наследник Ордена, будет придерживаться достигнутых
        # договоренностей. И что же мы видим сейчас?
        # Исходное окно facial: 12.5 с.
        t = 0
        brighton.facial(group=MAIN, index=290, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-3.5)


        # Реплика 300 · trent · исходное время 150 с
        # Что?...
        # Исходное окно facial: 3.5 с.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=300, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.7)


        # Реплика 310 · brighton · исходное время 151.8 с
        # А то, что эти ублюдки из ИРА во всю осваивают Тау-44.
        # Исходное окно facial: 4.3 с.
        t = 0
        cam_brighton_near.set(group=MAIN, time_delay=t)
        brighton.facial(group=MAIN, index=310, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(0.2)


        # Реплика 320 · trent · исходное время 156.3 с
        # Вот сволочи. А Ира - это кто?
        # Исходное окно facial: 5.2 с.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=320, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.2)


        # Реплика 330 · brighton · исходное время 160.3 с
        # Не "кто" а "что". Группа фанатиков, в том числе религиозных, требующих независимости Ирландии от
        # Британской короны.
        # Исходное окно facial: 7 с.
        t = 0
        cam_brighton.set(group=MAIN, time_delay=t)
        brighton.facial(group=MAIN, index=330, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.3)


        # Реплика 340 · trent · исходное время 167 с
        # Достаточно забавно, учитывая что в секторе Сириуса нет ни Ирландии, ни Британской короны.
        # Исходное окно facial: 7 с.
        t = 0
        cam_trent_sit.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=340, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.6)


        # Реплика 350 · kaitlyn · исходное время 173.4 с
        # Мистер Трент...
        # Исходное окно facial: 12 с.
        t = 0
        cam_kaytlin.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_kaytlin_ik_not_interested_head',
            target_name='automarker_kaytlin_ik_not_interested_head_pos2', duration=1.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_kaytlin_ik_not_interested_eye',
            target_name='automarker_kaytlin_ik_not_interested_eye_pos2', duration=1, smooth=True)
        kaytlin.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRF_HOLD_HEAD_RLEASE_000LV_XA_03, duration=7,
            time_scale=0.5)
        t += 1.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_kaytlin_ik_not_interested_eye',
            target_name='automarker_kaytlin_ik_not_interested_eye_pos3', duration=1, smooth=True)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_kaytlin_ik_not_interested_head',
            target_name='automarker_kaytlin_ik_not_interested_head_pos3', duration=1, smooth=True)
        t += 1.0
        kaytlin.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHEAD_MAD_COLD_000LV_XA_, duration=0.8, trans_time=0.5)
        kaytlin.facial(group=MAIN, index=350, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-8.0)


        # Реплика 360 · trent · исходное время 177.4 с
        # А что? Дома Ирландии, насколько я знаю, нет.
        # Исходное окно facial: 7 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_kaytlin_front', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_kaytlin', duration=1.25, smooth=True)
        cam_trent_sit.set(group=MAIN, time_delay=t)
        t += 2.6
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_brighton_head_ik',
            target_name='automarker_head_kaytlin_front_fwd2', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_brighton_eye_ik',
            target_name='automarker_head_kaytlin_lwr', duration=1.5, smooth=True)
        trent.facial(group=MAIN, index=360, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-3.6)


        # Реплика 370 · kaitlyn · исходное время 180.8 с
        # А ирландцы, к сожалению, есть...
        # Исходное окно facial: 12 с.
        t = 0
        cam_kaytlin.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_kaytlin_ik_not_interested_head',
            target_name='automarker_kaytlin_ik_not_interested_head_init', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_kaytlin_ik_not_interested_eye',
            target_name='automarker_kaytlin_ik_not_interested_eye_init', duration=1.8, smooth=True)
        t += 0.6
        kaytlin.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRF_GRABR_HEAD_RLEASE_000LV_XA_03, duration=7,
            time_scale=0.7, trans_time=1)
        kaytlin.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHAND_HNEUT_GESTR_CASL_000LV_00, duration=0.9, trans_time=1)
        t += 2.5
        kaytlin.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHEAD_MAD_COLD_000LV_XA_, duration=0.6, trans_time=0.5)
        kaytlin.facial(group=MAIN, index=370, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-7.4)


        # Реплика 380 · brighton · исходное время 185.4 с
        # Теперь вы понимаете, мистер Трент, насколько все это дико?
        # Исходное окно facial: 8 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_brighton_head_ik',
            target_name='automarker_head_trent_brightonside_front', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_brighton_eye_ik',
            target_name='automarker_head_trent_brightonside', duration=1.25, smooth=True)
        cam_brighton.set(group=MAIN, time_delay=t)
        t += 3.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_brighton', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_brighton', duration=1.25, smooth=True)
        brighton.facial(group=MAIN, index=380, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-4.2)


        # Реплика 390 · trent · исходное время 189.2 с
        # Допустим. Что требуется от меня?
        # Исходное окно facial: 7 с.
        t = 0
        cam_trent_sit.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=390, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-4.6)


        # Реплика 400 · brighton · исходное время 191.6 с
        # Чуточку помочь нам. В составе оперативного отряда вылететь в Тау-44, и очистить систему от присутствия
        # ИРА.
        # Исходное окно facial: 8 с.
        t = 0
        cam_brighton.set(group=MAIN, time_delay=t)
        t += 6.8
        brighton.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=5,
            time_scale=0.8, trans_time=0.3)
        brighton.facial(group=MAIN, index=400, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.0)


        # Реплика 410 · brighton · исходное время 198.6 с
        # Кроме всего прочего, мы подозреваем что СБА напрямую во всем этом замешано. И здесь нам пригодитесь вы.
        # Исходное окно facial: 8 с.
        t = 0
        t += 3.8
        brighton.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_GESTR_SELF_000LV_XA_03, duration=2.3,
            time_scale=0.2, trans_time=0.3)
        brighton.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_POINT_RGHT_CASL_000LV_XB_01, duration=2.3,
            time_scale=0.5)
        t += 2.5
        brighton.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=3, trans_time=1)
        brighton.facial(group=MAIN, index=410, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.0)


        # Реплика 420 · trent · исходное время 205.6 с
        # В качестве кого? Того, кто ткнет на кого-нибудь пальцем и скажет "он из СБА"? Звучит не очень
        # убедительно.
        # Исходное окно facial: 13 с.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=420, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-4.2)


        # Реплика 430 · kaitlyn · исходное время 214.4 с
        # Ахх...
        # Исходное окно facial: 0 с.
        t = 0
        voice_sound = self.lookup_single_sound(430)
        SoundEvent(root=self, group=MAIN, sound_name=voice_sound.get_nickname())
        t = 0
        cam_kaytlin.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_kaytlin_ik_not_interested_head',
            target_name='automarker_kaytlin_ik_not_interested_head_pos2', duration=1.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_kaytlin_ik_not_interested_eye',
            target_name='automarker_kaytlin_ik_not_interested_eye_pos2', duration=1, smooth=True)
        kaytlin.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRF_HOLD_HEAD_RLEASE_000LV_XA_03, duration=7,
            time_scale=0.5)
        kaytlin.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHEAD_MAD_COLD_000LV_XA_, duration=5, trans_time=0.5)
        t += 1.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_kaytlin_ik_not_interested_head',
            target_name='automarker_kaytlin_ik_not_interested_head_pos3', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_kaytlin_ik_not_interested_eye',
            target_name='automarker_kaytlin_ik_not_interested_eye_pos3', duration=1, smooth=True)
        main_group.append_time(2.5)


        # Реплика 435 · kaitlyn · исходное время 216.9 с
        # А пятьдесят тысяч звучат достаточно убедительно? Вы просто примите участие в заплыве, вам не обязательно
        # становиться победителем.
        # Исходное окно facial: 19 с.
        t = 0
        t += 5.0
        kaytlin.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRF_CONV_RHNDDN_TRNS_000LV_XA_02, duration=8,
            time_scale=0.3, trans_time=1)
        kaytlin.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHAND_HNEUT_GESTR_CASL_000LV_00, duration=10,
            time_scale=0.6)
        t += 7.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_kaytlin_front', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_kaytlin', duration=1.25, smooth=True)
        kaytlin.facial(group=MAIN, index=435, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-5.9)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M08OfferScene
