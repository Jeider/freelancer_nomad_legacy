"""m06_lab_land: полная постановка из master; точки в m06_lab_land.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character, ConnectHardpointEvent, Light, LookAtCamera, LookAtEvent, MAIN, Male, MotionPath, MoveEvent, PathAnimationEvent, Prop, RotateAxisEvent, Ship, Sound, StaticCamera,
)
from story.cutscenes.anim import (
    Male,
)
from story import actors


class PropPdaProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'pda'

class PropPilotProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'the_ship_pilot_trent'
    SRT_GRP = 1

class PlayershipProp(Ship):
    COMPOUND_TEMPLATE_NAME = 'PlayerShip'

class AlaricShipProp(Ship):
    COMPOUND_TEMPLATE_NAME = 'li_elite'


class M06LabLandScene(Scene):
    DUMP_FILE = 'm06_lab_land'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)
        self.set_duration(40.0)

        # Персонажи, камеры, реквизит и звук.
        prop_pda = PropPdaProp(root=self, name='prop_pda', light_group=0, init_point='prop_pda',
            rotate_from_quat=True)
        prop_pilot = PropPilotProp(root=self, name='prop_pilot', light_group=3, init_point='prop_pilot',
            rotate_from_quat=True)
        playership = PlayershipProp(root=self, name='PlayerShip', light_group=3, init_point='PlayerShip',
            rotate_from_quat=True)
        alaric_ship = AlaricShipProp(root=self, name='alaric_ship', light_group=3, init_point='alaric_ship',
            rotate_from_quat=True, loadout='lod_ms6_alaric_cloak')
        doors_sound = Sound(root=self, name='doors_sound', sound='hanger_doors_opening', attenuation=0, dmin=50,
            dmax=250, priority=None)
        cart_sound1 = Sound(root=self, name='cart_sound1', sound='equipment_cart_start', attenuation=-10, dmin=50,
            dmax=250, priority=None)
        cart_sound2 = Sound(root=self, name='cart_sound2', sound='equipment_cart_loop', attenuation=-10, dmin=50,
            dmax=250, priority=None)
        cart_sound3 = Sound(root=self, name='cart_sound3', sound='equipment_cart_stop', attenuation=-10, dmin=50,
            dmax=250, priority=None)
        turbine_sound = Sound(root=self, name='turbine_sound', sound='engine_rh_freighter_loop', attenuation=-50,
            dmin=50, dmax=250, priority=None)
        landed_sound = Sound(root=self, name='landed_sound', sound='engine_rh_freighter_kill', attenuation=2,
            dmin=50, dmax=250, priority=None)
        cam_land = StaticCamera(root=self, name='cam_land', fov=35, farplane=100000, nearplane=0.1,
            aspect=1.333333)
        path_landing = MotionPath(root=self, name='Path_Landing', point_name='Path_Landing',
            path_data='{45,5,0}, {0.5,0,0.5,0}, {20,5,0}, {0.5,0,0.5,0}, {0,0,0}, {0.25,0,0.75,0}')
        xambi_ltg00_point_trader_key_yellow = Light(root=self, name='Xambi_ltg00_point_trader_key_yellow',
            point_name='Xambi_ltg00_point_trader_key_yellow', extra_name='', light_group=5, hidden=False,
            rotate_from_quat=True, diffuse=[1, 1, 1], ambient=[0.18, 0.2, 0.18], direction=[0, 0, 1],
            light_type='L_POINT', range=2000, cutoff=98.999977, theta=90, color=[255, 255, 255],
            attenuation=[1, 0, 4e-06], on=True)
        trent = Character(root=self, actor=actors.Trent, name='Char_trent', light_group=5,
            init_point='Char_trent', rotate_from_quat=True, use_ambient=True, appearance='trent',
            actor_name='trent')
        alaric = Character(root=self, actor=actors.Alaric, name='Char_alaric', light_group=5,
            init_point='Char_alaric', rotate_from_quat=True, appearance='alaric', actor_name='alaric')
        cam_start = LookAtCamera(root=self, name='cam_start', fov=25, farplane=100000, nearplane=0.1,
            aspect=1.333333, look_duration=30)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=25, look_duration=1)
        cam_alaric = LookAtCamera(root=self, name='cam_alaric', fov=22, look_duration=51)
        cam_final = LookAtCamera(root=self, name='cam_final', fov=25, look_duration=111)

        # Исходные точки взгляда.

        # Абсолютное время исходной сцены; часы MAIN не сдвигаются.
        t = 0
        ConnectHardpointEvent(root=self, group=MAIN, target_name=prop_pda.name, parent_name=alaric.name,
            duration=66.389, target_hardpoint='Hp_LHand_PDA', parent_hardpoint='HpLeftConnect', time_delay=t)
        LookAtEvent(root=self, group=MAIN, point=cam_land.name, focus=playership.name, duration=30,
            target_type='HARDPOINT', target_part='HpRoot', up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        cam_land.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=cam_land.name,
            target_name=self.get_automarker_name('cam_land_pos2'), duration=14, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        PathAnimationEvent(root=self, group=MAIN, target_name=playership.name, path=path_landing, duration=15,
            adjust_pos=True, adjust_orient=True, start_percent=0, stop_percent=1,
            curve_points=[[0, 0, 0, 0], [0.791667, 0.977564, 0.2, 0.214286], [1, 1, 0, 0]], curve_period=-1,
            time_delay=t)
        turbine_sound.start(group=MAIN, duration=20, loop=True, start_time=0, time_delay=t)
        turbine_sound.change_attenuation(group=MAIN, duration=4, attenuation=0, time_delay=t)
        t += 0.25
        doors_sound.start(group=MAIN, duration=15, loop=False, start_time=0, time_delay=t)
        t += 9.75
        turbine_sound.change_attenuation(group=MAIN, duration=3, attenuation=-5, time_delay=t)
        t += 3
        turbine_sound.change_attenuation(group=MAIN, duration=7, attenuation=-100, time_delay=t)
        t += 1
        landed_sound.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 1.999
        MoveEvent(root=self, group=MAIN, object_name=alaric.name,
            target_name=self.get_automarker_name('point_alaric'), duration=0.001, smooth=False, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('point_trent'), duration=0.001, smooth=False, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 0.001
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_DEALR_PDA_000LV_XA_09, duration=5, start_time=2,
            time_delay=t)
        cam_start.set(group=MAIN, time_delay=t)
        cam_start.move_cam(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        cam_start.move_focus(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=5, time_scale=0.75,
            start_time=0.15, loop=True, time_delay=t)
        t += 5
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_TURN_090LV_XA_02, duration=6, time_scale=0.8,
            trans_time=1.5, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=4, time_scale=0.75,
            time_delay=t)
        t += 5
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=1, trans_time=2,
            time_delay=t)
        t += 1
        cam_trent.set(group=MAIN, time_delay=t)
        t += 0.5
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=6,
            time_scale=0.6, time_delay=t)
        t += 2.5
        cam_alaric.set(group=MAIN, time_delay=t)
        cam_alaric.move_cam(group=MAIN, index=2, duration=5, smooth=True, time_delay=t)
        cam_alaric.move_focus(group=MAIN, index=2, duration=5, smooth=True, time_delay=t)
        t += 1
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=6, time_scale=0.6,
            time_delay=t)
        t += 1
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_TURN_270LV_XA_04, duration=6, trans_time=1.5,
            time_delay=t)
        t += 2.7
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_1STEP_SIDWYSL_000LV_XA_02, duration=3, time_scale=1.2,
            time_delay=t)
        t += 0.3
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_DEALR_PDA_000LV_XA_09, duration=6, trans_time=1.5,
            time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=12, axis='Y_AXIS', duration=1.5,
            smooth=True, time_delay=t)
        t += 0.5
        cam_final.set(group=MAIN, time_delay=t)
        cam_final.move_focus(group=MAIN, index=2, duration=5, smooth=True, time_delay=t)
        t += 1
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_RUN_TRNS_000LV_XA_02, duration=16, time_scale=0.8,
            trans_time=1, time_delay=t)
        t += 2.5
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_RNNG_000LV_XA_01, duration=16, time_scale=0.6, time_delay=t)

        # m06_lab_land 10: Трент, у нас мало времени. Я уже установил взрывчатку с таймером обратного отсчета.
        self.add_group('voice_17', time=22)
        alaric.facial(group='voice_17', index=10, auto_lip=True, extra_delay=0, append=False)

        # m06_lab_land 20: Мы же хотели просто закрыть сферу?
        self.add_group('voice_22', time=27)
        trent.facial(group='voice_22', index=20, auto_lip=True, extra_delay=0, append=False)

        # m06_lab_land 30: Вот мы и закроем. Хетчер решила подстраховаться. Мы уничтожим лабораторию.
        self.add_group('voice_28', time=30)
        alaric.facial(group='voice_28', index=30, auto_lip=True, extra_delay=0, append=False)

        # m06_lab_land 40: Ясно.
        self.add_group('voice_39', time=35.5)
        trent.facial(group='voice_39', index=40, auto_lip=True, extra_delay=0, append=False)
