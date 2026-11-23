"""m08_offer_accept: полная постановка из master; точки в m08_offer_accept.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character, EyeIkEvent, Female, LookAtCamera, MAIN, Male, MoveEvent, NeckIkEvent, RotateAxisEvent,
)
from story.cutscenes.anim import (
    Female, Male,
)
from story import actors



class M08OfferAcceptScene(Scene):
    DUMP_FILE = 'm08_offer_accept'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Персонажи, камеры, реквизит и звук.
        kaytlin = Character(root=self, actor=actors.Kaitlyn, name='Char_kaytlin', light_group=0,
            init_point='Char_kaytlin', rotate_from_quat=True, appearance='kaytlin', actor_name='Kaytlin')
        brighton = Character(root=self, actor=actors.Brighton, name='Char_brighton', light_group=0,
            init_point='Char_brighton', rotate_from_quat=True, appearance='brighton', actor_name='Brighton')
        darcy = Character(root=self, actor=actors.Darcy, name='Char_darcy', light_group=0,
            init_point='Char_darcy', rotate_from_quat=True, appearance='darcy', actor_name='Darcy')
        trent = Character(root=self, actor=actors.Trent, name='Char_trent', light_group=0,
            init_point='Char_trent', rotate_from_quat=True, appearance='trent', actor_name='Player')
        cam_start = LookAtCamera(root=self, name='cam_start', fov=20, look_duration=70)
        cam_start_darcy = LookAtCamera(root=self, name='cam_start_darcy', fov=20, look_duration=70)
        cam_start_trent = LookAtCamera(root=self, name='cam_start_trent', fov=20, look_duration=70)
        cam_greetings = LookAtCamera(root=self, name='cam_greetings', fov=20, look_duration=70)
        cam_greetings_kaytlin = LookAtCamera(root=self, name='cam_greetings_kaytlin', fov=15, look_duration=70)
        cam_darcy_sit = LookAtCamera(root=self, name='cam_darcy_sit', fov=22, look_duration=70)
        cam_brighton = LookAtCamera(root=self, name='cam_brighton', fov=18, look_duration=710)
        cam_brighton_near = LookAtCamera(root=self, name='cam_brighton_near', fov=18, look_duration=710)
        cam_trent_sit = LookAtCamera(root=self, name='cam_trent_sit', fov=18, look_duration=710)
        cam_trent_far = LookAtCamera(root=self, name='cam_trent_far', fov=18, look_duration=710)
        cam_trent_near = LookAtCamera(root=self, name='cam_trent_near', fov=18, look_duration=710)
        cam_trent_xnear = LookAtCamera(root=self, name='cam_trent_xnear', fov=15, look_duration=710)
        cam_kaytlin = LookAtCamera(root=self, name='cam_kaytlin', fov=15, look_duration=710)

        # Исходные точки взгляда.

        # Вход.
        main_group.append_time(0)

        # m08_offer 440: Trent.
        # Олимпийский принцип? За пятьдесят тысяч? Возможно, я сильно поторопился, сказав, что в секторе
        # Сириуса нет британской короны.
        t = 0
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, duration=10, time_delay=t)
        kaytlin.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_IDLE_000LV_XA_05, duration=10, time_delay=t)
        brighton.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=100, time_scale=0.6,
            loop=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=100, time_scale=0.6,
            loop=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('kaytlin_ik_not_interested_head'),
            target_name=self.get_automarker_name('kaytlin_ik_not_interested_head_pos3'), duration=0, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('kaytlin_ik_not_interested_eye'),
            target_name=self.get_automarker_name('kaytlin_ik_not_interested_eye_pos3'), duration=0, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('darcy_head_ik'),
            target_name=self.get_automarker_name('head_trent_front'), duration=0, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('darcy_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=0, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=darcy.name,
            target_name=self.get_automarker_name('darcy_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=2555, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=darcy.name,
            target_name=self.get_automarker_name('darcy_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=2555, transition_duration=1, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=brighton.name,
            target_name=self.get_automarker_name('brighton_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=2555, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=brighton.name,
            target_name=self.get_automarker_name('brighton_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=2555, transition_duration=1, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=555, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=555, transition_duration=1, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=kaytlin.name,
            target_name=self.get_automarker_name('kaytlin_ik_not_interested_head'), target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS', duration=1000, transition_duration=2, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=kaytlin.name,
            target_name=self.get_automarker_name('kaytlin_ik_not_interested_eye'), target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS', duration=1000, transition_duration=2, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_kaytlin_front'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_kaytlin'), duration=1.25, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        cam_trent_sit.set(group=MAIN, time_delay=t)
        t += 0.01
        RotateAxisEvent(root=self, group=MAIN, object_name=darcy.name, angle=-25, axis='Y_AXIS', duration=0,
            smooth=False, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=kaytlin.name, angle=-125, axis='Y_AXIS', duration=0,
            smooth=False, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=brighton.name, angle=10, axis='Y_AXIS', duration=0,
            smooth=False, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=20, axis='Y_AXIS', duration=0,
            smooth=False, time_delay=t)
        trent.facial(group=MAIN, index=440, auto_lip=True)

        # m08_offer 450: Kaitlyn.
        # И были достаточно умны, чтобы это признать. Непосредственное руководство миссией возложено на
        # адмирала Брайтона, все детали обсудите с ним...
        t = 0
        cam_kaytlin.set(group=MAIN, time_delay=t)
        t += 2
        kaytlin.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=100, time_scale=0.3,
            trans_time=1, time_delay=t)
        t += 6
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('brighton_head_ik'),
            target_name=self.get_automarker_name('head_kaytlin_front_fwd2'), duration=2.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('brighton_eye_ik'),
            target_name=self.get_automarker_name('head_kaytlin_lwr'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 3.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('kaytlin_ik_not_interested_head'),
            target_name=self.get_automarker_name('head_brighton_front_fwd'), duration=2, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('kaytlin_ik_not_interested_eye'),
            target_name=self.get_automarker_name('head_brighton_front_lwr'), duration=1.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        kaytlin.facial(group=MAIN, index=450, auto_lip=True)

        # m08_offer 460: Kaitlyn.
        # Джентльмены...
        t = 2.6
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('brighton_head_ik'),
            target_name=self.get_automarker_name('head_trent_brightonside_front'), duration=2, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('brighton_eye_ik'),
            target_name=self.get_automarker_name('head_trent_brightonside'), duration=1.25, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        kaytlin.facial(group=MAIN, index=460, auto_lip=True)

        # m08_offer 470: Brighton.
        # Мистер Трент, на орбите планеты находится Принц Уэльский, мой линкор. Стыкуйтесь к нему, все
        # необходимые допуски и разрешения я вам выдам.
        t = 0
        cam_brighton.set(group=MAIN, time_delay=t)
        brighton.facial(group=MAIN, index=470, auto_lip=True)

        # m08_offer 480: Darcy.
        # Трент, увидимся на Принце Уэльском.
        t = 0
        cam_darcy_sit.set(group=MAIN, time_delay=t)
        t += 3
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_STNDCR_TRNS_090LV_XA_04, duration=4, time_scale=0.5,
            trans_time=1, time_delay=t)
        t += 0.3
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('darcy_head_ik'),
            target_name=self.get_automarker_name('head_trent_side_darcyout'), duration=2.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('darcy_eye_ik'),
            target_name=self.get_automarker_name('head_trent_side_darcyout'), duration=1.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        darcy.facial(group=MAIN, index=480, auto_lip=True)

        main_group.append_time(1)
