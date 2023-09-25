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
    def run_command(executable, main_params, nickname):
        root_path = CreateId.get_root_path()
        exec_path = root_path / executable
        exec_params = [exec_path]
        exec_params.extend(main_params)
        exec_params.append(nickname)

        cmd_output = subprocess.run(exec_params, cwd=root_path, capture_output=True)
        cmd_string = cmd_output.stdout.decode()
        items = cmd_string.split(',')

        return items[1]

    @staticmethod
    def get_id(nickname):
        return CreateId.run_command(
            CreateId.EXECUTABLE,
            CreateId.GET_ID_PARAMS,
            nickname,
        )
