ACTOR_MALE = 'male'
ACTOR_TRENT = 'trent'
ACTOR_FEMALE = 'female'


class Actor(object):
    TYPE = None
    NAME = None

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    @classmethod
    def is_male(cls):
        return cls.TYPE == ACTOR_MALE

    @classmethod
    def is_female(cls):
        return cls.TYPE == ACTOR_FEMALE

    @classmethod
    def is_player(cls):
        return cls.TYPE == ACTOR_TRENT


class Trent(Actor):
    TYPE = ACTOR_TRENT
    NAME = 'trent'
    COMM_APPEARANCE = 'pi_pirate5_head, player_body, player_commhelmet'


class Hatcher(Actor):
    TYPE = ACTOR_FEMALE
    NAME = 'hatcher'


class Darcy(Actor):
    TYPE = ACTOR_FEMALE
    NAME = 'darcy'


class Tilton(Actor):
    TYPE = ACTOR_MALE
    NAME = 'tilton'


class Brighton(Actor):
    TYPE = ACTOR_MALE
    NAME = 'brighton'


class MaleCaptain(Actor):
    TYPE = ACTOR_MALE
    NAME = 'captain'


class RedLeader(Actor):
    TYPE = ACTOR_MALE
    NAME = 'red'
