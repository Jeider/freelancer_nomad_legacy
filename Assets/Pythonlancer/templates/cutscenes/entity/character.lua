{
    entity_name="{{ name }}",
    type=DEFORMABLE,
    template_name="{{ template_name }}",
    lt_grp={{ light_group }},
    srt_grp=0,
    usr_flg=0,
    flags=LIT_DYNAMIC,
    spatialprops={
        pos={
            {{ init_pos }}
        },
        orient={ {{ init_matrix }} }
    },
    compoundprops={
        floor_height=0
    },
    userprops={
        Actor="{{ actor }}",
        category="Character"
    }
}
