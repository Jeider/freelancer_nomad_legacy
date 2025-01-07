ACTOR_MALE = 'male'
ACTOR_TRENT = 'trent'
ACTOR_FEMALE = 'female'
ACTOR_JUNI = 'juni'


class SteosInterface:

    @classmethod
    def get_steos_id(cls):
        raise NotImplementedError

    @classmethod
    def get_steos_pitch(cls):
        raise NotImplementedError

    @classmethod
    def get_steos_speed(cls):
        raise NotImplementedError


class DynamicActor:
    def __init__(self, steos_id, steos_pitch, steos_speed):
        self.steos_id = steos_id
        self.steos_pitch = steos_pitch
        self.steos_speed = steos_speed

    def get_steos_id(self):
        return self.steos_id

    def get_steos_pitch(self):
        return self.steos_pitch

    def get_steos_speed(self):
        return self.steos_speed


class Actor(SteosInterface):
    TYPE = None
    NAME = None
    RU_NAME = None
    NAME_ID = None
    COMM_APPEARANCE = ''
    CUTSCENE_APPEARANCE = ''
    SPACE_VOICE = None
    STEOS_ID = None
    STEOS_PITCH = 0
    STEOS_SPEED = 1

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    def get_steos_id(self):
        return self.STEOS_ID

    def get_steos_pitch(self):
        return self.STEOS_PITCH

    def get_steos_speed(self):
        return self.STEOS_SPEED

    @classmethod
    def is_male(cls):
        return cls.TYPE == ACTOR_MALE

    @classmethod
    def is_female(cls):
        return cls.TYPE == ACTOR_FEMALE

    @classmethod
    def is_player(cls):
        return cls.TYPE == ACTOR_TRENT

    @classmethod
    def is_juni(cls):  # надеюсь не пригодится
        return cls.TYPE == ACTOR_JUNI

    @classmethod
    def get_comm_appearance(cls):
        return cls.COMM_APPEARANCE


class Trent(Actor):
    RU_NAME = 'Трент'
    TYPE = ACTOR_TRENT
    NAME = 'trent'
    COMM_APPEARANCE = 'pi_pirate5_head, player_body, player_commhelmet'
    STEOS_ID = 2
    STEOS_PITCH = -0.5
    STEOS_SPEED = 1.13


class EdisonTrent(Actor):
    RU_NAME = 'Эдисон Трент'
    TYPE = ACTOR_TRENT
    NAME = 'edison'
    COMM_APPEARANCE = 'pi_pirate5_head, player_body, player_commhelmet'
    STEOS_ID = 2
    STEOS_PITCH = 0.5
    STEOS_SPEED = 1.05


class Juni(Actor):
    RU_NAME = 'Джуни'
    TYPE = ACTOR_JUNI  # Анимация имеет ту же природу, что и у Трента. Надеюсь не пригодится
    NAME = 'juni'


class Hatcher(Actor):
    RU_NAME = 'Хетчер'
    TYPE = ACTOR_FEMALE
    NAME = 'hatcher'
    COMM_APPEARANCE = 'pl_female2_head, li_hatcher_body, comm_li_hatcher_female'
    STEOS_ID = 217
    STEOS_PITCH = -1
    STEOS_SPEED = 1.2


class Darcy(Actor):
    RU_NAME = 'Дерси'
    TYPE = ACTOR_FEMALE
    NAME = 'darcy'
    COMM_APPEARANCE = 'ge_female1_head, br_darcy_body, comm_br_darcy_female'
    STEOS_ID = 219
    STEOS_PITCH = 0
    STEOS_SPEED = 1.2


class Kaitlyn(Actor):
    RU_NAME = 'Кейтлин'
    TYPE = ACTOR_FEMALE
    NAME = 'kaytlin'
    COMM_APPEARANCE = 'br_kaytlin_head, br_kaytlin_body'
    STEOS_ID = 219
    STEOS_PITCH = 0
    STEOS_SPEED = 1.2




