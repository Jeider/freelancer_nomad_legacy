{
    0,
    ATTACH_ENTITY,
    {
        "{{ target_name }}",
        "{{ parent_name }}"
    },
    {
        duration={{ duration }},
        offset={
            0,
            0,
            0
        },
        up=Y_AXIS,
        front=NEG_Z_AXIS,
        target_part="{{ target_part }}",
        target_type={{ target_type }},
        flags={{ flags }}
    }
}
