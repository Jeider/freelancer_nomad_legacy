"""m04_offer: постановка для ручного редактирования.

Точки: SCENES/m04_offer.blend → DUMPS/m04_offer.json.
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
    RotateAxisEvent,
    Sound,
    SoundEvent,
)
from story.cutscenes.anim import (
    Male,
    Trent,
)
from story.cutscenes.source_extensions import (
    preserve_entity,
)
from story import actors


class ExtraCharTrooper1(actors.Actor):
    NAME = 'trooper1'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'ms4_trooper1'
    GAME_ACTOR = 'Trooper1'


class ExtraCharTrooper2(actors.Actor):
    NAME = 'trooper2'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'ms4_trooper2'
    GAME_ACTOR = 'Trooper2'



class M04OfferScene(Scene):
    DUMP_FILE = 'm04_offer'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        DX_m04_offer_0070_trent = Sound(root=self, name='DX_m04_offer_0070_trent', sound='DX_m04_offer_0070_trent',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m04_offer_0070_trent, userprops={'category': 'Audio'})
        DX_m04_offer_0080_jacobo = Sound(root=self, name='DX_m04_offer_0080_jacobo', sound='DX_m04_offer_0080_jacobo',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m04_offer_0080_jacobo, userprops={'category': 'Audio'})
        DX_m04_offer_0090_trent = Sound(root=self, name='DX_m04_offer_0090_trent', sound='DX_m04_offer_0090_trent',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m04_offer_0090_trent, userprops={'category': 'Audio'})
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'actor': 'Player', 'category': 'Character'})
        trooper1 = Character(root=self, actor=ExtraCharTrooper1, light_group=0, init_point='Char_trooper1',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(trooper1, template_name='ms4_trooper1', userprops={'actor': 'Trooper1', 'category': 'Character'})
        trooper2 = Character(root=self, actor=ExtraCharTrooper2, light_group=0, init_point='Char_trooper2',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(trooper2, template_name='ms4_trooper2', userprops={'actor': 'Trooper2', 'category': 'Character'})
        jacobo = Character(root=self, actor=actors.Jacobo, light_group=0, init_point='Char_jacobo', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(jacobo, template_name='jacobo', userprops={'category': 'Character', 'actor': 'jacobo'})
        cam_start = LookAtCamera(root=self, name='cam_start', fov=20, farplane=5000, look_duration=300)
        preserve_entity(cam_start)
        cam_search = LookAtCamera(root=self, name='cam_search', fov=25, farplane=5000, look_duration=300)
        preserve_entity(cam_search)
        cam_jacobo_appear = LookAtCamera(root=self, name='cam_jacobo_appear', fov=22, farplane=5000, look_duration=300)
        preserve_entity(cam_jacobo_appear)
        cam_jacobo_sitting = LookAtCamera(root=self, name='cam_jacobo_sitting', fov=16, farplane=5000, look_duration=300)
        preserve_entity(cam_jacobo_sitting)
        cam_trent_sitting = LookAtCamera(root=self, name='cam_trent_sitting', fov=16, farplane=5000, look_duration=300)
        preserve_entity(cam_trent_sitting)

        # Вход / начальная постановка.
        t = 0
        cam_start.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_start', target_name='automarker_cam_start_pos2',
            duration=10, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_start_focus',
            target_name='automarker_cam_start_marker_pos2', duration=10, smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=1.3, loop=True)
        t += 1.3
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=15)
        t += 1.7
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trooper1', anim=Male.Sc_MLBODY_WLKG_000LV_XB_01,
            duration=15, loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trooper2', anim=Male.Sc_MLBODY_WLKG_000LV_XA_01,
            duration=15, start_time=1, loop=True)
        t += 0.6
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_1STEP_SIDWYSL_000LV_XA_02, duration=15)
        t += 2.4
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_1STEP_BKWD_PVOTR_090LV_XA_06, duration=15)
        t += 4
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_start_focus',
            target_name='automarker_cam_start_marker_pos3', duration=5, smooth=True)
        t += 2
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01, duration=1.1, trans_time=0.25)
        t += 1.1
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=1.89, loop=True,
            trans_time=0.001)
        t += 1.9
        cam_search.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_search', target_name='automarker_cam_search_pos2',
            duration=6, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_search_focus',
            target_name='automarker_cam_search_marker_pos2', duration=6, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent',
            target_name='automarker_point_trent_search', duration=0.001, smooth=False)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=3.9, loop=True)
        t += 3.9
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=2.3, trans_time=0.1)
        t += 2.3
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_LOOK_AROU_CASL_000LV_XA_08, duration=6.3)
        t += 5.8
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_head_ik',
            target_name='automarker_head_trent_search', duration=0.1, smooth=True)
        t += 0.5
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_TURN_090LV_XA_02, duration=3, time_scale=0.75,
            trans_time=1)
        t += 1.5
        cam_jacobo_appear.set(group=MAIN, time_delay=t)
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=2.3,
            start_time=0.45)
        t += 0.25
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_jacobo', target_name='automarker_jacobo_head_ik',
            duration=25, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 0.75
        trent.motion(group=MAIN, time_delay=t, anim=Trent.Sc_MLHEAD_MOTION_MOUTH_CLENCH_TRENT_000LV_, duration=1.937)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_jacobo_appear',
            target_name='automarker_cam_jacobo_appear_pos2', duration=6, smooth=True)
        t += 0.5
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=15,
            time_scale=0.75, trans_time=1)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=-15, axis='Y_AXIS', duration=1,
            smooth=True)
        main_group.append_time(32)


        # Реплика 10 · jacobo · исходное время 32 с
        # Герр Трент, это вы?
        # Исходное окно facial: 3 с.
        t = 0
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=0.333)
        t += 1
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_TURN_180LV_XA_04, duration=6, trans_time=1)
        jacobo.facial(group=MAIN, index=10, append=True, auto_lip=True, extra_delay=0)
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_head_ik',
            target_name='automarker_head_trent_sitting', duration=4, smooth=True)
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_SITCL_TRNS_180DN_XA_06, duration=8, trans_time=1)
        main_group.append_time(2)


        # Реплика 20 · jacobo · исходное время 37 с
        # Герр Трент, спасибо что согласились прилететь. У меня неприятности. Меня разыскивают власти Рейнланда.
        # Исходное окно facial: 8.5 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent',
            target_name='automarker_point_trent_sit_around_jacobo', duration=0.001, smooth=False)
        cam_jacobo_sitting.set(group=MAIN, time_delay=t)
        t += 0.0011
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=3)
        t += 1.9989
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_head_ik',
            target_name='automarker_head_trent_sit', duration=2, smooth=True)
        jacobo.facial(group=MAIN, index=20, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.5)


        # Реплика 30 · trent · исходное время 45 с
        # Это я уже понял. И у меня появилось знакомое ощущение что меня очень хотят втянуть в неприятности.
        # Исходное окно facial: 8 с.
        t = 0
        cam_trent_sitting.set(group=MAIN, time_delay=t)
        t += 5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_head_ik',
            target_name='automarker_head_trent_sit', duration=0.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_jacobo_eye_ik',
            target_name='automarker_head_trent_sit', duration=0.5, smooth=True)
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=3, time_scale=2,
            start_time=1, trans_time=1)
        trent.facial(group=MAIN, index=30, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1)


        # Реплика 40 · jacobo · исходное время 52 с
        # Герр Трент, вы не понимаете. Дело исключительной важности. Мне необходимо доставить в Либерти важные
        # документы.
        # Исходное окно facial: 10 с.
        t = 0
        cam_jacobo_sitting.set(group=MAIN, time_delay=t)
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_LOOK_RLLV_A_06, duration=3, time_scale=0.8,
            start_time=1, trans_time=1)
        t += 3
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_HNDS_CASL_000LV_xa_04, duration=4,
            time_scale=0.8, start_time=1, loop=True, trans_time=1)
        t += 1
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_jacobo', target_name='automarker_jacobo_head_ik',
            duration=55, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_jacobo', target_name='automarker_jacobo_eye_ik',
            duration=55, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 3
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, duration=5, time_scale=0.8,
            start_time=1, trans_time=1)
        t += 1
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=15, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_eye_ik',
            duration=15, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_jacobo_sit', duration=0.1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_jacobo_sit', duration=0.1, smooth=True)
        jacobo.facial(group=MAIN, index=40, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1)


        # Реплика 50 · trent · исходное время 61 с
        # Опять меня угораздило вляпаться в шпионские игры... Джакобо, вы в курсе, что в данный момент я работаю на
        # те самые власти Рейнланда, которые вас ищут?
        # Исходное окно facial: 11 с.
        t = 0
        cam_trent_sitting.set(group=MAIN, time_delay=t)
        t += 4
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=4, time_scale=0.6,
            trans_time=1)
        trent.facial(group=MAIN, index=50, append=True, auto_lip=True, extra_delay=0)
        t = 0


        # Реплика 60 · jacobo · исходное время 72 с
        # Герр Трент, вы же фриленсер. Вы не давали никаких присяг. После выполнения задания вас с заказчиком
        # ничего не связывает.
        # Исходное окно facial: 10 с.
        t = 0
        cam_jacobo_sitting.set(group=MAIN, time_delay=t)
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_TALK_HNSTBL_000LV_B_30, duration=26,
            time_scale=0.8, loop=True)
        jacobo.facial(group=MAIN, index=60, append=True, auto_lip=True, extra_delay=0)
        t = 0


        # Реплика 62 · jacobo · исходное время 82 с
        # Герр Трент, если мы сможем доставить эти ОЧЕНЬ важные документы в Либерти, в систему Форбс, нам заплатят
        # очень большие деньги, ОЧЕНЬ большие, понимаете?
        # Исходное окно facial: 10 с.
        t = 0
        jacobo.facial(group=MAIN, index=62, append=True, auto_lip=True, extra_delay=0)
        t = 0


        # Реплика 65 · jacobo · исходное время 92 с
        # У меня одного это скорее всего не получится, но если вы мне поможете...
        # Исходное окно facial: 9 с.
        t = 0
        jacobo.facial(group=MAIN, index=65, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-4)


        # Реплика 67 · jacobo · исходное время 97 с
        # А если вы мне не поможете, меня скорее всего просто убьют...
        # Исходное окно facial: 0 с.
        t = 0
        voice_sound = self.lookup_single_sound(67)
        SoundEvent(root=self, group=MAIN, sound_name=voice_sound.get_nickname())
        t = 0
        t += 1
        jacobo.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=5, trans_time=1)
        main_group.append_time(4.0)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M04OfferScene
