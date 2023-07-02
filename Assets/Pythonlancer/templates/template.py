class Template(object):
    TEMPLATE = None

    def format(self, params):
        return self.TEMPLATE.format(**params)

