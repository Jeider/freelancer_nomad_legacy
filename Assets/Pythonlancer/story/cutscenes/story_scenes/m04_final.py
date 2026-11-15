"""m04_final: постановка для ручного редактирования.

Точки: SCENES/m04_final.blend → DUMPS/m04_final.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — абсолютные секунды исходной сцены; часы MAIN не сдвигаются.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character,
    EyeIkEvent,
    LookAtCamera,
    MAIN,
    MoveEvent,
    NeckIkEvent,
    PlayerShip,
    Prop,
    Ship,
    SoundEvent,
    StaticCamera,
)
from story.cutscenes.anim import (
    Male,
    Trent,
)
from story.cutscenes.source_extensions import (
    SourceAttachEvent,
    preserve_entity,
)
from story import actors


class PropPropCityscapeBonus(Prop):
    COMPOUND_TEMPLATE_NAME = 'li_for_cityscape_bonus'
    SRT_GRP = 0
    USR_FLG = 0


class PropPlayership(Ship):
    COMPOUND_TEMPLATE_NAME = 'PlayerShip'
    SRT_GRP = 0
    USR_FLG = 0


class PropAlaricShip(Ship):
    COMPOUND_TEMPLATE_NAME = 'li_elite'
    SRT_GRP = 0
    USR_FLG = 0



class M04FinalScene(Scene):
    DUMP_FILE = 'm04_final'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(72.0)
        prop_cityscape_bonus = PropPropCityscapeBonus(root=self, name='prop_cityscape_bonus', light_group=3,
            init_point='prop_cityscape_bonus', rotate_from_quat=True, use_ambient=True)
        preserve_entity(prop_cityscape_bonus, userprops={'category': 'Prop'})
        PlayerShip = PropPlayership(root=self, name='PlayerShip', light_group=3, init_point='PlayerShip',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(PlayerShip, userprops={'category': 'Spaceship'})
        alaric_ship = PropAlaricShip(root=self, name='alaric_ship', light_group=3, init_point='alaric_ship',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(alaric_ship, userprops={'category': 'Spaceship', 'loadout': 'lod_ms4_alaric'})
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=True, floor_height=19.881128)
        preserve_entity(trent, template_name='trent', userprops={'actor': 'Player', 'category': 'Character'})
        alaric = Character(root=self, actor=actors.Alaric, light_group=0, init_point='Char_alaric', rotate_from_quat=True,
            use_ambient=True, floor_height=19.881128)
        preserve_entity(alaric, template_name='alaric', userprops={'actor': 'Alaric', 'category': 'Character'})
        cam_start = LookAtCamera(root=self, name='cam_start', fov=25, farplane=5000, look_duration=300)
        preserve_entity(cam_start)
        cam_wlkg_trent = StaticCamera(root=self, name='cam_wlkg_trent', fov=15, farplane=5000)
        preserve_entity(cam_wlkg_trent)
        cam_wlkg_alaric = StaticCamera(root=self, name='cam_wlkg_alaric', fov=15, farplane=5000)
        preserve_entity(cam_wlkg_alaric)
        cam_wlkg_alaric_far = StaticCamera(root=self, name='cam_wlkg_alaric_far', fov=20, farplane=5000)
        preserve_entity(cam_wlkg_alaric_far)
        cam_alaric_explain = LookAtCamera(root=self, name='cam_alaric_explain', fov=15, farplane=5000, look_duration=300)
        preserve_entity(cam_alaric_explain)
        cam_trent_explain = LookAtCamera(root=self, name='cam_trent_explain', fov=15, farplane=5000, look_duration=300)
        preserve_entity(cam_trent_explain)
        cam_explain_wide = LookAtCamera(root=self, name='cam_explain_wide', fov=25, farplane=5000, look_duration=300)
        preserve_entity(cam_explain_wide)

        # Действия по абсолютному времени сцены.
        t = 0
        cam_start.set(group=MAIN, time_delay=t)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['cam_wlkg_trent', 'Char_trent'], duration=55,
            offset=[0.75, 0.6, 2], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='POSITION')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['cam_wlkg_alaric', 'Char_alaric'], duration=55,
            offset=[-0.75, 0.6, 2], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='POSITION')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['cam_wlkg_alaric_far', 'Char_alaric'], duration=55,
            offset=[-1.25, 0.6, 3], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='POSITION')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['automarker_wlkg_trent_front', 'Char_trent'],
            duration=35, offset=[0, 0, 0.5], up='Y_AXIS', front='NEG_Z_AXIS', target_part='Body_Head', target_type='PART',
            flags='POSITION')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['automarker_wlkg_trent_front_near', 'Char_trent'],
            duration=35, offset=[1, 0, 1], up='Y_AXIS', front='NEG_Z_AXIS', target_part='Body_Head', target_type='PART',
            flags='POSITION')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['automarker_wlkg_trent_front_far', 'Char_trent'],
            duration=35, offset=[0, 0, 2], up='Y_AXIS', front='NEG_Z_AXIS', target_part='Body_Head', target_type='PART',
            flags='POSITION')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['automarker_wlkg_alaric_front', 'Char_alaric'],
            duration=35, offset=[0, 0, 0.5], up='Y_AXIS', front='NEG_Z_AXIS', target_part='Body_Head', target_type='PART',
            flags='POSITION')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['automarker_wlkg_alaric_front_near', 'Char_alaric'],
            duration=35, offset=[-1, 0, 1], up='Y_AXIS', front='NEG_Z_AXIS', target_part='Body_Head', target_type='PART',
            flags='POSITION')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['automarker_wlkg_alaric_front_far', 'Char_alaric'],
            duration=35, offset=[0, 0, 2], up='Y_AXIS', front='NEG_Z_AXIS', target_part='Body_Head', target_type='PART',
            flags='POSITION')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_start', target_name='automarker_cam_start_pos2',
            duration=7, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_start_focus',
            target_name='automarker_cam_start_marker_pos2', duration=7, smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=29, time_scale=0.75, loop=True)
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=30, time_scale=0.75,
            start_time=1, loop=True)
        t += 7
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_alaric',
            target_name='automarker_wlkg_alaric_front_near', duration=5, transition_duration=2, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        cam_wlkg_alaric_far.set(group=MAIN, time_delay=t)
        t += 3
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_alaric',
            target_name='automarker_wlkg_alaric_front_near', duration=15, transition_duration=2, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 2
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent',
            target_name='automarker_wlkg_trent_front_near', duration=7, transition_duration=2, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_alaric',
            target_name='automarker_wlkg_trent_front_far', duration=13, transition_duration=2, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 4
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_wlkg_alaric_front',
            duration=2.5, transition_duration=2, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        cam_wlkg_trent.set(group=MAIN, time_delay=t)
        t += 2.5
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent',
            target_name='automarker_wlkg_trent_front_far', duration=10.5, transition_duration=2, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 0.5
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent',
            target_name='automarker_wlkg_trent_front_far', duration=10, transition_duration=2, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 4.5
        cam_wlkg_alaric.set(group=MAIN, time_delay=t)
        t += 0.5
        trent.motion(group=MAIN, time_delay=t, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, duration=1)
        t += 1
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_alaric',
            target_name='automarker_wlkg_alaric_front_far', duration=5, transition_duration=2, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_alaric',
            target_name='automarker_wlkg_alaric_front_far', duration=5, transition_duration=2, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 4
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=5)
        t += 1
        cam_wlkg_trent.set(group=MAIN, time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_alaric',
            target_name='automarker_point_alaric_explain', duration=0.001, smooth=False)
        t += 0.1
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=1)
        t += 1.4
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_TURN_270LV_XA_04, duration=5)
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent',
            target_name='automarker_head_alaric_explain', duration=10, transition_duration=2, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 2.99
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_alaric',
            target_name='automarker_point_alaric_explain', duration=0.001, smooth=False)
        t += 0.01
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_alaric', target_name='automarker_alaric_head_ik',
            duration=28, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_alaric', target_name='automarker_alaric_eye_ik',
            duration=28, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_alaric_head_ik',
            target_name='automarker_head_trent_explain_front', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_alaric_eye_ik',
            target_name='automarker_head_trent_explain', duration=1.5, smooth=True)
        cam_alaric_explain.set(group=MAIN, time_delay=t)
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, duration=5, time_scale=0.6,
            start_time=1)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_alaric_explain_front', duration=0.1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_alaric_explain', duration=0.1, smooth=True)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=33, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_eye_ik',
            duration=33, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 2
        cam_trent_explain.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=3)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=5,
            time_scale=0.8, trans_time=1)
        t += 5
        cam_explain_wide.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_explain_wide',
            target_name='automarker_cam_explain_wide_pos2', duration=14, smooth=True)
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, duration=10,
            time_scale=0.6)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_trent_explain_outside', duration=3.5, smooth=True)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_trent_explain_outside', duration=4, smooth=True)
        t += 0.5
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_TURN_045LV_XA_04, duration=5, trans_time=1)
        t += 3
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=5,
            time_scale=0.7, trans_time=1)
        trent.motion(group=MAIN, time_delay=t, anim=Trent.Sc_MLHEAD_SAD_CONCERN_TRENT_000LV_XA_, duration=12,
            time_scale=0.6, trans_time=1)
        t += 0.5
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_LHNDUP_TRNS_000LV_XA_01, duration=3,
            trans_time=1.5)
        t += 1.0
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_LHND_CASL_000LV_xa_04, duration=4.5,
            loop=True, trans_time=1.5)
        t += 2.5
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=5,
            time_scale=0.5, trans_time=1)
        t += 2
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_LHNDDN_TRNS_000LV_XA_01, duration=3,
            trans_time=1.5)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_head_ik',
            target_name='automarker_head_alaric_explain_front', duration=2.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_alaric_explain', duration=1.5, smooth=True)
        t += 0.5
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_TURN_315LV_XA_02, duration=15)
        t += 1.0
        cam_trent_explain.set(group=MAIN, time_delay=t)
        t += 4.3
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_MOTION_BREATHE_HEAVY_000LV_XA_, duration=5,
            time_scale=0.2, start_time=0.25, trans_time=0.1)
        t += 0.2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_alaric_head_ik',
            target_name='automarker_head_alaric_explain_front', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_alaric_eye_ik',
            target_name='automarker_head_alaric_explain_front', duration=1, smooth=True)
        cam_alaric_explain.set(group=MAIN, time_delay=t)
        t += 1
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WALK_TRNS_270LV_XA_02, duration=4)
        t += 0.5
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=5, trans_time=1)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_trent_eye_ik',
            target_name='automarker_head_alaric_explain_front', duration=2, smooth=True)
        t += 1
        cam_trent_explain.set(group=MAIN, time_delay=t)
        t += 1
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=5,
            time_scale=0.8, start_time=0.3, trans_time=1)
        t += 3
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_alaric', target_name='offscreen', duration=0.001,
            smooth=False)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WALK_TRNS_180LV_XA_02, duration=10, time_scale=0.8,
            trans_time=1)
        self.add_group('voice_37', time=0.5)
        voice_sound = self.lookup_single_sound(10)
        SoundEvent(root=self, group='voice_37', sound_name=voice_sound.get_nickname())
        self.add_group('voice_38', time=4.5)
        voice_sound = self.lookup_single_sound(20)
        SoundEvent(root=self, group='voice_38', sound_name=voice_sound.get_nickname())
        self.add_group('voice_39', time=7)
        alaric.facial(group='voice_39', index=30, append=False, auto_lip=True, extra_delay=0)
        self.add_group('voice_42', time=16)
        trent.facial(group='voice_42', index=40, append=False, auto_lip=True, extra_delay=0)
        self.add_group('voice_47', time=23.5)
        alaric.facial(group='voice_47', index=50, append=False, auto_lip=True, extra_delay=0)
        self.add_group('voice_50', time=30)
        trent.facial(group='voice_50', index=60, append=False, auto_lip=True, extra_delay=0)
        self.add_group('voice_59', time=35)
        alaric.facial(group='voice_59', index=70, append=False, auto_lip=True, extra_delay=0)
        self.add_group('voice_64', time=38)
        trent.facial(group='voice_64', index=80, append=False, auto_lip=True, extra_delay=0)
        self.add_group('voice_69', time=43)
        alaric.facial(group='voice_69', index=90, append=False, auto_lip=True, extra_delay=0)
        self.add_group('voice_80', time=46.5)
        trent.facial(group='voice_80', index=100, append=False, auto_lip=True, extra_delay=0)
        self.add_group('voice_86', time=49.5)
        alaric.facial(group='voice_86', index=110, append=False, auto_lip=True, extra_delay=0)
        self.add_group('voice_93', time=57.5)
        trent.facial(group='voice_93', index=120, append=False, auto_lip=True, extra_delay=0)
        self.add_group('voice_100', time=62)
        voice_sound = self.lookup_single_sound(130)
        SoundEvent(root=self, group='voice_100', sound_name=voice_sound.get_nickname())
        self.add_group('voice_106', time=65)
        trent.facial(group='voice_106', index=140, append=False, auto_lip=True, extra_delay=0)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M04FinalScene
