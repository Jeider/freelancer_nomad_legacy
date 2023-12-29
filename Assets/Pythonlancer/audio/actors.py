ACTOR_MALE = 'male'
ACTOR_TRENT = 'trent'
ACTOR_FEMALE = 'female'


class Actor(object):
    TYPE = None
    NAME = None
    COMM_APPEARANCE = ''

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
    COMM_APPEARANCE = 'ge_female1_head, br_darcy_body, comm_br_darcy_female'


class Tilton(Actor):
    TYPE = ACTOR_MALE
    NAME = 'tilton'


class Rockford(Actor):
    TYPE = ACTOR_MALE
    NAME = 'rockford'
    COMM_APPEARANCE = 'li_rockford_head, li_male_elite_body, comm_ge_generic2'


class Brighton(Actor):
    TYPE = ACTOR_MALE
    NAME = 'brighton'


class MaleCaptain(Actor):
    TYPE = ACTOR_MALE
    NAME = 'captain'


class RedLeader(Actor):
    TYPE = ACTOR_MALE
    NAME = 'red'


class Bandit(Actor):
    TYPE = ACTOR_MALE
    NAME = 'bandit'


class Tortuga(Actor):
    TYPE = ACTOR_MALE
    NAME = 'tortuga'
    COMM_APPEARANCE = 'br_quigly_head, sh_male2_body, prop_hat_male_pirate_a, prop_neuralnet_d'


class Barman(Actor):
    TYPE = ACTOR_MALE
    NAME = 'barman'
    COMM_APPEARANCE = 'sh_male2_head, pi_pirate4_body'
