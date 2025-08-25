{
    entity_name="{{ name }}",
    type=CAMERA,
    template_name="", lt_grp=0, srt_grp=0, usr_flg=0,
    flags=HIDDEN,
    spatialprops={
        pos={ {{ point.pos }} },
        orient={ {{ point.matrix }} }
    },
    cameraprops={
        fovh={{ fov }},
        hvaspect=1.85,
        nearplane=0.2,
        farplane={{ farplane }}
    }
}
