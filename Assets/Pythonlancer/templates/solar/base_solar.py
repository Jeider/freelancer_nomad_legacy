

class MineableSolar(object):
    ALIAS = None

    def get_default_archetype(self):
        raise NotImplementedError

    def get_medium_reward_archetype(self):
        raise NotImplementedError

    def get_high_reward_archetype(self):
        raise NotImplementedError

    def get_ultra_reward_archetype(self):
        raise NotImplementedError
