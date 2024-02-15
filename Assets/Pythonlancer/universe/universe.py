class Universe(object):

    def __init__(self):
        self.systems_list = []
        self.systems_db = []

    def add_system(self, system):
        self.systems_list.append(system)
        self.systems_db[system.NAME] = system
