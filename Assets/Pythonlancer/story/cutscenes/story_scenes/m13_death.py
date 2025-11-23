from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import Male, Female, Trent

from story import actors


class TestShip(Ship):
    COMPOUND_TEMPLATE_NAME = 'li_elite'


class Beast(Ship):
    COMPOUND_TEMPLATE_NAME = 'beast_ship'


class SceneBackground(BackgroundProp):
    COMPOUND_TEMPLATE_NAME = 'edge_exclusion'


PATH_1 = '{0.0, 0.0, 0.0}, {1.0, 0.0, 0, 0.0}, {10.4392, -0.0065511, -50.3667}, {0.982119, -0.000183236, -0.188261, -3.51244e-05}, {39.4467, -0.0624247, -92.4023}, {0.885348, -0.00106029, -0.464927, -0.000556796}, {80.4048, -0.271387, -75.617}, {0.238855, -0.000466123, -0.971053, -0.001895}, {96.0648, -0.448733, -26.4794}, {0.099638, -0.000154673, -0.995023, -0.00154462}, {103.493, -0.600208, 24.6966}, {0.0502539, -7.00399e-05, -0.998735, -0.00139196}, {107.168, -0.739449, 76.2926}, {0.0230054, -3.00178e-05, -0.999735, -0.00130447}, {108.517, -0.831906, 128.005}, {0.0033625, 5.51487e-07, -0.999994, 0.00016401}, {108.035, -0.699112, 179.734}, {-0.0116737, -2.64099e-05, -0.999929, 0.00226218}, {106.31, -0.39282, 231.436}, {-0.0206812, -7.27599e-05, -0.99978, 0.00351738}, {103.964, 0.0, 283.115}, {-0.0236776, -9.3192e-05, -0.999712, 0.00393474}'

