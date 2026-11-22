"""m05_offer_decision: полная постановка из master; точки в m05_offer_decision.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character, Female, Light, LookAtCamera, MAIN, Male, MotionEvent,
)
from story.cutscenes.anim import (
    Female, Male,
)
from story import actors


class CharTrentActor(actors.Actor):
    NAME = 'trent'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'trent'


class M05OfferDecisionScene(Scene):
    DUMP_FILE = 'm05_offer_decision'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)
        self.set_duration(50000.0)

        # Персонажи, камеры, реквизит и звук.
        ambi_ltg00_tbl_rtable4_01 = Light(root=self, name='ambi_LtG00_Tbl_rTable4/01',
            point_name='ambi_LtG00_Tbl_rTable4/01', extra_name='', light_group=5, hidden=False,
            rotate_from_quat=True, diffuse=[1, 1, 1], ambient=[0.141176, 0.141176, 0.141176], direction=[0, 0, 1],
            light_type='L_POINT', range=451, cutoff=180, theta=180, color=[214, 187, 133],
            attenuation=[0.0099999998, 0, 5.1500000954], on=True)
        ambi_ltg00_bar_ovrhd01a = Light(root=self, name='ambi_LtG00_Bar_Ovrhd01A',
            point_name='ambi_LtG00_Bar_Ovrhd01A', extra_name='', light_group=5, hidden=False,
            rotate_from_quat=True, diffuse=[0.596078, 0.572549, 0.403922], ambient=[0.223529, 0.2, 0.192157],
            direction=[0, 0, 1], light_type='L_POINT', range=15, cutoff=18, theta=15, color=[233, 208, 150],
            attenuation=[0.8999999762, 0, 0.0060000001], on=True)
        hatcher = Character(root=self, actor=actors.Hatcher, name='Char_hatcher', light_group=5,
            init_point='Char_hatcher', rotate_from_quat=True, appearance='hatcher', actor_name='Hatcher')
        trent = Character(root=self, actor=CharTrentActor, name='Char_trent', light_group=0,
            init_point='Char_trent', rotate_from_quat=True, appearance='trent', actor_name='Player')
        cam_table = LookAtCamera(root=self, name='cam_table', fov=25, look_duration=300)

        # Исходные точки взгляда.

        # Абсолютное время исходной сцены; часы MAIN не сдвигаются.
        t = 0
        cam_table.set(group=MAIN, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=trent.name, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05,
            duration=50000, loop=True, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, duration=50000, loop=True,
            time_delay=t)
