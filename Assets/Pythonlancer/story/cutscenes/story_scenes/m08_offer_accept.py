"""m08_offer_accept: постановка для ручного редактирования.

Точки: SCENES/m08_offer_accept.blend → DUMPS/m08_offer_accept.json.
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



class M08OfferAcceptScene(Scene):
    DUMP_FILE = 'm08_offer_accept'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
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


        # Реплика 440 · trent · исходное время 0 с
        # Олимпийский принцип? За пятьдесят тысяч? Возможно, я сильно поторопился, сказав, что в секторе Сириуса
        # нет британской короны.
        # Исходное окно facial: 10.5 с.
        t = 0
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, duration=10)
        kaytlin.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRF_IDLE_000LV_XA_05, duration=10)
        brighton.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=100, time_scale=0.6,
            loop=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=100, time_scale=0.6,
            loop=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_kaytlin_ik_not_interested_head',
            target_name='automarker_kaytlin_ik_not_interested_head_pos3', duration=0, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_kaytlin_ik_not_interested_eye',
            target_name='automarker_kaytlin_ik_not_interested_eye_pos3', duration=0, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_darcy_head_ik',
            target_name='automarker_head_trent_front', duration=0, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_darcy_eye_ik',
            target_name='automarker_head_trent', duration=0, smooth=True)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_darcy', target_name='automarker_darcy_head_ik',
            duration=2555, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_darcy', target_name='automarker_darcy_eye_ik',
            duration=2555, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_brighton',
            target_name='automarker_brighton_head_ik', duration=2555, transition_duration=1, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_brighton', target_name='automarker_brighton_eye_ik',
            duration=2555, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=555, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_eye_ik',
            duration=555, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_kaitlyn',
            target_name='automarker_kaytlin_ik_not_interested_head', duration=1000, transition_duration=2,
            target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_kaitlyn',
            target_name='automarker_kaytlin_ik_not_interested_eye', duration=1000, transition_duration=2,
            target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_kaytlin_front', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_kaytlin', duration=1.25, smooth=True)
        cam_trent_sit.set(group=MAIN, time_delay=t)
        t += 0.01
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_darcy', angle=-25, axis='Y_AXIS', duration=0,
            smooth=False)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_kaitlyn', angle=-125, axis='Y_AXIS',
            duration=0, smooth=False)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_brighton', angle=10, axis='Y_AXIS',
            duration=0, smooth=False)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=20, axis='Y_AXIS', duration=0,
            smooth=False)
        trent.facial(group=MAIN, index=440, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.5)


        # Реплика 450 · kaitlyn · исходное время 10 с
        # И были достаточно умны, чтобы это признать. Непосредственное руководство миссией возложено на адмирала
        # Брайтона, все детали обсудите с ним...
        # Исходное окно facial: 20 с.
        t = 0
        cam_kaytlin.set(group=MAIN, time_delay=t)
        t += 2
        kaytlin.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=100,
            time_scale=0.3, trans_time=1)
        t += 6
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_brighton_head_ik',
            target_name='automarker_head_kaytlin_front_fwd2', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_brighton_eye_ik',
            target_name='automarker_head_kaytlin_lwr', duration=1.5, smooth=True)
        t += 3.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_kaytlin_ik_not_interested_head',
            target_name='automarker_head_brighton_front_fwd', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_kaytlin_ik_not_interested_eye',
            target_name='automarker_head_brighton_front_lwr', duration=1.5, smooth=True)
        kaytlin.facial(group=MAIN, index=450, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-7.6)


        # Реплика 460 · kaitlyn · исходное время 22.4 с
        # Джентльмены...
        # Исходное окно facial: 12 с.
        t = 0
        t += 2.6
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_brighton_head_ik',
            target_name='automarker_head_trent_brightonside_front', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_brighton_eye_ik',
            target_name='automarker_head_trent_brightonside', duration=1.25, smooth=True)
        kaytlin.facial(group=MAIN, index=460, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-8.9)


        # Реплика 470 · brighton · исходное время 25.5 с
        # Мистер Трент, на орбите планеты находится Принц Уэльский, мой линкор. Стыкуйтесь к нему, все необходимые
        # допуски и разрешения я вам выдам.
        # Исходное окно facial: 8 с.
        t = 0
        cam_brighton.set(group=MAIN, time_delay=t)
        brighton.facial(group=MAIN, index=470, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.2)


        # Реплика 480 · darcy · исходное время 33.3 с
        # Трент, увидимся на Принце Уэльском.
        # Исходное окно facial: 9 с.
        t = 0
        cam_darcy_sit.set(group=MAIN, time_delay=t)
        t += 3.0
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_STNDCR_TRNS_090LV_XA_04, duration=4,
            time_scale=0.5, trans_time=1)
        t += 0.3
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_darcy_head_ik',
            target_name='automarker_head_trent_side_darcyout', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_darcy_eye_ik',
            target_name='automarker_head_trent_side_darcyout', duration=1.5, smooth=True)
        darcy.facial(group=MAIN, index=480, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-4.7)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M08OfferAcceptScene
