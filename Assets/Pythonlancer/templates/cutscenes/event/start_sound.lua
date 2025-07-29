{
    {{ time }},
    START_SOUND,
    {"{{ sound }}"},
    {
        duration={{ duration }}
        {% if loop %}
        , flags=LOOP
        {% endif %}
    }
}
