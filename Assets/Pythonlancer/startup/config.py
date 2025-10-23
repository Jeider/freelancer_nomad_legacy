from startup.aspect_ratio import get_aspect_ratio


class StartupConfig:
    def __init__(self, screen_meta, resolution, russian=True, windowed=False, fovx=None, fovy=None):
        self.screen_meta = screen_meta
        self.resolution = resolution
        self.windowed = windowed
        self.fovx = fovx
        self.fovy = fovy
        self.russian = russian

        self.horizontal = None
        self.status_shift = None
        self.wide_weapons = False

        self.aspect_ratio = get_aspect_ratio(*self.resolution)
        aspect_str = f'{self.aspect_ratio[0]}:{self.aspect_ratio[1]}'
        print(f'Used aspect ratio: {aspect_str}')

        if ratio_data := self.screen_meta.get_aspect_ratio_data(aspect_str):
            print('Use overrided settings of aspect ratio')
            self.horizontal = ratio_data['horizontal']
            self.status_shift = ratio_data['status_shift']
            self.wide_weapons = ratio_data['wide_weapons']

    def get_horizontal(self):
        return self.horizontal if self.horizontal else self.screen_meta.get_default_horizontal()

    def get_status_shift(self):
        return self.status_shift if self.status_shift else self.screen_meta.get_default_status_shift()

    def get_wide_weapons(self):
        return self.wide_weapons if self.wide_weapons is not None else self.screen_meta.get_default_wide_weapons()

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
            'wide_weapon_groups': self.get_wide_weapons(),
        }

    def get_cameras_params(self):
        fov_params = []
        if self.fovx is not None:
            fov_params.append(f"fovx={self.fovx}!")
        else:
            fov_params.append("fovx=70")
        if self.fovy is not None and self.fovy != 70:
            fov_params.append(f"fovy={self.fovy}")
        fov_string = "\n".join(fov_params)

        return {
            'third_person_params': fov_string,
            'turret_params': fov_string,
            'rear_view_params': fov_string,
        }
