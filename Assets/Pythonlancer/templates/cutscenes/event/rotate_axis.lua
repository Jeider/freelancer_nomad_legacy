{
    {{ time }},
    START_SPATIAL_PROP_ANIM,
    {
        "{{ object_name }}"
    },
    {
        duration={{ duration }},
        target_type=ROOT,
        spatialprops={
            axisrot={
                {{ angle }},
                {{ axis }}
            }
        }
        {% if smooth %}
        ,
        param_curve={CLSID="FreeFormPCurve",points={ {0,0,0,0},{1,1,0,0} } },
        pcurve_period=-1000
        {% endif %}
    }
}
