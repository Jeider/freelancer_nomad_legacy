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

    @classmethod
    def get_steos_id(cls):
        return cls.STEOS_ID

    @classmethod
    def get_steos_pitch(cls):
        return cls.STEOS_PITCH

    @classmethod
    def get_steos_speed(cls):
        return cls.STEOS_SPEED

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
    STEOS_ID = 210
    STEOS_PITCH = -0.5
    STEOS_SPEED = 1.13


class EdisonTrent(Actor):
    RU_NAME = 'Эдисон Трент'
    TYPE = ACTOR_TRENT
    NAME = 'edison'
    COMM_APPEARANCE = 'pi_pirate5_head, pl_trent_body, comm_ge_generic1'
    STEOS_ID = 211
    STEOS_PITCH = -0.5
    STEOS_SPEED = 1.0


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
    SPACE_VOICE = 'pilot04'


class HatcherStation(Actor):
    RU_NAME = 'Хетчер'
    TYPE = ACTOR_FEMALE
    NAME = 'hatcher'
    COMM_APPEARANCE = 'li_hatcher_head, li_hatcher_body, new_fem_glasses'


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
    COMM_APPEARANCE = 'li_scrote_head, li_scrote_body'
    STEOS_ID = 211
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
    COMM_APPEARANCE = 'li_rockford_head, sh_male1_body, comm_ge_generic1'
    STEOS_ID = 13
    STEOS_PITCH = 0.2
    STEOS_SPEED = 1.05


class RockfordStation(Actor):
    RU_NAME = 'Рокфорд'
    TYPE = ACTOR_MALE
    NAME = 'rockford'
    COMM_APPEARANCE = 'li_rockford_head, sh_male1_body'
    STEOS_ID = 13
    STEOS_PITCH = 0.2
    STEOS_SPEED = 1.05


class Brighton(Actor):
    RU_NAME = 'Брайтон'
    TYPE = ACTOR_MALE
    NAME = 'brighton'
    COMM_APPEARANCE = 'br_brighton_head, br_brighton_body'


class DetroitDispatcher(Actor):
    RU_NAME = 'Детроит'
    TYPE = ACTOR_MALE
    NAME = 'dispatcher'
    COMM_APPEARANCE = 'br_kaitlyn_head, br_kaitlyn_body, prop_neuralnet_e'


class ClarkResearch(Actor):
    RU_NAME = 'Станция Кларк'
    TYPE = ACTOR_MALE
    NAME = 'clark'
    COMM_APPEARANCE = 'sh_male2_head, sh_male2_body, prop_hat_male_li_elite_visor'


class Sigma17Trader(Actor):
    RU_NAME = 'Торговец'
    TYPE = ACTOR_MALE
    NAME = 'trader'
    COMM_APPEARANCE = 'pl_female3_head, pl_female1_journeyman_body, prop_neuralnet_A'


class Sigma17Police(Actor):
    RU_NAME = 'Полициейский'
    TYPE = ACTOR_MALE
    NAME = 'police'
    COMM_APPEARANCE = 'li_captain_head, li_male_elite_body, comm_li_elite'


class Sigma17Assassin(Actor):
    RU_NAME = 'Киллер'
    TYPE = ACTOR_MALE
    NAME = 'assassin'
    COMM_APPEARANCE = 'rh_captain_head, rh_male_elite_body, comm_rh_elite'


class Kreitmaier(Actor):
    RU_NAME = 'Крейтмайер'
    TYPE = ACTOR_MALE
    NAME = 'officer'
    COMM_APPEARANCE = 'rh_captain_head, rh_male_elite_body, comm_rh_elite'


class Marauder(Actor):
    RU_NAME = 'Марадёр'
    TYPE = ACTOR_MALE
    NAME = 'marauder'
    COMM_APPEARANCE = 'li_captain_head, rh_male_guard_body, comm_rh_guard'


class Punisher(Actor):
    RU_NAME = 'Каратель'
    TYPE = ACTOR_MALE
    NAME = 'punisher'
    COMM_APPEARANCE = 'rh_sales_head, rh_male_elite_body, comm_rh_elite'


class PunisherCatcher(Actor):
    RU_NAME = 'Каратель'
    TYPE = ACTOR_MALE
    NAME = 'catcher'
    COMM_APPEARANCE = 'rh_sales_head, rh_male_elite_body, comm_rh_elite'


class Informer(Actor):
    RU_NAME = 'Информатор'
    TYPE = ACTOR_MALE
    NAME = 'informer'
    COMM_APPEARANCE = 'null, robot_body_E'


class Adelmar(Actor):
    RU_NAME = 'Аделмар'
    TYPE = ACTOR_MALE
    NAME = 'adelmar'
    COMM_APPEARANCE = 'pi_pirate3_head, rh_commtrader_body, prop_neuralnet_e_right'


