{
    {{ time }},
    START_MOTION,
    {"{{ object_name }}"},
    {animation="{{ anim }}",
     duration={{ duration }}, time_scale={{ time_scale }}, start_time={{ start_time }},
     weight=1, heading=-1 {% if loop %}, event_flags=2 {% endif %} }
}
