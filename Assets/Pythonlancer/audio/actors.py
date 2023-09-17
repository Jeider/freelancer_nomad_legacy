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


class Trent(Actor):
    TYPE = ACTOR_TRENT
    NAME = 'trent'


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


class MaleCaptain(Actor)
    TYPE = ACTOR_MALE
    NAME = 'captain'


class RedLeader(Actor):
    TYOE = ACTOR_MALE
    NAME = 'red'
