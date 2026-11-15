"""m06_lab_room: постановка для ручного редактирования.

Точки: SCENES/m06_lab_room.blend → DUMPS/m06_lab_room.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — смещение внутри текущего блока; facial()/append_time() двигают часы.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Alchemy,
    Character,
    ConnectHardpointEvent,
    LookAtCamera,
    MAIN,
    MotionPath,
    MoveEvent,
    NeckIkEvent,
    Prop,
    Sound,
    SoundEvent,
    StaticCamera,
)
from story.cutscenes.anim import (
    Male,
    Trent,
)
from story.cutscenes.source_extensions import (
    SourceAttachEvent,
    SourceMotionEvent,
    SourcePathEvent,
    preserve_entity,
)
from story import actors


class PropPropCase(Prop):
    COMPOUND_TEMPLATE_NAME = 'artifact_case'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropCrystal(Prop):
    COMPOUND_TEMPLATE_NAME = 'prop_artifact_crystal'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropTome(Prop):
    COMPOUND_TEMPLATE_NAME = 'tome'
    SRT_GRP = 0
    USR_FLG = 0



class M06LabRoomScene(Scene):
    DUMP_FILE = 'm06_lab_room'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        Camera_X = LookAtCamera(root=self, name='Camera_X', fov=30, farplane=100000, look_duration=300)
        preserve_entity(Camera_X, cameraprops={'hvaspect': 1.333333, 'nearplane': 0.1})
        Camera_Case = StaticCamera(root=self, name='Camera_Case', fov=30, farplane=100000)
        preserve_entity(Camera_Case, cameraprops={'hvaspect': 1.333333, 'nearplane': 0.1})
        prop_case = PropPropCase(root=self, name='prop_case', light_group=9, init_point='prop_case', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(prop_case, userprops={'category': 'Prop'})
        prop_crystal = PropPropCrystal(root=self, name='prop_crystal', light_group=9, init_point='prop_crystal',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(prop_crystal, userprops={'category': 'Prop'})
        prop_tome = PropPropTome(root=self, name='prop_tome', light_group=9, init_point='prop_tome', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(prop_tome, userprops={'category': 'Prop'})
        fx_gas = Alchemy(root=self, name='fx_gas', particles='rtc_artifactcasegas', point_name='fx_gas', sparam=0)
        preserve_entity(fx_gas, flags='LIT_DYNAMIC+LIT_AMBIENT')
        fx_light = Alchemy(root=self, name='fx_light', particles='rtc_artifactlight', point_name='fx_light', sparam=0)
        preserve_entity(fx_light, flags='LIT_DYNAMIC+LIT_AMBIENT')
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'actor': 'trent', 'category': 'Character'})
        Path_CameraInit = MotionPath(root=self, name='Path_CameraInit', point_name='Path_CameraInit',
            path_data='{3, 2, -3}, {1,0,0,0}, {-1.5, 2, -1.5}, {1,0,0,0}, {-2, 2, 1}, {1,0,0,0}')
        preserve_entity(Path_CameraInit)
        Path_Mrk_CameraInit = MotionPath(root=self, name='Path_Mrk_CameraInit', point_name='Path_Mrk_CameraInit',
            path_data='{0, 1, 0}, {1,0,0,0}, {0, 1, -1}, {1,0,0,0}')
        preserve_entity(Path_Mrk_CameraInit)
        Camera_Tome = LookAtCamera(root=self, name='Camera_Tome', fov=35, farplane=100000, look_duration=300)
        preserve_entity(Camera_Tome, cameraprops={'hvaspect': 1.333333, 'nearplane': 0.1})
        Camera_OpenCase = StaticCamera(root=self, name='Camera_OpenCase', fov=30, farplane=100000)
        preserve_entity(Camera_OpenCase, cameraprops={'hvaspect': 1.333333, 'nearplane': 0.1})
        Path_CameraOpenCase = MotionPath(root=self, name='Path_CameraOpenCase', point_name='Path_CameraOpenCase',
            path_data='{0.4, 1.5, -1.2}, {1,0,0,0}, {-0.3, 1.5, -1.5}, {1,0,0,0}')
        preserve_entity(Path_CameraOpenCase)
        Camera_GetCrystal = LookAtCamera(root=self, name='Camera_GetCrystal', fov=25, farplane=100000, look_duration=300)
        preserve_entity(Camera_GetCrystal, cameraprops={'hvaspect': 1.333333, 'nearplane': 0.1})
        Path_CameraGetCrystal = MotionPath(root=self, name='Path_CameraGetCrystal', point_name='Path_CameraGetCrystal',
            path_data='{0, 1.3, 0}, {1,0,0,0}, {0.3, 1.66, -0.5}, {1,0,0,0}')
        preserve_entity(Path_CameraGetCrystal)
        Path_MrkGetCrystal = MotionPath(root=self, name='Path_MrkGetCrystal', point_name='Path_MrkGetCrystal',
            path_data='{-0.2, 1.4, -0.8}, {1,0,0,0}, {-0.3, 1.6, -1.3}, {1,0,0,0}')
        preserve_entity(Path_MrkGetCrystal)
        Camera_Last = StaticCamera(root=self, name='Camera_Last', fov=35, farplane=100000)
        preserve_entity(Camera_Last, cameraprops={'hvaspect': 1.333333, 'nearplane': 0.1})
        music_main = Sound(root=self, name='music_main', sound='music_anticipation_more_forboding', attenuation=0, dmin=50,
            dmax=300, priority='Story_Sound_1')
        preserve_entity(music_main, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        pick_tome_sound = Sound(root=self, name='pick_tome_sound', sound='sfx_pick_up_bottle03', attenuation=-20, dmin=50,
            dmax=300, priority='Story_Sound_1')
        preserve_entity(pick_tome_sound, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        weld1_sound = Sound(root=self, name='weld1_sound', sound='sfx_weld1', attenuation=-10, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(weld1_sound, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        weld2_sound = Sound(root=self, name='weld2_sound', sound='sfx_weld2', attenuation=-10, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(weld2_sound, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        weld3_sound = Sound(root=self, name='weld3_sound', sound='sfx_weld3', attenuation=-10, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(weld3_sound, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        weld4_sound = Sound(root=self, name='weld4_sound', sound='sfx_weld4', attenuation=-10, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(weld4_sound, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        weld5_sound = Sound(root=self, name='weld5_sound', sound='sfx_weld5', attenuation=-10, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(weld5_sound, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        laser_sound = Sound(root=self, name='laser_sound', sound='rtc_laser_impact', attenuation=-5, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(laser_sound, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        step1 = Sound(root=self, name='step1', sound='fs_ml_stone04', attenuation=-15, dmin=50, dmax=300, priority=None)
        preserve_entity(step1, userprops={'category': 'Audio'})
        step2 = Sound(root=self, name='step2', sound='fs_mr_stone04', attenuation=-15, dmin=50, dmax=300, priority=None)
        preserve_entity(step2, userprops={'category': 'Audio'})
        step3 = Sound(root=self, name='step3', sound='fs_ml_stone03', attenuation=-15, dmin=50, dmax=300, priority=None)
        preserve_entity(step3, userprops={'category': 'Audio'})

        # Вход / начальная постановка.
        t = 0
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='prop_crystal', parent_name='prop_case',
            duration=10, target_hardpoint='Hp_Rest_crystal', parent_hardpoint='Hp_Connect_crystal')
        Camera_X.set(group=MAIN, time_delay=t)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['Camera_OpenCase', 'prop_crystal'], duration=300,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['Camera_X', 'Path_CameraInit'], duration=10,
            start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', flags='POSITION',
            param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]}, pcurve_period=-1000)
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['automarker_Camera_X_focus', 'Path_Mrk_CameraInit'],
            duration=10, start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS',
            flags='POSITION', param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]},
            pcurve_period=-1000)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', target_name='automarker_Mrk_TrentTome',
            duration=0.001, smooth=False)
        music_main.start(group=MAIN, time_delay=t, duration=500)
        t += 6
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_SPCBODY_s051x_Trent_XA_STND_000DN_07, duration=15,
            time_scale=0.6, start_time=1)
        t += 3
        Camera_Tome.set(group=MAIN, time_delay=t)
        t += 0.5
        trent.motion(group=MAIN, time_delay=t, anim=Trent.Sc_MLHEAD_HAPPY_CHUCKLE_TRENT_000LV_XA_, duration=15)
        t += 1.0
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='prop_tome', parent_name='Char_trent',
            duration=10000, target_hardpoint='rhand_connect_tome', parent_hardpoint='hprightconnect')
        pick_tome_sound.start(group=MAIN, time_delay=t, duration=5)
        t += 2.5
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='prop_crystal', duration=5,
            transition_duration=2, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        trent.motion(group=MAIN, time_delay=t, anim=Trent.Sc_MLHEAD_SURPRSE_IMPRESSED_TRENT_000LV_XA_, duration=15)
        t += 3
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', target_name='automarker_Mrk_TrentAway',
            duration=0.001, smooth=False)
        Camera_OpenCase.set(group=MAIN, time_delay=t)
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['Camera_OpenCase', 'Path_CameraOpenCase'],
            duration=15, start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS',
            flags='POSITION', param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]},
            pcurve_period=-1000)
        SourceMotionEvent(root=self, group=MAIN, time_delay=t, targets=['prop_case'], animation='Sc_open case', duration=15,
            start_time=0, time_scale=1, weight=1, trans_scale=1)
        t += 0.5
        fx_light.start(group=MAIN, time_delay=t, duration=36000)
        laser_sound.start(group=MAIN, time_delay=t, duration=5)
        t += 2.0
        weld2_sound.start(group=MAIN, time_delay=t, duration=5)
        t += 1.7
        weld3_sound.start(group=MAIN, time_delay=t, duration=5)
        t += 0.3
        weld3_sound.start(group=MAIN, time_delay=t, duration=5)
        t += 0.3
        weld3_sound.start(group=MAIN, time_delay=t, duration=5)
        t += 0.3
        weld3_sound.start(group=MAIN, time_delay=t, duration=5)
        t += 1.1
        weld5_sound.start(group=MAIN, time_delay=t, duration=5)
        t += 3.8
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', target_name='automarker_Mrk_TrentCrystal',
            duration=0.001, smooth=False)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent',
            target_name='automarker_Mrk_TrentCrystal_LookAt', duration=6, transition_duration=1, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 1
        Camera_GetCrystal.set(group=MAIN, time_delay=t)
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['Camera_GetCrystal', 'Path_CameraGetCrystal'],
            duration=5, start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS',
            flags='POSITION', param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]},
            pcurve_period=-1000)
        SourcePathEvent(root=self, group=MAIN, time_delay=t,
            targets=['automarker_Camera_GetCrystal_focus', 'Path_MrkGetCrystal'], duration=5, start_percent=0,
            stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', flags='POSITION',
            param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]}, pcurve_period=-1000)
        t += 0.001
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_SPCBODY_s012x_Quintaine_XA_STND_GRABL_ARTFCT_000DN_08,
            duration=15)
        t += 0.499
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_HOLD_ARTFCT_LHAND_000LV_XA_01, duration=15)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_Mrk_TrentCrystal_LookAt',
            target_name='automarker_Mrk_TrentCrystal_LookAt_pos2', duration=2.5, smooth=True)
        t += 0.4
        weld1_sound.start(group=MAIN, time_delay=t, duration=5)
        t += 0.1
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='prop_crystal', parent_name='Char_trent',
            duration=50000, target_hardpoint='HpLefthandConnect_prop_crystal', parent_hardpoint='hpleftconnect')
        main_group.append_time(29)


        # Реплика 10 · trent · исходное время 29 с
        # Обалдеть...
        # Исходное окно facial: 15 с.
        t = 0
        trent.facial(group=MAIN, index=10, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-13)


        # Реплика 20 · alaric · исходное время 31 с
        # Трент, бежим! Потом рассмотришь.
        # Исходное окно facial: 0 с.
        t = 0
        voice_sound = self.lookup_single_sound(20)
        SoundEvent(root=self, group=MAIN, sound_name=voice_sound.get_nickname())
        t = 0
        t += 1
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_TURN_LEFT_BAR_180LV_XA_02, duration=15, trans_time=1)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_Camera_GetCrystal_focus',
            target_name='automarker_Mrk_ExitPoint', duration=10, smooth=True)
        t += 0.5
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=15, loop=True)
        main_group.append_time(5.0)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M06LabRoomScene
