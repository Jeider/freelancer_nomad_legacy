from text.strings import MultiString as MS

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
    ATTENUATION = None
    GAME_ACTOR = None

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

    @classmethod
    def get_attenuation(cls):
        return cls.ATTENUATION

    @classmethod
    def get_game_actor(cls):
        return cls.GAME_ACTOR if cls.GAME_ACTOR else cls.NAME


class Trent(Actor):
    RU_NAME = MS('Трент', 'Trent')
    TYPE = ACTOR_TRENT
    NAME = 'trent'
    GAME_ACTOR = 'Player'
    COMM_APPEARANCE = 'pi_pirate5_head, player_body, player_commhelmet'
    CUTSCENE_APPEARANCE = 'trent'
    STEOS_ID = 210
    STEOS_PITCH = -0.5
    # STEOS_SPEED = 1.13
    STEOS_SPEED = 1  # For ENG


class EdisonTrent(Actor):
    RU_NAME = MS('Эдисон Трент', 'Edison Trent')
    TYPE = ACTOR_TRENT
    NAME = 'edison'
    COMM_APPEARANCE = 'pi_pirate5_head, pl_trent_body, comm_ge_generic1'
    CUTSCENE_APPEARANCE = 'edison_trent'
    # gameplay test
    # STEOS_ID = 208
    # STEOS_PITCH = -1
    # STEOS_SPEED = 1.45
    STEOS_ID = 210
    STEOS_PITCH = 0
    STEOS_SPEED = 1.13


class Juni(Actor):
    RU_NAME = MS('Джуни', 'Juni')
    TYPE = ACTOR_JUNI  # Анимация имеет ту же природу, что и у Трента. Надеюсь не пригодится
    CUTSCENE_APPEARANCE = 'junko_zane'
    NAME = 'juni'
    # STEOS_ID = 178
    # STEOS_PITCH = 0.1
    # STEOS_SPEED = 1.3
    STEOS_ID = 219
    STEOS_PITCH = -0.2
    STEOS_SPEED = 1.3


class Hatcher(Actor):
    RU_NAME = MS('Хетчер', 'Hatcher')
    TYPE = ACTOR_FEMALE
    NAME = 'hatcher'
    COMM_APPEARANCE = 'pl_female2_head, li_hatcher_body, comm_li_hatcher_female'
    CUTSCENE_APPEARANCE = 'hatcher'
    STEOS_ID = 217
    STEOS_PITCH = -1
    # STEOS_SPEED = 1.1
    STEOS_SPEED = 1  # eng
    SPACE_VOICE = 'pilot04'


class HatcherStation(Hatcher):
    RU_NAME = MS('Хетчер', 'Hatcher')
    TYPE = ACTOR_FEMALE
    NAME = 'hatcher'
    COMM_APPEARANCE = 'li_hatcher_head, li_hatcher_body, new_fem_glasses'


class Darcy(Actor):
    RU_NAME = MS('Дерси', 'Darcy')
    TYPE = ACTOR_FEMALE
    NAME = 'darcy'
    COMM_APPEARANCE = 'ge_female1_head, br_darcy_body, comm_br_darcy_female'
    CUTSCENE_APPEARANCE = 'darcy'
    STEOS_ID = 219
    STEOS_PITCH = 0
    # STEOS_SPEED = 1.2
    STEOS_SPEED = 1


class Kaitlyn(Actor):
    RU_NAME = MS('Кейтлин', 'Caitlyn')
    TYPE = ACTOR_FEMALE
    NAME = 'kaytlin'
    COMM_APPEARANCE = 'br_kaytlin_head, br_kaytlin_body'
    STEOS_ID = 203
    STEOS_PITCH = -0.5
    STEOS_SPEED = 1


class King(Actor):
    RU_NAME = MS('Кинг', 'King')
    TYPE = ACTOR_MALE
    NAME = 'king'
    COMM_APPEARANCE = 'li_scrote_head, li_scrote_body'
    # CUTSCENE_APPEARANCE = 'king'
    # STEOS_ID = 218
    # STEOS_PITCH = 1
    # STEOS_SPEED = 1.1
    STEOS_ID = 218
    STEOS_PITCH = 0.2
    STEOS_SPEED = 1


class Tilton(Actor):
    RU_NAME = MS('Тилтон', 'Tilton')
    TYPE = ACTOR_MALE
    NAME = 'tilton'
    COMM_APPEARANCE = 'pl_male4_head, li_tilton_body'
    STEOS_ID = 266
    STEOS_PITCH = -0.5
    STEOS_SPEED = 0.9


