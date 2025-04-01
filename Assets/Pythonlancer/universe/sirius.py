from universe import system
from universe.content import population
from universe.content import jump_effect

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
from universe.systems import rh_kgb as rh_kgb_content
from universe.systems import or_hq_static as or_hq_content
from universe.systems import rh_vien as rh_vien_content


class rh_mnh(system.RheinlandFirst, system.System, system.SiriusSystem):
    NAME = 'rh_mnh'
    TEMPLATE_NAME = 'rh_mnh'
    RU_NAME = 'Мюнхен'
    CONTENT = rh_mnh_content

    SYSTEM_FOLDER = 'RH_MUNCHEN'
    ALLOW_SYNC = True

    JUMP_EFFECT = jump_effect.Dark
    NAVMAP_POS = '10, 8.5'
    NAVMAP_SCALE = 1.8


class rh_biz(system.RheinlandFirst, system.System, system.SiriusSystem):
    NAME = 'rh_biz'
    TEMPLATE_NAME = 'rh_biz'
    RU_NAME = 'Б+исмарк'
    CONTENT = rh_biz_content

    SYSTEM_FOLDER = 'RH_BIZMARK'
    ALLOW_SYNC = True

    JUMP_EFFECT = jump_effect.Rheinland
    NAVMAP_POS = '12, 10'
    NAVMAP_SCALE = 1.5


class rh_stut(system.RheinlandFirst, system.System, system.SiriusSystem):
    NAME = 'rh_stut'
    TEMPLATE_NAME = 'rh_stut'
    RU_NAME = 'Шт+утгарт'
    CONTENT = rh_stut_content

    SYSTEM_FOLDER = 'RH_STUTTGART'
    ALLOW_SYNC = True

    JUMP_EFFECT = jump_effect.Walker
    NAVMAP_POS = '10, 12'
    NAVMAP_SCALE = 1.5


class rh_ber(system.RheinlandFirst, system.System, system.SiriusSystem):
    NAME = 'rh_ber'
    TEMPLATE_NAME = 'rh_ber'
    RU_NAME = 'Берл+ин'
    CONTENT = rh_ber_content

    SYSTEM_FOLDER = 'RH_BERLIN'
    ALLOW_SYNC = True

    JUMP_EFFECT = jump_effect.Rheinland
    NAVMAP_POS = '12, 7'
    NAVMAP_SCALE = 1.5


class sig8(system.RheinlandFirst, system.System, system.SiriusSystem):
    NAME = 'sig8'
    TEMPLATE_NAME = 'sig8'
    RU_NAME = 'С+игма-8'
    CONTENT = sig8_content

    SYSTEM_FOLDER = 'SIGMA8'
    ALLOW_SYNC = True

    JUMP_EFFECT = jump_effect.Rheinland
    NAVMAP_POS = '14, 9'
    NAVMAP_SCALE = 1.5


class om15(system.RheinlandFirst, system.System, system.SiriusSystem):
    NAME = 'om15'
    TEMPLATE_NAME = 'om15'
    RU_NAME = 'Ом+ега-15'
    CONTENT = om15_content

    SYSTEM_FOLDER = 'OMEGA15'
    ALLOW_SYNC = True

    JUMP_EFFECT = jump_effect.Walker
    NAVMAP_POS = '12, 13'
    NAVMAP_SCALE = 1.25


class sig13(system.RheinlandFirst, system.LibertySecond, system.System, system.SiriusSystem):
    NAME = 'sig13'
    TEMPLATE_NAME = 'sig13'
    RU_NAME = 'С+игма-13'
    CONTENT = sig13_content

    SYSTEM_FOLDER = 'SIGMA13'
    ALLOW_SYNC = True

    JUMP_EFFECT = jump_effect.Crow
    NAVMAP_POS = '10, 5'
    NAVMAP_SCALE = 2


class li_cal(system.LibertyFirst, system.System, system.SiriusSystem):
    NAME = 'li_cal'
    TEMPLATE_NAME = 'li_cal'
    RU_NAME = 'Калиф+орния'
    CONTENT = li_cal_content

    SYSTEM_FOLDER = 'LI_CALIFORNIA'
    ALLOW_SYNC = True

    JUMP_EFFECT = jump_effect.Crow
    NAVMAP_POS = '8.5, 3.5'
    NAVMAP_SCALE = 1.5