class King(Actor):
    RU_NAME = 'Кинг'
    TYPE = ACTOR_MALE
    NAME = 'king'
    STEOS_ID = 215
    STEOS_PITCH = 0
    STEOS_SPEED = 1.1


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
    STEOS_ID = 13
    STEOS_PITCH = 0
    STEOS_SPEED = 1.2


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
    STEOS_ID = 10090


class Missouri(Actor):
    RU_NAME = 'Капитан'
    TYPE = ACTOR_MALE
    NAME = 'missouri'
    COMM_APPEARANCE = 'li_captain_head, li_male_elite_body'
    STEOS_ID = 215
    STEOS_PITCH = -0.5
    STEOS_SPEED = 1.1


class Kruger(Actor):
    RU_NAME = 'Крюгер'
    TYPE = ACTOR_MALE
    NAME = 'kruger'
    COMM_APPEARANCE = 'li_captain_head, li_male_elite_body'
    STEOS_ID = 10090


class Omaha(Actor):
    RU_NAME = 'Омаха'
    TYPE = ACTOR_MALE
    NAME = 'omaha'
    COMM_APPEARANCE = 'li_captain_head, li_male_elite_body'
    STEOS_ID = 10090


class FortBush(Actor):
    RU_NAME = 'Форт Буш'
    TYPE = ACTOR_MALE
    NAME = 'bush'
    COMM_APPEARANCE = 'li_captain_head, li_male_elite_body'
    STEOS_ID = 10029


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
    STEOS_ID = 10029


class Hassler(Actor):
    RU_NAME = 'Хасслер'
    NAME_ID = 93202
    TYPE = ACTOR_MALE
    NAME = 'hassler'
    COMM_APPEARANCE = 'rh_hassler_head, rh_male_elite_body, comm_rh_reichman'
    CUTSCENE_APPEARANCE = 'hassler'
    STEOS_ID = 10029


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
    STEOS_ID = 204
    STEOS_PITCH = -0.5
    STEOS_SPEED = 0.7


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


class Mandrake(Actor):
    RU_NAME = 'Мандрейк'
    TYPE = ACTOR_MALE
    NAME = 'mandrake'
    COMM_APPEARANCE = 'ge_male7_head, sc_scientist1_body'
    CUTSCENE_APPEARANCE = 'mandrake'
    STEOS_ID = 214
    STEOS_PITCH = -0.5
    STEOS_SPEED = 1.1


class Kim(Actor):
    RU_NAME = 'Ким'
    TYPE = ACTOR_MALE
    NAME = 'kim'
    # COMM_APPEARANCE = ''
    CUTSCENE_APPEARANCE = 'kim'
    STEOS_ID = 287


class SakuraOne(Actor):
    RU_NAME = 'Сакура 1'
    TYPE = ACTOR_MALE
    NAME = 'kim'
    # COMM_APPEARANCE = '
    STEOS_ID = 119


class SakuraTwo(Actor):
    RU_NAME = 'Сакура 2'
    TYPE = ACTOR_MALE
    NAME = 'sakura2'
    # COMM_APPEARANCE = ''
    STEOS_ID = 10090


class SakuraThree(Actor):
    RU_NAME = 'Сакура 3'
    TYPE = ACTOR_MALE
    NAME = 'sakura3'
    # COMM_APPEARANCE = ''
    STEOS_ID = 10080


class Chrysanthemum(Actor):
    RU_NAME = 'Хризантема'
    TYPE = ACTOR_MALE
    NAME = 'chrys'
    # COMM_APPEARANCE = ''
    STEOS_ID = 10071


class Tor(Actor):
    RU_NAME = 'Тор'
    TYPE = ACTOR_FEMALE
    NAME = 'tor'
    # COMM_APPEARANCE = ''
    STEOS_ID = 10071


class Reichman(Actor):
    RU_NAME = 'Райхман'
    TYPE = ACTOR_MALE
    NAME = 'reichman'
    CUTSCENE_APPEARANCE = 'reichman'
    SPACE_VOICE = 'pilot_f_mil_m01'
    STEOS_ID = 10029