class Rockford(Actor):
    RU_NAME = MS('Рокфорд', 'Rockford')
    TYPE = ACTOR_MALE
    NAME = 'rockford'
    COMM_APPEARANCE = 'li_rockford_head, sh_male1_body, comm_ge_generic1'
    CUTSCENE_APPEARANCE = 'rockford'
    STEOS_ID = 13
    STEOS_PITCH = 0.2
    STEOS_SPEED = 1.05


class RockfordStation(Actor):
    RU_NAME = MS('Рокфорд', 'Rockford')
    TYPE = ACTOR_MALE
    NAME = 'rockford'
    COMM_APPEARANCE = 'li_rockford_head, sh_male1_body'
    STEOS_ID = 13
    STEOS_PITCH = 0.2
    STEOS_SPEED = 1.05


class Brighton(Actor):
    RU_NAME = MS('Брайтон', 'Brighton')
    TYPE = ACTOR_MALE
    NAME = 'brighton'
    COMM_APPEARANCE = 'br_brighton_head, br_brighton_body'
    STEOS_ID = 208
    STEOS_PITCH = -0.5
    STEOS_SPEED = 1.02


class DetroitDispatcher(Actor):
    RU_NAME = MS('Детроит', 'Detroit')
    TYPE = ACTOR_FEMALE
    NAME = 'dispatcher'
    COMM_APPEARANCE = 'br_kaitlyn_head, br_kaitlyn_body, prop_neuralnet_e'


class ClarkResearch(Actor):
    RU_NAME = MS('Станция Кларк', 'Clark Station')
    TYPE = ACTOR_MALE
    NAME = 'clark'
    COMM_APPEARANCE = 'sh_male2_head, sh_male2_body, prop_hat_male_li_elite_visor'
    STEOS_ID = 287
    STEOS_SPEED = 1
    STEOS_PITCH = 0.15


class Sigma17Trader(Actor):
    RU_NAME = MS('Торговец', 'Trader')
    TYPE = ACTOR_FEMALE
    NAME = 'trader'
    COMM_APPEARANCE = 'pl_female3_head, pl_female1_journeyman_body, prop_neuralnet_A'


class Sigma17Police(Actor):
    RU_NAME = MS('Полицейский', 'Officer')
    TYPE = ACTOR_MALE
    NAME = 'police'
    COMM_APPEARANCE = 'li_captain_head, li_male_elite_body, comm_li_elite'


class Sigma17Assassin(Actor):
    RU_NAME = MS('Киллер', 'Killer')
    TYPE = ACTOR_MALE
    NAME = 'assassin'
    COMM_APPEARANCE = 'rh_captain_head, rh_male_elite_body, comm_rh_elite'


class Kreitmaier(Actor):
    RU_NAME = MS('Крейтмайер', 'Kreitmaier')
    TYPE = ACTOR_MALE
    NAME = 'officer'
    COMM_APPEARANCE = 'rh_captain_head, rh_male_elite_body, comm_rh_elite'


class Marauder(Actor):
    RU_NAME = MS('Марадёр', 'Marauder')
    TYPE = ACTOR_MALE
    NAME = 'marauder'
    COMM_APPEARANCE = 'li_captain_head, rh_male_guard_body, comm_rh_guard'


class Punisher(Actor):
    RU_NAME = MS('Каратель', 'Punisher')
    TYPE = ACTOR_MALE
    NAME = 'punisher'
    COMM_APPEARANCE = 'rh_sales_head, rh_male_elite_body, comm_rh_elite'


class PunisherCatcher(Actor):
    RU_NAME = MS('Каратель', 'Punisher')
    TYPE = ACTOR_MALE
    NAME = 'catcher'
    COMM_APPEARANCE = 'rh_sales_head, rh_male_elite_body, comm_rh_elite'


class Informer(King):
    RU_NAME = MS('Информатор', 'Informer')
    TYPE = ACTOR_MALE
    NAME = 'informer'
    COMM_APPEARANCE = 'null, robot_body_E'


class Neuralnet(Actor):
    RU_NAME = MS('Нейросеть', 'NeuralNet')
    TYPE = ACTOR_FEMALE
    NAME = 'nn'
    COMM_APPEARANCE = 'null, robot_body_E'
    STEOS_ID = 219
    ATTENUATION = 0


class Adelmar(Actor):
    RU_NAME = MS('Аделмар', 'Adelmar')
    TYPE = ACTOR_MALE
    NAME = 'adelmar'
    COMM_APPEARANCE = 'pi_pirate3_head, rh_commtrader_body, prop_neuralnet_e_right'
    STEOS_ID = 287
    STEOS_SPEED = 0.9
    STEOS_PITCH = 0.15


class Luc(Actor):
    RU_NAME = MS('Луц', 'Lutz')
    TYPE = ACTOR_MALE
    NAME = 'luc'
    COMM_APPEARANCE = 'rh_sales_head, pl_male3_peasant_body, comm_ge_generic1'
    STEOS_ID = 211
    STEOS_SPEED = 0.9
    STEOS_PITCH = 0.25


