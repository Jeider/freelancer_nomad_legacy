import sys
import os
from time import sleep
import pathlib

from text.dividers import DIVIDER, SINGLE_DIVIDER

from core import get_core

from files.writer import FileWriter

from managers.script import ScriptManager

from templates.jinja_manager import JinjaTemplateManager

from universe.audio.manager import PilotManager
from universe.audio import pilot
from universe.audio import dispatcher
from universe.audio import nnvoice
from universe.audio import mission_comission

from universe.content import mineable

from templates.hardcoded_inis.audio import VoicesSpaceMaleTemplate, VoicesSpaceFemaleTemplate
from templates.hardcoded_inis.missions import VoicePropertiesTemplate

from tools import merge_image
from tools import data_folder
from tools import elevenlabs
from tools import audio_folder
from tools import maxlancer
from tools.audio_pilot import TempPilot, VanillaPilot

from story import actors

from tools.system_template import SystemTemplateLoader

from story.cutscenes.mission9.yokohama import Msn9YokohamaCutsceneThorn

from templates.solar import hacker_panel
from templates.dockable import terraforming
from templates.dockable import valensia
from templates.dockable import upsilon_gasinside
from templates.dockable import tunnel
from templates.misc import rmbase
from templates.misc import trading
from templates.dockable import nomad_asf_hq
from templates.dockable import order_shipyard

from templates.dockable import m13


def draw_base():
    new_name = None
    move_to = None
    workspace = '1'

    # base_class = m13.RockfordGenerator
    # new_name = 'or_hq_vienna_entry'
    # move_to = (13900, 0, 32400)
    #
    # base_class = trading.XenosOutpostPanels
    # new_name = 'xenos_control01'
    # move_to = (-2000, 0, -10000)
    #
    # base_class = order_shipyard.OrderShipyard
    # new_name = 'or_hq_shipyard_01'
    # move_to = (-20000, 0, 0)

    # base_class = ast_om15_xxxlarge.AsteroidOne
    # new_name = 'communicator'
    # move_to = (-9500, 0, -10000)

    base_class = nomad_asf_hq.AsfHQ
    the_base = base_class()

    content = the_base.get_instance(new_space_object_name=new_name, move_to=move_to)
    data_folder.DataFolder.sync_to_test_workspace(content, workspace_index=workspace)


def draw_base_for_hardpoints():
    new_name = None
    move_to = None
    workspace = '0'

    # base_class = m13.RockfordGenerator
    # new_name = 'or_hq_vienna_entry'
    # move_to = (13900, 0, 32400)

    base_class = terraforming.TerraformingTwo
    # new_name = 'or_hq_vienna_entry'
    the_base = base_class()

    the_base.get_instance(new_space_object_name=new_name, move_to=move_to)
    the_base.parse_segments()
    # print(the_base.get_segments_as_hardpoints_xml())
    print(the_base.get_segments_as_loadout(warning=True))
    # print(the_base.get_instance_from_segments())


def generate_hacker_panels():
    hacker_panel.HackerPanelManager().write_content()


def compile_audio():
    audio_folder.AudioFolder.compile_xml_to_utf()
    print('done')


def compile_pilots_ini():
    PilotManager.compile_pilots_ini()


def compile_pilots_audio():
    PilotManager.compile_pilots_audio()


def test_hacker_colors():
    x = hacker_panel.HackerPanelManager()

    x1 = x.get_random_hacker_panel()
    x2 = x1.get_space_content('sphere_depot_02_hacker', 'rh_grp', (-960, 17, 7000), hacker_panel.REL_TOP, 'sphere_success')
    print(x2)
    pass


def dump_system():
    system_template = SystemTemplateLoader.get_template('sphere')
    points = system_template.dump_points()
    for point in points:
        print(point)


