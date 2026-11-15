"""m07_reward: постановка для ручного редактирования.

Точки: SCENES/m07_reward.blend → DUMPS/m07_reward.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — смещение внутри текущего блока; facial()/append_time() двигают часы.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character,
    EyeIkEvent,
    Light,
    LightAnimEvent,
    LookAtCamera,
    MAIN,
    MotionEvent,
    MoveEvent,
    NeckIkEvent,
    Prop,
    RotateAxisEvent,
    Sound,
)
from story.cutscenes.anim import (
    Female,
    Male,
)
from story.cutscenes.source_extensions import (
    preserve_entity,
)
from story import actors


class PropPropServer01(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_server'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropServer03(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_server'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropServer04(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_server'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropServer05(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_server'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropBarocamera01(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_barocamera'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropBarocamera03(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_barocamera'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropBarocamera05(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_barocamera'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropAlien05(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_olaf'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropBarocamera06(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_barocamera_tall'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropAlien06(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_jarjar'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropBarocamera07(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_barocamera_tall'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropAlien07(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_samus'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropBarocamera08(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_barocamera'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropAlien08(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_mole'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropBarocamera09(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_barocamera_tall'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropAlien09(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_elon'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropBarocamera10(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_barocamera_tall'
    SRT_GRP = 0
    USR_FLG = 0


class ExtraCharMonkeyking(actors.Actor):
    NAME = 'monkeyking'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm07_monkeyking'
    GAME_ACTOR = 'monkeyking'


class PropPropAlien01(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_facehugger'
    SRT_GRP = 0
    USR_FLG = 0


class ExtraCharWorm(actors.Actor):
    NAME = 'worm'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'worm'
    GAME_ACTOR = 'worm'


class ExtraCharAssistant(actors.Actor):
    NAME = 'assistant'
    TYPE = 'female'
    CUTSCENE_APPEARANCE = 'm07_female_br_officer'
    GAME_ACTOR = 'Assistant'


class ExtraCharGunner(actors.Actor):
    NAME = 'gunner'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm07_male_br_officer_gunner'
    GAME_ACTOR = 'Gunner'


class ExtraCharDoorkeeper(actors.Actor):
    NAME = 'doorkeeper'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm07_male_br_officer_marksman'
    GAME_ACTOR = 'Doorkeeper'


class ExtraCharLeader(actors.Actor):
    NAME = 'leader'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm07_male_br_officer'
    GAME_ACTOR = 'Policeleader'



class M07RewardScene(Scene):
    DUMP_FILE = 'm07_reward'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        step1 = Sound(root=self, name='step1', sound='fs_fl_stone01', attenuation=-100, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(step1, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        step2 = Sound(root=self, name='step2', sound='fs_fl_stone02', attenuation=-100, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(step2, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        step3 = Sound(root=self, name='step3', sound='fs_fl_stone03', attenuation=-100, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(step3, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        step4 = Sound(root=self, name='step4', sound='fs_fl_stone04', attenuation=-100, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(step4, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        step1_cmdr = Sound(root=self, name='step1_cmdr', sound='fs_fl_stone02', attenuation=-20, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(step1_cmdr, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        step2_cmdr = Sound(root=self, name='step2_cmdr', sound='fs_fl_stone03', attenuation=-20, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(step2_cmdr, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        step3_cmdr = Sound(root=self, name='step3_cmdr', sound='fs_fl_stone04', attenuation=-20, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(step3_cmdr, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        LIGHT_barocameras_left = Light(root=self, name='LIGHT_barocameras_left', point_name='LIGHT_barocameras_left',
            extra_name='', light_group=55, diffuse=[0.6, 0.6, 0.8], ambient=[0.2, 0.4, 0.1], direction=[-1, 0, 0],
            light_type='L_DIRECT', on=True, range=150555, cutoff=30, theta=26.999985, color=[255, 255, 255],
            attenuation=[1, 0, 0.003])
        preserve_entity(LIGHT_barocameras_left)
        LIGHT_barocameras_trentlook = Light(root=self, name='LIGHT_barocameras_trentlook',
            point_name='LIGHT_barocameras_trentlook', extra_name='', light_group=56, diffuse=[0.6, 0.6, 0.8],
            ambient=[0.2, 0.4, 0.1], direction=[-1, 0, 0], light_type='L_DIRECT', on=True, range=150555, cutoff=30,
            theta=26.999985, color=[255, 255, 255], attenuation=[1, 0, 0.003])
        preserve_entity(LIGHT_barocameras_trentlook)
        LIGHT_trentchars_jabbaside = Light(root=self, name='LIGHT_trentchars_jabbaside',
            point_name='LIGHT_trentchars_jabbaside', extra_name='', light_group=56, diffuse=[0.5, 0.5, 0.5],
            ambient=[0.2, 0.2, 0.2], direction=[1, 0, 0], light_type='L_DIRECT', on=False, range=150555, cutoff=30,
            theta=26.999985, color=[255, 255, 255], attenuation=[1, 0, 0.003])
        preserve_entity(LIGHT_trentchars_jabbaside)
        LIGHT_darcy_and_girlfriend = Light(root=self, name='LIGHT_darcy_and_girlfriend',
            point_name='LIGHT_darcy_and_girlfriend', extra_name='', light_group=60, diffuse=[1, 1, 1],
            ambient=[0.3, 0.4, 0.55], direction=[1, 0, 0], light_type='L_DIRECT', on=True, range=150555, cutoff=30,
            theta=26.999985, color=[255, 255, 255], attenuation=[1, 0, 0.003])
        preserve_entity(LIGHT_darcy_and_girlfriend)
        Prop_server01 = PropPropServer01(root=self, name='Prop_server01', light_group=6, init_point='Prop_server01',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(Prop_server01, userprops={'category': 'Prop'})
        Prop_server03 = PropPropServer03(root=self, name='Prop_server03', light_group=6, init_point='Prop_server03',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(Prop_server03, userprops={'category': 'Prop'})
        Prop_server04 = PropPropServer04(root=self, name='Prop_server04', light_group=6, init_point='Prop_server04',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(Prop_server04, userprops={'category': 'Prop'})
        Prop_server05 = PropPropServer05(root=self, name='Prop_server05', light_group=6, init_point='Prop_server05',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(Prop_server05, userprops={'category': 'Prop'})
        Prop_barocamera01 = PropPropBarocamera01(root=self, name='Prop_barocamera01', light_group=6,
            init_point='Prop_barocamera01', rotate_from_quat=True, use_ambient=True)
        preserve_entity(Prop_barocamera01, userprops={'category': 'Prop'})
        Prop_barocamera03 = PropPropBarocamera03(root=self, name='Prop_barocamera03', light_group=6,
            init_point='Prop_barocamera03', rotate_from_quat=True, use_ambient=True)
        preserve_entity(Prop_barocamera03, userprops={'category': 'Prop'})
        Prop_barocamera05 = PropPropBarocamera05(root=self, name='Prop_barocamera05', light_group=7,
            init_point='Prop_barocamera05', rotate_from_quat=True, use_ambient=True)
        preserve_entity(Prop_barocamera05, userprops={'category': 'Prop'})
        Prop_alien05 = PropPropAlien05(root=self, name='Prop_alien05', light_group=52, init_point='Prop_alien05',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(Prop_alien05, userprops={'category': 'Prop'})
        Prop_barocamera06 = PropPropBarocamera06(root=self, name='Prop_barocamera06', light_group=7,
            init_point='Prop_barocamera06', rotate_from_quat=True, use_ambient=True)
        preserve_entity(Prop_barocamera06, userprops={'category': 'Prop'})
        Prop_alien06 = PropPropAlien06(root=self, name='Prop_alien06', light_group=51, init_point='Prop_alien06',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(Prop_alien06, userprops={'category': 'Prop'})
        Prop_barocamera07 = PropPropBarocamera07(root=self, name='Prop_barocamera07', light_group=7,
            init_point='Prop_barocamera07', rotate_from_quat=True, use_ambient=True)
        preserve_entity(Prop_barocamera07, userprops={'category': 'Prop'})
        Prop_alien07 = PropPropAlien07(root=self, name='Prop_alien07', light_group=50, init_point='Prop_alien07',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(Prop_alien07, userprops={'category': 'Prop'})
        Prop_barocamera08 = PropPropBarocamera08(root=self, name='Prop_barocamera08', light_group=7,
            init_point='Prop_barocamera08', rotate_from_quat=True, use_ambient=True)
        preserve_entity(Prop_barocamera08, userprops={'category': 'Prop'})
        Prop_alien08 = PropPropAlien08(root=self, name='Prop_alien08', light_group=55, init_point='Prop_alien08',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(Prop_alien08, userprops={'category': 'Prop'})
        Prop_barocamera09 = PropPropBarocamera09(root=self, name='Prop_barocamera09', light_group=7,
            init_point='Prop_barocamera09', rotate_from_quat=True, use_ambient=True)
        preserve_entity(Prop_barocamera09, userprops={'category': 'Prop'})
        Prop_alien09 = PropPropAlien09(root=self, name='Prop_alien09', light_group=53, init_point='Prop_alien09',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(Prop_alien09, userprops={'category': 'Prop'})
        Prop_barocamera10 = PropPropBarocamera10(root=self, name='Prop_barocamera10', light_group=7,
            init_point='Prop_barocamera10', rotate_from_quat=True, use_ambient=True)
        preserve_entity(Prop_barocamera10, userprops={'category': 'Prop'})
        monkeyking = Character(root=self, actor=ExtraCharMonkeyking, light_group=54, init_point='Char_monkeyking',
            rotate_from_quat=True, use_ambient=True, floor_height=0)
        preserve_entity(monkeyking, template_name='m07_monkeyking', userprops={'category': 'Character'})
        Prop_alien01 = PropPropAlien01(root=self, name='Prop_alien01', light_group=15, init_point='Prop_alien01',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(Prop_alien01, userprops={'category': 'Prop'})
        worm = Character(root=self, actor=ExtraCharWorm, light_group=5, init_point='Char_worm', rotate_from_quat=True,
            use_ambient=True, floor_height=1.2)
        preserve_entity(worm, template_name='worm', userprops={'category': 'Character'})
        LIGHT_barocamera_inside01 = Light(root=self, name='LIGHT_barocamera_inside01',
            point_name='LIGHT_barocamera_inside01', extra_name='', light_group=5, diffuse=[0.9, 1, 0],
            ambient=[1, 0.5, 0.25], direction=[0, -0.8, -0.2], light_type='L_DIRECT', on=True, range=150555, cutoff=30,
            theta=26.999985, color=[255, 255, 255], attenuation=[1, 0, 0.003])
        preserve_entity(LIGHT_barocamera_inside01)
        LIGHT_barocamera_inside02 = Light(root=self, name='LIGHT_barocamera_inside02',
            point_name='LIGHT_barocamera_inside02', extra_name='', light_group=15, diffuse=[0.4, 0.5, 0],
            ambient=[0.5, 0.25, 0], direction=[0, 0, 1], light_type='L_DIRECT', on=True, range=150555, cutoff=30,
            theta=26.999985, color=[255, 255, 255], attenuation=[1, 0, 0.003])
        preserve_entity(LIGHT_barocamera_inside02)
        LIGHT_barocamera_objects = Light(root=self, name='LIGHT_barocamera_objects', point_name='LIGHT_barocamera_objects',
            extra_name='', light_group=6, diffuse=[0.2, 0.2, 0.5], ambient=[0.3, 0.3, 0.2], direction=[0.2, 0, -0.5],
            light_type='L_DIRECT', on=True, range=150555, cutoff=30, theta=26.999985, color=[255, 255, 255],
            attenuation=[1, 0, 0.003])
        preserve_entity(LIGHT_barocamera_objects)
        LIGHT_barocamera_objects02 = Light(root=self, name='LIGHT_barocamera_objects02',
            point_name='LIGHT_barocamera_objects02', extra_name='', light_group=7, diffuse=[0.5, 0.5, 0.9],
            ambient=[0.9, 0.3, 0], direction=[0.2, 0, -0.5], light_type='L_DIRECT', on=True, range=5000, cutoff=30,
            theta=26.999985, color=[255, 255, 255], attenuation=[1, 0, 0.003])
        preserve_entity(LIGHT_barocamera_objects02, lightprops={'specular': [0, 1, 0]})
        LIGHT_barocamera_inside_samus = Light(root=self, name='LIGHT_barocamera_inside_samus',
            point_name='LIGHT_barocamera_inside_samus', extra_name='', light_group=50, diffuse=[0.9, 1, 0],
            ambient=[0.8, 0.5, 0.5], direction=[-0.5, -0.5, 0], light_type='L_DIRECT', on=True, range=150555, cutoff=30,
            theta=26.999985, color=[255, 255, 255], attenuation=[1, 0, 0.003])
        preserve_entity(LIGHT_barocamera_inside_samus)
        LIGHT_barocamera_inside_jarjar = Light(root=self, name='LIGHT_barocamera_inside_jarjar',
            point_name='LIGHT_barocamera_inside_jarjar', extra_name='', light_group=51, diffuse=[0.9, 1, 0],
            ambient=[0.8, 0.2, 0.1], direction=[1, 0, 0], light_type='L_DIRECT', on=True, range=150555, cutoff=30,
            theta=26.999985, color=[255, 255, 255], attenuation=[1, 0, 0.003])
        preserve_entity(LIGHT_barocamera_inside_jarjar)
        LIGHT_barocamera_inside_olaf = Light(root=self, name='LIGHT_barocamera_inside_olaf',
            point_name='LIGHT_barocamera_inside_olaf', extra_name='', light_group=52, diffuse=[0.9, 1, 0],
            ambient=[0.5, 0.5, 0.25], direction=[0, -0.5, -0.5], light_type='L_DIRECT', on=True, range=150555, cutoff=30,
            theta=26.999985, color=[255, 255, 255], attenuation=[1, 0, 0.003])
        preserve_entity(LIGHT_barocamera_inside_olaf)
        LIGHT_barocamera_inside_elon = Light(root=self, name='LIGHT_barocamera_inside_elon',
            point_name='LIGHT_barocamera_inside_elon', extra_name='', light_group=53, diffuse=[0.6, 0.6, 0],
            ambient=[0.7, 0.5, 0.2], direction=[-1, 0, 0], light_type='L_DIRECT', on=True, range=150555, cutoff=30,
            theta=26.999985, color=[255, 255, 255], attenuation=[1, 0, 0.003])
        preserve_entity(LIGHT_barocamera_inside_elon)
        LIGHT_barocamera_inside_monkeyking = Light(root=self, name='LIGHT_barocamera_inside_monkeyking',
            point_name='LIGHT_barocamera_inside_monkeyking', extra_name='', light_group=54, diffuse=[0.9, 1, 0],
            ambient=[0.2, 0.3, 0.6], direction=[-1, 0, 0], light_type='L_DIRECT', on=True, range=150555, cutoff=30,
            theta=26.999985, color=[255, 255, 255], attenuation=[1, 0, 0.003])
        preserve_entity(LIGHT_barocamera_inside_monkeyking)
        trent = Character(root=self, actor=actors.Trent, light_group=56, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=True, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'Actor': 'Player', 'category': 'Character'})
        jabba = Character(root=self, actor=actors.Jabba, light_group=55, init_point='Char_jabba', rotate_from_quat=True,
            use_ambient=True, floor_height=0)
        preserve_entity(jabba, template_name='jabba', userprops={'Actor': 'Jabba', 'category': 'Character'})
        darcy = Character(root=self, actor=actors.Darcy, light_group=60, init_point='Char_darcy', rotate_from_quat=True,
            use_ambient=True, floor_height=0)
        preserve_entity(darcy, template_name='darcy', userprops={'Actor': 'Darcy', 'category': 'Character'})
        assistant = Character(root=self, actor=ExtraCharAssistant, light_group=60, init_point='Char_assistant',
            rotate_from_quat=True, use_ambient=True, floor_height=0)
        preserve_entity(assistant, template_name='m07_female_br_officer',
            userprops={'Actor': 'Assistant', 'category': 'Character'})
        gunner = Character(root=self, actor=ExtraCharGunner, light_group=55, init_point='Char_gunner',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(gunner, template_name='m07_male_br_officer_gunner',
            userprops={'Actor': 'Gunner', 'category': 'Character'})
        doorkeeper = Character(root=self, actor=ExtraCharDoorkeeper, light_group=55, init_point='Char_doorkeeper',
            rotate_from_quat=True, use_ambient=True, floor_height=0)
        preserve_entity(doorkeeper, template_name='m07_male_br_officer_marksman',
            userprops={'Actor': 'Doorkeeper', 'category': 'Character'})
        leader = Character(root=self, actor=ExtraCharLeader, light_group=3, init_point='Char_leader', rotate_from_quat=True,
            use_ambient=True, floor_height=0)
        preserve_entity(leader, template_name='m07_male_br_officer',
            userprops={'Actor': 'Policeleader', 'category': 'Character'})
        cam_start = LookAtCamera(root=self, name='cam_start', fov=20, farplane=5000, look_duration=70)
        preserve_entity(cam_start)
        cam_darcy_meeting = LookAtCamera(root=self, name='cam_darcy_meeting', fov=20, farplane=5000, look_duration=70)
        preserve_entity(cam_darcy_meeting)
        cam_darcy = LookAtCamera(root=self, name='cam_darcy', fov=15, farplane=5000, look_duration=70)
        preserve_entity(cam_darcy)
        cam_darcy_top = LookAtCamera(root=self, name='cam_darcy_top', fov=18, farplane=5000, look_duration=70)
        preserve_entity(cam_darcy_top)
        cam_darcy_official = LookAtCamera(root=self, name='cam_darcy_official', fov=13, farplane=5000, look_duration=70)
        preserve_entity(cam_darcy_official)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=18, farplane=5000, look_duration=70)
        preserve_entity(cam_trent)

        # Вход / начальная постановка.
        t = 0
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='LIGHT_trentchars_jabbaside', angle=-25,
            axis='Y_AXIS', duration=0, smooth=False)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='LIGHT_darcy_and_girlfriend', angle=25,
            axis='Y_AXIS', duration=0, smooth=False)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_monkeyking',
            anim=Male.Sc_MLBODY_STND_IDLE_BIG_000LV_xa_05, duration=0.1, loop=True)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_worm', angle=-90, axis='Z_AXIS', duration=0,
            smooth=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_worm', anim='Sc_Sc_s069x_worm_A', duration=12.5,
            time_scale=0.125)
        jabba.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=100, loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_gunner',
            anim=Male.Sc_MLBODY_WALK_HOLD_GUN_RHAND_000LV_XB_01, duration=100, loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_doorkeeper',
            anim=Male.Sc_MLBODY_STND_HOLD_RIFLE_MILI_000LV_XA_05, duration=100, loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_leader',
            anim=Male.Sc_MLBODY_STND_LOOK_AROU_CASL_000LV_XA_08, duration=100, loop=True)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=15, axis='Y_AXIS', duration=0,
            smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_HOLD_000LV_XA_02, duration=5, time_scale=0.5)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='Char_jabba', duration=9.01,
            transition_duration=2, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_start', target_name='automarker_cam_start_pos2',
            duration=10, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_start_focus',
            target_name='automarker_cam_start_marker_pos2', duration=10, smooth=True)
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_ATEASE_HOLD_000LV_XA_01, duration=100)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_assistant',
            anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05, duration=100, loop=True)
        step1.change_attenuation(group=MAIN, time_delay=t, duration=3, attenuation=-15)
        step2.change_attenuation(group=MAIN, time_delay=t, duration=3, attenuation=-15)
        step3.change_attenuation(group=MAIN, time_delay=t, duration=3, attenuation=-15)
        t += 0.01
        cam_start.set(group=MAIN, time_delay=t)
        t += 0.19
        step3.start(group=MAIN, time_delay=t, duration=5)
        t += 0.3
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='LIGHT_trentchars_jabbaside', angle=-15,
            axis='X_AXIS', duration=0, smooth=False)
        t += 0.2
        step1.start(group=MAIN, time_delay=t, duration=5)
        t += 0.7
        step2.start(group=MAIN, time_delay=t, duration=5)
        t += 0.7
        step3.start(group=MAIN, time_delay=t, duration=5)
        t += 0.7
        step2.start(group=MAIN, time_delay=t, duration=5)
        t += 0.7
        step1.start(group=MAIN, time_delay=t, duration=5)
        t += 0.7
        step3.start(group=MAIN, time_delay=t, duration=5)
        t += 0.5
        step4.start(group=MAIN, time_delay=t, duration=5)
        t += 0.6
        step2.start(group=MAIN, time_delay=t, duration=5)
        t += 0.6
        step3.start(group=MAIN, time_delay=t, duration=5)
        t += 0.7
        step1.start(group=MAIN, time_delay=t, duration=5)
        t += 0.7
        step3.start(group=MAIN, time_delay=t, duration=5)
        t += 0.7
        step2.start(group=MAIN, time_delay=t, duration=5)
        step1.change_attenuation(group=MAIN, time_delay=t, duration=3, attenuation=-30)
        step2.change_attenuation(group=MAIN, time_delay=t, duration=3, attenuation=-30)
        step3.change_attenuation(group=MAIN, time_delay=t, duration=3, attenuation=-30)
        t += 0.7
        step3.start(group=MAIN, time_delay=t, duration=5)
        t += 0.7
        step4.start(group=MAIN, time_delay=t, duration=5)
        t += 0.6
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=-15, axis='Y_AXIS', duration=2,
            smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WALK_TRNS_090LV_XA_02, duration=5, trans_time=1)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='Char_darcy', duration=25,
            transition_duration=2, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 0.1
        step3.start(group=MAIN, time_delay=t, duration=5)
        t += 0.5
        step1.start(group=MAIN, time_delay=t, duration=5)
        t += 0.4
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_assistant',
            anim=Female.Sc_FMBODY_STND_CONV_HNDS_CASL_000LV_xa_03, duration=100)
        step3.start(group=MAIN, time_delay=t, duration=5)
        t += 0.2
        step1_cmdr.start(group=MAIN, time_delay=t, duration=5)
        t += 0.3
        step2.start(group=MAIN, time_delay=t, duration=5)
        t += 0.2
        step2_cmdr.start(group=MAIN, time_delay=t, duration=5)
        t += 0.4
        step3.start(group=MAIN, time_delay=t, duration=5)
        t += 0.1
        step1_cmdr.start(group=MAIN, time_delay=t, duration=5)
        t += 0.3
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='LIGHT_barocameras_trentlook', duration=0,
            smooth=False, on=False)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='LIGHT_trentchars_jabbaside', duration=0,
            smooth=False, on=True)
        cam_darcy_meeting.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_darcy_meeting',
            target_name='automarker_cam_darcy_meeting_pos2', duration=5, smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=5.2, loop=True)
        step3_cmdr.start(group=MAIN, time_delay=t, duration=5)
        t += 0.01
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=-12, axis='Y_AXIS', duration=3,
            smooth=True)
        t += 0.49
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_ATEASE_RLEASE_000LV_XA_02, duration=2,
            time_scale=0.7, trans_time=1)
        darcy.motion(group=MAIN, time_delay=t, anim=Male.GENERIC_ANIM, duration=25, time_scale=0.8, trans_time=0.25)
        t += 1
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_assistant',
            anim=Female.Sc_FMBODY_STND_CONV_HNDSDN_TRNS_000LV_XA_01, duration=100, time_scale=0.8, trans_time=1)
        t += 1
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_POINT_RHND_000LV_A_03, duration=100,
            time_scale=0.8, trans_time=0.5)
        t += 1
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_assistant',
            anim=Female.Sc_FMBODY_STND_SALUT_000LV_XA_03, duration=100, trans_time=1)
        t += 1
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=7, axis='Y_AXIS', duration=4,
            smooth=True)
        t += 0.7
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=6.5)
        t += 0.3
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='LIGHT_trentchars_jabbaside', duration=2,
            smooth=False, diffuse=[1, 1, 1], ambient=[0.3, 0.4, 0.55])
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_TURN_180LV_XA_04, duration=100, trans_time=1)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_assistant',
            anim=Female.Sc_FMBODY_STND_WALK_TRNS_180LV_XA_02, duration=100, trans_time=1)
        main_group.append_time(20)


        # Реплика 10 · darcy · исходное время 20 с
        # Спасибо, Трент. Я понимаю что долг платежом красен, но чуть попозже, хорошо? Оказывается этот урод далеко
        # не всегда «покупал» свои вещички.
        # Исходное окно facial: 30 с.
        t = 0
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_darcy', target_name='Char_trent', duration=25,
            transition_duration=2, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_assistant', target_name='offscreen', duration=0,
            smooth=False)
        cam_darcy_official.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_darcy_official',
            target_name='automarker_cam_darcy_official_pos2', duration=10, smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_darcy_official_focus',
            target_name='automarker_cam_darcy_official_marker_pos2', duration=10, smooth=False)
        t += 2
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CROSS_ARMS_000LV_xa_03, duration=100,
            time_scale=0.9, trans_time=1)
        t += 5
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_UNCRSS_ARMS_000LV_XA_03, duration=100,
            time_scale=0.8, trans_time=1)
        darcy.facial(group=MAIN, index=10, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-20)


        # Реплика 20 · darcy · исходное время 30 с
        # С особо несговорчивыми покупателями ему помогали те самые ребятки, которых мы сожгли рядом со станцией.
        # Нам надо с этим всем разобраться...
        # Исходное окно facial: 30 с.
        t = 0
        cam_darcy_top.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_darcy_top',
            target_name='automarker_cam_darcy_top_pos2', duration=17, smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_darcy_top_focus',
            target_name='automarker_cam_darcy_top_marker_pos2', duration=17, smooth=False)
        t += 1
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=100,
            time_scale=0.6, trans_time=1)
        t += 5
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=100,
            time_scale=0.4, trans_time=1)
        t += 4
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_ATEASE_HSEC_RLEASE_000LV_XA_02, duration=100,
            time_scale=0.8, trans_time=1)
        darcy.facial(group=MAIN, index=20, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-19.5)


        # Реплика 30 · darcy · исходное время 40.5 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m07_reward_0030_darcy
        # Исходное окно facial: 25 с.
        t = 0
        t += 5.5
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=10, loop=True)
        # darcy.facial(group=MAIN, index=30, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(25.0)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-18.7)


        # Реплика 40 · trent · исходное время 46.8 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m07_reward_0040_trent
        # Исходное окно facial: 6 с.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        # trent.facial(group=MAIN, index=40, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(6.0)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.3)


        # Реплика 50 · darcy · исходное время 50.5 с
        # Я выплачу бонус за твою работу. До скорого, Трент.
        # Исходное окно facial: 25 с.
        t = 0
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_darcy', target_name='Char_trent', duration=5,
            transition_duration=2, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_darcy', target_name='Char_trent', duration=5,
            transition_duration=1, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        cam_darcy.set(group=MAIN, time_delay=t)
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_ATEASE_HSEC_RLEASE_000LV_XA_02, duration=100,
            time_scale=0.8, trans_time=1)
        t += 4.0
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHEAD_MOTION_WINK_000LV_XA_, duration=25, time_scale=0.5,
            start_time=0.8, trans_time=0.2)
        t += 1.0
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_WALK_TRNS_090LV_XA_02, duration=100, trans_time=1)
        t += 1.0
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='Char_darcy', duration=25,
            transition_duration=4, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        darcy.facial(group=MAIN, index=50, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-18.0)


        # Реплика 60 · trent · исходное время 57.5 с
        # Постарайтесь побыстрее, Дерси.
        # Исходное окно facial: 6 с.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=60, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.0)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M07RewardScene
