{
    {{ time }},
    START_CAMERA_PROP_ANIM,
    {
        "{{ name }}"
    },
    {
        duration={{ duration }},
        cameraprops={
            fovh={{ fov }}
        }
        {% if smooth %}
        ,
        param_curve={CLSID="FreeFormPCurve",points={ {0,0,0,0},{1,1,0,0} } },
        pcurve_period=-1000
        {% endif %}
    }
}