"""m04_final: полная постановка из master; точки в m04_final.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    AttachEvent, Character, EyeIkEvent, LookAtCamera, MAIN, Male, MoveEvent, NeckIkEvent, Prop, Ship, SoundEvent, StaticCamera,
)
from story.cutscenes.anim import (
    Male, Trent,
)
from story import actors


class PropCityscapeBonusProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'li_for_cityscape_bonus'

class PlayershipProp(Ship):
    COMPOUND_TEMPLATE_NAME = 'PlayerShip'

class AlaricShipProp(Ship):
    COMPOUND_TEMPLATE_NAME = 'li_elite'


class M04FinalScene(Scene):
    DUMP_FILE = 'm04_final'
    SCENE_AMBIENT = [64, 64, 64]

    def action(self):
        main_group = self.get_group(MAIN)
        self.set_duration(72.0)

        # Персонажи, камеры, реквизит и звук.
        prop_cityscape_bonus = PropCityscapeBonusProp(root=self, name='prop_cityscape_bonus', light_group=3,
            init_point='prop_cityscape_bonus', rotate_from_quat=True, use_ambient=True)
        playership = PlayershipProp(root=self, name='PlayerShip', light_group=3, init_point='PlayerShip',
            rotate_from_quat=True)
        alaric_ship = AlaricShipProp(root=self, name='alaric_ship', light_group=3, init_point='alaric_ship',
            rotate_from_quat=True, loadout='lod_ms4_alaric')
        trent = Character(root=self, actor=actors.Trent, name='Char_trent', light_group=0,
            init_point='Char_trent', rotate_from_quat=True, use_ambient=True, appearance='trent',
            actor_name='Player', floor_height=19.881128)
        alaric = Character(root=self, actor=actors.Alaric, name='Char_alaric', light_group=0,
            init_point='Char_alaric', rotate_from_quat=True, use_ambient=True, appearance='alaric',
            actor_name='Alaric', floor_height=19.881128)
        cam_start = LookAtCamera(root=self, name='cam_start', fov=25, look_duration=300)
        cam_wlkg_trent = StaticCamera(root=self, name='cam_wlkg_trent', fov=15)
        cam_wlkg_alaric = StaticCamera(root=self, name='cam_wlkg_alaric', fov=15)
        cam_wlkg_alaric_far = StaticCamera(root=self, name='cam_wlkg_alaric_far', fov=20)
        cam_alaric_explain = LookAtCamera(root=self, name='cam_alaric_explain', fov=15, look_duration=300)
        cam_trent_explain = LookAtCamera(root=self, name='cam_trent_explain', fov=15, look_duration=300)
        cam_explain_wide = LookAtCamera(root=self, name='cam_explain_wide', fov=25, look_duration=300)

        # Исходные точки взгляда.

        # Абсолютное время исходной сцены; часы MAIN не сдвигаются.
        t = 0
        cam_start.set(group=MAIN, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=cam_wlkg_trent.name, parent_name=trent.name, duration=55,
            target_part='', target_type='ROOT', adjust_pos=True, adjust_orient=False, up='Y_AXIS',
            front='NEG_Z_AXIS', offset_x=0.75, offset_y=0.6, offset_z=2, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=cam_wlkg_alaric.name, parent_name=alaric.name, duration=55,
            target_part='', target_type='ROOT', adjust_pos=True, adjust_orient=False, up='Y_AXIS',
            front='NEG_Z_AXIS', offset_x=-0.75, offset_y=0.6, offset_z=2, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=cam_wlkg_alaric_far.name, parent_name=alaric.name,
            duration=55, target_part='', target_type='ROOT', adjust_pos=True, adjust_orient=False, up='Y_AXIS',
            front='NEG_Z_AXIS', offset_x=-1.25, offset_y=0.6, offset_z=3, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=self.get_automarker_name('wlkg_trent_front'),
            parent_name=trent.name, duration=35, target_part='Body_Head', target_type='PART', adjust_pos=True,
            adjust_orient=False, up='Y_AXIS', front='NEG_Z_AXIS', offset_z=0.5, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=self.get_automarker_name('wlkg_trent_front_near'),
            parent_name=trent.name, duration=35, target_part='Body_Head', target_type='PART', adjust_pos=True,
            adjust_orient=False, up='Y_AXIS', front='NEG_Z_AXIS', offset_x=1, offset_z=1, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=self.get_automarker_name('wlkg_trent_front_far'),
            parent_name=trent.name, duration=35, target_part='Body_Head', target_type='PART', adjust_pos=True,
            adjust_orient=False, up='Y_AXIS', front='NEG_Z_AXIS', offset_z=2, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=self.get_automarker_name('wlkg_alaric_front'),
            parent_name=alaric.name, duration=35, target_part='Body_Head', target_type='PART', adjust_pos=True,
            adjust_orient=False, up='Y_AXIS', front='NEG_Z_AXIS', offset_z=0.5, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=self.get_automarker_name('wlkg_alaric_front_near'),
            parent_name=alaric.name, duration=35, target_part='Body_Head', target_type='PART', adjust_pos=True,
            adjust_orient=False, up='Y_AXIS', front='NEG_Z_AXIS', offset_x=-1, offset_z=1, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=self.get_automarker_name('wlkg_alaric_front_far'),
            parent_name=alaric.name, duration=35, target_part='Body_Head', target_type='PART', adjust_pos=True,
            adjust_orient=False, up='Y_AXIS', front='NEG_Z_AXIS', offset_z=2, time_delay=t)
        cam_start.move_cam(group=MAIN, index=2, duration=7, smooth=True, time_delay=t)
        cam_start.move_focus(group=MAIN, index=2, duration=7, smooth=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=29, time_scale=0.75, loop=True,
            time_delay=t)
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=30, time_scale=0.75,
            start_time=1, loop=True, time_delay=t)
        t += 7
        NeckIkEvent(root=self, group=MAIN, char_name=alaric.name,
            target_name=self.get_automarker_name('wlkg_alaric_front_near'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=5, transition_duration=2, time_delay=t)
        cam_wlkg_alaric_far.set(group=MAIN, time_delay=t)
        t += 3
        EyeIkEvent(root=self, group=MAIN, char_name=alaric.name,
            target_name=self.get_automarker_name('wlkg_alaric_front_near'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=15, transition_duration=2, time_delay=t)
        t += 2
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('wlkg_trent_front_near'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=7, transition_duration=2, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=alaric.name,
            target_name=self.get_automarker_name('wlkg_trent_front_far'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=13, transition_duration=2, time_delay=t)
        t += 4
        EyeIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('wlkg_alaric_front'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=2.5, transition_duration=2, time_delay=t)
        cam_wlkg_trent.set(group=MAIN, time_delay=t)
        t += 2.5
        EyeIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('wlkg_trent_front_far'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=10.5, transition_duration=2, time_delay=t)
        t += 0.5
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('wlkg_trent_front_far'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=10, transition_duration=2, time_delay=t)
        t += 4.5
        cam_wlkg_alaric.set(group=MAIN, time_delay=t)
        t += 0.5
        trent.motion(group=MAIN, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, duration=1, time_delay=t)
        t += 1
        NeckIkEvent(root=self, group=MAIN, char_name=alaric.name,
            target_name=self.get_automarker_name('wlkg_alaric_front_far'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=5, transition_duration=2, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=alaric.name,
            target_name=self.get_automarker_name('wlkg_alaric_front_far'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=5, transition_duration=2, time_delay=t)
        t += 4
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=5, time_delay=t)
        t += 1
        cam_wlkg_trent.set(group=MAIN, time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, object_name=alaric.name,
            target_name=self.get_automarker_name('point_alaric_explain'), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.1
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=1, time_delay=t)
        t += 1.4
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_TURN_270LV_XA_04, duration=5, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('head_alaric_explain'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=10, transition_duration=2, time_delay=t)
        t += 2.99
        MoveEvent(root=self, group=MAIN, object_name=alaric.name,
            target_name=self.get_automarker_name('point_alaric_explain'), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.01
        NeckIkEvent(root=self, group=MAIN, char_name=alaric.name,
            target_name=self.get_automarker_name('alaric_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=28, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=alaric.name,
            target_name=self.get_automarker_name('alaric_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=28, transition_duration=1, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('alaric_head_ik'),
            target_name=self.get_automarker_name('head_trent_explain_front'), duration=2, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('alaric_eye_ik'),
            target_name=self.get_automarker_name('head_trent_explain'), duration=1.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        cam_alaric_explain.set(group=MAIN, time_delay=t)
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, duration=5, time_scale=0.6,
            start_time=1, time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_alaric_explain_front'), duration=0.1, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_alaric_explain'), duration=0.1, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=33, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=33, transition_duration=1, time_delay=t)
        t += 2
        cam_trent_explain.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=3, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=5,
            time_scale=0.8, trans_time=1, time_delay=t)
        t += 5
        cam_explain_wide.set(group=MAIN, time_delay=t)
        cam_explain_wide.move_cam(group=MAIN, index=2, duration=14, smooth=True, time_delay=t)
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, duration=10, time_scale=0.6,
            time_delay=t)
        t += 2
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_trent_explain_outside'), duration=3.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_trent_explain_outside'), duration=4, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.5
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_TURN_045LV_XA_04, duration=5, trans_time=1, time_delay=t)
        t += 3
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=5,
            time_scale=0.7, trans_time=1, time_delay=t)
        trent.motion(group=MAIN, anim=Trent.Sc_MLHEAD_SAD_CONCERN_TRENT_000LV_XA_, duration=12, time_scale=0.6,
            trans_time=1, time_delay=t)
        t += 0.5
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_LHNDUP_TRNS_000LV_XA_01, duration=3,
            trans_time=1.5, time_delay=t)
        t += 1
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_LHND_CASL_000LV_xa_04, duration=4.5,
            trans_time=1.5, loop=True, time_delay=t)
        t += 2.5
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=5, time_scale=0.5,
            trans_time=1, time_delay=t)
        t += 2
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_LHNDDN_TRNS_000LV_XA_01, duration=3,
            trans_time=1.5, time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_alaric_explain_front'), duration=2.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_alaric_explain'), duration=1.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.5
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_TURN_315LV_XA_02, duration=15, time_delay=t)
        t += 1
        cam_trent_explain.set(group=MAIN, time_delay=t)
        t += 4.3
        alaric.motion(group=MAIN, anim=Male.Sc_MLHEAD_MOTION_BREATHE_HEAVY_000LV_XA_, duration=5, time_scale=0.2,
            start_time=0.25, trans_time=0.1, time_delay=t)
        t += 0.2
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('alaric_head_ik'),
            target_name=self.get_automarker_name('head_alaric_explain_front'), duration=1, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('alaric_eye_ik'),
            target_name=self.get_automarker_name('head_alaric_explain_front'), duration=1, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        cam_alaric_explain.set(group=MAIN, time_delay=t)
        t += 1
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WALK_TRNS_270LV_XA_02, duration=4, time_delay=t)
        t += 0.5
        alaric.motion(group=MAIN, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=5, trans_time=1, time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_alaric_explain_front'), duration=2, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 1
        cam_trent_explain.set(group=MAIN, time_delay=t)
        t += 1
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=5,
            time_scale=0.8, start_time=0.3, trans_time=1, time_delay=t)
        t += 3
        MoveEvent(root=self, group=MAIN, object_name=alaric.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WALK_TRNS_180LV_XA_02, duration=10, time_scale=0.8,
            trans_time=1, time_delay=t)

        # m04_final 10: Круто, Трент, ты умеешь находить себе заказчиков и покровителей.
        self.add_group('voice_37', time=0.5)
        line_sound = self.lookup_single_sound(10)
        SoundEvent(root=self, group='voice_37', sound_name=line_sound.get_nickname())

        # m04_final 20: А так же врагов и убийц.
        self.add_group('voice_38', time=4.5)
        line_sound = self.lookup_single_sound(20)
        SoundEvent(root=self, group='voice_38', sound_name=line_sound.get_nickname())

        # m04_final 30: Да ладно тебе. Ты фриленесером работать стал всего ничего, и вот уже задания на уровне правительств с соответствующей оплатой.
        self.add_group('voice_39', time=7)
        alaric.facial(group='voice_39', index=30, auto_lip=True, extra_delay=0, append=False)

        # m04_final 40: Ага, и одно из правительств уже назначило награду за мою голову, и я сомневаюсь что у этого правительства короткая память.
        self.add_group('voice_42', time=16)
        trent.facial(group='voice_42', index=40, auto_lip=True, extra_delay=0, append=False)

        # m04_final 50: Да ладно тебе, с таким прикрытием рейнландцы пупок себе скорее надорвут, чем нас достанут.
        self.add_group('voice_47', time=23.5)
        alaric.facial(group='voice_47', index=50, auto_lip=True, extra_delay=0, append=False)

        # m04_final 60: С каким-таким прикрытием? Ну-ка Аларик, чего я не знаю?
        self.add_group('voice_50', time=30)
        trent.facial(group='voice_50', index=60, auto_lip=True, extra_delay=0, append=False)

        # m04_final 70: Эта мисс Хетчер, ты в курсе кто она?
        self.add_group('voice_59', time=35)
        alaric.facial(group='voice_59', index=70, auto_lip=True, extra_delay=0, append=False)

        # m04_final 80: Ну конечно в курсе. Я знаю её уже целых три часа, я в курсе. Аларик, короче, мать твою!
        self.add_group('voice_64', time=38)
        trent.facial(group='voice_64', index=80, auto_lip=True, extra_delay=0, append=False)

        # m04_final 90: Она офицер в одной из спецслужб Либерти.
        self.add_group('voice_69', time=43)
        alaric.facial(group='voice_69', index=90, auto_lip=True, extra_delay=0, append=False)

        # m04_final 100: О боже! Нет... Опять...
        self.add_group('voice_80', time=46.5)
        trent.facial(group='voice_80', index=100, auto_lip=True, extra_delay=0, append=False)

        # m04_final 110: Ты не понимаешь, это настолько крутая спецслужба, что другие спецслужбы даже не подозревают о её существовании.
        self.add_group('voice_86', time=49.5)
        alaric.facial(group='voice_86', index=110, auto_lip=True, extra_delay=0, append=False)

        # m04_final 120: Аларик, тогда ты то откуда про это знаешь?
        self.add_group('voice_93', time=57.5)
        trent.facial(group='voice_93', index=120, auto_lip=True, extra_delay=0, append=False)

        # m04_final 130: А... Э-э-э...
        self.add_group('voice_100', time=62)
        line_sound = self.lookup_single_sound(130)
        SoundEvent(root=self, group='voice_100', sound_name=line_sound.get_nickname())

        # m04_final 140: Короче, трындец, опять вляпался.
        self.add_group('voice_106', time=65)
        trent.facial(group='voice_106', index=140, auto_lip=True, extra_delay=0, append=False)
