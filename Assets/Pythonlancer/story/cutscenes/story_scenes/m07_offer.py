"""m07_offer: постановка для ручного редактирования.

Точки: SCENES/m07_offer.blend → DUMPS/m07_offer.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — смещение внутри текущего блока; facial()/append_time() двигают часы.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
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
)
from story.cutscenes.anim import (
    Male,
)
from story.cutscenes.source_extensions import (
    preserve_entity,
    restore_dialogue,
    select_dialogue,
)
from story import actors


class ExtraCharBartenderFixture(actors.Actor):
    NAME = 'bartender_fixture'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'li_bartender_1'
    GAME_ACTOR = 'bartender'


class PropPropCigarette2(Prop):
    COMPOUND_TEMPLATE_NAME = 'cigarette_2'
    SRT_GRP = 0
    USR_FLG = 0


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


class ExtraCharTrentBase(actors.Actor):
    NAME = 'trent_base'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'trent'
    GAME_ACTOR = 'Player'



class M07OfferScene(Scene):
    DUMP_FILE = 'm07_offer'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        # Исправлена опечатка исходного THN: floor_height==-110 → числовое -110.
        bartender_fixture = Character(root=self, actor=ExtraCharBartenderFixture, light_group=0,
            init_point='Char_bartender_fixture', rotate_from_quat=True, use_ambient=False, floor_height=-110)
        preserve_entity(bartender_fixture, template_name='li_bartender_1',
            userprops={'actor': 'bartender', 'category': 'Character'})
        prop_cigarette_2 = PropPropCigarette2(root=self, name='prop_cigarette_2', light_group=0,
            init_point='prop_cigarette_2', rotate_from_quat=True, use_ambient=True)
        preserve_entity(prop_cigarette_2, userprops={'category': 'Prop'})
        DX_m07_offer_0110_trent = Sound(root=self, name='DX_m07_offer_0110_trent', sound='DX_m07_offer_0110_trent',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m07_offer_0110_trent, userprops={'category': 'Audio'})
        delta = Character(root=self, actor=actors.DeltaOne, light_group=0, init_point='Char_delta1', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(delta, template_name='m06_asf_prisoner01b',
            userprops={'actor': 'Prisoner1b', 'category': 'Character'})
        prisoner2b = Character(root=self, actor=ExtraCharPrisoner2b, light_group=0, init_point='Char_prisoner2b',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(prisoner2b, template_name='m06_asf_prisoner02b',
            userprops={'actor': 'Prisoner2b', 'category': 'Character'})
        prisoner3b = Character(root=self, actor=ExtraCharPrisoner3b, light_group=0, init_point='Char_prisoner3b',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(prisoner3b, template_name='m06_asf_prisoner03b',
            userprops={'actor': 'Prisoner3b', 'category': 'Character'})
        prisoner4b = Character(root=self, actor=ExtraCharPrisoner4b, light_group=0, init_point='Char_prisoner4b',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(prisoner4b, template_name='m06_asf_prisoner04b',
            userprops={'actor': 'Prisoner4b', 'category': 'Character'})
        trent_base = Character(root=self, actor=ExtraCharTrentBase, light_group=0, init_point='Char_trent_base',
            rotate_from_quat=True, use_ambient=False, floor_height=-1000)
        preserve_entity(trent_base, template_name='trent', userprops={'Actor': 'Player', 'category': 'Character'})
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='trent_original', userprops={'actor': 'TrentOriginal', 'category': 'Character'})
        # Исправлена опечатка исходного THN: floor_height==-110 → числовое -110.
        barman = Character(root=self, actor=actors.CorsairBarman, light_group=0, init_point='Char_barman',
            rotate_from_quat=True, use_ambient=False, floor_height=-110)
        preserve_entity(barman, template_name='m07_bartender', userprops={'actor': 'm6_bartender', 'category': 'Character'})
        cam_start = LookAtCamera(root=self, name='cam_start', fov=20, farplane=5000, look_duration=70)
        preserve_entity(cam_start)
        cam_delta_sit_trent_sit_down = LookAtCamera(root=self, name='cam_delta_sit_trent_sit_down', fov=16, farplane=5000,
            look_duration=70)
        preserve_entity(cam_delta_sit_trent_sit_down)
        cam_delta_sit = LookAtCamera(root=self, name='cam_delta_sit', fov=15, farplane=5000, look_duration=70)
        preserve_entity(cam_delta_sit)
        cam_trent_sit = LookAtCamera(root=self, name='cam_trent_sit', fov=15, farplane=5000, look_duration=70)
        preserve_entity(cam_trent_sit)
        cam_delta_explaining = LookAtCamera(root=self, name='cam_delta_explaining', fov=15, farplane=5000, look_duration=70)
        preserve_entity(cam_delta_explaining)
        cam_delta_warning = LookAtCamera(root=self, name='cam_delta_warning', fov=15, farplane=5000, look_duration=100)
        preserve_entity(cam_delta_warning)
        cam_trent_standup = LookAtCamera(root=self, name='cam_trent_standup', fov=15, farplane=5000, look_duration=150)
        preserve_entity(cam_trent_standup)
        cam_barman = LookAtCamera(root=self, name='cam_barman', fov=15, farplane=5000, look_duration=150)
        preserve_entity(cam_barman)
        cam_second_start = LookAtCamera(root=self, name='cam_second_start', fov=15, farplane=5000, look_duration=150)
        preserve_entity(cam_second_start)
        cam_trent_deal = LookAtCamera(root=self, name='cam_trent_deal', fov=15, farplane=5000, look_duration=70)
        preserve_entity(cam_trent_deal)

        # Вход / начальная постановка.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_bartender_fixture', target_name='offscreen',
            duration=0, smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent_base', target_name='offscreen', duration=0,
            smooth=False)
        delta.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=4, loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner2b',
            anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=25, loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner3b',
            anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=25, loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner4b',
            anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=25, loop=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=10, loop=True)
        cam_start.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_start', target_name='automarker_cam_start_pos2',
            duration=7, smooth=True)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='Char_delta1', duration=25,
            transition_duration=3, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_delta1', target_name='Char_trent', duration=25,
            transition_duration=2, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 0.01
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent_base',
            anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=1, time_scale=0.8, trans_time=1)
        t += 1.99
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner3b',
            anim=Male.Sc_MLBODY_CHRB_TWSTU_CCL_LESS_000LV_A_14, duration=21, start_time=7, trans_time=1)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=28, axis='Y_AXIS', duration=4,
            smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_start_focus',
            target_name='automarker_cam_start_marker_pos2', duration=5, smooth=True)
        t += 2
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner2b',
            anim=Male.Sc_MLBODY_CHRF_TWSTS_LOOK_090LV_XA_02, duration=21, time_scale=0.6, trans_time=1)
        delta.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=15, time_scale=0.6,
            trans_time=1)
        t += 1
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_prisoner4b', target_name='Char_trent', duration=5,
            transition_duration=3, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        main_group.append_time(10)


        # Реплика 10 · delta1 · исходное время 10 с
        # Мистер Трент, мы благодарим вас за вашу работу. Мы виноваты в том, что вы попали в неприятности. И мы
        # постараемся исправить ситуацию.
        # Исходное окно facial: 13.3 с.
        t = 0
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner2b',
            anim=Male.Sc_MLBODY_CHRF_TWSTS_FROM_090LV_XA_02, duration=21, time_scale=0.6, trans_time=1)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent',
            target_name='automarker_point_trent_sit_down', duration=0, smooth=False)
        cam_delta_sit_trent_sit_down.set(group=MAIN, time_delay=t)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner4b',
            anim=Male.Sc_MLBODY_CHRF_TAP_RHND_000LV_A_02, duration=17, time_scale=0.3, loop=True, trans_time=1)
        t += 0.01
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_SITCR_TRNS_180DN_XA_06, duration=15)
        t += 0.99
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_delta_sit_trent_sit_down',
            target_name='automarker_cam_delta_sit_trent_sit_down_pos2', duration=13, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_delta_sit_trent_sit_down_focus',
            target_name='automarker_cam_delta_sit_trent_sit_down_marker_pos2', duration=13, smooth=True)
        t += 4
        delta.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=15, time_scale=0.5,
            trans_time=1)
        t += 7.9
        delta.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=4.444, time_scale=0.9,
            trans_time=1)
        select_dialogue(self, 6, 'Msn6Freeport', 'm06_freeport')
        delta.facial(group=MAIN, index=10, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(0.2)


        # Реплика 20 · trent · исходное время 23.5 с
        # Это все хорошо, конечно, но что мне, собственно, делать сейчас?
        # Исходное окно facial: 6 с.
        t = 0
        cam_trent_sit.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=20, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.5)


        # Реплика 30 · delta1 · исходное время 28 с
        # Ведите себя тихо, пока можете выполнять контрактны на местных базах, но ни в коем случае не возвращайтесь
        # в легальные системы.
        # Исходное окно facial: 11 с.
        t = 0
        cam_delta_explaining.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_delta_explaining',
            target_name='automarker_cam_delta_explaining_pos2', duration=20, smooth=True)
        delta.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_TALK_HNSTBL_000LV_A_34, duration=20, time_scale=0.8,
            trans_time=1)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_MED_000LV_XA_07, duration=62, time_scale=0.6,
            loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner4b',
            anim=Male.Sc_MLBODY_CHRF_IDLE_BIG_000LV_XA_06, duration=10, time_scale=0.6, start_time=2, loop=True)
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='prop_cigarette_2',
            parent_name='Char_prisoner4b', duration=50, target_hardpoint='hprightconnect_cigarette',
            parent_hardpoint='hprightconnect')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_delta1', target_name='Char_trent', duration=72,
            transition_duration=2, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_delta1', target_name='Char_trent', duration=72,
            transition_duration=4, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 10
        delta.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=1, time_scale=0.9,
            trans_time=0.5)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner4b',
            anim=Male.Sc_MLBODY_CHRF_TAP_RHND_000LV_A_02, duration=5, time_scale=0.4, loop=True, trans_time=1)
        delta.facial(group=MAIN, index=30, append=True, auto_lip=True, extra_delay=0)
        t = 0


        # Реплика 40 · delta1 · исходное время 39 с
        # А я пока постараюсь наладить связь со штабом СБА и выработать дальнейший план действий.
        # Исходное окно facial: 12 с.
        t = 0
        t += 4
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner4b',
            anim=Male.Sc_MLBODY_CHRF_GRABR_CHIN_RLEASE_000LV_XA_02, duration=5, time_scale=0.5, trans_time=1)
        t += 3
        delta.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=1, time_scale=0.9,
            trans_time=0.5)
        delta.facial(group=MAIN, index=40, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-4)


        # Реплика 50 · delta1 · исходное время 47 с
        # В благодарность за вашу работу я сейчас переведу вам пять тысяч кредитов. Обещанное вознаграждение за
        # миссию так же остается за вами и будет выплачено позже.
        # Исходное окно facial: 12.5 с.
        t = 0
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner4b',
            anim=Male.Sc_MLBODY_CHRF_CHIN_HOLDR_000LV_XA_03, duration=5, time_scale=0.5, loop=True, trans_time=0.5)
        t += 1
        delta.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, duration=15, loop=True,
            trans_time=3)
        t += 4
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner4b',
            anim=Male.Sc_MLBODY_CHRF_HOLD_CHIN_RLEASE_000LV_XA_03, duration=5, time_scale=0.5, trans_time=0.5)
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_delta_explaining',
            target_name='automarker_cam_delta_explaining_pos3', duration=15, smooth=True)
        t += 1
        delta.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDUP_TRNS_000LV_XA_02, duration=2,
            time_scale=0.75, trans_time=0.25)
        delta.facial(group=MAIN, index=50, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-4.5)


        # Реплика 60 · delta1 · исходное время 55 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m06_freeport_0060_delta1
        # Исходное окно facial: 18 с.
        t = 0
        t += 1
        delta.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_RHND_CASL_000LV_XA_04, duration=3.7,
            time_scale=0.75, loop=True, trans_time=0.25)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner4b',
            anim=Male.Sc_MLBODY_CHRF_TAP_RHND_000LV_A_02, duration=5, time_scale=0.4, loop=True, trans_time=1)
        t += 3
        delta.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDDN_TRNS_000LV_XA_02, duration=3,
            time_scale=0.5, trans_time=1)
        t += 2
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner4b',
            anim=Male.Sc_MLBODY_CHRF_GRABR_CHIN_RLEASE_000LV_XA_02, duration=5, time_scale=0.5, trans_time=1)
        t += 2.5
        delta.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=15, time_scale=0.4,
            trans_time=1)
        t += 1.5
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner4b',
            anim=Male.Sc_MLBODY_CHRF_CHIN_HOLDR_000LV_XA_03, duration=5, time_scale=0.5, loop=True, trans_time=0.5)
        t += 4
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner4b',
            anim=Male.Sc_MLBODY_CHRF_HOLD_CHIN_RLEASE_000LV_XA_03, duration=5, time_scale=0.5, trans_time=0.5)
        # delta.facial(group=MAIN, index=60, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(18)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2)


        # Реплика 70 · trent · исходное время 71 с
        # А как же компенсация за моральный ущерб?
        # Исходное окно facial: 6 с.
        t = 0
        cam_trent_sit.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=70, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-3)


        # Реплика 90 · delta1 · исходное время 74 с
        # Так что... как только появятся новости, мы с вами свяжемся.
        # Исходное окно facial: 14 с.
        t = 0
        cam_delta_warning.set(group=MAIN, time_delay=t)
        delta.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, duration=15, loop=True)
        t += 1
        delta.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDUP_TRNS_000LV_XA_02, duration=2,
            time_scale=0.75, trans_time=0.25)
        t += 2
        delta.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_RHND_CASL_000LV_XA_04, duration=3.7,
            time_scale=0.75, loop=True, trans_time=0.25)
        t += 3
        delta.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDDN_TRNS_000LV_XA_02, duration=3,
            time_scale=0.5, trans_time=1)
        t += 4
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_delta_warning',
            target_name='automarker_cam_delta_warning_pos2', duration=5, smooth=True)
        delta.facial(group=MAIN, index=90, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-3.5)


        # Реплика 100 · delta1 · исходное время 84.5 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m06_freeport_0100_delta1
        # Исходное окно facial: 11 с.
        t = 0
        t += 0.5
        delta.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=15, time_scale=0.5,
            trans_time=1)
        t += 3.0
        barman.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_BART_000LV_XA_10, duration=12, time_scale=0.8,
            start_time=1, loop=True)
        t += 1.0
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_WALK_TRNS_090LV_XA_10, duration=15, trans_time=1)
        t += 1.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_trent_standup',
            target_name='automarker_cam_trent_standup_pos2', duration=10, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_trent_standup_focus',
            target_name='automarker_cam_trent_standup_marker_pos2', duration=10, smooth=True)
        t += 2.0
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=-97, axis='Y_AXIS', duration=5,
            smooth=True)
        t += 1.0
        cam_trent_standup.set(group=MAIN, time_delay=t)
        t += 1.15
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=5.2, loop=True)
        # delta.facial(group=MAIN, index=100, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(11.0)  # длительность удалённой реплики
        t = 0
        t += 2.5
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_head_barman_near',
            duration=100, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 1.35
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=4)
        main_group.append_time(4.5)


        # Реплика 10 · barman · исходное время 100 с
        # Чего налить?
        # Исходное окно facial: 4.7 с.
        t = 0
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner2b',
            anim=Male.Sc_MLBODY_CHRB_WALK_TRNS_090LV_XA_10, duration=15, time_scale=0.7, trans_time=1)
        cam_second_start.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_second_start',
            target_name='automarker_cam_second_start_pos2', duration=5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_second_start_focus',
            target_name='automarker_cam_second_start_marker_pos2', duration=5, smooth=True)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_barman', target_name='Char_trent', duration=55,
            transition_duration=2, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        barman.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=100, time_scale=0.8,
            loop=True, trans_time=1)
        select_dialogue(self, 7, 'Msn7Offer', 'm07_offer')
        self.groups.pop('motion_10', None)
        barman.facial(group=MAIN, index=10, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-3.2)


        # Реплика 20 · trent · исходное время 101.5 с
        # Дельца какого-нибудь, желательно с хорошей оплатой.
        # Исходное окно facial: 6 с.
        t = 0
        t += 0.5
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner3b',
            anim=Male.Sc_MLBODY_CHRB_WALK_TRNS_270LV_XA_10, duration=15, time_scale=0.7, trans_time=1)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=15,
            time_scale=0.6, trans_time=1)
        self.groups.pop('motion_20', None)
        trent.facial(group=MAIN, index=20, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2.0)


        # Реплика 30 · barman · исходное время 105.5 с
        # Да у нас тут вроде и в своих фрилансерах недостатка нет, понимаете же в какой системе находитесь.
        # Исходное окно facial: 6 с.
        t = 0
        cam_barman.set(group=MAIN, time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner2b', target_name='offscreen', duration=0,
            smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner3b', target_name='offscreen', duration=0,
            smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner4b', target_name='offscreen', duration=0,
            smooth=False)
        t += 2.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_delta1',
            target_name='automarker_point_delta_walkout', duration=0.001, smooth=False)
        self.groups.pop('motion_30', None)
        barman.facial(group=MAIN, index=30, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1.0)


        # Реплика 40 · trent · исходное время 110.5 с
        # А я… скидку хорошую сделаю! Выручай дружище, я совсем на мели.
        # Исходное окно facial: 9.5 с.
        t = 0
        delta.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=55, loop=True)
        cam_trent_deal.set(group=MAIN, time_delay=t)
        t += 1.5
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=15,
            time_scale=0.6, trans_time=1)
        self.groups.pop('motion_40', None)
        trent.facial(group=MAIN, index=40, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-3.0)


        # Реплика 50 · barman · исходное время 117 с
        # Окей, мистер...
        # Исходное окно facial: 6 с.
        t = 0
        cam_second_start.set(group=MAIN, time_delay=t)
        self.groups.pop('motion_50', None)
        barman.facial(group=MAIN, index=50, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-4.7)


        # Реплика 60 · trent · исходное время 118.3 с
        # Трент
        # Исходное окно facial: 6 с.
        t = 0
        self.groups.pop('motion_60', None)
        trent.facial(group=MAIN, index=60, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-4.8)


        # Реплика 70 · barman · исходное время 119.5 с
        # Окей, мистер Трент. Будет для вас дельце.
        # Исходное окно facial: 6 с.
        t = 0
        cam_barman.set(group=MAIN, time_delay=t)
        self.groups.pop('motion_70', None)
        barman.facial(group=MAIN, index=70, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-3.5)


        # Реплика 80 · barman · исходное время 122 с
        # К нам тут гастролеры пожаловали из Либерти. Называют себя бандой Старлайна.
        # Исходное окно facial: 6 с.
        t = 0
        barman.facial(group=MAIN, index=80, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-1)


        # Реплика 90 · barman · исходное время 127 с
        # Найдите их и убейте Билла Айронсайда - их лидера. Координаты их предположительного местонахождения я вам
        # скину.
        # Исходное окно facial: 6 с.
        t = 0
        self.groups.pop('motion_90', None)
        barman.facial(group=MAIN, index=90, append=True, auto_lip=True, extra_delay=0)
        t = 0


        # Реплика 100 · barman · исходное время 133 с
        # Но учтите, гонорар будет ниже, чем обычно...
        # Исходное окно facial: 6 с.
        t = 0
        self.groups.pop('motion_100', None)
        barman.facial(group=MAIN, index=100, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-3.0)
        restore_dialogue(self)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M07OfferScene
