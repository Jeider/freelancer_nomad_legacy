class SimpleTemplate(object):
    TEMPLATE = None

    def format(self, params):
        return self.TEMPLATE.format(**params)

