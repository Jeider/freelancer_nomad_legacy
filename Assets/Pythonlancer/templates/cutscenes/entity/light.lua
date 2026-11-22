{
    entity_name="{{ name }}",
    type=LIGHT,
    template_name="",
    lt_grp={{ light_group }},
    srt_grp=0,
    usr_flg=0,
    {% if is_reference %} flags=REFERENCE, {% elif hidden %} flags=HIDDEN, {% endif %}
    spatialprops={
        pos={ {{ point.pos }} },
        orient={
            {% if rotate_from_quat %}{{ point.matrix_from_quat }}{% else %}{1,0,0},{0,1,0},{0,0,1}{% endif %}
        }
    },
    lightprops={
        on={% if on %}Y{% else %}N{% endif %},
        color={
            {{ color }}
        },
        diffuse={
            {{ diffuse }}
        },
        specular={
            {{ specular }}
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
            {{ attenuation }}
        }
    }
}