class sig22(system.LibertyFirst, system.BretoniaSecond, system.System, system.SiriusSystem):
    NAME = 'sig22'
    TEMPLATE_NAME = 'sig22'
    RU_NAME = 'С+игма-22'
    CONTENT = sig22_content

    SYSTEM_FOLDER = 'SIGMA22'
    ALLOW_SYNC = True

    JUMP_EFFECT = jump_effect.Dark
    NAVMAP_POS = '6.7, 4'
    NAVMAP_SCALE = 2


class li_mnh(system.LibertyFirst, system.System, system.SiriusSystem):
    NAME = 'li_mnh'
    TEMPLATE_NAME = 'li_mnh'
    RU_NAME = 'Нь+ю-Й+орк'
    CONTENT = li_mnh_content

    SYSTEM_FOLDER = 'LI_MANHATTAN'
    ALLOW_SYNC = True

    JUMP_EFFECT = jump_effect.Liberty
    NAVMAP_POS = '10, 1.5'
    NAVMAP_SCALE = 1.5


class li_for(system.LibertyFirst, system.System, system.SiriusSystem):
    NAME = 'li_for'
    TEMPLATE_NAME = 'li_for'
    RU_NAME = 'Ф+орбс'
    CONTENT = li_for_content

    SYSTEM_FOLDER = 'LI_FORBES'
    ALLOW_SYNC = True

    JUMP_EFFECT = jump_effect.Liberty
    NAVMAP_POS = '12, 4'
    NAVMAP_SCALE = 1.5


class sig17(system.LibertyFirst, system.System, system.SiriusSystem):
    NAME = 'sig17'
    TEMPLATE_NAME = 'sig17'
    RU_NAME = 'С+игма-17'
    CONTENT = sig17_content

    SYSTEM_FOLDER = 'SIGMA17'
    ALLOW_SYNC = True

    FIRST_UNLAWFUL_POPULATION_CLASS = population.CorsairAttackersPopulation

    JUMP_EFFECT = jump_effect.Liberty
    NAVMAP_POS = '14, 3'
    NAVMAP_SCALE = 1.5


class li_col(system.LibertyFirst, system.System, system.SiriusSystem):
    NAME = 'li_col'
    TEMPLATE_NAME = 'li_col'
    RU_NAME = 'Кол+умбия'
    CONTENT = li_col_content

    SYSTEM_FOLDER = 'LI_COLUMBIA'
    ALLOW_SYNC = True

    JUMP_EFFECT = jump_effect.Liberty
    NAVMAP_POS = '6.5, 0.5'
    NAVMAP_SCALE = 1.5


class tau31(system.LibertyFirst, system.System, system.SiriusSystem):
    NAME = 'tau31'
    TEMPLATE_NAME = 'tau31'
    RU_NAME = 'Т+ау-31'
    CONTENT = tau31_content

    SYSTEM_FOLDER = 'TAU31'
    ALLOW_SYNC = True

    JUMP_EFFECT = jump_effect.Edge
    NAVMAP_POS = '8.5, -1'
    NAVMAP_SCALE = 2


class br_wrw(system.BretoniaFirst, system.System, system.SiriusSystem):
    NAME = 'br_wrw'
    TEMPLATE_NAME = 'br_wrw'
    RU_NAME = 'У+орик'
    CONTENT = br_wrw_content

    SYSTEM_FOLDER = 'BR_WARWICK'
    ALLOW_SYNC = True

    JUMP_EFFECT = jump_effect.Bretonia
    NAVMAP_POS = '5, 5.5'
    NAVMAP_SCALE = 1.5


class tau29(system.BretoniaFirst, system.System, system.SiriusSystem):
    NAME = 'tau29'
    TEMPLATE_NAME = 'tau29'
    RU_NAME = 'Тау-29'
    CONTENT = tau29_content

    SYSTEM_FOLDER = 'TAU29'
    ALLOW_SYNC = True

    JUMP_EFFECT = jump_effect.Bretonia
    NAVMAP_POS = '3, 5.5'
    NAVMAP_SCALE = 1.7


class br_cam(system.BretoniaFirst, system.System, system.SiriusSystem):
    NAME = 'br_cam'
    TEMPLATE_NAME = 'br_cam'
    RU_NAME = 'К+ембридж'
    CONTENT = br_cam_content

    SYSTEM_FOLDER = 'BR_CAMBRIDGE'
    ALLOW_SYNC = True

    JUMP_EFFECT = jump_effect.Bretonia
    NAVMAP_POS = '3, 3'
    NAVMAP_SCALE = 2


