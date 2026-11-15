"""m03_offer_accept: постановка для ручного редактирования.

Точки: SCENES/m03_offer_accept.blend → DUMPS/m03_offer_accept.json.
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
    SoundEvent,
)
from story.cutscenes.anim import (
    Male,
)
from story.cutscenes.source_extensions import (
    preserve_entity,
)
from story import actors



class M03OfferAcceptScene(Scene):
    DUMP_FILE = 'm03_offer_accept'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'actor': 'Player', 'category': 'Character'})
        hassler = Character(root=self, actor=actors.Hassler, light_group=0, init_point='Char_hassler',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(hassler, template_name='hassler', userprops={'category': 'Character', 'actor': 'hassler'})
        wilham = Character(root=self, actor=actors.Wilham, light_group=0, init_point='Char_wilham', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(wilham, template_name='wilham', userprops={'category': 'Character', 'actor': 'wilham'})
        cam_trent_near = LookAtCamera(root=self, name='cam_trent_near', fov=15, farplane=5000, look_duration=300)
        preserve_entity(cam_trent_near)
        cam_trent_far = LookAtCamera(root=self, name='cam_trent_far', fov=15, farplane=5000, look_duration=300)
        preserve_entity(cam_trent_far)
        cam_hassler_near = LookAtCamera(root=self, name='cam_hassler_near', fov=15, farplane=5000, look_duration=300)
        preserve_entity(cam_hassler_near)
        cam_hassler_far = LookAtCamera(root=self, name='cam_hassler_far', fov=15, farplane=5000, look_duration=300)
        preserve_entity(cam_hassler_far)
        cam_wilham_near = LookAtCamera(root=self, name='cam_wilham_near', fov=15, farplane=5000, look_duration=300)
        preserve_entity(cam_wilham_near)
        cam_final = LookAtCamera(root=self, name='cam_final', fov=20, farplane=5000, look_duration=300)
        preserve_entity(cam_final)

        # Вход / начальная постановка.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_wilham', target_name='automarker_wilham_head_ik',
            duration=90, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_wilham', target_name='automarker_wilham_eye_ik',
            duration=90, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_hassler', target_name='automarker_hassler_head_ik',
            duration=90, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_hassler', target_name='automarker_hassler_eye_ik',
            duration=90, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=73, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_eye_ik',
            duration=73, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_LSTN_SMALL_000LV_A_34, duration=35, time_scale=0.5,
            loop=True)
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_LSTN_SMALL_000LV_B_09, duration=16,
            time_scale=0.5, loop=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=4, time_scale=0.5)
        main_group.append_time(1)


        # Реплика 100 · trent · исходное время 1 с
        # А можно узнать, как так оказалось, что элитная военная база осталась бесхозной и в итоге досталась
        # мятежникам и корсарам?
        # Исходное окно facial: 14.5 с.
        t = 0
        t += 3
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, duration=10, time_scale=0.4,
            trans_time=1)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_hassler_trent', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_hassler', duration=1.5, smooth=True)
        t += 4
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_wilham_half', duration=4, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_wilham', duration=2, smooth=True)
        t += 5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_hassler_trent', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_hassler', duration=2, smooth=True)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hassler_head_ik',
            target_name='automarker_head_trent_half', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hassler_eye_ik',
            target_name='automarker_head_trent', duration=1, smooth=True)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_head_ik',
            target_name='automarker_head_hassler_half', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_head_hassler', duration=1.5, smooth=True)
        trent.facial(group=MAIN, index=100, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(0.5)


        # Реплика 110 · hassler · исходное время 16 с
        # Герр Трент, станция Кёнигисберг когда-то была частью Мюнхенского контура обороны. Военные Кусари
        # рассматривали этот контур не иначе, чем шило у себя в заднице.
        # Исходное окно facial: 13 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hassler_head_ik',
            target_name='automarker_head_trent', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_hassler_far',
            target_name='automarker_cam_hassler_far_pos2', duration=15, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_hassler_far_focus',
            target_name='automarker_cam_hassler_far_marker_pos2', duration=15, smooth=True)
        cam_hassler_far.set(group=MAIN, time_delay=t)
        t += 1
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_HNDSUP_TRNS_000LV_XA_00, duration=3,
            time_scale=0.5, trans_time=1.5)
        t += 1.5
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_HNDS_CASL_000LV_xc_01, duration=4.5,
            time_scale=0.5, loop=True, trans_time=1.5)
        t += 4.5
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_HNDSDN_TRNS_000LV_XA_01, duration=3,
            time_scale=0.5, trans_time=1.5)
        t += 3
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, duration=5,
            time_scale=0.6, trans_time=1)
        # Duplicate source sound event 51, same timestamp.
        SoundEvent(root=self, group=MAIN, sound_name=self.lookup_single_sound(110).get_nickname())
        hassler.facial(group=MAIN, index=110, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(0.0)


        # Реплика 115 · hassler · исходное время 29 с
        # В ходе разравившегося конфликта с Кусари мы потерпели сокрушительное поражение и по условиям мирного
        # договора строительство контура было прекращено, а система Мюнхен была полностью демилитаризована.
        # Исходное окно facial: 13.8 с.
        t = 0
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_head_ik',
            target_name='automarker_head_trent_half', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_head_trent', duration=1.5, smooth=True)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_hassler_far',
            target_name='automarker_cam_hassler_far_pos3', duration=15, smooth=True)
        t += 10
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hassler_head_ik',
            target_name='automarker_head_wilham_half', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hassler_eye_ik',
            target_name='automarker_head_wilham', duration=1.5, smooth=True)
        t += 0.5
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_MAD_SNARL_000LV_XA_, duration=5.5, time_scale=0.5,
            trans_time=0.25)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_head_ik',
            target_name='automarker_head_hassler', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_head_hassler', duration=2, smooth=True)
        hassler.facial(group=MAIN, index=115, append=True, auto_lip=True, extra_delay=0)
        t = 0
        t += 0.2
        cam_wilham_near.set(group=MAIN, time_delay=t)
        t += 2.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hassler_head_ik',
            target_name='automarker_head_trent', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hassler_eye_ik',
            target_name='automarker_head_trent', duration=1, smooth=True)
        t += 0.5
        cam_hassler_near.set(group=MAIN, time_delay=t)
        main_group.append_time(3.7)


        # Реплика 120 · hassler · исходное время 46.5 с
        # Станция Кёнигсберг была законсервирована до нынешних пор, когда Дитрих, воспользовавшись старыми ключами
        # и доступами, не решил сделать из станции свой опорный пункт.
        # Исходное окно facial: 20 с.
        t = 0
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, duration=10,
            time_scale=0.6, trans_time=1)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_hassler_near',
            target_name='automarker_cam_hassler_near_pos2', duration=20, smooth=False)
        t += 8.5
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=10,
            time_scale=0.3, trans_time=1)
        t += 9.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_head_ik',
            target_name='automarker_head_trent', duration=4, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_head_trent', duration=2, smooth=True)
        hassler.facial(group=MAIN, index=120, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(0.0)


        # Реплика 130 · trent · исходное время 66.5 с
        # Я так понимаю, спрашивать всякие глупости типа, есть ли у меня выбор, в этой ситуации неуместно.
        # Исходное окно facial: 9 с.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        t += 1.5
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, duration=10,
            time_scale=0.5, trans_time=1)
        t += 2.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_wilham_half', duration=4, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_wilham', duration=2, smooth=True)
        t += 3.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_final', target_name='automarker_cam_final_pos2',
            duration=20, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_final_focus',
            target_name='automarker_cam_final_marker_pos2', duration=20, smooth=True)
        cam_final.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=130, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.0)


        # Реплика 140 · wilham · исходное время 73.5 с
        # Вы умный человек, герр Трент.
        # Исходное окно facial: 3 с.
        t = 0
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_GESTR_THMBSUP_000LV_XA_02, duration=25,
            time_scale=0.8)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_GESTR_THUMB_000LV_00, duration=25, time_scale=0.8)
        wilham.facial(group=MAIN, index=140, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.5)


        # Реплика 150 · hassler · исходное время 76 с
        # Герр Трент, вам предлагают работу, которая и не снилась большей части местных фрилансеров.
        # Исходное окно facial: 9.5 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_head_ik',
            target_name='automarker_head_hassler_half', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_head_hassler', duration=1.25, smooth=True)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='Char_hassler', duration=90,
            transition_duration=1, target_type='PART', target_part='Body_Neck', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='Char_hassler', duration=90,
            transition_duration=1, target_type='PART', target_part='Body_Neck', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 0.25
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_MED_000LV_xa_05, duration=10, time_scale=0.5,
            loop=True, trans_time=0.5)
        t += 0.25
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=10, trans_time=0.25)
        t += 6.5
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_wilham', angle=-10, axis='Y_AXIS',
            duration=3, smooth=True)
        t += 2
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_TURN_045LV_XA_04, duration=25, trans_time=1)
        hassler.facial(group=MAIN, index=150, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(0.5)


        # Реплика 155 · hassler · исходное время 86 с
        # Что вы капризничаете как старшеклассница на выпускном? Давайте вылетать. Встречаемся в космосе.
        # Исходное окно facial: 7 с.
        t = 0
        t += 1
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_TURN_315LV_XA_02, duration=25, time_scale=0.8,
            trans_time=1)
        t += 3
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=20, axis='Y_AXIS', duration=2,
            smooth=True)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hassler_head_ik',
            target_name='automarker_way_out', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hassler_eye_ik',
            target_name='automarker_way_out', duration=1, smooth=True)
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01, duration=25,
            time_scale=0.75, trans_time=1)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_TURN_315LV_XA_02, duration=25, trans_time=1)
        hassler.facial(group=MAIN, index=155, append=True, auto_lip=True, extra_delay=0)
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_head_ik',
            target_name='automarker_way_out', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_wilham_eye_ik',
            target_name='automarker_way_out', duration=2, smooth=True)
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01, duration=25,
            time_scale=0.75, trans_time=1)
        t += 0.42
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=25, time_scale=0.75,
            loop=True, trans_time=0.01)
        t += 1.0
        wilham.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=25, time_scale=0.75,
            loop=True, trans_time=0.01)
        main_group.append_time(5.0)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M03OfferAcceptScene