class Luc(Actor):
    RU_NAME = 'Луц'
    TYPE = ACTOR_MALE
    NAME = 'luc'
    COMM_APPEARANCE = 'rh_sales_head, pl_male3_peasant_body, comm_ge_generic1'


class Sigma8Cruiser(Actor):
    RU_NAME = 'Крейсер'
    TYPE = ACTOR_MALE
    NAME = 'cruiser'
    COMM_APPEARANCE = 'rh_sales_head, rh_male_guard_body, prop_neuralnet_d'


class BrandenburgCruiser(Actor):
    RU_NAME = 'Крейсер'
    TYPE = ACTOR_MALE
    NAME = 'cruiser'
    COMM_APPEARANCE = 'rh_sales_head, rh_male_guard_body, prop_neuralnet_d'


class ForbesSmugglerOne(Actor):
    RU_NAME = 'Контрабандист'
    TYPE = ACTOR_MALE
    NAME = 'smuggler1'
    COMM_APPEARANCE = 'pl_male1_head, pi_pirate3_body, comm_pi_pirate'


class ForbesSmugglerTwo(Actor):
    RU_NAME = 'Контрабандист'
    TYPE = ACTOR_MALE
    NAME = 'smuggler2'
    COMM_APPEARANCE = 'pl_male1_head, pi_pirate3_body, comm_pi_pirate'


class OmegaJunkerOne(Actor):
    RU_NAME = 'Мусорщик'
    TYPE = ACTOR_MALE
    NAME = 'junker1'
    COMM_APPEARANCE = 'pl_male1_head, pi_pirate3_body, comm_pi_pirate'


class OmegaJunkerTwo(Actor):
    RU_NAME = 'Мусорщик'
    TYPE = ACTOR_MALE
    NAME = 'junker2'
    COMM_APPEARANCE = 'pl_male1_head, pi_pirate3_body, comm_pi_pirate'


class OmegaJunkerThree(Actor):
    RU_NAME = 'Мусорщик'
    TYPE = ACTOR_MALE
    NAME = 'junker3'
    COMM_APPEARANCE = 'pl_male1_head, pi_pirate3_body, comm_pi_pirate'


class ForbesSmugglerThree(Actor):
    RU_NAME = 'Контрабандист'
    TYPE = ACTOR_MALE
    NAME = 'smuggler3'
    COMM_APPEARANCE = 'pl_male1_head, pi_pirate3_body, comm_pi_pirate'


class MaleCaptain(Actor):
    RU_NAME = 'Капитан'
    TYPE = ACTOR_MALE
    NAME = 'captain'
    COMM_APPEARANCE = 'li_captain_head, li_male_elite_body'
    STEOS_ID = 10090


class KusariCaptain(Actor):
    RU_NAME = 'Капитан'
    TYPE = ACTOR_MALE
    NAME = 'captain'
    COMM_APPEARANCE = 'ku_bartender_head, ku_male_guard_body'
    STEOS_ID = 10090


class Missouri(Actor):
    RU_NAME = 'Капитан'
    TYPE = ACTOR_MALE
    NAME = 'missouri'
    COMM_APPEARANCE = 'br_captain_head, li_male_elite_body'
    STEOS_ID = 215
    STEOS_PITCH = -0.5
    STEOS_SPEED = 1.1


class SphereMissouri(Actor):
    RU_NAME = 'Капитан'
    TYPE = ACTOR_MALE
    NAME = 'captain'
    COMM_APPEARANCE = 'br_captain_head, li_male_elite_body'
    STEOS_ID = 215
    STEOS_PITCH = -0.5
    STEOS_SPEED = 1.1


class Sigma8Outpost(Actor):
    RU_NAME = 'Аванпост'
    TYPE = ACTOR_MALE
    NAME = 'outpost'
    COMM_APPEARANCE = 'rh_captain_head, rh_male_elite_body, prop_hat_male_rh_elite_visor'


class SphereOutpost(Actor):
    RU_NAME = 'Аванпост'
    TYPE = ACTOR_MALE
    NAME = 'outpost'
    COMM_APPEARANCE = 'rh_captain_head, rh_male_elite_body, prop_hat_male_rh_elite_visor'


class BrandenburgOutpost(Actor):
    RU_NAME = 'Бранденбург'
    TYPE = ACTOR_MALE
    NAME = 'outpost'
    COMM_APPEARANCE = 'rh_captain_head, rh_male_elite_body, prop_hat_male_rh_elite_visor'


class SphereAssistant(Actor):
    RU_NAME = 'Ассистент'
    TYPE = ACTOR_MALE
    NAME = 'scient'
    COMM_APPEARANCE = 'ge_male4_head, sc_scientist3_body, prop_neuralnet_E'


