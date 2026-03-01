from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import Male, Female, Trent
from story.cutscenes import sequence

from story import actors


class SciConsole(Prop):
    COMPOUND_TEMPLATE_NAME = 'li_science_console'


class DigSiteTable(Prop):
    COMPOUND_TEMPLATE_NAME = 'table_analyzer'
    FORCE_POS = [
        -3.686486,
        0.398995,
        -8.169765
    ]
    FORCE_MATRIX = [
        [
            0.715366,
            0.016323,
            0.698559
        ],
        [
            0.698559,
            0.006647,
            -0.715522
        ],
        [
            -0.016323,
            0.999845,
            -0.006647
        ]
    ]


class PygarScene(Scene):
    DUMP_FILE = 'dig_site'

    def action(self):
        main_group = self.get_group(MAIN)

        DigSiteTable(root=self, name='table', init_point=self.DEFAULT_POINT_NAME, light_group=0, use_ambient=True)
        SciConsole(root=self, name='sci_console', init_point='sci_console', light_group=0, use_ambient=True, rotate_from_quat=True)

        music_one = Music(root=self, name='music1', sound='rtc_music_anticipation_more_forboding', attenuation=-12)
        music_one.start(group=MAIN, duration=1000, loop=True)

        cam_greet = StaticCamera(root=self, name='cam_greet', fov=28)

        cam_edison = StaticCamera(root=self, name='cam_edison', fov=25)
        cam_mandrake = StaticCamera(root=self, name='cam_mandrake', fov=25)
        cam_mandrake_alt = StaticCamera(root=self, name='cam_mandrake_alt', fov=18)
        cam_trent = StaticCamera(root=self, name='cam_trent', fov=18)
        cam_monkeyking = StaticCamera(root=self, name='cam_monkeyking', fov=18)

        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='trent', rotate_from_quat=True,
                           camera=cam_trent, anim_sequence=sequence.SEQUENCE_MALE_STAND_FSTHIPB_CROSS)

        edison = Character(root=self, actor=actors.EdisonTrentHolo, light_group=0, init_point='edison_init', rotate_from_quat=True,
                           camera=cam_edison, anim_sequence=sequence.SEQUENCE_MALE_STAND_CONV_FREE)

        mandrake = Character(root=self, actor=actors.Mandrake, light_group=0, init_point='mandrake', rotate_from_quat=True,
                           camera=cam_mandrake, anim_sequence=sequence.SEQUENCE_MALE_SCI_KEYBOARD)

        monkeyking = Character(root=self, actor=actors.MonkeyKing, light_group=0, init_point='monkeyking', rotate_from_quat=True,
                           camera=cam_monkeyking, anim_sequence=sequence.SEQUENCE_MALE_STAND_RHAND_ALT)

        juni = Character(root=self, actor=actors.Juni, light_group=0, init_point='juni', rotate_from_quat=True,
                           camera=cam_mandrake, anim_sequence=sequence.SEQUENCE_FEMALE_STAND_CROSS)

        trent.idle(group=MAIN)
        edison.idle(group=MAIN)
        mandrake.idle_sit(group=MAIN)
        monkeyking.idle(group=MAIN)
        juni.idle(group=MAIN)

        mrk_trent = trent.get_stand_marker('trent')
        mrk_monkeyking = monkeyking.get_stand_marker('monkeyking')


        mrk_looktable = self.get_automarker_name('mrk_looktable')
        mrk_looktrent = self.get_automarker_name('mrk_looktrent')
        mrk_lookmonkey = self.get_automarker_name('mrk_lookmonkey')

        trent.move_head_ik(group=MAIN, target_name=mrk_looktable, immediately=True)
        monkeyking.move_head_ik(group=MAIN, target_name=mrk_looktrent, immediately=True)
        mandrake.move_head_ik(group=MAIN, target_name=mrk_looktrent, immediately=True)

        cam_greet.set(group=MAIN)
        cam_greet.move_cam(group=MAIN, index=2, duration=6, smooth=True)

        mandrake.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, trans_time=1, time_scale=0.8, time_delay=2)

        main_group.append_time(6)

        mandrake.motion(group=MAIN, duration=300, loop=True, anim='Sc_MLHAND_HNEUT_GESTL_TYPING_000LV_XB', trans_time=0.5)
        mandrake.motion(group=MAIN, duration=300, loop=True, anim='Sc_MLHAND_HNEUT_GESTR_TYPING_000LV_XB', trans_time=0.5)

        Autoplay(
            self,
            group=MAIN,
            start_index=0,
            finish_index=30
        )
        cam_edison.set(group=MAIN)
        main_group.append_time(2)

        MoveFastEvent(root=self, group=MAIN, object_name=edison.name, target_name=self.get_automarker_name('edison'))

        # mandrake.motion(group=MAIN, duration=5, anim='Sc_MLHAND_NEUT_LEFT_000LV_A_00', trans_time=0.5)
        # mandrake.motion(group=MAIN, duration=5, anim='Sc_MLHAND_NEUT_RGHT_000LV_A_00', trans_time=0.5)

        Autoplay(
            self,
            group=MAIN,
            start_index=40,
            finish_index=100
        )

        MoveOffscreenEvent(root=self, group=MAIN, object_name=edison.name)

        main_group.append_time(2)

        trent.start_head_ik(group=MAIN, duration=1000)
        monkeyking.start_head_ik(group=MAIN, duration=1000)

        # mandrake.motion(group=MAIN, duration=80, loop=True, anim='Sc_MLHAND_HNEUT_GESTL_TYPING_000LV_XB', trans_time=0.5)
        # mandrake.motion(group=MAIN, duration=80, loop=True, anim='Sc_MLHAND_HNEUT_GESTR_TYPING_000LV_XB', trans_time=0.5)

        Autoplay(
            self,
            group=MAIN,
            start_index=110,
            finish_index=270,
            head_ik_per_index={
                160: [
                    IkDelay(trent, mrk_lookmonkey, duration=1),
                ],
                270: [
                    IkDelay(trent, mrk_looktable, duration=1),
                ],
            }
        )

        mandrake.motion(group=MAIN, duration=5, anim='Sc_MLHAND_NEUT_LEFT_000LV_A_00', trans_time=0.5, time_delay=-2)
        mandrake.motion(group=MAIN, duration=5, anim='Sc_MLHAND_NEUT_RGHT_000LV_A_00', trans_time=0.5, time_delay=-2)
        cam_mandrake_alt.set(group=MAIN)

        mandrake.start_head_ik(group=MAIN, duration=1000)
        mandrake.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, trans_time=1, time_scale=0.8)
        mandrake.facial(group=MAIN, index=280, auto_lip=True)

        main_group.append_time(2)


'''
{
		3.5,
		START_MOTION,
		{
			"Char_jacobo"
		},
		{
			animation="Sc_MLHAND_HNEUT_GESTL_TYPING_000LV_XB",
			duration=7.474,
			trans_time=0.5,
			time_scale=1,
			weight=1,
			heading=-1,
			event_flags=2
		}
	},
	{
		3.5,
		START_MOTION,
		{
			"Char_jacobo"
		},
		{
			animation="Sc_MLHAND_HNEUT_GESTR_TYPING_000LV_XB",
			duration=7.459,
			trans_time=0.5,
			time_scale=1,
			weight=1,
			heading=-1,
			event_flags=2
		}
	},
		{
		37,
		START_MOTION,
		{
			"Char_trent"
		},
		{
			animation="Sc_MLHAND_NEUT_LEFT_000LV_A_00",
			duration=5,
			time_scale=1,
			weight=1,
			heading=-1
		}
	},
			
	{
		37,
		START_MOTION,
		{
			"Char_trent"
		},
		{
			animation="Sc_MLHAND_NEUT_RGHT_000LV_A_00",
			duration=5,
			time_scale=1,
			weight=1,
			heading=-1
		}
	},
	
'''