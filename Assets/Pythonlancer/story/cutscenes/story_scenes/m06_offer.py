"""m06_offer: полная постановка из master; точки в m06_offer.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character, EyeIkEvent, Female, LookAtCamera, MAIN, Male, MoveEvent, NeckIkEvent, RotateAxisEvent,
)
from story.cutscenes.anim import (
    Female, Male,
)
from story import actors



class M06OfferScene(Scene):
    DUMP_FILE = 'm06_offer'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Персонажи, камеры, реквизит и звук.
        trent = Character(root=self, actor=actors.Trent, name='Char_trent', light_group=0,
            init_point='Char_trent', rotate_from_quat=True, appearance='trent', actor_name='Player')
        alaric = Character(root=self, actor=actors.Alaric, name='Char_alaric', light_group=0,
            init_point='Char_alaric', rotate_from_quat=True, use_ambient=True, appearance='alaric',
            actor_name='Alaric')
        hatcher = Character(root=self, actor=actors.Hatcher, name='Char_hatcher', light_group=0,
            init_point='Char_hatcher', rotate_from_quat=True, appearance='hatcher', actor_name='Hatcher')
        cam_start = LookAtCamera(root=self, name='cam_start', fov=30, look_duration=30)
        cam_trent_arrive = LookAtCamera(root=self, name='cam_trent_arrive', fov=25, look_duration=1)
        cam_greetings = LookAtCamera(root=self, name='cam_greetings', fov=22, look_duration=300)
        cam_hatcher = LookAtCamera(root=self, name='cam_hatcher', fov=20, look_duration=300)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=22, look_duration=1)
        cam_friends = LookAtCamera(root=self, name='cam_friends', fov=22, look_duration=1)
        cam_alaric = LookAtCamera(root=self, name='cam_alaric', fov=22, look_duration=1)

        # Исходные точки взгляда.

        # Вход.
        t = 0
        cam_start.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, duration=0.01, time_delay=t)
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_XB_04, duration=2, loop=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=3.8, time_scale=0.8, loop=True,
            time_delay=t)
        cam_start.move_cam(group=MAIN, index=2, duration=3.8, smooth=True, time_delay=t)
        cam_start.move_focus(group=MAIN, index=2, duration=3.8, smooth=True, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=hatcher.name, target_name=trent.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=10, transition_duration=2,
            time_delay=t)
        t += 2
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_SITCR_TRNS_180DN_XA_06, duration=1.8, trans_time=1,
            time_delay=t)
        t += 1.8
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=4, time_scale=0.8,
            time_delay=t)
        cam_trent_arrive.set(group=MAIN, time_delay=t)
        t += 0.001
        MoveEvent(root=self, group=MAIN, object_name=alaric.name,
            target_name=self.get_automarker_name('point_alaric_sit'), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.01
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=5, time_delay=t)
        t += 0.189
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=200, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=200, transition_duration=1, time_delay=t)
        main_group.append_time(5)

        # m06_offer 10: Trent.
        # Мисс Хетчер. Аларик, не ожидал, что ты уже здесь.
        t = 1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('table_center'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_alaric_btm'), duration=1.3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 0.5
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=10, axis='Y_AXIS', duration=2,
            smooth=True, time_delay=t)
        t += 0.5
        NeckIkEvent(root=self, group=MAIN, char_name=alaric.name,
            target_name=self.get_automarker_name('alaric_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=25, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=alaric.name,
            target_name=self.get_automarker_name('alaric_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=25, transition_duration=1, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=2.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 0.5
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_SITCR_TRNS_180DN_XA_06, duration=1, time_scale=0.7,
            trans_time=1, time_delay=t)
        trent.facial(group=MAIN, index=10, auto_lip=True, extra_delay=0)

        # m06_offer 20: Alaric.
        # Как только ты со мной связался, я сразу же прибыл к мисс Хетчер. Видимо, я был ближе к Нориджу, чем
        # ты.
        t = 0
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_CONV_LHNDUP_TRNS_000LV_XA_02, duration=7,
            time_scale=0.5, trans_time=0.25, time_delay=t)
        cam_greetings.set(group=MAIN, time_delay=t)
        t += 0.001
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('point_trent_sit'), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.01
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=5, time_delay=t)
        t += 2.489
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_CONV_LHND_CASL_000LV_xa_03, duration=2, time_scale=0.5,
            trans_time=1, time_delay=t)
        t += 2
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_CONV_LHNDDN_TRNS_000LV_XA_02, duration=4,
            time_scale=0.5, trans_time=2, time_delay=t)
        t += 0.5
        cam_greetings.move_cam(group=MAIN, index=2, duration=6, smooth=True, time_delay=t)
        cam_greetings.move_focus(group=MAIN, index=2, duration=6, smooth=True, time_delay=t)
        t += 1.5
        NeckIkEvent(root=self, group=MAIN, char_name=hatcher.name,
            target_name=self.get_automarker_name('hatcher_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=200, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=hatcher.name,
            target_name=self.get_automarker_name('hatcher_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=200, transition_duration=1, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('alaric_head_ik'),
            target_name=self.get_automarker_name('head_hatcher'), duration=2.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('alaric_eye_ik'),
            target_name=self.get_automarker_name('head_hatcher'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        alaric.facial(group=MAIN, index=20, auto_lip=True, extra_delay=0)

        # m06_offer 30: Hatcher.
        # А теперь, господа, когда все выяснили когда, откуда и каким образом мы все сюда прибыли, перейдем к
        # делу? ...
        t = 1
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=25, trans_time=2, loop=True,
            time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=2.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=5, time_scale=0.7,
            trans_time=1, time_delay=t)
        t += 2.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_alaric_near'), duration=1.75, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_alaric_near'), duration=1.25, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 1.8
        hatcher.motion(group=MAIN, anim=Female.Sc_FMHEAD_MOTION_MOUTH_CLENCH_000LV_, duration=1, trans_time=0.4,
            time_delay=t)
        t += 0.2
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.8, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.25, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        cam_greetings.move_cam(group=MAIN, index=3, duration=30, smooth=True, time_delay=t)
        t += 1
        hatcher.motion(group=MAIN, anim=Female.Sc_FMHEAD_BASEPOSE_000LV_02_01, duration=0.5, time_scale=0.8,
            trans_time=0.5, time_delay=t)
        hatcher.facial(group=MAIN, index=30, auto_lip=True, extra_delay=0)

        # m06_offer 40: Hatcher.
        # Отлично! Как вы уже поняли есть некий объект - Сфера. В свое время его обнаружил еще Орден, но тогда
        # никто не смог понять что это, для чего предназначено и как работает. И про Сферу забыли.
        t = 0
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=4, time_scale=0.6,
            trans_time=1, time_delay=t)
        t += 3
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_alaric_near'), duration=2.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_alaric_near'), duration=1.4, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 1
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, duration=8, time_scale=0.6,
            trans_time=1, loop=True, time_delay=t)
        t += 5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=2.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.4, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 2
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_CONV_LHNDUP_TRNS_000LV_XA_01, duration=2,
            time_scale=0.5, trans_time=1, time_delay=t)
        hatcher.facial(group=MAIN, index=40, auto_lip=True, extra_delay=0)

        # m06_offer 50: Hatcher.
        # А теперь мы узнаём что рейнландцам удалось подобрать к ней ключ и они проводят на ней свои
        # исследования. Есть обоснованное мнение, что ничем хорошим это не закончится. Поэтому исследования
        # эти нужно, как бы это сказать... закрыть.
        t = 0.7
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_CONV_LHND_CASL_000LV_xa_03, duration=3,
            time_scale=0.5, trans_time=1, loop=True, time_delay=t)
        t += 1.3
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_alaric_near'), duration=2.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_alaric_near'), duration=1.4, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 1.8
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_CONV_LHNDDN_TRNS_000LV_XA_01, duration=3,
            time_scale=0.5, trans_time=1.5, time_delay=t)
        t += 0.2
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=2.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.4, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 1
        hatcher.motion(group=MAIN, anim=Female.Sc_FMHEAD_BASEPOSE_000LV_02_01, duration=0.5, time_scale=0.8,
            trans_time=0.5, time_delay=t)
        t += 3
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_alaric_near'), duration=2.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_alaric_near'), duration=1.4, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 1
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=5, time_scale=0.7,
            trans_time=1, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_hatcher'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_hatcher'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 2
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        hatcher.facial(group=MAIN, index=50, auto_lip=True, extra_delay=0)

        # m06_offer 60: Trent.
        # Ха-ха-ха, отлично. Если вы не смогли подобрать к Сфере ключ сами, то никто не должен. А если
        # подобрал, то нужно срочно устранить либо ключ, либо Сферу, либо того кто это сделал. Браво! Так не
        # доставайся же ты никому.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=6, time_delay=t)
        t += 6
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_GRABR_CHIN_RLEASE_000LV_XA_02, duration=3,
            time_scale=0.6, trans_time=1, time_delay=t)
        t += 1
        trent.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_GESTR_FIST_000LV_00, duration=4, trans_time=0.25,
            time_delay=t)
        t += 3
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_HOLD_CHIN_RLEASE_000LV_XA_03, duration=7,
            time_scale=0.6, trans_time=1, time_delay=t)
        t += 1
        trent.motion(group=MAIN, anim=Female.Sc_FMHAND_NEUT_RGHT_000LV_A_00, duration=4, time_scale=0.5,
            trans_time=1, time_delay=t)
        t += 2.5
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=6, trans_time=1,
            time_delay=t)
        trent.facial(group=MAIN, index=60, auto_lip=True, extra_delay=0)

        # m06_offer 70: Hatcher.
        # Я не разделяю вашего сарказма, мистер Трент. В прошлый раз подобная ситуация случилась, когда другие
        # рейнландские ученые нашли нечто в Омикронах. Ох уж мне эти неугомонные рейнландцы.
        t = 0
        cam_hatcher.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_TILT_HEAD_QUZZCLLY_000LV_XA_04, duration=4,
            time_scale=0.6, start_time=1, time_delay=t)
        t += 2
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=5, time_scale=0.8,
            trans_time=1, time_delay=t)
        t += 2
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_CONV_RHNDUP_TRNS_000LV_XA_02, duration=2,
            time_scale=0.6, trans_time=1, time_delay=t)
        t += 2
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_CONV_RHNDDN_TRNS_000LV_XA_02, duration=4,
            time_scale=0.5, trans_time=1, time_delay=t)
        t += 4
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=4, time_scale=0.6,
            trans_time=1, time_delay=t)
        hatcher.facial(group=MAIN, index=70, auto_lip=True, extra_delay=0)

        # m06_offer 80: Hatcher.
        # И все закончилось тем самым кризисом, про который я вам рассказывала в присутствие профессора
        # Мандрейка. Вы поняли, о чем я?
        t = 2
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_TILT_HEAD_QUZZCLLY_000LV_XA_04, duration=2,
            time_scale=0.6, start_time=1, trans_time=1, time_delay=t)
        t += 2
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, duration=5, trans_time=3,
            loop=True, time_delay=t)
        hatcher.facial(group=MAIN, index=80, auto_lip=True, extra_delay=0)

        # m06_offer 90: Trent.
        # Да, понял. Не стоит шутить с ящиком Пандоры.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=8, loop=True, time_delay=t)
        trent.facial(group=MAIN, index=90, auto_lip=True, extra_delay=0)

        # m06_offer 100: Hatcher.
        # Хорошо, с моральной подоплекой наших действий мы разобрались, теперь про материальную. Вы получите
        # вознаграждение втрое больше обычного, и удостоверения внештатных сотрудников СБА.
        t = 0
        cam_hatcher.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_alaric_near'), duration=2.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_alaric_near'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 4
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=5, time_scale=0.7,
            trans_time=1, time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=2.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.4, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_alaric_near'), duration=2.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_alaric_near'), duration=1.4, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 1
        EyeIkEvent(root=self, group=MAIN, char_name=alaric.name,
            target_name=self.get_automarker_name('alaric_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=25, transition_duration=1, time_delay=t)
        hatcher.facial(group=MAIN, index=100, auto_lip=True, extra_delay=0)

        # m06_offer 110: Alaric.
        # Чёрт побери, я за! Где ставить подпись? Могу кровью!
        t = 0
        cam_alaric.set(group=MAIN, time_delay=t)
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_SHRG_SHLDRS_BIG_000LV_XA_03, duration=1.25,
            time_scale=0.6, trans_time=1, time_delay=t)
        t += 1.25
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=6, time_scale=0.6,
            trans_time=2.2, loop=True, time_delay=t)
        t += 0.25
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('alaric_eye_ik'),
            target_name=self.get_automarker_name('head_hatcher_near'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 2
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_alaric_near_far'), duration=0.01, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_alaric_near'), duration=0.01, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 0.8
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('alaric_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        alaric.facial(group=MAIN, index=110, auto_lip=True, extra_delay=0)
        # Действие после исходного окна реплики.
        t = 0
        alaric.motion(group=MAIN, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=2, trans_time=2, time_delay=t)
        main_group.append_time(0.3)

        # m06_offer 120: Trent.
        # Аларик, угомонись. Мисс Хетчер, а что конкретно нужно сделать? Уничтожить Сферу, уничтожить ученых?
        # Мне это совсем не по душе, я всё-таки не наёмный убийца.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_hatcher'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_hatcher'), duration=1.25, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 6.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 2
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_CONV_RHNDDN_TRNS_000LV_XA_02, duration=2,
            time_scale=0.5, start_time=1.2, time_delay=t)
        trent.facial(group=MAIN, index=120, auto_lip=True, extra_delay=0)

        # m06_offer 130: Hatcher.
        # А вы уверены? Нет, все не так страшно и кроваво, как вы сейчас расписали. В полученных нами
        # документах профессор нашел способ сделать Сферу невосприимчивой к внешним воздействиям, как сказал
        # профессор "закрыться".
        t = 0
        cam_hatcher.set(group=MAIN, time_delay=t)
        cam_greetings.move_cam(group=MAIN, index=3, duration=18, smooth=True, time_delay=t)
        t += 2.2
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=5, time_scale=0.6,
            trans_time=1, time_delay=t)
        t += 4.8
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_alaric_near'), duration=2.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=1.8, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 0.5
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, duration=15, trans_time=1,
            loop=True, time_delay=t)
        t += 2.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=2.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.4, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        hatcher.facial(group=MAIN, index=130, auto_lip=True, extra_delay=0)

        # m06_offer 140: Hatcher.
        # Все дальнейшие подробности - в том случае, если вы согласитесь.
        hatcher.facial(group=MAIN, index=140, auto_lip=True, extra_delay=0)
