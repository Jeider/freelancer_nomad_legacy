import pathlib

LOADOUTS_GEN = 'loadout_gen.ini'


class DataFolder(object):

    @staticmethod
    def get_root():
        current_path = pathlib.Path().resolve()
        return current_path.parent.parent / 'DATA'

    @classmethod
    def get_solar(cls):
        return cls.get_root() / 'SOLAR'

    @classmethod
    def get_universe(cls):
        return cls.get_root() / 'UNIVERSE'

    @classmethod
    def sync_solar_gen_loadouts(cls, content):
        loadouts_file = cls.get_solar() / LOADOUTS_GEN
        loadouts_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_system_mod(cls, system_name, system_folder, content):
        system_file = cls.get_universe() / 'SYSTEMS_MOD' / system_folder / f'{system_name}.ini'
        system_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_asteroid_definition(cls, definition_name, subfolder, content):
        asteroid_file = cls.get_solar() / 'ASTEROIDS_MOD' / subfolder / f'{definition_name}.ini'
        asteroid_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_interior(cls, interior_file_name, content):
        asteroid_file = cls.get_universe() / 'GENERATED_INTERIORS' / f'{interior_file_name}.ini'
        asteroid_file.write_text(content, encoding='utf-8')