def dump_story_system():
    current_path = pathlib.Path().resolve()
    path = current_path.parent.parent / 'DATA' / 'UNIVERSE' / 'SPECIAL' / 'SPHERE'
    system_template = SystemTemplateLoader.get_template('sphere_dev', source_path=path)
    points = system_template.dump_points()
    for point in points:
        print(f"'{point}',")


def build_image():
    merge_image.build_image()


def get_frames():
    results = merge_image.get_frames()
    for item in results:
        print(item)


def get_frames_ints():
    results = merge_image.get_frames_ints()
    for item in results:
        print(item)


def test_story():
    jinja = JinjaTemplateManager()
    tpl = 'missions/m01/m01a.ini'

    x = jinja.get_result(tpl, {})
    FileWriter.write('missions/m01a.ini', x)
    print('done')


def generate_script():
    ScriptManager().generate_script()
    # FileWriter.write('mission9.html', mission9.Mission9().get_story_script())
    # FileWriter.write('mission10.html', mission10.Mission10().get_story_script())
    # FileWriter.write('mission11.html', mission11.Mission11().get_story_script())
    # FileWriter.write('mission12.html', mission12.Mission12().get_story_script())
    # FileWriter.write('mission13.html', mission13.Mission13().get_story_script())
    # print(content)


# def parse_voices():
#     lines = []
#     for item in CONTENT.splitlines():
#         if item.startswith('msg'):
#             parts = item.split(' = ')
#             lines.append(parts[1])
#             print(f"'{parts[1]}',")



def test_voices():
    props = VanillaPilot.parse_vanilla_voice_props()
    return


def test_steos():
    # SteosVoice.prepare_temp_path()


    #
    # PilotManager.prepare_pilots_audio()
    #
    # return

    the_pilot = nnvoice.NNVoice()

    TempPilot.prepare_temp_folders(the_pilot)
    TempPilot.fill_audio(the_pilot, skip=True)

    TempPilot.fill_files_for_xml(the_pilot)
    TempPilot.build_voice_xml(the_pilot)



    # the_pilot = nnvoice.NNVoice()
    #
    # TempPilot.prepare_temp_folders(the_pilot)
    # TempPilot.fill_audio(the_pilot, skip=True)
    #
    # TempPilot.fill_files_for_xml(the_pilot)
    # TempPilot.build_voice_xml(the_pilot)







    return

    lines = pilot.get_number_lines()

    # for line in lines:
    #     SteosVoice.generate_temp_sound(
    #         actor=line.get_actor(steos_id=pilot.STEOS_ID),
    #         text=line.get_temp_text(),
    #         name=line.get_code(),
    #     )
    #     sleep(0.2)
    #
    # return

    for line in lines:
        line.process_temp()
    



    return


def generate_story_voices():
    script_manager = ScriptManager()
    # import pdb;pdb.set_trace()
    for msn in script_manager.get_missions():
        if msn.MISSION_INDEX != 13:
            continue
        for voice in msn.get_voices():
            audio_folder.AudioFolder.compile_story_voice_to_xml(voice)


def test_elevenlabs():
    result = elevenlabs.ElevenLabs.get_line('Это Рэйнланд, омега один слеш один. Я направляюсь к станции Потсдам. Скоро буду.')
    import pdb;pdb.set_trace()


def test_lua():
    manager = maxlancer.SceneEntityLoader.get_entity_manager('m9_yokohama')

    scene = Msn9YokohamaCutsceneThorn()

    content = scene.get_content()

    FileWriter.write('m9_yokohama.lua', content)


    import pdb;pdb.set_trace()


class MySupriseField(mineable.DefaultField):
    BOX_SIZE = 1800
    DENSITY_MULTIPLER = 3
    DRIFT_X = 0.8
    DRIFT_Y = 1
    DRIFT_Z = 0.8
    EMPTY_CHANCE = 0
    # ROTATE_X_MIN = -180
    # ROTATE_X_MAX = 180
    # ROTATE_Y_MIN = -180
    # ROTATE_Y_MAX = 180
    # ROTATE_Z_MIN = -180
    # ROTATE_Z_MAX = 180


