"""Встреча с Якобо: обычный API Pythonlancer, относительная постановка реплик."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    MAIN, Character, LookAtCamera, Prop, Sound, MotionEvent, MoveFastEvent, ConnectHardpointEvent,
)
from story.cutscenes.anim import (
    Male, Trent,
)
from story import actors


class Notebook(Prop):
    COMPOUND_TEMPLATE_NAME = 'notebook'


class Bartender(actors.Actor):
    NAME = 'bartender'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'botzler'


class BartenderFixture(Bartender):
    NAME = 'bartender_fixture'
    GAME_ACTOR = 'bartender'


class M02JacoboOfferScene(Scene):
    DUMP_FILE = 'm02_jacobo_offer'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Персонажи.
        trent = Character(root=self, actor=actors.Trent, light_group=0,
            init_point='Char_trent', rotate_from_quat=True)
        jacobo = Character(root=self, actor=actors.Jacobo, light_group=0,
            init_point='Char_jacobo', rotate_from_quat=True)
        bartender = Character(root=self, actor=Bartender, light_group=0,
            init_point='Char_bartender', rotate_from_quat=True, bind_actor=False)
        bartender_fixture = Character(root=self, actor=BartenderFixture, light_group=0,
            init_point='Char_bartender_fixture', rotate_from_quat=True)

        # Камеры: *_focus, *2 / *_focus2 и следующие позиции в Blender.
        cam_begin = LookAtCamera(root=self, name='cam_begin', fov=20)
        cam_jacobo_eyes = LookAtCamera(root=self, name='cam_jacobo_eyes', fov=12)
        cam_bartender_pointer = LookAtCamera(root=self, name='cam_bartender_pointer', fov=25)
        cam_jacobo_fingerprint = LookAtCamera(root=self, name='cam_jacobo_fingerprint', fov=15)
        cam_trent_arrival = LookAtCamera(root=self, name='cam_trent_arrival', fov=35)
        cam_trent_stand = LookAtCamera(root=self, name='cam_trent_stand', fov=25)
        cam_trent_stand_far = LookAtCamera(root=self, name='cam_trent_stand_far', fov=22)
        cam_walkout1 = LookAtCamera(root=self, name='cam_walkout1', fov=20)
        cam_walkout2 = LookAtCamera(root=self, name='cam_walkout2', fov=20)

        # Реквизит и звук.
        notebook = Notebook(root=self, name='notebook', light_group=0,
            init_point='prop_notebook', rotate_from_quat=True)
        sfx_ui_react_accept01 = Sound(root=self, name='sfx_ui_react_accept01', sound='sfx_ui_react_accept01',
            attenuation=-30, dmin=50, dmax=1000, priority=None)
        sfx_ui_react_accept02 = Sound(root=self, name='sfx_ui_react_accept02', sound='sfx_ui_react_accept02',
            attenuation=-30, dmin=50, dmax=1000, priority=None)
        sfx_ui_react_data01 = Sound(root=self, name='sfx_ui_react_data01', sound='sfx_ui_react_data01',
            attenuation=-20, dmin=50, dmax=1000, priority=None)
        sfx_ui_react_denied01 = Sound(root=self, name='sfx_ui_react_denied01', sound='sfx_ui_react_denied01',
            attenuation=-30, dmin=50, dmax=1000, priority=None)
        sfx_keyboard_flurry01 = Sound(root=self, name='sfx_keyboard_flurry01', sound='sfx_keyboard_flurry01',
            attenuation=-30, dmin=50, dmax=1000, priority=None)
        sfx_keyboard_flurry02 = Sound(root=self, name='sfx_keyboard_flurry02', sound='sfx_keyboard_flurry02',
            attenuation=-22, dmin=50, dmax=1000, priority=None)
        sfx_keyboard_flurry03 = Sound(root=self, name='sfx_keyboard_flurry03', sound='sfx_keyboard_flurry03',
            attenuation=-15, dmin=50, dmax=1000, priority=None)

        # Начальная расстановка взглядов.
        jacobo.move_head_ik(group=MAIN, target_name=self.get_automarker_name('jacobo_head_ik'), immediately=True)
        jacobo.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('jacobo_eye_ik'), immediately=True)
        # trent.move_head_ik(group=MAIN, target_name=self.get_automarker_name('trent_head_ik'), immediately=True)
        trent.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('trent_eye_ik'), immediately=True)

        # Вход.
        t = 0
        trent.motion(group=MAIN, anim=Male.Sc_MLHAND_NEUT_LEFT_000LV_A_00, duration=5, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLHAND_NEUT_RGHT_000LV_A_00, duration=5, time_delay=t)
        cam_begin.set(group=MAIN, time_delay=t)
        cam_begin.move_cam(group=MAIN, index=2, duration=10, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=notebook.name, anim='Sc_open', duration=3,
            time_scale=0.8, time_delay=t)
        jacobo.start_head_ik(group=MAIN, duration=851, time_delay=t)
        jacobo.start_eye_ik(group=MAIN, duration=851, time_delay=t)
        trent.start_head_ik(group=MAIN, duration=85, time_delay=t)
        trent.move_head_ik(group=MAIN, target_name=self.get_automarker_name('head_bartender'), duration=0.0001,
            time_delay=t)
        jacobo.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_SMALL_000LV_XA_07, duration=1.5, time_delay=t)
        t += 1.5
        jacobo.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=1.7, trans_time=1,
            time_delay=t)
        t += 1.7
        jacobo.motion(group=MAIN, anim=Male.Sc_SPCBODY_s020x_VanPelt_XC_CHRF_TYPE_000DN_06, duration=10,
            trans_time=0.5, loop=True, time_delay=t)
        t += 0.3
        jacobo.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_GESTL_TYPING_000LV_XB, duration=7.474,
            trans_time=0.5, loop=True, time_delay=t)
        jacobo.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_GESTR_TYPING_000LV_XB, duration=7.459,
            trans_time=0.5, loop=True, time_delay=t)
        t += 0.5
        sfx_keyboard_flurry02.start(group=MAIN, duration=9, loop=True, time_delay=t)
        t += 1
        cam_begin.move_focus(group=MAIN, index=2, duration=5, time_delay=t)
        t += 5
        cam_jacobo_eyes.set(group=MAIN, time_delay=t)
        t += 2
        jacobo.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_trent_far'), duration=3,
            time_delay=t)
        jacobo.move_head_ik(group=MAIN, target_name=self.get_automarker_name('head_trent_far'), duration=4,
            time_delay=t)
        jacobo.motion(group=MAIN, anim=Male.Sc_MLHEAD_MAD_COLD_000LV_XA_, duration=10, time_scale=0.8,
            trans_time=0.25, time_delay=t)
        t += 3
        cam_bartender_pointer.set(group=MAIN, time_delay=t)
        cam_bartender_pointer.change_fov(group=MAIN, fov=10, duration=5, smooth=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.GENERIC_ANIM, duration=10, time_scale=0.6, trans_time=0.25,
            time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_HNDS_CASL_000LV_xa_04, duration=2,
            time_scale=0.6, time_delay=t)
        bartender.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_000DN_A_29, duration=6, time_delay=t)
        t += 1
        jacobo.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('notebook_screen'), duration=2,
            time_delay=t)
        jacobo.move_head_ik(group=MAIN, target_name=self.get_automarker_name('notebook_screen'), duration=2,
            time_delay=t)
        t += 1
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_HNDSDN_TRNS_000LV_XA_01, duration=5,
            time_scale=0.6, trans_time=1, time_delay=t)
        bartender.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_POINT_RHND_270LV_A_03, duration=6,
            time_scale=0.6, trans_time=1, time_delay=t)
        t += 1
        trent.move_head_ik(group=MAIN, target_name=self.get_automarker_name('head_jacobo'), duration=4,
            time_delay=18)
        bartender.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_POINT_RGHT_CASL_000LV_00, duration=4,
            time_scale=2, trans_time=0.25, time_delay=t)
        t += 1
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_TURN_045LV_XA_04, duration=4, trans_time=1,
            time_delay=t)
        t += 1
        trent.motion(group=MAIN, anim=Trent.Sc_MLHEAD_HAPPY_SMILE_SNEER_TRENT_000LV_XA_, duration=10,
            trans_time=0.25, time_delay=t)
        t += 1.6
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01, duration=1.4, time_scale=0.7,
            trans_time=1, time_delay=t)
        t += 1.4
        MoveFastEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('point_trent_arriving'), time_delay=t)
        cam_trent_arrival.set(group=MAIN, time_delay=t)
        cam_trent_arrival.move_cam(group=MAIN, index=2, duration=5, time_delay=t)
        cam_trent_arrival.move_focus(group=MAIN, index=2, duration=5, time_delay=t)
        jacobo.motion(group=MAIN, anim=Male.Sc_SPCBODY_s020x_VanPelt_XC_CHRF_TYPE_000DN_06, duration=14,
            loop=True, time_delay=t)
        sfx_keyboard_flurry01.start(group=MAIN, duration=14, loop=True, time_delay=t)
        jacobo.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_GESTL_TYPING_000LV_XB, duration=14, trans_time=0.5,
            loop=True, time_delay=t)
        jacobo.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_GESTR_TYPING_000LV_XB, duration=14, trans_time=0.5,
            loop=True, time_delay=t)
        t += 2
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XC_03, duration=5, time_scale=0.6,
            time_delay=t)
        main_group.append_time(27)

        # 10: trent.
        # Приветствую!
        trent.facial(group=MAIN, index=10, auto_lip=True)

        # 20: jacobo.
        # Симметрично. Чему обязан?
        t = 0.5
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_000DN_A_29, duration=20, time_scale=0.6,
            trans_time=1, loop=True, time_delay=t)
        jacobo.facial(group=MAIN, index=20, auto_lip=True)
        main_group.append_time(1)

        # 30: trent.
        # Вильгельму вы обязаны.
        t = 0
        jacobo.motion(group=MAIN, anim=Male.Sc_MLHAND_NEUT_LEFT_000LV_A_00, duration=5, time_delay=t)
        jacobo.motion(group=MAIN, anim=Male.Sc_MLHAND_NEUT_RGHT_000LV_A_00, duration=5, time_delay=t)
        cam_trent_stand.set(group=MAIN, time_delay=t)
        t += 3
        cam_jacobo_fingerprint.set(group=MAIN, time_delay=t)
        jacobo.motion(group=MAIN, anim=Male.Sc_MLHEAD_MAD_COLD_000LV_XA_, duration=10, trans_time=0.25,
            time_delay=t)
        trent.facial(group=MAIN, index=30, auto_lip=True)
        # Действие после реплики.
        t = 0.5
        jacobo.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('jacobo_front_left'), duration=1,
            time_delay=t)
        main_group.append_time(1)

        # 40: jacobo.
        # Что есть -то есть.
        t = 0
        jacobo.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_IDLE_SMALL_000LV_XA_05, duration=14, trans_time=1,
            loop=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLHAND_NEUT_LEFT_000LV_A_00, duration=5, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLHAND_NEUT_RGHT_000LV_A_00, duration=5, time_delay=t)
        jacobo.move_head_ik(group=MAIN, target_name=self.get_automarker_name('jacobo_front'), duration=1,
            time_delay=t)
        jacobo.facial(group=MAIN, index=40, auto_lip=True)

        # 45: jacobo.
        # И что же на этот раз понадобилось герру Вильгельму?
        t = 0
        jacobo.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_trent'), duration=1.25,
            time_delay=t)
        jacobo.move_head_ik(group=MAIN, target_name=self.get_automarker_name('head_trent_btm'), duration=3,
            time_delay=t)
        jacobo.facial(group=MAIN, index=45, auto_lip=True)

        # 50: trent.
        # Координаты одного разбившегося корабля.
        t = 0
        cam_trent_stand.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=50, auto_lip=True)

        # 60: jacobo.
        # А! Это проще простого. Я сейчас скину вам все точки происшествий с повреждением судов за прошедший
        # месяц. Точность позиционирования плюс-минус двадцать миллиметров. Выбирайте что вам нужно,
        # фильтруйте по критериям, спасибо говорить не нужно.
        t = 0
        cam_jacobo_fingerprint.set(group=MAIN, time_delay=t)
        t += 2
        jacobo.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('notebook_screen'), duration=1.25,
            time_delay=t)
        jacobo.move_head_ik(group=MAIN, target_name=self.get_automarker_name('notebook_screen'), duration=2,
            time_delay=t)
        jacobo.motion(group=MAIN, anim=Male.Sc_SPCBODY_s020x_VanPelt_XC_CHRF_TYPE_000DN_06, duration=6,
            trans_time=1, loop=True, time_delay=t)
        sfx_keyboard_flurry03.start(group=MAIN, duration=6, loop=True, time_delay=t)
        t += 2
        sfx_ui_react_accept01.start(group=MAIN, duration=2, time_delay=t)
        t += 1
        jacobo.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('notebook_screen_left'),
            duration=0.5, time_delay=t)
        t += 0.5
        sfx_ui_react_accept02.start(group=MAIN, duration=2, time_delay=t)
        t += 0.5
        jacobo.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('notebook_screen_right'),
            duration=0.5, time_delay=t)
        sfx_ui_react_accept02.start(group=MAIN, duration=2, time_delay=t)
        t += 0.5
        sfx_ui_react_accept02.start(group=MAIN, duration=2, time_delay=t)
        t += 0.5
        jacobo.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('notebook_screen'), duration=0.5,
            time_delay=t)
        t += 1
        sfx_ui_react_data01.start(group=MAIN, duration=2, time_delay=t)
        t += 1
        jacobo.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_trent'), duration=1.25,
            time_delay=t)
        jacobo.move_head_ik(group=MAIN, target_name=self.get_automarker_name('head_trent_btm'), duration=2,
            time_delay=t)
        t += 1
        jacobo.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDUP_TRNS_000LV_XA_02, duration=2,
            time_scale=0.5, trans_time=1, time_delay=t)
        t += 1
        jacobo.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CONV_RHND_CASL_000LV_XC_01, duration=2,
            time_scale=0.5, trans_time=1, time_delay=t)
        t += 1
        jacobo.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDDN_TRNS_000LV_XA_02, duration=2,
            time_scale=0.5, trans_time=1, time_delay=t)
        t += 1
        jacobo.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('notebook_screen'), duration=1.25,
            time_delay=t)
        jacobo.move_head_ik(group=MAIN, target_name=self.get_automarker_name('notebook_screen'), duration=2,
            time_delay=t)
        t += 1
        jacobo.motion(group=MAIN, anim=Male.Sc_SPCBODY_s020x_VanPelt_XC_CHRF_TYPE_000DN_06, duration=7,
            trans_time=1, loop=True, time_delay=t)
        sfx_keyboard_flurry01.start(group=MAIN, duration=6, loop=True, time_delay=t)
        jacobo.facial(group=MAIN, index=60, auto_lip=True)

        # 70: trent.
        # Мы вместе полетим.
        t = 0
        cam_trent_stand.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_SMALL_000LV_xa_05, duration=5, time_scale=0.6,
            time_delay=t)
        t += 3
        trent.facial(group=MAIN, index=70, auto_lip=True)


        cam_jacobo_fingerprint.set(group=MAIN)

        # 80: jacobo.
        # Это зачем еще?
        t = 0
        jacobo.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_trent_btm'), duration=1.25,
            time_delay=t)
        jacobo.move_head_ik(group=MAIN, target_name=self.get_automarker_name('jacobo_front'), duration=1.5,
            time_delay=t)
        t += 1
        jacobo.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_IDLE_SMALL_000LV_XA_05, duration=5, trans_time=1,
            loop=True, time_delay=t)
        jacobo.facial(group=MAIN, index=80, auto_lip=True)

        # 90: trent.
        # Вильгельм сказал, ты должен мне указать на место интересующего нас события, а я должен его найти. А
        # как я могу быть уверен, что ты не слил мне туфту, чтобы через полчаса свалить в закат? У военных
        # свои причуды, а у фриленсеров - свои.
        t = 0
        trent.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_jacobo'), duration=0.0001,
            time_delay=t)
        cam_trent_stand_far.set(group=MAIN, time_delay=t)
        cam_trent_stand_far.move_cam(group=MAIN, index=2, duration=13, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=2,
            time_delay=t)
        t += 1
        trent.start_eye_ik(group=MAIN, duration=22, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_HOLD_000LV_XA_02, duration=4, trans_time=1,
            loop=True, time_delay=t)
        t += 4
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=2, trans_time=1,
            time_delay=t)
        t += 1.5
        trent.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_GESTR_THUMB_000LV_00, duration=2, time_delay=t)
        t += 1
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_GESTR_180LV_XA_02, duration=5, time_delay=t)
        trent.move_head_ik(group=MAIN, target_name=self.get_automarker_name('head_jacobo_outside_half'),
            duration=1, time_delay=t)
        trent.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_jacobo_outside'), duration=1,
            time_delay=t)
        t += 1
        trent.move_head_ik(group=MAIN, target_name=self.get_automarker_name('head_jacobo'), duration=2,
            time_delay=t)
        trent.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_jacobo'), duration=1,
            time_delay=t)
        t += 0.5
        bartender.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_000DN_A_29, duration=6, trans_time=1,
            time_delay=t)
        t += 1
        trent.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_GESTR_THUMB_000LV_00, duration=5, start_time=2,
            time_delay=t)
        trent.facial(group=MAIN, index=90, auto_lip=True)
        main_group.append_time(0.5)

        # 100: jacobo.
        # Сотню раз уже проклял тот день когда согласился Вильгельму помогать.
        t = 0
        jacobo.move_head_ik(group=MAIN, target_name=self.get_automarker_name('notebook_screen'), duration=2,
            time_delay=t)
        jacobo.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('notebook_screen_left'),
            duration=1, time_delay=t)
        cam_jacobo_fingerprint.set(group=MAIN, time_delay=t)
        jacobo.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=2, time_delay=t)
        t += 1
        MotionEvent(root=self, group=MAIN, object_name=notebook.name, anim='Sc_close', duration=3, time_delay=t)
        t += 1
        jacobo.move_head_ik(group=MAIN, target_name=self.get_automarker_name('head_jacobo_standing'),
            duration=1.5, time_delay=t)
        jacobo.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_jacobo_standing'),
            duration=1, time_delay=t)
        jacobo.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_STNDCR_TRNS_090LV_XA_05, duration=6, time_delay=t)
        t += 2
        trent.start_head_ik(group=MAIN, duration=10, time_delay=t)
        trent.start_eye_ik(group=MAIN, duration=10, time_delay=t)
        trent.move_head_ik(group=MAIN, target_name=self.get_automarker_name('head_jacobo_final_init'),
            duration=0.0001, time_delay=t)
        trent.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_jacobo_final_init'),
            duration=0.0001, time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('point_trent_final'), time_delay=t)
        jacobo.facial(group=MAIN, index=100, auto_lip=True)
        # Действие после реплики.
        t = 0
        trent.move_head_ik(group=MAIN, target_name=self.get_automarker_name('head_jacobo_final_done'),
            duration=3, time_delay=0)
        trent.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_jacobo_final_done'),
            duration=3, time_delay=0)
        jacobo.move_head_ik(group=MAIN, target_name=self.get_automarker_name('head_trent_final_half'),
            duration=0.01, time_delay=0)
        jacobo.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_trent_final'), duration=0.1,
            time_delay=0)
        cam_walkout1.set(group=MAIN, time_delay=t)
        cam_walkout1.move_cam(group=MAIN, index=2, duration=5, time_delay=t)
        cam_walkout1.move_focus(group=MAIN, index=2, duration=5, time_delay=t)
        ConnectHardpointEvent(root=self, group=MAIN, target_name=notebook.name, parent_name=jacobo.name,
            duration=28, target_hardpoint='HpHandConnect', parent_hardpoint='HpLeftConnect', time_delay=t)
        jacobo.motion(group=MAIN, anim=Male.Sc_MLHAND_NEUT_WALK_LEFT_000LV_XA_, duration=1, time_scale=2,
            time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=notebook.name, anim='Sc_close', duration=1,
            time_scale=5, time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name=jacobo.name,
            target_name=self.get_automarker_name('point_jacobo_final'), time_delay=t)
        jacobo.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=3, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_000DN_A_29, duration=1, time_delay=t)
        t += 1
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_TURN_270LV_XA_04, duration=3, trans_time=1,
            time_delay=t)
        main_group.append_time(1.5)

        # 110: jacobo.
        # Сам-то он где сейчас? Сидит в баре на ближайшем торговом посту?
        t = 1
        jacobo.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, duration=3,
            trans_time=1.5, time_delay=t)
        t += 1
        jacobo.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_RHND_CASL_000LV_xa_01, duration=2,
            trans_time=1.5, loop=True, time_delay=t)
        jacobo.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00, duration=4, time_scale=0.75,
            trans_time=0.25, time_delay=t)
        t += 0.5
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_000DN_A_29, duration=4, time_scale=0.6, trans_time=1,
            loop=True, time_delay=t)
        t += 1.5
        jacobo.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_02, duration=3,
            trans_time=1.5, time_delay=t)
        jacobo.facial(group=MAIN, index=110, auto_lip=True)
        # Действие после реплики.
        t = 0
        trent.move_head_ik(group=MAIN, target_name=self.get_automarker_name('trent_final_front'), duration=4,
            time_delay=t)
        trent.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('trent_final_front'), duration=4,
            time_delay=t)
        t += 0.5
        jacobo.move_head_ik(group=MAIN, target_name=self.get_automarker_name('jacobo_final_front'), duration=4,
            time_delay=t)
        jacobo.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('jacobo_final_front'), duration=2,
            time_delay=t)
        jacobo.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XC_02, duration=2, time_scale=1.5,
            time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WALK_TRNS_270LV_XA_02, duration=6, trans_time=1,
            time_delay=t)
        main_group.append_time(2)

        # 120: jacobo.
        # Что бы ни случилось, он тут не при чем окажется, а вот мы с тобой главные фигуранты.
        t = 0
        jacobo.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_GEST_RHND_TLKING_000LV_XB_02, duration=18,
            time_scale=0.8, loop=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=30, time_scale=0.8, loop=True,
            time_delay=t)
        cam_walkout2.set(group=MAIN, time_delay=t)
        cam_walkout2.move_cam(group=MAIN, index=2, duration=5, time_delay=t)
        cam_walkout2.move_focus(group=MAIN, index=2, duration=5, time_delay=t)
        jacobo.facial(group=MAIN, index=120, auto_lip=True)
        main_group.append_time(2.5)
