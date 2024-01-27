import subprocess
import pathlib
import os
import re


TRACKS_DIR = 'TRACKS'
FILES_DIR = 'FILES'
TMP_REQUEST_FILE_NAME = 'tmp.ini'
TMP_RESPONSE_FILE_NAME = 'tmp-fl.ini'

REQUEST_FILE_TEMPLATE = '{filename}.ini'
RESPONSE_FILE_TEMPLATE = '{filename}-fl.ini'

TITLE_OBJECT = '[Object]'.lower()
TITLE_ZONE = '[Zone]'.lower()
TITLES = (TITLE_OBJECT, TITLE_ZONE)

MULTI_INT_KEYS = ('pos', 'rotate', 'size')


class TracksResponseItem(object):
    OBJECT = 'object'
    ZONE = 'zone'
    NAME_KEY = 'nickname'
    TRADELANE_MARKER = '_Tradelane_'
    PATH_MARKER = '_path_'
    PATH_LABEL_KEY = 'path_label'

    def __init__(self):
        self.title = None
        self.lines = {}
        self.raw_lines = []

    def set_title(self, title):
        self.title = title.replace('[', '').replace(']', '')

    def add_line(self, line):
        self.raw_lines.append(line)
        split_line = line.split('=')
        line_key = split_line[0].strip()
        line_value = split_line[1].strip()

        if line_key in MULTI_INT_KEYS:
            try:
                line_value = tuple(int(val) for val in line_value.split(','))
            except ValueError:
                raise Exception('Convertion error when parse from tracks')

        self.lines[line_key] = line_value

    def get_title(self):
        return self.title

    def get_lines(self):
        return self.lines

    def is_clean(self):
        return self.title is None or len(self.lines) == 0

    def is_object(self):
        return self.title.lower() == self.OBJECT

    def is_zone(self):
        return self.title.lower() == self.ZONE

    def is_tlr_zone(self):
        return self.is_zone() and self.TRADELANE_MARKER in self.lines[self.NAME_KEY] 

    def is_path_zone(self):
        return self.is_zone() and self.PATH_MARKER in self.lines[self.NAME_KEY] 

    def get_path_label(self):
        if not self.is_path_zone():
            raise Exception('Is not a path zone')

        return self.lines[self.PATH_LABEL_KEY].split(',')[0].strip()
        

'''


[Zone]
nickname = Zone_br_wrw_path_bounty_hunter1_1
pos = -55000, 0, -16500
rotate = -90, -73, 0
shape = CYLINDER
size = 750, 10440
usage = patrol
path_label = bounty_hunter1, 1
'''


class Tracks(object):
    EXECUTABLE = 'tracks.exe'

    @staticmethod
    def get_tracks_path():
        current_path = pathlib.Path().resolve()
        return current_path.parent / TRACKS_DIR

    @staticmethod
    def run_command(request_file_name):
        tracks_path = Tracks.get_tracks_path()
        exec_path = tracks_path / Tracks.EXECUTABLE
        exec_params = [exec_path]
        exec_params.append(tracks_path / FILES_DIR / request_file_name)

        result = subprocess.run(exec_params)
        if result.returncode != 0:
            raise Exception('Cant process file request_file_name by tracks, aborting')

    @staticmethod
    def create_input_file(input_file, request_file_name):
        tracks_path = Tracks.get_tracks_path()
        tmp_file_path = tracks_path / FILES_DIR / request_file_name
        tmp_file_path.write_text(input_file, encoding='utf-8')

    @staticmethod
    def send_tracks_request(request_file_name):
        Tracks.run_command(request_file_name)

    @staticmethod
    def get_tracks_response(response_file_name):
        tracks_path = Tracks.get_tracks_path()
        response_file = open(tracks_path / FILES_DIR / response_file_name, "r")
        file_content = response_file.readlines()
        response_file.close()
        return file_content

    @staticmethod
    def parse_tracks_response(response_content):
        parsed_objects = []
        current_obj = TracksResponseItem()
        parsed_objects.append(current_obj)
        first_key = True

        for item in response_content:
            item_value = item.strip()
            if item_value == '':
                continue

            if item_value.lower() in TITLES:
                if first_key:
                    first_key = False
                    current_obj.set_title(item_value)
                else:
                    current_obj = TracksResponseItem()
                    current_obj.set_title(item_value)
                    parsed_objects.append(current_obj)
                continue

            else:
                current_obj.add_line(item_value)

        return parsed_objects


    @staticmethod
    def get_tracks(tracks_request_file_content):
        Tracks.clear_temp_files()
        Tracks.create_input_file(tracks_request_file_content, TMP_REQUEST_FILE_NAME)
        Tracks.send_tracks_request(TMP_REQUEST_FILE_NAME)
        response_content = Tracks.get_tracks_response(TMP_RESPONSE_FILE_NAME)
        raw_items = Tracks.parse_tracks_response(response_content)
        Tracks.clear_temp_files()
        return raw_items


    @staticmethod
    def clear_temp_files():
        return
        tracks_path = Tracks.get_tracks_path()
        request_path = tracks_path / FILES_DIR / TMP_REQUEST_FILE_NAME
        if request_path.exists():
            request_path.unlink()
        response_path = tracks_path / FILES_DIR / TMP_RESPONSE_FILE_NAME
        if response_path.exists():
            response_path.unlink()


    @staticmethod
    def demo_request():
        DEMO_REQUEST_CONTENT = '''[Settings]
        system = test
        distance = 7000


        [TradeLane]
        number = 1
        count = 1

        first = -22090, 0, 21247, 1
        last = -31135, 0, -24551, 1

        zone = 2500, 1
        '''

        tracks = Tracks.get_tracks(DEMO_REQUEST_CONTENT)

        import pdb;pdb.set_trace()

