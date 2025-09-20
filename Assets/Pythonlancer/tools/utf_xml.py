import os
import shutil
import subprocess
import pathlib


UTF_XML_DIR = 'UTF_XML'
INPUT_DIR = 'INPUT'
OUT_DIR = 'OUT'
TMP_REQUEST_FILE_NAME = 'tmp.xml'
MASS_ENCODE_INPUT_DIR = 'MASS_ENCODE_INPUT'
MASS_ENCODE_OUT_DIR = 'MASS_ENCODE_OUT'


class UTF_XML(object):
    EXECUTABLE = 'UTFXML.exe'

    @staticmethod
    def get_utf_xml_path():
        current_path = pathlib.Path().resolve()
        return current_path.parent / UTF_XML_DIR

    @staticmethod
    def get_mass_input_path():
        return UTF_XML.get_utf_xml_path() / 'MASS_DECODE_INPUT'

    @staticmethod
    def get_mass_output_path():
        return UTF_XML.get_utf_xml_path() / 'MASS_DECODE_OUT'

    @classmethod
    def run_command(cls, request_file_name, flags=None):
        utf_xml_path = cls.get_utf_xml_path()
        exec_path = utf_xml_path / UTF_XML.EXECUTABLE
        exec_params = [exec_path]

        if flags and len(flags):
            for flag in flags:
                exec_params.append(f'-{flag}')

        exec_params.append('-o')
        exec_params.append(cls.get_mass_output_path())
        exec_params.append(cls.get_mass_input_path() / request_file_name)
        # UTFXML.exe -i -g -a br_warwick_trader.cmp
        # UTFXML [-agitdrcC] [-s strings] [-o path] [file]

        result = subprocess.run(exec_params)
        if result.returncode != 0:
            raise Exception(f'Cant process file {request_file_name} by UTF_XML, aborting')

    @staticmethod
    def decode_file(request_file_name, flags=None):
        UTF_XML.run_command(request_file_name, flags=flags)

    @classmethod
    def mass_decode_utf(cls):
        flags = ['i']
        input_folder = cls.get_mass_input_path()

        for file in input_folder.iterdir():
            if not file.is_file():
                continue

            cls.decode_file(file.name, flags=flags)


class XML_UTF(object):
    EXECUTABLE = 'XMLUTF.exe'

    @staticmethod
    def get_utf_xml_path():
        current_path = pathlib.Path().resolve()
        return current_path.parent / UTF_XML_DIR

    @staticmethod
    def get_out_path():
        return XML_UTF.get_utf_xml_path() / OUT_DIR

    @staticmethod
    def run_command(request_file_name, input_dir, out_dir):
        utf_xml_path = XML_UTF.get_utf_xml_path()
        exec_path = utf_xml_path / XML_UTF.EXECUTABLE
        exec_params = [exec_path]
        exec_params.append('-O')
        exec_params.append(utf_xml_path / out_dir)
        exec_params.append(utf_xml_path / input_dir / request_file_name)

        result = subprocess.run(exec_params)
        if result.returncode != 0:
            raise Exception(f'Cant process file {request_file_name} by XML_UTF, aborting')

    @staticmethod
    def create_input_file(input_file, request_file_name):
        utf_xml_path = XML_UTF.get_utf_xml_path()
        tmp_file_path = utf_xml_path / INPUT_DIR / request_file_name
        tmp_file_path.write_text(input_file, encoding='utf-8')

    @staticmethod
    def process_xmls(xmls):
        for xml in xmls:
            XML_UTF.create_input_file(xml, TMP_REQUEST_FILE_NAME)
            XML_UTF.run_command(TMP_REQUEST_FILE_NAME, input_dir=INPUT_DIR, out_dir=OUT_DIR)


    @classmethod
    def mass_encode_updated_xml(cls, upgraded_subfilename, subfile_upgrades, file_upgrades, filename_upgrades):
        input_folder = cls.get_utf_xml_path() / MASS_ENCODE_INPUT_DIR
        output_folder = cls.get_utf_xml_path() / MASS_ENCODE_OUT_DIR

        # make upgrades
        for file in input_folder.iterdir():
            if file.is_file():
                extension = file.suffix
                if extension != '.xml':
                    continue

                file_content = file.read_text()

                for init_string, upgrade in file_upgrades:
                    file_content = file_content.replace(init_string, upgrade)

                file.write_text(file_content, encoding='utf-8')

            else:
                for subfile in file.iterdir():
                    if subfile.is_file():
                        subfile_content = subfile.read_text()

                        for init_string, upgrade in subfile_upgrades:
                            subfile_content = subfile_content.replace(init_string, upgrade)

                        subfile.write_text(subfile_content, encoding='utf-8')

        # process final
        for file in input_folder.iterdir():
            if not file.is_file():
                continue

            extension = file.suffix
            if extension == '.xml':
                XML_UTF.run_command(file.name, input_dir=MASS_ENCODE_INPUT_DIR, out_dir=MASS_ENCODE_OUT_DIR)

            elif extension == '.sur':

                new_name = file.name
                for init_string, upgrade in filename_upgrades:
                    new_name = new_name.replace(init_string, upgrade)

                shutil.copy(file, output_folder / new_name)








