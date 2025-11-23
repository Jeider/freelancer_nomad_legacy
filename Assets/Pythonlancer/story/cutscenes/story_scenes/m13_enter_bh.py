from story.cutscenes.scene import Scene
from story.cutscenes.content import *


class SceneBackground(BackgroundProp):
    COMPOUND_TEMPLATE_NAME = 'rtc_asf_prom_toroid_bh'


class Msn13EnterBlackholeScene(Scene):
    POINT_ROTATE_OVERRIDES = {}

    def action(self):
        main_group = self.get_group(MAIN)


        jump_sound = Sound(root=self, name='jump_snd', sound='tl_wind_int_bh', attenuation=-25)
        jump_sound.start(group=BG, duration=30, loop=True)


        cam_dbg = LookAtCamera(root=self, name='cam_dbg', fov=40)

        sh_lt = Light(root=self, name='test_ambi', point_name=self.DEFAULT_POINT_NAME,
                      light_group=0, diffuse=[0, 0, 0],
                      ambient=[1, 1, 0.2], direction=[0, 0, 1], light_type=L_DIRECT, range=2000)

        sh_lt.set_ambient(BG, duration=2, ambient=[0, 1, 0.8], smooth=True, time_delay=2)
        sh_lt.set_ambient(BG, duration=2, ambient=[0, 1, 1], smooth=True, time_delay=4)
        sh_lt.set_ambient(BG, duration=2, ambient=[0, 1, 0.8], smooth=True, time_delay=6)
        sh_lt.set_ambient(BG, duration=2, ambient=[1, 1, 0.4], smooth=True, time_delay=8)
        sh_lt.set_ambient(BG, duration=2, ambient=[0, 1, 0], smooth=True, time_delay=10)
        sh_lt.set_ambient(BG, duration=2, ambient=[0, 1, 1], smooth=True, time_delay=12)


        Light(root=self, name='test_ambi2', point_name=self.DEFAULT_POINT_NAME,
              light_group=5, diffuse=[0, 0, 0],
              ambient=[0, 1, 0], direction=[0, 0, -1], light_type=L_DIRECT, range=2000)

        bg = SceneBackground(root=self, name='scene_bg1', light_group=8, init_point=self.DEFAULT_POINT_NAME, rotate_y=-90)

        playership = PlayerShip(root=self, name='playership_the', light_group=0, init_point='ship', rotate_from_quat=True)
        # playership.anim(group=MAIN, anim='Sc_extend wing', duration=2, time_delay=0)  # didnt work

        stars_fx = Alchemy(root=self, name='stars_fx', particles='jumpbeam_walker', point_name='ship')
        stars_fx2 = Alchemy(root=self, name='stars_fx2', particles='jumpbeam_green', point_name='ship')
        stars_fx3 = Alchemy(root=self, name='stars_fx3', particles='jumpbeam_barrier', point_name='ship')
        stars_fx4 = Alchemy(root=self, name='stars_fx4', particles='jumpgate_stars', point_name='ship')

        stars_Afx = Alchemy(root=self, name='stars_Afx', particles='jumpbeam_walker', point_name='ship')
        stars_Afx2 = Alchemy(root=self, name='stars_Afx2', particles='jumpbeam_green', point_name='ship')
        stars_Afx3 = Alchemy(root=self, name='stars_Afx3', particles='jumpbeam_barrier', point_name='ship')
        stars_Afx4 = Alchemy(root=self, name='stars_Afx4', particles='jumpgate_stars', point_name='ship')


        group_bg_move = 'bg_move'
        group_bg_move2 = 'bg_move2'
        group_bg_move3 = 'bg_move3'
        group_bg_move4 = 'bg_move4'
        group_bg_move5 = 'bg_move5'
        self.add_group(group_bg_move, group_type=BG_GROUP)
        self.add_group(group_bg_move2, group_type=BG_GROUP)
        self.add_group(group_bg_move3, group_type=BG_GROUP)
        self.add_group(group_bg_move4, group_type=BG_GROUP)
        self.add_group(group_bg_move5, group_type=BG_GROUP)


        group_fx = 'bg_move_fx'
        self.add_group(group_fx, group_type=BG_GROUP)

        RotateAxisEvent(root=self, group=group_bg_move, object_name=stars_fx.name, angle=-10, duration=5, smooth=True)
        RotateAxisEvent(root=self, group=group_bg_move, object_name=stars_fx.name, angle=12, duration=5, smooth=True,
                        time_delay=5)
        RotateAxisEvent(root=self, group=group_bg_move, object_name=stars_fx.name, angle=-2, duration=5, smooth=True,
                        time_delay=10)

        RotateAxisEvent(root=self, group=group_bg_move2, object_name=stars_fx2.name, angle=-10, duration=5, smooth=True)
        RotateAxisEvent(root=self, group=group_bg_move2, object_name=stars_fx2.name, angle=12, duration=5, smooth=True,
                        time_delay=5)
        RotateAxisEvent(root=self, group=group_bg_move2, object_name=stars_fx2.name, angle=-2, duration=5, smooth=True,
                        time_delay=10)

        RotateAxisEvent(root=self, group=group_bg_move3, object_name=stars_fx3.name, angle=-10, duration=5, smooth=True)
        RotateAxisEvent(root=self, group=group_bg_move3, object_name=stars_fx3.name, angle=12, duration=5, smooth=True,
                        time_delay=5)
        RotateAxisEvent(root=self, group=group_bg_move3, object_name=stars_fx3.name, angle=-2, duration=5, smooth=True,
                        time_delay=10)

        RotateAxisEvent(root=self, group=group_bg_move4, object_name=bg.name, angle=-10, duration=5, smooth=True)
        RotateAxisEvent(root=self, group=group_bg_move4, object_name=bg.name, angle=12, duration=5, smooth=True,
                        time_delay=5)
        RotateAxisEvent(root=self, group=group_bg_move4, object_name=bg.name, angle=-2, duration=5, smooth=True,
                        time_delay=10)

        RotateAxisEvent(root=self, group=group_bg_move5, object_name=stars_fx4.name, angle=-10, duration=5, smooth=True)
        RotateAxisEvent(root=self, group=group_bg_move5, object_name=stars_fx4.name, angle=12, duration=5, smooth=True,
                        time_delay=5)
        RotateAxisEvent(root=self, group=group_bg_move5, object_name=stars_fx4.name, angle=-2, duration=5, smooth=True,
                        time_delay=10)


        neg_fx = Alchemy(root=self, name='fadenegative_variable_1', particles=FX_FADE_NEGATIVE, point_name=self.OFFSCREEN_POINT_NAME,
                         sparam=0)


        AttachEvent(root=self, group=BG, duration=5000, target_name=neg_fx.name, parent_name=cam_dbg.name,
                    target_part='', target_type=TARGET_ROOT, adjust_orient=True, entity_relative=True,
                    offset_z=-0.3)


        group_bg_neg = 'bg_neg'
        self.add_group(group_bg_neg, group_type=BG_GROUP)

        neg_fx.start(group=group_bg_neg, duration=5000)
        jump_sound.change_attenuation(group=group_bg_neg, attenuation=0, duration=5)
        neg_fx.set_sparam(group=group_bg_neg, duration=5, sparam=0.9, time_delay=0)
        neg_fx.set_sparam(group=group_bg_neg, duration=5, sparam=0, time_delay=20)
        jump_sound.change_attenuation(group=group_bg_neg, attenuation=-10, time_delay=18, duration=5)


        stars_fx.start(group=group_fx, duration=5000, time_delay=1)
        stars_fx2.start(group=group_fx, duration=5000, time_delay=3)
        stars_fx3.start(group=group_fx, duration=5000, time_delay=6)
        stars_fx4.start(group=group_fx, duration=5000, time_delay=9)

        stars_Afx.start(group=group_fx, duration=5000, time_delay=15)
        stars_Afx2.start(group=group_fx, duration=5000, time_delay=17)
        stars_Afx3.start(group=group_fx, duration=5000, time_delay=18)
        stars_Afx4.start(group=group_fx, duration=5000, time_delay=20)

        cam_dbg.move_cam(group=MAIN, index=2, duration=10, smooth=True)
        cam_dbg.move_cam(group=MAIN, index=3, duration=15, smooth=True, time_delay=10)

        cam_dbg.set(group=MAIN)

        main_group.append_time(28)
