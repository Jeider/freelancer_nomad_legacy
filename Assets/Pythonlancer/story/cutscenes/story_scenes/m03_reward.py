"""m03_reward: полная постановка из master; точки в m03_reward.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import (
    Male, Trent,
)
from story import actors


class CharOutcastActor(actors.Actor):
    NAME = 'outcast'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm03_deck_informer'


class M03RewardScene(Scene):
    DUMP_FILE = 'm03_reward'
    SCENE_AMBIENT = [25, 25, 25]

    def action(self):
        main_group = self.get_group(MAIN)

        LT = 99

        Light(root=self, name='lgt1', point_name='lgt1', light_group=LT, diffuse=[0.35, 0.4, 0.36],
            ambient=[0, 0, 0], direction=[0, 0, -1], light_type=L_POINT, range=50)
        Light(root=self, name='lgt2', point_name='lgt2', light_group=LT, diffuse=[0.7, 0.7, 0.7],
            ambient=[0, 0, 0], direction=[0, 0, -1], light_type=L_POINT, range=50)

        # Персонажи, камеры, реквизит и звук.
        trent = Character(root=self, actor=actors.Trent, name='Char_trent', light_group=LT,
            init_point='Char_trent', rotate_from_quat=True, use_ambient=True, appearance='trent',
            actor_name='Player')
        hassler = Character(root=self, actor=actors.Hassler, name='Char_hassler', light_group=LT,
            init_point='Char_hassler', rotate_from_quat=True, use_ambient=True, appearance='hassler',
            actor_name='hassler')
        outcast = Character(root=self, actor=CharOutcastActor, name='Char_outcast', light_group=LT,
            init_point='Char_outcast', rotate_from_quat=True, use_ambient=True, appearance='m03_deck_informer',
            bind_actor=False)
        cam_start = LookAtCamera(root=self, name='cam_start', fov=35, look_duration=300)
        cam_hassler = LookAtCamera(root=self, name='cam_hassler', fov=15, look_duration=300)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=15, look_duration=300)

        # Исходные точки взгляда.

        # Вход.
        t = 0
        cam_start.set(group=MAIN, time_delay=t)
        hassler.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_HNDSUP_TRNS_000LV_XA_00, duration=3,
            time_scale=0.5, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=outcast.name, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04,
            duration=3, time_scale=0.5, loop=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_LOOK_AROU_CASL_000LV_XA_08, duration=10, time_scale=0.8,
            time_delay=t)
        t += 1.5
        hassler.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_HNDS_CASL_000LV_xc_01, duration=2,
            time_scale=0.5, trans_time=1.5, loop=True, time_delay=t)
        t += 1.5
        MotionEvent(root=self, group=MAIN, object_name=outcast.name,
            anim=Male.Sc_MLBODY_STND_SHAKHEAD_NO_SLGHTLY_000LV_XA_02, duration=3, time_scale=0.5, trans_time=1,
            time_delay=t)
        t += 0.5
        hassler.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CONV_HNDSDN_TRNS_000LV_XA_01, duration=3,
            time_scale=0.5, trans_time=1.5, time_delay=t)
        t += 2.5
        hassler.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_NOD_YES_SLGHTLY_000LV_XA_02, duration=3,
            time_scale=0.5, trans_time=1, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=outcast.name,
            anim=Male.Sc_MLBODY_STND_SHRG_SHLDRS_SMALL_000LV_XA_01, duration=5, time_scale=0.5, trans_time=1,
            time_delay=t)
        t += 3
        cam_start.move_cam(group=MAIN, index=2, duration=5, smooth=True, time_delay=t)
        cam_start.move_focus(group=MAIN, index=2, duration=5, smooth=True, time_delay=t)
        hassler.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WALK_TRNS_180LV_XA_02, duration=4, time_scale=0.8,
            trans_time=1, time_delay=t)
        t += 1
        MotionEvent(root=self, group=MAIN, object_name=outcast.name,
            anim=Male.Sc_MLBODY_STND_WALK_TRNS_270LV_XA_02, duration=5, time_scale=0.8, trans_time=1, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=10, time_scale=0.8,
            trans_time=1, time_delay=t)
        t += 2
        EyeIkEvent(root=self, group=MAIN, char_name=hassler.name,
            target_name=self.get_automarker_name('head_trent'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=31, transition_duration=1, time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('head_hassler'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=90, transition_duration=1, time_delay=t)
        t += 0.3
        hassler.motion(group=MAIN, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=4, time_scale=0.8,
            trans_time=0.2, time_delay=t)
        t += 0.2
        MotionEvent(root=self, group=MAIN, object_name=outcast.name, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01,
            duration=33, time_scale=0.8, trans_time=0.02, loop=True, time_delay=t)
        t += 1.5
        cam_hassler.set(group=MAIN, time_delay=t)
        main_group.append_time(15)

        # m03_reward 10: Hassler.
        # Расспросил я местных, нихрена они не знают. В любом случае, спасибо, Трент, твоя работа на этом
        # закончена, будем искать грузовик по нашим каналам. К сожалению, из-за того, что  мы с ним
        # облажались, Райхманн значительно урезал гонорар.
        t = 3
        hassler.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, duration=10, time_scale=0.4,
            trans_time=1, time_delay=t)
        hassler.facial(group=MAIN, index=10, auto_lip=True, extra_delay=0)

        # m03_reward 20: Trent.
        # Странные дела. Базу уничтожили, Дитриха грохнули, а Райхманн выбесился из-за какого-то грузовика. Не
        # нравится мне это.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        t += 3
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, duration=2.5,
            time_scale=0.5, trans_time=0.25, time_delay=t)
        t += 5.25
        trent.motion(group=MAIN, anim=Trent.Sc_MLHEAD_BASEPOSE_TRENT_000LV_01_01, duration=5, trans_time=1,
            time_delay=t)
        trent.facial(group=MAIN, index=20, auto_lip=True, extra_delay=0)

        # m03_reward 30: Hassler.
        # Мне тоже... Деньги уже на твоем счету. До скорого.
        t = 0
        cam_hassler.set(group=MAIN, time_delay=t)
        t += 1
        hassler.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, duration=10, time_scale=0.4,
            trans_time=1, time_delay=t)
        hassler.facial(group=MAIN, index=30, auto_lip=True, extra_delay=0)
        # Действие после исходного окна реплики.
        t = 0
        hassler.motion(group=MAIN, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=4, trans_time=0.5,
            time_delay=t)
        t += 1
        hassler.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WALK_TRNS_090LV_XA_02, duration=10, time_scale=0.8,
            trans_time=1, time_delay=t)
        t += 2.5
        hassler.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=33, time_scale=0.8,
            trans_time=0.02, loop=True, time_delay=t)
        main_group.append_time(4)
