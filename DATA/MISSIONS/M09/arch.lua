duration = 25.125;

entities =
{

	{
		entity_name = "Scene_Untitled_2",
		type = SCENE,
		template_name = "",
		lt_grp = 0, srt_grp = 0, usr_flg = 0,
		spatialprops =
		{
			pos = { 0, 0, 0 },
			orient = { { 1, 0, 0 }, { 0, 1, 0 }, { 0, 0, 1 } }
		},
		up = Y_AXIS,
		front = Z_AXIS,
		ambient = { 128, 128, 128 }
	},

	{
		entity_name = "Cam_Static",
		type = CAMERA,
		template_name = "",
		lt_grp = 0, srt_grp = 0, usr_flg = 0,
		spatialprops =
		{
			pos = { -38140.75, 2737.364, 20685.66 },
			orient = { {  0.987197,  0.000000, -0.159504 },
					   {  0.067226,  0.906841,  0.416076 },
					   {  0.144644, -0.421472,  0.895231 } }
		},
		cameraprops =
		{
			fovh = 35,
			hvaspect = 1.85,
			nearplane = 0.2,
			farplane = 55000
		}
	},

	{
		entity_name = "Monitor",
		type = MONITOR,
		template_name = "",
		lt_grp = 0, srt_grp = 0, usr_flg = 0
	},

	{
		entity_name = "Cam_Static_New",
		type = CAMERA,
		template_name = "",
		lt_grp = 0, srt_grp = 0, usr_flg = 0,
		spatialprops =
		{
			pos = { -38018.02, 2853.075, 20439.26 },
			orient = { { -0.729156,  0.000000, -0.684348 },
					   { -0.194138,  0.958918,  0.206850 },
					   {  0.656233,  0.283684, -0.699201 } }
		},
		cameraprops =
		{
			fovh = 35,
			hvaspect = 1.85,
			nearplane = 0.2,
			farplane = 55000
		}
	},

	{
		entity_name = "Cam_Static_New_2",
		type = CAMERA,
		template_name = "",
		lt_grp = 0, srt_grp = 0, usr_flg = 0,
		spatialprops =
		{
			pos = { -37884.29, 2833.927, 20235.36 },
			orient = { { -0.754269,  0.000000, -0.656566 },
					   {  0.000641,  1.000000, -0.000737 },
					   {  0.656565, -0.000977, -0.754269 } }
		},
		cameraprops =
		{
			fovh = 35,
			hvaspect = 1.85,
			nearplane = 0.2,
			farplane = 55000
		}
	},

	{
		entity_name = "bw_fighter_1",
		type = COMPOUND,
		template_name = "bw_fighter",
		lt_grp = 0, srt_grp = 0, usr_flg = 0,
		flags = LIT_DYNAMIC,
		spatialprops =
		{
			pos = { -38155.64, 2759.344, 20598.75 },
			orient = { {  0.980096, -0.101684, -0.170508 },
					   {  0.198488,  0.518905,  0.831469 },
					   {  0.003931, -0.848763,  0.528760 } }
		},
		userprops =
		{
			category = "Spaceship",
		}
	},

	{
		entity_name = "Bw_Marker_1",
		type = MARKER,
		template_name = "",
		lt_grp = 0, srt_grp = 0, usr_flg = 0,
		spatialprops =
		{
			pos = { -38155.74, 2880.444, 20523.61 },
			orient = { {  0.980096, -0.101684, -0.170508 },
					   {  0.198488,  0.518905,  0.831469 },
					   {  0.003931, -0.848763,  0.528760 } }
		}
	},

	{
		entity_name = "Cam_Bruce_1",
		type = CAMERA,
		template_name = "",
		lt_grp = 0, srt_grp = 0, usr_flg = 0,
		spatialprops =
		{
			pos = { -37868.17, 2602.787, 20398.28 },
			orient = { { -0.477221,  0.404274, -0.780271 },
					   {  0.651056,  0.759014, -0.004932 },
					   {  0.590242, -0.510354, -0.625422 } }
		},
		cameraprops =
		{
			fovh = 35,
			hvaspect = 1.85,
			nearplane = 0.2,
			farplane = 55000
		}
	},

	{
		entity_name = "Cam_Static_Dock",
		type = CAMERA,
		template_name = "",
		lt_grp = 0, srt_grp = 0, usr_flg = 0,
		spatialprops =
		{
			pos = { -38129.47, 2766.08, 20285.64 },
			orient = { { -0.999877,  0.000000,  0.015715 },
					   { -0.001635,  0.994573, -0.104023 },
					   { -0.015630, -0.104036, -0.994451 } }
		},
		cameraprops =
		{
			fovh = 35,
			hvaspect = 1.85,
			nearplane = 0.2,
			farplane = 55000
		}
	},

	{
		entity_name = "Cam_Static_Dock_A",
		type = CAMERA,
		template_name = "",
		lt_grp = 0, srt_grp = 0, usr_flg = 0,
		spatialprops =
		{
			pos = { -38134.52, 2781.616, 20241.91 },
			orient = { { -0.997785,  0.000000,  0.066519 },
					   { -0.004027,  0.998166, -0.060404 },
					   { -0.066397, -0.060538, -0.995955 } }
		},
		cameraprops =
		{
			fovh = 35,
			hvaspect = 1.85,
			nearplane = 0.2,
			farplane = 55000
		}
	}
};

events =
{
	{
		0.000, SET_CAMERA, { "Monitor", "Cam_Static_New" }
	},

	{
		0.000, START_SPATIAL_PROP_ANIM, { "Cam_Static_New", "Cam_Static_New_2" },
		{
			duration = 15.000,
			target_part = "",
			target_type = ROOT,
			spatialprops =
			{
				pos = { -37884.29, 2833.927, 20235.36 },
				q_orient = { -0.754269, 0, -0.656566, 0.000641 }
			},
			param_curve =
			{
				CLSID = "FreeFormPCurve",
				points =
				{
					{  0.000000,  0.000000,  0.000000,  0.000000 },
					{  1.000000,  1.000000,  0.000000,  0.000000 },
				}
			},
			pcurve_period = -1000
		}
	},

	{
		15.000, SET_CAMERA, { "Monitor", "Cam_Static_Dock_A" }
	},

	{
		15.000, START_SPATIAL_PROP_ANIM, { "Cam_Static_Dock_A", "Cam_Static_Dock" },
		{
			duration = 10.312,
			target_part = "",
			target_type = ROOT,
			spatialprops =
			{
				pos = { -38129.47, 2766.08, 20285.64 },
				q_orient = { -0.999876, 0, 0.015715, -0.001635 }
			},
			param_curve =
			{
				CLSID = "FreeFormPCurve",
				points =
				{
					{  0.000000,  0.000000,  0.000000,  0.000000 },
					{  1.000000,  1.000000,  0.000000,  0.000000 },
				}
			},
			pcurve_period = -1000
		}
	}
};
