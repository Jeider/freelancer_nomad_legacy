class StringsMixin(object):
    def get_next_string_id(self):
        self.last_string_id += 1
        return self.last_string_id

    def get_next_infocard_id(self):
        self.last_infocard_id += 1
        return self.last_infocard_id