class Sigma8Cruiser(Actor):
    RU_NAME = MS('Крейсер', 'Cruiser')
    TYPE = ACTOR_MALE
    NAME = 'cruiser'
    COMM_APPEARANCE = 'rh_sales_head, rh_male_guard_body, prop_neuralnet_d'


class BrandenburgCruiser(Actor):
    RU_NAME = MS('Крейсер', 'Cruiser')
    TYPE = ACTOR_MALE
    NAME = 'cruiser'
    COMM_APPEARANCE = 'rh_sales_head, rh_male_guard_body, prop_neuralnet_d'
    STEOS_ID = 10029


class CadizEnemyOne(Actor):
    RU_NAME = MS('Киллер', 'Killer')
    TYPE = ACTOR_MALE
    NAME = 'enemy1'
    COMM_APPEARANCE = 'pl_male1_head, pi_pirate3_body, comm_pi_pirate'
    STEOS_ID = 211
    STEOS_PITCH = -1
    STEOS_SPEED = 1


class CadizEnemyTwo(Actor):
    RU_NAME = MS('Киллер', 'Killer')
    TYPE = ACTOR_MALE
    NAME = 'enemy2'
    COMM_APPEARANCE = 'pl_male1_head, pi_pirate3_body, comm_pi_pirate'
    STEOS_ID = 287
    STEOS_PITCH = -1


class CadizEnemyThree(CadizEnemyOne):
    NAME = 'enemy3'


class CadizEnemyFour(CadizEnemyOne):
    NAME = 'enemy4'


class ForbesSmugglerOne(Actor):
    RU_NAME = MS('Контрабандист', 'Smuggler')
    TYPE = ACTOR_MALE
    NAME = 'smuggler1'
    COMM_APPEARANCE = 'pl_male1_head, pi_pirate3_body, comm_pi_pirate'


class ForbesSmugglerTwo(Actor):
    RU_NAME = MS('Контрабандист', 'Smuggler')
    TYPE = ACTOR_MALE
    NAME = 'smuggler2'
    COMM_APPEARANCE = 'pl_male1_head, pi_pirate3_body, comm_pi_pirate'


class ForbesSmugglerThree(Actor):
    RU_NAME = MS('Контрабандист', 'Smuggler')
    TYPE = ACTOR_MALE
    NAME = 'smuggler3'
    COMM_APPEARANCE = 'pl_male1_head, pi_pirate3_body, comm_pi_pirate'


class OmegaJunkerOne(Actor):
    RU_NAME = MS('Мусорщик', 'Junker')
    TYPE = ACTOR_MALE
    NAME = 'junker1'
    COMM_APPEARANCE = 'pl_male1_head, pi_pirate3_body, comm_pi_pirate'


class OmegaJunkerTwo(Actor):
    RU_NAME = MS('Мусорщик', 'Junker')
    TYPE = ACTOR_MALE
    NAME = 'junker2'
    COMM_APPEARANCE = 'pl_male1_head, pi_pirate3_body, comm_pi_pirate'


class OmegaJunkerThree(Actor):
    RU_NAME = MS('Мусорщик', 'Junker')
    TYPE = ACTOR_MALE
    NAME = 'junker3'
    COMM_APPEARANCE = 'pl_male1_head, pi_pirate3_body, comm_pi_pirate'


class MaleCaptain(Actor):
    RU_NAME = MS('Капитан', 'Captain')
    TYPE = ACTOR_MALE
    NAME = 'captain'
    COMM_APPEARANCE = 'li_captain_head, li_male_elite_body'
    STEOS_ID = 10090


class KusariCaptain(Actor):
    RU_NAME = MS('Капитан', 'Captain')
    TYPE = ACTOR_MALE
    NAME = 'captain'
    COMM_APPEARANCE = 'ku_bartender_head, ku_male_guard_body'
    STEOS_ID = 10090


class Missouri(Actor):
    RU_NAME = MS('Капитан', 'Captain')
    TYPE = ACTOR_MALE
    NAME = 'missouri'
    COMM_APPEARANCE = 'br_captain_head, li_male_elite_body'
    STEOS_ID = 215
    STEOS_PITCH = -0.5
    STEOS_SPEED = 1.1


class SphereMissouri(Actor):
    RU_NAME = MS('Капитан', 'Captain')
    TYPE = ACTOR_MALE
    NAME = 'captain'
    COMM_APPEARANCE = 'br_captain_head, li_male_elite_body'
    STEOS_ID = 218
    STEOS_PITCH = 1
    STEOS_SPEED = 1.2


