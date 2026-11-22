"""m07_check_artifact: полная постановка из master; точки в m07_check_artifact.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character, Female, Light, LightAnimEvent, LookAtCamera, LookAtEvent, MAIN, Male, MotionEvent, MoveEvent, NeckIkEvent, Prop, RotateAxisEvent, StaticCamera,
)
from story.cutscenes.anim import (
    Female, Male,
)
from story import actors


class PropServer00Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_server'

class PropServer01Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_server'

class PropServer03Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_server'

class PropServer04Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_server'

class PropBarocamera01Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_barocamera'

class PropBarocamera03Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_barocamera'

class PropBarocamera05Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_barocamera'

class PropAlien05Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_olaf'

class PropBarocamera06Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_barocamera_tall'

class PropAlien06Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_jarjar'

class PropBarocamera07Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_barocamera_tall'

class PropAlien07Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_samus'

class PropBarocamera08Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_barocamera'

class PropAlien08Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_mole'

class PropBarocamera09Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_barocamera_tall'

class PropAlien09Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_elon'

class PropBarocamera10Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_barocamera_tall'

class CharMonkeykingActor(actors.Actor):
    NAME = 'monkeyking'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm07_monkeyking'

class PropAlien01Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_facehugger'

class CharWormActor(actors.Actor):
    NAME = 'worm'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'worm'


class M07CheckArtifactScene(Scene):
    DUMP_FILE = 'm07_check_artifact'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Персонажи, камеры, реквизит и звук.
        prop_server00 = PropServer00Prop(root=self, name='Prop_server00', light_group=6,
            init_point='Prop_server00', rotate_from_quat=True, use_ambient=True)
        prop_server01 = PropServer01Prop(root=self, name='Prop_server01', light_group=6,
            init_point='Prop_server01', rotate_from_quat=True, use_ambient=True)
        prop_server03 = PropServer03Prop(root=self, name='Prop_server03', light_group=6,
            init_point='Prop_server03', rotate_from_quat=True, use_ambient=True)
        prop_server04 = PropServer04Prop(root=self, name='Prop_server04', light_group=6,
            init_point='Prop_server04', rotate_from_quat=True, use_ambient=True)
        prop_barocamera01 = PropBarocamera01Prop(root=self, name='Prop_barocamera01', light_group=6,
            init_point='Prop_barocamera01', rotate_from_quat=True, use_ambient=True)
        prop_barocamera03 = PropBarocamera03Prop(root=self, name='Prop_barocamera03', light_group=6,
            init_point='Prop_barocamera03', rotate_from_quat=True, use_ambient=True)
        prop_barocamera05 = PropBarocamera05Prop(root=self, name='Prop_barocamera05', light_group=7,
            init_point='Prop_barocamera05', rotate_from_quat=True, use_ambient=True)
        prop_alien05 = PropAlien05Prop(root=self, name='Prop_alien05', light_group=52, init_point='Prop_alien05',
            rotate_from_quat=True, use_ambient=True)
        prop_barocamera06 = PropBarocamera06Prop(root=self, name='Prop_barocamera06', light_group=7,
            init_point='Prop_barocamera06', rotate_from_quat=True, use_ambient=True)
        prop_alien06 = PropAlien06Prop(root=self, name='Prop_alien06', light_group=51, init_point='Prop_alien06',
            rotate_from_quat=True, use_ambient=True)
        prop_barocamera07 = PropBarocamera07Prop(root=self, name='Prop_barocamera07', light_group=7,
            init_point='Prop_barocamera07', rotate_from_quat=True, use_ambient=True)
        prop_alien07 = PropAlien07Prop(root=self, name='Prop_alien07', light_group=50, init_point='Prop_alien07',
            rotate_from_quat=True, use_ambient=True)
        prop_barocamera08 = PropBarocamera08Prop(root=self, name='Prop_barocamera08', light_group=7,
            init_point='Prop_barocamera08', rotate_from_quat=True, use_ambient=True)
        prop_alien08 = PropAlien08Prop(root=self, name='Prop_alien08', light_group=55, init_point='Prop_alien08',
            rotate_from_quat=True, use_ambient=True)
        prop_barocamera09 = PropBarocamera09Prop(root=self, name='Prop_barocamera09', light_group=7,
            init_point='Prop_barocamera09', rotate_from_quat=True, use_ambient=True)
        prop_alien09 = PropAlien09Prop(root=self, name='Prop_alien09', light_group=53, init_point='Prop_alien09',
            rotate_from_quat=True, use_ambient=True)
        prop_barocamera10 = PropBarocamera10Prop(root=self, name='Prop_barocamera10', light_group=7,
            init_point='Prop_barocamera10', rotate_from_quat=True, use_ambient=True)
        monkeyking = Character(root=self, actor=CharMonkeykingActor, name='Char_monkeyking', light_group=54,
            init_point='Char_monkeyking', rotate_from_quat=True, use_ambient=True, appearance='m07_monkeyking',
            bind_actor=False)
        prop_alien01 = PropAlien01Prop(root=self, name='Prop_alien01', light_group=15, init_point='Prop_alien01',
            rotate_from_quat=True, use_ambient=True)
        worm = Character(root=self, actor=CharWormActor, name='Char_worm', light_group=5, init_point='Char_worm',
            rotate_from_quat=True, use_ambient=True, appearance='worm', bind_actor=False, floor_height=1.2)
        light_barocamera_inside01 = Light(root=self, name='LIGHT_barocamera_inside01',
            point_name='LIGHT_barocamera_inside01', extra_name='', light_group=5, hidden=False,
            rotate_from_quat=True, diffuse=[0.9, 1, 0], ambient=[1, 0.5, 0.25], direction=[0, -0.8, -0.2],
            light_type='L_DIRECT', range=150555, cutoff=30, theta=26.999985, color=[255, 255, 255],
            attenuation=[1, 0, 0.003], on=True)
        light_barocamera_inside02 = Light(root=self, name='LIGHT_barocamera_inside02',
            point_name='LIGHT_barocamera_inside02', extra_name='', light_group=15, hidden=False,
            rotate_from_quat=True, diffuse=[0.4, 0.5, 0], ambient=[0.5, 0.25, 0], direction=[0, 0, 1],
            light_type='L_DIRECT', range=150555, cutoff=30, theta=26.999985, color=[255, 255, 255],
            attenuation=[1, 0, 0.003], on=True)
        light_barocamera_objects = Light(root=self, name='LIGHT_barocamera_objects',
            point_name='LIGHT_barocamera_objects', extra_name='', light_group=6, hidden=False,
            rotate_from_quat=True, diffuse=[0.2, 0.2, 0.5], ambient=[0.3, 0.3, 0.2], direction=[0.2, 0, -0.5],
            light_type='L_DIRECT', range=150555, cutoff=30, theta=26.999985, color=[255, 255, 255],
            attenuation=[1, 0, 0.003], on=True)
        light_barocamera_objects02 = Light(root=self, name='LIGHT_barocamera_objects02',
            point_name='LIGHT_barocamera_objects02', extra_name='', light_group=7, hidden=False,
            rotate_from_quat=True, diffuse=[0.5, 0.5, 0.9], ambient=[0.9, 0.3, 0], direction=[0.2, 0, -0.5],
            light_type='L_DIRECT', range=5000, cutoff=30, theta=26.999985, color=[255, 255, 255],
            attenuation=[1, 0, 0.003], on=True, specular=[0, 1, 0])
        light_trentchars_init = Light(root=self, name='LIGHT_trentchars_init', point_name='LIGHT_trentchars_init',
            extra_name='', light_group=12, hidden=False, rotate_from_quat=True, diffuse=[0.6, 0.6, 0.8],
            ambient=[0.2, 0.4, 0.1], direction=[-1, 0, 0], light_type='L_DIRECT', range=150555, cutoff=30,
            theta=26.999985, color=[255, 255, 255], attenuation=[1, 0, 0.003], on=True)
        light_trentchars_jabbaside = Light(root=self, name='LIGHT_trentchars_jabbaside',
            point_name='LIGHT_trentchars_jabbaside', extra_name='', light_group=12, hidden=False,
            rotate_from_quat=True, diffuse=[0.8, 0.8, 0.9], ambient=[0.2, 0.3, 0.2], direction=[1, 0, 0],
            light_type='L_DIRECT', range=150555, cutoff=30, theta=26.999985, color=[255, 255, 255],
            attenuation=[1, 0, 0.003], on=False)
        light_barocamera_inside_samus = Light(root=self, name='LIGHT_barocamera_inside_samus',
            point_name='LIGHT_barocamera_inside_samus', extra_name='', light_group=50, hidden=False,
            rotate_from_quat=True, diffuse=[0.9, 1, 0], ambient=[0.8, 0.5, 0.5], direction=[-0.5, -0.5, 0],
            light_type='L_DIRECT', range=150555, cutoff=30, theta=26.999985, color=[255, 255, 255],
            attenuation=[1, 0, 0.003], on=True)
        light_barocamera_inside_jarjar = Light(root=self, name='LIGHT_barocamera_inside_jarjar',
            point_name='LIGHT_barocamera_inside_jarjar', extra_name='', light_group=51, hidden=False,
            rotate_from_quat=True, diffuse=[0.9, 1, 0], ambient=[0.8, 0.2, 0.1], direction=[1, 0, 0],
            light_type='L_DIRECT', range=150555, cutoff=30, theta=26.999985, color=[255, 255, 255],
            attenuation=[1, 0, 0.003], on=True)
        light_barocamera_inside_olaf = Light(root=self, name='LIGHT_barocamera_inside_olaf',
            point_name='LIGHT_barocamera_inside_olaf', extra_name='', light_group=52, hidden=False,
            rotate_from_quat=True, diffuse=[0.9, 1, 0], ambient=[0.5, 0.5, 0.25], direction=[0, -0.5, -0.5],
            light_type='L_DIRECT', range=150555, cutoff=30, theta=26.999985, color=[255, 255, 255],
            attenuation=[1, 0, 0.003], on=True)
        light_barocamera_inside_elon = Light(root=self, name='LIGHT_barocamera_inside_elon',
            point_name='LIGHT_barocamera_inside_elon', extra_name='', light_group=53, hidden=False,
            rotate_from_quat=True, diffuse=[0.6, 0.6, 0], ambient=[0.7, 0.5, 0.2], direction=[-1, 0, 0],
            light_type='L_DIRECT', range=150555, cutoff=30, theta=26.999985, color=[255, 255, 255],
            attenuation=[1, 0, 0.003], on=True)
        light_barocamera_inside_monkeyking = Light(root=self, name='LIGHT_barocamera_inside_monkeyking',
            point_name='LIGHT_barocamera_inside_monkeyking', extra_name='', light_group=54, hidden=False,
            rotate_from_quat=True, diffuse=[0.9, 1, 0], ambient=[0.2, 0.3, 0.6], direction=[-1, 0, 0],
            light_type='L_DIRECT', range=150555, cutoff=30, theta=26.999985, color=[255, 255, 255],
            attenuation=[1, 0, 0.003], on=True)
        trent = Character(root=self, actor=actors.Trent, name='Char_trent', light_group=12,
            init_point='Char_trent', rotate_from_quat=True, use_ambient=True, appearance='trent',
            actor_name='Player')
        jabba = Character(root=self, actor=actors.Jabba, name='Char_jabba', light_group=3,
            init_point='Char_jabba', rotate_from_quat=True, appearance='jabba', actor_name='Jabba')
        darcy = Character(root=self, actor=actors.Darcy, name='Char_darcy', light_group=12,
            init_point='Char_darcy', rotate_from_quat=True, appearance='darcy', actor_name='Darcy')
        cam_start = LookAtCamera(root=self, name='cam_start', fov=20, look_duration=70)
        cam_intro = LookAtCamera(root=self, name='cam_intro', fov=15, look_duration=70)
        cam_roomview = LookAtCamera(root=self, name='cam_roomview', fov=25, look_duration=70)
        cam_jabba_lookatdarcy = LookAtCamera(root=self, name='cam_jabba_lookatdarcy', fov=22, look_duration=70)
        cam_jabba_check_artifact = LookAtCamera(root=self, name='cam_jabba_check_artifact', fov=22,
            look_duration=70)
        cam_darcy_offer = LookAtCamera(root=self, name='cam_darcy_offer', fov=18, look_duration=70)
        cam_darcy_final = StaticCamera(root=self, name='cam_darcy_final', fov=15)
        cam_jabba_affirmative = StaticCamera(root=self, name='cam_jabba_affirmative', fov=22)

        # Исходные точки взгляда.

        # Вход.
        t = 0
        RotateAxisEvent(root=self, group=MAIN, object_name=light_trentchars_jabbaside.name, angle=-25,
            axis='Y_AXIS', duration=0, smooth=False, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=100, loop=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=monkeyking.name,
            anim=Male.Sc_MLBODY_STND_IDLE_BIG_000LV_xa_05, duration=0.1, loop=True, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=worm.name, angle=-90, axis='Z_AXIS', duration=0,
            smooth=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=worm.name, anim='Sc_Sc_s069x_worm_A', duration=10,
            time_scale=0.25, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=-15, axis='Y_AXIS', duration=0,
            smooth=True, time_delay=t)
        cam_start.move_cam(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=prop_alien01.name, angle=-35, axis='Y_AXIS',
            duration=0, smooth=True, time_delay=t)
        t += 0.01
        cam_start.set(group=MAIN, time_delay=t)
        t += 0.49
        RotateAxisEvent(root=self, group=MAIN, object_name=light_trentchars_jabbaside.name, angle=-15,
            axis='X_AXIS', duration=0, smooth=False, time_delay=t)
        main_group.append_time(10)

        # m07_check_artifact 10: Trent.
        # Ничего себе. Похоже, у этого парня очень разносторонние интересы.
        t = 0
        cam_intro.set(group=MAIN, time_delay=t)
        t += 3
        RotateAxisEvent(root=self, group=MAIN, object_name=prop_alien01.name, angle=-15, axis='Y_AXIS',
            duration=8, smooth=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=prop_alien01.name,
            target_name=self.get_automarker_name('point_alien01_top'), duration=8, smooth=True, adjust_pos=True,
            adjust_orient=False, time_delay=t)
        t += 2
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WALK_TRNS_090LV_XA_02, duration=10, time_scale=0.6,
            trans_time=0.25, time_delay=t)
        t += 4
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=30, axis='Y_AXIS', duration=0,
            smooth=True, time_delay=t)
        t += 1
        LightAnimEvent(root=self, group=MAIN, object_name=light_trentchars_init.name, duration=0, smooth=False,
            on=False, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_trentchars_jabbaside.name, duration=0,
            smooth=False, on=True, time_delay=t)
        cam_roomview.set(group=MAIN, time_delay=t)
        cam_roomview.move_cam(group=MAIN, index=2, duration=8, smooth=True, time_delay=t)
        cam_roomview.move_focus(group=MAIN, index=2, duration=8, smooth=True, time_delay=t)
        jabba.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=2.6, loop=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('point_trent_offscreen'), duration=0, smooth=False,
            adjust_pos=True, adjust_orient=False, time_delay=t)
        trent.facial(group=MAIN, index=10, auto_lip=True, extra_delay=0)

        # m07_check_artifact 20: Jabba.
        # Я интересуюсь редкими вещами, которые можно выгодно купить и еще более выгодно продать.
        t = 1.5
        RotateAxisEvent(root=self, group=MAIN, object_name=jabba.name, angle=25, axis='Y_AXIS', duration=2,
            smooth=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=2.6, loop=True, time_delay=t)
        t += 0.6
        jabba.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=10, time_delay=t)
        t += 1.4
        MoveEvent(root=self, group=MAIN, object_name=darcy.name,
            target_name=self.get_automarker_name('point_darcy_init'), duration=0, smooth=False, adjust_pos=True,
            adjust_orient=False, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=darcy.name, angle=10, axis='Y_AXIS', duration=0,
            smooth=True, time_delay=t)
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_STROLL_000LV_XA_01, duration=3.4, loop=True, time_delay=t)
        t += 0.6
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=10, time_delay=t)
        t += 2.4
        cam_jabba_lookatdarcy.set(group=MAIN, time_delay=t)
        t += 0.4
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_STROLL_STND_TRNS_000LV_XA_01, duration=10, time_delay=t)
        t += 0.1
        NeckIkEvent(root=self, group=MAIN, char_name=jabba.name, target_name=darcy.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=5, transition_duration=1,
            time_delay=t)
        jabba.facial(group=MAIN, index=20, auto_lip=True, extra_delay=0)

        # m07_check_artifact 30: Jabba.
        # Привет, Дерси.
        t = 1
        MoveEvent(root=self, group=MAIN, object_name=worm.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        jabba.facial(group=MAIN, index=30, auto_lip=True, extra_delay=0)

        # m07_check_artifact 40: Darcy.
        # Привет Джабба. Я хочу, чтобы ты взглянул на одну вещицу.
        t = 0
        LookAtEvent(root=self, group=MAIN, point=cam_darcy_final.name,
            focus=self.get_automarker_name('cam_darcy_final_marker'), duration=70, target_type='ROOT',
            target_part='', up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=darcy.name, target_name=jabba.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=5, transition_duration=1,
            time_delay=t)
        cam_darcy_offer.set(group=MAIN, time_delay=t)
        t += 4
        darcy.motion(group=MAIN, anim=Female.Sc_FMHEAD_BASEPOSE_000LV_02_01, duration=5, trans_time=1,
            time_delay=t)
        cam_jabba_check_artifact.set(group=MAIN, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=jabba.name,
            target_name=self.get_automarker_name('point_trent_hold_artifact_virtual'), target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS', duration=6, transition_duration=1, time_delay=t)
        darcy.facial(group=MAIN, index=40, auto_lip=True, extra_delay=0)

        # m07_check_artifact 50: Jabba.
        # Ух ты! Весьма интересная вещица, явно инопланетного происхождения.
        t = 0
        jabba.motion(group=MAIN, anim=Male.Sc_SPCBODY_s021x_Tobias_XA_STND_RUBH_000LV_05, duration=8,
            time_scale=0.6, trans_time=1, time_delay=t)
        t += 6
        NeckIkEvent(root=self, group=MAIN, char_name=jabba.name,
            target_name=self.get_automarker_name('point_darcy_head_near_jabba_virtual'), target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS', duration=15, transition_duration=1, time_delay=t)
        jabba.facial(group=MAIN, index=50, auto_lip=True, extra_delay=0)

        # m07_check_artifact 60: Jabba.
        # Если вы, вдруг, на мели готов дать вам за нее десять тысяч прямо сейчас.
        t = 1.8
        jabba.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, duration=8, time_scale=0.58,
            trans_time=1, time_delay=t)
        jabba.facial(group=MAIN, index=60, auto_lip=True, extra_delay=0)

        # m07_check_artifact 70: Darcy.
        # Вот дерьмо... Попила пивка в баре, нечего сказать. Ладно, Трент, уходим.
        t = 0
        LookAtEvent(root=self, group=MAIN, point=cam_jabba_affirmative.name,
            focus=self.get_automarker_name('cam_jabba_affirmative_marker'), duration=70, target_type='ROOT',
            target_part='', up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        jabba.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, duration=5, trans_time=1,
            time_delay=t)
        cam_darcy_final.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=cam_darcy_final.name,
            target_name=self.get_automarker_name('cam_darcy_final_pos2'), duration=15, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('cam_darcy_final_marker'),
            target_name=self.get_automarker_name('cam_darcy_final_marker_pos2'), duration=15, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=6,
            time_delay=t)
        t += 5
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=6, time_delay=t)
        t += 1
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_1STEP_BKWD_PVOTR_090LV_XA_05, duration=10,
            trans_time=1, time_delay=t)
        darcy.facial(group=MAIN, index=70, auto_lip=True, extra_delay=0)
        # Действие после исходного окна реплики.
        t = 0.5
        NeckIkEvent(root=self, group=MAIN, char_name=darcy.name, target_name=jabba.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=15, transition_duration=2,
            time_delay=t)
        main_group.append_time(1.5)

        # m07_check_artifact 80: Darcy.
        # Джабба, ты же не дурак да? Ты же будешь держать язык за зубами?
        t = 5
        NeckIkEvent(root=self, group=MAIN, char_name=jabba.name,
            target_name=self.get_automarker_name('point_darcy_head_near_jabba_virtual'), target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS', duration=6, transition_duration=1, time_delay=t)
        darcy.facial(group=MAIN, index=80, auto_lip=True, extra_delay=0)

        # m07_check_artifact 90: Jabba.
        # Само собой, Дерси, само собой.
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=darcy.name,
            target_name=self.get_automarker_name('offscreen_back'), duration=0, smooth=False, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('offscreen_back'), duration=0, smooth=False, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        cam_jabba_affirmative.set(group=MAIN, time_delay=t)
        jabba.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_ATEASE_HSEC_RLEASE_000LV_XA_03, duration=10,
            time_scale=0.6, time_delay=t)
        t += 2
        MoveEvent(root=self, group=MAIN, object_name=cam_jabba_affirmative.name,
            target_name=self.get_automarker_name('cam_jabba_affirmative_pos2'), duration=8, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('cam_jabba_affirmative_marker'),
            target_name=self.get_automarker_name('cam_jabba_affirmative_marker_pos2'), duration=8, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 3
        jabba.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WALK_TRNS_180LV_XA_02, duration=10, trans_time=2,
            time_delay=t)
        jabba.facial(group=MAIN, index=90, auto_lip=True, extra_delay=0)
