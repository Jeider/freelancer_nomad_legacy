import json
import pathlib


class MetaDatabase:

    @staticmethod
    def get_database_file_location():
        current_path = pathlib.Path().resolve()
        return current_path / 'story' / 'cutscenes' / 'db' / 'audio_meta.json'

    def __init__(self):
        db_file_loc = self.get_database_file_location()
        if not db_file_loc.exists():
            raise Exception('cutscene meta database file is not exist')

        try:
            with open(db_file_loc) as db_file:
                self.db = json.load(db_file)

        except json.JSONDecodeError as e:
            raise Exception(f'Could not previous cutscene metadata. Reason: {e}')

    def save_db(self):
        with open(self.get_database_file_location(), 'w') as db_file:
            json.dump(self.db, db_file)

    def set_meta(self, line, meta):
        self.db[line] = meta
        self.save_db()


class MetaManager:

    def __init__(self):
        self.meta_db = MetaDatabase()

    def edit_voice_line_interactive(self):
        pass

    def edit_cutscene_interactive(self, cutscene):
        pass

