class UniverseRoot(object):

    def __init__(self):
        self.systems_list = []
        self.systems_db = {}
        self.post_init_completed = False

    def add_system(self, system):
        self.systems_list.append(system)
        self.systems_db[system.NAME] = system

    def get_systems(self):
        if not self.post_init_completed:
            raise Exception('Systems is not post initialized')

        return self.systems_list

    def init_jumpgates(self):
        for system in self.systems_list:
            system.init_jumpgates()

    def do_post_init_actions(self):
        self.init_jumpgates()
        self.post_init_completed = True

    def get_system_by_name(self, system_name):
        try:
            return self.systems_db[system_name]
        except IndexError:
            raise Exception('System %s isnt presented in universe' % system_name)

    def get_system_by_class(self, system_class):
        try:
            return self.systems_db[system_class.NAME]
        except IndexError:
            raise Exception('System %s isnt presented in universe' % system_class.NAME)