class Sigma8Outpost(Actor):
    RU_NAME = MS('Аванпост', 'Outpost')
    TYPE = ACTOR_FEMALE
    NAME = 'outpost'
    COMM_APPEARANCE = 'rh_newscaster_head_gen_hat, rh_female_elite_body, prop_hat_female_rh_elite'


class SphereOutpost(Actor):
    RU_NAME = MS('Аванпост', 'Outpost')
    TYPE = ACTOR_MALE
    NAME = 'outpost'
    COMM_APPEARANCE = 'rh_captain_head, rh_male_elite_body, prop_hat_male_rh_elite_visor'
    STEOS_ID = 287


class BrandenburgOutpost(Actor):
    RU_NAME = MS('Бранденбург', 'Brandenburg')
    TYPE = ACTOR_MALE
    NAME = 'outpost'
    COMM_APPEARANCE = 'rh_captain_head, rh_male_elite_body, prop_hat_male_rh_elite_visor'
    STEOS_ID = 10090


class SphereAssistant(Actor):
    RU_NAME = MS('Ассистент', 'Assistant')
    TYPE = ACTOR_MALE
    NAME = 'scient'
    COMM_APPEARANCE = 'ge_male4_head, sc_scientist3_body, prop_neuralnet_E'


class DeltaOne(Actor):
    RU_NAME = MS('Дельта-1', 'Delta-1')
    TYPE = ACTOR_MALE
    NAME = 'delta1'
    COMM_APPEARANCE = 'br_bartender_head, pi_pirate2_body'
    STEOS_ID = 208
    STEOS_PITCH = -1
    # STEOS_SPEED = 1.45
    STEOS_SPEED = 1   # en


class DeltaThree(Actor):
    RU_NAME = MS('Дельта-3', 'Delta-3')
    TYPE = ACTOR_MALE
    NAME = 'delta3'
    COMM_APPEARANCE = 'br_quigly_head, pi_pirate3_body'
    STEOS_ID = 10090
    STEOS_PITCH = -0.3
    # STEOS_SPEED = 1.1
    STEOS_SPEED = 0.9  # en


class Reitherman(Actor):
    RU_NAME = MS('Роттерман', 'Reitherman')
    TYPE = ACTOR_MALE
    NAME = 'professor'
    COMM_APPEARANCE = 'ge_male1_head, sc_scientist4_body, prop_neuralnet_D'
    STEOS_ID = 214
    STEOS_PITCH = -0.5
    # STEOS_SPEED = 1.1
    STEOS_SPEED = 1


class FinnRunner(Actor):
    RU_NAME = MS('Финн', 'Finn')
    TYPE = ACTOR_MALE
    NAME = 'runner'
    COMM_APPEARANCE = 'sh_male1_head, sc_scientist1_body, prop_hat_male_rh_grd_visor'
    STEOS_ID = 218
    STEOS_PITCH = 1
    # STEOS_SPEED = 1.2
    STEOS_SPEED = 1  # en


class Ceed(Actor):
    RU_NAME = MS('Сид', 'Ceed')
    TYPE = ACTOR_MALE
    NAME = 'syd'
    COMM_APPEARANCE = 'pl_male7_head, pi_orillion_body'
    STEOS_ID = 211
    STEOS_PITCH = -0.6
    STEOS_SPEED = 1


class OrderPilot(Actor):
    RU_NAME = MS('Пилот Ордена', 'Order Pilot')
    TYPE = ACTOR_MALE
    NAME = 'orderpilot'
    COMM_APPEARANCE = 'pi_pirate2_head, pi_orillion_body, comm_br_guard'
    STEOS_ID = 13
    STEOS_PITCH = 0.7
    STEOS_SPEED = 1


class OrderGuard(Actor):
    RU_NAME = MS('Пилот Ордена', 'Order Pilot')
    TYPE = ACTOR_MALE
    NAME = 'guard'
    COMM_APPEARANCE = 'pi_pirate2_head, pi_orillion_body, comm_br_guard'
    STEOS_ID = 13
    STEOS_PITCH = 0.7
    STEOS_SPEED = 1


class Kruger(Actor):
    RU_NAME = MS('Крюгер', 'Kruger')
    TYPE = ACTOR_MALE
    NAME = 'kruger'
    COMM_APPEARANCE = 'li_captain_head, li_male_elite_body'
    STEOS_ID = 10090


class Omaha(Actor):
    RU_NAME = MS('Омаха', 'Omaha')
    TYPE = ACTOR_MALE
    NAME = 'omaha'
    COMM_APPEARANCE = 'li_captain_head, li_male_elite_body'
    STEOS_ID = 10090
    STEOS_PITCH = 0.2
    # STEOS_SPEED = 1.1
    STEOS_SPEED = 1



