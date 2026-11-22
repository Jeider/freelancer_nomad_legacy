{
    entity_name="{{ name }}",
    type=PSYS,
    template_name="{{ particles }}",
    lt_grp={{ light_group }},
    srt_grp={{ sort_group }},
    usr_flg=0,
    flags={{ flags }},
    spatialprops={
        pos={
            {{ point.pos }}
        },
        orient={
            {{ point.matrix }}
        }
    },
    psysprops={
        sparam={{ sparam }}
    }
}
