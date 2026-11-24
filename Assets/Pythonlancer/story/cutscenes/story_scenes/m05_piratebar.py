"""m05_piratebar: полная постановка из master; точки в m05_piratebar.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Alchemy, AttachEvent, Character, ConnectHardpointEvent, LookAtCamera, MAIN, Male, MoveEvent, NeckIkEvent, Prop, RotateAxisEvent,
)
from story.cutscenes.anim import (
    Male, Trent,
)
from story import actors


class PropCigarette2Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'cigarette_2'

class PropPdaProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'pda'


class M05PiratebarScene(Scene):
    DUMP_FILE = 'm05_piratebar'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Персонажи, камеры, реквизит и звук.
        vfx_rtc_sydsmoke_3 = Alchemy(root=self, name='vfx_rtc_sydsmoke_3', particles='rtc_sydsmoke',
            point_name='vfx_rtc_sydsmoke_3', sparam=0, light_group=0, sort_group=0, hidden=False, use_ambient=True)
        vfx_rtc_cigaretteglow_4 = Alchemy(root=self, name='vfx_rtc_cigaretteglow_4',
            particles='rtc_cigaretteglow', point_name='vfx_rtc_cigaretteglow_4', sparam=0, light_group=0,
            sort_group=0, hidden=False, use_ambient=True)
        prop_cigarette_2 = PropCigarette2Prop(root=self, name='prop_cigarette_2', light_group=0,
            init_point='prop_cigarette_2', rotate_from_quat=True, use_ambient=True)
        prop_pda = PropPdaProp(root=self, name='prop_pda', light_group=0, init_point='prop_pda',
            rotate_from_quat=True)
        smith = Character(root=self, actor=actors.Smith, name='Char_smith', light_group=0,
            init_point='Char_smith', rotate_from_quat=True, appearance='m05_smith', actor_name='m05_smith')
        trent = Character(root=self, actor=actors.Trent, name='Char_trent', light_group=0,
            init_point='Char_trent', rotate_from_quat=True, appearance='trent', actor_name='Player')
        cam_start = LookAtCamera(root=self, name='cam_start', fov=20, look_duration=300)
        cam_trent_stand = LookAtCamera(root=self, name='cam_trent_stand', fov=20, look_duration=300)
        cam_smith = LookAtCamera(root=self, name='cam_smith', fov=18, look_duration=300)
        cam_smith_far = LookAtCamera(root=self, name='cam_smith_far', fov=20, look_duration=300)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=18, look_duration=300)
        cam_trough = LookAtCamera(root=self, name='cam_trough', fov=30, look_duration=300)
        cam_trent_sidetalk = LookAtCamera(root=self, name='cam_trent_sidetalk', fov=18, look_duration=300)

        # Исходные точки взгляда.

        # Вход.
        t = 0
        AttachEvent(root=self, group=MAIN, target_name=vfx_rtc_sydsmoke_3.name, parent_name=prop_cigarette_2.name,
            duration=200, target_part='HP_cigarette_Tip_smoke', target_type='HARDPOINT', adjust_pos=True,
            adjust_orient=False, up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=vfx_rtc_cigaretteglow_4.name,
            parent_name=prop_cigarette_2.name, duration=200, target_part='HP_cigarette_Tip_smoke',
            target_type='HARDPOINT', adjust_pos=True, adjust_orient=True, up='Y_AXIS', front='NEG_Z_AXIS',
            time_delay=t)
        vfx_rtc_cigaretteglow_4.start(group=MAIN, duration=105, time_delay=t)
        vfx_rtc_sydsmoke_3.start(group=MAIN, duration=105, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLHAND_NEUT_LEFT_000LV_A_00, duration=5, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLHAND_NEUT_RGHT_000LV_A_00, duration=5, time_delay=t)
        ConnectHardpointEvent(root=self, group=MAIN, target_name=prop_cigarette_2.name, parent_name=smith.name,
            duration=105, target_hardpoint='hprightconnect_cigarette2', parent_hardpoint='hprightconnect',
            time_delay=t)
        cam_start.set(group=MAIN, time_delay=t)
        cam_start.move_cam(group=MAIN, index=2, duration=8, smooth=True, time_delay=t)
        cam_start.move_focus(group=MAIN, index=2, duration=8, smooth=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=3.9, loop=True, time_delay=t)
        smith.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_POINT_RGHT_MILI_000LV_00, duration=0.5, time_scale=10,
            time_delay=t)
        smith.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, duration=2, time_delay=t)
        t += 1
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=2, transition_duration=1, time_delay=t)
        t += 1
        smith.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_GRABR_CHIN_RLEASE_000LV_XA_02, duration=5,
            trans_time=0.3, time_delay=t)
        t += 1.9
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=3, time_delay=t)
        t += 0.1
        smith.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CHIN_HOLDR_000LV_XA_03, duration=4, loop=True,
            time_delay=t)
        t += 2.2
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_TURN_270LV_XA_04, duration=4, trans_time=0.25,
            time_delay=t)
        t += 0.8
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=24, transition_duration=2, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=45, axis='Y_AXIS', duration=2,
            smooth=True, time_delay=t)
        t += 1
        smith.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_HOLD_CHIN_RLEASE_000LV_XA_03, duration=15, trans_time=1,
            time_delay=t)
        t += 1
        smith.motion(group=MAIN, anim=Male.Sc_MLHAND_NEUT_RGHT_000LV_A_00, duration=5, trans_time=1, time_delay=t)
        main_group.append_time(10)

        # m05_piratebar 10: Trent.
        # Хай, бро! Есть чо? А то я тут с такого дальняка вернулся, что все мозги закисли, расслабиться бы...
        t = 0
        cam_trent_stand.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WAVE_RHND_000LV_XA_02, duration=1.5, time_scale=0.7,
            trans_time=0.25, time_delay=t)
        t += 1.5
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_TALK_SMALL_000DN_A_17, duration=6.5, time_scale=0.75,
            trans_time=2, time_delay=t)
        t += 0.5
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=25, axis='Y_AXIS', duration=2.5,
            smooth=True, time_delay=t)
        smith.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_GRABR_CHIN_RLEASE_000LV_XA_02, duration=5, time_delay=t)
        t += 4
        smith.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_POINT_RGHT_MILI_000LV_00, duration=0.5, time_scale=10,
            time_delay=t)
        t += 0.5
        t += 0.5
        trent.facial(group=MAIN, index=10, auto_lip=True)

        cam_smith_far.set(group=MAIN, time_delay=0)
        # Действие после исходного окна реплики.
        t = 0

        # m05_piratebar 20: Smith.
        # Та не, откуда, сам с пятого на десятое перебиваюсь.
        t = 0

        smith.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CHIN_HOLDR_000LV_XA_03, duration=1.5, loop=True,
            time_delay=-5)

        smith.motion(group=MAIN, anim=Male.Sc_MLHAND_NEUT_RGHT_000LV_A_00, duration=5, trans_time=1, time_delay=-1)

        smith.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_HOLD_CHIN_RLEASE_000LV_XA_03, duration=15, trans_time=1,
            time_delay=-1)

        main_group.append_time(0.5)
        t += 1.5
        NeckIkEvent(root=self, group=MAIN, char_name=smith.name,
            target_name=self.get_automarker_name('smith_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=7, transition_duration=1, time_delay=t)
        t += 3
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('smith_head_ik'),
            target_name=self.get_automarker_name('head_smith_front_btm'), duration=2, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        smith.facial(group=MAIN, index=20, auto_lip=True)
        # Действие после исходного окна реплики.
        t = 0
        cam_trent_stand.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('out_window_center'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=5,
            time_scale=0.7, trans_time=1, time_delay=t)
        main_group.append_time(1)

        # m05_piratebar 30: Trent.
        # Вот же козлы все эти пиджаки из ДипСпейс. Я им работу сработал, а они мне на Детройте даже посадку
        # не дали, типа мордой не вышел, пропуска нет.
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('smith_head_ik'),
            target_name=self.get_automarker_name('head_smith_front'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 2
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_smith'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 1
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=5, time_scale=0.5,
            trans_time=1, time_delay=t)
        t += 1
        smith.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_POINT_RGHT_MILI_000LV_00, duration=0.5, time_scale=10,
            time_delay=t)
        t += 1
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_SITCL_TRNS_180DN_XA_06, duration=3.4, time_scale=0.85,
            trans_time=0.25, time_delay=t)
        t += 3
        smith.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, duration=2, time_delay=t)
        t += 0.4
        cam_trough.set(group=MAIN, time_delay=t)
        cam_trough.move_cam(group=MAIN, index=2, duration=15, smooth=True, time_delay=t)
        cam_trough.move_focus(group=MAIN, index=2, duration=15, smooth=True, time_delay=t)
        t += 0.0001
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('point_trent_sit_side'), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.0001
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_TALK_000LV_A_16, duration=15.1, time_scale=0.75,
            loop=True, time_delay=t)
        trent.facial(group=MAIN, index=30, auto_lip=True)

        # m05_piratebar 40: Trent.
        # А у меня там заначка козырная, месяц оттопыриваться можно - из омикронов привез, дельце там одно
        # провернул.
        t = 0
        smith.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_TAP_RHND_000LV_A_02, duration=5.5, time_scale=0.7,
            trans_time=0.25, loop=True, time_delay=t)
        t += 5.5
        smith.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_GRABR_CHIN_RLEASE_000LV_XA_02, duration=5,
            trans_time=0.3, time_delay=t)
        trent.facial(group=MAIN, index=40, auto_lip=True)

        # m05_piratebar 50: Trent.
        # А теперь из-за этой мать ее боевой готовности сидеть тут пойлом местным травиться...  А когда она
        # еще закончится, готовность эта...
        t = 1
        smith.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CHIN_HOLDR_000LV_XA_03, duration=3, loop=True,
            time_delay=t)
        t += 3
        smith.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_HOLD_CHIN_RLEASE_000LV_XA_03, duration=15, trans_time=1,
            time_delay=t)
        t += 1
        smith.motion(group=MAIN, anim=Male.Sc_MLHAND_NEUT_RGHT_000LV_A_00, duration=5, trans_time=1, time_delay=t)
        trent.facial(group=MAIN, index=50, auto_lip=True)

        # m05_piratebar 55: Trent.
        # Эх, пропуск бы где раздобыть, я бы сундучок-то свой оттуда выцепил бы, оттянулись бы по полной...
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_TWSTU_CLOC_LESS_000LV_A_14, duration=25,
            time_scale=0.75, start_time=9, time_delay=t)
        t += 7.5
        trent.facial(group=MAIN, index=55, auto_lip=True)

        t = 0

        cam_smith.set(group=MAIN, time_delay=t)

        smith.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_HOLD_CHIN_RLEASE_000LV_XA_03, duration=15, time_delay=t)
        smith.motion(group=MAIN, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=3, time_scale=0.4,
            trans_time=0.25, time_delay=t)

        # m05_piratebar 60: Smith.
        # Слыш, это, дружище... Тебя как зовут?

        smith.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_GRABR_CHIN_RLEASE_000LV_XA_02, duration=5,
            trans_time=0.3, time_delay=0)

        main_group.append_time(2)

        smith.facial(group=MAIN, index=60, auto_lip=True)
        main_group.append_time(1)

        t = -2
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('point_trent_sit_side'), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t = -1
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=1, time_delay=t)
        t = 0
        cam_trent_sidetalk.set(group=MAIN, time_delay=t)
        t += 0.5
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=10, transition_duration=2, time_delay=-1)
        t += 0.5
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=-90, axis='Y_AXIS', duration=2,
            smooth=True, time_delay=-0.5)

        # m05_piratebar 70: Trent.
        # Трент. а тебя как?
        t = 0.5
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=3, time_scale=0.92,
            trans_time=0.25, time_delay=t)
        t += 0.5
        smith.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, duration=2, time_delay=t)
        trent.facial(group=MAIN, index=70, auto_lip=True)
        # Действие после исходного окна реплики.
        t = 0
        cam_smith_far.set(group=MAIN, time_delay=t)
        smith.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, duration=5, time_delay=t)
        main_group.append_time(0.5)

        # m05_piratebar 80: Smith.
        # Смит. Мистер Смит.
        smith.facial(group=MAIN, index=80, auto_lip=True)

        # m05_piratebar 90: Trent.
        # Приятно познакомитьcя. Мистер Смит, ты там что-то сказать хотел.
        t = 0
        cam_trent_sidetalk.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, duration=0.2, time_delay=t)
        t += 0.8
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDUP_TRNS_000LV_XA_02, duration=4,
            trans_time=0.25, time_delay=t)
        t += 1.5
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDDN_TRNS_000LV_XA_02, duration=3,
            time_scale=0.8, trans_time=0.25, time_delay=t)
        trent.facial(group=MAIN, index=90, auto_lip=True)

        # m05_piratebar 100: Smith.
        # Да? Да. А, Да! Я знаю где можно пропуск достать.
        t = 0
        cam_smith.set(group=MAIN, time_delay=0)
        smith.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, duration=5, time_delay=t)
        t += 0.5
        trent.motion(group=MAIN, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, duration=8, time_scale=0.6,
            trans_time=1, time_delay=t)
        t += 5
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, duration=1, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=10, transition_duration=1, time_delay=t)
        t += 1.2
        smith.motion(group=MAIN, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=8, time_scale=0.6,
            trans_time=1, time_delay=t)
        t += 0.8
        smith.facial(group=MAIN, index=100, auto_lip=True)
        cam_trent_sidetalk.set(group=MAIN, time_delay=0)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_LEAN_ARMB_000LV_A_10, duration=5, time_scale=0.5,
            time_delay=t)

        # m05_piratebar 110: Trent.
        # Да ты что! И где.
        t = 1
        smith.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=1, time_delay=t)
        trent.facial(group=MAIN, index=110, auto_lip=True)
        # Действие после исходного окна реплики.
        t = 0
        cam_smith_far.set(group=MAIN, time_delay=t)
        ConnectHardpointEvent(root=self, group=MAIN, target_name=prop_pda.name, parent_name=smith.name,
            duration=17, target_hardpoint='Hp_LHand_PDA', parent_hardpoint='HpLeftConnect', time_delay=t)
        smith.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=2, time_delay=t)
        main_group.append_time(1)

        # m05_piratebar 120: Smith.
        # Смотри. Вот тут склад есть секретный. Там у ребят пара штук на крайний случай точно есть. Я знаю.
        # Попробуй с ними договориться. Только ты это... Никому. Склад-то секретный!
        t = 1
        smith.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CONV_LHNDUP_TRNS_000LV_XA_02, duration=7,
            time_scale=0.5, trans_time=0.25, time_delay=t)
        t += 2.5
        smith.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CONV_LHND_CASL_000LV_xa_03, duration=4, time_scale=0.5,
            trans_time=1, time_delay=t)
        t += 4
        smith.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CONV_LHNDDN_TRNS_000LV_XA_02, duration=4,
            time_scale=0.5, trans_time=1, time_delay=t)
        t += 3.5
        smith.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CONV_LHNDUP_TRNS_000LV_XA_02, duration=7,
            trans_time=0.25, time_delay=t)
        t += 2
        smith.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=5, time_scale=0.5,
            start_time=1, trans_time=1, time_delay=t)
        smith.facial(group=MAIN, index=120, auto_lip=True)
        # Действие после исходного окна реплики.
        t = 0
        smith.motion(group=MAIN, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=4, trans_time=1, time_delay=t)
        main_group.append_time(1)

        # m05_piratebar 130: Trent.
        # Замётано, бро!
        t = 0
        cam_trent_sidetalk.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_WALK_TRNS_270LV_XA_10, duration=5, time_delay=t)
        t += 0.1
        MoveEvent(root=self, group=MAIN, object_name=prop_cigarette_2.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.9
        MoveEvent(root=self, group=MAIN, object_name=prop_pda.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        trent.facial(group=MAIN, index=130, auto_lip=True)
        # Действие после исходного окна реплики.
        main_group.append_time(2)
        t = 0
        cam_smith.set(group=MAIN, time_delay=t)
        smith.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_TWSTU_CLOC_LESS_000LV_A_14, duration=25,
            time_scale=0.75, start_time=8, time_delay=t)
        t += 0.01
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        main_group.append_time(4)

        # m05_piratebar 140: Smith.
        # Ты с сундучком-то забегай...
        smith.facial(group=MAIN, index=140, auto_lip=True)
        # Действие после исходного окна реплики.
        main_group.append_time(1)
