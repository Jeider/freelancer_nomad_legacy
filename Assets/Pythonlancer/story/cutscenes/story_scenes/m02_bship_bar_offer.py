"""m02_bship_bar_offer: постановка для ручного редактирования.

Точки: SCENES/m02_bship_bar_offer.blend → DUMPS/m02_bship_bar_offer.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — смещение внутри текущего блока; facial()/append_time() двигают часы.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Alchemy,
    Character,
    ConnectHardpointEvent,
    EyeIkEvent,
    LookAtCamera,
    MAIN,
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
    SourceAttachEvent,
    preserve_entity,
    preserve_spatial,
)
from story import actors


class PropPropCigarette2(Prop):
    COMPOUND_TEMPLATE_NAME = 'cigarette_2'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropAshtrayExtra1(Prop):
    COMPOUND_TEMPLATE_NAME = 'ashtray_2'
    SRT_GRP = 0
    USR_FLG = 0


class PropSubtitlesPack2(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_pack2'
    SRT_GRP = 0
    USR_FLG = 0


class PropSubtitlesM02Offer01(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer01'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer02(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer02'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer03(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer03'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer04(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer04'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer05(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer05'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer06(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer06'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer07(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer07'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer08(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer08'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer09(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer09'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer10(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer10'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer11(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer11'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer12(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer12'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer13(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer13'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer14(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer14'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer15(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer15'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer16(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer16'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer17(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer17'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer18(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer18'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer19(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer19'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer20(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer20'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer21(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer21'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer22(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer22'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer23(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer23'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer24(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer24'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer25(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer25'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer26(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer26'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer27(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer27'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer28(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer28'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer29(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer29'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer30(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer30'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer31(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer31'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Offer32(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer32'
    SRT_GRP = -1
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


class PropSubtitlesM02Offer44(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_offer44'
    SRT_GRP = -1
    USR_FLG = 0


class PropPropPda(Prop):
    COMPOUND_TEMPLATE_NAME = 'pda'
    SRT_GRP = 0
    USR_FLG = 0



class M02BshipBarOfferScene(Scene):
    DUMP_FILE = 'm02_bship_bar_offer'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        vfx_rtc_sydsmoke_3 = Alchemy(root=self, name='vfx_rtc_sydsmoke_3', particles='rtc_sydsmoke',
            point_name='vfx_rtc_sydsmoke_3', sparam=0)
        preserve_entity(vfx_rtc_sydsmoke_3, flags='LIT_DYNAMIC+LIT_AMBIENT')
        vfx_rtc_cigaretteglow_4 = Alchemy(root=self, name='vfx_rtc_cigaretteglow_4', particles='rtc_cigaretteglow',
            point_name='vfx_rtc_cigaretteglow_4', sparam=0)
        preserve_entity(vfx_rtc_cigaretteglow_4, flags='LIT_DYNAMIC+LIT_AMBIENT')
        prop_cigarette_2 = PropPropCigarette2(root=self, name='prop_cigarette_2', light_group=0,
            init_point='prop_cigarette_2', rotate_from_quat=True, use_ambient=True)
        preserve_entity(prop_cigarette_2, userprops={'category': 'Prop'})
        Prop_ashtray_extra_1 = PropPropAshtrayExtra1(root=self, name='Prop_ashtray_extra_1', light_group=0,
            init_point='Prop_ashtray_extra_1', rotate_from_quat=True, use_ambient=False)
        preserve_entity(Prop_ashtray_extra_1, userprops={'category': 'Prop', 'Priority': 'Room_Prop_1'})
        DX_m02_offer_0200_trent = Sound(root=self, name='DX_m02_offer_0200_trent', sound='DX_m02_offer_0200_trent',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m02_offer_0200_trent, userprops={'category': 'Audio'})
        DX_m02_offer_0210_wilham = Sound(root=self, name='DX_m02_offer_0210_wilham', sound='DX_m02_offer_0210_wilham',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m02_offer_0210_wilham, userprops={'category': 'Audio'})
        DX_m02_offer_0220_trent = Sound(root=self, name='DX_m02_offer_0220_trent', sound='DX_m02_offer_0220_trent',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m02_offer_0220_trent, userprops={'category': 'Audio'})
        DX_m02_offer_0230_wilham = Sound(root=self, name='DX_m02_offer_0230_wilham', sound='DX_m02_offer_0230_wilham',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m02_offer_0230_wilham, userprops={'category': 'Audio'})
        DX_m02_offer_0240_trent = Sound(root=self, name='DX_m02_offer_0240_trent', sound='DX_m02_offer_0240_trent',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m02_offer_0240_trent, userprops={'category': 'Audio'})
        DX_m02_offer_0250_wilham = Sound(root=self, name='DX_m02_offer_0250_wilham', sound='DX_m02_offer_0250_wilham',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m02_offer_0250_wilham, userprops={'category': 'Audio'})
        Prop_pda = PropPropPda(root=self, name='Prop_pda', light_group=0, init_point='Prop_pda', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(Prop_pda, userprops={'category': 'Prop'})
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='Trent', userprops={'category': 'Character', 'actor': 'Player'})
        wilham = Character(root=self, actor=actors.Wilham, light_group=0, init_point='Char_wilham', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(wilham, template_name='wilham', userprops={'category': 'Character', 'actor': 'wilham'})
        cam_start = LookAtCamera(root=self, name='cam_start', fov=35, farplane=5000, look_duration=300)
        preserve_entity(cam_start)
        cam_wilham_top = LookAtCamera(root=self, name='cam_wilham_top', fov=25, farplane=5000, look_duration=300)
        preserve_entity(cam_wilham_top)
        cam_trent_stand = LookAtCamera(root=self, name='cam_trent_stand', fov=20, farplane=5000, look_duration=300)
        preserve_entity(cam_trent_stand)
        cam_trent_top = LookAtCamera(root=self, name='cam_trent_top', fov=25, farplane=5000, look_duration=300)
        preserve_entity(cam_trent_top)
        cam_wilham_far = LookAtCamera(root=self, name='cam_wilham_far', fov=30, farplane=5000, look_duration=300)
        preserve_entity(cam_wilham_far)
        cam_sitting = LookAtCamera(root=self, name='cam_sitting', fov=30, farplane=5000, look_duration=300)
        preserve_entity(cam_sitting)
        cam_trent_near = LookAtCamera(root=self, name='cam_trent_near', fov=25, farplane=5000, look_duration=300)
        preserve_entity(cam_trent_near)
        cam_wilham_near = LookAtCamera(root=self, name='cam_wilham_near', fov=25, farplane=5000, look_duration=300)
        preserve_entity(cam_wilham_near)
        cam_trent_closest = LookAtCamera(root=self, name='cam_trent_closest', fov=20, farplane=5000, look_duration=300)
        preserve_entity(cam_trent_closest)
        cam_msn_begins = LookAtCamera(root=self, name='cam_msn_begins', fov=35, farplane=5000, look_duration=300)
        preserve_entity(cam_msn_begins)
        cam_wilham_msn1 = LookAtCamera(root=self, name='cam_wilham_msn1', fov=25, farplane=5000, look_duration=300)
        preserve_entity(cam_wilham_msn1)
        cam_wilham_middle = LookAtCamera(root=self, name='cam_wilham_middle', fov=25, farplane=5000, look_duration=300)
        preserve_entity(cam_wilham_middle)
        cam_wilham_msn2 = LookAtCamera(root=self, name='cam_wilham_msn2', fov=25, farplane=5000, look_duration=300)
        preserve_entity(cam_wilham_msn2)
        cam_wilham_msn3 = LookAtCamera(root=self, name='cam_wilham_msn3', fov=25, farplane=5000, look_duration=300)
        preserve_entity(cam_wilham_msn3)

        # Вход / начальная постановка.
        t = 0
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['vfx_rtc_sydsmoke_3', 'prop_cigarette_2'],
            duration=70, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='hp_cigarette_tip_smoke',
            target_type='HARDPOINT', flags='POSITION')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['vfx_rtc_cigaretteglow_4', 'prop_cigarette_2'],
            duration=70, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='hp_cigarette_tip_smoke',
            target_type='HARDPOINT', flags='POSITION+ORIENTATION')
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=30, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_eye_ik',
            duration=30, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_wilham', target_name='automarker_wilham_head_ik',
            duration=33, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_wilham', target_name='automarker_wilham_eye_ik',
            duration=33, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        cam_start.set(group=MAIN, time_delay=t)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_SMALL_000LV_XA_07, duration=4, loop=True)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_start_focus',
            target_name='automarker_cam_start_point2', duration=7, smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=5, time_scale=0.75,
            start_time=0.25)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_head_trent_stand', duration=2, smooth=True)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_head_ik',
            target_name='automarker_head_trent_stand', duration=2, smooth=True)
        main_group.append_time(3)


        # Реплика 10 · trent · исходное время 3 с
        # Вильгельм, полагаю?
        # Исходное окно facial: 6 с.
        t = 0
        trent.facial(group=MAIN, index=10, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-4.5)


        # Реплика 20 · wilham · исходное время 4.5 с
        # Так точно, герр Трент. Я рад, что вы согласились с нами работать.
        # Исходное окно facial: 6.8 с.
        t = 0
        t += 0.5
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_XB_04, duration=5, trans_time=2)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_TALK_000UP_A_17, duration=14, loop=True,
            trans_time=2)
        t += 3.0
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_XB_04, duration=2)
        wilham.facial(group=MAIN, index=20, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.8)


        # Реплика 30 · trent · исходное время 8.5 с
        # Еще не согласился, но определенно заинтересовался.
        # Исходное окно facial: 19.5 с.
        t = 0
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_start', target_name='automarker_cam_start_pos2',
            duration=11, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_start_focus',
            target_name='automarker_cam_start_point3', duration=11, smooth=True)
        t += 1.0
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, duration=6, time_scale=0.5,
            trans_time=1)
        t += 9.0
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, duration=5, time_scale=0.8,
            trans_time=1)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_wilham_front', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_head_ik',
            target_name='automarker_head_trent_stand_half', duration=2, smooth=True)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_MAD_COLD_000LV_XA_, duration=4, trans_time=0.25)
        t += 1.5
        trent.motion(group=MAIN, time_delay=t, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, duration=5, trans_time=1)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_head_trent_stand', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_head_ik',
            target_name='automarker_head_trent_stand', duration=2, smooth=True)
        cam_wilham_top.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=30, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-6.0)


        # Реплика 40 · wilham · исходное время 22 с
        # Тогда присаживайтесь, я введу вас в курс дела. Только давайте договоримся, что вне зависимости от того
        # чем закончится наш разговор, все его детали должны остаться между нами. Хорошо?
        # Исходное окно facial: 4 с.
        t = 0
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_GESTL_WHAT_000LV_XA_03, duration=6, time_scale=0.6,
            trans_time=1)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_pda_in_hands_half', duration=0.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_pda_in_hands', duration=0.75, smooth=True)
        t += 1
        cam_trent_stand.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_DEALR_PDA_000LV_XA_09, duration=5, time_scale=0.5,
            start_time=6)
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='Prop_pda', parent_name='Char_trent',
            duration=5.5, target_hardpoint='Hp_LHand_PDA', parent_hardpoint='HpLeftConnect')
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_PDA_LEFT_000LV_00, duration=2, time_scale=4,
            trans_time=0.25)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_GESTR_TYPING_000LV_XB, duration=3, time_scale=0.5)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_pda_in_hands', duration=0.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_pda_in_hands_left', duration=0.75, smooth=True)
        wilham.facial(group=MAIN, index=40, append=True, auto_lip=True, extra_delay=0)
        t = 0


        # Реплика 50 · trent · исходное время 26 с
        # Должны - значит останутся. Любите вы, военные, жути нагнать...
        # Исходное окно facial: 5.5 с.
        t = 0
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_pda_in_hands_half', duration=0.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_pda_in_hands_right', duration=1, smooth=True)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_wilham', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_wilham', duration=1, smooth=True)
        t += 1.99999
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent',
            target_name='automarker_point_trent_stand_to_sit', duration=1e-06, smooth=False)
        t += 1e-05
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_NEUT_LEFT_000LV_A_00, duration=5)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_NEUT_RGHT_000LV_A_00, duration=5)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_head_trent', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_head_ik',
            target_name='automarker_head_trent', duration=3, smooth=True)
        cam_sitting.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_sitting_focus',
            target_name='automarker_cam_sitting_point2', duration=10, smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_SITCL_TRNS_180DN_XA_06, duration=5.5)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=4, time_scale=0.8)
        t += 0.51
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Prop_pda', target_name='offscreen', duration=0.001,
            smooth=False)
        trent.facial(group=MAIN, index=50, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.5)


        # Реплика 60 · wilham · исходное время 31 с
        # Тогда перейдём к делу. Силы Рейнланда проводят регулярный мониторинг ситуации в системе Омега-15. Один
        # наш секретный агент добыл важные сведения и должен был доставить на полицейский аванпост в зоне рудокопов
        # Исходное окно facial: 13 с.
        t = 0
        t += 3
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_LOOK_RLLV_A_06, duration=9, time_scale=0.75,
            loop=True, trans_time=1)
        t += 2
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_SMALL_000LV_XA_07, duration=7, loop=True,
            trans_time=1)
        wilham.facial(group=MAIN, index=60, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1)


        # Реплика 70 · trent · исходное время 43 с
        # Но по непонятной для нас причине он так и не добрался до указанного места встречи. Скорее всего он был
        # перехвачен и убит.
        # TODO: в текущем сценарии говорит Wilham; в старой постановке — Trent.
        # Исходное окно facial: 6 с.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_YESS_000LV_A_01, duration=6, time_scale=0.6)
        t += 2
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_TALK_000UP_A_17, duration=6, time_scale=0.8,
            trans_time=1)
        trent.facial(group=MAIN, index=70, append=True, auto_lip=True, extra_delay=0)
        t = 0


        # Реплика 80 · wilham · исходное время 49 с
        # Сочувствую. Но при чем тут я?
        # TODO: в текущем сценарии говорит Trent; в старой постановке — Wilham.
        # Исходное окно facial: 6.5 с.
        t = 0
        cam_wilham_near.set(group=MAIN, time_delay=t)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDUP_TRNS_000LV_XA_02, duration=4)
        t += 1
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_GESTR_SMALL_000LV_00, duration=10)
        t += 0.7
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_RHND_CASL_000LV_xb_03, duration=2.3,
            time_scale=0.5, trans_time=1)
        t += 2.3
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDDN_TRNS_000LV_XA_02, duration=4,
            trans_time=1)
        wilham.facial(group=MAIN, index=80, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.5)


        # Реплика 90 · trent · исходное время 55 с
        # Вашей задачей будет найти этот корабль и получить с него интересующие нас данные.
        # TODO: в текущем сценарии говорит Wilham; в старой постановке — Trent.
        # Исходное окно facial: 6 с.
        t = 0
        cam_trent_closest.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_NOD_YES_SLGHTLY_000LV_XA_03, duration=6,
            time_scale=0.8, trans_time=1)
        trent.facial(group=MAIN, index=90, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-3)


        # Реплика 100 · wilham · исходное время 58 с
        # Вам в этом поможет наш внешний агент, электронщик-энтузиаст. Он работает в местной общие рудокопов.
        # Исходное окно facial: 12 с.
        t = 0
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_eye_ik',
            duration=30, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        cam_msn_begins.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_msn_begins',
            target_name='automarker_cam_msn_begins_pos2', duration=12, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_msn_begins_focus',
            target_name='automarker_cam_msn_begins_point2', duration=12, smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_LSTN_000UP_A_18, duration=50, loop=True)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_TALK_HNSTBL_000UP_A_33, duration=13, loop=True)
        wilham.facial(group=MAIN, index=100, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.0)


        # Реплика 110 · trent · исходное время 69 с
        # Там он помогает рабочим находить астероиды с ценной рудой, а так же имеет все данные об обломках
        # кораблей, которые могут быть нам интересны.
        # TODO: в текущем сценарии говорит Wilham; в старой постановке — Trent.
        # Исходное окно facial: 6 с.
        t = 0
        trent.facial(group=MAIN, index=110, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-4)


        # Реплика 120 · wilham · исходное время 71 с
        # И всего делов-то? Могу приступать?
        # TODO: в текущем сценарии говорит Trent; в старой постановке — Wilham.
        # Исходное окно facial: 27.5 с.
        t = 0
        cam_wilham_msn1.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_wilham_msn1',
            target_name='automarker_cam_wilham_msn1_pos2', duration=32, smooth=True)
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_wilham', target_name='automarker_wilham_eye_ik',
            duration=50, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_head_trent_middle', duration=2, smooth=True)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_TALK_HNSTBL_000LV_A_34, duration=26,
            time_scale=0.7, start_time=2, trans_time=2)
        t += 3
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_table_center', duration=2, smooth=True)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_head_trent_middle', duration=2, smooth=True)
        t += 5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_table_center_right', duration=2, smooth=True)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_table_center_left', duration=2, smooth=True)
        t += 3
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_head_trent_middle', duration=2, smooth=True)
        t += 3
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_table_center_left', duration=2, smooth=True)
        t += 5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_table_center_right', duration=2, smooth=True)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_head_trent_middle_right', duration=1, smooth=True)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_POINT_RGHT_MILI_000LV_00, duration=3)
        t += 1
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_GRABR_CHIN_RLEASE_000LV_XA_02, duration=5,
            trans_time=1)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_NEUT_ATEASE_RGHT_000LV_XB_, duration=2.533,
            trans_time=0.5)
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='prop_cigarette_2',
            parent_name='Char_wilham', duration=28, target_hardpoint='hprightconnect_cigarette2',
            parent_hardpoint='hprightconnect')
        vfx_rtc_cigaretteglow_4.start(group=MAIN, time_delay=t, duration=28)
        vfx_rtc_sydsmoke_3.start(group=MAIN, time_delay=t, duration=28)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_head_trent_right_far', duration=1, smooth=True)
        wilham.facial(group=MAIN, index=120, append=True, auto_lip=True, extra_delay=0)
        t = 0
        t += 0.5
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CHIN_HOLDR_000LV_XA_03, duration=5, trans_time=0.5)
        t += 2.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_head_trent_middle', duration=2, smooth=True)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_HOLD_CHIN_RLEASE_000LV_XA_03, duration=5,
            trans_time=0.5)
        main_group.append_time(4.5)


        # Реплика 130 · wilham · исходное время 103 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m02_offer_0130_wilham
        # Исходное окно facial: 16.5 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_wilham_msn1',
            target_name='automarker_cam_wilham_msn1_pos3', duration=18, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_wilham_msn1_focus',
            target_name='automarker_cam_wilham_msn1_point3', duration=18, smooth=True)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_IDLE_SMALL_000LV_XA_05, duration=5, loop=True,
            trans_time=1)
        t += 5
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_TAP_RHND_000LV_A_02, duration=5, time_scale=0.5,
            loop=True, trans_time=1)
        t += 5
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_IDLE_SMALL_000LV_XA_05, duration=8, loop=True,
            trans_time=1)
        t += 4
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_NEUT_RGHT_000LV_A_00, duration=5, trans_time=1)
        # wilham.facial(group=MAIN, index=130, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(16.5)  # длительность удалённой реплики
        main_group.append_time(0.5)


        # Реплика 140 · trent · исходное время 120 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m02_offer_0140_trent
        # Исходное окно facial: 6 с.
        t = 0
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_eye_ik',
            duration=30, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        cam_trent_near.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_SMALL_000LV_XA_07, duration=0.5)
        t += 0.5
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_SHRG_SHLDRS_SMALL_000LV_XA_03, duration=3,
            time_scale=0.8, trans_time=0.5)
        t += 2.5
        cam_wilham_msn3.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_wilham_msn3',
            target_name='automarker_cam_wilham_msn3_pos2', duration=17, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_wilham_msn3_focus',
            target_name='automarker_cam_wilham_msn3_point2', duration=17, smooth=True)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_HOLD_CHIN_RLEASE_000LV_XA_03, duration=3)
        # trent.facial(group=MAIN, index=140, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(6)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2)


        # Реплика 150 · wilham · исходное время 124 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m02_offer_0150_wilham
        # Исходное окно facial: 16 с.
        t = 0
        t += 1
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, duration=3, trans_time=1)
        t += 0.001
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='prop_cigarette_2', target_name='offscreen',
            duration=0.001, smooth=False)
        t += 3.499
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDUP_TRNS_000LV_XA_02, duration=5,
            trans_time=1)
        t += 0.5
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_POINT_RGHT_CASL_000LV_00, duration=4,
            time_scale=2, trans_time=0.25)
        t += 1
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_RHND_CASL_000LV_XA_04, duration=8, loop=True,
            trans_time=1)
        t += 3
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00, duration=4, time_scale=0.75,
            trans_time=0.25)
        t += 4
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_POINT_RGHT_CASL_000LV_00, duration=4,
            time_scale=2, start_time=3, trans_time=0.5)
        t += 1
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDDN_TRNS_000LV_XA_02, duration=3,
            trans_time=0.5)
        # wilham.facial(group=MAIN, index=150, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(16.0)  # длительность удалённой реплики
        main_group.append_time(0.0)


        # Реплика 160 · trent · исходное время 140 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m02_offer_0160_trent
        # Исходное окно facial: 7.8 с.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_TALK_000UP_A_17, duration=9, start_time=1)
        # trent.facial(group=MAIN, index=160, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(7.8)  # длительность удалённой реплики
        main_group.append_time(0.2)


        # Реплика 170 · wilham · исходное время 148 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m02_offer_0170_wilham
        # Исходное окно facial: 17.5 с.
        t = 0
        cam_wilham_msn2.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_wilham_msn2',
            target_name='automarker_cam_wilham_msn2_pos2', duration=15, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_wilham_msn2_focus',
            target_name='automarker_cam_wilham_msn2_point2', duration=15, smooth=True)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_NOD_YES_EMPH_000LV_XA_02, duration=1.8,
            time_scale=0.5, start_time=1)
        t += 1.8
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_HNDSUP_TRNS_000LV_XA_02, duration=5,
            time_scale=0.75, trans_time=0.5)
        t += 1.7
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_HNDS_CASL_000LV_xb_03, duration=3,
            time_scale=0.75, loop=True, trans_time=0.5)
        t += 3.0
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_HNDSDN_TRNS_000LV_XA_02, duration=3,
            trans_time=0.5)
        t += 1.5
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_LHNDUP_TRNS_000LV_XA_02, duration=5,
            time_scale=0.75, trans_time=0.5)
        t += 1.5
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_LHND_CASL_000LV_xa_03, duration=3.5,
            time_scale=0.75, loop=True, trans_time=0.5)
        t += 2.5
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_eye_ik',
            duration=8, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 1
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_LHNDDN_TRNS_000LV_XA_02, duration=5,
            trans_time=0.5)
        t += 1.5
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_IDLE_SMALL_000LV_XA_05, duration=0.5,
            trans_time=0.5)
        t += 0.5
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_wilham', target_name='automarker_wilham_head_ik',
            duration=20, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_head_ik',
            target_name='automarker_head_trent_middle', duration=2, smooth=True)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_IDLE_SMALL_000LV_XA_05, duration=1)
        cam_trent_closest.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_SMALL_000LV_XA_07, duration=7, start_time=2)
        # wilham.facial(group=MAIN, index=170, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(17.5)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.2)


        # Реплика 180 · trent · исходное время 163.3 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m02_offer_0180_trent
        # Исходное окно facial: 4.5 с.
        # trent.facial(group=MAIN, index=180, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(4.5)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.8)


        # Реплика 190 · wilham · исходное время 165 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m02_offer_0190_wilham
        # Исходное окно facial: 27.5 с.
        t = 0
        cam_wilham_near.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_wilham_near',
            target_name='automarker_cam_wilham_near_pos2', duration=28, smooth=True)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_EMPH_RHNDUP_TRNS_000LV_XA_01, duration=2,
            time_scale=0.7, start_time=0.5)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_POINT_RGHT_CASL_000LV_00, duration=1,
            start_time=3, trans_time=0.5)
        t += 1
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_EMPH_RHNDDN_TRNS_000LV_XA_00, duration=3,
            time_scale=0.75, trans_time=0.25)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_POINT_RGHT_CASL_000LV_00, duration=2,
            start_time=6, trans_time=0.5)
        t += 1.3
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=2, trans_time=1)
        t += 3.7
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_CONV_LHNDUP_TRNS_000LV_XA_02, duration=5,
            time_scale=0.75, trans_time=1)
        t += 1.5
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_CONV_LHND_CASL_000LV_xa_03, duration=4.5,
            time_scale=0.6, loop=True, trans_time=1)
        t += 4.5
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_CONV_LHNDDN_TRNS_000LV_XA_02, duration=5,
            time_scale=0.75, trans_time=1)
        t += 2
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_SMALL_000LV_XA_07, duration=8, loop=True,
            trans_time=1)
        t += 9
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_NOD_YES_SLGHTLY_000LV_XA_03, duration=3,
            time_scale=0.75, trans_time=0.2)
        t += 3
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_MED_000LV_XA_07, duration=3, loop=True,
            trans_time=1)
        # wilham.facial(group=MAIN, index=190, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(27.5)  # длительность удалённой реплики
        t = 0
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=5, trans_time=0.25)
        main_group.append_time(0.5)
        preserve_spatial(self.get_entity('automarker_point_trent_stand_init'),
            source_basis=[[0.5, 0, 0.5], [0, 1, 0], [-0.5, 0, -0.5]],
            reference_orientation=[0.5773502588272095, -0.0, 0.8164966106414795, -0.0])
        preserve_spatial(self.get_entity('automarker_point_trent_stand_final'),
            source_basis=[[0.5, 0, 0.5], [0, 1, 0], [-0.5, 0, -0.5]],
            reference_orientation=[0.5773502588272095, -0.0, 0.8164966106414795, -0.0])


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M02BshipBarOfferScene