class Msn13KriegDeathScene(Scene):
    POINT_ROTATE_OVERRIDES = {
        'ship_leave': [0, 180, 0],
        'fire_conn': [0, 180, 0],
    }

    def action(self):
        main_group = self.get_group(MAIN)

        music = Music(root=self, name='music_hypergate2', sound='rtc_music_finale2', attenuation=0)
        music.start(group=BG, duration=1000, loop=True)

        cam_dbg = LookAtCamera(root=self, name='cam_dbg', fov=40, farplane=100000)
        cam_leave = StaticCamera(root=self, name='cam_leave', fov=40, farplane=100000)
        cam_endanim = StaticCamera(root=self, name='cam_endanim', fov=25, farplane=100000)
        cam_fire = StaticCamera(root=self, name='cam_fire', fov=22, farplane=100000)
        cam_death = LookAtCamera(root=self, name='cam_death', fov=40, farplane=100000)

        beast = Beast(root=self, name='Beast', init_point='beast', light_group=5)
        playership = PlayerShip(root=self, name='playership_the', light_group=0, init_point='ship_init', rotate_from_quat=True)


        player_light = Light(root=self, name='test_ambi', point_name=self.DEFAULT_POINT_NAME,
                             light_group=0, diffuse=[1, 0.2, 0.2],
                             ambient=[0.05, 0.01, 0.01], direction=[0, 0, 1], light_type=L_DIRECT, range=2000, cutoff=150)


        player_light2 = Light(root=self, name='test_ambi2', point_name=self.DEFAULT_POINT_NAME,
                             light_group=0, diffuse=[0.5, 0, 0.4],
                             ambient=[0.05, 0.01, 0.01], direction=[0, 0, -1], light_type=L_DIRECT, range=2000, cutoff=150)

        beast_light1 = Light(root=self, name='beast_lt1', point_name='beast_lt1',
                             light_group=5, diffuse=[1, 0, 0], on=True,
                             ambient=[0.05, 0.01, 0.01], direction=[0, 1, 1], light_type=L_DIRECT, range=20000, cutoff=150)

        beast_light2 = Light(root=self, name='beast_lt2', point_name='beast_lt2',
                             light_group=5, diffuse=[0.6, 0, 0.1], on=True,
                             ambient=[0.05, 0.05, 0.1], direction=[0, 1, -1], light_type=L_DIRECT, range=20000, cutoff=150)

        RotateAxisEvent(root=self, group=BG, object_name=beast_light1.name, angle=-90, duration=0.01, smooth=False, axis=Z_AXIS)
        RotateAxisEvent(root=self, group=BG, object_name=beast_light2.name, angle=90, duration=0, smooth=False, axis=Z_AXIS)


        neuro1 = Alchemy(root=self, name='neuro1', particles='bh_neurons', point_name='fx1')
        neuro2 = Alchemy(root=self, name='neuro2', particles='bh_neurons', point_name='fx2')
        neuro3 = Alchemy(root=self, name='neuro3', particles='bh_neurons', point_name='fx3')
        neuro1.start(group=BG, duration=5000)
        neuro2.start(group=BG, duration=5000)
        neuro3.start(group=BG, duration=5000)


        bang1 = Alchemy(root=self, name='bang1fx', particles='gf_explosion_sphere_box', point_name='bang1')
        bang2 = Alchemy(root=self, name='bang2fx', particles='gf_explosion_sphere_box', point_name='bang2')
        bang3 = Alchemy(root=self, name='bang3fx', particles='gf_explosion_sphere_box', point_name='bang3')
        bang4 = Alchemy(root=self, name='bang4fx', particles='gf_explosion_sphere_box', point_name='bang4')
        bang1.start(group=BG, duration=15, time_delay=1)
        bang2.start(group=BG, duration=15, time_delay=4)
        bang3.start(group=BG, duration=15, time_delay=2)
        bang4.start(group=BG, duration=15, time_delay=3)

        bang1.start(group=BG, duration=15, time_delay=8)
        bang3.start(group=BG, duration=15, time_delay=10)

        bang1_sound = Sound(root=self, name='bang1_sound', sound='med_explosion3', attenuation=-8)
        bang2_sound = Sound(root=self, name='bang2_sound', sound='med_explosion2', attenuation=-8)
        bang3_sound = Sound(root=self, name='bang3_sound', sound='med_explosion1', attenuation=-8)
        bang4_sound = Sound(root=self, name='bang4_sound', sound='med_explosion2', attenuation=-8)
        bang1_sound.start(group=MAIN, duration=5, time_delay=1)
        bang2_sound.start(group=MAIN, duration=5, time_delay=3)
        bang3_sound.start(group=MAIN, duration=5, time_delay=5)
        bang4_sound.start(group=MAIN, duration=5, time_delay=7)
        bang1_sound.start(group=MAIN, duration=5, time_delay=8)
        bang2_sound.start(group=MAIN, duration=5, time_delay=10)

        kr_close_sound = Sound(root=self, name='kr_close_sound', sound='debris_explosion4', attenuation=-1)
        kr_close_sound.start(group=MAIN, duration=5, time_delay=12)


        damage1 = Alchemy(root=self, name='damage1fx', particles='gf_sphere_box_damage', point_name='damage1')
        damage1.start(group=BG, duration=15)

        beastfx1 = Alchemy(root=self, name='beastfx1', particles='beast_core', point_name='beast')
        beastfx2 = Alchemy(root=self, name='beastfx2', particles='beast_core_shield', point_name='beast')
        beastfx3 = Alchemy(root=self, name='beastfx3', particles='beast_core_light', point_name='beast')
        beastfx1.start(group=BG, duration=30)
        beastfx2.start(group=BG, duration=30)
        beastfx3.start(group=BG, duration=30)


        beast.anim(group=MAIN, anim='Sc_door open force', duration=1)




        player_engine = Alchemy(root=self, name='player_engine', particles=PLAYER_ENGINES, point_name=self.DEFAULT_POINT_NAME,
                                sparam=0)
        player_engine.start(group=BG, duration=5000)

        beast.anim(group=MAIN, anim='Sc_door close', time_scale=2, duration=25, time_delay=2)

        player_engine.set_sparam(group=MAIN, sparam=0.9, duration=0.1)
        MoveEvent(root=self, group=MAIN, object_name=playership.name, target_name=self.get_automarker_name('ship_leave'),
                  duration=21, smooth=True, adjust_orient=False)

        leave_point = self.get_point('ship_leave')
        cam_leave_point = self.get_point('cam_endanim')

        AttachEvent(root=self, group=MAIN, duration=100, target_name=cam_endanim.name, parent_name=playership.name,
                    target_part='', target_type=TARGET_ROOT, adjust_orient=False, entity_relative=False,
                    offset_x=cam_leave_point.position[0]-leave_point.position[0],
                    offset_y=cam_leave_point.position[1]-leave_point.position[1],
                    offset_z=cam_leave_point.position[2]-leave_point.position[2],
                    )

        cam_leave.set(group=MAIN)
        main_group.append_time(8)
        cam_endanim.set(group=MAIN)
        cam_endanim.change_fov(group=MAIN, fov=40, duration=5)


        player_engine.set_sparam(group=MAIN, sparam=0.0, duration=2, time_delay=4)
        RotateAxisEvent(root=self, group=MAIN, object_name=playership.name, angle=180,
                        duration=5, smooth=True, axis=Y_AXIS,
                        time_delay=4)


        powersource_fx = Alchemy(root=self, name='powersource_fx', particles='rtc_powesource_on', point_name=self.DEFAULT_POINT_NAME)
        powersource_beam = Alchemy(root=self, name='powersource_beam', particles='rtc_powesource_on_beam', point_name=self.DEFAULT_POINT_NAME)

        fire_connector = self.get_automarker_name('fire_conn')


        AttachEvent(root=self, group=MAIN, duration=100, target_name=powersource_fx.name, parent_name=playership.name,
                    target_part='', target_type=TARGET_ROOT, adjust_orient=True, entity_relative=False,
                    offset_y=5)

        AttachEvent(root=self, group=MAIN, duration=100, target_name=powersource_beam.name, parent_name=fire_connector,
                    target_part='hpcockpit', target_type=TARGET_ROOT, adjust_orient=True, entity_relative=True,
                    offset_y=2)

        AttachEvent(root=self, group=MAIN, duration=100, target_name=fire_connector, parent_name=playership.name,
                    target_part='hpcockpit', target_type=TARGET_HARDPOINT, adjust_orient=False, entity_relative=False)

        main_group.append_time(10)


        powersource_fx.start(group=MAIN, duration=15, time_delay=-5)

        # rtc_powesource_on
        # rtc_powesource_on_beam

        cam_fire.set(group=MAIN)
        cam_fire.move_cam(group=MAIN, index=2, duration=3)

        powersource_beam.start(group=MAIN, duration=5, time_delay=4)

        main_group.append_time(8)



        cam_death.set(group=MAIN)
        main_group.append_time(3)

        cam_death.change_fov(group=MAIN, fov=60, duration=25, smooth=True)
        cam_death.move_cam(group=MAIN, index=2, duration=25, smooth=True)


        player_engine.set_sparam(group=MAIN, sparam=0.9, duration=2)
        path = MotionPath(root=self, name='the_path1', path_data=PATH_1, point_name='ship_leave')
        path.anim(group=MAIN, duration=10, target_name=playership.name, adjust_orient=True, time_delay=1, smooth=False)

        MoveEvent(root=self, group=MAIN, object_name=playership.name, target_name=self.get_automarker_name('ship_goaway'),
                  duration=20, smooth=False, time_delay=11)


        exp_bang1 = Alchemy(root=self, name='fx_exp_bang1', particles='dyson_city_genexp', point_name='hp1')
        exp_bang2 = Alchemy(root=self, name='fx_exp_bang2', particles='dyson_city_genexp', point_name='hp2')
        exp_bang3 = Alchemy(root=self, name='fx_exp_bang3', particles='dyson_city_genexp', point_name='hp3')
        exp_bang4 = Alchemy(root=self, name='fx_exp_bang4', particles='dyson_city_genexp', point_name='hp4')
        exp_bang5 = Alchemy(root=self, name='fx_exp_bang5', particles='dyson_city_genexp', point_name='hp5')
        exp_bang6 = Alchemy(root=self, name='fx_exp_bang6', particles='dyson_city_genexp', point_name='hp6')
        exp_bang7 = Alchemy(root=self, name='fx_exp_bang7', particles='dyson_city_genexp', point_name='hp7')
        exp_bang1.start(group=MAIN, duration=15, time_delay=1)
        exp_bang2.start(group=MAIN, duration=15, time_delay=3)
        exp_bang3.start(group=MAIN, duration=15, time_delay=2)
        exp_bang4.start(group=MAIN, duration=15, time_delay=4.5)
        exp_bang5.start(group=MAIN, duration=15, time_delay=4)
        exp_bang6.start(group=MAIN, duration=15, time_delay=2.5)
        exp_bang7.start(group=MAIN, duration=15, time_delay=3.5)


        damage2 = Alchemy(root=self, name='damage2fx', particles='gf_sphere_box_damage', point_name='damage1')
        damage2.start(group=MAIN, duration=30, time_delay=2)


        gen_exp_bang1 = Alchemy(root=self, name='fx_gen_exp_bang1', particles='dyson_city_genexp', point_name='genp1')
        gen_exp_bang2 = Alchemy(root=self, name='fx_gen_exp_bang2', particles='dyson_city_genexp', point_name='genp2')
        gen_exp_bang3 = Alchemy(root=self, name='fx_gen_exp_bang3', particles='dyson_city_genexp', point_name='genp3')
        gen_exp_bang4 = Alchemy(root=self, name='fx_gen_exp_bang4', particles='dyson_city_genexp', point_name='genp4')
        gen_exp_bang5 = Alchemy(root=self, name='fx_gen_exp_bang5', particles='dyson_city_genexp', point_name='genp5')
        gen_exp_bang6 = Alchemy(root=self, name='fx_gen_exp_bang6', particles='dyson_city_genexp', point_name='genp6')

        gen_exp_bang1.start(group=MAIN, duration=15, time_delay=6)
        gen_exp_bang2.start(group=MAIN, duration=15, time_delay=7)
        gen_exp_bang3.start(group=MAIN, duration=15, time_delay=7.8)
        gen_exp_bang4.start(group=MAIN, duration=15, time_delay=8.6)
        gen_exp_bang5.start(group=MAIN, duration=15, time_delay=9.2)
        gen_exp_bang6.start(group=MAIN, duration=15, time_delay=10)


        redmoon_damage = Alchemy(root=self, name='fx_redmoon_dmg', particles='gf_redmoon_process_explosion', point_name='beast')
        redmoon_damage.start(group=MAIN, duration=15, time_delay=12)

        redmoon_damage2 = Alchemy(root=self, name='fx_redmoon_dmg2', particles='gf_redmoon_process_explosion', point_name='beast')
        redmoon_damage2.start(group=MAIN, duration=15, time_delay=24)

        redmoon_explode = Alchemy(root=self, name='fx_redmoon_expl', particles='gf_redmoon_final_explosion', point_name='beast')
        redmoon_explode.start(group=MAIN, duration=15, time_delay=22)

        MoveOffscreenEvent(root=self, group=MAIN, object_name=beast.name, time_delay=22.2)


        exp1_sound = Sound(root=self, name='exp1_sound', sound='csx_large01', attenuation=-4)
        exp2_sound = Sound(root=self, name='exp2_sound', sound='csx_large03', attenuation=-4)
        exp3_sound = Sound(root=self, name='exp3_sound', sound='csx_large04', attenuation=-4)
        exp4_sound = Sound(root=self, name='exp4_sound', sound='csx_large05', attenuation=-4)
        exp5_sound = Sound(root=self, name='exp5_sound', sound='csx_large01', attenuation=-4)
        exp6_sound = Sound(root=self, name='exp6_sound', sound='csx_large03', attenuation=-4)
        exp7_sound = Sound(root=self, name='exp7_sound', sound='csx_large04', attenuation=-4)
        exp8_sound = Sound(root=self, name='exp8_sound', sound='csx_large05', attenuation=-4)
        exp1_sound.start(group=MAIN, duration=5, time_delay=1)
        exp2_sound.start(group=MAIN, duration=5, time_delay=2)
        exp3_sound.start(group=MAIN, duration=5, time_delay=3)
        exp4_sound.start(group=MAIN, duration=5, time_delay=4)
        exp5_sound.start(group=MAIN, duration=5, time_delay=5)
        exp6_sound.start(group=MAIN, duration=5, time_delay=6)
        exp7_sound.start(group=MAIN, duration=5, time_delay=7)
        exp8_sound.start(group=MAIN, duration=5, time_delay=8)
        exp1_sound.start(group=MAIN, duration=5, time_delay=9)
        exp2_sound.start(group=MAIN, duration=5, time_delay=10)


        u_exp1_sound = Sound(root=self, name='u_exp1_sound', sound='med_explosion2', attenuation=0)
        u_exp2_sound = Sound(root=self, name='u_exp2_sound', sound='med_explosion3', attenuation=0)
        u_exp1_sound.start(group=MAIN, duration=5, time_delay=12)
        u_exp2_sound.start(group=MAIN, duration=5, time_delay=22)



        main_group.append_time(1000)
