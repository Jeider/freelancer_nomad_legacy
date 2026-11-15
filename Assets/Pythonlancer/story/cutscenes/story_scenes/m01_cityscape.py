from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story import actors


class Propglass_green(Prop):
    COMPOUND_TEMPLATE_NAME = 'glass_green'


class EliteShip(Ship):
    COMPOUND_TEMPLATE_NAME = 'li_elite'


class ArmoredShip(Ship):
    COMPOUND_TEMPLATE_NAME = 'ge_armored'


class CityscapeScene(Scene):
    DUMP_FILE = 'm01_cityscape'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        cam_bar = LookAtCamera(root=self, name='cam_bar', fov=30, look_duration=200)
        cam_start = LookAtCamera(root=self, name='cam_start', fov=25, look_duration=200)
        cam_stuard = LookAtCamera(root=self, name='cam_stuard', fov=20, look_duration=200)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=15, look_duration=200)
        cam_read = LookAtCamera(root=self, name='cam_read', fov=15, look_duration=200)
        cam_walk = LookAtCamera(root=self, name='cam_walk', fov=15, look_duration=200)

        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True, floor_height=0.89)
        stuard = Character(root=self, actor=actors.Stewardess, light_group=0, init_point='Char_stuard', rotate_from_quat=True, floor_height=0.89)

        position_item = Propglass_green(root=self, name='position_item', init_point='position_item', light_group=0, rotate_from_quat=True)
        Wingman1 = EliteShip(root=self, name='Wingman1', init_point='Wingman1', light_group=3, rotate_from_quat=True,
                             loadout='level_li_elite_loadout04', have_lights=True)
        Wingman2 = EliteShip(root=self, name='Wingman2', init_point='Wingman2', light_group=3, rotate_from_quat=True,
                             loadout='level_li_elite_loadout04', have_lights=True)
        Wingman3 = EliteShip(root=self, name='Wingman3', init_point='Wingman3', light_group=3, rotate_from_quat=True,
                             loadout='level_li_elite_loadout04', have_lights=True)
        Prop_armored_transport = ArmoredShip(root=self, name='Prop_armored_transport', init_point='Prop_armored_transport',
                                             light_group=3, rotate_from_quat=True, loadout='intro_armored_default')
        armored_lookat = self.get_automarker('armored_lookat')
        LookAtEvent(root=self, group=MAIN, point=Prop_armored_transport, focus=armored_lookat,
                    duration=100, target_part='Body_Head', target_type=TARGET_PART, time_delay=0)

        engine = SpatialSound(root=self, name='Ship_l_elite_1_engine_li_small_1', sound='engine_li_small',
                              attenuation=0, dmin=100, dmax=300, priority='')
        engine.start(group=MAIN, duration=15, loop=True, time_delay=0)
        AttachEvent(root=self, group=MAIN, duration=60, target_name=engine.name, parent_name=Wingman2.name,
                    target_part='HpEngine01', target_type=TARGET_HARDPOINT,
                    adjust_pos=True, adjust_orient=True, entity_relative=True, time_delay=0)
        launch_start = Sound(root=self, name='launch_start', sound='engine_playership_launch_turbine',
                             attenuation=-5, dmin=50, dmax=1000, priority='')
        launch_continue = Sound(root=self, name='launch_continue', sound='engine_playership_launch',
                                attenuation=-5, dmin=50, dmax=1000, priority='')

        cam_start.set(group=MAIN, time_delay=0)
        cam_start.move_cam(group=MAIN, index=2, duration=7, smooth=True, time_delay=0)
        cam_start.move_focus(group=MAIN, index=2, duration=7, smooth=True, time_delay=0)
        cam_start.move_cam(group=MAIN, index=3, duration=5, smooth=True, time_delay=7)
        cam_start.move_focus(group=MAIN, index=3, duration=5, smooth=True, time_delay=7)
        MoveEvent(root=self, group=MAIN, object_name='Wingman1', target_name=self.get_automarker_name('Wingman1_path'),
                  duration=15, smooth=False, adjust_orient=False, time_delay=0)
        MoveEvent(root=self, group=MAIN, object_name='Wingman2', target_name=self.get_automarker_name('Wingman2_path'),
                  duration=15, smooth=False, adjust_orient=False, time_delay=0)
        MoveEvent(root=self, group=MAIN, object_name='Wingman3', target_name=self.get_automarker_name('Wingman3_path'),
                  duration=15, smooth=False, adjust_orient=False, time_delay=0)
        Wingman1.anim(group=MAIN, anim='Sc_force extend', duration=30, time_delay=0, time_scale=1, start_time=0)
        Wingman2.anim(group=MAIN, anim='Sc_force extend', duration=30, time_delay=0, time_scale=1, start_time=0)
        Wingman3.anim(group=MAIN, anim='Sc_force extend', duration=30, time_delay=0, time_scale=1, start_time=0)

        self._m(stuard, 'Sc_FMBODY_STND_IDLE_MED_000LV_xa_05', 0, 12)
        MoveFastEvent(root=self, group=MAIN, object_name='Char_trent', target_name=self.get_automarker_name('trent_init_pos'), time_delay=12)
        cam_stuard.set(group=MAIN, time_delay=12)
        cam_stuard.move_cam(group=MAIN, index=2, duration=6, smooth=True, time_delay=12)
        cam_stuard.move_focus(group=MAIN, index=2, duration=6, smooth=True, time_delay=12)
        self._m(stuard, 'Sc_FMBODY_STND_WAVE_LHND_000LV_XA_03', 12, 15)
        self._m(trent, 'Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02', 12.001, 15, scale=0.5)
        EyeIkEvent(root=self, group=MAIN, char_name='Char_stuard', target_name=self.get_automarker_name('stuard_look_at_eyes'),
                   duration=19, time_delay=12, target_type=TARGET_ROOT, transition_duration=0.25)
        NeckIkEvent(root=self, group=MAIN, char_name='Char_stuard', target_name=self.get_automarker_name('stuard_look_at_head'),
                    duration=19, time_delay=13, target_type=TARGET_ROOT, transition_duration=0.5)

        self._line(stuard, 10, 15)
        self._m(stuard, 'Sc_FMBODY_STND_IDLE_MED_000LV_xa_05', 15, 15, trans=1)
        NeckIkEvent(root=self, group=MAIN, char_name='Char_trent', target_name='Char_stuard', duration=5, time_delay=15, target_type=TARGET_HARDPOINT, target_part='hp_neck')
        self._m(trent, 'Sc_MLBODY_STND_GIVE_VEND_000LV_B_07', 16.5, 5, trans=0.25)
        self._m(stuard, 'Sc_FMBODY_STND_IDLE_SMALL_000LV_xa_05', 17, 15, trans=1, loop=True)
        self._move(self.get_automarker_name('stuard_look_at_head'), 'marker_trent_head_middle', 18, 1.5)
        self._move(self.get_automarker_name('stuard_look_at_eyes'), 'marker_docs', 18, 1)
        cam_read.set(group=MAIN, time_delay=19)
        self._move(self.get_automarker_name('stuard_look_at_head'), 'marker_trent_head_middle_left', 19, 1.5)
        self._move(self.get_automarker_name('stuard_look_at_eyes'), 'marker_docs_left', 19, 1)
        self._move(self.get_automarker_name('stuard_look_at_eyes'), 'marker_docs_right', 20.3, 0.5)
        self._move(self.get_automarker_name('stuard_look_at_head'), 'marker_trent_head_middle_right', 20.5, 1)

        self._line(stuard, 20, 21)
        self._move(self.get_automarker_name('stuard_look_at_head'), 'marker_trent_head_top', 22, 1)
        self._move(self.get_automarker_name('stuard_look_at_eyes'), 'marker_trent_head_top', 22, 1)
        self._m(trent, 'Sc_MLBODY_STND_IDLE_000LV_xa_04', 22, 1, trans=0.2)
        self._move(self.get_automarker_name('stuard_look_at_eyes'), 'marker_trent_head_top_left', 23, 1)
        self._m(trent, 'Sc_MLBODY_STND_SHAKHEAD_NO_SLGHTLY_000LV_XA_02', 23, 3, scale=0.5, trans=0.5)
        cam_trent.set(group=MAIN, time_delay=24)

        self._line(trent, 30, 25)
        self._m(trent, 'Sc_MLBODY_STND_GIVE_VEND_000LV_B_07', 26, 4, start=3, trans=1)

        MoveOffscreenEvent(root=self, group=MAIN, object_name='Char_stuard', time_delay=30)
        MoveOffscreenEvent(root=self, group=MAIN, object_name='Char_trent', time_delay=30)
        cam_bar.set(group=MAIN, time_delay=30)
        cam_bar.move_cam(group=MAIN, index=2, duration=12, smooth=True, time_delay=30)
        cam_bar.move_focus(group=MAIN, index=2, duration=12, smooth=True, time_delay=30)
        MoveEvent(root=self, group=MAIN, object_name='Prop_armored_transport', target_name=self.get_automarker_name('armored_pos2'),
                  duration=7, smooth=True, time_delay=31)
        MoveEvent(root=self, group=MAIN, object_name=armored_lookat.name, target_name=self.get_automarker_name('armored_lookat_pos2'),
                  duration=7, smooth=True, time_delay=31)
        MoveEvent(root=self, group=MAIN, object_name='Prop_armored_transport', target_name=self.get_automarker_name('armored_pos3'),
                  duration=5, smooth=True, time_delay=38)
        MoveEvent(root=self, group=MAIN, object_name=armored_lookat.name, target_name=self.get_automarker_name('armored_lookat_pos4'),
                  duration=4, smooth=True, time_delay=38)


        launch_start.start(group=MAIN, duration=500, time_delay=31)
        launch_continue.start(group=MAIN, duration=500, time_delay=37.25)

        self.set_duration(42)

    def _m(self, char, anim, delay, duration, scale=1, start=0, trans=None, loop=False):
        char.motion(group=MAIN, anim=anim, duration=duration, time_delay=delay,
                    time_scale=scale, start_time=start, trans_time=trans, loop=loop)

    def _move(self, object_name, point_name, delay, duration):
        MoveEvent(root=self, group=MAIN, object_name=object_name,
                  target_name=self.get_automarker_name(point_name),
                  duration=duration, smooth=True, time_delay=delay)

    def _line(self, char, index, at):
        group = self.get_group(MAIN)
        saved = group.time
        group.time = at
        try:
            char.facial(group=MAIN, index=index, auto_lip=True, append=False)
        finally:
            group.time = saved

