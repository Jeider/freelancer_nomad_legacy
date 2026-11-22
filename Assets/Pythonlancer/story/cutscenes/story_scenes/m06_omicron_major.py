"""m06_omicron_major: полная постановка из master; точки в m06_omicron_major.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Alchemy, AttachEvent, ConnectHardpointEvent, Light, LookAtCamera, MAIN, MotionEvent, MotionPath, MoveEvent, PathAnimationEvent, Prop, RotateAxisEvent, Ship, Solar, Sound,
)

from story import actors


class BigshipProp(Ship):
    COMPOUND_TEMPLATE_NAME = 'or_osiris'

class PlayershipProp(Ship):
    COMPOUND_TEMPLATE_NAME = 'PlayerShip'

class PlayerConnecterProp(Solar):
    COMPOUND_TEMPLATE_NAME = 'hidden_connect'

class LiElite01Prop(Ship):
    COMPOUND_TEMPLATE_NAME = 'li_elite'

class LiElite02Prop(Ship):
    COMPOUND_TEMPLATE_NAME = 'li_elite'

class LiElite03Prop(Ship):
    COMPOUND_TEMPLATE_NAME = 'li_elite'

class LiElite04Prop(Ship):
    COMPOUND_TEMPLATE_NAME = 'li_elite'

class OrElite01Prop(Ship):
    COMPOUND_TEMPLATE_NAME = 'or_elite'

class OrElite02Prop(Ship):
    COMPOUND_TEMPLATE_NAME = 'or_elite'

class AmbiSkydomeCloudsSnowProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'edge_exclusion'
    SRT_GRP = -100
    USR_FLG = 2

class LapaProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'equip_magnet'


class M06OmicronMajorScene(Scene):
    DUMP_FILE = 'm06_omicron_major'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)
        self.set_duration(60.0)

        # Персонажи, камеры, реквизит и звук.
        light_scene = Light(root=self, name='Light_SCENE', point_name='Light_SCENE', extra_name='', light_group=0,
            hidden=True, rotate_from_quat=True, diffuse=[0.8, 0.3, 0.7], ambient=[0.2, 0.4, 0.35],
            direction=[-1, 0, 0], light_type='L_DIRECT', range=10000, cutoff=90, theta=90, color=[255, 255, 255],
            attenuation=[1, 0, 4e-06], on=True)
        camera_1 = LookAtCamera(root=self, name='Camera_1', fov=35, farplane=120000, look_duration=60)
        bigship = BigshipProp(root=self, name='BIGSHIP', light_group=0, init_point='BIGSHIP',
            rotate_from_quat=True, loadout='or_osiris')
        playership = PlayershipProp(root=self, name='PlayerShip', light_group=0, init_point='PlayerShip',
            rotate_from_quat=True)
        player_connecter = PlayerConnecterProp(root=self, name='Player_connecter', light_group=0,
            init_point='Player_connecter', rotate_from_quat=True)
        li_elite01 = LiElite01Prop(root=self, name='li_elite01', light_group=0, init_point='li_elite01',
            rotate_from_quat=True, loadout='level_li_elite_loadout04')
        li_elite02 = LiElite02Prop(root=self, name='li_elite02', light_group=0, init_point='li_elite02',
            rotate_from_quat=True, loadout='level_li_elite_loadout04')
        li_elite03 = LiElite03Prop(root=self, name='li_elite03', light_group=0, init_point='li_elite03',
            rotate_from_quat=True, loadout='level_li_elite_loadout04')
        li_elite04 = LiElite04Prop(root=self, name='li_elite04', light_group=0, init_point='li_elite04',
            rotate_from_quat=True, loadout='level_li_elite_loadout04')
        or_elite01 = OrElite01Prop(root=self, name='or_elite01', light_group=0, init_point='or_elite01',
            rotate_from_quat=True, loadout='ms6_cloak_co_elite2')
        or_elite02 = OrElite02Prop(root=self, name='or_elite02', light_group=0, init_point='or_elite02',
            rotate_from_quat=True, loadout='ms6_cloak_co_elite2')
        ambi_ltg11_puffs_amb = Light(root=self, name='ambi_LtG11_Puffs_Amb', point_name='ambi_LtG11_Puffs_Amb',
            extra_name='', light_group=11, hidden=False, rotate_from_quat=True, diffuse=[0, 0, 0],
            ambient=[0.2352941, 0.5882353, 0.3921569], direction=[0, 0, 1], light_type='L_DIRECT', range=2000,
            cutoff=98.999977, theta=90, color=[255, 255, 255], attenuation=[1, 0, 0], on=True)
        ambi_skydome_clouds_snow = AmbiSkydomeCloudsSnowProp(root=self, name='ambi_skydome_clouds_snow',
            light_group=23, init_point='ambi_skydome_clouds_snow', rotate_from_quat=True, use_ambient=True,
            use_dynamic=False, no_fog=True)
        path_goto_pl = MotionPath(root=self, name='Path_GOTO_PL', point_name='Path_GOTO_PL',
            path_data='{0, 75, -400}, {1,0,0,0}, {0, 75, -65}, {1,0,0,0}')
        path_order01_position = MotionPath(root=self, name='Path_Order01_Position',
            point_name='Path_Order01_Position',
            path_data='{-75, 10, -80}, {1,0,0,0}, {-65, 10, -10}, {1,0,0,0}, {-20, 10, 20}, {1,0,0,0}')
        path_order02_position = MotionPath(root=self, name='Path_Order02_Position',
            point_name='Path_Order02_Position',
            path_data='{-40, 10, -100}, {1,0,0,0}, {-35, 10, -50}, {1,0,0,0}, {-15, 10, -25}, {1,0,0,0}')
        lapa = LapaProp(root=self, name='lapa', light_group=0, init_point='lapa', rotate_from_quat=True)
        lapa_down = MotionPath(root=self, name='lapa_down', point_name='lapa_down',
            path_data='{0, 50, 0}, {1,0,0,0}, {0, 25, 0}, {1,0,0,0}')
        lapa_up = MotionPath(root=self, name='lapa_up', point_name='lapa_up',
            path_data='{0, 25, 0}, {1,0,0,0}, {0, 75, 0}, {1,0,0,0}')
        player_up = MotionPath(root=self, name='player_up', point_name='player_up',
            path_data='{0, 12, 0}, {1,0,0,0}, {0, 62, 0}, {1,0,0,0}')
        playershipengines_2 = Alchemy(root=self, name='PlayerShipEngines_2', particles='PlayerShipEngines',
            point_name='PlayerShipEngines_2', sparam=0, light_group=0, sort_group=0, hidden=False,
            use_ambient=True)
        fx_li_engine1 = Alchemy(root=self, name='fx_li_engine1', particles='gf_li_smallengine02_fire',
            point_name='fx_li_engine1', sparam=0, light_group=0, sort_group=0, hidden=False, use_ambient=True)
        fx_li_engine2 = Alchemy(root=self, name='fx_li_engine2', particles='gf_li_smallengine02_fire',
            point_name='fx_li_engine2', sparam=0, light_group=0, sort_group=0, hidden=False, use_ambient=True)
        fx_li_engine3 = Alchemy(root=self, name='fx_li_engine3', particles='gf_li_smallengine02_fire',
            point_name='fx_li_engine3', sparam=0, light_group=0, sort_group=0, hidden=False, use_ambient=True)
        fx_li_engine4 = Alchemy(root=self, name='fx_li_engine4', particles='gf_li_smallengine02_fire',
            point_name='fx_li_engine4', sparam=0, light_group=0, sort_group=0, hidden=False, use_ambient=True)
        fx_li_trapped1 = Alchemy(root=self, name='fx_li_trapped1', particles='ms6_trapped',
            point_name='fx_li_trapped1', sparam=0, light_group=0, sort_group=0, hidden=False, use_ambient=True)
        fx_li_trapped2 = Alchemy(root=self, name='fx_li_trapped2', particles='ms6_trapped',
            point_name='fx_li_trapped2', sparam=0, light_group=0, sort_group=0, hidden=False, use_ambient=True)
        fx_li_trapped3 = Alchemy(root=self, name='fx_li_trapped3', particles='ms6_trapped',
            point_name='fx_li_trapped3', sparam=0, light_group=0, sort_group=0, hidden=False, use_ambient=True)
        fx_player_trapped = Alchemy(root=self, name='fx_player_trapped', particles='ms6_trapped',
            point_name='fx_player_trapped', sparam=0, light_group=0, sort_group=0, hidden=False, use_ambient=True)
        fx_li_trapped4 = Alchemy(root=self, name='fx_li_trapped4', particles='ms6_trapped',
            point_name='fx_li_trapped4', sparam=0, light_group=0, sort_group=0, hidden=False, use_ambient=True)
        fx_or_engine1a = Alchemy(root=self, name='fx_or_engine1a', particles='gf_co_smallengine02_fire',
            point_name='fx_or_engine1a', sparam=0, light_group=0, sort_group=0, hidden=False, use_ambient=True)
        fx_or_engine1b = Alchemy(root=self, name='fx_or_engine1b', particles='gf_co_smallengine02_fire',
            point_name='fx_or_engine1b', sparam=0, light_group=0, sort_group=0, hidden=False, use_ambient=True)
        fx_or_engine1c = Alchemy(root=self, name='fx_or_engine1c', particles='gf_co_smallengine02_fire',
            point_name='fx_or_engine1c', sparam=0, light_group=0, sort_group=0, hidden=False, use_ambient=True)
        fx_or_engine2a = Alchemy(root=self, name='fx_or_engine2a', particles='gf_co_smallengine02_fire',
            point_name='fx_or_engine2a', sparam=0, light_group=0, sort_group=0, hidden=False, use_ambient=True)
        fx_or_engine2b = Alchemy(root=self, name='fx_or_engine2b', particles='gf_co_smallengine02_fire',
            point_name='fx_or_engine2b', sparam=0, light_group=0, sort_group=0, hidden=False, use_ambient=True)
        fx_or_engine2c = Alchemy(root=self, name='fx_or_engine2c', particles='gf_co_smallengine02_fire',
            point_name='fx_or_engine2c', sparam=0, light_group=0, sort_group=0, hidden=False, use_ambient=True)
        camera_start_path = MotionPath(root=self, name='camera_start_path', point_name='camera_start_path',
            path_data='{10, 10, 20}, {1,0,0,0}, {30, 15, -5}, {1,0,0,0}')
        marker_start_path = MotionPath(root=self, name='marker_start_path', point_name='marker_start_path',
            path_data='{-100, 10, 100}, {1,0,0,0}, {-100, -10, 0}, {1,0,0,0}')
        camera_bigship_arrive_path = MotionPath(root=self, name='camera_bigship_arrive_path',
            point_name='camera_bigship_arrive_path', path_data='{30, 15, -5}, {1,0,0,0}, {20, 5, 60}, {1,0,0,0}')
        marker_bigship_arrive_path = MotionPath(root=self, name='marker_bigship_arrive_path',
            point_name='marker_bigship_arrive_path',
            path_data='{-100, -10, 0}, {1,0,0,0}, {0, 75, -300}, {1,0,0,0}')
        camera_baydoor_path = MotionPath(root=self, name='camera_baydoor_path', point_name='camera_baydoor_path',
            path_data='{60, 40, 10}, {1,0,0,0}, {35, 25, -20}, {1,0,0,0}, {-10, 10, -35}, {1,0,0,0}')
        marker_baydoor_path = MotionPath(root=self, name='marker_baydoor_path', point_name='marker_baydoor_path',
            path_data='{0, 50, 0}, {1,0,0,0}, {0, 35, 0}, {1,0,0,0}')
        marker_baydoor_down_path = MotionPath(root=self, name='marker_baydoor_down_path',
            point_name='marker_baydoor_down_path', path_data='{0, 35, 0}, {1,0,0,0}, {0, 15, 0}, {1,0,0,0}')
        camera_getting_path = MotionPath(root=self, name='camera_getting_path', point_name='camera_getting_path',
            path_data='{-10, 10, -35}, {1,0,0,0}, {-20, 5, -55}, {1,0,0,0}')
        marker_getting_path = MotionPath(root=self, name='marker_getting_path', point_name='marker_getting_path',
            path_data='{0, 15, 0}, {1,0,0,0}, {0, 50, 0}, {1,0,0,0}')
        gf_rtc_shipcushion_1 = Alchemy(root=self, name='gf_rtc_shipcushion_1', particles='gf_rtc_shipcushion',
            point_name='gf_rtc_shipcushion_1', sparam=0, light_group=0, sort_group=0, hidden=False,
            use_ambient=True)
        music_main = Sound(root=self, name='music_main', sound='music_danger', attenuation=-15, dmin=50, dmax=300,
            priority='Story_Sound_1')
        rumble_player = Sound(root=self, name='rumble_player', sound='rumble_ci_h_fighter', attenuation=-5,
            dmin=50, dmax=300, priority='Story_Sound_1')
        rumble_osiris = Sound(root=self, name='rumble_osiris', sound='rumble_battleship', attenuation=-5, dmin=50,
            dmax=300, priority='Story_Sound_1')
        open_baydoor = Sound(root=self, name='open_baydoor', sound='depot_open_sound', attenuation=0, dmin=50,
            dmax=300, priority='Story_Sound_1')
        close_baydoor = Sound(root=self, name='close_baydoor', sound='depot_close_sound', attenuation=0, dmin=50,
            dmax=300, priority='Story_Sound_1')
        extend_lapa = Sound(root=self, name='extend_lapa', sound='hanger_doors_opening', attenuation=0, dmin=50,
            dmax=300, priority='Story_Sound_1')
        move_lapa_back = Sound(root=self, name='move_lapa_back', sound='hanger_doors_closing', attenuation=0,
            dmin=50, dmax=300, priority='Story_Sound_1')

        # Исходные точки взгляда.

        # Абсолютное время исходной сцены; часы MAIN не сдвигаются.
        t = 0
        camera_1.set(group=MAIN, time_delay=t)
        ConnectHardpointEvent(root=self, group=MAIN, target_name=playership.name,
            parent_name=player_connecter.name, duration=60, target_hardpoint='HpTop',
            parent_hardpoint='HpConnect', time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=player_connecter.name,
            parent_name=self.get_automarker_name('Player_Marker'), duration=60, target_part='',
            target_type='ROOT', adjust_pos=True, adjust_orient=True, entity_relative=True, up='Y_AXIS',
            front='NEG_Z_AXIS', time_delay=t)
        playershipengines_2.set_sparam(group=MAIN, duration=0.1, sparam=0.5, smooth=False, time_delay=t)
        playershipengines_2.start(group=MAIN, duration=60, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=playershipengines_2.name, parent_name=playership.name,
            duration=30, target_part='HpEngine01', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        fx_player_trapped.start(group=MAIN, duration=60, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=fx_player_trapped.name, parent_name=playership.name,
            duration=60, target_part='HpRoot', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        fx_li_engine1.start(group=MAIN, duration=60, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=fx_li_engine1.name, parent_name=li_elite01.name,
            duration=60, target_part='hpengine01', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        fx_li_trapped1.start(group=MAIN, duration=60, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=fx_li_trapped1.name, parent_name=li_elite01.name,
            duration=60, target_part='HpRoot', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        fx_li_engine2.start(group=MAIN, duration=60, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=fx_li_engine2.name, parent_name=li_elite02.name,
            duration=60, target_part='hpengine01', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        fx_li_trapped2.start(group=MAIN, duration=60, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=fx_li_trapped2.name, parent_name=li_elite02.name,
            duration=60, target_part='HpRoot', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        fx_li_engine3.start(group=MAIN, duration=60, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=fx_li_engine3.name, parent_name=li_elite03.name,
            duration=60, target_part='hpengine01', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        fx_li_trapped3.start(group=MAIN, duration=60, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=fx_li_trapped3.name, parent_name=li_elite03.name,
            duration=60, target_part='HpRoot', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        fx_li_engine4.start(group=MAIN, duration=60, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=fx_li_engine4.name, parent_name=li_elite04.name,
            duration=60, target_part='hpengine01', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        fx_li_trapped4.start(group=MAIN, duration=60, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=fx_li_trapped4.name, parent_name=li_elite04.name,
            duration=60, target_part='HpRoot', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        fx_or_engine1a.start(group=MAIN, duration=60, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=fx_or_engine1a.name, parent_name=or_elite01.name,
            duration=60, target_part='hpengine01', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        fx_or_engine1a.set_sparam(group=MAIN, duration=0.5, sparam=0.8, smooth=False, time_delay=t)
        fx_or_engine1b.start(group=MAIN, duration=60, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=fx_or_engine1b.name, parent_name=or_elite01.name,
            duration=60, target_part='hpengine02', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        fx_or_engine1b.set_sparam(group=MAIN, duration=0.5, sparam=0.8, smooth=False, time_delay=t)
        fx_or_engine1c.start(group=MAIN, duration=60, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=fx_or_engine1c.name, parent_name=or_elite01.name,
            duration=60, target_part='hpengine03', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        fx_or_engine1c.set_sparam(group=MAIN, duration=0.5, sparam=0.8, smooth=False, time_delay=t)
        fx_or_engine2a.start(group=MAIN, duration=60, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=fx_or_engine2a.name, parent_name=or_elite02.name,
            duration=60, target_part='hpengine01', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        fx_or_engine2a.set_sparam(group=MAIN, duration=0.5, sparam=0.8, smooth=False, time_delay=t)
        fx_or_engine2b.start(group=MAIN, duration=60, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=fx_or_engine2b.name, parent_name=or_elite02.name,
            duration=60, target_part='hpengine02', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        fx_or_engine2b.set_sparam(group=MAIN, duration=0.5, sparam=0.8, smooth=False, time_delay=t)
        fx_or_engine2c.start(group=MAIN, duration=60, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=fx_or_engine2c.name, parent_name=or_elite02.name,
            duration=60, target_part='hpengine03', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        fx_or_engine2c.set_sparam(group=MAIN, duration=0.5, sparam=0.8, smooth=False, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=li_elite01.name, anim='Sc_force extend', duration=30,
            trans_scale=1, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=li_elite02.name, anim='Sc_force extend', duration=30,
            trans_scale=1, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=li_elite03.name, anim='Sc_force extend', duration=30,
            trans_scale=1, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=li_elite04.name, anim='Sc_force extend', duration=30,
            trans_scale=1, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=or_elite01.name, anim='Sc_launch extend', duration=30,
            time_scale=1000, trans_scale=1, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=or_elite02.name, anim='Sc_launch extend', duration=30,
            time_scale=1000, trans_scale=1, time_delay=t)
        PathAnimationEvent(root=self, group=MAIN, target_name=camera_1.name, path=camera_start_path, duration=10,
            adjust_pos=True, adjust_orient=False, start_percent=0, stop_percent=1, smooth=True, time_delay=t)
        PathAnimationEvent(root=self, group=MAIN, target_name=self.get_automarker_name('Camera_1_focus'),
            path=marker_start_path, duration=10, adjust_pos=True, adjust_orient=False, start_percent=0,
            stop_percent=1, smooth=True, time_delay=t)
        gf_rtc_shipcushion_1.start(group=MAIN, duration=300, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=gf_rtc_shipcushion_1.name, parent_name=lapa.name,
            duration=600, target_part='HpFx01', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        music_main.start(group=MAIN, duration=60, loop=True, start_time=0, time_delay=t)
        rumble_player.start(group=MAIN, duration=60, loop=True, start_time=0, time_delay=t)
        music_main.change_attenuation(group=MAIN, duration=5, attenuation=0, time_delay=t)
        t += 5
        PathAnimationEvent(root=self, group=MAIN, target_name=or_elite01.name, path=path_order01_position,
            duration=5, adjust_pos=True, adjust_orient=False, start_percent=0, stop_percent=1, smooth=True,
            time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=or_elite01.name, angle=135, axis='Y_AXIS',
            duration=4.9, smooth=False, time_delay=t)
        t += 1
        PathAnimationEvent(root=self, group=MAIN, target_name=or_elite02.name, path=path_order02_position,
            duration=5, adjust_pos=True, adjust_orient=False, start_percent=0, stop_percent=1, smooth=True,
            time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=or_elite02.name, angle=50, axis='Y_AXIS',
            duration=4.85, smooth=False, time_delay=t)
        t += 4
        fx_or_engine1a.set_sparam(group=MAIN, duration=0.5, sparam=0, smooth=False, time_delay=t)
        fx_or_engine1b.set_sparam(group=MAIN, duration=0.5, sparam=0, smooth=False, time_delay=t)
        fx_or_engine1c.set_sparam(group=MAIN, duration=0.5, sparam=0, smooth=False, time_delay=t)
        fx_or_engine2a.set_sparam(group=MAIN, duration=0.5, sparam=0, smooth=False, time_delay=t)
        fx_or_engine2b.set_sparam(group=MAIN, duration=0.5, sparam=0, smooth=False, time_delay=t)
        fx_or_engine2c.set_sparam(group=MAIN, duration=0.5, sparam=0, smooth=False, time_delay=t)
        t += 2
        PathAnimationEvent(root=self, group=MAIN, target_name=bigship.name, path=path_goto_pl, duration=15,
            adjust_pos=True, adjust_orient=False, start_percent=0, stop_percent=1, smooth=True, time_delay=t)
        PathAnimationEvent(root=self, group=MAIN, target_name=camera_1.name, path=camera_bigship_arrive_path,
            duration=10, adjust_pos=True, adjust_orient=False, start_percent=0, stop_percent=1, smooth=True,
            time_delay=t)
        PathAnimationEvent(root=self, group=MAIN, target_name=self.get_automarker_name('Camera_1_focus'),
            path=marker_bigship_arrive_path, duration=10, adjust_pos=True, adjust_orient=False, start_percent=0,
            stop_percent=1, smooth=True, time_delay=t)
        PathAnimationEvent(root=self, group=MAIN, target_name=camera_1.name, path=camera_bigship_arrive_path,
            duration=10, adjust_pos=True, adjust_orient=False, start_percent=0, stop_percent=1, smooth=True,
            time_delay=t)
        PathAnimationEvent(root=self, group=MAIN, target_name=self.get_automarker_name('Camera_1_focus'),
            path=marker_bigship_arrive_path, duration=10, adjust_pos=True, adjust_orient=False, start_percent=0,
            stop_percent=1, smooth=True, time_delay=t)
        t += 3
        rumble_osiris.start(group=MAIN, duration=45, loop=True, start_time=0, time_delay=t)
        t += 7
        PathAnimationEvent(root=self, group=MAIN, target_name=camera_1.name, path=camera_baydoor_path,
            duration=20, adjust_pos=True, adjust_orient=False, start_percent=0, stop_percent=1, smooth=True,
            time_delay=t)
        PathAnimationEvent(root=self, group=MAIN, target_name=self.get_automarker_name('Camera_1_focus'),
            path=marker_baydoor_path, duration=12, adjust_pos=True, adjust_orient=False, start_percent=0,
            stop_percent=1, smooth=True, time_delay=t)
        t += 5
        MoveEvent(root=self, group=MAIN, object_name=lapa.name,
            target_name=self.get_automarker_name('Marker_Lapa'), duration=0.001, smooth=False, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 1
        MotionEvent(root=self, group=MAIN, object_name=bigship.name, anim='Sc_open baydoor', duration=15,
            time_delay=t)
        open_baydoor.start(group=MAIN, duration=15, loop=False, start_time=0, time_delay=t)
        t += 6
        PathAnimationEvent(root=self, group=MAIN, target_name=self.get_automarker_name('Camera_1_focus'),
            path=marker_baydoor_down_path, duration=8, adjust_pos=True, adjust_orient=False, start_percent=0,
            stop_percent=1, smooth=True, time_delay=t)
        t += 2
        PathAnimationEvent(root=self, group=MAIN, target_name=lapa.name, path=lapa_down, duration=8,
            adjust_pos=True, adjust_orient=False, start_percent=0, stop_percent=1, smooth=True, time_delay=t)
        extend_lapa.start(group=MAIN, duration=15, loop=False, start_time=0, time_delay=t)
        t += 6
        PathAnimationEvent(root=self, group=MAIN, target_name=camera_1.name, path=camera_getting_path,
            duration=15, adjust_pos=True, adjust_orient=False, start_percent=0, stop_percent=1, smooth=True,
            time_delay=t)
        t += 2
        PathAnimationEvent(root=self, group=MAIN, target_name=self.get_automarker_name('Camera_1_focus'),
            path=marker_getting_path, duration=15, adjust_pos=True, adjust_orient=False, start_percent=0,
            stop_percent=1, smooth=True, time_delay=t)
        PathAnimationEvent(root=self, group=MAIN, target_name=lapa.name, path=lapa_up, duration=10,
            adjust_pos=True, adjust_orient=False, start_percent=0, stop_percent=1, smooth=True, time_delay=t)
        PathAnimationEvent(root=self, group=MAIN, target_name=self.get_automarker_name('Player_Marker'),
            path=player_up, duration=10, adjust_pos=True, adjust_orient=False, start_percent=0, stop_percent=1,
            smooth=True, time_delay=t)
        move_lapa_back.start(group=MAIN, duration=15, loop=False, start_time=0, time_delay=t)
        t += 6
        music_main.change_attenuation(group=MAIN, duration=10, attenuation=-25, time_delay=t)
        t += 2
        MotionEvent(root=self, group=MAIN, object_name=bigship.name, anim='Sc_close baydoor', duration=15,
            time_scale=-1, time_delay=t)
        close_baydoor.start(group=MAIN, duration=15, loop=False, start_time=0, time_delay=t)