class DeltaOne(Actor):
    RU_NAME = 'Дельта-1'
    TYPE = ACTOR_MALE
    NAME = 'delta1'
    COMM_APPEARANCE = 'br_bartender_head, pi_pirate2_body'


class DeltaThree(Actor):
    RU_NAME = 'Дельта-3'
    TYPE = ACTOR_MALE
    NAME = 'delta3'
    COMM_APPEARANCE = 'br_quigly_head, pi_pirate3_body'


class Reitherman(Actor):
    RU_NAME = 'Рейтерман'
    TYPE = ACTOR_MALE
    NAME = 'professor'
    COMM_APPEARANCE = 'ge_male1_head, sc_scientist4_body, prop_neuralnet_D'


class FinnRunner(Actor):
    RU_NAME = 'Финн'
    TYPE = ACTOR_MALE
    NAME = 'runner'
    COMM_APPEARANCE = 'sh_male1_head, sc_scientist1_body, prop_hat_male_rh_grd_visor'


class Ceed(Actor):
    RU_NAME = 'Сид'
    TYPE = ACTOR_MALE
    NAME = 'syd'
    COMM_APPEARANCE = 'pl_male7_head, pi_orillion_body'


class OrderPilot(Actor):
    RU_NAME = 'Пилот Ордена'
    TYPE = ACTOR_MALE
    NAME = 'orderpilot'
    COMM_APPEARANCE = 'pi_pirate2_head, pi_orillion_body, comm_br_guard'


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
    STEOS_PITCH = 0.2
    STEOS_SPEED = 1.1


class PromDread1(Actor):
    RU_NAME = 'Цинцинатти'
    TYPE = ACTOR_MALE
    NAME = 'promdread1'
    COMM_APPEARANCE = 'li_captain_head, li_male_elite_body'
    STEOS_ID = 210
    STEOS_PITCH = 0.2
    STEOS_SPEED = 1.1


class PromDread2(Actor):
    RU_NAME = 'Рио-Гранде'
    TYPE = ACTOR_MALE
    NAME = 'promdread2'
    COMM_APPEARANCE = 'li_captain_head, li_male_elite_body'
    STEOS_ID = 220
    STEOS_PITCH = 0.2
    STEOS_SPEED = 1.1


class FortBush(Actor):
    RU_NAME = 'Форт Буш'
    TYPE = ACTOR_MALE
    NAME = 'bush'
    COMM_APPEARANCE = 'li_captain_head, li_male_elite_body'
    STEOS_ID = 220
    STEOS_PITCH = 0.2
    STEOS_SPEED = 1.1


class RedLeader(Actor):
    RU_NAME = 'Красный лидер'
    TYPE = ACTOR_MALE
    NAME = 'red'
    COMM_APPEARANCE = 'li_captain_head, li_male_elite_body, comm_li_elite'


class CruiserCaptain(Actor):
    RU_NAME = 'Уорфиш'
    TYPE = ACTOR_MALE
    NAME = 'captain'
    COMM_APPEARANCE = 'li_captain_head, li_male_elite_body, comm_li_elite'


class JabbaBandit(Actor):
    RU_NAME = 'Бандит'
    TYPE = ACTOR_MALE
    NAME = 'bandit'


class Tortuga(Actor):
    RU_NAME = 'Тортуга'
    TYPE = ACTOR_MALE
    NAME = 'tortuga'
    COMM_APPEARANCE = 'br_quigly_head, sh_male2_body, prop_hat_male_pirate_a, prop_neuralnet_d'
    STEOS_ID = 10029
    STEOS_PITCH = 0.25


class CorsairBarman(Actor):
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
    TYPE = ACTOR_MALE
    NAME = 'hassler'
    COMM_APPEARANCE = 'rh_hassler_head, rh_male_elite_body, comm_rh_reichman'
    CUTSCENE_APPEARANCE = 'hassler'
    STEOS_ID = 211


class HasslerOrder(Actor):
    RU_NAME = 'Хасслер'
    TYPE = ACTOR_MALE
    NAME = 'hassler'
    COMM_APPEARANCE = 'rh_hassler_head, pi_orillion_body'
    CUTSCENE_APPEARANCE = 'hassler'
    STEOS_ID = 10071


class Alaric(Actor):
    RU_NAME = 'Аларик'
    TYPE = ACTOR_MALE
    NAME = 'alaric'
    COMM_APPEARANCE = 'rh_alaric_head_hat, pi_pirate6_body, comm_rh_alaric'
    CUTSCENE_APPEARANCE = 'alaric'
    SPACE_VOICE = 'pilot_f_mil_m01'
    STEOS_ID = 204
    STEOS_PITCH = 0.1
    STEOS_SPEED = 1.1


