{
    entity_name="{{ name }}",
    type=COMPOUND,
    template_name="{{ template_name }}",
    lt_grp={{ light_group }},
    srt_grp=0,
    usr_flg=0,
    flags={{ light_flags }},
    spatialprops={
        pos={
            {{ init_pos }}
        },
        orient={ {{ init_matrix }} }
    },
    userprops={
        category="Spaceship"
        {% if loadout %}
			, loadout="{{ loadout }}"
		{% endif %}
        {% if have_lights %}
			, running_lights="true"
		{% endif %}
    }
}
