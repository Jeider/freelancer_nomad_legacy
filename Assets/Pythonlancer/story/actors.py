ACTOR_MALE = 'male'
ACTOR_TRENT = 'trent'
ACTOR_FEMALE = 'female'


class Actor(object):
    TYPE = None
    NAME = None
    RU_NAME = None
    NAME_ID = None
    COMM_APPEARANCE = None
    CUTSCENE_APPEARANCE = ''
    SPACE_VOICE = None

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
    NAME_ID = 93202
    TYPE = ACTOR_MALE
    NAME = 'hassler'
    COMM_APPEARANCE = 'rh_hassler_head, rh_male_elite_body, comm_rh_reichman'
    CUTSCENE_APPEARANCE = 'hassler'


class HasslerOrder(Actor):
    RU_NAME = 'Хасслер'
    TYPE = ACTOR_MALE
    NAME = 'hassler'
    COMM_APPEARANCE = 'rh_hassler_head, rh_male_elite_body, comm_rh_reichman'
    CUTSCENE_APPEARANCE = 'hassler_order'


class Alaric(Actor):
    RU_NAME = 'Аларик'
    NAME_ID = 94203
    TYPE = ACTOR_MALE
    NAME = 'alaric'
    COMM_APPEARANCE = 'rh_alaric_head_hat, pi_pirate6_body, comm_rh_alaric'
    CUTSCENE_APPEARANCE = 'alaric'
    SPACE_VOICE = 'pilot_f_mil_m01'


class Jacobo(Actor):
    RU_NAME = 'Джакобо'
    NAME_ID = 92211
    TYPE = ACTOR_MALE
    NAME = 'jacobo'
    COMM_APPEARANCE = 'pl_male1_head, pi_pirate2_body, comm_br_guard'
    CUTSCENE_APPEARANCE = 'jacobo'
    SPACE_VOICE = 'pilot_f_mil_m01'


class Dietrich(Actor):
    RU_NAME = 'Дитрих'
    NAME_ID = 93203
    TYPE = ACTOR_MALE
    NAME = 'deidrich'
    COMM_APPEARANCE = 'rh_deidrich_head, rh_deidrich_body, comm_rh_reichman'
    CUTSCENE_APPEARANCE = 'jacobo'
    SPACE_VOICE = 'pilot_f_mil_m01'


class Wilham(Actor):
    RU_NAME = 'Вильгельм'
    NAME_ID = 92210
    TYPE = ACTOR_MALE
    NAME = 'wilham'
    COMM_APPEARANCE = 'rh_wilham_head, rh_wilham_body, comm_rh_wilham'
    CUTSCENE_APPEARANCE = 'wilham'
    SPACE_VOICE = 'razor_1'


class Kim(Actor):
    RU_NAME = 'Ким'
    TYPE = ACTOR_FEMALE
    NAME = 'kim'
    # COMM_APPEARANCE = ''
    CUTSCENE_APPEARANCE = 'kim'


