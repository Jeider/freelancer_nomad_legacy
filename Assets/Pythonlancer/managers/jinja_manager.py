from jinja2 import Environment, FileSystemLoader, StrictUndefined

TEMPLATES_DIRECTORY = 'templates'


class JinjaTemplateManager(object):

    def __init__(self):
        self.environment = Environment(loader=FileSystemLoader(TEMPLATES_DIRECTORY), undefined=StrictUndefined)

    def get_result(self, template, context):
        template = self.environment.get_template(template)
        return template.render(context)
