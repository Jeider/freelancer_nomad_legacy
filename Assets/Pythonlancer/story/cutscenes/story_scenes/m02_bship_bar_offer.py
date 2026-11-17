"""Предложение Вильгельма: полная сцена master на API Pythonlancer."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    MAIN, Character, LookAtCamera, Prop, Alchemy, AttachEvent,
    ConnectHardpointEvent, MoveEvent, MoveFastEvent, TARGET_HARDPOINT,
)
from story.cutscenes.anim import Male, Trent
from story import actors


class Ashtray(Prop):
    COMPOUND_TEMPLATE_NAME = 'ashtray_2'


class PDA(Prop):
    COMPOUND_TEMPLATE_NAME = 'pda'


class Msn2OfferScene(Scene):
    DUMP_FILE = 'm02_bship_bar_offer'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Персонажи.
        trent = Character(root=self, actor=actors.Trent, light_group=0,
                          init_point='Char_trent', rotate_from_quat=True)
        wilham = Character(root=self, actor=actors.Wilham, light_group=0,
                          init_point='Char_wilham', rotate_from_quat=True)

        # Камеры и их точки *_focus, *2, *_focus2 в Blender.
        cam_start = LookAtCamera(root=self, name='cam_start', fov=35)
        cam_wilham_top = LookAtCamera(root=self, name='cam_wilham_top', fov=25)
        cam_trent_stand = LookAtCamera(root=self, name='cam_trent_stand', fov=20)
        cam_trent_top = LookAtCamera(root=self, name='cam_trent_top', fov=25)
        cam_wilham_far = LookAtCamera(root=self, name='cam_wilham_far', fov=30)
        cam_sitting = LookAtCamera(root=self, name='cam_sitting', fov=30)
        cam_trent_near = LookAtCamera(root=self, name='cam_trent_near', fov=25)
        cam_wilham_near = LookAtCamera(root=self, name='cam_wilham_near', fov=25)
        cam_trent_closest = LookAtCamera(root=self, name='cam_trent_closest', fov=20)
        cam_msn_begins = LookAtCamera(root=self, name='cam_msn_begins', fov=35)
        cam_wilham_msn1 = LookAtCamera(root=self, name='cam_wilham_msn1', fov=25)
        cam_wilham_middle = LookAtCamera(root=self, name='cam_wilham_middle', fov=25)
        cam_wilham_msn2 = LookAtCamera(root=self, name='cam_wilham_msn2', fov=25)
        cam_wilham_msn3 = LookAtCamera(root=self, name='cam_wilham_msn3', fov=25)

        # Реквизит.
        ashtray = Ashtray(root=self, name='ashtray', light_group=0,
                          init_point='Prop_ashtray_extra_1', rotate_from_quat=True)
        pda = PDA(root=self, name='pda', light_group=0,
                          init_point='Prop_pda', rotate_from_quat=True)
        smoke = Alchemy(root=self, name='smoke',
                          particles='rtc_sydsmoke', point_name='vfx_rtc_sydsmoke_3')

        # Начальная расстановка взглядов.
        trent.move_head_ik(group=MAIN, target_name=self.get_automarker_name('trent_head_ik'), immediately=True)
        trent.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('trent_eye_ik'), immediately=True)
        wilham.move_head_ik(group=MAIN, target_name=self.get_automarker_name('wilham_head_ik'), immediately=True)
        wilham.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('wilham_eye_ik'), immediately=True)


        trent.motion(group=MAIN, anim=Male.Sc_MLHAND_NEUT_LEFT_000LV_A_00, duration=1, time_delay=0)
        trent.motion(group=MAIN, anim=Male.Sc_MLHAND_NEUT_RGHT_000LV_A_00, duration=1, time_delay=0)

        # Вход.
        t = 0
        trent.start_head_ik(group=MAIN, duration=30, time_delay=t)
        trent.start_eye_ik(group=MAIN, duration=30, time_delay=t)
        wilham.start_head_ik(group=MAIN, duration=33, time_delay=t)
        wilham.start_eye_ik(group=MAIN, duration=33, time_delay=t)
        cam_start.set(group=MAIN, time_delay=t)
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_SMALL_000LV_XA_07, duration=4, loop=True,
            time_delay=t)
        t += 1
        cam_start.move_focus(group=MAIN, index=2, duration=20, time_delay=t, smooth=False)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=5, time_scale=0.75,
            start_time=0.25, time_delay=t)
        t += 1
        wilham.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_trent_stand'), duration=2,
            time_delay=t)
        t += 0.5
        wilham.move_head_ik(group=MAIN, target_name=self.get_automarker_name('head_trent_stand'), duration=2,
            time_delay=t)
        main_group.append_time(3)

        # 10: trent.
        # Вильгельм, я полагаю?
        trent.facial(group=MAIN, index=10, auto_lip=True, extra_delay=0)

        # 20: wilham.
        # Так точно, герр Трент. Я рад, что вы согласились с нами работать.
        t = 0.5
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_XB_04, duration=5, trans_time=2, time_delay=t)
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_TALK_000UP_A_17, duration=14, trans_time=2, loop=True,
            time_delay=t)
        t += 3
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_XB_04, duration=2, time_delay=t)
        wilham.facial(group=MAIN, index=20, auto_lip=True, extra_delay=0)

        # 30: trent.
        # Еще не согласился, но определенно заинтересовался. Не каждый день представители вооруженных сил
        # Рейнланда присылают мне сообщения на КПК с предложением личной встречи на борту линкора вооруженных
        # сил Рейнланда.
        t = 0.5
        t += 9
        wilham.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('wilham_front'), duration=1,
            time_delay=t)
        wilham.move_head_ik(group=MAIN, target_name=self.get_automarker_name('head_trent_stand_half'), duration=2,
            time_delay=t)
        #cam_start.move_focus(group=MAIN, index=1, duration=5, time_delay=t)
        trent.facial(group=MAIN, index=30, auto_lip=True, extra_delay=0)

        t = 0
        wilham.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_trent'), duration=3,
            time_delay=t)
        wilham.move_head_ik(group=MAIN, target_name=self.get_automarker_name('head_trent'), duration=3,
            time_delay=t)
        MoveFastEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('point_trent_stand_to_sit'), time_delay=t)
        cam_sitting.set(group=MAIN, time_delay=t)
        cam_sitting.move_focus(group=MAIN, index=2, duration=10, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_SITCL_TRNS_180DN_XA_06, duration=5.5, time_delay=t)

        # 60: wilham.
        # Да черт с ними, с сообщениями, герр Трент, давайте лучше о деле. И да, надеюсь, вы понимаете, что
        # вне зависимости от того чем закончится наш разговор, все его детали должны остаться между нами?
        t = 3
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_LOOK_RLLV_A_06, duration=9, time_scale=0.75,
            trans_time=1, loop=True, time_delay=t)
        t += 2
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_SMALL_000LV_XA_07, duration=7, trans_time=1,
            loop=True, time_delay=t)
        wilham.facial(group=MAIN, index=40, auto_lip=True)

        # 70: trent.
        # Должны - значит останутся. Любите вы, военные, жути нагнать... Кстати, а почему именно я?
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_YESS_000LV_A_01, duration=6, time_scale=0.6,
            time_delay=t)
        t += 2
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_TALK_000UP_A_17, duration=6, time_scale=0.8,
            trans_time=1, time_delay=t)
        trent.facial(group=MAIN, index=50, auto_lip=True, extra_delay=1)

        # 120: wilham.
        # Так вот, некоторое время назад один из информаторов вышел на связь по условленному каналу, сообщил,
        # что имеет информацию крайней степени важности и вылетел на своем корабле в условленную точку для
        # передачи данных. И в лучших традициях детективов в точке этой так и не появился. Не обозначил он
        # своего присутствия в течении недели и по месту внедрения, и по аварийным каналам. Это может означать
        # лишь одно - он мертв.
        t = 0
        cam_wilham_msn1.set(group=MAIN, time_delay=t)
        cam_wilham_msn1.move_cam(group=MAIN, index=2, duration=32, time_delay=t)
        wilham.start_eye_ik(group=MAIN, duration=50, time_delay=t)
        wilham.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_trent_middle'), duration=2,
            time_delay=t)
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_TALK_HNSTBL_000LV_A_34, duration=26, time_scale=0.7,
            start_time=2, trans_time=2, time_delay=t)
        t += 3
        wilham.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('table_center'), duration=2,
            time_delay=t)
        t += 2
        wilham.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_trent_middle'), duration=2,
            time_delay=t)
        t += 5
        wilham.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('table_center_right'), duration=2,
            time_delay=t)
        t += 2
        wilham.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('table_center_left'), duration=2,
            time_delay=t)
        t += 3
        wilham.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_trent_middle'), duration=2,
            time_delay=t)
        t += 3
        wilham.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('table_center_left'), duration=2,
            time_delay=t)
        t += 5
        wilham.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('table_center_right'), duration=2,
            time_delay=t)
        t += 2
        wilham.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_trent_middle_right'),
            duration=1, time_delay=t)
        wilham.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_POINT_RGHT_MILI_000LV_00, duration=3, time_delay=t)
        t += 1
        wilham.motion(group=MAIN, anim=Male.Sc_MLHAND_NEUT_ATEASE_RGHT_000LV_XB_, duration=2.533, trans_time=0.5,
            time_delay=t)
        t += 1
        wilham.move_eye_ik(group=MAIN, target_name=self.get_automarker_name('head_trent_right_far'), duration=1,
            time_delay=t)
        wilham.facial(group=MAIN, index=60, auto_lip=True)
        wilham.facial(group=MAIN, index=70, auto_lip=True)

        # 140: trent.
        # Сочувствую. Но при чем тут я?
        t = 0
        trent.start_eye_ik(group=MAIN, duration=30, time_delay=t)
        cam_trent_near.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_SMALL_000LV_XA_07, duration=0.5, time_delay=t)
        t += 0.5
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_SHRG_SHLDRS_SMALL_000LV_XA_03, duration=3,
            time_scale=0.8, trans_time=0.5, time_delay=t)
        t += 2.5
        cam_wilham_msn3.set(group=MAIN, time_delay=t)
        cam_wilham_msn3.move_cam(group=MAIN, index=2, duration=17, time_delay=t)
        cam_wilham_msn3.move_focus(group=MAIN, index=2, duration=17, time_delay=t)
        trent.facial(group=MAIN, index=80, auto_lip=True)

        # 150: wilham.
        # Вашей задачей будет найти этот корабль и снять с него интересующие нас данные. Сделать это
        # необходимо как можно скорее, так как в данном районе активность так называемых мусорщиков,
        # чрезвычайно высока. Вы должны их опередить.
        t = 1
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_IDLE_000LV_XA_06, duration=3, trans_time=1,
            time_delay=t)
        t += 3.499
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDUP_TRNS_000LV_XA_02, duration=5, trans_time=1,
            time_delay=t)
        t += 0.5
        wilham.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_POINT_RGHT_CASL_000LV_00, duration=4, time_scale=2,
            trans_time=0.25, time_delay=t)
        t += 1
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CONV_RHND_CASL_000LV_XA_04, duration=8, trans_time=1,
            loop=True, time_delay=t)
        t += 3
        wilham.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00, duration=4, time_scale=0.75,
            trans_time=0.25, time_delay=t)
        t += 4
        wilham.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_POINT_RGHT_CASL_000LV_00, duration=4, time_scale=2,
            start_time=3, trans_time=0.5, time_delay=t)
        t += 1
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CONV_RHNDDN_TRNS_000LV_XA_02, duration=3,
            trans_time=0.5, time_delay=t)
        wilham.facial(group=MAIN, index=90, auto_lip=True)
        wilham.facial(group=MAIN, index=100, auto_lip=True)
        wilham.facial(group=MAIN, index=110, auto_lip=True)

        main_group.append_time(0.5)
