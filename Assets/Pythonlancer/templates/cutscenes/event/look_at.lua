{
    {{ time }},
    ATTACH_ENTITY,
    {
        "{{ point.name }}",
        "{{ focus.name }}"
    },
    {
        duration={{ duration }}, offset={0,0,0},
        up=Y_AXIS, front=NEG_Z_AXIS, target_part="", target_type=ROOT, flags=LOOK_AT
    }
}