class MyField(mineable.StaticObjectField):
    ALIAS = 'bh_hazard_field'
    INDEX = 1
    STATIC_ARCHETYPES = [
        'bh_hazard',
    ]
    FIELD_CLASS = MySupriseField
    REWARDS_GROUP_CLASS = mineable.DefaultSupriseRewardsGroup
    ULTRA_REWARD = False


def generate_field():
    core = get_core()
    the_sys = core.universe.universe_root.get_all_system_by_name('bh')

    field = MyField(system=the_sys)
    content = field.get_system_content()
    print(content)


def generate_points():
    points = {
        'kernel2_ast1_in': '-7870, -538, -7906',
        'kernel2_ast1_wall1': '-7215, -167, -7573',
        'kernel2_ast1_wall2': '-6523, 276, -7479',
        'kernel2_ast1_end': '-6494, 115, -6336',
        'kernel2_ast2_in': '-4879, -235, -3877',
        'kernel2_ast2_mid1': '-3504, -246, -3033',
        'kernel2_ast2_end': '-2189, 70, -3062',
        'kernel2_ast3_in': '155, 62, -3307',
        'kernel2_ast3_mid1': '1490, -235, -3543',
        'kernel2_ast3_exit': '2968, -198, -2996',
        'kernel2_ast4_in': '3895, 527, -1377',
        'kernel2_ast4_split': '4903, 699, -683',
        'kernel2_ast4_mid1': '5770, 942, -1275',
        'kernel2_ast4_exit': '6710, 806, -1666',
        'kernel2_ast5_in': '8758, 511, -2579',
        'kernel2_ast5_wall1': '9376, 494, -2650',
        'kernel2_ast5_core': '9838, 446, -3017',
        'kernel2_ast5_wall2': '10265, 275, -3544',
        'kernel2_ast5_exit': '10614, 125, -3856',
    }

    data = []

    for name, pos in points.items():
        data.append(
            f'''[Object]
nickname = {name}
pos = {pos}
rotate = 0, 0, 0
archetype = nav_buoy
'''
        )

    names_list = [f"'{name}'," for name in points.keys()]
    names_combined = SINGLE_DIVIDER.join(names_list)

    targets_list = [
        f"NNObj(self, O.GOTO, target='{name}', reach_range=500),"
        for name in points.keys()
    ]
    targets_combined = SINGLE_DIVIDER.join(targets_list)

    nav_list = [
        f"{{{{ nn_{name}.reach() }}}}"
        for name in points.keys()
    ]
    nav_combined = SINGLE_DIVIDER.join(nav_list)


    data_combined = SINGLE_DIVIDER.join(data)

    print(nav_combined)


def dbg():
    # positions = [
    #     [83.005188, 125.17676, 13.371254],
    #     [2.4011745, -98.823227, -26.740688],
    #     [-30.598829, -100.68946, -27.857965],
    #     [1.4011707, -64.689461, -27.857965],
    #     [-31.8281, -64.08577, -28.232422],
    #     [-31.8281, 3.9142303, -28.232422],
    #     [1.2891908, 4.4142303, -28.366173],
    #     [-30.210812, 37.91423, -28.366173],
    #     [2.0597906, 71.176613, -27.857933],
    #     [-28.940208, 103.81059, -28.740768],
    #     [-65.773544, -10.689415, 20.9259],
    #     [-32.440212, -14.889441, 20.122753],
    #     [1.0397639, -14.889441, 18.739208],
    #     [34.541336, -12.024345, 19.405876],
    #     [-66.958664, -99.524345, 22.405876],
    #     [-32.592415, -100.40695, 22.405876],
    #     [5.915772, -63.532547, 22.405876],
    #     [53.915779, -98.636322, 27.168423],
    #     [46.249107, 65.363678, 17.835089],
    #     [44.366516, 31.863678, 17.968941],
    #     [44.249157, 22.204842, -22.531059],
    #     [-63.250843, 116.20483, -22.531059],
    #     [-65.133362, 81.967628, -23.435417],
    #     [-65.633362, 29.705048, -28.331703],
    #     [3.8666401, 119.70505, -28.331703],
    #     [-63.466682, 88.205048, 25.501633],
    #     [-67.083984, 54.863571, 26.001633],
    #     [49.130775, 124.57294, 18.642044],
    #     [-27.869226, 120.30232, 6.6966648],
    # ]
    #
    # i = 1
    # for pos_x, pos_y, pos_z in positions:
    #     print(f'''
    # <HpFX{i:02d}>
    #    <Orientation type="Matrix">1, 0, 0, 0, 1, 0, 0, 0, 1</Orientation>
    #    <Position type="Vector">{pos_x}, {pos_y}, {pos_z}</Position>
    # </HpFX{i:02d}>
    #
    # ''')
    #
    #     i += 1
    
    
  for i in range(1, 29+1):
