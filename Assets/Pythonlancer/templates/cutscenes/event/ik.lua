{
    {{ time }},
    START_IK,
    {
        "{{ char_name }}",
        "{{ target_name }}"
    },
    {
        duration=20,
        end_effector="{{ end_effector }}", transition_duration={{ transition_duration }},
        target_part="{{ target_part }}", target_type={{ target_type }},
        count_to_root=1, damping=1, up=NEG_Y_AXIS, front=Z_AXIS, point_at=1, move_to=0, event_flags=128
    }
}
