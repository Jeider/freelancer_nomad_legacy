import shutil
import time

from screeninfo import get_monitors
import subprocess
import os
import webview

from startup.meta import ScreenMeta
from startup.config import StartupConfig
from startup.text import LauncherText
from tools.data_folder import DataFolder
# from managers.crash import CrashManager
from managers.jinja_manager import JinjaTemplateManager
from managers.options import OptionsManager

SCREEN_CONFIG_HTML = 'startup/launcher.html'
BG_COLOR = "#132231"
DEFAULT_FOVY = 70

EASY = 'easy'
NORMAL = 'normal'
HARD = 'hard'
EXTREME = 'extreme'

DIFFICULTIES = [
    EASY,
    NORMAL,
    # HARD,
    # EXTREME
]
DEFAULT_DIFF = NORMAL

RU_BUILD_PER_DIFF = {
    EASY: 'RU_EASY',
    NORMAL: 'RU_NORMAL',
    HARD: 'RU_HARD',
    EXTREME: 'RU_EXTREME',
}

EN_BUILD_PER_DIFF = {
    EASY: 'EN_EASY',
    NORMAL: 'EN_NORMAL',
    HARD: 'EN_HARD',
    EXTREME: 'EN_EXTREME',
}


class Api:
    def __init__(self, russian):
        self.russian = russian
        self._window = None

    def set_window(self, window: webview.Window):
        self._window = window

    def quit(self):
        if self._window:
            self._window.destroy()

    def hide(self):
        if self._window:
            self._window.hide()

    def show(self):
        if self._window:
            self._window.show()

    def runFreelancer(self, resolution, windowed, dxwrapper, difficulty, fovy, front_light, trail, player_body, player_commhelmet):
        print(f'Run FL with resolution {resolution}')
        print(f'Windowed mode: {windowed}')
        print(f'use DxWrapper: {dxwrapper}')
        print(f'Difficulty: {difficulty}')
        print(f'Front light: {front_light}')
        print(f'Trail: {trail}')
        print(f'Player body: {player_body}')
        print(f'Player commhelmet: {player_commhelmet}')
        if fovy == int(70):
            fovy = None

        prev_cwd = os.getcwd()
        try:
            self.apply_settings(resolution, windowed, dxwrapper, difficulty, fovy, front_light, trail, player_body, player_commhelmet)
        except Exception as e:
            self.show()
            print(f'Cannot launch FL. Reason: {e}')
            os.chdir(prev_cwd)
            raise

    def apply_settings(self, resolution, windowed, dxwrapper, difficulty, fovy, front_light, trail, player_body, player_commhelmet):
        settings_save = {
            'current_resolution': resolution,
            'is_windowed': windowed,
            'is_dxwrapper': dxwrapper,
            'difficulty': difficulty,
            'front_light': front_light,
            'trail': trail,
            'player_body': player_body,
            'player_commhelmet': player_commhelmet,

        }
        if fovy and fovy != DEFAULT_FOVY:
            settings_save['fovy'] = fovy

        main_data_folder = DataFolder()
        meta = ScreenMeta()
        tpl_manager = JinjaTemplateManager()
        prev_cwd = os.getcwd()

        main_data_folder.save_startup_settings(settings_save)

        unpacked_resolution = [int(x) for x in resolution.split('x')]

        dyn_config_kwargs = {}
        if difficulty == EASY:
            dyn_config_kwargs['difficulty_easy'] = True
        if difficulty == EXTREME:
            dyn_config_kwargs['difficulty_hard'] = True

        config = StartupConfig(screen_meta=meta, resolution=unpacked_resolution, fovx=None, fovy=fovy,
                               dxwrapper=dxwrapper,
                               front_light=front_light, contrail=trail,
                               player_body=player_body, player_commhelmet=player_commhelmet,
                               **dyn_config_kwargs)
        manager = OptionsManager(tpl_manager=tpl_manager, config=config)
        manager.sync_data()

        if self.russian:
            build_name = RU_BUILD_PER_DIFF[difficulty]
        else:
            build_name = EN_BUILD_PER_DIFF[difficulty]

        game_folder = DataFolder()
        build_folder = DataFolder(build_to_folder=build_name)
        if not build_folder.get_root().exists():
            raise Exception(f'Build {build_name} not found!')

        print('Prepare to replace data')

        shutil.copytree(
            build_folder.get_root(),
            game_folder.get_root(),
            dirs_exist_ok=True,
        )

        print('Data replaced')

        if windowed:
            if self.russian:
                file_name = 'Freelancer_window.exe'
            else:
                file_name = 'Freelancer_window_en.exe'
        else:
            if self.russian:
                file_name = 'Freelancer.exe'
            else:
                file_name = 'Freelancer_en.exe'

        run_params = [file_name]
        if windowed:
            run_params.append('-w')

        file_root = os.getcwd().replace('Assets\\Pythonlancer', '')
        os.chdir(f'{file_root}EXE')

        # os.system(' '.join(run_params))
        try:
            print('run subprocess')
            self.hide()
            result = subprocess.run(run_params, check=True)
            os.chdir(prev_cwd)
            print(f"Subprocess completed successfully with return code: {result.returncode}")
            self.quit()
        except subprocess.CalledProcessError as e:
            # CrashManager().register_crash()
            print(f"Subprocess crashed with return code: {e.returncode}")
            self.quit()
        except FileNotFoundError:
            print("Error: Subprocess script or command not found.")


def create_launcher(russian=True):
    meta = ScreenMeta()
    tpl_manager = JinjaTemplateManager()

    my_width = None
    my_height = None
    frontend_resolutions = []

    main_data_folder = DataFolder()

    for m in get_monitors():
        my_width = m.width
        my_height = m.height

        frontend_resolutions.append(
            f"{my_width}x{my_height}"
        )

    for res_width, res_height in meta.get_resolutions():
        if my_width and my_height:
            if my_width == res_width and my_height == res_height:
                continue

            if res_width > my_width or res_height > my_height:
                continue

        frontend_resolutions.append(
            f"{res_width}x{res_height}"
        )

    defaults = main_data_folder.get_startup_settings()

    diff = defaults.get('difficulty', DEFAULT_DIFF)
    if diff not in DIFFICULTIES:
        diff = DEFAULT_DIFF

    context = {
        'resolutions': frontend_resolutions,
        'current_resolution': defaults.get('current_resolution', None),
        'is_windowed': defaults.get('is_windowed', False),
        'is_dxwrapper': defaults.get('is_dxwrapper', True),
        'fovy': defaults.get('fovy', DEFAULT_FOVY),
        'difficulty': diff,
        'front_light': defaults.get('front_light', 'white'),
        'trail': defaults.get('trail', 'default'),
        'player_body': defaults.get('player_body', 'default'),
        'player_commhelmet': defaults.get('player_commhelmet', 'default'),
        't': LauncherText(russian=russian),
    }
    html = tpl_manager.get_result(SCREEN_CONFIG_HTML, context)

    api = Api(russian=russian)
    window = webview.create_window('The Nomad Legacy', html=html, background_color=BG_COLOR, js_api=api,
                                   width=800, height=800, resizable=False)
    api.set_window(window)
    try:
        webview.start()
    except Exception as e:
        print(f'Launcher failed! Reason: {e}')
        time.sleep(10)
