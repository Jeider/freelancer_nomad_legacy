"""m04_hatcher: постановка для ручного редактирования.

Точки: SCENES/m04_hatcher.blend → DUMPS/m04_hatcher.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — смещение внутри текущего блока; facial()/append_time() двигают часы.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character,
    EyeIkEvent,
    Light,
    LookAtCamera,
    MAIN,
    MoveEvent,
    NeckIkEvent,
    RotateAxisEvent,
)
from story.cutscenes.anim import (
    Female,
    Male,
    Trent,
)
from story.cutscenes.source_extensions import (
    SourceAttachEvent,
    preserve_entity,
)
from story import actors


class ExtraCharBartenderFixture(actors.Actor):
    NAME = 'bartender_fixture'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'li_bartender_1'
    GAME_ACTOR = 'bartender'



class M04HatcherScene(Scene):
    DUMP_FILE = 'm04_hatcher'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        ambi_LtG00_Bar_Ovrhd01A = Light(root=self, name='ambi_LtG00_Bar_Ovrhd01A', point_name='ambi_LtG00_Bar_Ovrhd01A',
            extra_name='', light_group=5, diffuse=[0.596078, 0.572549, 0.403922], ambient=[0.223529, 0.2, 0.192157],
            direction=[0, 0, 1], light_type='L_POINT', on=True, range=15, cutoff=18, theta=15, color=[233, 208, 150],
            attenuation=[0.8999999762, 0, 0.006])
        preserve_entity(ambi_LtG00_Bar_Ovrhd01A)
        ambi_LtG00_Bar_Ovrhd01B = Light(root=self, name='ambi_LtG00_Bar_Ovrhd01B', point_name='ambi_LtG00_Bar_Ovrhd01B',
            extra_name='', light_group=5, diffuse=[0.596078, 0.572549, 0.403922], ambient=[0, 0, 0], direction=[0, 0, 1],
            light_type='L_POINT', on=True, range=5, cutoff=18, theta=15, color=[233, 208, 150],
            attenuation=[0.8999999762, 0, 0.006])
        preserve_entity(ambi_LtG00_Bar_Ovrhd01B)
        bartender_fixture = Character(root=self, actor=ExtraCharBartenderFixture, light_group=0,
            init_point='Char_bartender_fixture', rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(bartender_fixture, template_name='li_bartender_1',
            userprops={'actor': 'bartender', 'category': 'Character'})
        hatcher = Character(root=self, actor=actors.Hatcher, light_group=5, init_point='Char_hatcher',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(hatcher, template_name='hatcher', userprops={'actor': 'Hatcher', 'category': 'Character'})
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'Actor': 'Player', 'category': 'Character'})
        alaric = Character(root=self, actor=actors.Alaric, light_group=0, init_point='Char_alaric', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(alaric, template_name='alaric', userprops={'actor': 'Alaric', 'category': 'Character'})
        cam_start = LookAtCamera(root=self, name='cam_start', fov=25, farplane=5000, look_duration=300)
        preserve_entity(cam_start)
        cam_hatcher_firstlook = LookAtCamera(root=self, name='cam_hatcher_firstlook', fov=15, farplane=5000,
            look_duration=300)
        preserve_entity(cam_hatcher_firstlook)
        cam_hatcher_people_arrive = LookAtCamera(root=self, name='cam_hatcher_people_arrive', fov=15, farplane=5000,
            look_duration=300)
        preserve_entity(cam_hatcher_people_arrive)
        cam_hatcher_near = LookAtCamera(root=self, name='cam_hatcher_near', fov=15, farplane=5000, look_duration=300)
        preserve_entity(cam_hatcher_near)
        cam_trent_near = LookAtCamera(root=self, name='cam_trent_near', fov=15, farplane=5000, look_duration=300)
        preserve_entity(cam_trent_near)
        cam_alaric = LookAtCamera(root=self, name='cam_alaric', fov=20, farplane=5000, look_duration=300)
        preserve_entity(cam_alaric)
        cam_alaric_near = LookAtCamera(root=self, name='cam_alaric_near', fov=15, farplane=5000, look_duration=300)
        preserve_entity(cam_alaric_near)
        cam_hatcher_final = LookAtCamera(root=self, name='cam_hatcher_final', fov=20, farplane=5000, look_duration=300)
        preserve_entity(cam_hatcher_final)

        # Вход / начальная постановка.
        t = 0
        cam_start.set(group=MAIN, time_delay=t)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['wlkg_trent_front', 'Char_trent'], duration=35,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='Body_Head', target_type='PART',
            flags='POSITION')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['automarker_wlkg_alaric', 'Char_alaric'],
            duration=200, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='Body_Head', target_type='PART',
            flags='POSITION')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['automarker_wlkg_alaric_front_near', 'Char_alaric'],
            duration=200, offset=[0.75, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='Body_Head', target_type='PART',
            flags='POSITION')
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_NEUT_LEFT_000LV_A_00, duration=5)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_NEUT_RGHT_000LV_A_00, duration=5)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=6.91, time_scale=0.75,
            loop=True)
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=6.91, time_scale=0.75,
            start_time=0.2, loop=True)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STLB_000LV_A_21, duration=16, time_scale=0.75,
            start_time=2)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_start', target_name='automarker_cam_start_pos2',
            duration=15, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_start_focus',
            target_name='automarker_cam_start_marker_pos2', duration=15, smooth=True)
        t += 6.91
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=3, time_scale=0.75)
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=3, time_scale=0.75,
            start_time=0.22, trans_time=0.2)
        t += 1.09
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=10, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_eye_ik',
            duration=10, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_alaric', target_name='automarker_alaric_head_ik',
            duration=10, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 1.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_wlkg_alaric_front_near', duration=2, smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_POINT_RHND_000LV_A_03, duration=5, time_scale=0.75,
            trans_time=0.5)
        trent.motion(group=MAIN, time_delay=t, anim=Male.GENERIC_ANIM, duration=6, trans_time=0.25)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_alaric_head_ik',
            target_name='automarker_marker_hatcher_sitpoint', duration=2, smooth=True)
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=5,
            time_scale=0.8, trans_time=1)
        t += 3
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_trent_front_exitpoint', duration=2, smooth=True)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_hatcher_firstlook',
            target_name='automarker_cam_hatcher_firstlook_pos2', duration=7, smooth=True)
        cam_hatcher_firstlook.set(group=MAIN, time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_alaric_head_ik',
            target_name='automarker_head_alaric_front_exitpoint', duration=2, smooth=True)
        t += 1
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_hatcher', target_name='automarker_hatcher_eye_ik',
            duration=5, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STLB_LSTN_270LV_C_07, duration=6, trans_time=1)
        t += 1
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_hatcher', target_name='automarker_hatcher_head_ik',
            duration=4, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STLB_STDSL_TRNS_225LV_A_03, duration=3)
        cam_hatcher_people_arrive.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent',
            target_name='automarker_point_trent_wayforward', duration=0.001, smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_alaric',
            target_name='automarker_point_alaric_wayforward', duration=0.001, smooth=False)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STLB_STDSL_TRNS_225LV_A_03, duration=3)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=3.25, time_scale=0.75,
            loop=True)
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=3.25, time_scale=0.75,
            loop=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_hatcher', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_hatcher', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_alaric_head_ik',
            target_name='automarker_head_hatcher', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_alaric_eye_ik',
            target_name='automarker_head_hatcher', duration=2, smooth=True)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_hatcher_front', duration=0.1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_hatcher_front', duration=0.1, smooth=True)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_trent_near', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=2, smooth=True)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_hatcher', target_name='automarker_hatcher_head_ik',
            duration=90, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_hatcher', target_name='automarker_hatcher_eye_ik',
            duration=90, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 0.5
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=67.5, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_alaric', target_name='automarker_alaric_head_ik',
            duration=67.5, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        main_group.append_time(25)


        # Реплика 10 · hatcher · исходное время 25 с
        # Джентльмены.
        # Исходное окно facial: 2.8 с.
        t = 0
        t += 0.25
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_TURN_180LV_XA_04, duration=1, start_time=0.75,
            trans_time=1)
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_TURN_270LV_XA_04, duration=1.25, start_time=0.75,
            trans_time=1)
        t += 1.0
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=30, time_scale=0.7,
            trans_time=2)
        t += 0.25
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=10, time_scale=0.7,
            start_time=2, trans_time=2)
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_eye_ik',
            duration=60, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_alaric', target_name='automarker_alaric_eye_ik',
            duration=60, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_alaric_focus',
            target_name='automarker_cam_alaric_marker_pos2', duration=4, smooth=True)
        cam_alaric.set(group=MAIN, time_delay=t)
        hatcher.facial(group=MAIN, index=10, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.1)


        # Реплика 20 · trent · исходное время 26.7 с
        # Мисс Хетчер.
        # Исходное окно facial: 5.8 с.
        t = 0
        t += 1.1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_alaric_near', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_alaric', duration=1, smooth=True)
        trent.facial(group=MAIN, index=20, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-4.5)


        # Реплика 30 · alaric · исходное время 28 с
        # Мисс Хетчер, у вас такие красивые бездонные глаза, что...
        # Исходное окно facial: 7.5 с.
        t = 0
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_hatcher_front', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_hatcher_front', duration=1, smooth=True)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_hatcher', duration=1.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_hatcher', duration=1, smooth=True)
        alaric.facial(group=MAIN, index=30, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-3.5)


        # Реплика 40 · hatcher · исходное время 32 с
        # Что вы перестанете нести эту околесицу, иначе я рассержусь
        # Исходное окно facial: 6 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_alaric_near', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_alaric', duration=1.5, smooth=True)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_TALK_000LV_B_10, duration=17, time_scale=0.5,
            loop=True)
        cam_hatcher_people_arrive.set(group=MAIN, time_delay=t)
        t += 3.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_trent_near', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1.5, smooth=True)
        hatcher.facial(group=MAIN, index=40, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2)


        # Реплика 45 · hatcher · исходное время 36 с
        # . О деле. Все выполнено на лучшем уровне.
        # Исходное окно facial: 6.5 с.
        t = 0
        hatcher.facial(group=MAIN, index=45, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-3.5)


        # Реплика 50 · hatcher · исходное время 39 с
        # Я даже не буду спрашивать чего стоило вам сбежать из Рейнланда с ТАКИМИ документами
        # Исходное окно facial: 6.4 с.
        t = 0
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_alaric_near', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_alaric', duration=2, smooth=True)
        hatcher.facial(group=MAIN, index=50, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.4)


        # Реплика 55 · hatcher · исходное время 44 с
        # Я девушка впечатлительная, боюсь в обморок упасть.
        # Исходное окно facial: 3.1 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_hatcher_front', duration=2, smooth=True)
        t += 1.8
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1.5, smooth=True)
        hatcher.facial(group=MAIN, index=55, append=True, auto_lip=True, extra_delay=0)
        t = 0
        t += 0.1
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHEAD_BASEPOSE_000LV_02_01, duration=6, trans_time=1)
        t += 1.3
        cam_trent_near.set(group=MAIN, time_delay=t)
        main_group.append_time(1.5)


        # Реплика 60 · trent · исходное время 48.6 с
        # Мы старались.
        # Исходное окно facial: 5.9 с.
        t = 0
        t += 1.9
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_hatcher_people_arrive',
            target_name='automarker_cam_hatcher_people_arrive_pos2', duration=14.5, smooth=True)
        cam_hatcher_people_arrive.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=60, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-3.5)


        # Реплика 70 · hatcher · исходное время 51 с
        # Хе, вы тоже были в этом заинтересованы. А кстати, нам как раз нужны такие умелые и предприимчивые люди
        # как вы, для выполнения, скажем так, нестандартных заданий. Вы в ближайшее время не слишком заняты?
        # Исходное окно facial: 12.6 с.
        t = 0
        t += 1.5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=5,
            time_scale=0.5, trans_time=1)
        t += 7.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=5,
            time_scale=0.5, trans_time=1)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_alaric_near', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_alaric', duration=2, smooth=True)
        t += 3
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_hatcher_front', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_hatcher_front', duration=3, smooth=True)
        hatcher.facial(group=MAIN, index=70, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(1.4)


        # Реплика 80 · alaric · исходное время 65 с
        # Для вас мы всегда...
        # Исходное окно facial: 6 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_alaric_near', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_alaric', duration=0.5, smooth=True)
        cam_alaric_near.set(group=MAIN, time_delay=t)
        alaric.facial(group=MAIN, index=80, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-4)


        # Реплика 90 · trent · исходное время 67 с
        # Заткнись, Аларик. Нет, с тех пор как мы стали врагами Рейнландского государства, работы у нас
        # поубавилось.
        # Исходное окно facial: 10 с.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_hatcher', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_hatcher', duration=1, smooth=True)
        t += 5.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_hatcher_front', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1, smooth=True)
        trent.facial(group=MAIN, index=90, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-3)


        # Реплика 100 · hatcher · исходное время 74 с
        # То есть если у нас найдется пара заданий по вашему профилю за достойную плату...
        # Исходное окно facial: 8.5 с.
        t = 0
        cam_hatcher_near.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CROSS_ARMS_000LV_xa_03, duration=5,
            time_scale=0.8, trans_time=1)
        hatcher.facial(group=MAIN, index=100, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.5)


        # Реплика 110 · trent · исходное время 80 с
        # То мы не против их выполнить, если конечно же эти задания не приведут к тому что мы станем
        # государственными преступниками и в Либерти.
        # Исходное окно facial: 10 с.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=110, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.5)


        # Реплика 120 · hatcher · исходное время 88.5 с
        # О, нет, я думаю до этого не дойдет.
        # Исходное окно facial: 6 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_trent_near', duration=2, smooth=True)
        cam_hatcher_near.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_UNCRSS_ARMS_000LV_XA_03, duration=5,
            time_scale=0.8)
        t += 2.5
        cam_trent_near.set(group=MAIN, time_delay=t)
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WALK_TRNS_270LV_XA_02, duration=4, trans_time=2)
        hatcher.facial(group=MAIN, index=120, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-3.25)


        # Реплика 130 · trent · исходное время 91.25 с
        # Я вот тоже думал...
        # Исходное окно facial: 1.75 с.
        t = 0
        trent.facial(group=MAIN, index=130, append=True, auto_lip=True, extra_delay=0)
        t = 0
        trent.motion(group=MAIN, time_delay=t, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, duration=6, trans_time=0.25)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WALK_TRNS_270LV_XA_02, duration=2, trans_time=2)
        t += 1.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_hatcher_front', duration=0.1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_hatcher_front', duration=0.1, smooth=True)
        t += 1.0
        cam_hatcher_final.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_marker_bar_exitpoint', duration=5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_marker_bar_exitpoint', duration=3, smooth=True)
        t += 0.001
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', target_name='offscreen', duration=0.001,
            smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_alaric', target_name='offscreen', duration=0.001,
            smooth=False)
        t += 0.499
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_hatcher', angle=-45, axis='Y_AXIS',
            duration=2, smooth=True)
        t += 1.5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CROSS_ARMS_000LV_xa_03, duration=5,
            time_scale=0.8, trans_time=1)
        main_group.append_time(7.0)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M04HatcherScene
