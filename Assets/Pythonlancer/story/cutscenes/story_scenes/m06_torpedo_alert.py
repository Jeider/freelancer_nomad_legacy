"""m06_torpedo_alert: полная постановка из master; точки в m06_torpedo_alert.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character, Female, LookAtCamera, MAIN, Male, MotionEvent, NeckIkEvent, RotateAxisEvent, Sound,
)
from story.cutscenes.anim import (
    Female, Male,
)
from story import actors


class CharLiTrooper01Actor(actors.Actor):
    NAME = 'li_trooper01'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_dread_military_1'

class CharLiTrooper02Actor(actors.Actor):
    NAME = 'li_trooper02'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_dread_military_2'

class CharAssistActor(actors.Actor):
    NAME = 'assist'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_dread_military_2'


class M06TorpedoAlertScene(Scene):
    DUMP_FILE = 'm06_torpedo_alert'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Персонажи, камеры, реквизит и звук.
        alarm = Sound(root=self, name='alarm', sound='rtc_klaxon_loop_3', attenuation=-10, dmin=50, dmax=250,
            priority=None)
        trent = Character(root=self, actor=actors.Trent, name='Char_trent', light_group=0,
            init_point='Char_trent', rotate_from_quat=True, appearance='trent', actor_name='Player')
        hatcher = Character(root=self, actor=actors.Hatcher, name='Char_hatcher', light_group=0,
            init_point='Char_hatcher', rotate_from_quat=True, appearance='hatcher', actor_name='Hatcher')
        li_trooper01 = Character(root=self, actor=CharLiTrooper01Actor, name='Char_li_trooper01', light_group=0,
            init_point='Char_li_trooper01', rotate_from_quat=True, use_ambient=True,
            appearance='m06_dread_military_1', actor_name='li_troop01')
        li_trooper02 = Character(root=self, actor=CharLiTrooper02Actor, name='Char_li_trooper02', light_group=0,
            init_point='Char_li_trooper02', rotate_from_quat=True, use_ambient=True,
            appearance='m06_dread_military_2', actor_name='li_troop02')
        assist = Character(root=self, actor=CharAssistActor, name='Char_assist', light_group=0,
            init_point='Char_assist', rotate_from_quat=True, use_ambient=True, appearance='m06_dread_military_2',
            actor_name='li_troop03')
        cam_start = LookAtCamera(root=self, name='cam_start', fov=20, look_duration=30)
        cam_hatcher = LookAtCamera(root=self, name='cam_hatcher', fov=22, look_duration=300)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=20, look_duration=1)
        cam_final = LookAtCamera(root=self, name='cam_final', fov=22, look_duration=111)

        # Исходные точки взгляда.

        # Вход.
        t = 0
        cam_start.set(group=MAIN, time_delay=t)
        t += 1
        alarm.start(group=MAIN, duration=40, loop=True, start_time=0, time_delay=t)
        t += 1
        cam_start.move_cam(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        cam_start.move_focus(group=MAIN, index=2, duration=8, smooth=True, time_delay=t)
        t += 2
        alarm.change_attenuation(group=MAIN, duration=2, attenuation=-20, time_delay=t)
        t += 2
        MotionEvent(root=self, group=MAIN, object_name=li_trooper01.name, anim=Male.Sc_MLBODY_RNNG_000LV_XA_01,
            duration=25, time_scale=0.6, loop=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=li_trooper02.name, anim=Male.Sc_MLBODY_RNNG_000LV_XA_01,
            duration=25, time_scale=0.6, start_time=0.4, loop=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=7, start_time=0.73, loop=True,
            time_delay=t)
        t += 4
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=29.5, transition_duration=1, time_delay=t)
        t += 2
        hatcher.motion(group=MAIN, anim=Female.Sc_dx_s070x_2501_Jacobi, duration=10, time_scale=0.8, start_time=1,
            trans_time=0.25, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_CONV_HNDS_EMPH_000LV_XA_04, duration=3, loop=True,
            time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=assist.name,
            anim=Male.Sc_MLBODY_STND_FSTHIPB_HOLD_000LV_XA_02, duration=3, loop=True, time_delay=t)
        alarm.change_attenuation(group=MAIN, duration=2, attenuation=-40, time_delay=t)
        t += 1
        cam_hatcher.set(group=MAIN, time_delay=t)
        cam_hatcher.move_cam(group=MAIN, index=2, duration=11, smooth=True, time_delay=t)
        cam_hatcher.move_focus(group=MAIN, index=2, duration=11, smooth=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=4, trans_time=0.1,
            time_delay=t)
        t += 2
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_ATEASE_HSEC_RLEASE_000LV_XA_03, duration=3,
            trans_time=1, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_EMPH_HNDSDN_TRNS_000LV_XA_01, duration=5,
            trans_time=0.5, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=assist.name, anim=Male.Sc_MLBODY_STND_SALUT_000LV_XA_03,
            duration=5, time_scale=1.25, trans_time=0.8, time_delay=t)
        t += 1
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_POINTR_OVRTHRE_000LV_XA_02, duration=5,
            trans_time=0.5, time_delay=t)
        t += 1
        MotionEvent(root=self, group=MAIN, object_name=assist.name,
            anim=Male.Sc_MLBODY_STND_WALK_TRNS_270LV_XA_02, duration=2, trans_time=1, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=assist.name, angle=15, axis='Y_AXIS', duration=2,
            smooth=True, time_delay=t)
        t += 1
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_TURN_270LV_XA_03, duration=5, trans_time=1,
            time_delay=t)
        t += 1
        MotionEvent(root=self, group=MAIN, object_name=assist.name, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01,
            duration=1, loop=True, time_delay=t)
        main_group.append_time(20)

        # m06_torpedo_alert 10: Hatcher.
        # Трент, у нас критическая ситуация! Рейнландцы выпустили против Миссури торпедные канонерки.
        t = 0
        MotionEvent(root=self, group=MAIN, object_name=assist.name, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01,
            duration=15, time_scale=2, start_time=1, loop=True, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=hatcher.name,
            target_name=self.get_automarker_name('hatcher_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=35, transition_duration=1, time_delay=t)
        alarm.change_attenuation(group=MAIN, duration=10, attenuation=-100, time_delay=t)
        t += 1
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05, duration=3, trans_time=1,
            loop=True, time_delay=t)
        t += 3
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_CONV_HNDSUP_TRNS_000LV_XA_01, duration=5,
            trans_time=0.5, time_delay=t)
        t += 1
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_CONV_HNDS_CASL_000LV_xa_03, duration=4,
            trans_time=1, loop=True, time_delay=t)
        hatcher.facial(group=MAIN, index=10, auto_lip=True)

        # m06_torpedo_alert 20: Hatcher.
        # Мы не успеваем запустить гипердвигатель, а системы ПВО линкора не смогут перехватить все выпущенные
        # торпеды.
        t = 3.5
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_CONV_HNDSDN_TRNS_000LV_XA_01, duration=5,
            trans_time=0.5, time_delay=t)
        t += 1.9
        hatcher.facial(group=MAIN, index=20, auto_lip=True)

        # m06_torpedo_alert 40: Trent.
        # Но сначала нужно выгрузить артефакты.
        t = 0
        cam_trent.set(group=MAIN, time_delay=0)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_ATEASE_RLEASE_000LV_XA_01, duration=5, time_scale=0.6,
            trans_time=1, time_delay=t)
        trent.facial(group=MAIN, index=40, auto_lip=True)

        # m06_torpedo_alert 50: Hatcher.
        # В данной ситуации они большей безопасности у вас на борту, а не на Миссури. Вылетайте! Быстрее!
        t = 0
        cam_final.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_CONV_HNDSUP_TRNS_000LV_XA_01, duration=5,
            trans_time=0.5, time_delay=t)
        t += 1
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_CONV_HNDS_CASL_000LV_xa_03, duration=3.5,
            trans_time=1, loop=True, time_delay=t)
        t += 3.5
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_CONV_HNDSDN_TRNS_000LV_XA_01, duration=0.5,
            trans_time=0.5, time_delay=t)
        hatcher.facial(group=MAIN, index=50, auto_lip=True)

        main_group.append_time(1.5)
