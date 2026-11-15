"""m07_battleship: постановка для ручного редактирования.

Точки: SCENES/m07_battleship.blend → DUMPS/m07_battleship.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — смещение внутри текущего блока; facial()/append_time() двигают часы.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character,
    EyeIkEvent,
    Light,
    LookAtCamera,
    MAIN,
    MoveEvent,
    MoveFastEvent,
    NeckIkEvent,
    Prop,
    RotateAxisEvent,
    SoundEvent,
)
from story.cutscenes.anim import (
    Female,
    Male,
)
from story.cutscenes.source_extensions import (
    preserve_entity,
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


class PropPropNotebook(Prop):
    COMPOUND_TEMPLATE_NAME = 'notebook'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropTome(Prop):
    COMPOUND_TEMPLATE_NAME = 'tome_075'
    SRT_GRP = 0
    USR_FLG = 0



class M07BattleshipScene(Scene):
    DUMP_FILE = 'm07_battleship'
    SCENE_AMBIENT = [128, 128, 128]

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
        prop_notebook = PropPropNotebook(root=self, name='prop_notebook', light_group=0, init_point='prop_notebook',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(prop_notebook, userprops={'category': 'Prop'})
        prop_tome = PropPropTome(root=self, name='prop_tome', light_group=0, init_point='prop_tome', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(prop_tome, userprops={'category': 'Prop'})
        LIGHT_trent2 = Light(root=self, name='LIGHT_trent2', point_name='LIGHT_trent2', extra_name='', light_group=30,
            diffuse=[0.8, 0.8, 0.8], ambient=[0.1, 0.15, 0.18], direction=[0, 0, -1], light_type='L_DIRECT', on=True,
            range=150555, cutoff=30, theta=26.999985, color=[255, 255, 255], attenuation=[1, 0, 0.003])
        preserve_entity(LIGHT_trent2)
        trent = Character(root=self, actor=actors.Trent, light_group=30, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'Actor': 'Player', 'category': 'Character'})
        bartender = Character(root=self, actor=actors.WalesBarman, light_group=0, init_point='Char_barman',
            rotate_from_quat=True, use_ambient=True, floor_height=0)
        preserve_entity(bartender, template_name='m07_bartender_bship',
            userprops={'Actor': 'Bartender_Battleship', 'category': 'Character'})
        darcy = Character(root=self, actor=actors.Darcy, light_group=0, init_point='Char_darcy', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(darcy, template_name='darcy', userprops={'Actor': 'Darcy', 'category': 'Character'})
        cam_trent_runner = LookAtCamera(root=self, name='cam_trent_runner', fov=15, farplane=5000, look_duration=70)
        preserve_entity(cam_trent_runner)
        cam_bartender = LookAtCamera(root=self, name='cam_bartender', fov=15, farplane=5000, look_duration=70)
        preserve_entity(cam_bartender)
        cam_darcy_intro = LookAtCamera(root=self, name='cam_darcy_intro', fov=25, farplane=5000, look_duration=70)
        preserve_entity(cam_darcy_intro)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=15, farplane=5000, look_duration=70)
        preserve_entity(cam_trent)
        cam_trent_near = LookAtCamera(root=self, name='cam_trent_near', fov=15, farplane=5000, look_duration=70)
        preserve_entity(cam_trent_near)
        cam_darcy = LookAtCamera(root=self, name='cam_darcy', fov=15, farplane=5000, look_duration=710)
        preserve_entity(cam_darcy)
        cam_darcy_artifact = LookAtCamera(root=self, name='cam_darcy_artifact', fov=19, farplane=5000, look_duration=710)
        preserve_entity(cam_darcy_artifact)

        # Вход / начальная постановка.
        t = 0
        cam_trent_runner.set(group=MAIN, time_delay=t)
        bartender.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=0.1)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=-60, axis='Y_AXIS', duration=0,
            smooth=False)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_barman', angle=5, axis='Y_AXIS', duration=0,
            smooth=False)
        MoveFastEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent',
            target_name='automarker_Char_trent_runner')
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_RNNG_STND_TRNS_000LV_XA_07, duration=5, time_scale=0.7,
            start_time=0.3)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=30, axis='Y_AXIS', duration=1,
            smooth=False)
        t += 1
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_barman',
            target_name='automarker_bartender_head_ik', duration=500, transition_duration=1, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_barman', target_name='automarker_bartender_eye_ik',
            duration=500, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        main_group.append_time(2.5)


        # Реплика 10 · trent · исходное время 2.5 с
        # Мне нужна помощь! Дело государственной важности!
        # Исходное окно facial: 0 с.
        t = 0
        voice_sound = self.lookup_single_sound(10)
        SoundEvent(root=self, group=MAIN, sound_name=voice_sound.get_nickname())
        t = 0
        trent.motion(group=MAIN, time_delay=t, anim=Male.GENERIC_ANIM, duration=6, trans_time=0.25)
        main_group.append_time(3.3)


        # Реплика 20 · barman · исходное время 5.8 с
        # Хе... Прям-таки государственной. Тогда вам к представителю государства.
        # Исходное окно facial: 6 с.
        t = 0
        cam_bartender.set(group=MAIN, time_delay=t)
        t += 3.0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_bartender_head_ik',
            target_name='automarker_darcy_sit_point', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_bartender_eye_ik',
            target_name='automarker_darcy_sit_point', duration=1.5, smooth=True)
        t += 1.0
        bartender.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_POINT_LHND_000LV_A_04, duration=15,
            time_scale=0.5, trans_time=1)
        t += 1.0
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_barman', angle=15, axis='Y_AXIS', duration=3,
            smooth=False)
        bartender.facial(group=MAIN, index=20, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(0.0)


        # Реплика 30 · barman · исходное время 11.8 с
        # Вон там у нас офицер Дерси сидит, единственная и неповторимая.
        # Исходное окно facial: 6 с.
        t = 0
        t += 4.2
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_darcy', target_name='automarker_darcy_eye_ik',
            duration=2555, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='prop_notebook', angle=-46, axis='Y_AXIS',
            duration=0, smooth=False)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_darcy', angle=-25, axis='Y_AXIS', duration=0,
            smooth=False)
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRF_HEAD_HOLDR_000LV_XA_02, duration=1)
        t += 0.01
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHAND_HNEUT_GESTR_THUMB_000LV_00, duration=0.1,
            start_time=0.3)
        t += 1.0
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHAND_WALK_TALK_LEFT_CASL_000LV_XB_, duration=7,
            time_scale=0.8, start_time=0.5, loop=True, trans_time=1)
        t += 0.49
        cam_darcy_intro.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_darcy_intro',
            target_name='automarker_cam_darcy_intro_pos2', duration=5.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_darcy_intro_focus',
            target_name='automarker_cam_darcy_intro_marker_pos2', duration=7.5, smooth=True)
        bartender.facial(group=MAIN, index=30, append=True, auto_lip=True, extra_delay=0)
        t = 0
        t += 0.2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent',
            target_name='automarker_point_trent_near_darcy_wlkg', duration=0, smooth=False)
        t += 1.0
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=555, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_eye_ik',
            duration=555, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 1.0001
        MoveFastEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', target_name='automarker_Char_trent')
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=6, time_scale=0.65)
        main_group.append_time(5.5)


        # Реплика 40 · trent · исходное время 23.3 с
        # Меня зовут Трент. Я работаю на секретную организацию, связанную с Орденом и мне срочно нужно с ней
        # связаться.
        # Исходное окно facial: 12 с.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        t += 0.9
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_HOLD_000LV_XA_02, duration=6,
            time_scale=0.65, trans_time=1)
        trent.facial(group=MAIN, index=40, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-6.3)


        # Реплика 50 · darcy · исходное время 29 с
        # Еще один... Эй, мистер, ты у меня уже третий агент Ордена на неделе.
        # Исходное окно facial: 27 с.
        t = 0
        cam_darcy.set(group=MAIN, time_delay=t)
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRF_HOLD_HEAD_RLEASE_000LV_XA_03, duration=7,
            time_scale=0.5, trans_time=1)
        t += 1
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHAND_NEUT_RGHT_000LV_A_00, duration=10, time_scale=0.6,
            trans_time=1)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_darcy', target_name='automarker_darcy_head_ik',
            duration=2555, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_darcy_eye_ik',
            target_name='automarker_head_trent', duration=1, smooth=True)
        darcy.facial(group=MAIN, index=50, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-19)


        # Реплика 60 · darcy · исходное время 37 с
        # УДАЛЕНА ИЗ СЮЖЕТА. Озвучка отключена, движения и камеры оставлены для редактирования.
        # Старый звук: DX_m07_battleship_0060_darcy
        # Исходное окно facial: 28.5 с.
        t = 0
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRF_CONV_RHNDUP_TRNS_000LV_XA_02, duration=2,
            time_scale=0.5, trans_time=1)
        t += 1
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRF_CONV_RHND_CASL_000LV_XA_03, duration=3,
            time_scale=0.4, loop=True, trans_time=1)
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHAND_HNEUT_GESTR_CASL_000LV_00, duration=10, time_scale=0.6)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_darcy_head_ik',
            target_name='automarker_darcy_notebook_view_top', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_darcy_eye_ik',
            target_name='automarker_darcy_notebook_view', duration=1.25, smooth=True)
        t += 3
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRF_CONV_RHNDDN_TRNS_000LV_XA_02, duration=3,
            time_scale=0.5, trans_time=1.5)
        t += 5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_darcy_head_ik',
            target_name='automarker_head_trent', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_darcy_eye_ik',
            target_name='automarker_head_trent', duration=2, smooth=True)
        # darcy.facial(group=MAIN, index=60, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(28.5)  # длительность удалённой реплики
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-19.0)


        # Реплика 70 · darcy · исходное время 46.5 с
        # Сейчас сидят в камере и ждут своей участи. Хочешь составить им компанию?
        # Исходное окно facial: 25 с.
        t = 0
        darcy.facial(group=MAIN, index=70, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-18.0)


        # Реплика 80 · trent · исходное время 53.5 с
        # Я хочу доставить артефакт особой важности в штаб-квартиру нашей организации как можно быстрее.
        # Исходное окно facial: 12 с.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        t += 4.0
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=6,
            time_scale=0.5, trans_time=1)
        trent.facial(group=MAIN, index=80, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-7.0)


        # Реплика 90 · trent · исходное время 58.5 с
        # Иначе с меня шкуру спустят, а потом, возможно, и с вас. Кстати, об артефактах.
        # Исходное окно facial: 12 с.
        t = 0
        t += 2.0
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_GIVE_VEND_000LV_B_07, duration=12, time_scale=0.8,
            trans_time=1)
        t += 1.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='prop_tome',
            target_name='automarker_point_tome_darcy_hand', duration=0, smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_darcy', target_name='automarker_point_darcy_init',
            duration=0, smooth=False)
        t += 0.5
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_darcy', angle=-10, axis='Y_AXIS', duration=0,
            smooth=False)
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_darcy_head_ik',
            target_name='automarker_darcy_tome_view_top_upper', duration=1, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_darcy_eye_ik',
            target_name='automarker_darcy_tome_view', duration=1, smooth=True)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='prop_tome', angle=35, axis='Y_AXIS', duration=0,
            smooth=False)
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_GRABR_PRDRNK_TABL_000LV_XA_09, duration=0,
            time_scale=0.8, start_time=5.3)
        t += 0.2
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='prop_tome', angle=15.5, axis='Z_AXIS', duration=0,
            smooth=False)
        t += 0.1
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHAND_HNEUT_GESTL_THUMB_000LV_00, duration=0.1,
            time_scale=0.6)
        t += 0.3
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHAND_HNEUT_HOLDD_RGHT_000LV_00, duration=0.1, start_time=0.8)
        trent.facial(group=MAIN, index=90, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-5.5)


        # Реплика 100 · darcy · исходное время 65 с
        # О как... Впечатляет.
        # Исходное окно facial: 3 с.
        t = 0
        cam_darcy_artifact.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_darcy_artifact',
            target_name='automarker_cam_darcy_artifact_pos2', duration=11, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_darcy_artifact_focus',
            target_name='automarker_cam_darcy_artifact_marker_pos2', duration=11, smooth=True)
        darcy.facial(group=MAIN, index=100, append=True, auto_lip=True, extra_delay=0)
        t = 0


        # Реплика 110 · darcy · исходное время 68 с
        # А откуда мне знать что эта штука не из какой-нибудь сувенирной лавки для туристов?
        # Исходное окно facial: 25.2 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_darcy_head_ik',
            target_name='automarker_darcy_tome_view_top', duration=2, smooth=True)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_darcy_head_ik',
            target_name='automarker_head_trent', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_darcy_eye_ik',
            target_name='automarker_head_trent', duration=1.25, smooth=True)
        darcy.facial(group=MAIN, index=110, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-17.2)


        # Реплика 120 · trent · исходное время 76 с
        # Черт побери...
        # Исходное окно facial: 12 с.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=10, loop=True)
        trent.facial(group=MAIN, index=120, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-10)


        # Реплика 130 · darcy · исходное время 78 с
        # Ладно, есть у меня знакомый специалист по разным редкостям.
        # Исходное окно facial: 25 с.
        t = 0
        cam_darcy.set(group=MAIN, time_delay=t)
        t += 5.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_darcy_head_ik',
            target_name='automarker_darcy_tome_view_top_upper', duration=1.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_darcy_eye_ik',
            target_name='automarker_darcy_tome_view', duration=1, smooth=True)
        darcy.facial(group=MAIN, index=130, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-19)


        # Реплика 140 · darcy · исходное время 84 с
        # Пусть он взглянет на эту штуку и если ты говоришь правду, то я постараюсь помочь чем смогу.
        # Исходное окно facial: 27 с.
        t = 0
        t += 2.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_darcy_head_ik',
            target_name='automarker_head_trent', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_darcy_eye_ik',
            target_name='automarker_head_trent', duration=1.25, smooth=True)
        darcy.facial(group=MAIN, index=140, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-19.5)


        # Реплика 150 · darcy · исходное время 91.5 с
        # Если же это все-таки сувенир, то отправишь в камеру к тем ребятам из Ордена!
        # Исходное окно facial: 28.5 с.
        t = 0
        darcy.facial(group=MAIN, index=150, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-18.0)


        # Реплика 160 · trent · исходное время 102 с
        # Есть проблема. У меня на корабле сгорела почти вся электроника, даже и не знаю как смог сюда добраться
        # живым.
        # Исходное окно facial: 12 с.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        t += 2
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_HOLD_000LV_XA_02, duration=6,
            time_scale=0.65, trans_time=1)
        t += 4
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='prop_tome', target_name='offscreen', duration=0,
            smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_darcy', target_name='automarker_point_darcy_init',
            duration=0, smooth=False)
        t += 0.1
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_darcy', angle=-25, axis='Y_AXIS', duration=0,
            smooth=False)
        t += 0.1
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, duration=1)
        trent.facial(group=MAIN, index=160, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-5)


        # Реплика 170 · darcy · исходное время 109 с
        # (после долгого молчания и закатывания глаз) Хорошо, я дам вам один из наших кораблей
        # Исходное окно facial: 25 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_darcy_head_ik',
            target_name='automarker_darcy_notebook_view_top', duration=1.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_darcy_eye_ik',
            target_name='automarker_darcy_notebook_view', duration=1, smooth=True)
        cam_darcy.set(group=MAIN, time_delay=t)
        t += 3
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_darcy_head_ik',
            target_name='automarker_head_trent', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_darcy_eye_ik',
            target_name='automarker_head_trent', duration=1.25, smooth=True)
        darcy.facial(group=MAIN, index=170, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-21.5)


        # Реплика 180 · darcy · исходное время 112.5 с
        # (угрожающе) Но если захотите на нем смыться, имейте ввиду, что все наши корабли оборудованы маячками
        # слежения, так что я вас найду где угодно.
        # Исходное окно facial: 30 с.
        t = 0
        t += 4.5
        darcy.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=122,
            time_scale=0.6)
        t += 6.0
        cam_trent.set(group=MAIN, time_delay=t)
        darcy.facial(group=MAIN, index=180, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-19.5)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M07BattleshipScene
