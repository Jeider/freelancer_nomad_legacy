import re


class VoiceLine(object):
    COMMENT_START = "<span class='comment'>("
    COMMENT_END = ")</span>"

    def __init__(self, index, actor, ru='', en='', comment=''):
        self.index = index
        self.actor = actor
        self.ru = ru
        self.en = en
        self.comment = comment

    def get_ru_replaced_text(self):
        return self.ru.replace('(', self.COMMENT_START).replace(')', self.COMMENT_END)

    def get_ru_story_text(self):
        content = self.get_ru_replaced_text()

        return f'{self.actor.RU_NAME}: {content}'

    def get_ru_clean_text(self):
        return re.sub(r'\(.*?\)', '', self.ru)

    def get_ru_subtitle(self):
        return f'{self.actor.RU_NAME}:\n{self.get_ru_clean_text()}'
