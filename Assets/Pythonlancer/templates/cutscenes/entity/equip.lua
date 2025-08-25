{
    entity_name="{{ name }}",
    type=COMPOUND,
    template_name="{{ template_name }}",
    lt_grp={{ light_group }},
    srt_grp={{ srt_grp }},
    usr_flg={{ usr_flg }},
    flags={{ light_flags }},
    spatialprops={
        pos={
            {{ init_pos }}
        },
        orient={ {{ init_matrix }} }
    },
    userprops={
        category="Equipment"
    }
}
