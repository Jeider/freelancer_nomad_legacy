"""m06_offer_accept: полная постановка из master; точки в m06_offer_accept.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character, EyeIkEvent, Female, LookAtCamera, MAIN, Male, MoveEvent, NeckIkEvent, StaticCamera,
)
from story.cutscenes.anim import (
    Female, Male,
)
from story import actors



class M06OfferAcceptScene(Scene):
    DUMP_FILE = 'm06_offer_accept'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Персонажи, камеры, реквизит и звук.
        trent = Character(root=self, actor=actors.Trent, name='Char_trent', light_group=0,
            init_point='Char_trent', rotate_from_quat=True, appearance='trent', actor_name='Player')
        alaric = Character(root=self, actor=actors.Alaric, name='Char_alaric', light_group=0,
            init_point='Char_alaric', rotate_from_quat=True, use_ambient=True, appearance='alaric',
            actor_name='Alaric')
        hatcher = Character(root=self, actor=actors.Hatcher, name='Char_hatcher', light_group=0,
            init_point='Char_hatcher', rotate_from_quat=True, appearance='hatcher', actor_name='Hatcher')
        cam_hatcher = LookAtCamera(root=self, name='cam_hatcher', fov=20, look_duration=300)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=22, look_duration=1)
        cam_friends = StaticCamera(root=self, name='cam_friends', fov=22)
        cam_alaric = StaticCamera(root=self, name='cam_alaric', fov=22)

        # Исходные точки взгляда.

        # Вход.
        t = 0
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=51, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=51, transition_duration=1, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, duration=13, loop=True,
            time_delay=t)
        alaric.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=25, loop=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=25, loop=True, time_delay=t)
        cam_trent.set(group=MAIN, time_delay=t)
        main_group.append_time(1)

        # m06_offer 150: Trent.
        # У меня дежавю. Вот только в прошлый раз меня называли не "мистер Трент", а "герр Трент"... С другой
        # стороны, временами было весело... Хорошо, я в деле.
        t = 1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_alaric_near_far'), duration=2.25, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_alaric_near'), duration=1.25, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 4
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_hatcher'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_hatcher'), duration=1.25, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        trent.facial(group=MAIN, index=150, auto_lip=True, extra_delay=0)

        # m06_offer 160: Hatcher.
        # Тогда встретимся на орбите и продолжим разговор там.
        t = 0
        cam_hatcher.set(group=MAIN, time_delay=t)
        t += 2.5
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_WALK_TRNS_270LV_XA_02, duration=15, time_delay=t)
        hatcher.facial(group=MAIN, index=160, auto_lip=True, extra_delay=0)
