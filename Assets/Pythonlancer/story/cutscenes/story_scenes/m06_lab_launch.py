"""m06_lab_launch: полная постановка из master; точки в m06_lab_launch.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Alchemy, AttachEvent, Character, ConnectHardpointEvent, LookAtCamera, LookAtEvent, MAIN, Male, MotionPath, MoveEvent, PathAnimationEvent, Prop, RotateAxisEvent, Ship, Sound, StaticCamera,
)
from story.cutscenes.anim import (
    Male,
)
from story import actors


class PropCrystalProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'prop_artifact_crystal'

class PropTomeProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'tome'

class TheCart2Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'rh_cart'

class TheCart3Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'rh_cart'

class TheCart4Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'rh_cart'

class Crateb1Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm06_crate1'

class Crateb2Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm06_crate1'

class Cratec1Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm06_crate1'

class Cratec2Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm06_crate1'

class Cratea1Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm06_crate1'

class Cratea2Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm06_crate1'

class AlaricShipProp(Ship):
    COMPOUND_TEMPLATE_NAME = 'li_elite'

class PlayershipProp(Ship):
    COMPOUND_TEMPLATE_NAME = 'PlayerShip'


class M06LabLaunchScene(Scene):
    DUMP_FILE = 'm06_lab_launch'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)
        self.set_duration(14.0)

        # Персонажи, камеры, реквизит и звук.
        prop_crystal = PropCrystalProp(root=self, name='prop_crystal', light_group=9, init_point='prop_crystal',
            rotate_from_quat=True)
        prop_tome = PropTomeProp(root=self, name='prop_tome', light_group=9, init_point='prop_tome',
            rotate_from_quat=True)
        the_cart2 = TheCart2Prop(root=self, name='the_cart2', light_group=3, init_point='the_cart2',
            rotate_from_quat=True)
        the_cart3 = TheCart3Prop(root=self, name='the_cart3', light_group=3, init_point='the_cart3',
            rotate_from_quat=True)
        the_cart4 = TheCart4Prop(root=self, name='the_cart4', light_group=3, init_point='the_cart4',
            rotate_from_quat=True)
        crateb1 = Crateb1Prop(root=self, name='crateB1', light_group=3, init_point='crateB1',
            rotate_from_quat=True)
        crateb2 = Crateb2Prop(root=self, name='crateB2', light_group=3, init_point='crateB2',
            rotate_from_quat=True)
        cratec1 = Cratec1Prop(root=self, name='crateC1', light_group=3, init_point='crateC1',
            rotate_from_quat=True)
        cratec2 = Cratec2Prop(root=self, name='crateC2', light_group=3, init_point='crateC2',
            rotate_from_quat=True)
        cratea1 = Cratea1Prop(root=self, name='crateA1', light_group=3, init_point='crateA1',
            rotate_from_quat=True)
        cratea2 = Cratea2Prop(root=self, name='crateA2', light_group=3, init_point='crateA2',
            rotate_from_quat=True)
        camera_x = StaticCamera(root=self, name='Camera_X', fov=35, farplane=100000, nearplane=0.1,
            aspect=1.333333)
        alaric_ship = AlaricShipProp(root=self, name='alaric_ship', light_group=3, init_point='alaric_ship',
            rotate_from_quat=True, loadout='lod_ms6_alaric_cloak')
        playership = PlayershipProp(root=self, name='PlayerShip', light_group=3, init_point='PlayerShip',
            rotate_from_quat=True)
        trent = Character(root=self, actor=actors.Default, name='Char_Trent', light_group=0,
            init_point='Char_Trent', rotate_from_quat=True, use_ambient=True, appearance='trent',
            actor_name='trent')
        path_cameralaunch = MotionPath(root=self, name='Path_CameraLaunch', point_name='Path_CameraLaunch',
            path_data='{-20,4,0}, {1,0,0,0}, {-45,12,4}, {1,0,0,0}')
        path_playershipstart = MotionPath(root=self, name='Path_PlayerShipStart',
            point_name='Path_PlayerShipStart', path_data='{0,0,0}, {0.25,0,0.75,0}, {0,0.001,0}, {0.25,0,0.75,0}')
        path_playership = MotionPath(root=self, name='Path_PlayerShip', point_name='Path_PlayerShip',
            path_data='{0,0,0}, {1,0,0,0}, {1,4,0}, {1,0,0,0}')
        path_playershipflyout = MotionPath(root=self, name='Path_PlayerShipFlyOut',
            point_name='Path_PlayerShipFlyOut', path_data='{1,4,0}, {0.25,0,-0.5,0}, {50,4,0}, {0.5,0,-0.5,0}')
        path_alaricship = MotionPath(root=self, name='Path_AlaricShip', point_name='Path_AlaricShip',
            path_data='{-15,3,-5}, {0.25,0,-0.5,0}, {-14,9,0}, {0.5,0,0.5,0}')
        path_alaricshiporient = MotionPath(root=self, name='Path_AlaricShipOrient',
            point_name='Path_AlaricShipOrient', path_data='{-15,3,-5}, {0.25,0,-0.5,0}, {-1,9,0}, {0.5,0,0.5,0}')
        path_alaricshipflyaway = MotionPath(root=self, name='Path_AlaricShipFlyAway',
            point_name='Path_AlaricShipFlyAway', path_data='{-14,9,0}, {0.5,0,0.5,0}, {-50,9,0}, {0.25,0,-0.5,0}')
        camera_running = LookAtCamera(root=self, name='Camera_Running', fov=35, farplane=100000, nearplane=0.1,
            aspect=1.333333, look_duration=300)
        path_camerarunning = MotionPath(root=self, name='Path_CameraRunning', point_name='Path_CameraRunning',
            path_data='{-1, 3, 35}, {1,0,0,0}, {0, 4, 20}, {1,0,0,0}')
        path_mrkcamerarunning = MotionPath(root=self, name='Path_MrkCameraRunning',
            point_name='Path_MrkCameraRunning', path_data='{0, 0, 30}, {1,0,0,0}, {0, 5, 10}, {1,0,0,0}')
        camera_launch = LookAtCamera(root=self, name='Camera_Launch', fov=35, farplane=100000, nearplane=0.1,
            aspect=1.333333, look_duration=300)
        path_mrkcameralaunch = MotionPath(root=self, name='Path_MrkCameraLaunch',
            point_name='Path_MrkCameraLaunch', path_data='{0, 2, 0}, {1,0,0,0}, {0, 5, 0}, {1,0,0,0}')
        playershipengines_2 = Alchemy(root=self, name='PlayerShipEngines_2', particles='PlayerShipEngines',
            point_name='PlayerShipEngines_2', sparam=0, light_group=0, sort_group=0, hidden=False,
            use_ambient=True)
        music_main = Sound(root=self, name='music_main', sound='music_upcoming_action_heavy', attenuation=0,
            dmin=50, dmax=300, priority='Story_Sound_1')
        start_sound = Sound(root=self, name='start_sound', sound='engine_playership_launch_turbine',
            attenuation=0, dmin=50, dmax=300, priority='Story_Sound_1')
        launch_sound = Sound(root=self, name='launch_sound', sound='engine_playership_launch', attenuation=0,
            dmin=50, dmax=300, priority='Story_Sound_1')

        # Исходные точки взгляда.

        # Абсолютное время исходной сцены; часы MAIN не сдвигаются.
        t = 0
        ConnectHardpointEvent(root=self, group=MAIN, target_name=prop_crystal.name, parent_name=trent.name,
            duration=50000, target_hardpoint='HpLefthandConnect_prop_crystal', parent_hardpoint='hpleftconnect',
            time_delay=t)
        ConnectHardpointEvent(root=self, group=MAIN, target_name=prop_tome.name, parent_name=trent.name,
            duration=10000, target_hardpoint='rhand_connect_tome', parent_hardpoint='hprightconnect', time_delay=t)
        LookAtEvent(root=self, group=MAIN, point=camera_x.name, focus='Mrk_CameraInit', duration=300,
            target_type='ROOT', target_part='', up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        PathAnimationEvent(root=self, group=MAIN, target_name=playership.name, path=path_playershipstart,
            duration=0.001, adjust_pos=True, adjust_orient=True, start_percent=0, stop_percent=1, smooth=True,
            time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_RNNG_000LV_XA_01, duration=15, time_delay=t)
        camera_running.set(group=MAIN, time_delay=t)
        PathAnimationEvent(root=self, group=MAIN, target_name=camera_running.name, path=path_camerarunning,
            duration=5, adjust_pos=True, adjust_orient=False, start_percent=0, stop_percent=1, smooth=True,
            time_delay=t)
        PathAnimationEvent(root=self, group=MAIN, target_name=self.get_automarker_name('Camera_Running_focus'),
            path=path_mrkcamerarunning, duration=5, adjust_pos=True, adjust_orient=False, start_percent=0,
            stop_percent=1, smooth=True, time_delay=t)
        music_main.start(group=MAIN, duration=500, loop=False, start_time=0, time_delay=t)
        t += 0.6
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_RNNG_000LV_XA_01, duration=15, time_delay=t)
        t += 0.6
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_RNNG_000LV_XA_01, duration=15, time_delay=t)
        t += 0.6
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_RNNG_000LV_XA_01, duration=15, time_delay=t)
        t += 0.6
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_RNNG_000LV_XA_01, duration=15, time_delay=t)
        t += 0.6
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_RNNG_000LV_XA_01, duration=15, time_delay=t)
        t += 0.6
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_RNNG_000LV_XA_01, duration=15, time_delay=t)
        t += 0.6
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_RNNG_000LV_XA_01, duration=15, time_delay=t)
        t += 0.6
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_RNNG_000LV_XA_01, duration=15, time_delay=t)
        t += 0.2
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('Mrk_OffScreen'), duration=0.001, smooth=False, adjust_pos=True,
            adjust_orient=True, offset=(25000, 0, 0), time_delay=t)
        PathAnimationEvent(root=self, group=MAIN, target_name=alaric_ship.name, path=path_alaricshiporient,
            duration=8, adjust_pos=False, adjust_orient=True, start_percent=0, stop_percent=1, smooth=True,
            time_delay=t)
        PathAnimationEvent(root=self, group=MAIN, target_name=alaric_ship.name, path=path_alaricship, duration=5,
            adjust_pos=True, adjust_orient=False, start_percent=0, stop_percent=1, smooth=True, time_delay=t)
        camera_launch.set(group=MAIN, time_delay=t)
        PathAnimationEvent(root=self, group=MAIN, target_name=camera_launch.name, path=path_cameralaunch,
            duration=10, adjust_pos=True, adjust_orient=False, start_percent=0, stop_percent=1, smooth=True,
            time_delay=t)
        PathAnimationEvent(root=self, group=MAIN, target_name=self.get_automarker_name('Camera_Launch_focus'),
            path=path_mrkcameralaunch, duration=10, adjust_pos=True, adjust_orient=False, start_percent=0,
            stop_percent=1, smooth=True, time_delay=t)
        playershipengines_2.set_sparam(group=MAIN, duration=0.1, sparam=0.5, smooth=False, time_delay=t)
        playershipengines_2.start(group=MAIN, duration=20, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=playershipengines_2.name, parent_name=playership.name,
            duration=30, target_part='HpEngine01', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        start_sound.start(group=MAIN, duration=500, loop=False, start_time=0, time_delay=t)
        t += 5
        RotateAxisEvent(root=self, group=MAIN, object_name=playership.name, angle=135, axis='Y_AXIS', duration=7,
            smooth=False, time_delay=t)
        PathAnimationEvent(root=self, group=MAIN, target_name=playership.name, path=path_playership, duration=3,
            adjust_pos=True, adjust_orient=False, start_percent=0, stop_percent=1, smooth=True, time_delay=t)
        PathAnimationEvent(root=self, group=MAIN, target_name=alaric_ship.name, path=path_alaricshipflyaway,
            duration=5, adjust_pos=True, adjust_orient=False, start_percent=0, stop_percent=1, smooth=True,
            time_delay=t)
        t += 1
        launch_sound.start(group=MAIN, duration=500, loop=False, start_time=0, time_delay=t)
        t += 2
        PathAnimationEvent(root=self, group=MAIN, target_name=playership.name, path=path_playershipflyout,
            duration=5, adjust_pos=True, adjust_orient=False, start_percent=0, stop_percent=1, smooth=True,
            time_delay=t)
