"""m08_offer: полная постановка из master; точки в m08_offer.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character, EyeIkEvent, Female, LookAtCamera, MAIN, Male, MoveEvent, NeckIkEvent, RotateAxisEvent, SoundEvent,
)
from story.cutscenes.anim import (
    Female, Male, Trent as TrentAnim
)
from story import actors



class M08OfferScene(Scene):
    DUMP_FILE = 'm08_offer'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Персонажи, камеры, реквизит и звук.
        kaytlin = Character(root=self, actor=actors.Kaitlyn, name='Char_kaytlin', light_group=0,
            init_point='Char_kaytlin', rotate_from_quat=True, appearance='kaytlin', actor_name='Kaytlin')
        brighton = Character(root=self, actor=actors.Brighton, name='Char_brighton', light_group=0,
            init_point='Char_brighton', rotate_from_quat=True, appearance='brighton', actor_name='Brighton')
        darcy = Character(root=self, actor=actors.Darcy, name='Char_darcy', light_group=0,
            init_point='Char_darcy', rotate_from_quat=True, appearance='darcy', actor_name='Darcy')
        trent = Character(root=self, actor=actors.Trent, name='Char_trent', light_group=0,
            init_point='Char_trent', rotate_from_quat=True, appearance='trent', actor_name='Player')
        cam_start = LookAtCamera(root=self, name='cam_start', fov=20, look_duration=70)
        cam_start_darcy = LookAtCamera(root=self, name='cam_start_darcy', fov=20, look_duration=70)
        cam_start_trent = LookAtCamera(root=self, name='cam_start_trent', fov=20, look_duration=70)
        cam_greetings = LookAtCamera(root=self, name='cam_greetings', fov=20, look_duration=70)
        cam_greetings_kaytlin = LookAtCamera(root=self, name='cam_greetings_kaytlin', fov=15, look_duration=70)
        cam_darcy_sit = LookAtCamera(root=self, name='cam_darcy_sit', fov=22, look_duration=70)
        cam_brighton = LookAtCamera(root=self, name='cam_brighton', fov=18, look_duration=710)
        cam_brighton_near = LookAtCamera(root=self, name='cam_brighton_near', fov=18, look_duration=710)
        cam_trent_sit = LookAtCamera(root=self, name='cam_trent_sit', fov=18, look_duration=710)
        cam_trent_far = LookAtCamera(root=self, name='cam_trent_far', fov=18, look_duration=710)
        cam_trent_near = LookAtCamera(root=self, name='cam_trent_near', fov=18, look_duration=710)
        cam_trent_xnear = LookAtCamera(root=self, name='cam_trent_xnear', fov=15, look_duration=710)
        cam_kaytlin = LookAtCamera(root=self, name='cam_kaytlin', fov=15, look_duration=710)
        RotateAxisEvent(root=self, group=MAIN, object_name=kaytlin.name, angle=-125, axis='Y_AXIS', duration=0,
            smooth=False, time_delay=0.01)
        RotateAxisEvent(root=self, group=MAIN, object_name=brighton.name, angle=10, axis='Y_AXIS', duration=0,
            smooth=False, time_delay=0.01)

        # Исходные точки взгляда.

        # Вход.
        t = 0
        kaytlin.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_IDLE_000LV_XA_05, duration=10, time_delay=t)
        brighton.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=100, time_scale=0.6,
            loop=True, time_delay=t)

        def unused():
            cam_start.move_cam(group=MAIN, index=2, duration=9, smooth=True, time_delay=t)
            cam_start.move_focus(group=MAIN, index=2, duration=7, smooth=True, time_delay=t)
            trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=2.6, loop=True, time_delay=t)
            RotateAxisEvent(root=self, group=MAIN, object_name=darcy.name, angle=-67, axis='Y_AXIS', duration=0,
                smooth=False, time_delay=t)
            darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_HOLD_ARMS_CROSSED_000LV_XA_03, duration=1,
                time_delay=t)
            t += 0.01
            cam_start.set(group=MAIN, time_delay=t)
            t += 2.59
            trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=6, time_delay=t)
            RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=5, axis='Y_AXIS', duration=1,
                smooth=False, time_delay=t)
            t += 0.4
            darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_UNCRSS_ARMS_000LV_XA_03, duration=5, time_scale=0.8,
                time_delay=t)
            main_group.append_time(5)

            # m08_offer 10: Darcy.
            # Привет. Мы сейчас пройдем в одну комнату, в которой будет пара очень больших шишек.
            t = 0
            cam_start_darcy.set(group=MAIN, time_delay=t)
            t += 3
            darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=5,
                time_scale=0.8, time_delay=t)
            darcy.facial(group=MAIN, index=10, auto_lip=True)

            # m08_offer 20: Darcy.
            # Очень прошу, постарайся вести себя посдержаннее.
            t = 2.7
            darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_WALK_TRNS_270LV_XA_02, duration=5, time_scale=0.8,
                trans_time=1, time_delay=t)
            darcy.facial(group=MAIN, index=20, auto_lip=True)

            # m08_offer 30: Trent.
            # Ничего не понял, но постараюсь.
            t = 0
            cam_start_trent.set(group=MAIN, time_delay=t)
            t += 0.5
            NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
                target_name=self.get_automarker_name('head_darcy_move_from_start'), target_type='ROOT',
                target_part='', up='NEG_Y_AXIS', front='Z_AXIS', duration=5, transition_duration=2, time_delay=t)
            t += 2.2
            trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01, duration=1, time_scale=0.5,
                trans_time=1, time_delay=t)
            RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=-8, axis='Y_AXIS', duration=1,
                smooth=False, time_delay=t)
            trent.facial(group=MAIN, index=30, auto_lip=True)
            # Действие после исходного окна реплики.

        t = 0
        cam_greetings.set(group=MAIN, time_delay=t)
        cam_greetings.move_cam(group=MAIN, index=2, duration=7, smooth=True, time_delay=t)
        cam_greetings.move_focus(group=MAIN, index=2, duration=5, smooth=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=darcy.name,
            target_name=self.get_automarker_name('point_darcy_walk'), duration=0, smooth=False, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_WLKG_000LV_XA_01, duration=4, time_scale=0.6, loop=True,
            time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('point_trent_walk'), duration=0, smooth=False, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=4, time_scale=0.6, start_time=0.5,
            loop=True, time_delay=t)
        t += 0.01
        RotateAxisEvent(root=self, group=MAIN, object_name=darcy.name, angle=25, axis='Y_AXIS', duration=0,
            smooth=False, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=25, axis='Y_AXIS', duration=0,
            smooth=False, time_delay=t)
        t += 0.99
        NeckIkEvent(root=self, group=MAIN, char_name=brighton.name,
            target_name=self.get_automarker_name('head_darcy_near_table'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=15, transition_duration=2, time_delay=t)
        main_group.append_time(2.2)

        # m08_offer 40: Brighton.
        # А это мисс Дерси, наша краса и надежда на светлое будущее.
        t = 0
        NeckIkEvent(root=self, group=MAIN, char_name=kaytlin.name,
            target_name=self.get_automarker_name('head_darcy_near_table'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=5, transition_duration=2, time_delay=t)
        brighton.facial(group=MAIN, index=40, auto_lip=True)

        # m08_offer 50: Kaitlyn.
        # А это, если я все правильно поняла, эксперт по Ордену, о котором мне столько рассказывали.
        t = 0
        cam_greetings_kaytlin.set(group=MAIN, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=kaytlin.name,
            target_name=self.get_automarker_name('head_trent_near_table_up'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=15, transition_duration=2, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=kaytlin.name,
            target_name=self.get_automarker_name('head_trent_near_table'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=15, transition_duration=2, time_delay=t)
        t += 2
        kaytlin.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_GRABR_CHIN_RLEASE_000LV_XA_03, duration=7,
            time_scale=0.3, trans_time=1, time_delay=t)
        t += 2
        kaytlin.motion(group=MAIN, anim=Female.Sc_FMHAND_HNEUT_GESTR_THUMB_000LV_00, duration=0.5, trans_time=1,
            time_delay=t)
        t += 4
        t += 0.01
        kaytlin.facial(group=MAIN, index=50, auto_lip=True)

        NeckIkEvent(root=self, group=MAIN, char_name=darcy.name,
            target_name=self.get_automarker_name('darcy_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=2555, transition_duration=1, time_delay=-1)
        EyeIkEvent(root=self, group=MAIN, char_name=darcy.name,
            target_name=self.get_automarker_name('darcy_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=2555, transition_duration=1, time_delay=-1)

        RotateAxisEvent(root=self, group=MAIN, object_name=darcy.name, angle=-15, axis='Y_AXIS', duration=0,
            smooth=False, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=darcy.name,
            target_name=self.get_automarker_name('point_darcy_sit'), duration=0, smooth=False, adjust_pos=True,
            adjust_orient=True, time_delay=-0.2)
        RotateAxisEvent(root=self, group=MAIN, object_name=darcy.name, angle=-15, axis='Y_AXIS', duration=0,
            smooth=False, time_delay=-0.15)
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, duration=1, time_delay=-0.1)

        # m08_offer 60: Darcy.
        # Да, это мистер Трент. Трент, это адмирал Брайтон и принцесса Кейтлин.
        t = 0
        cam_darcy_sit.set(group=MAIN, time_delay=0)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('darcy_head_ik'),
            target_name=self.get_automarker_name('head_trent_front'), duration=2.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('darcy_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_CONV_LHNDUP_TRNS_000LV_XA_01, duration=2,
            time_scale=0.5, trans_time=1, time_delay=t)
        t += 0.8
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_CONV_LHND_CASL_000LV_xa_03, duration=3,
            time_scale=0.4, trans_time=1, loop=True, time_delay=t)
        t += 3
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_CONV_LHNDDN_TRNS_000LV_XA_01, duration=3,
            time_scale=0.5, trans_time=1.5, time_delay=t)
        t += 0.2
        NeckIkEvent(root=self, group=MAIN, char_name=brighton.name,
            target_name=self.get_automarker_name('brighton_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=2555, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=brighton.name,
            target_name=self.get_automarker_name('brighton_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=2555, transition_duration=1, time_delay=t)
        darcy.facial(group=MAIN, index=60, auto_lip=True)

        # m08_offer 70: Brighton.
        # И у нас к вам, мистер Трент, чрезвычайно важное дело.
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('point_trent_sit'), duration=0, smooth=False, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=1050, time_scale=0.6,
            loop=True, time_delay=t)
        cam_brighton.set(group=MAIN, time_delay=t)
        t += 0.01
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=20, axis='Y_AXIS', duration=0,
            smooth=False, time_delay=t)
        t += 0.99
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=555, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=555, transition_duration=1, time_delay=t)
        brighton.facial(group=MAIN, index=70, auto_lip=True)

        # m08_offer 80: Trent.
        # Шо, опять?
        t = 0
        cam_trent_xnear.set(group=MAIN, time_delay=t)
        t += 1.7
        trent.facial(group=MAIN, index=80, auto_lip=True)


        cam_brighton_near.set(group=MAIN, time_delay=0)

        # m08_offer 90: Brighton.
        # Мистер Трент, давайте чуточку серьёзнее. Речь идет о государственной безопасности Бретонии.
        brighton.facial(group=MAIN, index=90, auto_lip=True)

        # m08_offer 100: Trent.
        # Я постараюсь.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=100, auto_lip=True)

        # m08_offer 110: Brighton.
        # У нас для вас, мистер Трент, будет небольшое задание по вашему профилю.
        t = 0
        cam_brighton.set(group=MAIN, time_delay=t)
        t += 1
        brighton.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_GESTR_SELF_000LV_XA_03, duration=2.3, time_scale=0.2,
            trans_time=0.3, time_delay=t)
        brighton.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_POINT_RGHT_CASL_000LV_XB_01, duration=2.3,
            time_scale=0.5, time_delay=t)
        t += 2.5
        brighton.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=3, trans_time=1,
            time_delay=t)
        brighton.facial(group=MAIN, index=110, auto_lip=True)

        # m08_offer 120: Trent.
        # Моему профилю?
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=120, auto_lip=True)

        # m08_offer 130: Brighton.
        # Орден, мистер Трент, Орден.
        t = 0
        cam_brighton_near.set(group=MAIN, time_delay=t)
        brighton.facial(group=MAIN, index=130, auto_lip=True)

        # m08_offer 140: Trent.
        # А... Аааа...
        t = 0
        cam_trent_xnear.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_SHRG_SHLDRS_SMALL_000LV_XA_03, duration=100,
            time_scale=0.4, time_delay=t)
        # trent.motion(group=MAIN, anim=TrentAnim.Sc_dx_s020x_1601_Trent, duration = 3.81, time_scale = 1, trans_time = 0.25)

        trent.motion(group=MAIN, anim = TrentAnim.Sc_dx_s055b_0701_Trent,
            duration = 3.5, start_time = 0.2, time_scale = 0.6, trans_time = 0)
        trent.motion(group=MAIN, anim = TrentAnim.Sc_dx_s026b_1401_Trent,
            duration = 3.5, start_time = 0.2, time_scale = 0.2, trans_time = 0.25, time_delay=0.5)
        trent.motion(group=MAIN, anim = TrentAnim.Sc_dx_s055b_0701_Trent,
            duration = 3.5, start_time = 0.2, time_scale = 0.6, trans_time = 1, time_delay=2)

        trent.facial(group=MAIN, index=140, auto_lip=False, no_anim=True)


        # m08_offer 150: Brighton.
        # Мистер Трент, смею вас заверить, что данная миссия находится на контроле у самых высокопоставленных
        # лиц Бретонии.
        t = 0
        cam_brighton.set(group=MAIN, time_delay=t)
        t += 6
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('brighton_head_ik'),
            target_name=self.get_automarker_name('head_kaytlin_front_fwd2'), duration=2.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('brighton_eye_ik'),
            target_name=self.get_automarker_name('head_kaytlin_lwr'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        brighton.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_GESTL_180LV_XA_03, duration=100, time_scale=0.4,
            trans_time=0.5, time_delay=t)
        brighton.facial(group=MAIN, index=150, auto_lip=True)

        # m08_offer 160: Brighton.
        # Одно то, что на встрече с вами присутствует принцесса Кейтлин, должно о многом вам говорить.
        t = 2.3
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('brighton_head_ik'),
            target_name=self.get_automarker_name('head_trent_brightonside_front'), duration=2, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('brighton_eye_ik'),
            target_name=self.get_automarker_name('head_trent_brightonside'), duration=1.25, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        brighton.facial(group=MAIN, index=160, auto_lip=True)
        main_group.append_time(0.3)

        # m08_offer 170: Trent.
        # Минуй нас пуще всех печалей и барский гнев, и барская любовь...
        t = 0
        cam_trent_sit.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=170, auto_lip=True)

        # m08_offer 180: Brighton.
        # Я не понимаю вашего скептицизма, мистер Трент, будьте чуточку прозорливее
        t = 0
        cam_brighton_near.set(group=MAIN, time_delay=t)
        brighton.facial(group=MAIN, index=180, auto_lip=True)

        # m08_offer 190: Brighton.
        # Вы окажете услугу нам, а мы, при случае, окажем услугу вам.
        brighton.facial(group=MAIN, index=190, auto_lip=True)
        main_group.append_time(0.5)

        # m08_offer 200: Trent.
        # Допустим. А в чём задание-то?
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=200, auto_lip=True)

        # m08_offer 210: Brighton.
        # Вот это уже серьёзный разговор, мистер Трент. Принцесса?
        t = 0
        cam_brighton.set(group=MAIN, time_delay=t)
        t += 2
        NeckIkEvent(root=self, group=MAIN, char_name=kaytlin.name,
            target_name=self.get_automarker_name('kaytlin_ik_not_interested_head'), target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS', duration=1000, transition_duration=2, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=kaytlin.name,
            target_name=self.get_automarker_name('kaytlin_ik_not_interested_eye'), target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS', duration=1000, transition_duration=2, time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('brighton_head_ik'),
            target_name=self.get_automarker_name('head_kaytlin_front_fwd2'), duration=1.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('brighton_eye_ik'),
            target_name=self.get_automarker_name('head_kaytlin_lwr'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 0.5
        kaytlin.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_GRABR_HEAD_RLEASE_000LV_XA_03, duration=7,
            trans_time=1, time_delay=t)
        kaytlin.motion(group=MAIN, anim=Female.Sc_FMHAND_HNEUT_GESTR_CASL_000LV_00, duration=0.9, trans_time=1,
            time_delay=t)
        brighton.facial(group=MAIN, index=210, auto_lip=True)

        # m08_offer 215: Kaitlyn.
        # Угу...
        t = 0
        cam_kaytlin.set(group=MAIN, time_delay=t)
        kaytlin.motion(group=MAIN, anim=Female.Sc_FMHEAD_MAD_COLD_000LV_XA_, duration=5, start_time=0.8,
            trans_time=0.25, time_delay=t)
        t += 2.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('brighton_head_ik'),
            target_name=self.get_automarker_name('head_trent_brightonside_front'), duration=2, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('brighton_eye_ik'),
            target_name=self.get_automarker_name('head_trent_brightonside'), duration=1.25, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        line_sound = self.lookup_single_sound(215)
        SoundEvent(root=self, group=MAIN, sound_name=line_sound.get_nickname())
        main_group.append_time(3)

        cam_brighton.set(group=MAIN, time_delay=0)

        # m08_offer 220: Brighton.
        # Мистер Трент, в свое время правительство Бретонии заключило некое соглашение с Орденом.
        brighton.facial(group=MAIN, index=220, auto_lip=True)

        # m08_offer 230: Brighton.
        # Оно сводилось к тому, что Бретония, хм…
        t = 1.8
        brighton.motion(group=MAIN, anim=Male.Sc_MLHEAD_MAD_COLD_000LV_XA_, duration=4.7, start_time=0.6,
            trans_time=0.25, time_delay=t)
        t += 0.7
        brighton.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=100, time_scale=0.7,
            time_delay=t)
        brighton.facial(group=MAIN, index=230, auto_lip=True)

        # m08_offer 235: Brighton.
        # Мистер Трент, а вы слышали о проблеме кочевников?
        brighton.facial(group=MAIN, index=235, auto_lip=True)

        # m08_offer 240: Trent.
        # В общем и целом.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=240, auto_lip=True)

        # m08_offer 250: Brighton.
        # Отлично. Чуточку осторожности не помешает, вы же меня понимаете?
        t = 0
        cam_brighton.set(group=MAIN, time_delay=t)
        t += 4
        brighton.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDUP_TRNS_000LV_XA_02, duration=4,
            time_delay=t)
        brighton.facial(group=MAIN, index=250, auto_lip=True)

        # m08_offer 260: Brighton.
        # Так вот, по этому соглашению Бретония отказывалась от своих интересов в секторах так называемого
        # "Наследия Номадов", кочевников то есть. Вы понимаете, о чем я, мистер Трент?
        t = 0.6
        brighton.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00, duration=10, time_delay=t)
        t += 0.7
        brighton.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CONV_RHND_CASL_000LV_xb_03, duration=2.3,
            time_scale=0.5, trans_time=1, time_delay=t)
        t += 2.3
        brighton.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDDN_TRNS_000LV_XA_02, duration=4,
            trans_time=1, time_delay=t)
        brighton.facial(group=MAIN, index=260, auto_lip=True)

        # m08_offer 270: Trent.
        # Чуточку
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=270, auto_lip=True)

        # m08_offer 280: Brighton.
        # Гхм, хорошо. Взамен Орден обязался ограничить доступ к этим системам для всех. То есть совсем
        # ограничить. Вы меня понимаете, мистер Трент?
        t = 0
        cam_brighton.set(group=MAIN, time_delay=t)
        brighton.facial(group=MAIN, index=280, auto_lip=True)

        # m08_offer 290: Brighton.
        # И мы наивно полагали, что СБА, как прямой наследник Ордена, будет придерживаться достигнутых
        # договоренностей. И что же мы видим сейчас?
        brighton.facial(group=MAIN, index=290, auto_lip=True)

        # m08_offer 300: Trent.
        # Что?...
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=300, auto_lip=True)

        # m08_offer 310: Brighton.
        # А то, что эти ублюдки из ИРА во всю осваивают Тау-44.
        t = 0
        cam_brighton_near.set(group=MAIN, time_delay=t)
        brighton.facial(group=MAIN, index=310, auto_lip=True)
        # 		{animation="Sc_dx_s063x_0701_vonclaussn",
        # 		 duration=4.3, start_time=0, time_scale=1.1, trans_time=0.25, weight=1, heading=-1}
        main_group.append_time(0.2)

        # m08_offer 320: Trent.
        # Вот сволочи. А Ира - это кто?
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=320, auto_lip=True)

        # m08_offer 330: Brighton.
        # Не "кто" а "что". Группа фанатиков, в том числе религиозных, требующих независимости Ирландии от
        # Британской короны.
        t = 0
        cam_brighton.set(group=MAIN, time_delay=t)
        brighton.facial(group=MAIN, index=330, auto_lip=True)

        # m08_offer 340: Trent.
        # Достаточно забавно, учитывая что в секторе Сириуса нет ни Ирландии, ни Британской короны.
        t = 0
        cam_trent_sit.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=340, auto_lip=True)

        # m08_offer 350: Kaitlyn.
        # Мистер Трент...
        t = 0
        cam_kaytlin.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('kaytlin_ik_not_interested_head'),
            target_name=self.get_automarker_name('kaytlin_ik_not_interested_head_pos2'), duration=1.5,
            smooth=True, adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('kaytlin_ik_not_interested_eye'),
            target_name=self.get_automarker_name('kaytlin_ik_not_interested_eye_pos2'), duration=1, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        kaytlin.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_HOLD_HEAD_RLEASE_000LV_XA_03, duration=7,
            time_scale=0.5, time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('kaytlin_ik_not_interested_eye'),
            target_name=self.get_automarker_name('kaytlin_ik_not_interested_eye_pos3'), duration=1, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('kaytlin_ik_not_interested_head'),
            target_name=self.get_automarker_name('kaytlin_ik_not_interested_head_pos3'), duration=1, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 1
        kaytlin.motion(group=MAIN, anim=Female.Sc_FMHEAD_MAD_COLD_000LV_XA_, duration=0.8, trans_time=0.5,
            time_delay=t)
        kaytlin.facial(group=MAIN, index=350, auto_lip=True)

        # m08_offer 360: Trent.
        # А что? Дома Ирландии, насколько я знаю, нет.
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_kaytlin_front'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_kaytlin'), duration=1.25, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        cam_trent_sit.set(group=MAIN, time_delay=t)
        t += 2.6
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('brighton_head_ik'),
            target_name=self.get_automarker_name('head_kaytlin_front_fwd2'), duration=2.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('brighton_eye_ik'),
            target_name=self.get_automarker_name('head_kaytlin_lwr'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        trent.facial(group=MAIN, index=360, auto_lip=True)

        # m08_offer 370: Kaitlyn.
        # А ирландцы, к сожалению, есть...
        t = 0
        cam_kaytlin.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('kaytlin_ik_not_interested_head'),
            target_name=self.get_automarker_name('kaytlin_ik_not_interested_head_init'), duration=2.5,
            smooth=True, adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('kaytlin_ik_not_interested_eye'),
            target_name=self.get_automarker_name('kaytlin_ik_not_interested_eye_init'), duration=1.8, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.6
        kaytlin.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_GRABR_HEAD_RLEASE_000LV_XA_03, duration=7,
            time_scale=0.7, trans_time=1, time_delay=t)
        kaytlin.motion(group=MAIN, anim=Female.Sc_FMHAND_HNEUT_GESTR_CASL_000LV_00, duration=0.9, trans_time=1,
            time_delay=t)
        t += 2.5
        kaytlin.motion(group=MAIN, anim=Female.Sc_FMHEAD_MAD_COLD_000LV_XA_, duration=0.6, trans_time=0.5,
            time_delay=t)
        kaytlin.facial(group=MAIN, index=370, auto_lip=True)

        # m08_offer 380: Brighton.
        # Теперь вы понимаете, мистер Трент, насколько все это дико?
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('brighton_head_ik'),
            target_name=self.get_automarker_name('head_trent_brightonside_front'), duration=2, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('brighton_eye_ik'),
            target_name=self.get_automarker_name('head_trent_brightonside'), duration=1.25, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        cam_brighton.set(group=MAIN, time_delay=t)
        t += 3
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_brighton'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_brighton'), duration=1.25, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        brighton.facial(group=MAIN, index=380, auto_lip=True)

        # m08_offer 390: Trent.
        # Допустим. Что требуется от меня?
        t = 0
        cam_trent_sit.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=390, auto_lip=True)

        # m08_offer 400: Brighton.
        # Чуточку помочь нам. В составе оперативного отряда вылететь в Тау-44, и очистить систему от
        # присутствия ИРА.
        t = 0
        cam_brighton.set(group=MAIN, time_delay=t)
        t += 6.8
        brighton.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=5, time_scale=0.8,
            trans_time=0.3, time_delay=t)
        brighton.facial(group=MAIN, index=400, auto_lip=True)

        # m08_offer 410: Brighton.
        # Кроме всего прочего, мы подозреваем что СБА напрямую во всем этом замешано. И здесь нам пригодитесь
        # вы.
        t = 3.8
        brighton.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_GESTR_SELF_000LV_XA_03, duration=2.3, time_scale=0.2,
            trans_time=0.3, time_delay=t)
        brighton.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_POINT_RGHT_CASL_000LV_XB_01, duration=2.3,
            time_scale=0.5, time_delay=t)
        t += 2.5
        brighton.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=3, trans_time=1,
            time_delay=t)
        brighton.facial(group=MAIN, index=410, auto_lip=True)

        # m08_offer 420: Trent.
        # В качестве кого? Того, кто ткнет на кого-нибудь пальцем и скажет "он из СБА"? Звучит не очень
        # убедительно.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=420, auto_lip=True)

        # m08_offer 430: Kaitlyn.
        # Ахх...
        t = 0
        cam_kaytlin.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('kaytlin_ik_not_interested_head'),
            target_name=self.get_automarker_name('kaytlin_ik_not_interested_head_pos2'), duration=1.5,
            smooth=True, adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('kaytlin_ik_not_interested_eye'),
            target_name=self.get_automarker_name('kaytlin_ik_not_interested_eye_pos2'), duration=1, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        kaytlin.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_HOLD_HEAD_RLEASE_000LV_XA_03, duration=7,
            time_scale=0.5, time_delay=t)
        kaytlin.motion(group=MAIN, anim=Female.Sc_FMHEAD_MAD_COLD_000LV_XA_, duration=5, trans_time=0.5,
            time_delay=t)
        t += 1.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('kaytlin_ik_not_interested_head'),
            target_name=self.get_automarker_name('kaytlin_ik_not_interested_head_pos3'), duration=1, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('kaytlin_ik_not_interested_eye'),
            target_name=self.get_automarker_name('kaytlin_ik_not_interested_eye_pos3'), duration=1, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        line_sound = self.lookup_single_sound(430)
        SoundEvent(root=self, group=MAIN, sound_name=line_sound.get_nickname())
        main_group.append_time(2.5)

        # m08_offer 435: Kaitlyn.
        # А пятьдесят тысяч звучат достаточно убедительно? Вы просто примите участие в заплыве, вам не
        # обязательно становиться победителем.
        t = 5
        kaytlin.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_CONV_RHNDDN_TRNS_000LV_XA_02, duration=8,
            time_scale=0.3, trans_time=1, time_delay=t)
        kaytlin.motion(group=MAIN, anim=Female.Sc_FMHAND_HNEUT_GESTR_CASL_000LV_00, duration=10, time_scale=0.6,
            time_delay=t)
        t += 7.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_kaytlin_front'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_kaytlin'), duration=1.25, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        kaytlin.facial(group=MAIN, index=435, auto_lip=True)

        main_group.append_time(1)
