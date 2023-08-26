from universe.system import *
from world.gun import *
from world.faction import *
from world.equipment import MainMiscEquip as misc
from world.equipment import Equipment
from world.ship import *


LEVEL_1 = 1
LEVEL_2 = 2
LEVEL_3 = 3

EQUIP_CLASSES_PER_LEVEL = {
    LEVEL_1: [
        Equipment.CLASS_1,
        Equipment.CLASS_4,
        Equipment.CLASS_7,
    ],
    LEVEL_2: [
        Equipment.CLASS_2,
        Equipment.CLASS_5,
        Equipment.CLASS_8,
    ],
    LEVEL_3: [
        Equipment.CLASS_3,
        Equipment.CLASS_6,
        Equipment.CLASS_9,
    ],
}


class Base(object):
    SHIPS = []
    LEVEL = None 

    GUN = None
    GUN_LEVEL = None

    ENGINE = None
    ENGINE_LEVEL = None

    POWER = None
    POWER_LEVEL = None

    SHIELD = None
    SHIELD_LEVEL = None

    REWARD_LEVEL = None

    REWARD_GUN = None
    REWARD_GUN_LEVEL = None

    REWARD_ENGINE = None
    REWARD_ENGINE_LEVEL = None

    REWARD_POWER = None
    REWARD_POWER_LEVEL = None

    REWARD_SHIELD = None
    REWARD_SHIELD_LEVEL = None

    subclasses = []

    equip_items = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    def get_ships(self):
        return self.SHIPS

    def get_gun_level(self):
        if self.GUN_LEVEL:
            return self.GUN_LEVEL
        return self.LEVEL

    def get_engine_level(self):
        if self.ENGINE_LEVEL:
            return self.ENGINE_LEVEL
        return self.LEVEL

    def get_power_level(self):
        if self.POWER_LEVEL:
            return self.POWER_LEVEL
        return self.LEVEL

    def get_shield_level(self):
        if self.SHIELD_LEVEL:
            return self.SHIELD_LEVEL
        return self.LEVEL

    def get_gun_classes(self):
        return EQUIP_CLASSES_PER_LEVEL[self.get_gun_level()]

    def get_engine_classes(self):
        return EQUIP_CLASSES_PER_LEVEL[self.get_engine_level()]

    def get_power_classes(self):
        return EQUIP_CLASSES_PER_LEVEL[self.get_power_level()]

    def get_shield_classes(self):
        return EQUIP_CLASSES_PER_LEVEL[self.get_shield_level()]



# Planet Bizmark
class Bizmark_base(Base):
    NAME = 'Bizmark_base'
    SYSTEM = rh_biz
    SHIPS = [
        Dagger,
        Dromader,
        Stiletto,
    ]

    LEVEL = LEVEL_2

    GUN = RheinlandCivgun
    ENGINE = misc.RH_CIV
    POWER = misc.RH_CIV
    SHIELD = misc.RH_CIV



# Bremen Traders
class rh_biz_02_Base(Base):
    NAME = 'rh_biz_02_Base'
    SYSTEM = rh_biz
    LEVEL = LEVEL_1

    GUN = RheinlandCivgun
    ENGINE = misc.RH_CIV
    POWER = misc.RH_CIV
    SHIELD = misc.RH_CIV


# Battleship
class rh_biz_03_Base(Base):
    NAME = 'rh_biz_03_Base'
    SYSTEM = rh_biz
    SHIPS = [
        Valkyrie,
    ]

    LEVEL = LEVEL_1
    GUN = RheinlandHeavygun
    ENGINE = misc.RH_MAIN
    POWER = misc.RH_MAIN
    SHIELD = misc.RH_MAIN


# Scient
class rh_biz_04_Base(Base):
    NAME = 'rh_biz_04_Base'
    SYSTEM = rh_biz

    LEVEL = LEVEL_1
    GUN = RheinlandShieldgun
    ENGINE = misc.RH_CIV
    POWER = misc.RH_CIV
    SHIELD = misc.RH_CIV


# Military Base (Kologne)
class rh_biz_05_Base(Base):
    NAME = 'rh_biz_05_Base'
    SYSTEM = rh_biz

    LEVEL = LEVEL_2
    GUN = RheinlandHeavygun
    ENGINE = misc.RH_MAIN
    POWER = misc.RH_MAIN
    SHIELD = misc.RH_MAIN


