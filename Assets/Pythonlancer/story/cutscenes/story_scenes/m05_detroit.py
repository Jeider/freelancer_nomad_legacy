"""m05_detroit: полная постановка из master; точки в m05_detroit.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    AttachEvent, Character, ConnectHardpointEvent, LookAtCamera, MAIN, Male, MoveEvent, NeckIkEvent, Prop, RotateAxisEvent, StaticCamera,
)
from story.cutscenes.anim import (
    Male,
)
from story import actors


class PropBarclothWaddedBartProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'barcloth_wadded'

class PropGlassGreenProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'glass_green'


class M05DetroitScene(Scene):
    DUMP_FILE = 'm05_detroit'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Персонажи, камеры, реквизит и звук.
        prop_barcloth_wadded_bart = PropBarclothWaddedBartProp(root=self, name='Prop_barcloth_wadded_Bart',
            light_group=0, init_point='Prop_barcloth_wadded_Bart', rotate_from_quat=True)
        prop_glass_green = PropGlassGreenProp(root=self, name='Prop_glass_green', light_group=0,
            init_point='Prop_glass_green', rotate_from_quat=True)
        trent = Character(root=self, actor=actors.Trent, name='Char_trent', light_group=0,
            init_point='Char_trent', rotate_from_quat=True, appearance='trent', actor_name='Player')
        bartender = Character(root=self, actor=actors.DetroitBarman, name='Char_bartender', light_group=0,
            init_point='Char_bartender', rotate_from_quat=True, appearance='m05_barman', actor_name='m05_barman')
        bartender_fixture = Character(root=self, actor=actors.BartenderFixture, name='Char_bartender_Fixture',
            light_group=0, init_point='Char_bartender_Fixture', rotate_from_quat=True,
            appearance='li_bartender_1', actor_name='bartender')
        cam_start = LookAtCamera(root=self, name='cam_start', fov=20, look_duration=300)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=22, look_duration=300)
        cam_trent_near = LookAtCamera(root=self, name='cam_trent_near', fov=20, look_duration=300)
        cam_bartender = LookAtCamera(root=self, name='cam_bartender', fov=25, look_duration=300)
        cam_bartender_closest = LookAtCamera(root=self, name='cam_bartender_closest', fov=15, look_duration=300)
        cam_bartender_near = LookAtCamera(root=self, name='cam_bartender_near', fov=22, look_duration=300)
        cam_wlkg_trent = StaticCamera(root=self, name='cam_wlkg_trent', fov=15)

        # Исходные точки взгляда.

        # Вход.
        t = 0
        cam_start.set(group=MAIN, time_delay=t)
        ConnectHardpointEvent(root=self, group=MAIN, target_name=prop_barcloth_wadded_bart.name,
            parent_name=bartender.name, duration=512, target_hardpoint='hprightconnect_prop_barcloth_wadded',
            parent_hardpoint='hprightconnect', time_delay=t)
        cam_start.move_cam(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        cam_start.move_focus(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=9.99, time_scale=0.9, loop=True,
            time_delay=t)
        bartender.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WIPE_BAR_000LV_A_24, duration=25, time_scale=0.95,
            time_delay=t)
        t += 3
        ik_time = main_group.get_time() + t
        trent_ik = NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=51, transition_duration=2, time_delay=t)
        t += 4
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=35, axis='Y_AXIS', duration=2.99,
            smooth=True, time_delay=t)
        main_group.append_time(10)

        # m05_detroit 10: Trent.
        # Дружище, я тут одного профессора ищу, по фамилии Мандрейк. Не слышал о таком.
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('point_trent_stand'), duration=0, smooth=False, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_LEAN_BAR_TRNS_000LV_XA_02, duration=5, time_scale=0.7,
            trans_time=1, time_delay=t)
        cam_bartender.set(group=MAIN, time_delay=t)
        t += 1
        trent.facial(group=MAIN, index=10, auto_lip=True)

        # m05_detroit 20: DetroitBarman.
        # Не видел, не слышал, не разговаривал.
        t = 1.5
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_LEAN_STND_BAR_TRNS_000LV_XA_03, duration=3, time_scale=0.7,
            trans_time=1, time_delay=t)
        bartender.facial(group=MAIN, index=20, auto_lip=True)

        # m05_detroit 30: Trent.
        # А ты душка, я смотрю. А взгляни вот на это, дружище, я из профсоюза барменов.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_GIVE_VEND_000LV_B_07, duration=15, time_scale=0.7,
            time_delay=t)
        trent.facial(group=MAIN, index=30, auto_lip=True)

        # m05_detroit 40: DetroitBarman.
        # Чёрт, ты из этих... Светани-ка этой  штукой вон туда в камеру, чтобы я потом смог оправдаться.
        t = 0
        cam_bartender_near.set(group=MAIN, time_delay=0)
        bartender.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=2, time_scale=0.2,
            time_delay=t)
        t += 2
        bartender.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_GESTL_180LV_XA_02, duration=5, time_scale=0.6,
            trans_time=1, time_delay=t)
        t += 4
        bartender.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_LOOK_WATC_IMPA_315DN_XA_07, duration=4.2,
            time_scale=0.9, trans_time=1, time_delay=t)
        bartender.facial(group=MAIN, index=40, auto_lip=True)
        main_group.append_time(2)

        # m05_detroit 45: DetroitBarman.
        # Ага, спасибо. Исследовательская станция в Сигма-17.
        t = 1.2
        bartender.facial(group=MAIN, index=45, auto_lip=True)

        # m05_detroit 50: Trent.
        # Какая именно станция?
        t = 0
        cam_trent_near.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_LEAN_BAR_TRNS_000LV_XA_02, duration=5, time_scale=0.7,
            time_delay=t)
        t += 2
        ConnectHardpointEvent(root=self, group=MAIN, target_name=prop_glass_green.name,
            parent_name=bartender.name, duration=50, target_hardpoint='hpleftconnect_prop_glass_green',
            parent_hardpoint='hpleftconnect', time_delay=0)
        bartender.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_HOLDD_LEFT_000LV_00, duration=0.1, start_time=5,
            time_delay=0)
        trent.facial(group=MAIN, index=50, auto_lip=True)

        # m05_detroit 60: DetroitBarman.
        # Ис-сле-до-ва-тель-ска-я. Компренде? Странно, ваши обычно посообразительнее бывают.
        t = 0
        cam_bartender_near.set(group=MAIN, time_delay=t)

        bartender.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_CLEAN_GLAS_000LV_A_26, duration=55, time_scale=0.8,
            trans_time=0, time_delay=-1, start_time=4)
        bartender.facial(group=MAIN, index=60, auto_lip=True)

        # m05_detroit 70: Trent.
        # Ок. Спасибо за инфу. Видишь как легко растопить лед и найти взаимопонимание?
        t = 0

        cam_trent.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_LEAN_STND_BAR_TRNS_000LV_XA_03, duration=5, time_scale=0.7,
            trans_time=1, time_delay=t)

        trent_ik.set_duration(main_group.get_time() - ik_time)
        t += 5

        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_STND_WALK_TRNS_270LV_XA_02, duration=2, trans_time=1,
            time_delay=t)
        trent.facial(group=MAIN, index=70, auto_lip=True)

        main_group.append_time(1)
        t = 0
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('point_trent_walkout'), duration=0.00011, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=cam_wlkg_trent.name, parent_name=trent.name, duration=15,
            target_part='', target_type='ROOT', adjust_pos=True, adjust_orient=False, up='Y_AXIS',
            front='NEG_Z_AXIS', offset_x=0.75, offset_y=0.6, offset_z=2, time_delay=t)

        cam_wlkg_trent.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XC_01, duration=25, time_scale=0.7, loop=True,
            time_delay=t)

        # m05_detroit 80: Trent.
        # Вот чего не хватает человечеству - взаимопонимания.
        trent.facial(group=MAIN, index=80, auto_lip=True)

        main_group.append_time(2)
