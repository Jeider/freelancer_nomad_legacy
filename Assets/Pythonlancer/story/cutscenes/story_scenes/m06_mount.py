"""m06_mount: полная постановка из master; точки в m06_mount.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character, LookAtCamera, MAIN, Male, NeckIkEvent, RotateAxisEvent,
)
from story.cutscenes.anim import (
    Male,
)
from story import actors



class M06MountScene(Scene):
    DUMP_FILE = 'm06_mount'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)
        self.set_duration(40.0)

        # Персонажи, камеры, реквизит и звук.
        trent = Character(root=self, actor=actors.Trent, name='Char_trent', light_group=0,
            init_point='Char_trent', rotate_from_quat=True, appearance='trent', actor_name='Player')
        alaric = Character(root=self, actor=actors.Alaric, name='Char_alaric', light_group=0,
            init_point='Char_alaric', rotate_from_quat=True, use_ambient=True, appearance='alaric',
            actor_name='Alaric')
        cam_start = LookAtCamera(root=self, name='cam_start', fov=20, look_duration=30)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=20, look_duration=1)
        cam_alaric = LookAtCamera(root=self, name='cam_alaric', fov=20, look_duration=1)
        cam_final = LookAtCamera(root=self, name='cam_final', fov=26, look_duration=111)

        # Исходные точки взгляда.

        # Абсолютное время исходной сцены; часы MAIN не сдвигаются.
        t = 0
        cam_start.set(group=MAIN, time_delay=t)
        cam_start.move_cam(group=MAIN, index=2, duration=8, smooth=True, time_delay=t)
        cam_start.move_focus(group=MAIN, index=2, duration=8, smooth=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=6, time_scale=0.75,
            start_time=0.73, loop=True, time_delay=t)
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=8.5, time_scale=0.75, loop=True,
            time_delay=t)
        t += 2
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=25, transition_duration=2, time_delay=t)
        t += 4
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=4, time_scale=0.75,
            trans_time=0.1, time_delay=t)
        t += 2
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=-10, axis='Y_AXIS', duration=1,
            smooth=True, time_delay=t)
        t += 0.5
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_TURN_270LV_XA_04, duration=5, time_delay=t)
        t += 0.5
        NeckIkEvent(root=self, group=MAIN, char_name=alaric.name, target_name=trent.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=25, transition_duration=2,
            time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=alaric.name, angle=35, axis='Y_AXIS', duration=1,
            smooth=True, time_delay=t)
        t += 1.5
        cam_alaric.set(group=MAIN, time_delay=t)
        t += 2.5
        cam_trent.set(group=MAIN, time_delay=t)
        t += 3
        cam_alaric.set(group=MAIN, time_delay=t)
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_GESTR_THMBSUP_000LV_XA_02, duration=6, time_scale=0.6,
            time_delay=t)
        t += 2.5
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_GEST_HNDS_WAIT_000LV_XA_02, duration=6, time_scale=0.8,
            trans_time=0.5, time_delay=t)
        t += 2.8
        cam_trent.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=6,
            time_scale=0.6, time_delay=t)
        t += 4.2
        cam_alaric.set(group=MAIN, time_delay=t)
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_HOLD_HEAD_RLEASE_000LV_XA_01, duration=6,
            time_scale=0.8, start_time=0.4, time_delay=t)
        t += 2
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=6,
            time_scale=0.8, time_delay=t)
        t += 4
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=6, time_scale=0.8,
            time_delay=t)
        t += 1.7
        alaric.motion(group=MAIN, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=2, trans_time=1.5,
            time_delay=t)
        t += 0.8
        cam_final.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=6, time_scale=0.8,
            time_delay=t)
        cam_final.move_cam(group=MAIN, index=2, duration=6, smooth=True, time_delay=t)
        t += 1
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WALK_TRNS_180LV_XA_02, duration=5, time_scale=0.8,
            trans_time=1, time_delay=t)
        t += 1
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WALK_TRNS_270LV_XA_02, duration=5, time_scale=0.8,
            trans_time=1, time_delay=t)

        # m06_mount 10: У тебя редкий талант постоянно влипать в неприятности, Аларик.
        self.add_group('voice_16', time=2)
        trent.facial(group='voice_16', index=10, auto_lip=True, extra_delay=0, append=False)

        # m06_mount 20: Ты о чем? 
        self.add_group('voice_18', time=6)
        alaric.facial(group='voice_18', index=20, auto_lip=True, extra_delay=0, append=False)

        # m06_mount 30: О том что с нами будет происходить в ближайшем будущем.
        self.add_group('voice_20', time=7)
        trent.facial(group='voice_20', index=30, auto_lip=True, extra_delay=0, append=False)

        # m06_mount 40: Ты про нашу миссию?
        self.add_group('voice_23', time=10.5)
        alaric.facial(group='voice_23', index=40, auto_lip=True, extra_delay=0, append=False)

        # m06_mount 50: Про нашу СУИЦИДАЛЬНУЮ миссию.
        self.add_group('voice_26', time=13)
        trent.facial(group='voice_26', index=50, auto_lip=True, extra_delay=0, append=False)

        # m06_mount 60: Зато какие выгоды в случае успеха! К тому же ты мог бы отказаться.
        self.add_group('voice_29', time=16)
        alaric.facial(group='voice_29', index=60, auto_lip=True, extra_delay=0, append=False)

        # m06_mount 70: Боюсь, если бы я отказался, то уже летал бы в космосе без скафандра.
        self.add_group('voice_34', time=21.3)
        trent.facial(group='voice_34', index=70, auto_lip=True, extra_delay=0, append=False)

        # m06_mount 80: Трент, раз уж мы подписались, надо выполнять. Давай, Трент, полетели. Обещаю, в следующий раз заказчика будешь выбирать ты.
        self.add_group('voice_38', time=25.5)
        alaric.facial(group='voice_38', index=80, auto_lip=True, extra_delay=0, append=False)

        # m06_mount 90: Если он будет, этот следующий раз. 
        self.add_group('voice_46', time=34)
        trent.facial(group='voice_46', index=90, auto_lip=True, extra_delay=0, append=False)
