import sys
from story import math

from tools.crc import crc32_hex_from_str
from tools import utf_xml




def mass_decode():
    utf_xml.UTF_XML.mass_decode_utf()


def mass_upgrade1():
    subfolder_filename = 'lod0-112.vms.xml'
    old_outside_material = 'om15_xxlarge'
    old_inside_material = 'om15_inside'
    old_wall_material = 'mat_o15_a'

    original_asteroid_name = 'om15'
    new_asteroid_name = 'tau37'

    new_outside_material = f'{new_asteroid_name}_xxlarge'
    new_inside_material = f'{new_asteroid_name}_inside'
    new_wall_material = f'{new_asteroid_name}_wall'

    old_mat1 = crc32_hex_from_str(old_outside_material)
    old_mat2 = crc32_hex_from_str(old_inside_material)
    old_mat3 = crc32_hex_from_str(old_wall_material)

    new_mat1 = crc32_hex_from_str(new_outside_material)
    new_mat2 = crc32_hex_from_str(new_inside_material)
    new_mat3 = crc32_hex_from_str(new_wall_material)

    subfile_changed_strings = [
        [old_mat1, new_mat1],
        [old_mat2, new_mat2],
        [old_mat3, new_mat3],
        [f'0x0{old_mat1[2:].upper()}', new_mat1],
        [f'0x0{old_mat2[2:].upper()}', new_mat2],
        [f'0x0{old_mat3[2:].upper()}', new_mat3],
        [f'0x{old_mat1[2:].upper()}', new_mat1],
        [f'0x{old_mat2[2:].upper()}', new_mat2],
        [f'0x{old_mat3[2:].upper()}', new_mat3],
    ]

    # print(subfile_changed_strings)
    # x = subfile_changed_strings
    # import pdb;pdb.set_trace()


    main_file_upgrades = [
        [
            f'UTFXML filename="{original_asteroid_name}',
            f'UTFXML filename="{new_asteroid_name}'
        ],
        [
            '.lod0-112.vms include="',
            f'_{new_asteroid_name}_edition.lod0-112.vms include="'
        ],
        [
            '.lod0-112.vms,',
            f'_{new_asteroid_name}_edition.lod0-112.vms,'
        ],

    ]

    sur_filename_upgrades = [
        [
            original_asteroid_name,
            new_asteroid_name
        ]
    ]

    utf_xml.XML_UTF.mass_encode_updated_xml(
        subfolder_filename,
        subfile_changed_strings,
        main_file_upgrades,
        sur_filename_upgrades,
    )


def mass_upgrade_rock():
    subfolder_filename = 'lod0-212.vms.xml'

    old_material1 = crc32_hex_from_str('detailmap_planet_frag')
    old_material2 = crc32_hex_from_str('detailmap_ast_rock02')

    original_asteroid_name = 'rock'
    new_asteroid_name = 'li_cal'

    new_material1 = crc32_hex_from_str(f'detailmap_{new_asteroid_name}_side')

    subfile_changed_strings = [
        [f'0x{old_material1[2:].upper()}', new_material1],
        [f'0x{old_material2[2:].upper()}', new_material1],
        [f'0x0{old_material1[2:].upper()}', new_material1],
        [f'0x0{old_material2[2:].upper()}', new_material1],
    ]

    vmeshs = ['lod0-112', 'lod0-212', 'lod1-112', 'lod1-212']

    main_file_upgrades = [
        [
            f'UTFXML filename="{original_asteroid_name}',
            f'UTFXML filename="{new_asteroid_name}'
        ],
        [
            '.3db',
            f'_{new_asteroid_name}.3db'
        ]
    ]

    for vmesh in vmeshs:
        main_file_upgrades.extend([
            [
                f'.{vmesh}.vms include="',
                f'_{new_asteroid_name}_edition.{vmesh}.vms include="'
            ],
            [
                f'.{vmesh}.vms,',
                f'_{new_asteroid_name}_edition.{vmesh}.vms,'
            ],
        ])
        subfile_changed_strings.append(
            [
                f'.{vmesh}.vms,',
                f'_{new_asteroid_name}_edition.{vmesh}.vms,'
            ]
        )

    sur_filename_upgrades = [
        [
            original_asteroid_name,
            new_asteroid_name
        ]
    ]

    utf_xml.XML_UTF.mass_encode_updated_xml(
        subfolder_filename,
        subfile_changed_strings,
        main_file_upgrades,
        sur_filename_upgrades,
    )


