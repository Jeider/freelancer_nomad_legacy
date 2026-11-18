"""Принятие задания Вильгельма: полная сцена master на API Pythonlancer."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    MAIN, Character, LookAtCamera, NeckIkEvent,
    MoveEvent, MoveFastEvent, TARGET_HARDPOINT,
)
from story.cutscenes.anim import Male
from story import actors


class Msn2OfferAcceptScene(Scene):
    DUMP_FILE = 'm02_bship_bar_accept'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Персонажи.
        trent = Character(root=self, actor=actors.Trent, light_group=0,
                          init_point='Char_trent', rotate_from_quat=True)
        wilham = Character(root=self, actor=actors.Wilham, light_group=0,
                          init_point='Char_wilham', rotate_from_quat=True)

        # Камеры и их точки *_focus, *2, *_focus2 в Blender.
        cam_trent_near = LookAtCamera(root=self, name='cam_trent_near', fov=25)
        cam_wilham_near = LookAtCamera(root=self, name='cam_wilham_near', fov=25)
        cam_trent_standing = LookAtCamera(root=self, name='cam_trent_standing', fov=25)
        cam_wilham_stand = LookAtCamera(root=self, name='cam_wilham_stand', fov=22)
        cam_final = LookAtCamera(root=self, name='cam_final', fov=25)

        # Начальная расстановка взглядов.
        trent.move_head_ik(group=MAIN, target_name=self.get_automarker_name('trent_head_ik'), immediately=True)
        wilham.move_head_ik(group=MAIN, target_name=self.get_automarker_name('wilham_head_ik'), immediately=True)

        # Вход.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_SMALL_000LV_XA_07, duration=3, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_SMALL_000LV_XA_07, duration=5, time_delay=t)
        main_group.append_time(0.5)

        # 200: trent.
        # И всего делов-то? Могу приступать?
        trent.facial(group=MAIN, index=120, auto_lip=True)

        # 210: wilham.
        # Если вы согласны, то не "могу", а "можем". В этом задании я буду приписан к вам в качестве
        # напарника.
        t = 0
        cam_wilham_near.set(group=MAIN, time_delay=t)
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=3, time_delay=t)
        t += 2
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_SMALL_000LV_XA_07, duration=3, trans_time=1,
            time_delay=t)
        t += 3
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_STNDCR_TRNS_090LV_XA_05, duration=2.5, trans_time=1,
            time_delay=t)
        t += 1.5
        trent.start_head_ik(group=MAIN, duration=22, time_delay=t)



        wilham.facial(group=MAIN, index=210, auto_lip=True)



        # Действие после реплики.
        t = 0.5
        cam_trent_standing.set(group=MAIN, time_delay=t)
        cam_trent_standing.move_cam(group=MAIN, index=2, duration=3, time_delay=t)
        cam_trent_standing.move_focus(group=MAIN, index=2, duration=4, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_STNDCL_TRNS_270LV_XA_06, duration=5, start_time=1,
            time_delay=t)
        main_group.append_time(1)

        # 220: trent.
        # Будете контролировать мои действия?
        t = 0.5
        trent.move_head_ik(group=MAIN, target_name=self.get_automarker_name('head_wilham_stand_progress'),
            duration=3, time_delay=t)
        t += 1
        MoveFastEvent(root=self, group=MAIN, object_name=wilham.name,
            target_name=self.get_automarker_name('point_wilham_stand'), time_delay=t)
        wilham.start_head_ik(group=MAIN, duration=30, time_delay=t)
        wilham.move_head_ik(group=MAIN, target_name=self.get_automarker_name('head_trent_stand_lower'),
            duration=0.1, time_delay=t)



        trent.facial(group=MAIN, index=220, auto_lip=True)

        # 230: wilham.
        # Нет. Буду осуществлять поддержку и взаимодействие с властями - у меня достаточно высокий допуск в
        # системах Райнланда. Стратегия операции и тактика её проведения целиком на вас, герр Трент.
        t = 0
        wilham.move_head_ik(group=MAIN, target_name=self.get_automarker_name('head_trent_stand'), duration=3,
            time_delay=t)
        cam_wilham_stand.set(group=MAIN, time_delay=t)
        cam_wilham_stand.move_cam(group=MAIN, index=2, duration=11, time_delay=t)
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_GESTL_STOP_000LV_XA_03, duration=5, start_time=0.5,
            time_delay=t)
        t += 3
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, duration=3,
            trans_time=1.5, time_delay=t)
        t += 1
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_RHND_CASL_000LV_xa_01, duration=2, trans_time=1.5,
            loop=True, time_delay=t)
        wilham.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00, duration=4, time_scale=0.75,
            trans_time=0.25, time_delay=t)
        t += 2
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_02, duration=3,
            trans_time=1.5, time_delay=t)
        t += 2.5
        # wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_GESTR_THMBSUP_000LV_XA_02, duration=5, time_scale=0.6,
        #     time_delay=t)



        cam_final.move_cam(group=MAIN, index=2, duration=0.1, time_delay=-1, smooth=False)
        cam_final.move_focus(group=MAIN, index=2, duration=0.1, time_delay=-1, smooth=False)



        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_NOD_YES_EMPH_000LV_XA_01, duration=5, time_delay=t)
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_SMALL_000LV_xa_05, duration=4, time_delay=t)



        wilham.facial(group=MAIN, index=230, auto_lip=True)

        # 240: trent.
        # Спасибо за доверие... где поставить подпись?
        t = 0.5
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_SHRG_SHLDRS_SMALL_000LV_XA_01, duration=5, trans_time=1,
            time_delay=t)

        cam_final.set(group=MAIN, time_delay=0)

        tt = -0.1
        MoveFastEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('point_trent_stand'), time_delay=tt)
        tt += 0.01
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_SMALL_000LV_xa_05, duration=0.5, time_delay=tt)
        tt += 0.01
        trent.move_head_ik(group=MAIN, target_name=self.get_automarker_name('head_wilham_stand'), duration=1,
            time_delay=tt-1)
        trent.start_head_ik(group=MAIN, duration=30, time_delay=tt)


        trent.facial(group=MAIN, index=240, auto_lip=True)

        # 250: wilham.
        # Ха-ха-ха. Ну зачем нам эти условности? Встречаемся в космосе, герр Трент!
        t = 0
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_GESTL_STOP_000LV_XA_03, duration=5, trans_time=1,
            time_delay=t)
        t += 3
        # cam_final.move_cam(group=MAIN, index=3, duration=6, time_delay=t)
        # cam_final.move_focus(group=MAIN, index=3, duration=6, time_delay=t)
        t += 1
        # NeckIkEvent(root=self, group=MAIN, char_name=trent.name, target_name=wilham.name, duration=5,
        #     target_type=TARGET_HARDPOINT, target_part='hp_neck', time_delay=t)
        t += 1


        wilham.facial(group=MAIN, index=250, auto_lip=True)

        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01, duration=5, trans_time=1,
            time_delay=-2)
        wilham.move_head_ik(group=MAIN, target_name=self.get_automarker_name('wilham_outdoor'), duration=4,
            time_delay=-2)

        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=50, trans_time=0.25, loop=True,
            time_delay=-1)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_TURN_270LV_XA_04, duration=10, trans_time=1,
            time_delay=-2)

        trent.move_head_ik(group=MAIN, target_name=self.get_automarker_name('wilham_outdoor'), duration=10,
            time_delay=-1, smooth=True)
        # Действие после реплики.
        main_group.append_time(2)
