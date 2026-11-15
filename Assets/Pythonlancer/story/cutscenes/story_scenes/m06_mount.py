"""m06_mount: постановка для ручного редактирования.

Точки: SCENES/m06_mount.blend → DUMPS/m06_mount.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — смещение внутри текущего блока; facial()/append_time() двигают часы.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character,
    LookAtCamera,
    MAIN,
    MoveEvent,
    NeckIkEvent,
    RotateAxisEvent,
)
from story.cutscenes.anim import (
    Male,
)
from story.cutscenes.source_extensions import (
    preserve_entity,
)
from story import actors



class M06MountScene(Scene):
    DUMP_FILE = 'm06_mount'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'Actor': 'Player', 'category': 'Character'})
        alaric = Character(root=self, actor=actors.Alaric, light_group=0, init_point='Char_alaric', rotate_from_quat=True,
            use_ambient=True, floor_height=0)
        preserve_entity(alaric, template_name='alaric', userprops={'actor': 'Alaric', 'category': 'Character'})
        cam_start = LookAtCamera(root=self, name='cam_start', fov=20, farplane=5000, look_duration=30)
        preserve_entity(cam_start)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=20, farplane=5000, look_duration=1)
        preserve_entity(cam_trent)
        cam_alaric = LookAtCamera(root=self, name='cam_alaric', fov=20, farplane=5000, look_duration=1)
        preserve_entity(cam_alaric)
        cam_final = LookAtCamera(root=self, name='cam_final', fov=26, farplane=5000, look_duration=111)
        preserve_entity(cam_final)

        # Вход / начальная постановка.
        t = 0
        cam_start.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_start', target_name='automarker_cam_start_pos2',
            duration=8, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_start_focus',
            target_name='automarker_cam_start_marker_pos2', duration=8, smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=6, time_scale=0.75,
            start_time=0.73, loop=True)
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=8.5, time_scale=0.75,
            loop=True)
        main_group.append_time(2)


        # Реплика 10 · trent · исходное время 2 с
        # У тебя редкий талант постоянно влипать в неприятности, Аларик.
        # Исходное окно facial: 15 с.
        t = 0
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=25, transition_duration=2, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        trent.facial(group=MAIN, index=10, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-11)


        # Реплика 20 · alaric · исходное время 6 с
        # Ты о чем?
        # Исходное окно facial: 12 с.
        t = 0
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=4, time_scale=0.75,
            trans_time=0.1)
        alaric.facial(group=MAIN, index=20, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-11)


        # Реплика 30 · trent · исходное время 7 с
        # О том что с нами будет происходить в ближайшем будущем.
        # Исходное окно facial: 15 с.
        t = 0
        t += 1
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=-10, axis='Y_AXIS', duration=1,
            smooth=True)
        t += 0.5
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_TURN_270LV_XA_04, duration=5)
        t += 0.5
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_alaric', target_name='Char_trent', duration=25,
            transition_duration=2, target_type='PART', target_part='Body_Head', up='NEG_Y_AXIS', front='Z_AXIS')
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_alaric', angle=35, axis='Y_AXIS', duration=1,
            smooth=True)
        trent.facial(group=MAIN, index=30, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-11.5)


        # Реплика 40 · alaric · исходное время 10.5 с
        # Ты про нашу миссию?
        # Исходное окно facial: 12 с.
        t = 0
        cam_alaric.set(group=MAIN, time_delay=t)
        alaric.facial(group=MAIN, index=40, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-9.5)


        # Реплика 50 · trent · исходное время 13 с
        # Про нашу СУИЦИДАЛЬНУЮ миссию.
        # Исходное окно facial: 15 с.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=50, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-12)


        # Реплика 60 · alaric · исходное время 16 с
        # Зато какие выгоды в случае успеха! К тому же ты мог бы отказаться.
        # Исходное окно facial: 12 с.
        t = 0
        cam_alaric.set(group=MAIN, time_delay=t)
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_GESTR_THMBSUP_000LV_XA_02, duration=6,
            time_scale=0.6)
        t += 2.5
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_GEST_HNDS_WAIT_000LV_XA_02, duration=6,
            time_scale=0.8, trans_time=0.5)
        alaric.facial(group=MAIN, index=60, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-6.7)


        # Реплика 70 · trent · исходное время 21.3 с
        # Боюсь, если бы я отказался, то уже летал бы в космосе без скафандра.
        # Исходное окно facial: 15 с.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=6,
            time_scale=0.6)
        trent.facial(group=MAIN, index=70, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-10.8)


        # Реплика 80 · alaric · исходное время 25.5 с
        # Трент, раз уж мы подписались, надо выполнять. Давай, Трент, полетели. Обещаю, в следующий раз заказчика
        # будешь выбирать ты.
        # Исходное окно facial: 16 с.
        t = 0
        cam_alaric.set(group=MAIN, time_delay=t)
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_HOLD_HEAD_RLEASE_000LV_XA_01, duration=6,
            time_scale=0.8, start_time=0.4)
        t += 2.0
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=6,
            time_scale=0.8)
        t += 4.0
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=6,
            time_scale=0.8)
        t += 1.7
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=2, trans_time=1.5)
        alaric.facial(group=MAIN, index=80, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-7.5)


        # Реплика 90 · trent · исходное время 34 с
        # Если он будет, этот следующий раз.
        # Исходное окно facial: 15 с.
        t = 0
        cam_final.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, duration=6,
            time_scale=0.8)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_final', target_name='automarker_cam_final_pos2',
            duration=6, smooth=True)
        t += 1
        alaric.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WALK_TRNS_180LV_XA_02, duration=5, time_scale=0.8,
            trans_time=1)
        t += 1
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_WALK_TRNS_270LV_XA_02, duration=5, time_scale=0.8,
            trans_time=1)
        trent.facial(group=MAIN, index=90, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-9.0)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M06MountScene
