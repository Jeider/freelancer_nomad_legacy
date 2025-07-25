{
    entity_name="{{ name }}",
    type=DEFORMABLE,
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
    compoundprops={
        floor_height={{ floor_height }}
    },
    userprops={
        Actor="{{ actor }}",
        category="Character"
    }
}
