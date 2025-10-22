from screeninfo import get_monitors
import os
import webview

from startup.meta import ScreenMeta
from startup.config import StartupConfig
from managers.jinja_manager import JinjaTemplateManager
from managers.options import OptionsManager

meta = ScreenMeta()
tpl_manager = JinjaTemplateManager()


# os.system('"C:\\Documents and Settings\\flow_model\\flow.exe"')


russian = False
screen_width = None
screen_height = None

for m in get_monitors():
    screen_width = m.width
    screen_height = m.height

resolutions = meta.get_resolutions_joined()
if screen_width and screen_height:
    my_res_joined = f"{screen_width}x{screen_height}"
    if my_res_joined in resolutions:
        resolutions.remove(my_res_joined)
        resolutions.insert(0, my_res_joined)


SCREEN_CONFIG_HTML = 'startup/screen_options.html'
BG_COLOR = "#132231"
context = {
    'resolutions': resolutions
}
html = tpl_manager.get_result(SCREEN_CONFIG_HTML, context)



def apply_settings(resolution, windowed, fovx=None, fovy=None):
    config = StartupConfig(screen_meta=meta, resolution=resolution, fovx=fovx, fovy=fovy)
    manager = OptionsManager(tpl_manager=tpl_manager, config=config)
    manager.sync_data()

    prev_cwd = os.getcwd()
    file_root = os.getcwd().replace('Assets\\Pythonlancer', '')
    os.chdir(f'{file_root}EXE')

    if windowed:
        if russian:
            file_name = 'Freelancer_window.exe'
        else:
            file_name = 'Freelancer_window_en.exe'
    else:
        if russian:
            file_name = 'Freelancer.exe'
        else:
            file_name = 'Freelancer_en.exe'

    run_params = [file_name]
    if windowed:
        run_params.append('-w')

    os.system(' '.join(run_params))
    os.chdir(prev_cwd)


class Api:
    def __init__(self):
        self._window = None

    def set_window(self, window: webview.Window):
        self._window = window

    def quit(self):
        if self._window:
            self._window.destroy()

    def runFreelancer(self, resolution, windowed, fovx, fovy):
        print(resolution)
        print(windowed)
        if fovx == int(70):
            fovx = None
        if fovy == int(70):
            fovy = None

        apply_settings([int(x) for x in resolution.split('x')], windowed, fovx, fovy)

        self.quit()


api = Api()
webview.create_window('Hello world', html=html, background_color=BG_COLOR, js_api=api)
webview.start()
