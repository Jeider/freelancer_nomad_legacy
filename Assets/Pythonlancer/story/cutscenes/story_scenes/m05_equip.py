"""m05_equip: постановка для ручного редактирования.

Точки: SCENES/m05_equip.blend → DUMPS/m05_equip.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — смещение внутри текущего блока; facial()/append_time() двигают часы.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character,
    ConnectHardpointEvent,
    EyeIkEvent,
    Light,
    LookAtCamera,
    MAIN,
    MotionEvent,
    MoveEvent,
    NeckIkEvent,
    Prop,
    RotateAxisEvent,
    Sound,
    StaticCamera,
)
from story.cutscenes.anim import (
    Female,
    Male,
    Trent,
)
from story.cutscenes.source_extensions import (
    SourceAttachEvent,
    preserve_entity,
)
from story import actors


class PropPropPda(Prop):
    COMPOUND_TEMPLATE_NAME = 'pda'
    SRT_GRP = 0
    USR_FLG = 0


class PropHand(Prop):
    COMPOUND_TEMPLATE_NAME = 'equip_hand1_sml'
    SRT_GRP = 0
    USR_FLG = 0


class PropPod(Prop):
    COMPOUND_TEMPLATE_NAME = 'equip_pod'
    SRT_GRP = 0
    USR_FLG = 0


class PropPoda(Prop):
    COMPOUND_TEMPLATE_NAME = 'equip_pod'
    SRT_GRP = 0
    USR_FLG = 0


class PropPodb(Prop):
    COMPOUND_TEMPLATE_NAME = 'equip_pod'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropMaglev(Prop):
    COMPOUND_TEMPLATE_NAME = 'maglev'
    SRT_GRP = 0
    USR_FLG = 0


class ExtraCharHatcher2(actors.Actor):
    NAME = 'hatcher2'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'hatcher'
    GAME_ACTOR = 'hatcher2'


class ExtraCharMedic1(actors.Actor):
    NAME = 'medic1'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'medic_3'
    GAME_ACTOR = 'medic_1'



class M05EquipScene(Scene):
    DUMP_FILE = 'm05_equip'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        ambi_additional = Light(root=self, name='ambi_additional', point_name='ambi_additional', extra_name='',
            light_group=0, diffuse=[0.92549, 0.835294, 0.92549], ambient=[0.121569, 0.121569, 0.121569],
            direction=[0, 0, 1], light_type='L_POINT', on=True, range=150, cutoff=30, theta=26.999985,
            color=[180, 180, 180], attenuation=[1, 0, 0.003])
        preserve_entity(ambi_additional)
        sound_cart_start = Sound(root=self, name='sound_cart_start', sound='equipment_cart_start', attenuation=-5, dmin=50,
            dmax=250, priority=None)
        preserve_entity(sound_cart_start, userprops={'category': 'Audio'})
        sound_cart_stop = Sound(root=self, name='sound_cart_stop', sound='equipment_cart_stop', attenuation=-5, dmin=50,
            dmax=250, priority=None)
        preserve_entity(sound_cart_stop, userprops={'category': 'Audio'})
        sound_cart_loop = Sound(root=self, name='sound_cart_loop', sound='equipment_cart_loop', attenuation=-25, dmin=50,
            dmax=250, priority=None)
        preserve_entity(sound_cart_loop, userprops={'category': 'Audio'})
        sound_syd_clang = Sound(root=self, name='sound_syd_clang', sound='sfx_syd_clang', attenuation=-10, dmin=50,
            dmax=250, priority=None)
        preserve_entity(sound_syd_clang, userprops={'category': 'Audio'})
        music_hall_ambient = Sound(root=self, name='music_hall_ambient', sound='ambience_equip_ground_larger',
            attenuation=0, dmin=50, dmax=300, priority='Story_Sound_1')
        preserve_entity(music_hall_ambient, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        music_reveal_and_exposition = Sound(root=self, name='music_reveal_and_exposition',
            sound='rtc_music_reveal_and_exposition', attenuation=-12, dmin=50, dmax=300, priority='Story_Sound_1')
        preserve_entity(music_reveal_and_exposition, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        music_anticipation_light = Sound(root=self, name='music_anticipation_light', sound='rtc_music_anticipation_light',
            attenuation=-8, dmin=50, dmax=300, priority='Story_Sound_1')
        preserve_entity(music_anticipation_light, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        music_reveal_special_mystery = Sound(root=self, name='music_reveal_special_mystery',
            sound='rtc_music_reveal_special_mystery', attenuation=-12, dmin=50, dmax=300, priority='Story_Sound_1')
        preserve_entity(music_reveal_special_mystery, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        prop_pda = PropPropPda(root=self, name='prop_pda', light_group=0, init_point='prop_pda', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(prop_pda, userprops={'category': 'Prop'})
        hand = PropHand(root=self, name='hand', light_group=0, init_point='hand', rotate_from_quat=True, use_ambient=True)
        preserve_entity(hand, userprops={'category': 'Prop'})
        pod = PropPod(root=self, name='pod', light_group=0, init_point='pod', rotate_from_quat=True, use_ambient=False)
        preserve_entity(pod, userprops={'category': 'Prop'})
        podA = PropPoda(root=self, name='podA', light_group=0, init_point='podA', rotate_from_quat=True, use_ambient=False)
        preserve_entity(podA, userprops={'category': 'Prop'})
        podB = PropPodb(root=self, name='podB', light_group=0, init_point='podB', rotate_from_quat=True, use_ambient=False)
        preserve_entity(podB, userprops={'category': 'Prop'})
        Prop_Maglev = PropPropMaglev(root=self, name='Prop_Maglev', light_group=0, init_point='Prop_Maglev',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(Prop_Maglev, userprops={'category': 'Prop'})
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'actor': 'player', 'category': 'Character'})
        hatcher = Character(root=self, actor=actors.Hatcher, light_group=0, init_point='Char_hatcher',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(hatcher, template_name='hatcher', userprops={'actor': 'hatcher', 'category': 'Character'})
        hatcher2 = Character(root=self, actor=ExtraCharHatcher2, light_group=0, init_point='Char_hatcher2',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(hatcher2, template_name='hatcher', userprops={'actor': 'hatcher2', 'category': 'Character'})
        mandrake = Character(root=self, actor=actors.Mandrake, light_group=0, init_point='Char_mandrake',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(mandrake, template_name='mandrake', userprops={'actor': 'mandrake', 'category': 'Character'})
        medic1 = Character(root=self, actor=ExtraCharMedic1, light_group=0, init_point='Char_medic1', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(medic1, template_name='medic_3', userprops={'actor': 'medic_1', 'category': 'Character'})
        cam_start = LookAtCamera(root=self, name='cam_start', fov=35, farplane=5000, look_duration=100)
        preserve_entity(cam_start)
        cam_mandrake_full = LookAtCamera(root=self, name='cam_mandrake_full', fov=25, farplane=5000, look_duration=100)
        preserve_entity(cam_mandrake_full)
        cam_mandrake = LookAtCamera(root=self, name='cam_mandrake', fov=20, farplane=5000, look_duration=100)
        preserve_entity(cam_mandrake)
        cam_mandrake_top = LookAtCamera(root=self, name='cam_mandrake_top', fov=20, farplane=5000, look_duration=100)
        preserve_entity(cam_mandrake_top)
        cam_mandrake_trentside = LookAtCamera(root=self, name='cam_mandrake_trentside', fov=20, farplane=5000,
            look_duration=100)
        preserve_entity(cam_mandrake_trentside)
        cam_hatcher_down = LookAtCamera(root=self, name='cam_hatcher_down', fov=10, farplane=5000, look_duration=100)
        preserve_entity(cam_hatcher_down)
        cam_hatcher = LookAtCamera(root=self, name='cam_hatcher', fov=16, farplane=5000, look_duration=100)
        preserve_entity(cam_hatcher)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=15, farplane=5000, look_duration=200)
        preserve_entity(cam_trent)
        cam_hatcher_descript1 = StaticCamera(root=self, name='cam_hatcher_descript1', fov=22, farplane=5000)
        preserve_entity(cam_hatcher_descript1)
        cam_hatcher_descript2 = StaticCamera(root=self, name='cam_hatcher_descript2', fov=15, farplane=5000)
        preserve_entity(cam_hatcher_descript2)
        cam_hatcher_descript3 = StaticCamera(root=self, name='cam_hatcher_descript3', fov=15, farplane=5000)
        preserve_entity(cam_hatcher_descript3)
        cam_trent_answer1 = StaticCamera(root=self, name='cam_trent_answer1', fov=14, farplane=5000)
        preserve_entity(cam_trent_answer1)
        cam_hatcher_descript4 = StaticCamera(root=self, name='cam_hatcher_descript4', fov=15, farplane=5000)
        preserve_entity(cam_hatcher_descript4)
        cam_hatcher_descript5 = StaticCamera(root=self, name='cam_hatcher_descript5', fov=25, farplane=5000)
        preserve_entity(cam_hatcher_descript5)
        cam_trent_answer2 = StaticCamera(root=self, name='cam_trent_answer2', fov=14, farplane=5000)
        preserve_entity(cam_trent_answer2)
        cam_trent_answer3 = StaticCamera(root=self, name='cam_trent_answer3', fov=14, farplane=5000)
        preserve_entity(cam_trent_answer3)
        cam_mandrake_trentwell = StaticCamera(root=self, name='cam_mandrake_trentwell', fov=16, farplane=5000)
        preserve_entity(cam_mandrake_trentwell)
        cam_hatcher_descript6 = StaticCamera(root=self, name='cam_hatcher_descript6', fov=15, farplane=5000)
        preserve_entity(cam_hatcher_descript6)
        cam_hatcher_descript7 = StaticCamera(root=self, name='cam_hatcher_descript7', fov=15, farplane=5000)
        preserve_entity(cam_hatcher_descript7)
        cam_hatcher_descript8 = StaticCamera(root=self, name='cam_hatcher_descript8', fov=20, farplane=5000)
        preserve_entity(cam_hatcher_descript8)
        cam_hatcher_descript9 = StaticCamera(root=self, name='cam_hatcher_descript9', fov=15, farplane=5000)
        preserve_entity(cam_hatcher_descript9)
        cam_hatcher_descript10 = StaticCamera(root=self, name='cam_hatcher_descript10', fov=14, farplane=5000)
        preserve_entity(cam_hatcher_descript10)
        cam_trent_answer4 = StaticCamera(root=self, name='cam_trent_answer4', fov=16, farplane=5000)
        preserve_entity(cam_trent_answer4)
        cam_hatcher_angry01 = StaticCamera(root=self, name='cam_hatcher_angry01', fov=20, farplane=5000)
        preserve_entity(cam_hatcher_angry01)
        cam_hatcher_angry02 = StaticCamera(root=self, name='cam_hatcher_angry02', fov=18, farplane=5000)
        preserve_entity(cam_hatcher_angry02)
        cam_hatcher_objective01 = StaticCamera(root=self, name='cam_hatcher_objective01', fov=16, farplane=5000)
        preserve_entity(cam_hatcher_objective01)
        cam_mandrake_objective01 = StaticCamera(root=self, name='cam_mandrake_objective01', fov=18, farplane=5000)
        preserve_entity(cam_mandrake_objective01)
        cam_mandrake_objective02 = StaticCamera(root=self, name='cam_mandrake_objective02', fov=15, farplane=5000)
        preserve_entity(cam_mandrake_objective02)
        cam_hatcher_objective02 = StaticCamera(root=self, name='cam_hatcher_objective02', fov=16, farplane=5000)
        preserve_entity(cam_hatcher_objective02)
        cam_hatcher_objective03 = StaticCamera(root=self, name='cam_hatcher_objective03', fov=16, farplane=5000)
        preserve_entity(cam_hatcher_objective03)
        cam_trent_final = StaticCamera(root=self, name='cam_trent_final', fov=16, farplane=5000)
        preserve_entity(cam_trent_final)
        cam_final = StaticCamera(root=self, name='cam_final', fov=30, farplane=5000)
        preserve_entity(cam_final)
        cam_window = LookAtCamera(root=self, name='cam_window', fov=45, farplane=5000, look_duration=1)
        preserve_entity(cam_window)

        # Вход / начальная постановка.
        t = 0
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='podA', angle=40, axis='Z_AXIS', duration=0.01,
            smooth=False)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='podB', angle=40, axis='Z_AXIS', duration=0.01,
            smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='pod', target_name='automarker_pod_move_bottom',
            duration=5, smooth=True, adjust_orient=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='hand', target_name='automarker_hand_move_bottom',
            duration=5, smooth=True, adjust_orient=False)
        mandrake.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=15, loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_medic1',
            anim=Male.Sc_MLBODY_STND_DEALR_PDA_000LV_XA_09, duration=8, time_scale=0.75, start_time=2)
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='prop_pda', parent_name='Char_medic1',
            duration=50, target_hardpoint='Hp_LHand_PDA', parent_hardpoint='HpLeftConnect')
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_XB_04, duration=55, loop=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_NEUT_LEFT_000LV_A_00, duration=5)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_NEUT_RGHT_000LV_A_00, duration=5)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STROLL_000LV_XA_01, duration=8.5, loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_hatcher2', anim=Female.Sc_FMBODY_STND_000LV_B_07,
            duration=9)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_start', target_name='automarker_cam_start_pos2',
            duration=7, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_start_focus',
            target_name='automarker_cam_start_marker_pos2', duration=7, smooth=True)
        sound_cart_loop.change_attenuation(group=MAIN, time_delay=t, duration=1, attenuation=-5)
        music_hall_ambient.start(group=MAIN, time_delay=t, duration=108, loop=True)
        t += 0.01
        cam_start.set(group=MAIN, time_delay=t)
        t += 0.29
        sound_cart_loop.start(group=MAIN, time_delay=t, duration=3.2, loop=True)
        t += 3.2
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='pod', angle=38, axis='X_AXIS', duration=1.5,
            smooth=True)
        sound_cart_stop.start(group=MAIN, time_delay=t, duration=2)
        t += 1.0
        sound_syd_clang.start(group=MAIN, time_delay=t, duration=2)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='hand', target_name='automarker_hand_move_top',
            duration=7, smooth=True, adjust_orient=False)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='Char_hatcher', duration=15,
            transition_duration=2, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        sound_cart_start.start(group=MAIN, time_delay=t, duration=2)
        t += 1
        sound_cart_loop.change_attenuation(group=MAIN, time_delay=t, duration=5, attenuation=-25)
        t += 0.3
        sound_cart_loop.start(group=MAIN, time_delay=t, duration=10, loop=True)
        t += 0.7
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_hatcher', target_name='automarker_hatcher_head_ik',
            duration=500, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_hatcher', target_name='automarker_hatcher_eye_ik',
            duration=500, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_mandrake',
            target_name='automarker_mandrake_head_ik', duration=500, transition_duration=1, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_mandrake', target_name='automarker_mandrake_eye_ik',
            duration=500, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        cam_hatcher_down.set(group=MAIN, time_delay=t)
        t += 1
        music_hall_ambient.change_attenuation(group=MAIN, time_delay=t, duration=2, attenuation=-10)
        main_group.append_time(8.5)


        # Реплика 10 · hatcher · исходное время 8.5 с
        # (слабый и радостный) Хетчер, рад тебя видеть. Вы с фрилансером оказались очень вовремя.
        # TODO: в текущем сценарии говорит Mandrake; в старой постановке — Hatcher.
        # Исходное окно facial: 3 с.
        t = 0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STROLL_STND_TRNS_000LV_XA_01, duration=9,
            time_scale=0.825)
        hatcher.facial(group=MAIN, index=10, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.0)


        # Реплика 20 · mandrake · исходное время 10.5 с
        # Профессор, простите нас, вы лишний час просидели в капсуле из-за этого идиота Тилтона
        # TODO: в текущем сценарии говорит Hatcher; в старой постановке — Mandrake.
        # Исходное окно facial: 3 с.
        t = 0
        cam_mandrake_top.set(group=MAIN, time_delay=t)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_medic1',
            anim=Male.Sc_MLBODY_STND_WALK_TRNS_270LV_XA_02, duration=12)
        t += 1.5
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_medic1', anim=Male.Sc_MLBODY_WLKG_000LV_XA_01,
            duration=55, loop=True)
        mandrake.facial(group=MAIN, index=20, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.0)


        # Реплика 30 · hatcher · исходное время 12.5 с
        # Что с Тилтоном на этот раз? Опять хочет отжать полномия у СБА и получить доступ к вашим разработкам?
        # TODO: в текущем сценарии говорит Mandrake; в старой постановке — Hatcher.
        # Исходное окно facial: 5 с.
        t = 0
        cam_hatcher_down.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=9,
            time_scale=0.9)
        t += 1.5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_HOLD_000LV_XA_01, duration=46,
            loop=True, trans_time=0.5)
        hatcher.facial(group=MAIN, index=30, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.5)


        # Реплика 40 · mandrake · исходное время 17 с
        # Чёрта с два у него это выйдет! Я этого никогда не допущу!
        # TODO: в текущем сценарии говорит Hatcher; в старой постановке — Mandrake.
        # Исходное окно facial: 9 с.
        t = 0
        cam_mandrake.set(group=MAIN, time_delay=t)
        mandrake.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_TALK_000LV_A_16, duration=10, start_time=1)
        mandrake.facial(group=MAIN, index=40, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.5)


        # Реплика 50 · hatcher · исходное время 25.5 с
        # Да, я знаю. Ты никогда не отступаешь. Но зачем тебе понадобился я?
        # TODO: в текущем сценарии говорит Mandrake; в старой постановке — Hatcher.
        # Исходное окно facial: 5 с.
        t = 0
        cam_hatcher_down.set(group=MAIN, time_delay=t)
        hatcher.facial(group=MAIN, index=50, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.0)


        # Реплика 60 · mandrake · исходное время 29.5 с
        # Мы получили секретную информацию о разработках рейнландских учёных. Они что-то делают в Сфере. И у них
        # большой прогресс.
        # TODO: в текущем сценарии говорит Hatcher; в старой постановке — Mandrake.
        # Исходное окно facial: 6.5 с.
        t = 0
        cam_mandrake.set(group=MAIN, time_delay=t)
        mandrake.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=10, loop=True)
        mandrake.facial(group=MAIN, index=60, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(0.5)


        # Реплика 70 · hatcher · исходное время 36.5 с
        # (возмущение) Как... как вы это могли допустить? Где же флот, охрана? Как?
        # TODO: в текущем сценарии говорит Mandrake; в старой постановке — Hatcher.
        # Исходное окно facial: 10 с.
        t = 0
        cam_hatcher_down.set(group=MAIN, time_delay=t)
        t += 6.5
        mandrake.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=2, loop=True)
        hatcher.facial(group=MAIN, index=70, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.5)


        # Реплика 80 · mandrake · исходное время 44 с
        # Ну... У Тилтона стали появляться союзники. Наши силы поубавились... поэтому нам нужна ваша помощь.
        # TODO: в текущем сценарии говорит Hatcher; в старой постановке — Mandrake.
        # Исходное окно facial: 12 с.
        t = 0
        cam_mandrake.set(group=MAIN, time_delay=t)
        t += 1
        mandrake.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_CONV_RHNDUP_TRNS_000LV_XA_02, duration=7,
            time_scale=0.75, trans_time=0.25)
        t += 1.5
        mandrake.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00, duration=4, time_scale=0.5,
            trans_time=0.25)
        t += 0.5
        mandrake.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_CONV_RHND_CASL_000LV_xa_04, duration=4,
            time_scale=0.75, trans_time=1)
        t += 3
        mandrake.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_CONV_RHNDDN_TRNS_000LV_XA_02, duration=4,
            time_scale=0.75, trans_time=1)
        t += 2
        mandrake.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_SHRG_SHLDRS_SMALL_000LV_XA_03, duration=7,
            time_scale=0.5, trans_time=0.25)
        t += 3
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=45, axis='Y_AXIS',
            duration=0.01, smooth=False)
        mandrake.facial(group=MAIN, index=80, append=True, auto_lip=True, extra_delay=0)
        t = 0


        # Реплика 90 · hatcher · исходное время 56 с
        # Конечно, Хетчер! Нужно действовать как можно скорее.
        # TODO: в текущем сценарии говорит Mandrake; в старой постановке — Hatcher.
        # Исходное окно facial: 4.5 с.
        t = 0
        cam_hatcher_down.set(group=MAIN, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=500, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_eye_ik',
            duration=500, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        hatcher.facial(group=MAIN, index=90, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.5)


        # Реплика 100 · trent · исходное время 60 с
        # Кхм кхм. Можно я вас перебью?
        # Исходное окно facial: 8 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_hatcher_near_mandrake_half', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_hatcher_near_mandrake', duration=1.75, smooth=True)
        cam_trent.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_GEST_HNDS_WAIT_000LV_XA_02, duration=4)
        t += 3
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_mandrake_upper', duration=3.25, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_mandrake', duration=2.5, smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_SHRG_SHLDRS_SMALL_000LV_XA_01, duration=4,
            time_scale=0.8, trans_time=0.5)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_mandrake_head_ik',
            target_name='automarker_center_point1', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_mandrake_eye_ik',
            target_name='automarker_center_point1', duration=1, smooth=True)
        t += 3
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_mandrake_head_ik',
            target_name='automarker_head_trent_lower', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_mandrake_eye_ik',
            target_name='automarker_head_trent', duration=1, smooth=True)
        cam_mandrake_trentside.set(group=MAIN, time_delay=t)
        mandrake.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_TWSTS_LOOK_090LV_XA_02, duration=8,
            time_scale=0.45, start_time=0.8)
        trent.facial(group=MAIN, index=100, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.5)


        # Реплика 110 · mandrake · исходное время 66.5 с
        # Что такое, Трент?
        # TODO: в текущем сценарии говорит Hatcher; в старой постановке — Mandrake.
        # Исходное окно facial: 3 с.
        t = 0
        mandrake.facial(group=MAIN, index=110, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(0.0)


        # Реплика 120 · trent · исходное время 69.5 с
        # У меня два вопроса. Во-первых, о чеканной монете.
        # Исходное окно facial: 15 с.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=4,
            time_scale=0.8)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_hatcher_near_mandrake_half', duration=3.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_hatcher_near_mandrake', duration=2.25, smooth=True)
        t += 3.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_trent_mandrake_half', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1, smooth=True)
        t += 0.5
        cam_hatcher.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=120, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-10.5)


        # Реплика 130 · hatcher · исходное время 74 с
        # Ах, да. Сейчас переведу деньги на твой. Счёт. А что еще?
        # Исходное окно facial: 5 с.
        t = 0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=4,
            time_scale=0.6)
        hatcher.facial(group=MAIN, index=130, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2)


        # Реплика 140 · trent · исходное время 77 с
        # Во-вторых, что-то твоя СБА не кажется такой уж мегаструктурой, если Либерти крутит её направо и налево.
        # Исходное окно facial: 15 с.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, duration=4, time_scale=0.8)
        t += 3.6
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_mandrake_upper', duration=2.5, smooth=True)
        t += 0.4
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_mandrake', duration=1.25, smooth=True)
        t += 2.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_mandrake_head_ik',
            target_name='automarker_center_point1_btm', duration=2.8, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_mandrake_eye_ik',
            target_name='automarker_center_point1_btm2', duration=1.5, smooth=True)
        cam_mandrake_trentside.set(group=MAIN, time_delay=t)
        mandrake.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_TWSTS_FROM_090LV_XA_04, duration=8,
            time_scale=0.8, start_time=0.5)
        t += 1.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_mandrake_upper', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_mandrake', duration=1, smooth=True)
        t += 0.8
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_mandrake_head_ik',
            target_name='automarker_head_hatcher_near_mandrake_half_btm', duration=2, smooth=True)
        trent.facial(group=MAIN, index=140, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-6)


        # Реплика 150 · mandrake · исходное время 86 с
        # Так, знаешь Трент, если тебе что-то не нравится, то можешь задать такой же вопрос Тилтону. Или ты хочешь,
        # чтобы я отменила тот звонок на Грифон?
        # TODO: в текущем сценарии говорит Hatcher; в старой постановке — Mandrake.
        # Исходное окно facial: 3 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_mandrake_eye_ik',
            target_name='automarker_head_hatcher_near_mandrake', duration=1, smooth=True)
        mandrake.facial(group=MAIN, index=150, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1)


        # Реплика 160 · hatcher · исходное время 88 с
        # Не стоит, я всё понял. Тогда до связи.
        # TODO: в текущем сценарии говорит Trent; в старой постановке — Hatcher.
        # Исходное окно facial: 10 с.
        t = 0
        cam_hatcher.set(group=MAIN, time_delay=t)
        cam_hatcher.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05, duration=2)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_trent_mandrake_half', duration=4, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=2.5, smooth=True)
        t += 1
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=8,
            time_scale=0.6)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_hatcher_near_mandrake_half', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_hatcher_near_mandrake', duration=1, smooth=True)
        hatcher.facial(group=MAIN, index=160, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2)


        # Реплика 170 · trent · исходное время 96 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0170_trent
        # Исходное окно facial: 10 с.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_HOLD_ARMS_CROSSED_000LV_XA_02, duration=7, loop=True)
        # trent.facial(group=MAIN, index=170, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(10)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-6.25)


        # Реплика 180 · hatcher · исходное время 99.75 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0180_hatcher
        # Исходное окно facial: 4 с.
        t = 0
        cam_hatcher.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=8,
            time_scale=0.5)
        t += 0.25
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_hatcher_descript1', 'automarker_cam_hatcher_descript1_marker'], duration=100, offset=[0, 0, 0],
            up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_hatcher_descript2', 'automarker_cam_hatcher_descript2_marker'], duration=100, offset=[0, 0, 0],
            up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_hatcher_descript3', 'automarker_cam_hatcher_descript3_marker'], duration=100, offset=[0, 0, 0],
            up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_trent_answer1', 'automarker_cam_trent_answer1_marker'], duration=100, offset=[0, 0, 0],
            up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_hatcher_descript4', 'automarker_cam_hatcher_descript4_marker'], duration=100, offset=[0, 0, 0],
            up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        music_hall_ambient.change_attenuation(group=MAIN, time_delay=t, duration=8, attenuation=-100)
        # hatcher.facial(group=MAIN, index=180, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(4.0)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.75)


        # Реплика 190 · trent · исходное время 103 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0190_trent
        # Исходное окно facial: 15 с.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, duration=7, time_scale=0.6)
        t += 2
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHEAD_BASEPOSE_000LV_02_01, duration=4, trans_time=0.2)
        t += 1.5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05, duration=1.5)
        t += 1.0
        cam_hatcher_descript1.set(group=MAIN, time_delay=t)
        # trent.facial(group=MAIN, index=190, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(15)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-10)


        # Реплика 200 · hatcher · исходное время 108 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0200_hatcher
        # Исходное окно facial: 14.5 с.
        t = 0
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_XB_04, duration=30, loop=True)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_SHRG_SHLDRS_SMALL_000LV_XA_02, duration=4,
            time_scale=0.7, trans_time=0.25)
        music_anticipation_light.start(group=MAIN, time_delay=t, duration=90, loop=True)
        t += 2
        trent.motion(group=MAIN, time_delay=t, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, duration=15, trans_time=0.2)
        t += 1
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, duration=7,
            time_scale=0.7, trans_time=0.25)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHAND_HNEUT_GESTR_CASL_000LV_00, duration=6,
            time_scale=0.8, loop=True, trans_time=0.25)
        t += 2
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_RHND_CASL_000LV_xa_03, duration=6,
            time_scale=0.75, loop=True, trans_time=1)
        t += 4
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHAND_NEUT_RGHT_000LV_A_00, duration=2, trans_time=0.25)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_hatcher_description3', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_hatcher_description3', duration=1, smooth=True)
        t += 1
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_01, duration=1,
            time_scale=0.75, trans_time=1)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_hatcher_road_left', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_hatcher_road_left', duration=2.5, smooth=True)
        t += 0.5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_WALK_TRNS_090LV_XA_02, duration=2,
            trans_time=0.5)
        # hatcher.facial(group=MAIN, index=200, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(14.5)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.5)


        # Реплика 210 · hatcher · исходное время 122 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0210_hatcher
        # Исходное окно facial: 17 с.
        t = 0
        cam_hatcher_descript2.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_hatcher_descript2',
            target_name='automarker_cam_hatcher_descript2_pos2', duration=16, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_hatcher_descript2_marker',
            target_name='automarker_cam_hatcher_descript2_marker_pos2', duration=16, smooth=True)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_WALK_STND_TRNS_000LV_XA_01, duration=2,
            time_scale=0.8, start_time=0.1)
        t += 1
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=3,
            time_scale=0.4, trans_time=0.5)
        t += 3
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_HOLD_000LV_XA_01, duration=4,
            time_scale=0.6, loop=True, trans_time=0.5)
        t += 4
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_hatcher_description3_look_left_nearest', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_hatcher_description3_look_left', duration=2.5, smooth=True)
        t += 2
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=2,
            time_scale=0.7, trans_time=0.5)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_trent', duration=4, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=2.5, smooth=True)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_TURN_180LV_XA_04, duration=4, time_scale=0.8,
            trans_time=1)
        t += 3
        cam_hatcher_descript3.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_hatcher_descript3',
            target_name='automarker_cam_hatcher_descript3_pos2', duration=16, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_hatcher_descript3_marker',
            target_name='automarker_cam_hatcher_descript3_marker_pos2', duration=16, smooth=True)
        # hatcher.facial(group=MAIN, index=210, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(17)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1)


        # Реплика 220 · hatcher · исходное время 138 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0220_hatcher
        # Исходное окно facial: 6.5 с.
        t = 0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_LHNDUP_TRNS_000LV_XA_01, duration=1.3,
            time_scale=0.75, trans_time=0.25)
        t += 1.3
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_LHND_CASL_000LV_xa_04, duration=3.7,
            time_scale=0.5, loop=True, trans_time=0.1)
        t += 3.7
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_LHNDDN_TRNS_000LV_XA_00, duration=1.5,
            time_scale=0.5, trans_time=1)
        # hatcher.facial(group=MAIN, index=220, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(6.5)  # длительность удалённой реплики
        main_group.append_time(0.0)


        # Реплика 230 · hatcher · исходное время 144.5 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0230_hatcher
        # Исходное окно facial: 10 с.
        t = 0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CROSS_ARMS_000LV_xa_03, duration=3.6,
            time_scale=0.8, trans_time=0.5)
        t += 3.6
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_HOLD_ARMS_CROSSED_000LV_XA_03, duration=1.4,
            time_scale=0.8, loop=True, trans_time=0.5)
        t += 1.4
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_UNCRSS_ARMS_000LV_XA_03, duration=8,
            time_scale=0.8, trans_time=0.5)
        t += 0.5
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_hatcher_descript5', 'automarker_cam_hatcher_descript5_marker'], duration=100, offset=[0, 0, 0],
            up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_trent_answer2', 'automarker_cam_trent_answer2_marker'], duration=100, offset=[0, 0, 0],
            up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_trent_answer3', 'automarker_cam_trent_answer3_marker'], duration=100, offset=[0, 0, 0],
            up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_mandrake_trentwell', 'automarker_cam_mandrake_trentwell_marker'], duration=100, offset=[0, 0, 0],
            up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_hatcher_descript6', 'automarker_cam_hatcher_descript6_marker'], duration=100, offset=[0, 0, 0],
            up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_hatcher_descript7', 'automarker_cam_hatcher_descript7_marker'], duration=100, offset=[0, 0, 0],
            up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_hatcher_descript8', 'automarker_cam_hatcher_descript8_marker'], duration=100, offset=[0, 0, 0],
            up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_hatcher_descript9', 'automarker_cam_hatcher_descript9_marker'], duration=100, offset=[0, 0, 0],
            up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        # hatcher.facial(group=MAIN, index=230, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(10.0)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.5)


        # Реплика 240 · trent · исходное время 154 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0240_trent
        # Исходное окно facial: 7.5 с.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_trent_answer1',
            target_name='automarker_cam_trent_answer1_pos2', duration=8.5, smooth=True)
        cam_trent_answer1.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_XB_04, duration=3, time_scale=0.8)
        t += 3
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_ATEASE_HSEC_RLEASE_000LV_XA_03, duration=4,
            time_scale=0.5, trans_time=0.5)
        t += 3
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_ATEASE_HOLD_000LV_XA_01, duration=2, time_scale=0.5,
            loop=True, trans_time=0.5)
        # trent.facial(group=MAIN, index=240, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(7.5)  # длительность удалённой реплики
        t = 0
        trent.motion(group=MAIN, time_delay=t, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, duration=2, time_scale=0.8,
            trans_time=1)
        main_group.append_time(1.0)


        # Реплика 250 · hatcher · исходное время 162.5 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0250_hatcher
        # Исходное окно facial: 10 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_hatcher_descript4',
            target_name='automarker_cam_hatcher_descript4_pos2', duration=10, smooth=True)
        cam_hatcher_descript4.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05, duration=1, time_scale=0.8,
            trans_time=0.5)
        t += 1.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, duration=7,
            time_scale=0.7, trans_time=0.25)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHAND_HNEUT_GESTR_CASL_000LV_00, duration=7,
            time_scale=0.8, loop=True, trans_time=0.25)
        t += 2.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_RHND_CASL_000LV_xa_03, duration=3,
            time_scale=0.75, loop=True, trans_time=1)
        t += 3.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_01, duration=1,
            time_scale=0.75, trans_time=1)
        # hatcher.facial(group=MAIN, index=250, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(10.0)  # длительность удалённой реплики
        main_group.append_time(0.0)


        # Реплика 260 · trent · исходное время 172.5 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0260_trent
        # Исходное окно facial: 10 с.
        t = 0
        cam_trent_answer2.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, duration=5, time_scale=0.8,
            trans_time=0.5)
        t += 2.5
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_GESTR_FIST_000LV_00, duration=4, time_scale=2,
            trans_time=0.25)
        # trent.facial(group=MAIN, index=260, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(10.0)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-7.0)


        # Реплика 270 · hatcher · исходное время 175.5 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0270_hatcher
        # Исходное окно facial: 10 с.
        t = 0
        cam_hatcher_descript5.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, duration=7,
            time_scale=0.7, trans_time=0.25)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHAND_HNEUT_GESTR_CASL_000LV_00, duration=4,
            time_scale=0.8, loop=True, trans_time=0.25)
        t += 2.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_RHND_CASL_000LV_xa_03, duration=3,
            time_scale=0.75, loop=True, trans_time=1)
        t += 3.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_01, duration=2,
            time_scale=0.75, trans_time=1)
        # hatcher.facial(group=MAIN, index=270, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(10.0)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.0)


        # Реплика 280 · hatcher · исходное время 183.5 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0280_hatcher
        # Исходное окно facial: 10 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_hatcher_descript4',
            target_name='automarker_cam_hatcher_descript4_pos3', duration=10, smooth=True)
        cam_hatcher_descript4.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=3,
            time_scale=0.9, trans_time=0.5)
        t += 2.5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_HOLD_000LV_XA_01, duration=3,
            time_scale=0.8, loop=True, trans_time=0.5)
        t += 3.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=3,
            time_scale=0.8, trans_time=0.5)
        t += 1.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_mandrake_head_ik',
            target_name='automarker_center_point2', duration=0.1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_mandrake_eye_ik',
            target_name='automarker_center_point2', duration=0.1, smooth=True)
        # hatcher.facial(group=MAIN, index=280, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(10.0)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.5)


        # Реплика 290 · trent · исходное время 193 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0290_trent
        # Исходное окно facial: 3 с.
        t = 0
        cam_trent_answer3.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, duration=5, time_scale=0.8)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_mandrake_head_ik',
            target_name='automarker_head_hatcher_description3', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_mandrake_eye_ik',
            target_name='automarker_head_hatcher_description3', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_mandrake_upper', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_mandrake', duration=1, smooth=True)
        t += 0.7
        trent.motion(group=MAIN, time_delay=t, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, duration=15, time_scale=0.5,
            trans_time=2)
        # trent.facial(group=MAIN, index=290, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(3)  # длительность удалённой реплики
        t = 0
        cam_mandrake_trentwell.set(group=MAIN, time_delay=t)
        mandrake.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_TWSTS_LOOK_270LV_XA_03, duration=3,
            time_scale=0.5, start_time=0.5)
        main_group.append_time(0.1)


        # Реплика 300 · mandrake · исходное время 196.1 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0300_mandrake
        # Исходное окно facial: 3 с.
        t = 0
        t += 0.9
        music_anticipation_light.change_attenuation(group=MAIN, time_delay=t, duration=1, attenuation=-100)
        # mandrake.facial(group=MAIN, index=300, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(3.0)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.1)


        # Реплика 310 · hatcher · исходное время 198 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0310_hatcher
        # Исходное окно facial: 10 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_hatcher_descript6',
            target_name='automarker_cam_hatcher_descript6_pos2', duration=10, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_hatcher_descript6_marker',
            target_name='automarker_cam_hatcher_descript6_marker_pos2', duration=10, smooth=True)
        cam_hatcher_descript6.set(group=MAIN, time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_trent', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1, smooth=True)
        music_reveal_and_exposition.start(group=MAIN, time_delay=t, duration=77, loop=True)
        t += 0.1
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHEAD_BASEPOSE_000LV_02_01, duration=0.4, time_scale=0.5,
            trans_time=0.4)
        t += 0.9
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_hatcher_descript10', 'automarker_cam_hatcher_descript10_marker'], duration=100, offset=[0, 0, 0],
            up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_trent_answer4', 'automarker_cam_trent_answer4_marker'], duration=100, offset=[0, 0, 0],
            up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_HNDSUP_TRNS_000LV_XA_01, duration=4,
            time_scale=0.5, trans_time=0.25)
        t += 2
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_HNDS_CASL_000LV_xa_03, duration=4,
            time_scale=0.5, loop=True, trans_time=0.5)
        t += 4
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_HNDSDN_TRNS_000LV_XA_01, duration=2,
            time_scale=0.5, trans_time=0.5)
        # hatcher.facial(group=MAIN, index=310, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(10)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.5)


        # Реплика 320 · hatcher · исходное время 207.5 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0320_hatcher
        # Исходное окно facial: 10 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_hatcher_descript7',
            target_name='automarker_cam_hatcher_descript7_pos2', duration=14.5, smooth=True)
        cam_hatcher_descript7.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, duration=7,
            time_scale=0.7, trans_time=0.25)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHAND_HNEUT_GESTR_CASL_000LV_00, duration=6,
            time_scale=0.8, loop=True, trans_time=0.25)
        t += 2.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_RHND_CASL_000LV_xa_03, duration=6,
            time_scale=0.75, loop=True, trans_time=1)
        t += 4.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHAND_NEUT_RGHT_000LV_A_00, duration=2, trans_time=0.25)
        t += 2.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_01, duration=2,
            time_scale=0.75, trans_time=1)
        # hatcher.facial(group=MAIN, index=320, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(10.0)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.5)


        # Реплика 330 · hatcher · исходное время 217 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0330_hatcher
        # Исходное окно facial: 5 с.
        t = 0
        t += 4
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_hatcher_description8_lookexit', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_hatcher_description8_lookexit', duration=1.25, smooth=True)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_TURN_270LV_XA_03, duration=3, time_scale=0.75,
            trans_time=1)
        # hatcher.facial(group=MAIN, index=330, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(5)  # длительность удалённой реплики
        t = 0


        # Реплика 340 · hatcher · исходное время 222 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0340_hatcher
        # Исходное окно facial: 12 с.
        t = 0
        cam_hatcher_descript8.set(group=MAIN, time_delay=t)
        t += 2
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CROSS_ARMS_000LV_xa_03, duration=3.6,
            time_scale=0.8, trans_time=0.5)
        t += 3.6
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_HOLD_ARMS_CROSSED_000LV_XA_03, duration=1.4,
            time_scale=0.8, loop=True, trans_time=0.5)
        t += 1.4
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_UNCRSS_ARMS_000LV_XA_03, duration=8,
            time_scale=0.8, trans_time=0.5)
        # hatcher.facial(group=MAIN, index=340, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(12)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1)


        # Реплика 350 · hatcher · исходное время 233 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0350_hatcher
        # Исходное окно facial: 7 с.
        t = 0
        cam_hatcher_descript9.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05, duration=7, time_scale=0.8,
            loop=True, trans_time=0.5)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_hatcher_description8_lookbottom_to_trent_half', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_hatcher_description8_lookbottom_to_trent', duration=1.25, smooth=True)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_hatcher_description8_lookbottom', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_hatcher_description8_lookbottom', duration=1.25, smooth=True)
        t += 3.3
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHEAD_BASEPOSE_000LV_02_01, duration=3, trans_time=1.2)
        # hatcher.facial(group=MAIN, index=350, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(7)  # длительность удалённой реплики
        t = 0


        # Реплика 360 · trent · исходное время 240 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0360_trent
        # Исходное окно facial: 10 с.
        t = 0
        cam_trent_answer3.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_SHRG_SHLDRS_SMALL_000LV_XA_01, duration=15,
            time_scale=0.8, start_time=0.25)
        t += 2
        trent.motion(group=MAIN, time_delay=t, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, duration=15, trans_time=1)
        # trent.facial(group=MAIN, index=360, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(10)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-7.5)


        # Реплика 370 · hatcher · исходное время 242.5 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0370_hatcher
        # Исходное окно facial: 10 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_hatcher_description8_lookbottom_to_trent', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_hatcher_description8_lookbottom_to_trent_max', duration=1.25, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_hatcher_descript10',
            target_name='automarker_cam_hatcher_descript10_pos2', duration=10, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_hatcher_descript10_marker',
            target_name='automarker_cam_hatcher_descript10_marker_pos2', duration=10, smooth=True)
        cam_hatcher_descript10.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=3,
            time_scale=0.4, trans_time=0.5)
        t += 3.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_hatcher_description8_lookbottom', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_hatcher_description8_lookbottom', duration=1.25, smooth=True)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_HOLD_000LV_XA_01, duration=3,
            time_scale=0.6, loop=True, trans_time=0.5)
        t += 4.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=2,
            time_scale=0.7, trans_time=0.5)
        t += 0.5
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_hatcher_angry01', 'automarker_cam_hatcher_angry01_marker'], duration=100, offset=[0, 0, 0],
            up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_hatcher_angry02', 'automarker_cam_hatcher_angry02_marker'], duration=100, offset=[0, 0, 0],
            up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_hatcher_objective01', 'automarker_cam_hatcher_objective01_marker'], duration=100,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_mandrake_objective01', 'automarker_cam_mandrake_objective01_marker'], duration=100,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_mandrake_objective02', 'automarker_cam_mandrake_objective02_marker'], duration=100,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_hatcher_objective02', 'automarker_cam_hatcher_objective02_marker'], duration=100,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_hatcher_objective03', 'automarker_cam_hatcher_objective03_marker'], duration=100,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_trent_final', 'automarker_cam_trent_final_marker'], duration=100, offset=[0, 0, 0], up='Y_AXIS',
            front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['cam_final', 'automarker_cam_final_marker'],
            duration=100, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT',
            flags='LOOK_AT')
        t += 2.0
        cam_trent_answer4.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, duration=5)
        # hatcher.facial(group=MAIN, index=370, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(10.0)  # длительность удалённой реплики
        main_group.append_time(0.0)


        # Реплика 380 · trent · исходное время 252.5 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0380_trent
        # Исходное окно facial: 10 с.
        # trent.facial(group=MAIN, index=380, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(10.0)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-7.0)


        # Реплика 390 · hatcher · исходное время 255.5 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0390_hatcher
        # Исходное окно facial: 14.3 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_trent', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1.25, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_hatcher_angry01',
            target_name='automarker_cam_hatcher_angry01_pos2', duration=6, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_hatcher_angry01_marker',
            target_name='automarker_cam_hatcher_angry01_marker_pos2', duration=6, smooth=True)
        cam_hatcher_angry01.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_STEP_TRNS_090LV_XA_04, duration=5)
        t += 4.5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=2,
            trans_time=0.5)
        t += 1.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_hatcher_angry01',
            target_name='automarker_cam_hatcher_angry01_pos3', duration=6, smooth=True)
        t += 1.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=3,
            trans_time=0.5)
        t += 2.0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_EMPH_HNDSUP_TRNS_000LV_XA_01, duration=1.5,
            trans_time=0.5)
        t += 1.5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_EMPH_HNDSDN_TRNS_000LV_XA_01, duration=2,
            time_scale=0.7, trans_time=0.5)
        t += 1.7
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_hatcher_angry02',
            target_name='automarker_cam_hatcher_angry02_pos2', duration=6.3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_hatcher_angry02_marker',
            target_name='automarker_cam_hatcher_angry02_marker_pos2', duration=6.3, smooth=True)
        cam_hatcher_angry02.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_CROSS_ARMS_000LV_xa_03, duration=4,
            time_scale=0.6)
        # hatcher.facial(group=MAIN, index=390, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(14.3)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.8)


        # Реплика 400 · hatcher · исходное время 268 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0400_hatcher
        # Исходное окно facial: 6 с.
        t = 0
        t += 5
        music_reveal_and_exposition.change_attenuation(group=MAIN, time_delay=t, duration=3, attenuation=-25)
        # hatcher.facial(group=MAIN, index=400, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(6)  # длительность удалённой реплики
        t = 0


        # Реплика 410 · trent · исходное время 274 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0410_trent
        # Исходное окно facial: 10 с.
        t = 0
        cam_trent_answer4.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, duration=4, time_scale=0.8)
        # trent.facial(group=MAIN, index=410, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(10)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-8)


        # Реплика 420 · hatcher · исходное время 276 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0420_hatcher
        # Исходное окно facial: 4 с.
        t = 0
        cam_hatcher_angry02.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_UNCRSS_ARMS_000LV_XA_03, duration=5,
            start_time=0.75)
        # hatcher.facial(group=MAIN, index=420, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(4)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.5)


        # Реплика 430 · trent · исходное время 277.5 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0430_trent
        # Исходное окно facial: 10 с.
        t = 0
        cam_trent_answer4.set(group=MAIN, time_delay=t)
        t += 1.0
        trent.motion(group=MAIN, time_delay=t, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, duration=1, trans_time=1)
        # trent.facial(group=MAIN, index=430, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(10.0)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-8.5)


        # Реплика 440 · hatcher · исходное время 279 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0440_hatcher
        # Исходное окно facial: 4 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_mandrake_upper', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_mandrake', duration=1.25, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_mandrake_head_ik',
            target_name='automarker_head_hatcher_near_mandrake', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_mandrake_eye_ik',
            target_name='automarker_head_hatcher_near_mandrake', duration=1, smooth=True)
        cam_hatcher_objective01.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_TURN_090LV_XA_03, duration=4)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_hatcher', angle=20, axis='Y_AXIS',
            duration=2, smooth=False)
        music_reveal_special_mystery.start(group=MAIN, time_delay=t, duration=31, loop=True)
        # hatcher.facial(group=MAIN, index=440, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(4)  # длительность удалённой реплики
        t = 0
        cam_mandrake_objective01.set(group=MAIN, time_delay=t)
        mandrake.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_SHRG_SHLDRS_SMALL_000LV_XA_03, duration=7,
            time_scale=0.7, start_time=0.5)
        main_group.append_time(0.5)


        # Реплика 450 · mandrake · исходное время 283.5 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0450_mandrake
        # Исходное окно facial: 3 с.
        # mandrake.facial(group=MAIN, index=450, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(3.0)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.7)


        # Реплика 460 · hatcher · исходное время 284.8 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0460_hatcher
        # Исходное окно facial: 4 с.
        t = 0
        cam_hatcher_objective01.set(group=MAIN, time_delay=t)
        # hatcher.facial(group=MAIN, index=460, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(4.0)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.8)


        # Реплика 470 · mandrake · исходное время 287 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0470_mandrake
        # Исходное окно facial: 11.3 с.
        t = 0
        cam_mandrake_objective02.set(group=MAIN, time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_mandrake_objective02',
            target_name='automarker_cam_mandrake_objective02_pos2', duration=4, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_mandrake_objective02_marker',
            target_name='automarker_cam_mandrake_objective02_marker_pos2', duration=4, smooth=True)
        t += 1
        mandrake.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_2STEP_FRWD_TRNS_000LV_XA_02, duration=1.5,
            time_scale=0.5, start_time=1.5, trans_time=1.5)
        t += 2.2
        mandrake.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_EMPH_HNDSUP_TRNS_000LV_XA_00, duration=1,
            time_scale=0.8, trans_time=0.5)
        t += 0.8
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_mandrake_objective02',
            target_name='automarker_cam_mandrake_objective02_pos3', duration=7, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_mandrake_objective02_marker',
            target_name='automarker_cam_mandrake_objective02_marker_pos3', duration=7, smooth=True)
        mandrake.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_HNDS_EMPH_000LV_XC_01, duration=1,
            time_scale=0.8, loop=True, trans_time=0.5)
        t += 1
        mandrake.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_EMPH_HNDSDN_TRNS_000LV_XA_00, duration=3,
            time_scale=0.8, trans_time=0.5)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_mandrake_head_ik',
            target_name='automarker_head_trent_mandrakes_look', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_mandrake_eye_ik',
            target_name='automarker_head_trent_mandrakes_look_far', duration=1.5, smooth=True)
        mandrake.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=2,
            time_scale=0.8, trans_time=0.5)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_mandrake_head_ik',
            target_name='automarker_head_hatcher_near_mandrake', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_mandrake_eye_ik',
            target_name='automarker_head_hatcher_near_mandrake', duration=1.5, smooth=True)
        t += 0.5
        mandrake.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=2,
            time_scale=0.5, trans_time=0.5)
        # mandrake.facial(group=MAIN, index=470, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(11.3)  # длительность удалённой реплики
        t = 0
        mandrake.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=1, time_scale=1.5,
            trans_time=0.2)
        t += 0.2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_mandrake_stand', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_mandrake_stand', duration=1.25, smooth=True)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_mandrake_stand', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_mandrake_stand', duration=1.25, smooth=True)
        main_group.append_time(1.2)


        # Реплика 480 · trent · исходное время 299.5 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0480_trent
        # Исходное окно facial: 10 с.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_trent', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_trent', duration=1.25, smooth=True)
        t += 0.5
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_TURN_315LV_XA_03, duration=3)
        t += 0.5
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_hatcher', angle=-10, axis='Y_AXIS',
            duration=1, smooth=False)
        # trent.facial(group=MAIN, index=480, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(10.0)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-8.0)


        # Реплика 490 · hatcher · исходное время 301.5 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0490_hatcher
        # Исходное окно facial: 3 с.
        t = 0
        cam_hatcher_objective02.set(group=MAIN, time_delay=t)
        # hatcher.facial(group=MAIN, index=490, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(3.0)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.5)


        # Реплика 500 · trent · исходное время 303 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0500_trent
        # Исходное окно facial: 10 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_hatcher_description3', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_hatcher_description3', duration=1.25, smooth=True)
        cam_trent_final.set(group=MAIN, time_delay=t)
        t += 2.5
        trent.motion(group=MAIN, time_delay=t, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, duration=1, trans_time=1)
        # trent.facial(group=MAIN, index=500, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(10)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-7)


        # Реплика 510 · hatcher · исходное время 306 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m05_equip_0510_hatcher
        # Исходное окно facial: 4 с.
        t = 0
        cam_hatcher_objective02.set(group=MAIN, time_delay=t)
        t += 3.9999
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_hatcher', angle=25, axis='Y_AXIS',
            duration=1e-05, smooth=False)
        # hatcher.facial(group=MAIN, index=510, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(4)  # длительность удалённой реплики
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_head_ik',
            target_name='automarker_head_hatcher_exitpoint', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_hatcher_eye_ik',
            target_name='automarker_head_hatcher_exitpoint', duration=1.25, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_trent_final_exitpoint', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_trent_final_exitpoint', duration=1.25, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_mandrake_head_ik',
            target_name='automarker_head_mandrake_exipoint', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_mandrake_eye_ik',
            target_name='automarker_head_mandrake_exipoint', duration=1.25, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_final', target_name='automarker_cam_final_pos2',
            duration=6, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_final_marker',
            target_name='automarker_cam_final_marker_pos2', duration=6, smooth=True)
        cam_final.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Prop_Maglev', target_name='automarker_maglev_pos2',
            duration=0.001, smooth=False)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WALK_TRNS_270LV_XA_02, duration=2)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_STND_WALK_TRNS_270LV_XA_02, duration=2.35)
        music_reveal_special_mystery.change_attenuation(group=MAIN, time_delay=t, duration=0.001, attenuation=-5)
        music_reveal_special_mystery.start(group=MAIN, time_delay=t, duration=10000, start_time=16500)
        t += 1
        mandrake.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01, duration=2)
        t += 1
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=51, loop=True)
        t += 0.09
        mandrake.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=51, loop=True)
        t += 0.26
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_WLKG_000LV_XA_01, duration=21, loop=True)
        main_group.append_time(10.0)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M05EquipScene
