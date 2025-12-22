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

    @classmethod
    def extract_fog_color(cls):
        is_fog = False
        for line in cls.TEMPLATE.splitlines():
            if line.strip() == '[Fog]':
                is_fog = True

            if is_fog and line.strip().startswith('color'):
                return line.split('=')[1].strip()

        raise Exception(f'fog not found for {cls}')

    @classmethod
    def extract_exterior_color(cls):
        is_exterior = False
        for line in cls.TEMPLATE.splitlines():
            if line.strip() == '[Exterior]':
                is_exterior = True

            if is_exterior and line.strip().startswith('color'):
                return line.split('=')[1].strip()

        raise Exception(f'fog not found for {cls}')


class FileTemplate(BaseTemplate):
    FILE = None

    def format(self, params):
        if not self.FILE:
            raise Exception('FILE is required')

        response_file = open(CONTENT_DIR / self.FILE, "r")
        return ''.join(response_file).format(**params)


class ColorZoneTemplate(SimpleTemplate):
    COLOR_RGB = tuple()
