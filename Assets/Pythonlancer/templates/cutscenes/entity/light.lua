{
    entity_name="{{ name }}",
    type=LIGHT,
    template_name="",
    lt_grp={{ light_group }},
    srt_grp=0,
    usr_flg=0,
    {% if is_reference %} flags=REFERENCE, {% endif %}
    spatialprops={
        pos={ {{ point.pos }} },
        orient={
            {1,0,0},
            {0,1,0},
            {0,0,1}
        }
    },
    lightprops={
        on={% if on %}Y{% else %}N{% endif %},
        color={
            255,
            255,
            255
        },
        diffuse={
            {{ diffuse }}
        },
        specular={
            0,
            0,
            0
        },
        ambient={
            {{ ambient }}
        },
        direction={
            {{ direction }}
        },
        range={{ range }},
        cutoff={{ cutoff }},
        type={{ light_type }},
        theta={{ theta }},
        atten={
            1,
            0,
            0.003
        }
    }
}
