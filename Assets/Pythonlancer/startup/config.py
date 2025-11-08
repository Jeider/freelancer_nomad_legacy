from startup.aspect_ratio import get_aspect_ratio

DEFAULT_CONTRAIL = 'li_alt_contrail'
DEFAULT_FRONT_LIGHT_GLOW_COLOR = '255, 255, 255'
DEFAULT_FRONT_LIGHT_COLOR = '200, 200, 200'
DEFAULT_BODY = 'pl_male2_journeyman_body.dfm'
DEFAULT_COMMHELMET = 'comm_ge_generic2.3db'
DEFAULT_HAT = None
DEFAULT_EYEWEAR = None
DEFAULT_RIGHT_HAND = 'benchmarkmalehandright.dfm'
DEFAULT_LEFT_HAND = 'benchmarkmalehandleft.dfm'


class StartupConfig:
    def __init__(self, screen_meta, resolution, russian=True, windowed=False, fovx=None, fovy=None, dxwrapper=False,
                 front_light=None, contrail=None, player_body=None, player_commhelmet=None, player_hat=None,
                 difficulty_easy=False, difficulty_hard=False):
        self.screen_meta = screen_meta
        self.resolution = resolution
        self.windowed = windowed
        self.dxwrapper = dxwrapper
        self.fovx = fovx
        self.fovy = fovy
        self.russian = russian

        if difficulty_hard and difficulty_easy:
            raise Exception('Failed! Difficulty cannot be hard and easy at the same time')

        self.internal_difficulty = 1.0
        if difficulty_easy:
            self.internal_difficulty = 0.5
        elif difficulty_hard:
            self.internal_difficulty = 1.5

        self.horizontal = None
        self.status_shift = None
        self.wide_weapons = self.screen_meta.get_default_wide_weapons()

        self.front_light_glow_color = DEFAULT_FRONT_LIGHT_GLOW_COLOR
        self.front_light_color = DEFAULT_FRONT_LIGHT_COLOR
        self.contrail = DEFAULT_CONTRAIL
        self.player_body = DEFAULT_BODY
        self.player_commhelmet = DEFAULT_COMMHELMET
        self.player_hat = DEFAULT_HAT
        self.player_eyewear = DEFAULT_EYEWEAR
        self.player_left_hand = DEFAULT_LEFT_HAND
        self.player_right_hand = DEFAULT_RIGHT_HAND

        self.aspect_ratio = get_aspect_ratio(*self.resolution)
        aspect_str = f'{self.aspect_ratio[0]}:{self.aspect_ratio[1]}'
        print(f'Used aspect ratio: {aspect_str}')

        if ratio_data := self.screen_meta.get_aspect_ratio_data(aspect_str):
            print('Use overrided settings of aspect ratio')
            self.horizontal = ratio_data['horizontal']
            self.status_shift = ratio_data['status_shift']
            self.wide_weapons = ratio_data['wide_weapons']

        light_colors = self.screen_meta.get_front_light_colors()
        if front_light and front_light in light_colors:
            light_data = light_colors[front_light]
            self.front_light_glow_color = light_data['glow_color']
            self.front_light_color = light_data['color']

        contrails = self.screen_meta.get_contrails()
        if contrail and contrail in contrails:
            self.contrail = contrails[contrail]

        bodies = self.screen_meta.get_bodies()
        gloves_per_body = self.screen_meta.get_gloves_per_body()
        left_gloves = self.screen_meta.get_left_gloves()
        right_gloves = self.screen_meta.get_right_gloves()
        # hats = self.screen_meta.get_hats()  hats crashes :-(
        commhelmets = self.screen_meta.get_commhelmets()

        if player_body and player_body in bodies:
            self.player_body = bodies[player_body]
            if player_body in gloves_per_body:
                gloves = gloves_per_body[player_body]
                self.player_right_hand = right_gloves[gloves]
                self.player_left_hand = left_gloves[gloves]

        if player_commhelmet and player_commhelmet in commhelmets:
            self.player_commhelmet = commhelmets[player_commhelmet]
        #
        # if player_hat and player_hat in hats:
        #     self.player_hat = hats[player_hat]

    def get_horizontal(self):
        return self.horizontal if self.horizontal else self.screen_meta.get_default_horizontal()

    def get_status_shift(self):
        return self.status_shift if self.status_shift else self.screen_meta.get_default_status_shift()

    def get_wide_weapons(self):
        return self.wide_weapons

    def get_perf_options_params(self):
        return {
            'difficulty': self.internal_difficulty,
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
            fov_params.append(f"fovx = {self.fovx}!")
        else:
            fov_params.append("fovx = 70")
        if self.fovy is not None and int(self.fovy) != 70:
            fov_params.append(f"fovy = {self.fovy}")
        fov_string = "\n".join(fov_params)

        return {
            'third_person_params': fov_string,
            'turret_params': fov_string,
            'rear_view_params': fov_string,
        }

    def get_front_light_params(self):
        return {
            'glow_color': self.front_light_glow_color,
            'color': self.front_light_color,
        }

    def get_contrail_params(self):
        return {
            'contrail': self.contrail,
        }

    def get_player_bodyparts_params(self):
        return {
            'player_body': self.player_body,
            'player_hand_left': self.player_left_hand,
            'player_hand_right': self.player_right_hand,
            'player_hat': self.player_hat,
            'player_commhelmet': self.player_commhelmet,
            'player_eyewear': self.player_eyewear,
        }
