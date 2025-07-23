{
    entity_name="{{ name }}",
    type=MARKER,
    template_name="",lt_grp=0,srt_grp=0,usr_flg=0,
    spatialprops={
        pos={ {{ point.pos }} },
        orient={ {{ point.matrix }} }
    }
}