# West Pirates
class rh_biz_06_Base(Base):
    NAME = 'rh_biz_06_Base'
    SYSTEM = rh_biz

    LEVEL = LEVEL_1
    GUN = RheinlandHessiangun
    ENGINE = misc.RH_PIRATE
    POWER = misc.RH_PIRATE
    SHIELD = misc.RH_PIRATE


# East Pirates
class rh_biz_07_Base(Base):
    NAME = 'rh_biz_07_Base'
    SYSTEM = rh_biz

    LEVEL = LEVEL_1
    GUN = RheinlandPirategun
    ENGINE = misc.RH_PIRATE
    POWER = misc.RH_PIRATE
    SHIELD = misc.RH_PIRATE


class sig8_01_Base(Base):
    NAME = 'sig8_01_Base'
    SYSTEM = sig8


class sig8_02_Base(Base):
    NAME = 'sig8_02_Base'
    SYSTEM = sig8


class sig8_04_Base(Base):
    NAME = 'sig8_04_Base'
    SYSTEM = sig8


class om15_01_Base(Base):
    NAME = 'om15_01_Base'
    SYSTEM = om15


class om15_03_Base(Base):
    NAME = 'om15_03_Base'
    SYSTEM = om15


class om15_04_Base(Base):
    NAME = 'om15_04_Base'
    SYSTEM = om15


class om15_miner_01(Base):
    NAME = 'om15_miner_01'
    SYSTEM = om15


class om15_miner_02(Base):
    NAME = 'om15_miner_02'
    SYSTEM = om15


class om15_miner_03(Base):
    NAME = 'om15_miner_03'
    SYSTEM = om15


class rh_stut_01_Base(Base):
    NAME = 'rh_stut_01_Base'
    SYSTEM = rh_stut


class rh_stut_02_Base(Base):
    NAME = 'rh_stut_02_Base'
    SYSTEM = rh_stut


class rh_stut_03_Base(Base):
    NAME = 'rh_stut_03_Base'
    SYSTEM = rh_stut


class rh_stut_04_Base(Base):
    NAME = 'rh_stut_04_Base'
    SYSTEM = rh_stut


class rh_stut_05_Base(Base):
    NAME = 'rh_stut_05_Base'
    SYSTEM = rh_stut


class rh_stut_06_Base(Base):
    NAME = 'rh_stut_06_Base'
    SYSTEM = rh_stut


class rh_ber_01_Base(Base):
    NAME = 'rh_ber_01_Base'
    SYSTEM = rh_ber


class rh_ber_02_Base(Base):
    NAME = 'rh_ber_02_Base'
    SYSTEM = rh_ber


class rh_ber_03_Base(Base):
    NAME = 'rh_ber_03_Base'
    SYSTEM = rh_ber


class rh_ber_04_Base(Base):
    NAME = 'rh_ber_04_Base'
    SYSTEM = rh_ber


class rh_ber_05_Base(Base):
    NAME = 'rh_ber_05_Base'
    SYSTEM = rh_ber


class rh_ber_06_Base(Base):
    NAME = 'rh_ber_06_Base'
    SYSTEM = rh_ber


class rh_ber_07_Base(Base):
    NAME = 'rh_ber_07_Base'
    SYSTEM = rh_ber


class rh_ber_08_Base(Base):
    NAME = 'rh_ber_08_Base'
    SYSTEM = rh_ber


class sig13_01_Base(Base):
    NAME = 'sig13_01_Base'
    SYSTEM = sig13


class sig13_02_Base(Base):
    NAME = 'sig13_02_Base'
    SYSTEM = sig13


class sig13_03_Base(Base):
    NAME = 'sig13_03_Base'
    SYSTEM = sig13


class li_cal_01_Base(Base):
    NAME = 'li_cal_01_Base'
    SYSTEM = li_cal


class li_cal_02_Base(Base):
    NAME = 'li_cal_02_Base'
    SYSTEM = li_cal


class li_cal_03_Base(Base):
    NAME = 'li_cal_03_Base'
    SYSTEM = li_cal


class li_cal_04_Base(Base):
    NAME = 'li_cal_04_Base'
    SYSTEM = li_cal


class li_cal_05_Base(Base):
    NAME = 'li_cal_05_Base'
    SYSTEM = li_cal


class li_cal_06_Base(Base):
    NAME = 'li_cal_06_Base'
    SYSTEM = li_cal


class li_cal_07_Base(Base):
    NAME = 'li_cal_07_Base'
    SYSTEM = li_cal