class tau37(system.BretoniaFirst, system.System, system.SiriusSystem):
    NAME = 'tau37'
    TEMPLATE_NAME = 'tau37'
    RU_NAME = 'Тау-37'
    CONTENT = tau37_content

    SYSTEM_FOLDER = 'TAU37'
    ALLOW_SYNC = True

    FIRST_UNLAWFUL_POPULATION_CLASS = population.CorsairAttackersPopulation

    JUMP_EFFECT = jump_effect.Barrier
    NAVMAP_POS = '4, 0.5'
    NAVMAP_SCALE = 2


class br_avl(system.BretoniaFirst, system.System, system.SiriusSystem):
    NAME = 'br_avl'
    TEMPLATE_NAME = 'br_avl'
    RU_NAME = 'Авал+он'
    CONTENT = br_avl_content

    SYSTEM_FOLDER = 'BR_AVALON'
    ALLOW_SYNC = True

    JUMP_EFFECT = jump_effect.Bretonia
    NAVMAP_POS = '1.5, 5.5'
    NAVMAP_SCALE = 2


class sig42(system.BretoniaFirst, system.KusariSecond, system.System, system.SiriusSystem):
    NAME = 'sig42'
    TEMPLATE_NAME = 'sig42'
    RU_NAME = 'С+ириус'
    CONTENT = sig42_content

    SYSTEM_FOLDER = 'SIGMA42'
    ALLOW_SYNC = True

    JUMP_EFFECT = jump_effect.Dark
    NAVMAP_POS = '7.5, 6.5'
    NAVMAP_SCALE = 2


class tau23(system.BretoniaFirst, system.KusariSecond, system.System, system.SiriusSystem):
    NAME = 'tau23'
    TEMPLATE_NAME = 'tau23'
    RU_NAME = 'Тау-23'
    CONTENT = tau23_content

    SYSTEM_FOLDER = 'TAU23'
    ALLOW_SYNC = True

    JUMP_EFFECT = jump_effect.Barrier
    NAVMAP_POS = '1.5, 8'
    NAVMAP_SCALE = 2


class ku_ksu(system.KusariFirst, system.System, system.SiriusSystem):
    NAME = 'ku_ksu'
    TEMPLATE_NAME = 'ku_ksu'
    RU_NAME = 'Кус+ю'
    CONTENT = ku_ksu_content

    SYSTEM_FOLDER = 'KU_KYUSHU'
    ALLOW_SYNC = True

    JUMP_EFFECT = jump_effect.Kusari
    NAVMAP_POS = '3, 9'
    NAVMAP_SCALE = 1.5


class tau4(system.KusariFirst, system.System, system.SiriusSystem):
    NAME = 'tau4'
    TEMPLATE_NAME = 'tau4'
    RU_NAME = 'Тау-4'
    CONTENT = tau4_content

    SYSTEM_FOLDER = 'TAU4'
    ALLOW_SYNC = True

    FIRST_UNLAWFUL_POPULATION_CLASS = population.CorsairAttackersPopulation

    JUMP_EFFECT = jump_effect.Kusari
    NAVMAP_POS = '3, 11'
    NAVMAP_SCALE = 1.75


class ku_hns(system.KusariFirst, system.System, system.SiriusSystem):
    NAME = 'ku_hns'
    TEMPLATE_NAME = 'ku_hns'
    RU_NAME = 'Хонс+ю'
    CONTENT = ku_hns_content

    SYSTEM_FOLDER = 'KU_HONSHU'
    ALLOW_SYNC = True

    JUMP_EFFECT = jump_effect.Kusari
    NAVMAP_POS = '7.5, 8.5'
    NAVMAP_SCALE = 1.5


class ku_tgk(system.KusariFirst, system.System, system.SiriusSystem):
    NAME = 'ku_tgk'
    TEMPLATE_NAME = 'ku_tgk'
    RU_NAME = 'Ом+ега-3'
    CONTENT = ku_tgk_content

    SYSTEM_FOLDER = 'KU_TAGAKI'
    ALLOW_SYNC = True

    JUMP_EFFECT = jump_effect.Kusari
    NAVMAP_POS = '5, 9'
    NAVMAP_SCALE = 1.5


class ku_hkd(system.KusariFirst, system.System, system.SiriusSystem):
    NAME = 'ku_hkd'
    TEMPLATE_NAME = 'ku_hkd'
    RU_NAME = 'Хокк+айдо'
    CONTENT = ku_hkd_content

    SYSTEM_FOLDER = 'KU_HOKKAIDO'
    ALLOW_SYNC = True

    JUMP_EFFECT = jump_effect.Kusari
    NAVMAP_POS = '5, 11'
    NAVMAP_SCALE = 1.5


