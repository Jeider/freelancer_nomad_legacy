from pathlib import Path

CONTENT_DIR = Path().resolve() / 'templates' / 'hardcoded_inis' / 'static_content'


class BaseTemplate(object):
    TEMPLATE = None

    def format(self, params):
        raise NotImplementedError


class SimpleTemplate(BaseTemplate):
    TEMPLATE = None

    def format(self, params):
        if not self.TEMPLATE:
            raise Exception('TEMPLATE is required')
        return self.TEMPLATE.format(**params)


class FileTemplate(BaseTemplate):
    FILE = None

    def format(self, params):
        if not self.FILE:
            raise Exception('FILE is required')

        response_file = open(CONTENT_DIR / self.FILE, "r")
        return ''.join(response_file).format(**params)


class ColorZoneTemplate(SimpleTemplate):
    COLOR_RGB = tuple()
