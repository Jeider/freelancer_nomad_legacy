class SimpleTemplate(object):
    TEMPLATE = None

    def format(self, params):
        return self.TEMPLATE.format(**params)


class ColorZoneTemplate(SimpleTemplate):
    COLOR_RGB = tuple()
