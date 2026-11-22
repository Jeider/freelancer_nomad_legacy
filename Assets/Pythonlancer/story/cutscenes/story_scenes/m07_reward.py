"""m07_reward: полная постановка из master; точки в m07_reward.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character, EyeIkEvent, Female, Light, LightAnimEvent, LookAtCamera, MAIN, Male, MotionEvent, MoveEvent, NeckIkEvent, Prop, RotateAxisEvent, Sound,
)
from story.cutscenes.anim import (
    Female, Male,
)
from story import actors


class PropServer01Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_server'

class PropServer03Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_server'

class PropServer04Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_server'

class PropServer05Prop(Prop):
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

class CharAssistantActor(actors.Actor):
    NAME = 'assistant'
    TYPE = 'female'
    CUTSCENE_APPEARANCE = 'm07_female_br_officer'

class CharGunnerActor(actors.Actor):
    NAME = 'gunner'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm07_male_br_officer_gunner'

class CharDoorkeeperActor(actors.Actor):
    NAME = 'doorkeeper'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm07_male_br_officer_marksman'

class CharLeaderActor(actors.Actor):
    NAME = 'leader'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm07_male_br_officer'


class M07RewardScene(Scene):
    DUMP_FILE = 'm07_reward'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Персонажи, камеры, реквизит и звук.
        step1 = Sound(root=self, name='step1', sound='fs_fl_stone01', attenuation=-100, dmin=50, dmax=300,
            priority='Story_Sound_1')
        step2 = Sound(root=self, name='step2', sound='fs_fl_stone02', attenuation=-100, dmin=50, dmax=300,
            priority='Story_Sound_1')
        step3 = Sound(root=self, name='step3', sound='fs_fl_stone03', attenuation=-100, dmin=50, dmax=300,
            priority='Story_Sound_1')
        step4 = Sound(root=self, name='step4', sound='fs_fl_stone04', attenuation=-100, dmin=50, dmax=300,
            priority='Story_Sound_1')
        step1_cmdr = Sound(root=self, name='step1_cmdr', sound='fs_fl_stone02', attenuation=-20, dmin=50,
            dmax=300, priority='Story_Sound_1')
        step2_cmdr = Sound(root=self, name='step2_cmdr', sound='fs_fl_stone03', attenuation=-20, dmin=50,
            dmax=300, priority='Story_Sound_1')
        step3_cmdr = Sound(root=self, name='step3_cmdr', sound='fs_fl_stone04', attenuation=-20, dmin=50,
            dmax=300, priority='Story_Sound_1')
        light_barocameras_left = Light(root=self, name='LIGHT_barocameras_left',
            point_name='LIGHT_barocameras_left', extra_name='', light_group=55, hidden=False,
            rotate_from_quat=True, diffuse=[0.6, 0.6, 0.8], ambient=[0.2, 0.4, 0.1], direction=[-1, 0, 0],
            light_type='L_DIRECT', range=150555, cutoff=30, theta=26.999985, color=[255, 255, 255],
            attenuation=[1, 0, 0.003], on=True)
        light_barocameras_trentlook = Light(root=self, name='LIGHT_barocameras_trentlook',
            point_name='LIGHT_barocameras_trentlook', extra_name='', light_group=56, hidden=False,
            rotate_from_quat=True, diffuse=[0.6, 0.6, 0.8], ambient=[0.2, 0.4, 0.1], direction=[-1, 0, 0],
            light_type='L_DIRECT', range=150555, cutoff=30, theta=26.999985, color=[255, 255, 255],
            attenuation=[1, 0, 0.003], on=True)
        light_trentchars_jabbaside = Light(root=self, name='LIGHT_trentchars_jabbaside',
            point_name='LIGHT_trentchars_jabbaside', extra_name='', light_group=56, hidden=False,
            rotate_from_quat=True, diffuse=[0.5, 0.5, 0.5], ambient=[0.2, 0.2, 0.2], direction=[1, 0, 0],
            light_type='L_DIRECT', range=150555, cutoff=30, theta=26.999985, color=[255, 255, 255],
            attenuation=[1, 0, 0.003], on=False)
        light_darcy_and_girlfriend = Light(root=self, name='LIGHT_darcy_and_girlfriend',
            point_name='LIGHT_darcy_and_girlfriend', extra_name='', light_group=60, hidden=False,
            rotate_from_quat=True, diffuse=[1, 1, 1], ambient=[0.3, 0.4, 0.55], direction=[1, 0, 0],
            light_type='L_DIRECT', range=150555, cutoff=30, theta=26.999985, color=[255, 255, 255],
            attenuation=[1, 0, 0.003], on=True)
        prop_server01 = PropServer01Prop(root=self, name='Prop_server01', light_group=6,
            init_point='Prop_server01', rotate_from_quat=True, use_ambient=True)
        prop_server03 = PropServer03Prop(root=self, name='Prop_server03', light_group=6,
            init_point='Prop_server03', rotate_from_quat=True, use_ambient=True)
        prop_server04 = PropServer04Prop(root=self, name='Prop_server04', light_group=6,
            init_point='Prop_server04', rotate_from_quat=True, use_ambient=True)
        prop_server05 = PropServer05Prop(root=self, name='Prop_server05', light_group=6,
            init_point='Prop_server05', rotate_from_quat=True, use_ambient=True)
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
        trent = Character(root=self, actor=actors.Trent, name='Char_trent', light_group=56,
            init_point='Char_trent', rotate_from_quat=True, use_ambient=True, appearance='trent',
            actor_name='Player')
        jabba = Character(root=self, actor=actors.Jabba, name='Char_jabba', light_group=55,
            init_point='Char_jabba', rotate_from_quat=True, use_ambient=True, appearance='jabba',
            actor_name='Jabba')
        darcy = Character(root=self, actor=actors.Darcy, name='Char_darcy', light_group=60,
            init_point='Char_darcy', rotate_from_quat=True, use_ambient=True, appearance='darcy',
            actor_name='Darcy')
        assistant = Character(root=self, actor=CharAssistantActor, name='Char_assistant', light_group=60,
            init_point='Char_assistant', rotate_from_quat=True, use_ambient=True,
            appearance='m07_female_br_officer', actor_name='Assistant')
        gunner = Character(root=self, actor=CharGunnerActor, name='Char_gunner', light_group=55,
            init_point='Char_gunner', rotate_from_quat=True, appearance='m07_male_br_officer_gunner',
            actor_name='Gunner')
        doorkeeper = Character(root=self, actor=CharDoorkeeperActor, name='Char_doorkeeper', light_group=55,
            init_point='Char_doorkeeper', rotate_from_quat=True, use_ambient=True,
            appearance='m07_male_br_officer_marksman', actor_name='Doorkeeper')
        leader = Character(root=self, actor=CharLeaderActor, name='Char_leader', light_group=3,
            init_point='Char_leader', rotate_from_quat=True, use_ambient=True, appearance='m07_male_br_officer',
            actor_name='Policeleader')
        cam_start = LookAtCamera(root=self, name='cam_start', fov=20, look_duration=70)
        cam_darcy_meeting = LookAtCamera(root=self, name='cam_darcy_meeting', fov=20, look_duration=70)
        cam_darcy = LookAtCamera(root=self, name='cam_darcy', fov=15, look_duration=70)
        cam_darcy_top = LookAtCamera(root=self, name='cam_darcy_top', fov=18, look_duration=70)
        cam_darcy_official = LookAtCamera(root=self, name='cam_darcy_official', fov=13, look_duration=70)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=18, look_duration=70)

        # Исходные точки взгляда.

        # Вход.
        t = 0
        RotateAxisEvent(root=self, group=MAIN, object_name=light_trentchars_jabbaside.name, angle=-25,
            axis='Y_AXIS', duration=0, smooth=False, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=light_darcy_and_girlfriend.name, angle=25,
            axis='Y_AXIS', duration=0, smooth=False, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=monkeyking.name,
            anim=Male.Sc_MLBODY_STND_IDLE_BIG_000LV_xa_05, duration=0.1, loop=True, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=worm.name, angle=-90, axis='Z_AXIS', duration=0,
            smooth=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=worm.name, anim='Sc_Sc_s069x_worm_A', duration=12.5,
            time_scale=0.125, time_delay=t)
        jabba.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=100, loop=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=gunner.name,
            anim=Male.Sc_MLBODY_WALK_HOLD_GUN_RHAND_000LV_XB_01, duration=100, loop=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=doorkeeper.name,
            anim=Male.Sc_MLBODY_STND_HOLD_RIFLE_MILI_000LV_XA_05, duration=100, loop=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=leader.name,
            anim=Male.Sc_MLBODY_STND_LOOK_AROU_CASL_000LV_XA_08, duration=100, loop=True, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=15, axis='Y_AXIS', duration=0,
            smooth=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_HOLD_000LV_XA_02, duration=5, time_scale=0.5,
            time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name, target_name=jabba.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=9.01, transition_duration=2,
            time_delay=t)
        cam_start.move_cam(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        cam_start.move_focus(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_ATEASE_HOLD_000LV_XA_01, duration=100, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=assistant.name,
            anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05, duration=100, loop=True, time_delay=t)
        step1.change_attenuation(group=MAIN, duration=3, attenuation=-15, time_delay=t)
        step2.change_attenuation(group=MAIN, duration=3, attenuation=-15, time_delay=t)
        step3.change_attenuation(group=MAIN, duration=3, attenuation=-15, time_delay=t)
        t += 0.01
        cam_start.set(group=MAIN, time_delay=t)
        t += 0.19
        step3.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.3
        RotateAxisEvent(root=self, group=MAIN, object_name=light_trentchars_jabbaside.name, angle=-15,
            axis='X_AXIS', duration=0, smooth=False, time_delay=t)
        t += 0.2
        step1.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.7
        step2.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.7
        step3.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.7
        step2.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.7
        step1.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.7
        step3.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.5
        step4.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.6
        step2.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.6
        step3.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.7
        step1.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.7
        step3.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.7
        step2.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        step1.change_attenuation(group=MAIN, duration=3, attenuation=-30, time_delay=t)
        step2.change_attenuation(group=MAIN, duration=3, attenuation=-30, time_delay=t)
        step3.change_attenuation(group=MAIN, duration=3, attenuation=-30, time_delay=t)
        t += 0.7
        step3.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.7
        step4.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.6
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=-15, axis='Y_AXIS', duration=2,
            smooth=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WALK_TRNS_090LV_XA_02, duration=5, trans_time=1,
            time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name, target_name=darcy.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=25, transition_duration=2,
            time_delay=t)
        t += 0.1
        step3.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.5
        step1.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.4
        MotionEvent(root=self, group=MAIN, object_name=assistant.name,
            anim=Female.Sc_FMBODY_STND_CONV_HNDS_CASL_000LV_xa_03, duration=100, time_delay=t)
        step3.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.2
        step1_cmdr.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.3
        step2.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.2
        step2_cmdr.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.4
        step3.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.1
        step1_cmdr.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.3
        LightAnimEvent(root=self, group=MAIN, object_name=light_barocameras_trentlook.name, duration=0,
            smooth=False, on=False, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_trentchars_jabbaside.name, duration=0,
            smooth=False, on=True, time_delay=t)
        cam_darcy_meeting.set(group=MAIN, time_delay=t)
        cam_darcy_meeting.move_cam(group=MAIN, index=2, duration=5, smooth=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=5.2, loop=True, time_delay=t)
        step3_cmdr.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.01
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=-12, axis='Y_AXIS', duration=3,
            smooth=True, time_delay=t)
        t += 0.49
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_ATEASE_RLEASE_000LV_XA_02, duration=2, time_scale=0.7,
            trans_time=1, time_delay=t)
        darcy.motion(group=MAIN, anim=Female.Sc_dx_s070x_3001_Jacobi, duration=25, time_scale=0.8,
            trans_time=0.25, time_delay=t)
        t += 1
        MotionEvent(root=self, group=MAIN, object_name=assistant.name,
            anim=Female.Sc_FMBODY_STND_CONV_HNDSDN_TRNS_000LV_XA_01, duration=100, time_scale=0.8, trans_time=1,
            time_delay=t)
        t += 1
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_POINT_RHND_000LV_A_03, duration=100, time_scale=0.8,
            trans_time=0.5, time_delay=t)
        t += 1
        MotionEvent(root=self, group=MAIN, object_name=assistant.name,
            anim=Female.Sc_FMBODY_STND_SALUT_000LV_XA_03, duration=100, trans_time=1, time_delay=t)
        t += 1
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=7, axis='Y_AXIS', duration=4,
            smooth=True, time_delay=t)
        t += 0.7
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=6.5, time_delay=t)
        t += 0.3
        LightAnimEvent(root=self, group=MAIN, object_name=light_trentchars_jabbaside.name, duration=2,
            smooth=False, diffuse=[1, 1, 1], ambient=[0.3, 0.4, 0.55], time_delay=t)
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_TURN_180LV_XA_04, duration=100, trans_time=1,
            time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=assistant.name,
            anim=Female.Sc_FMBODY_STND_WALK_TRNS_180LV_XA_02, duration=100, trans_time=1, time_delay=t)
        main_group.append_time(20)

        # m07_reward 10: Darcy.
        # Спасибо, Трент. Я понимаю что долг платежом красен, но чуть попозже, хорошо? Оказывается этот урод
        # далеко не всегда «покупал» свои вещички.
        t = 0
        NeckIkEvent(root=self, group=MAIN, char_name=darcy.name, target_name=trent.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=25, transition_duration=2,
            time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=assistant.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        cam_darcy_official.set(group=MAIN, time_delay=t)
        cam_darcy_official.move_cam(group=MAIN, index=2, duration=10, smooth=False, time_delay=t)
        cam_darcy_official.move_focus(group=MAIN, index=2, duration=10, smooth=False, time_delay=t)
        t += 2
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_CROSS_ARMS_000LV_xa_03, duration=100, time_scale=0.9,
            trans_time=1, time_delay=t)
        t += 5
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_UNCRSS_ARMS_000LV_XA_03, duration=100, time_scale=0.8,
            trans_time=1, time_delay=t)
        darcy.facial(group=MAIN, index=10, auto_lip=True, extra_delay=0)

        # m07_reward 20: Darcy.
        # С особо несговорчивыми покупателями ему помогали те самые ребятки, которых мы сожгли рядом со
        # станцией. Нам надо с этим всем разобраться...
        t = 0
        cam_darcy_top.set(group=MAIN, time_delay=t)
        cam_darcy_top.move_cam(group=MAIN, index=2, duration=17, smooth=False, time_delay=t)
        cam_darcy_top.move_focus(group=MAIN, index=2, duration=17, smooth=False, time_delay=t)
        t += 1
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=100,
            time_scale=0.6, trans_time=1, time_delay=t)
        t += 5
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=100,
            time_scale=0.4, trans_time=1, time_delay=t)
        t += 4
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_ATEASE_HSEC_RLEASE_000LV_XA_02, duration=100,
            time_scale=0.8, trans_time=1, time_delay=t)
        darcy.facial(group=MAIN, index=20, auto_lip=True, extra_delay=0)

        # m07_reward 30: Darcy.
        # Кстати, вот вам официально от правительства Бретонии за помощь. Десять тысяч.
        t = 5.5
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=10, loop=True, time_delay=t)
        darcy.facial(group=MAIN, index=30, auto_lip=True, extra_delay=0)

        # m07_reward 40: Trent.
        # Но артефакт я тебе все равно не продам.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=40, auto_lip=True, extra_delay=0)

        # m07_reward 50: Darcy.
        # Да-да. Очень смешно, Трент. До скорого.
        t = 0
        NeckIkEvent(root=self, group=MAIN, char_name=darcy.name, target_name=trent.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=5, transition_duration=2,
            time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=darcy.name, target_name=trent.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=5, transition_duration=1,
            time_delay=t)
        cam_darcy.set(group=MAIN, time_delay=t)
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_ATEASE_HSEC_RLEASE_000LV_XA_02, duration=100,
            time_scale=0.8, trans_time=1, time_delay=t)
        darcy.facial(group=MAIN, index=50, auto_lip=True, extra_delay=0)
        # Действие после исходного окна реплики.
        t = 0
        darcy.motion(group=MAIN, anim=Female.Sc_FMHEAD_MOTION_WINK_000LV_XA_, duration=25, time_scale=0.5,
            start_time=0.8, trans_time=0.2, time_delay=t)
        t += 1
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_WALK_TRNS_090LV_XA_02, duration=100, trans_time=1,
            time_delay=t)
        t += 1
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name, target_name=darcy.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=25, transition_duration=4,
            time_delay=t)
        main_group.append_time(3)

        # m07_reward 60: Trent.
        # Постарайтесь побыстрее, Дерси.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=60, auto_lip=True, extra_delay=0)
