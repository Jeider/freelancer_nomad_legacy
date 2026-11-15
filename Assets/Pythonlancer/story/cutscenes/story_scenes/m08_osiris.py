"""m08_osiris: постановка для ручного редактирования.

Точки: SCENES/m08_osiris.blend → DUMPS/m08_osiris.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — смещение внутри текущего блока; facial()/append_time() двигают часы.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character,
    ConnectHardpointEvent,
    EyeIkEvent,
    LookAtCamera,
    MAIN,
    MotionEvent,
    MoveEvent,
    NeckIkEvent,
    Prop,
    RotateAxisEvent,
)
from story.cutscenes.anim import (
    Female,
    Male,
)
from story.cutscenes.source_extensions import (
    preserve_entity,
)
from story import actors


class PropChair(Prop):
    COMPOUND_TEMPLATE_NAME = 'm8_osiris_chair'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropTome(Prop):
    COMPOUND_TEMPLATE_NAME = 'tome'
    SRT_GRP = 0
    USR_FLG = 0


class ExtraCharRifleman(actors.Actor):
    NAME = 'rifleman'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm8_asf_rifleman'
    GAME_ACTOR = 'Gunner2'



class M08OsirisScene(Scene):
    DUMP_FILE = 'm08_osiris'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        chair = PropChair(root=self, name='chair', light_group=0, init_point='chair', rotate_from_quat=True,
            use_ambient=True)
        preserve_entity(chair, userprops={'category': 'Prop'})
        prop_tome = PropPropTome(root=self, name='prop_tome', light_group=9, init_point='prop_tome', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(prop_tome, userprops={'category': 'Prop'})
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'Actor': 'Player', 'category': 'Character'})
        king = Character(root=self, actor=actors.King, light_group=0, init_point='Char_king', rotate_from_quat=True,
            use_ambient=True, floor_height=0)
        preserve_entity(king, template_name='king', userprops={'Actor': 'King', 'category': 'Character'})
        major = Character(root=self, actor=actors.MajorScrew, light_group=0, init_point='Char_major', rotate_from_quat=True,
            use_ambient=True, floor_height=0)
        preserve_entity(major, template_name='major_screw', userprops={'Actor': 'Major_Screw', 'category': 'Character'})
        hatcher = Character(root=self, actor=actors.Hatcher, light_group=0, init_point='Char_hatcher',
            rotate_from_quat=True, use_ambient=True, floor_height=0)
        preserve_entity(hatcher, template_name='hatcher', userprops={'actor': 'Hatcher', 'category': 'Character'})
        captain = Character(root=self, actor=actors.MaleCaptain, light_group=0, init_point='Char_captain',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(captain, template_name='m8_asf_captain', userprops={'Actor': 'Gunner', 'category': 'Character'})
        rifleman = Character(root=self, actor=ExtraCharRifleman, light_group=0, init_point='Char_rifleman',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(rifleman, template_name='m8_asf_rifleman', userprops={'Actor': 'Gunner2', 'category': 'Character'})
        cam_start = LookAtCamera(root=self, name='cam_start', fov=20, farplane=5000, look_duration=70)
        preserve_entity(cam_start)
        cam_start_hatcher = LookAtCamera(root=self, name='cam_start_hatcher', fov=15, farplane=5000, look_duration=70)
        preserve_entity(cam_start_hatcher)
        cam_king_first = LookAtCamera(root=self, name='cam_king_first', fov=15, farplane=5000, look_duration=70)
        preserve_entity(cam_king_first)
        cam_trent_sits_down = LookAtCamera(root=self, name='cam_trent_sits_down', fov=15, farplane=5000, look_duration=70)
        preserve_entity(cam_trent_sits_down)
        cam_king_far = LookAtCamera(root=self, name='cam_king_far', fov=15, farplane=5000, look_duration=70)
        preserve_entity(cam_king_far)
        cam_king_near = LookAtCamera(root=self, name='cam_king_near', fov=12, farplane=5000, look_duration=120)
        preserve_entity(cam_king_near)
        cam_trent_near = LookAtCamera(root=self, name='cam_trent_near', fov=12, farplane=5000, look_duration=120)
        preserve_entity(cam_trent_near)
        cam_major_near = LookAtCamera(root=self, name='cam_major_near', fov=12, farplane=5000, look_duration=120)
        preserve_entity(cam_major_near)
        cam_trent_artifact = LookAtCamera(root=self, name='cam_trent_artifact', fov=15, farplane=5000, look_duration=120)
        preserve_entity(cam_trent_artifact)
        cam_trent_decline = LookAtCamera(root=self, name='cam_trent_decline', fov=12, farplane=5000, look_duration=200)
        preserve_entity(cam_trent_decline)
        cam_trent_reaction = LookAtCamera(root=self, name='cam_trent_reaction', fov=15, farplane=5000, look_duration=200)
        preserve_entity(cam_trent_reaction)
        cam_hatcher_sad = LookAtCamera(root=self, name='cam_hatcher_sad', fov=15, farplane=5000, look_duration=200)
        preserve_entity(cam_hatcher_sad)

        # Вход / начальная постановка.
        t = 0
        cam_start.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_start', target_name='automarker_cam_start_pos2',
            duration=7, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_start_focus',
            target_name='automarker_cam_start_marker_pos2', duration=7, smooth=True)
        major.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_HOLD_ARMS_CROSSED_000LV_XA_02, duration=1)
        king.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_LEAN_ARMB_090LV_A_08, duration=0.1, start_time=2.5)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_rifleman',
            anim=Male.Sc_MLBODY_STND_HOLD_RIFLE_MILI_000LV_XA_05, duration=100, loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_captain',
            anim=Female.Sc_FMBODY_WALK_HOLD_GUN_RHAND_000LV_XB_01, duration=7, time_scale=0.8, loop=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=7, time_scale=0.8, loop=True)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_WLKG_000LV_XA_01, duration=7, time_scale=0.8,
            loop=True)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_hatcher', angle=6, axis='Y_AXIS', duration=6,
            smooth=False)
        t += 0.01
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_king', angle=-140, axis='Y_AXIS', duration=0,
            smooth=False)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_rifleman', angle=30, axis='Y_AXIS',
            duration=0, smooth=False)
        t += 0.19
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_rifleman', target_name='Char_captain', duration=15,
            transition_duration=3, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 1.8
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_king', target_name='automarker_king_head_ik',
            duration=500, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_king', target_name='automarker_king_eye_ik',
            duration=500, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 1
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_hatcher', target_name='automarker_hatcher_head_ik',
            duration=2555, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_hatcher', target_name='automarker_hatcher_eye_ik',
            duration=2555, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 4
        cam_start_hatcher.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_WALK_STND_TRNS_000LV_XA_01, duration=15,
            time_scale=0.8)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_hatcher', angle=-15, axis='Y_AXIS',
            duration=2, smooth=False)
        main_group.append_time(8.5)


        # Реплика 10 · hatcher · исходное время 8.5 с
        # Майо... эээ... Простите, генерал Кинг, майор Скрю, Трент доставлен.
        # Исходное окно facial: 25 с.
        t = 0
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_king', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_king', duration=1.5, smooth=True)
        t += 0.5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_SALUT_000LV_XA_03, duration=10, start_time=0.5,
            trans_time=1)
        t += 2.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_major', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_major', duration=1.5, smooth=True)
        hatcher.facial(group=MAIN, index=10, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-19.5)


        # Реплика 20 · king · исходное время 14 с
        # Спасибо, мисс Хетчер.
        # Исходное окно facial: 6 с.
        t = 0
        cam_king_first.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_king_first',
            target_name='automarker_cam_king_first_pos2', duration=8, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_king_first_focus',
            target_name='automarker_cam_king_first_marker_pos2', duration=8, smooth=True)
        major.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_A_11, duration=50, time_scale=0.2,
            start_time=1, loop=True)
        king.facial(group=MAIN, index=20, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-4)


        # Реплика 30 · king · исходное время 16 с
        # Мистер Трент, я понимаю, что у вас выдались тяжелые... гхм... несколько дней...
        # Исходное окно facial: 12 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_king_head_ik',
            target_name='automarker_head_trent', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_king_eye_ik',
            target_name='automarker_head_trent', duration=1.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_captain',
            target_name='automarker_point_captain_aim', duration=0, smooth=False)
        t += 0.1
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_captain',
            anim=Female.Sc_FMBODY_CHRB_LSTN_000LV_A_08, duration=200, time_scale=0.4, loop=True)
        t += 0.1
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_captain', target_name='automarker_head_trent',
            duration=15, transition_duration=3, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 1.3
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent',
            target_name='automarker_point_trent_stand_to_sit', duration=0, smooth=False)
        t += 0.01
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=50, axis='Y_AXIS', duration=0,
            smooth=False)
        t += 0.99
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_SITCR_TRNS_090DN_XA_07, duration=15, start_time=1)
        t += 2.0
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=20, axis='Y_AXIS', duration=1,
            smooth=False)
        t += 1.5
        cam_trent_sits_down.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_king',
            target_name='automarker_point_king_talk_front', duration=0, smooth=False)
        t += 0.1
        king.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=0.1)
        t += 0.1
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_king', angle=-20, axis='Y_AXIS', duration=0,
            smooth=False)
        king.facial(group=MAIN, index=30, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-5.5)


        # Реплика 40 · trent · исходное время 22.5 с
        # Недель...
        # Исходное окно facial: 6 с.
        t = 0
        trent.facial(group=MAIN, index=40, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-3.5)


        # Реплика 50 · king · исходное время 25 с
        # Пусть даже месяцев, но есть некоторые вещи, которые выше нашего морального и физического состояния. И в
        # данный момент очень важно определить местонахождение известного вам тома Протеуса и ключа.
        # Исходное окно facial: 23 с.
        t = 0
        cam_king_far.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_king_far',
            target_name='automarker_cam_king_far_pos2', duration=26, smooth=True)
        king.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=5,
            time_scale=0.4, trans_time=1)
        t += 10
        king.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=5,
            time_scale=0.4, trans_time=1)
        king.facial(group=MAIN, index=50, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-9)


        # Реплика 60 · king · исходное время 39 с
        # А поэтому, расскажите, пожалуйста, подробно всё, что происходило с вами с момента когда мисс Хетчер
        # приказала вам вместе с отрядом Дельта отправиться в Сигму-17.
        # Исходное окно facial: 17 с.
        t = 0
        t += 1
        king.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, duration=5, time_scale=0.4,
            trans_time=2)
        t += 10
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=555, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        king.facial(group=MAIN, index=60, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-5.5)


        # Реплика 70 · trent · исходное время 50.5 с
        # Нас перехватили в Большом Омикроне, до сигмы-17 мы так и не добрались.
        # Исходное окно facial: 6 с.
        t = 0
        cam_trent_sits_down.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=70, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.7)


        # Реплика 80 · king · исходное время 54.8 с
        # Кто перехватил?
        # Исходное окно facial: 12 с.
        t = 0
        cam_king_near.set(group=MAIN, time_delay=t)
        t += 1.2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', target_name='automarker_point_trent_sit',
            duration=0, smooth=False)
        t += 0.1
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=100, time_scale=0.6,
            loop=True)
        king.facial(group=MAIN, index=80, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-10.3)


        # Реплика 90 · trent · исходное время 56.5 с
        # Да хрен его знает, какие-то бравые ребята с линкора под названием "Навухудоноссор". А потом нам помог с
        # него сбежать капитан Сид.
        # Исходное окно facial: 10 с.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        t += 1.5
        major.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_HOLD_ARMS_CROSSED_000LV_XA_02, duration=1,
            trans_time=1)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_major', target_name='automarker_major_head_ik',
            duration=555, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_major', target_name='automarker_major_eye_ik',
            duration=555, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        trent.facial(group=MAIN, index=90, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.5)


        # Реплика 100 · king · исходное время 64 с
        # Капитан Сид...
        # Исходное окно facial: 12 с.
        t = 0
        cam_king_far.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_king_head_ik',
            target_name='automarker_head_major_front_far', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_king_eye_ik',
            target_name='automarker_head_major_front_near', duration=1.5, smooth=True)
        t += 1.7
        cam_major_near.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_major_head_ik',
            target_name='automarker_head_king_front_far', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_major_eye_ik',
            target_name='automarker_head_king_front_near', duration=1.5, smooth=True)
        king.facial(group=MAIN, index=100, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-10)


        # Реплика 110 · major · исходное время 66 с
        # Капитан Сид...
        # Исходное окно facial: 12 с.
        t = 0
        major.facial(group=MAIN, index=110, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-10)


        # Реплика 120 · trent · исходное время 68 с
        # Потом со мной вышел на контакт агент Рокфорд. Или это я с ним на контакт вышел...
        # Исходное окно facial: 6 с.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_king_head_ik',
            target_name='automarker_head_trent', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_king_eye_ik',
            target_name='automarker_head_trent', duration=1.5, smooth=True)
        trent.facial(group=MAIN, index=120, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1)


        # Реплика 130 · king · исходное время 73 с
        # Рокфорд?
        # Исходное окно facial: 12 с.
        t = 0
        cam_king_near.set(group=MAIN, time_delay=t)
        king.facial(group=MAIN, index=130, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-11)


        # Реплика 140 · trent · исходное время 74 с
        # Рокфорд. И он помог мне вернуть артефакты. Но позже оказалось, что вернуть он их хотел себе, а меня
        # попытался уничтожить. (прикол жеж, удалось почти) И это ему почти удалось.
        # Исходное окно facial: 14 с.
        t = 0
        cam_trent_artifact.set(group=MAIN, time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_major_right', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_major_right', duration=1.5, smooth=True)
        t += 3
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_leaders_middle', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_leaders_middle', duration=1.5, smooth=True)
        trent.facial(group=MAIN, index=140, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-4)


        # Реплика 145 · trent · исходное время 84 с
        # В итоге, в последний момент я ускользнул от него и спас вот это:
        # Исходное окно facial: 6 с.
        t = 0
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_major_right', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_major_right', duration=1.5, smooth=True)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_trent_artifact_focus',
            target_name='automarker_cam_trent_artifact_marker_pos2', duration=5, smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_GESTR_RGHT_000LV_XA_03, duration=4, time_scale=0.15,
            trans_time=0.5)
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='prop_tome', parent_name='Char_trent',
            duration=20, target_hardpoint='rhand_connect_tome', parent_hardpoint='hprightconnect')
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_HOLDD_RGHT_000LV_00, duration=1, time_scale=5)
        t += 2.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_leaders_middle_bottom', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_leaders_middle_bottom', duration=1.5, smooth=True)
        trent.facial(group=MAIN, index=145, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(1)


        # Реплика 150 · king · исходное время 91 с
        # Значит Рокфорд в курсе
        # Исходное окно facial: 12 с.
        t = 0
        cam_king_near.set(group=MAIN, time_delay=t)
        t += 2.3
        cam_major_near.set(group=MAIN, time_delay=t)
        king.facial(group=MAIN, index=150, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-9.6)


        # Реплика 160 · major · исходное время 93.4 с
        # И в игре...
        # Исходное окно facial: 12 с.
        t = 0
        major.facial(group=MAIN, index=160, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-10.6)


        # Реплика 170 · king · исходное время 94.8 с
        # И в игре... пока... (серьёзно) Нужно это исправить.
        # Исходное окно facial: 12 с.
        t = 0
        cam_king_near.set(group=MAIN, time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_king_head_ik',
            target_name='automarker_head_major_front_far', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_king_eye_ik',
            target_name='automarker_head_major_front_near', duration=1.5, smooth=True)
        king.facial(group=MAIN, index=170, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-8.1)


        # Реплика 180 · major · исходное время 98.7 с
        # В данный момент он скорее всего где-то в штате Нового Ордена. Нам нужен агент в Новом Ордене. Агент,
        # который вычислит его местонахождение.
        # Исходное окно facial: 16 с.
        t = 0
        cam_major_near.set(group=MAIN, time_delay=t)
        t += 1.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_major_head_ik',
            target_name='automarker_head_hatcher', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_major_eye_ik',
            target_name='automarker_head_hatcher', duration=1.8, smooth=True)
        t += 4.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_major_head_ik',
            target_name='automarker_head_king_front_far', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_major_eye_ik',
            target_name='automarker_head_king_front_near', duration=1.8, smooth=True)
        major.facial(group=MAIN, index=180, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-6.7)


        # Реплика 190 · king · исходное время 108 с
        # И вы нам его обеспечите?
        # Исходное окно facial: 12 с.
        t = 0
        cam_king_near.set(group=MAIN, time_delay=t)
        king.facial(group=MAIN, index=190, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-9.8)


        # Реплика 200 · major · исходное время 110.2 с
        # Нет, не обеспечу. Моих агентов в Ордене осталось считанные единицы, их там отстреливают как куропаток.
        # Исходное окно facial: 14.7 с.
        t = 0
        cam_major_near.set(group=MAIN, time_delay=t)
        t += 4.8
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_major_head_ik',
            target_name='automarker_head_hatcher', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_major_eye_ik',
            target_name='automarker_head_hatcher', duration=1.8, smooth=True)
        major.facial(group=MAIN, index=200, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-6.8)


        # Реплика 210 · king · исходное время 118.1 с
        # А может быть нам в этом поможет… (взгляд) мистер Трент?
        # Исходное окно facial: 15 с.
        t = 0
        cam_king_far.set(group=MAIN, time_delay=t)
        t += 1.9
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='prop_tome', target_name='offscreen', duration=0,
            smooth=False)
        t += 1.1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_king_head_ik',
            target_name='automarker_head_trent_upper', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_king_eye_ik',
            target_name='automarker_head_trent', duration=1.3, smooth=True)
        t += 0.9
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_king', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_king', duration=1.5, smooth=True)
        hatcher.motion(group=MAIN, time_delay=t, anim=Male.GENERIC_ANIM, duration=0.1, trans_time=0)
        king.facial(group=MAIN, index=210, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-10.1)


        # Реплика 220 · hatcher · исходное время 123 с
        # Трент просрал два артефакта и звено прикрытия, и что же мы ему предложим? Стать нашим агентом в Ордене...
        # Генерал Кинг, вы в своем уме???
        # Исходное окно facial: 32.6 с.
        t = 0
        cam_start_hatcher.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_HNDS_EMPH_000LV_XB_03, duration=5,
            time_scale=0.8, loop=True, trans_time=1)
        t += 4
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_EMPH_HNDSDN_TRNS_000LV_XA_01, duration=100,
            time_scale=0.8, trans_time=1)
        t += 3
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=100,
            time_scale=0.5, trans_time=1)
        hatcher.facial(group=MAIN, index=220, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-21.8)


        # Реплика 230 · major · исходное время 133.8 с
        # Не говоря уже о том, что скорее всего он и есть агент Ордена.
        # Исходное окно facial: 15 с.
        t = 0
        cam_major_near.set(group=MAIN, time_delay=t)
        t += 1.2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_major_head_ik',
            target_name='automarker_head_king_front_far', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_major_eye_ik',
            target_name='automarker_head_king_front_near', duration=1.8, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_king_head_ik',
            target_name='automarker_head_major_front_far', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_king_eye_ik',
            target_name='automarker_head_major_front_near', duration=1.5, smooth=True)
        major.facial(group=MAIN, index=230, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-10.0)


        # Реплика 240 · king · исходное время 138.8 с
        # А я верю в этого паренька. Трент, давай так, ты помогаешь нам, а мы чистим всю твою биографию перед СБА и
        # платим тройной тариф.
        # Исходное окно facial: 15.2 с.
        t = 0
        cam_king_far.set(group=MAIN, time_delay=t)
        t += 1.2
        major.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=4.444, time_scale=0.9,
            trans_time=0.5)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_king_head_ik',
            target_name='automarker_head_trent_upper', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_king_eye_ik',
            target_name='automarker_head_trent', duration=1.5, smooth=True)
        t += 7.5
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=100, time_scale=0.6,
            loop=True)
        king.facial(group=MAIN, index=240, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-5.7)


        # Реплика 250 · trent · исходное время 148.3 с
        # Знаете что, идите нахер, генерал Кинг. Последнее время я только и занимаюсь тем, что стараюсь улучшить
        # репутацию и получить большие деньги.
        # Исходное окно facial: 11.2 с.
        t = 0
        cam_trent_decline.set(group=MAIN, time_delay=t)
        t += 3.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_trent_decline',
            target_name='automarker_cam_trent_decline_pos2', duration=13, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_trent_decline_focus',
            target_name='automarker_cam_trent_decline_marker_pos2', duration=13, smooth=True)
        trent.facial(group=MAIN, index=250, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.2)


        # Реплика 260 · trent · исходное время 158.3 с
        # А все заканчивается тем, что на меня начинают охоту и обвиняют во все более тяжких преступлениях.
        # Исходное окно facial: 8 с.
        t = 0
        trent.facial(group=MAIN, index=260, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.7)


        # Реплика 270 · major · исходное время 164.6 с
        # Генерал Кинг, а вы не напомните, как звали того агента, которого мы внедрили в Орден до Трента?
        # Исходное окно facial: 17 с.
        t = 0
        cam_major_near.set(group=MAIN, time_delay=t)
        major.facial(group=MAIN, index=270, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-10.3)


        # Реплика 280 · king · исходное время 171.3 с
        # Какая разница? Связь с ним утеряна, он, скорее всего погиб.
        # Исходное окно facial: 14.5 с.
        t = 0
        cam_king_near.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_king_head_ik',
            target_name='automarker_head_major_front_far', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_king_eye_ik',
            target_name='automarker_head_major_front_near', duration=1.5, smooth=True)
        king.facial(group=MAIN, index=280, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-10.3)


        # Реплика 290 · major · исходное время 175.5 с
        # Тем не менее, генерал.
        # Исходное окно facial: 12 с.
        t = 0
        cam_major_near.set(group=MAIN, time_delay=t)
        major.facial(group=MAIN, index=290, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-10.0)


        # Реплика 300 · king · исходное время 177.5 с
        # Аларик. По-моему, Аларик.
        # Исходное окно facial: 12 с.
        t = 0
        cam_king_near.set(group=MAIN, time_delay=t)
        t += 2.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent',
            target_name='automarker_point_trent_sit_forward', duration=0, smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_rifleman',
            target_name='automarker_point_rifleman_near_trent', duration=0, smooth=False)
        t += 0.005
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_rifleman', angle=-25, axis='Y_AXIS',
            duration=0, smooth=False)
        king.facial(group=MAIN, index=300, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-9.2)


        # Реплика 310 · trent · исходное время 180.3 с
        # Сволочи! Что с Алариком, гады?
        # Исходное окно facial: 6 с.
        t = 0
        cam_trent_reaction.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_SPCBODY_s051x_Trent_XC_CHRF_RLLV_29, duration=6, start_time=24.8)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_rifleman',
            anim=Male.Sc_SPCBODY_s051x_ku_guard01_XB_STND_000LV_05, duration=6)
        trent.facial(group=MAIN, index=310, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.3)


        # Реплика 320 · major · исходное время 184 с
        # Мы не знаем. Связь с ним прервалась где-то на территории Кусари.
        # Исходное окно facial: 13 с.
        t = 0
        cam_major_near.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_major_head_ik',
            target_name='automarker_head_trent_upper', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_major_eye_ik',
            target_name='automarker_head_trent', duration=1.5, smooth=True)
        t += 4
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05, duration=100, loop=True)
        major.facial(group=MAIN, index=320, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-8.5)


        # Реплика 330 · hatcher · исходное время 188.5 с
        # (виноватая): У него почти получилось. Он должен был передать нам базу данных, но не вышел на связь. Мы не
        # знаем, кто наложил лапу на Аларика и его информацию.
        # Исходное окно facial: 15.7 с.
        t = 0
        cam_hatcher_sad.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_trent_upper_forward', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1.5, smooth=True)
        hatcher.facial(group=MAIN, index=330, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-6.7)


        # Реплика 340 · king · исходное время 197.5 с
        # (мотивирующе): Ты можешь помочь и нам и своему другу. Найди его, заверши передачу информации, которую
        # должен был завершить твой друг - и ты свободен.
        # Исходное окно facial: 15 с.
        t = 0
        cam_king_near.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_king_head_ik',
            target_name='automarker_head_trent_upper', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_king_eye_ik',
            target_name='automarker_head_trent', duration=1.3, smooth=True)
        king.facial(group=MAIN, index=340, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-6.5)


        # Реплика 345 · king · исходное время 206 с
        # И не вздумай хитрить, дружище, не вздумай
        # Исходное окно facial: 12 с.
        t = 0
        t += 3
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_rifleman', target_name='offscreen', duration=0,
            smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', target_name='automarker_point_trent_sit',
            duration=0, smooth=False)
        t += 0.1
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=100, time_scale=0.6,
            loop=True)
        king.facial(group=MAIN, index=345, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-8.5)


        # Реплика 350 · trent · исходное время 209.5 с
        # Ладно... ваша взяла...
        # Исходное окно facial: 6 с.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=350, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-4.0)


        # Реплика 360 · king · исходное время 211.5 с
        # Мисс Хетчер, поднимите все данные по агенту Аларику и передайте их в распоряжение мистеру Тренту.
        # Исходное окно facial: 12 с.
        t = 0
        cam_king_far.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_king_head_ik',
            target_name='automarker_head_hatcher_right', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_king_eye_ik',
            target_name='automarker_head_hatcher_right_far', duration=1.5, smooth=True)
        king.facial(group=MAIN, index=360, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-6.6)


        # Реплика 370 · king · исходное время 216.9 с
        # Далее, вашим заданием будет сопровождение тома Протея вместе с Трентом и мисс Дерси на исследовательскую
        # базу.
        # Исходное окно facial: 14 с.
        t = 0
        t += 2.1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_king', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_king', duration=1.5, smooth=True)
        king.facial(group=MAIN, index=370, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-7.4)


        # Реплика 380 · hatcher · исходное время 223.5 с
        # Принято!
        # Исходное окно facial: 5 с.
        t = 0
        cam_start_hatcher.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_SALUT_000LV_XA_03, duration=10, start_time=1.5)
        hatcher.facial(group=MAIN, index=380, append=True, auto_lip=True, extra_delay=0)
        t = 0
        t += 10921.5
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_eye_ik',
            duration=55, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.5)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M08OsirisScene