class PromDread1(Actor):
    RU_NAME = MS('Цинцинатти', 'Cincinnati')
    TYPE = ACTOR_MALE
    NAME = 'promdread1'
    COMM_APPEARANCE = 'li_captain_head, li_male_elite_body'
    STEOS_ID = 210
    STEOS_PITCH = 0.2
    STEOS_SPEED = 1.1


class PromDread2(Actor):
    RU_NAME = MS('Рио-Гранде', 'Rio-Grande')
    TYPE = ACTOR_MALE
    NAME = 'promdread2'
    COMM_APPEARANCE = 'li_captain_head, li_male_elite_body'
    STEOS_ID = 220
    STEOS_PITCH = 0.2
    STEOS_SPEED = 1.1


class FortBush(Actor):
    RU_NAME = MS('Форт Буш', 'Fort Bush')
    TYPE = ACTOR_MALE
    NAME = 'bush'
    COMM_APPEARANCE = 'li_captain_head, li_male_elite_body'
    STEOS_ID = 220
    STEOS_PITCH = 0.2
    STEOS_SPEED = 1.1


class RedLeader(Actor):
    RU_NAME = MS('Красный лидер', 'Red Leader')
    TYPE = ACTOR_MALE
    NAME = 'red'
    COMM_APPEARANCE = 'li_captain_head, li_male_elite_body, comm_li_elite'


class CruiserCaptain(Actor):
    RU_NAME = MS('Уорфиш', 'Warfish')
    TYPE = ACTOR_MALE
    NAME = 'captain'
    COMM_APPEARANCE = 'li_captain_head, li_male_elite_body, comm_li_elite'


class JabbaBandit(Actor):
    RU_NAME = MS('Бандит', 'Bandit')
    TYPE = ACTOR_MALE
    NAME = 'bandit'


class Tortuga(Actor):
    RU_NAME = MS('Тортуга', 'Tortuga')
    TYPE = ACTOR_MALE
    NAME = 'tortuga'
    COMM_APPEARANCE = 'br_quigly_head, sh_male2_body, prop_hat_male_pirate_a, prop_neuralnet_d'
    STEOS_ID = 10029
    STEOS_PITCH = 0.25


class Smith(Actor):
    RU_NAME = MS('Смит', 'Smith')
    TYPE = ACTOR_MALE
    NAME = 'smith'
    STEOS_ID = 205
    STEOS_PITCH = 1


class DetroitBarman(Actor):
    RU_NAME = MS('Бармен', 'Bartender')
    TYPE = ACTOR_MALE
    NAME = 'barman'
    STEOS_ID = 13
    STEOS_PITCH = 1
    STEOS_SPEED = 1


class WalesBarman(Actor):
    RU_NAME = MS('Бармен', 'Bartender')
    TYPE = ACTOR_MALE
    NAME = 'barman'
    STEOS_ID = 218
    STEOS_PITCH = 0.3
    STEOS_SPEED = 1.1


class IntroBarman(Actor):
    RU_NAME = MS('Бармен', 'Bartender')
    TYPE = ACTOR_MALE
    NAME = 'barman'
    STEOS_ID = 287
    STEOS_SPEED = 1
    STEOS_PITCH = 0.09


class Jabba(Actor):
    RU_NAME = MS('Джабба', 'Jabba')
    TYPE = ACTOR_MALE
    NAME = 'jabba'
    STEOS_ID = 214
    STEOS_PITCH = 0.5
    STEOS_SPEED = 1  # ENG



class Stewardess(Hatcher):
    RU_NAME = MS('Стюардесса', 'Stewardess')
    TYPE = ACTOR_FEMALE
    NAME = 'stuard'


class CorsairBarman(Actor):
    RU_NAME = MS('Бармен', 'Bartender')
    TYPE = ACTOR_MALE
    NAME = 'barman'
    COMM_APPEARANCE = 'sh_male1_head, sh_male2_body'
    STEOS_ID = 287
    STEOS_SPEED = 0.9
    STEOS_PITCH = 0.25


class Yamamoto(Actor):
    RU_NAME = MS('Ямамото', 'Yamamoto')
    TYPE = ACTOR_MALE
    NAME = 'yamamoto'
    COMM_APPEARANCE = 'ku_tenji_head, pi_pirate4_body'
    CUTSCENE_APPEARANCE = 'tenji'
    STEOS_ID = 10029


class Hassler(Actor):
    RU_NAME = MS('Хасслер', 'Hassler')
    TYPE = ACTOR_MALE
    NAME = 'hassler'
    COMM_APPEARANCE = 'rh_hassler_head, rh_male_elite_body, comm_rh_reichman'
    CUTSCENE_APPEARANCE = 'hassler'
    STEOS_ID = 10071


