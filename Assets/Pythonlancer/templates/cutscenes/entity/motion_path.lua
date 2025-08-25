{
    entity_name="{{ name }}",
    type=MOTION_PATH,
    template_name="",
    template_id=0,
    spatialprops={
        pos={
            {{ init_pos }}
        },
        orient={ {{ init_matrix }} }
    },
    pathprops={
        path_type="CV_CROrientationSplinePath",
        path_data="OPEN, {{ path_data }}"
    }
}