class AlaricStation(Actor):
    RU_NAME = 'Аларик'
    TYPE = ACTOR_MALE
    NAME = 'alaric'
    COMM_APPEARANCE = 'rh_alaric_head, pi_pirate6_body'
    CUTSCENE_APPEARANCE = 'alaric'
    SPACE_VOICE = 'pilot_f_mil_m01'
    STEOS_ID = 204
    STEOS_PITCH = 0.1
    STEOS_SPEED = 1.1


class Jacobo(Actor):
    RU_NAME = 'Джакобо'
    TYPE = ACTOR_MALE
    NAME = 'jacobo'
    COMM_APPEARANCE = 'pl_male1_head, pi_pirate2_body, comm_br_guard'
    CUTSCENE_APPEARANCE = 'jacobo'
    SPACE_VOICE = 'pilot_f_mil_m01'


class JacoboTrader(Actor):
    RU_NAME = 'Джакобо'
    TYPE = ACTOR_MALE
    NAME = 'jacobo'
    COMM_APPEARANCE = 'pl_male1_head, pi_pirate2_body, prop_neuralnet_b'
    CUTSCENE_APPEARANCE = 'jacobo'
    SPACE_VOICE = 'pilot_f_mil_m01'


class Dietrich(Actor):
    RU_NAME = 'Дитрих'
    TYPE = ACTOR_MALE
    NAME = 'deidrich'
    COMM_APPEARANCE = 'rh_deidrich_head, rh_deidrich_body'


class Wilham(Actor):
    RU_NAME = 'Вильгельм'
    TYPE = ACTOR_MALE
    NAME = 'wilham'
    COMM_APPEARANCE = 'rh_wilham_head, rh_wilham_body, comm_rh_wilham'
    CUTSCENE_APPEARANCE = 'wilham'
    SPACE_VOICE = 'razor_1'


class WilhamStation(Actor):
    RU_NAME = 'Вильгельм'
    TYPE = ACTOR_MALE
    NAME = 'wilhelm'
    COMM_APPEARANCE = 'rh_wilham_head, rh_wilham_body'
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
    COMM_APPEARANCE = 'ku_captain_head, ku_male_elite_body, comm_ku_elite'
    CUTSCENE_APPEARANCE = 'kim'
    STEOS_ID = 287


class Matome(Actor):
    RU_NAME = 'Матомэ'
    TYPE = ACTOR_MALE
    NAME = 'matome'
    COMM_APPEARANCE = 'ge_male2_head, ku_male_guard_body, prop_neuralnet_e'
    STEOS_ID = 119  # 10090


class SakuraOne(Actor):
    RU_NAME = 'Сакура'
    TYPE = ACTOR_MALE
    NAME = 'sakura'
    COMM_APPEARANCE = 'ku_sales_head, ku_male_guard_body, comm_ku_guard'
    STEOS_ID = 10071  # 10090


class Chrysanthemum(Actor):
    RU_NAME = 'Хризантема'
    TYPE = ACTOR_FEMALE
    NAME = 'chrys'
    COMM_APPEARANCE = 'ku_kym_head, ku_kym_body, prop_neuralnet_d'
    STEOS_ID = 206


class ChrysanthemumTrain(Actor):
    RU_NAME = 'Хризантема'
    TYPE = ACTOR_MALE
    NAME = 'chrys'
    # COMM_APPEARANCE = ''
    STEOS_ID = 10071


class ChrysanthemumLifter(Actor):
    RU_NAME = 'Погрузчик Хризантемы'
    TYPE = ACTOR_MALE
    NAME = 'chrys'
    # COMM_APPEARANCE = ''
    STEOS_ID = 10071


class ChrysanthemumRepair(Actor):
    RU_NAME = 'Монтировщик Хризантемы'
    TYPE = ACTOR_MALE
    NAME = 'chrys'
    # COMM_APPEARANCE = ''
    STEOS_ID = 10071


class Tor(Actor):
    RU_NAME = 'Тор'
    TYPE = ACTOR_MALE
    NAME = 'tor'
    COMM_APPEARANCE = 'ku_bartender_head_hat, ku_male_guard_body, comm_ku_kym'
    STEOS_ID = 220


class Reichman(Actor):
    RU_NAME = 'Райхман'
    TYPE = ACTOR_MALE
    NAME = 'reichman'
    CUTSCENE_APPEARANCE = 'reichman'
    COMM_APPEARANCE = 'rh_reichman_head, rh_reichman_body, prop_neuralnet_A_right'
    SPACE_VOICE = 'pilot_f_mil_m01'
    STEOS_ID = 10080
    STEOS_PITCH = -0.5


class ActorManager:
    def __init__(self):
        self.actors_per_name = {actor.NAME: actor for actor in Actor.subclasses}

    def get_by_name(self, name):
        return self.actors_per_name[name]