class om7(system.KusariFirst, system.RheinlandSecond, system.System, system.SiriusSystem):
    NAME = 'om7'
    TEMPLATE_NAME = 'om7'
    RU_NAME = 'Ом+ега-7'
    CONTENT = om7_content

    SYSTEM_FOLDER = 'OMEGA7'
    ALLOW_SYNC = True

    JUMP_EFFECT = jump_effect.Walker
    NAVMAP_POS = '7.5, 12'
    NAVMAP_SCALE = 2


class rh_kgb(system.RheinlandFirst, system.System, system.SiriusSystem):
    NAME = 'rh_kgb'
    TEMPLATE_NAME = 'rh_kgb'
    RU_NAME = 'К+ёнигсберг'
    CONTENT = rh_kgb_content

    SYSTEM_FOLDER = 'RH_KOENIGSBERG'
    ALLOW_SYNC = True
    ENABLE_POPULATION = False

    SCAN_JUMP = False
    JUMP_EFFECT = jump_effect.Dark
    NAVMAP_POS = '10, 7'
    NAVMAP_SCALE = 1
    VISIT = system.VISIT_STORY

#
# # GENERATED EDITION
# class or_hq_gen(system.System, system.SiriusSystem):
#     NAME = 'or_hq_gen'
#     TEMPLATE_NAME = 'or_hq'
#     RU_NAME = 'Вавил+он'
#     CONTENT = or_hq_content
#
#     SYSTEM_FOLDER = 'ORDER_HQ'
#     ALLOW_SYNC = True
#     ENABLE_POPULATION = False
#
#     JUMP_EFFECT = jump_effect.Dark
#     NAVMAP_POS = '10, 7'
#     NAVMAP_SCALE = 1
#     VISIT = system.VISIT_STORY


# # GENERATED EDITION
# class rh_vien_gen(system.System, system.SiriusSystem):
#     NAME = 'rh_vien_gen'
#     TEMPLATE_NAME = 'rh_vien'
#     RU_NAME = 'Вена'
#     CONTENT = rh_vien_content
#
#     SYSTEM_FOLDER = 'RH_VIENNA'
#     ALLOW_SYNC = True
#     ENABLE_POPULATION = False
#
#     JUMP_EFFECT = jump_effect.Dark
#     NAVMAP_POS = '10, 7'
#     NAVMAP_SCALE = 1
#     VISIT = system.VISIT_STORY


# EDGE SYSTEMS


class co_cur(system.System, system.SiriusSystem):
    NAME = 'co_cur'
    RU_NAME = 'Кюрос+ао'

    SYSTEM_FOLDER = 'CO_CURACAO'
    NAVMAP_POS = '1, 2.5'
    NAVMAP_SCALE = 1.5


class co_mad(system.System, system.SiriusSystem):
    NAME = 'co_mad'
    RU_NAME = 'Мадр+ид'

    SYSTEM_FOLDER = 'CO_MADRID'
    NAVMAP_POS = '5, 15'
    NAVMAP_SCALE = 1.5


class co_val(system.System, system.SiriusSystem):
    NAME = 'co_val'
    RU_NAME = 'Вал+енсия'

    SYSTEM_FOLDER = 'CO_VALENSIA'
    NAVMAP_POS = '5.5, 14'
    NAVMAP_SCALE = 10


class co_och(system.System, system.SiriusSystem):
    NAME = 'co_och'
    RU_NAME = 'Очо-Р+иос'

    SYSTEM_FOLDER = ''
    NAVMAP_POS = '12, 15'
    NAVMAP_SCALE = 1.25


class co_cad(system.System, system.SiriusSystem):
    NAME = 'co_cad'
    RU_NAME = 'Кад+из'

    SYSTEM_FOLDER = 'CO_OCHORIOS'
    NAVMAP_POS = '15, 6.5'
    NAVMAP_SCALE = 1.5


class om13(system.System, system.SiriusSystem):
    NAME = 'om13'
    RU_NAME = 'Ом+ега-13'

    SYSTEM_FOLDER = 'OMEGA13'
    NAVMAP_POS = '15, 13'
    NAVMAP_SCALE = 1


class tau26(system.System, system.SiriusSystem):
    NAME = 'tau26'
    RU_NAME = 'Т+ау-26'

    SYSTEM_FOLDER = 'TAU26'
    NAVMAP_POS = '-0.3, 10'
    NAVMAP_SCALE = 1.75