class HasslerOrder(Actor):
    RU_NAME = MS('Хасслер', 'Hassler')
    TYPE = ACTOR_MALE
    NAME = 'hassler'
    COMM_APPEARANCE = 'rh_hassler_head, pi_orillion_body'
    CUTSCENE_APPEARANCE = 'hassler_order'
    STEOS_ID = 10071


class Alaric(Actor):
    RU_NAME = MS('Аларик', 'Alaric')
    TYPE = ACTOR_MALE
    NAME = 'alaric'
    COMM_APPEARANCE = 'rh_alaric_head_hat, pi_pirate6_body, comm_rh_alaric'
    CUTSCENE_APPEARANCE = 'alaric'
    SPACE_VOICE = 'pilot_f_mil_m01'
    STEOS_ID = 204
    STEOS_PITCH = -1
    # STEOS_SPEED = 1.1
    STEOS_SPEED = 1  # For ENG


class AlaricStation(Actor):
    RU_NAME = MS('Аларик', 'Alaric')
    TYPE = ACTOR_MALE
    NAME = 'alaric'
    COMM_APPEARANCE = 'rh_alaric_head, pi_pirate6_body'
    CUTSCENE_APPEARANCE = 'alaric'
    SPACE_VOICE = 'pilot_f_mil_m01'
    STEOS_ID = 204
    STEOS_PITCH = 0.1
    STEOS_SPEED = 1.1


class Jacobo(Actor):
    RU_NAME = MS('Джакобо', 'Jacobo')
    TYPE = ACTOR_MALE
    NAME = 'jacobo'
    COMM_APPEARANCE = 'pl_male1_head, pi_pirate2_body, comm_br_guard'
    CUTSCENE_APPEARANCE = 'jacobo'
    SPACE_VOICE = 'pilot_f_mil_m01'
    STEOS_ID = 205
    STEOS_PITCH = 0.5


class JacoboTrader(Actor):
    RU_NAME = MS('Джакобо', 'Jacobo')
    TYPE = ACTOR_MALE
    NAME = 'jacobo'
    COMM_APPEARANCE = 'pl_male1_head, pi_pirate2_body, prop_neuralnet_b'
    CUTSCENE_APPEARANCE = 'jacobo'
    SPACE_VOICE = 'pilot_f_mil_m01'


class Dietrich(Actor):
    RU_NAME = MS('Дитрих', 'Dietrich')
    TYPE = ACTOR_MALE
    NAME = 'deidrich'
    COMM_APPEARANCE = 'rh_deidrich_head, rh_deidrich_body'
    STEOS_ID = 214


class Wilham(Actor):
    RU_NAME = MS('Вильгельм', 'Wilhelm')
    TYPE = ACTOR_MALE
    NAME = 'wilham'
    COMM_APPEARANCE = 'rh_wilham_head, rh_wilham_body, comm_rh_wilham'
    CUTSCENE_APPEARANCE = 'wilham'
    SPACE_VOICE = 'razor_1'
    # STEOS_ID = 211
    # STEOS_SPEED = 0.95
    # STEOS_PITCH = -0.75
    STEOS_ID = 218
    STEOS_PITCH = 1
    STEOS_SPEED = 1


class WilhamStation(Actor):
    RU_NAME = MS('Вильгельм', 'Wilhelm')
    TYPE = ACTOR_MALE
    NAME = 'wilhelm'
    COMM_APPEARANCE = 'rh_wilham_head, rh_wilham_body'
    CUTSCENE_APPEARANCE = 'wilham'
    SPACE_VOICE = 'razor_1'


class Mandrake(Actor):
    RU_NAME = MS('Мандрейк', 'Mandrake')
    TYPE = ACTOR_MALE
    NAME = 'mandrake'
    COMM_APPEARANCE = 'ge_male7_head, sc_scientist1_body'
    CUTSCENE_APPEARANCE = 'mandrake'
    STEOS_ID = 214
    STEOS_PITCH = -0.5
    # STEOS_SPEED = 1.1
    STEOS_SPEED = 1 # ENG


class Kim(Actor):
    RU_NAME = MS('Ким', 'Kym')
    TYPE = ACTOR_MALE
    NAME = 'kim'
    COMM_APPEARANCE = 'ku_captain_head, ku_male_elite_body, comm_ku_elite'
    CUTSCENE_APPEARANCE = 'kim'
    STEOS_ID = 287


class Matome(Actor):
    RU_NAME = MS('Матомэ', 'Matome')
    TYPE = ACTOR_MALE
    NAME = 'matome'
    COMM_APPEARANCE = 'ge_male2_head, ku_male_guard_body, prop_neuralnet_e'
    STEOS_ID = 119  # 10090


