"""m06_prison_new: полная постановка из master; точки в m06_prison_new.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Alchemy, AttachEvent, Character, ConnectHardpointEvent, EyeIkEvent, LookAtCamera, LookAtEvent, MAIN, Male, MotionEvent, MoveEvent, NeckIkEvent, Prop, RotateAxisEvent, Sound, StaticCamera,
)
from story.cutscenes.anim import (
    Male, Trent,
)
from story import actors


class DoorsProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'prison_doors'

class PropCigaretteProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'cigarette_3'

class Case1Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_prison_case'

class Panel1Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_prison_panel'

class Case2Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_prison_case'

class Panel2Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_prison_panel'

class Body1Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_prison_pirate_body1'

class Body2Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_prison_pirate_body2'

class Body3Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_prison_pirate_body1'

class PropMaskTrentProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_prison_neck_bomb'

class PropMaskPris1Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_prison_neck_bomb'

class PropMaskPris2Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_prison_neck_bomb'

class PropMaskPris3Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_prison_neck_bomb'

class PropMaskPris4Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_prison_neck_bomb'

class PropMaskPris5Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'm6_prison_neck_bomb'

class CharPrisoner1Actor(actors.Actor):
    NAME = 'prisoner1'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_asf_prisoner04'

class CharPrisoner3Actor(actors.Actor):
    NAME = 'prisoner3'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_asf_prisoner03'

class CharTrentClassicActor(actors.Actor):
    NAME = 'trent_classic'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'trent_original'

class CharPrisoner1bActor(actors.Actor):
    NAME = 'prisoner1b'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_asf_prisoner01b'

class CharPrisoner2bActor(actors.Actor):
    NAME = 'prisoner2b'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_asf_prisoner02b'

class CharPrisoner3bActor(actors.Actor):
    NAME = 'prisoner3b'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_asf_prisoner03b'

class CharPrisoner4bActor(actors.Actor):
    NAME = 'prisoner4b'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_asf_prisoner04b'


class M06PrisonNewScene(Scene):
    DUMP_FILE = 'm06_prison_new'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Персонажи, камеры, реквизит и звук.
        doors = DoorsProp(root=self, name='doors', light_group=9, init_point='doors', rotate_from_quat=True)
        prop_cigarette = PropCigaretteProp(root=self, name='prop_cigarette', light_group=9,
            init_point='prop_cigarette', rotate_from_quat=True)
        vfx_rtc_cigaretteglow_4 = Alchemy(root=self, name='vfx_rtc_cigaretteglow_4',
            particles='rtc_cigaretteglow', point_name='vfx_rtc_cigaretteglow_4', sparam=0, light_group=0,
            sort_group=0, hidden=False, use_ambient=True)
        vfx_rtc_sydsmoke_3 = Alchemy(root=self, name='vfx_rtc_sydsmoke_3', particles='rtc_sydsmoke',
            point_name='vfx_rtc_sydsmoke_3', sparam=0, light_group=0, sort_group=0, hidden=False, use_ambient=True)
        case1 = Case1Prop(root=self, name='case1', light_group=9, init_point='case1', rotate_from_quat=True)
        panel1 = Panel1Prop(root=self, name='panel1', light_group=9, init_point='panel1', rotate_from_quat=True)
        case2 = Case2Prop(root=self, name='case2', light_group=9, init_point='case2', rotate_from_quat=True)
        panel2 = Panel2Prop(root=self, name='panel2', light_group=9, init_point='panel2', rotate_from_quat=True)
        body1 = Body1Prop(root=self, name='body1', light_group=9, init_point='body1', rotate_from_quat=True)
        body2 = Body2Prop(root=self, name='body2', light_group=9, init_point='body2', rotate_from_quat=True)
        body3 = Body3Prop(root=self, name='body3', light_group=9, init_point='body3', rotate_from_quat=True)
        prop_mask_trent = PropMaskTrentProp(root=self, name='prop_mask_trent', light_group=9,
            init_point='prop_mask_trent', rotate_from_quat=True)
        prop_mask_pris1 = PropMaskPris1Prop(root=self, name='prop_mask_pris1', light_group=9,
            init_point='prop_mask_pris1', rotate_from_quat=True)
        prop_mask_pris2 = PropMaskPris2Prop(root=self, name='prop_mask_pris2', light_group=9,
            init_point='prop_mask_pris2', rotate_from_quat=True)
        prop_mask_pris3 = PropMaskPris3Prop(root=self, name='prop_mask_pris3', light_group=9,
            init_point='prop_mask_pris3', rotate_from_quat=True)
        prop_mask_pris4 = PropMaskPris4Prop(root=self, name='prop_mask_pris4', light_group=9,
            init_point='prop_mask_pris4', rotate_from_quat=True)
        prop_mask_pris5 = PropMaskPris5Prop(root=self, name='prop_mask_pris5', light_group=9,
            init_point='prop_mask_pris5', rotate_from_quat=True)
        ambience_hall = Sound(root=self, name='ambience_hall', sound='ambience_deck_space_smaller', attenuation=0,
            dmin=50, dmax=300, priority='Story_Sound_1')
        ambience_room = Sound(root=self, name='ambience_room', sound='ambience_deck_space_larger',
            attenuation=-1000000, dmin=50, dmax=300, priority='Story_Sound_1')
        step1 = Sound(root=self, name='step1', sound='fs_ml_steel04', attenuation=-45, dmin=50, dmax=300,
            priority='Story_Sound_1')
        step2 = Sound(root=self, name='step2', sound='fs_ml_steel01', attenuation=-45, dmin=50, dmax=300,
            priority='Story_Sound_1')
        step3 = Sound(root=self, name='step3', sound='fs_ml_steel03', attenuation=-45, dmin=50, dmax=300,
            priority='Story_Sound_1')
        step1_cmdr = Sound(root=self, name='step1_cmdr', sound='fs_ml_steel04', attenuation=-20, dmin=50,
            dmax=300, priority='Story_Sound_1')
        step2_cmdr = Sound(root=self, name='step2_cmdr', sound='fs_ml_steel01', attenuation=-20, dmin=50,
            dmax=300, priority='Story_Sound_1')
        step3_cmdr = Sound(root=self, name='step3_cmdr', sound='fs_ml_steel03', attenuation=-20, dmin=50,
            dmax=300, priority='Story_Sound_1')
        snd_open_door = Sound(root=self, name='snd_open_door', sound='depot_open_sound', attenuation=0, dmin=50,
            dmax=300, priority='Story_Sound_1')
        snd_close_door = Sound(root=self, name='snd_close_door', sound='depot_close_sound', attenuation=0,
            dmin=50, dmax=300, priority='Story_Sound_1')
        snd_close_door_clothesbox = Sound(root=self, name='snd_close_door_clothesbox', sound='depot_close_sound',
            attenuation=-5, dmin=50, dmax=300, priority='Story_Sound_1')
        prisoner1 = Character(root=self, actor=CharPrisoner1Actor, name='Char_prisoner1', light_group=9,
            init_point='Char_prisoner1', rotate_from_quat=True, appearance='m06_asf_prisoner04',
            actor_name='Prisoner1')
        prisoner2 = Character(root=self, actor=actors.DeltaThree, name='Char_prisoner2', light_group=9,
            init_point='Char_prisoner2', rotate_from_quat=True, appearance='m06_asf_prisoner02',
            actor_name='Prisoner2')
        prisoner3 = Character(root=self, actor=CharPrisoner3Actor, name='Char_prisoner3', light_group=9,
            init_point='Char_prisoner3', rotate_from_quat=True, appearance='m06_asf_prisoner03',
            actor_name='Prisoner3')
        prisoner4 = Character(root=self, actor=actors.DeltaOne, name='Char_prisoner4', light_group=9,
            init_point='Char_prisoner4', rotate_from_quat=True, appearance='m06_asf_prisoner01',
            actor_name='Prisoner4')
        commander = Character(root=self, actor=actors.OrderGuard, name='Char_commander', light_group=9,
            init_point='Char_commander', rotate_from_quat=True, appearance='m06_gunner_leader',
            actor_name='Gunner_commander')
        syd = Character(root=self, actor=actors.Ceed, name='Char_syd', light_group=9, init_point='Char_syd',
            rotate_from_quat=True, appearance='syd', actor_name='Syd')
        trent = Character(root=self, actor=actors.Trent, name='Char_trent', light_group=9,
            init_point='Char_trent', rotate_from_quat=True, appearance='trent', actor_name='Player')
        trent_classic = Character(root=self, actor=CharTrentClassicActor, name='Char_trent_classic',
            light_group=9, init_point='Char_trent_classic', rotate_from_quat=True, appearance='trent_original',
            actor_name='TrentOriginal')
        prisoner1b = Character(root=self, actor=CharPrisoner1bActor, name='Char_prisoner1b', light_group=9,
            init_point='Char_prisoner1b', rotate_from_quat=True, appearance='m06_asf_prisoner01b',
            actor_name='Prisoner1b')
        prisoner2b = Character(root=self, actor=CharPrisoner2bActor, name='Char_prisoner2b', light_group=9,
            init_point='Char_prisoner2b', rotate_from_quat=True, appearance='m06_asf_prisoner02b',
            actor_name='Prisoner2b')
        prisoner3b = Character(root=self, actor=CharPrisoner3bActor, name='Char_prisoner3b', light_group=9,
            init_point='Char_prisoner3b', rotate_from_quat=True, appearance='m06_asf_prisoner03b',
            actor_name='Prisoner3b')
        prisoner4b = Character(root=self, actor=CharPrisoner4bActor, name='Char_prisoner4b', light_group=9,
            init_point='Char_prisoner4b', rotate_from_quat=True, appearance='m06_asf_prisoner04b',
            actor_name='Prisoner4b')
        cam_start_outside = LookAtCamera(root=self, name='cam_start_outside', fov=35, look_duration=70)
        cam_start_inside = LookAtCamera(root=self, name='cam_start_inside', fov=30, look_duration=70)
        cam_syd_appear = LookAtCamera(root=self, name='cam_syd_appear', fov=25, look_duration=70)
        cam_salut = LookAtCamera(root=self, name='cam_salut', fov=25, look_duration=70)
        cam_syd_gives_order = LookAtCamera(root=self, name='cam_syd_gives_order', fov=25, look_duration=70)
        cam_syd_order = LookAtCamera(root=self, name='cam_syd_order', fov=25, look_duration=70)
        cam_syd_opendoor = StaticCamera(root=self, name='cam_syd_opendoor', fov=20)
        cam_syd_doorclosed = StaticCamera(root=self, name='cam_syd_doorclosed', fov=15)
        cam_sydgreet_begin = StaticCamera(root=self, name='cam_sydgreet_begin', fov=15)
        cam_sydgreet_captapprove = StaticCamera(root=self, name='cam_sydgreet_captapprove', fov=15)
        cam_syd_reveal = StaticCamera(root=self, name='cam_syd_reveal', fov=15)
        cam_trent = StaticCamera(root=self, name='cam_trent', fov=15)
        cam_syd_trentside = StaticCamera(root=self, name='cam_syd_trentside', fov=15)
        cam_captain_sydanswer = StaticCamera(root=self, name='cam_captain_sydanswer', fov=15)
        cam_syd_captside = StaticCamera(root=self, name='cam_syd_captside', fov=16)
        cam_syd_clothesbox = StaticCamera(root=self, name='cam_syd_clothesbox', fov=15)
        cam_delta3 = StaticCamera(root=self, name='cam_delta3', fov=15)
        cam_delta1 = StaticCamera(root=self, name='cam_delta1', fov=15)
        cam_trent_finalword = StaticCamera(root=self, name='cam_trent_finalword', fov=15)
        cam_exit = StaticCamera(root=self, name='cam_exit', fov=20)

        # Исходные точки взгляда.

        # Вход.
        t = 0
        ConnectHardpointEvent(root=self, group=MAIN, target_name=prop_mask_trent.name, parent_name=trent.name,
            duration=1000, target_hardpoint='hp_neck_connect', parent_hardpoint='hp_head_top_conn', time_delay=t)
        ConnectHardpointEvent(root=self, group=MAIN, target_name=prop_mask_pris1.name, parent_name=prisoner1.name,
            duration=1000, target_hardpoint='hp_neck_connect', parent_hardpoint='hp_head_top_conn', time_delay=t)
        ConnectHardpointEvent(root=self, group=MAIN, target_name=prop_mask_pris2.name, parent_name=prisoner2.name,
            duration=1000, target_hardpoint='hp_neck_connect', parent_hardpoint='hp_head_top_conn', time_delay=t)
        ConnectHardpointEvent(root=self, group=MAIN, target_name=prop_mask_pris3.name, parent_name=prisoner3.name,
            duration=1000, target_hardpoint='hp_neck_connect', parent_hardpoint='hp_head_top_conn', time_delay=t)
        ConnectHardpointEvent(root=self, group=MAIN, target_name=prop_mask_pris4.name, parent_name=prisoner4.name,
            duration=1000, target_hardpoint='hp_neck_connect', parent_hardpoint='hp_head_top_conn', time_delay=t)
        ambience_hall.start(group=MAIN, duration=5000, loop=True, start_time=0, time_delay=t)
        ambience_room.start(group=MAIN, duration=5000, loop=True, start_time=0, time_delay=t)
        cam_start_outside.set(group=MAIN, time_delay=t)
        cam_start_outside.move_cam(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        cam_start_outside.move_focus(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        commander.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_STRCH_YAWN_000LV_XA_06, duration=11, loop=True,
            time_delay=t)
        t += 9.9
        ambience_hall.change_attenuation(group=MAIN, duration=0.1, attenuation=-100, time_delay=t)
        t += 0.1
        ambience_room.change_attenuation(group=MAIN, duration=0.1, attenuation=0, time_delay=t)
        cam_start_inside.set(group=MAIN, time_delay=t)
        cam_start_inside.move_cam(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        cam_start_inside.move_focus(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=prisoner3.name,
            anim=Male.Sc_MLBODY_CHRB_TWSTU_CCL_LESS_000LV_A_14, duration=20, time_delay=t)
        prisoner4.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_HEAD_HOLDR_000LV_XA_03, duration=20, time_delay=t)
        t += 4
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_LOOK_AROU_CASL_000LV_XA_04, duration=20, time_scale=0.8,
            time_delay=t)
        t += 2
        prisoner2.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_BIG_000LV_XA_05, duration=20, loop=True,
            time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=prisoner1.name,
            anim=Male.Sc_MLBODY_CHRB_LOOK_AROU_CASL_000LV_XA_04, duration=20, time_delay=t)
        t += 1
        prisoner4.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_HOLD_HEAD_RLEASE_000LV_XA_03, duration=20,
            time_scale=0.7, time_delay=t)
        t += 4
        commander.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_BEND_FOTR_SWNGARMS_000DN_XA_12, duration=11,
            trans_time=1, loop=True, time_delay=t)
        t += 0.9
        ambience_hall.change_attenuation(group=MAIN, duration=0.1, attenuation=0, time_delay=t)
        t += 0.1
        ambience_room.change_attenuation(group=MAIN, duration=0.1, attenuation=-100, time_delay=t)
        cam_syd_appear.set(group=MAIN, time_delay=t)
        cam_syd_appear.move_cam(group=MAIN, index=2, duration=6, smooth=True, time_delay=t)
        cam_syd_appear.move_focus(group=MAIN, index=2, duration=6, smooth=True, time_delay=t)
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=7.9999, loop=True, time_delay=t)
        t += 0.7
        step1.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.3
        step1.change_attenuation(group=MAIN, duration=3, attenuation=-15, time_delay=t)
        step2.change_attenuation(group=MAIN, duration=3, attenuation=-15, time_delay=t)
        step3.change_attenuation(group=MAIN, duration=3, attenuation=-15, time_delay=t)
        t += 0.4
        step2.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.6
        RotateAxisEvent(root=self, group=MAIN, object_name=syd.name, angle=-15, axis='Y_AXIS', duration=5.99,
            smooth=True, time_delay=t)
        t += 0.1
        step3.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.7
        step2.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.7
        step1.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.7
        step3.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.5
        step1.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.6
        step2.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.6
        step3.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.1
        step1.change_attenuation(group=MAIN, duration=3, attenuation=-30, time_delay=t)
        step2.change_attenuation(group=MAIN, duration=3, attenuation=-30, time_delay=t)
        step3.change_attenuation(group=MAIN, duration=3, attenuation=-30, time_delay=t)
        commander.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_TURN_270LV_XA_04, duration=5, time_delay=t)
        t += 0.6
        step1.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.65
        commander.motion(group=MAIN, anim=Male.Sc_MLHEAD_SURPRSE_000LV_XA_, duration=5, trans_time=0.25,
            time_delay=t)
        t += 0.05
        step3.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.7
        step2.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        cam_syd_order.set(group=MAIN, time_delay=t)
        cam_syd_order.move_cam(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        cam_syd_order.move_focus(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=syd.name,
            target_name=self.get_automarker_name('point_syd_around_commander'), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.01
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=6, time_scale=0.85,
            time_delay=t)
        t += 0.69
        step3.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.3
        commander.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_SALUT_000LV_XA_03, duration=5, trans_time=0.25,
            time_delay=t)
        t += 0.4
        step3.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        main_group.append_time(32)

        # m06_order_prison 10: Ceed.
        # Вольно, рядовой. Идите в диспетчерскую, пусть подготовят корабль для доставки пленных на нашу базу.
        # А я пока начну допрос.
        t = 0
        ambience_hall.change_attenuation(group=MAIN, duration=0.1, attenuation=-2, time_delay=t)
        t += 1
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_GESTR_180LV_XA_02, duration=6, time_scale=0.6,
            trans_time=1, time_delay=t)
        t += 2
        step1.change_attenuation(group=MAIN, duration=3, attenuation=-20, time_delay=t)
        step2.change_attenuation(group=MAIN, duration=3, attenuation=-20, time_delay=t)
        step3.change_attenuation(group=MAIN, duration=3, attenuation=-20, time_delay=t)
        t += 2
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_ATEASE_HSEC_RLEASE_000LV_XA_03, duration=6,
            time_scale=0.54, trans_time=1, time_delay=t)
        t += 3.5
        commander.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_HNDS_CASL_000LV_xa_04, duration=3,
            time_scale=0.8, trans_time=2, time_delay=t)
        syd.facial(group=MAIN, index=10, auto_lip=True, extra_delay=0)

        # m06_order_prison 20: OrderGuard.
        # Сэр, но если...
        t = 0
        cam_salut.set(group=MAIN, time_delay=t)
        commander.facial(group=MAIN, index=20, auto_lip=True, extra_delay=0)

        # m06_order_prison 30: Ceed.
        # Никаких если. На них же шокеры, пусть только попробуют рыпнуться.
        t = 0
        cam_syd_gives_order.set(group=MAIN, time_delay=t)
        t += 1
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_ATEASE_RLEASE_000LV_XA_01, duration=6, time_scale=0.6,
            trans_time=1, time_delay=t)
        t += 0.5
        commander.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_HNDSDN_TRNS_000LV_XA_01, duration=4,
            time_scale=0.8, trans_time=1, time_delay=t)
        t += 1.5
        cam_salut.move_cam(group=MAIN, index=2, duration=1, smooth=True, time_delay=t)
        cam_salut.move_focus(group=MAIN, index=2, duration=1, smooth=True, time_delay=t)
        t += 1
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=3, trans_time=1, loop=True,
            time_delay=t)
        t += 1
        commander.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_SALUT_000LV_XA_03, duration=5, time_scale=1.3,
            trans_time=0.25, time_delay=t)
        cam_salut.set(group=MAIN, time_delay=t)
        cam_salut.move_cam(group=MAIN, index=3, duration=12, smooth=True, time_delay=t)
        cam_salut.move_focus(group=MAIN, index=3, duration=10, smooth=True, time_delay=t)
        syd.facial(group=MAIN, index=30, auto_lip=True, extra_delay=0)

        # m06_order_prison 40: OrderGuard.
        # Есть, сэр.
        t = 0.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_eye_ik'),
            target_name=self.get_automarker_name('head_syd_front'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 1
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_1STEP_BKWD_PVOTL_270LV_XA_06, duration=6, trans_time=1,
            time_delay=t)
        t += 0.5
        RotateAxisEvent(root=self, group=MAIN, object_name=commander.name, angle=-25, axis='Y_AXIS', duration=1,
            smooth=True, time_delay=t)
        t += 0.2
        commander.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01, duration=5, trans_time=0.25,
            time_delay=t)
        t += 0.8
        RotateAxisEvent(root=self, group=MAIN, object_name=commander.name, angle=25, axis='Y_AXIS', duration=2,
            smooth=True, time_delay=t)
        t += 0.2
        step1_cmdr.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.05
        commander.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=55, loop=True, time_delay=t)
        t += 0.65
        step2_cmdr.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        commander.facial(group=MAIN, index=40, auto_lip=True, extra_delay=0)
        # Действие после исходного окна реплики.
        t = 0.5
        step1_cmdr.change_attenuation(group=MAIN, duration=5, attenuation=-50, time_delay=t)
        step2_cmdr.change_attenuation(group=MAIN, duration=5, attenuation=-50, time_delay=t)
        step3_cmdr.change_attenuation(group=MAIN, duration=5, attenuation=-50, time_delay=t)
        t += 0.1
        step3_cmdr.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.4
        RotateAxisEvent(root=self, group=MAIN, object_name=commander.name, angle=90, axis='Y_AXIS', duration=2.5,
            smooth=True, time_delay=t)
        t += 0.3
        step2_cmdr.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.7
        step1_cmdr.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.7
        step3_cmdr.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.3
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01, duration=5, trans_time=0.25,
            time_delay=t)
        t += 0.2
        step1_cmdr.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.6
        step2_cmdr.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.25
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=3.4499, loop=True, time_delay=t)
        t += 0.15
        step1.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.2
        step3_cmdr.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.5
        step2.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.2
        step1_cmdr.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.5
        step3.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.2
        step3_cmdr.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.5
        step2.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.2
        step2_cmdr.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.5
        step1.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.2
        step3_cmdr.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.3
        LookAtEvent(root=self, group=MAIN, point=cam_syd_opendoor.name,
            focus=self.get_automarker_name('cam_syd_opendoor_marker'), duration=50, target_type='ROOT',
            target_part='', up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        LookAtEvent(root=self, group=MAIN, point=cam_syd_doorclosed.name,
            focus=self.get_automarker_name('cam_syd_doorclosed_marker'), duration=50, target_type='ROOT',
            target_part='', up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        LookAtEvent(root=self, group=MAIN, point=cam_sydgreet_begin.name,
            focus=self.get_automarker_name('cam_sydgreet_begin_marker'), duration=150, target_type='ROOT',
            target_part='', up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        LookAtEvent(root=self, group=MAIN, point=cam_sydgreet_captapprove.name,
            focus=self.get_automarker_name('cam_sydgreet_captapprove_marker'), duration=150, target_type='ROOT',
            target_part='', up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        LookAtEvent(root=self, group=MAIN, point=cam_syd_reveal.name,
            focus=self.get_automarker_name('cam_syd_reveal_marker'), duration=150, target_type='ROOT',
            target_part='', up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        LookAtEvent(root=self, group=MAIN, point=cam_trent.name,
            focus=self.get_automarker_name('cam_trent_marker'), duration=50, target_type='ROOT', target_part='',
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        LookAtEvent(root=self, group=MAIN, point=cam_syd_trentside.name,
            focus=self.get_automarker_name('cam_syd_trentside_marker'), duration=150, target_type='ROOT',
            target_part='', up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        cam_syd_opendoor.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=cam_syd_opendoor.name,
            target_name=self.get_automarker_name('cam_syd_opendoor_pos2'), duration=10, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=syd.name,
            target_name=self.get_automarker_name('point_syd_walk_to_doors'), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=3, start_time=0.9, loop=True,
            time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=syd.name, angle=-45, axis='Y_AXIS', duration=1,
            smooth=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=25, loop=True, time_delay=t)
        prisoner2.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=25, loop=True,
            time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=prisoner3.name, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05,
            duration=2, time_delay=t)
        prisoner4.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=2, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=prisoner1.name, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05,
            duration=2, time_delay=t)
        t += 0.2
        step3.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.2
        step3_cmdr.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.3
        step1.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.6
        step2.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.6
        step3.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.7
        step1.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.4
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=4, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=syd.name, angle=-45, axis='Y_AXIS', duration=2,
            smooth=True, time_delay=t)
        t += 0.3
        step3.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.7
        step2.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.7
        step3.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.6
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WAVE_LHND_000LV_XA_02, duration=8, trans_time=0.5,
            time_delay=t)
        t += 1.7
        snd_open_door.start(group=MAIN, duration=10, loop=False, start_time=0, time_delay=t)
        t += 0.2
        MotionEvent(root=self, group=MAIN, object_name=prisoner1.name,
            anim=Male.Sc_MLBODY_CHRB_TWSTS_LOOK_090LV_XA_02, duration=5, time_scale=0.8, time_delay=t)
        t += 0.1
        MotionEvent(root=self, group=MAIN, object_name=doors.name, anim='Sc_cv_prison_cell', duration=3.332,
            trans_scale=1, time_delay=t)
        t += 0.2
        prisoner4.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_TWSTS_LOOK_090LV_XA_02, duration=5, time_scale=0.8,
            time_delay=t)
        t += 0.3
        prisoner2.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_TWSTS_LOOK_270LV_XA_03, duration=5, time_scale=0.8,
            time_delay=t)
        t += 0.2
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01, duration=4, trans_time=1,
            time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=prisoner1.name, target_name=syd.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=6, transition_duration=3,
            time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=prisoner2.name,
            target_name=self.get_automarker_name('prisoner2_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=20, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=prisoner2.name,
            target_name=self.get_automarker_name('prisoner2_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=20, transition_duration=1, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_TWSTS_LOOK_270LV_XA_03, duration=5, time_scale=0.6,
            time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=prisoner2.name,
            target_name=self.get_automarker_name('prisoner2_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=25, transition_duration=1, time_delay=t)
        t += 0.5
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name, target_name=syd.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=10, transition_duration=4,
            time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=prisoner4.name, target_name=syd.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=5, transition_duration=2.5,
            time_delay=t)
        t += 0.5
        NeckIkEvent(root=self, group=MAIN, char_name=prisoner3.name, target_name=syd.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=6, transition_duration=2,
            time_delay=t)
        t += 0.12
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=4, time_delay=t)
        t += 1.48
        MotionEvent(root=self, group=MAIN, object_name=doors.name, anim='Sc_cv_prison_cell', duration=3.332,
            start_time=3.332, trans_scale=1, time_delay=t)
        snd_close_door.start(group=MAIN, duration=10, loop=False, start_time=0, time_delay=t)
        t += 0.9
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_LOOK_AROU_CASL_000LV_XA_08, duration=8, trans_time=1,
            time_delay=t)
        t += 0.5
        snd_close_door.change_attenuation(group=MAIN, duration=0.1, attenuation=-2, time_delay=t)
        ambience_hall.change_attenuation(group=MAIN, duration=2, attenuation=-100, time_delay=t)
        ambience_room.change_attenuation(group=MAIN, duration=2, attenuation=0, time_delay=t)
        cam_sydgreet_begin.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=cam_sydgreet_begin.name,
            target_name=self.get_automarker_name('cam_sydgreet_begin_pos2'), duration=5.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('cam_sydgreet_begin_marker'),
            target_name=self.get_automarker_name('cam_sydgreet_begin_marker_pos2'), duration=5.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 1.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('prisoner2_head_ik'),
            target_name=self.get_automarker_name('head_asf_captain_p2_near'), duration=2.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('prisoner2_eye_ik'),
            target_name=self.get_automarker_name('head_asf_captain'), duration=1.25, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 0.5
        prisoner2.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_TWSTS_FROM_270LV_XA_03, duration=2.5,
            time_scale=0.2, time_delay=t)
        t += 1.5
        MotionEvent(root=self, group=MAIN, object_name=prisoner1.name,
            anim=Male.Sc_MLBODY_CHRB_IDLE_BIG_000LV_XA_05, duration=2, loop=True, time_delay=t)
        t += 0.5
        MotionEvent(root=self, group=MAIN, object_name=prisoner3.name,
            anim=Male.Sc_MLBODY_CHRB_TWSTU_CCL_LESS_000LV_A_14, duration=8, time_delay=t)
        t += 0.5
        MotionEvent(root=self, group=MAIN, object_name=prisoner1.name,
            anim=Male.Sc_MLBODY_CHRB_SHRG_SHLDRS_SMALL_000LV_XA_03, duration=11, time_scale=0.4, trans_time=1,
            time_delay=t)
        t += 0.5
        NeckIkEvent(root=self, group=MAIN, char_name=prisoner2.name,
            target_name=self.get_automarker_name('prisoner2_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=25, transition_duration=1, time_delay=t)
        t += 0.5
        cam_sydgreet_captapprove.set(group=MAIN, time_delay=t)
        prisoner4.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=1, start_time=2,
            time_delay=t)
        t += 0.5
        prisoner4.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_YESS_000LV_A_01, duration=4, time_scale=0.6,
            trans_time=0.25, time_delay=t)
        t += 0.1
        prisoner4.motion(group=MAIN, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=1, time_scale=0.3,
            trans_time=0.25, time_delay=t)
        main_group.append_time(27.5)

        # m06_order_prison 50: Ceed.
        # Спокойно, джентльмены, я не кусаюсь. Вам повезло, что все произошло во время моего дежурства.
        t = 0
        LookAtEvent(root=self, group=MAIN, point=cam_delta3.name,
            focus=self.get_automarker_name('cam_delta3_marker'), duration=50, target_type='ROOT', target_part='',
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        LookAtEvent(root=self, group=MAIN, point=cam_delta1.name,
            focus=self.get_automarker_name('cam_delta1_marker'), duration=50, target_type='ROOT', target_part='',
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('prisoner2_head_ik'),
            target_name=self.get_automarker_name('head_asf_captain_p2_near'), duration=2, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('prisoner2_eye_ik'),
            target_name=self.get_automarker_name('head_asf_captain'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        prisoner4.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_TWSTS_LOOK_090LV_XA_02, duration=5, time_scale=0.5,
            trans_time=1, time_delay=t)
        prisoner4.motion(group=MAIN, anim=Male.Sc_MLHEAD_SURPRSE_QUZZCLLY_000LV_XA_, duration=1, time_scale=0.8,
            trans_time=0.25, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=prisoner4.name, target_name=syd.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=10, transition_duration=2,
            time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=prisoner3.name, target_name=syd.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=10, transition_duration=2,
            time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=syd.name,
            target_name=self.get_automarker_name('syd_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=11.8, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=syd.name, target_name=self.get_automarker_name('syd_eye_ik'),
            target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', duration=11.8,
            transition_duration=1, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_head_ik'),
            target_name=self.get_automarker_name('head_prisoner2'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_eye_ik'),
            target_name=self.get_automarker_name('head_prisoner2'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=vfx_rtc_sydsmoke_3.name, parent_name=prop_cigarette.name,
            duration=110, target_part='hp_cigarette_tip_smoke', target_type='HARDPOINT', adjust_pos=True,
            adjust_orient=False, up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=vfx_rtc_cigaretteglow_4.name,
            parent_name=prop_cigarette.name, duration=110, target_part='hp_cigarette_tip_smoke',
            target_type='HARDPOINT', adjust_pos=True, adjust_orient=True, up='Y_AXIS', front='NEG_Z_AXIS',
            time_delay=t)
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_GESTR_NO_000LV_XA_02, duration=5, time_scale=0.7,
            time_delay=t)
        t += 0.5
        MotionEvent(root=self, group=MAIN, object_name=prisoner1.name,
            anim=Male.Sc_MLBODY_CHRB_TWSTS_LOOK_090LV_XA_02, duration=5, time_scale=0.5, trans_time=1,
            time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=prisoner1.name, target_name=syd.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=10, transition_duration=2,
            time_delay=t)
        t += 1.5
        cam_syd_reveal.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=cam_syd_reveal.name,
            target_name=self.get_automarker_name('cam_syd_reveal_pos2'), duration=18, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('cam_syd_reveal_marker'),
            target_name=self.get_automarker_name('cam_syd_reveal_marker_pos2'), duration=18, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_head_ik'),
            target_name=self.get_automarker_name('head_asf_captain'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_eye_ik'),
            target_name=self.get_automarker_name('head_asf_captain'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 1
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_ATEASE_HSEC_RLEASE_000LV_XA_03, duration=5,
            time_scale=0.8, trans_time=1, time_delay=t)
        t += 3
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_head_ik'),
            target_name=self.get_automarker_name('head_last_prisoner'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_eye_ik'),
            target_name=self.get_automarker_name('head_last_prisoner'), duration=1.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        syd.facial(group=MAIN, index=50, auto_lip=True, extra_delay=0)

        # m06_order_prison 60: Ceed.
        # Забыл представиться. Хари Сид, капитан Ордена, лейтенант СБА, работаю тут под прикрытием.
        t = 1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_head_ik'),
            target_name=self.get_automarker_name('head_syd_front'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_eye_ik'),
            target_name=self.get_automarker_name('head_syd_front'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_ATEASE_RLEASE_000LV_XA_01, duration=5, time_scale=0.6,
            trans_time=1, time_delay=t)
        t += 2.8
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_GIVE_VEND_000LV_B_07, duration=5, time_scale=0.5,
            trans_time=0.5, time_delay=t)
        t += 1.2
        vfx_rtc_cigaretteglow_4.start(group=MAIN, duration=106, time_delay=t)
        t += 0.5
        ConnectHardpointEvent(root=self, group=MAIN, target_name=prop_cigarette.name, parent_name=syd.name,
            duration=500, target_hardpoint='hprightconnect_cigarette', parent_hardpoint='hprightconnect',
            time_delay=t)
        syd.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_POINT_RGHT_MILI_000LV_00, duration=3, time_delay=t)
        t += 0.9
        syd.motion(group=MAIN, anim=Male.Sc_SPCBODY_s002x_syd_XE_STND_000LV_11, duration=6, time_scale=1.5,
            start_time=1.3, trans_time=2.5, time_delay=t)
        t += 1.6
        vfx_rtc_sydsmoke_3.start(group=MAIN, duration=106, time_delay=t)
        t += 0.4
        syd.motion(group=MAIN, anim=Male.Sc_MLHEAD_MOTION_BREATHE_HEAVY_000LV_XA_, duration=4.444, time_scale=0.9,
            start_time=0.5, trans_time=0.5, time_delay=t)
        syd.motion(group=MAIN, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=0.532, time_scale=0.1,
            time_delay=t)
        syd.facial(group=MAIN, index=60, auto_lip=True, extra_delay=0)
        # Действие после исходного окна реплики.
        t = 0.9
        syd.motion(group=MAIN, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=4.444, time_scale=0.9,
            trans_time=0.5, time_delay=t)
        main_group.append_time(2.5)

        # m06_order_prison 65: Ceed.
        # Сейчас подождем некоторое время, а потом я помогу вам покинуть негостеприимный борт Навуходоносора
        t = 0
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, duration=7, time_scale=0.7,
            trans_time=1, time_delay=t)
        t += 0.2
        NeckIkEvent(root=self, group=MAIN, char_name=syd.name,
            target_name=self.get_automarker_name('syd_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=25, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=syd.name, target_name=self.get_automarker_name('syd_eye_ik'),
            target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', duration=25,
            transition_duration=1, time_delay=t)
        t += 0.8
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_head_ik'),
            target_name=self.get_automarker_name('head_prisoner2_around'), duration=3, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_eye_ik'),
            target_name=self.get_automarker_name('head_prisoner2'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('prisoner2_head_ik'),
            target_name=self.get_automarker_name('head_syd'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('prisoner2_eye_ik'),
            target_name=self.get_automarker_name('head_syd'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 1
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_RHND_CASL_000LV_xa_01, duration=6, time_scale=0.75,
            trans_time=1, loop=True, time_delay=t)
        t += 2
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_head_ik'),
            target_name=self.get_automarker_name('head_last_prisoner'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_eye_ik'),
            target_name=self.get_automarker_name('head_last_prisoner'), duration=1.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 2
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_02, duration=3, time_scale=0.75,
            trans_time=1, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=prisoner2.name,
            target_name=self.get_automarker_name('prisoner2_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=25, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=prisoner2.name,
            target_name=self.get_automarker_name('prisoner2_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=25, transition_duration=1, time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_head_ik'),
            target_name=self.get_automarker_name('head_syd_front'), duration=2.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_eye_ik'),
            target_name=self.get_automarker_name('head_syd_front'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        syd.facial(group=MAIN, index=65, auto_lip=True, extra_delay=0)

        # m06_order_prison 70: DeltaThree.
        # Сдается мне, ребята, что это очередная провокация Ордена, и выведет нас этот милый капитан на
        # шеренгу бойцов со штурмовыми винтовками.
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('prisoner2_head_ik'),
            target_name=self.get_automarker_name('head_last_prisoner'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('prisoner2_eye_ik'),
            target_name=self.get_automarker_name('head_last_prisoner'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        cam_delta3.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('cam_delta3_marker'),
            target_name=self.get_automarker_name('cam_delta3_marker_pos2'), duration=10, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        prisoner2.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_TWSTS_FROM_270LV_XA_03, duration=5, time_scale=0.7,
            time_delay=t)
        prisoner4.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=1, time_delay=t)
        t += 3
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('prisoner2_head_ik'),
            target_name=self.get_automarker_name('head_prisoner3'), duration=2.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('prisoner2_eye_ik'),
            target_name=self.get_automarker_name('head_prisoner3'), duration=1.25, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        prisoner2.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_TALK_EMPH_000UP_A_18, duration=11, time_scale=0.8,
            trans_time=1, time_delay=t)
        t += 3
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('prisoner2_head_ik'),
            target_name=self.get_automarker_name('head_last_prisoner'), duration=2.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('prisoner2_eye_ik'),
            target_name=self.get_automarker_name('head_last_prisoner'), duration=1.25, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 3
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('prisoner2_head_ik'),
            target_name=self.get_automarker_name('head_asf_captain'), duration=2.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('prisoner2_eye_ik'),
            target_name=self.get_automarker_name('head_prisoner3'), duration=1.25, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('prisoner4_head_ik'),
            target_name=self.get_automarker_name('head_prisoner2'), duration=0.01, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        prisoner2.facial(group=MAIN, index=70, auto_lip=True, extra_delay=0)

        # m06_order_prison 80: DeltaOne.
        # А у тебя что, есть предложения получше? В любом случае, лучше на шеренгу бойцов с винтовками, чем на
        # допрос к специалистам Ордена.
        t = 0
        NeckIkEvent(root=self, group=MAIN, char_name=prisoner4.name,
            target_name=self.get_automarker_name('prisoner4_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=4, transition_duration=1, time_delay=t)
        cam_delta1.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=cam_delta1.name,
            target_name=self.get_automarker_name('cam_delta1_pos2'), duration=8, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        prisoner4.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_SHRG_SHLDRS_BIG_000LV_XA_03, duration=5,
            time_scale=0.7, time_delay=t)
        t += 2
        LookAtEvent(root=self, group=MAIN, point=cam_captain_sydanswer.name,
            focus=self.get_automarker_name('cam_captain_sydanswer_marker'), duration=150, target_type='ROOT',
            target_part='', up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        LookAtEvent(root=self, group=MAIN, point=cam_syd_captside.name,
            focus=self.get_automarker_name('cam_syd_captside_marker'), duration=150, target_type='ROOT',
            target_part='', up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        LookAtEvent(root=self, group=MAIN, point=cam_syd_clothesbox.name,
            focus=self.get_automarker_name('cam_syd_clothesbox_marker'), duration=150, target_type='ROOT',
            target_part='', up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_asf_captain'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_asf_captain'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 2
        prisoner4.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_GESTR_180LV_XA_03, duration=5, time_scale=0.7,
            trans_time=0.5, time_delay=t)
        t += 2
        NeckIkEvent(root=self, group=MAIN, char_name=prisoner4.name,
            target_name=self.get_automarker_name('prisoner4_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=4, transition_duration=1, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=100, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=25, transition_duration=1, time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, object_name=syd.name,
            target_name=self.get_automarker_name('point_syd_inside'), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=1, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=syd.name,
            target_name=self.get_automarker_name('syd_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=25, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=syd.name, target_name=self.get_automarker_name('syd_eye_ik'),
            target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', duration=25,
            transition_duration=1, time_delay=t)
        t += 1
        cam_trent.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_TWSTS_LOOK_270LV_XA_03, duration=5, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_syd'), duration=2.2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_syd'), duration=1.7, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        prisoner4.facial(group=MAIN, index=80, auto_lip=True, extra_delay=0)

        # m06_order_prison 90: Trent.
        # А что там с артефактами, капитан?
        t = 2.5
        cam_syd_trentside.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_head_ik'),
            target_name=self.get_automarker_name('head_trent_upper'), duration=1.75, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.25, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        trent.facial(group=MAIN, index=90, auto_lip=True, extra_delay=0)

        # m06_order_prison 100: Ceed.
        # Летят на базу Ордена.
        t = 0.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('prisoner4_head_ik'),
            target_name=self.get_automarker_name('head_syd'), duration=0.01, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=prisoner4.name,
            target_name=self.get_automarker_name('prisoner4_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=25, transition_duration=1, time_delay=t)
        syd.facial(group=MAIN, index=100, auto_lip=True, extra_delay=0)

        # m06_order_prison 110: DeltaOne.
        #  И вы позволили?
        t = 0
        syd.motion(group=MAIN, anim=Male.Sc_SPCBODY_s002x_syd_XE_STND_000LV_11, duration=2, time_scale=1.5,
            start_time=2, trans_time=1, time_delay=t)
        cam_captain_sydanswer.set(group=MAIN, time_delay=t)
        prisoner4.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_TWSTS_LOOK_090LV_XA_02, duration=5, time_scale=1.1,
            start_time=0.5, time_delay=t)
        t += 1
        syd.motion(group=MAIN, anim=Male.Sc_MLHEAD_MOTION_BREATHE_HEAVY_000LV_XA_, duration=4.444, time_scale=0.9,
            start_time=0.5, trans_time=0.5, time_delay=t)
        syd.motion(group=MAIN, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=0.532, time_scale=0.1,
            time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_head_ik'),
            target_name=self.get_automarker_name('head_asf_captain_upper'), duration=0.1, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_eye_ik'),
            target_name=self.get_automarker_name('head_asf_captain'), duration=0.1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 1
        syd.motion(group=MAIN, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=4.444, time_scale=0.9,
            trans_time=0.5, time_delay=t)
        cam_syd_captside.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=cam_syd_captside.name,
            target_name=self.get_automarker_name('cam_syd_captside_pos2'), duration=15, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        syd.motion(group=MAIN, anim=Male.Sc_SPCBODY_s002x_syd_XE_STND_000LV_11, duration=6, start_time=6.5,
            time_delay=t)
        prisoner4.facial(group=MAIN, index=110, auto_lip=True, extra_delay=0)

        # m06_order_prison 120: Ceed.
        # А что я, по-вашему, должен был сделать? Если бы я начал вставлять Ордену палки в колеса, то сидел бы
        # тут с вами, только не с сигаретой в руке, а с таким же милым ошейником на шее как у вас.
        t = 1.5
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_TALK_EMPH_000DN_A_20, duration=4, time_scale=0.5,
            trans_time=2, loop=True, time_delay=t)
        t += 2
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_head_ik'),
            target_name=self.get_automarker_name('head_trent_upper'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 3
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, duration=7, time_scale=0.7,
            trans_time=1, time_delay=t)
        t += 2
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_02, duration=3, time_scale=0.75,
            trans_time=1, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_head_ik'),
            target_name=self.get_automarker_name('head_asf_captain_upper'), duration=2, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_eye_ik'),
            target_name=self.get_automarker_name('head_asf_captain'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 4
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=4, time_scale=0.7,
            trans_time=1, loop=True, time_delay=t)
        syd.facial(group=MAIN, index=120, auto_lip=True, extra_delay=0)

        # m06_order_prison 130: Trent.
        # А как вы собираетесь помочь нам бежать?
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_head_ik'),
            target_name=self.get_automarker_name('head_syd_front'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        cam_trent.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=130, auto_lip=True, extra_delay=0)

        # m06_order_prison 140: Ceed.
        # Для начала вы примерите вот это...
        t = 0
        cam_syd_clothesbox.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=cam_syd_clothesbox.name,
            target_name=self.get_automarker_name('cam_syd_clothesbox_pos2'), duration=8, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('cam_syd_clothesbox_marker'),
            target_name=self.get_automarker_name('cam_syd_clothesbox_marker_pos2'), duration=8, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_GESTR_RGHT_000LV_XA_02, duration=8, time_scale=0.5,
            time_delay=t)
        t += 2
        MoveEvent(root=self, group=MAIN, object_name=panel1.name,
            target_name=self.get_automarker_name('panel1_pos_open'), duration=5, smooth=True, adjust_pos=True,
            adjust_orient=False, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=panel1.name, angle=-90, axis='Z_AXIS', duration=5,
            smooth=True, time_delay=t)
        snd_close_door_clothesbox.start(group=MAIN, duration=5, loop=False, start_time=500, time_delay=t)
        syd.facial(group=MAIN, index=140, auto_lip=True, extra_delay=0)

        # m06_order_prison 145: Ceed.
        # А потом спокойно и небрежно проследуете в ангар к кораблю мистера Трента.
        t = 0
        snd_close_door_clothesbox.change_attenuation(group=MAIN, duration=3, attenuation=-100, time_delay=t)
        t += 2
        NeckIkEvent(root=self, group=MAIN, char_name=syd.name,
            target_name=self.get_automarker_name('syd_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=25, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=syd.name, target_name=self.get_automarker_name('syd_eye_ik'),
            target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', duration=25,
            transition_duration=1, time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_head_ik'),
            target_name=self.get_automarker_name('head_trent_upper'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        syd.facial(group=MAIN, index=145, auto_lip=True, extra_delay=0)

        # m06_order_prison 150: Ceed.
        # К сожалению, все остальные уже разбирают на запчасти. А вот корабль Трента пока еще в целости и
        # сохранности. Так что, как говорится, в тесноте, да не в обиде.
        t = 0
        cam_syd_captside.set(group=MAIN, time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_head_ik'),
            target_name=self.get_automarker_name('head_asf_captain_upper'), duration=2.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_eye_ik'),
            target_name=self.get_automarker_name('head_asf_captain'), duration=1.6, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 2.5
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, duration=7, time_scale=0.7,
            trans_time=1, time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_head_ik'),
            target_name=self.get_automarker_name('head_trent_upper'), duration=2.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.6, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 1
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_02, duration=3, time_scale=0.75,
            trans_time=1, time_delay=t)
        t += 3
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_head_ik'),
            target_name=self.get_automarker_name('head_asf_captain_upper'), duration=2.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_eye_ik'),
            target_name=self.get_automarker_name('head_asf_captain'), duration=1.6, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        syd.facial(group=MAIN, index=150, auto_lip=True, extra_delay=0)

        # m06_order_prison 160: Trent.
        # А после нашего побега... Как это скажется на вас? Вы не будете сидеть здесь не с сигаретой в руке, а
        # с ошейником как у нас на шее?
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=160, auto_lip=True, extra_delay=0)

        # m06_order_prison 170: Ceed.
        # О, нет. Вы же меня вырубили, этому найдутся неоспоримые доказательства.
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_head_ik'),
            target_name=self.get_automarker_name('head_trent_upper'), duration=2.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.6, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        cam_syd_captside.set(group=MAIN, time_delay=t)
        t += 2
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_head_ik'),
            target_name=self.get_automarker_name('head_syd_front'), duration=1.75, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_eye_ik'),
            target_name=self.get_automarker_name('head_syd_front'), duration=1.25, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        syd.motion(group=MAIN, anim=Male.Sc_SPCBODY_s002x_syd_XE_STND_000LV_11, duration=6, time_scale=1.5,
            start_time=1.3, trans_time=2.5, time_delay=t)
        syd.facial(group=MAIN, index=170, auto_lip=True, extra_delay=0)

        # m06_order_prison 180: Ceed.
        # К тому же, что такое побег пленников в сравнении с тем, что я передал в руки  Ордена артефакты, за
        # которыми охотится весь сектор Сириуса.
        t = 0.5
        NeckIkEvent(root=self, group=MAIN, char_name=syd.name,
            target_name=self.get_automarker_name('syd_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=25, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=syd.name, target_name=self.get_automarker_name('syd_eye_ik'),
            target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', duration=25,
            transition_duration=1, time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_head_ik'),
            target_name=self.get_automarker_name('head_asf_captain_upper'), duration=1.75, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_eye_ik'),
            target_name=self.get_automarker_name('head_asf_captain'), duration=1.25, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 2
        LookAtEvent(root=self, group=MAIN, point=cam_trent_finalword.name,
            focus=self.get_automarker_name('cam_trent_finalword_marker'), duration=50, target_type='ROOT',
            target_part='', up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        LookAtEvent(root=self, group=MAIN, point=cam_exit.name, focus=self.get_automarker_name('cam_exit_marker'),
            duration=50, target_type='ROOT', target_part='', up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, duration=6, time_scale=0.6,
            trans_time=1, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_head_ik'),
            target_name=self.get_automarker_name('head_trent_upper'), duration=2.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 2
        MoveEvent(root=self, group=MAIN, object_name=vfx_rtc_cigaretteglow_4.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=vfx_rtc_sydsmoke_3.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 2
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_head_ik'),
            target_name=self.get_automarker_name('head_asf_captain_upper'), duration=2.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_eye_ik'),
            target_name=self.get_automarker_name('head_asf_captain'), duration=1.4, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 3
        MoveEvent(root=self, group=MAIN, object_name=prisoner4.name,
            target_name=self.get_automarker_name('point_prisoner4_stand'), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=prisoner1.name,
            target_name=self.get_automarker_name('point_prisoner1_stand'), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        syd.facial(group=MAIN, index=180, auto_lip=True, extra_delay=0)

        # m06_order_prison 190: Trent.
        # Толково, не поспоришь.
        t = 0
        cam_trent_finalword.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=cam_trent_finalword.name,
            target_name=self.get_automarker_name('cam_trent_finalword_pos2'), duration=5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        prisoner4.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=8, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=prisoner1.name, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04,
            duration=8, time_delay=t)
        t += 1
        prisoner4.motion(group=MAIN, anim=Male.Sc_MLBODY_STROLL_000LV_XA_01, duration=8, loop=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=prisoner1.name, anim=Male.Sc_MLBODY_STROLL_000LV_XA_01,
            duration=8, loop=True, time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_trent_front_upper'), duration=2.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_trent_front_upper'), duration=1.4, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_TWSTS_FROM_270LV_XA_03, duration=5, time_scale=0.7,
            time_delay=t)
        t += 1.5
        AttachEvent(root=self, group=MAIN, target_name=self.get_automarker_name('trent_head_ik'),
            parent_name=prisoner1.name, duration=4, target_part='Body_Head', target_type='PART', adjust_pos=True,
            adjust_orient=True, up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        t += 2.5
        EyeIkEvent(root=self, group=MAIN, char_name=trent.name, target_name=prisoner1.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=3, transition_duration=1,
            time_delay=t)
        t += 1.9
        ambience_hall.change_attenuation(group=MAIN, duration=0.1, attenuation=0, time_delay=t)
        t += 0.1
        ambience_room.change_attenuation(group=MAIN, duration=0.1, attenuation=-100, time_delay=t)
        cam_exit.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=cam_exit.name,
            target_name=self.get_automarker_name('cam_exit_pos2'), duration=12, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('cam_exit_marker'),
            target_name=self.get_automarker_name('cam_exit_marker_pos2'), duration=12, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=trent_classic.name,
            target_name=self.get_automarker_name('point_trent_classic'), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=prisoner1b.name,
            target_name=self.get_automarker_name('point_prisoner1b'), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=prisoner2b.name,
            target_name=self.get_automarker_name('point_prisoner2b'), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=prisoner3b.name,
            target_name=self.get_automarker_name('point_prisoner3b'), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=prisoner4b.name,
            target_name=self.get_automarker_name('point_prisoner4b'), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=syd.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=prisoner1.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=prisoner2.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=prisoner3.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=prisoner4.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.1
        MoveEvent(root=self, group=MAIN, object_name=body1.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=body2.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=body3.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.1
        MoveEvent(root=self, group=MAIN, object_name=panel1.name,
            target_name=self.get_automarker_name('panel1_init_pos'), duration=0.001, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 0.8
        MotionEvent(root=self, group=MAIN, object_name=doors.name, anim='Sc_cv_prison_cell', duration=3.332,
            trans_scale=1, time_delay=t)
        snd_open_door.start(group=MAIN, duration=10, loop=False, start_time=0, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=prisoner1b.name, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01,
            duration=25, start_time=0.5, loop=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=prisoner2b.name, anim=Male.Sc_MLBODY_WLKG_000LV_XB_01,
            duration=25, loop=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=prisoner3b.name, anim=Male.Sc_MLBODY_WLKG_000LV_XB_01,
            duration=25, start_time=0.5, loop=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=prisoner4b.name, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01,
            duration=25, loop=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=trent_classic.name, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01,
            duration=5.6, start_time=0.9, loop=True, time_delay=t)
        t += 4
        RotateAxisEvent(root=self, group=MAIN, object_name=prisoner3b.name, angle=90, axis='Y_AXIS', duration=4,
            smooth=True, time_delay=t)
        trent.facial(group=MAIN, index=190, auto_lip=True, extra_delay=0)
        # Действие после исходного окна реплики.
        t = 0
        RotateAxisEvent(root=self, group=MAIN, object_name=prisoner1b.name, angle=90, axis='Y_AXIS', duration=4,
            smooth=True, time_delay=t)
        t += 0.6
        MotionEvent(root=self, group=MAIN, object_name=trent_classic.name,
            anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=4, time_delay=t)
        t += 0.4
        RotateAxisEvent(root=self, group=MAIN, object_name=prisoner2b.name, angle=90, axis='Y_AXIS', duration=4,
            smooth=True, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=prisoner4b.name, angle=90, axis='Y_AXIS', duration=4,
            smooth=True, time_delay=t)
        t += 2
        MotionEvent(root=self, group=MAIN, object_name=trent_classic.name,
            anim=Male.Sc_MLBODY_STND_LOOK_AROU_000LV_XA_09, duration=10, trans_time=0.5, time_delay=t)
        t += 0.5
        MotionEvent(root=self, group=MAIN, object_name=trent_classic.name,
            anim=Trent.Sc_MLHEAD_HAPPY_SMILE_SNEER_TRENT_000LV_XA_, duration=10, time_scale=0.7, trans_time=0.25,
            time_delay=t)
        t += 2.7
        MotionEvent(root=self, group=MAIN, object_name=trent_classic.name,
            anim=Trent.Sc_MLHEAD_MOTION_EYES_OPENBG_TRENT_000LV_XA_, duration=10, time_scale=0.7, trans_time=0.25,
            time_delay=t)
        t += 5.8
        MotionEvent(root=self, group=MAIN, object_name=doors.name, anim='Sc_cv_prison_cell', duration=3.332,
            start_time=3.332, trans_scale=1, time_delay=t)
        snd_close_door.start(group=MAIN, duration=10, loop=False, start_time=0, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=trent_classic.name,
            anim=Male.Sc_MLBODY_STND_WALK_TRNS_270LV_XA_02, duration=10, trans_time=0.5, time_delay=t)
        t += 2
        MotionEvent(root=self, group=MAIN, object_name=trent_classic.name, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01,
            duration=10, loop=True, time_delay=t)
        main_group.append_time(17)