class om11(system.System, system.SiriusSystem):
    NAME = 'om11'
    RU_NAME = 'Ом+ега-11'

    SYSTEM_FOLDER = 'OMEGA11'
    NAVMAP_POS = '8, 14.5'
    NAVMAP_SCALE = 2


class br_uls(system.System, system.SiriusSystem):
    NAME = 'br_uls'
    RU_NAME = '+Ольстер'

    SYSTEM_FOLDER = 'BR_ULSTER'
    NAVMAP_POS = '4.5, 3'
    NAVMAP_SCALE = 1.5


class upsilon1(system.System, system.SiriusSystem):
    NAME = 'upsilon1'
    RU_NAME = 'Больш+ой +Ипсилон'

    SYSTEM_FOLDER = 'UPSILON_MAJOR'
    NAVMAP_POS = '2, 13.5'
    NAVMAP_SCALE = 2


class upsilon2(system.System, system.SiriusSystem):
    NAME = 'upsilon2'
    RU_NAME = 'М+алый +Ипсилон'

    SYSTEM_FOLDER = 'UPSILON_MINOR'
    NAVMAP_POS = '-0, 6'
    NAVMAP_SCALE = 1.25


class omicron1(system.System, system.SiriusSystem):
    NAME = 'omicron1'
    RU_NAME = 'Больш+ой Омикр+он'

    SYSTEM_FOLDER = 'OMICRON_MAJOR'
    NAVMAP_POS = '16, 3'
    NAVMAP_SCALE = 2


class omicron2(system.System, system.SiriusSystem):
    NAME = 'omicron2'
    RU_NAME = 'М+алый Омикр+он'

    SYSTEM_FOLDER = 'OMICRON_MINOR'
    NAVMAP_POS = '16, 10'
    NAVMAP_SCALE = 2


# STORY ONLY

class sphere2(system.StorySystem, system.SiriusSystem):
    NAME = 'sphere2'
    DIRECT_TEMPLATE_NAME = 'sph2_dev'
    RU_NAME = 'Сфера'

    ALLOW_SYNC = True

    SYSTEM_FOLDER = 'SPHERE2'
    NAVMAP_POS = '14.5, -1'


class sphere2_inside(system.StorySystem, system.SiriusSystem):
    NAME = 'sphere2_inside'
    DIRECT_TEMPLATE_NAME = 'sph2_inside_dev'
    RU_NAME = 'Сфера'

    ALLOW_SYNC = True

    SYSTEM_FOLDER = 'SPHERE2_INSIDE'
    NAVMAP_POS = '14.5, -1.1'


class asf_hq(system.StorySystem, system.SiriusSystem):
    NAME = 'asf_hq'
    DIRECT_TEMPLATE_NAME = 'asf_hq_dev'
    RU_NAME = 'Энтерпр+айз'

    ALLOW_SYNC = True

    SYSTEM_FOLDER = 'ASF_HQ'
    NAVMAP_POS = '14.5, -1.1'


class asf_prom(system.StorySystem, system.SiriusSystem):
    NAME = 'asf_prom'
    DIRECT_TEMPLATE_NAME = 'asf_prom_dev'
    RU_NAME = 'Промет+ей'

    ALLOW_SYNC = True

    SYSTEM_FOLDER = 'ASF_PROMETHEUS'
    NAVMAP_POS = '14.5, -1.1'


class or_hq(system.StorySystem, system.SiriusSystem):
    NAME = 'or_hq'
    DIRECT_TEMPLATE_NAME = 'or_hq_dev'
    RU_NAME = 'Вавил+он'

    ALLOW_SYNC = True

    SYSTEM_FOLDER = 'ORDER_HQ'
    NAVMAP_POS = '14.5, -1.1'


class rh_vien(system.StorySystem, system.SiriusSystem):
    NAME = 'rh_vien'
    DIRECT_TEMPLATE_NAME = 'rh_vien_dev'
    RU_NAME = 'Вена'

    ALLOW_SYNC = True

    SYSTEM_FOLDER = 'RH_VIENNA'
    NAVMAP_POS = '14.5, -1.1'


class xen(system.StorySystem, system.SiriusSystem):
    NAME = 'xen'
    DIRECT_TEMPLATE_NAME = 'xen_dev'
    RU_NAME = 'Ксеносы'

    ALLOW_SYNC = True

    SYSTEM_FOLDER = 'XENOS'
    NAVMAP_POS = '14.5, -1.1'
