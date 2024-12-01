import subprocess
import pathlib
import os


class CreateId(object):
    EXECUTABLE = 'createid.exe'
    GET_ID_PARAMS = ['-h', '-oc']

    @staticmethod
    def get_root_path():
        current_path = pathlib.Path().resolve()
        return current_path.parent.parent

    @staticmethod
    def run_command(nickname):
        root_path = CreateId.get_root_path()
        exec_path = root_path / CreateId.EXECUTABLE
        exec_params = [exec_path]
        exec_params.extend(CreateId.GET_ID_PARAMS)
        exec_params.append(nickname)

        cmd_output = subprocess.run(exec_params, cwd=root_path, capture_output=True)
        cmd_string = cmd_output.stdout.decode()
        return cmd_string.split(',')

        return items[1]

    @staticmethod
    def get_hex_id(nickname):
        return CreateId.run_command(nickname)[1]

    @staticmethod
    def get_audio_id(nickname):
        the_id = CreateId.get_hex_id(nickname)
        return f'0x{str(the_id)[2:].upper()}'

    @staticmethod
    def get_int_id(nickname):
        return CreateId.run_command(nickname)[0]
