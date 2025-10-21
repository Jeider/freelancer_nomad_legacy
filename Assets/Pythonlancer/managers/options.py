from tools.data_folder import DataFolder


PERF_OPTIONS_TEMPLATE = 'hardcoded_inis/static_content/PerfOptions.ini'
HUD_SHIFT_TEMPLATE = 'hardcoded_inis/static_content/HudShift.ini'
CAMERAS_TEMPLATE = 'hardcoded_inis/static_content/cameras.ini'


class OptionsManager:

    def __init__(self, tpl_manager, config):
        self.tpl_manager = tpl_manager
        self.config = config

        # self.sync_data()  # run it from launcher

    def get_perf_options_content(self):
        return self.tpl_manager.get_result(PERF_OPTIONS_TEMPLATE, self.config.get_perf_options_params())

    def get_hud_shift_content(self):
        return self.tpl_manager.get_result(HUD_SHIFT_TEMPLATE, self.config.get_hud_shift_params())

    def get_cameras_content(self):
        return self.tpl_manager.get_result(CAMERAS_TEMPLATE, self.config.get_cameras_params())

    def sync_data(self):
        DataFolder.sync_perf_options(self.get_perf_options_content())
        DataFolder.sync_hud_shift(self.get_hud_shift_content())
        DataFolder.sync_cameras(self.get_cameras_content())