class li_cal_08_Base(Base):
    NAME = 'li_cal_08_Base'
    SYSTEM = li_cal


class li_cal_09_Base(Base):
    NAME = 'li_cal_09_Base'
    SYSTEM = li_cal


class sig22_01_Base(Base):
    NAME = 'sig22_01_Base'
    SYSTEM = sig22


class sig22_02_Base(Base):
    NAME = 'sig22_02_Base'
    SYSTEM = sig22


class sig22_04_Base(Base):
    NAME = 'sig22_04_Base'
    SYSTEM = sig22

class sig42_01_Base(Base):
    NAME = 'sig42_01_Base'
    SYSTEM = sig42


class sig42_02_Base(Base):
    NAME = 'sig42_02_Base'
    SYSTEM = sig42


class li_mnh_01_Base(Base):
    NAME = 'li_mnh_01_Base'
    SYSTEM = li_mnh


class li_mnh_02_Base(Base):
    NAME = 'li_mnh_02_Base'
    SYSTEM = li_mnh


class li_mnh_03_Base(Base):
    NAME = 'li_mnh_03_Base'
    SYSTEM = li_mnh


class li_mnh_04_Base(Base):
    NAME = 'li_mnh_04_Base'
    SYSTEM = li_mnh


class li_mnh_05_Base(Base):
    NAME = 'li_mnh_05_Base'
    SYSTEM = li_mnh


class li_mnh_06_Base(Base):
    NAME = 'li_mnh_06_Base'
    SYSTEM = li_mnh


class li_mnh_07_Base(Base):
    NAME = 'li_mnh_07_Base'
    SYSTEM = li_mnh


class li_mnh_09_Base(Base):
    NAME = 'li_mnh_09_Base'
    SYSTEM = li_mnh


class li_for_01_Base(Base):
    NAME = 'li_for_01_Base'
    SYSTEM = li_for


class li_for_02_Base(Base):
    NAME = 'li_for_02_Base'
    SYSTEM = li_for


class li_for_03_Base(Base):
    NAME = 'li_for_03_Base'
    SYSTEM = li_for


class li_for_04_Base(Base):
    NAME = 'li_for_04_Base'
    SYSTEM = li_for


class li_for_05_Base(Base):
    NAME = 'li_for_05_Base'
    SYSTEM = li_for


class li_for_06_Base(Base):
    NAME = 'li_for_06_Base'
    SYSTEM = li_for


class sig17_01_Base(Base):
    NAME = 'sig17_01_Base'
    SYSTEM = sig17


class sig17_02_Base(Base):
    NAME = 'sig17_02_Base'
    SYSTEM = sig17


class sig17_03_Base(Base):
    NAME = 'sig17_03_Base'
    SYSTEM = sig17

class sig17_04_Base(Base):
    NAME = 'sig17_04_Base'
    SYSTEM = sig17

class li_col_01_Base(Base):
    NAME = 'li_col_01_Base'
    SYSTEM = li_col


class li_col_02_Base(Base):
    NAME = 'li_col_02_Base'
    SYSTEM = li_col


class li_col_03_Base(Base):
    NAME = 'li_col_03_Base'
    SYSTEM = li_col


class li_col_04_Base(Base):
    NAME = 'li_col_04_Base'
    SYSTEM = li_col


class li_col_06_Base(Base):
    NAME = 'li_col_06_Base'
    SYSTEM = li_col


class li_col_07_Base(Base):
    NAME = 'li_col_07_Base'
    SYSTEM = li_col


class Tau31_01_Base(Base):
    NAME = 'Tau31_01_Base'
    SYSTEM = tau31


class Tau31_02_Base(Base):
    NAME = 'Tau31_02_Base'
    SYSTEM = tau31


class Tau31_03_Base(Base):
    NAME = 'Tau31_03_Base'
    SYSTEM = tau31


class br_wrw_01_Base(Base):
    NAME = 'br_wrw_01_Base'
    SYSTEM = br_wrw


class br_wrw_02_Base(Base):
    NAME = 'br_wrw_02_Base'
    SYSTEM = br_wrw


class br_wrw_03_Base(Base):
    NAME = 'br_wrw_03_Base'
    SYSTEM = br_wrw


class br_wrw_04_Base(Base):
    NAME = 'br_wrw_04_Base'
    SYSTEM = br_wrw


class Tau37_01_Base(Base):
    NAME = 'Tau37_01_Base'
    SYSTEM = tau37


