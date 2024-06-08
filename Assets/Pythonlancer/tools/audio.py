from tools.utf_xml import XML_UTF
from tools.data_folder import DataFolder


STORY_FILES = [
    # 'echo_m01',
    # 'echo_m01_player',
    # 'echo_m02',
    # 'echo_m02_player',
    'echo_m03',
    'echo_m03_player',
    # 'echo_m04',
    # 'echo_m04_female',
    # 'echo_m04_player',
    # 'echo_m05',
    # 'echo_m05_female',
    # 'echo_m05_player',
    # 'echo_m06',
    # 'echo_m06_female',
    # 'echo_m06_player',
    # 'echo_m07',
    # 'echo_m07_female',
    # 'echo_m07_player',
    # 'echo_m08',
    # 'echo_m08_female',
    # 'echo_m08_player',
]
STORY_XML_TEMPLATE = '{file}.utf.xml'
STORY_UTF_TEMPLATE = '{file}.utf'

STORY_FOLDER_TEMPLATE = '../AUDIO_XML_RU_APPLY/{file}.xml'


class AudioCompiler(object):

    @classmethod
    def compile_story(cls):
        for file in STORY_FILES:
            XML_UTF.run_command(
                STORY_XML_TEMPLATE.format(file=file),
                STORY_FOLDER_TEMPLATE.format(file=file),
            )
            out_file_name = STORY_UTF_TEMPLATE.format(file=file)
            new_xml = XML_UTF.get_out_path() / out_file_name

            DataFolder.move_story_audio(
                new_xml,
                out_file_name,
            )