class SakuraOne(Actor):
    RU_NAME = MS('Сакура', 'Sakura')
    TYPE = ACTOR_MALE
    NAME = 'sakura'
    COMM_APPEARANCE = 'ku_sales_head, ku_male_guard_body, comm_ku_guard'
    STEOS_ID = 10071  # 10090


class Chrysanthemum(Actor):
    RU_NAME = MS('Хризантема', 'Chrysanthemum')
    TYPE = ACTOR_FEMALE
    NAME = 'chrys'
    COMM_APPEARANCE = 'ku_kym_head, ku_kym_body, prop_neuralnet_d'
    STEOS_ID = 206


class ChrysanthemumTrain(Actor):
    RU_NAME = MS('Хризантема', 'Chrysanthemum')
    TYPE = ACTOR_MALE
    NAME = 'chrys'
    # COMM_APPEARANCE = ''
    STEOS_ID = 10071


class ChrysanthemumLifter(Actor):
    RU_NAME = MS('Погрузчик Хризантемы', 'Chrysanthemum\'s Lifter')
    TYPE = ACTOR_MALE
    NAME = 'chrys'
    # COMM_APPEARANCE = ''
    STEOS_ID = 10071


class ChrysanthemumRepair(Actor):
    RU_NAME = MS('Монтировщик Хризантемы', 'Chrysanthemum\'s Repair Ship')
    TYPE = ACTOR_MALE
    NAME = 'chrys'
    # COMM_APPEARANCE = ''
    STEOS_ID = 10071


class Tor(Actor):
    RU_NAME = MS('Тор', 'Tor')
    TYPE = ACTOR_MALE
    NAME = 'tor'
    COMM_APPEARANCE = 'ku_bartender_head_hat, ku_male_guard_body, comm_ku_kym'
    STEOS_ID = 220


class Reichman(Actor):
    RU_NAME = MS('Райхман', 'Reichmann')
    TYPE = ACTOR_MALE
    NAME = 'reichman'
    CUTSCENE_APPEARANCE = 'reichman'
    COMM_APPEARANCE = 'rh_reichman_head, rh_reichman_body, prop_neuralnet_A_right'
    SPACE_VOICE = 'pilot_f_mil_m01'
    # ru
    # STEOS_ID = 10080
    # STEOS_PITCH = -0.5
    # en
    STEOS_ID = 220
    STEOS_PITCH = -0.5


class YokohamaBarOne(Actor):
    TYPE = ACTOR_MALE
    NAME = 'char1'
    CUTSCENE_APPEARANCE = 'yoko_char1'


class YokohamaBarTwo(Actor):
    TYPE = ACTOR_MALE
    NAME = 'char2'
    CUTSCENE_APPEARANCE = 'yoko_char2'


class YokohamaBarThree(Actor):
    TYPE = ACTOR_FEMALE
    NAME = 'char3'
    CUTSCENE_APPEARANCE = 'yoko_char3'


class YokohamaBarFour(Actor):
    TYPE = ACTOR_FEMALE
    NAME = 'char4'
    CUTSCENE_APPEARANCE = 'yoko_char4'


class YokohamaBarFive(Actor):
    TYPE = ACTOR_MALE
    NAME = 'char5'
    CUTSCENE_APPEARANCE = 'yoko_char5'


class YokohamaDancer1(Actor):
    TYPE = ACTOR_MALE
    NAME = 'dancer1'
    CUTSCENE_APPEARANCE = 'yoko_dancer1'


class YokohamaDancer2(Actor):
    TYPE = ACTOR_FEMALE
    NAME = 'dancer2'
    CUTSCENE_APPEARANCE = 'yoko_dancer2'


class YokohamaDancer3(Actor):
    TYPE = ACTOR_FEMALE
    NAME = 'dancer3'
    CUTSCENE_APPEARANCE = 'yoko_dancer3'


class YokohamaDancer4(Actor):
    TYPE = ACTOR_MALE
    NAME = 'dancer4'
    CUTSCENE_APPEARANCE = 'yoko_dancer4'


class YokohamaDancer5(Actor):
    TYPE = ACTOR_MALE
    NAME = 'dancer5'
    CUTSCENE_APPEARANCE = 'yoko_dancer5'


class YokohamaTable1(Actor):
    TYPE = ACTOR_FEMALE
    NAME = 'table1'
    CUTSCENE_APPEARANCE = 'yoko_table1'


class YokohamaTable2(Actor):
    TYPE = ACTOR_FEMALE
    NAME = 'table2'
    CUTSCENE_APPEARANCE = 'yoko_table2'


class YokohamaTable3(Actor):
    TYPE = ACTOR_MALE
    NAME = 'table3'
    CUTSCENE_APPEARANCE = 'yoko_table3'


class YokohamaTable4(Actor):
    TYPE = ACTOR_MALE
    NAME = 'table4'
    CUTSCENE_APPEARANCE = 'yoko_table4'


