"""m04_offer_accept: полная постановка из master; точки в m04_offer_accept.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character, EyeIkEvent, LookAtCamera, MAIN, Male, MoveEvent, NeckIkEvent, SetCameraEvent,
)
from story.cutscenes.anim import (
    Male,
)
from story import actors



class M04OfferAcceptScene(Scene):
    DUMP_FILE = 'm04_offer_accept'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Персонажи, камеры, реквизит и звук.
        trent = Character(root=self, actor=actors.Trent, name='Char_trent', light_group=0,
            init_point='Char_trent', rotate_from_quat=True, appearance='trent', actor_name='Player')
        jacobo = Character(root=self, actor=actors.Jacobo, name='Char_jacobo', light_group=0,
            init_point='Char_jacobo', rotate_from_quat=True, appearance='jacobo', actor_name='jacobo')
        cam_jacobo_sitting = LookAtCamera(root=self, name='cam_jacobo_sitting', fov=16, look_duration=300)
        cam_trent_sitting = LookAtCamera(root=self, name='cam_trent_sitting', fov=16, look_duration=300)

        # Исходные точки взгляда.

        # Вход.
        main_group.append_time(0)

        # m04_offer 70: Trent.
        # Я об этом еще пожалею... Хорошо, каков план?
        t = 0
        SetCameraEvent(root=self, group=MAIN, camera_name='cam_start', time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=2, time_delay=t)
        jacobo.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=3, time_delay=t)
        cam_trent_sitting.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=5, time_delay=t)
        trent.facial(group=MAIN, index=70, auto_lip=True, extra_delay=0)

        # m04_offer 80: Jacobo.
        # Герр Трент, спасибо, вы не пожалеете! Вылетайте в космос, я с помощью друзей попробую незаметно
        # пробраться на взлетную площадку. Встретимся на орбите.
        t = 0
        cam_jacobo_sitting.set(group=MAIN, time_delay=t)
        t += 8
        jacobo.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_STNDCL_TRNS_270LV_XA_06, duration=2.5, trans_time=1,
            time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_jacobo_standing'), duration=0.1, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_jacobo_standing'), duration=0.1, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 2
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_jacobo_standing_go_out'), duration=2, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_jacobo_standing_go_out'), duration=1, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=2, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=2, transition_duration=1, time_delay=t)
        jacobo.facial(group=MAIN, index=80, auto_lip=True, extra_delay=0)

        # m04_offer 90: Trent.
        # Тогда до встречи.
        t = 0
        cam_trent_sitting.set(group=MAIN, time_delay=t)
        t += 1
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_STNDCR_TRNS_090LV_XA_05, duration=5, trans_time=1,
            time_delay=t)
        trent.facial(group=MAIN, index=90, auto_lip=True, extra_delay=0)
        main_group.append_time(1)
