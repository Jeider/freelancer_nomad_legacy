"""m06_prison_new: постановка для ручного редактирования.

Точки: SCENES/m06_prison_new.blend → DUMPS/m06_prison_new.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — смещение внутри текущего блока; facial()/append_time() двигают часы.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Alchemy,
    Character,
    ConnectHardpointEvent,
    EyeIkEvent,
    LookAtCamera,
    MAIN,
    MotionEvent,
    MoveEvent,
    NeckIkEvent,
    Prop,
    RotateAxisEvent,
    Sound,
    SoundEvent,
    StaticCamera,
)
from story.cutscenes.anim import (
    Male,
    Trent,
)
from story.cutscenes.source_extensions import (
    SourceAttachEvent,
    SourceMotionEvent,
    preserve_entity,
    preserve_spatial,
)
from story import actors


class PropDoors(Prop):
    COMPOUND_TEMPLATE_NAME = 'prison_doors'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropCigarette(Prop):
    COMPOUND_TEMPLATE_NAME = 'cigarette_3'
    SRT_GRP = 0
    USR_FLG = 0


class PropCase1(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_prison_case'
    SRT_GRP = 0
    USR_FLG = 0


class PropPanel1(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_prison_panel'
    SRT_GRP = 0
    USR_FLG = 0


class PropCase2(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_prison_case'
    SRT_GRP = 0
    USR_FLG = 0


class PropPanel2(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_prison_panel'
    SRT_GRP = 0
    USR_FLG = 0


class PropBody1(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_prison_pirate_body1'
    SRT_GRP = 0
    USR_FLG = 0


class PropBody2(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_prison_pirate_body2'
    SRT_GRP = 0
    USR_FLG = 0


class PropBody3(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_prison_pirate_body1'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropMaskTrent(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_prison_neck_bomb'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropMaskPris1(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_prison_neck_bomb'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropMaskPris2(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_prison_neck_bomb'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropMaskPris3(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_prison_neck_bomb'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropMaskPris4(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_prison_neck_bomb'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropMaskPris5(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_prison_neck_bomb'
    SRT_GRP = 0
    USR_FLG = 0


class ExtraCharPrisoner1(actors.Actor):
    NAME = 'prisoner1'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_asf_prisoner04'
    GAME_ACTOR = 'Prisoner1'


class ExtraCharPrisoner2(actors.Actor):
    NAME = 'prisoner2'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_asf_prisoner02'
    GAME_ACTOR = 'Prisoner2'


class ExtraCharTrentClassic(actors.Actor):
    NAME = 'trent_classic'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'trent_original'
    GAME_ACTOR = 'TrentOriginal'


class ExtraCharPrisoner1b(actors.Actor):
    NAME = 'prisoner1b'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_asf_prisoner01b'
    GAME_ACTOR = 'Prisoner1b'


class ExtraCharPrisoner2b(actors.Actor):
    NAME = 'prisoner2b'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_asf_prisoner02b'
    GAME_ACTOR = 'Prisoner2b'


class ExtraCharPrisoner3b(actors.Actor):
    NAME = 'prisoner3b'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_asf_prisoner03b'
    GAME_ACTOR = 'Prisoner3b'


class ExtraCharPrisoner4b(actors.Actor):
    NAME = 'prisoner4b'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_asf_prisoner04b'
    GAME_ACTOR = 'Prisoner4b'



class M06PrisonNewScene(Scene):
    DUMP_FILE = 'm06_prison_new'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        doors = PropDoors(root=self, name='doors', light_group=9, init_point='doors', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(doors, userprops={'category': 'Prop'})
        prop_cigarette = PropPropCigarette(root=self, name='prop_cigarette', light_group=9, init_point='prop_cigarette',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(prop_cigarette, userprops={'category': 'Prop'})
        vfx_rtc_cigaretteglow_4 = Alchemy(root=self, name='vfx_rtc_cigaretteglow_4', particles='rtc_cigaretteglow',
            point_name='vfx_rtc_cigaretteglow_4', sparam=0)
        preserve_entity(vfx_rtc_cigaretteglow_4, flags='LIT_DYNAMIC+LIT_AMBIENT')
        vfx_rtc_sydsmoke_3 = Alchemy(root=self, name='vfx_rtc_sydsmoke_3', particles='rtc_sydsmoke',
            point_name='vfx_rtc_sydsmoke_3', sparam=0)
        preserve_entity(vfx_rtc_sydsmoke_3, flags='LIT_DYNAMIC+LIT_AMBIENT')
        case1 = PropCase1(root=self, name='case1', light_group=9, init_point='case1', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(case1, userprops={'category': 'Prop'})
        panel1 = PropPanel1(root=self, name='panel1', light_group=9, init_point='panel1', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(panel1, userprops={'category': 'Prop'})
        case2 = PropCase2(root=self, name='case2', light_group=9, init_point='case2', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(case2, userprops={'category': 'Prop'})
        panel2 = PropPanel2(root=self, name='panel2', light_group=9, init_point='panel2', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(panel2, userprops={'category': 'Prop'})
        body1 = PropBody1(root=self, name='body1', light_group=9, init_point='body1', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(body1, userprops={'category': 'Prop'})
        body2 = PropBody2(root=self, name='body2', light_group=9, init_point='body2', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(body2, userprops={'category': 'Prop'})
        body3 = PropBody3(root=self, name='body3', light_group=9, init_point='body3', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(body3, userprops={'category': 'Prop'})
        prop_mask_trent = PropPropMaskTrent(root=self, name='prop_mask_trent', light_group=9, init_point='prop_mask_trent',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(prop_mask_trent, userprops={'category': 'Prop'})
        prop_mask_pris1 = PropPropMaskPris1(root=self, name='prop_mask_pris1', light_group=9, init_point='prop_mask_pris1',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(prop_mask_pris1, userprops={'category': 'Prop'})
        prop_mask_pris2 = PropPropMaskPris2(root=self, name='prop_mask_pris2', light_group=9, init_point='prop_mask_pris2',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(prop_mask_pris2, userprops={'category': 'Prop'})
        prop_mask_pris3 = PropPropMaskPris3(root=self, name='prop_mask_pris3', light_group=9, init_point='prop_mask_pris3',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(prop_mask_pris3, userprops={'category': 'Prop'})
        prop_mask_pris4 = PropPropMaskPris4(root=self, name='prop_mask_pris4', light_group=9, init_point='prop_mask_pris4',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(prop_mask_pris4, userprops={'category': 'Prop'})
        prop_mask_pris5 = PropPropMaskPris5(root=self, name='prop_mask_pris5', light_group=9, init_point='prop_mask_pris5',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(prop_mask_pris5, userprops={'category': 'Prop'})
        ambience_hall = Sound(root=self, name='ambience_hall', sound='ambience_deck_space_smaller', attenuation=0, dmin=50,
            dmax=300, priority='Story_Sound_1')
        preserve_entity(ambience_hall, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        ambience_room = Sound(root=self, name='ambience_room', sound='ambience_deck_space_larger', attenuation=-1000000,
            dmin=50, dmax=300, priority='Story_Sound_1')
        preserve_entity(ambience_room, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        step1 = Sound(root=self, name='step1', sound='fs_ml_steel04', attenuation=-45, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(step1, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        step2 = Sound(root=self, name='step2', sound='fs_ml_steel01', attenuation=-45, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(step2, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        step3 = Sound(root=self, name='step3', sound='fs_ml_steel03', attenuation=-45, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(step3, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        step1_cmdr = Sound(root=self, name='step1_cmdr', sound='fs_ml_steel04', attenuation=-20, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(step1_cmdr, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        step2_cmdr = Sound(root=self, name='step2_cmdr', sound='fs_ml_steel01', attenuation=-20, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(step2_cmdr, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        step3_cmdr = Sound(root=self, name='step3_cmdr', sound='fs_ml_steel03', attenuation=-20, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(step3_cmdr, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        snd_open_door = Sound(root=self, name='snd_open_door', sound='depot_open_sound', attenuation=0, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(snd_open_door, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        snd_close_door = Sound(root=self, name='snd_close_door', sound='depot_close_sound', attenuation=0, dmin=50,
            dmax=300, priority='Story_Sound_1')
        preserve_entity(snd_close_door, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        snd_close_door_clothesbox = Sound(root=self, name='snd_close_door_clothesbox', sound='depot_close_sound',
            attenuation=-5, dmin=50, dmax=300, priority='Story_Sound_1')
        preserve_entity(snd_close_door_clothesbox, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        prisoner1 = Character(root=self, actor=ExtraCharPrisoner1, light_group=9, init_point='Char_prisoner1',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(prisoner1, template_name='m06_asf_prisoner04',
            userprops={'actor': 'Prisoner1', 'category': 'Character'})
        prisoner2 = Character(root=self, actor=ExtraCharPrisoner2, light_group=9, init_point='Char_prisoner2',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(prisoner2, template_name='m06_asf_prisoner02',
            userprops={'actor': 'Prisoner2', 'category': 'Character'})
        prisoner3 = Character(root=self, actor=actors.DeltaThree, light_group=9, init_point='Char_delta3',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(prisoner3, template_name='m06_asf_prisoner03',
            userprops={'actor': 'Prisoner3', 'category': 'Character'})
        prisoner4 = Character(root=self, actor=actors.DeltaOne, light_group=9, init_point='Char_delta1',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(prisoner4, template_name='m06_asf_prisoner01',
            userprops={'actor': 'Prisoner4', 'category': 'Character'})
        commander = Character(root=self, actor=actors.OrderGuard, light_group=9, init_point='Char_guard',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(commander, template_name='m06_gunner_leader',
            userprops={'actor': 'Gunner_commander', 'category': 'Character'})
        syd = Character(root=self, actor=actors.Ceed, light_group=9, init_point='Char_syd', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(syd, template_name='syd', userprops={'actor': 'Syd', 'category': 'Character'})
        trent = Character(root=self, actor=actors.Trent, light_group=9, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'Actor': 'Player', 'category': 'Character'})
        trent_classic = Character(root=self, actor=ExtraCharTrentClassic, light_group=9, init_point='Char_trent_classic',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(trent_classic, template_name='trent_original',
            userprops={'actor': 'TrentOriginal', 'category': 'Character'})
        prisoner1b = Character(root=self, actor=ExtraCharPrisoner1b, light_group=9, init_point='Char_prisoner1b',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(prisoner1b, template_name='m06_asf_prisoner01b',
            userprops={'actor': 'Prisoner1b', 'category': 'Character'})
        prisoner2b = Character(root=self, actor=ExtraCharPrisoner2b, light_group=9, init_point='Char_prisoner2b',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(prisoner2b, template_name='m06_asf_prisoner02b',
            userprops={'actor': 'Prisoner2b', 'category': 'Character'})
        prisoner3b = Character(root=self, actor=ExtraCharPrisoner3b, light_group=9, init_point='Char_prisoner3b',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(prisoner3b, template_name='m06_asf_prisoner03b',
            userprops={'actor': 'Prisoner3b', 'category': 'Character'})
        prisoner4b = Character(root=self, actor=ExtraCharPrisoner4b, light_group=9, init_point='Char_prisoner4b',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(prisoner4b, template_name='m06_asf_prisoner04b',
            userprops={'actor': 'Prisoner4b', 'category': 'Character'})
        cam_start_outside = LookAtCamera(root=self, name='cam_start_outside', fov=35, farplane=5000, look_duration=70)
        preserve_entity(cam_start_outside)
        cam_start_inside = LookAtCamera(root=self, name='cam_start_inside', fov=30, farplane=5000, look_duration=70)
        preserve_entity(cam_start_inside)
        cam_syd_appear = LookAtCamera(root=self, name='cam_syd_appear', fov=25, farplane=5000, look_duration=70)
        preserve_entity(cam_syd_appear)
        cam_salut = LookAtCamera(root=self, name='cam_salut', fov=25, farplane=5000, look_duration=70)
        preserve_entity(cam_salut)
        cam_syd_gives_order = LookAtCamera(root=self, name='cam_syd_gives_order', fov=25, farplane=5000, look_duration=70)
        preserve_entity(cam_syd_gives_order)
        cam_syd_order = LookAtCamera(root=self, name='cam_syd_order', fov=25, farplane=5000, look_duration=70)
        preserve_entity(cam_syd_order)
        cam_syd_opendoor = StaticCamera(root=self, name='cam_syd_opendoor', fov=20, farplane=5000)
        preserve_entity(cam_syd_opendoor)
        cam_syd_doorclosed = StaticCamera(root=self, name='cam_syd_doorclosed', fov=15, farplane=5000)
        preserve_entity(cam_syd_doorclosed)
        cam_sydgreet_begin = StaticCamera(root=self, name='cam_sydgreet_begin', fov=15, farplane=5000)
        preserve_entity(cam_sydgreet_begin)
        cam_sydgreet_captapprove = StaticCamera(root=self, name='cam_sydgreet_captapprove', fov=15, farplane=5000)
        preserve_entity(cam_sydgreet_captapprove)
        cam_syd_reveal = StaticCamera(root=self, name='cam_syd_reveal', fov=15, farplane=5000)
        preserve_entity(cam_syd_reveal)
        cam_trent = StaticCamera(root=self, name='cam_trent', fov=15, farplane=5000)
        preserve_entity(cam_trent)
        cam_syd_trentside = StaticCamera(root=self, name='cam_syd_trentside', fov=15, farplane=5000)
        preserve_entity(cam_syd_trentside)
        cam_captain_sydanswer = StaticCamera(root=self, name='cam_captain_sydanswer', fov=15, farplane=5000)
        preserve_entity(cam_captain_sydanswer)
        cam_syd_captside = StaticCamera(root=self, name='cam_syd_captside', fov=16, farplane=5000)
        preserve_entity(cam_syd_captside)
        cam_syd_clothesbox = StaticCamera(root=self, name='cam_syd_clothesbox', fov=15, farplane=5000)
        preserve_entity(cam_syd_clothesbox)
        cam_delta3 = StaticCamera(root=self, name='cam_delta3', fov=15, farplane=5000)
        preserve_entity(cam_delta3)
        cam_delta1 = StaticCamera(root=self, name='cam_delta1', fov=15, farplane=5000)
        preserve_entity(cam_delta1)
        cam_trent_finalword = StaticCamera(root=self, name='cam_trent_finalword', fov=15, farplane=5000)
        preserve_entity(cam_trent_finalword)
        cam_exit = StaticCamera(root=self, name='cam_exit', fov=20, farplane=5000)
        preserve_entity(cam_exit)

        # Вход / начальная постановка.
        t = 0
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='prop_mask_trent', parent_name='Char_trent',
            duration=1000, target_hardpoint='hp_neck_connect', parent_hardpoint='hp_head_top_conn')
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='prop_mask_pris1',
            parent_name='Char_prisoner1', duration=1000, target_hardpoint='hp_neck_connect',
            parent_hardpoint='hp_head_top_conn')
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='prop_mask_pris2',
            parent_name='Char_prisoner2', duration=1000, target_hardpoint='hp_neck_connect',
            parent_hardpoint='hp_head_top_conn')
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='prop_mask_pris3', parent_name='Char_delta3',
            duration=1000, target_hardpoint='hp_neck_connect', parent_hardpoint='hp_head_top_conn')
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='prop_mask_pris4', parent_name='Char_delta1',
            duration=1000, target_hardpoint='hp_neck_connect', parent_hardpoint='hp_head_top_conn')
        ambience_hall.start(group=MAIN, time_delay=t, duration=5000, loop=True)
        ambience_room.start(group=MAIN, time_delay=t, duration=5000, loop=True)
        cam_start_outside.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_start_outside',
            target_name='automarker_cam_start_outside_pos2', duration=10, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_start_outside_focus',
            target_name='automarker_cam_start_outside_marker_pos2', duration=10, smooth=True)
        commander.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_STRCH_YAWN_000LV_XA_06, duration=11, loop=True)
        t += 9.9
        ambience_hall.change_attenuation(group=MAIN, time_delay=t, duration=0.1, attenuation=-100)
        t += 0.1
        ambience_room.change_attenuation(group=MAIN, time_delay=t, duration=0.1, attenuation=0)
        cam_start_inside.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_start_inside',
            target_name='automarker_cam_start_inside_pos2', duration=10, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_start_inside_focus',
            target_name='automarker_cam_start_inside_marker_pos2', duration=10, smooth=True)
        prisoner3.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_TWSTU_CCL_LESS_000LV_A_14, duration=20)
        prisoner4.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_HEAD_HOLDR_000LV_XA_03, duration=20)
        t += 4
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_LOOK_AROU_CASL_000LV_XA_04, duration=20,
            time_scale=0.8)
        t += 2
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner2',
            anim=Male.Sc_MLBODY_CHRB_IDLE_BIG_000LV_XA_05, duration=20, loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner1',
            anim=Male.Sc_MLBODY_CHRB_LOOK_AROU_CASL_000LV_XA_04, duration=20)
        t += 1
        prisoner4.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_HOLD_HEAD_RLEASE_000LV_XA_03, duration=20,
            time_scale=0.7)
        t += 4
        commander.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_BEND_FOTR_SWNGARMS_000DN_XA_12, duration=11,
            loop=True, trans_time=1)
        t += 0.9
        ambience_hall.change_attenuation(group=MAIN, time_delay=t, duration=0.1, attenuation=0)
        t += 0.1
        ambience_room.change_attenuation(group=MAIN, time_delay=t, duration=0.1, attenuation=-100)
        cam_syd_appear.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_syd_appear',
            target_name='automarker_cam_syd_appear_pos2', duration=6, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_syd_appear_focus',
            target_name='automarker_cam_syd_appear_marker_pos2', duration=6, smooth=True)
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=7.9999, loop=True)
        t += 0.7
        step1.start(group=MAIN, time_delay=t, duration=5)
        t += 0.3
        step1.change_attenuation(group=MAIN, time_delay=t, duration=3, attenuation=-15)
        step2.change_attenuation(group=MAIN, time_delay=t, duration=3, attenuation=-15)
        step3.change_attenuation(group=MAIN, time_delay=t, duration=3, attenuation=-15)
        t += 0.4
        step2.start(group=MAIN, time_delay=t, duration=5)
        t += 0.6
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_syd', angle=-15, axis='Y_AXIS',
            duration=5.99, smooth=True)
        t += 0.1
        step3.start(group=MAIN, time_delay=t, duration=5)
        t += 0.7
        step2.start(group=MAIN, time_delay=t, duration=5)
        t += 0.7
        step1.start(group=MAIN, time_delay=t, duration=5)
        t += 0.7
        step3.start(group=MAIN, time_delay=t, duration=5)
        t += 0.5
        step1.start(group=MAIN, time_delay=t, duration=5)
        t += 0.6
        step2.start(group=MAIN, time_delay=t, duration=5)
        t += 0.6
        step3.start(group=MAIN, time_delay=t, duration=5)
        t += 0.1
        step1.change_attenuation(group=MAIN, time_delay=t, duration=3, attenuation=-30)
        step2.change_attenuation(group=MAIN, time_delay=t, duration=3, attenuation=-30)
        step3.change_attenuation(group=MAIN, time_delay=t, duration=3, attenuation=-30)
        commander.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_TURN_270LV_XA_04, duration=5)
        t += 0.6
        step1.start(group=MAIN, time_delay=t, duration=5)
        t += 0.65
        commander.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_SURPRSE_000LV_XA_, duration=5, trans_time=0.25)
        t += 0.05
        step3.start(group=MAIN, time_delay=t, duration=5)
        t += 0.7
        step2.start(group=MAIN, time_delay=t, duration=5)
        cam_syd_order.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_syd_order',
            target_name='automarker_cam_syd_order_pos2', duration=10, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_syd_order_focus',
            target_name='automarker_cam_syd_order_marker_pos2', duration=10, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_syd',
            target_name='automarker_point_syd_around_commander', duration=0.001, smooth=False)
        t += 0.01
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=6, time_scale=0.85)
        t += 0.69
        step3.start(group=MAIN, time_delay=t, duration=5)
        t += 0.3
        commander.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_SALUT_000LV_XA_03, duration=5, trans_time=0.25)
        t += 0.4
        step3.start(group=MAIN, time_delay=t, duration=5)
        main_group.append_time(32)


        # Реплика 10 · syd · исходное время 32 с
        # Вольно, рядовой. Идите в диспетчерскую, пусть подготовят корабль для доставки пленных на нашу базу. А я
        # пока начну допрос.
        # Исходное окно facial: 9.1 с.
        t = 0
        ambience_hall.change_attenuation(group=MAIN, time_delay=t, duration=0.1, attenuation=-2)
        t += 1
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_GESTR_180LV_XA_02, duration=6, time_scale=0.6,
            trans_time=1)
        t += 2
        step1.change_attenuation(group=MAIN, time_delay=t, duration=3, attenuation=-20)
        step2.change_attenuation(group=MAIN, time_delay=t, duration=3, attenuation=-20)
        step3.change_attenuation(group=MAIN, time_delay=t, duration=3, attenuation=-20)
        t += 2
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_ATEASE_HSEC_RLEASE_000LV_XA_03, duration=6,
            time_scale=0.54, trans_time=1)
        t += 3.5
        commander.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_HNDS_CASL_000LV_xa_04, duration=3,
            time_scale=0.8, trans_time=2)
        syd.facial(group=MAIN, index=10, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.1)


        # Реплика 20 · guard · исходное время 41 с
        # Сэр, но если...
        # Исходное окно facial: 4.5 с.
        t = 0
        cam_salut.set(group=MAIN, time_delay=t)
        commander.facial(group=MAIN, index=20, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.5)


        # Реплика 30 · syd · исходное время 43 с
        # Никаких если. На них же шокеры, пусть только попробуют рыпнуться.
        # Исходное окно facial: 7.25 с.
        t = 0
        cam_syd_gives_order.set(group=MAIN, time_delay=t)
        t += 1
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_ATEASE_RLEASE_000LV_XA_01, duration=6, time_scale=0.6,
            trans_time=1)
        t += 0.5
        commander.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_HNDSDN_TRNS_000LV_XA_01, duration=4,
            time_scale=0.8, trans_time=1)
        t += 1.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_salut', target_name='automarker_cam_salut_pos2',
            duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_salut_focus',
            target_name='automarker_cam_salut_marker_pos2', duration=1, smooth=True)
        t += 1
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=3, loop=True, trans_time=1)
        t += 1
        commander.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_SALUT_000LV_XA_03, duration=5, time_scale=1.3,
            trans_time=0.25)
        cam_salut.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_salut', target_name='automarker_cam_salut_pos3',
            duration=12, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_salut_focus',
            target_name='automarker_cam_salut_marker_pos3', duration=10, smooth=True)
        syd.facial(group=MAIN, index=30, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.75)


        # Реплика 40 · guard · исходное время 48.5 с
        # Есть, сэр.
        # Исходное окно facial: 4 с.
        t = 0
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_eye_ik',
            target_name='automarker_head_syd_front', duration=1, smooth=True)
        t += 1.0
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_1STEP_BKWD_PVOTL_270LV_XA_06, duration=6, trans_time=1)
        t += 0.5
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_guard', angle=-25, axis='Y_AXIS', duration=1,
            smooth=True)
        t += 0.2
        commander.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01, duration=5,
            trans_time=0.25)
        t += 0.8
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_guard', angle=25, axis='Y_AXIS', duration=2,
            smooth=True)
        t += 0.2
        step1_cmdr.start(group=MAIN, time_delay=t, duration=5)
        t += 0.05
        commander.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=55, loop=True)
        t += 0.65
        step2_cmdr.start(group=MAIN, time_delay=t, duration=5)
        commander.facial(group=MAIN, index=40, append=True, auto_lip=True, extra_delay=0)
        t = 0
        t += 0.5
        step1_cmdr.change_attenuation(group=MAIN, time_delay=t, duration=5, attenuation=-50)
        step2_cmdr.change_attenuation(group=MAIN, time_delay=t, duration=5, attenuation=-50)
        step3_cmdr.change_attenuation(group=MAIN, time_delay=t, duration=5, attenuation=-50)
        t += 0.1
        step3_cmdr.start(group=MAIN, time_delay=t, duration=5)
        t += 0.4
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_guard', angle=90, axis='Y_AXIS',
            duration=2.5, smooth=True)
        t += 0.3
        step2_cmdr.start(group=MAIN, time_delay=t, duration=5)
        t += 0.7
        step1_cmdr.start(group=MAIN, time_delay=t, duration=5)
        t += 0.7
        step3_cmdr.start(group=MAIN, time_delay=t, duration=5)
        t += 0.3
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01, duration=5, trans_time=0.25)
        t += 0.2
        step1_cmdr.start(group=MAIN, time_delay=t, duration=5)
        t += 0.6
        step2_cmdr.start(group=MAIN, time_delay=t, duration=5)
        t += 0.25
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=3.4499, loop=True)
        t += 0.15
        step1.start(group=MAIN, time_delay=t, duration=5)
        t += 0.2
        step3_cmdr.start(group=MAIN, time_delay=t, duration=5)
        t += 0.5
        step2.start(group=MAIN, time_delay=t, duration=5)
        t += 0.2
        step1_cmdr.start(group=MAIN, time_delay=t, duration=5)
        t += 0.5
        step3.start(group=MAIN, time_delay=t, duration=5)
        t += 0.2
        step3_cmdr.start(group=MAIN, time_delay=t, duration=5)
        t += 0.5
        step2.start(group=MAIN, time_delay=t, duration=5)
        t += 0.2
        step2_cmdr.start(group=MAIN, time_delay=t, duration=5)
        t += 0.5
        step1.start(group=MAIN, time_delay=t, duration=5)
        t += 0.2
        step3_cmdr.start(group=MAIN, time_delay=t, duration=5)
        t += 0.3
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_syd_opendoor', 'automarker_cam_syd_opendoor_marker'], duration=50, offset=[0, 0, 0], up='Y_AXIS',
            front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_syd_doorclosed', 'automarker_cam_syd_doorclosed_marker'], duration=50, offset=[0, 0, 0],
            up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_sydgreet_begin', 'automarker_cam_sydgreet_begin_marker'], duration=150, offset=[0, 0, 0],
            up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_sydgreet_captapprove', 'automarker_cam_sydgreet_captapprove_marker'], duration=150,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_syd_reveal', 'automarker_cam_syd_reveal_marker'], duration=150, offset=[0, 0, 0], up='Y_AXIS',
            front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['cam_trent', 'automarker_cam_trent_marker'],
            duration=50, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT',
            flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_syd_trentside', 'automarker_cam_syd_trentside_marker'], duration=150, offset=[0, 0, 0],
            up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        cam_syd_opendoor.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_syd_opendoor',
            target_name='automarker_cam_syd_opendoor_pos2', duration=10, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_syd',
            target_name='automarker_point_syd_walk_to_doors', duration=0.001, smooth=False)
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=3, start_time=0.9, loop=True)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_syd', angle=-45, axis='Y_AXIS', duration=1,
            smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=25, loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner2',
            anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=25, loop=True)
        prisoner3.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=2)
        prisoner4.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=2)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner1',
            anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=2)
        t += 0.2
        step3.start(group=MAIN, time_delay=t, duration=5)
        t += 0.2
        step3_cmdr.start(group=MAIN, time_delay=t, duration=5)
        t += 0.3
        step1.start(group=MAIN, time_delay=t, duration=5)
        t += 0.6
        step2.start(group=MAIN, time_delay=t, duration=5)
        t += 0.6
        step3.start(group=MAIN, time_delay=t, duration=5)
        t += 0.7
        step1.start(group=MAIN, time_delay=t, duration=5)
        t += 0.4
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=4)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_syd', angle=-45, axis='Y_AXIS', duration=2,
            smooth=True)
        t += 0.3
        step3.start(group=MAIN, time_delay=t, duration=5)
        t += 0.7
        step2.start(group=MAIN, time_delay=t, duration=5)
        t += 0.7
        step3.start(group=MAIN, time_delay=t, duration=5)
        t += 0.6
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WAVE_LHND_000LV_XA_02, duration=8, trans_time=0.5)
        t += 1.7
        snd_open_door.start(group=MAIN, time_delay=t, duration=10)
        t += 0.2
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner1',
            anim=Male.Sc_MLBODY_CHRB_TWSTS_LOOK_090LV_XA_02, duration=5, time_scale=0.8)
        t += 0.1
        SourceMotionEvent(root=self, group=MAIN, time_delay=t, targets=['doors'], animation='Sc_cv_prison_cell',
            duration=3.332, time_scale=1, weight=1, trans_scale=1)
        t += 0.2
        prisoner4.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_TWSTS_LOOK_090LV_XA_02, duration=5,
            time_scale=0.8)
        t += 0.3
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner2',
            anim=Male.Sc_MLBODY_CHRB_TWSTS_LOOK_270LV_XA_03, duration=5, time_scale=0.8)
        t += 0.2
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01, duration=4, trans_time=1)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_prisoner1', target_name='Char_syd', duration=6,
            transition_duration=3, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_prisoner2',
            target_name='automarker_prisoner2_head_ik', duration=20, transition_duration=1, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_prisoner2',
            target_name='automarker_prisoner2_eye_ik', duration=20, transition_duration=1, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_TWSTS_LOOK_270LV_XA_03, duration=5, time_scale=0.6)
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_prisoner2',
            target_name='automarker_prisoner2_eye_ik', duration=25, transition_duration=1, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 0.5
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='Char_syd', duration=10,
            transition_duration=4, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_delta1', target_name='Char_syd', duration=5,
            transition_duration=2.5, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 0.5
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_delta3', target_name='Char_syd', duration=6,
            transition_duration=2, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 0.12
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=4)
        t += 1.48
        SourceMotionEvent(root=self, group=MAIN, time_delay=t, targets=['doors'], animation='Sc_cv_prison_cell',
            duration=3.332, start_time=3.332, time_scale=1, weight=1, trans_scale=1)
        snd_close_door.start(group=MAIN, time_delay=t, duration=10)
        t += 0.9
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_LOOK_AROU_CASL_000LV_XA_08, duration=8, trans_time=1)
        t += 0.5
        snd_close_door.change_attenuation(group=MAIN, time_delay=t, duration=0.1, attenuation=-2)
        ambience_hall.change_attenuation(group=MAIN, time_delay=t, duration=2, attenuation=-100)
        ambience_room.change_attenuation(group=MAIN, time_delay=t, duration=2, attenuation=0)
        cam_sydgreet_begin.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_sydgreet_begin',
            target_name='automarker_cam_sydgreet_begin_pos2', duration=5.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_sydgreet_begin_marker',
            target_name='automarker_cam_sydgreet_begin_marker_pos2', duration=5.5, smooth=True)
        t += 1.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_prisoner2_head_ik',
            target_name='automarker_head_asf_captain_p2_near', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_prisoner2_eye_ik',
            target_name='automarker_head_asf_captain', duration=1.25, smooth=True)
        t += 0.5
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner2',
            anim=Male.Sc_MLBODY_CHRB_TWSTS_FROM_270LV_XA_03, duration=2.5, time_scale=0.2)
        t += 1.5
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner1',
            anim=Male.Sc_MLBODY_CHRB_IDLE_BIG_000LV_XA_05, duration=2, loop=True)
        t += 0.5
        prisoner3.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_TWSTU_CCL_LESS_000LV_A_14, duration=8)
        t += 0.5
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner1',
            anim=Male.Sc_MLBODY_CHRB_SHRG_SHLDRS_SMALL_000LV_XA_03, duration=11, time_scale=0.4, trans_time=1)
        t += 0.5
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_prisoner2',
            target_name='automarker_prisoner2_head_ik', duration=25, transition_duration=1, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 0.5
        cam_sydgreet_captapprove.set(group=MAIN, time_delay=t)
        prisoner4.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=1, start_time=2)
        t += 0.5
        prisoner4.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_YESS_000LV_A_01, duration=4, time_scale=0.6,
            trans_time=0.25)
        t += 0.1
        prisoner4.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=1,
            time_scale=0.3, trans_time=0.25)
        main_group.append_time(27.5)


        # Реплика 50 · syd · исходное время 80 с
        # Спокойно, джентльмены, я не кусаюсь. Вам повезло, что все произошло во время моего дежурства.
        # Исходное окно facial: 8.6 с.
        t = 0
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['cam_delta3', 'automarker_cam_delta3_marker'],
            duration=50, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT',
            flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['cam_delta1', 'automarker_cam_delta1_marker'],
            duration=50, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT',
            flags='LOOK_AT')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_prisoner2_head_ik',
            target_name='automarker_head_asf_captain_p2_near', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_prisoner2_eye_ik',
            target_name='automarker_head_asf_captain', duration=2, smooth=True)
        prisoner4.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_TWSTS_LOOK_090LV_XA_02, duration=5,
            time_scale=0.5, trans_time=1)
        prisoner4.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_SURPRSE_QUZZCLLY_000LV_XA_, duration=1,
            time_scale=0.8, trans_time=0.25)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_delta1', target_name='Char_syd', duration=10,
            transition_duration=2, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_delta3', target_name='Char_syd', duration=10,
            transition_duration=2, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_syd', target_name='automarker_syd_head_ik',
            duration=11.8, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_syd', target_name='automarker_syd_eye_ik',
            duration=11.8, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_head_ik',
            target_name='automarker_head_prisoner2', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_eye_ik',
            target_name='automarker_head_prisoner2', duration=1.5, smooth=True)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['vfx_rtc_sydsmoke_3', 'prop_cigarette'],
            duration=110, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='hp_cigarette_tip_smoke',
            target_type='HARDPOINT', flags='POSITION')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['vfx_rtc_cigaretteglow_4', 'prop_cigarette'],
            duration=110, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='hp_cigarette_tip_smoke',
            target_type='HARDPOINT', flags='POSITION+ORIENTATION')
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_GESTR_NO_000LV_XA_02, duration=5, time_scale=0.7)
        t += 0.5
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner1',
            anim=Male.Sc_MLBODY_CHRB_TWSTS_LOOK_090LV_XA_02, duration=5, time_scale=0.5, trans_time=1)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_prisoner1', target_name='Char_syd', duration=10,
            transition_duration=2, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 1.5
        cam_syd_reveal.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_syd_reveal',
            target_name='automarker_cam_syd_reveal_pos2', duration=18, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_syd_reveal_marker',
            target_name='automarker_cam_syd_reveal_marker_pos2', duration=18, smooth=True)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_head_ik',
            target_name='automarker_head_asf_captain', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_eye_ik',
            target_name='automarker_head_asf_captain', duration=1.5, smooth=True)
        t += 1
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_ATEASE_HSEC_RLEASE_000LV_XA_03, duration=5,
            time_scale=0.8, trans_time=1)
        t += 3
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_head_ik',
            target_name='automarker_head_last_prisoner', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_eye_ik',
            target_name='automarker_head_last_prisoner', duration=1.5, smooth=True)
        syd.facial(group=MAIN, index=50, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-0.6)


        # Реплика 60 · syd · исходное время 88 с
        # Забыл представиться. Хари Сид, капитан Ордена, лейтенант СБА, работаю тут под прикрытием.
        # Исходное окно facial: 8.5 с.
        t = 0
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_head_ik',
            target_name='automarker_head_syd_front', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_eye_ik',
            target_name='automarker_head_syd_front', duration=2, smooth=True)
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_ATEASE_RLEASE_000LV_XA_01, duration=5, time_scale=0.6,
            trans_time=1)
        t += 2.8
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_GIVE_VEND_000LV_B_07, duration=5, time_scale=0.5,
            trans_time=0.5)
        t += 1.2
        vfx_rtc_cigaretteglow_4.start(group=MAIN, time_delay=t, duration=106)
        t += 0.5
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='prop_cigarette', parent_name='Char_syd',
            duration=500, target_hardpoint='hprightconnect_cigarette', parent_hardpoint='hprightconnect')
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_POINT_RGHT_MILI_000LV_00, duration=3)
        t += 0.9
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_SPCBODY_s002x_syd_XE_STND_000LV_11, duration=6, time_scale=1.5,
            start_time=1.3, trans_time=2.5)
        t += 1.6
        vfx_rtc_sydsmoke_3.start(group=MAIN, time_delay=t, duration=106)
        t += 0.4
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_MOTION_BREATHE_HEAVY_000LV_XA_, duration=4.444,
            time_scale=0.9, start_time=0.5, trans_time=0.5)
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=0.532, time_scale=0.1)
        syd.facial(group=MAIN, index=60, append=True, auto_lip=True, extra_delay=0)
        t = 0
        t += 0.9
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=4.444, time_scale=0.9,
            trans_time=0.5)
        main_group.append_time(2.5)


        # Реплика 65 · syd · исходное время 99 с
        # Сейчас подождем некоторое время, а потом я помогу вам покинуть негостеприимный борт Навуходоносора
        # Исходное окно facial: 10.25 с.
        t = 0
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, duration=7,
            time_scale=0.7, trans_time=1)
        t += 0.2
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_syd', target_name='automarker_syd_head_ik',
            duration=25, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_syd', target_name='automarker_syd_eye_ik',
            duration=25, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 0.8
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_head_ik',
            target_name='automarker_head_prisoner2_around', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_eye_ik',
            target_name='automarker_head_prisoner2', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_prisoner2_head_ik',
            target_name='automarker_head_syd', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_prisoner2_eye_ik',
            target_name='automarker_head_syd', duration=1, smooth=True)
        t += 1
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_RHND_CASL_000LV_xa_01, duration=6,
            time_scale=0.75, loop=True, trans_time=1)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_head_ik',
            target_name='automarker_head_last_prisoner', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_eye_ik',
            target_name='automarker_head_last_prisoner', duration=1.5, smooth=True)
        t += 2
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_02, duration=3,
            time_scale=0.75, trans_time=1)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_prisoner2',
            target_name='automarker_prisoner2_head_ik', duration=25, transition_duration=1, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_prisoner2',
            target_name='automarker_prisoner2_eye_ik', duration=25, transition_duration=1, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_head_ik',
            target_name='automarker_head_syd_front', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_eye_ik',
            target_name='automarker_head_syd_front', duration=1.5, smooth=True)
        syd.facial(group=MAIN, index=65, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.25)


        # Реплика 70 · delta3 · исходное время 107 с
        # Сдается мне, ребята, что это очередная провокация Ордена, и выведет нас этот милый капитан на шеренгу
        # бойцов со штурмовыми винтовками.
        # Исходное окно facial: 0 с.
        t = 0
        voice_sound = self.lookup_single_sound(70)
        SoundEvent(root=self, group=MAIN, sound_name=voice_sound.get_nickname())
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_prisoner2_head_ik',
            target_name='automarker_head_last_prisoner', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_prisoner2_eye_ik',
            target_name='automarker_head_last_prisoner', duration=2, smooth=True)
        cam_delta3.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_delta3_marker',
            target_name='automarker_cam_delta3_marker_pos2', duration=10, smooth=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner2',
            anim=Male.Sc_MLBODY_CHRB_TWSTS_FROM_270LV_XA_03, duration=5, time_scale=0.7)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner2', anim=Male.GENERIC_ANIM, duration=15,
            trans_time=0.25)
        prisoner4.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=1)
        t += 3
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_prisoner2_head_ik',
            target_name='automarker_head_prisoner3', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_prisoner2_eye_ik',
            target_name='automarker_head_prisoner3', duration=1.25, smooth=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner2',
            anim=Male.Sc_MLBODY_CHRF_TALK_EMPH_000UP_A_18, duration=11, time_scale=0.8, trans_time=1)
        t += 1.5
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner2', anim=Male.GENERIC_ANIM, duration=15,
            time_scale=0.8, trans_time=0.25)
        t += 1.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_prisoner2_head_ik',
            target_name='automarker_head_last_prisoner', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_prisoner2_eye_ik',
            target_name='automarker_head_last_prisoner', duration=1.25, smooth=True)
        t += 3
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_prisoner2_head_ik',
            target_name='automarker_head_asf_captain', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_prisoner2_eye_ik',
            target_name='automarker_head_prisoner3', duration=1.25, smooth=True)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_prisoner4_head_ik',
            target_name='automarker_head_prisoner2', duration=0.01, smooth=True)
        main_group.append_time(11)


        # Реплика 80 · delta1 · исходное время 118 с
        # А у тебя что, есть предложения получше? В любом случае, лучше на шеренгу бойцов с винтовками, чем на
        # допрос к специалистам Ордена.
        # Исходное окно facial: 17 с.
        t = 0
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_delta1',
            target_name='automarker_prisoner4_head_ik', duration=4, transition_duration=1, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        cam_delta1.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_delta1', target_name='automarker_cam_delta1_pos2',
            duration=8, smooth=True)
        prisoner4.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_SHRG_SHLDRS_BIG_000LV_XA_03, duration=5,
            time_scale=0.7)
        t += 2
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_captain_sydanswer', 'automarker_cam_captain_sydanswer_marker'], duration=150, offset=[0, 0, 0],
            up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_syd_captside', 'automarker_cam_syd_captside_marker'], duration=150, offset=[0, 0, 0], up='Y_AXIS',
            front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_syd_clothesbox', 'automarker_cam_syd_clothesbox_marker'], duration=150, offset=[0, 0, 0],
            up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_asf_captain', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_asf_captain', duration=1, smooth=True)
        t += 2
        prisoner4.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_GESTR_180LV_XA_03, duration=5, time_scale=0.7,
            trans_time=0.5)
        t += 2
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_delta1',
            target_name='automarker_prisoner4_head_ik', duration=4, transition_duration=1, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=100, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_eye_ik',
            duration=25, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_syd', target_name='automarker_point_syd_inside',
            duration=0.001, smooth=False)
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=1)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_syd', target_name='automarker_syd_head_ik',
            duration=25, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_syd', target_name='automarker_syd_eye_ik',
            duration=25, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 1
        cam_trent.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_TWSTS_LOOK_270LV_XA_03, duration=5)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_syd', duration=2.2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_syd', duration=1.7, smooth=True)
        prisoner4.facial(group=MAIN, index=80, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-8)


        # Реплика 90 · trent · исходное время 127 с
        # А что там с артефактами, капитан?
        # Исходное окно facial: 15 с.
        t = 0
        t += 2.5
        cam_syd_trentside.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_head_ik',
            target_name='automarker_head_trent_upper', duration=1.75, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_eye_ik',
            target_name='automarker_head_trent', duration=1.25, smooth=True)
        trent.facial(group=MAIN, index=90, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-11.5)


        # Реплика 100 · syd · исходное время 130.5 с
        # Летят на базу Ордена.
        # Исходное окно facial: 4.2 с.
        t = 0
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_prisoner4_head_ik',
            target_name='automarker_head_syd', duration=0.01, smooth=True)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_delta1',
            target_name='automarker_prisoner4_head_ik', duration=25, transition_duration=1, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        syd.facial(group=MAIN, index=100, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.7)


        # Реплика 110 · delta1 · исходное время 133 с
        #  И вы позволили?
        # Исходное окно facial: 15 с.
        t = 0
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_SPCBODY_s002x_syd_XE_STND_000LV_11, duration=2, time_scale=1.5,
            start_time=2, trans_time=1)
        cam_captain_sydanswer.set(group=MAIN, time_delay=t)
        prisoner4.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_TWSTS_LOOK_090LV_XA_02, duration=5,
            time_scale=1.1, start_time=0.5)
        t += 1
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_MOTION_BREATHE_HEAVY_000LV_XA_, duration=4.444,
            time_scale=0.9, start_time=0.5, trans_time=0.5)
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=0.532, time_scale=0.1)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_head_ik',
            target_name='automarker_head_asf_captain_upper', duration=0.1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_eye_ik',
            target_name='automarker_head_asf_captain', duration=0.1, smooth=True)
        t += 1
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=4.444, time_scale=0.9,
            trans_time=0.5)
        cam_syd_captside.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_syd_captside',
            target_name='automarker_cam_syd_captside_pos2', duration=15, smooth=True)
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_SPCBODY_s002x_syd_XE_STND_000LV_11, duration=6, start_time=6.5)
        prisoner4.facial(group=MAIN, index=110, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-12.5)


        # Реплика 120 · syd · исходное время 135.5 с
        # А что я, по-вашему, должен был сделать? Если бы я начал вставлять Ордену палки в колеса, то сидел бы тут
        # с вами, только не с сигаретой в руке, а с таким же милым ошейником на шее как у вас.
        # Исходное окно facial: 17.5 с.
        t = 0
        t += 1.5
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_TALK_EMPH_000DN_A_20, duration=4, time_scale=0.5,
            loop=True, trans_time=2)
        t += 2.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_head_ik',
            target_name='automarker_head_trent_upper', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_eye_ik',
            target_name='automarker_head_trent', duration=1.5, smooth=True)
        t += 3.0
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, duration=7,
            time_scale=0.7, trans_time=1)
        t += 2.0
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_02, duration=3,
            time_scale=0.75, trans_time=1)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_head_ik',
            target_name='automarker_head_asf_captain_upper', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_eye_ik',
            target_name='automarker_head_asf_captain', duration=1.5, smooth=True)
        t += 4.0
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=4, time_scale=0.7,
            loop=True, trans_time=1)
        syd.facial(group=MAIN, index=120, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-4.0)


        # Реплика 130 · trent · исходное время 149 с
        # А как вы собираетесь помочь нам бежать?
        # Исходное окно facial: 15 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_head_ik',
            target_name='automarker_head_syd_front', duration=1, smooth=True)
        cam_trent.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=130, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-12)


        # Реплика 140 · syd · исходное время 152 с
        # Для начала вы примерите вот это...
        # Исходное окно facial: 9 с.
        t = 0
        cam_syd_clothesbox.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_syd_clothesbox',
            target_name='automarker_cam_syd_clothesbox_pos2', duration=8, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_syd_clothesbox_marker',
            target_name='automarker_cam_syd_clothesbox_marker_pos2', duration=8, smooth=True)
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_GESTR_RGHT_000LV_XA_02, duration=8, time_scale=0.5)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='panel1', target_name='automarker_panel1_pos_open',
            duration=5, smooth=True, adjust_orient=False)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='panel1', angle=-90, axis='Z_AXIS', duration=5,
            smooth=True)
        snd_close_door_clothesbox.start(group=MAIN, time_delay=t, duration=5, start_time=500)
        syd.facial(group=MAIN, index=140, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-5)


        # Реплика 145 · syd · исходное время 156 с
        # А потом спокойно и небрежно проследуете в ангар к кораблю мистера Трента.
        # Исходное окно facial: 10 с.
        t = 0
        snd_close_door_clothesbox.change_attenuation(group=MAIN, time_delay=t, duration=3, attenuation=-100)
        t += 2
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_syd', target_name='automarker_syd_head_ik',
            duration=25, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_syd', target_name='automarker_syd_eye_ik',
            duration=25, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_head_ik',
            target_name='automarker_head_trent_upper', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_eye_ik',
            target_name='automarker_head_trent', duration=1, smooth=True)
        syd.facial(group=MAIN, index=145, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-4)


        # Реплика 150 · syd · исходное время 162 с
        # К сожалению, все остальные уже разбирают на запчасти. А вот корабль Трента пока еще в целости и
        # сохранности. Так что, как говорится, в тесноте, да не в обиде.
        # Исходное окно facial: 16 с.
        t = 0
        cam_syd_captside.set(group=MAIN, time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_head_ik',
            target_name='automarker_head_asf_captain_upper', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_eye_ik',
            target_name='automarker_head_asf_captain', duration=1.6, smooth=True)
        t += 2.5
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, duration=7,
            time_scale=0.7, trans_time=1)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_head_ik',
            target_name='automarker_head_trent_upper', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_eye_ik',
            target_name='automarker_head_trent', duration=1.6, smooth=True)
        t += 1
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_02, duration=3,
            time_scale=0.75, trans_time=1)
        t += 3
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_head_ik',
            target_name='automarker_head_asf_captain_upper', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_eye_ik',
            target_name='automarker_head_asf_captain', duration=1.6, smooth=True)
        syd.facial(group=MAIN, index=150, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-4)


        # Реплика 160 · trent · исходное время 174 с
        # А после нашего побега... Как это скажется на вас? Вы не будете сидеть здесь не с сигаретой в руке, а с
        # ошейником как у нас на шее?
        # Исходное окно facial: 18 с.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=160, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-11)


        # Реплика 170 · syd · исходное время 181 с
        # О, нет. Вы же меня вырубили, этому найдутся неоспоримые доказательства.
        # Исходное окно facial: 9 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_head_ik',
            target_name='automarker_head_trent_upper', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_eye_ik',
            target_name='automarker_head_trent', duration=1.6, smooth=True)
        cam_syd_captside.set(group=MAIN, time_delay=t)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_head_ik',
            target_name='automarker_head_syd_front', duration=1.75, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_eye_ik',
            target_name='automarker_head_syd_front', duration=1.25, smooth=True)
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_SPCBODY_s002x_syd_XE_STND_000LV_11, duration=6, time_scale=1.5,
            start_time=1.3, trans_time=2.5)
        syd.facial(group=MAIN, index=170, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-3)


        # Реплика 180 · syd · исходное время 187 с
        # К тому же, что такое побег пленников в сравнении с тем, что я передал в руки  Ордена артефакты, за
        # которыми охотится весь сектор Сириуса.
        # Исходное окно facial: 15 с.
        t = 0
        t += 0.5
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_syd', target_name='automarker_syd_head_ik',
            duration=25, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_syd', target_name='automarker_syd_eye_ik',
            duration=25, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_head_ik',
            target_name='automarker_head_asf_captain_upper', duration=1.75, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_eye_ik',
            target_name='automarker_head_asf_captain', duration=1.25, smooth=True)
        t += 2
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_trent_finalword', 'automarker_cam_trent_finalword_marker'], duration=50, offset=[0, 0, 0],
            up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['cam_exit', 'automarker_cam_exit_marker'],
            duration=50, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT',
            flags='LOOK_AT')
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, duration=6, time_scale=0.6,
            trans_time=1)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_head_ik',
            target_name='automarker_head_trent_upper', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_eye_ik',
            target_name='automarker_head_trent', duration=1.5, smooth=True)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='vfx_rtc_cigaretteglow_4', target_name='offscreen',
            duration=0.001, smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='vfx_rtc_sydsmoke_3', target_name='offscreen',
            duration=0.001, smooth=False)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_head_ik',
            target_name='automarker_head_asf_captain_upper', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_eye_ik',
            target_name='automarker_head_asf_captain', duration=1.4, smooth=True)
        t += 3
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_delta1',
            target_name='automarker_point_prisoner4_stand', duration=0.001, smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner1',
            target_name='automarker_point_prisoner1_stand', duration=0.001, smooth=False)
        syd.facial(group=MAIN, index=180, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-4)


        # Реплика 190 · trent · исходное время 198 с
        # Толково, не поспоришь.
        # Исходное окно facial: 15 с.
        t = 0
        cam_trent_finalword.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_trent_finalword',
            target_name='automarker_cam_trent_finalword_pos2', duration=5, smooth=True)
        prisoner4.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=8)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner1',
            anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=8)
        t += 1
        prisoner4.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STROLL_000LV_XA_01, duration=8, loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner1',
            anim=Male.Sc_MLBODY_STROLL_000LV_XA_01, duration=8, loop=True)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_trent_front_upper', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_trent_front_upper', duration=1.4, smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_TWSTS_FROM_270LV_XA_03, duration=5, time_scale=0.7)
        t += 1.5
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['automarker_trent_head_ik', 'Char_prisoner1'],
            duration=4, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='Body_Head', target_type='PART',
            flags='POSITION+ORIENTATION')
        t += 2.5
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='Char_prisoner1', duration=3,
            transition_duration=1, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 1.9
        ambience_hall.change_attenuation(group=MAIN, time_delay=t, duration=0.1, attenuation=0)
        t += 0.1
        ambience_room.change_attenuation(group=MAIN, time_delay=t, duration=0.1, attenuation=-100)
        cam_exit.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_exit', target_name='automarker_cam_exit_pos2',
            duration=12, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_exit_marker',
            target_name='automarker_cam_exit_marker_pos2', duration=12, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent_classic',
            target_name='automarker_point_trent_classic', duration=0.001, smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner1b',
            target_name='automarker_point_prisoner1b', duration=0.001, smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner2b',
            target_name='automarker_point_prisoner2b', duration=0.001, smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner3b',
            target_name='automarker_point_prisoner3b', duration=0.001, smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner4b',
            target_name='automarker_point_prisoner4b', duration=0.001, smooth=False)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', target_name='offscreen', duration=0.001,
            smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_syd', target_name='offscreen', duration=0.001,
            smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner1', target_name='offscreen',
            duration=0.001, smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner2', target_name='offscreen',
            duration=0.001, smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_delta3', target_name='offscreen', duration=0.001,
            smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_delta1', target_name='offscreen', duration=0.001,
            smooth=False)
        t += 0.1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='body1', target_name='offscreen', duration=0.001,
            smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='body2', target_name='offscreen', duration=0.001,
            smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='body3', target_name='offscreen', duration=0.001,
            smooth=False)
        t += 0.1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='panel1', target_name='automarker_panel1_init_pos',
            duration=0.001, smooth=True)
        t += 0.8
        SourceMotionEvent(root=self, group=MAIN, time_delay=t, targets=['doors'], animation='Sc_cv_prison_cell',
            duration=3.332, time_scale=1, weight=1, trans_scale=1)
        snd_open_door.start(group=MAIN, time_delay=t, duration=10)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner1b',
            anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=25, start_time=0.5, loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner2b',
            anim=Male.Sc_MLBODY_WLKG_000LV_XB_01, duration=25, loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner3b',
            anim=Male.Sc_MLBODY_WLKG_000LV_XB_01, duration=25, start_time=0.5, loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner4b',
            anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=25, loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent_classic',
            anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=5.6, start_time=0.9, loop=True)
        t += 4
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner3b', angle=90, axis='Y_AXIS',
            duration=4, smooth=True)
        trent.facial(group=MAIN, index=190, append=True, auto_lip=True, extra_delay=0)
        t = 0
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner1b', angle=90, axis='Y_AXIS',
            duration=4, smooth=True)
        t += 0.6
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent_classic',
            anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=4)
        t += 0.4
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner2b', angle=90, axis='Y_AXIS',
            duration=4, smooth=True)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner4b', angle=90, axis='Y_AXIS',
            duration=4, smooth=True)
        t += 2
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent_classic',
            anim=Male.Sc_MLBODY_STND_LOOK_AROU_000LV_XA_09, duration=10, trans_time=0.5)
        t += 0.5
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent_classic',
            anim=Trent.Sc_MLHEAD_HAPPY_SMILE_SNEER_TRENT_000LV_XA_, duration=10, time_scale=0.7, trans_time=0.25)
        t += 2.7
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent_classic',
            anim=Trent.Sc_MLHEAD_MOTION_EYES_OPENBG_TRENT_000LV_XA_, duration=10, time_scale=0.7, trans_time=0.25)
        t += 5.8
        SourceMotionEvent(root=self, group=MAIN, time_delay=t, targets=['doors'], animation='Sc_cv_prison_cell',
            duration=3.332, start_time=3.332, time_scale=1, weight=1, trans_scale=1)
        snd_close_door.start(group=MAIN, time_delay=t, duration=10)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent_classic',
            anim=Male.Sc_MLBODY_STND_WALK_TRNS_270LV_XA_02, duration=10, trans_time=0.5)
        t += 2
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent_classic',
            anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=10, loop=True)
        main_group.append_time(17.0)
        preserve_spatial(self.get_entity('body1'), source_basis=[[0, 0, 0.8], [0, 1, 0], [-1, 0, 0]],
            reference_orientation=[0.7071068286895752, 2.9802322387695312e-08, 0.7071068286895752, -2.9802322387695312e-08])
        preserve_spatial(self.get_entity('body2'), source_basis=[[0, 0, 0.8], [0, 1, 0], [-1, 0, 0]],
            reference_orientation=[0.7071068286895752, 2.9802322387695312e-08, 0.7071068286895752, -2.9802322387695312e-08])
        preserve_spatial(self.get_entity('body3'), source_basis=[[0, 0, 0.8], [0, 1, 0], [-1, 0, 0]],
            reference_orientation=[0.7071068286895752, 2.9802322387695312e-08, 0.7071068286895752, -2.9802322387695312e-08])
        preserve_spatial(self.get_entity('prop_mask_trent'), source_basis=[[0, 0, 0.8], [0, 1, 0], [-1, 0, 0]],
            reference_orientation=[0.7071068286895752, 2.9802322387695312e-08, 0.7071068286895752, -2.9802322387695312e-08])
        preserve_spatial(self.get_entity('prop_mask_pris1'), source_basis=[[0, 0, 0.8], [0, 1, 0], [-1, 0, 0]],
            reference_orientation=[0.7071068286895752, 2.9802322387695312e-08, 0.7071068286895752, -2.9802322387695312e-08])
        preserve_spatial(self.get_entity('prop_mask_pris2'), source_basis=[[0, 0, 0.8], [0, 1, 0], [-1, 0, 0]],
            reference_orientation=[0.7071068286895752, 2.9802322387695312e-08, 0.7071068286895752, -2.9802322387695312e-08])
        preserve_spatial(self.get_entity('prop_mask_pris3'), source_basis=[[0, 0, 0.8], [0, 1, 0], [-1, 0, 0]],
            reference_orientation=[0.7071068286895752, 2.9802322387695312e-08, 0.7071068286895752, -2.9802322387695312e-08])
        preserve_spatial(self.get_entity('prop_mask_pris4'), source_basis=[[0, 0, 0.8], [0, 1, 0], [-1, 0, 0]],
            reference_orientation=[0.7071068286895752, 2.9802322387695312e-08, 0.7071068286895752, -2.9802322387695312e-08])
        preserve_spatial(self.get_entity('prop_mask_pris5'), source_basis=[[0, 0, 0.8], [0, 1, 0], [-1, 0, 0]],
            reference_orientation=[0.7071068286895752, 2.9802322387695312e-08, 0.7071068286895752, -2.9802322387695312e-08])


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M06PrisonNewScene
