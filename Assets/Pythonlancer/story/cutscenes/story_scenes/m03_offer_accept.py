"""m03_offer_accept: полная постановка из master; точки в m03_offer_accept.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character, EyeIkEvent, LookAtCamera, MAIN, Male, MoveEvent, NeckIkEvent, RotateAxisEvent, SoundEvent,
)
from story.cutscenes.anim import (
    Male,
)
from story import actors



class M03OfferAcceptScene(Scene):
    DUMP_FILE = 'm03_offer_accept'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Персонажи, камеры, реквизит и звук.
        trent = Character(root=self, actor=actors.Trent, name='Char_trent', light_group=0,
            init_point='Char_trent', rotate_from_quat=True, appearance='trent', actor_name='Player')
        hassler = Character(root=self, actor=actors.Hassler, name='Char_hassler', light_group=0,
            init_point='Char_hassler', rotate_from_quat=True, appearance='hassler', actor_name='hassler')
        wilham = Character(root=self, actor=actors.Wilham, name='Char_wilham', light_group=0,
            init_point='Char_wilham', rotate_from_quat=True, appearance='wilham', actor_name='wilham')
        cam_trent_near = LookAtCamera(root=self, name='cam_trent_near', fov=15, look_duration=300)
        cam_trent_far = LookAtCamera(root=self, name='cam_trent_far', fov=15, look_duration=300)
        cam_hassler_near = LookAtCamera(root=self, name='cam_hassler_near', fov=15, look_duration=300)
        cam_hassler_far = LookAtCamera(root=self, name='cam_hassler_far', fov=15, look_duration=300)
        cam_wilham_near = LookAtCamera(root=self, name='cam_wilham_near', fov=15, look_duration=300)
        cam_final = LookAtCamera(root=self, name='cam_final', fov=20, look_duration=300)

        # Исходные точки взгляда.

        # Вход.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=wilham.name,
            target_name=self.get_automarker_name('wilham_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=90, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=wilham.name,
            target_name=self.get_automarker_name('wilham_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=90, transition_duration=1, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=hassler.name,
            target_name=self.get_automarker_name('hassler_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=90, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=hassler.name,
            target_name=self.get_automarker_name('hassler_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=90, transition_duration=1, time_delay=t)

        trent_ik1 = NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=73, transition_duration=1, time_delay=t)
        trent_ik2 = EyeIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=73, transition_duration=1, time_delay=t)

        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_LSTN_SMALL_000LV_A_34, duration=35, time_scale=0.5,
            loop=True, time_delay=t)
        hassler.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_LSTN_SMALL_000LV_B_09, duration=16, time_scale=0.5,
            loop=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=4, time_scale=0.5,
            time_delay=t)
        main_group.append_time(1)

        # m03_offer 100: Trent.
        # Весьма польщён. А можно узнать, как так оказалось, что элитная военная база с высшим классом защиты
        # практически в самом центре территории Рейнланда осталась бесхозной и в итоге досталась мятежникам и
        # корсарам?
        t = 3
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, duration=10, time_scale=0.4,
            trans_time=1, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_hassler_trent'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_hassler'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 4
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_wilham_half'), duration=4, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_wilham'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_hassler_trent'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_hassler'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hassler_head_ik'),
            target_name=self.get_automarker_name('head_trent_half'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hassler_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('wilham_head_ik'),
            target_name=self.get_automarker_name('head_hassler_half'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('wilham_eye_ik'),
            target_name=self.get_automarker_name('head_hassler'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        trent.facial(group=MAIN, index=100, auto_lip=True)

        cam_hassler_far.set(group=MAIN, time_delay=0)
        cam_hassler_far.move_cam(group=MAIN, index=2, duration=15, smooth=True, time_delay=0)
        cam_hassler_far.move_focus(group=MAIN, index=2, duration=15, smooth=True, time_delay=0)
        cam_hassler_far.move_cam(group=MAIN, index=3, duration=15, smooth=True, time_delay=15)

        # m03_offer 110: Hassler.
        # Герр Трент, в свое время на территории Рейнланда строились две такие базы - Кёнигсберг и Регенсбург,
        # в системе Мюнхен, на границе с Кусари. Военные Кусари рассматривали Регенсбург не иначе чем шилом у
        # себя в заднице.
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hassler_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 1
        hassler.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_HNDSUP_TRNS_000LV_XA_00, duration=3,
            time_scale=0.5, trans_time=1.5, time_delay=t)
        t += 1.5
        hassler.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_HNDS_CASL_000LV_xc_01, duration=4.5,
            time_scale=0.5, trans_time=1.5, loop=True, time_delay=t)
        t += 4.5
        hassler.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_HNDSDN_TRNS_000LV_XA_01, duration=3,
            time_scale=0.5, trans_time=1.5, time_delay=t)
        t += 3
        hassler.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, duration=5, time_scale=0.6,
            trans_time=1, time_delay=t)
        hassler.facial(group=MAIN, index=110, auto_lip=True)

        # m03_offer 115: Hassler.
        # В ходе последнего военного конфликта с Кусари мы потерпели сокрушительное поражение и по условиям
        # мирного договора нам пришлось не только демилитаризовать систему Мюнхен, но и прекратить
        # строительство почти готовой станции Кёнигсберг...
        t = 1

        t += 10
        t += 0.5
        t += 0.5

        hassler.facial(group=MAIN, index=115, auto_lip=True)



        # m03_offer 120: Hassler.
        # Уничтожить Кёнигсберг или разобрать её так и не дошли руки у нашего правительства, а может,
        # надеялись на пересмотр мирного договора, с тем чтобы достроить ее и ввести в эксплуатацию, не знаю,
        # но в итоге получилось так, что Дитрих, как один из самых высокопоставленных военных, имеющий все
        # ключи доступа, просто-напросто её оккупировал...
        t = 0
        hassler.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, duration=10, time_scale=0.6,
            trans_time=1, time_delay=t)
        cam_hassler_near.move_cam(group=MAIN, index=2, duration=20, smooth=False, time_delay=t)
        t += 8.5
        hassler.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=10,
            time_scale=0.3, trans_time=1, time_delay=t)
        t += 9

        hassler.facial(group=MAIN, index=120, auto_lip=True)

        # m03_offer 130: Trent.
        # Я так понимаю, спрашивать всякие глупости типа, есть ли у меня выбор, в этой ситуации неуместно.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        t += 1.5
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, duration=10, time_scale=0.5,
            trans_time=1, time_delay=t)
        t += 2
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_wilham_half'), duration=4, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_wilham'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 3
        trent.facial(group=MAIN, index=130, auto_lip=True)
        cam_final.set(group=MAIN, time_delay=0)
        cam_final.move_cam(group=MAIN, index=2, duration=20, smooth=True, time_delay=0)
        cam_final.move_focus(group=MAIN, index=2, duration=20, smooth=True, time_delay=0)


        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('wilham_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=-2)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('wilham_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=-1)

        # m03_offer 140: Wilham.
        # : Вы умный человек, герр Трент.
        t = 0
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_GESTR_THMBSUP_000LV_XA_02, duration=25, time_scale=0.8,
            time_delay=t)
        wilham.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_GESTR_THUMB_000LV_00, duration=25, time_scale=0.8,
            time_delay=t)
        wilham.facial(group=MAIN, index=140, auto_lip=True)



        # m03_offer 150: Hassler.
        # Герр Трент, на вашем месте мечтали бы быть девяносто процентов местных фрилансеров. Вам платят
        # отличные деньги, вас курирует адмирал Райхманн лично.
        t = 0

        trent_ik1.set_duration(main_group.get_time())
        trent_ik2.set_duration(main_group.get_time())


        NeckIkEvent(root=self, group=MAIN, char_name=trent.name, target_name=hassler.name, target_type='PART',
            target_part='Body_Neck', up='NEG_Y_AXIS', front='Z_AXIS', duration=90, transition_duration=1,
            time_delay=1)
        EyeIkEvent(root=self, group=MAIN, char_name=trent.name, target_name=hassler.name, target_type='PART',
            target_part='Body_Neck', up='NEG_Y_AXIS', front='Z_AXIS', duration=90, transition_duration=1,
            time_delay=1)



        t += 0.25
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_MED_000LV_xa_05, duration=10, time_scale=0.5,
            trans_time=0.5, loop=True, time_delay=t)
        t += 0.25
        wilham.motion(group=MAIN, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=10, trans_time=0.25,
            time_delay=t)
        t += 6.5
        RotateAxisEvent(root=self, group=MAIN, object_name=wilham.name, angle=-10, axis='Y_AXIS', duration=3,
            smooth=True, time_delay=t)
        t += 2

        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hassler_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=0)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hassler_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=0)

        hassler.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=10,
            time_scale=0.3, trans_time=1, time_delay=1)

        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('wilham_head_ik'),
            target_name=self.get_automarker_name('head_hassler_half'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=0.5)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('wilham_eye_ik'),
            target_name=self.get_automarker_name('head_hassler'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=0.5)

        hassler.facial(group=MAIN, index=150, auto_lip=True)



        hassler.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_TURN_045LV_XA_04, duration=25, trans_time=1,
            time_delay=1)

        # m03_offer 155: Hassler.
        # Что вы капризничаете как старшеклассница на выпускном? Давайте вылетать. Встречаемся в космосе.

        hassler.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01, duration=25, time_scale=0.75,
            trans_time=1, time_delay=t)


        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_TURN_315LV_XA_02, duration=25, time_scale=0.8,
            trans_time=1, time_delay=3)
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=40, axis='Y_AXIS', duration=2,
            smooth=True, time_delay=4)

        hassler.facial(group=MAIN, index=155, auto_lip=True)


        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hassler_head_ik'),
            target_name=self.get_automarker_name('way_out'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=-0)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hassler_eye_ik'),
            target_name=self.get_automarker_name('way_out'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=-0)



        # Действие после исходного окна реплики.
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('wilham_head_ik'),
            target_name=self.get_automarker_name('way_out'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=-2)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('wilham_eye_ik'),
            target_name=self.get_automarker_name('way_out'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=-2)
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01, duration=25, time_scale=0.75,
            trans_time=1, time_delay=t+0.5)
        t += 0.42
        hassler.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=25, time_scale=0.75,
            trans_time=2, loop=True, time_delay=t)
        t += 1
        wilham.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=25, time_scale=0.75,
            trans_time=0.01, loop=True, time_delay=t+0.5)
        main_group.append_time(3)
