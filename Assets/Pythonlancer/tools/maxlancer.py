import json
import pathlib
import re

ENTITY_FILE_FORMAT = '{}.lua'

ENTITY_NAME = 'entity_name'
POS = 'pos'
ORIENT = 'orient'

SCANNED_KEYS = [
    ENTITY_NAME,
    POS,
    ORIENT,
]

_COMMENT = re.compile(r'--[^\n]*')
_ENTITY_NAME = re.compile(r'entity_name\s*=\s*"([^"]+)"', re.I)
_POS = re.compile(r'\bpos\s*=\s*\{([^{}]*)\}', re.I)
_ORIENT = re.compile(
    r'\borient\s*=\s*\{\s*\{([^{}]+)\}\s*,\s*\{([^{}]+)\}\s*,\s*\{([^{}]+)\}\s*\}',
    re.I | re.S,
)
_QORIENT = re.compile(r'\bq_orient\s*=\s*\{([^{}]+)\}', re.I)


def quat_to_matrix(quaternion):
    weight, x, y, z = quaternion
    return [
        [1 - 2 * (y * y + z * z), 2 * (x * y - z * weight), 2 * (x * z + y * weight)],
        [2 * (x * y + z * weight), 1 - 2 * (x * x + z * z), 2 * (y * z - x * weight)],
        [2 * (x * z - y * weight), 2 * (y * z + x * weight), 1 - 2 * (x * x + y * y)],
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
        if isinstance(text_content, str):
            text = text_content
        else:
            text = ''.join(
                line if line.endswith('\n') else line + '\n'
                for line in text_content
            )
        text = _COMMENT.sub('', text)
        matches = list(_ENTITY_NAME.finditer(text))
        for index, match in enumerate(matches):
            end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            window = text[match.end():end]
            entity = SceneEntity(name=match.group(1).lower())
            pos = _POS.search(window)
            orient = _ORIENT.search(window)
            quaternion = _QORIENT.search(window)
            if pos:
                entity.parse_pos_from_lua('{' + pos.group(1) + '}')
            if orient:
                rows = []
                for group in orient.groups():
                    rows.append(self._numbers(group))
                entity.parse_matrix_from_lua(json.dumps(rows))
            elif quaternion:
                entity.orient_matrix = quat_to_matrix(self._numbers(quaternion.group(1)))
            if entity.pos is not None:
                self.add_entity(entity)

    @staticmethod
    def _numbers(raw):
        return [float(item) for item in re.findall(r'[-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?', raw)]


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
