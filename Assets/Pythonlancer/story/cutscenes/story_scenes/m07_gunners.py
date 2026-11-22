"""m07_gunners: полная постановка из master; точки в m07_gunners.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Alchemy, AttachEvent, Character, ConnectHardpointEvent, LookAtCamera, MAIN, Male, MotionEvent, MoveEvent, NeckIkEvent, Prop, RotateAxisEvent, Sound, SoundEvent,
)
from story.cutscenes.anim import (
    Male, Trent,
)
from story import actors


class PropBarclothWaddedBartProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'barcloth_wadded'

class PropGlassGreenProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'glass_green'

class PropJesterGunProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'prop_gun_laser_1'

class PropHammerGunProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'gun_laser_2'

class PropRockfordRifleProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'rifle'

class CharPeasantActor(actors.Actor):
    NAME = 'peasant'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'tyler'

class CharJester2Actor(actors.Actor):
    NAME = 'jester2'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'jester'


class M07GunnersScene(Scene):
    DUMP_FILE = 'm07_gunners'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Персонажи, камеры, реквизит и звук.
        bartender_fixture = Character(root=self, actor=actors.BartenderFixture, name='Char_bartender_Fixture',
            light_group=0, init_point='Char_bartender_Fixture', rotate_from_quat=True,
            appearance='li_bartender_1', actor_name='bartender', floor_height=-110.0)
        music_hall_ambient = Sound(root=self, name='music_hall_ambient', sound='ambience_bar_space',
            attenuation=-12, dmin=50, dmax=300, priority='Story_Sound_1')
        music_bar = Sound(root=self, name='music_bar', sound='music_bar_generic03', attenuation=-5, dmin=50,
            dmax=300, priority='Story_Sound_1')
        music_danger = Sound(root=self, name='music_danger', sound='rtc_m07_bg_mix', attenuation=-100, dmin=50,
            dmax=300, priority='Story_Sound_1')
        music_fire_attempt = Sound(root=self, name='music_fire_attempt', sound='rtc_m07_fire_attempt',
            attenuation=0, dmin=50, dmax=300, priority='Story_Sound_1')
        sound_fire_rockford = Sound(root=self, name='sound_fire_rockford', sound='fire_rifle', attenuation=0,
            dmin=50, dmax=300, priority=None)
        sound_fire_rockford2 = Sound(root=self, name='sound_fire_rockford2', sound='fire_rifle_alt',
            attenuation=0, dmin=50, dmax=300, priority=None)
        prop_barcloth_wadded_bart = PropBarclothWaddedBartProp(root=self, name='Prop_barcloth_wadded_Bart',
            light_group=0, init_point='Prop_barcloth_wadded_Bart', rotate_from_quat=True, use_ambient=True)
        prop_glass_green = PropGlassGreenProp(root=self, name='Prop_glass_green', light_group=0,
            init_point='Prop_glass_green', rotate_from_quat=True)
        prop_jester_gun = PropJesterGunProp(root=self, name='prop_jester_gun', light_group=0,
            init_point='prop_jester_gun', rotate_from_quat=True)
        prop_hammer_gun = PropHammerGunProp(root=self, name='prop_hammer_gun', light_group=0,
            init_point='prop_hammer_gun', rotate_from_quat=True)
        prop_rockford_rifle = PropRockfordRifleProp(root=self, name='prop_rockford_rifle', light_group=0,
            init_point='prop_rockford_rifle', rotate_from_quat=True)
        trent = Character(root=self, actor=actors.Trent, name='Char_trent', light_group=0,
            init_point='Char_trent', rotate_from_quat=True, appearance='trent', actor_name='Player')
        barman = Character(root=self, actor=actors.DetroitBarman, name='Char_barman', light_group=0,
            init_point='Char_barman', rotate_from_quat=True, appearance='martin', actor_name='Barman')
        peasant = Character(root=self, actor=CharPeasantActor, name='Char_peasant', light_group=0,
            init_point='Char_peasant', rotate_from_quat=True, appearance='tyler', actor_name='Peasant')
        hammer = Character(root=self, actor=actors.CadizEnemyTwo, name='Char_hammer', light_group=0,
            init_point='Char_hammer', rotate_from_quat=True, appearance='hammer', actor_name='hammer')
        jester = Character(root=self, actor=actors.CadizEnemyOne, name='Char_jester', light_group=0,
            init_point='Char_jester', rotate_from_quat=True, appearance='jester', actor_name='jester')
        jester2 = Character(root=self, actor=CharJester2Actor, name='Char_jester2', light_group=0,
            init_point='Char_jester2', rotate_from_quat=True, appearance='jester', actor_name='jester2')
        rockford = Character(root=self, actor=actors.Rockford, name='Char_rockford', light_group=0,
            init_point='Char_rockford', rotate_from_quat=True, appearance='rockford', actor_name='rockford')
        cam_start = LookAtCamera(root=self, name='cam_start', fov=30, look_duration=70)
        cam_sit = LookAtCamera(root=self, name='cam_sit', fov=22, look_duration=70)
        cam_barman = LookAtCamera(root=self, name='cam_barman', fov=18, look_duration=70)
        cam_hammer_reveal = LookAtCamera(root=self, name='cam_hammer_reveal', fov=25, look_duration=70)
        cam_jester_ready = LookAtCamera(root=self, name='cam_jester_ready', fov=25, look_duration=70)
        cam_jester_standing = LookAtCamera(root=self, name='cam_jester_standing', fov=26, look_duration=70)
        cam_greet = LookAtCamera(root=self, name='cam_greet', fov=25, look_duration=70)
        cam_hammer_anger = LookAtCamera(root=self, name='cam_hammer_anger', fov=12, look_duration=70)
        cam_jester_aim = LookAtCamera(root=self, name='cam_jester_aim', fov=17, look_duration=70)
        cam_jester_fire = LookAtCamera(root=self, name='cam_jester_fire', fov=15, look_duration=70)
        cam_trent_fire = LookAtCamera(root=self, name='cam_trent_fire', fov=18, look_duration=70)
        cam_hammer_death = LookAtCamera(root=self, name='cam_hammer_death', fov=16, look_duration=70)
        cam_rockford_appear = LookAtCamera(root=self, name='cam_rockford_appear', fov=11, look_duration=70)
        fadenegative_variable_1 = Alchemy(root=self, name='fadenegative_variable_1',
            particles='rtc_fadenegative_variable', point_name='fadenegative_variable_1', sparam=0, light_group=0,
            sort_group=0, hidden=False, use_ambient=True)

        # Исходные точки взгляда.

        # Вход.
        t = 0
        cam_start.set(group=MAIN, time_delay=t)
        cam_start.move_cam(group=MAIN, index=2, duration=7, smooth=True, time_delay=t)
        cam_start.move_focus(group=MAIN, index=2, duration=7, smooth=True, time_delay=t)
        hammer.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=15, loop=True, time_delay=t)
        jester.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=15, loop=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=10, loop=True, time_delay=t)
        ConnectHardpointEvent(root=self, group=MAIN, target_name=prop_barcloth_wadded_bart.name,
            parent_name=barman.name, duration=35, target_hardpoint='hprightconnect_prop_barcloth_wadded',
            parent_hardpoint='hprightconnect', time_delay=t)
        ConnectHardpointEvent(root=self, group=MAIN, target_name=prop_glass_green.name, parent_name=barman.name,
            duration=35, target_hardpoint='hpleftconnect_prop_glass_green', parent_hardpoint='hpleftconnect',
            time_delay=t)
        music_hall_ambient.start(group=MAIN, duration=108, loop=True, start_time=0, time_delay=t)
        music_bar.start(group=MAIN, duration=25, loop=True, start_time=0, time_delay=t)
        t += 0.25
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=25, axis='Y_AXIS', duration=2,
            smooth=True, time_delay=t)
        t += 3
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=-115, axis='Y_AXIS', duration=4,
            smooth=True, time_delay=t)
        t += 3.75
        barman.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CLEAN_GLAS_000LV_A_26, duration=10, start_time=4,
            time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=barman.name, angle=-45, axis='Y_AXIS', duration=1,
            smooth=True, time_delay=t)
        t += 1
        cam_barman.set(group=MAIN, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=peasant.name, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04,
            duration=10, loop=True, time_delay=t)
        t += 4.9
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('point_trent_stand_to_sit'), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.1
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_SITCR_TRNS_090DN_XA_07, duration=15, start_time=1,
            time_delay=t)
        t += 1
        cam_hammer_reveal.set(group=MAIN, time_delay=t)
        cam_hammer_reveal.move_cam(group=MAIN, index=2, duration=8, smooth=True, time_delay=t)
        cam_hammer_reveal.move_focus(group=MAIN, index=2, duration=8, smooth=True, time_delay=t)
        t += 1
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=-20, axis='Y_AXIS', duration=1,
            smooth=True, time_delay=t)
        t += 2
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=15, trans_time=1,
            time_delay=t)
        t += 2
        hammer.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_GESTR_180LV_XA_03, duration=15, time_scale=0.4,
            trans_time=1, time_delay=t)
        hammer.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_GESTR_THUMB_000LV_00, duration=0.2, start_time=2,
            time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_TWSTS_LOOK_090LV_XA_02, duration=15, time_scale=0.8,
            trans_time=1, time_delay=t)
        t += 1
        music_danger.start(group=MAIN, duration=28, loop=True, start_time=0, time_delay=t)
        music_danger.change_attenuation(group=MAIN, duration=5, attenuation=-5, time_delay=t)
        t += 2
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_TWSTS_FROM_090LV_XA_02, duration=15, time_scale=0.65,
            trans_time=1, time_delay=t)
        t += 2
        ConnectHardpointEvent(root=self, group=MAIN, target_name=prop_jester_gun.name, parent_name=jester.name,
            duration=159.45, target_hardpoint='hprightconnect_gun', parent_hardpoint='hprightconnect',
            time_delay=t)
        jester.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_GUN_RGHT_000LV_XB_00, duration=0.2, time_delay=t)
        t += 1
        cam_jester_ready.set(group=MAIN, time_delay=t)
        jester.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=15, time_scale=0.6,
            time_delay=t)
        music_bar.change_attenuation(group=MAIN, duration=5, attenuation=-100, time_delay=t)
        t += 3
        ConnectHardpointEvent(root=self, group=MAIN, target_name=prop_hammer_gun.name, parent_name=hammer.name,
            duration=159.45, target_hardpoint='hprightconnect_gun', parent_hardpoint='hprightconnect',
            time_delay=t)
        hammer.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_GUN_RGHT_000LV_XB_00, duration=0.2, time_delay=t)
        t += 0.8
        cam_jester_standing.set(group=MAIN, time_delay=t)
        t += 0.2
        jester.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_WALK_TRNS_270LV_XA_10, duration=3.9, time_scale=0.8,
            start_time=1.5, trans_time=1, time_delay=t)
        barman.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CLEAN_GLAS_000LV_A_26, duration=3, start_time=7,
            time_delay=t)
        t += 1
        RotateAxisEvent(root=self, group=MAIN, object_name=jester.name, angle=-80, axis='Y_AXIS', duration=3,
            smooth=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=peasant.name,
            anim=Male.Sc_MLBODY_STND_RUN_TRNS_000LV_XD_02, duration=10, time_scale=0.68, trans_time=1,
            time_delay=t)
        t += 1.5
        RotateAxisEvent(root=self, group=MAIN, object_name=peasant.name, angle=-45, axis='Y_AXIS', duration=2,
            smooth=True, time_delay=t)
        t += 0.5
        barman.motion(group=MAIN, anim=Male.Sc_MLBODY_CROUCHNG_IDLE_000DN_XA_03, duration=10, trans_time=2,
            time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=10, loop=True, time_delay=t)
        hammer.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_STNDCR_TRNS_090LV_XA_05, duration=15, time_delay=t)
        t += 0.1
        RotateAxisEvent(root=self, group=MAIN, object_name=hammer.name, angle=-90, axis='Y_AXIS', duration=3,
            smooth=True, time_delay=t)
        t += 0.85
        MoveEvent(root=self, group=MAIN, object_name=jester.name,
            target_name=self.get_automarker_name('point_jester_ask'), duration=0, smooth=False, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 0.05
        cam_greet.set(group=MAIN, time_delay=t)
        cam_greet.move_cam(group=MAIN, index=2, duration=6, smooth=True, time_delay=t)
        cam_greet.move_focus(group=MAIN, index=2, duration=6, smooth=True, time_delay=t)
        jester.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=15, time_scale=0.8,
            start_time=0.5, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=jester.name, angle=-40, axis='Y_AXIS', duration=2,
            smooth=True, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=jester.name, target_name=trent.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=23, transition_duration=3,
            time_delay=t)
        t += 0.3
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name, target_name=jester.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=40, transition_duration=3,
            time_delay=t)
        main_group.append_time(34)

        # m07_cadiz 10: CadizEnemyOne.
        # Здаров, земляк! Где Рокфорд?
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=peasant.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=barman.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=hammer.name, target_name=trent.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=22, transition_duration=3,
            time_delay=t)
        jester.facial(group=MAIN, index=10, auto_lip=True, extra_delay=0)

        # m07_cadiz 20: Trent.
        # Понятия не имею.
        trent.facial(group=MAIN, index=20, auto_lip=True, extra_delay=0)

        # m07_cadiz 30: CadizEnemyTwo.
        # Слыш, земеля, ты чо такой дерзкий? Тебя по-хорошему спросили нна, где Рокфорд?
        t = 0
        cam_hammer_anger.set(group=MAIN, time_delay=t)
        t += 1
        trent.motion(group=MAIN, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, duration=4.444, time_scale=0.9,
            trans_time=0.5, time_delay=t)
        hammer.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=15,
            time_scale=0.6, trans_time=1, time_delay=t)
        t += 3.5
        hammer.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_HOLD_000LV_XA_02, duration=15, time_scale=0.8,
            trans_time=1, loop=True, time_delay=t)
        hammer.facial(group=MAIN, index=30, auto_lip=True, extra_delay=0)

        # m07_cadiz 40: CadizEnemyThree.
        # Сейчас наладим диалог.
        t = 0
        cam_jester_aim.set(group=MAIN, time_delay=t)
        t += 1
        jester.motion(group=MAIN, anim=Male.Sc_SPCBODY_s019b_Drake_XA_STND_000LV_13, duration=3.5, time_scale=0.7,
            trans_time=1.5, time_delay=t)
        music_fire_attempt.start(group=MAIN, duration=20, loop=False, start_time=0, time_delay=t)
        music_danger.change_attenuation(group=MAIN, duration=3, attenuation=-100, time_delay=t)
        jester.facial(group=MAIN, index=40, auto_lip=True, extra_delay=0, voice_actor=actors.CadizEnemyThree)

        # m07_cadiz 50: CadizEnemyFour.
        # Где Рокфорд, утырок?
        t = 2.3
        trent.motion(group=MAIN, anim=Trent.Sc_MLHEAD_MOTION_EYES_OPENBG_TRENT_000LV_XA_, duration=2,
            trans_time=0.1, time_delay=t)
        t += 0.2
        cam_trent_fire.set(group=MAIN, time_delay=t)
        cam_trent_fire.change_fov(group=MAIN, duration=5, fov=18, smooth=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_GEST_HNDS_WAIT_000LV_XA_03, duration=15, time_scale=0.3,
            start_time=2, time_delay=t)
        t += 2.5
        cam_jester_fire.change_fov(group=MAIN, duration=3, fov=17, smooth=True, time_delay=t)
        t += 0.5
        cam_jester_fire.set(group=MAIN, time_delay=t)
        jester.motion(group=MAIN, anim='Sc_SPCBODY_s019b_Drake_XB_STND_000LV_%', duration=6, loop=True,
            time_delay=t)
        jester.motion(group=MAIN, anim=Male.Sc_MLHEAD_MAD_COLD_000LV_XA_, duration=3, time_scale=0.6,
            start_time=0.5, time_delay=t)
        t += 1.5
        fadenegative_variable_1.set_sparam(group=MAIN, duration=0, sparam=1, smooth=False, time_delay=t)
        t += 0.7
        AttachEvent(root=self, group=MAIN, target_name=fadenegative_variable_1.name,
            parent_name=cam_jester_fire.name, duration=0.308, target_part='', target_type='ROOT', adjust_pos=True,
            adjust_orient=True, entity_relative=True, up='Y_AXIS', front='NEG_Z_AXIS', offset_z=-0.5, time_delay=t)
        fadenegative_variable_1.start(group=MAIN, duration=0.307, time_delay=t)
        fadenegative_variable_1.set_sparam(group=MAIN, duration=0.307, sparam=0, smooth=True, time_delay=t)
        sound_fire_rockford.start(group=MAIN, duration=20, loop=False, start_time=0, time_delay=t)
        t += 0.2
        jester.motion(group=MAIN, anim=Male.Sc_SPCBODY_s051x_ku_guard01_XC_STND_DEATH_225DN_03, duration=5,
            time_scale=0.8, start_time=1, trans_time=1.5, time_delay=t)
        t += 0.1
        hammer.motion(group=MAIN, anim=Male.Sc_SPCBODY_s002x_Vance_XD_STND_000DN_03, duration=15, time_scale=1.3,
            trans_time=1, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=hammer.name, angle=45, axis='Y_AXIS', duration=0,
            smooth=True, time_delay=t)
        cam_hammer_death.set(group=MAIN, time_delay=t)
        t += 0.1
        RotateAxisEvent(root=self, group=MAIN, object_name=hammer.name, angle=45, axis='Y_AXIS', duration=2,
            smooth=True, time_delay=t)
        t += 0.1
        fadenegative_variable_1.set_sparam(group=MAIN, duration=0, sparam=1, smooth=False, time_delay=t)
        t += 0.2
        RotateAxisEvent(root=self, group=MAIN, object_name=jester.name, angle=33, axis='Y_AXIS', duration=2,
            smooth=True, time_delay=t)
        t += 0.1
        AttachEvent(root=self, group=MAIN, target_name=fadenegative_variable_1.name,
            parent_name=cam_hammer_death.name, duration=0.508, target_part='', target_type='ROOT',
            adjust_pos=True, adjust_orient=True, entity_relative=True, up='Y_AXIS', front='NEG_Z_AXIS',
            offset_z=-0.5, time_delay=t)
        fadenegative_variable_1.start(group=MAIN, duration=0.507, time_delay=t)
        fadenegative_variable_1.set_sparam(group=MAIN, duration=0.507, sparam=0, smooth=True, time_delay=t)
        sound_fire_rockford2.start(group=MAIN, duration=20, loop=False, start_time=0, time_delay=t)
        music_fire_attempt.change_attenuation(group=MAIN, duration=1, attenuation=-100, time_delay=t)
        hammer.motion(group=MAIN, anim=Male.Sc_dx_s019b_2704_Drake, duration=2, trans_time=0.15, time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, object_name=rockford.name,
            target_name=self.get_automarker_name('point_rockford_aim'), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        rockford.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_GUN_RGHT_000LV_00, duration=1, time_scale=2,
            time_delay=t)
        rockford.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_RIFLE_LEFT_000LV_00, duration=0.4, time_scale=2,
            time_delay=t)
        ConnectHardpointEvent(root=self, group=MAIN, target_name=prop_rockford_rifle.name,
            parent_name=rockford.name, duration=59.45, target_hardpoint='hp_male_rhand_rifle',
            parent_hardpoint='hprightconnect', time_delay=t)
        jester.facial(group=MAIN, index=50, auto_lip=True, extra_delay=0, voice_actor=actors.CadizEnemyFour)
        # Действие после исходного окна реплики.
        t = 0.1
        rockford.motion(group=MAIN, anim=Male.Sc_SPCBODY_s010x_Rh_agent01_XA_STND_000LV_03, duration=0.2,
            start_time=2, time_delay=t)
        t += 1
        cam_rockford_appear.set(group=MAIN, time_delay=t)
        cam_rockford_appear.move_cam(group=MAIN, index=2, duration=4, smooth=True, time_delay=t)
        cam_rockford_appear.move_focus(group=MAIN, index=2, duration=4, smooth=True, time_delay=t)
        cam_rockford_appear.change_fov(group=MAIN, duration=4, fov=22, smooth=True, time_delay=t)
        main_group.append_time(2.6)

        # m07_cadiz 60: Rockford.
        # Я Рокфорд.
        t = 2
        rockford.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01, duration=15, trans_time=1,
            time_delay=t)
        rockford.facial(group=MAIN, index=60, auto_lip=True, extra_delay=0)

        # m07_cadiz 65: Rockford.
        # За мной! Быстро!
        t = 0.55
        rockford.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=15, loop=True, time_delay=t)
        line_sound = self.lookup_single_sound(65)
        SoundEvent(root=self, group=MAIN, sound_name=line_sound.get_nickname())
        main_group.append_time(4)