def mass_upgrade_fx():

    start = None
    max = 20

    ids_map = [
        11,
        12,
        13,

        21,
        22,
        23,

        31,
        32,
        33,

        41,
        42,
        43,

        51,
        52,
        53,

        # 15,
        # 16,
        # 17,
        #
        # 25,
        # 26,
        # 27,
        #
        # 35,
        # 36,
        # 37,
        #
        # 45,
        # 46,
        # 47,
        #
        # 55,
        # 56,
        # 57,
    ]

    i = start

    for item in ids_map:
        new_i = item

        root1 = 'empmissile'

        main_file_upgrades = [
            [
                f'{root1}{i:02d}' if i else root1,
                f'{root1}{new_i:02d}'
            ],
        ]

        utf_xml.XML_UTF.mass_encode_updated_xml(
            '',
            [],
            main_file_upgrades,
            [],
        )

        i = new_i



def mass_upgrade3():
    main_file_upgrades = [
        [
            f'ku_',
            f'dtr_'
        ],
    ]

    utf_xml.XML_UTF.mass_encode_updated_xml(
        [],
        [],
        main_file_upgrades,
        main_file_upgrades,
    )

def mass_upgrade44():
    pass
    # elite_256
    # elite_256B
    # elite_256LB
    # elite_256R
    # elite_256_2side
    # L_glass
    # L_wing_128
    # metal03

