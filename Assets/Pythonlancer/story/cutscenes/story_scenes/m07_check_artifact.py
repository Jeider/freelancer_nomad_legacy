"""m07_check_artifact: постановка для ручного редактирования.

Точки: SCENES/m07_check_artifact.blend → DUMPS/m07_check_artifact.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — смещение внутри текущего блока; facial()/append_time() двигают часы.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character,
    Light,
    LightAnimEvent,
    LookAtCamera,
    MAIN,
    MotionEvent,
    MoveEvent,
    NeckIkEvent,
    Prop,
    RotateAxisEvent,
    StaticCamera,
)
from story.cutscenes.anim import (
    Female,
    Male,
)
from story.cutscenes.source_extensions import (
    SourceAttachEvent,
    preserve_entity,
)
from story import actors


class PropPropServer00(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_server'
    SRT_GRP = 0
    USR_FLG = 0


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



class M07CheckArtifactScene(Scene):
    DUMP_FILE = 'm07_check_artifact'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        Prop_server00 = PropPropServer00(root=self, name='Prop_server00', light_group=6, init_point='Prop_server00',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(Prop_server00, userprops={'category': 'Prop'})
        Prop_server01 = PropPropServer01(root=self, name='Prop_server01', light_group=6, init_point='Prop_server01',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(Prop_server01, userprops={'category': 'Prop'})
        Prop_server03 = PropPropServer03(root=self, name='Prop_server03', light_group=6, init_point='Prop_server03',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(Prop_server03, userprops={'category': 'Prop'})
        Prop_server04 = PropPropServer04(root=self, name='Prop_server04', light_group=6, init_point='Prop_server04',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(Prop_server04, userprops={'category': 'Prop'})
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
        LIGHT_trentchars_init = Light(root=self, name='LIGHT_trentchars_init', point_name='LIGHT_trentchars_init',
            extra_name='', light_group=12, diffuse=[0.6, 0.6, 0.8], ambient=[0.2, 0.4, 0.1], direction=[-1, 0, 0],
            light_type='L_DIRECT', on=True, range=150555, cutoff=30, theta=26.999985, color=[255, 255, 255],
            attenuation=[1, 0, 0.003])
        preserve_entity(LIGHT_trentchars_init)
        LIGHT_trentchars_jabbaside = Light(root=self, name='LIGHT_trentchars_jabbaside',
            point_name='LIGHT_trentchars_jabbaside', extra_name='', light_group=12, diffuse=[0.8, 0.8, 0.9],
            ambient=[0.2, 0.3, 0.2], direction=[1, 0, 0], light_type='L_DIRECT', on=False, range=150555, cutoff=30,
            theta=26.999985, color=[255, 255, 255], attenuation=[1, 0, 0.003])
        preserve_entity(LIGHT_trentchars_jabbaside)
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
        trent = Character(root=self, actor=actors.Trent, light_group=12, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=True, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'Actor': 'Player', 'category': 'Character'})
        jabba = Character(root=self, actor=actors.Jabba, light_group=3, init_point='Char_jabba', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(jabba, template_name='jabba', userprops={'Actor': 'Jabba', 'category': 'Character'})
        darcy = Character(root=self, actor=actors.Darcy, light_group=12, init_point='Char_darcy', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(darcy, template_name='darcy', userprops={'Actor': 'Darcy', 'category': 'Character'})
        cam_start = LookAtCamera(root=self, name='cam_start', fov=20, farplane=5000, look_duration=70)
        preserve_entity(cam_start)
        cam_intro = LookAtCamera(root=self, name='cam_intro', fov=15, farplane=5000, look_duration=70)
        preserve_entity(cam_intro)
        cam_roomview = LookAtCamera(root=self, name='cam_roomview', fov=25, farplane=5000, look_duration=70)
        preserve_entity(cam_roomview)
        cam_jabba_lookatdarcy = LookAtCamera(root=self, name='cam_jabba_lookatdarcy', fov=22, farplane=5000,
            look_duration=70)
        preserve_entity(cam_jabba_lookatdarcy)
        cam_jabba_check_artifact = LookAtCamera(root=self, name='cam_jabba_check_artifact', fov=22, farplane=5000,
            look_duration=70)
        preserve_entity(cam_jabba_check_artifact)
        cam_darcy_offer = LookAtCamera(root=self, name='cam_darcy_offer', fov=18, farplane=5000, look_duration=70)
        preserve_entity(cam_darcy_offer)
        cam_darcy_final = StaticCamera(root=self, name='cam_darcy_final', fov=15, farplane=5000)
        preserve_entity(cam_darcy_final)
        cam_jabba_affirmative = StaticCamera(root=self, name='cam_jabba_affirmative', fov=22, farplane=5000)
        preserve_entity(cam_jabba_affirmative)

        # Вход / начальная постановка.
        t = 0
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='LIGHT_trentchars_jabbaside', angle=-25,
            axis='Y_AXIS', duration=0, smooth=False)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=100, loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_monkeyking',
            anim=Male.Sc_MLBODY_STND_IDLE_BIG_000LV_xa_05, duration=0.1, loop=True)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_worm', angle=-90, axis='Z_AXIS', duration=0,
            smooth=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_worm', anim='Sc_Sc_s069x_worm_A', duration=10,
            time_scale=0.25)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=-15, axis='Y_AXIS', duration=0,
            smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_start', target_name='automarker_cam_start_pos2',
            duration=10, smooth=True)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Prop_alien01', angle=-35, axis='Y_AXIS',
            duration=0, smooth=True)
        t += 0.01
        cam_start.set(group=MAIN, time_delay=t)
        t += 0.49
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='LIGHT_trentchars_jabbaside', angle=-15,
            axis='X_AXIS', duration=0, smooth=False)
        main_group.append_time(10)


        # Реплика 10 · trent · исходное время 10 с
        # Ничего себе. Похоже, у этого парня очень разносторонние интересы.
        # Исходное окно facial: 15 с.
        t = 0
        cam_intro.set(group=MAIN, time_delay=t)
        t += 3
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Prop_alien01', angle=-15, axis='Y_AXIS',
            duration=8, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Prop_alien01',
            target_name='automarker_point_alien01_top', duration=8, smooth=True, adjust_orient=False)
        t += 2
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WALK_TRNS_090LV_XA_02, duration=10, time_scale=0.6,
            trans_time=0.25)
        t += 4
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=30, axis='Y_AXIS', duration=0,
            smooth=True)
        t += 1
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='LIGHT_trentchars_init', duration=0, smooth=False,
            on=False)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='LIGHT_trentchars_jabbaside', duration=0,
            smooth=False, on=True)
        cam_roomview.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_roomview',
            target_name='automarker_cam_roomview_pos2', duration=8, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_roomview_focus',
            target_name='automarker_cam_roomview_marker_pos2', duration=8, smooth=True)
        jabba.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=2.6, loop=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent',
            target_name='automarker_point_trent_offscreen', duration=0, smooth=False, adjust_orient=False)
        trent.facial(group=MAIN, index=10, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-4.5)


        # Реплика 20 · jabba · исходное время 20.5 с
        # Я интересуюсь редкими вещами, которые можно выгодно купить и еще более выгодно продать.
        # Исходное окно facial: 14 с.
        t = 0
        t += 1.5
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_jabba', angle=25, axis='Y_AXIS', duration=2,
            smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=2.6, loop=True)
        t += 0.6
        jabba.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=10)
        t += 1.4
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_darcy', target_name='automarker_point_darcy_init',
            duration=0, smooth=False, adjust_orient=False)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_darcy', angle=10, axis='Y_AXIS', duration=0,
            smooth=True)
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STROLL_000LV_XA_01, duration=3.4, loop=True)
        t += 0.6
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=10)
        t += 2.4
        cam_jabba_lookatdarcy.set(group=MAIN, time_delay=t)
        t += 0.4
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STROLL_STND_TRNS_000LV_XA_01, duration=10)
        t += 0.1
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_jabba', target_name='Char_darcy', duration=5,
            transition_duration=1, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        jabba.facial(group=MAIN, index=20, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-6.5)


        # Реплика 30 · jabba · исходное время 28 с
        # Привет, Дерси.
        # Исходное окно facial: 12 с.
        t = 0
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_worm', target_name='offscreen', duration=0,
            smooth=False)
        jabba.facial(group=MAIN, index=30, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-10)


        # Реплика 40 · darcy · исходное время 30 с
        # Привет Джабба. Я хочу, чтобы ты взглянул на одну вещицу.
        # Исходное окно facial: 5 с.
        t = 0
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_darcy_final', 'automarker_cam_darcy_final_marker'], duration=70, offset=[0, 0, 0], up='Y_AXIS',
            front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_darcy', target_name='Char_jabba', duration=5,
            transition_duration=1, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        cam_darcy_offer.set(group=MAIN, time_delay=t)
        t += 4
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHEAD_BASEPOSE_000LV_02_01, duration=5, trans_time=1)
        cam_jabba_check_artifact.set(group=MAIN, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_jabba',
            target_name='automarker_point_trent_hold_artifact_virtual', duration=6, transition_duration=1,
            target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        darcy.facial(group=MAIN, index=40, append=True, auto_lip=True, extra_delay=0)
        t = 0


        # Реплика 50 · jabba · исходное время 35 с
        # Ух ты! Весьма интересная вещица, явно инопланетного происхождения.
        # Исходное окно facial: 15 с.
        t = 0
        jabba.motion(group=MAIN, time_delay=t, anim=Male.Sc_SPCBODY_s021x_Tobias_XA_STND_RUBH_000LV_05, duration=8,
            time_scale=0.6, trans_time=1)
        t += 6
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_jabba',
            target_name='automarker_point_darcy_head_near_jabba_virtual', duration=15, transition_duration=1,
            target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        jabba.facial(group=MAIN, index=50, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-8.3)


        # Реплика 60 · jabba · исходное время 41.7 с
        # Если вы, вдруг, на мели готов дать вам за нее десять тысяч прямо сейчас.
        # Исходное окно facial: 16.3 с.
        t = 0
        t += 1.8
        jabba.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, duration=8, time_scale=0.58,
            trans_time=1)
        jabba.facial(group=MAIN, index=60, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-8.0)


        # Реплика 70 · darcy · исходное время 50 с
        # Вот дерьмо... Попила пивка в баре, нечего сказать. Ладно, Трент, уходим.
        # Исходное окно facial: 25 с.
        t = 0
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_jabba_affirmative', 'automarker_cam_jabba_affirmative_marker'], duration=70, offset=[0, 0, 0],
            up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        jabba.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, duration=5, trans_time=1)
        cam_darcy_final.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_darcy_final',
            target_name='automarker_cam_darcy_final_pos2', duration=15, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_darcy_final_marker',
            target_name='automarker_cam_darcy_final_marker_pos2', duration=15, smooth=True)
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=6)
        t += 5
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=6)
        t += 1
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_1STEP_BKWD_PVOTR_090LV_XA_05, duration=10,
            trans_time=1)
        t += 2
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_darcy', target_name='Char_jabba', duration=15,
            transition_duration=2, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        darcy.facial(group=MAIN, index=70, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-16)


        # Реплика 80 · darcy · исходное время 59 с
        # Джабба, ты же не дурак да? Ты же будешь держать язык за зубами?
        # Исходное окно facial: 25 с.
        t = 0
        t += 5
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_jabba',
            target_name='automarker_point_darcy_head_near_jabba_virtual', duration=6, transition_duration=1,
            target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        darcy.facial(group=MAIN, index=80, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-19)


        # Реплика 90 · jabba · исходное время 65 с
        # Само собой, Дерси, само собой.
        # Исходное окно facial: 12 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_darcy', target_name='automarker_offscreen_back',
            duration=0, smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', target_name='automarker_offscreen_back',
            duration=0, smooth=False)
        cam_jabba_affirmative.set(group=MAIN, time_delay=t)
        jabba.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_ATEASE_HSEC_RLEASE_000LV_XA_03, duration=10,
            time_scale=0.6)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_jabba_affirmative',
            target_name='automarker_cam_jabba_affirmative_pos2', duration=8, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_jabba_affirmative_marker',
            target_name='automarker_cam_jabba_affirmative_marker_pos2', duration=8, smooth=True)
        t += 3
        jabba.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WALK_TRNS_180LV_XA_02, duration=10, trans_time=2)
        jabba.facial(group=MAIN, index=90, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-5.0)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M07CheckArtifactScene