class Tau37_02_Base(Base):
    NAME = 'Tau37_02_Base'
    SYSTEM = tau37

class Tau37_03_Base(Base):
    NAME = 'Tau37_03_Base'
    SYSTEM = tau37

class Tau37_04_Base(Base):
    NAME = 'Tau37_04_Base'
    SYSTEM = tau37


class Tau29_01_Base(Base):
    NAME = 'Tau29_01_Base'
    SYSTEM = tau29


class Tau29_02_Base(Base):
    NAME = 'Tau29_02_Base'
    SYSTEM = tau29


class Tau29_03_Base(Base):
    NAME = 'Tau29_03_Base'
    SYSTEM = tau29

class br_cam_01_Base(Base):
    NAME = 'br_cam_01_Base'
    SYSTEM = br_cam


class br_cam_02_Base(Base):
    NAME = 'br_cam_02_Base'
    SYSTEM = br_cam


class br_cam_03_Base(Base):
    NAME = 'br_cam_03_Base'
    SYSTEM = br_cam


class br_cam_04_Base(Base):
    NAME = 'br_cam_04_Base'
    SYSTEM = br_cam


class br_cam_05_Base(Base):
    NAME = 'br_cam_05_Base'
    SYSTEM = br_cam


class br_avl_01_Base(Base):
    NAME = 'br_avl_01_Base'
    SYSTEM = br_avl


class br_avl_02_Base(Base):
    NAME = 'br_avl_02_Base'
    SYSTEM = br_avl


class br_avl_03_Base(Base):
    NAME = 'br_avl_03_Base'
    SYSTEM = br_avl


class br_avl_04_Base(Base):
    NAME = 'br_avl_04_Base'
    SYSTEM = br_avl


class br_avl_06_Base(Base):
    NAME = 'br_avl_06_Base'
    SYSTEM = br_avl


class Tau23_01_Base(Base):
    NAME = 'Tau23_01_Base'
    SYSTEM = tau23


class Tau23_02_Base(Base):
    NAME = 'Tau23_02_Base'
    SYSTEM = tau23


class Tau23_03_Base(Base):
    NAME = 'Tau23_03_Base'
    SYSTEM = tau23


class Tau23_04_Base(Base):
    NAME = 'Tau23_04_Base'
    SYSTEM = tau23


class Tau23_m7_Base(Base):
    NAME = 'Tau23_m7_Base'
    SYSTEM = tau23



class ku_ksu_01_base(Base):
    NAME = 'ku_ksu_01_base'
    SYSTEM = ku_ksu


class ku_ksu_02_base(Base):
    NAME = 'ku_ksu_02_base'
    SYSTEM = ku_ksu


class ku_ksu_03_base(Base):
    NAME = 'ku_ksu_03_base'
    SYSTEM = ku_ksu


class ku_ksu_04_base(Base):
    NAME = 'ku_ksu_04_base'
    SYSTEM = ku_ksu


class ku_ksu_05_base(Base):
    NAME = 'ku_ksu_05_base'
    SYSTEM = ku_ksu


class tau4_01_base(Base):
    NAME = 'tau4_01_base'
    SYSTEM = tau4


class tau4_02_base(Base):
    NAME = 'tau4_02_base'
    SYSTEM = tau4


class tau4_03_base(Base):
    NAME = 'tau4_03_base'
    SYSTEM = tau4


class tau4_04_base(Base):
    NAME = 'tau4_04_base'
    SYSTEM = tau4


class ku_hns_01_base(Base):
    NAME = 'ku_hns_01_base'
    SYSTEM = ku_hns


class ku_hns_02_base(Base):
    NAME = 'ku_hns_02_base'
    SYSTEM = ku_hns


class ku_hns_03_base(Base):
    NAME = 'ku_hns_03_base'
    SYSTEM = ku_hns


class ku_hns_04_base(Base):
    NAME = 'ku_hns_04_base'
    SYSTEM = ku_hns


class ku_tgk_01_base(Base):
    NAME = 'ku_tgk_01_base'
    SYSTEM = ku_tgk


class ku_tgk_02_base(Base):
    NAME = 'ku_tgk_02_base'
    SYSTEM = ku_tgk


class ku_tgk_03_base(Base):
    NAME = 'ku_tgk_03_base'
    SYSTEM = ku_tgk


