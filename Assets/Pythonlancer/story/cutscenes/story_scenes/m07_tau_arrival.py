"""m07_tau_arrival: полная постановка из master; точки в m07_tau_arrival.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character, Light, LookAtCamera, MAIN, Male, MoveEvent, Prop, Sound,
)
from story.cutscenes.anim import (
    Male,
)
from story import actors


class AmbiSkydomeCloudsSnowProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'exclusion_barrier_m7'
    SRT_GRP = -100
    USR_FLG = 2

class TheCockpitProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_cockpit'

class ChairProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_pilot_chair'

class CaseProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_case'

class TransponderRootProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_transponder_root'

class TransponderCrystalsProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_transponder_crystals'


class M07TauArrivalScene(Scene):
    DUMP_FILE = 'm07_tau_arrival'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)
        from story.scripts.main.mission7 import Msn7Omega13
        m07_omega13_props = Msn7Omega13(self.props.mission)
        self.set_duration(32.0)

        # Персонажи, камеры, реквизит и звук.
        ambi_ltg11_puffs_amb = Light(root=self, name='ambi_LtG11_Puffs_Amb', point_name='ambi_LtG11_Puffs_Amb',
            extra_name='', light_group=11, hidden=False, rotate_from_quat=True, diffuse=[0, 0, 0],
            ambient=[0.5, 0.5, 0.55], direction=[0, 0, 1], light_type='L_DIRECT', range=2000, cutoff=98.999977,
            theta=90, color=[255, 255, 255], attenuation=[1, 0, 0], on=True)
        ambi_skydome_clouds_snow = AmbiSkydomeCloudsSnowProp(root=self, name='ambi_skydome_clouds_snow',
            light_group=23, init_point='ambi_skydome_clouds_snow', rotate_from_quat=True, use_ambient=True,
            use_dynamic=False, no_fog=True)
        light_cockpit_main = Light(root=self, name='LIGHT_cockpit_main', point_name='LIGHT_cockpit_main',
            extra_name='', light_group=5, hidden=False, rotate_from_quat=True, diffuse=[0.8, 0.8, 0.8],
            ambient=[0.3, 0.3, 0.3], direction=[-1, 0, 0], light_type='L_DIRECT', range=150555, cutoff=30,
            theta=26.999985, color=[255, 255, 255], attenuation=[1, 0, 0.003], on=True)
        light_trent_inner_objs = Light(root=self, name='LIGHT_trent_inner_objs',
            point_name='LIGHT_trent_inner_objs', extra_name='', light_group=6, hidden=False,
            rotate_from_quat=True, diffuse=[1, 1, 1], ambient=[0.2, 0.2, 0.2], direction=[0, -0.3, -1],
            light_type='L_DIRECT', range=150555, cutoff=30, theta=26.999985, color=[255, 255, 255],
            attenuation=[1, 0, 0.003], on=True)
        the_cockpit = TheCockpitProp(root=self, name='the_cockpit', light_group=5, init_point='the_cockpit',
            rotate_from_quat=True, use_ambient=True)
        trent = Character(root=self, actor=actors.Trent, name='Char_trent', light_group=6,
            init_point='Char_trent', rotate_from_quat=True, use_ambient=True, appearance='trent',
            actor_name='Player', floor_height=-1)
        chair = ChairProp(root=self, name='chair', light_group=6, init_point='chair', rotate_from_quat=True,
            use_ambient=True)
        case = CaseProp(root=self, name='case', light_group=5, init_point='case', rotate_from_quat=True,
            use_ambient=True)
        transponder_root = TransponderRootProp(root=self, name='transponder_root', light_group=6,
            init_point='transponder_root', rotate_from_quat=True, use_ambient=True)
        transponder_crystals = TransponderCrystalsProp(root=self, name='transponder_crystals', light_group=6,
            init_point='transponder_crystals', rotate_from_quat=True, use_ambient=True)
        cam_start = LookAtCamera(root=self, name='cam_start', fov=7, look_duration=70)
        cam_stand = LookAtCamera(root=self, name='cam_stand', fov=7, look_duration=70)
        cam_chair = LookAtCamera(root=self, name='cam_chair', fov=7, look_duration=70)
        click1 = Sound(root=self, name='click1', sound='sfx_ui_react_accept02', attenuation=-15, dmin=50,
            dmax=300, priority='Story_Sound_1')
        click2 = Sound(root=self, name='click2', sound='sfx_ui_react_data01', attenuation=-15, dmin=50, dmax=300,
            priority='Story_Sound_1')
        click3 = Sound(root=self, name='click3', sound='sfx_ui_react_data02', attenuation=-15, dmin=50, dmax=300,
            priority='Story_Sound_1')
        init_systems = Sound(root=self, name='init_systems', sound='sfx_ui_react_request01', attenuation=-10,
            dmin=50, dmax=300, priority='Story_Sound_1')
        system_error1 = Sound(root=self, name='system_error1', sound='sfx_ui_react_accept01', attenuation=-10,
            dmin=50, dmax=300, priority='Story_Sound_1')
        system_error2 = Sound(root=self, name='system_error2', sound='sfx_ui_react_denied01', attenuation=-5,
            dmin=50, dmax=300, priority='Story_Sound_1')
        system_success = Sound(root=self, name='system_success', sound='sfx_ui_react_processing01',
            attenuation=-5, dmin=50, dmax=300, priority='Story_Sound_1')
        music_main = Sound(root=self, name='music_main', sound='zone_field_ice', attenuation=-5, dmin=50,
            dmax=300, priority='Story_Sound_1')

        # Исходные точки взгляда.

        # Абсолютное время исходной сцены; часы MAIN не сдвигаются.
        t = 0
        trent.motion(group=MAIN, anim=Male.Sc_spcbody_s010x_trent_xf_prone_000up_13, duration=0.001, time_delay=t)
        music_main.start(group=MAIN, duration=60, loop=True, start_time=0, time_delay=t)
        t += 0.01
        cam_start.set(group=MAIN, time_delay=t)
        t += 0.99
        cam_start.move_cam(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        cam_start.move_focus(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        t += 2
        trent.motion(group=MAIN, anim=Male.Sc_spcbody_s010x_trent_xf_prone_000up_13, duration=25, time_scale=0.7,
            time_delay=t)
        t += 9
        trent.motion(group=MAIN, anim=Male.Sc_spcbody_s010x_trent_xf_prone_000up_13, duration=25, start_time=7,
            time_delay=t)
        cam_stand.set(group=MAIN, time_delay=t)
        cam_stand.move_cam(group=MAIN, index=2, duration=7, smooth=True, time_delay=t)
        cam_stand.move_focus(group=MAIN, index=2, duration=7, smooth=True, time_delay=t)
        t += 6
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=2.5, trans_time=1, loop=True,
            time_delay=t)
        t += 2
        music_main.change_attenuation(group=MAIN, duration=5, attenuation=-15, time_delay=t)
        t += 0.5
        cam_chair.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=chair.name,
            target_name=self.get_automarker_name('point_chair'), duration=0, smooth=False, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('point_trent_chair'), duration=0, smooth=False, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_SPCBODY_s027x_Trent_XB_CHRF_000DN_03, duration=18, time_scale=0.47,
            start_time=0.5, time_delay=t)
        t += 1
        init_systems.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 1.2
        click1.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.3
        system_error2.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.4
        click2.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.7
        click3.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.7
        click1.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.2
        system_error2.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.5
        click2.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.7
        click3.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.5
        click1.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.3
        system_error2.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.3
        click2.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.2
        trent.motion(group=MAIN, anim=Male.Sc_SPCBODY_s027x_Trent_XB_CHRF_000DN_03, duration=18, time_scale=0.5,
            start_time=1.5, trans_time=1, time_delay=t)
        t += 0.4
        click3.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.1
        system_error2.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.6
        click1.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.7
        click2.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.7
        click3.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.7
        click1.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.3
        system_success.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.4
        click2.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)

        # m07_omega13 100: Да за-пус-тись же ты, ста-ро-е ко-ры-то.
        self.add_group('voice_18', time=27)
        trent.facial(group='voice_18', index=100, auto_lip=True, extra_delay=0, append=False, props=m07_omega13_props)
