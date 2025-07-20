duration={{ scene_duration }}

entities={
	{
		entity_name="Scene_{{ scene_name }}",
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
		ambient={
		    {{ scene_ambient.0 }},
		    {{ scene_ambient.1 }},
		    {{ scene_ambient.2 }}
		}
	},

	{
		entity_name="Monitor_1",
		type=MONITOR,
		template_name="",
		template_id=0
	},
	{
		entity_name="offscreen",
		type=MARKER,
		template_name="",
		lt_grp=0,
		srt_grp=0,
		usr_flg=0,
		flags=HIDDEN,
		spatialprops={pos={-10000000,-10000,0},orient={ {1,0,0},{0,1,0},{0,0,1} } },
	},

	{
		entity_name="offscreen_back",
		type=MARKER,
		template_name="",
		lt_grp=0,
		srt_grp=0,
		usr_flg=0,
		flags=HIDDEN,
		spatialprops={pos={0,-10000,-10000000},orient={ {1,0,0},{0,1,0},{0,0,1} } },
	},

	{{ script_sounds }}

	,

	{{ entities }}
}

events={

    {{ events }}

}
