{
    {{ time }},
    START_PATH_ANIMATION,
    {
        "{{ target_name }}",
        "{{ path_name }}"
    },
    {
        duration={{ duration }},
        start_percent={{ start_percent }},
        stop_percent={{ stop_percent }},
        offset={
            0,
            0,
            0
        },
        up=Y_AXIS,
        front=NEG_Z_AXIS,
        flags={{ flags }}

        {% if smooth %}
        ,
        param_curve={CLSID="FreeFormPCurve",points={ {0,0,0,0},{1,1,0,0} } },
        pcurve_period=-1000
        {% endif %}
    }
}
