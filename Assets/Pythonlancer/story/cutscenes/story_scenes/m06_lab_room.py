"""m06_lab_room: полная постановка из master; точки в m06_lab_room.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Alchemy, Character, ConnectHardpointEvent, LookAtCamera, LookAtEvent, MAIN, Male, MotionEvent, MotionPath, MoveEvent, NeckIkEvent, PathAnimationEvent, Prop, Sound, SoundEvent, StaticCamera,
)
from story.cutscenes.anim import (
    Male, Trent,
)
from story import actors


class PropCaseProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'artifact_case'

class PropCrystalProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'prop_artifact_crystal'

class PropTomeProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'tome'


class M06LabRoomScene(Scene):
    DUMP_FILE = 'm06_lab_room'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Персонажи, камеры, реквизит и звук.
        camera_x = LookAtCamera(root=self, name='Camera_X', fov=30, farplane=100000, nearplane=0.1,
            aspect=1.333333, look_duration=300)
        camera_case = StaticCamera(root=self, name='Camera_Case', fov=30, farplane=100000, nearplane=0.1,
            aspect=1.333333)
        prop_case = PropCaseProp(root=self, name='prop_case', light_group=9, init_point='prop_case',
            rotate_from_quat=True)
        prop_crystal = PropCrystalProp(root=self, name='prop_crystal', light_group=9, init_point='prop_crystal',
            rotate_from_quat=True)
        prop_tome = PropTomeProp(root=self, name='prop_tome', light_group=9, init_point='prop_tome',
            rotate_from_quat=True)
        fx_gas = Alchemy(root=self, name='fx_gas', particles='rtc_artifactcasegas', point_name='fx_gas', sparam=0,
            light_group=0, sort_group=0, hidden=False, use_ambient=True)
        fx_light = Alchemy(root=self, name='fx_light', particles='rtc_artifactlight', point_name='fx_light',
            sparam=0, light_group=0, sort_group=0, hidden=False, use_ambient=True)
        trent = Character(root=self, actor=actors.Trent, name='Char_Trent', light_group=0,
            init_point='Char_Trent', rotate_from_quat=True, appearance='trent', actor_name='trent')
        path_camerainit = MotionPath(root=self, name='Path_CameraInit', point_name='Path_CameraInit',
            path_data='{3, 2, -3}, {1,0,0,0}, {-1.5, 2, -1.5}, {1,0,0,0}, {-2, 2, 1}, {1,0,0,0}')
        path_mrk_camerainit = MotionPath(root=self, name='Path_Mrk_CameraInit', point_name='Path_Mrk_CameraInit',
            path_data='{0, 1, 0}, {1,0,0,0}, {0, 1, -1}, {1,0,0,0}')
        camera_tome = LookAtCamera(root=self, name='Camera_Tome', fov=35, farplane=100000, nearplane=0.1,
            aspect=1.333333, look_duration=300)
        camera_opencase = StaticCamera(root=self, name='Camera_OpenCase', fov=30, farplane=100000, nearplane=0.1,
            aspect=1.333333)
        path_cameraopencase = MotionPath(root=self, name='Path_CameraOpenCase', point_name='Path_CameraOpenCase',
            path_data='{0.4, 1.5, -1.2}, {1,0,0,0}, {-0.3, 1.5, -1.5}, {1,0,0,0}')
        camera_getcrystal = LookAtCamera(root=self, name='Camera_GetCrystal', fov=25, farplane=100000,
            nearplane=0.1, aspect=1.333333, look_duration=300)
        path_cameragetcrystal = MotionPath(root=self, name='Path_CameraGetCrystal',
            point_name='Path_CameraGetCrystal', path_data='{0, 1.3, 0}, {1,0,0,0}, {0.3, 1.66, -0.5}, {1,0,0,0}')
        path_mrkgetcrystal = MotionPath(root=self, name='Path_MrkGetCrystal', point_name='Path_MrkGetCrystal',
            path_data='{-0.2, 1.4, -0.8}, {1,0,0,0}, {-0.3, 1.6, -1.3}, {1,0,0,0}')
        camera_last = StaticCamera(root=self, name='Camera_Last', fov=35, farplane=100000, nearplane=0.1,
            aspect=1.333333)
        music_main = Sound(root=self, name='music_main', sound='music_anticipation_more_forboding', attenuation=0,
            dmin=50, dmax=300, priority='Story_Sound_1')
        pick_tome_sound = Sound(root=self, name='pick_tome_sound', sound='sfx_pick_up_bottle03', attenuation=-20,
            dmin=50, dmax=300, priority='Story_Sound_1')
        weld1_sound = Sound(root=self, name='weld1_sound', sound='sfx_weld1', attenuation=-10, dmin=50, dmax=300,
            priority='Story_Sound_1')
        weld2_sound = Sound(root=self, name='weld2_sound', sound='sfx_weld2', attenuation=-10, dmin=50, dmax=300,
            priority='Story_Sound_1')
        weld3_sound = Sound(root=self, name='weld3_sound', sound='sfx_weld3', attenuation=-10, dmin=50, dmax=300,
            priority='Story_Sound_1')
        weld4_sound = Sound(root=self, name='weld4_sound', sound='sfx_weld4', attenuation=-10, dmin=50, dmax=300,
            priority='Story_Sound_1')
        weld5_sound = Sound(root=self, name='weld5_sound', sound='sfx_weld5', attenuation=-10, dmin=50, dmax=300,
            priority='Story_Sound_1')
        laser_sound = Sound(root=self, name='laser_sound', sound='rtc_laser_impact', attenuation=-5, dmin=50,
            dmax=300, priority='Story_Sound_1')
        step1 = Sound(root=self, name='step1', sound='fs_ml_stone04', attenuation=-15, dmin=50, dmax=300,
            priority=None)
        step2 = Sound(root=self, name='step2', sound='fs_mr_stone04', attenuation=-15, dmin=50, dmax=300,
            priority=None)
        step3 = Sound(root=self, name='step3', sound='fs_ml_stone03', attenuation=-15, dmin=50, dmax=300,
            priority=None)

        # Исходные точки взгляда.

        # Вход.
        t = 0
        ConnectHardpointEvent(root=self, group=MAIN, target_name=prop_crystal.name, parent_name=prop_case.name,
            duration=10, target_hardpoint='Hp_Rest_crystal', parent_hardpoint='Hp_Connect_crystal', time_delay=t)
        camera_x.set(group=MAIN, time_delay=t)
        LookAtEvent(root=self, group=MAIN, point=camera_opencase.name, focus=prop_crystal.name, duration=300,
            target_type='ROOT', target_part='', up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        PathAnimationEvent(root=self, group=MAIN, target_name=camera_x.name, path=path_camerainit, duration=10,
            adjust_pos=True, adjust_orient=False, start_percent=0, stop_percent=1, smooth=True, time_delay=t)
        PathAnimationEvent(root=self, group=MAIN, target_name=self.get_automarker_name('Camera_X_focus'),
            path=path_mrk_camerainit, duration=10, adjust_pos=True, adjust_orient=False, start_percent=0,
            stop_percent=1, smooth=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('Mrk_TrentTome'), duration=0.001, smooth=False, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        music_main.start(group=MAIN, duration=500, loop=False, start_time=0, time_delay=t)
        t += 6
        trent.motion(group=MAIN, anim=Male.Sc_SPCBODY_s051x_Trent_XA_STND_000DN_07, duration=15, time_scale=0.6,
            start_time=1, time_delay=t)
        t += 3
        camera_tome.set(group=MAIN, time_delay=t)
        t += 0.5
        trent.motion(group=MAIN, anim=Trent.Sc_MLHEAD_HAPPY_CHUCKLE_TRENT_000LV_XA_, duration=15, time_delay=t)
        t += 1
        ConnectHardpointEvent(root=self, group=MAIN, target_name=prop_tome.name, parent_name=trent.name,
            duration=10000, target_hardpoint='rhand_connect_tome', parent_hardpoint='hprightconnect', time_delay=t)
        pick_tome_sound.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 2.5
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name, target_name=prop_crystal.name,
            target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', duration=5,
            transition_duration=2, time_delay=t)
        trent.motion(group=MAIN, anim=Trent.Sc_MLHEAD_SURPRSE_IMPRESSED_TRENT_000LV_XA_, duration=15, time_delay=t)
        t += 3
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('Mrk_TrentAway'), duration=0.001, smooth=False, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        camera_opencase.set(group=MAIN, time_delay=t)
        PathAnimationEvent(root=self, group=MAIN, target_name=camera_opencase.name, path=path_cameraopencase,
            duration=15, adjust_pos=True, adjust_orient=False, start_percent=0, stop_percent=1, smooth=True,
            time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=prop_case.name, anim='Sc_open case', duration=15,
            trans_scale=1, time_delay=t)
        t += 0.5
        fx_light.start(group=MAIN, duration=36000, time_delay=t)
        laser_sound.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 2
        weld2_sound.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 1.7
        weld3_sound.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.3
        weld3_sound.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.3
        weld3_sound.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.3
        weld3_sound.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 1.1
        weld5_sound.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 3.8
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('Mrk_TrentCrystal'), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('Mrk_TrentCrystal_LookAt'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=6, transition_duration=1, time_delay=t)
        t += 1
        camera_getcrystal.set(group=MAIN, time_delay=t)
        PathAnimationEvent(root=self, group=MAIN, target_name=camera_getcrystal.name, path=path_cameragetcrystal,
            duration=5, adjust_pos=True, adjust_orient=False, start_percent=0, stop_percent=1, smooth=True,
            time_delay=t)
        PathAnimationEvent(root=self, group=MAIN, target_name=self.get_automarker_name('Camera_GetCrystal_focus'),
            path=path_mrkgetcrystal, duration=5, adjust_pos=True, adjust_orient=False, start_percent=0,
            stop_percent=1, smooth=True, time_delay=t)
        t += 0.001
        trent.motion(group=MAIN, anim=Male.Sc_SPCBODY_s012x_Quintaine_XA_STND_GRABL_ARTFCT_000DN_08, duration=15,
            time_delay=t)
        t += 0.499
        trent.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_HOLD_ARTFCT_LHAND_000LV_XA_01, duration=15,
            time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('Mrk_TrentCrystal_LookAt'),
            target_name=self.get_automarker_name('Mrk_TrentCrystal_LookAt_pos2'), duration=2.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.4
        weld1_sound.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.1
        ConnectHardpointEvent(root=self, group=MAIN, target_name=prop_crystal.name, parent_name=trent.name,
            duration=50000, target_hardpoint='HpLefthandConnect_prop_crystal', parent_hardpoint='hpleftconnect',
            time_delay=t)
        main_group.append_time(29)

        # m06_lab_room 10: Trent.
        # Обалдеть…
        trent.facial(group=MAIN, index=10, auto_lip=True, extra_delay=0)

        # m06_lab_room 20: Alaric.
        # Трент, бежим! Потом рассмотришь.
        t = 1
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_TURN_LEFT_BAR_180LV_XA_02, duration=15, trans_time=1,
            time_delay=t)
        t += 2
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('Camera_GetCrystal_focus'),
            target_name=self.get_automarker_name('Mrk_ExitPoint'), duration=10, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 0.5
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=15, loop=True, time_delay=t)
        line_sound = self.lookup_single_sound(20)
        SoundEvent(root=self, group=MAIN, sound_name=line_sound.get_nickname())
        main_group.append_time(5)
