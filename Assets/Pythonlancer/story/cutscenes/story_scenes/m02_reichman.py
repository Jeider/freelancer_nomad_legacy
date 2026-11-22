"""Завершение задания у Рейхмана: обычный API Pythonlancer, относительная постановка реплик."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import (
    Male, Trent,
)
from story import actors


class MainShip(Ship):
    COMPOUND_TEMPLATE_NAME = 'rh_elite'


class Trooper1(actors.Actor):
    NAME = 'trooper1'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'ms2_trooper1'
    GAME_ACTOR = 'Trooper1'


class Trooper2(actors.Actor):
    NAME = 'trooper2'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'ms2_trooper2'
    GAME_ACTOR = 'Trooper2'


class M02ReichmanScene(Scene):
    DUMP_FILE = 'm02_reichman'
    SCENE_AMBIENT = [32, 32, 32]

    def action(self):
        main_group = self.get_group(MAIN)

        LT = 99

        # Персонажи.
        reichman = Character(root=self, actor=actors.Reichman, light_group=LT,
            init_point='Char_reichman', rotate_from_quat=True, use_ambient=True)
        trent = Character(root=self, actor=actors.Trent, light_group=LT,
            init_point='Char_trent', rotate_from_quat=True, use_ambient=True)
        wilham = Character(root=self, actor=actors.Wilham, light_group=LT,
            init_point='Char_wilham', rotate_from_quat=True, use_ambient=True)
        trooper1 = Character(root=self, actor=Trooper1, light_group=LT,
            init_point='Char_trooper1', rotate_from_quat=True, use_ambient=True)
        trooper2 = Character(root=self, actor=Trooper2, light_group=LT,
            init_point='Char_trooper2', rotate_from_quat=True, use_ambient=True)

        # Камеры: *_focus, *2 / *_focus2 и следующие позиции в Blender.
        cam_start = LookAtCamera(root=self, name='cam_start', fov=40)
        cam_reichman_near = LookAtCamera(root=self, name='cam_reichman_near', fov=15)
        cam_reichman_top = LookAtCamera(root=self, name='cam_reichman_top', fov=17)
        cam_reichman_far = LookAtCamera(root=self, name='cam_reichman_far', fov=23)
        cam_reichman_reward = LookAtCamera(root=self, name='cam_reichman_reward', fov=17)
        cam_trent_near = LookAtCamera(root=self, name='cam_trent_near', fov=15)
        cam_trent_top = LookAtCamera(root=self, name='cam_trent_top', fov=18)
        cam_trent_far = LookAtCamera(root=self, name='cam_trent_far', fov=20)
        cam_trent_away = LookAtCamera(root=self, name='cam_trent_away', fov=15)
        cam_reichman_looktrent = LookAtCamera(root=self, name='cam_reichman_looktrent', fov=20)
        cam_final = LookAtCamera(root=self, name='cam_final', fov=25)

        # Реквизит и звук.
        main_ship = MainShip(root=self, name='main_ship', light_group=3,
            init_point='main_ship', rotate_from_quat=True, loadout='level_rh_elite_loadout04')
        music_main = Sound(root=self, name='music_main', sound='music_discordant_psychosis',
            attenuation=-10, dmin=50, dmax=300, priority='Story_Sound_1')
        music_second = Sound(root=self, name='music_second', sound='music_anticipation_more_forboding',
            attenuation=-10, dmin=50, dmax=300, priority='Story_Sound_1')


        Light(root=self, name='lgt1', point_name='lgt1', light_group=LT, diffuse=[0.65, 0.7, 0.7],
            ambient=[0, 0, 0], direction=[0, 0, -1], light_type=L_POINT, range=25)
        Light(root=self, name='lgt2', point_name='lgt2', light_group=LT, diffuse=[0.85, 0.8, 0.8],
            ambient=[0, 0, 0], direction=[0, 0, -1], light_type=L_POINT, range=25)

        # Начальная расстановка взглядов.
        reichman.move_head_ik(group=MAIN, target_name=self.get_automarker_name('reichman_head_ik'), immediately=True)
        reichman.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('reichman_eye_ik'), immediately=True)
        trent.move_head_ik(group=MAIN, target_name=self.get_automarker_name('trent_head_ik'), immediately=True)
        trent.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('trent_eye_ik'), immediately=True)
        wilham.move_head_ik(group=MAIN, target_name=self.get_automarker_name('wilham_head_ik'), immediately=True)
        wilham.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('wilham_eye_ik'), immediately=True)

        # Вход.
        t = 0
        music_main.start(group=MAIN, duration=47, loop=True, time_delay=t)
        trent.motion(group=MAIN, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, duration=1, time_delay=t)
        cam_start.set(group=MAIN, time_delay=t)
        cam_start.move_cam(group=MAIN, index=2, duration=6, time_delay=t)
        cam_start.move_focus(group=MAIN, index=2, duration=6, time_delay=t)
        trent.start_head_ik(group=MAIN, duration=10, time_delay=t)
        wilham.start_head_ik(group=MAIN, duration=10, time_delay=t)
        reichman.start_eye_ik(group=MAIN, duration=15, transition_duration=0.1, time_delay=t)
        trooper2.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_000LV_E_20, duration=1555, time_scale=0.5,
            loop=True, time_delay=t)
        trooper1.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_000LV_E_20, duration=1555, time_scale=0.5,
            loop=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=3.6, start_time=0.3, loop=True,
            time_delay=t)
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=3.8, start_time=0.1,
            loop=True, time_delay=t)
        reichman.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_HOLD_ARMS_CROSSED_000LV_XA_02, duration=5,
            time_delay=t)
        t += 3
        NeckIkEvent(root=self, group=MAIN, char_name=trooper2.name, target_name=wilham.name,
            target_type=TARGET_PART, target_part='Body_Head', duration=25, transition_duration=3, time_delay=t)
        t += 0.6
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=4, time_delay=t)
        t += 0.2
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=4, time_delay=t)
        t += 0.2
        reichman.motion(group=MAIN, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=2, time_scale=0.2,
            time_delay=t)
        t += 0.5
        reichman.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_reichman_back_left'),
            duration=2, time_delay=t)
        t += 0.5
        reichman.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, duration=5, time_delay=t)
        reichman.move_head_ik(group=MAIN, target_name=self.get_automarker_name('head_trent'), duration=1,
            time_delay=t)
        t += 1
        reichman.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_TURN_180LV_XA_04, duration=5, time_scale=0.75,
            trans_time=0.5, time_delay=t)
        t += 1
        cam_reichman_top.set(group=MAIN, time_delay=t)
        cam_reichman_top.move_cam(group=MAIN, index=2, duration=5, time_delay=t)
        cam_reichman_top.move_focus(group=MAIN, index=2, duration=6, time_delay=t)
        t += 0.5
        reichman.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_reichman_front'),
            duration=1, time_delay=t)
        main_group.append_time(10)

        # 10: reichman.
        # А вот и сам знаменитый Трент.
        t = 0
        reichman.start_head_ik(group=MAIN, duration=5, time_delay=t)
        t += 1
        reichman.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=5, time_scale=0.6,
            trans_time=2, loop=True, time_delay=t)
        t += 2
        cam_trent_far.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=4, trans_time=2,
            time_delay=t)
        reichman.facial(group=MAIN, index=10, auto_lip=True)

        # 20: trent.
        # И чем же я так знаменит, мистер, эмм...
        trent.facial(group=MAIN, index=20, auto_lip=True)
        # Действие после реплики.
        t = 0.2
        trent.motion(group=MAIN, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, duration=5, trans_time=1,
            time_delay=t)
        main_group.append_time(0.7)

        # 30: reichman.
        # Райхманн. Адмирал Райхманн, если позволите.
        t = 0
        cam_reichman_near.set(group=MAIN, time_delay=t)
        reichman.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_BOW_ASNSTYL_RSPCTFLY_000LV_xa_03, duration=3,
            time_delay=t)
        t += 2
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=7, trans_time=2,
            time_delay=t)
        t += 1
        reichman.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=5, time_scale=0.6,
            trans_time=2, time_delay=t)
        reichman.facial(group=MAIN, index=30, auto_lip=True)

        # 40: trent.
        # Моё почтение, адмирал Райхманн! Так чем же я знаменит?
        t = 0
        cam_trent_top.set(group=MAIN, time_delay=t)
        reichman.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_trent'), duration=2,
            time_delay=t)
        reichman.move_head_ik(group=MAIN, target_name=self.get_automarker_name('head_trent'), duration=2,
            time_delay=t)
        trent.facial(group=MAIN, index=40, auto_lip=True)

        # 50: reichman.
        # О, мистер Трент, в последнее время в некоторых кругах только и разговоров, что о вас! Надеюсь, герр
        # Вильгельм достойно оплачивает вашу работу?
        t = 0
        reichman.start_head_ik(group=MAIN, duration=30, time_delay=t)
        reichman.start_eye_ik(group=MAIN, duration=30, time_delay=t)
        cam_reichman_far.move_focus(group=MAIN, index=2, duration=8, time_delay=t)
        cam_reichman_far.set(group=MAIN, time_delay=t)
        t += 2
        cam_reichman_far.move_cam(group=MAIN, index=2, duration=6, time_delay=t)
        t += 2
        reichman.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_wilham'), duration=2,
            time_delay=t)
        reichman.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, duration=3,
            trans_time=1.5, time_delay=t)
        trent.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_reichman'), duration=2,
            time_delay=t)
        trent.move_head_ik(group=MAIN, target_name=self.get_automarker_name('head_reichman'), duration=2,
            time_delay=t)
        t += 1
        reichman.move_head_ik(group=MAIN, target_name=self.get_automarker_name('head_wilham_trent_half'),
            duration=2, time_delay=t)
        reichman.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_RHND_CASL_000LV_xa_01, duration=2,
            trans_time=1.5, loop=True, time_delay=t)
        reichman.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00, duration=4, time_scale=0.75,
            trans_time=0.25, time_delay=t)
        t += 1
        reichman.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_02, duration=3,
            trans_time=1.5, time_delay=t)
        trent.start_head_ik(group=MAIN, duration=10, time_delay=t)
        trent.start_eye_ik(group=MAIN, duration=10, time_delay=t)
        trent.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_wilham'), duration=2,
            time_delay=t)
        trent.move_head_ik(group=MAIN, target_name=self.get_automarker_name('head_reichman_wilham_half'),
            duration=2, time_delay=t)
        t += 2
        cam_trent_near.move_focus(group=MAIN, index=2, duration=4, time_delay=t)
        cam_trent_near.set(group=MAIN, time_delay=t)
        reichman.facial(group=MAIN, index=50, auto_lip=True)
        # Действие после реплики.
        t = 0.1
        trent.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_reichman'), duration=1,
            time_delay=t)
        trent.move_head_ik(group=MAIN, target_name=self.get_automarker_name('head_reichman'), duration=3.5,
            time_delay=t)
        main_group.append_time(0.8)

        # 60: trent.
        # Не жалуюсь.
        t = 0.8
        reichman.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_trent'), duration=1,
            time_delay=t)
        reichman.move_head_ik(group=MAIN, target_name=self.get_automarker_name('head_trent'), duration=1,
            time_delay=t)
        trent.facial(group=MAIN, index=60, auto_lip=True)
        main_group.append_time(1)

        # 70: reichman.
        # Скромность - похвальная благодетель, герр Трент, но одной благодетелью сыт не будешь, ха-ха. Я
        # распоряжусь, чтобы ваш гонорар за предыдущую миссию был удвоен. Всех благ, герр Трент!
        t = 0
        trent.motion(group=MAIN, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, duration=1, trans_time=1,
            time_delay=t)
        cam_reichman_reward.move_cam(group=MAIN, index=2, duration=10, time_delay=t)
        cam_reichman_reward.move_focus(group=MAIN, index=2, duration=10, time_delay=t)
        cam_reichman_reward.set(group=MAIN, time_delay=t)
        reichman.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=1, time_delay=t)
        t += 1
        reichman.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_GESTL_STOP_000LV_XA_03, duration=4.5,
            time_scale=0.6, trans_time=1, time_delay=t)
        t += 4.5
        reichman.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_ATEASE_HSEC_RLEASE_000LV_XA_03, duration=5,
            time_scale=0.6, trans_time=1, time_delay=t)
        t += 0.5
        music_main.change_attenuation(group=MAIN, duration=5, attenuation=-100, time_delay=t)
        t += 2
        reichman.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_ATEASE_HOLD_000LV_XA_01, duration=5,
            time_scale=0.6, trans_time=1, loop=True, time_delay=t)
        t += 3
        music_second.start(group=MAIN, duration=60, loop=True, time_delay=t)
        music_second.change_attenuation(group=MAIN, duration=5, attenuation=0, time_delay=t)
        cam_trent_away.move_cam(group=MAIN, index=2, duration=10, time_delay=t)
        cam_trent_away.move_focus(group=MAIN, index=2, duration=10, time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name=trooper1.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name=trooper2.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('point_trent_talk'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name=wilham.name,
            target_name=self.get_automarker_name('point_wilham_talk'), time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name=reichman.name,
            target_name=self.get_automarker_name('point_reichman_looktrent'), time_delay=t)
        cam_trent_away.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WALK_TRNS_180LV_XA_02, duration=5, time_scale=0.6,
            trans_time=1, time_delay=t)
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_TURN_090LV_XA_02, duration=5, time_scale=0.5,
            time_delay=t)
        t += 0.1
        NeckIkEvent(root=self, group=MAIN, char_name=wilham.name, target_name=trent.name,
            target_type=TARGET_PART, target_part='Body_Head', duration=5, transition_duration=5, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=wilham.name, target_name=trent.name,
            target_type=TARGET_PART, target_part='Body_Head', duration=5, transition_duration=2, time_delay=t)
        t += 3.9
        reichman.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=5, time_scale=0.5,
            start_time=0.35, time_delay=t)
        reichman.facial(group=MAIN, index=70, auto_lip=True)
        # Действие после реплики.
        t = 0.75
        # wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=25, time_scale=0.6,
        #     trans_time=2, loop=True, time_delay=t)
        reichman.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_reichman_trentaway_front'),
            duration=2, time_delay=t)
        reichman.move_head_ik(group=MAIN,
            target_name=self.get_automarker_name('head_reichman_trentaway_front'), duration=2, time_delay=t)
        t += 2
        wilham.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_trent_away'), duration=1,
            time_delay=t)
        wilham.move_head_ik(group=MAIN, target_name=self.get_automarker_name('head_trent_away'), duration=1,
            time_delay=t)
        main_group.append_time(8)

        # 80: reichman.
        # Так вы считаете, что он - тот кто нам нужен?
        t = 0
        wilham.start_head_ik(group=MAIN, duration=35, time_delay=t)
        wilham.start_eye_ik(group=MAIN, duration=35, time_delay=t)
        wilham.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_reichman_trentaway'),
            duration=2, time_delay=t)
        wilham.move_head_ik(group=MAIN, target_name=self.get_automarker_name('wilham_rotate_front_left'),
            duration=3, time_delay=t)
        t += 2
        cam_trent_away.move_cam(group=MAIN, index=3, duration=11, time_delay=t)
        cam_trent_away.move_focus(group=MAIN, index=3, duration=11, time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), time_delay=t)
        reichman.start_head_ik(group=MAIN, duration=35, time_delay=t)
        reichman.start_eye_ik(group=MAIN, duration=35, time_delay=t)
        reichman.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_wilham'), duration=2,
            time_delay=t)
        reichman.move_head_ik(group=MAIN,
            target_name=self.get_automarker_name('head_reichman_trentaway_front_right'), duration=2,
            time_delay=t)
        reichman.facial(group=MAIN, index=80, auto_lip=True)

        # 90: wilham.
        # Безусловно, герр Адмирал. Он - тот, кто поможет нам выполнить все известные вам задачи.
        t = 2
        wilham.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_trent_away'), duration=4,
            time_delay=t)
        wilham.move_head_ik(group=MAIN, target_name=self.get_automarker_name('wilham_rotate_front'),
            duration=4, time_delay=t)
        t += 1
        reichman.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_reichman_trentaway_front'),
            duration=2, time_delay=t)
        reichman.move_head_ik(group=MAIN,
            target_name=self.get_automarker_name('head_reichman_trentaway_front'), duration=2, time_delay=t)
        wilham.facial(group=MAIN, index=90, auto_lip=True)
        main_group.append_time(0.35)

        # 100: reichman.
        # И вы это гарантируете?
        t = 0
        reichman.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_wilham'), duration=1,
            time_delay=t)
        reichman.move_head_ik(group=MAIN,
            target_name=self.get_automarker_name('head_reichman_trentaway_front_right'), duration=1.5,
            time_delay=t)
        wilham.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_reichman_trentaway'),
            duration=3, time_delay=t)
        t += 1
        wilham.move_head_ik(group=MAIN, target_name=self.get_automarker_name('wilham_rotate_front_left'),
            duration=2, time_delay=t)
        reichman.facial(group=MAIN, index=100, auto_lip=True)

        # 110: wilham.
        # Абсолютно!
        t = 1.9
        cam_reichman_looktrent.set(group=MAIN, time_delay=t)
        wilham.facial(group=MAIN, index=110, auto_lip=True)

        # 120: reichman.
        # Хорошо, мы принимаем в работу ваш сценарий.
        t = 2
        reichman.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_reichman_trentaway_front'),
            duration=2, time_delay=t)
        reichman.move_head_ik(group=MAIN,
            target_name=self.get_automarker_name('head_reichman_trentaway_front'), duration=2, time_delay=t)
        t += 2.5
        reichman.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_ATEASE_HSEC_RLEASE_000LV_XA_03, duration=15,
            time_scale=0.6, time_delay=t, trans_time=1)
        reichman.facial(group=MAIN, index=120, auto_lip=True)

        # 130: wilham.
        # Благодарю за оказанное доверие.
        t = 0
        cam_final.set(group=MAIN, time_delay=t)
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_SALUT_000LV_XA_03, duration=15, time_scale=0.8,
            time_delay=t)
        t += 1.5
        reichman.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_wilham'), duration=2,
            time_delay=t)
        reichman.move_head_ik(group=MAIN,
            target_name=self.get_automarker_name('head_reichman_trentaway_front_right'), duration=2,
            time_delay=t)
        t += 0.5
        reichman.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_ATEASE_HOLD_000LV_XA_01, duration=15,
            time_scale=0.6, loop=True, time_delay=t, trans_time=1)
        t += 0.5
        wilham.motion(group=MAIN, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=5, trans_time=0.25,
            time_delay=t)
        cam_final.move_cam(group=MAIN, index=2, duration=10, time_delay=t)
        cam_final.move_focus(group=MAIN, index=2, duration=10, time_delay=t)
        wilham.facial(group=MAIN, index=130, auto_lip=True)

        # 140: reichman.
        # Посмотрим что из этого получится. Не смею задерживать, герр Вильгельм.
        t = 0.5
        reichman.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_reichman_trentaway_front'),
            duration=7, time_delay=t)
        reichman.move_head_ik(group=MAIN,
            target_name=self.get_automarker_name('head_reichman_trentaway_front'), duration=7, time_delay=t)
        t += 2
        wilham.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('outpoint'), duration=3,
            time_delay=t)
        wilham.move_head_ik(group=MAIN, target_name=self.get_automarker_name('outpoint'), duration=3,
            time_delay=t)
        t += 1
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WALK_TRNS_090LV_XA_02, duration=15, time_scale=0.8,
            time_delay=t)
        reichman.facial(group=MAIN, index=140, auto_lip=True)
        # Действие после реплики.
        t = 1.5
        reichman.motion(group=MAIN, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=2, time_scale=0.2,
            time_delay=t)
        t += 1
        music_second.change_attenuation(group=MAIN, duration=3, attenuation=-8, time_delay=t)
        main_group.append_time(5.5)
