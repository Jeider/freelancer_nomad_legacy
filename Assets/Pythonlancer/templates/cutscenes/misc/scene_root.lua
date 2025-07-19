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

	{{ entities }}
}

events={

    {{ events }}

}
