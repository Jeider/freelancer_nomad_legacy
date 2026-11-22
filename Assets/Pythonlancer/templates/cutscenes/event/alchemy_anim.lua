{
    {{ time }},
    START_PSYS_PROP_ANIM,
    {
        "{{ name }}"
    },
    {
        duration={{ duration }},
        psysprops={
            sparam={{ sparam }}
        }
        {% if smooth %}, param_curve={CLSID="FreeFormPCurve",points={ {0,0,0,0},{1,1,0,0} }}, pcurve_period=-1000{% endif %}
    }
}