def mass_upgrade_li():
    subfolder_filename = 'lod0-212.vms.xml'

    old_materials = [
        'elite_256',
        'elite_256B',
        'elite_256LB',
        'elite_256R',
        'elite_256_2side',
        'elite_256LB_2side',
        'elite_lod',
        'L_glass',
        'L_wing_128',
        'metal03',
        'metal03D',
        'Li_dmg',
        'L_fighter',
        'L_fighter_LG_2side',
        'freighter1',
        'freighter1B',
        'freighter1D',
        'freighter1W',
        'freighter1_2side',
        'freighter_LOD',
        # 'liberty1_256',
        # 'liberty1_256B',
        'liberty1_256LB',
        'liberty1_256R',
        'liberty1_256_2side',
        'Li_Equip_gen',
        'elite_order',

        'drd_interior3',
        'drd_interior3D',
        'drd_interior4',
        'hangardoor2_128',
        'liberty1_256',
        'liberty1_256B',
        'liberty1_256D',
        'liberty1_256R',
        'liberty2_256',
        'liberty2_256D',
        'liberty3_256',
        'liberty3_256D',
        'liberty_baydoors',
        'lib_weap1',
        'li_cruiser_LOD',
        'li_dreadnought_LOD',

        'O_glass',

        'drd_interior3.TGA',
        'drd_interior4.TGA',
        'elite_2562sideOR',
        'elite_256OR',
        'hangardoor2_128.TGA',
        'liberty1_256.TGA',
        'liberty2_256.TGA',
        'liberty3_256.TGA',
        'liberty_baydoors.TGA',
        'lib_weap1OR',
        'Li_dmgOR',
        'osiris_lod',
        'drd_interior4O',
        'drd_interior3O',
        'liberty1_256O',
        'liberty2_256O',
        'liberty3_256O',

    ]
    # old_materials = [
    #     'K_Debris',
    #     'K_dmg',
    #     'K_dmg2side',
    #     'K_glass',
    #     'K_metal03',
    #     'K_metal03_int',
    #     'K_metal03_intD',
    #     'K_panel01_256',
    #     'K_panel01_256D',
    #     'K_panel02',
    #     'K_panel02D',
    #     'K_panel02R',
    #     'k_panel03',
    #
    #     'K_fighter01',
    #     'K_fighter01_2side',
    # ]

    # old_materials = [
    #     'bw_engine',
    #     'bw_glass',
    #     'bw_panel2side',
    #     'bw_panel2sideD',
    #     'bw_panel_128',
    #     'bw_panel_128D',
    #     'bw_panel_256',
    #     'bw_panel_256D',
    # ]


    skin = 'alt'


    subfile_changed_strings = []
    # for old_mat in old_materials:
    #     old_mat_hex = crc32_hex_from_str(old_mat.lower())
    #     new_mat_hex = crc32_hex_from_str(f'{skin}_{old_mat.lower()}')
    #     subfile_changed_strings.append(
    #         [f'0x{old_mat_hex[2:].upper()}', new_mat_hex],
    #     )
    #     subfile_changed_strings.append(
    #         [f'0x0{old_mat_hex[2:].upper()}', new_mat_hex],
    #     )

    upgrades = [
        # ['filename="li_elite', 'filename="li_nmd_elite'],
        # ['data.ships.liberty.li_elite.li_elite', 'data.ships.liberty.li_elite.li_elite_fx1'],
        # ['Li_elite_animated_wings', 'Li_elite_fx1_animated_wings'],

        # ['filename="li_fighter', 'filename="li_nmd_fighter'],
        # ['data.ships.liberty.li_fighter.li_fighter', 'data.ships.liberty.li_fighter.li_fighter_fx1'],
        # ['fl.li_fighter_wings', 'fl.li_nmd_fighter_wings'],
        # ['lif_none', 'lif_none_nmd'],
        # ['lod1021021183448', 'nmd_lod1021021183448'],
        #
        # ['filename="li_freighter', 'filename="li_nmd_freighter'],
        # ['data.ships.liberty.li_freighter.li_freighter', 'data.ships.liberty.li_nmd_freighter.li_nmd_freighter'],
        # ['li_fr_none', 'li_fr_nmd_none'],
        # ['lod1021203111952', 'nmd_lod1021203111952'],
        #
        # ['filename="li_freighter', 'filename="li_pir_freighter'],
        # ['data.ships.liberty.li_freighter.li_freighter', 'data.ships.liberty.li_pir_freighter.li_pir_freighter'],
        # ['li_fr_none', 'li_fr_pir_none'],
        # ['lod1021203111952', 'pir_lod1021203111952'],

        # ['filename="bh_vheavy_fighter', f'filename="bh_{skin}_vheavy_fighter'],
        # ['data.ships.bounty_hunter.bh_vheavy_fighter.bh_vheavy_fighter', f'data.ships.bounty_hunter.bh_vheavy_fighter_{skin}.bh_vheavy_fighter'],
        # ['bh_fighter_adv', f'bh_{skin}_fighter_adv'],
        # ['bhfu3_none', f'bhfu3_{skin}_none'],
        # ['bh_hammer', f'bh_{skin}_hammer'],
        # ['lod1030109200506', f'{skin}_lod1030109200506'],

        # ['filename="bh_', f'filename="bh_{skin}_'],
        # ['data.ships.bounty_hunter', f'data.ships.bounty_hunter_{skin}'],
        # ['bh_fighter_adv', f'bh_{skin}_fighter_adv'],
        # ['bhfu3_none', f'bhfu3_{skin}_none'],
        # ['bh_hammerhead_fix', f'bh_{skin}_hammerhead_fix'],
        # ['lod1030109200506', f'{skin}_lod1030109200506'],
        #
        # ['filename="li_', f'filename="li_{skin}_'],
        # ['data.ships.liberty.li_elite', f'data.ships.liberty.li_elite_{skin}'],
        # ['lod1021107133350', f'{skin}_lod1021107133350'],
        # ['Li_elite_juni', f'Li_{skin}_elite_juni'],
        # ['Li_elite_animated_wings', f'Li_elite2_{skin}_animated_wings'],

        #
        # ['filename="or_', f'filename="or_{skin}_'],
        # ['data.ships.order.or_osiris', f'data.ships.order.or_osiris_{skin}'],
        # ['lod1021108124813', f'{skin}_lod1021108124813'],
        #
        # ['filename="or_', f'filename="or_{skin}_'],
        # ['order.or_elite', f'order.or_elite_{skin}'],
        # ['or_elite_telescope', f'or_elite_telescope_{skin}'],
        # ['lod1021102155951', f'{skin}_lod1021102155951'],

        ['filename="bw_', f'filename="bw_{skin}_'],
        ['data.ships.border_world', f'data.ships.border_world_{skin}'],
        ['bw_fighter_none', f'bw_fighter_none_{skin}'],
        ['bw_fighter_boards', f'bw_fighter_boards_{skin}'],
        ['bw_orig_elite_none', f'bw_orig_elite_none_{skin}'],
        ['bw_orig_elite_boards', f'bw_orig_elite_boards_{skin}'],
        ['bw_elite_boards', f'bw_elite_boards_{skin}'],
        ['bw_orig_elite2_non', f'bw_orig_elite2_non_{skin}'],
        ['lod1020912020823', f'{skin}_lod1020912020823'],
        ['lod1020911031436', f'{skin}_lod1020911031436'],
        ['lod1020911030723', f'{skin}_lod1020911030723'],
        ['lod1030109103849', f'{skin}_lod1030109103849'],



    ]

    # upgrades = [
    #     ['filename="li_elite', 'filename="li_pir_elite'],
    #     ['data.ships.liberty.li_elite.li_elite', 'data.ships.liberty.li_elite.li_elite_fx2'],
    #     ['Li_elite_animated_wings', 'Li_elite_fx2_animated_wings'],
    #
    #     ['filename="li_fighter', 'filename="li_pir_fighter'],
    #     ['data.ships.liberty.li_fighter.li_fighter', 'data.ships.liberty.li_fighter.li_fighter_fx2'],
    #     ['fl.li_fighter_wings', 'fl.li_pir_fighter_wings'],
    #     ['lif_none', 'lif_none_pir'],
    #     ['lod1021021183448', 'pir_lod1021021183448'],
    # ]

    utf_xml.XML_UTF.mass_force_encode_updated_xml()

    return

    main_file_upgrades = upgrades
    subfile_changed_strings = subfile_changed_strings + upgrades


    utf_xml.XML_UTF.mass_encode_updated_xml(
        subfolder_filename,
        subfile_changed_strings,
        main_file_upgrades,
        # [['li_elite', 'li_pir_elite'], ['li_fighter', 'li_pir_fighter'], ['li_freighter', 'li_pir_freighter']],
        # [['li_', f'li_{skin}_']],
        # [['or_', f'or_{skin}_']],
        [['bw_', f'bw_{skin}_']],
    )

