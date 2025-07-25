{
    0,
    START_LIGHT_PROP_ANIM,
    {
        "{{ name }}"
    },
    {
        duration={{ duration }},
        lightprops={
            {{ light_changes }}
        }
        {% if smooth %}
        ,
        param_curve={CLSID="FreeFormPCurve",points={ {0,0,0,0},{1,1,0,0} } },
        pcurve_period=-1000
        {% endif %}

},