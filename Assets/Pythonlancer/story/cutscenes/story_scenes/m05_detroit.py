"""m05_detroit: постановка для ручного редактирования.

Точки: SCENES/m05_detroit.blend → DUMPS/m05_detroit.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — смещение внутри текущего блока; facial()/append_time() двигают часы.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character,
    ConnectHardpointEvent,
    LookAtCamera,
    MAIN,
    MoveEvent,
    NeckIkEvent,
    Prop,
    RotateAxisEvent,
    StaticCamera,
)
from story.cutscenes.anim import (
    Male,
)
from story.cutscenes.source_extensions import (
    SourceAttachEvent,
    preserve_entity,
)
from story import actors


class PropPropBarclothWaddedBart(Prop):
    COMPOUND_TEMPLATE_NAME = 'barcloth_wadded'
    SRT_GRP = 0
    USR_FLG = 0


class PropPropGlassGreen(Prop):
    COMPOUND_TEMPLATE_NAME = 'glass_green'
    SRT_GRP = 0
    USR_FLG = 0


class ExtraCharBartenderFixture(actors.Actor):
    NAME = 'bartender_fixture'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'li_bartender_1'
    GAME_ACTOR = 'bartender'



class M05DetroitScene(Scene):
    DUMP_FILE = 'm05_detroit'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        Prop_barcloth_wadded_Bart = PropPropBarclothWaddedBart(root=self, name='Prop_barcloth_wadded_Bart', light_group=0,
            init_point='Prop_barcloth_wadded_Bart', rotate_from_quat=True, use_ambient=False)
        preserve_entity(Prop_barcloth_wadded_Bart, userprops={'category': 'Prop'})
        Prop_glass_green = PropPropGlassGreen(root=self, name='Prop_glass_green', light_group=0,
            init_point='Prop_glass_green', rotate_from_quat=True, use_ambient=False)
        preserve_entity(Prop_glass_green, userprops={'category': 'Prop'})
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'Actor': 'Player', 'category': 'Character'})
        bartender = Character(root=self, actor=actors.DetroitBarman, light_group=0, init_point='Char_barman',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(bartender, template_name='m05_barman', userprops={'actor': 'm05_barman', 'category': 'Character'})
        bartender_fixture = Character(root=self, actor=ExtraCharBartenderFixture, light_group=0,
            init_point='Char_bartender_fixture', rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(bartender_fixture, template_name='li_bartender_1',
            userprops={'actor': 'bartender', 'category': 'Character'})
        cam_start = LookAtCamera(root=self, name='cam_start', fov=20, farplane=5000, look_duration=300)
        preserve_entity(cam_start)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=22, farplane=5000, look_duration=300)
        preserve_entity(cam_trent)
        cam_trent_near = LookAtCamera(root=self, name='cam_trent_near', fov=20, farplane=5000, look_duration=300)
        preserve_entity(cam_trent_near)
        cam_bartender = LookAtCamera(root=self, name='cam_bartender', fov=25, farplane=5000, look_duration=300)
        preserve_entity(cam_bartender)
        cam_bartender_closest = LookAtCamera(root=self, name='cam_bartender_closest', fov=15, farplane=5000,
            look_duration=300)
        preserve_entity(cam_bartender_closest)
        cam_bartender_near = LookAtCamera(root=self, name='cam_bartender_near', fov=22, farplane=5000, look_duration=300)
        preserve_entity(cam_bartender_near)
        cam_wlkg_trent = StaticCamera(root=self, name='cam_wlkg_trent', fov=15, farplane=5000)
        preserve_entity(cam_wlkg_trent)

        # Вход / начальная постановка.
        t = 0
        cam_start.set(group=MAIN, time_delay=t)
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='Prop_barcloth_wadded_Bart',
            parent_name='Char_barman', duration=512, target_hardpoint='hprightconnect_prop_barcloth_wadded',
            parent_hardpoint='hprightconnect')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_start', target_name='automarker_cam_start_pos2',
            duration=10, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_start_focus',
            target_name='automarker_cam_start_marker_pos2', duration=10, smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=9.99, time_scale=0.9,
            loop=True)
        bartender.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WIPE_BAR_000LV_A_24, duration=25,
            time_scale=0.95)
        t += 3
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=51, transition_duration=2, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 4
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=35, axis='Y_AXIS',
            duration=2.99, smooth=True)
        main_group.append_time(10)


        # Реплика 10 · trent · исходное время 10 с
        # Дружище, я тут одного профессора ищу, по фамилии Мандрейк. Не слышал о таком.
        # Исходное окно facial: 15 с.
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', target_name='automarker_point_trent_stand',
            duration=1, smooth=False)
        cam_bartender.set(group=MAIN, time_delay=t)
        t += 1
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_LEAN_BAR_TRNS_000LV_XA_02, duration=5,
            time_scale=0.7, trans_time=1)
        trent.facial(group=MAIN, index=10, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-9.5)


        # Реплика 20 · barman · исходное время 15.5 с
        # Не видел, не слышал, не разговаривал.
        # Исходное окно facial: 15 с.
        t = 0
        t += 1.5
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_LEAN_STND_BAR_TRNS_000LV_XA_03, duration=3,
            time_scale=0.7, trans_time=1)
        bartender.facial(group=MAIN, index=20, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-10.5)


        # Реплика 30 · trent · исходное время 20 с
        # А ты душка, я смотрю. А взгляни вот на это, дружище, я из профсоюза барменов.
        # Исходное окно facial: 15 с.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        cam_trent.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_GIVE_VEND_000LV_B_07, duration=15, time_scale=0.7)
        trent.facial(group=MAIN, index=30, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-8.5)


        # Реплика 40 · barman · исходное время 26.5 с
        # Чёрт, ты из этих... Светани-ка этой  штукой вон туда в камеру, чтобы я потом смог оправдаться.
        # Исходное окно facial: 17 с.
        t = 0
        cam_bartender_near.set(group=MAIN, time_delay=t)
        bartender.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=2, time_scale=0.2)
        t += 2.0
        bartender.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_GESTL_180LV_XA_02, duration=5, time_scale=0.6,
            trans_time=1)
        t += 4.0
        bartender.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_LOOK_WATC_IMPA_315DN_XA_07, duration=4.2,
            time_scale=0.9, trans_time=1)
        bartender.facial(group=MAIN, index=40, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-8.0)


        # Реплика 45 · barman · исходное время 35.5 с
        # Ага, спасибо. Исследовательская станция в Сигма-17.
        # Исходное окно facial: 15 с.
        t = 0
        t += 1.2
        bartender.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CLEAN_GLAS_000LV_A_26, duration=55,
            time_scale=0.8, trans_time=1)
        bartender.facial(group=MAIN, index=45, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-10.5)


        # Реплика 50 · trent · исходное время 40 с
        # Какая именно станция?
        # Исходное окно facial: 15 с.
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_LEAN_BAR_TRNS_000LV_XA_02, duration=5,
            time_scale=0.7)
        t += 2
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='Prop_glass_green',
            parent_name='Char_barman', duration=50, target_hardpoint='hpleftconnect_prop_glass_green',
            parent_hardpoint='hpleftconnect')
        bartender.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHAND_HNEUT_HOLDD_LEFT_000LV_00, duration=0.1, start_time=5)
        trent.facial(group=MAIN, index=50, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-12)


        # Реплика 60 · barman · исходное время 43 с
        # Ис-сле-до-ва-тель-ска-я. Компренде? Странно, ваши обычно посообразительнее бывают.
        # Исходное окно facial: 20 с.
        t = 0
        cam_bartender_near.set(group=MAIN, time_delay=t)
        bartender.facial(group=MAIN, index=60, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-9)


        # Реплика 70 · trent · исходное время 54 с
        # Ок. Спасибо за инфу. Видишь как легко растопить лед и найти взаимопонимание?
        # Исходное окно facial: 15 с.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_LEAN_STND_BAR_TRNS_000LV_XA_03, duration=5,
            time_scale=0.7, trans_time=1)
        t += 5
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WALK_TRNS_270LV_XA_02, duration=2, trans_time=1)
        t += 2
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent',
            target_name='automarker_point_trent_walkout', duration=0.00011, smooth=False)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['cam_wlkg_trent', 'Char_trent'], duration=15,
            offset=[0.75, 0.6, 2], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='POSITION')
        cam_wlkg_trent.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XC_01, duration=25, time_scale=0.7, loop=True)
        trent.facial(group=MAIN, index=70, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-7)


        # Реплика 80 · trent · исходное время 62 с
        # Вот чего не хватает человечеству - взаимопонимания.
        # Исходное окно facial: 15 с.
        t = 0
        trent.facial(group=MAIN, index=80, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-9.0)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M05DetroitScene