class YokohamaTable5(Actor):
    TYPE = ACTOR_MALE
    NAME = 'table5'
    CUTSCENE_APPEARANCE = 'yoko_table5'


class YokohamaTable6(Actor):
    TYPE = ACTOR_FEMALE
    NAME = 'table6'
    CUTSCENE_APPEARANCE = 'yoko_table6'


class TekagiDj(Actor):
    TYPE = ACTOR_MALE
    NAME = 'tekagi'
    CUTSCENE_APPEARANCE = 'tekagi_dj'


class YokoDancepoint(Actor):
    TYPE = ACTOR_FEMALE
    NAME = 'yoko_dancepoint'
    CUTSCENE_APPEARANCE = 'yoko_dancepoint'


class YokoDancelook1(Actor):
    TYPE = ACTOR_MALE
    NAME = 'yoko_dancelook1'
    CUTSCENE_APPEARANCE = 'yoko_dancelook1'


class YokoDancelook2(Actor):
    TYPE = ACTOR_MALE
    NAME = 'yoko_dancelook2'
    CUTSCENE_APPEARANCE = 'yoko_dancelook2'


class YokoDancelook3(Actor):
    TYPE = ACTOR_MALE
    NAME = 'yoko_dancelook3'
    CUTSCENE_APPEARANCE = 'yoko_dancelook3'


class OrderMedic(Actor):
    TYPE = ACTOR_MALE
    NAME = 'or_medic'
    CUTSCENE_APPEARANCE = 'hochstedler'


class BartenderFixture(Actor):
    RU_NAME = MS('Стандартный бармен', 'Bartender')
    TYPE = ACTOR_MALE
    NAME = 'bartender'


class MusashiBartender(Actor):
    RU_NAME = MS('Бармен Мусаси', 'Captain')
    TYPE = ACTOR_MALE
    NAME = 'musashi_bartender'
    CUTSCENE_APPEARANCE = 'musashi_bartender'


class OsirisOfficer(Actor):
    RU_NAME = MS('Капитан', 'Captain')
    TYPE = ACTOR_FEMALE
    NAME = 'asf_captn'
    CUTSCENE_APPEARANCE = 'm8_asf_captain_visor'


class OsirisMaleElite1(Actor):
    RU_NAME = MS('Капитан', 'Captain')
    TYPE = ACTOR_MALE
    NAME = 'osiris_male_1'
    CUTSCENE_APPEARANCE = 'm13_male1'


class OsirisMaleElite2(Actor):
    RU_NAME = MS('Капитан', 'Captain')
    TYPE = ACTOR_MALE
    NAME = 'osiris_male_2'
    CUTSCENE_APPEARANCE = 'm13_male2'


class OsirisMaleElite3(Actor):
    RU_NAME = MS('Капитан', 'Captain')
    TYPE = ACTOR_MALE
    NAME = 'osiris_male_3'
    CUTSCENE_APPEARANCE = 'm13_male3'


class OsirisMaleElite4(Actor):
    RU_NAME = MS('Капитан', 'Captain')
    TYPE = ACTOR_MALE
    NAME = 'osiris_male_4'
    CUTSCENE_APPEARANCE = 'm13_male4'


class OsirisFemaleElite1(Actor):
    RU_NAME = MS('Капитан', 'Captain')
    TYPE = ACTOR_FEMALE
    NAME = 'osiris_female_1'
    CUTSCENE_APPEARANCE = 'm13_female1'


class OsirisFemaleElite2(Actor):
    RU_NAME = MS('Капитан', 'Captain')
    TYPE = ACTOR_FEMALE
    NAME = 'osiris_female_2'
    CUTSCENE_APPEARANCE = 'm13_female2'


class OsirisFemaleElite3(Actor):
    RU_NAME = MS('Капитан', 'Captain')
    TYPE = ACTOR_FEMALE
    NAME = 'osiris_female_3'
    CUTSCENE_APPEARANCE = 'm13_female3'


class OsirisFemaleElite4(Actor):
    RU_NAME = MS('Капитан', 'Captain')
    TYPE = ACTOR_FEMALE
    NAME = 'osiris_female_4'
    CUTSCENE_APPEARANCE = 'm13_female4'


class MajorScrew(Actor):
    RU_NAME = MS('Майор Скрю', 'Major Screw')
    TYPE = ACTOR_MALE
    NAME = 'major'
    CUTSCENE_APPEARANCE = 'major_screw'
    STEOS_ID = 211
    STEOS_PITCH = -0.6
    STEOS_SPEED = 1


class ActorManager:
    def __init__(self):
        self.actors_per_name = {actor.NAME: actor for actor in Actor.subclasses}

    def get_by_name(self, name):
        return self.actors_per_name[name]
