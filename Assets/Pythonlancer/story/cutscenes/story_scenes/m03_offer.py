"""m03_offer: полная постановка из master; точки в m03_offer.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character, EyeIkEvent, LookAtCamera, MAIN, Male, MoveEvent, NeckIkEvent, RotateAxisEvent, SoundEvent,
)
from story.cutscenes.anim import (
    Male, Trent,
)
from story import actors



class M03OfferScene(Scene):
    DUMP_FILE = 'm03_offer'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Персонажи, камеры, реквизит и звук.
        trent = Character(root=self, actor=actors.Trent, name='Char_trent', light_group=0,
            init_point='Char_trent', rotate_from_quat=True, appearance='trent', actor_name='Player')
        hassler = Character(root=self, actor=actors.Hassler, name='Char_hassler', light_group=0,
            init_point='Char_hassler', rotate_from_quat=True, appearance='hassler', actor_name='hassler')
        wilham = Character(root=self, actor=actors.Wilham, name='Char_wilham', light_group=0,
            init_point='Char_wilham', rotate_from_quat=True, appearance='wilham', actor_name='wilham')
        cam_start = LookAtCamera(root=self, name='cam_start', fov=20, look_duration=300)
        cam_trent_hands = LookAtCamera(root=self, name='cam_trent_hands', fov=15, look_duration=300)
        cam_wilham_near = LookAtCamera(root=self, name='cam_wilham_near', fov=15, look_duration=300)
        cam_trent_near = LookAtCamera(root=self, name='cam_trent_near', fov=15, look_duration=300)
        cam_wilham_far = LookAtCamera(root=self, name='cam_wilham_far', fov=16, look_duration=300)
        cam_trent_far = LookAtCamera(root=self, name='cam_trent_far', fov=15, look_duration=300)
        cam_top = LookAtCamera(root=self, name='cam_top', fov=25, look_duration=300)

        # Исходные точки взгляда.

        # Вход.
        t = 0
        cam_start.set(group=MAIN, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=wilham.name,
            target_name=self.get_automarker_name('wilham_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=90, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=wilham.name,
            target_name=self.get_automarker_name('wilham_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=90, transition_duration=1, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=hassler.name,
            target_name=self.get_automarker_name('hassler_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=90, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=hassler.name,
            target_name=self.get_automarker_name('hassler_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=90, transition_duration=1, time_delay=t)
        cam_start.move_cam(group=MAIN, index=2, duration=6, smooth=True, time_delay=t)
        cam_start.move_focus(group=MAIN, index=2, duration=6, smooth=True, time_delay=t)
        hassler.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_HOLD_ARMS_CROSSED_000LV_XA_02, duration=7,
            time_scale=0.8, loop=True, time_delay=t)
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=5, time_scale=0.5,
            loop=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=15, time_scale=0.6,
            time_delay=t)
        main_group.append_time(2)

        # m03_offer 10: Trent.
        # Салют, джентльмены.
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('wilham_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('wilham_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=2.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_wilham_half'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_wilham'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hassler_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hassler_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        trent.facial(group=MAIN, index=10, auto_lip=True)

        # m03_offer 20: Wilham.
        # А вот и герр Трент. Познакомьтесь с герром Хасслером. В ходе этой миссии вам придется плотно
        # сотрудничать.
        t = 1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('wilham_head_ik'),
            target_name=self.get_automarker_name('head_hassler_half'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('wilham_eye_ik'),
            target_name=self.get_automarker_name('head_hassler_half'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_GESTR_RGHT_000LV_XA_02, duration=10, time_scale=0.4,
            trans_time=1.5, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=90, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=90, transition_duration=1, time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hassler_head_ik'),
            target_name=self.get_automarker_name('head_trent_half'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hassler_eye_ik'),
            target_name=self.get_automarker_name('head_wilham_half'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 2.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('wilham_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('wilham_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        hassler.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, duration=7, time_scale=0.8,
            time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_hassler'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_hassler'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hassler_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hassler_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 1.5
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=25, axis='Y_AXIS', duration=2,
            smooth=True, time_delay=t)
        wilham.facial(group=MAIN, index=20, auto_lip=True)

        # m03_offer 30: Trent.
        # Герр Хасслер, мое почтение.
        t = 0
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_SHAK_RHAND_000LV_XA_03, duration=15, time_scale=0.7,
            trans_time=0.25, time_delay=t)
        cam_trent_hands.set(group=MAIN, time_delay=t)
        t += 0.3
        hassler.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_SHAK_RGHT_000LV_A_03, duration=15, time_scale=0.7,
            trans_time=0.25, time_delay=t)
        t += 1.7
        cam_trent_hands.move_focus(group=MAIN, index=2, duration=5, smooth=True, time_delay=t)
        t += 0.5
        trent.motion(group=MAIN, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, duration=5, trans_time=1,
            time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_wilham_half'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_wilham'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=-25, axis='Y_AXIS', duration=3,
            smooth=True, time_delay=t)
        trent.facial(group=MAIN, index=30, auto_lip=True)

        # m03_offer 40: Trent.
        # И в чем же будет состоять эта миссия?
        t = 2
        trent.motion(group=MAIN, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, duration=5, trans_time=1,
            time_delay=t)
        t += 0.75
        trent.facial(group=MAIN, index=40, auto_lip=True)
        cam_wilham_far.set(group=MAIN, time_delay=0)

        # m03_offer 70: Wilham.
        # Наша разведка локализовала местонахождение Дитриха. Это бывшая военная база Кёнигсберг.
        t = 0
        # NeckIkEvent(root=self, group=MAIN, char_name=wilham.name,
        #     target_name=self.get_automarker_name('wilham_head_ik'), target_type='ROOT', target_part='',
        #     up='NEG_Y_AXIS', front='Z_AXIS', duration=40, transition_duration=1, time_delay=t)
        hassler.motion(group=MAIN, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=3, time_scale=0.4,
            time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=wilham.name, angle=10, axis='Y_AXIS', duration=1,
            smooth=True, time_delay=t)
        cam_wilham_far.set(group=MAIN, time_delay=t)
        t += 1
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_MED_000LV_xa_05, duration=5, time_scale=0.5,
            trans_time=2, time_delay=t)
        t += 1
        cam_wilham_far.move_cam(group=MAIN, index=2, duration=23, smooth=True, time_delay=t)
        cam_wilham_far.move_focus(group=MAIN, index=2, duration=23, smooth=True, time_delay=t)
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_HNDSUP_TRNS_000LV_XA_00, duration=3,
            time_scale=0.5, trans_time=1.5, time_delay=t)
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_HNDS_CASL_000LV_xc_01, duration=8, time_scale=0.5,
            trans_time=1.5, loop=True, time_delay=t+1)
        t += 3
        hassler.motion(group=MAIN, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=3, time_scale=0.4,
            time_delay=t)
        t += 1

        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('wilham_head_ik'),
            target_name=self.get_automarker_name('head_hassler_half'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=2)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('wilham_eye_ik'),
            target_name=self.get_automarker_name('head_hassler'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=2)


        wilham.facial(group=MAIN, index=70, auto_lip=True)



        # m03_offer 75: Wilham.
        # В данный момент собирается ударный флот для атаки базы. Но наши аналитики просчтитали, что прямое
        # нападение на Кёнигсберг приведет к недопустимо большим потерям среди личного состава.
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hassler_head_ik'),
            target_name=self.get_automarker_name('head_wilham_half'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t+0.2)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hassler_eye_ik'),
            target_name=self.get_automarker_name('head_wilham'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t+0.2)
        t += 3
        hassler.motion(group=MAIN, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=3, time_scale=0.4,
            time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('wilham_head_ik'),
            target_name=self.get_automarker_name('head_trent_half'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('wilham_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 2
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hassler_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hassler_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 2
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_HNDSDN_TRNS_000LV_XA_01, duration=3,
            time_scale=0.5, trans_time=1.5, time_delay=t-2)
        t += 1
        hassler.motion(group=MAIN, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=3, time_scale=0.4,
            time_delay=t)

        t = 0.8
        hassler.motion(group=MAIN, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=3, time_scale=0.4,
            time_delay=t)
        t += 2
        t += 1

        t += 2
        hassler.motion(group=MAIN, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=3, time_scale=0.4,
            time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_GESTL_FIST_000LV_00, duration=1, time_scale=2,
            time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_GESTR_FIST_000LV_00, duration=1, time_scale=2,
            time_delay=t)


        wilham.facial(group=MAIN, index=75, auto_lip=True)
        wilham.facial(group=MAIN, index=77, auto_lip=True)

        # m03_offer 80: Trent.
        # То есть те, кто будет таскать вам каштаны из огня.
        t = 0
        cam_top.set(group=MAIN, time_delay=t)
        cam_top.move_cam(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        cam_top.move_focus(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_LSTN_SMALL_000LV_A_34, duration=3, loop=True,
            time_delay=t)
        hassler.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_LSTN_000DN_A_18, duration=15, loop=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_HOLD_000LV_XA_02, duration=5, time_scale=0.5,
            loop=True, time_delay=t)
        trent.facial(group=MAIN, index=80, auto_lip=True)
        # Действие после исходного окна реплики.
        t = 0
        trent.motion(group=MAIN, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, duration=5, trans_time=0.25,
            time_delay=t)
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_GESTR_THMBSUP_000LV_XA_02, duration=5, time_scale=0.75,
            trans_time=0.25, time_delay=t)
        wilham.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_POINT_RGHT_CASL_000LV_00, duration=4, time_scale=1.5,
            start_time=3, trans_time=0.5, time_delay=t)
        main_group.append_time(0.5)

        # m03_offer 90: Wilham.
        # Именно так, герр Трент. Кстати на вашем участии в этой миссии настаивал лично адмирал Райхманн.
        t = 0.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_hassler_trent'), duration=2.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_hassler'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('wilham_head_ik'),
            target_name=self.get_automarker_name('head_trent_half_right'), duration=2.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=5, time_scale=0.5,
            trans_time=0.25, time_delay=t)
        t += 3
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_wilham_half'), duration=2.2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_wilham'), duration=1.1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_TALK_SMALL_000DN_A_17, duration=15, time_scale=0.3,
            trans_time=1, loop=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_LSTN_SMALL_000LV_B_09, duration=5, time_scale=0.75,
            trans_time=0.25, time_delay=t)
        wilham.facial(group=MAIN, index=90, auto_lip=True)
