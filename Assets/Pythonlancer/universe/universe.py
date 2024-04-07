from universe import system
from universe.content import population

from universe.systems import rh_ber as rh_ber_content
from universe.systems import sig13 as sig13_content
from universe.systems import rh_biz as rh_biz_content
from universe.systems import sig8 as sig8_content
from universe.systems import rh_stut as rh_stut_content
from universe.systems import om15 as om15_content
from universe.systems import rh_mnh as rh_mnh_content
from universe.systems import br_avl as br_avl_content
from universe.systems import br_cam as br_cam_content
from universe.systems import br_wrw as br_wrw_content
from universe.systems import ku_hkd as ku_hkd_content
from universe.systems import ku_hns as ku_hns_content
from universe.systems import ku_ksu as ku_ksu_content
from universe.systems import ku_tgk as ku_tgk_content
from universe.systems import li_cal as li_cal_content
from universe.systems import li_col as li_col_content
from universe.systems import li_for as li_for_content
from universe.systems import li_mnh as li_mnh_content
from universe.systems import om7 as om7_content
from universe.systems import sig17 as sig17_content
from universe.systems import sig22 as sig22_content
from universe.systems import sig42 as sig42_content
from universe.systems import tau4 as tau4_content
from universe.systems import tau23 as tau23_content
from universe.systems import tau29 as tau29_content
from universe.systems import tau31 as tau31_content
from universe.systems import tau37 as tau37_content


class rh_mnh(system.RheinlandFirst, system.System):
    NAME = 'rh_mnh'
    TEMPLATE_NAME = 'rh_mnh'
    CONTENT = rh_mnh_content

    SYSTEM_FOLDER = 'RH_MUNCHEN'
    ALLOW_SYNC = True


class rh_biz(system.RheinlandFirst, system.System):
    NAME = 'rh_biz'
    TEMPLATE_NAME = 'rh_biz'
    CONTENT = rh_biz_content

    SYSTEM_FOLDER = 'RH_BIZMARK'
    ALLOW_SYNC = True


class rh_stut(system.RheinlandFirst, system.System):
    NAME = 'rh_stut'
    TEMPLATE_NAME = 'rh_stut'
    CONTENT = rh_stut_content

    SYSTEM_FOLDER = 'RH_STUTTGART'
    ALLOW_SYNC = True


class rh_ber(system.RheinlandFirst, system.System):
    NAME = 'rh_ber'
    TEMPLATE_NAME = 'rh_ber'
    CONTENT = rh_ber_content

    SYSTEM_FOLDER = 'RH_BERLIN'
    ALLOW_SYNC = True


class sig8(system.RheinlandFirst, system.System):
    NAME = 'sig8'
    TEMPLATE_NAME = 'sig8'
    CONTENT = sig8_content

    SYSTEM_FOLDER = 'SIGMA8'
    ALLOW_SYNC = True


class om15(system.RheinlandFirst, system.System):
    NAME = 'om15'
    TEMPLATE_NAME = 'om15'
    CONTENT = om15_content

    SYSTEM_FOLDER = 'OMEGA15'
    ALLOW_SYNC = True


class sig13(system.RheinlandFirst, system.LibertySecond, system.System):
    NAME = 'sig13'
    TEMPLATE_NAME = 'sig13'
    CONTENT = sig13_content

    SYSTEM_FOLDER = 'SIGMA13'
    ALLOW_SYNC = True


class li_cal(system.LibertyFirst, system.System):
    NAME = 'li_cal'
    TEMPLATE_NAME = 'li_cal'
    CONTENT = li_cal_content

    SYSTEM_FOLDER = 'LI_CALIFORNIA'
    ALLOW_SYNC = True


class sig22(system.LibertyFirst, system.BretoniaSecond, system.System):
    NAME = 'sig22'
    TEMPLATE_NAME = 'sig22'
    CONTENT = sig22_content

    SYSTEM_FOLDER = 'SIGMA22'
    ALLOW_SYNC = True


class li_mnh(system.LibertyFirst, system.System):
    NAME = 'li_mnh'
    TEMPLATE_NAME = 'li_mnh'
    CONTENT = li_mnh_content

    SYSTEM_FOLDER = 'LI_MANHATTAN'


class li_for(system.LibertyFirst, system.System):
    NAME = 'li_for'
    TEMPLATE_NAME = 'li_for'
    CONTENT = li_for_content

    SYSTEM_FOLDER = 'LI_FORBES'
    ALLOW_SYNC = True


class sig17(system.LibertyFirst, system.System):
    NAME = 'sig17'
    TEMPLATE_NAME = 'sig17'
    CONTENT = sig17_content

    SYSTEM_FOLDER = 'SIGMA17'
    ALLOW_SYNC = True

    FIRST_UNLAWFUL_POPULATION_CLASS = population.CorsairAttackersPopulation


