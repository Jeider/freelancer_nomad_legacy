{
    {{ time }},
    START_SPATIAL_PROP_ANIM,
    {
        "{{ object_name }}",
        "{{ target_name }}"
    },
    {
        duration={{ duration }},
        target_part="",
        target_type=ROOT,
        spatialprops={
            pos={ 0,0,0 },
            q_orient={ 1,0,0,0 }
        }
        {% if smooth %}
        ,
        param_curve={CLSID="FreeFormPCurve",points={ {0,0,0,0},{1,1,0,0} } },
        pcurve_period=-1000
        {% endif %}
    }
}
