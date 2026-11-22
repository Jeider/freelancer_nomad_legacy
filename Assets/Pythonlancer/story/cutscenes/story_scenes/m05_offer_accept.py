"""m05_offer_accept: полная постановка из master; точки в m05_offer_accept.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character, Female, Light, LookAtCamera, MAIN, Male, MoveEvent, StaticCamera,
)
from story.cutscenes.anim import (
    Female, Male,
)
from story import actors



class M05OfferAcceptScene(Scene):
    DUMP_FILE = 'm05_offer_accept'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Персонажи, камеры, реквизит и звук.
        ambi_ltg00_tbl_rtable4_01 = Light(root=self, name='ambi_LtG00_Tbl_rTable4/01',
            point_name='ambi_LtG00_Tbl_rTable4/01', extra_name='', light_group=5, hidden=False,
            rotate_from_quat=True, diffuse=[1, 1, 1], ambient=[0.141176, 0.141176, 0.141176], direction=[0, 0, 1],
            light_type='L_POINT', range=451, cutoff=180, theta=180, color=[214, 187, 133],
            attenuation=[0.0099999998, 0, 5.1500000954], on=True)
        ambi_ltg00_bar_ovrhd01a = Light(root=self, name='ambi_LtG00_Bar_Ovrhd01A',
            point_name='ambi_LtG00_Bar_Ovrhd01A', extra_name='', light_group=5, hidden=False,
            rotate_from_quat=True, diffuse=[0.596078, 0.572549, 0.403922], ambient=[0.223529, 0.2, 0.192157],
            direction=[0, 0, 1], light_type='L_POINT', range=15, cutoff=18, theta=15, color=[233, 208, 150],
            attenuation=[0.8999999762, 0, 0.0060000001], on=True)
        hatcher = Character(root=self, actor=actors.Hatcher, name='Char_hatcher', light_group=5,
            init_point='Char_hatcher', rotate_from_quat=True, appearance='hatcher', actor_name='Hatcher')
        trent = Character(root=self, actor=actors.Trent, name='Char_trent', light_group=0,
            init_point='Char_trent', rotate_from_quat=True, appearance='trent', actor_name='Player')
        cam_start = StaticCamera(root=self, name='cam_start', fov=25)
        cam_hatcher = LookAtCamera(root=self, name='cam_hatcher', fov=15, look_duration=300)
        cam_trent = StaticCamera(root=self, name='cam_trent', fov=25)
        cam_hatcher_top = StaticCamera(root=self, name='cam_hatcher_top', fov=20)
        cam_trent_top = LookAtCamera(root=self, name='cam_trent_top', fov=22, look_duration=300)
        cam_hatcher_table = StaticCamera(root=self, name='cam_hatcher_table', fov=25)
        cam_table = StaticCamera(root=self, name='cam_table', fov=22)
        cam_hatcher_reward = StaticCamera(root=self, name='cam_hatcher_reward', fov=20)

        # Исходные точки взгляда.

        # Вход.
        t = 0
        cam_trent_top.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=2, time_scale=0.7, loop=True,
            time_delay=t)
        main_group.append_time(0.5)

        # m05_offer 200: Trent.
        # Ок. Как скажете.
        t = 1.5
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_WALK_TRNS_090LV_XA_10, duration=6, trans_time=1,
            time_delay=t)
        trent.facial(group=MAIN, index=200, auto_lip=True, extra_delay=0)
        # Действие после исходного окна реплики.
        t = 1.5
        cam_hatcher.set(group=MAIN, time_delay=t)
        cam_hatcher.move_cam(group=MAIN, index=2, duration=17, smooth=True, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_TWSTS_FROM_270LV_XA_02, duration=3, time_scale=0.6,
            time_delay=t)
        t += 1.1
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 1.9
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_GRABR_HEAD_RLEASE_000LV_XA_03, duration=2,
            time_scale=0.8, trans_time=1, time_delay=t)
        main_group.append_time(5.5)

        # m05_offer 210: Hatcher.
        # Окей, фрилансер, теперь посмотрим чего ты стоишь. Языком молотить научился, посмотрим как научился
        # работать извилинами. А я за тобой присмотрю... Издалека.
        t = 0
        hatcher.motion(group=MAIN, anim=Female.Sc_FMHAND_HNEUT_GESTR_FIST_000LV_00, duration=5, trans_time=0.25,
            time_delay=t)
        t += 1
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_HEAD_HOLDR_000LV_XA_02, duration=4, time_scale=0.8,
            trans_time=1, loop=True, time_delay=t)
        t += 4
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_HOLD_HEAD_RLEASE_000LV_XA_03, duration=3,
            time_scale=0.8, trans_time=1, time_delay=t)
        t += 1
        hatcher.motion(group=MAIN, anim=Female.Sc_FMHAND_NEUT_RGHT_000LV_A_00, duration=5, trans_time=0.25,
            time_delay=t)
        t += 2
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_TWSTS_LOOK_270LV_XA_02, duration=3, time_scale=0.7,
            trans_time=1, time_delay=t)
        hatcher.facial(group=MAIN, index=210, auto_lip=True, extra_delay=0)
        main_group.append_time(1.2)
