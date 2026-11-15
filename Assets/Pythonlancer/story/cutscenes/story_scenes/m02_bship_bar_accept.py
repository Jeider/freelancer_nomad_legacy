"""m02_bship_bar_accept: постановка для ручного редактирования.

Точки: SCENES/m02_bship_bar_accept.blend → DUMPS/m02_bship_bar_accept.json.
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
    SoundEvent,
)
from story.cutscenes.anim import (
    Male,
)
from story.cutscenes.source_extensions import (
    preserve_entity,
)
from story import actors


class PropSubtitlesPack2(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_pack2'
    SRT_GRP = 0
    USR_FLG = 0


class PropSubtitlesM02Offer33(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer33'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer34(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer34'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer35(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer35'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer36(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer36'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer37(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer37'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer38(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer38'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer39(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer39'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer40(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer40'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer41(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer41'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer42(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer42'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer43(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer43'
    SRT_GRP = -1
    USR_FLG = 0



class M02BshipBarAcceptScene(Scene):
    DUMP_FILE = 'm02_bship_bar_accept'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='Trent', userprops={'category': 'Character', 'actor': 'Player'})
        wilham = Character(root=self, actor=actors.Wilham, light_group=0, init_point='Char_wilham', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(wilham, template_name='wilham', userprops={'category': 'Character', 'actor': 'wilham'})
        cam_trent_near = LookAtCamera(root=self, name='cam_trent_near', fov=25, farplane=5000, look_duration=300)
        preserve_entity(cam_trent_near)
        cam_wilham_near = LookAtCamera(root=self, name='cam_wilham_near', fov=25, farplane=5000, look_duration=300)
        preserve_entity(cam_wilham_near)
        cam_trent_standing = LookAtCamera(root=self, name='cam_trent_standing', fov=25, farplane=5000, look_duration=300)
        preserve_entity(cam_trent_standing)
        cam_wilham_stand = LookAtCamera(root=self, name='cam_wilham_stand', fov=22, farplane=5000, look_duration=300)
        preserve_entity(cam_wilham_stand)
        cam_final = LookAtCamera(root=self, name='cam_final', fov=25, farplane=5000, look_duration=300)
        preserve_entity(cam_final)

        # Вход / начальная постановка.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_SMALL_000LV_XA_07, duration=3)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_SMALL_000LV_XA_07, duration=5)
        main_group.append_time(0.5)


        # Реплика 200 · trent · исходное время 0.5 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m02_offer_0200_trent
        # Исходное окно facial: 6 с.
        # trent.facial(group=MAIN, index=200, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(6.0)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-3.0)


        # Реплика 210 · wilham · исходное время 3.5 с
        # Не "могу", а "можем", герр Трент. В этом задании я буду приписан к вам в качестве напарника.
        # Исходное окно facial: 7 с.
        t = 0
        cam_wilham_near.set(group=MAIN, time_delay=t)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=3)
        t += 2.0
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_SMALL_000LV_XA_07, duration=3, trans_time=1)
        t += 3.0
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_STNDCR_TRNS_090LV_XA_05, duration=2.5, trans_time=1)
        t += 1.5
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=22, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        wilham.facial(group=MAIN, index=210, append=True, auto_lip=True, extra_delay=0)
        t = 0
        t += 0.5
        cam_trent_standing.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_trent_standing',
            target_name='automarker_cam_trent_standing_pos2', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_trent_standing_focus',
            target_name='automarker_cam_trent_standing_point2', duration=4, smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_STNDCL_TRNS_270LV_XA_06, duration=5, start_time=1)
        main_group.append_time(1.0)


        # Реплика 220 · trent · исходное время 11.5 с
        # Будете контролировать мои действия?
        # Исходное окно facial: 6 с.
        t = 0
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_wilham_stand_progress', duration=3, smooth=True)
        t += 1.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_wilham',
            target_name='automarker_point_wilham_stand', duration=1e-05, smooth=False)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_wilham', target_name='automarker_wilham_head_ik',
            duration=30, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_head_ik',
            target_name='automarker_head_trent_stand_lower', duration=0.1, smooth=True)
        trent.facial(group=MAIN, index=220, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-3.5)


        # Реплика 230 · wilham · исходное время 14 с
        # Нет. Буду осуществлять поддержку и взаимодействие с властями. Стратегия операции и тактика её проведения
        # целиком на вас, герр Трент.
        # Исходное окно facial: 13 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_head_ik',
            target_name='automarker_head_trent_stand', duration=3, smooth=True)
        cam_wilham_stand.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_wilham_stand',
            target_name='automarker_cam_wilham_stand_pos2', duration=11, smooth=True)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_GESTL_STOP_000LV_XA_03, duration=5, start_time=0.5)
        t += 3
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, duration=3,
            trans_time=1.5)
        t += 1
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_RHND_CASL_000LV_xa_01, duration=2, loop=True,
            trans_time=1.5)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00, duration=4, time_scale=0.75,
            trans_time=0.25)
        t += 2
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_02, duration=3,
            trans_time=1.5)
        t += 2.5
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_GESTR_THMBSUP_000LV_XA_02, duration=5,
            time_scale=0.6)
        t += 0.5
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_POINT_RGHT_CASL_000LV_00, duration=4,
            time_scale=1.5, start_time=3, trans_time=0.5)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', target_name='automarker_point_trent_stand',
            duration=1e-05, smooth=False)
        t += 0.5
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_SMALL_000LV_xa_05, duration=0.5)
        t += 0.5
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=30, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_wilham_stand', duration=1, smooth=True)
        t += 1
        cam_final.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_NOD_YES_EMPH_000LV_XA_01, duration=5)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_SMALL_000LV_xa_05, duration=4)
        # Duplicate source sound event 43, same timestamp.
        SoundEvent(root=self, group=MAIN, sound_name=self.lookup_single_sound(230).get_nickname())
        wilham.facial(group=MAIN, index=230, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.5)


        # Реплика 240 · trent · исходное время 26.5 с
        # Спасибо за доверие... где поставить подпись?
        # Исходное окно facial: 6 с.
        t = 0
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_final', target_name='automarker_cam_final_pos2',
            duration=6, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_final_focus',
            target_name='automarker_cam_final_point2', duration=6, smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_SHRG_SHLDRS_SMALL_000LV_XA_01, duration=5,
            trans_time=1)
        trent.facial(group=MAIN, index=240, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.5)


        # Реплика 250 · wilham · исходное время 30 с
        # Ха-ха-ха. Ну зачем нам эти условности? Встречаемся в космосе, герр Трент!
        # Исходное окно facial: 6 с.
        t = 0
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_GESTL_STOP_000LV_XA_03, duration=5, trans_time=1)
        t += 3
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_final', target_name='automarker_cam_final_pos3',
            duration=6, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_final_focus',
            target_name='automarker_cam_final_point3', duration=6, smooth=True)
        t += 1
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01, duration=5, trans_time=1)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_head_ik',
            target_name='automarker_wilham_outdoor', duration=4, smooth=True)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='Char_wilham', duration=5,
            transition_duration=1, target_type='HARDPOINT', target_part='hp_neck', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 1
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=50, loop=True,
            trans_time=0.25)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_TURN_270LV_XA_04, duration=10, trans_time=1)
        wilham.facial(group=MAIN, index=250, append=True, auto_lip=True, extra_delay=0)
        t = 0
        t += 2
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=10,
            trans_time=1)
        main_group.append_time(4.5)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M02BshipBarAcceptScene
