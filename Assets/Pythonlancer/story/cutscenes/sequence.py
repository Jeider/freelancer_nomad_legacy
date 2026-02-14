from story.cutscenes.anim import Male, Female


SEQUENCE_MALE_STAND_CROSS = [
    [
        {'anim': Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, 'time_scale': 0.5}
    ],
    [
        {'anim': Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, 'time_scale': 0.5}
    ],

    # Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01
    # Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01


]

SEQUENCE_MALE_STAND_RHAND = [
    [
        {'anim': Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, 'time_scale': 0.5, 'trans_time': 0.5, 'time_delay': 0.25}
    ],
    [
        {'anim': Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, 'time_scale': 0.5, 'trans_time': 0.5, 'time_delay': 0.25}
    ],
    [
        {'anim': Male.Sc_MLBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, 'time_scale': 0.6, 'trans_time': 1, 'time_delay': 0.25},
        {'anim': Male.Sc_MLBODY_STND_CONV_RHND_CASL_000LV_xa_01, 'time_scale': 0.6, 'trans_time': 1, 'time_delay': 2.25, 'loop': True},
        {'anim': Male.Sc_MLBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_02, 'time_scale': 0.5, 'trans_time': 1, 'time_delay': 4.25},
    ],
    # [
    #     {'anim': Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, 'time_scale': 0.5, 'trans_time': 0.5}
    # ],
    # [
    #     {'anim': Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, 'time_scale': 0.5, 'trans_time': 0.5}
    # ],
    # [
    #     {'anim': Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, 'time_scale': 0.5, 'trans_time': 0.2}
    # ],
    # [
    #     {'anim': Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, 'time_scale': 0.5, 'trans_time': 0.2}
    # ],

    # Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01
    # Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01

#
    #
    #
    # '''
    #
    #     edison.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_STND_CONV_RHNDUP_TRNS_000LV_XA_01, time_scale=0.6, trans_time=1, time_delay=0)
    #     edison.motion(group=MAIN, duration=100, loop=True, anim=Male.Sc_MLBODY_STND_CONV_RHND_CASL_000LV_xa_01, time_scale=0.6, trans_time=1, time_delay=2)
    #     edison.motion(group=MAIN, duration=100, anim=Male.Sc_MLBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_02, time_scale=0.6, trans_time=0.5, time_delay=7)
    #
    # '''
]

SEQUENCE_FEMALE_STAND_CROSS = [
    [
        {'anim': Female.Sc_FMBODY_STND_CROSS_ARMS_000LV_xa_03, 'time_scale': 0.5}
    ],
    [
        {'anim': Female.Sc_FMBODY_STND_UNCRSS_ARMS_000LV_XA_03, 'time_scale': 0.5}
    ],
]
