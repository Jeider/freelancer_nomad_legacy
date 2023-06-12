from pathlib import Path

OUTPUT_FOLDER = Path('results')


class FileWriter():

    @staticmethod
    def write(file, data):
        filepath = OUTPUT_FOLDER / file
        filepath.write_text(data, encoding='utf-8')
