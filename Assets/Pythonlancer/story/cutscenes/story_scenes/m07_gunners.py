"""m07_gunners: постановка для ручного редактирования.

Точки: SCENES/m07_gunners.blend → DUMPS/m07_gunners.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — смещение внутри текущего блока; facial()/append_time() двигают часы.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Alchemy,
    CameraAnimEvent,
    Character,
    ConnectHardpointEvent,
    LookAtCamera,
    MAIN,
    MotionEvent,
    MoveEvent,
    NeckIkEvent,
    Prop,
    RotateAxisEvent,
    Sound,
    SoundEvent,
)
from story.cutscenes.anim import (
    Male,
    Trent,
)
from story.cutscenes.source_extensions import (
    SourceAlchemyAnimEvent,
    SourceAttachEvent,
    preserve_entity,
)
from story import actors


class ExtraCharBartenderFixture(actors.Actor):
    NAME = 'bartender_fixture'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'li_bartender_1'
    GAME_ACTOR = 'bartender'


class PropPropBarclothWaddedBart(Prop):
    COMPOUND_TEMPLATE_NAME = 'barcloth_wadded'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropGlassGreen(Prop):
    COMPOUND_TEMPLATE_NAME = 'glass_green'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropJesterGun(Prop):
    COMPOUND_TEMPLATE_NAME = 'prop_gun_laser_1'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropHammerGun(Prop):
    COMPOUND_TEMPLATE_NAME = 'gun_laser_2'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropRockfordRifle(Prop):
    COMPOUND_TEMPLATE_NAME = 'rifle'
    SRT_GRP = 0
    USR_FLG = 0


class ExtraCharPeasant(actors.Actor):
    NAME = 'peasant'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'tyler'
    GAME_ACTOR = 'Peasant'


class ExtraCharJester2(actors.Actor):
    NAME = 'jester2'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'jester'
    GAME_ACTOR = 'jester2'



class M07GunnersScene(Scene):
    DUMP_FILE = 'm07_gunners'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        # Исправлена опечатка исходного THN: floor_height==-110 → числовое -110.
        bartender_fixture = Character(root=self, actor=ExtraCharBartenderFixture, light_group=0,
            init_point='Char_bartender_fixture', rotate_from_quat=True, use_ambient=False, floor_height=-110)
        preserve_entity(bartender_fixture, template_name='li_bartender_1',
            userprops={'actor': 'bartender', 'category': 'Character'})
        music_hall_ambient = Sound(root=self, name='music_hall_ambient', sound='ambience_bar_space', attenuation=-12,
            dmin=50, dmax=300, priority='Story_Sound_1')
        preserve_entity(music_hall_ambient, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        music_bar = Sound(root=self, name='music_bar', sound='music_bar_generic03', attenuation=-5, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(music_bar, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        music_danger = Sound(root=self, name='music_danger', sound='rtc_m07_bg_mix', attenuation=-100, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(music_danger, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        music_fire_attempt = Sound(root=self, name='music_fire_attempt', sound='rtc_m07_fire_attempt', attenuation=0,
            dmin=50, dmax=300, priority='Story_Sound_1')
        preserve_entity(music_fire_attempt, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        sound_fire_rockford = Sound(root=self, name='sound_fire_rockford', sound='fire_rifle', attenuation=0, dmin=50,
            dmax=300, priority=None)
        preserve_entity(sound_fire_rockford, userprops={'category': 'Audio'})
        sound_fire_rockford2 = Sound(root=self, name='sound_fire_rockford2', sound='fire_rifle_alt', attenuation=0, dmin=50,
            dmax=300, priority=None)
        preserve_entity(sound_fire_rockford2, userprops={'category': 'Audio'})
        Prop_barcloth_wadded_Bart = PropPropBarclothWaddedBart(root=self, name='Prop_barcloth_wadded_Bart', light_group=0,
            init_point='Prop_barcloth_wadded_Bart', rotate_from_quat=True, use_ambient=True)
        preserve_entity(Prop_barcloth_wadded_Bart, userprops={'category': 'Prop'})
        Prop_glass_green = PropPropGlassGreen(root=self, name='Prop_glass_green', light_group=0,
            init_point='Prop_glass_green', rotate_from_quat=True, use_ambient=False)
        preserve_entity(Prop_glass_green, userprops={'category': 'Prop'})
        prop_jester_gun = PropPropJesterGun(root=self, name='prop_jester_gun', light_group=0, init_point='prop_jester_gun',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(prop_jester_gun, userprops={'category': 'Prop'})
        prop_hammer_gun = PropPropHammerGun(root=self, name='prop_hammer_gun', light_group=0, init_point='prop_hammer_gun',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(prop_hammer_gun, userprops={'category': 'Prop'})
        prop_rockford_rifle = PropPropRockfordRifle(root=self, name='prop_rockford_rifle', light_group=0,
            init_point='prop_rockford_rifle', rotate_from_quat=True, use_ambient=False)
        preserve_entity(prop_rockford_rifle, userprops={'category': 'Prop'})
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'Actor': 'Player', 'category': 'Character'})
        barman = Character(root=self, actor=actors.DetroitBarman, light_group=0, init_point='Char_barman',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(barman, template_name='martin', userprops={'actor': 'Barman', 'category': 'Character'})
        peasant = Character(root=self, actor=ExtraCharPeasant, light_group=0, init_point='Char_peasant',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(peasant, template_name='tyler', userprops={'actor': 'Peasant', 'category': 'Character'})
        hammer = Character(root=self, actor=actors.CadizEnemyTwo, light_group=0, init_point='Char_enemy2',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(hammer, template_name='hammer', userprops={'Actor': 'hammer', 'category': 'Character'})
        jester = Character(root=self, actor=actors.CadizEnemyOne, light_group=0, init_point='Char_enemy1',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(jester, template_name='jester', userprops={'Actor': 'jester', 'category': 'Character'})
        jester2 = Character(root=self, actor=ExtraCharJester2, light_group=0, init_point='Char_jester2',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(jester2, template_name='jester', userprops={'Actor': 'jester2', 'category': 'Character'})
        rockford = Character(root=self, actor=actors.Rockford, light_group=0, init_point='Char_rockford',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(rockford, template_name='rockford', userprops={'Actor': 'rockford', 'category': 'Character'})
        cam_start = LookAtCamera(root=self, name='cam_start', fov=30, farplane=5000, look_duration=70)
        preserve_entity(cam_start)
        cam_sit = LookAtCamera(root=self, name='cam_sit', fov=22, farplane=5000, look_duration=70)
        preserve_entity(cam_sit)
        cam_barman = LookAtCamera(root=self, name='cam_barman', fov=18, farplane=5000, look_duration=70)
        preserve_entity(cam_barman)
        cam_hammer_reveal = LookAtCamera(root=self, name='cam_hammer_reveal', fov=25, farplane=5000, look_duration=70)
        preserve_entity(cam_hammer_reveal)
        cam_jester_ready = LookAtCamera(root=self, name='cam_jester_ready', fov=25, farplane=5000, look_duration=70)
        preserve_entity(cam_jester_ready)
        cam_jester_standing = LookAtCamera(root=self, name='cam_jester_standing', fov=26, farplane=5000, look_duration=70)
        preserve_entity(cam_jester_standing)
        cam_greet = LookAtCamera(root=self, name='cam_greet', fov=25, farplane=5000, look_duration=70)
        preserve_entity(cam_greet)
        cam_hammer_anger = LookAtCamera(root=self, name='cam_hammer_anger', fov=12, farplane=5000, look_duration=70)
        preserve_entity(cam_hammer_anger)
        cam_jester_aim = LookAtCamera(root=self, name='cam_jester_aim', fov=17, farplane=5000, look_duration=70)
        preserve_entity(cam_jester_aim)
        cam_jester_fire = LookAtCamera(root=self, name='cam_jester_fire', fov=15, farplane=5000, look_duration=70)
        preserve_entity(cam_jester_fire)
        cam_trent_fire = LookAtCamera(root=self, name='cam_trent_fire', fov=18, farplane=5000, look_duration=70)
        preserve_entity(cam_trent_fire)
        cam_hammer_death = LookAtCamera(root=self, name='cam_hammer_death', fov=16, farplane=5000, look_duration=70)
        preserve_entity(cam_hammer_death)
        cam_rockford_appear = LookAtCamera(root=self, name='cam_rockford_appear', fov=11, farplane=5000, look_duration=70)
        preserve_entity(cam_rockford_appear)
        fadenegative_variable_1 = Alchemy(root=self, name='fadenegative_variable_1', particles='rtc_fadenegative_variable',
            point_name='fadenegative_variable_1', sparam=0)
        preserve_entity(fadenegative_variable_1, flags='LIT_DYNAMIC+LIT_AMBIENT')

        # Вход / начальная постановка.
        t = 0
        cam_start.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_start', target_name='automarker_cam_start_pos2',
            duration=7, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_start_focus',
            target_name='automarker_cam_start_marker_pos2', duration=7, smooth=True)
        hammer.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=15, loop=True)
        jester.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=15, loop=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=10, loop=True)
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='Prop_barcloth_wadded_Bart',
            parent_name='Char_barman', duration=35, target_hardpoint='hprightconnect_prop_barcloth_wadded',
            parent_hardpoint='hprightconnect')
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='Prop_glass_green',
            parent_name='Char_barman', duration=35, target_hardpoint='hpleftconnect_prop_glass_green',
            parent_hardpoint='hpleftconnect')
        music_hall_ambient.start(group=MAIN, time_delay=t, duration=108, loop=True)
        music_bar.start(group=MAIN, time_delay=t, duration=25, loop=True)
        t += 0.25
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=25, axis='Y_AXIS', duration=2,
            smooth=True)
        t += 3.0
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=-115, axis='Y_AXIS',
            duration=4, smooth=True)
        t += 3.75
        barman.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CLEAN_GLAS_000LV_A_26, duration=10, start_time=4)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_barman', angle=-45, axis='Y_AXIS',
            duration=1, smooth=True)
        t += 1
        cam_barman.set(group=MAIN, time_delay=t)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_peasant',
            anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=10, loop=True)
        t += 4.9
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent',
            target_name='automarker_point_trent_stand_to_sit', duration=0.001, smooth=False)
        t += 0.1
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_SITCR_TRNS_090DN_XA_07, duration=15, start_time=1)
        t += 1
        cam_hammer_reveal.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_hammer_reveal',
            target_name='automarker_cam_hammer_reveal_pos2', duration=8, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_hammer_reveal_focus',
            target_name='automarker_cam_hammer_reveal_marker_pos2', duration=8, smooth=True)
        t += 1
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=-20, axis='Y_AXIS', duration=1,
            smooth=True)
        t += 2
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=15, trans_time=1)
        t += 2
        hammer.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_GESTR_180LV_XA_03, duration=15, time_scale=0.4,
            trans_time=1)
        hammer.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_GESTR_THUMB_000LV_00, duration=0.2, start_time=2)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_TWSTS_LOOK_090LV_XA_02, duration=15, time_scale=0.8,
            trans_time=1)
        t += 1
        music_danger.start(group=MAIN, time_delay=t, duration=28, loop=True)
        music_danger.change_attenuation(group=MAIN, time_delay=t, duration=5, attenuation=-5)
        t += 2
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_TWSTS_FROM_090LV_XA_02, duration=15,
            time_scale=0.65, trans_time=1)
        t += 2
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='prop_jester_gun', parent_name='Char_enemy1',
            duration=159.45, target_hardpoint='hprightconnect_gun', parent_hardpoint='hprightconnect')
        jester.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_GUN_RGHT_000LV_XB_00, duration=0.2)
        t += 1
        cam_jester_ready.set(group=MAIN, time_delay=t)
        jester.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=15, time_scale=0.6)
        music_bar.change_attenuation(group=MAIN, time_delay=t, duration=5, attenuation=-100)
        t += 3
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='prop_hammer_gun', parent_name='Char_enemy2',
            duration=159.45, target_hardpoint='hprightconnect_gun', parent_hardpoint='hprightconnect')
        hammer.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_GUN_RGHT_000LV_XB_00, duration=0.2)
        t += 0.8
        cam_jester_standing.set(group=MAIN, time_delay=t)
        t += 0.2
        jester.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_WALK_TRNS_270LV_XA_10, duration=3.9,
            time_scale=0.8, start_time=1.5, trans_time=1)
        barman.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CLEAN_GLAS_000LV_A_26, duration=3, start_time=7)
        t += 1
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_enemy1', angle=-80, axis='Y_AXIS',
            duration=3, smooth=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_peasant',
            anim=Male.Sc_MLBODY_STND_RUN_TRNS_000LV_XD_02, duration=10, time_scale=0.68, trans_time=1)
        t += 1.5
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_peasant', angle=-45, axis='Y_AXIS',
            duration=2, smooth=True)
        t += 0.5
        barman.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CROUCHNG_IDLE_000DN_XA_03, duration=10, trans_time=2)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=10, loop=True)
        hammer.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_STNDCR_TRNS_090LV_XA_05, duration=15)
        t += 0.1
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_enemy2', angle=-90, axis='Y_AXIS',
            duration=3, smooth=True)
        t += 0.85
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_enemy1', target_name='automarker_point_jester_ask',
            duration=0, smooth=False)
        t += 0.05
        cam_greet.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_greet', target_name='automarker_cam_greet_pos2',
            duration=6, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_greet_focus',
            target_name='automarker_cam_greet_marker_pos2', duration=6, smooth=True)
        jester.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=15, time_scale=0.8,
            start_time=0.5)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_enemy1', angle=-40, axis='Y_AXIS',
            duration=2, smooth=True)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_enemy1', target_name='Char_trent', duration=23,
            transition_duration=3, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 0.3
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='Char_enemy1', duration=40,
            transition_duration=3, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        main_group.append_time(34)


        # Реплика 10 · enemy1 · исходное время 34 с
        # Здаров, земляк! Где Рокфорд?
        # Исходное окно facial: 6 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_peasant', target_name='offscreen', duration=0,
            smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_barman', target_name='offscreen', duration=0,
            smooth=False)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_enemy2', target_name='Char_trent', duration=22,
            transition_duration=3, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        jester.facial(group=MAIN, index=10, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-3)


        # Реплика 20 · trent · исходное время 37 с
        # Понятия не имею.
        # Исходное окно facial: 3.5 с.
        t = 0
        trent.facial(group=MAIN, index=20, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.5)


        # Реплика 30 · enemy2 · исходное время 39 с
        # Слыш, земеля, ты чо такой дерзкий? Тебя по-хорошему спросили, где Рокфорд?
        # Исходное окно facial: 17.5 с.
        t = 0
        cam_hammer_anger.set(group=MAIN, time_delay=t)
        t += 1
        trent.motion(group=MAIN, time_delay=t, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, duration=4.444,
            time_scale=0.9, trans_time=0.5)
        hammer.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=15,
            time_scale=0.6, trans_time=1)
        t += 3.5
        hammer.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_HOLD_000LV_XA_02, duration=15,
            time_scale=0.8, loop=True, trans_time=1)
        hammer.facial(group=MAIN, index=30, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-9.5)


        # Реплика 40 · enemy3 · исходное время 47 с
        # Сейчас наладим диалог (достаёт пушку).
        # Исходное окно facial: 6 с.
        t = 0
        cam_jester_aim.set(group=MAIN, time_delay=t)
        t += 1
        jester.motion(group=MAIN, time_delay=t, anim=Male.Sc_SPCBODY_s019b_Drake_XA_STND_000LV_13, duration=3.5,
            time_scale=0.7, trans_time=1.5)
        music_fire_attempt.start(group=MAIN, time_delay=t, duration=20)
        music_danger.change_attenuation(group=MAIN, time_delay=t, duration=3, attenuation=-100)
        jester.facial(group=MAIN, index=40, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-4)


        # Реплика 50 · enemy4 · исходное время 49 с
        # Где Рокфорд, утырок?
        # Исходное окно facial: 9.9 с.
        t = 0
        t += 2.3
        trent.motion(group=MAIN, time_delay=t, anim=Trent.Sc_MLHEAD_MOTION_EYES_OPENBG_TRENT_000LV_XA_, duration=2,
            trans_time=0.1)
        t += 0.2
        cam_trent_fire.set(group=MAIN, time_delay=t)
        CameraAnimEvent(root=self, group=MAIN, time_delay=t, camera_name='cam_trent_fire', duration=5, fov=18, smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_GEST_HNDS_WAIT_000LV_XA_03, duration=15,
            time_scale=0.3, start_time=2)
        t += 2.5
        CameraAnimEvent(root=self, group=MAIN, time_delay=t, camera_name='cam_jester_fire', duration=3, fov=17, smooth=True)
        t += 0.5
        cam_jester_fire.set(group=MAIN, time_delay=t)
        jester.motion(group=MAIN, time_delay=t, anim='Sc_SPCBODY_s019b_Drake_XB_STND_000LV_%', duration=6, loop=True)
        jester.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_MAD_COLD_000LV_XA_, duration=3, time_scale=0.6,
            start_time=0.5)
        t += 1.5
        SourceAlchemyAnimEvent(root=self, group=MAIN, time_delay=t, targets=['fadenegative_variable_1'], duration=0,
            psysprops={'sparam': 1})
        t += 0.7
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['fadenegative_variable_1', 'cam_jester_fire'],
            duration=0.308, offset=[0, 0, -0.5], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT',
            flags='POSITION+ORIENTATION+ENTITY_RELATIVE')
        fadenegative_variable_1.start(group=MAIN, time_delay=t, duration=0.307)
        SourceAlchemyAnimEvent(root=self, group=MAIN, time_delay=t, targets=['fadenegative_variable_1'], duration=0.307,
            psysprops={'sparam': 0}, param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]},
            pcurve_period=-1000)
        sound_fire_rockford.start(group=MAIN, time_delay=t, duration=20)
        t += 0.2
        jester.motion(group=MAIN, time_delay=t, anim=Male.Sc_SPCBODY_s051x_ku_guard01_XC_STND_DEATH_225DN_03, duration=5,
            time_scale=0.8, start_time=1, trans_time=1.5)
        t += 0.1
        hammer.motion(group=MAIN, time_delay=t, anim=Male.Sc_SPCBODY_s002x_Vance_XD_STND_000DN_03, duration=15,
            time_scale=1.3, trans_time=1)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_enemy2', angle=45, axis='Y_AXIS', duration=0,
            smooth=True)
        cam_hammer_death.set(group=MAIN, time_delay=t)
        t += 0.1
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_enemy2', angle=45, axis='Y_AXIS', duration=2,
            smooth=True)
        t += 0.1
        SourceAlchemyAnimEvent(root=self, group=MAIN, time_delay=t, targets=['fadenegative_variable_1'], duration=0,
            psysprops={'sparam': 1})
        t += 0.2
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_enemy1', angle=33, axis='Y_AXIS', duration=2,
            smooth=True)
        t += 0.1
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['fadenegative_variable_1', 'cam_hammer_death'],
            duration=0.508, offset=[0, 0, -0.5], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT',
            flags='POSITION+ORIENTATION+ENTITY_RELATIVE')
        fadenegative_variable_1.start(group=MAIN, time_delay=t, duration=0.507)
        SourceAlchemyAnimEvent(root=self, group=MAIN, time_delay=t, targets=['fadenegative_variable_1'], duration=0.507,
            psysprops={'sparam': 0}, param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]},
            pcurve_period=-1000)
        sound_fire_rockford2.start(group=MAIN, time_delay=t, duration=20)
        music_fire_attempt.change_attenuation(group=MAIN, time_delay=t, duration=1, attenuation=-100)
        hammer.motion(group=MAIN, time_delay=t, anim=Male.GENERIC_ANIM, duration=2, trans_time=0.15)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_rockford',
            target_name='automarker_point_rockford_aim', duration=0.001, smooth=False)
        rockford.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_GUN_RGHT_000LV_00, duration=1, time_scale=2)
        rockford.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_RIFLE_LEFT_000LV_00, duration=0.4, time_scale=2)
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='prop_rockford_rifle',
            parent_name='Char_rockford', duration=59.45, target_hardpoint='hp_male_rhand_rifle',
            parent_hardpoint='hprightconnect')
        jester.facial(group=MAIN, index=50, append=True, auto_lip=True, extra_delay=0)
        t = 0
        t += 0.1
        rockford.motion(group=MAIN, time_delay=t, anim=Male.Sc_SPCBODY_s010x_Rh_agent01_XA_STND_000LV_03, duration=0.2,
            start_time=2)
        t += 1.0
        cam_rockford_appear.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_rockford_appear',
            target_name='automarker_cam_rockford_appear_pos2', duration=4, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_rockford_appear_focus',
            target_name='automarker_cam_rockford_appear_marker_pos2', duration=4, smooth=True)
        CameraAnimEvent(root=self, group=MAIN, time_delay=t, camera_name='cam_rockford_appear', duration=4, fov=22,
            smooth=True)
        main_group.append_time(2.6)


        # Реплика 60 · rockford · исходное время 61.5 с
        # Я Рокфорд.
        # Исходное окно facial: 6 с.
        t = 0
        t += 2.0
        rockford.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01, duration=15, trans_time=1)
        rockford.facial(group=MAIN, index=60, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-3.5)


        # Реплика 65 · rockford · исходное время 64 с
        # За мной! Быстро!
        # Исходное окно facial: 0 с.
        t = 0
        voice_sound = self.lookup_single_sound(65)
        SoundEvent(root=self, group=MAIN, sound_name=voice_sound.get_nickname())
        t = 0
        t += 0.55
        rockford.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=15, loop=True)
        main_group.append_time(4.0)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M07GunnersScene