class ku_tgk_04_base(Base):
    NAME = 'ku_tgk_04_base'
    SYSTEM = ku_tgk


class ku_hkd_01_base(Base):
    NAME = 'ku_hkd_01_base'
    SYSTEM = ku_hkd


class ku_hkd_02_base(Base):
    NAME = 'ku_hkd_02_base'
    SYSTEM = ku_hkd


class ku_hkd_03_base(Base):
    NAME = 'ku_hkd_03_base'
    SYSTEM = ku_hkd


class ku_hkd_06_base(Base):
    NAME = 'ku_hkd_06_base'
    SYSTEM = ku_hkd


class ku_hkd_07_base(Base):
    NAME = 'ku_hkd_07_base'
    SYSTEM = ku_hkd


class om7_01_base(Base):
    NAME = 'om7_01_base'
    SYSTEM = om7


class om7_02_base(Base):
    NAME = 'om7_02_base'
    SYSTEM = om7


class om7_03_base(Base):
    NAME = 'om7_03_base'
    SYSTEM = om7


class co_cur_01_base(Base):
    NAME = 'co_cur_01_base'
    SYSTEM = co_cur


class co_cur_02_base(Base):
    NAME = 'co_cur_02_base'
    SYSTEM = co_cur


class om2_01_base(Base):
    NAME = 'om2_01_base'
    SYSTEM = omicron2


class om2_03_base(Base):
    NAME = 'om2_03_base'
    SYSTEM = omicron2


class om2_04_base(Base):
    NAME = 'om2_04_base'
    SYSTEM = omicron2


class om1_01_base(Base):
    NAME = 'om1_01_base'
    SYSTEM = omicron1


class tau26_01_base(Base):
    NAME = 'tau26_01_base'
    SYSTEM = tau26


class tau26_02_base(Base):
    NAME = 'tau26_02_base'
    SYSTEM = tau26


class up1_01_base(Base):
    NAME = 'up1_01_base'
    SYSTEM = upsilon1


class up1_02_base(Base):
    NAME = 'up1_02_base'
    SYSTEM = upsilon1


class up1_03_base(Base):
    NAME = 'up1_03_base'
    SYSTEM = upsilon1


class co_mad_01_base(Base):
    NAME = 'co_mad_01_base'
    SYSTEM = co_mad


class co_mad_03_base(Base):
    NAME = 'co_mad_03_base'
    SYSTEM = co_mad


class co_val_01_base(Base):
    NAME = 'co_val_01_base'
    SYSTEM = co_val


class om11_01_base(Base):
    NAME = 'om11_01_base'
    SYSTEM = om11


class om11_02_base(Base):
    NAME = 'om11_02_base'
    SYSTEM = om11

class om11_03_base(Base):
    NAME = 'om11_03_base'
    SYSTEM = om11

class om11_04_base(Base):
    NAME = 'om11_04_base'
    SYSTEM = om11


class co_och_01_base(Base):
    NAME = 'co_och_01_base'
    SYSTEM = co_och


class co_och_02_base(Base):
    NAME = 'co_och_02_base'
    SYSTEM = co_och


class co_och_04_base(Base):
    NAME = 'co_och_04_base'
    SYSTEM = co_och


class up2_01_base(Base):
    NAME = 'up2_01_base'
    SYSTEM = upsilon2

class up2_02_base(Base):
    NAME = 'up2_02_base'
    SYSTEM = upsilon2

class up2_03_base(Base):
    NAME = 'up2_03_base'
    SYSTEM = upsilon2


class up2_05_base(Base):
    NAME = 'up2_05_base'
    SYSTEM = upsilon2


class co_cad_01_base(Base):
    NAME = 'co_cad_01_base'
    SYSTEM = co_cad


class co_cad_02_base(Base):
    NAME = 'co_cad_02_base'
    SYSTEM = co_cad


class co_cad_03_base(Base):
    NAME = 'co_cad_03_base'
    SYSTEM = co_cad


class co_cad_04_base(Base):
    NAME = 'co_cad_04_base'
    SYSTEM = co_cad


class om13_01_Base(Base):
    NAME = 'om13_01_Base'
    SYSTEM = om13


class om13_02_Base(Base):
    NAME = 'om13_02_Base'
    SYSTEM = om13


class br_uls_01_base(Base):
    NAME = 'br_uls_01_base'
    SYSTEM = br_uls


class br_uls_02_base(Base):
    NAME = 'br_uls_02_base'
    SYSTEM = br_uls