def mass_upgrade():
    subfolder_filename = 'lod0-212.vms.xml'

    old_materials = [
        "ku_battleship_lod",
        "ku_cruiser_lod",
        "ku_gunboat_lod",
        "R_dtl1",
        "R_dtl1",
        "R_dtl1D",
        "R_dtl1G",
        "R_dtl1M",
        "R_dtl1Wfrm",
        "R_dtl1Wtrm",
        "R_dtl1_Y",
        "R_dtl2B",
        "R_dtl2B_M",
        "R_dtl2B_Y",
        "R_dtl3",
        "R_dtl3M",
        "R_dtl3W",

        "r-dark gray",
        "ku_elite_lod",
        "ku_fighter_lod",
        "ku_fighter_lod2side",
        "ku_freigher_lod",
        "ku_freighter_lod2side",
        "r_dmg3",
        "r_glass",
        "r_panel01_256",
        "r_panel01_2562side",
        "r_panel01_256D",
        "r_panel02_256",
        "r_panel02_2562side",
        "r_panel03_256",

    ]

    skin = 'alt'


    subfile_changed_strings = []
    # for old_mat in old_materials:
    #     old_mat_hex = crc32_hex_from_str(old_mat.lower())
    #     new_mat_hex = crc32_hex_from_str(f'{skin}_{old_mat.lower()}')
    #     subfile_changed_strings.append(
    #         [f'0x{old_mat_hex[2:].upper()}', new_mat_hex],
    #     )
    #     subfile_changed_strings.append(
    #         [f'0x0{old_mat_hex[2:].upper()}', new_mat_hex],
    #     )

    upgrades = [
        ['filename="rh_', f'filename="rh_{skin}_'],
        ['data.ships.rheinland.rh_gunship', f'data.ships.rheinland.rh_gunship_{skin}'],
        ['data.ships.rheinland.rh_cruiser', f'data.ships.rheinland.rh_cruiser_{skin}'],
        ['data.ships.rheinland.rh_battleship', f'data.ships.rheinland.rh_battleship_{skin}'],
        ['data.ships.rheinland.rh_fighter', f'data.ships.rheinland.rh_fighter_{skin}'],
        ['data.ships.rheinland.rh_elite', f'data.ships.rheinland.rh_elite_{skin}'],
        ['data.ships.rheinland.rh_freighter', f'data.ships.rheinland.rh_freighter_{skin}'],
        ['fl.rh', f'fl.rh_{skin}'],
        ['xrh_fr', f'xrh_fr_{skin}'],

        ['lod1020917205920', f'{skin}_lod1020917205920'],
        ['lod1020917203809', f'{skin}_lod1020917203809'],
        ['lod1021202173704', f'{skin}_lod1021202173704'],
        ['lod1020917112833', f'{skin}_lod1020917112833'],
        ['lod1020917110609', f'{skin}_lod1020917110609'],
        ['lod1020917142023', f'{skin}_lod1020917142023'],



    ]
    main_file_upgrades = upgrades
    subfile_changed_strings = subfile_changed_strings + upgrades

    utf_xml.XML_UTF.mass_encode_updated_xml(
        subfolder_filename,
        subfile_changed_strings,
        main_file_upgrades,
        [['rh_', f'rh_{skin}_']],
    )

