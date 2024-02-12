from pathlib import Path

OUTPUT_FOLDER = Path('results')


class FileWriter():

    @staticmethod
    def write(file, data):
        filepath = OUTPUT_FOLDER / file
        filepath.write_text(data, encoding='utf-8')

    @staticmethod
    def write_to_subfolder(subfolder, file, data):
        filepath = OUTPUT_FOLDER / subfolder / file
        filepath.write_text(data, encoding='utf-8')
