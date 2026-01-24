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
            f'rh_',
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

def mass_upgrade():
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
        'L_R_wnds_256',

    ]
    skin = 'nmd'


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

        # ['filename="bh_vheavy_fighter', 'filename="bh_nmd_vheavy_fighter'],
        # ['data.ships.bounty_hunter.bh_vheavy_fighter.bh_vheavy_fighter', 'data.ships.bounty_hunter.bh_vheavy_fighter_nmd.bh_vheavy_fighter'],
        # ['bh_fighter_adv', 'bh_nmd_fighter_adv'],
        # ['bhfu3_none', 'bhfu3_nmd_none'],
        # ['bh_hammerhead_fix', 'bh_nmd_hammerhead_fix'],
        # ['lod1030109200506', 'nmd_lod1030109200506'],
        #
        # ['filename="bh_', f'filename="bh_{skin}_'],
        # ['data.ships.bounty_hunter', f'data.ships.bounty_hunter_{skin}'],
        # ['bh_fighter_adv', f'bh_{skin}_fighter_adv'],
        # ['bhfu3_none', f'bhfu3_{skin}_none'],
        # ['bh_hammerhead_fix', f'bh_{skin}_hammerhead_fix'],
        # ['lod1030109200506', f'{skin}_lod1030109200506'],

        ['filename="li_', f'filename="li_{skin}_'],
        ['data.ships.liberty.li_dreadnought', f'data.ships.liberty.li_dreadnought_{skin}'],
        ['lod1021108124158', f'{skin}_lod1021108124158'],

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

    main_file_upgrades = upgrades
    subfile_changed_strings = subfile_changed_strings + upgrades

    utf_xml.XML_UTF.mass_encode_updated_xml(
        subfolder_filename,
        subfile_changed_strings,
        main_file_upgrades,
        # [['li_elite', 'li_pir_elite'], ['li_fighter', 'li_pir_fighter'], ['li_freighter', 'li_pir_freighter']],
        [['li_', f'li_{skin}_']],
    )

def dbg():
    point = [-132, 0, 65]
    rotated = math.relocate_point(point, 180)
    print(rotated)


ACTIONS = {
    'mass_decode': mass_decode,
    'mass_upgrade': mass_upgrade,
    'dbg': dbg,
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
