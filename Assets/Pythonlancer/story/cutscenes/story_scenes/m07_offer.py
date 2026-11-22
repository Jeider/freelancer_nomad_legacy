"""m07_offer: полная постановка из master; точки в m07_offer.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character, ConnectHardpointEvent, EyeIkEvent, LookAtCamera, MAIN, Male, MotionEvent, MoveEvent, NeckIkEvent, Prop, RotateAxisEvent,
)
from story.cutscenes.anim import (
    Male,
)
from story import actors


class PropCigarette2Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'cigarette_2'

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

class CharTrentBaseActor(actors.Actor):
    NAME = 'trent_base'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'trent'


class M07OfferScene(Scene):
    DUMP_FILE = 'm07_offer'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)
        from story.scripts.main.mission6 import Msn6Freeport
        m06_freeport_props = Msn6Freeport(self.props.mission)

        # Персонажи, камеры, реквизит и звук.
        bartender_fixture = Character(root=self, actor=actors.BartenderFixture, name='Char_bartender_Fixture',
            light_group=0, init_point='Char_bartender_Fixture', rotate_from_quat=True,
            appearance='li_bartender_1', actor_name='bartender', floor_height=-110.0)
        prop_cigarette_2 = PropCigarette2Prop(root=self, name='prop_cigarette_2', light_group=0,
            init_point='prop_cigarette_2', rotate_from_quat=True, use_ambient=True)
        delta = Character(root=self, actor=actors.DeltaOne, name='Char_delta', light_group=0,
            init_point='Char_delta', rotate_from_quat=True, appearance='m06_asf_prisoner01b',
            actor_name='Prisoner1b')
        prisoner2b = Character(root=self, actor=CharPrisoner2bActor, name='Char_prisoner2b', light_group=0,
            init_point='Char_prisoner2b', rotate_from_quat=True, appearance='m06_asf_prisoner02b',
            actor_name='Prisoner2b')
        prisoner3b = Character(root=self, actor=CharPrisoner3bActor, name='Char_prisoner3b', light_group=0,
            init_point='Char_prisoner3b', rotate_from_quat=True, appearance='m06_asf_prisoner03b',
            actor_name='Prisoner3b')
        prisoner4b = Character(root=self, actor=CharPrisoner4bActor, name='Char_prisoner4b', light_group=0,
            init_point='Char_prisoner4b', rotate_from_quat=True, appearance='m06_asf_prisoner04b',
            actor_name='Prisoner4b')
        trent_base = Character(root=self, actor=CharTrentBaseActor, name='Char_trent_base', light_group=0,
            init_point='Char_trent_base', rotate_from_quat=True, appearance='trent', actor_name='Player',
            floor_height=-1000)
        trent = Character(root=self, actor=actors.Trent, name='Char_trent', light_group=0,
            init_point='Char_trent', rotate_from_quat=True, appearance='trent_original',
            actor_name='TrentOriginal')
        barman = Character(root=self, actor=actors.CorsairBarman, name='Char_barman', light_group=0,
            init_point='Char_barman', rotate_from_quat=True, appearance='m07_bartender',
            actor_name='m6_bartender', floor_height=-110.0)
        cam_start = LookAtCamera(root=self, name='cam_start', fov=20, look_duration=70)
        cam_delta_sit_trent_sit_down = LookAtCamera(root=self, name='cam_delta_sit_trent_sit_down', fov=16,
            look_duration=70)
        cam_delta_sit = LookAtCamera(root=self, name='cam_delta_sit', fov=15, look_duration=70)
        cam_trent_sit = LookAtCamera(root=self, name='cam_trent_sit', fov=15, look_duration=70)
        cam_delta_explaining = LookAtCamera(root=self, name='cam_delta_explaining', fov=15, look_duration=70)
        cam_delta_warning = LookAtCamera(root=self, name='cam_delta_warning', fov=15, look_duration=100)
        cam_trent_standup = LookAtCamera(root=self, name='cam_trent_standup', fov=15, look_duration=150)
        cam_barman = LookAtCamera(root=self, name='cam_barman', fov=15, look_duration=150)
        cam_second_start = LookAtCamera(root=self, name='cam_second_start', fov=15, look_duration=150)
        cam_trent_deal = LookAtCamera(root=self, name='cam_trent_deal', fov=15, look_duration=70)

        # Исходные точки взгляда.

        # Вход.
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=bartender_fixture.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=trent_base.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        delta.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=4, loop=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=prisoner2b.name, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05,
            duration=25, loop=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=prisoner3b.name, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05,
            duration=25, loop=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=prisoner4b.name, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05,
            duration=25, loop=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=10, loop=True, time_delay=t)
        cam_start.set(group=MAIN, time_delay=t)
        cam_start.move_cam(group=MAIN, index=2, duration=7, smooth=True, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name, target_name=delta.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=25, transition_duration=3,
            time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=delta.name, target_name=trent.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=25, transition_duration=2,
            time_delay=t)
        t += 0.01
        MotionEvent(root=self, group=MAIN, object_name=trent_base.name, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04,
            duration=1, time_scale=0.8, trans_time=1, time_delay=t)
        t += 1.99
        MotionEvent(root=self, group=MAIN, object_name=prisoner3b.name,
            anim=Male.Sc_MLBODY_CHRB_TWSTU_CCL_LESS_000LV_A_14, duration=21, start_time=7, trans_time=1,
            time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=28, axis='Y_AXIS', duration=4,
            smooth=True, time_delay=t)
        cam_start.move_focus(group=MAIN, index=2, duration=5, smooth=True, time_delay=t)
        t += 2
        MotionEvent(root=self, group=MAIN, object_name=prisoner2b.name,
            anim=Male.Sc_MLBODY_CHRF_TWSTS_LOOK_090LV_XA_02, duration=21, time_scale=0.6, trans_time=1,
            time_delay=t)
        delta.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=15, time_scale=0.6,
            trans_time=1, time_delay=t)
        t += 1
        NeckIkEvent(root=self, group=MAIN, char_name=prisoner4b.name, target_name=trent.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=5, transition_duration=3,
            time_delay=t)
        main_group.append_time(10)

        # m06_freeport 10: DeltaOne.
        # Мистер Трент, Хочу вас поблагодарить за проделанную работу. Прошу извинить нас за то, что попали в
        # неприятности по нашей вине, и я обещаю, что сделаю все возможное, чтобы восстановить вашу репутацию.
        t = 0
        MotionEvent(root=self, group=MAIN, object_name=prisoner2b.name,
            anim=Male.Sc_MLBODY_CHRF_TWSTS_FROM_090LV_XA_02, duration=21, time_scale=0.6, trans_time=1,
            time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('point_trent_sit_down'), duration=0, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        cam_delta_sit_trent_sit_down.set(group=MAIN, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=prisoner4b.name,
            anim=Male.Sc_MLBODY_CHRF_TAP_RHND_000LV_A_02, duration=17, time_scale=0.3, trans_time=1, loop=True,
            time_delay=t)
        t += 0.01
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_SITCR_TRNS_180DN_XA_06, duration=15, time_delay=t)
        t += 0.99
        cam_delta_sit_trent_sit_down.move_cam(group=MAIN, index=2, duration=13, smooth=True, time_delay=t)
        cam_delta_sit_trent_sit_down.move_focus(group=MAIN, index=2, duration=13, smooth=True, time_delay=t)
        t += 4
        delta.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=15, time_scale=0.5,
            trans_time=1, time_delay=t)
        t += 7.9
        delta.motion(group=MAIN, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=4.444, time_scale=0.9,
            trans_time=1, time_delay=t)
        delta.facial(group=MAIN, index=10, auto_lip=True, extra_delay=0, props=m06_freeport_props)
        main_group.append_time(0.2)

        # m06_freeport 20: Trent.
        # Это все хорошо, конечно, но что мне, собственно, делать сейчас?
        t = 0
        cam_trent_sit.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=20, auto_lip=True, extra_delay=0, props=m06_freeport_props)

        # m06_freeport 30: DeltaOne.
        # Ведите себя тихо, принимайте контракты на этом фрипорте, в других независимых или пиратских
        # системах, но ни в коем случае не возвращайтесь в легальные системы.
        t = 0
        cam_delta_explaining.set(group=MAIN, time_delay=t)
        cam_delta_explaining.move_cam(group=MAIN, index=2, duration=20, smooth=True, time_delay=t)
        delta.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_TALK_HNSTBL_000LV_A_34, duration=20, time_scale=0.8,
            trans_time=1, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_MED_000LV_XA_07, duration=62, time_scale=0.6,
            loop=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=prisoner4b.name,
            anim=Male.Sc_MLBODY_CHRF_IDLE_BIG_000LV_XA_06, duration=10, time_scale=0.6, start_time=2, loop=True,
            time_delay=t)
        ConnectHardpointEvent(root=self, group=MAIN, target_name=prop_cigarette_2.name,
            parent_name=prisoner4b.name, duration=50, target_hardpoint='hprightconnect_cigarette',
            parent_hardpoint='hprightconnect', time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=delta.name, target_name=trent.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=72, transition_duration=2,
            time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=delta.name, target_name=trent.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=72, transition_duration=4,
            time_delay=t)
        t += 10
        delta.motion(group=MAIN, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=1, time_scale=0.9,
            trans_time=0.5, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=prisoner4b.name,
            anim=Male.Sc_MLBODY_CHRF_TAP_RHND_000LV_A_02, duration=5, time_scale=0.4, trans_time=1, loop=True,
            time_delay=t)
        delta.facial(group=MAIN, index=30, auto_lip=True, extra_delay=0, props=m06_freeport_props)

        # m06_freeport 40: DeltaOne.
        # Если вас там задержат, мы будем бессильны что-то с этим сделать. А вас превратят в козла отпущения.
        t = 4
        MotionEvent(root=self, group=MAIN, object_name=prisoner4b.name,
            anim=Male.Sc_MLBODY_CHRF_GRABR_CHIN_RLEASE_000LV_XA_02, duration=5, time_scale=0.5, trans_time=1,
            time_delay=t)
        t += 3
        delta.motion(group=MAIN, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=1, time_scale=0.9,
            trans_time=0.5, time_delay=t)
        delta.facial(group=MAIN, index=40, auto_lip=True, extra_delay=0, props=m06_freeport_props)

        # m06_freeport 50: DeltaOne.
        # А сейчас мне нужно выйти на связь со штабом СБА, обсудить создавшуюся ситуацию и выработать
        # дальнейший план действий.
        t = 0
        MotionEvent(root=self, group=MAIN, object_name=prisoner4b.name,
            anim=Male.Sc_MLBODY_CHRF_CHIN_HOLDR_000LV_XA_03, duration=5, time_scale=0.5, trans_time=0.5,
            loop=True, time_delay=t)
        t += 1
        delta.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, duration=15, trans_time=3, loop=True,
            time_delay=t)
        t += 4
        MotionEvent(root=self, group=MAIN, object_name=prisoner4b.name,
            anim=Male.Sc_MLBODY_CHRF_HOLD_CHIN_RLEASE_000LV_XA_03, duration=5, time_scale=0.5, trans_time=0.5,
            time_delay=t)
        t += 1
        cam_delta_explaining.move_cam(group=MAIN, index=3, duration=15, smooth=True, time_delay=t)
        t += 1
        delta.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDUP_TRNS_000LV_XA_02, duration=2,
            time_scale=0.75, trans_time=0.25, time_delay=t)
        delta.facial(group=MAIN, index=50, auto_lip=True, extra_delay=0, props=m06_freeport_props)

        # m06_freeport 60: DeltaOne.
        # В благодарность за вашу работу я перевожу вам со своего счета пять тысяч кредитов. Кроме того,
        # вознаграждение за предыдущую миссию остается за вами, и как только мы разрешим эту ситуацию, вы его
        # получите.
        t = 1
        delta.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CONV_RHND_CASL_000LV_XA_04, duration=3.7,
            time_scale=0.75, trans_time=0.25, loop=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=prisoner4b.name,
            anim=Male.Sc_MLBODY_CHRF_TAP_RHND_000LV_A_02, duration=5, time_scale=0.4, trans_time=1, loop=True,
            time_delay=t)
        t += 3
        delta.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDDN_TRNS_000LV_XA_02, duration=3,
            time_scale=0.5, trans_time=1, time_delay=t)
        t += 2
        MotionEvent(root=self, group=MAIN, object_name=prisoner4b.name,
            anim=Male.Sc_MLBODY_CHRF_GRABR_CHIN_RLEASE_000LV_XA_02, duration=5, time_scale=0.5, trans_time=1,
            time_delay=t)
        t += 2.5
        delta.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=15, time_scale=0.4,
            trans_time=1, time_delay=t)
        t += 1.5
        MotionEvent(root=self, group=MAIN, object_name=prisoner4b.name,
            anim=Male.Sc_MLBODY_CHRF_CHIN_HOLDR_000LV_XA_03, duration=5, time_scale=0.5, trans_time=0.5,
            loop=True, time_delay=t)
        t += 4
        MotionEvent(root=self, group=MAIN, object_name=prisoner4b.name,
            anim=Male.Sc_MLBODY_CHRF_HOLD_CHIN_RLEASE_000LV_XA_03, duration=5, time_scale=0.5, trans_time=0.5,
            time_delay=t)
        delta.facial(group=MAIN, index=60, auto_lip=True, extra_delay=0, props=m06_freeport_props)

        # m06_freeport 70: Trent.
        # А как же компенсация за моральный ущерб?
        t = 0
        cam_trent_sit.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=70, auto_lip=True, extra_delay=0, props=m06_freeport_props)

        # m06_freeport 90: DeltaOne.
        # Мистер Трент, вы никогда не производили впечатление жадного человека. Вы достаточно долго и успешно
        # действуете в непростых ситуациях.
        t = 0
        cam_delta_warning.set(group=MAIN, time_delay=t)
        delta.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, duration=15, loop=True, time_delay=t)
        t += 1
        delta.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDUP_TRNS_000LV_XA_02, duration=2,
            time_scale=0.75, trans_time=0.25, time_delay=t)
        t += 2
        delta.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CONV_RHND_CASL_000LV_XA_04, duration=3.7,
            time_scale=0.75, trans_time=0.25, loop=True, time_delay=t)
        t += 3
        delta.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDDN_TRNS_000LV_XA_02, duration=3,
            time_scale=0.5, trans_time=1, time_delay=t)
        t += 4
        cam_delta_warning.move_cam(group=MAIN, index=2, duration=5, smooth=True, time_delay=t)
        delta.facial(group=MAIN, index=90, auto_lip=True, extra_delay=0, props=m06_freeport_props)

        # m06_freeport 100: DeltaOne.
        # А вот жадные люди, я слышал, долго не живут... Как только появятся новости, я свяжусь с вами, мистер
        # Трент.
        t = 0.5
        delta.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=15, time_scale=0.5,
            trans_time=1, time_delay=t)
        t += 3
        barman.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_BART_000LV_XA_10, duration=12, time_scale=0.8,
            start_time=1, loop=True, time_delay=t)
        t += 1
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_WALK_TRNS_090LV_XA_10, duration=15, trans_time=1,
            time_delay=t)
        t += 1
        cam_trent_standup.move_cam(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        cam_trent_standup.move_focus(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        t += 2
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=-97, axis='Y_AXIS', duration=5,
            smooth=True, time_delay=t)
        t += 1
        cam_trent_standup.set(group=MAIN, time_delay=t)
        t += 1.15
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=5.2, loop=True, time_delay=t)
        delta.facial(group=MAIN, index=100, auto_lip=True, extra_delay=0, props=m06_freeport_props)
        # Действие после исходного окна реплики.
        t = 2.5
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('head_barman_near'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=100, transition_duration=1, time_delay=t)
        t += 1.35
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=4, time_delay=t)
        main_group.append_time(4.5)

        # m07_offer 10: CorsairBarman.
        # Чего налить?
        t = 0
        MotionEvent(root=self, group=MAIN, object_name=prisoner2b.name,
            anim=Male.Sc_MLBODY_CHRB_WALK_TRNS_090LV_XA_10, duration=15, time_scale=0.7, trans_time=1,
            time_delay=t)
        cam_second_start.set(group=MAIN, time_delay=t)
        cam_second_start.move_cam(group=MAIN, index=2, duration=5, smooth=True, time_delay=t)
        cam_second_start.move_focus(group=MAIN, index=2, duration=5, smooth=True, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=barman.name, target_name=trent.name, target_type='PART',
            target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS', duration=55, transition_duration=2,
            time_delay=t)
        barman.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=100, time_scale=0.8,
            trans_time=1, loop=True, time_delay=t)
        barman.facial(group=MAIN, index=10, auto_lip=True, extra_delay=0)

        # m07_offer 20: Trent.
        # Дельца какого-нибудь, желательно с хорошей оплатой.
        t = 0.5
        MotionEvent(root=self, group=MAIN, object_name=prisoner3b.name,
            anim=Male.Sc_MLBODY_CHRB_WALK_TRNS_270LV_XA_10, duration=15, time_scale=0.7, trans_time=1,
            time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=15,
            time_scale=0.6, trans_time=1, time_delay=t)
        trent.facial(group=MAIN, index=20, auto_lip=True, extra_delay=0)

        # m07_offer 30: CorsairBarman.
        # Да у нас тут вроде и в своих фрилансерах недостатка нет, понимаете же в какой системе находитесь.
        t = 0
        cam_barman.set(group=MAIN, time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, object_name=prisoner2b.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=prisoner3b.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=prisoner4b.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 2
        MoveEvent(root=self, group=MAIN, object_name=delta.name,
            target_name=self.get_automarker_name('point_delta_walkout'), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        barman.facial(group=MAIN, index=30, auto_lip=True, extra_delay=0)

        # m07_offer 40: Trent.
        # А я… скидку хорошую сделаю! Выручай дружище, я совсем на мели.
        t = 0
        delta.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=55, loop=True, time_delay=t)
        cam_trent_deal.set(group=MAIN, time_delay=t)
        t += 1.5
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=15, time_scale=0.6,
            trans_time=1, time_delay=t)
        trent.facial(group=MAIN, index=40, auto_lip=True, extra_delay=0)

        # m07_offer 50: CorsairBarman.
        # Окей, мистер...
        t = 0
        cam_second_start.set(group=MAIN, time_delay=t)
        barman.facial(group=MAIN, index=50, auto_lip=True, extra_delay=0)

        # m07_offer 60: Trent.
        trent.facial(group=MAIN, index=60, auto_lip=True, extra_delay=0)

        # m07_offer 70: CorsairBarman.
        # Трент.
        t = 0
        cam_barman.set(group=MAIN, time_delay=t)
        barman.facial(group=MAIN, index=70, auto_lip=True, extra_delay=0)

        # m07_offer 80: CorsairBarman.
        # Окей, мистер Трент. Будет для вас дельце.
        barman.facial(group=MAIN, index=80, auto_lip=True, extra_delay=0)

        # m07_offer 90: CorsairBarman.
        # К нам тут гастролеры пожаловали из Либерти. Называют себя бандой Старлайна.
        barman.facial(group=MAIN, index=90, auto_lip=True, extra_delay=0)

        # m07_offer 100: CorsairBarman.
        # Найдите их и убейте Билла Айронсайда - их лидера. Координаты их предположительного местонахождения я
        # вам скину.
        barman.facial(group=MAIN, index=100, auto_lip=True, extra_delay=0)
