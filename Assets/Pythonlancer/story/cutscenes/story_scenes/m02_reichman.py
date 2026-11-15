"""m02_reichman: постановка для ручного редактирования.

Точки: SCENES/m02_reichman.blend → DUMPS/m02_reichman.json.
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
    MotionEvent,
    MoveEvent,
    NeckIkEvent,
    Prop,
    Ship,
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


class PropSubtitlesPack3(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_pack3'
    SRT_GRP = 0
    USR_FLG = 0


class PropSubtitlesM02Done01(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_done01'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Done02(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_done02'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Done03(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_done03'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Done04(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_done04'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Done05(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_done05'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Done06(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_done06'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Done07(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_done07'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Done08(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_done08'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Done09(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_done09'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Done10(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_done10'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Done11(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_done11'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Done12(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_done12'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Done13(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_done13'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Done14(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_done14'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Done15(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_done15'
    SRT_GRP = -1
    USR_FLG = 0


class PropSubtitlesM02Done16(Prop):
    COMPOUND_TEMPLATE_NAME = 'subtitles_m02_done16'
    SRT_GRP = -1
    USR_FLG = 0


class PropMainShip(Ship):
    COMPOUND_TEMPLATE_NAME = 'rh_elite'
    SRT_GRP = 0
    USR_FLG = 0


class ExtraCharTrooper1(actors.Actor):
    NAME = 'trooper1'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'ms2_trooper1'
    GAME_ACTOR = 'Trooper1'


class ExtraCharTrooper2(actors.Actor):
    NAME = 'trooper2'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'ms2_trooper2'
    GAME_ACTOR = 'Trooper2'



class M02ReichmanScene(Scene):
    DUMP_FILE = 'm02_reichman'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        music_main = Sound(root=self, name='music_main', sound='music_discordant_psychosis', attenuation=-10, dmin=50,
            dmax=300, priority='Story_Sound_1')
        preserve_entity(music_main, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        music_second = Sound(root=self, name='music_second', sound='music_anticipation_more_forboding', attenuation=-10,
            dmin=50, dmax=300, priority='Story_Sound_1')
        preserve_entity(music_second, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        main_ship = PropMainShip(root=self, name='main_ship', light_group=3, init_point='main_ship', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(main_ship, userprops={'category': 'Spaceship', 'loadout': 'level_rh_elite_loadout04'})
        reichman = Character(root=self, actor=actors.Reichman, light_group=3, init_point='Char_reichman',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(reichman, template_name='reichman', userprops={'actor': 'Reichman', 'category': 'Character'})
        trent = Character(root=self, actor=actors.Trent, light_group=3, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'actor': 'Player', 'category': 'Character'})
        wilham = Character(root=self, actor=actors.Wilham, light_group=3, init_point='Char_wilham', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(wilham, template_name='wilham', userprops={'actor': 'Wilham', 'category': 'Character'})
        trooper1 = Character(root=self, actor=ExtraCharTrooper1, light_group=3, init_point='Char_trooper1',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(trooper1, template_name='ms2_trooper1', userprops={'actor': 'Trooper1', 'category': 'Character'})
        trooper2 = Character(root=self, actor=ExtraCharTrooper2, light_group=3, init_point='Char_trooper2',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(trooper2, template_name='ms2_trooper2', userprops={'actor': 'Trooper2', 'category': 'Character'})
        cam_start = LookAtCamera(root=self, name='cam_start', fov=40, farplane=5000, look_duration=300)
        preserve_entity(cam_start)
        cam_reichman_near = LookAtCamera(root=self, name='cam_reichman_near', fov=15, farplane=5000, look_duration=300)
        preserve_entity(cam_reichman_near)
        cam_reichman_top = LookAtCamera(root=self, name='cam_reichman_top', fov=17, farplane=5000, look_duration=300)
        preserve_entity(cam_reichman_top)
        cam_reichman_far = LookAtCamera(root=self, name='cam_reichman_far', fov=23, farplane=5000, look_duration=300)
        preserve_entity(cam_reichman_far)
        cam_reichman_reward = LookAtCamera(root=self, name='cam_reichman_reward', fov=17, farplane=5000, look_duration=300)
        preserve_entity(cam_reichman_reward)
        cam_trent_near = LookAtCamera(root=self, name='cam_trent_near', fov=15, farplane=5000, look_duration=300)
        preserve_entity(cam_trent_near)
        cam_trent_top = LookAtCamera(root=self, name='cam_trent_top', fov=18, farplane=5000, look_duration=300)
        preserve_entity(cam_trent_top)
        cam_trent_far = LookAtCamera(root=self, name='cam_trent_far', fov=20, farplane=5000, look_duration=300)
        preserve_entity(cam_trent_far)
        cam_trent_away = LookAtCamera(root=self, name='cam_trent_away', fov=15, farplane=5000, look_duration=300)
        preserve_entity(cam_trent_away)
        cam_reichman_looktrent = LookAtCamera(root=self, name='cam_reichman_looktrent', fov=20, farplane=5000,
            look_duration=300)
        preserve_entity(cam_reichman_looktrent)
        cam_final = LookAtCamera(root=self, name='cam_final', fov=25, farplane=5000, look_duration=300)
        preserve_entity(cam_final)

        # Вход / начальная постановка.
        t = 0
        music_main.start(group=MAIN, time_delay=t, duration=47, loop=True)
        trent.motion(group=MAIN, time_delay=t, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, duration=1)
        cam_start.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_start', target_name='automarker_cam_start_pos2',
            duration=6, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_start_focus',
            target_name='automarker_cam_start_marker_pos2', duration=6, smooth=True)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=10, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_wilham', target_name='automarker_wilham_head_ik',
            duration=10, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_reichman', target_name='automarker_reichman_eye_ik',
            duration=15, transition_duration=0.1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trooper2', anim=Male.Sc_MLBODY_STND_000LV_E_20,
            duration=1555, time_scale=0.5, loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trooper1', anim=Male.Sc_MLBODY_STND_000LV_E_20,
            duration=1555, time_scale=0.5, loop=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=3.6, start_time=0.3, loop=True)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=3.8, start_time=0.1,
            loop=True)
        reichman.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_HOLD_ARMS_CROSSED_000LV_XA_02, duration=5)
        t += 3
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trooper2', target_name='Char_wilham', duration=25,
            transition_duration=3, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 0.6
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=4)
        t += 0.2
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=4)
        t += 0.2
        reichman.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=2, time_scale=0.2)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_reichman_eye_ik',
            target_name='automarker_head_reichman_back_left', duration=2, smooth=True)
        t += 0.5
        reichman.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, duration=5)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_reichman_head_ik',
            target_name='automarker_head_trent', duration=1, smooth=True)
        t += 1
        reichman.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_TURN_180LV_XA_04, duration=5, time_scale=0.75,
            trans_time=0.5)
        t += 1
        cam_reichman_top.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_reichman_top',
            target_name='automarker_cam_reichman_top_pos2', duration=5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_reichman_top_focus',
            target_name='automarker_cam_reichman_top_marker_pos2', duration=6, smooth=True)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_reichman_eye_ik',
            target_name='automarker_head_reichman_front', duration=1, smooth=True)
        main_group.append_time(10)


        # Реплика 10 · reichman · исходное время 10 с
        # А вот и сам знаменитый Трент.
        # Исходное окно facial: 4 с.
        t = 0
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_reichman',
            target_name='automarker_reichman_head_ik', duration=5, transition_duration=1, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 1
        reichman.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=5, time_scale=0.6,
            loop=True, trans_time=2)
        t += 2
        cam_trent_far.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=4, trans_time=2)
        reichman.facial(group=MAIN, index=10, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.8)


        # Реплика 20 · trent · исходное время 13.2 с
        # И чем же я так знаменит, мистер, эмм...
        # Исходное окно facial: 2.1 с.
        t = 0
        trent.facial(group=MAIN, index=20, append=True, auto_lip=True, extra_delay=0)
        t = 0
        t += 0.2
        trent.motion(group=MAIN, time_delay=t, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, duration=5, trans_time=1)
        main_group.append_time(0.7)


        # Реплика 30 · reichman · исходное время 16 с
        # Райхманн. Адмирал Райхманн, если позволите.
        # Исходное окно facial: 4 с.
        t = 0
        cam_reichman_near.set(group=MAIN, time_delay=t)
        reichman.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_BOW_ASNSTYL_RSPCTFLY_000LV_xa_03, duration=3)
        t += 2
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=7, trans_time=2)
        t += 1
        reichman.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=5, time_scale=0.6,
            trans_time=2)
        reichman.facial(group=MAIN, index=30, append=True, auto_lip=True, extra_delay=0)
        t = 0


        # Реплика 40 · trent · исходное время 20 с
        # Моё почтение, адмирал Райхманн! Так чем же я знаменит?
        # Исходное окно facial: 8 с.
        t = 0
        cam_trent_top.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_reichman_eye_ik',
            target_name='automarker_head_trent', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_reichman_head_ik',
            target_name='automarker_head_trent', duration=2, smooth=True)
        trent.facial(group=MAIN, index=40, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-4)


        # Реплика 50 · reichman · исходное время 24 с
        # О, мистер Трент, в последнее время в некоторых кругах только и разговоров, что о вас! Надеюсь, герр
        # Вильгельм достойно оплачивает вашу работу?
        # Исходное окно facial: 8.4 с.
        t = 0
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_reichman',
            target_name='automarker_reichman_head_ik', duration=30, transition_duration=1, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_reichman', target_name='automarker_reichman_eye_ik',
            duration=30, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_reichman_far_focus',
            target_name='automarker_cam_reichman_far_marker_pos2', duration=8, smooth=True)
        cam_reichman_far.set(group=MAIN, time_delay=t)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_reichman_far',
            target_name='automarker_cam_reichman_far_pos2', duration=6, smooth=True)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_reichman_eye_ik',
            target_name='automarker_head_wilham', duration=2, smooth=True)
        reichman.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, duration=3,
            trans_time=1.5)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_reichman', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_reichman', duration=2, smooth=True)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_reichman_head_ik',
            target_name='automarker_head_wilham_trent_half', duration=2, smooth=True)
        reichman.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_RHND_CASL_000LV_xa_01, duration=2,
            loop=True, trans_time=1.5)
        reichman.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00, duration=4,
            time_scale=0.75, trans_time=0.25)
        t += 1
        reichman.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_02, duration=3,
            trans_time=1.5)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=10, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_eye_ik',
            duration=10, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_wilham', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_reichman_wilham_half', duration=2, smooth=True)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_trent_near_focus',
            target_name='automarker_cam_trent_near_marker_pos2', duration=4, smooth=True)
        cam_trent_near.set(group=MAIN, time_delay=t)
        reichman.facial(group=MAIN, index=50, append=True, auto_lip=True, extra_delay=0)
        t = 0
        t += 0.1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_reichman', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_reichman', duration=3.5, smooth=True)
        main_group.append_time(0.8)


        # Реплика 60 · trent · исходное время 33.2 с
        # Не жалуюсь.
        # Исходное окно facial: 4.5 с.
        t = 0
        t += 0.8
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_reichman_eye_ik',
            target_name='automarker_head_trent', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_reichman_head_ik',
            target_name='automarker_head_trent', duration=1, smooth=True)
        trent.facial(group=MAIN, index=60, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.7)


        # Реплика 70 · reichman · исходное время 36 с
        # Скромность - похвальная благодетель, герр Трент, но одной благодетелью сыт не будешь, ха-ха. Я
        # распоряжусь, чтобы ваш гонорар за предыдущую миссию был удвоен. Всех благ, герр Трент!
        # Исходное окно facial: 15.25 с.
        t = 0
        trent.motion(group=MAIN, time_delay=t, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, duration=1, trans_time=1)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_reichman_reward',
            target_name='automarker_cam_reichman_reward_pos2', duration=10, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_reichman_reward_focus',
            target_name='automarker_cam_reichman_reward_marker_pos2', duration=10, smooth=True)
        cam_reichman_reward.set(group=MAIN, time_delay=t)
        reichman.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=1)
        t += 1
        reichman.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_GESTL_STOP_000LV_XA_03, duration=4.5,
            time_scale=0.6, trans_time=1)
        t += 4.5
        reichman.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_ATEASE_HSEC_RLEASE_000LV_XA_03, duration=5,
            time_scale=0.6, trans_time=1)
        t += 0.5
        music_main.change_attenuation(group=MAIN, time_delay=t, duration=5, attenuation=-100)
        t += 2
        reichman.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_ATEASE_HOLD_000LV_XA_01, duration=5,
            time_scale=0.6, loop=True, trans_time=1)
        t += 3
        music_second.start(group=MAIN, time_delay=t, duration=60, loop=True)
        music_second.change_attenuation(group=MAIN, time_delay=t, duration=5, attenuation=0)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_trent_away',
            target_name='automarker_cam_trent_away_pos2', duration=10, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_trent_away_focus',
            target_name='automarker_cam_trent_away_marker_pos2', duration=10, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trooper1', target_name='offscreen', duration=1e-05,
            smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trooper2', target_name='offscreen', duration=1e-05,
            smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', target_name='automarker_point_trent_talk',
            duration=1e-05, smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_wilham',
            target_name='automarker_point_wilham_talk', duration=1e-05, smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_reichman',
            target_name='automarker_point_reichman_looktrent', duration=1e-05, smooth=False)
        cam_trent_away.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WALK_TRNS_180LV_XA_02, duration=5, time_scale=0.6,
            trans_time=1)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_TURN_090LV_XA_02, duration=5, time_scale=0.5)
        t += 0.1
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_wilham', target_name='Char_trent', duration=5,
            transition_duration=5, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_wilham', target_name='Char_trent', duration=5,
            transition_duration=2, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 3.9
        reichman.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=5,
            time_scale=0.5, start_time=0.35)
        reichman.facial(group=MAIN, index=70, append=True, auto_lip=True, extra_delay=0)
        t = 0
        t += 0.75
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=25, time_scale=0.6,
            loop=True, trans_time=2)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_reichman_eye_ik',
            target_name='automarker_head_reichman_trentaway_front', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_reichman_head_ik',
            target_name='automarker_head_reichman_trentaway_front', duration=2, smooth=True)
        t += 2.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_head_trent_away', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_head_ik',
            target_name='automarker_head_trent_away', duration=1, smooth=True)
        main_group.append_time(3.75)


        # Реплика 80 · reichman · исходное время 55 с
        # Так вы считаете, что он - тот кто нам нужен?
        # Исходное окно facial: 4 с.
        t = 0
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_wilham', target_name='automarker_wilham_head_ik',
            duration=35, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_wilham', target_name='automarker_wilham_eye_ik',
            duration=35, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_head_reichman_trentaway', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_head_ik',
            target_name='automarker_wilham_rotate_front_left', duration=3, smooth=True)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_trent_away',
            target_name='automarker_cam_trent_away_pos3', duration=11, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_trent_away_focus',
            target_name='automarker_cam_trent_away_marker_pos3', duration=11, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', target_name='offscreen', duration=1e-05,
            smooth=False)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_reichman',
            target_name='automarker_reichman_head_ik', duration=35, transition_duration=1, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_reichman', target_name='automarker_reichman_eye_ik',
            duration=35, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_reichman_eye_ik',
            target_name='automarker_head_wilham', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_reichman_head_ik',
            target_name='automarker_head_reichman_trentaway_front_right', duration=2, smooth=True)
        reichman.facial(group=MAIN, index=80, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1)


        # Реплика 90 · wilham · исходное время 58 с
        # Безусловно, герр Адмирал. Он - тот, кто поможет нам выполнить все известные вам задачи.
        # Исходное окно facial: 5.65 с.
        t = 0
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_head_trent_away', duration=4, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_head_ik',
            target_name='automarker_wilham_rotate_front', duration=4, smooth=True)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_reichman_eye_ik',
            target_name='automarker_head_reichman_trentaway_front', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_reichman_head_ik',
            target_name='automarker_head_reichman_trentaway_front', duration=2, smooth=True)
        wilham.facial(group=MAIN, index=90, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(0.35)


        # Реплика 100 · reichman · исходное время 64 с
        # И вы это гарантируете?
        # Исходное окно facial: 4 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_reichman_eye_ik',
            target_name='automarker_head_wilham', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_reichman_head_ik',
            target_name='automarker_head_reichman_trentaway_front_right', duration=1.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_head_reichman_trentaway', duration=3, smooth=True)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_head_ik',
            target_name='automarker_wilham_rotate_front_left', duration=2, smooth=True)
        reichman.facial(group=MAIN, index=100, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.4)


        # Реплика 110 · wilham · исходное время 65.6 с
        # Абсолютно!
        # Исходное окно facial: 5 с.
        t = 0
        t += 1.9
        cam_reichman_looktrent.set(group=MAIN, time_delay=t)
        wilham.facial(group=MAIN, index=110, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.6)


        # Реплика 120 · reichman · исходное время 68 с
        # Хорошо, мы принимаем в работу ваш сценарий.
        # Исходное окно facial: 6.5 с.
        t = 0
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_reichman_eye_ik',
            target_name='automarker_head_reichman_trentaway_front', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_reichman_head_ik',
            target_name='automarker_head_reichman_trentaway_front', duration=2, smooth=True)
        t += 2.5
        reichman.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_ATEASE_HSEC_RLEASE_000LV_XA_03, duration=15,
            time_scale=0.6)
        reichman.facial(group=MAIN, index=120, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.0)


        # Реплика 130 · wilham · исходное время 73.5 с
        # Благодарю за оказанное доверие.
        # Исходное окно facial: 5 с.
        t = 0
        cam_final.set(group=MAIN, time_delay=t)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_SALUT_000LV_XA_03, duration=15, time_scale=0.8)
        t += 1.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_reichman_eye_ik',
            target_name='automarker_head_wilham', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_reichman_head_ik',
            target_name='automarker_head_reichman_trentaway_front_right', duration=2, smooth=True)
        t += 0.5
        reichman.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_ATEASE_HOLD_000LV_XA_01, duration=15,
            time_scale=0.6, loop=True)
        t += 0.5
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=5, trans_time=0.25)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_final', target_name='automarker_cam_final_pos2',
            duration=10, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_final_focus',
            target_name='automarker_cam_final_marker_pos2', duration=10, smooth=True)
        wilham.facial(group=MAIN, index=130, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.0)


        # Реплика 140 · reichman · исходное время 76.5 с
        # Посмотрим что из этого получится. Не смею задерживать, герр Вильгельм.
        # Исходное окно facial: 4 с.
        t = 0
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_reichman_eye_ik',
            target_name='automarker_head_reichman_trentaway_front', duration=7, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_reichman_head_ik',
            target_name='automarker_head_reichman_trentaway_front', duration=7, smooth=True)
        t += 2.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_outpoint', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_head_ik',
            target_name='automarker_outpoint', duration=3, smooth=True)
        t += 1.0
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WALK_TRNS_090LV_XA_02, duration=15, time_scale=0.8)
        reichman.facial(group=MAIN, index=140, append=True, auto_lip=True, extra_delay=0)
        t = 0
        t += 1.5
        reichman.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=2, time_scale=0.2)
        t += 1.0
        music_second.change_attenuation(group=MAIN, time_delay=t, duration=3, attenuation=-8)
        main_group.append_time(5.5)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M02ReichmanScene
