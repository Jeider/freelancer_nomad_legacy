"""m05_offer_decision: постановка для ручного редактирования.

Точки: SCENES/m05_offer_decision.blend → DUMPS/m05_offer_decision.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — абсолютные секунды исходной сцены; часы MAIN не сдвигаются.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character,
    Light,
    LookAtCamera,
    MAIN,
)
from story.cutscenes.anim import (
    Female,
    Male,
)
from story.cutscenes.source_extensions import (
    preserve_entity,
)
from story import actors



class M05OfferDecisionScene(Scene):
    DUMP_FILE = 'm05_offer_decision'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        self.set_duration(50000.0)
        ambi_LtG00_Tbl_rTable4_01 = Light(root=self, name='ambi_LtG00_Tbl_rTable4/01',
            point_name='ambi_LtG00_Tbl_rTable4/01', extra_name='', light_group=5, diffuse=[1, 1, 1],
            ambient=[0.141176, 0.141176, 0.141176], direction=[0, 0, 1], light_type='L_POINT', on=True, range=451,
            cutoff=180, theta=180, color=[214, 187, 133], attenuation=[0.0099999998, 0, 5.1500000954])
        preserve_entity(ambi_LtG00_Tbl_rTable4_01)
        ambi_LtG00_Bar_Ovrhd01A = Light(root=self, name='ambi_LtG00_Bar_Ovrhd01A', point_name='ambi_LtG00_Bar_Ovrhd01A',
            extra_name='', light_group=5, diffuse=[0.596078, 0.572549, 0.403922], ambient=[0.223529, 0.2, 0.192157],
            direction=[0, 0, 1], light_type='L_POINT', on=True, range=15, cutoff=18, theta=15, color=[233, 208, 150],
            attenuation=[0.8999999762, 0, 0.006])
        preserve_entity(ambi_LtG00_Bar_Ovrhd01A)
        hatcher = Character(root=self, actor=actors.Hatcher, light_group=5, init_point='Char_hatcher',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(hatcher, template_name='hatcher', userprops={'actor': 'Hatcher', 'category': 'Character'})
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'Actor': 'Player', 'category': 'Character'})
        cam_table = LookAtCamera(root=self, name='cam_table', fov=25, farplane=5000, look_duration=300)
        preserve_entity(cam_table)

        # Действия по абсолютному времени сцены.
        t = 0
        cam_table.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=50000, loop=True)
        hatcher.motion(group=MAIN, time_delay=t, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, duration=50000, loop=True)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M05OfferDecisionScene
