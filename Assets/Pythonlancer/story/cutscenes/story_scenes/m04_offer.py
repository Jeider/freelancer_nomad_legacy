"""m04_offer: полная постановка из master; точки в m04_offer.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character, EyeIkEvent, LookAtCamera, MAIN, Male, MotionEvent, MoveEvent, NeckIkEvent, RotateAxisEvent, SoundEvent,
)
from story.cutscenes.anim import (
    Male, Trent,
)
from story import actors


class CharTrooper1Actor(actors.Actor):
    NAME = 'trooper1'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'ms4_trooper1'

class CharTrooper2Actor(actors.Actor):
    NAME = 'trooper2'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'ms4_trooper2'


class M04OfferScene(Scene):
    DUMP_FILE = 'm04_offer'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Персонажи, камеры, реквизит и звук.
        trent = Character(root=self, actor=actors.Trent, name='Char_trent', light_group=0,
            init_point='Char_trent', rotate_from_quat=True, appearance='trent', actor_name='Player')
        trooper1 = Character(root=self, actor=CharTrooper1Actor, name='Char_trooper1', light_group=0,
            init_point='Char_trooper1', rotate_from_quat=True, appearance='ms4_trooper1', actor_name='Trooper1')
        trooper2 = Character(root=self, actor=CharTrooper2Actor, name='Char_trooper2', light_group=0,
            init_point='Char_trooper2', rotate_from_quat=True, appearance='ms4_trooper2', actor_name='Trooper2')
        jacobo = Character(root=self, actor=actors.Jacobo, name='Char_jacobo', light_group=0,
            init_point='Char_jacobo', rotate_from_quat=True, appearance='jacobo', actor_name='jacobo')
        cam_start = LookAtCamera(root=self, name='cam_start', fov=20, look_duration=300)
        cam_search = LookAtCamera(root=self, name='cam_search', fov=25, look_duration=300)
        cam_jacobo_appear = LookAtCamera(root=self, name='cam_jacobo_appear', fov=22, look_duration=300)
        cam_jacobo_sitting = LookAtCamera(root=self, name='cam_jacobo_sitting', fov=16, look_duration=300)
        cam_trent_sitting = LookAtCamera(root=self, name='cam_trent_sitting', fov=16, look_duration=300)

        # Исходные точки взгляда.

        # Вход.
        t = 0
        cam_start.set(group=MAIN, time_delay=t)
        cam_start.move_cam(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        cam_start.move_focus(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=1.3, loop=True, time_delay=t)
        t += 1.3
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=15, time_delay=t)
        t += 1.7
        MotionEvent(root=self, group=MAIN, object_name=trooper1.name, anim=Male.Sc_MLBODY_WLKG_000LV_XB_01,
            duration=15, loop=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=trooper2.name, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01,
            duration=15, start_time=1, loop=True, time_delay=t)
        t += 0.6
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_1STEP_SIDWYSL_000LV_XA_02, duration=15, time_delay=t)
        t += 2.4
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_1STEP_BKWD_PVOTR_090LV_XA_06, duration=15, time_delay=t)
        t += 4
        cam_start.move_focus(group=MAIN, index=3, duration=5, smooth=True, time_delay=t)
        t += 2
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01, duration=1.1, trans_time=0.25,
            time_delay=t)
        t += 1.1
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=1.89, trans_time=0.001, loop=True,
            time_delay=t)
        t += 1.9
        cam_search.set(group=MAIN, time_delay=t)
        cam_search.move_cam(group=MAIN, index=2, duration=6, smooth=True, time_delay=t)
        cam_search.move_focus(group=MAIN, index=2, duration=6, smooth=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('point_trent_search'), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=3.9, loop=True, time_delay=t)
        t += 3.9
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=2.3, trans_time=0.1,
            time_delay=t)
        t += 2.3
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_LOOK_AROU_CASL_000LV_XA_08, duration=6.3, time_delay=t)
        t += 5.8
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('jacobo_head_ik'),
            target_name=self.get_automarker_name('head_trent_search'), duration=0.1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 0.5
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_TURN_090LV_XA_02, duration=3, time_scale=0.75,
            trans_time=1, time_delay=t)
        t += 1.5
        cam_jacobo_appear.set(group=MAIN, time_delay=t)
        jacobo.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=2.3, start_time=0.45,
            time_delay=t)
        t += 0.25
        NeckIkEvent(root=self, group=MAIN, char_name=jacobo.name,
            target_name=self.get_automarker_name('jacobo_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=25, transition_duration=1, time_delay=t)
        t += 0.75
        trent.motion(group=MAIN, anim=Trent.Sc_MLHEAD_MOTION_MOUTH_CLENCH_TRENT_000LV_, duration=1.937,
            time_delay=t)
        cam_jacobo_appear.move_cam(group=MAIN, index=2, duration=6, smooth=True, time_delay=t)
        t += 0.5
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=15,
            time_scale=0.75, trans_time=1, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=-15, axis='Y_AXIS', duration=1,
            smooth=True, time_delay=t)
        main_group.append_time(32)

        # m04_offer 10: Jacobo.
        # Герр Трент, это вы?
        t = 0
        trent.motion(group=MAIN, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=0.333, time_delay=t)
        t += 1
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_TURN_180LV_XA_04, duration=6, trans_time=1, time_delay=t)
        jacobo.facial(group=MAIN, index=10, auto_lip=True, extra_delay=0)
        # Действие после исходного окна реплики.
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('jacobo_head_ik'),
            target_name=self.get_automarker_name('head_trent_sitting'), duration=4, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        jacobo.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_SITCL_TRNS_180DN_XA_06, duration=8, trans_time=1,
            time_delay=t)
        main_group.append_time(2)

        # m04_offer 20: Jacobo.
        # Герр Трент, спасибо что согласились прилететь. У меня неприятности. Меня разыскивают власти
        # Рейнланда.
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('point_trent_sit_around_jacobo'), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        cam_jacobo_sitting.set(group=MAIN, time_delay=t)
        t += 0.0011
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=3, time_delay=t)
        t += 1.9989
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('jacobo_head_ik'),
            target_name=self.get_automarker_name('head_trent_sit'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        jacobo.facial(group=MAIN, index=20, auto_lip=True, extra_delay=0)

        # m04_offer 30: Trent.
        # Это я уже понял. И у меня появилось знакомое ощущение что меня очень хотят втянуть в неприятности.
        t = 0
        cam_trent_sitting.set(group=MAIN, time_delay=t)
        t += 5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('jacobo_head_ik'),
            target_name=self.get_automarker_name('head_trent_sit'), duration=0.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('jacobo_eye_ik'),
            target_name=self.get_automarker_name('head_trent_sit'), duration=0.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        jacobo.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=3, time_scale=2,
            start_time=1, trans_time=1, time_delay=t)
        trent.facial(group=MAIN, index=30, auto_lip=True, extra_delay=0)

        # m04_offer 40: Jacobo.
        # Герр Трент, вы не понимаете. Дело исключительной важности. Мне необходимо доставить в Либерти важные
        # документы.
        t = 0
        cam_jacobo_sitting.set(group=MAIN, time_delay=t)
        jacobo.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_LOOK_RLLV_A_06, duration=3, time_scale=0.8,
            start_time=1, trans_time=1, time_delay=t)
        t += 3
        jacobo.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CONV_HNDS_CASL_000LV_xa_04, duration=4, time_scale=0.8,
            start_time=1, trans_time=1, loop=True, time_delay=t)
        t += 1
        NeckIkEvent(root=self, group=MAIN, char_name=jacobo.name,
            target_name=self.get_automarker_name('jacobo_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=55, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=jacobo.name,
            target_name=self.get_automarker_name('jacobo_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=55, transition_duration=1, time_delay=t)
        t += 3
        jacobo.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, duration=5, time_scale=0.8,
            start_time=1, trans_time=1, time_delay=t)
        t += 1
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=15, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=15, transition_duration=1, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_jacobo_sit'), duration=0.1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_jacobo_sit'), duration=0.1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        jacobo.facial(group=MAIN, index=40, auto_lip=True, extra_delay=0)

        # m04_offer 50: Trent.
        # Опять меня угораздило вляпаться в шпионские игры... Джакобо, вы в курсе, что в данный момент я
        # работаю на те самые власти Рейнланда, которые вас ищут?
        t = 0
        cam_trent_sitting.set(group=MAIN, time_delay=t)
        t += 4
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=4, time_scale=0.6,
            trans_time=1, time_delay=t)
        trent.facial(group=MAIN, index=50, auto_lip=True, extra_delay=0)

        # m04_offer 60: Jacobo.
        # Герр Трент, вы же фриленсер. Вы не давали никаких присяг. После выполнения задания вас с заказчиком
        # ничего не связывает.
        t = 0
        cam_jacobo_sitting.set(group=MAIN, time_delay=t)
        jacobo.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_TALK_HNSTBL_000LV_B_30, duration=26, time_scale=0.8,
            loop=True, time_delay=t)
        jacobo.facial(group=MAIN, index=60, auto_lip=True, extra_delay=0)

        # m04_offer 62: Jacobo.
        # Герр Трент, если мы сможем доставить эти ОЧЕНЬ важные документы в Либерти, в систему Форбс, нам
        # заплатят очень большие деньги, ОЧЕНЬ большие, понимаете?
        jacobo.facial(group=MAIN, index=62, auto_lip=True, extra_delay=0)

        # m04_offer 65: Jacobo.
        # У меня одного это скорее всего не получится, но если вы мне поможете...
        jacobo.facial(group=MAIN, index=65, auto_lip=True, extra_delay=0)

        # m04_offer 67: Jacobo.
        # А если вы мне не поможете, меня скорее всего просто убьют...
        t = 1
        jacobo.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=5, trans_time=1,
            time_delay=t)
        line_sound = self.lookup_single_sound(67)
        SoundEvent(root=self, group=MAIN, sound_name=line_sound.get_nickname())
        main_group.append_time(4)
