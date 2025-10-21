from startup.aspect_ratio import get_aspect_ratio

# import os
# os.chdir('c:\\documents and settings\\flow_model')
# os.system('"C:\\Documents and Settings\\flow_model\\flow.exe"')


class StartupConfig:
    def __init__(self, screen_meta, resolution, russian=True, windowed=False, fovy=None):
        self.screen_meta = screen_meta
        self.resolution = resolution
        self.windowed = windowed
        self.fovy = fovy
        self.russian = russian

        self.horizontal = None
        self.status_shift = None

        self.aspect_ratio = get_aspect_ratio(*self.resolution)
        aspect_str = f'{self.aspect_ratio[0]}:{self.aspect_ratio[1]}'
        print(aspect_str)

        if ratio_data := self.screen_meta.get_aspect_ratio_data(aspect_str):
            self.horizontal = ratio_data['horizontal']
            self.status_shift = ratio_data['status_shift']

    def get_horizontal(self):
        return self.horizontal if self.horizontal else self.screen_meta.get_default_horizontal()

    def get_status_shift(self):
        return self.status_shift if self.status_shift else self.screen_meta.get_default_status_shift()

    def get_startup_params(self):
        pass

    def get_perf_options_params(self):
        return {
            'difficulty': 1.00,
            'width': self.resolution[0],
            'height': self.resolution[1],
        }

    def get_hud_shift_params(self):
        return {
            'horizontal': self.get_horizontal(),
            'status_shift': self.get_status_shift(),
            'wide_weapon_groups': False,
        }

    def get_cameras_params(self):
        return {
            'third_person_params': 'fovx=70',
            'turret_params': '',
            'rear_view_params': '',
        }
