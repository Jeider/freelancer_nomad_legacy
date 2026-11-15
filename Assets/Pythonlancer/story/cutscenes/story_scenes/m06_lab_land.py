"""m06_lab_land: постановка для ручного редактирования.

Точки: SCENES/m06_lab_land.blend → DUMPS/m06_lab_land.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — абсолютные секунды исходной сцены; часы MAIN не сдвигаются.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character,
    ConnectHardpointEvent,
    Light,
    LookAtCamera,
    MAIN,
    MotionPath,
    MoveEvent,
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
    SourceAttachEvent,
    SourcePathEvent,
    preserve_entity,
)
from story import actors


class PropPropPda(Prop):
    COMPOUND_TEMPLATE_NAME = 'pda'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropPilot(Prop):
    COMPOUND_TEMPLATE_NAME = 'the_ship_pilot_trent'
    SRT_GRP = 1
    USR_FLG = 0


class PropPlayership(Ship):
    COMPOUND_TEMPLATE_NAME = 'PlayerShip'
    SRT_GRP = 0
    USR_FLG = 0


class PropAlaricShip(Ship):
    COMPOUND_TEMPLATE_NAME = 'li_elite'
    SRT_GRP = 0
    USR_FLG = 0



class M06LabLandScene(Scene):
    DUMP_FILE = 'm06_lab_land'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(40.0)
        prop_pda = PropPropPda(root=self, name='prop_pda', light_group=0, init_point='prop_pda', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(prop_pda, userprops={'category': 'Prop'})
        prop_pilot = PropPropPilot(root=self, name='prop_pilot', light_group=3, init_point='prop_pilot',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(prop_pilot, srt_grp=1, userprops={'category': 'Prop'})
        PlayerShip = PropPlayership(root=self, name='PlayerShip', light_group=3, init_point='PlayerShip',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(PlayerShip, userprops={'category': 'Spaceship'})
        alaric_ship = PropAlaricShip(root=self, name='alaric_ship', light_group=3, init_point='alaric_ship',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(alaric_ship, userprops={'category': 'Spaceship', 'loadout': 'lod_ms6_alaric_cloak'})
        doors_sound = Sound(root=self, name='doors_sound', sound='hanger_doors_opening', attenuation=0, dmin=50, dmax=250,
            priority=None)
        preserve_entity(doors_sound)
        cart_sound1 = Sound(root=self, name='cart_sound1', sound='equipment_cart_start', attenuation=-10, dmin=50, dmax=250,
            priority=None)
        preserve_entity(cart_sound1)
        cart_sound2 = Sound(root=self, name='cart_sound2', sound='equipment_cart_loop', attenuation=-10, dmin=50, dmax=250,
            priority=None)
        preserve_entity(cart_sound2)
        cart_sound3 = Sound(root=self, name='cart_sound3', sound='equipment_cart_stop', attenuation=-10, dmin=50, dmax=250,
            priority=None)
        preserve_entity(cart_sound3)
        turbine_sound = Sound(root=self, name='turbine_sound', sound='engine_rh_freighter_loop', attenuation=-50, dmin=50,
            dmax=250, priority=None)
        preserve_entity(turbine_sound)
        landed_sound = Sound(root=self, name='landed_sound', sound='engine_rh_freighter_kill', attenuation=2, dmin=50,
            dmax=250, priority=None)
        preserve_entity(landed_sound)
        cam_land = StaticCamera(root=self, name='cam_land', fov=35, farplane=100000)
        preserve_entity(cam_land, cameraprops={'hvaspect': 1.333333, 'nearplane': 0.1})
        Path_Landing = MotionPath(root=self, name='Path_Landing', point_name='Path_Landing',
            path_data='{45,5,0}, {0.5,0,0.5,0}, {20,5,0}, {0.5,0,0.5,0}, {0,0,0}, {0.25,0,0.75,0}')
        preserve_entity(Path_Landing)
        Xambi_ltg00_point_trader_key_yellow = Light(root=self, name='Xambi_ltg00_point_trader_key_yellow',
            point_name='Xambi_ltg00_point_trader_key_yellow', extra_name='', light_group=5, diffuse=[1, 1, 1],
            ambient=[0.18, 0.2, 0.18], direction=[0, 0, 1], light_type='L_POINT', on=True, range=2000, cutoff=98.999977,
            theta=90, color=[255, 255, 255], attenuation=[1, 0, 4e-06])
        preserve_entity(Xambi_ltg00_point_trader_key_yellow)
        trent = Character(root=self, actor=actors.Trent, light_group=5, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=True, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'actor': 'trent', 'category': 'Character'})
        alaric = Character(root=self, actor=actors.Alaric, light_group=5, init_point='Char_alaric', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(alaric, template_name='alaric', userprops={'actor': 'alaric', 'category': 'Character'})
        cam_start = LookAtCamera(root=self, name='cam_start', fov=25, farplane=100000, look_duration=30)
        preserve_entity(cam_start, cameraprops={'hvaspect': 1.333333, 'nearplane': 0.1})
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=25, farplane=5000, look_duration=1)
        preserve_entity(cam_trent)
        cam_alaric = LookAtCamera(root=self, name='cam_alaric', fov=22, farplane=5000, look_duration=51)
        preserve_entity(cam_alaric)
        cam_final = LookAtCamera(root=self, name='cam_final', fov=25, farplane=5000, look_duration=111)
        preserve_entity(cam_final)

        # Действия по абсолютному времени сцены.
        t = 0
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='prop_pda', parent_name='Char_alaric',
            duration=66.389, target_hardpoint='Hp_LHand_PDA', parent_hardpoint='HpLeftConnect')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['cam_land', 'PlayerShip'], duration=30,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpRoot', target_type='HARDPOINT',
            flags='LOOK_AT')
        cam_land.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_land', target_name='automarker_cam_land_pos2',
            duration=14, smooth=True)
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['PlayerShip', 'Path_Landing'], duration=15,
            start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS',
            flags='POSITION+ORIENTATION',
            param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [0.791667, 0.977564, 0.2, 0.214286], [1, 1, 0, 0]]},
            pcurve_period=-1)
        turbine_sound.start(group=MAIN, time_delay=t, duration=20, loop=True)
        turbine_sound.change_attenuation(group=MAIN, time_delay=t, duration=4, attenuation=0)
        t += 0.25
        doors_sound.start(group=MAIN, time_delay=t, duration=15)
        t += 9.75
        turbine_sound.change_attenuation(group=MAIN, time_delay=t, duration=3, attenuation=-5)
        t += 3
        turbine_sound.change_attenuation(group=MAIN, time_delay=t, duration=7, attenuation=-100)
        t += 1
        landed_sound.start(group=MAIN, time_delay=t, duration=5)
        t += 1.999
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_alaric', target_name='automarker_point_alaric',
            duration=0.001, smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', target_name='automarker_point_trent',
            duration=0.001, smooth=False)
        t += 0.001
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_DEALR_PDA_000LV_XA_09, duration=5, start_time=2)
        cam_start.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_start', target_name='automarker_cam_start_pos2',
            duration=10, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_start_focus',
            target_name='automarker_cam_start_marker_pos2', duration=10, smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=5, time_scale=0.75,
            start_time=0.15, loop=True)
        t += 5
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_TURN_090LV_XA_02, duration=6, time_scale=0.8,
            trans_time=1.5)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=4, time_scale=0.75)
        t += 5
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=1, trans_time=2)
        t += 1
        cam_trent.set(group=MAIN, time_delay=t)
        t += 0.5
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=6,
            time_scale=0.6)
        t += 2.5
        cam_alaric.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_alaric', target_name='automarker_cam_alaric_pos2',
            duration=5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_alaric_focus',
            target_name='automarker_cam_alaric_marker_pos2', duration=5, smooth=True)
        t += 1
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=6,
            time_scale=0.6)
        t += 1
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_TURN_270LV_XA_04, duration=6, trans_time=1.5)
        t += 2.7
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_1STEP_SIDWYSL_000LV_XA_02, duration=3,
            time_scale=1.2)
        t += 0.3
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_DEALR_PDA_000LV_XA_09, duration=6, trans_time=1.5)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=12, axis='Y_AXIS',
            duration=1.5, smooth=True)
        t += 0.5
        cam_final.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_final_focus',
            target_name='automarker_cam_final_marker_pos2', duration=5, smooth=True)
        t += 1.0
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_RUN_TRNS_000LV_XA_02, duration=16, time_scale=0.8,
            trans_time=1)
        t += 2.5
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_RNNG_000LV_XA_01, duration=16, time_scale=0.6)
        self.add_group('voice_17', time=22)
        alaric.facial(group='voice_17', index=10, append=False, auto_lip=True, extra_delay=0)
        self.add_group('voice_22', time=27)
        trent.facial(group='voice_22', index=20, append=False, auto_lip=True, extra_delay=0)
        self.add_group('voice_28', time=30)
        alaric.facial(group='voice_28', index=30, append=False, auto_lip=True, extra_delay=0)
        self.add_group('voice_39', time=35.5)
        trent.facial(group='voice_39', index=40, append=False, auto_lip=True, extra_delay=0)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M06LabLandScene
