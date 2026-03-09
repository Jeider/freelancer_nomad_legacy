from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import Male, Female, Trent
from story.cutscenes import sequence

from story import actors


STATIC_ENTITIES = '''
	{
		entity_name="LIGHT_barocameras_left",
		type=LIGHT,
		template_name="",
		lt_grp=55,
		srt_grp=0,
		usr_flg=0,
		spatialprops={
			pos={0,1,0},
			orient={
				{1,0,0},
				{0,1,0},
				{0,0,1}
			}
		},
		lightprops={
			on=Y,
			color={
				255,
				255,
				255
			},
			diffuse={
				0.6,
				0.6,
				0.8
			},
			specular={
				0,
				0,
				0
			},
			ambient={
				0.2,
				0.4,
				0.1
			},
			direction={
				-1,
				0,
				0
			},
			range=150555,
			cutoff=30,
			type=L_DIRECT,
			theta=26.999985,
			atten={
				1,
				0,
				0.003
			}
		}
	},


	{
		entity_name="LIGHT_barocameras_trentlook",
		type=LIGHT,
		template_name="",
		lt_grp=56,
		srt_grp=0,
		usr_flg=0,
		spatialprops={
			pos={0,1,0},
			orient={
				{1,0,0},
				{0,1,0},
				{0,0,1}
			}
		},
		lightprops={
			on=Y,
			color={
				255,
				255,
				255
			},
			diffuse={
				0.6,
				0.6,
				0.8
			},
			specular={
				0,
				0,
				0
			},
			ambient={
				0.2,
				0.4,
				0.1
			},
			direction={
				-1,
				0,
				0
			},
			range=150555,
			cutoff=30,
			type=L_DIRECT,
			theta=26.999985,
			atten={
				1,
				0,
				0.003
			}
		}
	},


	{
		entity_name="Prop_server01",
		type=COMPOUND,
		template_name="m7_server",
		lt_grp=6,
		srt_grp=0,
		usr_flg=0,
		flags=LIT_DYNAMIC + LIT_AMBIENT,
		spatialprops={
			pos={
				-2.5,
				0,
				0.5

			},
			orient={
				{0,0,-1},
				{0,1,0},
				{1,0,0}
			}
		},
		userprops={
			category="Prop"
		}
	},

	{
		entity_name="Prop_server03",
		type=COMPOUND,
		template_name="m7_server",
		lt_grp=6,
		srt_grp=0,
		usr_flg=0,
		flags=LIT_DYNAMIC + LIT_AMBIENT,
		spatialprops={
			pos={
				-2.5,
				0,
				3.8
			},
			orient={
				{0,0,-1},
				{0,1,0},
				{1,0,0}
			}
		},
		userprops={
			category="Prop"
		}
	},
	{
		entity_name="Prop_server04",
		type=COMPOUND,
		template_name="m7_server",
		lt_grp=6,
		srt_grp=0,
		usr_flg=0,
		flags=LIT_DYNAMIC + LIT_AMBIENT,
		spatialprops={
			pos={
				2.7,
				0,
				0.5
			},
			orient={
				{0,0,1},
				{0,1,0},
				{-1,0,0}
			}
		},
		userprops={
			category="Prop"
		}
	},
	{
		entity_name="Prop_server05",
		type=COMPOUND,
		template_name="m7_server",
		lt_grp=6,
		srt_grp=0,
		usr_flg=0,
		flags=LIT_DYNAMIC + LIT_AMBIENT,
		spatialprops={
			pos={
				2.7,
				0,
				4.2
			},
			orient={
				{0,0,1},
				{0,1,0},
				{-1,0,0}
			}
		},
		userprops={
			category="Prop"
		}
	},
	
	{
		entity_name="Prop_barocamera01",
		type=COMPOUND,
		template_name="m7_barocamera",
		lt_grp=6,
		srt_grp=0,
		usr_flg=0,
		flags=LIT_DYNAMIC + LIT_AMBIENT,
		spatialprops={
			pos={
				2.8,
				0,
				2.4
			},
			orient={
				{1,0,0},
				{0,1,0},
				{0,0,1}
			}
		},
		userprops={
			category="Prop"
		}
	},

	{
		entity_name="Prop_barocamera03",
		type=COMPOUND,
		template_name="m7_barocamera",
		lt_grp=6,
		srt_grp=0,
		usr_flg=0,
		flags=LIT_DYNAMIC + LIT_AMBIENT,
		spatialprops={
			pos={
				-2.5,
				0,
				2
			},
			orient={
				{-1,0,0},
				{0,1,0},
				{0,0,-1}
			}
		},
		userprops={
			category="Prop"
		}
	},
	
	
	
	{
		entity_name="Prop_barocamera05",
		type=COMPOUND,
		template_name="m7_barocamera",
		lt_grp=7,
		srt_grp=0,
		usr_flg=0,
		flags=LIT_DYNAMIC + LIT_AMBIENT,
		spatialprops={
			pos={
				5.7,
				0,
				-9
			},
			orient={
				{0.7071068,0,-0.7071068},
				{0,1,0},
				{0.7071068,0,0.7071068}
			}
		},
		userprops={
			category="Prop"
		}
	},

	
	{
		entity_name="Prop_alien05",
		type=COMPOUND,
		template_name="m7_olaf",
		lt_grp=52,
		srt_grp=0,
		usr_flg=0,
		flags=LIT_DYNAMIC + LIT_AMBIENT,
		spatialprops={
			pos={
				5.6,
				1,
				-9.1
				
			},
			orient={
				{0.7071068,0,0.7071068},
				{0,1,0},
				{-0.7071068,0,0.7071068}
			}
		},
		userprops={
			category="Prop"
		}
	},

	
	{
		entity_name="Prop_barocamera06",
		type=COMPOUND,
		template_name="m7_barocamera_tall",
		lt_grp=7,
		srt_grp=0,
		usr_flg=0,
		flags=LIT_DYNAMIC + LIT_AMBIENT,
		spatialprops={
			pos={
				4.1,
				0,
				-10.6
			},
			orient={
				{0.7071068,0,-0.7071068},
				{0,1,0},
				{0.7071068,0,0.7071068}
			}
		},
		userprops={
			category="Prop"
		}
	},
	{
		entity_name="Prop_alien06",
		type=COMPOUND,
		template_name="m7_jarjar",
		lt_grp=51,
		srt_grp=0,
		usr_flg=0,
		flags=LIT_DYNAMIC + LIT_AMBIENT,
		spatialprops={
			pos={
				3.9,
				0.32,
				-10.5
			},
			orient={
				{0.7071068,0,0.7071068},
				{0,1,0},
				{-0.7071068,0,0.7071068}
			}
		},
		userprops={
			category="Prop"
		}
	},
	
	{
		entity_name="Prop_barocamera07",
		type=COMPOUND,
		template_name="m7_barocamera_tall",
		lt_grp=7,
		srt_grp=0,
		usr_flg=0,
		flags=LIT_DYNAMIC + LIT_AMBIENT,
		spatialprops={
			pos={
				2.5,
				0,
				-12.2
			},
			orient={
				{0.7071068,0,-0.7071068},
				{0,1,0},
				{0.7071068,0,0.7071068}
			}
		},
		userprops={
			category="Prop"
		}
	},
	{
		entity_name="Prop_alien07",
		type=COMPOUND,
		template_name="m7_samus",
		lt_grp=50,
		srt_grp=0,
		usr_flg=0,
		flags=LIT_DYNAMIC + LIT_AMBIENT,
		spatialprops={
			pos={
				2.4,
				-0.1,
				-12.2
			},
			orient={
				{0.7071068,0,0.7071068},
				{0,1,0},
				{-0.7071068,0,0.7071068}
			}
		},
		userprops={
			category="Prop"
		}
	},
	
	
	
	
	{
		entity_name="Prop_barocamera08",
		type=COMPOUND,
		template_name="m7_barocamera",
		lt_grp=7,
		srt_grp=0,
		usr_flg=0,
		flags=LIT_DYNAMIC + LIT_AMBIENT,
		spatialprops={
			pos={
				-5.7,
				0,
				-9
			},
			orient={
				{-0.7071068,0,-0.7071068},
				{0,1,0},
				{0.7071068,0,-0.7071068}
			}
		},
		userprops={
			category="Prop"
		}
	},
	{
		entity_name="Prop_alien08",
		type=COMPOUND,
		template_name="m7_mole",
		lt_grp=55,
		srt_grp=0,
		usr_flg=0,
		flags=LIT_DYNAMIC + LIT_AMBIENT,
		spatialprops={
			pos={
				-5.5,
				1.15,
				-8.8
			},
			orient={
				{-0.7071068,0,0.7071068},
				{0,1,0},
				{-0.7071068,0,-0.7071068}
			}
		},
		userprops={
			category="Prop"
		}
	},
	{
		entity_name="Prop_barocamera09",
		type=COMPOUND,
		template_name="m7_barocamera_tall",
		lt_grp=7,
		srt_grp=0,
		usr_flg=0,
		flags=LIT_DYNAMIC + LIT_AMBIENT,
		spatialprops={
			pos={
				-4.1,
				0,
				-10.6
			},
			orient={
				{-0.7071068,0,-0.7071068},
				{0,1,0},
				{0.7071068,0,-0.7071068}
			}
		},
		userprops={
			category="Prop"
		}
	},
	{
		entity_name="Prop_alien09",
		type=COMPOUND,
		template_name="m7_elon",
		lt_grp=53,
		srt_grp=0,
		usr_flg=0,
		flags=LIT_DYNAMIC + LIT_AMBIENT,
		spatialprops={
			pos={
				-4.1,
				0,
				-10.6
				
			},
			orient={
				{0.7071068,0,-0.7071068},
				{0,1,0},
				{0.7071068,0,0.7071068}
			}
		},
		userprops={
			category="Prop"
		}
	},
	{
		entity_name="Prop_barocamera10",
		type=COMPOUND,
		template_name="m7_barocamera_tall",
		lt_grp=7,
		srt_grp=0,
		usr_flg=0,
		flags=LIT_DYNAMIC + LIT_AMBIENT,
		spatialprops={
			pos={
				-2.5,
				0,
				-12.2
			},
			orient={
				{-0.7071068,0,-0.7071068},
				{0,1,0},
				{0.7071068,0,-0.7071068}
			}
		},
		userprops={
			category="Prop"
		}
	},
	{
		entity_name="Char_monkeyking",
		type=DEFORMABLE,
		template_name="m07_monkeyking",
		lt_grp=54,
		srt_grp=0,
		usr_flg=0,
		flags=LIT_DYNAMIC + LIT_AMBIENT,
		spatialprops={
			pos={
				-2.4,
				0,
				-12.0
			},
			orient={
				{-0.7071068,0,0.7071068},
				{0,1,0},
				{-0.7071068,0,-0.7071068}
			}
		},
		compoundprops={
			floor_height=0
		},
		userprops={
			category="Character"
		}
	},


	
	
	{
		entity_name="Prop_alien01",
		type=COMPOUND,
		template_name="m7_facehugger",
		lt_grp=15,
		srt_grp=0,
		usr_flg=0,
		flags=LIT_DYNAMIC + LIT_AMBIENT,
		spatialprops={
			pos={
				2.8,
				1.3,
				2.32
			},
			orient={
				{0,0,-1},
				{0,1,0},
				{1,0,0}
			}
		},
		userprops={
			category="Prop"
		}
	},
	
	
	{
		entity_name="LIGHT_barocamera_inside01",
		type=LIGHT,
		template_name="",
		lt_grp=5,
		srt_grp=0,
		usr_flg=0,
		spatialprops={
			pos={0,10,0 },
			orient={
				{0,0,-1},
				{0,1,0},
				{1,0,0}
			}
		},
		lightprops={
			on=Y,
			color={
				255,
				255,
				255
			},
			diffuse={
				0.9,
				1,
				0
			},
			specular={
				0,
				0,
				0
			},
			ambient={
				1,
				0.5,
				0.25
			},
			direction={
				0,
				-0.8,
				-0.2
			},
			range=150555,
			cutoff=30,
			type=L_DIRECT,
			theta=26.999985,
			atten={
				1,
				0,
				0.003
			}
		}
	},
	{
		entity_name="LIGHT_barocamera_inside02",
		type=LIGHT,
		template_name="",
		lt_grp=15,
		srt_grp=0,
		usr_flg=0,
		spatialprops={
			pos={0,10,0 },
			orient={
				{0.7071068,0,-0.7071068},
				{0,1,0},
				{0.7071068,0,0.7071068}
			}
		},
		lightprops={
			on=Y,
			color={
				255,
				255,
				255
			},
			diffuse={
				0.4,
				0.5,
				0
			},
			specular={
				0,
				0,
				0
			},
			ambient={
				0.5,
				0.25,
				0
			},
			direction={
				0,
				0,
				1
			},
			range=150555,
			cutoff=30,
			type=L_DIRECT,
			theta=26.999985,
			atten={
				1,
				0,
				0.003
			}
		}
	},
	{
		entity_name="LIGHT_barocamera_objects",
		type=LIGHT,
		template_name="",
		lt_grp=6,
		srt_grp=0,
		usr_flg=0,
		spatialprops={
			pos={0,1,0 },
			orient={
				{0,0,-1},
				{0,1,0},
				{1,0,0}
			}
		},
		lightprops={
			on=Y,
			color={
				255,
				255,
				255
			},
			diffuse={
				0.2,
				0.2,
				0.5
			},
			specular={
				0,
				0,
				0
			},
			ambient={
				0.3,
				0.3,
				0.2
			},
			direction={
				0.2,
				0,
				-0.5
			},
			range=150555,
			cutoff=30,
			type=L_DIRECT,
			theta=26.999985,
			atten={
				1,
				0,
				0.003
			}
		}
	},
	{
		entity_name="LIGHT_barocamera_objects02",
		type=LIGHT,
		template_name="",
		lt_grp=7,
		srt_grp=0,
		usr_flg=0,
		spatialprops={
			pos={0,15,0 },
			orient={
				{1,0,0},
				{0,1,0},
				{0,0,1}
			}
		},
		lightprops={
			on=Y,
			color={
				255,
				255,
				255
			},
			diffuse={
				0.5,
				0.5,
				0.9
			},
			specular={
				0,
				1,
				0
			},
			ambient={
				0.9,
				0.3,
				0.0
			},
			direction={
				0.2,
				0,
				-0.5
			},
			range=5000,
			cutoff=30,
			type=L_DIRECT,
			theta=26.999985,
			atten={
				1,
				0,
				0.003
			}
		}
	},

	
	
	
	
	
	
	{
		entity_name="LIGHT_barocamera_inside_samus",
		type=LIGHT,
		template_name="",
		lt_grp=50,
		srt_grp=0,
		usr_flg=0,
		spatialprops={
			pos={0,10,0 },
			orient={
				{-0.7071068,0,-0.7071068},
				{0,1,0},
				{0.7071068,0,-0.7071068}
			}
		},
		lightprops={
			on=Y,
			color={
				255,
				255,
				255
			},
			diffuse={
				0.9,
				1,
				0
			},
			specular={
				0,
				0,
				0
			},
			ambient={
				0.8,
				0.5,
				0.5
			},
			direction={
				-0.5,
				-0.5,
				0
			},
			range=150555,
			cutoff=30,
			type=L_DIRECT,
			theta=26.999985,
			atten={
				1,
				0,
				0.003
			}
		}
	},
	{
		entity_name="LIGHT_barocamera_inside_jarjar",
		type=LIGHT,
		template_name="",
		lt_grp=51,
		srt_grp=0,
		usr_flg=0,
		spatialprops={
			pos={0,10,0 },
			orient={
				{-0.7071068,0,-0.7071068},
				{0,1,0},
				{0.7071068,0,-0.7071068}
			}
		},
		lightprops={
			on=Y,
			color={
				255,
				255,
				255
			},
			diffuse={
				0.9,
				1,
				0
			},
			specular={
				0,
				0,
				0
			},
			ambient={
				0.8,
				0.2,
				0.1
			},
			direction={
				1,
				0,
				0
			},
			range=150555,
			cutoff=30,
			type=L_DIRECT,
			theta=26.999985,
			atten={
				1,
				0,
				0.003
			}
		}
	},
	{
		entity_name="LIGHT_barocamera_inside_olaf",
		type=LIGHT,
		template_name="",
		lt_grp=52,
		srt_grp=0,
		usr_flg=0,
		spatialprops={
			pos={0,10,0 },
			orient={
				{0,0,-1},
				{0,1,0},
				{1,0,0}
			}
		},
		lightprops={
			on=Y,
			color={
				255,
				255,
				255
			},
			diffuse={
				0.9,
				1,
				0
			},
			specular={
				0,
				0,
				0
			},
			ambient={
				0.5,
				0.5,
				0.25
			},
			direction={
				0,
				-0.5,
				-0.5
			},
			range=150555,
			cutoff=30,
			type=L_DIRECT,
			theta=26.999985,
			atten={
				1,
				0,
				0.003
			}
		}
	},
	{
		entity_name="LIGHT_barocamera_inside_elon",
		type=LIGHT,
		template_name="",
		lt_grp=53,
		srt_grp=0,
		usr_flg=0,
		spatialprops={
			pos={0,10,0 },
			orient={
				{0.7071068,0,-0.7071068},
				{0,1,0},
				{0.7071068,0,0.7071068}
			}
		},
		lightprops={
			on=Y,
			color={
				255,
				255,
				255
			},
			diffuse={
				0.6,
				0.6,
				0
			},
			specular={
				0,
				0,
				0
			},
			ambient={
				0.7,
				0.5,
				0.2
			},
			direction={
				-1,0,0
			},
			range=150555,
			cutoff=30,
			type=L_DIRECT,
			theta=26.999985,
			atten={
				1,
				0,
				0.003
			}
		}
	},
	{
		entity_name="LIGHT_barocamera_inside_monkeyking",
		type=LIGHT,
		template_name="",
		lt_grp=54,
		srt_grp=0,
		usr_flg=0,
		spatialprops={
			pos={0,10,0 },
			orient={
				{-0.7071068,0,0.7071068},
				{0,1,0},
				{-0.7071068,0,-0.7071068}
			}
		},
		lightprops={
			on=Y,
			color={
				255,
				255,
				255
			},
			diffuse={
				0.9,
				1,
				0
			},
			specular={
				0,
				0,
				0
			},
			ambient={
				0.2,
				0.3,
				0.6
			},
			direction={
				-1,0,0
			},
			range=150555,
			cutoff=30,
			type=L_DIRECT,
			theta=26.999985,
			atten={
				1,
				0,
				0.003
			}
		}
	}
'''

