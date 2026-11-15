"""m07_tau_arrival: постановка для ручного редактирования.

Точки: SCENES/m07_tau_arrival.blend → DUMPS/m07_tau_arrival.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — смещение внутри текущего блока; facial()/append_time() двигают часы.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character,
    Light,
    LookAtCamera,
    MAIN,
    MoveEvent,
    Prop,
    Sound,
)
from story.cutscenes.anim import (
    Male,
)
from story.cutscenes.source_extensions import (
    preserve_entity,
    preserve_spatial,
)
from story import actors


class PropAmbiSkydomeCloudsSnow(Prop):
    COMPOUND_TEMPLATE_NAME = 'exclusion_barrier_m7'
    SRT_GRP = -100
    USR_FLG = 2


class PropTheCockpit(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_cockpit'
    SRT_GRP = 0
    USR_FLG = 0


class PropChair(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_pilot_chair'
    SRT_GRP = 0
    USR_FLG = 0


class PropCase(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_case'
    SRT_GRP = 0
    USR_FLG = 0


class PropTransponderRoot(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_transponder_root'
    SRT_GRP = 0
    USR_FLG = 0


class PropTransponderCrystals(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_transponder_crystals'
    SRT_GRP = 0
    USR_FLG = 0



class M07TauArrivalScene(Scene):
    DUMP_FILE = 'm07_tau_arrival'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        ambi_LtG11_Puffs_Amb = Light(root=self, name='ambi_LtG11_Puffs_Amb', point_name='ambi_LtG11_Puffs_Amb',
            extra_name='', light_group=11, diffuse=[0, 0, 0], ambient=[0.5, 0.5, 0.55], direction=[0, 0, 1],
            light_type='L_DIRECT', on=True, range=2000, cutoff=98.999977, theta=90, color=[255, 255, 255],
            attenuation=[1, 0, 0])
        preserve_entity(ambi_LtG11_Puffs_Amb)
        ambi_skydome_clouds_snow = PropAmbiSkydomeCloudsSnow(root=self, name='ambi_skydome_clouds_snow', light_group=23,
            init_point='ambi_skydome_clouds_snow', rotate_from_quat=True, use_ambient=True)
        preserve_entity(ambi_skydome_clouds_snow, flags=4, userprops={'category': 'Prop', 'NoFog': 'Y'}, usr_flg=2,
            srt_grp=-100)
        LIGHT_cockpit_main = Light(root=self, name='LIGHT_cockpit_main', point_name='LIGHT_cockpit_main', extra_name='',
            light_group=5, diffuse=[0.8, 0.8, 0.8], ambient=[0.3, 0.3, 0.3], direction=[-1, 0, 0], light_type='L_DIRECT',
            on=True, range=150555, cutoff=30, theta=26.999985, color=[255, 255, 255], attenuation=[1, 0, 0.003])
        preserve_entity(LIGHT_cockpit_main)
        LIGHT_trent_inner_objs = Light(root=self, name='LIGHT_trent_inner_objs', point_name='LIGHT_trent_inner_objs',
            extra_name='', light_group=6, diffuse=[1, 1, 1], ambient=[0.2, 0.2, 0.2], direction=[0, -0.3, -1],
            light_type='L_DIRECT', on=True, range=150555, cutoff=30, theta=26.999985, color=[255, 255, 255],
            attenuation=[1, 0, 0.003])
        preserve_entity(LIGHT_trent_inner_objs)
        the_cockpit = PropTheCockpit(root=self, name='the_cockpit', light_group=5, init_point='the_cockpit',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(the_cockpit, userprops={'category': 'Prop'})
        trent = Character(root=self, actor=actors.Trent, light_group=6, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=True, floor_height=-1)
        preserve_entity(trent, template_name='trent', userprops={'Actor': 'Player', 'category': 'Character'})
        chair = PropChair(root=self, name='chair', light_group=6, init_point='chair', rotate_from_quat=True,
            use_ambient=True)
        preserve_entity(chair, userprops={'category': 'Prop'})
        case = PropCase(root=self, name='case', light_group=5, init_point='case', rotate_from_quat=True, use_ambient=True)
        preserve_entity(case, userprops={'category': 'Prop'})
        transponder_root = PropTransponderRoot(root=self, name='transponder_root', light_group=6,
            init_point='transponder_root', rotate_from_quat=True, use_ambient=True)
        preserve_entity(transponder_root, userprops={'category': 'Prop'})
        transponder_crystals = PropTransponderCrystals(root=self, name='transponder_crystals', light_group=6,
            init_point='transponder_crystals', rotate_from_quat=True, use_ambient=True)
        preserve_entity(transponder_crystals, userprops={'category': 'Prop'})
        cam_start = LookAtCamera(root=self, name='cam_start', fov=7, farplane=5000, look_duration=70)
        preserve_entity(cam_start)
        cam_stand = LookAtCamera(root=self, name='cam_stand', fov=7, farplane=5000, look_duration=70)
        preserve_entity(cam_stand)
        cam_chair = LookAtCamera(root=self, name='cam_chair', fov=7, farplane=5000, look_duration=70)
        preserve_entity(cam_chair)
        click1 = Sound(root=self, name='click1', sound='sfx_ui_react_accept02', attenuation=-15, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(click1, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        click2 = Sound(root=self, name='click2', sound='sfx_ui_react_data01', attenuation=-15, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(click2, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        click3 = Sound(root=self, name='click3', sound='sfx_ui_react_data02', attenuation=-15, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(click3, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        init_systems = Sound(root=self, name='init_systems', sound='sfx_ui_react_request01', attenuation=-10, dmin=50,
            dmax=300, priority='Story_Sound_1')
        preserve_entity(init_systems, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        system_error1 = Sound(root=self, name='system_error1', sound='sfx_ui_react_accept01', attenuation=-10, dmin=50,
            dmax=300, priority='Story_Sound_1')
        preserve_entity(system_error1, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        system_error2 = Sound(root=self, name='system_error2', sound='sfx_ui_react_denied01', attenuation=-5, dmin=50,
            dmax=300, priority='Story_Sound_1')
        preserve_entity(system_error2, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        system_success = Sound(root=self, name='system_success', sound='sfx_ui_react_processing01', attenuation=-5, dmin=50,
            dmax=300, priority='Story_Sound_1')
        preserve_entity(system_success, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        music_main = Sound(root=self, name='music_main', sound='zone_field_ice', attenuation=-5, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(music_main, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})

        # Вход / начальная постановка.
        t = 0
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_spcbody_s010x_trent_xf_prone_000up_13, duration=0.001)
        music_main.start(group=MAIN, time_delay=t, duration=60, loop=True)
        t += 0.01
        cam_start.set(group=MAIN, time_delay=t)
        t += 0.99
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_start', target_name='automarker_cam_start_pos2',
            duration=10, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_start_focus',
            target_name='automarker_cam_start_marker_pos2', duration=10, smooth=True)
        t += 2
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_spcbody_s010x_trent_xf_prone_000up_13, duration=25,
            time_scale=0.7)
        t += 9
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_spcbody_s010x_trent_xf_prone_000up_13, duration=25, start_time=7)
        cam_stand.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_stand', target_name='automarker_cam_stand_pos2',
            duration=7, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_stand_focus',
            target_name='automarker_cam_stand_marker_pos2', duration=7, smooth=True)
        t += 6
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=2.5, loop=True, trans_time=1)
        t += 2
        music_main.change_attenuation(group=MAIN, time_delay=t, duration=5, attenuation=-15)
        t += 0.5
        cam_chair.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='chair', target_name='automarker_point_chair',
            duration=0, smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', target_name='automarker_point_trent_chair',
            duration=0, smooth=False)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_SPCBODY_s027x_Trent_XB_CHRF_000DN_03, duration=18,
            time_scale=0.47, start_time=0.5)
        t += 1.0
        init_systems.start(group=MAIN, time_delay=t, duration=5)
        t += 1.2
        click1.start(group=MAIN, time_delay=t, duration=5)
        t += 0.3
        system_error2.start(group=MAIN, time_delay=t, duration=5)
        t += 0.4
        click2.start(group=MAIN, time_delay=t, duration=5)
        t += 0.7
        click3.start(group=MAIN, time_delay=t, duration=5)
        t += 0.7
        click1.start(group=MAIN, time_delay=t, duration=5)
        t += 0.2
        system_error2.start(group=MAIN, time_delay=t, duration=5)
        t += 0.5
        click2.start(group=MAIN, time_delay=t, duration=5)
        t += 0.7
        click3.start(group=MAIN, time_delay=t, duration=5)
        t += 0.5
        click1.start(group=MAIN, time_delay=t, duration=5)
        main_group.append_time(27)


        # Реплика 100 · trent · исходное время 27 с
        # Да за-пус-тись же ты, ста-ро-е ко-ры-то.
        # Исходное окно facial: 12 с.
        t = 0
        system_error2.start(group=MAIN, time_delay=t, duration=5)
        t += 0.3
        click2.start(group=MAIN, time_delay=t, duration=5)
        t += 0.2
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_SPCBODY_s027x_Trent_XB_CHRF_000DN_03, duration=18,
            time_scale=0.5, start_time=1.5, trans_time=1)
        t += 0.4
        click3.start(group=MAIN, time_delay=t, duration=5)
        t += 0.1
        system_error2.start(group=MAIN, time_delay=t, duration=5)
        t += 0.6
        click1.start(group=MAIN, time_delay=t, duration=5)
        t += 0.7
        click2.start(group=MAIN, time_delay=t, duration=5)
        t += 0.7
        click3.start(group=MAIN, time_delay=t, duration=5)
        t += 0.7
        click1.start(group=MAIN, time_delay=t, duration=5)
        t += 0.3
        system_success.start(group=MAIN, time_delay=t, duration=5)
        t += 0.4
        click2.start(group=MAIN, time_delay=t, duration=5)
        trent.facial(group=MAIN, index=100, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-7.0)
        preserve_spatial(self.get_entity('ambi_skydome_clouds_snow'), source_basis=[[0.1, 0, 0], [0, 0.1, 0], [0, 0, 0.1]],
            reference_orientation=[1.0, -0.0, -0.0, -0.0])


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M07TauArrivalScene
