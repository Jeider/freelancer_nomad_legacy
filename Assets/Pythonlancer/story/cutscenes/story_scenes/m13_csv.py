from random import choice

from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import Male, Female, Trent

from universe.content import mineable

from story import actors

LOGOS_ROT = 30
PATH_1 = '{0.0, 0.0, 0.0}, {1.0, 0.0, 0, 0.0}, {10.4392, -0.0065511, -50.3667}, {0.982119, -0.000183236, -0.188261, -3.51244e-05}, {39.4467, -0.0624247, -92.4023}, {0.885348, -0.00106029, -0.464927, -0.000556796}, {80.4048, -0.271387, -75.617}, {0.238855, -0.000466123, -0.971053, -0.001895}, {96.0648, -0.448733, -26.4794}, {0.099638, -0.000154673, -0.995023, -0.00154462}, {103.493, -0.600208, 24.6966}, {0.0502539, -7.00399e-05, -0.998735, -0.00139196}, {107.168, -0.739449, 76.2926}, {0.0230054, -3.00178e-05, -0.999735, -0.00130447}, {108.517, -0.831906, 128.005}, {0.0033625, 5.51487e-07, -0.999994, 0.00016401}, {108.035, -0.699112, 179.734}, {-0.0116737, -2.64099e-05, -0.999929, 0.00226218}, {106.31, -0.39282, 231.436}, {-0.0206812, -7.27599e-05, -0.99978, 0.00351738}, {103.964, 0.0, 283.115}, {-0.0236776, -9.3192e-05, -0.999712, 0.00393474}'


class Logos(Ship):
    COMPOUND_TEMPLATE_NAME = 'or_osiris'


class CSV(Ship):
    COMPOUND_TEMPLATE_NAME = 'ge_csv'


