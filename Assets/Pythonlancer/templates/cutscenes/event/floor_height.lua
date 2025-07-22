{
    {{ time }},
    START_FLR_HEIGHT_ANIM,
    {
        "{{ char }}"
    },
    {
        duration = {{ duration }},
        target_type = ROOT,
        floor_height = {{ floor_height }}
        {% if smooth %}
        ,
        param_curve={CLSID="FreeFormPCurve",points={ {0,0,0,0},{1,1,0,0} } },
        pcurve_period=-1000
        {% endif %}
    }
}