def mass_upgrade_ku():
    subfolder_filename = 'lod0-212.vms.xml'

    old_materials = [
        "ku_elite_planar",
        "ku_elite_planar_2side",
        "Ku_fighter_textures",
        "Ku_fighter_textures_2side",
        "ku_freighter_lod_256",
        "ku_wings_lod2",
        "K_Debris",
        "K_dmg",
        "K_dmg2side",
        "K_elite_256",
        "K_elite_256_2side",
        "K_fighter01",
        "K_fighter01_2side",
        "K_glass",
        "K_metal03",
        "K_metal03_int",
        "K_metal03_intD",
        "K_panel01_256",
        "K_panel01_256D",
        "K_panel02",
        "K_panel02D",
        "K_panel02R",
        "k_panel03",
        "K_panel_trim",
        "K_panel_trimD",
        "k_panel_window02",

        "K_wings",

        "k_wings2side",

        "Equip_genD",
        "Equip_mstrD",
        "ku_battleship_lod1_planar",
        "ku_detroyer_textures",
        "ku_gunboat_textures",

        "K_panel01_256R",
        "K_panel01_256_D",
        "K_panel01_256_M",
        "K_panel02_256",
        "K_panel03_256",
        "K_panel03_blu",
        "K_panel03_D",
        "K_panel03_O",
        "K_panel_trim_blu",
        "K_panel_trim_D",
        "K_panel_trim_M",
    ]

    skin = 'alt'


    subfile_changed_strings = []
    # for old_mat in old_materials:
    #     old_mat_hex = crc32_hex_from_str(old_mat.lower())
    #     new_mat_hex = crc32_hex_from_str(f'{skin}_{old_mat.lower()}')
    #     subfile_changed_strings.append(
    #         [f'0x{old_mat_hex[2:].upper()}', new_mat_hex],
    #     )
    #     subfile_changed_strings.append(
    #         [f'0x0{old_mat_hex[2:].upper()}', new_mat_hex],
    #     )

    upgrades = [
        ['filename="ku_', f'filename="ku_{skin}_'],
        ['filename="pi_', f'filename="pi_{skin}_'],
        ['filename="pir_', f'filename="pir_{skin}_'],
        ['data.ships.kusari.ku_gunship', f'data.ships.kusari.ku_gunship_{skin}'],
        ['data.ships.kusari.ku_destroyer', f'data.ships.kusari.ku_destroyer_{skin}'],
        ['data.ships.kusari.ku_battleship', f'data.ships.kusari.ku_battleship_{skin}'],
        ['data.ships.kusari.ku_fighter', f'data.ships.kusari.ku_fighter_{skin}'],
        ['data.ships.kusari.ku_elite', f'data.ships.kusari.ku_elite_{skin}'],
        ['data.ships.pirate.pi_elite', f'data.ships.pirate.pi_elite_{skin}'],
        ['data.ships.pirate.pi_fighter', f'data.ships.pirate.pi_fighter_{skin}'],
        ['data.ships.pirate.pi_vheavy_fighter', f'data.ships.pirate.pi_vheavy_fighter_{skin}'],

        ['fl.pi_elite_wings', f'fl.pi_elite_wings_{skin}'],
        ['fl.co_fighter_wings', f'fl.co_fighter_wings_{skin}'],
        ['pi_heavy_12345', f'pi_heavy_12345_{skin}'],


        ['xke_', f'xke_{skin}_'],
        ['KEstar', f'KEstar{skin}'],
        ['KEport', f'KEport{skin}'],

        ['xkf_', f'xkf_{skin}_'],
        ['KFstar', f'KFstar{skin}'],
        ['KFport', f'KFport{skin}'],

        # ['kf_', f'kf_{skin}_'],

        ['lod1021230105011', f'{skin}_lod1021230105011'],
        ['lod1021010103358', f'{skin}_lod1021010103358'],
        ['lod1021010103739', f'{skin}_lod1021010103739'],
        ['lod1030107115314', f'{skin}_lod1030107115314'],
        ['lod1030110104503', f'{skin}_lod1030110104503'],
        ['lod1020916162452', f'{skin}_lod1020916162452'],

        ['lod1TITAN.3db', f'{skin}_lod1TITAN.3db'],
        ['lod1030109204913', f'{skin}_lod1030109204913'],
        ['lod1030109205127', f'{skin}_lod1030109205127'],
    ]

    # utf_xml.XML_UTF.mass_force_encode_updated_xml()

    # return

    # upgrades = []
    main_file_upgrades = upgrades
    subfile_changed_strings = subfile_changed_strings + upgrades

    utf_xml.XML_UTF.mass_encode_updated_xml(
        subfolder_filename,
        subfile_changed_strings,
        main_file_upgrades,
        [['pi_', f'pi_{skin}_'],

        ['ku_', f'ku_{skin}_']],
    )


