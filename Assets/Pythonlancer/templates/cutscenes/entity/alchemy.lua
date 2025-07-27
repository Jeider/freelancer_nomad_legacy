{
    entity_name="{{ name }}",
    type=PSYS,
    template_name="{{ particles }}",
    lt_grp=0,
    srt_grp=0,
    usr_flg=0,
    flags=HIDDEN + LIT_DYNAMIC + LIT_AMBIENT,
    spatialprops={
        pos={
            {{ point.pos }}
        },
        orient={
            {
                1,
                0,
                0
            },
            {
                0,
                1,
                0
            },
            {
                0,
                0,
                1
            }
        }
    },
    psysprops={
        sparam={{ sparam }}
    }
}
