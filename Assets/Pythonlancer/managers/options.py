from tools.data_folder import DataFolder


PERF_OPTIONS_TEMPLATE = 'hardcoded_inis/static_content/PerfOptions.ini'
HUD_SHIFT_TEMPLATE = 'hardcoded_inis/static_content/HudShift.ini'
CAMERAS_TEMPLATE = 'hardcoded_inis/static_content/cameras.ini'
FRONT_LIGHT_TEMPLATE = 'hardcoded_inis/static_content/front_light.ini'
CONTRAIL_TEMPLATE = 'hardcoded_inis/static_content/contrail.ini'
PLAYRE_BODYPARTS_TEMPLATE = 'hardcoded_inis/static_content/bodyparts_player.ini'

MOUSE = "mouse_speed"
GAMMA = "gamma_ramp"

KEEPED_KEYS = [
    MOUSE,
    GAMMA,
    "audio_music",
    "audio_ambient",
    "audio_sfx",
    "audio_interface",
    "audio_voice",
    "skip_transition_scripts",
    "enable_tooltips",
    "enable_rollover",
    "cockpit",
    "autohide_maneuver_bar",
]
DEFAULT_ALL = '1.0'
DEFAULT_MOUSE = '0.5'
DEFAULT_GAMMA = '0.3'


class OptionsManager:

    def __init__(self, tpl_manager, config):
        self.tpl_manager = tpl_manager
        self.config = config
        self.exist_perf_options = {}

        self.load_perf_options()

        # self.sync_data()  # run it from launcher

    def load_perf_options(self):
        for line in DataFolder().get_perf_options():
            split_line = line.split('=')
            if len(split_line) == 2:
                key = split_line[0].strip()
                value = split_line[1].strip()

                if key in KEEPED_KEYS:
                    self.exist_perf_options[key] = value

        for key in KEEPED_KEYS:
            if key not in self.exist_perf_options:
                default = DEFAULT_ALL
                if key == MOUSE:
                    default = DEFAULT_MOUSE
                elif key == GAMMA:
                    default = DEFAULT_GAMMA
                self.exist_perf_options[key] = default

    def get_perf_options_content(self):
        context = self.config.get_perf_options_params()
        context.update(self.exist_perf_options)
        return self.tpl_manager.get_result(PERF_OPTIONS_TEMPLATE, context)

    def get_hud_shift_content(self):
        return self.tpl_manager.get_result(HUD_SHIFT_TEMPLATE, self.config.get_hud_shift_params())

    def get_cameras_content(self):
        return self.tpl_manager.get_result(CAMERAS_TEMPLATE, self.config.get_cameras_params())

    def get_front_light_content(self):
        return self.tpl_manager.get_result(FRONT_LIGHT_TEMPLATE, self.config.get_front_light_params())

    def get_contrail_content(self):
        return self.tpl_manager.get_result(CONTRAIL_TEMPLATE, self.config.get_contrail_params())

    def get_player_bodyparts_content(self):
        return self.tpl_manager.get_result(PLAYRE_BODYPARTS_TEMPLATE, self.config.get_player_bodyparts_params())

    def sync_data(self):
        data_folder = DataFolder()
        data_folder.sync_perf_options(self.get_perf_options_content())
        data_folder.sync_hud_shift(self.get_hud_shift_content())
        data_folder.sync_cameras(self.get_cameras_content())
        data_folder.sync_front_light(self.get_front_light_content())
        data_folder.sync_contrail(self.get_contrail_content())
        data_folder.sync_player_bodyparts(self.get_player_bodyparts_content())



