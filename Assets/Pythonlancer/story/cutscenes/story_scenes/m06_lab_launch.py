"""m06_lab_launch: постановка для ручного редактирования.

Точки: SCENES/m06_lab_launch.blend → DUMPS/m06_lab_launch.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — абсолютные секунды исходной сцены; часы MAIN не сдвигаются.
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
    PlayerShip,
    Prop,
    RotateAxisEvent,
    Ship,
    Sound,
    StaticCamera,
)
from story.cutscenes.anim import (
    Male,
)
from story.cutscenes.source_extensions import (
    SourceAlchemyAnimEvent,
    SourceAttachEvent,
    SourcePathEvent,
    SourceSpatialEvent,
    preserve_entity,
)
from story import actors


class PropPropCrystal(Prop):
    COMPOUND_TEMPLATE_NAME = 'prop_artifact_crystal'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropTome(Prop):
    COMPOUND_TEMPLATE_NAME = 'tome'
    SRT_GRP = 0
    USR_FLG = 0


class PropTheCart2(Prop):
    COMPOUND_TEMPLATE_NAME = 'rh_cart'
    SRT_GRP = 0
    USR_FLG = 0


class PropTheCart3(Prop):
    COMPOUND_TEMPLATE_NAME = 'rh_cart'
    SRT_GRP = 0
    USR_FLG = 0


class PropTheCart4(Prop):
    COMPOUND_TEMPLATE_NAME = 'rh_cart'
    SRT_GRP = 0
    USR_FLG = 0


class PropCrateb1(Prop):
    COMPOUND_TEMPLATE_NAME = 'm06_crate1'
    SRT_GRP = 0
    USR_FLG = 0


class PropCrateb2(Prop):
    COMPOUND_TEMPLATE_NAME = 'm06_crate1'
    SRT_GRP = 0
    USR_FLG = 0


class PropCratec1(Prop):
    COMPOUND_TEMPLATE_NAME = 'm06_crate1'
    SRT_GRP = 0
    USR_FLG = 0


class PropCratec2(Prop):
    COMPOUND_TEMPLATE_NAME = 'm06_crate1'
    SRT_GRP = 0
    USR_FLG = 0


class PropCratea1(Prop):
    COMPOUND_TEMPLATE_NAME = 'm06_crate1'
    SRT_GRP = 0
    USR_FLG = 0


class PropCratea2(Prop):
    COMPOUND_TEMPLATE_NAME = 'm06_crate1'
    SRT_GRP = 0
    USR_FLG = 0


class PropAlaricShip(Ship):
    COMPOUND_TEMPLATE_NAME = 'li_elite'
    SRT_GRP = 0
    USR_FLG = 0


class PropPlayership(Ship):
    COMPOUND_TEMPLATE_NAME = 'PlayerShip'
    SRT_GRP = 0
    USR_FLG = 0



class M06LabLaunchScene(Scene):
    DUMP_FILE = 'm06_lab_launch'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(14.0)
        prop_crystal = PropPropCrystal(root=self, name='prop_crystal', light_group=9, init_point='prop_crystal',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(prop_crystal, userprops={'category': 'Prop'})
        prop_tome = PropPropTome(root=self, name='prop_tome', light_group=9, init_point='prop_tome', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(prop_tome, userprops={'category': 'Prop'})
        the_cart2 = PropTheCart2(root=self, name='the_cart2', light_group=3, init_point='the_cart2', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(the_cart2, userprops={'category': 'Equipment Cart', 'Priority': 'Equip_2'})
        the_cart3 = PropTheCart3(root=self, name='the_cart3', light_group=3, init_point='the_cart3', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(the_cart3, userprops={'category': 'Equipment Cart', 'Priority': 'Equip_2'})
        the_cart4 = PropTheCart4(root=self, name='the_cart4', light_group=3, init_point='the_cart4', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(the_cart4, userprops={'category': 'Equipment Cart', 'Priority': 'Equip_2'})
        crateB1 = PropCrateb1(root=self, name='crateB1', light_group=3, init_point='crateB1', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(crateB1, userprops={'category': 'Prop'})
        crateB2 = PropCrateb2(root=self, name='crateB2', light_group=3, init_point='crateB2', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(crateB2, userprops={'category': 'Prop'})
        crateC1 = PropCratec1(root=self, name='crateC1', light_group=3, init_point='crateC1', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(crateC1, userprops={'category': 'Prop'})
        crateC2 = PropCratec2(root=self, name='crateC2', light_group=3, init_point='crateC2', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(crateC2, userprops={'category': 'Prop'})
        crateA1 = PropCratea1(root=self, name='crateA1', light_group=3, init_point='crateA1', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(crateA1, userprops={'category': 'Prop'})
        crateA2 = PropCratea2(root=self, name='crateA2', light_group=3, init_point='crateA2', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(crateA2, userprops={'category': 'Prop'})
        Camera_X = StaticCamera(root=self, name='Camera_X', fov=35, farplane=100000)
        preserve_entity(Camera_X, cameraprops={'hvaspect': 1.333333, 'nearplane': 0.1})
        alaric_ship = PropAlaricShip(root=self, name='alaric_ship', light_group=3, init_point='alaric_ship',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(alaric_ship, userprops={'category': 'Spaceship', 'loadout': 'lod_ms6_alaric_cloak'})
        PlayerShip = PropPlayership(root=self, name='PlayerShip', light_group=3, init_point='PlayerShip',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(PlayerShip, userprops={'category': 'Spaceship'})
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=True, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'actor': 'trent', 'category': 'Character'},
            ambient=[128, 128, 128])
        Path_CameraLaunch = MotionPath(root=self, name='Path_CameraLaunch', point_name='Path_CameraLaunch',
            path_data='{-20,4,0}, {1,0,0,0}, {-45,12,4}, {1,0,0,0}')
        preserve_entity(Path_CameraLaunch)
        Path_PlayerShipStart = MotionPath(root=self, name='Path_PlayerShipStart', point_name='Path_PlayerShipStart',
            path_data='{0,0,0}, {0.25,0,0.75,0}, {0,0.001,0}, {0.25,0,0.75,0}')
        preserve_entity(Path_PlayerShipStart)
        Path_PlayerShip = MotionPath(root=self, name='Path_PlayerShip', point_name='Path_PlayerShip',
            path_data='{0,0,0}, {1,0,0,0}, {1,4,0}, {1,0,0,0}')
        preserve_entity(Path_PlayerShip)
        Path_PlayerShipFlyOut = MotionPath(root=self, name='Path_PlayerShipFlyOut', point_name='Path_PlayerShipFlyOut',
            path_data='{1,4,0}, {0.25,0,-0.5,0}, {50,4,0}, {0.5,0,-0.5,0}')
        preserve_entity(Path_PlayerShipFlyOut)
        Path_AlaricShip = MotionPath(root=self, name='Path_AlaricShip', point_name='Path_AlaricShip',
            path_data='{-15,3,-5}, {0.25,0,-0.5,0}, {-14,9,0}, {0.5,0,0.5,0}')
        preserve_entity(Path_AlaricShip)
        Path_AlaricShipOrient = MotionPath(root=self, name='Path_AlaricShipOrient', point_name='Path_AlaricShipOrient',
            path_data='{-15,3,-5}, {0.25,0,-0.5,0}, {-1,9,0}, {0.5,0,0.5,0}')
        preserve_entity(Path_AlaricShipOrient)
        Path_AlaricShipFlyAway = MotionPath(root=self, name='Path_AlaricShipFlyAway', point_name='Path_AlaricShipFlyAway',
            path_data='{-14,9,0}, {0.5,0,0.5,0}, {-50,9,0}, {0.25,0,-0.5,0}')
        preserve_entity(Path_AlaricShipFlyAway)
        Camera_Running = LookAtCamera(root=self, name='Camera_Running', fov=35, farplane=100000, look_duration=300)
        preserve_entity(Camera_Running, cameraprops={'hvaspect': 1.333333, 'nearplane': 0.1})
        Path_CameraRunning = MotionPath(root=self, name='Path_CameraRunning', point_name='Path_CameraRunning',
            path_data='{-1, 3, 35}, {1,0,0,0}, {0, 4, 20}, {1,0,0,0}')
        preserve_entity(Path_CameraRunning)
        Path_MrkCameraRunning = MotionPath(root=self, name='Path_MrkCameraRunning', point_name='Path_MrkCameraRunning',
            path_data='{0, 0, 30}, {1,0,0,0}, {0, 5, 10}, {1,0,0,0}')
        preserve_entity(Path_MrkCameraRunning)
        Camera_Launch = LookAtCamera(root=self, name='Camera_Launch', fov=35, farplane=100000, look_duration=300)
        preserve_entity(Camera_Launch, cameraprops={'hvaspect': 1.333333, 'nearplane': 0.1})
        Path_MrkCameraLaunch = MotionPath(root=self, name='Path_MrkCameraLaunch', point_name='Path_MrkCameraLaunch',
            path_data='{0, 2, 0}, {1,0,0,0}, {0, 5, 0}, {1,0,0,0}')
        preserve_entity(Path_MrkCameraLaunch)
        PlayerShipEngines_2 = Alchemy(root=self, name='PlayerShipEngines_2', particles='PlayerShipEngines',
            point_name='PlayerShipEngines_2', sparam=0)
        preserve_entity(PlayerShipEngines_2, flags='LIT_DYNAMIC+LIT_AMBIENT')
        music_main = Sound(root=self, name='music_main', sound='music_upcoming_action_heavy', attenuation=0, dmin=50,
            dmax=300, priority='Story_Sound_1')
        preserve_entity(music_main, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        start_sound = Sound(root=self, name='start_sound', sound='engine_playership_launch_turbine', attenuation=0, dmin=50,
            dmax=300, priority='Story_Sound_1')
        preserve_entity(start_sound, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        launch_sound = Sound(root=self, name='launch_sound', sound='engine_playership_launch', attenuation=0, dmin=50,
            dmax=300, priority='Story_Sound_1')
        preserve_entity(launch_sound, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})

        # Действия по абсолютному времени сцены.
        t = 0
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='prop_crystal', parent_name='Char_trent',
            duration=50000, target_hardpoint='HpLefthandConnect_prop_crystal', parent_hardpoint='hpleftconnect')
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='prop_tome', parent_name='Char_trent',
            duration=10000, target_hardpoint='rhand_connect_tome', parent_hardpoint='hprightconnect')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['Camera_X', 'Mrk_CameraInit'], duration=300,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['PlayerShip', 'Path_PlayerShipStart'], duration=0.001,
            start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS',
            flags='POSITION+ORIENTATION', param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]},
            pcurve_period=-1000)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_RNNG_000LV_XA_01, duration=15)
        Camera_Running.set(group=MAIN, time_delay=t)
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['Camera_Running', 'Path_CameraRunning'], duration=5,
            start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', flags='POSITION',
            param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]}, pcurve_period=-1000)
        SourcePathEvent(root=self, group=MAIN, time_delay=t,
            targets=['automarker_Camera_Running_focus', 'Path_MrkCameraRunning'], duration=5, start_percent=0,
            stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', flags='POSITION',
            param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]}, pcurve_period=-1000)
        music_main.start(group=MAIN, time_delay=t, duration=500)
        t += 0.6
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_RNNG_000LV_XA_01, duration=15)
        t += 0.6
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_RNNG_000LV_XA_01, duration=15)
        t += 0.6
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_RNNG_000LV_XA_01, duration=15)
        t += 0.6
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_RNNG_000LV_XA_01, duration=15)
        t += 0.6
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_RNNG_000LV_XA_01, duration=15)
        t += 0.6
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_RNNG_000LV_XA_01, duration=15)
        t += 0.6
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_RNNG_000LV_XA_01, duration=15)
        t += 0.6
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_RNNG_000LV_XA_01, duration=15)
        t += 0.2
        SourceSpatialEvent(root=self, group=MAIN, time_delay=t, targets=['Char_trent', 'automarker_Mrk_OffScreen'],
            duration=0.001, target_part='', target_type='ROOT',
            spatialprops={'pos': [25000, 0, 0], 'q_orient': [1, 0, 0, 0]})
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['alaric_ship', 'Path_AlaricShipOrient'], duration=8,
            start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', flags='ORIENTATION',
            param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]}, pcurve_period=-1000)
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['alaric_ship', 'Path_AlaricShip'], duration=5,
            start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', flags='POSITION',
            param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]}, pcurve_period=-1000)
        Camera_Launch.set(group=MAIN, time_delay=t)
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['Camera_Launch', 'Path_CameraLaunch'], duration=10,
            start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', flags='POSITION',
            param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]}, pcurve_period=-1000)
        SourcePathEvent(root=self, group=MAIN, time_delay=t,
            targets=['automarker_Camera_Launch_focus', 'Path_MrkCameraLaunch'], duration=10, start_percent=0,
            stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', flags='POSITION',
            param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]}, pcurve_period=-1000)
        SourceAlchemyAnimEvent(root=self, group=MAIN, time_delay=t, targets=['PlayerShipEngines_2'], duration=0.1,
            psysprops={'sparam': 0.5})
        PlayerShipEngines_2.start(group=MAIN, time_delay=t, duration=20)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['PlayerShipEngines_2', 'PlayerShip'], duration=30,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpEngine01', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION')
        start_sound.start(group=MAIN, time_delay=t, duration=500)
        t += 5
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='PlayerShip', angle=135, axis='Y_AXIS', duration=7,
            smooth=False)
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['PlayerShip', 'Path_PlayerShip'], duration=3,
            start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', flags='POSITION',
            param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]}, pcurve_period=-1000)
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['alaric_ship', 'Path_AlaricShipFlyAway'], duration=5,
            start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', flags='POSITION',
            param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]}, pcurve_period=-1000)
        t += 1
        launch_sound.start(group=MAIN, time_delay=t, duration=500)
        t += 2
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['PlayerShip', 'Path_PlayerShipFlyOut'], duration=5,
            start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', flags='POSITION',
            param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]}, pcurve_period=-1000)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M06LabLaunchScene
