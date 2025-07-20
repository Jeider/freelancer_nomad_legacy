duration=500

entities={
	{
		entity_name="Scene_m06_dread_mount",
		type=SCENE,
		template_name="",
		template_id=0,
		spatialprops={
			pos={0,0,0},
			orient={
				{1,0,0},
				{0,1,0},
				{0,0,1}
			}
		},
		up=Y_AXIS,
		front=Z_AXIS,
		ambient={255,255,255}
	},

	{
		entity_name="Monitor_1",
		type=MONITOR,
		template_name="",
		template_id=0
	},


       {{ sound.get_thorn() }}

    ,

	{
		entity_name="Char_the",
		type=DEFORMABLE,
		template_name="{{ sound.thorn_costume }}",
		lt_grp=0,
		srt_grp=0,
		usr_flg=0,
		flags=LIT_DYNAMIC,
		spatialprops={
			pos={
				-11, 0, -11
			},
			orient={
				{0.7071068,0,-0.7071068},
				{0,1,0},
				{0.7071068,0,0.7071068}
			}
		},
		compoundprops={
			floor_height=0
		},
		userprops={
			Actor="Char_the_actor",
			category="Character"
		}
	},



	{
		entity_name="cam_dbg_trent",
		type=CAMERA,
		template_name="",
		lt_grp=0,
		srt_grp=0,
		usr_flg=0,
		flags=HIDDEN,
		spatialprops={
			pos={
			    -- -8, 3, -11

				-11.8, 1.7, -11.7


				-- -13.8, 1.7, -9.7
			},
			orient={
				{1,0,0},
				{0,1,0},
				{0,0,1}

			}
		},
		cameraprops={
			fovh=22,
			hvaspect=1.85,
			nearplane=0.2,
			farplane=5000
		}
	},
	{
		entity_name="cam_dbg_trent_marker",
		type=MARKER,
		template_name="",
		template_id=0,
		spatialprops={
			pos={
				-11, 1.65, -11



				-- -11, 1.3, -13
			},
			orient={
				{1,0,0},
				{0,1,0},
				{0,0,1}
			}
		},
	},


	{
		entity_name="cam_hatcher",
		type=CAMERA,
		template_name="",
		lt_grp=0,
		srt_grp=0,
		usr_flg=0,
		flags=HIDDEN,
		spatialprops={
			pos={
				-11.8, 1.65, -11.7
			},
			orient={
				{1,0,0},
				{0,1,0},
				{0,0,1}

			}
		},
		cameraprops={
			fovh=13,
			hvaspect=1.85,
			nearplane=0.2,
			farplane=5000
		}
	},
	{
		entity_name="cam_hatcher_marker",
		type=MARKER,
		template_name="",
		template_id=0,
		spatialprops={
			pos={
				-11, 1.55, -11
			},
			orient={
				{1,0,0},
				{0,1,0},
				{0,0,1}
			}
		},
	},

}

events={
	{
		0,
		ATTACH_ENTITY,
		{
			"cam_dbg_trent",
			"cam_dbg_trent_marker"
		},
		{
			duration=1,
			offset={0,0,0},
			up=Y_AXIS,
			front=NEG_Z_AXIS,
			target_part="",
			target_type=ROOT,
			flags=LOOK_AT
		}
	},
	{
		0,
		ATTACH_ENTITY,
		{
			"cam_hatcher",
			"cam_hatcher_marker"
		},
		{
			duration=300,
			offset={0,0,0},
			up=Y_AXIS,
			front=NEG_Z_AXIS,
			target_part="",
			target_type=ROOT,
			flags=LOOK_AT
		}
	},


	{
		0,
		SET_CAMERA,
		{
			"Monitor_1",
			"{{ camera }}"
		}
	},

	{
		0,
		START_MOTION,
		{"Char_the"},
		{animation="{{ stand_anim }}",
		 duration=15, time_scale=1, weight=1, heading=-1}
	},

	{{ sound.thorn_play }}


	{
		-- LIP
		0,
		START_MOTION,
		{"Char_the"},
		{animation="{{ anim }}", duration=10, time_scale=1, trans_time=0.25,  weight=1, heading=-1}
	},




}