def mass_upgrade_br():  # _br
    subfolder_filename = 'lod0-212.vms.xml'

    old_materials = [
        # "B-dtl1",
        # "B-dtl1-2-DB",
        # "B-dtl1-2-DR",
        # "B-dtl1-2-Y",
        # "B-dtl1-2B",
        # "B-dtl1-DG",
        # "B-dtl1-DR",
        # "B-dtl1-DY",
        # "B-dtl1-LB",
        # "B-dtl1-MB",
        # "B-dtl1-R",
        # "B-dtl1-Y",
        # "B-dtl2-LB",
        # "B-dtl2-R",
        # "B-dtl2-Y",
        # "B-dtl3-W",
        # "B-dtl4",
        # "B-dtl4-B",
        # "B-dtl4-D2side",
        # "B-dtl4-DB",
        # "B-dtl4-R",
        # "B-dtl4-Y",
        # "Br_battleship_lod_256",
        # "Br_destroyer",
        # "Br_destroyer_lod",
        # "br_gunship_256",
        # "Br_dmg",
        # "br_elite_lod",
        # "br_elite_lod2-side",
        # "br_fighter_256",
        # "br_fighter_256-2side",
        # "br_freighter_256",
        # "Br_freighter_256-2side",
        # "B_glass",
        # "B_player01_256",
        # "B_player01_256B",
        # "B_player01_256D",
        # "B_player01_256L",
        # "B_player01_256_2side",
        # "B_player02_256",
        # "B_player02_256_2side",
        # "B_player03_256",
        # "B_metal03D",
        # "B_metal03L",

    ]

    skin = 'alt'


    subfile_changed_strings = []
    for old_mat in old_materials:
        old_mat_hex = crc32_hex_from_str(old_mat.lower())
        new_mat_hex = crc32_hex_from_str(f'{skin}_{old_mat.lower()}')
        subfile_changed_strings.append(
            [f'0x{old_mat_hex[2:].upper()}', new_mat_hex],
        )
        subfile_changed_strings.append(
            [f'0x0{old_mat_hex[2:].upper()}', new_mat_hex],
        )

    upgrades = [
        ['filename="br_', f'filename="br_{skin}_'],

        ['data.ships.bretonia.br_gunship', f'data.ships.bretonia.br_gunship_{skin}'],
        ['data.ships.bretonia.br_destroyer', f'data.ships.bretonia.br_destroyer_{skin}'],
        ['data.ships.bretonia.br_battleship', f'data.ships.bretonia.br_battleship_{skin}'],
        ['data.ships.bretonia.br_fighter', f'data.ships.bretonia.br_fighter_{skin}'],
        ['data.ships.bretonia.br_elite', f'data.ships.bretonia.br_elite_{skin}'],
        ['data.ships.bretonia.br_freighter', f'data.ships.bretonia.br_freighter_{skin}'],

        # ['fl.pi_elite_wings', f'fl.pi_elite_wings_{skin}'],

        ['bgb_', f'bgb_{skin}_'],
        ['br_poly', f'br_poly{skin}_'],



        ['lod1021119215401', f'{skin}_lod1021119215401'],
        ['lod1020917152841', f'{skin}_lod1020917152841'],
        ['lod1020917162701', f'{skin}_lod1020917162701'],
        ['lod1020916111818', f'{skin}_lod1020916111818'],
        ['lod1021114142815', f'{skin}_lod1021114142815'],
        ['lod1030107145834', f'{skin}_lod1030107145834'],

    ]


    # upgrades = []
    main_file_upgrades = upgrades
    subfile_changed_strings = subfile_changed_strings + upgrades

    utf_xml.XML_UTF.mass_encode_updated_xml(
        subfolder_filename,
        subfile_changed_strings,
        main_file_upgrades,
        [
            ['br_', f'br_{skin}_'],
        ],
    )


