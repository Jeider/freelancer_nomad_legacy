"""m05_equip: полная постановка из master; точки в m05_equip.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character, ConnectHardpointEvent, EyeIkEvent, Female, Light, LookAtCamera, LookAtEvent, MAIN, Male, MotionEvent, MoveEvent, NeckIkEvent, Prop, RotateAxisEvent, Sound, StaticCamera,
)
from story.cutscenes.anim import (
    Female, Male, Trent,
)
from story import actors


class PropPdaProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'pda'

class HandProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'equip_hand1_sml'

class PodProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'equip_pod'

class PodaProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'equip_pod'

class PodbProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'equip_pod'

class PropMaglevProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'maglev'

class CharHatcher2Actor(actors.Actor):
    NAME = 'hatcher2'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'hatcher'

class CharMedic1Actor(actors.Actor):
    NAME = 'medic1'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'medic_3'


class M05EquipScene(Scene):
    DUMP_FILE = 'm05_equip'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Персонажи, камеры, реквизит и звук.
        ambi_additional = Light(root=self, name='ambi_additional', point_name='ambi_additional', extra_name='',
            light_group=0, hidden=False, rotate_from_quat=True, diffuse=[0.92549, 0.835294, 0.92549],
            ambient=[0.121569, 0.121569, 0.121569], direction=[0, 0, 1], light_type='L_POINT', range=150,
            cutoff=30, theta=26.999985, color=[180, 180, 180], attenuation=[1, 0, 0.003], on=True)
        sound_cart_start = Sound(root=self, name='sound_cart_start', sound='equipment_cart_start', attenuation=-5,
            dmin=50, dmax=250, priority=None)
        sound_cart_stop = Sound(root=self, name='sound_cart_stop', sound='equipment_cart_stop', attenuation=-5,
            dmin=50, dmax=250, priority=None)
        sound_cart_loop = Sound(root=self, name='sound_cart_loop', sound='equipment_cart_loop', attenuation=-25,
            dmin=50, dmax=250, priority=None)
        sound_syd_clang = Sound(root=self, name='sound_syd_clang', sound='sfx_syd_clang', attenuation=-10,
            dmin=50, dmax=250, priority=None)
        music_hall_ambient = Sound(root=self, name='music_hall_ambient', sound='ambience_equip_ground_larger',
            attenuation=0, dmin=50, dmax=300, priority='Story_Sound_1')
        music_reveal_and_exposition = Sound(root=self, name='music_reveal_and_exposition',
            sound='rtc_music_reveal_and_exposition', attenuation=-12, dmin=50, dmax=300, priority='Story_Sound_1')
        music_anticipation_light = Sound(root=self, name='music_anticipation_light',
            sound='rtc_music_anticipation_light', attenuation=-8, dmin=50, dmax=300, priority='Story_Sound_1')
        music_reveal_special_mystery = Sound(root=self, name='music_reveal_special_mystery',
            sound='rtc_music_reveal_special_mystery', attenuation=-12, dmin=50, dmax=300, priority='Story_Sound_1')
        prop_pda = PropPdaProp(root=self, name='prop_pda', light_group=0, init_point='prop_pda',
            rotate_from_quat=True)
        hand = HandProp(root=self, name='hand', light_group=0, init_point='hand', rotate_from_quat=True,
            use_ambient=True)
        pod = PodProp(root=self, name='pod', light_group=0, init_point='pod', rotate_from_quat=True,
            category='Equipment Cart')
        poda = PodaProp(root=self, name='podA', light_group=0, init_point='podA', rotate_from_quat=True,
            category='Equipment Cart')
        podb = PodbProp(root=self, name='podB', light_group=0, init_point='podB', rotate_from_quat=True,
            category='Equipment Cart')
        prop_maglev = PropMaglevProp(root=self, name='Prop_Maglev', light_group=0, init_point='Prop_Maglev',
            rotate_from_quat=True)
        trent = Character(root=self, actor=actors.Trent, name='Char_trent', light_group=0,
            init_point='Char_trent', rotate_from_quat=True, appearance='trent', actor_name='player')
        hatcher = Character(root=self, actor=actors.Hatcher, name='Char_hatcher', light_group=0,
            init_point='Char_hatcher', rotate_from_quat=True, appearance='hatcher', actor_name='hatcher')
        hatcher2 = Character(root=self, actor=CharHatcher2Actor, name='Char_hatcher2', light_group=0,
            init_point='Char_hatcher2', rotate_from_quat=True, appearance='hatcher', actor_name='hatcher2')
        mandrake = Character(root=self, actor=actors.Mandrake, name='Char_mandrake', light_group=0,
            init_point='Char_mandrake', rotate_from_quat=True, appearance='mandrake', actor_name='mandrake')
        medic1 = Character(root=self, actor=CharMedic1Actor, name='Char_medic1', light_group=0,
            init_point='Char_medic1', rotate_from_quat=True, appearance='medic_3', actor_name='medic_1')
        cam_start = LookAtCamera(root=self, name='cam_start', fov=35, look_duration=100)
        cam_mandrake = LookAtCamera(root=self, name='cam_mandrake', fov=20, look_duration=100)
        cam_mandrake_top = LookAtCamera(root=self, name='cam_mandrake_top', fov=20, look_duration=100)
        cam_hatcher_down = LookAtCamera(root=self, name='cam_hatcher_down', fov=10, look_duration=100)
        cam_hatcher = LookAtCamera(root=self, name='cam_hatcher', fov=16, look_duration=100)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=15, look_duration=200)


        # Исходные точки взгляда.

        # Вход.
        t = 0
        RotateAxisEvent(root=self, group=MAIN, object_name=poda.name, angle=40, axis='Z_AXIS', duration=0.01,
            smooth=False, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=podb.name, angle=40, axis='Z_AXIS', duration=0.01,
            smooth=False, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=pod.name,
            target_name=self.get_automarker_name('pod_move_bottom'), duration=5, smooth=True, adjust_pos=True,
            adjust_orient=False, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=hand.name,
            target_name=self.get_automarker_name('hand_move_bottom'), duration=5, smooth=True, adjust_pos=True,
            adjust_orient=False, time_delay=t)
        mandrake.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=15, loop=True,
            time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=medic1.name,
            anim=Male.Sc_MLBODY_STND_DEALR_PDA_000LV_XA_09, duration=8, time_scale=0.75, start_time=2,
            time_delay=t)
        ConnectHardpointEvent(root=self, group=MAIN, target_name=prop_pda.name, parent_name=medic1.name,
            duration=50, target_hardpoint='Hp_LHand_PDA', parent_hardpoint='HpLeftConnect', time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_XB_04, duration=55, loop=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLHAND_NEUT_LEFT_000LV_A_00, duration=5, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLHAND_NEUT_RGHT_000LV_A_00, duration=5, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STROLL_000LV_XA_01, duration=8.5, loop=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=hatcher2.name, anim=Female.Sc_FMBODY_STND_000LV_B_07,
            duration=9, time_delay=t)
        cam_start.move_cam(group=MAIN, index=2, duration=7, smooth=True, time_delay=t)
        cam_start.move_focus(group=MAIN, index=2, duration=7, smooth=True, time_delay=t)
        sound_cart_loop.change_attenuation(group=MAIN, duration=1, attenuation=-5, time_delay=t)
        music_hall_ambient.start(group=MAIN, duration=108, loop=True, start_time=0, time_delay=t)
        t += 0.01
        cam_start.set(group=MAIN, time_delay=t)
        t += 0.29
        sound_cart_loop.start(group=MAIN, duration=3.2, loop=True, start_time=0, time_delay=t)
        t += 3.2
        RotateAxisEvent(root=self, group=MAIN, object_name=pod.name, angle=38, axis='X_AXIS', duration=1.5,
            smooth=True, time_delay=t)
        sound_cart_stop.start(group=MAIN, duration=2, loop=False, start_time=0, time_delay=t)
        t += 1
        sound_syd_clang.start(group=MAIN, duration=2, loop=False, start_time=0, time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, object_name=hand.name,
            target_name=self.get_automarker_name('hand_move_top'), duration=7, smooth=True, adjust_pos=True,
            adjust_orient=False, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name, target_name=hatcher.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=15, transition_duration=2,
            time_delay=t)
        sound_cart_start.start(group=MAIN, duration=2, loop=False, start_time=0, time_delay=t)
        t += 1
        sound_cart_loop.change_attenuation(group=MAIN, duration=5, attenuation=-25, time_delay=t)
        t += 0.3
        sound_cart_loop.start(group=MAIN, duration=10, loop=True, start_time=0, time_delay=t)
        t += 0.7
        NeckIkEvent(root=self, group=MAIN, char_name=hatcher.name,
            target_name=self.get_automarker_name('hatcher_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=500, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=hatcher.name,
            target_name=self.get_automarker_name('hatcher_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=500, transition_duration=1, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=mandrake.name,
            target_name=self.get_automarker_name('mandrake_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=500, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=mandrake.name,
            target_name=self.get_automarker_name('mandrake_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=500, transition_duration=1, time_delay=t)
        # cam_hatcher_down.set(group=MAIN, time_delay=t)
        t += 1
        music_hall_ambient.change_attenuation(group=MAIN, duration=2, attenuation=-10, time_delay=t)
        main_group.append_time(8.5)

        # m05_equip 10: Hatcher.
        # Профессор Мандрейк.
        # t = 0
        # hatcher.facial(group=MAIN, index=10, auto_lip=True)

        # m05_equip 20: Mandrake.
        # Мисс Хетчер.
        t = 0
        cam_mandrake_top.set(group=MAIN, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=medic1.name,
            anim=Male.Sc_MLBODY_STND_WALK_TRNS_270LV_XA_02, duration=12, time_delay=t)
        t += 1.5
        MotionEvent(root=self, group=MAIN, object_name=medic1.name, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01,
            duration=55, loop=True, time_delay=t)


        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STROLL_STND_TRNS_000LV_XA_01, duration=9,
            time_scale=0.825, time_delay=0)
        mandrake.facial(group=MAIN, index=10, auto_lip=True)

        # m05_equip 30: Hatcher.
        # Профессор, вы лишний час просидели в капсуле из-за этого идиота Тилтона.
        t = 0
        cam_hatcher_down.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=9,
            time_scale=0.9, time_delay=t)
        t += 1.5
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_FSTHIPB_HOLD_000LV_XA_01, duration=46,
            trans_time=0.5, loop=True, time_delay=t)
        hatcher.facial(group=MAIN, index=20, auto_lip=True,
                       auto_anim_force=Female.Sc_dx_s070x_2701_Jacobi, auto_anim_force_seconds=3)

        # m05_equip 40: Mandrake.
        # Этот недоросль, хотя, скорее, переросль, все никак не может отделаться от навязчивой идеи подловить
        # вас, мисс Хетчер.
        t = 0
        cam_mandrake.set(group=MAIN, time_delay=t)
        mandrake.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_TALK_000LV_A_16, duration=10, start_time=1,
            time_delay=t)
        mandrake.facial(group=MAIN, index=30, auto_lip=True)

        # m05_equip 50: Hatcher.
        # Ага, и чем дальше, тем проще и тупее его схемы.
        t = 0
        cam_hatcher_down.set(group=MAIN, time_delay=t)
        hatcher.facial(group=MAIN, index=40, auto_lip=True, auto_anim_scale=0.8,
                       auto_anim_force=Female.Sc_dx_s069x_1701_Jacobi, auto_anim_force_seconds=4)

        # m05_equip 60: Mandrake.
        # Все-таки стоит опасаться таких людей. По теории больших чисел, рано или поздно они смогут добиться
        # своего.
        t = 0
        cam_mandrake.set(group=MAIN, time_delay=t)
        mandrake.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=10, loop=True,
            time_delay=t)
        mandrake.facial(group=MAIN, index=50, auto_lip=True)
        main_group.append_time(0.5)


        cam_hatcher_down.set(group=MAIN)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=9,
            time_scale=0.9, time_delay=1)
        hatcher.facial(group=MAIN, index=60, auto_lip=True)


        cam_mandrake.set(group=MAIN)
        mandrake.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_SHRG_SHLDRS_SMALL_000LV_XA_03, duration=9,
                       trans_time=1, time_scale=0.4)
        mandrake.facial(group=MAIN, index=70, auto_lip=True)
        main_group.append_time(0.5)


        cam_hatcher_down.set(group=MAIN)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_SHRG_SHLDRS_BIG_000LV_XA_02, duration=9,
                       trans_time=1, time_scale=0.6, time_delay=1)
        hatcher.facial(group=MAIN, index=80, auto_lip=True)


        cam_mandrake.set(group=MAIN)
        mandrake.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=10, loop=True,
            trans_time=1, time_delay=t)
        mandrake.facial(group=MAIN, index=90, auto_lip=True)


        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=500, transition_duration=1, time_delay=-2)
        EyeIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=500, transition_duration=1, time_delay=-2)


        t = 0
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_hatcher_near_mandrake_half'), duration=2.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_hatcher_near_mandrake'), duration=1.75, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        cam_trent.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_GEST_HNDS_WAIT_000LV_XA_02, duration=4, time_delay=0)

        trent.facial(group=MAIN, index=100, auto_lip=True)

        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=-0.5)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.25, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=-0.5)

        cam_hatcher.set(group=MAIN)

        RotateAxisEvent(root=self, group=MAIN, object_name=hatcher.name, angle=25, axis='Y_AXIS', duration=0.01,
            smooth=False, time_delay=-1)

        hatcher.facial(group=MAIN, index=110, auto_lip=True)

        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_hatcher_near_mandrake'), duration=2, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_hatcher_near_mandrake'), duration=1.25, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)

        cam_trent.set(group=MAIN)

        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=9, trans_time=1, time_scale=0.8)

        trent.facial(group=MAIN, index=120, auto_lip=True)


        cam_hatcher.set(group=MAIN)
        hatcher.facial(group=MAIN, index=130, auto_lip=True)

        cam_trent.set(group=MAIN)

        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=9, trans_time=1, time_scale=0.8)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, duration=9, trans_time=1,
                     time_scale=0.8, time_delay=2)

        trent.facial(group=MAIN, index=140, auto_lip=True)


        cam_hatcher.set(group=MAIN)

        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=9, trans_time=1, time_scale=0.8)

        hatcher.facial(group=MAIN, index=150, auto_lip=True)

        cam_trent.set(group=MAIN)

        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, duration=9, trans_time=1,
                     time_scale=0.8)
        trent.facial(group=MAIN, index=160, auto_lip=True)


        main_group.append_time(2)

        return
