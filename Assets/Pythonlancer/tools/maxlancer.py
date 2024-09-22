import json
import pathlib

ENTITY_FILE_FORMAT = '{}.lua'

ENTITY_NAME = 'entity_name'
POS = 'pos'
ORIENT = 'orient'

SCANNED_KEYS = [
    ENTITY_NAME,
    POS,
    ORIENT,
]


class SceneEntityManager(object):

    def __init__(self, entities_filename):
        self.name = entities_filename
        self.entities_db = {}

    def add_entity(self, entity):
        self.entities_db[entity.get_name()] = entity

    def get_entity(self, entity_name):
        return self.entities_db[entity_name.lower()]

    def get_first_match_entity(self, name_like):
        for key, item in self.entities_db.items():
            if name_like in key:
                return item

    def load_entities(self, text_content):
        entity = None
        last_key = None
        for line in text_content:
            split_line = line.split('=')
            if len(split_line) < 2:
                continue

            line_key = split_line[0].strip().lower()
            line_value = split_line[1].strip().lower()

            if line_key not in SCANNED_KEYS:
                continue

            last_key = line_key

            if line_key == ENTITY_NAME:
                if entity:
                    self.add_entity(entity)
                entity = SceneEntity(name=line_value)
            elif line_key == POS:
                entity.parse_pos_from_lua(line_value)
            elif line_key == ORIENT:
                entity.parse_matrix_from_lua(line_value)

        # add final item
        if last_key == ORIENT:
            self.add_entity(entity)


class SceneEntity(object):
    NAME_REPLACES = (
        ('"', ''),
        (',', ''),
    )
    POS_REPLACES = (
        ('{', '['),
        ('},', ']'),
        ('}', ']'),
    )
    MATRIX_REPLACES = (
        ('{', '['),
        ('}', ']'),
    )

    def __init__(self, name):
        self.name = self.clear_name(name)
        self.pos = None
        self.orient_matrix = None

    def get_name(self):
        return self.name

    def clear_name(self, raw_name):
        for str_from, str_to in self.NAME_REPLACES:
            raw_name = raw_name.replace(str_from, str_to)
        return raw_name

    def clear_pos(self, raw_pos):
        for str_from, str_to in self.POS_REPLACES:
            raw_pos = raw_pos.replace(str_from, str_to)
        return raw_pos

    def clear_matrix(self, raw_matrix):
        for str_from, str_to in self.MATRIX_REPLACES:
            raw_matrix = raw_matrix.replace(str_from, str_to)
        return raw_matrix

    def parse_pos_from_lua(self, lua_pos):
        """pos be like: {-8.14873, 1.61406, -1.12203}"""
        try:
            pos = json.loads(self.clear_pos(lua_pos))
            if len(pos) != 3:
                raise Exception('Invalid pos for entity %s. Reason: not 3 elements in root' % self.name)
            self.pos = pos
        except json.JSONDecodeError:
            raise Exception('Invalid pos for entity %s. Reason: could not be decoded' % self.name)

    def parse_matrix_from_lua(self, lua_matrix):
        """matrix be like: {{1.0, 0.0, 0.0}, {0.0, 1.0, 0.0}, {0.0, 0.0, 1.0}}"""
        try:
            matrix = json.loads(self.clear_matrix(lua_matrix))
            if len(matrix) != 3:
                raise Exception('Invalid matrix for entity %s. Reason: not 3 elements in root' % self.name)
            for mx in matrix:
                if len(mx) != 3:
                    raise Exception('Invalid matrix for entity %s. Reason: not 3 elements in children' % self.name)
            self.orient_matrix = matrix
        except json.JSONDecodeError:
            raise Exception('Invalid matrix for entity %s. Reason: could not be decoded' % self.name)


class SceneEntityLoader(object):

    @staticmethod
    def get_lua_scripts_path():
        current_path = pathlib.Path().resolve()
        return current_path / 'story' / 'cutscenes' / 'entities'

    @staticmethod
    def get_entities_text_content(entities_filename):
        entities_path = SceneEntityLoader.get_lua_scripts_path()
        entities_file = open(entities_path / ENTITY_FILE_FORMAT.format(entities_filename))
        file_content = entities_file.readlines()
        entities_file.close()
        return file_content

    @staticmethod
    def get_entity_manager(entities_filename):
        text_content = SceneEntityLoader.get_entities_text_content(entities_filename)
        manager = SceneEntityManager(entities_filename)
        manager.load_entities(text_content)
        return manager
