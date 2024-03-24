import pathlib

LOADOUTS_GEN = 'loadout_gen.ini'


class DataFolder(object):

    @staticmethod
    def get_root():
        current_path = pathlib.Path().resolve()
        return current_path.parent.parent / 'DATA'

    @classmethod
    def get_equip(cls):
        return cls.get_root() / 'EQUIPMENT'

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
    def sync_to_test_workspace(cls, content):
        system_file = cls.get_universe() / 'GENERATION_DATA' / 'WORKSPACE' / 'test.ini'
        system_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_system_mod(cls, system_name, system_folder, content):
        system_file = cls.get_universe() / 'SYSTEMS_MOD' / system_folder / f'{system_name}.ini'
        system_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_asteroid_definition(cls, definition_name, subfolder, content):
        asteroid_file = cls.get_solar() / 'ASTEROIDS_MOD' / subfolder / f'{definition_name}.ini'
        asteroid_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_templated_nebula(cls, nebula_file_name, subfolder, content):
        nebula_file = cls.get_solar() / 'NEBULA_MOD' / subfolder / f'{nebula_file_name}.ini'
        nebula_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_interior(cls, interior_file_name, content):
        asteroid_file = cls.get_universe() / 'GENERATED_INTERIORS' / f'{interior_file_name}.ini'
        asteroid_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_equip(cls, equip_file_name, subfolder, content):
        equip_file = cls.get_equip()  / subfolder / f'{equip_file_name}.ini'
        equip_file.write_text(content, encoding='utf-8')

    @classmethod
    def sync_equip_hardcoded(cls, equip_file_name, content):
        equip_file = cls.get_equip()  / f'{equip_file_name}.ini'
        equip_file.write_text(content, encoding='utf-8')
