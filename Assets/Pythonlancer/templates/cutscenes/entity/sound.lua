{
    entity_name="{{ name }}",
    template_name="{{ sound }}",
    type=SOUND,lt_grp=0, srt_grp=0, usr_flg=0,
    {% if flags %} flags={{ flags }}, {% endif %}
    spatialprops={
        pos={0,0,0},
        orient={
            {1,0,0},{0,1,0},{0,0,1}
        }
    },
    audioprops={attenuation={{ attenuation }},pan=0,dmin={{ dmin }},dmax={{ dmax }},ain=360,aout=360,atout=0,rmix=0},
    userprops={category="Audio"  {% if priority %}, Priority="{{ priority }}" {% endif %} }
}
