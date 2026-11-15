"""m06_torpedo_alert: постановка для ручного редактирования.

Точки: SCENES/m06_torpedo_alert.blend → DUMPS/m06_torpedo_alert.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — смещение внутри текущего блока; facial()/append_time() двигают часы.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character,
    LookAtCamera,
    MAIN,
    MotionEvent,
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


class ExtraCharLiTrooper01(actors.Actor):
    NAME = 'li_trooper01'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_dread_military_1'
    GAME_ACTOR = 'li_troop01'


class ExtraCharLiTrooper02(actors.Actor):
    NAME = 'li_trooper02'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_dread_military_2'
    GAME_ACTOR = 'li_troop02'


class ExtraCharAssist(actors.Actor):
    NAME = 'assist'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_dread_military_2'
    GAME_ACTOR = 'li_troop03'



class M06TorpedoAlertScene(Scene):
    DUMP_FILE = 'm06_torpedo_alert'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        alarm = Sound(root=self, name='alarm', sound='rtc_klaxon_loop_3', attenuation=-10, dmin=50, dmax=250, priority=None)
        preserve_entity(alarm)
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'Actor': 'Player', 'category': 'Character'})
        hatcher = Character(root=self, actor=actors.Hatcher, light_group=0, init_point='Char_hatcher',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(hatcher, template_name='hatcher', userprops={'actor': 'Hatcher', 'category': 'Character'})
        li_trooper01 = Character(root=self, actor=ExtraCharLiTrooper01, light_group=0, init_point='Char_li_trooper01',
            rotate_from_quat=True, use_ambient=True, floor_height=0)
        preserve_entity(li_trooper01, template_name='m06_dread_military_1',
            userprops={'actor': 'li_troop01', 'category': 'Character'})
        li_trooper02 = Character(root=self, actor=ExtraCharLiTrooper02, light_group=0, init_point='Char_li_trooper02',
            rotate_from_quat=True, use_ambient=True, floor_height=0)
        preserve_entity(li_trooper02, template_name='m06_dread_military_2',
            userprops={'actor': 'li_troop02', 'category': 'Character'})
        assist = Character(root=self, actor=ExtraCharAssist, light_group=0, init_point='Char_assist', rotate_from_quat=True,
            use_ambient=True, floor_height=0)
        preserve_entity(assist, template_name='m06_dread_military_2',
            userprops={'actor': 'li_troop03', 'category': 'Character'})
        cam_start = LookAtCamera(root=self, name='cam_start', fov=20, farplane=5000, look_duration=30)
        preserve_entity(cam_start)
        cam_hatcher = LookAtCamera(root=self, name='cam_hatcher', fov=22, farplane=5000, look_duration=300)
        preserve_entity(cam_hatcher)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=20, farplane=5000, look_duration=1)
        preserve_entity(cam_trent)
        cam_final = LookAtCamera(root=self, name='cam_final', fov=22, farplane=5000, look_duration=111)
        preserve_entity(cam_final)

        # Вход / начальная постановка.
        t = 0
        cam_start.set(group=MAIN, time_delay=t)
        t += 1
        alarm.start(group=MAIN, time_delay=t, duration=40, loop=True)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_start', target_name='automarker_cam_start_pos2',
            duration=10, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_start_focus',
            target_name='automarker_cam_start_marker_pos2', duration=8, smooth=True)
        t += 2
        alarm.change_attenuation(group=MAIN, time_delay=t, duration=2, attenuation=-20)
        t += 2
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_li_trooper01',
            anim=Male.Sc_MLBODY_RNNG_000LV_XA_01, duration=25, time_scale=0.6, loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_li_trooper02',
            anim=Male.Sc_MLBODY_RNNG_000LV_XA_01, duration=25, time_scale=0.6, start_time=0.4, loop=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=7, start_time=0.73, loop=True)
        t += 4
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=29.5, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 2
        hatcher.motion(group=MAIN, time_delay=t, anim=Male.GENERIC_ANIM, duration=10, time_scale=0.8, trans_time=0.25)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_HNDS_EMPH_000LV_XA_04, duration=3,
            loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_assist',
            anim=Male.Sc_MLBODY_STND_FSTHIPB_HOLD_000LV_XA_02, duration=3, loop=True)
        alarm.change_attenuation(group=MAIN, time_delay=t, duration=2, attenuation=-40)
        t += 1
        cam_hatcher.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_hatcher', target_name='automarker_cam_hatcher_pos2',
            duration=11, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_hatcher_focus',
            target_name='automarker_cam_hatcher_marker_pos2', duration=11, smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=4, trans_time=0.1)
        t += 2
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_ATEASE_HSEC_RLEASE_000LV_XA_03, duration=3,
            trans_time=1)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_EMPH_HNDSDN_TRNS_000LV_XA_01, duration=5,
            trans_time=0.5)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_assist',
            anim=Male.Sc_MLBODY_STND_SALUT_000LV_XA_03, duration=5, time_scale=1.25, trans_time=0.8)
        t += 1
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_POINTR_OVRTHRE_000LV_XA_02, duration=5,
            trans_time=0.5)
        t += 1
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_assist',
            anim=Male.Sc_MLBODY_STND_WALK_TRNS_270LV_XA_02, duration=2, trans_time=1)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_assist', angle=15, axis='Y_AXIS', duration=2,
            smooth=True)
        t += 1
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_TURN_270LV_XA_03, duration=5, trans_time=1)
        t += 1
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_assist', anim=Male.Sc_MLBODY_WLKG_000LV_XA_01,
            duration=1, loop=True)
        main_group.append_time(20)


        # Реплика 10 · hatcher · исходное время 20 с
        # Трент, у нас критическая ситуация! Рейнландцы выпустили против Миссури торпедные канонерки.
        # Исходное окно facial: 6.5 с.
        t = 0
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_assist', anim=Male.Sc_MLBODY_WLKG_000LV_XA_01,
            duration=15, time_scale=2, start_time=1, loop=True)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_hatcher', target_name='automarker_hatcher_head_ik',
            duration=35, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        alarm.change_attenuation(group=MAIN, time_delay=t, duration=10, attenuation=-100)
        t += 1
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05, duration=3, loop=True,
            trans_time=1)
        t += 3
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_HNDSUP_TRNS_000LV_XA_01, duration=5,
            trans_time=0.5)
        t += 1
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHEAD_BASEPOSE_000LV_02_01, duration=0.5, trans_time=0.5)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_HNDS_CASL_000LV_xa_03, duration=4,
            loop=True, trans_time=1)
        hatcher.facial(group=MAIN, index=10, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.0)


        # Реплика 20 · hatcher · исходное время 25.5 с
        # Мы не успеваем запустить гипердвигатель, а системы ПВО линкора не смогут перехватить все выпущенные
        # торпеды.
        # Исходное окно facial: 5.8 с.
        t = 0
        t += 3.5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_HNDSDN_TRNS_000LV_XA_01, duration=5,
            trans_time=0.5)
        t += 1.9
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHEAD_BASEPOSE_000LV_02_01, duration=1, trans_time=1)
        hatcher.facial(group=MAIN, index=20, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.3)


        # Реплика 40 · trent · исходное время 31 с
        # Но сначала нужно выгрузить артефакты.
        # Исходное окно facial: 15 с.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_ATEASE_RLEASE_000LV_XA_01, duration=5,
            time_scale=0.6, trans_time=1)
        trent.facial(group=MAIN, index=40, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-12)


        # Реплика 50 · hatcher · исходное время 34 с
        # В данной ситуации они большей безопасности у вас на борту, а не на Миссури. Вылетайте! Быстрее!
        # Исходное окно facial: 7 с.
        t = 0
        cam_final.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_HNDSUP_TRNS_000LV_XA_01, duration=5,
            trans_time=0.5)
        t += 1
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_HNDS_CASL_000LV_xa_03, duration=3.5,
            loop=True, trans_time=1)
        t += 3.5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_HNDSDN_TRNS_000LV_XA_01, duration=0.5,
            trans_time=0.5)
        hatcher.facial(group=MAIN, index=50, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.5)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M06TorpedoAlertScene