class Lapa(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_lapa'


class SceneBackground(BackgroundProp):
    COMPOUND_TEMPLATE_NAME = 'om13_nebula'


class Stars(BackgroundProp):
    COMPOUND_TEMPLATE_NAME = 'new_generic'


class Blackhole(Solar):
    COMPOUND_TEMPLATE_NAME = 'BlackHoleCore'


class AsteroidOne(Solar):
    COMPOUND_TEMPLATE_NAME = 'om15_static_large_ast01'


class AsteroidTwo(Solar):
    COMPOUND_TEMPLATE_NAME = 'om15_static_large_ast02'


class AsteroidThree(Solar):
    COMPOUND_TEMPLATE_NAME = 'om15_static_large_ast04'


class AsteroidField(mineable.DefaultField):
    BOX_SIZE = 700
    DENSITY_MULTIPLER = 5
    DRIFT_X = 0.8
    DRIFT_Y = 0.5
    DRIFT_Z = 0.8
    EMPTY_CHANCE = 0
    ROTATE_X_MIN = -180
    ROTATE_X_MAX = 180
    ROTATE_Y_MIN = -180
    ROTATE_Y_MAX = 180
    ROTATE_Z_MIN = -180
    ROTATE_Z_MAX = 180


class Msn13CSVMagnetScene(Scene):
    POINT_ROTATE_OVERRIDES = {
        'bh': [30, 0, 0],
        'logos_start': [0, 150, 0],
        'logos_launch': [0, 150, 0],
        'csv_launch': [0, -30, 0],
        'csv_launch2': [0, -30, 0],
    }

    def action(self):
        main_group = self.get_group(MAIN)
        farplane = 30000

        # CAMERAS

        cam_dbg = LookAtCamera(root=self, name='cam_dbg', fov=30, farplane=farplane)
        cam_xdbg = LookAtCamera(root=self, name='cam_xdbg', fov=30, farplane=farplane)
        cam_start = LookAtCamera(root=self, name='cam_start', fov=30, farplane=farplane)
        cam_launch = LookAtCamera(root=self, name='cam_launch', fov=25, farplane=farplane)

        # PROPS

        open_sound = Sound(root=self, name='depot_open_sound', sound='depot_open_sound', attenuation=-6)
        close_sound = Sound(root=self, name='depot_close_sound', sound='depot_close_sound', attenuation=-6)



        bh_point_name = 'point_bh_far'
        self.add_point(name=bh_point_name, position=[0, 0, 10000], rotate=[20, 0, 0], source=SOURCE_PYTHONLANCER)

        SceneBackground(root=self, name='scene_bg1', light_group=100, init_point=self.DEFAULT_POINT_NAME, rotate_y=-180)
        Stars(root=self, name='scene_bg2', light_group=100, init_point=self.DEFAULT_POINT_NAME)

        asteroid_classes = [
            AsteroidOne, AsteroidTwo, AsteroidThree
        ]

        field1 = AsteroidField()
        i = 0
        for box in field1.get_boxes():
            this_class = choice(asteroid_classes)

            name = f'astbox_{i}_a'
            self.add_point(name=name, position=box.get_position(y_adjust=-600), rotate=box.get_rotate(),
                           source=SOURCE_PYTHONLANCER)
            this_class(root=self, init_point=name, name=name, light_group=0)

            name = f'astbox_{i}_b'
            self.add_point(name=name, position=box.get_position(y_adjust=600), rotate=box.get_rotate(),
                           source=SOURCE_PYTHONLANCER)
            this_class(root=self, init_point=name, name=name, light_group=0)

            i += 1

        Blackhole(root=self, name='the_bh', light_group=101, init_point=bh_point_name)
        bh_effects = ['Intro_volcanoplanet_sun', 'gf_neutronstar', 'bh_chunks']

        i = 0
        for fx in bh_effects:
            alchemy = Alchemy(root=self, name=f'fx_{fx}', particles=fx, point_name=bh_point_name)
            alchemy.start(group=BG, duration=5000)
            # if i == 0:
            #     RotateAxisEvent(root=self, group=MAIN, object_name=alchemy.name,
            #                     angle=-1200, duration=360, smooth=False)

            i += 1

        playership = PlayerShip(root=self, name='playership_the', light_group=0, init_point='csv_alt', rotate_from_quat=True)
        csv = CSV(root=self, name='csv_the', light_group=0, init_point='csv_test',
                  loadout='rtc_m13_csv', have_lights=True)


        lapa = Lapa(root=self, name='the_lapa', init_point=self.OFFSCREEN_POINT_NAME, light_group=0)
        ConnectHardpointEvent(root=self, group=BG, target_name=lapa.name, parent_name=csv.name,
                              duration=1000, target_hardpoint="HpConnect",
                              parent_hardpoint="HpLapa01")

        csv_engine = Alchemy(root=self, name='csv_eng', particles='gf_br_csv_engine01_fire', point_name=self.OFFSCREEN_POINT_NAME)
        csv_engine.start(group=BG, duration=5000)
        AttachEvent(root=self, group=BG, duration=5000, target_name=csv_engine.name, parent_name=csv.name,
                    target_part='HpEngine01', target_type=TARGET_HARDPOINT, adjust_orient=True)


        csv_trail = Alchemy(root=self, name='csv_eng_trail', particles='gf_br_csv_engine01_trail', point_name=self.OFFSCREEN_POINT_NAME)
        csv_trail.start(group=BG, duration=5000)
        AttachEvent(root=self, group=BG, duration=5000, target_name=csv_trail.name, parent_name=csv.name,
                    target_part='HpEngine01', target_type=TARGET_HARDPOINT, adjust_orient=True)

        csv_rumble = SpatialSound(root=self, name='csv_rumble', sound='rumble_ci_h_fighter', attenuation=-20, dmin=100, dmax=300)
        AttachEvent(root=self, group=BG, duration=5000, target_name=csv_rumble.name, parent_name=csv.name,
                    target_part='HpEngine01', target_type=TARGET_HARDPOINT)

        csv_eng_start = SpatialSound(root=self, name='csv_eng_start', sound='engine_ci_freighter_start', attenuation=0, dmin=100, dmax=300)
        csv_eng_loop = SpatialSound(root=self, name='csv_eng_loop', sound='engine_ci_freighter_loop', attenuation=-20, dmin=100, dmax=300)


        # csv_trail.set_sparam(group=MAIN, duration=1, sparam=0.5, time_delay=1)

        # MoveEvent(root=self, group=MAIN, object_name=csv.name, target_name=self.get_automarker_name('csv_test2'), duration=10,)

        lapa.anim(group=MAIN, anim='Sc_lapa open', duration=3)
        lapa.anim(group=MAIN, anim='Sc_lapa close', duration=4, time_delay=5)


        Light(root=self, name='test_ambi', point_name=self.DEFAULT_POINT_NAME,
              light_group=0, diffuse=[1, 0.8, 0.6],
              ambient=[0.12, 0.12, 0.12], direction=[0, 0, 1], light_type=L_DIRECT, range=2000)

        logos = Logos(root=self, name='logos_the', light_group=0, init_point='logos_start',
                      loadout='li_battleship_01', have_lights=True)

        logos_engine = Alchemy(root=self, name='logos_engine', particles='gf_li_largeengine02', sparam=0.9, point_name=self.OFFSCREEN_POINT_NAME)
        logos_engine.start(group=BG, duration=5000)
        AttachEvent(root=self, group=BG, duration=5000, target_name=logos_engine.name, parent_name=logos.name,
                    target_part='HpEngine01', target_type=TARGET_HARDPOINT, adjust_orient=True)

        logos_reactor = Alchemy(root=self, name='logos_reactor', particles='gf_li_battleship_reactor01', point_name=self.OFFSCREEN_POINT_NAME)
        logos_reactor.start(group=BG, duration=5000)
        AttachEvent(root=self, group=BG, duration=5000, target_name=logos_reactor.name, parent_name=logos.name,
                    target_part='HpFX02', target_type=TARGET_HARDPOINT, adjust_orient=True)


        # logos_rumble = Sound(root=self, name='logos_rumble2', sound='rumble_battleship', attenuation=-20, dmin=1000, dmax=1000000)
        # logos_rumble.start(group=BG, duration=1000, loop=True)
        # AttachEvent(root=self, group=BG, duration=5000, target_name=logos_rumble.name, parent_name=logos.name,
        #             target_part='HpEngine01', target_type=TARGET_HARDPOINT)


        logos_rumble2 = SpatialSound(root=self, name='logos_rumble', sound='rumble_battleship_alt', attenuation=-20, dmin=10, dmax=1000000)
        logos_rumble2.start(group=BG, duration=1000, loop=True)
        AttachEvent(root=self, group=BG, duration=5000, target_name=logos_rumble2.name, parent_name=logos.name,
                    target_part='HpEngine01', target_type=TARGET_HARDPOINT)



        # elite_ship = TestShip(root=self, name='liberty_elite_ship', init_point='ship', light_group=0)
        #
        # path = MotionPath(root=self, name='the_path1', path_data=PATH_3)
        # path.anim(group=MAIN, duration=10, target_name=elite_ship.name, adjust_orient=True, time_delay=1, smooth=True)

        # LookAtEvent(
        #     root=self, group=BG,
        #     point=elite_ship, focus=self.get_automarker('shiplook'),
        #     duration=20,
        # )

        cam_start.set(group=MAIN)

        MoveEvent(root=self, group=MAIN, object_name=logos.name, target_name=self.get_automarker_name('logos_launch'), duration=20, smooth=True)
        logos_engine.set_sparam(group=MAIN, duration=1, sparam=0, time_delay=18)
        logos_rumble2.change_attenuation(group=MAIN, duration=3, attenuation=0)
        logos_rumble2.change_attenuation(group=MAIN, duration=5, attenuation=-20, time_delay=9)

        main_group.append_time(15)

        # self.set_start_time(main_group.get_time())

        # MoveFastEvent(root=self, group=MAIN, object_name=logos.name, target_name=self.get_automarker_name('logos_launch'))

        cam_launch.set(group=MAIN)
        cam_launch.move_cam(group=MAIN, index=3, duration=20, smooth=True)
        cam_launch.move_focus(group=MAIN, index=3, duration=15, smooth=True, time_delay=5)


        logos_rumble2.change_attenuation(group=MAIN, duration=0.3, attenuation=0)
        logos_rumble2.change_attenuation(group=MAIN, duration=2, attenuation=-10, time_delay=5)

        main_group.append_time(5)

        logos.anim(group=MAIN, anim='Sc_open baydoor', duration=10, time_delay=2)
        open_sound.start(group=MAIN, duration=5, time_delay=2)


        logos.anim(group=MAIN, anim='Sc_close baydoor', duration=10, time_delay=7)
        close_sound.start(group=MAIN, duration=5, time_delay=7)


        csv_eng_start.start(group=MAIN, duration=1000, loop=False, time_delay=3)
        csv_eng_loop.start(group=MAIN, duration=1000, loop=True, time_delay=3)

        MoveFastEvent(root=self, group=MAIN, object_name=csv.name, target_name=self.get_automarker_name('csv_launch'))
        MoveEvent(root=self, group=MAIN, object_name=csv.name, target_name=self.get_automarker_name('csv_launch2'),
                  duration=5, smooth=True, time_delay=3)
        csv_rumble.start(group=MAIN, duration=1000, loop=True, time_delay=3)
        csv_rumble.change_attenuation(group=MAIN, attenuation=-10, duration=3)
        csv_eng_loop.start(group=MAIN, duration=1000, loop=True, time_delay=3)

        #
        # main_group.append_time(100)
        #
        #
        # self.set_start_time(main_group.get_time())

        # cam_launch.set(group=MAIN)
        # cam_launch.move_cam(group=MAIN, index=3, duration=8, smooth=True)
        # cam_launch.move_focus(group=MAIN, index=3, duration=8, smooth=True)

        # MoveFastEvent(root=self, group=MAIN, object_name=csv.name, target_name=self.get_automarker_name('csv_launch2'))

        main_group.append_time(7)
        path = MotionPath(root=self, name='the_path1', path_data=PATH_1, point_name='csv_launch2')
        path.anim(group=MAIN, duration=10, target_name=csv.name, adjust_orient=True, time_delay=1, smooth=False)

        csv_rumble.change_attenuation(group=MAIN, attenuation=-5, duration=3)
        csv_eng_loop.change_attenuation(group=MAIN, attenuation=-2, duration=3)
        csv_engine.set_sparam(group=MAIN, duration=3, sparam=0.9)
        csv_trail.set_sparam(group=MAIN, duration=3, sparam=0.9)

        main_group.append_time(1000)

        self.set_start_time(main_group.get_time())

        cam_dbg.set(group=MAIN)

        main_group.append_time(1000)
