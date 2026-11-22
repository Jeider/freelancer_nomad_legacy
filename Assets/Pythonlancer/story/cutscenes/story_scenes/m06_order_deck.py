"""m06_order_deck: полная постановка из master; точки в m06_order_deck.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character, EyeIkEvent, LookAtCamera, MAIN, Male, MotionEvent, MotionPath, MoveEvent, NeckIkEvent, PathAnimationEvent, Ship, Sound, SoundEvent, StaticCamera,
)
from story.cutscenes.anim import (
    Male, Trent,
)
from story import actors


class PlayershipProp(Ship):
    COMPOUND_TEMPLATE_NAME = 'PlayerShip'

class PrisonersShip02Prop(Ship):
    COMPOUND_TEMPLATE_NAME = 'li_elite'

class PrisonersShip03Prop(Ship):
    COMPOUND_TEMPLATE_NAME = 'li_elite'

class TestVehicleProp(Ship):
    COMPOUND_TEMPLATE_NAME = 'li_elite'

class CharTrentActor(actors.Actor):
    NAME = 'trent'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'trent'

class CharPrisoner1Actor(actors.Actor):
    NAME = 'prisoner1'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_asf_prisoner01'

class CharPrisoner2Actor(actors.Actor):
    NAME = 'prisoner2'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_asf_prisoner02'

class CharPrisoner3Actor(actors.Actor):
    NAME = 'prisoner3'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_asf_prisoner03'

class CharPrisoner4Actor(actors.Actor):
    NAME = 'prisoner4'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_asf_prisoner04'

class CharCommanderActor(actors.Actor):
    NAME = 'commander'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_gunner_leader'

class CharGunner01Actor(actors.Actor):
    NAME = 'gunner01'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_gunner_sides1'

class CharGunner02Actor(actors.Actor):
    NAME = 'gunner02'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_gunner_sides2'

class CharGunner03Actor(actors.Actor):
    NAME = 'gunner03'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_gunner_back1'

class CharGunner04Actor(actors.Actor):
    NAME = 'gunner04'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_gunner_back2'

class CharSydGuardActor(actors.Actor):
    NAME = 'syd_guard'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_gunner_syd'


class M06OrderDeckScene(Scene):
    DUMP_FILE = 'm06_order_deck'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Персонажи, камеры, реквизит и звук.
        music_main = Sound(root=self, name='music_main', sound='music_discordant_psychosis', attenuation=0,
            dmin=50, dmax=300, priority='Story_Sound_1')
        playership = PlayershipProp(root=self, name='PlayerShip', light_group=3, init_point='PlayerShip',
            rotate_from_quat=True)
        prisoners_ship02 = PrisonersShip02Prop(root=self, name='prisoners_ship02', light_group=3,
            init_point='prisoners_ship02', rotate_from_quat=True, loadout='level_li_elite_loadout04')
        prisoners_ship03 = PrisonersShip03Prop(root=self, name='prisoners_ship03', light_group=3,
            init_point='prisoners_ship03', rotate_from_quat=True, loadout='level_li_elite_loadout04')
        test_vehicle = TestVehicleProp(root=self, name='test_vehicle', light_group=3, init_point='test_vehicle',
            rotate_from_quat=True, loadout='level_li_elite_loadout04')
        trent = Character(root=self, actor=CharTrentActor, name='Char_trent', light_group=3,
            init_point='Char_trent', rotate_from_quat=True, appearance='trent', actor_name='Player')
        prisoner1 = Character(root=self, actor=CharPrisoner1Actor, name='Char_prisoner1', light_group=3,
            init_point='Char_prisoner1', rotate_from_quat=True, appearance='m06_asf_prisoner01',
            actor_name='Prisoner1')
        prisoner2 = Character(root=self, actor=CharPrisoner2Actor, name='Char_prisoner2', light_group=3,
            init_point='Char_prisoner2', rotate_from_quat=True, appearance='m06_asf_prisoner02',
            actor_name='Prisoner2')
        prisoner3 = Character(root=self, actor=CharPrisoner3Actor, name='Char_prisoner3', light_group=3,
            init_point='Char_prisoner3', rotate_from_quat=True, appearance='m06_asf_prisoner03',
            actor_name='Prisoner3')
        prisoner4 = Character(root=self, actor=CharPrisoner4Actor, name='Char_prisoner4', light_group=3,
            init_point='Char_prisoner4', rotate_from_quat=True, appearance='m06_asf_prisoner04',
            actor_name='Prisoner4')
        commander = Character(root=self, actor=CharCommanderActor, name='Char_commander', light_group=3,
            init_point='Char_commander', rotate_from_quat=True, appearance='m06_gunner_leader',
            actor_name='Gunner_commander')
        gunner01 = Character(root=self, actor=CharGunner01Actor, name='Char_gunner01', light_group=3,
            init_point='Char_gunner01', rotate_from_quat=True, appearance='m06_gunner_sides1',
            actor_name='Gunner2')
        gunner02 = Character(root=self, actor=CharGunner02Actor, name='Char_gunner02', light_group=3,
            init_point='Char_gunner02', rotate_from_quat=True, appearance='m06_gunner_sides2',
            actor_name='Gunner3')
        gunner03 = Character(root=self, actor=CharGunner03Actor, name='Char_gunner03', light_group=3,
            init_point='Char_gunner03', rotate_from_quat=True, appearance='m06_gunner_back1', actor_name='Gunner4')
        gunner04 = Character(root=self, actor=CharGunner04Actor, name='Char_gunner04', light_group=3,
            init_point='Char_gunner04', rotate_from_quat=True, appearance='m06_gunner_back2', actor_name='Gunner5')
        syd = Character(root=self, actor=actors.Ceed, name='Char_syd', light_group=3, init_point='Char_syd',
            rotate_from_quat=True, appearance='syd', actor_name='Syd')
        syd_guard = Character(root=self, actor=CharSydGuardActor, name='Char_syd_guard', light_group=3,
            init_point='Char_syd_guard', rotate_from_quat=True, appearance='m06_gunner_syd',
            actor_name='GunnerSyd')
        cam_entry = StaticCamera(root=self, name='cam_entry', fov=25)
        path_cam_entry = MotionPath(root=self, name='Path_cam_entry', point_name='Path_cam_entry',
            path_data='{-15, 11, -25}, {0.5,0,-0.5,0},   {-10, 5, -10}, {0.8,0,-0.2,0},   {0, 4, 5}, {0.6,0,0.4,0},  {10, 1, 6}, {0.3,0,0.7,0}')
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=20, look_duration=150)
        cam_syd = LookAtCamera(root=self, name='cam_syd', fov=18, look_duration=150)

        # Исходные точки взгляда.

        # Вход.
        t = 0
        MotionEvent(root=self, group=MAIN, object_name=trent.name, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04,
            duration=50, loop=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=prisoner1.name, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04,
            duration=10, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=prisoner2.name, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04,
            duration=10, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=prisoner3.name, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04,
            duration=10, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=prisoner4.name, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04,
            duration=10, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=gunner01.name,
            anim=Male.Sc_MLBODY_STND_AIM_GUN_FRWD_000LV_XA_02, duration=2, loop=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=gunner02.name,
            anim=Male.Sc_SPCBODY_s019b_Drake_XA_STND_000LV_13, duration=2, loop=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=gunner03.name,
            anim=Male.Sc_SPCBODY_s019b_Drake_XA_STND_000LV_13, duration=2, loop=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=gunner04.name,
            anim=Male.Sc_MLBODY_STND_AIM_GUN_FRWD_000LV_XA_02, duration=2, loop=True, time_delay=t)
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_ATEASE_HOLD_000LV_XA_01, duration=1, loop=True,
            time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=syd_guard.name,
            anim=Male.Sc_MLBODY_STND_HOLD_RIFLE_MILI_000LV_XA_05, duration=555, loop=True, time_delay=t)
        cam_entry.set(group=MAIN, time_delay=t)
        PathAnimationEvent(root=self, group=MAIN, target_name=cam_entry.name, path=path_cam_entry, duration=25,
            adjust_pos=True, adjust_orient=True, start_percent=0, stop_percent=1, smooth=True, time_delay=t)
        music_main.start(group=MAIN, duration=47, loop=True, start_time=0, time_delay=t)
        t += 22.9
        MoveEvent(root=self, group=MAIN, object_name=commander.name,
            target_name=self.get_automarker_name('point_commander_start'), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.1
        MotionEvent(root=self, group=MAIN, object_name=commander.name, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01,
            duration=7, loop=True, time_delay=t)
        t += 5
        cam_trent.set(group=MAIN, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_lookpoint_commander'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=25, transition_duration=2, time_delay=t)
        t += 1
        MotionEvent(root=self, group=MAIN, object_name=trent.name, anim=Trent.Sc_MLHEAD_CONCNTRTE_TRENT_000LV_XA_,
            duration=5, trans_time=0.25, time_delay=t)
        t += 3
        MoveEvent(root=self, group=MAIN, object_name=commander.name,
            target_name=self.get_automarker_name('point_commander_around_syd'), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=syd.name,
            target_name=self.get_automarker_name('syd_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=55, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=syd.name, target_name=self.get_automarker_name('syd_eye_ik'),
            target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS', duration=55,
            transition_duration=1, time_delay=t)
        t += 1
        MotionEvent(root=self, group=MAIN, object_name=commander.name,
            anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=15, time_delay=t)
        cam_syd.set(group=MAIN, time_delay=t)
        cam_syd.move_cam(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        music_main.change_attenuation(group=MAIN, duration=5, attenuation=-15, time_delay=t)
        main_group.append_time(35)

        # m06_order_deck 10: OrderPilot.
        # Капитан Сид, мы обнаружили артефакты на борту этого фриленсера.
        t = 0
        MotionEvent(root=self, group=MAIN, object_name=commander.name, anim=Male.Sc_MLBODY_STND_SALUT_000LV_XA_03,
            duration=5, time_scale=0.8, trans_time=1, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_head_ik'),
            target_name=self.get_automarker_name('lookpoint_syd_at_commander'), duration=2, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_eye_ik'),
            target_name=self.get_automarker_name('lookpoint_syd_at_commander'), duration=1.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        line_sound = self.lookup_single_sound(10)
        SoundEvent(root=self, group=MAIN, sound_name=line_sound.get_nickname())
        main_group.append_time(4)

        # m06_order_deck 20: Ceed.
        # Отлично. Спасибо за работу, ребята. Артефакты – на склад, пленных – в кают-компанию.
        t = 0.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_head_ik'),
            target_name=self.get_automarker_name('lookpoint_syd_forward'), duration=2, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_eye_ik'),
            target_name=self.get_automarker_name('lookpoint_syd_forward'), duration=1.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 3.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_head_ik'),
            target_name=self.get_automarker_name('lookpoint_syd_at_commander'), duration=1.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_eye_ik'),
            target_name=self.get_automarker_name('lookpoint_syd_at_commander'), duration=1.1, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 3
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_head_ik'),
            target_name=self.get_automarker_name('lookpoint_syd_forward'), duration=3, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('syd_eye_ik'),
            target_name=self.get_automarker_name('lookpoint_syd_forward'), duration=2, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.5
        syd.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_ATEASE_RLEASE_000LV_XA_01, duration=15, time_scale=0.5,
            trans_time=1, time_delay=t)
        t += 0.5
        syd.motion(group=MAIN, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=15, time_scale=0.7,
            trans_time=0.5, time_delay=t)
        syd.facial(group=MAIN, index=20, auto_lip=True, extra_delay=0)