STATIC_EVENTS = '''
	{
		0,
		START_MOTION,
		{"Char_monkeyking"},
		{animation="Sc_MLBODY_STND_IDLE_BIG_000LV_xa_05",
		 duration=0.1, time_scale=1, weight=1, heading=-1, event_flags=2}
	}

'''


class CollectionStatic(StaticEntity):
    CONTENT = STATIC_ENTITIES


class CollectionEvent(StaticEvent):
    CONTENT = STATIC_EVENTS


class PDA(Prop):
    COMPOUND_TEMPLATE_NAME = 'pda'


class CollectionScene(Scene):
    DUMP_FILE = 'br_cambridge_trader'

    def action(self):
        main_group = self.get_group(MAIN)

        CollectionStatic(root=self, name="collection_statics")
        CollectionEvent(root=self, group=MAIN)
        pda = PDA(root=self, name='the_pda', init_point=self.DEFAULT_POINT_NAME, light_group=0)

        Light(root=self, name='ROOMA', point_name='light1', light_group=0, diffuse=[0.3, 0.4, 0.55],
              ambient=[0, 0, 0], direction=[0, 0, -1], light_type=L_POINT, range=15)

        cam_greet = StaticCamera(root=self, name='cam_greet', fov=12)
        cam_trent = StaticCamera(root=self, name='cam_trent', fov=15)
        cam_trent_alt = StaticCamera(root=self, name='cam_trent_alt', fov=14)
        cam_monkey = StaticCamera(root=self, name='cam_monkey', fov=16)
        cam_jack = StaticCamera(root=self, name='cam_jack', fov=13)
        cam_darcy = StaticCamera(root=self, name='cam_darcy', fov=15)
        cam_darcy_alt = StaticCamera(root=self, name='cam_darcy_alt', fov=13)
        # cam_char2 = StaticCamera(root=self, name='cam_char2', fov=18)

        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='trent', rotate_from_quat=True,
                           camera=cam_trent, anim_sequence=sequence.SEQUENCE_MALE_STAND_FSTHIPB_CROSS)
        jack = Character(root=self, actor=actors.JackRazorBarber, light_group=0, init_point='jack', rotate_from_quat=True,
                           camera=cam_trent, anim_sequence=sequence.SEQUENCE_MALE_STAND_RHAND_ALT2)
        darcy = Character(root=self, actor=actors.Darcy, light_group=0, init_point='darcy', rotate_from_quat=True,
                           camera=cam_trent, anim_sequence=sequence.SEQUENCE_MALE_STAND_RHAND_ALT2)

        darcy.idle(group=MAIN)
        trent.idle(group=MAIN)
        trent.motion(group=MAIN, duration=1, anim=Male.Sc_MLHAND_HNEUT_PDA_LEFT_000LV_00, time_scale=0.8)
        jack.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_FSTHIPB_HOLD_000LV_XA_02)

        ConnectHardpointEvent(root=self, group=MAIN, target_name=pda.name, parent_name=trent.name,
                              duration=61, target_hardpoint="Hp_LHand_PDA",
                              parent_hardpoint="HpLeftConnect")

        mrk_trent = trent.get_stand_marker('trent')
        mrk_darcy = darcy.get_stand_marker('darcy')
        mrk_jack = jack.get_stand_marker('jack')
        mrk_monkey = self.get_automarker_name('mrk_monkey')
        mrk_trent2 = self.get_automarker_name('mrk_trent2')
        mrk_darcy2 = self.get_automarker_name('mrk_darcy2')

        darcy.move_head_ik(group=MAIN, target_name=mrk_jack, immediately=True)
        trent.move_head_ik(group=MAIN, target_name=mrk_monkey, immediately=True)



        # darcy.start_head_ik(group=MAIN, duration=1000)
        # darcy.move_head_ik(group=MAIN, target_name=mrk_trent, immediately=True)
        #
        #
        # MoveFastEvent(root=self, group=MAIN, object_name=darcy.name, target_name=self.get_automarker_name('darcy2'))
        # cam_darcy_alt.set(group=MAIN)
        #
        # darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, trans_time=1, time_scale=0.6)
        #
        # darcy.facial(group=MAIN, index=120, auto_lip=True)
        #
        # darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, trans_time=1, time_scale=0.6)
        #
        # darcy.facial(group=MAIN, index=130, auto_lip=True)
        #
        #
        #
        #
        # main_group.append_time(5)
        #
        # return

        cam_greet.set(group=MAIN)
        cam_greet.move_cam(group=MAIN, index=2, duration=10, smooth=True, time_delay=0)

        main_group.append_time(1)


        jack.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_TURN_270LV_XA_04, trans_time=1, time_delay=1, time_scale=0.8)

        main_group.append_time(1)
        jack.facial(group=MAIN, index=10, auto_lip=True)

        darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_UNCRSS_ARMS_000LV_XA_03, time_scale=0.9)

        cam_trent.set(group=MAIN)
        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_DEALR_PDA_000LV_XA_09, start_time=2, time_scale=0.8)
        trent.facial(group=MAIN, index=20, auto_lip=True)

        darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_TURN_045LV_XA_03, trans_time=1, time_delay=-1, time_scale=0.8)
        darcy.facial(group=MAIN, index=30, auto_lip=True)

        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_TURN_090LV_XA_02, time_scale=0.6, trans_time=1, time_delay=-1)

        main_group.append_time(0.5)



        cam_jack.set(group=MAIN)

        jack.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, trans_time=1, time_scale=0.6)

        jack.facial(group=MAIN, index=40, auto_lip=True)



        RotateAxisEvent(root=self, group=MAIN, object_name=darcy.name, angle=-30, duration=0.1, smooth=True, time_delay=-1)
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=-30, duration=0.1, smooth=True)

        cam_darcy.set(group=MAIN)

        darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, trans_time=1, time_scale=0.6)

        darcy.start_head_ik(group=MAIN, duration=1000)

        darcy.facial(group=MAIN, index=50, auto_lip=True)
        darcy.move_head_ik(group=MAIN, target_name=mrk_monkey, duration=3, smooth=True)
        darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_TURN_315LV_XA_03, trans_time=1, time_scale=0.6)



        cam_monkey.set(group=MAIN)
        cam_monkey.move_cam(group=MAIN, index=2, duration=20, smooth=True, time_delay=0)

        trent.start_head_ik(group=MAIN, duration=1000)

        trent.facial(group=MAIN, index=60, auto_lip=True)

        darcy.move_head_ik(group=MAIN, target_name=mrk_trent2, duration=2, smooth=True)
        trent.move_head_ik(group=MAIN, target_name=mrk_darcy, duration=2, smooth=True, time_delay=2)

        darcy.facial(group=MAIN, index=70, auto_lip=True)
        darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, trans_time=1, time_scale=0.6)
        trent.facial(group=MAIN, index=80, auto_lip=True)


        cam_jack.set(group=MAIN)

        jack.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, trans_time=1, time_scale=0.6)
        jack.facial(group=MAIN, index=90, auto_lip=True)

        trent.move_head_ik(group=MAIN, target_name=mrk_jack, duration=3, smooth=True, time_delay=-1)
        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_TURN_270LV_XA_04, time_scale=0.6, trans_time=1, time_delay=-3)

        cam_trent_alt.set(group=MAIN)

        trent.facial(group=MAIN, index=100, auto_lip=True)

        darcy.start_head_ik(group=MAIN, duration=1000)
        darcy.move_head_ik(group=MAIN, target_name=mrk_trent, immediately=True)

        MoveFastEvent(root=self, group=MAIN, object_name=darcy.name, target_name=self.get_automarker_name('darcy2'))
        darcy.idle(group=MAIN)


        cam_jack.set(group=MAIN)

        jack.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, trans_time=1, time_scale=0.6)
        jack.facial(group=MAIN, index=110, auto_lip=True)


        cam_darcy_alt.set(group=MAIN)

        darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, trans_time=1, time_scale=0.6)

        darcy.facial(group=MAIN, index=120, auto_lip=True)

        darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, trans_time=1, time_scale=0.6)

        darcy.facial(group=MAIN, index=130, auto_lip=True)


        trent.move_head_ik(group=MAIN, target_name=mrk_darcy2, duration=2, smooth=True, time_delay=-1)


        cam_trent_alt.set(group=MAIN)

        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, trans_time=1, time_scale=0.6)

        trent.facial(group=MAIN, index=140, auto_lip=True)

        main_group.append_time(1)
