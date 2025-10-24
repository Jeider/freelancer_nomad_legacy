import json
import pathlib


class ScreenMeta:

    @staticmethod
    def get_database_file_location():
        current_path = pathlib.Path().resolve()
        return current_path / 'startup' / 'meta.json'

    def __init__(self):
        db_file_loc = self.get_database_file_location()
        if not db_file_loc.exists():
            raise Exception('options meta database file is not exist')

        try:
            with open(db_file_loc) as db_file:
                self.db = json.load(db_file)

        except json.JSONDecodeError as e:
            raise Exception(f'Could not previous options metadata. Reason: {e}')

    def get_default_horizontal(self):
        return self.db['default_horizontal']

    def get_default_status_shift(self):
        return self.db['default_status_shift']

    def get_default_wide_weapons(self):
        return self.db['default_wide_weapons']

    def get_aspect_ratio_data(self, aspect_ratio):
        return self.db['aspect_ratios'].get(aspect_ratio)

    def get_resolutions(self):
        return self.db['resolutions']

    def get_front_light_colors(self):
        return self.db['front_light_colors']

    def get_contrails(self):
        return self.db['contrails']

    def get_bodies(self):
        return self.db['bodies']

    def get_gloves_per_body(self):
        return self.db['gloves_per_body']

    def get_hats(self):
        return self.db['hats']

    def get_commhelmets(self):
        return self.db['commhelmets']

    def get_left_gloves(self):
        return self.db['left_gloves']

    def get_right_gloves(self):
        return self.db['right_gloves']

    def get_resolutions_joined(self):
        return [f"{w}x{h}" for w, h in self.db['resolutions']]
