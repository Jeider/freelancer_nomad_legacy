"""m05_offer_accept: постановка для ручного редактирования.

Точки: SCENES/m05_offer_accept.blend → DUMPS/m05_offer_accept.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — смещение внутри текущего блока; facial()/append_time() двигают часы.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character,
    Light,
    LookAtCamera,
    MAIN,
    MoveEvent,
    Sound,
    StaticCamera,
)
from story.cutscenes.anim import (
    Female,
    Male,
)
from story.cutscenes.source_extensions import (
    preserve_entity,
)
from story import actors



class M05OfferAcceptScene(Scene):
    DUMP_FILE = 'm05_offer_accept'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        ambi_LtG00_Tbl_rTable4_01 = Light(root=self, name='ambi_LtG00_Tbl_rTable4/01',
            point_name='ambi_LtG00_Tbl_rTable4/01', extra_name='', light_group=5, diffuse=[1, 1, 1],
            ambient=[0.141176, 0.141176, 0.141176], direction=[0, 0, 1], light_type='L_POINT', on=True, range=451,
            cutoff=180, theta=180, color=[214, 187, 133], attenuation=[0.0099999998, 0, 5.1500000954])
        preserve_entity(ambi_LtG00_Tbl_rTable4_01)
        ambi_LtG00_Bar_Ovrhd01A = Light(root=self, name='ambi_LtG00_Bar_Ovrhd01A', point_name='ambi_LtG00_Bar_Ovrhd01A',
            extra_name='', light_group=5, diffuse=[0.596078, 0.572549, 0.403922], ambient=[0.223529, 0.2, 0.192157],
            direction=[0, 0, 1], light_type='L_POINT', on=True, range=15, cutoff=18, theta=15, color=[233, 208, 150],
            attenuation=[0.8999999762, 0, 0.006])
        preserve_entity(ambi_LtG00_Bar_Ovrhd01A)
        DX_m05_offer_0180_trent = Sound(root=self, name='DX_m05_offer_0180_trent', sound='DX_m05_offer_0180_trent',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m05_offer_0180_trent, userprops={'category': 'Audio'})
        DX_m05_offer_0190_hatcher = Sound(root=self, name='DX_m05_offer_0190_hatcher', sound='DX_m05_offer_0190_hatcher',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m05_offer_0190_hatcher, userprops={'category': 'Audio'})
        hatcher = Character(root=self, actor=actors.Hatcher, light_group=5, init_point='Char_hatcher',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(hatcher, template_name='hatcher', userprops={'actor': 'Hatcher', 'category': 'Character'})
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'Actor': 'Player', 'category': 'Character'})
        cam_start = StaticCamera(root=self, name='cam_start', fov=25, farplane=5000)
        preserve_entity(cam_start)
        cam_hatcher = LookAtCamera(root=self, name='cam_hatcher', fov=15, farplane=5000, look_duration=300)
        preserve_entity(cam_hatcher)
        cam_trent = StaticCamera(root=self, name='cam_trent', fov=25, farplane=5000)
        preserve_entity(cam_trent)
        cam_hatcher_top = StaticCamera(root=self, name='cam_hatcher_top', fov=20, farplane=5000)
        preserve_entity(cam_hatcher_top)
        cam_trent_top = LookAtCamera(root=self, name='cam_trent_top', fov=22, farplane=5000, look_duration=300)
        preserve_entity(cam_trent_top)
        cam_hatcher_table = StaticCamera(root=self, name='cam_hatcher_table', fov=25, farplane=5000)
        preserve_entity(cam_hatcher_table)
        cam_table = StaticCamera(root=self, name='cam_table', fov=22, farplane=5000)
        preserve_entity(cam_table)
        cam_hatcher_reward = StaticCamera(root=self, name='cam_hatcher_reward', fov=20, farplane=5000)
        preserve_entity(cam_hatcher_reward)

        # Вход / начальная постановка.
        t = 0
        cam_trent_top.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=2, time_scale=0.7,
            loop=True)
        main_group.append_time(0.5)


        # Реплика 200 · trent · исходное время 0.5 с
        # Ок. Как скажете.
        # Исходное окно facial: 5 с.
        t = 0
        t += 1.5
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_WALK_TRNS_090LV_XA_10, duration=6, trans_time=1)
        trent.facial(group=MAIN, index=200, append=True, auto_lip=True, extra_delay=0)
        t = 0
        t += 1.5
        cam_hatcher.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_hatcher', target_name='automarker_cam_hatcher_pos2',
            duration=17, smooth=True)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRF_TWSTS_FROM_270LV_XA_02, duration=3,
            time_scale=0.6)
        t += 1.1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', target_name='offscreen', duration=0.001,
            smooth=False)
        t += 1.9
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRF_GRABR_HEAD_RLEASE_000LV_XA_03, duration=2,
            time_scale=0.8, trans_time=1)
        main_group.append_time(5.5)


        # Реплика 210 · hatcher · исходное время 11 с
        # Окей, фрилансер, теперь посмотрим чего ты стоишь. Языком молотить научился, посмотрим как научился
        # работать извилинами. А я за тобой присмотрю... Издалека.
        # Исходное окно facial: 11.8 с.
        t = 0
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHAND_HNEUT_GESTR_FIST_000LV_00, duration=5,
            trans_time=0.25)
        t += 1
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRF_HEAD_HOLDR_000LV_XA_02, duration=4,
            time_scale=0.8, loop=True, trans_time=1)
        t += 4
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRF_HOLD_HEAD_RLEASE_000LV_XA_03, duration=3,
            time_scale=0.8, trans_time=1)
        t += 1
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMHAND_NEUT_RGHT_000LV_A_00, duration=5, trans_time=0.25)
        t += 2
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRF_TWSTS_LOOK_270LV_XA_02, duration=3,
            time_scale=0.7, trans_time=1)
        hatcher.facial(group=MAIN, index=210, append=True, auto_lip=True, extra_delay=0)
        main_group.append_time(1.2)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M05OfferAcceptScene
