"""m05_piratebar: постановка для ручного редактирования.

Точки: SCENES/m05_piratebar.blend → DUMPS/m05_piratebar.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — смещение внутри текущего блока; facial()/append_time() двигают часы.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Alchemy,
    Character,
    ConnectHardpointEvent,
    LookAtCamera,
    MAIN,
    MoveEvent,
    NeckIkEvent,
    Prop,
    RotateAxisEvent,
)
from story.cutscenes.anim import (
    Male,
    Trent,
)
from story.cutscenes.source_extensions import (
    SourceAttachEvent,
    preserve_entity,
)
from story import actors


class PropPropCigarette2(Prop):
    COMPOUND_TEMPLATE_NAME = 'cigarette_2'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropPda(Prop):
    COMPOUND_TEMPLATE_NAME = 'pda'
    SRT_GRP = 0
    USR_FLG = 0



class M05PiratebarScene(Scene):
    DUMP_FILE = 'm05_piratebar'
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
        prop_pda = PropPropPda(root=self, name='prop_pda', light_group=0, init_point='prop_pda', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(prop_pda, userprops={'category': 'Prop'})
        smith = Character(root=self, actor=actors.Smith, light_group=0, init_point='Char_smith', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(smith, template_name='m05_smith', userprops={'actor': 'm05_smith', 'category': 'Character'})
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'Actor': 'Player', 'category': 'Character'})
        cam_start = LookAtCamera(root=self, name='cam_start', fov=20, farplane=5000, look_duration=300)
        preserve_entity(cam_start)
        cam_trent_stand = LookAtCamera(root=self, name='cam_trent_stand', fov=20, farplane=5000, look_duration=300)
        preserve_entity(cam_trent_stand)
        cam_smith = LookAtCamera(root=self, name='cam_smith', fov=18, farplane=5000, look_duration=300)
        preserve_entity(cam_smith)
        cam_smith_far = LookAtCamera(root=self, name='cam_smith_far', fov=20, farplane=5000, look_duration=300)
        preserve_entity(cam_smith_far)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=18, farplane=5000, look_duration=300)
        preserve_entity(cam_trent)
        cam_trough = LookAtCamera(root=self, name='cam_trough', fov=30, farplane=5000, look_duration=300)
        preserve_entity(cam_trough)
        cam_trent_sidetalk = LookAtCamera(root=self, name='cam_trent_sidetalk', fov=18, farplane=5000, look_duration=300)
        preserve_entity(cam_trent_sidetalk)

        # Вход / начальная постановка.
        t = 0
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['vfx_rtc_sydsmoke_3', 'prop_cigarette_2'],
            duration=200, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HP_cigarette_Tip_smoke',
            target_type='HARDPOINT', flags='POSITION')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['vfx_rtc_cigaretteglow_4', 'prop_cigarette_2'],
            duration=200, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HP_cigarette_Tip_smoke',
            target_type='HARDPOINT', flags='POSITION+ORIENTATION')
        vfx_rtc_cigaretteglow_4.start(group=MAIN, time_delay=t, duration=105)
        vfx_rtc_sydsmoke_3.start(group=MAIN, time_delay=t, duration=105)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_NEUT_LEFT_000LV_A_00, duration=5)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_NEUT_RGHT_000LV_A_00, duration=5)
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='prop_cigarette_2', parent_name='Char_smith',
            duration=105, target_hardpoint='hprightconnect_cigarette2', parent_hardpoint='hprightconnect')
        cam_start.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_start', target_name='automarker_cam_start_pos2',
            duration=8, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_start_focus',
            target_name='automarker_cam_start_marker_pos2', duration=8, smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=3.9, loop=True)
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_POINT_RGHT_MILI_000LV_00, duration=0.5,
            time_scale=10)
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, duration=2)
        t += 1
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=2, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 1
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_GRABR_CHIN_RLEASE_000LV_XA_02, duration=5,
            trans_time=0.3)
        t += 1.9
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=3)
        t += 0.1
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CHIN_HOLDR_000LV_XA_03, duration=4, loop=True)
        t += 2.2
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_TURN_270LV_XA_04, duration=4, trans_time=0.25)
        t += 0.8
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=24, transition_duration=2, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=45, axis='Y_AXIS', duration=2,
            smooth=True)
        t += 1
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_HOLD_CHIN_RLEASE_000LV_XA_03, duration=15,
            trans_time=1)
        t += 1
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_NEUT_RGHT_000LV_A_00, duration=5, trans_time=1)
        main_group.append_time(10)


        # Реплика 10 · trent · исходное время 10 с
        # Хай, бро! Есть чо? А то я тут с такого дальняка вернулся, что все мозги закисли, расслабиться бы...
        # Исходное окно facial: 8 с.
        t = 0
        cam_trent_stand.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WAVE_RHND_000LV_XA_02, duration=1.5, time_scale=0.7,
            trans_time=0.25)
        t += 1.5
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_TALK_SMALL_000DN_A_17, duration=6.5,
            time_scale=0.75, trans_time=2)
        t += 0.5
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=25, axis='Y_AXIS',
            duration=2.5, smooth=True)
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_GRABR_CHIN_RLEASE_000LV_XA_02, duration=5)
        t += 4
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_POINT_RGHT_MILI_000LV_00, duration=0.5,
            time_scale=10)
        t += 0.5
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CHIN_HOLDR_000LV_XA_03, duration=1.5, loop=True)
        t += 0.5
        cam_smith_far.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=10, append=True, auto_lip=True, extra_delay=0)
        t = 0
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_HOLD_CHIN_RLEASE_000LV_XA_03, duration=15,
            trans_time=1)
        main_group.append_time(0.5)


        # Реплика 20 · smith · исходное время 18.5 с
        # Та не, откуда, сам с пятого на десятое перебиваюсь.
        # Исходное окно facial: 5.5 с.
        t = 0
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_NEUT_RGHT_000LV_A_00, duration=5, trans_time=1)
        t += 1.5
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_smith', target_name='automarker_smith_head_ik',
            duration=7, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 3.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_smith_head_ik',
            target_name='automarker_head_smith_front_btm', duration=2, smooth=True)
        smith.facial(group=MAIN, index=20, append=True, auto_lip=True, extra_delay=0)
        t = 0
        cam_trent_stand.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_out_window_center', duration=1, smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=5,
            time_scale=0.7, trans_time=1)
        main_group.append_time(1.0)


        # Реплика 30 · trent · исходное время 25 с
        # Вот же козлы все эти пиджаки из ДипСпейс. Я им работу сработал, а они мне на Детройте даже посадку не
        # дали, типа мордой не вышел, пропуска нет.
        # Исходное окно facial: 15 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_smith_head_ik',
            target_name='automarker_head_smith_front', duration=1.5, smooth=True)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_smith', duration=2, smooth=True)
        t += 1
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=5,
            time_scale=0.5, trans_time=1)
        t += 1
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_POINT_RGHT_MILI_000LV_00, duration=0.5,
            time_scale=10)
        t += 1
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_SITCL_TRNS_180DN_XA_06, duration=3.4,
            time_scale=0.85, trans_time=0.25)
        t += 3
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, duration=2)
        t += 0.4
        cam_trough.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_trough', target_name='automarker_cam_trough_pos2',
            duration=15, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_trough_focus',
            target_name='automarker_cam_trough_marker_pos2', duration=15, smooth=True)
        t += 0.0001
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent',
            target_name='automarker_point_trent_sit_side', duration=0.001, smooth=False)
        t += 0.0001
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_TALK_000LV_A_16, duration=15.1, time_scale=0.75,
            loop=True)
        trent.facial(group=MAIN, index=30, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-6.5)


        # Реплика 40 · trent · исходное время 33.5 с
        # А у меня там заначка козырная, месяц оттопыриваться можно - из омикронов привез, дельце там одно
        # провернул.
        # Исходное окно facial: 15 с.
        t = 0
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_TAP_RHND_000LV_A_02, duration=5.5, time_scale=0.7,
            loop=True, trans_time=0.25)
        t += 5.5
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_GRABR_CHIN_RLEASE_000LV_XA_02, duration=5,
            trans_time=0.3)
        trent.facial(group=MAIN, index=40, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-8.5)


        # Реплика 50 · trent · исходное время 40 с
        # А теперь из-за этой мать ее боевой готовности сидеть тут пойлом местным травиться...  А когда она еще
        # закончится, готовность эта...
        # Исходное окно facial: 15 с.
        t = 0
        t += 1
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CHIN_HOLDR_000LV_XA_03, duration=3, loop=True)
        t += 3
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_HOLD_CHIN_RLEASE_000LV_XA_03, duration=15,
            trans_time=1)
        t += 1
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_NEUT_RGHT_000LV_A_00, duration=5, trans_time=1)
        trent.facial(group=MAIN, index=50, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-6.5)


        # Реплика 55 · trent · исходное время 48.5 с
        # Эх, пропуск бы где раздобыть, я бы сундучок-то свой оттуда выцепил бы, оттянулись бы по полной...
        # Исходное окно facial: 18 с.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_TWSTU_CLOC_LESS_000LV_A_14, duration=25,
            time_scale=0.75, start_time=9)
        t += 7.5
        cam_smith.set(group=MAIN, time_delay=t)
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_HOLD_CHIN_RLEASE_000LV_XA_03, duration=15)
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=3, time_scale=0.4,
            trans_time=0.25)
        trent.facial(group=MAIN, index=55, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-7.5)


        # Реплика 60 · smith · исходное время 59 с
        # Слыш, это, дружище... Тебя как зовут?
        # Исходное окно facial: 5.75 с.
        t = 0
        t += 2.5
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_GRABR_CHIN_RLEASE_000LV_XA_02, duration=5,
            trans_time=0.3)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent',
            target_name='automarker_point_trent_sit_side', duration=0.001, smooth=False)
        t += 0.2
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=1)
        t += 1.3
        cam_trent_sidetalk.set(group=MAIN, time_delay=t)
        t += 0.5
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=10, transition_duration=2, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 0.5
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=-90, axis='Y_AXIS', duration=2,
            smooth=True)
        smith.facial(group=MAIN, index=60, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(0.25)


        # Реплика 70 · trent · исходное время 65 с
        # Трент. а тебя как?
        # Исходное окно facial: 3 с.
        t = 0
        t += 0.5
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=3, time_scale=0.92,
            trans_time=0.25)
        t += 0.5
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, duration=2)
        trent.facial(group=MAIN, index=70, append=True, auto_lip=True, extra_delay=0)
        t = 0
        cam_smith_far.set(group=MAIN, time_delay=t)
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, duration=5)
        main_group.append_time(0.5)


        # Реплика 80 · smith · исходное время 68.5 с
        # Смит. Мистер Смит.
        # Исходное окно facial: 4 с.
        t = 0
        smith.facial(group=MAIN, index=80, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.5)


        # Реплика 90 · trent · исходное время 72 с
        # Приятно познакомитьcя. Мистер Смит, ты там что-то сказать хотел.
        # Исходное окно facial: 5 с.
        t = 0
        cam_trent_sidetalk.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, duration=0.2)
        t += 0.8
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDUP_TRNS_000LV_XA_02, duration=4,
            trans_time=0.25)
        t += 1.5
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDDN_TRNS_000LV_XA_02, duration=3,
            time_scale=0.8, trans_time=0.25)
        trent.facial(group=MAIN, index=90, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.5)


        # Реплика 100 · smith · исходное время 76.5 с
        # Да? Да. А, Да! Я знаю где можно пропуск достать.
        # Исходное окно facial: 8 с.
        t = 0
        cam_smith.set(group=MAIN, time_delay=t)
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, duration=5)
        cam_smith.set(group=MAIN, time_delay=t)
        t += 0.5
        trent.motion(group=MAIN, time_delay=t, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, duration=8, time_scale=0.6,
            trans_time=1)
        t += 5.0
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, duration=1)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=10, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 1.2
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=8, time_scale=0.6,
            trans_time=1)
        t += 0.8
        cam_trent_sidetalk.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_LEAN_ARMB_000LV_A_10, duration=5, time_scale=0.5)
        smith.facial(group=MAIN, index=100, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(0.5)


        # Реплика 110 · trent · исходное время 85 с
        # Да ты что! И где.
        # Исходное окно facial: 3 с.
        t = 0
        t += 1
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=1)
        trent.facial(group=MAIN, index=110, append=True, auto_lip=True, extra_delay=0)
        t = 0
        cam_smith_far.set(group=MAIN, time_delay=t)
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='prop_pda', parent_name='Char_smith',
            duration=17, target_hardpoint='Hp_LHand_PDA', parent_hardpoint='HpLeftConnect')
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=2)
        main_group.append_time(1)


        # Реплика 120 · smith · исходное время 89 с
        # Смотри. Вот тут склад есть секретный. Там у ребят пара штук на крайний случай точно есть. Я знаю.
        # Попробуй с ними договориться. Только ты это... Никому. Склад-то секретный!
        # Исходное окно facial: 15 с.
        t = 0
        t += 1
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_LHNDUP_TRNS_000LV_XA_02, duration=7,
            time_scale=0.5, trans_time=0.25)
        t += 2.5
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_LHND_CASL_000LV_xa_03, duration=4,
            time_scale=0.5, trans_time=1)
        t += 4.0
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_LHNDDN_TRNS_000LV_XA_02, duration=4,
            time_scale=0.5, trans_time=1)
        t += 3.5
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_LHNDUP_TRNS_000LV_XA_02, duration=7,
            trans_time=0.25)
        t += 2
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=5, time_scale=0.5,
            start_time=1, trans_time=1)
        smith.facial(group=MAIN, index=120, append=True, auto_lip=True, extra_delay=0)
        t = 0
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=4, trans_time=1)
        main_group.append_time(1)


        # Реплика 130 · trent · исходное время 105 с
        # Замётано, бро!
        # Исходное окно facial: 3 с.
        t = 0
        cam_trent_sidetalk.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_WALK_TRNS_270LV_XA_10, duration=5)
        t += 0.1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='prop_cigarette_2', target_name='offscreen',
            duration=0.001, smooth=False)
        t += 0.9
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='prop_pda', target_name='offscreen', duration=0.001,
            smooth=False)
        trent.facial(group=MAIN, index=130, append=True, auto_lip=True, extra_delay=0)
        t = 0
        t += 2
        cam_smith.set(group=MAIN, time_delay=t)
        smith.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_TWSTU_CLOC_LESS_000LV_A_14, duration=25,
            time_scale=0.75, start_time=8)
        t += 1e-05
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', target_name='offscreen', duration=0.001,
            smooth=False)
        main_group.append_time(4)


        # Реплика 140 · smith · исходное время 112 с
        # Ты с сундучком-то забегай...
        # Исходное окно facial: 3 с.
        t = 0
        smith.facial(group=MAIN, index=140, append=True, auto_lip=True, extra_delay=0)
        t = 0
        t += 4
        cam_trent.set(group=MAIN, time_delay=t)
        main_group.append_time(4.0)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M05PiratebarScene
