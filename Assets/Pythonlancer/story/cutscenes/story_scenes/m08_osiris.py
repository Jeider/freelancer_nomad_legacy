"""m08_osiris: полная постановка из master; точки в m08_osiris.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character, ConnectHardpointEvent, EyeIkEvent, Female, LookAtCamera, MAIN, Male, MotionEvent, MoveEvent, NeckIkEvent, Prop, RotateAxisEvent,
)
from story.cutscenes.anim import (
    Female, Male,
)
from story import actors


class ChairProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'm8_osiris_chair'

class PropTomeProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'tome'

class CharCaptainActor(actors.Actor):
    NAME = 'captain'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm8_asf_captain'

class CharRiflemanActor(actors.Actor):
    NAME = 'rifleman'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm8_asf_rifleman'


class M08OsirisScene(Scene):
    DUMP_FILE = 'm08_osiris'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Персонажи, камеры, реквизит и звук.
        chair = ChairProp(root=self, name='chair', light_group=0, init_point='chair', rotate_from_quat=True,
            use_ambient=True)
        prop_tome = PropTomeProp(root=self, name='prop_tome', light_group=9, init_point='prop_tome',
            rotate_from_quat=True)
        trent = Character(root=self, actor=actors.Trent, name='Char_trent', light_group=0,
            init_point='Char_trent', rotate_from_quat=True, appearance='trent', actor_name='Player')
        king = Character(root=self, actor=actors.King, name='Char_king', light_group=0, init_point='Char_king',
            rotate_from_quat=True, use_ambient=True, appearance='king', actor_name='King')
        major = Character(root=self, actor=actors.MajorScrew, name='Char_major', light_group=0,
            init_point='Char_major', rotate_from_quat=True, use_ambient=True, appearance='major_screw',
            actor_name='Major_Screw')
        hatcher = Character(root=self, actor=actors.Hatcher, name='Char_hatcher', light_group=0,
            init_point='Char_hatcher', rotate_from_quat=True, use_ambient=True, appearance='hatcher',
            actor_name='Hatcher')
        captain = Character(root=self, actor=CharCaptainActor, name='Char_captain', light_group=0,
            init_point='Char_captain', rotate_from_quat=True, appearance='m8_asf_captain', actor_name='Gunner')
        rifleman = Character(root=self, actor=CharRiflemanActor, name='Char_rifleman', light_group=0,
            init_point='Char_rifleman', rotate_from_quat=True, appearance='m8_asf_rifleman', actor_name='Gunner2')
        cam_start = LookAtCamera(root=self, name='cam_start', fov=20, look_duration=70)
        cam_start_hatcher = LookAtCamera(root=self, name='cam_start_hatcher', fov=15, look_duration=70)
        cam_king_first = LookAtCamera(root=self, name='cam_king_first', fov=15, look_duration=70)
        cam_trent_sits_down = LookAtCamera(root=self, name='cam_trent_sits_down', fov=15, look_duration=70)
        cam_king_far = LookAtCamera(root=self, name='cam_king_far', fov=15, look_duration=70)
        cam_king_near = LookAtCamera(root=self, name='cam_king_near', fov=12, look_duration=120)
        cam_trent_near = LookAtCamera(root=self, name='cam_trent_near', fov=12, look_duration=120)
        cam_major_near = LookAtCamera(root=self, name='cam_major_near', fov=12, look_duration=120)
        cam_trent_artifact = LookAtCamera(root=self, name='cam_trent_artifact', fov=15, look_duration=120)
        cam_trent_decline = LookAtCamera(root=self, name='cam_trent_decline', fov=12, look_duration=200)
        cam_trent_reaction = LookAtCamera(root=self, name='cam_trent_reaction', fov=15, look_duration=200)
        cam_hatcher_sad = LookAtCamera(root=self, name='cam_hatcher_sad', fov=15, look_duration=200)

        # Исходные точки взгляда.

        # Вход.
        t = 0
        cam_start.set(group=MAIN, time_delay=t)
        cam_start.move_cam(group=MAIN, index=2, duration=7, smooth=True, time_delay=t)
        cam_start.move_focus(group=MAIN, index=2, duration=7, smooth=True, time_delay=t)
        major.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_HOLD_ARMS_CROSSED_000LV_XA_02, duration=1, time_delay=t)
        king.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_LEAN_ARMB_090LV_A_08, duration=0.1, start_time=2.5,
            time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=rifleman.name,
            anim=Male.Sc_MLBODY_STND_HOLD_RIFLE_MILI_000LV_XA_05, duration=100, loop=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=captain.name,
            anim=Female.Sc_FMBODY_WALK_HOLD_GUN_RHAND_000LV_XB_01, duration=7, time_scale=0.8, loop=True,
            time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=7, time_scale=0.8, loop=True,
            time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_WLKG_000LV_XA_01, duration=7, time_scale=0.8, loop=True,
            time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=hatcher.name, angle=6, axis='Y_AXIS', duration=6,
            smooth=False, time_delay=t)
        t += 0.01
        RotateAxisEvent(root=self, group=MAIN, object_name=king.name, angle=-140, axis='Y_AXIS', duration=0,
            smooth=False, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=rifleman.name, angle=30, axis='Y_AXIS', duration=0,
            smooth=False, time_delay=t)
        t += 0.19
        NeckIkEvent(root=self, group=MAIN, char_name=rifleman.name, target_name=captain.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=15, transition_duration=3,
            time_delay=t)
        t += 1.8
        NeckIkEvent(root=self, group=MAIN, char_name=king.name,
            target_name=self.get_automarker_name('king_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=500, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=king.name,
            target_name=self.get_automarker_name('king_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=500, transition_duration=1, time_delay=t)
        t += 1
        NeckIkEvent(root=self, group=MAIN, char_name=hatcher.name,
            target_name=self.get_automarker_name('hatcher_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=2555, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=hatcher.name,
            target_name=self.get_automarker_name('hatcher_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=2555, transition_duration=1, time_delay=t)
        t += 4
        cam_start_hatcher.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_WALK_STND_TRNS_000LV_XA_01, duration=15, time_scale=0.8,
            time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=hatcher.name, angle=-15, axis='Y_AXIS', duration=2,
            smooth=False, time_delay=t)
        main_group.append_time(8.5)

        # m08_osiris 10: Hatcher.
        # Майо... эээ... Простите, генерал Кинг, майор Скрю, Трент доставлен.
        t = 0.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_king'), duration=2.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_king'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 0.5
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_SALUT_000LV_XA_03, duration=10, start_time=0.5,
            trans_time=1, time_delay=t)
        t += 2
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_major'), duration=2.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_major'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        hatcher.facial(group=MAIN, index=10, auto_lip=True)

        # m08_osiris 20: King.
        # Спасибо, мисс Хетчер.
        t = 0
        cam_king_first.set(group=MAIN, time_delay=t)
        cam_king_first.move_cam(group=MAIN, index=2, duration=8, smooth=True, time_delay=t)
        cam_king_first.move_focus(group=MAIN, index=2, duration=8, smooth=True, time_delay=t)
        major.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_A_11, duration=50, time_scale=0.2,
            start_time=1, loop=True, time_delay=t)
        king.facial(group=MAIN, index=20, auto_lip=True)

        # m08_osiris 30: King.
        # Мистер Трент, я понимаю, что у вас выдались тяжелые... гхм... несколько дней...
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('king_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('king_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=captain.name,
            target_name=self.get_automarker_name('point_captain_aim'), duration=0, smooth=False, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 0.1
        MotionEvent(root=self, group=MAIN, object_name=captain.name, anim=Female.Sc_FMBODY_CHRB_LSTN_000LV_A_08,
            duration=200, time_scale=0.4, loop=True, time_delay=t)
        t += 0.1
        NeckIkEvent(root=self, group=MAIN, char_name=captain.name,
            target_name=self.get_automarker_name('head_trent'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=15, transition_duration=3, time_delay=t)
        t += 1.3
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('point_trent_stand_to_sit'), duration=0, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.01
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=50, axis='Y_AXIS', duration=0,
            smooth=False, time_delay=t)
        t += 0.99
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_SITCR_TRNS_090DN_XA_07, duration=15, start_time=1,
            time_delay=t)
        t += 2
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=20, axis='Y_AXIS', duration=1,
            smooth=False, time_delay=t)
        t += 1.5
        king.facial(group=MAIN, index=30, auto_lip=True)

        cam_trent_sits_down.set(group=MAIN, time_delay=0)
        # m08_osiris 40: Trent.
        # Недель...
        main_group.append_time(1)
        trent.facial(group=MAIN, index=40, auto_lip=True)

        main_group.append_time(0.5)

        MoveEvent(root=self, group=MAIN, object_name=king.name,
            target_name=self.get_automarker_name('point_king_talk_front'), duration=0, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=-0.3)
        king.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=0.1, time_delay=-0.2)
        RotateAxisEvent(root=self, group=MAIN, object_name=king.name, angle=-20, axis='Y_AXIS', duration=0,
            smooth=False, time_delay=-0.1)

        # m08_osiris 50: King.
        # Пусть даже месяцев, но есть некоторые вещи, которые выше нашего морального и физического состояния.
        # И в данный момент очень важно определить местонахождение известного вам тома Протеуса и ключа.
        t = 0
        cam_king_far.set(group=MAIN, time_delay=0)
        cam_king_far.move_cam(group=MAIN, index=2, duration=26, smooth=True, time_delay=0)
        king.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=5,
            time_scale=0.4, trans_time=1, time_delay=t)
        t += 10
        king.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=5, time_scale=0.4,
            trans_time=1, time_delay=t)
        king.facial(group=MAIN, index=50, auto_lip=True)

        # m08_osiris 60: King.
        # А поэтому, расскажите, пожалуйста, подробно всё, что происходило с вами с момента когда мисс Хетчер
        # приказала вам вместе с отрядом Дельта отправиться в Сигму-17.
        t = 1
        king.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, duration=5, time_scale=0.4,
            trans_time=2, time_delay=t)
        t += 10
        king.facial(group=MAIN, index=60, auto_lip=True)

        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=555, transition_duration=1, time_delay=0)
        # m08_osiris 70: Trent.
        # Нас перехватили в Большом Омикроне, до сигмы-17 мы так и не добрались.
        t = 0
        cam_trent_sits_down.set(group=MAIN, time_delay=0)
        trent.facial(group=MAIN, index=70, auto_lip=True)

        # m08_osiris 80: King.
        # Кто перехватил?
        t = 0
        cam_king_near.set(group=MAIN, time_delay=0)
        t += 1.2
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('point_trent_sit'), duration=0, smooth=False, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 0.1
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=100, time_scale=0.6,
            loop=True, time_delay=t)
        king.facial(group=MAIN, index=80, auto_lip=True)

        # m08_osiris 90: Trent.
        # Да хрен его знает, какие-то бравые ребята с линкора под названием "Навухудоноссор". А потом нам
        # помог с него сбежать капитан Сид.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=0)
        t += 1.5
        major.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_HOLD_ARMS_CROSSED_000LV_XA_02, duration=1, trans_time=1,
            time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=major.name,
            target_name=self.get_automarker_name('major_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=555, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=major.name,
            target_name=self.get_automarker_name('major_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=555, transition_duration=1, time_delay=t)
        trent.facial(group=MAIN, index=90, auto_lip=True)

        # m08_osiris 100: King.
        # Капитан Сид...
        t = 0
        cam_king_far.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('king_head_ik'),
            target_name=self.get_automarker_name('head_major_front_far'), duration=2, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('king_eye_ik'),
            target_name=self.get_automarker_name('head_major_front_near'), duration=1.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        king.facial(group=MAIN, index=100, auto_lip=True)
        t = 0
        cam_major_near.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('major_head_ik'),
            target_name=self.get_automarker_name('head_king_front_far'), duration=2.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=-1)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('major_eye_ik'),
            target_name=self.get_automarker_name('head_king_front_near'), duration=1.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=-1)

        # m08_osiris 110: MajorScrew.
        # Капитан Сид...
        major.facial(group=MAIN, index=110, auto_lip=True)

        # m08_osiris 120: Trent.
        # Потом со мной вышел на контакт агент Рокфорд. Или это я с ним на контакт вышел...
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('king_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('king_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        trent.facial(group=MAIN, index=120, auto_lip=True)

        # m08_osiris 130: King.
        # Рокфорд?
        t = 0
        cam_king_near.set(group=MAIN, time_delay=t)
        king.facial(group=MAIN, index=130, auto_lip=True)

        # m08_osiris 140: Trent.
        # Рокфорд. И он помог мне вернуть артефакты. Но позже оказалось, что вернуть он их хотел себе, а меня
        # попытался уничтожить. (прикол жеж, удалось почти) И это ему почти удалось.
        t = 0
        cam_trent_artifact.set(group=MAIN, time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_major_right'), duration=2.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_major_right'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 3
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_leaders_middle'), duration=2.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_leaders_middle'), duration=1.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        trent.facial(group=MAIN, index=140, auto_lip=True)

        # m08_osiris 145: Trent.
        # В итоге, в последний момент я ускользнул от него и спас вот это:
        t = 1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_major_right'), duration=2.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_major_right'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 0.5
        cam_trent_artifact.move_focus(group=MAIN, index=2, duration=5, smooth=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_GESTR_RGHT_000LV_XA_03, duration=4, time_scale=0.15,
            trans_time=0.5, time_delay=t)
        ConnectHardpointEvent(root=self, group=MAIN, target_name=prop_tome.name, parent_name=trent.name,
            duration=20, target_hardpoint='rhand_connect_tome', parent_hardpoint='hprightconnect', time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_HOLDD_RGHT_000LV_00, duration=1, time_scale=5,
            time_delay=t)
        t += 2.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_leaders_middle_bottom'), duration=3, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_leaders_middle_bottom'), duration=1.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        trent.facial(group=MAIN, index=145, auto_lip=True)
        main_group.append_time(1)

        # m08_osiris 150: King.
        # Значит Рокфорд в курсе
        t = 0
        cam_king_near.set(group=MAIN, time_delay=t)
        t += 2.3
        king.facial(group=MAIN, index=150, auto_lip=True)

        cam_major_near.set(group=MAIN, time_delay=0)

        # m08_osiris 160: MajorScrew.
        # И в игре...
        major.facial(group=MAIN, index=160, auto_lip=True)

        # m08_osiris 170: King.
        # И в игре... пока... (серьёзно) Нужно это исправить.
        t = 0
        cam_king_near.set(group=MAIN, time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('king_head_ik'),
            target_name=self.get_automarker_name('head_major_front_far'), duration=2, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('king_eye_ik'),
            target_name=self.get_automarker_name('head_major_front_near'), duration=1.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        king.facial(group=MAIN, index=170, auto_lip=True)

        # m08_osiris 180: MajorScrew.
        # В данный момент он скорее всего где-то в штате Нового Ордена. Нам нужен агент в Новом Ордене. Агент,
        # который вычислит его местонахождение.
        t = 0
        cam_major_near.set(group=MAIN, time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('major_head_ik'),
            target_name=self.get_automarker_name('head_hatcher'), duration=2.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('major_eye_ik'),
            target_name=self.get_automarker_name('head_hatcher'), duration=1.8, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 4
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('major_head_ik'),
            target_name=self.get_automarker_name('head_king_front_far'), duration=2.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('major_eye_ik'),
            target_name=self.get_automarker_name('head_king_front_near'), duration=1.8, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        major.facial(group=MAIN, index=180, auto_lip=True)

        # m08_osiris 190: King.
        # И вы нам его обеспечите?
        t = 0
        cam_king_near.set(group=MAIN, time_delay=t)
        king.facial(group=MAIN, index=190, auto_lip=True)

        # m08_osiris 200: MajorScrew.
        # Нет, не обеспечу. Моих агентов в Ордене осталось считанные единицы, их там отстреливают как
        # куропаток.
        t = 0
        cam_major_near.set(group=MAIN, time_delay=t)
        t += 4.8
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('major_head_ik'),
            target_name=self.get_automarker_name('head_hatcher'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('major_eye_ik'),
            target_name=self.get_automarker_name('head_hatcher'), duration=1.8, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        major.facial(group=MAIN, index=200, auto_lip=True)

        # m08_osiris 210: King.
        # А может быть нам в этом поможет… (взгляд) мистер Трент?
        t = 0
        cam_king_far.set(group=MAIN, time_delay=t)
        t += 1.9
        MoveEvent(root=self, group=MAIN, object_name=prop_tome.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 1.1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('king_head_ik'),
            target_name=self.get_automarker_name('head_trent_upper'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('king_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 0.9
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_king'), duration=2.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_king'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_dx_s069x_1701_Jacobi, duration=0.1, trans_time=0, time_delay=t)
        king.facial(group=MAIN, index=210, auto_lip=True)

        # m08_osiris 220: Hatcher.
        # Трент просрал два артефакта и звено прикрытия, и что же мы ему предложим? Стать нашим агентом в
        # Ордене... Генерал Кинг, вы в своем уме???
        t = 0
        cam_start_hatcher.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_CONV_HNDS_EMPH_000LV_XB_03, duration=5,
            time_scale=0.8, trans_time=1, loop=True, time_delay=t)
        t += 4
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_EMPH_HNDSDN_TRNS_000LV_XA_01, duration=100,
            time_scale=0.8, trans_time=1, time_delay=t)
        t += 3
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=100,
            time_scale=0.5, trans_time=1, time_delay=t)

        hatcher.motion(group=MAIN, anim="Sc_dx_s069x_1701_Jacobi",
             duration=0.1, start_time=0, time_scale=1, trans_time=0, time_delay=-1)
        hatcher.motion(group=MAIN, anim="Sc_dx_s069x_0901_Jacobi",
             duration=5, start_time=2, time_scale=0.9, trans_time=0.25, time_delay=0)
        hatcher.motion(group=MAIN, anim="Sc_dx_s069x_1701_Jacobi",
             duration=5, start_time=0, time_scale=0.8, trans_time=0.25, time_delay=1)
        hatcher.motion(group=MAIN, anim="Sc_dx_s070x_0801_Jacobi",
             duration=5, start_time=0, time_scale=1, trans_time=0.25, time_delay=4)
        hatcher.motion(group=MAIN, anim="Sc_dx_s069x_2201_Jacobi",
             duration=5, start_time=0, time_scale=1, trans_time=0.25, time_delay=2.6)


        hatcher.facial(group=MAIN, index=220, auto_lip=True, no_anim=True)

        # m08_osiris 230: MajorScrew.
        # Не говоря уже о том, что скорее всего он и есть агент Ордена.
        t = 0
        cam_major_near.set(group=MAIN, time_delay=t)
        t += 1.2
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('major_head_ik'),
            target_name=self.get_automarker_name('head_king_front_far'), duration=2.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('major_eye_ik'),
            target_name=self.get_automarker_name('head_king_front_near'), duration=1.8, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('king_head_ik'),
            target_name=self.get_automarker_name('head_major_front_far'), duration=2, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('king_eye_ik'),
            target_name=self.get_automarker_name('head_major_front_near'), duration=1.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        major.facial(group=MAIN, index=230, auto_lip=True)

        # m08_osiris 240: King.
        # А я верю в этого паренька. Трент, давай так, ты помогаешь нам, а мы чистим всю твою биографию перед
        # СБА и платим тройной тариф.
        t = 0
        cam_king_far.set(group=MAIN, time_delay=t)
        t += 1.2
        major.motion(group=MAIN, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=4.444, time_scale=0.9,
            trans_time=0.5, time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('king_head_ik'),
            target_name=self.get_automarker_name('head_trent_upper'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('king_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 7.5
        king.facial(group=MAIN, index=240, auto_lip=True)

        # m08_osiris 250: Trent.
        # Знаете что, идите нахер, генерал Кинг. Последнее время я только и занимаюсь тем, что стараюсь
        # улучшить репутацию и получить большие деньги.
        t = 0

        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=100, time_scale=0.6,
            loop=True, time_delay=-1)
        cam_trent_decline.set(group=MAIN, time_delay=t)
        t += 3
        cam_trent_decline.move_cam(group=MAIN, index=2, duration=13, smooth=True, time_delay=t)
        cam_trent_decline.move_focus(group=MAIN, index=2, duration=13, smooth=True, time_delay=t)
        trent.facial(group=MAIN, index=250, auto_lip=True)

        # m08_osiris 260: Trent.
        # А все заканчивается тем, что на меня начинают охоту и обвиняют во все более тяжких преступлениях.
        trent.facial(group=MAIN, index=260, auto_lip=True)

        # m08_osiris 270: MajorScrew.
        # Генерал Кинг, а вы не напомните, как звали того агента, которого мы внедрили в Орден до Трента?
        t = 0
        cam_major_near.set(group=MAIN, time_delay=t)
        major.facial(group=MAIN, index=270, auto_lip=True)

        # m08_osiris 280: King.
        # Какая разница? Связь с ним утеряна, он, скорее всего погиб.
        t = 0
        cam_king_near.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('king_head_ik'),
            target_name=self.get_automarker_name('head_major_front_far'), duration=2, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('king_eye_ik'),
            target_name=self.get_automarker_name('head_major_front_near'), duration=1.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        king.facial(group=MAIN, index=280, auto_lip=True)

        # m08_osiris 290: MajorScrew.
        # Тем не менее, генерал.
        t = 0
        cam_major_near.set(group=MAIN, time_delay=t)
        major.facial(group=MAIN, index=290, auto_lip=True)

        # m08_osiris 300: King.
        # Аларик. По-моему, Аларик.
        t = 0
        cam_king_near.set(group=MAIN, time_delay=t)
        t += 2.5
        king.facial(group=MAIN, index=300, auto_lip=True)

        t = -1

        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('point_trent_sit_forward'), duration=0, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=rifleman.name,
            target_name=self.get_automarker_name('point_rifleman_near_trent'), duration=0, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.005
        RotateAxisEvent(root=self, group=MAIN, object_name=rifleman.name, angle=-25, axis='Y_AXIS', duration=0,
            smooth=False, time_delay=t)

        # m08_osiris 310: Trent.
        # Сволочи! Что с Алариком, гады?
        t = 0
        cam_trent_reaction.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_SPCBODY_s051x_Trent_XC_CHRF_RLLV_29, duration=6, start_time=24.8,
            time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=rifleman.name,
            anim=Male.Sc_SPCBODY_s051x_ku_guard01_XB_STND_000LV_05, duration=6, time_delay=t)
        trent.facial(group=MAIN, index=310, auto_lip=True)

        # m08_osiris 320: MajorScrew.
        # Мы не знаем. Связь с ним прервалась где-то на территории Кусари.
        t = 0
        cam_major_near.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('major_head_ik'),
            target_name=self.get_automarker_name('head_trent_upper'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('major_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 4
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05, duration=100, loop=True,
            time_delay=t)
        major.facial(group=MAIN, index=320, auto_lip=True)

        # m08_osiris 330: Hatcher.
        # (виноватая): У него почти получилось. Он должен был передать нам базу данных, но не вышел на связь.
        # Мы не знаем, кто наложил лапу на Аларика и его информацию.
        t = 0
        cam_hatcher_sad.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_trent_upper_forward'), duration=2.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        hatcher.facial(group=MAIN, index=330, auto_lip=True)

        # m08_osiris 340: King.
        # (мотивирующе): Ты можешь помочь и нам и своему другу. Найди его, заверши передачу информации,
        # которую должен был завершить твой друг - и ты свободен.
        t = 0
        cam_king_near.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('king_head_ik'),
            target_name=self.get_automarker_name('head_trent_upper'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('king_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        king.facial(group=MAIN, index=340, auto_lip=True)

        # m08_osiris 345: King.
        # И не вздумай хитрить, дружище, не вздумай
        t = 3
        MoveEvent(root=self, group=MAIN, object_name=rifleman.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('point_trent_sit'), duration=0, smooth=False, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 0.1
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=100, time_scale=0.6,
            loop=True, time_delay=t)
        king.facial(group=MAIN, index=345, auto_lip=True)

        # m08_osiris 350: Trent.
        # Ладно... ваша взяла...
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=350, auto_lip=True)

        # m08_osiris 360: King.
        # Мисс Хетчер, поднимите все данные по агенту Аларику и передайте их в распоряжение мистеру Тренту.
        t = 0
        cam_king_far.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('king_head_ik'),
            target_name=self.get_automarker_name('head_hatcher_right'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('king_eye_ik'),
            target_name=self.get_automarker_name('head_hatcher_right_far'), duration=1.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        king.facial(group=MAIN, index=360, auto_lip=True)

        # m08_osiris 370: King.
        # Далее, вашим заданием будет сопровождение тома Протея вместе с Трентом и мисс Дерси на
        # исследовательскую базу.
        t = 2.1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_king'), duration=2.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_eye_ik'),
            target_name=self.get_automarker_name('head_king'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        king.facial(group=MAIN, index=370, auto_lip=True)

        # m08_osiris 380: Hatcher.
        # Принято!
        t = 0
        cam_start_hatcher.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_STND_SALUT_000LV_XA_03, duration=10, start_time=1.5,
            time_delay=t)
        hatcher.facial(group=MAIN, index=380, auto_lip=True)
        # Действие после исходного окна реплики.
        t = 10921.5
        EyeIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=55, transition_duration=1, time_delay=t)

        main_group.append_time(1)