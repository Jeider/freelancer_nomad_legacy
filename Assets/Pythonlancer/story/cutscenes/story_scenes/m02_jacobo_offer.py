"""m02_jacobo_offer: постановка для ручного редактирования.

Точки: SCENES/m02_jacobo_offer.blend → DUMPS/m02_jacobo_offer.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — смещение внутри текущего блока; facial()/append_time() двигают часы.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    CameraAnimEvent,
    Character,
    ConnectHardpointEvent,
    EyeIkEvent,
    LookAtCamera,
    MAIN,
    MotionEvent,
    MoveEvent,
    NeckIkEvent,
    Prop,
    Sound,
)
from story.cutscenes.anim import (
    Male,
    Trent,
)
from story.cutscenes.source_extensions import (
    preserve_entity,
)
from story import actors


class PropSubtitlesPack2(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_pack2'
    SRT_GRP = 0
    USR_FLG = 0


class PropSubtitlesPack3(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_pack3'
    SRT_GRP = 0
    USR_FLG = 0


class PropSubtitlesM02Miner01(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_miner01'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Miner02(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_miner02'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Miner03(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_miner03'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Miner04(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_miner04'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Miner05(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_miner05'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Miner06(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_miner06'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Miner07(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_miner07'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Miner08(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_miner08'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Miner09(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_miner09'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Miner10(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_miner10'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Miner11(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_miner11'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Miner12(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_miner12'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Miner13(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_miner13'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Miner14(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_miner14'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Miner15(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_miner15'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Miner16(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_miner16'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Miner17(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_miner17'
    SRT_GRP = -1
    USR_FLG = 0


class ExtraCharBartenderFixture(actors.Actor):
    NAME = 'bartender_fixture'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'botzler'
    GAME_ACTOR = 'bartender'


class PropPropNotebook(Prop):
    COMPOUND_TEMPLATE_NAME = 'notebook'
    SRT_GRP = 0
    USR_FLG = 0



class M02JacoboOfferScene(Scene):
    DUMP_FILE = 'm02_jacobo_offer'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        sfx_ui_react_accept01 = Sound(root=self, name='sfx_ui_react_accept01', sound='sfx_ui_react_accept01',
            attenuation=-30, dmin=50, dmax=1000, priority=None)
        preserve_entity(sfx_ui_react_accept01, userprops={'category': 'Audio'})
        sfx_ui_react_accept02 = Sound(root=self, name='sfx_ui_react_accept02', sound='sfx_ui_react_accept02',
            attenuation=-30, dmin=50, dmax=1000, priority=None)
        preserve_entity(sfx_ui_react_accept02, userprops={'category': 'Audio'})
        sfx_ui_react_data01 = Sound(root=self, name='sfx_ui_react_data01', sound='sfx_ui_react_data01', attenuation=-20,
            dmin=50, dmax=1000, priority=None)
        preserve_entity(sfx_ui_react_data01, userprops={'category': 'Audio'})
        sfx_ui_react_denied01 = Sound(root=self, name='sfx_ui_react_denied01', sound='sfx_ui_react_denied01',
            attenuation=-30, dmin=50, dmax=1000, priority=None)
        preserve_entity(sfx_ui_react_denied01, userprops={'category': 'Audio'})
        sfx_keyboard_flurry01 = Sound(root=self, name='sfx_keyboard_flurry01', sound='sfx_keyboard_flurry01',
            attenuation=-30, dmin=50, dmax=1000, priority=None)
        preserve_entity(sfx_keyboard_flurry01, userprops={'category': 'Audio'})
        sfx_keyboard_flurry02 = Sound(root=self, name='sfx_keyboard_flurry02', sound='sfx_keyboard_flurry02',
            attenuation=-22, dmin=50, dmax=1000, priority=None)
        preserve_entity(sfx_keyboard_flurry02, userprops={'category': 'Audio'})
        sfx_keyboard_flurry03 = Sound(root=self, name='sfx_keyboard_flurry03', sound='sfx_keyboard_flurry03',
            attenuation=-15, dmin=50, dmax=1000, priority=None)
        preserve_entity(sfx_keyboard_flurry03, userprops={'category': 'Audio'})
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='Trent', userprops={'category': 'Character', 'actor': 'Player'})
        jacobo = Character(root=self, actor=actors.Jacobo, light_group=0, init_point='Char_jacobo', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(jacobo, template_name='jacobo', userprops={'category': 'Character', 'actor': 'jacobo'})
        bartender = Character(root=self, actor=actors.BartenderFixture, light_group=0, init_point='Char_bartender',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(bartender, template_name='botzler', userprops={'category': 'Character'})
        bartender_fixture = Character(root=self, actor=ExtraCharBartenderFixture, light_group=0,
            init_point='Char_bartender_fixture', rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(bartender_fixture, template_name='botzler',
            userprops={'category': 'Character', 'actor': 'bartender'})
        prop_notebook = PropPropNotebook(root=self, name='prop_notebook', light_group=0, init_point='prop_notebook',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(prop_notebook, userprops={'category': 'Prop'})
        cam_begin = LookAtCamera(root=self, name='cam_begin', fov=20, farplane=5000, look_duration=300)
        preserve_entity(cam_begin)
        cam_jacobo_eyes = LookAtCamera(root=self, name='cam_jacobo_eyes', fov=12, farplane=5000, look_duration=300)
        preserve_entity(cam_jacobo_eyes)
        cam_bartender_pointer = LookAtCamera(root=self, name='cam_bartender_pointer', fov=25, farplane=5000,
            look_duration=300)
        preserve_entity(cam_bartender_pointer)
        cam_jacobo_fingerprint = LookAtCamera(root=self, name='cam_jacobo_fingerprint', fov=15, farplane=5000,
            look_duration=300)
        preserve_entity(cam_jacobo_fingerprint)
        cam_trent_arrival = LookAtCamera(root=self, name='cam_trent_arrival', fov=35, farplane=5000, look_duration=300)
        preserve_entity(cam_trent_arrival)
        cam_trent_stand = LookAtCamera(root=self, name='cam_trent_stand', fov=25, farplane=5000, look_duration=300)
        preserve_entity(cam_trent_stand)
        cam_trent_stand_far = LookAtCamera(root=self, name='cam_trent_stand_far', fov=22, farplane=5000, look_duration=300)
        preserve_entity(cam_trent_stand_far)
        cam_walkout1 = LookAtCamera(root=self, name='cam_walkout1', fov=20, farplane=5000, look_duration=300)
        preserve_entity(cam_walkout1)
        cam_walkout2 = LookAtCamera(root=self, name='cam_walkout2', fov=20, farplane=5000, look_duration=300)
        preserve_entity(cam_walkout2)

        # Вход / начальная постановка.
        t = 0
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_NEUT_LEFT_000LV_A_00, duration=5)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_NEUT_RGHT_000LV_A_00, duration=5)
        cam_begin.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_begin', target_name='automarker_cam_begin_pos2',
            duration=10, smooth=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='prop_notebook', anim='Sc_open', duration=3,
            time_scale=0.5)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_jacobo', target_name='automarker_jacobo_head_ik',
            duration=851, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_jacobo', target_name='automarker_jacobo_eye_ik',
            duration=851, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=85, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_bartender', duration=0.0001, smooth=True)
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_SMALL_000LV_XA_07, duration=1.5)
        t += 1.5
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=1.7, trans_time=1)
        t += 1.7
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_SPCBODY_s020x_VanPelt_XC_CHRF_TYPE_000DN_06, duration=10,
            loop=True, trans_time=0.5)
        t += 0.3
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_GESTL_TYPING_000LV_XB, duration=7.474, loop=True,
            trans_time=0.5)
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_GESTR_TYPING_000LV_XB, duration=7.459, loop=True,
            trans_time=0.5)
        t += 0.5
        sfx_keyboard_flurry02.start(group=MAIN, time_delay=t, duration=9, loop=True)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_begin_focus',
            target_name='automarker_cam_begin_point2', duration=5, smooth=True)
        t += 5
        cam_jacobo_eyes.set(group=MAIN, time_delay=t)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_eye_ik',
            target_name='automarker_head_trent_far', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_head_ik',
            target_name='automarker_head_trent_far', duration=4, smooth=True)
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_MAD_COLD_000LV_XA_, duration=10, time_scale=0.8,
            trans_time=0.25)
        t += 3
        cam_bartender_pointer.set(group=MAIN, time_delay=t)
        CameraAnimEvent(root=self, group=MAIN, time_delay=t, camera_name='cam_bartender_pointer', duration=5, fov=10,
            smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.GENERIC_ANIM, duration=10, time_scale=0.6, trans_time=0.25)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_HNDS_CASL_000LV_xa_04, duration=2,
            time_scale=0.6)
        bartender.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_000DN_A_29, duration=6)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_eye_ik',
            target_name='automarker_notebook_screen', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_head_ik',
            target_name='automarker_notebook_screen', duration=2, smooth=True)
        t += 1
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_HNDSDN_TRNS_000LV_XA_01, duration=5,
            time_scale=0.6, trans_time=1)
        bartender.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_POINT_RHND_270LV_A_03, duration=6,
            time_scale=0.6, trans_time=1)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_jacobo', duration=4, smooth=True)
        bartender.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_POINT_RGHT_CASL_000LV_00, duration=4,
            time_scale=2, trans_time=0.25)
        t += 1
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_TURN_045LV_XA_04, duration=4, trans_time=1)
        t += 1
        trent.motion(group=MAIN, time_delay=t, anim=Trent.Sc_MLHEAD_HAPPY_SMILE_SNEER_TRENT_000LV_XA_, duration=10,
            trans_time=0.25)
        t += 1.6
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01, duration=1.4, time_scale=0.7,
            trans_time=1)
        t += 1.4
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent',
            target_name='automarker_point_trent_arriving', duration=1e-05, smooth=False)
        cam_trent_arrival.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_trent_arrival',
            target_name='automarker_cam_trent_arrival_pos2', duration=5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_trent_arrival_focus',
            target_name='automarker_cam_trent_arrival_point2', duration=5, smooth=True)
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_SPCBODY_s020x_VanPelt_XC_CHRF_TYPE_000DN_06, duration=14,
            loop=True)
        sfx_keyboard_flurry01.start(group=MAIN, time_delay=t, duration=14, loop=True)
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_GESTL_TYPING_000LV_XB, duration=14, loop=True,
            trans_time=0.5)
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_GESTR_TYPING_000LV_XB, duration=14, loop=True,
            trans_time=0.5)
        t += 2
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XC_03, duration=5, time_scale=0.6)
        main_group.append_time(27)


        # Реплика 10 · trent · исходное время 27 с
        # Приветствую!
        # Исходное окно facial: 4 с.
        t = 0
        trent.facial(group=MAIN, index=10, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-3)


        # Реплика 20 · jacobo · исходное время 28 с
        # Симметрично. Чему обязан?
        # Исходное окно facial: 3 с.
        t = 0
        t += 0.5
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_000DN_A_29, duration=20, time_scale=0.6, loop=True,
            trans_time=1)
        jacobo.facial(group=MAIN, index=20, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(1)


        # Реплика 30 · trent · исходное время 32 с
        # Вильгельму вы обязаны.
        # Исходное окно facial: 4 с.
        t = 0
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_NEUT_LEFT_000LV_A_00, duration=5)
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_NEUT_RGHT_000LV_A_00, duration=5)
        cam_trent_stand.set(group=MAIN, time_delay=t)
        t += 3
        cam_jacobo_fingerprint.set(group=MAIN, time_delay=t)
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_MAD_COLD_000LV_XA_, duration=10, trans_time=0.25)
        trent.facial(group=MAIN, index=30, append=True, auto_lip=True, extra_delay=0)
        t = 0
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_eye_ik',
            target_name='automarker_jacobo_front_left', duration=1, smooth=True)
        main_group.append_time(1)


        # Реплика 40 · jacobo · исходное время 37 с
        # Что есть -то есть.
        # Исходное окно facial: 3 с.
        t = 0
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_IDLE_SMALL_000LV_XA_05, duration=14, loop=True,
            trans_time=1)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_NEUT_LEFT_000LV_A_00, duration=5)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_NEUT_RGHT_000LV_A_00, duration=5)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_head_ik',
            target_name='automarker_jacobo_front', duration=1, smooth=True)
        jacobo.facial(group=MAIN, index=40, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1)


        # Реплика 45 · jacobo · исходное время 39 с
        # И что же на этот раз понадобилось герру Вильгельму?
        # Исходное окно facial: 10 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_eye_ik',
            target_name='automarker_head_trent', duration=1.25, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_head_ik',
            target_name='automarker_head_trent_btm', duration=3, smooth=True)
        jacobo.facial(group=MAIN, index=45, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-6)


        # Реплика 50 · trent · исходное время 43 с
        # Координаты одного разбившегося корабля.
        # Исходное окно facial: 10 с.
        t = 0
        cam_trent_stand.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=50, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-6)


        # Реплика 60 · jacobo · исходное время 47 с
        # А! Это проще простого. Я сейчас скину вам все точки происшествий с повреждением судов за прошедший месяц.
        # Точность позиционирования плюс-минус двадцать миллиметров. Выбирайте что вам нужно, фильтруйте по
        # критериям, спасибо говорить не нужно.
        # Исходное окно facial: 20 с.
        t = 0
        cam_jacobo_fingerprint.set(group=MAIN, time_delay=t)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_eye_ik',
            target_name='automarker_notebook_screen', duration=1.25, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_head_ik',
            target_name='automarker_notebook_screen', duration=2, smooth=True)
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_SPCBODY_s020x_VanPelt_XC_CHRF_TYPE_000DN_06, duration=6,
            loop=True, trans_time=1)
        sfx_keyboard_flurry03.start(group=MAIN, time_delay=t, duration=6, loop=True)
        t += 2
        sfx_ui_react_accept01.start(group=MAIN, time_delay=t, duration=2)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_eye_ik',
            target_name='automarker_notebook_screen_left', duration=0.5, smooth=True)
        t += 0.5
        sfx_ui_react_accept02.start(group=MAIN, time_delay=t, duration=2)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_eye_ik',
            target_name='automarker_notebook_screen_right', duration=0.5, smooth=True)
        sfx_ui_react_accept02.start(group=MAIN, time_delay=t, duration=2)
        t += 0.5
        sfx_ui_react_accept02.start(group=MAIN, time_delay=t, duration=2)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_eye_ik',
            target_name='automarker_notebook_screen', duration=0.5, smooth=True)
        t += 1
        sfx_ui_react_data01.start(group=MAIN, time_delay=t, duration=2)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_eye_ik',
            target_name='automarker_head_trent', duration=1.25, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_head_ik',
            target_name='automarker_head_trent_btm', duration=2, smooth=True)
        t += 1
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDUP_TRNS_000LV_XA_02, duration=2,
            time_scale=0.5, trans_time=1)
        t += 1
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_RHND_CASL_000LV_XC_01, duration=2,
            time_scale=0.5, trans_time=1)
        t += 1
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDDN_TRNS_000LV_XA_02, duration=2,
            time_scale=0.5, trans_time=1)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_eye_ik',
            target_name='automarker_notebook_screen', duration=1.25, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_head_ik',
            target_name='automarker_notebook_screen', duration=2, smooth=True)
        t += 1
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_SPCBODY_s020x_VanPelt_XC_CHRF_TYPE_000DN_06, duration=7,
            loop=True, trans_time=1)
        sfx_keyboard_flurry01.start(group=MAIN, time_delay=t, duration=6, loop=True)
        jacobo.facial(group=MAIN, index=60, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-4)


        # Реплика 70 · trent · исходное время 63 с
        # Мы вместе полетим.
        # Исходное окно facial: 4 с.
        t = 0
        cam_trent_stand.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_SMALL_000LV_xa_05, duration=5, time_scale=0.6)
        t += 3
        cam_jacobo_fingerprint.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=70, append=True, auto_lip=True, extra_delay=0)
        t = 0


        # Реплика 80 · jacobo · исходное время 67 с
        # Это зачем еще?
        # Исходное окно facial: 5 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_eye_ik',
            target_name='automarker_head_trent_btm', duration=1.25, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_head_ik',
            target_name='automarker_jacobo_front', duration=1.5, smooth=True)
        t += 1
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_IDLE_SMALL_000LV_XA_05, duration=5, loop=True,
            trans_time=1)
        jacobo.facial(group=MAIN, index=80, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2)


        # Реплика 90 · trent · исходное время 70 с
        # Вильгельм сказал, ты должен мне указать на место интересующего нас события, а я должен его найти. А как я
        # могу быть уверен, что ты не слил мне туфту, чтобы через полчаса свалить в закат? У военных свои причуды,
        # а у фриленсеров - свои.
        # Исходное окно facial: 12.5 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_jacobo', duration=0.0001, smooth=True)
        cam_trent_stand_far.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_trent_stand_far',
            target_name='automarker_cam_trent_stand_far_pos2', duration=13, smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=2)
        t += 1
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_eye_ik',
            duration=22, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_HOLD_000LV_XA_02, duration=4, loop=True,
            trans_time=1)
        t += 4
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=2, trans_time=1)
        t += 1.5
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_GESTR_THUMB_000LV_00, duration=2)
        t += 1.0
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_GESTR_180LV_XA_02, duration=5)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_jacobo_outside_half', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_jacobo_outside', duration=1, smooth=True)
        t += 1.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_jacobo', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_jacobo', duration=1, smooth=True)
        t += 0.5
        bartender.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_000DN_A_29, duration=6, trans_time=1)
        t += 1
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_GESTR_THUMB_000LV_00, duration=5, start_time=2)
        trent.facial(group=MAIN, index=90, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(0.5)


        # Реплика 100 · jacobo · исходное время 83 с
        # Сотню раз уже проклял тот день когда согласился Вильгельму помогать.
        # Исходное окно facial: 5 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_head_ik',
            target_name='automarker_notebook_screen', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_eye_ik',
            target_name='automarker_notebook_screen_left', duration=1, smooth=True)
        cam_jacobo_fingerprint.set(group=MAIN, time_delay=t)
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=2)
        t += 1
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='prop_notebook', anim='Sc_close', duration=3)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_head_ik',
            target_name='automarker_head_jacobo_standing', duration=2.9, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_eye_ik',
            target_name='automarker_head_jacobo_standing', duration=1, smooth=True)
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_STNDCR_TRNS_090LV_XA_05, duration=6)
        t += 2
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=10, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_eye_ik',
            duration=10, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_jacobo_final_init', duration=0.0001, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_jacobo_final_init', duration=0.0001, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', target_name='automarker_point_trent_final',
            duration=1e-05, smooth=False)
        jacobo.facial(group=MAIN, index=100, append=True, auto_lip=True, extra_delay=0)
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_jacobo_final_done', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_jacobo_final_done', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_head_ik',
            target_name='automarker_head_trent_final_half', duration=0.1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_eye_ik',
            target_name='automarker_head_trent_final', duration=0.1, smooth=True)
        cam_walkout1.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_walkout1',
            target_name='automarker_cam_walkout1_pos2', duration=5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_walkout1_focus',
            target_name='automarker_cam_walkout1_point2', duration=5, smooth=True)
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='prop_notebook', parent_name='Char_jacobo',
            duration=28, target_hardpoint='HpHandConnect', parent_hardpoint='HpLeftConnect')
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_NEUT_WALK_LEFT_000LV_XA_, duration=1, time_scale=2)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='prop_notebook', anim='Sc_close', duration=1,
            time_scale=5)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_jacobo',
            target_name='automarker_point_jacobo_final', duration=1e-05, smooth=False)
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=3)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_000DN_A_29, duration=1)
        t += 1
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_TURN_270LV_XA_04, duration=3, trans_time=1)
        main_group.append_time(1.5)


        # Реплика 110 · jacobo · исходное время 89.5 с
        # Сам-то он где сейчас? Сидит в баре на ближайшем торговом посту?
        # Исходное окно facial: 5 с.
        t = 0
        t += 1.0
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, duration=3,
            trans_time=1.5)
        t += 1.0
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_RHND_CASL_000LV_xa_01, duration=2, loop=True,
            trans_time=1.5)
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00, duration=4, time_scale=0.75,
            trans_time=0.25)
        t += 0.5
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_000DN_A_29, duration=4, time_scale=0.6, loop=True,
            trans_time=1)
        t += 1.5
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_02, duration=3,
            trans_time=1.5)
        jacobo.facial(group=MAIN, index=110, append=True, auto_lip=True, extra_delay=0)
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_trent_final_front', duration=4, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_trent_final_front', duration=4, smooth=True)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_head_ik',
            target_name='automarker_jacobo_final_front', duration=4, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_eye_ik',
            target_name='automarker_jacobo_final_front', duration=2, smooth=True)
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XC_02, duration=2, time_scale=1.5)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WALK_TRNS_270LV_XA_02, duration=6, trans_time=1)
        main_group.append_time(2.0)


        # Реплика 120 · jacobo · исходное время 96.5 с
        # Что бы ни случилось, он тут не при чем окажется, а вот мы с тобой главные фигуранты.
        # Исходное окно facial: 5 с.
        t = 0
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_GEST_RHND_TLKING_000LV_XB_02, duration=18,
            time_scale=0.8, loop=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=30, time_scale=0.8, loop=True)
        cam_walkout2.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_walkout2',
            target_name='automarker_cam_walkout2_pos2', duration=5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_walkout2_focus',
            target_name='automarker_cam_walkout2_point2', duration=5, smooth=True)
        jacobo.facial(group=MAIN, index=120, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(2.5)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M02JacoboOfferScene
