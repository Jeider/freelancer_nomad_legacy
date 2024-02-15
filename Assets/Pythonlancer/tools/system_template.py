import subprocess
import pathlib
import os
import re


TEMPLATES_FOLDER = 'SYSTEMS_TEMPLATES'

UTF_XML_DIR = 'UTF_XML'
INPUT_DIR = 'INPUT'
OUT_DIR = 'OUT'
TMP_REQUEST_FILE_NAME = 'tmp.xml'

TEMPLATE_FILE_FORMAT = '{}.ini'

NICKNAME = 'nickname'
POS = 'pos'
ROTATE = 'rotate'
SIZE = 'size'
SHAPE = 'shape'

MULTI_INT_KEYS = (POS, ROTATE, SIZE)
SCANNED_KEYS = (NICKNAME, POS, ROTATE, SIZE, SHAPE)


class SystemTemplate(object):

    def __init__(self, template_name, template_items):
        self.name = template_name
        self.items = template_items
        self.items_db = {}
        self.process_template_items()

    def process_template_items(self):
        for item in self.items:
            self.items_db[item.title] = item

    def get_items_db(self):
        return self.items_db

    def get_item_pos(self, item_key):
        return self.items_db[item_key].lines[POS]

    def get_item_rotate(self, item_key):
        return self.items_db[item_key].lines[ROTATE]

    def get_item_size(self, item_key):
        return self.items_db[item_key].lines[SIZE]

    def get_item_shape(self, item_key):
        return self.items_db[item_key].lines[SHAPE]


class SystemTemplateItem(object):

    def __init__(self):
        self.title = None
        self.raw_lines = {}
        self.lines = {}

    def set_title(self, title):
        self.title = title.replace('[', '').replace(']', '')

    def add_line(self, line_key, line_value):
        self.raw_lines[line_key] = line_value

        if line_key in MULTI_INT_KEYS:
            try:
                line_value = tuple(float(val) for val in line_value.split(','))
            except ValueError:
                raise Exception('Convertion error when parse from system template')

        self.lines[line_key] = line_value


class SystemTemplateLoader(object):

    @staticmethod
    def get_system_templates_path():
        current_path = pathlib.Path().resolve()
        return current_path.parent.parent / 'DATA' / 'UNIVERSE' / TEMPLATES_FOLDER

    def get_template_text_content(template_name):
        templates_path = SystemTemplateLoader.get_system_templates_path()
        template_file = open(templates_path / TEMPLATE_FILE_FORMAT.format(template_name))
        file_content = template_file.readlines()
        template_file.close()
        return file_content

    @staticmethod
    def parse_template(template_text_content):
        parsed_objects = []
        current_obj = SystemTemplateItem()
        parsed_objects.append(current_obj)
        first_key = True

        for line in template_text_content:
            split_line = line.split('=')
            if len(split_line) < 2:
                continue

            line_key = split_line[0].strip().lower()
            line_value = split_line[1].strip().lower()

            if line_key not in SCANNED_KEYS:
                continue

            if line_key == NICKNAME:
                if first_key:
                    first_key = False
                    current_obj.set_title(line_value)
                else:
                    current_obj = SystemTemplateItem()
                    current_obj.set_title(line_value)
                    parsed_objects.append(current_obj)
                continue

            else:
                current_obj.add_line(line_key, line_value)

        return parsed_objects

    @staticmethod
    def get_template(template_name):
        template_text_content = SystemTemplateLoader.get_template_text_content(template_name)
        parsed_content = SystemTemplateLoader.parse_template(template_text_content)
        template = SystemTemplate(template_name, parsed_content)
        return template
