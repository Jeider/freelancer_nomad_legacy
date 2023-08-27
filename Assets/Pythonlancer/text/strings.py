class StringCompiler(object):
    STRING_ITEM_TEMPLATE = '''{name_id}
{type}
{value}
'''
    NAME = 'NAME'
    INFOCARD = 'INFOCARD'

    @staticmethod
    def compile_name(name_id, value):
        return StringCompiler.STRING_ITEM_TEMPLATE.format(
            name_id=name_id,
            type=StringCompiler.NAME,
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
            type=StringCompiler.INFOCARD,
            value=value
        )

    @staticmethod
    def compile_infocards(data: dict[int, str]):
        items = [StringCompiler.compile_infocard(name_id, value) for name_id, value in data.items()]
        return ''.join(items)
