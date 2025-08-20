{
    {{ time }},
    START_SOUND,
    {"{{ sound }}"},
    {
        duration={{ duration }}, start_time={{start_time}}
        {% if loop %}
        , flags=LOOP
        {% endif %}
    }
}
