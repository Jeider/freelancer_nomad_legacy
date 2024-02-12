import subprocess
import pathlib
import os
import re


UTF_XML_DIR = 'UTF_XML'
INPUT_DIR = 'INPUT'
OUT_DIR = 'OUT'
TMP_REQUEST_FILE_NAME = 'tmp.xml'


class XML_UTF(object):
    EXECUTABLE = 'XMLUTF.exe'

    @staticmethod
    def get_utf_xml_path():
        current_path = pathlib.Path().resolve()
        return current_path.parent / UTF_XML_DIR

    @staticmethod
    def run_command(request_file_name):
        utf_xml_path = XML_UTF.get_utf_xml_path()
        exec_path = utf_xml_path / XML_UTF.EXECUTABLE
        exec_params = [exec_path]
        exec_params = [exec_path]
        exec_params.append('-O')
        exec_params.append(utf_xml_path / OUT_DIR)
        exec_params.append(utf_xml_path / INPUT_DIR / request_file_name)

        result = subprocess.run(exec_params)
        if result.returncode != 0:
            raise Exception('Cant process file request_file_name by XML_UTF, aborting')

    @staticmethod
    def create_input_file(input_file, request_file_name):
        utf_xml_path = XML_UTF.get_utf_xml_path()
        tmp_file_path = utf_xml_path / INPUT_DIR / request_file_name
        tmp_file_path.write_text(input_file, encoding='utf-8')

    @staticmethod
    def send_xml_utf_request(request_file_name):
        XML_UTF.run_command(request_file_name)

    @staticmethod
    def process_xmls(xmls):
        for xml in xmls:
            XML_UTF.create_input_file(xml, TMP_REQUEST_FILE_NAME)
            XML_UTF.send_xml_utf_request(TMP_REQUEST_FILE_NAME)