class li_col(system.LibertyFirst, system.System):
    NAME = 'li_col'
    TEMPLATE_NAME = 'li_col'
    CONTENT = li_col_content

    SYSTEM_FOLDER = 'LI_COLUMBIA'
    ALLOW_SYNC = True


class tau31(system.LibertyFirst, system.System):
    NAME = 'tau31'
    TEMPLATE_NAME = 'tau31'
    CONTENT = tau31_content

    SYSTEM_FOLDER = 'TAU31'
    ALLOW_SYNC = True


class br_wrw(system.BretoniaFirst, system.System):
    NAME = 'br_wrw'
    TEMPLATE_NAME = 'br_wrw'
    CONTENT = br_wrw_content

    SYSTEM_FOLDER = 'BR_WARWICK'
    ALLOW_SYNC = True


class tau29(system.BretoniaFirst, system.System):
    NAME = 'tau29'
    TEMPLATE_NAME = 'tau29'
    CONTENT = tau29_content

    SYSTEM_FOLDER = 'TAU29'
    ALLOW_SYNC = True


class br_cam(system.BretoniaFirst, system.System):
    NAME = 'br_cam'
    TEMPLATE_NAME = 'br_cam'
    CONTENT = br_cam_content

    SYSTEM_FOLDER = 'BR_CAMBRIDGE'


class tau37(system.BretoniaFirst, system.System):
    NAME = 'tau37'
    TEMPLATE_NAME = 'tau37'
    CONTENT = tau37_content

    SYSTEM_FOLDER = 'TAU37'

    FIRST_UNLAWFUL_POPULATION_CLASS = population.CorsairAttackersPopulation
    ALLOW_SYNC = True


class br_avl(system.BretoniaFirst, system.System):
    NAME = 'br_avl'
    TEMPLATE_NAME = 'br_avl'
    CONTENT = br_avl_content

    SYSTEM_FOLDER = 'BR_AVALON'


class sig42(system.BretoniaFirst, system.KusariSecond, system.System):
    NAME = 'sig42'
    TEMPLATE_NAME = 'sig42'
    CONTENT = sig42_content

    SYSTEM_FOLDER = 'SIGMA42'
    ALLOW_SYNC = True


class tau23(system.BretoniaFirst, system.KusariSecond, system.System):
    NAME = 'tau23'
    TEMPLATE_NAME = 'tau23'
    CONTENT = tau23_content

    SYSTEM_FOLDER = 'TAU23'
    ALLOW_SYNC = True


class ku_ksu(system.KusariFirst, system.System):
    NAME = 'ku_ksu'
    TEMPLATE_NAME = 'ku_ksu'
    CONTENT = ku_ksu_content

    SYSTEM_FOLDER = 'KU_KYUSHU'
    ALLOW_SYNC = True


class tau4(system.KusariFirst, system.System):
    NAME = 'tau4'
    TEMPLATE_NAME = 'tau4'
    CONTENT = tau4_content

    SYSTEM_FOLDER = 'TAU4'
    ALLOW_SYNC = True

    FIRST_UNLAWFUL_POPULATION_CLASS = population.CorsairAttackersPopulation


class ku_hns(system.KusariFirst, system.System):
    NAME = 'ku_hns'
    TEMPLATE_NAME = 'ku_hns'
    CONTENT = ku_hns_content

    SYSTEM_FOLDER = 'KU_HONSHU'
    ALLOW_SYNC = True


class ku_tgk(system.KusariFirst, system.System):
    NAME = 'ku_tgk'
    TEMPLATE_NAME = 'ku_tgk'
    CONTENT = ku_tgk_content

    SYSTEM_FOLDER = 'KU_TAGAKI'
    ALLOW_SYNC = True


class ku_hkd(system.KusariFirst, system.System):
    NAME = 'ku_hkd'
    TEMPLATE_NAME = 'ku_hkd'
    CONTENT = ku_hkd_content

    SYSTEM_FOLDER = 'KU_HOKKAIDO'
    ALLOW_SYNC = True


class om7(system.KusariFirst, system.RheinlandSecond, system.System):
    NAME = 'om7'
    TEMPLATE_NAME = 'om7'
    CONTENT = om7_content

    SYSTEM_FOLDER = 'OMEGA7'
    ALLOW_SYNC = True


class co_cur(system.System):
    NAME = 'co_cur'


class co_mad(system.System):
    NAME = 'co_mad'


class co_val(system.System):
    NAME = 'co_val'


class co_och(system.System):
    NAME = 'co_och'


class co_cad(system.System):
    NAME = 'co_cad'


class om13(system.System):
    NAME = 'om13'


class tau26(system.System):
    NAME = 'tau26'


class om11(system.System):
    NAME = 'om11'


class br_uls(system.System):
    NAME = 'br_uls'


class upsilon1(system.System):
    NAME = 'upsilon1'


class upsilon2(system.System):
    NAME = 'upsilon2'


class omicron1(system.System):
    NAME = 'omicron1'


class omicron2(system.System):
    NAME = 'omicron2'