def mass_upgrade99():
    subfolder_filename = 'lod0-212.vms.xml'

    old_materials = [
        "lavastroid",
        "lavastroid02",
    ]

    skin = 'nexus'

    # red
    # sphere
    # fish
    # nexus


    subfile_changed_strings = []
    for old_mat in old_materials:
        old_mat_hex = crc32_hex_from_str(old_mat.lower())
        new_mat_hex = crc32_hex_from_str(f'{skin}_{old_mat.lower()}')
        subfile_changed_strings.append(
            [f'0x{old_mat_hex[2:].upper()}', new_mat_hex],
        )
        subfile_changed_strings.append(
            [f'0x0{old_mat_hex[2:].upper()}', new_mat_hex],
        )

    upgrades = [
        ['filename="ast_', f'filename="ast_{skin}_'],

        ['data.solar.asteroids.models.ast_lava', f'data.solar.asteroids.models.ast_lava_{skin}'],

        # ['fl.pi_elite_wings', f'fl.pi_elite_wings_{skin}'],


    ]


    # upgrades = []
    main_file_upgrades = upgrades
    subfile_changed_strings = subfile_changed_strings + upgrades

    utf_xml.XML_UTF.mass_encode_updated_xml(
        subfolder_filename,
        subfile_changed_strings,
        main_file_upgrades,
        [
            ['ast_', f'ast_{skin}_'],
        ],
    )


ACTIONS = {
    'mass_decode': mass_decode,
    'mass_upgrade': mass_upgrade,
}


def single(action):
    action_function = ACTIONS.get(action, None)
    if action_function is None:
        raise Exception(f'Unknown action {action}')

    action_function()

try:
    action = sys.argv[1]
except IndexError:
    raise Exception('Action argument is required')

single(action)
