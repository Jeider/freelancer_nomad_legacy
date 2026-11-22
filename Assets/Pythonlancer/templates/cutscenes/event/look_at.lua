{
    {{ time }},
    ATTACH_ENTITY,
    {
        "{{ point_name }}",
        "{{ focus_name }}"
    },
    {
        duration={{ duration }}, offset={0,0,0},
        up={{ up }}, front={{ front }}, target_part="{{ target_part }}", target_type={{ target_type }}, flags=LOOK_AT
    }
}
