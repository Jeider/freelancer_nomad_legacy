"""m03_reward: постановка для ручного редактирования.

Точки: SCENES/m03_reward.blend → DUMPS/m03_reward.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — смещение внутри текущего блока; facial()/append_time() двигают часы.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character,
    EyeIkEvent,
    LookAtCamera,
    MAIN,
    MotionEvent,
    MoveEvent,
)
from story.cutscenes.anim import (
    Male,
    Trent,
)
from story.cutscenes.source_extensions import (
    preserve_entity,
)
from story import actors


class ExtraCharOutcast(actors.Actor):
    NAME = 'outcast'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm03_deck_informer'
    GAME_ACTOR = 'outcast'



class M03RewardScene(Scene):
    DUMP_FILE = 'm03_reward'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=True, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'actor': 'Player', 'category': 'Character'})
        hassler = Character(root=self, actor=actors.Hassler, light_group=0, init_point='Char_hassler',
            rotate_from_quat=True, use_ambient=True, floor_height=0)
        preserve_entity(hassler, template_name='hassler', userprops={'actor': 'hassler', 'category': 'Character'})
        outcast = Character(root=self, actor=ExtraCharOutcast, light_group=0, init_point='Char_outcast',
            rotate_from_quat=True, use_ambient=True, floor_height=0)
        preserve_entity(outcast, template_name='m03_deck_informer', userprops={'category': 'Character'})
        cam_start = LookAtCamera(root=self, name='cam_start', fov=35, farplane=5000, look_duration=300)
        preserve_entity(cam_start)
        cam_hassler = LookAtCamera(root=self, name='cam_hassler', fov=15, farplane=5000, look_duration=300)
        preserve_entity(cam_hassler)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=15, farplane=5000, look_duration=300)
        preserve_entity(cam_trent)

        # Вход / начальная постановка.
        t = 0
        cam_start.set(group=MAIN, time_delay=t)
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_HNDSUP_TRNS_000LV_XA_00, duration=3,
            time_scale=0.5)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_outcast',
            anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=3, time_scale=0.5, loop=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_LOOK_AROU_CASL_000LV_XA_08, duration=10,
            time_scale=0.8)
        t += 1.5
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_HNDS_CASL_000LV_xc_01, duration=2,
            time_scale=0.5, loop=True, trans_time=1.5)
        t += 1.5
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_outcast',
            anim=Male.Sc_MLBODY_STND_SHAKHEAD_NO_SLGHTLY_000LV_XA_02, duration=3, time_scale=0.5, trans_time=1)
        t += 0.5
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CONV_HNDSDN_TRNS_000LV_XA_01, duration=3,
            time_scale=0.5, trans_time=1.5)
        t += 2.5
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_NOD_YES_SLGHTLY_000LV_XA_02, duration=3,
            time_scale=0.5, trans_time=1)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_outcast',
            anim=Male.Sc_MLBODY_STND_SHRG_SHLDRS_SMALL_000LV_XA_01, duration=5, time_scale=0.5, trans_time=1)
        t += 3
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_start', target_name='automarker_cam_start_pos2',
            duration=5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_start_focus',
            target_name='automarker_cam_start_marker_pos2', duration=5, smooth=True)
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WALK_TRNS_180LV_XA_02, duration=4, time_scale=0.8,
            trans_time=1)
        t += 1
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_outcast',
            anim=Male.Sc_MLBODY_STND_WALK_TRNS_270LV_XA_02, duration=5, time_scale=0.8, trans_time=1)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=10, time_scale=0.8,
            trans_time=1)
        t += 2
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_hassler', target_name='automarker_head_trent',
            duration=31, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_head_hassler',
            duration=90, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 0.3
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=4, time_scale=0.8,
            trans_time=0.2)
        t += 0.2
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_outcast', anim=Male.Sc_MLBODY_WLKG_000LV_XA_01,
            duration=33, time_scale=0.8, loop=True, trans_time=0.02)
        t += 1.5
        cam_hassler.set(group=MAIN, time_delay=t)
        main_group.append_time(15)


        # Реплика 10 · hassler · исходное время 15 с
        # Расспросил я местных, нихрена они не знают. В любом случае, спасибо, Трент, твоя работа на этом
        # закончена, будем искать грузовик по нашим каналам.
        # Исходное окно facial: 14 с.
        t = 0
        t += 3
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, duration=10,
            time_scale=0.4, trans_time=1)
        hassler.facial(group=MAIN, index=10, append=True, auto_lip=True, extra_delay=0)
        t = 0


        # Реплика 20 · trent · исходное время 29 с
        # Странные дела. Базу уничтожили, Дитриха грохнули, а Райхманн выбесился из-за какого-то грузовика. Не
        # нравится мне это.
        # Исходное окно facial: 11 с.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        t += 3
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=2.5,
            time_scale=0.5, trans_time=0.25)
        t += 5.25
        trent.motion(group=MAIN, time_delay=t, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, duration=5, trans_time=1)
        trent.facial(group=MAIN, index=20, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-2)


        # Реплика 30 · hassler · исходное время 38 с
        # Мне тоже... Деньги уже на твоем счету. До скорого.
        # Исходное окно facial: 4 с.
        t = 0
        cam_hassler.set(group=MAIN, time_delay=t)
        t += 1
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, duration=10,
            time_scale=0.4, trans_time=1)
        hassler.facial(group=MAIN, index=30, append=True, auto_lip=True, extra_delay=0)
        t = 0
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=4, trans_time=0.5)
        t += 1
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WALK_TRNS_090LV_XA_02, duration=10,
            time_scale=0.8, trans_time=1)
        t += 2.5
        hassler.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=33, time_scale=0.8,
            loop=True, trans_time=0.02)
        main_group.append_time(4.0)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M03RewardScene
