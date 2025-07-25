NAME = 'NAME'
INFOCARD = 'INFOCARD'


class TheID:
    def __init__(self, id_value, text, kind):
        self.id = id_value
        self.text = text
        self.kind = kind

    def __str__(self):
        return str(self.id)

    def set_text(self, text):
        self.text = text

    def compile(self):
        return (
            StringCompiler.compile_name(self.id, self.text)
            if self.kind == NAME
            else StringCompiler.compile_infocard(self.id, self.text)
        )


class TheIndex:
    def __init__(self, id_value):
        self.id = id_value

    def __str__(self):
        return str(self.id)


class IDsDatabase:
    def __init__(self, db_name, start_id):
        self.db_name = db_name
        self.last_id = start_id
        self.ids = []

    def get_file_name(self):
        return f'strings_{self.db_name}.ini'

    def get_next_id(self):
        self.last_id += 1
        return self.last_id

    def add_force(self, the_id, text):
        the_id = TheID(the_id, text, kind=NAME)
        self.ids.append(the_id)
        return the_id

    def new_name(self, text):
        the_id = TheID(self.get_next_id(), text, kind=NAME)
        self.ids.append(the_id)
        return the_id

    def new_info(self, text):
        the_id = TheID(self.get_next_id(), text, kind=INFOCARD)
        self.ids.append(the_id)
        return the_id

    def compile(self):
        return ''.join([i.compile() for i in self.ids])


class IndexDatabase:
    def __init__(self, start_id):
        self.last_id = start_id
        self.ids = []

    def get_next_id(self):
        self.last_id += 1
        return self.last_id

    def new_id(self):
        the_id = TheIndex(self.get_next_id())
        self.ids.append(the_id)
        return the_id


class StringCompiler(object):
    STRING_ITEM_TEMPLATE = '''{name_id}
{type}
{value}
'''

    @staticmethod
    def compile_name(name_id, value):
        return StringCompiler.STRING_ITEM_TEMPLATE.format(
            name_id=name_id,
            type=NAME,
            value=value
        )

    @staticmethod
    def compile_names(data: dict[int, str]):
        items = [StringCompiler.compile_name(name_id, value) for name_id, value in data.items()]
        return ''.join(items)

    @staticmethod
    def compile_infocard(name_id, value):
        return StringCompiler.STRING_ITEM_TEMPLATE.format(
            name_id=name_id,
            type=INFOCARD,
            value=value
        )

    @staticmethod
    def compile_infocards(data: dict[int, str]):
        items = [StringCompiler.compile_infocard(name_id, value) for name_id, value in data.items()]
        return ''.join(items)
