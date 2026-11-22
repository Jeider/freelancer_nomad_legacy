{
    {{ time }},
    ATTACH_ENTITY,
    {
        "{{ target_name }}",
        "{{ parent_name }}"
    },
    {
        duration={{ duration }},
        offset={
            {{ offset_x }},
            {{ offset_y }},
            {{ offset_z }}
        },
        up={{ up }},
        front={{ front }},
        target_part="{{ target_part }}",
        target_type={{ target_type }},
        flags={{ flags }}
    }
}
