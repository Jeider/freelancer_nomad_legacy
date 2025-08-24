{
    entity_name="{{ name }}",
    type=DEFORMABLE,
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
    compoundprops={
        floor_height={{ floor_height }}
    },
    userprops={
        Actor="{{ actor }}",
        category="Character"
    }
}
