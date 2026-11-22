"""m07_battleship: полная постановка из master; точки в m07_battleship.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character, EyeIkEvent, Female, Light, LookAtCamera, MAIN, Male, MoveEvent, NeckIkEvent, Prop, RotateAxisEvent,
)
from story.cutscenes.anim import (
    Female, Male,
)
from story import actors


class PropCigarette2Prop(Prop):
    COMPOUND_TEMPLATE_NAME = 'cigarette_2'

class PropNotebookProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'notebook'

class PropTomeProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'tome_075'


class M07BattleshipScene(Scene):
    DUMP_FILE = 'm07_battleship'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Персонажи, камеры, реквизит и звук.
        bartender_fixture = Character(root=self, actor=actors.BartenderFixture, name='Char_bartender_Fixture',
            light_group=0, init_point='Char_bartender_Fixture', rotate_from_quat=True,
            appearance='li_bartender_1', actor_name='bartender', floor_height=-110.0)
        prop_cigarette_2 = PropCigarette2Prop(root=self, name='prop_cigarette_2', light_group=0,
            init_point='prop_cigarette_2', rotate_from_quat=True, use_ambient=True)
        prop_notebook = PropNotebookProp(root=self, name='prop_notebook', light_group=0,
            init_point='prop_notebook', rotate_from_quat=True)
        prop_tome = PropTomeProp(root=self, name='prop_tome', light_group=0, init_point='prop_tome',
            rotate_from_quat=True)
        light_trent2 = Light(root=self, name='LIGHT_trent2', point_name='LIGHT_trent2', extra_name='',
            light_group=30, hidden=False, rotate_from_quat=True, diffuse=[0.8, 0.8, 0.8],
            ambient=[0.1, 0.15, 0.18], direction=[0, 0, -1], light_type='L_DIRECT', range=150555, cutoff=30,
            theta=26.999985, color=[255, 255, 255], attenuation=[1, 0, 0.003], on=True)
        trent_runner = Character(root=self, actor=actors.Trent, name='Char_trent_runner', light_group=0,
            init_point='Char_trent_runner', rotate_from_quat=True, appearance='trent', actor_name='Player2')
        trent = Character(root=self, actor=actors.Trent, name='Char_trent', light_group=30,
            init_point='Char_trent', rotate_from_quat=True, appearance='trent', actor_name='Player')
        bartender = Character(root=self, actor=actors.WalesBarman, name='Char_bartender', light_group=0,
            init_point='Char_bartender', rotate_from_quat=True, use_ambient=True,
            appearance='m07_bartender_bship', actor_name='Bartender_Battleship')
        darcy = Character(root=self, actor=actors.Darcy, name='Char_darcy', light_group=0,
            init_point='Char_darcy', rotate_from_quat=True, appearance='darcy', actor_name='Darcy')
        cam_trent_runner = LookAtCamera(root=self, name='cam_trent_runner', fov=15, look_duration=70)
        cam_bartender = LookAtCamera(root=self, name='cam_bartender', fov=15, look_duration=70)
        cam_darcy_intro = LookAtCamera(root=self, name='cam_darcy_intro', fov=25, look_duration=70)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=15, look_duration=70)
        cam_trent_near = LookAtCamera(root=self, name='cam_trent_near', fov=15, look_duration=70)
        cam_darcy = LookAtCamera(root=self, name='cam_darcy', fov=15, look_duration=710)
        cam_darcy_artifact = LookAtCamera(root=self, name='cam_darcy_artifact', fov=19, look_duration=710)

        # Исходные точки взгляда.

        # Вход.
        t = 0
        cam_trent_runner.set(group=MAIN, time_delay=t)
        bartender.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=0.1, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=trent_runner.name, angle=-60, axis='Y_AXIS',
            duration=0, smooth=False, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=bartender.name, angle=5, axis='Y_AXIS', duration=0,
            smooth=False, time_delay=t)
        trent_runner.motion(group=MAIN, anim=Male.Sc_MLBODY_RNNG_STND_TRNS_000LV_XA_07, duration=5,
            time_scale=0.7, start_time=0.3, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=trent_runner.name, angle=30, axis='Y_AXIS', duration=1,
            smooth=False, time_delay=t)
        t += 1
        NeckIkEvent(root=self, group=MAIN, char_name=bartender.name,
            target_name=self.get_automarker_name('bartender_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=500, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=bartender.name,
            target_name=self.get_automarker_name('bartender_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=500, transition_duration=1, time_delay=t)
        main_group.append_time(2.5)

        # m07_battleship 10: Trent.
        # Мне нужна помощь! Дело государственной важности!
        trent_runner.facial(group=MAIN, index=10, auto_lip=True, extra_delay=0)

        # m07_battleship 20: WalesBarman.
        # Хе... Прям-таки государственной. Тогда вам к представителю государства.
        t = 0
        cam_bartender.set(group=MAIN, time_delay=t)
        t += 3
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('bartender_head_ik'),
            target_name=self.get_automarker_name('darcy_sit_point'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('bartender_eye_ik'),
            target_name=self.get_automarker_name('darcy_sit_point'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 1
        bartender.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_POINT_LHND_000LV_A_04, duration=15, time_scale=0.5,
            trans_time=1, time_delay=t)
        t += 1
        RotateAxisEvent(root=self, group=MAIN, object_name=bartender.name, angle=15, axis='Y_AXIS', duration=3,
            smooth=False, time_delay=t)
        bartender.facial(group=MAIN, index=20, auto_lip=True, extra_delay=0)

        # m07_battleship 30: WalesBarman.
        # Вон там у нас офицер Дерси сидит, единственная и неповторимая.
        t = 4.2
        EyeIkEvent(root=self, group=MAIN, char_name=darcy.name,
            target_name=self.get_automarker_name('darcy_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=2555, transition_duration=1, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=prop_notebook.name, angle=-46, axis='Y_AXIS',
            duration=0, smooth=False, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=darcy.name, angle=-25, axis='Y_AXIS', duration=0,
            smooth=False, time_delay=t)
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_HEAD_HOLDR_000LV_XA_02, duration=1, time_delay=t)
        t += 0.01
        darcy.motion(group=MAIN, anim=Female.Sc_FMHAND_HNEUT_GESTR_THUMB_000LV_00, duration=0.1, start_time=0.3,
            time_delay=t)
        t += 1
        darcy.motion(group=MAIN, anim=Female.Sc_FMHAND_WALK_TALK_LEFT_CASL_000LV_XB_, duration=7, time_scale=0.8,
            start_time=0.5, trans_time=1, loop=True, time_delay=t)
        t += 0.49
        cam_darcy_intro.set(group=MAIN, time_delay=t)
        cam_darcy_intro.move_cam(group=MAIN, index=2, duration=5.5, smooth=True, time_delay=t)
        cam_darcy_intro.move_focus(group=MAIN, index=2, duration=7.5, smooth=True, time_delay=t)
        bartender.facial(group=MAIN, index=30, auto_lip=True, extra_delay=0)
        # Действие после исходного окна реплики.
        t = 0.2
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('point_trent_near_darcy_wlkg'), duration=0, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 1
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=555, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=555, transition_duration=1, time_delay=t)
        t += 1.0001
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=6, time_scale=0.65,
            time_delay=t)
        main_group.append_time(5.5)

        # m07_battleship 40: Trent.
        # Меня зовут Трент. Я работаю на секретную организацию, связанную с Орденом и мне срочно нужно с ней
        # связаться.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        t += 0.9
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_HOLD_000LV_XA_02, duration=6, time_scale=0.65,
            trans_time=1, time_delay=t)
        trent.facial(group=MAIN, index=40, auto_lip=True, extra_delay=0)

        # m07_battleship 50: Darcy.
        # Еще один... Мистер, а вы в курсе, что торговля артефактами инопланетного происхождения является
        # незаконной?
        t = 0
        cam_darcy.set(group=MAIN, time_delay=t)
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_HOLD_HEAD_RLEASE_000LV_XA_03, duration=7,
            time_scale=0.5, trans_time=1, time_delay=t)
        t += 1
        darcy.motion(group=MAIN, anim=Female.Sc_FMHAND_NEUT_RGHT_000LV_A_00, duration=10, time_scale=0.6,
            trans_time=1, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=darcy.name,
            target_name=self.get_automarker_name('darcy_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=2555, transition_duration=1, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('darcy_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        darcy.facial(group=MAIN, index=50, auto_lip=True, extra_delay=0)

        # m07_battleship 60: Darcy.
        # Мы недавно взяли парочку вот таких вот продавцов. Когда сажали их в камеру, они тоже уверяли что
        # являются агентами Ордена.
        t = 0
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_CONV_RHNDUP_TRNS_000LV_XA_02, duration=2,
            time_scale=0.5, trans_time=1, time_delay=t)
        t += 1
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_CONV_RHND_CASL_000LV_XA_03, duration=3,
            time_scale=0.4, trans_time=1, loop=True, time_delay=t)
        darcy.motion(group=MAIN, anim=Female.Sc_FMHAND_HNEUT_GESTR_CASL_000LV_00, duration=10, time_scale=0.6,
            time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('darcy_head_ik'),
            target_name=self.get_automarker_name('darcy_notebook_view_top'), duration=2, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('darcy_eye_ik'),
            target_name=self.get_automarker_name('darcy_notebook_view'), duration=1.25, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 3
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_CONV_RHNDDN_TRNS_000LV_XA_02, duration=3,
            time_scale=0.5, trans_time=1.5, time_delay=t)
        t += 5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('darcy_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('darcy_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        darcy.facial(group=MAIN, index=60, auto_lip=True, extra_delay=0)

        # m07_battleship 70: Darcy.
        # Не хотите ли составить им компанию или, быть может, их другу герцогу Веллингтону в психушке?
        darcy.facial(group=MAIN, index=70, auto_lip=True, extra_delay=0)

        # m07_battleship 80: Trent.
        # Я хочу доставить артефакт особой важности в штаб-квартиру нашей организации как можно быстрее.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        t += 4
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=6, time_scale=0.5,
            trans_time=1, time_delay=t)
        trent.facial(group=MAIN, index=80, auto_lip=True, extra_delay=0)

        # m07_battleship 90: Trent.
        # Иначе с меня шкуру спустят, а потом, возможно, и с вас. Кстати, об артефактах.
        t = 2
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_GIVE_VEND_000LV_B_07, duration=12, time_scale=0.8,
            trans_time=1, time_delay=t)
        t += 1.5
        MoveEvent(root=self, group=MAIN, object_name=prop_tome.name,
            target_name=self.get_automarker_name('point_tome_darcy_hand'), duration=0, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=darcy.name,
            target_name=self.get_automarker_name('point_darcy_init'), duration=0, smooth=False, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 0.5
        RotateAxisEvent(root=self, group=MAIN, object_name=darcy.name, angle=-10, axis='Y_AXIS', duration=0,
            smooth=False, time_delay=t)
        t += 0.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('darcy_head_ik'),
            target_name=self.get_automarker_name('darcy_tome_view_top_upper'), duration=1, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('darcy_eye_ik'),
            target_name=self.get_automarker_name('darcy_tome_view'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=prop_tome.name, angle=35, axis='Y_AXIS', duration=0,
            smooth=False, time_delay=t)
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_GRABR_PRDRNK_TABL_000LV_XA_09, duration=0,
            time_scale=0.8, start_time=5.3, time_delay=t)
        t += 0.2
        RotateAxisEvent(root=self, group=MAIN, object_name=prop_tome.name, angle=15.5, axis='Z_AXIS', duration=0,
            smooth=False, time_delay=t)
        t += 0.1
        darcy.motion(group=MAIN, anim=Female.Sc_FMHAND_HNEUT_GESTL_THUMB_000LV_00, duration=0.1, time_scale=0.6,
            time_delay=t)
        t += 0.3
        darcy.motion(group=MAIN, anim=Female.Sc_FMHAND_HNEUT_HOLDD_RGHT_000LV_00, duration=0.1, start_time=0.8,
            time_delay=t)
        trent.facial(group=MAIN, index=90, auto_lip=True, extra_delay=0)

        # m07_battleship 100: Darcy.
        # О как... Впечатляет.
        t = 0
        cam_darcy_artifact.set(group=MAIN, time_delay=t)
        cam_darcy_artifact.move_cam(group=MAIN, index=2, duration=11, smooth=True, time_delay=t)
        cam_darcy_artifact.move_focus(group=MAIN, index=2, duration=11, smooth=True, time_delay=t)
        darcy.facial(group=MAIN, index=100, auto_lip=True, extra_delay=0)

        # m07_battleship 110: Darcy.
        # А откуда мне знать что эта штука не из какой-нибудь сувенирной лавки для туристов?
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('darcy_head_ik'),
            target_name=self.get_automarker_name('darcy_tome_view_top'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 2
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('darcy_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('darcy_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.25, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        darcy.facial(group=MAIN, index=110, auto_lip=True, extra_delay=0)

        # m07_battleship 120: Trent.
        # Черт побери...
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=10, loop=True, time_delay=t)
        trent.facial(group=MAIN, index=120, auto_lip=True, extra_delay=0)

        # m07_battleship 130: Darcy.
        # Ладно, есть у меня знакомый специалист по разным редкостям на соседней станции.
        t = 0
        cam_darcy.set(group=MAIN, time_delay=t)
        t += 5.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('darcy_head_ik'),
            target_name=self.get_automarker_name('darcy_tome_view_top_upper'), duration=1.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('darcy_eye_ik'),
            target_name=self.get_automarker_name('darcy_tome_view'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        darcy.facial(group=MAIN, index=130, auto_lip=True, extra_delay=0)

        # m07_battleship 140: Darcy.
        # Пусть он взглянет на эту штуку и если вы правы, то я обещаю вам всяческую поддержку.
        t = 2.5
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('darcy_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('darcy_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.25, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        darcy.facial(group=MAIN, index=140, auto_lip=True, extra_delay=0)

        # m07_battleship 150: Darcy.
        # Если же это все-таки сувенир, то у вас, мистер шутник, сегодня вечером будет назначено чаепитие с
        # тем самым герцогом Веллингтоном в психушке!
        darcy.facial(group=MAIN, index=150, auto_lip=True, extra_delay=0)

        # m07_battleship 160: Trent.
        # Есть проблема. У меня на корабле сгорела почти вся электроника, даже и не знаю как смог сюда
        # добраться живым.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        t += 2
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_HOLD_000LV_XA_02, duration=6, time_scale=0.65,
            trans_time=1, time_delay=t)
        t += 4
        MoveEvent(root=self, group=MAIN, object_name=prop_tome.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=darcy.name,
            target_name=self.get_automarker_name('point_darcy_init'), duration=0, smooth=False, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        t += 0.1
        RotateAxisEvent(root=self, group=MAIN, object_name=darcy.name, angle=-25, axis='Y_AXIS', duration=0,
            smooth=False, time_delay=t)
        t += 0.1
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, duration=1, time_delay=t)
        trent.facial(group=MAIN, index=160, auto_lip=True, extra_delay=0)

        # m07_battleship 170: Darcy.
        # Хорошо, я дам вам один из наших кораблей.
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('darcy_head_ik'),
            target_name=self.get_automarker_name('darcy_notebook_view_top'), duration=1.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('darcy_eye_ik'),
            target_name=self.get_automarker_name('darcy_notebook_view'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        cam_darcy.set(group=MAIN, time_delay=t)
        t += 3
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('darcy_head_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('darcy_eye_ik'),
            target_name=self.get_automarker_name('head_trent'), duration=1.25, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        darcy.facial(group=MAIN, index=170, auto_lip=True, extra_delay=0)

        # m07_battleship 180: Darcy.
        # Но если захотите на нем смыться, имейте ввиду, что все наши корабли оборудованы маячками слежения,
        # так что я вас найду где угодно.
        t = 4.5
        darcy.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=122, time_scale=0.6,
            time_delay=t)
        t += 6
        cam_trent.set(group=MAIN, time_delay=t)
        darcy.facial(group=MAIN, index=180, auto_lip=True, extra_delay=0)
