"""m04_hatcher: полная постановка из master; точки в m04_hatcher.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    AttachEvent, Character, EyeIkEvent, Female, Light, LookAtCamera, MAIN, Male, MoveEvent, NeckIkEvent, RotateAxisEvent,
)
from story.cutscenes.anim import (
    Female, Male, Trent,
)
from story import actors



class M04HatcherScene(Scene):
    DUMP_FILE = 'm04_hatcher'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Персонажи, камеры, реквизит и звук.
        ambi_ltg00_bar_ovrhd01a = Light(root=self, name='ambi_LtG00_Bar_Ovrhd01A',
            point_name='ambi_LtG00_Bar_Ovrhd01A', extra_name='', light_group=5, hidden=False,
            rotate_from_quat=True, diffuse=[0.596078, 0.572549, 0.403922], ambient=[0.223529, 0.2, 0.192157],
            direction=[0, 0, 1], light_type='L_POINT', range=15, cutoff=18, theta=15, color=[233, 208, 150],
            attenuation=[0.8999999762, 0, 0.0060000001], on=True)
        ambi_ltg00_bar_ovrhd01b = Light(root=self, name='ambi_LtG00_Bar_Ovrhd01B',
            point_name='ambi_LtG00_Bar_Ovrhd01B', extra_name='', light_group=5, hidden=False,
            rotate_from_quat=True, diffuse=[0.596078, 0.572549, 0.403922], ambient=[0, 0, 0], direction=[0, 0, 1],
            light_type='L_POINT', range=5, cutoff=18, theta=15, color=[233, 208, 150],
            attenuation=[0.8999999762, 0, 0.0060000001], on=True)
        bartender_fixture = Character(root=self, actor=actors.BartenderFixture, name='Char_bartender_Fixture',
            light_group=0, init_point='Char_bartender_Fixture', rotate_from_quat=True,
            appearance='li_bartender_1', actor_name='bartender')
        hatcher = Character(root=self, actor=actors.Hatcher, name='Char_hatcher', light_group=5,
            init_point='Char_hatcher', rotate_from_quat=True, appearance='hatcher', actor_name='Hatcher')
        trent = Character(root=self, actor=actors.Trent, name='Char_trent', light_group=0,
            init_point='Char_trent', rotate_from_quat=True, appearance='trent', actor_name='Player')
        alaric = Character(root=self, actor=actors.Alaric, name='Char_alaric', light_group=0,
            init_point='Char_alaric', rotate_from_quat=True, appearance='alaric', actor_name='Alaric')
        cam_start = LookAtCamera(root=self, name='cam_start', fov=25, look_duration=300)
        cam_hatcher_firstlook = LookAtCamera(root=self, name='cam_hatcher_firstlook', fov=15, look_duration=300)
        cam_hatcher_people_arrive = LookAtCamera(root=self, name='cam_hatcher_people_arrive', fov=15,
            look_duration=300)
        cam_hatcher_near = LookAtCamera(root=self, name='cam_hatcher_near', fov=15, look_duration=300)
        cam_trent_near = LookAtCamera(root=self, name='cam_trent_near', fov=15, look_duration=300)
        cam_alaric = LookAtCamera(root=self, name='cam_alaric', fov=20, look_duration=300)
        cam_alaric_near = LookAtCamera(root=self, name='cam_alaric_near', fov=15, look_duration=300)
        cam_hatcher_final = LookAtCamera(root=self, name='cam_hatcher_final', fov=20, look_duration=300)

        # Исходные точки взгляда.

        # Вход.
        t = 0
        cam_start.set(group=MAIN, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name='wlkg_trent_front', parent_name=trent.name, duration=35,
            target_part='Body_Head', target_type='PART', adjust_pos=True, adjust_orient=False, up='Y_AXIS',
            front='NEG_Z_AXIS', time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=self.get_automarker_name('wlkg_alaric'),
            parent_name=alaric.name, duration=200, target_part='Body_Head', target_type='PART', adjust_pos=True,
            adjust_orient=False, up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=self.get_automarker_name('wlkg_alaric_front_near'),
            parent_name=alaric.name, duration=200, target_part='Body_Head', target_type='PART', adjust_pos=True,
            adjust_orient=False, up='Y_AXIS', front='NEG_Z_AXIS', offset_x=0.75, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLHAND_NEUT_LEFT_000LV_A_00, duration=5, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLHAND_NEUT_RGHT_000LV_A_00, duration=5, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=6.91, time_scale=0.75, loop=True,
            time_delay=t)
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=6.91, time_scale=0.75,
            start_time=0.2, loop=True, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STLB_000LV_A_21, duration=16, time_scale=0.75,
            start_time=2, time_delay=t)
        cam_start.move_cam(group=MAIN, index=2, duration=15, smooth=True, time_delay=t)
        cam_start.move_focus(group=MAIN, index=2, duration=15, smooth=True, time_delay=t)
        t += 6.91
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=3, time_scale=0.75,
            time_delay=t)
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=3, time_scale=0.75,
            start_time=0.22, trans_time=0.2, time_delay=t)
        t += 1.09
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=10, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=10, transition_duration=1, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=alaric.name,
            target_name=self.get_automarker_name('alaric_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=10, transition_duration=1, time_delay=t)
        t += 1.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('wlkg_alaric_front_near'), duration=2, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_POINT_RHND_000LV_A_03, duration=5, time_scale=0.75,
            trans_time=0.5, time_delay=t)
        trent.motion(group=MAIN, anim='Sc_dx_s075x_0401_trent', duration=6, start_time=1, trans_time=0.25,
            time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('alaric_head_ik'),
            target_name=self.get_automarker_name('marker_hatcher_sitpoint'), duration=2, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=5,
            time_scale=0.8, trans_time=1, time_delay=t)
        t += 3
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_trent_front_exitpoint'), duration=2, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 1
        cam_hatcher_firstlook.move_cam(group=MAIN, index=2, duration=7, smooth=True, time_delay=t)
        cam_hatcher_firstlook.set(group=MAIN, time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('alaric_head_ik'),
            target_name=self.get_automarker_name('head_alaric_front_exitpoint'), duration=2, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 1
        EyeIkEvent(root=self, group=MAIN, char_name=hatcher.name,
            target_name=self.get_automarker_name('hatcher_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=5, transition_duration=1, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STLB_LSTN_270LV_C_07, duration=6, trans_time=1,
            time_delay=t)
        t += 1
        NeckIkEvent(root=self, group=MAIN, char_name=hatcher.name,
            target_name=self.get_automarker_name('hatcher_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=4, transition_duration=1, time_delay=t)
        t += 5
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STLB_STDSL_TRNS_225LV_A_03, duration=3, time_delay=t)
        cam_hatcher_people_arrive.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('point_trent_wayforward'), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=alaric.name,
            target_name=self.get_automarker_name('point_alaric_wayforward'), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STLB_STDSL_TRNS_225LV_A_03, duration=3, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=3.25, time_scale=0.75, loop=True,
            time_delay=t)
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=3.25, time_scale=0.75, loop=True,
            time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_hatcher'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_hatcher'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('alaric_head_ik'),
            target_name=self.get_automarker_name('head_hatcher'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('alaric_eye_ik'),
            target_name=self.get_automarker_name('head_hatcher'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_hatcher_front'), duration=0.1, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_hatcher_front'), duration=0.1, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_trent_near'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=hatcher.name,
            target_name=self.get_automarker_name('hatcher_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=90, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=hatcher.name,
            target_name=self.get_automarker_name('hatcher_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=90, transition_duration=1, time_delay=t)
        t += 0.5
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=67.5, transition_duration=1, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=alaric.name,
            target_name=self.get_automarker_name('alaric_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=67.5, transition_duration=1, time_delay=t)
        main_group.append_time(25)

        # m04_reward 10: Hatcher.
        # Мисс Хетчер.
        t = 0.25
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_TURN_180LV_XA_04, duration=1, start_time=0.75,
            trans_time=1, time_delay=t)
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_TURN_270LV_XA_04, duration=1.25, start_time=0.75,
            trans_time=1, time_delay=t)
        t += 1
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=30, time_scale=0.7,
            trans_time=2, time_delay=t)
        t += 0.25
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=10, time_scale=0.7,
            start_time=2, trans_time=2, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=60, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=alaric.name,
            target_name=self.get_automarker_name('alaric_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=60, transition_duration=1, time_delay=t)
        cam_alaric.move_focus(group=MAIN, index=2, duration=4, smooth=True, time_delay=t)
        cam_alaric.set(group=MAIN, time_delay=t)
        hatcher.facial(group=MAIN, index=10, auto_lip=True, extra_delay=0)

        # m04_reward 20: Trent.
        # Мисс Хетчер.
        t = 1.1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_alaric_near'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        trent.facial(group=MAIN, index=20, auto_lip=True, extra_delay=0)

        # m04_reward 30: Alaric.
        # Мисс Хетчер, у вас такие красивые бездонные глаза, что...
        t = 2
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_hatcher_front'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_hatcher_front'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_hatcher'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_hatcher'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        alaric.facial(group=MAIN, index=30, auto_lip=True, extra_delay=0)

        # m04_reward 40: Hatcher.
        # Что вы перестанете нести эту околесицу, иначе я рассержусь
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_alaric_near'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_TALK_000LV_B_10, duration=17, time_scale=0.5,
            loop=True, time_delay=t)
        cam_hatcher_people_arrive.set(group=MAIN, time_delay=t)
        t += 3.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_trent_near'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        hatcher.facial(group=MAIN, index=40, auto_lip=True, extra_delay=0)

        # m04_reward 45: Hatcher.
        # . О деле. Все выполнено на лучшем уровне.
        hatcher.facial(group=MAIN, index=45, auto_lip=True, extra_delay=0)

        # m04_reward 50: Hatcher.
        # Я даже не буду спрашивать чего стоило вам сбежать из Рейнланда с ТАКИМИ документами
        t = 1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_alaric_near'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        hatcher.facial(group=MAIN, index=50, auto_lip=True, extra_delay=0)

        # m04_reward 55: Hatcher.
        # Я девушка впечатлительная, боюсь в обморок упасть.
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_hatcher_front'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 1.8
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        hatcher.facial(group=MAIN, index=55, auto_lip=True, extra_delay=0)
        # Действие после исходного окна реплики.
        t = 0.1
        hatcher.motion(group=MAIN, anim=Female.Sc_FMHEAD_BASEPOSE_000LV_02_01, duration=6, trans_time=1,
            time_delay=t)
        t += 1.3
        cam_trent_near.set(group=MAIN, time_delay=t)
        main_group.append_time(1.5)

        # m04_reward 60: Trent.
        # Мы старались.
        t = 1.9
        cam_hatcher_people_arrive.move_cam(group=MAIN, index=2, duration=14.5, smooth=True, time_delay=t)
        cam_hatcher_people_arrive.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=60, auto_lip=True, extra_delay=0)

        # m04_reward 70: Hatcher.
        # Хе, вы тоже были в этом заинтересованы. А кстати, нам как раз нужны такие умелые и предприимчивые
        # люди как вы, для выполнения, скажем так, нестандартных заданий. Вы в ближайшее время не слишком
        # заняты?
        t = 1.5
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=5,
            time_scale=0.5, trans_time=1, time_delay=t)
        t += 7
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=5,
            time_scale=0.5, trans_time=1, time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_alaric_near'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 3
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_hatcher_front'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_hatcher_front'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        hatcher.facial(group=MAIN, index=70, auto_lip=True, extra_delay=0)
        main_group.append_time(1.4)

        # m04_reward 80: Alaric.
        # Заткнись, Аларик. Нет, с тех пор как мы стали врагами Рейнландского государства, работы у нас
        # поубавилось.
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_alaric_near'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_alaric'), duration=0.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        cam_alaric_near.set(group=MAIN, time_delay=t)
        alaric.facial(group=MAIN, index=80, auto_lip=True, extra_delay=0)

        # m04_reward 90: Trent.
        # Заткнись, Аларик. Нет, с тех пор как мы стали врагами Рейнландского государства, работы у нас
        # поубавилось.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_hatcher'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_hatcher'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 5.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_hatcher_front'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        trent.facial(group=MAIN, index=90, auto_lip=True, extra_delay=0)

        # m04_reward 100: Hatcher.
        # То есть если у нас найдется пара заданий по вашему профилю за достойную плату...
        t = 0
        cam_hatcher_near.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_CROSS_ARMS_000LV_xa_03, duration=5, time_scale=0.8,
            trans_time=1, time_delay=t)
        hatcher.facial(group=MAIN, index=100, auto_lip=True, extra_delay=0)

        # m04_reward 110: Trent.
        # То мы не против их выполнить, если конечно же эти задания не приведут к тому что мы станем
        # государственными преступниками и в Либерти.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=110, auto_lip=True, extra_delay=0)

        # m04_reward 120: Hatcher.
        # О, нет, я думаю до этого не дойдет.
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_trent_near'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        cam_hatcher_near.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_UNCRSS_ARMS_000LV_XA_03, duration=5, time_scale=0.8,
            time_delay=t)
        t += 2.5
        cam_trent_near.set(group=MAIN, time_delay=t)
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WALK_TRNS_270LV_XA_02, duration=4, trans_time=2,
            time_delay=t)
        hatcher.facial(group=MAIN, index=120, auto_lip=True, extra_delay=0)

        # m04_reward 130: Trent.
        # Я вот тоже думал...
        trent.facial(group=MAIN, index=130, auto_lip=True, extra_delay=0)
        # Действие после исходного окна реплики.
        t = 0
        trent.motion(group=MAIN, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, duration=6, trans_time=0.25,
            time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WALK_TRNS_270LV_XA_02, duration=2, trans_time=2,
            time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_hatcher_front'), duration=0.1, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_hatcher_front'), duration=0.1, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 1
        cam_hatcher_final.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('marker_bar_exitpoint'), duration=5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('marker_bar_exitpoint'), duration=3, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.001
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=alaric.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.499
        RotateAxisEvent(root=self, group=MAIN, object_name=hatcher.name, angle=-45, axis='Y_AXIS', duration=2,
            smooth=True, time_delay=t)
        t += 1.5
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_CROSS_ARMS_000LV_xa_03, duration=5, time_scale=0.8,
            trans_time=1, time_delay=t)
        main_group.append_time(7)