#         print(f'''
# g box{i:02d}_lod1
# usemtl debris_no_alpha
# f 354/6/36 355/5/36 356/8/36
# f 355/5/36 357/21/36 356/8/36
# s 2
# f 356/6/37 357/5/37 358/8/37
# f 357/5/37 359/21/37 358/8/37
# s 1
# f 358/6/38 359/5/38 360/8/38
# f 359/5/38 361/21/38 360/8/38
# s 2
# f 360/6/39 361/5/39 354/8/39
# f 361/5/39 355/21/39 354/8/39
# s 3
# f 360/6/40 354/5/40 358/8/40
# f 354/5/40 356/21/40 358/8/40
# f 355/6/41 361/5/41 357/8/41
# f 361/5/41 359/21/41 357/8/41
# # 12 triangles in group''')


        print(f'''
[CollisionGroup]
obj = box{i:02d}_lod1
separable = true
child_impulse = 1.000000
parent_impulse = 60.000000
debris_type = debris_vanish
fuse = debrisbox_is_ultra, 0.000000, 1
fuse = debris_box_dmg_box{i:02d}, 0.000000, 1
explosion_resistance = 0.0001
hit_pts = 2000
root_health_proxy = false''')

#         print(f'''
# [fuse]
# name = debris_box_dmg_box{i:02d}
# lifetime = 0.100000
# death_fuse = true
# 
# [destroy_hp_attachment]
# at_t = 0.0
# hardpoint = HpFX{i:02d}
# fate = debris
# 
# [destroy_group]
# at_t = 0.000000
# group_name = box{i:02d}_lod1
# fate = disappear''')



ACTIONS = {
    'generate_hacker_panels': generate_hacker_panels,
    'compile_audio': compile_audio,
    'test_hacker_colors': test_hacker_colors,
    'draw_base': draw_base,
    'draw_base_for_hardpoints': draw_base_for_hardpoints,
    'build_image': build_image,
    'get_frames': get_frames,
    'get_frames_ints': get_frames_ints,
    'test_story': test_story,
    'generate_script': generate_script,
    'test_voices': test_voices,
    'test_steos': test_steos,
    'test_elevenlabs': test_elevenlabs,
    'test_lua': test_lua,
    'dump_system': dump_system,
    'dump_story_system': dump_story_system,
    'compile_pilots_ini': compile_pilots_ini,
    'compile_pilots_audio': compile_pilots_audio,
    'generate_story_voices': generate_story_voices,
    'generate_field': generate_field,
    'generate_points': generate_points,
    'dbg': dbg,
}


def single(action):
    action_function = ACTIONS.get(action, None)
    if action_function is None:
        raise Exception('Unknown action')

    action_function()

try:
    action = sys.argv[1]
except IndexError:
    raise Exception('Action argument is required')

single(action)

