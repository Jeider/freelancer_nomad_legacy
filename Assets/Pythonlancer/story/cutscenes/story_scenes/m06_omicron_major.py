"""m06_omicron_major: постановка для ручного редактирования.

Точки: SCENES/m06_omicron_major.blend → DUMPS/m06_omicron_major.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — абсолютные секунды исходной сцены; часы MAIN не сдвигаются.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Alchemy,
    ConnectHardpointEvent,
    Light,
    LookAtCamera,
    MAIN,
    MotionEvent,
    MotionPath,
    MoveEvent,
    PlayerShip,
    Prop,
    RotateAxisEvent,
    Ship,
    Solar,
    Sound,
)

from story.cutscenes.source_extensions import (
    SourceAlchemyAnimEvent,
    SourceAttachEvent,
    SourceMotionEvent,
    SourcePathEvent,
    preserve_entity,
)
from story import actors


class PropBigship(Ship):
    COMPOUND_TEMPLATE_NAME = 'or_osiris'
    SRT_GRP = 0
    USR_FLG = 0


class PropPlayership(Ship):
    COMPOUND_TEMPLATE_NAME = 'PlayerShip'
    SRT_GRP = 0
    USR_FLG = 0


class PropPlayerConnecter(Solar):
    COMPOUND_TEMPLATE_NAME = 'hidden_connect'
    SRT_GRP = 0
    USR_FLG = 0


class PropLiElite01(Ship):
    COMPOUND_TEMPLATE_NAME = 'li_elite'
    SRT_GRP = 0
    USR_FLG = 0


class PropLiElite02(Ship):
    COMPOUND_TEMPLATE_NAME = 'li_elite'
    SRT_GRP = 0
    USR_FLG = 0


class PropLiElite03(Ship):
    COMPOUND_TEMPLATE_NAME = 'li_elite'
    SRT_GRP = 0
    USR_FLG = 0


class PropLiElite04(Ship):
    COMPOUND_TEMPLATE_NAME = 'li_elite'
    SRT_GRP = 0
    USR_FLG = 0


class PropOrElite01(Ship):
    COMPOUND_TEMPLATE_NAME = 'or_elite'
    SRT_GRP = 0
    USR_FLG = 0


class PropOrElite02(Ship):
    COMPOUND_TEMPLATE_NAME = 'or_elite'
    SRT_GRP = 0
    USR_FLG = 0


class PropAmbiSkydomeCloudsSnow(Prop):
    COMPOUND_TEMPLATE_NAME = 'edge_exclusion'
    SRT_GRP = -100
    USR_FLG = 2


class PropLapa(Prop):
    COMPOUND_TEMPLATE_NAME = 'equip_magnet'
    SRT_GRP = 0
    USR_FLG = 0



class M06OmicronMajorScene(Scene):
    DUMP_FILE = 'm06_omicron_major'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(60.0)
        Light_SCENE = Light(root=self, name='Light_SCENE', point_name='Light_SCENE', extra_name='', light_group=0,
            diffuse=[0.8, 0.3, 0.7], ambient=[0.2, 0.4, 0.35], direction=[-1, 0, 0], light_type='L_DIRECT', on=True,
            range=10000, cutoff=90, theta=90, color=[255, 255, 255], attenuation=[1, 0, 4e-06])
        preserve_entity(Light_SCENE, flags='HIDDEN')
        Camera_1 = LookAtCamera(root=self, name='Camera_1', fov=35, farplane=120000, look_duration=60)
        preserve_entity(Camera_1)
        BIGSHIP = PropBigship(root=self, name='BIGSHIP', light_group=0, init_point='BIGSHIP', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(BIGSHIP, userprops={'category': 'Spaceship', 'loadout': 'or_osiris'})
        PlayerShip = PropPlayership(root=self, name='PlayerShip', light_group=0, init_point='PlayerShip',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(PlayerShip, userprops={'category': 'Spaceship', 'running_lights': 'true'})
        Player_connecter = PropPlayerConnecter(root=self, name='Player_connecter', light_group=0,
            init_point='Player_connecter', rotate_from_quat=True, use_ambient=False)
        preserve_entity(Player_connecter, userprops={'category': 'Solar'})
        li_elite01 = PropLiElite01(root=self, name='li_elite01', light_group=0, init_point='li_elite01',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(li_elite01,
            userprops={'category': 'Spaceship', 'loadout': 'level_li_elite_loadout04', 'running_lights': 'true'})
        li_elite02 = PropLiElite02(root=self, name='li_elite02', light_group=0, init_point='li_elite02',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(li_elite02,
            userprops={'category': 'Spaceship', 'loadout': 'level_li_elite_loadout04', 'running_lights': 'true'})
        li_elite03 = PropLiElite03(root=self, name='li_elite03', light_group=0, init_point='li_elite03',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(li_elite03,
            userprops={'category': 'Spaceship', 'loadout': 'level_li_elite_loadout04', 'running_lights': 'true'})
        li_elite04 = PropLiElite04(root=self, name='li_elite04', light_group=0, init_point='li_elite04',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(li_elite04,
            userprops={'category': 'Spaceship', 'loadout': 'level_li_elite_loadout04', 'running_lights': 'true'})
        or_elite01 = PropOrElite01(root=self, name='or_elite01', light_group=0, init_point='or_elite01',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(or_elite01,
            userprops={'category': 'Spaceship', 'loadout': 'ms6_cloak_co_elite2', 'running_lights': 'true'})
        or_elite02 = PropOrElite02(root=self, name='or_elite02', light_group=0, init_point='or_elite02',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(or_elite02,
            userprops={'category': 'Spaceship', 'loadout': 'ms6_cloak_co_elite2', 'running_lights': 'true'})
        ambi_LtG11_Puffs_Amb = Light(root=self, name='ambi_LtG11_Puffs_Amb', point_name='ambi_LtG11_Puffs_Amb',
            extra_name='', light_group=11, diffuse=[0, 0, 0], ambient=[0.2352941, 0.5882353, 0.3921569],
            direction=[0, 0, 1], light_type='L_DIRECT', on=True, range=2000, cutoff=98.999977, theta=90,
            color=[255, 255, 255], attenuation=[1, 0, 0])
        preserve_entity(ambi_LtG11_Puffs_Amb)
        ambi_skydome_clouds_snow = PropAmbiSkydomeCloudsSnow(root=self, name='ambi_skydome_clouds_snow', light_group=23,
            init_point='ambi_skydome_clouds_snow', rotate_from_quat=True, use_ambient=True)
        preserve_entity(ambi_skydome_clouds_snow, flags=4, userprops={'category': 'Prop', 'NoFog': 'Y'}, usr_flg=2,
            srt_grp=-100)
        Path_GOTO_PL = MotionPath(root=self, name='Path_GOTO_PL', point_name='Path_GOTO_PL',
            path_data='{0, 75, -400}, {1,0,0,0}, {0, 75, -65}, {1,0,0,0}')
        preserve_entity(Path_GOTO_PL)
        Path_Order01_Position = MotionPath(root=self, name='Path_Order01_Position', point_name='Path_Order01_Position',
            path_data='{-75, 10, -80}, {1,0,0,0}, {-65, 10, -10}, {1,0,0,0}, {-20, 10, 20}, {1,0,0,0}')
        preserve_entity(Path_Order01_Position)
        Path_Order02_Position = MotionPath(root=self, name='Path_Order02_Position', point_name='Path_Order02_Position',
            path_data='{-40, 10, -100}, {1,0,0,0}, {-35, 10, -50}, {1,0,0,0}, {-15, 10, -25}, {1,0,0,0}')
        preserve_entity(Path_Order02_Position)
        lapa = PropLapa(root=self, name='lapa', light_group=0, init_point='lapa', rotate_from_quat=True, use_ambient=False)
        preserve_entity(lapa, userprops={'category': 'Prop'})
        lapa_down = MotionPath(root=self, name='lapa_down', point_name='lapa_down',
            path_data='{0, 50, 0}, {1,0,0,0}, {0, 25, 0}, {1,0,0,0}')
        preserve_entity(lapa_down)
        lapa_up = MotionPath(root=self, name='lapa_up', point_name='lapa_up',
            path_data='{0, 25, 0}, {1,0,0,0}, {0, 75, 0}, {1,0,0,0}')
        preserve_entity(lapa_up)
        player_up = MotionPath(root=self, name='player_up', point_name='player_up',
            path_data='{0, 12, 0}, {1,0,0,0}, {0, 62, 0}, {1,0,0,0}')
        preserve_entity(player_up)
        PlayerShipEngines_2 = Alchemy(root=self, name='PlayerShipEngines_2', particles='PlayerShipEngines',
            point_name='PlayerShipEngines_2', sparam=0)
        preserve_entity(PlayerShipEngines_2, flags='LIT_DYNAMIC+LIT_AMBIENT')
        fx_li_engine1 = Alchemy(root=self, name='fx_li_engine1', particles='gf_li_smallengine02_fire',
            point_name='fx_li_engine1', sparam=0)
        preserve_entity(fx_li_engine1, flags='LIT_DYNAMIC+LIT_AMBIENT')
        fx_li_engine2 = Alchemy(root=self, name='fx_li_engine2', particles='gf_li_smallengine02_fire',
            point_name='fx_li_engine2', sparam=0)
        preserve_entity(fx_li_engine2, flags='LIT_DYNAMIC+LIT_AMBIENT')
        fx_li_engine3 = Alchemy(root=self, name='fx_li_engine3', particles='gf_li_smallengine02_fire',
            point_name='fx_li_engine3', sparam=0)
        preserve_entity(fx_li_engine3, flags='LIT_DYNAMIC+LIT_AMBIENT')
        fx_li_engine4 = Alchemy(root=self, name='fx_li_engine4', particles='gf_li_smallengine02_fire',
            point_name='fx_li_engine4', sparam=0)
        preserve_entity(fx_li_engine4, flags='LIT_DYNAMIC+LIT_AMBIENT')
        fx_li_trapped1 = Alchemy(root=self, name='fx_li_trapped1', particles='ms6_trapped', point_name='fx_li_trapped1',
            sparam=0)
        preserve_entity(fx_li_trapped1, flags='LIT_DYNAMIC+LIT_AMBIENT')
        fx_li_trapped2 = Alchemy(root=self, name='fx_li_trapped2', particles='ms6_trapped', point_name='fx_li_trapped2',
            sparam=0)
        preserve_entity(fx_li_trapped2, flags='LIT_DYNAMIC+LIT_AMBIENT')
        fx_li_trapped3 = Alchemy(root=self, name='fx_li_trapped3', particles='ms6_trapped', point_name='fx_li_trapped3',
            sparam=0)
        preserve_entity(fx_li_trapped3, flags='LIT_DYNAMIC+LIT_AMBIENT')
        fx_player_trapped = Alchemy(root=self, name='fx_player_trapped', particles='ms6_trapped',
            point_name='fx_player_trapped', sparam=0)
        preserve_entity(fx_player_trapped, flags='LIT_DYNAMIC+LIT_AMBIENT')
        fx_li_trapped4 = Alchemy(root=self, name='fx_li_trapped4', particles='ms6_trapped', point_name='fx_li_trapped4',
            sparam=0)
        preserve_entity(fx_li_trapped4, flags='LIT_DYNAMIC+LIT_AMBIENT')
        fx_or_engine1a = Alchemy(root=self, name='fx_or_engine1a', particles='gf_co_smallengine02_fire',
            point_name='fx_or_engine1a', sparam=0)
        preserve_entity(fx_or_engine1a, flags='LIT_DYNAMIC+LIT_AMBIENT')
        fx_or_engine1b = Alchemy(root=self, name='fx_or_engine1b', particles='gf_co_smallengine02_fire',
            point_name='fx_or_engine1b', sparam=0)
        preserve_entity(fx_or_engine1b, flags='LIT_DYNAMIC+LIT_AMBIENT')
        fx_or_engine1c = Alchemy(root=self, name='fx_or_engine1c', particles='gf_co_smallengine02_fire',
            point_name='fx_or_engine1c', sparam=0)
        preserve_entity(fx_or_engine1c, flags='LIT_DYNAMIC+LIT_AMBIENT')
        fx_or_engine2a = Alchemy(root=self, name='fx_or_engine2a', particles='gf_co_smallengine02_fire',
            point_name='fx_or_engine2a', sparam=0)
        preserve_entity(fx_or_engine2a, flags='LIT_DYNAMIC+LIT_AMBIENT')
        fx_or_engine2b = Alchemy(root=self, name='fx_or_engine2b', particles='gf_co_smallengine02_fire',
            point_name='fx_or_engine2b', sparam=0)
        preserve_entity(fx_or_engine2b, flags='LIT_DYNAMIC+LIT_AMBIENT')
        fx_or_engine2c = Alchemy(root=self, name='fx_or_engine2c', particles='gf_co_smallengine02_fire',
            point_name='fx_or_engine2c', sparam=0)
        preserve_entity(fx_or_engine2c, flags='LIT_DYNAMIC+LIT_AMBIENT')
        camera_start_path = MotionPath(root=self, name='camera_start_path', point_name='camera_start_path',
            path_data='{10, 10, 20}, {1,0,0,0}, {30, 15, -5}, {1,0,0,0}')
        preserve_entity(camera_start_path)
        marker_start_path = MotionPath(root=self, name='marker_start_path', point_name='marker_start_path',
            path_data='{-100, 10, 100}, {1,0,0,0}, {-100, -10, 0}, {1,0,0,0}')
        preserve_entity(marker_start_path)
        camera_bigship_arrive_path = MotionPath(root=self, name='camera_bigship_arrive_path',
            point_name='camera_bigship_arrive_path', path_data='{30, 15, -5}, {1,0,0,0}, {20, 5, 60}, {1,0,0,0}')
        preserve_entity(camera_bigship_arrive_path)
        marker_bigship_arrive_path = MotionPath(root=self, name='marker_bigship_arrive_path',
            point_name='marker_bigship_arrive_path', path_data='{-100, -10, 0}, {1,0,0,0}, {0, 75, -300}, {1,0,0,0}')
        preserve_entity(marker_bigship_arrive_path)
        camera_baydoor_path = MotionPath(root=self, name='camera_baydoor_path', point_name='camera_baydoor_path',
            path_data='{60, 40, 10}, {1,0,0,0}, {35, 25, -20}, {1,0,0,0}, {-10, 10, -35}, {1,0,0,0}')
        preserve_entity(camera_baydoor_path)
        marker_baydoor_path = MotionPath(root=self, name='marker_baydoor_path', point_name='marker_baydoor_path',
            path_data='{0, 50, 0}, {1,0,0,0}, {0, 35, 0}, {1,0,0,0}')
        preserve_entity(marker_baydoor_path)
        marker_baydoor_down_path = MotionPath(root=self, name='marker_baydoor_down_path',
            point_name='marker_baydoor_down_path', path_data='{0, 35, 0}, {1,0,0,0}, {0, 15, 0}, {1,0,0,0}')
        preserve_entity(marker_baydoor_down_path)
        camera_getting_path = MotionPath(root=self, name='camera_getting_path', point_name='camera_getting_path',
            path_data='{-10, 10, -35}, {1,0,0,0}, {-20, 5, -55}, {1,0,0,0}')
        preserve_entity(camera_getting_path)
        marker_getting_path = MotionPath(root=self, name='marker_getting_path', point_name='marker_getting_path',
            path_data='{0, 15, 0}, {1,0,0,0}, {0, 50, 0}, {1,0,0,0}')
        preserve_entity(marker_getting_path)
        gf_rtc_shipcushion_1 = Alchemy(root=self, name='gf_rtc_shipcushion_1', particles='gf_rtc_shipcushion',
            point_name='gf_rtc_shipcushion_1', sparam=0)
        preserve_entity(gf_rtc_shipcushion_1, flags='LIT_DYNAMIC+LIT_AMBIENT')
        music_main = Sound(root=self, name='music_main', sound='music_danger', attenuation=-15, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(music_main, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        rumble_player = Sound(root=self, name='rumble_player', sound='rumble_ci_h_fighter', attenuation=-5, dmin=50,
            dmax=300, priority='Story_Sound_1')
        preserve_entity(rumble_player, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        rumble_osiris = Sound(root=self, name='rumble_osiris', sound='rumble_battleship', attenuation=-5, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(rumble_osiris, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        open_baydoor = Sound(root=self, name='open_baydoor', sound='depot_open_sound', attenuation=0, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(open_baydoor, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        close_baydoor = Sound(root=self, name='close_baydoor', sound='depot_close_sound', attenuation=0, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(close_baydoor, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        extend_lapa = Sound(root=self, name='extend_lapa', sound='hanger_doors_opening', attenuation=0, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(extend_lapa, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        move_lapa_back = Sound(root=self, name='move_lapa_back', sound='hanger_doors_closing', attenuation=0, dmin=50,
            dmax=300, priority='Story_Sound_1')
        preserve_entity(move_lapa_back, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})

        # Действия по абсолютному времени сцены.
        t = 0
        Camera_1.set(group=MAIN, time_delay=t)
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='PlayerShip', parent_name='Player_connecter',
            duration=60, target_hardpoint='HpTop', parent_hardpoint='HpConnect')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['Player_connecter', 'automarker_Player_Marker'],
            duration=60, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT',
            flags='POSITION+ORIENTATION+ENTITY_RELATIVE')
        SourceAlchemyAnimEvent(root=self, group=MAIN, time_delay=t, targets=['PlayerShipEngines_2'], duration=0.1,
            psysprops={'sparam': 0.5})
        PlayerShipEngines_2.start(group=MAIN, time_delay=t, duration=60)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['PlayerShipEngines_2', 'PlayerShip'], duration=30,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpEngine01', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION')
        fx_player_trapped.start(group=MAIN, time_delay=t, duration=60)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['fx_player_trapped', 'PlayerShip'], duration=60,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpRoot', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION')
        fx_li_engine1.start(group=MAIN, time_delay=t, duration=60)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['fx_li_engine1', 'li_elite01'], duration=60,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='hpengine01', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION')
        fx_li_trapped1.start(group=MAIN, time_delay=t, duration=60)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['fx_li_trapped1', 'li_elite01'], duration=60,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpRoot', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION')
        fx_li_engine2.start(group=MAIN, time_delay=t, duration=60)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['fx_li_engine2', 'li_elite02'], duration=60,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='hpengine01', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION')
        fx_li_trapped2.start(group=MAIN, time_delay=t, duration=60)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['fx_li_trapped2', 'li_elite02'], duration=60,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpRoot', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION')
        fx_li_engine3.start(group=MAIN, time_delay=t, duration=60)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['fx_li_engine3', 'li_elite03'], duration=60,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='hpengine01', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION')
        fx_li_trapped3.start(group=MAIN, time_delay=t, duration=60)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['fx_li_trapped3', 'li_elite03'], duration=60,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpRoot', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION')
        fx_li_engine4.start(group=MAIN, time_delay=t, duration=60)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['fx_li_engine4', 'li_elite04'], duration=60,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='hpengine01', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION')
        fx_li_trapped4.start(group=MAIN, time_delay=t, duration=60)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['fx_li_trapped4', 'li_elite04'], duration=60,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpRoot', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION')
        fx_or_engine1a.start(group=MAIN, time_delay=t, duration=60)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['fx_or_engine1a', 'or_elite01'], duration=60,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='hpengine01', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION')
        SourceAlchemyAnimEvent(root=self, group=MAIN, time_delay=t, targets=['fx_or_engine1a'], duration=0.5,
            psysprops={'sparam': 0.8})
        fx_or_engine1b.start(group=MAIN, time_delay=t, duration=60)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['fx_or_engine1b', 'or_elite01'], duration=60,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='hpengine02', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION')
        SourceAlchemyAnimEvent(root=self, group=MAIN, time_delay=t, targets=['fx_or_engine1b'], duration=0.5,
            psysprops={'sparam': 0.8})
        fx_or_engine1c.start(group=MAIN, time_delay=t, duration=60)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['fx_or_engine1c', 'or_elite01'], duration=60,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='hpengine03', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION')
        SourceAlchemyAnimEvent(root=self, group=MAIN, time_delay=t, targets=['fx_or_engine1c'], duration=0.5,
            psysprops={'sparam': 0.8})
        fx_or_engine2a.start(group=MAIN, time_delay=t, duration=60)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['fx_or_engine2a', 'or_elite02'], duration=60,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='hpengine01', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION')
        SourceAlchemyAnimEvent(root=self, group=MAIN, time_delay=t, targets=['fx_or_engine2a'], duration=0.5,
            psysprops={'sparam': 0.8})
        fx_or_engine2b.start(group=MAIN, time_delay=t, duration=60)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['fx_or_engine2b', 'or_elite02'], duration=60,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='hpengine02', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION')
        SourceAlchemyAnimEvent(root=self, group=MAIN, time_delay=t, targets=['fx_or_engine2b'], duration=0.5,
            psysprops={'sparam': 0.8})
        fx_or_engine2c.start(group=MAIN, time_delay=t, duration=60)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['fx_or_engine2c', 'or_elite02'], duration=60,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='hpengine03', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION')
        SourceAlchemyAnimEvent(root=self, group=MAIN, time_delay=t, targets=['fx_or_engine2c'], duration=0.5,
            psysprops={'sparam': 0.8})
        SourceMotionEvent(root=self, group=MAIN, time_delay=t, targets=['li_elite01'], animation='Sc_force extend',
            duration=30, time_scale=1, weight=1, trans_scale=1)
        SourceMotionEvent(root=self, group=MAIN, time_delay=t, targets=['li_elite02'], animation='Sc_force extend',
            duration=30, time_scale=1, weight=1, trans_scale=1)
        SourceMotionEvent(root=self, group=MAIN, time_delay=t, targets=['li_elite03'], animation='Sc_force extend',
            duration=30, time_scale=1, weight=1, trans_scale=1)
        SourceMotionEvent(root=self, group=MAIN, time_delay=t, targets=['li_elite04'], animation='Sc_force extend',
            duration=30, time_scale=1, weight=1, trans_scale=1)
        SourceMotionEvent(root=self, group=MAIN, time_delay=t, targets=['or_elite01'], animation='Sc_launch extend',
            duration=30, time_scale=1000, weight=1, trans_scale=1)
        SourceMotionEvent(root=self, group=MAIN, time_delay=t, targets=['or_elite02'], animation='Sc_launch extend',
            duration=30, time_scale=1000, weight=1, trans_scale=1)
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['Camera_1', 'camera_start_path'], duration=10,
            start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', flags='POSITION',
            param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]}, pcurve_period=-1000)
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['automarker_Camera_1_focus', 'marker_start_path'],
            duration=10, start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS',
            flags='POSITION', param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]},
            pcurve_period=-1000)
        gf_rtc_shipcushion_1.start(group=MAIN, time_delay=t, duration=300)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['gf_rtc_shipcushion_1', 'lapa'], duration=600,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpFx01', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION')
        music_main.start(group=MAIN, time_delay=t, duration=60, loop=True)
        rumble_player.start(group=MAIN, time_delay=t, duration=60, loop=True)
        music_main.change_attenuation(group=MAIN, time_delay=t, duration=5, attenuation=0)
        t += 5
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['or_elite01', 'Path_Order01_Position'], duration=5,
            start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', flags='POSITION',
            param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]}, pcurve_period=-1000)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='or_elite01', angle=135, axis='Y_AXIS',
            duration=4.9, smooth=False)
        t += 1
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['or_elite02', 'Path_Order02_Position'], duration=5,
            start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', flags='POSITION',
            param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]}, pcurve_period=-1000)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='or_elite02', angle=50, axis='Y_AXIS',
            duration=4.85, smooth=False)
        t += 4
        SourceAlchemyAnimEvent(root=self, group=MAIN, time_delay=t, targets=['fx_or_engine1a'], duration=0.5,
            psysprops={'sparam': 0})
        SourceAlchemyAnimEvent(root=self, group=MAIN, time_delay=t, targets=['fx_or_engine1b'], duration=0.5,
            psysprops={'sparam': 0})
        SourceAlchemyAnimEvent(root=self, group=MAIN, time_delay=t, targets=['fx_or_engine1c'], duration=0.5,
            psysprops={'sparam': 0})
        SourceAlchemyAnimEvent(root=self, group=MAIN, time_delay=t, targets=['fx_or_engine2a'], duration=0.5,
            psysprops={'sparam': 0})
        SourceAlchemyAnimEvent(root=self, group=MAIN, time_delay=t, targets=['fx_or_engine2b'], duration=0.5,
            psysprops={'sparam': 0})
        SourceAlchemyAnimEvent(root=self, group=MAIN, time_delay=t, targets=['fx_or_engine2c'], duration=0.5,
            psysprops={'sparam': 0})
        t += 2
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['BIGSHIP', 'Path_GOTO_PL'], duration=15,
            start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', flags='POSITION',
            param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]}, pcurve_period=-1000)
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['Camera_1', 'camera_bigship_arrive_path'],
            duration=10, start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS',
            flags='POSITION', param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]},
            pcurve_period=-1000)
        SourcePathEvent(root=self, group=MAIN, time_delay=t,
            targets=['automarker_Camera_1_focus', 'marker_bigship_arrive_path'], duration=10, start_percent=0,
            stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', flags='POSITION',
            param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]}, pcurve_period=-1000)
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['Camera_1', 'camera_bigship_arrive_path'],
            duration=10, start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS',
            flags='POSITION', param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]},
            pcurve_period=-1000)
        SourcePathEvent(root=self, group=MAIN, time_delay=t,
            targets=['automarker_Camera_1_focus', 'marker_bigship_arrive_path'], duration=10, start_percent=0,
            stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', flags='POSITION',
            param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]}, pcurve_period=-1000)
        t += 3
        rumble_osiris.start(group=MAIN, time_delay=t, duration=45, loop=True)
        t += 7
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['Camera_1', 'camera_baydoor_path'], duration=20,
            start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', flags='POSITION',
            param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]}, pcurve_period=-1000)
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['automarker_Camera_1_focus', 'marker_baydoor_path'],
            duration=12, start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS',
            flags='POSITION', param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]},
            pcurve_period=-1000)
        t += 5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='lapa', target_name='automarker_Marker_Lapa',
            duration=0.001, smooth=False)
        t += 1
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='BIGSHIP', anim='Sc_open baydoor', duration=15)
        open_baydoor.start(group=MAIN, time_delay=t, duration=15)
        t += 6
        SourcePathEvent(root=self, group=MAIN, time_delay=t,
            targets=['automarker_Camera_1_focus', 'marker_baydoor_down_path'], duration=8, start_percent=0, stop_percent=1,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', flags='POSITION',
            param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]}, pcurve_period=-1000)
        t += 2
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['lapa', 'lapa_down'], duration=8, start_percent=0,
            stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', flags='POSITION',
            param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]}, pcurve_period=-1000)
        extend_lapa.start(group=MAIN, time_delay=t, duration=15)
        t += 6
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['Camera_1', 'camera_getting_path'], duration=15,
            start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', flags='POSITION',
            param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]}, pcurve_period=-1000)
        t += 2
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['automarker_Camera_1_focus', 'marker_getting_path'],
            duration=15, start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS',
            flags='POSITION', param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]},
            pcurve_period=-1000)
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['lapa', 'lapa_up'], duration=10, start_percent=0,
            stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', flags='POSITION',
            param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]}, pcurve_period=-1000)
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['automarker_Player_Marker', 'player_up'], duration=10,
            start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', flags='POSITION',
            param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]}, pcurve_period=-1000)
        move_lapa_back.start(group=MAIN, time_delay=t, duration=15)
        t += 6
        music_main.change_attenuation(group=MAIN, time_delay=t, duration=10, attenuation=-25)
        t += 2
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='BIGSHIP', anim='Sc_close baydoor', duration=15,
            time_scale=-1)
        close_baydoor.start(group=MAIN, time_delay=t, duration=15)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M06OmicronMajorScene
