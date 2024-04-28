ACTOR_MALE = 'male'
ACTOR_TRENT = 'trent'
ACTOR_FEMALE = 'female'


class Actor(object):
    TYPE = None
    NAME = None
    RU_NAME = None
    COMM_APPEARANCE = ''
    CUTSCENE_APPEARANCE = ''

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
    RU_NAME = 'Трент'
    TYPE = ACTOR_TRENT
    NAME = 'trent'
    COMM_APPEARANCE = 'pi_pirate5_head, player_body, player_commhelmet'


class Hatcher(Actor):
    RU_NAME = 'Хетчер'
    TYPE = ACTOR_FEMALE
    NAME = 'hatcher'
    COMM_APPEARANCE = 'pl_female2_head, li_hatcher_body, comm_li_hatcher_female'


class Darcy(Actor):
    RU_NAME = 'Дерси'
    TYPE = ACTOR_FEMALE
    NAME = 'darcy'
    COMM_APPEARANCE = 'ge_female1_head, br_darcy_body, comm_br_darcy_female'


class Tilton(Actor):
    RU_NAME = 'Тилтон'
    TYPE = ACTOR_MALE
    NAME = 'tilton'
    COMM_APPEARANCE = 'pl_male4_head, li_tilton_body'


class Rockford(Actor):
    RU_NAME = 'Рокфорд'
    TYPE = ACTOR_MALE
    NAME = 'rockford'
    COMM_APPEARANCE = 'li_rockford_head, li_male_elite_body, comm_ge_generic2'


class Brighton(Actor):
    RU_NAME = 'Брайтон'
    TYPE = ACTOR_MALE
    NAME = 'brighton'
    COMM_APPEARANCE = 'br_brighton_head, br_brighton_body'


class MaleCaptain(Actor):
    RU_NAME = 'Капитан'
    TYPE = ACTOR_MALE
    NAME = 'captain'
    COMM_APPEARANCE = 'li_captain_head, li_male_elite_body'


class RedLeader(Actor):
    RU_NAME = 'Красный лидер'
    TYPE = ACTOR_MALE
    NAME = 'red'
    COMM_APPEARANCE = 'li_captain_head, li_male_elite_body, comm_li_elite'


class Bandit(Actor):
    RU_NAME = 'Бандит'
    TYPE = ACTOR_MALE
    NAME = 'bandit'


class Tortuga(Actor):
    RU_NAME = 'Тортуга'
    TYPE = ACTOR_MALE
    NAME = 'tortuga'
    COMM_APPEARANCE = 'br_quigly_head, sh_male2_body, prop_hat_male_pirate_a, prop_neuralnet_d'


class Barman(Actor):
    RU_NAME = 'Бармен'
    TYPE = ACTOR_MALE
    NAME = 'barman'
    COMM_APPEARANCE = 'sh_male2_head, pi_pirate4_body'


class Yamamoto(Actor):
    RU_NAME = 'Ямамото'
    TYPE = ACTOR_MALE
    NAME = 'yamamoto'
    COMM_APPEARANCE = 'ku_tenji_head, pi_pirate4_body'
    CUTSCENE_APPEARANCE = 'tenji'


class Hassler(Actor):
    RU_NAME = 'Хасслер'
    TYPE = ACTOR_MALE
    NAME = 'hassler'
    # COMM_APPEARANCE = ''
    CUTSCENE_APPEARANCE = 'hassler'


class Kim(Actor):
    RU_NAME = 'Ким'
    TYPE = ACTOR_FEMALE
    NAME = 'kim'
    # COMM_APPEARANCE = ''
    CUTSCENE_APPEARANCE = 'kim'
